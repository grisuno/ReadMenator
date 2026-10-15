"""Contract tests for per-project readmenator.toml configuration."""

import json
import unittest
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from readmenator._bundlegraph import BundleGraphRenderer
from readmenator._config import Config
from readmenator._diagrams import DocsSitePublisher
from readmenator._flowpage import render_flows_page
from readmenator._forcegraph import ForceGraphRenderer
from readmenator._project_config import (
    TOML_MAP,
    ensure_project_config,
    load_project_config,
    parse_toml,
    template_text,
    viewer_config_dict,
    write_viewer_config,
)


class TestProjectConfigContract(unittest.TestCase):
    def test_template_parses_back_to_defaults(self) -> None:
        text = template_text(Config())
        data = parse_toml(text)
        self.assertIn("outputs", data)
        self.assertIn("viewer", data)
        self.assertIn("features", data)
        self.assertIn("scan", data)
        self.assertEqual(data["outputs"]["agent_dir"], "readmenator-agent")
        self.assertEqual(data["viewer"]["theme"], "dark")

    def test_toml_map_covers_deliverables(self) -> None:
        fields = set(TOML_MAP.values())
        for name in (
            "AGENT_OUTPUT_DIR", "WIKI_OUTPUT_DIR", "APIDOCS_OUTPUT_DIR",
            "GRAPHRAG_OUTPUT_DIR", "DIAGRAM_OUTPUT_DIR", "GH_WIKI_ENABLED",
            "FORCEGRAPH_ENABLED", "BUNDLEGRAPH_ENABLED",
        ):
            self.assertIn(name, fields)

    def test_ensure_creates_but_never_overwrites(self) -> None:
        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "readmenator.toml"
            first = ensure_project_config(tmp, Config())
            self.assertTrue(first.is_file())
            first.write_text("[viewer]\ntheme = \"light\"\n", encoding="utf-8")
            second = ensure_project_config(tmp, Config())
            self.assertEqual(second, target)
            self.assertIn('theme = "light"', target.read_text(encoding="utf-8"))

    def test_ensure_refuses_symlink(self) -> None:
        with TemporaryDirectory() as tmp:
            real = Path(tmp) / "real.toml"
            real.write_text("[viewer]\ntheme = \"light\"\n", encoding="utf-8")
            link = Path(tmp) / "readmenator.toml"
            try:
                link.symlink_to(real)
            except OSError:
                self.skipTest("symlinks unavailable")
            out = ensure_project_config(tmp, Config())
            self.assertTrue(out.is_symlink())
            self.assertEqual(real.read_text(encoding="utf-8").count("light"), 1)

    def test_load_applies_toml_over_defaults(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[outputs]\nagent_dir = \"custom-agent\"\n"
                "[features]\ngh_wiki_enabled = false\n"
                "[viewer]\ntheme = \"light\"\n",
                encoding="utf-8",
            )
            effective = load_project_config(tmp, Config())
            self.assertEqual(effective.AGENT_OUTPUT_DIR, "custom-agent")
            self.assertFalse(effective.GH_WIKI_ENABLED)
            self.assertEqual(effective.DIAGRAM_THEME, "light")

    def test_cli_flags_win_over_toml(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[viewer]\ntheme = \"dark\"\ncharge = -500\n", encoding="utf-8"
            )
            base = replace(Config(), DIAGRAM_THEME="light", FORCEGRAPH_CHARGE=-100)
            effective = load_project_config(tmp, base)
            self.assertEqual(effective.DIAGRAM_THEME, "light")
            self.assertEqual(effective.FORCEGRAPH_CHARGE, -100)

    def test_load_ignores_broken_toml(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[viewer\ntheme = ", encoding="utf-8"
            )
            effective = load_project_config(tmp, Config())
            self.assertEqual(effective, Config())

    def test_tuple_coercion(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[scan]\ninclude_dirs = [\"src\", \"lib\"]\nmax_file_mb = 5\n",
                encoding="utf-8",
            )
            effective = load_project_config(tmp, Config())
            self.assertEqual(effective.SCAN_INCLUDE_DIRS, ("src", "lib"))
            self.assertEqual(effective.MAX_FILE_SIZE_MB, 5.0)

    def test_viewer_config_dict_has_viewer_keys(self) -> None:
        viewer = viewer_config_dict(Config(), "/tmp/demo")
        for key in ("theme", "charge", "link_distance", "bundle_beta", "mode"):
            self.assertIn(key, viewer)
        self.assertIn("_meta", viewer)

    def test_write_viewer_config(self) -> None:
        with TemporaryDirectory() as tmp:
            maps = Path(tmp) / "readmenator-maps"
            written = write_viewer_config(maps, Config(), tmp)
            self.assertIsNotNone(written)
            data = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(data["theme"], "dark")

    def test_forcegraph_embeds_config_modal(self) -> None:
        renderer = ForceGraphRenderer(Config())
        payload = {"nodes": [], "edges": []}
        content = renderer.render(payload, {}, title="Demo")
        self.assertIn("data-rm-config", content)
        self.assertIn("rm-cfg-modal", content)
        self.assertIn("ReadmenatorViewerApply", content)
        self.assertIn("__RM_VIEWER__", content)

    def test_bundlegraph_embeds_config_modal(self) -> None:
        renderer = BundleGraphRenderer(Config())
        content = renderer.render({"nodes": [], "edges": []}, title="Demo")
        self.assertIn("data-rm-config", content)
        self.assertIn("rm-cfg-modal", content)

    def test_flows_embeds_config_modal(self) -> None:
        content = render_flows_page([], "Demo", config=Config())
        self.assertIn("data-rm-config", content)
        self.assertIn("rm-cfg-modal", content)

    def test_gallery_embeds_config_modal(self) -> None:
        publisher = DocsSitePublisher(Config())
        content = publisher.render_index("Demo", {}, {})
        self.assertIn("data-rm-config", content)
        self.assertIn("rm-cfg-modal", content)

    def test_maps_budgets_load_from_toml(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[maps]\nsourceview_max_files = 5000\n"
                "sourceview_max_total_chars = 1000000\n",
                encoding="utf-8",
            )
            effective = load_project_config(tmp, Config())
            self.assertEqual(effective.SOURCEVIEW_MAX_FILES, 5000)
            self.assertEqual(effective.SOURCEVIEW_MAX_TOTAL_CHARS, 1000000)

    def test_template_has_maps_and_messages_sections(self) -> None:
        data = parse_toml(template_text(Config()))
        self.assertIn("maps", data)
        self.assertIn("messages", data)
        self.assertEqual(data["maps"]["sourceview_max_files"], 2500)
        self.assertEqual(data["messages"]["readme_heading"], "")
        viewer = viewer_config_dict(Config(), "/tmp/demo")
        self.assertIn("maps", viewer)
        self.assertIn("messages", viewer)
        self.assertEqual(viewer["maps"]["sourceview_max_files"], 2500)

    def test_example_toml_matches_template(self) -> None:
        example = Path(__file__).resolve().parent.parent / "example.readmenator.toml"
        self.assertEqual(
            parse_toml(example.read_text(encoding="utf-8")),
            parse_toml(template_text(Config())),
        )

    def test_modal_schema_covers_maps_and_messages(self) -> None:
        from readmenator._viewer_ui import VIEWER_SCHEMA, viewer_json

        by_key = {spec["key"]: spec for spec in VIEWER_SCHEMA}
        self.assertEqual(by_key["sourceview_max_files"]["section"], "maps")
        self.assertEqual(by_key["sourceview_max_total_chars"]["section"], "maps")
        for key in (
            "readme_heading", "readme_intro", "readme_agents_line",
            "readme_developers_line", "readme_regen_command", "agent_heading",
            "agent_intro", "agent_extra", "folder_notice",
        ):
            self.assertEqual(by_key[key]["section"], "messages")
        embedded = json.loads(viewer_json(Config()))
        for key in ("sourceview_max_files", "readme_heading", "agent_extra"):
            self.assertIn(key, embedded)

    def test_messages_load_from_toml_with_multiline(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[messages]\nreadme_heading = \"Docs\"\n"
                "agent_extra = \"Line one.\\nLine two.\"\n",
                encoding="utf-8",
            )
            effective = load_project_config(tmp, Config())
            self.assertEqual(effective.MSG_README_HEADING, "Docs")
            self.assertEqual(effective.MSG_AGENT_EXTRA, "Line one.\nLine two.")

    def test_mini_parser_keeps_hash_inside_quotes(self) -> None:
        from readmenator._project_config import _mini_toml_parse

        data = _mini_toml_parse('[branding]\naccent = "#22d3ee" # brand\n')
        self.assertEqual(data["branding"]["accent"], "#22d3ee")

    def test_readme_injector_message_overrides(self) -> None:
        from readmenator._readme_injector import ReadmeInjector

        injector = ReadmeInjector(
            readme_heading="Project Docs",
            readme_intro="Custom intro with {braces} inside.",
            readme_agents_line="Agents: start here.",
            readme_developers_line="Devs: start there.",
            readme_regen_command="make docs",
        )
        with TemporaryDirectory() as tmp:
            readme = Path(tmp) / "README.md"
            readme.write_text("# Demo\n", encoding="utf-8")
            self.assertTrue(injector.inject(str(tmp)))
            content = readme.read_text(encoding="utf-8")
            self.assertIn("## Project Docs", content)
            self.assertIn("Custom intro with {braces} inside.", content)
            self.assertIn("Agents: start here.", content)
            self.assertIn("Devs: start there.", content)
            self.assertIn("`make docs`", content)
            self.assertNotIn("Knowledge Base", content)
            self.assertFalse(injector.inject(str(tmp)))

    def test_readme_injector_rst_underline_matches_heading(self) -> None:
        from readmenator._readme_injector import ReadmeInjector

        injector = ReadmeInjector(readme_heading="A Much Longer Custom Heading")
        with TemporaryDirectory() as tmp:
            readme = Path(tmp) / "README.rst"
            readme.write_text("Demo\n====\n", encoding="utf-8")
            self.assertTrue(injector.inject(str(tmp)))
            lines = readme.read_text(encoding="utf-8").splitlines()
            idx = lines.index("A Much Longer Custom Heading")
            self.assertEqual(lines[idx + 1], "-" * len("A Much Longer Custom Heading"))

    def test_agent_injector_message_overrides(self) -> None:
        from readmenator._agent_injector import AgentInjector

        injector = AgentInjector(
            agent_heading="Read This First",
            agent_intro="Custom intro.",
            agent_extra="Project rule: {always} run tests.",
        )
        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "AGENTS.md"
            target.write_text("# Agents\n", encoding="utf-8")
            self.assertEqual(injector.inject(str(tmp)), 1)
            content = target.read_text(encoding="utf-8")
            self.assertIn("## Read This First", content)
            self.assertIn("Custom intro.", content)
            self.assertIn("Project rule: {always} run tests.", content)
            self.assertNotIn("MUST read before coding", content)
            self.assertEqual(injector.inject(str(tmp)), 0)

    def test_folder_readme_notice_override(self) -> None:
        from readmenator._folder_readme import FolderReadmeWriter

        writer = FolderReadmeWriter(replace(Config(), MSG_FOLDER_NOTICE="Custom notice."))
        with TemporaryDirectory() as tmp:
            folder = Path(tmp) / "readmenator-agent"
            folder.mkdir()
            (folder / "INDEX.md").write_text("x", encoding="utf-8")
            written = writer.write_all(str(tmp))
            self.assertEqual(len(written), 1)
            content = Path(written[0]).read_text(encoding="utf-8")
            self.assertIn("Custom notice.", content)
            self.assertNotIn("zero LLM tokens", content)


class TestViewerModalBehavior(unittest.TestCase):
    def test_gallery_config_button_matches_theme_style(self) -> None:
        content = DocsSitePublisher(Config()).render_index("Demo", {}, {})
        self.assertIn("#theme,.toolbar [data-rm-config]", content)
        self.assertNotIn("rm-cfg-btn", content)

    def test_modal_applies_only_dirty_keys_with_honest_status(self) -> None:
        from readmenator._viewer_ui import VIEWER_MODAL_JS

        self.assertIn("window.__rmCfgBase__", VIEWER_MODAL_JS)
        self.assertIn("Needs rebuild:", VIEWER_MODAL_JS)
        self.assertIn("Live:", VIEWER_MODAL_JS)

    def test_modal_reset_asks_for_confirmation(self) -> None:
        from readmenator._viewer_ui import VIEWER_MODAL_JS

        self.assertIn("window.confirm(", VIEWER_MODAL_JS)

    def test_forcegraph_hook_maps_modal_keys_and_busts_ink_cache(self) -> None:
        from readmenator._forcegraph_page import FORCEGRAPH_PAGE_TEMPLATE

        self.assertIn('hulls_enabled:"hulls"', FORCEGRAPH_PAGE_TEMPLATE)
        self.assertIn('label_top_n:"labelTopN"', FORCEGRAPH_PAGE_TEMPLATE)
        self.assertIn("link_distance", FORCEGRAPH_PAGE_TEMPLATE)
        self.assertIn("inkCache=null", FORCEGRAPH_PAGE_TEMPLATE)
        self.assertIn("labelSet.clear()", FORCEGRAPH_PAGE_TEMPLATE)
        self.assertIn("S.hulls=!!SETTINGS.hulls", FORCEGRAPH_PAGE_TEMPLATE)
        hook = FORCEGRAPH_PAGE_TEMPLATE.split("ReadmenatorViewerApply=")[1].split("};")[0]
        self.assertNotIn("return true", hook)
        self.assertNotIn("return false", hook)

    def test_bundlegraph_hook_rebuilds_labels_and_busts_ink(self) -> None:
        from readmenator._bundlegraph_page import BUNDLEGRAPH_PAGE_TEMPLATE

        self.assertIn("topSet.clear()", BUNDLEGRAPH_PAGE_TEMPLATE)
        self.assertIn("INK=null", BUNDLEGRAPH_PAGE_TEMPLATE)

    def test_flows_hook_uses_global_draw(self) -> None:
        from readmenator._flowpage import _PAGE

        hook = _PAGE.split("ReadmenatorViewerApply=")[1].split(";</script>")[0]
        self.assertIn("__rmFlowsDraw__", hook)

    def test_toml_viewer_keys_reach_embedded_settings(self) -> None:
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "readmenator.toml").write_text(
                "[viewer]\ncharge = -555\nlink_distance = 200\n",
                encoding="utf-8",
            )
            effective = load_project_config(tmp, Config())
            settings = ForceGraphRenderer(effective).page_settings(
                {"nodes": [], "edges": []}
            )
            self.assertEqual(settings["charge"], -555)
            self.assertEqual(settings["linkDistance"], 200)


if __name__ == "__main__":
    unittest.main()
