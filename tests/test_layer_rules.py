from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._layer_rules import LayerRuleEngine
from readmenator._models import Edge, Node


class TestLayerRuleEngineContract(unittest.TestCase):
    """Contract: LayerRuleEngine detects architectural layer violations."""

    def setUp(self) -> None:
        self.config = Config()
        self.engine = LayerRuleEngine(self.config)

    def _make_node(self, nid: str, label: str) -> Node:
        return Node(node_id=nid, label=label, kind="module", language="py")

    def test_empty_graph_returns_empty_violations(self) -> None:
        violations = self.engine.detect_violations([], [], layers={})
        self.assertEqual(len(violations), 0)

    def test_no_layers_returns_empty_violations(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        violations = self.engine.detect_violations(nodes, [], layers=None)
        self.assertEqual(len(violations), 0)

    def test_same_layer_no_violation(self) -> None:
        nodes = [self._make_node("a.py", "a.py"), self._make_node("b.py", "b.py")]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        layers = {"a.py": "testing", "b.py": "testing"}
        violations = self.engine.detect_violations(nodes, edges, layers=layers)
        self.assertEqual(len(violations), 0)

    def test_forbidden_edge_detected(self) -> None:
        nodes = [self._make_node("a.py", "a.py"), self._make_node("b.py", "b.py")]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        layers = {"a.py": "testing", "b.py": "infrastructure"}
        violations = self.engine.detect_violations(nodes, edges, layers=layers)
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].severity, "strict")
        self.assertEqual(violations[0].source_layer, "testing")
        self.assertEqual(violations[0].target_layer, "infrastructure")

    def test_multiple_violations(self) -> None:
        nodes = [
            self._make_node("test.py", "test.py"),
            self._make_node("db.py", "db.py"),
            self._make_node("ui.py", "ui.py"),
        ]
        edges = [
            Edge(source="test.py", target="db.py", relation="imports"),
            Edge(source="test.py", target="ui.py", relation="imports"),
        ]
        layers = {
            "test.py": "testing",
            "db.py": "data_access",
            "ui.py": "presentation",
        }
        violations = self.engine.detect_violations(nodes, edges, layers=layers)
        self.assertEqual(len(violations), 2)

    def test_utility_layer_ignored(self) -> None:
        nodes = [self._make_node("a.py", "a.py"), self._make_node("b.py", "b.py")]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        layers = {"a.py": "utility", "b.py": "testing"}
        violations = self.engine.detect_violations(nodes, edges, layers=layers)
        self.assertEqual(len(violations), 0)

    def test_violation_summary(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
            self._make_node("c.py", "c.py"),
        ]
        edges = [
            Edge(source="a.py", target="b.py", relation="imports"),
            Edge(source="c.py", target="b.py", relation="imports"),
        ]
        layers = {
            "a.py": "testing",
            "b.py": "infrastructure",
            "c.py": "testing",
        }
        violations = self.engine.detect_violations(nodes, edges, layers=layers)
        summary = self.engine.violation_summary(violations)
        self.assertIn("strict", summary)
        self.assertEqual(summary["strict"], 2)

    def test_resolved_edges_also_checked(self) -> None:
        nodes = [self._make_node("a.py", "a.py"), self._make_node("b.py", "b.py")]
        resolved = [
            Edge(source="a.py", target="b.py", relation="resolved_imports"),
        ]
        layers = {"a.py": "testing", "b.py": "infrastructure"}
        violations = self.engine.detect_violations(
            nodes, [], resolved_edges=resolved, layers=layers
        )
        self.assertEqual(len(violations), 1)
