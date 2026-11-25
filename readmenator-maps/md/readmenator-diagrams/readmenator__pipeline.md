# readmenator: _pipeline

readmenator: _pipeline groups 25 files (py) around _read_small, _git_dir, _packed_ref, read_git_head, is_garbage_doc. Agent-friendly output generator for ReadMenator.

```mermaid
graph LR
    readmenator["readmenator"]
    tests["tests"]
    tests -- "calls into" --> readmenator
```

## readmenator (3.1)

readmenator groups 16 files (py) around _read_small, _git_dir, _packed_ref, read_git_head, is_garbage_doc. Agent-friendly output generator for ReadMenator.

## tests (3.2)

tests groups 9 files (py) around _node, _edge, _big_project, TestAgentOutputBudget, test_agent_output_pages_respect_line_cap_on_large_projects. Contract tests for agent-facing output quality: budgets, purposes, freshness, noise.

**Files**:

- readmenator/_agent_output.py
- readmenator/_analyzer.py
- readmenator/_cache.py
- readmenator/_components.py
- readmenator/_folder_readme.py
- readmenator/_gh_wiki.py
- readmenator/_gitmeta.py
- readmenator/_hebbian.py
- readmenator/_layers.py
- readmenator/_memory.py
- readmenator/_ollama.py
- readmenator/_pipeline.py
- readmenator/_purpose.py
- readmenator/_security.py
- readmenator/_skill_installer.py
- readmenator/_wiki.py
- tests/test_agent_friendliness.py
- tests/test_analyzer.py
- tests/test_cache.py
- tests/test_folder_readme.py
- tests/test_hebbian.py
- tests/test_memory.py
- tests/test_ollama.py
- tests/test_security.py
- tests/test_wiki.py
