# API (page 3 of 3)
Previous: [API_p2.md](API_p2.md)

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

