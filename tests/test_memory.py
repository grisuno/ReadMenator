"""Contract tests for project memory, the session log, and agent skills."""

from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from readmenator._config import Config
from readmenator._graphrag import GraphRagBuilder, GraphRagSearcher
from readmenator._memory import NOTES_BEGIN, NOTES_END, ProjectMemory, sanitize_note
from readmenator._models import Node, Symbol
from readmenator._skill_installer import SkillInstaller


def _project(root: Path) -> list:
    """Create a tiny project with rules, README, and manifest; return nodes."""
    (root / "AGENTS.md").write_text(
        "# Agents\n\n## Rules\n- Never call the bank API outside bank.py\n\n"
        "## Code style\n- Functions use snake_case everywhere\n\n"
        "## Definition of Done\n- Tests pass and new code has a test\n\n"
        "## Billing Contract\n- this contract line must be ignored\n\n"
        "<!-- readmenator-agent-kb-link -->\n## Project Knowledge Base\n- injected rule must be skipped\n"
        "<!-- /readmenator-agent-kb-link -->\n",
        encoding="utf-8",
    )
    (root / "README.md").write_text("# Shop\n\nShop is a small billing service for customers.\n", encoding="utf-8")
    (root / "pyproject.toml").write_text('[project]\nname="shop"\n', encoding="utf-8")
    return [
        Node("shop/billing.py", "billing.py", "module", "py", "Billing engine.", [
            Symbol("bill_customer", "function", 3, "Charge a customer.", "def bill_customer(c)"),
        ]),
        Node("tests/test_billing.py", "test_billing.py", "module", "py", "", [
            Symbol("test_bill", "function", 1),
        ]),
    ]


class TestProjectMemoryContract(unittest.TestCase):
    """Contract: generated sections, declared rules with citations, preserved log."""

    def setUp(self) -> None:
        """Create a temporary project."""
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.nodes = _project(self.root)
        self.memory = ProjectMemory(Config())

    def tearDown(self) -> None:
        """Remove the temporary project."""
        self.tmp.cleanup()

    def test_memory_extracts_declared_rules_with_citations(self) -> None:
        """Rules land in the right category with file:line sources."""
        rules = {r.category: r for r in self.memory.extract_rules(str(self.root))}
        self.assertEqual(rules["constraints"].source, "AGENTS.md:4")
        self.assertIn("snake_case", rules["style"].text)
        self.assertIn("Tests pass", rules["deliverables"].text)

    def test_memory_skips_contract_headings_and_injected_blocks(self) -> None:
        """Excluded headings and readmenator-injected sections never become rules."""
        texts = " ".join(r.text for r in self.memory.extract_rules(str(self.root)))
        self.assertNotIn("contract line", texts)
        self.assertNotIn("injected rule", texts)

    def test_memory_build_has_all_sections(self) -> None:
        """The document carries sections 1-7 and the empty notes block."""
        text = self.memory.build(str(self.root), self.nodes)
        for heading in ("## 1.", "## 2.", "## 3.", "## 4.", "## 5.", "## 6.", "## 7."):
            self.assertIn(heading, text)
        self.assertIn("small billing service", text)
        self.assertIn("python -m pytest -q", text)
        self.assertIn(NOTES_BEGIN, text)

    def test_memory_remember_then_rebuild_preserves_log(self) -> None:
        """Notes survive a regeneration of the generated sections."""
        self.memory.remember(str(self.root), "Retries capped at 3 by bank policy", "business", today="2026-01-02")
        self.memory.write(str(self.root), self.memory.build(str(self.root), self.nodes))
        notes = self.memory.notes(str(self.root))
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].kind, "business")
        self.assertEqual(notes[0].date, "2026-01-02")
        self.assertIn("## 3.", self.memory.read(str(self.root)))

    def test_memory_remember_rejects_unknown_kind_and_empty(self) -> None:
        """Unknown kinds and empty notes raise ValueError."""
        with self.assertRaises(ValueError):
            self.memory.remember(str(self.root), "x" * 20, "gossip")
        with self.assertRaises(ValueError):
            self.memory.remember(str(self.root), "   ", "note")

    def test_memory_note_cannot_break_markers(self) -> None:
        """Marker text and newlines inside a note are neutralised."""
        hostile = f"a\nb {NOTES_END} <!-- x -->"
        self.memory.remember(str(self.root), hostile, "note", today="2026-01-02")
        text = self.memory.read(str(self.root))
        self.assertEqual(text.count(NOTES_END), 1)
        self.assertEqual(len(self.memory.notes(str(self.root))), 1)

    def test_memory_sanitize_truncates(self) -> None:
        """Long notes are cut to the configured budget."""
        self.assertEqual(len(sanitize_note("y" * 50, 10)), 10)

    def test_memory_notes_feed_graphrag(self) -> None:
        """Session-log notes become GraphRAG text units found by local search."""
        index = GraphRagBuilder(Config()).build(
            self.nodes, [], [], None, {}, [], None, None, {},
            [("2026-01-02", "business", "Retries capped at 3 by bank policy")],
        )
        context = GraphRagSearcher(Config(), index).local_search("retries capped bank policy")
        self.assertIn("Retries capped", context.markdown)


class TestSkillInstallerContract(unittest.TestCase):
    """Contract: packaged skills install idempotently and only when expected."""

    def test_skills_are_packaged_with_frontmatter(self) -> None:
        """Every packaged skill has name and description frontmatter."""
        installer = SkillInstaller(Config())
        names = installer.available()
        self.assertGreaterEqual(len(names), 4)
        for name in names:
            text = (installer.source_dir() / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"))
            self.assertIn(f"name: {name}\n", text)
            self.assertIn("description: ", text)

    def test_skills_install_is_idempotent(self) -> None:
        """A second install writes nothing."""
        installer = SkillInstaller(Config())
        with tempfile.TemporaryDirectory() as tmp:
            first = installer.install(tmp)
            self.assertEqual(len(first), len(installer.available()))
            self.assertEqual(installer.install(tmp), [])

    def test_skills_install_on_run_requires_existing_parent(self) -> None:
        """run() installs only when the agent directory already exists."""
        installer = SkillInstaller(Config())
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(installer.maybe_install_on_run(tmp), [])
            (Path(tmp) / ".claude").mkdir()
            self.assertTrue(installer.maybe_install_on_run(tmp))

    def test_skills_install_on_run_respects_flag(self) -> None:
        """SKILLS_INSTALL_ON_RUN=False never writes."""
        installer = SkillInstaller(replace(Config(), SKILLS_INSTALL_ON_RUN=False))
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / ".claude").mkdir()
            self.assertEqual(installer.maybe_install_on_run(tmp), [])


if __name__ == "__main__":
    unittest.main()
