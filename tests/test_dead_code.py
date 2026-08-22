"""Contract tests for the DeadCodeStripper.

Validates dead code detection, in-degree computation, entry point
exclusion, and recommendation classification.
"""

from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._dead_code import DeadCodeStripper
from readmenator._models import Edge, Node, Symbol


class TestDeadCodeStripperContract(unittest.TestCase):
    """Contract: DeadCodeStripper identifies orphaned symbols."""

    def setUp(self) -> None:
        self.config = Config()
        self.stripper = DeadCodeStripper(self.config)

    def _make_symbol(self, name: str, kind: str = "function") -> Symbol:
        return Symbol(name=name, kind=kind, line=1)

    def _make_node(self, nid: str, symbols: list = None) -> Node:
        return Node(
            node_id=nid,
            label=nid.split("/")[-1],
            kind="module",
            language="py",
            symbols=symbols or [],
        )

    def _make_edge(self, src: str, tgt: str) -> Edge:
        return Edge(source=src, target=tgt, relation="resolved_imports")

    def test_identify_empty_graph_returns_empty(self) -> None:
        reports = self.stripper.identify([], [])
        self.assertEqual(len(reports), 0)

    def test_identify_finds_dead_symbol(self) -> None:
        nodes = [
            self._make_node("a.py", [self._make_symbol("unused_func")]),
            self._make_node("b.py", [self._make_symbol("used_func")]),
        ]
        resolved = [self._make_edge("a.py", "b.py")]
        reports = self.stripper.identify(nodes, [], resolved_edges=resolved)
        dead_names = [r.symbol_name for r in reports]
        self.assertIn("unused_func", dead_names)
        self.assertNotIn("used_func", dead_names)

    def test_identify_excludes_entry_points(self) -> None:
        nodes = [
            self._make_node("main.py", [self._make_symbol("main")]),
        ]
        reports = self.stripper.identify(nodes, [])
        dead_names = [r.symbol_name for r in reports]
        self.assertNotIn("main", dead_names)

    def test_identify_excludes_app_entry_point(self) -> None:
        nodes = [
            self._make_node("app.py", [self._make_symbol("app")]),
        ]
        reports = self.stripper.identify(nodes, [])
        dead_names = [r.symbol_name for r in reports]
        self.assertNotIn("app", dead_names)

    def test_identify_excludes_init_entry_point(self) -> None:
        nodes = [
            self._make_node("__init__.py", [self._make_symbol("__init__")]),
        ]
        reports = self.stripper.identify(nodes, [])
        dead_names = [r.symbol_name for r in reports]
        self.assertNotIn("__init__", dead_names)

    def test_identify_recommends_review_for_classes(self) -> None:
        nodes = [
            self._make_node("a.py", [self._make_symbol("DeadClass", "class")]),
        ]
        reports = self.stripper.identify(nodes, [])
        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0].recommendation, "REVIEW")

    def test_identify_recommends_trash_for_functions(self) -> None:
        nodes = [
            self._make_node("a.py", [self._make_symbol("dead_func", "function")]),
        ]
        reports = self.stripper.identify(nodes, [])
        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0].recommendation, "MOVE_TO_TRASH")

    def test_identify_recommends_trash_for_variables(self) -> None:
        nodes = [
            self._make_node("a.py", [self._make_symbol("UNUSED_VAR", "variable")]),
        ]
        reports = self.stripper.identify(nodes, [])
        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0].recommendation, "MOVE_TO_TRASH")

    def test_all_symbols_imported_returns_empty(self) -> None:
        nodes = [
            self._make_node("a.py", [self._make_symbol("func_a")]),
            self._make_node("b.py", [self._make_symbol("func_b")]),
        ]
        resolved = [
            self._make_edge("a.py", "b.py"),
            self._make_edge("b.py", "a.py"),
        ]
        reports = self.stripper.identify(nodes, [], resolved_edges=resolved)
        self.assertEqual(len(reports), 0)

    def test_reports_sorted_by_file_path(self) -> None:
        nodes = [
            self._make_node("z.py", [self._make_symbol("z_func")]),
            self._make_node("a.py", [self._make_symbol("a_func")]),
        ]
        reports = self.stripper.identify(nodes, [])
        paths = [r.file_path for r in reports]
        self.assertEqual(paths, sorted(paths))


if __name__ == "__main__":
    unittest.main()
