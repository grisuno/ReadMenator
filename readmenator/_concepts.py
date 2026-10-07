"""Deterministic semantic concept graph over the structural knowledge graph.

Implements the second-brain parameters as an extra layer: nouns become
concept nodes, verbs become typed edges, every sentence is decomposed
atomically into individual tokens, and each noun maps to a file set.
Zero tokens, zero network, fully deterministic.
"""

from __future__ import annotations

import logging
import re
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import ConceptGraph, ConceptNode, ConceptRelation, Edge, Node

logger = logging.getLogger(__name__)

_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*")

_CAMEL_SPLIT_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")

_VERB_BY_RELATION: Dict[str, str] = {
    "imports": "consumes",
    "resolved_imports": "depends_on",
    "calls": "invokes",
    "inherits": "extends",
}


def verb_for_relation(relation: str) -> str:
    """Return the verb label for a structural edge relation."""
    return _VERB_BY_RELATION.get(relation, "bridges")


class ConceptExtractor:
    """Builds a ConceptGraph from scanned nodes and structural edges."""

    def __init__(self, config: Config) -> None:
        """Store configuration for concept extraction budgets."""
        self._config = config
        self._stopwords = {w.lower() for w in config.CONCEPT_STOPWORDS}
        self._privacy = bool(config.PRIVACY_MODE)

    def extract(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> ConceptGraph:
        """Build concepts and verb relations from structural topology."""
        if not self._config.CONCEPT_ENABLED:
            return ConceptGraph()
        token_files: Dict[str, Set[str]] = defaultdict(set)
        token_mentions: Counter = Counter()
        for node in nodes:
            for token in self._tokens_for_node(node):
                token_files[token].add(node.node_id)
                token_mentions[token] += 1
        ranked = sorted(
            token_files.items(),
            key=lambda kv: (-len(kv[1]), -token_mentions[kv[0]], kv[0]),
        )
        selected: List[Tuple[str, Set[str]]] = []
        for name, file_ids in ranked:
            if len(file_ids) < self._config.CONCEPT_MIN_FILES:
                continue
            selected.append((name, set(file_ids)))
            if len(selected) >= self._config.CONCEPT_MAX_CONCEPTS:
                break
        concepts = [
            ConceptNode(
                name=name,
                file_ids=file_ids,
                mention_count=int(token_mentions[name]),
                confidence="EXTRACTED",
            )
            for name, file_ids in selected
        ]
        file_to_concepts: Dict[str, Set[str]] = defaultdict(set)
        for concept in concepts:
            for fid in concept.file_ids:
                file_to_concepts[fid].add(concept.name)
        relations = self._build_relations(
            list(edges) + list(resolved_edges or []), file_to_concepts
        )
        questions = self._build_dialectic(concepts, relations)
        logger.info(
            "Concept graph: %d concepts, %d relations",
            len(concepts),
            len(relations),
        )
        return ConceptGraph(
            concepts=concepts,
            relations=relations,
            dialectic_questions=questions,
        )

    def _tokens_for_node(self, node: Node) -> List[str]:
        """Return atomic noun tokens extracted from one file node."""
        parts: List[str] = [node.node_id, node.label]
        if node.doc and not self._privacy:
            parts.append(node.doc)
        for symbol in node.symbols:
            parts.append(symbol.name)
            if symbol.doc and not self._privacy:
                parts.append(symbol.doc)
        tokens: List[str] = []
        for part in parts:
            tokens.extend(self._tokenize(part))
        return tokens

    def _tokenize(self, text: str) -> List[str]:
        """Split text atomically into normalised noun tokens."""
        tokens: List[str] = []
        for raw in _TOKEN_RE.findall(text or ""):
            for chunk in _CAMEL_SPLIT_RE.split(raw):
                cleaned = chunk.lower()
                if len(cleaned) < self._config.CONCEPT_MIN_TOKEN_LEN:
                    continue
                if cleaned in self._stopwords:
                    continue
                if cleaned.isdigit():
                    continue
                tokens.append(cleaned)
        return tokens

    def _build_relations(
        self,
        edges: List[Edge],
        file_to_concepts: Dict[str, Set[str]],
    ) -> List[ConceptRelation]:
        """Aggregate structural edges into concept verb relations."""
        evidence: Dict[Tuple[str, str, str], Set[str]] = defaultdict(set)
        for edge in edges:
            verb = verb_for_relation(edge.relation)
            sources = sorted(file_to_concepts.get(edge.source, set()))
            targets = sorted(file_to_concepts.get(edge.target, set()))
            for src in sources:
                for tgt in targets:
                    if src == tgt:
                        continue
                    evidence[(src, tgt, verb)].add(
                        f"{edge.source}->{edge.target}"
                    )
        if not evidence:
            return []
        peak = max(len(v) for v in evidence.values())
        relations: List[ConceptRelation] = []
        for (src, tgt, verb), files in sorted(evidence.items()):
            strength = round(len(files) / peak, 2) if peak else 0.0
            relations.append(
                ConceptRelation(
                    source=src,
                    target=tgt,
                    verb=verb,
                    file_evidence=sorted(files)[:10],
                    strength=strength,
                    confidence="INFERRED",
                )
            )
        relations.sort(
            key=lambda r: (-r.strength, r.source, r.target, r.verb)
        )
        return relations[: self._config.CONCEPT_MAX_RELATIONS]

    def _build_dialectic(
        self,
        concepts: List[ConceptNode],
        relations: List[ConceptRelation],
    ) -> List[str]:
        """Generate deterministic thesis/antithesis/synthesis prompts."""
        questions: List[str] = []
        by_name: Dict[str, ConceptNode] = {c.name: c for c in concepts}
        verbs: Dict[Tuple[str, str], str] = {}
        for rel in relations:
            key = (rel.source, rel.target)
            if key not in verbs:
                verbs[key] = rel.verb
        names = sorted(by_name)
        for pos, first in enumerate(names):
            for second in names[pos + 1:]:
                left = by_name[first].file_ids
                right = by_name[second].file_ids
                if not left or not right:
                    continue
                shared = left & right
                union = left | right
                jaccard = len(shared) / len(union) if union else 0.0
                if len(shared) >= 2 and jaccard >= 0.3:
                    verb = verbs.get((first, second)) or verbs.get(
                        (second, first), "bridges"
                    )
                    questions.append(
                        f"Thesis: `{first}` centralizes {len(left)} files; "
                        f"Antithesis: `{second}` pulls {len(right)} files "
                        f"with {len(shared)} shared (Jaccard {jaccard:.2f}); "
                        f"Synthesis: should they merge, split by layer, "
                        f"or keep `{verb}` explicit?"
                    )
                    if len(questions) >= self._config.CONCEPT_DIALECTIC_MAX:
                        return questions
        return questions
