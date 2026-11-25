# GraphRAG Community Reports

Entities: 3640 | Relationships: 12555 | Communities: 8 | Themes: 2 | Text units: 3524

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

167 files in 8 communities and 2 themes. Highest-impact communities: readmenator: _app (7.0), readmenator/parsers (5.6), readmenator: _mcp_server (4.1). God nodes: readmenator/_config.py, readmenator/_models.py, readmenator/_app.py, readmenator/_pipeline.py, readmenator/parsers/__init__.py.

- [readmenator: _app] rating 7.0: `readmenator/_config.py` ranks 1 by PageRank, 112 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator/parsers] rating 5.6: `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator: _mcp_server] rating 4.1: `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _pipeline] rating 2.3: `readmenator/_gitmeta.py` ranks 1 by PageRank, 6 importers, 4 symbols: Read-only git metadata for freshness stamps on generated documents.
- [readmenator: _diagrams] rating 2.1: `readmenator/_project_config.py` ranks 1 by PageRank, 18 importers, 18 symbols: Per-project persistent configuration (readmenator.toml).
- [readmenator: _flowcharts] rating 1.3: `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- [readmenator: _video] rating 1.1: `readmenator/_resolver.py` ranks 1 by PageRank, 8 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- [unassigned files] rating 0.2: `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- Key entities: file:tests/test_parsers.py, file:readmenator/_app.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:tests/test_ranking.py, file:readmenator/_mcp_server.py
- Children: t0, t1
- Root rating = highest community rating.

## readmenator: _app + readmenator/parsers +5 (`t0`, theme, rating 7.0)

Theme of 7 communities and 163 files: readmenator: _app (46 files, rating 7.0); readmenator/parsers (30 files, rating 5.6); readmenator: _mcp_server (15 files, rating 4.1); readmenator: _pipeline (25 files, rating 2.3); readmenator: _diagrams (20 files, rating 2.1); readmenator: _flowcharts (14 files, rating 1.3); readmenator: _video (13 files, rating 1.1).

- [readmenator: _app] `readmenator/_config.py` ranks 1 by PageRank, 112 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- [readmenator: _app] `readmenator/_app.py` ranks 2 by PageRank, 27 importers, 90 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- [readmenator/parsers] `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- [readmenator/parsers] `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- [readmenator: _mcp_server] `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- [readmenator: _mcp_server] `readmenator/_rank.py` ranks 2 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- [readmenator: _pipeline] `readmenator/_gitmeta.py` ranks 1 by PageRank, 6 importers, 4 symbols: Read-only git metadata for freshness stamps on generated documents.
- [readmenator: _pipeline] `readmenator/_purpose.py` ranks 2 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- Key entities: file:tests/test_parsers.py, file:readmenator/_app.py, file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, file:tests/test_ranking.py, file:readmenator/_mcp_server.py, file:readmenator/_pipeline.py, file:tests/test_security.py
- Children: c0, c1, c4, c2, c3, c5, c6
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.2)

Theme of 1 communities and 4 files: unassigned files (4 files, rating 0.2).

- [unassigned files] `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- [unassigned files] `readmenator/_vendor/force-graph.min.js` ranks 2 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py
- Children: c7
- Theme rating = highest child community rating.

## readmenator: _app (`c0`, community, rating 7.0)

46 files under readmenator (py 46), mostly testing. Core file readmenator/_config.py (PageRank 0.1482, imported by 112 files): Immutable configuration dataclass for readmenator. Key abstractions: Config, readmenatorApplication, ingest_receipts, run, check_freshness, publish_github_wiki. Depends on readmenator/parsers (35), readmenator: _diagrams (16), readmenator: _pipeline (11). Used by readmenator: _pipeline (36), readmenator: _diagrams (16), readmenator: _flowcharts (13).

- `readmenator/_config.py` ranks 1 by PageRank, 112 importers, 1 symbols: Immutable configuration dataclass for readmenator.
- `readmenator/_app.py` ranks 2 by PageRank, 27 importers, 90 symbols: Application orchestrator: scan, resolve, analyze, and write every output.
- `readmenator/_receipts.py` ranks 3 by PageRank, 4 importers, 24 symbols: Release receipts ingest contract: deploys as first-class evidence.  deploynator writes `release-receipts/*.json` receipts.
- Hotspot `readmenator/_app.py`: 90 symbols, 103 connections (score 0.35).
- Hotspot `tests/test_parsers.py`: 87 symbols, 6 connections (score 0.31).
- 1 layer violations, e.g. test_components.py (testing) -> _components.py (presentation).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: _hypotheses.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_parsers.py, file:readmenator/_app.py, file:tests/test_interactive_graph.py, file:readmenator/_config.py, file:tests/test_diagrams.py, file:tests/test_dataflow.py, file:tests/test_components.py, file:tests/test_docbranch.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 97.

## readmenator/parsers (`c1`, community, rating 5.6)

30 files under readmenator/parsers (py 30), mostly utility. Core file readmenator/_models.py (PageRank 0.1237, imported by 114 files): Data model types for the readmenator knowledge graph. Key abstractions: Symbol, Node, Edge, SecurityFinding, CommunityResult, AnalysisResult. Depends on readmenator: _app (5), readmenator: _mcp_server (1). Used by readmenator: _app (35), readmenator: _pipeline (17), readmenator: _flowcharts (14).

- `readmenator/_models.py` ranks 1 by PageRank, 114 importers, 23 symbols: Data model types for the readmenator knowledge graph.
- `readmenator/parsers/_base.py` ranks 2 by PageRank, 20 importers, 6 symbols: LanguageParser base class with shared docstring and signature extraction.
- `readmenator/parsers/__init__.py` ranks 3 by PageRank, 3 importers, 2 symbols: Parser factory: maps file extensions to per-language LanguageParser classes.
- Hotspot `readmenator/_models.py`: 23 symbols, 119 connections (score 0.12).
- Hotspot `tests/test_parsers_property.py`: 27 symbols, 46 connections (score 0.11).
- Taint: 3 paths reach this group via subprocess.
- Key entities: file:readmenator/_models.py, sym:readmenator/_models.py::Node@37, sym:readmenator/_models.py::Symbol@18, sym:readmenator/parsers/_base.py::parse@36, sym:readmenator/_models.py::Edge@58, file:tests/test_parsers_property.py, sym:readmenator/parsers/__init__.py::create_parser@70, file:readmenator/parsers/_base.py
- Rating 5.6/10 = 7 x PageRank share 0.80 + 3 x risk 0.00. Internal imports: 88.

## readmenator: _mcp_server (`c4`, community, rating 4.1)

15 files under readmenator (py 15), mostly utility. Core file readmenator/_category.py (PageRank 0.1201, imported by 9 files): Category theory model for the readmenator code graph. Key abstractions: EdgeKind, Morphism, Category, TypedGraph, weight, add_object. Depends on readmenator: _app (11), readmenator/parsers (9), readmenator: _pipeline (5). Used by readmenator: _pipeline (7), readmenator: _app (4), readmenator: _flowcharts (2).

- `readmenator/_category.py` ranks 1 by PageRank, 9 importers, 26 symbols: Category theory model for the readmenator code graph.
- `readmenator/_rank.py` ranks 2 by PageRank, 11 importers, 18 symbols: PageRank, Personalized PageRank, HITS, and composite scoring.
- `readmenator/_query.py` ranks 3 by PageRank, 3 importers, 17 symbols: Query engine for the readmenator knowledge base.
- Hotspot `tests/test_ranking.py`: 72 symbols, 13 connections (score 0.26).
- Hotspot `readmenator/_mcp_server.py`: 65 symbols, 17 connections (score 0.23).
- Taint: 3 paths reach this group via subprocess.
- Surprising bridge: readmenator.py <-> test_agent_injector.py (5 hops across communities).
- Key entities: file:tests/test_ranking.py, file:readmenator/_mcp_server.py, file:readmenator/_graphrag.py, file:tests/test_uml.py, file:tests/test_graphrag.py, file:readmenator/_category.py, sym:readmenator/__main__.py::main@155, file:readmenator/_uml.py
- Rating 4.1/10 = 7 x PageRank share 0.58 + 3 x risk 0.00. Internal imports: 22.

## readmenator: _pipeline (`c2`, community, rating 2.3)

25 files under readmenator (py 25), mostly utility. Core file readmenator/_gitmeta.py (PageRank 0.0071, imported by 6 files): Read-only git metadata for freshness stamps on generated documents. Key abstractions: read_git_head, is_garbage_doc, clean_purpose, escape_cell, truncate_words, first_sentence. Depends on readmenator: _app (36), readmenator/parsers (17), readmenator: _diagrams (10). Used by readmenator: _app (11), readmenator: _mcp_server (5), readmenator: _diagrams (4).

- `readmenator/_gitmeta.py` ranks 1 by PageRank, 6 importers, 4 symbols: Read-only git metadata for freshness stamps on generated documents.
- `readmenator/_purpose.py` ranks 2 by PageRank, 9 importers, 7 symbols: Purpose extraction shared by every agent-facing document generator.
- `readmenator/_layers.py` ranks 3 by PageRank, 7 importers, 7 symbols: Architectural layer detection for the readmenator knowledge graph.
- Hotspot `tests/test_security.py`: 68 symbols, 11 connections (score 0.24).
- Hotspot `readmenator/_pipeline.py`: 55 symbols, 93 connections (score 0.23).
- 1 layer violations, e.g. test_folder_readme.py (testing) -> _components.py (presentation).
- Taint: 2 paths reach this group via subprocess.
- Key entities: file:readmenator/_pipeline.py, file:tests/test_security.py, file:tests/test_agent_friendliness.py, sym:tests/test_security.py::_scan_content@71, file:readmenator/_agent_output.py, file:readmenator/_components.py, file:readmenator/_wiki.py, file:readmenator/_memory.py
- Rating 2.3/10 = 7 x PageRank share 0.32 + 3 x risk 0.00. Internal imports: 59.

## readmenator: _diagrams (`c3`, community, rating 2.1)

20 files under readmenator (py 20), mostly testing. Core file readmenator/_project_config.py (PageRank 0.0134, imported by 18 files): Per-project persistent configuration (readmenator.toml). Key abstractions: template_text, config_path, ensure_project_config, parse_toml, load_project_config, display_name. Depends on readmenator: _app (16), readmenator/parsers (10), readmenator: _pipeline (4). Used by readmenator: _app (16), readmenator: _pipeline (10), readmenator: _flowcharts (5).

- `readmenator/_project_config.py` ranks 1 by PageRank, 18 importers, 18 symbols: Per-project persistent configuration (readmenator.toml).
- `readmenator/_graphlayout.py` ranks 2 by PageRank, 5 importers, 26 symbols: Deterministic graph layout algorithms for animated renders.
- `readmenator/_htmlpack.py` ranks 3 by PageRank, 8 importers, 5 symbols: Compact JSON payload embedding for self-contained HTML pages.
- Hotspot `readmenator/_diagrams.py`: 97 symbols, 43 connections (score 0.36).
- Hotspot `tests/test_agent_output.py`: 45 symbols, 37 connections (score 0.17).
- 6 layer violations, e.g. test_layout_quality.py (testing) -> _forcegraph_page.py (presentation).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:readmenator/_diagrams.py, file:tests/test_agent_injector.py, file:tests/test_agent_output.py, file:tests/test_readme_injector.py, file:readmenator/_forcegraph.py, file:tests/test_project_config.py, file:tests/test_bundlegraph.py, file:tests/test_graphlayout.py
- Rating 2.1/10 = 7 x PageRank share 0.30 + 3 x risk 0.00. Internal imports: 54.

## readmenator: _flowcharts (`c5`, community, rating 1.3)

14 files under readmenator (py 14), mostly utility. Core file readmenator/_symindex.py (PageRank 0.0061, imported by 7 files): Deterministic symbol index with call-site resolution. Key abstractions: SymbolDef, CallSite, ResolvedCall, SymbolIndex, build, methods_index. Depends on readmenator/parsers (14), readmenator: _app (13), readmenator: _diagrams (5). Used by readmenator: _app (5), readmenator: _pipeline (5), readmenator: _diagrams (2).

- `readmenator/_symindex.py` ranks 1 by PageRank, 7 importers, 22 symbols: Deterministic symbol index with call-site resolution.
- `readmenator/_flowlayout.py` ranks 2 by PageRank, 6 importers, 11 symbols: Flow graph model and deterministic layered layout (Sugiyama style).
- `readmenator/_apidocs.py` ranks 3 by PageRank, 7 importers, 52 symbols: Deterministic API reference model: extraction, cross-references, coverage.
- Hotspot `readmenator/_flowcharts.py`: 54 symbols, 23 connections (score 0.20).
- Hotspot `readmenator/_apidocs.py`: 52 symbols, 24 connections (score 0.19).
- 3 layer violations, e.g. test_apidocs.py (testing) -> _apidocs_page.py (presentation).
- Taint: 2 paths reach this group via subprocess.
- Surprising bridge: _docstrings.py <-> test_graphlayout.py (5 hops across communities).
- Key entities: file:readmenator/_apidocs.py, file:tests/test_apidocs.py, sym:readmenator/_flowcharts.py::add@800, file:readmenator/_flowcharts.py, file:readmenator/_apidocs_render.py, file:tests/test_flowcharts.py, file:readmenator/_documentation.py, file:readmenator/_symindex.py
- Rating 1.3/10 = 7 x PageRank share 0.18 + 3 x risk 0.00. Internal imports: 30.

## readmenator: _video (`c6`, community, rating 1.1)

13 files under tests (py 13), mostly testing. Core file readmenator/_resolver.py (PageRank 0.0082, imported by 8 files): Import path resolver for the readmenator knowledge graph. Key abstractions: ImportResolver, resolve, resolve_all, Backdrop, CinematicVideoRenderer, ease. Depends on readmenator: _app (13), readmenator/parsers (8), readmenator: _diagrams (1). Used by readmenator: _pipeline (6), readmenator: _app (2), readmenator: _diagrams (1).

- `readmenator/_resolver.py` ranks 1 by PageRank, 8 importers, 17 symbols: Import path resolver for the readmenator knowledge graph.
- `readmenator/_video.py` ranks 2 by PageRank, 7 importers, 114 symbols: Cinematic codebase overview video, general purpose.
- `readmenator/_scanner.py` ranks 3 by PageRank, 5 importers, 16 symbols: Secure polyglot directory traversal and file analysis.
- Hotspot `readmenator/_video.py`: 114 symbols, 50 connections (score 0.42).
- Hotspot `tests/test_soundtrack.py`: 51 symbols, 24 connections (score 0.19).
- Key entities: file:readmenator/_video.py, file:tests/test_soundtrack.py, file:tests/test_taint_bdd.py, file:readmenator/_soundtrack.py, file:readmenator/_githistory.py, file:tests/test_video.py, file:readmenator/_resolver.py, file:tests/test_githistory.py
- Rating 1.1/10 = 7 x PageRank share 0.16 + 3 x risk 0.00. Internal imports: 17.

## unassigned files (`c7`, community, rating 0.2)

4 files under root (py 2, js 1, sh 1), mostly utility. Core file deploy.sh (PageRank 0.0026, imported by 0 files): one-liner deploy via deploynator (generic per-repo script). Key abstractions: ensure_pkg, Fe, as, as, wa, Na.

- `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- `readmenator/_vendor/force-graph.min.js` ranks 2 by PageRank, 0 importers, 35 symbols: Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `readmenator_orchestrator.py` ranks 3 by PageRank, 0 importers, 37 symbols: test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild with all improvements.
- Hotspot `readmenator/_vendor/force-graph.min.js`: 35 symbols, 1732 connections (score 0.72).
- Hotspot `readmenator_orchestrator.py`: 37 symbols, 15 connections (score 0.14).
- Key entities: file:readmenator/_vendor/force-graph.min.js, file:readmenator_orchestrator.py, sym:readmenator_orchestrator.py::run@372, sym:readmenator_orchestrator.py::_safe_env@68, sym:readmenator_orchestrator.py::process@202, sym:readmenator_orchestrator.py::_validate_repo_name@56, sym:readmenator_orchestrator.py::Config@21, sym:readmenator_orchestrator.py::__init__@84
- Rating 0.2/10 = 7 x PageRank share 0.03 + 3 x risk 0.00. Internal imports: 0.
