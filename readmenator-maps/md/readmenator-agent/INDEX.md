# Index

| File | Purpose | Subsystem | Symbols | Used by |
|------|---------|-----------|---------|---------|
| `readmenator.py` | Launcher shim that runs the readmenator CLI from a source checkout. | root | 0 | 0 |
| `readmenator/__init__.py` | ReadMenator -- Zero-token polyglot codebase knowledge graph generator. | readmenator | 0 | 0 |
| `readmenator/__main__.py` | Command line entry point: argument parsing and subcommand dispatch. | readmenator | 3 | 1 |
| `readmenator/_agent_injector.py` | Injects KNOWLEDGE_BASE.md references into AI agent instruction files. | readmenator | 14 | 3 |
| `readmenator/_agent_output.py` | Agent-friendly output generator for ReadMenator. | readmenator | 33 | 3 |
| `readmenator/_analytics.py` | Corpus analytics aggregations for the readmenator knowledge graph. | readmenator | 9 | 5 |
| `readmenator/_analyzer.py` | Graph analysis engine for the readmenator knowledge graph. | readmenator | 23 | 5 |
| `readmenator/_app.py` | Application orchestrator: scan, resolve, analyze, and write every output. | readmenator | 73 | 11 |
| `readmenator/_bundlegraph.py` | Edge bundle explorer: circle and sphere hierarchical edge bundling pages. | readmenator | 8 | 3 |
| `readmenator/_bundlegraph_page.py` | HTML page template for the edge bundle explorer. | readmenator | 0 | 1 |
| `readmenator/_cache.py` | File-content hash cache for incremental scanning and analysis caching. | readmenator | 14 | 4 |
| `readmenator/_category.py` | Category theory model for the readmenator code graph. | readmenator | 26 | 9 |
| `readmenator/_concepts.py` | Deterministic semantic concept graph over the structural knowledge graph. | readmenator | 8 | 3 |
| `readmenator/_config.py` | Immutable configuration dataclass for readmenator. | readmenator | 1 | 78 |
| `readmenator/_cpg.py` | Code Property Graph (CPG) generator emitting JSON-LD for AI agents. | readmenator | 6 | 3 |
| `readmenator/_cursorrules_generator.py` | Dynamic .cursorrules generator for the readmenator knowledge graph. | readmenator | 8 | 2 |
| `readmenator/_dataflow.py` | Procedural intra-function dataflow analysis for readmenator. | readmenator | 21 | 2 |
| `readmenator/_dead_code.py` | Dead code detection for the readmenator knowledge graph. | readmenator | 5 | 2 |
| `readmenator/_diagrams.py` | Self-contained interactive system maps for the knowledge graph. | readmenator | 91 | 6 |
| `readmenator/_documentation.py` | KNOWLEDGE_BASE.md generator: the human-facing architecture reference. | readmenator | 31 | 2 |
| `readmenator/_embed.py` | Optional semantic embeddings for the readmenator knowledge graph. | readmenator | 11 | 2 |
| `readmenator/_exclusions.py` | False-positive exclusion list for readmenator findings. | readmenator | 11 | 2 |
| `readmenator/_explain.py` | Score explanation and path decomposition for the ranking system. | readmenator | 3 | 1 |
| `readmenator/_explorer.py` | Stdlib explorer HTTP server for the readmenator knowledge graph. | readmenator | 13 | 2 |
| `readmenator/_exporter.py` | Multi-format exporter for the readmenator knowledge graph. | readmenator | 16 | 3 |
| `readmenator/_forcegraph.py` | Force-graph explorer for the readmenator knowledge graph. | readmenator | 22 | 7 |
| `readmenator/_forcegraph_page.py` | HTML page template for the force-graph explorer. | readmenator | 0 | 1 |
| `readmenator/_gh_wiki.py` | GitHub wiki publisher: mirrors generated knowledge into the repository wiki. | readmenator | 18 | 3 |
| `readmenator/_gitmeta.py` | Read-only git metadata for freshness stamps on generated documents. | readmenator | 4 | 5 |
| `readmenator/_graphlayout.py` | Deterministic graph layout algorithms for animated renders. | readmenator | 18 | 4 |
| `readmenator/_graphrag.py` | Zero-token GraphRAG index and retrieval for AI agents. | readmenator | 53 | 4 |
| `readmenator/_hotspots.py` | Hotspot, dependency cycle, and change impact analysis. | readmenator | 7 | 2 |
| `readmenator/_layer_rules.py` | Architecture layer rule engine: forbidden and warning edges between layers. | readmenator | 4 | 2 |
| `readmenator/_layers.py` | Architectural layer detection for the readmenator knowledge graph. | readmenator | 7 | 6 |
| `readmenator/_linter.py` | Architecture linter for the readmenator knowledge graph. | readmenator | 7 | 2 |
| `readmenator/_mcp_server.py` | MCP (Model Context Protocol) stdio server for ReadMenator. | readmenator | 64 | 3 |
| `readmenator/_memory.py` | Persistent project memory for agents, generated with zero tokens. | readmenator | 30 | 2 |
| `readmenator/_mermaid.py` | Mermaid graph renderer with intelligent pruning. | readmenator | 4 | 2 |
| `readmenator/_models.py` | Data model types for the readmenator knowledge graph. | readmenator | 23 | 90 |
| `readmenator/_pipeline.py` | AnalyzerFactory (lazy component construction) and DeepAnalysisRunner. | readmenator | 46 | 1 |
| `readmenator/_projections.py` | Functors and projections for the readmenator code category. | readmenator | 15 | 1 |
| `readmenator/_provenance.py` | Evidence-provenance audit for readmenator security findings. | readmenator | 10 | 2 |
| `readmenator/_purpose.py` | Purpose extraction shared by every agent-facing document generator. | readmenator | 7 | 6 |
| `readmenator/_query.py` | Query engine for the readmenator knowledge base. | readmenator | 17 | 3 |
| `readmenator/_rank.py` | PageRank, Personalized PageRank, HITS, and composite scoring. | readmenator | 18 | 10 |
| `readmenator/_readme_injector.py` | Injects a knowledge base section into the project README (Markdown or RST). | readmenator | 8 | 4 |
| `readmenator/_refactorizer.py` | Monolithic file refactoring planner for the readmenator knowledge graph. | readmenator | 9 | 2 |
| `readmenator/_resolver.py` | Import path resolver for the readmenator knowledge graph. | readmenator | 17 | 7 |
| `readmenator/_rule_gen.py` | Suggested linting rule generator producing Semgrep YAML from detected antipatterns. | readmenator | 9 | 2 |
| `readmenator/_sarif.py` | SARIF v2.1.0 exporter for security findings (GitHub Code Scanning compatible). | readmenator | 5 | 2 |
| `readmenator/_scanner.py` | Secure polyglot directory traversal and file analysis. | readmenator | 14 | 4 |
| `readmenator/_scantext.py` | Synthesized scan-text builder for the readmenator knowledge graph. | readmenator | 4 | 2 |
| `readmenator/_security.py` | Pattern-based static security analysis for the readmenator knowledge graph. | readmenator | 32 | 4 |
| `readmenator/_skill_installer.py` | Installs the packaged ReadMenator agent skills into a project. | readmenator | 7 | 2 |
| `readmenator/_taint.py` | Taint propagation analysis of dangerous imports through the resolved import graph. | readmenator | 6 | 3 |
| `readmenator/_uml.py` | UML class diagram renderer (Mermaid classDiagram) and 12-language stub generator. | readmenator | 25 | 4 |
| `readmenator/_vendor/force-graph.min.js` | Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph | misc | 35 | 0 |
| `readmenator/_video.py` | Cinematic codebase overview video, general purpose. | readmenator | 76 | 3 |
| `readmenator/_watcher.py` | Filesystem watcher for auto-rebuilding the knowledge base. | readmenator | 5 | 1 |
| `readmenator/_wiki.py` | Deterministic agent wiki generator for readmenator. | readmenator | 32 | 2 |
| `readmenator/_yaralite.py` | Zero-dependency YARA-lite rule parser and runner. | readmenator | 20 | 2 |
| `readmenator/parsers/__init__.py` | Parser factory: maps file extensions to per-language LanguageParser classes. | parsers | 2 | 3 |
| `readmenator/parsers/_assembly.py` | Assembly parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 1 |
| `readmenator/parsers/_base.py` | LanguageParser base class with shared docstring and signature extraction. | parsers | 6 | 20 |
| `readmenator/parsers/_c.py` | C and C++ parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 3 | 2 |
| `readmenator/parsers/_csharp.py` | C# parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_dart.py` | Dart parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_elixir.py` | Elixir parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_gdscript.py` | GDScript parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_go.py` | Go parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_java.py` | Java parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_javascript.py` | JavaScript and TypeScript parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_kotlin.py` | Kotlin parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_lua.py` | Lua parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_nim.py` | Nim parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_php.py` | PHP parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_python.py` | Python parser: native ast extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_ruby.py` | Ruby parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_rust.py` | Rust parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_scala.py` | Scala parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_shell.py` | Shell parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator/parsers/_swift.py` | Swift parser: regex extraction of symbols, signatures, docstrings, and imports. | parsers | 2 | 2 |
| `readmenator_orchestrator.py` | test_rebuild_command_includes_full_concept_layer: The orchestrator must force a full rebuild... | root | 37 | 0 |
| `tests/__init__.py` | - | tests | 0 | 0 |
| `tests/test_agent_friendliness.py` | Contract tests for agent-facing output quality: budgets, purposes, freshness, noise. | tests | 58 | 0 |
| `tests/test_agent_injector.py` | Contract tests for AI agent file injection. | tests | 38 | 0 |
| `tests/test_agent_output.py` | - | tests | 45 | 0 |
| `tests/test_analyzer.py` | Contract tests for the GraphAnalyzer. | tests | 14 | 0 |
| `tests/test_bundlegraph.py` | Contract tests for the edge bundle explorer (circle and sphere views). | tests | 27 | 0 |
| `tests/test_cache.py` | Contract tests for the FileCache. | tests | 22 | 0 |
| `tests/test_concepts.py` | test_concept_nouns_map_to_file_sets: Noun tokens become concepts mapping to file sets. | tests | 8 | 0 |
| `tests/test_config.py` | - | tests | 6 | 0 |
| `tests/test_cpg.py` | TestCodePropertyGraphContract: Contract: CodePropertyGraph generates valid JSON-LD CPG output. | tests | 11 | 0 |
| `tests/test_cursorrules.py` | Contract tests for the CursorRulesGenerator. | tests | 12 | 0 |
| `tests/test_dataflow.py` | - | tests | 47 | 0 |
| `tests/test_dead_code.py` | Contract tests for the DeadCodeStripper. | tests | 15 | 0 |
| `tests/test_diagrams.py` | Contract tests for interactive system maps. | tests | 72 | 0 |
| `tests/test_documentation.py` | - | tests | 29 | 0 |
| `tests/test_exporter.py` | Contract tests for the GraphExporter. | tests | 15 | 0 |
| `tests/test_gh_wiki.py` | Contract tests for the GitHub wiki publisher (no network: git/gh calls are faked). | tests | 17 | 0 |
| `tests/test_graphlayout.py` | Contract tests for ForceAtlas2 and hierarchical edge bundling layouts. | tests | 33 | 0 |
| `tests/test_graphrag.py` | Contract tests for the zero-token GraphRAG index and retrieval. | tests | 28 | 0 |
| `tests/test_hotspots.py` | TestHotspotAnalyzerContract: Contract: HotspotAnalyzer detects hotspots, cycles, and change impact. | tests | 11 | 0 |
| `tests/test_integration.py` | - | tests | 16 | 0 |
| `tests/test_interactive_graph.py` | Contract tests for the interactive explorer modules. | tests | 60 | 0 |
| `tests/test_layer_rules.py` | TestLayerRuleEngineContract: Contract: LayerRuleEngine detects architectural layer violations. | tests | 13 | 0 |
| `tests/test_linter.py` | Contract tests for the ArchitectureLinter. | tests | 14 | 0 |
| `tests/test_mcp_server.py` | Contract tests for the MCP server protocol and tool dispatch. | tests | 25 | 0 |
| `tests/test_memory.py` | Contract tests for project memory, the session log, and agent skills. | tests | 17 | 0 |
| `tests/test_mermaid.py` | - | tests | 11 | 0 |
| `tests/test_models.py` | - | tests | 11 | 0 |
| `tests/test_parsers.py` | - | tests | 87 | 0 |
| `tests/test_parsers_new.py` | Contract tests for the 6 new language parsers. | tests | 36 | 0 |
| `tests/test_parsers_property.py` | Property-based contract tests for all 19 language parsers. | tests | 27 | 0 |
| `tests/test_query.py` | - | tests | 18 | 0 |
| `tests/test_ranking.py` | Contract tests for the category theory and ranking system. | tests | 72 | 0 |
| `tests/test_readme_injector.py` | Contract tests for README injection into documented projects. | tests | 26 | 0 |
| `tests/test_refactorizer.py` | Contract tests for the MonolithRefactorizer. | tests | 17 | 0 |
| `tests/test_resolver.py` | Contract tests for the ImportResolver. | tests | 22 | 0 |
| `tests/test_rule_gen.py` | TestRuleGeneratorContract: Contract: RuleGenerator detects patterns and suggests rules. | tests | 10 | 0 |
| `tests/test_sarif.py` | TestSarifExporterContract: Contract: SarifExporter produces valid SARIF v2.1.0 JSON. | tests | 10 | 0 |
| `tests/test_scanner.py` | - | tests | 21 | 0 |
| `tests/test_security.py` | Contract tests for the static security analysis module. | tests | 68 | 0 |
| `tests/test_taint.py` | TestTaintAnalyzerContract: Contract: TaintAnalyzer discovers taint propagation paths. | tests | 10 | 0 |
| `tests/test_taint_bdd.py` | BDD-style contract tests for taint propagation analysis. | tests | 26 | 0 |
| `tests/test_uml.py` | Contract tests for UML class diagram generation and language code generation. | tests | 49 | 0 |
| `tests/test_video.py` | Contract tests for the cinematic overview video renderer. | tests | 18 | 0 |
| `tests/test_wiki.py` | - | tests | 30 | 0 |
