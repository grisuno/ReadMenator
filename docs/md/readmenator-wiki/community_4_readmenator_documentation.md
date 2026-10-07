# readmenator: _documentation

*Community 4 | 4 files | cohesion 0.23*

## Definition

This community groups 4 file(s) rooted at `readmenator` with dominant language py (cohesion 0.23). Central symbols: `DocumentationGenerator`, `MermaidRenderer`, `TestDocumentationGeneratorContract`, `TestMermaidRendererContract`, `__init__`, `_apply_context_budget`, `_build_architecture_reference`, `_build_change_impact`. Core file: `tests/test_documentation.py` (29 symbols). Documented purpose: KNOWLEDGE_BASE.md generator: the human-facing architecture reference.  Renders the dashboard, layers, communities, CPG, taint, hotspots, cycles, security audit,.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_documentation.py` | py | utility | 28 | yes |
| `readmenator/_mermaid.py` | py | utility | 4 | yes |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_mermaid.py` | py | testing | 11 | no |

## Key Symbols

- `DocumentationGenerator` (class, `readmenator/_documentation.py:33`) `class DocumentationGenerator` - Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.
- `__init__` (method, `readmenator/_documentation.py:45`) `def __init__(self, config)`
- `_ranking_version` (method, `readmenator/_documentation.py:63`) `def _ranking_version(self)`
- `_get_git_commit` (method, `readmenator/_documentation.py:81`) `def _get_git_commit()`
- `generate` (method, `readmenator/_documentation.py:91`) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, ana`
- `_apply_context_budget` (method, `readmenator/_documentation.py:178`) `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis,`
- `_build_toc` (method, `readmenator/_documentation.py:316`) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncate`
- `_build_layers` (method, `readmenator/_documentation.py:404`) `def _build_layers(self, layers, nodes)`
- `_build_dashboard` (method, `readmenator/_documentation.py:438`) `def _build_dashboard(self, nodes, edges, resolved_edges)`
- `_build_god_nodes` (method, `readmenator/_documentation.py:518`) `def _build_god_nodes(self, analysis, ranked)`
- `_build_community_analysis` (method, `readmenator/_documentation.py:546`) `def _build_community_analysis(self, analysis, nodes)`
- `_build_surprising_connections` (method, `readmenator/_documentation.py:579`) `def _build_surprising_connections(self, analysis, nodes)`
- `_build_suggested_questions` (method, `readmenator/_documentation.py:604`) `def _build_suggested_questions(self, analysis)`
- `_build_ranked_context` (method, `readmenator/_documentation.py:620`) `def _build_ranked_context(self, ranked)`
- `_build_orphans` (method, `readmenator/_documentation.py:666`) `def _build_orphans(self, nodes, analysis_v2, ranked)` - Build a section listing nodes with low coverage signals.
- `_build_query_recipes` (method, `readmenator/_documentation.py:716`) `def _build_query_recipes(self)`
- `_build_taint_analysis` (method, `readmenator/_documentation.py:758`) `def _build_taint_analysis(self, analysis_v2)`
- `_build_hotspots` (method, `readmenator/_documentation.py:793`) `def _build_hotspots(self, analysis_v2, ranked)`
- `_build_dataflow_analysis` (method, `readmenator/_documentation.py:831`) `def _build_dataflow_analysis(self, analysis_v2)` - Build the procedural dataflow findings section.
- `_build_dependency_cycles` (method, `readmenator/_documentation.py:862`) `def _build_dependency_cycles(self, analysis_v2)`
- `_build_change_impact` (method, `readmenator/_documentation.py:883`) `def _build_change_impact(self, analysis_v2)`
- `_build_layer_violations` (method, `readmenator/_documentation.py:908`) `def _build_layer_violations(self, analysis_v2)`
- `_build_suggested_rules` (method, `readmenator/_documentation.py:936`) `def _build_suggested_rules(self, analysis_v2)`
- `_build_security_findings` (method, `readmenator/_documentation.py:961`) `def _build_security_findings(self, findings)`
- `_build_mermaid_section` (method, `readmenator/_documentation.py:1008`) `def _build_mermaid_section(self, graph_output, is_truncated)`
- `_build_uml_diagram` (method, `readmenator/_documentation.py:1031`) `def _build_uml_diagram(self, nodes, edges)`
- `_build_cpg_block` (method, `readmenator/_documentation.py:1057`) `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
- `_build_architecture_reference` (method, `readmenator/_documentation.py:1083`) `def _build_architecture_reference(self, nodes, edges)`
- `MermaidRenderer` (class, `readmenator/_mermaid.py:17`) `class MermaidRenderer` - Renders a knowledge graph to Mermaid JS flowchart syntax.
- `__init__` (method, `readmenator/_mermaid.py:26`) `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, f`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 3
- Cross-boundary resolved imports (EXTRACTED): 14

## Connections

- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_rank.py.

## Risks

- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_documentation.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_documentation.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _documentation changed?
- Should readmenator: _documentation be split, given cohesion 0.23?

## Sources

- `readmenator/_documentation.py`
- `readmenator/_mermaid.py`
- `tests/test_documentation.py`
- `tests/test_mermaid.py`
