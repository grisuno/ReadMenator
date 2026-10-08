# Subsystem: readmenator (page 4 of 4)
Previous: [KB_readmenator_p3.md](KB_readmenator_p3.md)

## readmenator/_wiki.py
- Doc: Deterministic agent wiki generator for readmenator.
- Layer: utility
- Language: py
- Symbols:
  - `_is_garbage_purpose` (function, line 47) `def _is_garbage_purpose(text)`
  - `_slug` (function, line 55) `def _slug(text)`
  - `existing_ids` (function, line 62) `def existing_ids(connections)`
  - `_display_names` (function, line 72) `def _display_names(communities)`
  - `WikiGenerator` (class, line 86) `class WikiGenerator`
  - `__init__` (method, line 89) `def __init__(self, config)`
  - `generate` (method, line 94) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)`
  - `_write_concepts` (method, line 143) `def _write_concepts(self, out_dir, analysis_v2)`
  - `_prune_stale_pages` (method, line 210) `def _prune_stale_pages(self, out_dir, current)`
  - `lint` (method, line 219) `def lint(self, project_root)`
  - `_resolve_communities` (method, line 242) `def _resolve_communities(self, nodes, analysis, resolved)`
  - `_community_of` (method, line 268) `def _community_of(self, node_id, communities)`
  - `_build_connections` (method, line 277) `def _build_connections(self, communities, resolved, analysis, node_map, layers)`
  - `_duplicate_links` (method, line 342) `def _duplicate_links(communities, node_map, skip_pairs)`
  - `_shared_context_links` (method, line 385) `def _shared_context_links(self, communities, existing, node_map, layers)`
  - `_shared_context` (method, line 421) `def _shared_context(first, second, node_map, layers)`
  - `_build_connections_json` (method, line 454) `def _build_connections_json(self, connections)`
  - `_definition_for` (method, line 458) `def _definition_for(self, community, node_map)`
  - `_file_row` (method, line 487) `def _file_row(self, fid, node_map, layers)`
  - `_build_grouped_files` (method, line 501) `def _build_grouped_files(self, members, node_map, layers, max_files)`
  - `_build_community_page` (method, line 550) `def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)`
  - `_questions_for` (method, line 703) `def _questions_for(self, community, node_map, member_set, analysis_v2)`
  - `_large_files` (method, line 741) `def _large_files(self, nodes, project_root)`
  - `_build_index` (method, line 754) `def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections...`
  - `_overview_paragraph` (method, line 866) `def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)`
  - `_connective_paragraph` (method, line 899) `def _connective_paragraph(self, communities, connections)`
  - `_questions_paragraph` (method, line 920) `def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)`
  - `_build_queries` (method, line 936) `def _build_queries(self, analysis)`
  - `_build_report` (method, line 961) `def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name...`
  - `_estimate_tokens` (method, line 1033) `def _estimate_tokens(self, nodes, connections)`
  - `_write` (method, line 1044) `def _write(path, content)`
  - `dominant` (method, line 428) `def dominant(ids, key)`
- Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_purpose.py`, `readmenator/_security.py`
- Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`

## readmenator/_yaralite.py
- Doc: Zero-dependency YARA-lite rule parser and runner.
- Layer: utility
- Language: py
- Symbols:
  - `YaraLiteString` (class, line 24) `class YaraLiteString`
  - `YaraLiteRule` (class, line 33) `class YaraLiteRule`
  - `YaraLiteHit` (class, line 56) `class YaraLiteHit`
  - `YaraLiteMatch` (class, line 66) `class YaraLiteMatch`
  - `parse_yaralite_rules` (method, line 76) `def parse_yaralite_rules(rules_text)`
  - `run_yaralite_rules` (method, line 112) `def run_yaralite_rules(text, rules)`
  - `validate_yaralite_rules` (method, line 139) `def validate_yaralite_rules(rules_text)`
  - `_rule_blocks` (method, line 161) `def _rule_blocks(rules_text)`
  - `_section` (method, line 182) `def _section(body, start_marker, end_marker)`
  - `_parse_meta` (method, line 196) `def _parse_meta(meta_body)`
  - `_parse_strings` (method, line 215) `def _parse_strings(strings_body)`
  - `_strip_comments` (method, line 233) `def _strip_comments(text)`
  - `_decode_yara_string` (method, line 238) `def _decode_yara_string(value)`
  - `_string_hits` (method, line 243) `def _string_hits(text, rule)`
  - `_condition_matches` (method, line 265) `def _condition_matches(condition, hits)`
  - `_confidence` (method, line 305) `def _confidence(value)`
  - `_excerpt` (method, line 322) `def _excerpt(text, offset, length)`
  - `tier` (method, line 42) `def tier(self)`
  - `replace_group` (method, line 270) `def replace_group(match)`
  - `replace_identifier` (method, line 292) `def replace_identifier(match)`
- Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`

