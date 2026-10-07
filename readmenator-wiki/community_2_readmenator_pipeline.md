# readmenator: _pipeline

*Community 2 | 19 files | cohesion 0.40*

## Definition

This community groups 19 file(s) rooted at `readmenator` with dominant language py (cohesion 0.40). Central symbols: `AgentInjector`, `AnalyzerFactory`, `Category`, `CodePropertyGraph`, `CompositeRanker`, `DeepAnalysisRunner`, `DocProjection`, `DocumentationGenerator`. Core file: `tests/test_ranking.py` (72 symbols). Documented purpose: ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApp.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `readmenator/_category.py` | py | utility | 26 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_documentation.py` | py | utility | 28 | yes |
| `readmenator/_explain.py` | py | utility | 3 | yes |
| `readmenator/_pipeline.py` | py | utility | 34 | yes |
| `readmenator/_projections.py` | py | utility | 15 | yes |
| `readmenator/_query.py` | py | data_access | 17 | yes |
| `readmenator/_rank.py` | py | utility | 17 | yes |
| `readmenator/_readme_injector.py` | py | infrastructure | 8 | yes |
| `readmenator/_sarif.py` | py | utility | 5 | yes |
| `readmenator/_uml.py` | py | utility | 25 | yes |
| `tests/test_agent_injector.py` | py | testing | 38 | yes |
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_query.py` | py | testing | 18 | no |
| `tests/test_ranking.py` | py | testing | 72 | yes |
| `tests/test_readme_injector.py` | py | testing | 26 | yes |
| `tests/test_sarif.py` | py | testing | 10 | no |

## Key Symbols

- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:101`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:123`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:134`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:148`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:166`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:179`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:183`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:197`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:235`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:244`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:254`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:270`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:282`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:287`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
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

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 34
- Cross-boundary resolved imports (EXTRACTED): 49

## Connections

- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_app.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_output.py.
- [INFERRED] bridges community 3 <-> 2 (strength 0.6): Inferred cross-community bridge: readmenator/__main__.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_readme_injector.py in 5 hops.
- [INFERRED] bridges community 2 <-> 4 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] bridges community 2 <-> 4 (strength 0.5): Inferred cross-community bridge: tests/test_readme_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (readmenator: _pipeline) and community 5 (orphans).

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_diagrams.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_category.py` via `subprocess` (2 hops)

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `tests/test_agent_output.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _pipeline changed?
- Should readmenator: _pipeline be split, given cohesion 0.40?

## Sources

- `readmenator/__init__.py`
- `readmenator/_agent_injector.py`
- `readmenator/_category.py`
- `readmenator/_cpg.py`
- `readmenator/_documentation.py`
- `readmenator/_explain.py`
- `readmenator/_pipeline.py`
- `readmenator/_projections.py`
- `readmenator/_query.py`
- `readmenator/_rank.py`
- `readmenator/_readme_injector.py`
- `readmenator/_sarif.py`
- `readmenator/_uml.py`
- `tests/test_agent_injector.py`
- `tests/test_agent_output.py`
- `tests/test_query.py`
- `tests/test_ranking.py`
- `tests/test_readme_injector.py`
- `tests/test_sarif.py`
