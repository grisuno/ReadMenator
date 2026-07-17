import unittest

from readmenator._mermaid import MermaidRenderer
from readmenator._models import Edge, Node, Symbol


class TestMermaidRendererContract(unittest.TestCase):
    def setUp(self) -> None:
        self.renderer = MermaidRenderer()

    def test_renders_graph_header(self) -> None:
        output, _ = self.renderer.render([], [])
        self.assertIn("graph TD", output)
        self.assertIn("classDef mod", output)
        self.assertIn("classDef cls", output)
        self.assertIn("classDef fn", output)
        self.assertIn("classDef ext", output)

    def test_renders_module_node(self) -> None:
        node = Node(
            node_id="test.py", label="test.py", kind="module", language="py", doc="",
        )
        output, _ = self.renderer.render([node], [])
        self.assertIn('test_py["test.py (py)"]', output)
        self.assertIn("class test_py mod;", output)

    def test_renders_symbol_subnodes(self) -> None:
        sym = Symbol(name="my_func", kind="function", line=1)
        node = Node(
            node_id="test.py", label="test.py", kind="module", language="py",
            symbols=[sym],
        )
        output, _ = self.renderer.render([node], [])
        self.assertIn("test_py_my_func", output)

    def test_class_symbol_gets_cls_style(self) -> None:
        sym = Symbol(name="MyClass", kind="class", line=1)
        node = Node(
            node_id="test.py", label="test.py", kind="module", language="py",
            symbols=[sym],
        )
        output, _ = self.renderer.render([node], [])
        self.assertIn("class test_py_MyClass cls;", output)

    def test_function_symbol_gets_fn_style(self) -> None:
        sym = Symbol(name="helper", kind="function", line=1)
        node = Node(
            node_id="test.py", label="test.py", kind="module", language="py",
            symbols=[sym],
        )
        output, _ = self.renderer.render([node], [])
        self.assertIn("class test_py_helper fn;", output)

    def test_external_import_edge_is_dashed(self) -> None:
        node = Node(
            node_id="main.py", label="main.py", kind="module", language="py", doc="",
        )
        edge = Edge(source="main.py", target="os", relation="imports")
        output, _ = self.renderer.render([node], [edge])
        self.assertIn("-.->|imports|", output)

    def test_truncation_when_over_limit(self) -> None:
        renderer = MermaidRenderer(max_nodes=5)
        nodes = [
            Node(node_id=f"f{i}.py", label=f"f{i}.py", kind="module", language="py", doc="")
            for i in range(20)
        ]
        output, is_truncated = renderer.render(nodes, [])
        self.assertTrue(is_truncated)
        self.assertIn("classDef mod", output)

    def test_limits_symbols_to_five_per_node(self) -> None:
        symbols = [Symbol(name=f"f{i}", kind="function", line=i) for i in range(10)]
        node = Node(
            node_id="big.py", label="big.py", kind="module", language="py",
            symbols=symbols,
        )
        output, _ = self.renderer.render([node], [])
        count = output.count("class big_py_f")
        self.assertLessEqual(count, 5)

    def test_handles_special_characters_in_ids(self) -> None:
        node = Node(
            node_id="my-project/src/foo-bar.ts", label="foo-bar.ts",
            kind="module", language="ts", doc="",
        )
        output, _ = self.renderer.render([node], [])
        self.assertNotIn("my-project/src/foo-bar.ts", output)
        self.assertIn("my_project", output)
