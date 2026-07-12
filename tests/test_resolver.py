"""Contract tests for the ImportResolver.

Validates that import strings from various languages are correctly
resolved to project file paths, handles edge cases like relative
imports, dotted modules, and extensionless imports.
"""

from __future__ import annotations

import unittest

from readmenator._resolver import ImportResolver


class TestImportResolverContract(unittest.TestCase):
    """Contract: ImportResolver maps import strings to file paths."""

    def test_resolves_python_module_dotpath(self) -> None:
        resolver = ImportResolver(
            ["src/utils/helpers.py", "src/main.py"],
        )
        result = resolver.resolve("utils.helpers", "src/main.py")
        self.assertEqual(result, "src/utils/helpers.py")

    def test_resolves_relative_import(self) -> None:
        resolver = ImportResolver(
            ["src/utils/helpers.py", "src/main.py"],
        )
        result = resolver.resolve("./utils/helpers", "src/main.py")
        self.assertEqual(result, "src/utils/helpers.py")

    def test_resolves_extensionless_python_import(self) -> None:
        resolver = ImportResolver(
            ["src/utils/helpers.py", "src/main.py"],
        )
        result = resolver.resolve("helpers", "src/utils/__init__.py")
        self.assertEqual(result, "src/utils/helpers.py")

    def test_resolves_package_init(self) -> None:
        resolver = ImportResolver(
            ["src/utils/__init__.py", "src/main.py"],
        )
        result = resolver.resolve("utils", "src/main.py")
        self.assertIsNotNone(result)

    def test_returns_none_for_external_stdlib(self) -> None:
        resolver = ImportResolver(
            ["src/main.py"],
        )
        result = resolver.resolve("os", "src/main.py")
        self.assertIsNone(result)

    def test_returns_none_for_unknown_import(self) -> None:
        resolver = ImportResolver(
            ["src/main.py"],
        )
        result = resolver.resolve("nonexistent.module", "src/main.py")
        self.assertIsNone(result)

    def test_resolves_stem_match_when_unique(self) -> None:
        resolver = ImportResolver(
            ["src/models.py", "src/views.py", "src/main.py"],
        )
        result = resolver.resolve("models", "src/main.py")
        self.assertIsNotNone(result)

    def test_returns_none_for_empty_import(self) -> None:
        resolver = ImportResolver(["src/main.py"])
        result = resolver.resolve("", "src/main.py")
        self.assertIsNone(result)

    def test_resolves_go_import(self) -> None:
        resolver = ImportResolver(
            ["pkg/database/database.go", "pkg/handler/api.go"],
        )
        result = resolver.resolve("database", "pkg/handler/api.go")
        self.assertIsNotNone(result)

    def test_resolves_same_directory_import(self) -> None:
        resolver = ImportResolver(
            ["src/core/config.py", "src/core/models.py", "src/main.py"],
        )
        result = resolver.resolve("config", "src/core/models.py")
        self.assertEqual(result, "src/core/config.py")


if __name__ == "__main__":
    unittest.main()
