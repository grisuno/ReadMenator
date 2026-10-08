# Symbols (page 2 of 5)
Previous: [SYMBOLS.md](SYMBOLS.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_resource_kb` | method | `readmenator/_mcp_server.py:942` | `def _resource_kb(self)` |
| `_resource_summary` | method | `readmenator/_mcp_server.py:860` | `def _resource_summary(self)` |
| `_scan` | method | `readmenator/_mcp_server.py:532` | `def _scan(self)` |
| `_scan_deep` | method | `readmenator/_mcp_server.py:538` | `def _scan_deep(self)` |
| `_tool_analytics` | method | `readmenator/_mcp_server.py:792` | `def _tool_analytics(self)` |
| `_tool_communities` | method | `readmenator/_mcp_server.py:695` | `def _tool_communities(self)` |
| `_tool_concepts` | method | `readmenator/_mcp_server.py:766` | `def _tool_concepts(self)` |
| `_tool_cycles` | method | `readmenator/_mcp_server.py:684` | `def _tool_cycles(self)` |
| `_tool_explain` | method | `readmenator/_mcp_server.py:589` | `def _tool_explain(self, name)` |
| `_tool_export_json` | method | `readmenator/_mcp_server.py:762` | `def _tool_export_json(self)` |
| `_tool_findings` | method | `readmenator/_mcp_server.py:612` | `def _tool_findings(self, min_severity)` |
| `_tool_forcegraph` | method | `readmenator/_mcp_server.py:842` | `def _tool_forcegraph(self)` |
| `_tool_hotspots` | method | `readmenator/_mcp_server.py:668` | `def _tool_hotspots(self, top_n)` |
| `_tool_layer_violations` | method | `readmenator/_mcp_server.py:728` | `def _tool_layer_violations(self)` |
| `_tool_layers` | method | `readmenator/_mcp_server.py:710` | `def _tool_layers(self)` |
| `_tool_near` | method | `readmenator/_mcp_server.py:812` | `def _tool_near(self, query, top_k)` |
| `_tool_path` | method | `readmenator/_mcp_server.py:601` | `def _tool_path(self, symbol_a, symbol_b)` |
| `_tool_provenance` | method | `readmenator/_mcp_server.py:829` | `def _tool_provenance(self)` |
| `_tool_query` | method | `readmenator/_mcp_server.py:584` | `def _tool_query(self, text)` |
| `_tool_rebuild` | method | `readmenator/_mcp_server.py:744` | `def _tool_rebuild(self)` |
| `_tool_security_summary` | method | `readmenator/_mcp_server.py:642` | `def _tool_security_summary(self)` |
| `_tool_summary` | method | `readmenator/_mcp_server.py:546` | `def _tool_summary(self)` |
| `_tool_taint` | method | `readmenator/_mcp_server.py:647` | `def _tool_taint(self)` |
| `_tool_update` | method | `readmenator/_mcp_server.py:754` | `def _tool_update(self)` |
| `call` | method | `readmenator/_mcp_server.py:115` | `def call(self, arguments)` |
| `definition` | method | `readmenator/_mcp_server.py:108` | `def definition(self)` |
| `definition` | method | `readmenator/_mcp_server.py:134` | `def definition(self)` |
| `dispatch` | method | `readmenator/_mcp_server.py:241` | `def dispatch(self, req)` |
| `error` | method | `readmenator/_mcp_server.py:85` | `def error(self, code, message, data)` |
| `is_notification` | method | `readmenator/_mcp_server.py:79` | `def is_notification(self)` |
| `main` | method | `readmenator/_mcp_server.py:990` | `def main()` |
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
| `TaintAnalysisResult` | class | `readmenator/_models.py:172` | `class TaintAnalysisResult` |
| `TaintPath` | class | `readmenator/_models.py:151` | `class TaintPath` |
| `pluralize_symbol_kind` | method | `readmenator/_models.py:101` | `def pluralize_symbol_kind(kind, plural_map)` |
| `AnalyzerFactory` | class | `readmenator/_pipeline.py:56` | `class AnalyzerFactory` |
| `DeepAnalysisRunner` | class | `readmenator/_pipeline.py:355` | `class DeepAnalysisRunner` |
| `__init__` | method | `readmenator/_pipeline.py:64` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_pipeline.py:364` | `def __init__(self, factory)` |
| `agent_injector` | method | `readmenator/_pipeline.py:207` | `def agent_injector(self)` |
| `agent_output` | method | `readmenator/_pipeline.py:224` | `def agent_output(self)` |
| `analytics` | method | `readmenator/_pipeline.py:286` | `def analytics(self)` |
| `analyzer` | method | `readmenator/_pipeline.py:114` | `def analyzer(self)` |
| `build_typed_graph` | method | `readmenator/_pipeline.py:320` | `def build_typed_graph(self, nodes, edges, resolved_edges)` |
| `concepts` | method | `readmenator/_pipeline.py:272` | `def concepts(self)` |
| `cpg` | method | `readmenator/_pipeline.py:169` | `def cpg(self)` |
| `dataflow` | method | `readmenator/_pipeline.py:138` | `def dataflow(self)` |
| `diagram_builder` | method | `readmenator/_pipeline.py:230` | `def diagram_builder(self)` |
| `diagram_publisher` | method | `readmenator/_pipeline.py:251` | `def diagram_publisher(self)` |
| `diagram_renderer` | method | `readmenator/_pipeline.py:237` | `def diagram_renderer(self)` |
| `diagram_validator` | method | `readmenator/_pipeline.py:244` | `def diagram_validator(self)` |
| `embedder` | method | `readmenator/_pipeline.py:314` | `def embedder(self)` |
| `exclusions` | method | `readmenator/_pipeline.py:307` | `def exclusions(self)` |
| `exporter` | method | `readmenator/_pipeline.py:126` | `def exporter(self)` |
| `forcegraph` | method | `readmenator/_pipeline.py:279` | `def forcegraph(self)` |
| `generator` | method | `readmenator/_pipeline.py:108` | `def generator(self)` |
| `gh_wiki` | method | `readmenator/_pipeline.py:217` | `def gh_wiki(self)` |
| `hotspots` | method | `readmenator/_pipeline.py:145` | `def hotspots(self)` |
| `last_category` | method | `readmenator/_pipeline.py:347` | `def last_category(self)` |
| `last_typed_graph` | method | `readmenator/_pipeline.py:351` | `def last_typed_graph(self)` |
| `layer_detector` | method | `readmenator/_pipeline.py:178` | `def layer_detector(self)` |
| `layer_rules` | method | `readmenator/_pipeline.py:151` | `def layer_rules(self)` |
| `make_ranker` | method | `readmenator/_pipeline.py:330` | `def make_ranker(self, typed_graph)` |
| `provenance` | method | `readmenator/_pipeline.py:300` | `def provenance(self)` |
| `readme_injector` | method | `readmenator/_pipeline.py:197` | `def readme_injector(self)` |
| `rule_gen` | method | `readmenator/_pipeline.py:157` | `def rule_gen(self)` |
| `run` | method | `readmenator/_pipeline.py:367` | `def run(self, nodes, edges, resolved_edges, layers, content_map)` |
| `sarif` | method | `readmenator/_pipeline.py:163` | `def sarif(self)` |
| `scanner` | method | `readmenator/_pipeline.py:102` | `def scanner(self)` |
| `scantext` | method | `readmenator/_pipeline.py:293` | `def scantext(self)` |
| `security` | method | `readmenator/_pipeline.py:120` | `def security(self)` |
| `taint` | method | `readmenator/_pipeline.py:132` | `def taint(self)` |
| `uml` | method | `readmenator/_pipeline.py:184` | `def uml(self)` |
| `video` | method | `readmenator/_pipeline.py:265` | `def video(self)` |
| `vis_renderer` | method | `readmenator/_pipeline.py:258` | `def vis_renderer(self)` |
| `wiki` | method | `readmenator/_pipeline.py:190` | `def wiki(self)` |
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
| `ProvenanceAuditor` | class | `readmenator/_provenance.py:46` | `class ProvenanceAuditor` |
| `ProvenanceFinding` | class | `readmenator/_provenance.py:20` | `class ProvenanceFinding` |
| `__init__` | method | `readmenator/_provenance.py:49` | `def __init__(self, config)` |
| `_attach_frequency` | method | `readmenator/_provenance.py:124` | `def _attach_frequency(self, findings, content_map)` |
| `_corpus_frequency` | method | `readmenator/_provenance.py:153` | `def _corpus_frequency(patterns, rows)` |
| `_snippet_in_content` | method | `readmenator/_provenance.py:115` | `def _snippet_in_content(self, file_path, snippet, content_map)` |
| `audit` | method | `readmenator/_provenance.py:57` | `def audit(self, findings, content_map)` |
| `is_inferred_only` | method | `readmenator/_provenance.py:32` | `def is_inferred_only(self)` |
| `reading` | method | `readmenator/_provenance.py:37` | `def reading(self)` |
| `summary` | method | `readmenator/_provenance.py:98` | `def summary(self, findings)` |
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
| `ScanTextBuilder` | class | `readmenator/_scantext.py:16` | `class ScanTextBuilder` |
| `__init__` | method | `readmenator/_scantext.py:19` | `def __init__(self, config)` |
| `build_corpus` | method | `readmenator/_scantext.py:67` | `def build_corpus(self, nodes, content_map, edges)` |
| `build_for_node` | method | `readmenator/_scantext.py:27` | `def build_for_node(self, node, content, imports)` |
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
| `Fe` | class | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `Ha` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Ia` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `La` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Lo` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Na` | class | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Sr` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `_` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `_n` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `as` | class | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `as` | class | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `b` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `cr` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `e` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `e` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `e` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `f` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `h` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `h` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `i` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `i` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `l` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `o` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `r` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `s` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `s` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `t` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `u` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `wa` | class | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `xo` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `y` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `Backdrop` | class | `readmenator/_video.py:236` | `class Backdrop` |
| `CinematicVideoRenderer` | class | `readmenator/_video.py:431` | `class CinematicVideoRenderer` |
| `__init__` | method | `readmenator/_video.py:239` | `def __init__(self, width, height)` |
| `_build_dep_tree` | method | `readmenator/_video.py:586` | `def _build_dep_tree(self, node_by_id, link_set, god_names)` |
| `_caption_y` | function | `readmenator/_video.py:116` | `def _caption_y(cfg)` |
| `_code_tint` | function | `readmenator/_video.py:172` | `def _code_tint(line)` |
| `_dna_boxes` | function | `readmenator/_video.py:130` | `def _dna_boxes(cfg)` |
| `_draw_frame` | method | `readmenator/_video.py:816` | `def _draw_frame(fi)` |
| `_find` | method | `readmenator/_video.py:201` | `def _find(style)` |
| `_graph_boxes` | function | `readmenator/_video.py:121` | `def _graph_boxes(cfg)` |
| `_img` | method | `readmenator/_video.py:292` | `def _img()` |
| `_packet_offset` | function | `readmenator/_video.py:182` | `def _packet_offset(a, b, k)` |
| `_panel` | function | `readmenator/_video.py:111` | `def _panel(cfg)` |
| `_render_frame_bytes` | method | `readmenator/_video.py:811` | `def _render_frame_bytes(fi)` |
| `_scan_cursor` | function | `readmenator/_video.py:163` | `def _scan_cursor(d, box, progress, col)` |
| `_scene_card` | method | `readmenator/_video.py:879` | `def _scene_card(img, d, lt, gt, sc)` |
| `_scene_communities` | method | `readmenator/_video.py:1035` | `def _scene_communities(img, d, lt, gt, sc)` |
| `_scene_dna` | method | `readmenator/_video.py:1137` | `def _scene_dna(img, d, lt, gt, sc)` |
| `_scene_gods` | method | `readmenator/_video.py:918` | `def _scene_gods(img, d, lt, gt, sc)` |
| `_scene_graph` | method | `readmenator/_video.py:1079` | `def _scene_graph(img, d, lt, gt, sc)` |
| `_scene_layers` | method | `readmenator/_video.py:893` | `def _scene_layers(img, d, lt, gt, sc)` |
| `_scene_outro` | method | `readmenator/_video.py:1196` | `def _scene_outro(img, d, lt, gt, sc)` |
| `_scene_title` | method | `readmenator/_video.py:844` | `def _scene_title(img, d, lt, gt, sc)` |
| `_scene_tree` | method | `readmenator/_video.py:961` | `def _scene_tree(img, d, lt, gt, sc)` |
| `_split_boxes` | function | `readmenator/_video.py:139` | `def _split_boxes(cfg)` |
| `_sun` | method | `readmenator/_video.py:277` | `def _sun(self, r)` |
| `_verdict_badge` | function | `readmenator/_video.py:148` | `def _verdict_badge(d, box, text, fonts, lt, dur, col)` |
| `alpha` | function | `readmenator/_video.py:89` | `def alpha(c, a)` |
| `build_scenes` | method | `readmenator/_video.py:637` | `def build_scenes(self, data)` |
| `chroma_text` | method | `readmenator/_video.py:377` | `def chroma_text(img, xy, text, font, col, spread, anchor)` |
| `collect` | method | `readmenator/_video.py:436` | `def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map...` |
| `dependencies_available` | function | `readmenator/_video.py:188` | `def dependencies_available()` |
| `draw_caption` | method | `readmenator/_video.py:415` | `def draw_caption(d, text, lt, dur, fonts, width, y)` |
| `draw_grid` | method | `readmenator/_video.py:299` | `def draw_grid(img, t, strength, bd)` |
| `draw_header` | method | `readmenator/_video.py:401` | `def draw_header(img, d, gt, total, project, act_label, fonts, width)` |
| `draw_sun` | method | `readmenator/_video.py:319` | `def draw_sun(img, a, bd, cy)` |
| `ease` | function | `readmenator/_video.py:73` | `def ease(x)` |
| `fmt_int` | function | `readmenator/_video.py:79` | `def fmt_int(n)` |
| `glitch_fx` | method | `readmenator/_video.py:354` | `def glitch_fx(img, amount, seed)` |
| `graph_positions` | method | `readmenator/_video.py:663` | `def graph_positions(self, data, box)` |
| `hash_color` | function | `readmenator/_video.py:94` | `def hash_color(digest)` |
| `hud_panel` | method | `readmenator/_video.py:388` | `def hud_panel(d, box, title, fonts, col)` |
| `mix` | function | `readmenator/_video.py:84` | `def mix(a, b, t)` |
| `post` | method | `readmenator/_video.py:336` | `def post(img, glitch, seed)` |
| `render` | method | `readmenator/_video.py:771` | `def render(self, data, output_path)` |
| `render_single_frame` | method | `readmenator/_video.py:753` | `def render_single_frame(self, data, frame_index)` |
| `resolve_fonts` | function | `readmenator/_video.py:197` | `def resolve_fonts()` |
| `short_label` | function | `readmenator/_video.py:103` | `def short_label(text, limit)` |
| `tree_positions` | method | `readmenator/_video.py:710` | `def tree_positions(self, data, box)` |
| `DirectoryWatcher` | class | `readmenator/_watcher.py:21` | `class DirectoryWatcher` |
| `__init__` | method | `readmenator/_watcher.py:29` | `def __init__(self, root, config, callback, interval_seconds)` |
| `_compute_snapshot` | method | `readmenator/_watcher.py:51` | `def _compute_snapshot(self)` |
| `start` | method | `readmenator/_watcher.py:80` | `def start(self)` |
| `stop` | method | `readmenator/_watcher.py:97` | `def stop(self)` |
| `WikiGenerator` | class | `readmenator/_wiki.py:86` | `class WikiGenerator` |
| `__init__` | method | `readmenator/_wiki.py:89` | `def __init__(self, config)` |
| `_build_community_page` | method | `readmenator/_wiki.py:550` | `def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)` |
| `_build_connections` | method | `readmenator/_wiki.py:277` | `def _build_connections(self, communities, resolved, analysis, node_map, layers)` |
| `_build_connections_json` | method | `readmenator/_wiki.py:454` | `def _build_connections_json(self, connections)` |
| `_build_grouped_files` | method | `readmenator/_wiki.py:501` | `def _build_grouped_files(self, members, node_map, layers, max_files)` |
| `_build_index` | method | `readmenator/_wiki.py:754` | `def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections...` |
| `_build_queries` | method | `readmenator/_wiki.py:936` | `def _build_queries(self, analysis)` |
| `_build_report` | method | `readmenator/_wiki.py:961` | `def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name...` |
| `_community_of` | method | `readmenator/_wiki.py:268` | `def _community_of(self, node_id, communities)` |
| `_connective_paragraph` | method | `readmenator/_wiki.py:899` | `def _connective_paragraph(self, communities, connections)` |
| `_definition_for` | method | `readmenator/_wiki.py:458` | `def _definition_for(self, community, node_map)` |
| `_display_names` | function | `readmenator/_wiki.py:72` | `def _display_names(communities)` |
| `_duplicate_links` | method | `readmenator/_wiki.py:342` | `def _duplicate_links(communities, node_map, skip_pairs)` |
| `_estimate_tokens` | method | `readmenator/_wiki.py:1033` | `def _estimate_tokens(self, nodes, connections)` |
| `_file_row` | method | `readmenator/_wiki.py:487` | `def _file_row(self, fid, node_map, layers)` |
| `_is_garbage_purpose` | function | `readmenator/_wiki.py:47` | `def _is_garbage_purpose(text)` |
| `_large_files` | method | `readmenator/_wiki.py:741` | `def _large_files(self, nodes, project_root)` |
| `_overview_paragraph` | method | `readmenator/_wiki.py:866` | `def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)` |
| `_prune_stale_pages` | method | `readmenator/_wiki.py:210` | `def _prune_stale_pages(self, out_dir, current)` |
| `_questions_for` | method | `readmenator/_wiki.py:703` | `def _questions_for(self, community, node_map, member_set, analysis_v2)` |
| `_questions_paragraph` | method | `readmenator/_wiki.py:920` | `def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)` |
| `_resolve_communities` | method | `readmenator/_wiki.py:242` | `def _resolve_communities(self, nodes, analysis, resolved)` |
| `_shared_context` | method | `readmenator/_wiki.py:421` | `def _shared_context(first, second, node_map, layers)` |
| `_shared_context_links` | method | `readmenator/_wiki.py:385` | `def _shared_context_links(self, communities, existing, node_map, layers)` |
| `_slug` | function | `readmenator/_wiki.py:55` | `def _slug(text)` |
| `_write` | method | `readmenator/_wiki.py:1044` | `def _write(path, content)` |
| `_write_concepts` | method | `readmenator/_wiki.py:143` | `def _write_concepts(self, out_dir, analysis_v2)` |
| `dominant` | method | `readmenator/_wiki.py:428` | `def dominant(ids, key)` |
| `existing_ids` | function | `readmenator/_wiki.py:62` | `def existing_ids(connections)` |
| `generate` | method | `readmenator/_wiki.py:94` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)` |
| `lint` | method | `readmenator/_wiki.py:219` | `def lint(self, project_root)` |
| `YaraLiteHit` | class | `readmenator/_yaralite.py:56` | `class YaraLiteHit` |
| `YaraLiteMatch` | class | `readmenator/_yaralite.py:66` | `class YaraLiteMatch` |
| `YaraLiteRule` | class | `readmenator/_yaralite.py:33` | `class YaraLiteRule` |
| `YaraLiteString` | class | `readmenator/_yaralite.py:24` | `class YaraLiteString` |
| `_condition_matches` | method | `readmenator/_yaralite.py:265` | `def _condition_matches(condition, hits)` |
| `_confidence` | method | `readmenator/_yaralite.py:305` | `def _confidence(value)` |
| `_decode_yara_string` | method | `readmenator/_yaralite.py:238` | `def _decode_yara_string(value)` |
| `_excerpt` | method | `readmenator/_yaralite.py:322` | `def _excerpt(text, offset, length)` |
| `_parse_meta` | method | `readmenator/_yaralite.py:196` | `def _parse_meta(meta_body)` |
| `_parse_strings` | method | `readmenator/_yaralite.py:215` | `def _parse_strings(strings_body)` |
| `_rule_blocks` | method | `readmenator/_yaralite.py:161` | `def _rule_blocks(rules_text)` |
| `_section` | method | `readmenator/_yaralite.py:182` | `def _section(body, start_marker, end_marker)` |
| `_string_hits` | method | `readmenator/_yaralite.py:243` | `def _string_hits(text, rule)` |
| `_strip_comments` | method | `readmenator/_yaralite.py:233` | `def _strip_comments(text)` |
| `parse_yaralite_rules` | method | `readmenator/_yaralite.py:76` | `def parse_yaralite_rules(rules_text)` |
| `replace_group` | method | `readmenator/_yaralite.py:270` | `def replace_group(match)` |
| `replace_identifier` | method | `readmenator/_yaralite.py:292` | `def replace_identifier(match)` |
| `run_yaralite_rules` | method | `readmenator/_yaralite.py:112` | `def run_yaralite_rules(text, rules)` |
| `tier` | method | `readmenator/_yaralite.py:42` | `def tier(self)` |
| `validate_yaralite_rules` | method | `readmenator/_yaralite.py:139` | `def validate_yaralite_rules(rules_text)` |
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
| `GitHubClient` | class | `readmenator_orchestrator.py:83` | `class GitHubClient` |
| `Orchestrator` | class | `readmenator_orchestrator.py:366` | `class Orchestrator` |
| `RepositoryProcessor` | class | `readmenator_orchestrator.py:197` | `class RepositoryProcessor` |
| `TestOrchestrator` | class | `readmenator_orchestrator.py:421` | `class TestOrchestrator(TestCase)` |
| `__init__` | method | `readmenator_orchestrator.py:84` | `def __init__(self, config)` |

Next: [SYMBOLS_p3.md](SYMBOLS_p3.md)
