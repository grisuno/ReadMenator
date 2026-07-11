import unittest

from readmenator._config import Config
from readmenator._documentation import DocumentationGenerator
from readmenator._models import Edge, Node, Symbol


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
