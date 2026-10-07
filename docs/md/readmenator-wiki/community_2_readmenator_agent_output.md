# readmenator: _agent_output

*Community 2 | 10 files | cohesion 0.35*

## Definition

This community groups 10 file(s) rooted at `readmenator` with dominant language py (cohesion 0.35). Central symbols: `AgentOutputGenerator`, `FileCache`, `GitHubWikiPublisher`, `ImportResolver`, `TestAgentOutputBudget`, `TestAgentOutputSignal`, `TestCommunityHubDamping`, `TestCommunityShaping`. Core file: `tests/test_agent_friendliness.py` (43 symbols). Documented purpose: Agent-friendly output generator for ReadMenator.  Generates grep-optimized, flat-markdown files in a dedicated output directory.  File names for per-subsystem f.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_agent_output.py` | py | utility | 32 | yes |
| `readmenator/_cache.py` | py | infrastructure | 14 | yes |
| `readmenator/_gh_wiki.py` | py | utility | 18 | yes |
| `readmenator/_gitmeta.py` | py | utility | 4 | yes |
| `readmenator/_purpose.py` | py | utility | 7 | yes |
| `readmenator/_resolver.py` | py | utility | 17 | yes |
| `tests/test_agent_friendliness.py` | py | testing | 43 | yes |
| `tests/test_cache.py` | py | testing | 22 | yes |
| `tests/test_gh_wiki.py` | py | testing | 15 | yes |
| `tests/test_resolver.py` | py | testing | 22 | yes |

## Key Symbols

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
- `_inventory` (method, `readmenator/_agent_output.py:468`) `def _inventory(self, out_dir)` - List generated documents with line counts and token estimates.
- `_build_symbols` (method, `readmenator/_agent_output.py:481`) `def _build_symbols(self, nodes)` - Build grep-friendly symbol index (one line per symbol).
- `_closed_loop` (method, `readmenator/_agent_output.py:496`) `def _closed_loop(cycle)` - Render a cycle as a closed loop without duplicating a closed tail.
- `_build_gotchas` (method, `readmenator/_agent_output.py:503`) `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` - Build actionable warnings: blast radius, hotspots, cycles, violations.
- `keep` (method, `readmenator/_agent_output.py:522`) `def keep(file_id)` - Return whether a file belongs in the gotcha lists.
- `_safe_name` (method, `readmenator/_agent_output.py:626`) `def _safe_name(name)` - Return a filesystem-safe subsystem name.
- `_write_subsystem_files` (method, `readmenator/_agent_output.py:633`) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by,` - Write one paged KB_<subsystem>.md per inferred subsystem.
- `_build_subsystem_content` (method, `readmenator/_agent_output.py:648`) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by,` - Build per-file context (purpose, layer, symbols, edges) for one subsystem.
- `_write_recipes` (method, `readmenator/_agent_output.py:698`) `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` - Write task recipes grounded in this project's actual analysis data.
- `_deps_by_source` (method, `readmenator/_agent_output.py:826`) `def _deps_by_source(resolved_map)` - Index resolved dependencies by source file, sorted and deduplicated.
- `_build_resolved_map` (method, `readmenator/_agent_output.py:836`) `def _build_resolved_map(resolved_edges)` - Map (source, target) pairs to their relation.
- `_build_imported_by_map` (method, `readmenator/_agent_output.py:846`) `def _build_imported_by_map(resolved_edges)` - Map each file to the files that import it.
- `_page_name` (method, `readmenator/_agent_output.py:856`) `def _page_name(filename, page)` - Return the file name of a page (page 1 keeps the original name).
- `_split_units` (method, `readmenator/_agent_output.py:864`) `def _split_units(body, is_table)` - Split a document body into atomic units that should not straddle pages.
- `_chunk_unit` (method, `readmenator/_agent_output.py:877`) `def _chunk_unit(unit, budget)` - Split an oversized unit into budget-sized chunks with continued headings.
- `_paginate` (method, `readmenator/_agent_output.py:894`) `def _paginate(self, filename, content)` - Split a document into pages that each respect the line cap.
- `_write_paged` (method, `readmenator/_agent_output.py:933`) `def _write_paged(self, out_dir, filename, content)` - Write a document as one or more capped pages and return their paths.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 13
- Cross-boundary resolved imports (EXTRACTED): 28

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 6 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_friendliness.py imports readmenator/_scanner.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_output.py imports readmenator/_agent_output.py.
- [INFERRED] bridges community 1 <-> 2 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] bridges community 0 <-> 2 (strength 0.5): Inferred cross-community bridge: tests/test_readme_injector.py reaches tests/test_resolver.py in 5 hops.

## Risks

- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_gh_wiki.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_gitmeta.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `tests/test_gh_wiki.py` -> `tests/test_gh_wiki.py` via `subprocess` (0 hops)
- [taint high] `tests/test_gh_wiki.py` -> `readmenator/_gh_wiki.py` via `subprocess` (1 hops)
- [taint high] `tests/test_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Is the dangerous import `subprocess` in `readmenator/_gh_wiki.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _agent_output changed?
- Should readmenator: _agent_output be split, given cohesion 0.35?

## Sources

- `readmenator/_agent_output.py`
- `readmenator/_cache.py`
- `readmenator/_gh_wiki.py`
- `readmenator/_gitmeta.py`
- `readmenator/_purpose.py`
- `readmenator/_resolver.py`
- `tests/test_agent_friendliness.py`
- `tests/test_cache.py`
- `tests/test_gh_wiki.py`
- `tests/test_resolver.py`
