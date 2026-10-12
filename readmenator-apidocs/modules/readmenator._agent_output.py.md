# `readmenator._agent_output`

> Source: [readmenator/_agent_output.py:1](../../readmenator/_agent_output.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Agent-friendly output generator for ReadMenator.

Generates grep-optimized, flat-markdown files in a dedicated output
directory.  File names for per-subsystem files are **inferred** from the
project's directory structure, never hardcoded.  The generated files are
designed to be consumed by AI agents that perform ``grep`` / ``read``
operations and need queryable, small-context documents.

Every document is capped at `[`AGENT_OUTPUT_MAX_LINES`](readmenator._config.py.md#config-agent_output_max_lines)`: oversized
documents are split on section boundaries into ``NAME.md``,
``NAME_p2.md``, ... with the table header repeated on each page, so a
``grep`` over ``NAME*.md`` still sees every line and a single read never
blows an agent's context window.

Output layout::

    readmenator-agent/
    ├── MANIFEST.json         # freshness (git commit), read order, token costs
    ├── INDEX.md              # file -> purpose -> blast radius map
    ├── SYMBOLS.md            # one line per symbol
    ├── ARCHITECTURE.md       # dependency pairs (flat list)
    ├── SECURITY.md           # findings by severity
    ├── API.md                # public functions, one line each
    ├── GOTCHAS.md            # "don't change X because Y"
    ├── recipes/
    │   └── *.md              # actionable task blocks
    └── KB_<subsystem>.md     # 1 file per inferred subsystem

## Contents

- **Classes:** [`AgentOutputGenerator`](#agentoutputgenerator)

## Classes

<a id="agentoutputgenerator"></a>

### `AgentOutputGenerator`

`class` | [readmenator/_agent_output.py:70](../../readmenator/_agent_output.py#L70)

```python
class AgentOutputGenerator
```

Generates agent-friendly, grep-optimised output files.

All output is plain Markdown -- no JSON wrapping, no fenced code
blocks around data structures.  Every line is greppable.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#agentoutputgenerator-__init__) | constructor | Store configuration for output paths and size budgets. |
| [`generate`](#agentoutputgenerator-generate) | method | Write all agent output files and return the output directory path. |

<a id="agentoutputgenerator-__init__"></a>

#### `AgentOutputGenerator.__init__`

`constructor` | [readmenator/_agent_output.py:77](../../readmenator/_agent_output.py#L77)

```python
def __init__(self, config: Config) -> None
```

Store configuration for output paths and size budgets.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`AnalyzerFactory.agent_output`](readmenator._pipeline.py.md#analyzerfactory-agent_output)

<a id="agentoutputgenerator-generate"></a>

#### `AgentOutputGenerator.generate`

`method` | [readmenator/_agent_output.py:81](../../readmenator/_agent_output.py#L81)

```python
def generate(self, nodes: List[Node], edges: List[Edge], resolved_edges: List[Edge], analysis: Optional[AnalysisResult], analysis_v2: Optional[AnalysisResultV2], findings: List[SecurityFinding], layers: Dict[str, str], project_root: str) -> str
```

Write all agent output files and return the output directory path.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  |  |
| `edges` | `List[Edge]` |  |  |
| `resolved_edges` | `List[Edge]` |  |  |
| `analysis` | `Optional[AnalysisResult]` |  |  |
| `analysis_v2` | `Optional[AnalysisResultV2]` |  |  |
| `findings` | `List[SecurityFinding]` |  |  |
| `layers` | `Dict[str, str]` |  |  |
| `project_root` | `str` |  |  |

**Returns:** `str`

---
