# readmenator: _diagrams

*Community 2 | 30 files | cohesion 0.40*

## Definition

This community groups 30 file(s) rooted at `readmenator` with dominant language py (cohesion 0.40). Central symbols: `AgentOutputGenerator`, `ArchitectureLinter`, `ComponentDiagramBuilder`, `CursorRulesGenerator`, `DeclaredRule`, `DirectoryWatcher`, `DocsSitePublisher`, `FileCache`. Core file: `readmenator/_diagrams.py` (92 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

### `readmenator` (18 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__main__.py` | py | utility | 3 | yes |
| `readmenator/_agent_output.py` | py | utility | 33 | yes |
| `readmenator/_app.py` | py | utility | 85 | yes |
| `readmenator/_cache.py` | py | infrastructure | 14 | yes |
| `readmenator/_components.py` | py | presentation | 25 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_diagrams.py` | py | utility | 92 | yes |
| `readmenator/_folder_readme.py` | py | utility | 7 | yes |
| `readmenator/_gh_wiki.py` | py | utility | 18 | yes |
| `readmenator/_gitmeta.py` | py | utility | 4 | yes |

### `tests` (11 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_agent_friendliness.py` | py | testing | 59 | yes |
| `tests/test_cache.py` | py | testing | 22 | yes |
| `tests/test_components.py` | py | testing | 36 | yes |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_diagrams.py` | py | testing | 73 | yes |
| `tests/test_folder_readme.py` | py | testing | 20 | yes |
| `tests/test_gh_wiki.py` | py | testing | 17 | yes |
| `tests/test_integration.py` | py | testing | 16 | no |
| `tests/test_linter.py` | py | testing | 14 | yes |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |

*... and 10 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:136`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:151`) `def main()`
- `AgentOutputGenerator` (class, `readmenator/_agent_output.py:71`) `class AgentOutputGenerator` - Generates agent-friendly, grep-optimised output files.
- `__init__` (method, `readmenator/_agent_output.py:78`) `def __init__(self, config)` - Store configuration for output paths and size budgets.
- `generate` (method, `readmenator/_agent_output.py:82`) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings` - Write all agent output files and return the output directory path.
- `_infer_subsystems` (method, `readmenator/_agent_output.py:139`) `def _infer_subsystems(self, nodes)` - Group nodes by directory, inferring subsystem names.
- `_build_index` (method, `readmenator/_agent_output.py:174`) `def _build_index(self, nodes, subsystems, imported_by)` - Build the file -> purpose -> subsystem -> blast radius table.
- `_build_architecture` (method, `readmenator/_agent_output.py:206`) `def _build_architecture(self, edges, resolved_edges, nodes)` - Build internal dependency pairs plus per-file external imports.
- `_build_security` (method, `readmenator/_agent_output.py:258`) `def _build_security(self, findings, nodes)` - Build findings grouped by severity with scope and fix hints.
- `_enclosing_symbol` (method, `readmenator/_agent_output.py:294`) `def _enclosing_symbol(symbols, line)` - Return the nearest symbol defined at or before line.
- `_is_public` (method, `readmenator/_agent_output.py:304`) `def _is_public(self, sym)` - Return whether a symbol belongs in the public API listing.
- `_qualified_names` (method, `readmenator/_agent_output.py:311`) `def _qualified_names(symbols)` - Map each method's index to ``Owner.method`` using the nearest preceding type.
- `_build_api` (method, `readmenator/_agent_output.py:329`) `def _build_api(self, nodes, resolved_map, imported_by, layers)` - Build one greppable line per public function or method.
- `_build_manifest` (method, `readmenator/_agent_output.py:387`) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root,` - Build MANIFEST.json: freshness, entry points, read order, costs.
- `_entrypoints` (method, `readmenator/_agent_output.py:461`) `def _entrypoints(self, nodes, layers)` - Return likely program entry points, shallowest paths first.
- `_inventory` (method, `readmenator/_agent_output.py:472`) `def _inventory(self, out_dir)` - List generated documents with line counts and token estimates.
- `_build_symbols` (method, `readmenator/_agent_output.py:487`) `def _build_symbols(self, nodes)` - Build grep-friendly symbol index (one line per symbol).
- `_closed_loop` (method, `readmenator/_agent_output.py:502`) `def _closed_loop(cycle)` - Render a cycle as a closed loop without duplicating a closed tail.
- `_build_gotchas` (method, `readmenator/_agent_output.py:509`) `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` - Build actionable warnings: blast radius, hotspots, cycles, violations.
- `keep` (function, `readmenator/_agent_output.py:528`) `def keep(file_id)` - Return whether a file belongs in the gotcha lists.
- `_build_concepts` (method, `readmenator/_agent_output.py:631`) `def _build_concepts(self, analysis_v2)` - Build the grep-friendly semantic concept layer.
- `_safe_name` (method, `readmenator/_agent_output.py:671`) `def _safe_name(name)` - Return a filesystem-safe subsystem name.
- `_write_subsystem_files` (method, `readmenator/_agent_output.py:678`) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by,` - Write one paged KB_<subsystem>.md per inferred subsystem.
- `_build_subsystem_content` (method, `readmenator/_agent_output.py:693`) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by,` - Build per-file context (purpose, layer, symbols, edges) for one subsystem.
- `_write_recipes` (method, `readmenator/_agent_output.py:743`) `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` - Write task recipes grounded in this project's actual analysis data.
- `_deps_by_source` (method, `readmenator/_agent_output.py:871`) `def _deps_by_source(resolved_map)` - Index resolved dependencies by source file, sorted and deduplicated.
- `_build_resolved_map` (method, `readmenator/_agent_output.py:881`) `def _build_resolved_map(resolved_edges)` - Map (source, target) pairs to their relation.
- `_build_imported_by_map` (method, `readmenator/_agent_output.py:891`) `def _build_imported_by_map(resolved_edges)` - Map each file to the files that import it.
- `_page_name` (method, `readmenator/_agent_output.py:901`) `def _page_name(filename, page)` - Return the file name of a page (page 1 keeps the original name).

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 66
- Cross-boundary resolved imports (EXTRACTED): 103

## Connections

- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_app.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__main__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_security.py.
- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_apidocs.py.
- [EXTRACTED] depends_on community 6 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_output.py imports readmenator/_agent_output.py.
- [INFERRED] bridges community 2 <-> 6 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_diagrams.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_htmlpack.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_folder_readme.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [layer strict] `tests/test_components.py` (testing) -> `readmenator/_components.py` (presentation)
- [layer strict] `tests/test_folder_readme.py` (testing) -> `readmenator/_components.py` (presentation)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `tests/test_integration.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_diagrams.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _diagrams changed?
- Should readmenator: _diagrams be split, given cohesion 0.40?

## Sources

- `readmenator.py`
- `readmenator/__main__.py`
- `readmenator/_agent_output.py`
- `readmenator/_app.py`
- `readmenator/_cache.py`
- `readmenator/_components.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_diagrams.py`
- `readmenator/_folder_readme.py`
- `readmenator/_gh_wiki.py`
- `readmenator/_gitmeta.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- `readmenator/_mcp_server.py`
- `readmenator/_memory.py`
- `readmenator/_purpose.py`
- `readmenator/_resolver.py`
- `readmenator/_watcher.py`
- `readmenator/_yaralite.py`
- `tests/test_agent_friendliness.py`
- *... and 10 more*
