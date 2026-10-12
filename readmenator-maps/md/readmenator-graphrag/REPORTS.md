# GraphRAG Community Reports

Entities: 3090 | Relationships: 10499 | Communities: 7 | Themes: 2 | Text units: 2981

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

145 files in 7 communities and 2 themes. Highest-impact communities: readmenator: _graphrag (7.0), readmenator/parsers (7.0), readmenator: _diagrams (6.9). God nodes: readmenator/_models.py, readmenator/_config.py, readmenator/_pipeline.py, readmenator/_app.py, readmenator/parsers/__init__.py.

- [readmenator: _graphrag] rating 7.0: `readmenator/_config.py` ranks 1 by PageRank, 95 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator/parsers] rating 7.0: `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator: _diagrams] rating 6.9: `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _pipeline] rating 2.0: `readmenator/_graphlayout.py` ranks 1 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- [readmenator: _apidocs] rating 1.4: `readmenator/_apidocs.py` ranks 1 by PageRank, 6 importers, 52 symbols: Deterministic API reference model: extraction, cross-references, coverage.
- [readmenator: _agent_injector] rating 0.5: `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- [unassigned files] rating 0.2: `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- Key entities: file:tests/test_parsers.py, file:tests/test_security.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:readmenator/_diagrams.py, file:readmenator/_app.py
- Children: t0, t1
- Root rating = highest community rating.

## readmenator: _graphrag + readmenator/parsers +4 (`t0`, theme, rating 7.0)

Theme of 6 communities and 142 files: readmenator: _graphrag (40 files, rating 7.0); readmenator/parsers (32 files, rating 7.0); readmenator: _diagrams (31 files, rating 6.9); readmenator: _pipeline (20 files, rating 2.0); readmenator: _apidocs (14 files, rating 1.4); readmenator: _agent_injector (5 files, rating 0.5).

- [readmenator: _graphrag] `readmenator/_config.py` ranks 1 by PageRank, 95 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _graphrag] `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- [readmenator: _diagrams] `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _diagrams] `readmenator/_app.py` ranks 2 by PageRank, 24 importers, 81 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator: _pipeline] `readmenator/_graphlayout.py` ranks 1 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- [readmenator: _pipeline] `readmenator/_forcegraph.py` ranks 2 by PageRank, 9 importers, 23 symbols: Force-graph explorer for the readmenator knowledge graph.
- Key entities: file:tests/test_parsers.py, file:tests/test_security.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:readmenator/_diagrams.py, file:readmenator/_app.py, file:tests/test_interactive_graph.py, file:readmenator/_pipeline.py
- Children: c0, c1, c2, c3, c4, c5
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.2)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.2).

- [unassigned files] `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- [unassigned files] `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py
- Children: c6
- Theme rating = highest child community rating.

## readmenator: _graphrag (`c0`, community, rating 7.0)

40 files under readmenator (py 40), mostly testing. Core file readmenator/_config.py (PageRank 0.1275, imported by 95 files): Immutable configuration dataclass for readmenator. Key abstractions: Config, ImportResolver, resolve, resolve_all, is_garbage_doc, clean_purpose. Depends on readmenator/parsers (37), readmenator: _diagrams (9). Used by readmenator: _diagrams (33), readmenator: _pipeline (31), readmenator: _apidocs (11).

- `readmenator/_config.py` ranks 1 by PageRank, 95 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- `readmenator/_resolver.py` ranks 2 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- `readmenator/_purpose.py` ranks 3 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- Hotspot `tests/test_parsers.py`: 87 symbols, 6 connections (score 0.38).
- Hotspot `tests/test_security.py`: 68 symbols, 11 connections (score 0.30).
- Taint: 4 paths reach this group via subprocess.
- Key entities: file:tests/test_parsers.py, file:tests/test_security.py, file:readmenator/_config.py, file:tests/test_agent_friendliness.py, file:readmenator/_graphrag.py, file:tests/test_dataflow.py, sym:tests/test_security.py::_scan_content@71, file:tests/test_parsers_new.py
- Rating 7.0/10 = 7 x PageRank share 0.99 + 3 x risk 0.00. Internal imports: 88.

## readmenator/parsers (`c1`, community, rating 7.0)

32 files under readmenator/parsers (py 32), mostly utility. Core file readmenator/_models.py (PageRank 0.1449, imported by 114 files): Data model types for the readmenator knowledge graph. Key abstractions: Symbol, Node, Edge, SecurityFinding, CommunityResult, AnalysisResult. Depends on readmenator: _graphrag (8), readmenator: _diagrams (1). Used by readmenator: _graphrag (37), readmenator: _diagrams (19), readmenator: _pipeline (16).

- `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- `readmenator/parsers/__init__.py` ranks 3 by PageRank, 3 importers, 2 symbols: Parser factory: maps file extensions to per-language LanguageParser classes.
- Hotspot `readmenator/_models.py`: 23 symbols, 119 connections (score 0.14).
- Hotspot `tests/test_parsers_property.py`: 27 symbols, 46 connections (score 0.13).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, sym:readmenator/_models.py::Symbol@18, sym:readmenator/parsers/_base.py::parse@36, sym:readmenator/_models.py::Edge@58, file:tests/test_parsers_property.py, sym:readmenator/parsers/__init__.py::create_parser@70, file:readmenator/parsers/_base.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 91.

## readmenator: _diagrams (`c2`, community, rating 6.9)

31 files under readmenator (py 31), mostly utility. Core file readmenator/_category.py (PageRank 0.1409, imported by 9 files): Category theory model for the readmenator code graph. Key abstractions: EdgeKind, Morphism, Category, TypedGraph, weight, add_object. Depends on readmenator: _graphrag (33), readmenator/parsers (19), readmenator: _pipeline (5). Used by readmenator: _pipeline (19), readmenator: _graphrag (9), readmenator: _apidocs (4).

- `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- `readmenator/_app.py` ranks 2 by PageRank, 24 importers, 81 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- `readmenator/_rank.py` ranks 3 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- Hotspot `readmenator/_diagrams.py`: 92 symbols, 23 connections (score 0.41).
- Hotspot `readmenator/_app.py`: 81 symbols, 79 connections (score 0.38).
- 1 layer violations, e.g. test_components.py (testing) -> _components.py (presentation).
- Taint: 3 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:readmenator/_diagrams.py, file:readmenator/_app.py, file:tests/test_diagrams.py, file:readmenator/_video.py, file:tests/test_ranking.py, file:readmenator/_mcp_server.py, file:tests/test_components.py, file:readmenator/_components.py
- Rating 6.9/10 = 7 x PageRank share 0.99 + 3 x risk 0.00. Internal imports: 61.

## readmenator: _pipeline (`c3`, community, rating 2.0)

20 files under readmenator (py 20), mostly utility. Core file readmenator/_graphlayout.py (PageRank 0.0085, imported by 5 files): Deterministic graph layout algorithms for animated renders. Key abstractions: ForceAtlas2Settings, BundleLayout, SphereBundleLayout, forceatlas2_frames, fit_frames, interpolate_frames. Depends on readmenator: _graphrag (31), readmenator: _diagrams (19), readmenator/parsers (16). Used by readmenator: _diagrams (5), readmenator: _apidocs (2).

- `readmenator/_graphlayout.py` ranks 1 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- `readmenator/_forcegraph.py` ranks 2 by PageRank, 9 importers, 23 symbols: Force-graph explorer for the readmenator knowledge graph.
- `readmenator/_analytics.py` ranks 3 by PageRank, 5 importers, 9 symbols: Corpus analytics aggregations for the readmenator knowledge graph.
- Hotspot `tests/test_interactive_graph.py`: 60 symbols, 40 connections (score 0.27).
- Hotspot `readmenator/_pipeline.py`: 52 symbols, 87 connections (score 0.26).
- 1 layer violations, e.g. test_layout_quality.py (testing) -> _forcegraph_page.py (presentation).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:tests/test_interactive_graph.py, file:readmenator/_pipeline.py, file:readmenator/_forcegraph.py, file:tests/test_graphlayout.py, file:tests/test_bundlegraph.py, file:readmenator/_graphlayout.py, file:tests/test_sourceview.py, file:readmenator/_explorer.py
- Rating 2.0/10 = 7 x PageRank share 0.29 + 3 x risk 0.00. Internal imports: 39.

## readmenator: _apidocs (`c4`, community, rating 1.4)

14 files under readmenator (py 14), mostly utility. Core file readmenator/_apidocs.py (PageRank 0.0071, imported by 6 files): Deterministic API reference model: extraction, cross-references, coverage. Key abstractions: ApiParam, ApiEntity, DocWarning, ApiReference, ApiReferenceBuilder, to_dict. Depends on readmenator/parsers (15), readmenator: _graphrag (11), readmenator: _diagrams (4). Used by readmenator: _pipeline (5), readmenator: _diagrams (3).

- `readmenator/_apidocs.py` ranks 1 by PageRank, 6 importers, 52 symbols: Deterministic API reference model: extraction, cross-references, coverage.
- `readmenator/_pytypes.py` ranks 2 by PageRank, 3 importers, 16 symbols: Lightweight, deterministic receiver typing for Python attribute calls.
- `readmenator/_docstrings.py` ranks 3 by PageRank, 3 importers, 30 symbols: Multi-style docstring parser for the deterministic API reference.
- Hotspot `readmenator/_apidocs.py`: 52 symbols, 23 connections (score 0.23).
- Hotspot `tests/test_uml.py`: 49 symbols, 8 connections (score 0.22).
- 2 layer violations, e.g. test_apidocs.py (testing) -> _apidocs_page.py (presentation).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:readmenator/_apidocs.py, file:tests/test_apidocs.py, file:readmenator/_flowcharts.py, file:tests/test_uml.py, file:readmenator/_apidocs_render.py, file:readmenator/_documentation.py, file:tests/test_documentation.py, file:readmenator/_docstrings.py
- Rating 1.4/10 = 7 x PageRank share 0.20 + 3 x risk 0.00. Internal imports: 21.

## readmenator: _agent_injector (`c5`, community, rating 0.5)

5 files under tests (py 5), mostly testing. Core file readmenator/_readme_injector.py (PageRank 0.0062, imported by 5 files): Injects a knowledge base section into the project README (Markdown or RST). Key abstractions: ReadmeInjector, inject, remove, AgentInjector, ensure_readmenator_installed, inject. Depends on readmenator/parsers (4), readmenator: _graphrag (2). Used by readmenator: _pipeline (2), readmenator: _diagrams (1).

- `readmenator/_readme_injector.py` ranks 1 by PageRank, 5 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- `readmenator/_agent_injector.py` ranks 2 by PageRank, 5 importers, 14 symbols: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
- `tests/test_agent_injector.py` ranks 3 by PageRank, 0 importers, 38 symbols: Contract tests for AI agent file injection.
- Hotspot `tests/test_agent_output.py`: 45 symbols, 37 connections (score 0.21).
- Hotspot `tests/test_agent_injector.py`: 38 symbols, 10 connections (score 0.17).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_agent_injector.py, file:tests/test_agent_output.py, file:tests/test_readme_injector.py, file:readmenator/_agent_injector.py, file:readmenator/_readme_injector.py, sym:tests/test_agent_output.py::_make_node@19, sym:readmenator/_agent_injector.py::AgentInjector@129, sym:readmenator/_agent_injector.py::_inject_single@203
- Rating 0.5/10 = 7 x PageRank share 0.08 + 3 x risk 0.00. Internal imports: 7.

## unassigned files (`c6`, community, rating 0.2)

3 files under readmenator/_vendor (py 2, js 1), mostly utility. Core file readmenator/_vendor/force-graph.min.js (PageRank 0.0030, imported by 0 files): Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph Key abstractions: Fe, as, as, wa, Na, t.

- `readmenator/_vendor/force-graph.min.js` ranks 1 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `readmenator_orchestrator.py` ranks 2 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `readmenator/_vendor/force-graph.min.js`: 35 symbols, 1732 connections (score 0.75).
- Hotspot `readmenator_orchestrator.py`: 37 symbols, 15 connections (score 0.17).
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py, sym:readmenator_orchestrator.py::run@372, sym:readmenator_orchestrator.py::_safe_env@68, sym:readmenator_orchestrator.py::process@202, sym:readmenator_orchestrator.py::_validate_repo_name@56, sym:readmenator_orchestrator.py::Config@21, sym:readmenator_orchestrator.py::__init__@84
- Rating 0.2/10 = 7 x PageRank share 0.03 + 3 x risk 0.00. Internal imports: 0.
