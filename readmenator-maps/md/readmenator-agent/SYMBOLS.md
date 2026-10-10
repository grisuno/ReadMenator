# Symbols (page 1 of 5)
Pages: [SYMBOLS.md](SYMBOLS.md), [SYMBOLS_p2.md](SYMBOLS_p2.md), [SYMBOLS_p3.md](SYMBOLS_p3.md), [SYMBOLS_p4.md](SYMBOLS_p4.md), [SYMBOLS_p5.md](SYMBOLS_p5.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_run_tests` | function | `readmenator/__main__.py:132` | `def _run_tests()` |
| `build_parser` | function | `readmenator/__main__.py:18` | `def build_parser()` |
| `main` | function | `readmenator/__main__.py:147` | `def main()` |
| `AgentInjector` | class | `readmenator/_agent_injector.py:129` | `class AgentInjector` |
| `__init__` | method | `readmenator/_agent_injector.py:140` | `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)` |
| `_build_injection` | method | `readmenator/_agent_injector.py:276` | `def _build_injection(self, fmt)` |
| `_build_mdc_injection` | method | `readmenator/_agent_injector.py:288` | `def _build_mdc_injection(self)` |
| `_extract_current_injection` | method | `readmenator/_agent_injector.py:241` | `def _extract_current_injection(content)` |
| `_find_agent_files` | method | `readmenator/_agent_injector.py:189` | `def _find_agent_files(self, root)` |
| `_inject_single` | method | `readmenator/_agent_injector.py:203` | `def _inject_single(self, path)` |
| `_prepend_mdc_frontmatter` | method | `readmenator/_agent_injector.py:293` | `def _prepend_mdc_frontmatter(content, injection)` |
| `_remove_old_injection` | method | `readmenator/_agent_injector.py:250` | `def _remove_old_injection(content)` |
| `_remove_single` | method | `readmenator/_agent_injector.py:260` | `def _remove_single(self, path)` |
| `ensure_readmenator_installed` | function | `readmenator/_agent_injector.py:107` | `def ensure_readmenator_installed()` |
| `find_agent_files` | method | `readmenator/_agent_injector.py:185` | `def find_agent_files(self, project_root)` |
| `inject` | method | `readmenator/_agent_injector.py:154` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_agent_injector.py:172` | `def remove(self, project_root)` |
| `AgentOutputGenerator` | class | `readmenator/_agent_output.py:70` | `class AgentOutputGenerator` |
| `__init__` | method | `readmenator/_agent_output.py:77` | `def __init__(self, config)` |
| `_build_api` | method | `readmenator/_agent_output.py:328` | `def _build_api(self, nodes, resolved_map, imported_by, layers)` |
| `_build_architecture` | method | `readmenator/_agent_output.py:205` | `def _build_architecture(self, edges, resolved_edges, nodes)` |
| `_build_concepts` | method | `readmenator/_agent_output.py:628` | `def _build_concepts(self, analysis_v2)` |
| `_build_gotchas` | method | `readmenator/_agent_output.py:506` | `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` |
| `_build_imported_by_map` | method | `readmenator/_agent_output.py:888` | `def _build_imported_by_map(resolved_edges)` |
| `_build_index` | method | `readmenator/_agent_output.py:173` | `def _build_index(self, nodes, subsystems, imported_by)` |
| `_build_manifest` | method | `readmenator/_agent_output.py:386` | `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root, subsystems, layers, out_dir)` |
| `_build_resolved_map` | method | `readmenator/_agent_output.py:878` | `def _build_resolved_map(resolved_edges)` |
| `_build_security` | method | `readmenator/_agent_output.py:257` | `def _build_security(self, findings, nodes)` |
| `_build_subsystem_content` | method | `readmenator/_agent_output.py:690` | `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)` |
| `_build_symbols` | method | `readmenator/_agent_output.py:484` | `def _build_symbols(self, nodes)` |
| `_chunk_unit` | method | `readmenator/_agent_output.py:919` | `def _chunk_unit(unit, budget)` |
| `_closed_loop` | method | `readmenator/_agent_output.py:499` | `def _closed_loop(cycle)` |
| `_deps_by_source` | method | `readmenator/_agent_output.py:868` | `def _deps_by_source(resolved_map)` |
| `_enclosing_symbol` | method | `readmenator/_agent_output.py:293` | `def _enclosing_symbol(symbols, line)` |
| `_entrypoints` | method | `readmenator/_agent_output.py:460` | `def _entrypoints(self, nodes, layers)` |
| `_infer_subsystems` | method | `readmenator/_agent_output.py:138` | `def _infer_subsystems(self, nodes)` |
| `_inventory` | method | `readmenator/_agent_output.py:471` | `def _inventory(self, out_dir)` |
| `_is_public` | method | `readmenator/_agent_output.py:303` | `def _is_public(self, sym)` |
| `_page_name` | method | `readmenator/_agent_output.py:898` | `def _page_name(filename, page)` |
| `_paginate` | method | `readmenator/_agent_output.py:936` | `def _paginate(self, filename, content)` |
| `_prune_owned` | method | `readmenator/_agent_output.py:985` | `def _prune_owned(out_dir)` |
| `_qualified_names` | method | `readmenator/_agent_output.py:310` | `def _qualified_names(symbols)` |
| `_safe_name` | method | `readmenator/_agent_output.py:668` | `def _safe_name(name)` |
| `_split_units` | method | `readmenator/_agent_output.py:906` | `def _split_units(body, is_table)` |
| `_write` | method | `readmenator/_agent_output.py:992` | `def _write(path, content)` |
| `_write_paged` | method | `readmenator/_agent_output.py:975` | `def _write_paged(self, out_dir, filename, content)` |
| `_write_recipes` | method | `readmenator/_agent_output.py:740` | `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` |
| `_write_subsystem_files` | method | `readmenator/_agent_output.py:675` | `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)` |
| `generate` | method | `readmenator/_agent_output.py:81` | `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` |
| `keep` | method | `readmenator/_agent_output.py:525` | `def keep(file_id)` |
| `AnalyticsBuilder` | class | `readmenator/_analytics.py:25` | `class AnalyticsBuilder` |
| `__init__` | method | `readmenator/_analytics.py:28` | `def __init__(self, config)` |
| `_hotspot_ranking` | method | `readmenator/_analytics.py:120` | `def _hotspot_ranking(self, nodes, fan_in, fan_out, hotspots)` |
| `_language_distribution` | method | `readmenator/_analytics.py:112` | `def _language_distribution(self, nodes)` |
| `_layer_distribution` | method | `readmenator/_analytics.py:100` | `def _layer_distribution(self, nodes, layers)` |
| `_rule_yield` | method | `readmenator/_analytics.py:152` | `def _rule_yield(self, findings)` |
| `_scatter` | method | `readmenator/_analytics.py:181` | `def _scatter(self, nodes, fan_in, fan_out, layers)` |
| `_size_bands` | method | `readmenator/_analytics.py:164` | `def _size_bands(self, nodes)` |
| `build` | method | `readmenator/_analytics.py:36` | `def build(self, nodes, edges, resolved_edges, analysis, findings, layers, v2, hotspots)` |
| `GraphAnalyzer` | class | `readmenator/_analyzer.py:46` | `class GraphAnalyzer` |
| `__init__` | method | `readmenator/_analyzer.py:54` | `def __init__(self, config)` |
| `_aggregate` | method | `readmenator/_analyzer.py:322` | `def _aggregate(graph, partition)` |
| `_build_adjacency` | method | `readmenator/_analyzer.py:115` | `def _build_adjacency(self, nodes, edges)` |
| `_build_community_map` | method | `readmenator/_analyzer.py:441` | `def _build_community_map(self, communities)` |
| `_build_reverse_adjacency` | method | `readmenator/_analyzer.py:129` | `def _build_reverse_adjacency(self, adjacency)` |
| `_compute_cohesion` | method | `readmenator/_analyzer.py:451` | `def _compute_cohesion(self, communities, adjacency)` |
| `_compute_god_nodes` | method | `readmenator/_analyzer.py:139` | `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` |
| `_core_file` | method | `readmenator/_analyzer.py:426` | `def _core_file(members, node_map)` |
| `_detect_communities` | method | `readmenator/_analyzer.py:161` | `def _detect_communities(self, nodes, adjacency)` |
| `_finalize_communities` | method | `readmenator/_analyzer.py:213` | `def _finalize_communities(self, labels, adjacency)` |
| `_find_surprising_connections` | method | `readmenator/_analyzer.py:476` | `def _find_surprising_connections(self, nodes, adjacency, community_map)` |
| `_is_test_path` | function | `readmenator/_analyzer.py:40` | `def _is_test_path(file_id)` |
| `_label_communities` | method | `readmenator/_analyzer.py:398` | `def _label_communities(self, nodes, communities)` |
| `_louvain` | method | `readmenator/_analyzer.py:233` | `def _louvain(self, file_ids, adjacency)` |
| `_louvain_pass` | method | `readmenator/_analyzer.py:282` | `def _louvain_pass(self, graph, resolution, epsilon)` |
| `_merge_small_communities` | method | `readmenator/_analyzer.py:334` | `def _merge_small_communities(self, groups, adjacency, weights)` |
| `_shortest_path_communities` | method | `readmenator/_analyzer.py:516` | `def _shortest_path_communities(self, source, target, adjacency, community_map)` |
| `_suggest_questions` | method | `readmenator/_analyzer.py:543` | `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)` |
| `_vote_weights` | method | `readmenator/_analyzer.py:381` | `def _vote_weights(self, file_ids, adjacency)` |
| `analyze` | method | `readmenator/_analyzer.py:62` | `def analyze(self, nodes, edges, resolved_edges)` |
| `dominant_directory` | function | `readmenator/_analyzer.py:22` | `def dominant_directory(file_ids)` |
| `partition` | method | `readmenator/_analyzer.py:268` | `def partition(self, ids, adjacency)` |
| `__init__` | method | `readmenator/_app.py:50` | `def __init__(self, config)` |
| `_explorer_cards` | method | `readmenator/_app.py:760` | `def _explorer_cards(self, dest, href, home_href, nodes, edges, resolved, analysis, layers, findings)` |
| `_forcegraph_dest` | method | `readmenator/_app.py:665` | `def _forcegraph_dest(self, target_dir, output_path)` |
| `_inject_agent_files` | method | `readmenator/_app.py:349` | `def _inject_agent_files(self, root)` |
| `_inject_readme_link` | method | `readmenator/_app.py:341` | `def _inject_readme_link(self, root)` |
| `_live_renderer` | method | `readmenator/_app.py:1110` | `def _live_renderer(self)` |
| `_log_summary` | method | `readmenator/_app.py:369` | `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)` |
| `_maybe_export_forcegraph` | method | `readmenator/_app.py:1266` | `def _maybe_export_forcegraph(self, root, nodes, edges, resolved_edges, analysis, layers, findings)` |
| `_maybe_export_video` | method | `readmenator/_app.py:1227` | `def _maybe_export_video(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2...` |
| `_maybe_publish_github_wiki` | method | `readmenator/_app.py:283` | `def _maybe_publish_github_wiki(self, root)` |
| `_maybe_refresh_pages` | method | `readmenator/_app.py:265` | `def _maybe_refresh_pages(self, root)` |
| `_maybe_write_graphrag` | method | `readmenator/_app.py:1297` | `def _maybe_write_graphrag(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2...` |
| `_maybe_write_memory` | method | `readmenator/_app.py:1339` | `def _maybe_write_memory(self, root, nodes, analysis, analysis_v2, findings, content_map)` |
| `_memory_notes` | method | `readmenator/_app.py:1333` | `def _memory_notes(self, root)` |
| `_resolve_imports` | method | `readmenator/_app.py:77` | `def _resolve_imports(self, nodes, edges, target_dir)` |
| `_scan` | method | `readmenator/_app.py:59` | `def _scan(self, target_dir)` |
| `_scan_for_cache` | method | `readmenator/_app.py:529` | `def _scan_for_cache(self, root, cache)` |
| `_scan_with_content` | method | `readmenator/_app.py:67` | `def _scan_with_content(self, target_dir)` |
| `_site_stats` | method | `readmenator/_app.py:1098` | `def _site_stats(nodes, edges, analysis)` |
| `_write_bundlegraph` | method | `readmenator/_app.py:727` | `def _write_bundlegraph(self, dest, force_payload, home_href, explorer_href)` |
| `_write_forcegraph` | method | `readmenator/_app.py:680` | `def _write_forcegraph(self, dest, nodes, edges, resolved, analysis, layers, findings, home_href)` |
| `_write_sidecar_outputs` | method | `readmenator/_app.py:315` | `def _write_sidecar_outputs(self, root, findings, analysis_v2)` |
| `analytics` | method | `readmenator/_app.py:891` | `def analytics(self, target_dir)` |
| `analyze` | method | `readmenator/_app.py:615` | `def analyze(self, target_dir)` |
| `audit` | method | `readmenator/_app.py:1468` | `def audit(self, target_dir)` |
| `audit_deep` | method | `readmenator/_app.py:1475` | `def audit_deep(self, target_dir)` |
| `audit_provenance` | method | `readmenator/_app.py:934` | `def audit_provenance(self, target_dir)` |
| `build_graphrag` | method | `readmenator/_app.py:1414` | `def build_graphrag(self, target_dir)` |
| `check_freshness` | method | `readmenator/_app.py:238` | `def check_freshness(self, target_dir)` |
| `detect_layers` | method | `readmenator/_app.py:1515` | `def detect_layers(self, target_dir)` |
| `explain` | method | `readmenator/_app.py:552` | `def explain(self, target_dir, symbol_name)` |
| `explorer_state` | method | `readmenator/_app.py:862` | `def explorer_state(self, target_dir)` |
| `export` | method | `readmenator/_app.py:658` | `def export(self, target_dir)` |
| `export_bundlegraph` | method | `readmenator/_app.py:836` | `def export_bundlegraph(self, target_dir, output_path)` |
| `export_cypher` | method | `readmenator/_app.py:982` | `def export_cypher(self, target_dir, output_path)` |
| `export_diagram` | method | `readmenator/_app.py:1120` | `def export_diagram(self, target_dir, kind, output_path, full)` |
| `export_diagrams` | method | `readmenator/_app.py:1054` | `def export_diagrams(self, target_dir, output_dir, full)` |
| `export_forcegraph` | method | `readmenator/_app.py:817` | `def export_forcegraph(self, target_dir, output_path)` |
| `export_graphml` | method | `readmenator/_app.py:971` | `def export_graphml(self, target_dir, output_path)` |
| `export_html` | method | `readmenator/_app.py:636` | `def export_html(self, target_dir, output_path)` |
| `export_json` | method | `readmenator/_app.py:619` | `def export_json(self, target_dir, output_path)` |
| `export_obsidian` | method | `readmenator/_app.py:998` | `def export_obsidian(self, target_dir, output_dir)` |
| `export_pages` | method | `readmenator/_app.py:1159` | `def export_pages(self, target_dir, output_dir, full)` |
| `export_rules` | method | `readmenator/_app.py:1505` | `def export_rules(self, target_dir, output_dir)` |
| `export_sarif` | method | `readmenator/_app.py:1495` | `def export_sarif(self, target_dir, output_path)` |
| `export_svg` | method | `readmenator/_app.py:647` | `def export_svg(self, target_dir, output_path)` |
| `export_video` | method | `readmenator/_app.py:1203` | `def export_video(self, target_dir, output_path)` |
| `export_wiki` | method | `readmenator/_app.py:1013` | `def export_wiki(self, target_dir, output_dir)` |
| `find_path` | method | `readmenator/_app.py:564` | `def find_path(self, target_dir, symbol_a, symbol_b)` |
| `generate_cursorrules` | method | `readmenator/_app.py:1548` | `def generate_cursorrules(self, target_dir)` |
| `generate_uml_code` | method | `readmenator/_app.py:357` | `def generate_uml_code(self, target_dir, language, output_path)` |
| `graphrag_search` | method | `readmenator/_app.py:1437` | `def graphrag_search(self, target_dir, query, mode, budget_tokens)` |
| `install_skills` | method | `readmenator/_app.py:1402` | `def install_skills(self, target_dir, target)` |
| `lint` | method | `readmenator/_app.py:1525` | `def lint(self, target_dir)` |
| `lint_wiki` | method | `readmenator/_app.py:1036` | `def lint_wiki(self, target_dir)` |
| `memory` | method | `readmenator/_app.py:1365` | `def memory(self, target_dir)` |
| `near` | method | `readmenator/_app.py:920` | `def near(self, target_dir, query, top_k)` |
| `on_change` | method | `readmenator/_app.py:1462` | `def on_change()` |
| `publish_github_wiki` | method | `readmenator/_app.py:301` | `def publish_github_wiki(self, target_dir, dry_run)` |
| `query` | method | `readmenator/_app.py:547` | `def query(self, target_dir, question)` |
| `rank_query` | method | `readmenator/_app.py:582` | `def rank_query(self, target_dir, query, top_n)` |
| `readmenatorApplication` | class | `readmenator/_app.py:49` | `class readmenatorApplication` |
| `rebuild` | method | `readmenator/_app.py:612` | `def rebuild(self, target_dir, run_security)` |
| `refactor_monolith` | method | `readmenator/_app.py:1563` | `def refactor_monolith(self, target_dir)` |
| `remember` | method | `readmenator/_app.py:1388` | `def remember(self, target_dir, note, kind)` |
| `run` | method | `readmenator/_app.py:96` | `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)` |
| `scan_texts` | method | `readmenator/_app.py:908` | `def scan_texts(self, target_dir)` |
| `serve_explorer` | method | `readmenator/_app.py:878` | `def serve_explorer(self, target_dir, open_browser)` |
| `strip_dead_code` | method | `readmenator/_app.py:1538` | `def strip_dead_code(self, target_dir)` |
| `summary` | method | `readmenator/_app.py:577` | `def summary(self, target_dir)` |
| `update` | method | `readmenator/_app.py:424` | `def update(self, target_dir, run_security)` |
| `validate_yaralite` | method | `readmenator/_app.py:957` | `def validate_yaralite(self, target_dir)` |
| `watch` | method | `readmenator/_app.py:1458` | `def watch(self, target_dir)` |
| `BundleGraphRenderer` | class | `readmenator/_bundlegraph.py:48` | `class BundleGraphRenderer` |
| `__init__` | method | `readmenator/_bundlegraph.py:51` | `def __init__(self, config)` |
| `_json_script` | function | `readmenator/_bundlegraph.py:36` | `def _json_script(value)` |
| `build_payload` | method | `readmenator/_bundlegraph.py:60` | `def build_payload(self, force_payload)` |
| `page_settings` | method | `readmenator/_bundlegraph.py:147` | `def page_settings(self, force_payload, explorer_href)` |
| `render` | method | `readmenator/_bundlegraph.py:186` | `def render(self, force_payload, title, home_href, explorer_href)` |
| `thumbnail_svg` | method | `readmenator/_bundlegraph.py:248` | `def thumbnail_svg(self, force_payload)` |
| `write` | method | `readmenator/_bundlegraph.py:222` | `def write(self, output_path, force_payload, title, home_href, explorer_href)` |
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
| `ConceptExtractor` | class | `readmenator/_concepts.py:38` | `class ConceptExtractor` |
| `__init__` | method | `readmenator/_concepts.py:41` | `def __init__(self, config)` |
| `_build_dialectic` | method | `readmenator/_concepts.py:169` | `def _build_dialectic(self, concepts, relations)` |
| `_build_relations` | method | `readmenator/_concepts.py:130` | `def _build_relations(self, edges, file_to_concepts)` |
| `_tokenize` | method | `readmenator/_concepts.py:115` | `def _tokenize(self, text)` |
| `_tokens_for_node` | method | `readmenator/_concepts.py:101` | `def _tokens_for_node(self, node)` |
| `extract` | method | `readmenator/_concepts.py:47` | `def extract(self, nodes, edges, resolved_edges)` |
| `verb_for_relation` | function | `readmenator/_concepts.py:33` | `def verb_for_relation(relation)` |
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
| `DocsSitePublisher` | class | `readmenator/_diagrams.py:3200` | `class DocsSitePublisher` |
| `InteractiveMapRenderer` | class | `readmenator/_diagrams.py:1520` | `class InteractiveMapRenderer` |
| `MapDelta` | class | `readmenator/_diagrams.py:210` | `class MapDelta` |
| `MapDiagnostic` | class | `readmenator/_diagrams.py:176` | `class MapDiagnostic` |
| `MapEdge` | class | `readmenator/_diagrams.py:121` | `class MapEdge` |
| `MapNode` | class | `readmenator/_diagrams.py:88` | `class MapNode` |
| `MapReceipt` | class | `readmenator/_diagrams.py:193` | `class MapReceipt` |
| `MapView` | class | `readmenator/_diagrams.py:138` | `class MapView` |
| `SystemMap` | class | `readmenator/_diagrams.py:155` | `class SystemMap` |
| `SystemMapBuilder` | class | `readmenator/_diagrams.py:454` | `class SystemMapBuilder` |
| `SystemMapValidator` | class | `readmenator/_diagrams.py:230` | `class SystemMapValidator` |
| `VisNetworkRenderer` | class | `readmenator/_diagrams.py:2226` | `class VisNetworkRenderer` |
| `__init__` | method | `readmenator/_diagrams.py:233` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:483` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:1523` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:2234` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:3217` | `def __init__(self, config)` |
| `_annotate_communities` | method | `readmenator/_diagrams.py:555` | `def _annotate_communities(system_map, analysis)` |
| `_build_architecture` | method | `readmenator/_diagrams.py:1122` | `def _build_architecture(self, nodes, links, layers, findings, analysis, full)` |
| `_build_dataflow` | method | `readmenator/_diagrams.py:1344` | `def _build_dataflow(self, nodes, links, layers, findings, full)` |
| `_build_lifecycle` | method | `readmenator/_diagrams.py:1427` | `def _build_lifecycle(self, nodes, links, layers, findings, full)` |
| `_build_sequence` | method | `readmenator/_diagrams.py:1262` | `def _build_sequence(self, nodes, links, layers, analysis, full)` |
| `_build_workflow` | method | `readmenator/_diagrams.py:1182` | `def _build_workflow(self, nodes, links, layers, findings, full)` |
| `_canvas_for` | method | `readmenator/_diagrams.py:1009` | `def _canvas_for(self, positions, full)` |
| `_canvas_size` | method | `readmenator/_diagrams.py:1531` | `def _canvas_size(self, system_map)` |
| `_cap_lane_scope` | method | `readmenator/_diagrams.py:914` | `def _cap_lane_scope(self, ranked, layer_of)` |
| `_card` | method | `readmenator/_diagrams.py:3909` | `def _card(self, kind, system_map, href_prefix)` |
| `_community_legend` | method | `readmenator/_diagrams.py:2344` | `def _community_legend(self, system_map)` |
| `_doc_group` | method | `readmenator/_diagrams.py:3767` | `def _doc_group(self, name)` |
| `_doc_preview` | method | `readmenator/_diagrams.py:3477` | `def _doc_preview(self, text)` |
| `_doc_title` | method | `readmenator/_diagrams.py:3468` | `def _doc_title(text)` |
| `_docs_section` | method | `readmenator/_diagrams.py:3779` | `def _docs_section(self, doc_entries)` |
| `_edge_path` | method | `readmenator/_diagrams.py:1695` | `def _edge_path(self, x1, y1, x2, y2)` |
| `_edges_svg` | method | `readmenator/_diagrams.py:1779` | `def _edges_svg(self, system_map)` |
| `_effective_canvas` | method | `readmenator/_diagrams.py:241` | `def _effective_canvas(self, system_map)` |
| `_escape` | method | `readmenator/_diagrams.py:1673` | `def _escape(self, value)` |
| `_escape` | method | `readmenator/_diagrams.py:3995` | `def _escape(self, value)` |
| `_escape_markup` | function | `readmenator/_diagrams.py:31` | `def _escape_markup(value)` |
| `_extra_card` | method | `readmenator/_diagrams.py:3950` | `def _extra_card(self, entry)` |
| `_fill_template` | function | `readmenator/_diagrams.py:55` | `def _fill_template(template, values)` |
| `_fitted_gap` | method | `readmenator/_diagrams.py:876` | `def _fitted_gap(self, count, item, gap, total, margin)` |
| `_glyph` | method | `readmenator/_diagrams.py:3891` | `def _glyph(self, kind)` |
| `_href_prefix` | method | `readmenator/_diagrams.py:3861` | `def _href_prefix(self)` |
| `_internal_links` | method | `readmenator/_diagrams.py:751` | `def _internal_links(self, edges, selected, full)` |
| `_is_full` | method | `readmenator/_diagrams.py:500` | `def _is_full(self, full)` |
| `_json_payload` | function | `readmenator/_diagrams.py:43` | `def _json_payload(payload)` |
| `_lane_capacity` | method | `readmenator/_diagrams.py:900` | `def _lane_capacity(self)` |
| `_lanes_that_fit` | method | `readmenator/_diagrams.py:859` | `def _lanes_that_fit(self, lanes)` |
| `_layout_columns` | method | `readmenator/_diagrams.py:811` | `def _layout_columns(self, items, kind, full)` |
| `_layout_sequence` | method | `readmenator/_diagrams.py:938` | `def _layout_sequence(self, ordered, full)` |
| `_make_views` | method | `readmenator/_diagrams.py:1050` | `def _make_views(self, kind, primary, links)` |
| `_meta_for` | method | `readmenator/_diagrams.py:1027` | `def _meta_for(self, kind, placed, links, total, positions, full)` |
| `_nodes_svg` | method | `readmenator/_diagrams.py:1731` | `def _nodes_svg(self, system_map)` |
| `_place` | method | `readmenator/_diagrams.py:989` | `def _place(self, ranked, layer_of, kind, full)` |
| `_prune_stale_docs` | method | `readmenator/_diagrams.py:3513` | `def _prune_stale_docs(docs_root, keep)` |
| `_ranked_file_ids` | method | `readmenator/_diagrams.py:690` | `def _ranked_file_ids(self, nodes, links, analysis)` |
| `_render_poster` | method | `readmenator/_diagrams.py:3430` | `def _render_poster(self, video, site_root)` |
| `_role_color` | function | `readmenator/_diagrams.py:74` | `def _role_color(role, config)` |
| `_role_color` | method | `readmenator/_diagrams.py:1684` | `def _role_color(self, role)` |
| `_role_for` | method | `readmenator/_diagrams.py:656` | `def _role_for(self, group, sensitive)` |
| `_safe_json` | method | `readmenator/_diagrams.py:1662` | `def _safe_json(self, payload)` |
| `_select_primary` | method | `readmenator/_diagrams.py:725` | `def _select_primary(self, nodes, links, analysis, full)` |
| `_sensitive_files` | method | `readmenator/_diagrams.py:673` | `def _sensitive_files(self, findings)` |
| `_sequence_capacity` | method | `readmenator/_diagrams.py:975` | `def _sequence_capacity(self)` |
| `_short_label` | method | `readmenator/_diagrams.py:796` | `def _short_label(self, value)` |
| `_start_here` | method | `readmenator/_diagrams.py:3700` | `def _start_here(self, entries, video_rel)` |
| `_stat_tiles` | method | `readmenator/_diagrams.py:3680` | `def _stat_tiles(self, stats)` |
| `_stats_line` | method | `readmenator/_diagrams.py:3981` | `def _stats_line(self, stats)` |
| `_symbol_records` | method | `readmenator/_diagrams.py:774` | `def _symbol_records(self, node)` |
| `_template` | method | `readmenator/_diagrams.py:1826` | `def _template(self)` |
| `_template` | method | `readmenator/_diagrams.py:2412` | `def _template(self)` |
| `_title_for` | method | `readmenator/_diagrams.py:642` | `def _title_for(self, kind)` |
| `_tooltip` | method | `readmenator/_diagrams.py:2381` | `def _tooltip(self, node)` |
| `_video_section` | method | `readmenator/_diagrams.py:3740` | `def _video_section(self, video_rel, poster_rel)` |
| `build` | method | `readmenator/_diagrams.py:513` | `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)` |
| `build_all` | method | `readmenator/_diagrams.py:572` | `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)` |
| `collect_doc_sources` | method | `readmenator/_diagrams.py:3335` | `def collect_doc_sources(self, project_root)` |
| `compare` | method | `readmenator/_diagrams.py:603` | `def compare(self, base, head)` |
| `description_for` | method | `readmenator/_diagrams.py:3227` | `def description_for(self, kind)` |
| `doc_order` | method | `readmenator/_diagrams.py:3805` | `def doc_order(base)` |
| `order` | method | `readmenator/_diagrams.py:3581` | `def order(entry)` |
| `publish` | method | `readmenator/_diagrams.py:3241` | `def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries, extra_cards)` |
| `publish_assets` | method | `readmenator/_diagrams.py:3361` | `def publish_assets(self, project_root, output_dir)` |
| `render` | method | `readmenator/_diagrams.py:1552` | `def render(self, system_map)` |
| `render` | method | `readmenator/_diagrams.py:2242` | `def render(self, system_map)` |
| `render_index` | method | `readmenator/_diagrams.py:3609` | `def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries, poster_rel, extra_cards)` |
| `render_llms_txt` | method | `readmenator/_diagrams.py:3530` | `def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)` |
| `supported_kinds` | method | `readmenator/_diagrams.py:492` | `def supported_kinds(self)` |
| `validate` | method | `readmenator/_diagrams.py:262` | `def validate(self, system_map)` |
| `write` | method | `readmenator/_diagrams.py:1643` | `def write(self, system_map, output_path)` |
| `write` | method | `readmenator/_diagrams.py:2364` | `def write(self, system_map, output_path)` |
| `DocumentationGenerator` | class | `readmenator/_documentation.py:35` | `class DocumentationGenerator` |
| `__init__` | method | `readmenator/_documentation.py:47` | `def __init__(self, config)` |
| `_apply_context_budget` | method | `readmenator/_documentation.py:183` | `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)` |
| `_build_analytics_section` | method | `readmenator/_documentation.py:672` | `def _build_analytics_section(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2)` |
| `_build_architecture_reference` | method | `readmenator/_documentation.py:1217` | `def _build_architecture_reference(self, nodes, edges)` |
| `_build_change_impact` | method | `readmenator/_documentation.py:1017` | `def _build_change_impact(self, analysis_v2)` |
| `_build_community_analysis` | method | `readmenator/_documentation.py:561` | `def _build_community_analysis(self, analysis, nodes)` |
| `_build_concept_graph` | method | `readmenator/_documentation.py:949` | `def _build_concept_graph(self, analysis_v2)` |
| `_build_cpg_block` | method | `readmenator/_documentation.py:1191` | `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)` |
| `_build_dashboard` | method | `readmenator/_documentation.py:453` | `def _build_dashboard(self, nodes, edges, resolved_edges)` |
| `_build_dataflow_analysis` | method | `readmenator/_documentation.py:918` | `def _build_dataflow_analysis(self, analysis_v2)` |
| `_build_dependency_cycles` | method | `readmenator/_documentation.py:996` | `def _build_dependency_cycles(self, analysis_v2)` |
| `_build_forcegraph_section` | method | `readmenator/_documentation.py:635` | `def _build_forcegraph_section(self, nodes, edges, resolved_edges, analysis, layers, findings)` |
| `_build_god_nodes` | method | `readmenator/_documentation.py:533` | `def _build_god_nodes(self, analysis, ranked)` |
| `_build_hotspots` | method | `readmenator/_documentation.py:880` | `def _build_hotspots(self, analysis_v2, ranked)` |
| `_build_layer_violations` | method | `readmenator/_documentation.py:1042` | `def _build_layer_violations(self, analysis_v2)` |
| `_build_layers` | method | `readmenator/_documentation.py:419` | `def _build_layers(self, layers, nodes)` |
| `_build_mermaid_section` | method | `readmenator/_documentation.py:1142` | `def _build_mermaid_section(self, graph_output, is_truncated)` |
| `_build_orphans` | method | `readmenator/_documentation.py:753` | `def _build_orphans(self, nodes, analysis_v2, ranked)` |
| `_build_query_recipes` | method | `readmenator/_documentation.py:803` | `def _build_query_recipes(self)` |
| `_build_ranked_context` | method | `readmenator/_documentation.py:707` | `def _build_ranked_context(self, ranked)` |
| `_build_security_findings` | method | `readmenator/_documentation.py:1095` | `def _build_security_findings(self, findings)` |
| `_build_suggested_questions` | method | `readmenator/_documentation.py:619` | `def _build_suggested_questions(self, analysis)` |
| `_build_suggested_rules` | method | `readmenator/_documentation.py:1070` | `def _build_suggested_rules(self, analysis_v2)` |
| `_build_surprising_connections` | method | `readmenator/_documentation.py:594` | `def _build_surprising_connections(self, analysis, nodes)` |
| `_build_taint_analysis` | method | `readmenator/_documentation.py:845` | `def _build_taint_analysis(self, analysis_v2)` |
| `_build_toc` | method | `readmenator/_documentation.py:321` | `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)` |
| `_build_uml_diagram` | method | `readmenator/_documentation.py:1165` | `def _build_uml_diagram(self, nodes, edges)` |
| `_get_git_commit` | method | `readmenator/_documentation.py:83` | `def _get_git_commit()` |
| `_ranking_version` | method | `readmenator/_documentation.py:65` | `def _ranking_version(self)` |
| `generate` | method | `readmenator/_documentation.py:93` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)` |
| `Embedder` | class | `readmenator/_embed.py:39` | `class Embedder` |
| `__init__` | method | `readmenator/_embed.py:42` | `def __init__(self, config)` |
| `_jaccard` | function | `readmenator/_embed.py:27` | `def _jaccard(left, right)` |
| `_tokens` | function | `readmenator/_embed.py:22` | `def _tokens(text)` |
| `cluster_jaccard` | method | `readmenator/_embed.py:99` | `def cluster_jaccard(self, corpus, threshold)` |
| `dependencies_available` | method | `readmenator/_embed.py:50` | `def dependencies_available(self)` |
| `encode` | method | `readmenator/_embed.py:58` | `def encode(self, texts)` |
| `find` | method | `readmenator/_embed.py:115` | `def find(item)` |
| `near_jaccard` | method | `readmenator/_embed.py:75` | `def near_jaccard(self, query, corpus, top_k)` |
| `project_jaccard` | method | `readmenator/_embed.py:138` | `def project_jaccard(self, corpus)` |
| `union` | method | `readmenator/_embed.py:122` | `def union(left, right)` |
| `ExclusionEntry` | class | `readmenator/_exclusions.py:19` | `class ExclusionEntry` |
| `ExclusionList` | class | `readmenator/_exclusions.py:44` | `class ExclusionList` |
| `__init__` | method | `readmenator/_exclusions.py:47` | `def __init__(self, config)` |
| `_to_entry` | method | `readmenator/_exclusions.py:146` | `def _to_entry(data)` |
| `_unquote` | method | `readmenator/_exclusions.py:157` | `def _unquote(value)` |
| `entries` | method | `readmenator/_exclusions.py:58` | `def entries(self)` |
| `filter_findings` | method | `readmenator/_exclusions.py:98` | `def filter_findings(self, findings)` |
| `is_excluded` | method | `readmenator/_exclusions.py:86` | `def is_excluded(self, file_path, rule_id)` |
| `load` | method | `readmenator/_exclusions.py:62` | `def load(self, project_root)` |
| `matches` | method | `readmenator/_exclusions.py:27` | `def matches(self, file_path, rule_id)` |
| `parse_exclusions` | method | `readmenator/_exclusions.py:114` | `def parse_exclusions(text)` |
| `_find_item` | function | `readmenator/_explain.py:163` | `def _find_item(node_id, items)` |
| `explain_rank` | function | `readmenator/_explain.py:16` | `def explain_rank(node_id, ranked, category)` |
| `rank_summary` | function | `readmenator/_explain.py:140` | `def rank_summary(ranked, top_n)` |
| `ExplorerState` | class | `readmenator/_explorer.py:23` | `class ExplorerState` |
| `_Handler` | class | `readmenator/_explorer.py:81` | `class _Handler(BaseHTTPRequestHandler)` |
| `__init__` | method | `readmenator/_explorer.py:26` | `def __init__(self, config, nodes, edges, resolved_edges, analysis, findings, layers)` |
| `_serve_html` | method | `readmenator/_explorer.py:105` | `def _serve_html(self)` |
| `_serve_json` | method | `readmenator/_explorer.py:128` | `def _serve_json(self, payload)` |
| `_serve_vendor` | method | `readmenator/_explorer.py:114` | `def _serve_vendor(self)` |
| `build_state` | method | `readmenator/_explorer.py:191` | `def build_state(config, nodes, edges, resolved_edges, analysis, findings, layers)` |
| `do_GET` | method | `readmenator/_explorer.py:88` | `def do_GET(self)` |
| `find_free_port` | method | `readmenator/_explorer.py:139` | `def find_free_port(preferred)` |
| `log_message` | method | `readmenator/_explorer.py:84` | `def log_message(self, fmt)` |
| `samples` | method | `readmenator/_explorer.py:61` | `def samples(self)` |
| `serve` | method | `readmenator/_explorer.py:158` | `def serve(state, host, port, open_browser)` |
| `write_static` | method | `readmenator/_explorer.py:217` | `def write_static(state, output_dir, filename)` |
| `GraphExporter` | class | `readmenator/_exporter.py:28` | `class GraphExporter` |
| `__init__` | method | `readmenator/_exporter.py:36` | `def __init__(self, config)` |
| `_community_color_map` | method | `readmenator/_exporter.py:272` | `def _community_color_map(self, analysis)` |
| `_layout_spring` | method | `readmenator/_exporter.py:615` | `def _layout_spring(self, nodes, edges, node_map)` |
| `_lighten` | method | `readmenator/_exporter.py:290` | `def _lighten(hex_color)` |
| `_project` | method | `readmenator/_exporter.py:544` | `def _project(pos)` |
| `_render_html` | method | `readmenator/_exporter.py:298` | `def _render_html(self, vis_nodes, vis_edges, analysis, findings)` |
| `_render_truncated_svg` | method | `readmenator/_exporter.py:600` | `def _render_truncated_svg(self, total_nodes)` |
| `_sev_span` | method | `readmenator/_exporter.py:370` | `def _sev_span(sev, count)` |
| `to_cypher` | method | `readmenator/_exporter.py:773` | `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` |
| `to_forcegraph` | method | `readmenator/_exporter.py:1020` | `def to_forcegraph(self, nodes, edges, resolved_edges, analysis, layers, findings, analytics)` |
| `to_graphml` | method | `readmenator/_exporter.py:696` | `def to_graphml(self, nodes, edges, resolved_edges, analysis)` |
| `to_html` | method | `readmenator/_exporter.py:183` | `def to_html(self, nodes, edges, resolved_edges, analysis, findings)` |
| `to_json` | method | `readmenator/_exporter.py:44` | `def to_json(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` |
| `to_obsidian` | method | `readmenator/_exporter.py:895` | `def to_obsidian(self, nodes, edges, output_dir, analysis, concept_graph)` |
| `to_svg` | method | `readmenator/_exporter.py:482` | `def to_svg(self, nodes, edges, resolved_edges, analysis)` |
| `ForceGraphRenderer` | class | `readmenator/_forcegraph.py:75` | `class ForceGraphRenderer` |
| `__init__` | method | `readmenator/_forcegraph.py:78` | `def __init__(self, config)` |
| `_family_color` | method | `readmenator/_forcegraph.py:429` | `def _family_color(self, name)` |
| `_file_color` | method | `readmenator/_forcegraph.py:551` | `def _file_color(self, node_id, family, layer, palette)` |
| `_node_doc` | method | `readmenator/_forcegraph.py:532` | `def _node_doc(self, node)` |
| `_symbol_list` | method | `readmenator/_forcegraph.py:538` | `def _symbol_list(self, node)` |
| `add_node` | method | `readmenator/_forcegraph.py:195` | `def add_node(node_id, label, node_type)` |
| `build_payload` | method | `readmenator/_forcegraph.py:107` | `def build_payload(self, nodes, edges, resolved_edges, analysis, layers, findings)` |
| `copy_vendor` | method | `readmenator/_forcegraph.py:513` | `def copy_vendor(self, dest_dir)` |
| `edge_palette` | method | `readmenator/_forcegraph.py:90` | `def edge_palette(self)` |
| `family_color` | method | `readmenator/_forcegraph.py:418` | `def family_color(self, name)` |
| `family_color_from_name` | function | `readmenator/_forcegraph.py:34` | `def family_color_from_name(name, sat_base, sat_span, light_base, light_span)` |
| `file_of` | method | `readmenator/_forcegraph.py:141` | `def file_of(edge_id)` |
| `group_colors` | method | `readmenator/_forcegraph.py:326` | `def group_colors(self, payload)` |
| `node_palette` | method | `readmenator/_forcegraph.py:86` | `def node_palette(self)` |
| `node_value` | function | `readmenator/_forcegraph.py:62` | `def node_value(symbols, degree)` |
| `page_settings` | method | `readmenator/_forcegraph.py:349` | `def page_settings(self, payload)` |
| `render` | method | `readmenator/_forcegraph.py:283` | `def render(self, payload, analytics, title, home_href)` |
| `thumbnail_svg` | method | `readmenator/_forcegraph.py:446` | `def thumbnail_svg(self, payload)` |
| `vendor_href` | method | `readmenator/_forcegraph.py:102` | `def vendor_href(self)` |
| `vendor_source` | method | `readmenator/_forcegraph.py:94` | `def vendor_source(self)` |
| `write` | method | `readmenator/_forcegraph.py:486` | `def write(self, output_path, payload, analytics, title, home_href)` |
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
| `BundleLayout` | class | `readmenator/_graphlayout.py:278` | `class BundleLayout` |
| `ForceAtlas2Settings` | class | `readmenator/_graphlayout.py:37` | `class ForceAtlas2Settings` |
| `SphereBundleLayout` | class | `readmenator/_graphlayout.py:458` | `class SphereBundleLayout` |
| `_bspline` | method | `readmenator/_graphlayout.py:298` | `def _bspline(control, samples)` |
| `_bundle_curves` | method | `readmenator/_graphlayout.py:321` | `def _bundle_curves(leaves, member_group, hub, root, edges, beta, samples)` |
| `_fa2_numpy` | method | `readmenator/_graphlayout.py:116` | `def _fa2_numpy(n, pairs, start, cfg)` |
| `_fa2_python` | method | `readmenator/_graphlayout.py:163` | `def _fa2_python(n, pairs, start, cfg)` |
| `_initial_positions` | method | `readmenator/_graphlayout.py:63` | `def _initial_positions(n, seed, dims)` |
| `_snapshot_steps` | method | `readmenator/_graphlayout.py:110` | `def _snapshot_steps(iterations, snapshots)` |
| `_split_caps` | method | `readmenator/_graphlayout.py:476` | `def _split_caps(labels, sizes, points, lattice, out)` |
| `_unit` | method | `readmenator/_graphlayout.py:449` | `def _unit(v)` |
| `fibonacci_sphere` | method | `readmenator/_graphlayout.py:426` | `def fibonacci_sphere(count)` |
| `fit_frames` | method | `readmenator/_graphlayout.py:218` | `def fit_frames(frames, box, margin, trim)` |
| `forceatlas2_frames` | method | `readmenator/_graphlayout.py:70` | `def forceatlas2_frames(ids, edges, settings)` |
| `hierarchical_edge_bundling` | method | `readmenator/_graphlayout.py:371` | `def hierarchical_edge_bundling(groups, edges, center, radius, beta, samples, group_gap, inner_ratio)` |
| `interpolate_frames` | method | `readmenator/_graphlayout.py:263` | `def interpolate_frames(frames, t)` |
| `normalize_cloud` | method | `readmenator/_graphlayout.py:571` | `def normalize_cloud(points, quantile, max_radius)` |
| `spherical_edge_bundling` | method | `readmenator/_graphlayout.py:513` | `def spherical_edge_bundling(groups, edges, radius, beta, samples, inner_ratio)` |
| `Bm25Index` | class | `readmenator/_graphrag.py:267` | `class Bm25Index` |
| `GraphRagBuilder` | class | `readmenator/_graphrag.py:345` | `class GraphRagBuilder` |
| `GraphRagIndex` | class | `readmenator/_graphrag.py:169` | `class GraphRagIndex` |

Next: [SYMBOLS_p2.md](SYMBOLS_p2.md)
