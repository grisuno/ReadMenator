# Symbols (page 1 of 7)
Pages: [SYMBOLS.md](SYMBOLS.md), [SYMBOLS_p2.md](SYMBOLS_p2.md), [SYMBOLS_p3.md](SYMBOLS_p3.md), [SYMBOLS_p4.md](SYMBOLS_p4.md), [SYMBOLS_p5.md](SYMBOLS_p5.md), [SYMBOLS_p6.md](SYMBOLS_p6.md), [SYMBOLS_p7.md](SYMBOLS_p7.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `ensure_pkg` | function | `deploy.sh:22` | `` |
| `_run_tests` | function | `readmenator/__main__.py:137` | `def _run_tests()` |
| `build_parser` | function | `readmenator/__main__.py:18` | `def build_parser()` |
| `main` | function | `readmenator/__main__.py:152` | `def main()` |
| `AgentInjector` | class | `readmenator/_agent_injector.py:142` | `class AgentInjector` |
| `__init__` | method | `readmenator/_agent_injector.py:153` | `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir, agent_heading...` |
| `_build_injection` | method | `readmenator/_agent_injector.py:295` | `def _build_injection(self, fmt)` |
| `_build_mdc_injection` | method | `readmenator/_agent_injector.py:318` | `def _build_mdc_injection(self)` |
| `_extract_current_injection` | method | `readmenator/_agent_injector.py:260` | `def _extract_current_injection(content)` |
| `_find_agent_files` | method | `readmenator/_agent_injector.py:208` | `def _find_agent_files(self, root)` |
| `_inject_single` | method | `readmenator/_agent_injector.py:222` | `def _inject_single(self, path)` |
| `_prepend_mdc_frontmatter` | method | `readmenator/_agent_injector.py:323` | `def _prepend_mdc_frontmatter(content, injection)` |
| `_remove_old_injection` | method | `readmenator/_agent_injector.py:269` | `def _remove_old_injection(content)` |
| `_remove_single` | method | `readmenator/_agent_injector.py:279` | `def _remove_single(self, path)` |
| `ensure_readmenator_installed` | function | `readmenator/_agent_injector.py:120` | `def ensure_readmenator_installed()` |
| `find_agent_files` | method | `readmenator/_agent_injector.py:204` | `def find_agent_files(self, project_root)` |
| `inject` | method | `readmenator/_agent_injector.py:173` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_agent_injector.py:191` | `def remove(self, project_root)` |
| `AgentOutputGenerator` | class | `readmenator/_agent_output.py:71` | `class AgentOutputGenerator` |
| `__init__` | method | `readmenator/_agent_output.py:78` | `def __init__(self, config)` |
| `_build_api` | method | `readmenator/_agent_output.py:329` | `def _build_api(self, nodes, resolved_map, imported_by, layers)` |
| `_build_architecture` | method | `readmenator/_agent_output.py:206` | `def _build_architecture(self, edges, resolved_edges, nodes)` |
| `_build_concepts` | method | `readmenator/_agent_output.py:631` | `def _build_concepts(self, analysis_v2)` |
| `_build_gotchas` | method | `readmenator/_agent_output.py:509` | `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` |
| `_build_imported_by_map` | method | `readmenator/_agent_output.py:891` | `def _build_imported_by_map(resolved_edges)` |
| `_build_index` | method | `readmenator/_agent_output.py:174` | `def _build_index(self, nodes, subsystems, imported_by)` |
| `_build_manifest` | method | `readmenator/_agent_output.py:387` | `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root, subsystems, layers, out_dir)` |
| `_build_resolved_map` | method | `readmenator/_agent_output.py:881` | `def _build_resolved_map(resolved_edges)` |
| `_build_security` | method | `readmenator/_agent_output.py:258` | `def _build_security(self, findings, nodes)` |
| `_build_subsystem_content` | method | `readmenator/_agent_output.py:693` | `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)` |
| `_build_symbols` | method | `readmenator/_agent_output.py:487` | `def _build_symbols(self, nodes)` |
| `_chunk_unit` | method | `readmenator/_agent_output.py:922` | `def _chunk_unit(unit, budget)` |
| `_closed_loop` | method | `readmenator/_agent_output.py:502` | `def _closed_loop(cycle)` |
| `_deps_by_source` | method | `readmenator/_agent_output.py:871` | `def _deps_by_source(resolved_map)` |
| `_enclosing_symbol` | method | `readmenator/_agent_output.py:294` | `def _enclosing_symbol(symbols, line)` |
| `_entrypoints` | method | `readmenator/_agent_output.py:461` | `def _entrypoints(self, nodes, layers)` |
| `_infer_subsystems` | method | `readmenator/_agent_output.py:139` | `def _infer_subsystems(self, nodes)` |
| `_inventory` | method | `readmenator/_agent_output.py:472` | `def _inventory(self, out_dir)` |
| `_is_public` | method | `readmenator/_agent_output.py:304` | `def _is_public(self, sym)` |
| `_page_name` | method | `readmenator/_agent_output.py:901` | `def _page_name(filename, page)` |
| `_paginate` | method | `readmenator/_agent_output.py:939` | `def _paginate(self, filename, content)` |
| `_prune_owned` | method | `readmenator/_agent_output.py:988` | `def _prune_owned(out_dir)` |
| `_qualified_names` | method | `readmenator/_agent_output.py:311` | `def _qualified_names(symbols)` |
| `_safe_name` | method | `readmenator/_agent_output.py:671` | `def _safe_name(name)` |
| `_split_units` | method | `readmenator/_agent_output.py:909` | `def _split_units(body, is_table)` |
| `_write` | method | `readmenator/_agent_output.py:995` | `def _write(path, content)` |
| `_write_paged` | method | `readmenator/_agent_output.py:978` | `def _write_paged(self, out_dir, filename, content)` |
| `_write_recipes` | method | `readmenator/_agent_output.py:743` | `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` |
| `_write_subsystem_files` | method | `readmenator/_agent_output.py:678` | `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)` |
| `generate` | method | `readmenator/_agent_output.py:82` | `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` |
| `keep` | function | `readmenator/_agent_output.py:528` | `def keep(file_id)` |
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
| `ApiEntity` | class | `readmenator/_apidocs.py:98` | `class ApiEntity` |
| `ApiParam` | class | `readmenator/_apidocs.py:76` | `class ApiParam` |
| `ApiReference` | class | `readmenator/_apidocs.py:204` | `class ApiReference` |
| `ApiReferenceBuilder` | class | `readmenator/_apidocs.py:772` | `class ApiReferenceBuilder` |
| `DocWarning` | class | `readmenator/_apidocs.py:180` | `class DocWarning` |
| `_PythonExtractor` | class | `readmenator/_apidocs.py:254` | `class _PythonExtractor` |
| `__init__` | method | `readmenator/_apidocs.py:257` | `def __init__(self, file_id, language, include_private)` |
| `__init__` | method | `readmenator/_apidocs.py:775` | `def __init__(self, config)` |
| `_body_facts` | method | `readmenator/_apidocs.py:432` | `def _body_facts(node)` |
| `_class` | method | `readmenator/_apidocs.py:344` | `def _class(self, node, parent_uid, prefix)` |
| `_coverage` | method | `readmenator/_apidocs.py:1317` | `def _coverage(reference)` |
| `_data` | method | `readmenator/_apidocs.py:513` | `def _data(self, stmt, body, pos, parent_uid, prefix, in_class)` |
| `_extract_file` | method | `readmenator/_apidocs.py:881` | `def _extract_file(self, node, content)` |
| `_extract_generic` | method | `readmenator/_apidocs.py:894` | `def _extract_generic(self, node, content)` |
| `_function` | method | `readmenator/_apidocs.py:455` | `def _function(self, node, parent_uid, prefix, in_class)` |
| `_generic_bases` | method | `readmenator/_apidocs.py:1020` | `def _generic_bases(signature, name)` |
| `_generic_visibility` | method | `readmenator/_apidocs.py:994` | `def _generic_visibility(name, decl, language, parent)` |
| `_indent_end` | function | `readmenator/_apidocs.py:620` | `def _indent_end(lines, start)` |
| `_inherit_docs` | method | `readmenator/_apidocs.py:1082` | `def _inherit_docs(reference)` |
| `_is_include_guard` | method | `readmenator/_apidocs.py:987` | `def _is_include_guard(name, kind, doc)` |
| `_is_test_path` | method | `readmenator/_apidocs.py:783` | `def _is_test_path(self, file_id)` |
| `_is_vendored` | method | `readmenator/_apidocs.py:792` | `def _is_vendored(self, file_id)` |
| `_keep` | method | `readmenator/_apidocs.py:317` | `def _keep(self, name, visibility, documented)` |
| `_link_calls` | method | `readmenator/_apidocs.py:1122` | `def _link_calls(self, reference, nodes, edges, resolved_edges, contents)` |
| `_link_inheritance` | method | `readmenator/_apidocs.py:1049` | `def _link_inheritance(self, reference, edges)` |
| `_lint` | method | `readmenator/_apidocs.py:1259` | `def _lint(self, reference)` |
| `_matching_close` | function | `readmenator/_apidocs.py:564` | `def _matching_close(lines, start, scan_limit)` |
| `_module_entity` | method | `readmenator/_apidocs.py:873` | `def _module_entity(self, node, doc_text)` |
| `_owner_chain` | method | `readmenator/_apidocs.py:1216` | `def _owner_chain(reference, entity)` |
| `_param_span` | function | `readmenator/_apidocs.py:668` | `def _param_span(signature, name)` |
| `_params` | method | `readmenator/_apidocs.py:391` | `def _params(self, args, drop_receiver)` |
| `_read_all` | method | `readmenator/_apidocs.py:286` | `def _read_all(tree)` |
| `_receiver_plausible` | method | `readmenator/_apidocs.py:1229` | `def _receiver_plausible(self, reference, receiver, caller, callee, confidence)` |
| `_render_params` | method | `readmenator/_apidocs.py:410` | `def _render_params(params, args, receiver)` |
| `_split_top_level` | function | `readmenator/_apidocs.py:639` | `def _split_top_level(text, sep)` |
| `_type_index` | method | `readmenator/_apidocs.py:1040` | `def _type_index(reference)` |
| `_unparse` | function | `readmenator/_apidocs.py:244` | `def _unparse(node)` |
| `_visibility` | method | `readmenator/_apidocs.py:305` | `def _visibility(self, name, parent_uid)` |
| `_walk_body` | method | `readmenator/_apidocs.py:325` | `def _walk_body(self, body, parent_uid, prefix)` |
| `build` | method | `readmenator/_apidocs.py:796` | `def build(self, nodes, edges, resolved_edges, content_map)` |
| `children` | method | `readmenator/_apidocs.py:221` | `def children(self, uid, kinds)` |
| `counts` | function | `readmenator/_apidocs.py:1320` | `def counts(items)` |
| `extract` | method | `readmenator/_apidocs.py:272` | `def extract(self, content)` |
| `innermost` | function | `readmenator/_apidocs.py:1154` | `def innermost(file_id, line, name)` |
| `is_documented` | method | `readmenator/_apidocs.py:156` | `def is_documented(self)` |
| `is_vendored_path` | function | `readmenator/_apidocs.py:759` | `def is_vendored_path(file_id, config)` |
| `parse_signature_params` | function | `readmenator/_apidocs.py:685` | `def parse_signature_params(signature, name, language)` |
| `target_entity` | function | `readmenator/_apidocs.py:1166` | `def target_entity(file_id, line, name)` |
| `to_dict` | method | `readmenator/_apidocs.py:91` | `def to_dict(self)` |
| `to_dict` | method | `readmenator/_apidocs.py:160` | `def to_dict(self)` |
| `to_dict` | method | `readmenator/_apidocs.py:197` | `def to_dict(self)` |
| `to_dict` | method | `readmenator/_apidocs.py:232` | `def to_dict(self, schema_version)` |
| `_payload` | function | `readmenator/_apidocs_page.py:29` | `def _payload(reference, project_name, config)` |
| `render_api_site` | function | `readmenator/_apidocs_page.py:57` | `def render_api_site(reference, project_name, config, flow_graphs)` |
| `ApiDocsWriter` | class | `readmenator/_apidocs_render.py:823` | `class ApiDocsWriter` |
| `ApiLinker` | class | `readmenator/_apidocs_render.py:190` | `class ApiLinker` |
| `ApiMarkdownRenderer` | class | `readmenator/_apidocs_render.py:308` | `class ApiMarkdownRenderer` |
| `__init__` | method | `readmenator/_apidocs_render.py:193` | `def __init__(self, reference)` |
| `__init__` | method | `readmenator/_apidocs_render.py:311` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_apidocs_render.py:826` | `def __init__(self, config)` |
| `_call_graph` | method | `readmenator/_apidocs_render.py:791` | `def _call_graph(self, reference, uid)` |
| `_call_refs` | method | `readmenator/_apidocs_render.py:736` | `def _call_refs(self, linker, entity, module_uid)` |
| `_cell` | function | `readmenator/_apidocs_render.py:176` | `def _cell(text)` |
| `_class_diagram` | method | `readmenator/_apidocs_render.py:758` | `def _class_diagram(self, reference, uid)` |
| `_coverage` | method | `readmenator/_apidocs_render.py:491` | `def _coverage(self, reference, linker)` |
| `_descendants` | method | `readmenator/_apidocs_render.py:415` | `def _descendants(reference, uid)` |
| `_doc_block` | method | `readmenator/_apidocs_render.py:659` | `def _doc_block(self, doc, linker, module_uid, entity)` |
| `_entity` | method | `readmenator/_apidocs_render.py:589` | `def _entity(self, reference, linker, entity, module_uid, fence, level)` |
| `_genindex` | method | `readmenator/_apidocs_render.py:464` | `def _genindex(self, reference, linker)` |
| `_hierarchy` | method | `readmenator/_apidocs_render.py:427` | `def _hierarchy(self, reference, linker)` |
| `_index` | method | `readmenator/_apidocs_render.py:360` | `def _index(self, reference, linker, project_name)` |
| `_inline_code` | function | `readmenator/_apidocs_render.py:181` | `def _inline_code(text)` |
| `_jsonl_line` | function | `readmenator/_apidocs_render.py:91` | `def _jsonl_line(record)` |
| `_merged_params` | method | `readmenator/_apidocs_render.py:712` | `def _merged_params(entity, doc)` |
| `_mermaid_id` | method | `readmenator/_apidocs_render.py:749` | `def _mermaid_id(uid)` |
| `_mermaid_label` | method | `readmenator/_apidocs_render.py:754` | `def _mermaid_label(text)` |
| `_module` | method | `readmenator/_apidocs_render.py:549` | `def _module(self, reference, linker, uid)` |
| `_module_link` | method | `readmenator/_apidocs_render.py:341` | `def _module_link(self, linker, entity)` |
| `_prune_jsonl` | method | `readmenator/_apidocs_render.py:913` | `def _prune_jsonl(self, out_dir, pages)` |
| `_replace` | method | `readmenator/_apidocs_render.py:292` | `def _replace(self, match, from_module)` |
| `_source_link` | method | `readmenator/_apidocs_render.py:541` | `def _source_link(self, entity)` |
| `_summary` | method | `readmenator/_apidocs_render.py:351` | `def _summary(self, entity)` |
| `_top_link` | method | `readmenator/_apidocs_render.py:346` | `def _top_link(self, linker, entity, label)` |
| `anchor_slug` | function | `readmenator/_apidocs_render.py:171` | `def anchor_slug(qualname)` |
| `autolink` | method | `readmenator/_apidocs_render.py:272` | `def autolink(self, text, from_module)` |
| `href` | method | `readmenator/_apidocs_render.py:251` | `def href(self, entity, from_module)` |
| `jsonl_index_path` | function | `readmenator/_apidocs_render.py:81` | `def jsonl_index_path(config)` |
| `jsonl_pages` | function | `readmenator/_apidocs_render.py:96` | `def jsonl_pages(reference, config)` |
| `jsonl_warnings_path` | function | `readmenator/_apidocs_render.py:86` | `def jsonl_warnings_path(config)` |
| `link` | method | `readmenator/_apidocs_render.py:260` | `def link(self, entity, from_module, label)` |
| `link_uid` | method | `readmenator/_apidocs_render.py:265` | `def link_uid(self, uid, from_module)` |
| `module_display_name` | function | `readmenator/_apidocs_render.py:64` | `def module_display_name(entity)` |
| `module_of` | method | `readmenator/_apidocs_render.py:210` | `def module_of(self, entity)` |
| `page_slug` | function | `readmenator/_apidocs_render.py:75` | `def page_slug(module_uid)` |
| `read_api_jsonl` | function | `readmenator/_apidocs_render.py:143` | `def read_api_jsonl(api_dir, config)` |
| `render` | method | `readmenator/_apidocs_render.py:319` | `def render(self, reference, project_name)` |
| `resolve` | method | `readmenator/_apidocs_render.py:214` | `def resolve(self, name, context_file)` |
| `walk` | function | `readmenator/_apidocs_render.py:438` | `def walk(entity, depth)` |
| `write` | method | `readmenator/_apidocs_render.py:835` | `def write(self, reference, project_root, project_name, architecture_markdown, flow_graphs)` |
| `__init__` | method | `readmenator/_app.py:55` | `def __init__(self, config)` |
| `_apply_project_config` | method | `readmenator/_app.py:101` | `def _apply_project_config(self, target_dir)` |
| `_architecture_markdown` | method | `readmenator/_app.py:1121` | `def _architecture_markdown(self, nodes, edges, resolved_edges, content_map, analysis, layers)` |
| `_explorer_cards` | method | `readmenator/_app.py:868` | `def _explorer_cards(self, dest, href, home_href, nodes, edges, resolved, analysis, layers, findings, content_map...` |
| `_flow_graphs` | method | `readmenator/_app.py:1140` | `def _flow_graphs(self, nodes, edges, resolved_edges, content_map, analysis, layers)` |
| `_forcegraph_dest` | method | `readmenator/_app.py:759` | `def _forcegraph_dest(self, target_dir, output_path)` |
| `_inject_agent_files` | method | `readmenator/_app.py:432` | `def _inject_agent_files(self, root)` |
| `_inject_readme_link` | method | `readmenator/_app.py:424` | `def _inject_readme_link(self, root)` |
| `_live_renderer` | method | `readmenator/_app.py:1501` | `def _live_renderer(self)` |
| `_log_summary` | method | `readmenator/_app.py:452` | `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)` |
| `_maybe_export_forcegraph` | method | `readmenator/_app.py:1721` | `def _maybe_export_forcegraph(self, root, nodes, edges, resolved_edges, analysis, layers, findings, content_map)` |
| `_maybe_export_video` | method | `readmenator/_app.py:1619` | `def _maybe_export_video(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2...` |
| `_maybe_publish_github_wiki` | method | `readmenator/_app.py:349` | `def _maybe_publish_github_wiki(self, root)` |
| `_maybe_refresh_pages` | method | `readmenator/_app.py:331` | `def _maybe_refresh_pages(self, root)` |
| `_maybe_write_apidocs` | method | `readmenator/_app.py:1090` | `def _maybe_write_apidocs(self, root, nodes, edges, resolved_edges, content_map, analysis, layers)` |
| `_maybe_write_graphrag` | method | `readmenator/_app.py:1754` | `def _maybe_write_graphrag(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2...` |
| `_maybe_write_memory` | method | `readmenator/_app.py:1796` | `def _maybe_write_memory(self, root, nodes, analysis, analysis_v2, findings, content_map)` |
| `_memory_notes` | method | `readmenator/_app.py:1790` | `def _memory_notes(self, root)` |
| `_read_contents` | method | `readmenator/_app.py:1658` | `def _read_contents(self, root, nodes)` |
| `_refresh_explorers` | method | `readmenator/_app.py:1682` | `def _refresh_explorers(self, root, nodes, edges, resolved_edges, analysis, layers, findings)` |
| `_resolve_imports` | method | `readmenator/_app.py:82` | `def _resolve_imports(self, nodes, edges, target_dir)` |
| `_scan` | method | `readmenator/_app.py:64` | `def _scan(self, target_dir)` |
| `_scan_for_cache` | method | `readmenator/_app.py:623` | `def _scan_for_cache(self, root, cache)` |
| `_scan_with_content` | method | `readmenator/_app.py:72` | `def _scan_with_content(self, target_dir)` |
| `_site_stats` | method | `readmenator/_app.py:1489` | `def _site_stats(nodes, edges, analysis)` |
| `_write_bundlegraph` | method | `readmenator/_app.py:829` | `def _write_bundlegraph(self, dest, force_payload, home_href, explorer_href)` |
| `_write_components_card` | method | `readmenator/_app.py:940` | `def _write_components_card(self, maps_dir, nodes, edges, resolved, analysis, content_map, project_root, gallery_dir)` |
| `_write_flows_card` | method | `readmenator/_app.py:1155` | `def _write_flows_card(self, maps_dir, nodes, edges, resolved, analysis, layers, content_map)` |
| `_write_folder_readmes` | method | `readmenator/_app.py:409` | `def _write_folder_readmes(self, root)` |
| `_write_forcegraph` | method | `readmenator/_app.py:774` | `def _write_forcegraph(self, dest, nodes, edges, resolved, analysis, layers, findings, home_href, content_map)` |
| `_write_sidecar_outputs` | method | `readmenator/_app.py:383` | `def _write_sidecar_outputs(self, root, findings, analysis_v2)` |
| `_write_viewer_config` | method | `readmenator/_app.py:132` | `def _write_viewer_config(self, root)` |
| `analytics` | method | `readmenator/_app.py:1278` | `def analytics(self, target_dir)` |
| `analyze` | method | `readmenator/_app.py:709` | `def analyze(self, target_dir)` |
| `audit` | method | `readmenator/_app.py:1926` | `def audit(self, target_dir)` |
| `audit_deep` | method | `readmenator/_app.py:1933` | `def audit_deep(self, target_dir)` |
| `audit_provenance` | method | `readmenator/_app.py:1321` | `def audit_provenance(self, target_dir)` |
| `build_api_reference` | method | `readmenator/_app.py:1198` | `def build_api_reference(self, target_dir)` |
| `build_graphrag` | method | `readmenator/_app.py:1871` | `def build_graphrag(self, target_dir)` |
| `check_freshness` | method | `readmenator/_app.py:304` | `def check_freshness(self, target_dir)` |
| `detect_layers` | method | `readmenator/_app.py:1974` | `def detect_layers(self, target_dir)` |
| `explain` | method | `readmenator/_app.py:646` | `def explain(self, target_dir, symbol_name)` |
| `explorer_state` | method | `readmenator/_app.py:1249` | `def explorer_state(self, target_dir)` |
| `export` | method | `readmenator/_app.py:752` | `def export(self, target_dir)` |
| `export_apidocs` | method | `readmenator/_app.py:1210` | `def export_apidocs(self, target_dir)` |
| `export_bundlegraph` | method | `readmenator/_app.py:1036` | `def export_bundlegraph(self, target_dir, output_path)` |
| `export_components` | method | `readmenator/_app.py:1062` | `def export_components(self, target_dir, output_dir)` |
| `export_cypher` | method | `readmenator/_app.py:1369` | `def export_cypher(self, target_dir, output_path)` |
| `export_diagram` | method | `readmenator/_app.py:1511` | `def export_diagram(self, target_dir, kind, output_path, full)` |
| `export_diagrams` | method | `readmenator/_app.py:1442` | `def export_diagrams(self, target_dir, output_dir, full)` |
| `export_flows` | method | `readmenator/_app.py:1232` | `def export_flows(self, target_dir)` |
| `export_forcegraph` | method | `readmenator/_app.py:1017` | `def export_forcegraph(self, target_dir, output_path)` |
| `export_graphml` | method | `readmenator/_app.py:1358` | `def export_graphml(self, target_dir, output_path)` |
| `export_html` | method | `readmenator/_app.py:730` | `def export_html(self, target_dir, output_path)` |
| `export_json` | method | `readmenator/_app.py:713` | `def export_json(self, target_dir, output_path)` |
| `export_obsidian` | method | `readmenator/_app.py:1385` | `def export_obsidian(self, target_dir, output_dir)` |
| `export_pages` | method | `readmenator/_app.py:1550` | `def export_pages(self, target_dir, output_dir, full)` |
| `export_rules` | method | `readmenator/_app.py:1963` | `def export_rules(self, target_dir, output_dir)` |
| `export_sarif` | method | `readmenator/_app.py:1953` | `def export_sarif(self, target_dir, output_path)` |
| `export_svg` | method | `readmenator/_app.py:741` | `def export_svg(self, target_dir, output_path)` |
| `export_video` | method | `readmenator/_app.py:1595` | `def export_video(self, target_dir, output_path)` |
| `export_wiki` | method | `readmenator/_app.py:1400` | `def export_wiki(self, target_dir, output_dir)` |
| `find_path` | method | `readmenator/_app.py:658` | `def find_path(self, target_dir, symbol_a, symbol_b)` |
| `generate_cursorrules` | method | `readmenator/_app.py:2007` | `def generate_cursorrules(self, target_dir)` |
| `generate_uml_code` | method | `readmenator/_app.py:440` | `def generate_uml_code(self, target_dir, language, output_path)` |
| `graphrag_search` | method | `readmenator/_app.py:1895` | `def graphrag_search(self, target_dir, query, mode, budget_tokens)` |
| `install_skills` | method | `readmenator/_app.py:1859` | `def install_skills(self, target_dir, target)` |
| `lint` | method | `readmenator/_app.py:1984` | `def lint(self, target_dir)` |
| `lint_wiki` | method | `readmenator/_app.py:1424` | `def lint_wiki(self, target_dir)` |
| `memory` | method | `readmenator/_app.py:1822` | `def memory(self, target_dir)` |
| `near` | method | `readmenator/_app.py:1307` | `def near(self, target_dir, query, top_k)` |
| `on_change` | function | `readmenator/_app.py:1920` | `def on_change()` |
| `publish_github_wiki` | method | `readmenator/_app.py:367` | `def publish_github_wiki(self, target_dir, dry_run)` |
| `query` | method | `readmenator/_app.py:641` | `def query(self, target_dir, question)` |
| `rank_query` | method | `readmenator/_app.py:676` | `def rank_query(self, target_dir, query, top_n)` |
| `readmenatorApplication` | class | `readmenator/_app.py:54` | `class readmenatorApplication` |
| `rebuild` | method | `readmenator/_app.py:706` | `def rebuild(self, target_dir, run_security)` |
| `refactor_monolith` | method | `readmenator/_app.py:2022` | `def refactor_monolith(self, target_dir)` |
| `remember` | method | `readmenator/_app.py:1845` | `def remember(self, target_dir, note, kind)` |
| `run` | method | `readmenator/_app.py:150` | `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)` |
| `scan_texts` | method | `readmenator/_app.py:1295` | `def scan_texts(self, target_dir)` |
| `serve_explorer` | method | `readmenator/_app.py:1265` | `def serve_explorer(self, target_dir, open_browser)` |
| `strip_dead_code` | method | `readmenator/_app.py:1997` | `def strip_dead_code(self, target_dir)` |
| `summary` | method | `readmenator/_app.py:671` | `def summary(self, target_dir)` |
| `update` | method | `readmenator/_app.py:507` | `def update(self, target_dir, run_security)` |
| `validate_yaralite` | method | `readmenator/_app.py:1344` | `def validate_yaralite(self, target_dir)` |
| `watch` | method | `readmenator/_app.py:1916` | `def watch(self, target_dir)` |
| `BundleGraphRenderer` | class | `readmenator/_bundlegraph.py:51` | `class BundleGraphRenderer` |
| `__init__` | method | `readmenator/_bundlegraph.py:54` | `def __init__(self, config)` |
| `_json_script` | function | `readmenator/_bundlegraph.py:39` | `def _json_script(value)` |
| `build_payload` | method | `readmenator/_bundlegraph.py:63` | `def build_payload(self, force_payload)` |
| `page_settings` | method | `readmenator/_bundlegraph.py:184` | `def page_settings(self, force_payload, explorer_href, live_api)` |
| `render` | method | `readmenator/_bundlegraph.py:228` | `def render(self, force_payload, title, home_href, explorer_href, live_api)` |
| `thumbnail_svg` | method | `readmenator/_bundlegraph.py:299` | `def thumbnail_svg(self, force_payload)` |
| `write` | method | `readmenator/_bundlegraph.py:273` | `def write(self, output_path, force_payload, title, home_href, explorer_href)` |
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
| `source_fingerprint` | function | `readmenator/_cache.py:179` | `def source_fingerprint(project_root, file_ids)` |
| `Category` | class | `readmenator/_category.py:78` | `class Category` |
| `EdgeKind` | class | `readmenator/_category.py:24` | `class EdgeKind(str, Enum)` |
| `Morphism` | class | `readmenator/_category.py:57` | `class Morphism` |
| `TypedGraph` | class | `readmenator/_category.py:181` | `class TypedGraph` |
| `__init__` | method | `readmenator/_category.py:86` | `def __init__(self)` |
| `__init__` | method | `readmenator/_category.py:188` | `def __init__(self, category)` |
| `__str__` | method | `readmenator/_category.py:38` | `def __str__(self)` |
| `_compose_kind` | method | `readmenator/_category.py:157` | `def _compose_kind(a, b)` |
| `_compute_out_weights` | method | `readmenator/_category.py:197` | `def _compute_out_weights(self)` |
| `_infer_edge_kind` | function | `readmenator/_category.py:278` | `def _infer_edge_kind(relation)` |
| `add_morphism` | method | `readmenator/_category.py:95` | `def add_morphism(self, m)` |
| `add_object` | method | `readmenator/_category.py:92` | `def add_object(self, obj_id)` |
| `build_category_from_edges` | function | `readmenator/_category.py:236` | `def build_category_from_edges(edges, resolved_edges, node_ids)` |
| `compose` | method | `readmenator/_category.py:116` | `def compose(self, a, b)` |
| `dfs` | function | `readmenator/_category.py:139` | `def dfs(current, goal, path, depth)` |
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
| `ComponentDiagramBuilder` | class | `readmenator/_components.py:57` | `class ComponentDiagramBuilder` |
| `__init__` | method | `readmenator/_components.py:60` | `def __init__(self, config)` |
| `_component` | method | `readmenator/_components.py:363` | `def _component(self, cid, label, members, by_id, rank, index, calls, depth, resolved, raw, layers)` |
| `_component_card` | method | `readmenator/_components.py:798` | `def _component_card(self, component, rel_prefix, link_files)` |
| `_components_of` | method | `readmenator/_components.py:349` | `def _components_of(self, nodes, analysis)` |
| `_describe` | method | `readmenator/_components.py:564` | `def _describe(self, label, members, member_nodes, top_symbols, outgoing)` |
| `_dominant_layer` | method | `readmenator/_components.py:461` | `def _dominant_layer(members, layers)` |
| `_layer_color` | method | `readmenator/_components.py:869` | `def _layer_color(self, layer)` |
| `_legend` | method | `readmenator/_components.py:683` | `def _legend(self, components)` |
| `_meta_chips` | method | `readmenator/_components.py:785` | `def _meta_chips(self, analysis)` |
| `_rank_layout` | function | `readmenator/_components.py:1002` | `def _rank_layout(cids, pairs)` |
| `_rel_prefix` | method | `readmenator/_components.py:331` | `def _rel_prefix(project_root, output_dir)` |
| `_relations` | method | `readmenator/_components.py:492` | `def _relations(self, components, file_of_component, resolved, raw, calls, index)` |
| `_relations_section` | method | `readmenator/_components.py:704` | `def _relations_section(self, relations)` |
| `_root_description` | method | `readmenator/_components.py:589` | `def _root_description(self, nodes, components)` |
| `_split` | method | `readmenator/_components.py:481` | `def _split(self, members)` |
| `_svg_level` | method | `readmenator/_components.py:881` | `def _svg_level(self, components, relations, svg_id, anchor_prefix)` |
| `build` | method | `readmenator/_components.py:70` | `def build(self, nodes, edges, resolved_edges, analysis, project_root, content_map)` |
| `component_markdown` | method | `readmenator/_components.py:247` | `def component_markdown(self, component)` |
| `mermaid_lr` | method | `readmenator/_components.py:165` | `def mermaid_lr(self, components, relations, docs_ref)` |
| `overview_markdown` | method | `readmenator/_components.py:199` | `def overview_markdown(self, analysis, docs_ref, rel_prefix)` |
| `render_page` | method | `readmenator/_components.py:611` | `def render_page(self, analysis, title, home_href, rel_prefix, link_files)` |
| `sanitize` | function | `readmenator/_components.py:45` | `def sanitize(name)` |
| `thumbnail_svg` | method | `readmenator/_components.py:738` | `def thumbnail_svg(self, components, relations)` |
| `write` | method | `readmenator/_components.py:275` | `def write(self, analysis, output_dir, project_root)` |
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
| `_blank` | function | `readmenator/_dataflow.py:110` | `def _blank(match)` |
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
| `DocsSitePublisher` | class | `readmenator/_diagrams.py:3225` | `class DocsSitePublisher` |
| `InteractiveMapRenderer` | class | `readmenator/_diagrams.py:1522` | `class InteractiveMapRenderer` |
| `MapDelta` | class | `readmenator/_diagrams.py:212` | `class MapDelta` |
| `MapDiagnostic` | class | `readmenator/_diagrams.py:178` | `class MapDiagnostic` |
| `MapEdge` | class | `readmenator/_diagrams.py:123` | `class MapEdge` |
| `MapNode` | class | `readmenator/_diagrams.py:90` | `class MapNode` |
| `MapReceipt` | class | `readmenator/_diagrams.py:195` | `class MapReceipt` |
| `MapView` | class | `readmenator/_diagrams.py:140` | `class MapView` |
| `SystemMap` | class | `readmenator/_diagrams.py:157` | `class SystemMap` |
| `SystemMapBuilder` | class | `readmenator/_diagrams.py:456` | `class SystemMapBuilder` |
| `SystemMapValidator` | class | `readmenator/_diagrams.py:232` | `class SystemMapValidator` |
| `VisNetworkRenderer` | class | `readmenator/_diagrams.py:2233` | `class VisNetworkRenderer` |
| `__init__` | method | `readmenator/_diagrams.py:235` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:485` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:1525` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:2241` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_diagrams.py:3242` | `def __init__(self, config)` |
| `_annotate_communities` | method | `readmenator/_diagrams.py:557` | `def _annotate_communities(system_map, analysis)` |
| `_brand_block` | method | `readmenator/_diagrams.py:3712` | `def _brand_block(self)` |
| `_build_architecture` | method | `readmenator/_diagrams.py:1124` | `def _build_architecture(self, nodes, links, layers, findings, analysis, full)` |
| `_build_dataflow` | method | `readmenator/_diagrams.py:1346` | `def _build_dataflow(self, nodes, links, layers, findings, full)` |
| `_build_lifecycle` | method | `readmenator/_diagrams.py:1429` | `def _build_lifecycle(self, nodes, links, layers, findings, full)` |
| `_build_sequence` | method | `readmenator/_diagrams.py:1264` | `def _build_sequence(self, nodes, links, layers, analysis, full)` |
| `_build_workflow` | method | `readmenator/_diagrams.py:1184` | `def _build_workflow(self, nodes, links, layers, findings, full)` |
| `_canvas_for` | method | `readmenator/_diagrams.py:1011` | `def _canvas_for(self, positions, full)` |
| `_canvas_size` | method | `readmenator/_diagrams.py:1533` | `def _canvas_size(self, system_map)` |
| `_cap_lane_scope` | method | `readmenator/_diagrams.py:916` | `def _cap_lane_scope(self, ranked, layer_of)` |
| `_card` | method | `readmenator/_diagrams.py:4087` | `def _card(self, kind, system_map, href_prefix)` |
| `_community_legend` | method | `readmenator/_diagrams.py:2355` | `def _community_legend(self, system_map)` |
| `_doc_group` | method | `readmenator/_diagrams.py:3919` | `def _doc_group(self, name)` |
| `_doc_preview` | method | `readmenator/_diagrams.py:3502` | `def _doc_preview(self, text)` |
| `_doc_title` | method | `readmenator/_diagrams.py:3493` | `def _doc_title(text)` |
| `_docs_section` | method | `readmenator/_diagrams.py:3931` | `def _docs_section(self, doc_entries)` |
| `_edge_path` | method | `readmenator/_diagrams.py:1701` | `def _edge_path(self, x1, y1, x2, y2)` |
| `_edges_svg` | method | `readmenator/_diagrams.py:1785` | `def _edges_svg(self, system_map)` |
| `_effective_canvas` | method | `readmenator/_diagrams.py:243` | `def _effective_canvas(self, system_map)` |
| `_escape` | method | `readmenator/_diagrams.py:1679` | `def _escape(self, value)` |
| `_escape` | method | `readmenator/_diagrams.py:4173` | `def _escape(self, value)` |
| `_escape_markup` | function | `readmenator/_diagrams.py:33` | `def _escape_markup(value)` |
| `_extra_card` | method | `readmenator/_diagrams.py:4128` | `def _extra_card(self, entry)` |
| `_fill_template` | function | `readmenator/_diagrams.py:57` | `def _fill_template(template, values)` |
| `_fitted_gap` | method | `readmenator/_diagrams.py:878` | `def _fitted_gap(self, count, item, gap, total, margin)` |
| `_footer` | method | `readmenator/_diagrams.py:3768` | `def _footer(self)` |
| `_glyph` | method | `readmenator/_diagrams.py:4069` | `def _glyph(self, kind)` |
| `_href_prefix` | method | `readmenator/_diagrams.py:4013` | `def _href_prefix(self)` |
| `_internal_links` | method | `readmenator/_diagrams.py:753` | `def _internal_links(self, edges, selected, full)` |
| `_is_full` | method | `readmenator/_diagrams.py:502` | `def _is_full(self, full)` |
| `_json_payload` | function | `readmenator/_diagrams.py:45` | `def _json_payload(payload)` |
| `_lane_capacity` | method | `readmenator/_diagrams.py:902` | `def _lane_capacity(self)` |
| `_lanes_that_fit` | method | `readmenator/_diagrams.py:861` | `def _lanes_that_fit(self, lanes)` |
| `_layout_columns` | method | `readmenator/_diagrams.py:813` | `def _layout_columns(self, items, kind, full)` |
| `_layout_sequence` | method | `readmenator/_diagrams.py:940` | `def _layout_sequence(self, ordered, full)` |
| `_make_views` | method | `readmenator/_diagrams.py:1052` | `def _make_views(self, kind, primary, links)` |
| `_meta_for` | method | `readmenator/_diagrams.py:1029` | `def _meta_for(self, kind, placed, links, total, positions, full)` |
| `_nodes_svg` | method | `readmenator/_diagrams.py:1737` | `def _nodes_svg(self, system_map)` |
| `_place` | method | `readmenator/_diagrams.py:991` | `def _place(self, ranked, layer_of, kind, full)` |
| `_project_pills` | method | `readmenator/_diagrams.py:3739` | `def _project_pills(self)` |
| `_prune_stale_docs` | method | `readmenator/_diagrams.py:3538` | `def _prune_stale_docs(docs_root, keep)` |
| `_ranked_file_ids` | method | `readmenator/_diagrams.py:692` | `def _ranked_file_ids(self, nodes, links, analysis)` |
| `_render_poster` | method | `readmenator/_diagrams.py:3455` | `def _render_poster(self, video, site_root)` |
| `_role_color` | function | `readmenator/_diagrams.py:76` | `def _role_color(role, config)` |
| `_role_color` | method | `readmenator/_diagrams.py:1690` | `def _role_color(self, role)` |
| `_role_for` | method | `readmenator/_diagrams.py:658` | `def _role_for(self, group, sensitive)` |
| `_safe_json` | method | `readmenator/_diagrams.py:1668` | `def _safe_json(self, payload)` |
| `_select_primary` | method | `readmenator/_diagrams.py:727` | `def _select_primary(self, nodes, links, analysis, full)` |
| `_sensitive_files` | method | `readmenator/_diagrams.py:675` | `def _sensitive_files(self, findings)` |
| `_sequence_capacity` | method | `readmenator/_diagrams.py:977` | `def _sequence_capacity(self)` |
| `_short_label` | method | `readmenator/_diagrams.py:798` | `def _short_label(self, value)` |
| `_start_here` | method | `readmenator/_diagrams.py:3852` | `def _start_here(self, entries, video_rel)` |
| `_stat_tiles` | method | `readmenator/_diagrams.py:3832` | `def _stat_tiles(self, stats)` |
| `_stats_line` | method | `readmenator/_diagrams.py:4159` | `def _stats_line(self, stats)` |
| `_symbol_records` | method | `readmenator/_diagrams.py:776` | `def _symbol_records(self, node)` |
| `_template` | method | `readmenator/_diagrams.py:1832` | `def _template(self)` |
| `_template` | method | `readmenator/_diagrams.py:2423` | `def _template(self)` |
| `_title_for` | method | `readmenator/_diagrams.py:644` | `def _title_for(self, kind)` |
| `_tooltip` | method | `readmenator/_diagrams.py:2392` | `def _tooltip(self, node)` |
| `_video_section` | method | `readmenator/_diagrams.py:3892` | `def _video_section(self, video_rel, poster_rel)` |
| `_viewer_css` | method | `readmenator/_diagrams.py:4043` | `def _viewer_css(self)` |
| `_viewer_modal` | method | `readmenator/_diagrams.py:4024` | `def _viewer_modal(self)` |
| `_viewer_script` | method | `readmenator/_diagrams.py:4030` | `def _viewer_script(self)` |
| `build` | method | `readmenator/_diagrams.py:515` | `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)` |
| `build_all` | method | `readmenator/_diagrams.py:574` | `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)` |
| `collect_doc_sources` | method | `readmenator/_diagrams.py:3360` | `def collect_doc_sources(self, project_root)` |
| `compare` | method | `readmenator/_diagrams.py:605` | `def compare(self, base, head)` |
| `description_for` | method | `readmenator/_diagrams.py:3252` | `def description_for(self, kind)` |
| `doc_order` | function | `readmenator/_diagrams.py:3957` | `def doc_order(base)` |
| `order` | function | `readmenator/_diagrams.py:3606` | `def order(entry)` |
| `publish` | method | `readmenator/_diagrams.py:3266` | `def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries, extra_cards)` |
| `publish_assets` | method | `readmenator/_diagrams.py:3386` | `def publish_assets(self, project_root, output_dir)` |
| `render` | method | `readmenator/_diagrams.py:1554` | `def render(self, system_map)` |
| `render` | method | `readmenator/_diagrams.py:2249` | `def render(self, system_map)` |
| `render_index` | method | `readmenator/_diagrams.py:3634` | `def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries, poster_rel, extra_cards)` |
| `render_llms_txt` | method | `readmenator/_diagrams.py:3555` | `def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)` |
| `supported_kinds` | method | `readmenator/_diagrams.py:494` | `def supported_kinds(self)` |
| `validate` | method | `readmenator/_diagrams.py:264` | `def validate(self, system_map)` |
| `write` | method | `readmenator/_diagrams.py:1649` | `def write(self, system_map, output_path)` |
| `write` | method | `readmenator/_diagrams.py:2375` | `def write(self, system_map, output_path)` |
| `DocComment` | class | `readmenator/_docstrings.py:161` | `class DocComment` |
| `DocField` | class | `readmenator/_docstrings.py:135` | `class DocField` |
| `_apply_section` | function | `readmenator/_docstrings.py:336` | `def _apply_section(doc, key, body, item_mode)` |
| `_elixir_doc` | function | `readmenator/_docstrings.py:888` | `def _elixir_doc(lines, index, lookback)` |
| `_extract_doctests` | function | `readmenator/_docstrings.py:642` | `def _extract_doctests(text)` |

Next: [SYMBOLS_p2.md](SYMBOLS_p2.md)
