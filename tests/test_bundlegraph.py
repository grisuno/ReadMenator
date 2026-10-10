"""Contract tests for the edge bundle explorer (circle and sphere views)."""

from __future__ import annotations

import json
import math
import re
import tempfile
import unittest
from pathlib import Path

from readmenator._bundlegraph import UNASSIGNED_KEY, BundleGraphRenderer
from readmenator._config import Config
from readmenator._forcegraph import ForceGraphRenderer
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node, Symbol


def _node(nid: str, doc: str = "Purpose sentence.") -> Node:
    """Build a file node with one symbol."""
    return Node(nid, nid.split("/")[-1], "module", "python", doc, [Symbol("f", "function", 1)])


def _fixture(config: Config) -> dict:
    """Force-graph payload with two communities, one loose file, and duplicate edges."""
    nodes = [_node("pkg/a.py"), _node("pkg/b.py"), _node("lib/c.py"), _node("lib/d.py"), _node("loose.py")]
    resolved = [
        Edge("pkg/a.py", "pkg/b.py", "resolved_imports"),
        Edge("pkg/a.py", "lib/c.py", "resolved_imports"),
        Edge("lib/d.py", "lib/c.py", "resolved_imports"),
        Edge("lib/d.py", "pkg/b.py", "resolved_imports"),
        Edge("loose.py", "pkg/b.py", "resolved_imports"),
    ]
    edges = [Edge("pkg/a.py", "pkg/b.py", "calls"), Edge("pkg/a.py", "os", "imports")]
    analysis = AnalysisResult(
        god_nodes=[("pkg/b.py", 3.0)],
        communities=[
            CommunityResult(0, "pkg", {"pkg/a.py", "pkg/b.py"}, 0.5, 2),
            CommunityResult(1, "lib", {"lib/c.py", "lib/d.py"}, 0.5, 2),
        ],
        surprising_connections=[],
        suggested_questions=[],
        node_count=5,
        edge_count=5,
    )
    return ForceGraphRenderer(config).build_payload(nodes, edges, resolved, analysis, {"pkg/a.py": "presentation"}, [])


def _script_json(html: str, name: str) -> dict:
    """Extract one inline JSON constant from the rendered page."""
    match = re.search(r"const " + name + r"=(.*?);\n", html, re.S)
    assert match is not None
    return json.loads(match.group(1))


class TestBundleGraphPayloadContract(unittest.TestCase):
    """Contract: groups by community, PageRank order, circle and sphere coordinates, deduplicated edges."""

    def setUp(self) -> None:
        """Build the payload once."""
        self.config = Config()
        self.renderer = BundleGraphRenderer(self.config)
        self.payload = self.renderer.build_payload(_fixture(self.config))

    def test_bundlegraph_groups_follow_community_order_with_unassigned_last(self) -> None:
        """Communities keep analyzer order; files without one form the trailing group."""
        keys = [g["k"] for g in self.payload["groups"]]
        self.assertEqual(keys, ["community:0", "community:1", UNASSIGNED_KEY])
        self.assertEqual([g["n"] for g in self.payload["groups"]], [2, 2, 1])

    def test_bundlegraph_edges_are_distinct_file_pairs(self) -> None:
        """calls and resolved imports between the same files collapse; externals never appear."""
        ids = [n["id"] for n in self.payload["nodes"]]
        pairs = {(ids[a], ids[b]) for a, b in self.payload["edges"]}
        self.assertEqual(len(pairs), len(self.payload["edges"]))
        self.assertIn(("file:pkg/a.py", "file:pkg/b.py"), pairs)
        self.assertEqual(len(pairs), 5)

    def test_bundlegraph_nodes_on_circle_and_sphere(self) -> None:
        """Every file has a circle angle and a unit-sphere position."""
        for node in self.payload["nodes"]:
            self.assertTrue(-math.pi <= node["a"] <= 2 * math.pi)
            self.assertAlmostEqual(math.sqrt(sum(v * v for v in node["p"])), 1.0, places=3)

    def test_bundlegraph_hub_leads_its_arc(self) -> None:
        """The highest PageRank file of a group takes the first slot of its arc."""
        group = self.payload["groups"][0]
        members = [n for n in self.payload["nodes"] if n["g"] == 0]
        top = max(members, key=lambda n: n["r"])
        self.assertEqual(min(members, key=lambda n: n["a"])["id"], top["id"])
        self.assertTrue(group["a0"] <= top["a"] <= group["a1"])

    def test_bundlegraph_empty_payload(self) -> None:
        """No files yields empty lists and an empty thumbnail."""
        empty = {"nodes": [], "edges": []}
        self.assertEqual(self.renderer.build_payload(empty), {"nodes": [], "groups": [], "edges": []})
        self.assertEqual(self.renderer.thumbnail_svg(empty), "")

    def test_bundlegraph_privacy_mode_strips_docs(self) -> None:
        """PRIVACY_MODE leaves no purpose text in the payload."""
        config = Config(PRIVACY_MODE=True)
        payload = BundleGraphRenderer(config).build_payload(_fixture(config))
        self.assertTrue(all(n["d"] == "" for n in payload["nodes"]))


class TestBundleGraphRenderContract(unittest.TestCase):
    """Contract: self-contained page, every placeholder filled, untrusted text escaped."""

    def setUp(self) -> None:
        """Render the page once."""
        self.config = Config()
        self.renderer = BundleGraphRenderer(self.config)
        self.force = _fixture(self.config)
        self.html = self.renderer.render(self.force, title="demo", explorer_href="graph-force.html")

    def test_bundlegraph_render_fills_placeholders(self) -> None:
        """No template token survives and the data parses."""
        self.assertIsNone(re.search(r"__(TITLE|HOME|EXPLORER|DATA|SETTINGS)__", self.html))
        data = _script_json(self.html, "DATA")
        self.assertEqual(len(data["nodes"]), 5)
        settings = _script_json(self.html, "CFG")
        self.assertEqual(settings["beta"], self.config.BUNDLEGRAPH_BETA)
        self.assertEqual(settings["explorerHref"], "graph-force.html")

    def test_bundlegraph_render_has_no_network_requests(self) -> None:
        """The page loads no script, stylesheet, or font from the network."""
        self.assertNotIn("<script src", self.html)
        self.assertNotIn("<link", self.html)
        self.assertNotIn("http://", self.html)
        self.assertNotIn("https://", self.html)

    def test_bundlegraph_render_has_both_views_and_controls(self) -> None:
        """Circle and sphere views, beta slider, crossing filter, and explorer links ship in the page."""
        for marker in ('data-view="2d"', 'data-view="3d"', 'id="beta"', 'id="cross"',
                       'data-color="layer"', 'data-dir="in"', 'href="graph-force.html"', "#node="):
            self.assertIn(marker, self.html)

    def test_bundlegraph_render_escapes_untrusted_text(self) -> None:
        """Labels that try to close the script element stay inert."""
        hostile = Config()
        nodes = [_node("x/</script><img src=x onerror=alert(1)>.py", "</script><b>doc</b>")]
        force = ForceGraphRenderer(hostile).build_payload(nodes, [])
        html = BundleGraphRenderer(hostile).render(force, title="<t>", home_href="a\"b.html")
        self.assertNotIn("</script><img", html)
        self.assertNotIn("<b>doc</b>", html)
        self.assertIn("&lt;t&gt;", html)
        self.assertIn('href="a&quot;b.html"', html)

    def test_bundlegraph_render_payload_naming_a_token_stays_literal(self) -> None:
        """A label containing a placeholder name is not substituted again."""
        force = ForceGraphRenderer(self.config).build_payload([_node("__SETTINGS__.py")], [])
        html = self.renderer.render(force)
        self.assertIn("__SETTINGS__.py", html)

    def test_bundlegraph_thumbnail_is_safe_svg(self) -> None:
        """The thumbnail is a gallery-ready SVG with only numbers and escaped colors."""
        svg = self.renderer.thumbnail_svg(self.force)
        self.assertTrue(svg.startswith('<svg class="thumb"'))
        self.assertIn("<path", svg)
        self.assertNotIn("<script", svg)

    def test_bundlegraph_write_creates_parent(self) -> None:
        """write() creates the destination directory."""
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "maps" / "graph-bundle.html"
            self.renderer.write(target, self.force)
            self.assertTrue(target.is_file())


class TestBundleGraphAppContract(unittest.TestCase):
    """Contract: the gallery and the rebuild path ship the bundle page beside the force graph."""

    def _project(self, tmp: str) -> None:
        """Write a tiny two-file project."""
        Path(tmp, "a.py").write_text("import os\n", encoding="utf-8")
        Path(tmp, "b.py").write_text("import a\n", encoding="utf-8")

    def _config(self, **extra: object) -> Config:
        """Config with heavy sidecars disabled."""
        return Config(WIKI_ENABLED=False, AGENT_OUTPUT_ENABLED=False, VIDEO_ENABLED=False,
                      GH_WIKI_ENABLED=False, **extra)

    def test_export_diagrams_writes_bundle_page_and_card(self) -> None:
        """export_diagrams writes graph-bundle.html and links it from the gallery."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            readmenatorApplication(self._config()).export_diagrams(tmp)
            maps_dir = Path(tmp) / "readmenator-maps"
            page = maps_dir / Config.BUNDLEGRAPH_OUTPUT
            self.assertTrue(page.is_file())
            self.assertIn('href="graph-force.html"', page.read_text(encoding="utf-8"))
            index = (maps_dir / "index.html").read_text(encoding="utf-8")
            self.assertIn('href="graph-bundle.html"', index)
            self.assertIn("Edge Bundle Explorer", index)
            self.assertNotIn("| 2 communities", index)

    def test_bundle_page_skipped_when_disabled(self) -> None:
        """BUNDLEGRAPH_ENABLED=False writes no bundle page and no card."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            readmenatorApplication(self._config(BUNDLEGRAPH_ENABLED=False)).export_diagrams(tmp)
            maps_dir = Path(tmp) / "readmenator-maps"
            self.assertFalse((maps_dir / Config.BUNDLEGRAPH_OUTPUT).exists())
            self.assertNotIn("graph-bundle.html", (maps_dir / "index.html").read_text(encoding="utf-8"))

    def test_export_bundlegraph_cli_entry(self) -> None:
        """export_bundlegraph writes the page into the maps directory."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            out = readmenatorApplication(self._config()).export_bundlegraph(tmp)
            self.assertTrue(out.endswith(Config.BUNDLEGRAPH_OUTPUT))
            self.assertTrue(Path(out).is_file())

    def test_pages_subdir_card_points_into_maps_dir(self) -> None:
        """export_pages links the bundle page inside the maps subdirectory."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            out = Path(tmp) / "site"
            readmenatorApplication(self._config()).export_pages(tmp, str(out))
            subdir = Config.DIAGRAM_MAPS_SUBDIR.strip("/")
            self.assertTrue((out / subdir / Config.BUNDLEGRAPH_OUTPUT).is_file())
            self.assertIn(f'href="{subdir}/graph-bundle.html"', (out / "index.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
