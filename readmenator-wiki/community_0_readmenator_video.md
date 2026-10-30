# readmenator: _video

*Community 0 | 41 files | cohesion 0.35*

## Definition

This community groups 41 file(s) rooted at `tests` with dominant language py (cohesion 0.35). Central symbols: `ArchitectureLinter`, `Backdrop`, `CinematicVideoRenderer`, `Config`, `CursorRulesGenerator`, `DataflowAnalyzer`, `DeadCodeStripper`, `DirectoryWatcher`. Core file: `readmenator/_video.py` (98 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

### `tests` (21 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_diagrams.py` | py | testing | 73 | yes |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_githistory.py` | py | testing | 22 | yes |
| `tests/test_htmlpack.py` | py | testing | 18 | yes |
| `tests/test_integration.py` | py | testing | 16 | no |

### `readmenator` (19 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__main__.py` | py | utility | 3 | yes |
| `readmenator/_app.py` | py | utility | 88 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_githistory.py` | py | utility | 23 | yes |
| `readmenator/_hypotheses.py` | py | utility | 10 | yes |
| `readmenator/_layers.py` | py | utility | 7 | yes |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |

*... and 21 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:138`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:153`) `def main()`
- `readmenatorApplication` (class, `readmenator/_app.py:54`) `class readmenatorApplication`
- `__init__` (method, `readmenator/_app.py:55`) `def __init__(self, config)`
- `ingest_receipts` (method, `readmenator/_app.py:64`) `def ingest_receipts(self, target_dir, receipts_dir)` - Ingest deploynator release receipts into the release layer.
- `_scan` (method, `readmenator/_app.py:93`) `def _scan(self, target_dir)`
- `_scan_with_content` (method, `readmenator/_app.py:101`) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (method, `readmenator/_app.py:111`) `def _resolve_imports(self, nodes, edges, target_dir)`
- `_apply_project_config` (method, `readmenator/_app.py:130`) `def _apply_project_config(self, target_dir)` - Ensure readmenator.toml exists and adopt it as project truth.
- `_write_viewer_config` (method, `readmenator/_app.py:161`) `def _write_viewer_config(self, root)` - Write maps config.json from the effective config (never fatal).
- `run` (method, `readmenator/_app.py:179`) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_an`
- `check_freshness` (method, `readmenator/_app.py:333`) `def check_freshness(self, target_dir)` - Compare the MANIFEST source fingerprint against the current sources.
- `_maybe_refresh_pages` (method, `readmenator/_app.py:360`) `def _maybe_refresh_pages(self, root)` - Refresh the static docs site when a previous ``pages`` run created it.
- `_maybe_publish_github_wiki` (method, `readmenator/_app.py:378`) `def _maybe_publish_github_wiki(self, root)` - Publish generated docs to the GitHub wiki on every run of a git checkout.
- `publish_github_wiki` (method, `readmenator/_app.py:396`) `def publish_github_wiki(self, target_dir, dry_run)` - Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `_write_sidecar_outputs` (method, `readmenator/_app.py:412`) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_write_folder_readmes` (method, `readmenator/_app.py:438`) `def _write_folder_readmes(self, root)` - Write README.md into every generated readmenator-* folder (never fatal).
- `_inject_readme_link` (method, `readmenator/_app.py:453`) `def _inject_readme_link(self, root)`
- `_inject_agent_files` (method, `readmenator/_app.py:461`) `def _inject_agent_files(self, root)`
- `generate_uml_code` (method, `readmenator/_app.py:469`) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (method, `readmenator/_app.py:481`) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summa`
- `update` (method, `readmenator/_app.py:536`) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (method, `readmenator/_app.py:652`) `def _scan_for_cache(self, root, cache)`
- `query` (method, `readmenator/_app.py:670`) `def query(self, target_dir, question)`
- `explain` (method, `readmenator/_app.py:675`) `def explain(self, target_dir, symbol_name)`
- `find_path` (method, `readmenator/_app.py:687`) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (method, `readmenator/_app.py:700`) `def summary(self, target_dir)`
- `rank_query` (method, `readmenator/_app.py:705`) `def rank_query(self, target_dir, query, top_n)` - Run a ranked query against the knowledge graph.
- `rebuild` (method, `readmenator/_app.py:735`) `def rebuild(self, target_dir, run_security)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 82
- Cross-boundary resolved imports (EXTRACTED): 166

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

- Why do 9 file(s) lack file-level docs (e.g. `tests/test_config.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _video changed?
- Should readmenator: _video be split, given cohesion 0.35?

## Sources

- `readmenator.py`
- `readmenator/__main__.py`
- `readmenator/_app.py`
- `readmenator/_config.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_githistory.py`
- `readmenator/_hypotheses.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- `readmenator/_mcp_server.py`
- `readmenator/_receipts.py`
- `readmenator/_refactorizer.py`
- `readmenator/_scanner.py`
- `readmenator/_taint.py`
- `readmenator/_uncertainty.py`
- `readmenator/_video.py`
- `readmenator/_watcher.py`
- `readmenator/_yaralite.py`
- *... and 21 more*
