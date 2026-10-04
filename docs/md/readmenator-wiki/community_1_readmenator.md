# readmenator

*Community 1 | 7 files | cohesion 0.46*

## Definition

This community groups 7 file(s) rooted at `readmenator` with dominant language py (cohesion 0.46). Central symbols: `Category`, `CompositeRanker`, `DocProjection`, `EdgeKind`, `IdentityProjection`, `Morphism`, `Projection`, `QueryEngine`. Core file: `tests/test_ranking.py` (72 symbols). Documented purpose: Category theory model for the readmenator code graph.  Defines typed morphisms (edges with semantic kind), objects (file nodes), and a Category class for algebr.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_category.py` | py | utility | 26 | yes |
| `readmenator/_explain.py` | py | utility | 3 | yes |
| `readmenator/_projections.py` | py | utility | 15 | yes |
| `readmenator/_query.py` | py | data_access | 17 | yes |
| `readmenator/_rank.py` | py | utility | 17 | yes |
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
- `dfs` (method, `readmenator/_category.py:139`) `def dfs(current, goal, path, depth)`
- `_compose_kind` (method, `readmenator/_category.py:157`) `def _compose_kind(a, b)` - Determine the composite edge kind.
- `TypedGraph` (class, `readmenator/_category.py:181`) `class TypedGraph` - Weighted directed graph for PageRank computations.
- `__init__` (method, `readmenator/_category.py:188`) `def __init__(self, category)`
- `_compute_out_weights` (method, `readmenator/_category.py:197`) `def _compute_out_weights(self)`
- `nodes` (method, `readmenator/_category.py:203`) `def nodes(self)`
- `size` (method, `readmenator/_category.py:207`) `def size(self)`
- `node_index` (method, `readmenator/_category.py:210`) `def node_index(self, node_id)`
- `transition_weight` (method, `readmenator/_category.py:213`) `def transition_weight(self, source, target)` - Sum of weights of all morphisms from source to target.
- `stochastic_row` (method, `readmenator/_category.py:221`) `def stochastic_row(self, source)` - Return dict of target -> probability for the row of *source*.
- `build_category_from_edges` (method, `readmenator/_category.py:236`) `def build_category_from_edges(edges, resolved_edges, node_ids)` - Build a Category from lists of Edge objects.
- `_infer_edge_kind` (method, `readmenator/_category.py:280`) `def _infer_edge_kind(relation)` - Map a relation string to an EdgeKind.
- `explain_rank` (function, `readmenator/_explain.py:16`) `def explain_rank(node_id, ranked, category)` - Return a detailed breakdown of why *node_id* has its rank.
- `rank_summary` (function, `readmenator/_explain.py:140`) `def rank_summary(ranked, top_n)` - Return a short summary of the top-N ranked results.
- `_find_item` (function, `readmenator/_explain.py:163`) `def _find_item(node_id, items)`
- `Projection` (class, `readmenator/_projections.py:17`) `class Projection(Protocol)` - A functor from C_code to another category.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 11
- Cross-boundary resolved imports (EXTRACTED): 14

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_category.py.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_category.py reaches tests/test_resolver.py in 4 hops.
- [INFERRED] bridges community 1 <-> 2 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches readmenator/parsers/__init__.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches tests/test_cache.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_explain.py reaches tests/test_config.py in 4 hops.
- [INFERRED] shares_context community 1 <-> 3 (strength 0.5): Inferred shared context (layer utility) with no import path between community 1 (readmenator) and community 3 (orphans).

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_rank.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_query.py` via `subprocess` (4 hops)
- [cycle] `readmenator/_models.py` -> `readmenator/_category.py` -> `readmenator/_models.py`

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `tests/test_query.py`)? What purpose do they serve?
- Can the cycle `readmenator/_models.py` -> `readmenator/_category.py` be broken with an interface?
- What would break if the most connected file in readmenator changed?
- Should readmenator be split, given cohesion 0.46?

## Sources

- `readmenator/_category.py`
- `readmenator/_explain.py`
- `readmenator/_projections.py`
- `readmenator/_query.py`
- `readmenator/_rank.py`
- `tests/test_query.py`
- `tests/test_ranking.py`
