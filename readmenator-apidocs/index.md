# ReadMenator API Reference

> Generated offline by readmenator: 96 modules, 1905 documented entities, documentation coverage 82.4% (690/837 public items). Deterministic, zero tokens: signatures from source, docs parsed from Google, NumPy, reST, Javadoc/JSDoc/Doxygen, C# XML, and Rustdoc comments.

Navigate: [Interactive architecture and flows](flows.html) | [Architecture and flows (Mermaid)](architecture.md) | [Class hierarchy](classes.md) | [General index](genindex.md) | [Coverage and warnings](COVERAGE.md) | [`api/index.json`](api/index.json) | [HTML browser](index.html)

Languages: py (96)

## Modules

### `.`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`readmenator`](modules/readmenator.py.md) | Launcher shim that runs the readmenator CLI from a source checkout. | 0 | 0 | 100.0% |
| [`readmenator_orchestrator`](modules/readmenator_orchestrator.py.md) |  | 5 | 20 | 3.8% |

### `readmenator`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`readmenator`](modules/readmenator.__init__.py.md) | ReadMenator -- Zero-token polyglot codebase knowledge graph generator. | 0 | 0 | 100.0% |
| [`readmenator.__main__`](modules/readmenator.__main__.py.md) | Command line entry point: argument parsing and subcommand dispatch. | 0 | 2 | 33.3% |
| [`readmenator._agent_injector`](modules/readmenator._agent_injector.py.md) | Injects KNOWLEDGE_BASE.md references into AI agent instruction files. | 1 | 5 | 85.7% |
| [`readmenator._agent_output`](modules/readmenator._agent_output.py.md) | Agent-friendly output generator for ReadMenator. | 1 | 2 | 100.0% |
| [`readmenator._analytics`](modules/readmenator._analytics.py.md) | Corpus analytics aggregations for the readmenator knowledge graph. | 1 | 2 | 100.0% |
| [`readmenator._analyzer`](modules/readmenator._analyzer.py.md) | Graph analysis engine for the readmenator knowledge graph. | 1 | 4 | 100.0% |
| [`readmenator._apidocs`](modules/readmenator._apidocs.py.md) | Deterministic API reference model: extraction, cross-references, coverage. | 5 | 10 | 100.0% |
| [`readmenator._apidocs_page`](modules/readmenator._apidocs_page.py.md) | Self-contained HTML browser for the deterministic API reference. | 0 | 1 | 100.0% |
| [`readmenator._apidocs_render`](modules/readmenator._apidocs_render.py.md) | Markdown, JSON, and writer layer for the deterministic API reference. | 3 | 18 | 100.0% |
| [`readmenator._app`](modules/readmenator._app.py.md) | Application orchestrator: scan, resolve, analyze, and write every output. | 1 | 54 | 50.0% |
| [`readmenator._bundlegraph`](modules/readmenator._bundlegraph.py.md) | Edge bundle explorer: circle and sphere hierarchical edge bundling pages. | 1 | 6 | 100.0% |
| [`readmenator._bundlegraph_page`](modules/readmenator._bundlegraph_page.py.md) | HTML page template for the edge bundle explorer. | 0 | 0 | 100.0% |
| [`readmenator._cache`](modules/readmenator._cache.py.md) | File-content hash cache for incremental scanning and analysis caching. | 1 | 12 | 50.0% |
| [`readmenator._category`](modules/readmenator._category.py.md) | Category theory model for the readmenator code graph. | 4 | 17 | 50.0% |
| [`readmenator._components`](modules/readmenator._components.py.md) | Component architecture diagrams, token-free by default. | 1 | 9 | 100.0% |
| [`readmenator._concepts`](modules/readmenator._concepts.py.md) | Deterministic semantic concept graph over the structural knowledge graph. | 1 | 3 | 100.0% |
| [`readmenator._config`](modules/readmenator._config.py.md) | Immutable configuration dataclass for readmenator. | 1 | 0 | 100.0% |
| [`readmenator._cpg`](modules/readmenator._cpg.py.md) | Code Property Graph (CPG) generator emitting JSON-LD for AI agents. | 1 | 2 | 75.0% |
| [`readmenator._cursorrules_generator`](modules/readmenator._cursorrules_generator.py.md) | Dynamic .cursorrules generator for the readmenator knowledge graph. | 1 | 2 | 75.0% |
| [`readmenator._dataflow`](modules/readmenator._dataflow.py.md) | Procedural intra-function dataflow analysis for readmenator. | 1 | 2 | 100.0% |
| [`readmenator._dead_code`](modules/readmenator._dead_code.py.md) | Dead code detection for the readmenator knowledge graph. | 1 | 2 | 75.0% |
| [`readmenator._diagrams`](modules/readmenator._diagrams.py.md) | Self-contained interactive system maps for the knowledge graph. | 12 | 20 | 100.0% |
| [`readmenator._docstrings`](modules/readmenator._docstrings.py.md) | Multi-style docstring parser for the deterministic API reference. | 2 | 9 | 100.0% |
| [`readmenator._documentation`](modules/readmenator._documentation.py.md) | KNOWLEDGE_BASE.md generator: the human-facing architecture reference. | 1 | 2 | 75.0% |
| [`readmenator._embed`](modules/readmenator._embed.py.md) | Optional semantic embeddings for the readmenator knowledge graph. | 1 | 6 | 100.0% |
| [`readmenator._exclusions`](modules/readmenator._exclusions.py.md) | False-positive exclusion list for readmenator findings. | 2 | 7 | 100.0% |
| [`readmenator._explain`](modules/readmenator._explain.py.md) | Score explanation and path decomposition for the ranking system. | 0 | 2 | 100.0% |
| [`readmenator._explorer`](modules/readmenator._explorer.py.md) | Stdlib explorer HTTP server for the readmenator knowledge graph. | 1 | 7 | 100.0% |
| [`readmenator._exporter`](modules/readmenator._exporter.py.md) | Multi-format exporter for the readmenator knowledge graph. | 1 | 8 | 100.0% |
| [`readmenator._flowcharts`](modules/readmenator._flowcharts.py.md) | Architecture and execution-flow Mermaid diagrams from static structure. | 5 | 24 | 100.0% |
| [`readmenator._flowlayout`](modules/readmenator._flowlayout.py.md) | Flow graph model and deterministic layered layout (Sugiyama style). | 4 | 5 | 100.0% |
| [`readmenator._flowpage`](modules/readmenator._flowpage.py.md) | Interactive SVG viewer for laid-out architecture and execution-flow diagrams. | 0 | 3 | 100.0% |
| [`readmenator._folder_readme`](modules/readmenator._folder_readme.py.md) | Per-folder README.md files for every generated readmenator-* directory. | 2 | 5 | 100.0% |
| [`readmenator._forcegraph`](modules/readmenator._forcegraph.py.md) | Force-graph explorer for the readmenator knowledge graph. | 1 | 15 | 100.0% |
| [`readmenator._forcegraph_page`](modules/readmenator._forcegraph_page.py.md) | HTML page template for the force-graph explorer. | 0 | 0 | 100.0% |
| [`readmenator._gh_wiki`](modules/readmenator._gh_wiki.py.md) | GitHub wiki publisher: mirrors generated knowledge into the repository wiki. | 2 | 7 | 100.0% |
| [`readmenator._gitmeta`](modules/readmenator._gitmeta.py.md) | Read-only git metadata for freshness stamps on generated documents. | 0 | 1 | 100.0% |
| [`readmenator._graphlayout`](modules/readmenator._graphlayout.py.md) | Deterministic graph layout algorithms for animated renders. | 3 | 10 | 100.0% |
| [`readmenator._graphrag`](modules/readmenator._graphrag.py.md) | Zero-token GraphRAG index and retrieval for AI agents. | 10 | 17 | 100.0% |
| [`readmenator._hotspots`](modules/readmenator._hotspots.py.md) | Hotspot, dependency cycle, and change impact analysis. | 1 | 4 | 83.3% |
| [`readmenator._htmlpack`](modules/readmenator._htmlpack.py.md) | Compact JSON payload embedding for self-contained HTML pages. | 0 | 5 | 100.0% |
| [`readmenator._layer_rules`](modules/readmenator._layer_rules.py.md) | Architecture layer rule engine: forbidden and warning edges between layers. | 1 | 3 | 80.0% |
| [`readmenator._layers`](modules/readmenator._layers.py.md) | Architectural layer detection for the readmenator knowledge graph. | 1 | 2 | 100.0% |
| [`readmenator._linter`](modules/readmenator._linter.py.md) | Architecture linter for the readmenator knowledge graph. | 1 | 2 | 75.0% |
| [`readmenator._mcp_server`](modules/readmenator._mcp_server.py.md) | MCP (Model Context Protocol) stdio server for ReadMenator. | 5 | 17 | 8.7% |
| [`readmenator._memory`](modules/readmenator._memory.py.md) | Persistent project memory for agents, generated with zero tokens. | 3 | 10 | 100.0% |
| [`readmenator._mermaid`](modules/readmenator._mermaid.py.md) | Mermaid graph renderer with intelligent pruning. | 1 | 2 | 100.0% |
| [`readmenator._models`](modules/readmenator._models.py.md) | Data model types for the readmenator knowledge graph. | 22 | 1 | 100.0% |
| [`readmenator._ollama`](modules/readmenator._ollama.py.md) | Local Ollama client for optional LLM enrichment. | 1 | 6 | 100.0% |
| [`readmenator._pipeline`](modules/readmenator._pipeline.py.md) | AnalyzerFactory (lazy component construction) and DeepAnalysisRunner. | 2 | 51 | 59.3% |
| [`readmenator._projections`](modules/readmenator._projections.py.md) | Functors and projections for the readmenator code category. | 4 | 11 | 50.0% |
| [`readmenator._provenance`](modules/readmenator._provenance.py.md) | Evidence-provenance audit for readmenator security findings. | 2 | 5 | 100.0% |
| [`readmenator._purpose`](modules/readmenator._purpose.py.md) | Purpose extraction shared by every agent-facing document generator. | 0 | 6 | 100.0% |
| [`readmenator._pytypes`](modules/readmenator._pytypes.py.md) | Lightweight, deterministic receiver typing for Python attribute calls. | 1 | 9 | 100.0% |
| [`readmenator._query`](modules/readmenator._query.py.md) | Query engine for the readmenator knowledge base. | 1 | 7 | 100.0% |
| [`readmenator._rank`](modules/readmenator._rank.py.md) | PageRank, Personalized PageRank, HITS, and composite scoring. | 4 | 11 | 81.2% |
| [`readmenator._readme_injector`](modules/readmenator._readme_injector.py.md) | Injects a knowledge base section into the project README (Markdown or RST). | 1 | 3 | 100.0% |
| [`readmenator._refactorizer`](modules/readmenator._refactorizer.py.md) | Monolithic file refactoring planner for the readmenator knowledge graph. | 1 | 3 | 60.0% |
| [`readmenator._resolver`](modules/readmenator._resolver.py.md) | Import path resolver for the readmenator knowledge graph. | 1 | 3 | 100.0% |
| [`readmenator._rule_gen`](modules/readmenator._rule_gen.py.md) | Suggested linting rule generator producing Semgrep YAML from detected antipatterns. | 1 | 3 | 80.0% |
| [`readmenator._sarif`](modules/readmenator._sarif.py.md) | SARIF v2.1.0 exporter for security findings (GitHub Code Scanning compatible). | 1 | 2 | 75.0% |
| [`readmenator._scanner`](modules/readmenator._scanner.py.md) | Secure polyglot directory traversal and file analysis. | 1 | 3 | 100.0% |
| [`readmenator._scantext`](modules/readmenator._scantext.py.md) | Synthesized scan-text builder for the readmenator knowledge graph. | 1 | 3 | 100.0% |
| [`readmenator._security`](modules/readmenator._security.py.md) | Pattern-based static security analysis for the readmenator knowledge graph. | 2 | 4 | 57.1% |
| [`readmenator._skill_installer`](modules/readmenator._skill_installer.py.md) | Installs the packaged ReadMenator agent skills into a project. | 1 | 6 | 100.0% |
| [`readmenator._sourceview`](modules/readmenator._sourceview.py.md) | Source viewer payload builder for the graph explorers. | 2 | 5 | 100.0% |
| [`readmenator._symindex`](modules/readmenator._symindex.py.md) | Deterministic symbol index with call-site resolution. | 4 | 5 | 100.0% |
| [`readmenator._taint`](modules/readmenator._taint.py.md) | Taint propagation analysis of dangerous imports through the resolved import graph. | 1 | 2 | 75.0% |
| [`readmenator._uml`](modules/readmenator._uml.py.md) | UML class diagram renderer (Mermaid classDiagram) and 12-language stub generator. | 1 | 3 | 20.0% |
| [`readmenator._video`](modules/readmenator._video.py.md) | Cinematic codebase overview video, general purpose. | 2 | 35 | 100.0% |
| [`readmenator._watcher`](modules/readmenator._watcher.py.md) | Filesystem watcher for auto-rebuilding the knowledge base. | 1 | 3 | 100.0% |
| [`readmenator._wiki`](modules/readmenator._wiki.py.md) | Deterministic agent wiki generator for readmenator. | 1 | 4 | 100.0% |
| [`readmenator._yaralite`](modules/readmenator._yaralite.py.md) | Zero-dependency YARA-lite rule parser and runner. | 4 | 4 | 100.0% |

### `readmenator/parsers`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`readmenator.parsers`](modules/readmenator.parsers.__init__.py.md) | Parser factory: maps file extensions to per-language LanguageParser classes. | 0 | 1 | 100.0% |
| [`readmenator.parsers._assembly`](modules/readmenator.parsers._assembly.py.md) | Assembly parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._base`](modules/readmenator.parsers._base.py.md) | LanguageParser base class with shared docstring and signature extraction. | 1 | 2 | 100.0% |
| [`readmenator.parsers._c`](modules/readmenator.parsers._c.py.md) | C and C++ parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._csharp`](modules/readmenator.parsers._csharp.py.md) | C# parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._dart`](modules/readmenator.parsers._dart.py.md) | Dart parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._elixir`](modules/readmenator.parsers._elixir.py.md) | Elixir parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._gdscript`](modules/readmenator.parsers._gdscript.py.md) | GDScript parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._go`](modules/readmenator.parsers._go.py.md) | Go parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._java`](modules/readmenator.parsers._java.py.md) | Java parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._javascript`](modules/readmenator.parsers._javascript.py.md) | JavaScript and TypeScript parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._kotlin`](modules/readmenator.parsers._kotlin.py.md) | Kotlin parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._lua`](modules/readmenator.parsers._lua.py.md) | Lua parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._nim`](modules/readmenator.parsers._nim.py.md) | Nim parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._php`](modules/readmenator.parsers._php.py.md) | PHP parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._python`](modules/readmenator.parsers._python.py.md) | Python parser: native ast extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._ruby`](modules/readmenator.parsers._ruby.py.md) | Ruby parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._rust`](modules/readmenator.parsers._rust.py.md) | Rust parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._scala`](modules/readmenator.parsers._scala.py.md) | Scala parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._shell`](modules/readmenator.parsers._shell.py.md) | Shell parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
| [`readmenator.parsers._swift`](modules/readmenator.parsers._swift.py.md) | Swift parser: regex extraction of symbols, signatures, docstrings, and imports. | 1 | 0 | 100.0% |
