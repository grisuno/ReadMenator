# readmenator

*Community 0 | 69 files | cohesion 0.83*

## Definition

This community groups 69 file(s) rooted at `readmenator` with dominant language py (cohesion 0.83). Central symbols: `AgentInjector`, `AgentOutputGenerator`, `AnalysisResult`, `AnalysisResultV2`, `AnalyzerFactory`, `ArchitectureLinter`, `Backdrop`, `ChangeImpact`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApp.

## Files

### `readmenator` (35 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/__main__.py` | py | testing | 3 | no |
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `readmenator/_agent_output.py` | py | utility | 18 | yes |
| `readmenator/_analyzer.py` | py | utility | 14 | yes |
| `readmenator/_app.py` | py | utility | 46 | no |
| `readmenator/_cache.py` | py | infrastructure | 13 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | no |
| `readmenator/_cursorrules_generator.py` | py | business_logic | 8 | yes |

### `tests` (33 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_agent_injector.py` | py | testing | 38 | yes |
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_cache.py` | py | testing | 22 | yes |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | no |

*... and 49 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:16`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:114`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:129`) `def main()`
- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:111`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:136`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:147`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:161`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:179`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:192`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:196`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:210`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:248`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:257`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:267`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:283`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:295`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:300`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
- `AgentOutputGenerator` (class, `readmenator/_agent_output.py:47`) `class AgentOutputGenerator` - Generates agent-friendly, grep-optimised output files.
- `__init__` (method, `readmenator/_agent_output.py:54`) `def __init__(self, config)`
- `generate` (method, `readmenator/_agent_output.py:61`) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings` - Write all agent output files and return the output directory path.
- `_infer_subsystems` (method, `readmenator/_agent_output.py:116`) `def _infer_subsystems(self, nodes)` - Group nodes by directory, inferring subsystem names.
- `_build_index` (method, `readmenator/_agent_output.py:153`) `def _build_index(self, nodes, subsystems)`
- `_build_architecture` (method, `readmenator/_agent_output.py:183`) `def _build_architecture(self, edges, resolved_edges, nodes)`
- `_build_security` (method, `readmenator/_agent_output.py:227`) `def _build_security(self, findings, nodes)`
- `_enclosing_symbol` (method, `readmenator/_agent_output.py:257`) `def _enclosing_symbol(nodes, file_path, line)` - Return the nearest symbol defined at or before line in file_path.
- `_build_api` (method, `readmenator/_agent_output.py:276`) `def _build_api(self, nodes, resolved_map, imported_by)`
- `_build_manifest` (method, `readmenator/_agent_output.py:331`) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root)` - Build MANIFEST.json with freshness + entry points for agents.
- `_build_symbols` (method, `readmenator/_agent_output.py:370`) `def _build_symbols(self, nodes)` - Build grep-friendly symbol index (one line per symbol).
- `_build_gotchas` (method, `readmenator/_agent_output.py:387`) `def _build_gotchas(self, analysis, analysis_v2, nodes)`
- `_write_subsystem_files` (method, `readmenator/_agent_output.py:469`) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by,`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 213
- Cross-boundary resolved imports (EXTRACTED): 41

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_category.py.
- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/_scanner.py imports readmenator/parsers/__init__.py.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_category.py reaches tests/test_resolver.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches tests/test_cache.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches tests/test_config.py in 4 hops.

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/__main__.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_mcp_server.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_app.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_config.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_layers.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_query.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_models.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_resolver.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_linter.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_rank.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_cursorrules_generator.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_pipeline.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_watcher.py` via `subprocess` (4 hops)

## Open Questions

- Why do 29 file(s) lack file-level docs (e.g. `readmenator.py`)? What purpose do they serve?
- Can the cycle `readmenator/_app.py` -> `readmenator/_pipeline.py` -> `readmenator/_agent_injector.py` -> `readmenator.py` -> `readmenator/__main__.py` -> `readmenator/_mcp_server.py` be broken with an interface?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator changed?
- Should readmenator be split, given cohesion 0.83?

## Sources

- `readmenator.py`
- `readmenator/__init__.py`
- `readmenator/__main__.py`
- `readmenator/_agent_injector.py`
- `readmenator/_agent_output.py`
- `readmenator/_analyzer.py`
- `readmenator/_app.py`
- `readmenator/_cache.py`
- `readmenator/_config.py`
- `readmenator/_cpg.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_diagrams.py`
- `readmenator/_documentation.py`
- `readmenator/_exporter.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- *... and 49 more*
