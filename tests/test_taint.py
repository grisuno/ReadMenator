from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol
from readmenator._taint import TaintAnalyzer


class TestTaintAnalyzerContract(unittest.TestCase):
    """Contract: TaintAnalyzer discovers taint propagation paths."""

    def setUp(self) -> None:
        self.config = Config()
        self.taint = TaintAnalyzer(self.config)

    def _make_node(self, nid: str, label: str) -> Node:
        return Node(node_id=nid, label=label, kind="module", language="py")

    def test_empty_graph_returns_empty_result(self) -> None:
        result = self.taint.analyze([], [])
        self.assertEqual(len(result.paths), 0)
        self.assertEqual(result.source_count, 0)

    def test_no_dangerous_imports_returns_empty(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges = [Edge(source="main.py", target="os.path", relation="imports")]
        result = self.taint.analyze(nodes, edges)
        self.assertEqual(len(result.paths), 0)

    def test_direct_dangerous_import_found(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges = [Edge(source="main.py", target="subprocess", relation="imports")]
        result = self.taint.analyze(nodes, edges)
        self.assertGreater(len(result.paths), 0)
        self.assertEqual(result.source_count, 1)

    def test_taint_propagates_through_resolved_edges(self) -> None:
        nodes = [
            self._make_node("danger.py", "danger.py"),
            self._make_node("middle.py", "middle.py"),
            self._make_node("sink.py", "sink.py"),
        ]
        edges = [Edge(source="danger.py", target="subprocess", relation="imports")]
        resolved = [
            Edge(
                source="danger.py",
                target="middle.py",
                relation="resolved_imports",
            ),
            Edge(
                source="middle.py",
                target="sink.py",
                relation="resolved_imports",
            ),
        ]
        result = self.taint.analyze(nodes, edges, resolved)
        self.assertGreater(len(result.paths), 0)
        sink_found = any(p.sink_file == "sink.py" for p in result.paths)
        self.assertTrue(sink_found)

    def test_dangerous_import_by_language(self) -> None:
        nodes = [self._make_node("danger.js", "danger.js")]
        edges = [
            Edge(source="danger.js", target="child_process.exec", relation="imports")
        ]
        result = self.taint.analyze(nodes, edges)
        self.assertGreater(len(result.paths), 0)

    def test_taint_path_has_severity(self) -> None:
        nodes = [self._make_node("danger.py", "danger.py")]
        edges = [Edge(source="danger.py", target="os.system", relation="imports")]
        result = self.taint.analyze(nodes, edges)
        self.assertGreater(len(result.paths), 0)
        self.assertEqual(result.paths[0].severity, "critical")

    def test_max_depth_limits_propagation(self) -> None:
        cfg = Config(TAINT_MAX_DEPTH=1)
        taint = TaintAnalyzer(cfg)
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
            self._make_node("c.py", "c.py"),
        ]
        edges = [Edge(source="a.py", target="subprocess", relation="imports")]
        resolved = [
            Edge(source="a.py", target="b.py", relation="resolved_imports"),
            Edge(source="b.py", target="c.py", relation="resolved_imports"),
        ]
        result = taint.analyze(nodes, edges, resolved)
        deep_sinks = [p for p in result.paths if p.hops > 1]
        self.assertEqual(len(deep_sinks), 0)
