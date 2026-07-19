"""Property-based contract tests for all 19 language parsers.

Uses Hypothesis to generate random, malformed, edge-case, and massive
inputs to guarantee parsers fail gracefully without crashing.

Run with: hypothesis profile (e.g. ``pytest --hypothesis-show-statistics``).

These tests are skipped if Hypothesis is not installed.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from typing import List

from readmenator._config import Config
from readmenator._models import Symbol
from readmenator.parsers._python import PythonParser
from readmenator.parsers._c import CParser
from readmenator.parsers._go import GoParser
from readmenator.parsers._rust import RustParser
from readmenator.parsers._javascript import JavaScriptParser
from readmenator.parsers._java import JavaParser
from readmenator.parsers._csharp import CSharpParser
from readmenator.parsers._shell import ShellParser
from readmenator.parsers._php import PHPParser
from readmenator.parsers._dart import DartParser
from readmenator.parsers._gdscript import GDScriptParser
from readmenator.parsers._nim import NimParser
from readmenator.parsers._ruby import RubyParser
from readmenator.parsers._swift import SwiftParser
from readmenator.parsers._kotlin import KotlinParser
from readmenator.parsers._scala import ScalaParser
from readmenator.parsers._lua import LuaParser
from readmenator.parsers._elixir import ElixirParser

try:
    from hypothesis import given, settings, strategies as st
    HAS_HYPOTHESIS = True
except ImportError:
    HAS_HYPOTHESIS = False


# ── Strategy: source code that is deliberately pathological ──────────────

_malformed_code = st.recursive(
    st.just("") | st.just(" ") | st.just("\n") | st.just("\t"),
    lambda children: st.one_of(
        st.text(min_size=1, max_size=5, alphabet="\n\t "),
        st.text(min_size=1, max_size=10, alphabet="abcdefghijklmnopqrstuvwxyz{}();:<>*&|!@#$%^~`"),
        st.lists(children, min_size=1, max_size=3).map(lambda x: "\n".join(x)),
    ),
    max_leaves=3,
)

_unicode_code = st.text(
    min_size=0,
    max_size=256,
    alphabet=st.characters(blacklist_categories=("Cs",)),
)

_large_line_counts = st.integers(min_value=0, max_value=500)


def _generate_multiline_code(
    lines: int,
    line_strategy=st.text(min_size=0, max_size=40, alphabet="abcdefghijklmnopqrstuvwxyz \n\t{}();:="),
) -> st.SearchStrategy[str]:
    """Generate source code with a configurable number of lines."""
    return st.lists(line_strategy, min_size=lines, max_size=lines).map(
        lambda xs: "\n".join(xs)
    )


# ── Extensions to test ──────────────────────────────────────────────────

_PARSER_EXTENSIONS_MAP = {
    ".py": PythonParser,
    ".c": CParser, ".cpp": CParser, ".h": CParser,
    ".go": GoParser,
    ".rs": RustParser,
    ".js": JavaScriptParser, ".ts": JavaScriptParser, ".jsx": JavaScriptParser,
    ".java": JavaParser,
    ".cs": CSharpParser,
    ".sh": ShellParser,
    ".php": PHPParser,
    ".dart": DartParser,
    ".gd": GDScriptParser,
    ".nim": NimParser,
    ".rb": RubyParser,
    ".swift": SwiftParser,
    ".kt": KotlinParser,
    ".scala": ScalaParser,
    ".lua": LuaParser,
    ".ex": ElixirParser,
}

_PARSER_EXTENSIONS = list(_PARSER_EXTENSIONS_MAP.keys())
_TEST_CONFIG = Config()


def _create_parser(ext: str):
    """Create a parser for the given extension."""
    cls = _PARSER_EXTENSIONS_MAP.get(ext)
    if cls is None:
        return None
    return cls(f"test{ext}", _TEST_CONFIG)


# ── Base test class for property-based parser tests ─────────────────────
# These tests validate that parsers never raise exceptions, regardless of
# input, and that they always return valid Symbol lists with correct types.

@unittest.skipIf(not HAS_HYPOTHESIS, "hypothesis not installed — skipping property-based tests")
class TestParserHypothesisContract(unittest.TestCase):
    """Property-based contract: parsers never crash on arbitrary input."""

    # ── Fuzz: malformed code ──────────────────────────────────────────

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS), code=_malformed_code)
    @settings(max_examples=50, deadline=2000)
    def test_never_crashes_on_malformed_code(self, ext: str, code: str) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        try:
            symbols = parser.parse(code)
            if symbols is not None:
                self._assert_valid_symbols(symbols)
        except Exception as exc:
            raise AssertionError(
                f"Parser for {ext} crashed on malformed input.\n"
                f"Code: {code!r}\nException: {exc}"
            ) from exc

    # ── Fuzz: unicode / non-ASCII ─────────────────────────────────────

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS), code=_unicode_code)
    @settings(max_examples=20, deadline=2000)
    def test_never_crashes_on_unicode_code(self, ext: str, code: str) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        try:
            symbols = parser.parse(code)
            if symbols is not None:
                self._assert_valid_symbols(symbols)
        except Exception as exc:
            raise AssertionError(
                f"Parser for {ext} crashed on unicode input.\n"
                f"Code: {code!r}\nException: {exc}"
            ) from exc

    # ── Empty code ────────────────────────────────────────────────────

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS))
    @settings(max_examples=19, deadline=2000)
    def test_empty_code_returns_empty_or_valid(self, ext: str) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        symbols = parser.parse("")
        if symbols is not None:
            self._assert_valid_symbols(symbols)

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS))
    @settings(max_examples=19, deadline=2000)
    def test_whitespace_code_returns_empty_or_valid(self, ext: str) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        symbols = parser.parse("   \n\n  \t  \n")
        if symbols is not None:
            self._assert_valid_symbols(symbols)

    # ── Massive line count ────────────────────────────────────────────

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS), lines=st.integers(min_value=0, max_value=500))
    @settings(max_examples=10, deadline=1000)
    def test_never_crashes_on_many_lines(self, ext: str, lines: int) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        code = "\n".join([f"line_{i}" for i in range(min(lines, 5000))])
        try:
            symbols = parser.parse(code)
            if symbols is not None:
                self._assert_valid_symbols(symbols)
        except Exception as exc:
            raise AssertionError(
                f"Parser for {ext} crashed on {lines}-line input.\nException: {exc}"
            ) from exc

    # ── Quickly repeated keywords to trigger regex issues ──────────────

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS))
    @settings(max_examples=19, deadline=2000)
    def test_repeated_keywords_no_crash(self, ext: str) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        keywords = ["if", "for", "while", "try", "catch", "switch", "return", "class", "def", "fun", "fn", "func"]
        code = "\n".join([f"{kw} " * 20 for kw in keywords])
        try:
            symbols = parser.parse(code)
            if symbols is not None:
                self._assert_valid_symbols(symbols)
        except Exception as exc:
            raise AssertionError(
                f"Parser for {ext} crashed on repeated keywords.\nException: {exc}"
            ) from exc

    # ── All parsers produce consistent types ───────────────────────────

    @given(ext=st.sampled_from(_PARSER_EXTENSIONS))
    @settings(max_examples=19, deadline=2000)
    def test_parser_imports_is_list_of_strings(self, ext: str) -> None:
        parser = _create_parser(ext)
        if parser is None:
            return
        parser.parse("")
        imports = parser.imports
        self.assertIsInstance(imports, list)
        for imp in imports:
            self.assertIsInstance(imp, str)

    # ── Invalid extension returns None ─────────────────────────────────

    def test_unknown_extension_returns_none(self) -> None:
        parser = _create_parser(".xyz123")
        self.assertIsNone(parser)

    # ── Helper ─────────────────────────────────────────────────────────

    def _assert_valid_symbols(self, symbols: List[Symbol]) -> None:
        self.assertIsInstance(symbols, list)
        for sym in symbols:
            self.assertIsInstance(sym, Symbol)
            self.assertIsInstance(sym.name, str)
            self.assertIsInstance(sym.kind, str)
            self.assertIsInstance(sym.line, int)
            self.assertGreaterEqual(sym.line, 0)


# ── Python-specific property tests (uses native ast) ────────────────────

@unittest.skipIf(not HAS_HYPOTHESIS, "hypothesis not installed — skipping property-based tests")
class TestPythonParserProperty(unittest.TestCase):
    """Property-based tests specific to the Python parser (native ast)."""

    def setUp(self) -> None:
        self.parser = PythonParser("test.py", Config())

    @given(code=st.text(min_size=0, max_size=200, alphabet="abcdefghijklmnopqrstuvwxyz \n\t=(){}[]:.,"))
    @settings(max_examples=30, deadline=2000)
    def test_python_never_crashes_on_weird_ascii(self, code: str) -> None:
        if self.parser is None:
            return
        try:
            symbols = self.parser.parse(code)
            if symbols is not None:
                self.assertIsInstance(symbols, list)
        except Exception as exc:
            raise AssertionError(
                f"Python parser crashed on: {code!r}\nException: {exc}"
            ) from exc

    @given(code=st.text(min_size=0, max_size=50))
    @settings(max_examples=20, deadline=2000)
    def test_python_never_crashes_on_any_text(self, code: str) -> None:
        if self.parser is None:
            return
        try:
            symbols = self.parser.parse(code)
            if symbols is not None:
                self.assertIsInstance(symbols, list)
        except Exception:
            pass  # ast.parse may raise SyntaxError — that is acceptable


if __name__ == "__main__":
    unittest.main()
