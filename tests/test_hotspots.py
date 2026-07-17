from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._hotspots import HotspotAnalyzer
from readmenator._models import Edge, Node, Symbol


class TestHotspotAnalyzerContract(unittest.TestCase):
    """Contract: HotspotAnalyzer detects hotspots, cycles, and change impact."""

    def setUp(self) -> None:
        self.config = Config()
        self.hotspots = HotspotAnalyzer(self.config)

    def _make_node(
        self, nid: str, label: str, sym_count: int = 0
    ) -> Node:
        symbols = [Symbol(name=f"f{i}", kind="function", line=i) for i in range(sym_count)]
        return Node(
            node_id=nid,
            label=label,
            kind="module",
            language="py",
            symbols=symbols,
        )

    def test_empty_graph_returns_empty_hotspots(self) -> None:
        results = self.hotspots.analyze_hotspots([], [])
        self.assertEqual(len(results), 0)

    def test_hotspots_rank_by_combined_score(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py", sym_count=10),
            self._make_node("b.py", "b.py", sym_count=1),
        ]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        results = self.hotspots.analyze_hotspots(nodes, edges)
        self.assertEqual(len(results), 2)
        self.assertGreaterEqual(results[0].combined_score, results[1].combined_score)

    def test_hotspot_includes_scores(self) -> None:
        node = self._make_node("main.py", "main.py", sym_count=5)
        results = self.hotspots.analyze_hotspots([node], [])
        self.assertEqual(len(results), 1)
        r = results[0]
        self.assertEqual(r.file_id, "main.py")
        self.assertGreaterEqual(r.complexity_score, 0)
        self.assertGreaterEqual(r.centrality_score, 0)
        self.assertEqual(r.symbol_count, 5)

    def test_no_cycles_in_acyclic_graph(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
            self._make_node("c.py", "c.py"),
        ]
        resolved = [
            Edge(source="a.py", target="b.py", relation="resolved_imports"),
            Edge(source="b.py", target="c.py", relation="resolved_imports"),
        ]
        cycles = self.hotspots.detect_cycles(nodes, resolved)
        self.assertEqual(len(cycles), 0)

    def test_detects_simple_cycle(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        resolved = [
            Edge(source="a.py", target="b.py", relation="resolved_imports"),
            Edge(source="b.py", target="a.py", relation="resolved_imports"),
        ]
        cycles = self.hotspots.detect_cycles(nodes, resolved)
        self.assertGreater(len(cycles), 0)
        self.assertGreaterEqual(cycles[0].length, 2)

    def test_change_impact_ranks_by_total_impact(self) -> None:
        nodes = [
            self._make_node("core.py", "core.py"),
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        resolved = [
            Edge(source="a.py", target="core.py", relation="resolved_imports"),
            Edge(source="b.py", target="core.py", relation="resolved_imports"),
        ]
        results = self.hotspots.analyze_change_impact(nodes, resolved)
        impact_map = {r.file_id: r.total_impact for r in results}
        self.assertGreater(impact_map.get("core.py", 0), 0)
        self.assertEqual(impact_map.get("a.py", -1), 0)

    def test_change_impact_no_edges(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        results = self.hotspots.analyze_change_impact(nodes)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].total_impact, 0)

    def test_hotspot_weights_from_config(self) -> None:
        cfg = Config(HOTSPOT_COMPLEXITY_WEIGHT=0.9, HOTSPOT_CENTRALITY_WEIGHT=0.1)
        analyzer = HotspotAnalyzer(cfg)
        node = self._make_node("main.py", "main.py", sym_count=10)
        results = analyzer.analyze_hotspots([node], [])
        self.assertAlmostEqual(results[0].complexity_score, 1.0, places=2)
