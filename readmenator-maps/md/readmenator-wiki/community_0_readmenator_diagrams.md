# readmenator: _diagrams

*Community 0 | 50 files | cohesion 0.55*

## Definition

This community groups 50 file(s) rooted at `readmenator` with dominant language py (cohesion 0.55). Central symbols: `AnalyzerFactory`, `ArchitectureLinter`, `Backdrop`, `CinematicVideoRenderer`, `CodePropertyGraph`, `Config`, `CursorRulesGenerator`, `DataflowAnalyzer`. Core file: `readmenator/_diagrams.py` (79 symbols). Documented purpose: Launcher shim that runs the readmenator CLI from a source checkout..

## Files

### `readmenator` (27 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/__main__.py` | py | utility | 3 | yes |
| `readmenator/_analyzer.py` | py | utility | 18 | yes |
| `readmenator/_app.py` | py | utility | 50 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_cursorrules_generator.py` | py | utility | 8 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_diagrams.py` | py | utility | 79 | yes |

### `tests` (22 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_diagrams.py` | py | testing | 69 | yes |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_hotspots.py` | py | testing | 11 | no |

### `.` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator.py` | py | utility | 0 | yes |

*... and 30 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:18`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:121`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:136`) `def main()`
- `dominant_directory` (function, `readmenator/_analyzer.py:22`) `def dominant_directory(file_ids)` - Return the most informative directory label for a set of files.
- `GraphAnalyzer` (class, `readmenator/_analyzer.py:40`) `class GraphAnalyzer` - Deterministic graph analysis over scanned nodes and edges.
- `__init__` (method, `readmenator/_analyzer.py:48`) `def __init__(self, config)` - Initialise with application configuration.
- `analyze` (method, `readmenator/_analyzer.py:56`) `def analyze(self, nodes, edges, resolved_edges)` - Run the full analysis pipeline and return structured results.
- `_build_adjacency` (method, `readmenator/_analyzer.py:109`) `def _build_adjacency(self, nodes, edges)` - Build an undirected adjacency map from import edges.
- `_build_reverse_adjacency` (method, `readmenator/_analyzer.py:123`) `def _build_reverse_adjacency(self, adjacency)` - Build a directed reverse adjacency (incoming edges) map.
- `_compute_god_nodes` (method, `readmenator/_analyzer.py:133`) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` - Compute the most central nodes using combined degree centrality.
- `_detect_communities` (method, `readmenator/_analyzer.py:155`) `def _detect_communities(self, nodes, adjacency)` - Detect communities using label propagation.
- `_merge_small_communities` (method, `readmenator/_analyzer.py:217`) `def _merge_small_communities(self, groups, adjacency, weights)` - Fold communities smaller than COMMUNITY_MERGE_BELOW into their best neighbor.
- `_vote_weights` (method, `readmenator/_analyzer.py:264`) `def _vote_weights(self, file_ids, adjacency)` - Return each node's label-propagation vote weight.
- `_label_communities` (method, `readmenator/_analyzer.py:281`) `def _label_communities(self, nodes, communities)` - Generate human-readable labels for communities.
- `_core_file` (method, `readmenator/_analyzer.py:308`) `def _core_file(members, node_map)` - Return the stem of a community's most symbol-rich non-test file.
- `is_test` (method, `readmenator/_analyzer.py:314`) `def is_test(fid)` - Return whether a path looks like a test file.
- `_build_community_map` (method, `readmenator/_analyzer.py:328`) `def _build_community_map(self, communities)` - Build a reverse map from file ID to community ID.
- `_compute_cohesion` (method, `readmenator/_analyzer.py:338`) `def _compute_cohesion(self, communities, adjacency)` - Compute cohesion score for each community.
- `_find_surprising_connections` (method, `readmenator/_analyzer.py:363`) `def _find_surprising_connections(self, nodes, adjacency, community_map)` - Find non-obvious cross-community bridges.
- `_shortest_path_communities` (method, `readmenator/_analyzer.py:403`) `def _shortest_path_communities(self, source, target, adjacency, community_map)` - Find the shortest path and communities traversed.
- `_suggest_questions` (method, `readmenator/_analyzer.py:430`) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, su` - Generate plain-language exploration questions from graph structure.
- `readmenatorApplication` (class, `readmenator/_app.py:43`) `class readmenatorApplication`
- `__init__` (method, `readmenator/_app.py:44`) `def __init__(self, config)`
- `_scan` (method, `readmenator/_app.py:53`) `def _scan(self, target_dir)`
- `_scan_with_content` (method, `readmenator/_app.py:61`) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (method, `readmenator/_app.py:71`) `def _resolve_imports(self, nodes, edges, target_dir)`
- `run` (method, `readmenator/_app.py:90`) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_an`
- `check_freshness` (method, `readmenator/_app.py:214`) `def check_freshness(self, target_dir)` - Compare the MANIFEST source fingerprint against the current sources.
- `_maybe_refresh_pages` (method, `readmenator/_app.py:241`) `def _maybe_refresh_pages(self, root)` - Refresh the static docs site when a previous ``pages`` run created it.
- `_maybe_publish_github_wiki` (method, `readmenator/_app.py:259`) `def _maybe_publish_github_wiki(self, root)` - Publish generated docs to the GitHub wiki when GH_WIKI_ENABLED is set.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 110
- Cross-boundary resolved imports (EXTRACTED): 97

## Connections

- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_category.py.
- [EXTRACTED] depends_on community 0 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [EXTRACTED] depends_on community 0 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_scanner.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/__init__.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/__main__.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.
- [INFERRED] bridges community 0 <-> 2 (strength 0.5): Inferred cross-community bridge: tests/test_readme_injector.py reaches tests/test_resolver.py in 5 hops.

## Risks

- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_video.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `tests/test_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 10 file(s) lack file-level docs (e.g. `tests/test_config.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_video.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _diagrams changed?
- Should readmenator: _diagrams be split, given cohesion 0.55?

## Sources

- `readmenator.py`
- `readmenator/__init__.py`
- `readmenator/__main__.py`
- `readmenator/_analyzer.py`
- `readmenator/_app.py`
- `readmenator/_config.py`
- `readmenator/_cpg.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_diagrams.py`
- `readmenator/_exporter.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- `readmenator/_mcp_server.py`
- `readmenator/_pipeline.py`
- `readmenator/_query.py`
- `readmenator/_readme_injector.py`
- *... and 30 more*
