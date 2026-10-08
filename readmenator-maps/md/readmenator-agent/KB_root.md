# Subsystem: root

## readmenator.py
- Doc: Launcher shim that runs the readmenator CLI from a source checkout.
- Layer: utility
- Language: py
- Depends on: `readmenator/__main__.py`

## readmenator_orchestrator.py
- Doc: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild...
- Layer: utility
- Language: py
- Symbols:
  - `Config` (class, line 21) `class Config`
  - `_validate_repo_name` (method, line 56) `def _validate_repo_name(name)`
  - `_validate_branch_name` (method, line 62) `def _validate_branch_name(name)`
  - `_safe_env` (method, line 68) `def _safe_env()`
  - `GitHubClient` (class, line 83) `class GitHubClient`
  - `RepositoryProcessor` (class, line 197) `class RepositoryProcessor`
  - `Orchestrator` (class, line 366) `class Orchestrator`
  - `TestOrchestrator` (class, line 421) `class TestOrchestrator(TestCase)`
  - `parse_arguments` (method, line 481) `def parse_arguments()`
  - `main` (method, line 498) `def main()`
  - `__init__` (method, line 84) `def __init__(self, config)`
  - `_resolve_user` (method, line 89) `def _resolve_user(self)`
  - `_setup_git_auth` (method, line 110) `def _setup_git_auth(self)`
  - `list_repos` (method, line 124) `def list_repos(self)`
  - `close_existing_prs` (method, line 136) `def close_existing_prs(self, repo)`
  - `delete_remote_branch` (method, line 164) `def delete_remote_branch(self, repo)`
  - `create_pr` (method, line 176) `def create_pr(self, repo, default_branch, timestamp)`
  - `__init__` (method, line 198) `def __init__(self, config, github_client)`
  - `process` (method, line 202) `def process(self, repo)`
  - `_get_default_branch` (method, line 231) `def _get_default_branch(self, repo)`
  - `_clone_repository` (method, line 247) `def _clone_repository(self, repo)`
  - `_run_readmenator` (method, line 263) `def _run_readmenator(self, repo_dir)`
  - `_build_readmenator_command` (method, line 283) `def _build_readmenator_command(self, repo_dir)`
  - `_copy_to_docs_dir` (method, line 293) `def _copy_to_docs_dir(self, repo_dir, generated_file)`
  - `_commit_and_push` (method, line 313) `def _commit_and_push(self, repo_dir, repo)`
  - `_cleanup_temp_dir` (method, line 361) `def _cleanup_temp_dir(temp_dir)`
  - `__init__` (method, line 367) `def __init__(self, config)`
  - `run` (method, line 372) `def run(self, dry_run, only_repo)`
  - `setUp` (method, line 422) `def setUp(self)`
  - `tearDown` (method, line 426) `def tearDown(self)`
  - `test_config_immutability` (method, line 429) `def test_config_immutability(self)`
  - `test_config_defaults` (method, line 433) `def test_config_defaults(self)`
  - `test_rebuild_command_includes_full_concept_layer` (method, line 441) `def test_rebuild_command_includes_full_concept_layer(self)`
  - `test_pr_body_mentions_concept_layer` (method, line 452) `def test_pr_body_mentions_concept_layer(self)`
  - `test_skip_repos_logic` (method, line 458) `def test_skip_repos_logic(self)`
  - `test_repo_name_validation` (method, line 462) `def test_repo_name_validation(self)`
  - `test_branch_name_validation` (method, line 472) `def test_branch_name_validation(self)`
