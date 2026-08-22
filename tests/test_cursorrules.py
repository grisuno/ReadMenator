"""Contract tests for the CursorRulesGenerator.

Validates base rule generation, layer constraint extraction,
analysis constraint extraction, and violation rule formatting.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._cursorrules_generator import CursorRulesGenerator
from readmenator._models import AnalysisResult, CommunityResult, LinterViolation, Node, Symbol


class TestCursorRulesGeneratorContract(unittest.TestCase):
    """Contract: CursorRulesGenerator produces deterministic rulesets."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = CursorRulesGenerator(self.config)

    def test_generate_returns_string(self) -> None:
        result = self.generator.generate([], [])
        self.assertIsInstance(result, str)

    def test_generate_contains_header(self) -> None:
        result = self.generator.generate([], [])
        self.assertIn("ReadMenator Generated Architecture Rules", result)

    def test_generate_contains_base_rules(self) -> None:
        result = self.generator.generate([], [])
        self.assertIn("strict separation of concerns", result)
        self.assertIn("300 lines", result)

    def test_generate_includes_layer_constraints(self) -> None:
        layers = {
            "ui/view.py": "presentation",
            "data/repo.py": "data_access",
            "ui/template.py": "presentation",
        }
        result = self.generator.generate([], [], layers=layers)
        self.assertIn("Detected Architectural Layers", result)
        self.assertIn("presentation", result)
        self.assertIn("data_access", result)

    def test_generate_includes_god_nodes(self) -> None:
        analysis = AnalysisResult(
            god_nodes=[("hub.py", 10.0), ("core.py", 8.0)],
            communities=[],
            surprising_connections=[],
            suggested_questions=[],
            node_count=2,
            edge_count=1,
        )
        result = self.generator.generate([], [], analysis=analysis)
        self.assertIn("Central Files (God Nodes)", result)
        self.assertIn("hub.py", result)

    def test_generate_includes_communities(self) -> None:
        community = CommunityResult(
            community_id=0,
            label="core",
            file_ids={"a.py", "b.py"},
            cohesion=0.8,
            size=2,
        )
        analysis = AnalysisResult(
            god_nodes=[],
            communities=[community],
            surprising_connections=[],
            suggested_questions=[],
            node_count=2,
            edge_count=1,
        )
        result = self.generator.generate([], [], analysis=analysis)
        self.assertIn("Community Boundaries", result)
        self.assertIn("core", result)

    def test_generate_includes_violations(self) -> None:
        violations = [
            LinterViolation(
                file_path="ui/view.py",
                rule_id="ARC002",
                severity="error",
                message="presentation must not import data_access",
            ),
        ]
        result = self.generator.generate([], [], violations=violations)
        self.assertIn("Active Violations to Fix", result)
        self.assertIn("ARC002", result)

    def test_generate_limits_violations_to_ten(self) -> None:
        violations = [
            LinterViolation(f"file{i}.py", "ARC001", "warning", f"issue {i}")
            for i in range(15)
        ]
        result = self.generator.generate([], [], violations=violations)
        self.assertIn("and 5 more violations", result)

    def test_generate_writes_file_when_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            self.generator.generate([], [], project_root=tmpdir)
            output = Path(tmpdir) / self.config.CURSORRULES_OUTPUT
            self.assertTrue(output.exists())
            content = output.read_text(encoding="utf-8")
            self.assertIn("ReadMenator Generated Architecture Rules", content)

    def test_generate_idempotent(self) -> None:
        layers = {"a.py": "presentation"}
        result1 = self.generator.generate([], [], layers=layers)
        result2 = self.generator.generate([], [], layers=layers)
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
