# readmenator

*Community 1 | 3 files | cohesion 0.40*

## Definition

This community groups 3 file(s) rooted at `readmenator` with dominant language py (cohesion 0.40). Central symbols: `AgentInjector`, `TestAgentInjectorEdgeCases`, `TestAgentInjectorFindFiles`, `TestAgentInjectorInjectBehavior`, `TestAgentInjectorRemoveBehavior`, `__init__`, `_build_injection`, `_build_mdc_injection`. Core file: `tests/test_agent_injector.py` (38 symbols). Documented purpose: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects common AI agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules, etc.) an.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | no |
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `tests/test_agent_injector.py` | py | testing | 38 | yes |

## Key Symbols

- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:111`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:136`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:147`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:161`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:179`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:192`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:196`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:210`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:248`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:257`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:267`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:283`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:295`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:300`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
- `TestAgentInjectorInjectBehavior` (class, `tests/test_agent_injector.py:19`) `class TestAgentInjectorInjectBehavior(TestCase)` - BDD: AgentInjector injection contract.
- `setUp` (method, `tests/test_agent_injector.py:22`) `def setUp(self)`
- `tearDown` (method, `tests/test_agent_injector.py:27`) `def tearDown(self)`
- `test_inject_into_agents_md_adds_kb_link` (method, `tests/test_agent_injector.py:30`) `def test_inject_into_agents_md_adds_kb_link(self)`
- `test_inject_into_claude_md_adds_kb_link` (method, `tests/test_agent_injector.py:39`) `def test_inject_into_claude_md_adds_kb_link(self)`
- `test_inject_into_cursorrules_adds_kb_link` (method, `tests/test_agent_injector.py:49`) `def test_inject_into_cursorrules_adds_kb_link(self)`
- `test_inject_into_github_copilot_instructions` (method, `tests/test_agent_injector.py:57`) `def test_inject_into_github_copilot_instructions(self)`
- `test_inject_replaces_old_injection_without_regen_command` (method, `tests/test_agent_injector.py:67`) `def test_inject_replaces_old_injection_without_regen_command(self)`
- `test_inject_skips_when_already_up_to_date` (method, `tests/test_agent_injector.py:82`) `def test_inject_skips_when_already_up_to_date(self)`
- `test_inject_into_cursor_rules_mdc_glob` (method, `tests/test_agent_injector.py:96`) `def test_inject_into_cursor_rules_mdc_glob(self)`
- `test_inject_is_idempotent_does_not_duplicate` (method, `tests/test_agent_injector.py:106`) `def test_inject_is_idempotent_does_not_duplicate(self)`
- `test_inject_no_agent_files_returns_zero` (method, `tests/test_agent_injector.py:117`) `def test_inject_no_agent_files_returns_zero(self)`
- `test_inject_preserves_existing_content` (method, `tests/test_agent_injector.py:121`) `def test_inject_preserves_existing_content(self)`
- `test_inject_multiple_agent_files` (method, `tests/test_agent_injector.py:129`) `def test_inject_multiple_agent_files(self)`
- `test_inject_plain_text_format_for_yaml` (method, `tests/test_agent_injector.py:136`) `def test_inject_plain_text_format_for_yaml(self)`
- `test_custom_kb_filename_works` (method, `tests/test_agent_injector.py:145`) `def test_custom_kb_filename_works(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 3
- Cross-boundary resolved imports (EXTRACTED): 4

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/__init__.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_agent_injector.py reaches tests/test_resolver.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/_cache.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/_cursorrules_generator.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] shares_context community 1 <-> 2 (strength 0.5): Inferred shared context (layer utility) with no import path between community 1 (readmenator) and community 2 (orphans).

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/__main__.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_app.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_config.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_mcp_server.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_cursorrules_generator.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_models.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_layers.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_diagrams.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_pipeline.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_query.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_resolver.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_rank.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_watcher.py` via `subprocess` (4 hops)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `readmenator.py`)? What purpose do they serve?
- Can the cycle `readmenator/_app.py` -> `readmenator/_pipeline.py` -> `readmenator/_agent_injector.py` -> `readmenator.py` -> `readmenator/__main__.py` -> `readmenator/_mcp_server.py` be broken with an interface?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator changed?
- Should readmenator be split, given cohesion 0.40?

## Sources

- `readmenator.py`
- `readmenator/_agent_injector.py`
- `tests/test_agent_injector.py`
