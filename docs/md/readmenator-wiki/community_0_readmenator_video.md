# readmenator: _video

*Community 0 | 35 files | cohesion 0.30*

## Definition

This community groups 35 file(s) rooted at `tests` with dominant language py (cohesion 0.30). Central symbols: `ArchitectureLinter`, `Backdrop`, `CinematicVideoRenderer`, `Config`, `CursorRulesGenerator`, `DataflowAnalyzer`, `DeadCodeStripper`, `DirectoryWatcher`. Core file: `readmenator/_video.py` (90 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

### `tests` (19 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_diagrams.py` | py | testing | 73 | yes |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_hotspots.py` | py | testing | 11 | no |
| `tests/test_htmlpack.py` | py | testing | 18 | yes |

### `readmenator` (15 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__main__.py` | py | utility | 3 | yes |
| `readmenator/_app.py` | py | utility | 87 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_hotspots.py` | py | utility | 7 | yes |
| `readmenator/_layer_rules.py` | py | business_logic | 4 | yes |
| `readmenator/_layers.py` | py | utility | 7 | yes |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |

*... and 15 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:137`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:152`) `def main()`
- `readmenatorApplication` (class, `readmenator/_app.py:54`) `class readmenatorApplication`
- `__init__` (method, `readmenator/_app.py:55`) `def __init__(self, config)`
- `_scan` (method, `readmenator/_app.py:64`) `def _scan(self, target_dir)`
- `_scan_with_content` (method, `readmenator/_app.py:72`) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (method, `readmenator/_app.py:82`) `def _resolve_imports(self, nodes, edges, target_dir)`
- `_apply_project_config` (method, `readmenator/_app.py:101`) `def _apply_project_config(self, target_dir)` - Ensure readmenator.toml exists and adopt it as project truth.
- `_write_viewer_config` (method, `readmenator/_app.py:132`) `def _write_viewer_config(self, root)` - Write maps config.json from the effective config (never fatal).
- `run` (method, `readmenator/_app.py:150`) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_an`
- `check_freshness` (method, `readmenator/_app.py:304`) `def check_freshness(self, target_dir)` - Compare the MANIFEST source fingerprint against the current sources.
- `_maybe_refresh_pages` (method, `readmenator/_app.py:331`) `def _maybe_refresh_pages(self, root)` - Refresh the static docs site when a previous ``pages`` run created it.
- `_maybe_publish_github_wiki` (method, `readmenator/_app.py:349`) `def _maybe_publish_github_wiki(self, root)` - Publish generated docs to the GitHub wiki on every run of a git checkout.
- `publish_github_wiki` (method, `readmenator/_app.py:367`) `def publish_github_wiki(self, target_dir, dry_run)` - Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `_write_sidecar_outputs` (method, `readmenator/_app.py:383`) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_write_folder_readmes` (method, `readmenator/_app.py:409`) `def _write_folder_readmes(self, root)` - Write README.md into every generated readmenator-* folder (never fatal).
- `_inject_readme_link` (method, `readmenator/_app.py:424`) `def _inject_readme_link(self, root)`
- `_inject_agent_files` (method, `readmenator/_app.py:432`) `def _inject_agent_files(self, root)`
- `generate_uml_code` (method, `readmenator/_app.py:440`) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (method, `readmenator/_app.py:452`) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summa`
- `update` (method, `readmenator/_app.py:507`) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (method, `readmenator/_app.py:623`) `def _scan_for_cache(self, root, cache)`
- `query` (method, `readmenator/_app.py:641`) `def query(self, target_dir, question)`
- `explain` (method, `readmenator/_app.py:646`) `def explain(self, target_dir, symbol_name)`
- `find_path` (method, `readmenator/_app.py:658`) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (method, `readmenator/_app.py:671`) `def summary(self, target_dir)`
- `rank_query` (method, `readmenator/_app.py:676`) `def rank_query(self, target_dir, query, top_n)` - Run a ranked query against the knowledge graph.
- `rebuild` (method, `readmenator/_app.py:706`) `def rebuild(self, target_dir, run_security)`
- `analyze` (method, `readmenator/_app.py:709`) `def analyze(self, target_dir)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 63
- Cross-boundary resolved imports (EXTRACTED): 163

## Connections

- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_app.py.
- [EXTRACTED] depends_on community 0 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__main__.py imports readmenator/_project_config.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 6 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_models.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 8 file(s) lack file-level docs (e.g. `tests/test_config.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _video changed?
- Should readmenator: _video be split, given cohesion 0.30?

## Sources

- `readmenator.py`
- `readmenator/__main__.py`
- `readmenator/_app.py`
- `readmenator/_config.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- `readmenator/_mcp_server.py`
- `readmenator/_refactorizer.py`
- `readmenator/_video.py`
- `readmenator/_watcher.py`
- `readmenator/_yaralite.py`
- `tests/test_config.py`
- `tests/test_cpg.py`
- `tests/test_cursorrules.py`
- `tests/test_dataflow.py`
- *... and 15 more*
