# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 98 | **Total Symbols Extracted:** 1214 | **Total Imports:** 552
 | **Resolved Imports:** 266

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:75d209c | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Community Analysis](#community-analysis)
6. [Surprising Connections](#surprising-connections)
7. [Suggested Questions](#suggested-questions)
8. [Taint Propagation Map](#taint-propagation-map)
9. [Hotspot Analysis](#hotspot-analysis)
10. [Dependency Cycles](#dependency-cycles)
11. [Change Impact Analysis](#change-impact-analysis)
12. [Suggested Linting Rules](#suggested-linting-rules)
13. [Orphans](#orphans)
14. [Query Recipes](#query-recipes)
15. [Structural Knowledge Map](#structural-knowledge-map)
16. [UML Class Diagram](#uml-class-diagram)
17. [Code Property Graph](#code-property-graph)
18. [Architecture Reference](#architecture-reference)
    - [PY (88 files)](#py-88-files)
    - [SH (10 files)](#sh-10-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 98 |
| Total Symbols | 1214 |
| Total Imports | 552 |
| Call Edges | 6166 |
| Inheritance Edges | 92 |
| Languages | 2 |
| Avg Symbols/File | 12.4 |
| Avg Imports/File | 5.6 |
| Resolved Imports | 266 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `test_parsers_property.py` | 26 | 16 | py |
| `__init__.py` | 23 | 2 | py |
| `_pipeline.py` | 20 | 23 | py |
| `_app.py` | 17 | 37 | py |
| `readmenator_orchestrator.py` | 14 | 34 | py |
| `__main__.py` | 11 | 3 | py |
| `_mcp_server.py` | 11 | 52 | py |
| `test_taint_bdd.py` | 11 | 26 | py |
| `_documentation.py` | 10 | 27 | py |
| `_exporter.py` | 10 | 15 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 54 |
| testing | 36 |
| business_logic | 4 |
| infrastructure | 3 |
| data_access | 1 |

### utility

- `.refactor__app.sh` (sh, 0 symbols)
- `.refactor__documentation.sh` (sh, 0 symbols)
- `.refactor__exporter.sh` (sh, 0 symbols)
- `.refactor__mcp_server.sh` (sh, 0 symbols)
- `.refactor__rank.sh` (sh, 0 symbols)
- `.refactor__security.sh` (sh, 0 symbols)
- `.refactor__uml.sh` (sh, 0 symbols)
- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `_analyzer.py` (py, 13 symbols)
- `_app.py` (py, 37 symbols)
- `_category.py` (py, 26 symbols)
- `_cpg.py` (py, 6 symbols)
- `_dead_code.py` (py, 5 symbols)
- `_documentation.py` (py, 27 symbols)
- *... and 39 more*

### testing

- `.refactor_test_parsers.sh` (sh, 0 symbols)
- `.refactor_test_ranking.sh` (sh, 0 symbols)
- `.refactor_test_uml.sh` (sh, 0 symbols)
- `__main__.py` (py, 3 symbols)
- `readmenator_orchestrator.py` (py, 34 symbols)
- `__init__.py` (py, 0 symbols)
- `test_analyzer.py` (py, 12 symbols)
- `test_cache.py` (py, 22 symbols)
- `test_config.py` (py, 6 symbols)
- `test_cpg.py` (py, 11 symbols)
- `test_cursorrules.py` (py, 12 symbols)
- `test_dead_code.py` (py, 15 symbols)
- `test_documentation.py` (py, 29 symbols)
- `test_exporter.py` (py, 15 symbols)
- `test_hotspots.py` (py, 11 symbols)
- *... and 21 more*

### infrastructure

- `_cache.py` (py, 13 symbols)
- `_config.py` (py, 1 symbols)
- `_readme_injector.py` (py, 6 symbols)

### business_logic

- `_cursorrules_generator.py` (py, 8 symbols)
- `_layer_rules.py` (py, 4 symbols)
- `_models.py` (py, 19 symbols)
- `_rule_gen.py` (py, 9 symbols)

### data_access

- `_query.py` (py, 17 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `_models.py` | 0.3356 | 0.3658 | 0.3549 | 0.00 | 1.00 |
| 2 | `_category.py` | 0.2570 | 0.3289 | 0.3140 | 0.00 | 0.46 |
| 3 | `_config.py` | 0.1341 | 0.0502 | 0.0578 | 0.00 | 1.00 |
| 4 | `_layers.py` | 0.1056 | 0.0100 | 0.0056 | 0.00 | 1.00 |
| 5 | `_rule_gen.py` | 0.1054 | 0.0353 | 0.0032 | 0.00 | 0.89 |
| 6 | `_base.py` | 0.1049 | 0.0000 | 0.0247 | 0.00 | 1.00 |
| 7 | `_resolver.py` | 0.1011 | 0.0000 | 0.0053 | 0.00 | 1.00 |
| 8 | `_query.py` | 0.1009 | 0.0000 | 0.0045 | 0.00 | 1.00 |
| 9 | `_scanner.py` | 0.1007 | 0.0000 | 0.0036 | 0.00 | 1.00 |
| 10 | `_analyzer.py` | 0.1006 | 0.0000 | 0.0032 | 0.00 | 1.00 |

**Query anchors:** readmenator/_documentation.py, readmenator/_linter.py, tests/test_rule_gen.py, tests/test_linter.py, tests/test_documentation.py, readmenator/_rule_gen.py, tests/test_ranking.py

**Top result justification paths:**

  `_documentation.py -> _cpg.py -> _models.py`
  `_documentation.py -> _mermaid.py -> _models.py`

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `_models.py` | 135.9 | | 0.3549 |
| `_config.py` | 94.1 | | 0.0578 |
| `__init__.py` | 48.2 | | 0.0000 |
| `_base.py` | 44.6 | | 0.0247 |
| `test_parsers_property.py` | 41.6 | | 0.0000 |
| `_pipeline.py` | 40.3 | | 0.0000 |
| `_app.py` | 39.7 | | 0.0000 |
| `_mcp_server.py` | 21.2 | | 0.0000 |
| `_documentation.py` | 18.7 | | 0.0000 |
| `_category.py` | 18.6 | | 0.3140 |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### readmenator (Cohesion: 0.86)

**62 files** in this community:

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `__main__.py` (py, 3 symbols)
- `_analyzer.py` (py, 13 symbols)
- `_app.py` (py, 37 symbols)
- `_cache.py` (py, 13 symbols)
- `_category.py` (py, 26 symbols)
- `_config.py` (py, 1 symbols)
- `_cpg.py` (py, 6 symbols)
- `_cursorrules_generator.py` (py, 8 symbols)
- `_dead_code.py` (py, 5 symbols)
- `_documentation.py` (py, 27 symbols)
- `_explain.py` (py, 3 symbols)
- `_exporter.py` (py, 15 symbols)
- `_hotspots.py` (py, 7 symbols)
- `_layer_rules.py` (py, 4 symbols)
- `_layers.py` (py, 4 symbols)
- `_linter.py` (py, 7 symbols)
- `_mcp_server.py` (py, 52 symbols)
- `_mermaid.py` (py, 4 symbols)
- ... and 42 more files

### readmenator/parsers (Cohesion: 0.69)

**24 files** in this community:

- `__init__.py` (py, 2 symbols)
- `_assembly.py` (py, 2 symbols)
- `_base.py` (py, 6 symbols)
- `_c.py` (py, 2 symbols)
- `_csharp.py` (py, 2 symbols)
- `_dart.py` (py, 2 symbols)
- `_elixir.py` (py, 2 symbols)
- `_gdscript.py` (py, 2 symbols)
- `_go.py` (py, 2 symbols)
- `_java.py` (py, 2 symbols)
- `_javascript.py` (py, 2 symbols)
- `_kotlin.py` (py, 2 symbols)
- `_lua.py` (py, 2 symbols)
- `_nim.py` (py, 2 symbols)
- `_php.py` (py, 2 symbols)
- `_python.py` (py, 2 symbols)
- `_ruby.py` (py, 2 symbols)
- `_rust.py` (py, 2 symbols)
- `_scala.py` (py, 2 symbols)
- `_shell.py` (py, 2 symbols)
- ... and 4 more files

---

## Surprising Connections

Files in different communities connected through 3+ indirect hops.

- `_explain.py` <-> `__init__.py` (4 hops, across 2 communities)
- `_explain.py` <-> `test_parsers.py` (4 hops, across 2 communities)
- `_explain.py` <-> `test_parsers_new.py` (4 hops, across 2 communities)
- `_projections.py` <-> `test_parsers.py` (4 hops, across 2 communities)
- `_projections.py` <-> `test_parsers_new.py` (4 hops, across 2 communities)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does _models.py depend on, and what depends on it? (67 connections)
- What does _config.py depend on, and what depends on it? (47 connections)
- What does __init__.py depend on, and what depends on it? (24 connections)
- How are the 62 files in 'readmenator' related to each other?
- Why are _explain.py and __init__.py connected through 4 hops across 2 communities?

---

## Taint Propagation Map

Taint analysis traces how dangerous imports propagate through the codebase via transitive dependencies. Source files import dangerous modules directly; sink files receive the danger indirectly.

**Taint Sources:** 2 | **Taint Sinks:** 9 | **Propagation Paths:** 9

- `_documentation.py` imports `subprocess` (0 hop to `_documentation.py`) [high]
  Path: _documentation.py
- `_documentation.py` imports `subprocess` (1 hop to `_rank.py`) [high]
  Path: _documentation.py -> _rank.py
- `_documentation.py` imports `subprocess` (1 hop to `_cpg.py`) [high]
  Path: _documentation.py -> _cpg.py
- `_documentation.py` imports `subprocess` (1 hop to `_config.py`) [high]
  Path: _documentation.py -> _config.py
- `_documentation.py` imports `subprocess` (1 hop to `_uml.py`) [high]
  Path: _documentation.py -> _uml.py
- `_documentation.py` imports `subprocess` (1 hop to `_models.py`) [high]
  Path: _documentation.py -> _models.py
- `_documentation.py` imports `subprocess` (1 hop to `_mermaid.py`) [high]
  Path: _documentation.py -> _mermaid.py
- `_documentation.py` imports `subprocess` (2 hops to `_category.py`) [high]
  Path: _documentation.py -> _rank.py -> _category.py
- `readmenator_orchestrator.py` imports `subprocess` (0 hop to `readmenator_orchestrator.py`) [high]
  Path: readmenator_orchestrator.py

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `_models.py` | 0.226 | 1.000 | 0.691 | 19 | 79 |
| `_category.py` | 0.309 | 0.177 | 0.230 | 26 | 14 |
| `_config.py` | 0.012 | 0.658 | 0.400 | 1 | 52 |
| `_layers.py` | 0.048 | 0.114 | 0.087 | 4 | 9 |
| `_rule_gen.py` | 0.107 | 0.152 | 0.134 | 9 | 12 |
| `_base.py` | 0.071 | 0.342 | 0.234 | 6 | 27 |
| `_resolver.py` | 0.131 | 0.089 | 0.105 | 11 | 7 |
| `_query.py` | 0.202 | 0.152 | 0.172 | 17 | 12 |
| `_scanner.py` | 0.155 | 0.177 | 0.168 | 13 | 14 |
| `_analyzer.py` | 0.155 | 0.127 | 0.138 | 13 | 10 |
| `test_parsers.py` | 1.000 | 0.076 | 0.446 | 84 | 6 |
| `_app.py` | 0.441 | 0.443 | 0.442 | 37 | 35 |
| `test_ranking.py` | 0.857 | 0.165 | 0.442 | 72 | 13 |
| `test_parsers_property.py` | 0.191 | 0.582 | 0.426 | 16 | 46 |
| `_pipeline.py` | 0.274 | 0.494 | 0.406 | 23 | 39 |

---

## Dependency Cycles

Circular dependencies detected in the resolved import graph. Cycles increase coupling and make refactoring harder.

| Cycle | Length | Files |
|-------|--------|-------|
| `_models.py -> _category.py` | 2 | 2 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `_category.py` | 8 | 50 | 69 |
| `_models.py` | 50 | 0 | 67 |
| `_config.py` | 47 | 19 | 66 |
| `_base.py` | 20 | 14 | 34 |
| `_c.py` | 2 | 13 | 15 |
| `_csharp.py` | 2 | 13 | 15 |
| `_dart.py` | 2 | 13 | 15 |
| `_elixir.py` | 2 | 13 | 15 |
| `_gdscript.py` | 2 | 13 | 15 |
| `_go.py` | 2 | 13 | 15 |
| `_java.py` | 2 | 13 | 15 |
| `_javascript.py` | 2 | 13 | 15 |
| `_kotlin.py` | 2 | 13 | 15 |
| `_lua.py` | 2 | 13 | 15 |
| `_nim.py` | 2 | 13 | 15 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 1046 total | py | 1046 |
| `RM002` | info | Print statement found (consider logging instead) | python | 12 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `__init__.py` (0 symbols, no doc)
- `__main__.py` (3 symbols, no doc)
- `_uml.py` (25 symbols, no doc)
- `readmenator.py` (0 symbols, no doc)
- `readmenator_orchestrator.py` (34 symbols, no doc)
- `__init__.py` (0 symbols, no doc)
- `test_config.py` (6 symbols, no doc)
- `test_documentation.py` (29 symbols, no doc)
- `test_integration.py` (16 symbols, no doc)
- `test_mermaid.py` (11 symbols, no doc)
- `test_models.py` (11 symbols, no doc)
- `test_parsers.py` (84 symbols, no doc)
- `test_parsers_new.py` (36 symbols, no doc)
- `test_query.py` (18 symbols, no doc)
- `test_ranking.py` (72 symbols, no doc)
- `test_scanner.py` (17 symbols, no doc)
- `test_taint_bdd.py` (26 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_1 ["readmenator/parsers"]
    tests_test_parsers_property_py["test_parsers_property.py (py)"]
    class tests_test_parsers_property_py mod;
    tests_test_parsers_property_py__generate_multiline_code["_generate_multiline_code"]
    class tests_test_parsers_property_py__generate_multiline_code fn;
    tests_test_parsers_property_py --> tests_test_parsers_property_py__generate_multiline_code
    tests_test_parsers_property_py__create_parser["_create_parser"]
    class tests_test_parsers_property_py__create_parser fn;
    tests_test_parsers_property_py --> tests_test_parsers_property_py__create_parser
    tests_test_parsers_property_py_TestParserHypothesisContract["TestParserHypothesisContract"]
    class tests_test_parsers_property_py_TestParserHypothesisContract cls;
    tests_test_parsers_property_py --> tests_test_parsers_property_py_TestParserHypothesisContract
    tests_test_parsers_property_py_TestPythonParserProperty["TestPythonParserProperty"]
    class tests_test_parsers_property_py_TestPythonParserProperty cls;
    tests_test_parsers_property_py --> tests_test_parsers_property_py_TestPythonParserProperty
    tests_test_parsers_property_py_test_never_crashes_on_malformed_code["test_never_crashes_on_malformed_code"]
    class tests_test_parsers_property_py_test_never_crashes_on_malformed_code fn;
    tests_test_parsers_property_py --> tests_test_parsers_property_py_test_never_crashes_on_malformed_code
    readmenator_parsers___init___py["__init__.py (py)"]
    class readmenator_parsers___init___py mod;
    end
    subgraph community_0 ["readmenator"]
    readmenator__pipeline_py["_pipeline.py (py)"]
    class readmenator__pipeline_py mod;
    readmenator__app_py["_app.py (py)"]
    class readmenator__app_py mod;
    readmenator__mcp_server_py["_mcp_server.py (py)"]
    class readmenator__mcp_server_py mod;
    tests_test_documentation_py["test_documentation.py (py)"]
    class tests_test_documentation_py mod;
    readmenator__documentation_py["_documentation.py (py)"]
    class readmenator__documentation_py mod;
    tests_test_taint_bdd_py["test_taint_bdd.py (py)"]
    class tests_test_taint_bdd_py mod;
    tests_test_refactorizer_py["test_refactorizer.py (py)"]
    class tests_test_refactorizer_py mod;
    readmenator___main___py["__main__.py (py)"]
    class readmenator___main___py mod;
    readmenator___init___py["__init__.py (py)"]
    class readmenator___init___py mod;
    readmenator_orchestrator_py["readmenator_orchestrator.py (py)"]
    class readmenator_orchestrator_py mod;
    tests_test_ranking_py["test_ranking.py (py)"]
    class tests_test_ranking_py mod;
    tests_test_mcp_server_py["test_mcp_server.py (py)"]
    class tests_test_mcp_server_py mod;
    tests_test_scanner_py["test_scanner.py (py)"]
    class tests_test_scanner_py mod;
    readmenator__exporter_py["_exporter.py (py)"]
    class readmenator__exporter_py mod;
    tests_test_security_py["test_security.py (py)"]
    class tests_test_security_py mod;
    readmenator__scanner_py["_scanner.py (py)"]
    class readmenator__scanner_py mod;
    tests_test_readme_injector_py["test_readme_injector.py (py)"]
    class tests_test_readme_injector_py mod;
    tests_test_cache_py["test_cache.py (py)"]
    class tests_test_cache_py mod;
    tests_test_cursorrules_py["test_cursorrules.py (py)"]
    class tests_test_cursorrules_py mod;
    tests_test_rule_gen_py["test_rule_gen.py (py)"]
    class tests_test_rule_gen_py mod;
    readmenator__rule_gen_py["_rule_gen.py (py)"]
    class readmenator__rule_gen_py mod;
    readmenator__security_py["_security.py (py)"]
    class readmenator__security_py mod;
    readmenator__query_py["_query.py (py)"]
    class readmenator__query_py mod;
    tests_test_exporter_py["test_exporter.py (py)"]
    class tests_test_exporter_py mod;
    tests_test_cpg_py["test_cpg.py (py)"]
    class tests_test_cpg_py mod;
    tests_test_sarif_py["test_sarif.py (py)"]
    class tests_test_sarif_py mod;
    readmenator__cursorrules_generator_py["_cursorrules_generator.py (py)"]
    class readmenator__cursorrules_generator_py mod;
    readmenator__linter_py["_linter.py (py)"]
    class readmenator__linter_py mod;
    tests_test_uml_py["test_uml.py (py)"]
    class tests_test_uml_py mod;
    readmenator__uml_py["_uml.py (py)"]
    class readmenator__uml_py mod;
    tests_test_integration_py["test_integration.py (py)"]
    class tests_test_integration_py mod;
    tests_test_dead_code_py["test_dead_code.py (py)"]
    class tests_test_dead_code_py mod;
    tests_test_linter_py["test_linter.py (py)"]
    class tests_test_linter_py mod;
    readmenator__analyzer_py["_analyzer.py (py)"]
    class readmenator__analyzer_py mod;
    readmenator__cache_py["_cache.py (py)"]
    class readmenator__cache_py mod;
    tests_test_layer_rules_py["test_layer_rules.py (py)"]
    class tests_test_layer_rules_py mod;
    tests_test_analyzer_py["test_analyzer.py (py)"]
    class tests_test_analyzer_py mod;
    tests_test_hotspots_py["test_hotspots.py (py)"]
    class tests_test_hotspots_py mod;
    tests_test_taint_py["test_taint.py (py)"]
    class tests_test_taint_py mod;
    readmenator__refactorizer_py["_refactorizer.py (py)"]
    class readmenator__refactorizer_py mod;
    readmenator__watcher_py["_watcher.py (py)"]
    class readmenator__watcher_py mod;
    readmenator__hotspots_py["_hotspots.py (py)"]
    class readmenator__hotspots_py mod;
    readmenator__taint_py["_taint.py (py)"]
    class readmenator__taint_py mod;
    readmenator_parsers__base_py["_base.py (py)"]
    class readmenator_parsers__base_py mod;
    readmenator__dead_code_py["_dead_code.py (py)"]
    class readmenator__dead_code_py mod;
    readmenator_parsers__python_py["_python.py (py)"]
    class readmenator_parsers__python_py mod;
    tests_test_parsers_py["test_parsers.py (py)"]
    class tests_test_parsers_py mod;
    tests_test_parsers_new_py["test_parsers_new.py (py)"]
    class tests_test_parsers_new_py mod;
    readmenator__category_py["_category.py (py)"]
    class readmenator__category_py mod;
    readmenator__rank_py["_rank.py (py)"]
    class readmenator__rank_py mod;
    readmenator__projections_py["_projections.py (py)"]
    class readmenator__projections_py mod;
    readmenator__cpg_py["_cpg.py (py)"]
    class readmenator__cpg_py mod;
    readmenator__layer_rules_py["_layer_rules.py (py)"]
    class readmenator__layer_rules_py mod;
    readmenator__explain_py["_explain.py (py)"]
    class readmenator__explain_py mod;
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
    readmenator__models_py["_models.py (py)"]
    class readmenator__models_py mod;
    tests_test_query_py["test_query.py (py)"]
    class tests_test_query_py mod;
    tests_test_mermaid_py["test_mermaid.py (py)"]
    class tests_test_mermaid_py mod;
    readmenator__sarif_py["_sarif.py (py)"]
    class readmenator__sarif_py mod;
    readmenator__mermaid_py["_mermaid.py (py)"]
    class readmenator__mermaid_py mod;
    readmenator__resolver_py["_resolver.py (py)"]
    class readmenator__resolver_py mod;
    tests_test_resolver_py["test_resolver.py (py)"]
    class tests_test_resolver_py mod;
    readmenator__readme_injector_py["_readme_injector.py (py)"]
    class readmenator__readme_injector_py mod;
    tests_test_config_py["test_config.py (py)"]
    class tests_test_config_py mod;
    readmenator__layers_py["_layers.py (py)"]
    class readmenator__layers_py mod;
    readmenator_py["readmenator.py (py)"]
    class readmenator_py mod;
    tests_test_models_py["test_models.py (py)"]
    class tests_test_models_py mod;
    readmenator__config_py["_config.py (py)"]
    class readmenator__config_py mod;
    _refactor__app_sh[".refactor__app.sh (sh)"]
    class _refactor__app_sh mod;
    _refactor__documentation_sh[".refactor__documentation.sh (sh)"]
    class _refactor__documentation_sh mod;
    _refactor__exporter_sh[".refactor__exporter.sh (sh)"]
    class _refactor__exporter_sh mod;
    _refactor__mcp_server_sh[".refactor__mcp_server.sh (sh)"]
    class _refactor__mcp_server_sh mod;
    _refactor__rank_sh[".refactor__rank.sh (sh)"]
    class _refactor__rank_sh mod;
    _refactor__security_sh[".refactor__security.sh (sh)"]
    class _refactor__security_sh mod;
    _refactor__uml_sh[".refactor__uml.sh (sh)"]
    class _refactor__uml_sh mod;
    _refactor_test_parsers_sh[".refactor_test_parsers.sh (sh)"]
    class _refactor_test_parsers_sh mod;
    _refactor_test_ranking_sh[".refactor_test_ranking.sh (sh)"]
    class _refactor_test_ranking_sh mod;
    _refactor_test_uml_sh[".refactor_test_uml.sh (sh)"]
    class _refactor_test_uml_sh mod;
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
    end
    readmenator___init___py -- resolved_imports --> readmenator__app_py
    readmenator___init___py -- resolved_imports --> readmenator__category_py
    readmenator___init___py -- resolved_imports --> readmenator__config_py
    readmenator___init___py -- resolved_imports --> readmenator__mcp_server_py
    readmenator___init___py -- resolved_imports --> readmenator__models_py
    readmenator___init___py -- resolved_imports --> readmenator__rank_py
    readmenator___init___py -- resolved_imports --> readmenator__readme_injector_py
    readmenator___init___py -- resolved_imports --> readmenator__uml_py
    readmenator___main___py -- resolved_imports --> readmenator__app_py
    readmenator___main___py -- resolved_imports --> readmenator__mcp_server_py
    readmenator___main___py -- resolved_imports --> readmenator__config_py
    readmenator___main___py -- resolved_imports --> readmenator__config_py
    readmenator___main___py -- resolved_imports --> readmenator__config_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__config_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__cache_py
    readmenator__app_py -- resolved_imports --> readmenator__config_py
    readmenator__app_py -- resolved_imports --> readmenator__cursorrules_generator_py
    readmenator__app_py -- resolved_imports --> readmenator__dead_code_py
    readmenator__app_py -- resolved_imports --> readmenator__layers_py
    readmenator__app_py -- resolved_imports --> readmenator__linter_py
    readmenator__app_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__pipeline_py
    readmenator__app_py -- resolved_imports --> readmenator__query_py
    readmenator__app_py -- resolved_imports --> readmenator__rank_py
    readmenator__app_py -- resolved_imports --> readmenator__refactorizer_py
    readmenator__app_py -- resolved_imports --> readmenator__resolver_py
    readmenator__app_py -- resolved_imports --> readmenator__watcher_py
    readmenator__cache_py -- resolved_imports --> readmenator__config_py
    readmenator__category_py -- resolved_imports --> readmenator__models_py
    readmenator__cpg_py -- resolved_imports --> readmenator__models_py
    readmenator__cursorrules_generator_py -- resolved_imports --> readmenator__config_py
    readmenator__cursorrules_generator_py -- resolved_imports --> readmenator__layers_py
    readmenator__cursorrules_generator_py -- resolved_imports --> readmenator__models_py
    readmenator__dead_code_py -- resolved_imports --> readmenator__config_py
    readmenator__dead_code_py -- resolved_imports --> readmenator__models_py
    readmenator__documentation_py -- resolved_imports --> readmenator__config_py
    readmenator__documentation_py -- resolved_imports --> readmenator__cpg_py
    readmenator__documentation_py -- resolved_imports --> readmenator__mermaid_py
    readmenator__documentation_py -- resolved_imports --> readmenator__uml_py
    readmenator__documentation_py -- resolved_imports --> readmenator__models_py
    readmenator__documentation_py -- resolved_imports --> readmenator__rank_py
    readmenator__explain_py -- resolved_imports --> readmenator__category_py
    readmenator__explain_py -- resolved_imports --> readmenator__rank_py
    readmenator__exporter_py -- resolved_imports --> readmenator__config_py
    readmenator__exporter_py -- resolved_imports --> readmenator__models_py
    readmenator__hotspots_py -- resolved_imports --> readmenator__config_py
    readmenator__hotspots_py -- resolved_imports --> readmenator__models_py
    readmenator__layer_rules_py -- resolved_imports --> readmenator__config_py
    readmenator__layer_rules_py -- resolved_imports --> readmenator__models_py
    readmenator__layers_py -- resolved_imports --> readmenator__models_py
    readmenator__linter_py -- resolved_imports --> readmenator__config_py
    readmenator__linter_py -- resolved_imports --> readmenator__layers_py
    readmenator__linter_py -- resolved_imports --> readmenator__models_py
    readmenator__mcp_server_py -- resolved_imports --> readmenator__app_py
    readmenator__mcp_server_py -- resolved_imports --> readmenator__config_py
    readmenator__mcp_server_py -- resolved_imports --> readmenator__layers_py
    readmenator__mcp_server_py -- resolved_imports --> readmenator__models_py
    readmenator__mcp_server_py -- resolved_imports --> readmenator__query_py
    readmenator__mermaid_py -- resolved_imports --> readmenator__models_py
    readmenator__models_py -- resolved_imports --> readmenator__category_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__analyzer_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__category_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__config_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__cpg_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__documentation_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__exporter_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__hotspots_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__layer_rules_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__layers_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__models_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__rank_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__readme_injector_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__rule_gen_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__sarif_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__scanner_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__security_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__taint_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__uml_py
    readmenator__projections_py -- resolved_imports --> readmenator__category_py
    readmenator__projections_py -- resolved_imports --> readmenator__models_py
    readmenator__query_py -- resolved_imports --> readmenator__category_py
    readmenator__query_py -- resolved_imports --> readmenator__models_py
    readmenator__query_py -- resolved_imports --> readmenator__rank_py
    readmenator__rank_py -- resolved_imports --> readmenator__category_py
    readmenator__refactorizer_py -- resolved_imports --> readmenator__config_py
    readmenator__refactorizer_py -- resolved_imports --> readmenator__models_py
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
    readmenator__uml_py -- resolved_imports --> readmenator__config_py
    readmenator__uml_py -- resolved_imports --> readmenator__models_py
    readmenator__watcher_py -- resolved_imports --> readmenator__config_py
    ext_readmenator__app["readmenator._app"]
    class ext_readmenator__app ext;
    readmenator___init___py -.->|imports| ext_readmenator__app
    ext_readmenator__category["readmenator._category"]
    class ext_readmenator__category ext;
    readmenator___init___py -.->|imports| ext_readmenator__category
    ext_readmenator__config["readmenator._config"]
    class ext_readmenator__config ext;
    readmenator___init___py -.->|imports| ext_readmenator__config
    ext_readmenator__mcp_server["readmenator._mcp_server"]
    class ext_readmenator__mcp_server ext;
    readmenator___init___py -.->|imports| ext_readmenator__mcp_server
    ext_readmenator__models["readmenator._models"]
    class ext_readmenator__models ext;
    readmenator___init___py -.->|imports| ext_readmenator__models
    ext_readmenator__rank["readmenator._rank"]
    class ext_readmenator__rank ext;
    readmenator___init___py -.->|imports| ext_readmenator__rank
    ext_readmenator__readme_injector["readmenator._readme_injector"]
    class ext_readmenator__readme_injector ext;
    readmenator___init___py -.->|imports| ext_readmenator__readme_injector
    ext_readmenator__uml["readmenator._uml"]
    class ext_readmenator__uml ext;
    readmenator___init___py -.->|imports| ext_readmenator__uml
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
    readmenator___main___py -.->|imports| ext_readmenator__mcp_server
    readmenator___main___py -.->|imports| ext_readmenator__config
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
    ext_readmenator__cursorrules_generator["readmenator._cursorrules_generator"]
    class ext_readmenator__cursorrules_generator ext;
    readmenator__app_py -.->|imports| ext_readmenator__cursorrules_generator
    ext_readmenator__dead_code["readmenator._dead_code"]
    class ext_readmenator__dead_code ext;
    readmenator__app_py -.->|imports| ext_readmenator__dead_code
    ext_readmenator__layers["readmenator._layers"]
    class ext_readmenator__layers ext;
    readmenator__app_py -.->|imports| ext_readmenator__layers
    ext_readmenator__linter["readmenator._linter"]
    class ext_readmenator__linter ext;
    readmenator__app_py -.->|imports| ext_readmenator__linter
    readmenator__app_py -.->|imports| ext_readmenator__models
    ext_readmenator__pipeline["readmenator._pipeline"]
    class ext_readmenator__pipeline ext;
    readmenator__app_py -.->|imports| ext_readmenator__pipeline
    ext_readmenator__query["readmenator._query"]
    class ext_readmenator__query ext;
    readmenator__app_py -.->|imports| ext_readmenator__query
    readmenator__app_py -.->|imports| ext_readmenator__rank
    ext_readmenator__refactorizer["readmenator._refactorizer"]
    class ext_readmenator__refactorizer ext;
    readmenator__app_py -.->|imports| ext_readmenator__refactorizer
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
    readmenator__category_py -.->|imports| ext___future__
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    readmenator__category_py -.->|imports| ext_dataclasses
    ext_enum["enum"]
    class ext_enum ext;
    readmenator__category_py -.->|imports| ext_enum
    readmenator__category_py -.->|imports| ext_typing
    readmenator__category_py -.->|imports| ext_readmenator__models
    readmenator__config_py -.->|imports| ext___future__
    readmenator__config_py -.->|imports| ext_dataclasses
    readmenator__config_py -.->|imports| ext_typing
    readmenator__cpg_py -.->|imports| ext___future__
    readmenator__cpg_py -.->|imports| ext_hashlib
    readmenator__cpg_py -.->|imports| ext_json
    readmenator__cpg_py -.->|imports| ext_typing
    readmenator__cpg_py -.->|imports| ext_readmenator__models
    readmenator__cursorrules_generator_py -.->|imports| ext___future__
    readmenator__cursorrules_generator_py -.->|imports| ext_pathlib
    readmenator__cursorrules_generator_py -.->|imports| ext_typing
    readmenator__cursorrules_generator_py -.->|imports| ext_readmenator__config
    readmenator__cursorrules_generator_py -.->|imports| ext_readmenator__layers
    readmenator__cursorrules_generator_py -.->|imports| ext_readmenator__models
    readmenator__dead_code_py -.->|imports| ext___future__
    readmenator__dead_code_py -.->|imports| ext_collections
    readmenator__dead_code_py -.->|imports| ext_typing
    readmenator__dead_code_py -.->|imports| ext_readmenator__config
    readmenator__dead_code_py -.->|imports| ext_readmenator__models
    readmenator__documentation_py -.->|imports| ext___future__
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    readmenator__documentation_py -.->|imports| ext_subprocess
    readmenator__documentation_py -.->|imports| ext_collections
    readmenator__documentation_py -.->|imports| ext_typing
    readmenator__documentation_py -.->|imports| ext_readmenator__config
    ext_readmenator__cpg["readmenator._cpg"]
    class ext_readmenator__cpg ext;
    readmenator__documentation_py -.->|imports| ext_readmenator__cpg
    ext_readmenator__mermaid["readmenator._mermaid"]
    class ext_readmenator__mermaid ext;
    readmenator__documentation_py -.->|imports| ext_readmenator__mermaid
    readmenator__documentation_py -.->|imports| ext_readmenator__uml
    readmenator__documentation_py -.->|imports| ext_readmenator__models
    readmenator__documentation_py -.->|imports| ext_readmenator__rank
    readmenator__explain_py -.->|imports| ext___future__
    readmenator__explain_py -.->|imports| ext_typing
    readmenator__explain_py -.->|imports| ext_readmenator__category
    readmenator__explain_py -.->|imports| ext_readmenator__rank
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
    readmenator__linter_py -.->|imports| ext___future__
    readmenator__linter_py -.->|imports| ext_pathlib
    readmenator__linter_py -.->|imports| ext_typing
    readmenator__linter_py -.->|imports| ext_readmenator__config
    readmenator__linter_py -.->|imports| ext_readmenator__layers
    readmenator__linter_py -.->|imports| ext_readmenator__models
    readmenator__mcp_server_py -.->|imports| ext___future__
    readmenator__mcp_server_py -.->|imports| ext_json
    readmenator__mcp_server_py -.->|imports| ext_logging
    readmenator__mcp_server_py -.->|imports| ext_sys
    readmenator__mcp_server_py -.->|imports| ext_pathlib
    readmenator__mcp_server_py -.->|imports| ext_typing
    readmenator__mcp_server_py -.->|imports| ext_readmenator__app
    readmenator__mcp_server_py -.->|imports| ext_readmenator__config
    readmenator__mcp_server_py -.->|imports| ext_readmenator__layers
    readmenator__mcp_server_py -.->|imports| ext_readmenator__models
    readmenator__mcp_server_py -.->|imports| ext_readmenator__query
    readmenator__mermaid_py -.->|imports| ext___future__
    ext_re["re"]
    class ext_re ext;
    readmenator__mermaid_py -.->|imports| ext_re
    readmenator__mermaid_py -.->|imports| ext_typing
    readmenator__mermaid_py -.->|imports| ext_readmenator__models
    readmenator__models_py -.->|imports| ext___future__
    readmenator__models_py -.->|imports| ext_dataclasses
    readmenator__models_py -.->|imports| ext_typing
    readmenator__models_py -.->|imports| ext_readmenator__category
    readmenator__pipeline_py -.->|imports| ext___future__
    readmenator__pipeline_py -.->|imports| ext_typing
    ext_readmenator__analyzer["readmenator._analyzer"]
    class ext_readmenator__analyzer ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__analyzer
    readmenator__pipeline_py -.->|imports| ext_readmenator__category
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
    readmenator__pipeline_py -.->|imports| ext_readmenator__rank
    readmenator__pipeline_py -.->|imports| ext_readmenator__readme_injector
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
    readmenator__pipeline_py -.->|imports| ext_readmenator__uml
    readmenator__projections_py -.->|imports| ext___future__
    readmenator__projections_py -.->|imports| ext_typing
    readmenator__projections_py -.->|imports| ext_readmenator__category
    readmenator__projections_py -.->|imports| ext_readmenator__models
    readmenator__query_py -.->|imports| ext___future__
    readmenator__query_py -.->|imports| ext_collections
    readmenator__query_py -.->|imports| ext_typing
    readmenator__query_py -.->|imports| ext_readmenator__category
    readmenator__query_py -.->|imports| ext_readmenator__models
    readmenator__query_py -.->|imports| ext_readmenator__rank
    readmenator__rank_py -.->|imports| ext___future__
    readmenator__rank_py -.->|imports| ext_math
    readmenator__rank_py -.->|imports| ext_dataclasses
    readmenator__rank_py -.->|imports| ext_typing
    readmenator__rank_py -.->|imports| ext_readmenator__category
    readmenator__readme_injector_py -.->|imports| ext___future__
    readmenator__readme_injector_py -.->|imports| ext_logging
    readmenator__readme_injector_py -.->|imports| ext_pathlib
    readmenator__readme_injector_py -.->|imports| ext_typing
    readmenator__refactorizer_py -.->|imports| ext___future__
    readmenator__refactorizer_py -.->|imports| ext_re
    readmenator__refactorizer_py -.->|imports| ext_pathlib
    readmenator__refactorizer_py -.->|imports| ext_typing
    readmenator__refactorizer_py -.->|imports| ext_readmenator__config
    readmenator__refactorizer_py -.->|imports| ext_readmenator__models
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
    readmenator__uml_py -.->|imports| ext___future__
    readmenator__uml_py -.->|imports| ext_collections
    readmenator__uml_py -.->|imports| ext_typing
    readmenator__uml_py -.->|imports| ext_readmenator__config
    readmenator__uml_py -.->|imports| ext_readmenator__models
    readmenator__uml_py -.->|imports| ext_enum
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
    tests_test_cursorrules_py -.->|imports| ext___future__
    tests_test_cursorrules_py -.->|imports| ext_tempfile
    tests_test_cursorrules_py -.->|imports| ext_unittest
    tests_test_cursorrules_py -.->|imports| ext_pathlib
    tests_test_cursorrules_py -.->|imports| ext_readmenator__config
    tests_test_cursorrules_py -.->|imports| ext_readmenator__cursorrules_generator
    tests_test_cursorrules_py -.->|imports| ext_readmenator__models
    tests_test_dead_code_py -.->|imports| ext___future__
    tests_test_dead_code_py -.->|imports| ext_unittest
    tests_test_dead_code_py -.->|imports| ext_readmenator__config
    tests_test_dead_code_py -.->|imports| ext_readmenator__dead_code
    tests_test_dead_code_py -.->|imports| ext_readmenator__models
    tests_test_documentation_py -.->|imports| ext___future__
    tests_test_documentation_py -.->|imports| ext_unittest
    tests_test_documentation_py -.->|imports| ext_readmenator__config
    tests_test_documentation_py -.->|imports| ext_readmenator__documentation
    tests_test_documentation_py -.->|imports| ext_readmenator__models
    tests_test_documentation_py -.->|imports| ext_readmenator__models
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
    tests_test_linter_py -.->|imports| ext___future__
    tests_test_linter_py -.->|imports| ext_unittest
    tests_test_linter_py -.->|imports| ext_readmenator__config
    tests_test_linter_py -.->|imports| ext_readmenator__linter
    tests_test_linter_py -.->|imports| ext_readmenator__models
    tests_test_mcp_server_py -.->|imports| ext___future__
    tests_test_mcp_server_py -.->|imports| ext_json
    tests_test_mcp_server_py -.->|imports| ext_unittest
    tests_test_mcp_server_py -.->|imports| ext_pathlib
    tests_test_mcp_server_py -.->|imports| ext_tempfile
    tests_test_mcp_server_py -.->|imports| ext_typing
    tests_test_mcp_server_py -.->|imports| ext_readmenator__mcp_server
    tests_test_mcp_server_py -.->|imports| ext_readmenator__app
    tests_test_mcp_server_py -.->|imports| ext_readmenator__config
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
    tests_test_parsers_property_py -.->|imports| ext___future__
    tests_test_parsers_property_py -.->|imports| ext_sys
    tests_test_parsers_property_py -.->|imports| ext_unittest
    tests_test_parsers_property_py -.->|imports| ext_pathlib
    tests_test_parsers_property_py -.->|imports| ext_typing
    tests_test_parsers_property_py -.->|imports| ext_readmenator__config
    tests_test_parsers_property_py -.->|imports| ext_readmenator__models
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__python
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__c
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__go
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__rust
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__javascript
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__java
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__csharp
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__shell
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__php
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__dart
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__gdscript
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__nim
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__ruby
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__swift
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__kotlin
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__scala
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__lua
    tests_test_parsers_property_py -.->|imports| ext_readmenator_parsers__elixir
    ext_hypothesis["hypothesis"]
    class ext_hypothesis ext;
    tests_test_parsers_property_py -.->|imports| ext_hypothesis
    tests_test_query_py -.->|imports| ext_unittest
    tests_test_query_py -.->|imports| ext_readmenator__models
    tests_test_query_py -.->|imports| ext_readmenator__query
    tests_test_ranking_py -.->|imports| ext___future__
    tests_test_ranking_py -.->|imports| ext_typing
    ext_pytest["pytest"]
    class ext_pytest ext;
    tests_test_ranking_py -.->|imports| ext_pytest
    tests_test_ranking_py -.->|imports| ext_readmenator__category
    ext_readmenator__explain["readmenator._explain"]
    class ext_readmenator__explain ext;
    tests_test_ranking_py -.->|imports| ext_readmenator__explain
    tests_test_ranking_py -.->|imports| ext_readmenator__models
    ext_readmenator__projections["readmenator._projections"]
    class ext_readmenator__projections ext;
    tests_test_ranking_py -.->|imports| ext_readmenator__projections
    tests_test_ranking_py -.->|imports| ext_readmenator__rank
    tests_test_readme_injector_py -.->|imports| ext___future__
    tests_test_readme_injector_py -.->|imports| ext_tempfile
    tests_test_readme_injector_py -.->|imports| ext_unittest
    tests_test_readme_injector_py -.->|imports| ext_pathlib
    tests_test_readme_injector_py -.->|imports| ext_readmenator__readme_injector
    tests_test_readme_injector_py -.->|imports| ext_shutil
    tests_test_readme_injector_py -.->|imports| ext_shutil
    tests_test_readme_injector_py -.->|imports| ext_shutil
    tests_test_readme_injector_py -.->|imports| ext_shutil
    tests_test_refactorizer_py -.->|imports| ext___future__
    tests_test_refactorizer_py -.->|imports| ext_tempfile
    tests_test_refactorizer_py -.->|imports| ext_unittest
    tests_test_refactorizer_py -.->|imports| ext_pathlib
    tests_test_refactorizer_py -.->|imports| ext_readmenator__config
    tests_test_refactorizer_py -.->|imports| ext_readmenator__models
    tests_test_refactorizer_py -.->|imports| ext_readmenator__refactorizer
    tests_test_refactorizer_py -.->|imports| ext_readmenator__models
    tests_test_refactorizer_py -.->|imports| ext_readmenator__models
    tests_test_refactorizer_py -.->|imports| ext_readmenator__models
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
    tests_test_taint_bdd_py -.->|imports| ext___future__
    tests_test_taint_bdd_py -.->|imports| ext_tempfile
    tests_test_taint_bdd_py -.->|imports| ext_pathlib
    tests_test_taint_bdd_py -.->|imports| ext_typing
    tests_test_taint_bdd_py -.->|imports| ext_readmenator__config
    tests_test_taint_bdd_py -.->|imports| ext_readmenator__models
    tests_test_taint_bdd_py -.->|imports| ext_readmenator__taint
    ext_pytest_bdd["pytest_bdd"]
    class ext_pytest_bdd ext;
    tests_test_taint_bdd_py -.->|imports| ext_pytest_bdd
    tests_test_taint_bdd_py -.->|imports| ext_readmenator__scanner
    tests_test_taint_bdd_py -.->|imports| ext_readmenator__resolver
    tests_test_taint_bdd_py -.->|imports| ext_unittest
    tests_test_uml_py -.->|imports| ext___future__
    tests_test_uml_py -.->|imports| ext_unittest
    tests_test_uml_py -.->|imports| ext_readmenator__config
    tests_test_uml_py -.->|imports| ext_readmenator__models
    tests_test_uml_py -.->|imports| ext_readmenator__uml
```

---

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class _analyzer_py_GraphAnalyzer {
    <<class>>
    +__init__(self, config)
    +analyze(self, nodes, edges, resolved_edges)
    +_build_adjacency(self, nodes, edges)
    +_build_reverse_adjacency(self, adjacency)
    +_compute_god_nodes(self, nodes, adjacency, reverse_adjacency)
    +_detect_communities(self, nodes, adjacency)
    +_label_communities(self, nodes, communities)
    +_build_community_map(self, communities)
    +_compute_cohesion(self, communities, adjacency)
    +_find_surprising_connections(self, nodes, adjacency, community_map)
  }
  class _app_py_readmenatorApplication {
    <<class>>
    +__init__(self, config)
    +_scan(self, target_dir)
    +_scan_with_content(self, target_dir)
    +_resolve_imports(self, nodes, edges, target_dir)
    +run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)
    +_write_sidecar_outputs(self, root, findings, analysis_v2)
    +_inject_readme_link(self, root)
    +generate_uml_code(self, target_dir, language, output_path)
    +_log_summary(self, nodes, edges, resolved_edges, analysis, layer_summary, analysis_v2, findings)
    +update(self, target_dir, run_security)
  }
  class _cache_py_FileCache {
    <<class>>
    +__init__(self, config, project_root)
    +load(self)
    +save(self, hashes)
    +compute_hash(self, file_path)
    +compute_hashes(self, file_paths)
    +find_changed(self, file_paths)
    +prune_deleted(self, current_file_ids)
    +save_analysis(self, key, data)
    +load_analysis(self, key)
    +clear_analysis(self, key)
  }
  class _category_py_EdgeKind {
    <<class>>
    +build_category_from_edges(edges, resolved_edges, node_ids)
    +_infer_edge_kind(relation)
    +__str__(self)
    +weight(self)
    +__init__(self)
    +add_object(self, obj_id)
    +add_morphism(self, m)
    +objects(self)
    +morphisms(self)
    +outgoing(self, obj_id)
  }
  class _category_py_Morphism {
    <<class>>
    +build_category_from_edges(edges, resolved_edges, node_ids)
    +_infer_edge_kind(relation)
    +__str__(self)
    +weight(self)
    +__init__(self)
    +add_object(self, obj_id)
    +add_morphism(self, m)
    +objects(self)
    +morphisms(self)
    +outgoing(self, obj_id)
  }
  class _category_py_Category {
    <<class>>
    +build_category_from_edges(edges, resolved_edges, node_ids)
    +_infer_edge_kind(relation)
    +__str__(self)
    +weight(self)
    +__init__(self)
    +add_object(self, obj_id)
    +add_morphism(self, m)
    +objects(self)
    +morphisms(self)
    +outgoing(self, obj_id)
  }
  class _category_py_TypedGraph {
    <<class>>
    +build_category_from_edges(edges, resolved_edges, node_ids)
    +_infer_edge_kind(relation)
    +__str__(self)
    +weight(self)
    +__init__(self)
    +add_object(self, obj_id)
    +add_morphism(self, m)
    +objects(self)
    +morphisms(self)
    +outgoing(self, obj_id)
  }
  class _config_py_Config {
    <<class>>
  }
  class _cpg_py_CodePropertyGraph {
    <<class>>
    +__init__(self, privacy_mode, cpg_context)
    +generate(self, nodes, edges, resolved_edges, analysis, findings)
    +_severity_counts(self, findings)
    +_build_symbol_list(self, node)
    +_compute_node_hash(node)
  }
  class _cursorrules_generator_py_CursorRulesGenerator {
    <<class>>
    +__init__(self, config)
    +generate(self, nodes, edges, analysis, layers, violations, project_root)
    +_build_base_rules(self)
    +_extract_layer_constraints(self, layers)
    +_extract_analysis_constraints(self, analysis)
    +_extract_violation_rules(self, violations)
    +_write_file(self, project_root, content)
  }
  class _dead_code_py_DeadCodeStripper {
    <<class>>
    +__init__(self, config)
    +identify(self, nodes, edges, resolved_edges)
    +_build_in_degree_map(self, nodes, resolved_edges)
    +_classify_recommendation(self, symbol)
  }
  class _documentation_py_DocumentationGenerator {
    <<class>>
    +__init__(self, config)
    +_ranking_version(self)
    +_get_git_commit()
    +generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)
    +_apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)
    +_build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)
    +_build_layers(self, layers, nodes)
    +_build_dashboard(self, nodes, edges, resolved_edges)
    +_build_god_nodes(self, analysis, ranked)
    +_build_community_analysis(self, analysis, nodes)
  }
  class _exporter_py_GraphExporter {
    <<class>>
    +__init__(self, config)
    +to_json(self, nodes, edges, resolved_edges, analysis, findings)
    +to_html(self, nodes, edges, resolved_edges, analysis, findings)
    +_community_color_map(self, analysis)
    +_lighten(hex_color)
    +_render_html(self, vis_nodes, vis_edges, analysis, findings)
    +to_svg(self, nodes, edges, resolved_edges, analysis)
    +_render_truncated_svg(self, total_nodes)
    +_layout_spring(self, nodes, edges, node_map)
    +to_graphml(self, nodes, edges, resolved_edges, analysis)
  }
  class _hotspots_py_HotspotAnalyzer {
    <<class>>
    +__init__(self, config)
    +analyze_hotspots(self, nodes, edges, resolved_edges)
    +detect_cycles(self, nodes, resolved_edges)
    +analyze_change_impact(self, nodes, resolved_edges)
    +_dfs_visit(current)
    +_record_cycle(start, end)
  }
  class _layer_rules_py_LayerRuleEngine {
    <<class>>
    +__init__(self, config)
    +detect_violations(self, nodes, edges, resolved_edges, layers)
    +violation_summary(violations)
  }
  class _layers_py_LayerDetector {
    <<class>>
    +detect(self, nodes, edges)
    +_classify_file(self, node, edges)
    +layer_summary(layers)
  }
  class _linter_py_ArchitectureLinter {
    <<class>>
    +__init__(self, config)
    +lint(self, nodes, edges, resolved_edges, layers, content_map)
    +_check_file_length(self, nodes, content_map)
    +_check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)
    +_check_circular_dependencies(self, nodes, resolved_edges)
    +_dfs(current)
  }
  class _mcp_server_py_MCPError {
    <<class>>
    +main()
    +__init__(self, code, message, data)
    +__init__(self, msg)
    +is_notification(self)
    +response(self, result)
    +error(self, code, message, data)
    +__init__(self, name, description, handler, input_schema)
    +definition(self)
    +call(self, arguments)
    +__init__(self, uri, name, description, mime_type, handler)
  }
  class _mcp_server_py_MCPRequest {
    <<class>>
    +main()
    +__init__(self, code, message, data)
    +__init__(self, msg)
    +is_notification(self)
    +response(self, result)
    +error(self, code, message, data)
    +__init__(self, name, description, handler, input_schema)
    +definition(self)
    +call(self, arguments)
    +__init__(self, uri, name, description, mime_type, handler)
  }
  class _mcp_server_py_MCPTool {
    <<class>>
    +main()
    +__init__(self, code, message, data)
    +__init__(self, msg)
    +is_notification(self)
    +response(self, result)
    +error(self, code, message, data)
    +__init__(self, name, description, handler, input_schema)
    +definition(self)
    +call(self, arguments)
    +__init__(self, uri, name, description, mime_type, handler)
  }
  class _mcp_server_py_MCPResource {
    <<class>>
    +main()
    +__init__(self, code, message, data)
    +__init__(self, msg)
    +is_notification(self)
    +response(self, result)
    +error(self, code, message, data)
    +__init__(self, name, description, handler, input_schema)
    +definition(self)
    +call(self, arguments)
    +__init__(self, uri, name, description, mime_type, handler)
  }
  class _mcp_server_py_MCPServer {
    <<class>>
    +main()
    +__init__(self, code, message, data)
    +__init__(self, msg)
    +is_notification(self)
    +response(self, result)
    +error(self, code, message, data)
    +__init__(self, name, description, handler, input_schema)
    +definition(self)
    +call(self, arguments)
    +__init__(self, uri, name, description, mime_type, handler)
  }
  class _mermaid_py_MermaidRenderer {
    <<class>>
    +__init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)
    +_sanitize_id(node_id)
    +render(self, nodes, edges, resolved_edges, analysis)
  }
  class _models_py_Symbol {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_Node {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_Edge {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_SecurityFinding {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_CommunityResult {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_AnalysisResult {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_TaintPath {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_TaintAnalysisResult {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_DependencyCycle {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_ChangeImpact {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_HotspotResult {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_SuggestedRule {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_LayerViolation {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_AnalysisResultV2 {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_LinterViolation {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_DeadCodeReport {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_RefactoringAction {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _models_py_RefactoringPlan {
    <<class>>
    +pluralize_symbol_kind(kind, plural_map)
  }
  class _pipeline_py_AnalyzerFactory {
    <<class>>
    +__init__(self, config)
    +scanner(self)
    +generator(self)
    +analyzer(self)
    +security(self)
    +exporter(self)
    +taint(self)
    +hotspots(self)
    +layer_rules(self)
    +rule_gen(self)
  }
  class _pipeline_py_DeepAnalysisRunner {
    <<class>>
    +__init__(self, config)
    +scanner(self)
    +generator(self)
    +analyzer(self)
    +security(self)
    +exporter(self)
    +taint(self)
    +hotspots(self)
    +layer_rules(self)
    +rule_gen(self)
  }
  class _projections_py_Projection {
    <<class>>
    +apply_view(category, view_config)
    +map_node(self, node)
    +map_morphism(self, m)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, documented_ids)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, fan_in, fan_out, test_files)
    +map_node(self, node)
  }
  class _projections_py_IdentityProjection {
    <<class>>
    +apply_view(category, view_config)
    +map_node(self, node)
    +map_morphism(self, m)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, documented_ids)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, fan_in, fan_out, test_files)
    +map_node(self, node)
  }
  class _projections_py_DocProjection {
    <<class>>
    +apply_view(category, view_config)
    +map_node(self, node)
    +map_morphism(self, m)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, documented_ids)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, fan_in, fan_out, test_files)
    +map_node(self, node)
  }
  class _projections_py_RiskProjection {
    <<class>>
    +apply_view(category, view_config)
    +map_node(self, node)
    +map_morphism(self, m)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, documented_ids)
    +map_node(self, node)
    +map_morphism(self, m)
    +__init__(self, fan_in, fan_out, test_files)
    +map_node(self, node)
  }
  class _query_py_QueryEngine {
    <<class>>
    +__init__(self, nodes, edges, resolved_edges, ranker, config)
    +_init_default_ranker(self)
    +ranked_query(self, query, top_n)
    +_estimate_test_coverage(self)
    +_estimate_doc_coverage(self)
    +_build_symbol_index(self)
    +_build_import_graph(self)
    +_build_resolved_graph(self)
    +find_symbol(self, name)
    +explain(self, name)
  }
  class _rank_py_RankConfig {
    <<class>>
    +global_pagerank(graph, alpha, max_iter, tolerance)
    +personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)
    +hits(graph, max_iter, tolerance)
    +build_seeds_from_query(query, node_ids, node_labels, symbols)
    +build_seeds_for_context(node_ids, anchor_patterns)
    +_format_explanation(item, result)
    +label(self)
    +top(self, n)
    +explain(self, node_id)
    +__init__(self, graph, config)
  }
  class _rank_py_RankedItem {
    <<class>>
    +global_pagerank(graph, alpha, max_iter, tolerance)
    +personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)
    +hits(graph, max_iter, tolerance)
    +build_seeds_from_query(query, node_ids, node_labels, symbols)
    +build_seeds_for_context(node_ids, anchor_patterns)
    +_format_explanation(item, result)
    +label(self)
    +top(self, n)
    +explain(self, node_id)
    +__init__(self, graph, config)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [{"cohesion": 0.863, "id": 0, "label": "readmenator", "size": 62}, {"cohesion": 0.686, "id": 1, "label": "readmenator/parsers", "size": 24}], "god_nodes": [{"node_id": "readmenator/_models.py", "score": 135.9}, {"node_id": "readmenator/_config.py", "score": 94.1}, {"node_id": "readmenator/parsers/__init__.py", "score": 48.2}, {"node_id": "readmenator/parsers/_base.py", "score": 44.6}, {"node_id": "tests/test_parsers_property.py", "score": 41.6}, {"node_id": "readmenator/_pipeline.py", "score": 40.3}, {"node_id": "readmenator/_app.py", "score": 39.7}, {"node_id": "readmenator/_mcp_server.py", "score": 21.2}, {"node_id": "readmenator/_documentation.py", "score": 18.7}, {"node_id": "readmenator/_category.py", "score": 18.6}], "surprising_connections": [{"hops": 4, "source": "readmenator/_explain.py", "target": "readmenator/parsers/__init__.py"}, {"hops": 4, "source": "readmenator/_explain.py", "target": "tests/test_parsers.py"}, {"hops": 4, "source": "readmenator/_explain.py", "target": "tests/test_parsers_new.py"}, {"hops": 4, "source": "readmenator/_projections.py", "target": "tests/test_parsers.py"}, {"hops": 4, "source": "readmenator/_projections.py", "target": "tests/test_parsers_new.py"}]}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._mcp_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._mcp_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "random"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._cursorrules_generator"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._dead_code"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._linter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._pipeline"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._refactorizer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._watcher"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._mermaid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "textwrap"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._documentation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._exporter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._hotspots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._layer_rules"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._rule_gen"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._sarif"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._c"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._python"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._go"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._rust"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._javascript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._java"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._csharp"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._shell"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._php"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._dart"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._gdscript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._nim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._assembly"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._ruby"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._swift"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._kotlin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._scala"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._lua"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._elixir"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "ast"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "readmenator.__main__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "shlex"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "readmenator._cursorrules_generator"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "readmenator._dead_code"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._documentation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._exporter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._hotspots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._layer_rules"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "readmenator._linter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "readmenator._mcp_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "readmenator._mermaid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_models.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_models.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._python"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._c"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._go"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._rust"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._javascript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._java"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._csharp"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._shell"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._php"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._dart"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._gdscript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._nim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._ruby"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._swift"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._kotlin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._scala"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._lua"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._elixir"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "hypothesis"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._explain"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._projections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._refactorizer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._rule_gen"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._sarif"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "pytest_bdd"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_mcp_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_mcp_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_analyzer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_analyzer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_cursorrules_generator.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_dead_code.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_linter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_pipeline.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_refactorizer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_watcher.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cache.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_category.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cpg.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_dead_code.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_dead_code.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_mermaid.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_explain.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_explain.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_exporter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_exporter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_hotspots.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_hotspots.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layer_rules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layer_rules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layers.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_linter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_linter.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_linter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mermaid.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_models.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_documentation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_exporter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_hotspots.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_layer_rules.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_rule_gen.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_sarif.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_projections.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_projections.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rank.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_refactorizer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rule_gen.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rule_gen.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_sarif.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_security.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_security.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_taint.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_taint.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_uml.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_uml.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_watcher.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_c.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_python.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_go.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_rust.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_javascript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_java.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_csharp.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_shell.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_php.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_dart.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_gdscript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_nim.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_assembly.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_ruby.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_swift.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_kotlin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_scala.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_lua.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_elixir.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_base.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_base.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_c.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_c.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_go.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_go.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_java.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_java.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_php.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_php.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_python.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_python.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator.py", "target": "readmenator/__main__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cache.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cache.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_config.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cursorrules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cursorrules.py", "target": "readmenator/_cursorrules_generator.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cursorrules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dead_code.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dead_code.py", "target": "readmenator/_dead_code.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dead_code.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_documentation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_exporter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_hotspots.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integration.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integration.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_layer_rules.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_linter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_linter.py", "target": "readmenator/_linter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_linter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mcp_server.py", "target": "readmenator/_mcp_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mcp_server.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mcp_server.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mermaid.py", "target": "readmenator/_mermaid.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mermaid.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_models.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_new.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_new.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_python.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_c.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_go.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_rust.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_javascript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_java.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_csharp.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_shell.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_php.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_dart.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_gdscript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_nim.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_ruby.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_swift.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_kotlin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_scala.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_lua.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_elixir.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_query.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_query.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_explain.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_projections.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_readme_injector.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_refactorizer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_resolver.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_rule_gen.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_sarif.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_uml.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_uml.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_uml.py", "target": "readmenator/_uml.py"}], "generator": "readmenator", "metadata": {"edge_count": 7076, "file_count": 98, "language_count": 2, "symbol_count": 1214}, "nodes": [{"doc": "Refactoring plan for readmenator/_app.py Current lines: 643 Estimated impact: 5 files", "id": ".refactor__app.sh", "kind": "module", "label": ".refactor__app.sh", "language": "sh", "sha256": "c8d43a13618ada63", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for readmenator/_documentation.py Current lines: 1087 Estimated impact: 2 files", "id": ".refactor__documentation.sh", "kind": "module", "label": ".refactor__documentation.sh", "language": "sh", "sha256": "f9bd232cf1c6c97c", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for readmenator/_exporter.py Current lines: 898 Estimated impact: 2 files", "id": ".refactor__exporter.sh", "kind": "module", "label": ".refactor__exporter.sh", "language": "sh", "sha256": "4b921693f3908484", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for readmenator/_mcp_server.py Current lines: 813 Estimated impact: 3 files", "id": ".refactor__mcp_server.sh", "kind": "module", "label": ".refactor__mcp_server.sh", "language": "sh", "sha256": "00b150a21022fbf9", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for readmenator/_rank.py Current lines: 537 Estimated impact: 7 files", "id": ".refactor__rank.sh", "kind": "module", "label": ".refactor__rank.sh", "language": "sh", "sha256": "7bf93113424dc019", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for readmenator/_security.py Current lines: 583 Estimated impact: 2 files", "id": ".refactor__security.sh", "kind": "module", "label": ".refactor__security.sh", "language": "sh", "sha256": "06b7e053ad8e70bd", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for readmenator/_uml.py Current lines: 599 Estimated impact: 4 files", "id": ".refactor__uml.sh", "kind": "module", "label": ".refactor__uml.sh", "language": "sh", "sha256": "b5a426ccbd90baef", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for tests/test_parsers.py Current lines: 487 Estimated impact: 0 files", "id": ".refactor_test_parsers.sh", "kind": "module", "label": ".refactor_test_parsers.sh", "language": "sh", "sha256": "2c732237a693061c", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for tests/test_ranking.py Current lines: 666 Estimated impact: 0 files", "id": ".refactor_test_ranking.sh", "kind": "module", "label": ".refactor_test_ranking.sh", "language": "sh", "sha256": "18a1938e1ea8b4a3", "symbol_count": 0, "symbols": []}, {"doc": "Refactoring plan for tests/test_uml.py Current lines: 488 Estimated impact: 0 files", "id": ".refactor_test_uml.sh", "kind": "module", "label": ".refactor_test_uml.sh", "language": "sh", "sha256": "6cc41d327ff14a26", "symbol_count": 0, "symbols": []}, {"id": "readmenator/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "693c306a8ca0b67d", "symbol_count": 0, "symbols": []}, {"id": "readmenator/__main__.py", "kind": "module", "label": "__main__.py", "language": "py", "sha256": "83b65ab33d00543c", "symbol_count": 3, "symbols": [{"kind": "function", "line": 15, "name": "build_parser", "signature": "def build_parser()"}, {"kind": "function", "line": 97, "name": "_run_tests", "signature": "def _run_tests()"}, {"kind": "function", "line": 112, "name": "main", "signature": "def main()"}]}, {"id": "readmenator/_analyzer.py", "kind": "module", "label": "_analyzer.py", "language": "py", "sha256": "d56e0b4c1dbc4e05", "symbol_count": 13, "symbols": [{"doc": "Deterministic graph analysis over scanned nodes and edges.\n\nBuilds an internal adjacency graph from import edges, then applies\ncommunity detection, centrality scoring, cross-community bridge\ndiscovery, and question generation without any external API calls.", "kind": "class", "line": 20, "name": "GraphAnalyzer", "signature": "class GraphAnalyzer"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings for thresholds and limits.", "kind": "method", "line": 28, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run the full analysis pipeline and return structured results.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges from the scanner.\n    resolved_edges: Optional list of resolved-import edges (source and\n        target are both project file IDs).\n\nReturns:\n    An AnalysisResult with god nodes, communities, surprising\n    connections, and suggested questions.", "kind": "method", "line": 36, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges)"}, {"doc": "Build an undirected adjacency map from import edges.", "kind": "method", "line": 89, "name": "_build_adjacency", "signature": "def _build_adjacency(self, nodes, edges)"}, {"doc": "Build a directed reverse adjacency (incoming edges) map.", "kind": "method", "line": 103, "name": "_build_reverse_adjacency", "signature": "def _build_reverse_adjacency(self, adjacency)"}, {"doc": "Compute the most central nodes using combined degree centrality.\n\nScore is a combination of out-degree (imports), in-degree (imported-by),\nand symbol count. Higher score means more architecturally significant.", "kind": "method", "line": 113, "name": "_compute_god_nodes", "signature": "def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)"}, {"doc": "Detect communities using label propagation.\n\nEach node adopts the most frequent community label among its\nneighbors. Iterates until convergence or max iterations reached.\nSimple, deterministic, and correct for connected graphs.", "kind": "method", "line": 135, "name": "_detect_communities", "signature": "def _detect_communities(self, nodes, adjacency)"}, {"doc": "Generate human-readable labels for communities.\n\nLabels are based on the most common directory within the community.", "kind": "method", "line": 186, "name": "_label_communities", "signature": "def _label_communities(self, nodes, communities)"}, {"doc": "Build a reverse map from file ID to community ID.", "kind": "method", "line": 213, "name": "_build_community_map", "signature": "def _build_community_map(self, communities)"}, {"doc": "Compute cohesion score for each community.\n\nCohesion = internal edges / (internal edges + external edges).", "kind": "method", "line": 223, "name": "_compute_cohesion", "signature": "def _compute_cohesion(self, communities, adjacency)"}, {"doc": "Find non-obvious cross-community bridges.\n\nA connection is surprising when two nodes in different communities\nare connected indirectly through 3 or more hops, and the path\ncrosses community boundaries.", "kind": "method", "line": 248, "name": "_find_surprising_connections", "signature": "def _find_surprising_connections(self, nodes, adjacency, community_map)"}, {"doc": "Find the shortest path and communities traversed.", "kind": "method", "line": 288, "name": "_shortest_path_communities", "signature": "def _shortest_path_communities(self, source, target, adjacency, community_map)"}, {"doc": "Generate plain-language exploration questions from graph structure.", "kind": "method", "line": 315, "name": "_suggest_questions", "signature": "def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)"}]}, {"id": "readmenator/_app.py", "kind": "module", "label": "_app.py", "language": "py", "sha256": "bb21ec6f7162eb83", "symbol_count": 37, "symbols": [{"kind": "class", "line": 33, "name": "readmenatorApplication", "signature": "class readmenatorApplication"}, {"kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 43, "name": "_scan", "signature": "def _scan(self, target_dir)"}, {"kind": "method", "line": 51, "name": "_scan_with_content", "signature": "def _scan_with_content(self, target_dir)"}, {"kind": "method", "line": 61, "name": "_resolve_imports", "signature": "def _resolve_imports(self, nodes, edges, target_dir)"}, {"kind": "method", "line": 80, "name": "run", "signature": "def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)"}, {"kind": "method", "line": 174, "name": "_write_sidecar_outputs", "signature": "def _write_sidecar_outputs(self, root, findings, analysis_v2)"}, {"kind": "method", "line": 200, "name": "_inject_readme_link", "signature": "def _inject_readme_link(self, root)"}, {"kind": "method", "line": 208, "name": "generate_uml_code", "signature": "def generate_uml_code(self, target_dir, language, output_path)"}, {"kind": "method", "line": 220, "name": "_log_summary", "signature": "def _log_summary(self, nodes, edges, resolved_edges, analysis, layer_summary, analysis_v2, findings)"}, {"kind": "method", "line": 274, "name": "update", "signature": "def update(self, target_dir, run_security)"}, {"kind": "method", "line": 362, "name": "_scan_for_cache", "signature": "def _scan_for_cache(self, root, cache)"}, {"kind": "method", "line": 380, "name": "query", "signature": "def query(self, target_dir, question)"}, {"kind": "method", "line": 385, "name": "explain", "signature": "def explain(self, target_dir, symbol_name)"}, {"kind": "method", "line": 397, "name": "find_path", "signature": "def find_path(self, target_dir, symbol_a, symbol_b)"}, {"kind": "method", "line": 410, "name": "summary", "signature": "def summary(self, target_dir)"}, {"doc": "Run a ranked query against the knowledge graph.\n\nUses Personalized PageRank seeded from query terms to produce\na relevance-ranked list of files with score decomposition.\n\nArgs:\n    target_dir: Project root directory.\n    query: Free-text query.\n    top_n: Number of results.\n\nReturns:\n    A RankedResult with scored items.", "kind": "method", "line": 415, "name": "rank_query", "signature": "def rank_query(self, target_dir, query, top_n)"}, {"kind": "method", "line": 445, "name": "rebuild", "signature": "def rebuild(self, target_dir, run_security)"}, {"kind": "method", "line": 448, "name": "analyze", "signature": "def analyze(self, target_dir)"}, {"kind": "method", "line": 452, "name": "export_json", "signature": "def export_json(self, target_dir, output_path)"}, {"kind": "method", "line": 463, "name": "export_html", "signature": "def export_html(self, target_dir, output_path)"}, {"kind": "method", "line": 474, "name": "export_svg", "signature": "def export_svg(self, target_dir, output_path)"}, {"kind": "method", "line": 485, "name": "export", "signature": "def export(self, target_dir)"}, {"kind": "method", "line": 490, "name": "export_graphml", "signature": "def export_graphml(self, target_dir, output_path)"}, {"kind": "method", "line": 501, "name": "export_cypher", "signature": "def export_cypher(self, target_dir, output_path)"}, {"kind": "method", "line": 514, "name": "export_obsidian", "signature": "def export_obsidian(self, target_dir, output_dir)"}, {"kind": "method", "line": 524, "name": "watch", "signature": "def watch(self, target_dir)"}, {"kind": "method", "line": 534, "name": "audit", "signature": "def audit(self, target_dir)"}, {"kind": "method", "line": 541, "name": "audit_deep", "signature": "def audit_deep(self, target_dir)"}, {"kind": "method", "line": 561, "name": "export_sarif", "signature": "def export_sarif(self, target_dir, output_path)"}, {"kind": "method", "line": 571, "name": "export_rules", "signature": "def export_rules(self, target_dir, output_dir)"}, {"kind": "method", "line": 581, "name": "detect_layers", "signature": "def detect_layers(self, target_dir)"}, {"kind": "method", "line": 591, "name": "lint", "signature": "def lint(self, target_dir)"}, {"kind": "method", "line": 604, "name": "strip_dead_code", "signature": "def strip_dead_code(self, target_dir)"}, {"kind": "method", "line": 614, "name": "generate_cursorrules", "signature": "def generate_cursorrules(self, target_dir)"}, {"kind": "method", "line": 629, "name": "refactor_monolith", "signature": "def refactor_monolith(self, target_dir)"}, {"kind": "method", "line": 528, "name": "on_change", "signature": "def on_change()"}]}, {"id": "readmenator/_cache.py", "kind": "module", "label": "_cache.py", "language": "py", "sha256": "bc1d2673948b4971", "symbol_count": 13, "symbols": [{"doc": "SHA256-based cache for incremental file scanning and analysis.\n\nStores a JSON mapping of relative file paths to their content\nhashes inside the project's cache directory. On subsequent runs,\nfiles whose hash matches the cached value are skipped.\n\nAlso caches analysis results so that unchanged files reuse\npreviously-computed security findings, taint paths, etc.", "kind": "class", "line": 20, "name": "FileCache", "signature": "class FileCache"}, {"kind": "method", "line": 31, "name": "__init__", "signature": "def __init__(self, config, project_root)"}, {"kind": "method", "line": 38, "name": "load", "signature": "def load(self)"}, {"kind": "method", "line": 49, "name": "save", "signature": "def save(self, hashes)"}, {"kind": "method", "line": 55, "name": "compute_hash", "signature": "def compute_hash(self, file_path)"}, {"kind": "method", "line": 64, "name": "compute_hashes", "signature": "def compute_hashes(self, file_paths)"}, {"kind": "method", "line": 72, "name": "find_changed", "signature": "def find_changed(self, file_paths)"}, {"kind": "method", "line": 84, "name": "prune_deleted", "signature": "def prune_deleted(self, current_file_ids)"}, {"doc": "Save an analysis result to the semantic cache.\n\nArgs:\n    key: Cache key (e.g. \"security\", \"analysis_v2\", \"taint\").\n    data: Serializable analysis data.", "kind": "method", "line": 95, "name": "save_analysis", "signature": "def save_analysis(self, key, data)"}, {"doc": "Load a previously cached analysis result.\n\nArgs:\n    key: Cache key.\n\nReturns:\n    Cached data dict, or None if not found or expired.", "kind": "method", "line": 118, "name": "load_analysis", "signature": "def load_analysis(self, key)"}, {"doc": "Clear analysis cache, optionally for a specific key only.\n\nArgs:\n    key: If given, only clears this key. Otherwise clears all.", "kind": "method", "line": 135, "name": "clear_analysis", "signature": "def clear_analysis(self, key)"}, {"doc": "Remove analysis entries for files that no longer exist.", "kind": "method", "line": 155, "name": "_prune_analysis_cache", "signature": "def _prune_analysis_cache(self, current_file_ids)"}, {"doc": "Check if any file has changed since the last analysis cache.\n\nReturns True if there are no cached hashes (first run) or if\nany file hash differs from the cached value.", "kind": "method", "line": 166, "name": "has_changed_since_last_analysis", "signature": "def has_changed_since_last_analysis(self, file_paths)"}]}, {"id": "readmenator/_category.py", "kind": "module", "label": "_category.py", "language": "py", "sha256": "22dd68c7de95ca42", "symbol_count": 26, "symbols": [{"doc": "Semantic type of a morphism between two code artifacts.", "kind": "class", "line": 24, "name": "EdgeKind", "signature": "class EdgeKind(str, Enum)"}, {"doc": "A typed directed edge between two code artifacts.\n\nAttributes:\n    source: Node ID of the source artifact.\n    target: Node ID of the target artifact.\n    kind: Semantic type of the relationship.\n    confidence: Confidence score from static analysis (0.0 to 1.0).", "kind": "class", "line": 57, "name": "Morphism", "signature": "class Morphism"}, {"doc": "A category of code artifacts with typed morphisms.\n\nObjects are node IDs (file paths or symbol identifiers).\nMorphisms are typed directed edges. Composition follows\ncompatible source/target chains respecting edge-kind semantics.", "kind": "class", "line": 78, "name": "Category", "signature": "class Category"}, {"doc": "Weighted directed graph for PageRank computations.\n\nConverts a Category into a stochastic transition matrix suitable\nfor eigenvalue computation, preserving edge kind weights.", "kind": "class", "line": 181, "name": "TypedGraph", "signature": "class TypedGraph"}, {"doc": "Build a Category from lists of Edge objects.\n\nMaps Edge.relation strings to EdgeKind where possible.\nUnrecognised relation strings are mapped to DEPENDS_ON.\n\nArgs:\n    edges: Raw import edges from the scanner.\n    resolved_edges: Optional resolved-import edges.\n    node_ids: Optional set of valid node IDs to include.\n\nReturns:\n    A populated Category instance.", "kind": "method", "line": 236, "name": "build_category_from_edges", "signature": "def build_category_from_edges(edges, resolved_edges, node_ids)"}, {"doc": "Map a relation string to an EdgeKind.\n\nFalls back to DEPENDS_ON for unrecognised strings.", "kind": "method", "line": 280, "name": "_infer_edge_kind", "signature": "def _infer_edge_kind(relation)"}, {"kind": "method", "line": 38, "name": "__str__", "signature": "def __str__(self)"}, {"doc": "Effective weight for ranking = semantic weight * confidence.", "kind": "method", "line": 73, "name": "weight", "signature": "def weight(self)"}, {"kind": "method", "line": 86, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 92, "name": "add_object", "signature": "def add_object(self, obj_id)"}, {"kind": "method", "line": 95, "name": "add_morphism", "signature": "def add_morphism(self, m)"}, {"kind": "method", "line": 103, "name": "objects", "signature": "def objects(self)"}, {"kind": "method", "line": 107, "name": "morphisms", "signature": "def morphisms(self)"}, {"kind": "method", "line": 110, "name": "outgoing", "signature": "def outgoing(self, obj_id)"}, {"kind": "method", "line": 113, "name": "incoming", "signature": "def incoming(self, obj_id)"}, {"doc": "Compose two morphisms if target of a matches source of b.\n\nReturns a new Morphism with composite kind, or None if\nthe kinds are incompatible.", "kind": "method", "line": 116, "name": "compose", "signature": "def compose(self, a, b)"}, {"doc": "Find all composition paths from source to target up to max_depth.", "kind": "method", "line": 133, "name": "paths", "signature": "def paths(self, source, target, max_depth)"}, {"doc": "Determine the composite edge kind.\n\nComposition rules:\n- imports + defines -> defines (reachable definition)\n- imports + calls -> calls (reachable call)\n- defines + tests -> tests (tested through definition)\n- documents + defines -> documents (documented definition)\n- Same kind -> same kind.\n- Other combinations -> None (incompatible).", "kind": "method", "line": 157, "name": "_compose_kind", "signature": "def _compose_kind(a, b)"}, {"kind": "method", "line": 188, "name": "__init__", "signature": "def __init__(self, category)"}, {"kind": "method", "line": 197, "name": "_compute_out_weights", "signature": "def _compute_out_weights(self)"}, {"kind": "method", "line": 203, "name": "nodes", "signature": "def nodes(self)"}, {"kind": "method", "line": 207, "name": "size", "signature": "def size(self)"}, {"kind": "method", "line": 210, "name": "node_index", "signature": "def node_index(self, node_id)"}, {"doc": "Sum of weights of all morphisms from source to target.", "kind": "method", "line": 213, "name": "transition_weight", "signature": "def transition_weight(self, source, target)"}, {"doc": "Return dict of target -> probability for the row of *source*.\n\nProbabilities sum to 1.0 if source has outgoing edges.\nReturns empty dict for dangling nodes.", "kind": "method", "line": 221, "name": "stochastic_row", "signature": "def stochastic_row(self, source)"}, {"kind": "method", "line": 139, "name": "dfs", "signature": "def dfs(current, goal, path, depth)"}]}, {"id": "readmenator/_config.py", "kind": "module", "label": "_config.py", "language": "py", "sha256": "a5ac9a21b5bd0467", "symbol_count": 1, "symbols": [{"doc": "Single source of truth for all readmenator settings.\n\nEvery tuneable constant -- file-size limits, directory depth,\nsupported extensions, symbol pluralisation map, Mermaid style\ntokens, graph analysis thresholds, and export settings -- is\ndefined here and consumed by reference elsewhere.", "kind": "class", "line": 15, "name": "Config", "signature": "class Config"}]}, {"id": "readmenator/_cpg.py", "kind": "module", "label": "_cpg.py", "language": "py", "sha256": "ab3301bc458fdd9c", "symbol_count": 6, "symbols": [{"doc": "Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.\n\nProduces a structured representation merging AST-level symbol data,\ncontrol-flow edges (calls), data-flow edges (imports), inheritance\nrelationships, and security findings (with MITRE ATT&CK mappings)\ninto a single machine-readable document. Designed to be embedded in\nKNOWLEDGE_BASE.md for zero-token agent context.", "kind": "class", "line": 10, "name": "CodePropertyGraph", "signature": "class CodePropertyGraph"}, {"kind": "method", "line": 20, "name": "__init__", "signature": "def __init__(self, privacy_mode, cpg_context)"}, {"doc": "Generate the CPG JSON-LD string embeddable in markdown.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for metadata.\n    findings: Optional security findings with MITRE ATT&CK IDs.\n\nReturns:\n    Compact JSON-LD string with @context, nodes, edges, analysis,\n    and mitre_attack metadata.", "kind": "method", "line": 24, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, findings)"}, {"kind": "method", "line": 141, "name": "_severity_counts", "signature": "def _severity_counts(self, findings)"}, {"kind": "method", "line": 147, "name": "_build_symbol_list", "signature": "def _build_symbol_list(self, node)"}, {"kind": "method", "line": 163, "name": "_compute_node_hash", "signature": "def _compute_node_hash(node)"}]}, {"id": "readmenator/_cursorrules_generator.py", "kind": "module", "label": "_cursorrules_generator.py", "language": "py", "sha256": "df7fb514feb68f04", "symbol_count": 8, "symbols": [{"doc": "Generates a .cursorrules file from architectural analysis.\n\nCombines base rules, detected layer constraints, and active\nlinter violations into a deterministic ruleset for AI assistants.", "kind": "class", "line": 18, "name": "CursorRulesGenerator", "signature": "class CursorRulesGenerator"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate the .cursorrules content string.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    analysis: Optional analysis results.\n    layers: Optional layer mapping.\n    violations: Optional linter violations.\n    project_root: Optional project root for file output.\n\nReturns:\n    The generated .cursorrules content as a string.", "kind": "method", "line": 28, "name": "generate", "signature": "def generate(self, nodes, edges, analysis, layers, violations, project_root)"}, {"kind": "method", "line": 63, "name": "_build_base_rules", "signature": "def _build_base_rules(self)"}, {"kind": "method", "line": 81, "name": "_extract_layer_constraints", "signature": "def _extract_layer_constraints(self, layers)"}, {"kind": "method", "line": 92, "name": "_extract_analysis_constraints", "signature": "def _extract_analysis_constraints(self, analysis)"}, {"kind": "method", "line": 107, "name": "_extract_violation_rules", "signature": "def _extract_violation_rules(self, violations)"}, {"kind": "method", "line": 115, "name": "_write_file", "signature": "def _write_file(self, project_root, content)"}]}, {"id": "readmenator/_dead_code.py", "kind": "module", "label": "_dead_code.py", "language": "py", "sha256": "9606c78ecbfacbd6", "symbol_count": 5, "symbols": [{"doc": "Identifies dead code symbols in the knowledge graph.\n\nBuilds an in-degree map from resolved import edges, then flags\nsymbols that are never imported by any other file. Known entry\npoints are excluded from the dead code report.", "kind": "class", "line": 17, "name": "DeadCodeStripper", "signature": "class DeadCodeStripper"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Identify dead code symbols with zero in-degree.\n\nArgs:\n    nodes: Scanned file nodes with symbols.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n\nReturns:\n    List of DeadCodeReport instances for orphaned symbols.", "kind": "method", "line": 28, "name": "identify", "signature": "def identify(self, nodes, edges, resolved_edges)"}, {"doc": "Build in-degree count for each symbol name.", "kind": "method", "line": 64, "name": "_build_in_degree_map", "signature": "def _build_in_degree_map(self, nodes, resolved_edges)"}, {"doc": "Classify the recommended action for a dead symbol.", "kind": "method", "line": 88, "name": "_classify_recommendation", "signature": "def _classify_recommendation(self, symbol)"}]}, {"id": "readmenator/_documentation.py", "kind": "module", "label": "_documentation.py", "language": "py", "sha256": "3578656522b8e7dd", "symbol_count": 27, "symbols": [{"doc": "Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.\n\nDelegates graph rendering to MermaidRenderer and handles the\nMarkdown layout: header metadata, Mermaid block, statistics dashboard,\ngod nodes, community analysis, surprising connections, architecture\nlayers, security audit, taint analysis, hotspots, dependency cycles,\nchange impact, architecture violations, suggested rules, CPG block,\nranking metadata, orphans, query recipes, and per-language architecture\nsections with pluralised symbol kind headings.", "kind": "class", "line": 27, "name": "DocumentationGenerator", "signature": "class DocumentationGenerator"}, {"kind": "method", "line": 39, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 57, "name": "_ranking_version", "signature": "def _ranking_version(self)"}, {"kind": "method", "line": 75, "name": "_get_git_commit", "signature": "def _get_git_commit()"}, {"kind": "method", "line": 85, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)"}, {"kind": "method", "line": 158, "name": "_apply_context_budget", "signature": "def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)"}, {"kind": "method", "line": 296, "name": "_build_toc", "signature": "def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)"}, {"kind": "method", "line": 381, "name": "_build_layers", "signature": "def _build_layers(self, layers, nodes)"}, {"kind": "method", "line": 415, "name": "_build_dashboard", "signature": "def _build_dashboard(self, nodes, edges, resolved_edges)"}, {"kind": "method", "line": 495, "name": "_build_god_nodes", "signature": "def _build_god_nodes(self, analysis, ranked)"}, {"kind": "method", "line": 523, "name": "_build_community_analysis", "signature": "def _build_community_analysis(self, analysis, nodes)"}, {"kind": "method", "line": 556, "name": "_build_surprising_connections", "signature": "def _build_surprising_connections(self, analysis, nodes)"}, {"kind": "method", "line": 581, "name": "_build_suggested_questions", "signature": "def _build_suggested_questions(self, analysis)"}, {"kind": "method", "line": 597, "name": "_build_ranked_context", "signature": "def _build_ranked_context(self, ranked)"}, {"doc": "Build a section listing nodes with low coverage signals.", "kind": "method", "line": 643, "name": "_build_orphans", "signature": "def _build_orphans(self, nodes, analysis_v2, ranked)"}, {"kind": "method", "line": 693, "name": "_build_query_recipes", "signature": "def _build_query_recipes(self)"}, {"kind": "method", "line": 735, "name": "_build_taint_analysis", "signature": "def _build_taint_analysis(self, analysis_v2)"}, {"kind": "method", "line": 770, "name": "_build_hotspots", "signature": "def _build_hotspots(self, analysis_v2, ranked)"}, {"kind": "method", "line": 808, "name": "_build_dependency_cycles", "signature": "def _build_dependency_cycles(self, analysis_v2)"}, {"kind": "method", "line": 828, "name": "_build_change_impact", "signature": "def _build_change_impact(self, analysis_v2)"}, {"kind": "method", "line": 853, "name": "_build_layer_violations", "signature": "def _build_layer_violations(self, analysis_v2)"}, {"kind": "method", "line": 881, "name": "_build_suggested_rules", "signature": "def _build_suggested_rules(self, analysis_v2)"}, {"kind": "method", "line": 906, "name": "_build_security_findings", "signature": "def _build_security_findings(self, findings)"}, {"kind": "method", "line": 953, "name": "_build_mermaid_section", "signature": "def _build_mermaid_section(self, graph_output, is_truncated)"}, {"kind": "method", "line": 976, "name": "_build_uml_diagram", "signature": "def _build_uml_diagram(self, nodes, edges)"}, {"kind": "method", "line": 1002, "name": "_build_cpg_block", "signature": "def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)"}, {"kind": "method", "line": 1028, "name": "_build_architecture_reference", "signature": "def _build_architecture_reference(self, nodes, edges)"}]}, {"id": "readmenator/_explain.py", "kind": "module", "label": "_explain.py", "language": "py", "sha256": "1c5e324fb42169ed", "symbol_count": 3, "symbols": [{"doc": "Return a detailed breakdown of why *node_id* has its rank.\n\nIncludes score decomposition, seed paths, and quality signals.\n\nArgs:\n    node_id: The node to explain.\n    ranked: The RankedResult containing scores.\n    category: Optional Category for enriched path details.\n\nReturns:\n    Formatted explanation string, or None if node_id not found.", "kind": "function", "line": 16, "name": "explain_rank", "signature": "def explain_rank(node_id, ranked, category)"}, {"doc": "Return a short summary of the top-N ranked results.", "kind": "function", "line": 140, "name": "rank_summary", "signature": "def rank_summary(ranked, top_n)"}, {"kind": "function", "line": 163, "name": "_find_item", "signature": "def _find_item(node_id, items)"}]}, {"id": "readmenator/_exporter.py", "kind": "module", "label": "_exporter.py", "language": "py", "sha256": "8e3d442940cf31b1", "symbol_count": 15, "symbols": [{"doc": "Exports the knowledge graph to JSON, HTML, and SVG formats.\n\nEach method is self-contained and produces a single file. No\nexternal network calls are made; the HTML file embeds vis.js\nfrom a CDN reference for offline-compatible rendering.", "kind": "class", "line": 21, "name": "GraphExporter", "signature": "class GraphExporter"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings for export styling and limits.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Export the graph as a node-link JSON string.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for metadata.\n    findings: Optional security audit findings.\n\nReturns:\n    JSON string with nodes, edges, and optional analysis/findings metadata.", "kind": "method", "line": 37, "name": "to_json", "signature": "def to_json(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Generate a standalone interactive HTML graph page.\n\nUses vis.js loaded from CDN. Supports click-to-inspect nodes,\nsearch filtering, and community-based coloring.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community coloring.\n\nReturns:\n    Complete HTML document as a string.", "kind": "method", "line": 150, "name": "to_html", "signature": "def to_html(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Build a node-to-color map based on community membership.", "kind": "method", "line": 236, "name": "_community_color_map", "signature": "def _community_color_map(self, analysis)"}, {"doc": "Lighten a hex color by 30% for border use.", "kind": "method", "line": 254, "name": "_lighten", "signature": "def _lighten(hex_color)"}, {"doc": "Render the full HTML document with vis.js.", "kind": "method", "line": 262, "name": "_render_html", "signature": "def _render_html(self, vis_nodes, vis_edges, analysis, findings)"}, {"doc": "Generate a static SVG representation of the graph.\n\nUses a simple force-directed layout without external dependencies.\nFor graphs with more than SVG_MAX_NODES, returns a plain SVG\nwith a truncation message.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community coloring.\n\nReturns:\n    SVG document as a string.", "kind": "method", "line": 421, "name": "to_svg", "signature": "def to_svg(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Render a minimal SVG with a truncation notice.", "kind": "method", "line": 539, "name": "_render_truncated_svg", "signature": "def _render_truncated_svg(self, total_nodes)"}, {"doc": "Compute a simple spring-layout for node positioning.\n\nImplements a basic force-directed layout with repulsion\nbetween all nodes and attraction along edges. Runs a fixed\nnumber of iterations for determinism.", "kind": "method", "line": 554, "name": "_layout_spring", "signature": "def _layout_spring(self, nodes, edges, node_map)"}, {"doc": "Export the graph as GraphML (Gephi/yEd compatible).\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community data.\n\nReturns:\n    GraphML XML string.", "kind": "method", "line": 635, "name": "to_graphml", "signature": "def to_graphml(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Export the graph as native Cypher CREATE statements.\n\nGenerates Neo4j/Memgraph-compatible Cypher for direct graph\ndatabase ingestion. Each file node becomes a ``(:File)`` node,\nimport dependencies become ``(:File)-[:IMPORTS]->(:File)``\nrelationships. Optional security findings are attached as node\nproperties and standalone ``(:SecurityFinding)`` nodes.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community metadata.\n    findings: Optional security finding nodes.\n\nReturns:\n    String of Cypher CREATE statements.", "kind": "method", "line": 712, "name": "to_cypher", "signature": "def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Export the graph as an Obsidian vault with wikilinks.\n\nEach file node becomes a markdown note. Community hub notes\naggregate related files. All notes use [[wikilinks]] for\nObsidian graph navigation.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    output_dir: Directory to write the Obsidian notes.\n    analysis: Optional analysis results for community hubs.\n\nReturns:\n    Number of notes written.", "kind": "method", "line": 817, "name": "to_obsidian", "signature": "def to_obsidian(self, nodes, edges, output_dir, analysis)"}, {"kind": "method", "line": 483, "name": "_project", "signature": "def _project(pos)"}, {"kind": "method", "line": 334, "name": "_sev_span", "signature": "def _sev_span(sev, count)"}]}, {"id": "readmenator/_hotspots.py", "kind": "module", "label": "_hotspots.py", "language": "py", "sha256": "55e2be7374ada787", "symbol_count": 7, "symbols": [{"doc": "Hotspot detection, cycle analysis, and change impact analysis.\n\nHotspots are files with high complexity (many symbols) and high\ncentrality (many connections). Cycle detection finds circular\ndependencies in the resolved import graph. Change impact analysis\ncomputes transitive-dependent lists for every file.", "kind": "class", "line": 16, "name": "HotspotAnalyzer", "signature": "class HotspotAnalyzer"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Rank files by combined complexity and centrality scores.\n\nComplexity is normalised symbol count. Centrality is normalised\nconnection count (in-degree + out-degree). The combined score\nuses configured weights.", "kind": "method", "line": 28, "name": "analyze_hotspots", "signature": "def analyze_hotspots(self, nodes, edges, resolved_edges)"}, {"doc": "Detect cycles in the resolved import graph using DFS.\n\nUses Tarjan's algorithm variant with three-colour DFS to find\nall elementary cycles. Returns each cycle as a DependencyCycle.", "kind": "method", "line": 84, "name": "detect_cycles", "signature": "def detect_cycles(self, nodes, resolved_edges)"}, {"doc": "Compute change impact for every file in the project.\n\nFor each file, finds all files that would be affected if it\nchanged (direct and transitive dependents via reverse import\ngraph traversal).", "kind": "method", "line": 149, "name": "analyze_change_impact", "signature": "def analyze_change_impact(self, nodes, resolved_edges)"}, {"kind": "method", "line": 108, "name": "_dfs_visit", "signature": "def _dfs_visit(current)"}, {"kind": "method", "line": 119, "name": "_record_cycle", "signature": "def _record_cycle(start, end)"}]}, {"id": "readmenator/_layer_rules.py", "kind": "module", "label": "_layer_rules.py", "language": "py", "sha256": "8349f119aa3b1869", "symbol_count": 4, "symbols": [{"doc": "Architectural layer violation detection engine.\n\nDefines a set of permitted and forbidden layer-to-layer import\nrules. Scans all resolved import edges and flags violations\nwhere one layer imports from another in a way that violates\nthe architecture.", "kind": "class", "line": 9, "name": "LayerRuleEngine", "signature": "class LayerRuleEngine"}, {"kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Detect architectural layer violations.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved import edges.\n    layers: Dict mapping node_id to layer name. If None, imports\n        _layers.LayerDetector for automatic detection.\n\nReturns:\n    List of LayerViolation instances.", "kind": "method", "line": 37, "name": "detect_violations", "signature": "def detect_violations(self, nodes, edges, resolved_edges, layers)"}, {"doc": "Summarise violations by severity.", "kind": "method", "line": 109, "name": "violation_summary", "signature": "def violation_summary(violations)"}]}, {"id": "readmenator/_layers.py", "kind": "module", "label": "_layers.py", "language": "py", "sha256": "eca6996d1404b8ec", "symbol_count": 4, "symbols": [{"doc": "Detects architectural layers in a codebase.\n\nAssigns each file to a layer based on path patterns, naming\nconventions, and imported frameworks. Returns a mapping that\ncan enrich documentation and analysis. No config dependency.", "kind": "class", "line": 15, "name": "LayerDetector", "signature": "class LayerDetector"}, {"doc": "Assign each file node to an architectural layer.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n\nReturns:\n    Dict mapping node_id to layer name.", "kind": "method", "line": 71, "name": "detect", "signature": "def detect(self, nodes, edges)"}, {"doc": "Classify a single file into an architectural layer.", "kind": "method", "line": 89, "name": "_classify_file", "signature": "def _classify_file(self, node, edges)"}, {"doc": "Count files per layer.\n\nArgs:\n    layers: Mapping from detect().\n\nReturns:\n    Dict of layer_name -> file_count.", "kind": "method", "line": 122, "name": "layer_summary", "signature": "def layer_summary(layers)"}]}, {"id": "readmenator/_linter.py", "kind": "module", "label": "_linter.py", "language": "py", "sha256": "f3c1132fa2972d19", "symbol_count": 7, "symbols": [{"doc": "Enforces architectural rules over scanned nodes and edges.\n\nChecks file length, cross-layer import violations, and circular\ndependencies. Returns structured LinterViolation instances for\neach detected issue.", "kind": "class", "line": 18, "name": "ArchitectureLinter", "signature": "class ArchitectureLinter"}, {"kind": "method", "line": 31, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run all linter rules and return violations.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    layers: Optional mapping from node_id to layer name.\n    content_map: Optional mapping from node_id to file content.\n\nReturns:\n    List of LinterViolation instances sorted by severity.", "kind": "method", "line": 34, "name": "lint", "signature": "def lint(self, nodes, edges, resolved_edges, layers, content_map)"}, {"doc": "Check files against maximum line count threshold.", "kind": "method", "line": 65, "name": "_check_file_length", "signature": "def _check_file_length(self, nodes, content_map)"}, {"doc": "Check for forbidden cross-layer imports.", "kind": "method", "line": 96, "name": "_check_cross_layer_violations", "signature": "def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)"}, {"doc": "Check for circular dependencies in the resolved import graph.", "kind": "method", "line": 127, "name": "_check_circular_dependencies", "signature": "def _check_circular_dependencies(self, nodes, resolved_edges)"}, {"kind": "method", "line": 146, "name": "_dfs", "signature": "def _dfs(current)"}]}, {"id": "readmenator/_mcp_server.py", "kind": "module", "label": "_mcp_server.py", "language": "py", "sha256": "96151f2ad60cfb2d", "symbol_count": 52, "symbols": [{"kind": "class", "line": 58, "name": "MCPError", "signature": "class MCPError(Exception)"}, {"kind": "class", "line": 71, "name": "MCPRequest", "signature": "class MCPRequest"}, {"kind": "class", "line": 92, "name": "MCPTool", "signature": "class MCPTool"}, {"kind": "class", "line": 119, "name": "MCPResource", "signature": "class MCPResource"}, {"kind": "class", "line": 146, "name": "MCPServer", "signature": "class MCPServer"}, {"doc": "CLI entry point for `readmenator serve <path>`.", "kind": "method", "line": 796, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 59, "name": "__init__", "signature": "def __init__(self, code, message, data)"}, {"kind": "method", "line": 72, "name": "__init__", "signature": "def __init__(self, msg)"}, {"kind": "method", "line": 79, "name": "is_notification", "signature": "def is_notification(self)"}, {"kind": "method", "line": 82, "name": "response", "signature": "def response(self, result)"}, {"kind": "method", "line": 85, "name": "error", "signature": "def error(self, code, message, data)"}, {"kind": "method", "line": 93, "name": "__init__", "signature": "def __init__(self, name, description, handler, input_schema)"}, {"kind": "method", "line": 108, "name": "definition", "signature": "def definition(self)"}, {"kind": "method", "line": 115, "name": "call", "signature": "def call(self, arguments)"}, {"kind": "method", "line": 120, "name": "__init__", "signature": "def __init__(self, uri, name, description, mime_type, handler)"}, {"kind": "method", "line": 134, "name": "definition", "signature": "def definition(self)"}, {"kind": "method", "line": 142, "name": "read", "signature": "def read(self)"}, {"kind": "method", "line": 147, "name": "__init__", "signature": "def __init__(self, app, target_dir)"}, {"kind": "method", "line": 155, "name": "register_tool", "signature": "def register_tool(self, tool)"}, {"kind": "method", "line": 158, "name": "register_resource", "signature": "def register_resource(self, resource)"}, {"kind": "method", "line": 161, "name": "_ensure_kb", "signature": "def _ensure_kb(self)"}, {"kind": "method", "line": 173, "name": "_handle_initialize", "signature": "def _handle_initialize(self, req)"}, {"kind": "method", "line": 187, "name": "_handle_list_tools", "signature": "def _handle_list_tools(self, req)"}, {"kind": "method", "line": 192, "name": "_handle_call_tool", "signature": "def _handle_call_tool(self, req)"}, {"kind": "method", "line": 214, "name": "_handle_list_resources", "signature": "def _handle_list_resources(self, req)"}, {"kind": "method", "line": 219, "name": "_handle_read_resource", "signature": "def _handle_read_resource(self, req)"}, {"kind": "method", "line": 241, "name": "dispatch", "signature": "def dispatch(self, req)"}, {"kind": "method", "line": 261, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 285, "name": "_register_all", "signature": "def _register_all(self)"}, {"kind": "method", "line": 467, "name": "_scan", "signature": "def _scan(self)"}, {"kind": "method", "line": 473, "name": "_scan_deep", "signature": "def _scan_deep(self)"}, {"kind": "method", "line": 481, "name": "_tool_summary", "signature": "def _tool_summary(self)"}, {"kind": "method", "line": 519, "name": "_tool_query", "signature": "def _tool_query(self, text)"}, {"kind": "method", "line": 524, "name": "_tool_explain", "signature": "def _tool_explain(self, name)"}, {"kind": "method", "line": 536, "name": "_tool_path", "signature": "def _tool_path(self, symbol_a, symbol_b)"}, {"kind": "method", "line": 547, "name": "_tool_findings", "signature": "def _tool_findings(self, min_severity)"}, {"kind": "method", "line": 577, "name": "_tool_security_summary", "signature": "def _tool_security_summary(self)"}, {"kind": "method", "line": 582, "name": "_tool_taint", "signature": "def _tool_taint(self)"}, {"kind": "method", "line": 603, "name": "_tool_hotspots", "signature": "def _tool_hotspots(self, top_n)"}, {"kind": "method", "line": 619, "name": "_tool_cycles", "signature": "def _tool_cycles(self)"}, {"kind": "method", "line": 630, "name": "_tool_communities", "signature": "def _tool_communities(self)"}, {"kind": "method", "line": 645, "name": "_tool_layers", "signature": "def _tool_layers(self)"}, {"kind": "method", "line": 663, "name": "_tool_layer_violations", "signature": "def _tool_layer_violations(self)"}, {"kind": "method", "line": 679, "name": "_tool_rebuild", "signature": "def _tool_rebuild(self)"}, {"kind": "method", "line": 689, "name": "_tool_update", "signature": "def _tool_update(self)"}, {"kind": "method", "line": 697, "name": "_tool_export_json", "signature": "def _tool_export_json(self)"}, {"kind": "method", "line": 705, "name": "_resource_summary", "signature": "def _resource_summary(self)"}, {"kind": "method", "line": 722, "name": "_resource_graph", "signature": "def _resource_graph(self)"}, {"kind": "method", "line": 741, "name": "_resource_findings", "signature": "def _resource_findings(self)"}, {"kind": "method", "line": 757, "name": "_resource_analysis", "signature": "def _resource_analysis(self)"}, {"kind": "method", "line": 787, "name": "_resource_kb", "signature": "def _resource_kb(self)"}, {"kind": "method", "line": 791, "name": "_get_query_engine", "signature": "def _get_query_engine(self, nodes, edges, resolved)"}]}, {"id": "readmenator/_mermaid.py", "kind": "module", "label": "_mermaid.py", "language": "py", "sha256": "5832baaa4731cd40", "symbol_count": 4, "symbols": [{"doc": "Renders a knowledge graph to Mermaid JS flowchart syntax.\n\nNodes are ordered by import count and symbol richness; the top\n``max_nodes`` entries are included. External dependencies appear\nas dashed boxes. Internal import edges are solid arrows.\nCommunity subgraphs group related files when analysis is available.", "kind": "class", "line": 17, "name": "MermaidRenderer", "signature": "class MermaidRenderer"}, {"kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)"}, {"doc": "Convert *node_id* to a Mermaid-safe identifier.\n\nReplaces non-alphanumeric characters with underscores and\nprepends ``n_`` if the result starts with a digit.", "kind": "method", "line": 45, "name": "_sanitize_id", "signature": "def _sanitize_id(node_id)"}, {"doc": "Produce a Mermaid flowchart string and a truncation flag.\n\nNodes are sorted by import popularity, then by symbol count.\nInternal import edges (between project files) are rendered as\nsolid arrows when *resolved_edges* is provided. Community\nsubgraphs wrap related files when *analysis* is given.\n\nReturns:\n    Tuple of (Mermaid source string, is_truncated bool).", "kind": "method", "line": 56, "name": "render", "signature": "def render(self, nodes, edges, resolved_edges, analysis)"}]}, {"id": "readmenator/_models.py", "kind": "module", "label": "_models.py", "language": "py", "sha256": "11d46ca7191153de", "symbol_count": 19, "symbols": [{"doc": "A single code symbol extracted from a source file.\n\nAttributes:\n    name: Identifier of the symbol (class name, function name, etc.).\n    kind: Semantic type (class, function, struct, enum, ...).\n    line: One-based line number where the symbol is defined.\n    doc: Optional docstring or comment extracted from the source.\n    signature: Optional method or function signature snippet.", "kind": "class", "line": 18, "name": "Symbol", "signature": "class Symbol"}, {"doc": "A file node in the knowledge graph, containing its symbols.\n\nAttributes:\n    node_id: Relative path of the file used as a unique identifier.\n    label: Base file name for display purposes.\n    kind: Type of node (typically \"module\").\n    language: Programming language derived from the file extension.\n    doc: Optional file-level documentation string.\n    symbols: List of Symbol instances defined in this file.", "kind": "class", "line": 37, "name": "Node", "signature": "class Node"}, {"doc": "A directed relationship between two nodes in the knowledge graph.\n\nAttributes:\n    source: Node ID of the source (dependent) file.\n    target: Node ID of the target (dependency) file or module.\n    relation: Semantic relation label (e.g. \"imports\", \"resolved_imports\").\n    confidence: Confidence tier (\"EXTRACTED\" for structural, \"INFERRED\" for heuristic).\n    kind: Optional typed edge kind for ranking-aware computations.", "kind": "class", "line": 58, "name": "Edge", "signature": "class Edge"}, {"doc": "A security-relevant pattern detected in a source file.\n\nAttributes:\n    file_path: Relative path of the file containing the finding.\n    line: One-based line number where the pattern was found.\n    severity: Severity level (critical, high, medium, low, info).\n    rule_id: Unique identifier for the detection rule (e.g. \"PY001\").\n    description: Human-readable explanation of the issue.\n    snippet: The offending source code line.\n    cwe: CWE identifier string (e.g. \"CWE-78\").\n    mitre_attack: MITRE ATT&CK technique ID (e.g. \"T1059.001\").", "kind": "class", "line": 77, "name": "SecurityFinding", "signature": "class SecurityFinding"}, {"doc": "Return the plural form of *kind* according to *plural_map*.\n\nFalls back to appending ``\"s\"`` when the kind is not found.\nThis prevents obvious misspellings like ``\"Classs\"``.", "kind": "method", "line": 101, "name": "pluralize_symbol_kind", "signature": "def pluralize_symbol_kind(kind, plural_map)"}, {"doc": "Result of community detection on the import graph.\n\nAttributes:\n    community_id: Integer identifier of the community.\n    label: Human-readable name for the community.\n    file_ids: Set of node IDs belonging to this community.\n    cohesion: Cohesion score (internal edges / total edges involving community).\n    size: Number of files in the community.", "kind": "class", "line": 111, "name": "CommunityResult", "signature": "class CommunityResult"}, {"doc": "Complete graph analysis output.\n\nAttributes:\n    god_nodes: List of (node_id, score) for most central nodes.\n    communities: List of CommunityResult instances.\n    surprising_connections: List of (source_node, target_node, hops, bridging_communities).\n    suggested_questions: List of plain-language exploration questions.\n    node_count: Total nodes in the graph.\n    edge_count: Total edges in the graph.", "kind": "class", "line": 130, "name": "AnalysisResult", "signature": "class AnalysisResult"}, {"doc": "A taint propagation path from source to sink through the import graph.\n\nAttributes:\n    source_file: The file that introduces the dangerous import.\n    sink_file: The file that transitively receives the taint.\n    path: List of file node IDs forming the propagation chain.\n    hops: Number of hops in the propagation path.\n    dangerous_import: The specific dangerous module or function imported.\n    severity: Inferred severity of the taint path.", "kind": "class", "line": 151, "name": "TaintPath", "signature": "class TaintPath"}, {"doc": "Complete taint propagation analysis output.\n\nAttributes:\n    paths: List of TaintPath instances discovered.\n    source_count: Number of unique taint source files.\n    sink_count: Number of unique taint sink files.", "kind": "class", "line": 172, "name": "TaintAnalysisResult", "signature": "class TaintAnalysisResult"}, {"doc": "A cycle detected in the resolved import graph.\n\nAttributes:\n    cycle: List of file node IDs forming the cycle.\n    length: Number of files in the cycle.", "kind": "class", "line": 187, "name": "DependencyCycle", "signature": "class DependencyCycle"}, {"doc": "Change impact analysis for a single file.\n\nAttributes:\n    file_id: The file that would be changed.\n    direct_dependents: Files that directly import this file.\n    transitive_dependents: Files that transitively depend on this file.\n    total_impact: Total number of affected files (direct + transitive).", "kind": "class", "line": 200, "name": "ChangeImpact", "signature": "class ChangeImpact"}, {"doc": "A hotspot file combining complexity and centrality metrics.\n\nAttributes:\n    file_id: The file node ID.\n    complexity_score: Normalised symbol count score (0-1).\n    centrality_score: Normalised god node score (0-1).\n    combined_score: Weighted combination of complexity and centrality.\n    symbol_count: Raw symbol count.\n    connection_count: Raw connection count.", "kind": "class", "line": 217, "name": "HotspotResult", "signature": "class HotspotResult"}, {"doc": "A suggested linting/security rule derived from code patterns.\n\nAttributes:\n    rule_id: Suggested rule identifier (e.g. \"RM001\").\n    severity: Suggested severity (info, warning, error).\n    description: Human-readable description of the pattern.\n    pattern: The detected pattern or code snippet.\n    file_examples: Example file paths where the pattern was found.\n    match_count: Number of times the pattern was matched.\n    language: Target language for the rule.\n    semgrep_yaml: Optional Semgrep rule YAML string.", "kind": "class", "line": 238, "name": "SuggestedRule", "signature": "class SuggestedRule"}, {"doc": "A detected architectural layer violation.\n\nAttributes:\n    source_file: The file causing the violation.\n    source_layer: The layer of the source file.\n    target_file: The file being imported.\n    target_layer: The layer of the target file.\n    description: Description of the violation.\n    severity: Severity (strict, warn, info).", "kind": "class", "line": 263, "name": "LayerViolation", "signature": "class LayerViolation"}, {"doc": "Extended analysis result combining all new analysis modules.\n\nAttributes:\n    taint: Optional taint analysis result.\n    cycles: List of dependency cycles.\n    change_impacts: List of change impact results for key files.\n    hotspots: List of hotspot results.\n    suggested_rules: List of suggested linting rules.\n    layer_violations: List of layer violations.", "kind": "class", "line": 284, "name": "AnalysisResultV2", "signature": "class AnalysisResultV2"}, {"doc": "A violation detected by the architecture linter.\n\nAttributes:\n    file_path: Relative path of the file containing the violation.\n    rule_id: Unique identifier for the linter rule (e.g. \"ARC001\").\n    severity: Severity level (error, warning, info).\n    message: Human-readable description of the violation.", "kind": "class", "line": 305, "name": "LinterViolation", "signature": "class LinterViolation"}, {"doc": "A dead code symbol identified by the stripper.\n\nAttributes:\n    file_path: Relative path of the file containing the symbol.\n    symbol_name: Name of the dead symbol.\n    symbol_type: Type of symbol (function, class, method, etc.).\n    recommendation: Recommended action (MOVE_TO_TRASH, REVIEW, KEEP).", "kind": "class", "line": 322, "name": "DeadCodeReport", "signature": "class DeadCodeReport"}, {"doc": "A single refactoring action within a plan.\n\nAttributes:\n    action_type: Type of action (EXTRACT_CLASS, EXTRACT_FUNCTION, MOVE_SYMBOL).\n    source_file: The file to refactor.\n    start_line: Start line of the code range to extract.\n    end_line: End line of the code range to extract.\n    target_file: The new file to create (for EXTRACT actions).\n    description: Human-readable description of the action.", "kind": "class", "line": 339, "name": "RefactoringAction", "signature": "class RefactoringAction"}, {"doc": "A complete refactoring plan for a monolithic file.\n\nAttributes:\n    file_path: The file to refactor.\n    actions: List of refactoring actions to perform.\n    estimated_impact: Number of files affected by the refactoring.\n    current_lines: Current line count of the file.", "kind": "class", "line": 360, "name": "RefactoringPlan", "signature": "class RefactoringPlan"}]}, {"id": "readmenator/_pipeline.py", "kind": "module", "label": "_pipeline.py", "language": "py", "sha256": "240886314ab08124", "symbol_count": 23, "symbols": [{"doc": "Lazy factory for all readmenator analyzer and generator instances.\n\nDecouples the application orchestrator from the concrete\ninstantiation of analysis modules. Each component is created\non first access and cached for the lifetime of the factory.", "kind": "class", "line": 36, "name": "AnalyzerFactory", "signature": "class AnalyzerFactory"}, {"doc": "Orchestrates the extended V2 analysis pipeline.\n\nRuns taint propagation, hotspot detection, cycle detection,\nchange impact, layer violations, and rule generation as a\ncoordinated batch. Isolated from the main app to reduce\ncoupling in the primary orchestration layer.", "kind": "class", "line": 187, "name": "DeepAnalysisRunner", "signature": "class DeepAnalysisRunner"}, {"kind": "method", "line": 44, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 64, "name": "scanner", "signature": "def scanner(self)"}, {"kind": "method", "line": 70, "name": "generator", "signature": "def generator(self)"}, {"kind": "method", "line": 76, "name": "analyzer", "signature": "def analyzer(self)"}, {"kind": "method", "line": 82, "name": "security", "signature": "def security(self)"}, {"kind": "method", "line": 88, "name": "exporter", "signature": "def exporter(self)"}, {"kind": "method", "line": 94, "name": "taint", "signature": "def taint(self)"}, {"kind": "method", "line": 100, "name": "hotspots", "signature": "def hotspots(self)"}, {"kind": "method", "line": 106, "name": "layer_rules", "signature": "def layer_rules(self)"}, {"kind": "method", "line": 112, "name": "rule_gen", "signature": "def rule_gen(self)"}, {"kind": "method", "line": 118, "name": "sarif", "signature": "def sarif(self)"}, {"kind": "method", "line": 124, "name": "cpg", "signature": "def cpg(self)"}, {"kind": "method", "line": 133, "name": "layer_detector", "signature": "def layer_detector(self)"}, {"kind": "method", "line": 139, "name": "uml", "signature": "def uml(self)"}, {"kind": "method", "line": 145, "name": "readme_injector", "signature": "def readme_injector(self)"}, {"kind": "method", "line": 152, "name": "build_typed_graph", "signature": "def build_typed_graph(self, nodes, edges, resolved_edges)"}, {"doc": "Create a CompositeRanker for the given typed graph.", "kind": "method", "line": 162, "name": "make_ranker", "signature": "def make_ranker(self, typed_graph)"}, {"kind": "method", "line": 179, "name": "last_category", "signature": "def last_category(self)"}, {"kind": "method", "line": 183, "name": "last_typed_graph", "signature": "def last_typed_graph(self)"}, {"kind": "method", "line": 196, "name": "__init__", "signature": "def __init__(self, factory)"}, {"kind": "method", "line": 199, "name": "run", "signature": "def run(self, nodes, edges, resolved_edges, layers, content_map)"}]}, {"id": "readmenator/_projections.py", "kind": "module", "label": "_projections.py", "language": "py", "sha256": "1bf2c182b76b0945", "symbol_count": 15, "symbols": [{"doc": "A functor from C_code to another category.\n\nMaps nodes and morphisms while preserving composition structure.", "kind": "class", "line": 17, "name": "Projection", "signature": "class Projection(Protocol)"}, {"doc": "Identity functor: maps everything to itself.", "kind": "class", "line": 32, "name": "IdentityProjection", "signature": "class IdentityProjection"}, {"doc": "F_docs: project code to documentation.\n\nKeeps only nodes that have docstrings or are referenced in README.\nUseful for quantifying documentation gaps.", "kind": "class", "line": 42, "name": "DocProjection", "signature": "class DocProjection"}, {"doc": "F_risk: project code to risk/fragility nodes.\n\nNodes are transformed with risk attributes: fan-in, fan-out,\nsymbol count, test absence, and public API exposure.", "kind": "class", "line": 63, "name": "RiskProjection", "signature": "class RiskProjection"}, {"doc": "Apply a named view to produce a projected category.\n\nView config format::\n    {\n        \"edge_types\": [EdgeKind.IMPORTS, EdgeKind.DEFINES, ...],\n        \"direction\": \"forward\" | \"reverse\",  # default \"forward\"\n    }\n\nArgs:\n    category: Source category.\n    view_config: View definition dict.\n\nReturns:\n    A new Category with only matching morphisms.", "kind": "method", "line": 95, "name": "apply_view", "signature": "def apply_view(category, view_config)"}, {"doc": "Map a code node. Return None to exclude.", "kind": "method", "line": 23, "name": "map_node", "signature": "def map_node(self, node)"}, {"doc": "Map a morphism. Return None to exclude.", "kind": "method", "line": 27, "name": "map_morphism", "signature": "def map_morphism(self, m)"}, {"kind": "method", "line": 35, "name": "map_node", "signature": "def map_node(self, node)"}, {"kind": "method", "line": 38, "name": "map_morphism", "signature": "def map_morphism(self, m)"}, {"kind": "method", "line": 49, "name": "__init__", "signature": "def __init__(self, documented_ids)"}, {"kind": "method", "line": 52, "name": "map_node", "signature": "def map_node(self, node)"}, {"kind": "method", "line": 57, "name": "map_morphism", "signature": "def map_morphism(self, m)"}, {"kind": "method", "line": 70, "name": "__init__", "signature": "def __init__(self, fan_in, fan_out, test_files)"}, {"kind": "method", "line": 80, "name": "map_node", "signature": "def map_node(self, node)"}, {"kind": "method", "line": 91, "name": "map_morphism", "signature": "def map_morphism(self, m)"}]}, {"id": "readmenator/_query.py", "kind": "module", "label": "_query.py", "language": "py", "sha256": "4677486e84eaae1c", "symbol_count": 17, "symbols": [{"doc": "In-memory query engine over the scanned knowledge graph.\n\nBuilds a symbol-name index and an import-adjacency graph on\nconstruction. Provides exact and fuzzy symbol lookup, detailed\nexplanation output, BFS shortest-path resolution, free-text\nsearch, and a summary report.", "kind": "class", "line": 25, "name": "QueryEngine", "signature": "class QueryEngine"}, {"doc": "Initialise internal indexes from scanned data.\n\nArgs:\n    nodes: List of scanned file nodes.\n    edges: List of import-relationship edges.\n    resolved_edges: Optional resolved-import edges (both\n        source and target are project file IDs).\n    ranker: Optional CompositeRanker for ranked queries.\n    config: Optional RankConfig if ranker is not provided.", "kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, nodes, edges, resolved_edges, ranker, config)"}, {"doc": "Build a default CompositeRanker from the loaded data.", "kind": "method", "line": 64, "name": "_init_default_ranker", "signature": "def _init_default_ranker(self)"}, {"doc": "Answer *query* with a ranked list of relevant nodes.\n\nUses Personalized PageRank seeded from lexical matches\nagainst the query text, combined with authority, test\ncoverage, doc coverage, and freshness signals.\n\nArgs:\n    query: Free-text query string.\n    top_n: Number of results to return (default: RankConfig.top_n).\n\nReturns:\n    A RankedResult with scored items and explanations.", "kind": "method", "line": 73, "name": "ranked_query", "signature": "def ranked_query(self, query, top_n)"}, {"doc": "Estimate test coverage per file.\n\nA file is considered 'tested' if a test file imports it.\nReturns fraction of symbols referenced across test files.", "kind": "method", "line": 124, "name": "_estimate_test_coverage", "signature": "def _estimate_test_coverage(self)"}, {"doc": "Estimate documentation coverage per file.\n\nA file has doc coverage if it has a file-level docstring or\nany of its symbols have docstrings.", "kind": "method", "line": 150, "name": "_estimate_doc_coverage", "signature": "def _estimate_doc_coverage(self)"}, {"doc": "Build a name-to-list-of-(node, symbol) lookup.\n\nReturns:\n    Dict mapping symbol names to list of (Node, Symbol) tuples.", "kind": "method", "line": 170, "name": "_build_symbol_index", "signature": "def _build_symbol_index(self)"}, {"doc": "Build an adjacency map from import edges.\n\nReturns:\n    Dict mapping each file node_id to its set of import targets.", "kind": "method", "line": 184, "name": "_build_import_graph", "signature": "def _build_import_graph(self)"}, {"doc": "Build an adjacency map from resolved import edges.\n\nOnly contains edges where both source and target are\nproject files (not external modules).\n\nReturns:\n    Dict mapping each file node_id to files it imports within the project.", "kind": "method", "line": 200, "name": "_build_resolved_graph", "signature": "def _build_resolved_graph(self)"}, {"doc": "Look up *name* by exact match, then by substring fuzzy match.\n\nReturns:\n    A list of (Node, Symbol) tuples, or ``None`` if not found.", "kind": "method", "line": 220, "name": "find_symbol", "signature": "def find_symbol(self, name)"}, {"doc": "Return a detailed multi-line explanation of *name*.\n\nIncludes kind, file path, line number, docstring, signature,\nimports, reverse dependencies (\"imported by\"), and sibling\nsymbols in the same file.\n\nReturns:\n    Formatted string or ``None`` if the symbol is not found.", "kind": "method", "line": 238, "name": "explain", "signature": "def explain(self, name)"}, {"doc": "List all node IDs that import *target*.", "kind": "method", "line": 277, "name": "_find_incoming_imports", "signature": "def _find_incoming_imports(self, target)"}, {"doc": "Find the shortest import path from *symbol_a* to *symbol_b*.\n\nUses BFS on the resolved import graph (project-internal edges)\nfirst, traversing in both directions (forward = A imports B,\nreverse = B is imported by A). Falls back to the raw import\ngraph if no resolved path exists.\n\nReturns:\n    List of file node IDs forming the dependency chain, or ``None``.", "kind": "method", "line": 285, "name": "find_path", "signature": "def find_path(self, symbol_a, symbol_b)"}, {"doc": "Convert a directed graph to a bidirectional one.\n\nFor each edge A→B, adds both A→B and B→A edges.", "kind": "method", "line": 315, "name": "_make_bidirectional", "signature": "def _make_bidirectional(graph)"}, {"doc": "Run BFS to find the shortest path from *start* to *goal*.\n\nReturns:\n    List of node IDs or ``None`` if no path exists.", "kind": "method", "line": 331, "name": "_bfs_shortest_path", "signature": "def _bfs_shortest_path(self, graph, start, goal)"}, {"doc": "Free-text search over symbols and file paths.\n\nTokenises the input, matches against symbol names (substring)\nand then against file paths as a fallback. Returns a\nhuman-readable result string summarising matches or a\nno-results message with KB statistics.", "kind": "method", "line": 355, "name": "query", "signature": "def query(self, question)"}, {"doc": "Return a concise overview of the loaded knowledge base.\n\nReports file count, symbol count, import count, language\ndiversity, top-level modules (by import popularity), and\nlists of key class-like and function-like symbols.", "kind": "method", "line": 411, "name": "summary", "signature": "def summary(self)"}]}, {"id": "readmenator/_rank.py", "kind": "module", "label": "_rank.py", "language": "py", "sha256": "9cea35495030eb51", "symbol_count": 17, "symbols": [{"doc": "Tuneable parameters for the ranking system.\n\nAttributes:\n    alpha: Damping factor for PageRank (default 0.85).\n    max_iter: Maximum power-iteration steps.\n    tolerance: Convergence threshold (L1 norm).\n    top_n: Default number of ranked results to return.\n    noise_penalty: Multiplier applied to hub-penalty names\n        when they are not part of the query seeds.\n    composite_ppr_weight: Weight for PPR in composite score.\n    composite_authority_weight: Weight for global PageRank.\n    composite_test_weight: Weight for test coverage signal.\n    composite_doc_weight: Weight for documentation coverage.\n    composite_freshness_weight: Weight for code freshness.", "kind": "class", "line": 32, "name": "RankConfig", "signature": "class RankConfig"}, {"doc": "Compute global PageRank on the typed weighted graph.\n\nUses power iteration on the stochastic matrix derived from\nthe TypedGraph's edge weights. Dangling nodes (no outgoing\nedges) are handled by uniform random teleportation.\n\nArgs:\n    graph: A TypedGraph instance with weighted edges.\n    alpha: Damping factor (probability of following an edge).\n    max_iter: Maximum power-iteration steps.\n    tolerance: Convergence threshold (L1 norm).\n\nReturns:\n    Dict mapping node_id -> PageRank score. Scores sum to 1.0.", "kind": "method", "line": 61, "name": "global_pagerank", "signature": "def global_pagerank(graph, alpha, max_iter, tolerance)"}, {"doc": "Compute Personalized PageRank with a seed-node preference vector.\n\nInstead of uniform teleportation, probability mass is distributed\naccording to the seed vector. This makes the ranking sensitive to\na specific query or context.\n\nArgs:\n    graph: A TypedGraph instance.\n    seeds: Dict mapping seed node_id -> preference mass (sums to 1.0).\n    alpha: Damping factor.\n    max_iter: Maximum power-iteration steps.\n    tolerance: Convergence threshold (L1 norm).\n\nReturns:\n    Dict mapping node_id -> PPR score. Scores sum to 1.0.", "kind": "method", "line": 119, "name": "personalized_pagerank", "signature": "def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)"}, {"doc": "Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.\n\nAuthorities are nodes with many incoming edges from good hubs.\nHubs are nodes with many outgoing edges to good authorities.\n\nReturns:\n    Tuple of (authorities, hubs) as dicts mapping node_id -> score.\n    Scores are L2-normalised.", "kind": "method", "line": 189, "name": "hits", "signature": "def hits(graph, max_iter, tolerance)"}, {"doc": "Build a PPR seed vector from a natural-language query string.\n\nMatches query tokens against node IDs, labels, and symbol names.\nSeeds are assigned equal mass. If no match is found, returns\nempty dict (will use uniform teleportation).\n\nArgs:\n    query: Free-text query string.\n    node_ids: All valid node IDs.\n    node_labels: Mapping from node_id -> display label.\n    symbols: Mapping from node_id -> list of symbol names.\n\nReturns:\n    Dict of seed node_id -> equal mass fraction.", "kind": "method", "line": 240, "name": "build_seeds_from_query", "signature": "def build_seeds_from_query(query, node_ids, node_labels, symbols)"}, {"doc": "Build a PPR seed vector from anchor pattern strings.\n\nNodes whose ID or label contains any anchor pattern receive\nequal seed mass. Useful for section-level seeding.\n\nArgs:\n    node_ids: All valid node IDs.\n    anchor_patterns: List of substrings to match.\n\nReturns:\n    Dict of seed node_id -> equal mass fraction.", "kind": "method", "line": 286, "name": "build_seeds_for_context", "signature": "def build_seeds_for_context(node_ids, anchor_patterns)"}, {"doc": "A single ranked result with score decomposition.\n\nAttributes:\n    node_id: The ranked node ID.\n    composite_score: Final multi-signal score.\n    ppr_score: Personalized PageRank contribution.\n    authority_score: Global PageRank contribution.\n    test_coverage: Fraction of symbols referenced in test files.\n    doc_coverage: Fraction of symbols with documentation.\n    freshness: Decay-weighted recency signal.\n    justification_paths: Shortest paths from seed nodes to this node.", "kind": "class", "line": 320, "name": "RankedItem", "signature": "class RankedItem"}, {"doc": "Complete ranking result for a query or context.\n\nAttributes:\n    query: The query string or context label.\n    items: Ranked items in descending score order.\n    config: The RankConfig used.\n    seed_nodes: The seed node IDs used for PPR.\n    model_version: Version identifier for the ranking model.", "kind": "class", "line": 349, "name": "RankedResult", "signature": "class RankedResult"}, {"doc": "Combines PPR, authority, test/doc coverage, and freshness.\n\nProduces a single composite score per node:\nS_q(n) = w_ppr * PPR_q(n) + w_auth * Auth(n) + w_test * Test(n)\n       + w_doc * Doc(n) + w_fresh * Fresh(n)", "kind": "class", "line": 377, "name": "CompositeRanker", "signature": "class CompositeRanker"}, {"doc": "Format a human-readable explanation for a ranked item.", "kind": "method", "line": 512, "name": "_format_explanation", "signature": "def _format_explanation(item, result)"}, {"kind": "method", "line": 344, "name": "label", "signature": "def label(self)"}, {"kind": "method", "line": 366, "name": "top", "signature": "def top(self, n)"}, {"doc": "Return a human-readable explanation of why *node_id* ranks as it does.", "kind": "method", "line": 369, "name": "explain", "signature": "def explain(self, node_id)"}, {"kind": "method", "line": 385, "name": "__init__", "signature": "def __init__(self, graph, config)"}, {"kind": "method", "line": 394, "name": "_get_global_pr", "signature": "def _get_global_pr(self)"}, {"doc": "Compute composite ranking for a query.\n\nArgs:\n    query: Query string.\n    seeds: PPR seed vector.\n    category: Category with morphisms for path finding.\n    node_ids: All valid node IDs.\n    test_coverage: Optional dict of node_id -> test coverage (0-1).\n    doc_coverage: Optional dict of node_id -> doc coverage (0-1).\n    freshness: Optional dict of node_id -> freshness (0-1).\n\nReturns:\n    A RankedResult with scored and sorted items.", "kind": "method", "line": 404, "name": "rank", "signature": "def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)"}, {"doc": "Find shortest paths from any seed to target.", "kind": "method", "line": 486, "name": "_find_justification_paths", "signature": "def _find_justification_paths(self, target, seed_ids, category, max_paths)"}]}, {"id": "readmenator/_readme_injector.py", "kind": "module", "label": "_readme_injector.py", "language": "py", "sha256": "e99fd65ef4803223", "symbol_count": 6, "symbols": [{"doc": "Injects a link to KNOWLEDGE_BASE.md into the project README.\n\nDetects the project's README file, checks if injection is already\npresent, and appends a descriptive section about the knowledge base\nso that both human developers and AI agents know it exists.", "kind": "class", "line": 49, "name": "ReadmeInjector", "signature": "class ReadmeInjector"}, {"kind": "method", "line": 57, "name": "__init__", "signature": "def __init__(self, kb_filename)"}, {"kind": "method", "line": 60, "name": "inject", "signature": "def inject(self, project_root)"}, {"kind": "method", "line": 82, "name": "remove", "signature": "def remove(self, project_root)"}, {"kind": "method", "line": 111, "name": "_find_readme", "signature": "def _find_readme(root)"}, {"kind": "method", "line": 118, "name": "_build_injection", "signature": "def _build_injection(self, suffix)"}]}, {"id": "readmenator/_refactorizer.py", "kind": "module", "label": "_refactorizer.py", "language": "py", "sha256": "e7441939d0acf9ea", "symbol_count": 9, "symbols": [{"doc": "Generates refactoring plans for monolithic files.\n\nAnalyzes files exceeding the line threshold, extracts symbol\nboundaries, detects cohesive clusters via import analysis, and\nproduces structured refactoring plans without auto-execution.", "kind": "class", "line": 24, "name": "MonolithRefactorizer", "signature": "class MonolithRefactorizer"}, {"kind": "method", "line": 32, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Identify monolithic files and generate refactoring plans.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    content_map: Optional mapping from node_id to file content.\n\nReturns:\n    List of RefactoringPlan instances for files needing refactoring.", "kind": "method", "line": 35, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges, content_map)"}, {"kind": "method", "line": 70, "name": "_get_line_count", "signature": "def _get_line_count(self, file_id, content_map)"}, {"kind": "method", "line": 82, "name": "_plan_refactoring", "signature": "def _plan_refactoring(self, node, edges, resolved_edges, content_map)"}, {"kind": "method", "line": 126, "name": "_group_symbols_by_kind", "signature": "def _group_symbols_by_kind(self, symbols)"}, {"kind": "method", "line": 132, "name": "_suggest_target_file", "signature": "def _suggest_target_file(self, source_file, kind)"}, {"kind": "method", "line": 147, "name": "_estimate_impact", "signature": "def _estimate_impact(self, file_id, resolved_edges)"}, {"kind": "method", "line": 156, "name": "generate_script", "signature": "def generate_script(self, plan, project_root)"}]}, {"id": "readmenator/_resolver.py", "kind": "module", "label": "_resolver.py", "language": "py", "sha256": "e90a8f4bbda2c204", "symbol_count": 11, "symbols": [{"doc": "Resolves raw import strings to project file paths.\n\nUses heuristics tuned to each language's import conventions:\nPython dots to slashes, Java dots to directory separators,\nrelative-path resolution, and extensionless module detection.", "kind": "class", "line": 15, "name": "ImportResolver", "signature": "class ImportResolver"}, {"doc": "Initialise the resolver with all known file paths.\n\nArgs:\n    file_ids: List of relative file paths from the scan.\n    root: Root directory for relative-path resolution.", "kind": "method", "line": 58, "name": "__init__", "signature": "def __init__(self, file_ids, root)"}, {"doc": "Map file stems (without extension) to their full paths.", "kind": "method", "line": 70, "name": "_build_stem_index", "signature": "def _build_stem_index(self, file_ids)"}, {"doc": "Map directory paths to the files they contain.", "kind": "method", "line": 80, "name": "_build_dir_index", "signature": "def _build_dir_index(self, file_ids)"}, {"doc": "Resolve an import string to a concrete project file path.\n\nArgs:\n    import_str: The raw import string from the parser.\n    source_file: The file that contains the import (for relative resolution).\n\nReturns:\n    Matching file node ID or ``None`` if no match found.", "kind": "method", "line": 97, "name": "resolve", "signature": "def resolve(self, import_str, source_file)"}, {"doc": "Resolve *import_str* to all possible matching project file paths.\n\nArgs:\n    import_str: The raw import string.\n    source_file: The file that contains the import.\n\nReturns:\n    List of matching file node IDs (may be empty).", "kind": "method", "line": 132, "name": "resolve_all", "signature": "def resolve_all(self, import_str, source_file)"}, {"doc": "Resolve a relative import (starts with ``.`` or ``..``).", "kind": "method", "line": 148, "name": "_resolve_relative", "signature": "def _resolve_relative(self, import_str, source_file)"}, {"doc": "Resolve a bare module name by appending known extensions.", "kind": "method", "line": 166, "name": "_resolve_extensionless", "signature": "def _resolve_extensionless(self, import_str, source_file)"}, {"doc": "Resolve as a package directory with __init__ or index file.", "kind": "method", "line": 175, "name": "_resolve_directory_init", "signature": "def _resolve_directory_init(self, import_str, source_file)"}, {"doc": "Resolve a dotted module path (Python/Java convention).", "kind": "method", "line": 185, "name": "_resolve_module_dotpath", "signature": "def _resolve_module_dotpath(self, import_str)"}, {"doc": "Match by file stem only (last resort).", "kind": "method", "line": 207, "name": "_resolve_stem_match", "signature": "def _resolve_stem_match(self, import_str)"}]}, {"id": "readmenator/_rule_gen.py", "kind": "module", "label": "_rule_gen.py", "language": "py", "sha256": "16bae439053d55e3", "symbol_count": 9, "symbols": [{"doc": "Generates suggested linting and security rules from code patterns.\n\nAnalyses the scanned codebase for repeated patterns that suggest\nproject-specific linting rules: bare except clauses, repeated\ntype annotations, common security antipatterns, and naming\nconvention violations. Outputs Semgrep YAML rules to a directory.", "kind": "class", "line": 12, "name": "RuleGenerator", "signature": "class RuleGenerator"}, {"kind": "method", "line": 88, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate suggested rules by scanning code patterns.\n\nArgs:\n    nodes: Scanned file nodes with symbols.\n    content_map: Optional mapping of file paths to their source content\n        for deeper pattern matching.\n\nReturns:\n    List of SuggestedRule instances.", "kind": "method", "line": 92, "name": "generate", "signature": "def generate(self, nodes, content_map)"}, {"doc": "Write suggested rules to Semgrep YAML files in output_dir.\n\nReturns the number of rule files written.", "kind": "method", "line": 120, "name": "write_rules", "signature": "def write_rules(self, rules, output_dir)"}, {"doc": "Group nodes by their language extension.", "kind": "method", "line": 159, "name": "_group_by_language", "signature": "def _group_by_language(self, nodes)"}, {"doc": "Analyze a single language group for rule suggestions.", "kind": "method", "line": 169, "name": "_analyze_language", "signature": "def _analyze_language(self, lang, nodes, content_map)"}, {"doc": "Detect known antipatterns across all files.", "kind": "method", "line": 202, "name": "_detect_antipatterns", "signature": "def _detect_antipatterns(self, nodes, content_map)"}, {"doc": "Infer target language for a built-in antipattern rule.", "kind": "method", "line": 248, "name": "_infer_language_for_rule", "signature": "def _infer_language_for_rule(rule_id)"}, {"doc": "Generate the next rule identifier.", "kind": "method", "line": 258, "name": "_next_rule_id", "signature": "def _next_rule_id(self)"}]}, {"id": "readmenator/_sarif.py", "kind": "module", "label": "_sarif.py", "language": "py", "sha256": "c7489117abc919be", "symbol_count": 5, "symbols": [{"doc": "Exports security findings to the SARIF standard format.\n\nSARIF is an OASIS standard format for static analysis tool output.\nThis exporter produces SARIF v2.1.0 JSON compatible with GitHub\nCode Scanning, VS Code SARIF viewer, and other SARIF consumers.", "kind": "class", "line": 9, "name": "SarifExporter", "signature": "class SarifExporter"}, {"kind": "method", "line": 28, "name": "__init__", "signature": "def __init__(self, privacy_mode)"}, {"doc": "Generate a SARIF v2.1.0 JSON string from security findings.\n\nArgs:\n    findings: List of SecurityFinding instances.\n    project_name: Name of the scanned project for metadata.\n\nReturns:\n    SARIF JSON string.", "kind": "method", "line": 31, "name": "export", "signature": "def export(self, findings, project_name)"}, {"doc": "Build a SARIF reportingDescriptor (rule) object.", "kind": "method", "line": 80, "name": "_build_rule", "signature": "def _build_rule(self, finding)"}, {"doc": "Build a SARIF result object for a single finding.", "kind": "method", "line": 104, "name": "_build_result", "signature": "def _build_result(self, finding, rule_index)"}]}, {"id": "readmenator/_scanner.py", "kind": "module", "label": "_scanner.py", "language": "py", "sha256": "6694f88c25234419", "symbol_count": 13, "symbols": [{"doc": "Recursive directory scanner with security and size guards.\n\nRejects symlinks, enforces file-size and directory-depth limits,\nskips ignored directories, and silently catches parse errors\nso a single misbehaving file never breaks the full scan.\n\nSupports privacy mode (strips snippets and docstrings) and\ngitignore-aware scanning for more accurate project coverage.", "kind": "class", "line": 22, "name": "PolyglotScanner", "signature": "class PolyglotScanner"}, {"doc": "Initialise the scanner with application configuration.\n\nArgs:\n    config: Settings including ignore dirs, size limits, etc.", "kind": "method", "line": 33, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return ``True`` if any path component matches IGNORE_DIRS.", "kind": "method", "line": 42, "name": "_is_ignored", "signature": "def _is_ignored(self, path)"}, {"doc": "Parse .gitignore patterns using regex (no external deps).", "kind": "method", "line": 46, "name": "_load_gitignore", "signature": "def _load_gitignore(self, root)"}, {"doc": "Convert a .gitignore glob pattern to a regex pattern.", "kind": "method", "line": 68, "name": "_gitignore_glob_to_regex", "signature": "def _gitignore_glob_to_regex(pattern)"}, {"doc": "Check if a relative path matches any .gitignore pattern.", "kind": "method", "line": 108, "name": "_is_gitignored", "signature": "def _is_gitignored(self, rel_path)"}, {"doc": "Reject symlinks and files exceeding MAX_FILE_SIZE_MB.", "kind": "method", "line": 117, "name": "_validate_path_security", "signature": "def _validate_path_security(self, path)"}, {"doc": "Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.", "kind": "method", "line": 130, "name": "_check_directory_depth", "signature": "def _check_directory_depth(self, path, root)"}, {"doc": "Extract a file-level docstring from the first lines of a source file.\n\nWalks the first FILE_HEADER_MAX_LINES lines looking for a contiguous\nblock of comments or a shebang followed by comments. Returns the\nconcatenated comment text.\n\nArgs:\n    content: Raw file content as a string.\n\nReturns:\n    Extracted file-level docstring or empty string.", "kind": "method", "line": 138, "name": "_extract_file_doc", "signature": "def _extract_file_doc(self, content)"}, {"doc": "Emit a progress message every PROGRESS_REPORT_BATCH files.\n\nArgs:\n    count: Number of files scanned so far.", "kind": "method", "line": 191, "name": "_emit_progress", "signature": "def _emit_progress(self, count)"}, {"doc": "Walk *root* recursively and produce (nodes, edges) for the graph.\n\nSecurity checks (symlinks, size, depth, ignore dirs) are applied\nper file. Parse failures are silently caught so a single broken\nfile never blocks the rest of the scan.\n\nReturns:\n    A tuple of (list of Node, list of Edge). Edges represent\n    ``imports`` relationships between scanned files.", "kind": "method", "line": 201, "name": "scan", "signature": "def scan(self, root)"}, {"doc": "Scan and also return raw file contents for deeper analysis.\n\nReturns:\n    Tuple of (nodes, edges, content_map) where content_map maps\n    node_id to raw file content.", "kind": "method", "line": 215, "name": "scan_with_content", "signature": "def scan_with_content(self, root)"}, {"doc": "Internal scan implementation returning nodes, edges, and content.", "kind": "method", "line": 226, "name": "_scan_impl", "signature": "def _scan_impl(self, root)"}]}, {"id": "readmenator/_security.py", "kind": "module", "label": "_security.py", "language": "py", "sha256": "228129489ad16635", "symbol_count": 31, "symbols": [{"doc": "A single security detection rule loaded from YAML or built-in.\n\nAttributes:\n    rule_id: Unique identifier (e.g. \"PY001\").\n    severity: Severity level (critical, high, medium, low, info).\n    description: Human-readable description of the issue.\n    pattern: Compiled regex to search for.\n    cwe: CWE identifier string.\n    mitre_attack: MITRE ATT&CK technique ID (e.g. \"T1059.001\").", "kind": "class", "line": 24, "name": "SecurityRule", "signature": "class SecurityRule"}, {"doc": "Parse the simplified YAML format used by _security_rules.yml.\n\nOnly supports:\n  - top-level ``rules:`` key\n  - list items starting with ``  - rule_id:``\n  - scalar key: value pairs (quoted or unquoted)\n  - block list items: ``    - \"value\"``\n  - inline lists: ``key: [item1, item2]``\n  - ``#`` comments\n\nReturns a list of rule dicts.", "kind": "method", "line": 46, "name": "_parse_minimal_yaml", "signature": "def _parse_minimal_yaml(text)"}, {"kind": "method", "line": 121, "name": "_unquote", "signature": "def _unquote(s)"}, {"doc": "Load rule dicts from the YAML rules file, or return None on failure.", "kind": "method", "line": 128, "name": "_load_rules_from_yaml", "signature": "def _load_rules_from_yaml(yaml_path)"}, {"kind": "method", "line": 148, "name": "_compile", "signature": "def _compile()"}, {"kind": "method", "line": 153, "name": "_python_rules", "signature": "def _python_rules()"}, {"kind": "method", "line": 182, "name": "_javascript_rules", "signature": "def _javascript_rules()"}, {"kind": "method", "line": 201, "name": "_c_rules", "signature": "def _c_rules()"}, {"kind": "method", "line": 222, "name": "_java_rules", "signature": "def _java_rules()"}, {"kind": "method", "line": 237, "name": "_go_rules", "signature": "def _go_rules()"}, {"kind": "method", "line": 250, "name": "_ruby_rules", "signature": "def _ruby_rules()"}, {"kind": "method", "line": 267, "name": "_php_rules", "signature": "def _php_rules()"}, {"kind": "method", "line": 284, "name": "_shell_rules", "signature": "def _shell_rules()"}, {"kind": "method", "line": 297, "name": "_csharp_rules", "signature": "def _csharp_rules()"}, {"kind": "method", "line": 310, "name": "_kotlin_rules", "signature": "def _kotlin_rules()"}, {"kind": "method", "line": 321, "name": "_swift_rules", "signature": "def _swift_rules()"}, {"kind": "method", "line": 332, "name": "_scala_rules", "signature": "def _scala_rules()"}, {"kind": "method", "line": 343, "name": "_lua_rules", "signature": "def _lua_rules()"}, {"kind": "method", "line": 354, "name": "_dart_rules", "signature": "def _dart_rules()"}, {"kind": "method", "line": 365, "name": "_rust_rules", "signature": "def _rust_rules()"}, {"kind": "method", "line": 376, "name": "_nim_rules", "signature": "def _nim_rules()"}, {"kind": "method", "line": 387, "name": "_gdscript_rules", "signature": "def _gdscript_rules()"}, {"kind": "method", "line": 398, "name": "_elixir_rules", "signature": "def _elixir_rules()"}, {"doc": "Attempt to build the rule map from the YAML rules file.\n\nReturns None if the YAML file cannot be loaded or parsed, allowing\nthe caller to fall back to built-in rules.", "kind": "method", "line": 447, "name": "_build_rules_from_yaml", "signature": "def _build_rules_from_yaml(yaml_path)"}, {"doc": "Pattern-based static security scanner.\n\nLoads rules from the external YAML rules file when available,\nfalling back to the built-in hardcoded rule sets. Walks the\ntarget directory applying rules to every supported source file.", "kind": "class", "line": 486, "name": "SecurityAnalyzer", "signature": "class SecurityAnalyzer"}, {"kind": "method", "line": 496, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Resolve rules: prefer YAML, fall back to built-in.", "kind": "method", "line": 500, "name": "_resolve_rules", "signature": "def _resolve_rules(self)"}, {"kind": "method", "line": 509, "name": "_meets_threshold", "signature": "def _meets_threshold(self, severity)"}, {"kind": "method", "line": 513, "name": "scan", "signature": "def scan(self, root)"}, {"kind": "method", "line": 555, "name": "_validate_path", "signature": "def _validate_path(self, path, root)"}, {"kind": "method", "line": 572, "name": "summary", "signature": "def summary(self, findings)"}]}, {"id": "readmenator/_taint.py", "kind": "module", "label": "_taint.py", "language": "py", "sha256": "19fad0e20d2a1629", "symbol_count": 6, "symbols": [{"doc": "Propagation-based taint analysis over the resolved import graph.\n\nIdentifies files that import known-dangerous modules or functions\n(sources) and traces how that danger propagates through the import\ngraph to files that never directly import the dangerous module\nbut receive taint through transitive dependencies.", "kind": "class", "line": 10, "name": "TaintAnalyzer", "signature": "class TaintAnalyzer"}, {"kind": "method", "line": 71, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run taint propagation analysis on the codebase.\n\nScans all nodes for direct dangerous imports, then propagates\ntaint through the resolved import graph. Returns all discovered\ntaint paths from sources to sinks.", "kind": "method", "line": 75, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges)"}, {"doc": "Find files that directly import known-dangerous modules.", "kind": "method", "line": 134, "name": "_find_direct_sources", "signature": "def _find_direct_sources(self, nodes, edges)"}, {"doc": "BFS propagation from source through the import graph.", "kind": "method", "line": 160, "name": "_propagate", "signature": "def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)"}, {"doc": "Build a forward-directed import graph from resolved edges.", "kind": "method", "line": 211, "name": "_build_forward_graph", "signature": "def _build_forward_graph(nodes, resolved_edges)"}]}, {"id": "readmenator/_uml.py", "kind": "module", "label": "_uml.py", "language": "py", "sha256": "92afede9ad575857", "symbol_count": 25, "symbols": [{"kind": "class", "line": 32, "name": "UmlGenerator", "signature": "class UmlGenerator"}, {"kind": "method", "line": 170, "name": "_get_code_generator", "signature": "def _get_code_generator(language)"}, {"kind": "method", "line": 188, "name": "_type_map_py_to_target", "signature": "def _type_map_py_to_target(target, py_type_hint)"}, {"kind": "method", "line": 231, "name": "_generate_cpp", "signature": "def _generate_cpp(class_symbols, nodes, edges)"}, {"kind": "method", "line": 257, "name": "_cpp_params", "signature": "def _cpp_params(params)"}, {"kind": "method", "line": 272, "name": "_generate_java", "signature": "def _generate_java(class_symbols, nodes, edges)"}, {"kind": "method", "line": 299, "name": "_java_params", "signature": "def _java_params(params)"}, {"kind": "method", "line": 314, "name": "_generate_csharp", "signature": "def _generate_csharp(class_symbols, nodes, edges)"}, {"kind": "method", "line": 343, "name": "_cs_params", "signature": "def _cs_params(params)"}, {"kind": "method", "line": 358, "name": "_generate_python", "signature": "def _generate_python(class_symbols, nodes, edges)"}, {"kind": "method", "line": 393, "name": "_generate_go", "signature": "def _generate_go(class_symbols, nodes, edges)"}, {"kind": "method", "line": 420, "name": "_generate_rust", "signature": "def _generate_rust(class_symbols, nodes, edges)"}, {"kind": "method", "line": 446, "name": "_generate_php", "signature": "def _generate_php(class_symbols, nodes, edges)"}, {"kind": "method", "line": 474, "name": "_generate_kotlin", "signature": "def _generate_kotlin(class_symbols, nodes, edges)"}, {"kind": "method", "line": 494, "name": "_generate_scala", "signature": "def _generate_scala(class_symbols, nodes, edges)"}, {"kind": "method", "line": 516, "name": "_generate_swift", "signature": "def _generate_swift(class_symbols, nodes, edges)"}, {"kind": "method", "line": 545, "name": "_generate_dart", "signature": "def _generate_dart(class_symbols, nodes, edges)"}, {"kind": "method", "line": 565, "name": "_generate_ruby", "signature": "def _generate_ruby(class_symbols, nodes, edges)"}, {"kind": "method", "line": 586, "name": "_safe_name", "signature": "def _safe_name(name)"}, {"kind": "method", "line": 590, "name": "_extract_params", "signature": "def _extract_params(signature)"}, {"kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 37, "name": "render_mermaid_class_diagram", "signature": "def render_mermaid_class_diagram(self, nodes, edges)"}, {"kind": "method", "line": 127, "name": "generate_code", "signature": "def generate_code(self, nodes, edges, target_language)"}, {"kind": "method", "line": 151, "name": "_sanitize_id", "signature": "def _sanitize_id(raw)"}, {"kind": "method", "line": 163, "name": "_find_node", "signature": "def _find_node(nodes, node_id)"}]}, {"id": "readmenator/_watcher.py", "kind": "module", "label": "_watcher.py", "language": "py", "sha256": "239589d6f7746a2a", "symbol_count": 5, "symbols": [{"doc": "Polling-based directory watcher for auto-rebuild on changes.\n\nComputes a combined hash of all tracked files (filenames + sizes)\nand triggers a callback when the hash changes. Uses polling to\navoid external dependencies like watchdog or inotify.", "kind": "class", "line": 21, "name": "DirectoryWatcher", "signature": "class DirectoryWatcher"}, {"doc": "Initialise the watcher for a project root.\n\nArgs:\n    root: Project directory to watch.\n    config: Application configuration.\n    callback: Function called when changes are detected.\n    interval_seconds: Polling interval in seconds.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, root, config, callback, interval_seconds)"}, {"doc": "Compute a quick hash of all tracked files in the project.\n\nUses file paths and sizes (not full content) for speed.\nReturns a hex digest that changes when files are added,\nremoved, or modified.", "kind": "method", "line": 51, "name": "_compute_snapshot", "signature": "def _compute_snapshot(self)"}, {"doc": "Start watching the directory (blocking).", "kind": "method", "line": 80, "name": "start", "signature": "def start(self)"}, {"doc": "Stop watching.", "kind": "method", "line": 97, "name": "stop", "signature": "def stop(self)"}]}, {"id": "readmenator/parsers/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "8291343d44d60a19", "symbol_count": 2, "symbols": [{"kind": "function", "line": 32, "name": "_init_parser_map", "signature": "def _init_parser_map()"}, {"doc": "Factory: return a parser instance for the given file extension.", "kind": "function", "line": 65, "name": "create_parser", "signature": "def create_parser(extension, filename, config)"}]}, {"id": "readmenator/parsers/_assembly.py", "kind": "module", "label": "_assembly.py", "language": "py", "sha256": "3c54c72d2e2c3497", "symbol_count": 2, "symbols": [{"doc": "Parser for assembly (.asm, .s, .S).\n\nExtracts labels at the start of a line (``label:``) as function\nsymbols. This is a best-effort heuristic; local labels and\ndirectives are not always distinguishable.", "kind": "class", "line": 9, "name": "AssemblyParser", "signature": "class AssemblyParser(LanguageParser)"}, {"kind": "method", "line": 17, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_base.py", "kind": "module", "label": "_base.py", "language": "py", "sha256": "edb00b6f40c180b1", "symbol_count": 6, "symbols": [{"doc": "Base class for all language-specific parsers.\n\nSubclasses must implement ``_extract_specifics`` to populate\n``self.symbols`` and ``self.imports``. Common utility methods\n``_extract_docstring`` and ``_extract_signature`` are provided\nfor reuse across all parsers.", "kind": "class", "line": 10, "name": "LanguageParser", "signature": "class LanguageParser"}, {"doc": "Initialise the parser with a file path and application config.\n\nArgs:\n    filename: Relative or absolute path of the source file.\n    config: Application-wide configuration settings.", "kind": "method", "line": 19, "name": "__init__", "signature": "def __init__(self, filename, config)"}, {"doc": "Parse *content* and populate symbol/import lists.\n\nSplits the source into lines, then delegates to the subclass-\nspecific ``_extract_specifics`` logic.", "kind": "method", "line": 34, "name": "parse", "signature": "def parse(self, content)"}, {"doc": "Subclass hook for language-specific symbol extraction.", "kind": "method", "line": 43, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}, {"doc": "Walk backwards from *line_num* to collect preceding comments/docstrings.\n\nSupports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``\ncomment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``\nfrom Config.", "kind": "method", "line": 47, "name": "_extract_docstring", "signature": "def _extract_docstring(self, line_num)"}, {"doc": "Extract a compact signature snippet starting at *match_start*.\n\nScans forward to the opening brace or a fallback length,\nthen truncates to 100 characters for display.", "kind": "method", "line": 89, "name": "_extract_signature", "signature": "def _extract_signature(self, content, match_start, pattern)"}]}, {"id": "readmenator/parsers/_c.py", "kind": "module", "label": "_c.py", "language": "py", "sha256": "c7df3a6543a025c6", "symbol_count": 2, "symbols": [{"doc": "Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).\n\nExtracts includes, structs, classes, functions, and preprocessor\nmacros using regex heuristics tuned to C-family syntax.", "kind": "class", "line": 9, "name": "CParser", "signature": "class CParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_csharp.py", "kind": "module", "label": "_csharp.py", "language": "py", "sha256": "cfaa6ea3cf4296c4", "symbol_count": 2, "symbols": [{"doc": "Parser for C# (.cs).\n\nExtracts ``using`` directives, class/struct/interface/record\ndeclarations, and methods with access modifiers.", "kind": "class", "line": 9, "name": "CSharpParser", "signature": "class CSharpParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_dart.py", "kind": "module", "label": "_dart.py", "language": "py", "sha256": "4b087dfaed083323", "symbol_count": 2, "symbols": [{"doc": "Parser for Dart (.dart).\n\nExtracts import statements, class declarations (with extends),\nand top-level or method function declarations by return type.", "kind": "class", "line": 9, "name": "DartParser", "signature": "class DartParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_elixir.py", "kind": "module", "label": "_elixir.py", "language": "py", "sha256": "645a1d929186f850", "symbol_count": 2, "symbols": [{"doc": "Parser for Elixir (.ex, .exs).\n\nExtracts ``import``/``alias``/``require``/``use`` directives,\nmodule definitions, and named function definitions.", "kind": "class", "line": 9, "name": "ElixirParser", "signature": "class ElixirParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_gdscript.py", "kind": "module", "label": "_gdscript.py", "language": "py", "sha256": "27a50d6bc58f772f", "symbol_count": 2, "symbols": [{"doc": "Parser for Godot GDScript (.gd).\n\nExtracts ``extends`` / ``class_name`` directives and ``func``\nmethod declarations.", "kind": "class", "line": 9, "name": "GDScriptParser", "signature": "class GDScriptParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_go.py", "kind": "module", "label": "_go.py", "language": "py", "sha256": "2e55e35316be76bb", "symbol_count": 2, "symbols": [{"doc": "Parser for Go (.go).\n\nExtracts import blocks or single import statements, exported\nfunctions (including methods), and type definitions (struct/interface).", "kind": "class", "line": 9, "name": "GoParser", "signature": "class GoParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_java.py", "kind": "module", "label": "_java.py", "language": "py", "sha256": "25826d29281fc7a4", "symbol_count": 2, "symbols": [{"doc": "Parser for Java (.java).\n\nExtracts import statements, class and interface declarations,\nand methods complete with access modifiers and type signatures.", "kind": "class", "line": 9, "name": "JavaParser", "signature": "class JavaParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_javascript.py", "kind": "module", "label": "_javascript.py", "language": "py", "sha256": "a024f05bb3db8318", "symbol_count": 2, "symbols": [{"doc": "Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).\n\nExtracts ES module imports, CommonJS ``require`` calls, function\ndeclarations, arrow-function variables, and class definitions\n(including inheritance).", "kind": "class", "line": 9, "name": "JavaScriptParser", "signature": "class JavaScriptParser(LanguageParser)"}, {"kind": "method", "line": 17, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_kotlin.py", "kind": "module", "label": "_kotlin.py", "language": "py", "sha256": "cd1af4e9d8c2f23b", "symbol_count": 2, "symbols": [{"doc": "Parser for Kotlin (.kt, .kts).\n\nExtracts ``import`` statements, class/object/interface/data class\ndeclarations, and function definitions.", "kind": "class", "line": 9, "name": "KotlinParser", "signature": "class KotlinParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_lua.py", "kind": "module", "label": "_lua.py", "language": "py", "sha256": "df4d62ca2b4b2387", "symbol_count": 2, "symbols": [{"doc": "Parser for Lua (.lua).\n\nExtracts ``require`` imports, function declarations (named and\ntable-based), and module returns.", "kind": "class", "line": 9, "name": "LuaParser", "signature": "class LuaParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_nim.py", "kind": "module", "label": "_nim.py", "language": "py", "sha256": "fde950f2aaa92bb2", "symbol_count": 2, "symbols": [{"doc": "Parser for Nim (.nim).\n\nExtracts ``import`` statements, ``proc`` / ``func`` / ``method``\ndeclarations, and ``type`` definitions.", "kind": "class", "line": 9, "name": "NimParser", "signature": "class NimParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_php.py", "kind": "module", "label": "_php.py", "language": "py", "sha256": "30f0aa4f3d9573a9", "symbol_count": 2, "symbols": [{"doc": "Parser for PHP (.php).\n\nExtracts ``use/require/include`` (including ``_once`` variants),\nfunction declarations, and class declarations.", "kind": "class", "line": 9, "name": "PHPParser", "signature": "class PHPParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_python.py", "kind": "module", "label": "_python.py", "language": "py", "sha256": "b7a85e67d2c72a37", "symbol_count": 2, "symbols": [{"doc": "Parser for Python (.py) using the native ``ast`` module.\n\nExtracts imports, functions (including async), and class\ndefinitions with docstrings via ``ast.get_docstring``.", "kind": "class", "line": 10, "name": "PythonParser", "signature": "class PythonParser(LanguageParser)"}, {"kind": "method", "line": 17, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_ruby.py", "kind": "module", "label": "_ruby.py", "language": "py", "sha256": "f471ea9104217c63", "symbol_count": 2, "symbols": [{"doc": "Parser for Ruby (.rb).\n\nExtracts ``require`` / ``require_relative`` imports, class and\nmodule definitions with inheritance, and method definitions.", "kind": "class", "line": 9, "name": "RubyParser", "signature": "class RubyParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_rust.py", "kind": "module", "label": "_rust.py", "language": "py", "sha256": "46f030f5e898dd81", "symbol_count": 2, "symbols": [{"doc": "Parser for Rust (.rs).\n\nExtracts ``use`` imports, public and private functions,\nstructs, traits, and enums.", "kind": "class", "line": 9, "name": "RustParser", "signature": "class RustParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_scala.py", "kind": "module", "label": "_scala.py", "language": "py", "sha256": "386522f137dcc74a", "symbol_count": 2, "symbols": [{"doc": "Parser for Scala (.scala).\n\nExtracts ``import`` statements, class/object/trait declarations,\nand method definitions.", "kind": "class", "line": 9, "name": "ScalaParser", "signature": "class ScalaParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_shell.py", "kind": "module", "label": "_shell.py", "language": "py", "sha256": "18e886e8af9eca07", "symbol_count": 2, "symbols": [{"doc": "Parser for shell scripts (.sh, .bash, .zsh).\n\nExtracts function declarations in both POSIX (``name() {``)\nand ``function`` keyword syntax.", "kind": "class", "line": 9, "name": "ShellParser", "signature": "class ShellParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator/parsers/_swift.py", "kind": "module", "label": "_swift.py", "language": "py", "sha256": "865dacef6bb447dc", "symbol_count": 2, "symbols": [{"doc": "Parser for Swift (.swift).\n\nExtracts ``import`` statements, class/struct/enum/protocol\ndeclarations with inheritance, and function definitions.", "kind": "class", "line": 9, "name": "SwiftParser", "signature": "class SwiftParser(LanguageParser)"}, {"kind": "method", "line": 16, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"id": "readmenator.py", "kind": "module", "label": "readmenator.py", "language": "py", "sha256": "beabccf3e6d231db", "symbol_count": 0, "symbols": []}, {"id": "readmenator_orchestrator.py", "kind": "module", "label": "readmenator_orchestrator.py", "language": "py", "sha256": "250362479291af30", "symbol_count": 34, "symbols": [{"kind": "class", "line": 21, "name": "Config", "signature": "class Config"}, {"kind": "method", "line": 43, "name": "_validate_repo_name", "signature": "def _validate_repo_name(name)"}, {"kind": "method", "line": 49, "name": "_validate_branch_name", "signature": "def _validate_branch_name(name)"}, {"kind": "method", "line": 55, "name": "_safe_env", "signature": "def _safe_env()"}, {"kind": "class", "line": 70, "name": "GitHubClient", "signature": "class GitHubClient"}, {"kind": "class", "line": 184, "name": "RepositoryProcessor", "signature": "class RepositoryProcessor"}, {"kind": "class", "line": 326, "name": "Orchestrator", "signature": "class Orchestrator"}, {"kind": "class", "line": 381, "name": "TestOrchestrator", "signature": "class TestOrchestrator(TestCase)"}, {"kind": "method", "line": 422, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 439, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 71, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 76, "name": "_resolve_user", "signature": "def _resolve_user(self)"}, {"kind": "method", "line": 97, "name": "_setup_git_auth", "signature": "def _setup_git_auth(self)"}, {"kind": "method", "line": 111, "name": "list_repos", "signature": "def list_repos(self)"}, {"kind": "method", "line": 123, "name": "close_existing_prs", "signature": "def close_existing_prs(self, repo)"}, {"kind": "method", "line": 151, "name": "delete_remote_branch", "signature": "def delete_remote_branch(self, repo)"}, {"kind": "method", "line": 163, "name": "create_pr", "signature": "def create_pr(self, repo, default_branch, timestamp)"}, {"kind": "method", "line": 185, "name": "__init__", "signature": "def __init__(self, config, github_client)"}, {"kind": "method", "line": 189, "name": "process", "signature": "def process(self, repo)"}, {"kind": "method", "line": 218, "name": "_get_default_branch", "signature": "def _get_default_branch(self, repo)"}, {"kind": "method", "line": 234, "name": "_clone_repository", "signature": "def _clone_repository(self, repo)"}, {"kind": "method", "line": 250, "name": "_run_readmenator", "signature": "def _run_readmenator(self, repo_dir)"}, {"kind": "method", "line": 271, "name": "_copy_to_docs_dir", "signature": "def _copy_to_docs_dir(repo_dir, generated_file)"}, {"kind": "method", "line": 277, "name": "_commit_and_push", "signature": "def _commit_and_push(self, repo_dir, repo)"}, {"kind": "method", "line": 321, "name": "_cleanup_temp_dir", "signature": "def _cleanup_temp_dir(temp_dir)"}, {"kind": "method", "line": 327, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 332, "name": "run", "signature": "def run(self, dry_run, only_repo)"}, {"kind": "method", "line": 382, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 386, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 389, "name": "test_config_immutability", "signature": "def test_config_immutability(self)"}, {"kind": "method", "line": 393, "name": "test_config_defaults", "signature": "def test_config_defaults(self)"}, {"kind": "method", "line": 399, "name": "test_skip_repos_logic", "signature": "def test_skip_repos_logic(self)"}, {"kind": "method", "line": 403, "name": "test_repo_name_validation", "signature": "def test_repo_name_validation(self)"}, {"kind": "method", "line": 413, "name": "test_branch_name_validation", "signature": "def test_branch_name_validation(self)"}]}, {"id": "tests/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "f813c53b4d1cc74f", "symbol_count": 0, "symbols": []}, {"id": "tests/test_analyzer.py", "kind": "module", "label": "test_analyzer.py", "language": "py", "sha256": "0f8e3409a64ff96e", "symbol_count": 12, "symbols": [{"doc": "Contract: GraphAnalyzer provides graph intelligence.", "kind": "class", "line": 16, "name": "TestGraphAnalyzerContract", "signature": "class TestGraphAnalyzerContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 26, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt, rel)"}, {"kind": "method", "line": 29, "name": "test_analyze_empty_graph_returns_empty_result", "signature": "def test_analyze_empty_graph_returns_empty_result(self)"}, {"kind": "method", "line": 34, "name": "test_analyze_detects_communities_for_connected_graph", "signature": "def test_analyze_detects_communities_for_connected_graph(self)"}, {"kind": "method", "line": 48, "name": "test_analyze_computes_god_nodes", "signature": "def test_analyze_computes_god_nodes(self)"}, {"kind": "method", "line": 64, "name": "test_analyze_finds_surprising_connections", "signature": "def test_analyze_finds_surprising_connections(self)"}, {"kind": "method", "line": 81, "name": "test_analyze_generates_questions", "signature": "def test_analyze_generates_questions(self)"}, {"kind": "method", "line": 92, "name": "test_community_cohesion_is_between_zero_and_one", "signature": "def test_community_cohesion_is_between_zero_and_one(self)"}, {"kind": "method", "line": 107, "name": "test_isolated_nodes_do_not_form_communities", "signature": "def test_isolated_nodes_do_not_form_communities(self)"}, {"kind": "method", "line": 116, "name": "test_analyze_with_resolved_edges_counts_them", "signature": "def test_analyze_with_resolved_edges_counts_them(self)"}]}, {"id": "tests/test_cache.py", "kind": "module", "label": "test_cache.py", "language": "py", "sha256": "122bbfc37460eb38", "symbol_count": 22, "symbols": [{"doc": "Contract: FileCache provides SHA256-based incremental scan support.", "kind": "class", "line": 18, "name": "TestFileCacheContract", "signature": "class TestFileCacheContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 26, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 30, "name": "_write", "signature": "def _write(self, rel_path, content)"}, {"kind": "method", "line": 36, "name": "test_compute_hash_returns_hex_string", "signature": "def test_compute_hash_returns_hex_string(self)"}, {"kind": "method", "line": 42, "name": "test_different_content_produces_different_hash", "signature": "def test_different_content_produces_different_hash(self)"}, {"kind": "method", "line": 49, "name": "test_same_content_produces_same_hash", "signature": "def test_same_content_produces_same_hash(self)"}, {"kind": "method", "line": 56, "name": "test_load_returns_empty_dict_when_no_cache", "signature": "def test_load_returns_empty_dict_when_no_cache(self)"}, {"kind": "method", "line": 60, "name": "test_save_and_load_roundtrip", "signature": "def test_save_and_load_roundtrip(self)"}, {"kind": "method", "line": 66, "name": "test_find_changed_detects_new_files", "signature": "def test_find_changed_detects_new_files(self)"}, {"kind": "method", "line": 71, "name": "test_find_changed_detects_modified_files", "signature": "def test_find_changed_detects_modified_files(self)"}, {"kind": "method", "line": 78, "name": "test_find_changed_skips_unchanged_files", "signature": "def test_find_changed_skips_unchanged_files(self)"}, {"kind": "method", "line": 85, "name": "test_prune_deleted_removes_ghost_entries", "signature": "def test_prune_deleted_removes_ghost_entries(self)"}, {"kind": "method", "line": 92, "name": "test_compute_hashes_batch", "signature": "def test_compute_hashes_batch(self)"}, {"kind": "method", "line": 100, "name": "test_nonexistent_file_returns_empty_hash", "signature": "def test_nonexistent_file_returns_empty_hash(self)"}, {"kind": "method", "line": 109, "name": "test_save_and_load_analysis_roundtrip", "signature": "def test_save_and_load_analysis_roundtrip(self)"}, {"kind": "method", "line": 116, "name": "test_load_missing_analysis_key_returns_none", "signature": "def test_load_missing_analysis_key_returns_none(self)"}, {"kind": "method", "line": 120, "name": "test_clear_analysis_specific_key", "signature": "def test_clear_analysis_specific_key(self)"}, {"kind": "method", "line": 127, "name": "test_clear_analysis_all_keys", "signature": "def test_clear_analysis_all_keys(self)"}, {"kind": "method", "line": 134, "name": "test_has_changed_since_last_analysis_returns_true_on_first_run", "signature": "def test_has_changed_since_last_analysis_returns_true_on_first_run(self)"}, {"kind": "method", "line": 139, "name": "test_has_changed_since_last_analysis_returns_false_when_no_changes", "signature": "def test_has_changed_since_last_analysis_returns_false_when_no_changes(self)"}, {"kind": "method", "line": 147, "name": "test_has_changed_since_last_analysis_returns_true_when_file_changed", "signature": "def test_has_changed_since_last_analysis_returns_true_when_file_changed(self)"}]}, {"id": "tests/test_config.py", "kind": "module", "label": "test_config.py", "language": "py", "sha256": "0123e0442447e271", "symbol_count": 6, "symbols": [{"kind": "class", "line": 7, "name": "TestConfigContract", "signature": "class TestConfigContract(TestCase)"}, {"kind": "method", "line": 8, "name": "test_config_is_immutable", "signature": "def test_config_is_immutable(self)"}, {"kind": "method", "line": 13, "name": "test_config_defaults_are_sane", "signature": "def test_config_defaults_are_sane(self)"}, {"kind": "method", "line": 24, "name": "test_ignore_dirs_are_comprehensive", "signature": "def test_ignore_dirs_are_comprehensive(self)"}, {"kind": "method", "line": 30, "name": "test_plural_map_covers_all_symbol_types", "signature": "def test_plural_map_covers_all_symbol_types(self)"}, {"kind": "method", "line": 41, "name": "test_supported_extensions_no_duplicates", "signature": "def test_supported_extensions_no_duplicates(self)"}]}, {"id": "tests/test_cpg.py", "kind": "module", "label": "test_cpg.py", "language": "py", "sha256": "f71374c5b5964fc8", "symbol_count": 11, "symbols": [{"doc": "Contract: CodePropertyGraph generates valid JSON-LD CPG output.", "kind": "class", "line": 11, "name": "TestCodePropertyGraphContract", "signature": "class TestCodePropertyGraphContract(TestCase)"}, {"kind": "method", "line": 14, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 18, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 21, "name": "_make_sym", "signature": "def _make_sym(self, name, kind, line)"}, {"kind": "method", "line": 24, "name": "test_generate_returns_valid_json", "signature": "def test_generate_returns_valid_json(self)"}, {"kind": "method", "line": 33, "name": "test_generate_includes_node_data", "signature": "def test_generate_includes_node_data(self)"}, {"kind": "method", "line": 49, "name": "test_generate_includes_edges", "signature": "def test_generate_includes_edges(self)"}, {"kind": "method", "line": 61, "name": "test_generate_includes_metadata", "signature": "def test_generate_includes_metadata(self)"}, {"kind": "method", "line": 71, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 89, "name": "test_sha256_hash_included", "signature": "def test_sha256_hash_included(self)"}, {"kind": "method", "line": 96, "name": "test_empty_graph_returns_valid_json", "signature": "def test_empty_graph_returns_valid_json(self)"}]}, {"id": "tests/test_cursorrules.py", "kind": "module", "label": "test_cursorrules.py", "language": "py", "sha256": "cc1c4a1ca3487d28", "symbol_count": 12, "symbols": [{"doc": "Contract: CursorRulesGenerator produces deterministic rulesets.", "kind": "class", "line": 18, "name": "TestCursorRulesGeneratorContract", "signature": "class TestCursorRulesGeneratorContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 25, "name": "test_generate_returns_string", "signature": "def test_generate_returns_string(self)"}, {"kind": "method", "line": 29, "name": "test_generate_contains_header", "signature": "def test_generate_contains_header(self)"}, {"kind": "method", "line": 33, "name": "test_generate_contains_base_rules", "signature": "def test_generate_contains_base_rules(self)"}, {"kind": "method", "line": 38, "name": "test_generate_includes_layer_constraints", "signature": "def test_generate_includes_layer_constraints(self)"}, {"kind": "method", "line": 49, "name": "test_generate_includes_god_nodes", "signature": "def test_generate_includes_god_nodes(self)"}, {"kind": "method", "line": 62, "name": "test_generate_includes_communities", "signature": "def test_generate_includes_communities(self)"}, {"kind": "method", "line": 82, "name": "test_generate_includes_violations", "signature": "def test_generate_includes_violations(self)"}, {"kind": "method", "line": 95, "name": "test_generate_limits_violations_to_ten", "signature": "def test_generate_limits_violations_to_ten(self)"}, {"kind": "method", "line": 103, "name": "test_generate_writes_file_when_project_root", "signature": "def test_generate_writes_file_when_project_root(self)"}, {"kind": "method", "line": 111, "name": "test_generate_idempotent", "signature": "def test_generate_idempotent(self)"}]}, {"id": "tests/test_dead_code.py", "kind": "module", "label": "test_dead_code.py", "language": "py", "sha256": "4878048842697a87", "symbol_count": 15, "symbols": [{"doc": "Contract: DeadCodeStripper identifies orphaned symbols.", "kind": "class", "line": 16, "name": "TestDeadCodeStripperContract", "signature": "class TestDeadCodeStripperContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_symbol", "signature": "def _make_symbol(self, name, kind)"}, {"kind": "method", "line": 26, "name": "_make_node", "signature": "def _make_node(self, nid, symbols)"}, {"kind": "method", "line": 35, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt)"}, {"kind": "method", "line": 38, "name": "test_identify_empty_graph_returns_empty", "signature": "def test_identify_empty_graph_returns_empty(self)"}, {"kind": "method", "line": 42, "name": "test_identify_finds_dead_symbol", "signature": "def test_identify_finds_dead_symbol(self)"}, {"kind": "method", "line": 53, "name": "test_identify_excludes_entry_points", "signature": "def test_identify_excludes_entry_points(self)"}, {"kind": "method", "line": 61, "name": "test_identify_excludes_app_entry_point", "signature": "def test_identify_excludes_app_entry_point(self)"}, {"kind": "method", "line": 69, "name": "test_identify_excludes_init_entry_point", "signature": "def test_identify_excludes_init_entry_point(self)"}, {"kind": "method", "line": 77, "name": "test_identify_recommends_review_for_classes", "signature": "def test_identify_recommends_review_for_classes(self)"}, {"kind": "method", "line": 85, "name": "test_identify_recommends_trash_for_functions", "signature": "def test_identify_recommends_trash_for_functions(self)"}, {"kind": "method", "line": 93, "name": "test_identify_recommends_trash_for_variables", "signature": "def test_identify_recommends_trash_for_variables(self)"}, {"kind": "method", "line": 101, "name": "test_all_symbols_imported_returns_empty", "signature": "def test_all_symbols_imported_returns_empty(self)"}, {"kind": "method", "line": 113, "name": "test_reports_sorted_by_file_path", "signature": "def test_reports_sorted_by_file_path(self)"}]}, {"id": "tests/test_documentation.py", "kind": "module", "label": "test_documentation.py", "language": "py", "sha256": "11ed437912c144e4", "symbol_count": 29, "symbols": [{"kind": "class", "line": 17, "name": "TestDocumentationGeneratorContract", "signature": "class TestDocumentationGeneratorContract(TestCase)"}, {"kind": "method", "line": 18, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 22, "name": "test_contains_header", "signature": "def test_contains_header(self)"}, {"kind": "method", "line": 26, "name": "test_contains_metadata_line", "signature": "def test_contains_metadata_line(self)"}, {"kind": "method", "line": 32, "name": "test_contains_mermaid_block", "signature": "def test_contains_mermaid_block(self)"}, {"kind": "method", "line": 37, "name": "test_contains_architecture_reference", "signature": "def test_contains_architecture_reference(self)"}, {"kind": "method", "line": 41, "name": "test_contains_cpg_block", "signature": "def test_contains_cpg_block(self)"}, {"kind": "method", "line": 46, "name": "test_contains_statistics_dashboard", "signature": "def test_contains_statistics_dashboard(self)"}, {"kind": "method", "line": 51, "name": "test_groups_files_by_language", "signature": "def test_groups_files_by_language(self)"}, {"kind": "method", "line": 70, "name": "test_lists_symbols_under_file", "signature": "def test_lists_symbols_under_file(self)"}, {"kind": "method", "line": 83, "name": "test_class_symbol_is_pluralized_correctly", "signature": "def test_class_symbol_is_pluralized_correctly(self)"}, {"kind": "method", "line": 97, "name": "test_function_pluralization", "signature": "def test_function_pluralization(self)"}, {"kind": "method", "line": 109, "name": "test_method_pluralization", "signature": "def test_method_pluralization(self)"}, {"kind": "method", "line": 121, "name": "test_shows_no_symbols_for_empty_files", "signature": "def test_shows_no_symbols_for_empty_files(self)"}, {"kind": "method", "line": 132, "name": "test_includes_file_path", "signature": "def test_includes_file_path(self)"}, {"kind": "method", "line": 143, "name": "test_docstring_in_output", "signature": "def test_docstring_in_output(self)"}, {"kind": "method", "line": 155, "name": "test_truncation_note_when_limited", "signature": "def test_truncation_note_when_limited(self)"}, {"kind": "method", "line": 165, "name": "test_taint_propagation_section_present", "signature": "def test_taint_propagation_section_present(self)"}, {"kind": "method", "line": 185, "name": "test_hotspot_section_present", "signature": "def test_hotspot_section_present(self)"}, {"kind": "method", "line": 203, "name": "test_no_taint_section_when_empty", "signature": "def test_no_taint_section_when_empty(self)"}, {"kind": "method", "line": 207, "name": "test_no_hotspot_section_when_empty", "signature": "def test_no_hotspot_section_when_empty(self)"}, {"kind": "method", "line": 211, "name": "test_cpg_block_disabled_via_config", "signature": "def test_cpg_block_disabled_via_config(self)"}, {"kind": "method", "line": 217, "name": "test_architectural_layers_section", "signature": "def test_architectural_layers_section(self)"}, {"kind": "method", "line": 229, "name": "test_security_findings_section", "signature": "def test_security_findings_section(self)"}, {"kind": "method", "line": 252, "name": "test_context_budget_zero_returns_full_content", "signature": "def test_context_budget_zero_returns_full_content(self)"}, {"kind": "method", "line": 260, "name": "test_context_budget_returns_compact_summary", "signature": "def test_context_budget_returns_compact_summary(self)"}, {"kind": "method", "line": 268, "name": "test_context_budget_prioritizes_god_nodes", "signature": "def test_context_budget_prioritizes_god_nodes(self)"}, {"kind": "method", "line": 285, "name": "test_context_budget_truncates_at_limit", "signature": "def test_context_budget_truncates_at_limit(self)"}, {"kind": "method", "line": 293, "name": "test_context_budget_includes_security_findings", "signature": "def test_context_budget_includes_security_findings(self)"}]}, {"id": "tests/test_exporter.py", "kind": "module", "label": "test_exporter.py", "language": "py", "sha256": "b70cde45a0105c5f", "symbol_count": 15, "symbols": [{"doc": "Contract: GraphExporter produces valid JSON, HTML, and SVG outputs.", "kind": "class", "line": 23, "name": "TestGraphExporterContract", "signature": "class TestGraphExporterContract(TestCase)"}, {"kind": "method", "line": 26, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 30, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang, symbols)"}, {"kind": "method", "line": 42, "name": "_make_sym", "signature": "def _make_sym(self, name, kind, line)"}, {"kind": "method", "line": 47, "name": "test_to_json_produces_valid_json", "signature": "def test_to_json_produces_valid_json(self)"}, {"kind": "method", "line": 56, "name": "test_to_json_includes_symbol_data", "signature": "def test_to_json_includes_symbol_data(self)"}, {"kind": "method", "line": 65, "name": "test_to_json_includes_metadata", "signature": "def test_to_json_includes_metadata(self)"}, {"kind": "method", "line": 76, "name": "test_to_json_includes_analysis_metadata", "signature": "def test_to_json_includes_analysis_metadata(self)"}, {"kind": "method", "line": 101, "name": "test_to_html_produces_standalone_page", "signature": "def test_to_html_produces_standalone_page(self)"}, {"kind": "method", "line": 109, "name": "test_to_html_includes_node_data", "signature": "def test_to_html_includes_node_data(self)"}, {"kind": "method", "line": 116, "name": "test_to_html_includes_community_legend_when_analysis", "signature": "def test_to_html_includes_community_legend_when_analysis(self)"}, {"kind": "method", "line": 138, "name": "test_to_svg_produces_svg_string", "signature": "def test_to_svg_produces_svg_string(self)"}, {"kind": "method", "line": 145, "name": "test_to_svg_render_truncation_for_large_graph", "signature": "def test_to_svg_render_truncation_for_large_graph(self)"}, {"kind": "method", "line": 154, "name": "test_to_svg_includes_readmenator_title", "signature": "def test_to_svg_includes_readmenator_title(self)"}, {"kind": "method", "line": 160, "name": "test_to_json_handles_resolved_edges", "signature": "def test_to_json_handles_resolved_edges(self)"}]}, {"id": "tests/test_hotspots.py", "kind": "module", "label": "test_hotspots.py", "language": "py", "sha256": "2f31e5fb128e17d4", "symbol_count": 11, "symbols": [{"doc": "Contract: HotspotAnalyzer detects hotspots, cycles, and change impact.", "kind": "class", "line": 10, "name": "TestHotspotAnalyzerContract", "signature": "class TestHotspotAnalyzerContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label, sym_count)"}, {"kind": "method", "line": 29, "name": "test_empty_graph_returns_empty_hotspots", "signature": "def test_empty_graph_returns_empty_hotspots(self)"}, {"kind": "method", "line": 33, "name": "test_hotspots_rank_by_combined_score", "signature": "def test_hotspots_rank_by_combined_score(self)"}, {"kind": "method", "line": 43, "name": "test_hotspot_includes_scores", "signature": "def test_hotspot_includes_scores(self)"}, {"kind": "method", "line": 53, "name": "test_no_cycles_in_acyclic_graph", "signature": "def test_no_cycles_in_acyclic_graph(self)"}, {"kind": "method", "line": 66, "name": "test_detects_simple_cycle", "signature": "def test_detects_simple_cycle(self)"}, {"kind": "method", "line": 79, "name": "test_change_impact_ranks_by_total_impact", "signature": "def test_change_impact_ranks_by_total_impact(self)"}, {"kind": "method", "line": 94, "name": "test_change_impact_no_edges", "signature": "def test_change_impact_no_edges(self)"}, {"kind": "method", "line": 100, "name": "test_hotspot_weights_from_config", "signature": "def test_hotspot_weights_from_config(self)"}]}, {"id": "tests/test_integration.py", "kind": "module", "label": "test_integration.py", "language": "py", "sha256": "fa1c42eb78225f90", "symbol_count": 16, "symbols": [{"kind": "class", "line": 9, "name": "TestEndToEndContract", "signature": "class TestEndToEndContract(TestCase)"}, {"kind": "method", "line": 10, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 15, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 19, "name": "_write", "signature": "def _write(self, path, content)"}, {"kind": "method", "line": 24, "name": "test_full_pipeline_generates_knowledge_base", "signature": "def test_full_pipeline_generates_knowledge_base(self)"}, {"kind": "method", "line": 40, "name": "test_knowledge_base_contains_mermaid", "signature": "def test_knowledge_base_contains_mermaid(self)"}, {"kind": "method", "line": 48, "name": "test_query_subcommand_works", "signature": "def test_query_subcommand_works(self)"}, {"kind": "method", "line": 53, "name": "test_explain_subcommand_works", "signature": "def test_explain_subcommand_works(self)"}, {"kind": "method", "line": 59, "name": "test_path_subcommand_works", "signature": "def test_path_subcommand_works(self)"}, {"kind": "method", "line": 65, "name": "test_summary_works", "signature": "def test_summary_works(self)"}, {"kind": "method", "line": 71, "name": "test_rebuild", "signature": "def test_rebuild(self)"}, {"kind": "method", "line": 81, "name": "test_knowledge_base_contains_cpg", "signature": "def test_knowledge_base_contains_cpg(self)"}, {"kind": "method", "line": 89, "name": "test_knowledge_base_contains_statistics_dashboard", "signature": "def test_knowledge_base_contains_statistics_dashboard(self)"}, {"kind": "method", "line": 98, "name": "test_audit_deep_returns_analysis", "signature": "def test_audit_deep_returns_analysis(self)"}, {"kind": "method", "line": 105, "name": "test_privacy_mode_works", "signature": "def test_privacy_mode_works(self)"}, {"kind": "method", "line": 114, "name": "test_export_sarif_produces_file", "signature": "def test_export_sarif_produces_file(self)"}]}, {"id": "tests/test_layer_rules.py", "kind": "module", "label": "test_layer_rules.py", "language": "py", "sha256": "d530692da5fb3cd6", "symbol_count": 13, "symbols": [{"doc": "Contract: LayerRuleEngine detects architectural layer violations.", "kind": "class", "line": 10, "name": "TestLayerRuleEngineContract", "signature": "class TestLayerRuleEngineContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label)"}, {"kind": "method", "line": 20, "name": "test_empty_graph_returns_empty_violations", "signature": "def test_empty_graph_returns_empty_violations(self)"}, {"kind": "method", "line": 24, "name": "test_no_layers_returns_empty_violations", "signature": "def test_no_layers_returns_empty_violations(self)"}, {"kind": "method", "line": 29, "name": "test_same_layer_no_violation", "signature": "def test_same_layer_no_violation(self)"}, {"kind": "method", "line": 36, "name": "test_forbidden_edge_detected", "signature": "def test_forbidden_edge_detected(self)"}, {"kind": "method", "line": 46, "name": "test_allowed_testing_edges_no_violation", "signature": "def test_allowed_testing_edges_no_violation(self)"}, {"kind": "method", "line": 57, "name": "test_multiple_violations", "signature": "def test_multiple_violations(self)"}, {"kind": "method", "line": 75, "name": "test_utility_layer_ignored", "signature": "def test_utility_layer_ignored(self)"}, {"kind": "method", "line": 82, "name": "test_violation_summary", "signature": "def test_violation_summary(self)"}, {"kind": "method", "line": 104, "name": "test_resolved_edges_also_checked", "signature": "def test_resolved_edges_also_checked(self)"}, {"kind": "method", "line": 115, "name": "test_presentation_to_data_access_forbidden", "signature": "def test_presentation_to_data_access_forbidden(self)"}]}, {"id": "tests/test_linter.py", "kind": "module", "label": "test_linter.py", "language": "py", "sha256": "f65b401457b24d7c", "symbol_count": 14, "symbols": [{"doc": "Contract: ArchitectureLinter enforces architectural rules.", "kind": "class", "line": 16, "name": "TestArchitectureLinterContract", "signature": "class TestArchitectureLinterContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 26, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt, rel)"}, {"kind": "method", "line": 29, "name": "test_lint_empty_graph_returns_no_violations", "signature": "def test_lint_empty_graph_returns_no_violations(self)"}, {"kind": "method", "line": 33, "name": "test_lint_returns_empty_for_files_under_threshold", "signature": "def test_lint_returns_empty_for_files_under_threshold(self)"}, {"kind": "method", "line": 40, "name": "test_lint_detects_file_exceeding_max_lines", "signature": "def test_lint_detects_file_exceeding_max_lines(self)"}, {"kind": "method", "line": 49, "name": "test_lint_detects_cross_layer_violation", "signature": "def test_lint_detects_cross_layer_violation(self)"}, {"kind": "method", "line": 61, "name": "test_lint_allows_same_layer_imports", "signature": "def test_lint_allows_same_layer_imports(self)"}, {"kind": "method", "line": 72, "name": "test_lint_allows_testing_to_business_logic", "signature": "def test_lint_allows_testing_to_business_logic(self)"}, {"kind": "method", "line": 83, "name": "test_lint_ignores_utility_layer", "signature": "def test_lint_ignores_utility_layer(self)"}, {"kind": "method", "line": 94, "name": "test_lint_detects_circular_dependencies", "signature": "def test_lint_detects_circular_dependencies(self)"}, {"kind": "method", "line": 108, "name": "test_violations_sorted_by_severity", "signature": "def test_violations_sorted_by_severity(self)"}, {"kind": "method", "line": 121, "name": "test_lint_returns_empty_when_disabled", "signature": "def test_lint_returns_empty_when_disabled(self)"}]}, {"id": "tests/test_mcp_server.py", "kind": "module", "label": "test_mcp_server.py", "language": "py", "sha256": "b5ae9c9e9ce2e49f", "symbol_count": 25, "symbols": [{"doc": "Contract: MCP server implements JSON-RPC 2.0 over stdio.", "kind": "class", "line": 21, "name": "TestMCPProtocol", "signature": "class TestMCPProtocol(TestCase)"}, {"kind": "method", "line": 24, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 33, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 36, "name": "_make_request", "signature": "def _make_request(self, method, params, msg_id)"}, {"kind": "method", "line": 42, "name": "_call", "signature": "def _call(self, req)"}, {"kind": "method", "line": 49, "name": "test_initialize_exchanges_protocol_version", "signature": "def test_initialize_exchanges_protocol_version(self)"}, {"kind": "method", "line": 62, "name": "test_notifications_initialized_returns_no_response", "signature": "def test_notifications_initialized_returns_no_response(self)"}, {"kind": "method", "line": 67, "name": "test_unknown_method_returns_error", "signature": "def test_unknown_method_returns_error(self)"}, {"kind": "method", "line": 75, "name": "test_uninitialized_request_returns_error", "signature": "def test_uninitialized_request_returns_error(self)"}, {"kind": "method", "line": 85, "name": "test_list_tools_returns_all_tool_definitions", "signature": "def test_list_tools_returns_all_tool_definitions(self)"}, {"kind": "method", "line": 115, "name": "test_call_tool_without_initialize_returns_error", "signature": "def test_call_tool_without_initialize_returns_error(self)"}, {"kind": "method", "line": 123, "name": "test_call_tool_unknown_tool_returns_method_not_found", "signature": "def test_call_tool_unknown_tool_returns_method_not_found(self)"}, {"kind": "method", "line": 132, "name": "test_call_summary_tool_returns_content", "signature": "def test_call_summary_tool_returns_content(self)"}, {"kind": "method", "line": 145, "name": "test_call_query_tool_with_text_returns_results", "signature": "def test_call_query_tool_with_text_returns_results(self)"}, {"kind": "method", "line": 154, "name": "test_call_query_tool_missing_required_param_raises", "signature": "def test_call_query_tool_missing_required_param_raises(self)"}, {"kind": "method", "line": 168, "name": "test_list_resources_returns_resource_definitions", "signature": "def test_list_resources_returns_resource_definitions(self)"}, {"kind": "method", "line": 186, "name": "test_read_resource_summary_returns_json", "signature": "def test_read_resource_summary_returns_json(self)"}, {"kind": "method", "line": 197, "name": "test_read_resource_unknown_uri_returns_error", "signature": "def test_read_resource_unknown_uri_returns_error(self)"}, {"kind": "method", "line": 205, "name": "test_read_resource_kb_returns_markdown", "signature": "def test_read_resource_kb_returns_markdown(self)"}, {"kind": "method", "line": 219, "name": "_get_tool_def", "signature": "def _get_tool_def(self, name)"}, {"kind": "method", "line": 226, "name": "test_query_tool_requires_text_param", "signature": "def test_query_tool_requires_text_param(self)"}, {"kind": "method", "line": 230, "name": "test_explain_tool_requires_name_param", "signature": "def test_explain_tool_requires_name_param(self)"}, {"kind": "method", "line": 234, "name": "test_path_tool_requires_two_params", "signature": "def test_path_tool_requires_two_params(self)"}, {"kind": "method", "line": 243, "name": "test_parse_error_for_invalid_json", "signature": "def test_parse_error_for_invalid_json(self)"}, {"kind": "method", "line": 251, "name": "test_call_tool_returns_text_content_list", "signature": "def test_call_tool_returns_text_content_list(self)"}]}, {"id": "tests/test_mermaid.py", "kind": "module", "label": "test_mermaid.py", "language": "py", "sha256": "447a55c490312fe7", "symbol_count": 11, "symbols": [{"kind": "class", "line": 7, "name": "TestMermaidRendererContract", "signature": "class TestMermaidRendererContract(TestCase)"}, {"kind": "method", "line": 8, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 11, "name": "test_renders_graph_header", "signature": "def test_renders_graph_header(self)"}, {"kind": "method", "line": 19, "name": "test_renders_module_node", "signature": "def test_renders_module_node(self)"}, {"kind": "method", "line": 27, "name": "test_renders_symbol_subnodes", "signature": "def test_renders_symbol_subnodes(self)"}, {"kind": "method", "line": 36, "name": "test_class_symbol_gets_cls_style", "signature": "def test_class_symbol_gets_cls_style(self)"}, {"kind": "method", "line": 45, "name": "test_function_symbol_gets_fn_style", "signature": "def test_function_symbol_gets_fn_style(self)"}, {"kind": "method", "line": 54, "name": "test_external_import_edge_is_dashed", "signature": "def test_external_import_edge_is_dashed(self)"}, {"kind": "method", "line": 62, "name": "test_truncation_when_over_limit", "signature": "def test_truncation_when_over_limit(self)"}, {"kind": "method", "line": 72, "name": "test_limits_symbols_to_five_per_node", "signature": "def test_limits_symbols_to_five_per_node(self)"}, {"kind": "method", "line": 82, "name": "test_handles_special_characters_in_ids", "signature": "def test_handles_special_characters_in_ids(self)"}]}, {"id": "tests/test_models.py", "kind": "module", "label": "test_models.py", "language": "py", "sha256": "af0df48f490c3633", "symbol_count": 11, "symbols": [{"kind": "class", "line": 6, "name": "TestSymbolContract", "signature": "class TestSymbolContract(TestCase)"}, {"kind": "class", "line": 20, "name": "TestNodeContract", "signature": "class TestNodeContract(TestCase)"}, {"kind": "class", "line": 48, "name": "TestEdgeContract", "signature": "class TestEdgeContract(TestCase)"}, {"kind": "class", "line": 56, "name": "TestPluralizeContract", "signature": "class TestPluralizeContract(TestCase)"}, {"kind": "method", "line": 7, "name": "test_symbol_creation", "signature": "def test_symbol_creation(self)"}, {"kind": "method", "line": 15, "name": "test_symbol_with_signature", "signature": "def test_symbol_with_signature(self)"}, {"kind": "method", "line": 21, "name": "test_node_creation", "signature": "def test_node_creation(self)"}, {"kind": "method", "line": 35, "name": "test_node_with_symbols", "signature": "def test_node_with_symbols(self)"}, {"kind": "method", "line": 49, "name": "test_edge_creation", "signature": "def test_edge_creation(self)"}, {"kind": "method", "line": 57, "name": "test_pluralize_class", "signature": "def test_pluralize_class(self)"}, {"kind": "method", "line": 62, "name": "test_pluralize_unknown_appends_s", "signature": "def test_pluralize_unknown_appends_s(self)"}]}, {"id": "tests/test_parsers.py", "kind": "module", "label": "test_parsers.py", "language": "py", "sha256": "22219731d5514573", "symbol_count": 84, "symbols": [{"kind": "class", "line": 22, "name": "TestCParserContract", "signature": "class TestCParserContract(TestCase)"}, {"kind": "class", "line": 72, "name": "TestPythonParserContract", "signature": "class TestPythonParserContract(TestCase)"}, {"kind": "class", "line": 141, "name": "TestGoParserContract", "signature": "class TestGoParserContract(TestCase)"}, {"kind": "class", "line": 184, "name": "TestRustParserContract", "signature": "class TestRustParserContract(TestCase)"}, {"kind": "class", "line": 222, "name": "TestJavaScriptParserContract", "signature": "class TestJavaScriptParserContract(TestCase)"}, {"kind": "class", "line": 261, "name": "TestJavaParserContract", "signature": "class TestJavaParserContract(TestCase)"}, {"kind": "class", "line": 293, "name": "TestCSharpParserContract", "signature": "class TestCSharpParserContract(TestCase)"}, {"kind": "class", "line": 326, "name": "TestShellParserContract", "signature": "class TestShellParserContract(TestCase)"}, {"kind": "class", "line": 345, "name": "TestPHPParserContract", "signature": "class TestPHPParserContract(TestCase)"}, {"kind": "class", "line": 371, "name": "TestDartParserContract", "signature": "class TestDartParserContract(TestCase)"}, {"kind": "class", "line": 396, "name": "TestGDScriptParserContract", "signature": "class TestGDScriptParserContract(TestCase)"}, {"kind": "class", "line": 414, "name": "TestNimParserContract", "signature": "class TestNimParserContract(TestCase)"}, {"kind": "class", "line": 440, "name": "TestAssemblyParserContract", "signature": "class TestAssemblyParserContract(TestCase)"}, {"kind": "class", "line": 460, "name": "TestParserFactoryContract", "signature": "class TestParserFactoryContract(TestCase)"}, {"kind": "method", "line": 23, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 26, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 33, "name": "test_extracts_struct", "signature": "def test_extracts_struct(self)"}, {"kind": "method", "line": 40, "name": "test_extracts_include", "signature": "def test_extracts_include(self)"}, {"kind": "method", "line": 47, "name": "test_extracts_define", "signature": "def test_extracts_define(self)"}, {"kind": "method", "line": 54, "name": "test_skips_reserved_words", "signature": "def test_skips_reserved_words(self)"}, {"kind": "method", "line": 64, "name": "test_class_with_inheritance", "signature": "def test_class_with_inheritance(self)"}, {"kind": "method", "line": 73, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 76, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 83, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 90, "name": "test_extracts_imports", "signature": "def test_extracts_imports(self)"}, {"kind": "method", "line": 98, "name": "test_extracts_async_function", "signature": "def test_extracts_async_function(self)"}, {"kind": "method", "line": 105, "name": "test_handles_syntax_error_gracefully", "signature": "def test_handles_syntax_error_gracefully(self)"}, {"kind": "method", "line": 111, "name": "test_suppresses_syntax_warnings", "signature": "def test_suppresses_syntax_warnings(self)"}, {"kind": "method", "line": 123, "name": "test_extracts_signature_with_params", "signature": "def test_extracts_signature_with_params(self)"}, {"kind": "method", "line": 131, "name": "test_extracts_class_with_bases", "signature": "def test_extracts_class_with_bases(self)"}, {"kind": "method", "line": 142, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 145, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 152, "name": "test_extracts_method_receiver", "signature": "def test_extracts_method_receiver(self)"}, {"kind": "method", "line": 159, "name": "test_extracts_import_block", "signature": "def test_extracts_import_block(self)"}, {"kind": "method", "line": 166, "name": "test_extracts_single_import", "signature": "def test_extracts_single_import(self)"}, {"kind": "method", "line": 172, "name": "test_extracts_struct_and_interface", "signature": "def test_extracts_struct_and_interface(self)"}, {"kind": "method", "line": 185, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 188, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 195, "name": "test_extracts_pub_function", "signature": "def test_extracts_pub_function(self)"}, {"kind": "method", "line": 202, "name": "test_extracts_struct_and_trait_and_enum", "signature": "def test_extracts_struct_and_trait_and_enum(self)"}, {"kind": "method", "line": 215, "name": "test_extracts_use", "signature": "def test_extracts_use(self)"}, {"kind": "method", "line": 223, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 226, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 233, "name": "test_extracts_arrow_function", "signature": "def test_extracts_arrow_function(self)"}, {"kind": "method", "line": 240, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 247, "name": "test_extracts_import_and_require", "signature": "def test_extracts_import_and_require(self)"}, {"kind": "method", "line": 254, "name": "test_skips_reserved_words", "signature": "def test_skips_reserved_words(self)"}, {"kind": "method", "line": 262, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 265, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 272, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 279, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 285, "name": "test_abstract_class", "signature": "def test_abstract_class(self)"}, {"kind": "method", "line": 294, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 297, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 304, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 311, "name": "test_extracts_using", "signature": "def test_extracts_using(self)"}, {"kind": "method", "line": 317, "name": "test_record_and_interface", "signature": "def test_record_and_interface(self)"}, {"kind": "method", "line": 327, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 330, "name": "test_extracts_function_with_parentheses", "signature": "def test_extracts_function_with_parentheses(self)"}, {"kind": "method", "line": 337, "name": "test_extracts_function_keyword", "signature": "def test_extracts_function_keyword(self)"}, {"kind": "method", "line": 346, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 349, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 356, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 363, "name": "test_extracts_use_and_require", "signature": "def test_extracts_use_and_require(self)"}, {"kind": "method", "line": 372, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 375, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 382, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 389, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 397, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 400, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 407, "name": "test_extracts_extends", "signature": "def test_extracts_extends(self)"}, {"kind": "method", "line": 415, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 418, "name": "test_extracts_proc", "signature": "def test_extracts_proc(self)"}, {"kind": "method", "line": 425, "name": "test_extracts_type", "signature": "def test_extracts_type(self)"}, {"kind": "method", "line": 432, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 441, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 444, "name": "test_extracts_label", "signature": "def test_extracts_label(self)"}, {"kind": "method", "line": 451, "name": "test_extracts_multiple_labels", "signature": "def test_extracts_multiple_labels(self)"}, {"kind": "method", "line": 461, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 464, "name": "test_returns_c_parser_for_c_extensions", "signature": "def test_returns_c_parser_for_c_extensions(self)"}, {"kind": "method", "line": 470, "name": "test_returns_python_parser_for_py", "signature": "def test_returns_python_parser_for_py(self)"}, {"kind": "method", "line": 475, "name": "test_returns_none_for_unknown_extension", "signature": "def test_returns_none_for_unknown_extension(self)"}, {"kind": "method", "line": 479, "name": "test_returns_rust_parser_for_rs", "signature": "def test_returns_rust_parser_for_rs(self)"}, {"kind": "method", "line": 484, "name": "test_case_insensitive_extension", "signature": "def test_case_insensitive_extension(self)"}]}, {"id": "tests/test_parsers_new.py", "kind": "module", "label": "test_parsers_new.py", "language": "py", "sha256": "a737c2342ea5e554", "symbol_count": 36, "symbols": [{"kind": "class", "line": 15, "name": "TestRubyParserContract", "signature": "class TestRubyParserContract(TestCase)"}, {"kind": "class", "line": 45, "name": "TestSwiftParserContract", "signature": "class TestSwiftParserContract(TestCase)"}, {"kind": "class", "line": 68, "name": "TestKotlinParserContract", "signature": "class TestKotlinParserContract(TestCase)"}, {"kind": "class", "line": 85, "name": "TestScalaParserContract", "signature": "class TestScalaParserContract(TestCase)"}, {"kind": "class", "line": 102, "name": "TestLuaParserContract", "signature": "class TestLuaParserContract(TestCase)"}, {"kind": "class", "line": 117, "name": "TestElixirParserContract", "signature": "class TestElixirParserContract(TestCase)"}, {"kind": "class", "line": 134, "name": "TestNewParserFactoryContract", "signature": "class TestNewParserFactoryContract(TestCase)"}, {"kind": "class", "line": 151, "name": "TestPythonCallExtractionContract", "signature": "class TestPythonCallExtractionContract(TestCase)"}, {"kind": "method", "line": 16, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 19, "name": "test_extracts_class_with_inheritance", "signature": "def test_extracts_class_with_inheritance(self)"}, {"kind": "method", "line": 27, "name": "test_extracts_module", "signature": "def test_extracts_module(self)"}, {"kind": "method", "line": 33, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 39, "name": "test_extracts_require", "signature": "def test_extracts_require(self)"}, {"kind": "method", "line": 46, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 49, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 55, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 61, "name": "test_extracts_protocol", "signature": "def test_extracts_protocol(self)"}, {"kind": "method", "line": 69, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 72, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 78, "name": "test_extracts_fun", "signature": "def test_extracts_fun(self)"}, {"kind": "method", "line": 86, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 89, "name": "test_extracts_object", "signature": "def test_extracts_object(self)"}, {"kind": "method", "line": 95, "name": "test_extracts_def", "signature": "def test_extracts_def(self)"}, {"kind": "method", "line": 103, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 106, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 111, "name": "test_extracts_require", "signature": "def test_extracts_require(self)"}, {"kind": "method", "line": 118, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 121, "name": "test_extracts_defmodule", "signature": "def test_extracts_defmodule(self)"}, {"kind": "method", "line": 127, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 135, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 138, "name": "test_ruby_extension_maps_correctly", "signature": "def test_ruby_extension_maps_correctly(self)"}, {"kind": "method", "line": 142, "name": "test_swift_extension_maps_correctly", "signature": "def test_swift_extension_maps_correctly(self)"}, {"kind": "method", "line": 146, "name": "test_kotlin_extension_maps_correctly", "signature": "def test_kotlin_extension_maps_correctly(self)"}, {"kind": "method", "line": 152, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 155, "name": "test_extracts_class_inheritance", "signature": "def test_extracts_class_inheritance(self)"}, {"kind": "method", "line": 160, "name": "test_extracts_function_calls", "signature": "def test_extracts_function_calls(self)"}]}, {"id": "tests/test_parsers_property.py", "kind": "module", "label": "test_parsers_property.py", "language": "py", "sha256": "6bc539b91198ee91", "symbol_count": 16, "symbols": [{"doc": "Generate source code with a configurable number of lines.", "kind": "function", "line": 67, "name": "_generate_multiline_code", "signature": "def _generate_multiline_code(lines, line_strategy)"}, {"doc": "Create a parser for the given extension.", "kind": "function", "line": 104, "name": "_create_parser", "signature": "def _create_parser(ext)"}, {"doc": "Property-based contract: parsers never crash on arbitrary input.", "kind": "class", "line": 117, "name": "TestParserHypothesisContract", "signature": "class TestParserHypothesisContract(TestCase)"}, {"doc": "Property-based tests specific to the Python parser (native ast).", "kind": "class", "line": 250, "name": "TestPythonParserProperty", "signature": "class TestPythonParserProperty(TestCase)"}, {"kind": "method", "line": 124, "name": "test_never_crashes_on_malformed_code", "signature": "def test_never_crashes_on_malformed_code(self, ext, code)"}, {"kind": "method", "line": 142, "name": "test_never_crashes_on_unicode_code", "signature": "def test_never_crashes_on_unicode_code(self, ext, code)"}, {"kind": "method", "line": 160, "name": "test_empty_code_returns_empty_or_valid", "signature": "def test_empty_code_returns_empty_or_valid(self, ext)"}, {"kind": "method", "line": 170, "name": "test_whitespace_code_returns_empty_or_valid", "signature": "def test_whitespace_code_returns_empty_or_valid(self, ext)"}, {"kind": "method", "line": 182, "name": "test_never_crashes_on_many_lines", "signature": "def test_never_crashes_on_many_lines(self, ext, lines)"}, {"kind": "method", "line": 200, "name": "test_repeated_keywords_no_crash", "signature": "def test_repeated_keywords_no_crash(self, ext)"}, {"kind": "method", "line": 219, "name": "test_parser_imports_is_list_of_strings", "signature": "def test_parser_imports_is_list_of_strings(self, ext)"}, {"kind": "method", "line": 231, "name": "test_unknown_extension_returns_none", "signature": "def test_unknown_extension_returns_none(self)"}, {"kind": "method", "line": 237, "name": "_assert_valid_symbols", "signature": "def _assert_valid_symbols(self, symbols)"}, {"kind": "method", "line": 253, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 258, "name": "test_python_never_crashes_on_weird_ascii", "signature": "def test_python_never_crashes_on_weird_ascii(self, code)"}, {"kind": "method", "line": 272, "name": "test_python_never_crashes_on_any_text", "signature": "def test_python_never_crashes_on_any_text(self, code)"}]}, {"id": "tests/test_query.py", "kind": "module", "label": "test_query.py", "language": "py", "sha256": "9065822de432127b", "symbol_count": 18, "symbols": [{"kind": "function", "line": 7, "name": "_make_node", "signature": "def _make_node(node_id, symbols)"}, {"kind": "function", "line": 18, "name": "_make_sym", "signature": "def _make_sym(name, kind, line)"}, {"kind": "class", "line": 22, "name": "TestQueryEngineContract", "signature": "class TestQueryEngineContract(TestCase)"}, {"kind": "method", "line": 23, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 36, "name": "test_find_exact_symbol", "signature": "def test_find_exact_symbol(self)"}, {"kind": "method", "line": 42, "name": "test_find_symbol_fuzzy", "signature": "def test_find_symbol_fuzzy(self)"}, {"kind": "method", "line": 47, "name": "test_find_symbol_not_found", "signature": "def test_find_symbol_not_found(self)"}, {"kind": "method", "line": 51, "name": "test_explain_returns_details", "signature": "def test_explain_returns_details(self)"}, {"kind": "method", "line": 58, "name": "test_explain_shows_imports", "signature": "def test_explain_shows_imports(self)"}, {"kind": "method", "line": 63, "name": "test_explain_shows_siblings", "signature": "def test_explain_shows_siblings(self)"}, {"kind": "method", "line": 69, "name": "test_explain_unknown_returns_none", "signature": "def test_explain_unknown_returns_none(self)"}, {"kind": "method", "line": 73, "name": "test_find_path_direct_import", "signature": "def test_find_path_direct_import(self)"}, {"kind": "method", "line": 79, "name": "test_find_path_same_file", "signature": "def test_find_path_same_file(self)"}, {"kind": "method", "line": 84, "name": "test_find_path_unknown_returns_none", "signature": "def test_find_path_unknown_returns_none(self)"}, {"kind": "method", "line": 88, "name": "test_summary_shows_counts", "signature": "def test_summary_shows_counts(self)"}, {"kind": "method", "line": 94, "name": "test_summary_shows_top_modules", "signature": "def test_summary_shows_top_modules(self)"}, {"kind": "method", "line": 98, "name": "test_query_returns_matching_symbols", "signature": "def test_query_returns_matching_symbols(self)"}, {"kind": "method", "line": 102, "name": "test_query_returns_file_matches", "signature": "def test_query_returns_file_matches(self)"}]}, {"id": "tests/test_ranking.py", "kind": "module", "label": "test_ranking.py", "language": "py", "sha256": "3b50ba6e273cbac1", "symbol_count": 72, "symbols": [{"kind": "class", "line": 60, "name": "TestEdgeKind", "signature": "class TestEdgeKind"}, {"kind": "class", "line": 84, "name": "TestMorphism", "signature": "class TestMorphism"}, {"kind": "class", "line": 104, "name": "TestCategory", "signature": "class TestCategory"}, {"kind": "class", "line": 183, "name": "TestTypedGraph", "signature": "class TestTypedGraph"}, {"kind": "method", "line": 238, "name": "_make_test_graph", "signature": "def _make_test_graph()"}, {"kind": "class", "line": 247, "name": "TestGlobalPageRank", "signature": "class TestGlobalPageRank"}, {"kind": "class", "line": 288, "name": "TestPersonalizedPageRank", "signature": "class TestPersonalizedPageRank"}, {"kind": "class", "line": 325, "name": "TestHITS", "signature": "class TestHITS"}, {"kind": "class", "line": 350, "name": "TestSeedGeneration", "signature": "class TestSeedGeneration"}, {"kind": "class", "line": 403, "name": "TestCompositeRanker", "signature": "class TestCompositeRanker"}, {"kind": "class", "line": 490, "name": "TestProjections", "signature": "class TestProjections"}, {"kind": "class", "line": 539, "name": "TestExplain", "signature": "class TestExplain"}, {"kind": "class", "line": 587, "name": "TestIntegration", "signature": "class TestIntegration"}, {"kind": "method", "line": 61, "name": "test_all_edge_kinds_have_weights", "signature": "def test_all_edge_kinds_have_weights(self)"}, {"kind": "method", "line": 66, "name": "test_infer_edge_kind_maps_correctly", "signature": "def test_infer_edge_kind_maps_correctly(self)"}, {"kind": "method", "line": 71, "name": "test_infer_edge_kind_falls_back", "signature": "def test_infer_edge_kind_falls_back(self)"}, {"kind": "method", "line": 75, "name": "test_edge_kind_is_str_enum", "signature": "def test_edge_kind_is_str_enum(self)"}, {"kind": "method", "line": 85, "name": "test_weight_is_edge_weight_times_confidence", "signature": "def test_weight_is_edge_weight_times_confidence(self)"}, {"kind": "method", "line": 90, "name": "test_weight_default_confidence", "signature": "def test_weight_default_confidence(self)"}, {"kind": "method", "line": 94, "name": "test_morphism_is_frozen", "signature": "def test_morphism_is_frozen(self)"}, {"kind": "method", "line": 105, "name": "test_empty_category", "signature": "def test_empty_category(self)"}, {"kind": "method", "line": 110, "name": "test_add_object_and_morphism", "signature": "def test_add_object_and_morphism(self)"}, {"kind": "method", "line": 118, "name": "test_outgoing_and_incoming", "signature": "def test_outgoing_and_incoming(self)"}, {"kind": "method", "line": 130, "name": "test_compose_same_kind", "signature": "def test_compose_same_kind(self)"}, {"kind": "method", "line": 140, "name": "test_compose_imports_then_defines", "signature": "def test_compose_imports_then_defines(self)"}, {"kind": "method", "line": 148, "name": "test_compose_incompatible_returns_none", "signature": "def test_compose_incompatible_returns_none(self)"}, {"kind": "method", "line": 155, "name": "test_compose_mismatched_target_source", "signature": "def test_compose_mismatched_target_source(self)"}, {"kind": "method", "line": 162, "name": "test_paths_finds_composition_chains", "signature": "def test_paths_finds_composition_chains(self)"}, {"kind": "method", "line": 171, "name": "test_paths_empty_when_no_route", "signature": "def test_paths_empty_when_no_route(self)"}, {"kind": "method", "line": 184, "name": "test_empty_graph", "signature": "def test_empty_graph(self)"}, {"kind": "method", "line": 190, "name": "test_stochastic_row_normalizes_to_one", "signature": "def test_stochastic_row_normalizes_to_one(self)"}, {"kind": "method", "line": 199, "name": "test_stochastic_row_empty_for_dangling", "signature": "def test_stochastic_row_empty_for_dangling(self)"}, {"kind": "method", "line": 205, "name": "test_transition_weight_aggregates_parallel_edges", "signature": "def test_transition_weight_aggregates_parallel_edges(self)"}, {"kind": "method", "line": 214, "name": "test_build_category_from_edges", "signature": "def test_build_category_from_edges(self)"}, {"kind": "method", "line": 225, "name": "test_build_category_from_edges_filters_by_node_ids", "signature": "def test_build_category_from_edges_filters_by_node_ids(self)"}, {"kind": "method", "line": 248, "name": "test_scores_sum_to_one", "signature": "def test_scores_sum_to_one(self)"}, {"kind": "method", "line": 254, "name": "test_all_nodes_have_positive_score", "signature": "def test_all_nodes_have_positive_score(self)"}, {"kind": "method", "line": 260, "name": "test_converges_within_max_iter", "signature": "def test_converges_within_max_iter(self)"}, {"kind": "method", "line": 266, "name": "test_stable_across_calls", "signature": "def test_stable_across_calls(self)"}, {"kind": "method", "line": 273, "name": "test_dangling_node_handled", "signature": "def test_dangling_node_handled(self)"}, {"kind": "method", "line": 284, "name": "test_empty_graph", "signature": "def test_empty_graph(self)"}, {"kind": "method", "line": 289, "name": "test_seed_node_gets_highest_score", "signature": "def test_seed_node_gets_highest_score(self)"}, {"kind": "method", "line": 296, "name": "test_scores_sum_to_one", "signature": "def test_scores_sum_to_one(self)"}, {"kind": "method", "line": 303, "name": "test_different_seeds_produce_different_rankings", "signature": "def test_different_seeds_produce_different_rankings(self)"}, {"kind": "method", "line": 310, "name": "test_empty_seeds_uses_uniform", "signature": "def test_empty_seeds_uses_uniform(self)"}, {"kind": "method", "line": 317, "name": "test_multi_seed", "signature": "def test_multi_seed(self)"}, {"kind": "method", "line": 326, "name": "test_authorities_and_hubs_have_positive_scores", "signature": "def test_authorities_and_hubs_have_positive_scores(self)"}, {"kind": "method", "line": 333, "name": "test_authorities_l2_normalized", "signature": "def test_authorities_l2_normalized(self)"}, {"kind": "method", "line": 339, "name": "test_hubs_l2_normalized", "signature": "def test_hubs_l2_normalized(self)"}, {"kind": "method", "line": 351, "name": "test_build_seeds_from_query_matches_node_id", "signature": "def test_build_seeds_from_query_matches_node_id(self)"}, {"kind": "method", "line": 363, "name": "test_build_seeds_from_query_matches_symbol", "signature": "def test_build_seeds_from_query_matches_symbol(self)"}, {"kind": "method", "line": 374, "name": "test_build_seeds_from_query_no_match_returns_empty", "signature": "def test_build_seeds_from_query_no_match_returns_empty(self)"}, {"kind": "method", "line": 383, "name": "test_build_seeds_for_context", "signature": "def test_build_seeds_for_context(self)"}, {"kind": "method", "line": 392, "name": "test_build_seeds_for_context_no_match", "signature": "def test_build_seeds_for_context_no_match(self)"}, {"kind": "method", "line": 404, "name": "test_rank_returns_sorted_results", "signature": "def test_rank_returns_sorted_results(self)"}, {"kind": "method", "line": 421, "name": "test_rank_items_have_all_score_fields", "signature": "def test_rank_items_have_all_score_fields(self)"}, {"kind": "method", "line": 447, "name": "test_noise_penalty_applied", "signature": "def test_noise_penalty_applied(self)"}, {"kind": "method", "line": 466, "name": "test_top_n", "signature": "def test_top_n(self)"}, {"kind": "method", "line": 479, "name": "test_explain_returns_none_for_missing", "signature": "def test_explain_returns_none_for_missing(self)"}, {"kind": "method", "line": 491, "name": "test_identity_projection_passes_all", "signature": "def test_identity_projection_passes_all(self)"}, {"kind": "method", "line": 498, "name": "test_doc_projection_filters_undocumented", "signature": "def test_doc_projection_filters_undocumented(self)"}, {"kind": "method", "line": 506, "name": "test_doc_projection_filters_morphism_kind", "signature": "def test_doc_projection_filters_morphism_kind(self)"}, {"kind": "method", "line": 512, "name": "test_apply_view_architecture", "signature": "def test_apply_view_architecture(self)"}, {"kind": "method", "line": 521, "name": "test_apply_view_reverse", "signature": "def test_apply_view_reverse(self)"}, {"kind": "method", "line": 528, "name": "test_apply_view_empty", "signature": "def test_apply_view_empty(self)"}, {"kind": "method", "line": 540, "name": "test_explain_rank_found", "signature": "def test_explain_rank_found(self)"}, {"kind": "method", "line": 559, "name": "test_explain_rank_not_found", "signature": "def test_explain_rank_not_found(self)"}, {"kind": "method", "line": 565, "name": "test_rank_summary_format", "signature": "def test_rank_summary_format(self)"}, {"kind": "method", "line": 588, "name": "test_category_from_real_edges", "signature": "def test_category_from_real_edges(self)"}, {"kind": "method", "line": 613, "name": "test_pagerank_on_real_category", "signature": "def test_pagerank_on_real_category(self)"}, {"kind": "method", "line": 625, "name": "test_ppr_favors_seed", "signature": "def test_ppr_favors_seed(self)"}, {"kind": "method", "line": 637, "name": "test_ranker_from_real_data", "signature": "def test_ranker_from_real_data(self)"}]}, {"id": "tests/test_readme_injector.py", "kind": "module", "label": "test_readme_injector.py", "language": "py", "sha256": "b19d29474042de26", "symbol_count": 26, "symbols": [{"doc": "BDD: ReadmeInjector injection contract.", "kind": "class", "line": 16, "name": "TestReadmeInjectorInjectBehavior", "signature": "class TestReadmeInjectorInjectBehavior(TestCase)"}, {"doc": "BDD: ReadmeInjector removal contract.", "kind": "class", "line": 71, "name": "TestReadmeInjectorRemoveBehavior", "signature": "class TestReadmeInjectorRemoveBehavior(TestCase)"}, {"doc": "BDD: ReadmeInjector README file detection contract.", "kind": "class", "line": 104, "name": "TestReadmeInjectorFindReadme", "signature": "class TestReadmeInjectorFindReadme(TestCase)"}, {"doc": "BDD: ReadmeInjector edge case contract.", "kind": "class", "line": 139, "name": "TestReadmeInjectorEdgeCases", "signature": "class TestReadmeInjectorEdgeCases(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 24, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 28, "name": "test_inject_into_markdown_readme_adds_kb_link", "signature": "def test_inject_into_markdown_readme_adds_kb_link(self)"}, {"kind": "method", "line": 38, "name": "test_inject_into_rst_readme_adds_kb_link", "signature": "def test_inject_into_rst_readme_adds_kb_link(self)"}, {"kind": "method", "line": 47, "name": "test_inject_is_idempotent_does_not_duplicate", "signature": "def test_inject_is_idempotent_does_not_duplicate(self)"}, {"kind": "method", "line": 58, "name": "test_inject_no_readme_file_returns_false", "signature": "def test_inject_no_readme_file_returns_false(self)"}, {"kind": "method", "line": 62, "name": "test_inject_preserves_existing_content", "signature": "def test_inject_preserves_existing_content(self)"}, {"kind": "method", "line": 74, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 79, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 83, "name": "test_remove_strips_injected_section", "signature": "def test_remove_strips_injected_section(self)"}, {"kind": "method", "line": 93, "name": "test_remove_without_injection_returns_false", "signature": "def test_remove_without_injection_returns_false(self)"}, {"kind": "method", "line": 99, "name": "test_remove_no_readme_returns_false", "signature": "def test_remove_no_readme_returns_false(self)"}, {"kind": "method", "line": 107, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 111, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 115, "name": "test_finds_readme_md", "signature": "def test_finds_readme_md(self)"}, {"kind": "method", "line": 121, "name": "test_finds_readme_rst", "signature": "def test_finds_readme_rst(self)"}, {"kind": "method", "line": 127, "name": "test_prefers_readme_md_over_rst", "signature": "def test_prefers_readme_md_over_rst(self)"}, {"kind": "method", "line": 134, "name": "test_returns_none_when_no_readme", "signature": "def test_returns_none_when_no_readme(self)"}, {"kind": "method", "line": 142, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 147, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 151, "name": "test_inject_into_empty_readme", "signature": "def test_inject_into_empty_readme(self)"}, {"kind": "method", "line": 159, "name": "test_custom_kb_filename_works", "signature": "def test_custom_kb_filename_works(self)"}]}, {"id": "tests/test_refactorizer.py", "kind": "module", "label": "test_refactorizer.py", "language": "py", "sha256": "e6cf2a22e1c89a39", "symbol_count": 17, "symbols": [{"doc": "Contract: MonolithRefactorizer generates refactoring plans.", "kind": "class", "line": 18, "name": "TestMonolithRefactorizerContract", "signature": "class TestMonolithRefactorizerContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 25, "name": "_make_symbol", "signature": "def _make_symbol(self, name, kind, line)"}, {"kind": "method", "line": 28, "name": "_make_node", "signature": "def _make_node(self, nid, symbols)"}, {"kind": "method", "line": 37, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt)"}, {"kind": "method", "line": 40, "name": "test_analyze_empty_graph_returns_empty", "signature": "def test_analyze_empty_graph_returns_empty(self)"}, {"kind": "method", "line": 44, "name": "test_analyze_ignores_small_files", "signature": "def test_analyze_ignores_small_files(self)"}, {"kind": "method", "line": 50, "name": "test_analyze_detects_large_file", "signature": "def test_analyze_detects_large_file(self)"}, {"kind": "method", "line": 59, "name": "test_analyze_generates_extract_class_for_multiple_classes", "signature": "def test_analyze_generates_extract_class_for_multiple_classes(self)"}, {"kind": "method", "line": 74, "name": "test_analyze_generates_extract_function_for_multiple_functions", "signature": "def test_analyze_generates_extract_function_for_multiple_functions(self)"}, {"kind": "method", "line": 89, "name": "test_analyze_splits_file_with_many_symbols", "signature": "def test_analyze_splits_file_with_many_symbols(self)"}, {"kind": "method", "line": 97, "name": "test_analyze_estimates_impact_from_resolved_edges", "signature": "def test_analyze_estimates_impact_from_resolved_edges(self)"}, {"kind": "method", "line": 109, "name": "test_generate_script_contains_shebang", "signature": "def test_generate_script_contains_shebang(self)"}, {"kind": "method", "line": 129, "name": "test_generate_script_contains_set_e", "signature": "def test_generate_script_contains_set_e(self)"}, {"kind": "method", "line": 140, "name": "test_generate_script_contains_sed_commands", "signature": "def test_generate_script_contains_sed_commands(self)"}, {"kind": "method", "line": 160, "name": "test_analyze_sorted_by_line_count", "signature": "def test_analyze_sorted_by_line_count(self)"}, {"kind": "method", "line": 173, "name": "test_analyze_respects_max_files_limit", "signature": "def test_analyze_respects_max_files_limit(self)"}]}, {"id": "tests/test_resolver.py", "kind": "module", "label": "test_resolver.py", "language": "py", "sha256": "92f1d5514af2d416", "symbol_count": 11, "symbols": [{"doc": "Contract: ImportResolver maps import strings to file paths.", "kind": "class", "line": 15, "name": "TestImportResolverContract", "signature": "class TestImportResolverContract(TestCase)"}, {"kind": "method", "line": 18, "name": "test_resolves_python_module_dotpath", "signature": "def test_resolves_python_module_dotpath(self)"}, {"kind": "method", "line": 25, "name": "test_resolves_relative_import", "signature": "def test_resolves_relative_import(self)"}, {"kind": "method", "line": 32, "name": "test_resolves_extensionless_python_import", "signature": "def test_resolves_extensionless_python_import(self)"}, {"kind": "method", "line": 39, "name": "test_resolves_package_init", "signature": "def test_resolves_package_init(self)"}, {"kind": "method", "line": 46, "name": "test_returns_none_for_external_stdlib", "signature": "def test_returns_none_for_external_stdlib(self)"}, {"kind": "method", "line": 53, "name": "test_returns_none_for_unknown_import", "signature": "def test_returns_none_for_unknown_import(self)"}, {"kind": "method", "line": 60, "name": "test_resolves_stem_match_when_unique", "signature": "def test_resolves_stem_match_when_unique(self)"}, {"kind": "method", "line": 67, "name": "test_returns_none_for_empty_import", "signature": "def test_returns_none_for_empty_import(self)"}, {"kind": "method", "line": 72, "name": "test_resolves_go_import", "signature": "def test_resolves_go_import(self)"}, {"kind": "method", "line": 79, "name": "test_resolves_same_directory_import", "signature": "def test_resolves_same_directory_import(self)"}]}, {"id": "tests/test_rule_gen.py", "kind": "module", "label": "test_rule_gen.py", "language": "py", "sha256": "fe6c1fc2b2c56a51", "symbol_count": 10, "symbols": [{"doc": "Contract: RuleGenerator detects patterns and suggests rules.", "kind": "class", "line": 12, "name": "TestRuleGeneratorContract", "signature": "class TestRuleGeneratorContract(TestCase)"}, {"kind": "method", "line": 15, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 19, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 29, "name": "_make_node_with_symbols", "signature": "def _make_node_with_symbols(self, nid, sym_count)"}, {"kind": "method", "line": 44, "name": "test_empty_nodes_returns_empty_rules", "signature": "def test_empty_nodes_returns_empty_rules(self)"}, {"kind": "method", "line": 48, "name": "test_generates_rules_for_function_heavy_language", "signature": "def test_generates_rules_for_function_heavy_language(self)"}, {"kind": "method", "line": 56, "name": "test_detects_antipatterns_with_content", "signature": "def test_detects_antipatterns_with_content(self)"}, {"kind": "method", "line": 67, "name": "test_antipattern_threshold_from_config", "signature": "def test_antipattern_threshold_from_config(self)"}, {"kind": "method", "line": 77, "name": "test_write_rules_creates_files", "signature": "def test_write_rules_creates_files(self)"}, {"kind": "method", "line": 90, "name": "test_rule_id_increments", "signature": "def test_rule_id_increments(self)"}]}, {"id": "tests/test_sarif.py", "kind": "module", "label": "test_sarif.py", "language": "py", "sha256": "6522296ceb83662c", "symbol_count": 10, "symbols": [{"doc": "Contract: SarifExporter produces valid SARIF v2.1.0 JSON.", "kind": "class", "line": 11, "name": "TestSarifExporterContract", "signature": "class TestSarifExporterContract(TestCase)"}, {"kind": "method", "line": 14, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 18, "name": "_make_finding", "signature": "def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)"}, {"kind": "method", "line": 38, "name": "test_export_returns_valid_json", "signature": "def test_export_returns_valid_json(self)"}, {"kind": "method", "line": 46, "name": "test_export_includes_tool_info", "signature": "def test_export_includes_tool_info(self)"}, {"kind": "method", "line": 54, "name": "test_export_includes_rule", "signature": "def test_export_includes_rule(self)"}, {"kind": "method", "line": 62, "name": "test_export_includes_result", "signature": "def test_export_includes_result(self)"}, {"kind": "method", "line": 73, "name": "test_severity_maps_correctly", "signature": "def test_severity_maps_correctly(self)"}, {"kind": "method", "line": 88, "name": "test_privacy_mode_strips_snippets", "signature": "def test_privacy_mode_strips_snippets(self)"}, {"kind": "method", "line": 97, "name": "test_empty_findings_produces_valid_sarif", "signature": "def test_empty_findings_produces_valid_sarif(self)"}]}, {"id": "tests/test_scanner.py", "kind": "module", "label": "test_scanner.py", "language": "py", "sha256": "ede5f381a6fbf273", "symbol_count": 17, "symbols": [{"kind": "class", "line": 11, "name": "TestScannerContract", "signature": "class TestScannerContract(TestCase)"}, {"kind": "method", "line": 12, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 16, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 20, "name": "_write", "signature": "def _write(self, path, content)"}, {"kind": "method", "line": 25, "name": "test_scans_python_files", "signature": "def test_scans_python_files(self)"}, {"kind": "method", "line": 32, "name": "test_ignores_env_and_vendor_dirs", "signature": "def test_ignores_env_and_vendor_dirs(self)"}, {"kind": "method", "line": 45, "name": "test_rejects_symlinks", "signature": "def test_rejects_symlinks(self)"}, {"kind": "method", "line": 59, "name": "test_skips_non_code_files", "signature": "def test_skips_non_code_files(self)"}, {"kind": "method", "line": 70, "name": "test_scans_multiple_languages", "signature": "def test_scans_multiple_languages(self)"}, {"kind": "method", "line": 79, "name": "test_respects_max_directory_depth", "signature": "def test_respects_max_directory_depth(self)"}, {"kind": "method", "line": 89, "name": "test_raises_on_invalid_directory", "signature": "def test_raises_on_invalid_directory(self)"}, {"kind": "method", "line": 94, "name": "test_import_edges_are_created", "signature": "def test_import_edges_are_created(self)"}, {"kind": "method", "line": 104, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 114, "name": "test_scan_with_content_returns_content_map", "signature": "def test_scan_with_content_returns_content_map(self)"}, {"kind": "method", "line": 122, "name": "test_gitignore_respected_when_enabled", "signature": "def test_gitignore_respected_when_enabled(self)"}, {"kind": "method", "line": 133, "name": "test_gitignore_disabled_by_default", "signature": "def test_gitignore_disabled_by_default(self)"}, {"kind": "method", "line": 142, "name": "test_gitignore_glob_conversion", "signature": "def test_gitignore_glob_conversion(self)"}]}, {"id": "tests/test_security.py", "kind": "module", "label": "test_security.py", "language": "py", "sha256": "1d6c761aa2bbc230", "symbol_count": 63, "symbols": [{"doc": "SecurityFinding dataclass contract tests.", "kind": "class", "line": 21, "name": "TestSecurityFinding", "signature": "class TestSecurityFinding(TestCase)"}, {"doc": "SecurityAnalyzer configuration contract tests.", "kind": "class", "line": 43, "name": "TestSecurityAnalyzerConfig", "signature": "class TestSecurityAnalyzerConfig(TestCase)"}, {"doc": "Per-language rule detection tests using inline code.", "kind": "class", "line": 64, "name": "TestSecurityAnalyzerRules", "signature": "class TestSecurityAnalyzerRules(TestCase)"}, {"doc": "Severity threshold filtering tests.", "kind": "class", "line": 295, "name": "TestSecurityAnalyzerThreshold", "signature": "class TestSecurityAnalyzerThreshold(TestCase)"}, {"doc": "Security path validation tests.", "kind": "class", "line": 327, "name": "TestSecurityAnalyzerPathValidation", "signature": "class TestSecurityAnalyzerPathValidation(TestCase)"}, {"doc": "Security summary output tests.", "kind": "class", "line": 374, "name": "TestSecurityAnalyzerSummary", "signature": "class TestSecurityAnalyzerSummary(TestCase)"}, {"kind": "method", "line": 24, "name": "test_security_finding_fields", "signature": "def test_security_finding_fields(self)"}, {"kind": "method", "line": 46, "name": "test_default_config_disables_security", "signature": "def test_default_config_disables_security(self)"}, {"kind": "method", "line": 50, "name": "test_default_severity_threshold", "signature": "def test_default_severity_threshold(self)"}, {"kind": "method", "line": 54, "name": "test_default_security_output", "signature": "def test_default_security_output(self)"}, {"kind": "method", "line": 58, "name": "test_init_with_config", "signature": "def test_init_with_config(self)"}, {"kind": "method", "line": 67, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Write content to a temp file and scan it.", "kind": "method", "line": 71, "name": "_scan_content", "signature": "def _scan_content(self, content, extension)"}, {"kind": "method", "line": 78, "name": "test_python_os_system", "signature": "def test_python_os_system(self)"}, {"kind": "method", "line": 83, "name": "test_python_eval", "signature": "def test_python_eval(self)"}, {"kind": "method", "line": 88, "name": "test_python_pickle", "signature": "def test_python_pickle(self)"}, {"kind": "method", "line": 93, "name": "test_python_sql_injection", "signature": "def test_python_sql_injection(self)"}, {"kind": "method", "line": 98, "name": "test_python_hardcoded_secret", "signature": "def test_python_hardcoded_secret(self)"}, {"kind": "method", "line": 103, "name": "test_python_weak_crypto", "signature": "def test_python_weak_crypto(self)"}, {"kind": "method", "line": 108, "name": "test_python_request_verify_false", "signature": "def test_python_request_verify_false(self)"}, {"kind": "method", "line": 113, "name": "test_python_flask_debug", "signature": "def test_python_flask_debug(self)"}, {"kind": "method", "line": 118, "name": "test_python_yaml_load", "signature": "def test_python_yaml_load(self)"}, {"kind": "method", "line": 123, "name": "test_javascript_inner_html", "signature": "def test_javascript_inner_html(self)"}, {"kind": "method", "line": 128, "name": "test_javascript_eval", "signature": "def test_javascript_eval(self)"}, {"kind": "method", "line": 133, "name": "test_javascript_child_process", "signature": "def test_javascript_child_process(self)"}, {"kind": "method", "line": 138, "name": "test_javascript_dangerously_set_inner_html", "signature": "def test_javascript_dangerously_set_inner_html(self)"}, {"kind": "method", "line": 143, "name": "test_c_strcpy", "signature": "def test_c_strcpy(self)"}, {"kind": "method", "line": 148, "name": "test_c_gets", "signature": "def test_c_gets(self)"}, {"kind": "method", "line": 153, "name": "test_c_system", "signature": "def test_c_system(self)"}, {"kind": "method", "line": 158, "name": "test_java_runtime_exec", "signature": "def test_java_runtime_exec(self)"}, {"kind": "method", "line": 163, "name": "test_java_sql_injection", "signature": "def test_java_sql_injection(self)"}, {"kind": "method", "line": 168, "name": "test_go_exec_command", "signature": "def test_go_exec_command(self)"}, {"kind": "method", "line": 173, "name": "test_ruby_eval", "signature": "def test_ruby_eval(self)"}, {"kind": "method", "line": 178, "name": "test_ruby_marshal_load", "signature": "def test_ruby_marshal_load(self)"}, {"kind": "method", "line": 183, "name": "test_php_eval", "signature": "def test_php_eval(self)"}, {"kind": "method", "line": 188, "name": "test_php_sql_injection", "signature": "def test_php_sql_injection(self)"}, {"kind": "method", "line": 193, "name": "test_php_unseralize", "signature": "def test_php_unseralize(self)"}, {"kind": "method", "line": 198, "name": "test_shell_eval", "signature": "def test_shell_eval(self)"}, {"kind": "method", "line": 203, "name": "test_csharp_process_start", "signature": "def test_csharp_process_start(self)"}, {"kind": "method", "line": 208, "name": "test_kotlin_runtime_exec", "signature": "def test_kotlin_runtime_exec(self)"}, {"kind": "method", "line": 213, "name": "test_swift_process", "signature": "def test_swift_process(self)"}, {"kind": "method", "line": 218, "name": "test_lua_load", "signature": "def test_lua_load(self)"}, {"kind": "method", "line": 223, "name": "test_lua_os_execute", "signature": "def test_lua_os_execute(self)"}, {"kind": "method", "line": 228, "name": "test_dart_process_run", "signature": "def test_dart_process_run(self)"}, {"kind": "method", "line": 233, "name": "test_rust_unsafe", "signature": "def test_rust_unsafe(self)"}, {"kind": "method", "line": 238, "name": "test_elixir_code_eval", "signature": "def test_elixir_code_eval(self)"}, {"kind": "method", "line": 243, "name": "test_elixir_system_cmd", "signature": "def test_elixir_system_cmd(self)"}, {"kind": "method", "line": 248, "name": "test_gdscript_os_execute", "signature": "def test_gdscript_os_execute(self)"}, {"kind": "method", "line": 253, "name": "test_scala_runtime_exec", "signature": "def test_scala_runtime_exec(self)"}, {"kind": "method", "line": 258, "name": "test_nim_exec_process", "signature": "def test_nim_exec_process(self)"}, {"kind": "method", "line": 263, "name": "test_safe_code_produces_no_findings", "signature": "def test_safe_code_produces_no_findings(self)"}, {"kind": "method", "line": 274, "name": "test_csharp_binary_formatter", "signature": "def test_csharp_binary_formatter(self)"}, {"kind": "method", "line": 279, "name": "test_ruby_backtick", "signature": "def test_ruby_backtick(self)"}, {"kind": "method", "line": 284, "name": "test_php_xss", "signature": "def test_php_xss(self)"}, {"kind": "method", "line": 289, "name": "test_go_unsafe_package", "signature": "def test_go_unsafe_package(self)"}, {"kind": "method", "line": 298, "name": "test_threshold_filters_low", "signature": "def test_threshold_filters_low(self)"}, {"kind": "method", "line": 312, "name": "test_threshold_info_shows_all", "signature": "def test_threshold_info_shows_all(self)"}, {"kind": "method", "line": 330, "name": "test_ignores_symlinks", "signature": "def test_ignores_symlinks(self)"}, {"kind": "method", "line": 345, "name": "test_ignores_ignored_dirs", "signature": "def test_ignores_ignored_dirs(self)"}, {"kind": "method", "line": 357, "name": "test_empty_directory", "signature": "def test_empty_directory(self)"}, {"kind": "method", "line": 364, "name": "test_unsupported_extension", "signature": "def test_unsupported_extension(self)"}, {"kind": "method", "line": 377, "name": "test_summary_empty", "signature": "def test_summary_empty(self)"}, {"kind": "method", "line": 383, "name": "test_summary_with_findings", "signature": "def test_summary_with_findings(self)"}]}, {"id": "tests/test_taint.py", "kind": "module", "label": "test_taint.py", "language": "py", "sha256": "d196fca30ed7d086", "symbol_count": 10, "symbols": [{"doc": "Contract: TaintAnalyzer discovers taint propagation paths.", "kind": "class", "line": 10, "name": "TestTaintAnalyzerContract", "signature": "class TestTaintAnalyzerContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label)"}, {"kind": "method", "line": 20, "name": "test_empty_graph_returns_empty_result", "signature": "def test_empty_graph_returns_empty_result(self)"}, {"kind": "method", "line": 25, "name": "test_no_dangerous_imports_returns_empty", "signature": "def test_no_dangerous_imports_returns_empty(self)"}, {"kind": "method", "line": 31, "name": "test_direct_dangerous_import_found", "signature": "def test_direct_dangerous_import_found(self)"}, {"kind": "method", "line": 38, "name": "test_taint_propagates_through_resolved_edges", "signature": "def test_taint_propagates_through_resolved_edges(self)"}, {"kind": "method", "line": 62, "name": "test_dangerous_import_by_language", "signature": "def test_dangerous_import_by_language(self)"}, {"kind": "method", "line": 70, "name": "test_taint_path_has_severity", "signature": "def test_taint_path_has_severity(self)"}, {"kind": "method", "line": 77, "name": "test_max_depth_limits_propagation", "signature": "def test_max_depth_limits_propagation(self)"}]}, {"id": "tests/test_taint_bdd.py", "kind": "module", "label": "test_taint_bdd.py", "language": "py", "sha256": "7d68f72a29549f07", "symbol_count": 26, "symbols": [{"kind": "function", "line": 29, "name": "_build_project_files", "signature": "def _build_project_files(project, root)"}, {"kind": "function", "line": 36, "name": "_scan_project", "signature": "def _scan_project(root, cfg)"}, {"kind": "function", "line": 54, "name": "_run_taint", "signature": "def _run_taint(files, cfg)"}, {"kind": "function", "line": 71, "name": "test_direct_dangerous_import", "signature": "def test_direct_dangerous_import()"}, {"kind": "function", "line": 75, "name": "test_taint_propagates_chain", "signature": "def test_taint_propagates_chain()"}, {"kind": "function", "line": 79, "name": "test_taint_max_depth", "signature": "def test_taint_max_depth()"}, {"kind": "function", "line": 83, "name": "test_cross_language_taint", "signature": "def test_cross_language_taint()"}, {"kind": "function", "line": 87, "name": "test_bdd_skipped", "signature": "def test_bdd_skipped()"}, {"kind": "function", "line": 112, "name": "_bkg", "signature": "def _bkg()"}, {"kind": "function", "line": 117, "name": "_direct_given", "signature": "def _direct_given()"}, {"kind": "function", "line": 121, "name": "_direct_when", "signature": "def _direct_when(_taint_result)"}, {"kind": "function", "line": 125, "name": "_check_has_path", "signature": "def _check_has_path(_taint_result)"}, {"kind": "function", "line": 130, "name": "_check_direct_path", "signature": "def _check_direct_path(_taint_result)"}, {"kind": "function", "line": 135, "name": "_check_src", "signature": "def _check_src(_taint_result)"}, {"kind": "function", "line": 139, "name": "_check_sink", "signature": "def _check_sink(_taint_result)"}, {"kind": "function", "line": 144, "name": "_chain_given", "signature": "def _chain_given()"}, {"kind": "function", "line": 148, "name": "_chain_when", "signature": "def _chain_when(_taint_result)"}, {"kind": "function", "line": 152, "name": "_check_long_path", "signature": "def _check_long_path(_taint_result)"}, {"kind": "function", "line": 159, "name": "_shallow_cfg", "signature": "def _shallow_cfg()"}, {"kind": "function", "line": 163, "name": "_chain_given2", "signature": "def _chain_given2()"}, {"kind": "function", "line": 167, "name": "_run_shallow", "signature": "def _run_shallow(_shallow_cfg)"}, {"kind": "function", "line": 171, "name": "_check_shallow", "signature": "def _check_shallow(_taint_result)"}, {"kind": "function", "line": 178, "name": "_js_given", "signature": "def _js_given()"}, {"kind": "function", "line": 182, "name": "_js_when", "signature": "def _js_when(_taint_result)"}, {"kind": "function", "line": 186, "name": "_check_js_dangerous", "signature": "def _check_js_dangerous(_taint_result)"}, {"kind": "function", "line": 192, "name": "_check_js_source", "signature": "def _check_js_source(_taint_result)"}]}, {"id": "tests/test_uml.py", "kind": "module", "label": "test_uml.py", "language": "py", "sha256": "7988cf8ccdf212bc", "symbol_count": 49, "symbols": [{"doc": "BDD: UmlGenerator mermaid class diagram rendering contract.", "kind": "class", "line": 16, "name": "TestUmlMermaidDiagram", "signature": "class TestUmlMermaidDiagram(TestCase)"}, {"doc": "BDD: UmlGenerator ID sanitization contract.", "kind": "class", "line": 157, "name": "TestUmlSanitizeId", "signature": "class TestUmlSanitizeId(TestCase)"}, {"doc": "BDD: C++ code generation contract.", "kind": "class", "line": 181, "name": "TestUmlCodeGenerationCpp", "signature": "class TestUmlCodeGenerationCpp(TestCase)"}, {"doc": "BDD: Java code generation contract.", "kind": "class", "line": 239, "name": "TestUmlCodeGenerationJava", "signature": "class TestUmlCodeGenerationJava(TestCase)"}, {"doc": "BDD: C# code generation contract.", "kind": "class", "line": 281, "name": "TestUmlCodeGenerationCSharp", "signature": "class TestUmlCodeGenerationCSharp(TestCase)"}, {"doc": "BDD: Go code generation contract.", "kind": "class", "line": 306, "name": "TestUmlCodeGenerationGo", "signature": "class TestUmlCodeGenerationGo(TestCase)"}, {"doc": "BDD: Rust code generation contract.", "kind": "class", "line": 347, "name": "TestUmlCodeGenerationRust", "signature": "class TestUmlCodeGenerationRust(TestCase)"}, {"doc": "BDD: PHP code generation contract.", "kind": "class", "line": 387, "name": "TestUmlCodeGenerationPhp", "signature": "class TestUmlCodeGenerationPhp(TestCase)"}, {"doc": "BDD: Kotlin, Scala, Swift, Dart, Ruby code generation contracts.", "kind": "class", "line": 427, "name": "TestUmlCodeGenerationKotlinScalaSwiftDartRuby", "signature": "class TestUmlCodeGenerationKotlinScalaSwiftDartRuby(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "test_render_empty_nodes_returns_empty_string", "signature": "def test_render_empty_nodes_returns_empty_string(self)"}, {"kind": "method", "line": 27, "name": "test_render_no_class_symbols_returns_empty_string", "signature": "def test_render_no_class_symbols_returns_empty_string(self)"}, {"kind": "method", "line": 42, "name": "test_render_single_class_produces_mermaid_class_diagram", "signature": "def test_render_single_class_produces_mermaid_class_diagram(self)"}, {"kind": "method", "line": 62, "name": "test_render_multiple_classes_from_different_files", "signature": "def test_render_multiple_classes_from_different_files(self)"}, {"kind": "method", "line": 90, "name": "test_render_with_import_edges_produces_relationships", "signature": "def test_render_with_import_edges_produces_relationships(self)"}, {"kind": "method", "line": 119, "name": "test_render_respects_max_classes_limit", "signature": "def test_render_respects_max_classes_limit(self)"}, {"kind": "method", "line": 137, "name": "test_render_with_structs_interfaces_traits", "signature": "def test_render_with_structs_interfaces_traits(self)"}, {"kind": "method", "line": 160, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 164, "name": "test_sanitize_preserves_alphanumeric", "signature": "def test_sanitize_preserves_alphanumeric(self)"}, {"kind": "method", "line": 168, "name": "test_sanitize_replaces_special_chars", "signature": "def test_sanitize_replaces_special_chars(self)"}, {"kind": "method", "line": 172, "name": "test_sanitize_prefixes_digit_start", "signature": "def test_sanitize_prefixes_digit_start(self)"}, {"kind": "method", "line": 176, "name": "test_sanitize_handles_empty_string", "signature": "def test_sanitize_handles_empty_string(self)"}, {"kind": "method", "line": 184, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 188, "name": "test_generate_cpp_produces_valid_code", "signature": "def test_generate_cpp_produces_valid_code(self)"}, {"kind": "method", "line": 208, "name": "test_generate_cpp_with_empty_classes", "signature": "def test_generate_cpp_with_empty_classes(self)"}, {"kind": "method", "line": 223, "name": "test_generate_cpp_unknown_language_returns_error_message", "signature": "def test_generate_cpp_unknown_language_returns_error_message(self)"}, {"kind": "method", "line": 242, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 246, "name": "test_generate_java_class_produces_valid_code", "signature": "def test_generate_java_class_produces_valid_code(self)"}, {"kind": "method", "line": 265, "name": "test_generate_java_interface_produces_interface", "signature": "def test_generate_java_interface_produces_interface(self)"}, {"kind": "method", "line": 284, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 288, "name": "test_generate_csharp_produces_valid_code", "signature": "def test_generate_csharp_produces_valid_code(self)"}, {"kind": "method", "line": 309, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 313, "name": "test_generate_go_struct_produces_valid_code", "signature": "def test_generate_go_struct_produces_valid_code(self)"}, {"kind": "method", "line": 330, "name": "test_generate_go_interface_produces_valid_code", "signature": "def test_generate_go_interface_produces_valid_code(self)"}, {"kind": "method", "line": 350, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 354, "name": "test_generate_rust_struct_produces_valid_code", "signature": "def test_generate_rust_struct_produces_valid_code(self)"}, {"kind": "method", "line": 370, "name": "test_generate_rust_trait_produces_valid_code", "signature": "def test_generate_rust_trait_produces_valid_code(self)"}, {"kind": "method", "line": 390, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 394, "name": "test_generate_php_class_produces_valid_code", "signature": "def test_generate_php_class_produces_valid_code(self)"}, {"kind": "method", "line": 411, "name": "test_generate_php_interface_produces_valid_code", "signature": "def test_generate_php_interface_produces_valid_code(self)"}, {"kind": "method", "line": 430, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 434, "name": "_make_class_node", "signature": "def _make_class_node(self, name, lang, kind)"}, {"kind": "method", "line": 446, "name": "test_generate_kotlin_produces_valid_code", "signature": "def test_generate_kotlin_produces_valid_code(self)"}, {"kind": "method", "line": 452, "name": "test_generate_scala_produces_valid_code", "signature": "def test_generate_scala_produces_valid_code(self)"}, {"kind": "method", "line": 458, "name": "test_generate_scala_trait_produces_valid_code", "signature": "def test_generate_scala_trait_produces_valid_code(self)"}, {"kind": "method", "line": 463, "name": "test_generate_swift_produces_valid_code", "signature": "def test_generate_swift_produces_valid_code(self)"}, {"kind": "method", "line": 469, "name": "test_generate_swift_protocol_produces_valid_code", "signature": "def test_generate_swift_protocol_produces_valid_code(self)"}, {"kind": "method", "line": 474, "name": "test_generate_dart_produces_valid_code", "signature": "def test_generate_dart_produces_valid_code(self)"}, {"kind": "method", "line": 480, "name": "test_generate_ruby_produces_valid_code", "signature": "def test_generate_ruby_produces_valid_code(self)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (88 files)

#### `__init__.py`
**Path:** `readmenator/__init__.py`

*No symbols extracted*

#### `__main__.py`
**Path:** `readmenator/__main__.py`

**Functions:**
- `build_parser` (line 15) `def build_parser()`
- `_run_tests` (line 97) `def _run_tests()`
- `main` (line 112) `def main()`

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
- `readmenatorApplication` (line 33) `class readmenatorApplication`

**Methods:**
- `__init__` (line 34) `def __init__(self, config)`
- `_scan` (line 43) `def _scan(self, target_dir)`
- `_scan_with_content` (line 51) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (line 61) `def _resolve_imports(self, nodes, edges, target_dir)`
- `run` (line 80) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- `_write_sidecar_outputs` (line 174) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_inject_readme_link` (line 200) `def _inject_readme_link(self, root)`
- `generate_uml_code` (line 208) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (line 220) `def _log_summary(self, nodes, edges, resolved_edges, analysis, layer_summary, analysis_v2, findings)`
- `update` (line 274) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (line 362) `def _scan_for_cache(self, root, cache)`
- `query` (line 380) `def query(self, target_dir, question)`
- `explain` (line 385) `def explain(self, target_dir, symbol_name)`
- `find_path` (line 397) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (line 410) `def summary(self, target_dir)`
- `rank_query` (line 415) `def rank_query(self, target_dir, query, top_n)` - *Run a ranked query against the knowledge graph.

Uses Personalized PageRank seeded from query terms to produce
a relevance-ranked list of files with score decomposition.

Args:
    target_dir: Project root directory.
    query: Free-text query.
    top_n: Number of results.

Returns:
    A RankedResult with scored items.*
- `rebuild` (line 445) `def rebuild(self, target_dir, run_security)`
- `analyze` (line 448) `def analyze(self, target_dir)`
- `export_json` (line 452) `def export_json(self, target_dir, output_path)`
- `export_html` (line 463) `def export_html(self, target_dir, output_path)`
- `export_svg` (line 474) `def export_svg(self, target_dir, output_path)`
- `export` (line 485) `def export(self, target_dir)`
- `export_graphml` (line 490) `def export_graphml(self, target_dir, output_path)`
- `export_cypher` (line 501) `def export_cypher(self, target_dir, output_path)`
- `export_obsidian` (line 514) `def export_obsidian(self, target_dir, output_dir)`
- `watch` (line 524) `def watch(self, target_dir)`
- `audit` (line 534) `def audit(self, target_dir)`
- `audit_deep` (line 541) `def audit_deep(self, target_dir)`
- `export_sarif` (line 561) `def export_sarif(self, target_dir, output_path)`
- `export_rules` (line 571) `def export_rules(self, target_dir, output_dir)`
- `detect_layers` (line 581) `def detect_layers(self, target_dir)`
- `lint` (line 591) `def lint(self, target_dir)`
- `strip_dead_code` (line 604) `def strip_dead_code(self, target_dir)`
- `generate_cursorrules` (line 614) `def generate_cursorrules(self, target_dir)`
- `refactor_monolith` (line 629) `def refactor_monolith(self, target_dir)`
- `on_change` (line 528) `def on_change()`

#### `_cache.py`
**Path:** `readmenator/_cache.py`

**Classes:**
- `FileCache` (line 20) `class FileCache` - *SHA256-based cache for incremental file scanning and analysis.

Stores a JSON mapping of relative file paths to their content
hashes inside the project's cache directory. On subsequent runs,
files whose hash matches the cached value are skipped.

Also caches analysis results so that unchanged files reuse
previously-computed security findings, taint paths, etc.*

**Methods:**
- `__init__` (line 31) `def __init__(self, config, project_root)`
- `load` (line 38) `def load(self)`
- `save` (line 49) `def save(self, hashes)`
- `compute_hash` (line 55) `def compute_hash(self, file_path)`
- `compute_hashes` (line 64) `def compute_hashes(self, file_paths)`
- `find_changed` (line 72) `def find_changed(self, file_paths)`
- `prune_deleted` (line 84) `def prune_deleted(self, current_file_ids)`
- `save_analysis` (line 95) `def save_analysis(self, key, data)` - *Save an analysis result to the semantic cache.

Args:
    key: Cache key (e.g. "security", "analysis_v2", "taint").
    data: Serializable analysis data.*
- `load_analysis` (line 118) `def load_analysis(self, key)` - *Load a previously cached analysis result.

Args:
    key: Cache key.

Returns:
    Cached data dict, or None if not found or expired.*
- `clear_analysis` (line 135) `def clear_analysis(self, key)` - *Clear analysis cache, optionally for a specific key only.

Args:
    key: If given, only clears this key. Otherwise clears all.*
- `_prune_analysis_cache` (line 155) `def _prune_analysis_cache(self, current_file_ids)` - *Remove analysis entries for files that no longer exist.*
- `has_changed_since_last_analysis` (line 166) `def has_changed_since_last_analysis(self, file_paths)` - *Check if any file has changed since the last analysis cache.

Returns True if there are no cached hashes (first run) or if
any file hash differs from the cached value.*

#### `_category.py`
**Path:** `readmenator/_category.py`

**Classes:**
- `EdgeKind` (line 24) `class EdgeKind(str, Enum)` - *Semantic type of a morphism between two code artifacts.*
- `Morphism` (line 57) `class Morphism` - *A typed directed edge between two code artifacts.

Attributes:
    source: Node ID of the source artifact.
    target: Node ID of the target artifact.
    kind: Semantic type of the relationship.
    confidence: Confidence score from static analysis (0.0 to 1.0).*
- `Category` (line 78) `class Category` - *A category of code artifacts with typed morphisms.

Objects are node IDs (file paths or symbol identifiers).
Morphisms are typed directed edges. Composition follows
compatible source/target chains respecting edge-kind semantics.*
- `TypedGraph` (line 181) `class TypedGraph` - *Weighted directed graph for PageRank computations.

Converts a Category into a stochastic transition matrix suitable
for eigenvalue computation, preserving edge kind weights.*

**Methods:**
- `build_category_from_edges` (line 236) `def build_category_from_edges(edges, resolved_edges, node_ids)` - *Build a Category from lists of Edge objects.

Maps Edge.relation strings to EdgeKind where possible.
Unrecognised relation strings are mapped to DEPENDS_ON.

Args:
    edges: Raw import edges from the scanner.
    resolved_edges: Optional resolved-import edges.
    node_ids: Optional set of valid node IDs to include.

Returns:
    A populated Category instance.*
- `_infer_edge_kind` (line 280) `def _infer_edge_kind(relation)` - *Map a relation string to an EdgeKind.

Falls back to DEPENDS_ON for unrecognised strings.*
- `__str__` (line 38) `def __str__(self)`
- `weight` (line 73) `def weight(self)` - *Effective weight for ranking = semantic weight * confidence.*
- `__init__` (line 86) `def __init__(self)`
- `add_object` (line 92) `def add_object(self, obj_id)`
- `add_morphism` (line 95) `def add_morphism(self, m)`
- `objects` (line 103) `def objects(self)`
- `morphisms` (line 107) `def morphisms(self)`
- `outgoing` (line 110) `def outgoing(self, obj_id)`
- `incoming` (line 113) `def incoming(self, obj_id)`
- `compose` (line 116) `def compose(self, a, b)` - *Compose two morphisms if target of a matches source of b.

Returns a new Morphism with composite kind, or None if
the kinds are incompatible.*
- `paths` (line 133) `def paths(self, source, target, max_depth)` - *Find all composition paths from source to target up to max_depth.*
- `_compose_kind` (line 157) `def _compose_kind(a, b)` - *Determine the composite edge kind.

Composition rules:
- imports + defines -> defines (reachable definition)
- imports + calls -> calls (reachable call)
- defines + tests -> tests (tested through definition)
- documents + defines -> documents (documented definition)
- Same kind -> same kind.
- Other combinations -> None (incompatible).*
- `__init__` (line 188) `def __init__(self, category)`
- `_compute_out_weights` (line 197) `def _compute_out_weights(self)`
- `nodes` (line 203) `def nodes(self)`
- `size` (line 207) `def size(self)`
- `node_index` (line 210) `def node_index(self, node_id)`
- `transition_weight` (line 213) `def transition_weight(self, source, target)` - *Sum of weights of all morphisms from source to target.*
- `stochastic_row` (line 221) `def stochastic_row(self, source)` - *Return dict of target -> probability for the row of *source*.

Probabilities sum to 1.0 if source has outgoing edges.
Returns empty dict for dangling nodes.*
- `dfs` (line 139) `def dfs(current, goal, path, depth)`

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
control-flow edges (calls), data-flow edges (imports), inheritance
relationships, and security findings (with MITRE ATT&CK mappings)
into a single machine-readable document. Designed to be embedded in
KNOWLEDGE_BASE.md for zero-token agent context.*

**Methods:**
- `__init__` (line 20) `def __init__(self, privacy_mode, cpg_context)`
- `generate` (line 24) `def generate(self, nodes, edges, resolved_edges, analysis, findings)` - *Generate the CPG JSON-LD string embeddable in markdown.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for metadata.
    findings: Optional security findings with MITRE ATT&CK IDs.

Returns:
    Compact JSON-LD string with @context, nodes, edges, analysis,
    and mitre_attack metadata.*
- `_severity_counts` (line 141) `def _severity_counts(self, findings)`
- `_build_symbol_list` (line 147) `def _build_symbol_list(self, node)`
- `_compute_node_hash` (line 163) `def _compute_node_hash(node)`

#### `_cursorrules_generator.py`
**Path:** `readmenator/_cursorrules_generator.py`

**Classes:**
- `CursorRulesGenerator` (line 18) `class CursorRulesGenerator` - *Generates a .cursorrules file from architectural analysis.

Combines base rules, detected layer constraints, and active
linter violations into a deterministic ruleset for AI assistants.*

**Methods:**
- `__init__` (line 25) `def __init__(self, config)`
- `generate` (line 28) `def generate(self, nodes, edges, analysis, layers, violations, project_root)` - *Generate the .cursorrules content string.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    analysis: Optional analysis results.
    layers: Optional layer mapping.
    violations: Optional linter violations.
    project_root: Optional project root for file output.

Returns:
    The generated .cursorrules content as a string.*
- `_build_base_rules` (line 63) `def _build_base_rules(self)`
- `_extract_layer_constraints` (line 81) `def _extract_layer_constraints(self, layers)`
- `_extract_analysis_constraints` (line 92) `def _extract_analysis_constraints(self, analysis)`
- `_extract_violation_rules` (line 107) `def _extract_violation_rules(self, violations)`
- `_write_file` (line 115) `def _write_file(self, project_root, content)`

#### `_dead_code.py`
**Path:** `readmenator/_dead_code.py`

**Classes:**
- `DeadCodeStripper` (line 17) `class DeadCodeStripper` - *Identifies dead code symbols in the knowledge graph.

Builds an in-degree map from resolved import edges, then flags
symbols that are never imported by any other file. Known entry
points are excluded from the dead code report.*

**Methods:**
- `__init__` (line 25) `def __init__(self, config)`
- `identify` (line 28) `def identify(self, nodes, edges, resolved_edges)` - *Identify dead code symbols with zero in-degree.

Args:
    nodes: Scanned file nodes with symbols.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.

Returns:
    List of DeadCodeReport instances for orphaned symbols.*
- `_build_in_degree_map` (line 64) `def _build_in_degree_map(self, nodes, resolved_edges)` - *Build in-degree count for each symbol name.*
- `_classify_recommendation` (line 88) `def _classify_recommendation(self, symbol)` - *Classify the recommended action for a dead symbol.*

#### `_documentation.py`
**Path:** `readmenator/_documentation.py`

**Classes:**
- `DocumentationGenerator` (line 27) `class DocumentationGenerator` - *Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

Delegates graph rendering to MermaidRenderer and handles the
Markdown layout: header metadata, Mermaid block, statistics dashboard,
god nodes, community analysis, surprising connections, architecture
layers, security audit, taint analysis, hotspots, dependency cycles,
change impact, architecture violations, suggested rules, CPG block,
ranking metadata, orphans, query recipes, and per-language architecture
sections with pluralised symbol kind headings.*

**Methods:**
- `__init__` (line 39) `def __init__(self, config)`
- `_ranking_version` (line 57) `def _ranking_version(self)`
- `_get_git_commit` (line 75) `def _get_git_commit()`
- `generate` (line 85) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)`
- `_apply_context_budget` (line 158) `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)`
- `_build_toc` (line 296) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)`
- `_build_layers` (line 381) `def _build_layers(self, layers, nodes)`
- `_build_dashboard` (line 415) `def _build_dashboard(self, nodes, edges, resolved_edges)`
- `_build_god_nodes` (line 495) `def _build_god_nodes(self, analysis, ranked)`
- `_build_community_analysis` (line 523) `def _build_community_analysis(self, analysis, nodes)`
- `_build_surprising_connections` (line 556) `def _build_surprising_connections(self, analysis, nodes)`
- `_build_suggested_questions` (line 581) `def _build_suggested_questions(self, analysis)`
- `_build_ranked_context` (line 597) `def _build_ranked_context(self, ranked)`
- `_build_orphans` (line 643) `def _build_orphans(self, nodes, analysis_v2, ranked)` - *Build a section listing nodes with low coverage signals.*
- `_build_query_recipes` (line 693) `def _build_query_recipes(self)`
- `_build_taint_analysis` (line 735) `def _build_taint_analysis(self, analysis_v2)`
- `_build_hotspots` (line 770) `def _build_hotspots(self, analysis_v2, ranked)`
- `_build_dependency_cycles` (line 808) `def _build_dependency_cycles(self, analysis_v2)`
- `_build_change_impact` (line 828) `def _build_change_impact(self, analysis_v2)`
- `_build_layer_violations` (line 853) `def _build_layer_violations(self, analysis_v2)`
- `_build_suggested_rules` (line 881) `def _build_suggested_rules(self, analysis_v2)`
- `_build_security_findings` (line 906) `def _build_security_findings(self, findings)`
- `_build_mermaid_section` (line 953) `def _build_mermaid_section(self, graph_output, is_truncated)`
- `_build_uml_diagram` (line 976) `def _build_uml_diagram(self, nodes, edges)`
- `_build_cpg_block` (line 1002) `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
- `_build_architecture_reference` (line 1028) `def _build_architecture_reference(self, nodes, edges)`

#### `_explain.py`
**Path:** `readmenator/_explain.py`

**Functions:**
- `explain_rank` (line 16) `def explain_rank(node_id, ranked, category)` - *Return a detailed breakdown of why *node_id* has its rank.

Includes score decomposition, seed paths, and quality signals.

Args:
    node_id: The node to explain.
    ranked: The RankedResult containing scores.
    category: Optional Category for enriched path details.

Returns:
    Formatted explanation string, or None if node_id not found.*
- `rank_summary` (line 140) `def rank_summary(ranked, top_n)` - *Return a short summary of the top-N ranked results.*
- `_find_item` (line 163) `def _find_item(node_id, items)`

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
- `to_cypher` (line 712) `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)` - *Export the graph as native Cypher CREATE statements.

Generates Neo4j/Memgraph-compatible Cypher for direct graph
database ingestion. Each file node becomes a ``(:File)`` node,
import dependencies become ``(:File)-[:IMPORTS]->(:File)``
relationships. Optional security findings are attached as node
properties and standalone ``(:SecurityFinding)`` nodes.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community metadata.
    findings: Optional security finding nodes.

Returns:
    String of Cypher CREATE statements.*
- `to_obsidian` (line 817) `def to_obsidian(self, nodes, edges, output_dir, analysis)` - *Export the graph as an Obsidian vault with wikilinks.

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

#### `_linter.py`
**Path:** `readmenator/_linter.py`

**Classes:**
- `ArchitectureLinter` (line 18) `class ArchitectureLinter` - *Enforces architectural rules over scanned nodes and edges.

Checks file length, cross-layer import violations, and circular
dependencies. Returns structured LinterViolation instances for
each detected issue.*

**Methods:**
- `__init__` (line 31) `def __init__(self, config)`
- `lint` (line 34) `def lint(self, nodes, edges, resolved_edges, layers, content_map)` - *Run all linter rules and return violations.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    layers: Optional mapping from node_id to layer name.
    content_map: Optional mapping from node_id to file content.

Returns:
    List of LinterViolation instances sorted by severity.*
- `_check_file_length` (line 65) `def _check_file_length(self, nodes, content_map)` - *Check files against maximum line count threshold.*
- `_check_cross_layer_violations` (line 96) `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)` - *Check for forbidden cross-layer imports.*
- `_check_circular_dependencies` (line 127) `def _check_circular_dependencies(self, nodes, resolved_edges)` - *Check for circular dependencies in the resolved import graph.*
- `_dfs` (line 146) `def _dfs(current)`

#### `_mcp_server.py`
**Path:** `readmenator/_mcp_server.py`

**Classes:**
- `MCPError` (line 58) `class MCPError(Exception)`
- `MCPRequest` (line 71) `class MCPRequest`
- `MCPTool` (line 92) `class MCPTool`
- `MCPResource` (line 119) `class MCPResource`
- `MCPServer` (line 146) `class MCPServer`

**Methods:**
- `main` (line 796) `def main()` - *CLI entry point for `readmenator serve <path>`.*
- `__init__` (line 59) `def __init__(self, code, message, data)`
- `__init__` (line 72) `def __init__(self, msg)`
- `is_notification` (line 79) `def is_notification(self)`
- `response` (line 82) `def response(self, result)`
- `error` (line 85) `def error(self, code, message, data)`
- `__init__` (line 93) `def __init__(self, name, description, handler, input_schema)`
- `definition` (line 108) `def definition(self)`
- `call` (line 115) `def call(self, arguments)`
- `__init__` (line 120) `def __init__(self, uri, name, description, mime_type, handler)`
- `definition` (line 134) `def definition(self)`
- `read` (line 142) `def read(self)`
- `__init__` (line 147) `def __init__(self, app, target_dir)`
- `register_tool` (line 155) `def register_tool(self, tool)`
- `register_resource` (line 158) `def register_resource(self, resource)`
- `_ensure_kb` (line 161) `def _ensure_kb(self)`
- `_handle_initialize` (line 173) `def _handle_initialize(self, req)`
- `_handle_list_tools` (line 187) `def _handle_list_tools(self, req)`
- `_handle_call_tool` (line 192) `def _handle_call_tool(self, req)`
- `_handle_list_resources` (line 214) `def _handle_list_resources(self, req)`
- `_handle_read_resource` (line 219) `def _handle_read_resource(self, req)`
- `dispatch` (line 241) `def dispatch(self, req)`
- `run` (line 261) `def run(self)`
- `_register_all` (line 285) `def _register_all(self)`
- `_scan` (line 467) `def _scan(self)`
- `_scan_deep` (line 473) `def _scan_deep(self)`
- `_tool_summary` (line 481) `def _tool_summary(self)`
- `_tool_query` (line 519) `def _tool_query(self, text)`
- `_tool_explain` (line 524) `def _tool_explain(self, name)`
- `_tool_path` (line 536) `def _tool_path(self, symbol_a, symbol_b)`
- `_tool_findings` (line 547) `def _tool_findings(self, min_severity)`
- `_tool_security_summary` (line 577) `def _tool_security_summary(self)`
- `_tool_taint` (line 582) `def _tool_taint(self)`
- `_tool_hotspots` (line 603) `def _tool_hotspots(self, top_n)`
- `_tool_cycles` (line 619) `def _tool_cycles(self)`
- `_tool_communities` (line 630) `def _tool_communities(self)`
- `_tool_layers` (line 645) `def _tool_layers(self)`
- `_tool_layer_violations` (line 663) `def _tool_layer_violations(self)`
- `_tool_rebuild` (line 679) `def _tool_rebuild(self)`
- `_tool_update` (line 689) `def _tool_update(self)`
- `_tool_export_json` (line 697) `def _tool_export_json(self)`
- `_resource_summary` (line 705) `def _resource_summary(self)`
- `_resource_graph` (line 722) `def _resource_graph(self)`
- `_resource_findings` (line 741) `def _resource_findings(self)`
- `_resource_analysis` (line 757) `def _resource_analysis(self)`
- `_resource_kb` (line 787) `def _resource_kb(self)`
- `_get_query_engine` (line 791) `def _get_query_engine(self, nodes, edges, resolved)`

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
- `Symbol` (line 18) `class Symbol` - *A single code symbol extracted from a source file.

Attributes:
    name: Identifier of the symbol (class name, function name, etc.).
    kind: Semantic type (class, function, struct, enum, ...).
    line: One-based line number where the symbol is defined.
    doc: Optional docstring or comment extracted from the source.
    signature: Optional method or function signature snippet.*
- `Node` (line 37) `class Node` - *A file node in the knowledge graph, containing its symbols.

Attributes:
    node_id: Relative path of the file used as a unique identifier.
    label: Base file name for display purposes.
    kind: Type of node (typically "module").
    language: Programming language derived from the file extension.
    doc: Optional file-level documentation string.
    symbols: List of Symbol instances defined in this file.*
- `Edge` (line 58) `class Edge` - *A directed relationship between two nodes in the knowledge graph.

Attributes:
    source: Node ID of the source (dependent) file.
    target: Node ID of the target (dependency) file or module.
    relation: Semantic relation label (e.g. "imports", "resolved_imports").
    confidence: Confidence tier ("EXTRACTED" for structural, "INFERRED" for heuristic).
    kind: Optional typed edge kind for ranking-aware computations.*
- `SecurityFinding` (line 77) `class SecurityFinding` - *A security-relevant pattern detected in a source file.

Attributes:
    file_path: Relative path of the file containing the finding.
    line: One-based line number where the pattern was found.
    severity: Severity level (critical, high, medium, low, info).
    rule_id: Unique identifier for the detection rule (e.g. "PY001").
    description: Human-readable explanation of the issue.
    snippet: The offending source code line.
    cwe: CWE identifier string (e.g. "CWE-78").
    mitre_attack: MITRE ATT&CK technique ID (e.g. "T1059.001").*
- `CommunityResult` (line 111) `class CommunityResult` - *Result of community detection on the import graph.

Attributes:
    community_id: Integer identifier of the community.
    label: Human-readable name for the community.
    file_ids: Set of node IDs belonging to this community.
    cohesion: Cohesion score (internal edges / total edges involving community).
    size: Number of files in the community.*
- `AnalysisResult` (line 130) `class AnalysisResult` - *Complete graph analysis output.

Attributes:
    god_nodes: List of (node_id, score) for most central nodes.
    communities: List of CommunityResult instances.
    surprising_connections: List of (source_node, target_node, hops, bridging_communities).
    suggested_questions: List of plain-language exploration questions.
    node_count: Total nodes in the graph.
    edge_count: Total edges in the graph.*
- `TaintPath` (line 151) `class TaintPath` - *A taint propagation path from source to sink through the import graph.

Attributes:
    source_file: The file that introduces the dangerous import.
    sink_file: The file that transitively receives the taint.
    path: List of file node IDs forming the propagation chain.
    hops: Number of hops in the propagation path.
    dangerous_import: The specific dangerous module or function imported.
    severity: Inferred severity of the taint path.*
- `TaintAnalysisResult` (line 172) `class TaintAnalysisResult` - *Complete taint propagation analysis output.

Attributes:
    paths: List of TaintPath instances discovered.
    source_count: Number of unique taint source files.
    sink_count: Number of unique taint sink files.*
- `DependencyCycle` (line 187) `class DependencyCycle` - *A cycle detected in the resolved import graph.

Attributes:
    cycle: List of file node IDs forming the cycle.
    length: Number of files in the cycle.*
- `ChangeImpact` (line 200) `class ChangeImpact` - *Change impact analysis for a single file.

Attributes:
    file_id: The file that would be changed.
    direct_dependents: Files that directly import this file.
    transitive_dependents: Files that transitively depend on this file.
    total_impact: Total number of affected files (direct + transitive).*
- `HotspotResult` (line 217) `class HotspotResult` - *A hotspot file combining complexity and centrality metrics.

Attributes:
    file_id: The file node ID.
    complexity_score: Normalised symbol count score (0-1).
    centrality_score: Normalised god node score (0-1).
    combined_score: Weighted combination of complexity and centrality.
    symbol_count: Raw symbol count.
    connection_count: Raw connection count.*
- `SuggestedRule` (line 238) `class SuggestedRule` - *A suggested linting/security rule derived from code patterns.

Attributes:
    rule_id: Suggested rule identifier (e.g. "RM001").
    severity: Suggested severity (info, warning, error).
    description: Human-readable description of the pattern.
    pattern: The detected pattern or code snippet.
    file_examples: Example file paths where the pattern was found.
    match_count: Number of times the pattern was matched.
    language: Target language for the rule.
    semgrep_yaml: Optional Semgrep rule YAML string.*
- `LayerViolation` (line 263) `class LayerViolation` - *A detected architectural layer violation.

Attributes:
    source_file: The file causing the violation.
    source_layer: The layer of the source file.
    target_file: The file being imported.
    target_layer: The layer of the target file.
    description: Description of the violation.
    severity: Severity (strict, warn, info).*
- `AnalysisResultV2` (line 284) `class AnalysisResultV2` - *Extended analysis result combining all new analysis modules.

Attributes:
    taint: Optional taint analysis result.
    cycles: List of dependency cycles.
    change_impacts: List of change impact results for key files.
    hotspots: List of hotspot results.
    suggested_rules: List of suggested linting rules.
    layer_violations: List of layer violations.*
- `LinterViolation` (line 305) `class LinterViolation` - *A violation detected by the architecture linter.

Attributes:
    file_path: Relative path of the file containing the violation.
    rule_id: Unique identifier for the linter rule (e.g. "ARC001").
    severity: Severity level (error, warning, info).
    message: Human-readable description of the violation.*
- `DeadCodeReport` (line 322) `class DeadCodeReport` - *A dead code symbol identified by the stripper.

Attributes:
    file_path: Relative path of the file containing the symbol.
    symbol_name: Name of the dead symbol.
    symbol_type: Type of symbol (function, class, method, etc.).
    recommendation: Recommended action (MOVE_TO_TRASH, REVIEW, KEEP).*
- `RefactoringAction` (line 339) `class RefactoringAction` - *A single refactoring action within a plan.

Attributes:
    action_type: Type of action (EXTRACT_CLASS, EXTRACT_FUNCTION, MOVE_SYMBOL).
    source_file: The file to refactor.
    start_line: Start line of the code range to extract.
    end_line: End line of the code range to extract.
    target_file: The new file to create (for EXTRACT actions).
    description: Human-readable description of the action.*
- `RefactoringPlan` (line 360) `class RefactoringPlan` - *A complete refactoring plan for a monolithic file.

Attributes:
    file_path: The file to refactor.
    actions: List of refactoring actions to perform.
    estimated_impact: Number of files affected by the refactoring.
    current_lines: Current line count of the file.*

**Methods:**
- `pluralize_symbol_kind` (line 101) `def pluralize_symbol_kind(kind, plural_map)` - *Return the plural form of *kind* according to *plural_map*.

Falls back to appending ``"s"`` when the kind is not found.
This prevents obvious misspellings like ``"Classs"``.*

#### `_pipeline.py`
**Path:** `readmenator/_pipeline.py`

**Classes:**
- `AnalyzerFactory` (line 36) `class AnalyzerFactory` - *Lazy factory for all readmenator analyzer and generator instances.

Decouples the application orchestrator from the concrete
instantiation of analysis modules. Each component is created
on first access and cached for the lifetime of the factory.*
- `DeepAnalysisRunner` (line 187) `class DeepAnalysisRunner` - *Orchestrates the extended V2 analysis pipeline.

Runs taint propagation, hotspot detection, cycle detection,
change impact, layer violations, and rule generation as a
coordinated batch. Isolated from the main app to reduce
coupling in the primary orchestration layer.*

**Methods:**
- `__init__` (line 44) `def __init__(self, config)`
- `scanner` (line 64) `def scanner(self)`
- `generator` (line 70) `def generator(self)`
- `analyzer` (line 76) `def analyzer(self)`
- `security` (line 82) `def security(self)`
- `exporter` (line 88) `def exporter(self)`
- `taint` (line 94) `def taint(self)`
- `hotspots` (line 100) `def hotspots(self)`
- `layer_rules` (line 106) `def layer_rules(self)`
- `rule_gen` (line 112) `def rule_gen(self)`
- `sarif` (line 118) `def sarif(self)`
- `cpg` (line 124) `def cpg(self)`
- `layer_detector` (line 133) `def layer_detector(self)`
- `uml` (line 139) `def uml(self)`
- `readme_injector` (line 145) `def readme_injector(self)`
- `build_typed_graph` (line 152) `def build_typed_graph(self, nodes, edges, resolved_edges)`
- `make_ranker` (line 162) `def make_ranker(self, typed_graph)` - *Create a CompositeRanker for the given typed graph.*
- `last_category` (line 179) `def last_category(self)`
- `last_typed_graph` (line 183) `def last_typed_graph(self)`
- `__init__` (line 196) `def __init__(self, factory)`
- `run` (line 199) `def run(self, nodes, edges, resolved_edges, layers, content_map)`

#### `_projections.py`
**Path:** `readmenator/_projections.py`

**Classes:**
- `Projection` (line 17) `class Projection(Protocol)` - *A functor from C_code to another category.

Maps nodes and morphisms while preserving composition structure.*
- `IdentityProjection` (line 32) `class IdentityProjection` - *Identity functor: maps everything to itself.*
- `DocProjection` (line 42) `class DocProjection` - *F_docs: project code to documentation.

Keeps only nodes that have docstrings or are referenced in README.
Useful for quantifying documentation gaps.*
- `RiskProjection` (line 63) `class RiskProjection` - *F_risk: project code to risk/fragility nodes.

Nodes are transformed with risk attributes: fan-in, fan-out,
symbol count, test absence, and public API exposure.*

**Methods:**
- `apply_view` (line 95) `def apply_view(category, view_config)` - *Apply a named view to produce a projected category.

View config format::
    {
        "edge_types": [EdgeKind.IMPORTS, EdgeKind.DEFINES, ...],
        "direction": "forward" | "reverse",  # default "forward"
    }

Args:
    category: Source category.
    view_config: View definition dict.

Returns:
    A new Category with only matching morphisms.*
- `map_node` (line 23) `def map_node(self, node)` - *Map a code node. Return None to exclude.*
- `map_morphism` (line 27) `def map_morphism(self, m)` - *Map a morphism. Return None to exclude.*
- `map_node` (line 35) `def map_node(self, node)`
- `map_morphism` (line 38) `def map_morphism(self, m)`
- `__init__` (line 49) `def __init__(self, documented_ids)`
- `map_node` (line 52) `def map_node(self, node)`
- `map_morphism` (line 57) `def map_morphism(self, m)`
- `__init__` (line 70) `def __init__(self, fan_in, fan_out, test_files)`
- `map_node` (line 80) `def map_node(self, node)`
- `map_morphism` (line 91) `def map_morphism(self, m)`

#### `_query.py`
**Path:** `readmenator/_query.py`

**Classes:**
- `QueryEngine` (line 25) `class QueryEngine` - *In-memory query engine over the scanned knowledge graph.

Builds a symbol-name index and an import-adjacency graph on
construction. Provides exact and fuzzy symbol lookup, detailed
explanation output, BFS shortest-path resolution, free-text
search, and a summary report.*

**Methods:**
- `__init__` (line 34) `def __init__(self, nodes, edges, resolved_edges, ranker, config)` - *Initialise internal indexes from scanned data.

Args:
    nodes: List of scanned file nodes.
    edges: List of import-relationship edges.
    resolved_edges: Optional resolved-import edges (both
        source and target are project file IDs).
    ranker: Optional CompositeRanker for ranked queries.
    config: Optional RankConfig if ranker is not provided.*
- `_init_default_ranker` (line 64) `def _init_default_ranker(self)` - *Build a default CompositeRanker from the loaded data.*
- `ranked_query` (line 73) `def ranked_query(self, query, top_n)` - *Answer *query* with a ranked list of relevant nodes.

Uses Personalized PageRank seeded from lexical matches
against the query text, combined with authority, test
coverage, doc coverage, and freshness signals.

Args:
    query: Free-text query string.
    top_n: Number of results to return (default: RankConfig.top_n).

Returns:
    A RankedResult with scored items and explanations.*
- `_estimate_test_coverage` (line 124) `def _estimate_test_coverage(self)` - *Estimate test coverage per file.

A file is considered 'tested' if a test file imports it.
Returns fraction of symbols referenced across test files.*
- `_estimate_doc_coverage` (line 150) `def _estimate_doc_coverage(self)` - *Estimate documentation coverage per file.

A file has doc coverage if it has a file-level docstring or
any of its symbols have docstrings.*
- `_build_symbol_index` (line 170) `def _build_symbol_index(self)` - *Build a name-to-list-of-(node, symbol) lookup.

Returns:
    Dict mapping symbol names to list of (Node, Symbol) tuples.*
- `_build_import_graph` (line 184) `def _build_import_graph(self)` - *Build an adjacency map from import edges.

Returns:
    Dict mapping each file node_id to its set of import targets.*
- `_build_resolved_graph` (line 200) `def _build_resolved_graph(self)` - *Build an adjacency map from resolved import edges.

Only contains edges where both source and target are
project files (not external modules).

Returns:
    Dict mapping each file node_id to files it imports within the project.*
- `find_symbol` (line 220) `def find_symbol(self, name)` - *Look up *name* by exact match, then by substring fuzzy match.

Returns:
    A list of (Node, Symbol) tuples, or ``None`` if not found.*
- `explain` (line 238) `def explain(self, name)` - *Return a detailed multi-line explanation of *name*.

Includes kind, file path, line number, docstring, signature,
imports, reverse dependencies ("imported by"), and sibling
symbols in the same file.

Returns:
    Formatted string or ``None`` if the symbol is not found.*
- `_find_incoming_imports` (line 277) `def _find_incoming_imports(self, target)` - *List all node IDs that import *target*.*
- `find_path` (line 285) `def find_path(self, symbol_a, symbol_b)` - *Find the shortest import path from *symbol_a* to *symbol_b*.

Uses BFS on the resolved import graph (project-internal edges)
first, traversing in both directions (forward = A imports B,
reverse = B is imported by A). Falls back to the raw import
graph if no resolved path exists.

Returns:
    List of file node IDs forming the dependency chain, or ``None``.*
- `_make_bidirectional` (line 315) `def _make_bidirectional(graph)` - *Convert a directed graph to a bidirectional one.

For each edge A→B, adds both A→B and B→A edges.*
- `_bfs_shortest_path` (line 331) `def _bfs_shortest_path(self, graph, start, goal)` - *Run BFS to find the shortest path from *start* to *goal*.

Returns:
    List of node IDs or ``None`` if no path exists.*
- `query` (line 355) `def query(self, question)` - *Free-text search over symbols and file paths.

Tokenises the input, matches against symbol names (substring)
and then against file paths as a fallback. Returns a
human-readable result string summarising matches or a
no-results message with KB statistics.*
- `summary` (line 411) `def summary(self)` - *Return a concise overview of the loaded knowledge base.

Reports file count, symbol count, import count, language
diversity, top-level modules (by import popularity), and
lists of key class-like and function-like symbols.*

#### `_rank.py`
**Path:** `readmenator/_rank.py`

**Classes:**
- `RankConfig` (line 32) `class RankConfig` - *Tuneable parameters for the ranking system.

Attributes:
    alpha: Damping factor for PageRank (default 0.85).
    max_iter: Maximum power-iteration steps.
    tolerance: Convergence threshold (L1 norm).
    top_n: Default number of ranked results to return.
    noise_penalty: Multiplier applied to hub-penalty names
        when they are not part of the query seeds.
    composite_ppr_weight: Weight for PPR in composite score.
    composite_authority_weight: Weight for global PageRank.
    composite_test_weight: Weight for test coverage signal.
    composite_doc_weight: Weight for documentation coverage.
    composite_freshness_weight: Weight for code freshness.*
- `RankedItem` (line 320) `class RankedItem` - *A single ranked result with score decomposition.

Attributes:
    node_id: The ranked node ID.
    composite_score: Final multi-signal score.
    ppr_score: Personalized PageRank contribution.
    authority_score: Global PageRank contribution.
    test_coverage: Fraction of symbols referenced in test files.
    doc_coverage: Fraction of symbols with documentation.
    freshness: Decay-weighted recency signal.
    justification_paths: Shortest paths from seed nodes to this node.*
- `RankedResult` (line 349) `class RankedResult` - *Complete ranking result for a query or context.

Attributes:
    query: The query string or context label.
    items: Ranked items in descending score order.
    config: The RankConfig used.
    seed_nodes: The seed node IDs used for PPR.
    model_version: Version identifier for the ranking model.*
- `CompositeRanker` (line 377) `class CompositeRanker` - *Combines PPR, authority, test/doc coverage, and freshness.

Produces a single composite score per node:
S_q(n) = w_ppr * PPR_q(n) + w_auth * Auth(n) + w_test * Test(n)
       + w_doc * Doc(n) + w_fresh * Fresh(n)*

**Methods:**
- `global_pagerank` (line 61) `def global_pagerank(graph, alpha, max_iter, tolerance)` - *Compute global PageRank on the typed weighted graph.

Uses power iteration on the stochastic matrix derived from
the TypedGraph's edge weights. Dangling nodes (no outgoing
edges) are handled by uniform random teleportation.

Args:
    graph: A TypedGraph instance with weighted edges.
    alpha: Damping factor (probability of following an edge).
    max_iter: Maximum power-iteration steps.
    tolerance: Convergence threshold (L1 norm).

Returns:
    Dict mapping node_id -> PageRank score. Scores sum to 1.0.*
- `personalized_pagerank` (line 119) `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` - *Compute Personalized PageRank with a seed-node preference vector.

Instead of uniform teleportation, probability mass is distributed
according to the seed vector. This makes the ranking sensitive to
a specific query or context.

Args:
    graph: A TypedGraph instance.
    seeds: Dict mapping seed node_id -> preference mass (sums to 1.0).
    alpha: Damping factor.
    max_iter: Maximum power-iteration steps.
    tolerance: Convergence threshold (L1 norm).

Returns:
    Dict mapping node_id -> PPR score. Scores sum to 1.0.*
- `hits` (line 189) `def hits(graph, max_iter, tolerance)` - *Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.

Authorities are nodes with many incoming edges from good hubs.
Hubs are nodes with many outgoing edges to good authorities.

Returns:
    Tuple of (authorities, hubs) as dicts mapping node_id -> score.
    Scores are L2-normalised.*
- `build_seeds_from_query` (line 240) `def build_seeds_from_query(query, node_ids, node_labels, symbols)` - *Build a PPR seed vector from a natural-language query string.

Matches query tokens against node IDs, labels, and symbol names.
Seeds are assigned equal mass. If no match is found, returns
empty dict (will use uniform teleportation).

Args:
    query: Free-text query string.
    node_ids: All valid node IDs.
    node_labels: Mapping from node_id -> display label.
    symbols: Mapping from node_id -> list of symbol names.

Returns:
    Dict of seed node_id -> equal mass fraction.*
- `build_seeds_for_context` (line 286) `def build_seeds_for_context(node_ids, anchor_patterns)` - *Build a PPR seed vector from anchor pattern strings.

Nodes whose ID or label contains any anchor pattern receive
equal seed mass. Useful for section-level seeding.

Args:
    node_ids: All valid node IDs.
    anchor_patterns: List of substrings to match.

Returns:
    Dict of seed node_id -> equal mass fraction.*
- `_format_explanation` (line 512) `def _format_explanation(item, result)` - *Format a human-readable explanation for a ranked item.*
- `label` (line 344) `def label(self)`
- `top` (line 366) `def top(self, n)`
- `explain` (line 369) `def explain(self, node_id)` - *Return a human-readable explanation of why *node_id* ranks as it does.*
- `__init__` (line 385) `def __init__(self, graph, config)`
- `_get_global_pr` (line 394) `def _get_global_pr(self)`
- `rank` (line 404) `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` - *Compute composite ranking for a query.

Args:
    query: Query string.
    seeds: PPR seed vector.
    category: Category with morphisms for path finding.
    node_ids: All valid node IDs.
    test_coverage: Optional dict of node_id -> test coverage (0-1).
    doc_coverage: Optional dict of node_id -> doc coverage (0-1).
    freshness: Optional dict of node_id -> freshness (0-1).

Returns:
    A RankedResult with scored and sorted items.*
- `_find_justification_paths` (line 486) `def _find_justification_paths(self, target, seed_ids, category, max_paths)` - *Find shortest paths from any seed to target.*

#### `_readme_injector.py`
**Path:** `readmenator/_readme_injector.py`

**Classes:**
- `ReadmeInjector` (line 49) `class ReadmeInjector` - *Injects a link to KNOWLEDGE_BASE.md into the project README.

Detects the project's README file, checks if injection is already
present, and appends a descriptive section about the knowledge base
so that both human developers and AI agents know it exists.*

**Methods:**
- `__init__` (line 57) `def __init__(self, kb_filename)`
- `inject` (line 60) `def inject(self, project_root)`
- `remove` (line 82) `def remove(self, project_root)`
- `_find_readme` (line 111) `def _find_readme(root)`
- `_build_injection` (line 118) `def _build_injection(self, suffix)`

#### `_refactorizer.py`
**Path:** `readmenator/_refactorizer.py`

**Classes:**
- `MonolithRefactorizer` (line 24) `class MonolithRefactorizer` - *Generates refactoring plans for monolithic files.

Analyzes files exceeding the line threshold, extracts symbol
boundaries, detects cohesive clusters via import analysis, and
produces structured refactoring plans without auto-execution.*

**Methods:**
- `__init__` (line 32) `def __init__(self, config)`
- `analyze` (line 35) `def analyze(self, nodes, edges, resolved_edges, content_map)` - *Identify monolithic files and generate refactoring plans.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    content_map: Optional mapping from node_id to file content.

Returns:
    List of RefactoringPlan instances for files needing refactoring.*
- `_get_line_count` (line 70) `def _get_line_count(self, file_id, content_map)`
- `_plan_refactoring` (line 82) `def _plan_refactoring(self, node, edges, resolved_edges, content_map)`
- `_group_symbols_by_kind` (line 126) `def _group_symbols_by_kind(self, symbols)`
- `_suggest_target_file` (line 132) `def _suggest_target_file(self, source_file, kind)`
- `_estimate_impact` (line 147) `def _estimate_impact(self, file_id, resolved_edges)`
- `generate_script` (line 156) `def generate_script(self, plan, project_root)`

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
- `SecurityRule` (line 24) `class SecurityRule` - *A single security detection rule loaded from YAML or built-in.

Attributes:
    rule_id: Unique identifier (e.g. "PY001").
    severity: Severity level (critical, high, medium, low, info).
    description: Human-readable description of the issue.
    pattern: Compiled regex to search for.
    cwe: CWE identifier string.
    mitre_attack: MITRE ATT&CK technique ID (e.g. "T1059.001").*
- `SecurityAnalyzer` (line 486) `class SecurityAnalyzer` - *Pattern-based static security scanner.

Loads rules from the external YAML rules file when available,
falling back to the built-in hardcoded rule sets. Walks the
target directory applying rules to every supported source file.*

**Methods:**
- `_parse_minimal_yaml` (line 46) `def _parse_minimal_yaml(text)` - *Parse the simplified YAML format used by _security_rules.yml.

Only supports:
  - top-level ``rules:`` key
  - list items starting with ``  - rule_id:``
  - scalar key: value pairs (quoted or unquoted)
  - block list items: ``    - "value"``
  - inline lists: ``key: [item1, item2]``
  - ``#`` comments

Returns a list of rule dicts.*
- `_unquote` (line 121) `def _unquote(s)`
- `_load_rules_from_yaml` (line 128) `def _load_rules_from_yaml(yaml_path)` - *Load rule dicts from the YAML rules file, or return None on failure.*
- `_compile` (line 148) `def _compile()`
- `_python_rules` (line 153) `def _python_rules()`
- `_javascript_rules` (line 182) `def _javascript_rules()`
- `_c_rules` (line 201) `def _c_rules()`
- `_java_rules` (line 222) `def _java_rules()`
- `_go_rules` (line 237) `def _go_rules()`
- `_ruby_rules` (line 250) `def _ruby_rules()`
- `_php_rules` (line 267) `def _php_rules()`
- `_shell_rules` (line 284) `def _shell_rules()`
- `_csharp_rules` (line 297) `def _csharp_rules()`
- `_kotlin_rules` (line 310) `def _kotlin_rules()`
- `_swift_rules` (line 321) `def _swift_rules()`
- `_scala_rules` (line 332) `def _scala_rules()`
- `_lua_rules` (line 343) `def _lua_rules()`
- `_dart_rules` (line 354) `def _dart_rules()`
- `_rust_rules` (line 365) `def _rust_rules()`
- `_nim_rules` (line 376) `def _nim_rules()`
- `_gdscript_rules` (line 387) `def _gdscript_rules()`
- `_elixir_rules` (line 398) `def _elixir_rules()`
- `_build_rules_from_yaml` (line 447) `def _build_rules_from_yaml(yaml_path)` - *Attempt to build the rule map from the YAML rules file.

Returns None if the YAML file cannot be loaded or parsed, allowing
the caller to fall back to built-in rules.*
- `__init__` (line 496) `def __init__(self, config)`
- `_resolve_rules` (line 500) `def _resolve_rules(self)` - *Resolve rules: prefer YAML, fall back to built-in.*
- `_meets_threshold` (line 509) `def _meets_threshold(self, severity)`
- `scan` (line 513) `def scan(self, root)`
- `_validate_path` (line 555) `def _validate_path(self, path, root)`
- `summary` (line 572) `def summary(self, findings)`

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

#### `_uml.py`
**Path:** `readmenator/_uml.py`

**Classes:**
- `UmlGenerator` (line 32) `class UmlGenerator`

**Methods:**
- `_get_code_generator` (line 170) `def _get_code_generator(language)`
- `_type_map_py_to_target` (line 188) `def _type_map_py_to_target(target, py_type_hint)`
- `_generate_cpp` (line 231) `def _generate_cpp(class_symbols, nodes, edges)`
- `_cpp_params` (line 257) `def _cpp_params(params)`
- `_generate_java` (line 272) `def _generate_java(class_symbols, nodes, edges)`
- `_java_params` (line 299) `def _java_params(params)`
- `_generate_csharp` (line 314) `def _generate_csharp(class_symbols, nodes, edges)`
- `_cs_params` (line 343) `def _cs_params(params)`
- `_generate_python` (line 358) `def _generate_python(class_symbols, nodes, edges)`
- `_generate_go` (line 393) `def _generate_go(class_symbols, nodes, edges)`
- `_generate_rust` (line 420) `def _generate_rust(class_symbols, nodes, edges)`
- `_generate_php` (line 446) `def _generate_php(class_symbols, nodes, edges)`
- `_generate_kotlin` (line 474) `def _generate_kotlin(class_symbols, nodes, edges)`
- `_generate_scala` (line 494) `def _generate_scala(class_symbols, nodes, edges)`
- `_generate_swift` (line 516) `def _generate_swift(class_symbols, nodes, edges)`
- `_generate_dart` (line 545) `def _generate_dart(class_symbols, nodes, edges)`
- `_generate_ruby` (line 565) `def _generate_ruby(class_symbols, nodes, edges)`
- `_safe_name` (line 586) `def _safe_name(name)`
- `_extract_params` (line 590) `def _extract_params(signature)`
- `__init__` (line 34) `def __init__(self, config)`
- `render_mermaid_class_diagram` (line 37) `def render_mermaid_class_diagram(self, nodes, edges)`
- `generate_code` (line 127) `def generate_code(self, nodes, edges, target_language)`
- `_sanitize_id` (line 151) `def _sanitize_id(raw)`
- `_find_node` (line 163) `def _find_node(nodes, node_id)`

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
- `test_save_and_load_analysis_roundtrip` (line 109) `def test_save_and_load_analysis_roundtrip(self)`
- `test_load_missing_analysis_key_returns_none` (line 116) `def test_load_missing_analysis_key_returns_none(self)`
- `test_clear_analysis_specific_key` (line 120) `def test_clear_analysis_specific_key(self)`
- `test_clear_analysis_all_keys` (line 127) `def test_clear_analysis_all_keys(self)`
- `test_has_changed_since_last_analysis_returns_true_on_first_run` (line 134) `def test_has_changed_since_last_analysis_returns_true_on_first_run(self)`
- `test_has_changed_since_last_analysis_returns_false_when_no_changes` (line 139) `def test_has_changed_since_last_analysis_returns_false_when_no_changes(self)`
- `test_has_changed_since_last_analysis_returns_true_when_file_changed` (line 147) `def test_has_changed_since_last_analysis_returns_true_when_file_changed(self)`

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

#### `test_cursorrules.py`
**Path:** `tests/test_cursorrules.py`

**Classes:**
- `TestCursorRulesGeneratorContract` (line 18) `class TestCursorRulesGeneratorContract(TestCase)` - *Contract: CursorRulesGenerator produces deterministic rulesets.*

**Methods:**
- `setUp` (line 21) `def setUp(self)`
- `test_generate_returns_string` (line 25) `def test_generate_returns_string(self)`
- `test_generate_contains_header` (line 29) `def test_generate_contains_header(self)`
- `test_generate_contains_base_rules` (line 33) `def test_generate_contains_base_rules(self)`
- `test_generate_includes_layer_constraints` (line 38) `def test_generate_includes_layer_constraints(self)`
- `test_generate_includes_god_nodes` (line 49) `def test_generate_includes_god_nodes(self)`
- `test_generate_includes_communities` (line 62) `def test_generate_includes_communities(self)`
- `test_generate_includes_violations` (line 82) `def test_generate_includes_violations(self)`
- `test_generate_limits_violations_to_ten` (line 95) `def test_generate_limits_violations_to_ten(self)`
- `test_generate_writes_file_when_project_root` (line 103) `def test_generate_writes_file_when_project_root(self)`
- `test_generate_idempotent` (line 111) `def test_generate_idempotent(self)`

#### `test_dead_code.py`
**Path:** `tests/test_dead_code.py`

**Classes:**
- `TestDeadCodeStripperContract` (line 16) `class TestDeadCodeStripperContract(TestCase)` - *Contract: DeadCodeStripper identifies orphaned symbols.*

**Methods:**
- `setUp` (line 19) `def setUp(self)`
- `_make_symbol` (line 23) `def _make_symbol(self, name, kind)`
- `_make_node` (line 26) `def _make_node(self, nid, symbols)`
- `_make_edge` (line 35) `def _make_edge(self, src, tgt)`
- `test_identify_empty_graph_returns_empty` (line 38) `def test_identify_empty_graph_returns_empty(self)`
- `test_identify_finds_dead_symbol` (line 42) `def test_identify_finds_dead_symbol(self)`
- `test_identify_excludes_entry_points` (line 53) `def test_identify_excludes_entry_points(self)`
- `test_identify_excludes_app_entry_point` (line 61) `def test_identify_excludes_app_entry_point(self)`
- `test_identify_excludes_init_entry_point` (line 69) `def test_identify_excludes_init_entry_point(self)`
- `test_identify_recommends_review_for_classes` (line 77) `def test_identify_recommends_review_for_classes(self)`
- `test_identify_recommends_trash_for_functions` (line 85) `def test_identify_recommends_trash_for_functions(self)`
- `test_identify_recommends_trash_for_variables` (line 93) `def test_identify_recommends_trash_for_variables(self)`
- `test_all_symbols_imported_returns_empty` (line 101) `def test_all_symbols_imported_returns_empty(self)`
- `test_reports_sorted_by_file_path` (line 113) `def test_reports_sorted_by_file_path(self)`

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
- `test_context_budget_zero_returns_full_content` (line 252) `def test_context_budget_zero_returns_full_content(self)`
- `test_context_budget_returns_compact_summary` (line 260) `def test_context_budget_returns_compact_summary(self)`
- `test_context_budget_prioritizes_god_nodes` (line 268) `def test_context_budget_prioritizes_god_nodes(self)`
- `test_context_budget_truncates_at_limit` (line 285) `def test_context_budget_truncates_at_limit(self)`
- `test_context_budget_includes_security_findings` (line 293) `def test_context_budget_includes_security_findings(self)`

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

#### `test_linter.py`
**Path:** `tests/test_linter.py`

**Classes:**
- `TestArchitectureLinterContract` (line 16) `class TestArchitectureLinterContract(TestCase)` - *Contract: ArchitectureLinter enforces architectural rules.*

**Methods:**
- `setUp` (line 19) `def setUp(self)`
- `_make_node` (line 23) `def _make_node(self, nid, label, lang)`
- `_make_edge` (line 26) `def _make_edge(self, src, tgt, rel)`
- `test_lint_empty_graph_returns_no_violations` (line 29) `def test_lint_empty_graph_returns_no_violations(self)`
- `test_lint_returns_empty_for_files_under_threshold` (line 33) `def test_lint_returns_empty_for_files_under_threshold(self)`
- `test_lint_detects_file_exceeding_max_lines` (line 40) `def test_lint_detects_file_exceeding_max_lines(self)`
- `test_lint_detects_cross_layer_violation` (line 49) `def test_lint_detects_cross_layer_violation(self)`
- `test_lint_allows_same_layer_imports` (line 61) `def test_lint_allows_same_layer_imports(self)`
- `test_lint_allows_testing_to_business_logic` (line 72) `def test_lint_allows_testing_to_business_logic(self)`
- `test_lint_ignores_utility_layer` (line 83) `def test_lint_ignores_utility_layer(self)`
- `test_lint_detects_circular_dependencies` (line 94) `def test_lint_detects_circular_dependencies(self)`
- `test_violations_sorted_by_severity` (line 108) `def test_violations_sorted_by_severity(self)`
- `test_lint_returns_empty_when_disabled` (line 121) `def test_lint_returns_empty_when_disabled(self)`

#### `test_mcp_server.py`
**Path:** `tests/test_mcp_server.py`

**Classes:**
- `TestMCPProtocol` (line 21) `class TestMCPProtocol(TestCase)` - *Contract: MCP server implements JSON-RPC 2.0 over stdio.*

**Methods:**
- `setUp` (line 24) `def setUp(self)`
- `tearDown` (line 33) `def tearDown(self)`
- `_make_request` (line 36) `def _make_request(self, method, params, msg_id)`
- `_call` (line 42) `def _call(self, req)`
- `test_initialize_exchanges_protocol_version` (line 49) `def test_initialize_exchanges_protocol_version(self)`
- `test_notifications_initialized_returns_no_response` (line 62) `def test_notifications_initialized_returns_no_response(self)`
- `test_unknown_method_returns_error` (line 67) `def test_unknown_method_returns_error(self)`
- `test_uninitialized_request_returns_error` (line 75) `def test_uninitialized_request_returns_error(self)`
- `test_list_tools_returns_all_tool_definitions` (line 85) `def test_list_tools_returns_all_tool_definitions(self)`
- `test_call_tool_without_initialize_returns_error` (line 115) `def test_call_tool_without_initialize_returns_error(self)`
- `test_call_tool_unknown_tool_returns_method_not_found` (line 123) `def test_call_tool_unknown_tool_returns_method_not_found(self)`
- `test_call_summary_tool_returns_content` (line 132) `def test_call_summary_tool_returns_content(self)`
- `test_call_query_tool_with_text_returns_results` (line 145) `def test_call_query_tool_with_text_returns_results(self)`
- `test_call_query_tool_missing_required_param_raises` (line 154) `def test_call_query_tool_missing_required_param_raises(self)`
- `test_list_resources_returns_resource_definitions` (line 168) `def test_list_resources_returns_resource_definitions(self)`
- `test_read_resource_summary_returns_json` (line 186) `def test_read_resource_summary_returns_json(self)`
- `test_read_resource_unknown_uri_returns_error` (line 197) `def test_read_resource_unknown_uri_returns_error(self)`
- `test_read_resource_kb_returns_markdown` (line 205) `def test_read_resource_kb_returns_markdown(self)`
- `_get_tool_def` (line 219) `def _get_tool_def(self, name)`
- `test_query_tool_requires_text_param` (line 226) `def test_query_tool_requires_text_param(self)`
- `test_explain_tool_requires_name_param` (line 230) `def test_explain_tool_requires_name_param(self)`
- `test_path_tool_requires_two_params` (line 234) `def test_path_tool_requires_two_params(self)`
- `test_parse_error_for_invalid_json` (line 243) `def test_parse_error_for_invalid_json(self)`
- `test_call_tool_returns_text_content_list` (line 251) `def test_call_tool_returns_text_content_list(self)`

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

#### `test_parsers_property.py`
**Path:** `tests/test_parsers_property.py`

**Classes:**
- `TestParserHypothesisContract` (line 117) `class TestParserHypothesisContract(TestCase)` - *Property-based contract: parsers never crash on arbitrary input.*
- `TestPythonParserProperty` (line 250) `class TestPythonParserProperty(TestCase)` - *Property-based tests specific to the Python parser (native ast).*

**Functions:**
- `_generate_multiline_code` (line 67) `def _generate_multiline_code(lines, line_strategy)` - *Generate source code with a configurable number of lines.*
- `_create_parser` (line 104) `def _create_parser(ext)` - *Create a parser for the given extension.*

**Methods:**
- `test_never_crashes_on_malformed_code` (line 124) `def test_never_crashes_on_malformed_code(self, ext, code)`
- `test_never_crashes_on_unicode_code` (line 142) `def test_never_crashes_on_unicode_code(self, ext, code)`
- `test_empty_code_returns_empty_or_valid` (line 160) `def test_empty_code_returns_empty_or_valid(self, ext)`
- `test_whitespace_code_returns_empty_or_valid` (line 170) `def test_whitespace_code_returns_empty_or_valid(self, ext)`
- `test_never_crashes_on_many_lines` (line 182) `def test_never_crashes_on_many_lines(self, ext, lines)`
- `test_repeated_keywords_no_crash` (line 200) `def test_repeated_keywords_no_crash(self, ext)`
- `test_parser_imports_is_list_of_strings` (line 219) `def test_parser_imports_is_list_of_strings(self, ext)`
- `test_unknown_extension_returns_none` (line 231) `def test_unknown_extension_returns_none(self)`
- `_assert_valid_symbols` (line 237) `def _assert_valid_symbols(self, symbols)`
- `setUp` (line 253) `def setUp(self)`
- `test_python_never_crashes_on_weird_ascii` (line 258) `def test_python_never_crashes_on_weird_ascii(self, code)`
- `test_python_never_crashes_on_any_text` (line 272) `def test_python_never_crashes_on_any_text(self, code)`

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

#### `test_ranking.py`
**Path:** `tests/test_ranking.py`

**Classes:**
- `TestEdgeKind` (line 60) `class TestEdgeKind`
- `TestMorphism` (line 84) `class TestMorphism`
- `TestCategory` (line 104) `class TestCategory`
- `TestTypedGraph` (line 183) `class TestTypedGraph`
- `TestGlobalPageRank` (line 247) `class TestGlobalPageRank`
- `TestPersonalizedPageRank` (line 288) `class TestPersonalizedPageRank`
- `TestHITS` (line 325) `class TestHITS`
- `TestSeedGeneration` (line 350) `class TestSeedGeneration`
- `TestCompositeRanker` (line 403) `class TestCompositeRanker`
- `TestProjections` (line 490) `class TestProjections`
- `TestExplain` (line 539) `class TestExplain`
- `TestIntegration` (line 587) `class TestIntegration`

**Methods:**
- `_make_test_graph` (line 238) `def _make_test_graph()`
- `test_all_edge_kinds_have_weights` (line 61) `def test_all_edge_kinds_have_weights(self)`
- `test_infer_edge_kind_maps_correctly` (line 66) `def test_infer_edge_kind_maps_correctly(self)`
- `test_infer_edge_kind_falls_back` (line 71) `def test_infer_edge_kind_falls_back(self)`
- `test_edge_kind_is_str_enum` (line 75) `def test_edge_kind_is_str_enum(self)`
- `test_weight_is_edge_weight_times_confidence` (line 85) `def test_weight_is_edge_weight_times_confidence(self)`
- `test_weight_default_confidence` (line 90) `def test_weight_default_confidence(self)`
- `test_morphism_is_frozen` (line 94) `def test_morphism_is_frozen(self)`
- `test_empty_category` (line 105) `def test_empty_category(self)`
- `test_add_object_and_morphism` (line 110) `def test_add_object_and_morphism(self)`
- `test_outgoing_and_incoming` (line 118) `def test_outgoing_and_incoming(self)`
- `test_compose_same_kind` (line 130) `def test_compose_same_kind(self)`
- `test_compose_imports_then_defines` (line 140) `def test_compose_imports_then_defines(self)`
- `test_compose_incompatible_returns_none` (line 148) `def test_compose_incompatible_returns_none(self)`
- `test_compose_mismatched_target_source` (line 155) `def test_compose_mismatched_target_source(self)`
- `test_paths_finds_composition_chains` (line 162) `def test_paths_finds_composition_chains(self)`
- `test_paths_empty_when_no_route` (line 171) `def test_paths_empty_when_no_route(self)`
- `test_empty_graph` (line 184) `def test_empty_graph(self)`
- `test_stochastic_row_normalizes_to_one` (line 190) `def test_stochastic_row_normalizes_to_one(self)`
- `test_stochastic_row_empty_for_dangling` (line 199) `def test_stochastic_row_empty_for_dangling(self)`
- `test_transition_weight_aggregates_parallel_edges` (line 205) `def test_transition_weight_aggregates_parallel_edges(self)`
- `test_build_category_from_edges` (line 214) `def test_build_category_from_edges(self)`
- `test_build_category_from_edges_filters_by_node_ids` (line 225) `def test_build_category_from_edges_filters_by_node_ids(self)`
- `test_scores_sum_to_one` (line 248) `def test_scores_sum_to_one(self)`
- `test_all_nodes_have_positive_score` (line 254) `def test_all_nodes_have_positive_score(self)`
- `test_converges_within_max_iter` (line 260) `def test_converges_within_max_iter(self)`
- `test_stable_across_calls` (line 266) `def test_stable_across_calls(self)`
- `test_dangling_node_handled` (line 273) `def test_dangling_node_handled(self)`
- `test_empty_graph` (line 284) `def test_empty_graph(self)`
- `test_seed_node_gets_highest_score` (line 289) `def test_seed_node_gets_highest_score(self)`
- `test_scores_sum_to_one` (line 296) `def test_scores_sum_to_one(self)`
- `test_different_seeds_produce_different_rankings` (line 303) `def test_different_seeds_produce_different_rankings(self)`
- `test_empty_seeds_uses_uniform` (line 310) `def test_empty_seeds_uses_uniform(self)`
- `test_multi_seed` (line 317) `def test_multi_seed(self)`
- `test_authorities_and_hubs_have_positive_scores` (line 326) `def test_authorities_and_hubs_have_positive_scores(self)`
- `test_authorities_l2_normalized` (line 333) `def test_authorities_l2_normalized(self)`
- `test_hubs_l2_normalized` (line 339) `def test_hubs_l2_normalized(self)`
- `test_build_seeds_from_query_matches_node_id` (line 351) `def test_build_seeds_from_query_matches_node_id(self)`
- `test_build_seeds_from_query_matches_symbol` (line 363) `def test_build_seeds_from_query_matches_symbol(self)`
- `test_build_seeds_from_query_no_match_returns_empty` (line 374) `def test_build_seeds_from_query_no_match_returns_empty(self)`
- `test_build_seeds_for_context` (line 383) `def test_build_seeds_for_context(self)`
- `test_build_seeds_for_context_no_match` (line 392) `def test_build_seeds_for_context_no_match(self)`
- `test_rank_returns_sorted_results` (line 404) `def test_rank_returns_sorted_results(self)`
- `test_rank_items_have_all_score_fields` (line 421) `def test_rank_items_have_all_score_fields(self)`
- `test_noise_penalty_applied` (line 447) `def test_noise_penalty_applied(self)`
- `test_top_n` (line 466) `def test_top_n(self)`
- `test_explain_returns_none_for_missing` (line 479) `def test_explain_returns_none_for_missing(self)`
- `test_identity_projection_passes_all` (line 491) `def test_identity_projection_passes_all(self)`
- `test_doc_projection_filters_undocumented` (line 498) `def test_doc_projection_filters_undocumented(self)`
- `test_doc_projection_filters_morphism_kind` (line 506) `def test_doc_projection_filters_morphism_kind(self)`
- `test_apply_view_architecture` (line 512) `def test_apply_view_architecture(self)`
- `test_apply_view_reverse` (line 521) `def test_apply_view_reverse(self)`
- `test_apply_view_empty` (line 528) `def test_apply_view_empty(self)`
- `test_explain_rank_found` (line 540) `def test_explain_rank_found(self)`
- `test_explain_rank_not_found` (line 559) `def test_explain_rank_not_found(self)`
- `test_rank_summary_format` (line 565) `def test_rank_summary_format(self)`
- `test_category_from_real_edges` (line 588) `def test_category_from_real_edges(self)`
- `test_pagerank_on_real_category` (line 613) `def test_pagerank_on_real_category(self)`
- `test_ppr_favors_seed` (line 625) `def test_ppr_favors_seed(self)`
- `test_ranker_from_real_data` (line 637) `def test_ranker_from_real_data(self)`

#### `test_readme_injector.py`
**Path:** `tests/test_readme_injector.py`

**Classes:**
- `TestReadmeInjectorInjectBehavior` (line 16) `class TestReadmeInjectorInjectBehavior(TestCase)` - *BDD: ReadmeInjector injection contract.*
- `TestReadmeInjectorRemoveBehavior` (line 71) `class TestReadmeInjectorRemoveBehavior(TestCase)` - *BDD: ReadmeInjector removal contract.*
- `TestReadmeInjectorFindReadme` (line 104) `class TestReadmeInjectorFindReadme(TestCase)` - *BDD: ReadmeInjector README file detection contract.*
- `TestReadmeInjectorEdgeCases` (line 139) `class TestReadmeInjectorEdgeCases(TestCase)` - *BDD: ReadmeInjector edge case contract.*

**Methods:**
- `setUp` (line 19) `def setUp(self)`
- `tearDown` (line 24) `def tearDown(self)`
- `test_inject_into_markdown_readme_adds_kb_link` (line 28) `def test_inject_into_markdown_readme_adds_kb_link(self)`
- `test_inject_into_rst_readme_adds_kb_link` (line 38) `def test_inject_into_rst_readme_adds_kb_link(self)`
- `test_inject_is_idempotent_does_not_duplicate` (line 47) `def test_inject_is_idempotent_does_not_duplicate(self)`
- `test_inject_no_readme_file_returns_false` (line 58) `def test_inject_no_readme_file_returns_false(self)`
- `test_inject_preserves_existing_content` (line 62) `def test_inject_preserves_existing_content(self)`
- `setUp` (line 74) `def setUp(self)`
- `tearDown` (line 79) `def tearDown(self)`
- `test_remove_strips_injected_section` (line 83) `def test_remove_strips_injected_section(self)`
- `test_remove_without_injection_returns_false` (line 93) `def test_remove_without_injection_returns_false(self)`
- `test_remove_no_readme_returns_false` (line 99) `def test_remove_no_readme_returns_false(self)`
- `setUp` (line 107) `def setUp(self)`
- `tearDown` (line 111) `def tearDown(self)`
- `test_finds_readme_md` (line 115) `def test_finds_readme_md(self)`
- `test_finds_readme_rst` (line 121) `def test_finds_readme_rst(self)`
- `test_prefers_readme_md_over_rst` (line 127) `def test_prefers_readme_md_over_rst(self)`
- `test_returns_none_when_no_readme` (line 134) `def test_returns_none_when_no_readme(self)`
- `setUp` (line 142) `def setUp(self)`
- `tearDown` (line 147) `def tearDown(self)`
- `test_inject_into_empty_readme` (line 151) `def test_inject_into_empty_readme(self)`
- `test_custom_kb_filename_works` (line 159) `def test_custom_kb_filename_works(self)`

#### `test_refactorizer.py`
**Path:** `tests/test_refactorizer.py`

**Classes:**
- `TestMonolithRefactorizerContract` (line 18) `class TestMonolithRefactorizerContract(TestCase)` - *Contract: MonolithRefactorizer generates refactoring plans.*

**Methods:**
- `setUp` (line 21) `def setUp(self)`
- `_make_symbol` (line 25) `def _make_symbol(self, name, kind, line)`
- `_make_node` (line 28) `def _make_node(self, nid, symbols)`
- `_make_edge` (line 37) `def _make_edge(self, src, tgt)`
- `test_analyze_empty_graph_returns_empty` (line 40) `def test_analyze_empty_graph_returns_empty(self)`
- `test_analyze_ignores_small_files` (line 44) `def test_analyze_ignores_small_files(self)`
- `test_analyze_detects_large_file` (line 50) `def test_analyze_detects_large_file(self)`
- `test_analyze_generates_extract_class_for_multiple_classes` (line 59) `def test_analyze_generates_extract_class_for_multiple_classes(self)`
- `test_analyze_generates_extract_function_for_multiple_functions` (line 74) `def test_analyze_generates_extract_function_for_multiple_functions(self)`
- `test_analyze_splits_file_with_many_symbols` (line 89) `def test_analyze_splits_file_with_many_symbols(self)`
- `test_analyze_estimates_impact_from_resolved_edges` (line 97) `def test_analyze_estimates_impact_from_resolved_edges(self)`
- `test_generate_script_contains_shebang` (line 109) `def test_generate_script_contains_shebang(self)`
- `test_generate_script_contains_set_e` (line 129) `def test_generate_script_contains_set_e(self)`
- `test_generate_script_contains_sed_commands` (line 140) `def test_generate_script_contains_sed_commands(self)`
- `test_analyze_sorted_by_line_count` (line 160) `def test_analyze_sorted_by_line_count(self)`
- `test_analyze_respects_max_files_limit` (line 173) `def test_analyze_respects_max_files_limit(self)`

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

#### `test_taint_bdd.py`
**Path:** `tests/test_taint_bdd.py`

**Functions:**
- `_build_project_files` (line 29) `def _build_project_files(project, root)`
- `_scan_project` (line 36) `def _scan_project(root, cfg)`
- `_run_taint` (line 54) `def _run_taint(files, cfg)`
- `test_direct_dangerous_import` (line 71) `def test_direct_dangerous_import()`
- `test_taint_propagates_chain` (line 75) `def test_taint_propagates_chain()`
- `test_taint_max_depth` (line 79) `def test_taint_max_depth()`
- `test_cross_language_taint` (line 83) `def test_cross_language_taint()`
- `test_bdd_skipped` (line 87) `def test_bdd_skipped()`
- `_bkg` (line 112) `def _bkg()`
- `_direct_given` (line 117) `def _direct_given()`
- `_direct_when` (line 121) `def _direct_when(_taint_result)`
- `_check_has_path` (line 125) `def _check_has_path(_taint_result)`
- `_check_direct_path` (line 130) `def _check_direct_path(_taint_result)`
- `_check_src` (line 135) `def _check_src(_taint_result)`
- `_check_sink` (line 139) `def _check_sink(_taint_result)`
- `_chain_given` (line 144) `def _chain_given()`
- `_chain_when` (line 148) `def _chain_when(_taint_result)`
- `_check_long_path` (line 152) `def _check_long_path(_taint_result)`
- `_shallow_cfg` (line 159) `def _shallow_cfg()`
- `_chain_given2` (line 163) `def _chain_given2()`
- `_run_shallow` (line 167) `def _run_shallow(_shallow_cfg)`
- `_check_shallow` (line 171) `def _check_shallow(_taint_result)`
- `_js_given` (line 178) `def _js_given()`
- `_js_when` (line 182) `def _js_when(_taint_result)`
- `_check_js_dangerous` (line 186) `def _check_js_dangerous(_taint_result)`
- `_check_js_source` (line 192) `def _check_js_source(_taint_result)`

#### `test_uml.py`
**Path:** `tests/test_uml.py`

**Classes:**
- `TestUmlMermaidDiagram` (line 16) `class TestUmlMermaidDiagram(TestCase)` - *BDD: UmlGenerator mermaid class diagram rendering contract.*
- `TestUmlSanitizeId` (line 157) `class TestUmlSanitizeId(TestCase)` - *BDD: UmlGenerator ID sanitization contract.*
- `TestUmlCodeGenerationCpp` (line 181) `class TestUmlCodeGenerationCpp(TestCase)` - *BDD: C++ code generation contract.*
- `TestUmlCodeGenerationJava` (line 239) `class TestUmlCodeGenerationJava(TestCase)` - *BDD: Java code generation contract.*
- `TestUmlCodeGenerationCSharp` (line 281) `class TestUmlCodeGenerationCSharp(TestCase)` - *BDD: C# code generation contract.*
- `TestUmlCodeGenerationGo` (line 306) `class TestUmlCodeGenerationGo(TestCase)` - *BDD: Go code generation contract.*
- `TestUmlCodeGenerationRust` (line 347) `class TestUmlCodeGenerationRust(TestCase)` - *BDD: Rust code generation contract.*
- `TestUmlCodeGenerationPhp` (line 387) `class TestUmlCodeGenerationPhp(TestCase)` - *BDD: PHP code generation contract.*
- `TestUmlCodeGenerationKotlinScalaSwiftDartRuby` (line 427) `class TestUmlCodeGenerationKotlinScalaSwiftDartRuby(TestCase)` - *BDD: Kotlin, Scala, Swift, Dart, Ruby code generation contracts.*

**Methods:**
- `setUp` (line 19) `def setUp(self)`
- `test_render_empty_nodes_returns_empty_string` (line 23) `def test_render_empty_nodes_returns_empty_string(self)`
- `test_render_no_class_symbols_returns_empty_string` (line 27) `def test_render_no_class_symbols_returns_empty_string(self)`
- `test_render_single_class_produces_mermaid_class_diagram` (line 42) `def test_render_single_class_produces_mermaid_class_diagram(self)`
- `test_render_multiple_classes_from_different_files` (line 62) `def test_render_multiple_classes_from_different_files(self)`
- `test_render_with_import_edges_produces_relationships` (line 90) `def test_render_with_import_edges_produces_relationships(self)`
- `test_render_respects_max_classes_limit` (line 119) `def test_render_respects_max_classes_limit(self)`
- `test_render_with_structs_interfaces_traits` (line 137) `def test_render_with_structs_interfaces_traits(self)`
- `setUp` (line 160) `def setUp(self)`
- `test_sanitize_preserves_alphanumeric` (line 164) `def test_sanitize_preserves_alphanumeric(self)`
- `test_sanitize_replaces_special_chars` (line 168) `def test_sanitize_replaces_special_chars(self)`
- `test_sanitize_prefixes_digit_start` (line 172) `def test_sanitize_prefixes_digit_start(self)`
- `test_sanitize_handles_empty_string` (line 176) `def test_sanitize_handles_empty_string(self)`
- `setUp` (line 184) `def setUp(self)`
- `test_generate_cpp_produces_valid_code` (line 188) `def test_generate_cpp_produces_valid_code(self)`
- `test_generate_cpp_with_empty_classes` (line 208) `def test_generate_cpp_with_empty_classes(self)`
- `test_generate_cpp_unknown_language_returns_error_message` (line 223) `def test_generate_cpp_unknown_language_returns_error_message(self)`
- `setUp` (line 242) `def setUp(self)`
- `test_generate_java_class_produces_valid_code` (line 246) `def test_generate_java_class_produces_valid_code(self)`
- `test_generate_java_interface_produces_interface` (line 265) `def test_generate_java_interface_produces_interface(self)`
- `setUp` (line 284) `def setUp(self)`
- `test_generate_csharp_produces_valid_code` (line 288) `def test_generate_csharp_produces_valid_code(self)`
- `setUp` (line 309) `def setUp(self)`
- `test_generate_go_struct_produces_valid_code` (line 313) `def test_generate_go_struct_produces_valid_code(self)`
- `test_generate_go_interface_produces_valid_code` (line 330) `def test_generate_go_interface_produces_valid_code(self)`
- `setUp` (line 350) `def setUp(self)`
- `test_generate_rust_struct_produces_valid_code` (line 354) `def test_generate_rust_struct_produces_valid_code(self)`
- `test_generate_rust_trait_produces_valid_code` (line 370) `def test_generate_rust_trait_produces_valid_code(self)`
- `setUp` (line 390) `def setUp(self)`
- `test_generate_php_class_produces_valid_code` (line 394) `def test_generate_php_class_produces_valid_code(self)`
- `test_generate_php_interface_produces_valid_code` (line 411) `def test_generate_php_interface_produces_valid_code(self)`
- `setUp` (line 430) `def setUp(self)`
- `_make_class_node` (line 434) `def _make_class_node(self, name, lang, kind)`
- `test_generate_kotlin_produces_valid_code` (line 446) `def test_generate_kotlin_produces_valid_code(self)`
- `test_generate_scala_produces_valid_code` (line 452) `def test_generate_scala_produces_valid_code(self)`
- `test_generate_scala_trait_produces_valid_code` (line 458) `def test_generate_scala_trait_produces_valid_code(self)`
- `test_generate_swift_produces_valid_code` (line 463) `def test_generate_swift_produces_valid_code(self)`
- `test_generate_swift_protocol_produces_valid_code` (line 469) `def test_generate_swift_protocol_produces_valid_code(self)`
- `test_generate_dart_produces_valid_code` (line 474) `def test_generate_dart_produces_valid_code(self)`
- `test_generate_ruby_produces_valid_code` (line 480) `def test_generate_ruby_produces_valid_code(self)`

### SH (10 files)

#### `.refactor__app.sh`
**Path:** `.refactor__app.sh`
**File Doc:** *Refactoring plan for readmenator/_app.py Current lines: 643 Estimated impact: 5 files*

*No symbols extracted*

#### `.refactor__documentation.sh`
**Path:** `.refactor__documentation.sh`
**File Doc:** *Refactoring plan for readmenator/_documentation.py Current lines: 1087 Estimated impact: 2 files*

*No symbols extracted*

#### `.refactor__exporter.sh`
**Path:** `.refactor__exporter.sh`
**File Doc:** *Refactoring plan for readmenator/_exporter.py Current lines: 898 Estimated impact: 2 files*

*No symbols extracted*

#### `.refactor__mcp_server.sh`
**Path:** `.refactor__mcp_server.sh`
**File Doc:** *Refactoring plan for readmenator/_mcp_server.py Current lines: 813 Estimated impact: 3 files*

*No symbols extracted*

#### `.refactor__rank.sh`
**Path:** `.refactor__rank.sh`
**File Doc:** *Refactoring plan for readmenator/_rank.py Current lines: 537 Estimated impact: 7 files*

*No symbols extracted*

#### `.refactor__security.sh`
**Path:** `.refactor__security.sh`
**File Doc:** *Refactoring plan for readmenator/_security.py Current lines: 583 Estimated impact: 2 files*

*No symbols extracted*

#### `.refactor__uml.sh`
**Path:** `.refactor__uml.sh`
**File Doc:** *Refactoring plan for readmenator/_uml.py Current lines: 599 Estimated impact: 4 files*

*No symbols extracted*

#### `.refactor_test_parsers.sh`
**Path:** `.refactor_test_parsers.sh`
**File Doc:** *Refactoring plan for tests/test_parsers.py Current lines: 487 Estimated impact: 0 files*

*No symbols extracted*

#### `.refactor_test_ranking.sh`
**Path:** `.refactor_test_ranking.sh`
**File Doc:** *Refactoring plan for tests/test_ranking.py Current lines: 666 Estimated impact: 0 files*

*No symbols extracted*

#### `.refactor_test_uml.sh`
**Path:** `.refactor_test_uml.sh`
**File Doc:** *Refactoring plan for tests/test_uml.py Current lines: 488 Estimated impact: 0 files*

*No symbols extracted*
