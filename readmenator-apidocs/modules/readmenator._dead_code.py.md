# `readmenator._dead_code`

> Source: [readmenator/_dead_code.py:1](../../readmenator/_dead_code.py#L1) | language `py` | coverage 75.0% | [API index](../index.md)

Dead code detection for the readmenator knowledge graph.

Identifies orphaned symbols with zero in-degree in the resolved import
graph, excluding known entry points. Generates structured reports
without auto-deleting any code.

## Contents

- **Classes:** [`DeadCodeStripper`](#deadcodestripper)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_readmenator__dead_code_py__DeadCodeStripper_identify(["DeadCodeStripper.identify"])
    n_readmenator__models_py__DeadCodeReport["_models.DeadCodeReport"]
    n_readmenator__dead_code_py__DeadCodeStripper_identify -.-> n_readmenator__models_py__DeadCodeReport
```

## Classes

<a id="deadcodestripper"></a>

### `DeadCodeStripper`

`class` | [readmenator/_dead_code.py:17](../../readmenator/_dead_code.py#L17)

```python
class DeadCodeStripper
```

Identifies dead code symbols in the knowledge graph.

Builds an in-degree map from resolved import edges, then flags
symbols that are never imported by any other file. Known entry
points are excluded from the dead code report.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#deadcodestripper-__init__) | constructor |  |
| [`identify`](#deadcodestripper-identify) | method | Identify dead code symbols with zero in-degree. |

<a id="deadcodestripper-__init__"></a>

#### `DeadCodeStripper.__init__`

`constructor` | [readmenator/_dead_code.py:25](../../readmenator/_dead_code.py#L25)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`readmenatorApplication.strip_dead_code`](readmenator._app.py.md#readmenatorapplication-strip_dead_code)

<a id="deadcodestripper-identify"></a>

#### `DeadCodeStripper.identify`

`method` | [readmenator/_dead_code.py:28](../../readmenator/_dead_code.py#L28)

```python
def identify(self, nodes: List[Node], edges: List[Edge], resolved_edges: Optional[List[Edge]] = None) -> List[DeadCodeReport]
```

Identify dead code symbols with zero in-degree.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes with symbols. |
| `edges` | `List[Edge]` |  | Import edges. |
| `resolved_edges` | `Optional[List[Edge]]` | `None` | Optional resolved-import edges. |

**Returns:** `List[DeadCodeReport]` - List of DeadCodeReport instances for orphaned symbols.

*Calls:* [`DeadCodeReport`](readmenator._models.py.md#deadcodereport)

*Called by:* [`readmenatorApplication.strip_dead_code`](readmenator._app.py.md#readmenatorapplication-strip_dead_code)

---
