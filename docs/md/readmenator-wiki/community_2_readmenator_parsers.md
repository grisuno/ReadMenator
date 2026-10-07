# readmenator/parsers

*Community 2 | 24 files | cohesion 0.69*

## Definition

This community groups 24 file(s) rooted at `readmenator/parsers` with dominant language py (cohesion 0.69). Central symbols: `AssemblyParser`, `CParser`, `CSharpParser`, `DartParser`, `ElixirParser`, `GDScriptParser`, `GoParser`, `JavaParser`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Parser factory: maps file extensions to per-language LanguageParser classes..

## Files

### `readmenator/parsers` (21 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/parsers/__init__.py` | py | utility | 2 | yes |
| `readmenator/parsers/_assembly.py` | py | utility | 2 | yes |
| `readmenator/parsers/_base.py` | py | utility | 6 | yes |
| `readmenator/parsers/_c.py` | py | utility | 3 | yes |
| `readmenator/parsers/_csharp.py` | py | utility | 2 | yes |
| `readmenator/parsers/_dart.py` | py | utility | 2 | yes |
| `readmenator/parsers/_elixir.py` | py | utility | 2 | yes |
| `readmenator/parsers/_gdscript.py` | py | utility | 2 | yes |
| `readmenator/parsers/_go.py` | py | utility | 2 | yes |
| `readmenator/parsers/_java.py` | py | utility | 2 | yes |
| `readmenator/parsers/_javascript.py` | py | utility | 2 | yes |
| `readmenator/parsers/_kotlin.py` | py | utility | 2 | yes |
| `readmenator/parsers/_lua.py` | py | utility | 2 | yes |
| `readmenator/parsers/_nim.py` | py | utility | 2 | yes |
| `readmenator/parsers/_php.py` | py | utility | 2 | yes |
| `readmenator/parsers/_python.py` | py | utility | 2 | yes |
| `readmenator/parsers/_ruby.py` | py | utility | 2 | yes |

### `tests` (3 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_parsers.py` | py | testing | 87 | no |
| `tests/test_parsers_new.py` | py | testing | 36 | yes |
| `tests/test_parsers_property.py` | py | testing | 27 | yes |

*... and 4 more files in this community.*


## Key Symbols

- `_init_parser_map` (function, `readmenator/parsers/__init__.py:34`) `def _init_parser_map()`
- `create_parser` (function, `readmenator/parsers/__init__.py:70`) `def create_parser(extension, filename, config)` - Factory: return a parser instance for the given file extension.
- `AssemblyParser` (class, `readmenator/parsers/_assembly.py:11`) `class AssemblyParser(LanguageParser)` - Parser for assembly (.asm, .s, .S).
- `_extract_specifics` (method, `readmenator/parsers/_assembly.py:19`) `def _extract_specifics(self, content)`
- `LanguageParser` (class, `readmenator/parsers/_base.py:12`) `class LanguageParser` - Base class for all language-specific parsers.
- `__init__` (method, `readmenator/parsers/_base.py:21`) `def __init__(self, filename, config)` - Initialise the parser with a file path and application config.
- `parse` (method, `readmenator/parsers/_base.py:36`) `def parse(self, content)` - Parse *content* and populate symbol/import lists.
- `_extract_specifics` (method, `readmenator/parsers/_base.py:45`) `def _extract_specifics(self, content)` - Subclass hook for language-specific symbol extraction.
- `_extract_docstring` (method, `readmenator/parsers/_base.py:49`) `def _extract_docstring(self, line_num)` - Walk backwards from *line_num* to collect preceding comments/docstrings.
- `_extract_signature` (method, `readmenator/parsers/_base.py:91`) `def _extract_signature(self, content, match_start, pattern)` - Extract a compact signature snippet starting at *match_start*.
- `_has_type_prefix` (function, `readmenator/parsers/_c.py:18`) `def _has_type_prefix(prefix)` - Return True when a prototype prefix carries a return type.
- `CParser` (class, `readmenator/parsers/_c.py:30`) `class CParser(LanguageParser)` - Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).
- `_extract_specifics` (method, `readmenator/parsers/_c.py:37`) `def _extract_specifics(self, content)` - Extract C-family symbols and imports from source content.
- `CSharpParser` (class, `readmenator/parsers/_csharp.py:11`) `class CSharpParser(LanguageParser)` - Parser for C# (.cs).
- `_extract_specifics` (method, `readmenator/parsers/_csharp.py:18`) `def _extract_specifics(self, content)`
- `DartParser` (class, `readmenator/parsers/_dart.py:11`) `class DartParser(LanguageParser)` - Parser for Dart (.dart).
- `_extract_specifics` (method, `readmenator/parsers/_dart.py:18`) `def _extract_specifics(self, content)`
- `ElixirParser` (class, `readmenator/parsers/_elixir.py:11`) `class ElixirParser(LanguageParser)` - Parser for Elixir (.ex, .exs).
- `_extract_specifics` (method, `readmenator/parsers/_elixir.py:18`) `def _extract_specifics(self, content)`
- `GDScriptParser` (class, `readmenator/parsers/_gdscript.py:11`) `class GDScriptParser(LanguageParser)` - Parser for Godot GDScript (.gd).
- `_extract_specifics` (method, `readmenator/parsers/_gdscript.py:18`) `def _extract_specifics(self, content)`
- `GoParser` (class, `readmenator/parsers/_go.py:11`) `class GoParser(LanguageParser)` - Parser for Go (.go).
- `_extract_specifics` (method, `readmenator/parsers/_go.py:18`) `def _extract_specifics(self, content)`
- `JavaParser` (class, `readmenator/parsers/_java.py:11`) `class JavaParser(LanguageParser)` - Parser for Java (.java).
- `_extract_specifics` (method, `readmenator/parsers/_java.py:18`) `def _extract_specifics(self, content)`
- `JavaScriptParser` (class, `readmenator/parsers/_javascript.py:11`) `class JavaScriptParser(LanguageParser)` - Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).
- `_extract_specifics` (method, `readmenator/parsers/_javascript.py:19`) `def _extract_specifics(self, content)`
- `KotlinParser` (class, `readmenator/parsers/_kotlin.py:11`) `class KotlinParser(LanguageParser)` - Parser for Kotlin (.kt, .kts).
- `_extract_specifics` (method, `readmenator/parsers/_kotlin.py:18`) `def _extract_specifics(self, content)`
- `LuaParser` (class, `readmenator/parsers/_lua.py:11`) `class LuaParser(LanguageParser)` - Parser for Lua (.lua).

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 59
- Cross-boundary resolved imports (EXTRACTED): 27

## Connections

- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/_scanner.py imports readmenator/parsers/__init__.py.
- [INFERRED] bridges community 1 <-> 2 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches readmenator/parsers/__init__.py in 4 hops.
- [INFERRED] shares_context community 2 <-> 3 (strength 0.5): Inferred shared context (language py) with no import path between community 2 (readmenator/parsers) and community 3 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `tests/test_parsers.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator/parsers changed?
- Should readmenator/parsers be split, given cohesion 0.69?

## Sources

- `readmenator/parsers/__init__.py`
- `readmenator/parsers/_assembly.py`
- `readmenator/parsers/_base.py`
- `readmenator/parsers/_c.py`
- `readmenator/parsers/_csharp.py`
- `readmenator/parsers/_dart.py`
- `readmenator/parsers/_elixir.py`
- `readmenator/parsers/_gdscript.py`
- `readmenator/parsers/_go.py`
- `readmenator/parsers/_java.py`
- `readmenator/parsers/_javascript.py`
- `readmenator/parsers/_kotlin.py`
- `readmenator/parsers/_lua.py`
- `readmenator/parsers/_nim.py`
- `readmenator/parsers/_php.py`
- `readmenator/parsers/_python.py`
- `readmenator/parsers/_ruby.py`
- `readmenator/parsers/_rust.py`
- `readmenator/parsers/_scala.py`
- `readmenator/parsers/_shell.py`
- *... and 4 more*
