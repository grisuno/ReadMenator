# readmenator: _agent_output

*Community 3 | 17 files | cohesion 0.36*

## Definition

This community groups 17 file(s) rooted at `readmenator` with dominant language py (cohesion 0.36). Central symbols: `AgentOutputGenerator`, `FileCache`, `GraphAnalyzer`, `ImportResolver`, `PolyglotScanner`, `SecurityAnalyzer`, `SecurityRule`, `TestAgentOutputBudget`. Core file: `tests/test_security.py` (68 symbols). Documented purpose: Agent-friendly output generator for ReadMenator.  Generates grep-optimized, flat-markdown files in a dedicated output directory.  File names for per-subsystem f.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_agent_output.py` | py | utility | 33 | yes |
| `readmenator/_analyzer.py` | py | utility | 22 | yes |
| `readmenator/_cache.py` | py | infrastructure | 14 | yes |
| `readmenator/_gitmeta.py` | py | utility | 4 | yes |
| `readmenator/_purpose.py` | py | utility | 7 | yes |
| `readmenator/_resolver.py` | py | utility | 17 | yes |
| `readmenator/_scanner.py` | py | utility | 14 | yes |
| `readmenator/_security.py` | py | utility | 32 | yes |
| `readmenator/_wiki.py` | py | utility | 32 | yes |
| `tests/test_agent_friendliness.py` | py | testing | 58 | yes |
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_cache.py` | py | testing | 22 | yes |
| `tests/test_resolver.py` | py | testing | 22 | yes |
| `tests/test_scanner.py` | py | testing | 21 | no |
| `tests/test_security.py` | py | testing | 68 | yes |
| `tests/test_taint_bdd.py` | py | testing | 26 | yes |
| `tests/test_wiki.py` | py | testing | 30 | no |

## Key Symbols

- `AgentOutputGenerator` (class, `readmenator/_agent_output.py:70`) `class AgentOutputGenerator` - Generates agent-friendly, grep-optimised output files.
- `__init__` (method, `readmenator/_agent_output.py:77`) `def __init__(self, config)` - Store configuration for output paths and size budgets.
- `generate` (method, `readmenator/_agent_output.py:81`) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings` - Write all agent output files and return the output directory path.
- `_infer_subsystems` (method, `readmenator/_agent_output.py:138`) `def _infer_subsystems(self, nodes)` - Group nodes by directory, inferring subsystem names.
- `_build_index` (method, `readmenator/_agent_output.py:173`) `def _build_index(self, nodes, subsystems, imported_by)` - Build the file -> purpose -> subsystem -> blast radius table.
- `_build_architecture` (method, `readmenator/_agent_output.py:205`) `def _build_architecture(self, edges, resolved_edges, nodes)` - Build internal dependency pairs plus per-file external imports.
- `_build_security` (method, `readmenator/_agent_output.py:257`) `def _build_security(self, findings, nodes)` - Build findings grouped by severity with scope and fix hints.
- `_enclosing_symbol` (method, `readmenator/_agent_output.py:293`) `def _enclosing_symbol(symbols, line)` - Return the nearest symbol defined at or before line.
- `_is_public` (method, `readmenator/_agent_output.py:303`) `def _is_public(self, sym)` - Return whether a symbol belongs in the public API listing.
- `_qualified_names` (method, `readmenator/_agent_output.py:310`) `def _qualified_names(symbols)` - Map each method's index to ``Owner.method`` using the nearest preceding type.
- `_build_api` (method, `readmenator/_agent_output.py:328`) `def _build_api(self, nodes, resolved_map, imported_by, layers)` - Build one greppable line per public function or method.
- `_build_manifest` (method, `readmenator/_agent_output.py:386`) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root,` - Build MANIFEST.json: freshness, entry points, read order, costs.
- `_entrypoints` (method, `readmenator/_agent_output.py:458`) `def _entrypoints(self, nodes, layers)` - Return likely program entry points, shallowest paths first.
- `_inventory` (method, `readmenator/_agent_output.py:469`) `def _inventory(self, out_dir)` - List generated documents with line counts and token estimates.
- `_build_symbols` (method, `readmenator/_agent_output.py:482`) `def _build_symbols(self, nodes)` - Build grep-friendly symbol index (one line per symbol).
- `_closed_loop` (method, `readmenator/_agent_output.py:497`) `def _closed_loop(cycle)` - Render a cycle as a closed loop without duplicating a closed tail.
- `_build_gotchas` (method, `readmenator/_agent_output.py:504`) `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` - Build actionable warnings: blast radius, hotspots, cycles, violations.
- `keep` (method, `readmenator/_agent_output.py:523`) `def keep(file_id)` - Return whether a file belongs in the gotcha lists.
- `_build_concepts` (method, `readmenator/_agent_output.py:626`) `def _build_concepts(self, analysis_v2)` - Build the grep-friendly semantic concept layer.
- `_safe_name` (method, `readmenator/_agent_output.py:666`) `def _safe_name(name)` - Return a filesystem-safe subsystem name.
- `_write_subsystem_files` (method, `readmenator/_agent_output.py:673`) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by,` - Write one paged KB_<subsystem>.md per inferred subsystem.
- `_build_subsystem_content` (method, `readmenator/_agent_output.py:688`) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by,` - Build per-file context (purpose, layer, symbols, edges) for one subsystem.
- `_write_recipes` (method, `readmenator/_agent_output.py:738`) `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` - Write task recipes grounded in this project's actual analysis data.
- `_deps_by_source` (method, `readmenator/_agent_output.py:866`) `def _deps_by_source(resolved_map)` - Index resolved dependencies by source file, sorted and deduplicated.
- `_build_resolved_map` (method, `readmenator/_agent_output.py:876`) `def _build_resolved_map(resolved_edges)` - Map (source, target) pairs to their relation.
- `_build_imported_by_map` (method, `readmenator/_agent_output.py:886`) `def _build_imported_by_map(resolved_edges)` - Map each file to the files that import it.
- `_page_name` (method, `readmenator/_agent_output.py:896`) `def _page_name(filename, page)` - Return the file name of a page (page 1 keeps the original name).
- `_split_units` (method, `readmenator/_agent_output.py:904`) `def _split_units(body, is_table)` - Split a document body into atomic units that should not straddle pages.
- `_chunk_unit` (method, `readmenator/_agent_output.py:917`) `def _chunk_unit(unit, budget)` - Split an oversized unit into budget-sized chunks with continued headings.
- `_paginate` (method, `readmenator/_agent_output.py:934`) `def _paginate(self, filename, content)` - Split a document into pages that each respect the line cap.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 34
- Cross-boundary resolved imports (EXTRACTED): 44

## Connections

- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_cache.py.
- [EXTRACTED] depends_on community 4 <-> 3 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_output.py imports readmenator/_agent_output.py.
- [INFERRED] bridges community 4 <-> 3 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] bridges community 4 <-> 3 (strength 0.5): Inferred cross-community bridge: tests/test_readme_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] shares_context community 3 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (readmenator: _agent_output) and community 5 (orphans).

## Risks

- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_gitmeta.py` via `subprocess` (1 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_scanner.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _agent_output changed?
- Should readmenator: _agent_output be split, given cohesion 0.36?

## Sources

- `readmenator/_agent_output.py`
- `readmenator/_analyzer.py`
- `readmenator/_cache.py`
- `readmenator/_gitmeta.py`
- `readmenator/_purpose.py`
- `readmenator/_resolver.py`
- `readmenator/_scanner.py`
- `readmenator/_security.py`
- `readmenator/_wiki.py`
- `tests/test_agent_friendliness.py`
- `tests/test_analyzer.py`
- `tests/test_cache.py`
- `tests/test_resolver.py`
- `tests/test_scanner.py`
- `tests/test_security.py`
- `tests/test_taint_bdd.py`
- `tests/test_wiki.py`
