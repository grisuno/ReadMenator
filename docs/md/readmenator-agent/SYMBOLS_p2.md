# Symbols (page 2 of 7)
Previous: [SYMBOLS.md](SYMBOLS.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_extract_doctests` | function | `readmenator/_docstrings.py:642` | `def _extract_doctests(text)` |
| `_indent` | function | `readmenator/_docstrings.py:321` | `def _indent(line)` |
| `_join_block` | function | `readmenator/_docstrings.py:326` | `def _join_block(lines)` |
| `_parse_items` | function | `readmenator/_docstrings.py:393` | `def _parse_items(body, mode, allow_bare)` |
| `_parse_jsdoc_param` | function | `readmenator/_docstrings.py:664` | `def _parse_jsdoc_param(rest)` |
| `_parse_rest` | function | `readmenator/_docstrings.py:551` | `def _parse_rest(text)` |
| `_parse_return` | function | `readmenator/_docstrings.py:480` | `def _parse_return(body, mode)` |
| `_parse_sections` | function | `readmenator/_docstrings.py:498` | `def _parse_sections(text, mode)` |
| `_parse_tags` | function | `readmenator/_docstrings.py:690` | `def _parse_tags(text)` |
| `_parse_xml` | function | `readmenator/_docstrings.py:778` | `def _parse_xml(text)` |
| `_section_key` | function | `readmenator/_docstrings.py:331` | `def _section_key(header)` |
| `_split_refs` | function | `readmenator/_docstrings.py:382` | `def _split_refs(text)` |
| `_strip_fence` | function | `readmenator/_docstrings.py:372` | `def _strip_fence(text)` |
| `_strip_line_prefix` | function | `readmenator/_docstrings.py:874` | `def _strip_line_prefix(line, prefixes)` |
| `_xml_inline` | function | `readmenator/_docstrings.py:767` | `def _xml_inline(text)` |
| `clean_text` | function | `readmenator/_docstrings.py:230` | `def clean_text(text)` |
| `detect_style` | function | `readmenator/_docstrings.py:254` | `def detect_style(text)` |
| `flush` | function | `readmenator/_docstrings.py:413` | `def flush()` |
| `grab` | function | `readmenator/_docstrings.py:782` | `def grab(tag)` |
| `is_empty` | method | `readmenator/_docstrings.py:195` | `def is_empty(self)` |
| `param` | method | `readmenator/_docstrings.py:203` | `def param(self, name)` |
| `parse_docstring` | function | `readmenator/_docstrings.py:809` | `def parse_docstring(text)` |
| `recover_comment` | function | `readmenator/_docstrings.py:910` | `def recover_comment(content_lines, line, language, lookback)` |
| `split_summary` | function | `readmenator/_docstrings.py:293` | `def split_summary(text)` |
| `to_dict` | method | `readmenator/_docstrings.py:150` | `def to_dict(self)` |
| `to_dict` | method | `readmenator/_docstrings.py:211` | `def to_dict(self)` |
| `DocumentationGenerator` | class | `readmenator/_documentation.py:36` | `class DocumentationGenerator` |
| `__init__` | method | `readmenator/_documentation.py:48` | `def __init__(self, config)` |
| `_apply_context_budget` | method | `readmenator/_documentation.py:217` | `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)` |
| `_build_analytics_section` | method | `readmenator/_documentation.py:711` | `def _build_analytics_section(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2)` |
| `_build_architecture_reference` | method | `readmenator/_documentation.py:1275` | `def _build_architecture_reference(self, nodes, edges)` |
| `_build_change_impact` | method | `readmenator/_documentation.py:1056` | `def _build_change_impact(self, analysis_v2)` |
| `_build_community_analysis` | method | `readmenator/_documentation.py:600` | `def _build_community_analysis(self, analysis, nodes)` |
| `_build_concept_graph` | method | `readmenator/_documentation.py:988` | `def _build_concept_graph(self, analysis_v2)` |
| `_build_cpg_block` | method | `readmenator/_documentation.py:1249` | `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)` |
| `_build_dashboard` | method | `readmenator/_documentation.py:492` | `def _build_dashboard(self, nodes, edges, resolved_edges)` |
| `_build_dataflow_analysis` | method | `readmenator/_documentation.py:957` | `def _build_dataflow_analysis(self, analysis_v2)` |
| `_build_dependency_cycles` | method | `readmenator/_documentation.py:1035` | `def _build_dependency_cycles(self, analysis_v2)` |
| `_build_forcegraph_section` | method | `readmenator/_documentation.py:674` | `def _build_forcegraph_section(self, nodes, edges, resolved_edges, analysis, layers, findings)` |
| `_build_god_nodes` | method | `readmenator/_documentation.py:572` | `def _build_god_nodes(self, analysis, ranked)` |
| `_build_hotspots` | method | `readmenator/_documentation.py:919` | `def _build_hotspots(self, analysis_v2, ranked)` |
| `_build_layer_violations` | method | `readmenator/_documentation.py:1081` | `def _build_layer_violations(self, analysis_v2)` |
| `_build_layers` | method | `readmenator/_documentation.py:458` | `def _build_layers(self, layers, nodes)` |
| `_build_mermaid_section` | method | `readmenator/_documentation.py:1181` | `def _build_mermaid_section(self, graph_output, is_truncated)` |
| `_build_orphans` | method | `readmenator/_documentation.py:792` | `def _build_orphans(self, nodes, analysis_v2, ranked)` |
| `_build_query_recipes` | method | `readmenator/_documentation.py:842` | `def _build_query_recipes(self)` |
| `_build_ranked_context` | method | `readmenator/_documentation.py:746` | `def _build_ranked_context(self, ranked)` |
| `_build_security_findings` | method | `readmenator/_documentation.py:1134` | `def _build_security_findings(self, findings)` |
| `_build_suggested_questions` | method | `readmenator/_documentation.py:658` | `def _build_suggested_questions(self, analysis)` |
| `_build_suggested_rules` | method | `readmenator/_documentation.py:1109` | `def _build_suggested_rules(self, analysis_v2)` |
| `_build_surprising_connections` | method | `readmenator/_documentation.py:633` | `def _build_surprising_connections(self, analysis, nodes)` |
| `_build_taint_analysis` | method | `readmenator/_documentation.py:884` | `def _build_taint_analysis(self, analysis_v2)` |
| `_build_toc` | method | `readmenator/_documentation.py:355` | `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked, extra_sections)` |
| `_build_uml_diagram` | method | `readmenator/_documentation.py:1204` | `def _build_uml_diagram(self, nodes, edges)` |
| `_get_git_commit` | method | `readmenator/_documentation.py:89` | `def _get_git_commit()` |
| `_ranking_version` | method | `readmenator/_documentation.py:71` | `def _ranking_version(self)` |
| `generate` | method | `readmenator/_documentation.py:99` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked, content_map)` |
| `Embedder` | class | `readmenator/_embed.py:39` | `class Embedder` |
| `__init__` | method | `readmenator/_embed.py:42` | `def __init__(self, config)` |
| `_jaccard` | function | `readmenator/_embed.py:27` | `def _jaccard(left, right)` |
| `_tokens` | function | `readmenator/_embed.py:22` | `def _tokens(text)` |
| `cluster_jaccard` | method | `readmenator/_embed.py:99` | `def cluster_jaccard(self, corpus, threshold)` |
| `dependencies_available` | method | `readmenator/_embed.py:50` | `def dependencies_available(self)` |
| `encode` | method | `readmenator/_embed.py:58` | `def encode(self, texts)` |
| `find` | function | `readmenator/_embed.py:115` | `def find(item)` |
| `near_jaccard` | method | `readmenator/_embed.py:75` | `def near_jaccard(self, query, corpus, top_k)` |
| `project_jaccard` | method | `readmenator/_embed.py:138` | `def project_jaccard(self, corpus)` |
| `union` | function | `readmenator/_embed.py:122` | `def union(left, right)` |
| `ExclusionEntry` | class | `readmenator/_exclusions.py:19` | `class ExclusionEntry` |
| `ExclusionList` | class | `readmenator/_exclusions.py:44` | `class ExclusionList` |
| `__init__` | method | `readmenator/_exclusions.py:47` | `def __init__(self, config)` |
| `_to_entry` | function | `readmenator/_exclusions.py:146` | `def _to_entry(data)` |
| `_unquote` | function | `readmenator/_exclusions.py:157` | `def _unquote(value)` |
| `entries` | method | `readmenator/_exclusions.py:58` | `def entries(self)` |
| `filter_findings` | method | `readmenator/_exclusions.py:98` | `def filter_findings(self, findings)` |
| `is_excluded` | method | `readmenator/_exclusions.py:86` | `def is_excluded(self, file_path, rule_id)` |
| `load` | method | `readmenator/_exclusions.py:62` | `def load(self, project_root)` |
| `matches` | method | `readmenator/_exclusions.py:27` | `def matches(self, file_path, rule_id)` |
| `parse_exclusions` | function | `readmenator/_exclusions.py:114` | `def parse_exclusions(text)` |
| `_find_item` | function | `readmenator/_explain.py:163` | `def _find_item(node_id, items)` |
| `explain_rank` | function | `readmenator/_explain.py:16` | `def explain_rank(node_id, ranked, category)` |
| `rank_summary` | function | `readmenator/_explain.py:140` | `def rank_summary(ranked, top_n)` |
| `ExplorerState` | class | `readmenator/_explorer.py:23` | `class ExplorerState` |
| `_Handler` | class | `readmenator/_explorer.py:105` | `class _Handler(BaseHTTPRequestHandler)` |
| `__init__` | method | `readmenator/_explorer.py:26` | `def __init__(self, config, nodes, edges, resolved_edges, analysis, findings, layers, content_map)` |
| `_serve_html` | method | `readmenator/_explorer.py:135` | `def _serve_html(self)` |
| `_serve_json` | method | `readmenator/_explorer.py:158` | `def _serve_json(self, payload)` |
| `_serve_vendor` | method | `readmenator/_explorer.py:144` | `def _serve_vendor(self)` |
| `build_state` | function | `readmenator/_explorer.py:221` | `def build_state(config, nodes, edges, resolved_edges, analysis, findings, layers, content_map)` |
| `do_GET` | method | `readmenator/_explorer.py:112` | `def do_GET(self)` |
| `find_free_port` | function | `readmenator/_explorer.py:169` | `def find_free_port(preferred)` |
| `log_message` | method | `readmenator/_explorer.py:108` | `def log_message(self, fmt)` |
| `samples` | method | `readmenator/_explorer.py:64` | `def samples(self)` |
| `serve` | function | `readmenator/_explorer.py:188` | `def serve(state, host, port, open_browser)` |
| `source` | method | `readmenator/_explorer.py:80` | `def source(self, file_id)` |
| `write_static` | function | `readmenator/_explorer.py:249` | `def write_static(state, output_dir, filename)` |
| `GraphExporter` | class | `readmenator/_exporter.py:28` | `class GraphExporter` |
| `__init__` | method | `readmenator/_exporter.py:36` | `def __init__(self, config)` |
| `_community_color_map` | method | `readmenator/_exporter.py:272` | `def _community_color_map(self, analysis)` |
| `_layout_spring` | method | `readmenator/_exporter.py:615` | `def _layout_spring(self, nodes, edges, node_map)` |
| `_lighten` | method | `readmenator/_exporter.py:290` | `def _lighten(hex_color)` |
| `_project` | function | `readmenator/_exporter.py:544` | `def _project(pos)` |
| `_render_html` | method | `readmenator/_exporter.py:298` | `def _render_html(self, vis_nodes, vis_edges, analysis, findings)` |
| `_render_truncated_svg` | method | `readmenator/_exporter.py:600` | `def _render_truncated_svg(self, total_nodes)` |
| `_sev_span` | function | `readmenator/_exporter.py:370` | `def _sev_span(sev, count)` |
| `to_cypher` | method | `readmenator/_exporter.py:773` | `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` |
| `to_forcegraph` | method | `readmenator/_exporter.py:1020` | `def to_forcegraph(self, nodes, edges, resolved_edges, analysis, layers, findings, analytics)` |
| `to_graphml` | method | `readmenator/_exporter.py:696` | `def to_graphml(self, nodes, edges, resolved_edges, analysis)` |
| `to_html` | method | `readmenator/_exporter.py:183` | `def to_html(self, nodes, edges, resolved_edges, analysis, findings)` |
| `to_json` | method | `readmenator/_exporter.py:44` | `def to_json(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` |
| `to_obsidian` | method | `readmenator/_exporter.py:895` | `def to_obsidian(self, nodes, edges, output_dir, analysis, concept_graph)` |
| `to_svg` | method | `readmenator/_exporter.py:482` | `def to_svg(self, nodes, edges, resolved_edges, analysis)` |
| `ArchitectureDiagramBuilder` | class | `readmenator/_flowcharts.py:259` | `class ArchitectureDiagramBuilder` |
| `Component` | class | `readmenator/_flowcharts.py:237` | `class Component` |
| `EntryPoint` | class | `readmenator/_flowcharts.py:499` | `class EntryPoint` |
| `ExecutionFlowBuilder` | class | `readmenator/_flowcharts.py:543` | `class ExecutionFlowBuilder` |
| `FlowStep` | class | `readmenator/_flowcharts.py:523` | `class FlowStep` |
| `_ControlFlowBuilder` | class | `readmenator/_flowcharts.py:936` | `class _ControlFlowBuilder` |
| `__init__` | method | `readmenator/_flowcharts.py:262` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_flowcharts.py:546` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_flowcharts.py:948` | `def __init__(self, config, project_names, summaries, file_id)` |
| `_block` | method | `readmenator/_flowcharts.py:1017` | `def _block(self, body, tails)` |
| `_call_lines` | method | `readmenator/_flowcharts.py:987` | `def _call_lines(self, calls)` |
| `_calls` | method | `readmenator/_flowcharts.py:973` | `def _calls(self, node)` |
| `_case_of` | method | `readmenator/_flowcharts.py:1074` | `def _case_of(test)` |
| `_compound` | method | `readmenator/_flowcharts.py:1094` | `def _compound(self, stmt, tails)` |
| `_connect` | method | `readmenator/_flowcharts.py:1012` | `def _connect(self, tails, target)` |
| `_definition_detail` | method | `readmenator/_flowcharts.py:764` | `def _definition_detail(self, key, defs)` |
| `_first_sentence` | function | `readmenator/_flowcharts.py:927` | `def _first_sentence(text)` |
| `_heavy_threshold` | method | `readmenator/_flowcharts.py:490` | `def _heavy_threshold(counts)` |
| `_is_test` | method | `readmenator/_flowcharts.py:555` | `def _is_test(self, file_id)` |
| `_link` | method | `readmenator/_flowcharts.py:969` | `def _link(self, src, dst, label, style)` |
| `_new` | method | `readmenator/_flowcharts.py:958` | `def _new(self, shape, title, lines, tone, line, calls)` |
| `_short` | method | `readmenator/_flowcharts.py:754` | `def _short(self, key)` |
| `add` | function | `readmenator/_flowcharts.py:800` | `def add(key, tone)` |
| `build` | method | `readmenator/_flowcharts.py:994` | `def build(self, body, title)` |
| `build_flow_graphs` | function | `readmenator/_flowcharts.py:1231` | `def build_flow_graphs(config, nodes, edges, resolved_edges, content_map, analysis, layers)` |
| `bump` | function | `readmenator/_flowcharts.py:668` | `def bump(file_id, name, line, points, reason)` |
| `call_graph` | method | `readmenator/_flowcharts.py:564` | `def call_graph(self, nodes, edges, resolved_edges, content_map)` |
| `call_tree_mermaid` | method | `readmenator/_flowcharts.py:827` | `def call_tree_mermaid(self, entry, steps, defs)` |
| `call_tree_model` | method | `readmenator/_flowcharts.py:779` | `def call_tree_model(self, entry, steps, defs)` |
| `caller_key` | function | `readmenator/_flowcharts.py:596` | `def caller_key(site_file, site_line, caller)` |
| `components` | method | `readmenator/_flowcharts.py:270` | `def components(self, nodes, analysis, layers)` |
| `control_flow_mermaid` | method | `readmenator/_flowcharts.py:921` | `def control_flow_mermaid(self, content, entry, project_names)` |
| `control_flow_model` | method | `readmenator/_flowcharts.py:877` | `def control_flow_model(self, content, entry, project_names, defs, call_graph)` |
| `declare` | function | `readmenator/_flowcharts.py:1187` | `def declare(node, indent)` |
| `eades_lin_smyth` | function | `readmenator/_flowcharts.py:185` | `def eades_lin_smyth(vertices, weight)` |
| `entry_points` | method | `readmenator/_flowcharts.py:645` | `def entry_points(self, nodes, graph, defs, content_map)` |
| `flush` | function | `readmenator/_flowcharts.py:1022` | `def flush()` |
| `key` | method | `readmenator/_flowcharts.py:517` | `def key(self)` |
| `label` | function | `readmenator/_flowcharts.py:1182` | `def label(node)` |
| `live` | function | `readmenator/_flowcharts.py:211` | `def live(table)` |
| `mermaid_id` | function | `readmenator/_flowcharts.py:67` | `def mermaid_id(text, prefix)` |
| `mermaid_text` | function | `readmenator/_flowcharts.py:72` | `def mermaid_text(text, limit)` |
| `model` | method | `readmenator/_flowcharts.py:335` | `def model(self, nodes, resolved_edges, analysis, layers)` |
| `reachable` | function | `readmenator/_flowcharts.py:149` | `def reachable(vertex)` |
| `render` | method | `readmenator/_flowcharts.py:476` | `def render(self, nodes, resolved_edges, analysis, layers)` |
| `render_architecture_section` | function | `readmenator/_flowcharts.py:1287` | `def render_architecture_section(config, nodes, resolved_edges, analysis, layers)` |
| `render_flows_section` | function | `readmenator/_flowcharts.py:1319` | `def render_flows_section(config, nodes, edges, resolved_edges, content_map)` |
| `sequence_mermaid` | method | `readmenator/_flowcharts.py:862` | `def sequence_mermaid(self, entry, steps, defs)` |
| `sequence_model` | method | `readmenator/_flowcharts.py:831` | `def sequence_model(self, entry, steps, defs)` |
| `tarjan_scc` | function | `readmenator/_flowcharts.py:80` | `def tarjan_scc(vertices, adjacency)` |
| `to_mermaid` | function | `readmenator/_flowcharts.py:1170` | `def to_mermaid(graph, direction)` |
| `transitive_reduction` | function | `readmenator/_flowcharts.py:134` | `def transitive_reduction(adjacency)` |
| `visit` | function | `readmenator/_flowcharts.py:738` | `def visit(caller, depth, path)` |
| `walk` | method | `readmenator/_flowcharts.py:723` | `def walk(self, graph, start)` |
| `FlowEdge` | class | `readmenator/_flowlayout.py:67` | `class FlowEdge` |
| `FlowGraph` | class | `readmenator/_flowlayout.py:86` | `class FlowGraph` |
| `FlowNode` | class | `readmenator/_flowlayout.py:36` | `class FlowNode` |
| `LayoutMetrics` | class | `readmenator/_flowlayout.py:146` | `class LayoutMetrics` |
| `_ranks` | function | `readmenator/_flowlayout.py:210` | `def _ranks(graph)` |
| `_wrap` | function | `readmenator/_flowlayout.py:180` | `def _wrap(lines, metrics)` |
| `layout_flow` | function | `readmenator/_flowlayout.py:260` | `def layout_flow(graph, metrics, direction)` |
| `layout_sequence` | function | `readmenator/_flowlayout.py:414` | `def layout_sequence(graph, metrics)` |
| `measure` | function | `readmenator/_flowlayout.py:195` | `def measure(node, metrics)` |
| `node` | method | `readmenator/_flowlayout.py:117` | `def node(self, node_id)` |
| `to_dict` | method | `readmenator/_flowlayout.py:124` | `def to_dict(self)` |
| `flow_thumbnail_svg` | function | `readmenator/_flowpage.py:264` | `def flow_thumbnail_svg(graph, width, height)` |
| `flows_payload_json` | function | `readmenator/_flowpage.py:225` | `def flows_payload_json(graphs, api_href)` |
| `render_flows_page` | function | `readmenator/_flowpage.py:231` | `def render_flows_page(graphs, project_name, api_href, config)` |
| `FolderReadmeWriter` | class | `readmenator/_folder_readme.py:65` | `class FolderReadmeWriter` |
| `FolderSpec` | class | `readmenator/_folder_readme.py:27` | `class FolderSpec` |
| `__init__` | method | `readmenator/_folder_readme.py:68` | `def __init__(self, config)` |
| `is_generated_folder_readme` | function | `readmenator/_folder_readme.py:45` | `def is_generated_folder_readme(path, config)` |
| `render` | method | `readmenator/_folder_readme.py:272` | `def render(self, spec, folder)` |
| `specs` | method | `readmenator/_folder_readme.py:76` | `def specs(self)` |
| `write_all` | method | `readmenator/_folder_readme.py:310` | `def write_all(self, project_root)` |
| `ForceGraphRenderer` | class | `readmenator/_forcegraph.py:82` | `class ForceGraphRenderer` |
| `__init__` | method | `readmenator/_forcegraph.py:85` | `def __init__(self, config)` |
| `_family_color` | method | `readmenator/_forcegraph.py:523` | `def _family_color(self, name)` |
| `_file_color` | method | `readmenator/_forcegraph.py:645` | `def _file_color(self, node_id, family, layer, palette)` |
| `_node_doc` | method | `readmenator/_forcegraph.py:626` | `def _node_doc(self, node)` |
| `_seed_positions` | method | `readmenator/_forcegraph.py:316` | `def _seed_positions(self, payload)` |
| `_symbol_list` | method | `readmenator/_forcegraph.py:632` | `def _symbol_list(self, node)` |
| `add_node` | function | `readmenator/_forcegraph.py:204` | `def add_node(node_id, label, node_type)` |
| `build_payload` | method | `readmenator/_forcegraph.py:114` | `def build_payload(self, nodes, edges, resolved_edges, analysis, layers, findings, content_map)` |
| `copy_vendor` | method | `readmenator/_forcegraph.py:607` | `def copy_vendor(self, dest_dir)` |
| `edge_palette` | method | `readmenator/_forcegraph.py:97` | `def edge_palette(self)` |
| `family_color` | method | `readmenator/_forcegraph.py:512` | `def family_color(self, name)` |
| `family_color_from_name` | function | `readmenator/_forcegraph.py:41` | `def family_color_from_name(name, sat_base, sat_span, light_base, light_span)` |
| `file_of` | function | `readmenator/_forcegraph.py:150` | `def file_of(edge_id)` |
| `group_colors` | method | `readmenator/_forcegraph.py:413` | `def group_colors(self, payload)` |
| `node_palette` | method | `readmenator/_forcegraph.py:93` | `def node_palette(self)` |
| `node_value` | function | `readmenator/_forcegraph.py:69` | `def node_value(symbols, degree)` |
| `page_settings` | method | `readmenator/_forcegraph.py:436` | `def page_settings(self, payload, live_api)` |
| `render` | method | `readmenator/_forcegraph.py:359` | `def render(self, payload, analytics, title, home_href, live_api)` |
| `thumbnail_svg` | method | `readmenator/_forcegraph.py:540` | `def thumbnail_svg(self, payload)` |
| `vendor_href` | method | `readmenator/_forcegraph.py:109` | `def vendor_href(self)` |
| `vendor_source` | method | `readmenator/_forcegraph.py:101` | `def vendor_source(self)` |
| `write` | method | `readmenator/_forcegraph.py:580` | `def write(self, output_path, payload, analytics, title, home_href)` |
| `GitHubWikiPublisher` | class | `readmenator/_gh_wiki.py:60` | `class GitHubWikiPublisher` |
| `WikiPublishResult` | class | `readmenator/_gh_wiki.py:40` | `class WikiPublishResult` |
| `__init__` | method | `readmenator/_gh_wiki.py:63` | `def __init__(self, config, runner)` |
| `_blob_base` | method | `readmenator/_gh_wiki.py:122` | `def _blob_base(self, remote, commit)` |
| `_call` | method | `readmenator/_gh_wiki.py:280` | `def _call(self, command, cwd)` |
| `_fallback_home` | method | `readmenator/_gh_wiki.py:206` | `def _fallback_home(self, project_name)` |
| `_footer` | method | `readmenator/_gh_wiki.py:242` | `def _footer(git)` |
| `_origin` | method | `readmenator/_gh_wiki.py:268` | `def _origin(self, project_root)` |
| `_sidebar` | method | `readmenator/_gh_wiki.py:214` | `def _sidebar(self, names)` |
| `_write_pages` | method | `readmenator/_gh_wiki.py:294` | `def _write_pages(self, target, pages)` |
| `collect_sources` | method | `readmenator/_gh_wiki.py:97` | `def collect_sources(self, project_root)` |
| `link` | function | `readmenator/_gh_wiki.py:152` | `def link(match)` |
| `page_name` | method | `readmenator/_gh_wiki.py:73` | `def page_name(self, rel_path)` |
| `permalink` | function | `readmenator/_gh_wiki.py:165` | `def permalink(match)` |
| `publish` | method | `readmenator/_gh_wiki.py:314` | `def publish(self, project_root, dry_run)` |
| `render` | method | `readmenator/_gh_wiki.py:180` | `def render(self, project_root, remote)` |
| `rewrite` | method | `readmenator/_gh_wiki.py:130` | `def rewrite(self, text, rel_path, names, project_root, blob_base)` |
| `wiki_remote` | method | `readmenator/_gh_wiki.py:250` | `def wiki_remote(self, project_root)` |
| `GitHistoryReader` | class | `readmenator/_githistory.py:67` | `class GitHistoryReader` |
| `HistoryRelease` | class | `readmenator/_githistory.py:43` | `class HistoryRelease` |
| `__init__` | method | `readmenator/_githistory.py:76` | `def __init__(self, config, runner)` |
| `_blobs` | method | `readmenator/_githistory.py:279` | `def _blobs(self, root, shas)` |
| `_commit_date` | method | `readmenator/_githistory.py:198` | `def _commit_date(self, root, commit)` |
| `_entries` | method | `readmenator/_githistory.py:139` | `def _entries(self, root)` |
| `_genesis` | method | `readmenator/_githistory.py:162` | `def _genesis(self, root)` |
| `_git` | method | `readmenator/_githistory.py:296` | `def _git(self, root, args)` |
| `_git_bytes` | method | `readmenator/_githistory.py:301` | `def _git_bytes(self, root, args)` |
| `_git_env` | method | `readmenator/_githistory.py:333` | `def _git_env()` |
| `_head` | method | `readmenator/_githistory.py:191` | `def _head(self, root)` |
| `_is_source` | method | `readmenator/_githistory.py:261` | `def _is_source(self, path, scanner)` |
| `_parse_blobs` | method | `readmenator/_githistory.py:367` | `def _parse_blobs(payload)` |
| `_parse_tree` | method | `readmenator/_githistory.py:353` | `def _parse_tree(raw)` |
| `_resolve_links` | method | `readmenator/_githistory.py:233` | `def _resolve_links(self, file_ids, edges, root)` |
| `_run` | method | `readmenator/_githistory.py:308` | `def _run(self, root, args, stdin_file, stdout_file)` |
| `_snapshot` | method | `readmenator/_githistory.py:202` | `def _snapshot(self, root, label, ref, commit, date)` |
| `_source_files` | method | `readmenator/_githistory.py:247` | `def _source_files(self, tree)` |
| `_tags` | method | `readmenator/_githistory.py:171` | `def _tags(self, root)` |
| `_tree` | method | `readmenator/_githistory.py:274` | `def _tree(self, root, commit)` |
| `_version_label` | method | `readmenator/_githistory.py:341` | `def _version_label(ref)` |
| `available` | method | `readmenator/_githistory.py:81` | `def available(self, project_root)` |
| `timeline` | method | `readmenator/_githistory.py:100` | `def timeline(self, project_root)` |
| `_git_dir` | function | `readmenator/_gitmeta.py:38` | `def _git_dir(root)` |
| `_packed_ref` | function | `readmenator/_gitmeta.py:59` | `def _packed_ref(git_dir, ref)` |
| `_read_small` | function | `readmenator/_gitmeta.py:19` | `def _read_small(path)` |
| `read_git_head` | function | `readmenator/_gitmeta.py:84` | `def read_git_head(project_root)` |
| `BundleLayout` | class | `readmenator/_graphlayout.py:281` | `class BundleLayout` |
| `ForceAtlas2Settings` | class | `readmenator/_graphlayout.py:40` | `class ForceAtlas2Settings` |
| `SphereBundleLayout` | class | `readmenator/_graphlayout.py:461` | `class SphereBundleLayout` |
| `_angular_distance` | function | `readmenator/_graphlayout.py:648` | `def _angular_distance(a, b)` |
| `_bspline` | function | `readmenator/_graphlayout.py:301` | `def _bspline(control, samples)` |
| `_bundle_curves` | function | `readmenator/_graphlayout.py:324` | `def _bundle_curves(leaves, member_group, hub, root, edges, beta, samples)` |
| `_center_out` | function | `readmenator/_graphlayout.py:676` | `def _center_out(members)` |
| `_fa2_numpy` | function | `readmenator/_graphlayout.py:119` | `def _fa2_numpy(n, pairs, start, cfg)` |
| `_fa2_python` | function | `readmenator/_graphlayout.py:166` | `def _fa2_python(n, pairs, start, cfg)` |
| `_group_order_cost` | function | `readmenator/_graphlayout.py:688` | `def _group_order_cost(order, sizes, weights, gap)` |
| `_initial_positions` | function | `readmenator/_graphlayout.py:66` | `def _initial_positions(n, seed, dims)` |
| `_snapshot_steps` | function | `readmenator/_graphlayout.py:113` | `def _snapshot_steps(iterations, snapshots)` |
| `_split_caps` | function | `readmenator/_graphlayout.py:479` | `def _split_caps(labels, sizes, points, lattice, out)` |
| `_undirected_weights` | function | `readmenator/_graphlayout.py:623` | `def _undirected_weights(groups, edges)` |
| `_unit` | function | `readmenator/_graphlayout.py:452` | `def _unit(v)` |
| `bundle_angular_cost` | function | `readmenator/_graphlayout.py:654` | `def bundle_angular_cost(groups, edges, group_gap)` |
| `chord_total` | function | `readmenator/_graphlayout.py:829` | `def chord_total(leaves)` |
| `fibonacci_sphere` | function | `readmenator/_graphlayout.py:429` | `def fibonacci_sphere(count)` |
| `fit_frames` | function | `readmenator/_graphlayout.py:221` | `def fit_frames(frames, box, margin, trim)` |
| `forceatlas2_frames` | function | `readmenator/_graphlayout.py:73` | `def forceatlas2_frames(ids, edges, settings)` |
| `hierarchical_edge_bundling` | function | `readmenator/_graphlayout.py:374` | `def hierarchical_edge_bundling(groups, edges, center, radius, beta, samples, group_gap, inner_ratio)` |
| `interpolate_frames` | function | `readmenator/_graphlayout.py:266` | `def interpolate_frames(frames, t)` |
| `normalize_cloud` | function | `readmenator/_graphlayout.py:586` | `def normalize_cloud(points, quantile, max_radius)` |
| `optimize_bundle_order` | function | `readmenator/_graphlayout.py:702` | `def optimize_bundle_order(groups, edges, sweeps, passes, group_gap)` |
| `refine_sphere_leaves` | function | `readmenator/_graphlayout.py:804` | `def refine_sphere_leaves(layout, groups, edges, sweeps)` |
| `spherical_edge_bundling` | function | `readmenator/_graphlayout.py:516` | `def spherical_edge_bundling(groups, edges, radius, beta, samples, inner_ratio, refine_sweeps, affinity_edges)` |
| `Bm25Index` | class | `readmenator/_graphrag.py:267` | `class Bm25Index` |
| `GraphRagBuilder` | class | `readmenator/_graphrag.py:345` | `class GraphRagBuilder` |
| `GraphRagIndex` | class | `readmenator/_graphrag.py:169` | `class GraphRagIndex` |
| `GraphRagSearcher` | class | `readmenator/_graphrag.py:942` | `class GraphRagSearcher` |
| `GraphRagStore` | class | `readmenator/_graphrag.py:1212` | `class GraphRagStore` |
| `RagCommunity` | class | `readmenator/_graphrag.py:136` | `class RagCommunity` |
| `RagContext` | class | `readmenator/_graphrag.py:216` | `class RagContext` |
| `RagEntity` | class | `readmenator/_graphrag.py:67` | `class RagEntity` |
| `RagRelation` | class | `readmenator/_graphrag.py:94` | `class RagRelation` |
| `RagTextUnit` | class | `readmenator/_graphrag.py:115` | `class RagTextUnit` |
| `__init__` | method | `readmenator/_graphrag.py:270` | `def __init__(self, documents, k1, b)` |
| `__init__` | method | `readmenator/_graphrag.py:348` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_graphrag.py:945` | `def __init__(self, config, index)` |
| `__init__` | method | `readmenator/_graphrag.py:1215` | `def __init__(self, config)` |
| `_budget_chars` | method | `readmenator/_graphrag.py:1020` | `def _budget_chars(self, budget_tokens)` |
| `_community_report` | method | `readmenator/_graphrag.py:704` | `def _community_report(self, index, label, members, node_by_id, resolved_edges, layers, findings, analysis_v2...` |
| `_edge_kind` | function | `readmenator/_graphrag.py:327` | `def _edge_kind(relation)` |
| `_entity_doc` | method | `readmenator/_graphrag.py:974` | `def _entity_doc(self, entity)` |
| `_entity_rank` | method | `readmenator/_graphrag.py:597` | `def _entity_rank(self, ids, relations)` |
| `_file_entity` | function | `readmenator/_graphrag.py:322` | `def _file_entity(file_id)` |
| `_file_rank` | method | `readmenator/_graphrag.py:608` | `def _file_rank(self, nodes, resolved_edges)` |
| `_kind_counts` | method | `readmenator/_graphrag.py:578` | `def _kind_counts(entities)` |
| `_location` | method | `readmenator/_graphrag.py:1151` | `def _location(entity)` |
| `_pack` | method | `readmenator/_graphrag.py:1175` | `def _pack(self, header, sections, budget_tokens, shares)` |
| `_rating` | method | `readmenator/_graphrag.py:851` | `def _rating(self, mass, top_mass, risk)` |
| `_relation_weight` | function | `readmenator/_graphrag.py:335` | `def _relation_weight(relation)` |
| `_report_block` | method | `readmenator/_graphrag.py:1163` | `def _report_block(report)` |
| `_reports` | method | `readmenator/_graphrag.py:659` | `def _reports(self, nodes, resolved_edges, analysis, layers, findings, analysis_v2, file_rank, entities)` |
| `_risk_score` | method | `readmenator/_graphrag.py:649` | `def _risk_score(self, files, findings)` |
| `_root_report` | method | `readmenator/_graphrag.py:908` | `def _root_report(self, reports, themes, nodes, analysis)` |
| `_section` | method | `readmenator/_graphrag.py:1158` | `def _section(title, items)` |
| `_short` | function | `readmenator/_graphrag.py:340` | `def _short(file_id)` |
| `_text_units` | method | `readmenator/_graphrag.py:615` | `def _text_units(self, nodes, content_map)` |
| `_themes` | method | `readmenator/_graphrag.py:864` | `def _themes(self, reports, links)` |
| `_tok` | method | `readmenator/_graphrag.py:970` | `def _tok(self, text)` |
| `_undirected_graph` | method | `readmenator/_graphrag.py:585` | `def _undirected_graph(self, ids, relations)` |
| `_unit_block` | method | `readmenator/_graphrag.py:1170` | `def _unit_block(unit)` |
| `_walk_graph` | method | `readmenator/_graphrag.py:979` | `def _walk_graph(self)` |
| `add_relation` | function | `readmenator/_graphrag.py:406` | `def add_relation(source, target, relation, description, confidence)` |
| `build` | method | `readmenator/_graphrag.py:358` | `def build(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, concept_graph, content_map...` |
| `choose_mode` | method | `readmenator/_graphrag.py:987` | `def choose_mode(self, query)` |
| `directory` | method | `readmenator/_graphrag.py:1223` | `def directory(self, project_root)` |
| `from_dict` | method | `readmenator/_graphrag.py:197` | `def from_dict(cls, data)` |
| `global_search` | method | `readmenator/_graphrag.py:1106` | `def global_search(self, query, budget_tokens)` |
| `load` | method | `readmenator/_graphrag.py:1257` | `def load(self, project_root)` |
| `local_search` | method | `readmenator/_graphrag.py:1025` | `def local_search(self, query, budget_tokens)` |
| `render_reports` | method | `readmenator/_graphrag.py:1279` | `def render_reports(index)` |
| `resolve_symbol` | function | `readmenator/_graphrag.py:452` | `def resolve_symbol(file_id, name)` |
| `scores` | method | `readmenator/_graphrag.py:298` | `def scores(self, query)` |
| `search` | method | `readmenator/_graphrag.py:1004` | `def search(self, query, mode, budget_tokens)` |
| `to_dict` | method | `readmenator/_graphrag.py:186` | `def to_dict(self)` |
| `tokenize` | function | `readmenator/_graphrag.py:240` | `def tokenize(text, min_len, stopwords)` |
| `write` | method | `readmenator/_graphrag.py:1227` | `def write(self, index, project_root)` |
| `HotspotAnalyzer` | class | `readmenator/_hotspots.py:22` | `class HotspotAnalyzer` |
| `__init__` | method | `readmenator/_hotspots.py:31` | `def __init__(self, config)` |
| `_dfs_visit` | function | `readmenator/_hotspots.py:114` | `def _dfs_visit(current)` |
| `_record_cycle` | function | `readmenator/_hotspots.py:125` | `def _record_cycle(start, end)` |
| `analyze_change_impact` | method | `readmenator/_hotspots.py:155` | `def analyze_change_impact(self, nodes, resolved_edges)` |
| `analyze_hotspots` | method | `readmenator/_hotspots.py:34` | `def analyze_hotspots(self, nodes, edges, resolved_edges)` |
| `detect_cycles` | method | `readmenator/_hotspots.py:90` | `def detect_cycles(self, nodes, resolved_edges)` |
| `compress_text` | function | `readmenator/_htmlpack.py:77` | `def compress_text(text, config)` |
| `escape_json_for_script` | function | `readmenator/_htmlpack.py:49` | `def escape_json_for_script(text, chars)` |
| `payload_script` | function | `readmenator/_htmlpack.py:92` | `def payload_script(element_id, payload, config, compact, escape)` |
| `read_payload_script` | function | `readmenator/_htmlpack.py:119` | `def read_payload_script(document, element_id)` |
| `should_compress` | function | `readmenator/_htmlpack.py:64` | `def should_compress(raw_size, config)` |
| `Hypothesis` | class | `readmenator/_hypotheses.py:25` | `class Hypothesis` |
| `HypothesisValidator` | class | `readmenator/_hypotheses.py:73` | `class HypothesisValidator` |
| `HypothesisVerdict` | class | `readmenator/_hypotheses.py:58` | `class HypothesisVerdict` |
| `__init__` | method | `readmenator/_hypotheses.py:84` | `def __init__(self, known_edges, known_symbols)` |
| `_callee_symbol_match` | function | `readmenator/_hypotheses.py:141` | `def _callee_symbol_match(callee, symbols)` |
| `from_dict` | method | `readmenator/_hypotheses.py:33` | `def from_dict(cls, data)` |
| `to_dict` | method | `readmenator/_hypotheses.py:49` | `def to_dict(self)` |
| `to_dict` | method | `readmenator/_hypotheses.py:64` | `def to_dict(self)` |
| `validate` | method | `readmenator/_hypotheses.py:92` | `def validate(self, hypothesis, allow_assumed)` |
| `validate_json` | method | `readmenator/_hypotheses.py:126` | `def validate_json(self, raw_json, allow_assumed)` |
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
| `ArchitectureLinter` | class | `readmenator/_linter.py:21` | `class ArchitectureLinter` |
| `__init__` | method | `readmenator/_linter.py:34` | `def __init__(self, config)` |
| `_check_circular_dependencies` | method | `readmenator/_linter.py:134` | `def _check_circular_dependencies(self, nodes, resolved_edges)` |
| `_check_cross_layer_violations` | method | `readmenator/_linter.py:103` | `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)` |
| `_check_file_length` | method | `readmenator/_linter.py:72` | `def _check_file_length(self, nodes, content_map)` |
| `_check_unresolved_calls` | method | `readmenator/_linter.py:195` | `def _check_unresolved_calls(self, nodes, edges, resolved_edges, content_map)` |
| `_dfs` | function | `readmenator/_linter.py:153` | `def _dfs(current)` |
| `lint` | method | `readmenator/_linter.py:37` | `def lint(self, nodes, edges, resolved_edges, layers, content_map)` |
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
| `_get_query_engine` | method | `readmenator/_mcp_server.py:1069` | `def _get_query_engine(self, nodes, edges, resolved)` |
| `_handle_call_tool` | method | `readmenator/_mcp_server.py:192` | `def _handle_call_tool(self, req)` |
| `_handle_initialize` | method | `readmenator/_mcp_server.py:173` | `def _handle_initialize(self, req)` |
| `_handle_list_resources` | method | `readmenator/_mcp_server.py:214` | `def _handle_list_resources(self, req)` |
| `_handle_list_tools` | method | `readmenator/_mcp_server.py:187` | `def _handle_list_tools(self, req)` |
| `_handle_read_resource` | method | `readmenator/_mcp_server.py:219` | `def _handle_read_resource(self, req)` |
| `_register_all` | method | `readmenator/_mcp_server.py:285` | `def _register_all(self)` |
| `_resource_analysis` | method | `readmenator/_mcp_server.py:988` | `def _resource_analysis(self)` |
| `_resource_analytics` | method | `readmenator/_mcp_server.py:1063` | `def _resource_analytics(self)` |
| `_resource_concepts` | method | `readmenator/_mcp_server.py:1022` | `def _resource_concepts(self)` |
| `_resource_findings` | method | `readmenator/_mcp_server.py:972` | `def _resource_findings(self)` |
| `_resource_forcegraph` | method | `readmenator/_mcp_server.py:1049` | `def _resource_forcegraph(self)` |
| `_resource_graph` | method | `readmenator/_mcp_server.py:953` | `def _resource_graph(self)` |
| `_resource_graphrag` | method | `readmenator/_mcp_server.py:1055` | `def _resource_graphrag(self)` |
| `_resource_kb` | method | `readmenator/_mcp_server.py:1018` | `def _resource_kb(self)` |
| `_resource_summary` | method | `readmenator/_mcp_server.py:936` | `def _resource_summary(self)` |
| `_scan` | method | `readmenator/_mcp_server.py:590` | `def _scan(self)` |
| `_scan_deep` | method | `readmenator/_mcp_server.py:596` | `def _scan_deep(self)` |
| `_tool_analytics` | method | `readmenator/_mcp_server.py:850` | `def _tool_analytics(self)` |
| `_tool_communities` | method | `readmenator/_mcp_server.py:753` | `def _tool_communities(self)` |
| `_tool_concepts` | method | `readmenator/_mcp_server.py:824` | `def _tool_concepts(self)` |
| `_tool_cycles` | method | `readmenator/_mcp_server.py:742` | `def _tool_cycles(self)` |
| `_tool_explain` | method | `readmenator/_mcp_server.py:647` | `def _tool_explain(self, name)` |
| `_tool_export_json` | method | `readmenator/_mcp_server.py:820` | `def _tool_export_json(self)` |
| `_tool_findings` | method | `readmenator/_mcp_server.py:670` | `def _tool_findings(self, min_severity)` |
| `_tool_forcegraph` | method | `readmenator/_mcp_server.py:900` | `def _tool_forcegraph(self)` |
| `_tool_graphrag` | method | `readmenator/_mcp_server.py:925` | `def _tool_graphrag(self, query, mode, budget_tokens)` |
| `_tool_hotspots` | method | `readmenator/_mcp_server.py:726` | `def _tool_hotspots(self, top_n)` |
| `_tool_layer_violations` | method | `readmenator/_mcp_server.py:786` | `def _tool_layer_violations(self)` |
| `_tool_layers` | method | `readmenator/_mcp_server.py:768` | `def _tool_layers(self)` |
| `_tool_memory` | method | `readmenator/_mcp_server.py:914` | `def _tool_memory(self)` |
| `_tool_near` | method | `readmenator/_mcp_server.py:870` | `def _tool_near(self, query, top_k)` |
| `_tool_path` | method | `readmenator/_mcp_server.py:659` | `def _tool_path(self, symbol_a, symbol_b)` |
| `_tool_provenance` | method | `readmenator/_mcp_server.py:887` | `def _tool_provenance(self)` |
| `_tool_query` | method | `readmenator/_mcp_server.py:642` | `def _tool_query(self, text)` |
| `_tool_rebuild` | method | `readmenator/_mcp_server.py:802` | `def _tool_rebuild(self)` |
| `_tool_remember` | method | `readmenator/_mcp_server.py:918` | `def _tool_remember(self, note, kind)` |
| `_tool_security_summary` | method | `readmenator/_mcp_server.py:700` | `def _tool_security_summary(self)` |
| `_tool_summary` | method | `readmenator/_mcp_server.py:604` | `def _tool_summary(self)` |
| `_tool_taint` | method | `readmenator/_mcp_server.py:705` | `def _tool_taint(self)` |
| `_tool_update` | method | `readmenator/_mcp_server.py:812` | `def _tool_update(self)` |
| `call` | method | `readmenator/_mcp_server.py:115` | `def call(self, arguments)` |
| `definition` | method | `readmenator/_mcp_server.py:108` | `def definition(self)` |
| `definition` | method | `readmenator/_mcp_server.py:134` | `def definition(self)` |
| `dispatch` | method | `readmenator/_mcp_server.py:241` | `def dispatch(self, req)` |
| `error` | method | `readmenator/_mcp_server.py:85` | `def error(self, code, message, data)` |
| `is_notification` | method | `readmenator/_mcp_server.py:79` | `def is_notification(self)` |
| `main` | function | `readmenator/_mcp_server.py:1074` | `def main()` |
| `read` | method | `readmenator/_mcp_server.py:142` | `def read(self)` |
| `register_resource` | method | `readmenator/_mcp_server.py:158` | `def register_resource(self, resource)` |
| `register_tool` | method | `readmenator/_mcp_server.py:155` | `def register_tool(self, tool)` |
| `response` | method | `readmenator/_mcp_server.py:82` | `def response(self, result)` |
| `run` | method | `readmenator/_mcp_server.py:261` | `def run(self)` |
| `DeclaredRule` | class | `readmenator/_memory.py:53` | `class DeclaredRule` |
| `MemoryNote` | class | `readmenator/_memory.py:70` | `class MemoryNote` |
| `ProjectMemory` | class | `readmenator/_memory.py:102` | `class ProjectMemory` |
| `__init__` | method | `readmenator/_memory.py:105` | `def __init__(self, config)` |
| `_categorise` | method | `readmenator/_memory.py:360` | `def _categorise(heading, keywords)` |
| `_count_severe` | method | `readmenator/_memory.py:606` | `def _count_severe(findings)` |
| `_declared_section` | method | `readmenator/_memory.py:512` | `def _declared_section(title, rules, category, measured)` |
| `_deliverable_baselines` | method | `readmenator/_memory.py:559` | `def _deliverable_baselines(self, root, nodes, findings, analysis_v2)` |
| `_is_test` | method | `readmenator/_memory.py:483` | `def _is_test(file_id)` |
| `_log_section` | method | `readmenator/_memory.py:190` | `def _log_section(self, block)` |
| `_notes_block` | method | `readmenator/_memory.py:141` | `def _notes_block(text)` |
| `_pct` | method | `readmenator/_memory.py:601` | `def _pct(part, whole)` |
| `_purpose_section` | method | `readmenator/_memory.py:368` | `def _purpose_section(self, root, nodes, analysis, concept_graph)` |
| `_readme_lead` | method | `readmenator/_memory.py:400` | `def _readme_lead(self, root)` |
| `_risk_section` | method | `readmenator/_memory.py:579` | `def _risk_section(self, analysis, analysis_v2)` |
| `_safe_read` | method | `readmenator/_memory.py:473` | `def _safe_read(self, path)` |
| `_skeleton` | method | `readmenator/_memory.py:182` | `def _skeleton(self)` |
| `_splice` | method | `readmenator/_memory.py:201` | `def _splice(self, document, block)` |
| `_style_baselines` | method | `readmenator/_memory.py:524` | `def _style_baselines(self, nodes, content_map)` |
| `_workflow_section` | method | `readmenator/_memory.py:492` | `def _workflow_section(self, root, nodes)` |
| `_write` | method | `readmenator/_memory.py:209` | `def _write(self, project_root, text)` |
| `build` | method | `readmenator/_memory.py:231` | `def build(self, project_root, nodes, analysis, analysis_v2, findings, concept_graph, content_map)` |
| `detect_commands` | method | `readmenator/_memory.py:419` | `def detect_commands(self, root, nodes)` |
| `extract_rules` | method | `readmenator/_memory.py:291` | `def extract_rules(self, project_root)` |
| `notes` | method | `readmenator/_memory.py:124` | `def notes(self, project_root)` |
| `path` | method | `readmenator/_memory.py:113` | `def path(self, project_root)` |
| `read` | method | `readmenator/_memory.py:117` | `def read(self, project_root)` |
| `remember` | method | `readmenator/_memory.py:149` | `def remember(self, project_root, note, kind, today)` |
| `sanitize_note` | function | `readmenator/_memory.py:84` | `def sanitize_note(text, max_chars)` |
| `write` | method | `readmenator/_memory.py:218` | `def write(self, project_root, generated)` |
| `MermaidRenderer` | class | `readmenator/_mermaid.py:17` | `class MermaidRenderer` |
| `__init__` | method | `readmenator/_mermaid.py:26` | `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style...` |
| `_sanitize_id` | method | `readmenator/_mermaid.py:75` | `def _sanitize_id(node_id)` |
| `render` | method | `readmenator/_mermaid.py:86` | `def render(self, nodes, edges, resolved_edges, analysis)` |
| `AnalysisResult` | class | `readmenator/_models.py:130` | `class AnalysisResult` |
| `AnalysisResultV2` | class | `readmenator/_models.py:284` | `class AnalysisResultV2` |
| `ChangeImpact` | class | `readmenator/_models.py:200` | `class ChangeImpact` |
| `CommunityResult` | class | `readmenator/_models.py:111` | `class CommunityResult` |
| `ConceptGraph` | class | `readmenator/_models.py:442` | `class ConceptGraph` |
| `ConceptNode` | class | `readmenator/_models.py:404` | `class ConceptNode` |
| `ConceptRelation` | class | `readmenator/_models.py:421` | `class ConceptRelation` |
| `DataflowIssue` | class | `readmenator/_models.py:309` | `class DataflowIssue` |
| `DeadCodeReport` | class | `readmenator/_models.py:349` | `class DeadCodeReport` |
| `DependencyCycle` | class | `readmenator/_models.py:187` | `class DependencyCycle` |
| `Edge` | class | `readmenator/_models.py:58` | `class Edge` |
| `HotspotResult` | class | `readmenator/_models.py:217` | `class HotspotResult` |
| `LayerViolation` | class | `readmenator/_models.py:263` | `class LayerViolation` |
| `LinterViolation` | class | `readmenator/_models.py:332` | `class LinterViolation` |
| `Node` | class | `readmenator/_models.py:37` | `class Node` |
| `RefactoringAction` | class | `readmenator/_models.py:366` | `class RefactoringAction` |
| `RefactoringPlan` | class | `readmenator/_models.py:387` | `class RefactoringPlan` |
| `SecurityFinding` | class | `readmenator/_models.py:77` | `class SecurityFinding` |
| `SuggestedRule` | class | `readmenator/_models.py:238` | `class SuggestedRule` |
| `Symbol` | class | `readmenator/_models.py:18` | `class Symbol` |

Next: [SYMBOLS_p3.md](SYMBOLS_p3.md)
