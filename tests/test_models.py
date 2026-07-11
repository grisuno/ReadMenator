import unittest

from readmenator._models import Edge, Node, Symbol, pluralize_symbol_kind


class TestSymbolContract(unittest.TestCase):
    def test_symbol_creation(self) -> None:
        sym = Symbol(name="my_func", kind="function", line=42, doc="Does stuff")
        self.assertEqual(sym.name, "my_func")
        self.assertEqual(sym.kind, "function")
        self.assertEqual(sym.line, 42)
        self.assertEqual(sym.doc, "Does stuff")
        self.assertEqual(sym.signature, "")

    def test_symbol_with_signature(self) -> None:
        sym = Symbol(name="add", kind="function", line=10, doc="", signature="int add(int a, int b)")
        self.assertEqual(sym.signature, "int add(int a, int b)")


class TestNodeContract(unittest.TestCase):
    def test_node_creation(self) -> None:
        node = Node(
            node_id="src/main.py",
            label="main.py",
            kind="module",
            language="py",
            doc="",
        )
        self.assertEqual(node.node_id, "src/main.py")
        self.assertEqual(node.label, "main.py")
        self.assertEqual(node.kind, "module")
        self.assertEqual(node.language, "py")
        self.assertEqual(len(node.symbols), 0)

    def test_node_with_symbols(self) -> None:
        sym = Symbol(name="helper", kind="function", line=5)
        node = Node(
            node_id="utils.py",
            label="utils.py",
            kind="module",
            language="py",
            symbols=[sym],
        )
        self.assertEqual(len(node.symbols), 1)
        self.assertIs(node.symbols[0], sym)


class TestEdgeContract(unittest.TestCase):
    def test_edge_creation(self) -> None:
        edge = Edge(source="a.py", target="b.py", relation="imports")
        self.assertEqual(edge.source, "a.py")
        self.assertEqual(edge.target, "b.py")
        self.assertEqual(edge.relation, "imports")


class TestPluralizeContract(unittest.TestCase):
    def test_pluralize_class(self) -> None:
        plural_map = {"class": "classes", "function": "functions"}
        self.assertEqual(pluralize_symbol_kind("class", plural_map), "classes")
        self.assertEqual(pluralize_symbol_kind("function", plural_map), "functions")

    def test_pluralize_unknown_appends_s(self) -> None:
        plural_map = {}
        result = pluralize_symbol_kind("widget", plural_map)
        self.assertEqual(result, "widgets")
