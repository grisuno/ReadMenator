# readmenator/parsers

*Community 1 | 34 files | cohesion 0.52*

## Definition

This community groups 34 file(s) rooted at `readmenator/parsers` with dominant language py (cohesion 0.52). Central symbols: `AnalysisResult`, `AnalysisResultV2`, `AssemblyParser`, `CParser`, `CSharpParser`, `ChangeImpact`, `CommunityResult`, `ConceptGraph`. Core file: `tests/test_dataflow.py` (47 symbols). Documented purpose: Procedural intra-function dataflow analysis for readmenator.  Detects classic logic bug classes without tokens, types, or control-flow graphs: use of uninitiali.

## Files

### `readmenator/parsers` (21 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/parsers/__init__.py` | py | utility | 2 | yes |
| `readmenator/parsers/_assembly.py` | py | utility | 2 | yes |
| `readmenator/parsers/_base.py` | py | utility | 6 | yes |
| `readmenator/parsers/_c.py` | py | utility | 3 | yes |
| `readmenator/parsers/_csharp.py` | py | utility | 2 | yes |
| `readmenator/parsers/_dart.py` | py | utility | 2 | yes |
| `readmenator/parsers/_elixir.py` | py | utility | 2 | yes |

### `tests` (7 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_hotspots.py` | py | testing | 11 | no |
| `tests/test_mermaid.py` | py | testing | 13 | no |
| `tests/test_models.py` | py | testing | 11 | no |
| `tests/test_parsers_property.py` | py | testing | 27 | yes |
| `tests/test_rule_gen.py` | py | testing | 10 | no |
| `tests/test_sarif.py` | py | testing | 10 | no |

### `readmenator` (6 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_hotspots.py` | py | utility | 7 | yes |
| `readmenator/_mermaid.py` | py | utility | 4 | yes |
| `readmenator/_models.py` | py | business_logic | 23 | yes |
| `readmenator/_rule_gen.py` | py | business_logic | 9 | yes |
| `readmenator/_sarif.py` | py | utility | 5 | yes |

*... and 14 more files in this community.*


## Key Symbols

- `_strip_noise` (function, `readmenator/_dataflow.py:96`) `def _strip_noise(line)` - Remove comments and string contents that confuse identifier scans.
- `_strip_block_comments` (function, `readmenator/_dataflow.py:107`) `def _strip_block_comments(content)` - Blank block comments while preserving newlines and line numbers.
- `_blank` (function, `readmenator/_dataflow.py:110`) `def _blank(match)`
- `_strip_sizeof` (function, `readmenator/_dataflow.py:116`) `def _strip_sizeof(line)` - Blank sizeof operands, which never evaluate their argument at runtime.
- `DataflowAnalyzer` (class, `readmenator/_dataflow.py:122`) `class DataflowAnalyzer` - Regex-based intra-function dataflow checker over scanned content.
- `__init__` (method, `readmenator/_dataflow.py:125`) `def __init__(self, config)` - Store configuration for enable flag and issue caps.
- `analyze` (method, `readmenator/_dataflow.py:129`) `def analyze(self, nodes, content_map)` - Check every function body span and return capped issues.
- `_brace_depths` (method, `readmenator/_dataflow.py:153`) `def _brace_depths(lines)` - Return the brace depth before each line of noise-stripped code.
- `_function_spans` (method, `readmenator/_dataflow.py:164`) `def _function_spans(self, node, total_lines, depths)` - Return (name, start_idx, end_idx) spans for function symbols.
- `_analyze_function` (method, `readmenator/_dataflow.py:191`) `def _analyze_function(self, file_id, func, lines, start, end)` - Run def-use checks over one function body span.
- `_scan_reads` (method, `readmenator/_dataflow.py:403`) `def _scan_reads(text, lineno, reads, assigned, declared_names)` - Record identifier reads and address-takes inside an expression.
- `_scan_inline_aliases` (method, `readmenator/_dataflow.py:427`) `def _scan_inline_aliases(line, lineno, arrays, derived_alias, deriv_reads)` - Discover pointer-from-array aliases in mid-line statements.
- `_scan_out_params` (method, `readmenator/_dataflow.py:450`) `def _scan_out_params(line, lineno, assigned)` - Treat known filler/scan call arguments as assignments.
- `_scan_array_args` (method, `readmenator/_dataflow.py:461`) `def _scan_array_args(line, lineno, arrays, assigned)` - Treat arrays passed to non-readonly calls as assignments.
- `_params_of` (method, `readmenator/_dataflow.py:474`) `def _params_of(signature_line)` - Extract parameter names from a function signature line.
- `_track_call_continuation` (method, `readmenator/_dataflow.py:494`) `def _track_call_continuation(line, call_open, paren_balance)` - Track whether the next line continues an unclosed call.
- `_mentions_param` (method, `readmenator/_dataflow.py:513`) `def _mentions_param(text, params)` - Return True when an expression mentions a function parameter.
- `_is_member` (method, `readmenator/_dataflow.py:521`) `def _is_member(line, pos)` - Return True when the identifier at pos is a struct member access.
- `_member_base` (method, `readmenator/_dataflow.py:527`) `def _member_base(line, pos)` - Return the base identifier of a member access chain.
- `_is_prototype` (method, `readmenator/_dataflow.py:535`) `def _is_prototype(line)` - Return True for declaration lines that are actually prototypes.
- `_null_checked` (method, `readmenator/_dataflow.py:540`) `def _null_checked(body_text, name)` - Return True when body contains a NULL/boolean check for name.
- `HotspotAnalyzer` (class, `readmenator/_hotspots.py:22`) `class HotspotAnalyzer` - Hotspot detection, cycle analysis, and change impact analysis.
- `__init__` (method, `readmenator/_hotspots.py:31`) `def __init__(self, config)`
- `analyze_hotspots` (method, `readmenator/_hotspots.py:34`) `def analyze_hotspots(self, nodes, edges, resolved_edges)` - Rank files by combined complexity and centrality scores.
- `detect_cycles` (method, `readmenator/_hotspots.py:90`) `def detect_cycles(self, nodes, resolved_edges)` - Detect cycles in the resolved import graph using DFS.
- `_dfs_visit` (function, `readmenator/_hotspots.py:114`) `def _dfs_visit(current)`
- `_record_cycle` (function, `readmenator/_hotspots.py:125`) `def _record_cycle(start, end)`
- `analyze_change_impact` (method, `readmenator/_hotspots.py:155`) `def analyze_change_impact(self, nodes, resolved_edges)` - Compute change impact for every file in the project.
- `MermaidRenderer` (class, `readmenator/_mermaid.py:17`) `class MermaidRenderer` - Renders a knowledge graph to Mermaid JS flowchart syntax.
- `__init__` (method, `readmenator/_mermaid.py:26`) `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, f` - Initialise rendering budgets and styles.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 96
- Cross-boundary resolved imports (EXTRACTED): 99

## Connections

- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 5 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_explorer.py imports readmenator/_models.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `tests/test_dataflow.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator/parsers changed?
- Should readmenator/parsers be split, given cohesion 0.52?

## Sources

- `readmenator/_dataflow.py`
- `readmenator/_hotspots.py`
- `readmenator/_mermaid.py`
- `readmenator/_models.py`
- `readmenator/_rule_gen.py`
- `readmenator/_sarif.py`
- `readmenator/parsers/__init__.py`
- `readmenator/parsers/_assembly.py`
- `readmenator/parsers/_base.py`
- `readmenator/parsers/_c.py`
- `readmenator/parsers/_csharp.py`
- `readmenator/parsers/_dart.py`
- `readmenator/parsers/_elixir.py`
- `readmenator/parsers/_gdscript.py`
- `readmenator/parsers/_go.py`
- `readmenator/parsers/_java.py`
- `readmenator/parsers/_javascript.py`
- `readmenator/parsers/_kotlin.py`
- `readmenator/parsers/_lua.py`
- `readmenator/parsers/_nim.py`
- *... and 14 more*
