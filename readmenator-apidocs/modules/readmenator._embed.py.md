# `readmenator._embed`

> Source: [readmenator/_embed.py:1](../../readmenator/_embed.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Optional semantic embeddings for the readmenator knowledge graph.

Provides sentence-transformer encoding with HDBSCAN clustering and
UMAP/t-SNE projection when the optional dependencies are installed,
and a deterministic zero-dependency Jaccard fallback otherwise. The
fallback keeps [`near`](readmenator._app.py.md#readmenatorapplication-near) queries and similarity grouping available
offline without extra packages.

## Contents

- **Classes:** [`Embedder`](#embedder)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_readmenator__embed_py__Embedder_encode(["Embedder.encode"])
    n_readmenator__embed_py__Embedder_dependencies_available(["Embedder.dependencies_available"])
    n_readmenator__embed_py__Embedder_encode --> n_readmenator__embed_py__Embedder_dependencies_available
```

## Classes

<a id="embedder"></a>

### `Embedder`

`class` | [readmenator/_embed.py:39](../../readmenator/_embed.py#L39)

```python
class Embedder
```

Encodes scan-text blobs and answers similarity queries.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#embedder-__init__) | constructor | Initialise with application configuration. |
| [`dependencies_available`](#embedder-dependencies_available) | method | Return True when sentence-transformers is importable. |
| [`encode`](#embedder-encode) | method | Encode texts into L2-normalized vectors when available. |
| [`near_jaccard`](#embedder-near_jaccard) | method | Find nearest neighbors with offline Jaccard similarity. |
| [`cluster_jaccard`](#embedder-cluster_jaccard) | method | Group files into similarity clusters with union-find. |
| [`project_jaccard`](#embedder-project_jaccard) | method | Project files to 2D with a deterministic radial layout. |

<a id="embedder-__init__"></a>

#### `Embedder.__init__`

`constructor` | [readmenator/_embed.py:42](../../readmenator/_embed.py#L42)

```python
def __init__(self, config: Config) -> None
```

Initialise with application configuration.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  | Settings for model name and neighbor budgets. |

*Called by:* [`AnalyzerFactory.embedder`](readmenator._pipeline.py.md#analyzerfactory-embedder)

<a id="embedder-dependencies_available"></a>

#### `Embedder.dependencies_available`

`method` | [readmenator/_embed.py:50](../../readmenator/_embed.py#L50)

```python
def dependencies_available(self) -> bool
```

Return True when sentence-transformers is importable.

**Returns:** `bool`

*Called by:* [`Embedder.encode`](#embedder-encode)

<a id="embedder-encode"></a>

#### `Embedder.encode`

`method` | [readmenator/_embed.py:58](../../readmenator/_embed.py#L58)

```python
def encode(self, texts: List[str]) -> List[List[float]]
```

Encode texts into L2-normalized vectors when available.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `texts` | `List[str]` |  | Scan-text blobs to encode. |

**Returns:** `List[List[float]]` - List of float vectors; empty when dependencies are missing.

*Calls:* [`Embedder.dependencies_available`](#embedder-dependencies_available)

<a id="embedder-near_jaccard"></a>

#### `Embedder.near_jaccard`

`method` | [readmenator/_embed.py:75](../../readmenator/_embed.py#L75)

```python
def near_jaccard(self, query: str, corpus: Dict[str, str], top_k: int = 0) -> List[Dict[str, Any]]
```

Find nearest neighbors with offline Jaccard similarity.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `query` | `str` |  | Query scan text or file identifier present in corpus. |
| `corpus` | `Dict[str, str]` |  | Mapping of file identifier to scan text. |
| `top_k` | `int` | `0` | Maximum neighbors to return (0 uses config default). |

**Returns:** `List[Dict[str, Any]]` - Neighbor list sorted by descending similarity score.

<a id="embedder-cluster_jaccard"></a>

#### `Embedder.cluster_jaccard`

`method` | [readmenator/_embed.py:99](../../readmenator/_embed.py#L99)

```python
def cluster_jaccard(self, corpus: Dict[str, str], threshold: float = 0.08) -> List[List[str]]
```

Group files into similarity clusters with union-find.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `corpus` | `Dict[str, str]` |  | Mapping of file identifier to scan text. |
| `threshold` | `float` | `0.08` | Minimum Jaccard similarity to link two files. |

**Returns:** `List[List[str]]` - Clusters with at least EMBED_MIN_CLUSTER_SIZE members.

<a id="embedder-project_jaccard"></a>

#### `Embedder.project_jaccard`

`method` | [readmenator/_embed.py:138](../../readmenator/_embed.py#L138)

```python
def project_jaccard(self, corpus: Dict[str, str]) -> List[Dict[str, Any]]
```

Project files to 2D with a deterministic radial layout.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `corpus` | `Dict[str, str]` |  | Mapping of file identifier to scan text. |

**Returns:** `List[Dict[str, Any]]` - Points normalized to the [-1, 1] square.

---
