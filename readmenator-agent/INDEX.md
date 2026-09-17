# Index

| File | Purpose | Subsystem | Symbols |
|------|---------|-----------|---------|
| `.refactor__app.sh` | Refactoring plan for readmenator/_app.py Current lines: 643 Estimated impact: 5  | root | 0 |
| `.refactor__documentation.sh` | Refactoring plan for readmenator/_documentation.py Current lines: 1087 Estimated | root | 0 |
| `.refactor__exporter.sh` | Refactoring plan for readmenator/_exporter.py Current lines: 898 Estimated impac | root | 0 |
| `.refactor__mcp_server.sh` | Refactoring plan for readmenator/_mcp_server.py Current lines: 813 Estimated imp | root | 0 |
| `.refactor__rank.sh` | Refactoring plan for readmenator/_rank.py Current lines: 537 Estimated impact: 7 | root | 0 |
| `.refactor__security.sh` | Refactoring plan for readmenator/_security.py Current lines: 583 Estimated impac | root | 0 |
| `.refactor__uml.sh` | Refactoring plan for readmenator/_uml.py Current lines: 599 Estimated impact: 4  | root | 0 |
| `.refactor_test_parsers.sh` | Refactoring plan for tests/test_parsers.py Current lines: 487 Estimated impact:  | root | 0 |
| `.refactor_test_ranking.sh` | Refactoring plan for tests/test_ranking.py Current lines: 666 Estimated impact:  | root | 0 |
| `.refactor_test_uml.sh` | Refactoring plan for tests/test_uml.py Current lines: 488 Estimated impact: 0 fi | root | 0 |
| `readmenator.py` | - | root | 0 |
| `readmenator/__init__.py` | ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public A | readmenator | 0 |
| `readmenator/__main__.py` | - | readmenator | 3 |
| `readmenator/_agent_injector.py` | Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects c | readmenator | 14 |
| `readmenator/_agent_output.py` | Agent-friendly output generator for ReadMenator.  Generates grep-optimized, flat | readmenator | 18 |
| `readmenator/_analyzer.py` | Graph analysis engine for the readmenator knowledge graph.  Provides community d | readmenator | 14 |
| `readmenator/_app.py` | - | readmenator | 44 |
| `readmenator/_cache.py` | File-content hash cache for incremental scanning and analysis caching.  Computes | readmenator | 13 |
| `readmenator/_category.py` | Category theory model for the readmenator code graph.  Defines typed morphisms ( | readmenator | 26 |
| `readmenator/_config.py` | Immutable configuration dataclass for readmenator.  All tuneable parameters live | readmenator | 1 |
| `readmenator/_cpg.py` | - | readmenator | 6 |
| `readmenator/_cursorrules_generator.py` | Dynamic .cursorrules generator for the readmenator knowledge graph.  Reads archi | readmenator | 8 |
| `readmenator/_dataflow.py` | Procedural intra-function dataflow analysis for readmenator.  Detects classic lo | readmenator | 21 |
| `readmenator/_dead_code.py` | Dead code detection for the readmenator knowledge graph.  Identifies orphaned sy | readmenator | 5 |
| `readmenator/_diagrams.py` | Self-contained interactive system maps for the knowledge graph.  Builds typed in | readmenator | 67 |
| `readmenator/_documentation.py` | - | readmenator | 28 |
| `readmenator/_explain.py` | Score explanation and path decomposition for the ranking system.  Provides human | readmenator | 3 |
| `readmenator/_exporter.py` | Multi-format exporter for the readmenator knowledge graph.  Produces JSON (Graph | readmenator | 15 |
| `readmenator/_hotspots.py` | - | readmenator | 7 |
| `readmenator/_layer_rules.py` | - | readmenator | 4 |
| `readmenator/_layers.py` | Architectural layer detection for the readmenator knowledge graph.  Infers archi | readmenator | 4 |
| `readmenator/_linter.py` | Architecture linter for the readmenator knowledge graph.  Evaluates files agains | readmenator | 7 |
| `readmenator/_mcp_server.py` | MCP (Model Context Protocol) stdio server for ReadMenator.  Exposes the full cod | readmenator | 52 |
| `readmenator/_mermaid.py` | Mermaid graph renderer with intelligent pruning.  Converts the internal Node/Edg | readmenator | 4 |
| `readmenator/_models.py` | Data model types for the readmenator knowledge graph.  Defines the core entity t | readmenator | 20 |
| `readmenator/_pipeline.py` | - | readmenator | 32 |
| `readmenator/_projections.py` | Functors and projections for the readmenator code category.  Defines projection  | readmenator | 15 |
| `readmenator/_query.py` | Query engine for the readmenator knowledge base.  Supports natural-language-like | readmenator | 17 |
| `readmenator/_rank.py` | PageRank, Personalized PageRank, HITS, and composite scoring.  Provides typed-gr | readmenator | 17 |
| `readmenator/_readme_injector.py` | - | readmenator | 8 |
| `readmenator/_refactorizer.py` | Monolithic file refactoring planner for the readmenator knowledge graph.  Identi | readmenator | 9 |
| `readmenator/_resolver.py` | Import path resolver for the readmenator knowledge graph.  Maps raw import strin | readmenator | 16 |
| `readmenator/_rule_gen.py` | - | readmenator | 9 |
| `readmenator/_sarif.py` | - | readmenator | 5 |
| `readmenator/_scanner.py` | Secure polyglot directory traversal and file analysis.  The scanner walks a dire | readmenator | 13 |
| `readmenator/_security.py` | Pattern-based static security analysis for the readmenator knowledge graph.  Sca | readmenator | 32 |
| `readmenator/_taint.py` | - | readmenator | 6 |
| `readmenator/_uml.py` | - | readmenator | 25 |
| `readmenator/_watcher.py` | Filesystem watcher for auto-rebuilding the knowledge base.  Monitors the project | readmenator | 5 |
| `readmenator/_wiki.py` | Deterministic agent wiki generator for readmenator.  Builds a navigable, progres | readmenator | 34 |
| `readmenator/parsers/__init__.py` | - | parsers | 2 |
| `readmenator/parsers/_assembly.py` | - | parsers | 2 |
| `readmenator/parsers/_base.py` | - | parsers | 6 |
| `readmenator/parsers/_c.py` | - | parsers | 3 |
| `readmenator/parsers/_csharp.py` | - | parsers | 2 |
| `readmenator/parsers/_dart.py` | - | parsers | 2 |
| `readmenator/parsers/_elixir.py` | - | parsers | 2 |
| `readmenator/parsers/_gdscript.py` | - | parsers | 2 |
| `readmenator/parsers/_go.py` | - | parsers | 2 |
| `readmenator/parsers/_java.py` | - | parsers | 2 |
| `readmenator/parsers/_javascript.py` | - | parsers | 2 |
| `readmenator/parsers/_kotlin.py` | - | parsers | 2 |
| `readmenator/parsers/_lua.py` | - | parsers | 2 |
| `readmenator/parsers/_nim.py` | - | parsers | 2 |
| `readmenator/parsers/_php.py` | - | parsers | 2 |
| `readmenator/parsers/_python.py` | - | parsers | 2 |
| `readmenator/parsers/_ruby.py` | - | parsers | 2 |
| `readmenator/parsers/_rust.py` | - | parsers | 2 |
| `readmenator/parsers/_scala.py` | - | parsers | 2 |
| `readmenator/parsers/_shell.py` | - | parsers | 2 |
| `readmenator/parsers/_swift.py` | - | parsers | 2 |
| `readmenator_orchestrator.py` | - | root | 34 |
| `tests/__init__.py` | - | tests | 0 |
| `tests/test_agent_injector.py` | Contract tests for AI agent file injection.  SDD + TDD + BDD: Each test validate | tests | 38 |
| `tests/test_agent_output.py` | - | tests | 45 |
| `tests/test_analyzer.py` | Contract tests for the GraphAnalyzer.  Validates community detection, god node c | tests | 14 |
| `tests/test_cache.py` | Contract tests for the FileCache.  Validates SHA256 hashing, cache persistence,  | tests | 22 |
| `tests/test_config.py` | - | tests | 6 |
| `tests/test_cpg.py` | - | tests | 11 |
| `tests/test_cursorrules.py` | Contract tests for the CursorRulesGenerator.  Validates base rule generation, la | tests | 12 |
| `tests/test_dataflow.py` | - | tests | 47 |
| `tests/test_dead_code.py` | Contract tests for the DeadCodeStripper.  Validates dead code detection, in-degr | tests | 15 |
| `tests/test_diagrams.py` | Contract tests for interactive system maps.  Validates typed intermediate repres | tests | 69 |
| `tests/test_documentation.py` | - | tests | 29 |
| `tests/test_exporter.py` | Contract tests for the GraphExporter.  Validates JSON, HTML, and SVG export form | tests | 15 |
| `tests/test_hotspots.py` | - | tests | 11 |
| `tests/test_integration.py` | - | tests | 16 |
| `tests/test_layer_rules.py` | - | tests | 13 |
| `tests/test_linter.py` | Contract tests for the ArchitectureLinter.  Validates file length checks, cross- | tests | 14 |
| `tests/test_mcp_server.py` | Contract tests for the MCP server protocol and tool dispatch.  Validates JSON-RP | tests | 25 |
| `tests/test_mermaid.py` | - | tests | 11 |
| `tests/test_models.py` | - | tests | 11 |
| `tests/test_parsers.py` | - | tests | 87 |
| `tests/test_parsers_new.py` | Contract tests for the 6 new language parsers.  Validates that Ruby, Swift, Kotl | tests | 36 |
| `tests/test_parsers_property.py` | Property-based contract tests for all 19 language parsers.  Uses Hypothesis to g | tests | 27 |
| `tests/test_query.py` | - | tests | 18 |
| `tests/test_ranking.py` | Contract tests for the category theory and ranking system.  Tests cover: - EdgeK | tests | 72 |
| `tests/test_readme_injector.py` | Contract tests for README injection into documented projects.  SDD + TDD + BDD:  | tests | 26 |
| `tests/test_refactorizer.py` | Contract tests for the MonolithRefactorizer.  Validates monolithic file detectio | tests | 17 |
| `tests/test_resolver.py` | Contract tests for the ImportResolver.  Validates that import strings from vario | tests | 22 |
| `tests/test_rule_gen.py` | - | tests | 10 |
| `tests/test_sarif.py` | - | tests | 10 |
| `tests/test_scanner.py` | - | tests | 21 |
| `tests/test_security.py` | Contract tests for the static security analysis module.  Tests cover the Securit | tests | 68 |
| `tests/test_taint.py` | - | tests | 10 |
| `tests/test_taint_bdd.py` | BDD-style contract tests for taint propagation analysis.  Uses pytest-bdd scenar | tests | 26 |
| `tests/test_uml.py` | Contract tests for UML class diagram generation and language code generation.  S | tests | 49 |
| `tests/test_wiki.py` | - | tests | 30 |
