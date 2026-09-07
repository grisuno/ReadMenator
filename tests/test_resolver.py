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

    def test_resolves_c_quoted_header_same_dir(self) -> None:
        resolver = ImportResolver(
            ["src/main.c", "src/utils.h"],
        )
        result = resolver.resolve("utils.h", "src/main.c")
        self.assertEqual(result, "src/utils.h")

    def test_resolves_c_quoted_header_subdir(self) -> None:
        resolver = ImportResolver(
            ["src/main.c", "src/lib/net.h"],
        )
        result = resolver.resolve("lib/net.h", "src/main.c")
        self.assertEqual(result, "src/lib/net.h")

    def test_resolves_c_extensionless_header(self) -> None:
        resolver = ImportResolver(
            ["src/main.c", "src/utils.h"],
        )
        result = resolver.resolve("utils", "src/main.c")
        self.assertEqual(result, "src/utils.h")

    def test_resolves_c_source_from_header_dir(self) -> None:
        resolver = ImportResolver(
            ["src/utils.c", "src/utils.h"],
        )
        result = resolver.resolve("utils.h", "src/utils.c")
        self.assertEqual(result, "src/utils.h")

    def test_resolves_cpp_header_same_dir(self) -> None:
        resolver = ImportResolver(
            ["app/main.cpp", "app/core.hpp"],
        )
        result = resolver.resolve("core.hpp", "app/main.cpp")
        self.assertEqual(result, "app/core.hpp")

    def test_resolves_c_header_stem_across_dirs(self) -> None:
        resolver = ImportResolver(
            ["lib/utils.h", "other/main.c"],
        )
        result = resolver.resolve("utils.h", "other/main.c")
        self.assertEqual(result, "lib/utils.h")

    def test_returns_none_for_c_system_header(self) -> None:
        resolver = ImportResolver(
            ["src/main.c"],
        )
        result = resolver.resolve("stdio.h", "src/main.c")
        self.assertIsNone(result)

    def test_resolves_parent_dir_include(self) -> None:
        resolver = ImportResolver(
            ["include/types.h", "src/main.c"],
        )
        result = resolver.resolve("../include/types.h", "src/main.c")
        self.assertEqual(result, "include/types.h")

    def test_resolves_parent_dir_include_despite_ambiguous_stem(self) -> None:
        resolver = ImportResolver(
            ["include/types.h", "arch/types.h", "src/main.c"],
        )
        result = resolver.resolve("../include/types.h", "src/main.c")
        self.assertEqual(result, "include/types.h")

    def test_resolves_include_dir_suffix_match(self) -> None:
        resolver = ImportResolver(
            ["include/kernel/mm.h", "arch/mm.h", "src/main.c"],
        )
        result = resolver.resolve("kernel/mm.h", "src/main.c")
        self.assertEqual(result, "include/kernel/mm.h")

    def test_returns_none_for_ambiguous_suffix_match(self) -> None:
        resolver = ImportResolver(
            ["include/kernel/mm.h", "arch/kernel/mm.h", "src/main.c"],
        )
        result = resolver.resolve("kernel/mm.h", "src/main.c")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
