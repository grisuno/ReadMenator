from __future__ import annotations

import json
import unittest

from readmenator._config import Config
from readmenator._cpg import CodePropertyGraph
from readmenator._models import Edge, Node, Symbol


class TestCodePropertyGraphContract(unittest.TestCase):
    """Contract: CodePropertyGraph generates valid JSON-LD CPG output."""

    def setUp(self) -> None:
        self.config = Config()
        self.cpg = CodePropertyGraph(self.config)

    def _make_node(self, nid: str, label: str, lang: str = "py") -> Node:
        return Node(node_id=nid, label=label, kind="module", language=lang)

    def _make_sym(self, name: str, kind: str = "class", line: int = 1) -> Symbol:
        return Symbol(name=name, kind=kind, line=line)

    def test_generate_returns_valid_json(self) -> None:
        nodes = [self._make_node("main.py", "main.py")]
        edges: list = []
        result = self.cpg.generate(nodes, edges)
        data = json.loads(result)
        self.assertIn("@context", data)
        self.assertIn("nodes", data)
        self.assertIn("edges", data)

    def test_generate_includes_node_data(self) -> None:
        sym = self._make_sym("MyClass", "class", 42)
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            symbols=[sym],
        )
        result = self.cpg.generate([node], [])
        data = json.loads(result)
        self.assertEqual(len(data["nodes"]), 1)
        self.assertEqual(data["nodes"][0]["id"], "main.py")
        self.assertEqual(data["nodes"][0]["symbols"][0]["name"], "MyClass")
        self.assertEqual(data["nodes"][0]["symbols"][0]["line"], 42)

    def test_generate_includes_edges(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        edges = [Edge(source="a.py", target="b.py", relation="imports")]
        result = self.cpg.generate(nodes, edges)
        data = json.loads(result)
        self.assertEqual(len(data["edges"]), 1)
        self.assertEqual(data["edges"][0]["source"], "a.py")
        self.assertEqual(data["edges"][0]["target"], "b.py")

    def test_generate_includes_metadata(self) -> None:
        nodes = [
            self._make_node("a.py", "a.py"),
            self._make_node("b.py", "b.py"),
        ]
        result = self.cpg.generate(nodes, [])
        data = json.loads(result)
        self.assertEqual(data["metadata"]["file_count"], 2)
        self.assertEqual(data["generator"], "readmenator")

    def test_privacy_mode_strips_docs(self) -> None:
        cfg = Config(PRIVACY_MODE=True)
        cpg = CodePropertyGraph(cfg)
        sym = self._make_sym("MyClass", "class", line=1)
        sym.doc = "Sensitive docstring"
        node = Node(
            node_id="main.py",
            label="main.py",
            kind="module",
            language="py",
            doc="File level doc",
            symbols=[sym],
        )
        result = cpg.generate([node], [])
        data = json.loads(result)
        self.assertNotIn("doc", data["nodes"][0])
        self.assertNotIn("doc", data["nodes"][0]["symbols"][0])

    def test_sha256_hash_included(self) -> None:
        node = self._make_node("main.py", "main.py")
        result = self.cpg.generate([node], [])
        data = json.loads(result)
        self.assertIn("sha256", data["nodes"][0])
        self.assertEqual(len(data["nodes"][0]["sha256"]), 16)

    def test_empty_graph_returns_valid_json(self) -> None:
        result = self.cpg.generate([], [])
        data = json.loads(result)
        self.assertEqual(data["metadata"]["file_count"], 0)
        self.assertEqual(len(data["nodes"]), 0)
