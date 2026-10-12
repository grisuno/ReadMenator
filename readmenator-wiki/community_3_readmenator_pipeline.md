# readmenator: _pipeline

*Community 3 | 20 files | cohesion 0.28*

## Definition

This community groups 20 file(s) rooted at `readmenator` with dominant language py (cohesion 0.28). Central symbols: `AgentInjector`, `AnalyticsBuilder`, `AnalyzerFactory`, `CodePropertyGraph`, `DeepAnalysisRunner`, `DocumentationGenerator`, `Embedder`, `ExclusionEntry`. Core file: `tests/test_interactive_graph.py` (60 symbols). Documented purpose: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects common AI agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules, etc.) an.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_agent_injector.py` | py | infrastructure | 14 | yes |
| `readmenator/_analytics.py` | py | utility | 9 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_documentation.py` | py | utility | 31 | yes |
| `readmenator/_embed.py` | py | utility | 11 | yes |
| `readmenator/_exclusions.py` | py | utility | 11 | yes |
| `readmenator/_exporter.py` | py | utility | 16 | yes |
| `readmenator/_pipeline.py` | py | utility | 52 | yes |
| `readmenator/_provenance.py` | py | utility | 10 | yes |
| `readmenator/_readme_injector.py` | py | infrastructure | 9 | yes |
| `readmenator/_scantext.py` | py | utility | 4 | yes |
| `readmenator/_uml.py` | py | utility | 25 | yes |
| `tests/test_agent_injector.py` | py | testing | 38 | yes |
| `tests/test_agent_output.py` | py | testing | 45 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_interactive_graph.py` | py | testing | 60 | yes |
| `tests/test_readme_injector.py` | py | testing | 28 | yes |
| `tests/test_uml.py` | py | testing | 49 | yes |

## Key Symbols

- `ensure_readmenator_installed` (function, `readmenator/_agent_injector.py:107`) `def ensure_readmenator_installed()` - Check if readmenator is installed via pip; install it if missing.
- `AgentInjector` (class, `readmenator/_agent_injector.py:129`) `class AgentInjector` - Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.
- `__init__` (method, `readmenator/_agent_injector.py:140`) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki`
- `inject` (method, `readmenator/_agent_injector.py:154`) `def inject(self, project_root)` - Inject KB reference into all discovered agent files.
- `remove` (method, `readmenator/_agent_injector.py:172`) `def remove(self, project_root)` - Remove KB injection from all discovered agent files.
- `find_agent_files` (method, `readmenator/_agent_injector.py:185`) `def find_agent_files(self, project_root)` - Public accessor: return all detected agent files.
- `_find_agent_files` (method, `readmenator/_agent_injector.py:189`) `def _find_agent_files(self, root)`
- `_inject_single` (method, `readmenator/_agent_injector.py:203`) `def _inject_single(self, path)`
- `_extract_current_injection` (method, `readmenator/_agent_injector.py:241`) `def _extract_current_injection(content)`
- `_remove_old_injection` (method, `readmenator/_agent_injector.py:250`) `def _remove_old_injection(content)`
- `_remove_single` (method, `readmenator/_agent_injector.py:260`) `def _remove_single(self, path)`
- `_build_injection` (method, `readmenator/_agent_injector.py:276`) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (method, `readmenator/_agent_injector.py:288`) `def _build_mdc_injection(self)` - Build Cursor .mdc injection body (frontmatter added separately).
- `_prepend_mdc_frontmatter` (method, `readmenator/_agent_injector.py:293`) `def _prepend_mdc_frontmatter(content, injection)` - Prepend Cursor frontmatter so the rule is auto-attached.
- `AnalyticsBuilder` (class, `readmenator/_analytics.py:25`) `class AnalyticsBuilder` - Builds analytics payloads from scanned topology and findings.
- `__init__` (method, `readmenator/_analytics.py:28`) `def __init__(self, config)` - Initialise with application configuration.
- `build` (method, `readmenator/_analytics.py:36`) `def build(self, nodes, edges, resolved_edges, analysis, findings, layers, v2, ho` - Build the full analytics payload.
- `_layer_distribution` (method, `readmenator/_analytics.py:100`) `def _layer_distribution(self, nodes, layers)` - Count files per architectural layer.
- `_language_distribution` (method, `readmenator/_analytics.py:112`) `def _language_distribution(self, nodes)` - Count files per programming language.
- `_hotspot_ranking` (method, `readmenator/_analytics.py:120`) `def _hotspot_ranking(self, nodes, fan_in, fan_out, hotspots)` - Rank files by combined symbol and connectivity weight.
- `_rule_yield` (method, `readmenator/_analytics.py:152`) `def _rule_yield(self, findings)` - Count security findings per rule with severity breakdown.
- `_size_bands` (method, `readmenator/_analytics.py:164`) `def _size_bands(self, nodes)` - Bucket files by symbol-count bands.
- `_scatter` (method, `readmenator/_analytics.py:181`) `def _scatter(self, nodes, fan_in, fan_out, layers)` - Build a file scatter of symbols versus connectivity.
- `CodePropertyGraph` (class, `readmenator/_cpg.py:16`) `class CodePropertyGraph` - Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.
- `__init__` (method, `readmenator/_cpg.py:26`) `def __init__(self, privacy_mode, cpg_context)`
- `generate` (method, `readmenator/_cpg.py:30`) `def generate(self, nodes, edges, resolved_edges, analysis, findings)` - Generate the CPG JSON-LD string embeddable in markdown.
- `_severity_counts` (method, `readmenator/_cpg.py:147`) `def _severity_counts(self, findings)`
- `_build_symbol_list` (method, `readmenator/_cpg.py:153`) `def _build_symbol_list(self, node)`
- `_compute_node_hash` (method, `readmenator/_cpg.py:169`) `def _compute_node_hash(node)`
- `DocumentationGenerator` (class, `readmenator/_documentation.py:36`) `class DocumentationGenerator` - Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 32
- Cross-boundary resolved imports (EXTRACTED): 84

## Connections

- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_readme_injector.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_forcegraph.py.
- [EXTRACTED] depends_on community 3 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_flowcharts.py.
- [INFERRED] bridges community 2 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_agent_injector.py in 5 hops.
- [INFERRED] bridges community 2 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator.py reaches tests/test_readme_injector.py in 5 hops.
- [INFERRED] bridges community 3 <-> 4 (strength 0.5): Inferred cross-community bridge: tests/test_agent_injector.py reaches tests/test_graphlayout.py in 5 hops.

## Risks

- [taint high] `readmenator/_agent_injector.py` -> `readmenator/_agent_injector.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_flowcharts.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph_page.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_resolver.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_htmlpack.py` via `subprocess` (2 hops)

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `tests/test_agent_output.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_agent_injector.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _pipeline changed?
- Should readmenator: _pipeline be split, given cohesion 0.28?

## Sources

- `readmenator/_agent_injector.py`
- `readmenator/_analytics.py`
- `readmenator/_cpg.py`
- `readmenator/_documentation.py`
- `readmenator/_embed.py`
- `readmenator/_exclusions.py`
- `readmenator/_exporter.py`
- `readmenator/_pipeline.py`
- `readmenator/_provenance.py`
- `readmenator/_readme_injector.py`
- `readmenator/_scantext.py`
- `readmenator/_uml.py`
- `tests/test_agent_injector.py`
- `tests/test_agent_output.py`
- `tests/test_cpg.py`
- `tests/test_documentation.py`
- `tests/test_exporter.py`
- `tests/test_interactive_graph.py`
- `tests/test_readme_injector.py`
- `tests/test_uml.py`
