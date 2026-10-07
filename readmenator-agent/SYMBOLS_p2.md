# Symbols (page 2 of 4)
Previous: [SYMBOLS.md](SYMBOLS.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `vis_renderer` | method | `readmenator/_pipeline.py:244` | `def vis_renderer(self)` |
| `wiki` | method | `readmenator/_pipeline.py:176` | `def wiki(self)` |
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
| `_primary_symbol` | function | `readmenator/_purpose.py:116` | `def _primary_symbol(symbols)` |
| `clean_purpose` | function | `readmenator/_purpose.py:43` | `def clean_purpose(text)` |
| `escape_cell` | function | `readmenator/_purpose.py:66` | `def escape_cell(text)` |
| `file_purpose` | function | `readmenator/_purpose.py:140` | `def file_purpose(node, max_chars)` |
| `first_sentence` | function | `readmenator/_purpose.py:98` | `def first_sentence(doc)` |
| `is_garbage_doc` | function | `readmenator/_purpose.py:26` | `def is_garbage_doc(text)` |
| `truncate_words` | function | `readmenator/_purpose.py:78` | `def truncate_words(text, max_chars)` |
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
| `ReadmeInjector` | class | `readmenator/_readme_injector.py:70` | `class ReadmeInjector` |
| `__init__` | method | `readmenator/_readme_injector.py:78` | `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)` |
| `_build_injection` | method | `readmenator/_readme_injector.py:172` | `def _build_injection(self, suffix)` |
| `_extract_current_injection` | method | `readmenator/_readme_injector.py:117` | `def _extract_current_injection(content)` |
| `_find_readme` | method | `readmenator/_readme_injector.py:165` | `def _find_readme(root)` |
| `_remove_old_injection` | method | `readmenator/_readme_injector.py:126` | `def _remove_old_injection(content)` |
| `inject` | method | `readmenator/_readme_injector.py:88` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_readme_injector.py:136` | `def remove(self, project_root)` |
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
| `_resolve_basename_match` | method | `readmenator/_resolver.py:306` | `def _resolve_basename_match(self, import_str)` |
| `_resolve_directory_init` | method | `readmenator/_resolver.py:244` | `def _resolve_directory_init(self, import_str, source_file)` |
| `_resolve_extensionless` | method | `readmenator/_resolver.py:235` | `def _resolve_extensionless(self, import_str, source_file)` |
| `_resolve_include_dirs` | method | `readmenator/_resolver.py:179` | `def _resolve_include_dirs(self, import_str)` |
| `_resolve_module_dotpath` | method | `readmenator/_resolver.py:269` | `def _resolve_module_dotpath(self, import_str)` |
| `_resolve_relative` | method | `readmenator/_resolver.py:199` | `def _resolve_relative(self, import_str, source_file)` |
| `_resolve_root_package` | method | `readmenator/_resolver.py:254` | `def _resolve_root_package(self, import_str)` |
| `_resolve_stem_match` | method | `readmenator/_resolver.py:324` | `def _resolve_stem_match(self, import_str)` |
| `_resolve_suffix_match` | method | `readmenator/_resolver.py:291` | `def _resolve_suffix_match(self, import_str)` |
| `_resolve_verbatim` | method | `readmenator/_resolver.py:217` | `def _resolve_verbatim(self, import_str, source_file)` |
| `_strip_extension` | method | `readmenator/_resolver.py:333` | `def _strip_extension(self, name)` |
| `resolve` | method | `readmenator/_resolver.py:110` | `def resolve(self, import_str, source_file)` |
| `resolve_all` | method | `readmenator/_resolver.py:163` | `def resolve_all(self, import_str, source_file)` |
| `RuleGenerator` | class | `readmenator/_rule_gen.py:14` | `class RuleGenerator` |
| `__init__` | method | `readmenator/_rule_gen.py:90` | `def __init__(self, config)` |
| `_analyze_language` | method | `readmenator/_rule_gen.py:171` | `def _analyze_language(self, lang, nodes, content_map)` |
| `_detect_antipatterns` | method | `readmenator/_rule_gen.py:204` | `def _detect_antipatterns(self, nodes, content_map)` |
| `_group_by_language` | method | `readmenator/_rule_gen.py:161` | `def _group_by_language(self, nodes)` |
| `_infer_language_for_rule` | method | `readmenator/_rule_gen.py:250` | `def _infer_language_for_rule(rule_id)` |
| `_next_rule_id` | method | `readmenator/_rule_gen.py:260` | `def _next_rule_id(self)` |
| `generate` | method | `readmenator/_rule_gen.py:94` | `def generate(self, nodes, content_map)` |
| `write_rules` | method | `readmenator/_rule_gen.py:122` | `def write_rules(self, rules, output_dir)` |
| `SarifExporter` | class | `readmenator/_sarif.py:11` | `class SarifExporter` |
| `__init__` | method | `readmenator/_sarif.py:30` | `def __init__(self, privacy_mode)` |
| `_build_result` | method | `readmenator/_sarif.py:106` | `def _build_result(self, finding, rule_index)` |
| `_build_rule` | method | `readmenator/_sarif.py:82` | `def _build_rule(self, finding)` |
| `export` | method | `readmenator/_sarif.py:33` | `def export(self, findings, project_name)` |
| `PolyglotScanner` | class | `readmenator/_scanner.py:28` | `class PolyglotScanner` |
| `__init__` | method | `readmenator/_scanner.py:39` | `def __init__(self, config)` |
| `_check_directory_depth` | method | `readmenator/_scanner.py:167` | `def _check_directory_depth(self, path, root)` |
| `_emit_progress` | method | `readmenator/_scanner.py:251` | `def _emit_progress(self, count)` |
| `_extract_file_doc` | method | `readmenator/_scanner.py:175` | `def _extract_file_doc(self, content)` |
| `_gitignore_glob_to_regex` | method | `readmenator/_scanner.py:105` | `def _gitignore_glob_to_regex(pattern)` |
| `_is_generated` | method | `readmenator/_scanner.py:57` | `def _is_generated(self, rel_path)` |
| `_is_gitignored` | method | `readmenator/_scanner.py:145` | `def _is_gitignored(self, rel_path)` |
| `_is_ignored` | method | `readmenator/_scanner.py:50` | `def _is_ignored(self, path)` |
| `_load_gitignore` | method | `readmenator/_scanner.py:83` | `def _load_gitignore(self, root)` |
| `_scan_impl` | method | `readmenator/_scanner.py:286` | `def _scan_impl(self, root)` |
| `_validate_path_security` | method | `readmenator/_scanner.py:154` | `def _validate_path_security(self, path)` |
| `scan` | method | `readmenator/_scanner.py:261` | `def scan(self, root)` |
| `scan_with_content` | method | `readmenator/_scanner.py:275` | `def scan_with_content(self, root)` |
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
| `TaintAnalyzer` | class | `readmenator/_taint.py:12` | `class TaintAnalyzer` |
| `__init__` | method | `readmenator/_taint.py:73` | `def __init__(self, config)` |
| `_build_forward_graph` | method | `readmenator/_taint.py:213` | `def _build_forward_graph(nodes, resolved_edges)` |
| `_find_direct_sources` | method | `readmenator/_taint.py:136` | `def _find_direct_sources(self, nodes, edges)` |
| `_propagate` | method | `readmenator/_taint.py:162` | `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` |
| `analyze` | method | `readmenator/_taint.py:77` | `def analyze(self, nodes, edges, resolved_edges)` |
| `UmlGenerator` | class | `readmenator/_uml.py:34` | `class UmlGenerator` |
| `__init__` | method | `readmenator/_uml.py:36` | `def __init__(self, config)` |
| `_cpp_params` | method | `readmenator/_uml.py:259` | `def _cpp_params(params)` |
| `_cs_params` | method | `readmenator/_uml.py:345` | `def _cs_params(params)` |
| `_extract_params` | method | `readmenator/_uml.py:592` | `def _extract_params(signature)` |
| `_find_node` | method | `readmenator/_uml.py:165` | `def _find_node(nodes, node_id)` |
| `_generate_cpp` | method | `readmenator/_uml.py:233` | `def _generate_cpp(class_symbols, nodes, edges)` |
| `_generate_csharp` | method | `readmenator/_uml.py:316` | `def _generate_csharp(class_symbols, nodes, edges)` |
| `_generate_dart` | method | `readmenator/_uml.py:547` | `def _generate_dart(class_symbols, nodes, edges)` |
| `_generate_go` | method | `readmenator/_uml.py:395` | `def _generate_go(class_symbols, nodes, edges)` |
| `_generate_java` | method | `readmenator/_uml.py:274` | `def _generate_java(class_symbols, nodes, edges)` |
| `_generate_kotlin` | method | `readmenator/_uml.py:476` | `def _generate_kotlin(class_symbols, nodes, edges)` |
| `_generate_php` | method | `readmenator/_uml.py:448` | `def _generate_php(class_symbols, nodes, edges)` |
| `_generate_python` | method | `readmenator/_uml.py:360` | `def _generate_python(class_symbols, nodes, edges)` |
| `_generate_ruby` | method | `readmenator/_uml.py:567` | `def _generate_ruby(class_symbols, nodes, edges)` |
| `_generate_rust` | method | `readmenator/_uml.py:422` | `def _generate_rust(class_symbols, nodes, edges)` |
| `_generate_scala` | method | `readmenator/_uml.py:496` | `def _generate_scala(class_symbols, nodes, edges)` |
| `_generate_swift` | method | `readmenator/_uml.py:518` | `def _generate_swift(class_symbols, nodes, edges)` |
| `_get_code_generator` | method | `readmenator/_uml.py:172` | `def _get_code_generator(language)` |
| `_java_params` | method | `readmenator/_uml.py:301` | `def _java_params(params)` |
| `_safe_name` | method | `readmenator/_uml.py:588` | `def _safe_name(name)` |
| `_sanitize_id` | method | `readmenator/_uml.py:153` | `def _sanitize_id(raw)` |
| `_type_map_py_to_target` | method | `readmenator/_uml.py:190` | `def _type_map_py_to_target(target, py_type_hint)` |
| `generate_code` | method | `readmenator/_uml.py:129` | `def generate_code(self, nodes, edges, target_language)` |
| `render_mermaid_class_diagram` | method | `readmenator/_uml.py:39` | `def render_mermaid_class_diagram(self, nodes, edges)` |
| `Backdrop` | class | `readmenator/_video.py:236` | `class Backdrop` |
| `CinematicVideoRenderer` | class | `readmenator/_video.py:431` | `class CinematicVideoRenderer` |
| `__init__` | method | `readmenator/_video.py:239` | `def __init__(self, width, height)` |
| `_build_dep_tree` | method | `readmenator/_video.py:572` | `def _build_dep_tree(self, node_by_id, link_set, god_names)` |
| `_caption_y` | function | `readmenator/_video.py:116` | `def _caption_y(cfg)` |
| `_code_tint` | function | `readmenator/_video.py:172` | `def _code_tint(line)` |
| `_dna_boxes` | function | `readmenator/_video.py:130` | `def _dna_boxes(cfg)` |
| `_draw_frame` | method | `readmenator/_video.py:802` | `def _draw_frame(fi)` |
| `_find` | method | `readmenator/_video.py:201` | `def _find(style)` |
| `_graph_boxes` | function | `readmenator/_video.py:121` | `def _graph_boxes(cfg)` |
| `_img` | method | `readmenator/_video.py:292` | `def _img()` |
| `_packet_offset` | function | `readmenator/_video.py:182` | `def _packet_offset(a, b, k)` |
| `_panel` | function | `readmenator/_video.py:111` | `def _panel(cfg)` |
| `_render_frame_bytes` | method | `readmenator/_video.py:797` | `def _render_frame_bytes(fi)` |
| `_scan_cursor` | function | `readmenator/_video.py:163` | `def _scan_cursor(d, box, progress, col)` |
| `_scene_card` | method | `readmenator/_video.py:865` | `def _scene_card(img, d, lt, gt, sc)` |
| `_scene_communities` | method | `readmenator/_video.py:1021` | `def _scene_communities(img, d, lt, gt, sc)` |
| `_scene_dna` | method | `readmenator/_video.py:1123` | `def _scene_dna(img, d, lt, gt, sc)` |
| `_scene_gods` | method | `readmenator/_video.py:904` | `def _scene_gods(img, d, lt, gt, sc)` |
| `_scene_graph` | method | `readmenator/_video.py:1065` | `def _scene_graph(img, d, lt, gt, sc)` |
| `_scene_layers` | method | `readmenator/_video.py:879` | `def _scene_layers(img, d, lt, gt, sc)` |
| `_scene_outro` | method | `readmenator/_video.py:1182` | `def _scene_outro(img, d, lt, gt, sc)` |
| `_scene_title` | method | `readmenator/_video.py:830` | `def _scene_title(img, d, lt, gt, sc)` |
| `_scene_tree` | method | `readmenator/_video.py:947` | `def _scene_tree(img, d, lt, gt, sc)` |
| `_split_boxes` | function | `readmenator/_video.py:139` | `def _split_boxes(cfg)` |
| `_sun` | method | `readmenator/_video.py:277` | `def _sun(self, r)` |
| `_verdict_badge` | function | `readmenator/_video.py:148` | `def _verdict_badge(d, box, text, fonts, lt, dur, col)` |
| `alpha` | function | `readmenator/_video.py:89` | `def alpha(c, a)` |
| `build_scenes` | method | `readmenator/_video.py:623` | `def build_scenes(self, data)` |
| `chroma_text` | method | `readmenator/_video.py:377` | `def chroma_text(img, xy, text, font, col, spread, anchor)` |
| `collect` | method | `readmenator/_video.py:436` | `def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map)` |
| `dependencies_available` | function | `readmenator/_video.py:188` | `def dependencies_available()` |
| `draw_caption` | method | `readmenator/_video.py:415` | `def draw_caption(d, text, lt, dur, fonts, width, y)` |
| `draw_grid` | method | `readmenator/_video.py:299` | `def draw_grid(img, t, strength, bd)` |
| `draw_header` | method | `readmenator/_video.py:401` | `def draw_header(img, d, gt, total, project, act_label, fonts, width)` |
| `draw_sun` | method | `readmenator/_video.py:319` | `def draw_sun(img, a, bd, cy)` |
| `ease` | function | `readmenator/_video.py:73` | `def ease(x)` |
| `fmt_int` | function | `readmenator/_video.py:79` | `def fmt_int(n)` |
| `glitch_fx` | method | `readmenator/_video.py:354` | `def glitch_fx(img, amount, seed)` |
| `graph_positions` | method | `readmenator/_video.py:649` | `def graph_positions(self, data, box)` |
| `hash_color` | function | `readmenator/_video.py:94` | `def hash_color(digest)` |
| `hud_panel` | method | `readmenator/_video.py:388` | `def hud_panel(d, box, title, fonts, col)` |
| `mix` | function | `readmenator/_video.py:84` | `def mix(a, b, t)` |
| `post` | method | `readmenator/_video.py:336` | `def post(img, glitch, seed)` |
| `render` | method | `readmenator/_video.py:757` | `def render(self, data, output_path)` |
| `render_single_frame` | method | `readmenator/_video.py:739` | `def render_single_frame(self, data, frame_index)` |
| `resolve_fonts` | function | `readmenator/_video.py:197` | `def resolve_fonts()` |
| `short_label` | function | `readmenator/_video.py:103` | `def short_label(text, limit)` |
| `tree_positions` | method | `readmenator/_video.py:696` | `def tree_positions(self, data, box)` |
| `DirectoryWatcher` | class | `readmenator/_watcher.py:21` | `class DirectoryWatcher` |
| `__init__` | method | `readmenator/_watcher.py:29` | `def __init__(self, root, config, callback, interval_seconds)` |
| `_compute_snapshot` | method | `readmenator/_watcher.py:51` | `def _compute_snapshot(self)` |
| `start` | method | `readmenator/_watcher.py:80` | `def start(self)` |
| `stop` | method | `readmenator/_watcher.py:97` | `def stop(self)` |
| `WikiGenerator` | class | `readmenator/_wiki.py:86` | `class WikiGenerator` |
| `__init__` | method | `readmenator/_wiki.py:89` | `def __init__(self, config)` |
| `_build_community_page` | method | `readmenator/_wiki.py:482` | `def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)` |
| `_build_connections` | method | `readmenator/_wiki.py:209` | `def _build_connections(self, communities, resolved, analysis, node_map, layers)` |
| `_build_connections_json` | method | `readmenator/_wiki.py:386` | `def _build_connections_json(self, connections)` |
| `_build_grouped_files` | method | `readmenator/_wiki.py:433` | `def _build_grouped_files(self, members, node_map, layers, max_files)` |
| `_build_index` | method | `readmenator/_wiki.py:686` | `def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections...` |
| `_build_queries` | method | `readmenator/_wiki.py:868` | `def _build_queries(self, analysis)` |
| `_build_report` | method | `readmenator/_wiki.py:893` | `def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name...` |
| `_community_of` | method | `readmenator/_wiki.py:200` | `def _community_of(self, node_id, communities)` |
| `_connective_paragraph` | method | `readmenator/_wiki.py:831` | `def _connective_paragraph(self, communities, connections)` |
| `_definition_for` | method | `readmenator/_wiki.py:390` | `def _definition_for(self, community, node_map)` |
| `_display_names` | function | `readmenator/_wiki.py:72` | `def _display_names(communities)` |
| `_duplicate_links` | method | `readmenator/_wiki.py:274` | `def _duplicate_links(communities, node_map, skip_pairs)` |
| `_estimate_tokens` | method | `readmenator/_wiki.py:965` | `def _estimate_tokens(self, nodes, connections)` |
| `_file_row` | method | `readmenator/_wiki.py:419` | `def _file_row(self, fid, node_map, layers)` |
| `_is_garbage_purpose` | function | `readmenator/_wiki.py:47` | `def _is_garbage_purpose(text)` |
| `_large_files` | method | `readmenator/_wiki.py:673` | `def _large_files(self, nodes, project_root)` |
| `_overview_paragraph` | method | `readmenator/_wiki.py:798` | `def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)` |
| `_prune_stale_pages` | method | `readmenator/_wiki.py:142` | `def _prune_stale_pages(self, out_dir, current)` |
| `_questions_for` | method | `readmenator/_wiki.py:635` | `def _questions_for(self, community, node_map, member_set, analysis_v2)` |
| `_questions_paragraph` | method | `readmenator/_wiki.py:852` | `def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)` |
| `_resolve_communities` | method | `readmenator/_wiki.py:174` | `def _resolve_communities(self, nodes, analysis, resolved)` |
| `_shared_context` | method | `readmenator/_wiki.py:353` | `def _shared_context(first, second, node_map, layers)` |
| `_shared_context_links` | method | `readmenator/_wiki.py:317` | `def _shared_context_links(self, communities, existing, node_map, layers)` |
| `_slug` | function | `readmenator/_wiki.py:55` | `def _slug(text)` |
| `_write` | method | `readmenator/_wiki.py:976` | `def _write(path, content)` |
| `dominant` | method | `readmenator/_wiki.py:360` | `def dominant(ids, key)` |
| `existing_ids` | function | `readmenator/_wiki.py:62` | `def existing_ids(connections)` |
| `generate` | method | `readmenator/_wiki.py:94` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)` |
| `lint` | method | `readmenator/_wiki.py:151` | `def lint(self, project_root)` |
| `_init_parser_map` | function | `readmenator/parsers/__init__.py:34` | `def _init_parser_map()` |
| `create_parser` | function | `readmenator/parsers/__init__.py:70` | `def create_parser(extension, filename, config)` |
| `AssemblyParser` | class | `readmenator/parsers/_assembly.py:11` | `class AssemblyParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_assembly.py:19` | `def _extract_specifics(self, content)` |
| `LanguageParser` | class | `readmenator/parsers/_base.py:12` | `class LanguageParser` |
| `__init__` | method | `readmenator/parsers/_base.py:21` | `def __init__(self, filename, config)` |
| `_extract_docstring` | method | `readmenator/parsers/_base.py:49` | `def _extract_docstring(self, line_num)` |
| `_extract_signature` | method | `readmenator/parsers/_base.py:91` | `def _extract_signature(self, content, match_start, pattern)` |
| `_extract_specifics` | method | `readmenator/parsers/_base.py:45` | `def _extract_specifics(self, content)` |
| `parse` | method | `readmenator/parsers/_base.py:36` | `def parse(self, content)` |
| `CParser` | class | `readmenator/parsers/_c.py:30` | `class CParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_c.py:37` | `def _extract_specifics(self, content)` |
| `_has_type_prefix` | function | `readmenator/parsers/_c.py:18` | `def _has_type_prefix(prefix)` |
| `CSharpParser` | class | `readmenator/parsers/_csharp.py:11` | `class CSharpParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_csharp.py:18` | `def _extract_specifics(self, content)` |
| `DartParser` | class | `readmenator/parsers/_dart.py:11` | `class DartParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_dart.py:18` | `def _extract_specifics(self, content)` |
| `ElixirParser` | class | `readmenator/parsers/_elixir.py:11` | `class ElixirParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_elixir.py:18` | `def _extract_specifics(self, content)` |
| `GDScriptParser` | class | `readmenator/parsers/_gdscript.py:11` | `class GDScriptParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_gdscript.py:18` | `def _extract_specifics(self, content)` |
| `GoParser` | class | `readmenator/parsers/_go.py:11` | `class GoParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_go.py:18` | `def _extract_specifics(self, content)` |
| `JavaParser` | class | `readmenator/parsers/_java.py:11` | `class JavaParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_java.py:18` | `def _extract_specifics(self, content)` |
| `JavaScriptParser` | class | `readmenator/parsers/_javascript.py:11` | `class JavaScriptParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_javascript.py:19` | `def _extract_specifics(self, content)` |
| `KotlinParser` | class | `readmenator/parsers/_kotlin.py:11` | `class KotlinParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_kotlin.py:18` | `def _extract_specifics(self, content)` |
| `LuaParser` | class | `readmenator/parsers/_lua.py:11` | `class LuaParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_lua.py:18` | `def _extract_specifics(self, content)` |
| `NimParser` | class | `readmenator/parsers/_nim.py:11` | `class NimParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_nim.py:18` | `def _extract_specifics(self, content)` |
| `PHPParser` | class | `readmenator/parsers/_php.py:11` | `class PHPParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_php.py:18` | `def _extract_specifics(self, content)` |
| `PythonParser` | class | `readmenator/parsers/_python.py:12` | `class PythonParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_python.py:19` | `def _extract_specifics(self, content)` |
| `RubyParser` | class | `readmenator/parsers/_ruby.py:11` | `class RubyParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_ruby.py:18` | `def _extract_specifics(self, content)` |
| `RustParser` | class | `readmenator/parsers/_rust.py:11` | `class RustParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_rust.py:18` | `def _extract_specifics(self, content)` |
| `ScalaParser` | class | `readmenator/parsers/_scala.py:11` | `class ScalaParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_scala.py:18` | `def _extract_specifics(self, content)` |
| `ShellParser` | class | `readmenator/parsers/_shell.py:11` | `class ShellParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_shell.py:18` | `def _extract_specifics(self, content)` |
| `SwiftParser` | class | `readmenator/parsers/_swift.py:11` | `class SwiftParser(LanguageParser)` |
| `_extract_specifics` | method | `readmenator/parsers/_swift.py:18` | `def _extract_specifics(self, content)` |
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
| `TestAgentOutputBudget` | class | `tests/test_agent_friendliness.py:55` | `class TestAgentOutputBudget(TestCase)` |
| `TestAgentOutputSignal` | class | `tests/test_agent_friendliness.py:110` | `class TestAgentOutputSignal(TestCase)` |
| `TestCommunityHubDamping` | class | `tests/test_agent_friendliness.py:308` | `class TestCommunityHubDamping(TestCase)` |
| `TestCommunityShaping` | class | `tests/test_agent_friendliness.py:363` | `class TestCommunityShaping(TestCase)` |
| `TestGalleryIndex` | class | `tests/test_agent_friendliness.py:456` | `class TestGalleryIndex(TestCase)` |
| `TestLiveMapCommunities` | class | `tests/test_agent_friendliness.py:501` | `class TestLiveMapCommunities(TestCase)` |
| `TestLlmsTxt` | class | `tests/test_agent_friendliness.py:281` | `class TestLlmsTxt(TestCase)` |
| `TestLouvainCommunities` | class | `tests/test_agent_friendliness.py:411` | `class TestLouvainCommunities(TestCase)` |
| `TestManifestFreshness` | class | `tests/test_agent_friendliness.py:199` | `class TestManifestFreshness(TestCase)` |
| `TestNoiseReduction` | class | `tests/test_agent_friendliness.py:244` | `class TestNoiseReduction(TestCase)` |
| `TestPurposeExtraction` | class | `tests/test_agent_friendliness.py:176` | `class TestPurposeExtraction(TestCase)` |
| `TestSiteDocsPruning` | class | `tests/test_agent_friendliness.py:394` | `class TestSiteDocsPruning(TestCase)` |
| `TestSourceFreshness` | class | `tests/test_agent_friendliness.py:329` | `class TestSourceFreshness(TestCase)` |
| `_big_project` | function | `tests/test_agent_friendliness.py:34` | `def _big_project(files, symbols_per_file)` |
| `_edge` | function | `tests/test_agent_friendliness.py:29` | `def _edge(source, target, relation)` |
| `_entries` | method | `tests/test_agent_friendliness.py:459` | `def _entries(self)` |
| `_git_repo` | method | `tests/test_agent_friendliness.py:202` | `def _git_repo(self, root, packed)` |
| `_inputs` | method | `tests/test_agent_friendliness.py:504` | `def _inputs(self)` |
| `_node` | function | `tests/test_agent_friendliness.py:21` | `def _node(node_id, doc, symbols)` |
| `_two_cliques` | method | `tests/test_agent_friendliness.py:414` | `def _two_cliques(self)` |
| `test_agent_output_pages_repeat_table_header_and_link_next` | method | `tests/test_agent_friendliness.py:84` | `def test_agent_output_pages_repeat_table_header_and_link_next(self)` |
| `test_agent_output_pages_respect_line_cap_on_large_projects` | method | `tests/test_agent_friendliness.py:58` | `def test_agent_output_pages_respect_line_cap_on_large_projects(self)` |
| `test_agent_output_pagination_keeps_every_symbol_greppable` | method | `tests/test_agent_friendliness.py:71` | `def test_agent_output_pagination_keeps_every_symbol_greppable(self)` |
| `test_agent_output_prunes_stale_pages` | method | `tests/test_agent_friendliness.py:96` | `def test_agent_output_prunes_stale_pages(self)` |
| `test_api_qualifies_methods_with_owner_class` | method | `tests/test_agent_friendliness.py:136` | `def test_api_qualifies_methods_with_owner_class(self)` |
| `test_api_skips_private_helpers_and_test_layer` | method | `tests/test_agent_friendliness.py:122` | `def test_api_skips_private_helpers_and_test_layer(self)` |
| `test_api_states_dependencies_once_per_file` | method | `tests/test_agent_friendliness.py:113` | `def test_api_states_dependencies_once_per_file(self)` |
| `test_architecture_external_excludes_internally_resolved_imports` | method | `tests/test_agent_friendliness.py:144` | `def test_architecture_external_excludes_internally_resolved_imports(self)` |
| `test_built_maps_carry_community_and_core_role` | method | `tests/test_agent_friendliness.py:520` | `def test_built_maps_carry_community_and_core_role(self)` |
| `test_check_freshness_detects_source_edits` | method | `tests/test_agent_friendliness.py:343` | `def test_check_freshness_detects_source_edits(self)` |
| `test_communities_survive_a_shared_hub` | method | `tests/test_agent_friendliness.py:311` | `def test_communities_survive_a_shared_hub(self)` |
| `test_community_label_ignores_test_directory` | method | `tests/test_agent_friendliness.py:446` | `def test_community_label_ignores_test_directory(self)` |
| `test_doc_preview_skips_markdown_syntax` | method | `tests/test_agent_friendliness.py:494` | `def test_doc_preview_skips_markdown_syntax(self)` |
| `test_fingerprint_changes_with_content_not_with_order` | method | `tests/test_agent_friendliness.py:332` | `def test_fingerprint_changes_with_content_not_with_order(self)` |
| `test_gallery_groups_docs_and_collapses_pages` | method | `tests/test_agent_friendliness.py:470` | `def test_gallery_groups_docs_and_collapses_pages(self)` |
| `test_gallery_has_no_external_resources_and_escapes_titles` | method | `tests/test_agent_friendliness.py:486` | `def test_gallery_has_no_external_resources_and_escapes_titles(self)` |
| `test_gallery_video_has_poster_and_start_here` | method | `tests/test_agent_friendliness.py:480` | `def test_gallery_video_has_poster_and_start_here(self)` |
| `test_gitmeta_outside_repository_is_empty` | method | `tests/test_agent_friendliness.py:220` | `def test_gitmeta_outside_repository_is_empty(self)` |
| `test_gitmeta_reads_loose_and_packed_refs` | method | `tests/test_agent_friendliness.py:214` | `def test_gitmeta_reads_loose_and_packed_refs(self)` |
| `test_gotchas_exclude_test_layer_and_report_blast_radius` | method | `tests/test_agent_friendliness.py:161` | `def test_gotchas_exclude_test_layer_and_report_blast_radius(self)` |
| `test_index_reports_used_by_count_and_escapes_pipes` | method | `tests/test_agent_friendliness.py:153` | `def test_index_reports_used_by_count_and_escapes_pipes(self)` |
| `test_layers_match_whole_words_not_substrings` | method | `tests/test_agent_friendliness.py:264` | `def test_layers_match_whole_words_not_substrings(self)` |
| `test_layers_test_framework_import_needs_test_path` | method | `tests/test_agent_friendliness.py:272` | `def test_layers_test_framework_import_needs_test_path(self)` |
| `test_llms_txt_lists_wiki_before_agent_docs` | method | `tests/test_agent_friendliness.py:284` | `def test_llms_txt_lists_wiki_before_agent_docs(self)` |
| `test_louvain_is_deterministic_and_numbered_by_size` | method | `tests/test_agent_friendliness.py:435` | `def test_louvain_is_deterministic_and_numbered_by_size(self)` |
| `test_louvain_splits_bridged_cliques` | method | `tests/test_agent_friendliness.py:426` | `def test_louvain_splits_bridged_cliques(self)` |
| `test_manifest_has_commit_relative_root_and_inventory` | method | `tests/test_agent_friendliness.py:224` | `def test_manifest_has_commit_relative_root_and_inventory(self)` |
| `test_publish_assets_prunes_stale_markdown` | method | `tests/test_agent_friendliness.py:397` | `def test_publish_assets_prunes_stale_markdown(self)` |
| `test_publish_writes_llms_txt` | method | `tests/test_agent_friendliness.py:296` | `def test_publish_writes_llms_txt(self)` |
| `test_purpose_falls_back_to_primary_public_symbol` | method | `tests/test_agent_friendliness.py:185` | `def test_purpose_falls_back_to_primary_public_symbol(self)` |
| `test_purpose_skips_banners_and_spdx` | method | `tests/test_agent_friendliness.py:182` | `def test_purpose_skips_banners_and_spdx(self)` |
| `test_purpose_takes_first_sentence` | method | `tests/test_agent_friendliness.py:179` | `def test_purpose_takes_first_sentence(self)` |
| `test_purpose_truncates_on_word_boundary` | method | `tests/test_agent_friendliness.py:192` | `def test_purpose_truncates_on_word_boundary(self)` |
| `test_resolver_prefers_root_package_over_launcher_shim` | method | `tests/test_agent_friendliness.py:260` | `def test_resolver_prefers_root_package_over_launcher_shim(self)` |
| `test_scanner_skips_own_generated_outputs` | method | `tests/test_agent_friendliness.py:247` | `def test_scanner_skips_own_generated_outputs(self)` |
| `test_shared_directory_labels_use_core_file` | method | `tests/test_agent_friendliness.py:380` | `def test_shared_directory_labels_use_core_file(self)` |
| `test_small_community_merges_into_best_connected_neighbor` | method | `tests/test_agent_friendliness.py:366` | `def test_small_community_merges_into_best_connected_neighbor(self)` |
| `test_vis_render_includes_legend_and_dot_scaling` | method | `tests/test_agent_friendliness.py:529` | `def test_vis_render_includes_legend_and_dot_scaling(self)` |
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

Next: [SYMBOLS_p3.md](SYMBOLS_p3.md)
