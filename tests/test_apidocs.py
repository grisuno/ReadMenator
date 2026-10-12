"""Contract tests for the docstring parser and the deterministic API reference."""

from __future__ import annotations

import json
import re
import shutil
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from readmenator._apidocs import (
    WARN_PARAM_MISSING,
    WARN_PARAM_UNKNOWN,
    WARN_RAISE_MISSING,
    WARN_RETURN_MISSING,
    WARN_UNDOCUMENTED,
    ApiReferenceBuilder,
    parse_signature_params,
)
from readmenator._apidocs_page import render_api_site
from readmenator._apidocs_render import ApiDocsWriter, ApiLinker, ApiMarkdownRenderer, page_slug
from readmenator._app import readmenatorApplication
from readmenator._config import Config
from readmenator._docstrings import (
    STYLE_GOOGLE,
    STYLE_NUMPY,
    STYLE_REST,
    STYLE_RUSTDOC,
    STYLE_TAGS,
    STYLE_XML,
    detect_style,
    parse_docstring,
    recover_comment,
)
from readmenator._models import Edge, Node, Symbol

PY_SOURCE = '''"""Geometry helpers for the demo package."""

__all__ = ["Shape", "Circle", "area_of", "describe", "MAX_SIDES"]

MAX_SIDES = 12
"""Upper bound on polygon sides."""


class Shape:
    """Base shape.

    Attributes:
        name: Display name.
    """

    def area(self) -> float:
        """Return the area.

        Returns:
            float: Surface in square units.
        """
        raise NotImplementedError


class Circle(Shape):
    """A circle.

    Args:
        radius: Circle radius.
    """

    def __init__(self, radius: float = 1.0) -> None:
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def diameter(self) -> float:
        """Twice the radius."""
        return 2 * self.radius

    def scale(self, factor: float, *, clamp: bool = False) -> "Circle":
        """Scale the circle.

        Args:
            factor: Multiplier.
            ghost: Not a real parameter.
        """
        if factor < 0:
            raise ValueError("negative")
        return Circle(self.radius * factor)


def area_of(shape: Shape, /, precise: bool = True, *extra, **opts) -> float:
    """Compute the area of a shape.

    :param shape: Any shape.
    :type shape: Shape
    :param precise: Use full precision.
    :returns: The area.
    :rtype: float
    """
    return shape.area()


def describe(obj) -> str:
    """Describe an untyped object."""
    return str(obj.scale(2))


def _hidden():
    return 1


def undocumented(x):
    return area_of(x)
'''

C_HEADER = """#ifndef GEO_H
#define GEO_H

/**
 * @brief Open a device.
 * @param path Device path.
 * @param flags Open flags.
 * @return 0 on success.
 */
int dev_open(const char *path, int flags);

#endif
"""

C_SOURCE = """#include "geo.h"

static int helper(int x) { return x; }

int dev_open(const char *path, int flags) {
    return helper(flags);
}
"""


def _project() -> tuple:
    """Build nodes, edges, and contents for a small mixed project."""
    contents = {"demo/geo.py": PY_SOURCE, "demo/geo.h": C_HEADER, "demo/geo.c": C_SOURCE,
                "tests/test_geo.py": "def test_x():\n    pass\n"}
    nodes = [
        Node("demo/geo.py", "geo.py", "module", "py", "Geometry helpers for the demo package.", []),
        Node("demo/geo.h", "geo.h", "module", "h", "", [
            Symbol("GEO_H", "macro", 2), Symbol("dev_open", "function", 10, "", "int dev_open(const char *path, int flags);"),
        ]),
        Node("demo/geo.c", "geo.c", "module", "c", "", [
            Symbol("helper", "function", 3), Symbol("dev_open", "function", 5, "", "int dev_open(const char *path, int flags)"),
        ]),
        Node("tests/test_geo.py", "test_geo.py", "module", "py", "", [Symbol("test_x", "function", 1)]),
    ]
    edges = [Edge("demo/geo.c", "geo.h", "imports")]
    resolved = [Edge("demo/geo.c", "demo/geo.h", "resolved_imports")]
    return nodes, edges, resolved, contents


class TestDocstringParser(unittest.TestCase):
    """Contract: every documented convention parses into the same structure."""

    def test_docstrings_google_sections(self) -> None:
        doc = parse_docstring(
            "Do it.\n\nArgs:\n    x (int): The x.\n        More.\n    y: The y. Defaults to 3.\n\n"
            "Returns:\n    dict: Mapping.\n\nRaises:\n    ValueError: Bad.\n\nExample:\n    >>> f(1)\n    2\n"
        )
        self.assertEqual(doc.style, STYLE_GOOGLE)
        self.assertEqual(doc.summary, "Do it.")
        self.assertEqual([p.name for p in doc.params], ["x", "y"])
        self.assertEqual(doc.params[0].type, "int")
        self.assertIn("More.", doc.params[0].description)
        self.assertEqual(doc.params[1].default, "3")
        self.assertEqual(doc.returns.type, "dict")
        self.assertEqual(doc.raises[0].name, "ValueError")
        self.assertEqual(doc.examples, [">>> f(1)\n2"])

    def test_docstrings_numpy_sections(self) -> None:
        doc = parse_docstring(
            "Sum.\n\nParameters\n----------\na : int\n    First.\nb : float, optional\n    Second.\n\n"
            "Returns\n-------\nfloat\n    The sum.\n\nSee Also\n--------\nmean, median\n"
        )
        self.assertEqual(doc.style, STYLE_NUMPY)
        self.assertEqual([(p.name, p.type) for p in doc.params], [("a", "int"), ("b", "float")])
        self.assertEqual(doc.returns.type, "float")
        self.assertEqual(doc.see_also, ["mean", "median"])

    def test_docstrings_rest_fields_and_directives(self) -> None:
        doc = parse_docstring(
            "Go.\n\n:param int a: first\n:param b: second\n:type b: str\n:returns: ok\n:rtype: bool\n"
            ":raises KeyError: missing\n\n.. deprecated:: 2.0 use other\n.. note:: Careful.\n"
        )
        self.assertEqual(doc.style, STYLE_REST)
        self.assertEqual([(p.name, p.type) for p in doc.params], [("a", "int"), ("b", "str")])
        self.assertEqual((doc.returns.type, doc.returns.description), ("bool", "ok"))
        self.assertEqual(doc.raises[0].name, "KeyError")
        self.assertTrue(doc.deprecated.startswith("2.0"))
        self.assertIn(("Note", "Careful."), doc.notes)

    def test_docstrings_jsdoc_and_doxygen_tags(self) -> None:
        doc = parse_docstring(
            "Fetch.\n@param {string} id - The id.\n@param {number} [limit=10] Max.\n"
            "@returns {Promise<User>} The user.\n@throws {Error} Missing.\n@example\nfetch(1)\n@see load\n"
        )
        self.assertEqual(doc.style, STYLE_TAGS)
        self.assertEqual([(p.name, p.type, p.default) for p in doc.params],
                         [("id", "string", ""), ("limit", "number", "10")])
        self.assertEqual(doc.returns.type, "Promise<User>")
        self.assertEqual(doc.examples, ["fetch(1)"])
        self.assertEqual(doc.see_also, ["load"])
        brief = parse_docstring("\\brief Open.\n\\param[in] path Device.\n\\return 0 on success.")
        self.assertEqual(brief.summary, "Open.")
        self.assertEqual(brief.params[0].name, "path")

    def test_docstrings_phpdoc_type_before_variable(self) -> None:
        doc = parse_docstring("Run.\n@param string $name The name.")
        self.assertEqual((doc.params[0].name, doc.params[0].type), ("$name", "string"))

    def test_docstrings_csharp_xml(self) -> None:
        doc = parse_docstring(
            '<summary>Adds <paramref name="a"/>.</summary>\n<param name="a">First.</param>\n'
            '<returns>The sum.</returns>\n<exception cref="T:System.ArgumentException">Bad.</exception>'
        )
        self.assertEqual(doc.style, STYLE_XML)
        self.assertEqual(doc.summary, "Adds `a`.")
        self.assertEqual(doc.raises[0].name, "System.ArgumentException")

    def test_docstrings_rustdoc_sections(self) -> None:
        doc = parse_docstring("Parse.\n\n# Arguments\n\n* `input` - Text.\n\n# Examples\n\n```\nparse(1)\n```\n")
        self.assertEqual(doc.style, STYLE_RUSTDOC)
        self.assertEqual(doc.params[0].name, "input")
        self.assertEqual(doc.examples, ["parse(1)"])

    def test_docstrings_plain_and_empty(self) -> None:
        self.assertTrue(parse_docstring("").is_empty)
        doc = parse_docstring("One sentence. Second sentence here.")
        self.assertEqual(doc.summary, "One sentence.")
        self.assertEqual(doc.description, "Second sentence here.")
        self.assertEqual(detect_style("Just text."), "plain")

    def test_docstrings_recover_block_and_line_comments(self) -> None:
        lines = ["", "/**", " * @brief Open.", " * @param p Path.", " */", "[[nodiscard]]", "int f(int p);"]
        self.assertEqual(recover_comment(lines, 7, "cpp", 40), "@brief Open.\n@param p Path.")
        rust = ["/// Adds one.", "///", "/// # Examples", "#[inline]", "pub fn add() {}"]
        self.assertEqual(recover_comment(rust, 5, "rs", 40), "Adds one.\n\n# Examples")
        self.assertEqual(recover_comment(["#!/bin/sh", "run() {"], 2, "sh", 40), "")
        self.assertEqual(recover_comment(["int x;", "", "void f() {"], 3, "c", 40), "")

    def test_docstrings_recover_elixir_doc_heredoc(self) -> None:
        lines = ['  @doc """', "  Greets.", '  """', "  def hi do"]
        self.assertEqual(recover_comment(lines, 4, "ex", 40), "Greets.")


class TestApiReferenceBuilder(unittest.TestCase):
    """Contract: extraction, nesting, cross-references, coverage, and warnings."""

    @classmethod
    def setUpClass(cls) -> None:
        nodes, edges, resolved, contents = _project()
        cls.ref = ApiReferenceBuilder(Config()).build(nodes, edges, resolved, contents)

    def test_apidocs_python_signatures_exact(self) -> None:
        entity = self.ref.entities["demo/geo.py::area_of"]
        self.assertEqual(
            entity.signature,
            "def area_of(shape: Shape, /, precise: bool = True, *extra, **opts) -> float",
        )
        self.assertEqual([p.kind for p in entity.params],
                         ["positional_only", "positional", "var_positional", "var_keyword"])
        scale = self.ref.entities["demo/geo.py::Circle.scale"]
        self.assertEqual(scale.signature, 'def scale(self, factor: float, *, clamp: bool = False) -> \'Circle\'')
        self.assertEqual([p.name for p in scale.params], ["factor", "clamp"])

    def test_apidocs_python_nesting_and_kinds(self) -> None:
        circle = self.ref.entities["demo/geo.py::Circle"]
        kinds = {self.ref.entities[m].name: self.ref.entities[m].kind for m in circle.members}
        self.assertEqual(kinds["__init__"], "constructor")
        self.assertEqual(kinds["diameter"], "property")
        self.assertEqual(kinds["scale"], "method")
        self.assertEqual(self.ref.entities["demo/geo.py::MAX_SIDES"].doc.summary, "Upper bound on polygon sides.")

    def test_apidocs_python_all_and_private_filter(self) -> None:
        self.assertNotIn("demo/geo.py::_hidden", self.ref.entities)
        self.assertNotIn("demo/geo.py::undocumented", self.ref.entities)
        cfg = replace(Config(), APIDOCS_INCLUDE_PRIVATE=True)
        nodes, edges, resolved, contents = _project()
        ref = ApiReferenceBuilder(cfg).build(nodes, edges, resolved, contents)
        self.assertEqual(ref.entities["demo/geo.py::undocumented"].visibility, "private")
        self.assertEqual(ref.entities["demo/geo.py::_hidden"].visibility, "private")

    def test_apidocs_tests_excluded_by_default(self) -> None:
        self.assertNotIn("tests/test_geo.py", self.ref.modules)
        nodes, edges, resolved, contents = _project()
        cfg = replace(Config(), APIDOCS_INCLUDE_TESTS=True)
        ref = ApiReferenceBuilder(cfg).build(nodes, edges, resolved, contents)
        self.assertIn("tests/test_geo.py", ref.modules)

    def test_apidocs_constructor_inherits_class_args(self) -> None:
        init = self.ref.entities["demo/geo.py::Circle.__init__"]
        self.assertEqual(init.doc.param("radius").description, "Circle radius.")

    def test_apidocs_inheritance_links_and_doc_inheritance(self) -> None:
        circle = self.ref.entities["demo/geo.py::Circle"]
        shape = self.ref.entities["demo/geo.py::Shape"]
        self.assertEqual(circle.base_uids, [shape.uid])
        self.assertIn(circle.uid, shape.subclasses)
        area = self.ref.entities["demo/geo.py::Circle.area"]
        self.assertEqual(area.doc.summary, "Return the area.")
        self.assertTrue(any(label == "Inherited" for label, _ in area.doc.notes))

    def test_apidocs_c_prototype_doc_merges_into_definition(self) -> None:
        definition = self.ref.entities["demo/geo.c::dev_open"]
        self.assertEqual(definition.doc.summary, "Open a device.")
        self.assertEqual([p.name for p in definition.params], ["path", "flags"])
        self.assertEqual(definition.returns, "int")
        self.assertNotIn("demo/geo.c::helper", self.ref.entities)
        self.assertNotIn("demo/geo.h::GEO_H", self.ref.entities)

    def test_apidocs_call_graph_resolved(self) -> None:
        scale = self.ref.entities["demo/geo.py::Circle.scale"]
        self.assertIn("demo/geo.py::Circle.__init__", scale.calls)
        init = self.ref.entities["demo/geo.py::Circle.__init__"]
        self.assertIn(scale.uid, init.called_by)

    def test_apidocs_receiver_filter_drops_unproven_method_calls(self) -> None:
        describe = self.ref.entities["demo/geo.py::describe"]
        self.assertEqual(describe.calls, [])

    def test_apidocs_annotated_receiver_resolves_method(self) -> None:
        area_of = self.ref.entities["demo/geo.py::area_of"]
        self.assertEqual(area_of.calls, ["demo/geo.py::Shape.area"])

    def test_apidocs_warnings_cover_every_rule(self) -> None:
        codes = {(w.code, w.uid) for w in self.ref.warnings}
        self.assertIn((WARN_PARAM_UNKNOWN, "demo/geo.py::Circle.scale"), codes)
        self.assertIn((WARN_PARAM_MISSING, "demo/geo.py::Circle.scale"), codes)
        self.assertIn((WARN_RETURN_MISSING, "demo/geo.py::Circle.scale"), codes)
        self.assertIn((WARN_RAISE_MISSING, "demo/geo.py::Circle.scale"), codes)
        undocumented = {uid for code, uid in codes if code == WARN_UNDOCUMENTED}
        self.assertIn("demo/geo.c", undocumented)
        self.assertNotIn("demo/geo.py::Circle.__init__", undocumented)

    def test_apidocs_coverage_counts(self) -> None:
        overall = self.ref.coverage["overall"]
        self.assertGreater(overall["total"], 0)
        self.assertEqual(overall["percent"], round(100.0 * overall["documented"] / overall["total"], 1))
        self.assertIn("demo/geo.py", self.ref.coverage["by_module"])

    def test_apidocs_deterministic(self) -> None:
        nodes, edges, resolved, contents = _project()
        again = ApiReferenceBuilder(Config()).build(nodes, edges, resolved, contents)
        self.assertEqual(
            json.dumps(again.to_dict(1), sort_keys=True),
            json.dumps(self.ref.to_dict(1), sort_keys=True),
        )

    def test_apidocs_privacy_mode_strips_text(self) -> None:
        nodes, edges, resolved, contents = _project()
        ref = ApiReferenceBuilder(replace(Config(), PRIVACY_MODE=True)).build(nodes, edges, resolved, contents)
        for entity in ref.entities.values():
            self.assertEqual(entity.doc.summary, "")
            self.assertEqual(entity.doc.description, "")
            self.assertEqual(entity.value, "")

    def test_apidocs_entity_budget_truncates(self) -> None:
        nodes, edges, resolved, contents = _project()
        ref = ApiReferenceBuilder(replace(Config(), APIDOCS_MAX_ENTITIES=3)).build(nodes, edges, resolved, contents)
        self.assertLessEqual(len(ref.entities), 3)
        self.assertTrue(ref.meta["truncated"])

    def test_apidocs_without_content_uses_parser_symbols(self) -> None:
        nodes, edges, resolved, _ = _project()
        ref = ApiReferenceBuilder(Config()).build(nodes, edges, resolved, None)
        self.assertIn("demo/geo.c::dev_open", ref.entities)


class TestSignatureParsing(unittest.TestCase):
    """Contract: non-Python signatures split into typed parameters and returns."""

    def test_apidocs_signature_languages(self) -> None:
        params, ret = parse_signature_params("pub fn add(a: i32, b: i32) -> i32", "add", "rs")
        self.assertEqual([(p.name, p.annotation) for p in params], [("a", "i32"), ("b", "i32")])
        self.assertEqual(ret, "i32")
        params, ret = parse_signature_params("func Sum(xs []int, base int) int", "Sum", "go")
        self.assertEqual([(p.name, p.annotation) for p in params], [("xs", "[]int"), ("base", "int")])
        self.assertEqual(ret, "int")
        params, ret = parse_signature_params("public Map<String, List<Integer>> load(final String id, int n)", "load", "java")
        self.assertEqual([p.name for p in params], ["id", "n"])
        self.assertEqual(ret, "Map<String, List<Integer>>")
        params, ret = parse_signature_params("async fetch(id: string, limit: number = 10): Promise<User>", "fetch", "ts")
        self.assertEqual([(p.name, p.default) for p in params], [("id", ""), ("limit", "10")])
        self.assertEqual(ret, "Promise<User>")
        params, _ = parse_signature_params("function run(string $name, int $n = 2)", "run", "php")
        self.assertEqual([(p.name, p.annotation, p.default) for p in params],
                         [("$name", "string", ""), ("$n", "int", "2")])
        params, _ = parse_signature_params("int printf(const char *fmt, ...)", "printf", "c")
        self.assertEqual(params[-1].kind, "var_positional")


class TestApiRendering(unittest.TestCase):
    """Contract: Markdown pages, cross-links, HTML escaping, and the writer."""

    @classmethod
    def setUpClass(cls) -> None:
        nodes, edges, resolved, contents = _project()
        cls.config = Config()
        cls.ref = ApiReferenceBuilder(cls.config).build(nodes, edges, resolved, contents)
        cls.pages = ApiMarkdownRenderer(cls.config).render(cls.ref, "Demo")

    def test_apidocs_pages_layout(self) -> None:
        for name in ("index.md", "classes.md", "genindex.md", "COVERAGE.md"):
            self.assertIn(name, self.pages)
        self.assertIn(f"modules/{page_slug('demo/geo.py')}.md", self.pages)

    def test_apidocs_module_page_sections(self) -> None:
        page = self.pages[f"modules/{page_slug('demo/geo.py')}.md"]
        self.assertIn("# `demo.geo`", page)
        self.assertIn('<a id="circle-scale"></a>', page)
        self.assertIn("| `factor` | `float` |", page)
        self.assertIn("```mermaid\nclassDiagram", page)
        self.assertIn("Shape <|-- Circle", page)
        self.assertIn("**Raises**", page)
        self.assertIn("(raised in the body, not documented)", page)
        self.assertIn("../../demo/geo.py#L", page)

    def test_apidocs_hierarchy_nests_subclasses(self) -> None:
        hierarchy = self.pages["classes.md"]
        self.assertRegex(hierarchy, r"- \[`Shape`\].*\n  - \[`Circle`\]")

    def test_apidocs_linker_resolves_references(self) -> None:
        linker = ApiLinker(self.ref)
        text = linker.autolink("Use `Circle` or :class:`demo.geo.Shape` and `unknown_thing`.", "demo/geo.py")
        self.assertIn("[`Circle`](#circle)", text)
        self.assertIn("[`demo.geo.Shape`](#shape)", text)
        self.assertIn("`unknown_thing`", text)
        fenced = linker.autolink("```\n`Circle`\n```", "demo/geo.py")
        self.assertNotIn("](#circle)", fenced)

    def test_apidocs_html_is_self_contained_and_escaped(self) -> None:
        site = render_api_site(self.ref, "<Demo & co>", self.config)
        self.assertIn("&lt;Demo &amp; co&gt; API Reference", site)
        payload = re.search(r'<script type="application/json" id="api-data">(.*?)</script>', site, re.S).group(1)
        self.assertNotIn("<", payload)
        self.assertIsNotNone(json.loads(payload))
        self.assertNotRegex(site, r'<script[^>]+src=|<link[^>]+href="http')

    def test_apidocs_html_placeholder_in_payload_stays_literal(self) -> None:
        site = render_api_site(self.ref, "@@DATA@@", self.config)
        self.assertEqual(site.count('id="api-data"'), 1)

    def test_apidocs_writer_writes_and_prunes(self) -> None:
        tmp = Path(tempfile.mkdtemp())
        try:
            stale = tmp / self.config.APIDOCS_OUTPUT_DIR / self.config.APIDOCS_MODULES_SUBDIR / "old.md"
            stale.parent.mkdir(parents=True)
            stale.write_text("x", encoding="utf-8")
            written = ApiDocsWriter(self.config).write(self.ref, str(tmp), "Demo")
            self.assertFalse(stale.exists())
            self.assertIn("api.json", written)
            data = json.loads(Path(written["api.json"]).read_text(encoding="utf-8"))
            self.assertEqual(data["schema_version"], self.config.APIDOCS_SCHEMA_VERSION)
            self.assertTrue(Path(written["index.html"]).is_file())
        finally:
            shutil.rmtree(tmp)

    def test_apidocs_writer_refuses_symlinked_output(self) -> None:
        tmp = Path(tempfile.mkdtemp())
        outside = Path(tempfile.mkdtemp())
        try:
            (tmp / self.config.APIDOCS_OUTPUT_DIR).symlink_to(outside, target_is_directory=True)
            with self.assertRaises(OSError):
                ApiDocsWriter(self.config).write(self.ref, str(tmp), "Demo")
        finally:
            shutil.rmtree(tmp)
            shutil.rmtree(outside)


class TestApiDocsIntegration(unittest.TestCase):
    """Contract: CLI-facing app methods and scanner skipping of the output dir."""

    def test_apidocs_app_export_and_scanner_skip(self) -> None:
        tmp = Path(tempfile.mkdtemp())
        try:
            pkg = tmp / "demo"
            pkg.mkdir()
            (pkg / "geo.py").write_text(PY_SOURCE, encoding="utf-8")
            app = readmenatorApplication(Config())
            written = app.export_apidocs(str(tmp))
            self.assertIn("index.md", written)
            out = tmp / Config().APIDOCS_OUTPUT_DIR / "modules" / "leak.py"
            out.write_text("def leak():\n    pass\n", encoding="utf-8")
            reference = app.build_api_reference(str(tmp))
            self.assertNotIn(f"{Config().APIDOCS_OUTPUT_DIR}/modules/leak.py", reference.modules)
            self.assertIn("demo/geo.py", reference.modules)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
