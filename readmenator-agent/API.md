# API

## readmenator/__main__.py

### build_parser `def build_parser()`
- Defined: `readmenator/__main__.py:15`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

### _run_tests `def _run_tests()`
- Defined: `readmenator/__main__.py:101`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

### main `def main()`
- Defined: `readmenator/__main__.py:116`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

## readmenator/_agent_injector.py

### ensure_readmenator_installed `def ensure_readmenator_installed()`
- Defined: `readmenator/_agent_injector.py:96`
- Doc: Check if readmenator is installed via pip; install it if missing.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### __init__ `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs)`
- Defined: `readmenator/_agent_injector.py:132`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### inject `def inject(self, project_root)`
- Defined: `readmenator/_agent_injector.py:144`
- Doc: Inject KB reference into all discovered agent files.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### remove `def remove(self, project_root)`
- Defined: `readmenator/_agent_injector.py:162`
- Doc: Remove KB injection from all discovered agent files.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### find_agent_files `def find_agent_files(self, project_root)`
- Defined: `readmenator/_agent_injector.py:175`
- Doc: Public accessor: return all detected agent files.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _find_agent_files `def _find_agent_files(self, root)`
- Defined: `readmenator/_agent_injector.py:179`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _inject_single `def _inject_single(self, path)`
- Defined: `readmenator/_agent_injector.py:193`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _extract_current_injection `def _extract_current_injection(content)`
- Defined: `readmenator/_agent_injector.py:218`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _remove_old_injection `def _remove_old_injection(content)`
- Defined: `readmenator/_agent_injector.py:227`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _remove_single `def _remove_single(self, path)`
- Defined: `readmenator/_agent_injector.py:237`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _build_injection `def _build_injection(self, fmt)`
- Defined: `readmenator/_agent_injector.py:253`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

## readmenator/_agent_output.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_agent_output.py:53`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### generate `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)`
- Defined: `readmenator/_agent_output.py:60`
- Doc: Write all agent output files and return the output directory path.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _infer_subsystems `def _infer_subsystems(self, nodes)`
- Defined: `readmenator/_agent_output.py:111`
- Doc: Group nodes by directory, inferring subsystem names.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_index `def _build_index(self, nodes, subsystems)`
- Defined: `readmenator/_agent_output.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_architecture `def _build_architecture(self, edges, resolved_edges, nodes)`
- Defined: `readmenator/_agent_output.py:178`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_security `def _build_security(self, findings)`
- Defined: `readmenator/_agent_output.py:222`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_api `def _build_api(self, nodes, resolved_map, imported_by)`
- Defined: `readmenator/_agent_output.py:250`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_gotchas `def _build_gotchas(self, analysis, analysis_v2, nodes)`
- Defined: `readmenator/_agent_output.py:307`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _write_subsystem_files `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)`
- Defined: `readmenator/_agent_output.py:376`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_subsystem_content `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)`
- Defined: `readmenator/_agent_output.py:395`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _write_recipes `def _write_recipes(self, recipes_dir, analysis, analysis_v2)`
- Defined: `readmenator/_agent_output.py:445`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_resolved_map `def _build_resolved_map(resolved_edges)`
- Defined: `readmenator/_agent_output.py:499`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_imported_by_map `def _build_imported_by_map(resolved_edges)`
- Defined: `readmenator/_agent_output.py:508`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _write `def _write(path, content)`
- Defined: `readmenator/_agent_output.py:517`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

## readmenator/_analyzer.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_analyzer.py:28`
- Doc: Initialise with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### analyze `def analyze(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_analyzer.py:36`
- Doc: Run the full analysis pipeline and return structured results.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _build_adjacency `def _build_adjacency(self, nodes, edges)`
- Defined: `readmenator/_analyzer.py:89`
- Doc: Build an undirected adjacency map from import edges.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _build_reverse_adjacency `def _build_reverse_adjacency(self, adjacency)`
- Defined: `readmenator/_analyzer.py:103`
- Doc: Build a directed reverse adjacency (incoming edges) map.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _compute_god_nodes `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)`
- Defined: `readmenator/_analyzer.py:113`
- Doc: Compute the most central nodes using combined degree centrality.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _detect_communities `def _detect_communities(self, nodes, adjacency)`
- Defined: `readmenator/_analyzer.py:135`
- Doc: Detect communities using label propagation.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _label_communities `def _label_communities(self, nodes, communities)`
- Defined: `readmenator/_analyzer.py:186`
- Doc: Generate human-readable labels for communities.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _build_community_map `def _build_community_map(self, communities)`
- Defined: `readmenator/_analyzer.py:213`
- Doc: Build a reverse map from file ID to community ID.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _compute_cohesion `def _compute_cohesion(self, communities, adjacency)`
- Defined: `readmenator/_analyzer.py:223`
- Doc: Compute cohesion score for each community.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _find_surprising_connections `def _find_surprising_connections(self, nodes, adjacency, community_map)`
- Defined: `readmenator/_analyzer.py:248`
- Doc: Find non-obvious cross-community bridges.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _shortest_path_communities `def _shortest_path_communities(self, source, target, adjacency, community_map)`
- Defined: `readmenator/_analyzer.py:288`
- Doc: Find the shortest path and communities traversed.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

### _suggest_questions `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)`
- Defined: `readmenator/_analyzer.py:315`
- Doc: Generate plain-language exploration questions from graph structure.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

## readmenator/_app.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_app.py:34`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _scan `def _scan(self, target_dir)`
- Defined: `readmenator/_app.py:43`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _scan_with_content `def _scan_with_content(self, target_dir)`
- Defined: `readmenator/_app.py:51`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _resolve_imports `def _resolve_imports(self, nodes, edges, target_dir)`
- Defined: `readmenator/_app.py:61`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### run `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- Defined: `readmenator/_app.py:80`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _write_sidecar_outputs `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- Defined: `readmenator/_app.py:182`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _inject_readme_link `def _inject_readme_link(self, root)`
- Defined: `readmenator/_app.py:208`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _inject_agent_files `def _inject_agent_files(self, root)`
- Defined: `readmenator/_app.py:216`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### generate_uml_code `def generate_uml_code(self, target_dir, language, output_path)`
- Defined: `readmenator/_app.py:224`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _log_summary `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)`
- Defined: `readmenator/_app.py:236`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### update `def update(self, target_dir, run_security)`
- Defined: `readmenator/_app.py:291`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _scan_for_cache `def _scan_for_cache(self, root, cache)`
- Defined: `readmenator/_app.py:387`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### query `def query(self, target_dir, question)`
- Defined: `readmenator/_app.py:405`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### explain `def explain(self, target_dir, symbol_name)`
- Defined: `readmenator/_app.py:410`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### find_path `def find_path(self, target_dir, symbol_a, symbol_b)`
- Defined: `readmenator/_app.py:422`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### summary `def summary(self, target_dir)`
- Defined: `readmenator/_app.py:435`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### rank_query `def rank_query(self, target_dir, query, top_n)`
- Defined: `readmenator/_app.py:440`
- Doc: Run a ranked query against the knowledge graph.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### rebuild `def rebuild(self, target_dir, run_security)`
- Defined: `readmenator/_app.py:470`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### analyze `def analyze(self, target_dir)`
- Defined: `readmenator/_app.py:473`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_json `def export_json(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:477`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_html `def export_html(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:488`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_svg `def export_svg(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:499`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export `def export(self, target_dir)`
- Defined: `readmenator/_app.py:510`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_graphml `def export_graphml(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:515`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_cypher `def export_cypher(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:526`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_obsidian `def export_obsidian(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:539`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### watch `def watch(self, target_dir)`
- Defined: `readmenator/_app.py:549`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### audit `def audit(self, target_dir)`
- Defined: `readmenator/_app.py:559`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### audit_deep `def audit_deep(self, target_dir)`
- Defined: `readmenator/_app.py:566`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_sarif `def export_sarif(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:586`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_rules `def export_rules(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:596`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### detect_layers `def detect_layers(self, target_dir)`
- Defined: `readmenator/_app.py:606`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### lint `def lint(self, target_dir)`
- Defined: `readmenator/_app.py:616`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### strip_dead_code `def strip_dead_code(self, target_dir)`
- Defined: `readmenator/_app.py:629`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### generate_cursorrules `def generate_cursorrules(self, target_dir)`
- Defined: `readmenator/_app.py:639`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### refactor_monolith `def refactor_monolith(self, target_dir)`
- Defined: `readmenator/_app.py:654`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### on_change `def on_change()`
- Defined: `readmenator/_app.py:553`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

## readmenator/_cache.py

### __init__ `def __init__(self, config, project_root)`
- Defined: `readmenator/_cache.py:31`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### load `def load(self)`
- Defined: `readmenator/_cache.py:38`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### save `def save(self, hashes)`
- Defined: `readmenator/_cache.py:49`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### compute_hash `def compute_hash(self, file_path)`
- Defined: `readmenator/_cache.py:55`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### compute_hashes `def compute_hashes(self, file_paths)`
- Defined: `readmenator/_cache.py:64`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### find_changed `def find_changed(self, file_paths)`
- Defined: `readmenator/_cache.py:72`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### prune_deleted `def prune_deleted(self, current_file_ids)`
- Defined: `readmenator/_cache.py:84`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### save_analysis `def save_analysis(self, key, data)`
- Defined: `readmenator/_cache.py:95`
- Doc: Save an analysis result to the semantic cache.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### load_analysis `def load_analysis(self, key)`
- Defined: `readmenator/_cache.py:118`
- Doc: Load a previously cached analysis result.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### clear_analysis `def clear_analysis(self, key)`
- Defined: `readmenator/_cache.py:135`
- Doc: Clear analysis cache, optionally for a specific key only.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### _prune_analysis_cache `def _prune_analysis_cache(self, current_file_ids)`
- Defined: `readmenator/_cache.py:155`
- Doc: Remove analysis entries for files that no longer exist.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### has_changed_since_last_analysis `def has_changed_since_last_analysis(self, file_paths)`
- Defined: `readmenator/_cache.py:166`
- Doc: Check if any file has changed since the last analysis cache.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

## readmenator/_category.py

### build_category_from_edges `def build_category_from_edges(edges, resolved_edges, node_ids)`
- Defined: `readmenator/_category.py:236`
- Doc: Build a Category from lists of Edge objects.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### _infer_edge_kind `def _infer_edge_kind(relation)`
- Defined: `readmenator/_category.py:280`
- Doc: Map a relation string to an EdgeKind.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### __str__ `def __str__(self)`
- Defined: `readmenator/_category.py:38`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### weight `def weight(self)`
- Defined: `readmenator/_category.py:73`
- Doc: Effective weight for ranking = semantic weight * confidence.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### __init__ `def __init__(self)`
- Defined: `readmenator/_category.py:86`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### add_object `def add_object(self, obj_id)`
- Defined: `readmenator/_category.py:92`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### add_morphism `def add_morphism(self, m)`
- Defined: `readmenator/_category.py:95`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### objects `def objects(self)`
- Defined: `readmenator/_category.py:103`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### morphisms `def morphisms(self)`
- Defined: `readmenator/_category.py:107`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### outgoing `def outgoing(self, obj_id)`
- Defined: `readmenator/_category.py:110`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### incoming `def incoming(self, obj_id)`
- Defined: `readmenator/_category.py:113`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### compose `def compose(self, a, b)`
- Defined: `readmenator/_category.py:116`
- Doc: Compose two morphisms if target of a matches source of b.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### paths `def paths(self, source, target, max_depth)`
- Defined: `readmenator/_category.py:133`
- Doc: Find all composition paths from source to target up to max_depth.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### _compose_kind `def _compose_kind(a, b)`
- Defined: `readmenator/_category.py:157`
- Doc: Determine the composite edge kind.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### __init__ `def __init__(self, category)`
- Defined: `readmenator/_category.py:188`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### _compute_out_weights `def _compute_out_weights(self)`
- Defined: `readmenator/_category.py:197`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### nodes `def nodes(self)`
- Defined: `readmenator/_category.py:203`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### size `def size(self)`
- Defined: `readmenator/_category.py:207`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### node_index `def node_index(self, node_id)`
- Defined: `readmenator/_category.py:210`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### transition_weight `def transition_weight(self, source, target)`
- Defined: `readmenator/_category.py:213`
- Doc: Sum of weights of all morphisms from source to target.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### stochastic_row `def stochastic_row(self, source)`
- Defined: `readmenator/_category.py:221`
- Doc: Return dict of target -> probability for the row of *source*.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### dfs `def dfs(current, goal, path, depth)`
- Defined: `readmenator/_category.py:139`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

## readmenator/_cpg.py

### __init__ `def __init__(self, privacy_mode, cpg_context)`
- Defined: `readmenator/_cpg.py:20`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### generate `def generate(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_cpg.py:24`
- Doc: Generate the CPG JSON-LD string embeddable in markdown.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### _severity_counts `def _severity_counts(self, findings)`
- Defined: `readmenator/_cpg.py:141`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### _build_symbol_list `def _build_symbol_list(self, node)`
- Defined: `readmenator/_cpg.py:147`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### _compute_node_hash `def _compute_node_hash(node)`
- Defined: `readmenator/_cpg.py:163`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

## readmenator/_cursorrules_generator.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_cursorrules_generator.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### generate `def generate(self, nodes, edges, analysis, layers, violations, project_root)`
- Defined: `readmenator/_cursorrules_generator.py:28`
- Doc: Generate the .cursorrules content string.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _build_base_rules `def _build_base_rules(self)`
- Defined: `readmenator/_cursorrules_generator.py:63`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _extract_layer_constraints `def _extract_layer_constraints(self, layers)`
- Defined: `readmenator/_cursorrules_generator.py:81`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _extract_analysis_constraints `def _extract_analysis_constraints(self, analysis)`
- Defined: `readmenator/_cursorrules_generator.py:92`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _extract_violation_rules `def _extract_violation_rules(self, violations)`
- Defined: `readmenator/_cursorrules_generator.py:107`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _write_file `def _write_file(self, project_root, content)`
- Defined: `readmenator/_cursorrules_generator.py:115`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

## readmenator/_dead_code.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_dead_code.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

### identify `def identify(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_dead_code.py:28`
- Doc: Identify dead code symbols with zero in-degree.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

### _build_in_degree_map `def _build_in_degree_map(self, nodes, resolved_edges)`
- Defined: `readmenator/_dead_code.py:64`
- Doc: Build in-degree count for each symbol name.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

### _classify_recommendation `def _classify_recommendation(self, symbol)`
- Defined: `readmenator/_dead_code.py:88`
- Doc: Classify the recommended action for a dead symbol.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

## readmenator/_documentation.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_documentation.py:39`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _ranking_version `def _ranking_version(self)`
- Defined: `readmenator/_documentation.py:57`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _get_git_commit `def _get_git_commit()`
- Defined: `readmenator/_documentation.py:75`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### generate `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)`
- Defined: `readmenator/_documentation.py:85`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _apply_context_budget `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)`
- Defined: `readmenator/_documentation.py:158`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_toc `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)`
- Defined: `readmenator/_documentation.py:296`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_layers `def _build_layers(self, layers, nodes)`
- Defined: `readmenator/_documentation.py:381`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_dashboard `def _build_dashboard(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_documentation.py:415`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_god_nodes `def _build_god_nodes(self, analysis, ranked)`
- Defined: `readmenator/_documentation.py:495`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_community_analysis `def _build_community_analysis(self, analysis, nodes)`
- Defined: `readmenator/_documentation.py:523`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_surprising_connections `def _build_surprising_connections(self, analysis, nodes)`
- Defined: `readmenator/_documentation.py:556`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_suggested_questions `def _build_suggested_questions(self, analysis)`
- Defined: `readmenator/_documentation.py:581`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_ranked_context `def _build_ranked_context(self, ranked)`
- Defined: `readmenator/_documentation.py:597`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_orphans `def _build_orphans(self, nodes, analysis_v2, ranked)`
- Defined: `readmenator/_documentation.py:643`
- Doc: Build a section listing nodes with low coverage signals.
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_query_recipes `def _build_query_recipes(self)`
- Defined: `readmenator/_documentation.py:693`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_taint_analysis `def _build_taint_analysis(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:735`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_hotspots `def _build_hotspots(self, analysis_v2, ranked)`
- Defined: `readmenator/_documentation.py:770`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_dependency_cycles `def _build_dependency_cycles(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:808`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_change_impact `def _build_change_impact(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:828`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_layer_violations `def _build_layer_violations(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:853`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_suggested_rules `def _build_suggested_rules(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:881`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_security_findings `def _build_security_findings(self, findings)`
- Defined: `readmenator/_documentation.py:906`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_mermaid_section `def _build_mermaid_section(self, graph_output, is_truncated)`
- Defined: `readmenator/_documentation.py:953`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_uml_diagram `def _build_uml_diagram(self, nodes, edges)`
- Defined: `readmenator/_documentation.py:976`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_cpg_block `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_documentation.py:1002`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_architecture_reference `def _build_architecture_reference(self, nodes, edges)`
- Defined: `readmenator/_documentation.py:1028`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

## readmenator/_explain.py

### explain_rank `def explain_rank(node_id, ranked, category)`
- Defined: `readmenator/_explain.py:16`
- Doc: Return a detailed breakdown of why *node_id* has its rank.
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

### rank_summary `def rank_summary(ranked, top_n)`
- Defined: `readmenator/_explain.py:140`
- Doc: Return a short summary of the top-N ranked results.
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

### _find_item `def _find_item(node_id, items)`
- Defined: `readmenator/_explain.py:163`
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

## readmenator/_exporter.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_exporter.py:29`
- Doc: Initialise with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_json `def to_json(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:37`
- Doc: Export the graph as a node-link JSON string.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_html `def to_html(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:150`
- Doc: Generate a standalone interactive HTML graph page.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _community_color_map `def _community_color_map(self, analysis)`
- Defined: `readmenator/_exporter.py:236`
- Doc: Build a node-to-color map based on community membership.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _lighten `def _lighten(hex_color)`
- Defined: `readmenator/_exporter.py:254`
- Doc: Lighten a hex color by 30% for border use.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _render_html `def _render_html(self, vis_nodes, vis_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:262`
- Doc: Render the full HTML document with vis.js.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_svg `def to_svg(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_exporter.py:421`
- Doc: Generate a static SVG representation of the graph.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _render_truncated_svg `def _render_truncated_svg(self, total_nodes)`
- Defined: `readmenator/_exporter.py:539`
- Doc: Render a minimal SVG with a truncation notice.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _layout_spring `def _layout_spring(self, nodes, edges, node_map)`
- Defined: `readmenator/_exporter.py:554`
- Doc: Compute a simple spring-layout for node positioning.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_graphml `def to_graphml(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_exporter.py:635`
- Doc: Export the graph as GraphML (Gephi/yEd compatible).
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_cypher `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:712`
- Doc: Export the graph as native Cypher CREATE statements.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_obsidian `def to_obsidian(self, nodes, edges, output_dir, analysis)`
- Defined: `readmenator/_exporter.py:817`
- Doc: Export the graph as an Obsidian vault with wikilinks.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _project `def _project(pos)`
- Defined: `readmenator/_exporter.py:483`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _sev_span `def _sev_span(sev, count)`
- Defined: `readmenator/_exporter.py:334`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

## readmenator/_hotspots.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_hotspots.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### analyze_hotspots `def analyze_hotspots(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_hotspots.py:28`
- Doc: Rank files by combined complexity and centrality scores.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### detect_cycles `def detect_cycles(self, nodes, resolved_edges)`
- Defined: `readmenator/_hotspots.py:84`
- Doc: Detect cycles in the resolved import graph using DFS.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### analyze_change_impact `def analyze_change_impact(self, nodes, resolved_edges)`
- Defined: `readmenator/_hotspots.py:149`
- Doc: Compute change impact for every file in the project.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### _dfs_visit `def _dfs_visit(current)`
- Defined: `readmenator/_hotspots.py:108`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### _record_cycle `def _record_cycle(start, end)`
- Defined: `readmenator/_hotspots.py:119`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

## readmenator/_layer_rules.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_layer_rules.py:34`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

### detect_violations `def detect_violations(self, nodes, edges, resolved_edges, layers)`
- Defined: `readmenator/_layer_rules.py:37`
- Doc: Detect architectural layer violations.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

### violation_summary `def violation_summary(violations)`
- Defined: `readmenator/_layer_rules.py:109`
- Doc: Summarise violations by severity.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

## readmenator/_layers.py

### detect `def detect(self, nodes, edges)`
- Defined: `readmenator/_layers.py:71`
- Doc: Assign each file node to an architectural layer.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

### _classify_file `def _classify_file(self, node, edges)`
- Defined: `readmenator/_layers.py:89`
- Doc: Classify a single file into an architectural layer.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

### layer_summary `def layer_summary(layers)`
- Defined: `readmenator/_layers.py:122`
- Doc: Count files per layer.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

## readmenator/_linter.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_linter.py:31`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### lint `def lint(self, nodes, edges, resolved_edges, layers, content_map)`
- Defined: `readmenator/_linter.py:34`
- Doc: Run all linter rules and return violations.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _check_file_length `def _check_file_length(self, nodes, content_map)`
- Defined: `readmenator/_linter.py:65`
- Doc: Check files against maximum line count threshold.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _check_cross_layer_violations `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)`
- Defined: `readmenator/_linter.py:96`
- Doc: Check for forbidden cross-layer imports.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _check_circular_dependencies `def _check_circular_dependencies(self, nodes, resolved_edges)`
- Defined: `readmenator/_linter.py:127`
- Doc: Check for circular dependencies in the resolved import graph.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _dfs `def _dfs(current)`
- Defined: `readmenator/_linter.py:146`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

## readmenator/_mcp_server.py

### main `def main()`
- Defined: `readmenator/_mcp_server.py:796`
- Doc: CLI entry point for `readmenator serve <path>`.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ `def __init__(self, code, message, data)`
- Defined: `readmenator/_mcp_server.py:59`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ `def __init__(self, msg)`
- Defined: `readmenator/_mcp_server.py:72`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### is_notification `def is_notification(self)`
- Defined: `readmenator/_mcp_server.py:79`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### response `def response(self, result)`
- Defined: `readmenator/_mcp_server.py:82`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### error `def error(self, code, message, data)`
- Defined: `readmenator/_mcp_server.py:85`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ `def __init__(self, name, description, handler, input_schema)`
- Defined: `readmenator/_mcp_server.py:93`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### definition `def definition(self)`
- Defined: `readmenator/_mcp_server.py:108`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### call `def call(self, arguments)`
- Defined: `readmenator/_mcp_server.py:115`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ `def __init__(self, uri, name, description, mime_type, handler)`
- Defined: `readmenator/_mcp_server.py:120`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### definition `def definition(self)`
- Defined: `readmenator/_mcp_server.py:134`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### read `def read(self)`
- Defined: `readmenator/_mcp_server.py:142`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ `def __init__(self, app, target_dir)`
- Defined: `readmenator/_mcp_server.py:147`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### register_tool `def register_tool(self, tool)`
- Defined: `readmenator/_mcp_server.py:155`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### register_resource `def register_resource(self, resource)`
- Defined: `readmenator/_mcp_server.py:158`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _ensure_kb `def _ensure_kb(self)`
- Defined: `readmenator/_mcp_server.py:161`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_initialize `def _handle_initialize(self, req)`
- Defined: `readmenator/_mcp_server.py:173`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_list_tools `def _handle_list_tools(self, req)`
- Defined: `readmenator/_mcp_server.py:187`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_call_tool `def _handle_call_tool(self, req)`
- Defined: `readmenator/_mcp_server.py:192`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_list_resources `def _handle_list_resources(self, req)`
- Defined: `readmenator/_mcp_server.py:214`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_read_resource `def _handle_read_resource(self, req)`
- Defined: `readmenator/_mcp_server.py:219`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### dispatch `def dispatch(self, req)`
- Defined: `readmenator/_mcp_server.py:241`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### run `def run(self)`
- Defined: `readmenator/_mcp_server.py:261`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _register_all `def _register_all(self)`
- Defined: `readmenator/_mcp_server.py:285`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _scan `def _scan(self)`
- Defined: `readmenator/_mcp_server.py:467`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _scan_deep `def _scan_deep(self)`
- Defined: `readmenator/_mcp_server.py:473`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_summary `def _tool_summary(self)`
- Defined: `readmenator/_mcp_server.py:481`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_query `def _tool_query(self, text)`
- Defined: `readmenator/_mcp_server.py:519`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_explain `def _tool_explain(self, name)`
- Defined: `readmenator/_mcp_server.py:524`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_path `def _tool_path(self, symbol_a, symbol_b)`
- Defined: `readmenator/_mcp_server.py:536`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_findings `def _tool_findings(self, min_severity)`
- Defined: `readmenator/_mcp_server.py:547`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_security_summary `def _tool_security_summary(self)`
- Defined: `readmenator/_mcp_server.py:577`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_taint `def _tool_taint(self)`
- Defined: `readmenator/_mcp_server.py:582`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_hotspots `def _tool_hotspots(self, top_n)`
- Defined: `readmenator/_mcp_server.py:603`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_cycles `def _tool_cycles(self)`
- Defined: `readmenator/_mcp_server.py:619`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_communities `def _tool_communities(self)`
- Defined: `readmenator/_mcp_server.py:630`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_layers `def _tool_layers(self)`
- Defined: `readmenator/_mcp_server.py:645`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_layer_violations `def _tool_layer_violations(self)`
- Defined: `readmenator/_mcp_server.py:663`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_rebuild `def _tool_rebuild(self)`
- Defined: `readmenator/_mcp_server.py:679`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_update `def _tool_update(self)`
- Defined: `readmenator/_mcp_server.py:689`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_export_json `def _tool_export_json(self)`
- Defined: `readmenator/_mcp_server.py:697`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_summary `def _resource_summary(self)`
- Defined: `readmenator/_mcp_server.py:705`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_graph `def _resource_graph(self)`
- Defined: `readmenator/_mcp_server.py:722`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_findings `def _resource_findings(self)`
- Defined: `readmenator/_mcp_server.py:741`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_analysis `def _resource_analysis(self)`
- Defined: `readmenator/_mcp_server.py:757`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_kb `def _resource_kb(self)`
- Defined: `readmenator/_mcp_server.py:787`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _get_query_engine `def _get_query_engine(self, nodes, edges, resolved)`
- Defined: `readmenator/_mcp_server.py:791`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

## readmenator/_mermaid.py

### __init__ `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)`
- Defined: `readmenator/_mermaid.py:26`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

### _sanitize_id `def _sanitize_id(node_id)`
- Defined: `readmenator/_mermaid.py:45`
- Doc: Convert *node_id* to a Mermaid-safe identifier.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

### render `def render(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_mermaid.py:56`
- Doc: Produce a Mermaid flowchart string and a truncation flag.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

## readmenator/_models.py

### pluralize_symbol_kind `def pluralize_symbol_kind(kind, plural_map)`
- Defined: `readmenator/_models.py:101`
- Doc: Return the plural form of *kind* according to *plural_map*.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_app.py`, `readmenator/_category.py`, `readmenator/_cpg.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_mermaid.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_refactorizer.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_analyzer.py`, `tests/test_cpg.py`, `tests/test_cursorrules.py`, `tests/test_dead_code.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_exporter.py`, `tests/test_hotspots.py`, `tests/test_layer_rules.py`, `tests/test_linter.py`, `tests/test_mermaid.py`, `tests/test_models.py`, `tests/test_parsers_property.py`, `tests/test_query.py`, `tests/test_ranking.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_rule_gen.py`, `tests/test_sarif.py`, `tests/test_scanner.py`, `tests/test_security.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`, `tests/test_uml.py`

## readmenator/_pipeline.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_pipeline.py:46`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### scanner `def scanner(self)`
- Defined: `readmenator/_pipeline.py:68`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### generator `def generator(self)`
- Defined: `readmenator/_pipeline.py:74`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### analyzer `def analyzer(self)`
- Defined: `readmenator/_pipeline.py:80`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### security `def security(self)`
- Defined: `readmenator/_pipeline.py:86`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### exporter `def exporter(self)`
- Defined: `readmenator/_pipeline.py:92`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### taint `def taint(self)`
- Defined: `readmenator/_pipeline.py:98`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### hotspots `def hotspots(self)`
- Defined: `readmenator/_pipeline.py:104`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### layer_rules `def layer_rules(self)`
- Defined: `readmenator/_pipeline.py:110`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### rule_gen `def rule_gen(self)`
- Defined: `readmenator/_pipeline.py:116`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### sarif `def sarif(self)`
- Defined: `readmenator/_pipeline.py:122`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### cpg `def cpg(self)`
- Defined: `readmenator/_pipeline.py:128`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### layer_detector `def layer_detector(self)`
- Defined: `readmenator/_pipeline.py:137`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### uml `def uml(self)`
- Defined: `readmenator/_pipeline.py:143`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### readme_injector `def readme_injector(self)`
- Defined: `readmenator/_pipeline.py:149`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### agent_injector `def agent_injector(self)`
- Defined: `readmenator/_pipeline.py:158`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### agent_output `def agent_output(self)`
- Defined: `readmenator/_pipeline.py:167`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### build_typed_graph `def build_typed_graph(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_pipeline.py:172`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### make_ranker `def make_ranker(self, typed_graph)`
- Defined: `readmenator/_pipeline.py:182`
- Doc: Create a CompositeRanker for the given typed graph.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### last_category `def last_category(self)`
- Defined: `readmenator/_pipeline.py:199`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### last_typed_graph `def last_typed_graph(self)`
- Defined: `readmenator/_pipeline.py:203`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### __init__ `def __init__(self, factory)`
- Defined: `readmenator/_pipeline.py:216`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

### run `def run(self, nodes, edges, resolved_edges, layers, content_map)`
- Defined: `readmenator/_pipeline.py:219`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

## readmenator/_projections.py

### apply_view `def apply_view(category, view_config)`
- Defined: `readmenator/_projections.py:95`
- Doc: Apply a named view to produce a projected category.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node `def map_node(self, node)`
- Defined: `readmenator/_projections.py:23`
- Doc: Map a code node. Return None to exclude.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:27`
- Doc: Map a morphism. Return None to exclude.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node `def map_node(self, node)`
- Defined: `readmenator/_projections.py:35`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:38`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### __init__ `def __init__(self, documented_ids)`
- Defined: `readmenator/_projections.py:49`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node `def map_node(self, node)`
- Defined: `readmenator/_projections.py:52`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:57`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### __init__ `def __init__(self, fan_in, fan_out, test_files)`
- Defined: `readmenator/_projections.py:70`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node `def map_node(self, node)`
- Defined: `readmenator/_projections.py:80`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:91`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

## readmenator/_query.py

### __init__ `def __init__(self, nodes, edges, resolved_edges, ranker, config)`
- Defined: `readmenator/_query.py:34`
- Doc: Initialise internal indexes from scanned data.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _init_default_ranker `def _init_default_ranker(self)`
- Defined: `readmenator/_query.py:64`
- Doc: Build a default CompositeRanker from the loaded data.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### ranked_query `def ranked_query(self, query, top_n)`
- Defined: `readmenator/_query.py:73`
- Doc: Answer *query* with a ranked list of relevant nodes.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _estimate_test_coverage `def _estimate_test_coverage(self)`
- Defined: `readmenator/_query.py:124`
- Doc: Estimate test coverage per file.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _estimate_doc_coverage `def _estimate_doc_coverage(self)`
- Defined: `readmenator/_query.py:150`
- Doc: Estimate documentation coverage per file.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _build_symbol_index `def _build_symbol_index(self)`
- Defined: `readmenator/_query.py:170`
- Doc: Build a name-to-list-of-(node, symbol) lookup.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _build_import_graph `def _build_import_graph(self)`
- Defined: `readmenator/_query.py:184`
- Doc: Build an adjacency map from import edges.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _build_resolved_graph `def _build_resolved_graph(self)`
- Defined: `readmenator/_query.py:200`
- Doc: Build an adjacency map from resolved import edges.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### find_symbol `def find_symbol(self, name)`
- Defined: `readmenator/_query.py:220`
- Doc: Look up *name* by exact match, then by substring fuzzy match.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### explain `def explain(self, name)`
- Defined: `readmenator/_query.py:238`
- Doc: Return a detailed multi-line explanation of *name*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _find_incoming_imports `def _find_incoming_imports(self, target)`
- Defined: `readmenator/_query.py:277`
- Doc: List all node IDs that import *target*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### find_path `def find_path(self, symbol_a, symbol_b)`
- Defined: `readmenator/_query.py:285`
- Doc: Find the shortest import path from *symbol_a* to *symbol_b*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _make_bidirectional `def _make_bidirectional(graph)`
- Defined: `readmenator/_query.py:315`
- Doc: Convert a directed graph to a bidirectional one.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _bfs_shortest_path `def _bfs_shortest_path(self, graph, start, goal)`
- Defined: `readmenator/_query.py:331`
- Doc: Run BFS to find the shortest path from *start* to *goal*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### query `def query(self, question)`
- Defined: `readmenator/_query.py:355`
- Doc: Free-text search over symbols and file paths.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### summary `def summary(self)`
- Defined: `readmenator/_query.py:411`
- Doc: Return a concise overview of the loaded knowledge base.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

## readmenator/_rank.py

### global_pagerank `def global_pagerank(graph, alpha, max_iter, tolerance)`
- Defined: `readmenator/_rank.py:61`
- Doc: Compute global PageRank on the typed weighted graph.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### personalized_pagerank `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)`
- Defined: `readmenator/_rank.py:119`
- Doc: Compute Personalized PageRank with a seed-node preference vector.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### hits `def hits(graph, max_iter, tolerance)`
- Defined: `readmenator/_rank.py:189`
- Doc: Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### build_seeds_from_query `def build_seeds_from_query(query, node_ids, node_labels, symbols)`
- Defined: `readmenator/_rank.py:240`
- Doc: Build a PPR seed vector from a natural-language query string.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### build_seeds_for_context `def build_seeds_for_context(node_ids, anchor_patterns)`
- Defined: `readmenator/_rank.py:286`
- Doc: Build a PPR seed vector from anchor pattern strings.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### _format_explanation `def _format_explanation(item, result)`
- Defined: `readmenator/_rank.py:512`
- Doc: Format a human-readable explanation for a ranked item.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### label `def label(self)`
- Defined: `readmenator/_rank.py:344`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### top `def top(self, n)`
- Defined: `readmenator/_rank.py:366`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### explain `def explain(self, node_id)`
- Defined: `readmenator/_rank.py:369`
- Doc: Return a human-readable explanation of why *node_id* ranks as it does.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### __init__ `def __init__(self, graph, config)`
- Defined: `readmenator/_rank.py:385`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### _get_global_pr `def _get_global_pr(self)`
- Defined: `readmenator/_rank.py:394`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### rank `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)`
- Defined: `readmenator/_rank.py:404`
- Doc: Compute composite ranking for a query.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### _find_justification_paths `def _find_justification_paths(self, target, seed_ids, category, max_paths)`
- Defined: `readmenator/_rank.py:486`
- Doc: Find shortest paths from any seed to target.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

## readmenator/_readme_injector.py

### __init__ `def __init__(self, kb_filename, agent_output_dir)`
- Defined: `readmenator/_readme_injector.py:68`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### inject `def inject(self, project_root)`
- Defined: `readmenator/_readme_injector.py:76`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _extract_current_injection `def _extract_current_injection(content)`
- Defined: `readmenator/_readme_injector.py:105`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _remove_old_injection `def _remove_old_injection(content)`
- Defined: `readmenator/_readme_injector.py:114`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### remove `def remove(self, project_root)`
- Defined: `readmenator/_readme_injector.py:124`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _find_readme `def _find_readme(root)`
- Defined: `readmenator/_readme_injector.py:153`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _build_injection `def _build_injection(self, suffix)`
- Defined: `readmenator/_readme_injector.py:160`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

## readmenator/_refactorizer.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_refactorizer.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### analyze `def analyze(self, nodes, edges, resolved_edges, content_map)`
- Defined: `readmenator/_refactorizer.py:35`
- Doc: Identify monolithic files and generate refactoring plans.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _get_line_count `def _get_line_count(self, file_id, content_map)`
- Defined: `readmenator/_refactorizer.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _plan_refactoring `def _plan_refactoring(self, node, edges, resolved_edges, content_map)`
- Defined: `readmenator/_refactorizer.py:82`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _group_symbols_by_kind `def _group_symbols_by_kind(self, symbols)`
- Defined: `readmenator/_refactorizer.py:126`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _suggest_target_file `def _suggest_target_file(self, source_file, kind)`
- Defined: `readmenator/_refactorizer.py:132`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _estimate_impact `def _estimate_impact(self, file_id, resolved_edges)`
- Defined: `readmenator/_refactorizer.py:147`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### generate_script `def generate_script(self, plan, project_root)`
- Defined: `readmenator/_refactorizer.py:156`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

## readmenator/_resolver.py

### __init__ `def __init__(self, file_ids, root)`
- Defined: `readmenator/_resolver.py:58`
- Doc: Initialise the resolver with all known file paths.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _build_stem_index `def _build_stem_index(self, file_ids)`
- Defined: `readmenator/_resolver.py:70`
- Doc: Map file stems (without extension) to their full paths.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _build_dir_index `def _build_dir_index(self, file_ids)`
- Defined: `readmenator/_resolver.py:80`
- Doc: Map directory paths to the files they contain.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### resolve `def resolve(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:97`
- Doc: Resolve an import string to a concrete project file path.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### resolve_all `def resolve_all(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:132`
- Doc: Resolve *import_str* to all possible matching project file paths.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_relative `def _resolve_relative(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:148`
- Doc: Resolve a relative import (starts with ``.`` or ``..``).
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_extensionless `def _resolve_extensionless(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:166`
- Doc: Resolve a bare module name by appending known extensions.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_directory_init `def _resolve_directory_init(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:175`
- Doc: Resolve as a package directory with __init__ or index file.
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_module_dotpath `def _resolve_module_dotpath(self, import_str)`
- Defined: `readmenator/_resolver.py:185`
- Doc: Resolve a dotted module path (Python/Java convention).
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_stem_match `def _resolve_stem_match(self, import_str)`
- Defined: `readmenator/_resolver.py:207`
- Doc: Match by file stem only (last resort).
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

## readmenator/_rule_gen.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_rule_gen.py:88`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### generate `def generate(self, nodes, content_map)`
- Defined: `readmenator/_rule_gen.py:92`
- Doc: Generate suggested rules by scanning code patterns.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### write_rules `def write_rules(self, rules, output_dir)`
- Defined: `readmenator/_rule_gen.py:120`
- Doc: Write suggested rules to Semgrep YAML files in output_dir.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _group_by_language `def _group_by_language(self, nodes)`
- Defined: `readmenator/_rule_gen.py:159`
- Doc: Group nodes by their language extension.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _analyze_language `def _analyze_language(self, lang, nodes, content_map)`
- Defined: `readmenator/_rule_gen.py:169`
- Doc: Analyze a single language group for rule suggestions.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _detect_antipatterns `def _detect_antipatterns(self, nodes, content_map)`
- Defined: `readmenator/_rule_gen.py:202`
- Doc: Detect known antipatterns across all files.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _infer_language_for_rule `def _infer_language_for_rule(rule_id)`
- Defined: `readmenator/_rule_gen.py:248`
- Doc: Infer target language for a built-in antipattern rule.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _next_rule_id `def _next_rule_id(self)`
- Defined: `readmenator/_rule_gen.py:258`
- Doc: Generate the next rule identifier.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

## readmenator/_sarif.py

### __init__ `def __init__(self, privacy_mode)`
- Defined: `readmenator/_sarif.py:28`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

### export `def export(self, findings, project_name)`
- Defined: `readmenator/_sarif.py:31`
- Doc: Generate a SARIF v2.1.0 JSON string from security findings.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

### _build_rule `def _build_rule(self, finding)`
- Defined: `readmenator/_sarif.py:80`
- Doc: Build a SARIF reportingDescriptor (rule) object.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

### _build_result `def _build_result(self, finding, rule_index)`
- Defined: `readmenator/_sarif.py:104`
- Doc: Build a SARIF result object for a single finding.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

## readmenator/_scanner.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_scanner.py:33`
- Doc: Initialise the scanner with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _is_ignored `def _is_ignored(self, path)`
- Defined: `readmenator/_scanner.py:42`
- Doc: Return ``True`` if any path component matches IGNORE_DIRS.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _load_gitignore `def _load_gitignore(self, root)`
- Defined: `readmenator/_scanner.py:46`
- Doc: Parse .gitignore patterns using regex (no external deps).
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _gitignore_glob_to_regex `def _gitignore_glob_to_regex(pattern)`
- Defined: `readmenator/_scanner.py:68`
- Doc: Convert a .gitignore glob pattern to a regex pattern.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _is_gitignored `def _is_gitignored(self, rel_path)`
- Defined: `readmenator/_scanner.py:108`
- Doc: Check if a relative path matches any .gitignore pattern.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _validate_path_security `def _validate_path_security(self, path)`
- Defined: `readmenator/_scanner.py:117`
- Doc: Reject symlinks and files exceeding MAX_FILE_SIZE_MB.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _check_directory_depth `def _check_directory_depth(self, path, root)`
- Defined: `readmenator/_scanner.py:130`
- Doc: Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _extract_file_doc `def _extract_file_doc(self, content)`
- Defined: `readmenator/_scanner.py:138`
- Doc: Extract a file-level docstring from the first lines of a source file.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _emit_progress `def _emit_progress(self, count)`
- Defined: `readmenator/_scanner.py:191`
- Doc: Emit a progress message every PROGRESS_REPORT_BATCH files.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### scan `def scan(self, root)`
- Defined: `readmenator/_scanner.py:201`
- Doc: Walk *root* recursively and produce (nodes, edges) for the graph.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### scan_with_content `def scan_with_content(self, root)`
- Defined: `readmenator/_scanner.py:215`
- Doc: Scan and also return raw file contents for deeper analysis.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _scan_impl `def _scan_impl(self, root)`
- Defined: `readmenator/_scanner.py:226`
- Doc: Internal scan implementation returning nodes, edges, and content.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

## readmenator/_security.py

### _parse_minimal_yaml `def _parse_minimal_yaml(text)`
- Defined: `readmenator/_security.py:46`
- Doc: Parse the simplified YAML format used by _security_rules.yml.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _unquote `def _unquote(s)`
- Defined: `readmenator/_security.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _load_rules_from_yaml `def _load_rules_from_yaml(yaml_path)`
- Defined: `readmenator/_security.py:128`
- Doc: Load rule dicts from the YAML rules file, or return None on failure.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _compile `def _compile()`
- Defined: `readmenator/_security.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _python_rules `def _python_rules()`
- Defined: `readmenator/_security.py:153`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _javascript_rules `def _javascript_rules()`
- Defined: `readmenator/_security.py:182`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _c_rules `def _c_rules()`
- Defined: `readmenator/_security.py:201`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _java_rules `def _java_rules()`
- Defined: `readmenator/_security.py:222`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _go_rules `def _go_rules()`
- Defined: `readmenator/_security.py:237`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _ruby_rules `def _ruby_rules()`
- Defined: `readmenator/_security.py:250`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _php_rules `def _php_rules()`
- Defined: `readmenator/_security.py:267`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _shell_rules `def _shell_rules()`
- Defined: `readmenator/_security.py:284`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _csharp_rules `def _csharp_rules()`
- Defined: `readmenator/_security.py:297`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _kotlin_rules `def _kotlin_rules()`
- Defined: `readmenator/_security.py:310`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _swift_rules `def _swift_rules()`
- Defined: `readmenator/_security.py:321`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _scala_rules `def _scala_rules()`
- Defined: `readmenator/_security.py:332`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _lua_rules `def _lua_rules()`
- Defined: `readmenator/_security.py:343`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _dart_rules `def _dart_rules()`
- Defined: `readmenator/_security.py:354`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _rust_rules `def _rust_rules()`
- Defined: `readmenator/_security.py:365`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _nim_rules `def _nim_rules()`
- Defined: `readmenator/_security.py:376`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _gdscript_rules `def _gdscript_rules()`
- Defined: `readmenator/_security.py:387`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _elixir_rules `def _elixir_rules()`
- Defined: `readmenator/_security.py:398`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _build_rules_from_yaml `def _build_rules_from_yaml(yaml_path)`
- Defined: `readmenator/_security.py:447`
- Doc: Attempt to build the rule map from the YAML rules file.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_security.py:496`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _resolve_rules `def _resolve_rules(self)`
- Defined: `readmenator/_security.py:500`
- Doc: Resolve rules: prefer YAML, fall back to built-in.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _meets_threshold `def _meets_threshold(self, severity)`
- Defined: `readmenator/_security.py:509`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### scan `def scan(self, root)`
- Defined: `readmenator/_security.py:513`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### _validate_path `def _validate_path(self, path, root)`
- Defined: `readmenator/_security.py:555`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

### summary `def summary(self, findings)`
- Defined: `readmenator/_security.py:572`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

## readmenator/_taint.py

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_taint.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### analyze `def analyze(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_taint.py:75`
- Doc: Run taint propagation analysis on the codebase.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### _find_direct_sources `def _find_direct_sources(self, nodes, edges)`
- Defined: `readmenator/_taint.py:134`
- Doc: Find files that directly import known-dangerous modules.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### _propagate `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)`
- Defined: `readmenator/_taint.py:160`
- Doc: BFS propagation from source through the import graph.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### _build_forward_graph `def _build_forward_graph(nodes, resolved_edges)`
- Defined: `readmenator/_taint.py:211`
- Doc: Build a forward-directed import graph from resolved edges.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

## readmenator/_uml.py

### _get_code_generator `def _get_code_generator(language)`
- Defined: `readmenator/_uml.py:170`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _type_map_py_to_target `def _type_map_py_to_target(target, py_type_hint)`
- Defined: `readmenator/_uml.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_cpp `def _generate_cpp(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:231`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _cpp_params `def _cpp_params(params)`
- Defined: `readmenator/_uml.py:257`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_java `def _generate_java(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:272`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _java_params `def _java_params(params)`
- Defined: `readmenator/_uml.py:299`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_csharp `def _generate_csharp(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:314`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _cs_params `def _cs_params(params)`
- Defined: `readmenator/_uml.py:343`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_python `def _generate_python(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:358`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_go `def _generate_go(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:393`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_rust `def _generate_rust(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:420`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_php `def _generate_php(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:446`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_kotlin `def _generate_kotlin(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:474`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_scala `def _generate_scala(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:494`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_swift `def _generate_swift(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:516`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_dart `def _generate_dart(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:545`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_ruby `def _generate_ruby(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:565`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _safe_name `def _safe_name(name)`
- Defined: `readmenator/_uml.py:586`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _extract_params `def _extract_params(signature)`
- Defined: `readmenator/_uml.py:590`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### __init__ `def __init__(self, config)`
- Defined: `readmenator/_uml.py:34`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### render_mermaid_class_diagram `def render_mermaid_class_diagram(self, nodes, edges)`
- Defined: `readmenator/_uml.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### generate_code `def generate_code(self, nodes, edges, target_language)`
- Defined: `readmenator/_uml.py:127`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _sanitize_id `def _sanitize_id(raw)`
- Defined: `readmenator/_uml.py:151`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _find_node `def _find_node(nodes, node_id)`
- Defined: `readmenator/_uml.py:163`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

## readmenator/_watcher.py

### __init__ `def __init__(self, root, config, callback, interval_seconds)`
- Defined: `readmenator/_watcher.py:29`
- Doc: Initialise the watcher for a project root.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

### _compute_snapshot `def _compute_snapshot(self)`
- Defined: `readmenator/_watcher.py:51`
- Doc: Compute a quick hash of all tracked files in the project.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

### start `def start(self)`
- Defined: `readmenator/_watcher.py:80`
- Doc: Start watching the directory (blocking).
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

### stop `def stop(self)`
- Defined: `readmenator/_watcher.py:97`
- Doc: Stop watching.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

## readmenator/parsers/__init__.py

### _init_parser_map `def _init_parser_map()`
- Defined: `readmenator/parsers/__init__.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`

### create_parser `def create_parser(extension, filename, config)`
- Defined: `readmenator/parsers/__init__.py:65`
- Doc: Factory: return a parser instance for the given file extension.
- Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`

## readmenator/parsers/_assembly.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_assembly.py:17`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`

## readmenator/parsers/_base.py

### __init__ `def __init__(self, filename, config)`
- Defined: `readmenator/parsers/_base.py:19`
- Doc: Initialise the parser with a file path and application config.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### parse `def parse(self, content)`
- Defined: `readmenator/parsers/_base.py:34`
- Doc: Parse *content* and populate symbol/import lists.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_base.py:43`
- Doc: Subclass hook for language-specific symbol extraction.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _extract_docstring `def _extract_docstring(self, line_num)`
- Defined: `readmenator/parsers/_base.py:47`
- Doc: Walk backwards from *line_num* to collect preceding comments/docstrings.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _extract_signature `def _extract_signature(self, content, match_start, pattern)`
- Defined: `readmenator/parsers/_base.py:89`
- Doc: Extract a compact signature snippet starting at *match_start*.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

## readmenator/parsers/_c.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_c.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_csharp.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_csharp.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_dart.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_dart.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_elixir.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_elixir.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_gdscript.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_gdscript.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_go.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_go.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_java.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_java.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_javascript.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_javascript.py:17`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_kotlin.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_kotlin.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_lua.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_lua.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_nim.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_nim.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_php.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_php.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_python.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_python.py:17`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_ruby.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_ruby.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_rust.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_rust.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_scala.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_scala.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_shell.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_shell.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_swift.py

### _extract_specifics `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_swift.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator_orchestrator.py

### _validate_repo_name `def _validate_repo_name(name)`
- Defined: `readmenator_orchestrator.py:50`

### _validate_branch_name `def _validate_branch_name(name)`
- Defined: `readmenator_orchestrator.py:56`

### _safe_env `def _safe_env()`
- Defined: `readmenator_orchestrator.py:62`

### parse_arguments `def parse_arguments()`
- Defined: `readmenator_orchestrator.py:438`

### main `def main()`
- Defined: `readmenator_orchestrator.py:455`

### __init__ `def __init__(self, config)`
- Defined: `readmenator_orchestrator.py:78`

### _resolve_user `def _resolve_user(self)`
- Defined: `readmenator_orchestrator.py:83`

### _setup_git_auth `def _setup_git_auth(self)`
- Defined: `readmenator_orchestrator.py:104`

### list_repos `def list_repos(self)`
- Defined: `readmenator_orchestrator.py:118`

### close_existing_prs `def close_existing_prs(self, repo)`
- Defined: `readmenator_orchestrator.py:130`

### delete_remote_branch `def delete_remote_branch(self, repo)`
- Defined: `readmenator_orchestrator.py:158`

### create_pr `def create_pr(self, repo, default_branch, timestamp)`
- Defined: `readmenator_orchestrator.py:170`

### __init__ `def __init__(self, config, github_client)`
- Defined: `readmenator_orchestrator.py:192`

### process `def process(self, repo)`
- Defined: `readmenator_orchestrator.py:196`

### _get_default_branch `def _get_default_branch(self, repo)`
- Defined: `readmenator_orchestrator.py:225`

### _clone_repository `def _clone_repository(self, repo)`
- Defined: `readmenator_orchestrator.py:241`

### _run_readmenator `def _run_readmenator(self, repo_dir)`
- Defined: `readmenator_orchestrator.py:257`

### _copy_to_docs_dir `def _copy_to_docs_dir(self, repo_dir, generated_file)`
- Defined: `readmenator_orchestrator.py:277`

### _commit_and_push `def _commit_and_push(self, repo_dir, repo)`
- Defined: `readmenator_orchestrator.py:290`

### _cleanup_temp_dir `def _cleanup_temp_dir(temp_dir)`
- Defined: `readmenator_orchestrator.py:336`

### __init__ `def __init__(self, config)`
- Defined: `readmenator_orchestrator.py:342`

### run `def run(self, dry_run, only_repo)`
- Defined: `readmenator_orchestrator.py:347`

### setUp `def setUp(self)`
- Defined: `readmenator_orchestrator.py:397`

### tearDown `def tearDown(self)`
- Defined: `readmenator_orchestrator.py:401`

### test_config_immutability `def test_config_immutability(self)`
- Defined: `readmenator_orchestrator.py:404`

### test_config_defaults `def test_config_defaults(self)`
- Defined: `readmenator_orchestrator.py:408`

### test_skip_repos_logic `def test_skip_repos_logic(self)`
- Defined: `readmenator_orchestrator.py:415`

### test_repo_name_validation `def test_repo_name_validation(self)`
- Defined: `readmenator_orchestrator.py:419`

### test_branch_name_validation `def test_branch_name_validation(self)`
- Defined: `readmenator_orchestrator.py:429`

## tests/test_agent_injector.py

### setUp `def setUp(self)`
- Defined: `tests/test_agent_injector.py:22`
- Depends on: `readmenator/_agent_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:27`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_agents_md_adds_kb_link `def test_inject_into_agents_md_adds_kb_link(self)`
- Defined: `tests/test_agent_injector.py:30`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_claude_md_adds_kb_link `def test_inject_into_claude_md_adds_kb_link(self)`
- Defined: `tests/test_agent_injector.py:39`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_cursorrules_adds_kb_link `def test_inject_into_cursorrules_adds_kb_link(self)`
- Defined: `tests/test_agent_injector.py:47`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_github_copilot_instructions `def test_inject_into_github_copilot_instructions(self)`
- Defined: `tests/test_agent_injector.py:55`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_replaces_old_injection_without_regen_command `def test_inject_replaces_old_injection_without_regen_command(self)`
- Defined: `tests/test_agent_injector.py:65`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_skips_when_already_up_to_date `def test_inject_skips_when_already_up_to_date(self)`
- Defined: `tests/test_agent_injector.py:80`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_cursor_rules_mdc_glob `def test_inject_into_cursor_rules_mdc_glob(self)`
- Defined: `tests/test_agent_injector.py:93`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_is_idempotent_does_not_duplicate `def test_inject_is_idempotent_does_not_duplicate(self)`
- Defined: `tests/test_agent_injector.py:103`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_no_agent_files_returns_zero `def test_inject_no_agent_files_returns_zero(self)`
- Defined: `tests/test_agent_injector.py:114`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_preserves_existing_content `def test_inject_preserves_existing_content(self)`
- Defined: `tests/test_agent_injector.py:118`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_multiple_agent_files `def test_inject_multiple_agent_files(self)`
- Defined: `tests/test_agent_injector.py:126`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_plain_text_format_for_yaml `def test_inject_plain_text_format_for_yaml(self)`
- Defined: `tests/test_agent_injector.py:133`
- Depends on: `readmenator/_agent_injector.py`

### test_custom_kb_filename_works `def test_custom_kb_filename_works(self)`
- Defined: `tests/test_agent_injector.py:142`
- Depends on: `readmenator/_agent_injector.py`

### test_injection_includes_regeneration_command `def test_injection_includes_regeneration_command(self)`
- Defined: `tests/test_agent_injector.py:150`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_does_not_execute_commands `def test_inject_does_not_execute_commands(self)`
- Defined: `tests/test_agent_injector.py:157`
- Depends on: `readmenator/_agent_injector.py`

### setUp `def setUp(self)`
- Defined: `tests/test_agent_injector.py:168`
- Depends on: `readmenator/_agent_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:173`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_strips_injected_section `def test_remove_strips_injected_section(self)`
- Defined: `tests/test_agent_injector.py:176`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_without_injection_returns_zero `def test_remove_without_injection_returns_zero(self)`
- Defined: `tests/test_agent_injector.py:187`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_no_files_returns_zero `def test_remove_no_files_returns_zero(self)`
- Defined: `tests/test_agent_injector.py:193`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_preserves_original_content `def test_remove_preserves_original_content(self)`
- Defined: `tests/test_agent_injector.py:197`
- Depends on: `readmenator/_agent_injector.py`

### setUp `def setUp(self)`
- Defined: `tests/test_agent_injector.py:211`
- Depends on: `readmenator/_agent_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:215`
- Depends on: `readmenator/_agent_injector.py`

### test_finds_agents_md `def test_finds_agents_md(self)`
- Defined: `tests/test_agent_injector.py:218`
- Depends on: `readmenator/_agent_injector.py`

### test_finds_all_listed_files `def test_finds_all_listed_files(self)`
- Defined: `tests/test_agent_injector.py:224`
- Depends on: `readmenator/_agent_injector.py`

### test_finds_cursor_rules_glob `def test_finds_cursor_rules_glob(self)`
- Defined: `tests/test_agent_injector.py:231`
- Depends on: `readmenator/_agent_injector.py`

### test_returns_empty_when_no_files `def test_returns_empty_when_no_files(self)`
- Defined: `tests/test_agent_injector.py:240`
- Depends on: `readmenator/_agent_injector.py`

### setUp `def setUp(self)`
- Defined: `tests/test_agent_injector.py:248`
- Depends on: `readmenator/_agent_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:253`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_empty_file `def test_inject_into_empty_file(self)`
- Defined: `tests/test_agent_injector.py:256`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_respects_custom_agent_files_list `def test_inject_respects_custom_agent_files_list(self)`
- Defined: `tests/test_agent_injector.py:264`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_does_not_touch_unlisted_files `def test_inject_does_not_touch_unlisted_files(self)`
- Defined: `tests/test_agent_injector.py:272`
- Depends on: `readmenator/_agent_injector.py`

## tests/test_agent_output.py

### _make_node `def _make_node(node_id, symbols, doc, language)`
- Defined: `tests/test_agent_output.py:19`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### _make_edge `def _make_edge(source, target, relation)`
- Defined: `tests/test_agent_output.py:30`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### _make_finding `def _make_finding(file_path, line, severity, rule_id, description, snippet, cwe)`
- Defined: `tests/test_agent_output.py:34`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_config_defaults `def test_config_defaults(self)`
- Defined: `tests/test_agent_output.py:50`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_config_immutable `def test_config_immutable(self)`
- Defined: `tests/test_agent_output.py:56`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_inferred_from_directories `def test_inferred_from_directories(self)`
- Defined: `tests/test_agent_output.py:64`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_flat_project_single_file `def test_flat_project_single_file(self)`
- Defined: `tests/test_agent_output.py:80`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_min_threshold_respected `def test_min_threshold_respected(self)`
- Defined: `tests/test_agent_output.py:91`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_misc_catches_unassigned `def test_misc_catches_unassigned(self)`
- Defined: `tests/test_agent_output.py:103`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_index_lists_all_files `def test_index_lists_all_files(self)`
- Defined: `tests/test_agent_output.py:118`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_index_table_format `def test_index_table_format(self)`
- Defined: `tests/test_agent_output.py:133`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_empty_findings `def test_empty_findings(self)`
- Defined: `tests/test_agent_output.py:144`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_findings_grouped_by_severity `def test_findings_grouped_by_severity(self)`
- Defined: `tests/test_agent_output.py:150`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_no_json_wrapping `def test_no_json_wrapping(self)`
- Defined: `tests/test_agent_output.py:166`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_god_nodes_section `def test_god_nodes_section(self)`
- Defined: `tests/test_agent_output.py:176`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_cycles_section `def test_cycles_section(self)`
- Defined: `tests/test_agent_output.py:192`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_empty_gotchas `def test_empty_gotchas(self)`
- Defined: `tests/test_agent_output.py:209`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_internal_dependencies `def test_internal_dependencies(self)`
- Defined: `tests/test_agent_output.py:217`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_external_imports `def test_external_imports(self)`
- Defined: `tests/test_agent_output.py:228`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_functions_listed `def test_functions_listed(self)`
- Defined: `tests/test_agent_output.py:239`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_no_json_in_api `def test_no_json_in_api(self)`
- Defined: `tests/test_agent_output.py:253`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_subsystem_files_written `def test_subsystem_files_written(self)`
- Defined: `tests/test_agent_output.py:265`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_recipes_directory `def test_recipes_directory(self)`
- Defined: `tests/test_agent_output.py:287`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_generate_creates_all_files `def test_generate_creates_all_files(self)`
- Defined: `tests/test_agent_output.py:302`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_all_files_under_500_lines `def test_all_files_under_500_lines(self)`
- Defined: `tests/test_agent_output.py:333`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_no_json_in_any_output `def test_no_json_in_any_output(self)`
- Defined: `tests/test_agent_output.py:348`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_agent_injector_detects_outdated `def test_agent_injector_detects_outdated(self)`
- Defined: `tests/test_agent_output.py:362`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_agent_injector_skips_identical `def test_agent_injector_skips_identical(self)`
- Defined: `tests/test_agent_output.py:384`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_readme_injector_detects_outdated `def test_readme_injector_detects_outdated(self)`
- Defined: `tests/test_agent_output.py:400`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_readme_injector_skips_identical `def test_readme_injector_skips_identical(self)`
- Defined: `tests/test_agent_output.py:422`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

## tests/test_analyzer.py

### setUp `def setUp(self)`
- Defined: `tests/test_analyzer.py:19`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_analyzer.py:23`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### _make_edge `def _make_edge(self, src, tgt, rel)`
- Defined: `tests/test_analyzer.py:26`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_empty_graph_returns_empty_result `def test_analyze_empty_graph_returns_empty_result(self)`
- Defined: `tests/test_analyzer.py:29`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_detects_communities_for_connected_graph `def test_analyze_detects_communities_for_connected_graph(self)`
- Defined: `tests/test_analyzer.py:34`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_computes_god_nodes `def test_analyze_computes_god_nodes(self)`
- Defined: `tests/test_analyzer.py:48`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_finds_surprising_connections `def test_analyze_finds_surprising_connections(self)`
- Defined: `tests/test_analyzer.py:64`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_generates_questions `def test_analyze_generates_questions(self)`
- Defined: `tests/test_analyzer.py:81`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_community_cohesion_is_between_zero_and_one `def test_community_cohesion_is_between_zero_and_one(self)`
- Defined: `tests/test_analyzer.py:92`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_isolated_nodes_do_not_form_communities `def test_isolated_nodes_do_not_form_communities(self)`
- Defined: `tests/test_analyzer.py:107`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_with_resolved_edges_counts_them `def test_analyze_with_resolved_edges_counts_them(self)`
- Defined: `tests/test_analyzer.py:116`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

## tests/test_cache.py

### setUp `def setUp(self)`
- Defined: `tests/test_cache.py:21`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_cache.py:26`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### _write `def _write(self, rel_path, content)`
- Defined: `tests/test_cache.py:30`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_compute_hash_returns_hex_string `def test_compute_hash_returns_hex_string(self)`
- Defined: `tests/test_cache.py:36`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_different_content_produces_different_hash `def test_different_content_produces_different_hash(self)`
- Defined: `tests/test_cache.py:42`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_same_content_produces_same_hash `def test_same_content_produces_same_hash(self)`
- Defined: `tests/test_cache.py:49`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_load_returns_empty_dict_when_no_cache `def test_load_returns_empty_dict_when_no_cache(self)`
- Defined: `tests/test_cache.py:56`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_save_and_load_roundtrip `def test_save_and_load_roundtrip(self)`
- Defined: `tests/test_cache.py:60`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_find_changed_detects_new_files `def test_find_changed_detects_new_files(self)`
- Defined: `tests/test_cache.py:66`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_find_changed_detects_modified_files `def test_find_changed_detects_modified_files(self)`
- Defined: `tests/test_cache.py:71`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_find_changed_skips_unchanged_files `def test_find_changed_skips_unchanged_files(self)`
- Defined: `tests/test_cache.py:78`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_prune_deleted_removes_ghost_entries `def test_prune_deleted_removes_ghost_entries(self)`
- Defined: `tests/test_cache.py:85`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_compute_hashes_batch `def test_compute_hashes_batch(self)`
- Defined: `tests/test_cache.py:92`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_nonexistent_file_returns_empty_hash `def test_nonexistent_file_returns_empty_hash(self)`
- Defined: `tests/test_cache.py:100`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_save_and_load_analysis_roundtrip `def test_save_and_load_analysis_roundtrip(self)`
- Defined: `tests/test_cache.py:109`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_load_missing_analysis_key_returns_none `def test_load_missing_analysis_key_returns_none(self)`
- Defined: `tests/test_cache.py:116`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_clear_analysis_specific_key `def test_clear_analysis_specific_key(self)`
- Defined: `tests/test_cache.py:120`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_clear_analysis_all_keys `def test_clear_analysis_all_keys(self)`
- Defined: `tests/test_cache.py:127`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_has_changed_since_last_analysis_returns_true_on_first_run `def test_has_changed_since_last_analysis_returns_true_on_first_run(self)`
- Defined: `tests/test_cache.py:134`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_has_changed_since_last_analysis_returns_false_when_no_changes `def test_has_changed_since_last_analysis_returns_false_when_no_changes(self)`
- Defined: `tests/test_cache.py:139`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_has_changed_since_last_analysis_returns_true_when_file_changed `def test_has_changed_since_last_analysis_returns_true_when_file_changed(self)`
- Defined: `tests/test_cache.py:147`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

## tests/test_config.py

### test_config_is_immutable `def test_config_is_immutable(self)`
- Defined: `tests/test_config.py:8`
- Depends on: `readmenator/_config.py`

### test_config_defaults_are_sane `def test_config_defaults_are_sane(self)`
- Defined: `tests/test_config.py:13`
- Depends on: `readmenator/_config.py`

### test_ignore_dirs_are_comprehensive `def test_ignore_dirs_are_comprehensive(self)`
- Defined: `tests/test_config.py:24`
- Depends on: `readmenator/_config.py`

### test_plural_map_covers_all_symbol_types `def test_plural_map_covers_all_symbol_types(self)`
- Defined: `tests/test_config.py:30`
- Depends on: `readmenator/_config.py`

### test_supported_extensions_no_duplicates `def test_supported_extensions_no_duplicates(self)`
- Defined: `tests/test_config.py:41`
- Depends on: `readmenator/_config.py`

## tests/test_cpg.py

### setUp `def setUp(self)`
- Defined: `tests/test_cpg.py:14`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_cpg.py:18`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### _make_sym `def _make_sym(self, name, kind, line)`
- Defined: `tests/test_cpg.py:21`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_returns_valid_json `def test_generate_returns_valid_json(self)`
- Defined: `tests/test_cpg.py:24`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_includes_node_data `def test_generate_includes_node_data(self)`
- Defined: `tests/test_cpg.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_includes_edges `def test_generate_includes_edges(self)`
- Defined: `tests/test_cpg.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_includes_metadata `def test_generate_includes_metadata(self)`
- Defined: `tests/test_cpg.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_privacy_mode_strips_docs `def test_privacy_mode_strips_docs(self)`
- Defined: `tests/test_cpg.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_sha256_hash_included `def test_sha256_hash_included(self)`
- Defined: `tests/test_cpg.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_empty_graph_returns_valid_json `def test_empty_graph_returns_valid_json(self)`
- Defined: `tests/test_cpg.py:96`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

## tests/test_cursorrules.py

### setUp `def setUp(self)`
- Defined: `tests/test_cursorrules.py:21`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_returns_string `def test_generate_returns_string(self)`
- Defined: `tests/test_cursorrules.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_contains_header `def test_generate_contains_header(self)`
- Defined: `tests/test_cursorrules.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_contains_base_rules `def test_generate_contains_base_rules(self)`
- Defined: `tests/test_cursorrules.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_layer_constraints `def test_generate_includes_layer_constraints(self)`
- Defined: `tests/test_cursorrules.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_god_nodes `def test_generate_includes_god_nodes(self)`
- Defined: `tests/test_cursorrules.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_communities `def test_generate_includes_communities(self)`
- Defined: `tests/test_cursorrules.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_violations `def test_generate_includes_violations(self)`
- Defined: `tests/test_cursorrules.py:82`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_limits_violations_to_ten `def test_generate_limits_violations_to_ten(self)`
- Defined: `tests/test_cursorrules.py:95`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_writes_file_when_project_root `def test_generate_writes_file_when_project_root(self)`
- Defined: `tests/test_cursorrules.py:103`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_idempotent `def test_generate_idempotent(self)`
- Defined: `tests/test_cursorrules.py:111`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

## tests/test_dead_code.py

### setUp `def setUp(self)`
- Defined: `tests/test_dead_code.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### _make_symbol `def _make_symbol(self, name, kind)`
- Defined: `tests/test_dead_code.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, symbols)`
- Defined: `tests/test_dead_code.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### _make_edge `def _make_edge(self, src, tgt)`
- Defined: `tests/test_dead_code.py:35`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_empty_graph_returns_empty `def test_identify_empty_graph_returns_empty(self)`
- Defined: `tests/test_dead_code.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_finds_dead_symbol `def test_identify_finds_dead_symbol(self)`
- Defined: `tests/test_dead_code.py:42`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_excludes_entry_points `def test_identify_excludes_entry_points(self)`
- Defined: `tests/test_dead_code.py:53`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_excludes_app_entry_point `def test_identify_excludes_app_entry_point(self)`
- Defined: `tests/test_dead_code.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_excludes_init_entry_point `def test_identify_excludes_init_entry_point(self)`
- Defined: `tests/test_dead_code.py:69`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_recommends_review_for_classes `def test_identify_recommends_review_for_classes(self)`
- Defined: `tests/test_dead_code.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_recommends_trash_for_functions `def test_identify_recommends_trash_for_functions(self)`
- Defined: `tests/test_dead_code.py:85`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_recommends_trash_for_variables `def test_identify_recommends_trash_for_variables(self)`
- Defined: `tests/test_dead_code.py:93`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_all_symbols_imported_returns_empty `def test_all_symbols_imported_returns_empty(self)`
- Defined: `tests/test_dead_code.py:101`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_reports_sorted_by_file_path `def test_reports_sorted_by_file_path(self)`
- Defined: `tests/test_dead_code.py:113`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

## tests/test_documentation.py

### setUp `def setUp(self)`
- Defined: `tests/test_documentation.py:18`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_header `def test_contains_header(self)`
- Defined: `tests/test_documentation.py:22`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_metadata_line `def test_contains_metadata_line(self)`
- Defined: `tests/test_documentation.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_mermaid_block `def test_contains_mermaid_block(self)`
- Defined: `tests/test_documentation.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_architecture_reference `def test_contains_architecture_reference(self)`
- Defined: `tests/test_documentation.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_cpg_block `def test_contains_cpg_block(self)`
- Defined: `tests/test_documentation.py:41`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_statistics_dashboard `def test_contains_statistics_dashboard(self)`
- Defined: `tests/test_documentation.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_groups_files_by_language `def test_groups_files_by_language(self)`
- Defined: `tests/test_documentation.py:51`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_lists_symbols_under_file `def test_lists_symbols_under_file(self)`
- Defined: `tests/test_documentation.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_class_symbol_is_pluralized_correctly `def test_class_symbol_is_pluralized_correctly(self)`
- Defined: `tests/test_documentation.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_function_pluralization `def test_function_pluralization(self)`
- Defined: `tests/test_documentation.py:97`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_method_pluralization `def test_method_pluralization(self)`
- Defined: `tests/test_documentation.py:109`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_shows_no_symbols_for_empty_files `def test_shows_no_symbols_for_empty_files(self)`
- Defined: `tests/test_documentation.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_includes_file_path `def test_includes_file_path(self)`
- Defined: `tests/test_documentation.py:132`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_docstring_in_output `def test_docstring_in_output(self)`
- Defined: `tests/test_documentation.py:143`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_truncation_note_when_limited `def test_truncation_note_when_limited(self)`
- Defined: `tests/test_documentation.py:155`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_taint_propagation_section_present `def test_taint_propagation_section_present(self)`
- Defined: `tests/test_documentation.py:165`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_hotspot_section_present `def test_hotspot_section_present(self)`
- Defined: `tests/test_documentation.py:185`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_no_taint_section_when_empty `def test_no_taint_section_when_empty(self)`
- Defined: `tests/test_documentation.py:203`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_no_hotspot_section_when_empty `def test_no_hotspot_section_when_empty(self)`
- Defined: `tests/test_documentation.py:207`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_cpg_block_disabled_via_config `def test_cpg_block_disabled_via_config(self)`
- Defined: `tests/test_documentation.py:211`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_architectural_layers_section `def test_architectural_layers_section(self)`
- Defined: `tests/test_documentation.py:217`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_security_findings_section `def test_security_findings_section(self)`
- Defined: `tests/test_documentation.py:229`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_zero_returns_full_content `def test_context_budget_zero_returns_full_content(self)`
- Defined: `tests/test_documentation.py:252`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_returns_compact_summary `def test_context_budget_returns_compact_summary(self)`
- Defined: `tests/test_documentation.py:260`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_prioritizes_god_nodes `def test_context_budget_prioritizes_god_nodes(self)`
- Defined: `tests/test_documentation.py:268`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_truncates_at_limit `def test_context_budget_truncates_at_limit(self)`
- Defined: `tests/test_documentation.py:285`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_includes_security_findings `def test_context_budget_includes_security_findings(self)`
- Defined: `tests/test_documentation.py:293`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

## tests/test_exporter.py

### setUp `def setUp(self)`
- Defined: `tests/test_exporter.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, label, lang, symbols)`
- Defined: `tests/test_exporter.py:30`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### _make_sym `def _make_sym(self, name, kind, line)`
- Defined: `tests/test_exporter.py:42`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_produces_valid_json `def test_to_json_produces_valid_json(self)`
- Defined: `tests/test_exporter.py:47`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_includes_symbol_data `def test_to_json_includes_symbol_data(self)`
- Defined: `tests/test_exporter.py:56`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_includes_metadata `def test_to_json_includes_metadata(self)`
- Defined: `tests/test_exporter.py:65`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_includes_analysis_metadata `def test_to_json_includes_analysis_metadata(self)`
- Defined: `tests/test_exporter.py:76`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_html_produces_standalone_page `def test_to_html_produces_standalone_page(self)`
- Defined: `tests/test_exporter.py:101`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_html_includes_node_data `def test_to_html_includes_node_data(self)`
- Defined: `tests/test_exporter.py:109`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_html_includes_community_legend_when_analysis `def test_to_html_includes_community_legend_when_analysis(self)`
- Defined: `tests/test_exporter.py:116`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_svg_produces_svg_string `def test_to_svg_produces_svg_string(self)`
- Defined: `tests/test_exporter.py:138`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_svg_render_truncation_for_large_graph `def test_to_svg_render_truncation_for_large_graph(self)`
- Defined: `tests/test_exporter.py:145`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_svg_includes_readmenator_title `def test_to_svg_includes_readmenator_title(self)`
- Defined: `tests/test_exporter.py:154`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_handles_resolved_edges `def test_to_json_handles_resolved_edges(self)`
- Defined: `tests/test_exporter.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

## tests/test_hotspots.py

### setUp `def setUp(self)`
- Defined: `tests/test_hotspots.py:13`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, label, sym_count)`
- Defined: `tests/test_hotspots.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_empty_graph_returns_empty_hotspots `def test_empty_graph_returns_empty_hotspots(self)`
- Defined: `tests/test_hotspots.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_hotspots_rank_by_combined_score `def test_hotspots_rank_by_combined_score(self)`
- Defined: `tests/test_hotspots.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_hotspot_includes_scores `def test_hotspot_includes_scores(self)`
- Defined: `tests/test_hotspots.py:43`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_no_cycles_in_acyclic_graph `def test_no_cycles_in_acyclic_graph(self)`
- Defined: `tests/test_hotspots.py:53`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_detects_simple_cycle `def test_detects_simple_cycle(self)`
- Defined: `tests/test_hotspots.py:66`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_change_impact_ranks_by_total_impact `def test_change_impact_ranks_by_total_impact(self)`
- Defined: `tests/test_hotspots.py:79`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_change_impact_no_edges `def test_change_impact_no_edges(self)`
- Defined: `tests/test_hotspots.py:94`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_hotspot_weights_from_config `def test_hotspot_weights_from_config(self)`
- Defined: `tests/test_hotspots.py:100`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

## tests/test_integration.py

### setUp `def setUp(self)`
- Defined: `tests/test_integration.py:10`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_integration.py:15`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### _write `def _write(self, path, content)`
- Defined: `tests/test_integration.py:19`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_full_pipeline_generates_knowledge_base `def test_full_pipeline_generates_knowledge_base(self)`
- Defined: `tests/test_integration.py:24`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_knowledge_base_contains_mermaid `def test_knowledge_base_contains_mermaid(self)`
- Defined: `tests/test_integration.py:40`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_query_subcommand_works `def test_query_subcommand_works(self)`
- Defined: `tests/test_integration.py:48`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_explain_subcommand_works `def test_explain_subcommand_works(self)`
- Defined: `tests/test_integration.py:53`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_path_subcommand_works `def test_path_subcommand_works(self)`
- Defined: `tests/test_integration.py:59`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_summary_works `def test_summary_works(self)`
- Defined: `tests/test_integration.py:65`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_rebuild `def test_rebuild(self)`
- Defined: `tests/test_integration.py:71`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_knowledge_base_contains_cpg `def test_knowledge_base_contains_cpg(self)`
- Defined: `tests/test_integration.py:81`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_knowledge_base_contains_statistics_dashboard `def test_knowledge_base_contains_statistics_dashboard(self)`
- Defined: `tests/test_integration.py:89`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_audit_deep_returns_analysis `def test_audit_deep_returns_analysis(self)`
- Defined: `tests/test_integration.py:98`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_privacy_mode_works `def test_privacy_mode_works(self)`
- Defined: `tests/test_integration.py:105`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_export_sarif_produces_file `def test_export_sarif_produces_file(self)`
- Defined: `tests/test_integration.py:114`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

## tests/test_layer_rules.py

### setUp `def setUp(self)`
- Defined: `tests/test_layer_rules.py:13`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, label)`
- Defined: `tests/test_layer_rules.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_empty_graph_returns_empty_violations `def test_empty_graph_returns_empty_violations(self)`
- Defined: `tests/test_layer_rules.py:20`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_no_layers_returns_empty_violations `def test_no_layers_returns_empty_violations(self)`
- Defined: `tests/test_layer_rules.py:24`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_same_layer_no_violation `def test_same_layer_no_violation(self)`
- Defined: `tests/test_layer_rules.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_forbidden_edge_detected `def test_forbidden_edge_detected(self)`
- Defined: `tests/test_layer_rules.py:36`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_allowed_testing_edges_no_violation `def test_allowed_testing_edges_no_violation(self)`
- Defined: `tests/test_layer_rules.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_multiple_violations `def test_multiple_violations(self)`
- Defined: `tests/test_layer_rules.py:57`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_utility_layer_ignored `def test_utility_layer_ignored(self)`
- Defined: `tests/test_layer_rules.py:75`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_violation_summary `def test_violation_summary(self)`
- Defined: `tests/test_layer_rules.py:82`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_resolved_edges_also_checked `def test_resolved_edges_also_checked(self)`
- Defined: `tests/test_layer_rules.py:104`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_presentation_to_data_access_forbidden `def test_presentation_to_data_access_forbidden(self)`
- Defined: `tests/test_layer_rules.py:115`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

## tests/test_linter.py

### setUp `def setUp(self)`
- Defined: `tests/test_linter.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### _make_node `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_linter.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### _make_edge `def _make_edge(self, src, tgt, rel)`
- Defined: `tests/test_linter.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_empty_graph_returns_no_violations `def test_lint_empty_graph_returns_no_violations(self)`
- Defined: `tests/test_linter.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_returns_empty_for_files_under_threshold `def test_lint_returns_empty_for_files_under_threshold(self)`
- Defined: `tests/test_linter.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_detects_file_exceeding_max_lines `def test_lint_detects_file_exceeding_max_lines(self)`
- Defined: `tests/test_linter.py:40`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_detects_cross_layer_violation `def test_lint_detects_cross_layer_violation(self)`
- Defined: `tests/test_linter.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_allows_same_layer_imports `def test_lint_allows_same_layer_imports(self)`
- Defined: `tests/test_linter.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_allows_testing_to_business_logic `def test_lint_allows_testing_to_business_logic(self)`
- Defined: `tests/test_linter.py:72`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_ignores_utility_layer `def test_lint_ignores_utility_layer(self)`
- Defined: `tests/test_linter.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_detects_circular_dependencies `def test_lint_detects_circular_dependencies(self)`
- Defined: `tests/test_linter.py:94`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_violations_sorted_by_severity `def test_violations_sorted_by_severity(self)`
- Defined: `tests/test_linter.py:108`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_returns_empty_when_disabled `def test_lint_returns_empty_when_disabled(self)`
- Defined: `tests/test_linter.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

## tests/test_mcp_server.py

### setUp `def setUp(self)`
- Defined: `tests/test_mcp_server.py:24`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_mcp_server.py:33`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### _make_request `def _make_request(self, method, params, msg_id)`
- Defined: `tests/test_mcp_server.py:36`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### _call `def _call(self, req)`
- Defined: `tests/test_mcp_server.py:42`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_initialize_exchanges_protocol_version `def test_initialize_exchanges_protocol_version(self)`
- Defined: `tests/test_mcp_server.py:49`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_notifications_initialized_returns_no_response `def test_notifications_initialized_returns_no_response(self)`
- Defined: `tests/test_mcp_server.py:62`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_unknown_method_returns_error `def test_unknown_method_returns_error(self)`
- Defined: `tests/test_mcp_server.py:67`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_uninitialized_request_returns_error `def test_uninitialized_request_returns_error(self)`
- Defined: `tests/test_mcp_server.py:75`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_list_tools_returns_all_tool_definitions `def test_list_tools_returns_all_tool_definitions(self)`
- Defined: `tests/test_mcp_server.py:85`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_tool_without_initialize_returns_error `def test_call_tool_without_initialize_returns_error(self)`
- Defined: `tests/test_mcp_server.py:115`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_tool_unknown_tool_returns_method_not_found `def test_call_tool_unknown_tool_returns_method_not_found(self)`
- Defined: `tests/test_mcp_server.py:123`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_summary_tool_returns_content `def test_call_summary_tool_returns_content(self)`
- Defined: `tests/test_mcp_server.py:132`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_query_tool_with_text_returns_results `def test_call_query_tool_with_text_returns_results(self)`
- Defined: `tests/test_mcp_server.py:145`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_query_tool_missing_required_param_raises `def test_call_query_tool_missing_required_param_raises(self)`
- Defined: `tests/test_mcp_server.py:154`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_list_resources_returns_resource_definitions `def test_list_resources_returns_resource_definitions(self)`
- Defined: `tests/test_mcp_server.py:168`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_read_resource_summary_returns_json `def test_read_resource_summary_returns_json(self)`
- Defined: `tests/test_mcp_server.py:186`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_read_resource_unknown_uri_returns_error `def test_read_resource_unknown_uri_returns_error(self)`
- Defined: `tests/test_mcp_server.py:197`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_read_resource_kb_returns_markdown `def test_read_resource_kb_returns_markdown(self)`
- Defined: `tests/test_mcp_server.py:205`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### _get_tool_def `def _get_tool_def(self, name)`
- Defined: `tests/test_mcp_server.py:219`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_query_tool_requires_text_param `def test_query_tool_requires_text_param(self)`
- Defined: `tests/test_mcp_server.py:226`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_explain_tool_requires_name_param `def test_explain_tool_requires_name_param(self)`
- Defined: `tests/test_mcp_server.py:230`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_path_tool_requires_two_params `def test_path_tool_requires_two_params(self)`
- Defined: `tests/test_mcp_server.py:234`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_parse_error_for_invalid_json `def test_parse_error_for_invalid_json(self)`
- Defined: `tests/test_mcp_server.py:243`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_tool_returns_text_content_list `def test_call_tool_returns_text_content_list(self)`
- Defined: `tests/test_mcp_server.py:251`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

## tests/test_mermaid.py

### setUp `def setUp(self)`
- Defined: `tests/test_mermaid.py:8`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_renders_graph_header `def test_renders_graph_header(self)`
- Defined: `tests/test_mermaid.py:11`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_renders_module_node `def test_renders_module_node(self)`
- Defined: `tests/test_mermaid.py:19`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_renders_symbol_subnodes `def test_renders_symbol_subnodes(self)`
- Defined: `tests/test_mermaid.py:27`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_class_symbol_gets_cls_style `def test_class_symbol_gets_cls_style(self)`
- Defined: `tests/test_mermaid.py:36`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_function_symbol_gets_fn_style `def test_function_symbol_gets_fn_style(self)`
- Defined: `tests/test_mermaid.py:45`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_external_import_edge_is_dashed `def test_external_import_edge_is_dashed(self)`
- Defined: `tests/test_mermaid.py:54`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_truncation_when_over_limit `def test_truncation_when_over_limit(self)`
- Defined: `tests/test_mermaid.py:62`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_limits_symbols_to_five_per_node `def test_limits_symbols_to_five_per_node(self)`
- Defined: `tests/test_mermaid.py:72`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_handles_special_characters_in_ids `def test_handles_special_characters_in_ids(self)`
- Defined: `tests/test_mermaid.py:82`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

## tests/test_models.py

### test_symbol_creation `def test_symbol_creation(self)`
- Defined: `tests/test_models.py:7`
- Depends on: `readmenator/_models.py`

### test_symbol_with_signature `def test_symbol_with_signature(self)`
- Defined: `tests/test_models.py:15`
- Depends on: `readmenator/_models.py`

### test_node_creation `def test_node_creation(self)`
- Defined: `tests/test_models.py:21`
- Depends on: `readmenator/_models.py`

### test_node_with_symbols `def test_node_with_symbols(self)`
- Defined: `tests/test_models.py:35`
- Depends on: `readmenator/_models.py`

### test_edge_creation `def test_edge_creation(self)`
- Defined: `tests/test_models.py:49`
- Depends on: `readmenator/_models.py`

### test_pluralize_class `def test_pluralize_class(self)`
- Defined: `tests/test_models.py:57`
- Depends on: `readmenator/_models.py`

### test_pluralize_unknown_appends_s `def test_pluralize_unknown_appends_s(self)`
- Defined: `tests/test_models.py:62`
- Depends on: `readmenator/_models.py`

## tests/test_parsers.py

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_struct `def test_extracts_struct(self)`
- Defined: `tests/test_parsers.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_include `def test_extracts_include(self)`
- Defined: `tests/test_parsers.py:40`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_define `def test_extracts_define(self)`
- Defined: `tests/test_parsers.py:47`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_skips_reserved_words `def test_skips_reserved_words(self)`
- Defined: `tests/test_parsers.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_class_with_inheritance `def test_class_with_inheritance(self)`
- Defined: `tests/test_parsers.py:64`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:73`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:76`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_imports `def test_extracts_imports(self)`
- Defined: `tests/test_parsers.py:90`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_async_function `def test_extracts_async_function(self)`
- Defined: `tests/test_parsers.py:98`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_handles_syntax_error_gracefully `def test_handles_syntax_error_gracefully(self)`
- Defined: `tests/test_parsers.py:105`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_suppresses_syntax_warnings `def test_suppresses_syntax_warnings(self)`
- Defined: `tests/test_parsers.py:111`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_signature_with_params `def test_extracts_signature_with_params(self)`
- Defined: `tests/test_parsers.py:123`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class_with_bases `def test_extracts_class_with_bases(self)`
- Defined: `tests/test_parsers.py:131`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:142`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:145`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method_receiver `def test_extracts_method_receiver(self)`
- Defined: `tests/test_parsers.py:152`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import_block `def test_extracts_import_block(self)`
- Defined: `tests/test_parsers.py:159`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_single_import `def test_extracts_single_import(self)`
- Defined: `tests/test_parsers.py:166`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_struct_and_interface `def test_extracts_struct_and_interface(self)`
- Defined: `tests/test_parsers.py:172`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:185`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_pub_function `def test_extracts_pub_function(self)`
- Defined: `tests/test_parsers.py:195`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_struct_and_trait_and_enum `def test_extracts_struct_and_trait_and_enum(self)`
- Defined: `tests/test_parsers.py:202`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_use `def test_extracts_use(self)`
- Defined: `tests/test_parsers.py:215`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:223`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:226`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_arrow_function `def test_extracts_arrow_function(self)`
- Defined: `tests/test_parsers.py:233`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:240`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import_and_require `def test_extracts_import_and_require(self)`
- Defined: `tests/test_parsers.py:247`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_skips_reserved_words `def test_skips_reserved_words(self)`
- Defined: `tests/test_parsers.py:254`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:262`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:265`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method `def test_extracts_method(self)`
- Defined: `tests/test_parsers.py:272`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import `def test_extracts_import(self)`
- Defined: `tests/test_parsers.py:279`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_abstract_class `def test_abstract_class(self)`
- Defined: `tests/test_parsers.py:285`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:294`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:297`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method `def test_extracts_method(self)`
- Defined: `tests/test_parsers.py:304`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_using `def test_extracts_using(self)`
- Defined: `tests/test_parsers.py:311`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_record_and_interface `def test_record_and_interface(self)`
- Defined: `tests/test_parsers.py:317`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:327`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function_with_parentheses `def test_extracts_function_with_parentheses(self)`
- Defined: `tests/test_parsers.py:330`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function_keyword `def test_extracts_function_keyword(self)`
- Defined: `tests/test_parsers.py:337`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:346`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:349`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:356`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_use_and_require `def test_extracts_use_and_require(self)`
- Defined: `tests/test_parsers.py:363`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:372`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:375`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:382`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import `def test_extracts_import(self)`
- Defined: `tests/test_parsers.py:389`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:397`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:400`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_extends `def test_extracts_extends(self)`
- Defined: `tests/test_parsers.py:407`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:415`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_proc `def test_extracts_proc(self)`
- Defined: `tests/test_parsers.py:418`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_type `def test_extracts_type(self)`
- Defined: `tests/test_parsers.py:425`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import `def test_extracts_import(self)`
- Defined: `tests/test_parsers.py:432`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:441`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_label `def test_extracts_label(self)`
- Defined: `tests/test_parsers.py:444`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_multiple_labels `def test_extracts_multiple_labels(self)`
- Defined: `tests/test_parsers.py:451`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers.py:461`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_c_parser_for_c_extensions `def test_returns_c_parser_for_c_extensions(self)`
- Defined: `tests/test_parsers.py:464`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_python_parser_for_py `def test_returns_python_parser_for_py(self)`
- Defined: `tests/test_parsers.py:470`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_none_for_unknown_extension `def test_returns_none_for_unknown_extension(self)`
- Defined: `tests/test_parsers.py:475`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_rust_parser_for_rs `def test_returns_rust_parser_for_rs(self)`
- Defined: `tests/test_parsers.py:479`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_case_insensitive_extension `def test_case_insensitive_extension(self)`
- Defined: `tests/test_parsers.py:484`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

## tests/test_parsers_new.py

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:16`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class_with_inheritance `def test_extracts_class_with_inheritance(self)`
- Defined: `tests/test_parsers_new.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_module `def test_extracts_module(self)`
- Defined: `tests/test_parsers_new.py:27`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method `def test_extracts_method(self)`
- Defined: `tests/test_parsers_new.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_require `def test_extracts_require(self)`
- Defined: `tests/test_parsers_new.py:39`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers_new.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers_new.py:55`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_protocol `def test_extracts_protocol(self)`
- Defined: `tests/test_parsers_new.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:69`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class `def test_extracts_class(self)`
- Defined: `tests/test_parsers_new.py:72`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_fun `def test_extracts_fun(self)`
- Defined: `tests/test_parsers_new.py:78`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:86`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_object `def test_extracts_object(self)`
- Defined: `tests/test_parsers_new.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_def `def test_extracts_def(self)`
- Defined: `tests/test_parsers_new.py:95`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:103`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers_new.py:106`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_require `def test_extracts_require(self)`
- Defined: `tests/test_parsers_new.py:111`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:118`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_defmodule `def test_extracts_defmodule(self)`
- Defined: `tests/test_parsers_new.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function `def test_extracts_function(self)`
- Defined: `tests/test_parsers_new.py:127`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:135`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_ruby_extension_maps_correctly `def test_ruby_extension_maps_correctly(self)`
- Defined: `tests/test_parsers_new.py:138`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_swift_extension_maps_correctly `def test_swift_extension_maps_correctly(self)`
- Defined: `tests/test_parsers_new.py:142`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_kotlin_extension_maps_correctly `def test_kotlin_extension_maps_correctly(self)`
- Defined: `tests/test_parsers_new.py:146`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_new.py:152`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class_inheritance `def test_extracts_class_inheritance(self)`
- Defined: `tests/test_parsers_new.py:155`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function_calls `def test_extracts_function_calls(self)`
- Defined: `tests/test_parsers_new.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

## tests/test_parsers_property.py

### _generate_multiline_code `def _generate_multiline_code(lines, line_strategy)`
- Defined: `tests/test_parsers_property.py:67`
- Doc: Generate source code with a configurable number of lines.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _create_parser `def _create_parser(ext)`
- Defined: `tests/test_parsers_property.py:104`
- Doc: Create a parser for the given extension.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_never_crashes_on_malformed_code `def test_never_crashes_on_malformed_code(self, ext, code)`
- Defined: `tests/test_parsers_property.py:124`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_never_crashes_on_unicode_code `def test_never_crashes_on_unicode_code(self, ext, code)`
- Defined: `tests/test_parsers_property.py:142`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_empty_code_returns_empty_or_valid `def test_empty_code_returns_empty_or_valid(self, ext)`
- Defined: `tests/test_parsers_property.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_whitespace_code_returns_empty_or_valid `def test_whitespace_code_returns_empty_or_valid(self, ext)`
- Defined: `tests/test_parsers_property.py:170`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_never_crashes_on_many_lines `def test_never_crashes_on_many_lines(self, ext, lines)`
- Defined: `tests/test_parsers_property.py:182`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_repeated_keywords_no_crash `def test_repeated_keywords_no_crash(self, ext)`
- Defined: `tests/test_parsers_property.py:200`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_parser_imports_is_list_of_strings `def test_parser_imports_is_list_of_strings(self, ext)`
- Defined: `tests/test_parsers_property.py:219`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_unknown_extension_returns_none `def test_unknown_extension_returns_none(self)`
- Defined: `tests/test_parsers_property.py:231`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _assert_valid_symbols `def _assert_valid_symbols(self, symbols)`
- Defined: `tests/test_parsers_property.py:237`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### setUp `def setUp(self)`
- Defined: `tests/test_parsers_property.py:253`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_python_never_crashes_on_weird_ascii `def test_python_never_crashes_on_weird_ascii(self, code)`
- Defined: `tests/test_parsers_property.py:258`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_python_never_crashes_on_any_text `def test_python_never_crashes_on_any_text(self, code)`
- Defined: `tests/test_parsers_property.py:272`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

## tests/test_query.py

### _make_node `def _make_node(node_id, symbols)`
- Defined: `tests/test_query.py:7`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### _make_sym `def _make_sym(name, kind, line)`
- Defined: `tests/test_query.py:18`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### setUp `def setUp(self)`
- Defined: `tests/test_query.py:23`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_exact_symbol `def test_find_exact_symbol(self)`
- Defined: `tests/test_query.py:36`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_symbol_fuzzy `def test_find_symbol_fuzzy(self)`
- Defined: `tests/test_query.py:42`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_symbol_not_found `def test_find_symbol_not_found(self)`
- Defined: `tests/test_query.py:47`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_returns_details `def test_explain_returns_details(self)`
- Defined: `tests/test_query.py:51`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_shows_imports `def test_explain_shows_imports(self)`
- Defined: `tests/test_query.py:58`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_shows_siblings `def test_explain_shows_siblings(self)`
- Defined: `tests/test_query.py:63`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_unknown_returns_none `def test_explain_unknown_returns_none(self)`
- Defined: `tests/test_query.py:69`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_path_direct_import `def test_find_path_direct_import(self)`
- Defined: `tests/test_query.py:73`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_path_same_file `def test_find_path_same_file(self)`
- Defined: `tests/test_query.py:79`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_path_unknown_returns_none `def test_find_path_unknown_returns_none(self)`
- Defined: `tests/test_query.py:84`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_summary_shows_counts `def test_summary_shows_counts(self)`
- Defined: `tests/test_query.py:88`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_summary_shows_top_modules `def test_summary_shows_top_modules(self)`
- Defined: `tests/test_query.py:94`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_query_returns_matching_symbols `def test_query_returns_matching_symbols(self)`
- Defined: `tests/test_query.py:98`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_query_returns_file_matches `def test_query_returns_file_matches(self)`
- Defined: `tests/test_query.py:102`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

## tests/test_ranking.py

### _make_test_graph `def _make_test_graph()`
- Defined: `tests/test_ranking.py:238`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_all_edge_kinds_have_weights `def test_all_edge_kinds_have_weights(self)`
- Defined: `tests/test_ranking.py:61`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_infer_edge_kind_maps_correctly `def test_infer_edge_kind_maps_correctly(self)`
- Defined: `tests/test_ranking.py:66`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_infer_edge_kind_falls_back `def test_infer_edge_kind_falls_back(self)`
- Defined: `tests/test_ranking.py:71`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_edge_kind_is_str_enum `def test_edge_kind_is_str_enum(self)`
- Defined: `tests/test_ranking.py:75`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_weight_is_edge_weight_times_confidence `def test_weight_is_edge_weight_times_confidence(self)`
- Defined: `tests/test_ranking.py:85`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_weight_default_confidence `def test_weight_default_confidence(self)`
- Defined: `tests/test_ranking.py:90`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_morphism_is_frozen `def test_morphism_is_frozen(self)`
- Defined: `tests/test_ranking.py:94`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_category `def test_empty_category(self)`
- Defined: `tests/test_ranking.py:105`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_add_object_and_morphism `def test_add_object_and_morphism(self)`
- Defined: `tests/test_ranking.py:110`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_outgoing_and_incoming `def test_outgoing_and_incoming(self)`
- Defined: `tests/test_ranking.py:118`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_same_kind `def test_compose_same_kind(self)`
- Defined: `tests/test_ranking.py:130`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_imports_then_defines `def test_compose_imports_then_defines(self)`
- Defined: `tests/test_ranking.py:140`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_incompatible_returns_none `def test_compose_incompatible_returns_none(self)`
- Defined: `tests/test_ranking.py:148`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_mismatched_target_source `def test_compose_mismatched_target_source(self)`
- Defined: `tests/test_ranking.py:155`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_paths_finds_composition_chains `def test_paths_finds_composition_chains(self)`
- Defined: `tests/test_ranking.py:162`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_paths_empty_when_no_route `def test_paths_empty_when_no_route(self)`
- Defined: `tests/test_ranking.py:171`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_graph `def test_empty_graph(self)`
- Defined: `tests/test_ranking.py:184`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_stochastic_row_normalizes_to_one `def test_stochastic_row_normalizes_to_one(self)`
- Defined: `tests/test_ranking.py:190`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_stochastic_row_empty_for_dangling `def test_stochastic_row_empty_for_dangling(self)`
- Defined: `tests/test_ranking.py:199`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_transition_weight_aggregates_parallel_edges `def test_transition_weight_aggregates_parallel_edges(self)`
- Defined: `tests/test_ranking.py:205`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_category_from_edges `def test_build_category_from_edges(self)`
- Defined: `tests/test_ranking.py:214`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_category_from_edges_filters_by_node_ids `def test_build_category_from_edges_filters_by_node_ids(self)`
- Defined: `tests/test_ranking.py:225`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_scores_sum_to_one `def test_scores_sum_to_one(self)`
- Defined: `tests/test_ranking.py:248`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_all_nodes_have_positive_score `def test_all_nodes_have_positive_score(self)`
- Defined: `tests/test_ranking.py:254`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_converges_within_max_iter `def test_converges_within_max_iter(self)`
- Defined: `tests/test_ranking.py:260`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_stable_across_calls `def test_stable_across_calls(self)`
- Defined: `tests/test_ranking.py:266`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_dangling_node_handled `def test_dangling_node_handled(self)`
- Defined: `tests/test_ranking.py:273`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_graph `def test_empty_graph(self)`
- Defined: `tests/test_ranking.py:284`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_seed_node_gets_highest_score `def test_seed_node_gets_highest_score(self)`
- Defined: `tests/test_ranking.py:289`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_scores_sum_to_one `def test_scores_sum_to_one(self)`
- Defined: `tests/test_ranking.py:296`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_different_seeds_produce_different_rankings `def test_different_seeds_produce_different_rankings(self)`
- Defined: `tests/test_ranking.py:303`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_seeds_uses_uniform `def test_empty_seeds_uses_uniform(self)`
- Defined: `tests/test_ranking.py:310`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_multi_seed `def test_multi_seed(self)`
- Defined: `tests/test_ranking.py:317`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_authorities_and_hubs_have_positive_scores `def test_authorities_and_hubs_have_positive_scores(self)`
- Defined: `tests/test_ranking.py:326`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_authorities_l2_normalized `def test_authorities_l2_normalized(self)`
- Defined: `tests/test_ranking.py:333`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_hubs_l2_normalized `def test_hubs_l2_normalized(self)`
- Defined: `tests/test_ranking.py:339`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_from_query_matches_node_id `def test_build_seeds_from_query_matches_node_id(self)`
- Defined: `tests/test_ranking.py:351`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_from_query_matches_symbol `def test_build_seeds_from_query_matches_symbol(self)`
- Defined: `tests/test_ranking.py:363`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_from_query_no_match_returns_empty `def test_build_seeds_from_query_no_match_returns_empty(self)`
- Defined: `tests/test_ranking.py:374`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_for_context `def test_build_seeds_for_context(self)`
- Defined: `tests/test_ranking.py:383`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_for_context_no_match `def test_build_seeds_for_context_no_match(self)`
- Defined: `tests/test_ranking.py:392`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_rank_returns_sorted_results `def test_rank_returns_sorted_results(self)`
- Defined: `tests/test_ranking.py:404`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_rank_items_have_all_score_fields `def test_rank_items_have_all_score_fields(self)`
- Defined: `tests/test_ranking.py:421`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_noise_penalty_applied `def test_noise_penalty_applied(self)`
- Defined: `tests/test_ranking.py:447`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_top_n `def test_top_n(self)`
- Defined: `tests/test_ranking.py:466`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_explain_returns_none_for_missing `def test_explain_returns_none_for_missing(self)`
- Defined: `tests/test_ranking.py:479`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_identity_projection_passes_all `def test_identity_projection_passes_all(self)`
- Defined: `tests/test_ranking.py:491`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_doc_projection_filters_undocumented `def test_doc_projection_filters_undocumented(self)`
- Defined: `tests/test_ranking.py:498`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_doc_projection_filters_morphism_kind `def test_doc_projection_filters_morphism_kind(self)`
- Defined: `tests/test_ranking.py:506`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_apply_view_architecture `def test_apply_view_architecture(self)`
- Defined: `tests/test_ranking.py:512`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_apply_view_reverse `def test_apply_view_reverse(self)`
- Defined: `tests/test_ranking.py:521`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_apply_view_empty `def test_apply_view_empty(self)`
- Defined: `tests/test_ranking.py:528`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_explain_rank_found `def test_explain_rank_found(self)`
- Defined: `tests/test_ranking.py:540`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_explain_rank_not_found `def test_explain_rank_not_found(self)`
- Defined: `tests/test_ranking.py:559`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_rank_summary_format `def test_rank_summary_format(self)`
- Defined: `tests/test_ranking.py:565`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_category_from_real_edges `def test_category_from_real_edges(self)`
- Defined: `tests/test_ranking.py:588`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_pagerank_on_real_category `def test_pagerank_on_real_category(self)`
- Defined: `tests/test_ranking.py:613`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_ppr_favors_seed `def test_ppr_favors_seed(self)`
- Defined: `tests/test_ranking.py:625`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_ranker_from_real_data `def test_ranker_from_real_data(self)`
- Defined: `tests/test_ranking.py:637`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

## tests/test_readme_injector.py

### setUp `def setUp(self)`
- Defined: `tests/test_readme_injector.py:19`
- Depends on: `readmenator/_readme_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:24`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_into_markdown_readme_adds_kb_link `def test_inject_into_markdown_readme_adds_kb_link(self)`
- Defined: `tests/test_readme_injector.py:28`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_into_rst_readme_adds_kb_link `def test_inject_into_rst_readme_adds_kb_link(self)`
- Defined: `tests/test_readme_injector.py:38`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_is_idempotent_does_not_duplicate `def test_inject_is_idempotent_does_not_duplicate(self)`
- Defined: `tests/test_readme_injector.py:47`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_no_readme_file_returns_false `def test_inject_no_readme_file_returns_false(self)`
- Defined: `tests/test_readme_injector.py:58`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_preserves_existing_content `def test_inject_preserves_existing_content(self)`
- Defined: `tests/test_readme_injector.py:62`
- Depends on: `readmenator/_readme_injector.py`

### setUp `def setUp(self)`
- Defined: `tests/test_readme_injector.py:74`
- Depends on: `readmenator/_readme_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:79`
- Depends on: `readmenator/_readme_injector.py`

### test_remove_strips_injected_section `def test_remove_strips_injected_section(self)`
- Defined: `tests/test_readme_injector.py:83`
- Depends on: `readmenator/_readme_injector.py`

### test_remove_without_injection_returns_false `def test_remove_without_injection_returns_false(self)`
- Defined: `tests/test_readme_injector.py:93`
- Depends on: `readmenator/_readme_injector.py`

### test_remove_no_readme_returns_false `def test_remove_no_readme_returns_false(self)`
- Defined: `tests/test_readme_injector.py:99`
- Depends on: `readmenator/_readme_injector.py`

### setUp `def setUp(self)`
- Defined: `tests/test_readme_injector.py:107`
- Depends on: `readmenator/_readme_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:111`
- Depends on: `readmenator/_readme_injector.py`

### test_finds_readme_md `def test_finds_readme_md(self)`
- Defined: `tests/test_readme_injector.py:115`
- Depends on: `readmenator/_readme_injector.py`

### test_finds_readme_rst `def test_finds_readme_rst(self)`
- Defined: `tests/test_readme_injector.py:121`
- Depends on: `readmenator/_readme_injector.py`

### test_prefers_readme_md_over_rst `def test_prefers_readme_md_over_rst(self)`
- Defined: `tests/test_readme_injector.py:127`
- Depends on: `readmenator/_readme_injector.py`

### test_returns_none_when_no_readme `def test_returns_none_when_no_readme(self)`
- Defined: `tests/test_readme_injector.py:134`
- Depends on: `readmenator/_readme_injector.py`

### setUp `def setUp(self)`
- Defined: `tests/test_readme_injector.py:142`
- Depends on: `readmenator/_readme_injector.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:147`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_into_empty_readme `def test_inject_into_empty_readme(self)`
- Defined: `tests/test_readme_injector.py:151`
- Depends on: `readmenator/_readme_injector.py`

### test_custom_kb_filename_works `def test_custom_kb_filename_works(self)`
- Defined: `tests/test_readme_injector.py:159`
- Depends on: `readmenator/_readme_injector.py`

## tests/test_refactorizer.py

### setUp `def setUp(self)`
- Defined: `tests/test_refactorizer.py:21`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### _make_symbol `def _make_symbol(self, name, kind, line)`
- Defined: `tests/test_refactorizer.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### _make_node `def _make_node(self, nid, symbols)`
- Defined: `tests/test_refactorizer.py:28`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### _make_edge `def _make_edge(self, src, tgt)`
- Defined: `tests/test_refactorizer.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_empty_graph_returns_empty `def test_analyze_empty_graph_returns_empty(self)`
- Defined: `tests/test_refactorizer.py:40`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_ignores_small_files `def test_analyze_ignores_small_files(self)`
- Defined: `tests/test_refactorizer.py:44`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_detects_large_file `def test_analyze_detects_large_file(self)`
- Defined: `tests/test_refactorizer.py:50`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_generates_extract_class_for_multiple_classes `def test_analyze_generates_extract_class_for_multiple_classes(self)`
- Defined: `tests/test_refactorizer.py:59`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_generates_extract_function_for_multiple_functions `def test_analyze_generates_extract_function_for_multiple_functions(self)`
- Defined: `tests/test_refactorizer.py:74`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_splits_file_with_many_symbols `def test_analyze_splits_file_with_many_symbols(self)`
- Defined: `tests/test_refactorizer.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_estimates_impact_from_resolved_edges `def test_analyze_estimates_impact_from_resolved_edges(self)`
- Defined: `tests/test_refactorizer.py:97`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_generate_script_contains_shebang `def test_generate_script_contains_shebang(self)`
- Defined: `tests/test_refactorizer.py:109`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_generate_script_contains_set_e `def test_generate_script_contains_set_e(self)`
- Defined: `tests/test_refactorizer.py:129`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_generate_script_contains_sed_commands `def test_generate_script_contains_sed_commands(self)`
- Defined: `tests/test_refactorizer.py:140`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_sorted_by_line_count `def test_analyze_sorted_by_line_count(self)`
- Defined: `tests/test_refactorizer.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_respects_max_files_limit `def test_analyze_respects_max_files_limit(self)`
- Defined: `tests/test_refactorizer.py:173`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

## tests/test_resolver.py

### test_resolves_python_module_dotpath `def test_resolves_python_module_dotpath(self)`
- Defined: `tests/test_resolver.py:18`
- Depends on: `readmenator/_resolver.py`

### test_resolves_relative_import `def test_resolves_relative_import(self)`
- Defined: `tests/test_resolver.py:25`
- Depends on: `readmenator/_resolver.py`

### test_resolves_extensionless_python_import `def test_resolves_extensionless_python_import(self)`
- Defined: `tests/test_resolver.py:32`
- Depends on: `readmenator/_resolver.py`

### test_resolves_package_init `def test_resolves_package_init(self)`
- Defined: `tests/test_resolver.py:39`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_external_stdlib `def test_returns_none_for_external_stdlib(self)`
- Defined: `tests/test_resolver.py:46`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_unknown_import `def test_returns_none_for_unknown_import(self)`
- Defined: `tests/test_resolver.py:53`
- Depends on: `readmenator/_resolver.py`

### test_resolves_stem_match_when_unique `def test_resolves_stem_match_when_unique(self)`
- Defined: `tests/test_resolver.py:60`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_empty_import `def test_returns_none_for_empty_import(self)`
- Defined: `tests/test_resolver.py:67`
- Depends on: `readmenator/_resolver.py`

### test_resolves_go_import `def test_resolves_go_import(self)`
- Defined: `tests/test_resolver.py:72`
- Depends on: `readmenator/_resolver.py`

### test_resolves_same_directory_import `def test_resolves_same_directory_import(self)`
- Defined: `tests/test_resolver.py:79`
- Depends on: `readmenator/_resolver.py`

## tests/test_rule_gen.py

### setUp `def setUp(self)`
- Defined: `tests/test_rule_gen.py:15`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### _make_node `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_rule_gen.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### _make_node_with_symbols `def _make_node_with_symbols(self, nid, sym_count)`
- Defined: `tests/test_rule_gen.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_empty_nodes_returns_empty_rules `def test_empty_nodes_returns_empty_rules(self)`
- Defined: `tests/test_rule_gen.py:44`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_generates_rules_for_function_heavy_language `def test_generates_rules_for_function_heavy_language(self)`
- Defined: `tests/test_rule_gen.py:48`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_detects_antipatterns_with_content `def test_detects_antipatterns_with_content(self)`
- Defined: `tests/test_rule_gen.py:56`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_antipattern_threshold_from_config `def test_antipattern_threshold_from_config(self)`
- Defined: `tests/test_rule_gen.py:67`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_write_rules_creates_files `def test_write_rules_creates_files(self)`
- Defined: `tests/test_rule_gen.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_rule_id_increments `def test_rule_id_increments(self)`
- Defined: `tests/test_rule_gen.py:90`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

## tests/test_sarif.py

### setUp `def setUp(self)`
- Defined: `tests/test_sarif.py:14`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### _make_finding `def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)`
- Defined: `tests/test_sarif.py:18`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_returns_valid_json `def test_export_returns_valid_json(self)`
- Defined: `tests/test_sarif.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_includes_tool_info `def test_export_includes_tool_info(self)`
- Defined: `tests/test_sarif.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_includes_rule `def test_export_includes_rule(self)`
- Defined: `tests/test_sarif.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_includes_result `def test_export_includes_result(self)`
- Defined: `tests/test_sarif.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_severity_maps_correctly `def test_severity_maps_correctly(self)`
- Defined: `tests/test_sarif.py:73`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_privacy_mode_strips_snippets `def test_privacy_mode_strips_snippets(self)`
- Defined: `tests/test_sarif.py:88`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_empty_findings_produces_valid_sarif `def test_empty_findings_produces_valid_sarif(self)`
- Defined: `tests/test_sarif.py:97`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

## tests/test_scanner.py

### setUp `def setUp(self)`
- Defined: `tests/test_scanner.py:12`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### tearDown `def tearDown(self)`
- Defined: `tests/test_scanner.py:16`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### _write `def _write(self, path, content)`
- Defined: `tests/test_scanner.py:20`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_scans_python_files `def test_scans_python_files(self)`
- Defined: `tests/test_scanner.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_ignores_env_and_vendor_dirs `def test_ignores_env_and_vendor_dirs(self)`
- Defined: `tests/test_scanner.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_rejects_symlinks `def test_rejects_symlinks(self)`
- Defined: `tests/test_scanner.py:45`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_skips_non_code_files `def test_skips_non_code_files(self)`
- Defined: `tests/test_scanner.py:59`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_scans_multiple_languages `def test_scans_multiple_languages(self)`
- Defined: `tests/test_scanner.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_respects_max_directory_depth `def test_respects_max_directory_depth(self)`
- Defined: `tests/test_scanner.py:79`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_raises_on_invalid_directory `def test_raises_on_invalid_directory(self)`
- Defined: `tests/test_scanner.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_import_edges_are_created `def test_import_edges_are_created(self)`
- Defined: `tests/test_scanner.py:94`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_privacy_mode_strips_docs `def test_privacy_mode_strips_docs(self)`
- Defined: `tests/test_scanner.py:104`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_scan_with_content_returns_content_map `def test_scan_with_content_returns_content_map(self)`
- Defined: `tests/test_scanner.py:114`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_gitignore_respected_when_enabled `def test_gitignore_respected_when_enabled(self)`
- Defined: `tests/test_scanner.py:122`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_gitignore_disabled_by_default `def test_gitignore_disabled_by_default(self)`
- Defined: `tests/test_scanner.py:133`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_gitignore_glob_conversion `def test_gitignore_glob_conversion(self)`
- Defined: `tests/test_scanner.py:142`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

## tests/test_security.py

### test_security_finding_fields `def test_security_finding_fields(self)`
- Defined: `tests/test_security.py:24`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_default_config_disables_security `def test_default_config_disables_security(self)`
- Defined: `tests/test_security.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_default_severity_threshold `def test_default_severity_threshold(self)`
- Defined: `tests/test_security.py:50`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_default_security_output `def test_default_security_output(self)`
- Defined: `tests/test_security.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_init_with_config `def test_init_with_config(self)`
- Defined: `tests/test_security.py:58`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### setUp `def setUp(self)`
- Defined: `tests/test_security.py:67`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### _scan_content `def _scan_content(self, content, extension)`
- Defined: `tests/test_security.py:71`
- Doc: Write content to a temp file and scan it.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_os_system `def test_python_os_system(self)`
- Defined: `tests/test_security.py:78`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_eval `def test_python_eval(self)`
- Defined: `tests/test_security.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_pickle `def test_python_pickle(self)`
- Defined: `tests/test_security.py:88`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_sql_injection `def test_python_sql_injection(self)`
- Defined: `tests/test_security.py:93`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_hardcoded_secret `def test_python_hardcoded_secret(self)`
- Defined: `tests/test_security.py:98`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_weak_crypto `def test_python_weak_crypto(self)`
- Defined: `tests/test_security.py:103`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_request_verify_false `def test_python_request_verify_false(self)`
- Defined: `tests/test_security.py:108`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_flask_debug `def test_python_flask_debug(self)`
- Defined: `tests/test_security.py:113`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_yaml_load `def test_python_yaml_load(self)`
- Defined: `tests/test_security.py:118`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_inner_html `def test_javascript_inner_html(self)`
- Defined: `tests/test_security.py:123`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_eval `def test_javascript_eval(self)`
- Defined: `tests/test_security.py:128`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_child_process `def test_javascript_child_process(self)`
- Defined: `tests/test_security.py:133`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_dangerously_set_inner_html `def test_javascript_dangerously_set_inner_html(self)`
- Defined: `tests/test_security.py:138`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_c_strcpy `def test_c_strcpy(self)`
- Defined: `tests/test_security.py:143`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_c_gets `def test_c_gets(self)`
- Defined: `tests/test_security.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_c_system `def test_c_system(self)`
- Defined: `tests/test_security.py:153`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_java_runtime_exec `def test_java_runtime_exec(self)`
- Defined: `tests/test_security.py:158`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_java_sql_injection `def test_java_sql_injection(self)`
- Defined: `tests/test_security.py:163`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_go_exec_command `def test_go_exec_command(self)`
- Defined: `tests/test_security.py:168`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ruby_eval `def test_ruby_eval(self)`
- Defined: `tests/test_security.py:173`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ruby_marshal_load `def test_ruby_marshal_load(self)`
- Defined: `tests/test_security.py:178`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_eval `def test_php_eval(self)`
- Defined: `tests/test_security.py:183`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_sql_injection `def test_php_sql_injection(self)`
- Defined: `tests/test_security.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_unseralize `def test_php_unseralize(self)`
- Defined: `tests/test_security.py:193`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_shell_eval `def test_shell_eval(self)`
- Defined: `tests/test_security.py:198`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_csharp_process_start `def test_csharp_process_start(self)`
- Defined: `tests/test_security.py:203`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_kotlin_runtime_exec `def test_kotlin_runtime_exec(self)`
- Defined: `tests/test_security.py:208`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_swift_process `def test_swift_process(self)`
- Defined: `tests/test_security.py:213`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_lua_load `def test_lua_load(self)`
- Defined: `tests/test_security.py:218`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_lua_os_execute `def test_lua_os_execute(self)`
- Defined: `tests/test_security.py:223`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_dart_process_run `def test_dart_process_run(self)`
- Defined: `tests/test_security.py:228`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_rust_unsafe `def test_rust_unsafe(self)`
- Defined: `tests/test_security.py:233`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_elixir_code_eval `def test_elixir_code_eval(self)`
- Defined: `tests/test_security.py:238`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_elixir_system_cmd `def test_elixir_system_cmd(self)`
- Defined: `tests/test_security.py:243`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_gdscript_os_execute `def test_gdscript_os_execute(self)`
- Defined: `tests/test_security.py:248`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_scala_runtime_exec `def test_scala_runtime_exec(self)`
- Defined: `tests/test_security.py:253`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_nim_exec_process `def test_nim_exec_process(self)`
- Defined: `tests/test_security.py:258`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_safe_code_produces_no_findings `def test_safe_code_produces_no_findings(self)`
- Defined: `tests/test_security.py:263`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_csharp_binary_formatter `def test_csharp_binary_formatter(self)`
- Defined: `tests/test_security.py:274`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ruby_backtick `def test_ruby_backtick(self)`
- Defined: `tests/test_security.py:279`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_xss `def test_php_xss(self)`
- Defined: `tests/test_security.py:284`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_go_unsafe_package `def test_go_unsafe_package(self)`
- Defined: `tests/test_security.py:289`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_threshold_filters_low `def test_threshold_filters_low(self)`
- Defined: `tests/test_security.py:298`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_threshold_info_shows_all `def test_threshold_info_shows_all(self)`
- Defined: `tests/test_security.py:312`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ignores_symlinks `def test_ignores_symlinks(self)`
- Defined: `tests/test_security.py:330`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ignores_ignored_dirs `def test_ignores_ignored_dirs(self)`
- Defined: `tests/test_security.py:345`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_empty_directory `def test_empty_directory(self)`
- Defined: `tests/test_security.py:357`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_unsupported_extension `def test_unsupported_extension(self)`
- Defined: `tests/test_security.py:364`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_summary_empty `def test_summary_empty(self)`
- Defined: `tests/test_security.py:377`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_summary_with_findings `def test_summary_with_findings(self)`
- Defined: `tests/test_security.py:383`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

## tests/test_taint.py

### setUp `def setUp(self)`
- Defined: `tests/test_taint.py:13`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### _make_node `def _make_node(self, nid, label)`
- Defined: `tests/test_taint.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_empty_graph_returns_empty_result `def test_empty_graph_returns_empty_result(self)`
- Defined: `tests/test_taint.py:20`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_no_dangerous_imports_returns_empty `def test_no_dangerous_imports_returns_empty(self)`
- Defined: `tests/test_taint.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_direct_dangerous_import_found `def test_direct_dangerous_import_found(self)`
- Defined: `tests/test_taint.py:31`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_taint_propagates_through_resolved_edges `def test_taint_propagates_through_resolved_edges(self)`
- Defined: `tests/test_taint.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_dangerous_import_by_language `def test_dangerous_import_by_language(self)`
- Defined: `tests/test_taint.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_taint_path_has_severity `def test_taint_path_has_severity(self)`
- Defined: `tests/test_taint.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_max_depth_limits_propagation `def test_max_depth_limits_propagation(self)`
- Defined: `tests/test_taint.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

## tests/test_taint_bdd.py

### _build_project_files `def _build_project_files(project, root)`
- Defined: `tests/test_taint_bdd.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _scan_project `def _scan_project(root, cfg)`
- Defined: `tests/test_taint_bdd.py:36`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _run_taint `def _run_taint(files, cfg)`
- Defined: `tests/test_taint_bdd.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_direct_dangerous_import `def test_direct_dangerous_import()`
- Defined: `tests/test_taint_bdd.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_taint_propagates_chain `def test_taint_propagates_chain()`
- Defined: `tests/test_taint_bdd.py:75`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_taint_max_depth `def test_taint_max_depth()`
- Defined: `tests/test_taint_bdd.py:79`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_cross_language_taint `def test_cross_language_taint()`
- Defined: `tests/test_taint_bdd.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_bdd_skipped `def test_bdd_skipped()`
- Defined: `tests/test_taint_bdd.py:87`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _bkg `def _bkg()`
- Defined: `tests/test_taint_bdd.py:112`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _direct_given `def _direct_given()`
- Defined: `tests/test_taint_bdd.py:117`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _direct_when `def _direct_when(_taint_result)`
- Defined: `tests/test_taint_bdd.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_has_path `def _check_has_path(_taint_result)`
- Defined: `tests/test_taint_bdd.py:125`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_direct_path `def _check_direct_path(_taint_result)`
- Defined: `tests/test_taint_bdd.py:130`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_src `def _check_src(_taint_result)`
- Defined: `tests/test_taint_bdd.py:135`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_sink `def _check_sink(_taint_result)`
- Defined: `tests/test_taint_bdd.py:139`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _chain_given `def _chain_given()`
- Defined: `tests/test_taint_bdd.py:144`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _chain_when `def _chain_when(_taint_result)`
- Defined: `tests/test_taint_bdd.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_long_path `def _check_long_path(_taint_result)`
- Defined: `tests/test_taint_bdd.py:152`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _shallow_cfg `def _shallow_cfg()`
- Defined: `tests/test_taint_bdd.py:159`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _chain_given2 `def _chain_given2()`
- Defined: `tests/test_taint_bdd.py:163`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _run_shallow `def _run_shallow(_shallow_cfg)`
- Defined: `tests/test_taint_bdd.py:167`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_shallow `def _check_shallow(_taint_result)`
- Defined: `tests/test_taint_bdd.py:171`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _js_given `def _js_given()`
- Defined: `tests/test_taint_bdd.py:178`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _js_when `def _js_when(_taint_result)`
- Defined: `tests/test_taint_bdd.py:182`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_js_dangerous `def _check_js_dangerous(_taint_result)`
- Defined: `tests/test_taint_bdd.py:186`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_js_source `def _check_js_source(_taint_result)`
- Defined: `tests/test_taint_bdd.py:192`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

## tests/test_uml.py

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_empty_nodes_returns_empty_string `def test_render_empty_nodes_returns_empty_string(self)`
- Defined: `tests/test_uml.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_no_class_symbols_returns_empty_string `def test_render_no_class_symbols_returns_empty_string(self)`
- Defined: `tests/test_uml.py:27`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_single_class_produces_mermaid_class_diagram `def test_render_single_class_produces_mermaid_class_diagram(self)`
- Defined: `tests/test_uml.py:42`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_multiple_classes_from_different_files `def test_render_multiple_classes_from_different_files(self)`
- Defined: `tests/test_uml.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_with_import_edges_produces_relationships `def test_render_with_import_edges_produces_relationships(self)`
- Defined: `tests/test_uml.py:90`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_respects_max_classes_limit `def test_render_respects_max_classes_limit(self)`
- Defined: `tests/test_uml.py:119`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_with_structs_interfaces_traits `def test_render_with_structs_interfaces_traits(self)`
- Defined: `tests/test_uml.py:137`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_preserves_alphanumeric `def test_sanitize_preserves_alphanumeric(self)`
- Defined: `tests/test_uml.py:164`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_replaces_special_chars `def test_sanitize_replaces_special_chars(self)`
- Defined: `tests/test_uml.py:168`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_prefixes_digit_start `def test_sanitize_prefixes_digit_start(self)`
- Defined: `tests/test_uml.py:172`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_handles_empty_string `def test_sanitize_handles_empty_string(self)`
- Defined: `tests/test_uml.py:176`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:184`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_cpp_produces_valid_code `def test_generate_cpp_produces_valid_code(self)`
- Defined: `tests/test_uml.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_cpp_with_empty_classes `def test_generate_cpp_with_empty_classes(self)`
- Defined: `tests/test_uml.py:208`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_cpp_unknown_language_returns_error_message `def test_generate_cpp_unknown_language_returns_error_message(self)`
- Defined: `tests/test_uml.py:223`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:242`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_java_class_produces_valid_code `def test_generate_java_class_produces_valid_code(self)`
- Defined: `tests/test_uml.py:246`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_java_interface_produces_interface `def test_generate_java_interface_produces_interface(self)`
- Defined: `tests/test_uml.py:265`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:284`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_csharp_produces_valid_code `def test_generate_csharp_produces_valid_code(self)`
- Defined: `tests/test_uml.py:288`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:309`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_go_struct_produces_valid_code `def test_generate_go_struct_produces_valid_code(self)`
- Defined: `tests/test_uml.py:313`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_go_interface_produces_valid_code `def test_generate_go_interface_produces_valid_code(self)`
- Defined: `tests/test_uml.py:330`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:350`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_rust_struct_produces_valid_code `def test_generate_rust_struct_produces_valid_code(self)`
- Defined: `tests/test_uml.py:354`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_rust_trait_produces_valid_code `def test_generate_rust_trait_produces_valid_code(self)`
- Defined: `tests/test_uml.py:370`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:390`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_php_class_produces_valid_code `def test_generate_php_class_produces_valid_code(self)`
- Defined: `tests/test_uml.py:394`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_php_interface_produces_valid_code `def test_generate_php_interface_produces_valid_code(self)`
- Defined: `tests/test_uml.py:411`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp `def setUp(self)`
- Defined: `tests/test_uml.py:430`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### _make_class_node `def _make_class_node(self, name, lang, kind)`
- Defined: `tests/test_uml.py:434`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_kotlin_produces_valid_code `def test_generate_kotlin_produces_valid_code(self)`
- Defined: `tests/test_uml.py:446`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_scala_produces_valid_code `def test_generate_scala_produces_valid_code(self)`
- Defined: `tests/test_uml.py:452`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_scala_trait_produces_valid_code `def test_generate_scala_trait_produces_valid_code(self)`
- Defined: `tests/test_uml.py:458`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_swift_produces_valid_code `def test_generate_swift_produces_valid_code(self)`
- Defined: `tests/test_uml.py:463`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_swift_protocol_produces_valid_code `def test_generate_swift_protocol_produces_valid_code(self)`
- Defined: `tests/test_uml.py:469`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_dart_produces_valid_code `def test_generate_dart_produces_valid_code(self)`
- Defined: `tests/test_uml.py:474`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_ruby_produces_valid_code `def test_generate_ruby_produces_valid_code(self)`
- Defined: `tests/test_uml.py:480`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`
