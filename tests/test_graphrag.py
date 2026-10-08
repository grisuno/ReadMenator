"""Contract tests for the zero-token GraphRAG index and retrieval."""

from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from readmenator._config import Config
from readmenator._graphrag import (
    Bm25Index,
    GraphRagBuilder,
    GraphRagIndex,
    GraphRagSearcher,
    GraphRagStore,
    tokenize,
)
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    CommunityResult,
    DependencyCycle,
    Edge,
    Node,
    SecurityFinding,
    Symbol,
)


def _fixture():
    """Return a small two-community project with symbols, calls, and findings."""
    nodes = [
        Node("core/rank.py", "rank.py", "module", "py", "PageRank scoring for graphs.", [
            Symbol("PageRanker", "class", 3, "Rank nodes by random walks.", "class PageRanker"),
            Symbol("personalized", "function", 20, "Personalized PageRank from seeds.", "def personalized(seeds)"),
        ]),
        Node("core/graph.py", "graph.py", "module", "py", "Graph container.", [
            Symbol("Graph", "class", 1, "Directed graph.", "class Graph"),
        ]),
        Node("web/server.py", "server.py", "module", "py", "HTTP server for the explorer.", [
            Symbol("serve", "function", 5, "Start the HTTP server.", "def serve(port)"),
        ]),
        Node("web/views.py", "views.py", "module", "py", "Rendered views.", [
            Symbol("render", "function", 2, "Render a page.", "def render(name)"),
        ]),
    ]
    edges = [
        Edge("core/rank.py", "core/graph.py", "imports"),
        Edge("web/server.py", "subprocess", "imports"),
        Edge("core/rank.py::personalized", "core/rank.py::PageRanker", "calls"),
        Edge("web/server.py", "render", "calls"),
    ]
    resolved = [
        Edge("core/rank.py", "core/graph.py", "resolved_imports"),
        Edge("web/server.py", "web/views.py", "resolved_imports"),
        Edge("web/views.py", "core/rank.py", "resolved_imports"),
    ]
    analysis = AnalysisResult(
        god_nodes=[("core/rank.py", 5.0)],
        communities=[
            CommunityResult(0, "core", {"core/rank.py", "core/graph.py"}, 1.0, 2),
            CommunityResult(1, "web", {"web/server.py", "web/views.py"}, 0.5, 2),
        ],
        surprising_connections=[], suggested_questions=[], node_count=4, edge_count=3,
    )
    findings = [SecurityFinding("web/server.py", 6, "high", "PY-CMD", "Command injection", "os.system(x)", "CWE-78")]
    v2 = AnalysisResultV2(cycles=[DependencyCycle(["web/server.py", "web/views.py"], 2)])
    content = {
        "core/rank.py": "\n".join(f"line {i}" for i in range(1, 40)),
        "core/graph.py": "class Graph:\n    pass\n",
        "web/server.py": "import subprocess\n\n\n\ndef serve(port):\n    os.system(port)\n",
        "web/views.py": "\ndef render(name):\n    return name\n",
    }
    return nodes, edges, resolved, analysis, findings, v2, content


class TestGraphRagIndexContract(unittest.TestCase):
    """Contract: typed entities, relationships, text units, and report hierarchy."""

    def setUp(self) -> None:
        """Build the index once per test."""
        self.config = Config()
        nodes, edges, resolved, analysis, findings, v2, content = _fixture()
        self.inputs = (nodes, edges, resolved, analysis, {"core/rank.py": "business_logic"}, findings, v2, None, content)
        self.index = GraphRagBuilder(self.config).build(*self.inputs)

    def test_graphrag_entities_cover_files_symbols_externals(self) -> None:
        """Every file and symbol becomes an entity; external imports too."""
        kinds = {e.kind for e in self.index.entities}
        self.assertTrue({"file", "class", "function", "external"} <= kinds)
        ids = {e.entity_id for e in self.index.entities}
        self.assertIn("file:core/rank.py", ids)
        self.assertIn("ext:subprocess", ids)

    def test_graphrag_relationships_are_typed(self) -> None:
        """Defines, resolved imports, calls, and external imports are all present."""
        relations = {r.relation for r in self.index.relationships}
        self.assertTrue({"defines", "resolved_imports", "calls", "imports"} <= relations)
        calls = [r for r in self.index.relationships if r.relation == "calls"]
        self.assertTrue(any(r.target.endswith("::render@2") for r in calls))

    def test_graphrag_report_hierarchy_has_root(self) -> None:
        """Level-0 community reports and one root report exist; root covers every file."""
        levels = sorted({c.level for c in self.index.communities})
        self.assertIn(0, levels)
        self.assertIn(2, levels)
        root = [c for c in self.index.communities if c.community_id == "root"][0]
        self.assertEqual(len(root.file_ids), 4)

    def test_graphrag_reports_are_extractive_and_rated(self) -> None:
        """Reports cite measured facts: security, cycles, and a bounded rating."""
        web = [c for c in self.index.communities if c.title == "web"][0]
        joined = " ".join(web.findings)
        self.assertIn("Security", joined)
        self.assertIn("cycle", joined.lower())
        self.assertTrue(0.0 <= web.rating <= 10.0)
        self.assertIn("Rating", web.rating_explanation)

    def test_graphrag_text_units_use_source_spans(self) -> None:
        """Text units carry source excerpts bounded by the next symbol."""
        unit = [u for u in self.index.text_units if u.entity_id.endswith("PageRanker@3")][0]
        self.assertEqual(unit.start_line, 3)
        self.assertEqual(unit.end_line, 19)
        self.assertIn("line 3", unit.text)

    def test_graphrag_text_units_respect_max_lines(self) -> None:
        """No text unit spans more than GRAPHRAG_TEXT_UNIT_MAX_LINES lines."""
        for unit in self.index.text_units:
            self.assertLessEqual(unit.end_line - unit.start_line + 1, self.config.GRAPHRAG_TEXT_UNIT_MAX_LINES)

    def test_graphrag_privacy_mode_strips_sources_and_docs(self) -> None:
        """Privacy mode never leaks source text or docstrings."""
        private = GraphRagBuilder(replace(self.config, PRIVACY_MODE=True)).build(*self.inputs)
        for unit in private.text_units:
            self.assertNotIn("os.system", unit.text)
            self.assertNotIn("random walks", unit.text)
        for entity in private.entities:
            self.assertNotIn("random walks", entity.description)

    def test_graphrag_disabled_returns_empty_index(self) -> None:
        """GRAPHRAG_ENABLED=False yields an empty index."""
        empty = GraphRagBuilder(replace(self.config, GRAPHRAG_ENABLED=False)).build(*self.inputs)
        self.assertEqual(empty.entities, [])
        self.assertFalse(empty.meta["enabled"])

    def test_graphrag_build_is_deterministic(self) -> None:
        """Identical input yields byte-identical serialisation."""
        again = GraphRagBuilder(self.config).build(*self.inputs)
        self.assertEqual(json.dumps(self.index.to_dict(), sort_keys=True), json.dumps(again.to_dict(), sort_keys=True))

    def test_graphrag_roundtrip_dict(self) -> None:
        """from_dict(to_dict()) preserves the index."""
        clone = GraphRagIndex.from_dict(json.loads(json.dumps(self.index.to_dict())))
        self.assertEqual(clone.to_dict(), self.index.to_dict())


class TestGraphRagSearchContract(unittest.TestCase):
    """Contract: local PPR retrieval, global map-reduce, auto routing, budgets."""

    def setUp(self) -> None:
        """Build the searcher once per test."""
        self.config = Config()
        nodes, edges, resolved, analysis, findings, v2, content = _fixture()
        index = GraphRagBuilder(self.config).build(nodes, edges, resolved, analysis, {}, findings, v2, None, content)
        self.searcher = GraphRagSearcher(self.config, index)

    def test_graphrag_local_search_ranks_matching_symbol(self) -> None:
        """A symbol query puts that symbol among the top entities."""
        context = self.searcher.local_search("personalized pagerank seeds")
        self.assertEqual(context.mode, "local")
        top_ids = [eid for eid, _ in context.entities[:3]]
        self.assertTrue(any("personalized" in eid for eid in top_ids))
        self.assertIn("## Entities", context.markdown)

    def test_graphrag_local_search_expands_through_graph(self) -> None:
        """PPR pulls in graph neighbours that do not match the query text."""
        context = self.searcher.local_search("PageRanker")
        ids = {eid for eid, _ in context.entities}
        self.assertIn("file:core/rank.py", ids)

    def test_graphrag_global_search_uses_reports(self) -> None:
        """Global mode answers from community reports."""
        context = self.searcher.global_search("security risks overview")
        self.assertEqual(context.mode, "global")
        self.assertIn("## Overview", context.markdown)
        self.assertTrue(context.reports)

    def test_graphrag_auto_routes_broad_questions_global(self) -> None:
        """Broad questions go global; specific names go local."""
        self.assertEqual(self.searcher.choose_mode("give me the architecture overview"), "global")
        self.assertEqual(self.searcher.choose_mode("render"), "local")

    def test_graphrag_no_match_falls_back_global(self) -> None:
        """Queries with no entity hit are routed to global mode."""
        self.assertEqual(self.searcher.choose_mode("zzzqqq"), "global")

    def test_graphrag_budget_never_emits_empty_sections(self) -> None:
        """Every emitted heading is followed by at least one item."""
        context = self.searcher.search("personalized", "local", budget_tokens=80)
        lines = context.markdown.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("## "):
                self.assertTrue(i + 1 < len(lines) and lines[i + 1].strip())

    def test_graphrag_budget_bounds_markdown(self) -> None:
        """The packed context respects the token budget."""
        context = self.searcher.search("personalized", "local", budget_tokens=60)
        self.assertLessEqual(len(context.markdown), 60 * self.config.AGENT_CHARS_PER_TOKEN + 1)


class TestGraphRagStoreContract(unittest.TestCase):
    """Contract: persisted JSON, JSONL tables, and REPORTS.md load back."""

    def test_graphrag_store_writes_and_loads(self) -> None:
        """write() emits tables and load() restores the same index."""
        config = Config()
        nodes, edges, resolved, analysis, findings, v2, content = _fixture()
        index = GraphRagBuilder(config).build(nodes, edges, resolved, analysis, {}, findings, v2, None, content)
        store = GraphRagStore(config)
        with tempfile.TemporaryDirectory() as tmp:
            written = store.write(index, tmp)
            names = {p.name for p in written}
            self.assertTrue({"index.json", "entities.jsonl", "relationships.jsonl", "REPORTS.md"} <= names)
            loaded = store.load(tmp)
            self.assertIsNotNone(loaded)
            self.assertEqual(loaded.to_dict(), index.to_dict())
            self.assertIn("# GraphRAG Community Reports", (Path(tmp) / config.GRAPHRAG_OUTPUT_DIR / "REPORTS.md").read_text())

    def test_graphrag_store_rejects_wrong_schema(self) -> None:
        """A mismatched schema version loads as None."""
        config = Config()
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / config.GRAPHRAG_OUTPUT_DIR
            out.mkdir()
            (out / "index.json").write_text(json.dumps({"meta": {"schema_version": -1}}))
            self.assertIsNone(GraphRagStore(config).load(tmp))


class TestGraphRagPrimitives(unittest.TestCase):
    """Contract: tokenizer and BM25 behave like their textbook definitions."""

    def test_graphrag_tokenize_splits_camel_and_keeps_whole(self) -> None:
        """camelCase identifiers split and keep the joined form."""
        tokens = tokenize("PersonalizedPageRank", 2, set())
        self.assertIn("personalizedpagerank", tokens)
        self.assertIn("page", tokens)

    def test_graphrag_bm25_prefers_rare_terms(self) -> None:
        """Documents containing the rarer query term score higher."""
        bm25 = Bm25Index([["graph", "rank"], ["graph"], ["graph", "server"]], 1.2, 0.75)
        scores = bm25.scores(["rank"])
        self.assertGreater(scores[0], scores[1])
        self.assertEqual(scores[1], 0.0)


if __name__ == "__main__":
    unittest.main()
