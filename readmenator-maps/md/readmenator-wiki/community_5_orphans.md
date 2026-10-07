# orphans

*Community 5 | 2 files | cohesion 0.00*

## Definition

This community groups 2 file(s) rooted at `tests` with dominant language py (cohesion 0.00). Central symbols: `Config`, `GitHubClient`, `Orchestrator`, `RepositoryProcessor`, `TestOrchestrator`, `__init__`, `_cleanup_temp_dir`, `_clone_repository`. Core file: `readmenator_orchestrator.py` (34 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator_orchestrator.py` | py | utility | 34 | no |
| `tests/__init__.py` | py | testing | 0 | no |

## Key Symbols

- `Config` (class, `readmenator_orchestrator.py:21`) `class Config`
- `_validate_repo_name` (method, `readmenator_orchestrator.py:50`) `def _validate_repo_name(name)`
- `_validate_branch_name` (method, `readmenator_orchestrator.py:56`) `def _validate_branch_name(name)`
- `_safe_env` (method, `readmenator_orchestrator.py:62`) `def _safe_env()`
- `GitHubClient` (class, `readmenator_orchestrator.py:77`) `class GitHubClient`
- `__init__` (method, `readmenator_orchestrator.py:78`) `def __init__(self, config)`
- `_resolve_user` (method, `readmenator_orchestrator.py:83`) `def _resolve_user(self)`
- `_setup_git_auth` (method, `readmenator_orchestrator.py:104`) `def _setup_git_auth(self)`
- `list_repos` (method, `readmenator_orchestrator.py:118`) `def list_repos(self)`
- `close_existing_prs` (method, `readmenator_orchestrator.py:130`) `def close_existing_prs(self, repo)`
- `delete_remote_branch` (method, `readmenator_orchestrator.py:158`) `def delete_remote_branch(self, repo)`
- `create_pr` (method, `readmenator_orchestrator.py:170`) `def create_pr(self, repo, default_branch, timestamp)`
- `RepositoryProcessor` (class, `readmenator_orchestrator.py:191`) `class RepositoryProcessor`
- `__init__` (method, `readmenator_orchestrator.py:192`) `def __init__(self, config, github_client)`
- `process` (method, `readmenator_orchestrator.py:196`) `def process(self, repo)`
- `_get_default_branch` (method, `readmenator_orchestrator.py:225`) `def _get_default_branch(self, repo)`
- `_clone_repository` (method, `readmenator_orchestrator.py:241`) `def _clone_repository(self, repo)`
- `_run_readmenator` (method, `readmenator_orchestrator.py:257`) `def _run_readmenator(self, repo_dir)`
- `_copy_to_docs_dir` (method, `readmenator_orchestrator.py:277`) `def _copy_to_docs_dir(self, repo_dir, generated_file)`
- `_commit_and_push` (method, `readmenator_orchestrator.py:290`) `def _commit_and_push(self, repo_dir, repo)`
- `_cleanup_temp_dir` (method, `readmenator_orchestrator.py:336`) `def _cleanup_temp_dir(temp_dir)`
- `Orchestrator` (class, `readmenator_orchestrator.py:341`) `class Orchestrator`
- `__init__` (method, `readmenator_orchestrator.py:342`) `def __init__(self, config)`
- `run` (method, `readmenator_orchestrator.py:347`) `def run(self, dry_run, only_repo)`
- `TestOrchestrator` (class, `readmenator_orchestrator.py:396`) `class TestOrchestrator(TestCase)`
- `setUp` (method, `readmenator_orchestrator.py:397`) `def setUp(self)`
- `tearDown` (method, `readmenator_orchestrator.py:401`) `def tearDown(self)`
- `test_config_immutability` (method, `readmenator_orchestrator.py:404`) `def test_config_immutability(self)`
- `test_config_defaults` (method, `readmenator_orchestrator.py:408`) `def test_config_defaults(self)`
- `test_skip_repos_logic` (method, `readmenator_orchestrator.py:415`) `def test_skip_repos_logic(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (readmenator/parsers) and community 5 (orphans).
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (readmenator: _dataflow) and community 5 (orphans).
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (readmenator: _pipeline) and community 5 (orphans).
- [INFERRED] shares_context community 3 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 3 (readmenator: _diagrams) and community 5 (orphans).
- [INFERRED] shares_context community 4 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 4 (readmenator: _agent_output) and community 5 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `readmenator_orchestrator.py`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `readmenator_orchestrator.py`
- `tests/__init__.py`
