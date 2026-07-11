import unittest

from readmenator._models import Edge, Node, Symbol
from readmenator._query import QueryEngine


def _make_node(node_id: str, symbols=None) -> Node:
    return Node(
        node_id=node_id,
        label=node_id.split("/")[-1],
        kind="module",
        language=node_id.split(".")[-1],
        doc="",
        symbols=symbols or [],
    )


def _make_sym(name: str, kind: str = "function", line: int = 1) -> Symbol:
    return Symbol(name=name, kind=kind, line=line)


class TestQueryEngineContract(unittest.TestCase):
    def setUp(self) -> None:
        self.nodes = [
            _make_node("main.py", [_make_sym("run", "function"), _make_sym("Config", "class")]),
            _make_node("utils.py", [_make_sym("helper", "function")]),
            _make_node("models/user.py", [_make_sym("User", "class"), _make_sym("Profile", "class")]),
        ]
        self.edges = [
            Edge(source="main.py", target="utils.py", relation="imports"),
            Edge(source="main.py", target="models/user.py", relation="imports"),
            Edge(source="utils.py", target="os", relation="imports"),
        ]
        self.engine = QueryEngine(self.nodes, self.edges)

    def test_find_exact_symbol(self) -> None:
        results = self.engine.find_symbol("run")
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1].name, "run")

    def test_find_symbol_fuzzy(self) -> None:
        results = self.engine.find_symbol("User")
        self.assertIsNotNone(results)
        self.assertEqual(results[0][1].name, "User")

    def test_find_symbol_not_found(self) -> None:
        results = self.engine.find_symbol("nonexistent")
        self.assertIsNone(results)

    def test_explain_returns_details(self) -> None:
        result = self.engine.explain("run")
        self.assertIsNotNone(result)
        self.assertIn("run", result)
        self.assertIn("function", result)
        self.assertIn("main.py", result)

    def test_explain_shows_imports(self) -> None:
        result = self.engine.explain("Config")
        self.assertIsNotNone(result)
        self.assertIn("Imports", result)

    def test_explain_shows_siblings(self) -> None:
        result = self.engine.explain("run")
        self.assertIsNotNone(result)
        self.assertIn("Siblings", result)
        self.assertIn("Config", result)

    def test_explain_unknown_returns_none(self) -> None:
        result = self.engine.explain("ghost")
        self.assertIsNone(result)

    def test_find_path_direct_import(self) -> None:
        path = self.engine.find_path("run", "helper")
        self.assertIsNotNone(path)
        self.assertIn("main.py", path)
        self.assertIn("utils.py", path)

    def test_find_path_same_file(self) -> None:
        path = self.engine.find_path("run", "Config")
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 1)

    def test_find_path_unknown_returns_none(self) -> None:
        path = self.engine.find_path("run", "ghost")
        self.assertIsNone(path)

    def test_summary_shows_counts(self) -> None:
        summary = self.engine.summary()
        self.assertIn("3 files", summary)
        self.assertIn("5 symbols", summary)
        self.assertIn("3 imports", summary)

    def test_summary_shows_top_modules(self) -> None:
        summary = self.engine.summary()
        self.assertIn("main.py", summary)

    def test_query_returns_matching_symbols(self) -> None:
        result = self.engine.query("helper function")
        self.assertIn("helper", result)

    def test_query_returns_file_matches(self) -> None:
        result = self.engine.query("user profile")
        self.assertIn("user", result.lower())
