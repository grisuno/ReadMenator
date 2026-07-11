import tempfile
import unittest
from pathlib import Path

from readmenator._app import readmenatorApplication
from readmenator._config import Config


class TestEndToEndContract(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp())
        self.config = Config()
        self.app = readmenatorApplication(self.config)

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write(self, path: str, content: str) -> None:
        full_path = self.temp_dir / path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")

    def test_full_pipeline_generates_knowledge_base(self) -> None:
        self._write("main.py", "import os\n\ndef hello():\n    pass\n\nclass Greeter:\n    pass\n")
        self._write("lib.rs", "pub fn compute() -> i32 { 42 }\n")
        self._write("test.go", "package main\n\nfunc main() {}\n")
        self.app.run(str(self.temp_dir))
        kb_path = self.temp_dir / "KNOWLEDGE_BASE.md"
        self.assertTrue(kb_path.exists())
        content = kb_path.read_text(encoding="utf-8")
        self.assertIn("**Total Files Parsed:**", content)
        self.assertIn("3", content.split("Total Files Parsed:")[1].split("|")[0])
        self.assertIn("**Total Symbols Extracted:**", content)
        self.assertIn("hello", content)
        self.assertIn("Greeter", content)
        self.assertIn("compute", content)
        self.assertIn("main", content)

    def test_knowledge_base_contains_mermaid(self) -> None:
        self._write("main.py", "import sys\n")
        self.app.run(str(self.temp_dir))
        kb_path = self.temp_dir / "KNOWLEDGE_BASE.md"
        content = kb_path.read_text(encoding="utf-8")
        self.assertIn("```mermaid", content)
        self.assertIn("graph TD", content)

    def test_query_subcommand_works(self) -> None:
        self._write("main.py", "class Database:\n    pass\n")
        result = self.app.query(str(self.temp_dir), "Database")
        self.assertIn("Database", result)

    def test_explain_subcommand_works(self) -> None:
        self._write("main.py", "class Router:\n    \"\"\"Routes HTTP requests.\"\"\"\n    pass\n")
        result = self.app.explain(str(self.temp_dir), "Router")
        self.assertIn("Router", result)
        self.assertIn("class", result)

    def test_path_subcommand_works(self) -> None:
        self._write("main.py", "import utils\n")
        self._write("utils.py", "def helper(): pass\n")
        result = self.app.find_path(str(self.temp_dir), "helper", "helper")
        self.assertIn("utils.py", result)

    def test_summary_works(self) -> None:
        self._write("main.py", "def start(): pass\n")
        summary = self.app.summary(str(self.temp_dir))
        self.assertIn("1 files", summary)
        self.assertIn("1 symbols", summary)

    def test_rebuild(self) -> None:
        self._write("main.py", "x = 1\n")
        self.app.run(str(self.temp_dir))
        self._write("extra.py", "y = 2\n")
        self.app.rebuild(str(self.temp_dir))
        kb_path = self.temp_dir / "KNOWLEDGE_BASE.md"
        content = kb_path.read_text(encoding="utf-8")
        self.assertIn("**Total Files Parsed:**", content)
        self.assertIn("2", content.split("Total Files Parsed:")[1].split("|")[0])
