# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 32 | **Total Symbols Extracted:** 456 | **Total Imports:** 169
 | **Resolved Imports:** 61


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [God Nodes](#god-nodes)
4. [Community Analysis](#community-analysis)
5. [Surprising Connections](#surprising-connections)
6. [Suggested Questions](#suggested-questions)
7. [Structural Knowledge Map](#structural-knowledge-map)
8. [Architecture Reference](#architecture-reference)
    - [PY (32 files)](#py-32-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 32 |
| Total Symbols | 456 |
| Total Imports | 2622 |
| Languages | 1 |
| Avg Symbols/File | 14.2 |
| Avg Imports/File | 81.9 |
| Resolved Imports | 61 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| testing | 16 |
| utility | 12 |
| infrastructure | 2 |
| business_logic | 1 |
| data_access | 1 |

### utility

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `_analyzer.py` (py, 13 symbols)
- `_app.py` (py, 22 symbols)
- `_documentation.py` (py, 12 symbols)
- `_exporter.py` (py, 13 symbols)
- `_layers.py` (py, 5 symbols)
- `_mermaid.py` (py, 4 symbols)
- `_parsers.py` (py, 45 symbols)
- `_resolver.py` (py, 11 symbols)
- `_scanner.py` (py, 8 symbols)
- `_watcher.py` (py, 5 symbols)

### testing

- `__main__.py` (py, 3 symbols)
- `readmenator_orchestrator.py` (py, 30 symbols)
- `__init__.py` (py, 0 symbols)
- `test_analyzer.py` (py, 12 symbols)
- `test_cache.py` (py, 15 symbols)
- `test_config.py` (py, 6 symbols)
- `test_documentation.py` (py, 15 symbols)
- `test_exporter.py` (py, 15 symbols)
- `test_integration.py` (py, 11 symbols)
- `test_mermaid.py` (py, 11 symbols)
- `test_models.py` (py, 11 symbols)
- `test_parsers.py` (py, 84 symbols)
- `test_parsers_new.py` (py, 36 symbols)
- `test_query.py` (py, 18 symbols)
- `test_resolver.py` (py, 11 symbols)
- *... and 1 more*

### infrastructure

- `_cache.py` (py, 8 symbols)
- `_config.py` (py, 1 symbols)

### business_logic

- `_models.py` (py, 6 symbols)

### data_access

- `_query.py` (py, 13 symbols)

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections |
|------|-------|-------------|
| `_config.py` | 40.1 | |
| `_models.py` | 32.6 | |
| `_app.py` | 30.2 | |
| `_parsers.py` | 14.5 | |
| `test_parsers.py` | 12.4 | |
| `_documentation.py` | 11.2 | |
| `_scanner.py` | 10.8 | |
| `_analyzer.py` | 9.3 | |
| `_exporter.py` | 9.3 | |
| `_mermaid.py` | 8.4 | |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### readmenator (Cohesion: 0.98)

**28 files** in this community:

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `__main__.py` (py, 3 symbols)
- `_analyzer.py` (py, 13 symbols)
- `_app.py` (py, 22 symbols)
- `_cache.py` (py, 8 symbols)
- `_config.py` (py, 1 symbols)
- `_documentation.py` (py, 12 symbols)
- `_exporter.py` (py, 13 symbols)
- `_layers.py` (py, 5 symbols)
- `_mermaid.py` (py, 4 symbols)
- `_models.py` (py, 6 symbols)
- `_parsers.py` (py, 45 symbols)
- `_query.py` (py, 13 symbols)
- `_scanner.py` (py, 8 symbols)
- `_watcher.py` (py, 5 symbols)
- `test_analyzer.py` (py, 12 symbols)
- `test_cache.py` (py, 15 symbols)
- `test_config.py` (py, 6 symbols)
- `test_documentation.py` (py, 15 symbols)
- ... and 8 more files

### readmenator (Cohesion: 0.50)

**2 files** in this community:

- `_resolver.py` (py, 11 symbols)
- `test_resolver.py` (py, 11 symbols)

---

## Surprising Connections

Files in different communities connected through 3+ indirect hops.

- `_mermaid.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `_parsers.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `readmenator.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `test_analyzer.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `test_cache.py` <-> `test_resolver.py` (4 hops, across 2 communities)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does _config.py depend on, and what depends on it? (20 connections)
- What does _models.py depend on, and what depends on it? (16 connections)
- What does _app.py depend on, and what depends on it? (14 connections)
- How are the 28 files in 'readmenator' related to each other?
- Why are _mermaid.py and test_resolver.py connected through 4 hops across 2 communities?

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_0 ["readmenator"]
    readmenator__app_py["_app.py (py)"]
    class readmenator__app_py mod;
    readmenator__app_py_readmenatorApplication["readmenatorApplication"]
    class readmenator__app_py_readmenatorApplication cls;
    readmenator__app_py --> readmenator__app_py_readmenatorApplication
    readmenator__app_py___init__["__init__"]
    class readmenator__app_py___init__ fn;
    readmenator__app_py --> readmenator__app_py___init__
    readmenator__app_py__scan["_scan"]
    class readmenator__app_py__scan fn;
    readmenator__app_py --> readmenator__app_py__scan
    readmenator__app_py__resolve_imports["_resolve_imports"]
    class readmenator__app_py__resolve_imports fn;
    readmenator__app_py --> readmenator__app_py__resolve_imports
    readmenator__app_py_run["run"]
    class readmenator__app_py_run fn;
    readmenator__app_py --> readmenator__app_py_run
    readmenator_orchestrator_py["readmenator_orchestrator.py (py)"]
    class readmenator_orchestrator_py mod;
    readmenator_orchestrator_py_Config["Config"]
    class readmenator_orchestrator_py_Config cls;
    readmenator_orchestrator_py --> readmenator_orchestrator_py_Config
    readmenator_orchestrator_py_GitHubClient["GitHubClient"]
    class readmenator_orchestrator_py_GitHubClient cls;
    readmenator_orchestrator_py --> readmenator_orchestrator_py_GitHubClient
    readmenator_orchestrator_py_RepositoryProcessor["RepositoryProcessor"]
    class readmenator_orchestrator_py_RepositoryProcessor cls;
    readmenator_orchestrator_py --> readmenator_orchestrator_py_RepositoryProcessor
    readmenator_orchestrator_py_Orchestrator["Orchestrator"]
    class readmenator_orchestrator_py_Orchestrator cls;
    readmenator_orchestrator_py --> readmenator_orchestrator_py_Orchestrator
    readmenator_orchestrator_py_TestOrchestrator["TestOrchestrator"]
    class readmenator_orchestrator_py_TestOrchestrator cls;
    readmenator_orchestrator_py --> readmenator_orchestrator_py_TestOrchestrator
    readmenator__exporter_py["_exporter.py (py)"]
    class readmenator__exporter_py mod;
    readmenator__exporter_py_GraphExporter["GraphExporter"]
    class readmenator__exporter_py_GraphExporter cls;
    readmenator__exporter_py --> readmenator__exporter_py_GraphExporter
    readmenator__exporter_py___init__["__init__"]
    class readmenator__exporter_py___init__ fn;
    readmenator__exporter_py --> readmenator__exporter_py___init__
    readmenator__exporter_py_to_json["to_json"]
    class readmenator__exporter_py_to_json fn;
    readmenator__exporter_py --> readmenator__exporter_py_to_json
    readmenator__exporter_py_to_html["to_html"]
    class readmenator__exporter_py_to_html fn;
    readmenator__exporter_py --> readmenator__exporter_py_to_html
    readmenator__exporter_py__community_color_map["_community_color_map"]
    class readmenator__exporter_py__community_color_map fn;
    readmenator__exporter_py --> readmenator__exporter_py__community_color_map
    tests_test_cache_py["test_cache.py (py)"]
    class tests_test_cache_py mod;
    tests_test_cache_py_TestFileCacheContract["TestFileCacheContract"]
    class tests_test_cache_py_TestFileCacheContract cls;
    tests_test_cache_py --> tests_test_cache_py_TestFileCacheContract
    tests_test_cache_py_setUp["setUp"]
    class tests_test_cache_py_setUp fn;
    tests_test_cache_py --> tests_test_cache_py_setUp
    tests_test_cache_py_tearDown["tearDown"]
    class tests_test_cache_py_tearDown fn;
    tests_test_cache_py --> tests_test_cache_py_tearDown
    tests_test_cache_py__write["_write"]
    class tests_test_cache_py__write fn;
    tests_test_cache_py --> tests_test_cache_py__write
    tests_test_cache_py_test_compute_hash_returns_hex_string["test_compute_hash_returns_hex_string"]
    class tests_test_cache_py_test_compute_hash_returns_hex_string fn;
    tests_test_cache_py --> tests_test_cache_py_test_compute_hash_returns_hex_string
    readmenator__parsers_py["_parsers.py (py)"]
    class readmenator__parsers_py mod;
    readmenator__parsers_py_LanguageParser["LanguageParser"]
    class readmenator__parsers_py_LanguageParser cls;
    readmenator__parsers_py --> readmenator__parsers_py_LanguageParser
    readmenator__parsers_py_CParser["CParser"]
    class readmenator__parsers_py_CParser cls;
    readmenator__parsers_py --> readmenator__parsers_py_CParser
    readmenator__parsers_py_PythonParser["PythonParser"]
    class readmenator__parsers_py_PythonParser cls;
    readmenator__parsers_py --> readmenator__parsers_py_PythonParser
    readmenator__parsers_py_GoParser["GoParser"]
    class readmenator__parsers_py_GoParser cls;
    readmenator__parsers_py --> readmenator__parsers_py_GoParser
    readmenator__parsers_py_RustParser["RustParser"]
    class readmenator__parsers_py_RustParser cls;
    readmenator__parsers_py --> readmenator__parsers_py_RustParser
    tests_test_exporter_py["test_exporter.py (py)"]
    class tests_test_exporter_py mod;
    tests_test_exporter_py_TestGraphExporterContract["TestGraphExporterContract"]
    class tests_test_exporter_py_TestGraphExporterContract cls;
    tests_test_exporter_py --> tests_test_exporter_py_TestGraphExporterContract
    tests_test_exporter_py_setUp["setUp"]
    class tests_test_exporter_py_setUp fn;
    tests_test_exporter_py --> tests_test_exporter_py_setUp
    tests_test_exporter_py__make_node["_make_node"]
    class tests_test_exporter_py__make_node fn;
    tests_test_exporter_py --> tests_test_exporter_py__make_node
    tests_test_exporter_py__make_sym["_make_sym"]
    class tests_test_exporter_py__make_sym fn;
    tests_test_exporter_py --> tests_test_exporter_py__make_sym
    tests_test_exporter_py_test_to_json_produces_valid_json["test_to_json_produces_valid_json"]
    class tests_test_exporter_py_test_to_json_produces_valid_json fn;
    tests_test_exporter_py --> tests_test_exporter_py_test_to_json_produces_valid_json
    readmenator__analyzer_py["_analyzer.py (py)"]
    class readmenator__analyzer_py mod;
    readmenator__analyzer_py_GraphAnalyzer["GraphAnalyzer"]
    class readmenator__analyzer_py_GraphAnalyzer cls;
    readmenator__analyzer_py --> readmenator__analyzer_py_GraphAnalyzer
    readmenator__analyzer_py___init__["__init__"]
    class readmenator__analyzer_py___init__ fn;
    readmenator__analyzer_py --> readmenator__analyzer_py___init__
    readmenator__analyzer_py_analyze["analyze"]
    class readmenator__analyzer_py_analyze fn;
    readmenator__analyzer_py --> readmenator__analyzer_py_analyze
    readmenator__analyzer_py__build_adjacency["_build_adjacency"]
    class readmenator__analyzer_py__build_adjacency fn;
    readmenator__analyzer_py --> readmenator__analyzer_py__build_adjacency
    readmenator__analyzer_py__build_reverse_adjacency["_build_reverse_adjacency"]
    class readmenator__analyzer_py__build_reverse_adjacency fn;
    readmenator__analyzer_py --> readmenator__analyzer_py__build_reverse_adjacency
    readmenator__documentation_py["_documentation.py (py)"]
    class readmenator__documentation_py mod;
    readmenator__documentation_py_DocumentationGenerator["DocumentationGenerator"]
    class readmenator__documentation_py_DocumentationGenerator cls;
    readmenator__documentation_py --> readmenator__documentation_py_DocumentationGenerator
    readmenator__documentation_py___init__["__init__"]
    class readmenator__documentation_py___init__ fn;
    readmenator__documentation_py --> readmenator__documentation_py___init__
    readmenator__documentation_py_generate["generate"]
    class readmenator__documentation_py_generate fn;
    readmenator__documentation_py --> readmenator__documentation_py_generate
    readmenator__documentation_py__build_toc["_build_toc"]
    class readmenator__documentation_py__build_toc fn;
    readmenator__documentation_py --> readmenator__documentation_py__build_toc
    readmenator__documentation_py__build_layers["_build_layers"]
    class readmenator__documentation_py__build_layers fn;
    readmenator__documentation_py --> readmenator__documentation_py__build_layers
    tests_test_scanner_py["test_scanner.py (py)"]
    class tests_test_scanner_py mod;
    tests_test_scanner_py_TestScannerContract["TestScannerContract"]
    class tests_test_scanner_py_TestScannerContract cls;
    tests_test_scanner_py --> tests_test_scanner_py_TestScannerContract
    tests_test_scanner_py_setUp["setUp"]
    class tests_test_scanner_py_setUp fn;
    tests_test_scanner_py --> tests_test_scanner_py_setUp
    tests_test_scanner_py_tearDown["tearDown"]
    class tests_test_scanner_py_tearDown fn;
    tests_test_scanner_py --> tests_test_scanner_py_tearDown
    tests_test_scanner_py__write["_write"]
    class tests_test_scanner_py__write fn;
    tests_test_scanner_py --> tests_test_scanner_py__write
    tests_test_scanner_py_test_scans_python_files["test_scans_python_files"]
    class tests_test_scanner_py_test_scans_python_files fn;
    tests_test_scanner_py --> tests_test_scanner_py_test_scans_python_files
    readmenator__scanner_py["_scanner.py (py)"]
    class readmenator__scanner_py mod;
    readmenator__scanner_py_PolyglotScanner["PolyglotScanner"]
    class readmenator__scanner_py_PolyglotScanner cls;
    readmenator__scanner_py --> readmenator__scanner_py_PolyglotScanner
    readmenator__scanner_py___init__["__init__"]
    class readmenator__scanner_py___init__ fn;
    readmenator__scanner_py --> readmenator__scanner_py___init__
    readmenator__scanner_py__is_ignored["_is_ignored"]
    class readmenator__scanner_py__is_ignored fn;
    readmenator__scanner_py --> readmenator__scanner_py__is_ignored
    readmenator__scanner_py__validate_path_security["_validate_path_security"]
    class readmenator__scanner_py__validate_path_security fn;
    readmenator__scanner_py --> readmenator__scanner_py__validate_path_security
    readmenator__scanner_py__check_directory_depth["_check_directory_depth"]
    class readmenator__scanner_py__check_directory_depth fn;
    readmenator__scanner_py --> readmenator__scanner_py__check_directory_depth
    tests_test_analyzer_py["test_analyzer.py (py)"]
    class tests_test_analyzer_py mod;
    tests_test_analyzer_py_TestGraphAnalyzerContract["TestGraphAnalyzerContract"]
    class tests_test_analyzer_py_TestGraphAnalyzerContract cls;
    tests_test_analyzer_py --> tests_test_analyzer_py_TestGraphAnalyzerContract
    tests_test_analyzer_py_setUp["setUp"]
    class tests_test_analyzer_py_setUp fn;
    tests_test_analyzer_py --> tests_test_analyzer_py_setUp
    tests_test_analyzer_py__make_node["_make_node"]
    class tests_test_analyzer_py__make_node fn;
    tests_test_analyzer_py --> tests_test_analyzer_py__make_node
    tests_test_analyzer_py__make_edge["_make_edge"]
    class tests_test_analyzer_py__make_edge fn;
    tests_test_analyzer_py --> tests_test_analyzer_py__make_edge
    tests_test_analyzer_py_test_analyze_empty_graph_returns_empty_result["test_analyze_empty_graph_returns_empty_result"]
    class tests_test_analyzer_py_test_analyze_empty_graph_returns_empty_result fn;
    tests_test_analyzer_py --> tests_test_analyzer_py_test_analyze_empty_graph_returns_empty_result
    tests_test_integration_py["test_integration.py (py)"]
    class tests_test_integration_py mod;
    tests_test_integration_py_TestEndToEndContract["TestEndToEndContract"]
    class tests_test_integration_py_TestEndToEndContract cls;
    tests_test_integration_py --> tests_test_integration_py_TestEndToEndContract
    tests_test_integration_py_setUp["setUp"]
    class tests_test_integration_py_setUp fn;
    tests_test_integration_py --> tests_test_integration_py_setUp
    tests_test_integration_py_tearDown["tearDown"]
    class tests_test_integration_py_tearDown fn;
    tests_test_integration_py --> tests_test_integration_py_tearDown
    tests_test_integration_py__write["_write"]
    class tests_test_integration_py__write fn;
    tests_test_integration_py --> tests_test_integration_py__write
    tests_test_integration_py_test_full_pipeline_generates_knowledge_base["test_full_pipeline_generates_knowledge_base"]
    class tests_test_integration_py_test_full_pipeline_generates_knowledge_base fn;
    tests_test_integration_py --> tests_test_integration_py_test_full_pipeline_generates_knowledge_base
    readmenator__cache_py["_cache.py (py)"]
    class readmenator__cache_py mod;
    readmenator__cache_py_FileCache["FileCache"]
    class readmenator__cache_py_FileCache cls;
    readmenator__cache_py --> readmenator__cache_py_FileCache
    readmenator__cache_py___init__["__init__"]
    class readmenator__cache_py___init__ fn;
    readmenator__cache_py --> readmenator__cache_py___init__
    readmenator__cache_py_load["load"]
    class readmenator__cache_py_load fn;
    readmenator__cache_py --> readmenator__cache_py_load
    readmenator__cache_py_save["save"]
    class readmenator__cache_py_save fn;
    readmenator__cache_py --> readmenator__cache_py_save
    readmenator__cache_py_compute_hash["compute_hash"]
    class readmenator__cache_py_compute_hash fn;
    readmenator__cache_py --> readmenator__cache_py_compute_hash
    tests_test_documentation_py["test_documentation.py (py)"]
    class tests_test_documentation_py mod;
    tests_test_documentation_py_TestDocumentationGeneratorContract["TestDocumentationGeneratorContract"]
    class tests_test_documentation_py_TestDocumentationGeneratorContract cls;
    tests_test_documentation_py --> tests_test_documentation_py_TestDocumentationGeneratorContract
    tests_test_documentation_py_setUp["setUp"]
    class tests_test_documentation_py_setUp fn;
    tests_test_documentation_py --> tests_test_documentation_py_setUp
    tests_test_documentation_py_test_contains_header["test_contains_header"]
    class tests_test_documentation_py_test_contains_header fn;
    tests_test_documentation_py --> tests_test_documentation_py_test_contains_header
    tests_test_documentation_py_test_contains_metadata_line["test_contains_metadata_line"]
    class tests_test_documentation_py_test_contains_metadata_line fn;
    tests_test_documentation_py --> tests_test_documentation_py_test_contains_metadata_line
    tests_test_documentation_py_test_contains_mermaid_block["test_contains_mermaid_block"]
    class tests_test_documentation_py_test_contains_mermaid_block fn;
    tests_test_documentation_py --> tests_test_documentation_py_test_contains_mermaid_block
    tests_test_mermaid_py["test_mermaid.py (py)"]
    class tests_test_mermaid_py mod;
    tests_test_mermaid_py_TestMermaidRendererContract["TestMermaidRendererContract"]
    class tests_test_mermaid_py_TestMermaidRendererContract cls;
    tests_test_mermaid_py --> tests_test_mermaid_py_TestMermaidRendererContract
    tests_test_mermaid_py_setUp["setUp"]
    class tests_test_mermaid_py_setUp fn;
    tests_test_mermaid_py --> tests_test_mermaid_py_setUp
    tests_test_mermaid_py_test_renders_graph_header["test_renders_graph_header"]
    class tests_test_mermaid_py_test_renders_graph_header fn;
    tests_test_mermaid_py --> tests_test_mermaid_py_test_renders_graph_header
    tests_test_mermaid_py_test_renders_module_node["test_renders_module_node"]
    class tests_test_mermaid_py_test_renders_module_node fn;
    tests_test_mermaid_py --> tests_test_mermaid_py_test_renders_module_node
    tests_test_mermaid_py_test_renders_symbol_subnodes["test_renders_symbol_subnodes"]
    class tests_test_mermaid_py_test_renders_symbol_subnodes fn;
    tests_test_mermaid_py --> tests_test_mermaid_py_test_renders_symbol_subnodes
    readmenator__watcher_py["_watcher.py (py)"]
    class readmenator__watcher_py mod;
    readmenator__watcher_py_DirectoryWatcher["DirectoryWatcher"]
    class readmenator__watcher_py_DirectoryWatcher cls;
    readmenator__watcher_py --> readmenator__watcher_py_DirectoryWatcher
    readmenator__watcher_py___init__["__init__"]
    class readmenator__watcher_py___init__ fn;
    readmenator__watcher_py --> readmenator__watcher_py___init__
    readmenator__watcher_py__compute_snapshot["_compute_snapshot"]
    class readmenator__watcher_py__compute_snapshot fn;
    readmenator__watcher_py --> readmenator__watcher_py__compute_snapshot
    readmenator__watcher_py_start["start"]
    class readmenator__watcher_py_start fn;
    readmenator__watcher_py --> readmenator__watcher_py_start
    readmenator__watcher_py_stop["stop"]
    class readmenator__watcher_py_stop fn;
    readmenator__watcher_py --> readmenator__watcher_py_stop
    readmenator__mermaid_py["_mermaid.py (py)"]
    class readmenator__mermaid_py mod;
    readmenator__mermaid_py_MermaidRenderer["MermaidRenderer"]
    class readmenator__mermaid_py_MermaidRenderer cls;
    readmenator__mermaid_py --> readmenator__mermaid_py_MermaidRenderer
    readmenator__mermaid_py___init__["__init__"]
    class readmenator__mermaid_py___init__ fn;
    readmenator__mermaid_py --> readmenator__mermaid_py___init__
    readmenator__mermaid_py__sanitize_id["_sanitize_id"]
    class readmenator__mermaid_py__sanitize_id fn;
    readmenator__mermaid_py --> readmenator__mermaid_py__sanitize_id
    readmenator__mermaid_py_render["render"]
    class readmenator__mermaid_py_render fn;
    readmenator__mermaid_py --> readmenator__mermaid_py_render
    readmenator___main___py["__main__.py (py)"]
    class readmenator___main___py mod;
    readmenator___main___py_build_parser["build_parser"]
    class readmenator___main___py_build_parser fn;
    readmenator___main___py --> readmenator___main___py_build_parser
    readmenator___main___py__run_tests["_run_tests"]
    class readmenator___main___py__run_tests fn;
    readmenator___main___py --> readmenator___main___py__run_tests
    readmenator___main___py_main["main"]
    class readmenator___main___py_main fn;
    readmenator___main___py --> readmenator___main___py_main
    tests_test_parsers_py["test_parsers.py (py)"]
    class tests_test_parsers_py mod;
    tests_test_parsers_py_TestCParserContract["TestCParserContract"]
    class tests_test_parsers_py_TestCParserContract cls;
    tests_test_parsers_py --> tests_test_parsers_py_TestCParserContract
    tests_test_parsers_py_TestPythonParserContract["TestPythonParserContract"]
    class tests_test_parsers_py_TestPythonParserContract cls;
    tests_test_parsers_py --> tests_test_parsers_py_TestPythonParserContract
    tests_test_parsers_py_TestGoParserContract["TestGoParserContract"]
    class tests_test_parsers_py_TestGoParserContract cls;
    tests_test_parsers_py --> tests_test_parsers_py_TestGoParserContract
    tests_test_parsers_py_TestRustParserContract["TestRustParserContract"]
    class tests_test_parsers_py_TestRustParserContract cls;
    tests_test_parsers_py --> tests_test_parsers_py_TestRustParserContract
    tests_test_parsers_py_TestJavaScriptParserContract["TestJavaScriptParserContract"]
    class tests_test_parsers_py_TestJavaScriptParserContract cls;
    tests_test_parsers_py --> tests_test_parsers_py_TestJavaScriptParserContract
    tests_test_parsers_new_py["test_parsers_new.py (py)"]
    class tests_test_parsers_new_py mod;
    tests_test_parsers_new_py_TestRubyParserContract["TestRubyParserContract"]
    class tests_test_parsers_new_py_TestRubyParserContract cls;
    tests_test_parsers_new_py --> tests_test_parsers_new_py_TestRubyParserContract
    tests_test_parsers_new_py_TestSwiftParserContract["TestSwiftParserContract"]
    class tests_test_parsers_new_py_TestSwiftParserContract cls;
    tests_test_parsers_new_py --> tests_test_parsers_new_py_TestSwiftParserContract
    tests_test_parsers_new_py_TestKotlinParserContract["TestKotlinParserContract"]
    class tests_test_parsers_new_py_TestKotlinParserContract cls;
    tests_test_parsers_new_py --> tests_test_parsers_new_py_TestKotlinParserContract
    tests_test_parsers_new_py_TestScalaParserContract["TestScalaParserContract"]
    class tests_test_parsers_new_py_TestScalaParserContract cls;
    tests_test_parsers_new_py --> tests_test_parsers_new_py_TestScalaParserContract
    tests_test_parsers_new_py_TestLuaParserContract["TestLuaParserContract"]
    class tests_test_parsers_new_py_TestLuaParserContract cls;
    tests_test_parsers_new_py --> tests_test_parsers_new_py_TestLuaParserContract
    readmenator___init___py["__init__.py (py)"]
    class readmenator___init___py mod;
    tests_test_query_py["test_query.py (py)"]
    class tests_test_query_py mod;
    tests_test_query_py__make_node["_make_node"]
    class tests_test_query_py__make_node fn;
    tests_test_query_py --> tests_test_query_py__make_node
    tests_test_query_py__make_sym["_make_sym"]
    class tests_test_query_py__make_sym fn;
    tests_test_query_py --> tests_test_query_py__make_sym
    tests_test_query_py_TestQueryEngineContract["TestQueryEngineContract"]
    class tests_test_query_py_TestQueryEngineContract cls;
    tests_test_query_py --> tests_test_query_py_TestQueryEngineContract
    tests_test_query_py_setUp["setUp"]
    class tests_test_query_py_setUp fn;
    tests_test_query_py --> tests_test_query_py_setUp
    tests_test_query_py_test_find_exact_symbol["test_find_exact_symbol"]
    class tests_test_query_py_test_find_exact_symbol fn;
    tests_test_query_py --> tests_test_query_py_test_find_exact_symbol
    readmenator__query_py["_query.py (py)"]
    class readmenator__query_py mod;
    readmenator__query_py_QueryEngine["QueryEngine"]
    class readmenator__query_py_QueryEngine cls;
    readmenator__query_py --> readmenator__query_py_QueryEngine
    readmenator__query_py___init__["__init__"]
    class readmenator__query_py___init__ fn;
    readmenator__query_py --> readmenator__query_py___init__
    readmenator__query_py__build_symbol_index["_build_symbol_index"]
    class readmenator__query_py__build_symbol_index fn;
    readmenator__query_py --> readmenator__query_py__build_symbol_index
    readmenator__query_py__build_import_graph["_build_import_graph"]
    class readmenator__query_py__build_import_graph fn;
    readmenator__query_py --> readmenator__query_py__build_import_graph
    readmenator__query_py__build_resolved_graph["_build_resolved_graph"]
    class readmenator__query_py__build_resolved_graph fn;
    readmenator__query_py --> readmenator__query_py__build_resolved_graph
    end
    subgraph community_1 ["readmenator"]
    readmenator__resolver_py["_resolver.py (py)"]
    class readmenator__resolver_py mod;
    readmenator__resolver_py_ImportResolver["ImportResolver"]
    class readmenator__resolver_py_ImportResolver cls;
    readmenator__resolver_py --> readmenator__resolver_py_ImportResolver
    readmenator__resolver_py___init__["__init__"]
    class readmenator__resolver_py___init__ fn;
    readmenator__resolver_py --> readmenator__resolver_py___init__
    readmenator__resolver_py__build_stem_index["_build_stem_index"]
    class readmenator__resolver_py__build_stem_index fn;
    readmenator__resolver_py --> readmenator__resolver_py__build_stem_index
    readmenator__resolver_py__build_dir_index["_build_dir_index"]
    class readmenator__resolver_py__build_dir_index fn;
    readmenator__resolver_py --> readmenator__resolver_py__build_dir_index
    readmenator__resolver_py_resolve["resolve"]
    class readmenator__resolver_py_resolve fn;
    readmenator__resolver_py --> readmenator__resolver_py_resolve
    tests_test_resolver_py["test_resolver.py (py)"]
    class tests_test_resolver_py mod;
    tests_test_resolver_py_TestImportResolverContract["TestImportResolverContract"]
    class tests_test_resolver_py_TestImportResolverContract cls;
    tests_test_resolver_py --> tests_test_resolver_py_TestImportResolverContract
    tests_test_resolver_py_test_resolves_python_module_dotpath["test_resolves_python_module_dotpath"]
    class tests_test_resolver_py_test_resolves_python_module_dotpath fn;
    tests_test_resolver_py --> tests_test_resolver_py_test_resolves_python_module_dotpath
    tests_test_resolver_py_test_resolves_relative_import["test_resolves_relative_import"]
    class tests_test_resolver_py_test_resolves_relative_import fn;
    tests_test_resolver_py --> tests_test_resolver_py_test_resolves_relative_import
    tests_test_resolver_py_test_resolves_extensionless_python_import["test_resolves_extensionless_python_import"]
    class tests_test_resolver_py_test_resolves_extensionless_python_import fn;
    tests_test_resolver_py --> tests_test_resolver_py_test_resolves_extensionless_python_import
    tests_test_resolver_py_test_resolves_package_init["test_resolves_package_init"]
    class tests_test_resolver_py_test_resolves_package_init fn;
    tests_test_resolver_py --> tests_test_resolver_py_test_resolves_package_init
    tests_test_config_py["test_config.py (py)"]
    class tests_test_config_py mod;
    tests_test_config_py_TestConfigContract["TestConfigContract"]
    class tests_test_config_py_TestConfigContract cls;
    tests_test_config_py --> tests_test_config_py_TestConfigContract
    tests_test_config_py_test_config_is_immutable["test_config_is_immutable"]
    class tests_test_config_py_test_config_is_immutable fn;
    tests_test_config_py --> tests_test_config_py_test_config_is_immutable
    tests_test_config_py_test_config_defaults_are_sane["test_config_defaults_are_sane"]
    class tests_test_config_py_test_config_defaults_are_sane fn;
    tests_test_config_py --> tests_test_config_py_test_config_defaults_are_sane
    tests_test_config_py_test_ignore_dirs_are_comprehensive["test_ignore_dirs_are_comprehensive"]
    class tests_test_config_py_test_ignore_dirs_are_comprehensive fn;
    tests_test_config_py --> tests_test_config_py_test_ignore_dirs_are_comprehensive
    tests_test_config_py_test_plural_map_covers_all_symbol_types["test_plural_map_covers_all_symbol_types"]
    class tests_test_config_py_test_plural_map_covers_all_symbol_types fn;
    tests_test_config_py --> tests_test_config_py_test_plural_map_covers_all_symbol_types
    readmenator__layers_py["_layers.py (py)"]
    class readmenator__layers_py mod;
    readmenator__layers_py_LayerDetector["LayerDetector"]
    class readmenator__layers_py_LayerDetector cls;
    readmenator__layers_py --> readmenator__layers_py_LayerDetector
    readmenator__layers_py___init__["__init__"]
    class readmenator__layers_py___init__ fn;
    readmenator__layers_py --> readmenator__layers_py___init__
    readmenator__layers_py_detect["detect"]
    class readmenator__layers_py_detect fn;
    readmenator__layers_py --> readmenator__layers_py_detect
    readmenator__layers_py__classify_file["_classify_file"]
    class readmenator__layers_py__classify_file fn;
    readmenator__layers_py --> readmenator__layers_py__classify_file
    readmenator__layers_py_layer_summary["layer_summary"]
    class readmenator__layers_py_layer_summary fn;
    readmenator__layers_py --> readmenator__layers_py_layer_summary
    readmenator_py["readmenator.py (py)"]
    class readmenator_py mod;
    tests_test_models_py["test_models.py (py)"]
    class tests_test_models_py mod;
    tests_test_models_py_TestSymbolContract["TestSymbolContract"]
    class tests_test_models_py_TestSymbolContract cls;
    tests_test_models_py --> tests_test_models_py_TestSymbolContract
    tests_test_models_py_TestNodeContract["TestNodeContract"]
    class tests_test_models_py_TestNodeContract cls;
    tests_test_models_py --> tests_test_models_py_TestNodeContract
    tests_test_models_py_TestEdgeContract["TestEdgeContract"]
    class tests_test_models_py_TestEdgeContract cls;
    tests_test_models_py --> tests_test_models_py_TestEdgeContract
    tests_test_models_py_TestPluralizeContract["TestPluralizeContract"]
    class tests_test_models_py_TestPluralizeContract cls;
    tests_test_models_py --> tests_test_models_py_TestPluralizeContract
    tests_test_models_py_test_symbol_creation["test_symbol_creation"]
    class tests_test_models_py_test_symbol_creation fn;
    tests_test_models_py --> tests_test_models_py_test_symbol_creation
    readmenator__models_py["_models.py (py)"]
    class readmenator__models_py mod;
    readmenator__models_py_Symbol["Symbol"]
    class readmenator__models_py_Symbol cls;
    readmenator__models_py --> readmenator__models_py_Symbol
    readmenator__models_py_Node["Node"]
    class readmenator__models_py_Node cls;
    readmenator__models_py --> readmenator__models_py_Node
    readmenator__models_py_Edge["Edge"]
    class readmenator__models_py_Edge cls;
    readmenator__models_py --> readmenator__models_py_Edge
    readmenator__models_py_pluralize_symbol_kind["pluralize_symbol_kind"]
    class readmenator__models_py_pluralize_symbol_kind fn;
    readmenator__models_py --> readmenator__models_py_pluralize_symbol_kind
    readmenator__models_py_CommunityResult["CommunityResult"]
    class readmenator__models_py_CommunityResult cls;
    readmenator__models_py --> readmenator__models_py_CommunityResult
    readmenator__config_py["_config.py (py)"]
    class readmenator__config_py mod;
    readmenator__config_py_Config["Config"]
    class readmenator__config_py_Config cls;
    readmenator__config_py --> readmenator__config_py_Config
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
    end
    readmenator___init___py -- resolved_imports --> readmenator__app_py
    readmenator___init___py -- resolved_imports --> readmenator__config_py
    readmenator___init___py -- resolved_imports --> readmenator__models_py
    readmenator___main___py -- resolved_imports --> readmenator__app_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__config_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__analyzer_py
    readmenator__app_py -- resolved_imports --> readmenator__cache_py
    readmenator__app_py -- resolved_imports --> readmenator__config_py
    readmenator__app_py -- resolved_imports --> readmenator__documentation_py
    readmenator__app_py -- resolved_imports --> readmenator__exporter_py
    readmenator__app_py -- resolved_imports --> readmenator__layers_py
    readmenator__app_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__query_py
    readmenator__app_py -- resolved_imports --> readmenator__resolver_py
    readmenator__app_py -- resolved_imports --> readmenator__scanner_py
    readmenator__app_py -- resolved_imports --> readmenator__watcher_py
    readmenator__cache_py -- resolved_imports --> readmenator__config_py
    readmenator__documentation_py -- resolved_imports --> readmenator__config_py
    readmenator__documentation_py -- resolved_imports --> readmenator__mermaid_py
    readmenator__documentation_py -- resolved_imports --> readmenator__models_py
    readmenator__exporter_py -- resolved_imports --> readmenator__config_py
    readmenator__exporter_py -- resolved_imports --> readmenator__models_py
    readmenator__layers_py -- resolved_imports --> readmenator__models_py
    readmenator__mermaid_py -- resolved_imports --> readmenator__config_py
    readmenator__mermaid_py -- resolved_imports --> readmenator__models_py
    readmenator__parsers_py -- resolved_imports --> readmenator__config_py
    readmenator__parsers_py -- resolved_imports --> readmenator__models_py
    readmenator__query_py -- resolved_imports --> readmenator__models_py
    readmenator__scanner_py -- resolved_imports --> readmenator__config_py
    readmenator__scanner_py -- resolved_imports --> readmenator__models_py
    readmenator__scanner_py -- resolved_imports --> readmenator__parsers_py
    readmenator__watcher_py -- resolved_imports --> readmenator__config_py
    readmenator_py -- resolved_imports --> readmenator___main___py
    tests_test_analyzer_py -- resolved_imports --> readmenator__analyzer_py
    tests_test_analyzer_py -- resolved_imports --> readmenator__config_py
    tests_test_analyzer_py -- resolved_imports --> readmenator__models_py
    tests_test_cache_py -- resolved_imports --> readmenator__cache_py
    tests_test_cache_py -- resolved_imports --> readmenator__config_py
    tests_test_config_py -- resolved_imports --> readmenator__config_py
    tests_test_documentation_py -- resolved_imports --> readmenator__config_py
    tests_test_documentation_py -- resolved_imports --> readmenator__documentation_py
    tests_test_documentation_py -- resolved_imports --> readmenator__models_py
    tests_test_exporter_py -- resolved_imports --> readmenator__config_py
    tests_test_exporter_py -- resolved_imports --> readmenator__exporter_py
    tests_test_exporter_py -- resolved_imports --> readmenator__models_py
    tests_test_integration_py -- resolved_imports --> readmenator__app_py
    tests_test_integration_py -- resolved_imports --> readmenator__config_py
    tests_test_mermaid_py -- resolved_imports --> readmenator__config_py
    tests_test_mermaid_py -- resolved_imports --> readmenator__mermaid_py
    tests_test_mermaid_py -- resolved_imports --> readmenator__models_py
    tests_test_models_py -- resolved_imports --> readmenator__models_py
    tests_test_parsers_py -- resolved_imports --> readmenator__config_py
    tests_test_parsers_py -- resolved_imports --> readmenator__parsers_py
    tests_test_parsers_new_py -- resolved_imports --> readmenator__config_py
    tests_test_parsers_new_py -- resolved_imports --> readmenator__parsers_py
    tests_test_query_py -- resolved_imports --> readmenator__models_py
    tests_test_query_py -- resolved_imports --> readmenator__query_py
    tests_test_resolver_py -- resolved_imports --> readmenator__resolver_py
    tests_test_scanner_py -- resolved_imports --> readmenator__config_py
    tests_test_scanner_py -- resolved_imports --> readmenator__scanner_py
    ext_readmenator__app["readmenator._app"]
    class ext_readmenator__app ext;
    readmenator___init___py -.->|imports| ext_readmenator__app
    ext_readmenator__config["readmenator._config"]
    class ext_readmenator__config ext;
    readmenator___init___py -.->|imports| ext_readmenator__config
    ext_readmenator__models["readmenator._models"]
    class ext_readmenator__models ext;
    readmenator___init___py -.->|imports| ext_readmenator__models
    ext___future__["__future__"]
    class ext___future__ ext;
    readmenator___main___py -.->|imports| ext___future__
    ext_argparse["argparse"]
    class ext_argparse ext;
    readmenator___main___py -.->|imports| ext_argparse
    ext_sys["sys"]
    class ext_sys ext;
    readmenator___main___py -.->|imports| ext_sys
    ext_unittest["unittest"]
    class ext_unittest ext;
    readmenator___main___py -.->|imports| ext_unittest
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    readmenator___main___py -.->|imports| ext_pathlib
    readmenator___main___py -.->|imports| ext_readmenator__app
    readmenator__analyzer_py -.->|imports| ext___future__
    ext_random["random"]
    class ext_random ext;
    readmenator__analyzer_py -.->|imports| ext_random
    ext_collections["collections"]
    class ext_collections ext;
    readmenator__analyzer_py -.->|imports| ext_collections
    ext_typing["typing"]
    class ext_typing ext;
    readmenator__analyzer_py -.->|imports| ext_typing
    readmenator__analyzer_py -.->|imports| ext_readmenator__config
    readmenator__analyzer_py -.->|imports| ext_readmenator__models
    readmenator__analyzer_py -.->|imports| ext_collections
    readmenator__app_py -.->|imports| ext___future__
    ext_json["json"]
    class ext_json ext;
    readmenator__app_py -.->|imports| ext_json
    readmenator__app_py -.->|imports| ext_pathlib
    readmenator__app_py -.->|imports| ext_typing
    ext_readmenator__analyzer["readmenator._analyzer"]
    class ext_readmenator__analyzer ext;
    readmenator__app_py -.->|imports| ext_readmenator__analyzer
    ext_readmenator__cache["readmenator._cache"]
    class ext_readmenator__cache ext;
    readmenator__app_py -.->|imports| ext_readmenator__cache
    readmenator__app_py -.->|imports| ext_readmenator__config
    ext_readmenator__documentation["readmenator._documentation"]
    class ext_readmenator__documentation ext;
    readmenator__app_py -.->|imports| ext_readmenator__documentation
    ext_readmenator__exporter["readmenator._exporter"]
    class ext_readmenator__exporter ext;
    readmenator__app_py -.->|imports| ext_readmenator__exporter
    ext_readmenator__layers["readmenator._layers"]
    class ext_readmenator__layers ext;
    readmenator__app_py -.->|imports| ext_readmenator__layers
    readmenator__app_py -.->|imports| ext_readmenator__models
    ext_readmenator__query["readmenator._query"]
    class ext_readmenator__query ext;
    readmenator__app_py -.->|imports| ext_readmenator__query
    ext_readmenator__resolver["readmenator._resolver"]
    class ext_readmenator__resolver ext;
    readmenator__app_py -.->|imports| ext_readmenator__resolver
    ext_readmenator__scanner["readmenator._scanner"]
    class ext_readmenator__scanner ext;
    readmenator__app_py -.->|imports| ext_readmenator__scanner
    ext_readmenator__watcher["readmenator._watcher"]
    class ext_readmenator__watcher ext;
    readmenator__app_py -.->|imports| ext_readmenator__watcher
    readmenator__cache_py -.->|imports| ext___future__
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    readmenator__cache_py -.->|imports| ext_hashlib
    readmenator__cache_py -.->|imports| ext_json
    ext_os["os"]
    class ext_os ext;
    readmenator__cache_py -.->|imports| ext_os
    readmenator__cache_py -.->|imports| ext_pathlib
    readmenator__cache_py -.->|imports| ext_typing
    readmenator__cache_py -.->|imports| ext_readmenator__config
    readmenator__config_py -.->|imports| ext___future__
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    readmenator__config_py -.->|imports| ext_dataclasses
    readmenator__config_py -.->|imports| ext_typing
    readmenator__documentation_py -.->|imports| ext___future__
    readmenator__documentation_py -.->|imports| ext_typing
    readmenator__documentation_py -.->|imports| ext_readmenator__config
    ext_readmenator__mermaid["readmenator._mermaid"]
    class ext_readmenator__mermaid ext;
    readmenator__documentation_py -.->|imports| ext_readmenator__mermaid
    readmenator__documentation_py -.->|imports| ext_readmenator__models
    readmenator__documentation_py -.->|imports| ext_collections
    readmenator__exporter_py -.->|imports| ext___future__
    readmenator__exporter_py -.->|imports| ext_json
    readmenator__exporter_py -.->|imports| ext_os
    readmenator__exporter_py -.->|imports| ext_pathlib
    ext_textwrap["textwrap"]
    class ext_textwrap ext;
    readmenator__exporter_py -.->|imports| ext_textwrap
    readmenator__exporter_py -.->|imports| ext_typing
    readmenator__exporter_py -.->|imports| ext_readmenator__config
    readmenator__exporter_py -.->|imports| ext_readmenator__models
    ext_math["math"]
    class ext_math ext;
    readmenator__exporter_py -.->|imports| ext_math
    readmenator__exporter_py -.->|imports| ext_os
    readmenator__layers_py -.->|imports| ext___future__
    readmenator__layers_py -.->|imports| ext_typing
    readmenator__layers_py -.->|imports| ext_readmenator__models
    readmenator__mermaid_py -.->|imports| ext___future__
    ext_re["re"]
    class ext_re ext;
    readmenator__mermaid_py -.->|imports| ext_re
    readmenator__mermaid_py -.->|imports| ext_typing
    readmenator__mermaid_py -.->|imports| ext_readmenator__config
    readmenator__mermaid_py -.->|imports| ext_readmenator__models
    readmenator__models_py -.->|imports| ext___future__
    readmenator__models_py -.->|imports| ext_dataclasses
    readmenator__models_py -.->|imports| ext_typing
    readmenator__parsers_py -.->|imports| ext___future__
    ext_ast["ast"]
    class ext_ast ext;
    readmenator__parsers_py -.->|imports| ext_ast
    readmenator__parsers_py -.->|imports| ext_re
    ext_warnings["warnings"]
    class ext_warnings ext;
    readmenator__parsers_py -.->|imports| ext_warnings
    readmenator__parsers_py -.->|imports| ext_typing
    readmenator__parsers_py -.->|imports| ext_readmenator__config
    readmenator__parsers_py -.->|imports| ext_readmenator__models
    readmenator__query_py -.->|imports| ext___future__
    readmenator__query_py -.->|imports| ext_collections
    readmenator__query_py -.->|imports| ext_typing
    readmenator__query_py -.->|imports| ext_readmenator__models
    readmenator__resolver_py -.->|imports| ext___future__
    readmenator__resolver_py -.->|imports| ext_re
    readmenator__resolver_py -.->|imports| ext_pathlib
    readmenator__resolver_py -.->|imports| ext_typing
    readmenator__scanner_py -.->|imports| ext___future__
    readmenator__scanner_py -.->|imports| ext_pathlib
    readmenator__scanner_py -.->|imports| ext_typing
    readmenator__scanner_py -.->|imports| ext_readmenator__config
    readmenator__scanner_py -.->|imports| ext_readmenator__models
    ext_readmenator__parsers["readmenator._parsers"]
    class ext_readmenator__parsers ext;
    readmenator__scanner_py -.->|imports| ext_readmenator__parsers
    readmenator__watcher_py -.->|imports| ext___future__
    readmenator__watcher_py -.->|imports| ext_hashlib
    ext_time["time"]
    class ext_time ext;
    readmenator__watcher_py -.->|imports| ext_time
    readmenator__watcher_py -.->|imports| ext_pathlib
    readmenator__watcher_py -.->|imports| ext_typing
    readmenator__watcher_py -.->|imports| ext_readmenator__config
    readmenator_py -.->|imports| ext_sys
    readmenator_py -.->|imports| ext_pathlib
    ext_readmenator___main__["readmenator.__main__"]
    class ext_readmenator___main__ ext;
    readmenator_py -.->|imports| ext_readmenator___main__
    readmenator_orchestrator_py -.->|imports| ext_argparse
    ext_logging["logging"]
    class ext_logging ext;
    readmenator_orchestrator_py -.->|imports| ext_logging
    readmenator_orchestrator_py -.->|imports| ext_os
    ext_shutil["shutil"]
    class ext_shutil ext;
    readmenator_orchestrator_py -.->|imports| ext_shutil
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    readmenator_orchestrator_py -.->|imports| ext_subprocess
    readmenator_orchestrator_py -.->|imports| ext_sys
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    readmenator_orchestrator_py -.->|imports| ext_tempfile
    readmenator_orchestrator_py -.->|imports| ext_unittest
    readmenator_orchestrator_py -.->|imports| ext_dataclasses
    ext_datetime["datetime"]
    class ext_datetime ext;
    readmenator_orchestrator_py -.->|imports| ext_datetime
    readmenator_orchestrator_py -.->|imports| ext_pathlib
    readmenator_orchestrator_py -.->|imports| ext_typing
    tests_test_analyzer_py -.->|imports| ext___future__
    tests_test_analyzer_py -.->|imports| ext_unittest
    tests_test_analyzer_py -.->|imports| ext_readmenator__analyzer
    tests_test_analyzer_py -.->|imports| ext_readmenator__config
    tests_test_analyzer_py -.->|imports| ext_readmenator__models
    tests_test_cache_py -.->|imports| ext___future__
    tests_test_cache_py -.->|imports| ext_os
    tests_test_cache_py -.->|imports| ext_tempfile
    tests_test_cache_py -.->|imports| ext_unittest
    tests_test_cache_py -.->|imports| ext_pathlib
    tests_test_cache_py -.->|imports| ext_readmenator__cache
    tests_test_cache_py -.->|imports| ext_readmenator__config
    tests_test_cache_py -.->|imports| ext_shutil
    tests_test_config_py -.->|imports| ext_unittest
    tests_test_config_py -.->|imports| ext_dataclasses
    tests_test_config_py -.->|imports| ext_readmenator__config
    tests_test_documentation_py -.->|imports| ext_unittest
    tests_test_documentation_py -.->|imports| ext_readmenator__config
    tests_test_documentation_py -.->|imports| ext_readmenator__documentation
    tests_test_documentation_py -.->|imports| ext_readmenator__models
    tests_test_exporter_py -.->|imports| ext___future__
    tests_test_exporter_py -.->|imports| ext_json
    tests_test_exporter_py -.->|imports| ext_unittest
    tests_test_exporter_py -.->|imports| ext_readmenator__config
    tests_test_exporter_py -.->|imports| ext_readmenator__exporter
    tests_test_exporter_py -.->|imports| ext_readmenator__models
    tests_test_integration_py -.->|imports| ext_tempfile
    tests_test_integration_py -.->|imports| ext_unittest
    tests_test_integration_py -.->|imports| ext_pathlib
    tests_test_integration_py -.->|imports| ext_readmenator__app
    tests_test_integration_py -.->|imports| ext_readmenator__config
    tests_test_integration_py -.->|imports| ext_shutil
    tests_test_mermaid_py -.->|imports| ext_unittest
    tests_test_mermaid_py -.->|imports| ext_readmenator__config
    tests_test_mermaid_py -.->|imports| ext_readmenator__mermaid
    tests_test_mermaid_py -.->|imports| ext_readmenator__models
    tests_test_models_py -.->|imports| ext_unittest
    tests_test_models_py -.->|imports| ext_readmenator__models
    tests_test_parsers_py -.->|imports| ext_unittest
    tests_test_parsers_py -.->|imports| ext_readmenator__config
    tests_test_parsers_py -.->|imports| ext_readmenator__parsers
    tests_test_parsers_py -.->|imports| ext_warnings
    tests_test_parsers_new_py -.->|imports| ext___future__
    tests_test_parsers_new_py -.->|imports| ext_unittest
    tests_test_parsers_new_py -.->|imports| ext_readmenator__config
    tests_test_parsers_new_py -.->|imports| ext_readmenator__parsers
    tests_test_query_py -.->|imports| ext_unittest
    tests_test_query_py -.->|imports| ext_readmenator__models
    tests_test_query_py -.->|imports| ext_readmenator__query
    tests_test_resolver_py -.->|imports| ext___future__
    tests_test_resolver_py -.->|imports| ext_unittest
    tests_test_resolver_py -.->|imports| ext_readmenator__resolver
    tests_test_scanner_py -.->|imports| ext_os
    tests_test_scanner_py -.->|imports| ext_tempfile
    tests_test_scanner_py -.->|imports| ext_unittest
    tests_test_scanner_py -.->|imports| ext_pathlib
    tests_test_scanner_py -.->|imports| ext_readmenator__config
    tests_test_scanner_py -.->|imports| ext_readmenator__scanner
    tests_test_scanner_py -.->|imports| ext_shutil
```

---

## Architecture Reference

### PY (32 files)

#### `__init__.py`
**Path:** `readmenator/__init__.py`

*No symbols extracted*

#### `__main__.py`
**Path:** `readmenator/__main__.py`

**Functions:**
- `build_parser` (line 19) `def build_parser()` - *Construct the argument parser with subcommand help and examples.*
- `_run_tests` (line 99) `def _run_tests()` - *Discover and run the full test suite from the tests/ directory.*
- `main` (line 115) `def main()` - *Primary CLI entry point invoked by ``python -m readmenator``.

Supports direct subcommand dispatch (query, explain, path, summary,
update, export, analyze, --rebuild) or falls back to the argument
parser for the default workflow: generate or summarise
KNOWLEDGE_BASE.md.*

#### `_analyzer.py`
**Path:** `readmenator/_analyzer.py`

**Classes:**
- `GraphAnalyzer` (line 20) `class GraphAnalyzer` - *Deterministic graph analysis over scanned nodes and edges.

Builds an internal adjacency graph from import edges, then applies
community detection, centrality scoring, cross-community bridge
discovery, and question generation without any external API calls.*

**Methods:**
- `__init__` (line 28) `def __init__(self, config)` - *Initialise with application configuration.

Args:
    config: Settings for thresholds and limits.*
- `analyze` (line 36) `def analyze(self, nodes, edges, resolved_edges)` - *Run the full analysis pipeline and return structured results.

Args:
    nodes: Scanned file nodes.
    edges: Import edges from the scanner.
    resolved_edges: Optional list of resolved-import edges (source and
        target are both project file IDs).

Returns:
    An AnalysisResult with god nodes, communities, surprising
    connections, and suggested questions.*
- `_build_adjacency` (line 89) `def _build_adjacency(self, nodes, edges)` - *Build an undirected adjacency map from import edges.*
- `_build_reverse_adjacency` (line 103) `def _build_reverse_adjacency(self, adjacency)` - *Build a directed reverse adjacency (incoming edges) map.*
- `_compute_god_nodes` (line 113) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` - *Compute the most central nodes using combined degree centrality.

Score is a combination of out-degree (imports), in-degree (imported-by),
and symbol count. Higher score means more architecturally significant.*
- `_detect_communities` (line 135) `def _detect_communities(self, nodes, adjacency)` - *Detect communities using label propagation.

Each node adopts the most frequent community label among its
neighbors. Iterates until convergence or max iterations reached.
Simple, deterministic, and correct for connected graphs.*
- `_label_communities` (line 186) `def _label_communities(self, nodes, communities)` - *Generate human-readable labels for communities.

Labels are based on the most common directory within the community.*
- `_build_community_map` (line 213) `def _build_community_map(self, communities)` - *Build a reverse map from file ID to community ID.*
- `_compute_cohesion` (line 223) `def _compute_cohesion(self, communities, adjacency)` - *Compute cohesion score for each community.

Cohesion = internal edges / (internal edges + external edges).*
- `_find_surprising_connections` (line 248) `def _find_surprising_connections(self, nodes, adjacency, community_map)` - *Find non-obvious cross-community bridges.

A connection is surprising when two nodes in different communities
are connected indirectly through 3 or more hops, and the path
crosses community boundaries.*
- `_shortest_path_communities` (line 288) `def _shortest_path_communities(self, source, target, adjacency, community_map)` - *Find the shortest path and communities traversed.*
- `_suggest_questions` (line 316) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)` - *Generate plain-language exploration questions from graph structure.*

#### `_app.py`
**Path:** `readmenator/_app.py`

**Classes:**
- `readmenatorApplication` (line 27) `class readmenatorApplication` - *High-level facade for readmenator operations.

Provides convenience methods for the full pipeline:
  - ``run`` / ``rebuild``: scan + generate KNOWLEDGE_BASE.md
  - ``update``: incremental scan using content hash cache
  - ``query``, ``explain``, ``find_path``, ``summary``:
    scan + query in a single call
  - ``analyze``: run community detection and graph analysis
  - ``export_json``, ``export_html``, ``export_svg``:
    export the graph to various formats*

**Methods:**
- `__init__` (line 40) `def __init__(self, config)` - *Initialise the application with an optional custom config.

Args:
    config: Application settings; defaults to Config() if omitted.*
- `_scan` (line 55) `def _scan(self, target_dir)` - *Resolve *target_dir* and run the scanner, caching results.*
- `_resolve_imports` (line 64) `def _resolve_imports(self, nodes, edges, target_dir)` - *Resolve raw import strings to project file paths.

Args:
    nodes: Scanned file nodes.
    edges: Raw import edges.
    target_dir: Project root directory.

Returns:
    List of resolved import edges with project file targets.*
- `run` (line 93) `def run(self, target_dir, resolve_imports, run_analysis)` - *Scan *target_dir* and write KNOWLEDGE_BASE.md to disk.

Args:
    target_dir: Project directory to scan.
    resolve_imports: Whether to resolve raw imports to project files.
    run_analysis: Whether to run community detection and graph analysis.*
- `update` (line 148) `def update(self, target_dir)` - *Incrementally update KNOWLEDGE_BASE.md for changed files only.

Uses SHA256 content hashing to detect which files have changed
since the last run. Falls back to full rebuild if no cache exists.

Args:
    target_dir: Project directory to scan.*
- `_scan_for_cache` (line 176) `def _scan_for_cache(self, root, cache)` - *Scan only files that have changed since the last cache write.

If no cache exists, performs a full scan and populates the cache.*
- `query` (line 200) `def query(self, target_dir, question)` - *Scan *target_dir* and answer *question* using the query engine.*
- `explain` (line 206) `def explain(self, target_dir, symbol_name)` - *Scan *target_dir* and return a detailed explanation of *symbol_name*.*
- `find_path` (line 219) `def find_path(self, target_dir, symbol_a, symbol_b)` - *Scan *target_dir* and find the shortest import path between two symbols.

Uses resolved imports when available for project-internal paths.*
- `summary` (line 236) `def summary(self, target_dir)` - *Scan *target_dir* and return a concise knowledge base overview.*
- `rebuild` (line 242) `def rebuild(self, target_dir)` - *Alias for ``run`` -- forces regeneration of KNOWLEDGE_BASE.md.*
- `analyze` (line 246) `def analyze(self, target_dir)` - *Run community detection and graph analysis on *target_dir*.

Returns:
    Structured AnalysisResult with god nodes, communities, etc.*
- `export_json` (line 255) `def export_json(self, target_dir, output_path)` - *Export the knowledge graph as JSON.

Args:
    target_dir: Project directory to scan.
    output_path: Optional file path for the JSON output.
        Defaults to ``<target_dir>/graph.json``.

Returns:
    JSON string content.*
- `export_html` (line 280) `def export_html(self, target_dir, output_path)` - *Export the knowledge graph as an interactive HTML page.

Args:
    target_dir: Project directory to scan.
    output_path: Optional file path for the HTML output.
        Defaults to ``<target_dir>/graph.html``.

Returns:
    HTML document string.*
- `export_svg` (line 305) `def export_svg(self, target_dir, output_path)` - *Export the knowledge graph as a static SVG image.

Args:
    target_dir: Project directory to scan.
    output_path: Optional file path for the SVG output.
        Defaults to ``<target_dir>/graph.svg``.

Returns:
    SVG document string.*
- `export` (line 330) `def export(self, target_dir)` - *Export all formats (JSON, HTML, SVG) at once.*
- `export_graphml` (line 336) `def export_graphml(self, target_dir, output_path)` - *Export the knowledge graph as GraphML (Gephi/yEd compatible).

Args:
    target_dir: Project directory to scan.
    output_path: Optional file path for the GraphML output.
        Defaults to ``<target_dir>/graph.graphml``.

Returns:
    GraphML XML string.*
- `export_obsidian` (line 361) `def export_obsidian(self, target_dir, output_dir)` - *Export the knowledge graph as an Obsidian vault.

Args:
    target_dir: Project directory to scan.
    output_dir: Optional directory for the Obsidian vault.
        Defaults to ``<target_dir>/obsidian``.

Returns:
    Number of notes written.*
- `watch` (line 385) `def watch(self, target_dir)` - *Start watching the project directory for changes (auto-rebuild).

Args:
    target_dir: Project directory to watch.*
- `detect_layers` (line 400) `def detect_layers(self, target_dir)` - *Detect architectural layers in the codebase.

Args:
    target_dir: Project directory to scan.

Returns:
    Dict mapping node_id to layer name.*
- `on_change` (line 394) `def on_change()`

#### `_cache.py`
**Path:** `readmenator/_cache.py`

**Classes:**
- `FileCache` (line 19) `class FileCache` - *SHA256-based cache for incremental file scanning.

Stores a JSON mapping of relative file paths to their content
hashes inside the project's cache directory. On subsequent runs,
files whose hash matches the cached value are skipped.*

**Methods:**
- `__init__` (line 27) `def __init__(self, config, project_root)` - *Initialise cache for the given project root.

Args:
    config: Application settings including CACHE_DIR.
    project_root: Absolute path of the scanned project.*
- `load` (line 38) `def load(self)` - *Load the cached hash map from disk.

Returns:
    Dict mapping relative file paths to their SHA256 hex digests.*
- `save` (line 54) `def save(self, hashes)` - *Persist the hash map to disk.

Args:
    hashes: Dict mapping relative file paths to SHA256 hex digests.*
- `compute_hash` (line 65) `def compute_hash(self, file_path)` - *Compute the SHA256 hex digest of a file's contents.

Args:
    file_path: Absolute path to the file.

Returns:
    SHA256 hex digest string.*
- `compute_hashes` (line 82) `def compute_hashes(self, file_paths)` - *Compute hashes for a batch of relative-path-to-absolute-path mappings.

Args:
    file_paths: Dict mapping relative paths to absolute Path objects.

Returns:
    Dict mapping relative paths to their SHA256 hex digests.*
- `find_changed` (line 98) `def find_changed(self, file_paths)` - *Determine which files have changed since the last cache.

Args:
    file_paths: Dict mapping relative paths to absolute Path objects.

Returns:
    Set of relative paths for files that are new or changed.*
- `prune_deleted` (line 120) `def prune_deleted(self, current_file_ids)` - *Remove entries for files that no longer exist on disk.

Args:
    current_file_ids: Set of relative paths currently in the project.*

#### `_config.py`
**Path:** `readmenator/_config.py`

**Classes:**
- `Config` (line 15) `class Config` - *Single source of truth for all readmenator settings.

Every tuneable constant -- file-size limits, directory depth,
supported extensions, symbol pluralisation map, Mermaid style
tokens, graph analysis thresholds, and export settings -- is
defined here and consumed by reference elsewhere.*

#### `_documentation.py`
**Path:** `readmenator/_documentation.py`

**Classes:**
- `DocumentationGenerator` (line 19) `class DocumentationGenerator` - *Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

Delegates graph rendering to MermaidRenderer and handles the
Markdown layout: header metadata, Mermaid block, and per-language
architecture sections with pluralised symbol kind headings.*

**Methods:**
- `__init__` (line 27) `def __init__(self, config)` - *Initialise with config and pre-compute the plural map.

Args:
    config: Application settings including SYMBOL_TYPE_PLURALS.*
- `generate` (line 37) `def generate(self, nodes, edges, resolved_edges, analysis, layers)` - *Assemble the full KNOWLEDGE_BASE.md Markdown document.

Groups files by language, lists symbols per file under
pluralised kind headings (e.g. "Classes", "Functions"),
and includes a note when the Mermaid graph was pruned.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for communities, god nodes, etc.
    layers: Optional dict mapping node_id to architectural layer.

Returns:
    Complete Markdown string ready to write to disk.*
- `_build_toc` (line 99) `def _build_toc(self, nodes, analysis, layers, is_truncated)` - *Build a table of contents for the document.*
- `_build_layers` (line 140) `def _build_layers(self, layers, nodes)` - *Build the architectural layers section.*
- `_build_dashboard` (line 176) `def _build_dashboard(self, nodes, edges, resolved_edges)` - *Build a statistics dashboard with import metrics and top files.*
- `_build_god_nodes` (line 251) `def _build_god_nodes(self, analysis)` - *Build the god nodes section.*
- `_build_community_analysis` (line 272) `def _build_community_analysis(self, analysis, nodes)` - *Build the community analysis section.*
- `_build_surprising_connections` (line 306) `def _build_surprising_connections(self, analysis, nodes)` - *Build the surprising connections section.*
- `_build_suggested_questions` (line 332) `def _build_suggested_questions(self, analysis)` - *Build the suggested questions section.*
- `_build_mermaid_section` (line 349) `def _build_mermaid_section(self, graph_output, is_truncated)` - *Build the Mermaid graph section.*
- `_build_architecture_reference` (line 373) `def _build_architecture_reference(self, nodes, edges)` - *Build the architecture reference grouped by language.*

#### `_exporter.py`
**Path:** `readmenator/_exporter.py`

**Classes:**
- `GraphExporter` (line 20) `class GraphExporter` - *Exports the knowledge graph to JSON, HTML, and SVG formats.

Each method is self-contained and produces a single file. No
external network calls are made; the HTML file embeds vis.js
from a CDN reference for offline-compatible rendering.*

**Methods:**
- `__init__` (line 28) `def __init__(self, config)` - *Initialise with application configuration.

Args:
    config: Settings for export styling and limits.*
- `to_json` (line 36) `def to_json(self, nodes, edges, resolved_edges, analysis)` - *Export the graph as a node-link JSON string.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for metadata.

Returns:
    JSON string with nodes, edges, and optional analysis metadata.*
- `to_html` (line 133) `def to_html(self, nodes, edges, resolved_edges, analysis)` - *Generate a standalone interactive HTML graph page.

Uses vis.js loaded from CDN. Supports click-to-inspect nodes,
search filtering, and community-based coloring.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community coloring.

Returns:
    Complete HTML document as a string.*
- `_community_color_map` (line 218) `def _community_color_map(self, analysis)` - *Build a node-to-color map based on community membership.*
- `_lighten` (line 236) `def _lighten(hex_color)` - *Lighten a hex color by 30% for border use.*
- `_render_html` (line 244) `def _render_html(self, vis_nodes, vis_edges, analysis)` - *Render the full HTML document with vis.js.*
- `to_svg` (line 365) `def to_svg(self, nodes, edges, resolved_edges, analysis)` - *Generate a static SVG representation of the graph.

Uses a simple force-directed layout without external dependencies.
For graphs with more than SVG_MAX_NODES, returns a plain SVG
with a truncation message.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community coloring.

Returns:
    SVG document as a string.*
- `_render_truncated_svg` (line 483) `def _render_truncated_svg(self, total_nodes)` - *Render a minimal SVG with a truncation notice.*
- `_layout_spring` (line 498) `def _layout_spring(self, nodes, edges, node_map)` - *Compute a simple spring-layout for node positioning.

Implements a basic force-directed layout with repulsion
between all nodes and attraction along edges. Runs a fixed
number of iterations for determinism.*
- `to_graphml` (line 581) `def to_graphml(self, nodes, edges, resolved_edges, analysis)` - *Export the graph as GraphML (Gephi/yEd compatible).

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community data.

Returns:
    GraphML XML string.*
- `to_obsidian` (line 658) `def to_obsidian(self, nodes, edges, output_dir, analysis)` - *Export the graph as an Obsidian vault with wikilinks.

Each file node becomes a markdown note. Community hub notes
aggregate related files. All notes use [[wikilinks]] for
Obsidian graph navigation.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    output_dir: Directory to write the Obsidian notes.
    analysis: Optional analysis results for community hubs.

Returns:
    Number of notes written.*
- `_project` (line 427) `def _project(pos)`

#### `_layers.py`
**Path:** `readmenator/_layers.py`

**Classes:**
- `LayerDetector` (line 15) `class LayerDetector` - *Detects architectural layers in a codebase.

Assigns each file to a layer based on path patterns, naming
conventions, and imported frameworks. Returns a mapping that
can enrich documentation and analysis.*

**Methods:**
- `__init__` (line 71) `def __init__(self, config)` - *Initialise with application configuration.*
- `detect` (line 75) `def detect(self, nodes, edges)` - *Assign each file node to an architectural layer.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.

Returns:
    Dict mapping node_id to layer name.*
- `_classify_file` (line 93) `def _classify_file(self, node, edges)` - *Classify a single file into an architectural layer.*
- `layer_summary` (line 125) `def layer_summary(self, layers)` - *Count files per layer.

Args:
    layers: Mapping from detect().

Returns:
    Dict of layer_name -> file_count.*

#### `_mermaid.py`
**Path:** `readmenator/_mermaid.py`

**Classes:**
- `MermaidRenderer` (line 18) `class MermaidRenderer` - *Renders a knowledge graph to Mermaid JS flowchart syntax.

Nodes are ordered by import count and symbol richness; the top
``MERMAID_MAX_NODES`` entries are included. External dependencies
(import targets not matching any scanned file) appear as dashed
boxes. Internal import edges between project files are rendered
as solid arrows. Community subgraphs group related files when
analysis results are available.*

**Methods:**
- `__init__` (line 29) `def __init__(self, config)` - *Initialise with configuration for style tokens and node limits.

Args:
    config: Provides MERMAID_* style strings and MERMAID_MAX_NODES.*
- `_sanitize_id` (line 38) `def _sanitize_id(node_id)` - *Convert *node_id* to a Mermaid-safe identifier.

Replaces non-alphanumeric characters with underscores and
prepends ``n_`` if the result starts with a digit.*
- `render` (line 49) `def render(self, nodes, edges, resolved_edges, analysis)` - *Produce a Mermaid flowchart string and a truncation flag.

Nodes are sorted by import popularity, then by symbol count.
Internal import edges (between project files) are rendered as
solid arrows when *resolved_edges* is provided. Community
subgraphs wrap related files when *analysis* is given.

Returns:
    Tuple of (Mermaid source string, is_truncated bool).*

#### `_models.py`
**Path:** `readmenator/_models.py`

**Classes:**
- `Symbol` (line 16) `class Symbol` - *A single code symbol extracted from a source file.

Attributes:
    name: Identifier of the symbol (class name, function name, etc.).
    kind: Semantic type (class, function, struct, enum, ...).
    line: One-based line number where the symbol is defined.
    doc: Optional docstring or comment extracted from the source.
    signature: Optional method or function signature snippet.*
- `Node` (line 35) `class Node` - *A file node in the knowledge graph, containing its symbols.

Attributes:
    node_id: Relative path of the file used as a unique identifier.
    label: Base file name for display purposes.
    kind: Type of node (typically "module").
    language: Programming language derived from the file extension.
    doc: Optional file-level documentation string.
    symbols: List of Symbol instances defined in this file.*
- `Edge` (line 56) `class Edge` - *A directed relationship between two nodes in the knowledge graph.

Attributes:
    source: Node ID of the source (dependent) file.
    target: Node ID of the target (dependency) file or module.
    relation: Semantic relation label (e.g. "imports", "resolved_imports").
    confidence: Confidence tier ("EXTRACTED" for structural, "INFERRED" for heuristic).*
- `CommunityResult` (line 82) `class CommunityResult` - *Result of community detection on the import graph.

Attributes:
    community_id: Integer identifier of the community.
    label: Human-readable name for the community.
    file_ids: Set of node IDs belonging to this community.
    cohesion: Cohesion score (internal edges / total edges involving community).
    size: Number of files in the community.*
- `AnalysisResult` (line 101) `class AnalysisResult` - *Complete graph analysis output.

Attributes:
    god_nodes: List of (node_id, score) for most central nodes.
    communities: List of CommunityResult instances.
    surprising_connections: List of (source_node, target_node, hops, bridging_communities).
    suggested_questions: List of plain-language exploration questions.
    node_count: Total nodes in the graph.
    edge_count: Total edges in the graph.*

**Methods:**
- `pluralize_symbol_kind` (line 72) `def pluralize_symbol_kind(kind, plural_map)` - *Return the plural form of *kind* according to *plural_map*.

Falls back to appending ``"s"`` when the kind is not found.
This prevents obvious misspellings like ``"Classs"``.*

#### `_parsers.py`
**Path:** `readmenator/_parsers.py`

**Classes:**
- `LanguageParser` (line 22) `class LanguageParser` - *Base class for all language-specific parsers.

Subclasses must implement ``_extract_specifics`` to populate
``self.symbols`` and ``self.imports``. Common utility methods
``_extract_docstring`` and ``_extract_signature`` are provided
for reuse across all parsers.*
- `CParser` (line 120) `class CParser(LanguageParser)` - *Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).

Extracts includes, structs, classes, functions, and preprocessor
macros using regex heuristics tuned to C-family syntax.*
- `PythonParser` (line 195) `class PythonParser(LanguageParser)` - *Parser for Python (.py) using the native ``ast`` module.

Extracts imports, functions (including async), and class
definitions with docstrings via ``ast.get_docstring``.*
- `GoParser` (line 269) `class GoParser(LanguageParser)` - *Parser for Go (.go).

Extracts import blocks or single import statements, exported
functions (including methods), and type definitions (struct/interface).*
- `RustParser` (line 311) `class RustParser(LanguageParser)` - *Parser for Rust (.rs).

Extracts ``use`` imports, public and private functions,
structs, traits, and enums.*
- `JavaScriptParser` (line 365) `class JavaScriptParser(LanguageParser)` - *Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).

Extracts ES module imports, CommonJS ``require`` calls, function
declarations, arrow-function variables, and class definitions
(including inheritance).*
- `JavaParser` (line 424) `class JavaParser(LanguageParser)` - *Parser for Java (.java).

Extracts import statements, class and interface declarations,
and methods complete with access modifiers and type signatures.*
- `CSharpParser` (line 463) `class CSharpParser(LanguageParser)` - *Parser for C# (.cs).

Extracts ``using`` directives, class/struct/interface/record
declarations, and methods with access modifiers.*
- `ShellParser` (line 502) `class ShellParser(LanguageParser)` - *Parser for shell scripts (.sh, .bash, .zsh).

Extracts function declarations in both POSIX (``name() {``)
and ``function`` keyword syntax.*
- `PHPParser` (line 527) `class PHPParser(LanguageParser)` - *Parser for PHP (.php).

Extracts ``use/require/include`` (including ``_once`` variants),
function declarations, and class declarations.*
- `DartParser` (line 561) `class DartParser(LanguageParser)` - *Parser for Dart (.dart).

Extracts import statements, class declarations (with extends),
and top-level or method function declarations by return type.*
- `GDScriptParser` (line 599) `class GDScriptParser(LanguageParser)` - *Parser for Godot GDScript (.gd).

Extracts ``extends`` / ``class_name`` directives and ``func``
method declarations.*
- `NimParser` (line 623) `class NimParser(LanguageParser)` - *Parser for Nim (.nim).

Extracts ``import`` statements, ``proc`` / ``func`` / ``method``
declarations, and ``type`` definitions.*
- `AssemblyParser` (line 657) `class AssemblyParser(LanguageParser)` - *Parser for assembly (.asm, .s, .S).

Extracts labels at the start of a line (``label:``) as function
symbols. This is a best-effort heuristic; local labels and
directives are not always distinguishable.*
- `RubyParser` (line 678) `class RubyParser(LanguageParser)` - *Parser for Ruby (.rb).

Extracts ``require`` / ``require_relative`` imports, class and
module definitions with inheritance, and method definitions.*
- `SwiftParser` (line 733) `class SwiftParser(LanguageParser)` - *Parser for Swift (.swift).

Extracts ``import`` statements, class/struct/enum/protocol
declarations with inheritance, and function definitions.*
- `KotlinParser` (line 803) `class KotlinParser(LanguageParser)` - *Parser for Kotlin (.kt, .kts).

Extracts ``import`` statements, class/object/interface/data class
declarations, and function definitions.*
- `ScalaParser` (line 868) `class ScalaParser(LanguageParser)` - *Parser for Scala (.scala).

Extracts ``import`` statements, class/object/trait declarations,
and method definitions.*
- `LuaParser` (line 933) `class LuaParser(LanguageParser)` - *Parser for Lua (.lua).

Extracts ``require`` imports, function declarations (named and
table-based), and module returns.*
- `ElixirParser` (line 983) `class ElixirParser(LanguageParser)` - *Parser for Elixir (.ex, .exs).

Extracts ``import``/``alias``/``require``/``use`` directives,
module definitions, and named function definitions.*

**Methods:**
- `create_parser` (line 1067) `def create_parser(extension, filename, config)` - *Factory: return a parser instance for *extension* or ``None``.

Looks up the extension in ``_PARSER_MAP`` (case-insensitive).
Returns ``None`` for unsupported extensions so the caller can
silently skip unknown file types.*
- `__init__` (line 31) `def __init__(self, filename, config)` - *Initialise the parser with a file path and application config.

Args:
    filename: Relative or absolute path of the source file.
    config: Application-wide configuration settings.*
- `parse` (line 46) `def parse(self, content)` - *Parse *content* and populate symbol/import lists.

Splits the source into lines, then delegates to the subclass-
specific ``_extract_specifics`` logic.*
- `_extract_specifics` (line 55) `def _extract_specifics(self, content)` - *Subclass hook for language-specific symbol extraction.*
- `_extract_docstring` (line 59) `def _extract_docstring(self, line_num)` - *Walk backwards from *line_num* to collect preceding comments/docstrings.

Supports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``
comment styles. Truncates at ``DOCSTRING_MAX_LENGTH`` and limits
lookback to ``DOCSTRING_LOOKBACK_LINES`` (both from Config).*
- `_extract_signature` (line 104) `def _extract_signature(self, content, match_start, pattern)` - *Extract a compact signature snippet starting at *match_start*.

Scans forward to the opening brace or a fallback length,
then truncates to 100 characters for display.*
- `_extract_specifics` (line 127) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 202) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 276) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 318) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 373) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 431) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 470) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 509) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 534) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 568) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 606) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 630) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 665) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 685) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 740) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 810) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 875) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 940) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 990) `def _extract_specifics(self, content)`

#### `_query.py`
**Path:** `readmenator/_query.py`

**Classes:**
- `QueryEngine` (line 17) `class QueryEngine` - *In-memory query engine over the scanned knowledge graph.

Builds a symbol-name index and an import-adjacency graph on
construction. Provides exact and fuzzy symbol lookup, detailed
explanation output, BFS shortest-path resolution, free-text
search, and a summary report.*

**Methods:**
- `__init__` (line 26) `def __init__(self, nodes, edges, resolved_edges)` - *Initialise internal indexes from scanned data.

Args:
    nodes: List of scanned file nodes.
    edges: List of import-relationship edges.
    resolved_edges: Optional resolved-import edges (both
        source and target are project file IDs).*
- `_build_symbol_index` (line 47) `def _build_symbol_index(self)` - *Build a name-to-list-of-(node, symbol) lookup.

Returns:
    Dict mapping symbol names to list of (Node, Symbol) tuples.*
- `_build_import_graph` (line 61) `def _build_import_graph(self)` - *Build an adjacency map from import edges.

Returns:
    Dict mapping each file node_id to its set of import targets.*
- `_build_resolved_graph` (line 77) `def _build_resolved_graph(self)` - *Build an adjacency map from resolved import edges.

Only contains edges where both source and target are
project files (not external modules).

Returns:
    Dict mapping each file node_id to files it imports within the project.*
- `find_symbol` (line 97) `def find_symbol(self, name)` - *Look up *name* by exact match, then by substring fuzzy match.

Returns:
    A list of (Node, Symbol) tuples, or ``None`` if not found.*
- `explain` (line 115) `def explain(self, name)` - *Return a detailed multi-line explanation of *name*.

Includes kind, file path, line number, docstring, signature,
imports, reverse dependencies ("imported by"), and sibling
symbols in the same file.

Returns:
    Formatted string or ``None`` if the symbol is not found.*
- `_find_incoming_imports` (line 154) `def _find_incoming_imports(self, target)` - *List all node IDs that import *target*.*
- `find_path` (line 162) `def find_path(self, symbol_a, symbol_b)` - *Find the shortest import path from *symbol_a* to *symbol_b*.

Uses BFS on the resolved import graph (project-internal edges)
first, traversing in both directions (forward = A imports B,
reverse = B is imported by A). Falls back to the raw import
graph if no resolved path exists.

Returns:
    List of file node IDs forming the dependency chain, or ``None``.*
- `_make_bidirectional` (line 192) `def _make_bidirectional(graph)` - *Convert a directed graph to a bidirectional one.

For each edge A→B, adds both A→B and B→A edges.*
- `_bfs_shortest_path` (line 208) `def _bfs_shortest_path(self, graph, start, goal)` - *Run BFS to find the shortest path from *start* to *goal*.

Returns:
    List of node IDs or ``None`` if no path exists.*
- `query` (line 232) `def query(self, question)` - *Free-text search over symbols and file paths.

Tokenises the input, matches against symbol names (substring)
and then against file paths as a fallback. Returns a
human-readable result string summarising matches or a
no-results message with KB statistics.*
- `summary` (line 288) `def summary(self)` - *Return a concise overview of the loaded knowledge base.

Reports file count, symbol count, import count, language
diversity, top-level modules (by import popularity), and
lists of key class-like and function-like symbols.*

#### `_resolver.py`
**Path:** `readmenator/_resolver.py`

**Classes:**
- `ImportResolver` (line 15) `class ImportResolver` - *Resolves raw import strings to project file paths.

Uses heuristics tuned to each language's import conventions:
Python dots to slashes, Java dots to directory separators,
relative-path resolution, and extensionless module detection.*

**Methods:**
- `__init__` (line 58) `def __init__(self, file_ids, root)` - *Initialise the resolver with all known file paths.

Args:
    file_ids: List of relative file paths from the scan.
    root: Root directory for relative-path resolution.*
- `_build_stem_index` (line 70) `def _build_stem_index(self, file_ids)` - *Map file stems (without extension) to their full paths.*
- `_build_dir_index` (line 80) `def _build_dir_index(self, file_ids)` - *Map directory paths to the files they contain.*
- `resolve` (line 97) `def resolve(self, import_str, source_file)` - *Resolve an import string to a concrete project file path.

Args:
    import_str: The raw import string from the parser.
    source_file: The file that contains the import (for relative resolution).

Returns:
    Matching file node ID or ``None`` if no match found.*
- `resolve_all` (line 132) `def resolve_all(self, import_str, source_file)` - *Resolve *import_str* to all possible matching project file paths.

Args:
    import_str: The raw import string.
    source_file: The file that contains the import.

Returns:
    List of matching file node IDs (may be empty).*
- `_resolve_relative` (line 148) `def _resolve_relative(self, import_str, source_file)` - *Resolve a relative import (starts with ``.`` or ``..``).*
- `_resolve_extensionless` (line 166) `def _resolve_extensionless(self, import_str, source_file)` - *Resolve a bare module name by appending known extensions.*
- `_resolve_directory_init` (line 175) `def _resolve_directory_init(self, import_str, source_file)` - *Resolve as a package directory with __init__ or index file.*
- `_resolve_module_dotpath` (line 185) `def _resolve_module_dotpath(self, import_str)` - *Resolve a dotted module path (Python/Java convention).*
- `_resolve_stem_match` (line 207) `def _resolve_stem_match(self, import_str)` - *Match by file stem only (last resort).*

#### `_scanner.py`
**Path:** `readmenator/_scanner.py`

**Classes:**
- `PolyglotScanner` (line 18) `class PolyglotScanner` - *Recursive directory scanner with security and size guards.

Rejects symlinks, enforces file-size and directory-depth limits,
skips ignored directories, and silently catches parse errors
so a single misbehaving file never breaks the full scan.*

**Methods:**
- `__init__` (line 26) `def __init__(self, config)` - *Initialise the scanner with application configuration.

Args:
    config: Settings including ignore dirs, size limits, etc.*
- `_is_ignored` (line 34) `def _is_ignored(self, path)` - *Return ``True`` if any path component matches IGNORE_DIRS.*
- `_validate_path_security` (line 38) `def _validate_path_security(self, path)` - *Reject symlinks and files exceeding MAX_FILE_SIZE_MB.*
- `_check_directory_depth` (line 51) `def _check_directory_depth(self, path, root)` - *Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.*
- `_extract_file_doc` (line 59) `def _extract_file_doc(self, content)` - *Extract a file-level docstring from the first lines of a source file.

Walks the first FILE_HEADER_MAX_LINES lines looking for a contiguous
block of comments or a shebang followed by comments. Returns the
concatenated comment text.

Args:
    content: Raw file content as a string.

Returns:
    Extracted file-level docstring or empty string.*
- `_emit_progress` (line 115) `def _emit_progress(self, count)` - *Emit a progress message every PROGRESS_REPORT_BATCH files.

Args:
    count: Number of files scanned so far.*
- `scan` (line 125) `def scan(self, root)` - *Walk *root* recursively and produce (nodes, edges) for the graph.

Security checks (symlinks, size, depth, ignore dirs) are applied
per file. Parse failures are silently caught so a single broken
file never blocks the rest of the scan.

Returns:
    A tuple of (list of Node, list of Edge). Edges represent
    ``imports`` relationships between scanned files.*

#### `_watcher.py`
**Path:** `readmenator/_watcher.py`

**Classes:**
- `DirectoryWatcher` (line 18) `class DirectoryWatcher` - *Polling-based directory watcher for auto-rebuild on changes.

Computes a combined hash of all tracked files (filenames + sizes)
and triggers a callback when the hash changes. Uses polling to
avoid external dependencies like watchdog or inotify.*

**Methods:**
- `__init__` (line 26) `def __init__(self, root, config, callback, interval_seconds)` - *Initialise the watcher for a project root.

Args:
    root: Project directory to watch.
    config: Application configuration.
    callback: Function called when changes are detected.
    interval_seconds: Polling interval in seconds.*
- `_compute_snapshot` (line 48) `def _compute_snapshot(self)` - *Compute a quick hash of all tracked files in the project.

Uses file paths and sizes (not full content) for speed.
Returns a hex digest that changes when files are added,
removed, or modified.*
- `start` (line 77) `def start(self)` - *Start watching the directory (blocking).*
- `stop` (line 94) `def stop(self)` - *Stop watching.*

#### `readmenator.py`
**Path:** `readmenator.py`

*No symbols extracted*

#### `readmenator_orchestrator.py`
**Path:** `readmenator_orchestrator.py`

**Classes:**
- `Config` (line 15) `class Config` - *Centralized, immutable configuration. No magic numbers or hardcoded paths.*
- `GitHubClient` (line 38) `class GitHubClient` - *Handles all interactions with the GitHub API via the gh CLI.*
- `RepositoryProcessor` (line 123) `class RepositoryProcessor` - *Processes individual repositories: clones, generates docs, commits, and pushes.*
- `Orchestrator` (line 254) `class Orchestrator` - *Main orchestrator that coordinates the documentation generation across all repositories.*
- `TestOrchestrator` (line 310) `class TestOrchestrator(TestCase)` - *Test suite for the ReadMenator Orchestrator (SDD + TDD + BDD).*

**Methods:**
- `parse_arguments` (line 346) `def parse_arguments()` - *Parses command line arguments.*
- `main` (line 355) `def main()` - *Main entry point for the orchestrator.*
- `__init__` (line 41) `def __init__(self, config)` - *Initializes the client with configuration and resolves the GitHub user.*
- `_resolve_user` (line 47) `def _resolve_user(self)` - *Resolves the authenticated GitHub username.*
- `_setup_git_auth` (line 65) `def _setup_git_auth(self)` - *Configures Git to use gh CLI for authentication globally.*
- `list_repos` (line 76) `def list_repos(self)` - *Retrieves a list of all repositories for the authenticated user.*
- `close_existing_prs` (line 84) `def close_existing_prs(self, repo)` - *Closes all existing pull requests for the target branch.*
- `delete_remote_branch` (line 99) `def delete_remote_branch(self, repo)` - *Deletes the remote target branch if it exists.*
- `create_pr` (line 106) `def create_pr(self, repo, default_branch, timestamp)` - *Creates a new pull request for the generated documentation.*
- `__init__` (line 126) `def __init__(self, config, github_client)` - *Initializes the processor with configuration and GitHub client.*
- `process` (line 131) `def process(self, repo)` - *Executes the full processing pipeline for a single repository.*
- `_get_default_branch` (line 156) `def _get_default_branch(self, repo)` - *Retrieves the default branch name for the repository.*
- `_clone_repository` (line 167) `def _clone_repository(self, repo)` - *Clones the repository into a secure temporary directory.*
- `_run_readmenator` (line 183) `def _run_readmenator(self, repo_dir)`
- `_copy_to_docs_dir` (line 202) `def _copy_to_docs_dir(self, repo_dir, generated_file)` - *Copies the generated knowledge base to the docs subdirectory.*
- `_commit_and_push` (line 209) `def _commit_and_push(self, repo_dir, repo)` - *Commits and pushes the generated documentation to the target branch.*
- `_cleanup_temp_dir` (line 248) `def _cleanup_temp_dir(self, temp_dir)` - *Safely removes the temporary directory.*
- `__init__` (line 257) `def __init__(self, config)` - *Initializes the orchestrator with configuration.*
- `run` (line 263) `def run(self, dry_run, only_repo)` - *Executes the orchestration pipeline.*
- `setUp` (line 313) `def setUp(self)` - *Sets up test fixtures.*
- `tearDown` (line 318) `def tearDown(self)` - *Tears down test fixtures.*
- `test_config_immutability` (line 322) `def test_config_immutability(self)` - *Validates that the Config dataclass is immutable.*
- `test_config_defaults` (line 327) `def test_config_defaults(self)` - *Validates default configuration values.*
- `test_skip_repos_logic` (line 334) `def test_skip_repos_logic(self)` - *Validates that critical repositories are skipped by default.*
- `test_jq_filter_escaping` (line 339) `def test_jq_filter_escaping(self)` - *Validates that jq filters are safely escaped against injection.*

#### `__init__.py`
**Path:** `tests/__init__.py`

*No symbols extracted*

#### `test_analyzer.py`
**Path:** `tests/test_analyzer.py`

**Classes:**
- `TestGraphAnalyzerContract` (line 16) `class TestGraphAnalyzerContract(TestCase)` - *Contract: GraphAnalyzer provides graph intelligence.*

**Methods:**
- `setUp` (line 19) `def setUp(self)`
- `_make_node` (line 23) `def _make_node(self, nid, label, lang)`
- `_make_edge` (line 26) `def _make_edge(self, src, tgt, rel)`
- `test_analyze_empty_graph_returns_empty_result` (line 29) `def test_analyze_empty_graph_returns_empty_result(self)`
- `test_analyze_detects_communities_for_connected_graph` (line 34) `def test_analyze_detects_communities_for_connected_graph(self)`
- `test_analyze_computes_god_nodes` (line 48) `def test_analyze_computes_god_nodes(self)`
- `test_analyze_finds_surprising_connections` (line 64) `def test_analyze_finds_surprising_connections(self)`
- `test_analyze_generates_questions` (line 81) `def test_analyze_generates_questions(self)`
- `test_community_cohesion_is_between_zero_and_one` (line 92) `def test_community_cohesion_is_between_zero_and_one(self)`
- `test_isolated_nodes_do_not_form_communities` (line 107) `def test_isolated_nodes_do_not_form_communities(self)`
- `test_analyze_with_resolved_edges_counts_them` (line 116) `def test_analyze_with_resolved_edges_counts_them(self)`

#### `test_cache.py`
**Path:** `tests/test_cache.py`

**Classes:**
- `TestFileCacheContract` (line 18) `class TestFileCacheContract(TestCase)` - *Contract: FileCache provides SHA256-based incremental scan support.*

**Methods:**
- `setUp` (line 21) `def setUp(self)`
- `tearDown` (line 26) `def tearDown(self)`
- `_write` (line 30) `def _write(self, rel_path, content)`
- `test_compute_hash_returns_hex_string` (line 36) `def test_compute_hash_returns_hex_string(self)`
- `test_different_content_produces_different_hash` (line 42) `def test_different_content_produces_different_hash(self)`
- `test_same_content_produces_same_hash` (line 49) `def test_same_content_produces_same_hash(self)`
- `test_load_returns_empty_dict_when_no_cache` (line 56) `def test_load_returns_empty_dict_when_no_cache(self)`
- `test_save_and_load_roundtrip` (line 60) `def test_save_and_load_roundtrip(self)`
- `test_find_changed_detects_new_files` (line 66) `def test_find_changed_detects_new_files(self)`
- `test_find_changed_detects_modified_files` (line 71) `def test_find_changed_detects_modified_files(self)`
- `test_find_changed_skips_unchanged_files` (line 78) `def test_find_changed_skips_unchanged_files(self)`
- `test_prune_deleted_removes_ghost_entries` (line 85) `def test_prune_deleted_removes_ghost_entries(self)`
- `test_compute_hashes_batch` (line 92) `def test_compute_hashes_batch(self)`
- `test_nonexistent_file_returns_empty_hash` (line 100) `def test_nonexistent_file_returns_empty_hash(self)`

#### `test_config.py`
**Path:** `tests/test_config.py`

**Classes:**
- `TestConfigContract` (line 7) `class TestConfigContract(TestCase)`

**Methods:**
- `test_config_is_immutable` (line 8) `def test_config_is_immutable(self)`
- `test_config_defaults_are_sane` (line 13) `def test_config_defaults_are_sane(self)`
- `test_ignore_dirs_are_comprehensive` (line 25) `def test_ignore_dirs_are_comprehensive(self)`
- `test_plural_map_covers_all_symbol_types` (line 31) `def test_plural_map_covers_all_symbol_types(self)`
- `test_supported_extensions_no_duplicates` (line 42) `def test_supported_extensions_no_duplicates(self)`

#### `test_documentation.py`
**Path:** `tests/test_documentation.py`

**Classes:**
- `TestDocumentationGeneratorContract` (line 8) `class TestDocumentationGeneratorContract(TestCase)`

**Methods:**
- `setUp` (line 9) `def setUp(self)`
- `test_contains_header` (line 13) `def test_contains_header(self)`
- `test_contains_metadata_line` (line 17) `def test_contains_metadata_line(self)`
- `test_contains_mermaid_block` (line 23) `def test_contains_mermaid_block(self)`
- `test_contains_architecture_reference` (line 28) `def test_contains_architecture_reference(self)`
- `test_groups_files_by_language` (line 32) `def test_groups_files_by_language(self)`
- `test_lists_symbols_under_file` (line 51) `def test_lists_symbols_under_file(self)`
- `test_class_symbol_is_pluralized_correctly` (line 64) `def test_class_symbol_is_pluralized_correctly(self)`
- `test_function_pluralization` (line 78) `def test_function_pluralization(self)`
- `test_method_pluralization` (line 90) `def test_method_pluralization(self)`
- `test_shows_no_symbols_for_empty_files` (line 102) `def test_shows_no_symbols_for_empty_files(self)`
- `test_includes_file_path` (line 113) `def test_includes_file_path(self)`
- `test_docstring_in_output` (line 124) `def test_docstring_in_output(self)`
- `test_truncation_note_when_limited` (line 136) `def test_truncation_note_when_limited(self)`

#### `test_exporter.py`
**Path:** `tests/test_exporter.py`

**Classes:**
- `TestGraphExporterContract` (line 23) `class TestGraphExporterContract(TestCase)` - *Contract: GraphExporter produces valid JSON, HTML, and SVG outputs.*

**Methods:**
- `setUp` (line 26) `def setUp(self)`
- `_make_node` (line 30) `def _make_node(self, nid, label, lang, symbols)`
- `_make_sym` (line 42) `def _make_sym(self, name, kind, line)`
- `test_to_json_produces_valid_json` (line 47) `def test_to_json_produces_valid_json(self)`
- `test_to_json_includes_symbol_data` (line 56) `def test_to_json_includes_symbol_data(self)`
- `test_to_json_includes_metadata` (line 65) `def test_to_json_includes_metadata(self)`
- `test_to_json_includes_analysis_metadata` (line 76) `def test_to_json_includes_analysis_metadata(self)`
- `test_to_html_produces_standalone_page` (line 101) `def test_to_html_produces_standalone_page(self)`
- `test_to_html_includes_node_data` (line 109) `def test_to_html_includes_node_data(self)`
- `test_to_html_includes_community_legend_when_analysis` (line 116) `def test_to_html_includes_community_legend_when_analysis(self)`
- `test_to_svg_produces_svg_string` (line 138) `def test_to_svg_produces_svg_string(self)`
- `test_to_svg_render_truncation_for_large_graph` (line 145) `def test_to_svg_render_truncation_for_large_graph(self)`
- `test_to_svg_includes_readmenator_title` (line 154) `def test_to_svg_includes_readmenator_title(self)`
- `test_to_json_handles_resolved_edges` (line 160) `def test_to_json_handles_resolved_edges(self)`

#### `test_integration.py`
**Path:** `tests/test_integration.py`

**Classes:**
- `TestEndToEndContract` (line 9) `class TestEndToEndContract(TestCase)`

**Methods:**
- `setUp` (line 10) `def setUp(self)`
- `tearDown` (line 15) `def tearDown(self)`
- `_write` (line 19) `def _write(self, path, content)`
- `test_full_pipeline_generates_knowledge_base` (line 24) `def test_full_pipeline_generates_knowledge_base(self)`
- `test_knowledge_base_contains_mermaid` (line 40) `def test_knowledge_base_contains_mermaid(self)`
- `test_query_subcommand_works` (line 48) `def test_query_subcommand_works(self)`
- `test_explain_subcommand_works` (line 53) `def test_explain_subcommand_works(self)`
- `test_path_subcommand_works` (line 59) `def test_path_subcommand_works(self)`
- `test_summary_works` (line 65) `def test_summary_works(self)`
- `test_rebuild` (line 71) `def test_rebuild(self)`

#### `test_mermaid.py`
**Path:** `tests/test_mermaid.py`

**Classes:**
- `TestMermaidRendererContract` (line 8) `class TestMermaidRendererContract(TestCase)`

**Methods:**
- `setUp` (line 9) `def setUp(self)`
- `test_renders_graph_header` (line 13) `def test_renders_graph_header(self)`
- `test_renders_module_node` (line 21) `def test_renders_module_node(self)`
- `test_renders_symbol_subnodes` (line 33) `def test_renders_symbol_subnodes(self)`
- `test_class_symbol_gets_cls_style` (line 45) `def test_class_symbol_gets_cls_style(self)`
- `test_function_symbol_gets_fn_style` (line 57) `def test_function_symbol_gets_fn_style(self)`
- `test_external_import_edge_is_dashed` (line 69) `def test_external_import_edge_is_dashed(self)`
- `test_truncation_when_over_limit` (line 81) `def test_truncation_when_over_limit(self)`
- `test_limits_symbols_to_five_per_node` (line 92) `def test_limits_symbols_to_five_per_node(self)`
- `test_handles_special_characters_in_ids` (line 107) `def test_handles_special_characters_in_ids(self)`

#### `test_models.py`
**Path:** `tests/test_models.py`

**Classes:**
- `TestSymbolContract` (line 6) `class TestSymbolContract(TestCase)`
- `TestNodeContract` (line 20) `class TestNodeContract(TestCase)`
- `TestEdgeContract` (line 48) `class TestEdgeContract(TestCase)`
- `TestPluralizeContract` (line 56) `class TestPluralizeContract(TestCase)`

**Methods:**
- `test_symbol_creation` (line 7) `def test_symbol_creation(self)`
- `test_symbol_with_signature` (line 15) `def test_symbol_with_signature(self)`
- `test_node_creation` (line 21) `def test_node_creation(self)`
- `test_node_with_symbols` (line 35) `def test_node_with_symbols(self)`
- `test_edge_creation` (line 49) `def test_edge_creation(self)`
- `test_pluralize_class` (line 57) `def test_pluralize_class(self)`
- `test_pluralize_unknown_appends_s` (line 62) `def test_pluralize_unknown_appends_s(self)`

#### `test_parsers.py`
**Path:** `tests/test_parsers.py`

**Classes:**
- `TestCParserContract` (line 22) `class TestCParserContract(TestCase)`
- `TestPythonParserContract` (line 72) `class TestPythonParserContract(TestCase)`
- `TestGoParserContract` (line 141) `class TestGoParserContract(TestCase)`
- `TestRustParserContract` (line 184) `class TestRustParserContract(TestCase)`
- `TestJavaScriptParserContract` (line 222) `class TestJavaScriptParserContract(TestCase)`
- `TestJavaParserContract` (line 261) `class TestJavaParserContract(TestCase)`
- `TestCSharpParserContract` (line 293) `class TestCSharpParserContract(TestCase)`
- `TestShellParserContract` (line 326) `class TestShellParserContract(TestCase)`
- `TestPHPParserContract` (line 345) `class TestPHPParserContract(TestCase)`
- `TestDartParserContract` (line 371) `class TestDartParserContract(TestCase)`
- `TestGDScriptParserContract` (line 396) `class TestGDScriptParserContract(TestCase)`
- `TestNimParserContract` (line 414) `class TestNimParserContract(TestCase)`
- `TestAssemblyParserContract` (line 440) `class TestAssemblyParserContract(TestCase)`
- `TestParserFactoryContract` (line 460) `class TestParserFactoryContract(TestCase)`

**Methods:**
- `setUp` (line 23) `def setUp(self)`
- `test_extracts_function` (line 26) `def test_extracts_function(self)`
- `test_extracts_struct` (line 33) `def test_extracts_struct(self)`
- `test_extracts_include` (line 40) `def test_extracts_include(self)`
- `test_extracts_define` (line 47) `def test_extracts_define(self)`
- `test_skips_reserved_words` (line 54) `def test_skips_reserved_words(self)`
- `test_class_with_inheritance` (line 64) `def test_class_with_inheritance(self)`
- `setUp` (line 73) `def setUp(self)`
- `test_extracts_function` (line 76) `def test_extracts_function(self)`
- `test_extracts_class` (line 83) `def test_extracts_class(self)`
- `test_extracts_imports` (line 90) `def test_extracts_imports(self)`
- `test_extracts_async_function` (line 98) `def test_extracts_async_function(self)`
- `test_handles_syntax_error_gracefully` (line 105) `def test_handles_syntax_error_gracefully(self)`
- `test_suppresses_syntax_warnings` (line 111) `def test_suppresses_syntax_warnings(self)`
- `test_extracts_signature_with_params` (line 123) `def test_extracts_signature_with_params(self)`
- `test_extracts_class_with_bases` (line 131) `def test_extracts_class_with_bases(self)`
- `setUp` (line 142) `def setUp(self)`
- `test_extracts_function` (line 145) `def test_extracts_function(self)`
- `test_extracts_method_receiver` (line 152) `def test_extracts_method_receiver(self)`
- `test_extracts_import_block` (line 159) `def test_extracts_import_block(self)`
- `test_extracts_single_import` (line 166) `def test_extracts_single_import(self)`
- `test_extracts_struct_and_interface` (line 172) `def test_extracts_struct_and_interface(self)`
- `setUp` (line 185) `def setUp(self)`
- `test_extracts_function` (line 188) `def test_extracts_function(self)`
- `test_extracts_pub_function` (line 195) `def test_extracts_pub_function(self)`
- `test_extracts_struct_and_trait_and_enum` (line 202) `def test_extracts_struct_and_trait_and_enum(self)`
- `test_extracts_use` (line 215) `def test_extracts_use(self)`
- `setUp` (line 223) `def setUp(self)`
- `test_extracts_function` (line 226) `def test_extracts_function(self)`
- `test_extracts_arrow_function` (line 233) `def test_extracts_arrow_function(self)`
- `test_extracts_class` (line 240) `def test_extracts_class(self)`
- `test_extracts_import_and_require` (line 247) `def test_extracts_import_and_require(self)`
- `test_skips_reserved_words` (line 254) `def test_skips_reserved_words(self)`
- `setUp` (line 262) `def setUp(self)`
- `test_extracts_class` (line 265) `def test_extracts_class(self)`
- `test_extracts_method` (line 272) `def test_extracts_method(self)`
- `test_extracts_import` (line 279) `def test_extracts_import(self)`
- `test_abstract_class` (line 285) `def test_abstract_class(self)`
- `setUp` (line 294) `def setUp(self)`
- `test_extracts_class` (line 297) `def test_extracts_class(self)`
- `test_extracts_method` (line 304) `def test_extracts_method(self)`
- `test_extracts_using` (line 311) `def test_extracts_using(self)`
- `test_record_and_interface` (line 317) `def test_record_and_interface(self)`
- `setUp` (line 327) `def setUp(self)`
- `test_extracts_function_with_parentheses` (line 330) `def test_extracts_function_with_parentheses(self)`
- `test_extracts_function_keyword` (line 337) `def test_extracts_function_keyword(self)`
- `setUp` (line 346) `def setUp(self)`
- `test_extracts_function` (line 349) `def test_extracts_function(self)`
- `test_extracts_class` (line 356) `def test_extracts_class(self)`
- `test_extracts_use_and_require` (line 363) `def test_extracts_use_and_require(self)`
- `setUp` (line 372) `def setUp(self)`
- `test_extracts_class` (line 375) `def test_extracts_class(self)`
- `test_extracts_function` (line 382) `def test_extracts_function(self)`
- `test_extracts_import` (line 389) `def test_extracts_import(self)`
- `setUp` (line 397) `def setUp(self)`
- `test_extracts_function` (line 400) `def test_extracts_function(self)`
- `test_extracts_extends` (line 407) `def test_extracts_extends(self)`
- `setUp` (line 415) `def setUp(self)`
- `test_extracts_proc` (line 418) `def test_extracts_proc(self)`
- `test_extracts_type` (line 425) `def test_extracts_type(self)`
- `test_extracts_import` (line 432) `def test_extracts_import(self)`
- `setUp` (line 441) `def setUp(self)`
- `test_extracts_label` (line 444) `def test_extracts_label(self)`
- `test_extracts_multiple_labels` (line 451) `def test_extracts_multiple_labels(self)`
- `setUp` (line 461) `def setUp(self)`
- `test_returns_c_parser_for_c_extensions` (line 464) `def test_returns_c_parser_for_c_extensions(self)`
- `test_returns_python_parser_for_py` (line 470) `def test_returns_python_parser_for_py(self)`
- `test_returns_none_for_unknown_extension` (line 475) `def test_returns_none_for_unknown_extension(self)`
- `test_returns_rust_parser_for_rs` (line 479) `def test_returns_rust_parser_for_rs(self)`
- `test_case_insensitive_extension` (line 484) `def test_case_insensitive_extension(self)`

#### `test_parsers_new.py`
**Path:** `tests/test_parsers_new.py`

**Classes:**
- `TestRubyParserContract` (line 15) `class TestRubyParserContract(TestCase)`
- `TestSwiftParserContract` (line 45) `class TestSwiftParserContract(TestCase)`
- `TestKotlinParserContract` (line 68) `class TestKotlinParserContract(TestCase)`
- `TestScalaParserContract` (line 85) `class TestScalaParserContract(TestCase)`
- `TestLuaParserContract` (line 102) `class TestLuaParserContract(TestCase)`
- `TestElixirParserContract` (line 117) `class TestElixirParserContract(TestCase)`
- `TestNewParserFactoryContract` (line 134) `class TestNewParserFactoryContract(TestCase)`
- `TestPythonCallExtractionContract` (line 151) `class TestPythonCallExtractionContract(TestCase)`

**Methods:**
- `setUp` (line 16) `def setUp(self)`
- `test_extracts_class_with_inheritance` (line 19) `def test_extracts_class_with_inheritance(self)`
- `test_extracts_module` (line 27) `def test_extracts_module(self)`
- `test_extracts_method` (line 33) `def test_extracts_method(self)`
- `test_extracts_require` (line 39) `def test_extracts_require(self)`
- `setUp` (line 46) `def setUp(self)`
- `test_extracts_class` (line 49) `def test_extracts_class(self)`
- `test_extracts_function` (line 55) `def test_extracts_function(self)`
- `test_extracts_protocol` (line 61) `def test_extracts_protocol(self)`
- `setUp` (line 69) `def setUp(self)`
- `test_extracts_class` (line 72) `def test_extracts_class(self)`
- `test_extracts_fun` (line 78) `def test_extracts_fun(self)`
- `setUp` (line 86) `def setUp(self)`
- `test_extracts_object` (line 89) `def test_extracts_object(self)`
- `test_extracts_def` (line 95) `def test_extracts_def(self)`
- `setUp` (line 103) `def setUp(self)`
- `test_extracts_function` (line 106) `def test_extracts_function(self)`
- `test_extracts_require` (line 111) `def test_extracts_require(self)`
- `setUp` (line 118) `def setUp(self)`
- `test_extracts_defmodule` (line 121) `def test_extracts_defmodule(self)`
- `test_extracts_function` (line 127) `def test_extracts_function(self)`
- `setUp` (line 135) `def setUp(self)`
- `test_ruby_extension_maps_correctly` (line 138) `def test_ruby_extension_maps_correctly(self)`
- `test_swift_extension_maps_correctly` (line 142) `def test_swift_extension_maps_correctly(self)`
- `test_kotlin_extension_maps_correctly` (line 146) `def test_kotlin_extension_maps_correctly(self)`
- `setUp` (line 152) `def setUp(self)`
- `test_extracts_class_inheritance` (line 155) `def test_extracts_class_inheritance(self)`
- `test_extracts_function_calls` (line 160) `def test_extracts_function_calls(self)`

#### `test_query.py`
**Path:** `tests/test_query.py`

**Classes:**
- `TestQueryEngineContract` (line 22) `class TestQueryEngineContract(TestCase)`

**Functions:**
- `_make_node` (line 7) `def _make_node(node_id, symbols)`
- `_make_sym` (line 18) `def _make_sym(name, kind, line)`

**Methods:**
- `setUp` (line 23) `def setUp(self)`
- `test_find_exact_symbol` (line 36) `def test_find_exact_symbol(self)`
- `test_find_symbol_fuzzy` (line 42) `def test_find_symbol_fuzzy(self)`
- `test_find_symbol_not_found` (line 47) `def test_find_symbol_not_found(self)`
- `test_explain_returns_details` (line 51) `def test_explain_returns_details(self)`
- `test_explain_shows_imports` (line 58) `def test_explain_shows_imports(self)`
- `test_explain_shows_siblings` (line 63) `def test_explain_shows_siblings(self)`
- `test_explain_unknown_returns_none` (line 69) `def test_explain_unknown_returns_none(self)`
- `test_find_path_direct_import` (line 73) `def test_find_path_direct_import(self)`
- `test_find_path_same_file` (line 79) `def test_find_path_same_file(self)`
- `test_find_path_unknown_returns_none` (line 84) `def test_find_path_unknown_returns_none(self)`
- `test_summary_shows_counts` (line 88) `def test_summary_shows_counts(self)`
- `test_summary_shows_top_modules` (line 94) `def test_summary_shows_top_modules(self)`
- `test_query_returns_matching_symbols` (line 98) `def test_query_returns_matching_symbols(self)`
- `test_query_returns_file_matches` (line 102) `def test_query_returns_file_matches(self)`

#### `test_resolver.py`
**Path:** `tests/test_resolver.py`

**Classes:**
- `TestImportResolverContract` (line 15) `class TestImportResolverContract(TestCase)` - *Contract: ImportResolver maps import strings to file paths.*

**Methods:**
- `test_resolves_python_module_dotpath` (line 18) `def test_resolves_python_module_dotpath(self)`
- `test_resolves_relative_import` (line 25) `def test_resolves_relative_import(self)`
- `test_resolves_extensionless_python_import` (line 32) `def test_resolves_extensionless_python_import(self)`
- `test_resolves_package_init` (line 39) `def test_resolves_package_init(self)`
- `test_returns_none_for_external_stdlib` (line 46) `def test_returns_none_for_external_stdlib(self)`
- `test_returns_none_for_unknown_import` (line 53) `def test_returns_none_for_unknown_import(self)`
- `test_resolves_stem_match_when_unique` (line 60) `def test_resolves_stem_match_when_unique(self)`
- `test_returns_none_for_empty_import` (line 67) `def test_returns_none_for_empty_import(self)`
- `test_resolves_go_import` (line 72) `def test_resolves_go_import(self)`
- `test_resolves_same_directory_import` (line 79) `def test_resolves_same_directory_import(self)`

#### `test_scanner.py`
**Path:** `tests/test_scanner.py`

**Classes:**
- `TestScannerContract` (line 10) `class TestScannerContract(TestCase)`

**Methods:**
- `setUp` (line 11) `def setUp(self)`
- `tearDown` (line 15) `def tearDown(self)`
- `_write` (line 19) `def _write(self, path, content)`
- `test_scans_python_files` (line 24) `def test_scans_python_files(self)`
- `test_ignores_env_and_vendor_dirs` (line 31) `def test_ignores_env_and_vendor_dirs(self)`
- `test_rejects_symlinks` (line 44) `def test_rejects_symlinks(self)`
- `test_skips_non_code_files` (line 58) `def test_skips_non_code_files(self)`
- `test_scans_multiple_languages` (line 69) `def test_scans_multiple_languages(self)`
- `test_respects_max_directory_depth` (line 78) `def test_respects_max_directory_depth(self)`
- `test_raises_on_invalid_directory` (line 88) `def test_raises_on_invalid_directory(self)`
- `test_import_edges_are_created` (line 93) `def test_import_edges_are_created(self)`
