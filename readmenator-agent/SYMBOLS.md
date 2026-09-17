# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_run_tests` | function | `readmenator/__main__.py:107` | `def _run_tests()` |
| `build_parser` | function | `readmenator/__main__.py:16` | `def build_parser()` |
| `main` | function | `readmenator/__main__.py:122` | `def main()` |
| `AgentInjector` | class | `readmenator/_agent_injector.py:136` | `class AgentInjector` |
| `__init__` | method | `readmenator/_agent_injector.py:147` | `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)` |
| `_build_injection` | method | `readmenator/_agent_injector.py:283` | `def _build_injection(self, fmt)` |
| `_build_mdc_injection` | method | `readmenator/_agent_injector.py:295` | `def _build_mdc_injection(self)` |
| `_extract_current_injection` | method | `readmenator/_agent_injector.py:248` | `def _extract_current_injection(content)` |
| `_find_agent_files` | method | `readmenator/_agent_injector.py:196` | `def _find_agent_files(self, root)` |
| `_inject_single` | method | `readmenator/_agent_injector.py:210` | `def _inject_single(self, path)` |
| `_prepend_mdc_frontmatter` | method | `readmenator/_agent_injector.py:300` | `def _prepend_mdc_frontmatter(content, injection)` |
| `_remove_old_injection` | method | `readmenator/_agent_injector.py:257` | `def _remove_old_injection(content)` |
| `_remove_single` | method | `readmenator/_agent_injector.py:267` | `def _remove_single(self, path)` |
| `ensure_readmenator_installed` | function | `readmenator/_agent_injector.py:111` | `def ensure_readmenator_installed()` |
| `find_agent_files` | method | `readmenator/_agent_injector.py:192` | `def find_agent_files(self, project_root)` |
| `inject` | method | `readmenator/_agent_injector.py:161` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_agent_injector.py:179` | `def remove(self, project_root)` |
| `AgentOutputGenerator` | class | `readmenator/_agent_output.py:47` | `class AgentOutputGenerator` |
| `__init__` | method | `readmenator/_agent_output.py:54` | `def __init__(self, config)` |
| `_build_api` | method | `readmenator/_agent_output.py:276` | `def _build_api(self, nodes, resolved_map, imported_by)` |
| `_build_architecture` | method | `readmenator/_agent_output.py:183` | `def _build_architecture(self, edges, resolved_edges, nodes)` |
| `_build_gotchas` | method | `readmenator/_agent_output.py:387` | `def _build_gotchas(self, analysis, analysis_v2, nodes)` |
| `_build_imported_by_map` | method | `readmenator/_agent_output.py:646` | `def _build_imported_by_map(resolved_edges)` |
| `_build_index` | method | `readmenator/_agent_output.py:153` | `def _build_index(self, nodes, subsystems)` |
| `_build_manifest` | method | `readmenator/_agent_output.py:331` | `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root)` |
| `_build_resolved_map` | method | `readmenator/_agent_output.py:637` | `def _build_resolved_map(resolved_edges)` |
| `_build_security` | method | `readmenator/_agent_output.py:227` | `def _build_security(self, findings, nodes)` |
| `_build_subsystem_content` | method | `readmenator/_agent_output.py:488` | `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)` |
| `_build_symbols` | method | `readmenator/_agent_output.py:370` | `def _build_symbols(self, nodes)` |
| `_enclosing_symbol` | method | `readmenator/_agent_output.py:257` | `def _enclosing_symbol(nodes, file_path, line)` |
| `_infer_subsystems` | method | `readmenator/_agent_output.py:116` | `def _infer_subsystems(self, nodes)` |
| `_write` | method | `readmenator/_agent_output.py:655` | `def _write(path, content)` |
| `_write_recipes` | method | `readmenator/_agent_output.py:538` | `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings)` |
| `_write_subsystem_files` | method | `readmenator/_agent_output.py:469` | `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)` |
| `generate` | method | `readmenator/_agent_output.py:61` | `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` |
| `GraphAnalyzer` | class | `readmenator/_analyzer.py:39` | `class GraphAnalyzer` |
| `__init__` | method | `readmenator/_analyzer.py:47` | `def __init__(self, config)` |
| `_build_adjacency` | method | `readmenator/_analyzer.py:108` | `def _build_adjacency(self, nodes, edges)` |
| `_build_community_map` | method | `readmenator/_analyzer.py:226` | `def _build_community_map(self, communities)` |
| `_build_reverse_adjacency` | method | `readmenator/_analyzer.py:122` | `def _build_reverse_adjacency(self, adjacency)` |
| `_compute_cohesion` | method | `readmenator/_analyzer.py:236` | `def _compute_cohesion(self, communities, adjacency)` |
| `_compute_god_nodes` | method | `readmenator/_analyzer.py:132` | `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` |
| `_detect_communities` | method | `readmenator/_analyzer.py:154` | `def _detect_communities(self, nodes, adjacency)` |
| `_find_surprising_connections` | method | `readmenator/_analyzer.py:261` | `def _find_surprising_connections(self, nodes, adjacency, community_map)` |
| `_label_communities` | method | `readmenator/_analyzer.py:209` | `def _label_communities(self, nodes, communities)` |
| `_shortest_path_communities` | method | `readmenator/_analyzer.py:301` | `def _shortest_path_communities(self, source, target, adjacency, community_map)` |
| `_suggest_questions` | method | `readmenator/_analyzer.py:328` | `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)` |
| `analyze` | method | `readmenator/_analyzer.py:55` | `def analyze(self, nodes, edges, resolved_edges)` |
| `dominant_directory` | function | `readmenator/_analyzer.py:21` | `def dominant_directory(file_ids)` |
| `__init__` | method | `readmenator/_app.py:36` | `def __init__(self, config)` |
| `_inject_agent_files` | method | `readmenator/_app.py:233` | `def _inject_agent_files(self, root)` |
| `_inject_readme_link` | method | `readmenator/_app.py:225` | `def _inject_readme_link(self, root)` |
| `_live_renderer` | method | `readmenator/_app.py:655` | `def _live_renderer(self)` |
| `_log_summary` | method | `readmenator/_app.py:253` | `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)` |
| `_resolve_imports` | method | `readmenator/_app.py:63` | `def _resolve_imports(self, nodes, edges, target_dir)` |
| `_scan` | method | `readmenator/_app.py:45` | `def _scan(self, target_dir)` |
| `_scan_for_cache` | method | `readmenator/_app.py:413` | `def _scan_for_cache(self, root, cache)` |
| `_scan_with_content` | method | `readmenator/_app.py:53` | `def _scan_with_content(self, target_dir)` |
| `_write_sidecar_outputs` | method | `readmenator/_app.py:199` | `def _write_sidecar_outputs(self, root, findings, analysis_v2)` |
| `analyze` | method | `readmenator/_app.py:499` | `def analyze(self, target_dir)` |
| `audit` | method | `readmenator/_app.py:748` | `def audit(self, target_dir)` |
| `audit_deep` | method | `readmenator/_app.py:755` | `def audit_deep(self, target_dir)` |
| `detect_layers` | method | `readmenator/_app.py:795` | `def detect_layers(self, target_dir)` |
| `explain` | method | `readmenator/_app.py:436` | `def explain(self, target_dir, symbol_name)` |
| `export` | method | `readmenator/_app.py:536` | `def export(self, target_dir)` |
| `export_cypher` | method | `readmenator/_app.py:552` | `def export_cypher(self, target_dir, output_path)` |
| `export_diagram` | method | `readmenator/_app.py:665` | `def export_diagram(self, target_dir, kind, output_path)` |
| `export_diagrams` | method | `readmenator/_app.py:616` | `def export_diagrams(self, target_dir, output_dir)` |
| `export_graphml` | method | `readmenator/_app.py:541` | `def export_graphml(self, target_dir, output_path)` |
| `export_html` | method | `readmenator/_app.py:514` | `def export_html(self, target_dir, output_path)` |
| `export_json` | method | `readmenator/_app.py:503` | `def export_json(self, target_dir, output_path)` |
| `export_obsidian` | method | `readmenator/_app.py:565` | `def export_obsidian(self, target_dir, output_dir)` |
| `export_pages` | method | `readmenator/_app.py:702` | `def export_pages(self, target_dir, output_dir)` |
| `export_rules` | method | `readmenator/_app.py:785` | `def export_rules(self, target_dir, output_dir)` |
| `export_sarif` | method | `readmenator/_app.py:775` | `def export_sarif(self, target_dir, output_path)` |
| `export_svg` | method | `readmenator/_app.py:525` | `def export_svg(self, target_dir, output_path)` |
| `export_wiki` | method | `readmenator/_app.py:575` | `def export_wiki(self, target_dir, output_dir)` |
| `find_path` | method | `readmenator/_app.py:448` | `def find_path(self, target_dir, symbol_a, symbol_b)` |
| `generate_cursorrules` | method | `readmenator/_app.py:828` | `def generate_cursorrules(self, target_dir)` |
| `generate_uml_code` | method | `readmenator/_app.py:241` | `def generate_uml_code(self, target_dir, language, output_path)` |
| `lint` | method | `readmenator/_app.py:805` | `def lint(self, target_dir)` |
| `lint_wiki` | method | `readmenator/_app.py:598` | `def lint_wiki(self, target_dir)` |
| `on_change` | method | `readmenator/_app.py:742` | `def on_change()` |
| `query` | method | `readmenator/_app.py:431` | `def query(self, target_dir, question)` |
| `rank_query` | method | `readmenator/_app.py:466` | `def rank_query(self, target_dir, query, top_n)` |
| `readmenatorApplication` | class | `readmenator/_app.py:35` | `class readmenatorApplication` |
| `rebuild` | method | `readmenator/_app.py:496` | `def rebuild(self, target_dir, run_security)` |
| `refactor_monolith` | method | `readmenator/_app.py:843` | `def refactor_monolith(self, target_dir)` |
| `run` | method | `readmenator/_app.py:82` | `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)` |
| `strip_dead_code` | method | `readmenator/_app.py:818` | `def strip_dead_code(self, target_dir)` |
| `summary` | method | `readmenator/_app.py:461` | `def summary(self, target_dir)` |
| `update` | method | `readmenator/_app.py:308` | `def update(self, target_dir, run_security)` |
| `watch` | method | `readmenator/_app.py:738` | `def watch(self, target_dir)` |
| `FileCache` | class | `readmenator/_cache.py:20` | `class FileCache` |
| `__init__` | method | `readmenator/_cache.py:31` | `def __init__(self, config, project_root)` |
| `_prune_analysis_cache` | method | `readmenator/_cache.py:155` | `def _prune_analysis_cache(self, current_file_ids)` |
| `clear_analysis` | method | `readmenator/_cache.py:135` | `def clear_analysis(self, key)` |
| `compute_hash` | method | `readmenator/_cache.py:55` | `def compute_hash(self, file_path)` |
| `compute_hashes` | method | `readmenator/_cache.py:64` | `def compute_hashes(self, file_paths)` |
| `find_changed` | method | `readmenator/_cache.py:72` | `def find_changed(self, file_paths)` |
| `has_changed_since_last_analysis` | method | `readmenator/_cache.py:166` | `def has_changed_since_last_analysis(self, file_paths)` |
| `load` | method | `readmenator/_cache.py:38` | `def load(self)` |
| `load_analysis` | method | `readmenator/_cache.py:118` | `def load_analysis(self, key)` |
| `prune_deleted` | method | `readmenator/_cache.py:84` | `def prune_deleted(self, current_file_ids)` |
| `save` | method | `readmenator/_cache.py:49` | `def save(self, hashes)` |
| `save_analysis` | method | `readmenator/_cache.py:95` | `def save_analysis(self, key, data)` |
| `Category` | class | `readmenator/_category.py:78` | `class Category` |
| `EdgeKind` | class | `readmenator/_category.py:24` | `class EdgeKind(str, Enum)` |
| `Morphism` | class | `readmenator/_category.py:57` | `class Morphism` |
| `TypedGraph` | class | `readmenator/_category.py:181` | `class TypedGraph` |
| `__init__` | method | `readmenator/_category.py:86` | `def __init__(self)` |
| `__init__` | method | `readmenator/_category.py:188` | `def __init__(self, category)` |
| `__str__` | method | `readmenator/_category.py:38` | `def __str__(self)` |
| `_compose_kind` | method | `readmenator/_category.py:157` | `def _compose_kind(a, b)` |
| `_compute_out_weights` | method | `readmenator/_category.py:197` | `def _compute_out_weights(self)` |
| `_infer_edge_kind` | method | `readmenator/_category.py:280` | `def _infer_edge_kind(relation)` |
| `add_morphism` | method | `readmenator/_category.py:95` | `def add_morphism(self, m)` |
| `add_object` | method | `readmenator/_category.py:92` | `def add_object(self, obj_id)` |
| `build_category_from_edges` | method | `readmenator/_category.py:236` | `def build_category_from_edges(edges, resolved_edges, node_ids)` |
| `compose` | method | `readmenator/_category.py:116` | `def compose(self, a, b)` |
| `dfs` | method | `readmenator/_category.py:139` | `def dfs(current, goal, path, depth)` |
| `incoming` | method | `readmenator/_category.py:113` | `def incoming(self, obj_id)` |
| `morphisms` | method | `readmenator/_category.py:107` | `def morphisms(self)` |
| `node_index` | method | `readmenator/_category.py:210` | `def node_index(self, node_id)` |
| `nodes` | method | `readmenator/_category.py:203` | `def nodes(self)` |
| `objects` | method | `readmenator/_category.py:103` | `def objects(self)` |
| `outgoing` | method | `readmenator/_category.py:110` | `def outgoing(self, obj_id)` |
| `paths` | method | `readmenator/_category.py:133` | `def paths(self, source, target, max_depth)` |
| `size` | method | `readmenator/_category.py:207` | `def size(self)` |
| `stochastic_row` | method | `readmenator/_category.py:221` | `def stochastic_row(self, source)` |
| `transition_weight` | method | `readmenator/_category.py:213` | `def transition_weight(self, source, target)` |
| `weight` | method | `readmenator/_category.py:73` | `def weight(self)` |
| `Config` | class | `readmenator/_config.py:15` | `class Config` |
| `CodePropertyGraph` | class | `readmenator/_cpg.py:10` | `class CodePropertyGraph` |
| `__init__` | method | `readmenator/_cpg.py:20` | `def __init__(self, privacy_mode, cpg_context)` |
| `_build_symbol_list` | method | `readmenator/_cpg.py:147` | `def _build_symbol_list(self, node)` |
| `_compute_node_hash` | method | `readmenator/_cpg.py:163` | `def _compute_node_hash(node)` |
| `_severity_counts` | method | `readmenator/_cpg.py:141` | `def _severity_counts(self, findings)` |
| `generate` | method | `readmenator/_cpg.py:24` | `def generate(self, nodes, edges, resolved_edges, analysis, findings)` |
| `CursorRulesGenerator` | class | `readmenator/_cursorrules_generator.py:18` | `class CursorRulesGenerator` |
| `__init__` | method | `readmenator/_cursorrules_generator.py:25` | `def __init__(self, config)` |
| `_build_base_rules` | method | `readmenator/_cursorrules_generator.py:63` | `def _build_base_rules(self)` |
| `_extract_analysis_constraints` | method | `readmenator/_cursorrules_generator.py:92` | `def _extract_analysis_constraints(self, analysis)` |
| `_extract_layer_constraints` | method | `readmenator/_cursorrules_generator.py:81` | `def _extract_layer_constraints(self, layers)` |
| `_extract_violation_rules` | method | `readmenator/_cursorrules_generator.py:107` | `def _extract_violation_rules(self, violations)` |
| `_write_file` | method | `readmenator/_cursorrules_generator.py:115` | `def _write_file(self, project_root, content)` |
| `generate` | method | `readmenator/_cursorrules_generator.py:28` | `def generate(self, nodes, edges, analysis, layers, violations, project_root)` |
| `DataflowAnalyzer` | class | `readmenator/_dataflow.py:122` | `class DataflowAnalyzer` |
| `__init__` | method | `readmenator/_dataflow.py:125` | `def __init__(self, config)` |
| `_analyze_function` | method | `readmenator/_dataflow.py:191` | `def _analyze_function(self, file_id, func, lines, start, end)` |
| `_blank` | method | `readmenator/_dataflow.py:110` | `def _blank(match)` |
| `_brace_depths` | method | `readmenator/_dataflow.py:153` | `def _brace_depths(lines)` |
| `_function_spans` | method | `readmenator/_dataflow.py:164` | `def _function_spans(self, node, total_lines, depths)` |
| `_is_member` | method | `readmenator/_dataflow.py:521` | `def _is_member(line, pos)` |
| `_is_prototype` | method | `readmenator/_dataflow.py:535` | `def _is_prototype(line)` |
| `_member_base` | method | `readmenator/_dataflow.py:527` | `def _member_base(line, pos)` |
| `_mentions_param` | method | `readmenator/_dataflow.py:513` | `def _mentions_param(text, params)` |
| `_null_checked` | method | `readmenator/_dataflow.py:540` | `def _null_checked(body_text, name)` |
| `_params_of` | method | `readmenator/_dataflow.py:474` | `def _params_of(signature_line)` |
| `_scan_array_args` | method | `readmenator/_dataflow.py:461` | `def _scan_array_args(line, lineno, arrays, assigned)` |
| `_scan_inline_aliases` | method | `readmenator/_dataflow.py:427` | `def _scan_inline_aliases(line, lineno, arrays, derived_alias, deriv_reads)` |
| `_scan_out_params` | method | `readmenator/_dataflow.py:450` | `def _scan_out_params(line, lineno, assigned)` |
| `_scan_reads` | method | `readmenator/_dataflow.py:403` | `def _scan_reads(text, lineno, reads, assigned, declared_names)` |
| `_strip_block_comments` | function | `readmenator/_dataflow.py:107` | `def _strip_block_comments(content)` |
| `_strip_noise` | function | `readmenator/_dataflow.py:96` | `def _strip_noise(line)` |
| `_strip_sizeof` | function | `readmenator/_dataflow.py:116` | `def _strip_sizeof(line)` |
| `_track_call_continuation` | method | `readmenator/_dataflow.py:494` | `def _track_call_continuation(line, call_open, paren_balance)` |
| `analyze` | method | `readmenator/_dataflow.py:129` | `def analyze(self, nodes, content_map)` |
| `DeadCodeStripper` | class | `readmenator/_dead_code.py:17` | `class DeadCodeStripper` |
| `__init__` | method | `readmenator/_dead_code.py:25` | `def __init__(self, config)` |
| `_build_in_degree_map` | method | `readmenator/_dead_code.py:64` | `def _build_in_degree_map(self, nodes, resolved_edges)` |
| `_classify_recommendation` | method | `readmenator/_dead_code.py:88` | `def _classify_recommendation(self, symbol)` |
| `identify` | method | `readmenator/_dead_code.py:28` | `def identify(self, nodes, edges, resolved_edges)` |
| `DocsSitePublisher` | class | `readmenator/_diagrams.py:2552` | `class DocsSitePublisher` |
| `InteractiveMapRenderer` | class | `readmenator/_diagrams.py:1338` | `class InteractiveMapRenderer` |
| `MapDelta` | class | `readmenator/_diagrams.py:182` | `class MapDelta` |
| `MapDiagnostic` | class | `readmenator/_diagrams.py:148` | `class MapDiagnostic` |
| `MapEdge` | class | `readmenator/_diagrams.py:93` | `class MapEdge` |
| `MapNode` | class | `readmenator/_diagrams.py:62` | `class MapNode` |
| `MapReceipt` | class | `readmenator/_diagrams.py:165` | `class MapReceipt` |
| `MapView` | class | `readmenator/_diagrams.py:110` | `class MapView` |
| `SystemMap` | class | `readmenator/_diagrams.py:127` | `class SystemMap` |
| `SystemMapBuilder` | class | `readmenator/_diagrams.py:403` | `class SystemMapBuilder` |
| `SystemMapValidator` | class | `readmenator/_diagrams.py:202` | `class SystemMapValidator` |
| `VisNetworkRenderer` | class | `readmenator/_diagrams.py:2031` | `class VisNetworkRenderer` |
| `__init__` | method | `readmenator/_diagrams.py:205` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:432` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:1341` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:2039` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:2569` | `def __init__(self, config)` |
| `_build_architecture` | method | `readmenator/_diagrams.py:965` | `def _build_architecture(self, nodes, links, layers, findings, analysis)` |
| `_build_dataflow` | method | `readmenator/_diagrams.py:1167` | `def _build_dataflow(self, nodes, links, layers, findings)` |
| `_build_lifecycle` | method | `readmenator/_diagrams.py:1248` | `def _build_lifecycle(self, nodes, links, layers, findings)` |
| `_build_sequence` | method | `readmenator/_diagrams.py:1096` | `def _build_sequence(self, nodes, links, layers, analysis)` |
| `_build_workflow` | method | `readmenator/_diagrams.py:1023` | `def _build_workflow(self, nodes, links, layers, findings)` |
| `_cap_lane_scope` | method | `readmenator/_diagrams.py:815` | `def _cap_lane_scope(self, ranked, layer_of)` |
| `_card` | method | `readmenator/_diagrams.py:2759` | `def _card(self, kind, system_map, href_prefix)` |
| `_edge_path` | method | `readmenator/_diagrams.py:1502` | `def _edge_path(self, x1, y1, x2, y2)` |
| `_edges_svg` | method | `readmenator/_diagrams.py:1586` | `def _edges_svg(self, system_map)` |
| `_escape` | method | `readmenator/_diagrams.py:1480` | `def _escape(self, value)` |
| `_escape` | method | `readmenator/_diagrams.py:2809` | `def _escape(self, value)` |
| `_escape_markup` | function | `readmenator/_diagrams.py:24` | `def _escape_markup(value)` |
| `_fitted_gap` | method | `readmenator/_diagrams.py:777` | `def _fitted_gap(self, count, item, gap, total, margin)` |
| `_href_prefix` | method | `readmenator/_diagrams.py:2748` | `def _href_prefix(self)` |
| `_internal_links` | method | `readmenator/_diagrams.py:657` | `def _internal_links(self, edges, selected)` |
| `_json_payload` | function | `readmenator/_diagrams.py:36` | `def _json_payload(payload)` |
| `_lane_capacity` | method | `readmenator/_diagrams.py:801` | `def _lane_capacity(self)` |
| `_lanes_that_fit` | method | `readmenator/_diagrams.py:760` | `def _lanes_that_fit(self, lanes)` |
| `_layout_columns` | method | `readmenator/_diagrams.py:714` | `def _layout_columns(self, items, kind)` |
| `_layout_sequence` | method | `readmenator/_diagrams.py:839` | `def _layout_sequence(self, ordered)` |
| `_make_views` | method | `readmenator/_diagrams.py:893` | `def _make_views(self, kind, primary, links)` |
| `_nodes_svg` | method | `readmenator/_diagrams.py:1538` | `def _nodes_svg(self, system_map)` |
| `_place` | method | `readmenator/_diagrams.py:874` | `def _place(self, ranked, layer_of, kind)` |
| `_ranked_file_ids` | method | `readmenator/_diagrams.py:600` | `def _ranked_file_ids(self, nodes, links, analysis)` |
| `_role_color` | function | `readmenator/_diagrams.py:48` | `def _role_color(role, config)` |
| `_role_color` | method | `readmenator/_diagrams.py:1491` | `def _role_color(self, role)` |
| `_role_for` | method | `readmenator/_diagrams.py:566` | `def _role_for(self, group, sensitive)` |
| `_safe_json` | method | `readmenator/_diagrams.py:1469` | `def _safe_json(self, payload)` |
| `_select_primary` | method | `readmenator/_diagrams.py:635` | `def _select_primary(self, nodes, links, analysis)` |
| `_sensitive_files` | method | `readmenator/_diagrams.py:583` | `def _sensitive_files(self, findings)` |
| `_sequence_capacity` | method | `readmenator/_diagrams.py:860` | `def _sequence_capacity(self)` |
| `_short_label` | method | `readmenator/_diagrams.py:699` | `def _short_label(self, value)` |
| `_stats_line` | method | `readmenator/_diagrams.py:2795` | `def _stats_line(self, stats)` |
| `_symbol_records` | method | `readmenator/_diagrams.py:677` | `def _symbol_records(self, node)` |
| `_template` | method | `readmenator/_diagrams.py:1633` | `def _template(self)` |
| `_template` | method | `readmenator/_diagrams.py:2196` | `def _template(self)` |
| `_title_for` | method | `readmenator/_diagrams.py:552` | `def _title_for(self, kind)` |
| `_tooltip` | method | `readmenator/_diagrams.py:2165` | `def _tooltip(self, node)` |
| `build` | method | `readmenator/_diagrams.py:449` | `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind)` |
| `build_all` | method | `readmenator/_diagrams.py:484` | `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis)` |
| `compare` | method | `readmenator/_diagrams.py:513` | `def compare(self, base, head)` |
| `description_for` | method | `readmenator/_diagrams.py:2579` | `def description_for(self, kind)` |
| `publish` | method | `readmenator/_diagrams.py:2593` | `def publish(self, maps, project_name, output_dir, stats, renderer)` |
| `render` | method | `readmenator/_diagrams.py:1349` | `def render(self, system_map)` |
| `render` | method | `readmenator/_diagrams.py:2047` | `def render(self, system_map)` |
| `render_index` | method | `readmenator/_diagrams.py:2651` | `def render_index(self, project_name, maps, stats, href_prefix)` |
| `supported_kinds` | method | `readmenator/_diagrams.py:441` | `def supported_kinds(self)` |
| `validate` | method | `readmenator/_diagrams.py:213` | `def validate(self, system_map)` |
| `write` | method | `readmenator/_diagrams.py:1450` | `def write(self, system_map, output_path)` |
| `write` | method | `readmenator/_diagrams.py:2148` | `def write(self, system_map, output_path)` |
| `DocumentationGenerator` | class | `readmenator/_documentation.py:27` | `class DocumentationGenerator` |
| `__init__` | method | `readmenator/_documentation.py:39` | `def __init__(self, config)` |
| `_apply_context_budget` | method | `readmenator/_documentation.py:172` | `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)` |
| `_build_architecture_reference` | method | `readmenator/_documentation.py:1077` | `def _build_architecture_reference(self, nodes, edges)` |
| `_build_change_impact` | method | `readmenator/_documentation.py:877` | `def _build_change_impact(self, analysis_v2)` |
| `_build_community_analysis` | method | `readmenator/_documentation.py:540` | `def _build_community_analysis(self, analysis, nodes)` |
| `_build_cpg_block` | method | `readmenator/_documentation.py:1051` | `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)` |
| `_build_dashboard` | method | `readmenator/_documentation.py:432` | `def _build_dashboard(self, nodes, edges, resolved_edges)` |
| `_build_dataflow_analysis` | method | `readmenator/_documentation.py:825` | `def _build_dataflow_analysis(self, analysis_v2)` |
| `_build_dependency_cycles` | method | `readmenator/_documentation.py:856` | `def _build_dependency_cycles(self, analysis_v2)` |
| `_build_god_nodes` | method | `readmenator/_documentation.py:512` | `def _build_god_nodes(self, analysis, ranked)` |
| `_build_hotspots` | method | `readmenator/_documentation.py:787` | `def _build_hotspots(self, analysis_v2, ranked)` |
| `_build_layer_violations` | method | `readmenator/_documentation.py:902` | `def _build_layer_violations(self, analysis_v2)` |
| `_build_layers` | method | `readmenator/_documentation.py:398` | `def _build_layers(self, layers, nodes)` |
| `_build_mermaid_section` | method | `readmenator/_documentation.py:1002` | `def _build_mermaid_section(self, graph_output, is_truncated)` |
| `_build_orphans` | method | `readmenator/_documentation.py:660` | `def _build_orphans(self, nodes, analysis_v2, ranked)` |
| `_build_query_recipes` | method | `readmenator/_documentation.py:710` | `def _build_query_recipes(self)` |
| `_build_ranked_context` | method | `readmenator/_documentation.py:614` | `def _build_ranked_context(self, ranked)` |
| `_build_security_findings` | method | `readmenator/_documentation.py:955` | `def _build_security_findings(self, findings)` |
| `_build_suggested_questions` | method | `readmenator/_documentation.py:598` | `def _build_suggested_questions(self, analysis)` |
| `_build_suggested_rules` | method | `readmenator/_documentation.py:930` | `def _build_suggested_rules(self, analysis_v2)` |
| `_build_surprising_connections` | method | `readmenator/_documentation.py:573` | `def _build_surprising_connections(self, analysis, nodes)` |
| `_build_taint_analysis` | method | `readmenator/_documentation.py:752` | `def _build_taint_analysis(self, analysis_v2)` |
| `_build_toc` | method | `readmenator/_documentation.py:310` | `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)` |
| `_build_uml_diagram` | method | `readmenator/_documentation.py:1025` | `def _build_uml_diagram(self, nodes, edges)` |
| `_get_git_commit` | method | `readmenator/_documentation.py:75` | `def _get_git_commit()` |
| `_ranking_version` | method | `readmenator/_documentation.py:57` | `def _ranking_version(self)` |
| `generate` | method | `readmenator/_documentation.py:85` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)` |
| `_find_item` | function | `readmenator/_explain.py:163` | `def _find_item(node_id, items)` |
| `explain_rank` | function | `readmenator/_explain.py:16` | `def explain_rank(node_id, ranked, category)` |
| `rank_summary` | function | `readmenator/_explain.py:140` | `def rank_summary(ranked, top_n)` |
| `GraphExporter` | class | `readmenator/_exporter.py:21` | `class GraphExporter` |
| `__init__` | method | `readmenator/_exporter.py:29` | `def __init__(self, config)` |
| `_community_color_map` | method | `readmenator/_exporter.py:239` | `def _community_color_map(self, analysis)` |
| `_layout_spring` | method | `readmenator/_exporter.py:569` | `def _layout_spring(self, nodes, edges, node_map)` |
| `_lighten` | method | `readmenator/_exporter.py:257` | `def _lighten(hex_color)` |
| `_project` | method | `readmenator/_exporter.py:498` | `def _project(pos)` |
| `_render_html` | method | `readmenator/_exporter.py:265` | `def _render_html(self, vis_nodes, vis_edges, analysis, findings)` |
| `_render_truncated_svg` | method | `readmenator/_exporter.py:554` | `def _render_truncated_svg(self, total_nodes)` |
| `_sev_span` | method | `readmenator/_exporter.py:337` | `def _sev_span(sev, count)` |
| `to_cypher` | method | `readmenator/_exporter.py:727` | `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)` |
| `to_graphml` | method | `readmenator/_exporter.py:650` | `def to_graphml(self, nodes, edges, resolved_edges, analysis)` |
| `to_html` | method | `readmenator/_exporter.py:150` | `def to_html(self, nodes, edges, resolved_edges, analysis, findings)` |
| `to_json` | method | `readmenator/_exporter.py:37` | `def to_json(self, nodes, edges, resolved_edges, analysis, findings)` |
| `to_obsidian` | method | `readmenator/_exporter.py:832` | `def to_obsidian(self, nodes, edges, output_dir, analysis)` |
| `to_svg` | method | `readmenator/_exporter.py:436` | `def to_svg(self, nodes, edges, resolved_edges, analysis)` |
| `HotspotAnalyzer` | class | `readmenator/_hotspots.py:16` | `class HotspotAnalyzer` |
| `__init__` | method | `readmenator/_hotspots.py:25` | `def __init__(self, config)` |
| `_dfs_visit` | method | `readmenator/_hotspots.py:108` | `def _dfs_visit(current)` |
| `_record_cycle` | method | `readmenator/_hotspots.py:119` | `def _record_cycle(start, end)` |
| `analyze_change_impact` | method | `readmenator/_hotspots.py:149` | `def analyze_change_impact(self, nodes, resolved_edges)` |
| `analyze_hotspots` | method | `readmenator/_hotspots.py:28` | `def analyze_hotspots(self, nodes, edges, resolved_edges)` |
| `detect_cycles` | method | `readmenator/_hotspots.py:84` | `def detect_cycles(self, nodes, resolved_edges)` |
| `LayerRuleEngine` | class | `readmenator/_layer_rules.py:9` | `class LayerRuleEngine` |
| `__init__` | method | `readmenator/_layer_rules.py:34` | `def __init__(self, config)` |
| `detect_violations` | method | `readmenator/_layer_rules.py:37` | `def detect_violations(self, nodes, edges, resolved_edges, layers)` |
| `violation_summary` | method | `readmenator/_layer_rules.py:109` | `def violation_summary(violations)` |
| `LayerDetector` | class | `readmenator/_layers.py:15` | `class LayerDetector` |
| `_classify_file` | method | `readmenator/_layers.py:89` | `def _classify_file(self, node, edges)` |
| `detect` | method | `readmenator/_layers.py:71` | `def detect(self, nodes, edges)` |
| `layer_summary` | method | `readmenator/_layers.py:122` | `def layer_summary(layers)` |
| `ArchitectureLinter` | class | `readmenator/_linter.py:18` | `class ArchitectureLinter` |
| `__init__` | method | `readmenator/_linter.py:31` | `def __init__(self, config)` |
| `_check_circular_dependencies` | method | `readmenator/_linter.py:127` | `def _check_circular_dependencies(self, nodes, resolved_edges)` |
| `_check_cross_layer_violations` | method | `readmenator/_linter.py:96` | `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)` |
| `_check_file_length` | method | `readmenator/_linter.py:65` | `def _check_file_length(self, nodes, content_map)` |
| `_dfs` | method | `readmenator/_linter.py:146` | `def _dfs(current)` |
| `lint` | method | `readmenator/_linter.py:34` | `def lint(self, nodes, edges, resolved_edges, layers, content_map)` |
| `MCPError` | class | `readmenator/_mcp_server.py:58` | `class MCPError(Exception)` |
| `MCPRequest` | class | `readmenator/_mcp_server.py:71` | `class MCPRequest` |
| `MCPResource` | class | `readmenator/_mcp_server.py:119` | `class MCPResource` |
| `MCPServer` | class | `readmenator/_mcp_server.py:146` | `class MCPServer` |
| `MCPTool` | class | `readmenator/_mcp_server.py:92` | `class MCPTool` |
| `__init__` | method | `readmenator/_mcp_server.py:59` | `def __init__(self, code, message, data)` |
| `__init__` | method | `readmenator/_mcp_server.py:72` | `def __init__(self, msg)` |
| `__init__` | method | `readmenator/_mcp_server.py:93` | `def __init__(self, name, description, handler, input_schema)` |
| `__init__` | method | `readmenator/_mcp_server.py:120` | `def __init__(self, uri, name, description, mime_type, handler)` |
| `__init__` | method | `readmenator/_mcp_server.py:147` | `def __init__(self, app, target_dir)` |
| `_ensure_kb` | method | `readmenator/_mcp_server.py:161` | `def _ensure_kb(self)` |
| `_get_query_engine` | method | `readmenator/_mcp_server.py:791` | `def _get_query_engine(self, nodes, edges, resolved)` |
| `_handle_call_tool` | method | `readmenator/_mcp_server.py:192` | `def _handle_call_tool(self, req)` |
| `_handle_initialize` | method | `readmenator/_mcp_server.py:173` | `def _handle_initialize(self, req)` |
| `_handle_list_resources` | method | `readmenator/_mcp_server.py:214` | `def _handle_list_resources(self, req)` |
| `_handle_list_tools` | method | `readmenator/_mcp_server.py:187` | `def _handle_list_tools(self, req)` |
| `_handle_read_resource` | method | `readmenator/_mcp_server.py:219` | `def _handle_read_resource(self, req)` |
| `_register_all` | method | `readmenator/_mcp_server.py:285` | `def _register_all(self)` |
| `_resource_analysis` | method | `readmenator/_mcp_server.py:757` | `def _resource_analysis(self)` |
| `_resource_findings` | method | `readmenator/_mcp_server.py:741` | `def _resource_findings(self)` |
| `_resource_graph` | method | `readmenator/_mcp_server.py:722` | `def _resource_graph(self)` |
| `_resource_kb` | method | `readmenator/_mcp_server.py:787` | `def _resource_kb(self)` |
| `_resource_summary` | method | `readmenator/_mcp_server.py:705` | `def _resource_summary(self)` |
| `_scan` | method | `readmenator/_mcp_server.py:467` | `def _scan(self)` |
| `_scan_deep` | method | `readmenator/_mcp_server.py:473` | `def _scan_deep(self)` |
| `_tool_communities` | method | `readmenator/_mcp_server.py:630` | `def _tool_communities(self)` |
| `_tool_cycles` | method | `readmenator/_mcp_server.py:619` | `def _tool_cycles(self)` |
| `_tool_explain` | method | `readmenator/_mcp_server.py:524` | `def _tool_explain(self, name)` |
| `_tool_export_json` | method | `readmenator/_mcp_server.py:697` | `def _tool_export_json(self)` |
| `_tool_findings` | method | `readmenator/_mcp_server.py:547` | `def _tool_findings(self, min_severity)` |
| `_tool_hotspots` | method | `readmenator/_mcp_server.py:603` | `def _tool_hotspots(self, top_n)` |
| `_tool_layer_violations` | method | `readmenator/_mcp_server.py:663` | `def _tool_layer_violations(self)` |
| `_tool_layers` | method | `readmenator/_mcp_server.py:645` | `def _tool_layers(self)` |
| `_tool_path` | method | `readmenator/_mcp_server.py:536` | `def _tool_path(self, symbol_a, symbol_b)` |
| `_tool_query` | method | `readmenator/_mcp_server.py:519` | `def _tool_query(self, text)` |
| `_tool_rebuild` | method | `readmenator/_mcp_server.py:679` | `def _tool_rebuild(self)` |
| `_tool_security_summary` | method | `readmenator/_mcp_server.py:577` | `def _tool_security_summary(self)` |
| `_tool_summary` | method | `readmenator/_mcp_server.py:481` | `def _tool_summary(self)` |
| `_tool_taint` | method | `readmenator/_mcp_server.py:582` | `def _tool_taint(self)` |
| `_tool_update` | method | `readmenator/_mcp_server.py:689` | `def _tool_update(self)` |
| `call` | method | `readmenator/_mcp_server.py:115` | `def call(self, arguments)` |
| `definition` | method | `readmenator/_mcp_server.py:108` | `def definition(self)` |
| `definition` | method | `readmenator/_mcp_server.py:134` | `def definition(self)` |
| `dispatch` | method | `readmenator/_mcp_server.py:241` | `def dispatch(self, req)` |
| `error` | method | `readmenator/_mcp_server.py:85` | `def error(self, code, message, data)` |
| `is_notification` | method | `readmenator/_mcp_server.py:79` | `def is_notification(self)` |
| `main` | method | `readmenator/_mcp_server.py:796` | `def main()` |
| `read` | method | `readmenator/_mcp_server.py:142` | `def read(self)` |
| `register_resource` | method | `readmenator/_mcp_server.py:158` | `def register_resource(self, resource)` |
| `register_tool` | method | `readmenator/_mcp_server.py:155` | `def register_tool(self, tool)` |
| `response` | method | `readmenator/_mcp_server.py:82` | `def response(self, result)` |
| `run` | method | `readmenator/_mcp_server.py:261` | `def run(self)` |
| `MermaidRenderer` | class | `readmenator/_mermaid.py:17` | `class MermaidRenderer` |
| `__init__` | method | `readmenator/_mermaid.py:26` | `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_` |
| `_sanitize_id` | method | `readmenator/_mermaid.py:45` | `def _sanitize_id(node_id)` |
| `render` | method | `readmenator/_mermaid.py:56` | `def render(self, nodes, edges, resolved_edges, analysis)` |
| `AnalysisResult` | class | `readmenator/_models.py:130` | `class AnalysisResult` |
| `AnalysisResultV2` | class | `readmenator/_models.py:284` | `class AnalysisResultV2` |
| `ChangeImpact` | class | `readmenator/_models.py:200` | `class ChangeImpact` |
| `CommunityResult` | class | `readmenator/_models.py:111` | `class CommunityResult` |
| `DataflowIssue` | class | `readmenator/_models.py:307` | `class DataflowIssue` |
| `DeadCodeReport` | class | `readmenator/_models.py:347` | `class DeadCodeReport` |
| `DependencyCycle` | class | `readmenator/_models.py:187` | `class DependencyCycle` |
| `Edge` | class | `readmenator/_models.py:58` | `class Edge` |
| `HotspotResult` | class | `readmenator/_models.py:217` | `class HotspotResult` |
| `LayerViolation` | class | `readmenator/_models.py:263` | `class LayerViolation` |
| `LinterViolation` | class | `readmenator/_models.py:330` | `class LinterViolation` |
| `Node` | class | `readmenator/_models.py:37` | `class Node` |
| `RefactoringAction` | class | `readmenator/_models.py:364` | `class RefactoringAction` |
| `RefactoringPlan` | class | `readmenator/_models.py:385` | `class RefactoringPlan` |
| `SecurityFinding` | class | `readmenator/_models.py:77` | `class SecurityFinding` |
| `SuggestedRule` | class | `readmenator/_models.py:238` | `class SuggestedRule` |
| `Symbol` | class | `readmenator/_models.py:18` | `class Symbol` |
| `TaintAnalysisResult` | class | `readmenator/_models.py:172` | `class TaintAnalysisResult` |
| `TaintPath` | class | `readmenator/_models.py:151` | `class TaintPath` |
| `pluralize_symbol_kind` | method | `readmenator/_models.py:101` | `def pluralize_symbol_kind(kind, plural_map)` |
| `AnalyzerFactory` | class | `readmenator/_pipeline.py:41` | `class AnalyzerFactory` |
| `DeepAnalysisRunner` | class | `readmenator/_pipeline.py:268` | `class DeepAnalysisRunner` |
| `__init__` | method | `readmenator/_pipeline.py:49` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_pipeline.py:277` | `def __init__(self, factory)` |
| `agent_injector` | method | `readmenator/_pipeline.py:183` | `def agent_injector(self)` |
| `agent_output` | method | `readmenator/_pipeline.py:193` | `def agent_output(self)` |
| `analyzer` | method | `readmenator/_pipeline.py:90` | `def analyzer(self)` |
| `build_typed_graph` | method | `readmenator/_pipeline.py:233` | `def build_typed_graph(self, nodes, edges, resolved_edges)` |
| `cpg` | method | `readmenator/_pipeline.py:145` | `def cpg(self)` |
| `dataflow` | method | `readmenator/_pipeline.py:114` | `def dataflow(self)` |
| `diagram_builder` | method | `readmenator/_pipeline.py:199` | `def diagram_builder(self)` |
| `diagram_publisher` | method | `readmenator/_pipeline.py:220` | `def diagram_publisher(self)` |
| `diagram_renderer` | method | `readmenator/_pipeline.py:206` | `def diagram_renderer(self)` |
| `diagram_validator` | method | `readmenator/_pipeline.py:213` | `def diagram_validator(self)` |
| `exporter` | method | `readmenator/_pipeline.py:102` | `def exporter(self)` |
| `generator` | method | `readmenator/_pipeline.py:84` | `def generator(self)` |
| `hotspots` | method | `readmenator/_pipeline.py:121` | `def hotspots(self)` |
| `last_category` | method | `readmenator/_pipeline.py:260` | `def last_category(self)` |
| `last_typed_graph` | method | `readmenator/_pipeline.py:264` | `def last_typed_graph(self)` |
| `layer_detector` | method | `readmenator/_pipeline.py:154` | `def layer_detector(self)` |
| `layer_rules` | method | `readmenator/_pipeline.py:127` | `def layer_rules(self)` |
| `make_ranker` | method | `readmenator/_pipeline.py:243` | `def make_ranker(self, typed_graph)` |
| `readme_injector` | method | `readmenator/_pipeline.py:173` | `def readme_injector(self)` |
| `rule_gen` | method | `readmenator/_pipeline.py:133` | `def rule_gen(self)` |
| `run` | method | `readmenator/_pipeline.py:280` | `def run(self, nodes, edges, resolved_edges, layers, content_map)` |
| `sarif` | method | `readmenator/_pipeline.py:139` | `def sarif(self)` |
| `scanner` | method | `readmenator/_pipeline.py:78` | `def scanner(self)` |
| `security` | method | `readmenator/_pipeline.py:96` | `def security(self)` |
| `taint` | method | `readmenator/_pipeline.py:108` | `def taint(self)` |
| `uml` | method | `readmenator/_pipeline.py:160` | `def uml(self)` |
| `vis_renderer` | method | `readmenator/_pipeline.py:227` | `def vis_renderer(self)` |
| `wiki` | method | `readmenator/_pipeline.py:166` | `def wiki(self)` |
| `DocProjection` | class | `readmenator/_projections.py:42` | `class DocProjection` |
| `IdentityProjection` | class | `readmenator/_projections.py:32` | `class IdentityProjection` |
| `Projection` | class | `readmenator/_projections.py:17` | `class Projection(Protocol)` |
| `RiskProjection` | class | `readmenator/_projections.py:63` | `class RiskProjection` |
| `__init__` | method | `readmenator/_projections.py:49` | `def __init__(self, documented_ids)` |
| `__init__` | method | `readmenator/_projections.py:70` | `def __init__(self, fan_in, fan_out, test_files)` |
| `apply_view` | method | `readmenator/_projections.py:95` | `def apply_view(category, view_config)` |
| `map_morphism` | method | `readmenator/_projections.py:27` | `def map_morphism(self, m)` |
| `map_morphism` | method | `readmenator/_projections.py:38` | `def map_morphism(self, m)` |
| `map_morphism` | method | `readmenator/_projections.py:57` | `def map_morphism(self, m)` |
| `map_morphism` | method | `readmenator/_projections.py:91` | `def map_morphism(self, m)` |
| `map_node` | method | `readmenator/_projections.py:23` | `def map_node(self, node)` |
| `map_node` | method | `readmenator/_projections.py:35` | `def map_node(self, node)` |
| `map_node` | method | `readmenator/_projections.py:52` | `def map_node(self, node)` |
| `map_node` | method | `readmenator/_projections.py:80` | `def map_node(self, node)` |
| `QueryEngine` | class | `readmenator/_query.py:25` | `class QueryEngine` |
| `__init__` | method | `readmenator/_query.py:34` | `def __init__(self, nodes, edges, resolved_edges, ranker, config)` |
| `_bfs_shortest_path` | method | `readmenator/_query.py:331` | `def _bfs_shortest_path(self, graph, start, goal)` |
| `_build_import_graph` | method | `readmenator/_query.py:184` | `def _build_import_graph(self)` |
| `_build_resolved_graph` | method | `readmenator/_query.py:200` | `def _build_resolved_graph(self)` |
| `_build_symbol_index` | method | `readmenator/_query.py:170` | `def _build_symbol_index(self)` |
| `_estimate_doc_coverage` | method | `readmenator/_query.py:150` | `def _estimate_doc_coverage(self)` |
| `_estimate_test_coverage` | method | `readmenator/_query.py:124` | `def _estimate_test_coverage(self)` |
| `_find_incoming_imports` | method | `readmenator/_query.py:277` | `def _find_incoming_imports(self, target)` |
| `_init_default_ranker` | method | `readmenator/_query.py:64` | `def _init_default_ranker(self)` |
| `_make_bidirectional` | method | `readmenator/_query.py:315` | `def _make_bidirectional(graph)` |
| `explain` | method | `readmenator/_query.py:238` | `def explain(self, name)` |
| `find_path` | method | `readmenator/_query.py:285` | `def find_path(self, symbol_a, symbol_b)` |
| `find_symbol` | method | `readmenator/_query.py:220` | `def find_symbol(self, name)` |
| `query` | method | `readmenator/_query.py:355` | `def query(self, question)` |
| `ranked_query` | method | `readmenator/_query.py:73` | `def ranked_query(self, query, top_n)` |
| `summary` | method | `readmenator/_query.py:411` | `def summary(self)` |
| `CompositeRanker` | class | `readmenator/_rank.py:377` | `class CompositeRanker` |
| `RankConfig` | class | `readmenator/_rank.py:32` | `class RankConfig` |
| `RankedItem` | class | `readmenator/_rank.py:320` | `class RankedItem` |
| `RankedResult` | class | `readmenator/_rank.py:349` | `class RankedResult` |
| `__init__` | method | `readmenator/_rank.py:385` | `def __init__(self, graph, config)` |
| `_find_justification_paths` | method | `readmenator/_rank.py:486` | `def _find_justification_paths(self, target, seed_ids, category, max_paths)` |
| `_format_explanation` | method | `readmenator/_rank.py:512` | `def _format_explanation(item, result)` |
| `_get_global_pr` | method | `readmenator/_rank.py:394` | `def _get_global_pr(self)` |
| `build_seeds_for_context` | method | `readmenator/_rank.py:286` | `def build_seeds_for_context(node_ids, anchor_patterns)` |
| `build_seeds_from_query` | method | `readmenator/_rank.py:240` | `def build_seeds_from_query(query, node_ids, node_labels, symbols)` |
| `explain` | method | `readmenator/_rank.py:369` | `def explain(self, node_id)` |
| `global_pagerank` | method | `readmenator/_rank.py:61` | `def global_pagerank(graph, alpha, max_iter, tolerance)` |
| `hits` | method | `readmenator/_rank.py:189` | `def hits(graph, max_iter, tolerance)` |
| `label` | method | `readmenator/_rank.py:344` | `def label(self)` |
| `personalized_pagerank` | method | `readmenator/_rank.py:119` | `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` |
| `rank` | method | `readmenator/_rank.py:404` | `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` |
| `top` | method | `readmenator/_rank.py:366` | `def top(self, n)` |
| `ReadmeInjector` | class | `readmenator/_readme_injector.py:68` | `class ReadmeInjector` |
| `__init__` | method | `readmenator/_readme_injector.py:76` | `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)` |
| `_build_injection` | method | `readmenator/_readme_injector.py:170` | `def _build_injection(self, suffix)` |
| `_extract_current_injection` | method | `readmenator/_readme_injector.py:115` | `def _extract_current_injection(content)` |
| `_find_readme` | method | `readmenator/_readme_injector.py:163` | `def _find_readme(root)` |
| `_remove_old_injection` | method | `readmenator/_readme_injector.py:124` | `def _remove_old_injection(content)` |
| `inject` | method | `readmenator/_readme_injector.py:86` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_readme_injector.py:134` | `def remove(self, project_root)` |
| `MonolithRefactorizer` | class | `readmenator/_refactorizer.py:24` | `class MonolithRefactorizer` |
| `__init__` | method | `readmenator/_refactorizer.py:32` | `def __init__(self, config)` |
| `_estimate_impact` | method | `readmenator/_refactorizer.py:147` | `def _estimate_impact(self, file_id, resolved_edges)` |
| `_get_line_count` | method | `readmenator/_refactorizer.py:70` | `def _get_line_count(self, file_id, content_map)` |
| `_group_symbols_by_kind` | method | `readmenator/_refactorizer.py:126` | `def _group_symbols_by_kind(self, symbols)` |
| `_plan_refactoring` | method | `readmenator/_refactorizer.py:82` | `def _plan_refactoring(self, node, edges, resolved_edges, content_map)` |
| `_suggest_target_file` | method | `readmenator/_refactorizer.py:132` | `def _suggest_target_file(self, source_file, kind)` |
| `analyze` | method | `readmenator/_refactorizer.py:35` | `def analyze(self, nodes, edges, resolved_edges, content_map)` |
| `generate_script` | method | `readmenator/_refactorizer.py:156` | `def generate_script(self, plan, project_root)` |
| `ImportResolver` | class | `readmenator/_resolver.py:18` | `class ImportResolver` |
| `__init__` | method | `readmenator/_resolver.py:61` | `def __init__(self, file_ids, root, extensions, include_dirs)` |
| `_build_dir_index` | method | `readmenator/_resolver.py:93` | `def _build_dir_index(self, file_ids)` |
| `_build_stem_index` | method | `readmenator/_resolver.py:83` | `def _build_stem_index(self, file_ids)` |
| `_resolve_basename_match` | method | `readmenator/_resolver.py:287` | `def _resolve_basename_match(self, import_str)` |
| `_resolve_directory_init` | method | `readmenator/_resolver.py:240` | `def _resolve_directory_init(self, import_str, source_file)` |
| `_resolve_extensionless` | method | `readmenator/_resolver.py:231` | `def _resolve_extensionless(self, import_str, source_file)` |
| `_resolve_include_dirs` | method | `readmenator/_resolver.py:175` | `def _resolve_include_dirs(self, import_str)` |
| `_resolve_module_dotpath` | method | `readmenator/_resolver.py:250` | `def _resolve_module_dotpath(self, import_str)` |
| `_resolve_relative` | method | `readmenator/_resolver.py:195` | `def _resolve_relative(self, import_str, source_file)` |
| `_resolve_stem_match` | method | `readmenator/_resolver.py:305` | `def _resolve_stem_match(self, import_str)` |
| `_resolve_suffix_match` | method | `readmenator/_resolver.py:272` | `def _resolve_suffix_match(self, import_str)` |
| `_resolve_verbatim` | method | `readmenator/_resolver.py:213` | `def _resolve_verbatim(self, import_str, source_file)` |
| `_strip_extension` | method | `readmenator/_resolver.py:314` | `def _strip_extension(self, name)` |
| `resolve` | method | `readmenator/_resolver.py:110` | `def resolve(self, import_str, source_file)` |
| `resolve_all` | method | `readmenator/_resolver.py:159` | `def resolve_all(self, import_str, source_file)` |
| `RuleGenerator` | class | `readmenator/_rule_gen.py:12` | `class RuleGenerator` |
| `__init__` | method | `readmenator/_rule_gen.py:88` | `def __init__(self, config)` |
| `_analyze_language` | method | `readmenator/_rule_gen.py:169` | `def _analyze_language(self, lang, nodes, content_map)` |
| `_detect_antipatterns` | method | `readmenator/_rule_gen.py:202` | `def _detect_antipatterns(self, nodes, content_map)` |
| `_group_by_language` | method | `readmenator/_rule_gen.py:159` | `def _group_by_language(self, nodes)` |
| `_infer_language_for_rule` | method | `readmenator/_rule_gen.py:248` | `def _infer_language_for_rule(rule_id)` |
| `_next_rule_id` | method | `readmenator/_rule_gen.py:258` | `def _next_rule_id(self)` |
| `generate` | method | `readmenator/_rule_gen.py:92` | `def generate(self, nodes, content_map)` |
| `write_rules` | method | `readmenator/_rule_gen.py:120` | `def write_rules(self, rules, output_dir)` |
| `SarifExporter` | class | `readmenator/_sarif.py:9` | `class SarifExporter` |
| `__init__` | method | `readmenator/_sarif.py:28` | `def __init__(self, privacy_mode)` |
| `_build_result` | method | `readmenator/_sarif.py:104` | `def _build_result(self, finding, rule_index)` |
| `_build_rule` | method | `readmenator/_sarif.py:80` | `def _build_rule(self, finding)` |
| `export` | method | `readmenator/_sarif.py:31` | `def export(self, findings, project_name)` |
| `PolyglotScanner` | class | `readmenator/_scanner.py:28` | `class PolyglotScanner` |
| `__init__` | method | `readmenator/_scanner.py:39` | `def __init__(self, config)` |
| `_check_directory_depth` | method | `readmenator/_scanner.py:141` | `def _check_directory_depth(self, path, root)` |
| `_emit_progress` | method | `readmenator/_scanner.py:225` | `def _emit_progress(self, count)` |
| `_extract_file_doc` | method | `readmenator/_scanner.py:149` | `def _extract_file_doc(self, content)` |
| `_gitignore_glob_to_regex` | method | `readmenator/_scanner.py:79` | `def _gitignore_glob_to_regex(pattern)` |
| `_is_gitignored` | method | `readmenator/_scanner.py:119` | `def _is_gitignored(self, rel_path)` |
| `_is_ignored` | method | `readmenator/_scanner.py:50` | `def _is_ignored(self, path)` |
| `_load_gitignore` | method | `readmenator/_scanner.py:57` | `def _load_gitignore(self, root)` |
| `_scan_impl` | method | `readmenator/_scanner.py:260` | `def _scan_impl(self, root)` |
| `_validate_path_security` | method | `readmenator/_scanner.py:128` | `def _validate_path_security(self, path)` |
| `scan` | method | `readmenator/_scanner.py:235` | `def scan(self, root)` |
| `scan_with_content` | method | `readmenator/_scanner.py:249` | `def scan_with_content(self, root)` |
| `SecurityAnalyzer` | class | `readmenator/_security.py:486` | `class SecurityAnalyzer` |
| `SecurityRule` | class | `readmenator/_security.py:24` | `class SecurityRule` |
| `__init__` | method | `readmenator/_security.py:496` | `def __init__(self, config)` |
| `_build_rules_from_yaml` | method | `readmenator/_security.py:447` | `def _build_rules_from_yaml(yaml_path)` |
| `_c_rules` | method | `readmenator/_security.py:201` | `def _c_rules()` |
| `_compile` | method | `readmenator/_security.py:148` | `def _compile()` |
| `_csharp_rules` | method | `readmenator/_security.py:297` | `def _csharp_rules()` |
| `_dart_rules` | method | `readmenator/_security.py:354` | `def _dart_rules()` |
| `_elixir_rules` | method | `readmenator/_security.py:398` | `def _elixir_rules()` |
| `_gdscript_rules` | method | `readmenator/_security.py:387` | `def _gdscript_rules()` |
| `_go_rules` | method | `readmenator/_security.py:237` | `def _go_rules()` |
| `_java_rules` | method | `readmenator/_security.py:222` | `def _java_rules()` |
| `_javascript_rules` | method | `readmenator/_security.py:182` | `def _javascript_rules()` |
| `_kotlin_rules` | method | `readmenator/_security.py:310` | `def _kotlin_rules()` |
| `_load_rules_from_yaml` | method | `readmenator/_security.py:128` | `def _load_rules_from_yaml(yaml_path)` |
| `_lua_rules` | method | `readmenator/_security.py:343` | `def _lua_rules()` |
| `_meets_threshold` | method | `readmenator/_security.py:509` | `def _meets_threshold(self, severity)` |
| `_nim_rules` | method | `readmenator/_security.py:376` | `def _nim_rules()` |
| `_parse_minimal_yaml` | method | `readmenator/_security.py:46` | `def _parse_minimal_yaml(text)` |
| `_php_rules` | method | `readmenator/_security.py:267` | `def _php_rules()` |
| `_python_rules` | method | `readmenator/_security.py:153` | `def _python_rules()` |
| `_resolve_rules` | method | `readmenator/_security.py:500` | `def _resolve_rules(self)` |
| `_ruby_rules` | method | `readmenator/_security.py:250` | `def _ruby_rules()` |
| `_rust_rules` | method | `readmenator/_security.py:365` | `def _rust_rules()` |
| `_scala_rules` | method | `readmenator/_security.py:332` | `def _scala_rules()` |
| `_shell_rules` | method | `readmenator/_security.py:284` | `def _shell_rules()` |
| `_swift_rules` | method | `readmenator/_security.py:321` | `def _swift_rules()` |
| `_unquote` | method | `readmenator/_security.py:121` | `def _unquote(s)` |
| `_validate_path` | method | `readmenator/_security.py:555` | `def _validate_path(self, path, root)` |
| `fix_hint_for` | method | `readmenator/_security.py:620` | `def fix_hint_for(finding)` |
| `scan` | method | `readmenator/_security.py:513` | `def scan(self, root)` |
| `summary` | method | `readmenator/_security.py:572` | `def summary(self, findings)` |
| `TaintAnalyzer` | class | `readmenator/_taint.py:10` | `class TaintAnalyzer` |
| `__init__` | method | `readmenator/_taint.py:71` | `def __init__(self, config)` |
| `_build_forward_graph` | method | `readmenator/_taint.py:211` | `def _build_forward_graph(nodes, resolved_edges)` |
| `_find_direct_sources` | method | `readmenator/_taint.py:134` | `def _find_direct_sources(self, nodes, edges)` |
| `_propagate` | method | `readmenator/_taint.py:160` | `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` |
| `analyze` | method | `readmenator/_taint.py:75` | `def analyze(self, nodes, edges, resolved_edges)` |
| `UmlGenerator` | class | `readmenator/_uml.py:32` | `class UmlGenerator` |
| `__init__` | method | `readmenator/_uml.py:34` | `def __init__(self, config)` |
| `_cpp_params` | method | `readmenator/_uml.py:257` | `def _cpp_params(params)` |
| `_cs_params` | method | `readmenator/_uml.py:343` | `def _cs_params(params)` |
| `_extract_params` | method | `readmenator/_uml.py:590` | `def _extract_params(signature)` |
| `_find_node` | method | `readmenator/_uml.py:163` | `def _find_node(nodes, node_id)` |
| `_generate_cpp` | method | `readmenator/_uml.py:231` | `def _generate_cpp(class_symbols, nodes, edges)` |
| `_generate_csharp` | method | `readmenator/_uml.py:314` | `def _generate_csharp(class_symbols, nodes, edges)` |
| `_generate_dart` | method | `readmenator/_uml.py:545` | `def _generate_dart(class_symbols, nodes, edges)` |
| `_generate_go` | method | `readmenator/_uml.py:393` | `def _generate_go(class_symbols, nodes, edges)` |
| `_generate_java` | method | `readmenator/_uml.py:272` | `def _generate_java(class_symbols, nodes, edges)` |
| `_generate_kotlin` | method | `readmenator/_uml.py:474` | `def _generate_kotlin(class_symbols, nodes, edges)` |
| `_generate_php` | method | `readmenator/_uml.py:446` | `def _generate_php(class_symbols, nodes, edges)` |
| `_generate_python` | method | `readmenator/_uml.py:358` | `def _generate_python(class_symbols, nodes, edges)` |
| `_generate_ruby` | method | `readmenator/_uml.py:565` | `def _generate_ruby(class_symbols, nodes, edges)` |
| `_generate_rust` | method | `readmenator/_uml.py:420` | `def _generate_rust(class_symbols, nodes, edges)` |
| `_generate_scala` | method | `readmenator/_uml.py:494` | `def _generate_scala(class_symbols, nodes, edges)` |
| `_generate_swift` | method | `readmenator/_uml.py:516` | `def _generate_swift(class_symbols, nodes, edges)` |
| `_get_code_generator` | method | `readmenator/_uml.py:170` | `def _get_code_generator(language)` |
| `_java_params` | method | `readmenator/_uml.py:299` | `def _java_params(params)` |
| `_safe_name` | method | `readmenator/_uml.py:586` | `def _safe_name(name)` |
| `_sanitize_id` | method | `readmenator/_uml.py:151` | `def _sanitize_id(raw)` |
| `_type_map_py_to_target` | method | `readmenator/_uml.py:188` | `def _type_map_py_to_target(target, py_type_hint)` |
| `generate_code` | method | `readmenator/_uml.py:127` | `def generate_code(self, nodes, edges, target_language)` |
| `render_mermaid_class_diagram` | method | `readmenator/_uml.py:37` | `def render_mermaid_class_diagram(self, nodes, edges)` |
| `DirectoryWatcher` | class | `readmenator/_watcher.py:21` | `class DirectoryWatcher` |
| `__init__` | method | `readmenator/_watcher.py:29` | `def __init__(self, root, config, callback, interval_seconds)` |
| `_compute_snapshot` | method | `readmenator/_watcher.py:51` | `def _compute_snapshot(self)` |
| `start` | method | `readmenator/_watcher.py:80` | `def start(self)` |
| `stop` | method | `readmenator/_watcher.py:97` | `def stop(self)` |
| `WikiGenerator` | class | `readmenator/_wiki.py:120` | `class WikiGenerator` |
| `__init__` | method | `readmenator/_wiki.py:123` | `def __init__(self, config)` |
| `_build_community_page` | method | `readmenator/_wiki.py:516` | `def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)` |
| `_build_connections` | method | `readmenator/_wiki.py:243` | `def _build_connections(self, communities, resolved, analysis, node_map, layers)` |
| `_build_connections_json` | method | `readmenator/_wiki.py:420` | `def _build_connections_json(self, connections)` |
| `_build_grouped_files` | method | `readmenator/_wiki.py:467` | `def _build_grouped_files(self, members, node_map, layers, max_files)` |
| `_build_index` | method | `readmenator/_wiki.py:720` | `def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections, projec` |
| `_build_queries` | method | `readmenator/_wiki.py:902` | `def _build_queries(self, analysis)` |
| `_build_report` | method | `readmenator/_wiki.py:927` | `def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name, proj` |
| `_clean_purpose` | function | `readmenator/_wiki.py:55` | `def _clean_purpose(text)` |
| `_community_of` | method | `readmenator/_wiki.py:234` | `def _community_of(self, node_id, communities)` |
| `_connective_paragraph` | method | `readmenator/_wiki.py:865` | `def _connective_paragraph(self, communities, connections)` |
| `_definition_for` | method | `readmenator/_wiki.py:424` | `def _definition_for(self, community, node_map)` |
| `_display_names` | function | `readmenator/_wiki.py:106` | `def _display_names(communities)` |
| `_duplicate_links` | method | `readmenator/_wiki.py:308` | `def _duplicate_links(communities, node_map, skip_pairs)` |
| `_escape` | function | `readmenator/_wiki.py:81` | `def _escape(text)` |
| `_estimate_tokens` | method | `readmenator/_wiki.py:999` | `def _estimate_tokens(self, nodes, connections)` |
| `_file_row` | method | `readmenator/_wiki.py:453` | `def _file_row(self, fid, node_map, layers)` |
| `_is_garbage_doc` | function | `readmenator/_wiki.py:86` | `def _is_garbage_doc(text)` |
| `_is_garbage_purpose` | function | `readmenator/_wiki.py:44` | `def _is_garbage_purpose(text)` |
| `_large_files` | method | `readmenator/_wiki.py:707` | `def _large_files(self, nodes, project_root)` |
| `_overview_paragraph` | method | `readmenator/_wiki.py:832` | `def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)` |
| `_prune_stale_pages` | method | `readmenator/_wiki.py:176` | `def _prune_stale_pages(self, out_dir, current)` |
| `_questions_for` | method | `readmenator/_wiki.py:669` | `def _questions_for(self, community, node_map, member_set, analysis_v2)` |
| `_questions_paragraph` | method | `readmenator/_wiki.py:886` | `def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)` |
| `_resolve_communities` | method | `readmenator/_wiki.py:208` | `def _resolve_communities(self, nodes, analysis, resolved)` |
| `_shared_context` | method | `readmenator/_wiki.py:387` | `def _shared_context(first, second, node_map, layers)` |
| `_shared_context_links` | method | `readmenator/_wiki.py:351` | `def _shared_context_links(self, communities, existing, node_map, layers)` |
| `_slug` | function | `readmenator/_wiki.py:74` | `def _slug(text)` |
| `_write` | method | `readmenator/_wiki.py:1010` | `def _write(path, content)` |
| `dominant` | method | `readmenator/_wiki.py:394` | `def dominant(ids, key)` |
| `existing_ids` | function | `readmenator/_wiki.py:96` | `def existing_ids(connections)` |
| `generate` | method | `readmenator/_wiki.py:128` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)` |
| `lint` | method | `readmenator/_wiki.py:185` | `def lint(self, project_root)` |
| `_init_parser_map` | function | `readmenator/parsers/__init__.py:32` | `def _init_parser_map()` |
| `create_parser` | function | `readmenator/parsers/__init__.py:68` | `def create_parser(extension, filename, config)` |
| `AssemblyParser` | class | `readmenator/parsers/_assembly.py:9` | `class AssemblyParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_assembly.py:17` | `def _extract_specifics(self, content)` |
| `LanguageParser` | class | `readmenator/parsers/_base.py:10` | `class LanguageParser` |
| `__init__` | method | `readmenator/parsers/_base.py:19` | `def __init__(self, filename, config)` |
| `_extract_docstring` | method | `readmenator/parsers/_base.py:47` | `def _extract_docstring(self, line_num)` |
| `_extract_signature` | method | `readmenator/parsers/_base.py:89` | `def _extract_signature(self, content, match_start, pattern)` |
| `_extract_specifics` | method | `readmenator/parsers/_base.py:43` | `def _extract_specifics(self, content)` |
| `parse` | method | `readmenator/parsers/_base.py:34` | `def parse(self, content)` |
| `CParser` | class | `readmenator/parsers/_c.py:28` | `class CParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_c.py:35` | `def _extract_specifics(self, content)` |
| `_has_type_prefix` | function | `readmenator/parsers/_c.py:16` | `def _has_type_prefix(prefix)` |
| `CSharpParser` | class | `readmenator/parsers/_csharp.py:9` | `class CSharpParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_csharp.py:16` | `def _extract_specifics(self, content)` |
| `DartParser` | class | `readmenator/parsers/_dart.py:9` | `class DartParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_dart.py:16` | `def _extract_specifics(self, content)` |
| `ElixirParser` | class | `readmenator/parsers/_elixir.py:9` | `class ElixirParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_elixir.py:16` | `def _extract_specifics(self, content)` |
| `GDScriptParser` | class | `readmenator/parsers/_gdscript.py:9` | `class GDScriptParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_gdscript.py:16` | `def _extract_specifics(self, content)` |
| `GoParser` | class | `readmenator/parsers/_go.py:9` | `class GoParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_go.py:16` | `def _extract_specifics(self, content)` |
| `JavaParser` | class | `readmenator/parsers/_java.py:9` | `class JavaParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_java.py:16` | `def _extract_specifics(self, content)` |
| `JavaScriptParser` | class | `readmenator/parsers/_javascript.py:9` | `class JavaScriptParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_javascript.py:17` | `def _extract_specifics(self, content)` |
| `KotlinParser` | class | `readmenator/parsers/_kotlin.py:9` | `class KotlinParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_kotlin.py:16` | `def _extract_specifics(self, content)` |
| `LuaParser` | class | `readmenator/parsers/_lua.py:9` | `class LuaParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_lua.py:16` | `def _extract_specifics(self, content)` |
| `NimParser` | class | `readmenator/parsers/_nim.py:9` | `class NimParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_nim.py:16` | `def _extract_specifics(self, content)` |
| `PHPParser` | class | `readmenator/parsers/_php.py:9` | `class PHPParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_php.py:16` | `def _extract_specifics(self, content)` |
| `PythonParser` | class | `readmenator/parsers/_python.py:10` | `class PythonParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_python.py:17` | `def _extract_specifics(self, content)` |
| `RubyParser` | class | `readmenator/parsers/_ruby.py:9` | `class RubyParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_ruby.py:16` | `def _extract_specifics(self, content)` |
| `RustParser` | class | `readmenator/parsers/_rust.py:9` | `class RustParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_rust.py:16` | `def _extract_specifics(self, content)` |
| `ScalaParser` | class | `readmenator/parsers/_scala.py:9` | `class ScalaParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_scala.py:16` | `def _extract_specifics(self, content)` |
| `ShellParser` | class | `readmenator/parsers/_shell.py:9` | `class ShellParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_shell.py:16` | `def _extract_specifics(self, content)` |
| `SwiftParser` | class | `readmenator/parsers/_swift.py:9` | `class SwiftParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_swift.py:16` | `def _extract_specifics(self, content)` |
| `Config` | class | `readmenator_orchestrator.py:21` | `class Config` |
| `GitHubClient` | class | `readmenator_orchestrator.py:77` | `class GitHubClient` |
| `Orchestrator` | class | `readmenator_orchestrator.py:341` | `class Orchestrator` |
| `RepositoryProcessor` | class | `readmenator_orchestrator.py:191` | `class RepositoryProcessor` |
| `TestOrchestrator` | class | `readmenator_orchestrator.py:396` | `class TestOrchestrator(TestCase)` |
| `__init__` | method | `readmenator_orchestrator.py:78` | `def __init__(self, config)` |
| `__init__` | method | `readmenator_orchestrator.py:192` | `def __init__(self, config, github_client)` |
| `__init__` | method | `readmenator_orchestrator.py:342` | `def __init__(self, config)` |
| `_cleanup_temp_dir` | method | `readmenator_orchestrator.py:336` | `def _cleanup_temp_dir(temp_dir)` |
| `_clone_repository` | method | `readmenator_orchestrator.py:241` | `def _clone_repository(self, repo)` |
| `_commit_and_push` | method | `readmenator_orchestrator.py:290` | `def _commit_and_push(self, repo_dir, repo)` |
| `_copy_to_docs_dir` | method | `readmenator_orchestrator.py:277` | `def _copy_to_docs_dir(self, repo_dir, generated_file)` |
| `_get_default_branch` | method | `readmenator_orchestrator.py:225` | `def _get_default_branch(self, repo)` |
| `_resolve_user` | method | `readmenator_orchestrator.py:83` | `def _resolve_user(self)` |
| `_run_readmenator` | method | `readmenator_orchestrator.py:257` | `def _run_readmenator(self, repo_dir)` |
| `_safe_env` | method | `readmenator_orchestrator.py:62` | `def _safe_env()` |
| `_setup_git_auth` | method | `readmenator_orchestrator.py:104` | `def _setup_git_auth(self)` |
| `_validate_branch_name` | method | `readmenator_orchestrator.py:56` | `def _validate_branch_name(name)` |
| `_validate_repo_name` | method | `readmenator_orchestrator.py:50` | `def _validate_repo_name(name)` |
| `close_existing_prs` | method | `readmenator_orchestrator.py:130` | `def close_existing_prs(self, repo)` |
| `create_pr` | method | `readmenator_orchestrator.py:170` | `def create_pr(self, repo, default_branch, timestamp)` |
| `delete_remote_branch` | method | `readmenator_orchestrator.py:158` | `def delete_remote_branch(self, repo)` |
| `list_repos` | method | `readmenator_orchestrator.py:118` | `def list_repos(self)` |
| `main` | method | `readmenator_orchestrator.py:455` | `def main()` |
| `parse_arguments` | method | `readmenator_orchestrator.py:438` | `def parse_arguments()` |
| `process` | method | `readmenator_orchestrator.py:196` | `def process(self, repo)` |
| `run` | method | `readmenator_orchestrator.py:347` | `def run(self, dry_run, only_repo)` |
| `setUp` | method | `readmenator_orchestrator.py:397` | `def setUp(self)` |
| `tearDown` | method | `readmenator_orchestrator.py:401` | `def tearDown(self)` |
| `test_branch_name_validation` | method | `readmenator_orchestrator.py:429` | `def test_branch_name_validation(self)` |
| `test_config_defaults` | method | `readmenator_orchestrator.py:408` | `def test_config_defaults(self)` |
| `test_config_immutability` | method | `readmenator_orchestrator.py:404` | `def test_config_immutability(self)` |
| `test_repo_name_validation` | method | `readmenator_orchestrator.py:419` | `def test_repo_name_validation(self)` |
| `test_skip_repos_logic` | method | `readmenator_orchestrator.py:415` | `def test_skip_repos_logic(self)` |
| `TestAgentInjectorEdgeCases` | class | `tests/test_agent_injector.py:248` | `class TestAgentInjectorEdgeCases(TestCase)` |
| `TestAgentInjectorFindFiles` | class | `tests/test_agent_injector.py:211` | `class TestAgentInjectorFindFiles(TestCase)` |
| `TestAgentInjectorInjectBehavior` | class | `tests/test_agent_injector.py:19` | `class TestAgentInjectorInjectBehavior(TestCase)` |
| `TestAgentInjectorRemoveBehavior` | class | `tests/test_agent_injector.py:168` | `class TestAgentInjectorRemoveBehavior(TestCase)` |
| `setUp` | method | `tests/test_agent_injector.py:22` | `def setUp(self)` |
| `setUp` | method | `tests/test_agent_injector.py:171` | `def setUp(self)` |
| `setUp` | method | `tests/test_agent_injector.py:214` | `def setUp(self)` |
| `setUp` | method | `tests/test_agent_injector.py:251` | `def setUp(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:27` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:176` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:218` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:256` | `def tearDown(self)` |
| `test_custom_kb_filename_works` | method | `tests/test_agent_injector.py:145` | `def test_custom_kb_filename_works(self)` |
| `test_finds_agents_md` | method | `tests/test_agent_injector.py:221` | `def test_finds_agents_md(self)` |
| `test_finds_all_listed_files` | method | `tests/test_agent_injector.py:227` | `def test_finds_all_listed_files(self)` |
| `test_finds_cursor_rules_glob` | method | `tests/test_agent_injector.py:234` | `def test_finds_cursor_rules_glob(self)` |
| `test_inject_does_not_execute_commands` | method | `tests/test_agent_injector.py:160` | `def test_inject_does_not_execute_commands(self)` |
| `test_inject_does_not_touch_unlisted_files` | method | `tests/test_agent_injector.py:275` | `def test_inject_does_not_touch_unlisted_files(self)` |
| `test_inject_into_agents_md_adds_kb_link` | method | `tests/test_agent_injector.py:30` | `def test_inject_into_agents_md_adds_kb_link(self)` |
| `test_inject_into_claude_md_adds_kb_link` | method | `tests/test_agent_injector.py:39` | `def test_inject_into_claude_md_adds_kb_link(self)` |
| `test_inject_into_cursor_rules_mdc_glob` | method | `tests/test_agent_injector.py:96` | `def test_inject_into_cursor_rules_mdc_glob(self)` |
| `test_inject_into_cursorrules_adds_kb_link` | method | `tests/test_agent_injector.py:49` | `def test_inject_into_cursorrules_adds_kb_link(self)` |
| `test_inject_into_empty_file` | method | `tests/test_agent_injector.py:259` | `def test_inject_into_empty_file(self)` |
| `test_inject_into_github_copilot_instructions` | method | `tests/test_agent_injector.py:57` | `def test_inject_into_github_copilot_instructions(self)` |
| `test_inject_is_idempotent_does_not_duplicate` | method | `tests/test_agent_injector.py:106` | `def test_inject_is_idempotent_does_not_duplicate(self)` |
| `test_inject_multiple_agent_files` | method | `tests/test_agent_injector.py:129` | `def test_inject_multiple_agent_files(self)` |
| `test_inject_no_agent_files_returns_zero` | method | `tests/test_agent_injector.py:117` | `def test_inject_no_agent_files_returns_zero(self)` |
| `test_inject_plain_text_format_for_yaml` | method | `tests/test_agent_injector.py:136` | `def test_inject_plain_text_format_for_yaml(self)` |
| `test_inject_preserves_existing_content` | method | `tests/test_agent_injector.py:121` | `def test_inject_preserves_existing_content(self)` |
| `test_inject_replaces_old_injection_without_regen_command` | method | `tests/test_agent_injector.py:67` | `def test_inject_replaces_old_injection_without_regen_command(self)` |
| `test_inject_respects_custom_agent_files_list` | method | `tests/test_agent_injector.py:267` | `def test_inject_respects_custom_agent_files_list(self)` |
| `test_inject_skips_when_already_up_to_date` | method | `tests/test_agent_injector.py:82` | `def test_inject_skips_when_already_up_to_date(self)` |
| `test_injection_includes_regeneration_command` | method | `tests/test_agent_injector.py:153` | `def test_injection_includes_regeneration_command(self)` |
| `test_remove_no_files_returns_zero` | method | `tests/test_agent_injector.py:196` | `def test_remove_no_files_returns_zero(self)` |
| `test_remove_preserves_original_content` | method | `tests/test_agent_injector.py:200` | `def test_remove_preserves_original_content(self)` |
| `test_remove_strips_injected_section` | method | `tests/test_agent_injector.py:179` | `def test_remove_strips_injected_section(self)` |
| `test_remove_without_injection_returns_zero` | method | `tests/test_agent_injector.py:190` | `def test_remove_without_injection_returns_zero(self)` |
| `test_returns_empty_when_no_files` | method | `tests/test_agent_injector.py:243` | `def test_returns_empty_when_no_files(self)` |
| `TestAgentOutputContract` | class | `tests/test_agent_output.py:49` | `class TestAgentOutputContract(TestCase)` |
| `TestApiGeneration` | class | `tests/test_agent_output.py:268` | `class TestApiGeneration(TestCase)` |
| `TestArchitectureGeneration` | class | `tests/test_agent_output.py:246` | `class TestArchitectureGeneration(TestCase)` |
| `TestFullGenerate` | class | `tests/test_agent_output.py:362` | `class TestFullGenerate(TestCase)` |
| `TestGotchasGeneration` | class | `tests/test_agent_output.py:190` | `class TestGotchasGeneration(TestCase)` |
| `TestIndexGeneration` | class | `tests/test_agent_output.py:117` | `class TestIndexGeneration(TestCase)` |
| `TestInjectionOutdatedDetection` | class | `tests/test_agent_output.py:434` | `class TestInjectionOutdatedDetection(TestCase)` |
| `TestRecipesGeneration` | class | `tests/test_agent_output.py:316` | `class TestRecipesGeneration(TestCase)` |
| `TestSecurityGeneration` | class | `tests/test_agent_output.py:143` | `class TestSecurityGeneration(TestCase)` |
| `TestSubsystemFileGeneration` | class | `tests/test_agent_output.py:294` | `class TestSubsystemFileGeneration(TestCase)` |
| `TestSubsystemInference` | class | `tests/test_agent_output.py:63` | `class TestSubsystemInference(TestCase)` |
| `_make_edge` | function | `tests/test_agent_output.py:30` | `def _make_edge(source, target, relation)` |
| `_make_finding` | function | `tests/test_agent_output.py:34` | `def _make_finding(file_path, line, severity, rule_id, description, snippet, cwe)` |
| `_make_node` | function | `tests/test_agent_output.py:19` | `def _make_node(node_id, symbols, doc, language)` |
| `test_agent_injector_detects_outdated` | method | `tests/test_agent_output.py:435` | `def test_agent_injector_detects_outdated(self)` |
| `test_agent_injector_skips_identical` | method | `tests/test_agent_output.py:457` | `def test_agent_injector_skips_identical(self)` |
| `test_all_files_under_500_lines` | method | `tests/test_agent_output.py:394` | `def test_all_files_under_500_lines(self)` |
| `test_config_defaults` | method | `tests/test_agent_output.py:50` | `def test_config_defaults(self)` |
| `test_config_immutable` | method | `tests/test_agent_output.py:56` | `def test_config_immutable(self)` |
| `test_cycle_loop_closed` | method | `tests/test_agent_output.py:230` | `def test_cycle_loop_closed(self)` |
| `test_cycles_section` | method | `tests/test_agent_output.py:207` | `def test_cycles_section(self)` |
| `test_empty_findings` | method | `tests/test_agent_output.py:144` | `def test_empty_findings(self)` |
| `test_empty_gotchas` | method | `tests/test_agent_output.py:224` | `def test_empty_gotchas(self)` |
| `test_external_imports` | method | `tests/test_agent_output.py:258` | `def test_external_imports(self)` |
| `test_findings_grouped_by_severity` | method | `tests/test_agent_output.py:150` | `def test_findings_grouped_by_severity(self)` |
| `test_findings_include_fix_hint_and_scope` | method | `tests/test_agent_output.py:166` | `def test_findings_include_fix_hint_and_scope(self)` |
| `test_flat_project_single_file` | method | `tests/test_agent_output.py:80` | `def test_flat_project_single_file(self)` |
| `test_functions_listed` | method | `tests/test_agent_output.py:269` | `def test_functions_listed(self)` |
| `test_generate_creates_all_files` | method | `tests/test_agent_output.py:363` | `def test_generate_creates_all_files(self)` |
| `test_god_nodes_section` | method | `tests/test_agent_output.py:191` | `def test_god_nodes_section(self)` |
| `test_index_lists_all_files` | method | `tests/test_agent_output.py:118` | `def test_index_lists_all_files(self)` |
| `test_index_table_format` | method | `tests/test_agent_output.py:133` | `def test_index_table_format(self)` |
| `test_inferred_from_directories` | method | `tests/test_agent_output.py:64` | `def test_inferred_from_directories(self)` |
| `test_internal_dependencies` | method | `tests/test_agent_output.py:247` | `def test_internal_dependencies(self)` |
| `test_manifest_workflow_orients_with_ls` | method | `tests/test_agent_output.py:421` | `def test_manifest_workflow_orients_with_ls(self)` |
| `test_min_threshold_respected` | method | `tests/test_agent_output.py:91` | `def test_min_threshold_respected(self)` |
| `test_misc_catches_unassigned` | method | `tests/test_agent_output.py:103` | `def test_misc_catches_unassigned(self)` |
| `test_no_json_in_any_output` | method | `tests/test_agent_output.py:409` | `def test_no_json_in_any_output(self)` |
| `test_no_json_in_api` | method | `tests/test_agent_output.py:283` | `def test_no_json_in_api(self)` |
| `test_no_json_wrapping` | method | `tests/test_agent_output.py:181` | `def test_no_json_wrapping(self)` |
| `test_readme_injector_detects_outdated` | method | `tests/test_agent_output.py:473` | `def test_readme_injector_detects_outdated(self)` |
| `test_readme_injector_skips_identical` | method | `tests/test_agent_output.py:495` | `def test_readme_injector_skips_identical(self)` |
| `test_recipes_directory` | method | `tests/test_agent_output.py:317` | `def test_recipes_directory(self)` |
| `test_recipes_grounded_in_actual_findings` | method | `tests/test_agent_output.py:330` | `def test_recipes_grounded_in_actual_findings(self)` |
| `test_subsystem_files_written` | method | `tests/test_agent_output.py:295` | `def test_subsystem_files_written(self)` |
| `TestGraphAnalyzerContract` | class | `tests/test_analyzer.py:16` | `class TestGraphAnalyzerContract(TestCase)` |
| `_make_edge` | method | `tests/test_analyzer.py:26` | `def _make_edge(self, src, tgt, rel)` |
| `_make_node` | method | `tests/test_analyzer.py:23` | `def _make_node(self, nid, label, lang)` |
| `setUp` | method | `tests/test_analyzer.py:19` | `def setUp(self)` |
| `test_analyze_computes_god_nodes` | method | `tests/test_analyzer.py:48` | `def test_analyze_computes_god_nodes(self)` |
| `test_analyze_detects_communities_for_connected_graph` | method | `tests/test_analyzer.py:34` | `def test_analyze_detects_communities_for_connected_graph(self)` |
| `test_analyze_empty_graph_returns_empty_result` | method | `tests/test_analyzer.py:29` | `def test_analyze_empty_graph_returns_empty_result(self)` |
| `test_analyze_finds_surprising_connections` | method | `tests/test_analyzer.py:64` | `def test_analyze_finds_surprising_connections(self)` |
| `test_analyze_generates_questions` | method | `tests/test_analyzer.py:81` | `def test_analyze_generates_questions(self)` |
| `test_analyze_is_repeatable` | method | `tests/test_analyzer.py:130` | `def test_analyze_is_repeatable(self)` |
| `test_analyze_with_resolved_edges_counts_them` | method | `tests/test_analyzer.py:116` | `def test_analyze_with_resolved_edges_counts_them(self)` |
| `test_community_cohesion_is_between_zero_and_one` | method | `tests/test_analyzer.py:92` | `def test_community_cohesion_is_between_zero_and_one(self)` |
| `test_dominant_directory_prefers_specific_on_tie` | method | `tests/test_analyzer.py:141` | `def test_dominant_directory_prefers_specific_on_tie(self)` |
| `test_isolated_nodes_do_not_form_communities` | method | `tests/test_analyzer.py:107` | `def test_isolated_nodes_do_not_form_communities(self)` |
| `TestFileCacheContract` | class | `tests/test_cache.py:18` | `class TestFileCacheContract(TestCase)` |
| `_write` | method | `tests/test_cache.py:30` | `def _write(self, rel_path, content)` |
| `setUp` | method | `tests/test_cache.py:21` | `def setUp(self)` |
| `tearDown` | method | `tests/test_cache.py:26` | `def tearDown(self)` |
| `test_clear_analysis_all_keys` | method | `tests/test_cache.py:127` | `def test_clear_analysis_all_keys(self)` |
| `test_clear_analysis_specific_key` | method | `tests/test_cache.py:120` | `def test_clear_analysis_specific_key(self)` |
| `test_compute_hash_returns_hex_string` | method | `tests/test_cache.py:36` | `def test_compute_hash_returns_hex_string(self)` |
| `test_compute_hashes_batch` | method | `tests/test_cache.py:92` | `def test_compute_hashes_batch(self)` |
| `test_different_content_produces_different_hash` | method | `tests/test_cache.py:42` | `def test_different_content_produces_different_hash(self)` |
| `test_find_changed_detects_modified_files` | method | `tests/test_cache.py:71` | `def test_find_changed_detects_modified_files(self)` |
| `test_find_changed_detects_new_files` | method | `tests/test_cache.py:66` | `def test_find_changed_detects_new_files(self)` |
| `test_find_changed_skips_unchanged_files` | method | `tests/test_cache.py:78` | `def test_find_changed_skips_unchanged_files(self)` |
| `test_has_changed_since_last_analysis_returns_false_when_no_changes` | method | `tests/test_cache.py:139` | `def test_has_changed_since_last_analysis_returns_false_when_no_changes(self)` |
| `test_has_changed_since_last_analysis_returns_true_on_first_run` | method | `tests/test_cache.py:134` | `def test_has_changed_since_last_analysis_returns_true_on_first_run(self)` |
| `test_has_changed_since_last_analysis_returns_true_when_file_changed` | method | `tests/test_cache.py:147` | `def test_has_changed_since_last_analysis_returns_true_when_file_changed(self)` |
| `test_load_missing_analysis_key_returns_none` | method | `tests/test_cache.py:116` | `def test_load_missing_analysis_key_returns_none(self)` |
| `test_load_returns_empty_dict_when_no_cache` | method | `tests/test_cache.py:56` | `def test_load_returns_empty_dict_when_no_cache(self)` |
| `test_nonexistent_file_returns_empty_hash` | method | `tests/test_cache.py:100` | `def test_nonexistent_file_returns_empty_hash(self)` |
| `test_prune_deleted_removes_ghost_entries` | method | `tests/test_cache.py:85` | `def test_prune_deleted_removes_ghost_entries(self)` |
| `test_same_content_produces_same_hash` | method | `tests/test_cache.py:49` | `def test_same_content_produces_same_hash(self)` |
| `test_save_and_load_analysis_roundtrip` | method | `tests/test_cache.py:109` | `def test_save_and_load_analysis_roundtrip(self)` |
| `test_save_and_load_roundtrip` | method | `tests/test_cache.py:60` | `def test_save_and_load_roundtrip(self)` |
| `TestConfigContract` | class | `tests/test_config.py:7` | `class TestConfigContract(TestCase)` |
| `test_config_defaults_are_sane` | method | `tests/test_config.py:13` | `def test_config_defaults_are_sane(self)` |
| `test_config_is_immutable` | method | `tests/test_config.py:8` | `def test_config_is_immutable(self)` |
| `test_ignore_dirs_are_comprehensive` | method | `tests/test_config.py:24` | `def test_ignore_dirs_are_comprehensive(self)` |
| `test_plural_map_covers_all_symbol_types` | method | `tests/test_config.py:30` | `def test_plural_map_covers_all_symbol_types(self)` |
| `test_supported_extensions_no_duplicates` | method | `tests/test_config.py:41` | `def test_supported_extensions_no_duplicates(self)` |
| `TestCodePropertyGraphContract` | class | `tests/test_cpg.py:11` | `class TestCodePropertyGraphContract(TestCase)` |
| `_make_node` | method | `tests/test_cpg.py:18` | `def _make_node(self, nid, label, lang)` |
| `_make_sym` | method | `tests/test_cpg.py:21` | `def _make_sym(self, name, kind, line)` |
| `setUp` | method | `tests/test_cpg.py:14` | `def setUp(self)` |
| `test_empty_graph_returns_valid_json` | method | `tests/test_cpg.py:96` | `def test_empty_graph_returns_valid_json(self)` |
| `test_generate_includes_edges` | method | `tests/test_cpg.py:49` | `def test_generate_includes_edges(self)` |
| `test_generate_includes_metadata` | method | `tests/test_cpg.py:61` | `def test_generate_includes_metadata(self)` |
| `test_generate_includes_node_data` | method | `tests/test_cpg.py:33` | `def test_generate_includes_node_data(self)` |
| `test_generate_returns_valid_json` | method | `tests/test_cpg.py:24` | `def test_generate_returns_valid_json(self)` |
| `test_privacy_mode_strips_docs` | method | `tests/test_cpg.py:71` | `def test_privacy_mode_strips_docs(self)` |
| `test_sha256_hash_included` | method | `tests/test_cpg.py:89` | `def test_sha256_hash_included(self)` |
| `TestCursorRulesGeneratorContract` | class | `tests/test_cursorrules.py:18` | `class TestCursorRulesGeneratorContract(TestCase)` |
| `setUp` | method | `tests/test_cursorrules.py:21` | `def setUp(self)` |
| `test_generate_contains_base_rules` | method | `tests/test_cursorrules.py:33` | `def test_generate_contains_base_rules(self)` |
| `test_generate_contains_header` | method | `tests/test_cursorrules.py:29` | `def test_generate_contains_header(self)` |
| `test_generate_idempotent` | method | `tests/test_cursorrules.py:111` | `def test_generate_idempotent(self)` |
| `test_generate_includes_communities` | method | `tests/test_cursorrules.py:62` | `def test_generate_includes_communities(self)` |
| `test_generate_includes_god_nodes` | method | `tests/test_cursorrules.py:49` | `def test_generate_includes_god_nodes(self)` |
| `test_generate_includes_layer_constraints` | method | `tests/test_cursorrules.py:38` | `def test_generate_includes_layer_constraints(self)` |
| `test_generate_includes_violations` | method | `tests/test_cursorrules.py:82` | `def test_generate_includes_violations(self)` |
| `test_generate_limits_violations_to_ten` | method | `tests/test_cursorrules.py:95` | `def test_generate_limits_violations_to_ten(self)` |
| `test_generate_returns_string` | method | `tests/test_cursorrules.py:25` | `def test_generate_returns_string(self)` |
| `test_generate_writes_file_when_project_root` | method | `tests/test_cursorrules.py:103` | `def test_generate_writes_file_when_project_root(self)` |
| `TestDataflowContract` | class | `tests/test_dataflow.py:25` | `class TestDataflowContract(TestCase)` |
| `_analyze` | function | `tests/test_dataflow.py:17` | `def _analyze(body)` |
| `_node` | function | `tests/test_dataflow.py:8` | `def _node(node_id, funcs)` |
| `test_address_alias_pointer_not_dead` | method | `tests/test_dataflow.py:234` | `def test_address_alias_pointer_not_dead(self)` |
| `test_address_taken_suppresses_dead_store` | method | `tests/test_dataflow.py:369` | `def test_address_taken_suppresses_dead_store(self)` |
| `test_alias_pointer_store_initializes_array` | method | `tests/test_dataflow.py:272` | `def test_alias_pointer_store_initializes_array(self)` |
| `test_array_arg_to_filler_counts_as_init` | method | `tests/test_dataflow.py:173` | `def test_array_arg_to_filler_counts_as_init(self)` |
| `test_array_arg_to_readonly_still_uninit` | method | `tests/test_dataflow.py:181` | `def test_array_arg_to_readonly_still_uninit(self)` |
| `test_array_filled_in_decl_init_call` | method | `tests/test_dataflow.py:188` | `def test_array_filled_in_decl_init_call(self)` |
| `test_array_store_before_read_suppresses_uninit` | method | `tests/test_dataflow.py:248` | `def test_array_store_before_read_suppresses_uninit(self)` |
| `test_asm_output_counts_as_init` | method | `tests/test_dataflow.py:116` | `def test_asm_output_counts_as_init(self)` |
| `test_assert_macro_counts_as_null_check` | method | `tests/test_dataflow.py:352` | `def test_assert_macro_counts_as_null_check(self)` |
| `test_block_comment_malloc_ignored` | method | `tests/test_dataflow.py:225` | `def test_block_comment_malloc_ignored(self)` |
| `test_checked_alloc_clean` | method | `tests/test_dataflow.py:78` | `def test_checked_alloc_clean(self)` |
| `test_config_defaults` | method | `tests/test_dataflow.py:26` | `def test_config_defaults(self)` |
| `test_config_immutable` | method | `tests/test_dataflow.py:31` | `def test_config_immutable(self)` |
| `test_dead_store_detected` | method | `tests/test_dataflow.py:62` | `def test_dead_store_detected(self)` |
| `test_derived_pointer_not_dead` | method | `tests/test_dataflow.py:203` | `def test_derived_pointer_not_dead(self)` |
| `test_disabled_returns_empty` | method | `tests/test_dataflow.py:84` | `def test_disabled_returns_empty(self)` |
| `test_fd_lt_zero_counts_as_checked` | method | `tests/test_dataflow.py:123` | `def test_fd_lt_zero_counts_as_checked(self)` |
| `test_file_scope_symbol_still_bounds_span` | method | `tests/test_dataflow.py:329` | `def test_file_scope_symbol_still_bounds_span(self)` |
| `test_function_pointer_call_counts_as_use` | method | `tests/test_dataflow.py:290` | `def test_function_pointer_call_counts_as_use(self)` |
| `test_initialized_use_clean` | method | `tests/test_dataflow.py:46` | `def test_initialized_use_clean(self)` |
| `test_inline_alias_fill_suppresses_uninit` | method | `tests/test_dataflow.py:281` | `def test_inline_alias_fill_suppresses_uninit(self)` |
| `test_issue_cap_respected` | method | `tests/test_dataflow.py:96` | `def test_issue_cap_respected(self)` |
| `test_line_numbers_survive_subscript_stores` | method | `tests/test_dataflow.py:156` | `def test_line_numbers_survive_subscript_stores(self)` |
| `test_local_struct_does_not_truncate_span` | method | `tests/test_dataflow.py:305` | `def test_local_struct_does_not_truncate_span(self)` |
| `test_loop_carried_var_not_dead` | method | `tests/test_dataflow.py:144` | `def test_loop_carried_var_not_dead(self)` |
| `test_map_failed_counts_as_checked` | method | `tests/test_dataflow.py:129` | `def test_map_failed_counts_as_checked(self)` |
| `test_member_null_check_counts` | method | `tests/test_dataflow.py:136` | `def test_member_null_check_counts(self)` |
| `test_member_store_initializes_base` | method | `tests/test_dataflow.py:377` | `def test_member_store_initializes_base(self)` |
| `test_member_store_not_local_assign` | method | `tests/test_dataflow.py:167` | `def test_member_store_not_local_assign(self)` |
| `test_missing_content_skipped` | method | `tests/test_dataflow.py:91` | `def test_missing_content_skipped(self)` |
| `test_multiline_call_assigns_array_arg` | method | `tests/test_dataflow.py:360` | `def test_multiline_call_assigns_array_arg(self)` |
| `test_params_count_as_initialized` | method | `tests/test_dataflow.py:50` | `def test_params_count_as_initialized(self)` |
| `test_plain_assignment_is_not_a_declaration` | method | `tests/test_dataflow.py:105` | `def test_plain_assignment_is_not_a_declaration(self)` |
| `test_plain_call_is_not_a_local_use` | method | `tests/test_dataflow.py:298` | `def test_plain_call_is_not_a_local_use(self)` |
| `test_read_store_clean` | method | `tests/test_dataflow.py:67` | `def test_read_store_clean(self)` |
| `test_same_line_only_assign_is_dead` | method | `tests/test_dataflow.py:264` | `def test_same_line_only_assign_is_dead(self)` |
| `test_same_line_use_not_dead` | method | `tests/test_dataflow.py:256` | `def test_same_line_use_not_dead(self)` |
| `test_scanf_addr_counts_as_init` | method | `tests/test_dataflow.py:58` | `def test_scanf_addr_counts_as_init(self)` |
| `test_sizeof_is_not_a_read` | method | `tests/test_dataflow.py:216` | `def test_sizeof_is_not_a_read(self)` |
| `test_static_never_uninit` | method | `tests/test_dataflow.py:196` | `def test_static_never_uninit(self)` |
| `test_subscript_store_counts_as_init` | method | `tests/test_dataflow.py:110` | `def test_subscript_store_counts_as_init(self)` |
| `test_unchecked_alloc_detected` | method | `tests/test_dataflow.py:71` | `def test_unchecked_alloc_detected(self)` |
| `test_uninit_use_detected` | method | `tests/test_dataflow.py:37` | `def test_uninit_use_detected(self)` |
| `test_url_string_does_not_truncate_line` | method | `tests/test_dataflow.py:344` | `def test_url_string_does_not_truncate_line(self)` |
| `TestDeadCodeStripperContract` | class | `tests/test_dead_code.py:16` | `class TestDeadCodeStripperContract(TestCase)` |
| `_make_edge` | method | `tests/test_dead_code.py:35` | `def _make_edge(self, src, tgt)` |
| `_make_node` | method | `tests/test_dead_code.py:26` | `def _make_node(self, nid, symbols)` |
| `_make_symbol` | method | `tests/test_dead_code.py:23` | `def _make_symbol(self, name, kind)` |
| `setUp` | method | `tests/test_dead_code.py:19` | `def setUp(self)` |
| `test_all_symbols_imported_returns_empty` | method | `tests/test_dead_code.py:101` | `def test_all_symbols_imported_returns_empty(self)` |
| `test_identify_empty_graph_returns_empty` | method | `tests/test_dead_code.py:38` | `def test_identify_empty_graph_returns_empty(self)` |
| `test_identify_excludes_app_entry_point` | method | `tests/test_dead_code.py:61` | `def test_identify_excludes_app_entry_point(self)` |
| `test_identify_excludes_entry_points` | method | `tests/test_dead_code.py:53` | `def test_identify_excludes_entry_points(self)` |
| `test_identify_excludes_init_entry_point` | method | `tests/test_dead_code.py:69` | `def test_identify_excludes_init_entry_point(self)` |
| `test_identify_finds_dead_symbol` | method | `tests/test_dead_code.py:42` | `def test_identify_finds_dead_symbol(self)` |
| `test_identify_recommends_review_for_classes` | method | `tests/test_dead_code.py:77` | `def test_identify_recommends_review_for_classes(self)` |
| `test_identify_recommends_trash_for_functions` | method | `tests/test_dead_code.py:85` | `def test_identify_recommends_trash_for_functions(self)` |
| `test_identify_recommends_trash_for_variables` | method | `tests/test_dead_code.py:93` | `def test_identify_recommends_trash_for_variables(self)` |
| `test_reports_sorted_by_file_path` | method | `tests/test_dead_code.py:113` | `def test_reports_sorted_by_file_path(self)` |
| `TestDiagramVariantsContract` | class | `tests/test_diagrams.py:619` | `class TestDiagramVariantsContract(TestCase)` |
| `TestDocsSitePublisherContract` | class | `tests/test_diagrams.py:360` | `class TestDocsSitePublisherContract(TestCase)` |
| `TestInteractiveMapRendererContract` | class | `tests/test_diagrams.py:237` | `class TestInteractiveMapRendererContract(TestCase)` |
| `TestSystemMapBuilderContract` | class | `tests/test_diagrams.py:30` | `class TestSystemMapBuilderContract(TestCase)` |
| `TestSystemMapValidatorContract` | class | `tests/test_diagrams.py:176` | `class TestSystemMapValidatorContract(TestCase)` |
| `TestVisNetworkRendererContract` | class | `tests/test_diagrams.py:503` | `class TestVisNetworkRendererContract(TestCase)` |
| `_make_graph` | method | `tests/test_diagrams.py:38` | `def _make_graph(self)` |
| `_map` | method | `tests/test_diagrams.py:246` | `def _map(self, kind)` |
| `_map` | method | `tests/test_diagrams.py:512` | `def _map(self, kind)` |
| `_maps` | method | `tests/test_diagrams.py:369` | `def _maps(self)` |
| `_project` | method | `tests/test_diagrams.py:622` | `def _project(self, tmp)` |
| `_valid_map` | method | `tests/test_diagrams.py:184` | `def _valid_map(self)` |
| `setUp` | method | `tests/test_diagrams.py:33` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:179` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:240` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:363` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:506` | `def setUp(self)` |
| `test_builder_attaches_symbols_and_docs` | method | `tests/test_diagrams.py:126` | `def test_builder_attaches_symbols_and_docs(self)` |
| `test_builder_is_deterministic` | method | `tests/test_diagrams.py:68` | `def test_builder_is_deterministic(self)` |
| `test_builder_orders_links_deterministically` | method | `tests/test_diagrams.py:80` | `def test_builder_orders_links_deterministically(self)` |
| `test_builder_produces_all_kinds` | method | `tests/test_diagrams.py:59` | `def test_builder_produces_all_kinds(self)` |
| `test_builder_reports_total_scope` | method | `tests/test_diagrams.py:119` | `def test_builder_reports_total_scope(self)` |
| `test_builder_supports_five_kinds` | method | `tests/test_diagrams.py:52` | `def test_builder_supports_five_kinds(self)` |
| `test_builder_truncates_symbols_per_node` | method | `tests/test_diagrams.py:143` | `def test_builder_truncates_symbols_per_node(self)` |
| `test_builder_truncates_to_configured_limit` | method | `tests/test_diagrams.py:152` | `def test_builder_truncates_to_configured_limit(self)` |
| `test_builder_validates_large_graph_for_all_kinds` | method | `tests/test_diagrams.py:101` | `def test_builder_validates_large_graph_for_all_kinds(self)` |
| `test_compare_reports_added_removed_rerouted` | method | `tests/test_diagrams.py:162` | `def test_compare_reports_added_removed_rerouted(self)` |
| `test_export_diagrams_falls_back_offline_when_disabled` | method | `tests/test_diagrams.py:641` | `def test_export_diagrams_falls_back_offline_when_disabled(self)` |
| `test_export_diagrams_writes_vis_maps_by_default` | method | `tests/test_diagrams.py:627` | `def test_export_diagrams_writes_vis_maps_by_default(self)` |
| `test_publish_card_reports_primary_scope` | method | `tests/test_diagrams.py:494` | `def test_publish_card_reports_primary_scope(self)` |
| `test_publish_empty_maps_writes_empty_gallery` | method | `tests/test_diagrams.py:455` | `def test_publish_empty_maps_writes_empty_gallery(self)` |
| `test_publish_escapes_malicious_project_name` | method | `tests/test_diagrams.py:423` | `def test_publish_escapes_malicious_project_name(self)` |
| `test_publish_escapes_malicious_stat_keys` | method | `tests/test_diagrams.py:432` | `def test_publish_escapes_malicious_stat_keys(self)` |
| `test_publish_flat_subdir_keeps_links_relative` | method | `tests/test_diagrams.py:473` | `def test_publish_flat_subdir_keeps_links_relative(self)` |
| `test_publish_index_explains_how_to_read` | method | `tests/test_diagrams.py:486` | `def test_publish_index_explains_how_to_read(self)` |
| `test_publish_index_links_every_map` | method | `tests/test_diagrams.py:390` | `def test_publish_index_links_every_map(self)` |
| `test_publish_is_deterministic` | method | `tests/test_diagrams.py:412` | `def test_publish_is_deterministic(self)` |
| `test_publish_leaves_input_maps_unmodified` | method | `tests/test_diagrams.py:464` | `def test_publish_leaves_input_maps_unmodified(self)` |
| `test_publish_output_has_no_external_requests` | method | `tests/test_diagrams.py:399` | `def test_publish_output_has_no_external_requests(self)` |
| `test_publish_skips_invalid_maps` | method | `tests/test_diagrams.py:443` | `def test_publish_skips_invalid_maps(self)` |
| `test_publish_writes_index_plus_five_maps` | method | `tests/test_diagrams.py:379` | `def test_publish_writes_index_plus_five_maps(self)` |
| `test_renderer_builds_vis_network_with_physics` | method | `tests/test_diagrams.py:535` | `def test_renderer_builds_vis_network_with_physics(self)` |
| `test_renderer_buttons_explain_their_purpose` | method | `tests/test_diagrams.py:348` | `def test_renderer_buttons_explain_their_purpose(self)` |
| `test_renderer_covers_all_five_kinds` | method | `tests/test_diagrams.py:307` | `def test_renderer_covers_all_five_kinds(self)` |
| `test_renderer_disables_physics_from_config` | method | `tests/test_diagrams.py:551` | `def test_renderer_disables_physics_from_config(self)` |
| `test_renderer_documents_symbols_per_file` | method | `tests/test_diagrams.py:590` | `def test_renderer_documents_symbols_per_file(self)` |
| `test_renderer_embeds_valid_json_payloads` | method | `tests/test_diagrams.py:298` | `def test_renderer_embeds_valid_json_payloads(self)` |
| `test_renderer_embeds_valid_payloads` | method | `tests/test_diagrams.py:582` | `def test_renderer_embeds_valid_payloads(self)` |
| `test_renderer_escapes_malicious_labels` | method | `tests/test_diagrams.py:285` | `def test_renderer_escapes_malicious_labels(self)` |
| `test_renderer_escapes_malicious_symbol_docs` | method | `tests/test_diagrams.py:606` | `def test_renderer_escapes_malicious_symbol_docs(self)` |
| `test_renderer_escapes_malicious_titles` | method | `tests/test_diagrams.py:558` | `def test_renderer_escapes_malicious_titles(self)` |
| `test_renderer_exposes_reader_controls` | method | `tests/test_diagrams.py:571` | `def test_renderer_exposes_reader_controls(self)` |
| `test_renderer_has_no_external_requests` | method | `tests/test_diagrams.py:263` | `def test_renderer_has_no_external_requests(self)` |
| `test_renderer_includes_interaction_controls` | method | `tests/test_diagrams.py:270` | `def test_renderer_includes_interaction_controls(self)` |
| `test_renderer_includes_keyboard_and_deep_links` | method | `tests/test_diagrams.py:276` | `def test_renderer_includes_keyboard_and_deep_links(self)` |
| `test_renderer_is_deterministic` | method | `tests/test_diagrams.py:577` | `def test_renderer_is_deterministic(self)` |
| `test_renderer_keeps_canvas_distinct_from_nodes` | method | `tests/test_diagrams.py:326` | `def test_renderer_keeps_canvas_distinct_from_nodes(self)` |
| `test_renderer_links_gallery_home_when_configured` | method | `tests/test_diagrams.py:314` | `def test_renderer_links_gallery_home_when_configured(self)` |
| `test_renderer_links_gallery_home_when_configured` | method | `tests/test_diagrams.py:543` | `def test_renderer_links_gallery_home_when_configured(self)` |
| `test_renderer_omits_gallery_home_by_default` | method | `tests/test_diagrams.py:321` | `def test_renderer_omits_gallery_home_by_default(self)` |
| `test_renderer_produces_standalone_document` | method | `tests/test_diagrams.py:256` | `def test_renderer_produces_standalone_document(self)` |
| `test_renderer_sanitizes_viewer_state_on_export` | method | `tests/test_diagrams.py:342` | `def test_renderer_sanitizes_viewer_state_on_export(self)` |
| `test_renderer_supports_drag_and_settle` | method | `tests/test_diagrams.py:334` | `def test_renderer_supports_drag_and_settle(self)` |
| `test_renderer_uses_configured_cdn_urls` | method | `tests/test_diagrams.py:522` | `def test_renderer_uses_configured_cdn_urls(self)` |
| `test_validator_passes_valid_map` | method | `tests/test_diagrams.py:197` | `def test_validator_passes_valid_map(self)` |
| `test_validator_rejects_dangling_edge` | method | `tests/test_diagrams.py:214` | `def test_validator_rejects_dangling_edge(self)` |
| `test_validator_rejects_duplicate_node_ids` | method | `tests/test_diagrams.py:204` | `def test_validator_rejects_duplicate_node_ids(self)` |
| `test_validator_rejects_empty_map` | method | `tests/test_diagrams.py:222` | `def test_validator_rejects_empty_map(self)` |
| `test_validator_rejects_unknown_kind` | method | `tests/test_diagrams.py:228` | `def test_validator_rejects_unknown_kind(self)` |
| `TestDocumentationGeneratorContract` | class | `tests/test_documentation.py:17` | `class TestDocumentationGeneratorContract(TestCase)` |
| `setUp` | method | `tests/test_documentation.py:18` | `def setUp(self)` |
| `test_architectural_layers_section` | method | `tests/test_documentation.py:217` | `def test_architectural_layers_section(self)` |
| `test_class_symbol_is_pluralized_correctly` | method | `tests/test_documentation.py:83` | `def test_class_symbol_is_pluralized_correctly(self)` |
| `test_contains_architecture_reference` | method | `tests/test_documentation.py:37` | `def test_contains_architecture_reference(self)` |
| `test_contains_cpg_block` | method | `tests/test_documentation.py:41` | `def test_contains_cpg_block(self)` |
| `test_contains_header` | method | `tests/test_documentation.py:22` | `def test_contains_header(self)` |
| `test_contains_mermaid_block` | method | `tests/test_documentation.py:32` | `def test_contains_mermaid_block(self)` |
| `test_contains_metadata_line` | method | `tests/test_documentation.py:26` | `def test_contains_metadata_line(self)` |
| `test_contains_statistics_dashboard` | method | `tests/test_documentation.py:46` | `def test_contains_statistics_dashboard(self)` |
| `test_context_budget_includes_security_findings` | method | `tests/test_documentation.py:293` | `def test_context_budget_includes_security_findings(self)` |
| `test_context_budget_prioritizes_god_nodes` | method | `tests/test_documentation.py:268` | `def test_context_budget_prioritizes_god_nodes(self)` |
| `test_context_budget_returns_compact_summary` | method | `tests/test_documentation.py:260` | `def test_context_budget_returns_compact_summary(self)` |
| `test_context_budget_truncates_at_limit` | method | `tests/test_documentation.py:285` | `def test_context_budget_truncates_at_limit(self)` |
| `test_context_budget_zero_returns_full_content` | method | `tests/test_documentation.py:252` | `def test_context_budget_zero_returns_full_content(self)` |
| `test_cpg_block_disabled_via_config` | method | `tests/test_documentation.py:211` | `def test_cpg_block_disabled_via_config(self)` |
| `test_docstring_in_output` | method | `tests/test_documentation.py:143` | `def test_docstring_in_output(self)` |
| `test_function_pluralization` | method | `tests/test_documentation.py:97` | `def test_function_pluralization(self)` |
| `test_groups_files_by_language` | method | `tests/test_documentation.py:51` | `def test_groups_files_by_language(self)` |
| `test_hotspot_section_present` | method | `tests/test_documentation.py:185` | `def test_hotspot_section_present(self)` |
| `test_includes_file_path` | method | `tests/test_documentation.py:132` | `def test_includes_file_path(self)` |
| `test_lists_symbols_under_file` | method | `tests/test_documentation.py:70` | `def test_lists_symbols_under_file(self)` |
| `test_method_pluralization` | method | `tests/test_documentation.py:109` | `def test_method_pluralization(self)` |
| `test_no_hotspot_section_when_empty` | method | `tests/test_documentation.py:207` | `def test_no_hotspot_section_when_empty(self)` |
| `test_no_taint_section_when_empty` | method | `tests/test_documentation.py:203` | `def test_no_taint_section_when_empty(self)` |
| `test_security_findings_section` | method | `tests/test_documentation.py:229` | `def test_security_findings_section(self)` |
| `test_shows_no_symbols_for_empty_files` | method | `tests/test_documentation.py:121` | `def test_shows_no_symbols_for_empty_files(self)` |
| `test_taint_propagation_section_present` | method | `tests/test_documentation.py:165` | `def test_taint_propagation_section_present(self)` |
| `test_truncation_note_when_limited` | method | `tests/test_documentation.py:155` | `def test_truncation_note_when_limited(self)` |
| `TestGraphExporterContract` | class | `tests/test_exporter.py:23` | `class TestGraphExporterContract(TestCase)` |
| `_make_node` | method | `tests/test_exporter.py:30` | `def _make_node(self, nid, label, lang, symbols)` |
| `_make_sym` | method | `tests/test_exporter.py:42` | `def _make_sym(self, name, kind, line)` |
| `setUp` | method | `tests/test_exporter.py:26` | `def setUp(self)` |
| `test_to_html_includes_community_legend_when_analysis` | method | `tests/test_exporter.py:116` | `def test_to_html_includes_community_legend_when_analysis(self)` |
| `test_to_html_includes_node_data` | method | `tests/test_exporter.py:109` | `def test_to_html_includes_node_data(self)` |
| `test_to_html_produces_standalone_page` | method | `tests/test_exporter.py:101` | `def test_to_html_produces_standalone_page(self)` |
| `test_to_json_handles_resolved_edges` | method | `tests/test_exporter.py:160` | `def test_to_json_handles_resolved_edges(self)` |
| `test_to_json_includes_analysis_metadata` | method | `tests/test_exporter.py:76` | `def test_to_json_includes_analysis_metadata(self)` |
| `test_to_json_includes_metadata` | method | `tests/test_exporter.py:65` | `def test_to_json_includes_metadata(self)` |
| `test_to_json_includes_symbol_data` | method | `tests/test_exporter.py:56` | `def test_to_json_includes_symbol_data(self)` |
| `test_to_json_produces_valid_json` | method | `tests/test_exporter.py:47` | `def test_to_json_produces_valid_json(self)` |
| `test_to_svg_includes_readmenator_title` | method | `tests/test_exporter.py:154` | `def test_to_svg_includes_readmenator_title(self)` |
| `test_to_svg_produces_svg_string` | method | `tests/test_exporter.py:138` | `def test_to_svg_produces_svg_string(self)` |
| `test_to_svg_render_truncation_for_large_graph` | method | `tests/test_exporter.py:145` | `def test_to_svg_render_truncation_for_large_graph(self)` |
| `TestHotspotAnalyzerContract` | class | `tests/test_hotspots.py:10` | `class TestHotspotAnalyzerContract(TestCase)` |
| `_make_node` | method | `tests/test_hotspots.py:17` | `def _make_node(self, nid, label, sym_count)` |
| `setUp` | method | `tests/test_hotspots.py:13` | `def setUp(self)` |
| `test_change_impact_no_edges` | method | `tests/test_hotspots.py:94` | `def test_change_impact_no_edges(self)` |
| `test_change_impact_ranks_by_total_impact` | method | `tests/test_hotspots.py:79` | `def test_change_impact_ranks_by_total_impact(self)` |
| `test_detects_simple_cycle` | method | `tests/test_hotspots.py:66` | `def test_detects_simple_cycle(self)` |
| `test_empty_graph_returns_empty_hotspots` | method | `tests/test_hotspots.py:29` | `def test_empty_graph_returns_empty_hotspots(self)` |
| `test_hotspot_includes_scores` | method | `tests/test_hotspots.py:43` | `def test_hotspot_includes_scores(self)` |
| `test_hotspot_weights_from_config` | method | `tests/test_hotspots.py:100` | `def test_hotspot_weights_from_config(self)` |
| `test_hotspots_rank_by_combined_score` | method | `tests/test_hotspots.py:33` | `def test_hotspots_rank_by_combined_score(self)` |
| `test_no_cycles_in_acyclic_graph` | method | `tests/test_hotspots.py:53` | `def test_no_cycles_in_acyclic_graph(self)` |
| `TestEndToEndContract` | class | `tests/test_integration.py:9` | `class TestEndToEndContract(TestCase)` |
| `_write` | method | `tests/test_integration.py:19` | `def _write(self, path, content)` |
| `setUp` | method | `tests/test_integration.py:10` | `def setUp(self)` |
| `tearDown` | method | `tests/test_integration.py:15` | `def tearDown(self)` |
| `test_audit_deep_returns_analysis` | method | `tests/test_integration.py:98` | `def test_audit_deep_returns_analysis(self)` |
| `test_explain_subcommand_works` | method | `tests/test_integration.py:53` | `def test_explain_subcommand_works(self)` |
| `test_export_sarif_produces_file` | method | `tests/test_integration.py:114` | `def test_export_sarif_produces_file(self)` |
| `test_full_pipeline_generates_knowledge_base` | method | `tests/test_integration.py:24` | `def test_full_pipeline_generates_knowledge_base(self)` |
| `test_knowledge_base_contains_cpg` | method | `tests/test_integration.py:81` | `def test_knowledge_base_contains_cpg(self)` |
| `test_knowledge_base_contains_mermaid` | method | `tests/test_integration.py:40` | `def test_knowledge_base_contains_mermaid(self)` |
| `test_knowledge_base_contains_statistics_dashboard` | method | `tests/test_integration.py:89` | `def test_knowledge_base_contains_statistics_dashboard(self)` |
| `test_path_subcommand_works` | method | `tests/test_integration.py:59` | `def test_path_subcommand_works(self)` |
| `test_privacy_mode_works` | method | `tests/test_integration.py:105` | `def test_privacy_mode_works(self)` |
| `test_query_subcommand_works` | method | `tests/test_integration.py:48` | `def test_query_subcommand_works(self)` |
| `test_rebuild` | method | `tests/test_integration.py:71` | `def test_rebuild(self)` |
| `test_summary_works` | method | `tests/test_integration.py:65` | `def test_summary_works(self)` |
| `TestLayerRuleEngineContract` | class | `tests/test_layer_rules.py:10` | `class TestLayerRuleEngineContract(TestCase)` |
| `_make_node` | method | `tests/test_layer_rules.py:17` | `def _make_node(self, nid, label)` |
| `setUp` | method | `tests/test_layer_rules.py:13` | `def setUp(self)` |
| `test_allowed_testing_edges_no_violation` | method | `tests/test_layer_rules.py:46` | `def test_allowed_testing_edges_no_violation(self)` |
| `test_empty_graph_returns_empty_violations` | method | `tests/test_layer_rules.py:20` | `def test_empty_graph_returns_empty_violations(self)` |
| `test_forbidden_edge_detected` | method | `tests/test_layer_rules.py:36` | `def test_forbidden_edge_detected(self)` |
| `test_multiple_violations` | method | `tests/test_layer_rules.py:57` | `def test_multiple_violations(self)` |
| `test_no_layers_returns_empty_violations` | method | `tests/test_layer_rules.py:24` | `def test_no_layers_returns_empty_violations(self)` |
| `test_presentation_to_data_access_forbidden` | method | `tests/test_layer_rules.py:115` | `def test_presentation_to_data_access_forbidden(self)` |
| `test_resolved_edges_also_checked` | method | `tests/test_layer_rules.py:104` | `def test_resolved_edges_also_checked(self)` |
| `test_same_layer_no_violation` | method | `tests/test_layer_rules.py:29` | `def test_same_layer_no_violation(self)` |
| `test_utility_layer_ignored` | method | `tests/test_layer_rules.py:75` | `def test_utility_layer_ignored(self)` |
| `test_violation_summary` | method | `tests/test_layer_rules.py:82` | `def test_violation_summary(self)` |
| `TestArchitectureLinterContract` | class | `tests/test_linter.py:16` | `class TestArchitectureLinterContract(TestCase)` |
| `_make_edge` | method | `tests/test_linter.py:26` | `def _make_edge(self, src, tgt, rel)` |
| `_make_node` | method | `tests/test_linter.py:23` | `def _make_node(self, nid, label, lang)` |
| `setUp` | method | `tests/test_linter.py:19` | `def setUp(self)` |
| `test_lint_allows_same_layer_imports` | method | `tests/test_linter.py:61` | `def test_lint_allows_same_layer_imports(self)` |
| `test_lint_allows_testing_to_business_logic` | method | `tests/test_linter.py:72` | `def test_lint_allows_testing_to_business_logic(self)` |
| `test_lint_detects_circular_dependencies` | method | `tests/test_linter.py:94` | `def test_lint_detects_circular_dependencies(self)` |
| `test_lint_detects_cross_layer_violation` | method | `tests/test_linter.py:49` | `def test_lint_detects_cross_layer_violation(self)` |
| `test_lint_detects_file_exceeding_max_lines` | method | `tests/test_linter.py:40` | `def test_lint_detects_file_exceeding_max_lines(self)` |
| `test_lint_empty_graph_returns_no_violations` | method | `tests/test_linter.py:29` | `def test_lint_empty_graph_returns_no_violations(self)` |
| `test_lint_ignores_utility_layer` | method | `tests/test_linter.py:83` | `def test_lint_ignores_utility_layer(self)` |
| `test_lint_returns_empty_for_files_under_threshold` | method | `tests/test_linter.py:33` | `def test_lint_returns_empty_for_files_under_threshold(self)` |
| `test_lint_returns_empty_when_disabled` | method | `tests/test_linter.py:121` | `def test_lint_returns_empty_when_disabled(self)` |
| `test_violations_sorted_by_severity` | method | `tests/test_linter.py:108` | `def test_violations_sorted_by_severity(self)` |
| `TestMCPProtocol` | class | `tests/test_mcp_server.py:21` | `class TestMCPProtocol(TestCase)` |
| `_call` | method | `tests/test_mcp_server.py:42` | `def _call(self, req)` |
| `_get_tool_def` | method | `tests/test_mcp_server.py:219` | `def _get_tool_def(self, name)` |
| `_make_request` | method | `tests/test_mcp_server.py:36` | `def _make_request(self, method, params, msg_id)` |
| `setUp` | method | `tests/test_mcp_server.py:24` | `def setUp(self)` |
| `tearDown` | method | `tests/test_mcp_server.py:33` | `def tearDown(self)` |
| `test_call_query_tool_missing_required_param_raises` | method | `tests/test_mcp_server.py:154` | `def test_call_query_tool_missing_required_param_raises(self)` |
| `test_call_query_tool_with_text_returns_results` | method | `tests/test_mcp_server.py:145` | `def test_call_query_tool_with_text_returns_results(self)` |
| `test_call_summary_tool_returns_content` | method | `tests/test_mcp_server.py:132` | `def test_call_summary_tool_returns_content(self)` |
| `test_call_tool_returns_text_content_list` | method | `tests/test_mcp_server.py:251` | `def test_call_tool_returns_text_content_list(self)` |
| `test_call_tool_unknown_tool_returns_method_not_found` | method | `tests/test_mcp_server.py:123` | `def test_call_tool_unknown_tool_returns_method_not_found(self)` |
| `test_call_tool_without_initialize_returns_error` | method | `tests/test_mcp_server.py:115` | `def test_call_tool_without_initialize_returns_error(self)` |
| `test_explain_tool_requires_name_param` | method | `tests/test_mcp_server.py:230` | `def test_explain_tool_requires_name_param(self)` |
| `test_initialize_exchanges_protocol_version` | method | `tests/test_mcp_server.py:49` | `def test_initialize_exchanges_protocol_version(self)` |
| `test_list_resources_returns_resource_definitions` | method | `tests/test_mcp_server.py:168` | `def test_list_resources_returns_resource_definitions(self)` |
| `test_list_tools_returns_all_tool_definitions` | method | `tests/test_mcp_server.py:85` | `def test_list_tools_returns_all_tool_definitions(self)` |
| `test_notifications_initialized_returns_no_response` | method | `tests/test_mcp_server.py:62` | `def test_notifications_initialized_returns_no_response(self)` |
| `test_parse_error_for_invalid_json` | method | `tests/test_mcp_server.py:243` | `def test_parse_error_for_invalid_json(self)` |
| `test_path_tool_requires_two_params` | method | `tests/test_mcp_server.py:234` | `def test_path_tool_requires_two_params(self)` |
| `test_query_tool_requires_text_param` | method | `tests/test_mcp_server.py:226` | `def test_query_tool_requires_text_param(self)` |
| `test_read_resource_kb_returns_markdown` | method | `tests/test_mcp_server.py:205` | `def test_read_resource_kb_returns_markdown(self)` |
| `test_read_resource_summary_returns_json` | method | `tests/test_mcp_server.py:186` | `def test_read_resource_summary_returns_json(self)` |
| `test_read_resource_unknown_uri_returns_error` | method | `tests/test_mcp_server.py:197` | `def test_read_resource_unknown_uri_returns_error(self)` |
| `test_uninitialized_request_returns_error` | method | `tests/test_mcp_server.py:75` | `def test_uninitialized_request_returns_error(self)` |
| `test_unknown_method_returns_error` | method | `tests/test_mcp_server.py:67` | `def test_unknown_method_returns_error(self)` |
| `TestMermaidRendererContract` | class | `tests/test_mermaid.py:7` | `class TestMermaidRendererContract(TestCase)` |
| `setUp` | method | `tests/test_mermaid.py:8` | `def setUp(self)` |
| `test_class_symbol_gets_cls_style` | method | `tests/test_mermaid.py:36` | `def test_class_symbol_gets_cls_style(self)` |
| `test_external_import_edge_is_dashed` | method | `tests/test_mermaid.py:54` | `def test_external_import_edge_is_dashed(self)` |
| `test_function_symbol_gets_fn_style` | method | `tests/test_mermaid.py:45` | `def test_function_symbol_gets_fn_style(self)` |
| `test_handles_special_characters_in_ids` | method | `tests/test_mermaid.py:82` | `def test_handles_special_characters_in_ids(self)` |
| `test_limits_symbols_to_five_per_node` | method | `tests/test_mermaid.py:72` | `def test_limits_symbols_to_five_per_node(self)` |
| `test_renders_graph_header` | method | `tests/test_mermaid.py:11` | `def test_renders_graph_header(self)` |
| `test_renders_module_node` | method | `tests/test_mermaid.py:19` | `def test_renders_module_node(self)` |
| `test_renders_symbol_subnodes` | method | `tests/test_mermaid.py:27` | `def test_renders_symbol_subnodes(self)` |
| `test_truncation_when_over_limit` | method | `tests/test_mermaid.py:62` | `def test_truncation_when_over_limit(self)` |
| `TestEdgeContract` | class | `tests/test_models.py:48` | `class TestEdgeContract(TestCase)` |
| `TestNodeContract` | class | `tests/test_models.py:20` | `class TestNodeContract(TestCase)` |
| `TestPluralizeContract` | class | `tests/test_models.py:56` | `class TestPluralizeContract(TestCase)` |
| `TestSymbolContract` | class | `tests/test_models.py:6` | `class TestSymbolContract(TestCase)` |
| `test_edge_creation` | method | `tests/test_models.py:49` | `def test_edge_creation(self)` |
| `test_node_creation` | method | `tests/test_models.py:21` | `def test_node_creation(self)` |
| `test_node_with_symbols` | method | `tests/test_models.py:35` | `def test_node_with_symbols(self)` |
| `test_pluralize_class` | method | `tests/test_models.py:57` | `def test_pluralize_class(self)` |
| `test_pluralize_unknown_appends_s` | method | `tests/test_models.py:62` | `def test_pluralize_unknown_appends_s(self)` |
| `test_symbol_creation` | method | `tests/test_models.py:7` | `def test_symbol_creation(self)` |
| `test_symbol_with_signature` | method | `tests/test_models.py:15` | `def test_symbol_with_signature(self)` |
| `TestAssemblyParserContract` | class | `tests/test_parsers.py:456` | `class TestAssemblyParserContract(TestCase)` |
| `TestCParserContract` | class | `tests/test_parsers.py:22` | `class TestCParserContract(TestCase)` |
| `TestCSharpParserContract` | class | `tests/test_parsers.py:309` | `class TestCSharpParserContract(TestCase)` |
| `TestDartParserContract` | class | `tests/test_parsers.py:387` | `class TestDartParserContract(TestCase)` |
| `TestGDScriptParserContract` | class | `tests/test_parsers.py:412` | `class TestGDScriptParserContract(TestCase)` |
| `TestGoParserContract` | class | `tests/test_parsers.py:157` | `class TestGoParserContract(TestCase)` |
| `TestJavaParserContract` | class | `tests/test_parsers.py:277` | `class TestJavaParserContract(TestCase)` |
| `TestJavaScriptParserContract` | class | `tests/test_parsers.py:238` | `class TestJavaScriptParserContract(TestCase)` |
| `TestNimParserContract` | class | `tests/test_parsers.py:430` | `class TestNimParserContract(TestCase)` |
| `TestPHPParserContract` | class | `tests/test_parsers.py:361` | `class TestPHPParserContract(TestCase)` |
| `TestParserFactoryContract` | class | `tests/test_parsers.py:483` | `class TestParserFactoryContract(TestCase)` |
| `TestPythonParserContract` | class | `tests/test_parsers.py:88` | `class TestPythonParserContract(TestCase)` |
| `TestRustParserContract` | class | `tests/test_parsers.py:200` | `class TestRustParserContract(TestCase)` |
| `TestShellParserContract` | class | `tests/test_parsers.py:342` | `class TestShellParserContract(TestCase)` |
| `setUp` | method | `tests/test_parsers.py:23` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:89` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:158` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:201` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:239` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:278` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:310` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:343` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:362` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:388` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:413` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:431` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:457` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers.py:484` | `def setUp(self)` |
| `test_abstract_class` | method | `tests/test_parsers.py:301` | `def test_abstract_class(self)` |
| `test_calls_are_not_prototypes` | method | `tests/test_parsers.py:71` | `def test_calls_are_not_prototypes(self)` |
| `test_case_insensitive_extension` | method | `tests/test_parsers.py:507` | `def test_case_insensitive_extension(self)` |
| `test_class_with_inheritance` | method | `tests/test_parsers.py:80` | `def test_class_with_inheritance(self)` |
| `test_extracts_arrow_function` | method | `tests/test_parsers.py:249` | `def test_extracts_arrow_function(self)` |
| `test_extracts_async_function` | method | `tests/test_parsers.py:114` | `def test_extracts_async_function(self)` |
| `test_extracts_class` | method | `tests/test_parsers.py:99` | `def test_extracts_class(self)` |
| `test_extracts_class` | method | `tests/test_parsers.py:256` | `def test_extracts_class(self)` |
| `test_extracts_class` | method | `tests/test_parsers.py:281` | `def test_extracts_class(self)` |
| `test_extracts_class` | method | `tests/test_parsers.py:313` | `def test_extracts_class(self)` |
| `test_extracts_class` | method | `tests/test_parsers.py:372` | `def test_extracts_class(self)` |
| `test_extracts_class` | method | `tests/test_parsers.py:391` | `def test_extracts_class(self)` |
| `test_extracts_class_with_bases` | method | `tests/test_parsers.py:147` | `def test_extracts_class_with_bases(self)` |
| `test_extracts_define` | method | `tests/test_parsers.py:47` | `def test_extracts_define(self)` |
| `test_extracts_extends` | method | `tests/test_parsers.py:423` | `def test_extracts_extends(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:26` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:92` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:161` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:204` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:242` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:365` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:398` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers.py:416` | `def test_extracts_function(self)` |
| `test_extracts_function_keyword` | method | `tests/test_parsers.py:353` | `def test_extracts_function_keyword(self)` |
| `test_extracts_function_with_parentheses` | method | `tests/test_parsers.py:346` | `def test_extracts_function_with_parentheses(self)` |
| `test_extracts_import` | method | `tests/test_parsers.py:295` | `def test_extracts_import(self)` |
| `test_extracts_import` | method | `tests/test_parsers.py:405` | `def test_extracts_import(self)` |
| `test_extracts_import` | method | `tests/test_parsers.py:448` | `def test_extracts_import(self)` |
| `test_extracts_import_and_require` | method | `tests/test_parsers.py:263` | `def test_extracts_import_and_require(self)` |
| `test_extracts_import_block` | method | `tests/test_parsers.py:175` | `def test_extracts_import_block(self)` |
| `test_extracts_imports` | method | `tests/test_parsers.py:106` | `def test_extracts_imports(self)` |
| `test_extracts_include` | method | `tests/test_parsers.py:40` | `def test_extracts_include(self)` |
| `test_extracts_includes` | method | `tests/test_parsers.py:475` | `def test_extracts_includes(self)` |
| `test_extracts_label` | method | `tests/test_parsers.py:460` | `def test_extracts_label(self)` |
| `test_extracts_method` | method | `tests/test_parsers.py:288` | `def test_extracts_method(self)` |
| `test_extracts_method` | method | `tests/test_parsers.py:320` | `def test_extracts_method(self)` |
| `test_extracts_method_receiver` | method | `tests/test_parsers.py:168` | `def test_extracts_method_receiver(self)` |
| `test_extracts_multiple_labels` | method | `tests/test_parsers.py:467` | `def test_extracts_multiple_labels(self)` |
| `test_extracts_proc` | method | `tests/test_parsers.py:434` | `def test_extracts_proc(self)` |
| `test_extracts_pub_function` | method | `tests/test_parsers.py:211` | `def test_extracts_pub_function(self)` |
| `test_extracts_signature_with_params` | method | `tests/test_parsers.py:139` | `def test_extracts_signature_with_params(self)` |
| `test_extracts_single_import` | method | `tests/test_parsers.py:182` | `def test_extracts_single_import(self)` |
| `test_extracts_struct` | method | `tests/test_parsers.py:33` | `def test_extracts_struct(self)` |
| `test_extracts_struct_and_interface` | method | `tests/test_parsers.py:188` | `def test_extracts_struct_and_interface(self)` |
| `test_extracts_struct_and_trait_and_enum` | method | `tests/test_parsers.py:218` | `def test_extracts_struct_and_trait_and_enum(self)` |
| `test_extracts_type` | method | `tests/test_parsers.py:441` | `def test_extracts_type(self)` |
| `test_extracts_use` | method | `tests/test_parsers.py:231` | `def test_extracts_use(self)` |
| `test_extracts_use_and_require` | method | `tests/test_parsers.py:379` | `def test_extracts_use_and_require(self)` |
| `test_extracts_using` | method | `tests/test_parsers.py:327` | `def test_extracts_using(self)` |
| `test_function_line_points_at_definition` | method | `tests/test_parsers.py:64` | `def test_function_line_points_at_definition(self)` |
| `test_handles_syntax_error_gracefully` | method | `tests/test_parsers.py:121` | `def test_handles_syntax_error_gracefully(self)` |
| `test_record_and_interface` | method | `tests/test_parsers.py:333` | `def test_record_and_interface(self)` |
| `test_returns_c_parser_for_c_extensions` | method | `tests/test_parsers.py:487` | `def test_returns_c_parser_for_c_extensions(self)` |
| `test_returns_none_for_unknown_extension` | method | `tests/test_parsers.py:498` | `def test_returns_none_for_unknown_extension(self)` |
| `test_returns_python_parser_for_py` | method | `tests/test_parsers.py:493` | `def test_returns_python_parser_for_py(self)` |
| `test_returns_rust_parser_for_rs` | method | `tests/test_parsers.py:502` | `def test_returns_rust_parser_for_rs(self)` |
| `test_skips_reserved_words` | method | `tests/test_parsers.py:54` | `def test_skips_reserved_words(self)` |
| `test_skips_reserved_words` | method | `tests/test_parsers.py:270` | `def test_skips_reserved_words(self)` |
| `test_suppresses_syntax_warnings` | method | `tests/test_parsers.py:127` | `def test_suppresses_syntax_warnings(self)` |
| `TestElixirParserContract` | class | `tests/test_parsers_new.py:117` | `class TestElixirParserContract(TestCase)` |
| `TestKotlinParserContract` | class | `tests/test_parsers_new.py:68` | `class TestKotlinParserContract(TestCase)` |
| `TestLuaParserContract` | class | `tests/test_parsers_new.py:102` | `class TestLuaParserContract(TestCase)` |
| `TestNewParserFactoryContract` | class | `tests/test_parsers_new.py:134` | `class TestNewParserFactoryContract(TestCase)` |
| `TestPythonCallExtractionContract` | class | `tests/test_parsers_new.py:151` | `class TestPythonCallExtractionContract(TestCase)` |
| `TestRubyParserContract` | class | `tests/test_parsers_new.py:15` | `class TestRubyParserContract(TestCase)` |
| `TestScalaParserContract` | class | `tests/test_parsers_new.py:85` | `class TestScalaParserContract(TestCase)` |
| `TestSwiftParserContract` | class | `tests/test_parsers_new.py:45` | `class TestSwiftParserContract(TestCase)` |
| `setUp` | method | `tests/test_parsers_new.py:16` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:46` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:69` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:86` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:103` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:118` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:135` | `def setUp(self)` |
| `setUp` | method | `tests/test_parsers_new.py:152` | `def setUp(self)` |
| `test_extracts_class` | method | `tests/test_parsers_new.py:49` | `def test_extracts_class(self)` |
| `test_extracts_class` | method | `tests/test_parsers_new.py:72` | `def test_extracts_class(self)` |
| `test_extracts_class_inheritance` | method | `tests/test_parsers_new.py:155` | `def test_extracts_class_inheritance(self)` |
| `test_extracts_class_with_inheritance` | method | `tests/test_parsers_new.py:19` | `def test_extracts_class_with_inheritance(self)` |
| `test_extracts_def` | method | `tests/test_parsers_new.py:95` | `def test_extracts_def(self)` |
| `test_extracts_defmodule` | method | `tests/test_parsers_new.py:121` | `def test_extracts_defmodule(self)` |
| `test_extracts_fun` | method | `tests/test_parsers_new.py:78` | `def test_extracts_fun(self)` |
| `test_extracts_function` | method | `tests/test_parsers_new.py:55` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers_new.py:106` | `def test_extracts_function(self)` |
| `test_extracts_function` | method | `tests/test_parsers_new.py:127` | `def test_extracts_function(self)` |
| `test_extracts_function_calls` | method | `tests/test_parsers_new.py:160` | `def test_extracts_function_calls(self)` |
| `test_extracts_method` | method | `tests/test_parsers_new.py:33` | `def test_extracts_method(self)` |
| `test_extracts_module` | method | `tests/test_parsers_new.py:27` | `def test_extracts_module(self)` |
| `test_extracts_object` | method | `tests/test_parsers_new.py:89` | `def test_extracts_object(self)` |
| `test_extracts_protocol` | method | `tests/test_parsers_new.py:61` | `def test_extracts_protocol(self)` |
| `test_extracts_require` | method | `tests/test_parsers_new.py:39` | `def test_extracts_require(self)` |
| `test_extracts_require` | method | `tests/test_parsers_new.py:111` | `def test_extracts_require(self)` |
| `test_kotlin_extension_maps_correctly` | method | `tests/test_parsers_new.py:146` | `def test_kotlin_extension_maps_correctly(self)` |
| `test_ruby_extension_maps_correctly` | method | `tests/test_parsers_new.py:138` | `def test_ruby_extension_maps_correctly(self)` |
| `test_swift_extension_maps_correctly` | method | `tests/test_parsers_new.py:142` | `def test_swift_extension_maps_correctly(self)` |
| `TestParserHypothesisContract` | class | `tests/test_parsers_property.py:155` | `class TestParserHypothesisContract(TestCase)` |
| `TestPythonParserProperty` | class | `tests/test_parsers_property.py:288` | `class TestPythonParserProperty(TestCase)` |
| `_StrategyPlaceholder` | class | `tests/test_parsers_property.py:45` | `class _StrategyPlaceholder` |
| `_UnavailableStrategies` | class | `tests/test_parsers_property.py:60` | `class _UnavailableStrategies` |
| `__getattr__` | method | `tests/test_parsers_property.py:63` | `def __getattr__(self, name)` |
| `__or__` | method | `tests/test_parsers_property.py:48` | `def __or__(self, other)` |
| `__ror__` | method | `tests/test_parsers_property.py:52` | `def __ror__(self, other)` |
| `_assert_valid_symbols` | method | `tests/test_parsers_property.py:275` | `def _assert_valid_symbols(self, symbols)` |
| `_create_parser` | function | `tests/test_parsers_property.py:142` | `def _create_parser(ext)` |
| `_generate_multiline_code` | function | `tests/test_parsers_property.py:105` | `def _generate_multiline_code(lines, line_strategy)` |
| `builder` | method | `tests/test_parsers_property.py:65` | `def builder()` |
| `given` | method | `tests/test_parsers_property.py:69` | `def given()` |
| `map` | method | `tests/test_parsers_property.py:56` | `def map(self)` |
| `setUp` | method | `tests/test_parsers_property.py:291` | `def setUp(self)` |
| `settings` | method | `tests/test_parsers_property.py:75` | `def settings()` |
| `test_empty_code_returns_empty_or_valid` | method | `tests/test_parsers_property.py:198` | `def test_empty_code_returns_empty_or_valid(self, ext)` |
| `test_never_crashes_on_malformed_code` | method | `tests/test_parsers_property.py:162` | `def test_never_crashes_on_malformed_code(self, ext, code)` |
| `test_never_crashes_on_many_lines` | method | `tests/test_parsers_property.py:220` | `def test_never_crashes_on_many_lines(self, ext, lines)` |
| `test_never_crashes_on_unicode_code` | method | `tests/test_parsers_property.py:180` | `def test_never_crashes_on_unicode_code(self, ext, code)` |
| `test_parser_imports_is_list_of_strings` | method | `tests/test_parsers_property.py:257` | `def test_parser_imports_is_list_of_strings(self, ext)` |
| `test_python_never_crashes_on_any_text` | method | `tests/test_parsers_property.py:310` | `def test_python_never_crashes_on_any_text(self, code)` |
| `test_python_never_crashes_on_weird_ascii` | method | `tests/test_parsers_property.py:296` | `def test_python_never_crashes_on_weird_ascii(self, code)` |
| `test_repeated_keywords_no_crash` | method | `tests/test_parsers_property.py:238` | `def test_repeated_keywords_no_crash(self, ext)` |
| `test_unknown_extension_returns_none` | method | `tests/test_parsers_property.py:269` | `def test_unknown_extension_returns_none(self)` |
| `test_whitespace_code_returns_empty_or_valid` | method | `tests/test_parsers_property.py:208` | `def test_whitespace_code_returns_empty_or_valid(self, ext)` |
| `wrapper` | method | `tests/test_parsers_property.py:71` | `def wrapper(fn)` |
| `wrapper` | method | `tests/test_parsers_property.py:77` | `def wrapper(fn)` |
| `TestQueryEngineContract` | class | `tests/test_query.py:22` | `class TestQueryEngineContract(TestCase)` |
| `_make_node` | function | `tests/test_query.py:7` | `def _make_node(node_id, symbols)` |
| `_make_sym` | function | `tests/test_query.py:18` | `def _make_sym(name, kind, line)` |
| `setUp` | method | `tests/test_query.py:23` | `def setUp(self)` |
| `test_explain_returns_details` | method | `tests/test_query.py:51` | `def test_explain_returns_details(self)` |
| `test_explain_shows_imports` | method | `tests/test_query.py:58` | `def test_explain_shows_imports(self)` |
| `test_explain_shows_siblings` | method | `tests/test_query.py:63` | `def test_explain_shows_siblings(self)` |
| `test_explain_unknown_returns_none` | method | `tests/test_query.py:69` | `def test_explain_unknown_returns_none(self)` |
| `test_find_exact_symbol` | method | `tests/test_query.py:36` | `def test_find_exact_symbol(self)` |
| `test_find_path_direct_import` | method | `tests/test_query.py:73` | `def test_find_path_direct_import(self)` |
| `test_find_path_same_file` | method | `tests/test_query.py:79` | `def test_find_path_same_file(self)` |
| `test_find_path_unknown_returns_none` | method | `tests/test_query.py:84` | `def test_find_path_unknown_returns_none(self)` |
| `test_find_symbol_fuzzy` | method | `tests/test_query.py:42` | `def test_find_symbol_fuzzy(self)` |
| `test_find_symbol_not_found` | method | `tests/test_query.py:47` | `def test_find_symbol_not_found(self)` |
| `test_query_returns_file_matches` | method | `tests/test_query.py:102` | `def test_query_returns_file_matches(self)` |
| `test_query_returns_matching_symbols` | method | `tests/test_query.py:98` | `def test_query_returns_matching_symbols(self)` |
| `test_summary_shows_counts` | method | `tests/test_query.py:88` | `def test_summary_shows_counts(self)` |
| `test_summary_shows_top_modules` | method | `tests/test_query.py:94` | `def test_summary_shows_top_modules(self)` |
| `TestCategory` | class | `tests/test_ranking.py:104` | `class TestCategory` |
| `TestCompositeRanker` | class | `tests/test_ranking.py:403` | `class TestCompositeRanker` |
| `TestEdgeKind` | class | `tests/test_ranking.py:60` | `class TestEdgeKind` |
| `TestExplain` | class | `tests/test_ranking.py:539` | `class TestExplain` |
| `TestGlobalPageRank` | class | `tests/test_ranking.py:247` | `class TestGlobalPageRank` |
| `TestHITS` | class | `tests/test_ranking.py:325` | `class TestHITS` |
| `TestIntegration` | class | `tests/test_ranking.py:587` | `class TestIntegration` |
| `TestMorphism` | class | `tests/test_ranking.py:84` | `class TestMorphism` |
| `TestPersonalizedPageRank` | class | `tests/test_ranking.py:288` | `class TestPersonalizedPageRank` |
| `TestProjections` | class | `tests/test_ranking.py:490` | `class TestProjections` |
| `TestSeedGeneration` | class | `tests/test_ranking.py:350` | `class TestSeedGeneration` |
| `TestTypedGraph` | class | `tests/test_ranking.py:183` | `class TestTypedGraph` |
| `_make_test_graph` | method | `tests/test_ranking.py:238` | `def _make_test_graph()` |
| `test_add_object_and_morphism` | method | `tests/test_ranking.py:110` | `def test_add_object_and_morphism(self)` |
| `test_all_edge_kinds_have_weights` | method | `tests/test_ranking.py:61` | `def test_all_edge_kinds_have_weights(self)` |
| `test_all_nodes_have_positive_score` | method | `tests/test_ranking.py:254` | `def test_all_nodes_have_positive_score(self)` |
| `test_apply_view_architecture` | method | `tests/test_ranking.py:512` | `def test_apply_view_architecture(self)` |
| `test_apply_view_empty` | method | `tests/test_ranking.py:528` | `def test_apply_view_empty(self)` |
| `test_apply_view_reverse` | method | `tests/test_ranking.py:521` | `def test_apply_view_reverse(self)` |
| `test_authorities_and_hubs_have_positive_scores` | method | `tests/test_ranking.py:326` | `def test_authorities_and_hubs_have_positive_scores(self)` |
| `test_authorities_l2_normalized` | method | `tests/test_ranking.py:333` | `def test_authorities_l2_normalized(self)` |
| `test_build_category_from_edges` | method | `tests/test_ranking.py:214` | `def test_build_category_from_edges(self)` |
| `test_build_category_from_edges_filters_by_node_ids` | method | `tests/test_ranking.py:225` | `def test_build_category_from_edges_filters_by_node_ids(self)` |
| `test_build_seeds_for_context` | method | `tests/test_ranking.py:383` | `def test_build_seeds_for_context(self)` |
| `test_build_seeds_for_context_no_match` | method | `tests/test_ranking.py:392` | `def test_build_seeds_for_context_no_match(self)` |
| `test_build_seeds_from_query_matches_node_id` | method | `tests/test_ranking.py:351` | `def test_build_seeds_from_query_matches_node_id(self)` |
| `test_build_seeds_from_query_matches_symbol` | method | `tests/test_ranking.py:363` | `def test_build_seeds_from_query_matches_symbol(self)` |
| `test_build_seeds_from_query_no_match_returns_empty` | method | `tests/test_ranking.py:374` | `def test_build_seeds_from_query_no_match_returns_empty(self)` |
| `test_category_from_real_edges` | method | `tests/test_ranking.py:588` | `def test_category_from_real_edges(self)` |
| `test_compose_imports_then_defines` | method | `tests/test_ranking.py:140` | `def test_compose_imports_then_defines(self)` |
| `test_compose_incompatible_returns_none` | method | `tests/test_ranking.py:148` | `def test_compose_incompatible_returns_none(self)` |
| `test_compose_mismatched_target_source` | method | `tests/test_ranking.py:155` | `def test_compose_mismatched_target_source(self)` |
| `test_compose_same_kind` | method | `tests/test_ranking.py:130` | `def test_compose_same_kind(self)` |
| `test_converges_within_max_iter` | method | `tests/test_ranking.py:260` | `def test_converges_within_max_iter(self)` |
| `test_dangling_node_handled` | method | `tests/test_ranking.py:273` | `def test_dangling_node_handled(self)` |
| `test_different_seeds_produce_different_rankings` | method | `tests/test_ranking.py:303` | `def test_different_seeds_produce_different_rankings(self)` |
| `test_doc_projection_filters_morphism_kind` | method | `tests/test_ranking.py:506` | `def test_doc_projection_filters_morphism_kind(self)` |
| `test_doc_projection_filters_undocumented` | method | `tests/test_ranking.py:498` | `def test_doc_projection_filters_undocumented(self)` |
| `test_edge_kind_is_str_enum` | method | `tests/test_ranking.py:75` | `def test_edge_kind_is_str_enum(self)` |
| `test_empty_category` | method | `tests/test_ranking.py:105` | `def test_empty_category(self)` |
| `test_empty_graph` | method | `tests/test_ranking.py:184` | `def test_empty_graph(self)` |
| `test_empty_graph` | method | `tests/test_ranking.py:284` | `def test_empty_graph(self)` |
| `test_empty_seeds_uses_uniform` | method | `tests/test_ranking.py:310` | `def test_empty_seeds_uses_uniform(self)` |
| `test_explain_rank_found` | method | `tests/test_ranking.py:540` | `def test_explain_rank_found(self)` |
| `test_explain_rank_not_found` | method | `tests/test_ranking.py:559` | `def test_explain_rank_not_found(self)` |
| `test_explain_returns_none_for_missing` | method | `tests/test_ranking.py:479` | `def test_explain_returns_none_for_missing(self)` |
| `test_hubs_l2_normalized` | method | `tests/test_ranking.py:339` | `def test_hubs_l2_normalized(self)` |
| `test_identity_projection_passes_all` | method | `tests/test_ranking.py:491` | `def test_identity_projection_passes_all(self)` |
| `test_infer_edge_kind_falls_back` | method | `tests/test_ranking.py:71` | `def test_infer_edge_kind_falls_back(self)` |
| `test_infer_edge_kind_maps_correctly` | method | `tests/test_ranking.py:66` | `def test_infer_edge_kind_maps_correctly(self)` |
| `test_morphism_is_frozen` | method | `tests/test_ranking.py:94` | `def test_morphism_is_frozen(self)` |
| `test_multi_seed` | method | `tests/test_ranking.py:317` | `def test_multi_seed(self)` |
| `test_noise_penalty_applied` | method | `tests/test_ranking.py:447` | `def test_noise_penalty_applied(self)` |
| `test_outgoing_and_incoming` | method | `tests/test_ranking.py:118` | `def test_outgoing_and_incoming(self)` |
| `test_pagerank_on_real_category` | method | `tests/test_ranking.py:613` | `def test_pagerank_on_real_category(self)` |
| `test_paths_empty_when_no_route` | method | `tests/test_ranking.py:171` | `def test_paths_empty_when_no_route(self)` |
| `test_paths_finds_composition_chains` | method | `tests/test_ranking.py:162` | `def test_paths_finds_composition_chains(self)` |
| `test_ppr_favors_seed` | method | `tests/test_ranking.py:625` | `def test_ppr_favors_seed(self)` |
| `test_rank_items_have_all_score_fields` | method | `tests/test_ranking.py:421` | `def test_rank_items_have_all_score_fields(self)` |
| `test_rank_returns_sorted_results` | method | `tests/test_ranking.py:404` | `def test_rank_returns_sorted_results(self)` |
| `test_rank_summary_format` | method | `tests/test_ranking.py:565` | `def test_rank_summary_format(self)` |
| `test_ranker_from_real_data` | method | `tests/test_ranking.py:637` | `def test_ranker_from_real_data(self)` |
| `test_scores_sum_to_one` | method | `tests/test_ranking.py:248` | `def test_scores_sum_to_one(self)` |
| `test_scores_sum_to_one` | method | `tests/test_ranking.py:296` | `def test_scores_sum_to_one(self)` |
| `test_seed_node_gets_highest_score` | method | `tests/test_ranking.py:289` | `def test_seed_node_gets_highest_score(self)` |
| `test_stable_across_calls` | method | `tests/test_ranking.py:266` | `def test_stable_across_calls(self)` |
| `test_stochastic_row_empty_for_dangling` | method | `tests/test_ranking.py:199` | `def test_stochastic_row_empty_for_dangling(self)` |
| `test_stochastic_row_normalizes_to_one` | method | `tests/test_ranking.py:190` | `def test_stochastic_row_normalizes_to_one(self)` |
| `test_top_n` | method | `tests/test_ranking.py:466` | `def test_top_n(self)` |
| `test_transition_weight_aggregates_parallel_edges` | method | `tests/test_ranking.py:205` | `def test_transition_weight_aggregates_parallel_edges(self)` |
| `test_weight_default_confidence` | method | `tests/test_ranking.py:90` | `def test_weight_default_confidence(self)` |
| `test_weight_is_edge_weight_times_confidence` | method | `tests/test_ranking.py:85` | `def test_weight_is_edge_weight_times_confidence(self)` |
| `TestReadmeInjectorEdgeCases` | class | `tests/test_readme_injector.py:140` | `class TestReadmeInjectorEdgeCases(TestCase)` |
| `TestReadmeInjectorFindReadme` | class | `tests/test_readme_injector.py:105` | `class TestReadmeInjectorFindReadme(TestCase)` |
| `TestReadmeInjectorInjectBehavior` | class | `tests/test_readme_injector.py:16` | `class TestReadmeInjectorInjectBehavior(TestCase)` |
| `TestReadmeInjectorRemoveBehavior` | class | `tests/test_readme_injector.py:72` | `class TestReadmeInjectorRemoveBehavior(TestCase)` |
| `setUp` | method | `tests/test_readme_injector.py:19` | `def setUp(self)` |
| `setUp` | method | `tests/test_readme_injector.py:75` | `def setUp(self)` |
| `setUp` | method | `tests/test_readme_injector.py:108` | `def setUp(self)` |
| `setUp` | method | `tests/test_readme_injector.py:143` | `def setUp(self)` |
| `tearDown` | method | `tests/test_readme_injector.py:24` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_readme_injector.py:80` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_readme_injector.py:112` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_readme_injector.py:148` | `def tearDown(self)` |
| `test_custom_kb_filename_works` | method | `tests/test_readme_injector.py:160` | `def test_custom_kb_filename_works(self)` |
| `test_finds_readme_md` | method | `tests/test_readme_injector.py:116` | `def test_finds_readme_md(self)` |
| `test_finds_readme_rst` | method | `tests/test_readme_injector.py:122` | `def test_finds_readme_rst(self)` |
| `test_inject_into_empty_readme` | method | `tests/test_readme_injector.py:152` | `def test_inject_into_empty_readme(self)` |
| `test_inject_into_markdown_readme_adds_kb_link` | method | `tests/test_readme_injector.py:28` | `def test_inject_into_markdown_readme_adds_kb_link(self)` |
| `test_inject_into_rst_readme_adds_kb_link` | method | `tests/test_readme_injector.py:39` | `def test_inject_into_rst_readme_adds_kb_link(self)` |
| `test_inject_is_idempotent_does_not_duplicate` | method | `tests/test_readme_injector.py:48` | `def test_inject_is_idempotent_does_not_duplicate(self)` |
| `test_inject_no_readme_file_returns_false` | method | `tests/test_readme_injector.py:59` | `def test_inject_no_readme_file_returns_false(self)` |
| `test_inject_preserves_existing_content` | method | `tests/test_readme_injector.py:63` | `def test_inject_preserves_existing_content(self)` |
| `test_prefers_readme_md_over_rst` | method | `tests/test_readme_injector.py:128` | `def test_prefers_readme_md_over_rst(self)` |
| `test_remove_no_readme_returns_false` | method | `tests/test_readme_injector.py:100` | `def test_remove_no_readme_returns_false(self)` |
| `test_remove_strips_injected_section` | method | `tests/test_readme_injector.py:84` | `def test_remove_strips_injected_section(self)` |
| `test_remove_without_injection_returns_false` | method | `tests/test_readme_injector.py:94` | `def test_remove_without_injection_returns_false(self)` |
| `test_returns_none_when_no_readme` | method | `tests/test_readme_injector.py:135` | `def test_returns_none_when_no_readme(self)` |
| `TestMonolithRefactorizerContract` | class | `tests/test_refactorizer.py:18` | `class TestMonolithRefactorizerContract(TestCase)` |
| `_make_edge` | method | `tests/test_refactorizer.py:37` | `def _make_edge(self, src, tgt)` |
| `_make_node` | method | `tests/test_refactorizer.py:28` | `def _make_node(self, nid, symbols)` |
| `_make_symbol` | method | `tests/test_refactorizer.py:25` | `def _make_symbol(self, name, kind, line)` |
| `setUp` | method | `tests/test_refactorizer.py:21` | `def setUp(self)` |
| `test_analyze_detects_large_file` | method | `tests/test_refactorizer.py:50` | `def test_analyze_detects_large_file(self)` |
| `test_analyze_empty_graph_returns_empty` | method | `tests/test_refactorizer.py:40` | `def test_analyze_empty_graph_returns_empty(self)` |
| `test_analyze_estimates_impact_from_resolved_edges` | method | `tests/test_refactorizer.py:97` | `def test_analyze_estimates_impact_from_resolved_edges(self)` |
| `test_analyze_generates_extract_class_for_multiple_classes` | method | `tests/test_refactorizer.py:59` | `def test_analyze_generates_extract_class_for_multiple_classes(self)` |
| `test_analyze_generates_extract_function_for_multiple_functions` | method | `tests/test_refactorizer.py:74` | `def test_analyze_generates_extract_function_for_multiple_functions(self)` |
| `test_analyze_ignores_small_files` | method | `tests/test_refactorizer.py:44` | `def test_analyze_ignores_small_files(self)` |
| `test_analyze_respects_max_files_limit` | method | `tests/test_refactorizer.py:173` | `def test_analyze_respects_max_files_limit(self)` |
| `test_analyze_sorted_by_line_count` | method | `tests/test_refactorizer.py:160` | `def test_analyze_sorted_by_line_count(self)` |
| `test_analyze_splits_file_with_many_symbols` | method | `tests/test_refactorizer.py:89` | `def test_analyze_splits_file_with_many_symbols(self)` |
| `test_generate_script_contains_sed_commands` | method | `tests/test_refactorizer.py:140` | `def test_generate_script_contains_sed_commands(self)` |
| `test_generate_script_contains_set_e` | method | `tests/test_refactorizer.py:129` | `def test_generate_script_contains_set_e(self)` |
| `test_generate_script_contains_shebang` | method | `tests/test_refactorizer.py:109` | `def test_generate_script_contains_shebang(self)` |
| `TestImportResolverContract` | class | `tests/test_resolver.py:15` | `class TestImportResolverContract(TestCase)` |
| `test_resolves_c_extensionless_header` | method | `tests/test_resolver.py:100` | `def test_resolves_c_extensionless_header(self)` |
| `test_resolves_c_header_stem_across_dirs` | method | `tests/test_resolver.py:121` | `def test_resolves_c_header_stem_across_dirs(self)` |
| `test_resolves_c_quoted_header_same_dir` | method | `tests/test_resolver.py:86` | `def test_resolves_c_quoted_header_same_dir(self)` |
| `test_resolves_c_quoted_header_subdir` | method | `tests/test_resolver.py:93` | `def test_resolves_c_quoted_header_subdir(self)` |
| `test_resolves_c_source_from_header_dir` | method | `tests/test_resolver.py:107` | `def test_resolves_c_source_from_header_dir(self)` |
| `test_resolves_cpp_header_same_dir` | method | `tests/test_resolver.py:114` | `def test_resolves_cpp_header_same_dir(self)` |
| `test_resolves_extensionless_python_import` | method | `tests/test_resolver.py:32` | `def test_resolves_extensionless_python_import(self)` |
| `test_resolves_go_import` | method | `tests/test_resolver.py:72` | `def test_resolves_go_import(self)` |
| `test_resolves_include_dir_suffix_match` | method | `tests/test_resolver.py:149` | `def test_resolves_include_dir_suffix_match(self)` |
| `test_resolves_package_init` | method | `tests/test_resolver.py:39` | `def test_resolves_package_init(self)` |
| `test_resolves_parent_dir_include` | method | `tests/test_resolver.py:135` | `def test_resolves_parent_dir_include(self)` |
| `test_resolves_parent_dir_include_despite_ambiguous_stem` | method | `tests/test_resolver.py:142` | `def test_resolves_parent_dir_include_despite_ambiguous_stem(self)` |
| `test_resolves_python_module_dotpath` | method | `tests/test_resolver.py:18` | `def test_resolves_python_module_dotpath(self)` |
| `test_resolves_relative_import` | method | `tests/test_resolver.py:25` | `def test_resolves_relative_import(self)` |
| `test_resolves_same_directory_import` | method | `tests/test_resolver.py:79` | `def test_resolves_same_directory_import(self)` |
| `test_resolves_stem_match_when_unique` | method | `tests/test_resolver.py:60` | `def test_resolves_stem_match_when_unique(self)` |
| `test_returns_none_for_ambiguous_suffix_match` | method | `tests/test_resolver.py:156` | `def test_returns_none_for_ambiguous_suffix_match(self)` |
| `test_returns_none_for_c_system_header` | method | `tests/test_resolver.py:128` | `def test_returns_none_for_c_system_header(self)` |
| `test_returns_none_for_empty_import` | method | `tests/test_resolver.py:67` | `def test_returns_none_for_empty_import(self)` |
| `test_returns_none_for_external_stdlib` | method | `tests/test_resolver.py:46` | `def test_returns_none_for_external_stdlib(self)` |
| `test_returns_none_for_unknown_import` | method | `tests/test_resolver.py:53` | `def test_returns_none_for_unknown_import(self)` |
| `TestRuleGeneratorContract` | class | `tests/test_rule_gen.py:12` | `class TestRuleGeneratorContract(TestCase)` |
| `_make_node` | method | `tests/test_rule_gen.py:19` | `def _make_node(self, nid, label, lang)` |
| `_make_node_with_symbols` | method | `tests/test_rule_gen.py:29` | `def _make_node_with_symbols(self, nid, sym_count)` |
| `setUp` | method | `tests/test_rule_gen.py:15` | `def setUp(self)` |
| `test_antipattern_threshold_from_config` | method | `tests/test_rule_gen.py:67` | `def test_antipattern_threshold_from_config(self)` |
| `test_detects_antipatterns_with_content` | method | `tests/test_rule_gen.py:56` | `def test_detects_antipatterns_with_content(self)` |
| `test_empty_nodes_returns_empty_rules` | method | `tests/test_rule_gen.py:44` | `def test_empty_nodes_returns_empty_rules(self)` |
| `test_generates_rules_for_function_heavy_language` | method | `tests/test_rule_gen.py:48` | `def test_generates_rules_for_function_heavy_language(self)` |
| `test_rule_id_increments` | method | `tests/test_rule_gen.py:90` | `def test_rule_id_increments(self)` |
| `test_write_rules_creates_files` | method | `tests/test_rule_gen.py:77` | `def test_write_rules_creates_files(self)` |
| `TestSarifExporterContract` | class | `tests/test_sarif.py:11` | `class TestSarifExporterContract(TestCase)` |
| `_make_finding` | method | `tests/test_sarif.py:18` | `def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)` |
| `setUp` | method | `tests/test_sarif.py:14` | `def setUp(self)` |
| `test_empty_findings_produces_valid_sarif` | method | `tests/test_sarif.py:97` | `def test_empty_findings_produces_valid_sarif(self)` |
| `test_export_includes_result` | method | `tests/test_sarif.py:62` | `def test_export_includes_result(self)` |
| `test_export_includes_rule` | method | `tests/test_sarif.py:54` | `def test_export_includes_rule(self)` |
| `test_export_includes_tool_info` | method | `tests/test_sarif.py:46` | `def test_export_includes_tool_info(self)` |
| `test_export_returns_valid_json` | method | `tests/test_sarif.py:38` | `def test_export_returns_valid_json(self)` |
| `test_privacy_mode_strips_snippets` | method | `tests/test_sarif.py:88` | `def test_privacy_mode_strips_snippets(self)` |
| `test_severity_maps_correctly` | method | `tests/test_sarif.py:73` | `def test_severity_maps_correctly(self)` |
| `TestScannerContract` | class | `tests/test_scanner.py:11` | `class TestScannerContract(TestCase)` |
| `_write` | method | `tests/test_scanner.py:20` | `def _write(self, path, content)` |
| `setUp` | method | `tests/test_scanner.py:12` | `def setUp(self)` |
| `tearDown` | method | `tests/test_scanner.py:16` | `def tearDown(self)` |
| `test_coding_cookie_ignored_as_file_doc` | method | `tests/test_scanner.py:129` | `def test_coding_cookie_ignored_as_file_doc(self)` |
| `test_gitignore_disabled_by_default` | method | `tests/test_scanner.py:162` | `def test_gitignore_disabled_by_default(self)` |
| `test_gitignore_glob_conversion` | method | `tests/test_scanner.py:171` | `def test_gitignore_glob_conversion(self)` |
| `test_gitignore_respected_when_enabled` | method | `tests/test_scanner.py:151` | `def test_gitignore_respected_when_enabled(self)` |
| `test_ignores_env_and_vendor_dirs` | method | `tests/test_scanner.py:32` | `def test_ignores_env_and_vendor_dirs(self)` |
| `test_import_edges_are_created` | method | `tests/test_scanner.py:94` | `def test_import_edges_are_created(self)` |
| `test_module_docstring_extracted_as_file_doc` | method | `tests/test_scanner.py:114` | `def test_module_docstring_extracted_as_file_doc(self)` |
| `test_multiline_module_docstring_extracted` | method | `tests/test_scanner.py:121` | `def test_multiline_module_docstring_extracted(self)` |
| `test_preprocessor_guards_ignored_as_file_doc` | method | `tests/test_scanner.py:136` | `def test_preprocessor_guards_ignored_as_file_doc(self)` |
| `test_privacy_mode_strips_docs` | method | `tests/test_scanner.py:104` | `def test_privacy_mode_strips_docs(self)` |
| `test_raises_on_invalid_directory` | method | `tests/test_scanner.py:89` | `def test_raises_on_invalid_directory(self)` |
| `test_rejects_symlinks` | method | `tests/test_scanner.py:45` | `def test_rejects_symlinks(self)` |
| `test_respects_max_directory_depth` | method | `tests/test_scanner.py:79` | `def test_respects_max_directory_depth(self)` |
| `test_scan_with_content_returns_content_map` | method | `tests/test_scanner.py:143` | `def test_scan_with_content_returns_content_map(self)` |
| `test_scans_multiple_languages` | method | `tests/test_scanner.py:70` | `def test_scans_multiple_languages(self)` |
| `test_scans_python_files` | method | `tests/test_scanner.py:25` | `def test_scans_python_files(self)` |
| `test_skips_non_code_files` | method | `tests/test_scanner.py:59` | `def test_skips_non_code_files(self)` |
| `TestFixGuidance` | class | `tests/test_security.py:396` | `class TestFixGuidance(TestCase)` |
| `TestSecurityAnalyzerConfig` | class | `tests/test_security.py:43` | `class TestSecurityAnalyzerConfig(TestCase)` |
| `TestSecurityAnalyzerPathValidation` | class | `tests/test_security.py:327` | `class TestSecurityAnalyzerPathValidation(TestCase)` |
| `TestSecurityAnalyzerRules` | class | `tests/test_security.py:64` | `class TestSecurityAnalyzerRules(TestCase)` |
| `TestSecurityAnalyzerSummary` | class | `tests/test_security.py:374` | `class TestSecurityAnalyzerSummary(TestCase)` |
| `TestSecurityAnalyzerThreshold` | class | `tests/test_security.py:295` | `class TestSecurityAnalyzerThreshold(TestCase)` |
| `TestSecurityFinding` | class | `tests/test_security.py:21` | `class TestSecurityFinding(TestCase)` |
| `_finding` | method | `tests/test_security.py:399` | `def _finding(self, cwe)` |
| `_scan_content` | method | `tests/test_security.py:71` | `def _scan_content(self, content, extension)` |
| `setUp` | method | `tests/test_security.py:67` | `def setUp(self)` |
| `test_c_gets` | method | `tests/test_security.py:148` | `def test_c_gets(self)` |
| `test_c_strcpy` | method | `tests/test_security.py:143` | `def test_c_strcpy(self)` |
| `test_c_system` | method | `tests/test_security.py:153` | `def test_c_system(self)` |
| `test_csharp_binary_formatter` | method | `tests/test_security.py:274` | `def test_csharp_binary_formatter(self)` |
| `test_csharp_process_start` | method | `tests/test_security.py:203` | `def test_csharp_process_start(self)` |
| `test_dart_process_run` | method | `tests/test_security.py:228` | `def test_dart_process_run(self)` |
| `test_default_config_disables_security` | method | `tests/test_security.py:46` | `def test_default_config_disables_security(self)` |
| `test_default_security_output` | method | `tests/test_security.py:54` | `def test_default_security_output(self)` |
| `test_default_severity_threshold` | method | `tests/test_security.py:50` | `def test_default_severity_threshold(self)` |
| `test_elixir_code_eval` | method | `tests/test_security.py:238` | `def test_elixir_code_eval(self)` |
| `test_elixir_system_cmd` | method | `tests/test_security.py:243` | `def test_elixir_system_cmd(self)` |
| `test_empty_cwe_falls_back` | method | `tests/test_security.py:413` | `def test_empty_cwe_falls_back(self)` |
| `test_empty_directory` | method | `tests/test_security.py:357` | `def test_empty_directory(self)` |
| `test_gdscript_os_execute` | method | `tests/test_security.py:248` | `def test_gdscript_os_execute(self)` |
| `test_go_exec_command` | method | `tests/test_security.py:168` | `def test_go_exec_command(self)` |
| `test_go_unsafe_package` | method | `tests/test_security.py:289` | `def test_go_unsafe_package(self)` |
| `test_ignores_ignored_dirs` | method | `tests/test_security.py:345` | `def test_ignores_ignored_dirs(self)` |
| `test_ignores_symlinks` | method | `tests/test_security.py:330` | `def test_ignores_symlinks(self)` |
| `test_init_with_config` | method | `tests/test_security.py:58` | `def test_init_with_config(self)` |
| `test_java_runtime_exec` | method | `tests/test_security.py:158` | `def test_java_runtime_exec(self)` |
| `test_java_sql_injection` | method | `tests/test_security.py:163` | `def test_java_sql_injection(self)` |
| `test_javascript_child_process` | method | `tests/test_security.py:133` | `def test_javascript_child_process(self)` |
| `test_javascript_dangerously_set_inner_html` | method | `tests/test_security.py:138` | `def test_javascript_dangerously_set_inner_html(self)` |
| `test_javascript_eval` | method | `tests/test_security.py:128` | `def test_javascript_eval(self)` |
| `test_javascript_inner_html` | method | `tests/test_security.py:123` | `def test_javascript_inner_html(self)` |
| `test_known_cwe_returns_actionable_hint` | method | `tests/test_security.py:402` | `def test_known_cwe_returns_actionable_hint(self)` |
| `test_kotlin_runtime_exec` | method | `tests/test_security.py:208` | `def test_kotlin_runtime_exec(self)` |
| `test_lua_load` | method | `tests/test_security.py:218` | `def test_lua_load(self)` |
| `test_lua_os_execute` | method | `tests/test_security.py:223` | `def test_lua_os_execute(self)` |
| `test_nim_exec_process` | method | `tests/test_security.py:258` | `def test_nim_exec_process(self)` |
| `test_php_eval` | method | `tests/test_security.py:183` | `def test_php_eval(self)` |
| `test_php_sql_injection` | method | `tests/test_security.py:188` | `def test_php_sql_injection(self)` |
| `test_php_unseralize` | method | `tests/test_security.py:193` | `def test_php_unseralize(self)` |
| `test_php_xss` | method | `tests/test_security.py:284` | `def test_php_xss(self)` |
| `test_python_eval` | method | `tests/test_security.py:83` | `def test_python_eval(self)` |
| `test_python_flask_debug` | method | `tests/test_security.py:113` | `def test_python_flask_debug(self)` |
| `test_python_hardcoded_secret` | method | `tests/test_security.py:98` | `def test_python_hardcoded_secret(self)` |
| `test_python_os_system` | method | `tests/test_security.py:78` | `def test_python_os_system(self)` |
| `test_python_pickle` | method | `tests/test_security.py:88` | `def test_python_pickle(self)` |
| `test_python_request_verify_false` | method | `tests/test_security.py:108` | `def test_python_request_verify_false(self)` |
| `test_python_sql_injection` | method | `tests/test_security.py:93` | `def test_python_sql_injection(self)` |
| `test_python_weak_crypto` | method | `tests/test_security.py:103` | `def test_python_weak_crypto(self)` |
| `test_python_yaml_load` | method | `tests/test_security.py:118` | `def test_python_yaml_load(self)` |
| `test_ruby_backtick` | method | `tests/test_security.py:279` | `def test_ruby_backtick(self)` |
| `test_ruby_eval` | method | `tests/test_security.py:173` | `def test_ruby_eval(self)` |
| `test_ruby_marshal_load` | method | `tests/test_security.py:178` | `def test_ruby_marshal_load(self)` |
| `test_rust_unsafe` | method | `tests/test_security.py:233` | `def test_rust_unsafe(self)` |
| `test_safe_code_produces_no_findings` | method | `tests/test_security.py:263` | `def test_safe_code_produces_no_findings(self)` |
| `test_scala_runtime_exec` | method | `tests/test_security.py:253` | `def test_scala_runtime_exec(self)` |
| `test_security_finding_fields` | method | `tests/test_security.py:24` | `def test_security_finding_fields(self)` |
| `test_shell_eval` | method | `tests/test_security.py:198` | `def test_shell_eval(self)` |
| `test_summary_empty` | method | `tests/test_security.py:377` | `def test_summary_empty(self)` |
| `test_summary_with_findings` | method | `tests/test_security.py:383` | `def test_summary_with_findings(self)` |
| `test_swift_process` | method | `tests/test_security.py:213` | `def test_swift_process(self)` |
| `test_threshold_filters_low` | method | `tests/test_security.py:298` | `def test_threshold_filters_low(self)` |
| `test_threshold_info_shows_all` | method | `tests/test_security.py:312` | `def test_threshold_info_shows_all(self)` |
| `test_unknown_cwe_falls_back` | method | `tests/test_security.py:408` | `def test_unknown_cwe_falls_back(self)` |
| `test_unsupported_extension` | method | `tests/test_security.py:364` | `def test_unsupported_extension(self)` |
| `TestTaintAnalyzerContract` | class | `tests/test_taint.py:10` | `class TestTaintAnalyzerContract(TestCase)` |
| `_make_node` | method | `tests/test_taint.py:17` | `def _make_node(self, nid, label)` |
| `setUp` | method | `tests/test_taint.py:13` | `def setUp(self)` |
| `test_dangerous_import_by_language` | method | `tests/test_taint.py:62` | `def test_dangerous_import_by_language(self)` |
| `test_direct_dangerous_import_found` | method | `tests/test_taint.py:31` | `def test_direct_dangerous_import_found(self)` |
| `test_empty_graph_returns_empty_result` | method | `tests/test_taint.py:20` | `def test_empty_graph_returns_empty_result(self)` |
| `test_max_depth_limits_propagation` | method | `tests/test_taint.py:77` | `def test_max_depth_limits_propagation(self)` |
| `test_no_dangerous_imports_returns_empty` | method | `tests/test_taint.py:25` | `def test_no_dangerous_imports_returns_empty(self)` |
| `test_taint_path_has_severity` | method | `tests/test_taint.py:70` | `def test_taint_path_has_severity(self)` |
| `test_taint_propagates_through_resolved_edges` | method | `tests/test_taint.py:38` | `def test_taint_propagates_through_resolved_edges(self)` |
| `_bkg` | function | `tests/test_taint_bdd.py:112` | `def _bkg()` |
| `_build_project_files` | function | `tests/test_taint_bdd.py:29` | `def _build_project_files(project, root)` |
| `_chain_given` | function | `tests/test_taint_bdd.py:144` | `def _chain_given()` |
| `_chain_given2` | function | `tests/test_taint_bdd.py:163` | `def _chain_given2()` |
| `_chain_when` | function | `tests/test_taint_bdd.py:148` | `def _chain_when(_taint_result)` |
| `_check_direct_path` | function | `tests/test_taint_bdd.py:130` | `def _check_direct_path(_taint_result)` |
| `_check_has_path` | function | `tests/test_taint_bdd.py:125` | `def _check_has_path(_taint_result)` |
| `_check_js_dangerous` | function | `tests/test_taint_bdd.py:186` | `def _check_js_dangerous(_taint_result)` |
| `_check_js_source` | function | `tests/test_taint_bdd.py:192` | `def _check_js_source(_taint_result)` |
| `_check_long_path` | function | `tests/test_taint_bdd.py:152` | `def _check_long_path(_taint_result)` |
| `_check_shallow` | function | `tests/test_taint_bdd.py:171` | `def _check_shallow(_taint_result)` |
| `_check_sink` | function | `tests/test_taint_bdd.py:139` | `def _check_sink(_taint_result)` |
| `_check_src` | function | `tests/test_taint_bdd.py:135` | `def _check_src(_taint_result)` |
| `_direct_given` | function | `tests/test_taint_bdd.py:117` | `def _direct_given()` |
| `_direct_when` | function | `tests/test_taint_bdd.py:121` | `def _direct_when(_taint_result)` |
| `_js_given` | function | `tests/test_taint_bdd.py:178` | `def _js_given()` |
| `_js_when` | function | `tests/test_taint_bdd.py:182` | `def _js_when(_taint_result)` |
| `_run_shallow` | function | `tests/test_taint_bdd.py:167` | `def _run_shallow(_shallow_cfg)` |
| `_run_taint` | function | `tests/test_taint_bdd.py:54` | `def _run_taint(files, cfg)` |
| `_scan_project` | function | `tests/test_taint_bdd.py:36` | `def _scan_project(root, cfg)` |
| `_shallow_cfg` | function | `tests/test_taint_bdd.py:159` | `def _shallow_cfg()` |
| `test_bdd_skipped` | function | `tests/test_taint_bdd.py:87` | `def test_bdd_skipped()` |
| `test_cross_language_taint` | function | `tests/test_taint_bdd.py:83` | `def test_cross_language_taint()` |
| `test_direct_dangerous_import` | function | `tests/test_taint_bdd.py:71` | `def test_direct_dangerous_import()` |
| `test_taint_max_depth` | function | `tests/test_taint_bdd.py:79` | `def test_taint_max_depth()` |
| `test_taint_propagates_chain` | function | `tests/test_taint_bdd.py:75` | `def test_taint_propagates_chain()` |
| `TestUmlCodeGenerationCSharp` | class | `tests/test_uml.py:281` | `class TestUmlCodeGenerationCSharp(TestCase)` |
| `TestUmlCodeGenerationCpp` | class | `tests/test_uml.py:181` | `class TestUmlCodeGenerationCpp(TestCase)` |
| `TestUmlCodeGenerationGo` | class | `tests/test_uml.py:306` | `class TestUmlCodeGenerationGo(TestCase)` |
| `TestUmlCodeGenerationJava` | class | `tests/test_uml.py:239` | `class TestUmlCodeGenerationJava(TestCase)` |
| `TestUmlCodeGenerationKotlinScalaSwiftDartRuby` | class | `tests/test_uml.py:427` | `class TestUmlCodeGenerationKotlinScalaSwiftDartRuby(TestCase)` |
| `TestUmlCodeGenerationPhp` | class | `tests/test_uml.py:387` | `class TestUmlCodeGenerationPhp(TestCase)` |
| `TestUmlCodeGenerationRust` | class | `tests/test_uml.py:347` | `class TestUmlCodeGenerationRust(TestCase)` |
| `TestUmlMermaidDiagram` | class | `tests/test_uml.py:16` | `class TestUmlMermaidDiagram(TestCase)` |
| `TestUmlSanitizeId` | class | `tests/test_uml.py:157` | `class TestUmlSanitizeId(TestCase)` |
| `_make_class_node` | method | `tests/test_uml.py:434` | `def _make_class_node(self, name, lang, kind)` |
| `setUp` | method | `tests/test_uml.py:19` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:160` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:184` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:242` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:284` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:309` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:350` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:390` | `def setUp(self)` |
| `setUp` | method | `tests/test_uml.py:430` | `def setUp(self)` |
| `test_generate_cpp_produces_valid_code` | method | `tests/test_uml.py:188` | `def test_generate_cpp_produces_valid_code(self)` |
| `test_generate_cpp_unknown_language_returns_error_message` | method | `tests/test_uml.py:223` | `def test_generate_cpp_unknown_language_returns_error_message(self)` |
| `test_generate_cpp_with_empty_classes` | method | `tests/test_uml.py:208` | `def test_generate_cpp_with_empty_classes(self)` |
| `test_generate_csharp_produces_valid_code` | method | `tests/test_uml.py:288` | `def test_generate_csharp_produces_valid_code(self)` |
| `test_generate_dart_produces_valid_code` | method | `tests/test_uml.py:474` | `def test_generate_dart_produces_valid_code(self)` |
| `test_generate_go_interface_produces_valid_code` | method | `tests/test_uml.py:330` | `def test_generate_go_interface_produces_valid_code(self)` |
| `test_generate_go_struct_produces_valid_code` | method | `tests/test_uml.py:313` | `def test_generate_go_struct_produces_valid_code(self)` |
| `test_generate_java_class_produces_valid_code` | method | `tests/test_uml.py:246` | `def test_generate_java_class_produces_valid_code(self)` |
| `test_generate_java_interface_produces_interface` | method | `tests/test_uml.py:265` | `def test_generate_java_interface_produces_interface(self)` |
| `test_generate_kotlin_produces_valid_code` | method | `tests/test_uml.py:446` | `def test_generate_kotlin_produces_valid_code(self)` |
| `test_generate_php_class_produces_valid_code` | method | `tests/test_uml.py:394` | `def test_generate_php_class_produces_valid_code(self)` |
| `test_generate_php_interface_produces_valid_code` | method | `tests/test_uml.py:411` | `def test_generate_php_interface_produces_valid_code(self)` |
| `test_generate_ruby_produces_valid_code` | method | `tests/test_uml.py:480` | `def test_generate_ruby_produces_valid_code(self)` |
| `test_generate_rust_struct_produces_valid_code` | method | `tests/test_uml.py:354` | `def test_generate_rust_struct_produces_valid_code(self)` |
| `test_generate_rust_trait_produces_valid_code` | method | `tests/test_uml.py:370` | `def test_generate_rust_trait_produces_valid_code(self)` |
| `test_generate_scala_produces_valid_code` | method | `tests/test_uml.py:452` | `def test_generate_scala_produces_valid_code(self)` |
| `test_generate_scala_trait_produces_valid_code` | method | `tests/test_uml.py:458` | `def test_generate_scala_trait_produces_valid_code(self)` |
| `test_generate_swift_produces_valid_code` | method | `tests/test_uml.py:463` | `def test_generate_swift_produces_valid_code(self)` |
| `test_generate_swift_protocol_produces_valid_code` | method | `tests/test_uml.py:469` | `def test_generate_swift_protocol_produces_valid_code(self)` |
| `test_render_empty_nodes_returns_empty_string` | method | `tests/test_uml.py:23` | `def test_render_empty_nodes_returns_empty_string(self)` |
| `test_render_multiple_classes_from_different_files` | method | `tests/test_uml.py:62` | `def test_render_multiple_classes_from_different_files(self)` |
| `test_render_no_class_symbols_returns_empty_string` | method | `tests/test_uml.py:27` | `def test_render_no_class_symbols_returns_empty_string(self)` |
| `test_render_respects_max_classes_limit` | method | `tests/test_uml.py:119` | `def test_render_respects_max_classes_limit(self)` |
| `test_render_single_class_produces_mermaid_class_diagram` | method | `tests/test_uml.py:42` | `def test_render_single_class_produces_mermaid_class_diagram(self)` |
| `test_render_with_import_edges_produces_relationships` | method | `tests/test_uml.py:90` | `def test_render_with_import_edges_produces_relationships(self)` |
| `test_render_with_structs_interfaces_traits` | method | `tests/test_uml.py:137` | `def test_render_with_structs_interfaces_traits(self)` |
| `test_sanitize_handles_empty_string` | method | `tests/test_uml.py:176` | `def test_sanitize_handles_empty_string(self)` |
| `test_sanitize_prefixes_digit_start` | method | `tests/test_uml.py:172` | `def test_sanitize_prefixes_digit_start(self)` |
| `test_sanitize_preserves_alphanumeric` | method | `tests/test_uml.py:164` | `def test_sanitize_preserves_alphanumeric(self)` |
| `test_sanitize_replaces_special_chars` | method | `tests/test_uml.py:168` | `def test_sanitize_replaces_special_chars(self)` |
| `TestWikiConfigContract` | class | `tests/test_wiki.py:49` | `class TestWikiConfigContract(TestCase)` |
| `TestWikiGenerationContract` | class | `tests/test_wiki.py:65` | `class TestWikiGenerationContract(TestCase)` |
| `_make_analysis` | function | `tests/test_wiki.py:27` | `def _make_analysis()` |
| `_make_node` | function | `tests/test_wiki.py:12` | `def _make_node(node_id, doc, symbols, language)` |
| `_make_nodes` | function | `tests/test_wiki.py:41` | `def _make_nodes()` |
| `_make_symbol` | function | `tests/test_wiki.py:23` | `def _make_symbol(name, kind, line, doc)` |
| `test_community_page_sections` | method | `tests/test_wiki.py:81` | `def test_community_page_sections(self)` |
| `test_config_defaults` | method | `tests/test_wiki.py:50` | `def test_config_defaults(self)` |
| `test_config_immutable` | method | `tests/test_wiki.py:58` | `def test_config_immutable(self)` |
| `test_connections_typed_with_confidence` | method | `tests/test_wiki.py:95` | `def test_connections_typed_with_confidence(self)` |
| `test_definition_names_core_file` | method | `tests/test_wiki.py:217` | `def test_definition_names_core_file(self)` |
| `test_deterministic_connections` | method | `tests/test_wiki.py:161` | `def test_deterministic_connections(self)` |
| `test_duplicate_community_labels_disambiguated` | method | `tests/test_wiki.py:240` | `def test_duplicate_community_labels_disambiguated(self)` |
| `test_duplicate_god_basenames_disambiguated` | method | `tests/test_wiki.py:259` | `def test_duplicate_god_basenames_disambiguated(self)` |
| `test_duplicate_symbol_scope_detected` | method | `tests/test_wiki.py:365` | `def test_duplicate_symbol_scope_detected(self)` |
| `test_fallback_single_community_without_analysis` | method | `tests/test_wiki.py:115` | `def test_fallback_single_community_without_analysis(self)` |
| `test_garbage_doc_filtered_from_definition` | method | `tests/test_wiki.py:210` | `def test_garbage_doc_filtered_from_definition(self)` |
| `test_garbage_purpose_filtered` | method | `tests/test_wiki.py:408` | `def test_garbage_purpose_filtered(self)` |
| `test_generate_writes_all_files` | method | `tests/test_wiki.py:66` | `def test_generate_writes_all_files(self)` |
| `test_index_entry_point` | method | `tests/test_wiki.py:139` | `def test_index_entry_point(self)` |
| `test_large_files_flagged_in_index_and_report` | method | `tests/test_wiki.py:302` | `def test_large_files_flagged_in_index_and_report(self)` |
| `test_leftover_files_covered_by_orphans_community` | method | `tests/test_wiki.py:184` | `def test_leftover_files_covered_by_orphans_community(self)` |
| `test_lint_healthy_after_generate` | method | `tests/test_wiki.py:152` | `def test_lint_healthy_after_generate(self)` |
| `test_no_duplicate_link_for_disjoint_scopes` | method | `tests/test_wiki.py:388` | `def test_no_duplicate_link_for_disjoint_scopes(self)` |
| `test_oversized_community_grouped_by_directory` | method | `tests/test_wiki.py:278` | `def test_oversized_community_grouped_by_directory(self)` |
| `test_privacy_mode_strips_docs` | method | `tests/test_wiki.py:174` | `def test_privacy_mode_strips_docs(self)` |
| `test_report_honest_audit_sections` | method | `tests/test_wiki.py:125` | `def test_report_honest_audit_sections(self)` |
| `test_risks_carry_fix_hint_scope_and_closed_cycle` | method | `tests/test_wiki.py:335` | `def test_risks_carry_fix_hint_scope_and_closed_cycle(self)` |
| `test_shared_context_link_for_disconnected_communities` | method | `tests/test_wiki.py:194` | `def test_shared_context_link_for_disconnected_communities(self)` |
| `test_stale_pages_pruned_on_regenerate` | method | `tests/test_wiki.py:323` | `def test_stale_pages_pruned_on_regenerate(self)` |
