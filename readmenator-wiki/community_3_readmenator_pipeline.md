# readmenator: _pipeline

*Community 3 | 20 files | cohesion 0.35*

## Definition

This community groups 20 file(s) rooted at `readmenator` with dominant language py (cohesion 0.35). Central symbols: `AnalyticsBuilder`, `AnalyzerFactory`, `BundleGraphRenderer`, `BundleLayout`, `DeepAnalysisRunner`, `Embedder`, `ExclusionEntry`, `ExclusionList`. Core file: `tests/test_interactive_graph.py` (60 symbols). Documented purpose: Corpus analytics aggregations for the readmenator knowledge graph.  Computes the explorer dashboard payloads (attribution funnel, distributions, scatter, rule y.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analytics.py` | py | utility | 9 | yes |
| `readmenator/_bundlegraph.py` | py | utility | 8 | yes |
| `readmenator/_bundlegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_embed.py` | py | utility | 11 | yes |
| `readmenator/_exclusions.py` | py | utility | 11 | yes |
| `readmenator/_explorer.py` | py | utility | 14 | yes |
| `readmenator/_exporter.py` | py | utility | 16 | yes |
| `readmenator/_forcegraph.py` | py | utility | 23 | yes |
| `readmenator/_forcegraph_page.py` | py | presentation | 0 | yes |
| `readmenator/_graphlayout.py` | py | utility | 26 | yes |
| `readmenator/_pipeline.py` | py | utility | 52 | yes |
| `readmenator/_provenance.py` | py | utility | 10 | yes |
| `readmenator/_scantext.py` | py | utility | 4 | yes |
| `readmenator/_sourceview.py` | py | utility | 8 | yes |
| `tests/test_bundlegraph.py` | py | testing | 27 | yes |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_graphlayout.py` | py | testing | 33 | yes |
| `tests/test_interactive_graph.py` | py | testing | 60 | yes |
| `tests/test_layout_quality.py` | py | testing | 16 | yes |
| `tests/test_sourceview.py` | py | testing | 23 | yes |

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
- `page_settings` (method, `readmenator/_bundlegraph.py:181`) `def page_settings(self, force_payload, explorer_href, live_api)` - Collect the page settings serialized into the HTML.
- `render` (method, `readmenator/_bundlegraph.py:225`) `def render(self, force_payload, title, home_href, explorer_href, live_api)` - Render the standalone edge bundle explorer HTML document.
- `write` (method, `readmenator/_bundlegraph.py:263`) `def write(self, output_path, force_payload, title, home_href, explorer_href)` - Write the edge bundle explorer HTML document.
- `thumbnail_svg` (method, `readmenator/_bundlegraph.py:289`) `def thumbnail_svg(self, force_payload)` - Render a small circular bundle preview as inline SVG.
- `_tokens` (function, `readmenator/_embed.py:22`) `def _tokens(text)` - Tokenize scan text into a lowercase term counter.
- `_jaccard` (function, `readmenator/_embed.py:27`) `def _jaccard(left, right)` - Compute Jaccard similarity between two token counters.
- `Embedder` (class, `readmenator/_embed.py:39`) `class Embedder` - Encodes scan-text blobs and answers similarity queries.
- `__init__` (method, `readmenator/_embed.py:42`) `def __init__(self, config)` - Initialise with application configuration.
- `dependencies_available` (method, `readmenator/_embed.py:50`) `def dependencies_available(self)` - Return True when sentence-transformers is importable.
- `encode` (method, `readmenator/_embed.py:58`) `def encode(self, texts)` - Encode texts into L2-normalized vectors when available.
- `near_jaccard` (method, `readmenator/_embed.py:75`) `def near_jaccard(self, query, corpus, top_k)` - Find nearest neighbors with offline Jaccard similarity.
- `cluster_jaccard` (method, `readmenator/_embed.py:99`) `def cluster_jaccard(self, corpus, threshold)` - Group files into similarity clusters with union-find.
- `find` (function, `readmenator/_embed.py:115`) `def find(item)` - Find the union-find root for an item.
- `union` (function, `readmenator/_embed.py:122`) `def union(left, right)` - Merge two union-find sets.
- `project_jaccard` (method, `readmenator/_embed.py:138`) `def project_jaccard(self, corpus)` - Project files to 2D with a deterministic radial layout.
- `ExclusionEntry` (class, `readmenator/_exclusions.py:19`) `class ExclusionEntry` - A single exclusion record from the blocklist file.
- `matches` (method, `readmenator/_exclusions.py:27`) `def matches(self, file_path, rule_id)` - Return True when this entry suppresses the finding.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 39
- Cross-boundary resolved imports (EXTRACTED): 80

## Connections

- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_bundlegraph.py.
- [EXTRACTED] depends_on community 4 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_analytics.py.
- [EXTRACTED] depends_on community 3 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [INFERRED] bridges community 4 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator/_docstrings.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 4 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator/_pytypes.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 2 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_graphlayout.py in 5 hops.

## Risks

- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_graphlayout.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph_page.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_sourceview.py` via `subprocess` (2 hops)
- [layer strict] `tests/test_layout_quality.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation)

## Open Questions

- What would break if the most connected file in readmenator: _pipeline changed?
- Should readmenator: _pipeline be split, given cohesion 0.35?

## Sources

- `readmenator/_analytics.py`
- `readmenator/_bundlegraph.py`
- `readmenator/_bundlegraph_page.py`
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
- `readmenator/_sourceview.py`
- `tests/test_bundlegraph.py`
- `tests/test_exporter.py`
- `tests/test_graphlayout.py`
- `tests/test_interactive_graph.py`
- `tests/test_layout_quality.py`
- `tests/test_sourceview.py`
