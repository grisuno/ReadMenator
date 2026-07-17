import unittest

from readmenator._config import Config
from readmenator.parsers import (
    AssemblyParser,
    CParser,
    CSharpParser,
    DartParser,
    GDScriptParser,
    GoParser,
    JavaParser,
    JavaScriptParser,
    NimParser,
    PHPParser,
    PythonParser,
    RustParser,
    ShellParser,
    create_parser,
)


class TestCParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "/** Adds two numbers */\nint add(int a, int b) {\n    return a + b;\n}\n"
        parser = CParser("test.c", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("add", names)

    def test_extracts_struct(self) -> None:
        code = "struct Point { int x; int y; };\n"
        parser = CParser("test.c", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Point", names)

    def test_extracts_include(self) -> None:
        code = "#include <stdio.h>\n#include \"local.h\"\n"
        parser = CParser("test.c", self.config)
        parser.parse(code)
        self.assertIn("stdio.h", parser.imports)
        self.assertIn("local.h", parser.imports)

    def test_extracts_define(self) -> None:
        code = "#define MAX_SIZE 1024\n"
        parser = CParser("test.c", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("MAX_SIZE", names)

    def test_skips_reserved_words(self) -> None:
        code = "int main() {\n    if (x) {}\n    for (;;) {}\n    return 0;\n}\n"
        parser = CParser("test.c", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("main", names)
        self.assertNotIn("if", names)
        self.assertNotIn("for", names)
        self.assertNotIn("return", names)

    def test_class_with_inheritance(self) -> None:
        code = "class Dog : public Animal {};\n"
        parser = CParser("test.cpp", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Dog", names)


class TestPythonParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "def hello(name: str) -> None:\n    pass\n"
        parser = PythonParser("test.py", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("hello", names)

    def test_extracts_class(self) -> None:
        code = "class MyClass:\n    pass\n"
        parser = PythonParser("test.py", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("MyClass", names)

    def test_extracts_imports(self) -> None:
        code = "import os\nimport sys\nfrom pathlib import Path\n"
        parser = PythonParser("test.py", self.config)
        parser.parse(code)
        self.assertIn("os", parser.imports)
        self.assertIn("sys", parser.imports)
        self.assertIn("pathlib", parser.imports)

    def test_extracts_async_function(self) -> None:
        code = "async def fetch_data(url: str) -> dict:\n    pass\n"
        parser = PythonParser("test.py", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("fetch_data", names)

    def test_handles_syntax_error_gracefully(self) -> None:
        code = "def broken(\n"
        parser = PythonParser("broken.py", self.config)
        parser.parse(code)
        self.assertEqual(len(parser.symbols), 0)

    def test_suppresses_syntax_warnings(self) -> None:
        import warnings
        code = 'pattern = "\\e \\. \\S"\n'
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            parser = PythonParser("regex_test.py", self.config)
            parser.parse(code)
            syntax_warnings = [
                x for x in w if issubclass(x.category, SyntaxWarning)
            ]
            self.assertEqual(len(syntax_warnings), 0)

    def test_extracts_signature_with_params(self) -> None:
        code = "def greet(name: str, age: int) -> str:\n    return f'{name}'\n"
        parser = PythonParser("test.py", self.config)
        parser.parse(code)
        self.assertEqual(len(parser.symbols), 1)
        self.assertIn("name", parser.symbols[0].signature)
        self.assertIn("age", parser.symbols[0].signature)

    def test_extracts_class_with_bases(self) -> None:
        code = "class Child(Parent, Mixin):\n    pass\n"
        parser = PythonParser("test.py", self.config)
        parser.parse(code)
        sym = parser.symbols[0]
        self.assertEqual(sym.name, "Child")
        self.assertIn("Parent", sym.signature)
        self.assertIn("Mixin", sym.signature)


class TestGoParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "func main() {\n}\n"
        parser = GoParser("test.go", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("main", names)

    def test_extracts_method_receiver(self) -> None:
        code = "func (u *User) Save() error {\n}\n"
        parser = GoParser("test.go", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Save", names)

    def test_extracts_import_block(self) -> None:
        code = 'import (\n\t"fmt"\n\t"os"\n)\n'
        parser = GoParser("test.go", self.config)
        parser.parse(code)
        self.assertIn("fmt", parser.imports)
        self.assertIn("os", parser.imports)

    def test_extracts_single_import(self) -> None:
        code = 'import "fmt"\n'
        parser = GoParser("test.go", self.config)
        parser.parse(code)
        self.assertIn("fmt", parser.imports)

    def test_extracts_struct_and_interface(self) -> None:
        code = "type User struct {}\ntype Reader interface {}\n"
        parser = GoParser("test.go", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        kinds = [s.kind for s in parser.symbols]
        self.assertIn("User", names)
        self.assertIn("struct", kinds)
        self.assertIn("Reader", names)
        self.assertIn("interface", kinds)


class TestRustParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "fn calculate() {}\n"
        parser = RustParser("test.rs", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("calculate", names)

    def test_extracts_pub_function(self) -> None:
        code = "pub fn run() {}\n"
        parser = RustParser("test.rs", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("run", names)

    def test_extracts_struct_and_trait_and_enum(self) -> None:
        code = "struct Point {}\npub trait Draw {}\nenum Color {}\n"
        parser = RustParser("test.rs", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        kinds = [s.kind for s in parser.symbols]
        self.assertIn("Point", names)
        self.assertIn("struct", kinds)
        self.assertIn("Draw", names)
        self.assertIn("trait", kinds)
        self.assertIn("Color", names)
        self.assertIn("enum", kinds)

    def test_extracts_use(self) -> None:
        code = "use std::collections::HashMap;\n"
        parser = RustParser("test.rs", self.config)
        parser.parse(code)
        self.assertIn("std::collections::HashMap", parser.imports)


class TestJavaScriptParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "function hello() {}\n"
        parser = JavaScriptParser("test.js", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("hello", names)

    def test_extracts_arrow_function(self) -> None:
        code = "const greet = (name) => {}\n"
        parser = JavaScriptParser("test.js", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("greet", names)

    def test_extracts_class(self) -> None:
        code = "class Animal {}\n"
        parser = JavaScriptParser("test.js", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Animal", names)

    def test_extracts_import_and_require(self) -> None:
        code = 'import { readFile } from "fs";\nconst http = require("http");\n'
        parser = JavaScriptParser("test.js", self.config)
        parser.parse(code)
        self.assertIn("fs", parser.imports)
        self.assertIn("http", parser.imports)

    def test_skips_reserved_words(self) -> None:
        code = "if (true) {}\nfor (;;) {}\n"
        parser = JavaScriptParser("test.js", self.config)
        parser.parse(code)
        self.assertEqual(len(parser.symbols), 0)


class TestJavaParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class(self) -> None:
        code = "public class HelloWorld {}\n"
        parser = JavaParser("test.java", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("HelloWorld", names)

    def test_extracts_method(self) -> None:
        code = "public void sayHello() {}\n"
        parser = JavaParser("test.java", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("sayHello", names)

    def test_extracts_import(self) -> None:
        code = "import java.util.List;\n"
        parser = JavaParser("test.java", self.config)
        parser.parse(code)
        self.assertIn("java.util.List", parser.imports)

    def test_abstract_class(self) -> None:
        code = "public abstract class BaseHandler {}\n"
        parser = JavaParser("test.java", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("BaseHandler", names)


class TestCSharpParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class(self) -> None:
        code = "public class MyService {}\n"
        parser = CSharpParser("test.cs", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("MyService", names)

    def test_extracts_method(self) -> None:
        code = "public void Execute() {}\n"
        parser = CSharpParser("test.cs", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Execute", names)

    def test_extracts_using(self) -> None:
        code = "using System.Collections.Generic;\n"
        parser = CSharpParser("test.cs", self.config)
        parser.parse(code)
        self.assertIn("System.Collections.Generic", parser.imports)

    def test_record_and_interface(self) -> None:
        code = "public record Person {}\npublic interface ILogger {}\n"
        parser = CSharpParser("test.cs", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Person", names)
        self.assertIn("ILogger", names)


class TestShellParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function_with_parentheses(self) -> None:
        code = "my_func() {\n  echo hi\n}\n"
        parser = ShellParser("test.sh", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("my_func", names)

    def test_extracts_function_keyword(self) -> None:
        code = "function greet {\n  echo hello\n}\n"
        parser = ShellParser("test.sh", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("greet", names)


class TestPHPParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "function hello() {}\n"
        parser = PHPParser("test.php", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("hello", names)

    def test_extracts_class(self) -> None:
        code = "class UserController {}\n"
        parser = PHPParser("test.php", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("UserController", names)

    def test_extracts_use_and_require(self) -> None:
        code = 'use App\\Models\\User;\nrequire_once "config.php";\n'
        parser = PHPParser("test.php", self.config)
        parser.parse(code)
        self.assertIn("App\\Models\\User", parser.imports)
        self.assertIn("config.php", parser.imports)


class TestDartParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class(self) -> None:
        code = "class MyWidget extends StatelessWidget {}\n"
        parser = DartParser("test.dart", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("MyWidget", names)

    def test_extracts_function(self) -> None:
        code = "void main() {}\n"
        parser = DartParser("test.dart", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("main", names)

    def test_extracts_import(self) -> None:
        code = "import 'package:flutter/material.dart';\n"
        parser = DartParser("test.dart", self.config)
        parser.parse(code)
        self.assertIn("package:flutter/material.dart", parser.imports)


class TestGDScriptParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        code = "func _ready():\n    pass\n"
        parser = GDScriptParser("test.gd", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("_ready", names)

    def test_extracts_extends(self) -> None:
        code = "extends Node2D\n"
        parser = GDScriptParser("test.gd", self.config)
        parser.parse(code)
        self.assertIn("Node2D", parser.imports)


class TestNimParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_proc(self) -> None:
        code = "proc hello() =\n  echo \"hi\"\n"
        parser = NimParser("test.nim", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("hello", names)

    def test_extracts_type(self) -> None:
        code = "type Person = object\n"
        parser = NimParser("test.nim", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("Person", names)

    def test_extracts_import(self) -> None:
        code = "import os, strutils\n"
        parser = NimParser("test.nim", self.config)
        parser.parse(code)
        self.assertIn("os", parser.imports)
        self.assertIn("strutils", parser.imports)


class TestAssemblyParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_label(self) -> None:
        code = "_start:\n    mov rax, 60\n"
        parser = AssemblyParser("test.s", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("_start", names)

    def test_extracts_multiple_labels(self) -> None:
        code = "main:\nloop:\n    jmp loop\n"
        parser = AssemblyParser("test.s", self.config)
        parser.parse(code)
        names = [s.name for s in parser.symbols]
        self.assertIn("main", names)
        self.assertIn("loop", names)


class TestParserFactoryContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_returns_c_parser_for_c_extensions(self) -> None:
        for ext in (".c", ".cpp", ".cc", ".cxx", ".h", ".hpp"):
            parser = create_parser(ext, f"test{ext}", self.config)
            self.assertIsNotNone(parser)
            self.assertIsInstance(parser, CParser)

    def test_returns_python_parser_for_py(self) -> None:
        parser = create_parser(".py", "test.py", self.config)
        self.assertIsNotNone(parser)
        self.assertIsInstance(parser, PythonParser)

    def test_returns_none_for_unknown_extension(self) -> None:
        parser = create_parser(".xyz", "test.xyz", self.config)
        self.assertIsNone(parser)

    def test_returns_rust_parser_for_rs(self) -> None:
        parser = create_parser(".rs", "test.rs", self.config)
        self.assertIsNotNone(parser)
        self.assertIsInstance(parser, RustParser)

    def test_case_insensitive_extension(self) -> None:
        parser = create_parser(".PY", "test.PY", self.config)
        self.assertIsNotNone(parser)
        self.assertIsInstance(parser, PythonParser)
