# Symbols (page 1 of 4)
Pages: [SYMBOLS.md](SYMBOLS.md), [SYMBOLS_p2.md](SYMBOLS_p2.md), [SYMBOLS_p3.md](SYMBOLS_p3.md), [SYMBOLS_p4.md](SYMBOLS_p4.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_run_tests` | function | `readmenator/__main__.py:119` | `def _run_tests()` |
| `build_parser` | function | `readmenator/__main__.py:18` | `def build_parser()` |
| `main` | function | `readmenator/__main__.py:134` | `def main()` |
| `AgentInjector` | class | `readmenator/_agent_injector.py:123` | `class AgentInjector` |
| `__init__` | method | `readmenator/_agent_injector.py:134` | `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)` |
| `_build_injection` | method | `readmenator/_agent_injector.py:270` | `def _build_injection(self, fmt)` |
| `_build_mdc_injection` | method | `readmenator/_agent_injector.py:282` | `def _build_mdc_injection(self)` |
| `_extract_current_injection` | method | `readmenator/_agent_injector.py:235` | `def _extract_current_injection(content)` |
| `_find_agent_files` | method | `readmenator/_agent_injector.py:183` | `def _find_agent_files(self, root)` |
| `_inject_single` | method | `readmenator/_agent_injector.py:197` | `def _inject_single(self, path)` |
| `_prepend_mdc_frontmatter` | method | `readmenator/_agent_injector.py:287` | `def _prepend_mdc_frontmatter(content, injection)` |
| `_remove_old_injection` | method | `readmenator/_agent_injector.py:244` | `def _remove_old_injection(content)` |
| `_remove_single` | method | `readmenator/_agent_injector.py:254` | `def _remove_single(self, path)` |
| `ensure_readmenator_installed` | function | `readmenator/_agent_injector.py:101` | `def ensure_readmenator_installed()` |
| `find_agent_files` | method | `readmenator/_agent_injector.py:179` | `def find_agent_files(self, project_root)` |
| `inject` | method | `readmenator/_agent_injector.py:148` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_agent_injector.py:166` | `def remove(self, project_root)` |
| `AgentOutputGenerator` | class | `readmenator/_agent_output.py:70` | `class AgentOutputGenerator` |
| `__init__` | method | `readmenator/_agent_output.py:77` | `def __init__(self, config)` |
| `_build_api` | method | `readmenator/_agent_output.py:327` | `def _build_api(self, nodes, resolved_map, imported_by, layers)` |
| `_build_architecture` | method | `readmenator/_agent_output.py:204` | `def _build_architecture(self, edges, resolved_edges, nodes)` |
| `_build_gotchas` | method | `readmenator/_agent_output.py:503` | `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` |
| `_build_imported_by_map` | method | `readmenator/_agent_output.py:846` | `def _build_imported_by_map(resolved_edges)` |
| `_build_index` | method | `readmenator/_agent_output.py:172` | `def _build_index(self, nodes, subsystems, imported_by)` |
| `_build_manifest` | method | `readmenator/_agent_output.py:385` | `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root, subsystems, layers, out_dir)` |
| `_build_resolved_map` | method | `readmenator/_agent_output.py:836` | `def _build_resolved_map(resolved_edges)` |
| `_build_security` | method | `readmenator/_agent_output.py:256` | `def _build_security(self, findings, nodes)` |
| `_build_subsystem_content` | method | `readmenator/_agent_output.py:648` | `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)` |
| `_build_symbols` | method | `readmenator/_agent_output.py:481` | `def _build_symbols(self, nodes)` |
| `_chunk_unit` | method | `readmenator/_agent_output.py:877` | `def _chunk_unit(unit, budget)` |
| `_closed_loop` | method | `readmenator/_agent_output.py:496` | `def _closed_loop(cycle)` |
| `_deps_by_source` | method | `readmenator/_agent_output.py:826` | `def _deps_by_source(resolved_map)` |
| `_enclosing_symbol` | method | `readmenator/_agent_output.py:292` | `def _enclosing_symbol(symbols, line)` |
| `_entrypoints` | method | `readmenator/_agent_output.py:457` | `def _entrypoints(self, nodes, layers)` |
| `_infer_subsystems` | method | `readmenator/_agent_output.py:137` | `def _infer_subsystems(self, nodes)` |
| `_inventory` | method | `readmenator/_agent_output.py:468` | `def _inventory(self, out_dir)` |
| `_is_public` | method | `readmenator/_agent_output.py:302` | `def _is_public(self, sym)` |
| `_page_name` | method | `readmenator/_agent_output.py:856` | `def _page_name(filename, page)` |
| `_paginate` | method | `readmenator/_agent_output.py:894` | `def _paginate(self, filename, content)` |
| `_prune_owned` | method | `readmenator/_agent_output.py:943` | `def _prune_owned(out_dir)` |
| `_qualified_names` | method | `readmenator/_agent_output.py:309` | `def _qualified_names(symbols)` |
| `_safe_name` | method | `readmenator/_agent_output.py:626` | `def _safe_name(name)` |
| `_split_units` | method | `readmenator/_agent_output.py:864` | `def _split_units(body, is_table)` |
| `_write` | method | `readmenator/_agent_output.py:950` | `def _write(path, content)` |
| `_write_paged` | method | `readmenator/_agent_output.py:933` | `def _write_paged(self, out_dir, filename, content)` |
| `_write_recipes` | method | `readmenator/_agent_output.py:698` | `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` |
| `_write_subsystem_files` | method | `readmenator/_agent_output.py:633` | `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)` |
| `generate` | method | `readmenator/_agent_output.py:81` | `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` |
| `keep` | method | `readmenator/_agent_output.py:522` | `def keep(file_id)` |
| `GraphAnalyzer` | class | `readmenator/_analyzer.py:46` | `class GraphAnalyzer` |
| `__init__` | method | `readmenator/_analyzer.py:54` | `def __init__(self, config)` |
| `_aggregate` | method | `readmenator/_analyzer.py:308` | `def _aggregate(graph, partition)` |
| `_build_adjacency` | method | `readmenator/_analyzer.py:115` | `def _build_adjacency(self, nodes, edges)` |
| `_build_community_map` | method | `readmenator/_analyzer.py:427` | `def _build_community_map(self, communities)` |
| `_build_reverse_adjacency` | method | `readmenator/_analyzer.py:129` | `def _build_reverse_adjacency(self, adjacency)` |
| `_compute_cohesion` | method | `readmenator/_analyzer.py:437` | `def _compute_cohesion(self, communities, adjacency)` |
| `_compute_god_nodes` | method | `readmenator/_analyzer.py:139` | `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` |
| `_core_file` | method | `readmenator/_analyzer.py:412` | `def _core_file(members, node_map)` |
| `_detect_communities` | method | `readmenator/_analyzer.py:161` | `def _detect_communities(self, nodes, adjacency)` |
| `_finalize_communities` | method | `readmenator/_analyzer.py:213` | `def _finalize_communities(self, labels, adjacency)` |
| `_find_surprising_connections` | method | `readmenator/_analyzer.py:462` | `def _find_surprising_connections(self, nodes, adjacency, community_map)` |
| `_is_test_path` | function | `readmenator/_analyzer.py:40` | `def _is_test_path(file_id)` |
| `_label_communities` | method | `readmenator/_analyzer.py:384` | `def _label_communities(self, nodes, communities)` |
| `_louvain` | method | `readmenator/_analyzer.py:233` | `def _louvain(self, file_ids, adjacency)` |
| `_louvain_pass` | method | `readmenator/_analyzer.py:268` | `def _louvain_pass(self, graph, resolution, epsilon)` |
| `_merge_small_communities` | method | `readmenator/_analyzer.py:320` | `def _merge_small_communities(self, groups, adjacency, weights)` |
| `_shortest_path_communities` | method | `readmenator/_analyzer.py:502` | `def _shortest_path_communities(self, source, target, adjacency, community_map)` |
| `_suggest_questions` | method | `readmenator/_analyzer.py:529` | `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)` |
| `_vote_weights` | method | `readmenator/_analyzer.py:367` | `def _vote_weights(self, file_ids, adjacency)` |
| `analyze` | method | `readmenator/_analyzer.py:62` | `def analyze(self, nodes, edges, resolved_edges)` |
| `dominant_directory` | function | `readmenator/_analyzer.py:22` | `def dominant_directory(file_ids)` |
| `__init__` | method | `readmenator/_app.py:45` | `def __init__(self, config)` |
| `_inject_agent_files` | method | `readmenator/_app.py:326` | `def _inject_agent_files(self, root)` |
| `_inject_readme_link` | method | `readmenator/_app.py:318` | `def _inject_readme_link(self, root)` |
| `_live_renderer` | method | `readmenator/_app.py:760` | `def _live_renderer(self)` |
| `_log_summary` | method | `readmenator/_app.py:346` | `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)` |
| `_maybe_export_video` | method | `readmenator/_app.py:868` | `def _maybe_export_video(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2...` |
| `_maybe_publish_github_wiki` | method | `readmenator/_app.py:260` | `def _maybe_publish_github_wiki(self, root)` |
| `_maybe_refresh_pages` | method | `readmenator/_app.py:242` | `def _maybe_refresh_pages(self, root)` |
| `_resolve_imports` | method | `readmenator/_app.py:72` | `def _resolve_imports(self, nodes, edges, target_dir)` |
| `_scan` | method | `readmenator/_app.py:54` | `def _scan(self, target_dir)` |
| `_scan_for_cache` | method | `readmenator/_app.py:506` | `def _scan_for_cache(self, root, cache)` |
| `_scan_with_content` | method | `readmenator/_app.py:62` | `def _scan_with_content(self, target_dir)` |
| `_site_stats` | method | `readmenator/_app.py:748` | `def _site_stats(nodes, edges, analysis)` |
| `_write_sidecar_outputs` | method | `readmenator/_app.py:292` | `def _write_sidecar_outputs(self, root, findings, analysis_v2)` |
| `analyze` | method | `readmenator/_app.py:592` | `def analyze(self, target_dir)` |
| `audit` | method | `readmenator/_app.py:918` | `def audit(self, target_dir)` |
| `audit_deep` | method | `readmenator/_app.py:925` | `def audit_deep(self, target_dir)` |
| `check_freshness` | method | `readmenator/_app.py:215` | `def check_freshness(self, target_dir)` |
| `detect_layers` | method | `readmenator/_app.py:965` | `def detect_layers(self, target_dir)` |
| `explain` | method | `readmenator/_app.py:529` | `def explain(self, target_dir, symbol_name)` |
| `export` | method | `readmenator/_app.py:629` | `def export(self, target_dir)` |
| `export_cypher` | method | `readmenator/_app.py:645` | `def export_cypher(self, target_dir, output_path)` |
| `export_diagram` | method | `readmenator/_app.py:770` | `def export_diagram(self, target_dir, kind, output_path, full)` |
| `export_diagrams` | method | `readmenator/_app.py:709` | `def export_diagrams(self, target_dir, output_dir, full)` |
| `export_graphml` | method | `readmenator/_app.py:634` | `def export_graphml(self, target_dir, output_path)` |
| `export_html` | method | `readmenator/_app.py:607` | `def export_html(self, target_dir, output_path)` |
| `export_json` | method | `readmenator/_app.py:596` | `def export_json(self, target_dir, output_path)` |
| `export_obsidian` | method | `readmenator/_app.py:658` | `def export_obsidian(self, target_dir, output_dir)` |
| `export_pages` | method | `readmenator/_app.py:809` | `def export_pages(self, target_dir, output_dir, full)` |
| `export_rules` | method | `readmenator/_app.py:955` | `def export_rules(self, target_dir, output_dir)` |
| `export_sarif` | method | `readmenator/_app.py:945` | `def export_sarif(self, target_dir, output_path)` |
| `export_svg` | method | `readmenator/_app.py:618` | `def export_svg(self, target_dir, output_path)` |
| `export_video` | method | `readmenator/_app.py:844` | `def export_video(self, target_dir, output_path)` |
| `export_wiki` | method | `readmenator/_app.py:668` | `def export_wiki(self, target_dir, output_dir)` |
| `find_path` | method | `readmenator/_app.py:541` | `def find_path(self, target_dir, symbol_a, symbol_b)` |
| `generate_cursorrules` | method | `readmenator/_app.py:998` | `def generate_cursorrules(self, target_dir)` |
| `generate_uml_code` | method | `readmenator/_app.py:334` | `def generate_uml_code(self, target_dir, language, output_path)` |
| `lint` | method | `readmenator/_app.py:975` | `def lint(self, target_dir)` |
| `lint_wiki` | method | `readmenator/_app.py:691` | `def lint_wiki(self, target_dir)` |
| `on_change` | method | `readmenator/_app.py:912` | `def on_change()` |
| `publish_github_wiki` | method | `readmenator/_app.py:278` | `def publish_github_wiki(self, target_dir, dry_run)` |
| `query` | method | `readmenator/_app.py:524` | `def query(self, target_dir, question)` |
| `rank_query` | method | `readmenator/_app.py:559` | `def rank_query(self, target_dir, query, top_n)` |
| `readmenatorApplication` | class | `readmenator/_app.py:44` | `class readmenatorApplication` |
| `rebuild` | method | `readmenator/_app.py:589` | `def rebuild(self, target_dir, run_security)` |
| `refactor_monolith` | method | `readmenator/_app.py:1013` | `def refactor_monolith(self, target_dir)` |
| `run` | method | `readmenator/_app.py:91` | `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)` |
| `strip_dead_code` | method | `readmenator/_app.py:988` | `def strip_dead_code(self, target_dir)` |
| `summary` | method | `readmenator/_app.py:554` | `def summary(self, target_dir)` |
| `update` | method | `readmenator/_app.py:401` | `def update(self, target_dir, run_security)` |
| `watch` | method | `readmenator/_app.py:908` | `def watch(self, target_dir)` |
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
| `source_fingerprint` | method | `readmenator/_cache.py:179` | `def source_fingerprint(project_root, file_ids)` |
| `Category` | class | `readmenator/_category.py:78` | `class Category` |
| `EdgeKind` | class | `readmenator/_category.py:24` | `class EdgeKind(str, Enum)` |
| `Morphism` | class | `readmenator/_category.py:57` | `class Morphism` |
| `TypedGraph` | class | `readmenator/_category.py:181` | `class TypedGraph` |
| `__init__` | method | `readmenator/_category.py:86` | `def __init__(self)` |
| `__init__` | method | `readmenator/_category.py:188` | `def __init__(self, category)` |
| `__str__` | method | `readmenator/_category.py:38` | `def __str__(self)` |
| `_compose_kind` | method | `readmenator/_category.py:157` | `def _compose_kind(a, b)` |
| `_compute_out_weights` | method | `readmenator/_category.py:197` | `def _compute_out_weights(self)` |
| `_infer_edge_kind` | method | `readmenator/_category.py:278` | `def _infer_edge_kind(relation)` |
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
| `CodePropertyGraph` | class | `readmenator/_cpg.py:16` | `class CodePropertyGraph` |
| `__init__` | method | `readmenator/_cpg.py:26` | `def __init__(self, privacy_mode, cpg_context)` |
| `_build_symbol_list` | method | `readmenator/_cpg.py:153` | `def _build_symbol_list(self, node)` |
| `_compute_node_hash` | method | `readmenator/_cpg.py:169` | `def _compute_node_hash(node)` |
| `_severity_counts` | method | `readmenator/_cpg.py:147` | `def _severity_counts(self, findings)` |
| `generate` | method | `readmenator/_cpg.py:30` | `def generate(self, nodes, edges, resolved_edges, analysis, findings)` |
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
| `DocsSitePublisher` | class | `readmenator/_diagrams.py:2992` | `class DocsSitePublisher` |
| `InteractiveMapRenderer` | class | `readmenator/_diagrams.py:1501` | `class InteractiveMapRenderer` |
| `MapDelta` | class | `readmenator/_diagrams.py:191` | `class MapDelta` |
| `MapDiagnostic` | class | `readmenator/_diagrams.py:157` | `class MapDiagnostic` |
| `MapEdge` | class | `readmenator/_diagrams.py:102` | `class MapEdge` |
| `MapNode` | class | `readmenator/_diagrams.py:69` | `class MapNode` |
| `MapReceipt` | class | `readmenator/_diagrams.py:174` | `class MapReceipt` |
| `MapView` | class | `readmenator/_diagrams.py:119` | `class MapView` |
| `SystemMap` | class | `readmenator/_diagrams.py:136` | `class SystemMap` |
| `SystemMapBuilder` | class | `readmenator/_diagrams.py:435` | `class SystemMapBuilder` |
| `SystemMapValidator` | class | `readmenator/_diagrams.py:211` | `class SystemMapValidator` |
| `VisNetworkRenderer` | class | `readmenator/_diagrams.py:2216` | `class VisNetworkRenderer` |
| `__init__` | method | `readmenator/_diagrams.py:214` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:464` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:1504` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:2224` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:3009` | `def __init__(self, config)` |
| `_annotate_communities` | method | `readmenator/_diagrams.py:536` | `def _annotate_communities(system_map, analysis)` |
| `_build_architecture` | method | `readmenator/_diagrams.py:1103` | `def _build_architecture(self, nodes, links, layers, findings, analysis, full)` |
| `_build_dataflow` | method | `readmenator/_diagrams.py:1325` | `def _build_dataflow(self, nodes, links, layers, findings, full)` |
| `_build_lifecycle` | method | `readmenator/_diagrams.py:1408` | `def _build_lifecycle(self, nodes, links, layers, findings, full)` |
| `_build_sequence` | method | `readmenator/_diagrams.py:1243` | `def _build_sequence(self, nodes, links, layers, analysis, full)` |
| `_build_workflow` | method | `readmenator/_diagrams.py:1163` | `def _build_workflow(self, nodes, links, layers, findings, full)` |
| `_canvas_for` | method | `readmenator/_diagrams.py:990` | `def _canvas_for(self, positions, full)` |
| `_canvas_size` | method | `readmenator/_diagrams.py:1512` | `def _canvas_size(self, system_map)` |
| `_cap_lane_scope` | method | `readmenator/_diagrams.py:895` | `def _cap_lane_scope(self, ranked, layer_of)` |
| `_card` | method | `readmenator/_diagrams.py:3688` | `def _card(self, kind, system_map, href_prefix)` |
| `_community_legend` | method | `readmenator/_diagrams.py:2340` | `def _community_legend(self, system_map)` |
| `_doc_group` | method | `readmenator/_diagrams.py:3549` | `def _doc_group(self, name)` |
| `_doc_preview` | method | `readmenator/_diagrams.py:3265` | `def _doc_preview(self, text)` |
| `_doc_title` | method | `readmenator/_diagrams.py:3256` | `def _doc_title(text)` |
| `_docs_section` | method | `readmenator/_diagrams.py:3559` | `def _docs_section(self, doc_entries)` |
| `_edge_path` | method | `readmenator/_diagrams.py:1687` | `def _edge_path(self, x1, y1, x2, y2)` |
| `_edges_svg` | method | `readmenator/_diagrams.py:1771` | `def _edges_svg(self, system_map)` |
| `_effective_canvas` | method | `readmenator/_diagrams.py:222` | `def _effective_canvas(self, system_map)` |
| `_escape` | method | `readmenator/_diagrams.py:1665` | `def _escape(self, value)` |
| `_escape` | method | `readmenator/_diagrams.py:3743` | `def _escape(self, value)` |
| `_escape_markup` | function | `readmenator/_diagrams.py:31` | `def _escape_markup(value)` |
| `_fitted_gap` | method | `readmenator/_diagrams.py:857` | `def _fitted_gap(self, count, item, gap, total, margin)` |
| `_glyph` | method | `readmenator/_diagrams.py:3670` | `def _glyph(self, kind)` |
| `_href_prefix` | method | `readmenator/_diagrams.py:3640` | `def _href_prefix(self)` |
| `_internal_links` | method | `readmenator/_diagrams.py:732` | `def _internal_links(self, edges, selected, full)` |
| `_is_full` | method | `readmenator/_diagrams.py:481` | `def _is_full(self, full)` |
| `_json_payload` | function | `readmenator/_diagrams.py:43` | `def _json_payload(payload)` |
| `_lane_capacity` | method | `readmenator/_diagrams.py:881` | `def _lane_capacity(self)` |
| `_lanes_that_fit` | method | `readmenator/_diagrams.py:840` | `def _lanes_that_fit(self, lanes)` |
| `_layout_columns` | method | `readmenator/_diagrams.py:792` | `def _layout_columns(self, items, kind, full)` |
| `_layout_sequence` | method | `readmenator/_diagrams.py:919` | `def _layout_sequence(self, ordered, full)` |
| `_make_views` | method | `readmenator/_diagrams.py:1031` | `def _make_views(self, kind, primary, links)` |
| `_meta_for` | method | `readmenator/_diagrams.py:1008` | `def _meta_for(self, kind, placed, links, total, positions, full)` |
| `_nodes_svg` | method | `readmenator/_diagrams.py:1723` | `def _nodes_svg(self, system_map)` |
| `_place` | method | `readmenator/_diagrams.py:970` | `def _place(self, ranked, layer_of, kind, full)` |
| `_prune_stale_docs` | method | `readmenator/_diagrams.py:3301` | `def _prune_stale_docs(docs_root, keep)` |
| `_ranked_file_ids` | method | `readmenator/_diagrams.py:671` | `def _ranked_file_ids(self, nodes, links, analysis)` |
| `_render_poster` | method | `readmenator/_diagrams.py:3218` | `def _render_poster(self, video, site_root)` |
| `_role_color` | function | `readmenator/_diagrams.py:55` | `def _role_color(role, config)` |
| `_role_color` | method | `readmenator/_diagrams.py:1676` | `def _role_color(self, role)` |
| `_role_for` | method | `readmenator/_diagrams.py:637` | `def _role_for(self, group, sensitive)` |
| `_safe_json` | method | `readmenator/_diagrams.py:1654` | `def _safe_json(self, payload)` |
| `_select_primary` | method | `readmenator/_diagrams.py:706` | `def _select_primary(self, nodes, links, analysis, full)` |
| `_sensitive_files` | method | `readmenator/_diagrams.py:654` | `def _sensitive_files(self, findings)` |
| `_sequence_capacity` | method | `readmenator/_diagrams.py:956` | `def _sequence_capacity(self)` |
| `_short_label` | method | `readmenator/_diagrams.py:777` | `def _short_label(self, value)` |
| `_start_here` | method | `readmenator/_diagrams.py:3482` | `def _start_here(self, entries, video_rel)` |
| `_stat_tiles` | method | `readmenator/_diagrams.py:3462` | `def _stat_tiles(self, stats)` |
| `_stats_line` | method | `readmenator/_diagrams.py:3729` | `def _stats_line(self, stats)` |
| `_symbol_records` | method | `readmenator/_diagrams.py:755` | `def _symbol_records(self, node)` |
| `_template` | method | `readmenator/_diagrams.py:1818` | `def _template(self)` |
| `_template` | method | `readmenator/_diagrams.py:2408` | `def _template(self)` |
| `_title_for` | method | `readmenator/_diagrams.py:623` | `def _title_for(self, kind)` |
| `_tooltip` | method | `readmenator/_diagrams.py:2377` | `def _tooltip(self, node)` |
| `_video_section` | method | `readmenator/_diagrams.py:3522` | `def _video_section(self, video_rel, poster_rel)` |
| `build` | method | `readmenator/_diagrams.py:494` | `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)` |
| `build_all` | method | `readmenator/_diagrams.py:553` | `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)` |
| `collect_doc_sources` | method | `readmenator/_diagrams.py:3123` | `def collect_doc_sources(self, project_root)` |
| `compare` | method | `readmenator/_diagrams.py:584` | `def compare(self, base, head)` |
| `description_for` | method | `readmenator/_diagrams.py:3019` | `def description_for(self, kind)` |
| `doc_order` | method | `readmenator/_diagrams.py:3585` | `def doc_order(base)` |
| `order` | method | `readmenator/_diagrams.py:3366` | `def order(entry)` |
| `publish` | method | `readmenator/_diagrams.py:3033` | `def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries)` |
| `publish_assets` | method | `readmenator/_diagrams.py:3149` | `def publish_assets(self, project_root, output_dir)` |
| `render` | method | `readmenator/_diagrams.py:1533` | `def render(self, system_map)` |
| `render` | method | `readmenator/_diagrams.py:2232` | `def render(self, system_map)` |
| `render_index` | method | `readmenator/_diagrams.py:3394` | `def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries, poster_rel)` |
| `render_llms_txt` | method | `readmenator/_diagrams.py:3318` | `def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)` |
| `supported_kinds` | method | `readmenator/_diagrams.py:473` | `def supported_kinds(self)` |
| `validate` | method | `readmenator/_diagrams.py:243` | `def validate(self, system_map)` |
| `write` | method | `readmenator/_diagrams.py:1635` | `def write(self, system_map, output_path)` |
| `write` | method | `readmenator/_diagrams.py:2360` | `def write(self, system_map, output_path)` |
| `DocumentationGenerator` | class | `readmenator/_documentation.py:33` | `class DocumentationGenerator` |
| `__init__` | method | `readmenator/_documentation.py:45` | `def __init__(self, config)` |
| `_apply_context_budget` | method | `readmenator/_documentation.py:178` | `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)` |
| `_build_architecture_reference` | method | `readmenator/_documentation.py:1083` | `def _build_architecture_reference(self, nodes, edges)` |
| `_build_change_impact` | method | `readmenator/_documentation.py:883` | `def _build_change_impact(self, analysis_v2)` |
| `_build_community_analysis` | method | `readmenator/_documentation.py:546` | `def _build_community_analysis(self, analysis, nodes)` |
| `_build_cpg_block` | method | `readmenator/_documentation.py:1057` | `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)` |
| `_build_dashboard` | method | `readmenator/_documentation.py:438` | `def _build_dashboard(self, nodes, edges, resolved_edges)` |
| `_build_dataflow_analysis` | method | `readmenator/_documentation.py:831` | `def _build_dataflow_analysis(self, analysis_v2)` |
| `_build_dependency_cycles` | method | `readmenator/_documentation.py:862` | `def _build_dependency_cycles(self, analysis_v2)` |
| `_build_god_nodes` | method | `readmenator/_documentation.py:518` | `def _build_god_nodes(self, analysis, ranked)` |
| `_build_hotspots` | method | `readmenator/_documentation.py:793` | `def _build_hotspots(self, analysis_v2, ranked)` |
| `_build_layer_violations` | method | `readmenator/_documentation.py:908` | `def _build_layer_violations(self, analysis_v2)` |
| `_build_layers` | method | `readmenator/_documentation.py:404` | `def _build_layers(self, layers, nodes)` |
| `_build_mermaid_section` | method | `readmenator/_documentation.py:1008` | `def _build_mermaid_section(self, graph_output, is_truncated)` |
| `_build_orphans` | method | `readmenator/_documentation.py:666` | `def _build_orphans(self, nodes, analysis_v2, ranked)` |
| `_build_query_recipes` | method | `readmenator/_documentation.py:716` | `def _build_query_recipes(self)` |
| `_build_ranked_context` | method | `readmenator/_documentation.py:620` | `def _build_ranked_context(self, ranked)` |
| `_build_security_findings` | method | `readmenator/_documentation.py:961` | `def _build_security_findings(self, findings)` |
| `_build_suggested_questions` | method | `readmenator/_documentation.py:604` | `def _build_suggested_questions(self, analysis)` |
| `_build_suggested_rules` | method | `readmenator/_documentation.py:936` | `def _build_suggested_rules(self, analysis_v2)` |
| `_build_surprising_connections` | method | `readmenator/_documentation.py:579` | `def _build_surprising_connections(self, analysis, nodes)` |
| `_build_taint_analysis` | method | `readmenator/_documentation.py:758` | `def _build_taint_analysis(self, analysis_v2)` |
| `_build_toc` | method | `readmenator/_documentation.py:316` | `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)` |
| `_build_uml_diagram` | method | `readmenator/_documentation.py:1031` | `def _build_uml_diagram(self, nodes, edges)` |
| `_get_git_commit` | method | `readmenator/_documentation.py:81` | `def _get_git_commit()` |
| `_ranking_version` | method | `readmenator/_documentation.py:63` | `def _ranking_version(self)` |
| `generate` | method | `readmenator/_documentation.py:91` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)` |
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
| `GitHubWikiPublisher` | class | `readmenator/_gh_wiki.py:59` | `class GitHubWikiPublisher` |
| `WikiPublishResult` | class | `readmenator/_gh_wiki.py:39` | `class WikiPublishResult` |
| `__init__` | method | `readmenator/_gh_wiki.py:62` | `def __init__(self, config, runner)` |
| `_blob_base` | method | `readmenator/_gh_wiki.py:121` | `def _blob_base(self, remote, commit)` |
| `_call` | method | `readmenator/_gh_wiki.py:279` | `def _call(self, command, cwd)` |
| `_fallback_home` | method | `readmenator/_gh_wiki.py:205` | `def _fallback_home(self, project_name)` |
| `_footer` | method | `readmenator/_gh_wiki.py:241` | `def _footer(git)` |
| `_origin` | method | `readmenator/_gh_wiki.py:267` | `def _origin(self, project_root)` |
| `_sidebar` | method | `readmenator/_gh_wiki.py:213` | `def _sidebar(self, names)` |
| `_write_pages` | method | `readmenator/_gh_wiki.py:293` | `def _write_pages(self, target, pages)` |
| `collect_sources` | method | `readmenator/_gh_wiki.py:96` | `def collect_sources(self, project_root)` |
| `link` | method | `readmenator/_gh_wiki.py:151` | `def link(match)` |
| `page_name` | method | `readmenator/_gh_wiki.py:72` | `def page_name(self, rel_path)` |
| `permalink` | method | `readmenator/_gh_wiki.py:164` | `def permalink(match)` |
| `publish` | method | `readmenator/_gh_wiki.py:313` | `def publish(self, project_root, dry_run)` |
| `render` | method | `readmenator/_gh_wiki.py:179` | `def render(self, project_root, remote)` |
| `rewrite` | method | `readmenator/_gh_wiki.py:129` | `def rewrite(self, text, rel_path, names, project_root, blob_base)` |
| `wiki_remote` | method | `readmenator/_gh_wiki.py:249` | `def wiki_remote(self, project_root)` |
| `_git_dir` | function | `readmenator/_gitmeta.py:38` | `def _git_dir(root)` |
| `_packed_ref` | function | `readmenator/_gitmeta.py:59` | `def _packed_ref(git_dir, ref)` |
| `_read_small` | function | `readmenator/_gitmeta.py:19` | `def _read_small(path)` |
| `read_git_head` | function | `readmenator/_gitmeta.py:84` | `def read_git_head(project_root)` |
| `HotspotAnalyzer` | class | `readmenator/_hotspots.py:22` | `class HotspotAnalyzer` |
| `__init__` | method | `readmenator/_hotspots.py:31` | `def __init__(self, config)` |
| `_dfs_visit` | method | `readmenator/_hotspots.py:114` | `def _dfs_visit(current)` |
| `_record_cycle` | method | `readmenator/_hotspots.py:125` | `def _record_cycle(start, end)` |
| `analyze_change_impact` | method | `readmenator/_hotspots.py:155` | `def analyze_change_impact(self, nodes, resolved_edges)` |
| `analyze_hotspots` | method | `readmenator/_hotspots.py:34` | `def analyze_hotspots(self, nodes, edges, resolved_edges)` |
| `detect_cycles` | method | `readmenator/_hotspots.py:90` | `def detect_cycles(self, nodes, resolved_edges)` |
| `LayerRuleEngine` | class | `readmenator/_layer_rules.py:11` | `class LayerRuleEngine` |
| `__init__` | method | `readmenator/_layer_rules.py:36` | `def __init__(self, config)` |
| `detect_violations` | method | `readmenator/_layer_rules.py:39` | `def detect_violations(self, nodes, edges, resolved_edges, layers)` |
| `violation_summary` | method | `readmenator/_layer_rules.py:111` | `def violation_summary(violations)` |
| `LayerDetector` | class | `readmenator/_layers.py:17` | `class LayerDetector` |
| `_classify_file` | method | `readmenator/_layers.py:138` | `def _classify_file(self, node, edges, imports)` |
| `_import_roots` | method | `readmenator/_layers.py:128` | `def _import_roots(cls, imports)` |
| `_path_tokens` | method | `readmenator/_layers.py:108` | `def _path_tokens(cls, node_id)` |
| `_pattern_hits` | method | `readmenator/_layers.py:114` | `def _pattern_hits(cls, pattern, tokens, joined)` |
| `detect` | method | `readmenator/_layers.py:83` | `def detect(self, nodes, edges)` |
| `layer_summary` | method | `readmenator/_layers.py:189` | `def layer_summary(layers)` |
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
| `__init__` | method | `readmenator/_mermaid.py:26` | `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style...` |
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
| `AnalyzerFactory` | class | `readmenator/_pipeline.py:49` | `class AnalyzerFactory` |
| `DeepAnalysisRunner` | class | `readmenator/_pipeline.py:292` | `class DeepAnalysisRunner` |
| `__init__` | method | `readmenator/_pipeline.py:57` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_pipeline.py:301` | `def __init__(self, factory)` |
| `agent_injector` | method | `readmenator/_pipeline.py:193` | `def agent_injector(self)` |
| `agent_output` | method | `readmenator/_pipeline.py:210` | `def agent_output(self)` |
| `analyzer` | method | `readmenator/_pipeline.py:100` | `def analyzer(self)` |
| `build_typed_graph` | method | `readmenator/_pipeline.py:257` | `def build_typed_graph(self, nodes, edges, resolved_edges)` |
| `cpg` | method | `readmenator/_pipeline.py:155` | `def cpg(self)` |
| `dataflow` | method | `readmenator/_pipeline.py:124` | `def dataflow(self)` |
| `diagram_builder` | method | `readmenator/_pipeline.py:216` | `def diagram_builder(self)` |
| `diagram_publisher` | method | `readmenator/_pipeline.py:237` | `def diagram_publisher(self)` |
| `diagram_renderer` | method | `readmenator/_pipeline.py:223` | `def diagram_renderer(self)` |
| `diagram_validator` | method | `readmenator/_pipeline.py:230` | `def diagram_validator(self)` |
| `exporter` | method | `readmenator/_pipeline.py:112` | `def exporter(self)` |
| `generator` | method | `readmenator/_pipeline.py:94` | `def generator(self)` |
| `gh_wiki` | method | `readmenator/_pipeline.py:203` | `def gh_wiki(self)` |
| `hotspots` | method | `readmenator/_pipeline.py:131` | `def hotspots(self)` |
| `last_category` | method | `readmenator/_pipeline.py:284` | `def last_category(self)` |
| `last_typed_graph` | method | `readmenator/_pipeline.py:288` | `def last_typed_graph(self)` |
| `layer_detector` | method | `readmenator/_pipeline.py:164` | `def layer_detector(self)` |
| `layer_rules` | method | `readmenator/_pipeline.py:137` | `def layer_rules(self)` |
| `make_ranker` | method | `readmenator/_pipeline.py:267` | `def make_ranker(self, typed_graph)` |
| `readme_injector` | method | `readmenator/_pipeline.py:183` | `def readme_injector(self)` |
| `rule_gen` | method | `readmenator/_pipeline.py:143` | `def rule_gen(self)` |
| `run` | method | `readmenator/_pipeline.py:304` | `def run(self, nodes, edges, resolved_edges, layers, content_map)` |
| `sarif` | method | `readmenator/_pipeline.py:149` | `def sarif(self)` |
| `scanner` | method | `readmenator/_pipeline.py:88` | `def scanner(self)` |
| `security` | method | `readmenator/_pipeline.py:106` | `def security(self)` |
| `taint` | method | `readmenator/_pipeline.py:118` | `def taint(self)` |
| `uml` | method | `readmenator/_pipeline.py:170` | `def uml(self)` |
| `video` | method | `readmenator/_pipeline.py:251` | `def video(self)` |

Next: [SYMBOLS_p2.md](SYMBOLS_p2.md)
