# Subsystem: root

## readmenator.py
- Doc: Launcher shim that runs the readmenator CLI from a source checkout.
- Layer: utility
- Language: py
- Depends on: `readmenator/__main__.py`

## readmenator_orchestrator.py
- Layer: utility
- Language: py
- Symbols:
  - `Config` (class, line 21) `class Config`
  - `_validate_repo_name` (method, line 50) `def _validate_repo_name(name)`
  - `_validate_branch_name` (method, line 56) `def _validate_branch_name(name)`
  - `_safe_env` (method, line 62) `def _safe_env()`
  - `GitHubClient` (class, line 77) `class GitHubClient`
  - `RepositoryProcessor` (class, line 191) `class RepositoryProcessor`
  - `Orchestrator` (class, line 341) `class Orchestrator`
  - `TestOrchestrator` (class, line 396) `class TestOrchestrator(TestCase)`
  - `parse_arguments` (method, line 438) `def parse_arguments()`
  - `main` (method, line 455) `def main()`
  - `__init__` (method, line 78) `def __init__(self, config)`
  - `_resolve_user` (method, line 83) `def _resolve_user(self)`
  - `_setup_git_auth` (method, line 104) `def _setup_git_auth(self)`
  - `list_repos` (method, line 118) `def list_repos(self)`
  - `close_existing_prs` (method, line 130) `def close_existing_prs(self, repo)`
  - `delete_remote_branch` (method, line 158) `def delete_remote_branch(self, repo)`
  - `create_pr` (method, line 170) `def create_pr(self, repo, default_branch, timestamp)`
  - `__init__` (method, line 192) `def __init__(self, config, github_client)`
  - `process` (method, line 196) `def process(self, repo)`
  - `_get_default_branch` (method, line 225) `def _get_default_branch(self, repo)`
  - `_clone_repository` (method, line 241) `def _clone_repository(self, repo)`
  - `_run_readmenator` (method, line 257) `def _run_readmenator(self, repo_dir)`
  - `_copy_to_docs_dir` (method, line 277) `def _copy_to_docs_dir(self, repo_dir, generated_file)`
  - `_commit_and_push` (method, line 290) `def _commit_and_push(self, repo_dir, repo)`
  - `_cleanup_temp_dir` (method, line 336) `def _cleanup_temp_dir(temp_dir)`
  - `__init__` (method, line 342) `def __init__(self, config)`
  - `run` (method, line 347) `def run(self, dry_run, only_repo)`
  - `setUp` (method, line 397) `def setUp(self)`
  - `tearDown` (method, line 401) `def tearDown(self)`
  - `test_config_immutability` (method, line 404) `def test_config_immutability(self)`
  - `test_config_defaults` (method, line 408) `def test_config_defaults(self)`
  - `test_skip_repos_logic` (method, line 415) `def test_skip_repos_logic(self)`
  - `test_repo_name_validation` (method, line 419) `def test_repo_name_validation(self)`
  - `test_branch_name_validation` (method, line 429) `def test_branch_name_validation(self)`
