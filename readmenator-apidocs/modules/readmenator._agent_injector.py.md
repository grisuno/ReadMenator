# `readmenator._agent_injector`

> Source: [readmenator/_agent_injector.py:1](../../readmenator/_agent_injector.py#L1) | language `py` | coverage 85.7% | [API index](../index.md)

Injects KNOWLEDGE_BASE.md references into AI agent instruction files.

Detects common AI agent configuration files (AGENTS.md, CLAUDE.md,
.cursorrules, etc.) and appends a pointer to KNOWLEDGE_BASE.md so
that agents can discover project context quickly without manual setup.

The injected text includes instructions for the agent to regenerate
KNOWLEDGE_BASE.md by running readmenator when needed.

## Contents

- **Classes:** [`AgentInjector`](#agentinjector)
- **Functions:** [`ensure_readmenator_installed`](#ensure_readmenator_installed)

## Classes

<a id="agentinjector"></a>

### `AgentInjector`

`class` | [readmenator/_agent_injector.py:142](../../readmenator/_agent_injector.py#L142)

```python
class AgentInjector
```

Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.

Detects common AI agent configuration files (AGENTS.md, CLAUDE.md,
.cursorrules, etc.) and appends a descriptive section pointing to
the knowledge base so agents discover it automatically.

The injected text instructs the agent how to regenerate the KB
by running readmenator when needed.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#agentinjector-__init__) | constructor |  |
| [`inject`](#agentinjector-inject) | method | Inject KB reference into all discovered agent files. |
| [`remove`](#agentinjector-remove) | method | Remove KB injection from all discovered agent files. |
| [`find_agent_files`](#agentinjector-find_agent_files) | method | Public accessor: return all detected agent files. |

<a id="agentinjector-__init__"></a>

#### `AgentInjector.__init__`

`constructor` | [readmenator/_agent_injector.py:153](../../readmenator/_agent_injector.py#L153)

```python
def __init__(self, kb_filename: str = 'KNOWLEDGE_BASE.md', agent_output_dir: str = 'readmenator-agent', agent_files: Optional[Sequence[str]] = None, agent_globs: Optional[Sequence[str]] = None, wiki_output_dir: str = 'readmenator-wiki', agent_heading: str = '', agent_intro: str = '', agent_extra: str = '') -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `kb_filename` | `str` | `'KNOWLEDGE_BASE.md'` |  |
| `agent_output_dir` | `str` | `'readmenator-agent'` |  |
| `agent_files` | `Optional[Sequence[str]]` | `None` |  |
| `agent_globs` | `Optional[Sequence[str]]` | `None` |  |
| `wiki_output_dir` | `str` | `'readmenator-wiki'` |  |
| `agent_heading` | `str` | `''` |  |
| `agent_intro` | `str` | `''` |  |
| `agent_extra` | `str` | `''` |  |

*Called by:* [`AnalyzerFactory.agent_injector`](readmenator._pipeline.py.md#analyzerfactory-agent_injector)

<a id="agentinjector-inject"></a>

#### `AgentInjector.inject`

`method` | [readmenator/_agent_injector.py:173](../../readmenator/_agent_injector.py#L173)

```python
def inject(self, project_root: str) -> int
```

Inject KB reference into all discovered agent files.

Returns the number of agent files actually modified.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  |  |

**Returns:** `int`

<a id="agentinjector-remove"></a>

#### `AgentInjector.remove`

`method` | [readmenator/_agent_injector.py:191](../../readmenator/_agent_injector.py#L191)

```python
def remove(self, project_root: str) -> int
```

Remove KB injection from all discovered agent files.

Returns the number of files actually modified.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  |  |

**Returns:** `int`

<a id="agentinjector-find_agent_files"></a>

#### `AgentInjector.find_agent_files`

`method` | [readmenator/_agent_injector.py:204](../../readmenator/_agent_injector.py#L204)

```python
def find_agent_files(self, project_root: str) -> List[Path]
```

Public accessor: return all detected agent files.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  |  |

**Returns:** `List[Path]`

---

## Functions

<a id="ensure_readmenator_installed"></a>

### `ensure_readmenator_installed`

`function` | [readmenator/_agent_injector.py:120](../../readmenator/_agent_injector.py#L120)

```python
def ensure_readmenator_installed() -> bool
```

Check if readmenator is installed via pip; install it if missing.

Returns True if readmenator is available after the check.

**Returns:** `bool`

---
