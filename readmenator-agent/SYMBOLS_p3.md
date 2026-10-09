# Symbols (page 3 of 5)
Previous: [SYMBOLS_p2.md](SYMBOLS_p2.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `dependencies_available` | function | `readmenator/_video.py:221` | `def dependencies_available()` |
| `draw_caption` | method | `readmenator/_video.py:448` | `def draw_caption(d, text, lt, dur, fonts, width, y)` |
| `draw_grid` | method | `readmenator/_video.py:332` | `def draw_grid(img, t, strength, bd)` |
| `draw_header` | method | `readmenator/_video.py:434` | `def draw_header(img, d, gt, total, project, act_label, fonts, width)` |
| `draw_sun` | method | `readmenator/_video.py:352` | `def draw_sun(img, a, bd, cy)` |
| `ease` | function | `readmenator/_video.py:88` | `def ease(x)` |
| `emergence_frames` | method | `readmenator/_video.py:800` | `def emergence_frames(self, data, box)` |
| `fmt_int` | function | `readmenator/_video.py:94` | `def fmt_int(n)` |
| `glitch_fx` | method | `readmenator/_video.py:387` | `def glitch_fx(img, amount, seed)` |
| `graph_positions` | method | `readmenator/_video.py:710` | `def graph_positions(self, data, box)` |
| `hash_color` | function | `readmenator/_video.py:109` | `def hash_color(digest)` |
| `hud_panel` | method | `readmenator/_video.py:421` | `def hud_panel(d, box, title, fonts, col)` |
| `mix` | function | `readmenator/_video.py:99` | `def mix(a, b, t)` |
| `post` | method | `readmenator/_video.py:369` | `def post(img, glitch, seed)` |
| `render` | method | `readmenator/_video.py:853` | `def render(self, data, output_path)` |
| `render_single_frame` | method | `readmenator/_video.py:839` | `def render_single_frame(self, data, frame_index)` |
| `resolve_fonts` | function | `readmenator/_video.py:230` | `def resolve_fonts()` |
| `short_label` | function | `readmenator/_video.py:118` | `def short_label(text, limit)` |
| `tree_positions` | method | `readmenator/_video.py:757` | `def tree_positions(self, data, box)` |
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
| `_safe_env` | method | `readmenator_orchestrator.py:68` | `def _safe_env()` |
| `_setup_git_auth` | method | `readmenator_orchestrator.py:110` | `def _setup_git_auth(self)` |
| `_validate_branch_name` | method | `readmenator_orchestrator.py:62` | `def _validate_branch_name(name)` |
| `_validate_repo_name` | method | `readmenator_orchestrator.py:56` | `def _validate_repo_name(name)` |
| `close_existing_prs` | method | `readmenator_orchestrator.py:136` | `def close_existing_prs(self, repo)` |
| `create_pr` | method | `readmenator_orchestrator.py:176` | `def create_pr(self, repo, default_branch, timestamp)` |
| `delete_remote_branch` | method | `readmenator_orchestrator.py:164` | `def delete_remote_branch(self, repo)` |
| `list_repos` | method | `readmenator_orchestrator.py:124` | `def list_repos(self)` |
| `main` | method | `readmenator_orchestrator.py:498` | `def main()` |
| `parse_arguments` | method | `readmenator_orchestrator.py:481` | `def parse_arguments()` |
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
| `test_sizeof_is_not_a_read` | method | `tests/test_dataflow.py:216` | `def test_sizeof_is_not_a_read(self)` |
| `test_static_never_uninit` | method | `tests/test_dataflow.py:196` | `def test_static_never_uninit(self)` |
| `test_subscript_store_counts_as_init` | method | `tests/test_dataflow.py:110` | `def test_subscript_store_counts_as_init(self)` |
| `test_unchecked_alloc_detected` | method | `tests/test_dataflow.py:71` | `def test_unchecked_alloc_detected(self)` |
| `test_uninit_use_detected` | method | `tests/test_dataflow.py:37` | `def test_uninit_use_detected(self)` |
| `test_url_string_does_not_truncate_line` | method | `tests/test_dataflow.py:344` | `def test_url_string_does_not_truncate_line(self)` |
| `TestDeadCodeStripperContract` | class | `tests/test_dead_code.py:16` | `class TestDeadCodeStripperContract(TestCase)` |
| `_make_edge` | method | `tests/test_dead_code.py:35` | `def _make_edge(self, src, tgt)` |
| `_make_node` | method | `tests/test_dead_code.py:26` | `def _make_node(self, nid, symbols)` |
| `_make_symbol` | method | `tests/test_dead_code.py:23` | `def _make_symbol(self, name, kind)` |
| `setUp` | method | `tests/test_dead_code.py:19` | `def setUp(self)` |
| `test_all_symbols_imported_returns_empty` | method | `tests/test_dead_code.py:101` | `def test_all_symbols_imported_returns_empty(self)` |
| `test_identify_empty_graph_returns_empty` | method | `tests/test_dead_code.py:38` | `def test_identify_empty_graph_returns_empty(self)` |
| `test_identify_excludes_app_entry_point` | method | `tests/test_dead_code.py:61` | `def test_identify_excludes_app_entry_point(self)` |
| `test_identify_excludes_entry_points` | method | `tests/test_dead_code.py:53` | `def test_identify_excludes_entry_points(self)` |
| `test_identify_excludes_init_entry_point` | method | `tests/test_dead_code.py:69` | `def test_identify_excludes_init_entry_point(self)` |
| `test_identify_finds_dead_symbol` | method | `tests/test_dead_code.py:42` | `def test_identify_finds_dead_symbol(self)` |
| `test_identify_recommends_review_for_classes` | method | `tests/test_dead_code.py:77` | `def test_identify_recommends_review_for_classes(self)` |
| `test_identify_recommends_trash_for_functions` | method | `tests/test_dead_code.py:85` | `def test_identify_recommends_trash_for_functions(self)` |
| `test_identify_recommends_trash_for_variables` | method | `tests/test_dead_code.py:93` | `def test_identify_recommends_trash_for_variables(self)` |
| `test_reports_sorted_by_file_path` | method | `tests/test_dead_code.py:113` | `def test_reports_sorted_by_file_path(self)` |
| `TestDiagramVariantsContract` | class | `tests/test_diagrams.py:627` | `class TestDiagramVariantsContract(TestCase)` |
| `TestDocsSitePublisherContract` | class | `tests/test_diagrams.py:367` | `class TestDocsSitePublisherContract(TestCase)` |
| `TestInteractiveMapRendererContract` | class | `tests/test_diagrams.py:237` | `class TestInteractiveMapRendererContract(TestCase)` |
| `TestSystemMapBuilderContract` | class | `tests/test_diagrams.py:30` | `class TestSystemMapBuilderContract(TestCase)` |
| `TestSystemMapValidatorContract` | class | `tests/test_diagrams.py:176` | `class TestSystemMapValidatorContract(TestCase)` |
| `TestVisNetworkRendererContract` | class | `tests/test_diagrams.py:510` | `class TestVisNetworkRendererContract(TestCase)` |
| `_make_graph` | method | `tests/test_diagrams.py:38` | `def _make_graph(self)` |
| `_map` | method | `tests/test_diagrams.py:246` | `def _map(self, kind)` |
| `_map` | method | `tests/test_diagrams.py:519` | `def _map(self, kind)` |
| `_maps` | method | `tests/test_diagrams.py:376` | `def _maps(self)` |
| `_project` | method | `tests/test_diagrams.py:630` | `def _project(self, tmp)` |
| `_valid_map` | method | `tests/test_diagrams.py:184` | `def _valid_map(self)` |
| `setUp` | method | `tests/test_diagrams.py:33` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:179` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:240` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:370` | `def setUp(self)` |
| `setUp` | method | `tests/test_diagrams.py:513` | `def setUp(self)` |
| `test_builder_attaches_symbols_and_docs` | method | `tests/test_diagrams.py:126` | `def test_builder_attaches_symbols_and_docs(self)` |
| `test_builder_is_deterministic` | method | `tests/test_diagrams.py:68` | `def test_builder_is_deterministic(self)` |
| `test_builder_orders_links_deterministically` | method | `tests/test_diagrams.py:80` | `def test_builder_orders_links_deterministically(self)` |
| `test_builder_produces_all_kinds` | method | `tests/test_diagrams.py:59` | `def test_builder_produces_all_kinds(self)` |
| `test_builder_reports_total_scope` | method | `tests/test_diagrams.py:119` | `def test_builder_reports_total_scope(self)` |
| `test_builder_supports_five_kinds` | method | `tests/test_diagrams.py:52` | `def test_builder_supports_five_kinds(self)` |
| `test_builder_truncates_symbols_per_node` | method | `tests/test_diagrams.py:143` | `def test_builder_truncates_symbols_per_node(self)` |
| `test_builder_truncates_to_configured_limit` | method | `tests/test_diagrams.py:152` | `def test_builder_truncates_to_configured_limit(self)` |
| `test_builder_validates_large_graph_for_all_kinds` | method | `tests/test_diagrams.py:101` | `def test_builder_validates_large_graph_for_all_kinds(self)` |
| `test_compare_reports_added_removed_rerouted` | method | `tests/test_diagrams.py:162` | `def test_compare_reports_added_removed_rerouted(self)` |
| `test_export_diagrams_falls_back_offline_when_disabled` | method | `tests/test_diagrams.py:649` | `def test_export_diagrams_falls_back_offline_when_disabled(self)` |
| `test_export_diagrams_writes_vis_maps_by_default` | method | `tests/test_diagrams.py:635` | `def test_export_diagrams_writes_vis_maps_by_default(self)` |
| `test_publish_card_reports_primary_scope` | method | `tests/test_diagrams.py:501` | `def test_publish_card_reports_primary_scope(self)` |
| `test_publish_empty_maps_writes_empty_gallery` | method | `tests/test_diagrams.py:462` | `def test_publish_empty_maps_writes_empty_gallery(self)` |
| `test_publish_escapes_malicious_project_name` | method | `tests/test_diagrams.py:430` | `def test_publish_escapes_malicious_project_name(self)` |
| `test_publish_escapes_malicious_stat_keys` | method | `tests/test_diagrams.py:439` | `def test_publish_escapes_malicious_stat_keys(self)` |
| `test_publish_flat_subdir_keeps_links_relative` | method | `tests/test_diagrams.py:480` | `def test_publish_flat_subdir_keeps_links_relative(self)` |
| `test_publish_index_explains_how_to_read` | method | `tests/test_diagrams.py:493` | `def test_publish_index_explains_how_to_read(self)` |
| `test_publish_index_links_every_map` | method | `tests/test_diagrams.py:397` | `def test_publish_index_links_every_map(self)` |
| `test_publish_is_deterministic` | method | `tests/test_diagrams.py:419` | `def test_publish_is_deterministic(self)` |
| `test_publish_leaves_input_maps_unmodified` | method | `tests/test_diagrams.py:471` | `def test_publish_leaves_input_maps_unmodified(self)` |
| `test_publish_output_has_no_external_requests` | method | `tests/test_diagrams.py:406` | `def test_publish_output_has_no_external_requests(self)` |
| `test_publish_skips_invalid_maps` | method | `tests/test_diagrams.py:450` | `def test_publish_skips_invalid_maps(self)` |
| `test_publish_writes_index_plus_five_maps` | method | `tests/test_diagrams.py:386` | `def test_publish_writes_index_plus_five_maps(self)` |
| `test_renderer_builds_vis_network_with_physics` | method | `tests/test_diagrams.py:542` | `def test_renderer_builds_vis_network_with_physics(self)` |
| `test_renderer_buttons_explain_their_purpose` | method | `tests/test_diagrams.py:355` | `def test_renderer_buttons_explain_their_purpose(self)` |
| `test_renderer_covers_all_five_kinds` | method | `tests/test_diagrams.py:314` | `def test_renderer_covers_all_five_kinds(self)` |
| `test_renderer_disables_physics_from_config` | method | `tests/test_diagrams.py:558` | `def test_renderer_disables_physics_from_config(self)` |
| `test_renderer_documents_symbols_per_file` | method | `tests/test_diagrams.py:597` | `def test_renderer_documents_symbols_per_file(self)` |
| `test_renderer_embeds_valid_json_payloads` | method | `tests/test_diagrams.py:305` | `def test_renderer_embeds_valid_json_payloads(self)` |
| `test_renderer_embeds_valid_payloads` | method | `tests/test_diagrams.py:589` | `def test_renderer_embeds_valid_payloads(self)` |
| `test_renderer_escapes_malicious_labels` | method | `tests/test_diagrams.py:292` | `def test_renderer_escapes_malicious_labels(self)` |
| `test_renderer_escapes_malicious_symbol_docs` | method | `tests/test_diagrams.py:613` | `def test_renderer_escapes_malicious_symbol_docs(self)` |
| `test_renderer_escapes_malicious_titles` | method | `tests/test_diagrams.py:565` | `def test_renderer_escapes_malicious_titles(self)` |
| `test_renderer_exposes_reader_controls` | method | `tests/test_diagrams.py:578` | `def test_renderer_exposes_reader_controls(self)` |
| `test_renderer_has_no_external_requests` | method | `tests/test_diagrams.py:270` | `def test_renderer_has_no_external_requests(self)` |
| `test_renderer_includes_interaction_controls` | method | `tests/test_diagrams.py:277` | `def test_renderer_includes_interaction_controls(self)` |
| `test_renderer_includes_keyboard_and_deep_links` | method | `tests/test_diagrams.py:283` | `def test_renderer_includes_keyboard_and_deep_links(self)` |
| `test_renderer_is_deterministic` | method | `tests/test_diagrams.py:584` | `def test_renderer_is_deterministic(self)` |
| `test_renderer_keeps_canvas_distinct_from_nodes` | method | `tests/test_diagrams.py:333` | `def test_renderer_keeps_canvas_distinct_from_nodes(self)` |

Next: [SYMBOLS_p4.md](SYMBOLS_p4.md)
