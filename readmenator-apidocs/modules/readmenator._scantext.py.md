# `readmenator._scantext`

> Source: [readmenator/_scantext.py:1](../../readmenator/_scantext.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Synthesized scan-text builder for the readmenator knowledge graph.

Flattens per-file metadata (names, symbols, imports, docs, content
snippets) into a single searchable text blob. The blob is the shared
input for YARA-lite matching, provenance auditing, and embedding.

## Contents

- **Classes:** [`ScanTextBuilder`](#scantextbuilder)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_readmenator__scantext_py__ScanTextBuilder_build_corpus(["ScanTextBuilder.build_corpus"])
    n_readmenator__scantext_py__ScanTextBuilder_build_for_node(["ScanTextBuilder.build_for_node"])
    n_readmenator__scantext_py__ScanTextBuilder_build_corpus --> n_readmenator__scantext_py__ScanTextBuilder_build_for_node
```

## Classes

<a id="scantextbuilder"></a>

### `ScanTextBuilder`

`class` | [readmenator/_scantext.py:16](../../readmenator/_scantext.py#L16)

```python
class ScanTextBuilder
```

Builds searchable scan-text blobs from scanned nodes.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#scantextbuilder-__init__) | constructor | Initialise with application configuration. |
| [`build_for_node`](#scantextbuilder-build_for_node) | method | Build the scan-text blob for a single file node. |
| [`build_corpus`](#scantextbuilder-build_corpus) | method | Build scan-text blobs for every node in the corpus. |

<a id="scantextbuilder-__init__"></a>

#### `ScanTextBuilder.__init__`

`constructor` | [readmenator/_scantext.py:19](../../readmenator/_scantext.py#L19)

```python
def __init__(self, config: Config) -> None
```

Initialise with application configuration.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  | Settings for symbol/import/snippet budgets. |

*Called by:* [`AnalyzerFactory.scantext`](readmenator._pipeline.py.md#analyzerfactory-scantext)

<a id="scantextbuilder-build_for_node"></a>

#### `ScanTextBuilder.build_for_node`

`method` | [readmenator/_scantext.py:27](../../readmenator/_scantext.py#L27)

```python
def build_for_node(self, node: Node, content: str = '', imports: Optional[List[str]] = None) -> str
```

Build the scan-text blob for a single file node.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `node` | `Node` |  | Scanned file node with symbols and docs. |
| `content` | `str` | `''` | Optional raw file content for snippet inclusion. |
| `imports` | `Optional[List[str]]` | `None` | Optional raw import strings for the file. |

**Returns:** `str` - Newline-joined scan text with labelled sections.

*Called by:* [`ScanTextBuilder.build_corpus`](#scantextbuilder-build_corpus)

<a id="scantextbuilder-build_corpus"></a>

#### `ScanTextBuilder.build_corpus`

`method` | [readmenator/_scantext.py:67](../../readmenator/_scantext.py#L67)

```python
def build_corpus(self, nodes: List[Node], content_map: Optional[Dict[str, str]] = None, edges: Optional[List[Edge]] = None) -> Dict[str, str]
```

Build scan-text blobs for every node in the corpus.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes. |
| `content_map` | `Optional[Dict[str, str]]` | `None` | Optional mapping of node_id to raw content. |
| `edges` | `Optional[List[Edge]]` | `None` | Optional import edges used as per-file import lists. |

**Returns:** `Dict[str, str]` - Mapping of node_id to scan-text blob.

*Calls:* [`ScanTextBuilder.build_for_node`](#scantextbuilder-build_for_node)

---
