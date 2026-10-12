# `readmenator._wiki`

> Source: [readmenator/_wiki.py:1](../../readmenator/_wiki.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Deterministic agent wiki generator for readmenator.

Builds a navigable, progressively disclosed wiki on top of the scanned
knowledge graph. The layout mirrors the Karpathy LLM Wiki Pattern used
by graphify and second-brain (index plus one page per community plus
machine-readable connections), but every page is synthesised
deterministically from static analysis with zero LLM calls, zero
tokens, and an honest confidence trail.

Output layout::

    readmenator-wiki/
    ├── index.md              # entry point: overview plus all links
    ├── community_<id>_<slug>.md  # one synthesis page per community
    ├── connections.json      # typed bridges with strength and confidence
    ├── queries.md            # suggested questions plus answer log
    └── REPORT.md             # honest audit: coverage, confidence, limits

## Contents

- **Classes:** [`WikiGenerator`](#wikigenerator)
- **Functions:** [`existing_ids`](#existing_ids)

## Classes

<a id="wikigenerator"></a>

### `WikiGenerator`

`class` | [readmenator/_wiki.py:86](../../readmenator/_wiki.py#L86)

```python
class WikiGenerator
```

Generates the navigable agent wiki from scanned topology.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#wikigenerator-__init__) | constructor | Store configuration for wiki output limits and paths. |
| [`generate`](#wikigenerator-generate) | method | Write all wiki files and return the output directory path. |
| [`lint`](#wikigenerator-lint) | method | Check wiki health and return a list of issue descriptions. |

<a id="wikigenerator-__init__"></a>

#### `WikiGenerator.__init__`

`constructor` | [readmenator/_wiki.py:89](../../readmenator/_wiki.py#L89)

```python
def __init__(self, config: Config) -> None
```

Store configuration for wiki output limits and paths.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`AnalyzerFactory.wiki`](readmenator._pipeline.py.md#analyzerfactory-wiki)

<a id="wikigenerator-generate"></a>

#### `WikiGenerator.generate`

`method` | [readmenator/_wiki.py:94](../../readmenator/_wiki.py#L94)

```python
def generate(self, nodes: List[Node], edges: List[Edge], resolved_edges: Optional[List[Edge]], analysis: Optional[AnalysisResult], layers: Optional[Dict[str, str]], findings: List[SecurityFinding], analysis_v2: Optional[AnalysisResultV2], project_root: str) -> str
```

Write all wiki files and return the output directory path.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  |  |
| `edges` | `List[Edge]` |  |  |
| `resolved_edges` | `Optional[List[Edge]]` |  |  |
| `analysis` | `Optional[AnalysisResult]` |  |  |
| `layers` | `Optional[Dict[str, str]]` |  |  |
| `findings` | `List[SecurityFinding]` |  |  |
| `analysis_v2` | `Optional[AnalysisResultV2]` |  |  |
| `project_root` | `str` |  |  |

**Returns:** `str`

<a id="wikigenerator-lint"></a>

#### `WikiGenerator.lint`

`method` | [readmenator/_wiki.py:219](../../readmenator/_wiki.py#L219)

```python
def lint(self, project_root: str) -> List[str]
```

Check wiki health and return a list of issue descriptions.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  |  |

**Returns:** `List[str]`

---

## Functions

<a id="existing_ids"></a>

### `existing_ids`

`function` | [readmenator/_wiki.py:62](../../readmenator/_wiki.py#L62)

```python
def existing_ids(connections: List[Dict[str, object]]) -> Set[frozenset]
```

Return community id pairs already linked, to avoid duplicate edges.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `connections` | `List[Dict[str, object]]` |  |  |

**Returns:** `Set[frozenset]`

---
