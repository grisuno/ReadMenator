# readmenator: _graphlayout

*Community 4 | 13 files | cohesion 0.38*

## Definition

This community groups 13 file(s) rooted at `readmenator` with dominant language py (cohesion 0.38). Central symbols: `BundleGraphRenderer`, `BundleLayout`, `ExplorerState`, `ForceAtlas2Settings`, `ForceGraphRenderer`, `SourceEntry`, `SourceViewBuilder`, `SphereBundleLayout`. Core file: `tests/test_graphlayout.py` (33 symbols). Documented purpose: Edge bundle explorer: circle and sphere hierarchical edge bundling pages.  Turns the force-graph payload (file nodes with community, layer, language, PageRank, .

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_bundlegraph.py` | py | utility | 8 | yes |
| `readmenator/_bundlegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_explorer.py` | py | utility | 14 | yes |
| `readmenator/_forcegraph.py` | py | utility | 23 | yes |
| `readmenator/_forcegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_graphlayout.py` | py | utility | 26 | yes |
| `readmenator/_htmlpack.py` | py | utility | 5 | yes |
| `readmenator/_sourceview.py` | py | utility | 8 | yes |
| `tests/test_bundlegraph.py` | py | testing | 27 | yes |
| `tests/test_graphlayout.py` | py | testing | 33 | yes |
| `tests/test_htmlpack.py` | py | testing | 18 | yes |
| `tests/test_layout_quality.py` | py | testing | 16 | yes |
| `tests/test_sourceview.py` | py | testing | 23 | yes |

## Key Symbols

- `_json_script` (function, `readmenator/_bundlegraph.py:37`) `def _json_script(value)` - Serialize a value for an inline script, escaping angle brackets.
- `BundleGraphRenderer` (class, `readmenator/_bundlegraph.py:49`) `class BundleGraphRenderer` - Builds the bundle payload and renders the edge bundle explorer page.
- `__init__` (method, `readmenator/_bundlegraph.py:52`) `def __init__(self, config)` - Initialise with application configuration.
- `build_payload` (method, `readmenator/_bundlegraph.py:61`) `def build_payload(self, force_payload)` - Derive the bundle payload from a force-graph payload.
- `page_settings` (method, `readmenator/_bundlegraph.py:182`) `def page_settings(self, force_payload, explorer_href, live_api)` - Collect the page settings serialized into the HTML.
- `render` (method, `readmenator/_bundlegraph.py:226`) `def render(self, force_payload, title, home_href, explorer_href, live_api)` - Render the standalone edge bundle explorer HTML document.
- `write` (method, `readmenator/_bundlegraph.py:265`) `def write(self, output_path, force_payload, title, home_href, explorer_href)` - Write the edge bundle explorer HTML document.
- `thumbnail_svg` (method, `readmenator/_bundlegraph.py:291`) `def thumbnail_svg(self, force_payload)` - Render a small circular bundle preview as inline SVG.
- `ExplorerState` (class, `readmenator/_explorer.py:23`) `class ExplorerState` - Holds the precomputed payloads served by the explorer.
- `__init__` (method, `readmenator/_explorer.py:26`) `def __init__(self, config, nodes, edges, resolved_edges, analysis, findings, lay` - Initialise explorer state and precompute payloads.
- `samples` (method, `readmenator/_explorer.py:64`) `def samples(self)` - Return a compact per-file sample listing.
- `source` (method, `readmenator/_explorer.py:80`) `def source(self, file_id)` - Return the bounded source text for one file.
- `_Handler` (class, `readmenator/_explorer.py:105`) `class _Handler(BaseHTTPRequestHandler)` - HTTP handler serving explorer HTML and JSON APIs.
- `log_message` (method, `readmenator/_explorer.py:108`) `def log_message(self, fmt)` - Silence the default access log.
- `do_GET` (method, `readmenator/_explorer.py:112`) `def do_GET(self)` - Dispatch GET routes for HTML and JSON APIs.
- `_serve_html` (method, `readmenator/_explorer.py:135`) `def _serve_html(self)` - Serve the precomputed explorer HTML document.
- `_serve_vendor` (method, `readmenator/_explorer.py:144`) `def _serve_vendor(self)` - Serve the vendored 2D graph engine beside the page.
- `_serve_json` (method, `readmenator/_explorer.py:158`) `def _serve_json(self, payload)` - Serve a JSON payload with permissive CORS headers.
- `find_free_port` (function, `readmenator/_explorer.py:169`) `def find_free_port(preferred)` - Find a free TCP port, preferring the configured value.
- `serve` (function, `readmenator/_explorer.py:188`) `def serve(state, host, port, open_browser)` - Serve the explorer state until interrupted.
- `build_state` (function, `readmenator/_explorer.py:221`) `def build_state(config, nodes, edges, resolved_edges, analysis, findings, layers` - Build explorer state without starting the server.
- `write_static` (function, `readmenator/_explorer.py:249`) `def write_static(state, output_dir, filename)` - Write the explorer HTML to a static file.
- `family_color_from_name` (function, `readmenator/_forcegraph.py:39`) `def family_color_from_name(name, sat_base, sat_span, light_base, light_span)` - Derive a stable, visually-distinct HSL color from a label.
- `node_value` (function, `readmenator/_forcegraph.py:67`) `def node_value(symbols, degree)` - Scale a node value with log2 dampening.
- `ForceGraphRenderer` (class, `readmenator/_forcegraph.py:80`) `class ForceGraphRenderer` - Builds force-graph payloads and renders the explorer HTML.
- `__init__` (method, `readmenator/_forcegraph.py:83`) `def __init__(self, config)` - Initialise with application configuration.
- `node_palette` (method, `readmenator/_forcegraph.py:91`) `def node_palette(self)` - Return the node-type color palette from configuration.
- `edge_palette` (method, `readmenator/_forcegraph.py:95`) `def edge_palette(self)` - Return the edge-relation color palette from configuration.
- `vendor_source` (method, `readmenator/_forcegraph.py:99`) `def vendor_source(self)` - Return the path of the vendored 2D engine shipped in the package.
- `vendor_href` (method, `readmenator/_forcegraph.py:107`) `def vendor_href(self)` - Return the relative vendor script href used beside the page.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 22
- Cross-boundary resolved imports (EXTRACTED): 40

## Connections

- [EXTRACTED] depends_on community 5 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs_page.py imports readmenator/_htmlpack.py.
- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_bundlegraph.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_bundlegraph.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_forcegraph.py.
- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_explorer.py imports readmenator/_models.py.
- [INFERRED] bridges community 5 <-> 4 (strength 0.5): Inferred cross-community bridge: readmenator/_docstrings.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 2 <-> 4 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 3 <-> 4 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_graphlayout.py in 5 hops.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_htmlpack.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph_page.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_htmlpack.py` via `subprocess` (2 hops)
- [layer strict] `tests/test_layout_quality.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation)

## Open Questions

- What would break if the most connected file in readmenator: _graphlayout changed?
- Should readmenator: _graphlayout be split, given cohesion 0.38?

## Sources

- `readmenator/_bundlegraph.py`
- `readmenator/_bundlegraph_page.py`
- `readmenator/_explorer.py`
- `readmenator/_forcegraph.py`
- `readmenator/_forcegraph_page.py`
- `readmenator/_graphlayout.py`
- `readmenator/_htmlpack.py`
- `readmenator/_sourceview.py`
- `tests/test_bundlegraph.py`
- `tests/test_graphlayout.py`
- `tests/test_htmlpack.py`
- `tests/test_layout_quality.py`
- `tests/test_sourceview.py`
