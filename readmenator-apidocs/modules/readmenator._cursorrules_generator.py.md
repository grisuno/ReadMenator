# `readmenator._cursorrules_generator`

> Source: [readmenator/_cursorrules_generator.py:1](../../readmenator/_cursorrules_generator.py#L1) | language `py` | coverage 75.0% | [API index](../index.md)

Dynamic .cursorrules generator for the readmenator knowledge graph.

Reads architectural analysis results and linter violations to produce
a deterministic .cursorrules file that feeds structural constraints
back into AI coding assistants.

## Contents

- **Classes:** [`CursorRulesGenerator`](#cursorrulesgenerator)

## Classes

<a id="cursorrulesgenerator"></a>

### `CursorRulesGenerator`

`class` | [readmenator/_cursorrules_generator.py:18](../../readmenator/_cursorrules_generator.py#L18)

```python
class CursorRulesGenerator
```

Generates a .cursorrules file from architectural analysis.

Combines base rules, detected layer constraints, and active
linter violations into a deterministic ruleset for AI assistants.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#cursorrulesgenerator-__init__) | constructor |  |
| [`generate`](#cursorrulesgenerator-generate) | method | Generate the .cursorrules content string. |

<a id="cursorrulesgenerator-__init__"></a>

#### `CursorRulesGenerator.__init__`

`constructor` | [readmenator/_cursorrules_generator.py:25](../../readmenator/_cursorrules_generator.py#L25)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`readmenatorApplication.generate_cursorrules`](readmenator._app.py.md#readmenatorapplication-generate_cursorrules)

<a id="cursorrulesgenerator-generate"></a>

#### `CursorRulesGenerator.generate`

`method` | [readmenator/_cursorrules_generator.py:28](../../readmenator/_cursorrules_generator.py#L28)

```python
def generate(self, nodes: Any, edges: Any, analysis: Optional[AnalysisResult] = None, layers: Optional[Dict[str, str]] = None, violations: Optional[List[LinterViolation]] = None, project_root: Optional[str] = None) -> str
```

Generate the .cursorrules content string.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `Any` |  | Scanned file nodes. |
| `edges` | `Any` |  | Import edges. |
| `analysis` | `Optional[AnalysisResult]` | `None` | Optional analysis results. |
| `layers` | `Optional[Dict[str, str]]` | `None` | Optional layer mapping. |
| `violations` | `Optional[List[LinterViolation]]` | `None` | Optional linter violations. |
| `project_root` | `Optional[str]` | `None` | Optional project root for file output. |

**Returns:** `str` - The generated .cursorrules content as a string.

*Called by:* [`readmenatorApplication.generate_cursorrules`](readmenator._app.py.md#readmenatorapplication-generate_cursorrules)

---
