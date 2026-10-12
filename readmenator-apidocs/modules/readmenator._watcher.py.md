# `readmenator._watcher`

> Source: [readmenator/_watcher.py:1](../../readmenator/_watcher.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Filesystem watcher for auto-rebuilding the knowledge base.

Monitors the project directory for file changes and triggers
automatic regeneration of KNOWLEDGE_BASE.md. Uses polling with
configurable interval to avoid external dependencies.

## Contents

- **Classes:** [`DirectoryWatcher`](#directorywatcher)

## Classes

<a id="directorywatcher"></a>

### `DirectoryWatcher`

`class` | [readmenator/_watcher.py:21](../../readmenator/_watcher.py#L21)

```python
class DirectoryWatcher
```

Polling-based directory watcher for auto-rebuild on changes.

Computes a combined hash of all tracked files (filenames + sizes)
and triggers a callback when the hash changes. Uses polling to
avoid external dependencies like watchdog or inotify.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#directorywatcher-__init__) | constructor | Initialise the watcher for a project root. |
| [`start`](#directorywatcher-start) | method | Start watching the directory (blocking). |
| [`stop`](#directorywatcher-stop) | method | Stop watching. |

<a id="directorywatcher-__init__"></a>

#### `DirectoryWatcher.__init__`

`constructor` | [readmenator/_watcher.py:29](../../readmenator/_watcher.py#L29)

```python
def __init__(self, root: str, config: Config, callback: Callable[[], None], interval_seconds: float = 3.0)
```

Initialise the watcher for a project root.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `root` | `str` |  | Project directory to watch. |
| `config` | `Config` |  | Application configuration. |
| `callback` | `Callable[[], None]` |  | Function called when changes are detected. |
| `interval_seconds` | `float` | `3.0` | Polling interval in seconds. |

*Called by:* [`readmenatorApplication.watch`](readmenator._app.py.md#readmenatorapplication-watch)

<a id="directorywatcher-start"></a>

#### `DirectoryWatcher.start`

`method` | [readmenator/_watcher.py:80](../../readmenator/_watcher.py#L80)

```python
def start(self) -> None
```

Start watching the directory (blocking).

*Called by:* [`readmenatorApplication.watch`](readmenator._app.py.md#readmenatorapplication-watch)

<a id="directorywatcher-stop"></a>

#### `DirectoryWatcher.stop`

`method` | [readmenator/_watcher.py:97](../../readmenator/_watcher.py#L97)

```python
def stop(self) -> None
```

Stop watching.

---
