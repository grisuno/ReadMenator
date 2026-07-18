from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._documentation import DocumentationGenerator
from readmenator._models import (
    AnalysisResultV2,
    Edge,
    Node,
    Symbol,
    TaintAnalysisResult,
    TaintPath,
)


class TestDocumentationGeneratorContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()
        self.generator = DocumentationGenerator(self.config)

    def test_contains_header(self) -> None:
        content = self.generator.generate([], [])
        self.assertIn("# Polyglot Codebase Knowledge Graph", content)

    def test_contains_metadata_line(self) -> None:
        content = self.generator.generate([], [])
        self.assertIn("Total Files Parsed:", content)
        self.assertIn("Total Symbols Extracted:", content)
        self.assertIn("Total Imports:", content)

    def test_contains_mermaid_block(self) -> None:
        content = self.generator.generate([], [])
        self.assertIn("```mermaid", content)
        self.assertIn("```", content.split("```mermaid")[1])

    def test_contains_architecture_reference(self) -> None:
        content = self.generator.generate([], [])
        self.assertIn("## Architecture Reference", content)

    def test_contains_cpg_block(self) -> None:
        content = self.generator.generate([], [])
        self.assertIn("## Code Property Graph", content)
        self.assertIn("@context", content)

    def test_contains_statistics_dashboard(self) -> None:
        content = self.generator.generate([], [])
        self.assertIn("## Statistics Dashboard", content)
        self.assertIn("Total Files", content)

    def test_groups_files_by_language(self) -> None:
        py_node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            doc="",
        )
        rs_node = Node(
            node_id="lib.rs",
            label="lib.rs",
            kind="module",
            language="rs",
            doc="",
        )
        content = self.generator.generate([py_node, rs_node], [])
        self.assertIn("### PY", content)
        self.assertIn("### RS", content)

    def test_lists_symbols_under_file(self) -> None:
        sym = Symbol(name="hello", kind="function", line=42)
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            symbols=[sym],
        )
        content = self.generator.generate([node], [])
        self.assertIn("hello", content)
        self.assertIn("(line 42)", content)

    def test_class_symbol_is_pluralized_correctly(self) -> None:
        sym = Symbol(name="MyClass", kind="class", line=10)
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            symbols=[sym],
        )
        content = self.generator.generate([node], [])
        self.assertIn("**Classes:**", content)
        self.assertNotIn("**Classs:**", content)
        self.assertNotIn("classs", content.lower())

    def test_function_pluralization(self) -> None:
        sym = Symbol(name="helper", kind="function", line=1)
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            symbols=[sym],
        )
        content = self.generator.generate([node], [])
        self.assertIn("**Functions:**", content)

    def test_method_pluralization(self) -> None:
        sym = Symbol(name="doStuff", kind="method", line=5)
        node = Node(
            node_id="test.java",
            label="test.java",
            kind="module",
            language="java",
            symbols=[sym],
        )
        content = self.generator.generate([node], [])
        self.assertIn("**Methods:**", content)

    def test_shows_no_symbols_for_empty_files(self) -> None:
        node = Node(
            node_id="empty.py",
            label="empty.py",
            kind="module",
            language="py",
            doc="",
        )
        content = self.generator.generate([node], [])
        self.assertIn("No symbols extracted", content)

    def test_includes_file_path(self) -> None:
        node = Node(
            node_id="src/main.py",
            label="main.py",
            kind="module",
            language="py",
            doc="",
        )
        content = self.generator.generate([node], [])
        self.assertIn("**Path:** `src/main.py`", content)

    def test_docstring_in_output(self) -> None:
        sym = Symbol(name="greet", kind="function", line=3, doc="Says hello")
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            symbols=[sym],
        )
        content = self.generator.generate([node], [])
        self.assertIn("*Says hello*", content)

    def test_truncation_note_when_limited(self) -> None:
        small_cfg = Config(MERMAID_MAX_NODES=2)
        generator = DocumentationGenerator(small_cfg)
        nodes = [
            Node(node_id=f"f{i}.py", label=f"f{i}.py", kind="module", language="py", doc="")
            for i in range(10)
        ]
        content = generator.generate(nodes, [])
        self.assertIn("intelligently pruned", content)

    def test_taint_propagation_section_present(self) -> None:
        taint = TaintAnalysisResult(
            paths=[
                TaintPath(
                    source_file="a.py",
                    sink_file="c.py",
                    path=["a.py", "b.py", "c.py"],
                    hops=2,
                    dangerous_import="subprocess",
                    severity="high",
                )
            ],
            source_count=1,
            sink_count=1,
        )
        analysis_v2 = AnalysisResultV2(taint=taint)
        content = self.generator.generate([], [], analysis_v2=analysis_v2)
        self.assertIn("## Taint Propagation Map", content)
        self.assertIn("subprocess", content)

    def test_hotspot_section_present(self) -> None:
        from readmenator._models import HotspotResult

        analysis_v2 = AnalysisResultV2(
            hotspots=[
                HotspotResult(
                    file_id="main.py",
                    complexity_score=0.8,
                    centrality_score=0.5,
                    combined_score=0.65,
                    symbol_count=10,
                    connection_count=5,
                )
            ]
        )
        content = self.generator.generate([], [], analysis_v2=analysis_v2)
        self.assertIn("## Hotspot Analysis", content)

    def test_no_taint_section_when_empty(self) -> None:
        content = self.generator.generate([], [])
        self.assertNotIn("## Taint Propagation Map", content)

    def test_no_hotspot_section_when_empty(self) -> None:
        content = self.generator.generate([], [])
        self.assertNotIn("## Hotspot Analysis", content)

    def test_cpg_block_disabled_via_config(self) -> None:
        cfg = Config(CPG_ENABLED=False)
        generator = DocumentationGenerator(cfg)
        content = generator.generate([], [])
        self.assertNotIn("## Code Property Graph", content)

    def test_architectural_layers_section(self) -> None:
        layers = {"main.py": "testing"}
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
        )
        content = self.generator.generate([node], [], layers=layers)
        self.assertIn("## Architectural Layers", content)
        self.assertIn("testing", content)

    def test_security_findings_section(self) -> None:
        from readmenator._models import SecurityFinding

        findings = [
            SecurityFinding(
                file_path="main.py",
                line=10,
                severity="critical",
                rule_id="TEST001",
                description="Eval detected",
                snippet="eval(x)",
                cwe="CWE-95",
            )
        ]
        content = self.generator.generate([], [], findings=findings)
        self.assertIn("## Security Audit", content)
        self.assertIn("Critical", content)
        self.assertIn("eval(x)", content)

    # ------------------------------------------------------------------
    # Context budget tests
    # ------------------------------------------------------------------

    def test_context_budget_zero_returns_full_content(self) -> None:
        cfg = Config(CONTEXT_BUDGET=0)
        generator = DocumentationGenerator(cfg)
        node = Node(node_id="main.py", label="main.py", kind="module", language="py")
        content = generator.generate([node], [])
        self.assertIn("# Polyglot Codebase Knowledge Graph", content)
        self.assertIn("## Architecture Reference", content)

    def test_context_budget_returns_compact_summary(self) -> None:
        cfg = Config(CONTEXT_BUDGET=200)
        generator = DocumentationGenerator(cfg)
        node = Node(node_id="main.py", label="main.py", kind="module", language="py")
        content = generator.generate([node], [])
        self.assertIn("# Knowledge Base Summary", content)
        self.assertIn("Files:", content)

    def test_context_budget_prioritizes_god_nodes(self) -> None:
        cfg = Config(CONTEXT_BUDGET=500)
        generator = DocumentationGenerator(cfg)
        from readmenator._models import AnalysisResult
        node = Node(node_id="core.py", label="core.py", kind="module", language="py",
                     symbols=[Symbol(name="run", kind="function", line=1)])
        analysis = AnalysisResult(
            god_nodes=[("core.py", 15.5)],
            communities=[],
            surprising_connections=[],
            suggested_questions=[],
            node_count=1,
            edge_count=0,
        )
        content = generator.generate([node], [], analysis=analysis)
        self.assertIn("core.py", content)

    def test_context_budget_truncates_at_limit(self) -> None:
        cfg = Config(CONTEXT_BUDGET=50)
        generator = DocumentationGenerator(cfg)
        node = Node(node_id="long.py", label="long.py", kind="module", language="py",
                     symbols=[Symbol(name="x", kind="function", line=1)])
        content = generator.generate([node], [])
        self.assertIn("truncated", content)

    def test_context_budget_includes_security_findings(self) -> None:
        cfg = Config(CONTEXT_BUDGET=1000)
        generator = DocumentationGenerator(cfg)
        from readmenator._models import SecurityFinding
        findings = [
            SecurityFinding(
                file_path="danger.py",
                line=5,
                severity="critical",
                rule_id="SEC001",
                description="Hardcoded secret",
                snippet="password = '1234'",
                cwe="CWE-798",
            )
        ]
        content = generator.generate([], [], findings=findings)
        self.assertIn("Security Findings:", content)
