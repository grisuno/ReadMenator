"""Contract tests for the 6 new language parsers.

Validates that Ruby, Swift, Kotlin, Scala, Lua, and Elixir parsers
correctly extract symbols, imports, calls, and inheritance edges.
"""

from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._parsers import create_parser


class TestRubyParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class_with_inheritance(self) -> None:
        parser = create_parser(".rb", "test.rb", self.config)
        parser.parse("class Dog < Animal\nend")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "Dog")
        self.assertEqual(len(parser.inherits), 1)
        self.assertEqual(parser.inherits[0][1], "Animal")

    def test_extracts_module(self) -> None:
        parser = create_parser(".rb", "test.rb", self.config)
        parser.parse("module MyModule\nend")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].kind, "module")

    def test_extracts_method(self) -> None:
        parser = create_parser(".rb", "test.rb", self.config)
        parser.parse("def hello\nend")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "hello")

    def test_extracts_require(self) -> None:
        parser = create_parser(".rb", "test.rb", self.config)
        parser.parse("require 'json'\nrequire_relative './helper'")
        self.assertIn("json", parser.imports)


class TestSwiftParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class(self) -> None:
        parser = create_parser(".swift", "test.swift", self.config)
        parser.parse("class ViewController: UIViewController {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "ViewController")

    def test_extracts_function(self) -> None:
        parser = create_parser(".swift", "test.swift", self.config)
        parser.parse("func viewDidLoad() {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].kind, "function")

    def test_extracts_protocol(self) -> None:
        parser = create_parser(".swift", "test.swift", self.config)
        parser.parse("protocol Drawable {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].kind, "protocol")


class TestKotlinParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class(self) -> None:
        parser = create_parser(".kt", "test.kt", self.config)
        parser.parse("class MyActivity : AppCompatActivity() {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "MyActivity")

    def test_extracts_fun(self) -> None:
        parser = create_parser(".kt", "test.kt", self.config)
        parser.parse("fun onCreate(savedInstanceState: Bundle?) {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "onCreate")


class TestScalaParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_object(self) -> None:
        parser = create_parser(".scala", "test.scala", self.config)
        parser.parse("object Main extends App {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "Main")

    def test_extracts_def(self) -> None:
        parser = create_parser(".scala", "test.scala", self.config)
        parser.parse("def greet(name: String): Unit = {\n}")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "greet")


class TestLuaParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_function(self) -> None:
        parser = create_parser(".lua", "test.lua", self.config)
        parser.parse("function setup() end")
        self.assertGreater(len(parser.symbols), 0)

    def test_extracts_require(self) -> None:
        parser = create_parser(".lua", "test.lua", self.config)
        parser.parse('local json = require("json")')
        self.assertIn("json", parser.imports)


class TestElixirParserContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_defmodule(self) -> None:
        parser = create_parser(".ex", "test.ex", self.config)
        parser.parse("defmodule MyApp.Worker do\nend")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].kind, "module")

    def test_extracts_function(self) -> None:
        parser = create_parser(".ex", "test.ex", self.config)
        parser.parse("def process(data) do\nend")
        self.assertEqual(len(parser.symbols), 1)
        self.assertEqual(parser.symbols[0].name, "process")


class TestNewParserFactoryContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_ruby_extension_maps_correctly(self) -> None:
        parser = create_parser(".rb", "test.rb", self.config)
        self.assertIsNotNone(parser)

    def test_swift_extension_maps_correctly(self) -> None:
        parser = create_parser(".swift", "test.swift", self.config)
        self.assertIsNotNone(parser)

    def test_kotlin_extension_maps_correctly(self) -> None:
        parser = create_parser(".kt", "test.kt", self.config)
        self.assertIsNotNone(parser)


class TestPythonCallExtractionContract(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_extracts_class_inheritance(self) -> None:
        parser = create_parser(".py", "test.py", self.config)
        parser.parse("class Dog(Animal):\n    pass")
        self.assertGreater(len(parser.inherits), 0)

    def test_extracts_function_calls(self) -> None:
        parser = create_parser(".py", "test.py", self.config)
        parser.parse("def main():\n    helper()\ndef helper():\n    pass")
        self.assertGreater(len(parser.calls), 0)


if __name__ == "__main__":
    unittest.main()
