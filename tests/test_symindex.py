"""Contract tests for the deterministic symbol index."""

from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol
from readmenator._symindex import SymbolIndex


def _node(nid: str, *names: str) -> Node:
    """Build a file node with function symbols starting at line 1, step 3."""
    return Node(
        nid, nid.split("/")[-1], "module", "py", "",
        [Symbol(name, "function", 1 + pos * 3) for pos, name in enumerate(names)],
    )


class TestSymbolIndexContract(unittest.TestCase):
    """Contract: spans, call-site lines, and confidence tiers."""

    def setUp(self) -> None:
        """Build a two-file project with a cross-file call."""
        self.config = Config()
        self.index = SymbolIndex(self.config)
        self.nodes = [_node("a.py", "foo", "bar"), _node("b.py", "baz")]
        self.content = {
            "a.py": "def foo():\n    bar()\n    return 1\ndef bar():\n    return 2\n",
            "b.py": "from a import foo\ndef baz():\n    foo()\n",
        }

    def test_build_assigns_spans(self) -> None:
        """Definitions carry line spans up to the next symbol."""
        built = self.index.build(self.nodes, self.content)
        foo = next(s for s in built["a.py"] if s.name == "foo")
        self.assertEqual((foo.line, foo.end_line), (1, 3))
        self.assertEqual(foo.qualified, "a.py::foo")

    def test_python_call_sites_carry_lines(self) -> None:
        """Python calls resolve with exact lines and callers."""
        sites = self.index.extract_call_sites("a.py", self.content["a.py"], "py")
        bar = next(s for s in sites if s.callee == "bar")
        self.assertEqual((bar.line, bar.caller), (2, "foo"))

    def test_resolve_prefers_same_file(self) -> None:
        """A call matching a same-file def wins with SAME_FILE."""
        resolved = self.index.resolve(
            self.nodes, [], [Edge("b.py", "a.py", "resolved_imports")], self.content
        )
        bar = next(r for r in resolved if r.site.callee == "bar")
        self.assertEqual((bar.confidence, bar.target_file, bar.target_line), ("SAME_FILE", "a.py", 4))

    def test_resolve_follows_imports(self) -> None:
        """A call matching an imported file resolves as IMPORTED."""
        resolved = self.index.resolve(
            self.nodes, [], [Edge("b.py", "a.py", "resolved_imports")], self.content
        )
        foo = next(r for r in resolved if r.site.file == "b.py" and r.site.callee == "foo")
        self.assertEqual((foo.confidence, foo.target_file), ("IMPORTED", "a.py"))

    def test_unresolved_and_builtin_tiers(self) -> None:
        """Unknown names are UNRESOLVED, builtins are BUILTIN."""
        nodes = [_node("a.py", "foo")]
        content = {"a.py": "def foo():\n    missing_thing()\n    print(1)\n"}
        resolved = self.index.resolve(nodes, [], [], content)
        by_callee = {r.site.callee: r.confidence for r in resolved}
        self.assertEqual(by_callee.get("missing_thing"), "UNRESOLVED")
        self.assertEqual(by_callee.get("print"), "BUILTIN")

    def test_methods_index_matches_pipe_keys(self) -> None:
        """methods_index keys look like file|file::name with line spans."""
        methods = self.index.methods_index(self.index.build(self.nodes, self.content))
        entry = methods["a.py|a.py::foo"]
        self.assertEqual(
            (entry["file_path"], entry["start_line"], entry["type"]),
            ("a.py", 1, "FUNCTION"),
        )
        self.assertEqual(len(str(entry["content_hash"])), 16)

    def test_edge_fallback_without_content(self) -> None:
        """Parser edges still resolve when content is missing."""
        resolved = self.index.resolve(
            self.nodes,
            [Edge("b.py::baz", "b.py::foo", "calls"), Edge("a.py::foo", "a.py::bar", "calls")],
            [],
            None,
        )
        self.assertTrue(any(r.confidence == "SAME_FILE" for r in resolved))
        self.assertTrue(all(r.site.line == 0 for r in resolved))


if __name__ == "__main__":
    unittest.main()
