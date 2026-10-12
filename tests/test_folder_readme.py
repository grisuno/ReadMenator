"""Contract tests for per-folder README.md files (readmenator/_folder_readme.py)."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from readmenator._agent_output import AgentOutputGenerator
from readmenator._app import readmenatorApplication
from readmenator._components import ComponentDiagramBuilder
from readmenator._config import Config
from readmenator._diagrams import DocsSitePublisher
from readmenator._folder_readme import FolderReadmeWriter, is_generated_folder_readme
from readmenator._gh_wiki import GitHubWikiPublisher


class TestFolderReadmeWriterContract(unittest.TestCase):
    """Contract: one README per existing generated folder, honest contents, user files kept."""

    def setUp(self) -> None:
        """Create a project with a few generated folders."""
        self.config = Config()
        self.root = Path(tempfile.mkdtemp())
        self.writer = FolderReadmeWriter(self.config)
        agent = self.root / self.config.AGENT_OUTPUT_DIR
        (agent / "recipes").mkdir(parents=True)
        (agent / "INDEX.md").write_text("# Index\n", encoding="utf-8")
        (agent / "MANIFEST.json").write_text("{}", encoding="utf-8")
        rules = self.root / self.config.RULE_GEN_OUTPUT_DIR
        rules.mkdir()
        (rules / "yara_rules.yar").write_text("", encoding="utf-8")

    def tearDown(self) -> None:
        """Remove the temporary project."""
        shutil.rmtree(self.root)

    def readme(self, dirname: str) -> Path:
        """Return the README path of a folder."""
        return self.root / dirname / self.config.FOLDER_README_FILENAME

    def test_folder_readme_written_only_for_existing_folders(self) -> None:
        written = self.writer.write_all(str(self.root))
        self.assertEqual(sorted(written), sorted([str(self.readme(self.config.AGENT_OUTPUT_DIR).resolve()),
                                                  str(self.readme(self.config.RULE_GEN_OUTPUT_DIR).resolve())]))
        self.assertFalse((self.root / self.config.WIKI_OUTPUT_DIR).exists())

    def test_folder_readme_explains_purpose_and_lists_only_present_entries(self) -> None:
        self.writer.write_all(str(self.root))
        text = self.readme(self.config.AGENT_OUTPUT_DIR).read_text(encoding="utf-8")
        self.assertTrue(text.startswith(self.config.FOLDER_README_MARKER + "\n# " + self.config.AGENT_OUTPUT_DIR))
        self.assertIn("grep-optimized", text)
        self.assertIn("| `INDEX*.md` |", text)
        self.assertIn("| `recipes/` |", text)
        contents = text.split("## How to use")[0]
        self.assertNotIn("SECURITY", contents)
        self.assertNotIn("CONCEPTS", contents)
        self.assertNotIn("| `README.md`", text)
        self.assertIn("## How to use", text)
        self.assertIn("readmenator . --rebuild", text)

    def test_folder_readme_is_idempotent_and_deterministic(self) -> None:
        self.writer.write_all(str(self.root))
        first = self.readme(self.config.AGENT_OUTPUT_DIR).read_text(encoding="utf-8")
        self.writer.write_all(str(self.root))
        self.assertEqual(first, self.readme(self.config.AGENT_OUTPUT_DIR).read_text(encoding="utf-8"))

    def test_folder_readme_keeps_hand_written_readme(self) -> None:
        mine = self.readme(self.config.RULE_GEN_OUTPUT_DIR)
        mine.write_text("# My rules\n", encoding="utf-8")
        self.writer.write_all(str(self.root))
        self.assertEqual(mine.read_text(encoding="utf-8"), "# My rules\n")
        self.assertFalse(is_generated_folder_readme(mine, self.config))

    def test_folder_readme_refuses_symlinks(self) -> None:
        outside = Path(tempfile.mkdtemp())
        try:
            (self.root / self.config.WIKI_OUTPUT_DIR).symlink_to(outside, target_is_directory=True)
            target = outside / "elsewhere.md"
            target.write_text("x", encoding="utf-8")
            self.readme(self.config.RULE_GEN_OUTPUT_DIR).symlink_to(target)
            self.writer.write_all(str(self.root))
            self.assertFalse((outside / self.config.FOLDER_README_FILENAME).exists())
            self.assertEqual(target.read_text(encoding="utf-8"), "x")
        finally:
            shutil.rmtree(outside)

    def test_folder_readme_disabled_writes_nothing(self) -> None:
        writer = FolderReadmeWriter(replace(self.config, FOLDER_README_ENABLED=False))
        self.assertEqual(writer.write_all(str(self.root)), [])
        self.assertFalse(self.readme(self.config.AGENT_OUTPUT_DIR).exists())

    def test_folder_readme_specs_cover_every_generated_folder(self) -> None:
        names = {spec.dirname for spec in self.writer.specs()}
        cfg = self.config
        expected = {cfg.AGENT_OUTPUT_DIR, cfg.WIKI_OUTPUT_DIR, cfg.GRAPHRAG_OUTPUT_DIR, cfg.APIDOCS_OUTPUT_DIR,
                    cfg.DIAGRAM_OUTPUT_DIR, cfg.COMPONENTS_OUTPUT_DIR, cfg.RULE_GEN_OUTPUT_DIR, cfg.GH_WIKI_DRY_RUN_DIR}
        self.assertEqual(names, expected)


class TestFolderReadmeConsumersContract(unittest.TestCase):
    """Contract: Markdown consumers never treat generated folder READMEs as documents."""

    def setUp(self) -> None:
        """Create agent, wiki, and component folders with a generated README each."""
        self.config = Config()
        self.root = Path(tempfile.mkdtemp())
        for dirname in (self.config.AGENT_OUTPUT_DIR, self.config.WIKI_OUTPUT_DIR, self.config.COMPONENTS_OUTPUT_DIR):
            folder = self.root / dirname
            folder.mkdir()
            (folder / "index.md").write_text("# Doc\n", encoding="utf-8")
        FolderReadmeWriter(self.config).write_all(str(self.root))

    def tearDown(self) -> None:
        """Remove the temporary project."""
        shutil.rmtree(self.root)

    def test_folder_readme_not_published_to_site_or_github_wiki(self) -> None:
        site = [p.name for p in DocsSitePublisher(self.config).collect_doc_sources(str(self.root))]
        self.assertNotIn(self.config.FOLDER_README_FILENAME, site)
        self.assertIn("index.md", site)
        wiki = GitHubWikiPublisher(self.config).collect_sources(str(self.root))
        self.assertFalse(any(s.endswith("/" + self.config.FOLDER_README_FILENAME) for s in wiki))

    def test_folder_readme_hand_written_still_published(self) -> None:
        mine = self.root / self.config.WIKI_OUTPUT_DIR / self.config.FOLDER_README_FILENAME
        mine.write_text("# Notes\n", encoding="utf-8")
        site = DocsSitePublisher(self.config).collect_doc_sources(str(self.root))
        self.assertIn(mine.resolve(), [p.resolve() for p in site])

    def test_folder_readme_excluded_from_agent_inventory(self) -> None:
        inventory = AgentOutputGenerator(self.config)._inventory(self.root / self.config.AGENT_OUTPUT_DIR)
        self.assertEqual([item["path"] for item in inventory], ["index.md"])

    def test_folder_readme_survives_component_pruning(self) -> None:
        folder = self.root / self.config.COMPONENTS_OUTPUT_DIR
        document = {"components": [], "components_relations": [], "metadata": {}, "files": [], "methods_index": {}, "description": ""}
        ComponentDiagramBuilder(self.config).write(document, str(folder), str(self.root))
        self.assertTrue((folder / self.config.FOLDER_README_FILENAME).is_file())


class TestFolderReadmeAppWiring(unittest.TestCase):
    """Contract: CLI-facing exports leave a README in the folder they write."""

    def test_folder_readme_written_by_export_apidocs(self) -> None:
        root = Path(tempfile.mkdtemp())
        try:
            (root / "pkg").mkdir()
            (root / "pkg" / "mod.py").write_text('"""Mod."""\n\n\ndef f() -> int:\n    """F."""\n    return 1\n', encoding="utf-8")
            config = replace(Config(), VIDEO_ENABLED=False, GH_WIKI_ENABLED=False)
            readmenatorApplication(config).export_apidocs(str(root))
            readme = root / config.APIDOCS_OUTPUT_DIR / config.FOLDER_README_FILENAME
            self.assertTrue(is_generated_folder_readme(readme, config))
            self.assertIn("api/index.json", readme.read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
