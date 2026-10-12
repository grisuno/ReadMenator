# GraphRAG Community Reports

Entities: 3174 | Relationships: 10937 | Communities: 7 | Themes: 2 | Text units: 3063

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

149 files in 7 communities and 2 themes. Highest-impact communities: readmenator/parsers (7.0), readmenator: _graphrag (6.8), readmenator: _diagrams (6.5). God nodes: readmenator/_models.py, readmenator/_config.py, readmenator/_pipeline.py, readmenator/_app.py, readmenator/parsers/__init__.py.

- [readmenator/parsers] rating 7.0: `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator: _graphrag] rating 6.8: `readmenator/_config.py` ranks 1 by PageRank, 98 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _diagrams] rating 6.5: `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _pipeline] rating 1.8: `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- [readmenator: _graphlayout] rating 1.5: `readmenator/_htmlpack.py` ranks 1 by PageRank, 8 importers, 5 symbols: Compact JSON payload embedding for self-contained HTML pages.
- [readmenator: _flowcharts] rating 1.4: `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- [unassigned files] rating 0.2: `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:tests/test_parsers.py, file:tests/test_security.py, file:readmenator/_diagrams.py, file:readmenator/_app.py
- Children: t0, t1
- Root rating = highest community rating.

## readmenator/parsers + readmenator: _graphrag +4 (`t0`, theme, rating 7.0)

Theme of 6 communities and 146 files: readmenator/parsers (34 files, rating 7.0); readmenator: _graphrag (38 files, rating 6.8); readmenator: _diagrams (29 files, rating 6.5); readmenator: _pipeline (20 files, rating 1.8); readmenator: _graphlayout (13 files, rating 1.5); readmenator: _flowcharts (12 files, rating 1.4).

- [readmenator/parsers] `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- [readmenator: _graphrag] `readmenator/_config.py` ranks 1 by PageRank, 98 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _graphrag] `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- [readmenator: _diagrams] `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _diagrams] `readmenator/_app.py` ranks 2 by PageRank, 25 importers, 84 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator: _pipeline] `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- [readmenator: _pipeline] `readmenator/_agent_injector.py` ranks 2 by PageRank, 5 importers, 14 symbols: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:tests/test_parsers.py, file:tests/test_security.py, file:readmenator/_diagrams.py, file:readmenator/_app.py, file:tests/test_interactive_graph.py, file:readmenator/_pipeline.py
- Children: c1, c0, c2, c3, c4, c5
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.2)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.2).

- [unassigned files] `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- [unassigned files] `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py
- Children: c6
- Theme rating = highest child community rating.

## readmenator/parsers (`c1`, community, rating 7.0)

34 files under readmenator/parsers (py 34), mostly utility. Core file readmenator/_models.py (PageRank 0.1398, imported by 114 files): Data model types for the readmenator knowledge graph. Key abstractions: Symbol, Node, Edge, SecurityFinding, CommunityResult, AnalysisResult. Depends on readmenator: _graphrag (10), readmenator: _diagrams (1). Used by readmenator: _graphrag (33), readmenator: _pipeline (26), readmenator: _diagrams (17).

- `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- `readmenator/parsers/__init__.py` ranks 3 by PageRank, 3 importers, 2 symbols: Parser factory: maps file extensions to per-language LanguageParser classes.
- Hotspot `tests/test_dataflow.py`: 47 symbols, 12 connections (score 0.21).
- Hotspot `readmenator/_models.py`: 23 symbols, 119 connections (score 0.14).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, sym:readmenator/_models.py::Symbol@18, sym:readmenator/parsers/_base.py::parse@36, sym:readmenator/_models.py::Edge@58, file:tests/test_dataflow.py, file:tests/test_parsers_property.py, sym:tests/test_dataflow.py::_analyze@17
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 96.

## readmenator: _graphrag (`c0`, community, rating 6.8)

38 files under readmenator (py 38), mostly testing. Core file readmenator/_config.py (PageRank 0.1311, imported by 98 files): Immutable configuration dataclass for readmenator. Key abstractions: Config, ImportResolver, resolve, resolve_all, is_garbage_doc, clean_purpose. Depends on readmenator/parsers (33), readmenator: _diagrams (9). Used by readmenator: _diagrams (31), readmenator: _pipeline (28), readmenator: _graphlayout (11).

- `readmenator/_config.py` ranks 1 by PageRank, 98 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- `readmenator/_purpose.py` ranks 3 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- Hotspot `tests/test_parsers.py`: 87 symbols, 6 connections (score 0.38).
- Hotspot `tests/test_security.py`: 68 symbols, 11 connections (score 0.30).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:tests/test_parsers.py, file:tests/test_security.py, file:readmenator/_config.py, file:tests/test_agent_friendliness.py, file:readmenator/_graphrag.py, sym:tests/test_security.py::_scan_content@71, file:tests/test_parsers_new.py, file:readmenator/_agent_output.py
- Rating 6.8/10 = 7 x PageRank share 0.98 + 3 x risk 0.00. Internal imports: 85.

## readmenator: _diagrams (`c2`, community, rating 6.5)

29 files under readmenator (py 29), mostly utility. Core file readmenator/_category.py (PageRank 0.1358, imported by 9 files): Category theory model for the readmenator code graph. Key abstractions: EdgeKind, Morphism, Category, TypedGraph, weight, add_object. Depends on readmenator: _graphrag (31), readmenator/parsers (17), readmenator: _flowcharts (8). Used by readmenator: _pipeline (13), readmenator: _graphrag (9), readmenator: _graphlayout (7).

- `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- `readmenator/_app.py` ranks 2 by PageRank, 25 importers, 84 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- `readmenator/_rank.py` ranks 3 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- Hotspot `readmenator/_diagrams.py`: 92 symbols, 25 connections (score 0.41).
- Hotspot `readmenator/_video.py`: 90 symbols, 39 connections (score 0.40).
- 1 layer violations, e.g. test_components.py (testing) -> _components.py (presentation).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:readmenator/_diagrams.py, file:readmenator/_app.py, file:tests/test_diagrams.py, file:readmenator/_video.py, file:tests/test_ranking.py, file:readmenator/_mcp_server.py, file:tests/test_components.py, file:readmenator/_components.py
- Rating 6.5/10 = 7 x PageRank share 0.93 + 3 x risk 0.00. Internal imports: 57.

## readmenator: _pipeline (`c3`, community, rating 1.8)

20 files under readmenator (py 20), mostly utility. Core file readmenator/_readme_injector.py (PageRank 0.0061, imported by 5 files): Injects a knowledge base section into the project README (Markdown or RST). Key abstractions: ReadmeInjector, inject, remove, AgentInjector, ensure_readmenator_installed, inject. Depends on readmenator: _graphrag (28), readmenator/parsers (26), readmenator: _diagrams (13). Used by readmenator: _diagrams (3), readmenator: _graphlayout (1), readmenator: _flowcharts (1).

- `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- `readmenator/_agent_injector.py` ranks 2 by PageRank, 5 importers, 14 symbols: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
- `readmenator/_analytics.py` ranks 3 by PageRank, 5 importers, 9 symbols: Corpus analytics aggregations for the readmenator knowledge graph.
- Hotspot `tests/test_interactive_graph.py`: 60 symbols, 42 connections (score 0.28).
- Hotspot `readmenator/_pipeline.py`: 52 symbols, 87 connections (score 0.26).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_interactive_graph.py, file:readmenator/_pipeline.py, file:tests/test_agent_injector.py, file:tests/test_uml.py, file:tests/test_agent_output.py, file:tests/test_readme_injector.py, file:readmenator/_documentation.py, file:tests/test_documentation.py
- Rating 1.8/10 = 7 x PageRank share 0.26 + 3 x risk 0.00. Internal imports: 32.

## readmenator: _graphlayout (`c4`, community, rating 1.5)

13 files under readmenator (py 13), mostly utility. Core file readmenator/_htmlpack.py (PageRank 0.0090, imported by 8 files): Compact JSON payload embedding for self-contained HTML pages. Key abstractions: escape_json_for_script, should_compress, compress_text, payload_script, read_payload_script, ForceAtlas2Settings. Depends on readmenator: _graphrag (11), readmenator: _diagrams (7), readmenator/parsers (6). Used by readmenator: _pipeline (8), readmenator: _diagrams (5), readmenator: _flowcharts (2).

- `readmenator/_htmlpack.py` ranks 1 by PageRank, 8 importers, 5 symbols: Compact JSON payload embedding for self-contained HTML pages.
- `readmenator/_graphlayout.py` ranks 2 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- `readmenator/_forcegraph.py` ranks 3 by PageRank, 9 importers, 23 symbols: Force-graph explorer for the readmenator knowledge graph.
- Hotspot `tests/test_graphlayout.py`: 33 symbols, 5 connections (score 0.15).
- Hotspot `tests/test_bundlegraph.py`: 27 symbols, 25 connections (score 0.13).
- 1 layer violations, e.g. test_layout_quality.py (testing) -> _forcegraph_page.py (presentation).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:readmenator/_forcegraph.py, file:tests/test_graphlayout.py, file:tests/test_bundlegraph.py, file:readmenator/_graphlayout.py, file:tests/test_sourceview.py, file:readmenator/_explorer.py, file:tests/test_htmlpack.py, file:readmenator/_bundlegraph.py
- Rating 1.5/10 = 7 x PageRank share 0.21 + 3 x risk 0.00. Internal imports: 22.

## readmenator: _flowcharts (`c5`, community, rating 1.4)

12 files under readmenator (py 12), mostly utility. Core file readmenator/_symindex.py (PageRank 0.0069, imported by 7 files): Deterministic symbol index with call-site resolution. Key abstractions: SymbolDef, CallSite, ResolvedCall, SymbolIndex, build, methods_index. Depends on readmenator: _graphrag (9), readmenator/parsers (6), readmenator: _graphlayout (2). Used by readmenator: _diagrams (8), readmenator: _pipeline (4).

- `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- `readmenator/_flowlayout.py` ranks 2 by PageRank, 6 importers, 11 symbols: Flow graph model and deterministic layered layout (Sugiyama style).
- `readmenator/_apidocs.py` ranks 3 by PageRank, 7 importers, 52 symbols: Deterministic API reference model: extraction, cross-references, coverage.
- Hotspot `readmenator/_flowcharts.py`: 54 symbols, 23 connections (score 0.24).
- Hotspot `readmenator/_apidocs.py`: 52 symbols, 24 connections (score 0.23).
- 3 layer violations, e.g. test_apidocs.py (testing) -> _apidocs_page.py (presentation).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:tests/test_apidocs.py, file:readmenator/_apidocs.py, sym:readmenator/_flowcharts.py::add@800, file:readmenator/_flowcharts.py, file:readmenator/_apidocs_render.py, file:tests/test_flowcharts.py, file:readmenator/_symindex.py, file:readmenator/_docstrings.py
- Rating 1.4/10 = 7 x PageRank share 0.20 + 3 x risk 0.00. Internal imports: 27.

## unassigned files (`c6`, community, rating 0.2)

3 files under readmenator/_vendor (py 2, js 1), mostly utility. Core file readmenator/_vendor/force-graph.min.js (PageRank 0.0029, imported by 0 files): Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph Key abstractions: Fe, as, as, wa, Na, t.

- `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `readmenator/_vendor/force-graph.min.js`: 35 symbols, 1732 connections (score 0.75).
- Hotspot `readmenator_orchestrator.py`: 37 symbols, 15 connections (score 0.17).
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py, sym:readmenator_orchestrator.py::run@372, sym:readmenator_orchestrator.py::_safe_env@68, sym:readmenator_orchestrator.py::process@202, sym:readmenator_orchestrator.py::_validate_repo_name@56, sym:readmenator_orchestrator.py::Config@21, sym:readmenator_orchestrator.py::__init__@84
- Rating 0.2/10 = 7 x PageRank share 0.03 + 3 x risk 0.00. Internal imports: 0.
