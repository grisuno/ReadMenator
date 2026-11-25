# readmenator: _app

*Community 0 | 46 files | cohesion 0.36*

## Definition

This community groups 46 file(s) rooted at `readmenator` with dominant language py (cohesion 0.36). Central symbols: `AnalyticsBuilder`, `ArchitectureLinter`, `ConceptExtractor`, `Config`, `CursorRulesGenerator`, `DataflowAnalyzer`, `DeadCodeStripper`, `DirectoryWatcher`. Core file: `readmenator/_app.py` (90 symbols). Documented purpose: Corpus analytics aggregations for the readmenator knowledge graph.  Computes the explorer dashboard payloads (attribution funnel, distributions, scatter, rule y.

## Files

### `readmenator` (24 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analytics.py` | py | utility | 9 | yes |
| `readmenator/_app.py` | py | utility | 90 | yes |
| `readmenator/_concepts.py` | py | utility | 8 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_docbranch.py` | py | utility | 12 | yes |
| `readmenator/_embed.py` | py | utility | 11 | yes |
| `readmenator/_exclusions.py` | py | utility | 11 | yes |

### `tests` (22 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_components.py` | py | testing | 37 | yes |
| `tests/test_concepts.py` | py | testing | 8 | no |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_diagrams.py` | py | testing | 73 | yes |
| `tests/test_docbranch.py` | py | testing | 37 | yes |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_gh_wiki.py` | py | testing | 17 | yes |

*... and 26 more files in this community.*


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
- `readmenatorApplication` (class, `readmenator/_app.py:56`) `class readmenatorApplication`
- `__init__` (method, `readmenator/_app.py:57`) `def __init__(self, config)`
- `ingest_receipts` (method, `readmenator/_app.py:66`) `def ingest_receipts(self, target_dir, receipts_dir)` - Ingest deploynator release receipts into the release layer.
- `_scan` (method, `readmenator/_app.py:95`) `def _scan(self, target_dir)`
- `_scan_with_content` (method, `readmenator/_app.py:103`) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (method, `readmenator/_app.py:113`) `def _resolve_imports(self, nodes, edges, target_dir)`
- `_apply_project_config` (method, `readmenator/_app.py:132`) `def _apply_project_config(self, target_dir)` - Ensure readmenator.toml exists and adopt it as project truth.
- `_write_viewer_config` (method, `readmenator/_app.py:163`) `def _write_viewer_config(self, root)` - Write maps config.json from the effective config (never fatal).
- `run` (method, `readmenator/_app.py:181`) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_an`
- `check_freshness` (method, `readmenator/_app.py:335`) `def check_freshness(self, target_dir)` - Compare the MANIFEST source fingerprint against the current sources.
- `_maybe_refresh_pages` (method, `readmenator/_app.py:362`) `def _maybe_refresh_pages(self, root)` - Refresh the static docs site when a previous ``pages`` run created it.
- `_maybe_publish_github_wiki` (method, `readmenator/_app.py:380`) `def _maybe_publish_github_wiki(self, root)` - Publish generated docs to the GitHub wiki on every run of a git checkout.
- `publish_github_wiki` (method, `readmenator/_app.py:398`) `def publish_github_wiki(self, target_dir, dry_run)` - Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `_write_sidecar_outputs` (method, `readmenator/_app.py:414`) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_write_folder_readmes` (method, `readmenator/_app.py:440`) `def _write_folder_readmes(self, root)` - Write README.md into every generated readmenator-* folder (never fatal).
- `_inject_readme_link` (method, `readmenator/_app.py:455`) `def _inject_readme_link(self, root)`
- `_inject_agent_files` (method, `readmenator/_app.py:463`) `def _inject_agent_files(self, root)`
- `generate_uml_code` (method, `readmenator/_app.py:471`) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (method, `readmenator/_app.py:483`) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summa`
- `update` (method, `readmenator/_app.py:538`) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (method, `readmenator/_app.py:654`) `def _scan_for_cache(self, root, cache)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 97
- Cross-boundary resolved imports (EXTRACTED): 167

## Connections

- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_app.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 5 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_bundlegraph.py.
- [EXTRACTED] depends_on community 0 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_resolver.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_docbranch.py` -> `readmenator/_docbranch.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_docbranch.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_docbranch.py` -> `readmenator/_gitmeta.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [layer strict] `tests/test_components.py` (testing) -> `readmenator/_components.py` (presentation)

## Open Questions

- Why do 9 file(s) lack file-level docs (e.g. `tests/test_concepts.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_docbranch.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _app changed?
- Should readmenator: _app be split, given cohesion 0.36?

## Sources

- `readmenator/_analytics.py`
- `readmenator/_app.py`
- `readmenator/_concepts.py`
- `readmenator/_config.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_docbranch.py`
- `readmenator/_embed.py`
- `readmenator/_exclusions.py`
- `readmenator/_explorer.py`
- `readmenator/_exporter.py`
- `readmenator/_hotspots.py`
- `readmenator/_hypotheses.py`
- `readmenator/_layer_rules.py`
- `readmenator/_linter.py`
- `readmenator/_provenance.py`
- `readmenator/_receipts.py`
- `readmenator/_refactorizer.py`
- `readmenator/_rule_gen.py`
- *... and 26 more*
