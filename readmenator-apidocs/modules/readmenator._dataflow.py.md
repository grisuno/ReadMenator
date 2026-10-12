# `readmenator._dataflow`

> Source: [readmenator/_dataflow.py:1](../../readmenator/_dataflow.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Procedural intra-function dataflow analysis for readmenator.

Detects classic logic bug classes without tokens, types, or control-flow
graphs: use of uninitialized locals, dead stores (assigned but never
read), and unchecked allocator results. Pure regex over function body
spans derived from parsed symbol line ranges. Every finding is marked
INFERRED: heuristics trade recall for reviewable, line-grounded leads.

## Contents

- **Classes:** [`DataflowAnalyzer`](#dataflowanalyzer)

## Classes

<a id="dataflowanalyzer"></a>

### `DataflowAnalyzer`

`class` | [readmenator/_dataflow.py:122](../../readmenator/_dataflow.py#L122)

```python
class DataflowAnalyzer
```

Regex-based intra-function dataflow checker over scanned content.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#dataflowanalyzer-__init__) | constructor | Store configuration for enable flag and issue caps. |
| [`analyze`](#dataflowanalyzer-analyze) | method | Check every function body span and return capped issues. |

<a id="dataflowanalyzer-__init__"></a>

#### `DataflowAnalyzer.__init__`

`constructor` | [readmenator/_dataflow.py:125](../../readmenator/_dataflow.py#L125)

```python
def __init__(self, config: Config) -> None
```

Store configuration for enable flag and issue caps.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`AnalyzerFactory.dataflow`](readmenator._pipeline.py.md#analyzerfactory-dataflow)

<a id="dataflowanalyzer-analyze"></a>

#### `DataflowAnalyzer.analyze`

`method` | [readmenator/_dataflow.py:129](../../readmenator/_dataflow.py#L129)

```python
def analyze(self, nodes: List[Node], content_map: Optional[Dict[str, str]]) -> List[DataflowIssue]
```

Check every function body span and return capped issues.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  |  |
| `content_map` | `Optional[Dict[str, str]]` |  |  |

**Returns:** `List[DataflowIssue]`

---
