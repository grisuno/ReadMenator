"""Zero-inference recall over the preserved session log, hebbmesh style.

MEMORY.md notes become recallable in under a millisecond with zero
embeddings and zero LLM calls:

- Write-time semantic seeding: ``readmenator . remember "<note>" --sem
  "synonym, synonym"`` stores 3-5 explicit synonyms as a ``| sem:``
  suffix. They act as high-weight dendrites, so a query in different
  words still finds the note (no embedding model needed).
- Hebbian reinforcement: every recall strengthens the co-activation
  weights between the notes that fired together ("cells that fire
  together wire together"). Weights live in MEMORY_STATE.json next to
  MEMORY.md and persist across sessions; nothing is inferred, only
  counted.
- Recall = lexical base score (note body + seeded synonyms) plus a
  saturating boost from co-activation with every primed note, so the
  graph of past recalls guides retrieval without any model.

The state file is deterministic JSON (sorted keys, capped pairs), lives
inside the agent output directory the scanner already skips, and is
bounded by configuration so it can never grow without limit.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._memory import MemoryNote, ProjectMemory, split_sem

logger = logging.getLogger(__name__)

_TOKEN_RE = re.compile(r"[a-z0-9_]+")


@dataclass(frozen=True)
class RecallHit:
    """One scored memory note.

    Attributes:
        date: ISO date of the note.
        kind: Note kind.
        text: Note body (without the sem suffix).
        sem: Write-time semantic seeds ("" when absent).
        base: Lexical score from body + seeds.
        boost: Hebbian co-activation boost added on top of base.
        fire_count: Times this note has been a recall winner before.
        score: Final score (base + boost), the sort key.
    """

    date: str
    kind: str
    text: str
    sem: str
    base: float
    boost: float
    fire_count: int
    score: float

    def line(self) -> str:
        """Render the hit as one greppable line."""
        seed = f" | sem: {self.sem}" if self.sem else ""
        return (
            f"[{self.kind}] {self.date} ({self.score:.2f}, fires={self.fire_count}) "
            f"{self.text}{seed}"
        )


class HebbianMemory:
    """Recall and Hebbian reinforcement over MEMORY.md session notes."""

    def __init__(self, config: Config, memory: Optional[ProjectMemory] = None) -> None:
        """Store configuration and the memory reader.

        Args:
            config: MEMORY_*/HEBBIAN_* settings and output directories.
            memory: Project memory reader (defaults to a fresh one).
        """
        self._config = config
        self._memory = memory or ProjectMemory(config)

    def state_path(self, project_root: str) -> Path:
        """Return the co-activation state file location."""
        return Path(project_root) / self._config.AGENT_OUTPUT_DIR / self._config.MEMORY_STATE_FILENAME

    def _load_state(self, project_root: str) -> Tuple[Dict[str, int], Dict[str, int]]:
        """Load (pairs, fires) from the state file, tolerating any problem."""
        path = self.state_path(project_root)
        if path.is_symlink() or not path.is_file():
            return {}, {}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}, {}
        pairs = data.get("pairs", {})
        fires = data.get("fires", {})
        if not isinstance(pairs, dict) or not isinstance(fires, dict):
            return {}, {}
        clean_pairs = {}
        for key, value in pairs.items():
            if isinstance(key, str) and isinstance(value, int) and value > 0:
                clean_pairs[key] = min(value, self._config.HEBBIAN_MAX_PAIR_WEIGHT)
        clean_fires = {}
        for key, value in fires.items():
            if isinstance(key, str) and isinstance(value, int) and value > 0:
                clean_fires[key] = min(value, self._config.HEBBIAN_FIRE_CAP)
        return clean_pairs, clean_fires

    def _save_state(self, project_root: str, pairs: Dict[str, int], fires: Dict[str, int]) -> None:
        """Write the deterministic, capped state file."""
        path = self.state_path(project_root)
        if path.is_symlink():
            logger.warning("Refusing to write through symlink: %s", path)
            return
        capped = dict(sorted(pairs.items(), key=lambda kv: (-kv[1], kv[0]))[: self._config.HEBBIAN_MAX_PAIRS])
        capped_fires = {key: value for key, value in sorted(fires.items()) if value > 0}
        payload = {"schema_version": 1, "pairs": capped, "fires": capped_fires}
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        except OSError:
            logger.warning("Could not write Hebbian state: %s", path, exc_info=True)

    def reinforce(self, project_root: str, winners: List[MemoryNote]) -> None:
        """Strengthen co-activation between the notes that fired together.

        Args:
            project_root: Project root directory.
            winners: Notes selected by the last recall, in score order.
        """
        if not winners:
            return
        pairs, fires = self._load_state(project_root)
        keys = [self._note_key(note) for note in winners]
        for key in keys:
            fires[key] = fires.get(key, 0) + 1
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                pair = f"{a}|{b}" if a < b else f"{b}|{a}"
                pairs[pair] = min(pairs.get(pair, 0) + 1, self._config.HEBBIAN_MAX_PAIR_WEIGHT)
        self._save_state(project_root, pairs, fires)

    def recall(
        self, project_root: str, query: str, top_k: int = 0, reinforce_winners: bool = True,
    ) -> List[RecallHit]:
        """Score notes against the query and reinforce the winners.

        Base score: unique query tokens found in the note body count 1.0
        each, tokens found in the ``| sem:`` seeds count MEMORY_SEM_WEIGHT
        each (seeded dendrites fire easier). Hebbian boost: every note
        that shares co-activation history with a primed note (any note
        with base > 0) gains a saturating MEMORY_HEBBIAN_BOOST * w/(w+k)
        per such neighbour, so notes that repeatedly proved useful
        together surface first without any model.

        Args:
            project_root: Project root directory.
            query: Free-text query (any language).
            top_k: Winners kept; 0 uses MEMORY_RECALL_TOP_K.
            reinforce_winners: Whether the winners strengthen the graph.

        Returns:
            Scored hits, best first, only notes with score > 0.
        """
        cfg = self._config
        limit = top_k or cfg.MEMORY_RECALL_TOP_K
        query_tokens = set(self._tokenize(query))
        if not query_tokens:
            return []
        pairs, fires = self._load_state(project_root)
        base_hits: List[Tuple[MemoryNote, float]] = []
        for note in self._memory.notes(project_root):
            base = self._base_score(note, query_tokens)
            if base > 0.0:
                base_hits.append((note, base))
        if not base_hits:
            return []
        primed = {self._note_key(note) for note, _score in base_hits}
        hits: List[RecallHit] = []
        for note, base in base_hits:
            key = self._note_key(note)
            boost = 0.0
            for other in primed:
                if other == key:
                    continue
                pair = f"{key}|{other}" if key < other else f"{other}|{key}"
                weight = pairs.get(pair, 0)
                if weight:
                    boost += cfg.HEBBIAN_BOOST * weight / (weight + cfg.HEBBIAN_SATURATION)
            count = fires.get(key, 0)
            score = base + boost
            hits.append(RecallHit(note.date, note.kind, note.text, note.sem, base, boost, count, score))
        hits.sort(key=lambda h: (-h.score, h.date, h.text))
        winners = hits[:limit]
        if reinforce_winners and winners:
            self.reinforce(
                project_root,
                [MemoryNote(h.date, h.kind, h.text, h.sem) for h in winners],
            )
        return winners

    def _base_score(self, note: MemoryNote, query_tokens: set) -> float:
        """Lexical overlap of the query with the note body and seeds."""
        cfg = self._config
        body_tokens = set(self._tokenize(f"{note.kind} {note.text}"))
        sem_tokens = set(self._tokenize(note.sem))
        score = 0.0
        for token in query_tokens:
            if token in sem_tokens:
                score += cfg.MEMORY_SEM_WEIGHT
            elif token in body_tokens:
                score += 1.0
        return score

    @staticmethod
    def _note_key(note: MemoryNote) -> str:
        """Stable key for one note inside the state file."""
        body, _sem = split_sem(note.text)
        return f"{note.date}|{note.kind}|{body[:80]}"

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Lowercase alphanumeric tokens with length at least 2."""
        return [token for token in _TOKEN_RE.findall(str(text).lower()) if len(token) >= 2]
