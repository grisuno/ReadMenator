# `readmenator.parsers._base`

> Source: [readmenator/parsers/_base.py:1](../../readmenator/parsers/_base.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

LanguageParser base class with shared docstring and signature extraction.

## Contents

- **Classes:** [`LanguageParser`](#languageparser)

## Classes

<a id="languageparser"></a>

### `LanguageParser`

`class` | [readmenator/parsers/_base.py:12](../../readmenator/parsers/_base.py#L12)

```python
class LanguageParser
```

Subclasses: [`AssemblyParser`](readmenator.parsers._assembly.py.md#assemblyparser), [`CParser`](readmenator.parsers._c.py.md#cparser), [`CSharpParser`](readmenator.parsers._csharp.py.md#csharpparser), [`DartParser`](readmenator.parsers._dart.py.md#dartparser), [`ElixirParser`](readmenator.parsers._elixir.py.md#elixirparser), [`GDScriptParser`](readmenator.parsers._gdscript.py.md#gdscriptparser), [`GoParser`](readmenator.parsers._go.py.md#goparser), [`JavaParser`](readmenator.parsers._java.py.md#javaparser), [`JavaScriptParser`](readmenator.parsers._javascript.py.md#javascriptparser), [`KotlinParser`](readmenator.parsers._kotlin.py.md#kotlinparser), [`LuaParser`](readmenator.parsers._lua.py.md#luaparser), [`NimParser`](readmenator.parsers._nim.py.md#nimparser), [`PHPParser`](readmenator.parsers._php.py.md#phpparser), [`PythonParser`](readmenator.parsers._python.py.md#pythonparser), [`RubyParser`](readmenator.parsers._ruby.py.md#rubyparser), [`RustParser`](readmenator.parsers._rust.py.md#rustparser), [`ScalaParser`](readmenator.parsers._scala.py.md#scalaparser), [`ShellParser`](readmenator.parsers._shell.py.md#shellparser), [`SwiftParser`](readmenator.parsers._swift.py.md#swiftparser)

Base class for all language-specific parsers.

Subclasses must implement ``_extract_specifics`` to populate
``self.symbols`` and ``self.imports``. Common utility methods
``_extract_docstring`` and ``_extract_signature`` are provided
for reuse across all parsers.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#languageparser-__init__) | constructor | Initialise the parser with a file path and application config. |
| [`parse`](#languageparser-parse) | method | Parse *content* and populate symbol/import lists. |

<a id="languageparser-__init__"></a>

#### `LanguageParser.__init__`

`constructor` | [readmenator/parsers/_base.py:21](../../readmenator/parsers/_base.py#L21)

```python
def __init__(self, filename: str, config: Config) -> None
```

Initialise the parser with a file path and application config.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `filename` | `str` |  | Relative or absolute path of the source file. |
| `config` | `Config` |  | Application-wide configuration settings. |

<a id="languageparser-parse"></a>

#### `LanguageParser.parse`

`method` | [readmenator/parsers/_base.py:36](../../readmenator/parsers/_base.py#L36)

```python
def parse(self, content: str) -> None
```

Parse *content* and populate symbol/import lists.

Splits the source into lines, then delegates to the subclass-
specific ``_extract_specifics`` logic.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `content` | `str` |  |  |

---
