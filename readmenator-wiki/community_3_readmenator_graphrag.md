# readmenator: _graphrag

*Community 3 | 18 files | cohesion 0.32*

## Definition

This community groups 18 file(s) rooted at `readmenator` with dominant language py (cohesion 0.32). Central symbols: `Bm25Index`, `Category`, `ComponentDiagramBuilder`, `CompositeRanker`, `ConceptExtractor`, `DocProjection`, `EdgeKind`, `GraphRagBuilder`. Core file: `tests/test_ranking.py` (72 symbols). Documented purpose: ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApp.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/_category.py` | py | utility | 26 | yes |
| `readmenator/_components.py` | py | presentation | 25 | yes |
| `readmenator/_concepts.py` | py | utility | 8 | yes |
| `readmenator/_explain.py` | py | utility | 3 | yes |
| `readmenator/_graphrag.py` | py | utility | 53 | yes |
| `readmenator/_ollama.py` | py | utility | 7 | yes |
| `readmenator/_projections.py` | py | utility | 15 | yes |
| `readmenator/_query.py` | py | data_access | 17 | yes |
| `readmenator/_rank.py` | py | utility | 18 | yes |
| `readmenator/_skill_installer.py` | py | utility | 7 | yes |
| `tests/test_components.py` | py | testing | 36 | yes |
| `tests/test_concepts.py` | py | testing | 8 | no |
| `tests/test_graphrag.py` | py | testing | 28 | yes |
| `tests/test_memory.py` | py | testing | 17 | yes |
| `tests/test_ollama.py` | py | testing | 4 | yes |
| `tests/test_query.py` | py | testing | 18 | no |
| `tests/test_ranking.py` | py | testing | 72 | yes |

## Key Symbols

- `EdgeKind` (class, `readmenator/_category.py:24`) `class EdgeKind(str, Enum)` - Semantic type of a morphism between two code artifacts.
- `__str__` (method, `readmenator/_category.py:38`) `def __str__(self)`
- `Morphism` (class, `readmenator/_category.py:57`) `class Morphism` - A typed directed edge between two code artifacts.
- `weight` (method, `readmenator/_category.py:73`) `def weight(self)` - Effective weight for ranking = semantic weight * confidence.
- `Category` (class, `readmenator/_category.py:78`) `class Category` - A category of code artifacts with typed morphisms.
- `__init__` (method, `readmenator/_category.py:86`) `def __init__(self)`
- `add_object` (method, `readmenator/_category.py:92`) `def add_object(self, obj_id)`
- `add_morphism` (method, `readmenator/_category.py:95`) `def add_morphism(self, m)`
- `objects` (method, `readmenator/_category.py:103`) `def objects(self)`
- `morphisms` (method, `readmenator/_category.py:107`) `def morphisms(self)`
- `outgoing` (method, `readmenator/_category.py:110`) `def outgoing(self, obj_id)`
- `incoming` (method, `readmenator/_category.py:113`) `def incoming(self, obj_id)`
- `compose` (method, `readmenator/_category.py:116`) `def compose(self, a, b)` - Compose two morphisms if target of a matches source of b.
- `paths` (method, `readmenator/_category.py:133`) `def paths(self, source, target, max_depth)` - Find all composition paths from source to target up to max_depth.
- `dfs` (function, `readmenator/_category.py:139`) `def dfs(current, goal, path, depth)`
- `_compose_kind` (method, `readmenator/_category.py:157`) `def _compose_kind(a, b)` - Determine the composite edge kind.
- `TypedGraph` (class, `readmenator/_category.py:181`) `class TypedGraph` - Weighted directed graph for PageRank computations.
- `__init__` (method, `readmenator/_category.py:188`) `def __init__(self, category)`
- `_compute_out_weights` (method, `readmenator/_category.py:197`) `def _compute_out_weights(self)`
- `nodes` (method, `readmenator/_category.py:203`) `def nodes(self)`
- `size` (method, `readmenator/_category.py:207`) `def size(self)`
- `node_index` (method, `readmenator/_category.py:210`) `def node_index(self, node_id)`
- `transition_weight` (method, `readmenator/_category.py:213`) `def transition_weight(self, source, target)` - Sum of weights of all morphisms from source to target.
- `stochastic_row` (method, `readmenator/_category.py:221`) `def stochastic_row(self, source)` - Return dict of target -> probability for the row of *source*.
- `build_category_from_edges` (function, `readmenator/_category.py:236`) `def build_category_from_edges(edges, resolved_edges, node_ids)` - Build a Category from lists of Edge objects.
- `_infer_edge_kind` (function, `readmenator/_category.py:278`) `def _infer_edge_kind(relation)` - Map a relation string to an EdgeKind.
- `sanitize` (function, `readmenator/_components.py:45`) `def sanitize(name)` - Replace non-alphanumerics with underscores for Mermaid node ids.
- `ComponentDiagramBuilder` (class, `readmenator/_components.py:57`) `class ComponentDiagramBuilder` - Builds component-diagram analysis from readmenator topology.
- `__init__` (method, `readmenator/_components.py:60`) `def __init__(self, config)` - Initialise with application configuration.
- `build` (method, `readmenator/_components.py:70`) `def build(self, nodes, edges, resolved_edges, analysis, project_root, content_ma` - Build the full analysis document.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 26
- Cross-boundary resolved imports (EXTRACTED): 59

## Connections

- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_app.py.
- [EXTRACTED] depends_on community 3 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_project_config.py.
- [EXTRACTED] depends_on community 3 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_symindex.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_readme_injector.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/_components.py imports readmenator/_cache.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [layer strict] `tests/test_components.py` (testing) -> `readmenator/_components.py` (presentation)
- [layer strict] `tests/test_folder_readme.py` (testing) -> `readmenator/_components.py` (presentation)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_concepts.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _graphrag changed?
- Should readmenator: _graphrag be split, given cohesion 0.32?

## Sources

- `readmenator/__init__.py`
- `readmenator/_category.py`
- `readmenator/_components.py`
- `readmenator/_concepts.py`
- `readmenator/_explain.py`
- `readmenator/_graphrag.py`
- `readmenator/_ollama.py`
- `readmenator/_projections.py`
- `readmenator/_query.py`
- `readmenator/_rank.py`
- `readmenator/_skill_installer.py`
- `tests/test_components.py`
- `tests/test_concepts.py`
- `tests/test_graphrag.py`
- `tests/test_memory.py`
- `tests/test_ollama.py`
- `tests/test_query.py`
- `tests/test_ranking.py`
