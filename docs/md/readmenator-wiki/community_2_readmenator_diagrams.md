# readmenator: _diagrams

*Community 2 | 31 files | cohesion 0.40*

## Definition

This community groups 31 file(s) rooted at `readmenator` with dominant language py (cohesion 0.40). Central symbols: `ArchitectureLinter`, `Backdrop`, `CallSite`, `Category`, `CinematicVideoRenderer`, `ComponentDiagramBuilder`, `CompositeRanker`, `CursorRulesGenerator`. Core file: `readmenator/_diagrams.py` (92 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

### `readmenator` (19 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/__main__.py` | py | utility | 3 | yes |
| `readmenator/_app.py` | py | utility | 81 | yes |
| `readmenator/_category.py` | py | utility | 26 | yes |
| `readmenator/_components.py` | py | presentation | 25 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_diagrams.py` | py | utility | 92 | yes |
| `readmenator/_explain.py` | py | utility | 3 | yes |
| `readmenator/_layers.py` | py | utility | 7 | yes |
| `readmenator/_linter.py` | py | utility | 8 | yes |

### `tests` (11 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_components.py` | py | testing | 36 | yes |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_diagrams.py` | py | testing | 73 | yes |
| `tests/test_integration.py` | py | testing | 16 | no |
| `tests/test_linter.py` | py | testing | 14 | yes |
| `tests/test_mcp_server.py` | py | testing | 25 | yes |
| `tests/test_ollama.py` | py | testing | 4 | yes |
| `tests/test_query.py` | py | testing | 18 | no |
| `tests/test_ranking.py` | py | testing | 72 | yes |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |

*... and 11 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:135`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:150`) `def main()`
- `readmenatorApplication` (class, `readmenator/_app.py:52`) `class readmenatorApplication`
- `__init__` (method, `readmenator/_app.py:53`) `def __init__(self, config)`
- `_scan` (method, `readmenator/_app.py:62`) `def _scan(self, target_dir)`
- `_scan_with_content` (method, `readmenator/_app.py:70`) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (method, `readmenator/_app.py:80`) `def _resolve_imports(self, nodes, edges, target_dir)`
- `run` (method, `readmenator/_app.py:99`) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_an`
- `check_freshness` (method, `readmenator/_app.py:250`) `def check_freshness(self, target_dir)` - Compare the MANIFEST source fingerprint against the current sources.
- `_maybe_refresh_pages` (method, `readmenator/_app.py:277`) `def _maybe_refresh_pages(self, root)` - Refresh the static docs site when a previous ``pages`` run created it.
- `_maybe_publish_github_wiki` (method, `readmenator/_app.py:295`) `def _maybe_publish_github_wiki(self, root)` - Publish generated docs to the GitHub wiki on every run of a git checkout.
- `publish_github_wiki` (method, `readmenator/_app.py:313`) `def publish_github_wiki(self, target_dir, dry_run)` - Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `_write_sidecar_outputs` (method, `readmenator/_app.py:327`) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_inject_readme_link` (method, `readmenator/_app.py:353`) `def _inject_readme_link(self, root)`
- `_inject_agent_files` (method, `readmenator/_app.py:361`) `def _inject_agent_files(self, root)`
- `generate_uml_code` (method, `readmenator/_app.py:369`) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (method, `readmenator/_app.py:381`) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summa`
- `update` (method, `readmenator/_app.py:436`) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (method, `readmenator/_app.py:549`) `def _scan_for_cache(self, root, cache)`
- `query` (method, `readmenator/_app.py:567`) `def query(self, target_dir, question)`
- `explain` (method, `readmenator/_app.py:572`) `def explain(self, target_dir, symbol_name)`
- `find_path` (method, `readmenator/_app.py:584`) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (method, `readmenator/_app.py:597`) `def summary(self, target_dir)`
- `rank_query` (method, `readmenator/_app.py:602`) `def rank_query(self, target_dir, query, top_n)` - Run a ranked query against the knowledge graph.
- `rebuild` (method, `readmenator/_app.py:632`) `def rebuild(self, target_dir, run_security)`
- `analyze` (method, `readmenator/_app.py:635`) `def analyze(self, target_dir)`
- `export_json` (method, `readmenator/_app.py:639`) `def export_json(self, target_dir, output_path)`
- `export_html` (method, `readmenator/_app.py:656`) `def export_html(self, target_dir, output_path)`
- `export_svg` (method, `readmenator/_app.py:667`) `def export_svg(self, target_dir, output_path)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 61
- Cross-boundary resolved imports (EXTRACTED): 94

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_readme_injector.py.
- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_uml.py.
- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_bundlegraph.py.
- [INFERRED] bridges community 2 <-> 5 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.
- [INFERRED] bridges community 2 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 2 <-> 5 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_readme_injector.py in 5 hops.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_diagrams.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [layer strict] `tests/test_components.py` (testing) -> `readmenator/_components.py` (presentation)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_integration.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_diagrams.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _diagrams changed?
- Should readmenator: _diagrams be split, given cohesion 0.40?

## Sources

- `readmenator.py`
- `readmenator/__init__.py`
- `readmenator/__main__.py`
- `readmenator/_app.py`
- `readmenator/_category.py`
- `readmenator/_components.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_diagrams.py`
- `readmenator/_explain.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- `readmenator/_mcp_server.py`
- `readmenator/_ollama.py`
- `readmenator/_projections.py`
- `readmenator/_query.py`
- `readmenator/_rank.py`
- `readmenator/_symindex.py`
- `readmenator/_video.py`
- `readmenator/_watcher.py`
- `readmenator/_yaralite.py`
- *... and 11 more*
