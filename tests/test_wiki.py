import json
import os
import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node, Symbol
from readmenator._wiki import WikiGenerator


def _make_node(node_id: str, doc: str = "", symbols=None, language: str = "py") -> Node:
    return Node(
        node_id=node_id,
        label=os.path.basename(node_id),
        kind="module",
        language=language,
        doc=doc,
        symbols=symbols or [],
    )


def _make_symbol(name: str, kind: str = "function", line: int = 1, doc: str = "") -> Symbol:
    return Symbol(name=name, kind=kind, line=line, doc=doc, signature=f"{name}()")


def _make_analysis() -> AnalysisResult:
    return AnalysisResult(
        god_nodes=[("app.py", 6.0), ("db.py", 4.0)],
        communities=[
            CommunityResult(0, "core", {"app.py", "db.py"}, 0.8, 2),
            CommunityResult(1, "util", {"utils.py"}, 1.0, 1),
        ],
        surprising_connections=[("app.py", "utils.py", 3, [0, 1])],
        suggested_questions=["What breaks if app.py changes?"],
        node_count=3,
        edge_count=2,
    )


def _make_nodes() -> list:
    return [
        _make_node("app.py", doc="App entry.", symbols=[_make_symbol("main", doc="Run.")]),
        _make_node("db.py", doc="DB layer.", symbols=[_make_symbol("save", doc="Save.")]),
        _make_node("utils.py", symbols=[_make_symbol("slug")]),
    ]


class TestWikiConfigContract(unittest.TestCase):
    def test_config_defaults(self) -> None:
        config = Config()
        self.assertTrue(config.WIKI_ENABLED)
        self.assertEqual(config.WIKI_OUTPUT_DIR, "readmenator-wiki")
        self.assertEqual(config.WIKI_MAX_FILES_PER_PAGE, 20)
        self.assertEqual(config.WIKI_MAX_SYMBOLS_PER_PAGE, 30)
        self.assertEqual(config.WIKI_MAX_CONNECTIONS, 20)

    def test_config_immutable(self) -> None:
        from dataclasses import FrozenInstanceError
        config = Config()
        with self.assertRaises(FrozenInstanceError):
            config.WIKI_ENABLED = False  # type: ignore[misc]


class TestWikiGenerationContract(unittest.TestCase):
    def test_generate_writes_all_files(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        resolved = [Edge("app.py", "db.py", "resolved_imports", "EXTRACTED")]
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], resolved, _make_analysis(), {"app.py": "utility"}, [], None, tmp)
            out_path = Path(out)
            self.assertTrue((out_path / "index.md").exists())
            self.assertTrue((out_path / "connections.json").exists())
            self.assertTrue((out_path / "queries.md").exists())
            self.assertTrue((out_path / "REPORT.md").exists())
            pages = sorted(out_path.glob("community_*.md"))
            self.assertEqual(len(pages), 2)

    def test_community_page_sections(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        resolved = [Edge("app.py", "db.py", "resolved_imports", "EXTRACTED")]
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], resolved, _make_analysis(), {}, [], None, tmp)
            pages = sorted(Path(out).glob("community_*.md"))
            content = pages[0].read_text(encoding="utf-8")
            for section in ("## Definition", "## Files", "## Key Symbols",
                            "## Internal vs External Edges", "## Connections",
                            "## Risks", "## Open Questions", "## Sources"):
                self.assertIn(section, content)

    def test_connections_typed_with_confidence(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        resolved = [Edge("app.py", "utils.py", "resolved_imports", "EXTRACTED")]
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], resolved, _make_analysis(), {}, [], None, tmp)
            data = json.loads((Path(out) / "connections.json").read_text(encoding="utf-8"))
            self.assertTrue(len(data) >= 2)
            by_type = {d["connection_type"] for d in data}
            self.assertIn("depends_on", by_type)
            self.assertIn("bridges", by_type)
            confidences = {d["confidence"] for d in data}
            self.assertIn("EXTRACTED", confidences)
            self.assertIn("INFERRED", confidences)
            strengths = [float(d["strength"]) for d in data]
            self.assertEqual(strengths, sorted(strengths, reverse=True))
            for entry in data:
                self.assertIn("explanation", entry)

    def test_fallback_single_community_without_analysis(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], None, {}, [], None, tmp)
            pages = sorted(Path(out).glob("community_*.md"))
            self.assertEqual(len(pages), 1)
            self.assertIn("root", pages[0].read_text(encoding="utf-8").lower())

    def test_report_honest_audit_sections(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            report = (Path(out) / "REPORT.md").read_text(encoding="utf-8")
            self.assertIn("Confidence Trail", report)
            self.assertIn("EXTRACTED", report)
            self.assertIn("INFERRED", report)
            self.assertIn("AMBIGUOUS", report)
            self.assertIn("Limits", report)
            self.assertIn("Token Benchmark", report)

    def test_index_entry_point(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            index = (Path(out) / "index.md").read_text(encoding="utf-8")
            self.assertIn("Reading Order", index)
            self.assertIn("Concept Wiki", index)
            self.assertIn("God Nodes", index)
            self.assertIn("Strongest Connections", index)
            self.assertIn("community_", index)

    def test_lint_healthy_after_generate(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(len(gen.lint(tmp)) > 0)
            gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            self.assertEqual(gen.lint(tmp), [])

    def test_deterministic_connections(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        resolved = [Edge("app.py", "utils.py", "resolved_imports", "EXTRACTED")]
        analysis = _make_analysis()
        with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
            out1 = gen.generate(nodes, [], resolved, analysis, {}, [], None, tmp1)
            out2 = gen.generate(nodes, [], resolved, analysis, {}, [], None, tmp2)
            raw1 = (Path(out1) / "connections.json").read_text(encoding="utf-8")
            raw2 = (Path(out2) / "connections.json").read_text(encoding="utf-8")
            self.assertEqual(raw1, raw2)

    def test_privacy_mode_strips_docs(self) -> None:
        config = Config(PRIVACY_MODE=True)
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            pages = sorted(Path(out).glob("community_*.md"))
            content = pages[0].read_text(encoding="utf-8")
            self.assertNotIn("App entry.", content)

    def test_leftover_files_covered_by_orphans_community(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes() + [_make_node("stray.py", symbols=[_make_symbol("lonely")])]
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            pages = sorted(Path(out).glob("community_*.md"))
            self.assertEqual(len(pages), 3)
            names = [p.name for p in pages]
            self.assertTrue(any("orphans" in name for name in names))
    def test_shared_context_link_for_disconnected_communities(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        analysis = _make_analysis()
        analysis.surprising_connections = []
        layers = {"app.py": "utility", "db.py": "utility", "utils.py": "utility"}
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, layers, [], None, tmp)
            data = json.loads((Path(out) / "connections.json").read_text(encoding="utf-8"))
            types = {d["connection_type"] for d in data}
            self.assertIn("shares_context", types)
            for entry in data:
                if entry["connection_type"] == "shares_context":
                    self.assertEqual(entry["confidence"], "INFERRED")

    def test_garbage_doc_filtered_from_definition(self) -> None:
        from readmenator._wiki import _is_garbage_doc
        self.assertTrue(_is_garbage_doc("-*- coding: utf-8 -*-"))
        self.assertTrue(_is_garbage_doc("# coding=utf-8"))
        self.assertTrue(_is_garbage_doc(""))
        self.assertFalse(_is_garbage_doc("Linker entry point."))

    def test_definition_names_core_file(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = [
            _make_node("tiny.py", doc="Tiny.", symbols=[_make_symbol("a")]),
            _make_node("core.py", doc="Core.", symbols=[
                _make_symbol("b"), _make_symbol("c"), _make_symbol("d"),
            ]),
        ]
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "root", {"tiny.py", "core.py"}, 1.0, 2),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=2, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            page = next(iter(sorted(Path(out).glob("community_*.md"))))
            content = page.read_text(encoding="utf-8")
            self.assertIn("Core file: `core.py` (3 symbols)", content)
            self.assertNotIn("coding", content)

    def test_duplicate_community_labels_disambiguated(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "cvm2", {"app.py"}, 1.0, 1),
                CommunityResult(1, "cvm2", {"db.py"}, 1.0, 1),
                CommunityResult(2, "other", {"utils.py"}, 1.0, 1),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=3, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            index = (Path(out) / "index.md").read_text(encoding="utf-8")
            self.assertIn("cvm2 (community 0)", index)
            self.assertIn("cvm2 (community 1)", index)

    def test_duplicate_god_basenames_disambiguated(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = [
            _make_node("a/tool.h", symbols=[_make_symbol("x")]),
            _make_node("b/tool.h", symbols=[_make_symbol("y")]),
        ]
        analysis = AnalysisResult(
            god_nodes=[("a/tool.h", 5.0), ("b/tool.h", 4.0)],
            communities=[CommunityResult(0, "root", {"a/tool.h", "b/tool.h"}, 1.0, 2)],
            surprising_connections=[], suggested_questions=[],
            node_count=2, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            index = (Path(out) / "index.md").read_text(encoding="utf-8")
            self.assertIn("`tool.h`", index)
            self.assertIn("`b/tool.h`", index)

    def test_oversized_community_grouped_by_directory(self) -> None:
        config = Config(WIKI_MAX_FILES_PER_PAGE=3)
        gen = WikiGenerator(config)
        nodes = [
            _make_node("src/a.py", symbols=[_make_symbol("a")]),
            _make_node("src/b.py", symbols=[_make_symbol("b")]),
            _make_node("lib/c.py", symbols=[_make_symbol("c")]),
            _make_node("lib/d.py", symbols=[_make_symbol("d")]),
        ]
        members = {"src/a.py", "src/b.py", "lib/c.py", "lib/d.py"}
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "root", members, 1.0, 4),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=4, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            page = next(iter(sorted(Path(out).glob("community_*.md"))))
            content = page.read_text(encoding="utf-8")
            self.assertIn("### `src` (2 files)", content)
            self.assertIn("more files in this community", content)

    def test_large_files_flagged_in_index_and_report(self) -> None:
        config = Config(WIKI_LARGE_FILE_KB=1)
        gen = WikiGenerator(config)
        with tempfile.TemporaryDirectory() as tmp:
            big = Path(tmp) / "gen.s"
            big.write_bytes(b"x" * 2048)
            nodes = [_make_node("gen.s", symbols=[_make_symbol("lbl")])]
            analysis = AnalysisResult(
                god_nodes=[("gen.s", 9.0)], communities=[
                    CommunityResult(0, "root", {"gen.s"}, 1.0, 1),
                ],
                surprising_connections=[], suggested_questions=[],
                node_count=1, edge_count=0,
            )
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            index = (Path(out) / "index.md").read_text(encoding="utf-8")
            report = (Path(out) / "REPORT.md").read_text(encoding="utf-8")
            self.assertIn("maybe generated", index)
            self.assertIn("gen.s", index)
            self.assertIn("Large files", report)

    def test_stale_pages_pruned_on_regenerate(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = _make_nodes()
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            stale = Path(out) / "community_99_stale.md"
            stale.write_text("# stale", encoding="utf-8")
            gen.generate(nodes, [], [], _make_analysis(), {}, [], None, tmp)
            self.assertFalse(stale.exists())
            self.assertTrue((Path(out) / "index.md").exists())

    def test_risks_carry_fix_hint_scope_and_closed_cycle(self) -> None:
        from readmenator._models import AnalysisResultV2, DependencyCycle, SecurityFinding
        config = Config()
        gen = WikiGenerator(config)
        nodes = [_make_node("app.py", doc="App.", symbols=[
            Symbol("login", "function", 5, "Login."),
        ])]
        findings = [SecurityFinding(
            "app.py", 9, "high", "PY005", "Hardcoded secret", "PW = 'x'", "CWE-798",
        )]
        analysis_v2 = AnalysisResultV2(
            taint=None,
            cycles=[DependencyCycle(cycle=["app.py", "db.py"], length=2)],
            change_impacts=[], hotspots=[], suggested_rules=[], layer_violations=[],
        )
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "root", {"app.py", "db.py"}, 1.0, 2),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=2, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, findings, analysis_v2, tmp)
            page = next(iter(sorted(Path(out).glob("community_*.md"))))
            content = page.read_text(encoding="utf-8")
            self.assertIn("(in `login`)", content)
            self.assertIn("Fix:", content)
            self.assertIn("`app.py` -> `db.py` -> `app.py`", content)

    def test_duplicate_symbol_scope_detected(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = [
            _make_node("a.py", symbols=[_make_symbol("run"), _make_symbol("stop"), _make_symbol("cfg"), _make_symbol("openx")]),
            _make_node("b.py", symbols=[_make_symbol("run"), _make_symbol("stop"), _make_symbol("cfg"), _make_symbol("other")]),
        ]
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "r", {"a.py"}, 1.0, 1),
                CommunityResult(1, "r", {"b.py"}, 1.0, 1),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=2, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            data = json.loads((Path(out) / "connections.json").read_text(encoding="utf-8"))
            dupes = [d for d in data if d["connection_type"] == "duplicates"]
            self.assertEqual(len(dupes), 1)
            self.assertEqual(dupes[0]["confidence"], "INFERRED")
            self.assertIn("consolidation", dupes[0]["explanation"])

    def test_no_duplicate_link_for_disjoint_scopes(self) -> None:
        config = Config()
        gen = WikiGenerator(config)
        nodes = [
            _make_node("a.py", symbols=[_make_symbol("aaa"), _make_symbol("aab")]),
            _make_node("b.py", symbols=[_make_symbol("bba"), _make_symbol("bbb")]),
        ]
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "r", {"a.py"}, 1.0, 1),
                CommunityResult(1, "r", {"b.py"}, 1.0, 1),
            ],
            surprising_connections=[], suggested_questions=[],
            node_count=2, edge_count=0,
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = gen.generate(nodes, [], [], analysis, {}, [], None, tmp)
            data = json.loads((Path(out) / "connections.json").read_text(encoding="utf-8"))
            self.assertFalse([d for d in data if d["connection_type"] == "duplicates"])

    def test_garbage_purpose_filtered(self) -> None:
        from readmenator._wiki import _is_garbage_purpose
        self.assertTrue(_is_garbage_purpose("SPDX-License-Identifier: GPL-2.0-or-later"))
        self.assertTrue(_is_garbage_purpose("=" * 40))
        self.assertTrue(_is_garbage_purpose("test_connection.c"))
        self.assertTrue(_is_garbage_purpose("==== VSL-DSP: Captura ===="))
        self.assertTrue(_is_garbage_purpose("vsl_config.h (VERSION CORREGIDA) " + "=" * 10))
        self.assertFalse(_is_garbage_purpose("VSL-DSP API - driver."))


if __name__ == "__main__":
    unittest.main()
