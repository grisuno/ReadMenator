# Symbols (page 4 of 7)
Previous: [SYMBOLS_p3.md](SYMBOLS_p3.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
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
| `dominant` | function | `readmenator/_wiki.py:428` | `def dominant(ids, key)` |
| `existing_ids` | function | `readmenator/_wiki.py:62` | `def existing_ids(connections)` |
| `generate` | method | `readmenator/_wiki.py:94` | `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)` |
| `lint` | method | `readmenator/_wiki.py:219` | `def lint(self, project_root)` |
| `YaraLiteHit` | class | `readmenator/_yaralite.py:56` | `class YaraLiteHit` |
| `YaraLiteMatch` | class | `readmenator/_yaralite.py:66` | `class YaraLiteMatch` |
| `YaraLiteRule` | class | `readmenator/_yaralite.py:33` | `class YaraLiteRule` |
| `YaraLiteString` | class | `readmenator/_yaralite.py:24` | `class YaraLiteString` |
| `_condition_matches` | function | `readmenator/_yaralite.py:265` | `def _condition_matches(condition, hits)` |
| `_confidence` | function | `readmenator/_yaralite.py:305` | `def _confidence(value)` |
| `_decode_yara_string` | function | `readmenator/_yaralite.py:238` | `def _decode_yara_string(value)` |
| `_excerpt` | function | `readmenator/_yaralite.py:322` | `def _excerpt(text, offset, length)` |
| `_parse_meta` | function | `readmenator/_yaralite.py:196` | `def _parse_meta(meta_body)` |
| `_parse_strings` | function | `readmenator/_yaralite.py:215` | `def _parse_strings(strings_body)` |
| `_rule_blocks` | function | `readmenator/_yaralite.py:161` | `def _rule_blocks(rules_text)` |
| `_section` | function | `readmenator/_yaralite.py:182` | `def _section(body, start_marker, end_marker)` |
| `_string_hits` | function | `readmenator/_yaralite.py:243` | `def _string_hits(text, rule)` |
| `_strip_comments` | function | `readmenator/_yaralite.py:233` | `def _strip_comments(text)` |
| `parse_yaralite_rules` | function | `readmenator/_yaralite.py:76` | `def parse_yaralite_rules(rules_text)` |
| `replace_group` | function | `readmenator/_yaralite.py:270` | `def replace_group(match)` |
| `replace_identifier` | function | `readmenator/_yaralite.py:292` | `def replace_identifier(match)` |
| `run_yaralite_rules` | function | `readmenator/_yaralite.py:112` | `def run_yaralite_rules(text, rules)` |
| `tier` | method | `readmenator/_yaralite.py:42` | `def tier(self)` |
| `validate_yaralite_rules` | function | `readmenator/_yaralite.py:139` | `def validate_yaralite_rules(rules_text)` |
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
| `__init__` | method | `readmenator_orchestrator.py:198` | `def __init__(self, config, github_client)` |
| `__init__` | method | `readmenator_orchestrator.py:367` | `def __init__(self, config)` |
| `_build_readmenator_command` | method | `readmenator_orchestrator.py:283` | `def _build_readmenator_command(self, repo_dir)` |
| `_cleanup_temp_dir` | method | `readmenator_orchestrator.py:361` | `def _cleanup_temp_dir(temp_dir)` |
| `_clone_repository` | method | `readmenator_orchestrator.py:247` | `def _clone_repository(self, repo)` |
| `_commit_and_push` | method | `readmenator_orchestrator.py:313` | `def _commit_and_push(self, repo_dir, repo)` |
| `_copy_to_docs_dir` | method | `readmenator_orchestrator.py:293` | `def _copy_to_docs_dir(self, repo_dir, generated_file)` |
| `_get_default_branch` | method | `readmenator_orchestrator.py:231` | `def _get_default_branch(self, repo)` |
| `_resolve_user` | method | `readmenator_orchestrator.py:89` | `def _resolve_user(self)` |
| `_run_readmenator` | method | `readmenator_orchestrator.py:263` | `def _run_readmenator(self, repo_dir)` |
| `_safe_env` | function | `readmenator_orchestrator.py:68` | `def _safe_env()` |
| `_setup_git_auth` | method | `readmenator_orchestrator.py:110` | `def _setup_git_auth(self)` |
| `_validate_branch_name` | function | `readmenator_orchestrator.py:62` | `def _validate_branch_name(name)` |
| `_validate_repo_name` | function | `readmenator_orchestrator.py:56` | `def _validate_repo_name(name)` |
| `close_existing_prs` | method | `readmenator_orchestrator.py:136` | `def close_existing_prs(self, repo)` |
| `create_pr` | method | `readmenator_orchestrator.py:176` | `def create_pr(self, repo, default_branch, timestamp)` |
| `delete_remote_branch` | method | `readmenator_orchestrator.py:164` | `def delete_remote_branch(self, repo)` |
| `list_repos` | method | `readmenator_orchestrator.py:124` | `def list_repos(self)` |
| `main` | function | `readmenator_orchestrator.py:498` | `def main()` |
| `parse_arguments` | function | `readmenator_orchestrator.py:481` | `def parse_arguments()` |
| `process` | method | `readmenator_orchestrator.py:202` | `def process(self, repo)` |
| `run` | method | `readmenator_orchestrator.py:372` | `def run(self, dry_run, only_repo)` |
| `setUp` | method | `readmenator_orchestrator.py:422` | `def setUp(self)` |
| `tearDown` | method | `readmenator_orchestrator.py:426` | `def tearDown(self)` |
| `test_branch_name_validation` | method | `readmenator_orchestrator.py:472` | `def test_branch_name_validation(self)` |
| `test_config_defaults` | method | `readmenator_orchestrator.py:433` | `def test_config_defaults(self)` |
| `test_config_immutability` | method | `readmenator_orchestrator.py:429` | `def test_config_immutability(self)` |
| `test_pr_body_mentions_concept_layer` | method | `readmenator_orchestrator.py:452` | `def test_pr_body_mentions_concept_layer(self)` |
| `test_rebuild_command_includes_full_concept_layer` | method | `readmenator_orchestrator.py:441` | `def test_rebuild_command_includes_full_concept_layer(self)` |
| `test_repo_name_validation` | method | `readmenator_orchestrator.py:462` | `def test_repo_name_validation(self)` |
| `test_skip_repos_logic` | method | `readmenator_orchestrator.py:458` | `def test_skip_repos_logic(self)` |
| `TestAgentOutputBudget` | class | `tests/test_agent_friendliness.py:55` | `class TestAgentOutputBudget(TestCase)` |
| `TestAgentOutputSignal` | class | `tests/test_agent_friendliness.py:110` | `class TestAgentOutputSignal(TestCase)` |
| `TestCommunityHubDamping` | class | `tests/test_agent_friendliness.py:308` | `class TestCommunityHubDamping(TestCase)` |
| `TestCommunityShaping` | class | `tests/test_agent_friendliness.py:363` | `class TestCommunityShaping(TestCase)` |
| `TestGalleryIndex` | class | `tests/test_agent_friendliness.py:456` | `class TestGalleryIndex(TestCase)` |
| `TestLiveMapCommunities` | class | `tests/test_agent_friendliness.py:514` | `class TestLiveMapCommunities(TestCase)` |
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
| `_inputs` | method | `tests/test_agent_friendliness.py:517` | `def _inputs(self)` |
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
| `test_built_maps_carry_community_and_core_role` | method | `tests/test_agent_friendliness.py:533` | `def test_built_maps_carry_community_and_core_role(self)` |
| `test_check_freshness_detects_source_edits` | method | `tests/test_agent_friendliness.py:343` | `def test_check_freshness_detects_source_edits(self)` |
| `test_communities_survive_a_shared_hub` | method | `tests/test_agent_friendliness.py:311` | `def test_communities_survive_a_shared_hub(self)` |
| `test_community_label_ignores_test_directory` | method | `tests/test_agent_friendliness.py:446` | `def test_community_label_ignores_test_directory(self)` |
| `test_doc_preview_skips_markdown_syntax` | method | `tests/test_agent_friendliness.py:507` | `def test_doc_preview_skips_markdown_syntax(self)` |
| `test_fingerprint_changes_with_content_not_with_order` | method | `tests/test_agent_friendliness.py:332` | `def test_fingerprint_changes_with_content_not_with_order(self)` |
| `test_gallery_footer_links_github_and_pypi` | method | `tests/test_agent_friendliness.py:497` | `def test_gallery_footer_links_github_and_pypi(self)` |
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
| `test_vis_render_includes_legend_and_dot_scaling` | method | `tests/test_agent_friendliness.py:542` | `def test_vis_render_includes_legend_and_dot_scaling(self)` |
| `TestAgentInjectorEdgeCases` | class | `tests/test_agent_injector.py:241` | `class TestAgentInjectorEdgeCases(TestCase)` |
| `TestAgentInjectorFindFiles` | class | `tests/test_agent_injector.py:204` | `class TestAgentInjectorFindFiles(TestCase)` |
| `TestAgentInjectorInjectBehavior` | class | `tests/test_agent_injector.py:19` | `class TestAgentInjectorInjectBehavior(TestCase)` |
| `TestAgentInjectorRemoveBehavior` | class | `tests/test_agent_injector.py:161` | `class TestAgentInjectorRemoveBehavior(TestCase)` |
| `setUp` | method | `tests/test_agent_injector.py:22` | `def setUp(self)` |
| `setUp` | method | `tests/test_agent_injector.py:164` | `def setUp(self)` |
| `setUp` | method | `tests/test_agent_injector.py:207` | `def setUp(self)` |
| `setUp` | method | `tests/test_agent_injector.py:244` | `def setUp(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:27` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:169` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:211` | `def tearDown(self)` |
| `tearDown` | method | `tests/test_agent_injector.py:249` | `def tearDown(self)` |
| `test_custom_kb_filename_works` | method | `tests/test_agent_injector.py:138` | `def test_custom_kb_filename_works(self)` |
| `test_finds_agents_md` | method | `tests/test_agent_injector.py:214` | `def test_finds_agents_md(self)` |
| `test_finds_all_listed_files` | method | `tests/test_agent_injector.py:220` | `def test_finds_all_listed_files(self)` |
| `test_finds_cursor_rules_glob` | method | `tests/test_agent_injector.py:227` | `def test_finds_cursor_rules_glob(self)` |
| `test_inject_does_not_execute_commands` | method | `tests/test_agent_injector.py:153` | `def test_inject_does_not_execute_commands(self)` |
| `test_inject_does_not_touch_unlisted_files` | method | `tests/test_agent_injector.py:268` | `def test_inject_does_not_touch_unlisted_files(self)` |
| `test_inject_into_agents_md_adds_kb_link` | method | `tests/test_agent_injector.py:30` | `def test_inject_into_agents_md_adds_kb_link(self)` |
| `test_inject_into_claude_md_adds_kb_link` | method | `tests/test_agent_injector.py:39` | `def test_inject_into_claude_md_adds_kb_link(self)` |
| `test_inject_into_cursor_rules_mdc_glob` | method | `tests/test_agent_injector.py:89` | `def test_inject_into_cursor_rules_mdc_glob(self)` |
| `test_inject_into_cursorrules_adds_kb_link` | method | `tests/test_agent_injector.py:49` | `def test_inject_into_cursorrules_adds_kb_link(self)` |
| `test_inject_into_empty_file` | method | `tests/test_agent_injector.py:252` | `def test_inject_into_empty_file(self)` |
| `test_inject_into_github_copilot_instructions` | method | `tests/test_agent_injector.py:57` | `def test_inject_into_github_copilot_instructions(self)` |
| `test_inject_is_idempotent_does_not_duplicate` | method | `tests/test_agent_injector.py:99` | `def test_inject_is_idempotent_does_not_duplicate(self)` |
| `test_inject_multiple_agent_files` | method | `tests/test_agent_injector.py:122` | `def test_inject_multiple_agent_files(self)` |
| `test_inject_no_agent_files_returns_zero` | method | `tests/test_agent_injector.py:110` | `def test_inject_no_agent_files_returns_zero(self)` |
| `test_inject_plain_text_format_for_yaml` | method | `tests/test_agent_injector.py:129` | `def test_inject_plain_text_format_for_yaml(self)` |
| `test_inject_preserves_existing_content` | method | `tests/test_agent_injector.py:114` | `def test_inject_preserves_existing_content(self)` |
| `test_inject_replaces_old_injection_without_regen_command` | method | `tests/test_agent_injector.py:67` | `def test_inject_replaces_old_injection_without_regen_command(self)` |
| `test_inject_respects_custom_agent_files_list` | method | `tests/test_agent_injector.py:260` | `def test_inject_respects_custom_agent_files_list(self)` |
| `test_inject_skips_when_already_up_to_date` | method | `tests/test_agent_injector.py:82` | `def test_inject_skips_when_already_up_to_date(self)` |
| `test_injection_includes_regeneration_command` | method | `tests/test_agent_injector.py:146` | `def test_injection_includes_regeneration_command(self)` |
| `test_remove_no_files_returns_zero` | method | `tests/test_agent_injector.py:189` | `def test_remove_no_files_returns_zero(self)` |
| `test_remove_preserves_original_content` | method | `tests/test_agent_injector.py:193` | `def test_remove_preserves_original_content(self)` |
| `test_remove_strips_injected_section` | method | `tests/test_agent_injector.py:172` | `def test_remove_strips_injected_section(self)` |
| `test_remove_without_injection_returns_zero` | method | `tests/test_agent_injector.py:183` | `def test_remove_without_injection_returns_zero(self)` |
| `test_returns_empty_when_no_files` | method | `tests/test_agent_injector.py:236` | `def test_returns_empty_when_no_files(self)` |
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
| `TestApiDocsIntegration` | class | `tests/test_apidocs.py:541` | `class TestApiDocsIntegration(TestCase)` |
| `TestApiReferenceBuilder` | class | `tests/test_apidocs.py:257` | `class TestApiReferenceBuilder(TestCase)` |
| `TestApiRendering` | class | `tests/test_apidocs.py:403` | `class TestApiRendering(TestCase)` |
| `TestDocstringParser` | class | `tests/test_apidocs.py:163` | `class TestDocstringParser(TestCase)` |
| `TestSignatureParsing` | class | `tests/test_apidocs.py:380` | `class TestSignatureParsing(TestCase)` |
| `_project` | function | `tests/test_apidocs.py:144` | `def _project()` |
| `setUpClass` | method | `tests/test_apidocs.py:261` | `def setUpClass(cls)` |
| `setUpClass` | method | `tests/test_apidocs.py:407` | `def setUpClass(cls)` |
| `test_apidocs_annotated_receiver_resolves_method` | method | `tests/test_apidocs.py:332` | `def test_apidocs_annotated_receiver_resolves_method(self)` |
| `test_apidocs_app_export_and_scanner_skip` | method | `tests/test_apidocs.py:544` | `def test_apidocs_app_export_and_scanner_skip(self)` |
| `test_apidocs_c_prototype_doc_merges_into_definition` | method | `tests/test_apidocs.py:314` | `def test_apidocs_c_prototype_doc_merges_into_definition(self)` |
| `test_apidocs_call_graph_resolved` | method | `tests/test_apidocs.py:322` | `def test_apidocs_call_graph_resolved(self)` |
| `test_apidocs_constructor_inherits_class_args` | method | `tests/test_apidocs.py:301` | `def test_apidocs_constructor_inherits_class_args(self)` |
| `test_apidocs_coverage_counts` | method | `tests/test_apidocs.py:346` | `def test_apidocs_coverage_counts(self)` |
| `test_apidocs_deterministic` | method | `tests/test_apidocs.py:352` | `def test_apidocs_deterministic(self)` |
| `test_apidocs_entity_budget_truncates` | method | `tests/test_apidocs.py:368` | `def test_apidocs_entity_budget_truncates(self)` |
| `test_apidocs_hierarchy_nests_subclasses` | method | `tests/test_apidocs.py:429` | `def test_apidocs_hierarchy_nests_subclasses(self)` |
| `test_apidocs_html_compression_disabled_keeps_plain_json` | method | `tests/test_apidocs.py:464` | `def test_apidocs_html_compression_disabled_keeps_plain_json(self)` |
| `test_apidocs_html_is_self_contained_and_escaped` | method | `tests/test_apidocs.py:442` | `def test_apidocs_html_is_self_contained_and_escaped(self)` |
| `test_apidocs_html_large_payload_is_gzip_base64` | method | `tests/test_apidocs.py:454` | `def test_apidocs_html_large_payload_is_gzip_base64(self)` |
| `test_apidocs_html_placeholder_in_payload_stays_literal` | method | `tests/test_apidocs.py:450` | `def test_apidocs_html_placeholder_in_payload_stays_literal(self)` |
| `test_apidocs_inheritance_links_and_doc_inheritance` | method | `tests/test_apidocs.py:305` | `def test_apidocs_inheritance_links_and_doc_inheritance(self)` |
| `test_apidocs_linker_resolves_references` | method | `tests/test_apidocs.py:433` | `def test_apidocs_linker_resolves_references(self)` |
| `test_apidocs_module_page_sections` | method | `tests/test_apidocs.py:418` | `def test_apidocs_module_page_sections(self)` |
| `test_apidocs_pages_layout` | method | `tests/test_apidocs.py:413` | `def test_apidocs_pages_layout(self)` |
| `test_apidocs_privacy_mode_strips_text` | method | `tests/test_apidocs.py:360` | `def test_apidocs_privacy_mode_strips_text(self)` |
| `test_apidocs_python_all_and_private_filter` | method | `tests/test_apidocs.py:285` | `def test_apidocs_python_all_and_private_filter(self)` |
| `test_apidocs_python_nesting_and_kinds` | method | `tests/test_apidocs.py:277` | `def test_apidocs_python_nesting_and_kinds(self)` |
| `test_apidocs_python_signatures_exact` | method | `tests/test_apidocs.py:265` | `def test_apidocs_python_signatures_exact(self)` |
| `test_apidocs_receiver_filter_drops_unproven_method_calls` | method | `tests/test_apidocs.py:328` | `def test_apidocs_receiver_filter_drops_unproven_method_calls(self)` |
| `test_apidocs_signature_languages` | method | `tests/test_apidocs.py:383` | `def test_apidocs_signature_languages(self)` |
| `test_apidocs_tests_excluded_by_default` | method | `tests/test_apidocs.py:294` | `def test_apidocs_tests_excluded_by_default(self)` |
| `test_apidocs_warnings_cover_every_rule` | method | `tests/test_apidocs.py:336` | `def test_apidocs_warnings_cover_every_rule(self)` |
| `test_apidocs_without_content_uses_parser_symbols` | method | `tests/test_apidocs.py:374` | `def test_apidocs_without_content_uses_parser_symbols(self)` |
| `test_apidocs_writer_jsonl_one_file_per_module_one_line_per_entity` | method | `tests/test_apidocs.py:485` | `def test_apidocs_writer_jsonl_one_file_per_module_one_line_per_entity(self)` |
| `test_apidocs_writer_prunes_stale_jsonl_and_monolith` | method | `tests/test_apidocs.py:512` | `def test_apidocs_writer_prunes_stale_jsonl_and_monolith(self)` |
| `test_apidocs_writer_refuses_symlinked_output` | method | `tests/test_apidocs.py:529` | `def test_apidocs_writer_refuses_symlinked_output(self)` |
| `test_apidocs_writer_writes_and_prunes` | method | `tests/test_apidocs.py:470` | `def test_apidocs_writer_writes_and_prunes(self)` |
| `test_docstrings_csharp_xml` | method | `tests/test_apidocs.py:222` | `def test_docstrings_csharp_xml(self)` |
| `test_docstrings_google_sections` | method | `tests/test_apidocs.py:166` | `def test_docstrings_google_sections(self)` |
| `test_docstrings_jsdoc_and_doxygen_tags` | method | `tests/test_apidocs.py:203` | `def test_docstrings_jsdoc_and_doxygen_tags(self)` |
| `test_docstrings_numpy_sections` | method | `tests/test_apidocs.py:181` | `def test_docstrings_numpy_sections(self)` |
| `test_docstrings_phpdoc_type_before_variable` | method | `tests/test_apidocs.py:218` | `def test_docstrings_phpdoc_type_before_variable(self)` |
| `test_docstrings_plain_and_empty` | method | `tests/test_apidocs.py:237` | `def test_docstrings_plain_and_empty(self)` |
| `test_docstrings_recover_block_and_line_comments` | method | `tests/test_apidocs.py:244` | `def test_docstrings_recover_block_and_line_comments(self)` |
| `test_docstrings_recover_elixir_doc_heredoc` | method | `tests/test_apidocs.py:252` | `def test_docstrings_recover_elixir_doc_heredoc(self)` |
| `test_docstrings_rest_fields_and_directives` | method | `tests/test_apidocs.py:191` | `def test_docstrings_rest_fields_and_directives(self)` |
| `test_docstrings_rustdoc_sections` | method | `tests/test_apidocs.py:231` | `def test_docstrings_rustdoc_sections(self)` |
| `TestBundleGraphAppContract` | class | `tests/test_bundlegraph.py:172` | `class TestBundleGraphAppContract(TestCase)` |
| `TestBundleGraphPayloadContract` | class | `tests/test_bundlegraph.py:58` | `class TestBundleGraphPayloadContract(TestCase)` |
| `TestBundleGraphRenderContract` | class | `tests/test_bundlegraph.py:108` | `class TestBundleGraphRenderContract(TestCase)` |
| `_config` | method | `tests/test_bundlegraph.py:180` | `def _config(self)` |
| `_fixture` | function | `tests/test_bundlegraph.py:24` | `def _fixture(config)` |
| `_node` | function | `tests/test_bundlegraph.py:19` | `def _node(nid, doc)` |
| `_project` | method | `tests/test_bundlegraph.py:175` | `def _project(self, tmp)` |
| `_script_json` | function | `tests/test_bundlegraph.py:49` | `def _script_json(html, name)` |
| `setUp` | method | `tests/test_bundlegraph.py:61` | `def setUp(self)` |
| `setUp` | method | `tests/test_bundlegraph.py:111` | `def setUp(self)` |
| `test_bundle_page_skipped_when_disabled` | method | `tests/test_bundlegraph.py:201` | `def test_bundle_page_skipped_when_disabled(self)` |
| `test_bundlegraph_edges_are_distinct_file_pairs` | method | `tests/test_bundlegraph.py:73` | `def test_bundlegraph_edges_are_distinct_file_pairs(self)` |
| `test_bundlegraph_empty_payload` | method | `tests/test_bundlegraph.py:95` | `def test_bundlegraph_empty_payload(self)` |
| `test_bundlegraph_groups_follow_community_order_with_unassigned_last` | method | `tests/test_bundlegraph.py:67` | `def test_bundlegraph_groups_follow_community_order_with_unassigned_last(self)` |
| `test_bundlegraph_hub_leads_its_arc` | method | `tests/test_bundlegraph.py:87` | `def test_bundlegraph_hub_leads_its_arc(self)` |
| `test_bundlegraph_nodes_on_circle_and_sphere` | method | `tests/test_bundlegraph.py:81` | `def test_bundlegraph_nodes_on_circle_and_sphere(self)` |
| `test_bundlegraph_privacy_mode_strips_docs` | method | `tests/test_bundlegraph.py:101` | `def test_bundlegraph_privacy_mode_strips_docs(self)` |
| `test_bundlegraph_render_escapes_untrusted_text` | method | `tests/test_bundlegraph.py:140` | `def test_bundlegraph_render_escapes_untrusted_text(self)` |
| `test_bundlegraph_render_fills_placeholders` | method | `tests/test_bundlegraph.py:118` | `def test_bundlegraph_render_fills_placeholders(self)` |
| `test_bundlegraph_render_has_both_views_and_controls` | method | `tests/test_bundlegraph.py:134` | `def test_bundlegraph_render_has_both_views_and_controls(self)` |
| `test_bundlegraph_render_has_no_network_requests` | method | `tests/test_bundlegraph.py:127` | `def test_bundlegraph_render_has_no_network_requests(self)` |
| `test_bundlegraph_render_payload_naming_a_token_stays_literal` | method | `tests/test_bundlegraph.py:151` | `def test_bundlegraph_render_payload_naming_a_token_stays_literal(self)` |
| `test_bundlegraph_thumbnail_is_safe_svg` | method | `tests/test_bundlegraph.py:157` | `def test_bundlegraph_thumbnail_is_safe_svg(self)` |
| `test_bundlegraph_write_creates_parent` | method | `tests/test_bundlegraph.py:164` | `def test_bundlegraph_write_creates_parent(self)` |
| `test_export_bundlegraph_cli_entry` | method | `tests/test_bundlegraph.py:212` | `def test_export_bundlegraph_cli_entry(self)` |
| `test_export_diagrams_writes_bundle_page_and_card` | method | `tests/test_bundlegraph.py:185` | `def test_export_diagrams_writes_bundle_page_and_card(self)` |
| `test_pages_subdir_card_points_into_maps_dir` | method | `tests/test_bundlegraph.py:222` | `def test_pages_subdir_card_points_into_maps_dir(self)` |
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
| `TestComponentGalleryContract` | class | `tests/test_components.py:238` | `class TestComponentGalleryContract(TestCase)` |
| `TestComponentPageContract` | class | `tests/test_components.py:140` | `class TestComponentPageContract(TestCase)` |
| `TestComponentRenderContract` | class | `tests/test_components.py:94` | `class TestComponentRenderContract(TestCase)` |
| `TestComponentSchemaContract` | class | `tests/test_components.py:46` | `class TestComponentSchemaContract(TestCase)` |
| `_config` | method | `tests/test_components.py:246` | `def _config(self)` |
| `_fixture` | function | `tests/test_components.py:25` | `def _fixture()` |
| `_node` | function | `tests/test_components.py:17` | `def _node(nid)` |
| `_project` | method | `tests/test_components.py:241` | `def _project(self, tmp)` |
| `setUp` | method | `tests/test_components.py:49` | `def setUp(self)` |
| `setUp` | method | `tests/test_components.py:97` | `def setUp(self)` |
| `setUp` | method | `tests/test_components.py:143` | `def setUp(self)` |
| `test_build_records_layers_hub_and_counts` | method | `tests/test_components.py:177` | `def test_build_records_layers_hub_and_counts(self)` |
| `test_card_skipped_when_disabled` | method | `tests/test_components.py:305` | `def test_card_skipped_when_disabled(self)` |
| `test_components_carry_entities_and_file_methods` | method | `tests/test_components.py:67` | `def test_components_carry_entities_and_file_methods(self)` |
| `test_docs_collect_components_overview` | method | `tests/test_components.py:319` | `def test_docs_collect_components_overview(self)` |
| `test_empty_project_yields_empty_diagram` | method | `tests/test_components.py:133` | `def test_empty_project_yields_empty_diagram(self)` |
| `test_export_diagrams_links_components_card` | method | `tests/test_components.py:251` | `def test_export_diagrams_links_components_card(self)` |
| `test_export_pages_links_components_relatively` | method | `tests/test_components.py:266` | `def test_export_pages_links_components_relatively(self)` |
| `test_mermaid_matches_layered_style` | method | `tests/test_components.py:105` | `def test_mermaid_matches_layered_style(self)` |
| `test_methods_index_keys_use_pipe_separator` | method | `tests/test_components.py:89` | `def test_methods_index_keys_use_pipe_separator(self)` |
| `test_nested_relations_roll_up` | method | `tests/test_components.py:331` | `def test_nested_relations_roll_up(self)` |
| `test_overview_lists_related_entities` | method | `tests/test_components.py:118` | `def test_overview_lists_related_entities(self)` |
| `test_overview_prefixes_source_links` | method | `tests/test_components.py:293` | `def test_overview_prefixes_source_links(self)` |
| `test_page_draws_nodes_edges_and_links` | method | `tests/test_components.py:152` | `def test_page_draws_nodes_edges_and_links(self)` |
| `test_page_escapes_untrusted_text` | method | `tests/test_components.py:194` | `def test_page_escapes_untrusted_text(self)` |
| `test_page_has_no_network_requests` | method | `tests/test_components.py:186` | `def test_page_has_no_network_requests(self)` |
| `test_page_nodes_explain_themselves` | method | `tests/test_components.py:162` | `def test_page_nodes_explain_themselves(self)` |
| `test_page_script_is_valid_javascript` | method | `tests/test_components.py:223` | `def test_page_script_is_valid_javascript(self)` |
| `test_relations_link_components_with_call_sites` | method | `tests/test_components.py:78` | `def test_relations_link_components_with_call_sites(self)` |
| `test_relations_section_lists_call_evidence` | method | `tests/test_components.py:171` | `def test_relations_section_lists_call_evidence(self)` |
| `test_sanitize_for_mermaid_ids` | method | `tests/test_components.py:114` | `def test_sanitize_for_mermaid_ids(self)` |
| `test_site_copy_has_no_source_links` | method | `tests/test_components.py:284` | `def test_site_copy_has_no_source_links(self)` |
| `test_thumbnail_is_safe_svg` | method | `tests/test_components.py:204` | `def test_thumbnail_is_safe_svg(self)` |
| `test_top_level_keys_match_schema` | method | `tests/test_components.py:57` | `def test_top_level_keys_match_schema(self)` |
| `test_write_emits_analysis_and_pages` | method | `tests/test_components.py:124` | `def test_write_emits_analysis_and_pages(self)` |
| `test_write_emits_index_page` | method | `tests/test_components.py:213` | `def test_write_emits_index_page(self)` |
| `TestConceptGraphContract` | class | `tests/test_concepts.py:20` | `class TestConceptGraphContract(TestCase)` |
| `_node` | function | `tests/test_concepts.py:8` | `def _node(fid, symbols, doc)` |
| `test_concept_atomic_breakdown_splits_camelcase` | method | `tests/test_concepts.py:53` | `def test_concept_atomic_breakdown_splits_camelcase(self)` |
| `test_concept_deterministic_ordering` | method | `tests/test_concepts.py:62` | `def test_concept_deterministic_ordering(self)` |
| `test_concept_dialectic_questions_for_overlap` | method | `tests/test_concepts.py:85` | `def test_concept_dialectic_questions_for_overlap(self)` |
| `test_concept_disabled_returns_empty_graph` | method | `tests/test_concepts.py:76` | `def test_concept_disabled_returns_empty_graph(self)` |
| `test_concept_nouns_map_to_file_sets` | method | `tests/test_concepts.py:21` | `def test_concept_nouns_map_to_file_sets(self)` |
| `test_concept_verbs_come_from_structural_edges` | method | `tests/test_concepts.py:36` | `def test_concept_verbs_come_from_structural_edges(self)` |
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

Next: [SYMBOLS_p5.md](SYMBOLS_p5.md)
