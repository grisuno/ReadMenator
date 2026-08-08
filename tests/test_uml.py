"""Contract tests for UML class diagram generation and language code generation.

SDD + TDD + BDD: Each test method validates a specific behavioral contract
of the UmlGenerator and its per-language code generators.
"""

from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol
from readmenator._uml import UmlGenerator


class TestUmlMermaidDiagram(unittest.TestCase):
    """BDD: UmlGenerator mermaid class diagram rendering contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_render_empty_nodes_returns_empty_string(self):
        result = self.generator.render_mermaid_class_diagram([], [])
        self.assertEqual(result, "")

    def test_render_no_class_symbols_returns_empty_string(self):
        nodes = [
            Node(
                node_id="src/main.py",
                label="main.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="my_func", kind="function", line=1),
                ],
            )
        ]
        result = self.generator.render_mermaid_class_diagram(nodes, [])
        self.assertEqual(result, "")

    def test_render_single_class_produces_mermaid_class_diagram(self):
        nodes = [
            Node(
                node_id="src/models.py",
                label="models.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="User", kind="class", line=3, doc="A user model"),
                    Symbol(name="login", kind="method", line=5,
                            signature="def login(self, username: str, password: str):"),
                ],
            )
        ]
        result = self.generator.render_mermaid_class_diagram(nodes, [])
        self.assertIn("classDiagram", result)
        self.assertIn("User", result)
        self.assertIn("login", result)
        self.assertIn("<<class>>", result)

    def test_render_multiple_classes_from_different_files(self):
        nodes = [
            Node(
                node_id="src/models.py",
                label="models.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="User", kind="class", line=3),
                    Symbol(name="get_name", kind="method", line=7),
                ],
            ),
            Node(
                node_id="src/services.py",
                label="services.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="UserService", kind="class", line=5),
                    Symbol(name="create_user", kind="method", line=9),
                ],
            ),
        ]
        result = self.generator.render_mermaid_class_diagram(nodes, [])
        self.assertIn("classDiagram", result)
        self.assertIn("User", result)
        self.assertIn("UserService", result)

    def test_render_with_import_edges_produces_relationships(self):
        nodes = [
            Node(
                node_id="src/main.py",
                label="main.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="App", kind="class", line=3),
                ],
            ),
            Node(
                node_id="src/services.py",
                label="services.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="Service", kind="class", line=1),
                ],
            ),
        ]
        edges = [
            Edge(source="src/main.py", target="src/services.py",
                 relation="imports", confidence="EXTRACTED"),
        ]
        result = self.generator.render_mermaid_class_diagram(nodes, edges)
        self.assertIn("-->", result)
        self.assertIn("uses", result)

    def test_render_respects_max_classes_limit(self):
        nodes = []
        for i in range(100):
            nodes.append(
                Node(
                    node_id=f"src/file_{i}.py",
                    label=f"file_{i}.py",
                    kind="module",
                    language="python",
                    symbols=[
                        Symbol(name=f"Class{i}", kind="class", line=1),
                    ],
                )
            )
        result = self.generator.render_mermaid_class_diagram(nodes, [])
        class_count = result.count("<<class>>")
        self.assertLessEqual(class_count, self.config.UML_MAX_CLASSES)

    def test_render_with_structs_interfaces_traits(self):
        nodes = [
            Node(
                node_id="src/types.py",
                label="types.py",
                kind="module",
                language="rust",
                symbols=[
                    Symbol(name="Point", kind="struct", line=1),
                    Symbol(name="Drawable", kind="trait", line=5),
                    Symbol(name="Color", kind="enum", line=10),
                ],
            )
        ]
        result = self.generator.render_mermaid_class_diagram(nodes, [])
        self.assertIn("Point", result)
        self.assertIn("Drawable", result)
        self.assertIn("Color", result)


class TestUmlSanitizeId(unittest.TestCase):
    """BDD: UmlGenerator ID sanitization contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_sanitize_preserves_alphanumeric(self):
        result = self.generator._sanitize_id("hello_world_123")
        self.assertEqual(result, "hello_world_123")

    def test_sanitize_replaces_special_chars(self):
        result = self.generator._sanitize_id("hello/world.py")
        self.assertEqual(result, "hello_world_py")

    def test_sanitize_prefixes_digit_start(self):
        result = self.generator._sanitize_id("123abc")
        self.assertEqual(result, "n_123abc")

    def test_sanitize_handles_empty_string(self):
        result = self.generator._sanitize_id("")
        self.assertEqual(result, "")


class TestUmlCodeGenerationCpp(unittest.TestCase):
    """BDD: C++ code generation contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_generate_cpp_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/models.py",
                label="models.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="User", kind="class", line=3),
                    Symbol(name="login", kind="method", line=5,
                            signature="def login(self, username: str, password: str):"),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "cpp")
        self.assertIn("class User", result)
        self.assertIn("public:", result)
        self.assertIn("void login", result)
        self.assertIn("std::string", result)

    def test_generate_cpp_with_empty_classes(self):
        nodes = [
            Node(
                node_id="src/empty.py",
                label="empty.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="EmptyClass", kind="class", line=1),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "cpp")
        self.assertIn("class EmptyClass", result)

    def test_generate_cpp_unknown_language_returns_error_message(self):
        nodes = [
            Node(
                node_id="src/test.py",
                label="test.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="Foo", kind="class", line=1),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "brainfuck")
        self.assertIn("Unknown target language", result)


class TestUmlCodeGenerationJava(unittest.TestCase):
    """BDD: Java code generation contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_generate_java_class_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/models.py",
                label="models.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="User", kind="class", line=3),
                    Symbol(name="getName", kind="method", line=5,
                            signature="def getName(self) -> str:"),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "java")
        self.assertIn("public class User", result)
        self.assertIn("public void getName", result)
        self.assertIn("import java.util.List", result)

    def test_generate_java_interface_produces_interface(self):
        nodes = [
            Node(
                node_id="src/contract.py",
                label="contract.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="Runnable", kind="interface", line=1),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "java")
        self.assertIn("public interface Runnable", result)


class TestUmlCodeGenerationCSharp(unittest.TestCase):
    """BDD: C# code generation contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_generate_csharp_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/models.py",
                label="models.py",
                kind="module",
                language="python",
                symbols=[
                    Symbol(name="User", kind="class", line=3),
                    Symbol(name="Login", kind="method", line=5),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "csharp")
        self.assertIn("public class User", result)
        self.assertIn("using System", result)


class TestUmlCodeGenerationGo(unittest.TestCase):
    """BDD: Go code generation contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_generate_go_struct_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/models.go",
                label="models.go",
                kind="module",
                language="go",
                symbols=[
                    Symbol(name="User", kind="struct", line=1),
                    Symbol(name="Save", kind="function", line=5),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "go")
        self.assertIn("type User struct", result)
        self.assertIn("package generated", result)

    def test_generate_go_interface_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/iface.go",
                label="iface.go",
                kind="module",
                language="go",
                symbols=[
                    Symbol(name="Reader", kind="interface", line=1),
                    Symbol(name="Read", kind="function", line=5),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "go")
        self.assertIn("type Reader interface", result)


class TestUmlCodeGenerationRust(unittest.TestCase):
    """BDD: Rust code generation contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_generate_rust_struct_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/models.rs",
                label="models.rs",
                kind="module",
                language="rust",
                symbols=[
                    Symbol(name="User", kind="struct", line=1),
                    Symbol(name="new", kind="function", line=5),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "rust")
        self.assertIn("pub struct User", result)

    def test_generate_rust_trait_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/traits.rs",
                label="traits.rs",
                kind="module",
                language="rust",
                symbols=[
                    Symbol(name="Serialize", kind="trait", line=1),
                    Symbol(name="to_json", kind="function", line=5),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "rust")
        self.assertIn("pub trait Serialize", result)


class TestUmlCodeGenerationPhp(unittest.TestCase):
    """BDD: PHP code generation contract."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def test_generate_php_class_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/models.php",
                label="models.php",
                kind="module",
                language="php",
                symbols=[
                    Symbol(name="User", kind="class", line=3),
                    Symbol(name="save", kind="method", line=7),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "php")
        self.assertIn("class User", result)
        self.assertIn("<?php", result)

    def test_generate_php_interface_produces_valid_code(self):
        nodes = [
            Node(
                node_id="src/contract.php",
                label="contract.php",
                kind="module",
                language="php",
                symbols=[
                    Symbol(name="Persistable", kind="interface", line=1),
                ],
            )
        ]
        result = self.generator.generate_code(nodes, [], "php")
        self.assertIn("interface Persistable", result)


class TestUmlCodeGenerationKotlinScalaSwiftDartRuby(unittest.TestCase):
    """BDD: Kotlin, Scala, Swift, Dart, Ruby code generation contracts."""

    def setUp(self) -> None:
        self.config = Config()
        self.generator = UmlGenerator(self.config)

    def _make_class_node(self, name: str, lang: str, kind: str = "class"):
        return Node(
            node_id=f"src/{name}.{lang[:2] if lang != 'kotlin' else 'kt'}",
            label=f"{name}.{lang[:2]}",
            kind="module",
            language=lang,
            symbols=[
                Symbol(name=name, kind=kind, line=1),
                Symbol(name="doWork", kind="method", line=5),
            ],
        )

    def test_generate_kotlin_produces_valid_code(self):
        nodes = [self._make_class_node("User", "kotlin")]
        result = self.generator.generate_code(nodes, [], "kotlin")
        self.assertIn("open class User", result)
        self.assertIn("fun doWork", result)

    def test_generate_scala_produces_valid_code(self):
        nodes = [self._make_class_node("User", "scala")]
        result = self.generator.generate_code(nodes, [], "scala")
        self.assertIn("class User", result)
        self.assertIn("def doWork", result)

    def test_generate_scala_trait_produces_valid_code(self):
        nodes = [self._make_class_node("Drawable", "scala", kind="trait")]
        result = self.generator.generate_code(nodes, [], "scala")
        self.assertIn("trait Drawable", result)

    def test_generate_swift_produces_valid_code(self):
        nodes = [self._make_class_node("User", "swift")]
        result = self.generator.generate_code(nodes, [], "swift")
        self.assertIn("class User", result)
        self.assertIn("import Foundation", result)

    def test_generate_swift_protocol_produces_valid_code(self):
        nodes = [self._make_class_node("Codable", "swift", kind="protocol")]
        result = self.generator.generate_code(nodes, [], "swift")
        self.assertIn("protocol Codable", result)

    def test_generate_dart_produces_valid_code(self):
        nodes = [self._make_class_node("User", "dart")]
        result = self.generator.generate_code(nodes, [], "dart")
        self.assertIn("class User", result)
        self.assertIn("void doWork", result)

    def test_generate_ruby_produces_valid_code(self):
        nodes = [self._make_class_node("User", "ruby")]
        result = self.generator.generate_code(nodes, [], "ruby")
        self.assertIn("class User", result)
        self.assertIn("def doWork", result)


if __name__ == "__main__":
    unittest.main()
