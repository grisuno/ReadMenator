# `readmenator._rule_gen`

> Source: [readmenator/_rule_gen.py:1](../../readmenator/_rule_gen.py#L1) | language `py` | coverage 80.0% | [API index](../index.md)

Suggested linting rule generator producing Semgrep YAML from detected antipatterns.

## Contents

- **Classes:** [`RuleGenerator`](#rulegenerator)

## Classes

<a id="rulegenerator"></a>

### `RuleGenerator`

`class` | [readmenator/_rule_gen.py:14](../../readmenator/_rule_gen.py#L14)

```python
class RuleGenerator
```

Generates suggested linting and security rules from code patterns.

Analyses the scanned codebase for repeated patterns that suggest
project-specific linting rules: bare except clauses, repeated
type annotations, common security antipatterns, and naming
convention violations. Outputs Semgrep YAML rules to a directory.

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`ANTIPATTERN_RULES`](#rulegenerator-antipattern_rules) | `Dict[str, Dict]` | `{'bare_except': {'pattern': '^\\s*except\\s*:', 'severity': 'warning', 'description': 'Bare except clause catches all exceptions including SystemExit', 'message': "Use 'except Exception:' instead of bare 'except:'", 'semgrep_yaml': 'rules:\n - id: rm-bare-except\n pattern: "except:"\n message: "Use \'except Exception:\' instead of bare \'except:\'"\n severity: WARNING\n languages: [python]\n'}, 'print_statement': {'pattern': '^\\s*print\\(', 'severity': 'info', 'description': 'Print statement found (consider logging instead)', 'message': 'Use logging module instead of print()', 'semgrep_yaml': 'rules:\n - id: rm-print-statement\n pattern: "print(...)"\n message: "Use logging module instead of print()"\n severity: INFO\n languages: [python]\n'}, 'todo_comment': {'pattern': '#\\s*(TODO\|FIXME\|HACK\|XXX)\\b', 'severity': 'info', 'description': 'Code marker comment found', 'message': 'Resolve remaining code markers', 'semgrep_yaml': 'rules:\n - id: rm-todo-comment\n pattern-regex: "#\\\\s*(TODO\|FIXME\|HACK\|XXX)"\n message: "Resolve remaining code markers"\n severity: INFO\n languages: [python, javascript, typescript, java, go, rust]\n'}, 'hardcoded_password': {'pattern': '(password\|passwd\|pwd)\\s*[:=]\\s*[\'\\"][^\'\\"]+[\'\\"]', 'severity': 'error', 'description': 'Hardcoded credential detected', 'message': 'Do not hardcode credentials; use environment variables or secrets manager', 'semgrep_yaml': 'rules:\n - id: rm-hardcoded-password\n pattern-either:\n - pattern: "password = "...""\n - pattern: "passwd = "...""\n - pattern: "pwd = "...""\n message: "Do not hardcode credentials"\n severity: ERROR\n languages: [python, javascript, typescript, java, go]\n'}}` |  |
| [`NAMING_PATTERNS`](#rulegenerator-naming_patterns) | `Dict[str, str]` | `{'py': '^[a-z_][a-z0-9_]*$', 'js': '^[a-z][a-zA-Z0-9]*$', 'ts': '^[a-z][a-zA-Z0-9]*$', 'java': '^[a-z][a-zA-Z0-9]*$', 'go': '^[A-Za-z][A-Za-z0-9]*$', 'rs': '^[a-z_][a-z0-9_]*$'}` |  |

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#rulegenerator-__init__) | constructor |  |
| [`generate`](#rulegenerator-generate) | method | Generate suggested rules by scanning code patterns. |
| [`write_rules`](#rulegenerator-write_rules) | method | Write suggested rules to Semgrep YAML files in output_dir. |

<a id="rulegenerator-__init__"></a>

#### `RuleGenerator.__init__`

`constructor` | [readmenator/_rule_gen.py:90](../../readmenator/_rule_gen.py#L90)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`AnalyzerFactory.rule_gen`](readmenator._pipeline.py.md#analyzerfactory-rule_gen)

<a id="rulegenerator-generate"></a>

#### `RuleGenerator.generate`

`method` | [readmenator/_rule_gen.py:94](../../readmenator/_rule_gen.py#L94)

```python
def generate(self, nodes: List[Node], content_map: Optional[Dict[str, str]] = None) -> List[SuggestedRule]
```

Generate suggested rules by scanning code patterns.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes with symbols. |
| `content_map` | `Optional[Dict[str, str]]` | `None` | Optional mapping of file paths to their source content for deeper pattern matching. |

**Returns:** `List[SuggestedRule]` - List of SuggestedRule instances.

<a id="rulegenerator-write_rules"></a>

#### `RuleGenerator.write_rules`

`method` | [readmenator/_rule_gen.py:122](../../readmenator/_rule_gen.py#L122)

```python
def write_rules(self, rules: List[SuggestedRule], output_dir: str) -> int
```

Write suggested rules to Semgrep YAML files in output_dir.

Returns the number of rule files written.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `rules` | `List[SuggestedRule]` |  |  |
| `output_dir` | `str` |  |  |

**Returns:** `int`

---
