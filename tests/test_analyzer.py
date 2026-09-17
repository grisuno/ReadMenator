"""Contract tests for the GraphAnalyzer.

Validates community detection, god node computation, surprising
connection discovery, and suggested question generation.
"""

from __future__ import annotations

import unittest

from readmenator._analyzer import GraphAnalyzer
from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol


class TestGraphAnalyzerContract(unittest.TestCase):
    """Contract: GraphAnalyzer provides graph intelligence."""

    def setUp(self) -> None:
        self.config = Config()
        self.analyzer = GraphAnalyzer(self.config)

    def _make_node(self, nid: str, label: str, lang: str = "py") -> Node:
        return Node(node_id=nid, label=label, kind="module", language=lang)

    def _make_edge(self, src: str, tgt: str, rel: str = "imports") -> Edge:
        return Edge(source=src, target=tgt, relation=rel)

    def test_analyze_empty_graph_returns_empty_result(self) -> None:
        result = self.analyzer.analyze([], [])
        self.assertEqual(result.node_count, 0)
        self.assertEqual(result.edge_count, 0)

    def test_analyze_detects_communities_for_connected_graph(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
            self._make_node("c.py", "c.py"),
        ]
        edges = [
            self._make_edge("a.py", "b.py"),
            self._make_edge("b.py", "c.py"),
            self._make_edge("a.py", "c.py"),
        ]
        result = self.analyzer.analyze(nodes, edges)
        self.assertGreaterEqual(len(result.communities), 1)

    def test_analyze_computes_god_nodes(self) -> None:
        nodes = [
            self._make_node("hub.py", "hub.py"),
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        edges = [
            self._make_edge("a.py", "hub.py"),
            self._make_edge("b.py", "hub.py"),
            self._make_edge("hub.py", "a.py"),
        ]
        result = self.analyzer.analyze(nodes, edges)
        self.assertGreater(len(result.god_nodes), 0)
        top_node = result.god_nodes[0][0]
        self.assertEqual(top_node, "hub.py")

    def test_analyze_finds_surprising_connections(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
            self._make_node("c.py", "c.py"),
            self._make_node("d.py", "d.py"),
            self._make_node("e.py", "e.py"),
        ]
        edges = [
            self._make_edge("a.py", "b.py"),
            self._make_edge("b.py", "c.py"),
            self._make_edge("c.py", "d.py"),
            self._make_edge("d.py", "e.py"),
        ]
        result = self.analyzer.analyze(nodes, edges)
        self.assertIsNotNone(result.surprising_connections)

    def test_analyze_generates_questions(self) -> None:
        nodes = [
            self._make_node("main.py", "main.py"),
            self._make_node("utils.py", "utils.py"),
        ]
        edges = [
            self._make_edge("main.py", "utils.py"),
        ]
        result = self.analyzer.analyze(nodes, edges)
        self.assertTrue(len(result.suggested_questions) > 0)

    def test_community_cohesion_is_between_zero_and_one(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
            self._make_node("c.py", "c.py"),
        ]
        edges = [
            self._make_edge("a.py", "b.py"),
            self._make_edge("b.py", "c.py"),
        ]
        result = self.analyzer.analyze(nodes, edges)
        for c in result.communities:
            self.assertGreaterEqual(c.cohesion, 0.0)
            self.assertLessEqual(c.cohesion, 1.0)

    def test_isolated_nodes_do_not_form_communities(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        edges: list = []
        result = self.analyzer.analyze(nodes, edges)
        self.assertEqual(len(result.communities), 0)

    def test_analyze_with_resolved_edges_counts_them(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        edges = [
            self._make_edge("a.py", "b.py", "resolved_imports"),
        ]
        resolved = [
            Edge(source="a.py", target="b.py", relation="resolved_imports"),
        ]
        result = self.analyzer.analyze(nodes, edges, resolved)
        self.assertEqual(result.edge_count, 2)

    def test_analyze_is_repeatable(self) -> None:
        nodes = [self._make_node(f"n{i}.py", f"n{i}.py") for i in range(12)]
        edges = [self._make_edge(f"n{i}.py", f"n{(i + 1) % 12}.py") for i in range(12)]
        edges += [self._make_edge("n0.py", "n6.py"), self._make_edge("n3.py", "n9.py")]
        first = self.analyzer.analyze(nodes, edges)
        second = self.analyzer.analyze(nodes, edges)
        first_comms = sorted(sorted(c.file_ids) for c in first.communities)
        second_comms = sorted(sorted(c.file_ids) for c in second.communities)
        self.assertEqual(first_comms, second_comms)
        self.assertEqual(first.surprising_connections, second.surprising_connections)

    def test_dominant_directory_prefers_specific_on_tie(self) -> None:
        from readmenator._analyzer import dominant_directory
        self.assertEqual(
            dominant_directory({"a.c", "b.c", "sandbox/c.c", "sandbox/d.c"}),
            "sandbox",
        )
        self.assertEqual(dominant_directory({"a.c"}), "root")
        self.assertEqual(dominant_directory(set()), "root")
        self.assertEqual(
            dominant_directory({"src/a.c", "src/b.c", "lib/c.c"}),
            "src",
        )


if __name__ == "__main__":
    unittest.main()
