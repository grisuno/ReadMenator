# `readmenator._scanner`

> Source: [readmenator/_scanner.py:1](../../readmenator/_scanner.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Secure polyglot directory traversal and file analysis.

The scanner walks a directory tree, applies security and size checks,
resolves each supported file through ParserFactory, and returns a
flat list of Node and Edge objects that form the knowledge graph.

## Contents

- **Classes:** [`PolyglotScanner`](#polyglotscanner)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_readmenator__scanner_py__PolyglotScanner_scan_contents(["PolyglotScanner.scan_contents"])
    n_readmenator__scanner_py__PolyglotScanner_is_generated(["PolyglotScanner.is_generated"])
    n_readmenator__scanner_py__PolyglotScanner_scan_contents --> n_readmenator__scanner_py__PolyglotScanner_is_generated
```

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
| [`is_generated`](#polyglotscanner-is_generated) | method | Return ``True`` for artifacts readmenator itself wrote into the project. |
| [`scan`](#polyglotscanner-scan) | method | Walk *root* recursively and produce (nodes, edges) for the graph. |
| [`scan_with_content`](#polyglotscanner-scan_with_content) | method | Scan and also return raw file contents for deeper analysis. |
| [`scan_contents`](#polyglotscanner-scan_contents) | method | Scan an in-memory file map instead of the filesystem. |

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

<a id="polyglotscanner-is_generated"></a>

#### `PolyglotScanner.is_generated`

`method` | [readmenator/_scanner.py:57](../../readmenator/_scanner.py#L57)

```python
def is_generated(self, rel_path: Path) -> bool
```

Return ``True`` for artifacts readmenator itself wrote into the project.

Rescanning its own output (agent docs, wiki, rules, maps, refactor
scripts) would feed generated noise back into the graph and skew
indexes, centrality, and purposes on every rebuild.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `rel_path` | `Path` |  | Path relative to the scan root. |

**Returns:** `bool` - Whether the path belongs to a readmenator-generated artifact.

*Called by:* [`PolyglotScanner.scan_contents`](#polyglotscanner-scan_contents)

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

<a id="polyglotscanner-scan_contents"></a>

#### `PolyglotScanner.scan_contents`

`method` | [readmenator/_scanner.py:360](../../readmenator/_scanner.py#L360)

```python
def scan_contents(self, contents: Dict[str, str]) -> Tuple[List[Node], List[Edge], Dict[str, str]]
```

Scan an in-memory file map instead of the filesystem.

Used to replay historical trees read from git: the same parsers,
the same file-level doc extraction, the same generated-output
filtering, but over contents that already live in memory.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `contents` | `Dict[str, str]` |  | Mapping of relative file path to raw file content. |

**Returns:** `Tuple[List[Node], List[Edge], Dict[str, str]]` - Tuple of (list of Node, list of Edge, content map).

*Calls:* [`PolyglotScanner.is_generated`](#polyglotscanner-is_generated)

---
