# Symbols (page 3 of 7)
Previous: [SYMBOLS_p2.md](SYMBOLS_p2.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `TaintAnalysisResult` | class | `readmenator/_models.py:172` | `class TaintAnalysisResult` |
| `TaintPath` | class | `readmenator/_models.py:151` | `class TaintPath` |
| `pluralize_symbol_kind` | function | `readmenator/_models.py:101` | `def pluralize_symbol_kind(kind, plural_map)` |
| `OllamaClient` | class | `readmenator/_ollama.py:33` | `class OllamaClient` |
| `__init__` | method | `readmenator/_ollama.py:36` | `def __init__(self, config)` |
| `available` | method | `readmenator/_ollama.py:48` | `def available(self, timeout)` |
| `describe_component` | method | `readmenator/_ollama.py:104` | `def describe_component(self, name, files, symbols, imports)` |
| `enabled` | method | `readmenator/_ollama.py:44` | `def enabled(self)` |
| `generate` | method | `readmenator/_ollama.py:69` | `def generate(self, prompt, system)` |
| `strip_thinking` | function | `readmenator/_ollama.py:21` | `def strip_thinking(text)` |
| `AnalyzerFactory` | class | `readmenator/_pipeline.py:67` | `class AnalyzerFactory` |
| `DeepAnalysisRunner` | class | `readmenator/_pipeline.py:484` | `class DeepAnalysisRunner` |
| `__init__` | method | `readmenator/_pipeline.py:75` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_pipeline.py:493` | `def __init__(self, factory)` |
| `agent_injector` | method | `readmenator/_pipeline.py:249` | `def agent_injector(self)` |
| `agent_output` | method | `readmenator/_pipeline.py:269` | `def agent_output(self)` |
| `analytics` | method | `readmenator/_pipeline.py:338` | `def analytics(self)` |
| `analyzer` | method | `readmenator/_pipeline.py:137` | `def analyzer(self)` |
| `apidocs` | method | `readmenator/_pipeline.py:429` | `def apidocs(self)` |
| `apidocs_writer` | method | `readmenator/_pipeline.py:436` | `def apidocs_writer(self)` |
| `build_typed_graph` | method | `readmenator/_pipeline.py:449` | `def build_typed_graph(self, nodes, edges, resolved_edges)` |
| `bundlegraph` | method | `readmenator/_pipeline.py:331` | `def bundlegraph(self)` |
| `components` | method | `readmenator/_pipeline.py:415` | `def components(self)` |
| `concepts` | method | `readmenator/_pipeline.py:317` | `def concepts(self)` |
| `cpg` | method | `readmenator/_pipeline.py:192` | `def cpg(self)` |
| `dataflow` | method | `readmenator/_pipeline.py:161` | `def dataflow(self)` |
| `diagram_builder` | method | `readmenator/_pipeline.py:275` | `def diagram_builder(self)` |
| `diagram_publisher` | method | `readmenator/_pipeline.py:296` | `def diagram_publisher(self)` |
| `diagram_renderer` | method | `readmenator/_pipeline.py:282` | `def diagram_renderer(self)` |
| `diagram_validator` | method | `readmenator/_pipeline.py:289` | `def diagram_validator(self)` |
| `embedder` | method | `readmenator/_pipeline.py:366` | `def embedder(self)` |
| `exclusions` | method | `readmenator/_pipeline.py:359` | `def exclusions(self)` |
| `exporter` | method | `readmenator/_pipeline.py:149` | `def exporter(self)` |
| `folder_readme` | method | `readmenator/_pipeline.py:422` | `def folder_readme(self)` |
| `forcegraph` | method | `readmenator/_pipeline.py:324` | `def forcegraph(self)` |
| `generator` | method | `readmenator/_pipeline.py:131` | `def generator(self)` |
| `gh_wiki` | method | `readmenator/_pipeline.py:262` | `def gh_wiki(self)` |
| `graphrag` | method | `readmenator/_pipeline.py:373` | `def graphrag(self)` |
| `graphrag_store` | method | `readmenator/_pipeline.py:380` | `def graphrag_store(self)` |
| `hotspots` | method | `readmenator/_pipeline.py:168` | `def hotspots(self)` |
| `last_category` | method | `readmenator/_pipeline.py:476` | `def last_category(self)` |
| `last_typed_graph` | method | `readmenator/_pipeline.py:480` | `def last_typed_graph(self)` |
| `layer_detector` | method | `readmenator/_pipeline.py:201` | `def layer_detector(self)` |
| `layer_rules` | method | `readmenator/_pipeline.py:174` | `def layer_rules(self)` |
| `make_ranker` | method | `readmenator/_pipeline.py:459` | `def make_ranker(self, typed_graph)` |
| `memory` | method | `readmenator/_pipeline.py:387` | `def memory(self)` |
| `ollama` | method | `readmenator/_pipeline.py:443` | `def ollama(self)` |
| `provenance` | method | `readmenator/_pipeline.py:352` | `def provenance(self)` |
| `readme_injector` | method | `readmenator/_pipeline.py:220` | `def readme_injector(self)` |
| `rule_gen` | method | `readmenator/_pipeline.py:180` | `def rule_gen(self)` |
| `run` | method | `readmenator/_pipeline.py:496` | `def run(self, nodes, edges, resolved_edges, layers, content_map)` |
| `sarif` | method | `readmenator/_pipeline.py:186` | `def sarif(self)` |
| `scanner` | method | `readmenator/_pipeline.py:125` | `def scanner(self)` |
| `scantext` | method | `readmenator/_pipeline.py:345` | `def scantext(self)` |
| `security` | method | `readmenator/_pipeline.py:143` | `def security(self)` |
| `skills` | method | `readmenator/_pipeline.py:394` | `def skills(self)` |
| `sourceview` | method | `readmenator/_pipeline.py:401` | `def sourceview(self)` |
| `symindex` | method | `readmenator/_pipeline.py:408` | `def symindex(self)` |
| `taint` | method | `readmenator/_pipeline.py:155` | `def taint(self)` |
| `uml` | method | `readmenator/_pipeline.py:207` | `def uml(self)` |
| `video` | method | `readmenator/_pipeline.py:310` | `def video(self)` |
| `vis_renderer` | method | `readmenator/_pipeline.py:303` | `def vis_renderer(self)` |
| `wiki` | method | `readmenator/_pipeline.py:213` | `def wiki(self)` |
| `_coerce` | function | `readmenator/_project_config.py:492` | `def _coerce(field_name, value, default)` |
| `_field_types` | function | `readmenator/_project_config.py:484` | `def _field_types()` |
| `_mini_toml_parse` | function | `readmenator/_project_config.py:333` | `def _mini_toml_parse(text)` |
| `_mini_toml_value` | function | `readmenator/_project_config.py:395` | `def _mini_toml_value(value)` |
| `_strip_toml_comment` | function | `readmenator/_project_config.py:367` | `def _strip_toml_comment(value)` |
| `_toml_str` | function | `readmenator/_project_config.py:136` | `def _toml_str(value)` |
| `_toml_value` | function | `readmenator/_project_config.py:148` | `def _toml_value(value)` |
| `branding_css` | function | `readmenator/_project_config.py:642` | `def branding_css(config)` |
| `config_path` | function | `readmenator/_project_config.py:286` | `def config_path(project_root, config)` |
| `display_name` | function | `readmenator/_project_config.py:595` | `def display_name(config, fallback)` |
| `ensure_project_config` | function | `readmenator/_project_config.py:300` | `def ensure_project_config(project_root, config)` |
| `load_project_config` | function | `readmenator/_project_config.py:544` | `def load_project_config(project_root, base)` |
| `parse_toml` | function | `readmenator/_project_config.py:450` | `def parse_toml(text)` |
| `safe_color` | function | `readmenator/_project_config.py:624` | `def safe_color(value, fallback)` |
| `safe_url` | function | `readmenator/_project_config.py:609` | `def safe_url(url)` |
| `template_text` | function | `readmenator/_project_config.py:159` | `def template_text(config)` |
| `viewer_config_dict` | function | `readmenator/_project_config.py:663` | `def viewer_config_dict(config, project_root)` |
| `write_viewer_config` | function | `readmenator/_project_config.py:717` | `def write_viewer_config(maps_dir, config, project_root)` |
| `DocProjection` | class | `readmenator/_projections.py:42` | `class DocProjection` |
| `IdentityProjection` | class | `readmenator/_projections.py:32` | `class IdentityProjection` |
| `Projection` | class | `readmenator/_projections.py:17` | `class Projection(Protocol)` |
| `RiskProjection` | class | `readmenator/_projections.py:63` | `class RiskProjection` |
| `__init__` | method | `readmenator/_projections.py:49` | `def __init__(self, documented_ids)` |
| `__init__` | method | `readmenator/_projections.py:70` | `def __init__(self, fan_in, fan_out, test_files)` |
| `apply_view` | function | `readmenator/_projections.py:95` | `def apply_view(category, view_config)` |
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
| `_corpus_frequency` | function | `readmenator/_provenance.py:153` | `def _corpus_frequency(patterns, rows)` |
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
| `PythonReceiverTypes` | class | `readmenator/_pytypes.py:78` | `class PythonReceiverTypes` |
| `_Scope` | class | `readmenator/_pytypes.py:31` | `class _Scope` |
| `__init__` | method | `readmenator/_pytypes.py:81` | `def __init__(self, contents, language)` |
| `_annotation_name` | function | `readmenator/_pytypes.py:41` | `def _annotation_name(node)` |
| `_constructed` | function | `readmenator/_pytypes.py:68` | `def _constructed(node)` |
| `_index_file` | method | `readmenator/_pytypes.py:122` | `def _index_file(self, file_id, tree)` |
| `_record_assignment` | method | `readmenator/_pytypes.py:156` | `def _record_assignment(self, node, scope)` |
| `accepts` | method | `readmenator/_pytypes.py:269` | `def accepts(self, file_id, line, receiver, target_file, target_line, target_name)` |
| `classes` | method | `readmenator/_pytypes.py:118` | `def classes(self)` |
| `is_self_receiver` | method | `readmenator/_pytypes.py:304` | `def is_self_receiver(self, receiver)` |
| `lineage` | method | `readmenator/_pytypes.py:233` | `def lineage(self, class_name)` |
| `owner_of` | method | `readmenator/_pytypes.py:187` | `def owner_of(self, file_id, line)` |
| `receiver_class` | method | `readmenator/_pytypes.py:191` | `def receiver_class(self, file_id, line, receiver)` |
| `resolve_method` | method | `readmenator/_pytypes.py:245` | `def resolve_method(self, file_id, line, receiver, name)` |
| `scope_at` | method | `readmenator/_pytypes.py:179` | `def scope_at(self, file_id, line)` |
| `visit` | function | `readmenator/_pytypes.py:126` | `def visit(body, owner)` |
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
| `CompositeRanker` | class | `readmenator/_rank.py:411` | `class CompositeRanker` |
| `RankConfig` | class | `readmenator/_rank.py:32` | `class RankConfig` |
| `RankedItem` | class | `readmenator/_rank.py:354` | `class RankedItem` |
| `RankedResult` | class | `readmenator/_rank.py:383` | `class RankedResult` |
| `__init__` | method | `readmenator/_rank.py:419` | `def __init__(self, graph, config)` |
| `_find_justification_paths` | method | `readmenator/_rank.py:520` | `def _find_justification_paths(self, target, seed_ids, category, max_paths)` |
| `_format_explanation` | function | `readmenator/_rank.py:546` | `def _format_explanation(item, result)` |
| `_get_global_pr` | method | `readmenator/_rank.py:428` | `def _get_global_pr(self)` |
| `build_seeds_for_context` | function | `readmenator/_rank.py:320` | `def build_seeds_for_context(node_ids, anchor_patterns)` |
| `build_seeds_from_query` | function | `readmenator/_rank.py:274` | `def build_seeds_from_query(query, node_ids, node_labels, symbols)` |
| `explain` | method | `readmenator/_rank.py:403` | `def explain(self, node_id)` |
| `file_pagerank` | function | `readmenator/_rank.py:119` | `def file_pagerank(file_ids, edges, alpha, max_iter, tolerance)` |
| `global_pagerank` | function | `readmenator/_rank.py:61` | `def global_pagerank(graph, alpha, max_iter, tolerance)` |
| `hits` | function | `readmenator/_rank.py:223` | `def hits(graph, max_iter, tolerance)` |
| `label` | method | `readmenator/_rank.py:378` | `def label(self)` |
| `personalized_pagerank` | function | `readmenator/_rank.py:153` | `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` |
| `rank` | method | `readmenator/_rank.py:438` | `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` |
| `top` | method | `readmenator/_rank.py:400` | `def top(self, n)` |
| `ReadmeInjector` | class | `readmenator/_readme_injector.py:134` | `class ReadmeInjector` |
| `__init__` | method | `readmenator/_readme_injector.py:145` | `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir, graphrag_output_dir, maps_output_dir, pages_dir...` |
| `_build_injection` | method | `readmenator/_readme_injector.py:363` | `def _build_injection(self, suffix)` |
| `_extract_current_injection` | method | `readmenator/_readme_injector.py:260` | `def _extract_current_injection(content)` |
| `_find_readme` | method | `readmenator/_readme_injector.py:348` | `def _find_readme(root)` |
| `_remove_old_injection` | method | `readmenator/_readme_injector.py:277` | `def _remove_old_injection(content)` |
| `_strip_partial_anchor` | method | `readmenator/_readme_injector.py:296` | `def _strip_partial_anchor(content)` |
| `inject` | method | `readmenator/_readme_injector.py:219` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_readme_injector.py:311` | `def remove(self, project_root)` |
| `EdgeInfo` | class | `readmenator/_receipts.py:91` | `class EdgeInfo` |
| `ReceiptIngestor` | class | `readmenator/_receipts.py:113` | `class ReceiptIngestor` |
| `ReceiptsReconciler` | class | `readmenator/_receipts.py:269` | `class ReceiptsReconciler` |
| `ReleaseReceiptRecord` | class | `readmenator/_receipts.py:43` | `class ReleaseReceiptRecord` |
| `__init__` | method | `readmenator/_receipts.py:116` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_receipts.py:272` | `def __init__(self, config)` |
| `_caller_from_stage` | function | `readmenator/_receipts.py:247` | `def _caller_from_stage(stage, default)` |
| `_dedupe` | function | `readmenator/_receipts.py:257` | `def _dedupe(edges)` |
| `_edge_from_command` | function | `readmenator/_receipts.py:201` | `def _edge_from_command(raw, provenance)` |
| `_edges_section` | function | `readmenator/_receipts.py:376` | `def _edges_section(edges, title)` |
| `_explicit_edges` | method | `readmenator/_receipts.py:185` | `def _explicit_edges(self, records)` |
| `_format_receipt` | function | `readmenator/_receipts.py:354` | `def _format_receipt(receipt)` |
| `_now_iso` | function | `readmenator/_receipts.py:109` | `def _now_iso()` |
| `_opt` | function | `readmenator/_receipts.py:370` | `def _opt(value)` |
| `_receipt_title` | function | `readmenator/_receipts.py:346` | `def _receipt_title(receipt)` |
| `candidate_edges` | method | `readmenator/_receipts.py:169` | `def candidate_edges(self, records)` |
| `from_dict` | method | `readmenator/_receipts.py:64` | `def from_dict(cls, data, source_path)` |
| `load_dir` | method | `readmenator/_receipts.py:134` | `def load_dir(self, receipts_dir)` |
| `load_file` | method | `readmenator/_receipts.py:121` | `def load_file(self, path)` |
| `observed_edges` | method | `readmenator/_receipts.py:156` | `def observed_edges(self, records)` |
| `reconcile` | method | `readmenator/_receipts.py:276` | `def reconcile(self, records, candidate_edges, predicted_edges)` |
| `releases_markdown` | method | `readmenator/_receipts.py:307` | `def releases_markdown(self, report)` |
| `to_dict` | method | `readmenator/_receipts.py:101` | `def to_dict(self)` |
| `write_pages` | method | `readmenator/_receipts.py:330` | `def write_pages(self, report, target_dir, out_dirname)` |
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
| `_check_directory_depth` | method | `readmenator/_scanner.py:168` | `def _check_directory_depth(self, path, root)` |
| `_emit_progress` | method | `readmenator/_scanner.py:252` | `def _emit_progress(self, count)` |
| `_extract_file_doc` | method | `readmenator/_scanner.py:176` | `def _extract_file_doc(self, content)` |
| `_gitignore_glob_to_regex` | method | `readmenator/_scanner.py:106` | `def _gitignore_glob_to_regex(pattern)` |
| `_is_gitignored` | method | `readmenator/_scanner.py:146` | `def _is_gitignored(self, rel_path)` |
| `_is_ignored` | method | `readmenator/_scanner.py:50` | `def _is_ignored(self, path)` |
| `_load_gitignore` | method | `readmenator/_scanner.py:84` | `def _load_gitignore(self, root)` |
| `_parse_source` | method | `readmenator/_scanner.py:287` | `def _parse_source(self, rel_path_str, content, label, privacy)` |
| `_scan_impl` | method | `readmenator/_scanner.py:397` | `def _scan_impl(self, root)` |
| `_validate_path_security` | method | `readmenator/_scanner.py:155` | `def _validate_path_security(self, path)` |
| `is_generated` | method | `readmenator/_scanner.py:57` | `def is_generated(self, rel_path)` |
| `scan` | method | `readmenator/_scanner.py:262` | `def scan(self, root)` |
| `scan_contents` | method | `readmenator/_scanner.py:360` | `def scan_contents(self, contents)` |
| `scan_with_content` | method | `readmenator/_scanner.py:276` | `def scan_with_content(self, root)` |
| `ScanTextBuilder` | class | `readmenator/_scantext.py:16` | `class ScanTextBuilder` |
| `__init__` | method | `readmenator/_scantext.py:19` | `def __init__(self, config)` |
| `build_corpus` | method | `readmenator/_scantext.py:67` | `def build_corpus(self, nodes, content_map, edges)` |
| `build_for_node` | method | `readmenator/_scantext.py:27` | `def build_for_node(self, node, content, imports)` |
| `SecurityAnalyzer` | class | `readmenator/_security.py:486` | `class SecurityAnalyzer` |
| `SecurityRule` | class | `readmenator/_security.py:24` | `class SecurityRule` |
| `__init__` | method | `readmenator/_security.py:496` | `def __init__(self, config)` |
| `_build_rules_from_yaml` | function | `readmenator/_security.py:447` | `def _build_rules_from_yaml(yaml_path)` |
| `_c_rules` | function | `readmenator/_security.py:201` | `def _c_rules()` |
| `_compile` | function | `readmenator/_security.py:148` | `def _compile()` |
| `_csharp_rules` | function | `readmenator/_security.py:297` | `def _csharp_rules()` |
| `_dart_rules` | function | `readmenator/_security.py:354` | `def _dart_rules()` |
| `_elixir_rules` | function | `readmenator/_security.py:398` | `def _elixir_rules()` |
| `_gdscript_rules` | function | `readmenator/_security.py:387` | `def _gdscript_rules()` |
| `_go_rules` | function | `readmenator/_security.py:237` | `def _go_rules()` |
| `_java_rules` | function | `readmenator/_security.py:222` | `def _java_rules()` |
| `_javascript_rules` | function | `readmenator/_security.py:182` | `def _javascript_rules()` |
| `_kotlin_rules` | function | `readmenator/_security.py:310` | `def _kotlin_rules()` |
| `_load_rules_from_yaml` | function | `readmenator/_security.py:128` | `def _load_rules_from_yaml(yaml_path)` |
| `_lua_rules` | function | `readmenator/_security.py:343` | `def _lua_rules()` |
| `_meets_threshold` | method | `readmenator/_security.py:509` | `def _meets_threshold(self, severity)` |
| `_nim_rules` | function | `readmenator/_security.py:376` | `def _nim_rules()` |
| `_parse_minimal_yaml` | function | `readmenator/_security.py:46` | `def _parse_minimal_yaml(text)` |
| `_php_rules` | function | `readmenator/_security.py:267` | `def _php_rules()` |
| `_python_rules` | function | `readmenator/_security.py:153` | `def _python_rules()` |
| `_resolve_rules` | method | `readmenator/_security.py:500` | `def _resolve_rules(self)` |
| `_ruby_rules` | function | `readmenator/_security.py:250` | `def _ruby_rules()` |
| `_rust_rules` | function | `readmenator/_security.py:365` | `def _rust_rules()` |
| `_scala_rules` | function | `readmenator/_security.py:332` | `def _scala_rules()` |
| `_shell_rules` | function | `readmenator/_security.py:284` | `def _shell_rules()` |
| `_swift_rules` | function | `readmenator/_security.py:321` | `def _swift_rules()` |
| `_unquote` | function | `readmenator/_security.py:121` | `def _unquote(s)` |
| `_validate_path` | method | `readmenator/_security.py:555` | `def _validate_path(self, path, root)` |
| `fix_hint_for` | function | `readmenator/_security.py:620` | `def fix_hint_for(finding)` |
| `scan` | method | `readmenator/_security.py:513` | `def scan(self, root)` |
| `summary` | method | `readmenator/_security.py:572` | `def summary(self, findings)` |
| `SkillInstaller` | class | `readmenator/_skill_installer.py:22` | `class SkillInstaller` |
| `__init__` | method | `readmenator/_skill_installer.py:25` | `def __init__(self, config)` |
| `available` | method | `readmenator/_skill_installer.py:38` | `def available(self)` |
| `install` | method | `readmenator/_skill_installer.py:61` | `def install(self, project_root, target)` |
| `maybe_install_on_run` | method | `readmenator/_skill_installer.py:87` | `def maybe_install_on_run(self, project_root)` |
| `source_dir` | method | `readmenator/_skill_installer.py:34` | `def source_dir()` |
| `target_dir` | method | `readmenator/_skill_installer.py:48` | `def target_dir(self, project_root, target)` |
| `SourceEntry` | class | `readmenator/_sourceview.py:20` | `class SourceEntry` |
| `SourceViewBuilder` | class | `readmenator/_sourceview.py:36` | `class SourceViewBuilder` |
| `__init__` | method | `readmenator/_sourceview.py:39` | `def __init__(self, config)` |
| `_build` | method | `readmenator/_sourceview.py:89` | `def _build(self, nodes, content_map)` |
| `build_reasons` | method | `readmenator/_sourceview.py:70` | `def build_reasons(self, nodes, content_map)` |
| `build_sources` | method | `readmenator/_sourceview.py:55` | `def build_sources(self, nodes, content_map)` |
| `enabled` | method | `readmenator/_sourceview.py:47` | `def enabled(self)` |
| `to_payload` | method | `readmenator/_sourceview.py:149` | `def to_payload(self, sources)` |
| `CallSite` | class | `readmenator/_symindex.py:81` | `class CallSite` |
| `ResolvedCall` | class | `readmenator/_symindex.py:102` | `class ResolvedCall` |
| `SymbolDef` | class | `readmenator/_symindex.py:56` | `class SymbolDef` |
| `SymbolIndex` | class | `readmenator/_symindex.py:132` | `class SymbolIndex` |
| `_Visitor` | class | `readmenator/_symindex.py:365` | `class _Visitor(NodeVisitor)` |
| `__init__` | method | `readmenator/_symindex.py:135` | `def __init__(self, config)` |
| `_edge_call_sites` | method | `readmenator/_symindex.py:331` | `def _edge_call_sites(self, edges)` |
| `_kind_to_node_type` | function | `readmenator/_symindex.py:122` | `def _kind_to_node_type(kind)` |
| `_pop` | method | `readmenator/_symindex.py:374` | `def _pop(self, node)` |
| `_push` | method | `readmenator/_symindex.py:368` | `def _push(self, node)` |
| `_python_call_sites` | method | `readmenator/_symindex.py:348` | `def _python_call_sites(self, file_id, content)` |
| `_receiver_text` | function | `readmenator/_symindex.py:42` | `def _receiver_text(node)` |
| `_regex_call_sites` | method | `readmenator/_symindex.py:422` | `def _regex_call_sites(self, file_id, content, symbols)` |
| `_resolve_one` | method | `readmenator/_symindex.py:286` | `def _resolve_one(self, site, by_name, imports_of)` |
| `build` | method | `readmenator/_symindex.py:144` | `def build(self, nodes, content_map)` |
| `extract_call_sites` | method | `readmenator/_symindex.py:212` | `def extract_call_sites(self, file_id, content, language, symbols)` |
| `methods_index` | method | `readmenator/_symindex.py:184` | `def methods_index(self, index)` |
| `resolve` | method | `readmenator/_symindex.py:237` | `def resolve(self, nodes, edges, resolved_edges, content_map)` |
| `visit_AsyncFunctionDef` | method | `readmenator/_symindex.py:391` | `def visit_AsyncFunctionDef(self, node)` |
| `visit_Call` | method | `readmenator/_symindex.py:397` | `def visit_Call(self, node)` |
| `visit_ClassDef` | method | `readmenator/_symindex.py:379` | `def visit_ClassDef(self, node)` |
| `visit_FunctionDef` | method | `readmenator/_symindex.py:385` | `def visit_FunctionDef(self, node)` |
| `TaintAnalyzer` | class | `readmenator/_taint.py:12` | `class TaintAnalyzer` |
| `__init__` | method | `readmenator/_taint.py:73` | `def __init__(self, config)` |
| `_build_forward_graph` | method | `readmenator/_taint.py:213` | `def _build_forward_graph(nodes, resolved_edges)` |
| `_find_direct_sources` | method | `readmenator/_taint.py:136` | `def _find_direct_sources(self, nodes, edges)` |
| `_propagate` | method | `readmenator/_taint.py:162` | `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` |
| `analyze` | method | `readmenator/_taint.py:77` | `def analyze(self, nodes, edges, resolved_edges)` |
| `UmlGenerator` | class | `readmenator/_uml.py:34` | `class UmlGenerator` |
| `__init__` | method | `readmenator/_uml.py:36` | `def __init__(self, config)` |
| `_cpp_params` | function | `readmenator/_uml.py:259` | `def _cpp_params(params)` |
| `_cs_params` | function | `readmenator/_uml.py:345` | `def _cs_params(params)` |
| `_extract_params` | function | `readmenator/_uml.py:592` | `def _extract_params(signature)` |
| `_find_node` | method | `readmenator/_uml.py:165` | `def _find_node(nodes, node_id)` |
| `_generate_cpp` | function | `readmenator/_uml.py:233` | `def _generate_cpp(class_symbols, nodes, edges)` |
| `_generate_csharp` | function | `readmenator/_uml.py:316` | `def _generate_csharp(class_symbols, nodes, edges)` |
| `_generate_dart` | function | `readmenator/_uml.py:547` | `def _generate_dart(class_symbols, nodes, edges)` |
| `_generate_go` | function | `readmenator/_uml.py:395` | `def _generate_go(class_symbols, nodes, edges)` |
| `_generate_java` | function | `readmenator/_uml.py:274` | `def _generate_java(class_symbols, nodes, edges)` |
| `_generate_kotlin` | function | `readmenator/_uml.py:476` | `def _generate_kotlin(class_symbols, nodes, edges)` |
| `_generate_php` | function | `readmenator/_uml.py:448` | `def _generate_php(class_symbols, nodes, edges)` |
| `_generate_python` | function | `readmenator/_uml.py:360` | `def _generate_python(class_symbols, nodes, edges)` |
| `_generate_ruby` | function | `readmenator/_uml.py:567` | `def _generate_ruby(class_symbols, nodes, edges)` |
| `_generate_rust` | function | `readmenator/_uml.py:422` | `def _generate_rust(class_symbols, nodes, edges)` |
| `_generate_scala` | function | `readmenator/_uml.py:496` | `def _generate_scala(class_symbols, nodes, edges)` |
| `_generate_swift` | function | `readmenator/_uml.py:518` | `def _generate_swift(class_symbols, nodes, edges)` |
| `_get_code_generator` | function | `readmenator/_uml.py:172` | `def _get_code_generator(language)` |
| `_java_params` | function | `readmenator/_uml.py:301` | `def _java_params(params)` |
| `_safe_name` | function | `readmenator/_uml.py:588` | `def _safe_name(name)` |
| `_sanitize_id` | method | `readmenator/_uml.py:153` | `def _sanitize_id(raw)` |
| `_type_map_py_to_target` | function | `readmenator/_uml.py:190` | `def _type_map_py_to_target(target, py_type_hint)` |
| `generate_code` | method | `readmenator/_uml.py:129` | `def generate_code(self, nodes, edges, target_language)` |
| `render_mermaid_class_diagram` | method | `readmenator/_uml.py:39` | `def render_mermaid_class_diagram(self, nodes, edges)` |
| `HeuristicScorer` | class | `readmenator/_uncertainty.py:101` | `class HeuristicScorer` |
| `RandomForestScorer` | class | `readmenator/_uncertainty.py:138` | `class RandomForestScorer` |
| `UncertaintyPrediction` | class | `readmenator/_uncertainty.py:93` | `class UncertaintyPrediction` |
| `__init__` | method | `readmenator/_uncertainty.py:143` | `def __init__(self, n_estimators, random_state)` |
| `_bucket_evidence` | function | `readmenator/_uncertainty.py:50` | `def _bucket_evidence(evidence)` |
| `_bucket_target` | function | `readmenator/_uncertainty.py:67` | `def _bucket_target(callee)` |
| `_sigmoid` | function | `readmenator/_uncertainty.py:180` | `def _sigmoid(x)` |
| `available` | method | `readmenator/_uncertainty.py:149` | `def available()` |
| `featurize` | function | `readmenator/_uncertainty.py:83` | `def featurize(edge, known_observed)` |
| `fit` | method | `readmenator/_uncertainty.py:156` | `def fit(self, x, y)` |
| `predict_uncertain_edges` | function | `readmenator/_uncertainty.py:187` | `def predict_uncertain_edges(candidate_edges, known_observed, config, min_confidence, scorer)` |
| `prediction_edges` | function | `readmenator/_uncertainty.py:214` | `def prediction_edges(predictions, provenance_version)` |
| `score` | method | `readmenator/_uncertainty.py:129` | `def score(self, features)` |
| `score` | method | `readmenator/_uncertainty.py:171` | `def score(self, features)` |
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
| `Backdrop` | class | `readmenator/_video.py:690` | `class Backdrop` |
| `CinematicVideoRenderer` | class | `readmenator/_video.py:885` | `class CinematicVideoRenderer` |
| `__init__` | method | `readmenator/_video.py:693` | `def __init__(self, width, height)` |
| `_bezier` | function | `readmenator/_video.py:2499` | `def _bezier(points, t)` |
| `_build_dep_tree` | method | `readmenator/_video.py:1138` | `def _build_dep_tree(self, node_by_id, link_set, god_names)` |
| `_build_growth` | method | `readmenator/_video.py:1083` | `def _build_growth(self, project_root, graph_nodes, graph_links)` |
| `_camera_track` | function | `readmenator/_video.py:256` | `def _camera_track(keys, f)` |
| `_caption_y` | function | `readmenator/_video.py:153` | `def _caption_y(cfg)` |
| `_clipped` | function | `readmenator/_video.py:279` | `def _clipped(img, box, paint)` |
| `_cloud_core` | function | `readmenator/_video.py:335` | `def _cloud_core(d, data, box, cfg, yaw, pitch, target, zoom, mode, lit_nodes, edge_lit, gt, fonts, appear, labels)` |
| `_code_tint` | function | `readmenator/_video.py:626` | `def _code_tint(line)` |
| `_depth_alpha` | function | `readmenator/_video.py:232` | `def _depth_alpha(z, fade)` |
| `_dna_boxes` | function | `readmenator/_video.py:167` | `def _dna_boxes(cfg)` |
| `_draw_flow_edge` | function | `readmenator/_video.py:2507` | `def _draw_flow_edge(d, pts, col, a, width, upto, dashed)` |
| `_draw_flow_node` | function | `readmenator/_video.py:2526` | `def _draw_flow_node(d, node, tf, fonts, col, a, glow, lines)` |
| `_draw_frame` | function | `readmenator/_video.py:1564` | `def _draw_frame(fi)` |
| `_find` | function | `readmenator/_video.py:655` | `def _find(style)` |
| `_flow_graph` | function | `readmenator/_video.py:2491` | `def _flow_graph(kind)` |
| `_graph_boxes` | function | `readmenator/_video.py:158` | `def _graph_boxes(cfg)` |
| `_growth_frame` | function | `readmenator/_video.py:2177` | `def _growth_frame(data, cfg, local_t, phase_dur)` |
| `_growth_pulse` | function | `readmenator/_video.py:430` | `def _growth_pulse(d, data, proj, cfg)` |
| `_growth_pulse_anchor` | function | `readmenator/_video.py:2238` | `def _growth_pulse_anchor(releases, factor, rank)` |
| `_growth_ticker` | function | `readmenator/_video.py:2263` | `def _growth_ticker(d, side, meta, releases, fonts)` |
| `_img` | function | `readmenator/_video.py:746` | `def _img()` |
| `_img_draw` | function | `readmenator/_video.py:2721` | `def _img_draw(img)` |
| `_language_color` | function | `readmenator/_video.py:237` | `def _language_color(language)` |
| `_lerp3` | function | `readmenator/_video.py:251` | `def _lerp3(a, b, t)` |
| `_motion_blurred` | function | `readmenator/_video.py:1540` | `def _motion_blurred(index, lt)` |
| `_orbit_plan` | function | `readmenator/_video.py:1995` | `def _orbit_plan(dur)` |
| `_outgoing_frame` | function | `readmenator/_video.py:1555` | `def _outgoing_frame(index)` |
| `_packet_offset` | function | `readmenator/_video.py:636` | `def _packet_offset(a, b, k)` |
| `_paint_scene` | function | `readmenator/_video.py:1525` | `def _paint_scene(index, lt)` |
| `_panel` | function | `readmenator/_video.py:148` | `def _panel(cfg)` |
| `_place_label` | function | `readmenator/_video.py:267` | `def _place_label(d, placed, x, y, text, font, col, a)` |
| `_polyline_point` | function | `readmenator/_video.py:192` | `def _polyline_point(points, f)` |
| `_prepare_growth` | method | `readmenator/_video.py:1404` | `def _prepare_growth(self, data)` |
| `_prepare_layouts` | method | `readmenator/_video.py:1389` | `def _prepare_layouts(self, data)` |
| `_render_frame_bytes` | function | `readmenator/_video.py:1509` | `def _render_frame_bytes(fi)` |
| `_scan_cursor` | function | `readmenator/_video.py:617` | `def _scan_cursor(d, box, progress, col)` |
| `_scene_bundle` | function | `readmenator/_video.py:1909` | `def _scene_bundle(img, d, lt, gt, sc)` |
| `_scene_card` | function | `readmenator/_video.py:1623` | `def _scene_card(img, d, lt, gt, sc)` |
| `_scene_communities` | function | `readmenator/_video.py:1779` | `def _scene_communities(img, d, lt, gt, sc)` |
| `_scene_dna` | function | `readmenator/_video.py:2402` | `def _scene_dna(img, d, lt, gt, sc)` |
| `_scene_flow` | function | `readmenator/_video.py:2628` | `def _scene_flow(img, d, lt, gt, sc)` |
| `_scene_gods` | function | `readmenator/_video.py:1662` | `def _scene_gods(img, d, lt, gt, sc)` |
| `_scene_graph` | function | `readmenator/_video.py:1823` | `def _scene_graph(img, d, lt, gt, sc)` |
| `_scene_growth` | function | `readmenator/_video.py:2299` | `def _scene_growth(img, d, lt, gt, sc)` |
| `_scene_index` | function | `readmenator/_video.py:1517` | `def _scene_index(gt)` |
| `_scene_invite` | function | `readmenator/_video.py:2355` | `def _scene_invite(img, d, lt, gt, sc)` |
| `_scene_layers` | function | `readmenator/_video.py:1637` | `def _scene_layers(img, d, lt, gt, sc)` |
| `_scene_orbit` | function | `readmenator/_video.py:2000` | `def _scene_orbit(img, d, lt, gt, sc)` |
| `_scene_outro` | function | `readmenator/_video.py:2461` | `def _scene_outro(img, d, lt, gt, sc)` |
| `_scene_sphere` | function | `readmenator/_video.py:2116` | `def _scene_sphere(img, d, lt, gt, sc)` |
| `_scene_tiers` | function | `readmenator/_video.py:2549` | `def _scene_tiers(img, d, lt, gt, sc)` |
| `_scene_title` | function | `readmenator/_video.py:1588` | `def _scene_title(img, d, lt, gt, sc)` |
| `_scene_tree` | function | `readmenator/_video.py:1705` | `def _scene_tree(img, d, lt, gt, sc)` |
| `_sphere_core` | function | `readmenator/_video.py:505` | `def _sphere_core(d, data, layout, box, cfg, yaw, pitch, morph, reveal, spot, gt, fonts, group_labels, zoom)` |
| `_split_boxes` | function | `readmenator/_video.py:176` | `def _split_boxes(cfg)` |
| `_sun` | method | `readmenator/_video.py:731` | `def _sun(self, r)` |
| `_verdict_badge` | function | `readmenator/_video.py:602` | `def _verdict_badge(d, box, text, fonts, lt, dur, col)` |
| `alpha` | function | `readmenator/_video.py:126` | `def alpha(c, a)` |
| `build_scenes` | method | `readmenator/_video.py:1189` | `def build_scenes(self, data)` |
| `bundle_groups` | method | `readmenator/_video.py:1321` | `def bundle_groups(self, data)` |
| `bundle_layout` | method | `readmenator/_video.py:1346` | `def bundle_layout(self, data, box)` |
| `chroma_text` | function | `readmenator/_video.py:831` | `def chroma_text(img, xy, text, font, col, spread, anchor)` |
| `collect` | method | `readmenator/_video.py:890` | `def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map...` |
| `community_color` | function | `readmenator/_video.py:185` | `def community_color(index)` |
| `dependencies_available` | function | `readmenator/_video.py:642` | `def dependencies_available()` |
| `draw_caption` | function | `readmenator/_video.py:869` | `def draw_caption(d, text, lt, dur, fonts, width, y)` |
| `draw_cloud3d` | function | `readmenator/_video.py:291` | `def draw_cloud3d(img, data, box, cfg, yaw, pitch, target, zoom, mode, lit_nodes, edge_lit, gt, fonts, appear, labels)` |
| `draw_grid` | function | `readmenator/_video.py:753` | `def draw_grid(img, t, strength, bd)` |
| `draw_header` | function | `readmenator/_video.py:855` | `def draw_header(img, d, gt, total, project, act_label, fonts, width)` |
| `draw_sphere3d` | function | `readmenator/_video.py:464` | `def draw_sphere3d(img, data, box, cfg, yaw, pitch, morph, reveal, spot, gt, fonts, group_labels, zoom)` |
| `draw_sun` | function | `readmenator/_video.py:773` | `def draw_sun(img, a, bd, cy)` |
| `ease` | function | `readmenator/_video.py:105` | `def ease(x)` |
| `emergence_frames` | method | `readmenator/_video.py:1311` | `def emergence_frames(self, data, box)` |
| `factor` | function | `readmenator/_video.py:2206` | `def factor(born)` |
| `fmt_int` | function | `readmenator/_video.py:116` | `def fmt_int(n)` |
| `glitch_fx` | function | `readmenator/_video.py:808` | `def glitch_fx(img, amount, seed)` |
| `graph_positions` | method | `readmenator/_video.py:1221` | `def graph_positions(self, data, box)` |
| `hash_color` | function | `readmenator/_video.py:131` | `def hash_color(digest)` |
| `hud_panel` | function | `readmenator/_video.py:842` | `def hud_panel(d, box, title, fonts, col)` |
| `mix` | function | `readmenator/_video.py:121` | `def mix(a, b, t)` |
| `mode_color` | function | `readmenator/_video.py:242` | `def mode_color(data, nid, mode)` |
| `orbit_positions` | method | `readmenator/_video.py:1355` | `def orbit_positions(self, data)` |
| `orbit_stops` | method | `readmenator/_video.py:1374` | `def orbit_stops(self, data, positions)` |
| `ordered_groups` | method | `readmenator/_video.py:1336` | `def ordered_groups(self, data)` |

Next: [SYMBOLS_p4.md](SYMBOLS_p4.md)
