# readmenator

*Community 0 | 81 files | cohesion 0.90*

## Definition

This community groups 81 file(s) rooted at `readmenator` with dominant language py (cohesion 0.90). Central symbols: `AgentInjector`, `AgentOutputGenerator`, `AnalysisResult`, `AnalysisResultV2`, `AnalyzerFactory`, `ArchitectureLinter`, `Backdrop`, `Category`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

### `readmenator` (43 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/__main__.py` | py | testing | 3 | yes |
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `readmenator/_agent_output.py` | py | utility | 32 | yes |
| `readmenator/_analyzer.py` | py | utility | 18 | yes |
| `readmenator/_app.py` | py | utility | 50 | yes |
| `readmenator/_cache.py` | py | infrastructure | 14 | yes |
| `readmenator/_category.py` | py | utility | 26 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |

### `tests` (37 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_agent_friendliness.py` | py | testing | 43 | yes |
| `tests/test_agent_injector.py` | py | testing | 38 | yes |
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_cache.py` | py | testing | 22 | yes |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |

*... and 61 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:121`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:136`) `def main()`
- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:101`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:123`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:134`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:148`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:166`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:179`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:183`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:197`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:235`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:244`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:254`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:270`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:282`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:287`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
- `AgentOutputGenerator` (class, `readmenator/_agent_output.py:70`) `class AgentOutputGenerator` - Generates agent-friendly, grep-optimised output files.
- `__init__` (method, `readmenator/_agent_output.py:77`) `def __init__(self, config)` - Store configuration for output paths and size budgets.
- `generate` (method, `readmenator/_agent_output.py:81`) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings` - Write all agent output files and return the output directory path.
- `_infer_subsystems` (method, `readmenator/_agent_output.py:137`) `def _infer_subsystems(self, nodes)` - Group nodes by directory, inferring subsystem names.
- `_build_index` (method, `readmenator/_agent_output.py:172`) `def _build_index(self, nodes, subsystems, imported_by)` - Build the file -> purpose -> subsystem -> blast radius table.
- `_build_architecture` (method, `readmenator/_agent_output.py:204`) `def _build_architecture(self, edges, resolved_edges, nodes)` - Build internal dependency pairs plus per-file external imports.
- `_build_security` (method, `readmenator/_agent_output.py:256`) `def _build_security(self, findings, nodes)` - Build findings grouped by severity with scope and fix hints.
- `_enclosing_symbol` (method, `readmenator/_agent_output.py:292`) `def _enclosing_symbol(symbols, line)` - Return the nearest symbol defined at or before line.
- `_is_public` (method, `readmenator/_agent_output.py:302`) `def _is_public(self, sym)` - Return whether a symbol belongs in the public API listing.
- `_qualified_names` (method, `readmenator/_agent_output.py:309`) `def _qualified_names(symbols)` - Map each method's index to ``Owner.method`` using the nearest preceding type.
- `_build_api` (method, `readmenator/_agent_output.py:327`) `def _build_api(self, nodes, resolved_map, imported_by, layers)` - Build one greppable line per public function or method.
- `_build_manifest` (method, `readmenator/_agent_output.py:385`) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root,` - Build MANIFEST.json: freshness, entry points, read order, costs.
- `_entrypoints` (method, `readmenator/_agent_output.py:457`) `def _entrypoints(self, nodes, layers)` - Return likely program entry points, shallowest paths first.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 264
- Cross-boundary resolved imports (EXTRACTED): 27

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_scanner.py imports readmenator/parsers/__init__.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches readmenator/parsers/__init__.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/parsers/__init__.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/parsers/__init__.py reaches tests/test_readme_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/parsers/_assembly.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/parsers/_assembly.py reaches tests/test_readme_injector.py in 4 hops.

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_gh_wiki.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_gitmeta.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_video.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 17 file(s) lack file-level docs (e.g. `tests/test_agent_output.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator changed?
- Should readmenator be split, given cohesion 0.90?

## Sources

- `readmenator.py`
- `readmenator/__init__.py`
- `readmenator/__main__.py`
- `readmenator/_agent_injector.py`
- `readmenator/_agent_output.py`
- `readmenator/_analyzer.py`
- `readmenator/_app.py`
- `readmenator/_cache.py`
- `readmenator/_category.py`
- `readmenator/_config.py`
- `readmenator/_cpg.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_diagrams.py`
- `readmenator/_documentation.py`
- `readmenator/_explain.py`
- `readmenator/_exporter.py`
- `readmenator/_gh_wiki.py`
- `readmenator/_gitmeta.py`
- *... and 61 more*
