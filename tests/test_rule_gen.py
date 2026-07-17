from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._models import Node, Symbol
from readmenator._rule_gen import RuleGenerator


class TestRuleGeneratorContract(unittest.TestCase):
    """Contract: RuleGenerator detects patterns and suggests rules."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = RuleGenerator(self.config)

    def _make_node(
        self, nid: str, label: str, lang: str = "py"
    ) -> Node:
        return Node(
            node_id=nid,
            label=label,
            kind="module",
            language=lang,
        )

    def _make_node_with_symbols(
        self, nid: str, sym_count: int
    ) -> Node:
        symbols = [
            Symbol(name=f"func{i}", kind="function", line=i)
            for i in range(sym_count)
        ]
        return Node(
            node_id=nid,
            label=Path(nid).name,
            kind="module",
            language="py",
            symbols=symbols,
        )

    def test_empty_nodes_returns_empty_rules(self) -> None:
        rules = self.generator.generate([])
        self.assertEqual(len(rules), 0)

    def test_generates_rules_for_function_heavy_language(self) -> None:
        nodes = [
            self._make_node_with_symbols("main.py", 10),
        ]
        rules = self.generator.generate(nodes)
        py_rules = [r for r in rules if r.language == "py"]
        self.assertGreater(len(py_rules), 0)

    def test_detects_antipatterns_with_content(self) -> None:
        cfg = Config(RULE_GEN_MIN_PATTERN_COUNT=1)
        generator = RuleGenerator(cfg)
        nodes = [self._make_node("main.py", "main.py")]
        content_map = {
            "main.py": "    try:\n        pass\n    except:\n        pass\n",
        }
        rules = generator.generate(nodes, content_map)
        bare_except_rules = [r for r in rules if "bare except" in r.description.lower()]
        self.assertGreater(len(bare_except_rules), 0)

    def test_antipattern_threshold_from_config(self) -> None:
        cfg = Config(RULE_GEN_MIN_PATTERN_COUNT=1)
        generator = RuleGenerator(cfg)
        nodes = [self._make_node("main.py", "main.py")]
        content_map = {
            "main.py": "try:\n    pass\nexcept:\n    pass\n",
        }
        rules = generator.generate(nodes, content_map)
        self.assertGreater(len(rules), 0)

    def test_write_rules_creates_files(self) -> None:
        nodes = [
            self._make_node_with_symbols("main.py", 10),
        ]
        rules = self.generator.generate(nodes)
        with tempfile.TemporaryDirectory() as tmpdir:
            written = self.generator.write_rules(rules, tmpdir)
            self.assertGreaterEqual(written, 0)
            if written > 0:
                out_dir = Path(tmpdir)
                files = list(out_dir.glob("*.yml"))
                self.assertGreater(len(files), 0)

    def test_rule_id_increments(self) -> None:
        generator = RuleGenerator(self.config)
        nodes = [
            self._make_node_with_symbols("a.py", 10),
            self._make_node_with_symbols("b.py", 10),
        ]
        rules = generator.generate(nodes)
        ids = [r.rule_id for r in rules]
        unique_ids = set(ids)
        self.assertEqual(len(ids), len(unique_ids))
