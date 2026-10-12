# GraphRAG Community Reports

Entities: 3205 | Relationships: 11074 | Communities: 8 | Themes: 2 | Text units: 3094

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

151 files in 8 communities and 2 themes. Highest-impact communities: readmenator: _pipeline (7.0), readmenator/parsers (6.9), readmenator: _video (4.5). God nodes: readmenator/_models.py, readmenator/_config.py, readmenator/_pipeline.py, readmenator/_app.py, readmenator/parsers/__init__.py.

- [readmenator: _pipeline] rating 7.0: `readmenator/_config.py` ranks 1 by PageRank, 100 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator/parsers] rating 6.9: `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator: _video] rating 4.5: `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _diagrams] rating 3.2: `readmenator/_app.py` ranks 1 by PageRank, 26 importers, 85 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator: _flowcharts] rating 1.3: `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- [readmenator: _security] rating 0.6: `readmenator/_analyzer.py` ranks 1 by PageRank, 12 importers, 23 symbols: Graph analysis engine for the readmenator knowledge graph.
- [readmenator: _agent_injector] rating 0.5: `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- [unassigned files] rating 0.2: `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- Key entities: file:tests/test_parsers.py, file:tests/test_interactive_graph.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:readmenator/_video.py, file:tests/test_ranking.py
- Children: t0, t1
- Root rating = highest community rating.

## readmenator: _pipeline + readmenator/parsers +5 (`t0`, theme, rating 7.0)

Theme of 7 communities and 148 files: readmenator: _pipeline (44 files, rating 7.0); readmenator/parsers (37 files, rating 6.9); readmenator: _video (14 files, rating 4.5); readmenator: _diagrams (30 files, rating 3.2); readmenator: _flowcharts (12 files, rating 1.3); readmenator: _security (6 files, rating 0.6); readmenator: _agent_injector (5 files, rating 0.5).

- [readmenator: _pipeline] `readmenator/_config.py` ranks 1 by PageRank, 100 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _pipeline] `readmenator/_htmlpack.py` ranks 2 by PageRank, 8 importers, 5 symbols: Compact JSON payload embedding for self-contained HTML pages.
- [readmenator/parsers] `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- [readmenator: _video] `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _video] `readmenator/_rank.py` ranks 2 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- [readmenator: _diagrams] `readmenator/_app.py` ranks 1 by PageRank, 26 importers, 85 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator: _diagrams] `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- Key entities: file:tests/test_parsers.py, file:tests/test_interactive_graph.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:readmenator/_video.py, file:tests/test_ranking.py, file:readmenator/_diagrams.py, file:readmenator/_app.py
- Children: c0, c1, c3, c2, c4, c5, c6
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.2)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.2).

- [unassigned files] `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- [unassigned files] `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py
- Children: c7
- Theme rating = highest child community rating.

## readmenator: _pipeline (`c0`, community, rating 7.0)

44 files under readmenator (py 44), mostly testing. Core file readmenator/_config.py (PageRank 0.1337, imported by 100 files): Immutable configuration dataclass for readmenator. Key abstractions: Config, escape_json_for_script, should_compress, compress_text, payload_script, read_payload_script. Depends on readmenator/parsers (40), readmenator: _diagrams (21), readmenator: _video (8). Used by readmenator: _diagrams (32), readmenator/parsers (13), readmenator: _flowcharts (12).

- `readmenator/_config.py` ranks 1 by PageRank, 100 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- `readmenator/_htmlpack.py` ranks 2 by PageRank, 8 importers, 5 symbols: Compact JSON payload embedding for self-contained HTML pages.
- `readmenator/_graphlayout.py` ranks 3 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- Hotspot `tests/test_parsers.py`: 87 symbols, 6 connections (score 0.38).
- Hotspot `tests/test_interactive_graph.py`: 60 symbols, 42 connections (score 0.28).
- 1 layer violations, e.g. test_layout_quality.py (testing) -> _forcegraph_page.py (presentation).
- Taint: 8 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:tests/test_parsers.py, file:tests/test_interactive_graph.py, file:readmenator/_pipeline.py, file:readmenator/_config.py, file:tests/test_uml.py, file:tests/test_dataflow.py, file:tests/test_parsers_new.py, file:readmenator/_forcegraph.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 104.

## readmenator/parsers (`c1`, community, rating 6.9)

37 files under readmenator/parsers (py 37), mostly utility. Core file readmenator/_models.py (PageRank 0.1376, imported by 114 files): Data model types for the readmenator knowledge graph. Key abstractions: Symbol, Node, Edge, SecurityFinding, CommunityResult, AnalysisResult. Depends on readmenator: _pipeline (13), readmenator: _diagrams (1), readmenator: _video (1). Used by readmenator: _pipeline (40), readmenator: _diagrams (17), readmenator: _video (11).

- `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- `readmenator/parsers/__init__.py` ranks 3 by PageRank, 3 importers, 2 symbols: Parser factory: maps file extensions to per-language LanguageParser classes.
- Hotspot `readmenator/_models.py`: 23 symbols, 119 connections (score 0.14).
- Hotspot `tests/test_parsers_property.py`: 27 symbols, 46 connections (score 0.13).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, sym:readmenator/_models.py::Symbol@18, sym:readmenator/parsers/_base.py::parse@36, sym:readmenator/_models.py::Edge@58, file:tests/test_parsers_property.py, file:tests/test_taint_bdd.py, file:readmenator/_scanner.py
- Rating 6.9/10 = 7 x PageRank share 0.98 + 3 x risk 0.00. Internal imports: 104.

## readmenator: _video (`c3`, community, rating 4.5)

14 files under readmenator (py 14), mostly utility. Core file readmenator/_category.py (PageRank 0.1337, imported by 9 files): Category theory model for the readmenator code graph. Key abstractions: EdgeKind, Morphism, Category, TypedGraph, weight, add_object. Depends on readmenator/parsers (11), readmenator: _pipeline (10), readmenator: _diagrams (7). Used by readmenator: _pipeline (8), readmenator: _diagrams (6), readmenator/parsers (1).

- `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- `readmenator/_rank.py` ranks 2 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- `readmenator/_query.py` ranks 3 by PageRank, 3 importers, 17 symbols: Query engine for the readmenator knowledge base.
- Hotspot `readmenator/_video.py`: 90 symbols, 39 connections (score 0.40).
- Hotspot `tests/test_ranking.py`: 72 symbols, 13 connections (score 0.32).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_video.py, file:tests/test_ranking.py, file:readmenator/_graphrag.py, file:tests/test_graphrag.py, file:readmenator/_category.py, file:readmenator/_rank.py, file:readmenator/_query.py, sym:readmenator/_graphrag.py::search@1004
- Rating 4.5/10 = 7 x PageRank share 0.64 + 3 x risk 0.00. Internal imports: 20.

## readmenator: _diagrams (`c2`, community, rating 3.2)

30 files under readmenator (py 30), mostly utility. Core file readmenator/_app.py (PageRank 0.0148, imported by 26 files): Application orchestrator: scan, resolve, analyze, and write every output. Key abstractions: readmenatorApplication, run, check_freshness, publish_github_wiki, generate_uml_code, update. Depends on readmenator: _pipeline (32), readmenator/parsers (17), readmenator: _security (8). Used by readmenator: _pipeline (21), readmenator: _video (7), readmenator: _security (3).

- `readmenator/_app.py` ranks 1 by PageRank, 26 importers, 85 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- `readmenator/_purpose.py` ranks 3 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- Hotspot `readmenator/_diagrams.py`: 92 symbols, 28 connections (score 0.41).
- Hotspot `readmenator/_app.py`: 85 symbols, 85 connections (score 0.40).
- 2 layer violations, e.g. test_components.py (testing) -> _components.py (presentation).
- Taint: 2 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:readmenator/_diagrams.py, file:readmenator/_app.py, file:tests/test_diagrams.py, file:readmenator/_mcp_server.py, file:tests/test_agent_friendliness.py, file:tests/test_components.py, file:readmenator/_agent_output.py, file:readmenator/_components.py
- Rating 3.2/10 = 7 x PageRank share 0.46 + 3 x risk 0.00. Internal imports: 66.

## readmenator: _flowcharts (`c4`, community, rating 1.3)

12 files under readmenator (py 12), mostly utility. Core file readmenator/_symindex.py (PageRank 0.0068, imported by 7 files): Deterministic symbol index with call-site resolution. Key abstractions: SymbolDef, CallSite, ResolvedCall, SymbolIndex, build, methods_index. Depends on readmenator: _pipeline (12), readmenator/parsers (6), readmenator: _diagrams (1). Used by readmenator: _diagrams (6), readmenator: _pipeline (4), readmenator: _video (2).

- `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- `readmenator/_flowlayout.py` ranks 2 by PageRank, 6 importers, 11 symbols: Flow graph model and deterministic layered layout (Sugiyama style).
- `readmenator/_apidocs.py` ranks 3 by PageRank, 7 importers, 52 symbols: Deterministic API reference model: extraction, cross-references, coverage.
- Hotspot `readmenator/_flowcharts.py`: 54 symbols, 23 connections (score 0.24).
- Hotspot `readmenator/_apidocs.py`: 52 symbols, 24 connections (score 0.23).
- 3 layer violations, e.g. test_apidocs.py (testing) -> _apidocs_page.py (presentation).
- Taint: 3 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:tests/test_apidocs.py, file:readmenator/_apidocs.py, sym:readmenator/_flowcharts.py::add@800, file:readmenator/_flowcharts.py, file:readmenator/_apidocs_render.py, file:tests/test_flowcharts.py, file:readmenator/_symindex.py, file:readmenator/_docstrings.py
- Rating 1.3/10 = 7 x PageRank share 0.19 + 3 x risk 0.00. Internal imports: 27.

## readmenator: _security (`c5`, community, rating 0.6)

6 files under readmenator (py 6), mostly testing. Core file readmenator/_analyzer.py (PageRank 0.0060, imported by 12 files): Graph analysis engine for the readmenator knowledge graph. Key abstractions: GraphAnalyzer, dominant_directory, analyze, partition, SecurityRule, SecurityAnalyzer. Depends on readmenator/parsers (7), readmenator: _pipeline (6), readmenator: _diagrams (3). Used by readmenator: _diagrams (8), readmenator: _pipeline (3), readmenator: _video (1).

- `readmenator/_analyzer.py` ranks 1 by PageRank, 12 importers, 23 symbols: Graph analysis engine for the readmenator knowledge graph.
- `readmenator/_security.py` ranks 2 by PageRank, 4 importers, 32 symbols: Pattern-based static security analysis for the readmenator knowledge graph.
- `readmenator/_wiki.py` ranks 3 by PageRank, 4 importers, 32 symbols: Deterministic agent wiki generator for readmenator.
- Hotspot `tests/test_security.py`: 68 symbols, 11 connections (score 0.30).
- Hotspot `readmenator/_wiki.py`: 32 symbols, 27 connections (score 0.15).
- Key entities: file:tests/test_security.py, sym:tests/test_security.py::_scan_content@71, file:readmenator/_wiki.py, file:readmenator/_security.py, file:readmenator/_analyzer.py, file:tests/test_wiki.py, file:tests/test_analyzer.py, sym:readmenator/_security.py::SecurityRule@24
- Rating 0.6/10 = 7 x PageRank share 0.08 + 3 x risk 0.00. Internal imports: 8.

## readmenator: _agent_injector (`c6`, community, rating 0.5)

5 files under tests (py 5), mostly testing. Core file readmenator/_readme_injector.py (PageRank 0.0060, imported by 5 files): Injects a knowledge base section into the project README (Markdown or RST). Key abstractions: ReadmeInjector, inject, remove, AgentInjector, ensure_readmenator_installed, inject. Depends on readmenator/parsers (4), readmenator: _pipeline (1), readmenator: _diagrams (1). Used by readmenator: _pipeline (2), readmenator: _video (1).

- `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- `readmenator/_agent_injector.py` ranks 2 by PageRank, 5 importers, 14 symbols: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
- `tests/test_agent_injector.py` ranks 3 by PageRank, 0 importers, 38 symbols: Contract tests for AI agent file injection.
- Hotspot `tests/test_agent_output.py`: 45 symbols, 37 connections (score 0.21).
- Hotspot `tests/test_agent_injector.py`: 38 symbols, 10 connections (score 0.17).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_agent_injector.py, file:tests/test_agent_output.py, file:tests/test_readme_injector.py, file:readmenator/_agent_injector.py, file:readmenator/_readme_injector.py, sym:tests/test_agent_output.py::_make_node@19, sym:readmenator/_agent_injector.py::AgentInjector@129, sym:readmenator/_agent_injector.py::_inject_single@203
- Rating 0.5/10 = 7 x PageRank share 0.07 + 3 x risk 0.00. Internal imports: 7.

## unassigned files (`c7`, community, rating 0.2)

3 files under readmenator/_vendor (py 2, js 1), mostly utility. Core file readmenator/_vendor/force-graph.min.js (PageRank 0.0028, imported by 0 files): Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph Key abstractions: Fe, as, as, wa, Na, t.

- `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `readmenator/_vendor/force-graph.min.js`: 35 symbols, 1732 connections (score 0.75).
- Hotspot `readmenator_orchestrator.py`: 37 symbols, 15 connections (score 0.17).
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py, sym:readmenator_orchestrator.py::run@372, sym:readmenator_orchestrator.py::_safe_env@68, sym:readmenator_orchestrator.py::process@202, sym:readmenator_orchestrator.py::_validate_repo_name@56, sym:readmenator_orchestrator.py::Config@21, sym:readmenator_orchestrator.py::__init__@84
- Rating 0.2/10 = 7 x PageRank share 0.03 + 3 x risk 0.00. Internal imports: 0.
