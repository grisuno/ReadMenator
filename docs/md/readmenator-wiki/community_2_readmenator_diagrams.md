# readmenator: _diagrams

*Community 2 | 20 files | cohesion 0.33*

## Definition

This community groups 20 file(s) rooted at `readmenator` with dominant language py (cohesion 0.33). Central symbols: `ArchitectureLinter`, `ConceptExtractor`, `CursorRulesGenerator`, `DirectoryWatcher`, `DocsSitePublisher`, `GitHubWikiPublisher`, `InteractiveMapRenderer`, `LayerDetector`. Core file: `readmenator/_diagrams.py` (90 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/__main__.py` | py | utility | 3 | yes |
| `readmenator/_app.py` | py | utility | 71 | yes |
| `readmenator/_concepts.py` | py | utility | 8 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_diagrams.py` | py | utility | 90 | yes |
| `readmenator/_gh_wiki.py` | py | utility | 18 | yes |
| `readmenator/_layers.py` | py | utility | 7 | yes |
| `readmenator/_linter.py` | py | utility | 7 | yes |
| `readmenator/_mcp_server.py` | py | utility | 64 | yes |
| `readmenator/_watcher.py` | py | utility | 5 | yes |
| `readmenator/_yaralite.py` | py | utility | 20 | yes |
| `tests/test_concepts.py` | py | testing | 8 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_diagrams.py` | py | testing | 69 | yes |
| `tests/test_gh_wiki.py` | py | testing | 17 | yes |
| `tests/test_integration.py` | py | testing | 16 | no |
| `tests/test_linter.py` | py | testing | 14 | yes |
| `tests/test_mcp_server.py` | py | testing | 25 | yes |

## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:131`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:146`) `def main()`
- `readmenatorApplication` (class, `readmenator/_app.py:48`) `class readmenatorApplication`
- `__init__` (method, `readmenator/_app.py:49`) `def __init__(self, config)`
- `_scan` (method, `readmenator/_app.py:58`) `def _scan(self, target_dir)`
- `_scan_with_content` (method, `readmenator/_app.py:66`) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (method, `readmenator/_app.py:76`) `def _resolve_imports(self, nodes, edges, target_dir)`
- `run` (method, `readmenator/_app.py:95`) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_an`
- `check_freshness` (method, `readmenator/_app.py:237`) `def check_freshness(self, target_dir)` - Compare the MANIFEST source fingerprint against the current sources.
- `_maybe_refresh_pages` (method, `readmenator/_app.py:264`) `def _maybe_refresh_pages(self, root)` - Refresh the static docs site when a previous ``pages`` run created it.
- `_maybe_publish_github_wiki` (method, `readmenator/_app.py:282`) `def _maybe_publish_github_wiki(self, root)` - Publish generated docs to the GitHub wiki on every run of a git checkout.
- `publish_github_wiki` (method, `readmenator/_app.py:300`) `def publish_github_wiki(self, target_dir, dry_run)` - Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `_write_sidecar_outputs` (method, `readmenator/_app.py:314`) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_inject_readme_link` (method, `readmenator/_app.py:340`) `def _inject_readme_link(self, root)`
- `_inject_agent_files` (method, `readmenator/_app.py:348`) `def _inject_agent_files(self, root)`
- `generate_uml_code` (method, `readmenator/_app.py:356`) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (method, `readmenator/_app.py:368`) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summa`
- `update` (method, `readmenator/_app.py:423`) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (method, `readmenator/_app.py:528`) `def _scan_for_cache(self, root, cache)`
- `query` (method, `readmenator/_app.py:546`) `def query(self, target_dir, question)`
- `explain` (method, `readmenator/_app.py:551`) `def explain(self, target_dir, symbol_name)`
- `find_path` (method, `readmenator/_app.py:563`) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (method, `readmenator/_app.py:576`) `def summary(self, target_dir)`
- `rank_query` (method, `readmenator/_app.py:581`) `def rank_query(self, target_dir, query, top_n)` - Run a ranked query against the knowledge graph.
- `rebuild` (method, `readmenator/_app.py:611`) `def rebuild(self, target_dir, run_security)`
- `analyze` (method, `readmenator/_app.py:614`) `def analyze(self, target_dir)`
- `export_json` (method, `readmenator/_app.py:618`) `def export_json(self, target_dir, output_path)`
- `export_html` (method, `readmenator/_app.py:635`) `def export_html(self, target_dir, output_path)`
- `export_svg` (method, `readmenator/_app.py:646`) `def export_svg(self, target_dir, output_path)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 31
- Cross-boundary resolved imports (EXTRACTED): 61

## Connections

- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_category.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_readme_injector.py.
- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_uml.py.
- [INFERRED] bridges community 2 <-> 5 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.
- [INFERRED] bridges community 2 <-> 4 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 2 <-> 5 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_readme_injector.py in 5 hops.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_diagrams.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_gh_wiki.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_concepts.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_diagrams.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _diagrams changed?
- Should readmenator: _diagrams be split, given cohesion 0.33?

## Sources

- `readmenator.py`
- `readmenator/__init__.py`
- `readmenator/__main__.py`
- `readmenator/_app.py`
- `readmenator/_concepts.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_diagrams.py`
- `readmenator/_gh_wiki.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- `readmenator/_mcp_server.py`
- `readmenator/_watcher.py`
- `readmenator/_yaralite.py`
- `tests/test_concepts.py`
- `tests/test_cursorrules.py`
- `tests/test_diagrams.py`
- `tests/test_gh_wiki.py`
- `tests/test_integration.py`
- `tests/test_linter.py`
- `tests/test_mcp_server.py`
