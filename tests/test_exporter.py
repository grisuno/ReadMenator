"""Contract tests for the GraphExporter.

Validates JSON, HTML, and SVG export formats with various node/edge
configurations and analysis metadata.
"""

from __future__ import annotations

import json
import unittest

from readmenator._config import Config
from readmenator._exporter import GraphExporter
from readmenator._models import (
    AnalysisResult,
    CommunityResult,
    Edge,
    Node,
    Symbol,
)


class TestGraphExporterContract(unittest.TestCase):
    """Contract: GraphExporter produces valid JSON, HTML, and SVG outputs."""

    def setUp(self) -> None:
        self.config = Config()
        self.exporter = GraphExporter(self.config)

    def _make_node(
        self, nid: str, label: str, lang: str = "py",
        symbols: list | None = None,
    ) -> Node:
        return Node(
            node_id=nid,
            label=label,
            kind="module",
            language=lang,
            symbols=symbols or [],
        )

    def _make_sym(
        self, name: str, kind: str = "class", line: int = 1,
    ) -> Symbol:
        return Symbol(name=name, kind=kind, line=line)

    def test_to_json_produces_valid_json(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        result = self.exporter.to_json(nodes, edges)
        data = json.loads(result)
        self.assertIn("nodes", data)
        self.assertIn("edges", data)
        self.assertIn("metadata", data)

    def test_to_json_includes_symbol_data(self) -> None:
        sym = self._make_sym("MyClass", "class", 42)
        nodes = [self._make_node("main.py", "main.py", symbols=[sym])]
        edges: list = []
        result = self.exporter.to_json(nodes, edges)
        data = json.loads(result)
        self.assertEqual(data["nodes"][0]["symbols"][0]["name"], "MyClass")
        self.assertEqual(data["nodes"][0]["symbols"][0]["line"], 42)

    def test_to_json_includes_metadata(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        result = self.exporter.to_json(nodes, edges)
        data = json.loads(result)
        self.assertEqual(data["metadata"]["file_count"], 2)
        self.assertEqual(data["metadata"]["import_count"], 1)

    def test_to_json_includes_analysis_metadata(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        analysis = AnalysisResult(
            god_nodes=[("main.py", 5.0)],
            communities=[
                CommunityResult(
                    community_id=0,
                    label="Core",
                    file_ids={"main.py"},
                    cohesion=1.0,
                    size=1,
                )
            ],
            surprising_connections=[],
            suggested_questions=["What is main.py?"],
            node_count=1,
            edge_count=0,
        )
        result = self.exporter.to_json(nodes, edges, [], analysis)
        data = json.loads(result)
        self.assertIn("analysis", data)
        self.assertEqual(data["analysis"]["god_nodes"][0]["node_id"], "main.py")
        self.assertEqual(len(data["analysis"]["communities"]), 1)

    def test_to_html_produces_standalone_page(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        result = self.exporter.to_html(nodes, edges)
        self.assertIn("<!DOCTYPE html>", result)
        self.assertIn("<title>ReadMenator", result)
        self.assertIn("vis.Network", result)

    def test_to_html_includes_node_data(self) -> None:
        sym = self._make_sym("MyClass", "class", 10)
        nodes = [self._make_node("main.py", "main.py", symbols=[sym])]
        edges: list = []
        result = self.exporter.to_html(nodes, edges)
        self.assertIn("MyClass", result)

    def test_to_html_includes_community_legend_when_analysis(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        analysis = AnalysisResult(
            god_nodes=[],
            communities=[
                CommunityResult(
                    community_id=0,
                    label="Core",
                    file_ids={"main.py"},
                    cohesion=1.0,
                    size=1,
                )
            ],
            surprising_connections=[],
            suggested_questions=[],
            node_count=1,
            edge_count=0,
        )
        result = self.exporter.to_html(nodes, edges, [], analysis)
        self.assertIn("Core", result)

    def test_to_svg_produces_svg_string(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        result = self.exporter.to_svg(nodes, edges)
        self.assertIn("<svg", result)
        self.assertIn("</svg>", result)

    def test_to_svg_render_truncation_for_large_graph(self) -> None:
        nodes = [
            self._make_node(f"{i}.py", f"{i}.py")
            for i in range(self.config.SVG_MAX_NODES + 10)
        ]
        edges: list = []
        result = self.exporter.to_svg(nodes, edges)
        self.assertIn("Graph Too Large", result)

    def test_to_svg_includes_readmenator_title(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        result = self.exporter.to_svg(nodes, edges)
        self.assertIn("ReadMenator", result)

    def test_to_json_handles_resolved_edges(self) -> None:
        nodes = [self._make_node("a.py", "a.py"), self._make_node("b.py", "b.py")]
        edges = [Edge(source="a.py", target="os", relation="imports")]
        resolved = [Edge(source="a.py", target="b.py", relation="resolved_imports")]
        result = self.exporter.to_json(nodes, edges, resolved)
        data = json.loads(result)
        self.assertEqual(data["metadata"]["resolved_import_count"], 1)


if __name__ == "__main__":
    unittest.main()
