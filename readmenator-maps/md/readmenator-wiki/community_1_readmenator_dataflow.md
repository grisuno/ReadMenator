# readmenator: _dataflow

*Community 1 | 23 files | cohesion 0.29*

## Definition

This community groups 23 file(s) rooted at `tests` with dominant language py (cohesion 0.29). Central symbols: `Config`, `DataflowAnalyzer`, `DeadCodeStripper`, `GraphExporter`, `HotspotAnalyzer`, `LayerRuleEngine`, `MonolithRefactorizer`, `RuleGenerator`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Immutable configuration dataclass for readmenator.  All tuneable parameters live here as frozen dataclass fields. No magic numbers or hardcoded paths exist else.

## Files

### `tests` (14 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_hotspots.py` | py | testing | 11 | no |
| `tests/test_layer_rules.py` | py | testing | 13 | no |
| `tests/test_parsers.py` | py | testing | 87 | no |
| `tests/test_parsers_new.py` | py | testing | 36 | yes |
| `tests/test_refactorizer.py` | py | testing | 17 | yes |

### `readmenator` (9 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_exporter.py` | py | utility | 15 | yes |
| `readmenator/_hotspots.py` | py | utility | 7 | yes |
| `readmenator/_layer_rules.py` | py | business_logic | 4 | yes |
| `readmenator/_refactorizer.py` | py | utility | 9 | yes |
| `readmenator/_rule_gen.py` | py | business_logic | 9 | yes |
| `readmenator/_taint.py` | py | utility | 6 | yes |

*... and 3 more files in this community.*


## Key Symbols

- `Config` (class, `readmenator/_config.py:15`) `class Config` - Single source of truth for all readmenator settings.
- `_strip_noise` (function, `readmenator/_dataflow.py:96`) `def _strip_noise(line)` - Remove comments and string contents that confuse identifier scans.
- `_strip_block_comments` (function, `readmenator/_dataflow.py:107`) `def _strip_block_comments(content)` - Blank block comments while preserving newlines and line numbers.
- `_blank` (method, `readmenator/_dataflow.py:110`) `def _blank(match)`
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
- `DeadCodeStripper` (class, `readmenator/_dead_code.py:17`) `class DeadCodeStripper` - Identifies dead code symbols in the knowledge graph.
- `__init__` (method, `readmenator/_dead_code.py:25`) `def __init__(self, config)`
- `identify` (method, `readmenator/_dead_code.py:28`) `def identify(self, nodes, edges, resolved_edges)` - Identify dead code symbols with zero in-degree.
- `_build_in_degree_map` (method, `readmenator/_dead_code.py:64`) `def _build_in_degree_map(self, nodes, resolved_edges)` - Build in-degree count for each symbol name.
- `_classify_recommendation` (method, `readmenator/_dead_code.py:88`) `def _classify_recommendation(self, symbol)` - Classify the recommended action for a dead symbol.
- `GraphExporter` (class, `readmenator/_exporter.py:21`) `class GraphExporter` - Exports the knowledge graph to JSON, HTML, and SVG formats.
- `__init__` (method, `readmenator/_exporter.py:29`) `def __init__(self, config)` - Initialise with application configuration.
- `to_json` (method, `readmenator/_exporter.py:37`) `def to_json(self, nodes, edges, resolved_edges, analysis, findings)` - Export the graph as a node-link JSON string.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 30
- Cross-boundary resolved imports (EXTRACTED): 81

## Connections

- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__main__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_dataflow.py imports readmenator/_models.py.
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (readmenator: _dataflow) and community 5 (orphans).

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 9 file(s) lack file-level docs (e.g. `tests/test_config.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _dataflow changed?
- Should readmenator: _dataflow be split, given cohesion 0.29?

## Sources

- `readmenator/_config.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_exporter.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_refactorizer.py`
- `readmenator/_rule_gen.py`
- `readmenator/_taint.py`
- `tests/test_config.py`
- `tests/test_cpg.py`
- `tests/test_dataflow.py`
- `tests/test_dead_code.py`
- `tests/test_documentation.py`
- `tests/test_exporter.py`
- `tests/test_hotspots.py`
- `tests/test_layer_rules.py`
- `tests/test_parsers.py`
- `tests/test_parsers_new.py`
- `tests/test_refactorizer.py`
- *... and 3 more*
