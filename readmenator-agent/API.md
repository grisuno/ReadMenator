# API

## readmenator/__main__.py

### build_parser (function) `def build_parser()`
- Defined: `readmenator/__main__.py:16`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

### _run_tests (function) `def _run_tests()`
- Defined: `readmenator/__main__.py:107`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

### main (function) `def main()`
- Defined: `readmenator/__main__.py:122`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

## readmenator/_agent_injector.py

### ensure_readmenator_installed (function) `def ensure_readmenator_installed()`
- Defined: `readmenator/_agent_injector.py:111`
- Doc: Check if readmenator is installed via pip; install it if missing.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### __init__ (method) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)`
- Defined: `readmenator/_agent_injector.py:147`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### inject (method) `def inject(self, project_root)`
- Defined: `readmenator/_agent_injector.py:161`
- Doc: Inject KB reference into all discovered agent files.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### remove (method) `def remove(self, project_root)`
- Defined: `readmenator/_agent_injector.py:179`
- Doc: Remove KB injection from all discovered agent files.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### find_agent_files (method) `def find_agent_files(self, project_root)`
- Defined: `readmenator/_agent_injector.py:192`
- Doc: Public accessor: return all detected agent files.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _find_agent_files (method) `def _find_agent_files(self, root)`
- Defined: `readmenator/_agent_injector.py:196`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _inject_single (method) `def _inject_single(self, path)`
- Defined: `readmenator/_agent_injector.py:210`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _extract_current_injection (method) `def _extract_current_injection(content)`
- Defined: `readmenator/_agent_injector.py:248`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _remove_old_injection (method) `def _remove_old_injection(content)`
- Defined: `readmenator/_agent_injector.py:257`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _remove_single (method) `def _remove_single(self, path)`
- Defined: `readmenator/_agent_injector.py:267`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _build_injection (method) `def _build_injection(self, fmt)`
- Defined: `readmenator/_agent_injector.py:283`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _build_mdc_injection (method) `def _build_mdc_injection(self)`
- Defined: `readmenator/_agent_injector.py:295`
- Doc: Build Cursor .mdc injection body (frontmatter added separately).
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

### _prepend_mdc_frontmatter (method) `def _prepend_mdc_frontmatter(content, injection)`
- Defined: `readmenator/_agent_injector.py:300`
- Doc: Prepend Cursor frontmatter so the rule is auto-attached.
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

## readmenator/_agent_output.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_agent_output.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### generate (method) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)`
- Defined: `readmenator/_agent_output.py:61`
- Doc: Write all agent output files and return the output directory path.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _infer_subsystems (method) `def _infer_subsystems(self, nodes)`
- Defined: `readmenator/_agent_output.py:116`
- Doc: Group nodes by directory, inferring subsystem names.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_index (method) `def _build_index(self, nodes, subsystems)`
- Defined: `readmenator/_agent_output.py:153`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_architecture (method) `def _build_architecture(self, edges, resolved_edges, nodes)`
- Defined: `readmenator/_agent_output.py:183`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_security (method) `def _build_security(self, findings, nodes)`
- Defined: `readmenator/_agent_output.py:227`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _enclosing_symbol (method) `def _enclosing_symbol(nodes, file_path, line)`
- Defined: `readmenator/_agent_output.py:257`
- Doc: Return the nearest symbol defined at or before line in file_path.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_api (method) `def _build_api(self, nodes, resolved_map, imported_by)`
- Defined: `readmenator/_agent_output.py:276`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_manifest (method) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root)`
- Defined: `readmenator/_agent_output.py:331`
- Doc: Build MANIFEST.json with freshness + entry points for agents.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_symbols (method) `def _build_symbols(self, nodes)`
- Defined: `readmenator/_agent_output.py:370`
- Doc: Build grep-friendly symbol index (one line per symbol).
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_gotchas (method) `def _build_gotchas(self, analysis, analysis_v2, nodes)`
- Defined: `readmenator/_agent_output.py:387`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _write_subsystem_files (method) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)`
- Defined: `readmenator/_agent_output.py:469`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_subsystem_content (method) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)`
- Defined: `readmenator/_agent_output.py:488`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _write_recipes (method) `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings)`
- Defined: `readmenator/_agent_output.py:538`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_resolved_map (method) `def _build_resolved_map(resolved_edges)`
- Defined: `readmenator/_agent_output.py:637`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _build_imported_by_map (method) `def _build_imported_by_map(resolved_edges)`
- Defined: `readmenator/_agent_output.py:646`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

### _write (method) `def _write(path, content)`
- Defined: `readmenator/_agent_output.py:655`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

## readmenator/_analyzer.py

### dominant_directory (function) `def dominant_directory(file_ids)`
- Defined: `readmenator/_analyzer.py:21`
- Doc: Return the most informative directory label for a set of files.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_analyzer.py:47`
- Doc: Initialise with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### analyze (method) `def analyze(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_analyzer.py:55`
- Doc: Run the full analysis pipeline and return structured results.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _build_adjacency (method) `def _build_adjacency(self, nodes, edges)`
- Defined: `readmenator/_analyzer.py:108`
- Doc: Build an undirected adjacency map from import edges.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _build_reverse_adjacency (method) `def _build_reverse_adjacency(self, adjacency)`
- Defined: `readmenator/_analyzer.py:122`
- Doc: Build a directed reverse adjacency (incoming edges) map.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _compute_god_nodes (method) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)`
- Defined: `readmenator/_analyzer.py:132`
- Doc: Compute the most central nodes using combined degree centrality.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _detect_communities (method) `def _detect_communities(self, nodes, adjacency)`
- Defined: `readmenator/_analyzer.py:154`
- Doc: Detect communities using label propagation.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _label_communities (method) `def _label_communities(self, nodes, communities)`
- Defined: `readmenator/_analyzer.py:209`
- Doc: Generate human-readable labels for communities.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _build_community_map (method) `def _build_community_map(self, communities)`
- Defined: `readmenator/_analyzer.py:226`
- Doc: Build a reverse map from file ID to community ID.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _compute_cohesion (method) `def _compute_cohesion(self, communities, adjacency)`
- Defined: `readmenator/_analyzer.py:236`
- Doc: Compute cohesion score for each community.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _find_surprising_connections (method) `def _find_surprising_connections(self, nodes, adjacency, community_map)`
- Defined: `readmenator/_analyzer.py:261`
- Doc: Find non-obvious cross-community bridges.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _shortest_path_communities (method) `def _shortest_path_communities(self, source, target, adjacency, community_map)`
- Defined: `readmenator/_analyzer.py:301`
- Doc: Find the shortest path and communities traversed.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

### _suggest_questions (method) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)`
- Defined: `readmenator/_analyzer.py:328`
- Doc: Generate plain-language exploration questions from graph structure.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_analyzer.py`, `tests/test_analyzer.py`

## readmenator/_app.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_app.py:36`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _scan (method) `def _scan(self, target_dir)`
- Defined: `readmenator/_app.py:45`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _scan_with_content (method) `def _scan_with_content(self, target_dir)`
- Defined: `readmenator/_app.py:53`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _resolve_imports (method) `def _resolve_imports(self, nodes, edges, target_dir)`
- Defined: `readmenator/_app.py:63`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### run (method) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- Defined: `readmenator/_app.py:82`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _write_sidecar_outputs (method) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- Defined: `readmenator/_app.py:199`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _inject_readme_link (method) `def _inject_readme_link(self, root)`
- Defined: `readmenator/_app.py:225`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _inject_agent_files (method) `def _inject_agent_files(self, root)`
- Defined: `readmenator/_app.py:233`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### generate_uml_code (method) `def generate_uml_code(self, target_dir, language, output_path)`
- Defined: `readmenator/_app.py:241`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _log_summary (method) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)`
- Defined: `readmenator/_app.py:253`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### update (method) `def update(self, target_dir, run_security)`
- Defined: `readmenator/_app.py:308`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _scan_for_cache (method) `def _scan_for_cache(self, root, cache)`
- Defined: `readmenator/_app.py:413`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### query (method) `def query(self, target_dir, question)`
- Defined: `readmenator/_app.py:431`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### explain (method) `def explain(self, target_dir, symbol_name)`
- Defined: `readmenator/_app.py:436`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### find_path (method) `def find_path(self, target_dir, symbol_a, symbol_b)`
- Defined: `readmenator/_app.py:448`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### summary (method) `def summary(self, target_dir)`
- Defined: `readmenator/_app.py:461`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### rank_query (method) `def rank_query(self, target_dir, query, top_n)`
- Defined: `readmenator/_app.py:466`
- Doc: Run a ranked query against the knowledge graph.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### rebuild (method) `def rebuild(self, target_dir, run_security)`
- Defined: `readmenator/_app.py:496`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### analyze (method) `def analyze(self, target_dir)`
- Defined: `readmenator/_app.py:499`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_json (method) `def export_json(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:503`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_html (method) `def export_html(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:514`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_svg (method) `def export_svg(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:525`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export (method) `def export(self, target_dir)`
- Defined: `readmenator/_app.py:536`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_graphml (method) `def export_graphml(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:541`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_cypher (method) `def export_cypher(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:552`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_obsidian (method) `def export_obsidian(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:565`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_wiki (method) `def export_wiki(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:575`
- Doc: Generate the navigable agent wiki for the target project.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### lint_wiki (method) `def lint_wiki(self, target_dir)`
- Defined: `readmenator/_app.py:598`
- Doc: Check wiki health and log reported issues.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_diagrams (method) `def export_diagrams(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:616`
- Doc: Export all five interactive system maps plus a gallery index.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### _live_renderer (method) `def _live_renderer(self)`
- Defined: `readmenator/_app.py:655`
- Doc: Return the configured map renderer for published output.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_diagram (method) `def export_diagram(self, target_dir, kind, output_path)`
- Defined: `readmenator/_app.py:665`
- Doc: Export a single interactive system map as standalone HTML.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_pages (method) `def export_pages(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:702`
- Doc: Publish all system maps plus a gallery index as a static site.
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### watch (method) `def watch(self, target_dir)`
- Defined: `readmenator/_app.py:738`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### audit (method) `def audit(self, target_dir)`
- Defined: `readmenator/_app.py:748`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### audit_deep (method) `def audit_deep(self, target_dir)`
- Defined: `readmenator/_app.py:755`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_sarif (method) `def export_sarif(self, target_dir, output_path)`
- Defined: `readmenator/_app.py:775`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### export_rules (method) `def export_rules(self, target_dir, output_dir)`
- Defined: `readmenator/_app.py:785`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### detect_layers (method) `def detect_layers(self, target_dir)`
- Defined: `readmenator/_app.py:795`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### lint (method) `def lint(self, target_dir)`
- Defined: `readmenator/_app.py:805`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### strip_dead_code (method) `def strip_dead_code(self, target_dir)`
- Defined: `readmenator/_app.py:818`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### generate_cursorrules (method) `def generate_cursorrules(self, target_dir)`
- Defined: `readmenator/_app.py:828`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### refactor_monolith (method) `def refactor_monolith(self, target_dir)`
- Defined: `readmenator/_app.py:843`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

### on_change (method) `def on_change()`
- Defined: `readmenator/_app.py:742`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

## readmenator/_cache.py

### __init__ (method) `def __init__(self, config, project_root)`
- Defined: `readmenator/_cache.py:31`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### load (method) `def load(self)`
- Defined: `readmenator/_cache.py:38`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### save (method) `def save(self, hashes)`
- Defined: `readmenator/_cache.py:49`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### compute_hash (method) `def compute_hash(self, file_path)`
- Defined: `readmenator/_cache.py:55`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### compute_hashes (method) `def compute_hashes(self, file_paths)`
- Defined: `readmenator/_cache.py:64`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### find_changed (method) `def find_changed(self, file_paths)`
- Defined: `readmenator/_cache.py:72`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### prune_deleted (method) `def prune_deleted(self, current_file_ids)`
- Defined: `readmenator/_cache.py:84`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### save_analysis (method) `def save_analysis(self, key, data)`
- Defined: `readmenator/_cache.py:95`
- Doc: Save an analysis result to the semantic cache.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### load_analysis (method) `def load_analysis(self, key)`
- Defined: `readmenator/_cache.py:118`
- Doc: Load a previously cached analysis result.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### clear_analysis (method) `def clear_analysis(self, key)`
- Defined: `readmenator/_cache.py:135`
- Doc: Clear analysis cache, optionally for a specific key only.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### _prune_analysis_cache (method) `def _prune_analysis_cache(self, current_file_ids)`
- Defined: `readmenator/_cache.py:155`
- Doc: Remove analysis entries for files that no longer exist.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

### has_changed_since_last_analysis (method) `def has_changed_since_last_analysis(self, file_paths)`
- Defined: `readmenator/_cache.py:166`
- Doc: Check if any file has changed since the last analysis cache.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

## readmenator/_category.py

### build_category_from_edges (method) `def build_category_from_edges(edges, resolved_edges, node_ids)`
- Defined: `readmenator/_category.py:236`
- Doc: Build a Category from lists of Edge objects.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### _infer_edge_kind (method) `def _infer_edge_kind(relation)`
- Defined: `readmenator/_category.py:280`
- Doc: Map a relation string to an EdgeKind.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### __str__ (method) `def __str__(self)`
- Defined: `readmenator/_category.py:38`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### weight (method) `def weight(self)`
- Defined: `readmenator/_category.py:73`
- Doc: Effective weight for ranking = semantic weight * confidence.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### __init__ (method) `def __init__(self)`
- Defined: `readmenator/_category.py:86`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### add_object (method) `def add_object(self, obj_id)`
- Defined: `readmenator/_category.py:92`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### add_morphism (method) `def add_morphism(self, m)`
- Defined: `readmenator/_category.py:95`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### objects (method) `def objects(self)`
- Defined: `readmenator/_category.py:103`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### morphisms (method) `def morphisms(self)`
- Defined: `readmenator/_category.py:107`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### outgoing (method) `def outgoing(self, obj_id)`
- Defined: `readmenator/_category.py:110`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### incoming (method) `def incoming(self, obj_id)`
- Defined: `readmenator/_category.py:113`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### compose (method) `def compose(self, a, b)`
- Defined: `readmenator/_category.py:116`
- Doc: Compose two morphisms if target of a matches source of b.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### paths (method) `def paths(self, source, target, max_depth)`
- Defined: `readmenator/_category.py:133`
- Doc: Find all composition paths from source to target up to max_depth.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### _compose_kind (method) `def _compose_kind(a, b)`
- Defined: `readmenator/_category.py:157`
- Doc: Determine the composite edge kind.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### __init__ (method) `def __init__(self, category)`
- Defined: `readmenator/_category.py:188`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### _compute_out_weights (method) `def _compute_out_weights(self)`
- Defined: `readmenator/_category.py:197`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### nodes (method) `def nodes(self)`
- Defined: `readmenator/_category.py:203`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### size (method) `def size(self)`
- Defined: `readmenator/_category.py:207`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### node_index (method) `def node_index(self, node_id)`
- Defined: `readmenator/_category.py:210`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### transition_weight (method) `def transition_weight(self, source, target)`
- Defined: `readmenator/_category.py:213`
- Doc: Sum of weights of all morphisms from source to target.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### stochastic_row (method) `def stochastic_row(self, source)`
- Defined: `readmenator/_category.py:221`
- Doc: Return dict of target -> probability for the row of *source*.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

### dfs (method) `def dfs(current, goal, path, depth)`
- Defined: `readmenator/_category.py:139`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

## readmenator/_cpg.py

### __init__ (method) `def __init__(self, privacy_mode, cpg_context)`
- Defined: `readmenator/_cpg.py:20`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### generate (method) `def generate(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_cpg.py:24`
- Doc: Generate the CPG JSON-LD string embeddable in markdown.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### _severity_counts (method) `def _severity_counts(self, findings)`
- Defined: `readmenator/_cpg.py:141`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### _build_symbol_list (method) `def _build_symbol_list(self, node)`
- Defined: `readmenator/_cpg.py:147`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

### _compute_node_hash (method) `def _compute_node_hash(node)`
- Defined: `readmenator/_cpg.py:163`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

## readmenator/_cursorrules_generator.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_cursorrules_generator.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### generate (method) `def generate(self, nodes, edges, analysis, layers, violations, project_root)`
- Defined: `readmenator/_cursorrules_generator.py:28`
- Doc: Generate the .cursorrules content string.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _build_base_rules (method) `def _build_base_rules(self)`
- Defined: `readmenator/_cursorrules_generator.py:63`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _extract_layer_constraints (method) `def _extract_layer_constraints(self, layers)`
- Defined: `readmenator/_cursorrules_generator.py:81`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _extract_analysis_constraints (method) `def _extract_analysis_constraints(self, analysis)`
- Defined: `readmenator/_cursorrules_generator.py:92`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _extract_violation_rules (method) `def _extract_violation_rules(self, violations)`
- Defined: `readmenator/_cursorrules_generator.py:107`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

### _write_file (method) `def _write_file(self, project_root, content)`
- Defined: `readmenator/_cursorrules_generator.py:115`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

## readmenator/_dataflow.py

### _strip_noise (function) `def _strip_noise(line)`
- Defined: `readmenator/_dataflow.py:96`
- Doc: Remove comments and string contents that confuse identifier scans.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _strip_block_comments (function) `def _strip_block_comments(content)`
- Defined: `readmenator/_dataflow.py:107`
- Doc: Blank block comments while preserving newlines and line numbers.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _strip_sizeof (function) `def _strip_sizeof(line)`
- Defined: `readmenator/_dataflow.py:116`
- Doc: Blank sizeof operands, which never evaluate their argument at runtime.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _blank (method) `def _blank(match)`
- Defined: `readmenator/_dataflow.py:110`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_dataflow.py:125`
- Doc: Store configuration for enable flag and issue caps.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### analyze (method) `def analyze(self, nodes, content_map)`
- Defined: `readmenator/_dataflow.py:129`
- Doc: Check every function body span and return capped issues.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _brace_depths (method) `def _brace_depths(lines)`
- Defined: `readmenator/_dataflow.py:153`
- Doc: Return the brace depth before each line of noise-stripped code.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _function_spans (method) `def _function_spans(self, node, total_lines, depths)`
- Defined: `readmenator/_dataflow.py:164`
- Doc: Return (name, start_idx, end_idx) spans for function symbols.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _analyze_function (method) `def _analyze_function(self, file_id, func, lines, start, end)`
- Defined: `readmenator/_dataflow.py:191`
- Doc: Run def-use checks over one function body span.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _scan_reads (method) `def _scan_reads(text, lineno, reads, assigned, declared_names)`
- Defined: `readmenator/_dataflow.py:403`
- Doc: Record identifier reads and address-takes inside an expression.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _scan_inline_aliases (method) `def _scan_inline_aliases(line, lineno, arrays, derived_alias, deriv_reads)`
- Defined: `readmenator/_dataflow.py:427`
- Doc: Discover pointer-from-array aliases in mid-line statements.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _scan_out_params (method) `def _scan_out_params(line, lineno, assigned)`
- Defined: `readmenator/_dataflow.py:450`
- Doc: Treat known filler/scan call arguments as assignments.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _scan_array_args (method) `def _scan_array_args(line, lineno, arrays, assigned)`
- Defined: `readmenator/_dataflow.py:461`
- Doc: Treat arrays passed to non-readonly calls as assignments.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _params_of (method) `def _params_of(signature_line)`
- Defined: `readmenator/_dataflow.py:474`
- Doc: Extract parameter names from a function signature line.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _track_call_continuation (method) `def _track_call_continuation(line, call_open, paren_balance)`
- Defined: `readmenator/_dataflow.py:494`
- Doc: Track whether the next line continues an unclosed call.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _mentions_param (method) `def _mentions_param(text, params)`
- Defined: `readmenator/_dataflow.py:513`
- Doc: Return True when an expression mentions a function parameter.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _is_member (method) `def _is_member(line, pos)`
- Defined: `readmenator/_dataflow.py:521`
- Doc: Return True when the identifier at pos is a struct member access.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _member_base (method) `def _member_base(line, pos)`
- Defined: `readmenator/_dataflow.py:527`
- Doc: Return the base identifier of a member access chain.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _is_prototype (method) `def _is_prototype(line)`
- Defined: `readmenator/_dataflow.py:535`
- Doc: Return True for declaration lines that are actually prototypes.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

### _null_checked (method) `def _null_checked(body_text, name)`
- Defined: `readmenator/_dataflow.py:540`
- Doc: Return True when body contains a NULL/boolean check for name.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`

## readmenator/_dead_code.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_dead_code.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

### identify (method) `def identify(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_dead_code.py:28`
- Doc: Identify dead code symbols with zero in-degree.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

### _build_in_degree_map (method) `def _build_in_degree_map(self, nodes, resolved_edges)`
- Defined: `readmenator/_dead_code.py:64`
- Doc: Build in-degree count for each symbol name.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

### _classify_recommendation (method) `def _classify_recommendation(self, symbol)`
- Defined: `readmenator/_dead_code.py:88`
- Doc: Classify the recommended action for a dead symbol.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

## readmenator/_diagrams.py

### _escape_markup (function) `def _escape_markup(value)`
- Defined: `readmenator/_diagrams.py:24`
- Doc: Escape text for HTML and tooltip embedding.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _json_payload (function) `def _json_payload(payload)`
- Defined: `readmenator/_diagrams.py:36`
- Doc: Serialize a payload for safe inline script embedding.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _role_color (function) `def _role_color(role, config)`
- Defined: `readmenator/_diagrams.py:48`
- Doc: Return the stroke color for a semantic role.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_diagrams.py:205`
- Doc: Initialise the validator with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### validate (method) `def validate(self, system_map)`
- Defined: `readmenator/_diagrams.py:213`
- Doc: Validate a system map and return a deterministic receipt.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_diagrams.py:432`
- Doc: Initialise the builder with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### supported_kinds (method) `def supported_kinds(self)`
- Defined: `readmenator/_diagrams.py:441`
- Doc: Return the supported diagram kind identifiers.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### build (method) `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind)`
- Defined: `readmenator/_diagrams.py:449`
- Doc: Build one deterministic system map of the requested kind.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### build_all (method) `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis)`
- Defined: `readmenator/_diagrams.py:484`
- Doc: Build all five diagram kinds deterministically.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### compare (method) `def compare(self, base, head)`
- Defined: `readmenator/_diagrams.py:513`
- Doc: Compare two maps of the same kind as before, delta, and after.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _title_for (method) `def _title_for(self, kind)`
- Defined: `readmenator/_diagrams.py:552`
- Doc: Return the display title for a diagram kind.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _role_for (method) `def _role_for(self, group, sensitive)`
- Defined: `readmenator/_diagrams.py:566`
- Doc: Return the semantic role for a group with sensitivity override.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _sensitive_files (method) `def _sensitive_files(self, findings)`
- Defined: `readmenator/_diagrams.py:583`
- Doc: Return files carrying elevated severity findings.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _ranked_file_ids (method) `def _ranked_file_ids(self, nodes, links, analysis)`
- Defined: `readmenator/_diagrams.py:600`
- Doc: Rank file identifiers by centrality then symbol count.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _select_primary (method) `def _select_primary(self, nodes, links, analysis)`
- Defined: `readmenator/_diagrams.py:635`
- Doc: Select the primary node scope honoring the configured limit.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _internal_links (method) `def _internal_links(self, edges, selected)`
- Defined: `readmenator/_diagrams.py:657`
- Doc: Filter edges to project-internal links between selected files.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _symbol_records (method) `def _symbol_records(self, node)`
- Defined: `readmenator/_diagrams.py:677`
- Doc: Build truncated symbol records for map documentation payloads.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _short_label (method) `def _short_label(self, value)`
- Defined: `readmenator/_diagrams.py:699`
- Doc: Shorten a label to the configured readable length.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _layout_columns (method) `def _layout_columns(self, items, kind)`
- Defined: `readmenator/_diagrams.py:714`
- Doc: Compute deterministic column lane coordinates for grouped items.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _lanes_that_fit (method) `def _lanes_that_fit(self, lanes)`
- Defined: `readmenator/_diagrams.py:760`
- Doc: Drop lowest-priority lanes until columns fit the canvas width.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _fitted_gap (method) `def _fitted_gap(self, count, item, gap, total, margin)`
- Defined: `readmenator/_diagrams.py:777`
- Doc: Compress spacing deterministically so items fit the canvas.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _lane_capacity (method) `def _lane_capacity(self)`
- Defined: `readmenator/_diagrams.py:801`
- Doc: Return the maximum members per lane fitting the canvas height.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _cap_lane_scope (method) `def _cap_lane_scope(self, ranked, layer_of)`
- Defined: `readmenator/_diagrams.py:815`
- Doc: Cap ranked nodes per lane so every lane fits the canvas height.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _layout_sequence (method) `def _layout_sequence(self, ordered)`
- Defined: `readmenator/_diagrams.py:839`
- Doc: Compute deterministic lifeline row coordinates for sequences.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _sequence_capacity (method) `def _sequence_capacity(self)`
- Defined: `readmenator/_diagrams.py:860`
- Doc: Return the maximum participants fitting the canvas width.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _place (method) `def _place(self, ranked, layer_of, kind)`
- Defined: `readmenator/_diagrams.py:874`
- Doc: Cap lane scope and compute coordinates for placed nodes only.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _make_views (method) `def _make_views(self, kind, primary, links)`
- Defined: `readmenator/_diagrams.py:893`
- Doc: Create guided chapters from authored topology.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _build_architecture (method) `def _build_architecture(self, nodes, links, layers, findings, analysis)`
- Defined: `readmenator/_diagrams.py:965`
- Doc: Build the runtime architecture map from file topology.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _build_workflow (method) `def _build_workflow(self, nodes, links, layers, findings)`
- Defined: `readmenator/_diagrams.py:1023`
- Doc: Build the delivery workflow map across architectural lanes.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _build_sequence (method) `def _build_sequence(self, nodes, links, layers, analysis)`
- Defined: `readmenator/_diagrams.py:1096`
- Doc: Build the request sequence map over top participants.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _build_dataflow (method) `def _build_dataflow(self, nodes, links, layers, findings)`
- Defined: `readmenator/_diagrams.py:1167`
- Doc: Build the data flow map from sources through stores.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _build_lifecycle (method) `def _build_lifecycle(self, nodes, links, layers, findings)`
- Defined: `readmenator/_diagrams.py:1248`
- Doc: Build the change lifecycle map with waits, retries, and terminals.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_diagrams.py:1341`
- Doc: Initialise the renderer with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### render (method) `def render(self, system_map)`
- Defined: `readmenator/_diagrams.py:1349`
- Doc: Render a system map as a self-contained HTML document.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### write (method) `def write(self, system_map, output_path)`
- Defined: `readmenator/_diagrams.py:1450`
- Doc: Render a system map and write it to a relative output path.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _safe_json (method) `def _safe_json(self, payload)`
- Defined: `readmenator/_diagrams.py:1469`
- Doc: Serialize a payload for safe inline script embedding.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _escape (method) `def _escape(self, value)`
- Defined: `readmenator/_diagrams.py:1480`
- Doc: Escape text for SVG and HTML embedding.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _role_color (method) `def _role_color(self, role)`
- Defined: `readmenator/_diagrams.py:1491`
- Doc: Return the stroke color for a semantic role.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _edge_path (method) `def _edge_path(self, x1, y1, x2, y2)`
- Defined: `readmenator/_diagrams.py:1502`
- Doc: Compute a deterministic curved route between two nodes.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _nodes_svg (method) `def _nodes_svg(self, system_map)`
- Defined: `readmenator/_diagrams.py:1538`
- Doc: Render authored nodes as inline SVG groups.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _edges_svg (method) `def _edges_svg(self, system_map)`
- Defined: `readmenator/_diagrams.py:1586`
- Doc: Render authored relationships as inline SVG paths.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _template (method) `def _template(self)`
- Defined: `readmenator/_diagrams.py:1633`
- Doc: Return the self-contained viewer document template.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_diagrams.py:2039`
- Doc: Initialise the renderer with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### render (method) `def render(self, system_map)`
- Defined: `readmenator/_diagrams.py:2047`
- Doc: Render a system map as a vis.js network HTML document.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### write (method) `def write(self, system_map, output_path)`
- Defined: `readmenator/_diagrams.py:2148`
- Doc: Render a vis.js map and write it to a relative output path.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _tooltip (method) `def _tooltip(self, node)`
- Defined: `readmenator/_diagrams.py:2165`
- Doc: Build a documentation tooltip for a network node.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _template (method) `def _template(self)`
- Defined: `readmenator/_diagrams.py:2196`
- Doc: Return the vis.js viewer document template.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_diagrams.py:2569`
- Doc: Initialise the publisher with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### description_for (method) `def description_for(self, kind)`
- Defined: `readmenator/_diagrams.py:2579`
- Doc: Return the gallery description for a diagram kind.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### publish (method) `def publish(self, maps, project_name, output_dir, stats, renderer)`
- Defined: `readmenator/_diagrams.py:2593`
- Doc: Publish maps and a gallery index into a documentation directory.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### render_index (method) `def render_index(self, project_name, maps, stats, href_prefix)`
- Defined: `readmenator/_diagrams.py:2651`
- Doc: Render the gallery index page for published maps.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _href_prefix (method) `def _href_prefix(self)`
- Defined: `readmenator/_diagrams.py:2748`
- Doc: Return the relative href prefix for map links.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _card (method) `def _card(self, kind, system_map, href_prefix)`
- Defined: `readmenator/_diagrams.py:2759`
- Doc: Render one gallery card linking to a published map.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _stats_line (method) `def _stats_line(self, stats)`
- Defined: `readmenator/_diagrams.py:2795`
- Doc: Render the gallery header statistics line.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

### _escape (method) `def _escape(self, value)`
- Defined: `readmenator/_diagrams.py:2809`
- Doc: Escape text for HTML embedding.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_diagrams.py`, `tests/test_diagrams.py`

## readmenator/_documentation.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_documentation.py:39`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _ranking_version (method) `def _ranking_version(self)`
- Defined: `readmenator/_documentation.py:57`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _get_git_commit (method) `def _get_git_commit()`
- Defined: `readmenator/_documentation.py:75`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### generate (method) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)`
- Defined: `readmenator/_documentation.py:85`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _apply_context_budget (method) `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)`
- Defined: `readmenator/_documentation.py:172`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_toc (method) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)`
- Defined: `readmenator/_documentation.py:310`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_layers (method) `def _build_layers(self, layers, nodes)`
- Defined: `readmenator/_documentation.py:398`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_dashboard (method) `def _build_dashboard(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_documentation.py:432`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_god_nodes (method) `def _build_god_nodes(self, analysis, ranked)`
- Defined: `readmenator/_documentation.py:512`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_community_analysis (method) `def _build_community_analysis(self, analysis, nodes)`
- Defined: `readmenator/_documentation.py:540`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_surprising_connections (method) `def _build_surprising_connections(self, analysis, nodes)`
- Defined: `readmenator/_documentation.py:573`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_suggested_questions (method) `def _build_suggested_questions(self, analysis)`
- Defined: `readmenator/_documentation.py:598`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_ranked_context (method) `def _build_ranked_context(self, ranked)`
- Defined: `readmenator/_documentation.py:614`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_orphans (method) `def _build_orphans(self, nodes, analysis_v2, ranked)`
- Defined: `readmenator/_documentation.py:660`
- Doc: Build a section listing nodes with low coverage signals.
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_query_recipes (method) `def _build_query_recipes(self)`
- Defined: `readmenator/_documentation.py:710`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_taint_analysis (method) `def _build_taint_analysis(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:752`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_hotspots (method) `def _build_hotspots(self, analysis_v2, ranked)`
- Defined: `readmenator/_documentation.py:787`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_dataflow_analysis (method) `def _build_dataflow_analysis(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:825`
- Doc: Build the procedural dataflow findings section.
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_dependency_cycles (method) `def _build_dependency_cycles(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:856`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_change_impact (method) `def _build_change_impact(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:877`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_layer_violations (method) `def _build_layer_violations(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:902`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_suggested_rules (method) `def _build_suggested_rules(self, analysis_v2)`
- Defined: `readmenator/_documentation.py:930`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_security_findings (method) `def _build_security_findings(self, findings)`
- Defined: `readmenator/_documentation.py:955`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_mermaid_section (method) `def _build_mermaid_section(self, graph_output, is_truncated)`
- Defined: `readmenator/_documentation.py:1002`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_uml_diagram (method) `def _build_uml_diagram(self, nodes, edges)`
- Defined: `readmenator/_documentation.py:1025`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_cpg_block (method) `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_documentation.py:1051`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

### _build_architecture_reference (method) `def _build_architecture_reference(self, nodes, edges)`
- Defined: `readmenator/_documentation.py:1077`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

## readmenator/_explain.py

### explain_rank (function) `def explain_rank(node_id, ranked, category)`
- Defined: `readmenator/_explain.py:16`
- Doc: Return a detailed breakdown of why *node_id* has its rank.
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

### rank_summary (function) `def rank_summary(ranked, top_n)`
- Defined: `readmenator/_explain.py:140`
- Doc: Return a short summary of the top-N ranked results.
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

### _find_item (function) `def _find_item(node_id, items)`
- Defined: `readmenator/_explain.py:163`
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

## readmenator/_exporter.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_exporter.py:29`
- Doc: Initialise with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_json (method) `def to_json(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:37`
- Doc: Export the graph as a node-link JSON string.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_html (method) `def to_html(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:150`
- Doc: Generate a standalone interactive HTML graph page.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _community_color_map (method) `def _community_color_map(self, analysis)`
- Defined: `readmenator/_exporter.py:239`
- Doc: Build a node-to-color map based on community membership.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _lighten (method) `def _lighten(hex_color)`
- Defined: `readmenator/_exporter.py:257`
- Doc: Lighten a hex color by 30% for border use.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _render_html (method) `def _render_html(self, vis_nodes, vis_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:265`
- Doc: Render the full HTML document with vis.js.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_svg (method) `def to_svg(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_exporter.py:436`
- Doc: Generate a static SVG representation of the graph.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _render_truncated_svg (method) `def _render_truncated_svg(self, total_nodes)`
- Defined: `readmenator/_exporter.py:554`
- Doc: Render a minimal SVG with a truncation notice.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _layout_spring (method) `def _layout_spring(self, nodes, edges, node_map)`
- Defined: `readmenator/_exporter.py:569`
- Doc: Compute a simple spring-layout for node positioning.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_graphml (method) `def to_graphml(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_exporter.py:650`
- Doc: Export the graph as GraphML (Gephi/yEd compatible).
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_cypher (method) `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)`
- Defined: `readmenator/_exporter.py:727`
- Doc: Export the graph as native Cypher CREATE statements.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### to_obsidian (method) `def to_obsidian(self, nodes, edges, output_dir, analysis)`
- Defined: `readmenator/_exporter.py:832`
- Doc: Export the graph as an Obsidian vault with wikilinks.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _project (method) `def _project(pos)`
- Defined: `readmenator/_exporter.py:498`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

### _sev_span (method) `def _sev_span(sev, count)`
- Defined: `readmenator/_exporter.py:337`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

## readmenator/_hotspots.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_hotspots.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### analyze_hotspots (method) `def analyze_hotspots(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_hotspots.py:28`
- Doc: Rank files by combined complexity and centrality scores.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### detect_cycles (method) `def detect_cycles(self, nodes, resolved_edges)`
- Defined: `readmenator/_hotspots.py:84`
- Doc: Detect cycles in the resolved import graph using DFS.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### analyze_change_impact (method) `def analyze_change_impact(self, nodes, resolved_edges)`
- Defined: `readmenator/_hotspots.py:149`
- Doc: Compute change impact for every file in the project.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### _dfs_visit (method) `def _dfs_visit(current)`
- Defined: `readmenator/_hotspots.py:108`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

### _record_cycle (method) `def _record_cycle(start, end)`
- Defined: `readmenator/_hotspots.py:119`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

## readmenator/_layer_rules.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_layer_rules.py:34`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

### detect_violations (method) `def detect_violations(self, nodes, edges, resolved_edges, layers)`
- Defined: `readmenator/_layer_rules.py:37`
- Doc: Detect architectural layer violations.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

### violation_summary (method) `def violation_summary(violations)`
- Defined: `readmenator/_layer_rules.py:109`
- Doc: Summarise violations by severity.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

## readmenator/_layers.py

### detect (method) `def detect(self, nodes, edges)`
- Defined: `readmenator/_layers.py:71`
- Doc: Assign each file node to an architectural layer.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

### _classify_file (method) `def _classify_file(self, node, edges)`
- Defined: `readmenator/_layers.py:89`
- Doc: Classify a single file into an architectural layer.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

### layer_summary (method) `def layer_summary(layers)`
- Defined: `readmenator/_layers.py:122`
- Doc: Count files per layer.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

## readmenator/_linter.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_linter.py:31`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### lint (method) `def lint(self, nodes, edges, resolved_edges, layers, content_map)`
- Defined: `readmenator/_linter.py:34`
- Doc: Run all linter rules and return violations.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _check_file_length (method) `def _check_file_length(self, nodes, content_map)`
- Defined: `readmenator/_linter.py:65`
- Doc: Check files against maximum line count threshold.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _check_cross_layer_violations (method) `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)`
- Defined: `readmenator/_linter.py:96`
- Doc: Check for forbidden cross-layer imports.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _check_circular_dependencies (method) `def _check_circular_dependencies(self, nodes, resolved_edges)`
- Defined: `readmenator/_linter.py:127`
- Doc: Check for circular dependencies in the resolved import graph.
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

### _dfs (method) `def _dfs(current)`
- Defined: `readmenator/_linter.py:146`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

## readmenator/_mcp_server.py

### main (method) `def main()`
- Defined: `readmenator/_mcp_server.py:796`
- Doc: CLI entry point for `readmenator serve <path>`.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ (method) `def __init__(self, code, message, data)`
- Defined: `readmenator/_mcp_server.py:59`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ (method) `def __init__(self, msg)`
- Defined: `readmenator/_mcp_server.py:72`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### is_notification (method) `def is_notification(self)`
- Defined: `readmenator/_mcp_server.py:79`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### response (method) `def response(self, result)`
- Defined: `readmenator/_mcp_server.py:82`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### error (method) `def error(self, code, message, data)`
- Defined: `readmenator/_mcp_server.py:85`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ (method) `def __init__(self, name, description, handler, input_schema)`
- Defined: `readmenator/_mcp_server.py:93`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### definition (method) `def definition(self)`
- Defined: `readmenator/_mcp_server.py:108`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### call (method) `def call(self, arguments)`
- Defined: `readmenator/_mcp_server.py:115`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ (method) `def __init__(self, uri, name, description, mime_type, handler)`
- Defined: `readmenator/_mcp_server.py:120`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### definition (method) `def definition(self)`
- Defined: `readmenator/_mcp_server.py:134`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### read (method) `def read(self)`
- Defined: `readmenator/_mcp_server.py:142`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### __init__ (method) `def __init__(self, app, target_dir)`
- Defined: `readmenator/_mcp_server.py:147`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### register_tool (method) `def register_tool(self, tool)`
- Defined: `readmenator/_mcp_server.py:155`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### register_resource (method) `def register_resource(self, resource)`
- Defined: `readmenator/_mcp_server.py:158`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _ensure_kb (method) `def _ensure_kb(self)`
- Defined: `readmenator/_mcp_server.py:161`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_initialize (method) `def _handle_initialize(self, req)`
- Defined: `readmenator/_mcp_server.py:173`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_list_tools (method) `def _handle_list_tools(self, req)`
- Defined: `readmenator/_mcp_server.py:187`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_call_tool (method) `def _handle_call_tool(self, req)`
- Defined: `readmenator/_mcp_server.py:192`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_list_resources (method) `def _handle_list_resources(self, req)`
- Defined: `readmenator/_mcp_server.py:214`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _handle_read_resource (method) `def _handle_read_resource(self, req)`
- Defined: `readmenator/_mcp_server.py:219`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### dispatch (method) `def dispatch(self, req)`
- Defined: `readmenator/_mcp_server.py:241`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### run (method) `def run(self)`
- Defined: `readmenator/_mcp_server.py:261`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _register_all (method) `def _register_all(self)`
- Defined: `readmenator/_mcp_server.py:285`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _scan (method) `def _scan(self)`
- Defined: `readmenator/_mcp_server.py:467`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _scan_deep (method) `def _scan_deep(self)`
- Defined: `readmenator/_mcp_server.py:473`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_summary (method) `def _tool_summary(self)`
- Defined: `readmenator/_mcp_server.py:481`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_query (method) `def _tool_query(self, text)`
- Defined: `readmenator/_mcp_server.py:519`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_explain (method) `def _tool_explain(self, name)`
- Defined: `readmenator/_mcp_server.py:524`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_path (method) `def _tool_path(self, symbol_a, symbol_b)`
- Defined: `readmenator/_mcp_server.py:536`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_findings (method) `def _tool_findings(self, min_severity)`
- Defined: `readmenator/_mcp_server.py:547`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_security_summary (method) `def _tool_security_summary(self)`
- Defined: `readmenator/_mcp_server.py:577`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_taint (method) `def _tool_taint(self)`
- Defined: `readmenator/_mcp_server.py:582`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_hotspots (method) `def _tool_hotspots(self, top_n)`
- Defined: `readmenator/_mcp_server.py:603`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_cycles (method) `def _tool_cycles(self)`
- Defined: `readmenator/_mcp_server.py:619`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_communities (method) `def _tool_communities(self)`
- Defined: `readmenator/_mcp_server.py:630`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_layers (method) `def _tool_layers(self)`
- Defined: `readmenator/_mcp_server.py:645`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_layer_violations (method) `def _tool_layer_violations(self)`
- Defined: `readmenator/_mcp_server.py:663`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_rebuild (method) `def _tool_rebuild(self)`
- Defined: `readmenator/_mcp_server.py:679`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_update (method) `def _tool_update(self)`
- Defined: `readmenator/_mcp_server.py:689`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _tool_export_json (method) `def _tool_export_json(self)`
- Defined: `readmenator/_mcp_server.py:697`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_summary (method) `def _resource_summary(self)`
- Defined: `readmenator/_mcp_server.py:705`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_graph (method) `def _resource_graph(self)`
- Defined: `readmenator/_mcp_server.py:722`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_findings (method) `def _resource_findings(self)`
- Defined: `readmenator/_mcp_server.py:741`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_analysis (method) `def _resource_analysis(self)`
- Defined: `readmenator/_mcp_server.py:757`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _resource_kb (method) `def _resource_kb(self)`
- Defined: `readmenator/_mcp_server.py:787`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

### _get_query_engine (method) `def _get_query_engine(self, nodes, edges, resolved)`
- Defined: `readmenator/_mcp_server.py:791`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

## readmenator/_mermaid.py

### __init__ (method) `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)`
- Defined: `readmenator/_mermaid.py:26`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

### _sanitize_id (method) `def _sanitize_id(node_id)`
- Defined: `readmenator/_mermaid.py:45`
- Doc: Convert *node_id* to a Mermaid-safe identifier.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

### render (method) `def render(self, nodes, edges, resolved_edges, analysis)`
- Defined: `readmenator/_mermaid.py:56`
- Doc: Produce a Mermaid flowchart string and a truncation flag.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

## readmenator/_models.py

### pluralize_symbol_kind (method) `def pluralize_symbol_kind(kind, plural_map)`
- Defined: `readmenator/_models.py:101`
- Doc: Return the plural form of *kind* according to *plural_map*.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_app.py`, `readmenator/_category.py`, `readmenator/_cpg.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dataflow.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_mermaid.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_refactorizer.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_analyzer.py`, `tests/test_cpg.py`, `tests/test_cursorrules.py`, `tests/test_dataflow.py`, `tests/test_dataflow.py`, `tests/test_dataflow.py`, `tests/test_dead_code.py`, `tests/test_diagrams.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_exporter.py`, `tests/test_hotspots.py`, `tests/test_layer_rules.py`, `tests/test_linter.py`, `tests/test_mermaid.py`, `tests/test_models.py`, `tests/test_parsers_property.py`, `tests/test_query.py`, `tests/test_ranking.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_rule_gen.py`, `tests/test_sarif.py`, `tests/test_scanner.py`, `tests/test_security.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`, `tests/test_uml.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

## readmenator/_pipeline.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_pipeline.py:49`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### scanner (method) `def scanner(self)`
- Defined: `readmenator/_pipeline.py:78`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### generator (method) `def generator(self)`
- Defined: `readmenator/_pipeline.py:84`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### analyzer (method) `def analyzer(self)`
- Defined: `readmenator/_pipeline.py:90`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### security (method) `def security(self)`
- Defined: `readmenator/_pipeline.py:96`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### exporter (method) `def exporter(self)`
- Defined: `readmenator/_pipeline.py:102`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### taint (method) `def taint(self)`
- Defined: `readmenator/_pipeline.py:108`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### dataflow (method) `def dataflow(self)`
- Defined: `readmenator/_pipeline.py:114`
- Doc: Return the lazily initialised dataflow analyzer.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### hotspots (method) `def hotspots(self)`
- Defined: `readmenator/_pipeline.py:121`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### layer_rules (method) `def layer_rules(self)`
- Defined: `readmenator/_pipeline.py:127`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### rule_gen (method) `def rule_gen(self)`
- Defined: `readmenator/_pipeline.py:133`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### sarif (method) `def sarif(self)`
- Defined: `readmenator/_pipeline.py:139`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### cpg (method) `def cpg(self)`
- Defined: `readmenator/_pipeline.py:145`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### layer_detector (method) `def layer_detector(self)`
- Defined: `readmenator/_pipeline.py:154`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### uml (method) `def uml(self)`
- Defined: `readmenator/_pipeline.py:160`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### wiki (method) `def wiki(self)`
- Defined: `readmenator/_pipeline.py:166`
- Doc: Return the lazily initialised agent wiki generator.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### readme_injector (method) `def readme_injector(self)`
- Defined: `readmenator/_pipeline.py:173`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### agent_injector (method) `def agent_injector(self)`
- Defined: `readmenator/_pipeline.py:183`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### agent_output (method) `def agent_output(self)`
- Defined: `readmenator/_pipeline.py:193`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### diagram_builder (method) `def diagram_builder(self)`
- Defined: `readmenator/_pipeline.py:199`
- Doc: Return the lazily initialised system map builder.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### diagram_renderer (method) `def diagram_renderer(self)`
- Defined: `readmenator/_pipeline.py:206`
- Doc: Return the lazily initialised interactive map renderer.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### diagram_validator (method) `def diagram_validator(self)`
- Defined: `readmenator/_pipeline.py:213`
- Doc: Return the lazily initialised system map validator.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### diagram_publisher (method) `def diagram_publisher(self)`
- Defined: `readmenator/_pipeline.py:220`
- Doc: Return the lazily initialised documentation site publisher.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### vis_renderer (method) `def vis_renderer(self)`
- Defined: `readmenator/_pipeline.py:227`
- Doc: Return the lazily initialised vis.js network renderer.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### build_typed_graph (method) `def build_typed_graph(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_pipeline.py:233`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### make_ranker (method) `def make_ranker(self, typed_graph)`
- Defined: `readmenator/_pipeline.py:243`
- Doc: Create a CompositeRanker for the given typed graph.
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### last_category (method) `def last_category(self)`
- Defined: `readmenator/_pipeline.py:260`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### last_typed_graph (method) `def last_typed_graph(self)`
- Defined: `readmenator/_pipeline.py:264`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### __init__ (method) `def __init__(self, factory)`
- Defined: `readmenator/_pipeline.py:277`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

### run (method) `def run(self, nodes, edges, resolved_edges, layers, content_map)`
- Defined: `readmenator/_pipeline.py:280`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_wiki.py`
- Imported by: `readmenator/_app.py`

## readmenator/_projections.py

### apply_view (method) `def apply_view(category, view_config)`
- Defined: `readmenator/_projections.py:95`
- Doc: Apply a named view to produce a projected category.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node (method) `def map_node(self, node)`
- Defined: `readmenator/_projections.py:23`
- Doc: Map a code node. Return None to exclude.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism (method) `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:27`
- Doc: Map a morphism. Return None to exclude.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node (method) `def map_node(self, node)`
- Defined: `readmenator/_projections.py:35`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism (method) `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:38`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### __init__ (method) `def __init__(self, documented_ids)`
- Defined: `readmenator/_projections.py:49`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node (method) `def map_node(self, node)`
- Defined: `readmenator/_projections.py:52`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism (method) `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:57`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### __init__ (method) `def __init__(self, fan_in, fan_out, test_files)`
- Defined: `readmenator/_projections.py:70`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_node (method) `def map_node(self, node)`
- Defined: `readmenator/_projections.py:80`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

### map_morphism (method) `def map_morphism(self, m)`
- Defined: `readmenator/_projections.py:91`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

## readmenator/_query.py

### __init__ (method) `def __init__(self, nodes, edges, resolved_edges, ranker, config)`
- Defined: `readmenator/_query.py:34`
- Doc: Initialise internal indexes from scanned data.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _init_default_ranker (method) `def _init_default_ranker(self)`
- Defined: `readmenator/_query.py:64`
- Doc: Build a default CompositeRanker from the loaded data.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### ranked_query (method) `def ranked_query(self, query, top_n)`
- Defined: `readmenator/_query.py:73`
- Doc: Answer *query* with a ranked list of relevant nodes.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _estimate_test_coverage (method) `def _estimate_test_coverage(self)`
- Defined: `readmenator/_query.py:124`
- Doc: Estimate test coverage per file.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _estimate_doc_coverage (method) `def _estimate_doc_coverage(self)`
- Defined: `readmenator/_query.py:150`
- Doc: Estimate documentation coverage per file.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _build_symbol_index (method) `def _build_symbol_index(self)`
- Defined: `readmenator/_query.py:170`
- Doc: Build a name-to-list-of-(node, symbol) lookup.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _build_import_graph (method) `def _build_import_graph(self)`
- Defined: `readmenator/_query.py:184`
- Doc: Build an adjacency map from import edges.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _build_resolved_graph (method) `def _build_resolved_graph(self)`
- Defined: `readmenator/_query.py:200`
- Doc: Build an adjacency map from resolved import edges.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### find_symbol (method) `def find_symbol(self, name)`
- Defined: `readmenator/_query.py:220`
- Doc: Look up *name* by exact match, then by substring fuzzy match.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### explain (method) `def explain(self, name)`
- Defined: `readmenator/_query.py:238`
- Doc: Return a detailed multi-line explanation of *name*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _find_incoming_imports (method) `def _find_incoming_imports(self, target)`
- Defined: `readmenator/_query.py:277`
- Doc: List all node IDs that import *target*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### find_path (method) `def find_path(self, symbol_a, symbol_b)`
- Defined: `readmenator/_query.py:285`
- Doc: Find the shortest import path from *symbol_a* to *symbol_b*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _make_bidirectional (method) `def _make_bidirectional(graph)`
- Defined: `readmenator/_query.py:315`
- Doc: Convert a directed graph to a bidirectional one.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### _bfs_shortest_path (method) `def _bfs_shortest_path(self, graph, start, goal)`
- Defined: `readmenator/_query.py:331`
- Doc: Run BFS to find the shortest path from *start* to *goal*.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### query (method) `def query(self, question)`
- Defined: `readmenator/_query.py:355`
- Doc: Free-text search over symbols and file paths.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

### summary (method) `def summary(self)`
- Defined: `readmenator/_query.py:411`
- Doc: Return a concise overview of the loaded knowledge base.
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

## readmenator/_rank.py

### global_pagerank (method) `def global_pagerank(graph, alpha, max_iter, tolerance)`
- Defined: `readmenator/_rank.py:61`
- Doc: Compute global PageRank on the typed weighted graph.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### personalized_pagerank (method) `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)`
- Defined: `readmenator/_rank.py:119`
- Doc: Compute Personalized PageRank with a seed-node preference vector.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### hits (method) `def hits(graph, max_iter, tolerance)`
- Defined: `readmenator/_rank.py:189`
- Doc: Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### build_seeds_from_query (method) `def build_seeds_from_query(query, node_ids, node_labels, symbols)`
- Defined: `readmenator/_rank.py:240`
- Doc: Build a PPR seed vector from a natural-language query string.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### build_seeds_for_context (method) `def build_seeds_for_context(node_ids, anchor_patterns)`
- Defined: `readmenator/_rank.py:286`
- Doc: Build a PPR seed vector from anchor pattern strings.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### _format_explanation (method) `def _format_explanation(item, result)`
- Defined: `readmenator/_rank.py:512`
- Doc: Format a human-readable explanation for a ranked item.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### label (method) `def label(self)`
- Defined: `readmenator/_rank.py:344`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### top (method) `def top(self, n)`
- Defined: `readmenator/_rank.py:366`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### explain (method) `def explain(self, node_id)`
- Defined: `readmenator/_rank.py:369`
- Doc: Return a human-readable explanation of why *node_id* ranks as it does.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### __init__ (method) `def __init__(self, graph, config)`
- Defined: `readmenator/_rank.py:385`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### _get_global_pr (method) `def _get_global_pr(self)`
- Defined: `readmenator/_rank.py:394`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### rank (method) `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)`
- Defined: `readmenator/_rank.py:404`
- Doc: Compute composite ranking for a query.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

### _find_justification_paths (method) `def _find_justification_paths(self, target, seed_ids, category, max_paths)`
- Defined: `readmenator/_rank.py:486`
- Doc: Find shortest paths from any seed to target.
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

## readmenator/_readme_injector.py

### __init__ (method) `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)`
- Defined: `readmenator/_readme_injector.py:76`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### inject (method) `def inject(self, project_root)`
- Defined: `readmenator/_readme_injector.py:86`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _extract_current_injection (method) `def _extract_current_injection(content)`
- Defined: `readmenator/_readme_injector.py:115`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _remove_old_injection (method) `def _remove_old_injection(content)`
- Defined: `readmenator/_readme_injector.py:124`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### remove (method) `def remove(self, project_root)`
- Defined: `readmenator/_readme_injector.py:134`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _find_readme (method) `def _find_readme(root)`
- Defined: `readmenator/_readme_injector.py:163`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

### _build_injection (method) `def _build_injection(self, suffix)`
- Defined: `readmenator/_readme_injector.py:170`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

## readmenator/_refactorizer.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_refactorizer.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### analyze (method) `def analyze(self, nodes, edges, resolved_edges, content_map)`
- Defined: `readmenator/_refactorizer.py:35`
- Doc: Identify monolithic files and generate refactoring plans.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _get_line_count (method) `def _get_line_count(self, file_id, content_map)`
- Defined: `readmenator/_refactorizer.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _plan_refactoring (method) `def _plan_refactoring(self, node, edges, resolved_edges, content_map)`
- Defined: `readmenator/_refactorizer.py:82`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _group_symbols_by_kind (method) `def _group_symbols_by_kind(self, symbols)`
- Defined: `readmenator/_refactorizer.py:126`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _suggest_target_file (method) `def _suggest_target_file(self, source_file, kind)`
- Defined: `readmenator/_refactorizer.py:132`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### _estimate_impact (method) `def _estimate_impact(self, file_id, resolved_edges)`
- Defined: `readmenator/_refactorizer.py:147`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

### generate_script (method) `def generate_script(self, plan, project_root)`
- Defined: `readmenator/_refactorizer.py:156`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

## readmenator/_resolver.py

### __init__ (method) `def __init__(self, file_ids, root, extensions, include_dirs)`
- Defined: `readmenator/_resolver.py:61`
- Doc: Initialise the resolver with all known file paths.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _build_stem_index (method) `def _build_stem_index(self, file_ids)`
- Defined: `readmenator/_resolver.py:83`
- Doc: Map file stems (without extension) to their full paths.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _build_dir_index (method) `def _build_dir_index(self, file_ids)`
- Defined: `readmenator/_resolver.py:93`
- Doc: Map directory paths to the files they contain.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### resolve (method) `def resolve(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:110`
- Doc: Resolve an import string to a concrete project file path.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### resolve_all (method) `def resolve_all(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:159`
- Doc: Resolve *import_str* to all possible matching project file paths.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_include_dirs (method) `def _resolve_include_dirs(self, import_str)`
- Defined: `readmenator/_resolver.py:175`
- Doc: Resolve *import_str* against configured ``-I`` include dirs.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_relative (method) `def _resolve_relative(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:195`
- Doc: Resolve a relative import (starts with ``.`` or ``..``).
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_verbatim (method) `def _resolve_verbatim(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:213`
- Doc: Resolve a path-like import verbatim against the source directory.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_extensionless (method) `def _resolve_extensionless(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:231`
- Doc: Resolve a bare module name by appending known extensions.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_directory_init (method) `def _resolve_directory_init(self, import_str, source_file)`
- Defined: `readmenator/_resolver.py:240`
- Doc: Resolve as a package directory with __init__ or index file.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_module_dotpath (method) `def _resolve_module_dotpath(self, import_str)`
- Defined: `readmenator/_resolver.py:250`
- Doc: Resolve a dotted module path (Python/Java convention).
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_suffix_match (method) `def _resolve_suffix_match(self, import_str)`
- Defined: `readmenator/_resolver.py:272`
- Doc: Match a slash-qualified include against project path suffixes.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_basename_match (method) `def _resolve_basename_match(self, import_str)`
- Defined: `readmenator/_resolver.py:287`
- Doc: Match by exact file basename including extension.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _resolve_stem_match (method) `def _resolve_stem_match(self, import_str)`
- Defined: `readmenator/_resolver.py:305`
- Doc: Match by file stem only (last resort).
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

### _strip_extension (method) `def _strip_extension(self, name)`
- Defined: `readmenator/_resolver.py:314`
- Doc: Remove a trailing known source extension from a file name.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

## readmenator/_rule_gen.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_rule_gen.py:88`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### generate (method) `def generate(self, nodes, content_map)`
- Defined: `readmenator/_rule_gen.py:92`
- Doc: Generate suggested rules by scanning code patterns.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### write_rules (method) `def write_rules(self, rules, output_dir)`
- Defined: `readmenator/_rule_gen.py:120`
- Doc: Write suggested rules to Semgrep YAML files in output_dir.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _group_by_language (method) `def _group_by_language(self, nodes)`
- Defined: `readmenator/_rule_gen.py:159`
- Doc: Group nodes by their language extension.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _analyze_language (method) `def _analyze_language(self, lang, nodes, content_map)`
- Defined: `readmenator/_rule_gen.py:169`
- Doc: Analyze a single language group for rule suggestions.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _detect_antipatterns (method) `def _detect_antipatterns(self, nodes, content_map)`
- Defined: `readmenator/_rule_gen.py:202`
- Doc: Detect known antipatterns across all files.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _infer_language_for_rule (method) `def _infer_language_for_rule(rule_id)`
- Defined: `readmenator/_rule_gen.py:248`
- Doc: Infer target language for a built-in antipattern rule.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

### _next_rule_id (method) `def _next_rule_id(self)`
- Defined: `readmenator/_rule_gen.py:258`
- Doc: Generate the next rule identifier.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

## readmenator/_sarif.py

### __init__ (method) `def __init__(self, privacy_mode)`
- Defined: `readmenator/_sarif.py:28`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

### export (method) `def export(self, findings, project_name)`
- Defined: `readmenator/_sarif.py:31`
- Doc: Generate a SARIF v2.1.0 JSON string from security findings.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

### _build_rule (method) `def _build_rule(self, finding)`
- Defined: `readmenator/_sarif.py:80`
- Doc: Build a SARIF reportingDescriptor (rule) object.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

### _build_result (method) `def _build_result(self, finding, rule_index)`
- Defined: `readmenator/_sarif.py:104`
- Doc: Build a SARIF result object for a single finding.
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

## readmenator/_scanner.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_scanner.py:39`
- Doc: Initialise the scanner with application configuration.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _is_ignored (method) `def _is_ignored(self, path)`
- Defined: `readmenator/_scanner.py:50`
- Doc: Return ``True`` if any path component matches IGNORE_DIRS.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _load_gitignore (method) `def _load_gitignore(self, root)`
- Defined: `readmenator/_scanner.py:57`
- Doc: Parse .gitignore patterns using regex (no external deps).
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _gitignore_glob_to_regex (method) `def _gitignore_glob_to_regex(pattern)`
- Defined: `readmenator/_scanner.py:79`
- Doc: Convert a .gitignore glob pattern to a regex pattern.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _is_gitignored (method) `def _is_gitignored(self, rel_path)`
- Defined: `readmenator/_scanner.py:119`
- Doc: Check if a relative path matches any .gitignore pattern.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _validate_path_security (method) `def _validate_path_security(self, path)`
- Defined: `readmenator/_scanner.py:128`
- Doc: Reject symlinks and files exceeding MAX_FILE_SIZE_MB.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _check_directory_depth (method) `def _check_directory_depth(self, path, root)`
- Defined: `readmenator/_scanner.py:141`
- Doc: Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _extract_file_doc (method) `def _extract_file_doc(self, content)`
- Defined: `readmenator/_scanner.py:149`
- Doc: Extract a file-level docstring from the first lines of a source file.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _emit_progress (method) `def _emit_progress(self, count)`
- Defined: `readmenator/_scanner.py:225`
- Doc: Emit a progress message every PROGRESS_REPORT_BATCH files.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### scan (method) `def scan(self, root)`
- Defined: `readmenator/_scanner.py:235`
- Doc: Walk *root* recursively and produce (nodes, edges) for the graph.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### scan_with_content (method) `def scan_with_content(self, root)`
- Defined: `readmenator/_scanner.py:249`
- Doc: Scan and also return raw file contents for deeper analysis.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

### _scan_impl (method) `def _scan_impl(self, root)`
- Defined: `readmenator/_scanner.py:260`
- Doc: Internal scan implementation returning nodes, edges, and content.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

## readmenator/_security.py

### _parse_minimal_yaml (method) `def _parse_minimal_yaml(text)`
- Defined: `readmenator/_security.py:46`
- Doc: Parse the simplified YAML format used by _security_rules.yml.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _unquote (method) `def _unquote(s)`
- Defined: `readmenator/_security.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _load_rules_from_yaml (method) `def _load_rules_from_yaml(yaml_path)`
- Defined: `readmenator/_security.py:128`
- Doc: Load rule dicts from the YAML rules file, or return None on failure.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _compile (method) `def _compile()`
- Defined: `readmenator/_security.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _python_rules (method) `def _python_rules()`
- Defined: `readmenator/_security.py:153`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _javascript_rules (method) `def _javascript_rules()`
- Defined: `readmenator/_security.py:182`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _c_rules (method) `def _c_rules()`
- Defined: `readmenator/_security.py:201`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _java_rules (method) `def _java_rules()`
- Defined: `readmenator/_security.py:222`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _go_rules (method) `def _go_rules()`
- Defined: `readmenator/_security.py:237`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _ruby_rules (method) `def _ruby_rules()`
- Defined: `readmenator/_security.py:250`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _php_rules (method) `def _php_rules()`
- Defined: `readmenator/_security.py:267`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _shell_rules (method) `def _shell_rules()`
- Defined: `readmenator/_security.py:284`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _csharp_rules (method) `def _csharp_rules()`
- Defined: `readmenator/_security.py:297`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _kotlin_rules (method) `def _kotlin_rules()`
- Defined: `readmenator/_security.py:310`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _swift_rules (method) `def _swift_rules()`
- Defined: `readmenator/_security.py:321`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _scala_rules (method) `def _scala_rules()`
- Defined: `readmenator/_security.py:332`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _lua_rules (method) `def _lua_rules()`
- Defined: `readmenator/_security.py:343`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _dart_rules (method) `def _dart_rules()`
- Defined: `readmenator/_security.py:354`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _rust_rules (method) `def _rust_rules()`
- Defined: `readmenator/_security.py:365`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _nim_rules (method) `def _nim_rules()`
- Defined: `readmenator/_security.py:376`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _gdscript_rules (method) `def _gdscript_rules()`
- Defined: `readmenator/_security.py:387`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _elixir_rules (method) `def _elixir_rules()`
- Defined: `readmenator/_security.py:398`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _build_rules_from_yaml (method) `def _build_rules_from_yaml(yaml_path)`
- Defined: `readmenator/_security.py:447`
- Doc: Attempt to build the rule map from the YAML rules file.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### fix_hint_for (method) `def fix_hint_for(finding)`
- Defined: `readmenator/_security.py:620`
- Doc: Return a one-line remediation hint for a security finding.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_security.py:496`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _resolve_rules (method) `def _resolve_rules(self)`
- Defined: `readmenator/_security.py:500`
- Doc: Resolve rules: prefer YAML, fall back to built-in.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _meets_threshold (method) `def _meets_threshold(self, severity)`
- Defined: `readmenator/_security.py:509`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### scan (method) `def scan(self, root)`
- Defined: `readmenator/_security.py:513`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### _validate_path (method) `def _validate_path(self, path, root)`
- Defined: `readmenator/_security.py:555`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

### summary (method) `def summary(self, findings)`
- Defined: `readmenator/_security.py:572`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

## readmenator/_taint.py

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_taint.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### analyze (method) `def analyze(self, nodes, edges, resolved_edges)`
- Defined: `readmenator/_taint.py:75`
- Doc: Run taint propagation analysis on the codebase.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### _find_direct_sources (method) `def _find_direct_sources(self, nodes, edges)`
- Defined: `readmenator/_taint.py:134`
- Doc: Find files that directly import known-dangerous modules.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### _propagate (method) `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)`
- Defined: `readmenator/_taint.py:160`
- Doc: BFS propagation from source through the import graph.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

### _build_forward_graph (method) `def _build_forward_graph(nodes, resolved_edges)`
- Defined: `readmenator/_taint.py:211`
- Doc: Build a forward-directed import graph from resolved edges.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

## readmenator/_uml.py

### _get_code_generator (method) `def _get_code_generator(language)`
- Defined: `readmenator/_uml.py:170`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _type_map_py_to_target (method) `def _type_map_py_to_target(target, py_type_hint)`
- Defined: `readmenator/_uml.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_cpp (method) `def _generate_cpp(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:231`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _cpp_params (method) `def _cpp_params(params)`
- Defined: `readmenator/_uml.py:257`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_java (method) `def _generate_java(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:272`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _java_params (method) `def _java_params(params)`
- Defined: `readmenator/_uml.py:299`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_csharp (method) `def _generate_csharp(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:314`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _cs_params (method) `def _cs_params(params)`
- Defined: `readmenator/_uml.py:343`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_python (method) `def _generate_python(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:358`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_go (method) `def _generate_go(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:393`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_rust (method) `def _generate_rust(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:420`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_php (method) `def _generate_php(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:446`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_kotlin (method) `def _generate_kotlin(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:474`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_scala (method) `def _generate_scala(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:494`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_swift (method) `def _generate_swift(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:516`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_dart (method) `def _generate_dart(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:545`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _generate_ruby (method) `def _generate_ruby(class_symbols, nodes, edges)`
- Defined: `readmenator/_uml.py:565`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _safe_name (method) `def _safe_name(name)`
- Defined: `readmenator/_uml.py:586`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _extract_params (method) `def _extract_params(signature)`
- Defined: `readmenator/_uml.py:590`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_uml.py:34`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### render_mermaid_class_diagram (method) `def render_mermaid_class_diagram(self, nodes, edges)`
- Defined: `readmenator/_uml.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### generate_code (method) `def generate_code(self, nodes, edges, target_language)`
- Defined: `readmenator/_uml.py:127`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _sanitize_id (method) `def _sanitize_id(raw)`
- Defined: `readmenator/_uml.py:151`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

### _find_node (method) `def _find_node(nodes, node_id)`
- Defined: `readmenator/_uml.py:163`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

## readmenator/_watcher.py

### __init__ (method) `def __init__(self, root, config, callback, interval_seconds)`
- Defined: `readmenator/_watcher.py:29`
- Doc: Initialise the watcher for a project root.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

### _compute_snapshot (method) `def _compute_snapshot(self)`
- Defined: `readmenator/_watcher.py:51`
- Doc: Compute a quick hash of all tracked files in the project.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

### start (method) `def start(self)`
- Defined: `readmenator/_watcher.py:80`
- Doc: Start watching the directory (blocking).
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

### stop (method) `def stop(self)`
- Defined: `readmenator/_watcher.py:97`
- Doc: Stop watching.
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`

## readmenator/_wiki.py

### _is_garbage_purpose (function) `def _is_garbage_purpose(text)`
- Defined: `readmenator/_wiki.py:44`
- Doc: Return True for file-doc first lines that state no purpose.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _clean_purpose (function) `def _clean_purpose(text)`
- Defined: `readmenator/_wiki.py:55`
- Doc: Return the purpose signal of a doc first line, or empty string.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _slug (function) `def _slug(text)`
- Defined: `readmenator/_wiki.py:74`
- Doc: Return a filesystem-safe slug for community labels.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _escape (function) `def _escape(text)`
- Defined: `readmenator/_wiki.py:81`
- Doc: Escape markdown table breaking characters in one line of text.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _is_garbage_doc (function) `def _is_garbage_doc(text)`
- Defined: `readmenator/_wiki.py:86`
- Doc: Return True for doc lines that carry no purpose signal.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### existing_ids (function) `def existing_ids(connections)`
- Defined: `readmenator/_wiki.py:96`
- Doc: Return community id pairs already linked, to avoid duplicate edges.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _display_names (function) `def _display_names(communities)`
- Defined: `readmenator/_wiki.py:106`
- Doc: Return unique display names, disambiguating duplicate labels.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator/_wiki.py:123`
- Doc: Store configuration for wiki output limits and paths.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### generate (method) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)`
- Defined: `readmenator/_wiki.py:128`
- Doc: Write all wiki files and return the output directory path.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _prune_stale_pages (method) `def _prune_stale_pages(self, out_dir, current)`
- Defined: `readmenator/_wiki.py:176`
- Doc: Delete community pages from previous runs that are no longer generated.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### lint (method) `def lint(self, project_root)`
- Defined: `readmenator/_wiki.py:185`
- Doc: Check wiki health and return a list of issue descriptions.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _resolve_communities (method) `def _resolve_communities(self, nodes, analysis, resolved)`
- Defined: `readmenator/_wiki.py:208`
- Doc: Return detected communities plus an orphan fallback for leftovers.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _community_of (method) `def _community_of(self, node_id, communities)`
- Defined: `readmenator/_wiki.py:234`
- Doc: Return the community containing the given node id.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_connections (method) `def _build_connections(self, communities, resolved, analysis, node_map, layers)`
- Defined: `readmenator/_wiki.py:243`
- Doc: Derive typed bridges between communities with strength scores.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _duplicate_links (method) `def _duplicate_links(communities, node_map, skip_pairs)`
- Defined: `readmenator/_wiki.py:308`
- Doc: Flag community pairs sharing an unusual fraction of symbol names.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _shared_context_links (method) `def _shared_context_links(self, communities, existing, node_map, layers)`
- Defined: `readmenator/_wiki.py:351`
- Doc: Infer weak links between otherwise disconnected communities.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _shared_context (method) `def _shared_context(first, second, node_map, layers)`
- Defined: `readmenator/_wiki.py:387`
- Doc: Describe shared language or layer between two communities.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_connections_json (method) `def _build_connections_json(self, connections)`
- Defined: `readmenator/_wiki.py:420`
- Doc: Serialize connections as pretty-printed JSON.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _definition_for (method) `def _definition_for(self, community, node_map)`
- Defined: `readmenator/_wiki.py:424`
- Doc: Synthesize a one-paragraph definition for a community.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _file_row (method) `def _file_row(self, fid, node_map, layers)`
- Defined: `readmenator/_wiki.py:453`
- Doc: Return a markdown table row for a single file, or empty string.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_grouped_files (method) `def _build_grouped_files(self, members, node_map, layers, max_files)`
- Defined: `readmenator/_wiki.py:467`
- Doc: List oversized communities grouped by directory within budget.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_community_page (method) `def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)`
- Defined: `readmenator/_wiki.py:516`
- Doc: Build the synthesis page for a single community.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _questions_for (method) `def _questions_for(self, community, node_map, member_set, analysis_v2)`
- Defined: `readmenator/_wiki.py:669`
- Doc: Generate deterministic open questions for a community.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _large_files (method) `def _large_files(self, nodes, project_root)`
- Defined: `readmenator/_wiki.py:707`
- Doc: Return node ids whose on-disk size exceeds the large-file threshold.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_index (method) `def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections, project_name, project_root)`
- Defined: `readmenator/_wiki.py:720`
- Doc: Build the wiki entry point with overview and navigation.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _overview_paragraph (method) `def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)`
- Defined: `readmenator/_wiki.py:832`
- Doc: Synthesize the central preoccupations paragraph.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _connective_paragraph (method) `def _connective_paragraph(self, communities, connections)`
- Defined: `readmenator/_wiki.py:865`
- Doc: Synthesize the connective tissue paragraph.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _questions_paragraph (method) `def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)`
- Defined: `readmenator/_wiki.py:886`
- Doc: Synthesize the open questions paragraph.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_queries (method) `def _build_queries(self, analysis)`
- Defined: `readmenator/_wiki.py:902`
- Doc: Build the starter question log with feedback loop instructions.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _build_report (method) `def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name, project_root)`
- Defined: `readmenator/_wiki.py:927`
- Doc: Build the honest audit report with confidence and limits.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _estimate_tokens (method) `def _estimate_tokens(self, nodes, connections)`
- Defined: `readmenator/_wiki.py:999`
- Doc: Estimate wiki read cost as characters divided by four.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### _write (method) `def _write(path, content)`
- Defined: `readmenator/_wiki.py:1010`
- Doc: Write wiki file content with UTF-8 encoding.
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

### dominant (method) `def dominant(ids, key)`
- Defined: `readmenator/_wiki.py:394`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`, `tests/test_wiki.py`, `tests/test_wiki.py`

## readmenator/parsers/__init__.py

### _init_parser_map (function) `def _init_parser_map()`
- Defined: `readmenator/parsers/__init__.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`

### create_parser (function) `def create_parser(extension, filename, config)`
- Defined: `readmenator/parsers/__init__.py:68`
- Doc: Factory: return a parser instance for the given file extension.
- Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`

## readmenator/parsers/_assembly.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_assembly.py:17`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`

## readmenator/parsers/_base.py

### __init__ (method) `def __init__(self, filename, config)`
- Defined: `readmenator/parsers/_base.py:19`
- Doc: Initialise the parser with a file path and application config.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### parse (method) `def parse(self, content)`
- Defined: `readmenator/parsers/_base.py:34`
- Doc: Parse *content* and populate symbol/import lists.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_base.py:43`
- Doc: Subclass hook for language-specific symbol extraction.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _extract_docstring (method) `def _extract_docstring(self, line_num)`
- Defined: `readmenator/parsers/_base.py:47`
- Doc: Walk backwards from *line_num* to collect preceding comments/docstrings.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _extract_signature (method) `def _extract_signature(self, content, match_start, pattern)`
- Defined: `readmenator/parsers/_base.py:89`
- Doc: Extract a compact signature snippet starting at *match_start*.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

## readmenator/parsers/_c.py

### _has_type_prefix (function) `def _has_type_prefix(prefix)`
- Defined: `readmenator/parsers/_c.py:16`
- Doc: Return True when a prototype prefix carries a return type.
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_c.py:35`
- Doc: Extract C-family symbols and imports from source content.
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_csharp.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_csharp.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_dart.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_dart.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_elixir.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_elixir.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_gdscript.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_gdscript.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_go.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_go.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_java.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_java.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_javascript.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_javascript.py:17`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_kotlin.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_kotlin.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_lua.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_lua.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_nim.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_nim.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_php.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_php.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_python.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_python.py:17`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_ruby.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_ruby.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_rust.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_rust.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_scala.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_scala.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_shell.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_shell.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator/parsers/_swift.py

### _extract_specifics (method) `def _extract_specifics(self, content)`
- Defined: `readmenator/parsers/_swift.py:16`
- Depends on: `readmenator/_models.py`, `readmenator/parsers/_base.py`
- Imported by: `readmenator/parsers/__init__.py`, `tests/test_parsers_property.py`

## readmenator_orchestrator.py

### _validate_repo_name (method) `def _validate_repo_name(name)`
- Defined: `readmenator_orchestrator.py:50`

### _validate_branch_name (method) `def _validate_branch_name(name)`
- Defined: `readmenator_orchestrator.py:56`

### _safe_env (method) `def _safe_env()`
- Defined: `readmenator_orchestrator.py:62`

### parse_arguments (method) `def parse_arguments()`
- Defined: `readmenator_orchestrator.py:438`

### main (method) `def main()`
- Defined: `readmenator_orchestrator.py:455`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator_orchestrator.py:78`

### _resolve_user (method) `def _resolve_user(self)`
- Defined: `readmenator_orchestrator.py:83`

### _setup_git_auth (method) `def _setup_git_auth(self)`
- Defined: `readmenator_orchestrator.py:104`

### list_repos (method) `def list_repos(self)`
- Defined: `readmenator_orchestrator.py:118`

### close_existing_prs (method) `def close_existing_prs(self, repo)`
- Defined: `readmenator_orchestrator.py:130`

### delete_remote_branch (method) `def delete_remote_branch(self, repo)`
- Defined: `readmenator_orchestrator.py:158`

### create_pr (method) `def create_pr(self, repo, default_branch, timestamp)`
- Defined: `readmenator_orchestrator.py:170`

### __init__ (method) `def __init__(self, config, github_client)`
- Defined: `readmenator_orchestrator.py:192`

### process (method) `def process(self, repo)`
- Defined: `readmenator_orchestrator.py:196`

### _get_default_branch (method) `def _get_default_branch(self, repo)`
- Defined: `readmenator_orchestrator.py:225`

### _clone_repository (method) `def _clone_repository(self, repo)`
- Defined: `readmenator_orchestrator.py:241`

### _run_readmenator (method) `def _run_readmenator(self, repo_dir)`
- Defined: `readmenator_orchestrator.py:257`

### _copy_to_docs_dir (method) `def _copy_to_docs_dir(self, repo_dir, generated_file)`
- Defined: `readmenator_orchestrator.py:277`

### _commit_and_push (method) `def _commit_and_push(self, repo_dir, repo)`
- Defined: `readmenator_orchestrator.py:290`

### _cleanup_temp_dir (method) `def _cleanup_temp_dir(temp_dir)`
- Defined: `readmenator_orchestrator.py:336`

### __init__ (method) `def __init__(self, config)`
- Defined: `readmenator_orchestrator.py:342`

### run (method) `def run(self, dry_run, only_repo)`
- Defined: `readmenator_orchestrator.py:347`

### setUp (method) `def setUp(self)`
- Defined: `readmenator_orchestrator.py:397`

### tearDown (method) `def tearDown(self)`
- Defined: `readmenator_orchestrator.py:401`

### test_config_immutability (method) `def test_config_immutability(self)`
- Defined: `readmenator_orchestrator.py:404`

### test_config_defaults (method) `def test_config_defaults(self)`
- Defined: `readmenator_orchestrator.py:408`

### test_skip_repos_logic (method) `def test_skip_repos_logic(self)`
- Defined: `readmenator_orchestrator.py:415`

### test_repo_name_validation (method) `def test_repo_name_validation(self)`
- Defined: `readmenator_orchestrator.py:419`

### test_branch_name_validation (method) `def test_branch_name_validation(self)`
- Defined: `readmenator_orchestrator.py:429`

## tests/test_agent_injector.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_agent_injector.py:22`
- Depends on: `readmenator/_agent_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:27`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_agents_md_adds_kb_link (method) `def test_inject_into_agents_md_adds_kb_link(self)`
- Defined: `tests/test_agent_injector.py:30`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_claude_md_adds_kb_link (method) `def test_inject_into_claude_md_adds_kb_link(self)`
- Defined: `tests/test_agent_injector.py:39`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_cursorrules_adds_kb_link (method) `def test_inject_into_cursorrules_adds_kb_link(self)`
- Defined: `tests/test_agent_injector.py:49`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_github_copilot_instructions (method) `def test_inject_into_github_copilot_instructions(self)`
- Defined: `tests/test_agent_injector.py:57`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_replaces_old_injection_without_regen_command (method) `def test_inject_replaces_old_injection_without_regen_command(self)`
- Defined: `tests/test_agent_injector.py:67`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_skips_when_already_up_to_date (method) `def test_inject_skips_when_already_up_to_date(self)`
- Defined: `tests/test_agent_injector.py:82`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_cursor_rules_mdc_glob (method) `def test_inject_into_cursor_rules_mdc_glob(self)`
- Defined: `tests/test_agent_injector.py:96`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_is_idempotent_does_not_duplicate (method) `def test_inject_is_idempotent_does_not_duplicate(self)`
- Defined: `tests/test_agent_injector.py:106`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_no_agent_files_returns_zero (method) `def test_inject_no_agent_files_returns_zero(self)`
- Defined: `tests/test_agent_injector.py:117`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_preserves_existing_content (method) `def test_inject_preserves_existing_content(self)`
- Defined: `tests/test_agent_injector.py:121`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_multiple_agent_files (method) `def test_inject_multiple_agent_files(self)`
- Defined: `tests/test_agent_injector.py:129`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_plain_text_format_for_yaml (method) `def test_inject_plain_text_format_for_yaml(self)`
- Defined: `tests/test_agent_injector.py:136`
- Depends on: `readmenator/_agent_injector.py`

### test_custom_kb_filename_works (method) `def test_custom_kb_filename_works(self)`
- Defined: `tests/test_agent_injector.py:145`
- Depends on: `readmenator/_agent_injector.py`

### test_injection_includes_regeneration_command (method) `def test_injection_includes_regeneration_command(self)`
- Defined: `tests/test_agent_injector.py:153`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_does_not_execute_commands (method) `def test_inject_does_not_execute_commands(self)`
- Defined: `tests/test_agent_injector.py:160`
- Depends on: `readmenator/_agent_injector.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_agent_injector.py:171`
- Depends on: `readmenator/_agent_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:176`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_strips_injected_section (method) `def test_remove_strips_injected_section(self)`
- Defined: `tests/test_agent_injector.py:179`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_without_injection_returns_zero (method) `def test_remove_without_injection_returns_zero(self)`
- Defined: `tests/test_agent_injector.py:190`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_no_files_returns_zero (method) `def test_remove_no_files_returns_zero(self)`
- Defined: `tests/test_agent_injector.py:196`
- Depends on: `readmenator/_agent_injector.py`

### test_remove_preserves_original_content (method) `def test_remove_preserves_original_content(self)`
- Defined: `tests/test_agent_injector.py:200`
- Depends on: `readmenator/_agent_injector.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_agent_injector.py:214`
- Depends on: `readmenator/_agent_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:218`
- Depends on: `readmenator/_agent_injector.py`

### test_finds_agents_md (method) `def test_finds_agents_md(self)`
- Defined: `tests/test_agent_injector.py:221`
- Depends on: `readmenator/_agent_injector.py`

### test_finds_all_listed_files (method) `def test_finds_all_listed_files(self)`
- Defined: `tests/test_agent_injector.py:227`
- Depends on: `readmenator/_agent_injector.py`

### test_finds_cursor_rules_glob (method) `def test_finds_cursor_rules_glob(self)`
- Defined: `tests/test_agent_injector.py:234`
- Depends on: `readmenator/_agent_injector.py`

### test_returns_empty_when_no_files (method) `def test_returns_empty_when_no_files(self)`
- Defined: `tests/test_agent_injector.py:243`
- Depends on: `readmenator/_agent_injector.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_agent_injector.py:251`
- Depends on: `readmenator/_agent_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_agent_injector.py:256`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_into_empty_file (method) `def test_inject_into_empty_file(self)`
- Defined: `tests/test_agent_injector.py:259`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_respects_custom_agent_files_list (method) `def test_inject_respects_custom_agent_files_list(self)`
- Defined: `tests/test_agent_injector.py:267`
- Depends on: `readmenator/_agent_injector.py`

### test_inject_does_not_touch_unlisted_files (method) `def test_inject_does_not_touch_unlisted_files(self)`
- Defined: `tests/test_agent_injector.py:275`
- Depends on: `readmenator/_agent_injector.py`

## tests/test_agent_output.py

### _make_node (function) `def _make_node(node_id, symbols, doc, language)`
- Defined: `tests/test_agent_output.py:19`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### _make_edge (function) `def _make_edge(source, target, relation)`
- Defined: `tests/test_agent_output.py:30`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### _make_finding (function) `def _make_finding(file_path, line, severity, rule_id, description, snippet, cwe)`
- Defined: `tests/test_agent_output.py:34`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_config_defaults (method) `def test_config_defaults(self)`
- Defined: `tests/test_agent_output.py:50`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_config_immutable (method) `def test_config_immutable(self)`
- Defined: `tests/test_agent_output.py:56`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_inferred_from_directories (method) `def test_inferred_from_directories(self)`
- Defined: `tests/test_agent_output.py:64`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_flat_project_single_file (method) `def test_flat_project_single_file(self)`
- Defined: `tests/test_agent_output.py:80`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_min_threshold_respected (method) `def test_min_threshold_respected(self)`
- Defined: `tests/test_agent_output.py:91`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_misc_catches_unassigned (method) `def test_misc_catches_unassigned(self)`
- Defined: `tests/test_agent_output.py:103`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_index_lists_all_files (method) `def test_index_lists_all_files(self)`
- Defined: `tests/test_agent_output.py:118`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_index_table_format (method) `def test_index_table_format(self)`
- Defined: `tests/test_agent_output.py:133`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_empty_findings (method) `def test_empty_findings(self)`
- Defined: `tests/test_agent_output.py:144`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_findings_grouped_by_severity (method) `def test_findings_grouped_by_severity(self)`
- Defined: `tests/test_agent_output.py:150`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_findings_include_fix_hint_and_scope (method) `def test_findings_include_fix_hint_and_scope(self)`
- Defined: `tests/test_agent_output.py:166`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_no_json_wrapping (method) `def test_no_json_wrapping(self)`
- Defined: `tests/test_agent_output.py:181`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_god_nodes_section (method) `def test_god_nodes_section(self)`
- Defined: `tests/test_agent_output.py:191`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_cycles_section (method) `def test_cycles_section(self)`
- Defined: `tests/test_agent_output.py:207`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_empty_gotchas (method) `def test_empty_gotchas(self)`
- Defined: `tests/test_agent_output.py:224`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_cycle_loop_closed (method) `def test_cycle_loop_closed(self)`
- Defined: `tests/test_agent_output.py:230`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_internal_dependencies (method) `def test_internal_dependencies(self)`
- Defined: `tests/test_agent_output.py:247`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_external_imports (method) `def test_external_imports(self)`
- Defined: `tests/test_agent_output.py:258`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_functions_listed (method) `def test_functions_listed(self)`
- Defined: `tests/test_agent_output.py:269`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_no_json_in_api (method) `def test_no_json_in_api(self)`
- Defined: `tests/test_agent_output.py:283`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_subsystem_files_written (method) `def test_subsystem_files_written(self)`
- Defined: `tests/test_agent_output.py:295`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_recipes_directory (method) `def test_recipes_directory(self)`
- Defined: `tests/test_agent_output.py:317`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_recipes_grounded_in_actual_findings (method) `def test_recipes_grounded_in_actual_findings(self)`
- Defined: `tests/test_agent_output.py:330`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_generate_creates_all_files (method) `def test_generate_creates_all_files(self)`
- Defined: `tests/test_agent_output.py:363`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_all_files_under_500_lines (method) `def test_all_files_under_500_lines(self)`
- Defined: `tests/test_agent_output.py:394`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_no_json_in_any_output (method) `def test_no_json_in_any_output(self)`
- Defined: `tests/test_agent_output.py:409`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_manifest_workflow_orients_with_ls (method) `def test_manifest_workflow_orients_with_ls(self)`
- Defined: `tests/test_agent_output.py:421`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_agent_injector_detects_outdated (method) `def test_agent_injector_detects_outdated(self)`
- Defined: `tests/test_agent_output.py:435`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_agent_injector_skips_identical (method) `def test_agent_injector_skips_identical(self)`
- Defined: `tests/test_agent_output.py:457`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_readme_injector_detects_outdated (method) `def test_readme_injector_detects_outdated(self)`
- Defined: `tests/test_agent_output.py:473`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

### test_readme_injector_skips_identical (method) `def test_readme_injector_skips_identical(self)`
- Defined: `tests/test_agent_output.py:495`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_readme_injector.py`

## tests/test_analyzer.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_analyzer.py:19`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_analyzer.py:23`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### _make_edge (method) `def _make_edge(self, src, tgt, rel)`
- Defined: `tests/test_analyzer.py:26`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_empty_graph_returns_empty_result (method) `def test_analyze_empty_graph_returns_empty_result(self)`
- Defined: `tests/test_analyzer.py:29`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_detects_communities_for_connected_graph (method) `def test_analyze_detects_communities_for_connected_graph(self)`
- Defined: `tests/test_analyzer.py:34`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_computes_god_nodes (method) `def test_analyze_computes_god_nodes(self)`
- Defined: `tests/test_analyzer.py:48`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_finds_surprising_connections (method) `def test_analyze_finds_surprising_connections(self)`
- Defined: `tests/test_analyzer.py:64`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_generates_questions (method) `def test_analyze_generates_questions(self)`
- Defined: `tests/test_analyzer.py:81`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_community_cohesion_is_between_zero_and_one (method) `def test_community_cohesion_is_between_zero_and_one(self)`
- Defined: `tests/test_analyzer.py:92`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_isolated_nodes_do_not_form_communities (method) `def test_isolated_nodes_do_not_form_communities(self)`
- Defined: `tests/test_analyzer.py:107`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_with_resolved_edges_counts_them (method) `def test_analyze_with_resolved_edges_counts_them(self)`
- Defined: `tests/test_analyzer.py:116`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_analyze_is_repeatable (method) `def test_analyze_is_repeatable(self)`
- Defined: `tests/test_analyzer.py:130`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

### test_dominant_directory_prefers_specific_on_tie (method) `def test_dominant_directory_prefers_specific_on_tie(self)`
- Defined: `tests/test_analyzer.py:141`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`

## tests/test_cache.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_cache.py:21`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_cache.py:26`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### _write (method) `def _write(self, rel_path, content)`
- Defined: `tests/test_cache.py:30`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_compute_hash_returns_hex_string (method) `def test_compute_hash_returns_hex_string(self)`
- Defined: `tests/test_cache.py:36`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_different_content_produces_different_hash (method) `def test_different_content_produces_different_hash(self)`
- Defined: `tests/test_cache.py:42`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_same_content_produces_same_hash (method) `def test_same_content_produces_same_hash(self)`
- Defined: `tests/test_cache.py:49`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_load_returns_empty_dict_when_no_cache (method) `def test_load_returns_empty_dict_when_no_cache(self)`
- Defined: `tests/test_cache.py:56`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_save_and_load_roundtrip (method) `def test_save_and_load_roundtrip(self)`
- Defined: `tests/test_cache.py:60`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_find_changed_detects_new_files (method) `def test_find_changed_detects_new_files(self)`
- Defined: `tests/test_cache.py:66`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_find_changed_detects_modified_files (method) `def test_find_changed_detects_modified_files(self)`
- Defined: `tests/test_cache.py:71`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_find_changed_skips_unchanged_files (method) `def test_find_changed_skips_unchanged_files(self)`
- Defined: `tests/test_cache.py:78`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_prune_deleted_removes_ghost_entries (method) `def test_prune_deleted_removes_ghost_entries(self)`
- Defined: `tests/test_cache.py:85`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_compute_hashes_batch (method) `def test_compute_hashes_batch(self)`
- Defined: `tests/test_cache.py:92`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_nonexistent_file_returns_empty_hash (method) `def test_nonexistent_file_returns_empty_hash(self)`
- Defined: `tests/test_cache.py:100`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_save_and_load_analysis_roundtrip (method) `def test_save_and_load_analysis_roundtrip(self)`
- Defined: `tests/test_cache.py:109`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_load_missing_analysis_key_returns_none (method) `def test_load_missing_analysis_key_returns_none(self)`
- Defined: `tests/test_cache.py:116`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_clear_analysis_specific_key (method) `def test_clear_analysis_specific_key(self)`
- Defined: `tests/test_cache.py:120`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_clear_analysis_all_keys (method) `def test_clear_analysis_all_keys(self)`
- Defined: `tests/test_cache.py:127`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_has_changed_since_last_analysis_returns_true_on_first_run (method) `def test_has_changed_since_last_analysis_returns_true_on_first_run(self)`
- Defined: `tests/test_cache.py:134`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_has_changed_since_last_analysis_returns_false_when_no_changes (method) `def test_has_changed_since_last_analysis_returns_false_when_no_changes(self)`
- Defined: `tests/test_cache.py:139`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

### test_has_changed_since_last_analysis_returns_true_when_file_changed (method) `def test_has_changed_since_last_analysis_returns_true_when_file_changed(self)`
- Defined: `tests/test_cache.py:147`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`

## tests/test_config.py

### test_config_is_immutable (method) `def test_config_is_immutable(self)`
- Defined: `tests/test_config.py:8`
- Depends on: `readmenator/_config.py`

### test_config_defaults_are_sane (method) `def test_config_defaults_are_sane(self)`
- Defined: `tests/test_config.py:13`
- Depends on: `readmenator/_config.py`

### test_ignore_dirs_are_comprehensive (method) `def test_ignore_dirs_are_comprehensive(self)`
- Defined: `tests/test_config.py:24`
- Depends on: `readmenator/_config.py`

### test_plural_map_covers_all_symbol_types (method) `def test_plural_map_covers_all_symbol_types(self)`
- Defined: `tests/test_config.py:30`
- Depends on: `readmenator/_config.py`

### test_supported_extensions_no_duplicates (method) `def test_supported_extensions_no_duplicates(self)`
- Defined: `tests/test_config.py:41`
- Depends on: `readmenator/_config.py`

## tests/test_cpg.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_cpg.py:14`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_cpg.py:18`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### _make_sym (method) `def _make_sym(self, name, kind, line)`
- Defined: `tests/test_cpg.py:21`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_returns_valid_json (method) `def test_generate_returns_valid_json(self)`
- Defined: `tests/test_cpg.py:24`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_includes_node_data (method) `def test_generate_includes_node_data(self)`
- Defined: `tests/test_cpg.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_includes_edges (method) `def test_generate_includes_edges(self)`
- Defined: `tests/test_cpg.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_generate_includes_metadata (method) `def test_generate_includes_metadata(self)`
- Defined: `tests/test_cpg.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_privacy_mode_strips_docs (method) `def test_privacy_mode_strips_docs(self)`
- Defined: `tests/test_cpg.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_sha256_hash_included (method) `def test_sha256_hash_included(self)`
- Defined: `tests/test_cpg.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

### test_empty_graph_returns_valid_json (method) `def test_empty_graph_returns_valid_json(self)`
- Defined: `tests/test_cpg.py:96`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_models.py`

## tests/test_cursorrules.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_cursorrules.py:21`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_returns_string (method) `def test_generate_returns_string(self)`
- Defined: `tests/test_cursorrules.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_contains_header (method) `def test_generate_contains_header(self)`
- Defined: `tests/test_cursorrules.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_contains_base_rules (method) `def test_generate_contains_base_rules(self)`
- Defined: `tests/test_cursorrules.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_layer_constraints (method) `def test_generate_includes_layer_constraints(self)`
- Defined: `tests/test_cursorrules.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_god_nodes (method) `def test_generate_includes_god_nodes(self)`
- Defined: `tests/test_cursorrules.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_communities (method) `def test_generate_includes_communities(self)`
- Defined: `tests/test_cursorrules.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_includes_violations (method) `def test_generate_includes_violations(self)`
- Defined: `tests/test_cursorrules.py:82`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_limits_violations_to_ten (method) `def test_generate_limits_violations_to_ten(self)`
- Defined: `tests/test_cursorrules.py:95`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_writes_file_when_project_root (method) `def test_generate_writes_file_when_project_root(self)`
- Defined: `tests/test_cursorrules.py:103`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

### test_generate_idempotent (method) `def test_generate_idempotent(self)`
- Defined: `tests/test_cursorrules.py:111`
- Depends on: `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_models.py`

## tests/test_dataflow.py

### _node (function) `def _node(node_id, funcs)`
- Defined: `tests/test_dataflow.py:8`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### _analyze (function) `def _analyze(body)`
- Defined: `tests/test_dataflow.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_config_defaults (method) `def test_config_defaults(self)`
- Defined: `tests/test_dataflow.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_config_immutable (method) `def test_config_immutable(self)`
- Defined: `tests/test_dataflow.py:31`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_uninit_use_detected (method) `def test_uninit_use_detected(self)`
- Defined: `tests/test_dataflow.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_initialized_use_clean (method) `def test_initialized_use_clean(self)`
- Defined: `tests/test_dataflow.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_params_count_as_initialized (method) `def test_params_count_as_initialized(self)`
- Defined: `tests/test_dataflow.py:50`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_scanf_addr_counts_as_init (method) `def test_scanf_addr_counts_as_init(self)`
- Defined: `tests/test_dataflow.py:58`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_dead_store_detected (method) `def test_dead_store_detected(self)`
- Defined: `tests/test_dataflow.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_read_store_clean (method) `def test_read_store_clean(self)`
- Defined: `tests/test_dataflow.py:67`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_unchecked_alloc_detected (method) `def test_unchecked_alloc_detected(self)`
- Defined: `tests/test_dataflow.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_checked_alloc_clean (method) `def test_checked_alloc_clean(self)`
- Defined: `tests/test_dataflow.py:78`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_disabled_returns_empty (method) `def test_disabled_returns_empty(self)`
- Defined: `tests/test_dataflow.py:84`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_missing_content_skipped (method) `def test_missing_content_skipped(self)`
- Defined: `tests/test_dataflow.py:91`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_issue_cap_respected (method) `def test_issue_cap_respected(self)`
- Defined: `tests/test_dataflow.py:96`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_plain_assignment_is_not_a_declaration (method) `def test_plain_assignment_is_not_a_declaration(self)`
- Defined: `tests/test_dataflow.py:105`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_subscript_store_counts_as_init (method) `def test_subscript_store_counts_as_init(self)`
- Defined: `tests/test_dataflow.py:110`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_asm_output_counts_as_init (method) `def test_asm_output_counts_as_init(self)`
- Defined: `tests/test_dataflow.py:116`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_fd_lt_zero_counts_as_checked (method) `def test_fd_lt_zero_counts_as_checked(self)`
- Defined: `tests/test_dataflow.py:123`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_map_failed_counts_as_checked (method) `def test_map_failed_counts_as_checked(self)`
- Defined: `tests/test_dataflow.py:129`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_member_null_check_counts (method) `def test_member_null_check_counts(self)`
- Defined: `tests/test_dataflow.py:136`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_loop_carried_var_not_dead (method) `def test_loop_carried_var_not_dead(self)`
- Defined: `tests/test_dataflow.py:144`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_line_numbers_survive_subscript_stores (method) `def test_line_numbers_survive_subscript_stores(self)`
- Defined: `tests/test_dataflow.py:156`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_member_store_not_local_assign (method) `def test_member_store_not_local_assign(self)`
- Defined: `tests/test_dataflow.py:167`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_array_arg_to_filler_counts_as_init (method) `def test_array_arg_to_filler_counts_as_init(self)`
- Defined: `tests/test_dataflow.py:173`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_array_arg_to_readonly_still_uninit (method) `def test_array_arg_to_readonly_still_uninit(self)`
- Defined: `tests/test_dataflow.py:181`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_array_filled_in_decl_init_call (method) `def test_array_filled_in_decl_init_call(self)`
- Defined: `tests/test_dataflow.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_static_never_uninit (method) `def test_static_never_uninit(self)`
- Defined: `tests/test_dataflow.py:196`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_derived_pointer_not_dead (method) `def test_derived_pointer_not_dead(self)`
- Defined: `tests/test_dataflow.py:203`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_sizeof_is_not_a_read (method) `def test_sizeof_is_not_a_read(self)`
- Defined: `tests/test_dataflow.py:216`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_block_comment_malloc_ignored (method) `def test_block_comment_malloc_ignored(self)`
- Defined: `tests/test_dataflow.py:225`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_address_alias_pointer_not_dead (method) `def test_address_alias_pointer_not_dead(self)`
- Defined: `tests/test_dataflow.py:234`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_array_store_before_read_suppresses_uninit (method) `def test_array_store_before_read_suppresses_uninit(self)`
- Defined: `tests/test_dataflow.py:248`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_same_line_use_not_dead (method) `def test_same_line_use_not_dead(self)`
- Defined: `tests/test_dataflow.py:256`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_same_line_only_assign_is_dead (method) `def test_same_line_only_assign_is_dead(self)`
- Defined: `tests/test_dataflow.py:264`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_alias_pointer_store_initializes_array (method) `def test_alias_pointer_store_initializes_array(self)`
- Defined: `tests/test_dataflow.py:272`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_inline_alias_fill_suppresses_uninit (method) `def test_inline_alias_fill_suppresses_uninit(self)`
- Defined: `tests/test_dataflow.py:281`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_function_pointer_call_counts_as_use (method) `def test_function_pointer_call_counts_as_use(self)`
- Defined: `tests/test_dataflow.py:290`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_plain_call_is_not_a_local_use (method) `def test_plain_call_is_not_a_local_use(self)`
- Defined: `tests/test_dataflow.py:298`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_local_struct_does_not_truncate_span (method) `def test_local_struct_does_not_truncate_span(self)`
- Defined: `tests/test_dataflow.py:305`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_file_scope_symbol_still_bounds_span (method) `def test_file_scope_symbol_still_bounds_span(self)`
- Defined: `tests/test_dataflow.py:329`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_url_string_does_not_truncate_line (method) `def test_url_string_does_not_truncate_line(self)`
- Defined: `tests/test_dataflow.py:344`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_assert_macro_counts_as_null_check (method) `def test_assert_macro_counts_as_null_check(self)`
- Defined: `tests/test_dataflow.py:352`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_multiline_call_assigns_array_arg (method) `def test_multiline_call_assigns_array_arg(self)`
- Defined: `tests/test_dataflow.py:360`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_address_taken_suppresses_dead_store (method) `def test_address_taken_suppresses_dead_store(self)`
- Defined: `tests/test_dataflow.py:369`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

### test_member_store_initializes_base (method) `def test_member_store_initializes_base(self)`
- Defined: `tests/test_dataflow.py:377`
- Depends on: `readmenator/_config.py`, `readmenator/_dataflow.py`, `readmenator/_models.py`

## tests/test_dead_code.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_dead_code.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### _make_symbol (method) `def _make_symbol(self, name, kind)`
- Defined: `tests/test_dead_code.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, symbols)`
- Defined: `tests/test_dead_code.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### _make_edge (method) `def _make_edge(self, src, tgt)`
- Defined: `tests/test_dead_code.py:35`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_empty_graph_returns_empty (method) `def test_identify_empty_graph_returns_empty(self)`
- Defined: `tests/test_dead_code.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_finds_dead_symbol (method) `def test_identify_finds_dead_symbol(self)`
- Defined: `tests/test_dead_code.py:42`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_excludes_entry_points (method) `def test_identify_excludes_entry_points(self)`
- Defined: `tests/test_dead_code.py:53`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_excludes_app_entry_point (method) `def test_identify_excludes_app_entry_point(self)`
- Defined: `tests/test_dead_code.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_excludes_init_entry_point (method) `def test_identify_excludes_init_entry_point(self)`
- Defined: `tests/test_dead_code.py:69`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_recommends_review_for_classes (method) `def test_identify_recommends_review_for_classes(self)`
- Defined: `tests/test_dead_code.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_recommends_trash_for_functions (method) `def test_identify_recommends_trash_for_functions(self)`
- Defined: `tests/test_dead_code.py:85`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_identify_recommends_trash_for_variables (method) `def test_identify_recommends_trash_for_variables(self)`
- Defined: `tests/test_dead_code.py:93`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_all_symbols_imported_returns_empty (method) `def test_all_symbols_imported_returns_empty(self)`
- Defined: `tests/test_dead_code.py:101`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

### test_reports_sorted_by_file_path (method) `def test_reports_sorted_by_file_path(self)`
- Defined: `tests/test_dead_code.py:113`
- Depends on: `readmenator/_config.py`, `readmenator/_dead_code.py`, `readmenator/_models.py`

## tests/test_diagrams.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_diagrams.py:33`
- Doc: Initialise builder with default configuration.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### _make_graph (method) `def _make_graph(self)`
- Defined: `tests/test_diagrams.py:38`
- Doc: Create a small deterministic project graph.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_supports_five_kinds (method) `def test_builder_supports_five_kinds(self)`
- Defined: `tests/test_diagrams.py:52`
- Doc: Builder exposes architecture, workflow, sequence, dataflow, lifecycle.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_produces_all_kinds (method) `def test_builder_produces_all_kinds(self)`
- Defined: `tests/test_diagrams.py:59`
- Doc: Build all returns one map per supported kind.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_is_deterministic (method) `def test_builder_is_deterministic(self)`
- Defined: `tests/test_diagrams.py:68`
- Doc: Two builds over identical input share coordinates and bytes.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_orders_links_deterministically (method) `def test_builder_orders_links_deterministically(self)`
- Defined: `tests/test_diagrams.py:80`
- Doc: Shuffled input edges yield identical ordered map relationships.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_validates_large_graph_for_all_kinds (method) `def test_builder_validates_large_graph_for_all_kinds(self)`
- Defined: `tests/test_diagrams.py:101`
- Doc: Large layered graphs validate for every diagram kind.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_reports_total_scope (method) `def test_builder_reports_total_scope(self)`
- Defined: `tests/test_diagrams.py:119`
- Doc: Built maps record shown scope and total input file count.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_attaches_symbols_and_docs (method) `def test_builder_attaches_symbols_and_docs(self)`
- Defined: `tests/test_diagrams.py:126`
- Doc: Map nodes carry symbol records, file docs, and language.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_truncates_symbols_per_node (method) `def test_builder_truncates_symbols_per_node(self)`
- Defined: `tests/test_diagrams.py:143`
- Doc: Symbol records respect the per-node configured cap.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_builder_truncates_to_configured_limit (method) `def test_builder_truncates_to_configured_limit(self)`
- Defined: `tests/test_diagrams.py:152`
- Doc: Oversized graphs are truncated to the configured node limit.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_compare_reports_added_removed_rerouted (method) `def test_compare_reports_added_removed_rerouted(self)`
- Defined: `tests/test_diagrams.py:162`
- Doc: Delta comparison reports added, removed, and rerouted facts.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_diagrams.py:179`
- Doc: Initialise validator with default configuration.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### _valid_map (method) `def _valid_map(self)`
- Defined: `tests/test_diagrams.py:184`
- Doc: Create a minimal valid architecture map.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_validator_passes_valid_map (method) `def test_validator_passes_valid_map(self)`
- Defined: `tests/test_diagrams.py:197`
- Doc: Valid maps pass with the full check list and zero errors.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_validator_rejects_duplicate_node_ids (method) `def test_validator_rejects_duplicate_node_ids(self)`
- Defined: `tests/test_diagrams.py:204`
- Doc: Duplicate identifiers fail with rule D001.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_validator_rejects_dangling_edge (method) `def test_validator_rejects_dangling_edge(self)`
- Defined: `tests/test_diagrams.py:214`
- Doc: Edges pointing at unknown nodes fail with rule D002.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_validator_rejects_empty_map (method) `def test_validator_rejects_empty_map(self)`
- Defined: `tests/test_diagrams.py:222`
- Doc: Maps without nodes fail with rule D003.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_validator_rejects_unknown_kind (method) `def test_validator_rejects_unknown_kind(self)`
- Defined: `tests/test_diagrams.py:228`
- Doc: Unknown diagram kinds fail with rule D000.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_diagrams.py:240`
- Doc: Initialise builder and renderer with default configuration.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### _map (method) `def _map(self, kind)`
- Defined: `tests/test_diagrams.py:246`
- Doc: Build a small map of the requested kind.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_produces_standalone_document (method) `def test_renderer_produces_standalone_document(self)`
- Defined: `tests/test_diagrams.py:256`
- Doc: Output is a complete HTML document with inline SVG.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_has_no_external_requests (method) `def test_renderer_has_no_external_requests(self)`
- Defined: `tests/test_diagrams.py:263`
- Doc: Output performs no external fetches or CDN references.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_includes_interaction_controls (method) `def test_renderer_includes_interaction_controls(self)`
- Defined: `tests/test_diagrams.py:270`
- Doc: Output includes search, passport, reach, route, lens, views, export.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_includes_keyboard_and_deep_links (method) `def test_renderer_includes_keyboard_and_deep_links(self)`
- Defined: `tests/test_diagrams.py:276`
- Doc: Output documents shortcuts and hash deep link contracts.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_escapes_malicious_labels (method) `def test_renderer_escapes_malicious_labels(self)`
- Defined: `tests/test_diagrams.py:285`
- Doc: Malicious labels are escaped and never break the document.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_embeds_valid_json_payloads (method) `def test_renderer_embeds_valid_json_payloads(self)`
- Defined: `tests/test_diagrams.py:298`
- Doc: Embedded payload scripts parse as valid JSON arrays.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_covers_all_five_kinds (method) `def test_renderer_covers_all_five_kinds(self)`
- Defined: `tests/test_diagrams.py:307`
- Doc: Every diagram kind renders a standalone document.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_links_gallery_home_when_configured (method) `def test_renderer_links_gallery_home_when_configured(self)`
- Defined: `tests/test_diagrams.py:314`
- Doc: Maps with a home target expose a gallery back link.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_omits_gallery_home_by_default (method) `def test_renderer_omits_gallery_home_by_default(self)`
- Defined: `tests/test_diagrams.py:321`
- Doc: Maps without a home target expose no gallery link.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_keeps_canvas_distinct_from_nodes (method) `def test_renderer_keeps_canvas_distinct_from_nodes(self)`
- Defined: `tests/test_diagrams.py:326`
- Doc: Canvas background differs from node fill for readability.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_supports_drag_and_settle (method) `def test_renderer_supports_drag_and_settle(self)`
- Defined: `tests/test_diagrams.py:334`
- Doc: Nodes are draggable with pointer capture plus a force pass.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_sanitizes_viewer_state_on_export (method) `def test_renderer_sanitizes_viewer_state_on_export(self)`
- Defined: `tests/test_diagrams.py:342`
- Doc: Exports drop temporary focus, dim, and drag classes.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_buttons_explain_their_purpose (method) `def test_renderer_buttons_explain_their_purpose(self)`
- Defined: `tests/test_diagrams.py:348`
- Doc: Every toolbar action carries a human-readable title.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_diagrams.py:363`
- Doc: Initialise builder and publisher with default configuration.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### _maps (method) `def _maps(self)`
- Defined: `tests/test_diagrams.py:369`
- Doc: Build all five maps from a small deterministic graph.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_writes_index_plus_five_maps (method) `def test_publish_writes_index_plus_five_maps(self)`
- Defined: `tests/test_diagrams.py:379`
- Doc: Publish creates an index, five map files, and a nojekyll marker.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_index_links_every_map (method) `def test_publish_index_links_every_map(self)`
- Defined: `tests/test_diagrams.py:390`
- Doc: Gallery index links every published map with relative paths.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_output_has_no_external_requests (method) `def test_publish_output_has_no_external_requests(self)`
- Defined: `tests/test_diagrams.py:399`
- Doc: Index and maps perform no external fetches or CDN references.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_is_deterministic (method) `def test_publish_is_deterministic(self)`
- Defined: `tests/test_diagrams.py:412`
- Doc: Two publishes over identical input share index bytes.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_escapes_malicious_project_name (method) `def test_publish_escapes_malicious_project_name(self)`
- Defined: `tests/test_diagrams.py:423`
- Doc: Malicious project names are escaped in the gallery index.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_escapes_malicious_stat_keys (method) `def test_publish_escapes_malicious_stat_keys(self)`
- Defined: `tests/test_diagrams.py:432`
- Doc: Malicious statistics keys are escaped in the gallery index.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_skips_invalid_maps (method) `def test_publish_skips_invalid_maps(self)`
- Defined: `tests/test_diagrams.py:443`
- Doc: Maps failing validation are skipped while the index is written.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_empty_maps_writes_empty_gallery (method) `def test_publish_empty_maps_writes_empty_gallery(self)`
- Defined: `tests/test_diagrams.py:455`
- Doc: Empty input writes an index with an empty gallery notice.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_leaves_input_maps_unmodified (method) `def test_publish_leaves_input_maps_unmodified(self)`
- Defined: `tests/test_diagrams.py:464`
- Doc: Publish never mutates the caller supplied map metadata.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_flat_subdir_keeps_links_relative (method) `def test_publish_flat_subdir_keeps_links_relative(self)`
- Defined: `tests/test_diagrams.py:473`
- Doc: Flat layouts link maps beside the index with a local home.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_index_explains_how_to_read (method) `def test_publish_index_explains_how_to_read(self)`
- Defined: `tests/test_diagrams.py:486`
- Doc: Gallery index documents the reader interactions.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_publish_card_reports_primary_scope (method) `def test_publish_card_reports_primary_scope(self)`
- Defined: `tests/test_diagrams.py:494`
- Doc: Gallery cards state shown files against the project total.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_diagrams.py:506`
- Doc: Initialise builder and renderer with default configuration.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### _map (method) `def _map(self, kind)`
- Defined: `tests/test_diagrams.py:512`
- Doc: Build a small map of the requested kind.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_uses_configured_cdn_urls (method) `def test_renderer_uses_configured_cdn_urls(self)`
- Defined: `tests/test_diagrams.py:522`
- Doc: Script and style tags come from Config, never hardcoded.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_builds_vis_network_with_physics (method) `def test_renderer_builds_vis_network_with_physics(self)`
- Defined: `tests/test_diagrams.py:535`
- Doc: Output instantiates a vis network with physics enabled.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_links_gallery_home_when_configured (method) `def test_renderer_links_gallery_home_when_configured(self)`
- Defined: `tests/test_diagrams.py:543`
- Doc: Vis maps with a home target expose a gallery back link.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_disables_physics_from_config (method) `def test_renderer_disables_physics_from_config(self)`
- Defined: `tests/test_diagrams.py:551`
- Doc: Physics honors the configured enabled flag.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_escapes_malicious_titles (method) `def test_renderer_escapes_malicious_titles(self)`
- Defined: `tests/test_diagrams.py:558`
- Doc: Malicious labels never break tooltips or markup.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_exposes_reader_controls (method) `def test_renderer_exposes_reader_controls(self)`
- Defined: `tests/test_diagrams.py:571`
- Doc: Output carries search, reach, route, lens, chapters, export.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_is_deterministic (method) `def test_renderer_is_deterministic(self)`
- Defined: `tests/test_diagrams.py:577`
- Doc: Two renders over identical input share bytes.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_embeds_valid_payloads (method) `def test_renderer_embeds_valid_payloads(self)`
- Defined: `tests/test_diagrams.py:582`
- Doc: Embedded node and edge payloads parse as valid JSON.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_documents_symbols_per_file (method) `def test_renderer_documents_symbols_per_file(self)`
- Defined: `tests/test_diagrams.py:590`
- Doc: Node payloads and tooltips expose symbols with signatures.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_renderer_escapes_malicious_symbol_docs (method) `def test_renderer_escapes_malicious_symbol_docs(self)`
- Defined: `tests/test_diagrams.py:606`
- Doc: Malicious symbol documentation never breaks tooltips.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### _project (method) `def _project(self, tmp)`
- Defined: `tests/test_diagrams.py:622`
- Doc: Create a two-file project in a temporary directory.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_export_diagrams_writes_vis_maps_by_default (method) `def test_export_diagrams_writes_vis_maps_by_default(self)`
- Defined: `tests/test_diagrams.py:627`
- Doc: Default diagram export writes CDN-powered vis.js maps.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

### test_export_diagrams_falls_back_offline_when_disabled (method) `def test_export_diagrams_falls_back_offline_when_disabled(self)`
- Defined: `tests/test_diagrams.py:641`
- Doc: Disabled vis flag produces offline maps without CDN.
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_diagrams.py`, `readmenator/_models.py`

## tests/test_documentation.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_documentation.py:18`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_header (method) `def test_contains_header(self)`
- Defined: `tests/test_documentation.py:22`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_metadata_line (method) `def test_contains_metadata_line(self)`
- Defined: `tests/test_documentation.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_mermaid_block (method) `def test_contains_mermaid_block(self)`
- Defined: `tests/test_documentation.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_architecture_reference (method) `def test_contains_architecture_reference(self)`
- Defined: `tests/test_documentation.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_cpg_block (method) `def test_contains_cpg_block(self)`
- Defined: `tests/test_documentation.py:41`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_contains_statistics_dashboard (method) `def test_contains_statistics_dashboard(self)`
- Defined: `tests/test_documentation.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_groups_files_by_language (method) `def test_groups_files_by_language(self)`
- Defined: `tests/test_documentation.py:51`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_lists_symbols_under_file (method) `def test_lists_symbols_under_file(self)`
- Defined: `tests/test_documentation.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_class_symbol_is_pluralized_correctly (method) `def test_class_symbol_is_pluralized_correctly(self)`
- Defined: `tests/test_documentation.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_function_pluralization (method) `def test_function_pluralization(self)`
- Defined: `tests/test_documentation.py:97`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_method_pluralization (method) `def test_method_pluralization(self)`
- Defined: `tests/test_documentation.py:109`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_shows_no_symbols_for_empty_files (method) `def test_shows_no_symbols_for_empty_files(self)`
- Defined: `tests/test_documentation.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_includes_file_path (method) `def test_includes_file_path(self)`
- Defined: `tests/test_documentation.py:132`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_docstring_in_output (method) `def test_docstring_in_output(self)`
- Defined: `tests/test_documentation.py:143`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_truncation_note_when_limited (method) `def test_truncation_note_when_limited(self)`
- Defined: `tests/test_documentation.py:155`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_taint_propagation_section_present (method) `def test_taint_propagation_section_present(self)`
- Defined: `tests/test_documentation.py:165`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_hotspot_section_present (method) `def test_hotspot_section_present(self)`
- Defined: `tests/test_documentation.py:185`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_no_taint_section_when_empty (method) `def test_no_taint_section_when_empty(self)`
- Defined: `tests/test_documentation.py:203`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_no_hotspot_section_when_empty (method) `def test_no_hotspot_section_when_empty(self)`
- Defined: `tests/test_documentation.py:207`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_cpg_block_disabled_via_config (method) `def test_cpg_block_disabled_via_config(self)`
- Defined: `tests/test_documentation.py:211`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_architectural_layers_section (method) `def test_architectural_layers_section(self)`
- Defined: `tests/test_documentation.py:217`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_security_findings_section (method) `def test_security_findings_section(self)`
- Defined: `tests/test_documentation.py:229`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_zero_returns_full_content (method) `def test_context_budget_zero_returns_full_content(self)`
- Defined: `tests/test_documentation.py:252`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_returns_compact_summary (method) `def test_context_budget_returns_compact_summary(self)`
- Defined: `tests/test_documentation.py:260`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_prioritizes_god_nodes (method) `def test_context_budget_prioritizes_god_nodes(self)`
- Defined: `tests/test_documentation.py:268`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_truncates_at_limit (method) `def test_context_budget_truncates_at_limit(self)`
- Defined: `tests/test_documentation.py:285`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

### test_context_budget_includes_security_findings (method) `def test_context_budget_includes_security_findings(self)`
- Defined: `tests/test_documentation.py:293`
- Depends on: `readmenator/_config.py`, `readmenator/_documentation.py`, `readmenator/_models.py`

## tests/test_exporter.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_exporter.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, label, lang, symbols)`
- Defined: `tests/test_exporter.py:30`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### _make_sym (method) `def _make_sym(self, name, kind, line)`
- Defined: `tests/test_exporter.py:42`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_produces_valid_json (method) `def test_to_json_produces_valid_json(self)`
- Defined: `tests/test_exporter.py:47`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_includes_symbol_data (method) `def test_to_json_includes_symbol_data(self)`
- Defined: `tests/test_exporter.py:56`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_includes_metadata (method) `def test_to_json_includes_metadata(self)`
- Defined: `tests/test_exporter.py:65`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_includes_analysis_metadata (method) `def test_to_json_includes_analysis_metadata(self)`
- Defined: `tests/test_exporter.py:76`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_html_produces_standalone_page (method) `def test_to_html_produces_standalone_page(self)`
- Defined: `tests/test_exporter.py:101`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_html_includes_node_data (method) `def test_to_html_includes_node_data(self)`
- Defined: `tests/test_exporter.py:109`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_html_includes_community_legend_when_analysis (method) `def test_to_html_includes_community_legend_when_analysis(self)`
- Defined: `tests/test_exporter.py:116`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_svg_produces_svg_string (method) `def test_to_svg_produces_svg_string(self)`
- Defined: `tests/test_exporter.py:138`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_svg_render_truncation_for_large_graph (method) `def test_to_svg_render_truncation_for_large_graph(self)`
- Defined: `tests/test_exporter.py:145`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_svg_includes_readmenator_title (method) `def test_to_svg_includes_readmenator_title(self)`
- Defined: `tests/test_exporter.py:154`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

### test_to_json_handles_resolved_edges (method) `def test_to_json_handles_resolved_edges(self)`
- Defined: `tests/test_exporter.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_exporter.py`, `readmenator/_models.py`

## tests/test_hotspots.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_hotspots.py:13`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, label, sym_count)`
- Defined: `tests/test_hotspots.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_empty_graph_returns_empty_hotspots (method) `def test_empty_graph_returns_empty_hotspots(self)`
- Defined: `tests/test_hotspots.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_hotspots_rank_by_combined_score (method) `def test_hotspots_rank_by_combined_score(self)`
- Defined: `tests/test_hotspots.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_hotspot_includes_scores (method) `def test_hotspot_includes_scores(self)`
- Defined: `tests/test_hotspots.py:43`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_no_cycles_in_acyclic_graph (method) `def test_no_cycles_in_acyclic_graph(self)`
- Defined: `tests/test_hotspots.py:53`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_detects_simple_cycle (method) `def test_detects_simple_cycle(self)`
- Defined: `tests/test_hotspots.py:66`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_change_impact_ranks_by_total_impact (method) `def test_change_impact_ranks_by_total_impact(self)`
- Defined: `tests/test_hotspots.py:79`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_change_impact_no_edges (method) `def test_change_impact_no_edges(self)`
- Defined: `tests/test_hotspots.py:94`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

### test_hotspot_weights_from_config (method) `def test_hotspot_weights_from_config(self)`
- Defined: `tests/test_hotspots.py:100`
- Depends on: `readmenator/_config.py`, `readmenator/_hotspots.py`, `readmenator/_models.py`

## tests/test_integration.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_integration.py:10`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_integration.py:15`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### _write (method) `def _write(self, path, content)`
- Defined: `tests/test_integration.py:19`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_full_pipeline_generates_knowledge_base (method) `def test_full_pipeline_generates_knowledge_base(self)`
- Defined: `tests/test_integration.py:24`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_knowledge_base_contains_mermaid (method) `def test_knowledge_base_contains_mermaid(self)`
- Defined: `tests/test_integration.py:40`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_query_subcommand_works (method) `def test_query_subcommand_works(self)`
- Defined: `tests/test_integration.py:48`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_explain_subcommand_works (method) `def test_explain_subcommand_works(self)`
- Defined: `tests/test_integration.py:53`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_path_subcommand_works (method) `def test_path_subcommand_works(self)`
- Defined: `tests/test_integration.py:59`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_summary_works (method) `def test_summary_works(self)`
- Defined: `tests/test_integration.py:65`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_rebuild (method) `def test_rebuild(self)`
- Defined: `tests/test_integration.py:71`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_knowledge_base_contains_cpg (method) `def test_knowledge_base_contains_cpg(self)`
- Defined: `tests/test_integration.py:81`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_knowledge_base_contains_statistics_dashboard (method) `def test_knowledge_base_contains_statistics_dashboard(self)`
- Defined: `tests/test_integration.py:89`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_audit_deep_returns_analysis (method) `def test_audit_deep_returns_analysis(self)`
- Defined: `tests/test_integration.py:98`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_privacy_mode_works (method) `def test_privacy_mode_works(self)`
- Defined: `tests/test_integration.py:105`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

### test_export_sarif_produces_file (method) `def test_export_sarif_produces_file(self)`
- Defined: `tests/test_integration.py:114`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`

## tests/test_layer_rules.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_layer_rules.py:13`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, label)`
- Defined: `tests/test_layer_rules.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_empty_graph_returns_empty_violations (method) `def test_empty_graph_returns_empty_violations(self)`
- Defined: `tests/test_layer_rules.py:20`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_no_layers_returns_empty_violations (method) `def test_no_layers_returns_empty_violations(self)`
- Defined: `tests/test_layer_rules.py:24`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_same_layer_no_violation (method) `def test_same_layer_no_violation(self)`
- Defined: `tests/test_layer_rules.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_forbidden_edge_detected (method) `def test_forbidden_edge_detected(self)`
- Defined: `tests/test_layer_rules.py:36`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_allowed_testing_edges_no_violation (method) `def test_allowed_testing_edges_no_violation(self)`
- Defined: `tests/test_layer_rules.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_multiple_violations (method) `def test_multiple_violations(self)`
- Defined: `tests/test_layer_rules.py:57`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_utility_layer_ignored (method) `def test_utility_layer_ignored(self)`
- Defined: `tests/test_layer_rules.py:75`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_violation_summary (method) `def test_violation_summary(self)`
- Defined: `tests/test_layer_rules.py:82`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_resolved_edges_also_checked (method) `def test_resolved_edges_also_checked(self)`
- Defined: `tests/test_layer_rules.py:104`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

### test_presentation_to_data_access_forbidden (method) `def test_presentation_to_data_access_forbidden(self)`
- Defined: `tests/test_layer_rules.py:115`
- Depends on: `readmenator/_config.py`, `readmenator/_layer_rules.py`, `readmenator/_models.py`

## tests/test_linter.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_linter.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### _make_node (method) `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_linter.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### _make_edge (method) `def _make_edge(self, src, tgt, rel)`
- Defined: `tests/test_linter.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_empty_graph_returns_no_violations (method) `def test_lint_empty_graph_returns_no_violations(self)`
- Defined: `tests/test_linter.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_returns_empty_for_files_under_threshold (method) `def test_lint_returns_empty_for_files_under_threshold(self)`
- Defined: `tests/test_linter.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_detects_file_exceeding_max_lines (method) `def test_lint_detects_file_exceeding_max_lines(self)`
- Defined: `tests/test_linter.py:40`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_detects_cross_layer_violation (method) `def test_lint_detects_cross_layer_violation(self)`
- Defined: `tests/test_linter.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_allows_same_layer_imports (method) `def test_lint_allows_same_layer_imports(self)`
- Defined: `tests/test_linter.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_allows_testing_to_business_logic (method) `def test_lint_allows_testing_to_business_logic(self)`
- Defined: `tests/test_linter.py:72`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_ignores_utility_layer (method) `def test_lint_ignores_utility_layer(self)`
- Defined: `tests/test_linter.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_detects_circular_dependencies (method) `def test_lint_detects_circular_dependencies(self)`
- Defined: `tests/test_linter.py:94`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_violations_sorted_by_severity (method) `def test_violations_sorted_by_severity(self)`
- Defined: `tests/test_linter.py:108`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

### test_lint_returns_empty_when_disabled (method) `def test_lint_returns_empty_when_disabled(self)`
- Defined: `tests/test_linter.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_linter.py`, `readmenator/_models.py`

## tests/test_mcp_server.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_mcp_server.py:24`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_mcp_server.py:33`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### _make_request (method) `def _make_request(self, method, params, msg_id)`
- Defined: `tests/test_mcp_server.py:36`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### _call (method) `def _call(self, req)`
- Defined: `tests/test_mcp_server.py:42`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_initialize_exchanges_protocol_version (method) `def test_initialize_exchanges_protocol_version(self)`
- Defined: `tests/test_mcp_server.py:49`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_notifications_initialized_returns_no_response (method) `def test_notifications_initialized_returns_no_response(self)`
- Defined: `tests/test_mcp_server.py:62`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_unknown_method_returns_error (method) `def test_unknown_method_returns_error(self)`
- Defined: `tests/test_mcp_server.py:67`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_uninitialized_request_returns_error (method) `def test_uninitialized_request_returns_error(self)`
- Defined: `tests/test_mcp_server.py:75`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_list_tools_returns_all_tool_definitions (method) `def test_list_tools_returns_all_tool_definitions(self)`
- Defined: `tests/test_mcp_server.py:85`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_tool_without_initialize_returns_error (method) `def test_call_tool_without_initialize_returns_error(self)`
- Defined: `tests/test_mcp_server.py:115`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_tool_unknown_tool_returns_method_not_found (method) `def test_call_tool_unknown_tool_returns_method_not_found(self)`
- Defined: `tests/test_mcp_server.py:123`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_summary_tool_returns_content (method) `def test_call_summary_tool_returns_content(self)`
- Defined: `tests/test_mcp_server.py:132`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_query_tool_with_text_returns_results (method) `def test_call_query_tool_with_text_returns_results(self)`
- Defined: `tests/test_mcp_server.py:145`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_query_tool_missing_required_param_raises (method) `def test_call_query_tool_missing_required_param_raises(self)`
- Defined: `tests/test_mcp_server.py:154`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_list_resources_returns_resource_definitions (method) `def test_list_resources_returns_resource_definitions(self)`
- Defined: `tests/test_mcp_server.py:168`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_read_resource_summary_returns_json (method) `def test_read_resource_summary_returns_json(self)`
- Defined: `tests/test_mcp_server.py:186`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_read_resource_unknown_uri_returns_error (method) `def test_read_resource_unknown_uri_returns_error(self)`
- Defined: `tests/test_mcp_server.py:197`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_read_resource_kb_returns_markdown (method) `def test_read_resource_kb_returns_markdown(self)`
- Defined: `tests/test_mcp_server.py:205`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### _get_tool_def (method) `def _get_tool_def(self, name)`
- Defined: `tests/test_mcp_server.py:219`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_query_tool_requires_text_param (method) `def test_query_tool_requires_text_param(self)`
- Defined: `tests/test_mcp_server.py:226`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_explain_tool_requires_name_param (method) `def test_explain_tool_requires_name_param(self)`
- Defined: `tests/test_mcp_server.py:230`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_path_tool_requires_two_params (method) `def test_path_tool_requires_two_params(self)`
- Defined: `tests/test_mcp_server.py:234`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_parse_error_for_invalid_json (method) `def test_parse_error_for_invalid_json(self)`
- Defined: `tests/test_mcp_server.py:243`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

### test_call_tool_returns_text_content_list (method) `def test_call_tool_returns_text_content_list(self)`
- Defined: `tests/test_mcp_server.py:251`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`

## tests/test_mermaid.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_mermaid.py:8`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_renders_graph_header (method) `def test_renders_graph_header(self)`
- Defined: `tests/test_mermaid.py:11`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_renders_module_node (method) `def test_renders_module_node(self)`
- Defined: `tests/test_mermaid.py:19`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_renders_symbol_subnodes (method) `def test_renders_symbol_subnodes(self)`
- Defined: `tests/test_mermaid.py:27`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_class_symbol_gets_cls_style (method) `def test_class_symbol_gets_cls_style(self)`
- Defined: `tests/test_mermaid.py:36`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_function_symbol_gets_fn_style (method) `def test_function_symbol_gets_fn_style(self)`
- Defined: `tests/test_mermaid.py:45`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_external_import_edge_is_dashed (method) `def test_external_import_edge_is_dashed(self)`
- Defined: `tests/test_mermaid.py:54`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_truncation_when_over_limit (method) `def test_truncation_when_over_limit(self)`
- Defined: `tests/test_mermaid.py:62`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_limits_symbols_to_five_per_node (method) `def test_limits_symbols_to_five_per_node(self)`
- Defined: `tests/test_mermaid.py:72`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

### test_handles_special_characters_in_ids (method) `def test_handles_special_characters_in_ids(self)`
- Defined: `tests/test_mermaid.py:82`
- Depends on: `readmenator/_mermaid.py`, `readmenator/_models.py`

## tests/test_models.py

### test_symbol_creation (method) `def test_symbol_creation(self)`
- Defined: `tests/test_models.py:7`
- Depends on: `readmenator/_models.py`

### test_symbol_with_signature (method) `def test_symbol_with_signature(self)`
- Defined: `tests/test_models.py:15`
- Depends on: `readmenator/_models.py`

### test_node_creation (method) `def test_node_creation(self)`
- Defined: `tests/test_models.py:21`
- Depends on: `readmenator/_models.py`

### test_node_with_symbols (method) `def test_node_with_symbols(self)`
- Defined: `tests/test_models.py:35`
- Depends on: `readmenator/_models.py`

### test_edge_creation (method) `def test_edge_creation(self)`
- Defined: `tests/test_models.py:49`
- Depends on: `readmenator/_models.py`

### test_pluralize_class (method) `def test_pluralize_class(self)`
- Defined: `tests/test_models.py:57`
- Depends on: `readmenator/_models.py`

### test_pluralize_unknown_appends_s (method) `def test_pluralize_unknown_appends_s(self)`
- Defined: `tests/test_models.py:62`
- Depends on: `readmenator/_models.py`

## tests/test_parsers.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:26`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_struct (method) `def test_extracts_struct(self)`
- Defined: `tests/test_parsers.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_include (method) `def test_extracts_include(self)`
- Defined: `tests/test_parsers.py:40`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_define (method) `def test_extracts_define(self)`
- Defined: `tests/test_parsers.py:47`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_skips_reserved_words (method) `def test_skips_reserved_words(self)`
- Defined: `tests/test_parsers.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_function_line_points_at_definition (method) `def test_function_line_points_at_definition(self)`
- Defined: `tests/test_parsers.py:64`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_calls_are_not_prototypes (method) `def test_calls_are_not_prototypes(self)`
- Defined: `tests/test_parsers.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_class_with_inheritance (method) `def test_class_with_inheritance(self)`
- Defined: `tests/test_parsers.py:80`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:92`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:99`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_imports (method) `def test_extracts_imports(self)`
- Defined: `tests/test_parsers.py:106`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_async_function (method) `def test_extracts_async_function(self)`
- Defined: `tests/test_parsers.py:114`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_handles_syntax_error_gracefully (method) `def test_handles_syntax_error_gracefully(self)`
- Defined: `tests/test_parsers.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_suppresses_syntax_warnings (method) `def test_suppresses_syntax_warnings(self)`
- Defined: `tests/test_parsers.py:127`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_signature_with_params (method) `def test_extracts_signature_with_params(self)`
- Defined: `tests/test_parsers.py:139`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class_with_bases (method) `def test_extracts_class_with_bases(self)`
- Defined: `tests/test_parsers.py:147`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:158`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:161`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method_receiver (method) `def test_extracts_method_receiver(self)`
- Defined: `tests/test_parsers.py:168`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import_block (method) `def test_extracts_import_block(self)`
- Defined: `tests/test_parsers.py:175`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_single_import (method) `def test_extracts_single_import(self)`
- Defined: `tests/test_parsers.py:182`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_struct_and_interface (method) `def test_extracts_struct_and_interface(self)`
- Defined: `tests/test_parsers.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:201`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:204`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_pub_function (method) `def test_extracts_pub_function(self)`
- Defined: `tests/test_parsers.py:211`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_struct_and_trait_and_enum (method) `def test_extracts_struct_and_trait_and_enum(self)`
- Defined: `tests/test_parsers.py:218`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_use (method) `def test_extracts_use(self)`
- Defined: `tests/test_parsers.py:231`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:239`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:242`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_arrow_function (method) `def test_extracts_arrow_function(self)`
- Defined: `tests/test_parsers.py:249`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:256`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import_and_require (method) `def test_extracts_import_and_require(self)`
- Defined: `tests/test_parsers.py:263`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_skips_reserved_words (method) `def test_skips_reserved_words(self)`
- Defined: `tests/test_parsers.py:270`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:278`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:281`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method (method) `def test_extracts_method(self)`
- Defined: `tests/test_parsers.py:288`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import (method) `def test_extracts_import(self)`
- Defined: `tests/test_parsers.py:295`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_abstract_class (method) `def test_abstract_class(self)`
- Defined: `tests/test_parsers.py:301`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:310`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:313`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method (method) `def test_extracts_method(self)`
- Defined: `tests/test_parsers.py:320`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_using (method) `def test_extracts_using(self)`
- Defined: `tests/test_parsers.py:327`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_record_and_interface (method) `def test_record_and_interface(self)`
- Defined: `tests/test_parsers.py:333`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:343`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function_with_parentheses (method) `def test_extracts_function_with_parentheses(self)`
- Defined: `tests/test_parsers.py:346`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function_keyword (method) `def test_extracts_function_keyword(self)`
- Defined: `tests/test_parsers.py:353`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:362`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:365`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:372`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_use_and_require (method) `def test_extracts_use_and_require(self)`
- Defined: `tests/test_parsers.py:379`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:388`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers.py:391`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:398`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import (method) `def test_extracts_import(self)`
- Defined: `tests/test_parsers.py:405`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:413`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers.py:416`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_extends (method) `def test_extracts_extends(self)`
- Defined: `tests/test_parsers.py:423`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:431`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_proc (method) `def test_extracts_proc(self)`
- Defined: `tests/test_parsers.py:434`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_type (method) `def test_extracts_type(self)`
- Defined: `tests/test_parsers.py:441`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_import (method) `def test_extracts_import(self)`
- Defined: `tests/test_parsers.py:448`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:457`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_label (method) `def test_extracts_label(self)`
- Defined: `tests/test_parsers.py:460`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_multiple_labels (method) `def test_extracts_multiple_labels(self)`
- Defined: `tests/test_parsers.py:467`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_includes (method) `def test_extracts_includes(self)`
- Defined: `tests/test_parsers.py:475`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers.py:484`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_c_parser_for_c_extensions (method) `def test_returns_c_parser_for_c_extensions(self)`
- Defined: `tests/test_parsers.py:487`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_python_parser_for_py (method) `def test_returns_python_parser_for_py(self)`
- Defined: `tests/test_parsers.py:493`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_none_for_unknown_extension (method) `def test_returns_none_for_unknown_extension(self)`
- Defined: `tests/test_parsers.py:498`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_returns_rust_parser_for_rs (method) `def test_returns_rust_parser_for_rs(self)`
- Defined: `tests/test_parsers.py:502`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_case_insensitive_extension (method) `def test_case_insensitive_extension(self)`
- Defined: `tests/test_parsers.py:507`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

## tests/test_parsers_new.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:16`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class_with_inheritance (method) `def test_extracts_class_with_inheritance(self)`
- Defined: `tests/test_parsers_new.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_module (method) `def test_extracts_module(self)`
- Defined: `tests/test_parsers_new.py:27`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_method (method) `def test_extracts_method(self)`
- Defined: `tests/test_parsers_new.py:33`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_require (method) `def test_extracts_require(self)`
- Defined: `tests/test_parsers_new.py:39`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers_new.py:49`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers_new.py:55`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_protocol (method) `def test_extracts_protocol(self)`
- Defined: `tests/test_parsers_new.py:61`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:69`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class (method) `def test_extracts_class(self)`
- Defined: `tests/test_parsers_new.py:72`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_fun (method) `def test_extracts_fun(self)`
- Defined: `tests/test_parsers_new.py:78`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:86`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_object (method) `def test_extracts_object(self)`
- Defined: `tests/test_parsers_new.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_def (method) `def test_extracts_def(self)`
- Defined: `tests/test_parsers_new.py:95`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:103`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers_new.py:106`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_require (method) `def test_extracts_require(self)`
- Defined: `tests/test_parsers_new.py:111`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:118`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_defmodule (method) `def test_extracts_defmodule(self)`
- Defined: `tests/test_parsers_new.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function (method) `def test_extracts_function(self)`
- Defined: `tests/test_parsers_new.py:127`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:135`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_ruby_extension_maps_correctly (method) `def test_ruby_extension_maps_correctly(self)`
- Defined: `tests/test_parsers_new.py:138`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_swift_extension_maps_correctly (method) `def test_swift_extension_maps_correctly(self)`
- Defined: `tests/test_parsers_new.py:142`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_kotlin_extension_maps_correctly (method) `def test_kotlin_extension_maps_correctly(self)`
- Defined: `tests/test_parsers_new.py:146`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_new.py:152`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_class_inheritance (method) `def test_extracts_class_inheritance(self)`
- Defined: `tests/test_parsers_new.py:155`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

### test_extracts_function_calls (method) `def test_extracts_function_calls(self)`
- Defined: `tests/test_parsers_new.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/parsers/__init__.py`

## tests/test_parsers_property.py

### _generate_multiline_code (function) `def _generate_multiline_code(lines, line_strategy)`
- Defined: `tests/test_parsers_property.py:105`
- Doc: Generate source code with a configurable number of lines.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _create_parser (function) `def _create_parser(ext)`
- Defined: `tests/test_parsers_property.py:142`
- Doc: Create a parser for the given extension.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_never_crashes_on_malformed_code (method) `def test_never_crashes_on_malformed_code(self, ext, code)`
- Defined: `tests/test_parsers_property.py:162`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_never_crashes_on_unicode_code (method) `def test_never_crashes_on_unicode_code(self, ext, code)`
- Defined: `tests/test_parsers_property.py:180`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_empty_code_returns_empty_or_valid (method) `def test_empty_code_returns_empty_or_valid(self, ext)`
- Defined: `tests/test_parsers_property.py:198`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_whitespace_code_returns_empty_or_valid (method) `def test_whitespace_code_returns_empty_or_valid(self, ext)`
- Defined: `tests/test_parsers_property.py:208`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_never_crashes_on_many_lines (method) `def test_never_crashes_on_many_lines(self, ext, lines)`
- Defined: `tests/test_parsers_property.py:220`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_repeated_keywords_no_crash (method) `def test_repeated_keywords_no_crash(self, ext)`
- Defined: `tests/test_parsers_property.py:238`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_parser_imports_is_list_of_strings (method) `def test_parser_imports_is_list_of_strings(self, ext)`
- Defined: `tests/test_parsers_property.py:257`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_unknown_extension_returns_none (method) `def test_unknown_extension_returns_none(self)`
- Defined: `tests/test_parsers_property.py:269`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### _assert_valid_symbols (method) `def _assert_valid_symbols(self, symbols)`
- Defined: `tests/test_parsers_property.py:275`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_parsers_property.py:291`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_python_never_crashes_on_weird_ascii (method) `def test_python_never_crashes_on_weird_ascii(self, code)`
- Defined: `tests/test_parsers_property.py:296`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### test_python_never_crashes_on_any_text (method) `def test_python_never_crashes_on_any_text(self, code)`
- Defined: `tests/test_parsers_property.py:310`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### given (method) `def given()`
- Defined: `tests/test_parsers_property.py:69`
- Doc: Identity decorator used when hypothesis is unavailable.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### settings (method) `def settings()`
- Defined: `tests/test_parsers_property.py:75`
- Doc: Identity decorator used when hypothesis is unavailable.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### __or__ (method) `def __or__(self, other)`
- Defined: `tests/test_parsers_property.py:48`
- Doc: Combine placeholders without evaluating strategies.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### __ror__ (method) `def __ror__(self, other)`
- Defined: `tests/test_parsers_property.py:52`
- Doc: Combine placeholders without evaluating strategies.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### map (method) `def map(self)`
- Defined: `tests/test_parsers_property.py:56`
- Doc: Return the placeholder unchanged.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### __getattr__ (method) `def __getattr__(self, name)`
- Defined: `tests/test_parsers_property.py:63`
- Doc: Return a builder producing inert placeholders.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### wrapper (method) `def wrapper(fn)`
- Defined: `tests/test_parsers_property.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### wrapper (method) `def wrapper(fn)`
- Defined: `tests/test_parsers_property.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

### builder (method) `def builder()`
- Defined: `tests/test_parsers_property.py:65`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`

## tests/test_query.py

### _make_node (function) `def _make_node(node_id, symbols)`
- Defined: `tests/test_query.py:7`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### _make_sym (function) `def _make_sym(name, kind, line)`
- Defined: `tests/test_query.py:18`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_query.py:23`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_exact_symbol (method) `def test_find_exact_symbol(self)`
- Defined: `tests/test_query.py:36`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_symbol_fuzzy (method) `def test_find_symbol_fuzzy(self)`
- Defined: `tests/test_query.py:42`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_symbol_not_found (method) `def test_find_symbol_not_found(self)`
- Defined: `tests/test_query.py:47`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_returns_details (method) `def test_explain_returns_details(self)`
- Defined: `tests/test_query.py:51`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_shows_imports (method) `def test_explain_shows_imports(self)`
- Defined: `tests/test_query.py:58`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_shows_siblings (method) `def test_explain_shows_siblings(self)`
- Defined: `tests/test_query.py:63`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_explain_unknown_returns_none (method) `def test_explain_unknown_returns_none(self)`
- Defined: `tests/test_query.py:69`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_path_direct_import (method) `def test_find_path_direct_import(self)`
- Defined: `tests/test_query.py:73`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_path_same_file (method) `def test_find_path_same_file(self)`
- Defined: `tests/test_query.py:79`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_find_path_unknown_returns_none (method) `def test_find_path_unknown_returns_none(self)`
- Defined: `tests/test_query.py:84`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_summary_shows_counts (method) `def test_summary_shows_counts(self)`
- Defined: `tests/test_query.py:88`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_summary_shows_top_modules (method) `def test_summary_shows_top_modules(self)`
- Defined: `tests/test_query.py:94`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_query_returns_matching_symbols (method) `def test_query_returns_matching_symbols(self)`
- Defined: `tests/test_query.py:98`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

### test_query_returns_file_matches (method) `def test_query_returns_file_matches(self)`
- Defined: `tests/test_query.py:102`
- Depends on: `readmenator/_models.py`, `readmenator/_query.py`

## tests/test_ranking.py

### _make_test_graph (method) `def _make_test_graph()`
- Defined: `tests/test_ranking.py:238`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_all_edge_kinds_have_weights (method) `def test_all_edge_kinds_have_weights(self)`
- Defined: `tests/test_ranking.py:61`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_infer_edge_kind_maps_correctly (method) `def test_infer_edge_kind_maps_correctly(self)`
- Defined: `tests/test_ranking.py:66`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_infer_edge_kind_falls_back (method) `def test_infer_edge_kind_falls_back(self)`
- Defined: `tests/test_ranking.py:71`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_edge_kind_is_str_enum (method) `def test_edge_kind_is_str_enum(self)`
- Defined: `tests/test_ranking.py:75`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_weight_is_edge_weight_times_confidence (method) `def test_weight_is_edge_weight_times_confidence(self)`
- Defined: `tests/test_ranking.py:85`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_weight_default_confidence (method) `def test_weight_default_confidence(self)`
- Defined: `tests/test_ranking.py:90`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_morphism_is_frozen (method) `def test_morphism_is_frozen(self)`
- Defined: `tests/test_ranking.py:94`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_category (method) `def test_empty_category(self)`
- Defined: `tests/test_ranking.py:105`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_add_object_and_morphism (method) `def test_add_object_and_morphism(self)`
- Defined: `tests/test_ranking.py:110`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_outgoing_and_incoming (method) `def test_outgoing_and_incoming(self)`
- Defined: `tests/test_ranking.py:118`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_same_kind (method) `def test_compose_same_kind(self)`
- Defined: `tests/test_ranking.py:130`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_imports_then_defines (method) `def test_compose_imports_then_defines(self)`
- Defined: `tests/test_ranking.py:140`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_incompatible_returns_none (method) `def test_compose_incompatible_returns_none(self)`
- Defined: `tests/test_ranking.py:148`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_compose_mismatched_target_source (method) `def test_compose_mismatched_target_source(self)`
- Defined: `tests/test_ranking.py:155`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_paths_finds_composition_chains (method) `def test_paths_finds_composition_chains(self)`
- Defined: `tests/test_ranking.py:162`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_paths_empty_when_no_route (method) `def test_paths_empty_when_no_route(self)`
- Defined: `tests/test_ranking.py:171`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_graph (method) `def test_empty_graph(self)`
- Defined: `tests/test_ranking.py:184`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_stochastic_row_normalizes_to_one (method) `def test_stochastic_row_normalizes_to_one(self)`
- Defined: `tests/test_ranking.py:190`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_stochastic_row_empty_for_dangling (method) `def test_stochastic_row_empty_for_dangling(self)`
- Defined: `tests/test_ranking.py:199`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_transition_weight_aggregates_parallel_edges (method) `def test_transition_weight_aggregates_parallel_edges(self)`
- Defined: `tests/test_ranking.py:205`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_category_from_edges (method) `def test_build_category_from_edges(self)`
- Defined: `tests/test_ranking.py:214`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_category_from_edges_filters_by_node_ids (method) `def test_build_category_from_edges_filters_by_node_ids(self)`
- Defined: `tests/test_ranking.py:225`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_scores_sum_to_one (method) `def test_scores_sum_to_one(self)`
- Defined: `tests/test_ranking.py:248`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_all_nodes_have_positive_score (method) `def test_all_nodes_have_positive_score(self)`
- Defined: `tests/test_ranking.py:254`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_converges_within_max_iter (method) `def test_converges_within_max_iter(self)`
- Defined: `tests/test_ranking.py:260`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_stable_across_calls (method) `def test_stable_across_calls(self)`
- Defined: `tests/test_ranking.py:266`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_dangling_node_handled (method) `def test_dangling_node_handled(self)`
- Defined: `tests/test_ranking.py:273`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_graph (method) `def test_empty_graph(self)`
- Defined: `tests/test_ranking.py:284`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_seed_node_gets_highest_score (method) `def test_seed_node_gets_highest_score(self)`
- Defined: `tests/test_ranking.py:289`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_scores_sum_to_one (method) `def test_scores_sum_to_one(self)`
- Defined: `tests/test_ranking.py:296`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_different_seeds_produce_different_rankings (method) `def test_different_seeds_produce_different_rankings(self)`
- Defined: `tests/test_ranking.py:303`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_empty_seeds_uses_uniform (method) `def test_empty_seeds_uses_uniform(self)`
- Defined: `tests/test_ranking.py:310`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_multi_seed (method) `def test_multi_seed(self)`
- Defined: `tests/test_ranking.py:317`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_authorities_and_hubs_have_positive_scores (method) `def test_authorities_and_hubs_have_positive_scores(self)`
- Defined: `tests/test_ranking.py:326`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_authorities_l2_normalized (method) `def test_authorities_l2_normalized(self)`
- Defined: `tests/test_ranking.py:333`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_hubs_l2_normalized (method) `def test_hubs_l2_normalized(self)`
- Defined: `tests/test_ranking.py:339`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_from_query_matches_node_id (method) `def test_build_seeds_from_query_matches_node_id(self)`
- Defined: `tests/test_ranking.py:351`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_from_query_matches_symbol (method) `def test_build_seeds_from_query_matches_symbol(self)`
- Defined: `tests/test_ranking.py:363`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_from_query_no_match_returns_empty (method) `def test_build_seeds_from_query_no_match_returns_empty(self)`
- Defined: `tests/test_ranking.py:374`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_for_context (method) `def test_build_seeds_for_context(self)`
- Defined: `tests/test_ranking.py:383`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_build_seeds_for_context_no_match (method) `def test_build_seeds_for_context_no_match(self)`
- Defined: `tests/test_ranking.py:392`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_rank_returns_sorted_results (method) `def test_rank_returns_sorted_results(self)`
- Defined: `tests/test_ranking.py:404`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_rank_items_have_all_score_fields (method) `def test_rank_items_have_all_score_fields(self)`
- Defined: `tests/test_ranking.py:421`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_noise_penalty_applied (method) `def test_noise_penalty_applied(self)`
- Defined: `tests/test_ranking.py:447`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_top_n (method) `def test_top_n(self)`
- Defined: `tests/test_ranking.py:466`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_explain_returns_none_for_missing (method) `def test_explain_returns_none_for_missing(self)`
- Defined: `tests/test_ranking.py:479`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_identity_projection_passes_all (method) `def test_identity_projection_passes_all(self)`
- Defined: `tests/test_ranking.py:491`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_doc_projection_filters_undocumented (method) `def test_doc_projection_filters_undocumented(self)`
- Defined: `tests/test_ranking.py:498`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_doc_projection_filters_morphism_kind (method) `def test_doc_projection_filters_morphism_kind(self)`
- Defined: `tests/test_ranking.py:506`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_apply_view_architecture (method) `def test_apply_view_architecture(self)`
- Defined: `tests/test_ranking.py:512`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_apply_view_reverse (method) `def test_apply_view_reverse(self)`
- Defined: `tests/test_ranking.py:521`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_apply_view_empty (method) `def test_apply_view_empty(self)`
- Defined: `tests/test_ranking.py:528`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_explain_rank_found (method) `def test_explain_rank_found(self)`
- Defined: `tests/test_ranking.py:540`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_explain_rank_not_found (method) `def test_explain_rank_not_found(self)`
- Defined: `tests/test_ranking.py:559`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_rank_summary_format (method) `def test_rank_summary_format(self)`
- Defined: `tests/test_ranking.py:565`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_category_from_real_edges (method) `def test_category_from_real_edges(self)`
- Defined: `tests/test_ranking.py:588`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_pagerank_on_real_category (method) `def test_pagerank_on_real_category(self)`
- Defined: `tests/test_ranking.py:613`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_ppr_favors_seed (method) `def test_ppr_favors_seed(self)`
- Defined: `tests/test_ranking.py:625`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

### test_ranker_from_real_data (method) `def test_ranker_from_real_data(self)`
- Defined: `tests/test_ranking.py:637`
- Depends on: `readmenator/_category.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_projections.py`, `readmenator/_rank.py`

## tests/test_readme_injector.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_readme_injector.py:19`
- Depends on: `readmenator/_readme_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:24`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_into_markdown_readme_adds_kb_link (method) `def test_inject_into_markdown_readme_adds_kb_link(self)`
- Defined: `tests/test_readme_injector.py:28`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_into_rst_readme_adds_kb_link (method) `def test_inject_into_rst_readme_adds_kb_link(self)`
- Defined: `tests/test_readme_injector.py:39`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_is_idempotent_does_not_duplicate (method) `def test_inject_is_idempotent_does_not_duplicate(self)`
- Defined: `tests/test_readme_injector.py:48`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_no_readme_file_returns_false (method) `def test_inject_no_readme_file_returns_false(self)`
- Defined: `tests/test_readme_injector.py:59`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_preserves_existing_content (method) `def test_inject_preserves_existing_content(self)`
- Defined: `tests/test_readme_injector.py:63`
- Depends on: `readmenator/_readme_injector.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_readme_injector.py:75`
- Depends on: `readmenator/_readme_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:80`
- Depends on: `readmenator/_readme_injector.py`

### test_remove_strips_injected_section (method) `def test_remove_strips_injected_section(self)`
- Defined: `tests/test_readme_injector.py:84`
- Depends on: `readmenator/_readme_injector.py`

### test_remove_without_injection_returns_false (method) `def test_remove_without_injection_returns_false(self)`
- Defined: `tests/test_readme_injector.py:94`
- Depends on: `readmenator/_readme_injector.py`

### test_remove_no_readme_returns_false (method) `def test_remove_no_readme_returns_false(self)`
- Defined: `tests/test_readme_injector.py:100`
- Depends on: `readmenator/_readme_injector.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_readme_injector.py:108`
- Depends on: `readmenator/_readme_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:112`
- Depends on: `readmenator/_readme_injector.py`

### test_finds_readme_md (method) `def test_finds_readme_md(self)`
- Defined: `tests/test_readme_injector.py:116`
- Depends on: `readmenator/_readme_injector.py`

### test_finds_readme_rst (method) `def test_finds_readme_rst(self)`
- Defined: `tests/test_readme_injector.py:122`
- Depends on: `readmenator/_readme_injector.py`

### test_prefers_readme_md_over_rst (method) `def test_prefers_readme_md_over_rst(self)`
- Defined: `tests/test_readme_injector.py:128`
- Depends on: `readmenator/_readme_injector.py`

### test_returns_none_when_no_readme (method) `def test_returns_none_when_no_readme(self)`
- Defined: `tests/test_readme_injector.py:135`
- Depends on: `readmenator/_readme_injector.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_readme_injector.py:143`
- Depends on: `readmenator/_readme_injector.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_readme_injector.py:148`
- Depends on: `readmenator/_readme_injector.py`

### test_inject_into_empty_readme (method) `def test_inject_into_empty_readme(self)`
- Defined: `tests/test_readme_injector.py:152`
- Depends on: `readmenator/_readme_injector.py`

### test_custom_kb_filename_works (method) `def test_custom_kb_filename_works(self)`
- Defined: `tests/test_readme_injector.py:160`
- Depends on: `readmenator/_readme_injector.py`

## tests/test_refactorizer.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_refactorizer.py:21`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### _make_symbol (method) `def _make_symbol(self, name, kind, line)`
- Defined: `tests/test_refactorizer.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### _make_node (method) `def _make_node(self, nid, symbols)`
- Defined: `tests/test_refactorizer.py:28`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### _make_edge (method) `def _make_edge(self, src, tgt)`
- Defined: `tests/test_refactorizer.py:37`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_empty_graph_returns_empty (method) `def test_analyze_empty_graph_returns_empty(self)`
- Defined: `tests/test_refactorizer.py:40`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_ignores_small_files (method) `def test_analyze_ignores_small_files(self)`
- Defined: `tests/test_refactorizer.py:44`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_detects_large_file (method) `def test_analyze_detects_large_file(self)`
- Defined: `tests/test_refactorizer.py:50`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_generates_extract_class_for_multiple_classes (method) `def test_analyze_generates_extract_class_for_multiple_classes(self)`
- Defined: `tests/test_refactorizer.py:59`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_generates_extract_function_for_multiple_functions (method) `def test_analyze_generates_extract_function_for_multiple_functions(self)`
- Defined: `tests/test_refactorizer.py:74`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_splits_file_with_many_symbols (method) `def test_analyze_splits_file_with_many_symbols(self)`
- Defined: `tests/test_refactorizer.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_estimates_impact_from_resolved_edges (method) `def test_analyze_estimates_impact_from_resolved_edges(self)`
- Defined: `tests/test_refactorizer.py:97`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_generate_script_contains_shebang (method) `def test_generate_script_contains_shebang(self)`
- Defined: `tests/test_refactorizer.py:109`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_generate_script_contains_set_e (method) `def test_generate_script_contains_set_e(self)`
- Defined: `tests/test_refactorizer.py:129`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_generate_script_contains_sed_commands (method) `def test_generate_script_contains_sed_commands(self)`
- Defined: `tests/test_refactorizer.py:140`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_sorted_by_line_count (method) `def test_analyze_sorted_by_line_count(self)`
- Defined: `tests/test_refactorizer.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

### test_analyze_respects_max_files_limit (method) `def test_analyze_respects_max_files_limit(self)`
- Defined: `tests/test_refactorizer.py:173`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_refactorizer.py`

## tests/test_resolver.py

### test_resolves_python_module_dotpath (method) `def test_resolves_python_module_dotpath(self)`
- Defined: `tests/test_resolver.py:18`
- Depends on: `readmenator/_resolver.py`

### test_resolves_relative_import (method) `def test_resolves_relative_import(self)`
- Defined: `tests/test_resolver.py:25`
- Depends on: `readmenator/_resolver.py`

### test_resolves_extensionless_python_import (method) `def test_resolves_extensionless_python_import(self)`
- Defined: `tests/test_resolver.py:32`
- Depends on: `readmenator/_resolver.py`

### test_resolves_package_init (method) `def test_resolves_package_init(self)`
- Defined: `tests/test_resolver.py:39`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_external_stdlib (method) `def test_returns_none_for_external_stdlib(self)`
- Defined: `tests/test_resolver.py:46`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_unknown_import (method) `def test_returns_none_for_unknown_import(self)`
- Defined: `tests/test_resolver.py:53`
- Depends on: `readmenator/_resolver.py`

### test_resolves_stem_match_when_unique (method) `def test_resolves_stem_match_when_unique(self)`
- Defined: `tests/test_resolver.py:60`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_empty_import (method) `def test_returns_none_for_empty_import(self)`
- Defined: `tests/test_resolver.py:67`
- Depends on: `readmenator/_resolver.py`

### test_resolves_go_import (method) `def test_resolves_go_import(self)`
- Defined: `tests/test_resolver.py:72`
- Depends on: `readmenator/_resolver.py`

### test_resolves_same_directory_import (method) `def test_resolves_same_directory_import(self)`
- Defined: `tests/test_resolver.py:79`
- Depends on: `readmenator/_resolver.py`

### test_resolves_c_quoted_header_same_dir (method) `def test_resolves_c_quoted_header_same_dir(self)`
- Defined: `tests/test_resolver.py:86`
- Depends on: `readmenator/_resolver.py`

### test_resolves_c_quoted_header_subdir (method) `def test_resolves_c_quoted_header_subdir(self)`
- Defined: `tests/test_resolver.py:93`
- Depends on: `readmenator/_resolver.py`

### test_resolves_c_extensionless_header (method) `def test_resolves_c_extensionless_header(self)`
- Defined: `tests/test_resolver.py:100`
- Depends on: `readmenator/_resolver.py`

### test_resolves_c_source_from_header_dir (method) `def test_resolves_c_source_from_header_dir(self)`
- Defined: `tests/test_resolver.py:107`
- Depends on: `readmenator/_resolver.py`

### test_resolves_cpp_header_same_dir (method) `def test_resolves_cpp_header_same_dir(self)`
- Defined: `tests/test_resolver.py:114`
- Depends on: `readmenator/_resolver.py`

### test_resolves_c_header_stem_across_dirs (method) `def test_resolves_c_header_stem_across_dirs(self)`
- Defined: `tests/test_resolver.py:121`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_c_system_header (method) `def test_returns_none_for_c_system_header(self)`
- Defined: `tests/test_resolver.py:128`
- Depends on: `readmenator/_resolver.py`

### test_resolves_parent_dir_include (method) `def test_resolves_parent_dir_include(self)`
- Defined: `tests/test_resolver.py:135`
- Depends on: `readmenator/_resolver.py`

### test_resolves_parent_dir_include_despite_ambiguous_stem (method) `def test_resolves_parent_dir_include_despite_ambiguous_stem(self)`
- Defined: `tests/test_resolver.py:142`
- Depends on: `readmenator/_resolver.py`

### test_resolves_include_dir_suffix_match (method) `def test_resolves_include_dir_suffix_match(self)`
- Defined: `tests/test_resolver.py:149`
- Depends on: `readmenator/_resolver.py`

### test_returns_none_for_ambiguous_suffix_match (method) `def test_returns_none_for_ambiguous_suffix_match(self)`
- Defined: `tests/test_resolver.py:156`
- Depends on: `readmenator/_resolver.py`

## tests/test_rule_gen.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_rule_gen.py:15`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### _make_node (method) `def _make_node(self, nid, label, lang)`
- Defined: `tests/test_rule_gen.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### _make_node_with_symbols (method) `def _make_node_with_symbols(self, nid, sym_count)`
- Defined: `tests/test_rule_gen.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_empty_nodes_returns_empty_rules (method) `def test_empty_nodes_returns_empty_rules(self)`
- Defined: `tests/test_rule_gen.py:44`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_generates_rules_for_function_heavy_language (method) `def test_generates_rules_for_function_heavy_language(self)`
- Defined: `tests/test_rule_gen.py:48`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_detects_antipatterns_with_content (method) `def test_detects_antipatterns_with_content(self)`
- Defined: `tests/test_rule_gen.py:56`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_antipattern_threshold_from_config (method) `def test_antipattern_threshold_from_config(self)`
- Defined: `tests/test_rule_gen.py:67`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_write_rules_creates_files (method) `def test_write_rules_creates_files(self)`
- Defined: `tests/test_rule_gen.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

### test_rule_id_increments (method) `def test_rule_id_increments(self)`
- Defined: `tests/test_rule_gen.py:90`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_rule_gen.py`

## tests/test_sarif.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_sarif.py:14`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### _make_finding (method) `def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)`
- Defined: `tests/test_sarif.py:18`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_returns_valid_json (method) `def test_export_returns_valid_json(self)`
- Defined: `tests/test_sarif.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_includes_tool_info (method) `def test_export_includes_tool_info(self)`
- Defined: `tests/test_sarif.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_includes_rule (method) `def test_export_includes_rule(self)`
- Defined: `tests/test_sarif.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_export_includes_result (method) `def test_export_includes_result(self)`
- Defined: `tests/test_sarif.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_severity_maps_correctly (method) `def test_severity_maps_correctly(self)`
- Defined: `tests/test_sarif.py:73`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_privacy_mode_strips_snippets (method) `def test_privacy_mode_strips_snippets(self)`
- Defined: `tests/test_sarif.py:88`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

### test_empty_findings_produces_valid_sarif (method) `def test_empty_findings_produces_valid_sarif(self)`
- Defined: `tests/test_sarif.py:97`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_sarif.py`

## tests/test_scanner.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_scanner.py:12`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### tearDown (method) `def tearDown(self)`
- Defined: `tests/test_scanner.py:16`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### _write (method) `def _write(self, path, content)`
- Defined: `tests/test_scanner.py:20`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_scans_python_files (method) `def test_scans_python_files(self)`
- Defined: `tests/test_scanner.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_ignores_env_and_vendor_dirs (method) `def test_ignores_env_and_vendor_dirs(self)`
- Defined: `tests/test_scanner.py:32`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_rejects_symlinks (method) `def test_rejects_symlinks(self)`
- Defined: `tests/test_scanner.py:45`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_skips_non_code_files (method) `def test_skips_non_code_files(self)`
- Defined: `tests/test_scanner.py:59`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_scans_multiple_languages (method) `def test_scans_multiple_languages(self)`
- Defined: `tests/test_scanner.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_respects_max_directory_depth (method) `def test_respects_max_directory_depth(self)`
- Defined: `tests/test_scanner.py:79`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_raises_on_invalid_directory (method) `def test_raises_on_invalid_directory(self)`
- Defined: `tests/test_scanner.py:89`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_import_edges_are_created (method) `def test_import_edges_are_created(self)`
- Defined: `tests/test_scanner.py:94`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_privacy_mode_strips_docs (method) `def test_privacy_mode_strips_docs(self)`
- Defined: `tests/test_scanner.py:104`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_module_docstring_extracted_as_file_doc (method) `def test_module_docstring_extracted_as_file_doc(self)`
- Defined: `tests/test_scanner.py:114`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_multiline_module_docstring_extracted (method) `def test_multiline_module_docstring_extracted(self)`
- Defined: `tests/test_scanner.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_coding_cookie_ignored_as_file_doc (method) `def test_coding_cookie_ignored_as_file_doc(self)`
- Defined: `tests/test_scanner.py:129`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_preprocessor_guards_ignored_as_file_doc (method) `def test_preprocessor_guards_ignored_as_file_doc(self)`
- Defined: `tests/test_scanner.py:136`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_scan_with_content_returns_content_map (method) `def test_scan_with_content_returns_content_map(self)`
- Defined: `tests/test_scanner.py:143`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_gitignore_respected_when_enabled (method) `def test_gitignore_respected_when_enabled(self)`
- Defined: `tests/test_scanner.py:151`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_gitignore_disabled_by_default (method) `def test_gitignore_disabled_by_default(self)`
- Defined: `tests/test_scanner.py:162`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

### test_gitignore_glob_conversion (method) `def test_gitignore_glob_conversion(self)`
- Defined: `tests/test_scanner.py:171`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_scanner.py`

## tests/test_security.py

### test_security_finding_fields (method) `def test_security_finding_fields(self)`
- Defined: `tests/test_security.py:24`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_default_config_disables_security (method) `def test_default_config_disables_security(self)`
- Defined: `tests/test_security.py:46`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_default_severity_threshold (method) `def test_default_severity_threshold(self)`
- Defined: `tests/test_security.py:50`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_default_security_output (method) `def test_default_security_output(self)`
- Defined: `tests/test_security.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_init_with_config (method) `def test_init_with_config(self)`
- Defined: `tests/test_security.py:58`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_security.py:67`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### _scan_content (method) `def _scan_content(self, content, extension)`
- Defined: `tests/test_security.py:71`
- Doc: Write content to a temp file and scan it.
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_os_system (method) `def test_python_os_system(self)`
- Defined: `tests/test_security.py:78`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_eval (method) `def test_python_eval(self)`
- Defined: `tests/test_security.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_pickle (method) `def test_python_pickle(self)`
- Defined: `tests/test_security.py:88`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_sql_injection (method) `def test_python_sql_injection(self)`
- Defined: `tests/test_security.py:93`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_hardcoded_secret (method) `def test_python_hardcoded_secret(self)`
- Defined: `tests/test_security.py:98`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_weak_crypto (method) `def test_python_weak_crypto(self)`
- Defined: `tests/test_security.py:103`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_request_verify_false (method) `def test_python_request_verify_false(self)`
- Defined: `tests/test_security.py:108`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_flask_debug (method) `def test_python_flask_debug(self)`
- Defined: `tests/test_security.py:113`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_python_yaml_load (method) `def test_python_yaml_load(self)`
- Defined: `tests/test_security.py:118`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_inner_html (method) `def test_javascript_inner_html(self)`
- Defined: `tests/test_security.py:123`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_eval (method) `def test_javascript_eval(self)`
- Defined: `tests/test_security.py:128`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_child_process (method) `def test_javascript_child_process(self)`
- Defined: `tests/test_security.py:133`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_javascript_dangerously_set_inner_html (method) `def test_javascript_dangerously_set_inner_html(self)`
- Defined: `tests/test_security.py:138`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_c_strcpy (method) `def test_c_strcpy(self)`
- Defined: `tests/test_security.py:143`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_c_gets (method) `def test_c_gets(self)`
- Defined: `tests/test_security.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_c_system (method) `def test_c_system(self)`
- Defined: `tests/test_security.py:153`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_java_runtime_exec (method) `def test_java_runtime_exec(self)`
- Defined: `tests/test_security.py:158`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_java_sql_injection (method) `def test_java_sql_injection(self)`
- Defined: `tests/test_security.py:163`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_go_exec_command (method) `def test_go_exec_command(self)`
- Defined: `tests/test_security.py:168`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ruby_eval (method) `def test_ruby_eval(self)`
- Defined: `tests/test_security.py:173`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ruby_marshal_load (method) `def test_ruby_marshal_load(self)`
- Defined: `tests/test_security.py:178`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_eval (method) `def test_php_eval(self)`
- Defined: `tests/test_security.py:183`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_sql_injection (method) `def test_php_sql_injection(self)`
- Defined: `tests/test_security.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_unseralize (method) `def test_php_unseralize(self)`
- Defined: `tests/test_security.py:193`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_shell_eval (method) `def test_shell_eval(self)`
- Defined: `tests/test_security.py:198`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_csharp_process_start (method) `def test_csharp_process_start(self)`
- Defined: `tests/test_security.py:203`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_kotlin_runtime_exec (method) `def test_kotlin_runtime_exec(self)`
- Defined: `tests/test_security.py:208`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_swift_process (method) `def test_swift_process(self)`
- Defined: `tests/test_security.py:213`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_lua_load (method) `def test_lua_load(self)`
- Defined: `tests/test_security.py:218`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_lua_os_execute (method) `def test_lua_os_execute(self)`
- Defined: `tests/test_security.py:223`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_dart_process_run (method) `def test_dart_process_run(self)`
- Defined: `tests/test_security.py:228`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_rust_unsafe (method) `def test_rust_unsafe(self)`
- Defined: `tests/test_security.py:233`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_elixir_code_eval (method) `def test_elixir_code_eval(self)`
- Defined: `tests/test_security.py:238`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_elixir_system_cmd (method) `def test_elixir_system_cmd(self)`
- Defined: `tests/test_security.py:243`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_gdscript_os_execute (method) `def test_gdscript_os_execute(self)`
- Defined: `tests/test_security.py:248`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_scala_runtime_exec (method) `def test_scala_runtime_exec(self)`
- Defined: `tests/test_security.py:253`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_nim_exec_process (method) `def test_nim_exec_process(self)`
- Defined: `tests/test_security.py:258`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_safe_code_produces_no_findings (method) `def test_safe_code_produces_no_findings(self)`
- Defined: `tests/test_security.py:263`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_csharp_binary_formatter (method) `def test_csharp_binary_formatter(self)`
- Defined: `tests/test_security.py:274`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ruby_backtick (method) `def test_ruby_backtick(self)`
- Defined: `tests/test_security.py:279`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_php_xss (method) `def test_php_xss(self)`
- Defined: `tests/test_security.py:284`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_go_unsafe_package (method) `def test_go_unsafe_package(self)`
- Defined: `tests/test_security.py:289`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_threshold_filters_low (method) `def test_threshold_filters_low(self)`
- Defined: `tests/test_security.py:298`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_threshold_info_shows_all (method) `def test_threshold_info_shows_all(self)`
- Defined: `tests/test_security.py:312`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ignores_symlinks (method) `def test_ignores_symlinks(self)`
- Defined: `tests/test_security.py:330`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_ignores_ignored_dirs (method) `def test_ignores_ignored_dirs(self)`
- Defined: `tests/test_security.py:345`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_empty_directory (method) `def test_empty_directory(self)`
- Defined: `tests/test_security.py:357`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_unsupported_extension (method) `def test_unsupported_extension(self)`
- Defined: `tests/test_security.py:364`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_summary_empty (method) `def test_summary_empty(self)`
- Defined: `tests/test_security.py:377`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_summary_with_findings (method) `def test_summary_with_findings(self)`
- Defined: `tests/test_security.py:383`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### _finding (method) `def _finding(self, cwe)`
- Defined: `tests/test_security.py:399`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_known_cwe_returns_actionable_hint (method) `def test_known_cwe_returns_actionable_hint(self)`
- Defined: `tests/test_security.py:402`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_unknown_cwe_falls_back (method) `def test_unknown_cwe_falls_back(self)`
- Defined: `tests/test_security.py:408`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

### test_empty_cwe_falls_back (method) `def test_empty_cwe_falls_back(self)`
- Defined: `tests/test_security.py:413`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_security.py`

## tests/test_taint.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_taint.py:13`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### _make_node (method) `def _make_node(self, nid, label)`
- Defined: `tests/test_taint.py:17`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_empty_graph_returns_empty_result (method) `def test_empty_graph_returns_empty_result(self)`
- Defined: `tests/test_taint.py:20`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_no_dangerous_imports_returns_empty (method) `def test_no_dangerous_imports_returns_empty(self)`
- Defined: `tests/test_taint.py:25`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_direct_dangerous_import_found (method) `def test_direct_dangerous_import_found(self)`
- Defined: `tests/test_taint.py:31`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_taint_propagates_through_resolved_edges (method) `def test_taint_propagates_through_resolved_edges(self)`
- Defined: `tests/test_taint.py:38`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_dangerous_import_by_language (method) `def test_dangerous_import_by_language(self)`
- Defined: `tests/test_taint.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_taint_path_has_severity (method) `def test_taint_path_has_severity(self)`
- Defined: `tests/test_taint.py:70`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

### test_max_depth_limits_propagation (method) `def test_max_depth_limits_propagation(self)`
- Defined: `tests/test_taint.py:77`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_taint.py`

## tests/test_taint_bdd.py

### _build_project_files (function) `def _build_project_files(project, root)`
- Defined: `tests/test_taint_bdd.py:29`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _scan_project (function) `def _scan_project(root, cfg)`
- Defined: `tests/test_taint_bdd.py:36`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _run_taint (function) `def _run_taint(files, cfg)`
- Defined: `tests/test_taint_bdd.py:54`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_direct_dangerous_import (function) `def test_direct_dangerous_import()`
- Defined: `tests/test_taint_bdd.py:71`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_taint_propagates_chain (function) `def test_taint_propagates_chain()`
- Defined: `tests/test_taint_bdd.py:75`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_taint_max_depth (function) `def test_taint_max_depth()`
- Defined: `tests/test_taint_bdd.py:79`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_cross_language_taint (function) `def test_cross_language_taint()`
- Defined: `tests/test_taint_bdd.py:83`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### test_bdd_skipped (function) `def test_bdd_skipped()`
- Defined: `tests/test_taint_bdd.py:87`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _bkg (function) `def _bkg()`
- Defined: `tests/test_taint_bdd.py:112`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _direct_given (function) `def _direct_given()`
- Defined: `tests/test_taint_bdd.py:117`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _direct_when (function) `def _direct_when(_taint_result)`
- Defined: `tests/test_taint_bdd.py:121`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_has_path (function) `def _check_has_path(_taint_result)`
- Defined: `tests/test_taint_bdd.py:125`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_direct_path (function) `def _check_direct_path(_taint_result)`
- Defined: `tests/test_taint_bdd.py:130`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_src (function) `def _check_src(_taint_result)`
- Defined: `tests/test_taint_bdd.py:135`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_sink (function) `def _check_sink(_taint_result)`
- Defined: `tests/test_taint_bdd.py:139`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _chain_given (function) `def _chain_given()`
- Defined: `tests/test_taint_bdd.py:144`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _chain_when (function) `def _chain_when(_taint_result)`
- Defined: `tests/test_taint_bdd.py:148`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_long_path (function) `def _check_long_path(_taint_result)`
- Defined: `tests/test_taint_bdd.py:152`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _shallow_cfg (function) `def _shallow_cfg()`
- Defined: `tests/test_taint_bdd.py:159`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _chain_given2 (function) `def _chain_given2()`
- Defined: `tests/test_taint_bdd.py:163`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _run_shallow (function) `def _run_shallow(_shallow_cfg)`
- Defined: `tests/test_taint_bdd.py:167`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_shallow (function) `def _check_shallow(_taint_result)`
- Defined: `tests/test_taint_bdd.py:171`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _js_given (function) `def _js_given()`
- Defined: `tests/test_taint_bdd.py:178`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _js_when (function) `def _js_when(_taint_result)`
- Defined: `tests/test_taint_bdd.py:182`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_js_dangerous (function) `def _check_js_dangerous(_taint_result)`
- Defined: `tests/test_taint_bdd.py:186`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

### _check_js_source (function) `def _check_js_source(_taint_result)`
- Defined: `tests/test_taint_bdd.py:192`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_resolver.py`, `readmenator/_scanner.py`, `readmenator/_taint.py`

## tests/test_uml.py

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:19`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_empty_nodes_returns_empty_string (method) `def test_render_empty_nodes_returns_empty_string(self)`
- Defined: `tests/test_uml.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_no_class_symbols_returns_empty_string (method) `def test_render_no_class_symbols_returns_empty_string(self)`
- Defined: `tests/test_uml.py:27`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_single_class_produces_mermaid_class_diagram (method) `def test_render_single_class_produces_mermaid_class_diagram(self)`
- Defined: `tests/test_uml.py:42`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_multiple_classes_from_different_files (method) `def test_render_multiple_classes_from_different_files(self)`
- Defined: `tests/test_uml.py:62`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_with_import_edges_produces_relationships (method) `def test_render_with_import_edges_produces_relationships(self)`
- Defined: `tests/test_uml.py:90`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_respects_max_classes_limit (method) `def test_render_respects_max_classes_limit(self)`
- Defined: `tests/test_uml.py:119`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_render_with_structs_interfaces_traits (method) `def test_render_with_structs_interfaces_traits(self)`
- Defined: `tests/test_uml.py:137`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:160`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_preserves_alphanumeric (method) `def test_sanitize_preserves_alphanumeric(self)`
- Defined: `tests/test_uml.py:164`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_replaces_special_chars (method) `def test_sanitize_replaces_special_chars(self)`
- Defined: `tests/test_uml.py:168`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_prefixes_digit_start (method) `def test_sanitize_prefixes_digit_start(self)`
- Defined: `tests/test_uml.py:172`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_sanitize_handles_empty_string (method) `def test_sanitize_handles_empty_string(self)`
- Defined: `tests/test_uml.py:176`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:184`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_cpp_produces_valid_code (method) `def test_generate_cpp_produces_valid_code(self)`
- Defined: `tests/test_uml.py:188`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_cpp_with_empty_classes (method) `def test_generate_cpp_with_empty_classes(self)`
- Defined: `tests/test_uml.py:208`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_cpp_unknown_language_returns_error_message (method) `def test_generate_cpp_unknown_language_returns_error_message(self)`
- Defined: `tests/test_uml.py:223`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:242`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_java_class_produces_valid_code (method) `def test_generate_java_class_produces_valid_code(self)`
- Defined: `tests/test_uml.py:246`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_java_interface_produces_interface (method) `def test_generate_java_interface_produces_interface(self)`
- Defined: `tests/test_uml.py:265`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:284`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_csharp_produces_valid_code (method) `def test_generate_csharp_produces_valid_code(self)`
- Defined: `tests/test_uml.py:288`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:309`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_go_struct_produces_valid_code (method) `def test_generate_go_struct_produces_valid_code(self)`
- Defined: `tests/test_uml.py:313`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_go_interface_produces_valid_code (method) `def test_generate_go_interface_produces_valid_code(self)`
- Defined: `tests/test_uml.py:330`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:350`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_rust_struct_produces_valid_code (method) `def test_generate_rust_struct_produces_valid_code(self)`
- Defined: `tests/test_uml.py:354`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_rust_trait_produces_valid_code (method) `def test_generate_rust_trait_produces_valid_code(self)`
- Defined: `tests/test_uml.py:370`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:390`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_php_class_produces_valid_code (method) `def test_generate_php_class_produces_valid_code(self)`
- Defined: `tests/test_uml.py:394`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_php_interface_produces_valid_code (method) `def test_generate_php_interface_produces_valid_code(self)`
- Defined: `tests/test_uml.py:411`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### setUp (method) `def setUp(self)`
- Defined: `tests/test_uml.py:430`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### _make_class_node (method) `def _make_class_node(self, name, lang, kind)`
- Defined: `tests/test_uml.py:434`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_kotlin_produces_valid_code (method) `def test_generate_kotlin_produces_valid_code(self)`
- Defined: `tests/test_uml.py:446`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_scala_produces_valid_code (method) `def test_generate_scala_produces_valid_code(self)`
- Defined: `tests/test_uml.py:452`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_scala_trait_produces_valid_code (method) `def test_generate_scala_trait_produces_valid_code(self)`
- Defined: `tests/test_uml.py:458`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_swift_produces_valid_code (method) `def test_generate_swift_produces_valid_code(self)`
- Defined: `tests/test_uml.py:463`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_swift_protocol_produces_valid_code (method) `def test_generate_swift_protocol_produces_valid_code(self)`
- Defined: `tests/test_uml.py:469`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_dart_produces_valid_code (method) `def test_generate_dart_produces_valid_code(self)`
- Defined: `tests/test_uml.py:474`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

### test_generate_ruby_produces_valid_code (method) `def test_generate_ruby_produces_valid_code(self)`
- Defined: `tests/test_uml.py:480`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_uml.py`

## tests/test_wiki.py

### _make_node (function) `def _make_node(node_id, doc, symbols, language)`
- Defined: `tests/test_wiki.py:12`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### _make_symbol (function) `def _make_symbol(name, kind, line, doc)`
- Defined: `tests/test_wiki.py:23`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### _make_analysis (function) `def _make_analysis()`
- Defined: `tests/test_wiki.py:27`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### _make_nodes (function) `def _make_nodes()`
- Defined: `tests/test_wiki.py:41`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_config_defaults (method) `def test_config_defaults(self)`
- Defined: `tests/test_wiki.py:50`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_config_immutable (method) `def test_config_immutable(self)`
- Defined: `tests/test_wiki.py:58`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_generate_writes_all_files (method) `def test_generate_writes_all_files(self)`
- Defined: `tests/test_wiki.py:66`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_community_page_sections (method) `def test_community_page_sections(self)`
- Defined: `tests/test_wiki.py:81`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_connections_typed_with_confidence (method) `def test_connections_typed_with_confidence(self)`
- Defined: `tests/test_wiki.py:95`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_fallback_single_community_without_analysis (method) `def test_fallback_single_community_without_analysis(self)`
- Defined: `tests/test_wiki.py:115`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_report_honest_audit_sections (method) `def test_report_honest_audit_sections(self)`
- Defined: `tests/test_wiki.py:125`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_index_entry_point (method) `def test_index_entry_point(self)`
- Defined: `tests/test_wiki.py:139`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_lint_healthy_after_generate (method) `def test_lint_healthy_after_generate(self)`
- Defined: `tests/test_wiki.py:152`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_deterministic_connections (method) `def test_deterministic_connections(self)`
- Defined: `tests/test_wiki.py:161`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_privacy_mode_strips_docs (method) `def test_privacy_mode_strips_docs(self)`
- Defined: `tests/test_wiki.py:174`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_leftover_files_covered_by_orphans_community (method) `def test_leftover_files_covered_by_orphans_community(self)`
- Defined: `tests/test_wiki.py:184`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_shared_context_link_for_disconnected_communities (method) `def test_shared_context_link_for_disconnected_communities(self)`
- Defined: `tests/test_wiki.py:194`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_garbage_doc_filtered_from_definition (method) `def test_garbage_doc_filtered_from_definition(self)`
- Defined: `tests/test_wiki.py:210`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_definition_names_core_file (method) `def test_definition_names_core_file(self)`
- Defined: `tests/test_wiki.py:217`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_duplicate_community_labels_disambiguated (method) `def test_duplicate_community_labels_disambiguated(self)`
- Defined: `tests/test_wiki.py:240`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_duplicate_god_basenames_disambiguated (method) `def test_duplicate_god_basenames_disambiguated(self)`
- Defined: `tests/test_wiki.py:259`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_oversized_community_grouped_by_directory (method) `def test_oversized_community_grouped_by_directory(self)`
- Defined: `tests/test_wiki.py:278`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_large_files_flagged_in_index_and_report (method) `def test_large_files_flagged_in_index_and_report(self)`
- Defined: `tests/test_wiki.py:302`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_stale_pages_pruned_on_regenerate (method) `def test_stale_pages_pruned_on_regenerate(self)`
- Defined: `tests/test_wiki.py:323`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_risks_carry_fix_hint_scope_and_closed_cycle (method) `def test_risks_carry_fix_hint_scope_and_closed_cycle(self)`
- Defined: `tests/test_wiki.py:335`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_duplicate_symbol_scope_detected (method) `def test_duplicate_symbol_scope_detected(self)`
- Defined: `tests/test_wiki.py:365`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_no_duplicate_link_for_disjoint_scopes (method) `def test_no_duplicate_link_for_disjoint_scopes(self)`
- Defined: `tests/test_wiki.py:388`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`

### test_garbage_purpose_filtered (method) `def test_garbage_purpose_filtered(self)`
- Defined: `tests/test_wiki.py:408`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_wiki.py`
