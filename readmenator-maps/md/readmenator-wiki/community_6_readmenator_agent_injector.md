# readmenator: _agent_injector

*Community 6 | 5 files | cohesion 0.40*

## Definition

This community groups 5 file(s) rooted at `tests` with dominant language py (cohesion 0.40). Central symbols: `AgentInjector`, `ReadmeInjector`, `TestAgentInjectorEdgeCases`, `TestAgentInjectorFindFiles`, `TestAgentInjectorInjectBehavior`, `TestAgentInjectorRemoveBehavior`, `TestAgentOutputContract`, `TestApiGeneration`. Core file: `tests/test_agent_output.py` (45 symbols). Documented purpose: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects common AI agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules, etc.) an.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `readmenator/_readme_injector.py` | py | infrastructure | 9 | yes |
| `tests/test_agent_injector.py` | py | testing | 38 | yes |
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_readme_injector.py` | py | testing | 28 | yes |

## Key Symbols

- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:107`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:129`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:140`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:154`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:172`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:185`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:189`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:203`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:241`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:250`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:260`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:276`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:288`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:293`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
- `ReadmeInjector` (class, `readmenator/_readme_injector.py:122`) `class ReadmeInjector` - Injects a link to KNOWLEDGE_BASE.md into the project README.
- `__init__` (method, `readmenator/_readme_injector.py:133`) `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir, graphrag_outp` - Initialise the injector with output locations.
- `inject` (method, `readmenator/_readme_injector.py:192`) `def inject(self, project_root)` - Inject or refresh the knowledge base section in the README.
- `_extract_current_injection` (method, `readmenator/_readme_injector.py:233`) `def _extract_current_injection(content)` - Return the current anchored injection block.
- `_remove_old_injection` (method, `readmenator/_readme_injector.py:250`) `def _remove_old_injection(content)` - Remove a complete anchored injection block.
- `_strip_partial_anchor` (method, `readmenator/_readme_injector.py:269`) `def _strip_partial_anchor(content)` - Remove a broken half-anchor so a fresh tag can be created.
- `remove` (method, `readmenator/_readme_injector.py:284`) `def remove(self, project_root)` - Remove the injected section from the README.
- `_find_readme` (method, `readmenator/_readme_injector.py:321`) `def _find_readme(root)` - Return the first README candidate present in the directory.
- `_build_injection` (method, `readmenator/_readme_injector.py:336`) `def _build_injection(self, suffix)` - Build the injection text for a README suffix.
- `TestAgentInjectorInjectBehavior` (class, `tests/test_agent_injector.py:19`) `class TestAgentInjectorInjectBehavior(TestCase)` - BDD: AgentInjector injection contract.
- `setUp` (method, `tests/test_agent_injector.py:22`) `def setUp(self)`
- `tearDown` (method, `tests/test_agent_injector.py:27`) `def tearDown(self)`
- `test_inject_into_agents_md_adds_kb_link` (method, `tests/test_agent_injector.py:30`) `def test_inject_into_agents_md_adds_kb_link(self)`
- `test_inject_into_claude_md_adds_kb_link` (method, `tests/test_agent_injector.py:39`) `def test_inject_into_claude_md_adds_kb_link(self)`
- `test_inject_into_cursorrules_adds_kb_link` (method, `tests/test_agent_injector.py:49`) `def test_inject_into_cursorrules_adds_kb_link(self)`
- `test_inject_into_github_copilot_instructions` (method, `tests/test_agent_injector.py:57`) `def test_inject_into_github_copilot_instructions(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 7
- Cross-boundary resolved imports (EXTRACTED): 9

## Connections

- [EXTRACTED] depends_on community 3 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_readme_injector.py.
- [EXTRACTED] depends_on community 0 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [EXTRACTED] depends_on community 6 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_output.py imports readmenator/_agent_output.py.
- [EXTRACTED] depends_on community 6 <-> 1 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_output.py imports readmenator/_models.py.
- [INFERRED] bridges community 2 <-> 6 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `tests/test_agent_output.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _agent_injector changed?
- Should readmenator: _agent_injector be split, given cohesion 0.40?

## Sources

- `readmenator/_agent_injector.py`
- `readmenator/_readme_injector.py`
- `tests/test_agent_injector.py`
- `tests/test_agent_output.py`
- `tests/test_readme_injector.py`
