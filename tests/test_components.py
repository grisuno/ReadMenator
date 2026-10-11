"""Contract tests for the component diagram exporter."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from readmenator._components import ComponentDiagramBuilder, sanitize
from readmenator._config import Config
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node, Symbol


def _node(nid: str, *names: str) -> Node:
    """Build a file node with function symbols."""
    return Node(
        nid, nid.split("/")[-1], "module", "py", f"Purpose of {nid}.",
        [Symbol(name, "function", 1 + pos * 3) for pos, name in enumerate(names)],
    )


def _fixture() -> tuple:
    """Two-community project with a cross-component call."""
    nodes = [_node("pkg/a.py", "foo"), _node("pkg/b.py", "bar"), _node("lib/c.py", "baz")]
    content = {
        "pkg/a.py": "from pkg.b import bar\ndef foo():\n    bar()\n",
        "pkg/b.py": "def bar():\n    return 1\n",
        "lib/c.py": "from pkg.b import bar\ndef baz():\n    bar()\n",
    }
    analysis = AnalysisResult(
        god_nodes=[], communities=[
            CommunityResult(0, "pkg", {"pkg/a.py", "pkg/b.py"}, 0.8, 2),
            CommunityResult(1, "lib", {"lib/c.py"}, 1.0, 1),
        ],
        surprising_connections=[], suggested_questions=[],
        node_count=3, edge_count=1,
    )
    resolved = [Edge("pkg/a.py", "pkg/b.py", "resolved_imports"),
                Edge("lib/c.py", "pkg/b.py", "resolved_imports")]
    return nodes, content, analysis, resolved


class TestComponentSchemaContract(unittest.TestCase):
    """Contract: analysis.json uses the stable component/relation top-level schema."""

    def setUp(self) -> None:
        """Build the analysis once."""
        nodes, content, analysis, resolved = _fixture()
        self.builder = ComponentDiagramBuilder(Config())
        self.document = self.builder.build(
            nodes, [], resolved, analysis, "/tmp", content
        )

    def test_top_level_keys_match_schema(self) -> None:
        """metadata, description, files, methods_index, components, relations."""
        self.assertEqual(
            set(self.document),
            {"metadata", "description", "files", "methods_index",
             "components", "components_relations"},
        )
        self.assertIn("source_tree_hash", self.document["metadata"])
        self.assertIn("file_coverage_summary", self.document["metadata"])

    def test_components_carry_entities_and_file_methods(self) -> None:
        """Components expose ids, key entities with lines, and file methods."""
        component = next(c for c in self.document["components"] if c["name"] == "pkg")
        self.assertEqual(component["component_id"], "1")
        self.assertTrue(component["key_entities"])
        entity = component["key_entities"][0]
        self.assertIn("reference_start_line", entity)
        self.assertTrue(any(
            group["file_path"] == "pkg/a.py" for group in component["file_methods"]
        ))

    def test_relations_link_components_with_call_sites(self) -> None:
        """Cross-component calls become relations with method key edges."""
        relations = self.document["components_relations"]
        self.assertEqual(len(relations), 1)
        relation = relations[0]
        self.assertTrue(relation["is_static"])
        self.assertEqual((relation["src_id"], relation["dst_id"]), ("2", "1"))
        edge = relation["key_edges"][0]
        self.assertIn("|", edge["source"])
        self.assertEqual(edge["call_sites"][0]["line"], 3)

    def test_methods_index_keys_use_pipe_separator(self) -> None:
        """methods_index keys look like file|file::symbol."""
        self.assertIn("pkg/a.py|pkg/a.py::foo", self.document["methods_index"])


class TestComponentRenderContract(unittest.TestCase):
    """Contract: graph LR diagram and markdown pages in layered style."""

    def setUp(self) -> None:
        """Build and render once."""
        nodes, content, analysis, resolved = _fixture()
        self.builder = ComponentDiagramBuilder(Config())
        self.document = self.builder.build(
            nodes, [], resolved, analysis, "/tmp", content
        )

    def test_mermaid_matches_layered_style(self) -> None:
        """graph LR with quoted labels, labeled edges, and click links."""
        diagram = self.builder.mermaid_lr(
            self.document["components"], self.document["components_relations"]
        )
        self.assertTrue(diagram.startswith("```mermaid\ngraph LR"))
        self.assertIn('pkg["pkg"]', diagram)
        self.assertIn('-- "calls into" -->', diagram)

    def test_sanitize_for_mermaid_ids(self) -> None:
        """Non-alphanumerics become underscores."""
        self.assertEqual(sanitize("My Component-2!"), "My_Component_2_")

    def test_overview_lists_related_entities(self) -> None:
        """Overview carries Related Classes/Methods with file anchors."""
        overview = self.builder.overview_markdown(self.document)
        self.assertIn("**Related Classes/Methods**", overview)
        self.assertIn("pkg/a.py#L", overview)

    def test_write_emits_analysis_and_pages(self) -> None:
        """write() emits analysis.json plus overview markdown."""
        with tempfile.TemporaryDirectory() as tmp:
            written = self.builder.write(self.document, tmp)
            self.assertTrue(Path(written["analysis"]).is_file())
            stored = json.loads(Path(written["analysis"]).read_text(encoding="utf-8"))
            self.assertEqual(len(stored["components"]), 2)
            self.assertTrue(Path(written["overview"]).is_file())

    def test_empty_project_yields_empty_diagram(self) -> None:
        """No files yields no components and a valid empty diagram."""
        document = ComponentDiagramBuilder(Config()).build([], [], [], None, "/tmp", {})
        self.assertEqual(document["components"], [])
        self.assertIn("graph LR", self.builder.mermaid_lr([], []))


class TestComponentPageContract(unittest.TestCase):
    """Contract: offline interactive page mirroring the Cytoscape/dagre look."""

    def setUp(self) -> None:
        """Build the document and render the page once."""
        nodes, content, analysis, resolved = _fixture()
        self.builder = ComponentDiagramBuilder(Config())
        self.document = self.builder.build(
            nodes, [], resolved, analysis, "/tmp", content
        )
        self.html = self.builder.render_page(self.document, home_href="index.html")

    def test_page_draws_nodes_edges_and_links(self) -> None:
        """SVG carries component boxes, labeled arrows, and click anchors."""
        self.assertIn("<svg", self.html)
        self.assertIn("pkg", self.html)
        self.assertIn("calls into", self.html)
        self.assertIn('href="#comp-1"', self.html)
        self.assertIn("cb-tip", self.html)
        for token in ("cb-reset", "cb-fit", "cb-png", "cb-theme"):
            self.assertIn(token, self.html)

    def test_page_nodes_explain_themselves(self) -> None:
        """Boxes show symbols, layer, counts; the hub glows; edges weight evidence."""
        self.assertIn("cb-node-sym", self.html)
        self.assertIn("foo", self.html)
        self.assertIn("cb-node-layer", self.html)
        self.assertIn("cb-node hub", self.html)
        self.assertIn("1 calls · 1 imports", self.html)
        self.assertIn("legend", self.html)

    def test_relations_section_lists_call_evidence(self) -> None:
        """Every arrow is explained with evidence and file:line samples."""
        self.assertIn("<h2>Relations</h2>", self.html)
        self.assertIn("@3", self.html)
        self.assertIn("across the boundary", self.html)

    def test_build_records_layers_hub_and_counts(self) -> None:
        """Components carry dominant layer, hub flag, symbols, edge counts."""
        component = next(c for c in self.document["components"] if c["name"] == "pkg")
        self.assertIn("layer", component)
        self.assertTrue(component["hub"])
        self.assertTrue(component["top_symbols"])
        relation = self.document["components_relations"][0]
        self.assertEqual((relation["call_count"], relation["import_count"]), (1, 1))

    def test_page_has_no_network_requests(self) -> None:
        """No script, stylesheet, image, or font leaves the machine."""
        self.assertNotIn("<script src", self.html)
        self.assertNotIn("<link", self.html)
        self.assertNotIn("http://", self.html)
        self.assertNotIn("https://", self.html)
        self.assertNotIn("url(http", self.html)

    def test_page_escapes_untrusted_text(self) -> None:
        """Hostile component names stay inert in markup and attributes."""
        hostile = Config()
        nodes = [_node('x/</script><img src=x onerror=alert(1)>.py', "f")]
        document = ComponentDiagramBuilder(hostile).build(nodes, [], [], None, "/tmp", {})
        page = ComponentDiagramBuilder(hostile).render_page(document, title="<t>")
        self.assertNotIn("</script><img", page)
        self.assertNotIn("<img src=x", page)
        self.assertIn("&lt;t&gt;", page)

    def test_thumbnail_is_safe_svg(self) -> None:
        """The gallery thumbnail is numbers plus escaped colors only."""
        svg = self.builder.thumbnail_svg(
            self.document["components"], self.document["components_relations"]
        )
        self.assertTrue(svg.startswith('<svg class="thumb"'))
        self.assertNotIn("<script", svg)
        self.assertEqual(ComponentDiagramBuilder(Config()).thumbnail_svg([], []), "")

    def test_write_emits_index_page(self) -> None:
        """write() emits index.html next to analysis.json and overview.md."""
        with tempfile.TemporaryDirectory() as tmp:
            written = self.builder.write(self.document, tmp)
            self.assertTrue(Path(written["index"]).is_file())
            page = Path(written["index"]).read_text(encoding="utf-8")
            self.assertIn("<svg", page)
            self.assertIn("Related Classes/Methods", page)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_page_script_is_valid_javascript(self) -> None:
        """The inline page script parses cleanly with node --check."""
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "cb.js"
            script.write_text(
                self.html.rsplit("<script>", 1)[1].split("</script>", 1)[0],
                encoding="utf-8",
            )
            result = subprocess.run(
                ["node", "--check", str(script)],
                capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(result.returncode, 0, result.stderr)


class TestComponentGalleryContract(unittest.TestCase):
    """Contract: gallery card, docs drawer sources, and nested rollup."""

    def _project(self, tmp: str) -> None:
        """Write a tiny two-file project."""
        Path(tmp, "a.py").write_text("from b import g\ndef f():\n    g()\n", encoding="utf-8")
        Path(tmp, "b.py").write_text("def g():\n    return 1\n", encoding="utf-8")

    def _config(self, **extra: object) -> Config:
        """Config with heavy sidecars disabled."""
        return Config(WIKI_ENABLED=False, AGENT_OUTPUT_ENABLED=False, VIDEO_ENABLED=False,
                      GH_WIKI_ENABLED=False, DIAGRAM_VIS_ENABLED=False, **extra)

    def test_export_diagrams_links_components_card(self) -> None:
        """export_diagrams writes index.html and links it from the gallery."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            readmenatorApplication(self._config()).export_diagrams(tmp)
            maps_dir = Path(tmp) / "readmenator-diagrams"
            self.assertTrue((maps_dir / "index.html").is_file())
            index = (Path(tmp) / "readmenator-maps" / "index.html").read_text(encoding="utf-8")
            self.assertIn("Component Diagrams", index)
            self.assertIn("../readmenator-diagrams/index.html", index)

    def test_export_pages_links_components_relatively(self) -> None:
        """export_pages links the page from inside the maps subdirectory."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            out = Path(tmp) / "site"
            readmenatorApplication(self._config()).export_pages(tmp, str(out))
            subdir = Config().DIAGRAM_MAPS_SUBDIR.strip("/")
            page = Path(tmp) / "readmenator-diagrams" / "index.html"
            self.assertTrue(page.is_file())
            index = (out / "index.html").read_text(encoding="utf-8")
            self.assertIn("../../readmenator-diagrams/index.html", index)
            self.assertIn(subdir + "/graph-force.html", index)

    def test_card_skipped_when_disabled(self) -> None:
        """COMPONENTS_ENABLED=False writes no page and no card."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            readmenatorApplication(self._config(COMPONENTS_ENABLED=False)).export_diagrams(tmp)
            maps_dir = Path(tmp) / "readmenator-maps"
            self.assertFalse((Path(tmp) / "readmenator-diagrams" / "index.html").exists())
            self.assertNotIn("Component Diagrams", (maps_dir / "index.html").read_text(encoding="utf-8"))

    def test_docs_collect_components_overview(self) -> None:
        """The static site ships the component markdown in its drawer."""
        from readmenator._app import readmenatorApplication
        from readmenator._diagrams import DocsSitePublisher

        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            readmenatorApplication(self._config()).export_components(tmp)
            sources = DocsSitePublisher(Config()).collect_doc_sources(tmp)
            names = [s.relative_to(Path(tmp)).as_posix() for s in sources]
            self.assertIn("readmenator-diagrams/overview.md", names)

    def test_nested_relations_roll_up(self) -> None:
        """Nested levels aggregate parent edges like project_relations_to_level."""
        builder = ComponentDiagramBuilder(Config(COMPONENTS_EXPAND_MIN_FILES=2))
        nodes = [_node("pkg/a.py", "f"), _node("pkg/b.py", "g"),
                 _node("lib/c.py", "h"), _node("lib/d.py", "i")]
        content = {
            "pkg/a.py": "from pkg.b import g\ndef f():\n    g()\n",
            "pkg/b.py": "def g():\n    return 1\n",
            "lib/c.py": "from pkg.b import g\ndef h():\n    g()\n",
            "lib/d.py": "def i():\n    return 2\n",
        }
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "all", {"pkg/a.py", "pkg/b.py", "lib/c.py", "lib/d.py"}, 0.5, 4),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=4, edge_count=2,
        )
        resolved = [Edge("pkg/a.py", "pkg/b.py", "resolved_imports"),
                    Edge("lib/c.py", "pkg/b.py", "resolved_imports")]
        document = builder.build(nodes, [], resolved, analysis, "/tmp", content)
        root = document["components"][0]
        self.assertTrue(root["can_expand"])
        nested_ids = {c["component_id"] for c in root["components"]}
        self.assertEqual(nested_ids, {"1.1", "1.2"})
        rolled = {(r["src_id"], r["dst_id"]) for r in root["components_relations"]}
        self.assertIn(("1.1", "1.2"), rolled)


if __name__ == "__main__":
    unittest.main()
