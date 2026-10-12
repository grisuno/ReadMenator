# readmenator: _security

*Community 5 | 6 files | cohesion 0.21*

## Definition

This community groups 6 file(s) rooted at `readmenator` with dominant language py (cohesion 0.21). Central symbols: `GraphAnalyzer`, `SecurityAnalyzer`, `SecurityRule`, `TestFixGuidance`, `TestGraphAnalyzerContract`, `TestSecurityAnalyzerConfig`, `TestSecurityAnalyzerPathValidation`, `TestSecurityAnalyzerRules`. Core file: `tests/test_security.py` (68 symbols). Documented purpose: Graph analysis engine for the readmenator knowledge graph.  Provides community detection (Louvain-like greedy modularity), god node identification (degree/PageR.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analyzer.py` | py | utility | 23 | yes |
| `readmenator/_security.py` | py | utility | 32 | yes |
| `readmenator/_wiki.py` | py | utility | 32 | yes |
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_security.py` | py | testing | 68 | yes |
| `tests/test_wiki.py` | py | testing | 30 | no |

## Key Symbols

- `dominant_directory` (function, `readmenator/_analyzer.py:22`) `def dominant_directory(file_ids)` - Return the most informative directory label for a set of files.
- `_is_test_path` (function, `readmenator/_analyzer.py:40`) `def _is_test_path(file_id)` - Return whether a project path looks like a test file or lives under tests/.
- `GraphAnalyzer` (class, `readmenator/_analyzer.py:46`) `class GraphAnalyzer` - Deterministic graph analysis over scanned nodes and edges.
- `__init__` (method, `readmenator/_analyzer.py:54`) `def __init__(self, config)` - Initialise with application configuration.
- `analyze` (method, `readmenator/_analyzer.py:62`) `def analyze(self, nodes, edges, resolved_edges)` - Run the full analysis pipeline and return structured results.
- `_build_adjacency` (method, `readmenator/_analyzer.py:115`) `def _build_adjacency(self, nodes, edges)` - Build an undirected adjacency map from import edges.
- `_build_reverse_adjacency` (method, `readmenator/_analyzer.py:129`) `def _build_reverse_adjacency(self, adjacency)` - Build a directed reverse adjacency (incoming edges) map.
- `_compute_god_nodes` (method, `readmenator/_analyzer.py:139`) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` - Compute the most central nodes using combined degree centrality.
- `_detect_communities` (method, `readmenator/_analyzer.py:161`) `def _detect_communities(self, nodes, adjacency)` - Detect communities using label propagation.
- `_finalize_communities` (method, `readmenator/_analyzer.py:213`) `def _finalize_communities(self, labels, adjacency)` - Group labels, fold tiny groups, drop undersized ones, renumber by size.
- `_louvain` (method, `readmenator/_analyzer.py:233`) `def _louvain(self, file_ids, adjacency)` - Partition files by greedy modularity optimisation (Louvain method).
- `partition` (method, `readmenator/_analyzer.py:268`) `def partition(self, ids, adjacency)` - Partition an arbitrary undirected id graph with deterministic Louvain.
- `_louvain_pass` (method, `readmenator/_analyzer.py:282`) `def _louvain_pass(self, graph, resolution, epsilon)` - Run Louvain local moves on one level and return a compact partition.
- `_aggregate` (method, `readmenator/_analyzer.py:322`) `def _aggregate(graph, partition)` - Collapse each community into one weighted super node.
- `_merge_small_communities` (method, `readmenator/_analyzer.py:334`) `def _merge_small_communities(self, groups, adjacency, weights)` - Fold communities smaller than COMMUNITY_MERGE_BELOW into their best neighbor.
- `_vote_weights` (method, `readmenator/_analyzer.py:381`) `def _vote_weights(self, file_ids, adjacency)` - Return each node's label-propagation vote weight.
- `_label_communities` (method, `readmenator/_analyzer.py:398`) `def _label_communities(self, nodes, communities)` - Generate human-readable labels for communities.
- `_core_file` (method, `readmenator/_analyzer.py:426`) `def _core_file(members, node_map)` - Return the stem of a community's most symbol-rich non-test file.
- `_build_community_map` (method, `readmenator/_analyzer.py:441`) `def _build_community_map(self, communities)` - Build a reverse map from file ID to community ID.
- `_compute_cohesion` (method, `readmenator/_analyzer.py:451`) `def _compute_cohesion(self, communities, adjacency)` - Compute cohesion score for each community.
- `_find_surprising_connections` (method, `readmenator/_analyzer.py:476`) `def _find_surprising_connections(self, nodes, adjacency, community_map)` - Find non-obvious cross-community bridges.
- `_shortest_path_communities` (method, `readmenator/_analyzer.py:516`) `def _shortest_path_communities(self, source, target, adjacency, community_map)` - Find the shortest path and communities traversed.
- `_suggest_questions` (method, `readmenator/_analyzer.py:543`) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, su` - Generate plain-language exploration questions from graph structure.
- `SecurityRule` (class, `readmenator/_security.py:24`) `class SecurityRule` - A single security detection rule loaded from YAML or built-in.
- `_parse_minimal_yaml` (function, `readmenator/_security.py:46`) `def _parse_minimal_yaml(text)` - Parse the simplified YAML format used by _security_rules.yml.
- `_unquote` (function, `readmenator/_security.py:121`) `def _unquote(s)`
- `_load_rules_from_yaml` (function, `readmenator/_security.py:128`) `def _load_rules_from_yaml(yaml_path)` - Load rule dicts from the YAML rules file, or return None on failure.
- `_compile` (function, `readmenator/_security.py:148`) `def _compile()`
- `_python_rules` (function, `readmenator/_security.py:153`) `def _python_rules()`
- `_javascript_rules` (function, `readmenator/_security.py:182`) `def _javascript_rules()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 8
- Cross-boundary resolved imports (EXTRACTED): 28

## Connections

- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_security.py.
- [EXTRACTED] depends_on community 5 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_analyzer.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 5 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analyzer.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_graphrag.py imports readmenator/_analyzer.py.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `tests/test_wiki.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _security changed?
- Should readmenator: _security be split, given cohesion 0.21?

## Sources

- `readmenator/_analyzer.py`
- `readmenator/_security.py`
- `readmenator/_wiki.py`
- `tests/test_analyzer.py`
- `tests/test_security.py`
- `tests/test_wiki.py`
