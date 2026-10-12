# `readmenator._cpg`

> Source: [readmenator/_cpg.py:1](../../readmenator/_cpg.py#L1) | language `py` | coverage 75.0% | [API index](../index.md)

Code Property Graph (CPG) generator emitting JSON-LD for AI agents.

Merges symbols, call, import, and inheritance edges, content hashes, and
optional analysis metadata into one embeddable, zero-token graph.

## Contents

- **Classes:** [`CodePropertyGraph`](#codepropertygraph)

## Classes

<a id="codepropertygraph"></a>

### `CodePropertyGraph`

`class` | [readmenator/_cpg.py:16](../../readmenator/_cpg.py#L16)

```python
class CodePropertyGraph
```

Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.

Produces a structured representation merging AST-level symbol data,
control-flow edges (calls), data-flow edges (imports), inheritance
relationships, and security findings (with MITRE ATT&CK mappings)
into a single machine-readable document. Designed to be embedded in
KNOWLEDGE_BASE.md for zero-token agent context.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#codepropertygraph-__init__) | constructor |  |
| [`generate`](#codepropertygraph-generate) | method | Generate the CPG JSON-LD string embeddable in markdown. |

<a id="codepropertygraph-__init__"></a>

#### `CodePropertyGraph.__init__`

`constructor` | [readmenator/_cpg.py:26](../../readmenator/_cpg.py#L26)

```python
def __init__(self, privacy_mode: bool = False, cpg_context: str = '') -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `privacy_mode` | `bool` | `False` |  |
| `cpg_context` | `str` | `''` |  |

*Called by:* [`DocumentationGenerator.__init__`](readmenator._documentation.py.md#documentationgenerator-__init__), [`AnalyzerFactory.cpg`](readmenator._pipeline.py.md#analyzerfactory-cpg)

<a id="codepropertygraph-generate"></a>

#### `CodePropertyGraph.generate`

`method` | [readmenator/_cpg.py:30](../../readmenator/_cpg.py#L30)

```python
def generate(self, nodes: List[Node], edges: List[Edge], resolved_edges: Optional[List[Edge]] = None, analysis: Optional[AnalysisResult] = None, findings: Optional[List[SecurityFinding]] = None) -> str
```

Generate the CPG JSON-LD string embeddable in markdown.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes. |
| `edges` | `List[Edge]` |  | Import edges. |
| `resolved_edges` | `Optional[List[Edge]]` | `None` | Optional resolved-import edges. |
| `analysis` | `Optional[AnalysisResult]` | `None` | Optional analysis results for metadata. |
| `findings` | `Optional[List[SecurityFinding]]` | `None` | Optional security findings with MITRE ATT&CK IDs. |

**Returns:** `str` - Compact JSON-LD string with @context, nodes, edges, analysis,
and mitre_attack metadata.

---
