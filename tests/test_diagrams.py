"""Contract tests for interactive system maps.

Validates typed intermediate representations, deterministic validation
receipts, before and after comparison, and self-contained HTML rendering
for the five diagram kinds.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._diagrams import (
    DocsSitePublisher,
    InteractiveMapRenderer,
    MapEdge,
    MapNode,
    MapView,
    SystemMap,
    SystemMapBuilder,
    SystemMapValidator,
    VisNetworkRenderer,
)
from readmenator._models import Edge, Node, Symbol


class TestSystemMapBuilderContract(unittest.TestCase):
    """Contract: builder produces deterministic maps for all five kinds."""

    def setUp(self) -> None:
        """Initialise builder with default configuration."""
        self.config = Config()
        self.builder = SystemMapBuilder(self.config)

    def _make_graph(self) -> tuple:
        """Create a small deterministic project graph."""
        nodes = [
            Node(node_id="web/app.py", label="app.py", kind="module", language="py", symbols=[Symbol(name="serve", kind="function", line=1)]),
            Node(node_id="core/logic.py", label="logic.py", kind="module", language="py", symbols=[Symbol(name="run", kind="function", line=4)]),
            Node(node_id="data/store.py", label="store.py", kind="module", language="py", symbols=[Symbol(name="save", kind="function", line=9)]),
        ]
        edges = [
            Edge(source="web/app.py", target="core/logic.py", relation="imports"),
            Edge(source="core/logic.py", target="data/store.py", relation="imports"),
        ]
        layers = {"web/app.py": "presentation", "core/logic.py": "business_logic", "data/store.py": "data_access"}
        return nodes, edges, layers

    def test_builder_supports_five_kinds(self) -> None:
        """Builder exposes architecture, workflow, sequence, dataflow, lifecycle."""
        self.assertEqual(
            self.builder.supported_kinds(),
            ["architecture", "workflow", "sequence", "dataflow", "lifecycle"],
        )

    def test_builder_produces_all_kinds(self) -> None:
        """Build all returns one map per supported kind."""
        nodes, edges, layers = self._make_graph()
        maps = self.builder.build_all(nodes, edges, edges, layers, [], None)
        self.assertEqual(set(maps.keys()), set(self.builder.supported_kinds()))
        for kind, system_map in maps.items():
            self.assertEqual(system_map.kind, kind)
            self.assertTrue(system_map.nodes)

    def test_builder_is_deterministic(self) -> None:
        """Two builds over identical input share coordinates and bytes."""
        nodes, edges, layers = self._make_graph()
        first = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        second = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        self.assertEqual(
            [(n.node_id, n.x, n.y) for n in first.nodes],
            [(n.node_id, n.x, n.y) for n in second.nodes],
        )
        renderer = InteractiveMapRenderer(self.config)
        self.assertEqual(renderer.render(first), renderer.render(second))

    def test_builder_orders_links_deterministically(self) -> None:
        """Shuffled input edges yield identical ordered map relationships."""
        nodes = [
            Node(node_id="c.py", label="c.py", kind="module", language="py"),
            Node(node_id="a.py", label="a.py", kind="module", language="py"),
            Node(node_id="d.py", label="d.py", kind="module", language="py"),
            Node(node_id="b.py", label="b.py", kind="module", language="py"),
        ]
        edges = [
            Edge(source="c.py", target="d.py", relation="imports"),
            Edge(source="a.py", target="b.py", relation="imports"),
            Edge(source="b.py", target="c.py", relation="imports"),
        ]
        layers = {"a.py": "presentation", "b.py": "business_logic", "c.py": "data_access", "d.py": "testing"}
        first = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        second = self.builder.build(nodes, list(reversed(edges)), list(reversed(edges)), layers, [], None, "architecture")
        first_routes = [(e.source, e.target) for e in first.edges]
        second_routes = [(e.source, e.target) for e in second.edges]
        self.assertEqual(first_routes, second_routes)
        self.assertEqual(first_routes, sorted(first_routes))

    def test_builder_validates_large_graph_for_all_kinds(self) -> None:
        """Large layered graphs validate for every diagram kind."""
        from readmenator._diagrams import SystemMapValidator
        lanes = ["presentation", "business_logic", "data_access", "infrastructure", "testing", "utility"]
        nodes = [
            Node(node_id="pkg" + str(lane) + "/mod" + str(i) + ".py", label="mod" + str(i) + ".py", kind="module", language="py")
            for lane in range(len(lanes))
            for i in range(8)
        ]
        ids = [n.node_id for n in nodes]
        edges = [Edge(source=ids[i], target=ids[i + 1], relation="imports") for i in range(len(ids) - 1)]
        layers = {n.node_id: lanes[int(n.node_id.split("pkg")[1][0])] for n in nodes}
        validator = SystemMapValidator(self.config)
        for kind in self.builder.supported_kinds():
            system_map = self.builder.build(nodes, edges, edges, layers, [], None, kind)
            receipt = validator.validate(system_map)
            self.assertTrue(receipt.passed, kind + ": " + str([(d.rule, d.subject) for d in receipt.errors[:3]]))

    def test_builder_reports_total_scope(self) -> None:
        """Built maps record shown scope and total input file count."""
        nodes, edges, layers = self._make_graph()
        system_map = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        self.assertEqual(system_map.meta.get("total"), str(len(nodes)))
        self.assertEqual(system_map.meta.get("scope"), str(len(system_map.nodes)))

    def test_builder_attaches_symbols_and_docs(self) -> None:
        """Map nodes carry symbol records, file docs, and language."""
        nodes = [
            Node(node_id="a.py", label="a.py", kind="module", language="py", doc="Alpha module",
                 symbols=[Symbol(name="serve", kind="function", line=3, signature="serve()", doc="Serves.")]),
            Node(node_id="b.py", label="b.py", kind="module", language="py"),
        ]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        layers = {"a.py": "presentation", "b.py": "business_logic"}
        system_map = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        by_id = {node.node_id: node for node in system_map.nodes}
        self.assertEqual(by_id["a.py"].doc, "Alpha module")
        self.assertEqual(by_id["a.py"].language, "py")
        self.assertEqual(by_id["a.py"].symbol_total, 1)
        self.assertEqual(by_id["a.py"].symbols[0]["name"], "serve")
        self.assertEqual(by_id["a.py"].symbols[0]["signature"], "serve()")

    def test_builder_truncates_symbols_per_node(self) -> None:
        """Symbol records respect the per-node configured cap."""
        symbols = [Symbol(name="f" + str(i), kind="function", line=i + 1) for i in range(40)]
        nodes = [Node(node_id="big.py", label="big.py", kind="module", language="py", symbols=symbols)]
        system_map = self.builder.build(nodes, [], [], {}, [], None, "architecture")
        node = system_map.nodes[0]
        self.assertLessEqual(len(node.symbols), self.config.DIAGRAM_MAP_SYMBOLS_PER_NODE)
        self.assertEqual(node.symbol_total, 40)

    def test_builder_truncates_to_configured_limit(self) -> None:
        """Oversized graphs are truncated to the configured node limit."""
        nodes = [
            Node(node_id="f" + str(i) + ".py", label="f" + str(i) + ".py", kind="module", language="py")
            for i in range(self.config.DIAGRAM_MAX_NODES + 20)
        ]
        edges: list = []
        system_map = self.builder.build(nodes, edges, edges, {}, [], None, "architecture")
        self.assertLessEqual(len(system_map.nodes), self.config.DIAGRAM_MAX_NODES)

    def test_compare_reports_added_removed_rerouted(self) -> None:
        """Delta comparison reports added, removed, and rerouted facts."""
        nodes, edges, layers = self._make_graph()
        base = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        extended_nodes = list(nodes) + [
            Node(node_id="extra/job.py", label="job.py", kind="module", language="py")
        ]
        head = self.builder.build(extended_nodes, edges, edges, layers, [], None, "architecture")
        delta = self.builder.compare(base, head)
        self.assertIn("extra/job.py", delta.added)
        self.assertEqual(delta.removed, [])
        self.assertIsInstance(delta.rerouted, list)


class TestSystemMapValidatorContract(unittest.TestCase):
    """Contract: validator returns deterministic receipts with rule codes."""

    def setUp(self) -> None:
        """Initialise validator with default configuration."""
        self.config = Config()
        self.validator = SystemMapValidator(self.config)

    def _valid_map(self) -> SystemMap:
        """Create a minimal valid architecture map."""
        return SystemMap(
            kind="architecture",
            title="Runtime Architecture",
            nodes=[
                MapNode(node_id="a", label="alpha", role="frontend", group="presentation", x=40, y=90),
                MapNode(node_id="b", label="beta", role="backend", group="business_logic", x=320, y=90),
            ],
            edges=[MapEdge(source="a", target="b", label="imports", kind="imports")],
            views=[MapView(view_id="primary-path", title="Primary path", focus=["a", "b"])],
        )

    def test_validator_passes_valid_map(self) -> None:
        """Valid maps pass with the full check list and zero errors."""
        receipt = self.validator.validate(self._valid_map())
        self.assertTrue(receipt.passed)
        self.assertEqual(len(receipt.checks), 9)
        self.assertEqual(receipt.errors, [])

    def test_validator_rejects_duplicate_node_ids(self) -> None:
        """Duplicate identifiers fail with rule D001."""
        system_map = self._valid_map()
        system_map.nodes.append(
            MapNode(node_id="a", label="again", role="backend", group="business_logic", x=600, y=90)
        )
        receipt = self.validator.validate(system_map)
        self.assertFalse(receipt.passed)
        self.assertTrue(any(d.rule == "D001" for d in receipt.errors))

    def test_validator_rejects_dangling_edge(self) -> None:
        """Edges pointing at unknown nodes fail with rule D002."""
        system_map = self._valid_map()
        system_map.edges.append(MapEdge(source="a", target="ghost", label="imports"))
        receipt = self.validator.validate(system_map)
        self.assertFalse(receipt.passed)
        self.assertTrue(any(d.rule == "D002" for d in receipt.errors))

    def test_validator_rejects_empty_map(self) -> None:
        """Maps without nodes fail with rule D003."""
        receipt = self.validator.validate(SystemMap(kind="architecture", title="Empty"))
        self.assertFalse(receipt.passed)
        self.assertTrue(any(d.rule == "D003" for d in receipt.errors))

    def test_validator_rejects_unknown_kind(self) -> None:
        """Unknown diagram kinds fail with rule D000."""
        system_map = self._valid_map()
        system_map.kind = "unknown"
        receipt = self.validator.validate(system_map)
        self.assertFalse(receipt.passed)
        self.assertTrue(any(d.rule == "D000" for d in receipt.errors))


class TestInteractiveMapRendererContract(unittest.TestCase):
    """Contract: renderer emits standalone interactive HTML documents."""

    def setUp(self) -> None:
        """Initialise builder and renderer with default configuration."""
        self.config = Config()
        self.builder = SystemMapBuilder(self.config)
        self.renderer = InteractiveMapRenderer(self.config)

    def _map(self, kind: str = "architecture") -> SystemMap:
        """Build a small map of the requested kind."""
        nodes = [
            Node(node_id="web/app.py", label="app.py", kind="module", language="py"),
            Node(node_id="core/logic.py", label="logic.py", kind="module", language="py"),
        ]
        edges = [Edge(source="web/app.py", target="core/logic.py", relation="imports")]
        layers = {"web/app.py": "presentation", "core/logic.py": "business_logic"}
        return self.builder.build(nodes, edges, edges, layers, [], None, kind)

    def test_renderer_produces_standalone_document(self) -> None:
        """Output is a complete HTML document with inline SVG."""
        output = self.renderer.render(self._map())
        self.assertIn("<!DOCTYPE html>", output)
        self.assertIn("<svg", output)
        self.assertIn("map-nodes", output)

    def test_renderer_has_no_external_requests(self) -> None:
        """Output performs no external fetches or CDN references."""
        output = self.renderer.render(self._map())
        self.assertNotIn("src=\"http", output)
        self.assertNotIn("href=\"http", output)
        self.assertNotIn("cdn", output.lower())

    def test_renderer_includes_interaction_controls(self) -> None:
        """Output includes search, passport, reach, route, lens, views, export."""
        output = self.renderer.render(self._map())
        for token in ["search", "passport", "Upstream", "Downstream", "Lens", "Play", "Present", "Export", "route-from", "chapters", "role-counts"]:
            self.assertIn(token, output)

    def test_renderer_includes_keyboard_and_deep_links(self) -> None:
        """Output documents shortcuts and hash deep link contracts."""
        output = self.renderer.render(self._map())
        self.assertIn("#focus=", output)
        self.assertIn("#route=", output)
        self.assertIn("#lens=", output)
        self.assertIn("#view=", output)
        self.assertIn("prefers-reduced-motion", output)

    def test_renderer_escapes_malicious_labels(self) -> None:
        """Malicious labels are escaped and never break the document."""
        system_map = SystemMap(
            kind="architecture",
            title="Evil <Title>",
            nodes=[MapNode(node_id="evil.py", label="<script>alert(1)</script>", role="frontend", group="presentation", x=40, y=90)],
            edges=[],
            views=[],
        )
        output = self.renderer.render(system_map)
        self.assertNotIn("<script>alert(1)</script>", output)
        self.assertIn("&lt;script&gt;", output)

    def test_renderer_embeds_valid_json_payloads(self) -> None:
        """Embedded payload scripts parse as valid JSON arrays."""
        output = self.renderer.render(self._map())
        match = re.search(r'<script type="application/json" id="map-nodes">(.*?)</script>', output, re.DOTALL)
        self.assertIsNotNone(match)
        payload = json.loads(match.group(1).replace("\\u003c", "<"))
        self.assertTrue(isinstance(payload, list))
        self.assertGreaterEqual(len(payload), 1)

    def test_renderer_covers_all_five_kinds(self) -> None:
        """Every diagram kind renders a standalone document."""
        for kind in ["architecture", "workflow", "sequence", "dataflow", "lifecycle"]:
            output = self.renderer.render(self._map(kind))
            self.assertIn("<!DOCTYPE html>", output)
            self.assertIn(kind, output)

    def test_renderer_links_gallery_home_when_configured(self) -> None:
        """Maps with a home target expose a gallery back link."""
        system_map = self._map()
        system_map.meta["home"] = "../index.html"
        output = self.renderer.render(system_map)
        self.assertIn("../index.html", output)
        self.assertIn("Gallery", output)
    def test_renderer_omits_gallery_home_by_default(self) -> None:
        """Maps without a home target expose no gallery link."""
        output = self.renderer.render(self._map())
        self.assertNotIn("Gallery</a>", output)

    def test_renderer_keeps_canvas_distinct_from_nodes(self) -> None:
        """Canvas background differs from node fill for readability."""
        output = self.renderer.render(self._map())
        self.assertIn("svg#canvas{", output)
        canvas_rule = output.split("svg#canvas{")[1].split("}")[0]
        self.assertIn("background:var(--canvas)", canvas_rule)
        self.assertIn(".node-box{fill:var(--mask)", output)

    def test_renderer_supports_drag_and_settle(self) -> None:
        """Nodes are draggable with pointer capture plus a force pass."""
        output = self.renderer.render(self._map())
        self.assertIn("setPointerCapture", output)
        self.assertIn("data-action=\"settle\"", output)
        self.assertIn("function settle()", output)
        self.assertIn("touch-action:none", output)

    def test_renderer_sanitizes_viewer_state_on_export(self) -> None:
        """Exports drop temporary focus, dim, and drag classes."""
        output = self.renderer.render(self._map())
        self.assertIn("cleanClone", output)
        self.assertIn(".dim,.strong", output)

    def test_renderer_buttons_explain_their_purpose(self) -> None:
        """Every toolbar action carries a human-readable title."""
        import re as _re
        output = self.renderer.render(self._map())
        buttons = _re.findall(r"<button[^>]*data-action=\"([^\"]+)\"[^>]*>", output)
        self.assertGreater(len(buttons), 5)
        for match in _re.finditer(r"<button([^>]*)>", output):
            attrs = match.group(1)
            if "data-action" in attrs and "close-" not in attrs:
                self.assertIn("title=", attrs)


class TestDocsSitePublisherContract(unittest.TestCase):
    """Contract: publisher writes maps plus a gallery index as a static site."""

    def setUp(self) -> None:
        """Initialise builder and publisher with default configuration."""
        self.config = Config()
        self.builder = SystemMapBuilder(self.config)
        self.publisher = DocsSitePublisher(self.config)

    def _maps(self) -> dict:
        """Build all five maps from a small deterministic graph."""
        nodes = [
            Node(node_id="web/app.py", label="app.py", kind="module", language="py"),
            Node(node_id="core/logic.py", label="logic.py", kind="module", language="py"),
        ]
        edges = [Edge(source="web/app.py", target="core/logic.py", relation="imports")]
        layers = {"web/app.py": "presentation", "core/logic.py": "business_logic"}
        return self.builder.build_all(nodes, edges, edges, layers, [], None)

    def test_publish_writes_index_plus_five_maps(self) -> None:
        """Publish creates an index, five map files, and a nojekyll marker."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(self._maps(), "Demo", tmp, {"files": 2})
            self.assertIn("index", written)
            self.assertIn("nojekyll", written)
            for kind in ["architecture", "workflow", "sequence", "dataflow", "lifecycle"]:
                self.assertIn(kind, written)
                self.assertTrue(Path(written[kind]).is_file())

    def test_publish_index_links_every_map(self) -> None:
        """Gallery index links every published map with relative paths."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(self._maps(), "Demo", tmp, {})
            index = Path(written["index"]).read_text(encoding="utf-8")
            for kind in ["architecture", "workflow", "sequence", "dataflow", "lifecycle"]:
                self.assertIn("maps/" + kind + ".html", index)

    def test_publish_output_has_no_external_requests(self) -> None:
        """Index and maps perform no external fetches or CDN references."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(self._maps(), "Demo", tmp, {})
            for key, path in written.items():
                if key == "nojekyll":
                    continue
                content = Path(path).read_text(encoding="utf-8")
                self.assertNotIn("src=\"http", content)
                self.assertNotIn("href=\"http", content)
                self.assertNotIn("unpkg", content)

    def test_publish_is_deterministic(self) -> None:
        """Two publishes over identical input share index bytes."""
        import tempfile
        with tempfile.TemporaryDirectory() as first:
            with tempfile.TemporaryDirectory() as second:
                self.publisher.publish(self._maps(), "Demo", first, {"files": 2})
                self.publisher.publish(self._maps(), "Demo", second, {"files": 2})
                first_index = Path(first, "index.html").read_text(encoding="utf-8")
                second_index = Path(second, "index.html").read_text(encoding="utf-8")
                self.assertEqual(first_index, second_index)

    def test_publish_escapes_malicious_project_name(self) -> None:
        """Malicious project names are escaped in the gallery index."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(self._maps(), "<script>alert(1)</script>", tmp, {})
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertNotIn("<script>alert(1)</script>", index)
            self.assertIn("&lt;script&gt;", index)

    def test_publish_escapes_malicious_stat_keys(self) -> None:
        """Malicious statistics keys are escaped in the gallery index."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(
                self._maps(), "Demo", tmp, {"<img src=x onerror=alert(1)>": 3}
            )
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertNotIn("<img src=x onerror=alert(1)>", index)
            self.assertIn("&lt;img", index)

    def test_publish_skips_invalid_maps(self) -> None:
        """Maps failing validation are skipped while the index is written."""
        import tempfile
        maps = self._maps()
        maps["sequence"].edges.append(MapEdge(source="ghost", target="nowhere", label="x"))
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(maps, "Demo", tmp, {})
            self.assertNotIn("sequence", written)
            self.assertIn("index", written)
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertNotIn("maps/sequence.html", index)

    def test_publish_empty_maps_writes_empty_gallery(self) -> None:
        """Empty input writes an index with an empty gallery notice."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish({}, "Demo", tmp, {})
            self.assertIn("index", written)
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertIn("<!DOCTYPE html>", index)

    def test_publish_leaves_input_maps_unmodified(self) -> None:
        """Publish never mutates the caller supplied map metadata."""
        import tempfile
        maps = self._maps()
        with tempfile.TemporaryDirectory() as tmp:
            self.publisher.publish(maps, "Demo", tmp, {})
            for system_map in maps.values():
                self.assertNotIn("home", system_map.meta)

    def test_publish_flat_subdir_keeps_links_relative(self) -> None:
        """Flat layouts link maps beside the index with a local home."""
        import tempfile
        from dataclasses import replace
        flat = DocsSitePublisher(replace(self.config, DIAGRAM_MAPS_SUBDIR="."))
        with tempfile.TemporaryDirectory() as tmp:
            written = flat.publish(self._maps(), "Demo", tmp, {})
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertIn("architecture.html", index)
            self.assertNotIn("maps/architecture.html", index)
            architecture = Path(written["architecture"]).read_text(encoding="utf-8")
            self.assertIn('href="index.html"', architecture)

    def test_publish_index_explains_how_to_read(self) -> None:
        """Gallery index documents the reader interactions."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(self._maps(), "Demo", tmp, {})
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertIn("How to read", index)

    def test_publish_card_reports_primary_scope(self) -> None:
        """Gallery cards state shown files against the project total."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            written = self.publisher.publish(self._maps(), "Demo", tmp, {})
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertIn("files in primary scope", index)


class TestVisNetworkRendererContract(unittest.TestCase):
    """Contract: vis.js renderer emits CDN-powered physics documents."""

    def setUp(self) -> None:
        """Initialise builder and renderer with default configuration."""
        self.config = Config()
        self.builder = SystemMapBuilder(self.config)
        self.renderer = VisNetworkRenderer(self.config)

    def _map(self, kind: str = "architecture") -> SystemMap:
        """Build a small map of the requested kind."""
        nodes = [
            Node(node_id="web/app.py", label="app.py", kind="module", language="py"),
            Node(node_id="core/logic.py", label="logic.py", kind="module", language="py"),
        ]
        edges = [Edge(source="web/app.py", target="core/logic.py", relation="imports")]
        layers = {"web/app.py": "presentation", "core/logic.py": "business_logic"}
        return self.builder.build(nodes, edges, edges, layers, [], None, kind)

    def test_renderer_uses_configured_cdn_urls(self) -> None:
        """Script and style tags come from Config, never hardcoded."""
        from dataclasses import replace
        custom = replace(
            self.config,
            DIAGRAM_VIS_CDN_JS="https://example.invalid/vis.js",
            DIAGRAM_VIS_CDN_CSS="https://example.invalid/vis.css",
        )
        output = VisNetworkRenderer(custom).render(self._map())
        self.assertIn("https://example.invalid/vis.js", output)
        self.assertIn("https://example.invalid/vis.css", output)
        self.assertNotIn("unpkg", output)

    def test_renderer_builds_vis_network_with_physics(self) -> None:
        """Output instantiates a vis network with physics enabled."""
        output = self.renderer.render(self._map())
        self.assertIn("vis.Network", output)
        self.assertIn("vis.DataSet", output)
        self.assertIn("physics", output)
        self.assertIn("barnesHut", output)

    def test_renderer_links_gallery_home_when_configured(self) -> None:
        """Vis maps with a home target expose a gallery back link."""
        system_map = self._map()
        system_map.meta["home"] = "../index.html"
        output = self.renderer.render(system_map)
        self.assertIn("../index.html", output)
        self.assertIn("Gallery", output)

    def test_renderer_disables_physics_from_config(self) -> None:
        """Physics honors the configured enabled flag."""
        from dataclasses import replace
        frozen = replace(self.config, DIAGRAM_VIS_PHYSICS_ENABLED=False)
        output = VisNetworkRenderer(frozen).render(self._map())
        self.assertIn('"enabled": false', output)

    def test_renderer_escapes_malicious_titles(self) -> None:
        """Malicious labels never break tooltips or markup."""
        system_map = SystemMap(
            kind="architecture",
            title="Evil <Title>",
            nodes=[MapNode(node_id="evil.py", label="<script>alert(1)</script>", role="frontend", group="presentation", x=40, y=90)],
            edges=[],
            views=[],
        )
        output = self.renderer.render(system_map)
        self.assertNotIn("<script>alert(1)</script>", output)
        self.assertIn("&lt;script&gt;", output)

    def test_renderer_exposes_reader_controls(self) -> None:
        """Output carries search, reach, route, lens, chapters, export."""
        output = self.renderer.render(self._map())
        for token in ["search", "Upstream", "Downstream", "Lens", "Play", "Stabilize", "Theme", "Export", "route-from", "chapters"]:
            self.assertIn(token, output)

    def test_renderer_is_deterministic(self) -> None:
        """Two renders over identical input share bytes."""
        system_map = self._map()
        self.assertEqual(self.renderer.render(system_map), self.renderer.render(system_map))

    def test_renderer_embeds_valid_payloads(self) -> None:
        """Embedded node and edge payloads parse as valid JSON."""
        output = self.renderer.render(self._map())
        match = re.search(r'<script type="application/json" id="vis-nodes">(.*?)</script>', output, re.DOTALL)
        self.assertIsNotNone(match)
        payload = json.loads(match.group(1).replace("\\u003c", "<"))
        self.assertEqual(len(payload), 2)

    def test_renderer_documents_symbols_per_file(self) -> None:
        """Node payloads and tooltips expose symbols with signatures."""
        nodes = [
            Node(node_id="a.py", label="a.py", kind="module", language="py", doc="Alpha.",
                 symbols=[Symbol(name="serve", kind="function", line=3, signature="serve()", doc="Serves.")]),
            Node(node_id="b.py", label="b.py", kind="module", language="py"),
        ]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        layers = {"a.py": "presentation", "b.py": "business_logic"}
        system_map = self.builder.build(nodes, edges, edges, layers, [], None, "architecture")
        output = self.renderer.render(system_map)
        self.assertIn("serve()", output)
        self.assertIn("Alpha.", output)
        self.assertIn('id="node-symbols"', output)
        self.assertIn("renderNodeDetail", output)

    def test_renderer_escapes_malicious_symbol_docs(self) -> None:
        """Malicious symbol documentation never breaks tooltips."""
        nodes = [
            Node(node_id="a.py", label="a.py", kind="module", language="py",
                 symbols=[Symbol(name="x", kind="function", line=1, doc="<img src=x onerror=alert(1)>")]),
        ]
        system_map = self.builder.build(nodes, [], [], {}, [], None, "architecture")
        output = self.renderer.render(system_map)
        self.assertNotIn("<img src=x onerror=alert(1)>", output)
        self.assertIn("\\u003cimg", output)
        self.assertIn("escapeHtml(s.doc)", output)


class TestDiagramVariantsContract(unittest.TestCase):
    """Contract: default exports are vis.js maps with gallery links."""

    def _project(self, tmp: str) -> None:
        """Create a two-file project in a temporary directory."""
        Path(tmp, "a.py").write_text("from b import run\ndef serve():\n    return run()\n", encoding="utf-8")
        Path(tmp, "b.py").write_text("def run():\n    return True\n", encoding="utf-8")

    def test_export_diagrams_writes_vis_maps_by_default(self) -> None:
        """Default diagram export writes CDN-powered vis.js maps."""
        import tempfile
        from readmenator._app import readmenatorApplication
        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            written = readmenatorApplication().export_diagrams(tmp)
            self.assertIn("architecture", written)
            content = Path(written["architecture"]).read_text(encoding="utf-8")
            self.assertIn("vis.Network", content)
            self.assertIn("unpkg", content)
            index = Path(written["index"]).read_text(encoding="utf-8")
            self.assertIn("architecture.html", index)

    def test_export_diagrams_falls_back_offline_when_disabled(self) -> None:
        """Disabled vis flag produces offline maps without CDN."""
        import tempfile
        from dataclasses import replace
        from readmenator._app import readmenatorApplication
        config = replace(Config(), DIAGRAM_VIS_ENABLED=False)
        with tempfile.TemporaryDirectory() as tmp:
            self._project(tmp)
            written = readmenatorApplication(config).export_diagrams(tmp)
            self.assertIn("architecture", written)
            content = Path(written["architecture"]).read_text(encoding="utf-8")
            self.assertNotIn("unpkg", content)
            self.assertIn("<svg", content)


if __name__ == "__main__":
    unittest.main()
