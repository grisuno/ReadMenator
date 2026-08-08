"""Contract tests for README injection into documented projects.

SDD + TDD + BDD: Each test validates a specific behavioral contract
of the ReadmeInjector for injecting/deleting knowledge base links.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from readmenator._readme_injector import ReadmeInjector


class TestReadmeInjectorInjectBehavior(unittest.TestCase):
    """BDD: ReadmeInjector injection contract."""

    def setUp(self) -> None:
        self.tmpdir = tempfile.mkdtemp()
        self.root = Path(self.tmpdir)
        self.injector = ReadmeInjector(kb_filename="KNOWLEDGE_BASE.md")

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_inject_into_markdown_readme_adds_kb_link(self):
        readme = self.root / "README.md"
        readme.write_text("# My Project\n\nSome content.\n")
        result = self.injector.inject(str(self.root))
        self.assertTrue(result)
        content = readme.read_text()
        self.assertIn("KNOWLEDGE_BASE.md", content)
        self.assertIn("ReadMenator", content)
        self.assertIn("<!-- readmenator-kb-link -->", content)

    def test_inject_into_rst_readme_adds_kb_link(self):
        readme = self.root / "README.rst"
        readme.write_text("My Project\n==========\n\nSome content.\n")
        result = self.injector.inject(str(self.root))
        self.assertTrue(result)
        content = readme.read_text()
        self.assertIn("KNOWLEDGE_BASE.md", content)
        self.assertIn("<!-- readmenator-kb-link -->", content)

    def test_inject_is_idempotent_does_not_duplicate(self):
        readme = self.root / "README.md"
        readme.write_text("# My Project\n\nSome content.\n")
        first = self.injector.inject(str(self.root))
        self.assertTrue(first)
        second = self.injector.inject(str(self.root))
        self.assertFalse(second)
        content = readme.read_text()
        occurrences = content.count("Knowledge Base")
        self.assertEqual(occurrences, 1)

    def test_inject_no_readme_file_returns_false(self):
        result = self.injector.inject(str(self.root))
        self.assertFalse(result)

    def test_inject_preserves_existing_content(self):
        original = "# My Project\n\nSome original content.\n"
        readme = self.root / "README.md"
        readme.write_text(original)
        self.injector.inject(str(self.root))
        content = readme.read_text()
        self.assertTrue(content.startswith(original.strip()))


class TestReadmeInjectorRemoveBehavior(unittest.TestCase):
    """BDD: ReadmeInjector removal contract."""

    def setUp(self) -> None:
        self.tmpdir = tempfile.mkdtemp()
        self.root = Path(self.tmpdir)
        self.injector = ReadmeInjector(kb_filename="KNOWLEDGE_BASE.md")

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_remove_strips_injected_section(self):
        readme = self.root / "README.md"
        original = "# My Project\n\nOriginal content.\n"
        readme.write_text(original)
        self.injector.inject(str(self.root))
        self.injector.remove(str(self.root))
        content = readme.read_text()
        self.assertNotIn("<!-- readmenator-kb-link -->", content)
        self.assertIn("Original content", content)

    def test_remove_without_injection_returns_false(self):
        readme = self.root / "README.md"
        readme.write_text("# My Project\n")
        result = self.injector.remove(str(self.root))
        self.assertFalse(result)

    def test_remove_no_readme_returns_false(self):
        result = self.injector.remove(str(self.root))
        self.assertFalse(result)


class TestReadmeInjectorFindReadme(unittest.TestCase):
    """BDD: ReadmeInjector README file detection contract."""

    def setUp(self) -> None:
        self.tmpdir = tempfile.mkdtemp()
        self.root = Path(self.tmpdir)

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_finds_readme_md(self):
        (self.root / "README.md").write_text("")
        result = ReadmeInjector._find_readme(self.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "README.md")

    def test_finds_readme_rst(self):
        (self.root / "README.rst").write_text("")
        result = ReadmeInjector._find_readme(self.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "README.rst")

    def test_prefers_readme_md_over_rst(self):
        (self.root / "README.rst").write_text("")
        (self.root / "README.md").write_text("")
        result = ReadmeInjector._find_readme(self.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "README.md")

    def test_returns_none_when_no_readme(self):
        result = ReadmeInjector._find_readme(self.root)
        self.assertIsNone(result)


class TestReadmeInjectorEdgeCases(unittest.TestCase):
    """BDD: ReadmeInjector edge case contract."""

    def setUp(self) -> None:
        self.tmpdir = tempfile.mkdtemp()
        self.root = Path(self.tmpdir)
        self.injector = ReadmeInjector(kb_filename="KNOWLEDGE_BASE.md")

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_inject_into_empty_readme(self):
        readme = self.root / "README.md"
        readme.write_text("")
        result = self.injector.inject(str(self.root))
        self.assertTrue(result)
        content = readme.read_text()
        self.assertIn("KNOWLEDGE_BASE.md", content)

    def test_custom_kb_filename_works(self):
        injector = ReadmeInjector(kb_filename="docs/KB.md")
        readme = self.root / "README.md"
        readme.write_text("# Test\n")
        injector.inject(str(self.root))
        content = readme.read_text()
        self.assertIn("docs/KB.md", content)


if __name__ == "__main__":
    unittest.main()
