# readmenator: _pipeline

*Community 2 | 23 files | cohesion 0.35*

## Definition

This community groups 23 file(s) rooted at `readmenator` with dominant language py (cohesion 0.35). Central symbols: `AnalyticsBuilder`, `AnalyzerFactory`, `BundleGraphRenderer`, `BundleLayout`, `CodePropertyGraph`, `DeepAnalysisRunner`, `DocumentationGenerator`, `Embedder`. Core file: `tests/test_interactive_graph.py` (60 symbols). Documented purpose: Corpus analytics aggregations for the readmenator knowledge graph.  Computes the explorer dashboard payloads (attribution funnel, distributions, scatter, rule y.

## Files

### `readmenator` (16 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analytics.py` | py | utility | 9 | yes |
| `readmenator/_bundlegraph.py` | py | utility | 8 | yes |
| `readmenator/_bundlegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_documentation.py` | py | utility | 31 | yes |
| `readmenator/_embed.py` | py | utility | 11 | yes |
| `readmenator/_exclusions.py` | py | utility | 11 | yes |
| `readmenator/_explorer.py` | py | utility | 13 | yes |
| `readmenator/_exporter.py` | py | utility | 16 | yes |
| `readmenator/_forcegraph.py` | py | utility | 22 | yes |
| `readmenator/_forcegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_graphlayout.py` | py | utility | 18 | yes |
| `readmenator/_pipeline.py` | py | utility | 46 | yes |

### `tests` (7 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_bundlegraph.py` | py | testing | 27 | yes |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_graphlayout.py` | py | testing | 33 | yes |
| `tests/test_interactive_graph.py` | py | testing | 60 | yes |
| `tests/test_uml.py` | py | testing | 49 | yes |

*... and 3 more files in this community.*


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
- `_json_script` (function, `readmenator/_bundlegraph.py:36`) `def _json_script(value)` - Serialize a value for an inline script, escaping angle brackets.
- `BundleGraphRenderer` (class, `readmenator/_bundlegraph.py:48`) `class BundleGraphRenderer` - Builds the bundle payload and renders the edge bundle explorer page.
- `__init__` (method, `readmenator/_bundlegraph.py:51`) `def __init__(self, config)` - Initialise with application configuration.
- `build_payload` (method, `readmenator/_bundlegraph.py:60`) `def build_payload(self, force_payload)` - Derive the bundle payload from a force-graph payload.
- `page_settings` (method, `readmenator/_bundlegraph.py:147`) `def page_settings(self, force_payload, explorer_href)` - Collect the page settings serialized into the HTML.
- `render` (method, `readmenator/_bundlegraph.py:186`) `def render(self, force_payload, title, home_href, explorer_href)` - Render the standalone edge bundle explorer HTML document.
- `write` (method, `readmenator/_bundlegraph.py:222`) `def write(self, output_path, force_payload, title, home_href, explorer_href)` - Write the edge bundle explorer HTML document.
- `thumbnail_svg` (method, `readmenator/_bundlegraph.py:248`) `def thumbnail_svg(self, force_payload)` - Render a small circular bundle preview as inline SVG.
- `CodePropertyGraph` (class, `readmenator/_cpg.py:16`) `class CodePropertyGraph` - Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.
- `__init__` (method, `readmenator/_cpg.py:26`) `def __init__(self, privacy_mode, cpg_context)`
- `generate` (method, `readmenator/_cpg.py:30`) `def generate(self, nodes, edges, resolved_edges, analysis, findings)` - Generate the CPG JSON-LD string embeddable in markdown.
- `_severity_counts` (method, `readmenator/_cpg.py:147`) `def _severity_counts(self, findings)`
- `_build_symbol_list` (method, `readmenator/_cpg.py:153`) `def _build_symbol_list(self, node)`
- `_compute_node_hash` (method, `readmenator/_cpg.py:169`) `def _compute_node_hash(node)`
- `DocumentationGenerator` (class, `readmenator/_documentation.py:35`) `class DocumentationGenerator` - Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.
- `__init__` (method, `readmenator/_documentation.py:47`) `def __init__(self, config)`
- `_ranking_version` (method, `readmenator/_documentation.py:65`) `def _ranking_version(self)`
- `_get_git_commit` (method, `readmenator/_documentation.py:83`) `def _get_git_commit()`
- `generate` (method, `readmenator/_documentation.py:93`) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, ana`
- `_apply_context_budget` (method, `readmenator/_documentation.py:183`) `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis,`
- `_build_toc` (method, `readmenator/_documentation.py:321`) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncate`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 39
- Cross-boundary resolved imports (EXTRACTED): 81

## Connections

- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_uml.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_rank.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 5 <-> 2 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_graphlayout.py in 5 hops.

## Risks

- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_purpose.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_resolver.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph_page.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_graphlayout.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_cpg.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_documentation.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _pipeline changed?
- Should readmenator: _pipeline be split, given cohesion 0.35?

## Sources

- `readmenator/_analytics.py`
- `readmenator/_bundlegraph.py`
- `readmenator/_bundlegraph_page.py`
- `readmenator/_cpg.py`
- `readmenator/_documentation.py`
- `readmenator/_embed.py`
- `readmenator/_exclusions.py`
- `readmenator/_explorer.py`
- `readmenator/_exporter.py`
- `readmenator/_forcegraph.py`
- `readmenator/_forcegraph_page.py`
- `readmenator/_graphlayout.py`
- `readmenator/_pipeline.py`
- `readmenator/_provenance.py`
- `readmenator/_scantext.py`
- `readmenator/_uml.py`
- `tests/test_bundlegraph.py`
- `tests/test_cpg.py`
- `tests/test_documentation.py`
- `tests/test_exporter.py`
- *... and 3 more*
