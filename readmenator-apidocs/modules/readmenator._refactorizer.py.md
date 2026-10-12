# `readmenator._refactorizer`

> Source: [readmenator/_refactorizer.py:1](../../readmenator/_refactorizer.py#L1) | language `py` | coverage 60.0% | [API index](../index.md)

Monolithic file refactoring planner for the readmenator knowledge graph.

Identifies large files exceeding configurable thresholds and generates
deterministic refactoring plans based on symbol extraction and
cohesive cluster detection. Never auto-executes; only produces plans.

## Contents

- **Classes:** [`MonolithRefactorizer`](#monolithrefactorizer)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_readmenator__refactorizer_py__MonolithRefactorizer_analyze(["MonolithRefactorizer.analyze"])
    n_readmenator__models_py__RefactoringPlan["_models.RefactoringPlan"]
    n_readmenator__refactorizer_py__MonolithRefactorizer_analyze -.-> n_readmenator__models_py__RefactoringPlan
```

## Classes

<a id="monolithrefactorizer"></a>

### `MonolithRefactorizer`

`class` | [readmenator/_refactorizer.py:24](../../readmenator/_refactorizer.py#L24)

```python
class MonolithRefactorizer
```

Generates refactoring plans for monolithic files.

Analyzes files exceeding the line threshold, extracts symbol
boundaries, detects cohesive clusters via import analysis, and
produces structured refactoring plans without auto-execution.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#monolithrefactorizer-__init__) | constructor |  |
| [`analyze`](#monolithrefactorizer-analyze) | method | Identify monolithic files and generate refactoring plans. |
| [`generate_script`](#monolithrefactorizer-generate_script) | method |  |

<a id="monolithrefactorizer-__init__"></a>

#### `MonolithRefactorizer.__init__`

`constructor` | [readmenator/_refactorizer.py:32](../../readmenator/_refactorizer.py#L32)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`readmenatorApplication.refactor_monolith`](readmenator._app.py.md#readmenatorapplication-refactor_monolith)

<a id="monolithrefactorizer-analyze"></a>

#### `MonolithRefactorizer.analyze`

`method` | [readmenator/_refactorizer.py:35](../../readmenator/_refactorizer.py#L35)

```python
def analyze(self, nodes: List[Node], edges: List[Edge], resolved_edges: Optional[List[Edge]] = None, content_map: Optional[Dict[str, str]] = None) -> List[RefactoringPlan]
```

Identify monolithic files and generate refactoring plans.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes. |
| `edges` | `List[Edge]` |  | Import edges. |
| `resolved_edges` | `Optional[List[Edge]]` | `None` | Optional resolved-import edges. |
| `content_map` | `Optional[Dict[str, str]]` | `None` | Optional mapping from node_id to file content. |

**Returns:** `List[RefactoringPlan]` - List of RefactoringPlan instances for files needing refactoring.

*Calls:* [`RefactoringPlan`](readmenator._models.py.md#refactoringplan)

*Called by:* [`readmenatorApplication.refactor_monolith`](readmenator._app.py.md#readmenatorapplication-refactor_monolith)

<a id="monolithrefactorizer-generate_script"></a>

#### `MonolithRefactorizer.generate_script`

`method` | [readmenator/_refactorizer.py:156](../../readmenator/_refactorizer.py#L156)

```python
def generate_script(self, plan: RefactoringPlan, project_root: str) -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `plan` | `RefactoringPlan` |  |  |
| `project_root` | `str` |  |  |

**Returns:** `str`

*Called by:* [`readmenatorApplication.refactor_monolith`](readmenator._app.py.md#readmenatorapplication-refactor_monolith)

---
