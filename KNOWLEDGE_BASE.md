# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 67 | **Total Symbols Extracted:** 717 | **Total Imports:** 371
 | **Resolved Imports:** 168


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [God Nodes](#god-nodes)
4. [Community Analysis](#community-analysis)
5. [Surprising Connections](#surprising-connections)
6. [Suggested Questions](#suggested-questions)
7. [Taint Propagation Map](#taint-propagation-map)
8. [Hotspot Analysis](#hotspot-analysis)
9. [Change Impact Analysis](#change-impact-analysis)
10. [Suggested Linting Rules](#suggested-linting-rules)
11. [Structural Knowledge Map](#structural-knowledge-map)
12. [Code Property Graph](#code-property-graph)
13. [Architecture Reference](#architecture-reference)
    - [PY (67 files)](#py-67-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 67 |
| Total Symbols | 717 |
| Total Imports | 371 |
| Call Edges | 3689 |
| Inheritance Edges | 68 |
| Languages | 1 |
| Avg Symbols/File | 10.7 |
| Avg Imports/File | 5.5 |
| Resolved Imports | 168 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `__init__.py` | 23 | 2 | py |
| `_pipeline.py` | 16 | 17 | py |
| `readmenator_orchestrator.py` | 14 | 34 | py |
| `_app.py` | 12 | 29 | py |
| `_exporter.py` | 10 | 14 | py |
| `__main__.py` | 9 | 3 | py |
| `test_scanner.py` | 9 | 17 | py |
| `_rule_gen.py` | 8 | 9 | py |
| `_scanner.py` | 8 | 13 | py |
| `test_cache.py` | 8 | 15 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 38 |
| testing | 23 |
| business_logic | 3 |
| infrastructure | 2 |
| data_access | 1 |

### utility

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `_analyzer.py` (py, 13 symbols)
- `_app.py` (py, 29 symbols)
- `_cpg.py` (py, 5 symbols)
- `_documentation.py` (py, 20 symbols)
- `_exporter.py` (py, 14 symbols)
- `_hotspots.py` (py, 7 symbols)
- `_layers.py` (py, 4 symbols)
- `_mermaid.py` (py, 4 symbols)
- `_pipeline.py` (py, 17 symbols)
- `_resolver.py` (py, 11 symbols)
- `_sarif.py` (py, 5 symbols)
- `_scanner.py` (py, 13 symbols)
- `_security.py` (py, 27 symbols)
- *... and 23 more*

### testing

- `__main__.py` (py, 3 symbols)
- `readmenator_orchestrator.py` (py, 34 symbols)
- `__init__.py` (py, 0 symbols)
- `test_analyzer.py` (py, 12 symbols)
- `test_cache.py` (py, 15 symbols)
- `test_config.py` (py, 6 symbols)
- `test_cpg.py` (py, 11 symbols)
- `test_documentation.py` (py, 24 symbols)
- `test_exporter.py` (py, 15 symbols)
- `test_hotspots.py` (py, 11 symbols)
- `test_integration.py` (py, 16 symbols)
- `test_layer_rules.py` (py, 13 symbols)
- `test_mermaid.py` (py, 11 symbols)
- `test_models.py` (py, 11 symbols)
- `test_parsers.py` (py, 84 symbols)
- *... and 8 more*

### infrastructure

- `_cache.py` (py, 8 symbols)
- `_config.py` (py, 1 symbols)

### business_logic

- `_layer_rules.py` (py, 4 symbols)
- `_models.py` (py, 15 symbols)
- `_rule_gen.py` (py, 9 symbols)

### data_access

- `_query.py` (py, 13 symbols)

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections |
|------|-------|-------------|
| `_models.py` | 103.5 | |
| `_config.py` | 66.1 | |
| `__init__.py` | 48.2 | |
| `_base.py` | 44.6 | |
| `_pipeline.py` | 31.7 | |
| `_app.py` | 24.9 | |
| `_documentation.py` | 14.0 | |
| `test_parsers.py` | 12.4 | |
| `test_security.py` | 12.3 | |
| `_scanner.py` | 11.3 | |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### readmenator (Cohesion: 0.99)

**63 files** in this community:

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `__main__.py` (py, 3 symbols)
- `_analyzer.py` (py, 13 symbols)
- `_app.py` (py, 29 symbols)
- `_cache.py` (py, 8 symbols)
- `_config.py` (py, 1 symbols)
- `_cpg.py` (py, 5 symbols)
- `_documentation.py` (py, 20 symbols)
- `_exporter.py` (py, 14 symbols)
- `_hotspots.py` (py, 7 symbols)
- `_layer_rules.py` (py, 4 symbols)
- `_layers.py` (py, 4 symbols)
- `_mermaid.py` (py, 4 symbols)
- `_models.py` (py, 15 symbols)
- `_pipeline.py` (py, 17 symbols)
- `_query.py` (py, 13 symbols)
- `_rule_gen.py` (py, 9 symbols)
- `_sarif.py` (py, 5 symbols)
- `_scanner.py` (py, 13 symbols)
- ... and 43 more files

### readmenator (Cohesion: 0.50)

**2 files** in this community:

- `_resolver.py` (py, 11 symbols)
- `test_resolver.py` (py, 11 symbols)

---

## Surprising Connections

Files in different communities connected through 3+ indirect hops.

- `_analyzer.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `_cpg.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `_documentation.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `_exporter.py` <-> `test_resolver.py` (4 hops, across 2 communities)
- `_hotspots.py` <-> `test_resolver.py` (4 hops, across 2 communities)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does _models.py depend on, and what depends on it? (51 connections)
- What does _config.py depend on, and what depends on it? (33 connections)
- What does __init__.py depend on, and what depends on it? (24 connections)
- How are the 63 files in 'readmenator' related to each other?
- Why are _analyzer.py and test_resolver.py connected through 4 hops across 2 communities?

---

## Taint Propagation Map

Taint analysis traces how dangerous imports propagate through the codebase via transitive dependencies. Source files import dangerous modules directly; sink files receive the danger indirectly.

**Taint Sources:** 1 | **Taint Sinks:** 1 | **Propagation Paths:** 1

- `readmenator_orchestrator.py` imports `subprocess` (0 hop to `readmenator_orchestrator.py`) [high]
  Path: readmenator_orchestrator.py

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `_models.py` | 0.179 | 1.000 | 0.671 | 15 | 56 |
| `__init__.py` | 0.024 | 0.839 | 0.513 | 2 | 47 |
| `test_parsers.py` | 1.000 | 0.107 | 0.464 | 84 | 6 |
| `test_security.py` | 0.750 | 0.196 | 0.418 | 63 | 11 |
| `_pipeline.py` | 0.202 | 0.554 | 0.413 | 17 | 31 |
| `_config.py` | 0.012 | 0.661 | 0.401 | 1 | 37 |
| `_app.py` | 0.345 | 0.411 | 0.385 | 29 | 23 |
| `_base.py` | 0.071 | 0.482 | 0.318 | 6 | 27 |
| `readmenator_orchestrator.py` | 0.405 | 0.250 | 0.312 | 34 | 14 |
| `_security.py` | 0.321 | 0.196 | 0.246 | 27 | 11 |
| `test_documentation.py` | 0.286 | 0.214 | 0.243 | 24 | 12 |
| `test_parsers_new.py` | 0.429 | 0.107 | 0.236 | 36 | 6 |
| `_documentation.py` | 0.238 | 0.232 | 0.234 | 20 | 13 |
| `_exporter.py` | 0.167 | 0.250 | 0.217 | 14 | 14 |
| `test_scanner.py` | 0.202 | 0.214 | 0.209 | 17 | 12 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `_config.py` | 33 | 20 | 53 |
| `_models.py` | 50 | 0 | 51 |
| `_base.py` | 20 | 10 | 30 |
| `_assembly.py` | 1 | 10 | 11 |
| `_c.py` | 1 | 10 | 11 |
| `_csharp.py` | 1 | 10 | 11 |
| `_dart.py` | 1 | 10 | 11 |
| `_elixir.py` | 1 | 10 | 11 |
| `_gdscript.py` | 1 | 10 | 11 |
| `_go.py` | 1 | 10 | 11 |
| `_java.py` | 1 | 10 | 11 |
| `_javascript.py` | 1 | 10 | 11 |
| `_kotlin.py` | 1 | 10 | 11 |
| `_lua.py` | 1 | 10 | 11 |
| `_nim.py` | 1 | 10 | 11 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 608 total | py | 608 |
| `RM002` | info | Print statement found (consider logging instead) | python | 6 |

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_0 ["readmenator"]
    readmenator_parsers___init___py["__init__.py (py)"]
    class readmenator_parsers___init___py mod;
    readmenator_parsers___init___py__init_parser_map["_init_parser_map"]
    class readmenator_parsers___init___py__init_parser_map fn;
    readmenator_parsers___init___py --> readmenator_parsers___init___py__init_parser_map
    readmenator_parsers___init___py_create_parser["create_parser"]
    class readmenator_parsers___init___py_create_parser fn;
    readmenator_parsers___init___py --> readmenator_parsers___init___py_create_parser
    readmenator__pipeline_py["_pipeline.py (py)"]
    class readmenator__pipeline_py mod;
    readmenator__pipeline_py_AnalyzerFactory["AnalyzerFactory"]
    class readmenator__pipeline_py_AnalyzerFactory cls;
    readmenator__pipeline_py --> readmenator__pipeline_py_AnalyzerFactory
    readmenator__pipeline_py_DeepAnalysisRunner["DeepAnalysisRunner"]
    class readmenator__pipeline_py_DeepAnalysisRunner cls;
    readmenator__pipeline_py --> readmenator__pipeline_py_DeepAnalysisRunner
    readmenator__pipeline_py___init__["__init__"]
    class readmenator__pipeline_py___init__ fn;
    readmenator__pipeline_py --> readmenator__pipeline_py___init__
    readmenator__pipeline_py_scanner["scanner"]
    class readmenator__pipeline_py_scanner fn;
    readmenator__pipeline_py --> readmenator__pipeline_py_scanner
    readmenator__pipeline_py_generator["generator"]
    class readmenator__pipeline_py_generator fn;
    readmenator__pipeline_py --> readmenator__pipeline_py_generator
    readmenator__app_py["_app.py (py)"]
    class readmenator__app_py mod;
    readmenator_orchestrator_py["readmenator_orchestrator.py (py)"]
    class readmenator_orchestrator_py mod;
    tests_test_documentation_py["test_documentation.py (py)"]
    class tests_test_documentation_py mod;
    tests_test_scanner_py["test_scanner.py (py)"]
    class tests_test_scanner_py mod;
    readmenator__exporter_py["_exporter.py (py)"]
    class readmenator__exporter_py mod;
    readmenator___main___py["__main__.py (py)"]
    class readmenator___main___py mod;
    tests_test_security_py["test_security.py (py)"]
    class tests_test_security_py mod;
    readmenator__documentation_py["_documentation.py (py)"]
    class readmenator__documentation_py mod;
    readmenator__scanner_py["_scanner.py (py)"]
    class readmenator__scanner_py mod;
    tests_test_cache_py["test_cache.py (py)"]
    class tests_test_cache_py mod;
    tests_test_rule_gen_py["test_rule_gen.py (py)"]
    class tests_test_rule_gen_py mod;
    readmenator__rule_gen_py["_rule_gen.py (py)"]
    class readmenator__rule_gen_py mod;
    readmenator__security_py["_security.py (py)"]
    class readmenator__security_py mod;
    tests_test_exporter_py["test_exporter.py (py)"]
    class tests_test_exporter_py mod;
    tests_test_cpg_py["test_cpg.py (py)"]
    class tests_test_cpg_py mod;
    tests_test_sarif_py["test_sarif.py (py)"]
    class tests_test_sarif_py mod;
    tests_test_integration_py["test_integration.py (py)"]
    class tests_test_integration_py mod;
    readmenator__analyzer_py["_analyzer.py (py)"]
    class readmenator__analyzer_py mod;
    tests_test_layer_rules_py["test_layer_rules.py (py)"]
    class tests_test_layer_rules_py mod;
    tests_test_analyzer_py["test_analyzer.py (py)"]
    class tests_test_analyzer_py mod;
    tests_test_hotspots_py["test_hotspots.py (py)"]
    class tests_test_hotspots_py mod;
    tests_test_taint_py["test_taint.py (py)"]
    class tests_test_taint_py mod;
    readmenator__cache_py["_cache.py (py)"]
    class readmenator__cache_py mod;
    readmenator__watcher_py["_watcher.py (py)"]
    class readmenator__watcher_py mod;
    readmenator__hotspots_py["_hotspots.py (py)"]
    class readmenator__hotspots_py mod;
    readmenator__taint_py["_taint.py (py)"]
    class readmenator__taint_py mod;
    readmenator_parsers__base_py["_base.py (py)"]
    class readmenator_parsers__base_py mod;
    readmenator_parsers__python_py["_python.py (py)"]
    class readmenator_parsers__python_py mod;
    tests_test_parsers_py["test_parsers.py (py)"]
    class tests_test_parsers_py mod;
    tests_test_parsers_new_py["test_parsers_new.py (py)"]
    class tests_test_parsers_new_py mod;
    readmenator__cpg_py["_cpg.py (py)"]
    class readmenator__cpg_py mod;
    readmenator__layer_rules_py["_layer_rules.py (py)"]
    class readmenator__layer_rules_py mod;
    readmenator_parsers__assembly_py["_assembly.py (py)"]
    class readmenator_parsers__assembly_py mod;
    readmenator_parsers__c_py["_c.py (py)"]
    class readmenator_parsers__c_py mod;
    readmenator_parsers__csharp_py["_csharp.py (py)"]
    class readmenator_parsers__csharp_py mod;
    readmenator_parsers__dart_py["_dart.py (py)"]
    class readmenator_parsers__dart_py mod;
    readmenator_parsers__elixir_py["_elixir.py (py)"]
    class readmenator_parsers__elixir_py mod;
    readmenator_parsers__gdscript_py["_gdscript.py (py)"]
    class readmenator_parsers__gdscript_py mod;
    readmenator_parsers__go_py["_go.py (py)"]
    class readmenator_parsers__go_py mod;
    readmenator_parsers__java_py["_java.py (py)"]
    class readmenator_parsers__java_py mod;
    readmenator_parsers__javascript_py["_javascript.py (py)"]
    class readmenator_parsers__javascript_py mod;
    readmenator_parsers__kotlin_py["_kotlin.py (py)"]
    class readmenator_parsers__kotlin_py mod;
    readmenator_parsers__lua_py["_lua.py (py)"]
    class readmenator_parsers__lua_py mod;
    readmenator_parsers__nim_py["_nim.py (py)"]
    class readmenator_parsers__nim_py mod;
    readmenator_parsers__php_py["_php.py (py)"]
    class readmenator_parsers__php_py mod;
    readmenator_parsers__ruby_py["_ruby.py (py)"]
    class readmenator_parsers__ruby_py mod;
    readmenator_parsers__rust_py["_rust.py (py)"]
    class readmenator_parsers__rust_py mod;
    readmenator_parsers__scala_py["_scala.py (py)"]
    class readmenator_parsers__scala_py mod;
    readmenator_parsers__shell_py["_shell.py (py)"]
    class readmenator_parsers__shell_py mod;
    readmenator_parsers__swift_py["_swift.py (py)"]
    class readmenator_parsers__swift_py mod;
    readmenator___init___py["__init__.py (py)"]
    class readmenator___init___py mod;
    tests_test_query_py["test_query.py (py)"]
    class tests_test_query_py mod;
    readmenator__query_py["_query.py (py)"]
    class readmenator__query_py mod;
    tests_test_mermaid_py["test_mermaid.py (py)"]
    class tests_test_mermaid_py mod;
    readmenator__sarif_py["_sarif.py (py)"]
    class readmenator__sarif_py mod;
    readmenator__mermaid_py["_mermaid.py (py)"]
    class readmenator__mermaid_py mod;
    end
    subgraph community_1 ["readmenator"]
    readmenator__resolver_py["_resolver.py (py)"]
    class readmenator__resolver_py mod;
    tests_test_resolver_py["test_resolver.py (py)"]
    class tests_test_resolver_py mod;
    tests_test_config_py["test_config.py (py)"]
    class tests_test_config_py mod;
    readmenator__layers_py["_layers.py (py)"]
    class readmenator__layers_py mod;
    readmenator_py["readmenator.py (py)"]
    class readmenator_py mod;
    readmenator__models_py["_models.py (py)"]
    class readmenator__models_py mod;
    tests_test_models_py["test_models.py (py)"]
    class tests_test_models_py mod;
    readmenator__config_py["_config.py (py)"]
    class readmenator__config_py mod;
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
    end
    readmenator___init___py -- resolved_imports --> readmenator__app_py
    readmenator___init___py -- resolved_imports --> readmenator__config_py
    readmenator___init___py -- resolved_imports --> readmenator__models_py
    readmenator___main___py -- resolved_imports --> readmenator__app_py
    readmenator___main___py -- resolved_imports --> readmenator__config_py
    readmenator___main___py -- resolved_imports --> readmenator__config_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__config_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__cache_py
    readmenator__app_py -- resolved_imports --> readmenator__config_py
    readmenator__app_py -- resolved_imports --> readmenator__layers_py
    readmenator__app_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__pipeline_py
    readmenator__app_py -- resolved_imports --> readmenator__query_py
    readmenator__app_py -- resolved_imports --> readmenator__resolver_py
    readmenator__app_py -- resolved_imports --> readmenator__watcher_py
    readmenator__cache_py -- resolved_imports --> readmenator__config_py
    readmenator__cpg_py -- resolved_imports --> readmenator__models_py
    readmenator__documentation_py -- resolved_imports --> readmenator__config_py
    readmenator__documentation_py -- resolved_imports --> readmenator__cpg_py
    readmenator__documentation_py -- resolved_imports --> readmenator__mermaid_py
    readmenator__documentation_py -- resolved_imports --> readmenator__models_py
    readmenator__exporter_py -- resolved_imports --> readmenator__config_py
    readmenator__exporter_py -- resolved_imports --> readmenator__models_py
    readmenator__hotspots_py -- resolved_imports --> readmenator__config_py
    readmenator__hotspots_py -- resolved_imports --> readmenator__models_py
    readmenator__layer_rules_py -- resolved_imports --> readmenator__config_py
    readmenator__layer_rules_py -- resolved_imports --> readmenator__models_py
    readmenator__layers_py -- resolved_imports --> readmenator__models_py
    readmenator__mermaid_py -- resolved_imports --> readmenator__models_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__analyzer_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__config_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__cpg_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__documentation_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__exporter_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__hotspots_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__layer_rules_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__layers_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__models_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__rule_gen_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__sarif_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__scanner_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__security_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__taint_py
    readmenator__query_py -- resolved_imports --> readmenator__models_py
    readmenator__rule_gen_py -- resolved_imports --> readmenator__config_py
    readmenator__rule_gen_py -- resolved_imports --> readmenator__models_py
    readmenator__sarif_py -- resolved_imports --> readmenator__models_py
    readmenator__scanner_py -- resolved_imports --> readmenator__config_py
    readmenator__scanner_py -- resolved_imports --> readmenator__models_py
    readmenator__scanner_py -- resolved_imports --> readmenator_parsers___init___py
    readmenator__security_py -- resolved_imports --> readmenator__config_py
    readmenator__security_py -- resolved_imports --> readmenator__models_py
    readmenator__taint_py -- resolved_imports --> readmenator__config_py
    readmenator__taint_py -- resolved_imports --> readmenator__models_py
    readmenator__watcher_py -- resolved_imports --> readmenator__config_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator__config_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__c_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__python_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__go_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__rust_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__javascript_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__java_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__csharp_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__shell_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__php_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__dart_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__gdscript_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__nim_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__assembly_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__ruby_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__swift_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__kotlin_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__scala_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__lua_py
    readmenator_parsers___init___py -- resolved_imports --> readmenator_parsers__elixir_py
    readmenator_parsers__assembly_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__assembly_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__base_py -- resolved_imports --> readmenator__config_py
    readmenator_parsers__base_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__c_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__c_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__csharp_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__csharp_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__dart_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__dart_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__elixir_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__elixir_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__gdscript_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__gdscript_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__go_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__go_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__java_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__java_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__javascript_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__javascript_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__kotlin_py -- resolved_imports --> readmenator_parsers__base_py
    readmenator_parsers__kotlin_py -- resolved_imports --> readmenator__models_py
    readmenator_parsers__lua_py -- resolved_imports --> readmenator_parsers__base_py
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
    ext_logging["logging"]
    class ext_logging ext;
    readmenator___main___py -.->|imports| ext_logging
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
    readmenator___main___py -.->|imports| ext_readmenator__config
    readmenator___main___py -.->|imports| ext_readmenator__config
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
    readmenator__app_py -.->|imports| ext___future__
    readmenator__app_py -.->|imports| ext_logging
    readmenator__app_py -.->|imports| ext_pathlib
    readmenator__app_py -.->|imports| ext_typing
    ext_readmenator__cache["readmenator._cache"]
    class ext_readmenator__cache ext;
    readmenator__app_py -.->|imports| ext_readmenator__cache
    readmenator__app_py -.->|imports| ext_readmenator__config
    ext_readmenator__layers["readmenator._layers"]
    class ext_readmenator__layers ext;
    readmenator__app_py -.->|imports| ext_readmenator__layers
    readmenator__app_py -.->|imports| ext_readmenator__models
    ext_readmenator__pipeline["readmenator._pipeline"]
    class ext_readmenator__pipeline ext;
    readmenator__app_py -.->|imports| ext_readmenator__pipeline
    ext_readmenator__query["readmenator._query"]
    class ext_readmenator__query ext;
    readmenator__app_py -.->|imports| ext_readmenator__query
    ext_readmenator__resolver["readmenator._resolver"]
    class ext_readmenator__resolver ext;
    readmenator__app_py -.->|imports| ext_readmenator__resolver
    ext_readmenator__watcher["readmenator._watcher"]
    class ext_readmenator__watcher ext;
    readmenator__app_py -.->|imports| ext_readmenator__watcher
    readmenator__cache_py -.->|imports| ext___future__
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    readmenator__cache_py -.->|imports| ext_hashlib
    ext_json["json"]
    class ext_json ext;
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
    readmenator__cpg_py -.->|imports| ext___future__
    readmenator__cpg_py -.->|imports| ext_hashlib
    readmenator__cpg_py -.->|imports| ext_json
    readmenator__cpg_py -.->|imports| ext_typing
    readmenator__cpg_py -.->|imports| ext_readmenator__models
    readmenator__documentation_py -.->|imports| ext___future__
    readmenator__documentation_py -.->|imports| ext_collections
    readmenator__documentation_py -.->|imports| ext_typing
    readmenator__documentation_py -.->|imports| ext_readmenator__config
    ext_readmenator__cpg["readmenator._cpg"]
    class ext_readmenator__cpg ext;
    readmenator__documentation_py -.->|imports| ext_readmenator__cpg
    ext_readmenator__mermaid["readmenator._mermaid"]
    class ext_readmenator__mermaid ext;
    readmenator__documentation_py -.->|imports| ext_readmenator__mermaid
    readmenator__documentation_py -.->|imports| ext_readmenator__models
    readmenator__exporter_py -.->|imports| ext___future__
    readmenator__exporter_py -.->|imports| ext_json
    ext_math["math"]
    class ext_math ext;
    readmenator__exporter_py -.->|imports| ext_math
    readmenator__exporter_py -.->|imports| ext_os
    readmenator__exporter_py -.->|imports| ext_pathlib
    ext_textwrap["textwrap"]
    class ext_textwrap ext;
    readmenator__exporter_py -.->|imports| ext_textwrap
    readmenator__exporter_py -.->|imports| ext_typing
    readmenator__exporter_py -.->|imports| ext_readmenator__config
    readmenator__exporter_py -.->|imports| ext_readmenator__models
    readmenator__exporter_py -.->|imports| ext_os
    readmenator__hotspots_py -.->|imports| ext___future__
    readmenator__hotspots_py -.->|imports| ext_collections
    readmenator__hotspots_py -.->|imports| ext_typing
    readmenator__hotspots_py -.->|imports| ext_readmenator__config
    readmenator__hotspots_py -.->|imports| ext_readmenator__models
    readmenator__layer_rules_py -.->|imports| ext___future__
    readmenator__layer_rules_py -.->|imports| ext_typing
    readmenator__layer_rules_py -.->|imports| ext_readmenator__config
    readmenator__layer_rules_py -.->|imports| ext_readmenator__models
    readmenator__layers_py -.->|imports| ext___future__
    readmenator__layers_py -.->|imports| ext_typing
    readmenator__layers_py -.->|imports| ext_readmenator__models
    readmenator__mermaid_py -.->|imports| ext___future__
    ext_re["re"]
    class ext_re ext;
    readmenator__mermaid_py -.->|imports| ext_re
    readmenator__mermaid_py -.->|imports| ext_typing
    readmenator__mermaid_py -.->|imports| ext_readmenator__models
    readmenator__models_py -.->|imports| ext___future__
    readmenator__models_py -.->|imports| ext_dataclasses
    readmenator__models_py -.->|imports| ext_typing
    readmenator__pipeline_py -.->|imports| ext___future__
    readmenator__pipeline_py -.->|imports| ext_typing
    ext_readmenator__analyzer["readmenator._analyzer"]
    class ext_readmenator__analyzer ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__analyzer
    readmenator__pipeline_py -.->|imports| ext_readmenator__config
    readmenator__pipeline_py -.->|imports| ext_readmenator__cpg
    ext_readmenator__documentation["readmenator._documentation"]
    class ext_readmenator__documentation ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__documentation
    ext_readmenator__exporter["readmenator._exporter"]
    class ext_readmenator__exporter ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__exporter
    ext_readmenator__hotspots["readmenator._hotspots"]
    class ext_readmenator__hotspots ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__hotspots
    ext_readmenator__layer_rules["readmenator._layer_rules"]
    class ext_readmenator__layer_rules ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__layer_rules
    readmenator__pipeline_py -.->|imports| ext_readmenator__layers
    readmenator__pipeline_py -.->|imports| ext_readmenator__models
    ext_readmenator__rule_gen["readmenator._rule_gen"]
    class ext_readmenator__rule_gen ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__rule_gen
    ext_readmenator__sarif["readmenator._sarif"]
    class ext_readmenator__sarif ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__sarif
    ext_readmenator__scanner["readmenator._scanner"]
    class ext_readmenator__scanner ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__scanner
    ext_readmenator__security["readmenator._security"]
    class ext_readmenator__security ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__security
    ext_readmenator__taint["readmenator._taint"]
    class ext_readmenator__taint ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__taint
    readmenator__query_py -.->|imports| ext___future__
    readmenator__query_py -.->|imports| ext_collections
    readmenator__query_py -.->|imports| ext_typing
    readmenator__query_py -.->|imports| ext_readmenator__models
    readmenator__resolver_py -.->|imports| ext___future__
    readmenator__resolver_py -.->|imports| ext_re
    readmenator__resolver_py -.->|imports| ext_pathlib
    readmenator__resolver_py -.->|imports| ext_typing
    readmenator__rule_gen_py -.->|imports| ext___future__
    readmenator__rule_gen_py -.->|imports| ext_os
    readmenator__rule_gen_py -.->|imports| ext_collections
    readmenator__rule_gen_py -.->|imports| ext_pathlib
    readmenator__rule_gen_py -.->|imports| ext_typing
    readmenator__rule_gen_py -.->|imports| ext_readmenator__config
    readmenator__rule_gen_py -.->|imports| ext_readmenator__models
    readmenator__rule_gen_py -.->|imports| ext_re
    readmenator__sarif_py -.->|imports| ext___future__
    readmenator__sarif_py -.->|imports| ext_json
    readmenator__sarif_py -.->|imports| ext_typing
    readmenator__sarif_py -.->|imports| ext_readmenator__models
    readmenator__scanner_py -.->|imports| ext___future__
    readmenator__scanner_py -.->|imports| ext_logging
    readmenator__scanner_py -.->|imports| ext_re
    readmenator__scanner_py -.->|imports| ext_pathlib
    readmenator__scanner_py -.->|imports| ext_typing
    readmenator__scanner_py -.->|imports| ext_readmenator__config
    readmenator__scanner_py -.->|imports| ext_readmenator__models
    ext_readmenator_parsers["readmenator.parsers"]
    class ext_readmenator_parsers ext;
    readmenator__scanner_py -.->|imports| ext_readmenator_parsers
    readmenator__security_py -.->|imports| ext___future__
    readmenator__security_py -.->|imports| ext_re
    readmenator__security_py -.->|imports| ext_dataclasses
    readmenator__security_py -.->|imports| ext_pathlib
    readmenator__security_py -.->|imports| ext_typing
    readmenator__security_py -.->|imports| ext_readmenator__config
    readmenator__security_py -.->|imports| ext_readmenator__models
    readmenator__taint_py -.->|imports| ext___future__
    readmenator__taint_py -.->|imports| ext_collections
    readmenator__taint_py -.->|imports| ext_typing
    readmenator__taint_py -.->|imports| ext_readmenator__config
    readmenator__taint_py -.->|imports| ext_readmenator__models
    readmenator__watcher_py -.->|imports| ext___future__
    readmenator__watcher_py -.->|imports| ext_hashlib
    readmenator__watcher_py -.->|imports| ext_logging
    ext_time["time"]
    class ext_time ext;
    readmenator__watcher_py -.->|imports| ext_time
    readmenator__watcher_py -.->|imports| ext_pathlib
    readmenator__watcher_py -.->|imports| ext_typing
    readmenator__watcher_py -.->|imports| ext_readmenator__config
    readmenator_parsers___init___py -.->|imports| ext___future__
    readmenator_parsers___init___py -.->|imports| ext_typing
    readmenator_parsers___init___py -.->|imports| ext_readmenator__config
    ext_readmenator_parsers__base["readmenator.parsers._base"]
    class ext_readmenator_parsers__base ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__base
    ext_readmenator_parsers__c["readmenator.parsers._c"]
    class ext_readmenator_parsers__c ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__c
    ext_readmenator_parsers__python["readmenator.parsers._python"]
    class ext_readmenator_parsers__python ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__python
    ext_readmenator_parsers__go["readmenator.parsers._go"]
    class ext_readmenator_parsers__go ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__go
    ext_readmenator_parsers__rust["readmenator.parsers._rust"]
    class ext_readmenator_parsers__rust ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__rust
    ext_readmenator_parsers__javascript["readmenator.parsers._javascript"]
    class ext_readmenator_parsers__javascript ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__javascript
    ext_readmenator_parsers__java["readmenator.parsers._java"]
    class ext_readmenator_parsers__java ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__java
    ext_readmenator_parsers__csharp["readmenator.parsers._csharp"]
    class ext_readmenator_parsers__csharp ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__csharp
    ext_readmenator_parsers__shell["readmenator.parsers._shell"]
    class ext_readmenator_parsers__shell ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__shell
    ext_readmenator_parsers__php["readmenator.parsers._php"]
    class ext_readmenator_parsers__php ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__php
    ext_readmenator_parsers__dart["readmenator.parsers._dart"]
    class ext_readmenator_parsers__dart ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__dart
    ext_readmenator_parsers__gdscript["readmenator.parsers._gdscript"]
    class ext_readmenator_parsers__gdscript ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__gdscript
    ext_readmenator_parsers__nim["readmenator.parsers._nim"]
    class ext_readmenator_parsers__nim ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__nim
    ext_readmenator_parsers__assembly["readmenator.parsers._assembly"]
    class ext_readmenator_parsers__assembly ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__assembly
    ext_readmenator_parsers__ruby["readmenator.parsers._ruby"]
    class ext_readmenator_parsers__ruby ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__ruby
    ext_readmenator_parsers__swift["readmenator.parsers._swift"]
    class ext_readmenator_parsers__swift ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__swift
    ext_readmenator_parsers__kotlin["readmenator.parsers._kotlin"]
    class ext_readmenator_parsers__kotlin ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__kotlin
    ext_readmenator_parsers__scala["readmenator.parsers._scala"]
    class ext_readmenator_parsers__scala ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__scala
    ext_readmenator_parsers__lua["readmenator.parsers._lua"]
    class ext_readmenator_parsers__lua ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__lua
    ext_readmenator_parsers__elixir["readmenator.parsers._elixir"]
    class ext_readmenator_parsers__elixir ext;
    readmenator_parsers___init___py -.->|imports| ext_readmenator_parsers__elixir
    readmenator_parsers__assembly_py -.->|imports| ext___future__
    readmenator_parsers__assembly_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__assembly_py -.->|imports| ext_readmenator__models
    readmenator_parsers__assembly_py -.->|imports| ext_re
    readmenator_parsers__base_py -.->|imports| ext___future__
    readmenator_parsers__base_py -.->|imports| ext_re
    readmenator_parsers__base_py -.->|imports| ext_typing
    readmenator_parsers__base_py -.->|imports| ext_readmenator__config
    readmenator_parsers__base_py -.->|imports| ext_readmenator__models
    readmenator_parsers__c_py -.->|imports| ext___future__
    readmenator_parsers__c_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__c_py -.->|imports| ext_readmenator__models
    readmenator_parsers__c_py -.->|imports| ext_re
    readmenator_parsers__csharp_py -.->|imports| ext___future__
    readmenator_parsers__csharp_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__csharp_py -.->|imports| ext_readmenator__models
    readmenator_parsers__csharp_py -.->|imports| ext_re
    readmenator_parsers__dart_py -.->|imports| ext___future__
    readmenator_parsers__dart_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__dart_py -.->|imports| ext_readmenator__models
    readmenator_parsers__dart_py -.->|imports| ext_re
    readmenator_parsers__elixir_py -.->|imports| ext___future__
    readmenator_parsers__elixir_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__elixir_py -.->|imports| ext_readmenator__models
    readmenator_parsers__elixir_py -.->|imports| ext_re
    readmenator_parsers__gdscript_py -.->|imports| ext___future__
    readmenator_parsers__gdscript_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__gdscript_py -.->|imports| ext_readmenator__models
    readmenator_parsers__gdscript_py -.->|imports| ext_re
    readmenator_parsers__go_py -.->|imports| ext___future__
    readmenator_parsers__go_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__go_py -.->|imports| ext_readmenator__models
    readmenator_parsers__go_py -.->|imports| ext_re
    readmenator_parsers__java_py -.->|imports| ext___future__
    readmenator_parsers__java_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__java_py -.->|imports| ext_readmenator__models
    readmenator_parsers__java_py -.->|imports| ext_re
    readmenator_parsers__javascript_py -.->|imports| ext___future__
    readmenator_parsers__javascript_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__javascript_py -.->|imports| ext_readmenator__models
    readmenator_parsers__javascript_py -.->|imports| ext_re
    readmenator_parsers__kotlin_py -.->|imports| ext___future__
    readmenator_parsers__kotlin_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__kotlin_py -.->|imports| ext_readmenator__models
    readmenator_parsers__kotlin_py -.->|imports| ext_re
    readmenator_parsers__lua_py -.->|imports| ext___future__
    readmenator_parsers__lua_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__lua_py -.->|imports| ext_readmenator__models
    readmenator_parsers__lua_py -.->|imports| ext_re
    readmenator_parsers__nim_py -.->|imports| ext___future__
    readmenator_parsers__nim_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__nim_py -.->|imports| ext_readmenator__models
    readmenator_parsers__nim_py -.->|imports| ext_re
    readmenator_parsers__php_py -.->|imports| ext___future__
    readmenator_parsers__php_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__php_py -.->|imports| ext_readmenator__models
    readmenator_parsers__php_py -.->|imports| ext_re
    readmenator_parsers__python_py -.->|imports| ext___future__
    ext_ast["ast"]
    class ext_ast ext;
    readmenator_parsers__python_py -.->|imports| ext_ast
    ext_warnings["warnings"]
    class ext_warnings ext;
    readmenator_parsers__python_py -.->|imports| ext_warnings
    readmenator_parsers__python_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__python_py -.->|imports| ext_readmenator__models
    readmenator_parsers__ruby_py -.->|imports| ext___future__
    readmenator_parsers__ruby_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__ruby_py -.->|imports| ext_readmenator__models
    readmenator_parsers__ruby_py -.->|imports| ext_re
    readmenator_parsers__rust_py -.->|imports| ext___future__
    readmenator_parsers__rust_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__rust_py -.->|imports| ext_readmenator__models
    readmenator_parsers__rust_py -.->|imports| ext_re
    readmenator_parsers__scala_py -.->|imports| ext___future__
    readmenator_parsers__scala_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__scala_py -.->|imports| ext_readmenator__models
    readmenator_parsers__scala_py -.->|imports| ext_re
    readmenator_parsers__shell_py -.->|imports| ext___future__
    readmenator_parsers__shell_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__shell_py -.->|imports| ext_readmenator__models
    readmenator_parsers__shell_py -.->|imports| ext_re
    readmenator_parsers__swift_py -.->|imports| ext___future__
    readmenator_parsers__swift_py -.->|imports| ext_readmenator_parsers__base
    readmenator_parsers__swift_py -.->|imports| ext_readmenator__models
    readmenator_parsers__swift_py -.->|imports| ext_re
    readmenator_py -.->|imports| ext_sys
    readmenator_py -.->|imports| ext_pathlib
    ext_readmenator___main__["readmenator.__main__"]
    class ext_readmenator___main__ ext;
    readmenator_py -.->|imports| ext_readmenator___main__
    readmenator_orchestrator_py -.->|imports| ext_argparse
    readmenator_orchestrator_py -.->|imports| ext_logging
    readmenator_orchestrator_py -.->|imports| ext_os
    readmenator_orchestrator_py -.->|imports| ext_re
    ext_shlex["shlex"]
    class ext_shlex ext;
    readmenator_orchestrator_py -.->|imports| ext_shlex
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
    tests_test_cpg_py -.->|imports| ext___future__
    tests_test_cpg_py -.->|imports| ext_json
    tests_test_cpg_py -.->|imports| ext_unittest
    tests_test_cpg_py -.->|imports| ext_readmenator__config
    tests_test_cpg_py -.->|imports| ext_readmenator__cpg
    tests_test_cpg_py -.->|imports| ext_readmenator__models
    tests_test_documentation_py -.->|imports| ext___future__
    tests_test_documentation_py -.->|imports| ext_unittest
    tests_test_documentation_py -.->|imports| ext_readmenator__config
    tests_test_documentation_py -.->|imports| ext_readmenator__documentation
    tests_test_documentation_py -.->|imports| ext_readmenator__models
    tests_test_documentation_py -.->|imports| ext_readmenator__models
    tests_test_documentation_py -.->|imports| ext_readmenator__models
    tests_test_exporter_py -.->|imports| ext___future__
    tests_test_exporter_py -.->|imports| ext_json
    tests_test_exporter_py -.->|imports| ext_unittest
    tests_test_exporter_py -.->|imports| ext_readmenator__config
    tests_test_exporter_py -.->|imports| ext_readmenator__exporter
    tests_test_exporter_py -.->|imports| ext_readmenator__models
    tests_test_hotspots_py -.->|imports| ext___future__
    tests_test_hotspots_py -.->|imports| ext_unittest
    tests_test_hotspots_py -.->|imports| ext_readmenator__config
    tests_test_hotspots_py -.->|imports| ext_readmenator__hotspots
    tests_test_hotspots_py -.->|imports| ext_readmenator__models
    tests_test_integration_py -.->|imports| ext_tempfile
    tests_test_integration_py -.->|imports| ext_unittest
    tests_test_integration_py -.->|imports| ext_pathlib
    tests_test_integration_py -.->|imports| ext_readmenator__app
    tests_test_integration_py -.->|imports| ext_readmenator__config
    tests_test_integration_py -.->|imports| ext_shutil
    tests_test_layer_rules_py -.->|imports| ext___future__
    tests_test_layer_rules_py -.->|imports| ext_unittest
    tests_test_layer_rules_py -.->|imports| ext_readmenator__config
    tests_test_layer_rules_py -.->|imports| ext_readmenator__layer_rules
    tests_test_layer_rules_py -.->|imports| ext_readmenator__models
    tests_test_mermaid_py -.->|imports| ext_unittest
    tests_test_mermaid_py -.->|imports| ext_readmenator__mermaid
    tests_test_mermaid_py -.->|imports| ext_readmenator__models
    tests_test_models_py -.->|imports| ext_unittest
    tests_test_models_py -.->|imports| ext_readmenator__models
    tests_test_parsers_py -.->|imports| ext_unittest
    tests_test_parsers_py -.->|imports| ext_readmenator__config
    tests_test_parsers_py -.->|imports| ext_readmenator_parsers
    tests_test_parsers_py -.->|imports| ext_warnings
    tests_test_parsers_new_py -.->|imports| ext___future__
    tests_test_parsers_new_py -.->|imports| ext_unittest
    tests_test_parsers_new_py -.->|imports| ext_readmenator__config
    tests_test_parsers_new_py -.->|imports| ext_readmenator_parsers
    tests_test_query_py -.->|imports| ext_unittest
    tests_test_query_py -.->|imports| ext_readmenator__models
    tests_test_query_py -.->|imports| ext_readmenator__query
    tests_test_resolver_py -.->|imports| ext___future__
    tests_test_resolver_py -.->|imports| ext_unittest
    tests_test_resolver_py -.->|imports| ext_readmenator__resolver
    tests_test_rule_gen_py -.->|imports| ext___future__
    tests_test_rule_gen_py -.->|imports| ext_tempfile
    tests_test_rule_gen_py -.->|imports| ext_unittest
    tests_test_rule_gen_py -.->|imports| ext_pathlib
    tests_test_rule_gen_py -.->|imports| ext_readmenator__config
    tests_test_rule_gen_py -.->|imports| ext_readmenator__models
    tests_test_rule_gen_py -.->|imports| ext_readmenator__rule_gen
    tests_test_sarif_py -.->|imports| ext___future__
    tests_test_sarif_py -.->|imports| ext_json
    tests_test_sarif_py -.->|imports| ext_unittest
    tests_test_sarif_py -.->|imports| ext_readmenator__config
    tests_test_sarif_py -.->|imports| ext_readmenator__models
    tests_test_sarif_py -.->|imports| ext_readmenator__sarif
    tests_test_scanner_py -.->|imports| ext_os
    tests_test_scanner_py -.->|imports| ext_tempfile
    tests_test_scanner_py -.->|imports| ext_unittest
    tests_test_scanner_py -.->|imports| ext_pathlib
    tests_test_scanner_py -.->|imports| ext_readmenator__config
    tests_test_scanner_py -.->|imports| ext_readmenator__models
    tests_test_scanner_py -.->|imports| ext_readmenator__scanner
    tests_test_scanner_py -.->|imports| ext_shutil
    tests_test_scanner_py -.->|imports| ext_re
    tests_test_security_py -.->|imports| ext___future__
    tests_test_security_py -.->|imports| ext_os
    tests_test_security_py -.->|imports| ext_tempfile
    tests_test_security_py -.->|imports| ext_unittest
    tests_test_security_py -.->|imports| ext_pathlib
    tests_test_security_py -.->|imports| ext_readmenator__config
    tests_test_security_py -.->|imports| ext_readmenator__models
    tests_test_security_py -.->|imports| ext_readmenator__security
    tests_test_taint_py -.->|imports| ext___future__
    tests_test_taint_py -.->|imports| ext_unittest
    tests_test_taint_py -.->|imports| ext_readmenator__config
    tests_test_taint_py -.->|imports| ext_readmenator__models
    tests_test_taint_py -.->|imports| ext_readmenator__taint
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://readmenator.dev/cpg/v1", "analysis": {"communities": [{"cohesion": 0.994, "id": 0, "label": "readmenator", "size": 63}, {"cohesion": 0.5, "id": 1, "label": "readmenator", "size": 2}], "god_nodes": [{"node_id": "readmenator/_models.py", "score": 103.5}, {"node_id": "readmenator/_config.py", "score": 66.1}, {"node_id": "readmenator/parsers/__init__.py", "score": 48.2}, {"node_id": "readmenator/parsers/_base.py", "score": 44.6}, {"node_id": "readmenator/_pipeline.py", "score": 31.7}, {"node_id": "readmenator/_app.py", "score": 24.9}, {"node_id": "readmenator/_documentation.py", "score": 14.0}, {"node_id": "tests/test_parsers.py", "score": 12.4}, {"node_id": "tests/test_security.py", "score": 12.3}, {"node_id": "readmenator/_scanner.py", "score": 11.3}], "surprising_connections": [{"hops": 4, "source": "readmenator/_analyzer.py", "target": "tests/test_resolver.py"}, {"hops": 4, "source": "readmenator/_cpg.py", "target": "tests/test_resolver.py"}, {"hops": 4, "source": "readmenator/_documentation.py", "target": "tests/test_resolver.py"}, {"hops": 4, "source": "readmenator/_exporter.py", "target": "tests/test_resolver.py"}, {"hops": 4, "source": "readmenator/_hotspots.py", "target": "tests/test_resolver.py"}]}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "random"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._pipeline"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._watcher"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._mermaid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "textwrap"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._documentation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._exporter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._hotspots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._layer_rules"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._rule_gen"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._sarif"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._c"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._python"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._go"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._rust"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._javascript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._java"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._csharp"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._shell"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._php"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._dart"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._gdscript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._nim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._assembly"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._ruby"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._swift"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._kotlin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._scala"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._lua"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._elixir"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "ast"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "readmenator.__main__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "shlex"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._documentation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._exporter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._hotspots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._layer_rules"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "readmenator._mermaid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_models.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_models.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._rule_gen"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._sarif"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_analyzer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_analyzer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_pipeline.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_watcher.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cache.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cpg.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_mermaid.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_exporter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_exporter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_hotspots.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_hotspots.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layer_rules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layer_rules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layers.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mermaid.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_documentation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_exporter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_hotspots.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_layer_rules.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_rule_gen.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_sarif.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rule_gen.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rule_gen.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_sarif.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_security.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_security.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_taint.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_taint.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_watcher.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_c.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_python.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_go.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_rust.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_javascript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_java.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_csharp.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_shell.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_php.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_dart.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_gdscript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_nim.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_assembly.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_ruby.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_swift.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_kotlin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_scala.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_lua.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_elixir.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_base.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_base.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_c.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_c.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_go.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_go.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_java.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_java.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_php.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_php.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_python.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_python.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator.py", "target": "readmenator/__main__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cache.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cache.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_config.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_documentation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_exporter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_hotspots.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integration.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integration.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_layer_rules.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mermaid.py", "target": "readmenator/_mermaid.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mermaid.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_models.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_new.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_new.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_query.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_query.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_resolver.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_rule_gen.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_sarif.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_taint.py"}], "generator": "readmenator", "metadata": {"edge_count": 4296, "file_count": 67, "language_count": 1, "symbol_count": 717}, "nodes": [{"id": "readmenator/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "693c306a8ca0b67d", "symbol_count": 0, "symbols": []}, {"id": "readmenator/__main__.py", "kind": "module", "label": "__main__.py", "language": "py", "sha256": "0cae1a2caefaa78c", "symbol_count": 3, "symbols": [{"kind": "function", "line": 14, "name": "build_parser", "signature": "def build_parser()"}, {"kind": "function", "line": 59, "name": "_run_tests", "signature": "def _run_tests()"}, {"kind": "function", "line": 74, "name": "main", "signature": "def main()"}]}, {"id": "readmenator/_analyzer.py", "kind": "module", "label": "_analyzer.py", "language": "py", "sha256": "d56e0b4c1dbc4e05", "symbol_count": 13, "symbols": [{"doc": "Deterministic graph analysis over scanned nodes and edges.\n\nBuilds an internal adjacency graph from import edges, then applies\ncommunity detection, centrality scoring, cross-community bridge\ndiscovery, and question generation without any external API calls.", "kind": "class", "line": 20, "name": "GraphAnalyzer", "signature": "class GraphAnalyzer"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings for thresholds and limits.", "kind": "method", "line": 28, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run the full analysis pipeline and return structured results.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges from the scanner.\n    resolved_edges: Optional list of resolved-import edges (source and\n        target are both project file IDs).\n\nReturns:\n    An AnalysisResult with god nodes, communities, surprising\n    connections, and suggested questions.", "kind": "method", "line": 36, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges)"}, {"doc": "Build an undirected adjacency map from import edges.", "kind": "method", "line": 89, "name": "_build_adjacency", "signature": "def _build_adjacency(self, nodes, edges)"}, {"doc": "Build a directed reverse adjacency (incoming edges) map.", "kind": "method", "line": 103, "name": "_build_reverse_adjacency", "signature": "def _build_reverse_adjacency(self, adjacency)"}, {"doc": "Compute the most central nodes using combined degree centrality.\n\nScore is a combination of out-degree (imports), in-degree (imported-by),\nand symbol count. Higher score means more architecturally significant.", "kind": "method", "line": 113, "name": "_compute_god_nodes", "signature": "def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)"}, {"doc": "Detect communities using label propagation.\n\nEach node adopts the most frequent community label among its\nneighbors. Iterates until convergence or max iterations reached.\nSimple, deterministic, and correct for connected graphs.", "kind": "method", "line": 135, "name": "_detect_communities", "signature": "def _detect_communities(self, nodes, adjacency)"}, {"doc": "Generate human-readable labels for communities.\n\nLabels are based on the most common directory within the community.", "kind": "method", "line": 186, "name": "_label_communities", "signature": "def _label_communities(self, nodes, communities)"}, {"doc": "Build a reverse map from file ID to community ID.", "kind": "method", "line": 213, "name": "_build_community_map", "signature": "def _build_community_map(self, communities)"}, {"doc": "Compute cohesion score for each community.\n\nCohesion = internal edges / (internal edges + external edges).", "kind": "method", "line": 223, "name": "_compute_cohesion", "signature": "def _compute_cohesion(self, communities, adjacency)"}, {"doc": "Find non-obvious cross-community bridges.\n\nA connection is surprising when two nodes in different communities\nare connected indirectly through 3 or more hops, and the path\ncrosses community boundaries.", "kind": "method", "line": 248, "name": "_find_surprising_connections", "signature": "def _find_surprising_connections(self, nodes, adjacency, community_map)"}, {"doc": "Find the shortest path and communities traversed.", "kind": "method", "line": 288, "name": "_shortest_path_communities", "signature": "def _shortest_path_communities(self, source, target, adjacency, community_map)"}, {"doc": "Generate plain-language exploration questions from graph structure.", "kind": "method", "line": 315, "name": "_suggest_questions", "signature": "def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)"}]}, {"id": "readmenator/_app.py", "kind": "module", "label": "_app.py", "language": "py", "sha256": "a5165449ff6befd6", "symbol_count": 29, "symbols": [{"kind": "class", "line": 24, "name": "readmenatorApplication", "signature": "class readmenatorApplication"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 34, "name": "_scan", "signature": "def _scan(self, target_dir)"}, {"kind": "method", "line": 42, "name": "_scan_with_content", "signature": "def _scan_with_content(self, target_dir)"}, {"kind": "method", "line": 52, "name": "_resolve_imports", "signature": "def _resolve_imports(self, nodes, edges, target_dir)"}, {"kind": "method", "line": 71, "name": "run", "signature": "def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)"}, {"kind": "method", "line": 122, "name": "_write_sidecar_outputs", "signature": "def _write_sidecar_outputs(self, root, findings, analysis_v2)"}, {"kind": "method", "line": 148, "name": "_log_summary", "signature": "def _log_summary(self, nodes, edges, resolved_edges, analysis, layer_summary, analysis_v2, findings)"}, {"kind": "method", "line": 202, "name": "update", "signature": "def update(self, target_dir, run_security)"}, {"kind": "method", "line": 233, "name": "_scan_for_cache", "signature": "def _scan_for_cache(self, root, cache)"}, {"kind": "method", "line": 251, "name": "query", "signature": "def query(self, target_dir, question)"}, {"kind": "method", "line": 256, "name": "explain", "signature": "def explain(self, target_dir, symbol_name)"}, {"kind": "method", "line": 268, "name": "find_path", "signature": "def find_path(self, target_dir, symbol_a, symbol_b)"}, {"kind": "method", "line": 281, "name": "summary", "signature": "def summary(self, target_dir)"}, {"kind": "method", "line": 286, "name": "rebuild", "signature": "def rebuild(self, target_dir, run_security)"}, {"kind": "method", "line": 289, "name": "analyze", "signature": "def analyze(self, target_dir)"}, {"kind": "method", "line": 293, "name": "export_json", "signature": "def export_json(self, target_dir, output_path)"}, {"kind": "method", "line": 304, "name": "export_html", "signature": "def export_html(self, target_dir, output_path)"}, {"kind": "method", "line": 315, "name": "export_svg", "signature": "def export_svg(self, target_dir, output_path)"}, {"kind": "method", "line": 326, "name": "export", "signature": "def export(self, target_dir)"}, {"kind": "method", "line": 331, "name": "export_graphml", "signature": "def export_graphml(self, target_dir, output_path)"}, {"kind": "method", "line": 342, "name": "export_obsidian", "signature": "def export_obsidian(self, target_dir, output_dir)"}, {"kind": "method", "line": 352, "name": "watch", "signature": "def watch(self, target_dir)"}, {"kind": "method", "line": 362, "name": "audit", "signature": "def audit(self, target_dir)"}, {"kind": "method", "line": 369, "name": "audit_deep", "signature": "def audit_deep(self, target_dir)"}, {"kind": "method", "line": 389, "name": "export_sarif", "signature": "def export_sarif(self, target_dir, output_path)"}, {"kind": "method", "line": 399, "name": "export_rules", "signature": "def export_rules(self, target_dir, output_dir)"}, {"kind": "method", "line": 409, "name": "detect_layers", "signature": "def detect_layers(self, target_dir)"}, {"kind": "method", "line": 356, "name": "on_change", "signature": "def on_change()"}]}, {"id": "readmenator/_cache.py", "kind": "module", "label": "_cache.py", "language": "py", "sha256": "c01bab06c4962e46", "symbol_count": 8, "symbols": [{"doc": "SHA256-based cache for incremental file scanning.\n\nStores a JSON mapping of relative file paths to their content\nhashes inside the project's cache directory. On subsequent runs,\nfiles whose hash matches the cached value are skipped.", "kind": "class", "line": 19, "name": "FileCache", "signature": "class FileCache"}, {"doc": "Initialise cache for the given project root.\n\nArgs:\n    config: Application settings including CACHE_DIR.\n    project_root: Absolute path of the scanned project.", "kind": "method", "line": 27, "name": "__init__", "signature": "def __init__(self, config, project_root)"}, {"doc": "Load the cached hash map from disk.\n\nReturns:\n    Dict mapping relative file paths to their SHA256 hex digests.", "kind": "method", "line": 38, "name": "load", "signature": "def load(self)"}, {"doc": "Persist the hash map to disk.\n\nArgs:\n    hashes: Dict mapping relative file paths to SHA256 hex digests.", "kind": "method", "line": 54, "name": "save", "signature": "def save(self, hashes)"}, {"doc": "Compute the SHA256 hex digest of a file's contents.\n\nArgs:\n    file_path: Absolute path to the file.\n\nReturns:\n    SHA256 hex digest string.", "kind": "method", "line": 65, "name": "compute_hash", "signature": "def compute_hash(self, file_path)"}, {"doc": "Compute hashes for a batch of relative-path-to-absolute-path mappings.\n\nArgs:\n    file_paths: Dict mapping relative paths to absolute Path objects.\n\nReturns:\n    Dict mapping relative paths to their SHA256 hex digests.", "kind": "method", "line": 82, "name": "compute_hashes", "signature": "def compute_hashes(self, file_paths)"}, {"doc": "Determine which files have changed since the last cache.\n\nArgs:\n    file_paths: Dict mapping relative paths to absolute Path objects.\n\nReturns:\n    Set of relative paths for files that are new or changed.", "kind": "method", "line": 98, "name": "find_changed", "signature": "def find_changed(self, file_paths)"}, {"doc": "Remove entries for files that no longer exist on disk.\n\nArgs:\n    current_file_ids: Set of relative paths currently in the project.", "kind": "method", "line": 120, "name": "prune_deleted", "signature": "def prune_deleted(self, current_file_ids)"}]}, {"id": "readmenator/_config.py", "kind": "module", "label": "_config.py", "language": "py", "sha256": "a5ac9a21b5bd0467", "symbol_count": 1, "symbols": [{"doc": "Single source of truth for all readmenator settings.\n\nEvery tuneable constant -- file-size limits, directory depth,\nsupported extensions, symbol pluralisation map, Mermaid style\ntokens, graph analysis thresholds, and export settings -- is\ndefined here and consumed by reference elsewhere.", "kind": "class", "line": 15, "name": "Config", "signature": "class Config"}]}, {"id": "readmenator/_cpg.py", "kind": "module", "label": "_cpg.py", "language": "py", "sha256": "8afe5303232e87a1", "symbol_count": 5, "symbols": [{"doc": "Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.\n\nProduces a structured representation merging AST-level symbol data,\ncontrol-flow edges (calls), data-flow edges (imports), and inheritance\nrelationships into a single machine-readable document. Designed to be\nembedded in KNOWLEDGE_BASE.md for zero-token agent context.", "kind": "class", "line": 10, "name": "CodePropertyGraph", "signature": "class CodePropertyGraph"}, {"kind": "method", "line": 21, "name": "__init__", "signature": "def __init__(self, privacy_mode)"}, {"doc": "Generate the CPG JSON-LD string embeddable in markdown.\n\nReturns a compact JSON object with @context, nodes array (each\ncontaining id, label, kind, language, sha256, symbols, layer),\nedges array (source, target, relation, confidence), and analysis\nmetadata (god_nodes, communities).", "kind": "method", "line": 24, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Build symbol list for a node, respecting privacy mode.", "kind": "method", "line": 109, "name": "_build_symbol_list", "signature": "def _build_symbol_list(self, node)"}, {"doc": "Compute a deterministic content hash for a node.", "kind": "method", "line": 126, "name": "_compute_node_hash", "signature": "def _compute_node_hash(node)"}]}, {"id": "readmenator/_documentation.py", "kind": "module", "label": "_documentation.py", "language": "py", "sha256": "fab2e04863ba7289", "symbol_count": 20, "symbols": [{"doc": "Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.\n\nDelegates graph rendering to MermaidRenderer and handles the\nMarkdown layout: header metadata, Mermaid block, statistics dashboard,\ngod nodes, community analysis, surprising connections, architecture\nlayers, security audit, taint analysis, hotspots, dependency cycles,\nchange impact, architecture violations, suggested rules, CPG block,\nand per-language architecture sections with pluralised symbol kind headings.", "kind": "class", "line": 24, "name": "DocumentationGenerator", "signature": "class DocumentationGenerator"}, {"kind": "method", "line": 35, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 49, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2)"}, {"kind": "method", "line": 105, "name": "_build_toc", "signature": "def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated)"}, {"kind": "method", "line": 172, "name": "_build_layers", "signature": "def _build_layers(self, layers, nodes)"}, {"kind": "method", "line": 206, "name": "_build_dashboard", "signature": "def _build_dashboard(self, nodes, edges, resolved_edges)"}, {"kind": "method", "line": 286, "name": "_build_god_nodes", "signature": "def _build_god_nodes(self, analysis)"}, {"kind": "method", "line": 306, "name": "_build_community_analysis", "signature": "def _build_community_analysis(self, analysis, nodes)"}, {"kind": "method", "line": 339, "name": "_build_surprising_connections", "signature": "def _build_surprising_connections(self, analysis, nodes)"}, {"kind": "method", "line": 364, "name": "_build_suggested_questions", "signature": "def _build_suggested_questions(self, analysis)"}, {"kind": "method", "line": 380, "name": "_build_taint_analysis", "signature": "def _build_taint_analysis(self, analysis_v2)"}, {"kind": "method", "line": 415, "name": "_build_hotspots", "signature": "def _build_hotspots(self, analysis_v2)"}, {"kind": "method", "line": 441, "name": "_build_dependency_cycles", "signature": "def _build_dependency_cycles(self, analysis_v2)"}, {"kind": "method", "line": 461, "name": "_build_change_impact", "signature": "def _build_change_impact(self, analysis_v2)"}, {"kind": "method", "line": 486, "name": "_build_layer_violations", "signature": "def _build_layer_violations(self, analysis_v2)"}, {"kind": "method", "line": 514, "name": "_build_suggested_rules", "signature": "def _build_suggested_rules(self, analysis_v2)"}, {"kind": "method", "line": 539, "name": "_build_security_findings", "signature": "def _build_security_findings(self, findings)"}, {"kind": "method", "line": 586, "name": "_build_mermaid_section", "signature": "def _build_mermaid_section(self, graph_output, is_truncated)"}, {"kind": "method", "line": 609, "name": "_build_cpg_block", "signature": "def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)"}, {"kind": "method", "line": 635, "name": "_build_architecture_reference", "signature": "def _build_architecture_reference(self, nodes, edges)"}]}, {"id": "readmenator/_exporter.py", "kind": "module", "label": "_exporter.py", "language": "py", "sha256": "292742323c0af8f9", "symbol_count": 14, "symbols": [{"doc": "Exports the knowledge graph to JSON, HTML, and SVG formats.\n\nEach method is self-contained and produces a single file. No\nexternal network calls are made; the HTML file embeds vis.js\nfrom a CDN reference for offline-compatible rendering.", "kind": "class", "line": 21, "name": "GraphExporter", "signature": "class GraphExporter"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings for export styling and limits.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Export the graph as a node-link JSON string.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for metadata.\n    findings: Optional security audit findings.\n\nReturns:\n    JSON string with nodes, edges, and optional analysis/findings metadata.", "kind": "method", "line": 37, "name": "to_json", "signature": "def to_json(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Generate a standalone interactive HTML graph page.\n\nUses vis.js loaded from CDN. Supports click-to-inspect nodes,\nsearch filtering, and community-based coloring.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community coloring.\n\nReturns:\n    Complete HTML document as a string.", "kind": "method", "line": 150, "name": "to_html", "signature": "def to_html(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Build a node-to-color map based on community membership.", "kind": "method", "line": 236, "name": "_community_color_map", "signature": "def _community_color_map(self, analysis)"}, {"doc": "Lighten a hex color by 30% for border use.", "kind": "method", "line": 254, "name": "_lighten", "signature": "def _lighten(hex_color)"}, {"doc": "Render the full HTML document with vis.js.", "kind": "method", "line": 262, "name": "_render_html", "signature": "def _render_html(self, vis_nodes, vis_edges, analysis, findings)"}, {"doc": "Generate a static SVG representation of the graph.\n\nUses a simple force-directed layout without external dependencies.\nFor graphs with more than SVG_MAX_NODES, returns a plain SVG\nwith a truncation message.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community coloring.\n\nReturns:\n    SVG document as a string.", "kind": "method", "line": 421, "name": "to_svg", "signature": "def to_svg(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Render a minimal SVG with a truncation notice.", "kind": "method", "line": 539, "name": "_render_truncated_svg", "signature": "def _render_truncated_svg(self, total_nodes)"}, {"doc": "Compute a simple spring-layout for node positioning.\n\nImplements a basic force-directed layout with repulsion\nbetween all nodes and attraction along edges. Runs a fixed\nnumber of iterations for determinism.", "kind": "method", "line": 554, "name": "_layout_spring", "signature": "def _layout_spring(self, nodes, edges, node_map)"}, {"doc": "Export the graph as GraphML (Gephi/yEd compatible).\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community data.\n\nReturns:\n    GraphML XML string.", "kind": "method", "line": 635, "name": "to_graphml", "signature": "def to_graphml(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Export the graph as an Obsidian vault with wikilinks.\n\nEach file node becomes a markdown note. Community hub notes\naggregate related files. All notes use [[wikilinks]] for\nObsidian graph navigation.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    output_dir: Directory to write the Obsidian notes.\n    analysis: Optional analysis results for community hubs.\n\nReturns:\n    Number of notes written.", "kind": "method", "line": 712, "name": "to_obsidian", "signature": "def to_obsidian(self, nodes, edges, output_dir, analysis)"}, {"kind": "method", "line": 483, "name": "_project", "signature": "def _project(pos)"}, {"kind": "method", "line": 334, "name": "_sev_span", "signature": "def _sev_span(sev, count)"}]}, {"id": "readmenator/_hotspots.py", "kind": "module", "label": "_hotspots.py", "language": "py", "sha256": "55e2be7374ada787", "symbol_count": 7, "symbols": [{"doc": "Hotspot detection, cycle analysis, and change impact analysis.\n\nHotspots are files with high complexity (many symbols) and high\ncentrality (many connections). Cycle detection finds circular\ndependencies in the resolved import graph. Change impact analysis\ncomputes transitive-dependent lists for every file.", "kind": "class", "line": 16, "name": "HotspotAnalyzer", "signature": "class HotspotAnalyzer"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Rank files by combined complexity and centrality scores.\n\nComplexity is normalised symbol count. Centrality is normalised\nconnection count (in-degree + out-degree). The combined score\nuses configured weights.", "kind": "method", "line": 28, "name": "analyze_hotspots", "signature": "def analyze_hotspots(self, nodes, edges, resolved_edges)"}, {"doc": "Detect cycles in the resolved import graph using DFS.\n\nUses Tarjan's algorithm variant with three-colour DFS to find\nall elementary cycles. Returns each cycle as a DependencyCycle.", "kind": "method", "line": 84, "name": "detect_cycles", "signature": "def detect_cycles(self, nodes, resolved_edges)"}, {"doc": "Compute change impact for every file in the project.\n\nFor each file, finds all files that would be affected if it\nchanged (direct and transitive dependents via reverse import\ngraph traversal).", "kind": "method", "line": 149, "name": "analyze_change_impact", "signature": "def analyze_change_impact(self, nodes, resolved_edges)"}, {"kind": "method", "line": 108, "name": "_dfs_visit", "signature": "def _dfs_visit(current)"}, {"kind": "method", "line": 119, "name": "_record_cycle", "signature": "def _record_cycle(start, end)"}]}, {"id": "readmenator/_layer_rules.py", "kind": "module", "label": "_layer_rules.py", "language": "py", "sha256": "8349f119aa3b1869", "symbol_count": 4, "symbols": [{"doc": "Architectural layer violation detection engine.\n\nDefines a set of permitted and forbidden layer-to-layer import\nrules. Scans all resolved import edges and flags violations\nwhere one layer imports from another in a way that violates\nthe architecture.", "kind": "class", "line": 9, "name": "LayerRuleEngine", "signature": "class LayerRuleEngine"}, {"kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Detect architectural layer violations.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved import edges.\n    layers: Dict mapping node_id to layer name. If None, imports\n        _layers.LayerDetector for automatic detection.\n\nReturns:\n    List of LayerViolation instances.", "kind": "method", "line": 37, "name": "detect_violations", "signature": "def detect_violations(self, nodes, edges, resolved_edges, layers)"}, {"doc": "Summarise violations by severity.", "kind": "method", "line": 109, "name": "violation_summary", "signature": "def violation_summary(violations)"}]}, {"id": "readmenator/_layers.py", "kind": "module", "label": "_layers.py", "language": "py", "sha256": "eca6996d1404b8ec", "symbol_count": 4, "symbols": [{"doc": "Detects architectural layers in a codebase.\n\nAssigns each file to a layer based on path patterns, naming\nconventions, and imported frameworks. Returns a mapping that\ncan enrich documentation and analysis. No config dependency.", "kind": "class", "line": 15, "name": "LayerDetector", "signature": "class LayerDetector"}, {"doc": "Assign each file node to an architectural layer.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n\nReturns:\n    Dict mapping node_id to layer name.", "kind": "method", "line": 71, "name": "detect", "signature": "def detect(self, nodes, edges)"}, {"doc": "Classify a single file into an architectural layer.", "kind": "method", "line": 89, "name": "_classify_file", "signature": "def _classify_file(self, node, edges)"}, {"doc": "Count files per layer.\n\nArgs:\n    layers: Mapping from detect().\n\nReturns:\n    Dict of layer_name -> file_count.", "kind": "method", "line": 122, "name": "layer_summary", "signature": "def layer_summary(layers)"}]}, {"id": "readmenator/_mermaid.py", "kind": "module", "label": "_mermaid.py", "language": "py", "sha256": "5832baaa4731cd40", "symbol_count": 4, "symbols": [{"doc": "Renders a knowledge graph to Mermaid JS flowchart syntax.\n\nNodes are ordered by import count and symbol richness; the top\n``max_nodes`` entries are included. External dependencies appear\nas dashed boxes. Internal import edges are solid arrows.\nCommunity subgraphs group related files when analysis is available.", "kind": "class", "line": 17, "name": "MermaidRenderer", "signature": "class MermaidRenderer"}, {"kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)"}, {"doc": "Convert *node_id* to a Mermaid-safe identifier.\n\nReplaces non-alphanumeric characters with underscores and\nprepends ``n_`` if the result starts with a digit.", "kind": "method", "line": 45, "name": "_sanitize_id", "signature": "def _sanitize_id(node_id)"}, {"doc": "Produce a Mermaid flowchart string and a truncation flag.\n\nNodes are sorted by import popularity, then by symbol count.\nInternal import edges (between project files) are rendered as\nsolid arrows when *resolved_edges* is provided. Community\nsubgraphs wrap related files when *analysis* is given.\n\nReturns:\n    Tuple of (Mermaid source string, is_truncated bool).", "kind": "method", "line": 56, "name": "render", "signature": "def render(self, nodes, edges, resolved_edges, analysis)"}]}, {"id": "readmenator/_models.py", "kind": "module", "label": "_models.py", "language": "py", "sha256": "0f08c578bd33b736", "symbol_count": 15, "symbols": [{"doc": "A single code symbol extracted from a source file.\n\nAttributes:\n    name: Identifier of the symbol (class name, function name, etc.).\n    kind: Semantic type (class, function, struct, enum, ...).\n    line: One-based line number where the symbol is defined.\n    doc: Optional docstring or comment extracted from the source.\n    signature: Optional method or function signature snippet.", "kind": "class", "line": 16, "name": "Symbol", "signature": "class Symbol"}, {"doc": "A file node in the knowledge graph, containing its symbols.\n\nAttributes:\n    node_id: Relative path of the file used as a unique identifier.\n    label: Base file name for display purposes.\n    kind: Type of node (typically \"module\").\n    language: Programming language derived from the file extension.\n    doc: Optional file-level documentation string.\n    symbols: List of Symbol instances defined in this file.", "kind": "class", "line": 35, "name": "Node", "signature": "class Node"}, {"doc": "A directed relationship between two nodes in the knowledge graph.\n\nAttributes:\n    source: Node ID of the source (dependent) file.\n    target: Node ID of the target (dependency) file or module.\n    relation: Semantic relation label (e.g. \"imports\", \"resolved_imports\").\n    confidence: Confidence tier (\"EXTRACTED\" for structural, \"INFERRED\" for heuristic).", "kind": "class", "line": 56, "name": "Edge", "signature": "class Edge"}, {"doc": "A security-relevant pattern detected in a source file.\n\nAttributes:\n    file_path: Relative path of the file containing the finding.\n    line: One-based line number where the pattern was found.\n    severity: Severity level (critical, high, medium, low, info).\n    rule_id: Unique identifier for the detection rule (e.g. \"PY001\").\n    description: Human-readable explanation of the issue.\n    snippet: The offending source code line.\n    cwe: CWE identifier string (e.g. \"CWE-78\").", "kind": "class", "line": 73, "name": "SecurityFinding", "signature": "class SecurityFinding"}, {"doc": "Return the plural form of *kind* according to *plural_map*.\n\nFalls back to appending ``\"s\"`` when the kind is not found.\nThis prevents obvious misspellings like ``\"Classs\"``.", "kind": "method", "line": 95, "name": "pluralize_symbol_kind", "signature": "def pluralize_symbol_kind(kind, plural_map)"}, {"doc": "Result of community detection on the import graph.\n\nAttributes:\n    community_id: Integer identifier of the community.\n    label: Human-readable name for the community.\n    file_ids: Set of node IDs belonging to this community.\n    cohesion: Cohesion score (internal edges / total edges involving community).\n    size: Number of files in the community.", "kind": "class", "line": 105, "name": "CommunityResult", "signature": "class CommunityResult"}, {"doc": "Complete graph analysis output.\n\nAttributes:\n    god_nodes: List of (node_id, score) for most central nodes.\n    communities: List of CommunityResult instances.\n    surprising_connections: List of (source_node, target_node, hops, bridging_communities).\n    suggested_questions: List of plain-language exploration questions.\n    node_count: Total nodes in the graph.\n    edge_count: Total edges in the graph.", "kind": "class", "line": 124, "name": "AnalysisResult", "signature": "class AnalysisResult"}, {"doc": "A taint propagation path from source to sink through the import graph.\n\nAttributes:\n    source_file: The file that introduces the dangerous import.\n    sink_file: The file that transitively receives the taint.\n    path: List of file node IDs forming the propagation chain.\n    hops: Number of hops in the propagation path.\n    dangerous_import: The specific dangerous module or function imported.\n    severity: Inferred severity of the taint path.", "kind": "class", "line": 145, "name": "TaintPath", "signature": "class TaintPath"}, {"doc": "Complete taint propagation analysis output.\n\nAttributes:\n    paths: List of TaintPath instances discovered.\n    source_count: Number of unique taint source files.\n    sink_count: Number of unique taint sink files.", "kind": "class", "line": 166, "name": "TaintAnalysisResult", "signature": "class TaintAnalysisResult"}, {"doc": "A cycle detected in the resolved import graph.\n\nAttributes:\n    cycle: List of file node IDs forming the cycle.\n    length: Number of files in the cycle.", "kind": "class", "line": 181, "name": "DependencyCycle", "signature": "class DependencyCycle"}, {"doc": "Change impact analysis for a single file.\n\nAttributes:\n    file_id: The file that would be changed.\n    direct_dependents: Files that directly import this file.\n    transitive_dependents: Files that transitively depend on this file.\n    total_impact: Total number of affected files (direct + transitive).", "kind": "class", "line": 194, "name": "ChangeImpact", "signature": "class ChangeImpact"}, {"doc": "A hotspot file combining complexity and centrality metrics.\n\nAttributes:\n    file_id: The file node ID.\n    complexity_score: Normalised symbol count score (0-1).\n    centrality_score: Normalised god node score (0-1).\n    combined_score: Weighted combination of complexity and centrality.\n    symbol_count: Raw symbol count.\n    connection_count: Raw connection count.", "kind": "class", "line": 211, "name": "HotspotResult", "signature": "class HotspotResult"}, {"doc": "A suggested linting/security rule derived from code patterns.\n\nAttributes:\n    rule_id: Suggested rule identifier (e.g. \"RM001\").\n    severity: Suggested severity (info, warning, error).\n    description: Human-readable description of the pattern.\n    pattern: The detected pattern or code snippet.\n    file_examples: Example file paths where the pattern was found.\n    match_count: Number of times the pattern was matched.\n    language: Target language for the rule.\n    semgrep_yaml: Optional Semgrep rule YAML string.", "kind": "class", "line": 232, "name": "SuggestedRule", "signature": "class SuggestedRule"}, {"doc": "A detected architectural layer violation.\n\nAttributes:\n    source_file: The file causing the violation.\n    source_layer: The layer of the source file.\n    target_file: The file being imported.\n    target_layer: The layer of the target file.\n    description: Description of the violation.\n    severity: Severity (strict, warn, info).", "kind": "class", "line": 257, "name": "LayerViolation", "signature": "class LayerViolation"}, {"doc": "Extended analysis result combining all new analysis modules.\n\nAttributes:\n    taint: Optional taint analysis result.\n    cycles: List of dependency cycles.\n    change_impacts: List of change impact results for key files.\n    hotspots: List of hotspot results.\n    suggested_rules: List of suggested linting rules.\n    layer_violations: List of layer violations.", "kind": "class", "line": 278, "name": "AnalysisResultV2", "signature": "class AnalysisResultV2"}]}, {"id": "readmenator/_pipeline.py", "kind": "module", "label": "_pipeline.py", "language": "py", "sha256": "6ec75fdc90c75f18", "symbol_count": 17, "symbols": [{"doc": "Lazy factory for all readmenator analyzer and generator instances.\n\nDecouples the application orchestrator from the concrete\ninstantiation of analysis modules. Each component is created\non first access and cached for the lifetime of the factory.", "kind": "class", "line": 28, "name": "AnalyzerFactory", "signature": "class AnalyzerFactory"}, {"doc": "Orchestrates the extended V2 analysis pipeline.\n\nRuns taint propagation, hotspot detection, cycle detection,\nchange impact, layer violations, and rule generation as a\ncoordinated batch. Isolated from the main app to reduce\ncoupling in the primary orchestration layer.", "kind": "class", "line": 124, "name": "DeepAnalysisRunner", "signature": "class DeepAnalysisRunner"}, {"kind": "method", "line": 36, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 52, "name": "scanner", "signature": "def scanner(self)"}, {"kind": "method", "line": 58, "name": "generator", "signature": "def generator(self)"}, {"kind": "method", "line": 64, "name": "analyzer", "signature": "def analyzer(self)"}, {"kind": "method", "line": 70, "name": "security", "signature": "def security(self)"}, {"kind": "method", "line": 76, "name": "exporter", "signature": "def exporter(self)"}, {"kind": "method", "line": 82, "name": "taint", "signature": "def taint(self)"}, {"kind": "method", "line": 88, "name": "hotspots", "signature": "def hotspots(self)"}, {"kind": "method", "line": 94, "name": "layer_rules", "signature": "def layer_rules(self)"}, {"kind": "method", "line": 100, "name": "rule_gen", "signature": "def rule_gen(self)"}, {"kind": "method", "line": 106, "name": "sarif", "signature": "def sarif(self)"}, {"kind": "method", "line": 112, "name": "cpg", "signature": "def cpg(self)"}, {"kind": "method", "line": 118, "name": "layer_detector", "signature": "def layer_detector(self)"}, {"kind": "method", "line": 133, "name": "__init__", "signature": "def __init__(self, factory)"}, {"kind": "method", "line": 136, "name": "run", "signature": "def run(self, nodes, edges, resolved_edges, layers, content_map)"}]}, {"id": "readmenator/_query.py", "kind": "module", "label": "_query.py", "language": "py", "sha256": "0713a8e96feda8ce", "symbol_count": 13, "symbols": [{"doc": "In-memory query engine over the scanned knowledge graph.\n\nBuilds a symbol-name index and an import-adjacency graph on\nconstruction. Provides exact and fuzzy symbol lookup, detailed\nexplanation output, BFS shortest-path resolution, free-text\nsearch, and a summary report.", "kind": "class", "line": 17, "name": "QueryEngine", "signature": "class QueryEngine"}, {"doc": "Initialise internal indexes from scanned data.\n\nArgs:\n    nodes: List of scanned file nodes.\n    edges: List of import-relationship edges.\n    resolved_edges: Optional resolved-import edges (both\n        source and target are project file IDs).", "kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self, nodes, edges, resolved_edges)"}, {"doc": "Build a name-to-list-of-(node, symbol) lookup.\n\nReturns:\n    Dict mapping symbol names to list of (Node, Symbol) tuples.", "kind": "method", "line": 47, "name": "_build_symbol_index", "signature": "def _build_symbol_index(self)"}, {"doc": "Build an adjacency map from import edges.\n\nReturns:\n    Dict mapping each file node_id to its set of import targets.", "kind": "method", "line": 61, "name": "_build_import_graph", "signature": "def _build_import_graph(self)"}, {"doc": "Build an adjacency map from resolved import edges.\n\nOnly contains edges where both source and target are\nproject files (not external modules).\n\nReturns:\n    Dict mapping each file node_id to files it imports within the project.", "kind": "method", "line": 77, "name": "_build_resolved_graph", "signature": "def _build_resolved_graph(self)"}, {"doc": "Look up *name* by exact match, then by substring fuzzy match.\n\nReturns:\n    A list of (Node, Symbol) tuples, or ``None`` if not found.", "kind": "method", "line": 97, "name": "find_symbol", "signature": "def find_symbol(self, name)"}, {"doc": "Return a detailed multi-line explanation of *name*.\n\nIncludes kind, file path, line number, docstring, signature,\nimports, reverse dependencies (\"imported by\"), and sibling\nsymbols in the same file.\n\nReturns:\n    Formatted string or ``None`` if the symbol is not found.", "kind": "method", "line": 115, "name": "explain", "signature": "def explain(self, name)"}, {"doc": "List all node IDs that import *target*.", "kind": "method", "line": 154, "name": "_find_incoming_imports", "signature": "def _find_incoming_imports(self, target)"}, {"doc": "Find the shortest import path from *symbol_a* to *symbol_b*.\n\nUses BFS on the resolved import graph (project-internal edges)\nfirst, traversing in both directions (forward = A imports B,\nreverse = B is imported by A). Falls back to the raw import\ngraph if no resolved path exists.\n\nReturns:\n    List of file node IDs forming the dependency chain, or ``None``.", "kind": "method", "line": 162, "name": "find_path", "signature": "def find_path(self, symbol_a, symbol_b)"}, {"doc": "Convert a directed graph to a bidirectional one.\n\nFor each edge A→B, adds both A→B and B→A edges.", "kind": "method", "line": 192, "name": "_make_bidirectional", "signature": "def _make_bidirectional(graph)"}, {"doc": "Run BFS to find the shortest path from *start* to *goal*.\n\nReturns:\n    List of node IDs or ``None`` if no path exists.", "kind": "method", "line": 208, "name": "_bfs_shortest_path", "signature": "def _bfs_shortest_path(self, graph, start, goal)"}, {"doc": "Free-text search over symbols and file paths.\n\nTokenises the input, matches against symbol names (substring)\nand then against file paths as a fallback. Returns a\nhuman-readable result string summarising matches or a\nno-results message with KB statistics.", "kind": "method", "line": 232, "name": "query", "signature": "def query(self, question)"}, {"doc": "Return a concise overview of the loaded knowledge base.\n\nReports file count, symbol count, import count, language\ndiversity, top-level modules (by import popularity), and\nlists of key class-like and function-like symbols.", "kind": "method", "line": 288, "name": "summary", "signature": "def summary(self)"}]}, {"id": "readmenator/_resolver.py", "kind": "module", "label": "_resolver.py", "language": "py", "sha256": "e90a8f4bbda2c204", "symbol_count": 11, "symbols": [{"doc": "Resolves raw import strings to project file paths.\n\nUses heuristics tuned to each language's import conventions:\nPython dots to slashes, Java dots to directory separators,\nrelative-path resolution, and extensionless module detection.", "kind": "class", "line": 15, "name": "ImportResolver", "signature": "class ImportResolver"}, {"doc": "Initialise the resolver with all known file paths.\n\nArgs:\n    file_ids: List of relative file paths from the scan.\n    root: Root directory for relative-path resolution.", "kind": "method", "line": 58, "name": "__init__", "signature": "def __init__(self, file_ids, root)"}, {"doc": "Map file stems (without extension) to their full paths.", "kind": "method", "line": 70, "name": "_build_stem_index", "signature": "def _build_stem_index(self, file_ids)"}, {"doc": "Map directory paths to the files they contain.", "kind": "method", "line": 80, "name": "_build_dir_index", "signature": "def _build_dir_index(self, file_ids)"}, {"doc": "Resolve an import string to a concrete project file path.\n\nArgs:\n    import_str: The raw import string from the parser.\n    source_file: The file that contains the import (for relative resolution).\n\nReturns:\n    Matching file node ID or ``None`` if no match found.", "kind": "method", "line": 97, "name": "resolve", "signature": "def resolve(self, import_str, source_file)"}, {"doc": "Resolve *import_str* to all possible matching project file paths.\n\nArgs:\n    import_str: The raw import string.\n    source_file: The file that contains the import.\n\nReturns:\n    List of matching file node IDs (may be empty).", "kind": "method", "line": 132, "name": "resolve_all", "signature": "def resolve_all(self, import_str, source_file)"}, {"doc": "Resolve a relative import (starts with ``.`` or ``..``).", "kind": "method", "line": 148, "name": "_resolve_relative", "signature": "def _resolve_relative(self, import_str, source_file)"}, {"doc": "Resolve a bare module name by appending known extensions.", "kind": "method", "line": 166, "name": "_resolve_extensionless", "signature": "def _resolve_extensionless(self, import_str, source_file)"}, {"doc": "Resolve as a package directory with __init__ or index file.", "kind": "method", "line": 175, "name": "_resolve_directory_init", "signature": "def _resolve_directory_init(self, import_str, source_file)"}, {"doc": "Resolve a dotted module path (Python/Java convention).", "kind": "method", "line": 185, "name": "_resolve_module_dotpath", "signature": "def _resolve_module_dotpath(self, import_str)"}, {"doc": "Match by file stem only (last resort).", "kind": "method", "line": 207, "name": "_resolve_stem_match", "signature": "def _resolve_stem_match(self, import_str)"}]}, {"id": "readmenator/_rule_gen.py", "kind": "module", "label": "_rule_gen.py", "language": "py", "sha256": "16bae439053d55e3", "symbol_count": 9, "symbols": [{"doc": "Generates suggested linting and security rules from code patterns.\n\nAnalyses the scanned codebase for repeated patterns that suggest\nproject-specific linting rules: bare except clauses, repeated\ntype annotations, common security antipatterns, and naming\nconvention violations. Outputs Semgrep YAML rules to a directory.", "kind": "class", "line": 12, "name": "RuleGenerator", "signature": "class RuleGenerator"}, {"kind": "method", "line": 88, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate suggested rules by scanning code patterns.\n\nArgs:\n    nodes: Scanned file nodes with symbols.\n    content_map: Optional mapping of file paths to their source content\n        for deeper pattern matching.\n\nReturns:\n    List of SuggestedRule instances.", "kind": "method", "line": 92, "name": "generate", "signature": "def generate(self, nodes, content_map)"}, {"doc": "Write suggested rules to Semgrep YAML files in output_dir.\n\nReturns the number of rule files written.", "kind": "method", "line": 120, "name": "write_rules", "signature": "def write_rules(self, rules, output_dir)"}, {"doc": "Group nodes by their language extension.", "kind": "method", "line": 159, "name": "_group_by_language", "signature": "def _group_by_language(self, nodes)"}, {"doc": "Analyze a single language group for rule suggestions.", "kind": "method", "line": 169, "name": "_analyze_language", "signature": "def _analyze_language(self, lang, nodes, content_map)"}, {"doc": "Detect known antipatterns across all files.", "kind": "method", "line": 202, "name": "_detect_antipatterns", "signature": "def _detect_antipatterns(self, nodes, content_map)"}, {"doc": "Infer target language for a built-in antipattern rule.", "kind": "method", "line": 248, "name": "_infer_language_for_rule", "signature": "def _infer_language_for_rule(rule_id)"}, {"doc": "Generate the next rule identifier.", "kind": "method", "line": 258, "name": "_next_rule_id", "signature": "def _next_rule_id(self)"}]}, {"id": "readmenator/_sarif.py", "kind": "module", "label": "_sarif.py", "language": "py", "sha256": "c7489117abc919be", "symbol_count": 5, "symbols": [{"doc": "Exports security findings to the SARIF standard format.\n\nSARIF is an OASIS standard format for static analysis tool output.\nThis exporter produces SARIF v2.1.0 JSON compatible with GitHub\nCode Scanning, VS Code SARIF viewer, and other SARIF consumers.", "kind": "class", "line": 9, "name": "SarifExporter", "signature": "class SarifExporter"}, {"kind": "method", "line": 28, "name": "__init__", "signature": "def __init__(self, privacy_mode)"}, {"doc": "Generate a SARIF v2.1.0 JSON string from security findings.\n\nArgs:\n    findings: List of SecurityFinding instances.\n    project_name: Name of the scanned project for metadata.\n\nReturns:\n    SARIF JSON string.", "kind": "method", "line": 31, "name": "export", "signature": "def export(self, findings, project_name)"}, {"doc": "Build a SARIF reportingDescriptor (rule) object.", "kind": "method", "line": 80, "name": "_build_rule", "signature": "def _build_rule(self, finding)"}, {"doc": "Build a SARIF result object for a single finding.", "kind": "method", "line": 104, "name": "_build_result", "signature": "def _build_result(self, finding, rule_index)"}]}, {"id": "readmenator/_scanner.py", "kind": "module", "label": "_scanner.py", "language": "py", "sha256": "6694f88c25234419", "symbol_count": 13, "symbols": [{"doc": "Recursive directory scanner with security and size guards.\n\nRejects symlinks, enforces file-size and directory-depth limits,\nskips ignored directories, and silently catches parse errors\nso a single misbehaving file never breaks the full scan.\n\nSupports privacy mode (strips snippets and docstrings) and\ngitignore-aware scanning for more accurate project coverage.", "kind": "class", "line": 22, "name": "PolyglotScanner", "signature": "class PolyglotScanner"}, {"doc": "Initialise the scanner with application configuration.\n\nArgs:\n    config: Settings including ignore dirs, size limits, etc.", "kind": "method", "line": 33, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return ``True`` if any path component matches IGNORE_DIRS.", "kind": "method", "line": 42, "name": "_is_ignored", "signature": "def _is_ignored(self, path)"}, {"doc": "Parse .gitignore patterns using regex (no external deps).", "kind": "method", "line": 46, "name": "_load_gitignore", "signature": "def _load_gitignore(self, root)"}, {"doc": "Convert a .gitignore glob pattern to a regex pattern.", "kind": "method", "line": 68, "name": "_gitignore_glob_to_regex", "signature": "def _gitignore_glob_to_regex(pattern)"}, {"doc": "Check if a relative path matches any .gitignore pattern.", "kind": "method", "line": 108, "name": "_is_gitignored", "signature": "def _is_gitignored(self, rel_path)"}, {"doc": "Reject symlinks and files exceeding MAX_FILE_SIZE_MB.", "kind": "method", "line": 117, "name": "_validate_path_security", "signature": "def _validate_path_security(self, path)"}, {"doc": "Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.", "kind": "method", "line": 130, "name": "_check_directory_depth", "signature": "def _check_directory_depth(self, path, root)"}, {"doc": "Extract a file-level docstring from the first lines of a source file.\n\nWalks the first FILE_HEADER_MAX_LINES lines looking for a contiguous\nblock of comments or a shebang followed by comments. Returns the\nconcatenated comment text.\n\nArgs:\n    content: Raw file content as a string.\n\nReturns:\n    Extracted file-level docstring or empty string.", "kind": "method", "line": 138, "name": "_extract_file_doc", "signature": "def _extract_file_doc(self, content)"}, {"doc": "Emit a progress message every PROGRESS_REPORT_BATCH files.\n\nArgs:\n    count: Number of files scanned so far.", "kind": "method", "line": 191, "name": "_emit_progress", "signature": "def _emit_progress(self, count)"}, {"doc": "Walk *root* recursively and produce (nodes, edges) for the graph.\n\nSecurity checks (symlinks, size, depth, ignore dirs) are applied\nper file. Parse failures are silently caught so a single broken\nfile never blocks the rest of the scan.\n\nReturns:\n    A tuple of (list of Node, list of Edge). Edges represent\n    ``imports`` relationships between scanned files.", "kind": "method", "line": 201, "name": "scan", "signature": "def scan(self, root)"}, {"doc": "Scan and also return raw file contents for deeper analysis.\n\nReturns:\n    Tuple of (nodes, edges, content_map) where content_map maps\n    node_id to raw file content.", "kind": "method", "line": 215, "name": "scan_with_content", "signature": "def scan_with_content(self, root)"}, {"doc": "Internal scan implementation returning nodes, edges, and content.", "kind": "method", "line": 226, "name": "_scan_impl", "signature": "def _scan_impl(self, root)"}]}, {"id": "readmenator/_security.py", "kind": "module", "label": "_security.py", "language": "py", "sha256": "4663db73914d1163", "symbol_count": 27, "symbols": [{"doc": "A single security detection rule.\n\nAttributes:\n    rule_id: Unique identifier (e.g. \"PY001\").\n    severity: Severity level (critical, high, medium, low, info).\n    description: Human-readable description of the issue.\n    pattern: Compiled regex to search for.\n    cwe: CWE identifier string.", "kind": "class", "line": 20, "name": "SecurityRule", "signature": "class SecurityRule"}, {"doc": "Pattern-based static security scanner.\n\nMaintains per-language rule sets and walks the target directory\napplying rules to every supported source file. Designed to slot\ninto the readmenator pipeline alongside GraphAnalyzer.", "kind": "class", "line": 38, "name": "SecurityAnalyzer", "signature": "class SecurityAnalyzer"}, {"doc": "Compile multiple patterns into a single case-insensitive regex.", "kind": "method", "line": 203, "name": "_compile", "signature": "def _compile()"}, {"doc": "Return security rules for Python (.py).", "kind": "method", "line": 209, "name": "_python_rules", "signature": "def _python_rules()"}, {"doc": "Return security rules for JavaScript/TypeScript (.js/.ts/.jsx/.tsx).", "kind": "method", "line": 307, "name": "_javascript_rules", "signature": "def _javascript_rules()"}, {"doc": "Return security rules for C/C++ (.c/.cpp/.cc/.cxx/.h/.hpp/.hxx).", "kind": "method", "line": 361, "name": "_c_rules", "signature": "def _c_rules()"}, {"doc": "Return security rules for Java (.java).", "kind": "method", "line": 415, "name": "_java_rules", "signature": "def _java_rules()"}, {"doc": "Return security rules for Go (.go).", "kind": "method", "line": 454, "name": "_go_rules", "signature": "def _go_rules()"}, {"doc": "Return security rules for Ruby (.rb).", "kind": "method", "line": 487, "name": "_ruby_rules", "signature": "def _ruby_rules()"}, {"doc": "Return security rules for PHP (.php).", "kind": "method", "line": 529, "name": "_php_rules", "signature": "def _php_rules()"}, {"doc": "Return security rules for Shell (.sh/.bash/.zsh).", "kind": "method", "line": 590, "name": "_shell_rules", "signature": "def _shell_rules()"}, {"doc": "Return security rules for C# (.cs).", "kind": "method", "line": 620, "name": "_csharp_rules", "signature": "def _csharp_rules()"}, {"doc": "Return security rules for Kotlin (.kt/.kts).", "kind": "method", "line": 659, "name": "_kotlin_rules", "signature": "def _kotlin_rules()"}, {"doc": "Return security rules for Swift (.swift).", "kind": "method", "line": 686, "name": "_swift_rules", "signature": "def _swift_rules()"}, {"doc": "Return security rules for Scala (.scala/.sc).", "kind": "method", "line": 713, "name": "_scala_rules", "signature": "def _scala_rules()"}, {"doc": "Return security rules for Lua (.lua).", "kind": "method", "line": 741, "name": "_lua_rules", "signature": "def _lua_rules()"}, {"doc": "Return security rules for Dart (.dart).", "kind": "method", "line": 765, "name": "_dart_rules", "signature": "def _dart_rules()"}, {"doc": "Return security rules for Rust (.rs).", "kind": "method", "line": 797, "name": "_rust_rules", "signature": "def _rust_rules()"}, {"doc": "Return security rules for Nim (.nim).", "kind": "method", "line": 830, "name": "_nim_rules", "signature": "def _nim_rules()"}, {"doc": "Return security rules for GDScript (.gd).", "kind": "method", "line": 858, "name": "_gdscript_rules", "signature": "def _gdscript_rules()"}, {"doc": "Return security rules for Elixir (.ex/.exs).", "kind": "method", "line": 882, "name": "_elixir_rules", "signature": "def _elixir_rules()"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings including SECURITY_ENABLED and\n        SECURITY_SEVERITY_THRESHOLD.", "kind": "method", "line": 48, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Build the complete per-language rule set.", "kind": "method", "line": 59, "name": "_build_rules", "signature": "def _build_rules()"}, {"doc": "Check if *severity* meets the configured threshold.", "kind": "method", "line": 96, "name": "_meets_threshold", "signature": "def _meets_threshold(self, severity)"}, {"doc": "Walk *root* and return all security findings.\n\nApplies the same security checks as PolyglotScanner (symlinks,\nignore dirs, size limits, depth limits) for consistency.\n\nArgs:\n    root: Project root directory to scan.\n\nReturns:\n    List of SecurityFinding instances, sorted by severity.", "kind": "method", "line": 103, "name": "scan", "signature": "def scan(self, root)"}, {"doc": "Validate path security: reject symlinks and enforce limits.", "kind": "method", "line": 170, "name": "_validate_path", "signature": "def _validate_path(self, path, root)"}, {"doc": "Return a concise summary string of security findings.", "kind": "method", "line": 188, "name": "summary", "signature": "def summary(self, findings)"}]}, {"id": "readmenator/_taint.py", "kind": "module", "label": "_taint.py", "language": "py", "sha256": "19fad0e20d2a1629", "symbol_count": 6, "symbols": [{"doc": "Propagation-based taint analysis over the resolved import graph.\n\nIdentifies files that import known-dangerous modules or functions\n(sources) and traces how that danger propagates through the import\ngraph to files that never directly import the dangerous module\nbut receive taint through transitive dependencies.", "kind": "class", "line": 10, "name": "TaintAnalyzer", "signature": "class TaintAnalyzer"}, {"kind": "method", "line": 71, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run taint propagation analysis on the codebase.\n\nScans all nodes for direct dangerous imports, then propagates\ntaint through the resolved import graph. Returns all discovered\ntaint paths from sources to sinks.", "kind": "method", "line": 75, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges)"}, {"doc": "Find files that directly import known-dangerous modules.", "kind": "method", "line": 134, "name": "_find_direct_sources", "signature": "def _find_direct_sources(self, nodes, edges)"}, {"doc": "BFS propagation from source through the import graph.", "kind": "method", "line": 160, "name": "_propagate", "signature": "def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)"}, {"doc": "Build a forward-directed import graph from resolved edges.", "kind": "method", "line": 211, "name": "_build_forward_graph", "signature": "def _build_forward_graph(nodes, resolved_edges)"}]}, {"id": "readmenator/_watcher.py", "kind": "module", "label": "_watcher.py", "language": "py", "sha256": "239589d6f7746a2a", "symbol_count": 5, "symbols": [{"doc": "Polling-based directory watcher for auto-rebuild on changes.\n\nComputes a combined hash of all tracked files (filenames + sizes)\nand triggers a callback when the hash changes. Uses polling to\navoid external dependencies like watchdog or inotify.", "kind": "class", "line": 21, "name": "DirectoryWatcher", "signature": "class DirectoryWatcher"}, {"doc": "Initialise the watcher for a project root.\n\nArgs:\n    root: Project directory to watch.\n    config: Application configuration.\n    callback: Function called when changes are detected.\n    interval_seconds: Polling interval in seconds.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, root, config, callback, interval_seconds)"}, {"doc": "Compute a quick hash of all tracked files in the project.\n\nUses file paths and sizes (not full content) for speed.\nReturns a hex digest that changes when files are added,\nremoved, or modified.", "kind": "method", "line": 51, "name": "_compute_snapshot", "signature": "def _compute_snapshot(self)"}, {"doc": "Start watching the directory (blocking).", "kind": "method", "line": 80, "name": "start", "signature": "def start(self)"}, {"doc": "Stop watching.", "kind": "method", "line": 97, "name": "stop", "signature": "def stop(self)"}]}, {"id": "readmenator/parsers/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "8291343d44d60a19", "symbol_count": 2, "symbols": [{"kind": "function", "line": 32, "name": "_init_parser_map", "signature": "def _init_parser_map()"}, {"doc": "Factory: return a parser instance for the given file extension.", "kind": "function", "line": 65, "name": "create_parser", "signature": "def create_parser(extension, filename, config)"}]}, {"id": "readmenator/parsers/_assembly.py", "kind": "module", "label": "_assembly.py", "language": "py", "sha256": "3c54c72d2e2c3497", "symbol_count": 2, "symbols": [{"doc": "Parser for assembly (.asm, .s, .S).\n\nExtracts labels at the start of a line (``label:``) as function\nsymbols. This is a best-effort heuristic; local labels and\ndirectives are not always distinguishable.", "kind": "class", "line": 9, "name": "AssemblyParser", "signature": "class AssemblyParser(LanguageParser)"}, {"kind": "method", "line": 17, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_base.py", "kind": "module", "label": "_base.py", "language": "py", "sha256": "edb00b6f40c180b1", "symbol_count": 6, "symbols": [{"doc": "Base class for all language-specific parsers.\n\nSubclasses must implement ``_extract_specifics`` to populate\n``self.symbols`` and ``self.imports``. Common utility methods\n``_extract_docstring`` and ``_extract_signature`` are provided\nfor reuse across all parsers.", "kind": "class", "line": 10, "name": "LanguageParser", "signature": "class LanguageParser"}, {"doc": "Initialise the parser with a file path and application config.\n\nArgs:\n    filename: Relative or absolute path of the source file.\n    config: Application-wide configuration settings.", "kind": "method", "line": 19, "name": "__init__", "signature": "def __init__(self, filename, config)"}, {"doc": "Parse *content* and populate symbol/import lists.\n\nSplits the source into lines, then delegates to the subclass-\nspecific ``_extract_specifics`` logic.", "kind": "method", "line": 34, "name": "parse", "signature": "def parse(self, content)"}, {"doc": "Subclass hook for language-specific symbol extraction.", "kind": "method", "line": 43, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}, {"doc": "Walk backwards from *line_num* to collect preceding comments/docstrings.\n\nSupports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``\ncomment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``\nfrom Config.", "kind": "method", "line": 47, "name": "_extract_docstring", "signature": "def _extract_docstring(self, line_num)"}, {"doc": "Extract a compact signature snippet starting at *match_start*.\n\nScans forward to the opening brace or a fallback length,\nthen truncates to 100 characters for display.", "kind": "method", "line": 89, "name": "_extract_signature", "signature": "def _extract_signature(self, content, match_start, pattern)"}]}, {"id": "readmenator/parsers/_c.py", "kind": "module", "label": "_c.py", "language": "py", "sha256": "c7df3a6543a025c6", "symbol_count": 2, "symbols": [{"doc": "Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).\n\nExtracts includes, structs, classes, functions, and preprocessor\nmacros using regex heuristics tuned to C-family syntax.", "kind": "class", "line": 9, "name": "CParser", "signature": "class CParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_csharp.py", "kind": "module", "label": "_csharp.py", "language": "py", "sha256": "cfaa6ea3cf4296c4", "symbol_count": 2, "symbols": [{"doc": "Parser for C# (.cs).\n\nExtracts ``using`` directives, class/struct/interface/record\ndeclarations, and methods with access modifiers.", "kind": "class", "line": 9, "name": "CSharpParser", "signature": "class CSharpParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_dart.py", "kind": "module", "label": "_dart.py", "language": "py", "sha256": "4b087dfaed083323", "symbol_count": 2, "symbols": [{"doc": "Parser for Dart (.dart).\n\nExtracts import statements, class declarations (with extends),\nand top-level or method function declarations by return type.", "kind": "class", "line": 9, "name": "DartParser", "signature": "class DartParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_elixir.py", "kind": "module", "label": "_elixir.py", "language": "py", "sha256": "645a1d929186f850", "symbol_count": 2, "symbols": [{"doc": "Parser for Elixir (.ex, .exs).\n\nExtracts ``import``/``alias``/``require``/``use`` directives,\nmodule definitions, and named function definitions.", "kind": "class", "line": 9, "name": "ElixirParser", "signature": "class ElixirParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_gdscript.py", "kind": "module", "label": "_gdscript.py", "language": "py", "sha256": "27a50d6bc58f772f", "symbol_count": 2, "symbols": [{"doc": "Parser for Godot GDScript (.gd).\n\nExtracts ``extends`` / ``class_name`` directives and ``func``\nmethod declarations.", "kind": "class", "line": 9, "name": "GDScriptParser", "signature": "class GDScriptParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_go.py", "kind": "module", "label": "_go.py", "language": "py", "sha256": "2e55e35316be76bb", "symbol_count": 2, "symbols": [{"doc": "Parser for Go (.go).\n\nExtracts import blocks or single import statements, exported\nfunctions (including methods), and type definitions (struct/interface).", "kind": "class", "line": 9, "name": "GoParser", "signature": "class GoParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_java.py", "kind": "module", "label": "_java.py", "language": "py", "sha256": "25826d29281fc7a4", "symbol_count": 2, "symbols": [{"doc": "Parser for Java (.java).\n\nExtracts import statements, class and interface declarations,\nand methods complete with access modifiers and type signatures.", "kind": "class", "line": 9, "name": "JavaParser", "signature": "class JavaParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_javascript.py", "kind": "module", "label": "_javascript.py", "language": "py", "sha256": "a024f05bb3db8318", "symbol_count": 2, "symbols": [{"doc": "Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).\n\nExtracts ES module imports, CommonJS ``require`` calls, function\ndeclarations, arrow-function variables, and class definitions\n(including inheritance).", "kind": "class", "line": 9, "name": "JavaScriptParser", "signature": "class JavaScriptParser(LanguageParser)"}, {"kind": "method", "line": 17, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_kotlin.py", "kind": "module", "label": "_kotlin.py", "language": "py", "sha256": "cd1af4e9d8c2f23b", "symbol_count": 2, "symbols": [{"doc": "Parser for Kotlin (.kt, .kts).\n\nExtracts ``import`` statements, class/object/interface/data class\ndeclarations, and function definitions.", "kind": "class", "line": 9, "name": "KotlinParser", "signature": "class KotlinParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_lua.py", "kind": "module", "label": "_lua.py", "language": "py", "sha256": "df4d62ca2b4b2387", "symbol_count": 2, "symbols": [{"doc": "Parser for Lua (.lua).\n\nExtracts ``require`` imports, function declarations (named and\ntable-based), and module returns.", "kind": "class", "line": 9, "name": "LuaParser", "signature": "class LuaParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_nim.py", "kind": "module", "label": "_nim.py", "language": "py", "sha256": "fde950f2aaa92bb2", "symbol_count": 2, "symbols": [{"doc": "Parser for Nim (.nim).\n\nExtracts ``import`` statements, ``proc`` / ``func`` / ``method``\ndeclarations, and ``type`` definitions.", "kind": "class", "line": 9, "name": "NimParser", "signature": "class NimParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_php.py", "kind": "module", "label": "_php.py", "language": "py", "sha256": "30f0aa4f3d9573a9", "symbol_count": 2, "symbols": [{"doc": "Parser for PHP (.php).\n\nExtracts ``use/require/include`` (including ``_once`` variants),\nfunction declarations, and class declarations.", "kind": "class", "line": 9, "name": "PHPParser", "signature": "class PHPParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_python.py", "kind": "module", "label": "_python.py", "language": "py", "sha256": "b7a85e67d2c72a37", "symbol_count": 2, "symbols": [{"doc": "Parser for Python (.py) using the native ``ast`` module.\n\nExtracts imports, functions (including async), and class\ndefinitions with docstrings via ``ast.get_docstring``.", "kind": "class", "line": 10, "name": "PythonParser", "signature": "class PythonParser(LanguageParser)"}, {"kind": "method", "line": 17, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_ruby.py", "kind": "module", "label": "_ruby.py", "language": "py", "sha256": "f471ea9104217c63", "symbol_count": 2, "symbols": [{"doc": "Parser for Ruby (.rb).\n\nExtracts ``require`` / ``require_relative`` imports, class and\nmodule definitions with inheritance, and method definitions.", "kind": "class", "line": 9, "name": "RubyParser", "signature": "class RubyParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_rust.py", "kind": "module", "label": "_rust.py", "language": "py", "sha256": "46f030f5e898dd81", "symbol_count": 2, "symbols": [{"doc": "Parser for Rust (.rs).\n\nExtracts ``use`` imports, public and private functions,\nstructs, traits, and enums.", "kind": "class", "line": 9, "name": "RustParser", "signature": "class RustParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_scala.py", "kind": "module", "label": "_scala.py", "language": "py", "sha256": "386522f137dcc74a", "symbol_count": 2, "symbols": [{"doc": "Parser for Scala (.scala).\n\nExtracts ``import`` statements, class/object/trait declarations,\nand method definitions.", "kind": "class", "line": 9, "name": "ScalaParser", "signature": "class ScalaParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_shell.py", "kind": "module", "label": "_shell.py", "language": "py", "sha256": "18e886e8af9eca07", "symbol_count": 2, "symbols": [{"doc": "Parser for shell scripts (.sh, .bash, .zsh).\n\nExtracts function declarations in both POSIX (``name() {``)\nand ``function`` keyword syntax.", "kind": "class", "line": 9, "name": "ShellParser", "signature": "class ShellParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_swift.py", "kind": "module", "label": "_swift.py", "language": "py", "sha256": "865dacef6bb447dc", "symbol_count": 2, "symbols": [{"doc": "Parser for Swift (.swift).\n\nExtracts ``import`` statements, class/struct/enum/protocol\ndeclarations with inheritance, and function definitions.", "kind": "class", "line": 9, "name": "SwiftParser", "signature": "class SwiftParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator.py", "kind": "module", "label": "readmenator.py", "language": "py", "sha256": "beabccf3e6d231db", "symbol_count": 0, "symbols": []}, {"id": "readmenator_orchestrator.py", "kind": "module", "label": "readmenator_orchestrator.py", "language": "py", "sha256": "250362479291af30", "symbol_count": 34, "symbols": [{"kind": "class", "line": 21, "name": "Config", "signature": "class Config"}, {"kind": "method", "line": 43, "name": "_validate_repo_name", "signature": "def _validate_repo_name(name)"}, {"kind": "method", "line": 49, "name": "_validate_branch_name", "signature": "def _validate_branch_name(name)"}, {"kind": "method", "line": 55, "name": "_safe_env", "signature": "def _safe_env()"}, {"kind": "class", "line": 70, "name": "GitHubClient", "signature": "class GitHubClient"}, {"kind": "class", "line": 184, "name": "RepositoryProcessor", "signature": "class RepositoryProcessor"}, {"kind": "class", "line": 326, "name": "Orchestrator", "signature": "class Orchestrator"}, {"kind": "class", "line": 381, "name": "TestOrchestrator", "signature": "class TestOrchestrator(TestCase)"}, {"kind": "method", "line": 422, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 439, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 71, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 76, "name": "_resolve_user", "signature": "def _resolve_user(self)"}, {"kind": "method", "line": 97, "name": "_setup_git_auth", "signature": "def _setup_git_auth(self)"}, {"kind": "method", "line": 111, "name": "list_repos", "signature": "def list_repos(self)"}, {"kind": "method", "line": 123, "name": "close_existing_prs", "signature": "def close_existing_prs(self, repo)"}, {"kind": "method", "line": 151, "name": "delete_remote_branch", "signature": "def delete_remote_branch(self, repo)"}, {"kind": "method", "line": 163, "name": "create_pr", "signature": "def create_pr(self, repo, default_branch, timestamp)"}, {"kind": "method", "line": 185, "name": "__init__", "signature": "def __init__(self, config, github_client)"}, {"kind": "method", "line": 189, "name": "process", "signature": "def process(self, repo)"}, {"kind": "method", "line": 218, "name": "_get_default_branch", "signature": "def _get_default_branch(self, repo)"}, {"kind": "method", "line": 234, "name": "_clone_repository", "signature": "def _clone_repository(self, repo)"}, {"kind": "method", "line": 250, "name": "_run_readmenator", "signature": "def _run_readmenator(self, repo_dir)"}, {"kind": "method", "line": 271, "name": "_copy_to_docs_dir", "signature": "def _copy_to_docs_dir(repo_dir, generated_file)"}, {"kind": "method", "line": 277, "name": "_commit_and_push", "signature": "def _commit_and_push(self, repo_dir, repo)"}, {"kind": "method", "line": 321, "name": "_cleanup_temp_dir", "signature": "def _cleanup_temp_dir(temp_dir)"}, {"kind": "method", "line": 327, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 332, "name": "run", "signature": "def run(self, dry_run, only_repo)"}, {"kind": "method", "line": 382, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 386, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 389, "name": "test_config_immutability", "signature": "def test_config_immutability(self)"}, {"kind": "method", "line": 393, "name": "test_config_defaults", "signature": "def test_config_defaults(self)"}, {"kind": "method", "line": 399, "name": "test_skip_repos_logic", "signature": "def test_skip_repos_logic(self)"}, {"kind": "method", "line": 403, "name": "test_repo_name_validation", "signature": "def test_repo_name_validation(self)"}, {"kind": "method", "line": 413, "name": "test_branch_name_validation", "signature": "def test_branch_name_validation(self)"}]}, {"id": "tests/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "f813c53b4d1cc74f", "symbol_count": 0, "symbols": []}, {"id": "tests/test_analyzer.py", "kind": "module", "label": "test_analyzer.py", "language": "py", "sha256": "0f8e3409a64ff96e", "symbol_count": 12, "symbols": [{"doc": "Contract: GraphAnalyzer provides graph intelligence.", "kind": "class", "line": 16, "name": "TestGraphAnalyzerContract", "signature": "class TestGraphAnalyzerContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 26, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt, rel)"}, {"kind": "method", "line": 29, "name": "test_analyze_empty_graph_returns_empty_result", "signature": "def test_analyze_empty_graph_returns_empty_result(self)"}, {"kind": "method", "line": 34, "name": "test_analyze_detects_communities_for_connected_graph", "signature": "def test_analyze_detects_communities_for_connected_graph(self)"}, {"kind": "method", "line": 48, "name": "test_analyze_computes_god_nodes", "signature": "def test_analyze_computes_god_nodes(self)"}, {"kind": "method", "line": 64, "name": "test_analyze_finds_surprising_connections", "signature": "def test_analyze_finds_surprising_connections(self)"}, {"kind": "method", "line": 81, "name": "test_analyze_generates_questions", "signature": "def test_analyze_generates_questions(self)"}, {"kind": "method", "line": 92, "name": "test_community_cohesion_is_between_zero_and_one", "signature": "def test_community_cohesion_is_between_zero_and_one(self)"}, {"kind": "method", "line": 107, "name": "test_isolated_nodes_do_not_form_communities", "signature": "def test_isolated_nodes_do_not_form_communities(self)"}, {"kind": "method", "line": 116, "name": "test_analyze_with_resolved_edges_counts_them", "signature": "def test_analyze_with_resolved_edges_counts_them(self)"}]}, {"id": "tests/test_cache.py", "kind": "module", "label": "test_cache.py", "language": "py", "sha256": "8f87c6228fec0800", "symbol_count": 15, "symbols": [{"doc": "Contract: FileCache provides SHA256-based incremental scan support.", "kind": "class", "line": 18, "name": "TestFileCacheContract", "signature": "class TestFileCacheContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 26, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 30, "name": "_write", "signature": "def _write(self, rel_path, content)"}, {"kind": "method", "line": 36, "name": "test_compute_hash_returns_hex_string", "signature": "def test_compute_hash_returns_hex_string(self)"}, {"kind": "method", "line": 42, "name": "test_different_content_produces_different_hash", "signature": "def test_different_content_produces_different_hash(self)"}, {"kind": "method", "line": 49, "name": "test_same_content_produces_same_hash", "signature": "def test_same_content_produces_same_hash(self)"}, {"kind": "method", "line": 56, "name": "test_load_returns_empty_dict_when_no_cache", "signature": "def test_load_returns_empty_dict_when_no_cache(self)"}, {"kind": "method", "line": 60, "name": "test_save_and_load_roundtrip", "signature": "def test_save_and_load_roundtrip(self)"}, {"kind": "method", "line": 66, "name": "test_find_changed_detects_new_files", "signature": "def test_find_changed_detects_new_files(self)"}, {"kind": "method", "line": 71, "name": "test_find_changed_detects_modified_files", "signature": "def test_find_changed_detects_modified_files(self)"}, {"kind": "method", "line": 78, "name": "test_find_changed_skips_unchanged_files", "signature": "def test_find_changed_skips_unchanged_files(self)"}, {"kind": "method", "line": 85, "name": "test_prune_deleted_removes_ghost_entries", "signature": "def test_prune_deleted_removes_ghost_entries(self)"}, {"kind": "method", "line": 92, "name": "test_compute_hashes_batch", "signature": "def test_compute_hashes_batch(self)"}, {"kind": "method", "line": 100, "name": "test_nonexistent_file_returns_empty_hash", "signature": "def test_nonexistent_file_returns_empty_hash(self)"}]}, {"id": "tests/test_config.py", "kind": "module", "label": "test_config.py", "language": "py", "sha256": "0123e0442447e271", "symbol_count": 6, "symbols": [{"kind": "class", "line": 7, "name": "TestConfigContract", "signature": "class TestConfigContract(TestCase)"}, {"kind": "method", "line": 8, "name": "test_config_is_immutable", "signature": "def test_config_is_immutable(self)"}, {"kind": "method", "line": 13, "name": "test_config_defaults_are_sane", "signature": "def test_config_defaults_are_sane(self)"}, {"kind": "method", "line": 24, "name": "test_ignore_dirs_are_comprehensive", "signature": "def test_ignore_dirs_are_comprehensive(self)"}, {"kind": "method", "line": 30, "name": "test_plural_map_covers_all_symbol_types", "signature": "def test_plural_map_covers_all_symbol_types(self)"}, {"kind": "method", "line": 41, "name": "test_supported_extensions_no_duplicates", "signature": "def test_supported_extensions_no_duplicates(self)"}]}, {"id": "tests/test_cpg.py", "kind": "module", "label": "test_cpg.py", "language": "py", "sha256": "f71374c5b5964fc8", "symbol_count": 11, "symbols": [{"doc": "Contract: CodePropertyGraph generates valid JSON-LD CPG output.", "kind": "class", "line": 11, "name": "TestCodePropertyGraphContract", "signature": "class TestCodePropertyGraphContract(TestCase)"}, {"kind": "method", "line": 14, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 18, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 21, "name": "_make_sym", "signature": "def _make_sym(self, name, kind, line)"}, {"kind": "method", "line": 24, "name": "test_generate_returns_valid_json", "signature": "def test_generate_returns_valid_json(self)"}, {"kind": "method", "line": 33, "name": "test_generate_includes_node_data", "signature": "def test_generate_includes_node_data(self)"}, {"kind": "method", "line": 49, "name": "test_generate_includes_edges", "signature": "def test_generate_includes_edges(self)"}, {"kind": "method", "line": 61, "name": "test_generate_includes_metadata", "signature": "def test_generate_includes_metadata(self)"}, {"kind": "method", "line": 71, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 89, "name": "test_sha256_hash_included", "signature": "def test_sha256_hash_included(self)"}, {"kind": "method", "line": 96, "name": "test_empty_graph_returns_valid_json", "signature": "def test_empty_graph_returns_valid_json(self)"}]}, {"id": "tests/test_documentation.py", "kind": "module", "label": "test_documentation.py", "language": "py", "sha256": "3fcd3f8ce2cf70eb", "symbol_count": 24, "symbols": [{"kind": "class", "line": 17, "name": "TestDocumentationGeneratorContract", "signature": "class TestDocumentationGeneratorContract(TestCase)"}, {"kind": "method", "line": 18, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 22, "name": "test_contains_header", "signature": "def test_contains_header(self)"}, {"kind": "method", "line": 26, "name": "test_contains_metadata_line", "signature": "def test_contains_metadata_line(self)"}, {"kind": "method", "line": 32, "name": "test_contains_mermaid_block", "signature": "def test_contains_mermaid_block(self)"}, {"kind": "method", "line": 37, "name": "test_contains_architecture_reference", "signature": "def test_contains_architecture_reference(self)"}, {"kind": "method", "line": 41, "name": "test_contains_cpg_block", "signature": "def test_contains_cpg_block(self)"}, {"kind": "method", "line": 46, "name": "test_contains_statistics_dashboard", "signature": "def test_contains_statistics_dashboard(self)"}, {"kind": "method", "line": 51, "name": "test_groups_files_by_language", "signature": "def test_groups_files_by_language(self)"}, {"kind": "method", "line": 70, "name": "test_lists_symbols_under_file", "signature": "def test_lists_symbols_under_file(self)"}, {"kind": "method", "line": 83, "name": "test_class_symbol_is_pluralized_correctly", "signature": "def test_class_symbol_is_pluralized_correctly(self)"}, {"kind": "method", "line": 97, "name": "test_function_pluralization", "signature": "def test_function_pluralization(self)"}, {"kind": "method", "line": 109, "name": "test_method_pluralization", "signature": "def test_method_pluralization(self)"}, {"kind": "method", "line": 121, "name": "test_shows_no_symbols_for_empty_files", "signature": "def test_shows_no_symbols_for_empty_files(self)"}, {"kind": "method", "line": 132, "name": "test_includes_file_path", "signature": "def test_includes_file_path(self)"}, {"kind": "method", "line": 143, "name": "test_docstring_in_output", "signature": "def test_docstring_in_output(self)"}, {"kind": "method", "line": 155, "name": "test_truncation_note_when_limited", "signature": "def test_truncation_note_when_limited(self)"}, {"kind": "method", "line": 165, "name": "test_taint_propagation_section_present", "signature": "def test_taint_propagation_section_present(self)"}, {"kind": "method", "line": 185, "name": "test_hotspot_section_present", "signature": "def test_hotspot_section_present(self)"}, {"kind": "method", "line": 203, "name": "test_no_taint_section_when_empty", "signature": "def test_no_taint_section_when_empty(self)"}, {"kind": "method", "line": 207, "name": "test_no_hotspot_section_when_empty", "signature": "def test_no_hotspot_section_when_empty(self)"}, {"kind": "method", "line": 211, "name": "test_cpg_block_disabled_via_config", "signature": "def test_cpg_block_disabled_via_config(self)"}, {"kind": "method", "line": 217, "name": "test_architectural_layers_section", "signature": "def test_architectural_layers_section(self)"}, {"kind": "method", "line": 229, "name": "test_security_findings_section", "signature": "def test_security_findings_section(self)"}]}, {"id": "tests/test_exporter.py", "kind": "module", "label": "test_exporter.py", "language": "py", "sha256": "b70cde45a0105c5f", "symbol_count": 15, "symbols": [{"doc": "Contract: GraphExporter produces valid JSON, HTML, and SVG outputs.", "kind": "class", "line": 23, "name": "TestGraphExporterContract", "signature": "class TestGraphExporterContract(TestCase)"}, {"kind": "method", "line": 26, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 30, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang, symbols)"}, {"kind": "method", "line": 42, "name": "_make_sym", "signature": "def _make_sym(self, name, kind, line)"}, {"kind": "method", "line": 47, "name": "test_to_json_produces_valid_json", "signature": "def test_to_json_produces_valid_json(self)"}, {"kind": "method", "line": 56, "name": "test_to_json_includes_symbol_data", "signature": "def test_to_json_includes_symbol_data(self)"}, {"kind": "method", "line": 65, "name": "test_to_json_includes_metadata", "signature": "def test_to_json_includes_metadata(self)"}, {"kind": "method", "line": 76, "name": "test_to_json_includes_analysis_metadata", "signature": "def test_to_json_includes_analysis_metadata(self)"}, {"kind": "method", "line": 101, "name": "test_to_html_produces_standalone_page", "signature": "def test_to_html_produces_standalone_page(self)"}, {"kind": "method", "line": 109, "name": "test_to_html_includes_node_data", "signature": "def test_to_html_includes_node_data(self)"}, {"kind": "method", "line": 116, "name": "test_to_html_includes_community_legend_when_analysis", "signature": "def test_to_html_includes_community_legend_when_analysis(self)"}, {"kind": "method", "line": 138, "name": "test_to_svg_produces_svg_string", "signature": "def test_to_svg_produces_svg_string(self)"}, {"kind": "method", "line": 145, "name": "test_to_svg_render_truncation_for_large_graph", "signature": "def test_to_svg_render_truncation_for_large_graph(self)"}, {"kind": "method", "line": 154, "name": "test_to_svg_includes_readmenator_title", "signature": "def test_to_svg_includes_readmenator_title(self)"}, {"kind": "method", "line": 160, "name": "test_to_json_handles_resolved_edges", "signature": "def test_to_json_handles_resolved_edges(self)"}]}, {"id": "tests/test_hotspots.py", "kind": "module", "label": "test_hotspots.py", "language": "py", "sha256": "2f31e5fb128e17d4", "symbol_count": 11, "symbols": [{"doc": "Contract: HotspotAnalyzer detects hotspots, cycles, and change impact.", "kind": "class", "line": 10, "name": "TestHotspotAnalyzerContract", "signature": "class TestHotspotAnalyzerContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label, sym_count)"}, {"kind": "method", "line": 29, "name": "test_empty_graph_returns_empty_hotspots", "signature": "def test_empty_graph_returns_empty_hotspots(self)"}, {"kind": "method", "line": 33, "name": "test_hotspots_rank_by_combined_score", "signature": "def test_hotspots_rank_by_combined_score(self)"}, {"kind": "method", "line": 43, "name": "test_hotspot_includes_scores", "signature": "def test_hotspot_includes_scores(self)"}, {"kind": "method", "line": 53, "name": "test_no_cycles_in_acyclic_graph", "signature": "def test_no_cycles_in_acyclic_graph(self)"}, {"kind": "method", "line": 66, "name": "test_detects_simple_cycle", "signature": "def test_detects_simple_cycle(self)"}, {"kind": "method", "line": 79, "name": "test_change_impact_ranks_by_total_impact", "signature": "def test_change_impact_ranks_by_total_impact(self)"}, {"kind": "method", "line": 94, "name": "test_change_impact_no_edges", "signature": "def test_change_impact_no_edges(self)"}, {"kind": "method", "line": 100, "name": "test_hotspot_weights_from_config", "signature": "def test_hotspot_weights_from_config(self)"}]}, {"id": "tests/test_integration.py", "kind": "module", "label": "test_integration.py", "language": "py", "sha256": "fa1c42eb78225f90", "symbol_count": 16, "symbols": [{"kind": "class", "line": 9, "name": "TestEndToEndContract", "signature": "class TestEndToEndContract(TestCase)"}, {"kind": "method", "line": 10, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 15, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 19, "name": "_write", "signature": "def _write(self, path, content)"}, {"kind": "method", "line": 24, "name": "test_full_pipeline_generates_knowledge_base", "signature": "def test_full_pipeline_generates_knowledge_base(self)"}, {"kind": "method", "line": 40, "name": "test_knowledge_base_contains_mermaid", "signature": "def test_knowledge_base_contains_mermaid(self)"}, {"kind": "method", "line": 48, "name": "test_query_subcommand_works", "signature": "def test_query_subcommand_works(self)"}, {"kind": "method", "line": 53, "name": "test_explain_subcommand_works", "signature": "def test_explain_subcommand_works(self)"}, {"kind": "method", "line": 59, "name": "test_path_subcommand_works", "signature": "def test_path_subcommand_works(self)"}, {"kind": "method", "line": 65, "name": "test_summary_works", "signature": "def test_summary_works(self)"}, {"kind": "method", "line": 71, "name": "test_rebuild", "signature": "def test_rebuild(self)"}, {"kind": "method", "line": 81, "name": "test_knowledge_base_contains_cpg", "signature": "def test_knowledge_base_contains_cpg(self)"}, {"kind": "method", "line": 89, "name": "test_knowledge_base_contains_statistics_dashboard", "signature": "def test_knowledge_base_contains_statistics_dashboard(self)"}, {"kind": "method", "line": 98, "name": "test_audit_deep_returns_analysis", "signature": "def test_audit_deep_returns_analysis(self)"}, {"kind": "method", "line": 105, "name": "test_privacy_mode_works", "signature": "def test_privacy_mode_works(self)"}, {"kind": "method", "line": 114, "name": "test_export_sarif_produces_file", "signature": "def test_export_sarif_produces_file(self)"}]}, {"id": "tests/test_layer_rules.py", "kind": "module", "label": "test_layer_rules.py", "language": "py", "sha256": "d530692da5fb3cd6", "symbol_count": 13, "symbols": [{"doc": "Contract: LayerRuleEngine detects architectural layer violations.", "kind": "class", "line": 10, "name": "TestLayerRuleEngineContract", "signature": "class TestLayerRuleEngineContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label)"}, {"kind": "method", "line": 20, "name": "test_empty_graph_returns_empty_violations", "signature": "def test_empty_graph_returns_empty_violations(self)"}, {"kind": "method", "line": 24, "name": "test_no_layers_returns_empty_violations", "signature": "def test_no_layers_returns_empty_violations(self)"}, {"kind": "method", "line": 29, "name": "test_same_layer_no_violation", "signature": "def test_same_layer_no_violation(self)"}, {"kind": "method", "line": 36, "name": "test_forbidden_edge_detected", "signature": "def test_forbidden_edge_detected(self)"}, {"kind": "method", "line": 46, "name": "test_allowed_testing_edges_no_violation", "signature": "def test_allowed_testing_edges_no_violation(self)"}, {"kind": "method", "line": 57, "name": "test_multiple_violations", "signature": "def test_multiple_violations(self)"}, {"kind": "method", "line": 75, "name": "test_utility_layer_ignored", "signature": "def test_utility_layer_ignored(self)"}, {"kind": "method", "line": 82, "name": "test_violation_summary", "signature": "def test_violation_summary(self)"}, {"kind": "method", "line": 104, "name": "test_resolved_edges_also_checked", "signature": "def test_resolved_edges_also_checked(self)"}, {"kind": "method", "line": 115, "name": "test_presentation_to_data_access_forbidden", "signature": "def test_presentation_to_data_access_forbidden(self)"}]}, {"id": "tests/test_mermaid.py", "kind": "module", "label": "test_mermaid.py", "language": "py", "sha256": "447a55c490312fe7", "symbol_count": 11, "symbols": [{"kind": "class", "line": 7, "name": "TestMermaidRendererContract", "signature": "class TestMermaidRendererContract(TestCase)"}, {"kind": "method", "line": 8, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 11, "name": "test_renders_graph_header", "signature": "def test_renders_graph_header(self)"}, {"kind": "method", "line": 19, "name": "test_renders_module_node", "signature": "def test_renders_module_node(self)"}, {"kind": "method", "line": 27, "name": "test_renders_symbol_subnodes", "signature": "def test_renders_symbol_subnodes(self)"}, {"kind": "method", "line": 36, "name": "test_class_symbol_gets_cls_style", "signature": "def test_class_symbol_gets_cls_style(self)"}, {"kind": "method", "line": 45, "name": "test_function_symbol_gets_fn_style", "signature": "def test_function_symbol_gets_fn_style(self)"}, {"kind": "method", "line": 54, "name": "test_external_import_edge_is_dashed", "signature": "def test_external_import_edge_is_dashed(self)"}, {"kind": "method", "line": 62, "name": "test_truncation_when_over_limit", "signature": "def test_truncation_when_over_limit(self)"}, {"kind": "method", "line": 72, "name": "test_limits_symbols_to_five_per_node", "signature": "def test_limits_symbols_to_five_per_node(self)"}, {"kind": "method", "line": 82, "name": "test_handles_special_characters_in_ids", "signature": "def test_handles_special_characters_in_ids(self)"}]}, {"id": "tests/test_models.py", "kind": "module", "label": "test_models.py", "language": "py", "sha256": "af0df48f490c3633", "symbol_count": 11, "symbols": [{"kind": "class", "line": 6, "name": "TestSymbolContract", "signature": "class TestSymbolContract(TestCase)"}, {"kind": "class", "line": 20, "name": "TestNodeContract", "signature": "class TestNodeContract(TestCase)"}, {"kind": "class", "line": 48, "name": "TestEdgeContract", "signature": "class TestEdgeContract(TestCase)"}, {"kind": "class", "line": 56, "name": "TestPluralizeContract", "signature": "class TestPluralizeContract(TestCase)"}, {"kind": "method", "line": 7, "name": "test_symbol_creation", "signature": "def test_symbol_creation(self)"}, {"kind": "method", "line": 15, "name": "test_symbol_with_signature", "signature": "def test_symbol_with_signature(self)"}, {"kind": "method", "line": 21, "name": "test_node_creation", "signature": "def test_node_creation(self)"}, {"kind": "method", "line": 35, "name": "test_node_with_symbols", "signature": "def test_node_with_symbols(self)"}, {"kind": "method", "line": 49, "name": "test_edge_creation", "signature": "def test_edge_creation(self)"}, {"kind": "method", "line": 57, "name": "test_pluralize_class", "signature": "def test_pluralize_class(self)"}, {"kind": "method", "line": 62, "name": "test_pluralize_unknown_appends_s", "signature": "def test_pluralize_unknown_appends_s(self)"}]}, {"id": "tests/test_parsers.py", "kind": "module", "label": "test_parsers.py", "language": "py", "sha256": "22219731d5514573", "symbol_count": 84, "symbols": [{"kind": "class", "line": 22, "name": "TestCParserContract", "signature": "class TestCParserContract(TestCase)"}, {"kind": "class", "line": 72, "name": "TestPythonParserContract", "signature": "class TestPythonParserContract(TestCase)"}, {"kind": "class", "line": 141, "name": "TestGoParserContract", "signature": "class TestGoParserContract(TestCase)"}, {"kind": "class", "line": 184, "name": "TestRustParserContract", "signature": "class TestRustParserContract(TestCase)"}, {"kind": "class", "line": 222, "name": "TestJavaScriptParserContract", "signature": "class TestJavaScriptParserContract(TestCase)"}, {"kind": "class", "line": 261, "name": "TestJavaParserContract", "signature": "class TestJavaParserContract(TestCase)"}, {"kind": "class", "line": 293, "name": "TestCSharpParserContract", "signature": "class TestCSharpParserContract(TestCase)"}, {"kind": "class", "line": 326, "name": "TestShellParserContract", "signature": "class TestShellParserContract(TestCase)"}, {"kind": "class", "line": 345, "name": "TestPHPParserContract", "signature": "class TestPHPParserContract(TestCase)"}, {"kind": "class", "line": 371, "name": "TestDartParserContract", "signature": "class TestDartParserContract(TestCase)"}, {"kind": "class", "line": 396, "name": "TestGDScriptParserContract", "signature": "class TestGDScriptParserContract(TestCase)"}, {"kind": "class", "line": 414, "name": "TestNimParserContract", "signature": "class TestNimParserContract(TestCase)"}, {"kind": "class", "line": 440, "name": "TestAssemblyParserContract", "signature": "class TestAssemblyParserContract(TestCase)"}, {"kind": "class", "line": 460, "name": "TestParserFactoryContract", "signature": "class TestParserFactoryContract(TestCase)"}, {"kind": "method", "line": 23, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 26, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 33, "name": "test_extracts_struct", "signature": "def test_extracts_struct(self)"}, {"kind": "method", "line": 40, "name": "test_extracts_include", "signature": "def test_extracts_include(self)"}, {"kind": "method", "line": 47, "name": "test_extracts_define", "signature": "def test_extracts_define(self)"}, {"kind": "method", "line": 54, "name": "test_skips_reserved_words", "signature": "def test_skips_reserved_words(self)"}, {"kind": "method", "line": 64, "name": "test_class_with_inheritance", "signature": "def test_class_with_inheritance(self)"}, {"kind": "method", "line": 73, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 76, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 83, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 90, "name": "test_extracts_imports", "signature": "def test_extracts_imports(self)"}, {"kind": "method", "line": 98, "name": "test_extracts_async_function", "signature": "def test_extracts_async_function(self)"}, {"kind": "method", "line": 105, "name": "test_handles_syntax_error_gracefully", "signature": "def test_handles_syntax_error_gracefully(self)"}, {"kind": "method", "line": 111, "name": "test_suppresses_syntax_warnings", "signature": "def test_suppresses_syntax_warnings(self)"}, {"kind": "method", "line": 123, "name": "test_extracts_signature_with_params", "signature": "def test_extracts_signature_with_params(self)"}, {"kind": "method", "line": 131, "name": "test_extracts_class_with_bases", "signature": "def test_extracts_class_with_bases(self)"}, {"kind": "method", "line": 142, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 145, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 152, "name": "test_extracts_method_receiver", "signature": "def test_extracts_method_receiver(self)"}, {"kind": "method", "line": 159, "name": "test_extracts_import_block", "signature": "def test_extracts_import_block(self)"}, {"kind": "method", "line": 166, "name": "test_extracts_single_import", "signature": "def test_extracts_single_import(self)"}, {"kind": "method", "line": 172, "name": "test_extracts_struct_and_interface", "signature": "def test_extracts_struct_and_interface(self)"}, {"kind": "method", "line": 185, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 188, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 195, "name": "test_extracts_pub_function", "signature": "def test_extracts_pub_function(self)"}, {"kind": "method", "line": 202, "name": "test_extracts_struct_and_trait_and_enum", "signature": "def test_extracts_struct_and_trait_and_enum(self)"}, {"kind": "method", "line": 215, "name": "test_extracts_use", "signature": "def test_extracts_use(self)"}, {"kind": "method", "line": 223, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 226, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 233, "name": "test_extracts_arrow_function", "signature": "def test_extracts_arrow_function(self)"}, {"kind": "method", "line": 240, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 247, "name": "test_extracts_import_and_require", "signature": "def test_extracts_import_and_require(self)"}, {"kind": "method", "line": 254, "name": "test_skips_reserved_words", "signature": "def test_skips_reserved_words(self)"}, {"kind": "method", "line": 262, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 265, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 272, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 279, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 285, "name": "test_abstract_class", "signature": "def test_abstract_class(self)"}, {"kind": "method", "line": 294, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 297, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 304, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 311, "name": "test_extracts_using", "signature": "def test_extracts_using(self)"}, {"kind": "method", "line": 317, "name": "test_record_and_interface", "signature": "def test_record_and_interface(self)"}, {"kind": "method", "line": 327, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 330, "name": "test_extracts_function_with_parentheses", "signature": "def test_extracts_function_with_parentheses(self)"}, {"kind": "method", "line": 337, "name": "test_extracts_function_keyword", "signature": "def test_extracts_function_keyword(self)"}, {"kind": "method", "line": 346, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 349, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 356, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 363, "name": "test_extracts_use_and_require", "signature": "def test_extracts_use_and_require(self)"}, {"kind": "method", "line": 372, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 375, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 382, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 389, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 397, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 400, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 407, "name": "test_extracts_extends", "signature": "def test_extracts_extends(self)"}, {"kind": "method", "line": 415, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 418, "name": "test_extracts_proc", "signature": "def test_extracts_proc(self)"}, {"kind": "method", "line": 425, "name": "test_extracts_type", "signature": "def test_extracts_type(self)"}, {"kind": "method", "line": 432, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 441, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 444, "name": "test_extracts_label", "signature": "def test_extracts_label(self)"}, {"kind": "method", "line": 451, "name": "test_extracts_multiple_labels", "signature": "def test_extracts_multiple_labels(self)"}, {"kind": "method", "line": 461, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 464, "name": "test_returns_c_parser_for_c_extensions", "signature": "def test_returns_c_parser_for_c_extensions(self)"}, {"kind": "method", "line": 470, "name": "test_returns_python_parser_for_py", "signature": "def test_returns_python_parser_for_py(self)"}, {"kind": "method", "line": 475, "name": "test_returns_none_for_unknown_extension", "signature": "def test_returns_none_for_unknown_extension(self)"}, {"kind": "method", "line": 479, "name": "test_returns_rust_parser_for_rs", "signature": "def test_returns_rust_parser_for_rs(self)"}, {"kind": "method", "line": 484, "name": "test_case_insensitive_extension", "signature": "def test_case_insensitive_extension(self)"}]}, {"id": "tests/test_parsers_new.py", "kind": "module", "label": "test_parsers_new.py", "language": "py", "sha256": "a737c2342ea5e554", "symbol_count": 36, "symbols": [{"kind": "class", "line": 15, "name": "TestRubyParserContract", "signature": "class TestRubyParserContract(TestCase)"}, {"kind": "class", "line": 45, "name": "TestSwiftParserContract", "signature": "class TestSwiftParserContract(TestCase)"}, {"kind": "class", "line": 68, "name": "TestKotlinParserContract", "signature": "class TestKotlinParserContract(TestCase)"}, {"kind": "class", "line": 85, "name": "TestScalaParserContract", "signature": "class TestScalaParserContract(TestCase)"}, {"kind": "class", "line": 102, "name": "TestLuaParserContract", "signature": "class TestLuaParserContract(TestCase)"}, {"kind": "class", "line": 117, "name": "TestElixirParserContract", "signature": "class TestElixirParserContract(TestCase)"}, {"kind": "class", "line": 134, "name": "TestNewParserFactoryContract", "signature": "class TestNewParserFactoryContract(TestCase)"}, {"kind": "class", "line": 151, "name": "TestPythonCallExtractionContract", "signature": "class TestPythonCallExtractionContract(TestCase)"}, {"kind": "method", "line": 16, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 19, "name": "test_extracts_class_with_inheritance", "signature": "def test_extracts_class_with_inheritance(self)"}, {"kind": "method", "line": 27, "name": "test_extracts_module", "signature": "def test_extracts_module(self)"}, {"kind": "method", "line": 33, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 39, "name": "test_extracts_require", "signature": "def test_extracts_require(self)"}, {"kind": "method", "line": 46, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 49, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 55, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 61, "name": "test_extracts_protocol", "signature": "def test_extracts_protocol(self)"}, {"kind": "method", "line": 69, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 72, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 78, "name": "test_extracts_fun", "signature": "def test_extracts_fun(self)"}, {"kind": "method", "line": 86, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 89, "name": "test_extracts_object", "signature": "def test_extracts_object(self)"}, {"kind": "method", "line": 95, "name": "test_extracts_def", "signature": "def test_extracts_def(self)"}, {"kind": "method", "line": 103, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 106, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 111, "name": "test_extracts_require", "signature": "def test_extracts_require(self)"}, {"kind": "method", "line": 118, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 121, "name": "test_extracts_defmodule", "signature": "def test_extracts_defmodule(self)"}, {"kind": "method", "line": 127, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 135, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 138, "name": "test_ruby_extension_maps_correctly", "signature": "def test_ruby_extension_maps_correctly(self)"}, {"kind": "method", "line": 142, "name": "test_swift_extension_maps_correctly", "signature": "def test_swift_extension_maps_correctly(self)"}, {"kind": "method", "line": 146, "name": "test_kotlin_extension_maps_correctly", "signature": "def test_kotlin_extension_maps_correctly(self)"}, {"kind": "method", "line": 152, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 155, "name": "test_extracts_class_inheritance", "signature": "def test_extracts_class_inheritance(self)"}, {"kind": "method", "line": 160, "name": "test_extracts_function_calls", "signature": "def test_extracts_function_calls(self)"}]}, {"id": "tests/test_query.py", "kind": "module", "label": "test_query.py", "language": "py", "sha256": "9065822de432127b", "symbol_count": 18, "symbols": [{"kind": "function", "line": 7, "name": "_make_node", "signature": "def _make_node(node_id, symbols)"}, {"kind": "function", "line": 18, "name": "_make_sym", "signature": "def _make_sym(name, kind, line)"}, {"kind": "class", "line": 22, "name": "TestQueryEngineContract", "signature": "class TestQueryEngineContract(TestCase)"}, {"kind": "method", "line": 23, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 36, "name": "test_find_exact_symbol", "signature": "def test_find_exact_symbol(self)"}, {"kind": "method", "line": 42, "name": "test_find_symbol_fuzzy", "signature": "def test_find_symbol_fuzzy(self)"}, {"kind": "method", "line": 47, "name": "test_find_symbol_not_found", "signature": "def test_find_symbol_not_found(self)"}, {"kind": "method", "line": 51, "name": "test_explain_returns_details", "signature": "def test_explain_returns_details(self)"}, {"kind": "method", "line": 58, "name": "test_explain_shows_imports", "signature": "def test_explain_shows_imports(self)"}, {"kind": "method", "line": 63, "name": "test_explain_shows_siblings", "signature": "def test_explain_shows_siblings(self)"}, {"kind": "method", "line": 69, "name": "test_explain_unknown_returns_none", "signature": "def test_explain_unknown_returns_none(self)"}, {"kind": "method", "line": 73, "name": "test_find_path_direct_import", "signature": "def test_find_path_direct_import(self)"}, {"kind": "method", "line": 79, "name": "test_find_path_same_file", "signature": "def test_find_path_same_file(self)"}, {"kind": "method", "line": 84, "name": "test_find_path_unknown_returns_none", "signature": "def test_find_path_unknown_returns_none(self)"}, {"kind": "method", "line": 88, "name": "test_summary_shows_counts", "signature": "def test_summary_shows_counts(self)"}, {"kind": "method", "line": 94, "name": "test_summary_shows_top_modules", "signature": "def test_summary_shows_top_modules(self)"}, {"kind": "method", "line": 98, "name": "test_query_returns_matching_symbols", "signature": "def test_query_returns_matching_symbols(self)"}, {"kind": "method", "line": 102, "name": "test_query_returns_file_matches", "signature": "def test_query_returns_file_matches(self)"}]}, {"id": "tests/test_resolver.py", "kind": "module", "label": "test_resolver.py", "language": "py", "sha256": "92f1d5514af2d416", "symbol_count": 11, "symbols": [{"doc": "Contract: ImportResolver maps import strings to file paths.", "kind": "class", "line": 15, "name": "TestImportResolverContract", "signature": "class TestImportResolverContract(TestCase)"}, {"kind": "method", "line": 18, "name": "test_resolves_python_module_dotpath", "signature": "def test_resolves_python_module_dotpath(self)"}, {"kind": "method", "line": 25, "name": "test_resolves_relative_import", "signature": "def test_resolves_relative_import(self)"}, {"kind": "method", "line": 32, "name": "test_resolves_extensionless_python_import", "signature": "def test_resolves_extensionless_python_import(self)"}, {"kind": "method", "line": 39, "name": "test_resolves_package_init", "signature": "def test_resolves_package_init(self)"}, {"kind": "method", "line": 46, "name": "test_returns_none_for_external_stdlib", "signature": "def test_returns_none_for_external_stdlib(self)"}, {"kind": "method", "line": 53, "name": "test_returns_none_for_unknown_import", "signature": "def test_returns_none_for_unknown_import(self)"}, {"kind": "method", "line": 60, "name": "test_resolves_stem_match_when_unique", "signature": "def test_resolves_stem_match_when_unique(self)"}, {"kind": "method", "line": 67, "name": "test_returns_none_for_empty_import", "signature": "def test_returns_none_for_empty_import(self)"}, {"kind": "method", "line": 72, "name": "test_resolves_go_import", "signature": "def test_resolves_go_import(self)"}, {"kind": "method", "line": 79, "name": "test_resolves_same_directory_import", "signature": "def test_resolves_same_directory_import(self)"}]}, {"id": "tests/test_rule_gen.py", "kind": "module", "label": "test_rule_gen.py", "language": "py", "sha256": "fe6c1fc2b2c56a51", "symbol_count": 10, "symbols": [{"doc": "Contract: RuleGenerator detects patterns and suggests rules.", "kind": "class", "line": 12, "name": "TestRuleGeneratorContract", "signature": "class TestRuleGeneratorContract(TestCase)"}, {"kind": "method", "line": 15, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 19, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 29, "name": "_make_node_with_symbols", "signature": "def _make_node_with_symbols(self, nid, sym_count)"}, {"kind": "method", "line": 44, "name": "test_empty_nodes_returns_empty_rules", "signature": "def test_empty_nodes_returns_empty_rules(self)"}, {"kind": "method", "line": 48, "name": "test_generates_rules_for_function_heavy_language", "signature": "def test_generates_rules_for_function_heavy_language(self)"}, {"kind": "method", "line": 56, "name": "test_detects_antipatterns_with_content", "signature": "def test_detects_antipatterns_with_content(self)"}, {"kind": "method", "line": 67, "name": "test_antipattern_threshold_from_config", "signature": "def test_antipattern_threshold_from_config(self)"}, {"kind": "method", "line": 77, "name": "test_write_rules_creates_files", "signature": "def test_write_rules_creates_files(self)"}, {"kind": "method", "line": 90, "name": "test_rule_id_increments", "signature": "def test_rule_id_increments(self)"}]}, {"id": "tests/test_sarif.py", "kind": "module", "label": "test_sarif.py", "language": "py", "sha256": "6522296ceb83662c", "symbol_count": 10, "symbols": [{"doc": "Contract: SarifExporter produces valid SARIF v2.1.0 JSON.", "kind": "class", "line": 11, "name": "TestSarifExporterContract", "signature": "class TestSarifExporterContract(TestCase)"}, {"kind": "method", "line": 14, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 18, "name": "_make_finding", "signature": "def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)"}, {"kind": "method", "line": 38, "name": "test_export_returns_valid_json", "signature": "def test_export_returns_valid_json(self)"}, {"kind": "method", "line": 46, "name": "test_export_includes_tool_info", "signature": "def test_export_includes_tool_info(self)"}, {"kind": "method", "line": 54, "name": "test_export_includes_rule", "signature": "def test_export_includes_rule(self)"}, {"kind": "method", "line": 62, "name": "test_export_includes_result", "signature": "def test_export_includes_result(self)"}, {"kind": "method", "line": 73, "name": "test_severity_maps_correctly", "signature": "def test_severity_maps_correctly(self)"}, {"kind": "method", "line": 88, "name": "test_privacy_mode_strips_snippets", "signature": "def test_privacy_mode_strips_snippets(self)"}, {"kind": "method", "line": 97, "name": "test_empty_findings_produces_valid_sarif", "signature": "def test_empty_findings_produces_valid_sarif(self)"}]}, {"id": "tests/test_scanner.py", "kind": "module", "label": "test_scanner.py", "language": "py", "sha256": "ede5f381a6fbf273", "symbol_count": 17, "symbols": [{"kind": "class", "line": 11, "name": "TestScannerContract", "signature": "class TestScannerContract(TestCase)"}, {"kind": "method", "line": 12, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 16, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 20, "name": "_write", "signature": "def _write(self, path, content)"}, {"kind": "method", "line": 25, "name": "test_scans_python_files", "signature": "def test_scans_python_files(self)"}, {"kind": "method", "line": 32, "name": "test_ignores_env_and_vendor_dirs", "signature": "def test_ignores_env_and_vendor_dirs(self)"}, {"kind": "method", "line": 45, "name": "test_rejects_symlinks", "signature": "def test_rejects_symlinks(self)"}, {"kind": "method", "line": 59, "name": "test_skips_non_code_files", "signature": "def test_skips_non_code_files(self)"}, {"kind": "method", "line": 70, "name": "test_scans_multiple_languages", "signature": "def test_scans_multiple_languages(self)"}, {"kind": "method", "line": 79, "name": "test_respects_max_directory_depth", "signature": "def test_respects_max_directory_depth(self)"}, {"kind": "method", "line": 89, "name": "test_raises_on_invalid_directory", "signature": "def test_raises_on_invalid_directory(self)"}, {"kind": "method", "line": 94, "name": "test_import_edges_are_created", "signature": "def test_import_edges_are_created(self)"}, {"kind": "method", "line": 104, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 114, "name": "test_scan_with_content_returns_content_map", "signature": "def test_scan_with_content_returns_content_map(self)"}, {"kind": "method", "line": 122, "name": "test_gitignore_respected_when_enabled", "signature": "def test_gitignore_respected_when_enabled(self)"}, {"kind": "method", "line": 133, "name": "test_gitignore_disabled_by_default", "signature": "def test_gitignore_disabled_by_default(self)"}, {"kind": "method", "line": 142, "name": "test_gitignore_glob_conversion", "signature": "def test_gitignore_glob_conversion(self)"}]}, {"id": "tests/test_security.py", "kind": "module", "label": "test_security.py", "language": "py", "sha256": "1d6c761aa2bbc230", "symbol_count": 63, "symbols": [{"doc": "SecurityFinding dataclass contract tests.", "kind": "class", "line": 21, "name": "TestSecurityFinding", "signature": "class TestSecurityFinding(TestCase)"}, {"doc": "SecurityAnalyzer configuration contract tests.", "kind": "class", "line": 43, "name": "TestSecurityAnalyzerConfig", "signature": "class TestSecurityAnalyzerConfig(TestCase)"}, {"doc": "Per-language rule detection tests using inline code.", "kind": "class", "line": 64, "name": "TestSecurityAnalyzerRules", "signature": "class TestSecurityAnalyzerRules(TestCase)"}, {"doc": "Severity threshold filtering tests.", "kind": "class", "line": 295, "name": "TestSecurityAnalyzerThreshold", "signature": "class TestSecurityAnalyzerThreshold(TestCase)"}, {"doc": "Security path validation tests.", "kind": "class", "line": 327, "name": "TestSecurityAnalyzerPathValidation", "signature": "class TestSecurityAnalyzerPathValidation(TestCase)"}, {"doc": "Security summary output tests.", "kind": "class", "line": 374, "name": "TestSecurityAnalyzerSummary", "signature": "class TestSecurityAnalyzerSummary(TestCase)"}, {"kind": "method", "line": 24, "name": "test_security_finding_fields", "signature": "def test_security_finding_fields(self)"}, {"kind": "method", "line": 46, "name": "test_default_config_disables_security", "signature": "def test_default_config_disables_security(self)"}, {"kind": "method", "line": 50, "name": "test_default_severity_threshold", "signature": "def test_default_severity_threshold(self)"}, {"kind": "method", "line": 54, "name": "test_default_security_output", "signature": "def test_default_security_output(self)"}, {"kind": "method", "line": 58, "name": "test_init_with_config", "signature": "def test_init_with_config(self)"}, {"kind": "method", "line": 67, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Write content to a temp file and scan it.", "kind": "method", "line": 71, "name": "_scan_content", "signature": "def _scan_content(self, content, extension)"}, {"kind": "method", "line": 78, "name": "test_python_os_system", "signature": "def test_python_os_system(self)"}, {"kind": "method", "line": 83, "name": "test_python_eval", "signature": "def test_python_eval(self)"}, {"kind": "method", "line": 88, "name": "test_python_pickle", "signature": "def test_python_pickle(self)"}, {"kind": "method", "line": 93, "name": "test_python_sql_injection", "signature": "def test_python_sql_injection(self)"}, {"kind": "method", "line": 98, "name": "test_python_hardcoded_secret", "signature": "def test_python_hardcoded_secret(self)"}, {"kind": "method", "line": 103, "name": "test_python_weak_crypto", "signature": "def test_python_weak_crypto(self)"}, {"kind": "method", "line": 108, "name": "test_python_request_verify_false", "signature": "def test_python_request_verify_false(self)"}, {"kind": "method", "line": 113, "name": "test_python_flask_debug", "signature": "def test_python_flask_debug(self)"}, {"kind": "method", "line": 118, "name": "test_python_yaml_load", "signature": "def test_python_yaml_load(self)"}, {"kind": "method", "line": 123, "name": "test_javascript_inner_html", "signature": "def test_javascript_inner_html(self)"}, {"kind": "method", "line": 128, "name": "test_javascript_eval", "signature": "def test_javascript_eval(self)"}, {"kind": "method", "line": 133, "name": "test_javascript_child_process", "signature": "def test_javascript_child_process(self)"}, {"kind": "method", "line": 138, "name": "test_javascript_dangerously_set_inner_html", "signature": "def test_javascript_dangerously_set_inner_html(self)"}, {"kind": "method", "line": 143, "name": "test_c_strcpy", "signature": "def test_c_strcpy(self)"}, {"kind": "method", "line": 148, "name": "test_c_gets", "signature": "def test_c_gets(self)"}, {"kind": "method", "line": 153, "name": "test_c_system", "signature": "def test_c_system(self)"}, {"kind": "method", "line": 158, "name": "test_java_runtime_exec", "signature": "def test_java_runtime_exec(self)"}, {"kind": "method", "line": 163, "name": "test_java_sql_injection", "signature": "def test_java_sql_injection(self)"}, {"kind": "method", "line": 168, "name": "test_go_exec_command", "signature": "def test_go_exec_command(self)"}, {"kind": "method", "line": 173, "name": "test_ruby_eval", "signature": "def test_ruby_eval(self)"}, {"kind": "method", "line": 178, "name": "test_ruby_marshal_load", "signature": "def test_ruby_marshal_load(self)"}, {"kind": "method", "line": 183, "name": "test_php_eval", "signature": "def test_php_eval(self)"}, {"kind": "method", "line": 188, "name": "test_php_sql_injection", "signature": "def test_php_sql_injection(self)"}, {"kind": "method", "line": 193, "name": "test_php_unseralize", "signature": "def test_php_unseralize(self)"}, {"kind": "method", "line": 198, "name": "test_shell_eval", "signature": "def test_shell_eval(self)"}, {"kind": "method", "line": 203, "name": "test_csharp_process_start", "signature": "def test_csharp_process_start(self)"}, {"kind": "method", "line": 208, "name": "test_kotlin_runtime_exec", "signature": "def test_kotlin_runtime_exec(self)"}, {"kind": "method", "line": 213, "name": "test_swift_process", "signature": "def test_swift_process(self)"}, {"kind": "method", "line": 218, "name": "test_lua_load", "signature": "def test_lua_load(self)"}, {"kind": "method", "line": 223, "name": "test_lua_os_execute", "signature": "def test_lua_os_execute(self)"}, {"kind": "method", "line": 228, "name": "test_dart_process_run", "signature": "def test_dart_process_run(self)"}, {"kind": "method", "line": 233, "name": "test_rust_unsafe", "signature": "def test_rust_unsafe(self)"}, {"kind": "method", "line": 238, "name": "test_elixir_code_eval", "signature": "def test_elixir_code_eval(self)"}, {"kind": "method", "line": 243, "name": "test_elixir_system_cmd", "signature": "def test_elixir_system_cmd(self)"}, {"kind": "method", "line": 248, "name": "test_gdscript_os_execute", "signature": "def test_gdscript_os_execute(self)"}, {"kind": "method", "line": 253, "name": "test_scala_runtime_exec", "signature": "def test_scala_runtime_exec(self)"}, {"kind": "method", "line": 258, "name": "test_nim_exec_process", "signature": "def test_nim_exec_process(self)"}, {"kind": "method", "line": 263, "name": "test_safe_code_produces_no_findings", "signature": "def test_safe_code_produces_no_findings(self)"}, {"kind": "method", "line": 274, "name": "test_csharp_binary_formatter", "signature": "def test_csharp_binary_formatter(self)"}, {"kind": "method", "line": 279, "name": "test_ruby_backtick", "signature": "def test_ruby_backtick(self)"}, {"kind": "method", "line": 284, "name": "test_php_xss", "signature": "def test_php_xss(self)"}, {"kind": "method", "line": 289, "name": "test_go_unsafe_package", "signature": "def test_go_unsafe_package(self)"}, {"kind": "method", "line": 298, "name": "test_threshold_filters_low", "signature": "def test_threshold_filters_low(self)"}, {"kind": "method", "line": 312, "name": "test_threshold_info_shows_all", "signature": "def test_threshold_info_shows_all(self)"}, {"kind": "method", "line": 330, "name": "test_ignores_symlinks", "signature": "def test_ignores_symlinks(self)"}, {"kind": "method", "line": 345, "name": "test_ignores_ignored_dirs", "signature": "def test_ignores_ignored_dirs(self)"}, {"kind": "method", "line": 357, "name": "test_empty_directory", "signature": "def test_empty_directory(self)"}, {"kind": "method", "line": 364, "name": "test_unsupported_extension", "signature": "def test_unsupported_extension(self)"}, {"kind": "method", "line": 377, "name": "test_summary_empty", "signature": "def test_summary_empty(self)"}, {"kind": "method", "line": 383, "name": "test_summary_with_findings", "signature": "def test_summary_with_findings(self)"}]}, {"id": "tests/test_taint.py", "kind": "module", "label": "test_taint.py", "language": "py", "sha256": "d196fca30ed7d086", "symbol_count": 10, "symbols": [{"doc": "Contract: TaintAnalyzer discovers taint propagation paths.", "kind": "class", "line": 10, "name": "TestTaintAnalyzerContract", "signature": "class TestTaintAnalyzerContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label)"}, {"kind": "method", "line": 20, "name": "test_empty_graph_returns_empty_result", "signature": "def test_empty_graph_returns_empty_result(self)"}, {"kind": "method", "line": 25, "name": "test_no_dangerous_imports_returns_empty", "signature": "def test_no_dangerous_imports_returns_empty(self)"}, {"kind": "method", "line": 31, "name": "test_direct_dangerous_import_found", "signature": "def test_direct_dangerous_import_found(self)"}, {"kind": "method", "line": 38, "name": "test_taint_propagates_through_resolved_edges", "signature": "def test_taint_propagates_through_resolved_edges(self)"}, {"kind": "method", "line": 62, "name": "test_dangerous_import_by_language", "signature": "def test_dangerous_import_by_language(self)"}, {"kind": "method", "line": 70, "name": "test_taint_path_has_severity", "signature": "def test_taint_path_has_severity(self)"}, {"kind": "method", "line": 77, "name": "test_max_depth_limits_propagation", "signature": "def test_max_depth_limits_propagation(self)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (67 files)

#### `__init__.py`
**Path:** `readmenator/__init__.py`

*No symbols extracted*

#### `__main__.py`
**Path:** `readmenator/__main__.py`

**Functions:**
- `build_parser` (line 14) `def build_parser()`
- `_run_tests` (line 59) `def _run_tests()`
- `main` (line 74) `def main()`

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
- `_suggest_questions` (line 315) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)` - *Generate plain-language exploration questions from graph structure.*

#### `_app.py`
**Path:** `readmenator/_app.py`

**Classes:**
- `readmenatorApplication` (line 24) `class readmenatorApplication`

**Methods:**
- `__init__` (line 25) `def __init__(self, config)`
- `_scan` (line 34) `def _scan(self, target_dir)`
- `_scan_with_content` (line 42) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (line 52) `def _resolve_imports(self, nodes, edges, target_dir)`
- `run` (line 71) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- `_write_sidecar_outputs` (line 122) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_log_summary` (line 148) `def _log_summary(self, nodes, edges, resolved_edges, analysis, layer_summary, analysis_v2, findings)`
- `update` (line 202) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (line 233) `def _scan_for_cache(self, root, cache)`
- `query` (line 251) `def query(self, target_dir, question)`
- `explain` (line 256) `def explain(self, target_dir, symbol_name)`
- `find_path` (line 268) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (line 281) `def summary(self, target_dir)`
- `rebuild` (line 286) `def rebuild(self, target_dir, run_security)`
- `analyze` (line 289) `def analyze(self, target_dir)`
- `export_json` (line 293) `def export_json(self, target_dir, output_path)`
- `export_html` (line 304) `def export_html(self, target_dir, output_path)`
- `export_svg` (line 315) `def export_svg(self, target_dir, output_path)`
- `export` (line 326) `def export(self, target_dir)`
- `export_graphml` (line 331) `def export_graphml(self, target_dir, output_path)`
- `export_obsidian` (line 342) `def export_obsidian(self, target_dir, output_dir)`
- `watch` (line 352) `def watch(self, target_dir)`
- `audit` (line 362) `def audit(self, target_dir)`
- `audit_deep` (line 369) `def audit_deep(self, target_dir)`
- `export_sarif` (line 389) `def export_sarif(self, target_dir, output_path)`
- `export_rules` (line 399) `def export_rules(self, target_dir, output_dir)`
- `detect_layers` (line 409) `def detect_layers(self, target_dir)`
- `on_change` (line 356) `def on_change()`

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

#### `_cpg.py`
**Path:** `readmenator/_cpg.py`

**Classes:**
- `CodePropertyGraph` (line 10) `class CodePropertyGraph` - *Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.

Produces a structured representation merging AST-level symbol data,
control-flow edges (calls), data-flow edges (imports), and inheritance
relationships into a single machine-readable document. Designed to be
embedded in KNOWLEDGE_BASE.md for zero-token agent context.*

**Methods:**
- `__init__` (line 21) `def __init__(self, privacy_mode)`
- `generate` (line 24) `def generate(self, nodes, edges, resolved_edges, analysis)` - *Generate the CPG JSON-LD string embeddable in markdown.

Returns a compact JSON object with @context, nodes array (each
containing id, label, kind, language, sha256, symbols, layer),
edges array (source, target, relation, confidence), and analysis
metadata (god_nodes, communities).*
- `_build_symbol_list` (line 109) `def _build_symbol_list(self, node)` - *Build symbol list for a node, respecting privacy mode.*
- `_compute_node_hash` (line 126) `def _compute_node_hash(node)` - *Compute a deterministic content hash for a node.*

#### `_documentation.py`
**Path:** `readmenator/_documentation.py`

**Classes:**
- `DocumentationGenerator` (line 24) `class DocumentationGenerator` - *Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

Delegates graph rendering to MermaidRenderer and handles the
Markdown layout: header metadata, Mermaid block, statistics dashboard,
god nodes, community analysis, surprising connections, architecture
layers, security audit, taint analysis, hotspots, dependency cycles,
change impact, architecture violations, suggested rules, CPG block,
and per-language architecture sections with pluralised symbol kind headings.*

**Methods:**
- `__init__` (line 35) `def __init__(self, config)`
- `generate` (line 49) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2)`
- `_build_toc` (line 105) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated)`
- `_build_layers` (line 172) `def _build_layers(self, layers, nodes)`
- `_build_dashboard` (line 206) `def _build_dashboard(self, nodes, edges, resolved_edges)`
- `_build_god_nodes` (line 286) `def _build_god_nodes(self, analysis)`
- `_build_community_analysis` (line 306) `def _build_community_analysis(self, analysis, nodes)`
- `_build_surprising_connections` (line 339) `def _build_surprising_connections(self, analysis, nodes)`
- `_build_suggested_questions` (line 364) `def _build_suggested_questions(self, analysis)`
- `_build_taint_analysis` (line 380) `def _build_taint_analysis(self, analysis_v2)`
- `_build_hotspots` (line 415) `def _build_hotspots(self, analysis_v2)`
- `_build_dependency_cycles` (line 441) `def _build_dependency_cycles(self, analysis_v2)`
- `_build_change_impact` (line 461) `def _build_change_impact(self, analysis_v2)`
- `_build_layer_violations` (line 486) `def _build_layer_violations(self, analysis_v2)`
- `_build_suggested_rules` (line 514) `def _build_suggested_rules(self, analysis_v2)`
- `_build_security_findings` (line 539) `def _build_security_findings(self, findings)`
- `_build_mermaid_section` (line 586) `def _build_mermaid_section(self, graph_output, is_truncated)`
- `_build_cpg_block` (line 609) `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
- `_build_architecture_reference` (line 635) `def _build_architecture_reference(self, nodes, edges)`

#### `_exporter.py`
**Path:** `readmenator/_exporter.py`

**Classes:**
- `GraphExporter` (line 21) `class GraphExporter` - *Exports the knowledge graph to JSON, HTML, and SVG formats.

Each method is self-contained and produces a single file. No
external network calls are made; the HTML file embeds vis.js
from a CDN reference for offline-compatible rendering.*

**Methods:**
- `__init__` (line 29) `def __init__(self, config)` - *Initialise with application configuration.

Args:
    config: Settings for export styling and limits.*
- `to_json` (line 37) `def to_json(self, nodes, edges, resolved_edges, analysis, findings)` - *Export the graph as a node-link JSON string.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for metadata.
    findings: Optional security audit findings.

Returns:
    JSON string with nodes, edges, and optional analysis/findings metadata.*
- `to_html` (line 150) `def to_html(self, nodes, edges, resolved_edges, analysis, findings)` - *Generate a standalone interactive HTML graph page.

Uses vis.js loaded from CDN. Supports click-to-inspect nodes,
search filtering, and community-based coloring.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community coloring.

Returns:
    Complete HTML document as a string.*
- `_community_color_map` (line 236) `def _community_color_map(self, analysis)` - *Build a node-to-color map based on community membership.*
- `_lighten` (line 254) `def _lighten(hex_color)` - *Lighten a hex color by 30% for border use.*
- `_render_html` (line 262) `def _render_html(self, vis_nodes, vis_edges, analysis, findings)` - *Render the full HTML document with vis.js.*
- `to_svg` (line 421) `def to_svg(self, nodes, edges, resolved_edges, analysis)` - *Generate a static SVG representation of the graph.

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
- `_render_truncated_svg` (line 539) `def _render_truncated_svg(self, total_nodes)` - *Render a minimal SVG with a truncation notice.*
- `_layout_spring` (line 554) `def _layout_spring(self, nodes, edges, node_map)` - *Compute a simple spring-layout for node positioning.

Implements a basic force-directed layout with repulsion
between all nodes and attraction along edges. Runs a fixed
number of iterations for determinism.*
- `to_graphml` (line 635) `def to_graphml(self, nodes, edges, resolved_edges, analysis)` - *Export the graph as GraphML (Gephi/yEd compatible).

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community data.

Returns:
    GraphML XML string.*
- `to_obsidian` (line 712) `def to_obsidian(self, nodes, edges, output_dir, analysis)` - *Export the graph as an Obsidian vault with wikilinks.

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
- `_project` (line 483) `def _project(pos)`
- `_sev_span` (line 334) `def _sev_span(sev, count)`

#### `_hotspots.py`
**Path:** `readmenator/_hotspots.py`

**Classes:**
- `HotspotAnalyzer` (line 16) `class HotspotAnalyzer` - *Hotspot detection, cycle analysis, and change impact analysis.

Hotspots are files with high complexity (many symbols) and high
centrality (many connections). Cycle detection finds circular
dependencies in the resolved import graph. Change impact analysis
computes transitive-dependent lists for every file.*

**Methods:**
- `__init__` (line 25) `def __init__(self, config)`
- `analyze_hotspots` (line 28) `def analyze_hotspots(self, nodes, edges, resolved_edges)` - *Rank files by combined complexity and centrality scores.

Complexity is normalised symbol count. Centrality is normalised
connection count (in-degree + out-degree). The combined score
uses configured weights.*
- `detect_cycles` (line 84) `def detect_cycles(self, nodes, resolved_edges)` - *Detect cycles in the resolved import graph using DFS.

Uses Tarjan's algorithm variant with three-colour DFS to find
all elementary cycles. Returns each cycle as a DependencyCycle.*
- `analyze_change_impact` (line 149) `def analyze_change_impact(self, nodes, resolved_edges)` - *Compute change impact for every file in the project.

For each file, finds all files that would be affected if it
changed (direct and transitive dependents via reverse import
graph traversal).*
- `_dfs_visit` (line 108) `def _dfs_visit(current)`
- `_record_cycle` (line 119) `def _record_cycle(start, end)`

#### `_layer_rules.py`
**Path:** `readmenator/_layer_rules.py`

**Classes:**
- `LayerRuleEngine` (line 9) `class LayerRuleEngine` - *Architectural layer violation detection engine.

Defines a set of permitted and forbidden layer-to-layer import
rules. Scans all resolved import edges and flags violations
where one layer imports from another in a way that violates
the architecture.*

**Methods:**
- `__init__` (line 34) `def __init__(self, config)`
- `detect_violations` (line 37) `def detect_violations(self, nodes, edges, resolved_edges, layers)` - *Detect architectural layer violations.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved import edges.
    layers: Dict mapping node_id to layer name. If None, imports
        _layers.LayerDetector for automatic detection.

Returns:
    List of LayerViolation instances.*
- `violation_summary` (line 109) `def violation_summary(violations)` - *Summarise violations by severity.*

#### `_layers.py`
**Path:** `readmenator/_layers.py`

**Classes:**
- `LayerDetector` (line 15) `class LayerDetector` - *Detects architectural layers in a codebase.

Assigns each file to a layer based on path patterns, naming
conventions, and imported frameworks. Returns a mapping that
can enrich documentation and analysis. No config dependency.*

**Methods:**
- `detect` (line 71) `def detect(self, nodes, edges)` - *Assign each file node to an architectural layer.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.

Returns:
    Dict mapping node_id to layer name.*
- `_classify_file` (line 89) `def _classify_file(self, node, edges)` - *Classify a single file into an architectural layer.*
- `layer_summary` (line 122) `def layer_summary(layers)` - *Count files per layer.

Args:
    layers: Mapping from detect().

Returns:
    Dict of layer_name -> file_count.*

#### `_mermaid.py`
**Path:** `readmenator/_mermaid.py`

**Classes:**
- `MermaidRenderer` (line 17) `class MermaidRenderer` - *Renders a knowledge graph to Mermaid JS flowchart syntax.

Nodes are ordered by import count and symbol richness; the top
``max_nodes`` entries are included. External dependencies appear
as dashed boxes. Internal import edges are solid arrows.
Community subgraphs group related files when analysis is available.*

**Methods:**
- `__init__` (line 26) `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)`
- `_sanitize_id` (line 45) `def _sanitize_id(node_id)` - *Convert *node_id* to a Mermaid-safe identifier.

Replaces non-alphanumeric characters with underscores and
prepends ``n_`` if the result starts with a digit.*
- `render` (line 56) `def render(self, nodes, edges, resolved_edges, analysis)` - *Produce a Mermaid flowchart string and a truncation flag.

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
- `SecurityFinding` (line 73) `class SecurityFinding` - *A security-relevant pattern detected in a source file.

Attributes:
    file_path: Relative path of the file containing the finding.
    line: One-based line number where the pattern was found.
    severity: Severity level (critical, high, medium, low, info).
    rule_id: Unique identifier for the detection rule (e.g. "PY001").
    description: Human-readable explanation of the issue.
    snippet: The offending source code line.
    cwe: CWE identifier string (e.g. "CWE-78").*
- `CommunityResult` (line 105) `class CommunityResult` - *Result of community detection on the import graph.

Attributes:
    community_id: Integer identifier of the community.
    label: Human-readable name for the community.
    file_ids: Set of node IDs belonging to this community.
    cohesion: Cohesion score (internal edges / total edges involving community).
    size: Number of files in the community.*
- `AnalysisResult` (line 124) `class AnalysisResult` - *Complete graph analysis output.

Attributes:
    god_nodes: List of (node_id, score) for most central nodes.
    communities: List of CommunityResult instances.
    surprising_connections: List of (source_node, target_node, hops, bridging_communities).
    suggested_questions: List of plain-language exploration questions.
    node_count: Total nodes in the graph.
    edge_count: Total edges in the graph.*
- `TaintPath` (line 145) `class TaintPath` - *A taint propagation path from source to sink through the import graph.

Attributes:
    source_file: The file that introduces the dangerous import.
    sink_file: The file that transitively receives the taint.
    path: List of file node IDs forming the propagation chain.
    hops: Number of hops in the propagation path.
    dangerous_import: The specific dangerous module or function imported.
    severity: Inferred severity of the taint path.*
- `TaintAnalysisResult` (line 166) `class TaintAnalysisResult` - *Complete taint propagation analysis output.

Attributes:
    paths: List of TaintPath instances discovered.
    source_count: Number of unique taint source files.
    sink_count: Number of unique taint sink files.*
- `DependencyCycle` (line 181) `class DependencyCycle` - *A cycle detected in the resolved import graph.

Attributes:
    cycle: List of file node IDs forming the cycle.
    length: Number of files in the cycle.*
- `ChangeImpact` (line 194) `class ChangeImpact` - *Change impact analysis for a single file.

Attributes:
    file_id: The file that would be changed.
    direct_dependents: Files that directly import this file.
    transitive_dependents: Files that transitively depend on this file.
    total_impact: Total number of affected files (direct + transitive).*
- `HotspotResult` (line 211) `class HotspotResult` - *A hotspot file combining complexity and centrality metrics.

Attributes:
    file_id: The file node ID.
    complexity_score: Normalised symbol count score (0-1).
    centrality_score: Normalised god node score (0-1).
    combined_score: Weighted combination of complexity and centrality.
    symbol_count: Raw symbol count.
    connection_count: Raw connection count.*
- `SuggestedRule` (line 232) `class SuggestedRule` - *A suggested linting/security rule derived from code patterns.

Attributes:
    rule_id: Suggested rule identifier (e.g. "RM001").
    severity: Suggested severity (info, warning, error).
    description: Human-readable description of the pattern.
    pattern: The detected pattern or code snippet.
    file_examples: Example file paths where the pattern was found.
    match_count: Number of times the pattern was matched.
    language: Target language for the rule.
    semgrep_yaml: Optional Semgrep rule YAML string.*
- `LayerViolation` (line 257) `class LayerViolation` - *A detected architectural layer violation.

Attributes:
    source_file: The file causing the violation.
    source_layer: The layer of the source file.
    target_file: The file being imported.
    target_layer: The layer of the target file.
    description: Description of the violation.
    severity: Severity (strict, warn, info).*
- `AnalysisResultV2` (line 278) `class AnalysisResultV2` - *Extended analysis result combining all new analysis modules.

Attributes:
    taint: Optional taint analysis result.
    cycles: List of dependency cycles.
    change_impacts: List of change impact results for key files.
    hotspots: List of hotspot results.
    suggested_rules: List of suggested linting rules.
    layer_violations: List of layer violations.*

**Methods:**
- `pluralize_symbol_kind` (line 95) `def pluralize_symbol_kind(kind, plural_map)` - *Return the plural form of *kind* according to *plural_map*.

Falls back to appending ``"s"`` when the kind is not found.
This prevents obvious misspellings like ``"Classs"``.*

#### `_pipeline.py`
**Path:** `readmenator/_pipeline.py`

**Classes:**
- `AnalyzerFactory` (line 28) `class AnalyzerFactory` - *Lazy factory for all readmenator analyzer and generator instances.

Decouples the application orchestrator from the concrete
instantiation of analysis modules. Each component is created
on first access and cached for the lifetime of the factory.*
- `DeepAnalysisRunner` (line 124) `class DeepAnalysisRunner` - *Orchestrates the extended V2 analysis pipeline.

Runs taint propagation, hotspot detection, cycle detection,
change impact, layer violations, and rule generation as a
coordinated batch. Isolated from the main app to reduce
coupling in the primary orchestration layer.*

**Methods:**
- `__init__` (line 36) `def __init__(self, config)`
- `scanner` (line 52) `def scanner(self)`
- `generator` (line 58) `def generator(self)`
- `analyzer` (line 64) `def analyzer(self)`
- `security` (line 70) `def security(self)`
- `exporter` (line 76) `def exporter(self)`
- `taint` (line 82) `def taint(self)`
- `hotspots` (line 88) `def hotspots(self)`
- `layer_rules` (line 94) `def layer_rules(self)`
- `rule_gen` (line 100) `def rule_gen(self)`
- `sarif` (line 106) `def sarif(self)`
- `cpg` (line 112) `def cpg(self)`
- `layer_detector` (line 118) `def layer_detector(self)`
- `__init__` (line 133) `def __init__(self, factory)`
- `run` (line 136) `def run(self, nodes, edges, resolved_edges, layers, content_map)`

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

#### `_rule_gen.py`
**Path:** `readmenator/_rule_gen.py`

**Classes:**
- `RuleGenerator` (line 12) `class RuleGenerator` - *Generates suggested linting and security rules from code patterns.

Analyses the scanned codebase for repeated patterns that suggest
project-specific linting rules: bare except clauses, repeated
type annotations, common security antipatterns, and naming
convention violations. Outputs Semgrep YAML rules to a directory.*

**Methods:**
- `__init__` (line 88) `def __init__(self, config)`
- `generate` (line 92) `def generate(self, nodes, content_map)` - *Generate suggested rules by scanning code patterns.

Args:
    nodes: Scanned file nodes with symbols.
    content_map: Optional mapping of file paths to their source content
        for deeper pattern matching.

Returns:
    List of SuggestedRule instances.*
- `write_rules` (line 120) `def write_rules(self, rules, output_dir)` - *Write suggested rules to Semgrep YAML files in output_dir.

Returns the number of rule files written.*
- `_group_by_language` (line 159) `def _group_by_language(self, nodes)` - *Group nodes by their language extension.*
- `_analyze_language` (line 169) `def _analyze_language(self, lang, nodes, content_map)` - *Analyze a single language group for rule suggestions.*
- `_detect_antipatterns` (line 202) `def _detect_antipatterns(self, nodes, content_map)` - *Detect known antipatterns across all files.*
- `_infer_language_for_rule` (line 248) `def _infer_language_for_rule(rule_id)` - *Infer target language for a built-in antipattern rule.*
- `_next_rule_id` (line 258) `def _next_rule_id(self)` - *Generate the next rule identifier.*

#### `_sarif.py`
**Path:** `readmenator/_sarif.py`

**Classes:**
- `SarifExporter` (line 9) `class SarifExporter` - *Exports security findings to the SARIF standard format.

SARIF is an OASIS standard format for static analysis tool output.
This exporter produces SARIF v2.1.0 JSON compatible with GitHub
Code Scanning, VS Code SARIF viewer, and other SARIF consumers.*

**Methods:**
- `__init__` (line 28) `def __init__(self, privacy_mode)`
- `export` (line 31) `def export(self, findings, project_name)` - *Generate a SARIF v2.1.0 JSON string from security findings.

Args:
    findings: List of SecurityFinding instances.
    project_name: Name of the scanned project for metadata.

Returns:
    SARIF JSON string.*
- `_build_rule` (line 80) `def _build_rule(self, finding)` - *Build a SARIF reportingDescriptor (rule) object.*
- `_build_result` (line 104) `def _build_result(self, finding, rule_index)` - *Build a SARIF result object for a single finding.*

#### `_scanner.py`
**Path:** `readmenator/_scanner.py`

**Classes:**
- `PolyglotScanner` (line 22) `class PolyglotScanner` - *Recursive directory scanner with security and size guards.

Rejects symlinks, enforces file-size and directory-depth limits,
skips ignored directories, and silently catches parse errors
so a single misbehaving file never breaks the full scan.

Supports privacy mode (strips snippets and docstrings) and
gitignore-aware scanning for more accurate project coverage.*

**Methods:**
- `__init__` (line 33) `def __init__(self, config)` - *Initialise the scanner with application configuration.

Args:
    config: Settings including ignore dirs, size limits, etc.*
- `_is_ignored` (line 42) `def _is_ignored(self, path)` - *Return ``True`` if any path component matches IGNORE_DIRS.*
- `_load_gitignore` (line 46) `def _load_gitignore(self, root)` - *Parse .gitignore patterns using regex (no external deps).*
- `_gitignore_glob_to_regex` (line 68) `def _gitignore_glob_to_regex(pattern)` - *Convert a .gitignore glob pattern to a regex pattern.*
- `_is_gitignored` (line 108) `def _is_gitignored(self, rel_path)` - *Check if a relative path matches any .gitignore pattern.*
- `_validate_path_security` (line 117) `def _validate_path_security(self, path)` - *Reject symlinks and files exceeding MAX_FILE_SIZE_MB.*
- `_check_directory_depth` (line 130) `def _check_directory_depth(self, path, root)` - *Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.*
- `_extract_file_doc` (line 138) `def _extract_file_doc(self, content)` - *Extract a file-level docstring from the first lines of a source file.

Walks the first FILE_HEADER_MAX_LINES lines looking for a contiguous
block of comments or a shebang followed by comments. Returns the
concatenated comment text.

Args:
    content: Raw file content as a string.

Returns:
    Extracted file-level docstring or empty string.*
- `_emit_progress` (line 191) `def _emit_progress(self, count)` - *Emit a progress message every PROGRESS_REPORT_BATCH files.

Args:
    count: Number of files scanned so far.*
- `scan` (line 201) `def scan(self, root)` - *Walk *root* recursively and produce (nodes, edges) for the graph.

Security checks (symlinks, size, depth, ignore dirs) are applied
per file. Parse failures are silently caught so a single broken
file never blocks the rest of the scan.

Returns:
    A tuple of (list of Node, list of Edge). Edges represent
    ``imports`` relationships between scanned files.*
- `scan_with_content` (line 215) `def scan_with_content(self, root)` - *Scan and also return raw file contents for deeper analysis.

Returns:
    Tuple of (nodes, edges, content_map) where content_map maps
    node_id to raw file content.*
- `_scan_impl` (line 226) `def _scan_impl(self, root)` - *Internal scan implementation returning nodes, edges, and content.*

#### `_security.py`
**Path:** `readmenator/_security.py`

**Classes:**
- `SecurityRule` (line 20) `class SecurityRule` - *A single security detection rule.

Attributes:
    rule_id: Unique identifier (e.g. "PY001").
    severity: Severity level (critical, high, medium, low, info).
    description: Human-readable description of the issue.
    pattern: Compiled regex to search for.
    cwe: CWE identifier string.*
- `SecurityAnalyzer` (line 38) `class SecurityAnalyzer` - *Pattern-based static security scanner.

Maintains per-language rule sets and walks the target directory
applying rules to every supported source file. Designed to slot
into the readmenator pipeline alongside GraphAnalyzer.*

**Methods:**
- `_compile` (line 203) `def _compile()` - *Compile multiple patterns into a single case-insensitive regex.*
- `_python_rules` (line 209) `def _python_rules()` - *Return security rules for Python (.py).*
- `_javascript_rules` (line 307) `def _javascript_rules()` - *Return security rules for JavaScript/TypeScript (.js/.ts/.jsx/.tsx).*
- `_c_rules` (line 361) `def _c_rules()` - *Return security rules for C/C++ (.c/.cpp/.cc/.cxx/.h/.hpp/.hxx).*
- `_java_rules` (line 415) `def _java_rules()` - *Return security rules for Java (.java).*
- `_go_rules` (line 454) `def _go_rules()` - *Return security rules for Go (.go).*
- `_ruby_rules` (line 487) `def _ruby_rules()` - *Return security rules for Ruby (.rb).*
- `_php_rules` (line 529) `def _php_rules()` - *Return security rules for PHP (.php).*
- `_shell_rules` (line 590) `def _shell_rules()` - *Return security rules for Shell (.sh/.bash/.zsh).*
- `_csharp_rules` (line 620) `def _csharp_rules()` - *Return security rules for C# (.cs).*
- `_kotlin_rules` (line 659) `def _kotlin_rules()` - *Return security rules for Kotlin (.kt/.kts).*
- `_swift_rules` (line 686) `def _swift_rules()` - *Return security rules for Swift (.swift).*
- `_scala_rules` (line 713) `def _scala_rules()` - *Return security rules for Scala (.scala/.sc).*
- `_lua_rules` (line 741) `def _lua_rules()` - *Return security rules for Lua (.lua).*
- `_dart_rules` (line 765) `def _dart_rules()` - *Return security rules for Dart (.dart).*
- `_rust_rules` (line 797) `def _rust_rules()` - *Return security rules for Rust (.rs).*
- `_nim_rules` (line 830) `def _nim_rules()` - *Return security rules for Nim (.nim).*
- `_gdscript_rules` (line 858) `def _gdscript_rules()` - *Return security rules for GDScript (.gd).*
- `_elixir_rules` (line 882) `def _elixir_rules()` - *Return security rules for Elixir (.ex/.exs).*
- `__init__` (line 48) `def __init__(self, config)` - *Initialise with application configuration.

Args:
    config: Settings including SECURITY_ENABLED and
        SECURITY_SEVERITY_THRESHOLD.*
- `_build_rules` (line 59) `def _build_rules()` - *Build the complete per-language rule set.*
- `_meets_threshold` (line 96) `def _meets_threshold(self, severity)` - *Check if *severity* meets the configured threshold.*
- `scan` (line 103) `def scan(self, root)` - *Walk *root* and return all security findings.

Applies the same security checks as PolyglotScanner (symlinks,
ignore dirs, size limits, depth limits) for consistency.

Args:
    root: Project root directory to scan.

Returns:
    List of SecurityFinding instances, sorted by severity.*
- `_validate_path` (line 170) `def _validate_path(self, path, root)` - *Validate path security: reject symlinks and enforce limits.*
- `summary` (line 188) `def summary(self, findings)` - *Return a concise summary string of security findings.*

#### `_taint.py`
**Path:** `readmenator/_taint.py`

**Classes:**
- `TaintAnalyzer` (line 10) `class TaintAnalyzer` - *Propagation-based taint analysis over the resolved import graph.

Identifies files that import known-dangerous modules or functions
(sources) and traces how that danger propagates through the import
graph to files that never directly import the dangerous module
but receive taint through transitive dependencies.*

**Methods:**
- `__init__` (line 71) `def __init__(self, config)`
- `analyze` (line 75) `def analyze(self, nodes, edges, resolved_edges)` - *Run taint propagation analysis on the codebase.

Scans all nodes for direct dangerous imports, then propagates
taint through the resolved import graph. Returns all discovered
taint paths from sources to sinks.*
- `_find_direct_sources` (line 134) `def _find_direct_sources(self, nodes, edges)` - *Find files that directly import known-dangerous modules.*
- `_propagate` (line 160) `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` - *BFS propagation from source through the import graph.*
- `_build_forward_graph` (line 211) `def _build_forward_graph(nodes, resolved_edges)` - *Build a forward-directed import graph from resolved edges.*

#### `_watcher.py`
**Path:** `readmenator/_watcher.py`

**Classes:**
- `DirectoryWatcher` (line 21) `class DirectoryWatcher` - *Polling-based directory watcher for auto-rebuild on changes.

Computes a combined hash of all tracked files (filenames + sizes)
and triggers a callback when the hash changes. Uses polling to
avoid external dependencies like watchdog or inotify.*

**Methods:**
- `__init__` (line 29) `def __init__(self, root, config, callback, interval_seconds)` - *Initialise the watcher for a project root.

Args:
    root: Project directory to watch.
    config: Application configuration.
    callback: Function called when changes are detected.
    interval_seconds: Polling interval in seconds.*
- `_compute_snapshot` (line 51) `def _compute_snapshot(self)` - *Compute a quick hash of all tracked files in the project.

Uses file paths and sizes (not full content) for speed.
Returns a hex digest that changes when files are added,
removed, or modified.*
- `start` (line 80) `def start(self)` - *Start watching the directory (blocking).*
- `stop` (line 97) `def stop(self)` - *Stop watching.*

#### `__init__.py`
**Path:** `readmenator/parsers/__init__.py`

**Functions:**
- `_init_parser_map` (line 32) `def _init_parser_map()`
- `create_parser` (line 65) `def create_parser(extension, filename, config)` - *Factory: return a parser instance for the given file extension.*

#### `_assembly.py`
**Path:** `readmenator/parsers/_assembly.py`

**Classes:**
- `AssemblyParser` (line 9) `class AssemblyParser(LanguageParser)` - *Parser for assembly (.asm, .s, .S).

Extracts labels at the start of a line (``label:``) as function
symbols. This is a best-effort heuristic; local labels and
directives are not always distinguishable.*

**Methods:**
- `_extract_specifics` (line 17) `def _extract_specifics(self, content)`

#### `_base.py`
**Path:** `readmenator/parsers/_base.py`

**Classes:**
- `LanguageParser` (line 10) `class LanguageParser` - *Base class for all language-specific parsers.

Subclasses must implement ``_extract_specifics`` to populate
``self.symbols`` and ``self.imports``. Common utility methods
``_extract_docstring`` and ``_extract_signature`` are provided
for reuse across all parsers.*

**Methods:**
- `__init__` (line 19) `def __init__(self, filename, config)` - *Initialise the parser with a file path and application config.

Args:
    filename: Relative or absolute path of the source file.
    config: Application-wide configuration settings.*
- `parse` (line 34) `def parse(self, content)` - *Parse *content* and populate symbol/import lists.

Splits the source into lines, then delegates to the subclass-
specific ``_extract_specifics`` logic.*
- `_extract_specifics` (line 43) `def _extract_specifics(self, content)` - *Subclass hook for language-specific symbol extraction.*
- `_extract_docstring` (line 47) `def _extract_docstring(self, line_num)` - *Walk backwards from *line_num* to collect preceding comments/docstrings.

Supports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``
comment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``
from Config.*
- `_extract_signature` (line 89) `def _extract_signature(self, content, match_start, pattern)` - *Extract a compact signature snippet starting at *match_start*.

Scans forward to the opening brace or a fallback length,
then truncates to 100 characters for display.*

#### `_c.py`
**Path:** `readmenator/parsers/_c.py`

**Classes:**
- `CParser` (line 9) `class CParser(LanguageParser)` - *Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).

Extracts includes, structs, classes, functions, and preprocessor
macros using regex heuristics tuned to C-family syntax.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_csharp.py`
**Path:** `readmenator/parsers/_csharp.py`

**Classes:**
- `CSharpParser` (line 9) `class CSharpParser(LanguageParser)` - *Parser for C# (.cs).

Extracts ``using`` directives, class/struct/interface/record
declarations, and methods with access modifiers.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_dart.py`
**Path:** `readmenator/parsers/_dart.py`

**Classes:**
- `DartParser` (line 9) `class DartParser(LanguageParser)` - *Parser for Dart (.dart).

Extracts import statements, class declarations (with extends),
and top-level or method function declarations by return type.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_elixir.py`
**Path:** `readmenator/parsers/_elixir.py`

**Classes:**
- `ElixirParser` (line 9) `class ElixirParser(LanguageParser)` - *Parser for Elixir (.ex, .exs).

Extracts ``import``/``alias``/``require``/``use`` directives,
module definitions, and named function definitions.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_gdscript.py`
**Path:** `readmenator/parsers/_gdscript.py`

**Classes:**
- `GDScriptParser` (line 9) `class GDScriptParser(LanguageParser)` - *Parser for Godot GDScript (.gd).

Extracts ``extends`` / ``class_name`` directives and ``func``
method declarations.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_go.py`
**Path:** `readmenator/parsers/_go.py`

**Classes:**
- `GoParser` (line 9) `class GoParser(LanguageParser)` - *Parser for Go (.go).

Extracts import blocks or single import statements, exported
functions (including methods), and type definitions (struct/interface).*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_java.py`
**Path:** `readmenator/parsers/_java.py`

**Classes:**
- `JavaParser` (line 9) `class JavaParser(LanguageParser)` - *Parser for Java (.java).

Extracts import statements, class and interface declarations,
and methods complete with access modifiers and type signatures.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_javascript.py`
**Path:** `readmenator/parsers/_javascript.py`

**Classes:**
- `JavaScriptParser` (line 9) `class JavaScriptParser(LanguageParser)` - *Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).

Extracts ES module imports, CommonJS ``require`` calls, function
declarations, arrow-function variables, and class definitions
(including inheritance).*

**Methods:**
- `_extract_specifics` (line 17) `def _extract_specifics(self, content)`

#### `_kotlin.py`
**Path:** `readmenator/parsers/_kotlin.py`

**Classes:**
- `KotlinParser` (line 9) `class KotlinParser(LanguageParser)` - *Parser for Kotlin (.kt, .kts).

Extracts ``import`` statements, class/object/interface/data class
declarations, and function definitions.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_lua.py`
**Path:** `readmenator/parsers/_lua.py`

**Classes:**
- `LuaParser` (line 9) `class LuaParser(LanguageParser)` - *Parser for Lua (.lua).

Extracts ``require`` imports, function declarations (named and
table-based), and module returns.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_nim.py`
**Path:** `readmenator/parsers/_nim.py`

**Classes:**
- `NimParser` (line 9) `class NimParser(LanguageParser)` - *Parser for Nim (.nim).

Extracts ``import`` statements, ``proc`` / ``func`` / ``method``
declarations, and ``type`` definitions.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_php.py`
**Path:** `readmenator/parsers/_php.py`

**Classes:**
- `PHPParser` (line 9) `class PHPParser(LanguageParser)` - *Parser for PHP (.php).

Extracts ``use/require/include`` (including ``_once`` variants),
function declarations, and class declarations.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_python.py`
**Path:** `readmenator/parsers/_python.py`

**Classes:**
- `PythonParser` (line 10) `class PythonParser(LanguageParser)` - *Parser for Python (.py) using the native ``ast`` module.

Extracts imports, functions (including async), and class
definitions with docstrings via ``ast.get_docstring``.*

**Methods:**
- `_extract_specifics` (line 17) `def _extract_specifics(self, content)`

#### `_ruby.py`
**Path:** `readmenator/parsers/_ruby.py`

**Classes:**
- `RubyParser` (line 9) `class RubyParser(LanguageParser)` - *Parser for Ruby (.rb).

Extracts ``require`` / ``require_relative`` imports, class and
module definitions with inheritance, and method definitions.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_rust.py`
**Path:** `readmenator/parsers/_rust.py`

**Classes:**
- `RustParser` (line 9) `class RustParser(LanguageParser)` - *Parser for Rust (.rs).

Extracts ``use`` imports, public and private functions,
structs, traits, and enums.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_scala.py`
**Path:** `readmenator/parsers/_scala.py`

**Classes:**
- `ScalaParser` (line 9) `class ScalaParser(LanguageParser)` - *Parser for Scala (.scala).

Extracts ``import`` statements, class/object/trait declarations,
and method definitions.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_shell.py`
**Path:** `readmenator/parsers/_shell.py`

**Classes:**
- `ShellParser` (line 9) `class ShellParser(LanguageParser)` - *Parser for shell scripts (.sh, .bash, .zsh).

Extracts function declarations in both POSIX (``name() {``)
and ``function`` keyword syntax.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `_swift.py`
**Path:** `readmenator/parsers/_swift.py`

**Classes:**
- `SwiftParser` (line 9) `class SwiftParser(LanguageParser)` - *Parser for Swift (.swift).

Extracts ``import`` statements, class/struct/enum/protocol
declarations with inheritance, and function definitions.*

**Methods:**
- `_extract_specifics` (line 16) `def _extract_specifics(self, content)`

#### `readmenator.py`
**Path:** `readmenator.py`

*No symbols extracted*

#### `readmenator_orchestrator.py`
**Path:** `readmenator_orchestrator.py`

**Classes:**
- `Config` (line 21) `class Config`
- `GitHubClient` (line 70) `class GitHubClient`
- `RepositoryProcessor` (line 184) `class RepositoryProcessor`
- `Orchestrator` (line 326) `class Orchestrator`
- `TestOrchestrator` (line 381) `class TestOrchestrator(TestCase)`

**Methods:**
- `_validate_repo_name` (line 43) `def _validate_repo_name(name)`
- `_validate_branch_name` (line 49) `def _validate_branch_name(name)`
- `_safe_env` (line 55) `def _safe_env()`
- `parse_arguments` (line 422) `def parse_arguments()`
- `main` (line 439) `def main()`
- `__init__` (line 71) `def __init__(self, config)`
- `_resolve_user` (line 76) `def _resolve_user(self)`
- `_setup_git_auth` (line 97) `def _setup_git_auth(self)`
- `list_repos` (line 111) `def list_repos(self)`
- `close_existing_prs` (line 123) `def close_existing_prs(self, repo)`
- `delete_remote_branch` (line 151) `def delete_remote_branch(self, repo)`
- `create_pr` (line 163) `def create_pr(self, repo, default_branch, timestamp)`
- `__init__` (line 185) `def __init__(self, config, github_client)`
- `process` (line 189) `def process(self, repo)`
- `_get_default_branch` (line 218) `def _get_default_branch(self, repo)`
- `_clone_repository` (line 234) `def _clone_repository(self, repo)`
- `_run_readmenator` (line 250) `def _run_readmenator(self, repo_dir)`
- `_copy_to_docs_dir` (line 271) `def _copy_to_docs_dir(repo_dir, generated_file)`
- `_commit_and_push` (line 277) `def _commit_and_push(self, repo_dir, repo)`
- `_cleanup_temp_dir` (line 321) `def _cleanup_temp_dir(temp_dir)`
- `__init__` (line 327) `def __init__(self, config)`
- `run` (line 332) `def run(self, dry_run, only_repo)`
- `setUp` (line 382) `def setUp(self)`
- `tearDown` (line 386) `def tearDown(self)`
- `test_config_immutability` (line 389) `def test_config_immutability(self)`
- `test_config_defaults` (line 393) `def test_config_defaults(self)`
- `test_skip_repos_logic` (line 399) `def test_skip_repos_logic(self)`
- `test_repo_name_validation` (line 403) `def test_repo_name_validation(self)`
- `test_branch_name_validation` (line 413) `def test_branch_name_validation(self)`

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
- `test_ignore_dirs_are_comprehensive` (line 24) `def test_ignore_dirs_are_comprehensive(self)`
- `test_plural_map_covers_all_symbol_types` (line 30) `def test_plural_map_covers_all_symbol_types(self)`
- `test_supported_extensions_no_duplicates` (line 41) `def test_supported_extensions_no_duplicates(self)`

#### `test_cpg.py`
**Path:** `tests/test_cpg.py`

**Classes:**
- `TestCodePropertyGraphContract` (line 11) `class TestCodePropertyGraphContract(TestCase)` - *Contract: CodePropertyGraph generates valid JSON-LD CPG output.*

**Methods:**
- `setUp` (line 14) `def setUp(self)`
- `_make_node` (line 18) `def _make_node(self, nid, label, lang)`
- `_make_sym` (line 21) `def _make_sym(self, name, kind, line)`
- `test_generate_returns_valid_json` (line 24) `def test_generate_returns_valid_json(self)`
- `test_generate_includes_node_data` (line 33) `def test_generate_includes_node_data(self)`
- `test_generate_includes_edges` (line 49) `def test_generate_includes_edges(self)`
- `test_generate_includes_metadata` (line 61) `def test_generate_includes_metadata(self)`
- `test_privacy_mode_strips_docs` (line 71) `def test_privacy_mode_strips_docs(self)`
- `test_sha256_hash_included` (line 89) `def test_sha256_hash_included(self)`
- `test_empty_graph_returns_valid_json` (line 96) `def test_empty_graph_returns_valid_json(self)`

#### `test_documentation.py`
**Path:** `tests/test_documentation.py`

**Classes:**
- `TestDocumentationGeneratorContract` (line 17) `class TestDocumentationGeneratorContract(TestCase)`

**Methods:**
- `setUp` (line 18) `def setUp(self)`
- `test_contains_header` (line 22) `def test_contains_header(self)`
- `test_contains_metadata_line` (line 26) `def test_contains_metadata_line(self)`
- `test_contains_mermaid_block` (line 32) `def test_contains_mermaid_block(self)`
- `test_contains_architecture_reference` (line 37) `def test_contains_architecture_reference(self)`
- `test_contains_cpg_block` (line 41) `def test_contains_cpg_block(self)`
- `test_contains_statistics_dashboard` (line 46) `def test_contains_statistics_dashboard(self)`
- `test_groups_files_by_language` (line 51) `def test_groups_files_by_language(self)`
- `test_lists_symbols_under_file` (line 70) `def test_lists_symbols_under_file(self)`
- `test_class_symbol_is_pluralized_correctly` (line 83) `def test_class_symbol_is_pluralized_correctly(self)`
- `test_function_pluralization` (line 97) `def test_function_pluralization(self)`
- `test_method_pluralization` (line 109) `def test_method_pluralization(self)`
- `test_shows_no_symbols_for_empty_files` (line 121) `def test_shows_no_symbols_for_empty_files(self)`
- `test_includes_file_path` (line 132) `def test_includes_file_path(self)`
- `test_docstring_in_output` (line 143) `def test_docstring_in_output(self)`
- `test_truncation_note_when_limited` (line 155) `def test_truncation_note_when_limited(self)`
- `test_taint_propagation_section_present` (line 165) `def test_taint_propagation_section_present(self)`
- `test_hotspot_section_present` (line 185) `def test_hotspot_section_present(self)`
- `test_no_taint_section_when_empty` (line 203) `def test_no_taint_section_when_empty(self)`
- `test_no_hotspot_section_when_empty` (line 207) `def test_no_hotspot_section_when_empty(self)`
- `test_cpg_block_disabled_via_config` (line 211) `def test_cpg_block_disabled_via_config(self)`
- `test_architectural_layers_section` (line 217) `def test_architectural_layers_section(self)`
- `test_security_findings_section` (line 229) `def test_security_findings_section(self)`

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

#### `test_hotspots.py`
**Path:** `tests/test_hotspots.py`

**Classes:**
- `TestHotspotAnalyzerContract` (line 10) `class TestHotspotAnalyzerContract(TestCase)` - *Contract: HotspotAnalyzer detects hotspots, cycles, and change impact.*

**Methods:**
- `setUp` (line 13) `def setUp(self)`
- `_make_node` (line 17) `def _make_node(self, nid, label, sym_count)`
- `test_empty_graph_returns_empty_hotspots` (line 29) `def test_empty_graph_returns_empty_hotspots(self)`
- `test_hotspots_rank_by_combined_score` (line 33) `def test_hotspots_rank_by_combined_score(self)`
- `test_hotspot_includes_scores` (line 43) `def test_hotspot_includes_scores(self)`
- `test_no_cycles_in_acyclic_graph` (line 53) `def test_no_cycles_in_acyclic_graph(self)`
- `test_detects_simple_cycle` (line 66) `def test_detects_simple_cycle(self)`
- `test_change_impact_ranks_by_total_impact` (line 79) `def test_change_impact_ranks_by_total_impact(self)`
- `test_change_impact_no_edges` (line 94) `def test_change_impact_no_edges(self)`
- `test_hotspot_weights_from_config` (line 100) `def test_hotspot_weights_from_config(self)`

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
- `test_knowledge_base_contains_cpg` (line 81) `def test_knowledge_base_contains_cpg(self)`
- `test_knowledge_base_contains_statistics_dashboard` (line 89) `def test_knowledge_base_contains_statistics_dashboard(self)`
- `test_audit_deep_returns_analysis` (line 98) `def test_audit_deep_returns_analysis(self)`
- `test_privacy_mode_works` (line 105) `def test_privacy_mode_works(self)`
- `test_export_sarif_produces_file` (line 114) `def test_export_sarif_produces_file(self)`

#### `test_layer_rules.py`
**Path:** `tests/test_layer_rules.py`

**Classes:**
- `TestLayerRuleEngineContract` (line 10) `class TestLayerRuleEngineContract(TestCase)` - *Contract: LayerRuleEngine detects architectural layer violations.*

**Methods:**
- `setUp` (line 13) `def setUp(self)`
- `_make_node` (line 17) `def _make_node(self, nid, label)`
- `test_empty_graph_returns_empty_violations` (line 20) `def test_empty_graph_returns_empty_violations(self)`
- `test_no_layers_returns_empty_violations` (line 24) `def test_no_layers_returns_empty_violations(self)`
- `test_same_layer_no_violation` (line 29) `def test_same_layer_no_violation(self)`
- `test_forbidden_edge_detected` (line 36) `def test_forbidden_edge_detected(self)`
- `test_allowed_testing_edges_no_violation` (line 46) `def test_allowed_testing_edges_no_violation(self)`
- `test_multiple_violations` (line 57) `def test_multiple_violations(self)`
- `test_utility_layer_ignored` (line 75) `def test_utility_layer_ignored(self)`
- `test_violation_summary` (line 82) `def test_violation_summary(self)`
- `test_resolved_edges_also_checked` (line 104) `def test_resolved_edges_also_checked(self)`
- `test_presentation_to_data_access_forbidden` (line 115) `def test_presentation_to_data_access_forbidden(self)`

#### `test_mermaid.py`
**Path:** `tests/test_mermaid.py`

**Classes:**
- `TestMermaidRendererContract` (line 7) `class TestMermaidRendererContract(TestCase)`

**Methods:**
- `setUp` (line 8) `def setUp(self)`
- `test_renders_graph_header` (line 11) `def test_renders_graph_header(self)`
- `test_renders_module_node` (line 19) `def test_renders_module_node(self)`
- `test_renders_symbol_subnodes` (line 27) `def test_renders_symbol_subnodes(self)`
- `test_class_symbol_gets_cls_style` (line 36) `def test_class_symbol_gets_cls_style(self)`
- `test_function_symbol_gets_fn_style` (line 45) `def test_function_symbol_gets_fn_style(self)`
- `test_external_import_edge_is_dashed` (line 54) `def test_external_import_edge_is_dashed(self)`
- `test_truncation_when_over_limit` (line 62) `def test_truncation_when_over_limit(self)`
- `test_limits_symbols_to_five_per_node` (line 72) `def test_limits_symbols_to_five_per_node(self)`
- `test_handles_special_characters_in_ids` (line 82) `def test_handles_special_characters_in_ids(self)`

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

#### `test_rule_gen.py`
**Path:** `tests/test_rule_gen.py`

**Classes:**
- `TestRuleGeneratorContract` (line 12) `class TestRuleGeneratorContract(TestCase)` - *Contract: RuleGenerator detects patterns and suggests rules.*

**Methods:**
- `setUp` (line 15) `def setUp(self)`
- `_make_node` (line 19) `def _make_node(self, nid, label, lang)`
- `_make_node_with_symbols` (line 29) `def _make_node_with_symbols(self, nid, sym_count)`
- `test_empty_nodes_returns_empty_rules` (line 44) `def test_empty_nodes_returns_empty_rules(self)`
- `test_generates_rules_for_function_heavy_language` (line 48) `def test_generates_rules_for_function_heavy_language(self)`
- `test_detects_antipatterns_with_content` (line 56) `def test_detects_antipatterns_with_content(self)`
- `test_antipattern_threshold_from_config` (line 67) `def test_antipattern_threshold_from_config(self)`
- `test_write_rules_creates_files` (line 77) `def test_write_rules_creates_files(self)`
- `test_rule_id_increments` (line 90) `def test_rule_id_increments(self)`

#### `test_sarif.py`
**Path:** `tests/test_sarif.py`

**Classes:**
- `TestSarifExporterContract` (line 11) `class TestSarifExporterContract(TestCase)` - *Contract: SarifExporter produces valid SARIF v2.1.0 JSON.*

**Methods:**
- `setUp` (line 14) `def setUp(self)`
- `_make_finding` (line 18) `def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)`
- `test_export_returns_valid_json` (line 38) `def test_export_returns_valid_json(self)`
- `test_export_includes_tool_info` (line 46) `def test_export_includes_tool_info(self)`
- `test_export_includes_rule` (line 54) `def test_export_includes_rule(self)`
- `test_export_includes_result` (line 62) `def test_export_includes_result(self)`
- `test_severity_maps_correctly` (line 73) `def test_severity_maps_correctly(self)`
- `test_privacy_mode_strips_snippets` (line 88) `def test_privacy_mode_strips_snippets(self)`
- `test_empty_findings_produces_valid_sarif` (line 97) `def test_empty_findings_produces_valid_sarif(self)`

#### `test_scanner.py`
**Path:** `tests/test_scanner.py`

**Classes:**
- `TestScannerContract` (line 11) `class TestScannerContract(TestCase)`

**Methods:**
- `setUp` (line 12) `def setUp(self)`
- `tearDown` (line 16) `def tearDown(self)`
- `_write` (line 20) `def _write(self, path, content)`
- `test_scans_python_files` (line 25) `def test_scans_python_files(self)`
- `test_ignores_env_and_vendor_dirs` (line 32) `def test_ignores_env_and_vendor_dirs(self)`
- `test_rejects_symlinks` (line 45) `def test_rejects_symlinks(self)`
- `test_skips_non_code_files` (line 59) `def test_skips_non_code_files(self)`
- `test_scans_multiple_languages` (line 70) `def test_scans_multiple_languages(self)`
- `test_respects_max_directory_depth` (line 79) `def test_respects_max_directory_depth(self)`
- `test_raises_on_invalid_directory` (line 89) `def test_raises_on_invalid_directory(self)`
- `test_import_edges_are_created` (line 94) `def test_import_edges_are_created(self)`
- `test_privacy_mode_strips_docs` (line 104) `def test_privacy_mode_strips_docs(self)`
- `test_scan_with_content_returns_content_map` (line 114) `def test_scan_with_content_returns_content_map(self)`
- `test_gitignore_respected_when_enabled` (line 122) `def test_gitignore_respected_when_enabled(self)`
- `test_gitignore_disabled_by_default` (line 133) `def test_gitignore_disabled_by_default(self)`
- `test_gitignore_glob_conversion` (line 142) `def test_gitignore_glob_conversion(self)`

#### `test_security.py`
**Path:** `tests/test_security.py`

**Classes:**
- `TestSecurityFinding` (line 21) `class TestSecurityFinding(TestCase)` - *SecurityFinding dataclass contract tests.*
- `TestSecurityAnalyzerConfig` (line 43) `class TestSecurityAnalyzerConfig(TestCase)` - *SecurityAnalyzer configuration contract tests.*
- `TestSecurityAnalyzerRules` (line 64) `class TestSecurityAnalyzerRules(TestCase)` - *Per-language rule detection tests using inline code.*
- `TestSecurityAnalyzerThreshold` (line 295) `class TestSecurityAnalyzerThreshold(TestCase)` - *Severity threshold filtering tests.*
- `TestSecurityAnalyzerPathValidation` (line 327) `class TestSecurityAnalyzerPathValidation(TestCase)` - *Security path validation tests.*
- `TestSecurityAnalyzerSummary` (line 374) `class TestSecurityAnalyzerSummary(TestCase)` - *Security summary output tests.*

**Methods:**
- `test_security_finding_fields` (line 24) `def test_security_finding_fields(self)`
- `test_default_config_disables_security` (line 46) `def test_default_config_disables_security(self)`
- `test_default_severity_threshold` (line 50) `def test_default_severity_threshold(self)`
- `test_default_security_output` (line 54) `def test_default_security_output(self)`
- `test_init_with_config` (line 58) `def test_init_with_config(self)`
- `setUp` (line 67) `def setUp(self)`
- `_scan_content` (line 71) `def _scan_content(self, content, extension)` - *Write content to a temp file and scan it.*
- `test_python_os_system` (line 78) `def test_python_os_system(self)`
- `test_python_eval` (line 83) `def test_python_eval(self)`
- `test_python_pickle` (line 88) `def test_python_pickle(self)`
- `test_python_sql_injection` (line 93) `def test_python_sql_injection(self)`
- `test_python_hardcoded_secret` (line 98) `def test_python_hardcoded_secret(self)`
- `test_python_weak_crypto` (line 103) `def test_python_weak_crypto(self)`
- `test_python_request_verify_false` (line 108) `def test_python_request_verify_false(self)`
- `test_python_flask_debug` (line 113) `def test_python_flask_debug(self)`
- `test_python_yaml_load` (line 118) `def test_python_yaml_load(self)`
- `test_javascript_inner_html` (line 123) `def test_javascript_inner_html(self)`
- `test_javascript_eval` (line 128) `def test_javascript_eval(self)`
- `test_javascript_child_process` (line 133) `def test_javascript_child_process(self)`
- `test_javascript_dangerously_set_inner_html` (line 138) `def test_javascript_dangerously_set_inner_html(self)`
- `test_c_strcpy` (line 143) `def test_c_strcpy(self)`
- `test_c_gets` (line 148) `def test_c_gets(self)`
- `test_c_system` (line 153) `def test_c_system(self)`
- `test_java_runtime_exec` (line 158) `def test_java_runtime_exec(self)`
- `test_java_sql_injection` (line 163) `def test_java_sql_injection(self)`
- `test_go_exec_command` (line 168) `def test_go_exec_command(self)`
- `test_ruby_eval` (line 173) `def test_ruby_eval(self)`
- `test_ruby_marshal_load` (line 178) `def test_ruby_marshal_load(self)`
- `test_php_eval` (line 183) `def test_php_eval(self)`
- `test_php_sql_injection` (line 188) `def test_php_sql_injection(self)`
- `test_php_unseralize` (line 193) `def test_php_unseralize(self)`
- `test_shell_eval` (line 198) `def test_shell_eval(self)`
- `test_csharp_process_start` (line 203) `def test_csharp_process_start(self)`
- `test_kotlin_runtime_exec` (line 208) `def test_kotlin_runtime_exec(self)`
- `test_swift_process` (line 213) `def test_swift_process(self)`
- `test_lua_load` (line 218) `def test_lua_load(self)`
- `test_lua_os_execute` (line 223) `def test_lua_os_execute(self)`
- `test_dart_process_run` (line 228) `def test_dart_process_run(self)`
- `test_rust_unsafe` (line 233) `def test_rust_unsafe(self)`
- `test_elixir_code_eval` (line 238) `def test_elixir_code_eval(self)`
- `test_elixir_system_cmd` (line 243) `def test_elixir_system_cmd(self)`
- `test_gdscript_os_execute` (line 248) `def test_gdscript_os_execute(self)`
- `test_scala_runtime_exec` (line 253) `def test_scala_runtime_exec(self)`
- `test_nim_exec_process` (line 258) `def test_nim_exec_process(self)`
- `test_safe_code_produces_no_findings` (line 263) `def test_safe_code_produces_no_findings(self)`
- `test_csharp_binary_formatter` (line 274) `def test_csharp_binary_formatter(self)`
- `test_ruby_backtick` (line 279) `def test_ruby_backtick(self)`
- `test_php_xss` (line 284) `def test_php_xss(self)`
- `test_go_unsafe_package` (line 289) `def test_go_unsafe_package(self)`
- `test_threshold_filters_low` (line 298) `def test_threshold_filters_low(self)`
- `test_threshold_info_shows_all` (line 312) `def test_threshold_info_shows_all(self)`
- `test_ignores_symlinks` (line 330) `def test_ignores_symlinks(self)`
- `test_ignores_ignored_dirs` (line 345) `def test_ignores_ignored_dirs(self)`
- `test_empty_directory` (line 357) `def test_empty_directory(self)`
- `test_unsupported_extension` (line 364) `def test_unsupported_extension(self)`
- `test_summary_empty` (line 377) `def test_summary_empty(self)`
- `test_summary_with_findings` (line 383) `def test_summary_with_findings(self)`

#### `test_taint.py`
**Path:** `tests/test_taint.py`

**Classes:**
- `TestTaintAnalyzerContract` (line 10) `class TestTaintAnalyzerContract(TestCase)` - *Contract: TaintAnalyzer discovers taint propagation paths.*

**Methods:**
- `setUp` (line 13) `def setUp(self)`
- `_make_node` (line 17) `def _make_node(self, nid, label)`
- `test_empty_graph_returns_empty_result` (line 20) `def test_empty_graph_returns_empty_result(self)`
- `test_no_dangerous_imports_returns_empty` (line 25) `def test_no_dangerous_imports_returns_empty(self)`
- `test_direct_dangerous_import_found` (line 31) `def test_direct_dangerous_import_found(self)`
- `test_taint_propagates_through_resolved_edges` (line 38) `def test_taint_propagates_through_resolved_edges(self)`
- `test_dangerous_import_by_language` (line 62) `def test_dangerous_import_by_language(self)`
- `test_taint_path_has_severity` (line 70) `def test_taint_path_has_severity(self)`
- `test_max_depth_limits_propagation` (line 77) `def test_max_depth_limits_propagation(self)`
