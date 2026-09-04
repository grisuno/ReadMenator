# Subsystem: readmenator

## readmenator/__init__.py
- Layer: utility
- Language: py
- Depends on: `readmenator/_app.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_uml.py`

## readmenator/__main__.py
- Layer: testing
- Language: py
- Symbols:
  - `build_parser` (function, line 15) `def build_parser()`
  - `_run_tests` (function, line 101) `def _run_tests()`
  - `main` (function, line 116) `def main()`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
- Imported by: `readmenator.py`

## readmenator/_agent_injector.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `ensure_readmenator_installed` (function, line 96) `def ensure_readmenator_installed()`
  - `AgentInjector` (class, line 121) `class AgentInjector`
  - `__init__` (method, line 132) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs)`
  - `inject` (method, line 144) `def inject(self, project_root)`
  - `remove` (method, line 162) `def remove(self, project_root)`
  - `find_agent_files` (method, line 175) `def find_agent_files(self, project_root)`
  - `_find_agent_files` (method, line 179) `def _find_agent_files(self, root)`
  - `_inject_single` (method, line 193) `def _inject_single(self, path)`
  - `_extract_current_injection` (method, line 218) `def _extract_current_injection(content)`
  - `_remove_old_injection` (method, line 227) `def _remove_old_injection(content)`
  - `_remove_single` (method, line 237) `def _remove_single(self, path)`
  - `_build_injection` (method, line 253) `def _build_injection(self, fmt)`
- Depends on: `readmenator.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`

## readmenator/_agent_output.py
- Layer: utility
- Language: py
- Symbols:
  - `AgentOutputGenerator` (class, line 46) `class AgentOutputGenerator`
  - `__init__` (method, line 53) `def __init__(self, config)`
  - `generate` (method, line 60) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)`
  - `_infer_subsystems` (method, line 111) `def _infer_subsystems(self, nodes)`
  - `_build_index` (method, line 148) `def _build_index(self, nodes, subsystems)`
  - `_build_architecture` (method, line 178) `def _build_architecture(self, edges, resolved_edges, nodes)`
  - `_build_security` (method, line 222) `def _build_security(self, findings)`
  - `_build_api` (method, line 250) `def _build_api(self, nodes, resolved_map, imported_by)`
  - `_build_gotchas` (method, line 307) `def _build_gotchas(self, analysis, analysis_v2, nodes)`
  - `_write_subsystem_files` (method, line 376) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)`
  - `_build_subsystem_content` (method, line 395) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)`
  - `_write_recipes` (method, line 445) `def _write_recipes(self, recipes_dir, analysis, analysis_v2)`
  - `_build_resolved_map` (method, line 499) `def _build_resolved_map(resolved_edges)`
  - `_build_imported_by_map` (method, line 508) `def _build_imported_by_map(resolved_edges)`
  - `_write` (method, line 517) `def _write(path, content)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_agent_output.py`

## readmenator/_analyzer.py
- Layer: utility
- Language: py
- Symbols:
  - `GraphAnalyzer` (class, line 20) `class GraphAnalyzer`
  - `__init__` (method, line 28) `def __init__(self, config)`
  - `analyze` (method, line 36) `def analyze(self, nodes, edges, resolved_edges)`
  - `_build_adjacency` (method, line 89) `def _build_adjacency(self, nodes, edges)`
  - `_build_reverse_adjacency` (method, line 103) `def _build_reverse_adjacency(self, adjacency)`
  - `_compute_god_nodes` (method, line 113) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)`
  - `_detect_communities` (method, line 135) `def _detect_communities(self, nodes, adjacency)`
  - `_label_communities` (method, line 186) `def _label_communities(self, nodes, communities)`
  - `_build_community_map` (method, line 213) `def _build_community_map(self, communities)`
  - `_compute_cohesion` (method, line 223) `def _compute_cohesion(self, communities, adjacency)`
  - `_find_surprising_connections` (method, line 248) `def _find_surprising_connections(self, nodes, adjacency, community_map)`
  - `_shortest_path_communities` (method, line 288) `def _shortest_path_communities(self, source, target, adjacency, community_map)`
  - `_suggest_questions` (method, line 315) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_analyzer.py`

## readmenator/_app.py
- Layer: utility
- Language: py
- Symbols:
  - `readmenatorApplication` (class, line 33) `class readmenatorApplication`
  - `__init__` (method, line 34) `def __init__(self, config)`
  - `_scan` (method, line 43) `def _scan(self, target_dir)`
  - `_scan_with_content` (method, line 51) `def _scan_with_content(self, target_dir)`
  - `_resolve_imports` (method, line 61) `def _resolve_imports(self, nodes, edges, target_dir)`
  - `run` (method, line 80) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
  - `_write_sidecar_outputs` (method, line 182) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
  - `_inject_readme_link` (method, line 208) `def _inject_readme_link(self, root)`
  - `_inject_agent_files` (method, line 216) `def _inject_agent_files(self, root)`
  - `generate_uml_code` (method, line 224) `def generate_uml_code(self, target_dir, language, output_path)`
  - `_log_summary` (method, line 236) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)`
  - `update` (method, line 291) `def update(self, target_dir, run_security)`
  - `_scan_for_cache` (method, line 387) `def _scan_for_cache(self, root, cache)`
  - `query` (method, line 405) `def query(self, target_dir, question)`
  - `explain` (method, line 410) `def explain(self, target_dir, symbol_name)`
  - `find_path` (method, line 422) `def find_path(self, target_dir, symbol_a, symbol_b)`
  - `summary` (method, line 435) `def summary(self, target_dir)`
  - `rank_query` (method, line 440) `def rank_query(self, target_dir, query, top_n)`
  - `rebuild` (method, line 470) `def rebuild(self, target_dir, run_security)`
  - `analyze` (method, line 473) `def analyze(self, target_dir)`
  - `export_json` (method, line 477) `def export_json(self, target_dir, output_path)`
  - `export_html` (method, line 488) `def export_html(self, target_dir, output_path)`
  - `export_svg` (method, line 499) `def export_svg(self, target_dir, output_path)`
  - `export` (method, line 510) `def export(self, target_dir)`
  - `export_graphml` (method, line 515) `def export_graphml(self, target_dir, output_path)`
  - `export_cypher` (method, line 526) `def export_cypher(self, target_dir, output_path)`
  - `export_obsidian` (method, line 539) `def export_obsidian(self, target_dir, output_dir)`
  - `watch` (method, line 549) `def watch(self, target_dir)`
  - `audit` (method, line 559) `def audit(self, target_dir)`
  - `audit_deep` (method, line 566) `def audit_deep(self, target_dir)`
  - `export_sarif` (method, line 586) `def export_sarif(self, target_dir, output_path)`
  - `export_rules` (method, line 596) `def export_rules(self, target_dir, output_dir)`
  - `detect_layers` (method, line 606) `def detect_layers(self, target_dir)`
  - `lint` (method, line 616) `def lint(self, target_dir)`
  - `strip_dead_code` (method, line 629) `def strip_dead_code(self, target_dir)`
  - `generate_cursorrules` (method, line 639) `def generate_cursorrules(self, target_dir)`
  - `refactor_monolith` (method, line 654) `def refactor_monolith(self, target_dir)`
  - `on_change` (method, line 553) `def on_change()`
- Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_watcher.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_integration.py`, `tests/test_mcp_server.py`

## readmenator/_cache.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `FileCache` (class, line 20) `class FileCache`
  - `__init__` (method, line 31) `def __init__(self, config, project_root)`
  - `load` (method, line 38) `def load(self)`
  - `save` (method, line 49) `def save(self, hashes)`
  - `compute_hash` (method, line 55) `def compute_hash(self, file_path)`
  - `compute_hashes` (method, line 64) `def compute_hashes(self, file_paths)`
  - `find_changed` (method, line 72) `def find_changed(self, file_paths)`
  - `prune_deleted` (method, line 84) `def prune_deleted(self, current_file_ids)`
  - `save_analysis` (method, line 95) `def save_analysis(self, key, data)`
  - `load_analysis` (method, line 118) `def load_analysis(self, key)`
  - `clear_analysis` (method, line 135) `def clear_analysis(self, key)`
  - `_prune_analysis_cache` (method, line 155) `def _prune_analysis_cache(self, current_file_ids)`
  - `has_changed_since_last_analysis` (method, line 166) `def has_changed_since_last_analysis(self, file_paths)`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `tests/test_cache.py`

## readmenator/_category.py
- Layer: utility
- Language: py
- Symbols:
  - `EdgeKind` (class, line 24) `class EdgeKind(str, Enum)`
  - `Morphism` (class, line 57) `class Morphism`
  - `Category` (class, line 78) `class Category`
  - `TypedGraph` (class, line 181) `class TypedGraph`
  - `build_category_from_edges` (method, line 236) `def build_category_from_edges(edges, resolved_edges, node_ids)`
  - `_infer_edge_kind` (method, line 280) `def _infer_edge_kind(relation)`
  - `__str__` (method, line 38) `def __str__(self)`
  - `weight` (method, line 73) `def weight(self)`
  - `__init__` (method, line 86) `def __init__(self)`
  - `add_object` (method, line 92) `def add_object(self, obj_id)`
  - `add_morphism` (method, line 95) `def add_morphism(self, m)`
  - `objects` (method, line 103) `def objects(self)`
  - `morphisms` (method, line 107) `def morphisms(self)`
  - `outgoing` (method, line 110) `def outgoing(self, obj_id)`
  - `incoming` (method, line 113) `def incoming(self, obj_id)`
  - `compose` (method, line 116) `def compose(self, a, b)`
  - `paths` (method, line 133) `def paths(self, source, target, max_depth)`
  - `_compose_kind` (method, line 157) `def _compose_kind(a, b)`
  - `__init__` (method, line 188) `def __init__(self, category)`
  - `_compute_out_weights` (method, line 197) `def _compute_out_weights(self)`
  - `nodes` (method, line 203) `def nodes(self)`
  - `size` (method, line 207) `def size(self)`
  - `node_index` (method, line 210) `def node_index(self, node_id)`
  - `transition_weight` (method, line 213) `def transition_weight(self, source, target)`
  - `stochastic_row` (method, line 221) `def stochastic_row(self, source)`
  - `dfs` (method, line 139) `def dfs(current, goal, path, depth)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`

## readmenator/_config.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `Config` (class, line 15) `class Config`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/__main__.py`, `readmenator/__main__.py`, `readmenator/__main__.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_app.py`, `readmenator/_cache.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`, `readmenator/_refactorizer.py`, `readmenator/_rule_gen.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_watcher.py`, `readmenator/parsers/__init__.py`, `readmenator/parsers/_base.py`, `tests/test_agent_output.py`, `tests/test_analyzer.py`, `tests/test_cache.py`, `tests/test_config.py`, `tests/test_cpg.py`, `tests/test_cursorrules.py`, `tests/test_dead_code.py`, `tests/test_documentation.py`, `tests/test_exporter.py`, `tests/test_hotspots.py`, `tests/test_integration.py`, `tests/test_layer_rules.py`, `tests/test_linter.py`, `tests/test_mcp_server.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`, `tests/test_parsers_property.py`, `tests/test_refactorizer.py`, `tests/test_rule_gen.py`, `tests/test_sarif.py`, `tests/test_scanner.py`, `tests/test_security.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`, `tests/test_uml.py`

## readmenator/_cpg.py
- Layer: utility
- Language: py
- Symbols:
  - `CodePropertyGraph` (class, line 10) `class CodePropertyGraph`
  - `__init__` (method, line 20) `def __init__(self, privacy_mode, cpg_context)`
  - `generate` (method, line 24) `def generate(self, nodes, edges, resolved_edges, analysis, findings)`
  - `_severity_counts` (method, line 141) `def _severity_counts(self, findings)`
  - `_build_symbol_list` (method, line 147) `def _build_symbol_list(self, node)`
  - `_compute_node_hash` (method, line 163) `def _compute_node_hash(node)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`

## readmenator/_cursorrules_generator.py
- Layer: business_logic
- Language: py
- Symbols:
  - `CursorRulesGenerator` (class, line 18) `class CursorRulesGenerator`
  - `__init__` (method, line 25) `def __init__(self, config)`
  - `generate` (method, line 28) `def generate(self, nodes, edges, analysis, layers, violations, project_root)`
  - `_build_base_rules` (method, line 63) `def _build_base_rules(self)`
  - `_extract_layer_constraints` (method, line 81) `def _extract_layer_constraints(self, layers)`
  - `_extract_analysis_constraints` (method, line 92) `def _extract_analysis_constraints(self, analysis)`
  - `_extract_violation_rules` (method, line 107) `def _extract_violation_rules(self, violations)`
  - `_write_file` (method, line 115) `def _write_file(self, project_root, content)`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`

## readmenator/_dead_code.py
- Layer: utility
- Language: py
- Symbols:
  - `DeadCodeStripper` (class, line 17) `class DeadCodeStripper`
  - `__init__` (method, line 25) `def __init__(self, config)`
  - `identify` (method, line 28) `def identify(self, nodes, edges, resolved_edges)`
  - `_build_in_degree_map` (method, line 64) `def _build_in_degree_map(self, nodes, resolved_edges)`
  - `_classify_recommendation` (method, line 88) `def _classify_recommendation(self, symbol)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`

## readmenator/_documentation.py
- Layer: utility
- Language: py
- Symbols:
  - `DocumentationGenerator` (class, line 27) `class DocumentationGenerator`
  - `__init__` (method, line 39) `def __init__(self, config)`
  - `_ranking_version` (method, line 57) `def _ranking_version(self)`
  - `_get_git_commit` (method, line 75) `def _get_git_commit()`
  - `generate` (method, line 85) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)`
  - `_apply_context_budget` (method, line 158) `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)`
  - `_build_toc` (method, line 296) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)`
  - `_build_layers` (method, line 381) `def _build_layers(self, layers, nodes)`
  - `_build_dashboard` (method, line 415) `def _build_dashboard(self, nodes, edges, resolved_edges)`
  - `_build_god_nodes` (method, line 495) `def _build_god_nodes(self, analysis, ranked)`
  - `_build_community_analysis` (method, line 523) `def _build_community_analysis(self, analysis, nodes)`
  - `_build_surprising_connections` (method, line 556) `def _build_surprising_connections(self, analysis, nodes)`
  - `_build_suggested_questions` (method, line 581) `def _build_suggested_questions(self, analysis)`
  - `_build_ranked_context` (method, line 597) `def _build_ranked_context(self, ranked)`
  - `_build_orphans` (method, line 643) `def _build_orphans(self, nodes, analysis_v2, ranked)`
  - `_build_query_recipes` (method, line 693) `def _build_query_recipes(self)`
  - `_build_taint_analysis` (method, line 735) `def _build_taint_analysis(self, analysis_v2)`
  - `_build_hotspots` (method, line 770) `def _build_hotspots(self, analysis_v2, ranked)`
  - `_build_dependency_cycles` (method, line 808) `def _build_dependency_cycles(self, analysis_v2)`
  - `_build_change_impact` (method, line 828) `def _build_change_impact(self, analysis_v2)`
  - `_build_layer_violations` (method, line 853) `def _build_layer_violations(self, analysis_v2)`
  - `_build_suggested_rules` (method, line 881) `def _build_suggested_rules(self, analysis_v2)`
  - `_build_security_findings` (method, line 906) `def _build_security_findings(self, findings)`
  - `_build_mermaid_section` (method, line 953) `def _build_mermaid_section(self, graph_output, is_truncated)`
  - `_build_uml_diagram` (method, line 976) `def _build_uml_diagram(self, nodes, edges)`
  - `_build_cpg_block` (method, line 1002) `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
  - `_build_architecture_reference` (method, line 1028) `def _build_architecture_reference(self, nodes, edges)`
- Depends on: `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`

## readmenator/_explain.py
- Layer: utility
- Language: py
- Symbols:
  - `explain_rank` (function, line 16) `def explain_rank(node_id, ranked, category)`
  - `rank_summary` (function, line 140) `def rank_summary(ranked, top_n)`
  - `_find_item` (function, line 163) `def _find_item(node_id, items)`
- Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
- Imported by: `tests/test_ranking.py`

## readmenator/_exporter.py
- Layer: utility
- Language: py
- Symbols:
  - `GraphExporter` (class, line 21) `class GraphExporter`
  - `__init__` (method, line 29) `def __init__(self, config)`
  - `to_json` (method, line 37) `def to_json(self, nodes, edges, resolved_edges, analysis, findings)`
  - `to_html` (method, line 150) `def to_html(self, nodes, edges, resolved_edges, analysis, findings)`
  - `_community_color_map` (method, line 236) `def _community_color_map(self, analysis)`
  - `_lighten` (method, line 254) `def _lighten(hex_color)`
  - `_render_html` (method, line 262) `def _render_html(self, vis_nodes, vis_edges, analysis, findings)`
  - `to_svg` (method, line 421) `def to_svg(self, nodes, edges, resolved_edges, analysis)`
  - `_render_truncated_svg` (method, line 539) `def _render_truncated_svg(self, total_nodes)`
  - `_layout_spring` (method, line 554) `def _layout_spring(self, nodes, edges, node_map)`
  - `to_graphml` (method, line 635) `def to_graphml(self, nodes, edges, resolved_edges, analysis)`
  - `to_cypher` (method, line 712) `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)`
  - `to_obsidian` (method, line 817) `def to_obsidian(self, nodes, edges, output_dir, analysis)`
  - `_project` (method, line 483) `def _project(pos)`
  - `_sev_span` (method, line 334) `def _sev_span(sev, count)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`

## readmenator/_hotspots.py
- Layer: utility
- Language: py
- Symbols:
  - `HotspotAnalyzer` (class, line 16) `class HotspotAnalyzer`
  - `__init__` (method, line 25) `def __init__(self, config)`
  - `analyze_hotspots` (method, line 28) `def analyze_hotspots(self, nodes, edges, resolved_edges)`
  - `detect_cycles` (method, line 84) `def detect_cycles(self, nodes, resolved_edges)`
  - `analyze_change_impact` (method, line 149) `def analyze_change_impact(self, nodes, resolved_edges)`
  - `_dfs_visit` (method, line 108) `def _dfs_visit(current)`
  - `_record_cycle` (method, line 119) `def _record_cycle(start, end)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`

## readmenator/_layer_rules.py
- Layer: business_logic
- Language: py
- Symbols:
  - `LayerRuleEngine` (class, line 9) `class LayerRuleEngine`
  - `__init__` (method, line 34) `def __init__(self, config)`
  - `detect_violations` (method, line 37) `def detect_violations(self, nodes, edges, resolved_edges, layers)`
  - `violation_summary` (method, line 109) `def violation_summary(violations)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`

## readmenator/_layers.py
- Layer: utility
- Language: py
- Symbols:
  - `LayerDetector` (class, line 15) `class LayerDetector`
  - `detect` (method, line 71) `def detect(self, nodes, edges)`
  - `_classify_file` (method, line 89) `def _classify_file(self, node, edges)`
  - `layer_summary` (method, line 122) `def layer_summary(layers)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`

## readmenator/_linter.py
- Layer: utility
- Language: py
- Symbols:
  - `ArchitectureLinter` (class, line 18) `class ArchitectureLinter`
  - `__init__` (method, line 31) `def __init__(self, config)`
  - `lint` (method, line 34) `def lint(self, nodes, edges, resolved_edges, layers, content_map)`
  - `_check_file_length` (method, line 65) `def _check_file_length(self, nodes, content_map)`
  - `_check_cross_layer_violations` (method, line 96) `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)`
  - `_check_circular_dependencies` (method, line 127) `def _check_circular_dependencies(self, nodes, resolved_edges)`
  - `_dfs` (method, line 146) `def _dfs(current)`
- Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_linter.py`

## readmenator/_mcp_server.py
- Layer: utility
- Language: py
- Symbols:
  - `MCPError` (class, line 58) `class MCPError(Exception)`
  - `MCPRequest` (class, line 71) `class MCPRequest`
  - `MCPTool` (class, line 92) `class MCPTool`
  - `MCPResource` (class, line 119) `class MCPResource`
  - `MCPServer` (class, line 146) `class MCPServer`
  - `main` (method, line 796) `def main()`
  - `__init__` (method, line 59) `def __init__(self, code, message, data)`
  - `__init__` (method, line 72) `def __init__(self, msg)`
  - `is_notification` (method, line 79) `def is_notification(self)`
  - `response` (method, line 82) `def response(self, result)`
  - `error` (method, line 85) `def error(self, code, message, data)`
  - `__init__` (method, line 93) `def __init__(self, name, description, handler, input_schema)`
  - `definition` (method, line 108) `def definition(self)`
  - `call` (method, line 115) `def call(self, arguments)`
  - `__init__` (method, line 120) `def __init__(self, uri, name, description, mime_type, handler)`
  - `definition` (method, line 134) `def definition(self)`
  - `read` (method, line 142) `def read(self)`
  - `__init__` (method, line 147) `def __init__(self, app, target_dir)`
  - `register_tool` (method, line 155) `def register_tool(self, tool)`
  - `register_resource` (method, line 158) `def register_resource(self, resource)`
  - `_ensure_kb` (method, line 161) `def _ensure_kb(self)`
  - `_handle_initialize` (method, line 173) `def _handle_initialize(self, req)`
  - `_handle_list_tools` (method, line 187) `def _handle_list_tools(self, req)`
  - `_handle_call_tool` (method, line 192) `def _handle_call_tool(self, req)`
  - `_handle_list_resources` (method, line 214) `def _handle_list_resources(self, req)`
  - `_handle_read_resource` (method, line 219) `def _handle_read_resource(self, req)`
  - `dispatch` (method, line 241) `def dispatch(self, req)`
  - `run` (method, line 261) `def run(self)`
  - `_register_all` (method, line 285) `def _register_all(self)`
  - `_scan` (method, line 467) `def _scan(self)`
  - `_scan_deep` (method, line 473) `def _scan_deep(self)`
  - `_tool_summary` (method, line 481) `def _tool_summary(self)`
  - `_tool_query` (method, line 519) `def _tool_query(self, text)`
  - `_tool_explain` (method, line 524) `def _tool_explain(self, name)`
  - `_tool_path` (method, line 536) `def _tool_path(self, symbol_a, symbol_b)`
  - `_tool_findings` (method, line 547) `def _tool_findings(self, min_severity)`
  - `_tool_security_summary` (method, line 577) `def _tool_security_summary(self)`
  - `_tool_taint` (method, line 582) `def _tool_taint(self)`
  - `_tool_hotspots` (method, line 603) `def _tool_hotspots(self, top_n)`
  - `_tool_cycles` (method, line 619) `def _tool_cycles(self)`
  - `_tool_communities` (method, line 630) `def _tool_communities(self)`
  - `_tool_layers` (method, line 645) `def _tool_layers(self)`
  - `_tool_layer_violations` (method, line 663) `def _tool_layer_violations(self)`
  - `_tool_rebuild` (method, line 679) `def _tool_rebuild(self)`
  - `_tool_update` (method, line 689) `def _tool_update(self)`
  - `_tool_export_json` (method, line 697) `def _tool_export_json(self)`
  - `_resource_summary` (method, line 705) `def _resource_summary(self)`
  - `_resource_graph` (method, line 722) `def _resource_graph(self)`
  - `_resource_findings` (method, line 741) `def _resource_findings(self)`
  - `_resource_analysis` (method, line 757) `def _resource_analysis(self)`
  - `_resource_kb` (method, line 787) `def _resource_kb(self)`
  - `_get_query_engine` (method, line 791) `def _get_query_engine(self, nodes, edges, resolved)`
- Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`

## readmenator/_mermaid.py
- Layer: utility
- Language: py
- Symbols:
  - `MermaidRenderer` (class, line 17) `class MermaidRenderer`
  - `__init__` (method, line 26) `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)`
  - `_sanitize_id` (method, line 45) `def _sanitize_id(node_id)`
  - `render` (method, line 56) `def render(self, nodes, edges, resolved_edges, analysis)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`

## readmenator/_models.py
- Layer: business_logic
- Language: py
- Symbols:
  - `Symbol` (class, line 18) `class Symbol`
  - `Node` (class, line 37) `class Node`
  - `Edge` (class, line 58) `class Edge`
  - `SecurityFinding` (class, line 77) `class SecurityFinding`
  - `pluralize_symbol_kind` (method, line 101) `def pluralize_symbol_kind(kind, plural_map)`
  - `CommunityResult` (class, line 111) `class CommunityResult`
  - `AnalysisResult` (class, line 130) `class AnalysisResult`
  - `TaintPath` (class, line 151) `class TaintPath`
  - `TaintAnalysisResult` (class, line 172) `class TaintAnalysisResult`
  - `DependencyCycle` (class, line 187) `class DependencyCycle`
  - `ChangeImpact` (class, line 200) `class ChangeImpact`
  - `HotspotResult` (class, line 217) `class HotspotResult`
  - `SuggestedRule` (class, line 238) `class SuggestedRule`
  - `LayerViolation` (class, line 263) `class LayerViolation`
  - `AnalysisResultV2` (class, line 284) `class AnalysisResultV2`
  - `LinterViolation` (class, line 305) `class LinterViolation`
  - `DeadCodeReport` (class, line 322) `class DeadCodeReport`
  - `RefactoringAction` (class, line 339) `class RefactoringAction`
  - `RefactoringPlan` (class, line 360) `class RefactoringPlan`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_app.py`, `readmenator/_category.py`, `readmenator/_cpg.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_mermaid.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_refactorizer.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_analyzer.py`, `tests/test_cpg.py`, `tests/test_cursorrules.py`, `tests/test_dead_code.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_documentation.py`, `tests/test_exporter.py`, `tests/test_hotspots.py`, `tests/test_layer_rules.py`, `tests/test_linter.py`, `tests/test_mermaid.py`, `tests/test_models.py`, `tests/test_parsers_property.py`, `tests/test_query.py`, `tests/test_ranking.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_refactorizer.py`, `tests/test_rule_gen.py`, `tests/test_sarif.py`, `tests/test_scanner.py`, `tests/test_security.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`, `tests/test_uml.py`

## readmenator/_pipeline.py
- Layer: utility
- Language: py
- Symbols:
  - `AnalyzerFactory` (class, line 38) `class AnalyzerFactory`
  - `DeepAnalysisRunner` (class, line 207) `class DeepAnalysisRunner`
  - `__init__` (method, line 46) `def __init__(self, config)`
  - `scanner` (method, line 68) `def scanner(self)`
  - `generator` (method, line 74) `def generator(self)`
  - `analyzer` (method, line 80) `def analyzer(self)`
  - `security` (method, line 86) `def security(self)`
  - `exporter` (method, line 92) `def exporter(self)`
  - `taint` (method, line 98) `def taint(self)`
  - `hotspots` (method, line 104) `def hotspots(self)`
  - `layer_rules` (method, line 110) `def layer_rules(self)`
  - `rule_gen` (method, line 116) `def rule_gen(self)`
  - `sarif` (method, line 122) `def sarif(self)`
  - `cpg` (method, line 128) `def cpg(self)`
  - `layer_detector` (method, line 137) `def layer_detector(self)`
  - `uml` (method, line 143) `def uml(self)`
  - `readme_injector` (method, line 149) `def readme_injector(self)`
  - `agent_injector` (method, line 158) `def agent_injector(self)`
  - `agent_output` (method, line 167) `def agent_output(self)`
  - `build_typed_graph` (method, line 172) `def build_typed_graph(self, nodes, edges, resolved_edges)`
  - `make_ranker` (method, line 182) `def make_ranker(self, typed_graph)`
  - `last_category` (method, line 199) `def last_category(self)`
  - `last_typed_graph` (method, line 203) `def last_typed_graph(self)`
  - `__init__` (method, line 216) `def __init__(self, factory)`
  - `run` (method, line 219) `def run(self, nodes, edges, resolved_edges, layers, content_map)`
- Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_documentation.py`, `readmenator/_exporter.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`
- Imported by: `readmenator/_app.py`

## readmenator/_projections.py
- Layer: utility
- Language: py
- Symbols:
  - `Projection` (class, line 17) `class Projection(Protocol)`
  - `IdentityProjection` (class, line 32) `class IdentityProjection`
  - `DocProjection` (class, line 42) `class DocProjection`
  - `RiskProjection` (class, line 63) `class RiskProjection`
  - `apply_view` (method, line 95) `def apply_view(category, view_config)`
  - `map_node` (method, line 23) `def map_node(self, node)`
  - `map_morphism` (method, line 27) `def map_morphism(self, m)`
  - `map_node` (method, line 35) `def map_node(self, node)`
  - `map_morphism` (method, line 38) `def map_morphism(self, m)`
  - `__init__` (method, line 49) `def __init__(self, documented_ids)`
  - `map_node` (method, line 52) `def map_node(self, node)`
  - `map_morphism` (method, line 57) `def map_morphism(self, m)`
  - `__init__` (method, line 70) `def __init__(self, fan_in, fan_out, test_files)`
  - `map_node` (method, line 80) `def map_node(self, node)`
  - `map_morphism` (method, line 91) `def map_morphism(self, m)`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`
- Imported by: `tests/test_ranking.py`

## readmenator/_query.py
- Layer: data_access
- Language: py
- Symbols:
  - `QueryEngine` (class, line 25) `class QueryEngine`
  - `__init__` (method, line 34) `def __init__(self, nodes, edges, resolved_edges, ranker, config)`
  - `_init_default_ranker` (method, line 64) `def _init_default_ranker(self)`
  - `ranked_query` (method, line 73) `def ranked_query(self, query, top_n)`
  - `_estimate_test_coverage` (method, line 124) `def _estimate_test_coverage(self)`
  - `_estimate_doc_coverage` (method, line 150) `def _estimate_doc_coverage(self)`
  - `_build_symbol_index` (method, line 170) `def _build_symbol_index(self)`
  - `_build_import_graph` (method, line 184) `def _build_import_graph(self)`
  - `_build_resolved_graph` (method, line 200) `def _build_resolved_graph(self)`
  - `find_symbol` (method, line 220) `def find_symbol(self, name)`
  - `explain` (method, line 238) `def explain(self, name)`
  - `_find_incoming_imports` (method, line 277) `def _find_incoming_imports(self, target)`
  - `find_path` (method, line 285) `def find_path(self, symbol_a, symbol_b)`
  - `_make_bidirectional` (method, line 315) `def _make_bidirectional(graph)`
  - `_bfs_shortest_path` (method, line 331) `def _bfs_shortest_path(self, graph, start, goal)`
  - `query` (method, line 355) `def query(self, question)`
  - `summary` (method, line 411) `def summary(self)`
- Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
- Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`

## readmenator/_rank.py
- Layer: utility
- Language: py
- Symbols:
  - `RankConfig` (class, line 32) `class RankConfig`
  - `global_pagerank` (method, line 61) `def global_pagerank(graph, alpha, max_iter, tolerance)`
  - `personalized_pagerank` (method, line 119) `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)`
  - `hits` (method, line 189) `def hits(graph, max_iter, tolerance)`
  - `build_seeds_from_query` (method, line 240) `def build_seeds_from_query(query, node_ids, node_labels, symbols)`
  - `build_seeds_for_context` (method, line 286) `def build_seeds_for_context(node_ids, anchor_patterns)`
  - `RankedItem` (class, line 320) `class RankedItem`
  - `RankedResult` (class, line 349) `class RankedResult`
  - `CompositeRanker` (class, line 377) `class CompositeRanker`
  - `_format_explanation` (method, line 512) `def _format_explanation(item, result)`
  - `label` (method, line 344) `def label(self)`
  - `top` (method, line 366) `def top(self, n)`
  - `explain` (method, line 369) `def explain(self, node_id)`
  - `__init__` (method, line 385) `def __init__(self, graph, config)`
  - `_get_global_pr` (method, line 394) `def _get_global_pr(self)`
  - `rank` (method, line 404) `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)`
  - `_find_justification_paths` (method, line 486) `def _find_justification_paths(self, target, seed_ids, category, max_paths)`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`

## readmenator/_readme_injector.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `ReadmeInjector` (class, line 60) `class ReadmeInjector`
  - `__init__` (method, line 68) `def __init__(self, kb_filename, agent_output_dir)`
  - `inject` (method, line 76) `def inject(self, project_root)`
  - `_extract_current_injection` (method, line 105) `def _extract_current_injection(content)`
  - `_remove_old_injection` (method, line 114) `def _remove_old_injection(content)`
  - `remove` (method, line 124) `def remove(self, project_root)`
  - `_find_readme` (method, line 153) `def _find_readme(root)`
  - `_build_injection` (method, line 160) `def _build_injection(self, suffix)`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`

## readmenator/_refactorizer.py
- Layer: utility
- Language: py
- Symbols:
  - `MonolithRefactorizer` (class, line 24) `class MonolithRefactorizer`
  - `__init__` (method, line 32) `def __init__(self, config)`
  - `analyze` (method, line 35) `def analyze(self, nodes, edges, resolved_edges, content_map)`
  - `_get_line_count` (method, line 70) `def _get_line_count(self, file_id, content_map)`
  - `_plan_refactoring` (method, line 82) `def _plan_refactoring(self, node, edges, resolved_edges, content_map)`
  - `_group_symbols_by_kind` (method, line 126) `def _group_symbols_by_kind(self, symbols)`
  - `_suggest_target_file` (method, line 132) `def _suggest_target_file(self, source_file, kind)`
  - `_estimate_impact` (method, line 147) `def _estimate_impact(self, file_id, resolved_edges)`
  - `generate_script` (method, line 156) `def generate_script(self, plan, project_root)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`

## readmenator/_resolver.py
- Layer: utility
- Language: py
- Symbols:
  - `ImportResolver` (class, line 15) `class ImportResolver`
  - `__init__` (method, line 58) `def __init__(self, file_ids, root)`
  - `_build_stem_index` (method, line 70) `def _build_stem_index(self, file_ids)`
  - `_build_dir_index` (method, line 80) `def _build_dir_index(self, file_ids)`
  - `resolve` (method, line 97) `def resolve(self, import_str, source_file)`
  - `resolve_all` (method, line 132) `def resolve_all(self, import_str, source_file)`
  - `_resolve_relative` (method, line 148) `def _resolve_relative(self, import_str, source_file)`
  - `_resolve_extensionless` (method, line 166) `def _resolve_extensionless(self, import_str, source_file)`
  - `_resolve_directory_init` (method, line 175) `def _resolve_directory_init(self, import_str, source_file)`
  - `_resolve_module_dotpath` (method, line 185) `def _resolve_module_dotpath(self, import_str)`
  - `_resolve_stem_match` (method, line 207) `def _resolve_stem_match(self, import_str)`
- Imported by: `readmenator/_app.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

## readmenator/_rule_gen.py
- Layer: business_logic
- Language: py
- Symbols:
  - `RuleGenerator` (class, line 12) `class RuleGenerator`
  - `__init__` (method, line 88) `def __init__(self, config)`
  - `generate` (method, line 92) `def generate(self, nodes, content_map)`
  - `write_rules` (method, line 120) `def write_rules(self, rules, output_dir)`
  - `_group_by_language` (method, line 159) `def _group_by_language(self, nodes)`
  - `_analyze_language` (method, line 169) `def _analyze_language(self, lang, nodes, content_map)`
  - `_detect_antipatterns` (method, line 202) `def _detect_antipatterns(self, nodes, content_map)`
  - `_infer_language_for_rule` (method, line 248) `def _infer_language_for_rule(rule_id)`
  - `_next_rule_id` (method, line 258) `def _next_rule_id(self)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

## readmenator/_sarif.py
- Layer: utility
- Language: py
- Symbols:
  - `SarifExporter` (class, line 9) `class SarifExporter`
  - `__init__` (method, line 28) `def __init__(self, privacy_mode)`
  - `export` (method, line 31) `def export(self, findings, project_name)`
  - `_build_rule` (method, line 80) `def _build_rule(self, finding)`
  - `_build_result` (method, line 104) `def _build_result(self, finding, rule_index)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

## readmenator/_scanner.py
- Layer: utility
- Language: py
- Symbols:
  - `PolyglotScanner` (class, line 22) `class PolyglotScanner`
  - `__init__` (method, line 33) `def __init__(self, config)`
  - `_is_ignored` (method, line 42) `def _is_ignored(self, path)`
  - `_load_gitignore` (method, line 46) `def _load_gitignore(self, root)`
  - `_gitignore_glob_to_regex` (method, line 68) `def _gitignore_glob_to_regex(pattern)`
  - `_is_gitignored` (method, line 108) `def _is_gitignored(self, rel_path)`
  - `_validate_path_security` (method, line 117) `def _validate_path_security(self, path)`
  - `_check_directory_depth` (method, line 130) `def _check_directory_depth(self, path, root)`
  - `_extract_file_doc` (method, line 138) `def _extract_file_doc(self, content)`
  - `_emit_progress` (method, line 191) `def _emit_progress(self, count)`
  - `scan` (method, line 201) `def scan(self, root)`
  - `scan_with_content` (method, line 215) `def scan_with_content(self, root)`
  - `_scan_impl` (method, line 226) `def _scan_impl(self, root)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

## readmenator/_security.py
- Layer: utility
- Language: py
- Symbols:
  - `SecurityRule` (class, line 24) `class SecurityRule`
  - `_parse_minimal_yaml` (method, line 46) `def _parse_minimal_yaml(text)`
  - `_unquote` (method, line 121) `def _unquote(s)`
  - `_load_rules_from_yaml` (method, line 128) `def _load_rules_from_yaml(yaml_path)`
  - `_compile` (method, line 148) `def _compile()`
  - `_python_rules` (method, line 153) `def _python_rules()`
  - `_javascript_rules` (method, line 182) `def _javascript_rules()`
  - `_c_rules` (method, line 201) `def _c_rules()`
  - `_java_rules` (method, line 222) `def _java_rules()`
  - `_go_rules` (method, line 237) `def _go_rules()`
  - `_ruby_rules` (method, line 250) `def _ruby_rules()`
  - `_php_rules` (method, line 267) `def _php_rules()`
  - `_shell_rules` (method, line 284) `def _shell_rules()`
  - `_csharp_rules` (method, line 297) `def _csharp_rules()`
  - `_kotlin_rules` (method, line 310) `def _kotlin_rules()`
  - `_swift_rules` (method, line 321) `def _swift_rules()`
  - `_scala_rules` (method, line 332) `def _scala_rules()`
  - `_lua_rules` (method, line 343) `def _lua_rules()`
  - `_dart_rules` (method, line 354) `def _dart_rules()`
  - `_rust_rules` (method, line 365) `def _rust_rules()`
  - `_nim_rules` (method, line 376) `def _nim_rules()`
  - `_gdscript_rules` (method, line 387) `def _gdscript_rules()`
  - `_elixir_rules` (method, line 398) `def _elixir_rules()`
  - `_build_rules_from_yaml` (method, line 447) `def _build_rules_from_yaml(yaml_path)`
  - `SecurityAnalyzer` (class, line 486) `class SecurityAnalyzer`
  - `__init__` (method, line 496) `def __init__(self, config)`
  - `_resolve_rules` (method, line 500) `def _resolve_rules(self)`
  - `_meets_threshold` (method, line 509) `def _meets_threshold(self, severity)`
  - `scan` (method, line 513) `def scan(self, root)`
  - `_validate_path` (method, line 555) `def _validate_path(self, path, root)`
  - `summary` (method, line 572) `def summary(self, findings)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_security.py`

## readmenator/_taint.py
- Layer: utility
- Language: py
- Symbols:
  - `TaintAnalyzer` (class, line 10) `class TaintAnalyzer`
  - `__init__` (method, line 71) `def __init__(self, config)`
  - `analyze` (method, line 75) `def analyze(self, nodes, edges, resolved_edges)`
  - `_find_direct_sources` (method, line 134) `def _find_direct_sources(self, nodes, edges)`
  - `_propagate` (method, line 160) `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)`
  - `_build_forward_graph` (method, line 211) `def _build_forward_graph(nodes, resolved_edges)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

## readmenator/_uml.py
- Layer: utility
- Language: py
- Symbols:
  - `UmlGenerator` (class, line 32) `class UmlGenerator`
  - `_get_code_generator` (method, line 170) `def _get_code_generator(language)`
  - `_type_map_py_to_target` (method, line 188) `def _type_map_py_to_target(target, py_type_hint)`
  - `_generate_cpp` (method, line 231) `def _generate_cpp(class_symbols, nodes, edges)`
  - `_cpp_params` (method, line 257) `def _cpp_params(params)`
  - `_generate_java` (method, line 272) `def _generate_java(class_symbols, nodes, edges)`
  - `_java_params` (method, line 299) `def _java_params(params)`
  - `_generate_csharp` (method, line 314) `def _generate_csharp(class_symbols, nodes, edges)`
  - `_cs_params` (method, line 343) `def _cs_params(params)`
  - `_generate_python` (method, line 358) `def _generate_python(class_symbols, nodes, edges)`
  - `_generate_go` (method, line 393) `def _generate_go(class_symbols, nodes, edges)`
  - `_generate_rust` (method, line 420) `def _generate_rust(class_symbols, nodes, edges)`
  - `_generate_php` (method, line 446) `def _generate_php(class_symbols, nodes, edges)`
  - `_generate_kotlin` (method, line 474) `def _generate_kotlin(class_symbols, nodes, edges)`
  - `_generate_scala` (method, line 494) `def _generate_scala(class_symbols, nodes, edges)`
  - `_generate_swift` (method, line 516) `def _generate_swift(class_symbols, nodes, edges)`
  - `_generate_dart` (method, line 545) `def _generate_dart(class_symbols, nodes, edges)`
  - `_generate_ruby` (method, line 565) `def _generate_ruby(class_symbols, nodes, edges)`
  - `_safe_name` (method, line 586) `def _safe_name(name)`
  - `_extract_params` (method, line 590) `def _extract_params(signature)`
  - `__init__` (method, line 34) `def __init__(self, config)`
  - `render_mermaid_class_diagram` (method, line 37) `def render_mermaid_class_diagram(self, nodes, edges)`
  - `generate_code` (method, line 127) `def generate_code(self, nodes, edges, target_language)`
  - `_sanitize_id` (method, line 151) `def _sanitize_id(raw)`
  - `_find_node` (method, line 163) `def _find_node(nodes, node_id)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

## readmenator/_watcher.py
- Layer: utility
- Language: py
- Symbols:
  - `DirectoryWatcher` (class, line 21) `class DirectoryWatcher`
  - `__init__` (method, line 29) `def __init__(self, root, config, callback, interval_seconds)`
  - `_compute_snapshot` (method, line 51) `def _compute_snapshot(self)`
  - `start` (method, line 80) `def start(self)`
  - `stop` (method, line 97) `def stop(self)`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`
