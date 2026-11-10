# API (page 3 of 3)
Previous: [API_p2.md](API_p2.md)

## readmenator/_yaralite.py
Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`
- `YaraLiteRule.tier` (method) `readmenator/_yaralite.py:42` `def tier(self)` -- Return the rule tier from meta or name prefix.
- `parse_yaralite_rules` (function) `readmenator/_yaralite.py:76` `def parse_yaralite_rules(rules_text)` -- Parse YARA-lite rules text into rules and error messages.
- `run_yaralite_rules` (function) `readmenator/_yaralite.py:112` `def run_yaralite_rules(text, rules)` -- Run parsed rules against a scan-text blob.
- `validate_yaralite_rules` (function) `readmenator/_yaralite.py:139` `def validate_yaralite_rules(rules_text)` -- Validate rules text and summarize tier counts.
- `replace_group` (function) `readmenator/_yaralite.py:270` `def replace_group(match)` -- Replace an N-of group with its boolean outcome.
- `replace_identifier` (function) `readmenator/_yaralite.py:292` `def replace_identifier(match)` -- Replace a string identifier with its hit boolean.

## readmenator/parsers/__init__.py
Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`
- `create_parser` (function) `readmenator/parsers/__init__.py:70` `def create_parser(extension, filename, config)` -- Factory: return a parser instance for the given file extension.

## readmenator/parsers/_base.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- `LanguageParser.__init__` (method) `readmenator/parsers/_base.py:21` `def __init__(self, filename, config)` -- Initialise the parser with a file path and application config.
- `LanguageParser.parse` (method) `readmenator/parsers/_base.py:36` `def parse(self, content)` -- Parse *content* and populate symbol/import lists.

## readmenator_orchestrator.py
- `GitHubClient.__init__` (method) `readmenator_orchestrator.py:84` `def __init__(self, config)`
- `GitHubClient.list_repos` (method) `readmenator_orchestrator.py:124` `def list_repos(self)`
- `GitHubClient.close_existing_prs` (method) `readmenator_orchestrator.py:136` `def close_existing_prs(self, repo)`
- `GitHubClient.delete_remote_branch` (method) `readmenator_orchestrator.py:164` `def delete_remote_branch(self, repo)`
- `GitHubClient.create_pr` (method) `readmenator_orchestrator.py:176` `def create_pr(self, repo, default_branch, timestamp)`
- `RepositoryProcessor.__init__` (method) `readmenator_orchestrator.py:198` `def __init__(self, config, github_client)`
- `RepositoryProcessor.process` (method) `readmenator_orchestrator.py:202` `def process(self, repo)`
- `Orchestrator.__init__` (method) `readmenator_orchestrator.py:367` `def __init__(self, config)`
- `Orchestrator.run` (method) `readmenator_orchestrator.py:372` `def run(self, dry_run, only_repo)`
- `TestOrchestrator.setUp` (method) `readmenator_orchestrator.py:422` `def setUp(self)`
- `TestOrchestrator.tearDown` (method) `readmenator_orchestrator.py:426` `def tearDown(self)`
- `TestOrchestrator.test_config_immutability` (method) `readmenator_orchestrator.py:429` `def test_config_immutability(self)`
- `TestOrchestrator.test_config_defaults` (method) `readmenator_orchestrator.py:433` `def test_config_defaults(self)`
- `TestOrchestrator.test_rebuild_command_includes_full_concept_layer` (method) `readmenator_orchestrator.py:441` `def test_rebuild_command_includes_full_concept_layer(self)` -- The orchestrator must force a full rebuild with all improvements.
- `TestOrchestrator.test_pr_body_mentions_concept_layer` (method) `readmenator_orchestrator.py:452` `def test_pr_body_mentions_concept_layer(self)`
- `TestOrchestrator.test_skip_repos_logic` (method) `readmenator_orchestrator.py:458` `def test_skip_repos_logic(self)`
- `TestOrchestrator.test_repo_name_validation` (method) `readmenator_orchestrator.py:462` `def test_repo_name_validation(self)`
- `TestOrchestrator.test_branch_name_validation` (method) `readmenator_orchestrator.py:472` `def test_branch_name_validation(self)`
- `parse_arguments` (function) `readmenator_orchestrator.py:481` `def parse_arguments()`
- `main` (function) `readmenator_orchestrator.py:498` `def main()`

