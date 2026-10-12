# readmenator: _pipeline

*Community 0 | 44 files | cohesion 0.43*

## Definition

This community groups 44 file(s) rooted at `readmenator` with dominant language py (cohesion 0.43). Central symbols: `AnalyticsBuilder`, `AnalyzerFactory`, `BundleGraphRenderer`, `BundleLayout`, `CodePropertyGraph`, `Config`, `DataflowAnalyzer`, `DeepAnalysisRunner`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Corpus analytics aggregations for the readmenator knowledge graph.  Computes the explorer dashboard payloads (attribution funnel, distributions, scatter, rule y.

## Files

### `readmenator` (25 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analytics.py` | py | utility | 9 | yes |
| `readmenator/_bundlegraph.py` | py | utility | 8 | yes |
| `readmenator/_bundlegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_documentation.py` | py | utility | 31 | yes |
| `readmenator/_embed.py` | py | utility | 11 | yes |
| `readmenator/_exclusions.py` | py | utility | 11 | yes |
| `readmenator/_explorer.py` | py | utility | 14 | yes |

### `tests` (19 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_bundlegraph.py` | py | testing | 27 | yes |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_graphlayout.py` | py | testing | 33 | yes |
| `tests/test_hotspots.py` | py | testing | 11 | no |
| `tests/test_htmlpack.py` | py | testing | 18 | yes |
| `tests/test_interactive_graph.py` | py | testing | 60 | yes |

*... and 24 more files in this community.*


## Key Symbols

- `AnalyticsBuilder` (class, `readmenator/_analytics.py:25`) `class AnalyticsBuilder` - Builds analytics payloads from scanned topology and findings.
- `__init__` (method, `readmenator/_analytics.py:28`) `def __init__(self, config)` - Initialise with application configuration.
- `build` (method, `readmenator/_analytics.py:36`) `def build(self, nodes, edges, resolved_edges, analysis, findings, layers, v2, ho` - Build the full analytics payload.
- `_layer_distribution` (method, `readmenator/_analytics.py:100`) `def _layer_distribution(self, nodes, layers)` - Count files per architectural layer.
- `_language_distribution` (method, `readmenator/_analytics.py:112`) `def _language_distribution(self, nodes)` - Count files per programming language.
- `_hotspot_ranking` (method, `readmenator/_analytics.py:120`) `def _hotspot_ranking(self, nodes, fan_in, fan_out, hotspots)` - Rank files by combined symbol and connectivity weight.
- `_rule_yield` (method, `readmenator/_analytics.py:152`) `def _rule_yield(self, findings)` - Count security findings per rule with severity breakdown.
- `_size_bands` (method, `readmenator/_analytics.py:164`) `def _size_bands(self, nodes)` - Bucket files by symbol-count bands.
- `_scatter` (method, `readmenator/_analytics.py:181`) `def _scatter(self, nodes, fan_in, fan_out, layers)` - Build a file scatter of symbols versus connectivity.
- `_json_script` (function, `readmenator/_bundlegraph.py:37`) `def _json_script(value)` - Serialize a value for an inline script, escaping angle brackets.
- `BundleGraphRenderer` (class, `readmenator/_bundlegraph.py:49`) `class BundleGraphRenderer` - Builds the bundle payload and renders the edge bundle explorer page.
- `__init__` (method, `readmenator/_bundlegraph.py:52`) `def __init__(self, config)` - Initialise with application configuration.
- `build_payload` (method, `readmenator/_bundlegraph.py:61`) `def build_payload(self, force_payload)` - Derive the bundle payload from a force-graph payload.
- `page_settings` (method, `readmenator/_bundlegraph.py:182`) `def page_settings(self, force_payload, explorer_href, live_api)` - Collect the page settings serialized into the HTML.
- `render` (method, `readmenator/_bundlegraph.py:226`) `def render(self, force_payload, title, home_href, explorer_href, live_api)` - Render the standalone edge bundle explorer HTML document.
- `write` (method, `readmenator/_bundlegraph.py:265`) `def write(self, output_path, force_payload, title, home_href, explorer_href)` - Write the edge bundle explorer HTML document.
- `thumbnail_svg` (method, `readmenator/_bundlegraph.py:291`) `def thumbnail_svg(self, force_payload)` - Render a small circular bundle preview as inline SVG.
- `Config` (class, `readmenator/_config.py:15`) `class Config` - Single source of truth for all readmenator settings.
- `CodePropertyGraph` (class, `readmenator/_cpg.py:16`) `class CodePropertyGraph` - Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.
- `__init__` (method, `readmenator/_cpg.py:26`) `def __init__(self, privacy_mode, cpg_context)`
- `generate` (method, `readmenator/_cpg.py:30`) `def generate(self, nodes, edges, resolved_edges, analysis, findings)` - Generate the CPG JSON-LD string embeddable in markdown.
- `_severity_counts` (method, `readmenator/_cpg.py:147`) `def _severity_counts(self, findings)`
- `_build_symbol_list` (method, `readmenator/_cpg.py:153`) `def _build_symbol_list(self, node)`
- `_compute_node_hash` (method, `readmenator/_cpg.py:169`) `def _compute_node_hash(node)`
- `_strip_noise` (function, `readmenator/_dataflow.py:96`) `def _strip_noise(line)` - Remove comments and string contents that confuse identifier scans.
- `_strip_block_comments` (function, `readmenator/_dataflow.py:107`) `def _strip_block_comments(content)` - Blank block comments while preserving newlines and line numbers.
- `_blank` (function, `readmenator/_dataflow.py:110`) `def _blank(match)`
- `_strip_sizeof` (function, `readmenator/_dataflow.py:116`) `def _strip_sizeof(line)` - Blank sizeof operands, which never evaluate their argument at runtime.
- `DataflowAnalyzer` (class, `readmenator/_dataflow.py:122`) `class DataflowAnalyzer` - Regex-based intra-function dataflow checker over scanned content.
- `__init__` (method, `readmenator/_dataflow.py:125`) `def __init__(self, config)` - Store configuration for enable flag and issue caps.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 104
- Cross-boundary resolved imports (EXTRACTED): 152

## Connections

- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__main__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 5 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_analyzer.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [INFERRED] bridges community 4 <-> 0 (strength 0.5): Inferred cross-community bridge: readmenator/_docstrings.py reaches tests/test_graphlayout.py in 5 hops.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_htmlpack.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_flowcharts.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_pytypes.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_flowlayout.py` via `subprocess` (2 hops)

## Open Questions

- Why do 8 file(s) lack file-level docs (e.g. `tests/test_config.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_documentation.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _pipeline changed?
- Should readmenator: _pipeline be split, given cohesion 0.43?

## Sources

- `readmenator/_analytics.py`
- `readmenator/_bundlegraph.py`
- `readmenator/_bundlegraph_page.py`
- `readmenator/_config.py`
- `readmenator/_cpg.py`
- `readmenator/_dataflow.py`
- `readmenator/_documentation.py`
- `readmenator/_embed.py`
- `readmenator/_exclusions.py`
- `readmenator/_explorer.py`
- `readmenator/_exporter.py`
- `readmenator/_forcegraph.py`
- `readmenator/_forcegraph_page.py`
- `readmenator/_graphlayout.py`
- `readmenator/_hotspots.py`
- `readmenator/_htmlpack.py`
- `readmenator/_layer_rules.py`
- `readmenator/_ollama.py`
- `readmenator/_pipeline.py`
- `readmenator/_provenance.py`
- *... and 24 more*
