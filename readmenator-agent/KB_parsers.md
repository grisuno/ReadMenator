# Subsystem: parsers

## readmenator/parsers/__init__.py
- Layer: utility
- Doc: Parser factory: maps file extensions to per-language LanguageParser classes.
- Language: py
- Symbols:
  - `_init_parser_map` (function, line 34) `def _init_parser_map()`
  - `create_parser` (function, line 70) `def create_parser(extension, filename, config)`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`

## readmenator/parsers/_assembly.py
- Layer: utility
- Doc: Assembly parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `AssemblyParser` (class, line 11) `class AssemblyParser(LanguageParser)`
  - `_extract_specifics` (method, line 19) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`

## readmenator/parsers/_base.py
- Layer: utility
- Doc: LanguageParser base class with shared docstring and signature extraction.
- Language: py
- Symbols:
  - `LanguageParser` (class, line 12) `class LanguageParser`
  - `__init__` (method, line 21) `def __init__(self, filename, config)`
  - `parse` (method, line 36) `def parse(self, content)`
  - `_extract_specifics` (method, line 45) `def _extract_specifics(self, content)`
  - `_extract_docstring` (method, line 49) `def _extract_docstring(self, line_num)`
  - `_extract_signature` (method, line 91) `def _extract_signature(self, content, match_start, pattern)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

## readmenator/parsers/_c.py
- Layer: utility
- Doc: C and C++ parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `_has_type_prefix` (function, line 18) `def _has_type_prefix(prefix)`
  - `CParser` (class, line 30) `class CParser(LanguageParser)`
  - `_extract_specifics` (method, line 37) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_csharp.py
- Layer: utility
- Doc: C# parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `CSharpParser` (class, line 11) `class CSharpParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_dart.py
- Layer: utility
- Doc: Dart parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `DartParser` (class, line 11) `class DartParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_elixir.py
- Layer: utility
- Doc: Elixir parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `ElixirParser` (class, line 11) `class ElixirParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_gdscript.py
- Layer: utility
- Doc: GDScript parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `GDScriptParser` (class, line 11) `class GDScriptParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_go.py
- Layer: utility
- Doc: Go parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `GoParser` (class, line 11) `class GoParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_java.py
- Layer: utility
- Doc: Java parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `JavaParser` (class, line 11) `class JavaParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_javascript.py
- Layer: utility
- Doc: JavaScript and TypeScript parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `JavaScriptParser` (class, line 11) `class JavaScriptParser(LanguageParser)`
  - `_extract_specifics` (method, line 19) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_kotlin.py
- Layer: utility
- Doc: Kotlin parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `KotlinParser` (class, line 11) `class KotlinParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_lua.py
- Layer: utility
- Doc: Lua parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `LuaParser` (class, line 11) `class LuaParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_nim.py
- Layer: utility
- Doc: Nim parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `NimParser` (class, line 11) `class NimParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_php.py
- Layer: utility
- Doc: PHP parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `PHPParser` (class, line 11) `class PHPParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_python.py
- Layer: utility
- Doc: Python parser: native ast extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `PythonParser` (class, line 12) `class PythonParser(LanguageParser)`
  - `_extract_specifics` (method, line 19) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_ruby.py
- Layer: utility
- Doc: Ruby parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `RubyParser` (class, line 11) `class RubyParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_rust.py
- Layer: utility
- Doc: Rust parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `RustParser` (class, line 11) `class RustParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_scala.py
- Layer: utility
- Doc: Scala parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `ScalaParser` (class, line 11) `class ScalaParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_shell.py
- Layer: utility
- Doc: Shell parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `ShellParser` (class, line 11) `class ShellParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_swift.py
- Layer: utility
- Doc: Swift parser: regex extraction of symbols, signatures, docstrings, and imports.
- Language: py
- Symbols:
  - `SwiftParser` (class, line 11) `class SwiftParser(LanguageParser)`
  - `_extract_specifics` (method, line 18) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`
