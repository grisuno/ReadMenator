import os
import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._models import Symbol
from readmenator._scanner import PolyglotScanner


class TestScannerContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()
        self.temp_dir = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write(self, path: str, content: str) -> None:
        full_path = self.temp_dir / path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")

    def test_scans_python_files(self) -> None:
        self._write("main.py", "def hello(): pass\n")
        scanner = PolyglotScanner(self.config)
        nodes, edges = scanner.scan(self.temp_dir)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].label, "main.py")

    def test_ignores_env_and_vendor_dirs(self) -> None:
        self._write("env/lib/x.py", "def fake(): pass\n")
        self._write("vendor/x.py", "def fake(): pass\n")
        self._write("node_modules/x.js", "function fake() {}\n")
        self._write("main.py", "def real(): pass\n")
        scanner = PolyglotScanner(self.config)
        nodes, _ = scanner.scan(self.temp_dir)
        paths = [n.node_id for n in nodes]
        self.assertIn("main.py", paths)
        self.assertNotIn("env/lib/x.py", paths)
        self.assertNotIn("vendor/x.py", paths)
        self.assertNotIn("node_modules/x.js", paths)

    def test_rejects_symlinks(self) -> None:
        real_file = self.temp_dir / "real.py"
        real_file.write_text("def real(): pass\n")
        link_path = self.temp_dir / "link.py"
        try:
            os.symlink(real_file, link_path)
        except OSError:
            self.skipTest("Cannot create symlinks on this platform")
        scanner = PolyglotScanner(self.config)
        nodes, _ = scanner.scan(self.temp_dir)
        paths = [n.node_id for n in nodes]
        self.assertIn("real.py", paths)
        self.assertNotIn("link.py", paths)

    def test_skips_non_code_files(self) -> None:
        self._write("data.json", '{"key": "value"}')
        self._write("main.py", "def hello(): pass\n")
        self._write("readme.md", "# Title\n")
        scanner = PolyglotScanner(self.config)
        nodes, _ = scanner.scan(self.temp_dir)
        paths = [n.node_id for n in nodes]
        self.assertIn("main.py", paths)
        self.assertNotIn("data.json", paths)
        self.assertNotIn("readme.md", paths)

    def test_scans_multiple_languages(self) -> None:
        self._write("main.c", "int main() { return 0; }\n")
        self._write("utils.py", "def helper(): pass\n")
        self._write("server.go", "func main() {}\n")
        self._write("lib.rs", "fn calculate() {}\n")
        scanner = PolyglotScanner(self.config)
        nodes, _ = scanner.scan(self.temp_dir)
        self.assertEqual(len(nodes), 4)

    def test_respects_max_directory_depth(self) -> None:
        deep_config = Config(MAX_DIRECTORY_DEPTH=3)
        self._write("a/b/c/d/e/file.py", "def deep(): pass\n")
        self._write("a/b/file.py", "def shallow(): pass\n")
        scanner = PolyglotScanner(deep_config)
        nodes, _ = scanner.scan(self.temp_dir)
        paths = [n.node_id for n in nodes]
        self.assertNotIn("a/b/c/d/e/file.py", paths)
        self.assertIn("a/b/file.py", paths)

    def test_raises_on_invalid_directory(self) -> None:
        scanner = PolyglotScanner(self.config)
        with self.assertRaises(ValueError):
            scanner.scan(Path("/nonexistent_path_xyz"))

    def test_import_edges_are_created(self) -> None:
        self._write("main.py", "import os\nimport sys\n")
        scanner = PolyglotScanner(self.config)
        nodes, edges = scanner.scan(self.temp_dir)
        sources = [e.source for e in edges]
        targets = [e.target for e in edges]
        self.assertIn("main.py", sources)
        self.assertIn("os", targets)
        self.assertIn("sys", targets)

    def test_privacy_mode_strips_docs(self) -> None:
        self._write("main.py", '"""File doc."""\ndef foo():\n    """Func doc."""\n    pass\n')
        cfg = Config(PRIVACY_MODE=True)
        scanner = PolyglotScanner(cfg)
        nodes, _ = scanner.scan(self.temp_dir)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].doc, "")
        for sym in nodes[0].symbols:
            self.assertEqual(sym.doc, "")

    def test_scan_with_content_returns_content_map(self) -> None:
        self._write("main.py", "def hello(): pass\n")
        scanner = PolyglotScanner(self.config)
        nodes, edges, content_map = scanner.scan_with_content(self.temp_dir)
        self.assertEqual(len(nodes), 1)
        self.assertIn("main.py", content_map)
        self.assertIn("def hello()", content_map["main.py"])

    def test_gitignore_respected_when_enabled(self) -> None:
        self._write("main.py", "def real(): pass\n")
        self._write(".gitignore", "ignored.py\n")
        self._write("ignored.py", "def ignored(): pass\n")
        cfg = Config(GITIGNORE_AWARE=True)
        scanner = PolyglotScanner(cfg)
        nodes, _ = scanner.scan(self.temp_dir)
        paths = [n.node_id for n in nodes]
        self.assertIn("main.py", paths)
        self.assertNotIn("ignored.py", paths)

    def test_gitignore_disabled_by_default(self) -> None:
        self._write("main.py", "def real(): pass\n")
        self._write(".gitignore", "main.py\n")
        default_cfg = Config()  # GITIGNORE_AWARE=True by default
        scanner = PolyglotScanner(default_cfg)
        nodes, _ = scanner.scan(self.temp_dir)
        paths = [n.node_id for n in nodes]
        self.assertNotIn("main.py", paths)

    def test_gitignore_glob_conversion(self) -> None:
        pattern = PolyglotScanner._gitignore_glob_to_regex("*.pyc")
        import re
        self.assertIsNotNone(re.search(pattern, "test.pyc"))
        self.assertIsNone(re.search(pattern, "test.py"))
