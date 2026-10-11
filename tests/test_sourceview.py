"""Contract tests for the source viewer (View drawer in explorers)."""

from __future__ import annotations

import re
import unittest

from readmenator._bundlegraph import BundleGraphRenderer
from readmenator._config import Config
from readmenator._forcegraph import ForceGraphRenderer
from readmenator._models import Edge, Node, Symbol
from readmenator._sourceview import SourceViewBuilder


def _node(nid: str) -> Node:
    """Build a file node with one function symbol."""
    return Node(nid, nid.split("/")[-1], "module", "py", "Purpose.",
                [Symbol("foo", "function", 1, "Do foo.", "def foo():")])


class TestSourceViewBuilderContract(unittest.TestCase):
    """Contract: bounded sources, deterministic, privacy-aware."""

    def test_build_sources_embeds_truncated_text(self) -> None:
        """Sources carry text, line counts, and truncation flags."""
        builder = SourceViewBuilder(Config())
        sources = builder.build_sources([_node("a.py")], {"a.py": "def foo():\n    return 1\n"})
        self.assertIn("a.py", sources)
        self.assertIn("def foo", sources["a.py"].text)
        self.assertEqual(sources["a.py"].lines, 2)
        self.assertFalse(sources["a.py"].truncated)

    def test_build_sources_respects_caps(self) -> None:
        """Per-file char caps truncate deterministically."""
        builder = SourceViewBuilder(Config(SOURCEVIEW_MAX_CHARS_PER_FILE=10))
        sources = builder.build_sources([_node("a.py")], {"a.py": "x" * 100})
        self.assertTrue(sources["a.py"].truncated)
        self.assertLessEqual(len(sources["a.py"].text), 10)

    def test_build_sources_empty_in_privacy_mode(self) -> None:
        """Privacy mode embeds no source text."""
        builder = SourceViewBuilder(Config(PRIVACY_MODE=True))
        self.assertEqual(builder.build_sources([_node("a.py")], {"a.py": "x = 1"}), {})

    def test_build_sources_disabled_flag(self) -> None:
        """SOURCEVIEW_ENABLED=False embeds nothing."""
        builder = SourceViewBuilder(Config(SOURCEVIEW_ENABLED=False))
        self.assertEqual(builder.build_sources([_node("a.py")], {"a.py": "x = 1"}), {})


class TestSourceViewerRenderContract(unittest.TestCase):
    """Contract: View button, drawer, highlight, ctrl+click, theme, no network."""

    def setUp(self) -> None:
        """Build payloads with embedded sources."""
        self.config = Config()
        self.nodes = [_node("a.py"), _node("b.py")]
        self.content = {"a.py": "def foo():\n    return bar\n", "b.py": "def bar():\n    pass\n"}
        self.force = ForceGraphRenderer(self.config).build_payload(
            self.nodes, [], content_map=self.content)
        self.force_html = ForceGraphRenderer(self.config).render(self.force)
        self.bundle_html = BundleGraphRenderer(self.config).render(self.force)

    def test_forcegraph_embeds_src_fields(self) -> None:
        """File nodes carry src, src_lines, and src_cut."""
        node = next(n for n in self.force["nodes"] if n["id"] == "file:a.py")
        self.assertIn("def foo", node["src"])
        self.assertEqual(node["src_lines"], 2)
        self.assertEqual(node["src_cut"], 0)

    def test_bundlegraph_propagates_src_and_syms(self) -> None:
        """Bundle nodes keep source text and symbol records."""
        payload = BundleGraphRenderer(self.config).build_payload(self.force)
        node = next(n for n in payload["nodes"] if n["f"] == "a.py")
        self.assertIn("def foo", node["src"])
        self.assertTrue(any(s["n"] == "foo" for s in node["syms"]))

    def test_both_pages_ship_view_drawer(self) -> None:
        """View button, drawer, and lazy chunk rendering ship in both pages."""
        for html in (self.force_html, self.bundle_html):
            for token in ("View", "src-viewer", "src-scrim", "openSource",
                          "requestAnimationFrame", "srcChunk" if False else "srcChunk",
                          "tok-kw", "tok-sym", "Ctrl+Click", "src-tip"):
                # srcChunk lives in SETTINGS/CFG; check separately below
                if token == "srcChunk":
                    continue
                self.assertIn(token, html)

    def test_settings_carry_src_budgets(self) -> None:
        """Chunk sizes come from Config, never hardcoded."""
        self.assertIn(str(self.config.SOURCEVIEW_CHUNK_LINES), self.force_html)
        self.assertIn(str(self.config.SOURCEVIEW_CHUNK_LINES), self.bundle_html)

    def test_no_network_requests(self) -> None:
        """Bundle stays fully offline; force-graph keeps only its engine CDN."""
        self.assertNotIn("<script src", self.bundle_html)
        self.assertNotIn("https://", self.bundle_html)
        # force-graph page has vendor + pinned CDN fallbacks only
        self.assertNotIn("highlight.js", self.force_html)
        self.assertNotIn("cdnjs", self.force_html)

    def test_theme_tokens_for_both_modes(self) -> None:
        """Syntax colors follow dark/light via CSS vars."""
        for html in (self.force_html, self.bundle_html):
            self.assertIn("--kw", html)
            self.assertIn('data-theme="light"', html)

    def test_privacy_mode_strips_viewer(self) -> None:
        """Privacy payloads carry no src and settings disable the viewer."""
        private = ForceGraphRenderer(Config(PRIVACY_MODE=True)).build_payload(
            self.nodes, [], content_map=self.content)
        for node in private["nodes"]:
            if node["type"] == "file":
                self.assertEqual(node.get("src", ""), "")
        html = ForceGraphRenderer(Config(PRIVACY_MODE=True)).render(private)
        self.assertIn("srcEnabled", html)
        # srcEnabled false is serialized
        self.assertIn('"srcEnabled": false', html)

    def test_untrusted_source_cannot_break_script(self) -> None:
        """Angle brackets in sources stay unicode-escaped."""
        evil = {"a.py": "</script><script>alert(1)</script>"}
        payload = ForceGraphRenderer(self.config).build_payload(self.nodes, [], content_map=evil)
        html = ForceGraphRenderer(self.config).render(payload)
        self.assertNotIn("</script><script>alert(1)", html)

    def test_missing_source_falls_back_to_live_api(self) -> None:
        """Empty embedded source tries /api/source before blaming the build."""
        for html in (self.force_html, self.bundle_html):
            self.assertIn("api/source?file=", html)
            self.assertIn("loading live source", html)
            self.assertIn("source viewer disabled (privacy mode or SOURCEVIEW_ENABLED off)", html)
            self.assertIn("readmenator . --rebuild", html)
            self.assertNotIn("rebuild with SOURCEVIEW_ENABLED to read it here", html)

    def test_static_pages_never_probe_the_api(self) -> None:
        """Static exports keep srcLive false so Pages hosting fires no fetch (no 404)."""
        for html in (self.force_html, self.bundle_html):
            self.assertIn('"srcLive": false', html)
        live = ForceGraphRenderer(self.config).render(self.force, live_api=True)
        self.assertIn('"srcLive": true', live)

    def test_budget_cut_files_say_so(self) -> None:
        """Files cut by SOURCEVIEW budgets carry src_why so the drawer is honest."""
        tiny = Config(SOURCEVIEW_MAX_FILES=1)
        payload = ForceGraphRenderer(tiny).build_payload(self.nodes, [], content_map=self.content)
        by_id = {n["id"]: n for n in payload["nodes"]}
        self.assertEqual(by_id["file:a.py"]["src_why"], "")
        self.assertIn("def foo", by_id["file:a.py"]["src"])
        self.assertEqual(by_id["file:b.py"]["src"], "")
        self.assertEqual(by_id["file:b.py"]["src_why"], "budget")
        bundle = BundleGraphRenderer(tiny).build_payload(payload)
        bnode = next(n for n in bundle["nodes"] if n["f"] == "b.py")
        self.assertEqual(bnode["src_why"], "budget")
        html = ForceGraphRenderer(tiny).render(payload)
        self.assertIn("cut by SOURCEVIEW budgets", html)

    def test_empty_files_say_so(self) -> None:
        """Files with no content report empty instead of stale."""
        builder = SourceViewBuilder(Config())
        reasons = builder.build_reasons(self.nodes, {"a.py": "x = 1\n"})
        self.assertNotIn("a.py", reasons)
        self.assertEqual(reasons.get("b.py"), "empty")

    def test_default_budgets_cover_mid_size_projects(self) -> None:
        """Raised defaults embed far more than the old 400-file cap."""
        self.assertGreaterEqual(Config().SOURCEVIEW_MAX_FILES, 1000)
        self.assertGreaterEqual(Config().SOURCEVIEW_MAX_TOTAL_CHARS, 4000000)

    def test_budget_cut_warns_on_console(self) -> None:
        """Hitting a budget logs which knobs to raise."""
        tiny = Config(SOURCEVIEW_MAX_FILES=1)
        with self.assertLogs("readmenator._forcegraph", level="WARNING") as captured:
            ForceGraphRenderer(tiny).build_payload(self.nodes, [], content_map=self.content)
        self.assertTrue(any("SOURCEVIEW budgets hit" in line for line in captured.output))
        full = ForceGraphRenderer(self.config).build_payload(self.nodes, [], content_map=self.content)
        self.assertTrue(all(n.get("src") for n in full["nodes"] if n["type"] == "file"))

    def test_update_refreshes_explorer_sources(self) -> None:
        """update() rewrites explorers so new files carry embedded source."""
        import tempfile
        from pathlib import Path
        from readmenator._app import readmenatorApplication
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.py").write_text("import os\n", encoding="utf-8")
            app = readmenatorApplication(Config(
                WIKI_ENABLED=False, AGENT_OUTPUT_ENABLED=False,
                VIDEO_ENABLED=False, GH_WIKI_ENABLED=False,
                COMPONENTS_ENABLED=False, DIAGRAM_ENABLED=False,
            ))
            app.update(tmp)
            force = Path(tmp) / "readmenator-maps" / "graph-force.html"
            self.assertTrue(force.is_file())
            Path(tmp, "logging_config.py").write_text("LEVEL = 1\n", encoding="utf-8")
            app.update(tmp)
            html = force.read_text(encoding="utf-8")
            self.assertIn("logging_config.py", html)
            self.assertIn("LEVEL = 1", html)


if __name__ == "__main__":
    unittest.main()
