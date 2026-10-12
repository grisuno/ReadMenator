# `readmenator._mermaid`

> Source: [readmenator/_mermaid.py:1](../../readmenator/_mermaid.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Mermaid graph renderer with intelligent pruning.

Converts the internal Node/Edge graph into a Mermaid flowchart
(string) suitable for embedding in Markdown. Handles node limits,
deduplication, CSS-like class styling, internal import edges, and
community subgraphs.

## Contents

- **Classes:** [`MermaidRenderer`](#mermaidrenderer)

## Classes

<a id="mermaidrenderer"></a>

### `MermaidRenderer`

`class` | [readmenator/_mermaid.py:17](../../readmenator/_mermaid.py#L17)

```python
class MermaidRenderer
```

Renders a knowledge graph to Mermaid JS flowchart syntax.

Nodes are ordered by import count and symbol richness; the top
``max_nodes`` entries are included. External dependencies appear
as dashed boxes. Internal import edges are solid arrows.
Community subgraphs group related files when analysis is available.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#mermaidrenderer-__init__) | constructor | Initialise rendering budgets and styles. |
| [`render`](#mermaidrenderer-render) | method | Produce a Mermaid flowchart string and a truncation flag. |

<a id="mermaidrenderer-__init__"></a>

#### `MermaidRenderer.__init__`

`constructor` | [readmenator/_mermaid.py:26](../../readmenator/_mermaid.py#L26)

```python
def __init__(self, max_nodes: int = 300, max_symbols_per_file: int = 5, module_style: str = 'fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff', class_style: str = 'fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff', function_style: str = 'fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa', external_style: str = 'fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa', internal_edge_style: str = 'stroke:#88aaff,stroke-width:1px', max_edges: int = 480, max_internal_edges: int = 100) -> None
```

Initialise rendering budgets and styles.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `max_nodes` | `int` | `300` | Maximum file nodes drawn. |
| `max_symbols_per_file` | `int` | `5` | Symbol budget per file. |
| `module_style` | `str` | `'fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff'` | classDef style for files. |
| `class_style` | `str` | `'fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff'` | classDef style for class-like symbols. |
| `function_style` | `str` | `'fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa'` | classDef style for callables. |
| `external_style` | `str` | `'fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa'` | classDef style for external imports. |
| `internal_edge_style` | `str` | `'stroke:#88aaff,stroke-width:1px'` | Style for internal import edges. |
| `max_edges` | `int` | `480` | Total edge budget; Mermaid refuses to render more than 500 edges, so the default stays below that hard limit. |
| `max_internal_edges` | `int` | `100` | Budget for project-internal import edges. |

*Called by:* [`DocumentationGenerator.__init__`](readmenator._documentation.py.md#documentationgenerator-__init__)

<a id="mermaidrenderer-render"></a>

#### `MermaidRenderer.render`

`method` | [readmenator/_mermaid.py:74](../../readmenator/_mermaid.py#L74)

```python
def render(self, nodes: List[Node], edges: List[Edge], resolved_edges: Optional[List[Edge]] = None, analysis: Optional[AnalysisResult] = None) -> Tuple[str, bool]
```

Produce a Mermaid flowchart string and a truncation flag.

Nodes are sorted by import popularity, then by symbol count.
Internal import edges (between project files) are rendered as
solid arrows when *resolved_edges* is provided. Community
subgraphs wrap related files when *analysis* is given.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  |  |
| `edges` | `List[Edge]` |  |  |
| `resolved_edges` | `Optional[List[Edge]]` | `None` |  |
| `analysis` | `Optional[AnalysisResult]` | `None` |  |

**Returns:** `Tuple[str, bool]` - Tuple of (Mermaid source string, is_truncated bool).

*Called by:* [`DocumentationGenerator.generate`](readmenator._documentation.py.md#documentationgenerator-generate)

---
