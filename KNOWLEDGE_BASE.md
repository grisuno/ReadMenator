# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 21 | **Total Symbols Extracted:** 271 | **Total Imports:** 99

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
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
    readmenator__app_py_run["run"]
    class readmenator__app_py_run fn;
    readmenator__app_py --> readmenator__app_py_run
    readmenator__app_py_query["query"]
    class readmenator__app_py_query fn;
    readmenator__app_py --> readmenator__app_py_query
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
    readmenator__query_py_find_symbol["find_symbol"]
    class readmenator__query_py_find_symbol fn;
    readmenator__query_py --> readmenator__query_py_find_symbol
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
    readmenator__config_py["_config.py (py)"]
    class readmenator__config_py mod;
    readmenator__config_py_Config["Config"]
    class readmenator__config_py_Config cls;
    readmenator__config_py --> readmenator__config_py_Config
    readmenator___init___py["__init__.py (py)"]
    class readmenator___init___py mod;
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
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
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
    ext_os["os"]
    class ext_os ext;
    readmenator___main___py -.->|imports| ext_os
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
    readmenator__app_py -.->|imports| ext___future__
    readmenator__app_py -.->|imports| ext_pathlib
    ext_typing["typing"]
    class ext_typing ext;
    readmenator__app_py -.->|imports| ext_typing
    readmenator__app_py -.->|imports| ext_readmenator__config
    ext_readmenator__documentation["readmenator._documentation"]
    class ext_readmenator__documentation ext;
    readmenator__app_py -.->|imports| ext_readmenator__documentation
    readmenator__app_py -.->|imports| ext_readmenator__models
    ext_readmenator__query["readmenator._query"]
    class ext_readmenator__query ext;
    readmenator__app_py -.->|imports| ext_readmenator__query
    ext_readmenator__scanner["readmenator._scanner"]
    class ext_readmenator__scanner ext;
    readmenator__app_py -.->|imports| ext_readmenator__scanner
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
    ext_collections["collections"]
    class ext_collections ext;
    readmenator__query_py -.->|imports| ext_collections
    readmenator__query_py -.->|imports| ext_typing
    readmenator__query_py -.->|imports| ext_readmenator__models
    readmenator__scanner_py -.->|imports| ext___future__
    readmenator__scanner_py -.->|imports| ext_pathlib
    readmenator__scanner_py -.->|imports| ext_typing
    readmenator__scanner_py -.->|imports| ext_readmenator__config
    readmenator__scanner_py -.->|imports| ext_readmenator__models
    ext_readmenator__parsers["readmenator._parsers"]
    class ext_readmenator__parsers ext;
    readmenator__scanner_py -.->|imports| ext_readmenator__parsers
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
    tests_test_config_py -.->|imports| ext_unittest
    tests_test_config_py -.->|imports| ext_dataclasses
    tests_test_config_py -.->|imports| ext_readmenator__config
    tests_test_documentation_py -.->|imports| ext_unittest
    tests_test_documentation_py -.->|imports| ext_readmenator__config
    tests_test_documentation_py -.->|imports| ext_readmenator__documentation
    tests_test_documentation_py -.->|imports| ext_readmenator__models
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
    tests_test_query_py -.->|imports| ext_unittest
    tests_test_query_py -.->|imports| ext_readmenator__models
    tests_test_query_py -.->|imports| ext_readmenator__query
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

### PY (21 files)

#### `__init__.py`
**Path:** `readmenator/__init__.py`

*No symbols extracted*

#### `__main__.py`
**Path:** `readmenator/__main__.py`

**Functions:**
- `build_parser` (line 12) `def build_parser()`
- `_run_tests` (line 47) `def _run_tests()`
- `main` (line 62) `def main()`

#### `_app.py`
**Path:** `readmenator/_app.py`

**Classes:**
- `readmenatorApplication` (line 13) `class readmenatorApplication`

**Functions:**
- `__init__` (line 14) `def __init__(self, config)`
- `_scan` (line 21) `def _scan(self, target_dir)`
- `run` (line 28) `def run(self, target_dir)`
- `query` (line 42) `def query(self, target_dir, question)`
- `explain` (line 47) `def explain(self, target_dir, symbol_name)`
- `find_path` (line 59) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (line 72) `def summary(self, target_dir)`
- `rebuild` (line 77) `def rebuild(self, target_dir)`

#### `_config.py`
**Path:** `readmenator/_config.py`

**Classes:**
- `Config` (line 8) `class Config`

#### `_documentation.py`
**Path:** `readmenator/_documentation.py`

**Classes:**
- `DocumentationGenerator` (line 10) `class DocumentationGenerator`

**Functions:**
- `__init__` (line 11) `def __init__(self, config)`
- `generate` (line 16) `def generate(self, nodes, edges)`

#### `_mermaid.py`
**Path:** `readmenator/_mermaid.py`

**Classes:**
- `MermaidRenderer` (line 10) `class MermaidRenderer`

**Functions:**
- `__init__` (line 11) `def __init__(self, config)`
- `_sanitize_id` (line 14) `def _sanitize_id(self, node_id)`
- `render` (line 20) `def render(self, nodes, edges)`

#### `_models.py`
**Path:** `readmenator/_models.py`

**Classes:**
- `Symbol` (line 8) `class Symbol`
- `Node` (line 17) `class Node`
- `Edge` (line 27) `class Edge`

**Functions:**
- `pluralize_symbol_kind` (line 33) `def pluralize_symbol_kind(kind, plural_map)`

#### `_parsers.py`
**Path:** `readmenator/_parsers.py`

**Classes:**
- `LanguageParser` (line 12) `class LanguageParser`
- `CParser` (line 77) `class CParser(LanguageParser)`
- `PythonParser` (line 146) `class PythonParser(LanguageParser)`
- `GoParser` (line 193) `class GoParser(LanguageParser)`
- `RustParser` (line 229) `class RustParser(LanguageParser)`
- `JavaScriptParser` (line 277) `class JavaScriptParser(LanguageParser)`
- `JavaParser` (line 320) `class JavaParser(LanguageParser)`
- `CSharpParser` (line 353) `class CSharpParser(LanguageParser)`
- `ShellParser` (line 386) `class ShellParser(LanguageParser)`
- `PHPParser` (line 405) `class PHPParser(LanguageParser)`
- `DartParser` (line 433) `class DartParser(LanguageParser)`
- `GDScriptParser` (line 465) `class GDScriptParser(LanguageParser)`
- `NimParser` (line 483) `class NimParser(LanguageParser)`
- `AssemblyParser` (line 511) `class AssemblyParser(LanguageParser)`

**Functions:**
- `create_parser` (line 555) `def create_parser(extension, filename, config)`
- `__init__` (line 13) `def __init__(self, filename, config)`
- `parse` (line 20) `def parse(self, content)`
- `_extract_specifics` (line 24) `def _extract_specifics(self, content)`
- `_extract_docstring` (line 27) `def _extract_docstring(self, line_num)`
- `_extract_signature` (line 66) `def _extract_signature(self, content, match_start, pattern)`
- `_extract_specifics` (line 78) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 147) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 194) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 230) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 278) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 321) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 354) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 387) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 406) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 434) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 466) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 484) `def _extract_specifics(self, content)`
- `_extract_specifics` (line 512) `def _extract_specifics(self, content)`

#### `_query.py`
**Path:** `readmenator/_query.py`

**Classes:**
- `QueryEngine` (line 9) `class QueryEngine`

**Functions:**
- `__init__` (line 10) `def __init__(self, nodes, edges)`
- `_build_symbol_index` (line 16) `def _build_symbol_index(self)`
- `_build_import_graph` (line 25) `def _build_import_graph(self)`
- `find_symbol` (line 36) `def find_symbol(self, name)`
- `explain` (line 49) `def explain(self, name)`
- `_find_incoming_imports` (line 77) `def _find_incoming_imports(self, target)`
- `find_path` (line 84) `def find_path(self, symbol_a, symbol_b)`
- `query` (line 113) `def query(self, question)`
- `summary` (line 162) `def summary(self)`

#### `_scanner.py`
**Path:** `readmenator/_scanner.py`

**Classes:**
- `PolyglotScanner` (line 11) `class PolyglotScanner`

**Functions:**
- `__init__` (line 12) `def __init__(self, config)`
- `_is_ignored` (line 15) `def _is_ignored(self, path)`
- `_validate_path_security` (line 18) `def _validate_path_security(self, path)`
- `_check_directory_depth` (line 30) `def _check_directory_depth(self, path, root)`
- `scan` (line 37) `def scan(self, root)`

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
- `TestOrchestrator` (line 310) `class TestOrchestrator` - *Test suite for the ReadMenator Orchestrator (SDD + TDD + BDD).*

**Functions:**
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

#### `test_config.py`
**Path:** `tests/test_config.py`

**Classes:**
- `TestConfigContract` (line 7) `class TestConfigContract`

**Functions:**
- `test_config_is_immutable` (line 8) `def test_config_is_immutable(self)`
- `test_config_defaults_are_sane` (line 13) `def test_config_defaults_are_sane(self)`
- `test_ignore_dirs_are_comprehensive` (line 25) `def test_ignore_dirs_are_comprehensive(self)`
- `test_plural_map_covers_all_symbol_types` (line 31) `def test_plural_map_covers_all_symbol_types(self)`
- `test_supported_extensions_no_duplicates` (line 42) `def test_supported_extensions_no_duplicates(self)`

#### `test_documentation.py`
**Path:** `tests/test_documentation.py`

**Classes:**
- `TestDocumentationGeneratorContract` (line 8) `class TestDocumentationGeneratorContract`

**Functions:**
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

#### `test_integration.py`
**Path:** `tests/test_integration.py`

**Classes:**
- `TestEndToEndContract` (line 9) `class TestEndToEndContract`

**Functions:**
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
- `TestMermaidRendererContract` (line 8) `class TestMermaidRendererContract`

**Functions:**
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
- `TestSymbolContract` (line 6) `class TestSymbolContract`
- `TestNodeContract` (line 20) `class TestNodeContract`
- `TestEdgeContract` (line 48) `class TestEdgeContract`
- `TestPluralizeContract` (line 56) `class TestPluralizeContract`

**Functions:**
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
- `TestCParserContract` (line 22) `class TestCParserContract`
- `TestPythonParserContract` (line 72) `class TestPythonParserContract`
- `TestGoParserContract` (line 141) `class TestGoParserContract`
- `TestRustParserContract` (line 184) `class TestRustParserContract`
- `TestJavaScriptParserContract` (line 222) `class TestJavaScriptParserContract`
- `TestJavaParserContract` (line 261) `class TestJavaParserContract`
- `TestCSharpParserContract` (line 293) `class TestCSharpParserContract`
- `TestShellParserContract` (line 326) `class TestShellParserContract`
- `TestPHPParserContract` (line 345) `class TestPHPParserContract`
- `TestDartParserContract` (line 371) `class TestDartParserContract`
- `TestGDScriptParserContract` (line 396) `class TestGDScriptParserContract`
- `TestNimParserContract` (line 414) `class TestNimParserContract`
- `TestAssemblyParserContract` (line 440) `class TestAssemblyParserContract`
- `TestParserFactoryContract` (line 460) `class TestParserFactoryContract`

**Functions:**
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

#### `test_query.py`
**Path:** `tests/test_query.py`

**Classes:**
- `TestQueryEngineContract` (line 22) `class TestQueryEngineContract`

**Functions:**
- `_make_node` (line 7) `def _make_node(node_id, symbols)`
- `_make_sym` (line 18) `def _make_sym(name, kind, line)`
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

#### `test_scanner.py`
**Path:** `tests/test_scanner.py`

**Classes:**
- `TestScannerContract` (line 10) `class TestScannerContract`

**Functions:**
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
