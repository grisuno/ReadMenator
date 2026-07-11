import unittest
from dataclasses import FrozenInstanceError

from readmenator._config import Config


class TestConfigContract(unittest.TestCase):
    def test_config_is_immutable(self) -> None:
        config = Config()
        with self.assertRaises(FrozenInstanceError):
            config.MAX_FILE_SIZE_MB = 99.0

    def test_config_defaults_are_sane(self) -> None:
        config = Config()
        self.assertEqual(config.MAX_FILE_SIZE_MB, 10.0)
        self.assertEqual(config.MAX_DIRECTORY_DEPTH, 20)
        self.assertEqual(config.DOCSTRING_LOOKBACK_LINES, 15)
        self.assertEqual(config.DOCSTRING_MAX_LENGTH, 150)
        self.assertEqual(config.MERMAID_MAX_NODES, 300)
        self.assertIn(".py", config.SUPPORTED_EXTENSIONS)
        self.assertIn(".rs", config.SUPPORTED_EXTENSIONS)
        self.assertIn(".java", config.SUPPORTED_EXTENSIONS)
        self.assertNotIn(".xyz", config.SUPPORTED_EXTENSIONS)

    def test_ignore_dirs_are_comprehensive(self) -> None:
        config = Config()
        critical = {".git", "__pycache__", "node_modules", "venv", "target", "build"}
        for d in critical:
            self.assertIn(d, config.IGNORE_DIRS)

    def test_plural_map_covers_all_symbol_types(self) -> None:
        config = Config()
        plural_map = dict(config.SYMBOL_TYPE_PLURALS)
        self.assertEqual(plural_map["class"], "classes")
        self.assertEqual(plural_map["function"], "functions")
        self.assertEqual(plural_map["method"], "methods")
        self.assertEqual(plural_map["struct"], "structs")
        self.assertIn("class", plural_map)
        self.assertIn("function", plural_map)
        self.assertIn("trait", plural_map)

    def test_supported_extensions_no_duplicates(self) -> None:
        config = Config()
        exts = list(config.SUPPORTED_EXTENSIONS)
        self.assertEqual(len(exts), len(set(exts)))
