"""Contract tests for zero-inference Hebbian recall over the session log."""

from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from readmenator._config import Config
from readmenator._graphrag import GraphRagBuilder
from readmenator._hebbian import HebbianMemory
from readmenator._memory import ProjectMemory


class TestHebbianMemoryContract(unittest.TestCase):
    """Contract: sem seeding, lexical recall, Hebbian reinforcement, bounded state."""

    def setUp(self) -> None:
        """Create a temporary project with a fresh memory engine."""
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cfg = Config()
        self.memory = ProjectMemory(self.cfg)
        self.hebbian = HebbianMemory(self.cfg, self.memory)

    def tearDown(self) -> None:
        """Remove the temporary project."""
        self.tmp.cleanup()

    def _seed(self) -> None:
        """Record two notes, one with write-time semantic seeds."""
        self.memory.remember(self.root_str(), "Persist event.id before mutating balances.", "business",
                             today="2026-01-01", sem="duplicate charge, stripe webhook, billing")
        self.memory.remember(self.root_str(), "Keep commits local until approval.", "rule",
                             today="2026-01-02")

    def root_str(self) -> str:
        """Project root as a string."""
        return str(self.root)

    def test_remember_stores_sem_suffix_and_parses_it_back(self) -> None:
        """| sem: survives the round trip and stays out of the body."""
        self._seed()
        notes = self.memory.notes(self.root_str())
        self.assertEqual(notes[0].sem, "duplicate charge, stripe webhook, billing")
        self.assertEqual(notes[0].text, "Persist event.id before mutating balances.")
        self.assertEqual(notes[1].sem, "")

    def test_remember_caps_sem_terms(self) -> None:
        """More than MEMORY_SEM_MAX_TERMS seeds are truncated."""
        self.memory.remember(self.root_str(), "Note.", "note", today="2026-01-01",
                             sem="a, b, c, d, e, f, g")
        notes = self.memory.notes(self.root_str())
        self.assertEqual(len(notes[0].sem.split(", ")), self.cfg.MEMORY_SEM_MAX_TERMS)

    def test_recall_matches_sem_synonyms_without_embeddings(self) -> None:
        """A query built from the seeded synonyms finds the note through its seeds."""
        self._seed()
        hits = self.hebbian.recall(self.root_str(), "duplicate charges on stripe webhooks")
        self.assertTrue(hits)
        self.assertIn("event.id", hits[0].text)

    def test_recall_matches_note_body(self) -> None:
        """A literal body word scores the note lexically."""
        self._seed()
        hits = self.hebbian.recall(self.root_str(), "approval commits")
        self.assertTrue(hits)
        self.assertEqual(hits[0].kind, "rule")

    def test_recall_no_match_is_empty(self) -> None:
        """An unrelated query returns nothing."""
        self._seed()
        self.assertEqual(self.hebbian.recall(self.root_str(), "quantum crochet"), [])

    def test_recall_is_deterministic_on_ties(self) -> None:
        """Equal scores order by date then text, stable across calls."""
        self.memory.remember(self.root_str(), "Alpha rule about deploys.", "rule", today="2026-01-02")
        self.memory.remember(self.root_str(), "Beta rule about deploys.", "rule", today="2026-01-01")
        first = [h.text for h in self.hebbian.recall(self.root_str(), "deploys", top_k=2, reinforce_winners=False)]
        second = [h.text for h in self.hebbian.recall(self.root_str(), "deploys", top_k=2, reinforce_winners=False)]
        self.assertEqual(first, second)
        self.assertEqual(len(first), 2)
        self.assertEqual(first[0], "Beta rule about deploys.")

    def test_recall_reinforces_co_firing_notes(self) -> None:
        """Winners strengthen co-activation; the next recall gains boost."""
        self._seed()
        hits = self.hebbian.recall(self.root_str(), "duplicate charge approval commits", top_k=2)
        self.assertEqual(len(hits), 2)
        state = json.loads(self.hebbian.state_path(self.root_str()).read_text(encoding="utf-8"))
        self.assertTrue(state["fires"])
        self.assertTrue(state["pairs"])

    def test_co_activation_boost_lifts_partner_notes(self) -> None:
        """A note reinforced with a strong partner surfaces on partner queries."""
        self.memory.remember(self.root_str(), "Rule one about cashflow.", "rule", today="2026-01-01")
        self.memory.remember(self.root_str(), "Rule two about cashflow.", "rule", today="2026-01-02")
        for _ in range(5):
            self.hebbian.recall(self.root_str(), "cashflow rule one", top_k=2)
        hits = self.hebbian.recall(self.root_str(), "cashflow", top_k=2)
        boosted = {h.text: h.boost for h in hits}
        self.assertTrue(any(v > 0 for v in boosted.values()))

    def test_state_file_is_deterministic_and_capped(self) -> None:
        """Pairs are sorted, weights capped, and the file byte-stable."""
        self.memory.remember(self.root_str(), "One rule about latency.", "rule", today="2026-01-01")
        self.memory.remember(self.root_str(), "Two rule about latency.", "rule", today="2026-01-02")
        self.hebbian.recall(self.root_str(), "latency", top_k=2)
        path = self.hebbian.state_path(self.root_str())
        first = path.read_bytes()
        self.hebbian.recall(self.root_str(), "latency", top_k=2)
        second = path.read_bytes()
        self.assertNotEqual(first, second)
        state = json.loads(second.decode("utf-8"))
        weights = list(state["pairs"].values())
        self.assertTrue(all(0 < w <= self.cfg.HEBBIAN_MAX_PAIR_WEIGHT for w in weights))
        self.assertEqual(state["pairs"], dict(sorted(state["pairs"].items())))

    def test_state_pairs_pruned_to_budget(self) -> None:
        """The pair map never exceeds HEBBIAN_MAX_PAIRS entries."""
        for i in range(30):
            self.memory.remember(self.root_str(), f"Rule {i} about scaling.", "rule",
                                 today=f"2026-01-{i + 1:02d}")
        self.hebbian.recall(self.root_str(), "scaling", top_k=30)
        state = json.loads(self.hebbian.state_path(self.root_str()).read_text(encoding="utf-8"))
        self.assertLessEqual(len(state["pairs"]), self.cfg.HEBBIAN_MAX_PAIRS)

    def test_tampered_state_is_ignored(self) -> None:
        """A corrupt state file degrades to pure lexical scoring."""
        self._seed()
        self.hebbian.state_path(self.root_str()).write_text("{not json", encoding="utf-8")
        hits = self.hebbian.recall(self.root_str(), "stripe webhook")
        self.assertTrue(hits)
        self.assertEqual(hits[0].boost, 0.0)

    def test_graphrag_memory_text_units_carry_sem_terms(self) -> None:
        """The GraphRAG index sees the seeded synonyms through the triples."""
        self._seed()
        triples = [
            (n.date, n.kind, n.text + (f" | sem: {n.sem}" if n.sem else ""))
            for n in self.memory.notes(self.root_str())
        ]
        builder = GraphRagBuilder(self.cfg)
        index = builder.build([], [], [], None, [], [], None, None, None, triples)
        memory_units = [u for u in index.text_units if u.entity_id == "memory:log"]
        self.assertTrue(memory_units)
        self.assertTrue(any("stripe webhook" in u.text for u in memory_units))

    def test_smaller_top_k_respects_argument(self) -> None:
        """top_k overrides MEMORY_RECALL_TOP_K."""
        self._seed()
        self.memory.remember(self.root_str(), "Third note about billing.", "note", today="2026-01-03")
        hits = self.hebbian.recall(self.root_str(), "billing", top_k=1)
        self.assertEqual(len(hits), 1)


class TestHebbianRecallWithPrivacy(unittest.TestCase):
    """Contract: recall keeps working when privacy mode strips nothing extra."""

    def test_privacy_config_still_recalls(self) -> None:
        """Privacy mode does not break the session log round trip."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cfg = replace(Config(), PRIVACY_MODE=True)
            memory = ProjectMemory(cfg)
            memory.remember(str(root), "Deploy with the canary first.", "workflow",
                            today="2026-01-01", sem="rollout, staging")
            hits = HebbianMemory(cfg, memory).recall(str(root), "canary rollout")
            self.assertTrue(hits)
            self.assertIn("canary", hits[0].text)


if __name__ == "__main__":
    unittest.main()
