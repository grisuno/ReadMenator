# readmenator

*Community 0 | 93 files | cohesion 0.99*

## Definition

This community groups 93 file(s) rooted at `readmenator` with dominant language py (cohesion 0.99). Central symbols: `AgentOutputGenerator`, `AnalysisResult`, `AnalysisResultV2`, `AnalyzerFactory`, `ArchitectureLinter`, `AssemblyParser`, `CParser`, `CSharpParser`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApp.

## Files

### `readmenator` (38 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/__init__.py` | py | utility | 0 | yes |
| `readmenator/__main__.py` | py | testing | 3 | no |
| `readmenator/_agent_output.py` | py | utility | 18 | yes |
| `readmenator/_analyzer.py` | py | utility | 14 | yes |
| `readmenator/_app.py` | py | utility | 44 | no |
| `readmenator/_cache.py` | py | infrastructure | 13 | yes |
| `readmenator/_category.py` | py | utility | 26 | yes |

### `tests` (34 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_analyzer.py` | py | testing | 14 | yes |
| `tests/test_cache.py` | py | testing | 22 | yes |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_cursorrules.py` | py | testing | 12 | yes |
| `tests/test_dataflow.py` | py | testing | 47 | no |

### `readmenator/parsers` (21 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/parsers/__init__.py` | py | utility | 2 | no |
| `readmenator/parsers/_assembly.py` | py | utility | 2 | no |
| `readmenator/parsers/_base.py` | py | utility | 6 | no |
| `readmenator/parsers/_c.py` | py | utility | 3 | no |
| `readmenator/parsers/_csharp.py` | py | utility | 2 | no |
| `readmenator/parsers/_dart.py` | py | utility | 2 | no |

*... and 73 more files in this community.*


## Key Symbols

- `build_parser` (function, `readmenator/__main__.py:16`) `def build_parser()`
- `_run_tests` (function, `readmenator/__main__.py:107`) `def _run_tests()`
- `main` (function, `readmenator/__main__.py:122`) `def main()`
- `AgentOutputGenerator` (class, `readmenator/_agent_output.py:47`) `class AgentOutputGenerator` - Generates agent-friendly, grep-optimised output files.
- `__init__` (method, `readmenator/_agent_output.py:54`) `def __init__(self, config)`
- `generate` (method, `readmenator/_agent_output.py:61`) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings` - Write all agent output files and return the output directory path.
- `_infer_subsystems` (method, `readmenator/_agent_output.py:116`) `def _infer_subsystems(self, nodes)` - Group nodes by directory, inferring subsystem names.
- `_build_index` (method, `readmenator/_agent_output.py:153`) `def _build_index(self, nodes, subsystems)`
- `_build_architecture` (method, `readmenator/_agent_output.py:183`) `def _build_architecture(self, edges, resolved_edges, nodes)`
- `_build_security` (method, `readmenator/_agent_output.py:227`) `def _build_security(self, findings, nodes)`
- `_enclosing_symbol` (method, `readmenator/_agent_output.py:257`) `def _enclosing_symbol(nodes, file_path, line)` - Return the nearest symbol defined at or before line in file_path.
- `_build_api` (method, `readmenator/_agent_output.py:276`) `def _build_api(self, nodes, resolved_map, imported_by)`
- `_build_manifest` (method, `readmenator/_agent_output.py:331`) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root)` - Build MANIFEST.json with freshness + entry points for agents.
- `_build_symbols` (method, `readmenator/_agent_output.py:370`) `def _build_symbols(self, nodes)` - Build grep-friendly symbol index (one line per symbol).
- `_build_gotchas` (method, `readmenator/_agent_output.py:387`) `def _build_gotchas(self, analysis, analysis_v2, nodes)`
- `_write_subsystem_files` (method, `readmenator/_agent_output.py:469`) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by,`
- `_build_subsystem_content` (method, `readmenator/_agent_output.py:488`) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by,`
- `_write_recipes` (method, `readmenator/_agent_output.py:538`) `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings)`
- `_build_resolved_map` (method, `readmenator/_agent_output.py:637`) `def _build_resolved_map(resolved_edges)`
- `_build_imported_by_map` (method, `readmenator/_agent_output.py:646`) `def _build_imported_by_map(resolved_edges)`
- `_write` (method, `readmenator/_agent_output.py:655`) `def _write(path, content)`
- `dominant_directory` (function, `readmenator/_analyzer.py:21`) `def dominant_directory(file_ids)` - Return the most informative directory label for a set of files.
- `GraphAnalyzer` (class, `readmenator/_analyzer.py:39`) `class GraphAnalyzer` - Deterministic graph analysis over scanned nodes and edges.
- `__init__` (method, `readmenator/_analyzer.py:47`) `def __init__(self, config)` - Initialise with application configuration.
- `analyze` (method, `readmenator/_analyzer.py:55`) `def analyze(self, nodes, edges, resolved_edges)` - Run the full analysis pipeline and return structured results.
- `_build_adjacency` (method, `readmenator/_analyzer.py:108`) `def _build_adjacency(self, nodes, edges)` - Build an undirected adjacency map from import edges.
- `_build_reverse_adjacency` (method, `readmenator/_analyzer.py:122`) `def _build_reverse_adjacency(self, adjacency)` - Build a directed reverse adjacency (incoming edges) map.
- `_compute_god_nodes` (method, `readmenator/_analyzer.py:132`) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` - Compute the most central nodes using combined degree centrality.
- `_detect_communities` (method, `readmenator/_analyzer.py:154`) `def _detect_communities(self, nodes, adjacency)` - Detect communities using label propagation.
- `_label_communities` (method, `readmenator/_analyzer.py:209`) `def _label_communities(self, nodes, communities)` - Generate human-readable labels for communities.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 307
- Cross-boundary resolved imports (EXTRACTED): 4

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/__init__.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.6): Inferred cross-community bridge: readmenator/_agent_injector.py reaches tests/test_resolver.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/_cache.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: readmenator/_cursorrules_generator.py reaches tests/test_agent_injector.py in 4 hops.
- [INFERRED] bridges community 1 <-> 0 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_resolver.py in 5 hops.
- [INFERRED] shares_context community 0 <-> 2 (strength 0.5): Inferred shared context (layer utility) with no import path between community 0 (readmenator) and community 2 (orphans).

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/__main__.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_app.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_config.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_mcp_server.py` via `subprocess` (3 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_cursorrules_generator.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_models.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_layers.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_diagrams.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_pipeline.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_query.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_resolver.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_rank.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_watcher.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_refactorizer.py` via `subprocess` (4 hops)
- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_dead_code.py` via `subprocess` (4 hops)

## Open Questions

- Why do 50 file(s) lack file-level docs (e.g. `readmenator/__main__.py`)? What purpose do they serve?
- Can the cycle `readmenator/_app.py` -> `readmenator/_pipeline.py` -> `readmenator/_agent_injector.py` -> `readmenator.py` -> `readmenator/__main__.py` -> `readmenator/_mcp_server.py` be broken with an interface?
- What would break if the most connected file in readmenator changed?
- Should readmenator be split, given cohesion 0.99?

## Sources

- `readmenator/__init__.py`
- `readmenator/__main__.py`
- `readmenator/_agent_output.py`
- `readmenator/_analyzer.py`
- `readmenator/_app.py`
- `readmenator/_cache.py`
- `readmenator/_category.py`
- `readmenator/_config.py`
- `readmenator/_cpg.py`
- `readmenator/_cursorrules_generator.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_diagrams.py`
- `readmenator/_documentation.py`
- `readmenator/_explain.py`
- `readmenator/_exporter.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_layers.py`
- `readmenator/_linter.py`
- *... and 73 more*
