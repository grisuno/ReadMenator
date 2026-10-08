"""Contract tests for the interactive explorer modules.

Validates force-graph payloads and rendering, scan-text synthesis,
YARA-lite parsing and matching, provenance auditing, exclusion
filtering, analytics aggregation, explorer state, offline embedding
similarity, and the rebuild wiring into the maps directory.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from readmenator._analytics import AnalyticsBuilder
from readmenator._config import Config
from readmenator._embed import Embedder
from readmenator._exclusions import ExclusionList, parse_exclusions
from readmenator._explorer import build_state
from readmenator._exporter import GraphExporter
from readmenator._forcegraph import ForceGraphRenderer, family_color_from_name, node_value
from readmenator._models import (
    AnalysisResult,
    CommunityResult,
    Edge,
    Node,
    SecurityFinding,
    Symbol,
)
from readmenator._provenance import ProvenanceAuditor
from readmenator._scantext import ScanTextBuilder
from readmenator._yaralite import parse_yaralite_rules, run_yaralite_rules, validate_yaralite_rules


def _node(nid: str, symbols: int = 3) -> Node:
    """Build a file node with a fixed symbol count."""
    return Node(
        node_id=nid,
        label=nid.split("/")[-1],
        kind="module",
        language="py",
        doc="Purpose sentence.",
        symbols=[Symbol(name=f"sym{i}", kind="function", line=i + 1) for i in range(symbols)],
    )


class TestForceGraphContract(unittest.TestCase):
    """Contract: heterogeneous payload with stable colors and log2 sizing."""

    def setUp(self) -> None:
        """Initialise renderer and sample topology."""
        self.renderer = ForceGraphRenderer(Config())
        self.nodes = [_node("a.py", 4), _node("b.py", 1)]
        self.edges = [Edge(source="a.py", target="b.py", relation="imports", confidence="EXTRACTED")]

    def test_family_color_is_deterministic(self) -> None:
        """Identical labels hash to identical colors."""
        self.assertEqual(family_color_from_name("core"), family_color_from_name("core"))
        self.assertNotEqual(family_color_from_name("core"), family_color_from_name("zzz-other"))

    def test_node_value_dampens_large_files(self) -> None:
        """Log2 sizing keeps large files from dominating."""
        small = node_value(1, 1)
        large = node_value(500, 200)
        self.assertGreaterEqual(small, 1.0)
        self.assertLess(large, 12.0)
        self.assertGreater(large, small)

    def test_build_payload_has_heterogeneous_nodes(self) -> None:
        """Payload contains file, layer, and edge entries."""
        payload = self.renderer.build_payload(self.nodes, self.edges)
        types = {node["type"] for node in payload["nodes"]}
        self.assertIn("file", types)
        self.assertIn("layer", types)
        self.assertTrue(payload["edges"])

    def test_build_payload_maps_communities(self) -> None:
        """Community membership stamps family and member edges."""
        analysis = AnalysisResult(
            god_nodes=[], communities=[CommunityResult(0, "core", ["a.py"], 1.0, 1)],
            surprising_connections=[], suggested_questions=[],
            node_count=2, edge_count=1,
        )
        payload = self.renderer.build_payload(self.nodes, self.edges, analysis=analysis)
        families = [node.get("family") for node in payload["nodes"] if node["type"] == "file"]
        self.assertIn("core", families)
        self.assertTrue(any(edge["type"] == "member_of" for edge in payload["edges"]))

    def test_render_produces_standalone_html(self) -> None:
        """Rendered HTML embeds local vendor ref, data, and hull code."""
        payload = self.renderer.build_payload(self.nodes, self.edges)
        html = self.renderer.render(payload, {"attribution_funnel": {}})
        self.assertIn("vendor/force-graph.min.js", html)
        self.assertIn("convexHull", html)
        self.assertIn("linkDirectionalParticles", html)
        self.assertIn("Maps gallery", html)
        self.assertIn("engine-error", html)
        self.assertNotIn("__TITLE__", html)
        self.assertNotIn("__DATA__", html)

    def test_render_uses_supported_cdn_fallback(self) -> None:
        """The 2D fallback URL points at an existing package release."""
        html = self.renderer.render({"nodes": [], "edges": []})
        self.assertIn("cdn.jsdelivr.net/npm/force-graph@1/", html)
        self.assertNotIn("force-graph@1.73.4", html)

    def test_write_copies_vendor_engine(self) -> None:
        """write() emits HTML plus the vendored engine beside it."""
        import tempfile
        from pathlib import Path

        payload = self.renderer.build_payload(self.nodes, self.edges)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "maps" / "graph-force.html"
            content = self.renderer.write(str(target), payload)
            self.assertTrue(target.is_file())
            vendor = Path(tmp) / "maps" / "vendor" / "force-graph.min.js"
            self.assertTrue(vendor.is_file())
            self.assertIn("ForceGraph", vendor.read_text(encoding="utf-8")[:500])
            self.assertIn("force-graph", content)

    def test_exporter_delegates_to_forcegraph(self) -> None:
        """GraphExporter.to_forcegraph returns the explorer document."""
        html = GraphExporter(Config()).to_forcegraph(self.nodes, self.edges)
        self.assertIn("force-graph", html)


class TestScanTextContract(unittest.TestCase):
    """Contract: scan-text blob carries names, symbols, and imports."""

    def test_build_for_node_includes_sections(self) -> None:
        """Blob contains file, symbol, import, and content sections."""
        builder = ScanTextBuilder(Config())
        node = _node("pkg/mod.py", 2)
        text = builder.build_for_node(node, content="import os\neval(x)", imports=["os"])
        self.assertIn("pkg/mod.py", text)
        self.assertIn("sym0", text)
        self.assertIn("imports:", text)
        self.assertIn("eval(x)", text)

    def test_build_corpus_maps_every_node(self) -> None:
        """Corpus build returns one blob per node."""
        builder = ScanTextBuilder(Config())
        result = builder.build_corpus(self_nodes(), {"a.py": "x = 1"}, [])
        self.assertEqual(set(result), {"a.py", "b.py"})


def self_nodes() -> list:
    """Return two sample nodes for scan-text tests."""
    return [_node("a.py", 1), _node("b.py", 1)]


class TestYaraLiteContract(unittest.TestCase):
    """Contract: zero-dep YARA-lite parses tiers and matches text."""

    RULES = """rule T1-Test-Rule {
  meta:
    description = "test rule"
    tier = "T1"
    confidence = "high"
  strings:
    $a = "eval(" nocase
    $b = "exec(" nocase
  condition:
    any of them
}
rule T2-Cooccur {
  meta:
    description = "cooccur"
    tier = "T2"
  strings:
    $a = "subprocess" nocase
    $b = "socket" nocase
  condition:
    2 of ($a, $b)
}
"""

    def test_parse_reports_tiers(self) -> None:
        """Parser extracts both rules with correct tiers."""
        rules, errors = parse_yaralite_rules(self.RULES)
        self.assertEqual(errors, [])
        self.assertEqual([rule.tier for rule in rules], ["T1", "T2"])

    def test_run_matches_any_of_them(self) -> None:
        """Any-of condition fires on a single primitive."""
        rules, _ = parse_yaralite_rules(self.RULES)
        matches = run_yaralite_rules("x = eval(y)", rules)
        self.assertEqual([match.rule for match in matches], ["T1-Test-Rule"])

    def test_run_requires_cooccurrence(self) -> None:
        """Two-of condition needs both signals."""
        rules, _ = parse_yaralite_rules(self.RULES)
        self.assertEqual(run_yaralite_rules("import subprocess", rules), [])
        matches = run_yaralite_rules("import subprocess\nimport socket", rules)
        self.assertEqual(len(matches), 1)

    def test_validate_counts_rules(self) -> None:
        """Validation reports counts and tier breakdown."""
        report = validate_yaralite_rules(self.RULES)
        self.assertTrue(report["valid"])
        self.assertEqual(report["rule_count"], 2)
        self.assertEqual(report["tiers"]["T1"], 1)


class TestProvenanceContract(unittest.TestCase):
    """Contract: findings split into static versus inferred-only."""

    def test_audit_flags_snippetless_findings(self) -> None:
        """Findings without snippets are inferred-only."""
        auditor = ProvenanceAuditor(Config())
        findings = [
            SecurityFinding("a.py", 1, "high", "R1", "desc", "eval(x)", "CWE-95"),
            SecurityFinding("b.py", 2, "low", "R2", "desc", "", "CWE-1"),
        ]
        result = auditor.audit(findings)
        by_file = {item.file_path: item for item in result}
        self.assertEqual(by_file["a.py"].provenance, "static")
        self.assertTrue(by_file["b.py"].is_inferred_only)

    def test_summary_counts_classes(self) -> None:
        """Summary reports static and inferred-only counts."""
        auditor = ProvenanceAuditor(Config())
        findings = [SecurityFinding("b.py", 2, "low", "R2", "desc", "", "CWE-1")]
        summary = auditor.summary(auditor.audit(findings))
        self.assertEqual(summary["inferred_only"], 1)


class TestExclusionsContract(unittest.TestCase):
    """Contract: blocklist suppresses known-clean findings."""

    def test_parse_and_match_glob(self) -> None:
        """Glob patterns match paths with rule scoping."""
        entries = parse_exclusions("exclusions:\n  - pattern: \"tests/*\"\n    rule_id: \"*\"\n")
        self.assertTrue(entries[0].matches("tests/a.py", "R1"))
        self.assertFalse(entries[0].matches("src/a.py", "R1"))

    def test_filter_findings_removes_excluded(self) -> None:
        """Excluded findings are removed from the list."""
        exclusions = ExclusionList(Config())
        exclusions._entries = parse_exclusions("exclusions:\n  - pattern: \"tests/*\"\n    rule_id: \"*\"\n")
        findings = [
            SecurityFinding("tests/a.py", 1, "high", "R1", "d", "s", "CWE-1"),
            SecurityFinding("src/a.py", 1, "high", "R1", "d", "s", "CWE-1"),
        ]
        self.assertEqual(len(exclusions.filter_findings(findings)), 1)


class TestAnalyticsContract(unittest.TestCase):
    """Contract: analytics payload carries funnel and distributions."""

    def test_build_has_all_sections(self) -> None:
        """Payload includes funnel, layers, languages, and scatter."""
        builder = AnalyticsBuilder(Config())
        payload = builder.build(
            [_node("a.py", 5), _node("b.py", 0)],
            [Edge(source="a.py", target="b.py", relation="imports", confidence="EXTRACTED")],
            [],
            None,
            [SecurityFinding("a.py", 1, "high", "R1", "d", "s", "CWE-1")],
            {"a.py": "core", "b.py": "core"},
        )
        self.assertEqual(payload["attribution_funnel"]["total"], 2)
        self.assertTrue(payload["layer_distribution"])
        self.assertTrue(payload["language_distribution"])
        self.assertTrue(payload["sample_scatter"])
        self.assertTrue(payload["rule_yield"])


class TestExplorerContract(unittest.TestCase):
    """Contract: explorer state precomputes graph and analytics."""

    def test_build_state_serves_apis(self) -> None:
        """State exposes graph, analytics, samples, and HTML."""
        state = build_state(
            Config(), [_node("a.py", 2)],
            [Edge(source="a.py", target="os", relation="imports", confidence="EXTRACTED")],
        )
        self.assertTrue(state.graph["nodes"])
        self.assertIn("attribution_funnel", state.analytics)
        self.assertTrue(state.samples())
        self.assertIn("force-graph", state.html)


class TestEmbedContract(unittest.TestCase):
    """Contract: offline similarity ranks related files first."""

    def test_near_jaccard_prefers_shared_terms(self) -> None:
        """Files sharing tokens rank above unrelated files."""
        embedder = Embedder(Config())
        corpus = {
            "a.py": "import subprocess socket eval shell",
            "b.py": "import subprocess socket shell exec",
            "c.py": "def render_template html css layout",
        }
        neighbors = embedder.near_jaccard("a.py", corpus, top_k=2)
        self.assertEqual(neighbors[0]["file"], "b.py")

    def test_cluster_groups_similar_files(self) -> None:
        """Near-duplicate files land in one cluster."""
        embedder = Embedder(Config())
        corpus = {
            "a.py": "import subprocess socket shell eval exec alpha",
            "b.py": "import subprocess socket shell eval exec extra",
            "b2.py": "import subprocess socket shell eval exec gamma",
            "c.py": "def render_template html css layout margin",
        }
        clusters = embedder.cluster_jaccard(corpus, threshold=0.05)
        self.assertTrue(any(set(cluster) >= {"a.py", "b.py"} for cluster in clusters))


class TestRebuildContract(unittest.TestCase):
    """Contract: run()/rebuild() writes the explorer into the maps directory."""

    def _run_app(self, tmp: str) -> None:
        """Run the application with heavy sidecars disabled."""
        from readmenator._app import readmenatorApplication

        app = readmenatorApplication(
            Config(
                DIAGRAM_ENABLED=False,
                WIKI_ENABLED=False,
                AGENT_OUTPUT_ENABLED=False,
                VIDEO_ENABLED=False,
                GH_WIKI_ENABLED=False,
            )
        )
        app.run(tmp)

    def test_run_writes_forcegraph_html(self) -> None:
        """The --rebuild path emits maps/graph-force.html plus vendor."""
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.py").write_text("import os\n", encoding="utf-8")
            Path(tmp, "b.py").write_text("import a\n", encoding="utf-8")
            self._run_app(tmp)
            output = Path(tmp) / "readmenator-maps" / Config.FORCEGRAPH_OUTPUT
            self.assertTrue(output.is_file())
            self.assertIn("vendor/force-graph.min.js", output.read_text(encoding="utf-8"))
            vendor = Path(tmp) / "readmenator-maps" / "vendor" / "force-graph.min.js"
            self.assertTrue(vendor.is_file())

    def test_run_skips_forcegraph_when_disabled(self) -> None:
        """FORCEGRAPH_ENABLED=False leaves no explorer HTML behind."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.py").write_text("import os\n", encoding="utf-8")
            app = readmenatorApplication(
                Config(
                    FORCEGRAPH_ENABLED=False,
                    DIAGRAM_ENABLED=False,
                    WIKI_ENABLED=False,
                    AGENT_OUTPUT_ENABLED=False,
                    VIDEO_ENABLED=False,
                    GH_WIKI_ENABLED=False,
                )
            )
            app.run(tmp)
            self.assertFalse(
                (Path(tmp) / "readmenator-maps" / Config.FORCEGRAPH_OUTPUT).exists()
            )


class TestGalleryCardContract(unittest.TestCase):
    """Contract: the maps gallery index links the force-graph page."""

    def test_publish_appends_extra_card(self) -> None:
        """Extra cards render with gallery styling and relative links."""
        from readmenator._diagrams import DocsSitePublisher

        publisher = DocsSitePublisher(Config())
        html = publisher.render_index(
            "demo",
            {},
            {"files": 2},
            None,
            None,
            [],
            None,
            extra_cards=[
                {
                    "kind": "forcegraph",
                    "title": "Force Graph",
                    "href": "graph-force.html",
                    "description": "Physics-driven explorer.",
                    "meta": "9 nodes | 10 edges",
                }
            ],
        )
        self.assertIn('href="graph-force.html"', html)
        self.assertIn("Force Graph", html)
        self.assertIn("9 nodes | 10 edges", html)

    def test_export_diagrams_writes_forcegraph_and_card(self) -> None:
        """export_diagrams emits the page, vendor lib, and gallery card."""
        from readmenator._app import readmenatorApplication

        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.py").write_text("import os\n", encoding="utf-8")
            Path(tmp, "b.py").write_text("import a\n", encoding="utf-8")
            app = readmenatorApplication(
                Config(
                    WIKI_ENABLED=False,
                    AGENT_OUTPUT_ENABLED=False,
                    VIDEO_ENABLED=False,
                    GH_WIKI_ENABLED=False,
                )
            )
            app.export_diagrams(tmp)
            maps_dir = Path(tmp) / "readmenator-maps"
            self.assertTrue((maps_dir / "graph-force.html").is_file())
            self.assertTrue((maps_dir / "vendor" / "force-graph.min.js").is_file())
            index = (maps_dir / "index.html").read_text(encoding="utf-8")
            self.assertIn("graph-force.html", index)


if __name__ == "__main__":
    unittest.main()
