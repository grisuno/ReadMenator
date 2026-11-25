# readmenator: _diagrams

*Community 3 | 20 files | cohesion 0.41*

## Definition

This community groups 20 file(s) rooted at `readmenator` with dominant language py (cohesion 0.41). Central symbols: `AgentInjector`, `BundleGraphRenderer`, `BundleLayout`, `DocsSitePublisher`, `ForceAtlas2Settings`, `ForceGraphRenderer`, `InteractiveMapRenderer`, `MapDelta`. Core file: `readmenator/_diagrams.py` (97 symbols). Documented purpose: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects common AI agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules, etc.) an.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `readmenator/_bundlegraph.py` | py | utility | 8 | yes |
| `readmenator/_bundlegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_diagrams.py` | py | utility | 97 | yes |
| `readmenator/_forcegraph.py` | py | utility | 23 | yes |
| `readmenator/_forcegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_graphlayout.py` | py | utility | 26 | yes |
| `readmenator/_htmlpack.py` | py | utility | 5 | yes |
| `readmenator/_project_config.py` | py | infrastructure | 18 | yes |
| `readmenator/_readme_injector.py` | py | infrastructure | 9 | yes |
| `readmenator/_sourceview.py` | py | utility | 8 | yes |
| `readmenator/_viewer_ui.py` | py | presentation | 7 | yes |
| `tests/test_agent_injector.py` | py | testing | 38 | yes |
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_bundlegraph.py` | py | testing | 30 | yes |
| `tests/test_graphlayout.py` | py | testing | 33 | yes |
| `tests/test_layout_quality.py` | py | testing | 16 | yes |
| `tests/test_project_config.py` | py | testing | 33 | yes |
| `tests/test_readme_injector.py` | py | testing | 29 | yes |
| `tests/test_sourceview.py` | py | testing | 23 | yes |

## Key Symbols

- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:120`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:142`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:153`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:173`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:191`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:204`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:208`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:222`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:260`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:269`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:279`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:295`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:318`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:323`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
- `_json_script` (function, `readmenator/_bundlegraph.py:39`) `def _json_script(value)` - Serialize a value for an inline script, escaping angle brackets.
- `BundleGraphRenderer` (class, `readmenator/_bundlegraph.py:51`) `class BundleGraphRenderer` - Builds the bundle payload and renders the edge bundle explorer page.
- `__init__` (method, `readmenator/_bundlegraph.py:54`) `def __init__(self, config)` - Initialise with application configuration.
- `build_payload` (method, `readmenator/_bundlegraph.py:63`) `def build_payload(self, force_payload)` - Derive the bundle payload from a force-graph payload.
- `page_settings` (method, `readmenator/_bundlegraph.py:184`) `def page_settings(self, force_payload, explorer_href, live_api)` - Collect the page settings serialized into the HTML.
- `render` (method, `readmenator/_bundlegraph.py:236`) `def render(self, force_payload, title, home_href, explorer_href, live_api)` - Render the standalone edge bundle explorer HTML document.
- `write` (method, `readmenator/_bundlegraph.py:281`) `def write(self, output_path, force_payload, title, home_href, explorer_href)` - Write the edge bundle explorer HTML document.
- `thumbnail_svg` (method, `readmenator/_bundlegraph.py:307`) `def thumbnail_svg(self, force_payload)` - Render a small circular bundle preview as inline SVG.
- `_escape_markup` (function, `readmenator/_diagrams.py:33`) `def _escape_markup(value)` - Escape text for HTML and tooltip embedding.
- `_json_payload` (function, `readmenator/_diagrams.py:45`) `def _json_payload(payload)` - Serialize a payload for safe inline script embedding.
- `_fill_template` (function, `readmenator/_diagrams.py:57`) `def _fill_template(template, values)` - Substitute __KEY__ placeholders in a single pass.
- `_role_color` (function, `readmenator/_diagrams.py:76`) `def _role_color(role, config)` - Return the stroke color for a semantic role.
- `MapNode` (class, `readmenator/_diagrams.py:90`) `class MapNode` - Single authored node in a system map.
- `MapEdge` (class, `readmenator/_diagrams.py:123`) `class MapEdge` - Single authored directed relationship in a system map.
- `MapView` (class, `readmenator/_diagrams.py:140`) `class MapView` - Single guided chapter over authored topology.
- `SystemMap` (class, `readmenator/_diagrams.py:157`) `class SystemMap` - Typed intermediate representation of one diagram.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 54
- Cross-boundary resolved imports (EXTRACTED): 70

## Connections

- [EXTRACTED] depends_on community 4 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_project_config.py.
- [EXTRACTED] depends_on community 5 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs_page.py imports readmenator/_htmlpack.py.
- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_bundlegraph.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/_diagrams.py imports readmenator/_folder_readme.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_diagrams.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_forcegraph.py imports readmenator/_resolver.py.

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_diagrams.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_project_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_htmlpack.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_folder_readme.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_viewer_ui.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [layer strict] `tests/test_layout_quality.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_viewer_ui.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_viewer_ui.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_viewer_ui.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `tests/test_agent_output.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _diagrams changed?
- Should readmenator: _diagrams be split, given cohesion 0.41?

## Sources

- `readmenator/_agent_injector.py`
- `readmenator/_bundlegraph.py`
- `readmenator/_bundlegraph_page.py`
- `readmenator/_diagrams.py`
- `readmenator/_forcegraph.py`
- `readmenator/_forcegraph_page.py`
- `readmenator/_graphlayout.py`
- `readmenator/_htmlpack.py`
- `readmenator/_project_config.py`
- `readmenator/_readme_injector.py`
- `readmenator/_sourceview.py`
- `readmenator/_viewer_ui.py`
- `tests/test_agent_injector.py`
- `tests/test_agent_output.py`
- `tests/test_bundlegraph.py`
- `tests/test_graphlayout.py`
- `tests/test_layout_quality.py`
- `tests/test_project_config.py`
- `tests/test_readme_injector.py`
- `tests/test_sourceview.py`
