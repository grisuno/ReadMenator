# `readmenator._scanner`

> Source: [readmenator/_scanner.py:1](../../readmenator/_scanner.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Secure polyglot directory traversal and file analysis.

The scanner walks a directory tree, applies security and size checks,
resolves each supported file through ParserFactory, and returns a
flat list of Node and Edge objects that form the knowledge graph.

## Contents

- **Classes:** [`PolyglotScanner`](#polyglotscanner)

## Classes

<a id="polyglotscanner"></a>

### `PolyglotScanner`

`class` | [readmenator/_scanner.py:28](../../readmenator/_scanner.py#L28)

```python
class PolyglotScanner
```

Recursive directory scanner with security and size guards.

Rejects symlinks, enforces file-size and directory-depth limits,
skips ignored directories, and silently catches parse errors
so a single misbehaving file never breaks the full scan.

Supports privacy mode (strips snippets and docstrings) and
gitignore-aware scanning for more accurate project coverage.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#polyglotscanner-__init__) | constructor | Initialise the scanner with application configuration. |
| [`scan`](#polyglotscanner-scan) | method | Walk *root* recursively and produce (nodes, edges) for the graph. |
| [`scan_with_content`](#polyglotscanner-scan_with_content) | method | Scan and also return raw file contents for deeper analysis. |

<a id="polyglotscanner-__init__"></a>

#### `PolyglotScanner.__init__`

`constructor` | [readmenator/_scanner.py:39](../../readmenator/_scanner.py#L39)

```python
def __init__(self, config: Config) -> None
```

Initialise the scanner with application configuration.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  | Settings including ignore dirs, size limits, etc. |

*Called by:* [`AnalyzerFactory.scanner`](readmenator._pipeline.py.md#analyzerfactory-scanner)

<a id="polyglotscanner-scan"></a>

#### `PolyglotScanner.scan`

`method` | [readmenator/_scanner.py:262](../../readmenator/_scanner.py#L262)

```python
def scan(self, root: Path) -> Tuple[List[Node], List[Edge]]
```

Walk *root* recursively and produce (nodes, edges) for the graph.

Security checks (symlinks, size, depth, ignore dirs) are applied
per file. Parse failures are silently caught so a single broken
file never blocks the rest of the scan.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `root` | `Path` |  |  |

**Returns:** `Tuple[List[Node], List[Edge]]` - A tuple of (list of Node, list of Edge). Edges represent
``imports`` relationships between scanned files.

<a id="polyglotscanner-scan_with_content"></a>

#### `PolyglotScanner.scan_with_content`

`method` | [readmenator/_scanner.py:276](../../readmenator/_scanner.py#L276)

```python
def scan_with_content(self, root: Path) -> Tuple[List[Node], List[Edge], Dict[str, str]]
```

Scan and also return raw file contents for deeper analysis.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `root` | `Path` |  |  |

**Returns:** `Tuple[List[Node], List[Edge], Dict[str, str]]` - Tuple of (nodes, edges, content_map) where content_map maps
node_id to raw file content.

---
