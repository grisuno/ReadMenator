# readmenator: _pipeline

*Community 0 | 37 files | cohesion 0.45*

## Definition

This community groups 37 file(s) rooted at `readmenator` with dominant language py (cohesion 0.45). Central symbols: `AnalyticsBuilder`, `AnalyzerFactory`, `CodePropertyGraph`, `ConceptExtractor`, `Config`, `DataflowAnalyzer`, `DeadCodeStripper`, `DeepAnalysisRunner`. Core file: `tests/test_parsers.py` (87 symbols). Documented purpose: Corpus analytics aggregations for the readmenator knowledge graph.  Computes the explorer dashboard payloads (attribution funnel, distributions, scatter, rule y.

## Files

### `readmenator` (21 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_analytics.py` | py | utility | 9 | yes |
| `readmenator/_concepts.py` | py | utility | 8 | yes |
| `readmenator/_config.py` | py | infrastructure | 1 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_dataflow.py` | py | data_access | 21 | yes |
| `readmenator/_dead_code.py` | py | utility | 5 | yes |
| `readmenator/_documentation.py` | py | utility | 31 | yes |
| `readmenator/_embed.py` | py | utility | 11 | yes |
| `readmenator/_exclusions.py` | py | utility | 11 | yes |
| `readmenator/_explorer.py` | py | utility | 13 | yes |

### `tests` (16 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_concepts.py` | py | testing | 8 | no |
| `tests/test_config.py` | py | testing | 6 | no |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_dataflow.py` | py | testing | 47 | no |
| `tests/test_dead_code.py` | py | testing | 15 | yes |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_exporter.py` | py | testing | 15 | yes |
| `tests/test_hotspots.py` | py | testing | 11 | no |
| `tests/test_interactive_graph.py` | py | testing | 40 | yes |
| `tests/test_layer_rules.py` | py | testing | 13 | no |

*... and 17 more files in this community.*


## Key Symbols

- `AnalyticsBuilder` (class, `readmenator/_analytics.py:25`) `class AnalyticsBuilder` - Builds analytics payloads from scanned topology and findings.
- `__init__` (method, `readmenator/_analytics.py:28`) `def __init__(self, config)` - Initialise with application configuration.
- `build` (method, `readmenator/_analytics.py:36`) `def build(self, nodes, edges, resolved_edges, analysis, findings, layers, v2, ho` - Build the full analytics payload.
- `_layer_distribution` (method, `readmenator/_analytics.py:100`) `def _layer_distribution(self, nodes, layers)` - Count files per architectural layer.
- `_language_distribution` (method, `readmenator/_analytics.py:112`) `def _language_distribution(self, nodes)` - Count files per programming language.
- `_hotspot_ranking` (method, `readmenator/_analytics.py:120`) `def _hotspot_ranking(self, nodes, fan_in, fan_out, hotspots)` - Rank files by combined symbol and connectivity weight.
- `_rule_yield` (method, `readmenator/_analytics.py:152`) `def _rule_yield(self, findings)` - Count security findings per rule with severity breakdown.
- `_size_bands` (method, `readmenator/_analytics.py:164`) `def _size_bands(self, nodes)` - Bucket files by symbol-count bands.
- `_scatter` (method, `readmenator/_analytics.py:181`) `def _scatter(self, nodes, fan_in, fan_out, layers)` - Build a file scatter of symbols versus connectivity.
- `verb_for_relation` (function, `readmenator/_concepts.py:33`) `def verb_for_relation(relation)` - Return the verb label for a structural edge relation.
- `ConceptExtractor` (class, `readmenator/_concepts.py:38`) `class ConceptExtractor` - Builds a ConceptGraph from scanned nodes and structural edges.
- `__init__` (method, `readmenator/_concepts.py:41`) `def __init__(self, config)` - Store configuration for concept extraction budgets.
- `extract` (method, `readmenator/_concepts.py:47`) `def extract(self, nodes, edges, resolved_edges)` - Build concepts and verb relations from structural topology.
- `_tokens_for_node` (method, `readmenator/_concepts.py:101`) `def _tokens_for_node(self, node)` - Return atomic noun tokens extracted from one file node.
- `_tokenize` (method, `readmenator/_concepts.py:115`) `def _tokenize(self, text)` - Split text atomically into normalised noun tokens.
- `_build_relations` (method, `readmenator/_concepts.py:130`) `def _build_relations(self, edges, file_to_concepts)` - Aggregate structural edges into concept verb relations.
- `_build_dialectic` (method, `readmenator/_concepts.py:169`) `def _build_dialectic(self, concepts, relations)` - Generate deterministic thesis/antithesis/synthesis prompts.
- `Config` (class, `readmenator/_config.py:15`) `class Config` - Single source of truth for all readmenator settings.
- `CodePropertyGraph` (class, `readmenator/_cpg.py:16`) `class CodePropertyGraph` - Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.
- `__init__` (method, `readmenator/_cpg.py:26`) `def __init__(self, privacy_mode, cpg_context)`
- `generate` (method, `readmenator/_cpg.py:30`) `def generate(self, nodes, edges, resolved_edges, analysis, findings)` - Generate the CPG JSON-LD string embeddable in markdown.
- `_severity_counts` (method, `readmenator/_cpg.py:147`) `def _severity_counts(self, findings)`
- `_build_symbol_list` (method, `readmenator/_cpg.py:153`) `def _build_symbol_list(self, node)`
- `_compute_node_hash` (method, `readmenator/_cpg.py:169`) `def _compute_node_hash(node)`
- `_strip_noise` (function, `readmenator/_dataflow.py:96`) `def _strip_noise(line)` - Remove comments and string contents that confuse identifier scans.
- `_strip_block_comments` (function, `readmenator/_dataflow.py:107`) `def _strip_block_comments(content)` - Blank block comments while preserving newlines and line numbers.
- `_blank` (method, `readmenator/_dataflow.py:110`) `def _blank(match)`
- `_strip_sizeof` (function, `readmenator/_dataflow.py:116`) `def _strip_sizeof(line)` - Blank sizeof operands, which never evaluate their argument at runtime.
- `DataflowAnalyzer` (class, `readmenator/_dataflow.py:122`) `class DataflowAnalyzer` - Regex-based intra-function dataflow checker over scanned content.
- `__init__` (method, `readmenator/_dataflow.py:125`) `def __init__(self, config)` - Store configuration for enable flag and issue caps.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 79
- Cross-boundary resolved imports (EXTRACTED): 107

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_analytics.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 0 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_agent_injector.py.
- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (readmenator: _pipeline) and community 5 (orphans).

## Risks

- [taint high] `readmenator/_diagrams.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_category.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_gh_wiki.py` -> `readmenator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 10 file(s) lack file-level docs (e.g. `tests/test_concepts.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_documentation.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _pipeline changed?
- Should readmenator: _pipeline be split, given cohesion 0.45?

## Sources

- `readmenator/_analytics.py`
- `readmenator/_concepts.py`
- `readmenator/_config.py`
- `readmenator/_cpg.py`
- `readmenator/_dataflow.py`
- `readmenator/_dead_code.py`
- `readmenator/_documentation.py`
- `readmenator/_embed.py`
- `readmenator/_exclusions.py`
- `readmenator/_explorer.py`
- `readmenator/_exporter.py`
- `readmenator/_forcegraph.py`
- `readmenator/_hotspots.py`
- `readmenator/_layer_rules.py`
- `readmenator/_pipeline.py`
- `readmenator/_provenance.py`
- `readmenator/_refactorizer.py`
- `readmenator/_rule_gen.py`
- `readmenator/_scantext.py`
- `readmenator/_taint.py`
- *... and 17 more*
