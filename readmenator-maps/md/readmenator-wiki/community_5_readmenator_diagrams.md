# readmenator: _diagrams

*Community 5 | 15 files | cohesion 0.39*

## Definition

This community groups 15 file(s) rooted at `readmenator` with dominant language py (cohesion 0.39). Central symbols: `BundleGraphRenderer`, `BundleLayout`, `DocsSitePublisher`, `ForceAtlas2Settings`, `ForceGraphRenderer`, `InteractiveMapRenderer`, `MapDelta`, `MapDiagnostic`. Core file: `readmenator/_diagrams.py` (97 symbols). Documented purpose: Edge bundle explorer: circle and sphere hierarchical edge bundling pages.  Turns the force-graph payload (file nodes with community, layer, language, PageRank, .

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_bundlegraph.py` | py | utility | 8 | yes |
| `readmenator/_bundlegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_diagrams.py` | py | utility | 97 | yes |
| `readmenator/_forcegraph.py` | py | utility | 23 | yes |
| `readmenator/_forcegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_graphlayout.py` | py | utility | 26 | yes |
| `readmenator/_htmlpack.py` | py | utility | 5 | yes |
| `readmenator/_project_config.py` | py | infrastructure | 18 | yes |
| `readmenator/_sourceview.py` | py | utility | 8 | yes |
| `readmenator/_viewer_ui.py` | py | presentation | 7 | yes |
| `tests/test_bundlegraph.py` | py | testing | 27 | yes |
| `tests/test_graphlayout.py` | py | testing | 33 | yes |
| `tests/test_layout_quality.py` | py | testing | 16 | yes |
| `tests/test_project_config.py` | py | testing | 33 | yes |
| `tests/test_sourceview.py` | py | testing | 23 | yes |

## Key Symbols

- `_json_script` (function, `readmenator/_bundlegraph.py:39`) `def _json_script(value)` - Serialize a value for an inline script, escaping angle brackets.
- `BundleGraphRenderer` (class, `readmenator/_bundlegraph.py:51`) `class BundleGraphRenderer` - Builds the bundle payload and renders the edge bundle explorer page.
- `__init__` (method, `readmenator/_bundlegraph.py:54`) `def __init__(self, config)` - Initialise with application configuration.
- `build_payload` (method, `readmenator/_bundlegraph.py:63`) `def build_payload(self, force_payload)` - Derive the bundle payload from a force-graph payload.
- `page_settings` (method, `readmenator/_bundlegraph.py:184`) `def page_settings(self, force_payload, explorer_href, live_api)` - Collect the page settings serialized into the HTML.
- `render` (method, `readmenator/_bundlegraph.py:228`) `def render(self, force_payload, title, home_href, explorer_href, live_api)` - Render the standalone edge bundle explorer HTML document.
- `write` (method, `readmenator/_bundlegraph.py:273`) `def write(self, output_path, force_payload, title, home_href, explorer_href)` - Write the edge bundle explorer HTML document.
- `thumbnail_svg` (method, `readmenator/_bundlegraph.py:299`) `def thumbnail_svg(self, force_payload)` - Render a small circular bundle preview as inline SVG.
- `_escape_markup` (function, `readmenator/_diagrams.py:33`) `def _escape_markup(value)` - Escape text for HTML and tooltip embedding.
- `_json_payload` (function, `readmenator/_diagrams.py:45`) `def _json_payload(payload)` - Serialize a payload for safe inline script embedding.
- `_fill_template` (function, `readmenator/_diagrams.py:57`) `def _fill_template(template, values)` - Substitute __KEY__ placeholders in a single pass.
- `_role_color` (function, `readmenator/_diagrams.py:76`) `def _role_color(role, config)` - Return the stroke color for a semantic role.
- `MapNode` (class, `readmenator/_diagrams.py:90`) `class MapNode` - Single authored node in a system map.
- `MapEdge` (class, `readmenator/_diagrams.py:123`) `class MapEdge` - Single authored directed relationship in a system map.
- `MapView` (class, `readmenator/_diagrams.py:140`) `class MapView` - Single guided chapter over authored topology.
- `SystemMap` (class, `readmenator/_diagrams.py:157`) `class SystemMap` - Typed intermediate representation of one diagram.
- `MapDiagnostic` (class, `readmenator/_diagrams.py:178`) `class MapDiagnostic` - Single machine-readable validation diagnostic.
- `MapReceipt` (class, `readmenator/_diagrams.py:195`) `class MapReceipt` - Deterministic validation receipt for a system map.
- `MapDelta` (class, `readmenator/_diagrams.py:212`) `class MapDelta` - Before and after comparison between two maps of the same kind.
- `SystemMapValidator` (class, `readmenator/_diagrams.py:232`) `class SystemMapValidator` - Deterministic validator for system map intermediate representations.
- `__init__` (method, `readmenator/_diagrams.py:235`) `def __init__(self, config)` - Initialise the validator with application configuration.
- `_effective_canvas` (method, `readmenator/_diagrams.py:243`) `def _effective_canvas(self, system_map)` - Return the canvas bounds applying per-map full-mode growth.
- `validate` (method, `readmenator/_diagrams.py:264`) `def validate(self, system_map)` - Validate a system map and return a deterministic receipt.
- `SystemMapBuilder` (class, `readmenator/_diagrams.py:456`) `class SystemMapBuilder` - Builds deterministic system maps from the scanned knowledge graph.
- `__init__` (method, `readmenator/_diagrams.py:485`) `def __init__(self, config)` - Initialise the builder with application configuration.
- `supported_kinds` (method, `readmenator/_diagrams.py:494`) `def supported_kinds(self)` - Return the supported diagram kind identifiers.
- `_is_full` (method, `readmenator/_diagrams.py:502`) `def _is_full(self, full)` - Return whether full-map scope applies for this build.
- `build` (method, `readmenator/_diagrams.py:515`) `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind,` - Build one deterministic system map of the requested kind.
- `_annotate_communities` (method, `readmenator/_diagrams.py:557`) `def _annotate_communities(system_map, analysis)` - Tag map nodes with their code community so renderers can color clusters.
- `build_all` (method, `readmenator/_diagrams.py:574`) `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, fu` - Build all five diagram kinds deterministically.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 45
- Cross-boundary resolved imports (EXTRACTED): 64

## Connections

- [EXTRACTED] depends_on community 3 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_project_config.py.
- [EXTRACTED] depends_on community 0 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__main__.py imports readmenator/_project_config.py.
- [EXTRACTED] depends_on community 6 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs_page.py imports readmenator/_htmlpack.py.
- [EXTRACTED] depends_on community 5 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/_diagrams.py imports readmenator/_folder_readme.py.
- [EXTRACTED] depends_on community 5 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_diagrams.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_forcegraph.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_diagrams.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_htmlpack.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_project_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_folder_readme.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_viewer_ui.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [layer strict] `tests/test_layout_quality.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_viewer_ui.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_viewer_ui.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_viewer_ui.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation)
- [layer strict] `tests/test_project_config.py` (testing) -> `readmenator/_bundlegraph_page.py` (presentation)

## Open Questions

- Is the dangerous import `subprocess` in `readmenator/_diagrams.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _diagrams changed?
- Should readmenator: _diagrams be split, given cohesion 0.39?

## Sources

- `readmenator/_bundlegraph.py`
- `readmenator/_bundlegraph_page.py`
- `readmenator/_diagrams.py`
- `readmenator/_forcegraph.py`
- `readmenator/_forcegraph_page.py`
- `readmenator/_graphlayout.py`
- `readmenator/_htmlpack.py`
- `readmenator/_project_config.py`
- `readmenator/_sourceview.py`
- `readmenator/_viewer_ui.py`
- `tests/test_bundlegraph.py`
- `tests/test_graphlayout.py`
- `tests/test_layout_quality.py`
- `tests/test_project_config.py`
- `tests/test_sourceview.py`
