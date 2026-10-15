# `readmenator._readme_injector`

> Source: [readmenator/_readme_injector.py:1](../../readmenator/_readme_injector.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Injects a knowledge base section into the project README (Markdown or RST).

## Contents

- **Classes:** [`ReadmeInjector`](#readmeinjector)

## Classes

<a id="readmeinjector"></a>

### `ReadmeInjector`

`class` | [readmenator/_readme_injector.py:134](../../readmenator/_readme_injector.py#L134)

```python
class ReadmeInjector
```

Injects a link to KNOWLEDGE_BASE.md into the project README.

Detects the project's README file, checks if injection is already
present, and appends a descriptive section about the knowledge base
so that both human developers and AI agents know it exists.

When the anchor tag is missing the section is created; when the tag
exists but the text is outdated it is replaced in place.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#readmeinjector-__init__) | constructor | Initialise the injector with output locations. |
| [`inject`](#readmeinjector-inject) | method | Inject or refresh the knowledge base section in the README. |
| [`remove`](#readmeinjector-remove) | method | Remove the injected section from the README. |

<a id="readmeinjector-__init__"></a>

#### `ReadmeInjector.__init__`

`constructor` | [readmenator/_readme_injector.py:145](../../readmenator/_readme_injector.py#L145)

```python
def __init__(self, kb_filename: str = 'KNOWLEDGE_BASE.md', agent_output_dir: str = 'readmenator-agent', wiki_output_dir: str = 'readmenator-wiki', graphrag_output_dir: str = 'readmenator-graphrag', maps_output_dir: str = 'readmenator-maps', pages_dir: str = 'docs', components_output_dir: str = 'readmenator-diagrams', rules_output_dir: str = 'readmenator-rules', video_output: str = 'readmenator.mp4', cursorrules_output: str = '.cursorrules', sarif_output: str = 'readmenator_audit.sarif', cache_dir: str = '.readmenator_cache', skills_dir: str = '.claude/skills', llms_txt: str = 'llms.txt', forcegraph_output: str = 'graph-force.html', bundlegraph_output: str = 'graph-bundle.html', apidocs_output_dir: str = 'readmenator-apidocs', readme_heading: str = '', readme_intro: str = '', readme_agents_line: str = '', readme_developers_line: str = '', readme_regen_command: str = '') -> None
```

Initialise the injector with output locations.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `kb_filename` | `str` | `'KNOWLEDGE_BASE.md'` | Knowledge base filename. |
| `agent_output_dir` | `str` | `'readmenator-agent'` | Agent output directory. |
| `wiki_output_dir` | `str` | `'readmenator-wiki'` | Wiki output directory. |
| `graphrag_output_dir` | `str` | `'readmenator-graphrag'` | GraphRAG output directory. |
| `maps_output_dir` | `str` | `'readmenator-maps'` | Interactive maps output directory. |
| `pages_dir` | `str` | `'docs'` | Static site output directory. |
| `components_output_dir` | `str` | `'readmenator-diagrams'` | Component diagram output directory. |
| `rules_output_dir` | `str` | `'readmenator-rules'` | Suggested rules output directory. |
| `video_output` | `str` | `'readmenator.mp4'` | Overview video filename. |
| `cursorrules_output` | `str` | `'.cursorrules'` | Generated cursor rules filename. |
| `sarif_output` | `str` | `'readmenator_audit.sarif'` | SARIF audit filename. |
| `cache_dir` | `str` | `'.readmenator_cache'` | Incremental cache directory. |
| `skills_dir` | `str` | `'.claude/skills'` | Packaged agent skills target directory. |
| `llms_txt` | `str` | `'llms.txt'` | Site llms.txt filename. |
| `forcegraph_output` | `str` | `'graph-force.html'` | Force-graph explorer filename. |
| `bundlegraph_output` | `str` | `'graph-bundle.html'` | Edge bundle explorer filename. |
| `apidocs_output_dir` | `str` | `'readmenator-apidocs'` | API reference output directory. |
| `readme_heading` | `str` | `''` | Override for the section heading ("" = built-in). |
| `readme_intro` | `str` | `''` | Override for the opening paragraph ("" = built-in). |
| `readme_agents_line` | `str` | `''` | Override for the closing agents line ("" = built-in). |
| `readme_developers_line` | `str` | `''` | Override for the closing developers line ("" = built-in). |
| `readme_regen_command` | `str` | `''` | Override for the rebuild command ("" = built-in). |

*Called by:* [`AnalyzerFactory.readme_injector`](readmenator._pipeline.py.md#analyzerfactory-readme_injector)

<a id="readmeinjector-inject"></a>

#### `ReadmeInjector.inject`

`method` | [readmenator/_readme_injector.py:219](../../readmenator/_readme_injector.py#L219)

```python
def inject(self, project_root: str) -> bool
```

Inject or refresh the knowledge base section in the README.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  | Project root directory holding the README. |

**Returns:** `bool` - True when the README was created or modified, False otherwise.

<a id="readmeinjector-remove"></a>

#### `ReadmeInjector.remove`

`method` | [readmenator/_readme_injector.py:311](../../readmenator/_readme_injector.py#L311)

```python
def remove(self, project_root: str) -> bool
```

Remove the injected section from the README.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  | Project root directory holding the README. |

**Returns:** `bool` - True when a section was removed, False otherwise.

---
