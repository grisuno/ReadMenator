"""Contract tests for agent-facing output quality: budgets, purposes, freshness, noise."""

import json
import os
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from readmenator._agent_output import AgentOutputGenerator
from readmenator._config import Config
from readmenator._diagrams import DocsSitePublisher
from readmenator._gitmeta import read_git_head
from readmenator._layers import LayerDetector
from readmenator._models import AnalysisResultV2, ChangeImpact, Edge, Node, Symbol
from readmenator._purpose import file_purpose, first_sentence, truncate_words
from readmenator._resolver import ImportResolver
from readmenator._scanner import PolyglotScanner


def _node(node_id: str, doc: str = "", symbols=None) -> Node:
    """Build a Python file node for tests."""
    return Node(
        node_id=node_id, label=os.path.basename(node_id), kind="module",
        language="py", doc=doc, symbols=symbols or [],
    )


def _edge(source: str, target: str, relation: str = "imports") -> Edge:
    """Build an extracted edge for tests."""
    return Edge(source=source, target=target, relation=relation, confidence="EXTRACTED")


def _big_project(files: int, symbols_per_file: int):
    """Build a project large enough to force pagination of every document."""
    nodes = [
        _node(
            f"pkg/mod_{i}.py",
            doc=f"Module {i} does work.",
            symbols=[
                Symbol(name=f"func_{i}_{j}", kind="function", line=j + 1,
                       doc="Compute a value.", signature=f"def func_{i}_{j}(x)")
                for j in range(symbols_per_file)
            ],
        )
        for i in range(files)
    ]
    resolved = [
        _edge(f"pkg/mod_{i}.py", f"pkg/mod_{(i + 1) % files}.py", "resolved_imports")
        for i in range(files)
    ]
    return nodes, resolved


class TestAgentOutputBudget(unittest.TestCase):
    """Every generated document respects the line cap, with nothing lost."""

    def test_agent_output_pages_respect_line_cap_on_large_projects(self) -> None:
        config = Config()
        nodes, resolved = _big_project(files=120, symbols_per_file=12)
        with tempfile.TemporaryDirectory() as tmpdir:
            AgentOutputGenerator(config).generate(
                nodes, [], resolved, None, None, [], {}, tmpdir,
            )
            out = Path(tmpdir) / config.AGENT_OUTPUT_DIR
            for md_file in out.rglob("*.md"):
                count = len(md_file.read_text().splitlines())
                self.assertLessEqual(count, config.AGENT_OUTPUT_MAX_LINES, md_file.name)
            self.assertTrue((out / "SYMBOLS_p2.md").exists())

    def test_agent_output_pagination_keeps_every_symbol_greppable(self) -> None:
        config = Config()
        nodes, resolved = _big_project(files=60, symbols_per_file=15)
        with tempfile.TemporaryDirectory() as tmpdir:
            AgentOutputGenerator(config).generate(
                nodes, [], resolved, None, None, [], {}, tmpdir,
            )
            out = Path(tmpdir) / config.AGENT_OUTPUT_DIR
            text = "".join(p.read_text() for p in sorted(out.glob("SYMBOLS*.md")))
            for node in nodes:
                for sym in node.symbols:
                    self.assertIn(f"`{sym.name}`", text)

    def test_agent_output_pages_repeat_table_header_and_link_next(self) -> None:
        config = replace(Config(), AGENT_OUTPUT_MAX_LINES=20)
        gen = AgentOutputGenerator(config)
        content = gen._build_symbols(_big_project(files=5, symbols_per_file=10)[0])
        pages = gen._paginate("SYMBOLS.md", content)
        self.assertGreater(len(pages), 1)
        for page in pages:
            self.assertIn("| Symbol | Kind |", page)
            self.assertLessEqual(len(page.splitlines()), 20)
        self.assertIn("Next: [SYMBOLS_p2.md](SYMBOLS_p2.md)", pages[0])
        self.assertIn("Previous: [SYMBOLS.md](SYMBOLS.md)", pages[1])

    def test_agent_output_prunes_stale_pages(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir) / config.AGENT_OUTPUT_DIR
            out.mkdir()
            (out / "API_p9.md").write_text("stale")
            (out / "NOTES.md").write_text("user file")
            AgentOutputGenerator(config).generate(
                [_node("a.py")], [], [], None, None, [], {}, tmpdir,
            )
            self.assertFalse((out / "API_p9.md").exists())
            self.assertTrue((out / "NOTES.md").exists())


class TestAgentOutputSignal(unittest.TestCase):
    """Documents carry signal, not repetition."""

    def test_api_states_dependencies_once_per_file(self) -> None:
        gen = AgentOutputGenerator(Config())
        node = _node("lib.py", symbols=[
            Symbol(name=f"f{i}", kind="function", line=i + 1) for i in range(5)
        ])
        content = gen._build_api([node], {("lib.py", "dep.py"): "resolved_imports"}, {"lib.py": ["main.py"]})
        self.assertEqual(content.count("Depends on:"), 1)
        self.assertEqual(content.count("Imported by:"), 1)

    def test_api_skips_private_helpers_and_test_layer(self) -> None:
        gen = AgentOutputGenerator(Config())
        nodes = [
            _node("lib.py", symbols=[
                Symbol(name="public", kind="function", line=1),
                Symbol(name="_private", kind="function", line=2),
            ]),
            _node("tests/test_lib.py", symbols=[Symbol(name="test_x", kind="method", line=1)]),
        ]
        content = gen._build_api(nodes, {}, {}, {"tests/test_lib.py": "testing"})
        self.assertIn("`public`", content)
        self.assertNotIn("_private", content)
        self.assertNotIn("test_x", content)

    def test_api_qualifies_methods_with_owner_class(self) -> None:
        gen = AgentOutputGenerator(Config())
        node = _node("svc.py", symbols=[
            Symbol(name="Service", kind="class", line=1),
            Symbol(name="run", kind="method", line=3),
        ])
        self.assertIn("`Service.run`", gen._build_api([node], {}, {}))

    def test_architecture_external_excludes_internally_resolved_imports(self) -> None:
        gen = AgentOutputGenerator(Config())
        nodes = [_node("pkg/__init__.py"), _node("pkg/core.py"), _node("main.py")]
        edges = [_edge("main.py", "pkg.core"), _edge("main.py", "requests")]
        content = gen._build_architecture(edges, [_edge("main.py", "pkg/core.py", "resolved_imports")], nodes)
        external = content.split("## External Imports", 1)[1]
        self.assertIn("requests", external)
        self.assertNotIn("pkg.core", external)

    def test_index_reports_used_by_count_and_escapes_pipes(self) -> None:
        gen = AgentOutputGenerator(Config())
        nodes = [_node("a.py", doc="Parses a | b tables."), _node("b.py")]
        content = gen._build_index(nodes, {"root": nodes}, {"a.py": ["b.py", "b.py"]})
        self.assertIn("| Used by |", content)
        self.assertIn("a \\| b", content)
        self.assertIn("| 1 |", content)

    def test_gotchas_exclude_test_layer_and_report_blast_radius(self) -> None:
        gen = AgentOutputGenerator(Config())
        v2 = AnalysisResultV2(
            taint=None, cycles=[], hotspots=[], suggested_rules=[], layer_violations=[],
            change_impacts=[
                ChangeImpact("core.py", ["a.py"], ["b.py"], 2),
                ChangeImpact("tests/test_core.py", ["x.py"], [], 1),
            ],
        )
        content = gen._build_gotchas(None, v2, [], {"tests/test_core.py": "testing"})
        self.assertIn("Blast Radius", content)
        self.assertIn("`core.py` -- 1 direct, 2 total dependents", content)
        self.assertNotIn("tests/test_core.py", content)


class TestPurposeExtraction(unittest.TestCase):
    """File purposes are one clean sentence with a symbol fallback."""

    def test_purpose_takes_first_sentence(self) -> None:
        self.assertEqual(first_sentence("Parse files. Then more detail."), "Parse files.")

    def test_purpose_skips_banners_and_spdx(self) -> None:
        self.assertEqual(first_sentence("=========\nSPDX-License-Identifier: MIT\n\nReal purpose here."), "Real purpose here.")

    def test_purpose_falls_back_to_primary_public_symbol(self) -> None:
        node = _node("svc.py", symbols=[
            Symbol(name="_helper", kind="function", line=1, doc="Private helper."),
            Symbol(name="Service", kind="class", line=5, doc="Runs the service loop."),
        ])
        self.assertEqual(file_purpose(node, 100), "Service: Runs the service loop.")

    def test_purpose_truncates_on_word_boundary(self) -> None:
        result = truncate_words("alpha beta gamma delta epsilon", 16)
        self.assertTrue(result.endswith("..."))
        self.assertLessEqual(len(result), 16)
        self.assertNotIn("gam...", result)


class TestManifestFreshness(unittest.TestCase):
    """MANIFEST lets an agent decide staleness without reading anything else."""

    def _git_repo(self, root: Path, packed: bool) -> str:
        """Create a minimal git directory layout pointing at a fixed commit."""
        commit = "0123456789abcdef0123456789abcdef01234567"
        git = root / ".git"
        (git / "refs" / "heads").mkdir(parents=True)
        (git / "HEAD").write_text("ref: refs/heads/main\n")
        if packed:
            (git / "packed-refs").write_text(f"# pack-refs\n{commit} refs/heads/main\n")
        else:
            (git / "refs" / "heads" / "main").write_text(commit + "\n")
        return commit

    def test_gitmeta_reads_loose_and_packed_refs(self) -> None:
        for packed in (False, True):
            with tempfile.TemporaryDirectory() as tmpdir:
                commit = self._git_repo(Path(tmpdir), packed)
                self.assertEqual(read_git_head(tmpdir), {"commit": commit, "branch": "main"})

    def test_gitmeta_outside_repository_is_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            self.assertEqual(read_git_head(tmpdir), {"commit": "", "branch": ""})

    def test_manifest_has_commit_relative_root_and_inventory(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            commit = self._git_repo(Path(tmpdir), packed=False)
            AgentOutputGenerator(config).generate(
                [_node("cli/main.py"), _node("tests/main.py")], [_edge("cli/main.py", "os")],
                [], None, None, [], {"tests/main.py": "testing"}, tmpdir,
            )
            raw = (Path(tmpdir) / config.AGENT_OUTPUT_DIR / "MANIFEST.json").read_text()
            manifest = json.loads(raw)
            self.assertEqual(manifest["git_commit"], commit)
            self.assertEqual(manifest["project_root"], ".")
            self.assertNotIn(str(Path(tmpdir).resolve()), raw)
            self.assertEqual(manifest["imports"], 1)
            self.assertEqual(manifest["entrypoints"], ["cli/main.py"])
            paths = {d["path"] for d in manifest["documents"]}
            self.assertIn("INDEX.md", paths)
            self.assertTrue(all(d["approx_tokens"] > 0 for d in manifest["documents"]))


class TestNoiseReduction(unittest.TestCase):
    """Generated artifacts and naive heuristics never pollute the graph."""

    def test_scanner_skips_own_generated_outputs(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "app.py").write_text("def run():\n    pass\n")
            (root / ".refactor_app.sh").write_text("#!/bin/sh\necho hi\n")
            (root / config.RULE_GEN_OUTPUT_DIR).mkdir()
            (root / config.RULE_GEN_OUTPUT_DIR / "gen.py").write_text("x = 1\n")
            scanner = PolyglotScanner(config)
            nodes, _ = scanner.scan(root)
            self.assertEqual([n.node_id for n in nodes], ["app.py"])
            self.assertEqual(scanner.last_skip_counts.get("generated"), 2)

    def test_resolver_prefers_root_package_over_launcher_shim(self) -> None:
        resolver = ImportResolver(["tool.py", "tool/__init__.py", "tool/core.py"])
        self.assertEqual(resolver.resolve("tool", "tool/core.py"), "tool/__init__.py")

    def test_layers_match_whole_words_not_substrings(self) -> None:
        detector = LayerDetector()
        nodes = [_node("pkg/diagrams.py"), _node("pkg/build_guide.py"), _node("pkg/views/home.py")]
        layers = detector.detect(nodes, [])
        self.assertEqual(layers["pkg/diagrams.py"], "utility")
        self.assertEqual(layers["pkg/build_guide.py"], "utility")
        self.assertEqual(layers["pkg/views/home.py"], "presentation")

    def test_layers_test_framework_import_needs_test_path(self) -> None:
        detector = LayerDetector()
        nodes = [_node("pkg/__main__.py"), _node("tests/helpers.py")]
        edges = [_edge("pkg/__main__.py", "unittest"), _edge("tests/helpers.py", "unittest")]
        layers = detector.detect(nodes, edges)
        self.assertEqual(layers["pkg/__main__.py"], "utility")
        self.assertEqual(layers["tests/helpers.py"], "testing")


class TestLlmsTxt(unittest.TestCase):
    """The published site exposes an llms.txt entry point for agents."""

    def test_llms_txt_lists_wiki_before_agent_docs(self) -> None:
        publisher = DocsSitePublisher(Config())
        docs = [
            {"name": "readmenator-agent/API.md", "href": "md/readmenator-agent/API.md", "preview": "# API"},
            {"name": "readmenator-agent/INDEX.md", "href": "md/readmenator-agent/INDEX.md", "preview": "# Index"},
            {"name": "readmenator-wiki/index.md", "href": "md/readmenator-wiki/index.md", "preview": "# Wiki"},
        ]
        text = publisher.render_llms_txt("Demo", {}, {"files": 3}, "maps/", docs)
        self.assertTrue(text.startswith("# Demo\n\n> "))
        self.assertLess(text.index("## Wiki"), text.index("## Agent Docs"))
        self.assertLess(text.index("INDEX.md]"), text.index("API.md]"))

    def test_publish_writes_llms_txt(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            written = DocsSitePublisher(config).publish({}, "Demo", tmpdir, doc_entries=[], video_rel=None)
            self.assertIn("llms", written)
            self.assertTrue((Path(tmpdir) / config.SITE_LLMS_TXT_FILENAME).is_file())


if __name__ == "__main__":
    unittest.main()


class TestCommunityHubDamping(unittest.TestCase):
    """A shared hub imported by every file must not merge unrelated clusters."""

    def test_communities_survive_a_shared_hub(self) -> None:
        from readmenator._analyzer import GraphAnalyzer

        groups = {g: [f"{g}/m{i}.py" for i in range(6)] for g in ("a", "b", "c")}
        files = [f for members in groups.values() for f in members] + ["core/models.py"]
        nodes = [_node(f) for f in files]
        resolved = []
        for members in groups.values():
            for i, src in enumerate(members):
                resolved.append(_edge(src, members[(i + 1) % len(members)], "resolved_imports"))
                resolved.append(_edge(src, "core/models.py", "resolved_imports"))
        result = GraphAnalyzer(Config()).analyze(nodes, [], resolved)
        community_of = {f: c.community_id for c in result.communities for f in c.file_ids}
        self.assertEqual(len(result.communities), 3)
        self.assertNotEqual(community_of.get("a/m0.py"), community_of.get("b/m0.py"))
        self.assertEqual(len({community_of.get(f) for f in groups["a"]}), 1)


class TestSourceFreshness(unittest.TestCase):
    """Docs freshness is verifiable from content, independent of commit timing."""

    def test_fingerprint_changes_with_content_not_with_order(self) -> None:
        from readmenator._cache import source_fingerprint

        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "a.py").write_text("x = 1\n")
            (Path(tmpdir) / "b.py").write_text("y = 2\n")
            first = source_fingerprint(tmpdir, ["a.py", "b.py"])
            self.assertEqual(first, source_fingerprint(tmpdir, ["b.py", "a.py"]))
            (Path(tmpdir) / "a.py").write_text("x = 3\n")
            self.assertNotEqual(first, source_fingerprint(tmpdir, ["a.py", "b.py"]))

    def test_check_freshness_detects_source_edits(self) -> None:
        from readmenator._app import readmenatorApplication

        config = replace(
            Config(), VIDEO_ENABLED=False, DIAGRAM_ENABLED=False,
            AGENT_INJECTION_ENABLED=False, README_INJECTION_ENABLED=False,
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            source = Path(tmpdir) / "app.py"
            source.write_text('"""App."""\n\ndef run():\n    return 1\n')
            app = readmenatorApplication(config)
            self.assertFalse(app.check_freshness(tmpdir)[0])
            app.run(tmpdir)
            self.assertTrue(app.check_freshness(tmpdir)[0])
            source.write_text('"""App."""\n\ndef run():\n    return 2\n')
            fresh, reason = app.check_freshness(tmpdir)
            self.assertFalse(fresh)
            self.assertTrue(reason.startswith("stale"))


class TestCommunityShaping(unittest.TestCase):
    """Tiny groups fold into neighbors and shared-directory labels stay distinct."""

    def test_small_community_merges_into_best_connected_neighbor(self) -> None:
        from readmenator._analyzer import GraphAnalyzer

        analyzer = GraphAnalyzer(Config())
        groups = {0: ["a1", "a2", "a3", "a4"], 1: ["b1", "b2", "b3", "b4"], 2: ["p1", "p2"]}
        adjacency = {
            "p1": {"a1", "a2", "b1"}, "p2": {"a3"},
            "a1": {"p1"}, "a2": {"p1"}, "a3": {"p2"}, "b1": {"p1"},
        }
        weights = {fid: 1.0 for members in groups.values() for fid in members}
        merged = analyzer._merge_small_communities(groups, adjacency, weights)
        self.assertEqual(sorted(merged), [0, 1])
        self.assertIn("p1", merged[0])

    def test_shared_directory_labels_use_core_file(self) -> None:
        from readmenator._analyzer import GraphAnalyzer

        nodes = [
            _node("pkg/video.py", symbols=[Symbol("a", "function", 1), Symbol("b", "function", 2)]),
            _node("pkg/v_util.py"), _node("pkg/wiki.py", symbols=[Symbol("c", "function", 1)]),
            _node("pkg/w_util.py"), _node("tests/test_video.py", symbols=[Symbol(f"t{i}", "method", i) for i in range(9)]),
        ]
        labels = GraphAnalyzer(Config())._label_communities(
            nodes, {0: ["pkg/video.py", "pkg/v_util.py", "tests/test_video.py"], 1: ["pkg/wiki.py", "pkg/w_util.py"]},
        )
        self.assertEqual(labels, {0: "pkg: video", 1: "pkg: wiki"})


class TestSiteDocsPruning(unittest.TestCase):
    """The static site never keeps copies of docs that were renamed or removed."""

    def test_publish_assets_prunes_stale_markdown(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as project, tempfile.TemporaryDirectory() as site:
            wiki = Path(project) / config.WIKI_OUTPUT_DIR
            wiki.mkdir()
            (wiki / "index.md").write_text("# Wiki\n")
            stale = Path(site) / config.SITE_DOCS_SUBDIR / config.WIKI_OUTPUT_DIR / "community_9_old.md"
            stale.parent.mkdir(parents=True)
            stale.write_text("old")
            DocsSitePublisher(config).publish_assets(project, site)
            self.assertFalse(stale.exists())
            self.assertTrue((stale.parent / "index.md").exists())


class TestLouvainCommunities(unittest.TestCase):
    """Default community detection is deterministic modularity optimisation."""

    def _two_cliques(self):
        """Two dense groups joined by one bridge edge."""
        left = [f"left/m{i}.py" for i in range(5)]
        right = [f"right/m{i}.py" for i in range(5)]
        resolved = []
        for group in (left, right):
            for i, src in enumerate(group):
                for tgt in group[i + 1:]:
                    resolved.append(_edge(src, tgt, "resolved_imports"))
        resolved.append(_edge(left[0], right[0], "resolved_imports"))
        return [_node(f) for f in left + right], resolved

    def test_louvain_splits_bridged_cliques(self) -> None:
        from readmenator._analyzer import GraphAnalyzer

        nodes, resolved = self._two_cliques()
        result = GraphAnalyzer(Config()).analyze(nodes, [], resolved)
        groups = sorted(sorted(c.file_ids) for c in result.communities)
        self.assertEqual(len(groups), 2)
        self.assertTrue(all(len({f.split("/")[0] for f in g}) == 1 for g in groups))

    def test_louvain_is_deterministic_and_numbered_by_size(self) -> None:
        from readmenator._analyzer import GraphAnalyzer

        nodes, resolved = self._two_cliques()
        runs = [
            [(c.community_id, sorted(c.file_ids)) for c in GraphAnalyzer(Config()).analyze(list(reversed(nodes)) if i else nodes, [], resolved).communities]
            for i in range(2)
        ]
        self.assertEqual(runs[0], runs[1])
        self.assertEqual(Config().COMMUNITY_ALGORITHM, "louvain")

    def test_community_label_ignores_test_directory(self) -> None:
        from readmenator._analyzer import GraphAnalyzer

        nodes = [_node("src/core.py"), _node("tests/test_a.py"), _node("tests/test_b.py")]
        labels = GraphAnalyzer(Config())._label_communities(
            nodes, {0: ["src/core.py", "tests/test_a.py", "tests/test_b.py"]},
        )
        self.assertEqual(labels[0], "src")


class TestGalleryIndex(unittest.TestCase):
    """The gallery groups docs, collapses pages, shows titles, and stays offline."""

    def _entries(self):
        """Doc entries covering wiki, agent pages, recipes, and project docs."""
        return [
            {"name": "readmenator-wiki/index.md", "href": "md/readmenator-wiki/index.md", "preview": "Overview.", "lines": "10", "chars": "400", "title": "Second Brain"},
            {"name": "readmenator-wiki/community_0_core.md", "href": "md/readmenator-wiki/community_0_core.md", "preview": "", "lines": "5", "chars": "100", "title": "core"},
            {"name": "readmenator-agent/API.md", "href": "md/readmenator-agent/API.md", "preview": "", "lines": "500", "chars": "4000", "title": "API"},
            {"name": "readmenator-agent/API_p2.md", "href": "md/readmenator-agent/API_p2.md", "preview": "", "lines": "100", "chars": "800", "title": "API"},
            {"name": "readmenator-agent/recipes/fix-cycle.md", "href": "md/readmenator-agent/recipes/fix-cycle.md", "preview": "", "lines": "7", "chars": "70", "title": "Recipe"},
            {"name": "KNOWLEDGE_BASE.md", "href": "md/KNOWLEDGE_BASE.md", "preview": "", "lines": "9", "chars": "90", "title": "KB"},
        ]

    def test_gallery_groups_docs_and_collapses_pages(self) -> None:
        html = DocsSitePublisher(Config()).render_index("Demo", {}, {"files": 3}, "", "v.mp4", self._entries(), "poster.jpg")
        for group in ('data-group="wiki"', 'data-group="agent"', 'data-group="recipes"', 'data-group="project"'):
            self.assertIn(group, html)
        self.assertEqual(html.count('data-doc="readmenator-agent/API'), 1)
        self.assertIn('class="page doc-open"', html)
        self.assertIn("600 lines", html)
        self.assertIn("<h3>Second Brain</h3>", html)
        self.assertLess(html.index("Second Brain"), html.index("<h3>core</h3>"))

    def test_gallery_video_has_poster_and_start_here(self) -> None:
        html = DocsSitePublisher(Config()).render_index("Demo", {}, {"files": 3}, "", "v.mp4", self._entries(), "poster.jpg")
        self.assertIn('poster="poster.jpg"', html)
        self.assertIn("Start here", html)
        self.assertIn('data-count="3"', html)

    def test_gallery_has_no_external_resources_and_escapes_titles(self) -> None:
        entries = self._entries()
        entries[0]["title"] = "<img src=x onerror=alert(1)>"
        html = DocsSitePublisher(Config()).render_index("Demo", {}, {}, "", None, entries)
        self.assertNotIn('src="http', html)
        self.assertNotIn('href="http', html)
        self.assertNotIn("<img src=x", html)

    def test_doc_preview_skips_markdown_syntax(self) -> None:
        publisher = DocsSitePublisher(Config())
        text = "# Title\n\n| a | b |\n|---|---|\nPages: [x](x)\n\nThe **real** sentence about [this](y.md) module.\n"
        self.assertEqual(publisher._doc_preview(text), "The real sentence about this module.")
        self.assertEqual(publisher._doc_title("# API (page 1 of 3)\n"), "API")


class TestLiveMapCommunities(unittest.TestCase):
    """Live maps color by code community, size by degree, and map layers to honest roles."""

    def _inputs(self):
        """Two communities of files with resolved imports and layers."""
        from readmenator._analyzer import GraphAnalyzer

        files = [f"left/m{i}.py" for i in range(5)] + [f"right/m{i}.py" for i in range(5)]
        nodes = [_node(f) for f in files]
        resolved = []
        for side in ("left", "right"):
            group = [f for f in files if f.startswith(side)]
            for i, src in enumerate(group):
                for tgt in group[i + 1:]:
                    resolved.append(_edge(src, tgt, "resolved_imports"))
        analysis = GraphAnalyzer(Config()).analyze(nodes, [], resolved)
        layers = {f: "utility" for f in files}
        return nodes, resolved, layers, analysis

    def test_built_maps_carry_community_and_core_role(self) -> None:
        from readmenator._diagrams import SystemMapBuilder

        nodes, resolved, layers, analysis = self._inputs()
        system_map = SystemMapBuilder(Config()).build(nodes, [], resolved, layers, [], analysis, "architecture", True)
        self.assertTrue(system_map.nodes)
        self.assertTrue(all(n.community >= 0 for n in system_map.nodes))
        self.assertNotIn("external", {n.role for n in system_map.nodes})

    def test_vis_render_includes_legend_and_dot_scaling(self) -> None:
        from readmenator._diagrams import SystemMapBuilder, VisNetworkRenderer

        nodes, resolved, layers, analysis = self._inputs()
        system_map = SystemMapBuilder(Config()).build(nodes, [], resolved, layers, [], analysis, "architecture", True)
        html = VisNetworkRenderer(Config()).render(system_map)
        self.assertIn('"communities"', html)
        self.assertIn('shape:"dot"', html)
        self.assertIn('data-action="color"', html)
        self.assertIn("#community=", html)
