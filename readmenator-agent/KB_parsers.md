# Subsystem: parsers

## readmenator/parsers/__init__.py
- Layer: utility
- Language: py
- Symbols:
  - `_init_parser_map` (function, line 32) `def _init_parser_map()`
  - `create_parser` (function, line 65) `def create_parser(extension, filename, config)`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`

## readmenator/parsers/_assembly.py
- Layer: utility
- Language: py
- Symbols:
  - `AssemblyParser` (class, line 9) `class AssemblyParser(LanguageParser)`
  - `_extract_specifics` (method, line 17) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`

## readmenator/parsers/_base.py
- Layer: utility
- Language: py
- Symbols:
  - `LanguageParser` (class, line 10) `class LanguageParser`
  - `__init__` (method, line 19) `def __init__(self, filename, config)`
  - `parse` (method, line 34) `def parse(self, content)`
  - `_extract_specifics` (method, line 43) `def _extract_specifics(self, content)`
  - `_extract_docstring` (method, line 47) `def _extract_docstring(self, line_num)`
  - `_extract_signature` (method, line 89) `def _extract_signature(self, content, match_start, pattern)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

## readmenator/parsers/_c.py
- Layer: utility
- Language: py
- Symbols:
  - `CParser` (class, line 9) `class CParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_csharp.py
- Layer: utility
- Language: py
- Symbols:
  - `CSharpParser` (class, line 9) `class CSharpParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_dart.py
- Layer: utility
- Language: py
- Symbols:
  - `DartParser` (class, line 9) `class DartParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_elixir.py
- Layer: utility
- Language: py
- Symbols:
  - `ElixirParser` (class, line 9) `class ElixirParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_gdscript.py
- Layer: utility
- Language: py
- Symbols:
  - `GDScriptParser` (class, line 9) `class GDScriptParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_go.py
- Layer: utility
- Language: py
- Symbols:
  - `GoParser` (class, line 9) `class GoParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_java.py
- Layer: utility
- Language: py
- Symbols:
  - `JavaParser` (class, line 9) `class JavaParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_javascript.py
- Layer: utility
- Language: py
- Symbols:
  - `JavaScriptParser` (class, line 9) `class JavaScriptParser(LanguageParser)`
  - `_extract_specifics` (method, line 17) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_kotlin.py
- Layer: utility
- Language: py
- Symbols:
  - `KotlinParser` (class, line 9) `class KotlinParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_lua.py
- Layer: utility
- Language: py
- Symbols:
  - `LuaParser` (class, line 9) `class LuaParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_nim.py
- Layer: utility
- Language: py
- Symbols:
  - `NimParser` (class, line 9) `class NimParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_php.py
- Layer: utility
- Language: py
- Symbols:
  - `PHPParser` (class, line 9) `class PHPParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_python.py
- Layer: utility
- Language: py
- Symbols:
  - `PythonParser` (class, line 10) `class PythonParser(LanguageParser)`
  - `_extract_specifics` (method, line 17) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_ruby.py
- Layer: utility
- Language: py
- Symbols:
  - `RubyParser` (class, line 9) `class RubyParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_rust.py
- Layer: utility
- Language: py
- Symbols:
  - `RustParser` (class, line 9) `class RustParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_scala.py
- Layer: utility
- Language: py
- Symbols:
  - `ScalaParser` (class, line 9) `class ScalaParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_shell.py
- Layer: utility
- Language: py
- Symbols:
  - `ShellParser` (class, line 9) `class ShellParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_swift.py
- Layer: utility
- Language: py
- Symbols:
  - `SwiftParser` (class, line 9) `class SwiftParser(LanguageParser)`
  - `_extract_specifics` (method, line 16) `def _extract_specifics(self, content)`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`
