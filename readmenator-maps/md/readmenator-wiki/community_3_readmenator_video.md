# readmenator: _video

*Community 3 | 14 files | cohesion 0.30*

## Definition

This community groups 14 file(s) rooted at `readmenator` with dominant language py (cohesion 0.30). Central symbols: `Backdrop`, `Bm25Index`, `Category`, `CinematicVideoRenderer`, `CompositeRanker`, `ConceptExtractor`, `DocProjection`, `EdgeKind`. Core file: `readmenator/_video.py` (90 symbols). Documented purpose: ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApp.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/_category.py` | py | utility | 26 | yes |
| `readmenator/_concepts.py` | py | utility | 8 | yes |
| `readmenator/_explain.py` | py | utility | 3 | yes |
| `readmenator/_graphrag.py` | py | utility | 53 | yes |
| `readmenator/_projections.py` | py | utility | 15 | yes |
| `readmenator/_query.py` | py | data_access | 17 | yes |
| `readmenator/_rank.py` | py | utility | 18 | yes |
| `readmenator/_video.py` | py | utility | 90 | yes |
| `tests/test_concepts.py` | py | testing | 8 | no |
| `tests/test_graphrag.py` | py | testing | 28 | yes |
| `tests/test_query.py` | py | testing | 18 | no |
| `tests/test_ranking.py` | py | testing | 72 | yes |
| `tests/test_video.py` | py | testing | 20 | yes |

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
- `verb_for_relation` (function, `readmenator/_concepts.py:33`) `def verb_for_relation(relation)` - Return the verb label for a structural edge relation.
- `ConceptExtractor` (class, `readmenator/_concepts.py:38`) `class ConceptExtractor` - Builds a ConceptGraph from scanned nodes and structural edges.
- `__init__` (method, `readmenator/_concepts.py:41`) `def __init__(self, config)` - Store configuration for concept extraction budgets.
- `extract` (method, `readmenator/_concepts.py:47`) `def extract(self, nodes, edges, resolved_edges)` - Build concepts and verb relations from structural topology.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 20
- Cross-boundary resolved imports (EXTRACTED): 47

## Connections

- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_app.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_symindex.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_readme_injector.py.
- [EXTRACTED] depends_on community 3 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_graphrag.py imports readmenator/_analyzer.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_concepts.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _video changed?
- Should readmenator: _video be split, given cohesion 0.30?

## Sources

- `readmenator/__init__.py`
- `readmenator/_category.py`
- `readmenator/_concepts.py`
- `readmenator/_explain.py`
- `readmenator/_graphrag.py`
- `readmenator/_projections.py`
- `readmenator/_query.py`
- `readmenator/_rank.py`
- `readmenator/_video.py`
- `tests/test_concepts.py`
- `tests/test_graphrag.py`
- `tests/test_query.py`
- `tests/test_ranking.py`
- `tests/test_video.py`
