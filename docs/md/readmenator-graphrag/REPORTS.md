# GraphRAG Community Reports

Entities: 3365 | Relationships: 11588 | Communities: 8 | Themes: 2 | Text units: 3251

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

159 files in 8 communities and 2 themes. Highest-impact communities: readmenator: _video (7.0), readmenator/parsers (6.9), readmenator: _graphrag (4.8). God nodes: readmenator/_models.py, readmenator/_config.py, readmenator/_app.py, readmenator/_pipeline.py, readmenator/parsers/__init__.py.

- [readmenator: _video] rating 7.0: `readmenator/_config.py` ranks 1 by PageRank, 104 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator/parsers] rating 6.9: `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator: _graphrag] rating 4.8: `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _agent_output] rating 2.0: `readmenator/_resolver.py` ranks 1 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- [readmenator: _diagrams] rating 1.9: `readmenator/_project_config.py` ranks 1 by PageRank, 18 importers, 18 symbols: Per-project persistent configuration (readmenator.toml).
- [readmenator: _pipeline] rating 1.6: `readmenator/_readme_injector.py` ranks 1 by PageRank, 7 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- [readmenator: _flowcharts] rating 1.3: `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- [unassigned files] rating 0.3: `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- Key entities: file:tests/test_parsers.py, file:readmenator/_app.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:tests/test_ranking.py, file:readmenator/_graphrag.py
- Children: t0, t1
- Root rating = highest community rating.

## readmenator: _video + readmenator/parsers +5 (`t0`, theme, rating 7.0)

Theme of 7 communities and 155 files: readmenator: _video (36 files, rating 7.0); readmenator/parsers (37 files, rating 6.9); readmenator: _graphrag (18 files, rating 4.8); readmenator: _agent_output (19 files, rating 2.0); readmenator: _diagrams (15 files, rating 1.9); readmenator: _pipeline (18 files, rating 1.6); readmenator: _flowcharts (12 files, rating 1.3).

- [readmenator: _video] `readmenator/_config.py` ranks 1 by PageRank, 104 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _video] `readmenator/_app.py` ranks 2 by PageRank, 26 importers, 88 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator/parsers] `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- [readmenator: _graphrag] `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _graphrag] `readmenator/_rank.py` ranks 2 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- [readmenator: _agent_output] `readmenator/_resolver.py` ranks 1 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- [readmenator: _agent_output] `readmenator/_purpose.py` ranks 2 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- Key entities: file:tests/test_parsers.py, file:readmenator/_app.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:tests/test_ranking.py, file:readmenator/_graphrag.py, file:tests/test_security.py, file:tests/test_agent_friendliness.py
- Children: c1, c0, c3, c2, c5, c4, c6
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.3)

Theme of 1 communities and 4 files: unassigned files (4 files, rating 0.3).

- [unassigned files] `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- [unassigned files] `readmenator/_vendor/force-graph.min.js` ranks 2 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py
- Children: c7
- Theme rating = highest child community rating.

## readmenator: _video (`c1`, community, rating 7.0)

36 files under tests (py 36), mostly testing. Core file readmenator/_config.py (PageRank 0.1433, imported by 104 files): Immutable configuration dataclass for readmenator. Key abstractions: Config, readmenatorApplication, ingest_receipts, run, check_freshness, publish_github_wiki. Depends on readmenator/parsers (31), readmenator: _diagrams (11), readmenator: _pipeline (6). Used by readmenator: _agent_output (21), readmenator: _pipeline (21), readmenator: _graphrag (18).

- `readmenator/_config.py` ranks 1 by PageRank, 104 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- `readmenator/_app.py` ranks 2 by PageRank, 26 importers, 88 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- `readmenator/_receipts.py` ranks 3 by PageRank, 4 importers, 24 symbols: Release receipts ingest contract: deploys as first-class evidence.  deploynator writes `release-receipts/*.json` receipts.
- Hotspot `readmenator/_app.py`: 88 symbols, 98 connections (score 0.40).
- Hotspot `readmenator/_video.py`: 90 symbols, 39 connections (score 0.38).
- Taint: 2 paths reach this group via subprocess.
- Surprising bridge: _hypotheses.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_parsers.py, file:readmenator/_app.py, file:tests/test_diagrams.py, file:readmenator/_video.py, file:readmenator/_config.py, file:readmenator/_mcp_server.py, file:tests/test_dataflow.py, file:tests/test_parsers_new.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 69.

## readmenator/parsers (`c0`, community, rating 6.9)

37 files under readmenator/parsers (py 37), mostly utility. Core file readmenator/_models.py (PageRank 0.1289, imported by 114 files): Data model types for the readmenator knowledge graph. Key abstractions: Symbol, Node, Edge, SecurityFinding, CommunityResult, AnalysisResult. Depends on readmenator: _video (13), readmenator: _agent_output (1), readmenator: _graphrag (1). Used by readmenator: _video (31), readmenator: _pipeline (21), readmenator: _agent_output (12).

- `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- `readmenator/parsers/__init__.py` ranks 3 by PageRank, 3 importers, 2 symbols: Parser factory: maps file extensions to per-language LanguageParser classes.
- Hotspot `readmenator/_models.py`: 23 symbols, 119 connections (score 0.14).
- Hotspot `tests/test_parsers_property.py`: 27 symbols, 46 connections (score 0.13).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, sym:readmenator/_models.py::Symbol@18, sym:readmenator/parsers/_base.py::parse@36, sym:readmenator/_models.py::Edge@58, file:tests/test_parsers_property.py, file:tests/test_taint_bdd.py, file:readmenator/_scanner.py
- Rating 6.9/10 = 7 x PageRank share 0.99 + 3 x risk 0.00. Internal imports: 101.

## readmenator: _graphrag (`c3`, community, rating 4.8)

18 files under readmenator (py 18), mostly utility. Core file readmenator/_category.py (PageRank 0.1252, imported by 9 files): Category theory model for the readmenator code graph. Key abstractions: EdgeKind, Morphism, Category, TypedGraph, weight, add_object. Depends on readmenator: _video (18), readmenator/parsers (12), readmenator: _agent_output (6). Used by readmenator: _pipeline (8), readmenator: _video (5), readmenator/parsers (1).

- `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- `readmenator/_rank.py` ranks 2 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- `readmenator/_query.py` ranks 3 by PageRank, 3 importers, 17 symbols: Query engine for the readmenator knowledge base.
- Hotspot `tests/test_ranking.py`: 72 symbols, 13 connections (score 0.30).
- Hotspot `readmenator/_graphrag.py`: 53 symbols, 26 connections (score 0.23).
- 1 layer violations, e.g. test_components.py (testing) -> _components.py (presentation).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:tests/test_ranking.py, file:readmenator/_graphrag.py, file:tests/test_components.py, file:readmenator/_components.py, file:tests/test_graphrag.py, file:readmenator/_category.py, file:readmenator/_rank.py, sym:readmenator/_graphrag.py::search@1004
- Rating 4.8/10 = 7 x PageRank share 0.69 + 3 x risk 0.00. Internal imports: 26.

## readmenator: _agent_output (`c2`, community, rating 2.0)

19 files under readmenator (py 19), mostly utility. Core file readmenator/_resolver.py (PageRank 0.0073, imported by 7 files): Import path resolver for the readmenator knowledge graph. Key abstractions: ImportResolver, resolve, resolve_all, is_garbage_doc, clean_purpose, escape_cell. Depends on readmenator: _video (21), readmenator/parsers (12), readmenator: _diagrams (4). Used by readmenator: _pipeline (8), readmenator: _graphrag (6), readmenator: _video (4).

- `readmenator/_resolver.py` ranks 1 by PageRank, 7 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- `readmenator/_purpose.py` ranks 2 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- `readmenator/_analyzer.py` ranks 3 by PageRank, 12 importers, 23 symbols: Graph analysis engine for the readmenator knowledge graph.
- Hotspot `tests/test_security.py`: 68 symbols, 11 connections (score 0.28).
- Hotspot `tests/test_agent_friendliness.py`: 59 symbols, 47 connections (score 0.26).
- 1 layer violations, e.g. test_folder_readme.py (testing) -> _components.py (presentation).
- Taint: 1 paths reach this group via subprocess.
- Key entities: file:tests/test_security.py, file:tests/test_agent_friendliness.py, sym:tests/test_security.py::_scan_content@71, file:readmenator/_agent_output.py, file:readmenator/_wiki.py, file:readmenator/_memory.py, file:readmenator/_security.py, file:readmenator/_analyzer.py
- Rating 2.0/10 = 7 x PageRank share 0.28 + 3 x risk 0.00. Internal imports: 39.

## readmenator: _diagrams (`c5`, community, rating 1.9)

15 files under readmenator (py 15), mostly utility. Core file readmenator/_project_config.py (PageRank 0.0141, imported by 18 files): Per-project persistent configuration (readmenator.toml). Key abstractions: template_text, config_path, ensure_project_config, parse_toml, load_project_config, display_name. Depends on readmenator: _video (15), readmenator/parsers (6), readmenator: _agent_output (4). Used by readmenator: _video (11), readmenator: _pipeline (11), readmenator: _agent_output (4).

- `readmenator/_project_config.py` ranks 1 by PageRank, 18 importers, 18 symbols: Per-project persistent configuration (readmenator.toml).
- `readmenator/_graphlayout.py` ranks 2 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- `readmenator/_htmlpack.py` ranks 3 by PageRank, 8 importers, 5 symbols: Compact JSON payload embedding for self-contained HTML pages.
- Hotspot `readmenator/_diagrams.py`: 97 symbols, 43 connections (score 0.41).
- Hotspot `tests/test_project_config.py`: 33 symbols, 39 connections (score 0.15).
- 6 layer violations, e.g. test_layout_quality.py (testing) -> _forcegraph_page.py (presentation).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:readmenator/_diagrams.py, file:readmenator/_forcegraph.py, file:tests/test_project_config.py, file:tests/test_graphlayout.py, file:tests/test_bundlegraph.py, file:readmenator/_project_config.py, file:readmenator/_graphlayout.py, file:tests/test_sourceview.py
- Rating 1.9/10 = 7 x PageRank share 0.27 + 3 x risk 0.00. Internal imports: 45.

## readmenator: _pipeline (`c4`, community, rating 1.6)

18 files under readmenator (py 18), mostly utility. Core file readmenator/_readme_injector.py (PageRank 0.0059, imported by 7 files): Injects a knowledge base section into the project README (Markdown or RST). Key abstractions: ReadmeInjector, inject, remove, AgentInjector, ensure_readmenator_installed, inject. Depends on readmenator/parsers (21), readmenator: _video (21), readmenator: _diagrams (11). Used by readmenator: _video (6), readmenator: _diagrams (3), readmenator: _graphrag (2).

- `readmenator/_readme_injector.py` ranks 1 by PageRank, 7 importers, 9 symbols: Injects a knowledge base section into the project README (Markdown or RST).
- `readmenator/_agent_injector.py` ranks 2 by PageRank, 5 importers, 14 symbols: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
- `readmenator/_analytics.py` ranks 3 by PageRank, 5 importers, 9 symbols: Corpus analytics aggregations for the readmenator knowledge graph.
- Hotspot `tests/test_interactive_graph.py`: 60 symbols, 42 connections (score 0.26).
- Hotspot `readmenator/_pipeline.py`: 53 symbols, 89 connections (score 0.25).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: _hypotheses.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_interactive_graph.py, file:readmenator/_pipeline.py, file:tests/test_agent_injector.py, file:tests/test_uml.py, file:tests/test_agent_output.py, file:tests/test_readme_injector.py, file:readmenator/_documentation.py, file:readmenator/_explorer.py
- Rating 1.6/10 = 7 x PageRank share 0.23 + 3 x risk 0.00. Internal imports: 30.

## readmenator: _flowcharts (`c6`, community, rating 1.3)

12 files under readmenator (py 12), mostly utility. Core file readmenator/_symindex.py (PageRank 0.0064, imported by 7 files): Deterministic symbol index with call-site resolution. Key abstractions: SymbolDef, CallSite, ResolvedCall, SymbolIndex, build, methods_index. Depends on readmenator: _video (10), readmenator/parsers (6), readmenator: _diagrams (4). Used by readmenator: _video (6), readmenator: _pipeline (4), readmenator: _graphrag (2).

- `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- `readmenator/_flowlayout.py` ranks 2 by PageRank, 6 importers, 11 symbols: Flow graph model and deterministic layered layout (Sugiyama style).
- `readmenator/_apidocs.py` ranks 3 by PageRank, 7 importers, 52 symbols: Deterministic API reference model: extraction, cross-references, coverage.
- Hotspot `readmenator/_flowcharts.py`: 54 symbols, 23 connections (score 0.23).
- Hotspot `readmenator/_apidocs.py`: 52 symbols, 24 connections (score 0.22).
- 3 layer violations, e.g. test_apidocs.py (testing) -> _apidocs_page.py (presentation).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:tests/test_apidocs.py, file:readmenator/_apidocs.py, sym:readmenator/_flowcharts.py::add@800, file:readmenator/_flowcharts.py, file:readmenator/_apidocs_render.py, file:tests/test_flowcharts.py, file:readmenator/_symindex.py, file:readmenator/_docstrings.py
- Rating 1.3/10 = 7 x PageRank share 0.18 + 3 x risk 0.00. Internal imports: 27.

## unassigned files (`c7`, community, rating 0.3)

4 files under root (py 2, js 1, sh 1), mostly utility. Core file deploy.sh (PageRank 0.0027, imported by 0 files): one-liner deploy via deploynator (generic per-repo script). Key abstractions: ensure_pkg, Fe, as, as, wa, Na.

- `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- `readmenator/_vendor/force-graph.min.js` ranks 2 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `readmenator_orchestrator.py` ranks 3 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- Hotspot `readmenator/_vendor/force-graph.min.js`: 35 symbols, 1732 connections (score 0.74).
- Hotspot `readmenator_orchestrator.py`: 37 symbols, 15 connections (score 0.16).
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py, sym:readmenator_orchestrator.py::run@372, sym:readmenator_orchestrator.py::_safe_env@68, sym:readmenator_orchestrator.py::process@202, sym:readmenator_orchestrator.py::_validate_repo_name@56, sym:readmenator_orchestrator.py::Config@21, sym:readmenator_orchestrator.py::__init__@84
- Rating 0.3/10 = 7 x PageRank share 0.04 + 3 x risk 0.00. Internal imports: 0.
