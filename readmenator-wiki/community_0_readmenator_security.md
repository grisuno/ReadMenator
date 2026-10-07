# readmenator: _security

*Community 0 | 29 files | cohesion 0.34*

## Definition

This community groups 29 file(s) rooted at `tests` with dominant language py (cohesion 0.34). Central symbols: `ConceptExtractor`, `Config`, `DataflowAnalyzer`, `DeadCodeStripper`, `GraphAnalyzer`, `GraphExporter`, `HotspotAnalyzer`, `LayerRuleEngine`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Graph analysis engine for the readmenator knowledge graph.  Provides community detection (Louvain-like greedy modularity), god node identification (degree/PageR.

## Files

### `tests` (17 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_concepts.py` | py | testing | 8 | no |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_hotspots.py` | py | testing | 11 | no |
| `tests/test_layer_rules.py` | py | testing | 13 | no |

### `readmenator` (12 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analyzer.py` | py | utility | 22 | yes |
| `readmenator/_concepts.py` | py | utility | 8 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_exporter.py` | py | utility | 15 | yes |
| `readmenator/_hotspots.py` | py | utility | 7 | yes |
| `readmenator/_layer_rules.py` | py | business_logic | 4 | yes |
| `readmenator/_refactorizer.py` | py | utility | 9 | yes |
| `readmenator/_rule_gen.py` | py | business_logic | 9 | yes |

*... and 9 more files in this community.*


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
- `_louvain_pass` (method, `readmenator/_analyzer.py:268`) `def _louvain_pass(self, graph, resolution, epsilon)` - Run Louvain local moves on one level and return a compact partition.
- `_aggregate` (method, `readmenator/_analyzer.py:308`) `def _aggregate(graph, partition)` - Collapse each community into one weighted super node.
- `_merge_small_communities` (method, `readmenator/_analyzer.py:320`) `def _merge_small_communities(self, groups, adjacency, weights)` - Fold communities smaller than COMMUNITY_MERGE_BELOW into their best neighbor.
- `_vote_weights` (method, `readmenator/_analyzer.py:367`) `def _vote_weights(self, file_ids, adjacency)` - Return each node's label-propagation vote weight.
- `_label_communities` (method, `readmenator/_analyzer.py:384`) `def _label_communities(self, nodes, communities)` - Generate human-readable labels for communities.
- `_core_file` (method, `readmenator/_analyzer.py:412`) `def _core_file(members, node_map)` - Return the stem of a community's most symbol-rich non-test file.
- `_build_community_map` (method, `readmenator/_analyzer.py:427`) `def _build_community_map(self, communities)` - Build a reverse map from file ID to community ID.
- `_compute_cohesion` (method, `readmenator/_analyzer.py:437`) `def _compute_cohesion(self, communities, adjacency)` - Compute cohesion score for each community.
- `_find_surprising_connections` (method, `readmenator/_analyzer.py:462`) `def _find_surprising_connections(self, nodes, adjacency, community_map)` - Find non-obvious cross-community bridges.
- `_shortest_path_communities` (method, `readmenator/_analyzer.py:502`) `def _shortest_path_communities(self, source, target, adjacency, community_map)` - Find the shortest path and communities traversed.
- `_suggest_questions` (method, `readmenator/_analyzer.py:529`) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, su` - Generate plain-language exploration questions from graph structure.
- `verb_for_relation` (function, `readmenator/_concepts.py:33`) `def verb_for_relation(relation)` - Return the verb label for a structural edge relation.
- `ConceptExtractor` (class, `readmenator/_concepts.py:38`) `class ConceptExtractor` - Builds a ConceptGraph from scanned nodes and structural edges.
- `__init__` (method, `readmenator/_concepts.py:41`) `def __init__(self, config)` - Store configuration for concept extraction budgets.
- `extract` (method, `readmenator/_concepts.py:47`) `def extract(self, nodes, edges, resolved_edges)` - Build concepts and verb relations from structural topology.
- `_tokens_for_node` (method, `readmenator/_concepts.py:101`) `def _tokens_for_node(self, node)` - Return atomic noun tokens extracted from one file node.
- `_tokenize` (method, `readmenator/_concepts.py:115`) `def _tokenize(self, text)` - Split text atomically into normalised noun tokens.
- `_build_relations` (method, `readmenator/_concepts.py:130`) `def _build_relations(self, edges, file_to_concepts)` - Aggregate structural edges into concept verb relations.
- `_build_dialectic` (method, `readmenator/_concepts.py:169`) `def _build_dialectic(self, concepts, relations)` - Generate deterministic thesis/antithesis/synthesis prompts.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 44
- Cross-boundary resolved imports (EXTRACTED): 98

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__main__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analyzer.py imports readmenator/_models.py.
- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 0 (readmenator: _security) and community 5 (orphans).

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 10 file(s) lack file-level docs (e.g. `tests/test_concepts.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _security changed?
- Should readmenator: _security be split, given cohesion 0.34?

## Sources

- `readmenator/_analyzer.py`
- `readmenator/_concepts.py`
- `readmenator/_config.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_exporter.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_refactorizer.py`
- `readmenator/_rule_gen.py`
- `readmenator/_security.py`
- `readmenator/_wiki.py`
- `tests/test_analyzer.py`
- `tests/test_concepts.py`
- `tests/test_config.py`
- `tests/test_cpg.py`
- `tests/test_dataflow.py`
- `tests/test_dead_code.py`
- `tests/test_documentation.py`
- `tests/test_exporter.py`
- *... and 9 more*
