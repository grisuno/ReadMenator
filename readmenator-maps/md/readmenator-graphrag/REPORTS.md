# GraphRAG Community Reports

Entities: 2516 | Relationships: 8523 | Communities: 7 | Themes: 2 | Text units: 2408

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

124 files in 7 communities and 2 themes. Highest-impact communities: readmenator/parsers (7.0), readmenator: _agent_output (6.8), readmenator: _video (5.1). God nodes: readmenator/_models.py, readmenator/_config.py, readmenator/_pipeline.py, readmenator/_app.py, readmenator/parsers/__init__.py.

- [readmenator/parsers] rating 7.0: `readmenator/_models.py` ranks 1 by PageRank, 102 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator: _agent_output] rating 6.8: `readmenator/_config.py` ranks 1 by PageRank, 76 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _video] rating 5.1: `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _diagrams] rating 2.3: `readmenator/_app.py` ranks 1 by PageRank, 14 importers, 71 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator: _pipeline] rating 1.7: `readmenator/_analytics.py` ranks 1 by PageRank, 5 importers, 9 symbols: Corpus analytics aggregations for the readmenator knowledge graph.
- [readmenator: _agent_injector] rating 0.6: `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 8 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- [unassigned files] rating 0.2: `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Symbol@18, file:tests/test_parsers.py, file:tests/test_security.py, file:tests/test_ranking.py, file:readmenator/_graphrag.py
- Children: t0, t1
- Root rating = highest community rating.

## readmenator/parsers + readmenator: _agent_output +4 (`t0`, theme, rating 7.0)

Theme of 6 communities and 121 files: readmenator/parsers (28 files, rating 7.0); readmenator: _agent_output (38 files, rating 6.8); readmenator: _video (13 files, rating 5.1); readmenator: _diagrams (20 files, rating 2.3); readmenator: _pipeline (17 files, rating 1.7); readmenator: _agent_injector (5 files, rating 0.6).

- [readmenator/parsers] `readmenator/_models.py` ranks 1 by PageRank, 102 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- [readmenator: _agent_output] `readmenator/_config.py` ranks 1 by PageRank, 76 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _agent_output] `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- [readmenator: _video] `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _video] `readmenator/_rank.py` ranks 2 by PageRank, 10 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- [readmenator: _diagrams] `readmenator/_app.py` ranks 1 by PageRank, 14 importers, 71 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator: _diagrams] `readmenator/_layers.py` ranks 2 by PageRank, 6 importers, 7 symbols: Architectural layer detection for the readmenator knowledge graph.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Symbol@18, file:tests/test_parsers.py, file:tests/test_security.py, file:tests/test_ranking.py, file:readmenator/_graphrag.py, file:readmenator/_diagrams.py, file:readmenator/_app.py
- Children: c1, c0, c4, c2, c3, c5
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.2)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.2).

- [unassigned files] `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- [unassigned files] `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py
- Children: c6
- Theme rating = highest child community rating.

## readmenator/parsers (`c1`, community, rating 7.0)

28 files under readmenator/parsers (py 28), mostly utility. Core file readmenator/_models.py (PageRank 0.1553, imported by 102 files): Data model types for the readmenator knowledge graph. Key abstractions: Symbol, Node, Edge, SecurityFinding, CommunityResult, AnalysisResult. Depends on readmenator: _agent_output (4), readmenator: _video (1). Used by readmenator: _agent_output (37), readmenator: _pipeline (21), readmenator: _diagrams (11).

- `readmenator/_models.py` ranks 1 by PageRank, 102 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- `readmenator/parsers/__init__.py` ranks 3 by PageRank, 3 importers, 2 symbols: Parser factory: maps file extensions to per-language LanguageParser classes.
- Hotspot `tests/test_parsers_property.py`: 27 symbols, 46 connections (score 0.13).
- Hotspot `readmenator/_models.py`: 23 symbols, 107 connections (score 0.13).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Symbol@18, sym:readmenator/_models.py::Node@37, sym:readmenator/parsers/_base.py::parse@36, sym:readmenator/_models.py::Edge@58, file:tests/test_parsers_property.py, sym:readmenator/parsers/__init__.py::create_parser@70, file:readmenator/parsers/_base.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 85.

## readmenator: _agent_output (`c0`, community, rating 6.8)

38 files under readmenator (py 38), mostly testing. Core file readmenator/_config.py (PageRank 0.1243, imported by 76 files): Immutable configuration dataclass for readmenator. Key abstractions: Config, ImportResolver, resolve, resolve_all, is_garbage_doc, clean_purpose. Depends on readmenator/parsers (37), readmenator: _diagrams (5), readmenator: _video (1). Used by readmenator: _pipeline (30), readmenator: _diagrams (23), readmenator: _video (7).

- `readmenator/_config.py` ranks 1 by PageRank, 76 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- `readmenator/_purpose.py` ranks 3 by PageRank, 8 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- Hotspot `tests/test_parsers.py`: 87 symbols, 6 connections (score 0.39).
- Hotspot `tests/test_security.py`: 68 symbols, 11 connections (score 0.30).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: test_agent_injector.py <-> test_resolver.py (5 hops across communities).
- Key entities: file:tests/test_parsers.py, file:tests/test_security.py, sym:readmenator/_resolver.py::resolve@110, file:tests/test_agent_friendliness.py, file:readmenator/_config.py, file:tests/test_dataflow.py, sym:tests/test_security.py::_scan_content@71, file:tests/test_parsers_new.py
- Rating 6.8/10 = 7 x PageRank share 0.97 + 3 x risk 0.00. Internal imports: 80.

## readmenator: _video (`c4`, community, rating 5.1)

13 files under readmenator (py 13), mostly utility. Core file readmenator/_category.py (PageRank 0.1521, imported by 9 files): Category theory model for the readmenator code graph. Key abstractions: EdgeKind, Morphism, Category, TypedGraph, weight, add_object. Depends on readmenator/parsers (8), readmenator: _agent_output (7), readmenator: _diagrams (1). Used by readmenator: _diagrams (7), readmenator: _pipeline (7), readmenator: _agent_output (1).

- `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- `readmenator/_rank.py` ranks 2 by PageRank, 10 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- `readmenator/_graphlayout.py` ranks 3 by PageRank, 3 importers, 11 symbols: Deterministic graph layout algorithms for animated renders.
- Hotspot `tests/test_ranking.py`: 72 symbols, 13 connections (score 0.32).
- Hotspot `readmenator/_video.py`: 55 symbols, 34 connections (score 0.25).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:tests/test_ranking.py, file:readmenator/_graphrag.py, file:readmenator/_video.py, file:tests/test_graphrag.py, file:readmenator/_category.py, file:readmenator/_rank.py, file:readmenator/_query.py, file:tests/test_query.py
- Rating 5.1/10 = 7 x PageRank share 0.73 + 3 x risk 0.00. Internal imports: 18.

## readmenator: _diagrams (`c2`, community, rating 2.3)

20 files under readmenator (py 20), mostly utility. Core file readmenator/_app.py (PageRank 0.0131, imported by 14 files): Application orchestrator: scan, resolve, analyze, and write every output. Key abstractions: readmenatorApplication, run, check_freshness, publish_github_wiki, generate_uml_code, update. Depends on readmenator: _agent_output (23), readmenator/parsers (11), readmenator: _video (7). Used by readmenator: _pipeline (9), readmenator: _agent_output (5), readmenator: _video (1).

- `readmenator/_app.py` ranks 1 by PageRank, 14 importers, 71 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- `readmenator/_layers.py` ranks 2 by PageRank, 6 importers, 7 symbols: Architectural layer detection for the readmenator knowledge graph.
- `readmenator/_mcp_server.py` ranks 3 by PageRank, 3 importers, 64 symbols: MCP (Model Context Protocol) stdio server for ReadMenator.
- Hotspot `readmenator/_diagrams.py`: 90 symbols, 22 connections (score 0.41).
- Hotspot `readmenator/_app.py`: 71 symbols, 62 connections (score 0.33).
- Taint: 2 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:readmenator/_diagrams.py, file:readmenator/_app.py, file:tests/test_diagrams.py, file:readmenator/_mcp_server.py, file:readmenator/_gh_wiki.py, sym:readmenator/__main__.py::main@146, file:tests/test_mcp_server.py, file:readmenator/_yaralite.py
- Rating 2.3/10 = 7 x PageRank share 0.33 + 3 x risk 0.00. Internal imports: 31.

## readmenator: _pipeline (`c3`, community, rating 1.7)

17 files under readmenator (py 17), mostly utility. Core file readmenator/_analytics.py (PageRank 0.0061, imported by 5 files): Corpus analytics aggregations for the readmenator knowledge graph. Key abstractions: AnalyticsBuilder, build, ForceGraphRenderer, family_color_from_name, node_value, node_palette. Depends on readmenator: _agent_output (30), readmenator/parsers (21), readmenator: _diagrams (9). Used by readmenator: _diagrams (4).

- `readmenator/_analytics.py` ranks 1 by PageRank, 5 importers, 9 symbols: Corpus analytics aggregations for the readmenator knowledge graph.
- `readmenator/_forcegraph.py` ranks 2 by PageRank, 5 importers, 18 symbols: Force-graph explorer for the readmenator knowledge graph.
- `readmenator/_uml.py` ranks 3 by PageRank, 4 importers, 25 symbols: UML class diagram renderer (Mermaid classDiagram) and 12-language stub generator.
- Hotspot `tests/test_uml.py`: 49 symbols, 8 connections (score 0.22).
- Hotspot `readmenator/_pipeline.py`: 45 symbols, 73 connections (score 0.22).
- Taint: 5 paths reach this group via subprocess.
- Key entities: file:readmenator/_pipeline.py, file:tests/test_interactive_graph.py, file:tests/test_uml.py, file:readmenator/_documentation.py, file:readmenator/_forcegraph.py, file:tests/test_documentation.py, file:readmenator/_uml.py, file:readmenator/_exporter.py
- Rating 1.7/10 = 7 x PageRank share 0.24 + 3 x risk 0.00. Internal imports: 30.

## readmenator: _agent_injector (`c5`, community, rating 0.6)

5 files under tests (py 5), mostly testing. Core file readmenator/_readme_injector.py (PageRank 0.0073, imported by 5 files): Injects a knowledge base section into the project README (Markdown or RST). Key abstractions: ReadmeInjector, inject, remove, AgentInjector, ensure_readmenator_installed, inject. Depends on readmenator/parsers (4), readmenator: _agent_output (2). Used by readmenator: _pipeline (2), readmenator: _diagrams (1).

- `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 8 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- `readmenator/_agent_injector.py` ranks 2 by PageRank, 5 importers, 14 symbols: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
- `tests/test_agent_injector.py` ranks 3 by PageRank, 0 importers, 38 symbols: Contract tests for AI agent file injection.
- Hotspot `tests/test_agent_output.py`: 45 symbols, 37 connections (score 0.21).
- Hotspot `tests/test_agent_injector.py`: 38 symbols, 10 connections (score 0.17).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_agent_injector.py, file:tests/test_agent_output.py, file:tests/test_readme_injector.py, file:readmenator/_agent_injector.py, file:readmenator/_readme_injector.py, sym:tests/test_agent_output.py::_make_node@19, sym:readmenator/_agent_injector.py::AgentInjector@129, sym:readmenator/_agent_injector.py::_inject_single@203
- Rating 0.6/10 = 7 x PageRank share 0.08 + 3 x risk 0.00. Internal imports: 7.

## unassigned files (`c6`, community, rating 0.2)

3 files under readmenator/_vendor (py 2, js 1), mostly utility. Core file readmenator/_vendor/force-graph.min.js (PageRank 0.0034, imported by 0 files): Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph Key abstractions: Fe, as, as, wa, Na, t.

- `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `readmenator/_vendor/force-graph.min.js`: 35 symbols, 2351 connections (score 0.76).
- Hotspot `readmenator_orchestrator.py`: 37 symbols, 15 connections (score 0.17).
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py, sym:readmenator_orchestrator.py::run@372, sym:readmenator_orchestrator.py::_safe_env@68, sym:readmenator_orchestrator.py::process@202, sym:readmenator_orchestrator.py::_validate_repo_name@56, sym:readmenator_orchestrator.py::Config@21, sym:readmenator_orchestrator.py::__init__@84
- Rating 0.2/10 = 7 x PageRank share 0.03 + 3 x risk 0.00. Internal imports: 0.
