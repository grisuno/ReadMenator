"""Contract tests for the MonolithRefactorizer.

Validates monolithic file detection, refactoring plan generation,
symbol grouping, target file suggestion, and script generation.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol
from readmenator._refactorizer import MonolithRefactorizer


class TestMonolithRefactorizerContract(unittest.TestCase):
    """Contract: MonolithRefactorizer generates refactoring plans."""

    def setUp(self) -> None:
        self.config = Config()
        self.refactorizer = MonolithRefactorizer(self.config)

    def _make_symbol(self, name: str, kind: str = "function", line: int = 1) -> Symbol:
        return Symbol(name=name, kind=kind, line=line)

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

    def test_analyze_empty_graph_returns_empty(self) -> None:
        plans = self.refactorizer.analyze([], [])
        self.assertEqual(len(plans), 0)

    def test_analyze_ignores_small_files(self) -> None:
        nodes = [self._make_node("small.py", [self._make_symbol("f1")])]
        content_map = {"small.py": "line1\nline2\nline3\n"}
        plans = self.refactorizer.analyze(nodes, [], content_map=content_map)
        self.assertEqual(len(plans), 0)

    def test_analyze_detects_large_file(self) -> None:
        nodes = [self._make_node("big.py", [self._make_symbol("f1"), self._make_symbol("f2")])]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        plans = self.refactorizer.analyze(nodes, [], content_map=content_map)
        self.assertGreater(len(plans), 0)
        self.assertEqual(plans[0].file_path, "big.py")
        self.assertEqual(plans[0].current_lines, 400)

    def test_analyze_generates_extract_class_for_multiple_classes(self) -> None:
        symbols = [
            self._make_symbol("ClassA", "class", 10),
            self._make_symbol("ClassB", "class", 50),
            self._make_symbol("ClassC", "class", 100),
        ]
        nodes = [self._make_node("big.py", symbols)]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        plans = self.refactorizer.analyze(nodes, [], content_map=content_map)
        self.assertGreater(len(plans), 0)
        actions = plans[0].actions
        class_actions = [a for a in actions if a.action_type == "EXTRACT_CLASS"]
        self.assertGreater(len(class_actions), 0)

    def test_analyze_generates_extract_function_for_multiple_functions(self) -> None:
        symbols = [
            self._make_symbol("func1", "function", 10),
            self._make_symbol("func2", "function", 50),
            self._make_symbol("func3", "function", 100),
        ]
        nodes = [self._make_node("big.py", symbols)]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        plans = self.refactorizer.analyze(nodes, [], content_map=content_map)
        self.assertGreater(len(plans), 0)
        actions = plans[0].actions
        func_actions = [a for a in actions if a.action_type == "EXTRACT_FUNCTION"]
        self.assertGreater(len(func_actions), 0)

    def test_analyze_splits_file_with_many_symbols(self) -> None:
        symbols = [self._make_symbol(f"f{i}", "function", i * 10) for i in range(10)]
        nodes = [self._make_node("big.py", symbols)]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        plans = self.refactorizer.analyze(nodes, [], content_map=content_map)
        self.assertGreater(len(plans), 0)

    def test_analyze_estimates_impact_from_resolved_edges(self) -> None:
        nodes = [self._make_node("big.py", [self._make_symbol("f1"), self._make_symbol("f2")])]
        resolved = [
            self._make_edge("a.py", "big.py"),
            self._make_edge("b.py", "big.py"),
        ]
        content = "\n".join(f"line{i}" for i in range(400))
        content_map = {"big.py": content}
        plans = self.refactorizer.analyze(nodes, [], resolved_edges=resolved, content_map=content_map)
        self.assertGreater(len(plans), 0)
        self.assertEqual(plans[0].estimated_impact, 2)

    def test_generate_script_contains_shebang(self) -> None:
        from readmenator._models import RefactoringAction, RefactoringPlan
        plan = RefactoringPlan(
            file_path="big.py",
            actions=[
                RefactoringAction(
                    action_type="EXTRACT_CLASS",
                    source_file="big.py",
                    start_line=1,
                    end_line=50,
                    target_file="big_classes.py",
                    description="Extract classes",
                ),
            ],
            estimated_impact=0,
            current_lines=400,
        )
        script = self.refactorizer.generate_script(plan, ".")
        self.assertTrue(script.startswith("#!/bin/bash"))

    def test_generate_script_contains_set_e(self) -> None:
        from readmenator._models import RefactoringAction, RefactoringPlan
        plan = RefactoringPlan(
            file_path="big.py",
            actions=[],
            estimated_impact=0,
            current_lines=400,
        )
        script = self.refactorizer.generate_script(plan, ".")
        self.assertIn("set -e", script)

    def test_generate_script_contains_sed_commands(self) -> None:
        from readmenator._models import RefactoringAction, RefactoringPlan
        plan = RefactoringPlan(
            file_path="big.py",
            actions=[
                RefactoringAction(
                    action_type="EXTRACT_CLASS",
                    source_file="big.py",
                    start_line=1,
                    end_line=50,
                    target_file="big_classes.py",
                    description="Extract classes",
                ),
            ],
            estimated_impact=0,
            current_lines=400,
        )
        script = self.refactorizer.generate_script(plan, ".")
        self.assertIn("sed -n '1,50p'", script)

    def test_analyze_sorted_by_line_count(self) -> None:
        nodes = [
            self._make_node("medium.py", [self._make_symbol("f1"), self._make_symbol("f2")]),
            self._make_node("huge.py", [self._make_symbol("g1"), self._make_symbol("g2")]),
        ]
        content_map = {
            "medium.py": "\n".join(f"line{i}" for i in range(350)),
            "huge.py": "\n".join(f"line{i}" for i in range(500)),
        }
        plans = self.refactorizer.analyze(nodes, [], content_map=content_map)
        if len(plans) >= 2:
            self.assertGreaterEqual(plans[0].current_lines, plans[1].current_lines)

    def test_analyze_respects_max_files_limit(self) -> None:
        config = Config(REFACTORIZER_MAX_FILES=1)
        refactorizer = MonolithRefactorizer(config)
        nodes = [
            self._make_node("a.py", [self._make_symbol("f1"), self._make_symbol("f2")]),
            self._make_node("b.py", [self._make_symbol("g1"), self._make_symbol("g2")]),
        ]
        content_map = {
            "a.py": "\n".join(f"line{i}" for i in range(400)),
            "b.py": "\n".join(f"line{i}" for i in range(400)),
        }
        plans = refactorizer.analyze(nodes, [], content_map=content_map)
        self.assertLessEqual(len(plans), 1)


if __name__ == "__main__":
    unittest.main()
