# readmenator/parsers

*Community 5 | 26 files | cohesion 0.56*

## Definition

This community groups 26 file(s) rooted at `readmenator/parsers` with dominant language py (cohesion 0.56). Central symbols: `AnalysisResult`, `AnalysisResultV2`, `AssemblyParser`, `CParser`, `CSharpParser`, `ChangeImpact`, `CommunityResult`, `DartParser`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Data model types for the readmenator knowledge graph.  Defines the core entity types -- Symbol, Node, Edge -- plus a utility function for pluralising symbol kin.

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
| `readmenator/parsers/_gdscript.py` | py | utility | 2 | yes |
| `readmenator/parsers/_go.py` | py | utility | 2 | yes |
| `readmenator/parsers/_java.py` | py | utility | 2 | yes |
| `readmenator/parsers/_javascript.py` | py | utility | 2 | yes |
| `readmenator/parsers/_kotlin.py` | py | utility | 2 | yes |
| `readmenator/parsers/_lua.py` | py | utility | 2 | yes |
| `readmenator/parsers/_nim.py` | py | utility | 2 | yes |
| `readmenator/parsers/_php.py` | py | utility | 2 | yes |

### `tests` (4 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_models.py` | py | testing | 11 | no |
| `tests/test_parsers.py` | py | testing | 87 | no |
| `tests/test_parsers_new.py` | py | testing | 36 | yes |
| `tests/test_parsers_property.py` | py | testing | 27 | yes |

### `readmenator` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_models.py` | py | business_logic | 20 | yes |

*... and 6 more files in this community.*


## Key Symbols

- `Symbol` (class, `readmenator/_models.py:18`) `class Symbol` - A single code symbol extracted from a source file.
- `Node` (class, `readmenator/_models.py:37`) `class Node` - A file node in the knowledge graph, containing its symbols.
- `Edge` (class, `readmenator/_models.py:58`) `class Edge` - A directed relationship between two nodes in the knowledge graph.
- `SecurityFinding` (class, `readmenator/_models.py:77`) `class SecurityFinding` - A security-relevant pattern detected in a source file.
- `pluralize_symbol_kind` (method, `readmenator/_models.py:101`) `def pluralize_symbol_kind(kind, plural_map)` - Return the plural form of *kind* according to *plural_map*.
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
- `DataflowIssue` (class, `readmenator/_models.py:307`) `class DataflowIssue` - A procedural intra-function dataflow finding.
- `LinterViolation` (class, `readmenator/_models.py:330`) `class LinterViolation` - A violation detected by the architecture linter.
- `DeadCodeReport` (class, `readmenator/_models.py:347`) `class DeadCodeReport` - A dead code symbol identified by the stripper.
- `RefactoringAction` (class, `readmenator/_models.py:364`) `class RefactoringAction` - A single refactoring action within a plan.
- `RefactoringPlan` (class, `readmenator/_models.py:385`) `class RefactoringPlan` - A complete refactoring plan for a monolithic file.
- `_init_parser_map` (function, `readmenator/parsers/__init__.py:34`) `def _init_parser_map()`
- `create_parser` (function, `readmenator/parsers/__init__.py:70`) `def create_parser(extension, filename, config)` - Factory: return a parser instance for the given file extension.
- `AssemblyParser` (class, `readmenator/parsers/_assembly.py:11`) `class AssemblyParser(LanguageParser)` - Parser for assembly (.asm, .s, .S).
- `_extract_specifics` (method, `readmenator/parsers/_assembly.py:19`) `def _extract_specifics(self, content)`
- `LanguageParser` (class, `readmenator/parsers/_base.py:12`) `class LanguageParser` - Base class for all language-specific parsers.
- `__init__` (method, `readmenator/parsers/_base.py:21`) `def __init__(self, filename, config)` - Initialise the parser with a file path and application config.
- `parse` (method, `readmenator/parsers/_base.py:36`) `def parse(self, content)` - Parse *content* and populate symbol/import lists.
- `_extract_specifics` (method, `readmenator/parsers/_base.py:45`) `def _extract_specifics(self, content)` - Subclass hook for language-specific symbol extraction.
- `_extract_docstring` (method, `readmenator/parsers/_base.py:49`) `def _extract_docstring(self, line_num)` - Walk backwards from *line_num* to collect preceding comments/docstrings.
- `_extract_signature` (method, `readmenator/parsers/_base.py:91`) `def _extract_signature(self, content, match_start, pattern)` - Extract a compact signature snippet starting at *match_start*.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 81
- Cross-boundary resolved imports (EXTRACTED): 76

## Connections

- [EXTRACTED] depends_on community 0 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 5 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_models.py imports readmenator/_category.py.
- [EXTRACTED] depends_on community 6 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_scanner.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 1 <-> 5 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_output.py imports readmenator/_models.py.

## Risks

- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_video.py` -> `readmenator/_models.py` via `subprocess` (1 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_models.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator/parsers changed?
- Should readmenator/parsers be split, given cohesion 0.56?

## Sources

- `readmenator/_models.py`
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
- `readmenator/parsers/_php.py`
- `readmenator/parsers/_python.py`
- `readmenator/parsers/_ruby.py`
- `readmenator/parsers/_rust.py`
- `readmenator/parsers/_scala.py`
- *... and 6 more*
