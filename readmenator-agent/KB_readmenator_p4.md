# Subsystem: readmenator (page 4 of 5)
Previous: [KB_readmenator_p3.md](KB_readmenator_p3.md)

## readmenator/_project_config.py
- Doc: Per-project persistent configuration (readmenator.toml).
- Layer: infrastructure
- Language: py
- Symbols:
  - `_toml_str` (function, line 136) `def _toml_str(value)`
  - `_toml_value` (function, line 148) `def _toml_value(value)`
  - `template_text` (function, line 159) `def template_text(config)`
  - `config_path` (function, line 286) `def config_path(project_root, config)`
  - `ensure_project_config` (function, line 300) `def ensure_project_config(project_root, config)`
  - `_mini_toml_parse` (function, line 333) `def _mini_toml_parse(text)`
  - `_strip_toml_comment` (function, line 367) `def _strip_toml_comment(value)`
  - `_mini_toml_value` (function, line 395) `def _mini_toml_value(value)`
  - `parse_toml` (function, line 450) `def parse_toml(text)`
  - `_field_types` (function, line 484) `def _field_types()`
  - `_coerce` (function, line 492) `def _coerce(field_name, value, default)`
  - `load_project_config` (function, line 544) `def load_project_config(project_root, base)`
  - `display_name` (function, line 595) `def display_name(config, fallback)`
  - `safe_url` (function, line 609) `def safe_url(url)`
  - `safe_color` (function, line 624) `def safe_color(value, fallback)`
  - `branding_css` (function, line 642) `def branding_css(config)`
  - `viewer_config_dict` (function, line 663) `def viewer_config_dict(config, project_root)`
  - `write_viewer_config` (function, line 717) `def write_viewer_config(maps_dir, config, project_root)`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_app.py`, `readmenator/_bundlegraph.py`, `readmenator/_diagrams.py`, `readmenator/_flowpage.py`, `readmenator/_forcegraph.py`, `readmenator/_viewer_ui.py`, `tests/test_project_config.py`

## readmenator/_projections.py
- Doc: Functors and projections for the readmenator code category.
- Layer: utility
- Language: py
- Symbols:
  - `Projection` (class, line 17) `class Projection(Protocol)`
  - `IdentityProjection` (class, line 32) `class IdentityProjection`
  - `DocProjection` (class, line 42) `class DocProjection`
  - `RiskProjection` (class, line 63) `class RiskProjection`
  - `apply_view` (function, line 95) `def apply_view(category, view_config)`
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

## readmenator/_provenance.py
- Doc: Evidence-provenance audit for readmenator security findings.
- Layer: utility
- Language: py
- Symbols:
  - `ProvenanceFinding` (class, line 20) `class ProvenanceFinding`
  - `ProvenanceAuditor` (class, line 46) `class ProvenanceAuditor`
  - `_corpus_frequency` (function, line 153) `def _corpus_frequency(patterns, rows)`
  - `is_inferred_only` (method, line 32) `def is_inferred_only(self)`
  - `reading` (method, line 37) `def reading(self)`
  - `__init__` (method, line 49) `def __init__(self, config)`
  - `audit` (method, line 57) `def audit(self, findings, content_map)`
  - `summary` (method, line 98) `def summary(self, findings)`
  - `_snippet_in_content` (method, line 115) `def _snippet_in_content(self, file_path, snippet, content_map)`
  - `_attach_frequency` (method, line 124) `def _attach_frequency(self, findings, content_map)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`

## readmenator/_purpose.py
- Doc: Purpose extraction shared by every agent-facing document generator.
- Layer: utility
- Language: py
- Symbols:
  - `is_garbage_doc` (function, line 26) `def is_garbage_doc(text)`
  - `clean_purpose` (function, line 43) `def clean_purpose(text)`
  - `escape_cell` (function, line 66) `def escape_cell(text)`
  - `truncate_words` (function, line 78) `def truncate_words(text, max_chars)`
  - `first_sentence` (function, line 98) `def first_sentence(doc)`
  - `_primary_symbol` (function, line 116) `def _primary_symbol(symbols)`
  - `file_purpose` (function, line 140) `def file_purpose(node, max_chars)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_components.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `readmenator/_memory.py`, `readmenator/_wiki.py`, `tests/test_agent_friendliness.py`

## readmenator/_pytypes.py
- Doc: Lightweight, deterministic receiver typing for Python attribute calls.
- Layer: utility
- Language: py
- Symbols:
  - `_Scope` (class, line 31) `class _Scope`
  - `_annotation_name` (function, line 41) `def _annotation_name(node)`
  - `_constructed` (function, line 68) `def _constructed(node)`
  - `PythonReceiverTypes` (class, line 78) `class PythonReceiverTypes`
  - `__init__` (method, line 81) `def __init__(self, contents, language)`
  - `classes` (method, line 118) `def classes(self)`
  - `_index_file` (method, line 122) `def _index_file(self, file_id, tree)`
  - `_record_assignment` (method, line 156) `def _record_assignment(self, node, scope)`
  - `scope_at` (method, line 179) `def scope_at(self, file_id, line)`
  - `owner_of` (method, line 187) `def owner_of(self, file_id, line)`
  - `receiver_class` (method, line 191) `def receiver_class(self, file_id, line, receiver)`
  - `lineage` (method, line 233) `def lineage(self, class_name)`
  - `resolve_method` (method, line 245) `def resolve_method(self, file_id, line, receiver, name)`
  - `accepts` (method, line 269) `def accepts(self, file_id, line, receiver, target_file, target_line, target_name)`
  - `is_self_receiver` (method, line 304) `def is_self_receiver(self, receiver)`
  - `visit` (function, line 126) `def visit(body, owner)`
- Imported by: `readmenator/_apidocs.py`, `readmenator/_flowcharts.py`, `tests/test_flowcharts.py`

## readmenator/_query.py
- Doc: Query engine for the readmenator knowledge base.
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
- Doc: PageRank, Personalized PageRank, HITS, and composite scoring.
- Layer: utility
- Language: py
- Symbols:
  - `RankConfig` (class, line 32) `class RankConfig`
  - `global_pagerank` (function, line 61) `def global_pagerank(graph, alpha, max_iter, tolerance)`
  - `file_pagerank` (function, line 119) `def file_pagerank(file_ids, edges, alpha, max_iter, tolerance)`
  - `personalized_pagerank` (function, line 153) `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)`
  - `hits` (function, line 223) `def hits(graph, max_iter, tolerance)`
  - `build_seeds_from_query` (function, line 274) `def build_seeds_from_query(query, node_ids, node_labels, symbols)`
  - `build_seeds_for_context` (function, line 320) `def build_seeds_for_context(node_ids, anchor_patterns)`
  - `RankedItem` (class, line 354) `class RankedItem`
  - `RankedResult` (class, line 383) `class RankedResult`
  - `CompositeRanker` (class, line 411) `class CompositeRanker`
  - `_format_explanation` (function, line 546) `def _format_explanation(item, result)`
  - `label` (method, line 378) `def label(self)`
  - `top` (method, line 400) `def top(self, n)`
  - `explain` (method, line 403) `def explain(self, node_id)`
  - `__init__` (method, line 419) `def __init__(self, graph, config)`
  - `_get_global_pr` (method, line 428) `def _get_global_pr(self)`
  - `rank` (method, line 438) `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)`
  - `_find_justification_paths` (method, line 520) `def _find_justification_paths(self, target, seed_ids, category, max_paths)`
- Depends on: `readmenator/_category.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_components.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_video.py`, `tests/test_ranking.py`

## readmenator/_readme_injector.py
- Doc: Injects a knowledge base section into the project README (Markdown or RST).
- Layer: infrastructure
- Language: py
- Symbols:
  - `ReadmeInjector` (class, line 134) `class ReadmeInjector`
  - `__init__` (method, line 145) `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir, graphrag_output_dir, maps_output_dir, pages_dir...`
  - `inject` (method, line 219) `def inject(self, project_root)`
  - `_extract_current_injection` (method, line 260) `def _extract_current_injection(content)`
  - `_remove_old_injection` (method, line 277) `def _remove_old_injection(content)`
  - `_strip_partial_anchor` (method, line 296) `def _strip_partial_anchor(content)`
  - `remove` (method, line 311) `def remove(self, project_root)`
  - `_find_readme` (method, line 348) `def _find_readme(root)`
  - `_build_injection` (method, line 363) `def _build_injection(self, suffix)`
- Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_project_config.py`, `tests/test_readme_injector.py`

## readmenator/_receipts.py
- Doc: Release receipts ingest contract: deploys as first-class evidence.  deploynator writes...
- Layer: utility
- Language: py
- Symbols:
  - `ReleaseReceiptRecord` (class, line 43) `class ReleaseReceiptRecord`
  - `EdgeInfo` (class, line 91) `class EdgeInfo`
  - `_now_iso` (function, line 109) `def _now_iso()`
  - `ReceiptIngestor` (class, line 113) `class ReceiptIngestor`
  - `_edge_from_command` (function, line 201) `def _edge_from_command(raw, provenance)`
  - `_caller_from_stage` (function, line 247) `def _caller_from_stage(stage, default)`
  - `_dedupe` (function, line 257) `def _dedupe(edges)`
  - `ReceiptsReconciler` (class, line 269) `class ReceiptsReconciler`
  - `_receipt_title` (function, line 346) `def _receipt_title(receipt)`
  - `_format_receipt` (function, line 354) `def _format_receipt(receipt)`
  - `_opt` (function, line 370) `def _opt(value)`
  - `_edges_section` (function, line 376) `def _edges_section(edges, title)`
  - `from_dict` (method, line 64) `def from_dict(cls, data, source_path)`
  - `to_dict` (method, line 101) `def to_dict(self)`
  - `__init__` (method, line 116) `def __init__(self, config)`
  - `load_file` (method, line 121) `def load_file(self, path)`
  - `load_dir` (method, line 134) `def load_dir(self, receipts_dir)`
  - `observed_edges` (method, line 156) `def observed_edges(self, records)`
  - `candidate_edges` (method, line 169) `def candidate_edges(self, records)`
  - `_explicit_edges` (method, line 185) `def _explicit_edges(self, records)`
  - `__init__` (method, line 272) `def __init__(self, config)`
  - `reconcile` (method, line 276) `def reconcile(self, records, candidate_edges, predicted_edges)`
  - `releases_markdown` (method, line 307) `def releases_markdown(self, report)`
  - `write_pages` (method, line 330) `def write_pages(self, report, target_dir, out_dirname)`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_app.py`, `readmenator/_hypotheses.py`, `readmenator/_uncertainty.py`, `tests/test_receipts.py`

## readmenator/_refactorizer.py
- Doc: Monolithic file refactoring planner for the readmenator knowledge graph.
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
- Doc: Import path resolver for the readmenator knowledge graph.
- Layer: utility
- Language: py
- Symbols:
  - `ImportResolver` (class, line 18) `class ImportResolver`
  - `__init__` (method, line 61) `def __init__(self, file_ids, root, extensions, include_dirs)`
  - `_build_stem_index` (method, line 83) `def _build_stem_index(self, file_ids)`
  - `_build_dir_index` (method, line 93) `def _build_dir_index(self, file_ids)`
  - `resolve` (method, line 110) `def resolve(self, import_str, source_file)`
  - `resolve_all` (method, line 163) `def resolve_all(self, import_str, source_file)`
  - `_resolve_include_dirs` (method, line 179) `def _resolve_include_dirs(self, import_str)`
  - `_resolve_relative` (method, line 199) `def _resolve_relative(self, import_str, source_file)`
  - `_resolve_verbatim` (method, line 217) `def _resolve_verbatim(self, import_str, source_file)`
  - `_resolve_extensionless` (method, line 235) `def _resolve_extensionless(self, import_str, source_file)`
  - `_resolve_directory_init` (method, line 244) `def _resolve_directory_init(self, import_str, source_file)`
  - `_resolve_root_package` (method, line 254) `def _resolve_root_package(self, import_str)`
  - `_resolve_module_dotpath` (method, line 269) `def _resolve_module_dotpath(self, import_str)`
  - `_resolve_suffix_match` (method, line 291) `def _resolve_suffix_match(self, import_str)`
  - `_resolve_basename_match` (method, line 306) `def _resolve_basename_match(self, import_str)`
  - `_resolve_stem_match` (method, line 324) `def _resolve_stem_match(self, import_str)`
  - `_strip_extension` (method, line 333) `def _strip_extension(self, name)`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `readmenator/_forcegraph.py`, `readmenator/_githistory.py`, `readmenator/_graphrag.py`, `tests/test_agent_friendliness.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`

## readmenator/_rule_gen.py
- Doc: Suggested linting rule generator producing Semgrep YAML from detected antipatterns.
- Layer: business_logic
- Language: py
- Symbols:
  - `RuleGenerator` (class, line 14) `class RuleGenerator`
  - `__init__` (method, line 90) `def __init__(self, config)`
  - `generate` (method, line 94) `def generate(self, nodes, content_map)`
  - `write_rules` (method, line 122) `def write_rules(self, rules, output_dir)`
  - `_group_by_language` (method, line 161) `def _group_by_language(self, nodes)`
  - `_analyze_language` (method, line 171) `def _analyze_language(self, lang, nodes, content_map)`
  - `_detect_antipatterns` (method, line 204) `def _detect_antipatterns(self, nodes, content_map)`
  - `_infer_language_for_rule` (method, line 250) `def _infer_language_for_rule(rule_id)`
  - `_next_rule_id` (method, line 260) `def _next_rule_id(self)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`

## readmenator/_sarif.py
- Doc: SARIF v2.1.0 exporter for security findings (GitHub Code Scanning compatible).
- Layer: utility
- Language: py
- Symbols:
  - `SarifExporter` (class, line 11) `class SarifExporter`
  - `__init__` (method, line 30) `def __init__(self, privacy_mode)`
  - `export` (method, line 33) `def export(self, findings, project_name)`
  - `_build_rule` (method, line 82) `def _build_rule(self, finding)`
  - `_build_result` (method, line 106) `def _build_result(self, finding, rule_index)`
- Depends on: `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`

## readmenator/_scanner.py
- Doc: Secure polyglot directory traversal and file analysis.
- Layer: utility
- Language: py
- Symbols:
  - `PolyglotScanner` (class, line 28) `class PolyglotScanner`
  - `__init__` (method, line 39) `def __init__(self, config)`
  - `_is_ignored` (method, line 50) `def _is_ignored(self, path)`
  - `is_generated` (method, line 57) `def is_generated(self, rel_path)`
  - `_load_gitignore` (method, line 84) `def _load_gitignore(self, root)`
  - `_gitignore_glob_to_regex` (method, line 106) `def _gitignore_glob_to_regex(pattern)`
  - `_is_gitignored` (method, line 146) `def _is_gitignored(self, rel_path)`
  - `_validate_path_security` (method, line 155) `def _validate_path_security(self, path)`
  - `_check_directory_depth` (method, line 168) `def _check_directory_depth(self, path, root)`
  - `_extract_file_doc` (method, line 176) `def _extract_file_doc(self, content)`
  - `_emit_progress` (method, line 252) `def _emit_progress(self, count)`
  - `scan` (method, line 262) `def scan(self, root)`
  - `scan_with_content` (method, line 276) `def scan_with_content(self, root)`
  - `_parse_source` (method, line 287) `def _parse_source(self, rel_path_str, content, label, privacy)`
  - `scan_contents` (method, line 360) `def scan_contents(self, contents)`
  - `_scan_impl` (method, line 397) `def _scan_impl(self, root)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
- Imported by: `readmenator/_githistory.py`, `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`

## readmenator/_scantext.py
- Doc: Synthesized scan-text builder for the readmenator knowledge graph.
- Layer: utility
- Language: py
- Symbols:
  - `ScanTextBuilder` (class, line 16) `class ScanTextBuilder`
  - `__init__` (method, line 19) `def __init__(self, config)`
  - `build_for_node` (method, line 27) `def build_for_node(self, node, content, imports)`
  - `build_corpus` (method, line 67) `def build_corpus(self, nodes, content_map, edges)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`

## readmenator/_security.py
- Doc: Pattern-based static security analysis for the readmenator knowledge graph.
- Layer: utility
- Language: py
- Symbols:
  - `SecurityRule` (class, line 24) `class SecurityRule`
  - `_parse_minimal_yaml` (function, line 46) `def _parse_minimal_yaml(text)`
  - `_unquote` (function, line 121) `def _unquote(s)`
  - `_load_rules_from_yaml` (function, line 128) `def _load_rules_from_yaml(yaml_path)`
  - `_compile` (function, line 148) `def _compile()`
  - `_python_rules` (function, line 153) `def _python_rules()`
  - `_javascript_rules` (function, line 182) `def _javascript_rules()`
  - `_c_rules` (function, line 201) `def _c_rules()`
  - `_java_rules` (function, line 222) `def _java_rules()`
  - `_go_rules` (function, line 237) `def _go_rules()`
  - `_ruby_rules` (function, line 250) `def _ruby_rules()`
  - `_php_rules` (function, line 267) `def _php_rules()`
  - `_shell_rules` (function, line 284) `def _shell_rules()`
  - `_csharp_rules` (function, line 297) `def _csharp_rules()`
  - `_kotlin_rules` (function, line 310) `def _kotlin_rules()`
  - `_swift_rules` (function, line 321) `def _swift_rules()`
  - `_scala_rules` (function, line 332) `def _scala_rules()`
  - `_lua_rules` (function, line 343) `def _lua_rules()`
  - `_dart_rules` (function, line 354) `def _dart_rules()`
  - `_rust_rules` (function, line 365) `def _rust_rules()`
  - `_nim_rules` (function, line 376) `def _nim_rules()`
  - `_gdscript_rules` (function, line 387) `def _gdscript_rules()`
  - `_elixir_rules` (function, line 398) `def _elixir_rules()`
  - `_build_rules_from_yaml` (function, line 447) `def _build_rules_from_yaml(yaml_path)`
  - `SecurityAnalyzer` (class, line 486) `class SecurityAnalyzer`
  - `fix_hint_for` (function, line 620) `def fix_hint_for(finding)`
  - `__init__` (method, line 496) `def __init__(self, config)`
  - `_resolve_rules` (method, line 500) `def _resolve_rules(self)`
  - `_meets_threshold` (method, line 509) `def _meets_threshold(self, severity)`
  - `scan` (method, line 513) `def scan(self, root)`
  - `_validate_path` (method, line 555) `def _validate_path(self, path, root)`
  - `summary` (method, line 572) `def summary(self, findings)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`

## readmenator/_skill_installer.py
- Doc: Installs the packaged ReadMenator agent skills into a project.
- Layer: utility
- Language: py
- Symbols:
  - `SkillInstaller` (class, line 22) `class SkillInstaller`
  - `__init__` (method, line 25) `def __init__(self, config)`
  - `source_dir` (method, line 34) `def source_dir()`
  - `available` (method, line 38) `def available(self)`
  - `target_dir` (method, line 48) `def target_dir(self, project_root, target)`
  - `install` (method, line 61) `def install(self, project_root, target)`
  - `maybe_install_on_run` (method, line 87) `def maybe_install_on_run(self, project_root)`
- Depends on: `readmenator/_config.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_memory.py`

## readmenator/_sourceview.py
- Doc: Source viewer payload builder for the graph explorers.
- Layer: utility
- Language: py
- Symbols:
  - `SourceEntry` (class, line 20) `class SourceEntry`
  - `SourceViewBuilder` (class, line 36) `class SourceViewBuilder`
  - `__init__` (method, line 39) `def __init__(self, config)`
  - `enabled` (method, line 47) `def enabled(self)`
  - `build_sources` (method, line 55) `def build_sources(self, nodes, content_map)`
  - `build_reasons` (method, line 70) `def build_reasons(self, nodes, content_map)`
  - `_build` (method, line 89) `def _build(self, nodes, content_map)`
  - `to_payload` (method, line 149) `def to_payload(self, sources)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_explorer.py`, `readmenator/_forcegraph.py`, `readmenator/_pipeline.py`, `tests/test_sourceview.py`

## readmenator/_symindex.py
- Doc: Deterministic symbol index with call-site resolution.
- Layer: utility
- Language: py
- Symbols:
  - `_receiver_text` (function, line 42) `def _receiver_text(node)`
  - `SymbolDef` (class, line 56) `class SymbolDef`
  - `CallSite` (class, line 81) `class CallSite`
  - `ResolvedCall` (class, line 102) `class ResolvedCall`
  - `_kind_to_node_type` (function, line 122) `def _kind_to_node_type(kind)`
  - `SymbolIndex` (class, line 132) `class SymbolIndex`
  - `__init__` (method, line 135) `def __init__(self, config)`
  - `build` (method, line 144) `def build(self, nodes, content_map)`
  - `methods_index` (method, line 184) `def methods_index(self, index)`
  - `extract_call_sites` (method, line 212) `def extract_call_sites(self, file_id, content, language, symbols)`
  - `resolve` (method, line 237) `def resolve(self, nodes, edges, resolved_edges, content_map)`
  - `_resolve_one` (method, line 286) `def _resolve_one(self, site, by_name, imports_of)`
  - `_edge_call_sites` (method, line 331) `def _edge_call_sites(self, edges)`
  - `_python_call_sites` (method, line 348) `def _python_call_sites(self, file_id, content)`
  - `_regex_call_sites` (method, line 422) `def _regex_call_sites(self, file_id, content, symbols)`
  - `_Visitor` (class, line 365) `class _Visitor(NodeVisitor)`
  - `_push` (method, line 368) `def _push(self, node)`
  - `_pop` (method, line 374) `def _pop(self, node)`
  - `visit_ClassDef` (method, line 379) `def visit_ClassDef(self, node)`
  - `visit_FunctionDef` (method, line 385) `def visit_FunctionDef(self, node)`
  - `visit_AsyncFunctionDef` (method, line 391) `def visit_AsyncFunctionDef(self, node)`
  - `visit_Call` (method, line 397) `def visit_Call(self, node)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_apidocs.py`, `readmenator/_components.py`, `readmenator/_flowcharts.py`, `readmenator/_linter.py`, `readmenator/_pipeline.py`, `tests/test_symindex.py`

## readmenator/_taint.py
- Doc: Taint propagation analysis of dangerous imports through the resolved import graph.
- Layer: utility
- Language: py
- Symbols:
  - `TaintAnalyzer` (class, line 12) `class TaintAnalyzer`
  - `__init__` (method, line 73) `def __init__(self, config)`
  - `analyze` (method, line 77) `def analyze(self, nodes, edges, resolved_edges)`
  - `_find_direct_sources` (method, line 136) `def _find_direct_sources(self, nodes, edges)`
  - `_propagate` (method, line 162) `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)`
  - `_build_forward_graph` (method, line 213) `def _build_forward_graph(nodes, resolved_edges)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`

## readmenator/_uml.py
- Doc: UML class diagram renderer (Mermaid classDiagram) and 12-language stub generator.
- Layer: utility
- Language: py
- Symbols:
  - `UmlGenerator` (class, line 34) `class UmlGenerator`
  - `_get_code_generator` (function, line 172) `def _get_code_generator(language)`
  - `_type_map_py_to_target` (function, line 190) `def _type_map_py_to_target(target, py_type_hint)`
  - `_generate_cpp` (function, line 233) `def _generate_cpp(class_symbols, nodes, edges)`
  - `_cpp_params` (function, line 259) `def _cpp_params(params)`
  - `_generate_java` (function, line 274) `def _generate_java(class_symbols, nodes, edges)`
  - `_java_params` (function, line 301) `def _java_params(params)`
  - `_generate_csharp` (function, line 316) `def _generate_csharp(class_symbols, nodes, edges)`
  - `_cs_params` (function, line 345) `def _cs_params(params)`
  - `_generate_python` (function, line 360) `def _generate_python(class_symbols, nodes, edges)`
  - `_generate_go` (function, line 395) `def _generate_go(class_symbols, nodes, edges)`
  - `_generate_rust` (function, line 422) `def _generate_rust(class_symbols, nodes, edges)`
  - `_generate_php` (function, line 448) `def _generate_php(class_symbols, nodes, edges)`
  - `_generate_kotlin` (function, line 476) `def _generate_kotlin(class_symbols, nodes, edges)`
  - `_generate_scala` (function, line 496) `def _generate_scala(class_symbols, nodes, edges)`
  - `_generate_swift` (function, line 518) `def _generate_swift(class_symbols, nodes, edges)`
  - `_generate_dart` (function, line 547) `def _generate_dart(class_symbols, nodes, edges)`
  - `_generate_ruby` (function, line 567) `def _generate_ruby(class_symbols, nodes, edges)`
  - `_safe_name` (function, line 588) `def _safe_name(name)`
  - `_extract_params` (function, line 592) `def _extract_params(signature)`
  - `__init__` (method, line 36) `def __init__(self, config)`
  - `render_mermaid_class_diagram` (method, line 39) `def render_mermaid_class_diagram(self, nodes, edges)`
  - `generate_code` (method, line 129) `def generate_code(self, nodes, edges, target_language)`
  - `_sanitize_id` (method, line 153) `def _sanitize_id(raw)`
  - `_find_node` (method, line 165) `def _find_node(nodes, node_id)`
- Depends on: `readmenator/_config.py`, `readmenator/_models.py`
- Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`

## readmenator/_uncertainty.py
- Doc: Uncertainty engine: classify candidate edges, never invent facts.
- Layer: utility
- Language: py
- Symbols:
  - `_bucket_evidence` (function, line 50) `def _bucket_evidence(evidence)`
  - `_bucket_target` (function, line 67) `def _bucket_target(callee)`
  - `featurize` (function, line 83) `def featurize(edge, known_observed)`
  - `UncertaintyPrediction` (class, line 93) `class UncertaintyPrediction`
  - `HeuristicScorer` (class, line 101) `class HeuristicScorer`
  - `RandomForestScorer` (class, line 138) `class RandomForestScorer`
  - `_sigmoid` (function, line 180) `def _sigmoid(x)`
  - `predict_uncertain_edges` (function, line 187) `def predict_uncertain_edges(candidate_edges, known_observed, config, min_confidence, scorer)`
  - `prediction_edges` (function, line 214) `def prediction_edges(predictions, provenance_version)`
  - `score` (method, line 129) `def score(self, features)`
  - `__init__` (method, line 143) `def __init__(self, n_estimators, random_state)`
  - `available` (method, line 149) `def available()`
  - `fit` (method, line 156) `def fit(self, x, y)`
  - `score` (method, line 171) `def score(self, features)`
- Depends on: `readmenator/_config.py`, `readmenator/_receipts.py`
- Imported by: `readmenator/_app.py`, `tests/test_receipts.py`


Next: [KB_readmenator_p5.md](KB_readmenator_p5.md)
