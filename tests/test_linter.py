"""Contract tests for the ArchitectureLinter.

Validates file length checks, cross-layer violation detection,
and circular dependency identification.
"""

from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._linter import ArchitectureLinter
from readmenator._models import Edge, Node, Symbol


class TestArchitectureLinterContract(unittest.TestCase):
    """Contract: ArchitectureLinter enforces architectural rules."""

    def setUp(self) -> None:
        self.config = Config()
        self.linter = ArchitectureLinter(self.config)

    def _make_node(self, nid: str, label: str, lang: str = "py") -> Node:
        return Node(node_id=nid, label=label, kind="module", language=lang)

    def _make_edge(self, src: str, tgt: str, rel: str = "imports") -> Edge:
        return Edge(source=src, target=tgt, relation=rel)

    def test_lint_empty_graph_returns_no_violations(self) -> None:
        violations = self.linter.lint([], [])
        self.assertEqual(len(violations), 0)

    def test_lint_returns_empty_for_files_under_threshold(self) -> None:
        nodes = [self._make_node("small.py", "small.py")]
        content_map = {"small.py": "line1\nline2\nline3\n"}
        violations = self.linter.lint(nodes, [], content_map=content_map)
        length_violations = [v for v in violations if v.rule_id == "ARC001"]
        self.assertEqual(len(length_violations), 0)

    def test_lint_detects_file_exceeding_max_lines(self) -> None:
        nodes = [self._make_node("big.py", "big.py")]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        violations = self.linter.lint(nodes, [], content_map=content_map)
        length_violations = [v for v in violations if v.rule_id == "ARC001"]
        self.assertEqual(len(length_violations), 1)
        self.assertEqual(length_violations[0].severity, "warning")

    def test_lint_detects_cross_layer_violation(self) -> None:
        nodes = [
            self._make_node("ui/view.py", "view.py"),
            self._make_node("data/repo.py", "repo.py"),
        ]
        edges = [self._make_edge("ui/view.py", "data/repo.py")]
        layers = {"ui/view.py": "presentation", "data/repo.py": "data_access"}
        violations = self.linter.lint(nodes, edges, layers=layers)
        cross_layer = [v for v in violations if v.rule_id == "ARC002"]
        self.assertGreater(len(cross_layer), 0)
        self.assertEqual(cross_layer[0].severity, "error")

    def test_lint_allows_same_layer_imports(self) -> None:
        nodes = [
            self._make_node("ui/a.py", "a.py"),
            self._make_node("ui/b.py", "b.py"),
        ]
        edges = [self._make_edge("ui/a.py", "ui/b.py")]
        layers = {"ui/a.py": "presentation", "ui/b.py": "presentation"}
        violations = self.linter.lint(nodes, edges, layers=layers)
        cross_layer = [v for v in violations if v.rule_id == "ARC002"]
        self.assertEqual(len(cross_layer), 0)

    def test_lint_allows_testing_to_business_logic(self) -> None:
        nodes = [
            self._make_node("tests/test_x.py", "test_x.py"),
            self._make_node("services/svc.py", "svc.py"),
        ]
        edges = [self._make_edge("tests/test_x.py", "services/svc.py")]
        layers = {"tests/test_x.py": "testing", "services/svc.py": "business_logic"}
        violations = self.linter.lint(nodes, edges, layers=layers)
        cross_layer = [v for v in violations if v.rule_id == "ARC002"]
        self.assertEqual(len(cross_layer), 0)

    def test_lint_ignores_utility_layer(self) -> None:
        nodes = [
            self._make_node("ui/view.py", "view.py"),
            self._make_node("util/helpers.py", "helpers.py"),
        ]
        edges = [self._make_edge("ui/view.py", "util/helpers.py")]
        layers = {"ui/view.py": "presentation", "util/helpers.py": "utility"}
        violations = self.linter.lint(nodes, edges, layers=layers)
        cross_layer = [v for v in violations if v.rule_id == "ARC002"]
        self.assertEqual(len(cross_layer), 0)

    def test_lint_detects_circular_dependencies(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        resolved = [
            Edge(source="a.py", target="b.py", relation="resolved_imports"),
            Edge(source="b.py", target="a.py", relation="resolved_imports"),
        ]
        layers = {"a.py": "business_logic", "b.py": "business_logic"}
        violations = self.linter.lint(nodes, [], resolved_edges=resolved, layers=layers)
        circular = [v for v in violations if v.rule_id == "ARC003"]
        self.assertGreater(len(circular), 0)

    def test_violations_sorted_by_severity(self) -> None:
        nodes = [
            self._make_node("ui/view.py", "view.py"),
            self._make_node("data/repo.py", "repo.py"),
        ]
        edges = [self._make_edge("ui/view.py", "data/repo.py")]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"ui/view.py": content, "data/repo.py": "x\n"}
        layers = {"ui/view.py": "presentation", "data/repo.py": "data_access"}
        violations = self.linter.lint(nodes, edges, layers=layers, content_map=content_map)
        severities = [v.severity for v in violations]
        self.assertEqual(severities, sorted(severities, key=lambda s: ("error", "warning", "info").index(s) if s in ("error", "warning", "info") else 3))

    def test_lint_returns_empty_when_disabled(self) -> None:
        config = Config(LINTER_MAX_LINES=999999)
        linter = ArchitectureLinter(config)
        nodes = [self._make_node("big.py", "big.py")]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        violations = linter.lint(nodes, [], content_map=content_map)
        length_violations = [v for v in violations if v.rule_id == "ARC001"]
        self.assertEqual(len(length_violations), 0)


if __name__ == "__main__":
    unittest.main()
