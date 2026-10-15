# readmenator/parsers

*Community 1 | 35 files | cohesion 0.52*

## Definition

This community groups 35 file(s) rooted at `readmenator/parsers` with dominant language py (cohesion 0.52). Central symbols: `AnalysisResult`, `AnalysisResultV2`, `AssemblyParser`, `CParser`, `CSharpParser`, `ChangeImpact`, `CommunityResult`, `ConceptGraph`. Core file: `tests/test_parsers_property.py` (27 symbols). Documented purpose: Mermaid graph renderer with intelligent pruning.  Converts the internal Node/Edge graph into a Mermaid flowchart (string) suitable for embedding in Markdown. Ha.

## Files

### `readmenator/parsers` (21 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/parsers/__init__.py` | py | utility | 2 | yes |
| `readmenator/parsers/_assembly.py` | py | utility | 2 | yes |
| `readmenator/parsers/_base.py` | py | utility | 6 | yes |
| `readmenator/parsers/_c.py` | py | utility | 3 | yes |
| `readmenator/parsers/_csharp.py` | py | utility | 2 | yes |
| `readmenator/parsers/_dart.py` | py | utility | 2 | yes |
| `readmenator/parsers/_elixir.py` | py | utility | 2 | yes |

### `tests` (8 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_mermaid.py` | py | testing | 13 | no |
| `tests/test_models.py` | py | testing | 11 | no |
| `tests/test_parsers_property.py` | py | testing | 27 | yes |
| `tests/test_rule_gen.py` | py | testing | 10 | no |
| `tests/test_sarif.py` | py | testing | 10 | no |
| `tests/test_scanner.py` | py | testing | 21 | no |
| `tests/test_taint.py` | py | testing | 10 | no |

### `readmenator` (6 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_mermaid.py` | py | utility | 4 | yes |
| `readmenator/_models.py` | py | business_logic | 23 | yes |
| `readmenator/_rule_gen.py` | py | business_logic | 9 | yes |
| `readmenator/_sarif.py` | py | utility | 5 | yes |
| `readmenator/_scanner.py` | py | utility | 14 | yes |
| `readmenator/_taint.py` | py | utility | 6 | yes |

*... and 15 more files in this community.*


## Key Symbols

- `MermaidRenderer` (class, `readmenator/_mermaid.py:17`) `class MermaidRenderer` - Renders a knowledge graph to Mermaid JS flowchart syntax.
- `__init__` (method, `readmenator/_mermaid.py:26`) `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, f` - Initialise rendering budgets and styles.
- `_sanitize_id` (method, `readmenator/_mermaid.py:75`) `def _sanitize_id(node_id)` - Convert *node_id* to a Mermaid-safe identifier.
- `render` (method, `readmenator/_mermaid.py:86`) `def render(self, nodes, edges, resolved_edges, analysis)` - Produce a Mermaid flowchart string and a truncation flag.
- `Symbol` (class, `readmenator/_models.py:18`) `class Symbol` - A single code symbol extracted from a source file.
- `Node` (class, `readmenator/_models.py:37`) `class Node` - A file node in the knowledge graph, containing its symbols.
- `Edge` (class, `readmenator/_models.py:58`) `class Edge` - A directed relationship between two nodes in the knowledge graph.
- `SecurityFinding` (class, `readmenator/_models.py:77`) `class SecurityFinding` - A security-relevant pattern detected in a source file.
- `pluralize_symbol_kind` (function, `readmenator/_models.py:101`) `def pluralize_symbol_kind(kind, plural_map)` - Return the plural form of *kind* according to *plural_map*.
- `CommunityResult` (class, `readmenator/_models.py:111`) `class CommunityResult` - Result of community detection on the import graph.
- `AnalysisResult` (class, `readmenator/_models.py:130`) `class AnalysisResult` - Complete graph analysis output.
- `TaintPath` (class, `readmenator/_models.py:151`) `class TaintPath` - A taint propagation path from source to sink through the import graph.
- `TaintAnalysisResult` (class, `readmenator/_models.py:172`) `class TaintAnalysisResult` - Complete taint propagation analysis output.
- `DependencyCycle` (class, `readmenator/_models.py:187`) `class DependencyCycle` - A cycle detected in the resolved import graph.
- `ChangeImpact` (class, `readmenator/_models.py:200`) `class ChangeImpact` - Change impact analysis for a single file.
- `HotspotResult` (class, `readmenator/_models.py:217`) `class HotspotResult` - A hotspot file combining complexity and centrality metrics.
- `SuggestedRule` (class, `readmenator/_models.py:238`) `class SuggestedRule` - A suggested linting/security rule derived from code patterns.
- `LayerViolation` (class, `readmenator/_models.py:263`) `class LayerViolation` - A detected architectural layer violation.
- `AnalysisResultV2` (class, `readmenator/_models.py:284`) `class AnalysisResultV2` - Extended analysis result combining all new analysis modules.
- `DataflowIssue` (class, `readmenator/_models.py:309`) `class DataflowIssue` - A procedural intra-function dataflow finding.
- `LinterViolation` (class, `readmenator/_models.py:332`) `class LinterViolation` - A violation detected by the architecture linter.
- `DeadCodeReport` (class, `readmenator/_models.py:349`) `class DeadCodeReport` - A dead code symbol identified by the stripper.
- `RefactoringAction` (class, `readmenator/_models.py:366`) `class RefactoringAction` - A single refactoring action within a plan.
- `RefactoringPlan` (class, `readmenator/_models.py:387`) `class RefactoringPlan` - A complete refactoring plan for a monolithic file.
- `ConceptNode` (class, `readmenator/_models.py:404`) `class ConceptNode` - A semantic noun node in the concept graph.
- `ConceptRelation` (class, `readmenator/_models.py:421`) `class ConceptRelation` - A verb edge between two concept noun nodes.
- `ConceptGraph` (class, `readmenator/_models.py:442`) `class ConceptGraph` - Deterministic semantic layer over the structural graph.
- `RuleGenerator` (class, `readmenator/_rule_gen.py:14`) `class RuleGenerator` - Generates suggested linting and security rules from code patterns.
- `__init__` (method, `readmenator/_rule_gen.py:90`) `def __init__(self, config)`
- `generate` (method, `readmenator/_rule_gen.py:94`) `def generate(self, nodes, content_map)` - Generate suggested rules by scanning code patterns.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 98
- Cross-boundary resolved imports (EXTRACTED): 102

## Connections

- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 6 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 5 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_diagrams.py imports readmenator/_models.py.

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `tests/test_mermaid.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator/parsers changed?
- Should readmenator/parsers be split, given cohesion 0.52?

## Sources

- `readmenator/_mermaid.py`
- `readmenator/_models.py`
- `readmenator/_rule_gen.py`
- `readmenator/_sarif.py`
- `readmenator/_scanner.py`
- `readmenator/_taint.py`
- `readmenator/parsers/__init__.py`
- `readmenator/parsers/_assembly.py`
- `readmenator/parsers/_base.py`
- `readmenator/parsers/_c.py`
- `readmenator/parsers/_csharp.py`
- `readmenator/parsers/_dart.py`
- `readmenator/parsers/_elixir.py`
- `readmenator/parsers/_gdscript.py`
- `readmenator/parsers/_go.py`
- `readmenator/parsers/_java.py`
- `readmenator/parsers/_javascript.py`
- `readmenator/parsers/_kotlin.py`
- `readmenator/parsers/_lua.py`
- `readmenator/parsers/_nim.py`
- *... and 15 more*
