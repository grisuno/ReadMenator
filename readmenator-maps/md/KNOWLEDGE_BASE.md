# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. 105 files, 1852 symbols, 788 imports. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Start here:** Statistics Dashboard for scope, God Nodes for blast radius, Architecture Reference for per-file API. Agents: prefer `readmenator-agent/INDEX.md` + `SYMBOLS.md`.

**Wiki:** prefer `readmenator-wiki/index.md` for progressive disclosure: one synthesis page per community, `connections.json` with EXTRACTED vs INFERRED confidence, `queries.md` log, `REPORT.md` audit.

**Confidence:** EXTRACTED = parsed from source, INFERRED = heuristic bridge, AMBIGUOUS = reported, never hidden. See `readmenator-wiki/REPORT.md`.

**Total Files Parsed:** 105 | **Total Symbols Extracted:** 1852 | **Total Imports:** 788
 | **Resolved Imports:** 348

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:c8d49e5 | date:2026-07-18 -->


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
10. [Change Impact Analysis](#change-impact-analysis)
11. [Suggested Linting Rules](#suggested-linting-rules)
12. [Orphans](#orphans)
13. [Query Recipes](#query-recipes)
14. [Structural Knowledge Map](#structural-knowledge-map)
15. [UML Class Diagram](#uml-class-diagram)
16. [Code Property Graph](#code-property-graph)
17. [Architecture Reference](#architecture-reference)
    - [PY (105 files)](#py-105-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 105 |
| Total Symbols | 1852 |
| Total Imports | 788 |
| Call Edges | 11251 |
| Inheritance Edges | 130 |
| Languages | 1 |
| Avg Symbols/File | 17.6 |
| Avg Imports/File | 7.5 |
| Resolved Imports | 348 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `test_diagrams.py` | 30 | 69 | py |
| `_pipeline.py` | 27 | 34 | py |
| `test_agent_output.py` | 27 | 45 | py |
| `_video.py` | 26 | 49 | py |
| `test_parsers_property.py` | 26 | 27 | py |
| `__init__.py` | 23 | 2 | py |
| `_app.py` | 22 | 50 | py |
| `test_agent_friendliness.py` | 20 | 43 | py |
| `_agent_output.py` | 16 | 32 | py |
| `_wiki.py` | 16 | 31 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 57 |
| testing | 39 |
| infrastructure | 4 |
| business_logic | 3 |
| data_access | 2 |

### utility

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `__main__.py` (py, 3 symbols)
- `_agent_output.py` (py, 32 symbols)
- `_analyzer.py` (py, 18 symbols)
- `_app.py` (py, 50 symbols)
- `_category.py` (py, 26 symbols)
- `_cpg.py` (py, 6 symbols)
- `_cursorrules_generator.py` (py, 8 symbols)
- `_dead_code.py` (py, 5 symbols)
- `_diagrams.py` (py, 79 symbols)
- `_documentation.py` (py, 28 symbols)
- `_explain.py` (py, 3 symbols)
- `_exporter.py` (py, 15 symbols)
- `_gh_wiki.py` (py, 18 symbols)
- *... and 42 more*

### infrastructure

- `_agent_injector.py` (py, 14 symbols)
- `_cache.py` (py, 14 symbols)
- `_config.py` (py, 1 symbols)
- `_readme_injector.py` (py, 8 symbols)

### data_access

- `_dataflow.py` (py, 21 symbols)
- `_query.py` (py, 17 symbols)

### business_logic

- `_layer_rules.py` (py, 4 symbols)
- `_models.py` (py, 20 symbols)
- `_rule_gen.py` (py, 9 symbols)

### testing

- `__init__.py` (py, 0 symbols)
- `test_agent_friendliness.py` (py, 43 symbols)
- `test_agent_injector.py` (py, 38 symbols)
- `test_agent_output.py` (py, 45 symbols)
- `test_analyzer.py` (py, 14 symbols)
- `test_cache.py` (py, 22 symbols)
- `test_config.py` (py, 6 symbols)
- `test_cpg.py` (py, 11 symbols)
- `test_cursorrules.py` (py, 12 symbols)
- `test_dataflow.py` (py, 47 symbols)
- `test_dead_code.py` (py, 15 symbols)
- `test_diagrams.py` (py, 69 symbols)
- `test_documentation.py` (py, 29 symbols)
- `test_exporter.py` (py, 15 symbols)
- `test_gh_wiki.py` (py, 15 symbols)
- *... and 24 more*

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `_config.py` | 0.2747 | 0.1127 | 0.1199 | 0.00 | 2.00 |
| 2 | `_models.py` | 0.2129 | 0.1656 | 0.1672 | 0.00 | 1.05 |
| 3 | `_category.py` | 0.1567 | 0.1649 | 0.1626 | 0.00 | 0.50 |
| 4 | `_c.py` | 0.1343 | 0.0000 | 0.0045 | 0.00 | 1.33 |
| 5 | `_gitmeta.py` | 0.1298 | 0.0074 | 0.0076 | 0.00 | 1.25 |
| 6 | `_base.py` | 0.1249 | 0.0002 | 0.0409 | 0.00 | 1.17 |
| 7 | `_layers.py` | 0.1233 | 0.0157 | 0.0096 | 0.00 | 1.14 |
| 8 | `_agent_output.py` | 0.1230 | 0.0420 | 0.0047 | 0.00 | 1.03 |
| 9 | `_rule_gen.py` | 0.1222 | 0.0470 | 0.0053 | 0.00 | 1.00 |
| 10 | `_watcher.py` | 0.1210 | 0.0001 | 0.0047 | 0.00 | 1.20 |

**Query anchors:** readmenator/_documentation.py, tests/test_agent_output.py, readmenator/_linter.py, readmenator/_diagrams.py, tests/test_linter.py, tests/test_ranking.py, readmenator/_rule_gen.py, tests/test_rule_gen.py (+3 more)

**Top result justification paths:**

  `_documentation.py -> _config.py`
  `_documentation.py -> _uml.py -> _config.py`

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `_models.py` | 160.0 | | 0.1672 |
| `_config.py` | 122.1 | | 0.1199 |
| `_pipeline.py` | 55.4 | | 0.0000 |
| `_app.py` | 53.0 | | 0.0000 |
| `__init__.py` | 48.2 | | 0.0000 |
| `_base.py` | 44.6 | | 0.0409 |
| `test_parsers_property.py` | 42.7 | | 0.0000 |
| `test_agent_friendliness.py` | 28.3 | | 0.0000 |
| `_agent_output.py` | 23.2 | | 0.0047 |
| `_diagrams.py` | 21.9 | | 0.0000 |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### readmenator: _diagrams (Cohesion: 0.55)

**50 files** in this community:

- `readmenator.py` (py, 0 symbols)
- `__init__.py` (py, 0 symbols)
- `__main__.py` (py, 3 symbols)
- `_analyzer.py` (py, 18 symbols)
- `_app.py` (py, 50 symbols)
- `_config.py` (py, 1 symbols)
- `_cpg.py` (py, 6 symbols)
- `_cursorrules_generator.py` (py, 8 symbols)
- `_dataflow.py` (py, 21 symbols)
- `_dead_code.py` (py, 5 symbols)
- `_diagrams.py` (py, 79 symbols)
- `_exporter.py` (py, 15 symbols)
- `_hotspots.py` (py, 7 symbols)
- `_layer_rules.py` (py, 4 symbols)
- `_layers.py` (py, 7 symbols)
- `_linter.py` (py, 7 symbols)
- `_mcp_server.py` (py, 52 symbols)
- `_pipeline.py` (py, 34 symbols)
- `_query.py` (py, 17 symbols)
- `_readme_injector.py` (py, 8 symbols)
- ... and 30 more files

### tests: _agent_injector (Cohesion: 0.29)

**3 files** in this community:

- `_agent_injector.py` (py, 14 symbols)
- `test_agent_injector.py` (py, 38 symbols)
- `test_agent_output.py` (py, 45 symbols)

### readmenator: _agent_output (Cohesion: 0.35)

**10 files** in this community:

- `_agent_output.py` (py, 32 symbols)
- `_cache.py` (py, 14 symbols)
- `_gh_wiki.py` (py, 18 symbols)
- `_gitmeta.py` (py, 4 symbols)
- `_purpose.py` (py, 7 symbols)
- `_resolver.py` (py, 17 symbols)
- `test_agent_friendliness.py` (py, 43 symbols)
- `test_cache.py` (py, 22 symbols)
- `test_gh_wiki.py` (py, 15 symbols)
- `test_resolver.py` (py, 22 symbols)

### readmenator: _category (Cohesion: 0.42)

**5 files** in this community:

- `_category.py` (py, 26 symbols)
- `_explain.py` (py, 3 symbols)
- `_projections.py` (py, 15 symbols)
- `_rank.py` (py, 17 symbols)
- `test_ranking.py` (py, 72 symbols)

### readmenator: _documentation (Cohesion: 0.23)

**4 files** in this community:

- `_documentation.py` (py, 28 symbols)
- `_mermaid.py` (py, 4 symbols)
- `test_documentation.py` (py, 29 symbols)
- `test_mermaid.py` (py, 11 symbols)

### readmenator/parsers (Cohesion: 0.56)

**26 files** in this community:

- `_models.py` (py, 20 symbols)
- `__init__.py` (py, 2 symbols)
- `_assembly.py` (py, 2 symbols)
- `_base.py` (py, 6 symbols)
- `_c.py` (py, 3 symbols)
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
- ... and 6 more files

### tests: _scanner (Cohesion: 0.21)

**5 files** in this community:

- `_scanner.py` (py, 14 symbols)
- `_taint.py` (py, 6 symbols)
- `test_scanner.py` (py, 21 symbols)
- `test_taint.py` (py, 10 symbols)
- `test_taint_bdd.py` (py, 26 symbols)

---

## Surprising Connections

Files in different communities connected through 3+ indirect hops.

- `readmenator.py` <-> `test_agent_injector.py` (5 hops, across 2 communities)
- `test_agent_injector.py` <-> `test_resolver.py` (5 hops, across 3 communities)
- `test_readme_injector.py` <-> `test_resolver.py` (5 hops, across 2 communities)
- `__init__.py` <-> `test_agent_injector.py` (4 hops, across 2 communities)
- `__main__.py` <-> `test_agent_injector.py` (4 hops, across 2 communities)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does _models.py depend on, and what depends on it? (79 connections)
- What does _config.py depend on, and what depends on it? (61 connections)
- What does _pipeline.py depend on, and what depends on it? (26 connections)
- How are the 50 files in 'readmenator: _diagrams' related to each other?
- Why are readmenator.py and test_agent_injector.py connected through 5 hops across 2 communities?

---

## Taint Propagation Map

Taint analysis traces how dangerous imports propagate through the codebase via transitive dependencies. Source files import dangerous modules directly; sink files receive the danger indirectly.

**Taint Sources:** 6 | **Taint Sinks:** 14 | **Propagation Paths:** 20

- `_agent_injector.py` imports `subprocess` (0 hop to `_agent_injector.py`) [high]
  Path: _agent_injector.py
- `_documentation.py` imports `subprocess` (0 hop to `_documentation.py`) [high]
  Path: _documentation.py
- `_documentation.py` imports `subprocess` (1 hop to `_cpg.py`) [high]
  Path: _documentation.py -> _cpg.py
- `_documentation.py` imports `subprocess` (1 hop to `_rank.py`) [high]
  Path: _documentation.py -> _rank.py
- `_documentation.py` imports `subprocess` (1 hop to `_uml.py`) [high]
  Path: _documentation.py -> _uml.py
- `_documentation.py` imports `subprocess` (1 hop to `_mermaid.py`) [high]
  Path: _documentation.py -> _mermaid.py
- `_documentation.py` imports `subprocess` (1 hop to `_models.py`) [high]
  Path: _documentation.py -> _models.py
- `_documentation.py` imports `subprocess` (1 hop to `_config.py`) [high]
  Path: _documentation.py -> _config.py
- `_documentation.py` imports `subprocess` (2 hops to `_category.py`) [high]
  Path: _documentation.py -> _rank.py -> _category.py
- `_gh_wiki.py` imports `subprocess` (0 hop to `_gh_wiki.py`) [high]
  Path: _gh_wiki.py
- `_gh_wiki.py` imports `subprocess` (1 hop to `_gitmeta.py`) [high]
  Path: _gh_wiki.py -> _gitmeta.py
- `_gh_wiki.py` imports `subprocess` (1 hop to `_config.py`) [high]
  Path: _gh_wiki.py -> _config.py
- `_video.py` imports `subprocess` (0 hop to `_video.py`) [high]
  Path: _video.py
- `_video.py` imports `subprocess` (1 hop to `_models.py`) [high]
  Path: _video.py -> _models.py
- `_video.py` imports `subprocess` (1 hop to `_config.py`) [high]
  Path: _video.py -> _config.py
- `_video.py` imports `subprocess` (2 hops to `_category.py`) [high]
  Path: _video.py -> _models.py -> _category.py
- `readmenator_orchestrator.py` imports `subprocess` (0 hop to `readmenator_orchestrator.py`) [high]
  Path: readmenator_orchestrator.py
- `test_gh_wiki.py` imports `subprocess` (0 hop to `test_gh_wiki.py`) [high]
  Path: test_gh_wiki.py
- `test_gh_wiki.py` imports `subprocess` (1 hop to `_gh_wiki.py`) [high]
  Path: test_gh_wiki.py -> _gh_wiki.py
- `test_gh_wiki.py` imports `subprocess` (1 hop to `_config.py`) [high]
  Path: test_gh_wiki.py -> _config.py

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `_config.py` | 0.011 | 0.667 | 0.405 | 1 | 64 |
| `_models.py` | 0.230 | 1.000 | 0.692 | 20 | 96 |
| `_category.py` | 0.299 | 0.125 | 0.195 | 26 | 12 |
| `_c.py` | 0.035 | 0.083 | 0.064 | 3 | 8 |
| `_gitmeta.py` | 0.046 | 0.062 | 0.056 | 4 | 6 |
| `_base.py` | 0.069 | 0.281 | 0.196 | 6 | 27 |
| `_layers.py` | 0.081 | 0.125 | 0.107 | 7 | 12 |
| `_agent_output.py` | 0.368 | 0.271 | 0.310 | 32 | 26 |
| `_rule_gen.py` | 0.103 | 0.125 | 0.116 | 9 | 12 |
| `_watcher.py` | 0.058 | 0.094 | 0.079 | 5 | 9 |
| `test_diagrams.py` | 0.793 | 0.375 | 0.542 | 69 | 36 |
| `_app.py` | 0.575 | 0.490 | 0.524 | 50 | 47 |
| `_pipeline.py` | 0.391 | 0.552 | 0.488 | 34 | 53 |
| `_diagrams.py` | 0.908 | 0.177 | 0.469 | 79 | 17 |
| `test_agent_output.py` | 0.517 | 0.385 | 0.438 | 45 | 37 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `_category.py` | 8 | 50 | 81 |
| `_models.py` | 50 | 0 | 78 |
| `_config.py` | 50 | 0 | 61 |
| `_base.py` | 20 | 17 | 37 |
| `_c.py` | 2 | 16 | 18 |
| `_csharp.py` | 2 | 16 | 18 |
| `_dart.py` | 2 | 16 | 18 |
| `_elixir.py` | 2 | 16 | 18 |
| `_gdscript.py` | 2 | 16 | 18 |
| `_go.py` | 2 | 16 | 18 |
| `_java.py` | 2 | 16 | 18 |
| `_javascript.py` | 2 | 16 | 18 |
| `_kotlin.py` | 2 | 16 | 18 |
| `_lua.py` | 2 | 16 | 18 |
| `_nim.py` | 2 | 16 | 18 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 1622 total | py | 1622 |
| `RM002` | info | Print statement found (consider logging instead) | python | 16 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `readmenator_orchestrator.py` (34 symbols, no doc)
- `__init__.py` (0 symbols, no doc)
- `test_agent_output.py` (45 symbols, no doc)
- `test_config.py` (6 symbols, no doc)
- `test_dataflow.py` (47 symbols, no doc)
- `test_documentation.py` (29 symbols, no doc)
- `test_integration.py` (16 symbols, no doc)
- `test_mermaid.py` (11 symbols, no doc)
- `test_models.py` (11 symbols, no doc)
- `test_parsers.py` (87 symbols, no doc)
- `test_query.py` (18 symbols, no doc)
- `test_scanner.py` (21 symbols, no doc)
- `test_wiki.py` (30 symbols, no doc)

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
    subgraph community_0 ["readmenator: _diagrams"]
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
    end
    subgraph community_5 ["readmenator/parsers"]
    tests_test_parsers_property_py["test_parsers_property.py (py)"]
    class tests_test_parsers_property_py mod;
    readmenator_parsers___init___py["__init__.py (py)"]
    class readmenator_parsers___init___py mod;
    readmenator__app_py["_app.py (py)"]
    class readmenator__app_py mod;
    end
    subgraph community_1 ["tests: _agent_injector"]
    tests_test_agent_output_py["test_agent_output.py (py)"]
    class tests_test_agent_output_py mod;
    tests_test_diagrams_py["test_diagrams.py (py)"]
    class tests_test_diagrams_py mod;
    end
    subgraph community_2 ["readmenator: _agent_output"]
    tests_test_agent_friendliness_py["test_agent_friendliness.py (py)"]
    class tests_test_agent_friendliness_py mod;
    readmenator__video_py["_video.py (py)"]
    class readmenator__video_py mod;
    readmenator__agent_output_py["_agent_output.py (py)"]
    class readmenator__agent_output_py mod;
    readmenator__wiki_py["_wiki.py (py)"]
    class readmenator__wiki_py mod;
    tests_test_wiki_py["test_wiki.py (py)"]
    class tests_test_wiki_py mod;
    readmenator___init___py["__init__.py (py)"]
    class readmenator___init___py mod;
    readmenator__mcp_server_py["_mcp_server.py (py)"]
    class readmenator__mcp_server_py mod;
    end
    subgraph community_4 ["readmenator: _documentation"]
    tests_test_documentation_py["test_documentation.py (py)"]
    class tests_test_documentation_py mod;
    readmenator__documentation_py["_documentation.py (py)"]
    class readmenator__documentation_py mod;
    end
    subgraph community_6 ["tests: _scanner"]
    tests_test_taint_bdd_py["test_taint_bdd.py (py)"]
    class tests_test_taint_bdd_py mod;
    tests_test_refactorizer_py["test_refactorizer.py (py)"]
    class tests_test_refactorizer_py mod;
    readmenator_orchestrator_py["readmenator_orchestrator.py (py)"]
    class readmenator_orchestrator_py mod;
    readmenator__gh_wiki_py["_gh_wiki.py (py)"]
    class readmenator__gh_wiki_py mod;
    end
    subgraph community_3 ["readmenator: _category"]
    tests_test_ranking_py["test_ranking.py (py)"]
    class tests_test_ranking_py mod;
    tests_test_dataflow_py["test_dataflow.py (py)"]
    class tests_test_dataflow_py mod;
    tests_test_mcp_server_py["test_mcp_server.py (py)"]
    class tests_test_mcp_server_py mod;
    tests_test_scanner_py["test_scanner.py (py)"]
    class tests_test_scanner_py mod;
    readmenator__exporter_py["_exporter.py (py)"]
    class readmenator__exporter_py mod;
    readmenator___main___py["__main__.py (py)"]
    class readmenator___main___py mod;
    readmenator__diagrams_py["_diagrams.py (py)"]
    class readmenator__diagrams_py mod;
    tests_test_security_py["test_security.py (py)"]
    class tests_test_security_py mod;
    readmenator__scanner_py["_scanner.py (py)"]
    class readmenator__scanner_py mod;
    tests_test_video_py["test_video.py (py)"]
    class tests_test_video_py mod;
    tests_test_agent_injector_py["test_agent_injector.py (py)"]
    class tests_test_agent_injector_py mod;
    tests_test_readme_injector_py["test_readme_injector.py (py)"]
    class tests_test_readme_injector_py mod;
    tests_test_cache_py["test_cache.py (py)"]
    class tests_test_cache_py mod;
    readmenator__analyzer_py["_analyzer.py (py)"]
    class readmenator__analyzer_py mod;
    tests_test_gh_wiki_py["test_gh_wiki.py (py)"]
    class tests_test_gh_wiki_py mod;
    tests_test_analyzer_py["test_analyzer.py (py)"]
    class tests_test_analyzer_py mod;
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
    readmenator__dataflow_py["_dataflow.py (py)"]
    class readmenator__dataflow_py mod;
    tests_test_integration_py["test_integration.py (py)"]
    class tests_test_integration_py mod;
    tests_test_dead_code_py["test_dead_code.py (py)"]
    class tests_test_dead_code_py mod;
    readmenator__agent_injector_py["_agent_injector.py (py)"]
    class readmenator__agent_injector_py mod;
    readmenator__cache_py["_cache.py (py)"]
    class readmenator__cache_py mod;
    tests_test_linter_py["test_linter.py (py)"]
    class tests_test_linter_py mod;
    tests_test_layer_rules_py["test_layer_rules.py (py)"]
    class tests_test_layer_rules_py mod;
    tests_test_hotspots_py["test_hotspots.py (py)"]
    class tests_test_hotspots_py mod;
    tests_test_taint_py["test_taint.py (py)"]
    class tests_test_taint_py mod;
    readmenator__refactorizer_py["_refactorizer.py (py)"]
    class readmenator__refactorizer_py mod;
    readmenator__watcher_py["_watcher.py (py)"]
    class readmenator__watcher_py mod;
    readmenator__resolver_py["_resolver.py (py)"]
    class readmenator__resolver_py mod;
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
    readmenator__rank_py["_rank.py (py)"]
    class readmenator__rank_py mod;
    readmenator__projections_py["_projections.py (py)"]
    class readmenator__projections_py mod;
    readmenator__layers_py["_layers.py (py)"]
    class readmenator__layers_py mod;
    readmenator__cpg_py["_cpg.py (py)"]
    class readmenator__cpg_py mod;
    readmenator__layer_rules_py["_layer_rules.py (py)"]
    class readmenator__layer_rules_py mod;
    readmenator__explain_py["_explain.py (py)"]
    class readmenator__explain_py mod;
    readmenator_parsers__c_py["_c.py (py)"]
    class readmenator_parsers__c_py mod;
    readmenator_parsers__assembly_py["_assembly.py (py)"]
    class readmenator_parsers__assembly_py mod;
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
    readmenator__purpose_py["_purpose.py (py)"]
    class readmenator__purpose_py mod;
    readmenator__sarif_py["_sarif.py (py)"]
    class readmenator__sarif_py mod;
    readmenator__mermaid_py["_mermaid.py (py)"]
    class readmenator__mermaid_py mod;
    readmenator__category_py["_category.py (py)"]
    class readmenator__category_py mod;
    tests_test_resolver_py["test_resolver.py (py)"]
    class tests_test_resolver_py mod;
    readmenator__readme_injector_py["_readme_injector.py (py)"]
    class readmenator__readme_injector_py mod;
    tests_test_config_py["test_config.py (py)"]
    class tests_test_config_py mod;
    readmenator_py["readmenator.py (py)"]
    class readmenator_py mod;
    tests_test_models_py["test_models.py (py)"]
    class tests_test_models_py mod;
    readmenator__gitmeta_py["_gitmeta.py (py)"]
    class readmenator__gitmeta_py mod;
    readmenator__config_py["_config.py (py)"]
    class readmenator__config_py mod;
    tests___init___py["__init__.py (py)"]
    class tests___init___py mod;
    end
    readmenator___init___py -- resolved_imports --> readmenator__app_py
    readmenator___init___py -- resolved_imports --> readmenator__category_py
    readmenator___init___py -- resolved_imports --> readmenator__config_py
    readmenator___init___py -- resolved_imports --> readmenator__diagrams_py
    readmenator___init___py -- resolved_imports --> readmenator__mcp_server_py
    readmenator___init___py -- resolved_imports --> readmenator__models_py
    readmenator___init___py -- resolved_imports --> readmenator__rank_py
    readmenator___init___py -- resolved_imports --> readmenator__readme_injector_py
    readmenator___init___py -- resolved_imports --> readmenator__uml_py
    readmenator___main___py -- resolved_imports --> readmenator__app_py
    readmenator___main___py -- resolved_imports --> readmenator__config_py
    readmenator___main___py -- resolved_imports --> readmenator__mcp_server_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__cache_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__config_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__gitmeta_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__models_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__purpose_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__resolver_py
    readmenator__agent_output_py -- resolved_imports --> readmenator__security_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__config_py
    readmenator__analyzer_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__cache_py
    readmenator__app_py -- resolved_imports --> readmenator__config_py
    readmenator__app_py -- resolved_imports --> readmenator__cursorrules_generator_py
    readmenator__app_py -- resolved_imports --> readmenator__dead_code_py
    readmenator__app_py -- resolved_imports --> readmenator__diagrams_py
    readmenator__app_py -- resolved_imports --> readmenator__gh_wiki_py
    readmenator__app_py -- resolved_imports --> readmenator__layers_py
    readmenator__app_py -- resolved_imports --> readmenator__linter_py
    readmenator__app_py -- resolved_imports --> readmenator__models_py
    readmenator__app_py -- resolved_imports --> readmenator__pipeline_py
    readmenator__app_py -- resolved_imports --> readmenator__query_py
    readmenator__app_py -- resolved_imports --> readmenator__rank_py
    readmenator__app_py -- resolved_imports --> readmenator__refactorizer_py
    readmenator__app_py -- resolved_imports --> readmenator__resolver_py
    readmenator__app_py -- resolved_imports --> readmenator__watcher_py
    readmenator__app_py -- resolved_imports --> readmenator__video_py
    readmenator__cache_py -- resolved_imports --> readmenator__config_py
    readmenator__cpg_py -- resolved_imports --> readmenator__models_py
    readmenator__cursorrules_generator_py -- resolved_imports --> readmenator__config_py
    readmenator__cursorrules_generator_py -- resolved_imports --> readmenator__layers_py
    readmenator__cursorrules_generator_py -- resolved_imports --> readmenator__models_py
    readmenator__dataflow_py -- resolved_imports --> readmenator__config_py
    readmenator__dataflow_py -- resolved_imports --> readmenator__models_py
    readmenator__dead_code_py -- resolved_imports --> readmenator__config_py
    readmenator__dead_code_py -- resolved_imports --> readmenator__models_py
    readmenator__diagrams_py -- resolved_imports --> readmenator__config_py
    readmenator__diagrams_py -- resolved_imports --> readmenator__models_py
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
    readmenator__gh_wiki_py -- resolved_imports --> readmenator__config_py
    readmenator__gh_wiki_py -- resolved_imports --> readmenator__gitmeta_py
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
    readmenator__pipeline_py -- resolved_imports --> readmenator__agent_injector_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__agent_output_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__analyzer_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__category_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__config_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__cpg_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__dataflow_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__diagrams_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__documentation_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__exporter_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__gh_wiki_py
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
    readmenator__pipeline_py -- resolved_imports --> readmenator__video_py
    readmenator__pipeline_py -- resolved_imports --> readmenator__wiki_py
    ext_readmenator__app["readmenator._app"]
    class ext_readmenator__app ext;
    readmenator___init___py -.->|imports| ext_readmenator__app
    ext_readmenator__category["readmenator._category"]
    class ext_readmenator__category ext;
    readmenator___init___py -.->|imports| ext_readmenator__category
    ext_readmenator__config["readmenator._config"]
    class ext_readmenator__config ext;
    readmenator___init___py -.->|imports| ext_readmenator__config
    ext_readmenator__diagrams["readmenator._diagrams"]
    class ext_readmenator__diagrams ext;
    readmenator___init___py -.->|imports| ext_readmenator__diagrams
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
    readmenator___main___py -.->|imports| ext_readmenator__config
    readmenator___main___py -.->|imports| ext_readmenator__mcp_server
    readmenator__agent_injector_py -.->|imports| ext___future__
    ext_glob["glob"]
    class ext_glob ext;
    readmenator__agent_injector_py -.->|imports| ext_glob
    ext_importlib_util["importlib.util"]
    class ext_importlib_util ext;
    readmenator__agent_injector_py -.->|imports| ext_importlib_util
    readmenator__agent_injector_py -.->|imports| ext_logging
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    readmenator__agent_injector_py -.->|imports| ext_subprocess
    readmenator__agent_injector_py -.->|imports| ext_sys
    readmenator__agent_injector_py -.->|imports| ext_pathlib
    ext_typing["typing"]
    class ext_typing ext;
    readmenator__agent_injector_py -.->|imports| ext_typing
    readmenator__agent_output_py -.->|imports| ext___future__
    ext_json["json"]
    class ext_json ext;
    readmenator__agent_output_py -.->|imports| ext_json
    readmenator__agent_output_py -.->|imports| ext_logging
    ext_os["os"]
    class ext_os ext;
    readmenator__agent_output_py -.->|imports| ext_os
    ext_re["re"]
    class ext_re ext;
    readmenator__agent_output_py -.->|imports| ext_re
    ext_time["time"]
    class ext_time ext;
    readmenator__agent_output_py -.->|imports| ext_time
    ext_collections["collections"]
    class ext_collections ext;
    readmenator__agent_output_py -.->|imports| ext_collections
    readmenator__agent_output_py -.->|imports| ext_pathlib
    readmenator__agent_output_py -.->|imports| ext_typing
    ext_readmenator__cache["readmenator._cache"]
    class ext_readmenator__cache ext;
    readmenator__agent_output_py -.->|imports| ext_readmenator__cache
    readmenator__agent_output_py -.->|imports| ext_readmenator__config
    ext_readmenator__gitmeta["readmenator._gitmeta"]
    class ext_readmenator__gitmeta ext;
    readmenator__agent_output_py -.->|imports| ext_readmenator__gitmeta
    readmenator__agent_output_py -.->|imports| ext_readmenator__models
    ext_readmenator__purpose["readmenator._purpose"]
    class ext_readmenator__purpose ext;
    readmenator__agent_output_py -.->|imports| ext_readmenator__purpose
    ext_readmenator__resolver["readmenator._resolver"]
    class ext_readmenator__resolver ext;
    readmenator__agent_output_py -.->|imports| ext_readmenator__resolver
    ext_readmenator__security["readmenator._security"]
    class ext_readmenator__security ext;
    readmenator__agent_output_py -.->|imports| ext_readmenator__security
    readmenator__analyzer_py -.->|imports| ext___future__
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    readmenator__analyzer_py -.->|imports| ext_hashlib
    ext_math["math"]
    class ext_math ext;
    readmenator__analyzer_py -.->|imports| ext_math
    ext_random["random"]
    class ext_random ext;
    readmenator__analyzer_py -.->|imports| ext_random
    readmenator__analyzer_py -.->|imports| ext_collections
    readmenator__analyzer_py -.->|imports| ext_typing
    readmenator__analyzer_py -.->|imports| ext_readmenator__config
    readmenator__analyzer_py -.->|imports| ext_readmenator__models
    readmenator__app_py -.->|imports| ext___future__
    readmenator__app_py -.->|imports| ext_json
    readmenator__app_py -.->|imports| ext_logging
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    readmenator__app_py -.->|imports| ext_dataclasses
    readmenator__app_py -.->|imports| ext_pathlib
    readmenator__app_py -.->|imports| ext_typing
    readmenator__app_py -.->|imports| ext_readmenator__cache
    readmenator__app_py -.->|imports| ext_readmenator__config
    ext_readmenator__cursorrules_generator["readmenator._cursorrules_generator"]
    class ext_readmenator__cursorrules_generator ext;
    readmenator__app_py -.->|imports| ext_readmenator__cursorrules_generator
    ext_readmenator__dead_code["readmenator._dead_code"]
    class ext_readmenator__dead_code ext;
    readmenator__app_py -.->|imports| ext_readmenator__dead_code
    readmenator__app_py -.->|imports| ext_readmenator__diagrams
    ext_readmenator__gh_wiki["readmenator._gh_wiki"]
    class ext_readmenator__gh_wiki ext;
    readmenator__app_py -.->|imports| ext_readmenator__gh_wiki
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
    readmenator__app_py -.->|imports| ext_readmenator__resolver
    ext_readmenator__watcher["readmenator._watcher"]
    class ext_readmenator__watcher ext;
    readmenator__app_py -.->|imports| ext_readmenator__watcher
    ext_readmenator__video["readmenator._video"]
    class ext_readmenator__video ext;
    readmenator__app_py -.->|imports| ext_readmenator__video
    readmenator__cache_py -.->|imports| ext___future__
    readmenator__cache_py -.->|imports| ext_hashlib
    readmenator__cache_py -.->|imports| ext_json
    readmenator__cache_py -.->|imports| ext_os
    readmenator__cache_py -.->|imports| ext_pathlib
    readmenator__cache_py -.->|imports| ext_typing
    readmenator__cache_py -.->|imports| ext_readmenator__config
    readmenator__category_py -.->|imports| ext___future__
    readmenator__category_py -.->|imports| ext_dataclasses
    ext_enum["enum"]
    class ext_enum ext;
    readmenator__category_py -.->|imports| ext_enum
    readmenator__category_py -.->|imports| ext_typing
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
    readmenator__dataflow_py -.->|imports| ext___future__
    readmenator__dataflow_py -.->|imports| ext_logging
    readmenator__dataflow_py -.->|imports| ext_re
    readmenator__dataflow_py -.->|imports| ext_typing
    readmenator__dataflow_py -.->|imports| ext_readmenator__config
    readmenator__dataflow_py -.->|imports| ext_readmenator__models
    readmenator__dead_code_py -.->|imports| ext___future__
    readmenator__dead_code_py -.->|imports| ext_collections
    readmenator__dead_code_py -.->|imports| ext_typing
    readmenator__dead_code_py -.->|imports| ext_readmenator__config
    readmenator__dead_code_py -.->|imports| ext_readmenator__models
    readmenator__diagrams_py -.->|imports| ext___future__
    ext_html["html"]
    class ext_html ext;
    readmenator__diagrams_py -.->|imports| ext_html
    readmenator__diagrams_py -.->|imports| ext_json
    readmenator__diagrams_py -.->|imports| ext_dataclasses
    readmenator__diagrams_py -.->|imports| ext_pathlib
    readmenator__diagrams_py -.->|imports| ext_typing
    readmenator__diagrams_py -.->|imports| ext_readmenator__config
    readmenator__diagrams_py -.->|imports| ext_readmenator__models
    ext_shutil["shutil"]
    class ext_shutil ext;
    readmenator__diagrams_py -.->|imports| ext_shutil
    readmenator__documentation_py -.->|imports| ext___future__
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
    readmenator__gh_wiki_py -.->|imports| ext___future__
    readmenator__gh_wiki_py -.->|imports| ext_logging
    ext_posixpath["posixpath"]
    class ext_posixpath ext;
    readmenator__gh_wiki_py -.->|imports| ext_posixpath
    readmenator__gh_wiki_py -.->|imports| ext_re
    readmenator__gh_wiki_py -.->|imports| ext_shutil
    readmenator__gh_wiki_py -.->|imports| ext_subprocess
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    readmenator__gh_wiki_py -.->|imports| ext_tempfile
    readmenator__gh_wiki_py -.->|imports| ext_dataclasses
    readmenator__gh_wiki_py -.->|imports| ext_pathlib
    readmenator__gh_wiki_py -.->|imports| ext_typing
    readmenator__gh_wiki_py -.->|imports| ext_readmenator__config
    readmenator__gh_wiki_py -.->|imports| ext_readmenator__gitmeta
    readmenator__gitmeta_py -.->|imports| ext___future__
    readmenator__gitmeta_py -.->|imports| ext_pathlib
    readmenator__gitmeta_py -.->|imports| ext_typing
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
    readmenator__layers_py -.->|imports| ext_re
    readmenator__layers_py -.->|imports| ext_collections
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
    readmenator__mermaid_py -.->|imports| ext_re
    readmenator__mermaid_py -.->|imports| ext_typing
    readmenator__mermaid_py -.->|imports| ext_readmenator__models
    readmenator__models_py -.->|imports| ext___future__
    readmenator__models_py -.->|imports| ext_dataclasses
    readmenator__models_py -.->|imports| ext_typing
    readmenator__models_py -.->|imports| ext_readmenator__category
    readmenator__pipeline_py -.->|imports| ext___future__
    readmenator__pipeline_py -.->|imports| ext_typing
    ext_readmenator__agent_injector["readmenator._agent_injector"]
    class ext_readmenator__agent_injector ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__agent_injector
    ext_readmenator__agent_output["readmenator._agent_output"]
    class ext_readmenator__agent_output ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__agent_output
    ext_readmenator__analyzer["readmenator._analyzer"]
    class ext_readmenator__analyzer ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__analyzer
    readmenator__pipeline_py -.->|imports| ext_readmenator__category
    readmenator__pipeline_py -.->|imports| ext_readmenator__config
    readmenator__pipeline_py -.->|imports| ext_readmenator__cpg
    ext_readmenator__dataflow["readmenator._dataflow"]
    class ext_readmenator__dataflow ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__dataflow
    readmenator__pipeline_py -.->|imports| ext_readmenator__diagrams
    ext_readmenator__documentation["readmenator._documentation"]
    class ext_readmenator__documentation ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__documentation
    ext_readmenator__exporter["readmenator._exporter"]
    class ext_readmenator__exporter ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__exporter
    readmenator__pipeline_py -.->|imports| ext_readmenator__gh_wiki
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
    readmenator__pipeline_py -.->|imports| ext_readmenator__security
    ext_readmenator__taint["readmenator._taint"]
    class ext_readmenator__taint ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__taint
    readmenator__pipeline_py -.->|imports| ext_readmenator__uml
    readmenator__pipeline_py -.->|imports| ext_readmenator__video
    ext_readmenator__wiki["readmenator._wiki"]
    class ext_readmenator__wiki ext;
    readmenator__pipeline_py -.->|imports| ext_readmenator__wiki
    readmenator__projections_py -.->|imports| ext___future__
    readmenator__projections_py -.->|imports| ext_typing
    readmenator__projections_py -.->|imports| ext_readmenator__category
    readmenator__projections_py -.->|imports| ext_readmenator__models
    readmenator__purpose_py -.->|imports| ext___future__
    readmenator__purpose_py -.->|imports| ext_re
    readmenator__purpose_py -.->|imports| ext_typing
    readmenator__purpose_py -.->|imports| ext_readmenator__models
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
    readmenator__resolver_py -.->|imports| ext_posixpath
    readmenator__resolver_py -.->|imports| ext_re
    readmenator__resolver_py -.->|imports| ext_pathlib
    readmenator__resolver_py -.->|imports| ext_typing
    readmenator__resolver_py -.->|imports| ext_readmenator__config
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
    readmenator__video_py -.->|imports| ext___future__
    ext_colorsys["colorsys"]
    class ext_colorsys ext;
    readmenator__video_py -.->|imports| ext_colorsys
    readmenator__video_py -.->|imports| ext_hashlib
    readmenator__video_py -.->|imports| ext_math
    ext_multiprocessing["multiprocessing"]
    class ext_multiprocessing ext;
    readmenator__video_py -.->|imports| ext_multiprocessing
    readmenator__video_py -.->|imports| ext_os
    readmenator__video_py -.->|imports| ext_shutil
    readmenator__video_py -.->|imports| ext_subprocess
    readmenator__video_py -.->|imports| ext_dataclasses
    readmenator__video_py -.->|imports| ext_pathlib
    readmenator__video_py -.->|imports| ext_typing
    readmenator__video_py -.->|imports| ext_readmenator__config
    readmenator__video_py -.->|imports| ext_readmenator__models
    ext_PIL["PIL"]
    class ext_PIL ext;
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__video_py -.->|imports| ext_PIL
    ext_networkx["networkx"]
    class ext_networkx ext;
    readmenator__video_py -.->|imports| ext_networkx
    readmenator__video_py -.->|imports| ext_PIL
    readmenator__watcher_py -.->|imports| ext___future__
    readmenator__watcher_py -.->|imports| ext_hashlib
    readmenator__watcher_py -.->|imports| ext_logging
    readmenator__watcher_py -.->|imports| ext_time
    readmenator__watcher_py -.->|imports| ext_pathlib
    readmenator__watcher_py -.->|imports| ext_typing
    readmenator__watcher_py -.->|imports| ext_readmenator__config
    readmenator__wiki_py -.->|imports| ext___future__
    readmenator__wiki_py -.->|imports| ext_json
    readmenator__wiki_py -.->|imports| ext_logging
    readmenator__wiki_py -.->|imports| ext_os
    readmenator__wiki_py -.->|imports| ext_re
    readmenator__wiki_py -.->|imports| ext_time
    readmenator__wiki_py -.->|imports| ext_collections
    readmenator__wiki_py -.->|imports| ext_pathlib
    readmenator__wiki_py -.->|imports| ext_typing
    readmenator__wiki_py -.->|imports| ext_readmenator__config
    readmenator__wiki_py -.->|imports| ext_readmenator__analyzer
    readmenator__wiki_py -.->|imports| ext_readmenator__models
    readmenator__wiki_py -.->|imports| ext_readmenator__purpose
    readmenator__wiki_py -.->|imports| ext_readmenator__purpose
    readmenator__wiki_py -.->|imports| ext_readmenator__purpose
    readmenator__wiki_py -.->|imports| ext_readmenator__security
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
    readmenator_orchestrator_py -.->|imports| ext_shutil
    readmenator_orchestrator_py -.->|imports| ext_subprocess
    readmenator_orchestrator_py -.->|imports| ext_sys
    readmenator_orchestrator_py -.->|imports| ext_tempfile
    readmenator_orchestrator_py -.->|imports| ext_unittest
    readmenator_orchestrator_py -.->|imports| ext_dataclasses
    ext_datetime["datetime"]
    class ext_datetime ext;
    readmenator_orchestrator_py -.->|imports| ext_datetime
    readmenator_orchestrator_py -.->|imports| ext_pathlib
    readmenator_orchestrator_py -.->|imports| ext_typing
    tests_test_agent_friendliness_py -.->|imports| ext_json
    tests_test_agent_friendliness_py -.->|imports| ext_os
    tests_test_agent_friendliness_py -.->|imports| ext_tempfile
    tests_test_agent_friendliness_py -.->|imports| ext_unittest
    tests_test_agent_friendliness_py -.->|imports| ext_dataclasses
    tests_test_agent_friendliness_py -.->|imports| ext_pathlib
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__agent_output
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__config
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__diagrams
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__gitmeta
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__layers
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__models
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__purpose
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__resolver
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__scanner
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__analyzer
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__cache
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__app
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__analyzer
    tests_test_agent_friendliness_py -.->|imports| ext_readmenator__analyzer
    tests_test_agent_injector_py -.->|imports| ext___future__
    tests_test_agent_injector_py -.->|imports| ext_shutil
    tests_test_agent_injector_py -.->|imports| ext_tempfile
    tests_test_agent_injector_py -.->|imports| ext_unittest
    tests_test_agent_injector_py -.->|imports| ext_pathlib
    ext_unittest_mock["unittest.mock"]
    class ext_unittest_mock ext;
    tests_test_agent_injector_py -.->|imports| ext_unittest_mock
    tests_test_agent_injector_py -.->|imports| ext_readmenator__agent_injector
    tests_test_agent_injector_py -.->|imports| ext_readmenator__agent_injector
    tests_test_agent_output_py -.->|imports| ext_os
    tests_test_agent_output_py -.->|imports| ext_unittest
    tests_test_agent_output_py -.->|imports| ext_pathlib
    tests_test_agent_output_py -.->|imports| ext_unittest_mock
    tests_test_agent_output_py -.->|imports| ext_readmenator__agent_output
    tests_test_agent_output_py -.->|imports| ext_readmenator__config
    tests_test_agent_output_py -.->|imports| ext_readmenator__models
    tests_test_agent_output_py -.->|imports| ext_dataclasses
    tests_test_agent_output_py -.->|imports| ext_readmenator__models
    tests_test_agent_output_py -.->|imports| ext_readmenator__models
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_readmenator__models
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_json
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_readmenator__agent_injector
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_readmenator__agent_injector
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_readmenator__readme_injector
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_agent_output_py -.->|imports| ext_readmenator__readme_injector
    tests_test_agent_output_py -.->|imports| ext_tempfile
    tests_test_analyzer_py -.->|imports| ext___future__
    tests_test_analyzer_py -.->|imports| ext_unittest
    tests_test_analyzer_py -.->|imports| ext_readmenator__analyzer
    tests_test_analyzer_py -.->|imports| ext_readmenator__config
    tests_test_analyzer_py -.->|imports| ext_readmenator__models
    tests_test_analyzer_py -.->|imports| ext_readmenator__analyzer
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
    tests_test_dataflow_py -.->|imports| ext_unittest
    tests_test_dataflow_py -.->|imports| ext_readmenator__config
    tests_test_dataflow_py -.->|imports| ext_readmenator__dataflow
    tests_test_dataflow_py -.->|imports| ext_readmenator__models
    tests_test_dataflow_py -.->|imports| ext_dataclasses
    tests_test_dataflow_py -.->|imports| ext_readmenator__models
    tests_test_dataflow_py -.->|imports| ext_readmenator__models
    tests_test_dead_code_py -.->|imports| ext___future__
    tests_test_dead_code_py -.->|imports| ext_unittest
    tests_test_dead_code_py -.->|imports| ext_readmenator__config
    tests_test_dead_code_py -.->|imports| ext_readmenator__dead_code
    tests_test_dead_code_py -.->|imports| ext_readmenator__models
    tests_test_diagrams_py -.->|imports| ext___future__
    tests_test_diagrams_py -.->|imports| ext_json
    tests_test_diagrams_py -.->|imports| ext_re
    tests_test_diagrams_py -.->|imports| ext_unittest
    tests_test_diagrams_py -.->|imports| ext_pathlib
    tests_test_diagrams_py -.->|imports| ext_readmenator__config
    tests_test_diagrams_py -.->|imports| ext_readmenator__diagrams
    tests_test_diagrams_py -.->|imports| ext_readmenator__models
    tests_test_diagrams_py -.->|imports| ext_readmenator__diagrams
    tests_test_diagrams_py -.->|imports| ext_re
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_dataclasses
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_dataclasses
    tests_test_diagrams_py -.->|imports| ext_dataclasses
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_readmenator__app
    tests_test_diagrams_py -.->|imports| ext_tempfile
    tests_test_diagrams_py -.->|imports| ext_dataclasses
    tests_test_diagrams_py -.->|imports| ext_readmenator__app
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
    tests_test_gh_wiki_py -.->|imports| ext_subprocess
    tests_test_gh_wiki_py -.->|imports| ext_tempfile
    tests_test_gh_wiki_py -.->|imports| ext_unittest
    tests_test_gh_wiki_py -.->|imports| ext_dataclasses
    tests_test_gh_wiki_py -.->|imports| ext_pathlib
    tests_test_gh_wiki_py -.->|imports| ext_typing
    tests_test_gh_wiki_py -.->|imports| ext_readmenator__config
    tests_test_gh_wiki_py -.->|imports| ext_readmenator__gh_wiki
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
    tests_test_video_py -.->|imports| ext_unittest
    tests_test_video_py -.->|imports| ext_readmenator__config
    tests_test_video_py -.->|imports| ext_readmenator__models
    tests_test_video_py -.->|imports| ext_readmenator__video
    tests_test_video_py -.->|imports| ext_hashlib
    tests_test_video_py -.->|imports| ext_pathlib
    tests_test_video_py -.->|imports| ext_readmenator__app
    tests_test_wiki_py -.->|imports| ext_json
    tests_test_wiki_py -.->|imports| ext_os
    tests_test_wiki_py -.->|imports| ext_tempfile
    tests_test_wiki_py -.->|imports| ext_unittest
    tests_test_wiki_py -.->|imports| ext_pathlib
    tests_test_wiki_py -.->|imports| ext_readmenator__config
    tests_test_wiki_py -.->|imports| ext_readmenator__models
    tests_test_wiki_py -.->|imports| ext_readmenator__wiki
    tests_test_wiki_py -.->|imports| ext_dataclasses
    tests_test_wiki_py -.->|imports| ext_readmenator__wiki
    tests_test_wiki_py -.->|imports| ext_readmenator__models
    tests_test_wiki_py -.->|imports| ext_readmenator__wiki
```

---

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class _agent_injector_py_AgentInjector {
    <<class>>
    +ensure_readmenator_installed()
    +__init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)
    +inject(self, project_root)
    +remove(self, project_root)
    +find_agent_files(self, project_root)
    +_find_agent_files(self, root)
    +_inject_single(self, path)
    +_extract_current_injection(content)
    +_remove_old_injection(content)
    +_remove_single(self, path)
  }
  class _agent_output_py_AgentOutputGenerator {
    <<class>>
    +__init__(self, config)
    +generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)
    +_infer_subsystems(self, nodes)
    +_build_index(self, nodes, subsystems, imported_by)
    +_build_architecture(self, edges, resolved_edges, nodes)
    +_build_security(self, findings, nodes)
    +_enclosing_symbol(symbols, line)
    +_is_public(self, sym)
    +_qualified_names(symbols)
    +_build_api(self, nodes, resolved_map, imported_by, layers)
  }
  class _analyzer_py_GraphAnalyzer {
    <<class>>
    +dominant_directory(file_ids)
    +__init__(self, config)
    +analyze(self, nodes, edges, resolved_edges)
    +_build_adjacency(self, nodes, edges)
    +_build_reverse_adjacency(self, adjacency)
    +_compute_god_nodes(self, nodes, adjacency, reverse_adjacency)
    +_detect_communities(self, nodes, adjacency)
    +_merge_small_communities(self, groups, adjacency, weights)
    +_vote_weights(self, file_ids, adjacency)
    +_label_communities(self, nodes, communities)
  }
  class _app_py_readmenatorApplication {
    <<class>>
    +__init__(self, config)
    +_scan(self, target_dir)
    +_scan_with_content(self, target_dir)
    +_resolve_imports(self, nodes, edges, target_dir)
    +run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)
    +check_freshness(self, target_dir)
    +_maybe_refresh_pages(self, root)
    +_maybe_publish_github_wiki(self, root)
    +publish_github_wiki(self, target_dir, dry_run)
    +_write_sidecar_outputs(self, root, findings, analysis_v2)
  }
  class _cache_py_FileCache {
    <<class>>
    +source_fingerprint(project_root, file_ids)
    +__init__(self, config, project_root)
    +load(self)
    +save(self, hashes)
    +compute_hash(self, file_path)
    +compute_hashes(self, file_paths)
    +find_changed(self, file_paths)
    +prune_deleted(self, current_file_ids)
    +save_analysis(self, key, data)
    +load_analysis(self, key)
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
  class _dataflow_py_DataflowAnalyzer {
    <<class>>
    +_strip_noise(line)
    +_strip_block_comments(content)
    +_strip_sizeof(line)
    +_blank(match)
    +__init__(self, config)
    +analyze(self, nodes, content_map)
    +_brace_depths(lines)
    +_function_spans(self, node, total_lines, depths)
    +_analyze_function(self, file_id, func, lines, start, end)
    +_scan_reads(text, lineno, reads, assigned, declared_names)
  }
  class _dead_code_py_DeadCodeStripper {
    <<class>>
    +__init__(self, config)
    +identify(self, nodes, edges, resolved_edges)
    +_build_in_degree_map(self, nodes, resolved_edges)
    +_classify_recommendation(self, symbol)
  }
  class _diagrams_py_MapNode {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_MapEdge {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_MapView {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_SystemMap {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_MapDiagnostic {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_MapReceipt {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_MapDelta {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_SystemMapValidator {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_SystemMapBuilder {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_InteractiveMapRenderer {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_VisNetworkRenderer {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
  }
  class _diagrams_py_DocsSitePublisher {
    <<class>>
    +_escape_markup(value)
    +_json_payload(payload)
    +_role_color(role, config)
    +__init__(self, config)
    +_effective_canvas(self, system_map)
    +validate(self, system_map)
    +__init__(self, config)
    +supported_kinds(self)
    +_is_full(self, full)
    +build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)
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
  class _gh_wiki_py_WikiPublishResult {
    <<class>>
    +__init__(self, config, runner)
    +page_name(self, rel_path)
    +collect_sources(self, project_root)
    +_blob_base(self, remote, commit)
    +rewrite(self, text, rel_path, names, project_root, blob_base)
    +render(self, project_root, remote)
    +_fallback_home(self, project_name)
    +_sidebar(self, names)
    +_footer(git)
    +wiki_remote(self, project_root)
  }
  class _gh_wiki_py_GitHubWikiPublisher {
    <<class>>
    +__init__(self, config, runner)
    +page_name(self, rel_path)
    +collect_sources(self, project_root)
    +_blob_base(self, remote, commit)
    +rewrite(self, text, rel_path, names, project_root, blob_base)
    +render(self, project_root, remote)
    +_fallback_home(self, project_name)
    +_sidebar(self, names)
    +_footer(git)
    +wiki_remote(self, project_root)
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
    +_path_tokens(cls, node_id)
    +_pattern_hits(cls, pattern, tokens, joined)
    +_import_roots(cls, imports)
    +_classify_file(self, node, edges, imports)
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
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [{"cohesion": 0.55, "id": 0, "label": "readmenator: _diagrams", "size": 50}, {"cohesion": 0.286, "id": 1, "label": "tests: _agent_injector", "size": 3}, {"cohesion": 0.351, "id": 2, "label": "readmenator: _agent_output", "size": 10}, {"cohesion": 0.421, "id": 3, "label": "readmenator: _category", "size": 5}, {"cohesion": 0.231, "id": 4, "label": "readmenator: _documentation", "size": 4}, {"cohesion": 0.562, "id": 5, "label": "readmenator/parsers", "size": 26}, {"cohesion": 0.211, "id": 6, "label": "tests: _scanner", "size": 5}], "god_nodes": [{"node_id": "readmenator/_models.py", "score": 160.0}, {"node_id": "readmenator/_config.py", "score": 122.1}, {"node_id": "readmenator/_pipeline.py", "score": 55.4}, {"node_id": "readmenator/_app.py", "score": 53.0}, {"node_id": "readmenator/parsers/__init__.py", "score": 48.2}, {"node_id": "readmenator/parsers/_base.py", "score": 44.6}, {"node_id": "tests/test_parsers_property.py", "score": 42.7}, {"node_id": "tests/test_agent_friendliness.py", "score": 28.3}, {"node_id": "readmenator/_agent_output.py", "score": 23.2}, {"node_id": "readmenator/_diagrams.py", "score": 21.9}], "surprising_connections": [{"hops": 5, "source": "readmenator.py", "target": "tests/test_agent_injector.py"}, {"hops": 5, "source": "tests/test_agent_injector.py", "target": "tests/test_resolver.py"}, {"hops": 5, "source": "tests/test_readme_injector.py", "target": "tests/test_resolver.py"}, {"hops": 4, "source": "readmenator/__init__.py", "target": "tests/test_agent_injector.py"}, {"hops": 4, "source": "readmenator/__main__.py", "target": "tests/test_agent_injector.py"}]}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._diagrams"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._mcp_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__init__.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/__main__.py", "target": "readmenator._mcp_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_injector.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._gitmeta"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._purpose"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_agent_output.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "random"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_analyzer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._cursorrules_generator"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._dead_code"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._diagrams"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._gh_wiki"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._linter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._pipeline"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._refactorizer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._watcher"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_app.py", "target": "readmenator._video"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cache.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_category.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_config.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cpg.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dataflow.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dataflow.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dataflow.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dataflow.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dataflow.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dataflow.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_dead_code.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "html"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_diagrams.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._mermaid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_documentation.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_explain.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "textwrap"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_exporter.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "posixpath"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gh_wiki.py", "target": "readmenator._gitmeta"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gitmeta.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gitmeta.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_gitmeta.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_hotspots.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layer_rules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_layers.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_linter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mcp_server.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_mermaid.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_models.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._agent_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._agent_output"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._dataflow"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._diagrams"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._documentation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._exporter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._gh_wiki"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._hotspots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._layer_rules"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._rule_gen"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._sarif"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._video"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_pipeline.py", "target": "readmenator._wiki"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_projections.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_purpose.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_purpose.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_purpose.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_purpose.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_query.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rank.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_readme_injector.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "posixpath"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_resolver.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_rule_gen.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_sarif.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_scanner.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_security.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_taint.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_uml.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "colorsys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "multiprocessing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "networkx"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_video.py", "target": "PIL"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_watcher.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._purpose"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._purpose"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._purpose"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/_wiki.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._c"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._python"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._go"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._rust"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._javascript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._java"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._csharp"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._shell"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._php"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._dart"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._gdscript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._nim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._assembly"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._ruby"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._swift"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._kotlin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._scala"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._lua"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator.parsers._elixir"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_assembly.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_base.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_c.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_csharp.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_dart.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_elixir.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_gdscript.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_go.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_java.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_javascript.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_kotlin.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_lua.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_nim.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_php.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "ast"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_python.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_ruby.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_rust.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_scala.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_shell.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator.parsers._base"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator/parsers/_swift.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator.py", "target": "readmenator.__main__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "shlex"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "readmenator_orchestrator.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._agent_output"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._diagrams"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._gitmeta"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._layers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._purpose"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "unittest.mock"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "readmenator._agent_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_injector.py", "target": "readmenator._agent_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "unittest.mock"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._agent_output"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._agent_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._agent_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_agent_output.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_analyzer.py", "target": "readmenator._analyzer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "readmenator._cache"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cache.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_config.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._cpg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cpg.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "readmenator._cursorrules_generator"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_cursorrules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "readmenator._dataflow"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dataflow.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "readmenator._dead_code"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_dead_code.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "readmenator._diagrams"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "readmenator._diagrams"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_diagrams.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._documentation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_documentation.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._exporter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_exporter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_gh_wiki.py", "target": "readmenator._gh_wiki"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._hotspots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_hotspots.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_integration.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._layer_rules"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_layer_rules.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "readmenator._linter"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_linter.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "readmenator._mcp_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mcp_server.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "readmenator._mermaid"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_mermaid.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_models.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_models.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_new.py", "target": "readmenator.parsers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._python"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._c"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._go"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._rust"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._javascript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._java"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._csharp"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._shell"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._php"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._dart"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._gdscript"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._nim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._ruby"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._swift"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._kotlin"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._scala"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._lua"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "readmenator.parsers._elixir"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_parsers_property.py", "target": "hypothesis"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_query.py", "target": "readmenator._query"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._category"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._explain"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._projections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_ranking.py", "target": "readmenator._rank"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "readmenator._readme_injector"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_readme_injector.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._refactorizer"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_refactorizer.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_resolver.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_rule_gen.py", "target": "readmenator._rule_gen"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_sarif.py", "target": "readmenator._sarif"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_scanner.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_security.py", "target": "readmenator._security"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._taint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "pytest_bdd"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._scanner"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "readmenator._resolver"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_taint_bdd.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_uml.py", "target": "readmenator._uml"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "readmenator._video"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_video.py", "target": "readmenator._app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "unittest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "readmenator._config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "readmenator._wiki"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "readmenator._wiki"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "readmenator._models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_wiki.py", "target": "readmenator._wiki"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_diagrams.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_mcp_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__init__.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/__main__.py", "target": "readmenator/_mcp_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_gitmeta.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_purpose.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_agent_output.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_analyzer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_analyzer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_cursorrules_generator.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_dead_code.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_diagrams.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_gh_wiki.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_linter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_pipeline.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_refactorizer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_watcher.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_app.py", "target": "readmenator/_video.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cache.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cpg.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_cursorrules_generator.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_dataflow.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_dataflow.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_dead_code.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_dead_code.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_diagrams.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_diagrams.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_mermaid.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_documentation.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_explain.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_explain.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_exporter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_exporter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_gh_wiki.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_gh_wiki.py", "target": "readmenator/_gitmeta.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_hotspots.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_hotspots.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layer_rules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layer_rules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_layers.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_linter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_linter.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_linter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mcp_server.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_mermaid.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_models.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_agent_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_agent_output.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_dataflow.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_diagrams.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_documentation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_exporter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_gh_wiki.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_hotspots.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_layer_rules.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_rule_gen.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_sarif.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_video.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_pipeline.py", "target": "readmenator/_wiki.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_projections.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_projections.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_purpose.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_query.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rank.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_refactorizer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_resolver.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rule_gen.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_rule_gen.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_sarif.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_scanner.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_security.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_security.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_taint.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_taint.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_uml.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_uml.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_video.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_video.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_watcher.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_purpose.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_purpose.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_purpose.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/_wiki.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_c.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_python.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_go.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_rust.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_javascript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_java.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_csharp.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_shell.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_php.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_dart.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_gdscript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_nim.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_assembly.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_ruby.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_swift.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_kotlin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_scala.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_lua.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/__init__.py", "target": "readmenator/parsers/_elixir.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_assembly.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_base.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_base.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_c.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_c.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_csharp.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_dart.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_elixir.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_gdscript.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_go.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_go.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_java.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_java.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_javascript.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_kotlin.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_lua.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_nim.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_php.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_php.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_python.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_python.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_ruby.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_rust.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_scala.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_shell.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator/parsers/_base.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator/parsers/_swift.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "readmenator.py", "target": "readmenator/__main__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_agent_output.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_diagrams.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_gitmeta.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_layers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_purpose.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_friendliness.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_injector.py", "target": "readmenator/_agent_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_injector.py", "target": "readmenator/_agent_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_agent_output.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_agent_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_agent_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_agent_output.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_analyzer.py", "target": "readmenator/_analyzer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cache.py", "target": "readmenator/_cache.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cache.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_config.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_cpg.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cpg.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cursorrules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cursorrules.py", "target": "readmenator/_cursorrules_generator.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_cursorrules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dataflow.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dataflow.py", "target": "readmenator/_dataflow.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dataflow.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dataflow.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dataflow.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dead_code.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dead_code.py", "target": "readmenator/_dead_code.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_dead_code.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_diagrams.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_diagrams.py", "target": "readmenator/_diagrams.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_diagrams.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_diagrams.py", "target": "readmenator/_diagrams.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_diagrams.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_diagrams.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_documentation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_documentation.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_exporter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_exporter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_gh_wiki.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_gh_wiki.py", "target": "readmenator/_gh_wiki.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_hotspots.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_hotspots.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integration.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_integration.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_layer_rules.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_layer_rules.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_linter.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_linter.py", "target": "readmenator/_linter.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_linter.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mcp_server.py", "target": "readmenator/_mcp_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mcp_server.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mcp_server.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mermaid.py", "target": "readmenator/_mermaid.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_mermaid.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_models.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_new.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_new.py", "target": "readmenator/parsers/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_python.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_c.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_go.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_rust.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_javascript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_java.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_csharp.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_shell.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_php.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_dart.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_gdscript.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_nim.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_ruby.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_swift.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_kotlin.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_scala.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_lua.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_parsers_property.py", "target": "readmenator/parsers/_elixir.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_query.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_query.py", "target": "readmenator/_query.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_category.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_explain.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_projections.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_ranking.py", "target": "readmenator/_rank.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_readme_injector.py", "target": "readmenator/_readme_injector.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_refactorizer.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_refactorizer.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_resolver.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_rule_gen.py", "target": "readmenator/_rule_gen.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_sarif.py", "target": "readmenator/_sarif.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_scanner.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_security.py", "target": "readmenator/_security.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_taint.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_scanner.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_taint_bdd.py", "target": "readmenator/_resolver.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_uml.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_uml.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_uml.py", "target": "readmenator/_uml.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_video.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_video.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_video.py", "target": "readmenator/_video.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_video.py", "target": "readmenator/_app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_wiki.py", "target": "readmenator/_config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_wiki.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_wiki.py", "target": "readmenator/_wiki.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_wiki.py", "target": "readmenator/_wiki.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_wiki.py", "target": "readmenator/_models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_wiki.py", "target": "readmenator/_wiki.py"}], "generator": "readmenator", "metadata": {"edge_count": 12517, "file_count": 105, "language_count": 1, "symbol_count": 1852}, "nodes": [{"doc": "ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApplication provide the complete toolkit for generating, querying, ranking, and UML diagramming codebase knowledge graphs without any LLM calls or cloud dependencies.", "id": "readmenator/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "693c306a8ca0b67d", "symbol_count": 0, "symbols": []}, {"doc": "Command line entry point: argument parsing and subcommand dispatch.", "id": "readmenator/__main__.py", "kind": "module", "label": "__main__.py", "language": "py", "sha256": "826dfe84833490c8", "symbol_count": 3, "symbols": [{"kind": "function", "line": 18, "name": "build_parser", "signature": "def build_parser()"}, {"kind": "function", "line": 121, "name": "_run_tests", "signature": "def _run_tests()"}, {"kind": "function", "line": 136, "name": "main", "signature": "def main()"}]}, {"doc": "Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects common AI agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules, etc.) and appends a pointer to KNOWLEDGE_BASE.md so that agents can discover project context quickly without manual setup.  The injected text includes instructions for the agent to regenerate KNOWLEDGE_BASE.md by running readmenator when needed.", "id": "readmenator/_agent_injector.py", "kind": "module", "label": "_agent_injector.py", "language": "py", "sha256": "5def5d7a5f853501", "symbol_count": 14, "symbols": [{"doc": "Check if readmenator is installed via pip; install it if missing.\n\nReturns True if readmenator is available after the check.", "kind": "function", "line": 101, "name": "ensure_readmenator_installed", "signature": "def ensure_readmenator_installed()"}, {"doc": "Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.\n\nDetects common AI agent configuration files (AGENTS.md, CLAUDE.md,\n.cursorrules, etc.) and appends a descriptive section pointing to\nthe knowledge base so agents discover it automatically.\n\nThe injected text instructs the agent how to regenerate the KB\nby running readmenator when needed.", "kind": "class", "line": 123, "name": "AgentInjector", "signature": "class AgentInjector"}, {"kind": "method", "line": 134, "name": "__init__", "signature": "def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)"}, {"doc": "Inject KB reference into all discovered agent files.\n\nReturns the number of agent files actually modified.", "kind": "method", "line": 148, "name": "inject", "signature": "def inject(self, project_root)"}, {"doc": "Remove KB injection from all discovered agent files.\n\nReturns the number of files actually modified.", "kind": "method", "line": 166, "name": "remove", "signature": "def remove(self, project_root)"}, {"doc": "Public accessor: return all detected agent files.", "kind": "method", "line": 179, "name": "find_agent_files", "signature": "def find_agent_files(self, project_root)"}, {"kind": "method", "line": 183, "name": "_find_agent_files", "signature": "def _find_agent_files(self, root)"}, {"kind": "method", "line": 197, "name": "_inject_single", "signature": "def _inject_single(self, path)"}, {"kind": "method", "line": 235, "name": "_extract_current_injection", "signature": "def _extract_current_injection(content)"}, {"kind": "method", "line": 244, "name": "_remove_old_injection", "signature": "def _remove_old_injection(content)"}, {"kind": "method", "line": 254, "name": "_remove_single", "signature": "def _remove_single(self, path)"}, {"kind": "method", "line": 270, "name": "_build_injection", "signature": "def _build_injection(self, fmt)"}, {"doc": "Build Cursor .mdc injection body (frontmatter added separately).", "kind": "method", "line": 282, "name": "_build_mdc_injection", "signature": "def _build_mdc_injection(self)"}, {"doc": "Prepend Cursor frontmatter so the rule is auto-attached.", "kind": "method", "line": 287, "name": "_prepend_mdc_frontmatter", "signature": "def _prepend_mdc_frontmatter(content, injection)"}]}, {"doc": "Agent-friendly output generator for ReadMenator.  Generates grep-optimized, flat-markdown files in a dedicated output directory.  File names for per-subsystem files are **inferred** from the project's directory structure, never hardcoded.  The generated files are designed to be consumed by AI agents that perform ``grep`` / ``read`` operations and need queryable, small-context documents.  Every document is capped at ``AGENT_OUTPUT_MAX_LINES``: oversized documents are split on section boundaries into ``NAME.md``, ``NAME_p2.md``, ... with the table header repeated on each page, so a ``grep`` over ``NAME*.md`` still sees every line and a single read never blows an agent's context window.  Output layout::  readmenator-agent/ ├── MANIFEST.json         # freshness (git commit), read order, token costs ├── INDEX.md              # file -> purpose -> blast radius map ├── SYMBOLS.md            # one line per symbol ├── ARCHITECTURE.md       # dependency pairs (flat list) ├── SECURITY.md           # findings by severity ├── API.md                # public functions, one line each ├── GOTCHAS.md            # \"don't change X because Y\" ├── recipes/ │   └── *.md              # actionable task blocks └── KB_<subsystem>.md     # 1 file per inferred subsystem", "id": "readmenator/_agent_output.py", "kind": "module", "label": "_agent_output.py", "language": "py", "sha256": "8ecacdeef8281459", "symbol_count": 32, "symbols": [{"doc": "Generates agent-friendly, grep-optimised output files.\n\nAll output is plain Markdown -- no JSON wrapping, no fenced code\nblocks around data structures.  Every line is greppable.", "kind": "class", "line": 70, "name": "AgentOutputGenerator", "signature": "class AgentOutputGenerator"}, {"doc": "Store configuration for output paths and size budgets.", "kind": "method", "line": 77, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Write all agent output files and return the output directory path.", "kind": "method", "line": 81, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)"}, {"doc": "Group nodes by directory, inferring subsystem names.", "kind": "method", "line": 137, "name": "_infer_subsystems", "signature": "def _infer_subsystems(self, nodes)"}, {"doc": "Build the file -> purpose -> subsystem -> blast radius table.", "kind": "method", "line": 172, "name": "_build_index", "signature": "def _build_index(self, nodes, subsystems, imported_by)"}, {"doc": "Build internal dependency pairs plus per-file external imports.\n\nExternal imports exclude raw import strings that resolved to a\nproject file, so internal modules are never listed twice.", "kind": "method", "line": 204, "name": "_build_architecture", "signature": "def _build_architecture(self, edges, resolved_edges, nodes)"}, {"doc": "Build findings grouped by severity with scope and fix hints.", "kind": "method", "line": 256, "name": "_build_security", "signature": "def _build_security(self, findings, nodes)"}, {"doc": "Return the nearest symbol defined at or before line.", "kind": "method", "line": 292, "name": "_enclosing_symbol", "signature": "def _enclosing_symbol(symbols, line)"}, {"doc": "Return whether a symbol belongs in the public API listing.", "kind": "method", "line": 302, "name": "_is_public", "signature": "def _is_public(self, sym)"}, {"doc": "Map each method's index to ``Owner.method`` using the nearest preceding type.", "kind": "method", "line": 309, "name": "_qualified_names", "signature": "def _qualified_names(symbols)"}, {"doc": "Build one greppable line per public function or method.\n\nDependencies and importers are stated once per file instead of\nonce per function, and test-layer files are skipped, which keeps\nthe listing an API reference rather than a symbol dump.", "kind": "method", "line": 327, "name": "_build_api", "signature": "def _build_api(self, nodes, resolved_map, imported_by, layers)"}, {"doc": "Build MANIFEST.json: freshness, entry points, read order, costs.\n\nThe project root is recorded relatively (never an absolute path),\nand the git commit lets agents detect a stale knowledge base with\none ``git rev-parse HEAD`` instead of re-reading everything.", "kind": "method", "line": 385, "name": "_build_manifest", "signature": "def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root, subsystems, layers, out_dir)"}, {"doc": "Return likely program entry points, shallowest paths first.", "kind": "method", "line": 457, "name": "_entrypoints", "signature": "def _entrypoints(self, nodes, layers)"}, {"doc": "List generated documents with line counts and token estimates.", "kind": "method", "line": 468, "name": "_inventory", "signature": "def _inventory(self, out_dir)"}, {"doc": "Build grep-friendly symbol index (one line per symbol).", "kind": "method", "line": 481, "name": "_build_symbols", "signature": "def _build_symbols(self, nodes)"}, {"doc": "Render a cycle as a closed loop without duplicating a closed tail.", "kind": "method", "line": 496, "name": "_closed_loop", "signature": "def _closed_loop(cycle)"}, {"doc": "Build actionable warnings: blast radius, hotspots, cycles, violations.\n\nFiles in excluded layers (tests by default) are left out of the\ncentrality lists because their connectivity says nothing about\nthe risk of editing production code.", "kind": "method", "line": 503, "name": "_build_gotchas", "signature": "def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)"}, {"doc": "Return a filesystem-safe subsystem name.", "kind": "method", "line": 626, "name": "_safe_name", "signature": "def _safe_name(name)"}, {"doc": "Write one paged KB_<subsystem>.md per inferred subsystem.", "kind": "method", "line": 633, "name": "_write_subsystem_files", "signature": "def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)"}, {"doc": "Build per-file context (purpose, layer, symbols, edges) for one subsystem.", "kind": "method", "line": 648, "name": "_build_subsystem_content", "signature": "def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)"}, {"doc": "Write task recipes grounded in this project's actual analysis data.", "kind": "method", "line": 698, "name": "_write_recipes", "signature": "def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)"}, {"doc": "Index resolved dependencies by source file, sorted and deduplicated.", "kind": "method", "line": 826, "name": "_deps_by_source", "signature": "def _deps_by_source(resolved_map)"}, {"doc": "Map (source, target) pairs to their relation.", "kind": "method", "line": 836, "name": "_build_resolved_map", "signature": "def _build_resolved_map(resolved_edges)"}, {"doc": "Map each file to the files that import it.", "kind": "method", "line": 846, "name": "_build_imported_by_map", "signature": "def _build_imported_by_map(resolved_edges)"}, {"doc": "Return the file name of a page (page 1 keeps the original name).", "kind": "method", "line": 856, "name": "_page_name", "signature": "def _page_name(filename, page)"}, {"doc": "Split a document body into atomic units that should not straddle pages.", "kind": "method", "line": 864, "name": "_split_units", "signature": "def _split_units(body, is_table)"}, {"doc": "Split an oversized unit into budget-sized chunks with continued headings.", "kind": "method", "line": 877, "name": "_chunk_unit", "signature": "def _chunk_unit(unit, budget)"}, {"doc": "Split a document into pages that each respect the line cap.", "kind": "method", "line": 894, "name": "_paginate", "signature": "def _paginate(self, filename, content)"}, {"doc": "Write a document as one or more capped pages and return their paths.", "kind": "method", "line": 933, "name": "_write_paged", "signature": "def _write_paged(self, out_dir, filename, content)"}, {"doc": "Remove previously generated pages so renamed or shrunk docs leave no stale files.", "kind": "method", "line": 943, "name": "_prune_owned", "signature": "def _prune_owned(out_dir)"}, {"doc": "Write UTF-8 text content to a path.", "kind": "method", "line": 950, "name": "_write", "signature": "def _write(path, content)"}, {"doc": "Return whether a file belongs in the gotcha lists.", "kind": "method", "line": 522, "name": "keep", "signature": "def keep(file_id)"}]}, {"doc": "Graph analysis engine for the readmenator knowledge graph.  Provides community detection (Louvain-like greedy modularity), god node identification (degree/PageRank centrality), surprising connection discovery (cross-community bridges), and suggested exploration questions derived from graph structure. All operations are deterministic and token-free.", "id": "readmenator/_analyzer.py", "kind": "module", "label": "_analyzer.py", "language": "py", "sha256": "144a6cbe12268ae6", "symbol_count": 18, "symbols": [{"doc": "Return the most informative directory label for a set of files.\n\nHighest file count wins; ties prefer the longest (most specific)\ndirectory so that ``sandbox`` beats ``.``; remaining ties go\nalphabetical. ``\".\"`` is reported as ``\"root\"``.", "kind": "function", "line": 22, "name": "dominant_directory", "signature": "def dominant_directory(file_ids)"}, {"doc": "Deterministic graph analysis over scanned nodes and edges.\n\nBuilds an internal adjacency graph from import edges, then applies\ncommunity detection, centrality scoring, cross-community bridge\ndiscovery, and question generation without any external API calls.", "kind": "class", "line": 40, "name": "GraphAnalyzer", "signature": "class GraphAnalyzer"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings for thresholds and limits.", "kind": "method", "line": 48, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run the full analysis pipeline and return structured results.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges from the scanner.\n    resolved_edges: Optional list of resolved-import edges (source and\n        target are both project file IDs).\n\nReturns:\n    An AnalysisResult with god nodes, communities, surprising\n    connections, and suggested questions.", "kind": "method", "line": 56, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges)"}, {"doc": "Build an undirected adjacency map from import edges.", "kind": "method", "line": 109, "name": "_build_adjacency", "signature": "def _build_adjacency(self, nodes, edges)"}, {"doc": "Build a directed reverse adjacency (incoming edges) map.", "kind": "method", "line": 123, "name": "_build_reverse_adjacency", "signature": "def _build_reverse_adjacency(self, adjacency)"}, {"doc": "Compute the most central nodes using combined degree centrality.\n\nScore is a combination of out-degree (imports), in-degree (imported-by),\nand symbol count. Higher score means more architecturally significant.", "kind": "method", "line": 133, "name": "_compute_god_nodes", "signature": "def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)"}, {"doc": "Detect communities using label propagation.\n\nEach node adopts the label with the highest weighted vote among\nits neighbors. Iterates until convergence or max iterations reached.\nDeterministic: content-seeded order, sorted neighbors, min-label\ntie-break within COMMUNITY_VOTE_EPSILON.", "kind": "method", "line": 155, "name": "_detect_communities", "signature": "def _detect_communities(self, nodes, adjacency)"}, {"doc": "Fold communities smaller than COMMUNITY_MERGE_BELOW into their best neighbor.\n\nLabel propagation leaves many module-plus-test pairs; each would\nbecome its own wiki page. The smallest group first joins the\nneighboring community it shares the most vote weight with (ties\nto the lowest label). Isolated groups are kept unchanged.", "kind": "method", "line": 217, "name": "_merge_small_communities", "signature": "def _merge_small_communities(self, groups, adjacency, weights)"}, {"doc": "Return each node's label-propagation vote weight.\n\nWith COMMUNITY_HUB_DAMPING a neighbor votes with weight\n``1 / log2(2 + degree)``: hubs such as shared models or config,\nwhich nearly every file imports, stop pulling the whole project\ninto one giant community, while ordinary neighbors keep full say.", "kind": "method", "line": 264, "name": "_vote_weights", "signature": "def _vote_weights(self, file_ids, adjacency)"}, {"doc": "Generate human-readable labels for communities.\n\nLabels are based on the most common directory within the community.", "kind": "method", "line": 281, "name": "_label_communities", "signature": "def _label_communities(self, nodes, communities)"}, {"doc": "Return the stem of a community's most symbol-rich non-test file.\n\nUsed to tell apart communities that share a dominant directory,\nso labels read ``pkg: _video`` instead of an opaque number.", "kind": "method", "line": 308, "name": "_core_file", "signature": "def _core_file(members, node_map)"}, {"doc": "Build a reverse map from file ID to community ID.", "kind": "method", "line": 328, "name": "_build_community_map", "signature": "def _build_community_map(self, communities)"}, {"doc": "Compute cohesion score for each community.\n\nCohesion = internal edges / (internal edges + external edges).", "kind": "method", "line": 338, "name": "_compute_cohesion", "signature": "def _compute_cohesion(self, communities, adjacency)"}, {"doc": "Find non-obvious cross-community bridges.\n\nA connection is surprising when two nodes in different communities\nare connected indirectly through 3 or more hops, and the path\ncrosses community boundaries.", "kind": "method", "line": 363, "name": "_find_surprising_connections", "signature": "def _find_surprising_connections(self, nodes, adjacency, community_map)"}, {"doc": "Find the shortest path and communities traversed.", "kind": "method", "line": 403, "name": "_shortest_path_communities", "signature": "def _shortest_path_communities(self, source, target, adjacency, community_map)"}, {"doc": "Generate plain-language exploration questions from graph structure.", "kind": "method", "line": 430, "name": "_suggest_questions", "signature": "def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)"}, {"doc": "Return whether a path looks like a test file.", "kind": "method", "line": 314, "name": "is_test", "signature": "def is_test(fid)"}]}, {"doc": "Application orchestrator: scan, resolve, analyze, and write every output.  Thin facade over AnalyzerFactory that wires the scanner, analyzers, and generators into the run, rebuild, update, query, and export commands.", "id": "readmenator/_app.py", "kind": "module", "label": "_app.py", "language": "py", "sha256": "5b4058a7a430c3f2", "symbol_count": 50, "symbols": [{"kind": "class", "line": 43, "name": "readmenatorApplication", "signature": "class readmenatorApplication"}, {"kind": "method", "line": 44, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 53, "name": "_scan", "signature": "def _scan(self, target_dir)"}, {"kind": "method", "line": 61, "name": "_scan_with_content", "signature": "def _scan_with_content(self, target_dir)"}, {"kind": "method", "line": 71, "name": "_resolve_imports", "signature": "def _resolve_imports(self, nodes, edges, target_dir)"}, {"kind": "method", "line": 90, "name": "run", "signature": "def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)"}, {"doc": "Compare the MANIFEST source fingerprint against the current sources.\n\nArgs:\n    target_dir: Project root directory.\n\nReturns:\n    Tuple of (fresh, human-readable reason).", "kind": "method", "line": 214, "name": "check_freshness", "signature": "def check_freshness(self, target_dir)"}, {"doc": "Refresh the static docs site when a previous ``pages`` run created it.\n\nThe site directory is only rewritten when it already holds a\nreadmenator gallery (index plus maps subdirectory), so a user's own\ndocs folder is never taken over by a plain rebuild.", "kind": "method", "line": 241, "name": "_maybe_refresh_pages", "signature": "def _maybe_refresh_pages(self, root)"}, {"doc": "Publish generated docs to the GitHub wiki when GH_WIKI_ENABLED is set.", "kind": "method", "line": 259, "name": "_maybe_publish_github_wiki", "signature": "def _maybe_publish_github_wiki(self, root)"}, {"doc": "Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.\n\nArgs:\n    target_dir: Project root directory with generated outputs.\n    dry_run: Render pages into GH_WIKI_DRY_RUN_DIR without git calls.\n\nReturns:\n    WikiPublishResult with pages written and push status.", "kind": "method", "line": 265, "name": "publish_github_wiki", "signature": "def publish_github_wiki(self, target_dir, dry_run)"}, {"kind": "method", "line": 279, "name": "_write_sidecar_outputs", "signature": "def _write_sidecar_outputs(self, root, findings, analysis_v2)"}, {"kind": "method", "line": 305, "name": "_inject_readme_link", "signature": "def _inject_readme_link(self, root)"}, {"kind": "method", "line": 313, "name": "_inject_agent_files", "signature": "def _inject_agent_files(self, root)"}, {"kind": "method", "line": 321, "name": "generate_uml_code", "signature": "def generate_uml_code(self, target_dir, language, output_path)"}, {"kind": "method", "line": 333, "name": "_log_summary", "signature": "def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)"}, {"kind": "method", "line": 388, "name": "update", "signature": "def update(self, target_dir, run_security)"}, {"kind": "method", "line": 493, "name": "_scan_for_cache", "signature": "def _scan_for_cache(self, root, cache)"}, {"kind": "method", "line": 511, "name": "query", "signature": "def query(self, target_dir, question)"}, {"kind": "method", "line": 516, "name": "explain", "signature": "def explain(self, target_dir, symbol_name)"}, {"kind": "method", "line": 528, "name": "find_path", "signature": "def find_path(self, target_dir, symbol_a, symbol_b)"}, {"kind": "method", "line": 541, "name": "summary", "signature": "def summary(self, target_dir)"}, {"doc": "Run a ranked query against the knowledge graph.\n\nUses Personalized PageRank seeded from query terms to produce\na relevance-ranked list of files with score decomposition.\n\nArgs:\n    target_dir: Project root directory.\n    query: Free-text query.\n    top_n: Number of results.\n\nReturns:\n    A RankedResult with scored items.", "kind": "method", "line": 546, "name": "rank_query", "signature": "def rank_query(self, target_dir, query, top_n)"}, {"kind": "method", "line": 576, "name": "rebuild", "signature": "def rebuild(self, target_dir, run_security)"}, {"kind": "method", "line": 579, "name": "analyze", "signature": "def analyze(self, target_dir)"}, {"kind": "method", "line": 583, "name": "export_json", "signature": "def export_json(self, target_dir, output_path)"}, {"kind": "method", "line": 594, "name": "export_html", "signature": "def export_html(self, target_dir, output_path)"}, {"kind": "method", "line": 605, "name": "export_svg", "signature": "def export_svg(self, target_dir, output_path)"}, {"kind": "method", "line": 616, "name": "export", "signature": "def export(self, target_dir)"}, {"kind": "method", "line": 621, "name": "export_graphml", "signature": "def export_graphml(self, target_dir, output_path)"}, {"kind": "method", "line": 632, "name": "export_cypher", "signature": "def export_cypher(self, target_dir, output_path)"}, {"kind": "method", "line": 645, "name": "export_obsidian", "signature": "def export_obsidian(self, target_dir, output_dir)"}, {"doc": "Generate the navigable agent wiki for the target project.\n\nArgs:\n    target_dir: Project root directory.\n    output_dir: Optional override for the wiki output directory.\n\nReturns:\n    Path of the wiki directory that was written.", "kind": "method", "line": 655, "name": "export_wiki", "signature": "def export_wiki(self, target_dir, output_dir)"}, {"doc": "Check wiki health and log reported issues.\n\nArgs:\n    target_dir: Project root directory.\n\nReturns:\n    List of issue descriptions, empty when healthy.", "kind": "method", "line": 678, "name": "lint_wiki", "signature": "def lint_wiki(self, target_dir)"}, {"doc": "Export all five interactive system maps plus a gallery index.\n\nArgs:\n    target_dir: Project root directory.\n    output_dir: Destination directory for map files.\n    full: True includes every file with a grown canvas, False truncates.\n\nReturns:\n    Mapping of diagram kind to written file path.", "kind": "method", "line": 696, "name": "export_diagrams", "signature": "def export_diagrams(self, target_dir, output_dir, full)"}, {"doc": "Return the configured map renderer for published output.\n\nReturns:\n    The vis.js renderer when enabled, else the offline renderer.", "kind": "method", "line": 738, "name": "_live_renderer", "signature": "def _live_renderer(self)"}, {"doc": "Export a single interactive system map as standalone HTML.\n\nArgs:\n    target_dir: Project root directory.\n    kind: Diagram kind identifier.\n    output_path: Destination file path.\n    full: True includes every file with a grown canvas, False truncates.\n\nReturns:\n    Rendered HTML document that was written.", "kind": "method", "line": 748, "name": "export_diagram", "signature": "def export_diagram(self, target_dir, kind, output_path, full)"}, {"doc": "Publish all system maps plus a gallery index as a static site.\n\nArgs:\n    target_dir: Project root directory.\n    output_dir: Destination directory for the static site.\n    full: True includes every file with a grown canvas, False truncates.\n\nReturns:\n    Mapping of published page identifier to written file path.", "kind": "method", "line": 787, "name": "export_pages", "signature": "def export_pages(self, target_dir, output_dir, full)"}, {"doc": "Render the cinematic overview video for the target project.\n\nArgs:\n    target_dir: Project root directory.\n    output_path: Destination mp4 path.\n\nReturns:\n    Written file path, or None when video is disabled or skipped.", "kind": "method", "line": 826, "name": "export_video", "signature": "def export_video(self, target_dir, output_path)"}, {"doc": "Render video when enabled, skipping gracefully without deps.", "kind": "method", "line": 850, "name": "_maybe_export_video", "signature": "def _maybe_export_video(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, content_map, output_path)"}, {"kind": "method", "line": 890, "name": "watch", "signature": "def watch(self, target_dir)"}, {"kind": "method", "line": 900, "name": "audit", "signature": "def audit(self, target_dir)"}, {"kind": "method", "line": 907, "name": "audit_deep", "signature": "def audit_deep(self, target_dir)"}, {"kind": "method", "line": 927, "name": "export_sarif", "signature": "def export_sarif(self, target_dir, output_path)"}, {"kind": "method", "line": 937, "name": "export_rules", "signature": "def export_rules(self, target_dir, output_dir)"}, {"kind": "method", "line": 947, "name": "detect_layers", "signature": "def detect_layers(self, target_dir)"}, {"kind": "method", "line": 957, "name": "lint", "signature": "def lint(self, target_dir)"}, {"kind": "method", "line": 970, "name": "strip_dead_code", "signature": "def strip_dead_code(self, target_dir)"}, {"kind": "method", "line": 980, "name": "generate_cursorrules", "signature": "def generate_cursorrules(self, target_dir)"}, {"kind": "method", "line": 995, "name": "refactor_monolith", "signature": "def refactor_monolith(self, target_dir)"}, {"kind": "method", "line": 894, "name": "on_change", "signature": "def on_change()"}]}, {"doc": "File-content hash cache for incremental scanning and analysis caching.  Computes SHA256 digests of file contents and persists them to disk so that subsequent scans can skip unchanged files. Also supports caching of analysis results (security findings, v2 analysis, etc.) for faster incremental rebuilds.", "id": "readmenator/_cache.py", "kind": "module", "label": "_cache.py", "language": "py", "sha256": "1a09ce2729ffe307", "symbol_count": 14, "symbols": [{"doc": "SHA256-based cache for incremental file scanning and analysis.\n\nStores a JSON mapping of relative file paths to their content\nhashes inside the project's cache directory. On subsequent runs,\nfiles whose hash matches the cached value are skipped.\n\nAlso caches analysis results so that unchanged files reuse\npreviously-computed security findings, taint paths, etc.", "kind": "class", "line": 20, "name": "FileCache", "signature": "class FileCache"}, {"doc": "Return one SHA256 over the sorted paths and contents of scanned sources.\n\nGenerated documents embed this value; recomputing it later answers\n\"do the docs still describe these sources?\" exactly, independent of\ngit commits (docs generated before a commit stay fresh after it).\n\nArgs:\n    project_root: Project root directory.\n    file_ids: Project-relative source paths that were scanned.\n\nReturns:\n    Hex digest; missing, unreadable, or symlinked files hash as empty.", "kind": "method", "line": 179, "name": "source_fingerprint", "signature": "def source_fingerprint(project_root, file_ids)"}, {"kind": "method", "line": 31, "name": "__init__", "signature": "def __init__(self, config, project_root)"}, {"kind": "method", "line": 38, "name": "load", "signature": "def load(self)"}, {"kind": "method", "line": 49, "name": "save", "signature": "def save(self, hashes)"}, {"kind": "method", "line": 55, "name": "compute_hash", "signature": "def compute_hash(self, file_path)"}, {"kind": "method", "line": 64, "name": "compute_hashes", "signature": "def compute_hashes(self, file_paths)"}, {"kind": "method", "line": 72, "name": "find_changed", "signature": "def find_changed(self, file_paths)"}, {"kind": "method", "line": 84, "name": "prune_deleted", "signature": "def prune_deleted(self, current_file_ids)"}, {"doc": "Save an analysis result to the semantic cache.\n\nArgs:\n    key: Cache key (e.g. \"security\", \"analysis_v2\", \"taint\").\n    data: Serializable analysis data.", "kind": "method", "line": 95, "name": "save_analysis", "signature": "def save_analysis(self, key, data)"}, {"doc": "Load a previously cached analysis result.\n\nArgs:\n    key: Cache key.\n\nReturns:\n    Cached data dict, or None if not found or expired.", "kind": "method", "line": 118, "name": "load_analysis", "signature": "def load_analysis(self, key)"}, {"doc": "Clear analysis cache, optionally for a specific key only.\n\nArgs:\n    key: If given, only clears this key. Otherwise clears all.", "kind": "method", "line": 135, "name": "clear_analysis", "signature": "def clear_analysis(self, key)"}, {"doc": "Remove analysis entries for files that no longer exist.", "kind": "method", "line": 155, "name": "_prune_analysis_cache", "signature": "def _prune_analysis_cache(self, current_file_ids)"}, {"doc": "Check if any file has changed since the last analysis cache.\n\nReturns True if there are no cached hashes (first run) or if\nany file hash differs from the cached value.", "kind": "method", "line": 166, "name": "has_changed_since_last_analysis", "signature": "def has_changed_since_last_analysis(self, file_paths)"}]}, {"doc": "Category theory model for the readmenator code graph.  Defines typed morphisms (edges with semantic kind), objects (file nodes), and a Category class for algebraic path composition. Every edge in the knowledge graph carries an EdgeKind that survives through to ranking computations.  The gain from category theory is that ReadMenator can answer queries by transformation, not just proximity:  - \"What code implements this concept?\"  -> documents -> defines - \"What breaks if I change this node?\"  -> composition of reverse edges - \"What tests validate this abstraction?\" -> defines <- tests - \"How do I get from public API to impl?\" -> composite paths", "id": "readmenator/_category.py", "kind": "module", "label": "_category.py", "language": "py", "sha256": "af20c924da229812", "symbol_count": 26, "symbols": [{"doc": "Semantic type of a morphism between two code artifacts.", "kind": "class", "line": 24, "name": "EdgeKind", "signature": "class EdgeKind(str, Enum)"}, {"doc": "A typed directed edge between two code artifacts.\n\nAttributes:\n    source: Node ID of the source artifact.\n    target: Node ID of the target artifact.\n    kind: Semantic type of the relationship.\n    confidence: Confidence score from static analysis (0.0 to 1.0).", "kind": "class", "line": 57, "name": "Morphism", "signature": "class Morphism"}, {"doc": "A category of code artifacts with typed morphisms.\n\nObjects are node IDs (file paths or symbol identifiers).\nMorphisms are typed directed edges. Composition follows\ncompatible source/target chains respecting edge-kind semantics.", "kind": "class", "line": 78, "name": "Category", "signature": "class Category"}, {"doc": "Weighted directed graph for PageRank computations.\n\nConverts a Category into a stochastic transition matrix suitable\nfor eigenvalue computation, preserving edge kind weights.", "kind": "class", "line": 181, "name": "TypedGraph", "signature": "class TypedGraph"}, {"doc": "Build a Category from lists of Edge objects.\n\nMaps Edge.relation strings to EdgeKind where possible.\nUnrecognised relation strings are mapped to DEPENDS_ON.\n\nArgs:\n    edges: Raw import edges from the scanner.\n    resolved_edges: Optional resolved-import edges.\n    node_ids: Optional set of valid node IDs to include.\n\nReturns:\n    A populated Category instance.", "kind": "method", "line": 236, "name": "build_category_from_edges", "signature": "def build_category_from_edges(edges, resolved_edges, node_ids)"}, {"doc": "Map a relation string to an EdgeKind.\n\nFalls back to DEPENDS_ON for unrecognised strings.", "kind": "method", "line": 278, "name": "_infer_edge_kind", "signature": "def _infer_edge_kind(relation)"}, {"kind": "method", "line": 38, "name": "__str__", "signature": "def __str__(self)"}, {"doc": "Effective weight for ranking = semantic weight * confidence.", "kind": "method", "line": 73, "name": "weight", "signature": "def weight(self)"}, {"kind": "method", "line": 86, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 92, "name": "add_object", "signature": "def add_object(self, obj_id)"}, {"kind": "method", "line": 95, "name": "add_morphism", "signature": "def add_morphism(self, m)"}, {"kind": "method", "line": 103, "name": "objects", "signature": "def objects(self)"}, {"kind": "method", "line": 107, "name": "morphisms", "signature": "def morphisms(self)"}, {"kind": "method", "line": 110, "name": "outgoing", "signature": "def outgoing(self, obj_id)"}, {"kind": "method", "line": 113, "name": "incoming", "signature": "def incoming(self, obj_id)"}, {"doc": "Compose two morphisms if target of a matches source of b.\n\nReturns a new Morphism with composite kind, or None if\nthe kinds are incompatible.", "kind": "method", "line": 116, "name": "compose", "signature": "def compose(self, a, b)"}, {"doc": "Find all composition paths from source to target up to max_depth.", "kind": "method", "line": 133, "name": "paths", "signature": "def paths(self, source, target, max_depth)"}, {"doc": "Determine the composite edge kind.\n\nComposition rules:\n- imports + defines -> defines (reachable definition)\n- imports + calls -> calls (reachable call)\n- defines + tests -> tests (tested through definition)\n- documents + defines -> documents (documented definition)\n- Same kind -> same kind.\n- Other combinations -> None (incompatible).", "kind": "method", "line": 157, "name": "_compose_kind", "signature": "def _compose_kind(a, b)"}, {"kind": "method", "line": 188, "name": "__init__", "signature": "def __init__(self, category)"}, {"kind": "method", "line": 197, "name": "_compute_out_weights", "signature": "def _compute_out_weights(self)"}, {"kind": "method", "line": 203, "name": "nodes", "signature": "def nodes(self)"}, {"kind": "method", "line": 207, "name": "size", "signature": "def size(self)"}, {"kind": "method", "line": 210, "name": "node_index", "signature": "def node_index(self, node_id)"}, {"doc": "Sum of weights of all morphisms from source to target.", "kind": "method", "line": 213, "name": "transition_weight", "signature": "def transition_weight(self, source, target)"}, {"doc": "Return dict of target -> probability for the row of *source*.\n\nProbabilities sum to 1.0 if source has outgoing edges.\nReturns empty dict for dangling nodes.", "kind": "method", "line": 221, "name": "stochastic_row", "signature": "def stochastic_row(self, source)"}, {"kind": "method", "line": 139, "name": "dfs", "signature": "def dfs(current, goal, path, depth)"}]}, {"doc": "Immutable configuration dataclass for readmenator.  All tuneable parameters live here as frozen dataclass fields. No magic numbers or hardcoded paths exist elsewhere in the codebase. Derived consumers import Config and read values from an instance.", "id": "readmenator/_config.py", "kind": "module", "label": "_config.py", "language": "py", "sha256": "a5ac9a21b5bd0467", "symbol_count": 1, "symbols": [{"doc": "Single source of truth for all readmenator settings.\n\nEvery tuneable constant -- file-size limits, directory depth,\nsupported extensions, symbol pluralisation map, Mermaid style\ntokens, graph analysis thresholds, and export settings -- is\ndefined here and consumed by reference elsewhere.", "kind": "class", "line": 15, "name": "Config", "signature": "class Config"}]}, {"doc": "Code Property Graph (CPG) generator emitting JSON-LD for AI agents.  Merges symbols, call, import, and inheritance edges, content hashes, and optional analysis metadata into one embeddable, zero-token graph.", "id": "readmenator/_cpg.py", "kind": "module", "label": "_cpg.py", "language": "py", "sha256": "8a900bfd31ac5121", "symbol_count": 6, "symbols": [{"doc": "Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.\n\nProduces a structured representation merging AST-level symbol data,\ncontrol-flow edges (calls), data-flow edges (imports), inheritance\nrelationships, and security findings (with MITRE ATT&CK mappings)\ninto a single machine-readable document. Designed to be embedded in\nKNOWLEDGE_BASE.md for zero-token agent context.", "kind": "class", "line": 16, "name": "CodePropertyGraph", "signature": "class CodePropertyGraph"}, {"kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self, privacy_mode, cpg_context)"}, {"doc": "Generate the CPG JSON-LD string embeddable in markdown.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for metadata.\n    findings: Optional security findings with MITRE ATT&CK IDs.\n\nReturns:\n    Compact JSON-LD string with @context, nodes, edges, analysis,\n    and mitre_attack metadata.", "kind": "method", "line": 30, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, findings)"}, {"kind": "method", "line": 147, "name": "_severity_counts", "signature": "def _severity_counts(self, findings)"}, {"kind": "method", "line": 153, "name": "_build_symbol_list", "signature": "def _build_symbol_list(self, node)"}, {"kind": "method", "line": 169, "name": "_compute_node_hash", "signature": "def _compute_node_hash(node)"}]}, {"doc": "Dynamic .cursorrules generator for the readmenator knowledge graph.  Reads architectural analysis results and linter violations to produce a deterministic .cursorrules file that feeds structural constraints back into AI coding assistants.", "id": "readmenator/_cursorrules_generator.py", "kind": "module", "label": "_cursorrules_generator.py", "language": "py", "sha256": "df7fb514feb68f04", "symbol_count": 8, "symbols": [{"doc": "Generates a .cursorrules file from architectural analysis.\n\nCombines base rules, detected layer constraints, and active\nlinter violations into a deterministic ruleset for AI assistants.", "kind": "class", "line": 18, "name": "CursorRulesGenerator", "signature": "class CursorRulesGenerator"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate the .cursorrules content string.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    analysis: Optional analysis results.\n    layers: Optional layer mapping.\n    violations: Optional linter violations.\n    project_root: Optional project root for file output.\n\nReturns:\n    The generated .cursorrules content as a string.", "kind": "method", "line": 28, "name": "generate", "signature": "def generate(self, nodes, edges, analysis, layers, violations, project_root)"}, {"kind": "method", "line": 63, "name": "_build_base_rules", "signature": "def _build_base_rules(self)"}, {"kind": "method", "line": 81, "name": "_extract_layer_constraints", "signature": "def _extract_layer_constraints(self, layers)"}, {"kind": "method", "line": 92, "name": "_extract_analysis_constraints", "signature": "def _extract_analysis_constraints(self, analysis)"}, {"kind": "method", "line": 107, "name": "_extract_violation_rules", "signature": "def _extract_violation_rules(self, violations)"}, {"kind": "method", "line": 115, "name": "_write_file", "signature": "def _write_file(self, project_root, content)"}]}, {"doc": "Procedural intra-function dataflow analysis for readmenator.  Detects classic logic bug classes without tokens, types, or control-flow graphs: use of uninitialized locals, dead stores (assigned but never read), and unchecked allocator results. Pure regex over function body spans derived from parsed symbol line ranges. Every finding is marked INFERRED: heuristics trade recall for reviewable, line-grounded leads.", "id": "readmenator/_dataflow.py", "kind": "module", "label": "_dataflow.py", "language": "py", "sha256": "83f0c71512dcaffa", "symbol_count": 21, "symbols": [{"doc": "Remove comments and string contents that confuse identifier scans.\n\nStrings are blanked before comment stripping so that ``//`` inside\nURL literals is not mistaken for a comment opener.", "kind": "function", "line": 96, "name": "_strip_noise", "signature": "def _strip_noise(line)"}, {"doc": "Blank block comments while preserving newlines and line numbers.", "kind": "function", "line": 107, "name": "_strip_block_comments", "signature": "def _strip_block_comments(content)"}, {"doc": "Blank sizeof operands, which never evaluate their argument at runtime.", "kind": "function", "line": 116, "name": "_strip_sizeof", "signature": "def _strip_sizeof(line)"}, {"doc": "Regex-based intra-function dataflow checker over scanned content.", "kind": "class", "line": 122, "name": "DataflowAnalyzer", "signature": "class DataflowAnalyzer"}, {"kind": "method", "line": 110, "name": "_blank", "signature": "def _blank(match)"}, {"doc": "Store configuration for enable flag and issue caps.", "kind": "method", "line": 125, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Check every function body span and return capped issues.", "kind": "method", "line": 129, "name": "analyze", "signature": "def analyze(self, nodes, content_map)"}, {"doc": "Return the brace depth before each line of noise-stripped code.", "kind": "method", "line": 153, "name": "_brace_depths", "signature": "def _brace_depths(lines)"}, {"doc": "Return (name, start_idx, end_idx) spans for function symbols.\n\nOnly function lines and file-scope (depth 0) symbols terminate a\nspan; local struct, enum, or variable declarations inside a body\ndo not truncate the enclosing function.", "kind": "method", "line": 164, "name": "_function_spans", "signature": "def _function_spans(self, node, total_lines, depths)"}, {"doc": "Run def-use checks over one function body span.", "kind": "method", "line": 191, "name": "_analyze_function", "signature": "def _analyze_function(self, file_id, func, lines, start, end)"}, {"doc": "Record identifier reads and address-takes inside an expression.", "kind": "method", "line": 403, "name": "_scan_reads", "signature": "def _scan_reads(text, lineno, reads, assigned, declared_names)"}, {"doc": "Discover pointer-from-array aliases in mid-line statements.", "kind": "method", "line": 427, "name": "_scan_inline_aliases", "signature": "def _scan_inline_aliases(line, lineno, arrays, derived_alias, deriv_reads)"}, {"doc": "Treat known filler/scan call arguments as assignments.", "kind": "method", "line": 450, "name": "_scan_out_params", "signature": "def _scan_out_params(line, lineno, assigned)"}, {"doc": "Treat arrays passed to non-readonly calls as assignments.", "kind": "method", "line": 461, "name": "_scan_array_args", "signature": "def _scan_array_args(line, lineno, arrays, assigned)"}, {"doc": "Extract parameter names from a function signature line.", "kind": "method", "line": 474, "name": "_params_of", "signature": "def _params_of(signature_line)"}, {"doc": "Track whether the next line continues an unclosed call.", "kind": "method", "line": 494, "name": "_track_call_continuation", "signature": "def _track_call_continuation(line, call_open, paren_balance)"}, {"doc": "Return True when an expression mentions a function parameter.", "kind": "method", "line": 513, "name": "_mentions_param", "signature": "def _mentions_param(text, params)"}, {"doc": "Return True when the identifier at pos is a struct member access.", "kind": "method", "line": 521, "name": "_is_member", "signature": "def _is_member(line, pos)"}, {"doc": "Return the base identifier of a member access chain.", "kind": "method", "line": 527, "name": "_member_base", "signature": "def _member_base(line, pos)"}, {"doc": "Return True for declaration lines that are actually prototypes.", "kind": "method", "line": 535, "name": "_is_prototype", "signature": "def _is_prototype(line)"}, {"doc": "Return True when body contains a NULL/boolean check for name.", "kind": "method", "line": 540, "name": "_null_checked", "signature": "def _null_checked(body_text, name)"}]}, {"doc": "Dead code detection for the readmenator knowledge graph.  Identifies orphaned symbols with zero in-degree in the resolved import graph, excluding known entry points. Generates structured reports without auto-deleting any code.", "id": "readmenator/_dead_code.py", "kind": "module", "label": "_dead_code.py", "language": "py", "sha256": "9606c78ecbfacbd6", "symbol_count": 5, "symbols": [{"doc": "Identifies dead code symbols in the knowledge graph.\n\nBuilds an in-degree map from resolved import edges, then flags\nsymbols that are never imported by any other file. Known entry\npoints are excluded from the dead code report.", "kind": "class", "line": 17, "name": "DeadCodeStripper", "signature": "class DeadCodeStripper"}, {"kind": "method", "line": 25, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Identify dead code symbols with zero in-degree.\n\nArgs:\n    nodes: Scanned file nodes with symbols.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n\nReturns:\n    List of DeadCodeReport instances for orphaned symbols.", "kind": "method", "line": 28, "name": "identify", "signature": "def identify(self, nodes, edges, resolved_edges)"}, {"doc": "Build in-degree count for each symbol name.", "kind": "method", "line": 64, "name": "_build_in_degree_map", "signature": "def _build_in_degree_map(self, nodes, resolved_edges)"}, {"doc": "Classify the recommended action for a dead symbol.", "kind": "method", "line": 88, "name": "_classify_recommendation", "signature": "def _classify_recommendation(self, symbol)"}]}, {"doc": "Self-contained interactive system maps for the knowledge graph.  Builds typed intermediate representations for five diagram kinds (architecture, workflow, sequence, dataflow, lifecycle) from scanned nodes and edges, validates each map deterministically, and renders a single self-contained HTML document with inline SVG, search, focus, reach tracing, route probing, role comparison, guided views, presentation stage, themes, presets, keyboard access, deep links, finite motion, and client-side export.", "id": "readmenator/_diagrams.py", "kind": "module", "label": "_diagrams.py", "language": "py", "sha256": "890ab4c64275f3b4", "symbol_count": 79, "symbols": [{"doc": "Escape text for HTML and tooltip embedding.\n\nArgs:\n    value: Raw text.\n\nReturns:\n    Escaped text safe for markup contexts.", "kind": "function", "line": 24, "name": "_escape_markup", "signature": "def _escape_markup(value)"}, {"doc": "Serialize a payload for safe inline script embedding.\n\nArgs:\n    payload: JSON-serializable payload.\n\nReturns:\n    JSON text with angle brackets unicode-escaped.", "kind": "function", "line": 36, "name": "_json_payload", "signature": "def _json_payload(payload)"}, {"doc": "Return the stroke color for a semantic role.\n\nArgs:\n    role: Semantic role identifier.\n    config: Central settings holding the role palette.\n\nReturns:\n    Hex color string for the role.", "kind": "function", "line": 48, "name": "_role_color", "signature": "def _role_color(role, config)"}, {"doc": "Single authored node in a system map.\n\nAttributes:\n    node_id: Stable identifier derived from the file path.\n    label: Short display label.\n    role: Semantic role used for color and lens comparison.\n    group: Lane or layer grouping used for layout.\n    detail: Supporting detail shown in the passport panel.\n    x: Deterministic horizontal canvas coordinate.\n    y: Deterministic vertical canvas coordinate.\n    language: Programming language of the source file.\n    doc: File-level documentation string.\n    symbols: Symbol records with name, kind, line, signature, doc.\n    symbol_total: Total symbol count before per-node truncation.", "kind": "class", "line": 62, "name": "MapNode", "signature": "class MapNode"}, {"doc": "Single authored directed relationship in a system map.\n\nAttributes:\n    source: Source node identifier.\n    target: Target node identifier.\n    label: Semantic relationship label.\n    kind: Relationship kind used for styling.", "kind": "class", "line": 93, "name": "MapEdge", "signature": "class MapEdge"}, {"doc": "Single guided chapter over authored topology.\n\nAttributes:\n    view_id: Stable chapter identifier usable in deep links.\n    title: Chapter title.\n    focus: Ordered node identifiers highlighted by the chapter.\n    description: Supporting explanation for the chapter.", "kind": "class", "line": 110, "name": "MapView", "signature": "class MapView"}, {"doc": "Typed intermediate representation of one diagram.\n\nAttributes:\n    kind: Diagram kind identifier.\n    title: Human-readable diagram title.\n    nodes: Authored nodes with deterministic coordinates.\n    edges: Authored directed relationships.\n    views: Guided chapters over the topology.\n    meta: Generation metadata for receipts and exports.", "kind": "class", "line": 127, "name": "SystemMap", "signature": "class SystemMap"}, {"doc": "Single machine-readable validation diagnostic.\n\nAttributes:\n    rule: Stable rule code.\n    subject: Identifier of the offending subject.\n    evidence: Measured evidence describing the failure.\n    repair: Supported repair control for the failure.", "kind": "class", "line": 148, "name": "MapDiagnostic", "signature": "class MapDiagnostic"}, {"doc": "Deterministic validation receipt for a system map.\n\nAttributes:\n    passed: True when zero errors were found.\n    checks: Names of checks that were executed.\n    errors: Error diagnostics blocking delivery.\n    warnings: Non-blocking advisory diagnostics.", "kind": "class", "line": 165, "name": "MapReceipt", "signature": "class MapReceipt"}, {"doc": "Before and after comparison between two maps of the same kind.\n\nAttributes:\n    kind: Diagram kind that was compared.\n    added: Node identifiers present only in the head map.\n    removed: Node identifiers present only in the base map.\n    changed: Node identifiers with altered role, group, or label.\n    moved: Node identifiers with altered coordinates.\n    rerouted: Edge pairs present only in one of the two maps.", "kind": "class", "line": 182, "name": "MapDelta", "signature": "class MapDelta"}, {"doc": "Deterministic validator for system map intermediate representations.", "kind": "class", "line": 202, "name": "SystemMapValidator", "signature": "class SystemMapValidator"}, {"doc": "Builds deterministic system maps from the scanned knowledge graph.", "kind": "class", "line": 426, "name": "SystemMapBuilder", "signature": "class SystemMapBuilder"}, {"doc": "Renders a system map as one self-contained interactive HTML document.", "kind": "class", "line": 1471, "name": "InteractiveMapRenderer", "signature": "class InteractiveMapRenderer"}, {"doc": "Renders a system map as a physics-driven vis.js network document.\n\nFetches the configured vis-network bundle from a CDN at view time,\nso pages need network access. Nodes stay draggable with live\nphysics; use the inline renderer when fully offline output matters.", "kind": "class", "line": 2186, "name": "VisNetworkRenderer", "signature": "class VisNetworkRenderer"}, {"doc": "Publishes validated system maps as a static documentation site.\n\nWrites one standalone map document per diagram kind plus a gallery\nindex page, ready to serve as project documentation or a static\nhosting root. All output is self-contained with zero external\nrequests and relative links only.", "kind": "class", "line": 2707, "name": "DocsSitePublisher", "signature": "class DocsSitePublisher"}, {"doc": "Initialise the validator with application configuration.\n\nArgs:\n    config: Central settings for map size limits.", "kind": "method", "line": 205, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return the canvas bounds applying per-map full-mode growth.\n\nArgs:\n    system_map: Map carrying optional canvas_width/canvas_height metadata.\n\nReturns:\n    Effective canvas width and height pair.", "kind": "method", "line": 213, "name": "_effective_canvas", "signature": "def _effective_canvas(self, system_map)"}, {"doc": "Validate a system map and return a deterministic receipt.\n\nArgs:\n    system_map: Map intermediate representation to validate.\n\nReturns:\n    Validation receipt with executed checks and diagnostics.", "kind": "method", "line": 234, "name": "validate", "signature": "def validate(self, system_map)"}, {"doc": "Initialise the builder with application configuration.\n\nArgs:\n    config: Central settings for layout geometry and limits.", "kind": "method", "line": 455, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return the supported diagram kind identifiers.\n\nReturns:\n    Ordered list of the configured diagram kinds.", "kind": "method", "line": 464, "name": "supported_kinds", "signature": "def supported_kinds(self)"}, {"doc": "Return whether full-map scope applies for this build.\n\nArgs:\n    full: Explicit caller override, None honors configuration.\n\nReturns:\n    True when every scanned file must be included without truncation.", "kind": "method", "line": 472, "name": "_is_full", "signature": "def _is_full(self, full)"}, {"doc": "Build one deterministic system map of the requested kind.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Raw import edges.\n    resolved_edges: Project-internal resolved import edges.\n    layers: Mapping of file identifier to architectural layer.\n    findings: Security findings used for sensitivity marking.\n    analysis: Graph analysis used for centrality ranking.\n    kind: Diagram kind identifier.\n    full: True includes every file with a grown canvas, None honors config.\n\nReturns:\n    Validated system map intermediate representation.", "kind": "method", "line": 485, "name": "build", "signature": "def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)"}, {"doc": "Build all five diagram kinds deterministically.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Raw import edges.\n    resolved_edges: Project-internal resolved import edges.\n    layers: Mapping of file identifier to architectural layer.\n    findings: Security findings used for sensitivity marking.\n    analysis: Graph analysis used for centrality ranking.\n    full: True includes every file with a grown canvas, None honors config.\n\nReturns:\n    Mapping of diagram kind to system map.", "kind": "method", "line": 523, "name": "build_all", "signature": "def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)"}, {"doc": "Compare two maps of the same kind as before, delta, and after.\n\nArgs:\n    base: Baseline system map.\n    head: Revised system map.\n\nReturns:\n    Deterministic delta with added, removed, changed, moved, rerouted facts.", "kind": "method", "line": 554, "name": "compare", "signature": "def compare(self, base, head)"}, {"doc": "Return the display title for a diagram kind.\n\nArgs:\n    kind: Diagram kind identifier.\n\nReturns:\n    Human-readable diagram title.", "kind": "method", "line": 593, "name": "_title_for", "signature": "def _title_for(self, kind)"}, {"doc": "Return the semantic role for a group with sensitivity override.\n\nArgs:\n    group: Architectural layer group name.\n    sensitive: True when the file carries elevated findings.\n\nReturns:\n    Semantic role identifier.", "kind": "method", "line": 607, "name": "_role_for", "signature": "def _role_for(self, group, sensitive)"}, {"doc": "Return files carrying elevated severity findings.\n\nArgs:\n    findings: Security findings to inspect.\n\nReturns:\n    Set of file paths with critical or high severity.", "kind": "method", "line": 624, "name": "_sensitive_files", "signature": "def _sensitive_files(self, findings)"}, {"doc": "Rank file identifiers by centrality then symbol count.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges used for degree scoring.\n    analysis: Optional analysis with god node scores.\n\nReturns:\n    File identifiers ordered by importance.", "kind": "method", "line": 641, "name": "_ranked_file_ids", "signature": "def _ranked_file_ids(self, nodes, links, analysis)"}, {"doc": "Select the primary node scope honoring the configured limit.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges used for ranking.\n    analysis: Optional analysis with centrality scores.\n    full: True returns every ranked node without truncation.\n\nReturns:\n    Primary nodes in deterministic ranked order.", "kind": "method", "line": 676, "name": "_select_primary", "signature": "def _select_primary(self, nodes, links, analysis, full)"}, {"doc": "Filter edges to project-internal links between selected files.\n\nArgs:\n    edges: Candidate edges.\n    selected: Selected file identifiers.\n    full: True keeps every internal edge without truncation.\n\nReturns:\n    Deterministically ordered internal edges.", "kind": "method", "line": 702, "name": "_internal_links", "signature": "def _internal_links(self, edges, selected, full)"}, {"doc": "Build truncated symbol records for map documentation payloads.\n\nArgs:\n    node: Scanned file node with extracted symbols.\n\nReturns:\n    Symbol records ordered by line, capped by configuration.", "kind": "method", "line": 725, "name": "_symbol_records", "signature": "def _symbol_records(self, node)"}, {"doc": "Shorten a label to the configured readable length.\n\nArgs:\n    value: Raw label text.\n\nReturns:\n    Truncated label with length guard applied.", "kind": "method", "line": 747, "name": "_short_label", "signature": "def _short_label(self, value)"}, {"doc": "Compute deterministic column lane coordinates for grouped items.\n\nArgs:\n    items: Pairs of identifier and group name.\n    kind: Diagram kind used only for metadata completeness.\n    full: True keeps every lane and grows the canvas instead of dropping.\n\nReturns:\n    Mapping of identifier to canvas coordinates.", "kind": "method", "line": 762, "name": "_layout_columns", "signature": "def _layout_columns(self, items, kind, full)"}, {"doc": "Drop lowest-priority lanes until columns fit the canvas width.\n\nArgs:\n    lanes: Lane names in priority order.\n\nReturns:\n    Leading lanes whose node boxes fit the canvas width.", "kind": "method", "line": 810, "name": "_lanes_that_fit", "signature": "def _lanes_that_fit(self, lanes)"}, {"doc": "Compress spacing deterministically so items fit the canvas.\n\nArgs:\n    count: Number of items placed along the axis.\n    item: Fixed item extent along the axis.\n    gap: Preferred spacing between items.\n    total: Total canvas extent along the axis.\n    margin: Margin reserved on each side.\n\nReturns:\n    Spacing that keeps every item inside the canvas.", "kind": "method", "line": 827, "name": "_fitted_gap", "signature": "def _fitted_gap(self, count, item, gap, total, margin)"}, {"doc": "Return the maximum members per lane fitting the canvas height.\n\nReturns:\n    Number of node rows fitting between lane top and margin.", "kind": "method", "line": 851, "name": "_lane_capacity", "signature": "def _lane_capacity(self)"}, {"doc": "Cap ranked nodes per lane so every lane fits the canvas height.\n\nArgs:\n    ranked: Nodes in global rank order.\n    layer_of: Mapping of file identifier to lane name.\n\nReturns:\n    Scoped nodes preserving rank order within each lane.", "kind": "method", "line": 865, "name": "_cap_lane_scope", "signature": "def _cap_lane_scope(self, ranked, layer_of)"}, {"doc": "Compute deterministic lifeline row coordinates for sequences.\n\nArgs:\n    ordered: Participant identifiers in display order.\n    full: True wraps participants across rows instead of truncating width.\n\nReturns:\n    Mapping of identifier to canvas coordinates.", "kind": "method", "line": 889, "name": "_layout_sequence", "signature": "def _layout_sequence(self, ordered, full)"}, {"doc": "Return the maximum participants fitting the canvas width.\n\nReturns:\n    Number of lifelines fitting with minimum spacing applied.", "kind": "method", "line": 926, "name": "_sequence_capacity", "signature": "def _sequence_capacity(self)"}, {"doc": "Cap lane scope and compute coordinates for placed nodes only.\n\nArgs:\n    ranked: Nodes in global rank order.\n    layer_of: Mapping of file identifier to lane name.\n    kind: Diagram kind used only for metadata completeness.\n    full: True keeps every node without lane caps or drops.\n\nReturns:\n    Canvas positions and the placed node subset.", "kind": "method", "line": 940, "name": "_place", "signature": "def _place(self, ranked, layer_of, kind, full)"}, {"doc": "Grow the canvas to enclose every placed node in full mode.\n\nArgs:\n    positions: Placed node coordinates.\n    full: True grows beyond configured bounds, False returns configured size.\n\nReturns:\n    Effective canvas width and height pair.", "kind": "method", "line": 960, "name": "_canvas_for", "signature": "def _canvas_for(self, positions, full)"}, {"doc": "Build generation metadata with honest scope and canvas size.\n\nArgs:\n    kind: Diagram kind identifier, unused beyond completeness.\n    placed: Authored map nodes.\n    links: Authored edge count.\n    total: Total scanned file count.\n    positions: Placed coordinates used for canvas growth.\n    full: True tags the map as untruncated with a grown canvas.\n\nReturns:\n    Metadata mapping for receipts and exports.", "kind": "method", "line": 978, "name": "_meta_for", "signature": "def _meta_for(self, kind, placed, links, total, positions, full)"}, {"doc": "Create guided chapters from authored topology.\n\nArgs:\n    kind: Diagram kind identifier.\n    primary: Ordered primary path node identifiers.\n    links: Authored internal relationships.\n\nReturns:\n    Guided chapters limited to the configured maximum.", "kind": "method", "line": 1001, "name": "_make_views", "signature": "def _make_views(self, kind, primary, links)"}, {"doc": "Build the runtime architecture map from file topology.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges.\n    layers: Layer mapping.\n    findings: Security findings.\n    analysis: Graph analysis.\n    full: True keeps every file without truncation.\n\nReturns:\n    Architecture system map.", "kind": "method", "line": 1073, "name": "_build_architecture", "signature": "def _build_architecture(self, nodes, links, layers, findings, analysis, full)"}, {"doc": "Build the delivery workflow map across architectural lanes.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges.\n    layers: Layer mapping.\n    findings: Security findings.\n    full: True keeps every file without lane sampling.\n\nReturns:\n    Workflow system map.", "kind": "method", "line": 1133, "name": "_build_workflow", "signature": "def _build_workflow(self, nodes, links, layers, findings, full)"}, {"doc": "Build the request sequence map over top participants.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges.\n    layers: Layer mapping.\n    analysis: Graph analysis.\n    full: True keeps every participant with wrapped rows.\n\nReturns:\n    Sequence system map.", "kind": "method", "line": 1213, "name": "_build_sequence", "signature": "def _build_sequence(self, nodes, links, layers, analysis, full)"}, {"doc": "Build the data flow map from sources through stores.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges.\n    layers: Layer mapping.\n    findings: Security findings for sensitivity.\n    full: True keeps every file without truncation.\n\nReturns:\n    Dataflow system map.", "kind": "method", "line": 1295, "name": "_build_dataflow", "signature": "def _build_dataflow(self, nodes, links, layers, findings, full)"}, {"doc": "Build the change lifecycle map with waits, retries, and terminals.\n\nArgs:\n    nodes: Scanned file nodes.\n    links: Internal edges.\n    layers: Layer mapping.\n    findings: Security findings.\n    full: True keeps every file without truncation.\n\nReturns:\n    Lifecycle system map.", "kind": "method", "line": 1378, "name": "_build_lifecycle", "signature": "def _build_lifecycle(self, nodes, links, layers, findings, full)"}, {"doc": "Initialise the renderer with application configuration.\n\nArgs:\n    config: Central settings for preset, theme, and share size.", "kind": "method", "line": 1474, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return the effective canvas size for rendering a map.\n\nArgs:\n    system_map: Map carrying optional grown canvas metadata.\n\nReturns:\n    Effective canvas width and height pair.", "kind": "method", "line": 1482, "name": "_canvas_size", "signature": "def _canvas_size(self, system_map)"}, {"doc": "Render a system map as a self-contained HTML document.\n\nArgs:\n    system_map: Validated system map intermediate representation.\n\nReturns:\n    Complete standalone HTML document with inline SVG and scripting.", "kind": "method", "line": 1503, "name": "render", "signature": "def render(self, system_map)"}, {"doc": "Render a system map and write it to a relative output path.\n\nArgs:\n    system_map: System map intermediate representation.\n    output_path: Destination file path.\n\nReturns:\n    Rendered HTML document that was written.", "kind": "method", "line": 1605, "name": "write", "signature": "def write(self, system_map, output_path)"}, {"doc": "Serialize a payload for safe inline script embedding.\n\nArgs:\n    payload: JSON-serializable payload.\n\nReturns:\n    JSON text with angle brackets unicode-escaped.", "kind": "method", "line": 1624, "name": "_safe_json", "signature": "def _safe_json(self, payload)"}, {"doc": "Escape text for SVG and HTML embedding.\n\nArgs:\n    value: Raw text.\n\nReturns:\n    Escaped text safe for markup contexts.", "kind": "method", "line": 1635, "name": "_escape", "signature": "def _escape(self, value)"}, {"doc": "Return the stroke color for a semantic role.\n\nArgs:\n    role: Semantic role identifier.\n\nReturns:\n    Hex color string for the role.", "kind": "method", "line": 1646, "name": "_role_color", "signature": "def _role_color(self, role)"}, {"doc": "Compute a deterministic curved route between two nodes.\n\nArgs:\n    x1: Source horizontal center.\n    y1: Source vertical center.\n    x2: Target horizontal center.\n    y2: Target vertical center.\n\nReturns:\n    SVG path data string.", "kind": "method", "line": 1657, "name": "_edge_path", "signature": "def _edge_path(self, x1, y1, x2, y2)"}, {"doc": "Render authored nodes as inline SVG groups.\n\nArgs:\n    system_map: System map intermediate representation.\n\nReturns:\n    SVG fragment with one group per node.", "kind": "method", "line": 1693, "name": "_nodes_svg", "signature": "def _nodes_svg(self, system_map)"}, {"doc": "Render authored relationships as inline SVG paths.\n\nArgs:\n    system_map: System map intermediate representation.\n\nReturns:\n    SVG fragment with one path per relationship.", "kind": "method", "line": 1741, "name": "_edges_svg", "signature": "def _edges_svg(self, system_map)"}, {"doc": "Return the self-contained viewer document template.\n\nReturns:\n    HTML template with replacement tokens for map content.", "kind": "method", "line": 1788, "name": "_template", "signature": "def _template(self)"}, {"doc": "Initialise the renderer with application configuration.\n\nArgs:\n    config: Central settings for CDN bundle and physics.", "kind": "method", "line": 2194, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Render a system map as a vis.js network HTML document.\n\nArgs:\n    system_map: Validated system map intermediate representation.\n\nReturns:\n    HTML document driving a draggable physics network.", "kind": "method", "line": 2202, "name": "render", "signature": "def render(self, system_map)"}, {"doc": "Render a vis.js map and write it to a relative output path.\n\nArgs:\n    system_map: System map intermediate representation.\n    output_path: Destination file path.\n\nReturns:\n    Rendered HTML document that was written.", "kind": "method", "line": 2303, "name": "write", "signature": "def write(self, system_map, output_path)"}, {"doc": "Build a documentation tooltip for a network node.\n\nArgs:\n    node: Authored map node.\n\nReturns:\n    Escaped tooltip markup with docs and top symbols.", "kind": "method", "line": 2320, "name": "_tooltip", "signature": "def _tooltip(self, node)"}, {"doc": "Return the vis.js viewer document template.\n\nReturns:\n    HTML template with replacement tokens for map content.", "kind": "method", "line": 2351, "name": "_template", "signature": "def _template(self)"}, {"doc": "Initialise the publisher with application configuration.\n\nArgs:\n    config: Central settings for pages layout and map limits.", "kind": "method", "line": 2724, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return the gallery description for a diagram kind.\n\nArgs:\n    kind: Diagram kind identifier.\n\nReturns:\n    Human-readable gallery description.", "kind": "method", "line": 2734, "name": "description_for", "signature": "def description_for(self, kind)"}, {"doc": "Publish maps and a gallery index into a documentation directory.\n\nArgs:\n    maps: Mapping of diagram kind to system map.\n    project_name: Display name used for index titles.\n    output_dir: Destination directory for the static site.\n    stats: Optional project counters shown in the gallery header.\n    renderer: Map renderer with a write method, defaults to offline.\n    project_root: Optional project root used to collect video and docs.\n    video_rel: Optional precomputed video href relative to the index.\n    doc_entries: Optional precomputed doc entries with name and href.\n\nReturns:\n    Mapping of published page identifier to written file path.", "kind": "method", "line": 2748, "name": "publish", "signature": "def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries)"}, {"doc": "Collect generated markdown sources for the static site.\n\nArgs:\n    project_root: Project root directory to scan for docs.\n\nReturns:\n    Sorted list of markdown file paths capped by configuration.", "kind": "method", "line": 2836, "name": "collect_doc_sources", "signature": "def collect_doc_sources(self, project_root)"}, {"doc": "Copy overview video and markdown docs into the static site.\n\nArgs:\n    project_root: Project root holding generated artifacts.\n    output_dir: Static site root receiving copied assets.\n\nReturns:\n    Mapping with video_rel, doc_entries, and written paths.", "kind": "method", "line": 2862, "name": "publish_assets", "signature": "def publish_assets(self, project_root, output_dir)"}, {"doc": "Delete copied markdown docs that no longer exist in the project.\n\nThe docs subdirectory is owned by the publisher; without pruning,\nrenamed wiki or paged agent files would linger in the site forever.\n\nArgs:\n    docs_root: Site directory holding copied markdown.\n    keep: Relative paths published in this run.", "kind": "method", "line": 2918, "name": "_prune_stale_docs", "signature": "def _prune_stale_docs(docs_root, keep)"}, {"doc": "Render an llms.txt entry point so agents can navigate the site as text.\n\nFollows the llms.txt convention: an H1 title, a blockquote summary,\nthen H2 sections of markdown links. Agent-oriented markdown comes\nfirst because it is cheaper to read than the HTML maps.\n\nArgs:\n    project_name: Display name used for the title.\n    maps: Mapping of published diagram kind to system map.\n    stats: Project counters summarized in the blockquote.\n    href_prefix: Relative prefix pointing at the map directory.\n    doc_entries: Published markdown docs with name and href.\n\nReturns:\n    Plain markdown text for llms.txt.", "kind": "method", "line": 2935, "name": "render_llms_txt", "signature": "def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)"}, {"doc": "Render the gallery index page for published maps.\n\nArgs:\n    project_name: Display name used for index titles.\n    maps: Mapping of published diagram kind to system map.\n    stats: Project counters shown in the gallery header.\n    href_prefix: Relative prefix pointing at the map directory.\n    video_rel: Optional video href relative to the index.\n    doc_entries: Optional doc entries with name, href, preview.\n\nReturns:\n    Complete standalone HTML gallery document.", "kind": "method", "line": 3011, "name": "render_index", "signature": "def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries)"}, {"doc": "Render the overview video section with an HTML5 video tag.\n\nArgs:\n    video_rel: Video href relative to the index, None hides the section.\n\nReturns:\n    HTML section fragment, empty string when no video is available.", "kind": "method", "line": 3170, "name": "_video_section", "signature": "def _video_section(self, video_rel)"}, {"doc": "Render the documentation grid with an offline markdown viewer.\n\nArgs:\n    doc_entries: Doc entries with name, href, and preview keys.\n\nReturns:\n    HTML section fragment, empty string when no docs are available.", "kind": "method", "line": 3194, "name": "_docs_section", "signature": "def _docs_section(self, doc_entries)"}, {"doc": "Return the relative href prefix for map links.\n\nReturns:\n    Map subdirectory with trailing slash, or empty string.", "kind": "method", "line": 3239, "name": "_href_prefix", "signature": "def _href_prefix(self)"}, {"doc": "Render one gallery card linking to a published map.\n\nArgs:\n    kind: Diagram kind identifier.\n    system_map: Published system map.\n    href_prefix: Relative prefix pointing at the map directory.\n\nReturns:\n    HTML card fragment with a relative map link.", "kind": "method", "line": 3250, "name": "_card", "signature": "def _card(self, kind, system_map, href_prefix)"}, {"doc": "Render the gallery header statistics line.\n\nArgs:\n    stats: Project counters.\n\nReturns:\n    Escaped statistics summary string.", "kind": "method", "line": 3289, "name": "_stats_line", "signature": "def _stats_line(self, stats)"}, {"doc": "Escape text for HTML embedding.\n\nArgs:\n    value: Raw text.\n\nReturns:\n    Escaped text safe for markup contexts.", "kind": "method", "line": 3303, "name": "_escape", "signature": "def _escape(self, value)"}, {"doc": "Sort entry points first, then alphabetically.", "kind": "method", "line": 2983, "name": "order", "signature": "def order(entry)"}]}, {"doc": "KNOWLEDGE_BASE.md generator: the human-facing architecture reference.  Renders the dashboard, layers, communities, CPG, taint, hotspots, cycles, security audit, Mermaid graph, and per-file reference sections.", "id": "readmenator/_documentation.py", "kind": "module", "label": "_documentation.py", "language": "py", "sha256": "53f41fd1e065ee70", "symbol_count": 28, "symbols": [{"doc": "Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.\n\nDelegates graph rendering to MermaidRenderer and handles the\nMarkdown layout: header metadata, Mermaid block, statistics dashboard,\ngod nodes, community analysis, surprising connections, architecture\nlayers, security audit, taint analysis, hotspots, dependency cycles,\nchange impact, architecture violations, suggested rules, CPG block,\nranking metadata, orphans, query recipes, and per-language architecture\nsections with pluralised symbol kind headings.", "kind": "class", "line": 33, "name": "DocumentationGenerator", "signature": "class DocumentationGenerator"}, {"kind": "method", "line": 45, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 63, "name": "_ranking_version", "signature": "def _ranking_version(self)"}, {"kind": "method", "line": 81, "name": "_get_git_commit", "signature": "def _get_git_commit()"}, {"kind": "method", "line": 91, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)"}, {"kind": "method", "line": 178, "name": "_apply_context_budget", "signature": "def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)"}, {"kind": "method", "line": 316, "name": "_build_toc", "signature": "def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)"}, {"kind": "method", "line": 404, "name": "_build_layers", "signature": "def _build_layers(self, layers, nodes)"}, {"kind": "method", "line": 438, "name": "_build_dashboard", "signature": "def _build_dashboard(self, nodes, edges, resolved_edges)"}, {"kind": "method", "line": 518, "name": "_build_god_nodes", "signature": "def _build_god_nodes(self, analysis, ranked)"}, {"kind": "method", "line": 546, "name": "_build_community_analysis", "signature": "def _build_community_analysis(self, analysis, nodes)"}, {"kind": "method", "line": 579, "name": "_build_surprising_connections", "signature": "def _build_surprising_connections(self, analysis, nodes)"}, {"kind": "method", "line": 604, "name": "_build_suggested_questions", "signature": "def _build_suggested_questions(self, analysis)"}, {"kind": "method", "line": 620, "name": "_build_ranked_context", "signature": "def _build_ranked_context(self, ranked)"}, {"doc": "Build a section listing nodes with low coverage signals.", "kind": "method", "line": 666, "name": "_build_orphans", "signature": "def _build_orphans(self, nodes, analysis_v2, ranked)"}, {"kind": "method", "line": 716, "name": "_build_query_recipes", "signature": "def _build_query_recipes(self)"}, {"kind": "method", "line": 758, "name": "_build_taint_analysis", "signature": "def _build_taint_analysis(self, analysis_v2)"}, {"kind": "method", "line": 793, "name": "_build_hotspots", "signature": "def _build_hotspots(self, analysis_v2, ranked)"}, {"doc": "Build the procedural dataflow findings section.", "kind": "method", "line": 831, "name": "_build_dataflow_analysis", "signature": "def _build_dataflow_analysis(self, analysis_v2)"}, {"kind": "method", "line": 862, "name": "_build_dependency_cycles", "signature": "def _build_dependency_cycles(self, analysis_v2)"}, {"kind": "method", "line": 883, "name": "_build_change_impact", "signature": "def _build_change_impact(self, analysis_v2)"}, {"kind": "method", "line": 908, "name": "_build_layer_violations", "signature": "def _build_layer_violations(self, analysis_v2)"}, {"kind": "method", "line": 936, "name": "_build_suggested_rules", "signature": "def _build_suggested_rules(self, analysis_v2)"}, {"kind": "method", "line": 961, "name": "_build_security_findings", "signature": "def _build_security_findings(self, findings)"}, {"kind": "method", "line": 1008, "name": "_build_mermaid_section", "signature": "def _build_mermaid_section(self, graph_output, is_truncated)"}, {"kind": "method", "line": 1031, "name": "_build_uml_diagram", "signature": "def _build_uml_diagram(self, nodes, edges)"}, {"kind": "method", "line": 1057, "name": "_build_cpg_block", "signature": "def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)"}, {"kind": "method", "line": 1083, "name": "_build_architecture_reference", "signature": "def _build_architecture_reference(self, nodes, edges)"}]}, {"doc": "Score explanation and path decomposition for the ranking system.  Provides human-readable explanations of why a particular node ranks where it does, including score breakdown, strongest paths from seeds, and quality signal summary.", "id": "readmenator/_explain.py", "kind": "module", "label": "_explain.py", "language": "py", "sha256": "1c5e324fb42169ed", "symbol_count": 3, "symbols": [{"doc": "Return a detailed breakdown of why *node_id* has its rank.\n\nIncludes score decomposition, seed paths, and quality signals.\n\nArgs:\n    node_id: The node to explain.\n    ranked: The RankedResult containing scores.\n    category: Optional Category for enriched path details.\n\nReturns:\n    Formatted explanation string, or None if node_id not found.", "kind": "function", "line": 16, "name": "explain_rank", "signature": "def explain_rank(node_id, ranked, category)"}, {"doc": "Return a short summary of the top-N ranked results.", "kind": "function", "line": 140, "name": "rank_summary", "signature": "def rank_summary(ranked, top_n)"}, {"kind": "function", "line": 163, "name": "_find_item", "signature": "def _find_item(node_id, items)"}]}, {"doc": "Multi-format exporter for the readmenator knowledge graph.  Produces JSON (GraphRAG-ready node-link format), interactive HTML (vis.js standalone), and static SVG (matplotlib-based) outputs from the scanned nodes, edges, and optional analysis results.", "id": "readmenator/_exporter.py", "kind": "module", "label": "_exporter.py", "language": "py", "sha256": "e8305a07a66f0e36", "symbol_count": 15, "symbols": [{"doc": "Exports the knowledge graph to JSON, HTML, and SVG formats.\n\nEach method is self-contained and produces a single file. No\nexternal network calls are made; the HTML file embeds vis.js\nfrom a CDN reference for offline-compatible rendering.", "kind": "class", "line": 21, "name": "GraphExporter", "signature": "class GraphExporter"}, {"doc": "Initialise with application configuration.\n\nArgs:\n    config: Settings for export styling and limits.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Export the graph as a node-link JSON string.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for metadata.\n    findings: Optional security audit findings.\n\nReturns:\n    JSON string with nodes, edges, and optional analysis/findings metadata.", "kind": "method", "line": 37, "name": "to_json", "signature": "def to_json(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Generate a standalone interactive HTML graph page.\n\nUses vis.js loaded from CDN. Supports click-to-inspect nodes,\nsearch filtering, and community-based coloring.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community coloring.\n\nReturns:\n    Complete HTML document as a string.", "kind": "method", "line": 150, "name": "to_html", "signature": "def to_html(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Build a node-to-color map based on community membership.", "kind": "method", "line": 239, "name": "_community_color_map", "signature": "def _community_color_map(self, analysis)"}, {"doc": "Lighten a hex color by 30% for border use.", "kind": "method", "line": 257, "name": "_lighten", "signature": "def _lighten(hex_color)"}, {"doc": "Render the full HTML document with vis.js.", "kind": "method", "line": 265, "name": "_render_html", "signature": "def _render_html(self, vis_nodes, vis_edges, analysis, findings)"}, {"doc": "Generate a static SVG representation of the graph.\n\nUses a simple force-directed layout without external dependencies.\nFor graphs with more than SVG_MAX_NODES, returns a plain SVG\nwith a truncation message.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community coloring.\n\nReturns:\n    SVG document as a string.", "kind": "method", "line": 436, "name": "to_svg", "signature": "def to_svg(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Render a minimal SVG with a truncation notice.", "kind": "method", "line": 554, "name": "_render_truncated_svg", "signature": "def _render_truncated_svg(self, total_nodes)"}, {"doc": "Compute a simple spring-layout for node positioning.\n\nImplements a basic force-directed layout with repulsion\nbetween all nodes and attraction along edges. Runs a fixed\nnumber of iterations for determinism.", "kind": "method", "line": 569, "name": "_layout_spring", "signature": "def _layout_spring(self, nodes, edges, node_map)"}, {"doc": "Export the graph as GraphML (Gephi/yEd compatible).\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community data.\n\nReturns:\n    GraphML XML string.", "kind": "method", "line": 650, "name": "to_graphml", "signature": "def to_graphml(self, nodes, edges, resolved_edges, analysis)"}, {"doc": "Export the graph as native Cypher CREATE statements.\n\nGenerates Neo4j/Memgraph-compatible Cypher for direct graph\ndatabase ingestion. Each file node becomes a ``(:File)`` node,\nimport dependencies become ``(:File)-[:IMPORTS]->(:File)``\nrelationships. Optional security findings are attached as node\nproperties and standalone ``(:SecurityFinding)`` nodes.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    analysis: Optional analysis results for community metadata.\n    findings: Optional security finding nodes.\n\nReturns:\n    String of Cypher CREATE statements.", "kind": "method", "line": 727, "name": "to_cypher", "signature": "def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)"}, {"doc": "Export the graph as an Obsidian vault with wikilinks.\n\nEach file node becomes a markdown note. Community hub notes\naggregate related files. All notes use [[wikilinks]] for\nObsidian graph navigation.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    output_dir: Directory to write the Obsidian notes.\n    analysis: Optional analysis results for community hubs.\n\nReturns:\n    Number of notes written.", "kind": "method", "line": 832, "name": "to_obsidian", "signature": "def to_obsidian(self, nodes, edges, output_dir, analysis)"}, {"kind": "method", "line": 498, "name": "_project", "signature": "def _project(pos)"}, {"kind": "method", "line": 337, "name": "_sev_span", "signature": "def _sev_span(sev, count)"}]}, {"doc": "GitHub wiki publisher: mirrors generated knowledge into the repository wiki.  Turns the readmenator wiki, agent docs, recipes, and KNOWLEDGE_BASE.md into flat GitHub wiki pages (Home, _Sidebar, _Footer), rewrites relative markdown links to wiki page names, and turns backticked project paths into commit-pinned source permalinks. Publishing clones ``<repo>.wiki.git``, replaces only pages it generated before (tracked in a state file), commits, and pushes. It is opt-in, never runs during analysis, and shells out with argument lists only (no shell).", "id": "readmenator/_gh_wiki.py", "kind": "module", "label": "_gh_wiki.py", "language": "py", "sha256": "48ab96c3ef223668", "symbol_count": 18, "symbols": [{"doc": "Outcome of a GitHub wiki publish.\n\nAttributes:\n    pages: Wiki page file names written.\n    removed: Previously generated page files deleted as stale.\n    pushed: Whether a commit was pushed to the wiki remote.\n    remote: Wiki remote URL used, empty in dry runs without a remote.\n    output_dir: Directory holding the rendered pages.\n    message: Human-readable status line.", "kind": "class", "line": 39, "name": "WikiPublishResult", "signature": "class WikiPublishResult"}, {"doc": "Renders and publishes generated documentation to a GitHub wiki.", "kind": "class", "line": 59, "name": "GitHubWikiPublisher", "signature": "class GitHubWikiPublisher"}, {"doc": "Store configuration and the subprocess runner (injectable for tests).\n\nArgs:\n    config: Central settings for paths, page names, and git options.\n    runner: Callable compatible with ``subprocess.run``.", "kind": "method", "line": 62, "name": "__init__", "signature": "def __init__(self, config, runner)"}, {"doc": "Map a generated markdown path to its flat GitHub wiki page name.\n\nArgs:\n    rel_path: Project-relative markdown path.\n\nReturns:\n    Wiki page name without extension.", "kind": "method", "line": 72, "name": "page_name", "signature": "def page_name(self, rel_path)"}, {"doc": "List project-relative markdown sources to publish, sorted.\n\nArgs:\n    project_root: Project root holding generated outputs.\n\nReturns:\n    Relative POSIX paths of regular, non-symlink markdown files.", "kind": "method", "line": 96, "name": "collect_sources", "signature": "def collect_sources(self, project_root)"}, {"doc": "Return the web URL prefix for commit-pinned source links, or empty.", "kind": "method", "line": 121, "name": "_blob_base", "signature": "def _blob_base(self, remote, commit)"}, {"doc": "Rewrite relative doc links to wiki pages and paths to source permalinks.\n\nArgs:\n    text: Markdown content of one source document.\n    rel_path: Project-relative path of that document.\n    names: Mapping of published relative paths to page names.\n    project_root: Project root used to check that paths exist.\n    blob_base: Commit-pinned blob URL prefix, empty to skip.\n\nReturns:\n    Markdown ready for the GitHub wiki.", "kind": "method", "line": 129, "name": "rewrite", "signature": "def rewrite(self, text, rel_path, names, project_root, blob_base)"}, {"doc": "Render every wiki page, including sidebar and footer.\n\nArgs:\n    project_root: Project root holding generated outputs.\n    remote: Main repository remote used for source permalinks.\n\nReturns:\n    Mapping of wiki file name to markdown content.", "kind": "method", "line": 179, "name": "render", "signature": "def render(self, project_root, remote)"}, {"doc": "Return a Home page used when the readmenator wiki was not generated.", "kind": "method", "line": 205, "name": "_fallback_home", "signature": "def _fallback_home(self, project_name)"}, {"doc": "Return the navigation sidebar grouping pages by origin.", "kind": "method", "line": 213, "name": "_sidebar", "signature": "def _sidebar(self, names)"}, {"doc": "Return the footer stamping the source commit and regeneration command.", "kind": "method", "line": 241, "name": "_footer", "signature": "def _footer(git)"}, {"doc": "Resolve the wiki remote from config, ``gh``, or the git origin.\n\nArgs:\n    project_root: Project root of the main repository.\n\nReturns:\n    The ``.wiki.git`` remote URL, or empty string when unknown.", "kind": "method", "line": 249, "name": "wiki_remote", "signature": "def wiki_remote(self, project_root)"}, {"doc": "Return the main repository URL via ``gh`` or ``git remote``.", "kind": "method", "line": 267, "name": "_origin", "signature": "def _origin(self, project_root)"}, {"doc": "Run a command without a shell and return stdout, or None on failure.", "kind": "method", "line": 279, "name": "_call", "signature": "def _call(self, command, cwd)"}, {"doc": "Write pages, delete stale previously generated ones, and record state.", "kind": "method", "line": 293, "name": "_write_pages", "signature": "def _write_pages(self, target, pages)"}, {"doc": "Render pages and push them to the GitHub wiki (or a local folder).\n\nArgs:\n    project_root: Project root holding generated outputs.\n    dry_run: Render into GH_WIKI_DRY_RUN_DIR without any git calls.\n\nReturns:\n    WikiPublishResult describing what was written and pushed.", "kind": "method", "line": 313, "name": "publish", "signature": "def publish(self, project_root, dry_run)"}, {"doc": "Replace one relative markdown link when its target is published.", "kind": "method", "line": 151, "name": "link", "signature": "def link(match)"}, {"doc": "Link a backticked project file (optionally with a line) to source.", "kind": "method", "line": 164, "name": "permalink", "signature": "def permalink(match)"}]}, {"doc": "Read-only git metadata for freshness stamps on generated documents.  Reads ``.git`` plumbing files directly (no subprocess, no network) so agents can compare a generated MANIFEST against ``git rev-parse HEAD`` and know whether the knowledge base is stale before trusting it.", "id": "readmenator/_gitmeta.py", "kind": "module", "label": "_gitmeta.py", "language": "py", "sha256": "f2d97022c2d6682a", "symbol_count": 4, "symbols": [{"doc": "Return the stripped text of a small regular file, or empty string.\n\nArgs:\n    path: File to read.\n\nReturns:\n    File contents, or empty string when missing, a symlink, or oversized.", "kind": "function", "line": 19, "name": "_read_small", "signature": "def _read_small(path)"}, {"doc": "Locate the git directory for a work tree, following gitdir files.\n\nArgs:\n    root: Work tree root.\n\nReturns:\n    The git directory path, or None when the root is not a repository.", "kind": "function", "line": 38, "name": "_git_dir", "signature": "def _git_dir(root)"}, {"doc": "Look up a ref in packed-refs, honoring worktree commondir.\n\nArgs:\n    git_dir: Git directory of the work tree.\n    ref: Fully qualified ref name.\n\nReturns:\n    The commit hash, or empty string.", "kind": "function", "line": 59, "name": "_packed_ref", "signature": "def _packed_ref(git_dir, ref)"}, {"doc": "Return the current commit and branch of a project, when available.\n\nArgs:\n    project_root: Work tree root directory.\n\nReturns:\n    Mapping with ``commit`` and ``branch`` keys (empty strings when\n    unknown or not a git repository).", "kind": "function", "line": 84, "name": "read_git_head", "signature": "def read_git_head(project_root)"}]}, {"doc": "Hotspot, dependency cycle, and change impact analysis.  Scores files by complexity plus centrality, finds import cycles with DFS, and measures transitive dependents with bounded BFS.", "id": "readmenator/_hotspots.py", "kind": "module", "label": "_hotspots.py", "language": "py", "sha256": "89a15a177df1f60a", "symbol_count": 7, "symbols": [{"doc": "Hotspot detection, cycle analysis, and change impact analysis.\n\nHotspots are files with high complexity (many symbols) and high\ncentrality (many connections). Cycle detection finds circular\ndependencies in the resolved import graph. Change impact analysis\ncomputes transitive-dependent lists for every file.", "kind": "class", "line": 22, "name": "HotspotAnalyzer", "signature": "class HotspotAnalyzer"}, {"kind": "method", "line": 31, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Rank files by combined complexity and centrality scores.\n\nComplexity is normalised symbol count. Centrality is normalised\nconnection count (in-degree + out-degree). The combined score\nuses configured weights.", "kind": "method", "line": 34, "name": "analyze_hotspots", "signature": "def analyze_hotspots(self, nodes, edges, resolved_edges)"}, {"doc": "Detect cycles in the resolved import graph using DFS.\n\nUses Tarjan's algorithm variant with three-colour DFS to find\nall elementary cycles. Returns each cycle as a DependencyCycle.", "kind": "method", "line": 90, "name": "detect_cycles", "signature": "def detect_cycles(self, nodes, resolved_edges)"}, {"doc": "Compute change impact for every file in the project.\n\nFor each file, finds all files that would be affected if it\nchanged (direct and transitive dependents via reverse import\ngraph traversal).", "kind": "method", "line": 155, "name": "analyze_change_impact", "signature": "def analyze_change_impact(self, nodes, resolved_edges)"}, {"kind": "method", "line": 114, "name": "_dfs_visit", "signature": "def _dfs_visit(current)"}, {"kind": "method", "line": 125, "name": "_record_cycle", "signature": "def _record_cycle(start, end)"}]}, {"doc": "Architecture layer rule engine: forbidden and warning edges between layers.", "id": "readmenator/_layer_rules.py", "kind": "module", "label": "_layer_rules.py", "language": "py", "sha256": "d210f851b1778697", "symbol_count": 4, "symbols": [{"doc": "Architectural layer violation detection engine.\n\nDefines a set of permitted and forbidden layer-to-layer import\nrules. Scans all resolved import edges and flags violations\nwhere one layer imports from another in a way that violates\nthe architecture.", "kind": "class", "line": 11, "name": "LayerRuleEngine", "signature": "class LayerRuleEngine"}, {"kind": "method", "line": 36, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Detect architectural layer violations.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved import edges.\n    layers: Dict mapping node_id to layer name. If None, imports\n        _layers.LayerDetector for automatic detection.\n\nReturns:\n    List of LayerViolation instances.", "kind": "method", "line": 39, "name": "detect_violations", "signature": "def detect_violations(self, nodes, edges, resolved_edges, layers)"}, {"doc": "Summarise violations by severity.", "kind": "method", "line": 111, "name": "violation_summary", "signature": "def violation_summary(violations)"}]}, {"doc": "Architectural layer detection for the readmenator knowledge graph.  Infers architectural layers (presentation, business logic, data access, infrastructure, testing, configuration) from file paths, naming conventions, and import patterns. No external API calls.", "id": "readmenator/_layers.py", "kind": "module", "label": "_layers.py", "language": "py", "sha256": "74e808d11118e2e5", "symbol_count": 7, "symbols": [{"doc": "Detects architectural layers in a codebase.\n\nAssigns each file to a layer based on path patterns, naming\nconventions, and imported frameworks. Returns a mapping that\ncan enrich documentation and analysis. No config dependency.", "kind": "class", "line": 17, "name": "LayerDetector", "signature": "class LayerDetector"}, {"doc": "Assign each file node to an architectural layer.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n\nReturns:\n    Dict mapping node_id to layer name.", "kind": "method", "line": 83, "name": "detect", "signature": "def detect(self, nodes, edges)"}, {"doc": "Split a path into lowercase word tokens, honoring camelCase.", "kind": "method", "line": 108, "name": "_path_tokens", "signature": "def _path_tokens(cls, node_id)"}, {"doc": "Return whether a layer pattern matches path tokens as a whole word.\n\nShort patterns (``ui``, ``di``, ``api``) must equal a token;\nlonger ones also match token prefixes (``tests``, ``views``).\nMulti-word patterns match underscore-joined token runs.", "kind": "method", "line": 114, "name": "_pattern_hits", "signature": "def _pattern_hits(cls, pattern, tokens, joined)"}, {"doc": "Return the top-level module names of raw import strings.", "kind": "method", "line": 128, "name": "_import_roots", "signature": "def _import_roots(cls, imports)"}, {"doc": "Classify a single file into an architectural layer.\n\nPath words score one point each, framework imports three, and\ntest-file naming five. Layers in _EVIDENCE_REQUIRED_LAYERS only\naccept framework points when the path already points there, so a\nCLI that imports ``unittest`` to run the suite stays production code.", "kind": "method", "line": 138, "name": "_classify_file", "signature": "def _classify_file(self, node, edges, imports)"}, {"doc": "Count files per layer.\n\nArgs:\n    layers: Mapping from detect().\n\nReturns:\n    Dict of layer_name -> file_count.", "kind": "method", "line": 189, "name": "layer_summary", "signature": "def layer_summary(layers)"}]}, {"doc": "Architecture linter for the readmenator knowledge graph.  Evaluates files against predefined architectural rules: file length limits, cross-layer import violations, and circular dependency detection. All rules are deterministic and token-free.", "id": "readmenator/_linter.py", "kind": "module", "label": "_linter.py", "language": "py", "sha256": "f3c1132fa2972d19", "symbol_count": 7, "symbols": [{"doc": "Enforces architectural rules over scanned nodes and edges.\n\nChecks file length, cross-layer import violations, and circular\ndependencies. Returns structured LinterViolation instances for\neach detected issue.", "kind": "class", "line": 18, "name": "ArchitectureLinter", "signature": "class ArchitectureLinter"}, {"kind": "method", "line": 31, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run all linter rules and return violations.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    layers: Optional mapping from node_id to layer name.\n    content_map: Optional mapping from node_id to file content.\n\nReturns:\n    List of LinterViolation instances sorted by severity.", "kind": "method", "line": 34, "name": "lint", "signature": "def lint(self, nodes, edges, resolved_edges, layers, content_map)"}, {"doc": "Check files against maximum line count threshold.", "kind": "method", "line": 65, "name": "_check_file_length", "signature": "def _check_file_length(self, nodes, content_map)"}, {"doc": "Check for forbidden cross-layer imports.", "kind": "method", "line": 96, "name": "_check_cross_layer_violations", "signature": "def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)"}, {"doc": "Check for circular dependencies in the resolved import graph.", "kind": "method", "line": 127, "name": "_check_circular_dependencies", "signature": "def _check_circular_dependencies(self, nodes, resolved_edges)"}, {"kind": "method", "line": 146, "name": "_dfs", "signature": "def _dfs(current)"}]}, {"doc": "MCP (Model Context Protocol) stdio server for ReadMenator.  Exposes the full codebase knowledge graph as MCP tools and resources, allowing AI agents to query structural information without parsing KNOWLEDGE_BASE.md as text. Each query costs ~50-200 tokens vs 2000-8000+ tokens of reading the full KB file.  Tools: readmenator.summary       — codebase overview (files, symbols, langs) readmenator.query         — free-text symbol/file search readmenator.explain       — detailed symbol explanation readmenator.path          — dependency chain between two symbols readmenator.findings      — security findings readmenator.taint         — taint propagation analysis readmenator.hotspots      — hotspot analysis readmenator.cycles        — dependency cycles readmenator.communities   — community detection readmenator.layers        — architectural layers readmenator.layer_violations — layer rule violations readmenator.rebuild       — regenerate KNOWLEDGE_BASE.md readmenator.update        — incremental update (SHA256 cache) readmenator.export_json   — export graph.json readmenator.security_summary — security audit summary  Resources: readmenator://summary     — structured JSON summary readmenator://graph       — graph data (nodes + edges) readmenator://file/{path} — file details readmenator://symbol/{name} — symbol details readmenator://findings    — security findings", "id": "readmenator/_mcp_server.py", "kind": "module", "label": "_mcp_server.py", "language": "py", "sha256": "96151f2ad60cfb2d", "symbol_count": 52, "symbols": [{"kind": "class", "line": 58, "name": "MCPError", "signature": "class MCPError(Exception)"}, {"kind": "class", "line": 71, "name": "MCPRequest", "signature": "class MCPRequest"}, {"kind": "class", "line": 92, "name": "MCPTool", "signature": "class MCPTool"}, {"kind": "class", "line": 119, "name": "MCPResource", "signature": "class MCPResource"}, {"kind": "class", "line": 146, "name": "MCPServer", "signature": "class MCPServer"}, {"doc": "CLI entry point for `readmenator serve <path>`.", "kind": "method", "line": 796, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 59, "name": "__init__", "signature": "def __init__(self, code, message, data)"}, {"kind": "method", "line": 72, "name": "__init__", "signature": "def __init__(self, msg)"}, {"kind": "method", "line": 79, "name": "is_notification", "signature": "def is_notification(self)"}, {"kind": "method", "line": 82, "name": "response", "signature": "def response(self, result)"}, {"kind": "method", "line": 85, "name": "error", "signature": "def error(self, code, message, data)"}, {"kind": "method", "line": 93, "name": "__init__", "signature": "def __init__(self, name, description, handler, input_schema)"}, {"kind": "method", "line": 108, "name": "definition", "signature": "def definition(self)"}, {"kind": "method", "line": 115, "name": "call", "signature": "def call(self, arguments)"}, {"kind": "method", "line": 120, "name": "__init__", "signature": "def __init__(self, uri, name, description, mime_type, handler)"}, {"kind": "method", "line": 134, "name": "definition", "signature": "def definition(self)"}, {"kind": "method", "line": 142, "name": "read", "signature": "def read(self)"}, {"kind": "method", "line": 147, "name": "__init__", "signature": "def __init__(self, app, target_dir)"}, {"kind": "method", "line": 155, "name": "register_tool", "signature": "def register_tool(self, tool)"}, {"kind": "method", "line": 158, "name": "register_resource", "signature": "def register_resource(self, resource)"}, {"kind": "method", "line": 161, "name": "_ensure_kb", "signature": "def _ensure_kb(self)"}, {"kind": "method", "line": 173, "name": "_handle_initialize", "signature": "def _handle_initialize(self, req)"}, {"kind": "method", "line": 187, "name": "_handle_list_tools", "signature": "def _handle_list_tools(self, req)"}, {"kind": "method", "line": 192, "name": "_handle_call_tool", "signature": "def _handle_call_tool(self, req)"}, {"kind": "method", "line": 214, "name": "_handle_list_resources", "signature": "def _handle_list_resources(self, req)"}, {"kind": "method", "line": 219, "name": "_handle_read_resource", "signature": "def _handle_read_resource(self, req)"}, {"kind": "method", "line": 241, "name": "dispatch", "signature": "def dispatch(self, req)"}, {"kind": "method", "line": 261, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 285, "name": "_register_all", "signature": "def _register_all(self)"}, {"kind": "method", "line": 467, "name": "_scan", "signature": "def _scan(self)"}, {"kind": "method", "line": 473, "name": "_scan_deep", "signature": "def _scan_deep(self)"}, {"kind": "method", "line": 481, "name": "_tool_summary", "signature": "def _tool_summary(self)"}, {"kind": "method", "line": 519, "name": "_tool_query", "signature": "def _tool_query(self, text)"}, {"kind": "method", "line": 524, "name": "_tool_explain", "signature": "def _tool_explain(self, name)"}, {"kind": "method", "line": 536, "name": "_tool_path", "signature": "def _tool_path(self, symbol_a, symbol_b)"}, {"kind": "method", "line": 547, "name": "_tool_findings", "signature": "def _tool_findings(self, min_severity)"}, {"kind": "method", "line": 577, "name": "_tool_security_summary", "signature": "def _tool_security_summary(self)"}, {"kind": "method", "line": 582, "name": "_tool_taint", "signature": "def _tool_taint(self)"}, {"kind": "method", "line": 603, "name": "_tool_hotspots", "signature": "def _tool_hotspots(self, top_n)"}, {"kind": "method", "line": 619, "name": "_tool_cycles", "signature": "def _tool_cycles(self)"}, {"kind": "method", "line": 630, "name": "_tool_communities", "signature": "def _tool_communities(self)"}, {"kind": "method", "line": 645, "name": "_tool_layers", "signature": "def _tool_layers(self)"}, {"kind": "method", "line": 663, "name": "_tool_layer_violations", "signature": "def _tool_layer_violations(self)"}, {"kind": "method", "line": 679, "name": "_tool_rebuild", "signature": "def _tool_rebuild(self)"}, {"kind": "method", "line": 689, "name": "_tool_update", "signature": "def _tool_update(self)"}, {"kind": "method", "line": 697, "name": "_tool_export_json", "signature": "def _tool_export_json(self)"}, {"kind": "method", "line": 705, "name": "_resource_summary", "signature": "def _resource_summary(self)"}, {"kind": "method", "line": 722, "name": "_resource_graph", "signature": "def _resource_graph(self)"}, {"kind": "method", "line": 741, "name": "_resource_findings", "signature": "def _resource_findings(self)"}, {"kind": "method", "line": 757, "name": "_resource_analysis", "signature": "def _resource_analysis(self)"}, {"kind": "method", "line": 787, "name": "_resource_kb", "signature": "def _resource_kb(self)"}, {"kind": "method", "line": 791, "name": "_get_query_engine", "signature": "def _get_query_engine(self, nodes, edges, resolved)"}]}, {"doc": "Mermaid graph renderer with intelligent pruning.  Converts the internal Node/Edge graph into a Mermaid flowchart (string) suitable for embedding in Markdown. Handles node limits, deduplication, CSS-like class styling, internal import edges, and community subgraphs.", "id": "readmenator/_mermaid.py", "kind": "module", "label": "_mermaid.py", "language": "py", "sha256": "5832baaa4731cd40", "symbol_count": 4, "symbols": [{"doc": "Renders a knowledge graph to Mermaid JS flowchart syntax.\n\nNodes are ordered by import count and symbol richness; the top\n``max_nodes`` entries are included. External dependencies appear\nas dashed boxes. Internal import edges are solid arrows.\nCommunity subgraphs group related files when analysis is available.", "kind": "class", "line": 17, "name": "MermaidRenderer", "signature": "class MermaidRenderer"}, {"kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style, internal_edge_style)"}, {"doc": "Convert *node_id* to a Mermaid-safe identifier.\n\nReplaces non-alphanumeric characters with underscores and\nprepends ``n_`` if the result starts with a digit.", "kind": "method", "line": 45, "name": "_sanitize_id", "signature": "def _sanitize_id(node_id)"}, {"doc": "Produce a Mermaid flowchart string and a truncation flag.\n\nNodes are sorted by import popularity, then by symbol count.\nInternal import edges (between project files) are rendered as\nsolid arrows when *resolved_edges* is provided. Community\nsubgraphs wrap related files when *analysis* is given.\n\nReturns:\n    Tuple of (Mermaid source string, is_truncated bool).", "kind": "method", "line": 56, "name": "render", "signature": "def render(self, nodes, edges, resolved_edges, analysis)"}]}, {"doc": "Data model types for the readmenator knowledge graph.  Defines the core entity types -- Symbol, Node, Edge -- plus a utility function for pluralising symbol kind labels and a helper for constructing community analysis results. Every parser, scanner, renderer, and query engine depends on these definitions.", "id": "readmenator/_models.py", "kind": "module", "label": "_models.py", "language": "py", "sha256": "758ca743fd06046b", "symbol_count": 20, "symbols": [{"doc": "A single code symbol extracted from a source file.\n\nAttributes:\n    name: Identifier of the symbol (class name, function name, etc.).\n    kind: Semantic type (class, function, struct, enum, ...).\n    line: One-based line number where the symbol is defined.\n    doc: Optional docstring or comment extracted from the source.\n    signature: Optional method or function signature snippet.", "kind": "class", "line": 18, "name": "Symbol", "signature": "class Symbol"}, {"doc": "A file node in the knowledge graph, containing its symbols.\n\nAttributes:\n    node_id: Relative path of the file used as a unique identifier.\n    label: Base file name for display purposes.\n    kind: Type of node (typically \"module\").\n    language: Programming language derived from the file extension.\n    doc: Optional file-level documentation string.\n    symbols: List of Symbol instances defined in this file.", "kind": "class", "line": 37, "name": "Node", "signature": "class Node"}, {"doc": "A directed relationship between two nodes in the knowledge graph.\n\nAttributes:\n    source: Node ID of the source (dependent) file.\n    target: Node ID of the target (dependency) file or module.\n    relation: Semantic relation label (e.g. \"imports\", \"resolved_imports\").\n    confidence: Confidence tier (\"EXTRACTED\" for structural, \"INFERRED\" for heuristic).\n    kind: Optional typed edge kind for ranking-aware computations.", "kind": "class", "line": 58, "name": "Edge", "signature": "class Edge"}, {"doc": "A security-relevant pattern detected in a source file.\n\nAttributes:\n    file_path: Relative path of the file containing the finding.\n    line: One-based line number where the pattern was found.\n    severity: Severity level (critical, high, medium, low, info).\n    rule_id: Unique identifier for the detection rule (e.g. \"PY001\").\n    description: Human-readable explanation of the issue.\n    snippet: The offending source code line.\n    cwe: CWE identifier string (e.g. \"CWE-78\").\n    mitre_attack: MITRE ATT&CK technique ID (e.g. \"T1059.001\").", "kind": "class", "line": 77, "name": "SecurityFinding", "signature": "class SecurityFinding"}, {"doc": "Return the plural form of *kind* according to *plural_map*.\n\nFalls back to appending ``\"s\"`` when the kind is not found.\nThis prevents obvious misspellings like ``\"Classs\"``.", "kind": "method", "line": 101, "name": "pluralize_symbol_kind", "signature": "def pluralize_symbol_kind(kind, plural_map)"}, {"doc": "Result of community detection on the import graph.\n\nAttributes:\n    community_id: Integer identifier of the community.\n    label: Human-readable name for the community.\n    file_ids: Set of node IDs belonging to this community.\n    cohesion: Cohesion score (internal edges / total edges involving community).\n    size: Number of files in the community.", "kind": "class", "line": 111, "name": "CommunityResult", "signature": "class CommunityResult"}, {"doc": "Complete graph analysis output.\n\nAttributes:\n    god_nodes: List of (node_id, score) for most central nodes.\n    communities: List of CommunityResult instances.\n    surprising_connections: List of (source_node, target_node, hops, bridging_communities).\n    suggested_questions: List of plain-language exploration questions.\n    node_count: Total nodes in the graph.\n    edge_count: Total edges in the graph.", "kind": "class", "line": 130, "name": "AnalysisResult", "signature": "class AnalysisResult"}, {"doc": "A taint propagation path from source to sink through the import graph.\n\nAttributes:\n    source_file: The file that introduces the dangerous import.\n    sink_file: The file that transitively receives the taint.\n    path: List of file node IDs forming the propagation chain.\n    hops: Number of hops in the propagation path.\n    dangerous_import: The specific dangerous module or function imported.\n    severity: Inferred severity of the taint path.", "kind": "class", "line": 151, "name": "TaintPath", "signature": "class TaintPath"}, {"doc": "Complete taint propagation analysis output.\n\nAttributes:\n    paths: List of TaintPath instances discovered.\n    source_count: Number of unique taint source files.\n    sink_count: Number of unique taint sink files.", "kind": "class", "line": 172, "name": "TaintAnalysisResult", "signature": "class TaintAnalysisResult"}, {"doc": "A cycle detected in the resolved import graph.\n\nAttributes:\n    cycle: List of file node IDs forming the cycle.\n    length: Number of files in the cycle.", "kind": "class", "line": 187, "name": "DependencyCycle", "signature": "class DependencyCycle"}, {"doc": "Change impact analysis for a single file.\n\nAttributes:\n    file_id: The file that would be changed.\n    direct_dependents: Files that directly import this file.\n    transitive_dependents: Files that transitively depend on this file.\n    total_impact: Total number of affected files (direct + transitive).", "kind": "class", "line": 200, "name": "ChangeImpact", "signature": "class ChangeImpact"}, {"doc": "A hotspot file combining complexity and centrality metrics.\n\nAttributes:\n    file_id: The file node ID.\n    complexity_score: Normalised symbol count score (0-1).\n    centrality_score: Normalised god node score (0-1).\n    combined_score: Weighted combination of complexity and centrality.\n    symbol_count: Raw symbol count.\n    connection_count: Raw connection count.", "kind": "class", "line": 217, "name": "HotspotResult", "signature": "class HotspotResult"}, {"doc": "A suggested linting/security rule derived from code patterns.\n\nAttributes:\n    rule_id: Suggested rule identifier (e.g. \"RM001\").\n    severity: Suggested severity (info, warning, error).\n    description: Human-readable description of the pattern.\n    pattern: The detected pattern or code snippet.\n    file_examples: Example file paths where the pattern was found.\n    match_count: Number of times the pattern was matched.\n    language: Target language for the rule.\n    semgrep_yaml: Optional Semgrep rule YAML string.", "kind": "class", "line": 238, "name": "SuggestedRule", "signature": "class SuggestedRule"}, {"doc": "A detected architectural layer violation.\n\nAttributes:\n    source_file: The file causing the violation.\n    source_layer: The layer of the source file.\n    target_file: The file being imported.\n    target_layer: The layer of the target file.\n    description: Description of the violation.\n    severity: Severity (strict, warn, info).", "kind": "class", "line": 263, "name": "LayerViolation", "signature": "class LayerViolation"}, {"doc": "Extended analysis result combining all new analysis modules.\n\nAttributes:\n    taint: Optional taint analysis result.\n    cycles: List of dependency cycles.\n    change_impacts: List of change impact results for key files.\n    hotspots: List of hotspot results.\n    suggested_rules: List of suggested linting rules.\n    layer_violations: List of layer violations.\n    dataflow_issues: List of procedural dataflow findings.", "kind": "class", "line": 284, "name": "AnalysisResultV2", "signature": "class AnalysisResultV2"}, {"doc": "A procedural intra-function dataflow finding.\n\nAttributes:\n    file_path: Relative path of the file containing the issue.\n    function: Name of the enclosing function.\n    line: One-based line number of the suspicious operation.\n    kind: Issue kind (UNINIT_USE, DEAD_STORE, UNCHECKED_ALLOC).\n    variable: Name of the involved local variable.\n    description: Human-readable explanation of the suspicion.\n    confidence: Confidence tier (always INFERRED for heuristics).", "kind": "class", "line": 307, "name": "DataflowIssue", "signature": "class DataflowIssue"}, {"doc": "A violation detected by the architecture linter.\n\nAttributes:\n    file_path: Relative path of the file containing the violation.\n    rule_id: Unique identifier for the linter rule (e.g. \"ARC001\").\n    severity: Severity level (error, warning, info).\n    message: Human-readable description of the violation.", "kind": "class", "line": 330, "name": "LinterViolation", "signature": "class LinterViolation"}, {"doc": "A dead code symbol identified by the stripper.\n\nAttributes:\n    file_path: Relative path of the file containing the symbol.\n    symbol_name: Name of the dead symbol.\n    symbol_type: Type of symbol (function, class, method, etc.).\n    recommendation: Recommended action (MOVE_TO_TRASH, REVIEW, KEEP).", "kind": "class", "line": 347, "name": "DeadCodeReport", "signature": "class DeadCodeReport"}, {"doc": "A single refactoring action within a plan.\n\nAttributes:\n    action_type: Type of action (EXTRACT_CLASS, EXTRACT_FUNCTION, MOVE_SYMBOL).\n    source_file: The file to refactor.\n    start_line: Start line of the code range to extract.\n    end_line: End line of the code range to extract.\n    target_file: The new file to create (for EXTRACT actions).\n    description: Human-readable description of the action.", "kind": "class", "line": 364, "name": "RefactoringAction", "signature": "class RefactoringAction"}, {"doc": "A complete refactoring plan for a monolithic file.\n\nAttributes:\n    file_path: The file to refactor.\n    actions: List of refactoring actions to perform.\n    estimated_impact: Number of files affected by the refactoring.\n    current_lines: Current line count of the file.", "kind": "class", "line": 385, "name": "RefactoringPlan", "signature": "class RefactoringPlan"}]}, {"doc": "AnalyzerFactory (lazy component construction) and DeepAnalysisRunner.  Decouples the application orchestrator from concrete analyzers and runs the v2 analyses (taint, cycles, impact, hotspots, rules, layers, dataflow).", "id": "readmenator/_pipeline.py", "kind": "module", "label": "_pipeline.py", "language": "py", "sha256": "3430264b4fff1645", "symbol_count": 34, "symbols": [{"doc": "Lazy factory for all readmenator analyzer and generator instances.\n\nDecouples the application orchestrator from the concrete\ninstantiation of analysis modules. Each component is created\non first access and cached for the lifetime of the factory.", "kind": "class", "line": 49, "name": "AnalyzerFactory", "signature": "class AnalyzerFactory"}, {"doc": "Orchestrates the extended V2 analysis pipeline.\n\nRuns taint propagation, hotspot detection, cycle detection,\nchange impact, layer violations, and rule generation as a\ncoordinated batch. Isolated from the main app to reduce\ncoupling in the primary orchestration layer.", "kind": "class", "line": 292, "name": "DeepAnalysisRunner", "signature": "class DeepAnalysisRunner"}, {"kind": "method", "line": 57, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 88, "name": "scanner", "signature": "def scanner(self)"}, {"kind": "method", "line": 94, "name": "generator", "signature": "def generator(self)"}, {"kind": "method", "line": 100, "name": "analyzer", "signature": "def analyzer(self)"}, {"kind": "method", "line": 106, "name": "security", "signature": "def security(self)"}, {"kind": "method", "line": 112, "name": "exporter", "signature": "def exporter(self)"}, {"kind": "method", "line": 118, "name": "taint", "signature": "def taint(self)"}, {"doc": "Return the lazily initialised dataflow analyzer.", "kind": "method", "line": 124, "name": "dataflow", "signature": "def dataflow(self)"}, {"kind": "method", "line": 131, "name": "hotspots", "signature": "def hotspots(self)"}, {"kind": "method", "line": 137, "name": "layer_rules", "signature": "def layer_rules(self)"}, {"kind": "method", "line": 143, "name": "rule_gen", "signature": "def rule_gen(self)"}, {"kind": "method", "line": 149, "name": "sarif", "signature": "def sarif(self)"}, {"kind": "method", "line": 155, "name": "cpg", "signature": "def cpg(self)"}, {"kind": "method", "line": 164, "name": "layer_detector", "signature": "def layer_detector(self)"}, {"kind": "method", "line": 170, "name": "uml", "signature": "def uml(self)"}, {"doc": "Return the lazily initialised agent wiki generator.", "kind": "method", "line": 176, "name": "wiki", "signature": "def wiki(self)"}, {"kind": "method", "line": 183, "name": "readme_injector", "signature": "def readme_injector(self)"}, {"kind": "method", "line": 193, "name": "agent_injector", "signature": "def agent_injector(self)"}, {"doc": "Return the lazily initialised GitHub wiki publisher.", "kind": "method", "line": 203, "name": "gh_wiki", "signature": "def gh_wiki(self)"}, {"kind": "method", "line": 210, "name": "agent_output", "signature": "def agent_output(self)"}, {"doc": "Return the lazily initialised system map builder.", "kind": "method", "line": 216, "name": "diagram_builder", "signature": "def diagram_builder(self)"}, {"doc": "Return the lazily initialised interactive map renderer.", "kind": "method", "line": 223, "name": "diagram_renderer", "signature": "def diagram_renderer(self)"}, {"doc": "Return the lazily initialised system map validator.", "kind": "method", "line": 230, "name": "diagram_validator", "signature": "def diagram_validator(self)"}, {"doc": "Return the lazily initialised documentation site publisher.", "kind": "method", "line": 237, "name": "diagram_publisher", "signature": "def diagram_publisher(self)"}, {"doc": "Return the lazily initialised vis.js network renderer.", "kind": "method", "line": 244, "name": "vis_renderer", "signature": "def vis_renderer(self)"}, {"doc": "Return the lazily initialised cinematic video renderer.", "kind": "method", "line": 251, "name": "video", "signature": "def video(self)"}, {"kind": "method", "line": 257, "name": "build_typed_graph", "signature": "def build_typed_graph(self, nodes, edges, resolved_edges)"}, {"doc": "Create a CompositeRanker for the given typed graph.", "kind": "method", "line": 267, "name": "make_ranker", "signature": "def make_ranker(self, typed_graph)"}, {"kind": "method", "line": 284, "name": "last_category", "signature": "def last_category(self)"}, {"kind": "method", "line": 288, "name": "last_typed_graph", "signature": "def last_typed_graph(self)"}, {"kind": "method", "line": 301, "name": "__init__", "signature": "def __init__(self, factory)"}, {"kind": "method", "line": 304, "name": "run", "signature": "def run(self, nodes, edges, resolved_edges, layers, content_map)"}]}, {"doc": "Functors and projections for the readmenator code category.  Defines projection functors that preserve structure but change the point of view: F_docs (code -> documentation), F_risk (code -> risk), and view-based projections for architecture, execution, quality, and change impact analysis.", "id": "readmenator/_projections.py", "kind": "module", "label": "_projections.py", "language": "py", "sha256": "1bf2c182b76b0945", "symbol_count": 15, "symbols": [{"doc": "A functor from C_code to another category.\n\nMaps nodes and morphisms while preserving composition structure.", "kind": "class", "line": 17, "name": "Projection", "signature": "class Projection(Protocol)"}, {"doc": "Identity functor: maps everything to itself.", "kind": "class", "line": 32, "name": "IdentityProjection", "signature": "class IdentityProjection"}, {"doc": "F_docs: project code to documentation.\n\nKeeps only nodes that have docstrings or are referenced in README.\nUseful for quantifying documentation gaps.", "kind": "class", "line": 42, "name": "DocProjection", "signature": "class DocProjection"}, {"doc": "F_risk: project code to risk/fragility nodes.\n\nNodes are transformed with risk attributes: fan-in, fan-out,\nsymbol count, test absence, and public API exposure.", "kind": "class", "line": 63, "name": "RiskProjection", "signature": "class RiskProjection"}, {"doc": "Apply a named view to produce a projected category.\n\nView config format::\n    {\n        \"edge_types\": [EdgeKind.IMPORTS, EdgeKind.DEFINES, ...],\n        \"direction\": \"forward\" | \"reverse\",  # default \"forward\"\n    }\n\nArgs:\n    category: Source category.\n    view_config: View definition dict.\n\nReturns:\n    A new Category with only matching morphisms.", "kind": "method", "line": 95, "name": "apply_view", "signature": "def apply_view(category, view_config)"}, {"doc": "Map a code node. Return None to exclude.", "kind": "method", "line": 23, "name": "map_node", "signature": "def map_node(self, node)"}, {"doc": "Map a morphism. Return None to exclude.", "kind": "method", "line": 27, "name": "map_morphism", "signature": "def map_morphism(self, m)"}, {"kind": "method", "line": 35, "name": "map_node", "signature": "def map_node(self, node)"}, {"kind": "method", "line": 38, "name": "map_morphism", "signature": "def map_morphism(self, m)"}, {"kind": "method", "line": 49, "name": "__init__", "signature": "def __init__(self, documented_ids)"}, {"kind": "method", "line": 52, "name": "map_node", "signature": "def map_node(self, node)"}, {"kind": "method", "line": 57, "name": "map_morphism", "signature": "def map_morphism(self, m)"}, {"kind": "method", "line": 70, "name": "__init__", "signature": "def __init__(self, fan_in, fan_out, test_files)"}, {"kind": "method", "line": 80, "name": "map_node", "signature": "def map_node(self, node)"}, {"kind": "method", "line": 91, "name": "map_morphism", "signature": "def map_morphism(self, m)"}]}, {"doc": "Purpose extraction shared by every agent-facing document generator.  Turns raw file and symbol docstrings into one clean, bounded sentence that tells a reader what a file is for. Banner rules, SPDX headers, encoding cookies, and bare file names are rejected; files without a module docstring fall back to the docstring of their primary symbol so agent indexes never show an empty purpose when the code explains itself.", "id": "readmenator/_purpose.py", "kind": "module", "label": "_purpose.py", "language": "py", "sha256": "539642983e59296b", "symbol_count": 7, "symbols": [{"doc": "Return True for doc lines that carry no purpose signal.\n\nArgs:\n    text: One doc line.\n\nReturns:\n    Whether the line is too short, an encoding cookie, or symbol noise.", "kind": "function", "line": 26, "name": "is_garbage_doc", "signature": "def is_garbage_doc(text)"}, {"doc": "Return the purpose signal of a doc first line, or an empty string.\n\nArgs:\n    text: First line of a file or symbol docstring.\n\nReturns:\n    The line without banners, SPDX tags, and leading file names.", "kind": "function", "line": 43, "name": "clean_purpose", "signature": "def clean_purpose(text)"}, {"doc": "Escape markdown table breaking characters in one line of text.\n\nArgs:\n    text: Arbitrary text destined for a table cell.\n\nReturns:\n    Single-line text with pipes escaped.", "kind": "function", "line": 66, "name": "escape_cell", "signature": "def escape_cell(text)"}, {"doc": "Truncate text at a word boundary and mark the cut with an ellipsis.\n\nArgs:\n    text: Text to shorten.\n    max_chars: Maximum length of the returned string.\n\nReturns:\n    The original text when short enough, otherwise a word-aligned prefix.", "kind": "function", "line": 78, "name": "truncate_words", "signature": "def truncate_words(text, max_chars)"}, {"doc": "Return the first clean sentence of the first meaningful paragraph.\n\nArgs:\n    doc: Full docstring text.\n\nReturns:\n    One sentence with whitespace collapsed, or an empty string.", "kind": "function", "line": 98, "name": "first_sentence", "signature": "def first_sentence(doc)"}, {"doc": "Pick the documented symbol that best represents a file.\n\nPublic symbols outrank private ones and type-like kinds outrank\nfunctions; ties fall back to source order.\n\nArgs:\n    symbols: Symbols extracted from one file.\n\nReturns:\n    The representative documented symbol, or None.", "kind": "function", "line": 116, "name": "_primary_symbol", "signature": "def _primary_symbol(symbols)"}, {"doc": "Return a bounded one-sentence purpose for a file node.\n\nArgs:\n    node: Scanned file node.\n    max_chars: Maximum characters of the returned purpose.\n\nReturns:\n    Module doc sentence, else ``Symbol: sentence`` from the primary\n    documented symbol, else an empty string.", "kind": "function", "line": 140, "name": "file_purpose", "signature": "def file_purpose(node, max_chars)"}]}, {"doc": "Query engine for the readmenator knowledge base.  Supports natural-language-like search (``query``), symbol explanation (``explain``), dependency-path tracing (``find_path``), ranked queries via PageRank/PPR integration (``ranked_query``), and a concise codebase overview (``summary``). All queries operate on an in-memory index built from the scanned Node/Edge list.", "id": "readmenator/_query.py", "kind": "module", "label": "_query.py", "language": "py", "sha256": "4677486e84eaae1c", "symbol_count": 17, "symbols": [{"doc": "In-memory query engine over the scanned knowledge graph.\n\nBuilds a symbol-name index and an import-adjacency graph on\nconstruction. Provides exact and fuzzy symbol lookup, detailed\nexplanation output, BFS shortest-path resolution, free-text\nsearch, and a summary report.", "kind": "class", "line": 25, "name": "QueryEngine", "signature": "class QueryEngine"}, {"doc": "Initialise internal indexes from scanned data.\n\nArgs:\n    nodes: List of scanned file nodes.\n    edges: List of import-relationship edges.\n    resolved_edges: Optional resolved-import edges (both\n        source and target are project file IDs).\n    ranker: Optional CompositeRanker for ranked queries.\n    config: Optional RankConfig if ranker is not provided.", "kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, nodes, edges, resolved_edges, ranker, config)"}, {"doc": "Build a default CompositeRanker from the loaded data.", "kind": "method", "line": 64, "name": "_init_default_ranker", "signature": "def _init_default_ranker(self)"}, {"doc": "Answer *query* with a ranked list of relevant nodes.\n\nUses Personalized PageRank seeded from lexical matches\nagainst the query text, combined with authority, test\ncoverage, doc coverage, and freshness signals.\n\nArgs:\n    query: Free-text query string.\n    top_n: Number of results to return (default: RankConfig.top_n).\n\nReturns:\n    A RankedResult with scored items and explanations.", "kind": "method", "line": 73, "name": "ranked_query", "signature": "def ranked_query(self, query, top_n)"}, {"doc": "Estimate test coverage per file.\n\nA file is considered 'tested' if a test file imports it.\nReturns fraction of symbols referenced across test files.", "kind": "method", "line": 124, "name": "_estimate_test_coverage", "signature": "def _estimate_test_coverage(self)"}, {"doc": "Estimate documentation coverage per file.\n\nA file has doc coverage if it has a file-level docstring or\nany of its symbols have docstrings.", "kind": "method", "line": 150, "name": "_estimate_doc_coverage", "signature": "def _estimate_doc_coverage(self)"}, {"doc": "Build a name-to-list-of-(node, symbol) lookup.\n\nReturns:\n    Dict mapping symbol names to list of (Node, Symbol) tuples.", "kind": "method", "line": 170, "name": "_build_symbol_index", "signature": "def _build_symbol_index(self)"}, {"doc": "Build an adjacency map from import edges.\n\nReturns:\n    Dict mapping each file node_id to its set of import targets.", "kind": "method", "line": 184, "name": "_build_import_graph", "signature": "def _build_import_graph(self)"}, {"doc": "Build an adjacency map from resolved import edges.\n\nOnly contains edges where both source and target are\nproject files (not external modules).\n\nReturns:\n    Dict mapping each file node_id to files it imports within the project.", "kind": "method", "line": 200, "name": "_build_resolved_graph", "signature": "def _build_resolved_graph(self)"}, {"doc": "Look up *name* by exact match, then by substring fuzzy match.\n\nReturns:\n    A list of (Node, Symbol) tuples, or ``None`` if not found.", "kind": "method", "line": 220, "name": "find_symbol", "signature": "def find_symbol(self, name)"}, {"doc": "Return a detailed multi-line explanation of *name*.\n\nIncludes kind, file path, line number, docstring, signature,\nimports, reverse dependencies (\"imported by\"), and sibling\nsymbols in the same file.\n\nReturns:\n    Formatted string or ``None`` if the symbol is not found.", "kind": "method", "line": 238, "name": "explain", "signature": "def explain(self, name)"}, {"doc": "List all node IDs that import *target*.", "kind": "method", "line": 277, "name": "_find_incoming_imports", "signature": "def _find_incoming_imports(self, target)"}, {"doc": "Find the shortest import path from *symbol_a* to *symbol_b*.\n\nUses BFS on the resolved import graph (project-internal edges)\nfirst, traversing in both directions (forward = A imports B,\nreverse = B is imported by A). Falls back to the raw import\ngraph if no resolved path exists.\n\nReturns:\n    List of file node IDs forming the dependency chain, or ``None``.", "kind": "method", "line": 285, "name": "find_path", "signature": "def find_path(self, symbol_a, symbol_b)"}, {"doc": "Convert a directed graph to a bidirectional one.\n\nFor each edge A→B, adds both A→B and B→A edges.", "kind": "method", "line": 315, "name": "_make_bidirectional", "signature": "def _make_bidirectional(graph)"}, {"doc": "Run BFS to find the shortest path from *start* to *goal*.\n\nReturns:\n    List of node IDs or ``None`` if no path exists.", "kind": "method", "line": 331, "name": "_bfs_shortest_path", "signature": "def _bfs_shortest_path(self, graph, start, goal)"}, {"doc": "Free-text search over symbols and file paths.\n\nTokenises the input, matches against symbol names (substring)\nand then against file paths as a fallback. Returns a\nhuman-readable result string summarising matches or a\nno-results message with KB statistics.", "kind": "method", "line": 355, "name": "query", "signature": "def query(self, question)"}, {"doc": "Return a concise overview of the loaded knowledge base.\n\nReports file count, symbol count, import count, language\ndiversity, top-level modules (by import popularity), and\nlists of key class-like and function-like symbols.", "kind": "method", "line": 411, "name": "summary", "signature": "def summary(self)"}]}, {"doc": "PageRank, Personalized PageRank, HITS, and composite scoring.  Provides typed-graph-aware ranking for the readmenator knowledge graph. Global PageRank measures structural authority; Personalized PageRank measures query-specific relevance; HITS separates authorities from hubs; composite scoring combines multiple quality signals into a single explainable rank.", "id": "readmenator/_rank.py", "kind": "module", "label": "_rank.py", "language": "py", "sha256": "9cea35495030eb51", "symbol_count": 17, "symbols": [{"doc": "Tuneable parameters for the ranking system.\n\nAttributes:\n    alpha: Damping factor for PageRank (default 0.85).\n    max_iter: Maximum power-iteration steps.\n    tolerance: Convergence threshold (L1 norm).\n    top_n: Default number of ranked results to return.\n    noise_penalty: Multiplier applied to hub-penalty names\n        when they are not part of the query seeds.\n    composite_ppr_weight: Weight for PPR in composite score.\n    composite_authority_weight: Weight for global PageRank.\n    composite_test_weight: Weight for test coverage signal.\n    composite_doc_weight: Weight for documentation coverage.\n    composite_freshness_weight: Weight for code freshness.", "kind": "class", "line": 32, "name": "RankConfig", "signature": "class RankConfig"}, {"doc": "Compute global PageRank on the typed weighted graph.\n\nUses power iteration on the stochastic matrix derived from\nthe TypedGraph's edge weights. Dangling nodes (no outgoing\nedges) are handled by uniform random teleportation.\n\nArgs:\n    graph: A TypedGraph instance with weighted edges.\n    alpha: Damping factor (probability of following an edge).\n    max_iter: Maximum power-iteration steps.\n    tolerance: Convergence threshold (L1 norm).\n\nReturns:\n    Dict mapping node_id -> PageRank score. Scores sum to 1.0.", "kind": "method", "line": 61, "name": "global_pagerank", "signature": "def global_pagerank(graph, alpha, max_iter, tolerance)"}, {"doc": "Compute Personalized PageRank with a seed-node preference vector.\n\nInstead of uniform teleportation, probability mass is distributed\naccording to the seed vector. This makes the ranking sensitive to\na specific query or context.\n\nArgs:\n    graph: A TypedGraph instance.\n    seeds: Dict mapping seed node_id -> preference mass (sums to 1.0).\n    alpha: Damping factor.\n    max_iter: Maximum power-iteration steps.\n    tolerance: Convergence threshold (L1 norm).\n\nReturns:\n    Dict mapping node_id -> PPR score. Scores sum to 1.0.", "kind": "method", "line": 119, "name": "personalized_pagerank", "signature": "def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)"}, {"doc": "Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.\n\nAuthorities are nodes with many incoming edges from good hubs.\nHubs are nodes with many outgoing edges to good authorities.\n\nReturns:\n    Tuple of (authorities, hubs) as dicts mapping node_id -> score.\n    Scores are L2-normalised.", "kind": "method", "line": 189, "name": "hits", "signature": "def hits(graph, max_iter, tolerance)"}, {"doc": "Build a PPR seed vector from a natural-language query string.\n\nMatches query tokens against node IDs, labels, and symbol names.\nSeeds are assigned equal mass. If no match is found, returns\nempty dict (will use uniform teleportation).\n\nArgs:\n    query: Free-text query string.\n    node_ids: All valid node IDs.\n    node_labels: Mapping from node_id -> display label.\n    symbols: Mapping from node_id -> list of symbol names.\n\nReturns:\n    Dict of seed node_id -> equal mass fraction.", "kind": "method", "line": 240, "name": "build_seeds_from_query", "signature": "def build_seeds_from_query(query, node_ids, node_labels, symbols)"}, {"doc": "Build a PPR seed vector from anchor pattern strings.\n\nNodes whose ID or label contains any anchor pattern receive\nequal seed mass. Useful for section-level seeding.\n\nArgs:\n    node_ids: All valid node IDs.\n    anchor_patterns: List of substrings to match.\n\nReturns:\n    Dict of seed node_id -> equal mass fraction.", "kind": "method", "line": 286, "name": "build_seeds_for_context", "signature": "def build_seeds_for_context(node_ids, anchor_patterns)"}, {"doc": "A single ranked result with score decomposition.\n\nAttributes:\n    node_id: The ranked node ID.\n    composite_score: Final multi-signal score.\n    ppr_score: Personalized PageRank contribution.\n    authority_score: Global PageRank contribution.\n    test_coverage: Fraction of symbols referenced in test files.\n    doc_coverage: Fraction of symbols with documentation.\n    freshness: Decay-weighted recency signal.\n    justification_paths: Shortest paths from seed nodes to this node.", "kind": "class", "line": 320, "name": "RankedItem", "signature": "class RankedItem"}, {"doc": "Complete ranking result for a query or context.\n\nAttributes:\n    query: The query string or context label.\n    items: Ranked items in descending score order.\n    config: The RankConfig used.\n    seed_nodes: The seed node IDs used for PPR.\n    model_version: Version identifier for the ranking model.", "kind": "class", "line": 349, "name": "RankedResult", "signature": "class RankedResult"}, {"doc": "Combines PPR, authority, test/doc coverage, and freshness.\n\nProduces a single composite score per node:\nS_q(n) = w_ppr * PPR_q(n) + w_auth * Auth(n) + w_test * Test(n)\n       + w_doc * Doc(n) + w_fresh * Fresh(n)", "kind": "class", "line": 377, "name": "CompositeRanker", "signature": "class CompositeRanker"}, {"doc": "Format a human-readable explanation for a ranked item.", "kind": "method", "line": 512, "name": "_format_explanation", "signature": "def _format_explanation(item, result)"}, {"kind": "method", "line": 344, "name": "label", "signature": "def label(self)"}, {"kind": "method", "line": 366, "name": "top", "signature": "def top(self, n)"}, {"doc": "Return a human-readable explanation of why *node_id* ranks as it does.", "kind": "method", "line": 369, "name": "explain", "signature": "def explain(self, node_id)"}, {"kind": "method", "line": 385, "name": "__init__", "signature": "def __init__(self, graph, config)"}, {"kind": "method", "line": 394, "name": "_get_global_pr", "signature": "def _get_global_pr(self)"}, {"doc": "Compute composite ranking for a query.\n\nArgs:\n    query: Query string.\n    seeds: PPR seed vector.\n    category: Category with morphisms for path finding.\n    node_ids: All valid node IDs.\n    test_coverage: Optional dict of node_id -> test coverage (0-1).\n    doc_coverage: Optional dict of node_id -> doc coverage (0-1).\n    freshness: Optional dict of node_id -> freshness (0-1).\n\nReturns:\n    A RankedResult with scored and sorted items.", "kind": "method", "line": 404, "name": "rank", "signature": "def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)"}, {"doc": "Find shortest paths from any seed to target.", "kind": "method", "line": 486, "name": "_find_justification_paths", "signature": "def _find_justification_paths(self, target, seed_ids, category, max_paths)"}]}, {"doc": "Injects a knowledge base section into the project README (Markdown or RST).", "id": "readmenator/_readme_injector.py", "kind": "module", "label": "_readme_injector.py", "language": "py", "sha256": "ef4591270405752e", "symbol_count": 8, "symbols": [{"doc": "Injects a link to KNOWLEDGE_BASE.md into the project README.\n\nDetects the project's README file, checks if injection is already\npresent, and appends a descriptive section about the knowledge base\nso that both human developers and AI agents know it exists.", "kind": "class", "line": 70, "name": "ReadmeInjector", "signature": "class ReadmeInjector"}, {"kind": "method", "line": 78, "name": "__init__", "signature": "def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)"}, {"kind": "method", "line": 88, "name": "inject", "signature": "def inject(self, project_root)"}, {"kind": "method", "line": 117, "name": "_extract_current_injection", "signature": "def _extract_current_injection(content)"}, {"kind": "method", "line": 126, "name": "_remove_old_injection", "signature": "def _remove_old_injection(content)"}, {"kind": "method", "line": 136, "name": "remove", "signature": "def remove(self, project_root)"}, {"kind": "method", "line": 165, "name": "_find_readme", "signature": "def _find_readme(root)"}, {"kind": "method", "line": 172, "name": "_build_injection", "signature": "def _build_injection(self, suffix)"}]}, {"doc": "Monolithic file refactoring planner for the readmenator knowledge graph.  Identifies large files exceeding configurable thresholds and generates deterministic refactoring plans based on symbol extraction and cohesive cluster detection. Never auto-executes; only produces plans.", "id": "readmenator/_refactorizer.py", "kind": "module", "label": "_refactorizer.py", "language": "py", "sha256": "e7441939d0acf9ea", "symbol_count": 9, "symbols": [{"doc": "Generates refactoring plans for monolithic files.\n\nAnalyzes files exceeding the line threshold, extracts symbol\nboundaries, detects cohesive clusters via import analysis, and\nproduces structured refactoring plans without auto-execution.", "kind": "class", "line": 24, "name": "MonolithRefactorizer", "signature": "class MonolithRefactorizer"}, {"kind": "method", "line": 32, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Identify monolithic files and generate refactoring plans.\n\nArgs:\n    nodes: Scanned file nodes.\n    edges: Import edges.\n    resolved_edges: Optional resolved-import edges.\n    content_map: Optional mapping from node_id to file content.\n\nReturns:\n    List of RefactoringPlan instances for files needing refactoring.", "kind": "method", "line": 35, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges, content_map)"}, {"kind": "method", "line": 70, "name": "_get_line_count", "signature": "def _get_line_count(self, file_id, content_map)"}, {"kind": "method", "line": 82, "name": "_plan_refactoring", "signature": "def _plan_refactoring(self, node, edges, resolved_edges, content_map)"}, {"kind": "method", "line": 126, "name": "_group_symbols_by_kind", "signature": "def _group_symbols_by_kind(self, symbols)"}, {"kind": "method", "line": 132, "name": "_suggest_target_file", "signature": "def _suggest_target_file(self, source_file, kind)"}, {"kind": "method", "line": 147, "name": "_estimate_impact", "signature": "def _estimate_impact(self, file_id, resolved_edges)"}, {"kind": "method", "line": 156, "name": "generate_script", "signature": "def generate_script(self, plan, project_root)"}]}, {"doc": "Import path resolver for the readmenator knowledge graph.  Maps raw import strings (e.g. ``\"os\"``, ``\"../utils\"``, ``\"java.util.List\"``) to actual file node IDs within the scanned project so that dependency- tracing operations work on concrete files rather than opaque strings.", "id": "readmenator/_resolver.py", "kind": "module", "label": "_resolver.py", "language": "py", "sha256": "a1e4b13df0c80b33", "symbol_count": 17, "symbols": [{"doc": "Resolves raw import strings to project file paths.\n\nUses heuristics tuned to each language's import conventions:\nPython dots to slashes, Java dots to directory separators,\nrelative-path resolution, and extensionless module detection.", "kind": "class", "line": 18, "name": "ImportResolver", "signature": "class ImportResolver"}, {"doc": "Initialise the resolver with all known file paths.\n\nArgs:\n    file_ids: List of relative file paths from the scan.\n    root: Root directory for relative-path resolution.\n    extensions: Known source extensions, defaults to Config.\n    include_dirs: Extra include search dirs (``-I`` style).", "kind": "method", "line": 61, "name": "__init__", "signature": "def __init__(self, file_ids, root, extensions, include_dirs)"}, {"doc": "Map file stems (without extension) to their full paths.", "kind": "method", "line": 83, "name": "_build_stem_index", "signature": "def _build_stem_index(self, file_ids)"}, {"doc": "Map directory paths to the files they contain.", "kind": "method", "line": 93, "name": "_build_dir_index", "signature": "def _build_dir_index(self, file_ids)"}, {"doc": "Resolve an import string to a concrete project file path.\n\nArgs:\n    import_str: The raw import string from the parser.\n    source_file: The file that contains the import (for relative resolution).\n\nReturns:\n    Matching file node ID or ``None`` if no match found.", "kind": "method", "line": 110, "name": "resolve", "signature": "def resolve(self, import_str, source_file)"}, {"doc": "Resolve *import_str* to all possible matching project file paths.\n\nArgs:\n    import_str: The raw import string.\n    source_file: The file that contains the import.\n\nReturns:\n    List of matching file node IDs (may be empty).", "kind": "method", "line": 163, "name": "resolve_all", "signature": "def resolve_all(self, import_str, source_file)"}, {"doc": "Resolve *import_str* against configured ``-I`` include dirs.\n\nArgs:\n    import_str: Raw header path without ``sys:`` prefix.\n\nReturns:\n    Matching file node ID or ``None``.", "kind": "method", "line": 179, "name": "_resolve_include_dirs", "signature": "def _resolve_include_dirs(self, import_str)"}, {"doc": "Resolve a relative import (starts with ``.`` or ``..``).", "kind": "method", "line": 199, "name": "_resolve_relative", "signature": "def _resolve_relative(self, import_str, source_file)"}, {"doc": "Resolve a path-like import verbatim against the source directory.\n\nCovers quoted C-family includes such as ``\"utils.h\"`` or\n``\"lib/net.h\"`` which name a project file relative to the\nincluding file.", "kind": "method", "line": 217, "name": "_resolve_verbatim", "signature": "def _resolve_verbatim(self, import_str, source_file)"}, {"doc": "Resolve a bare module name by appending known extensions.", "kind": "method", "line": 235, "name": "_resolve_extensionless", "signature": "def _resolve_extensionless(self, import_str, source_file)"}, {"doc": "Resolve as a package directory with __init__ or index file.", "kind": "method", "line": 244, "name": "_resolve_directory_init", "signature": "def _resolve_directory_init(self, import_str, source_file)"}, {"doc": "Resolve a bare top-level name to a root package ``__init__.py``.\n\nPython prefers a package directory over a same-named module, so\n``import pkg`` must map to ``pkg/__init__.py`` even when a\n``pkg.py`` launcher shim exists; stem matching would otherwise\npick the shim and fabricate dependency cycles.", "kind": "method", "line": 254, "name": "_resolve_root_package", "signature": "def _resolve_root_package(self, import_str)"}, {"doc": "Resolve a dotted module path (Python/Java convention).", "kind": "method", "line": 269, "name": "_resolve_module_dotpath", "signature": "def _resolve_module_dotpath(self, import_str)"}, {"doc": "Match a slash-qualified include against project path suffixes.\n\nCovers include-directory style references such as\n``\"kernel/mm.h\"`` mapping to ``\"include/kernel/mm.h\"``. Only\nunambiguous matches resolve.", "kind": "method", "line": 291, "name": "_resolve_suffix_match", "signature": "def _resolve_suffix_match(self, import_str)"}, {"doc": "Match by exact file basename including extension.\n\nCovers the classic C pair pattern where ``kernel.h`` is\nincluded but ``kernel.c`` shares its stem: stem matching\nstays ambiguous while the basename is unique. Only\nunambiguous matches resolve.", "kind": "method", "line": 306, "name": "_resolve_basename_match", "signature": "def _resolve_basename_match(self, import_str)"}, {"doc": "Match by file stem only (last resort).", "kind": "method", "line": 324, "name": "_resolve_stem_match", "signature": "def _resolve_stem_match(self, import_str)"}, {"doc": "Remove a trailing known source extension from a file name.\n\nArgs:\n    name: Base file name which may carry an extension.\n\nReturns:\n    The file stem used for stem index lookups.", "kind": "method", "line": 333, "name": "_strip_extension", "signature": "def _strip_extension(self, name)"}]}, {"doc": "Suggested linting rule generator producing Semgrep YAML from detected antipatterns.", "id": "readmenator/_rule_gen.py", "kind": "module", "label": "_rule_gen.py", "language": "py", "sha256": "40dca3acec597dd6", "symbol_count": 9, "symbols": [{"doc": "Generates suggested linting and security rules from code patterns.\n\nAnalyses the scanned codebase for repeated patterns that suggest\nproject-specific linting rules: bare except clauses, repeated\ntype annotations, common security antipatterns, and naming\nconvention violations. Outputs Semgrep YAML rules to a directory.", "kind": "class", "line": 14, "name": "RuleGenerator", "signature": "class RuleGenerator"}, {"kind": "method", "line": 90, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate suggested rules by scanning code patterns.\n\nArgs:\n    nodes: Scanned file nodes with symbols.\n    content_map: Optional mapping of file paths to their source content\n        for deeper pattern matching.\n\nReturns:\n    List of SuggestedRule instances.", "kind": "method", "line": 94, "name": "generate", "signature": "def generate(self, nodes, content_map)"}, {"doc": "Write suggested rules to Semgrep YAML files in output_dir.\n\nReturns the number of rule files written.", "kind": "method", "line": 122, "name": "write_rules", "signature": "def write_rules(self, rules, output_dir)"}, {"doc": "Group nodes by their language extension.", "kind": "method", "line": 161, "name": "_group_by_language", "signature": "def _group_by_language(self, nodes)"}, {"doc": "Analyze a single language group for rule suggestions.", "kind": "method", "line": 171, "name": "_analyze_language", "signature": "def _analyze_language(self, lang, nodes, content_map)"}, {"doc": "Detect known antipatterns across all files.", "kind": "method", "line": 204, "name": "_detect_antipatterns", "signature": "def _detect_antipatterns(self, nodes, content_map)"}, {"doc": "Infer target language for a built-in antipattern rule.", "kind": "method", "line": 250, "name": "_infer_language_for_rule", "signature": "def _infer_language_for_rule(rule_id)"}, {"doc": "Generate the next rule identifier.", "kind": "method", "line": 260, "name": "_next_rule_id", "signature": "def _next_rule_id(self)"}]}, {"doc": "SARIF v2.1.0 exporter for security findings (GitHub Code Scanning compatible).", "id": "readmenator/_sarif.py", "kind": "module", "label": "_sarif.py", "language": "py", "sha256": "9cf9cfcb63cbe38c", "symbol_count": 5, "symbols": [{"doc": "Exports security findings to the SARIF standard format.\n\nSARIF is an OASIS standard format for static analysis tool output.\nThis exporter produces SARIF v2.1.0 JSON compatible with GitHub\nCode Scanning, VS Code SARIF viewer, and other SARIF consumers.", "kind": "class", "line": 11, "name": "SarifExporter", "signature": "class SarifExporter"}, {"kind": "method", "line": 30, "name": "__init__", "signature": "def __init__(self, privacy_mode)"}, {"doc": "Generate a SARIF v2.1.0 JSON string from security findings.\n\nArgs:\n    findings: List of SecurityFinding instances.\n    project_name: Name of the scanned project for metadata.\n\nReturns:\n    SARIF JSON string.", "kind": "method", "line": 33, "name": "export", "signature": "def export(self, findings, project_name)"}, {"doc": "Build a SARIF reportingDescriptor (rule) object.", "kind": "method", "line": 82, "name": "_build_rule", "signature": "def _build_rule(self, finding)"}, {"doc": "Build a SARIF result object for a single finding.", "kind": "method", "line": 106, "name": "_build_result", "signature": "def _build_result(self, finding, rule_index)"}]}, {"doc": "Secure polyglot directory traversal and file analysis.  The scanner walks a directory tree, applies security and size checks, resolves each supported file through ParserFactory, and returns a flat list of Node and Edge objects that form the knowledge graph.", "id": "readmenator/_scanner.py", "kind": "module", "label": "_scanner.py", "language": "py", "sha256": "6e77318175215be7", "symbol_count": 14, "symbols": [{"doc": "Recursive directory scanner with security and size guards.\n\nRejects symlinks, enforces file-size and directory-depth limits,\nskips ignored directories, and silently catches parse errors\nso a single misbehaving file never breaks the full scan.\n\nSupports privacy mode (strips snippets and docstrings) and\ngitignore-aware scanning for more accurate project coverage.", "kind": "class", "line": 28, "name": "PolyglotScanner", "signature": "class PolyglotScanner"}, {"doc": "Initialise the scanner with application configuration.\n\nArgs:\n    config: Settings including ignore dirs, size limits, etc.", "kind": "method", "line": 39, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return ``True`` if any path component matches IGNORE_DIRS.", "kind": "method", "line": 50, "name": "_is_ignored", "signature": "def _is_ignored(self, path)"}, {"doc": "Return ``True`` for artifacts readmenator itself wrote into the project.\n\nRescanning its own output (agent docs, wiki, rules, maps, refactor\nscripts) would feed generated noise back into the graph and skew\nindexes, centrality, and purposes on every rebuild.\n\nArgs:\n    rel_path: Path relative to the scan root.\n\nReturns:\n    Whether the path belongs to a readmenator-generated artifact.", "kind": "method", "line": 57, "name": "_is_generated", "signature": "def _is_generated(self, rel_path)"}, {"doc": "Parse .gitignore patterns using regex (no external deps).", "kind": "method", "line": 83, "name": "_load_gitignore", "signature": "def _load_gitignore(self, root)"}, {"doc": "Convert a .gitignore glob pattern to a regex pattern.", "kind": "method", "line": 105, "name": "_gitignore_glob_to_regex", "signature": "def _gitignore_glob_to_regex(pattern)"}, {"doc": "Check if a relative path matches any .gitignore pattern.", "kind": "method", "line": 145, "name": "_is_gitignored", "signature": "def _is_gitignored(self, rel_path)"}, {"doc": "Reject symlinks and files exceeding MAX_FILE_SIZE_MB.", "kind": "method", "line": 154, "name": "_validate_path_security", "signature": "def _validate_path_security(self, path)"}, {"doc": "Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.", "kind": "method", "line": 167, "name": "_check_directory_depth", "signature": "def _check_directory_depth(self, path, root)"}, {"doc": "Extract a file-level docstring from the first lines of a source file.\n\nWalks the first FILE_HEADER_MAX_LINES lines looking for a contiguous\nblock of comments, a Python module docstring, or a shebang followed\nby comments. Returns the concatenated comment text.\n\nArgs:\n    content: Raw file content as a string.\n\nReturns:\n    Extracted file-level docstring or empty string.", "kind": "method", "line": 175, "name": "_extract_file_doc", "signature": "def _extract_file_doc(self, content)"}, {"doc": "Emit a progress message every PROGRESS_REPORT_BATCH files.\n\nArgs:\n    count: Number of files scanned so far.", "kind": "method", "line": 251, "name": "_emit_progress", "signature": "def _emit_progress(self, count)"}, {"doc": "Walk *root* recursively and produce (nodes, edges) for the graph.\n\nSecurity checks (symlinks, size, depth, ignore dirs) are applied\nper file. Parse failures are silently caught so a single broken\nfile never blocks the rest of the scan.\n\nReturns:\n    A tuple of (list of Node, list of Edge). Edges represent\n    ``imports`` relationships between scanned files.", "kind": "method", "line": 261, "name": "scan", "signature": "def scan(self, root)"}, {"doc": "Scan and also return raw file contents for deeper analysis.\n\nReturns:\n    Tuple of (nodes, edges, content_map) where content_map maps\n    node_id to raw file content.", "kind": "method", "line": 275, "name": "scan_with_content", "signature": "def scan_with_content(self, root)"}, {"doc": "Internal scan implementation returning nodes, edges, and content.", "kind": "method", "line": 286, "name": "_scan_impl", "signature": "def _scan_impl(self, root)"}]}, {"doc": "Pattern-based static security analysis for the readmenator knowledge graph.  Scans source files across all supported languages for dangerous patterns: command injection, SQL injection, XSS, weak crypto, unsafe deserialization, hardcoded secrets, and more. Pure regex-based, zero external dependencies.  Rules are loaded from readmenator-rules/_security_rules.yml at runtime, eliminating hardcoded patterns from source code (per the externalization principle). Falls back to built-in rules if the YAML file is not present.", "id": "readmenator/_security.py", "kind": "module", "label": "_security.py", "language": "py", "sha256": "a51d57d73c52ac05", "symbol_count": 32, "symbols": [{"doc": "A single security detection rule loaded from YAML or built-in.\n\nAttributes:\n    rule_id: Unique identifier (e.g. \"PY001\").\n    severity: Severity level (critical, high, medium, low, info).\n    description: Human-readable description of the issue.\n    pattern: Compiled regex to search for.\n    cwe: CWE identifier string.\n    mitre_attack: MITRE ATT&CK technique ID (e.g. \"T1059.001\").", "kind": "class", "line": 24, "name": "SecurityRule", "signature": "class SecurityRule"}, {"doc": "Parse the simplified YAML format used by _security_rules.yml.\n\nOnly supports:\n  - top-level ``rules:`` key\n  - list items starting with ``  - rule_id:``\n  - scalar key: value pairs (quoted or unquoted)\n  - block list items: ``    - \"value\"``\n  - inline lists: ``key: [item1, item2]``\n  - ``#`` comments\n\nReturns a list of rule dicts.", "kind": "method", "line": 46, "name": "_parse_minimal_yaml", "signature": "def _parse_minimal_yaml(text)"}, {"kind": "method", "line": 121, "name": "_unquote", "signature": "def _unquote(s)"}, {"doc": "Load rule dicts from the YAML rules file, or return None on failure.", "kind": "method", "line": 128, "name": "_load_rules_from_yaml", "signature": "def _load_rules_from_yaml(yaml_path)"}, {"kind": "method", "line": 148, "name": "_compile", "signature": "def _compile()"}, {"kind": "method", "line": 153, "name": "_python_rules", "signature": "def _python_rules()"}, {"kind": "method", "line": 182, "name": "_javascript_rules", "signature": "def _javascript_rules()"}, {"kind": "method", "line": 201, "name": "_c_rules", "signature": "def _c_rules()"}, {"kind": "method", "line": 222, "name": "_java_rules", "signature": "def _java_rules()"}, {"kind": "method", "line": 237, "name": "_go_rules", "signature": "def _go_rules()"}, {"kind": "method", "line": 250, "name": "_ruby_rules", "signature": "def _ruby_rules()"}, {"kind": "method", "line": 267, "name": "_php_rules", "signature": "def _php_rules()"}, {"kind": "method", "line": 284, "name": "_shell_rules", "signature": "def _shell_rules()"}, {"kind": "method", "line": 297, "name": "_csharp_rules", "signature": "def _csharp_rules()"}, {"kind": "method", "line": 310, "name": "_kotlin_rules", "signature": "def _kotlin_rules()"}, {"kind": "method", "line": 321, "name": "_swift_rules", "signature": "def _swift_rules()"}, {"kind": "method", "line": 332, "name": "_scala_rules", "signature": "def _scala_rules()"}, {"kind": "method", "line": 343, "name": "_lua_rules", "signature": "def _lua_rules()"}, {"kind": "method", "line": 354, "name": "_dart_rules", "signature": "def _dart_rules()"}, {"kind": "method", "line": 365, "name": "_rust_rules", "signature": "def _rust_rules()"}, {"kind": "method", "line": 376, "name": "_nim_rules", "signature": "def _nim_rules()"}, {"kind": "method", "line": 387, "name": "_gdscript_rules", "signature": "def _gdscript_rules()"}, {"kind": "method", "line": 398, "name": "_elixir_rules", "signature": "def _elixir_rules()"}, {"doc": "Attempt to build the rule map from the YAML rules file.\n\nReturns None if the YAML file cannot be loaded or parsed, allowing\nthe caller to fall back to built-in rules.", "kind": "method", "line": 447, "name": "_build_rules_from_yaml", "signature": "def _build_rules_from_yaml(yaml_path)"}, {"doc": "Pattern-based static security scanner.\n\nLoads rules from the external YAML rules file when available,\nfalling back to the built-in hardcoded rule sets. Walks the\ntarget directory applying rules to every supported source file.", "kind": "class", "line": 486, "name": "SecurityAnalyzer", "signature": "class SecurityAnalyzer"}, {"doc": "Return a one-line remediation hint for a security finding.\n\nLooks up the finding CWE in the guidance map and falls back to a\ngeneric least-privilege hint for unmapped identifiers.\n\nArgs:\n    finding: Security finding with a CWE identifier string.\n\nReturns:\n    One-line remediation hint without markdown formatting.", "kind": "method", "line": 620, "name": "fix_hint_for", "signature": "def fix_hint_for(finding)"}, {"kind": "method", "line": 496, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Resolve rules: prefer YAML, fall back to built-in.", "kind": "method", "line": 500, "name": "_resolve_rules", "signature": "def _resolve_rules(self)"}, {"kind": "method", "line": 509, "name": "_meets_threshold", "signature": "def _meets_threshold(self, severity)"}, {"kind": "method", "line": 513, "name": "scan", "signature": "def scan(self, root)"}, {"kind": "method", "line": 555, "name": "_validate_path", "signature": "def _validate_path(self, path, root)"}, {"kind": "method", "line": 572, "name": "summary", "signature": "def summary(self, findings)"}]}, {"doc": "Taint propagation analysis of dangerous imports through the resolved import graph.", "id": "readmenator/_taint.py", "kind": "module", "label": "_taint.py", "language": "py", "sha256": "e5d5f3447e3207de", "symbol_count": 6, "symbols": [{"doc": "Propagation-based taint analysis over the resolved import graph.\n\nIdentifies files that import known-dangerous modules or functions\n(sources) and traces how that danger propagates through the import\ngraph to files that never directly import the dangerous module\nbut receive taint through transitive dependencies.", "kind": "class", "line": 12, "name": "TaintAnalyzer", "signature": "class TaintAnalyzer"}, {"kind": "method", "line": 73, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run taint propagation analysis on the codebase.\n\nScans all nodes for direct dangerous imports, then propagates\ntaint through the resolved import graph. Returns all discovered\ntaint paths from sources to sinks.", "kind": "method", "line": 77, "name": "analyze", "signature": "def analyze(self, nodes, edges, resolved_edges)"}, {"doc": "Find files that directly import known-dangerous modules.", "kind": "method", "line": 136, "name": "_find_direct_sources", "signature": "def _find_direct_sources(self, nodes, edges)"}, {"doc": "BFS propagation from source through the import graph.", "kind": "method", "line": 162, "name": "_propagate", "signature": "def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)"}, {"doc": "Build a forward-directed import graph from resolved edges.", "kind": "method", "line": 213, "name": "_build_forward_graph", "signature": "def _build_forward_graph(nodes, resolved_edges)"}]}, {"doc": "UML class diagram renderer (Mermaid classDiagram) and 12-language stub generator.", "id": "readmenator/_uml.py", "kind": "module", "label": "_uml.py", "language": "py", "sha256": "1c08f1d5566773e1", "symbol_count": 25, "symbols": [{"kind": "class", "line": 34, "name": "UmlGenerator", "signature": "class UmlGenerator"}, {"kind": "method", "line": 172, "name": "_get_code_generator", "signature": "def _get_code_generator(language)"}, {"kind": "method", "line": 190, "name": "_type_map_py_to_target", "signature": "def _type_map_py_to_target(target, py_type_hint)"}, {"kind": "method", "line": 233, "name": "_generate_cpp", "signature": "def _generate_cpp(class_symbols, nodes, edges)"}, {"kind": "method", "line": 259, "name": "_cpp_params", "signature": "def _cpp_params(params)"}, {"kind": "method", "line": 274, "name": "_generate_java", "signature": "def _generate_java(class_symbols, nodes, edges)"}, {"kind": "method", "line": 301, "name": "_java_params", "signature": "def _java_params(params)"}, {"kind": "method", "line": 316, "name": "_generate_csharp", "signature": "def _generate_csharp(class_symbols, nodes, edges)"}, {"kind": "method", "line": 345, "name": "_cs_params", "signature": "def _cs_params(params)"}, {"kind": "method", "line": 360, "name": "_generate_python", "signature": "def _generate_python(class_symbols, nodes, edges)"}, {"kind": "method", "line": 395, "name": "_generate_go", "signature": "def _generate_go(class_symbols, nodes, edges)"}, {"kind": "method", "line": 422, "name": "_generate_rust", "signature": "def _generate_rust(class_symbols, nodes, edges)"}, {"kind": "method", "line": 448, "name": "_generate_php", "signature": "def _generate_php(class_symbols, nodes, edges)"}, {"kind": "method", "line": 476, "name": "_generate_kotlin", "signature": "def _generate_kotlin(class_symbols, nodes, edges)"}, {"kind": "method", "line": 496, "name": "_generate_scala", "signature": "def _generate_scala(class_symbols, nodes, edges)"}, {"kind": "method", "line": 518, "name": "_generate_swift", "signature": "def _generate_swift(class_symbols, nodes, edges)"}, {"kind": "method", "line": 547, "name": "_generate_dart", "signature": "def _generate_dart(class_symbols, nodes, edges)"}, {"kind": "method", "line": 567, "name": "_generate_ruby", "signature": "def _generate_ruby(class_symbols, nodes, edges)"}, {"kind": "method", "line": 588, "name": "_safe_name", "signature": "def _safe_name(name)"}, {"kind": "method", "line": 592, "name": "_extract_params", "signature": "def _extract_params(signature)"}, {"kind": "method", "line": 36, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 39, "name": "render_mermaid_class_diagram", "signature": "def render_mermaid_class_diagram(self, nodes, edges)"}, {"kind": "method", "line": 129, "name": "generate_code", "signature": "def generate_code(self, nodes, edges, target_language)"}, {"kind": "method", "line": 153, "name": "_sanitize_id", "signature": "def _sanitize_id(raw)"}, {"kind": "method", "line": 165, "name": "_find_node", "signature": "def _find_node(nodes, node_id)"}]}, {"doc": "Cinematic codebase overview video, general purpose.  Renders a short synthwave explainer for any project analysed by readmenator, in the visual language of the miniGCC self-host video (neon HUD panels, striped sun, scrolling grid, bloom, scanlines, chromatic text, glitch transitions). Every number on screen comes from a real scan: file/symbol/import counts, detected layers, god nodes, communities, the resolved import graph, per-file hash colors and top security findings.  Zero tokens: pure PIL frame drawing piped to ffmpeg. Optional dependency: when PIL or ffmpeg is missing the caller skips with a warning instead of failing the rebuild.", "id": "readmenator/_video.py", "kind": "module", "label": "_video.py", "language": "py", "sha256": "cda664fd11996138", "symbol_count": 49, "symbols": [{"doc": "Smoothstep clamped to [0, 1].", "kind": "function", "line": 73, "name": "ease", "signature": "def ease(x)"}, {"doc": "Group thousands with commas.", "kind": "function", "line": 79, "name": "fmt_int", "signature": "def fmt_int(n)"}, {"doc": "Linear blend of two RGB colors.", "kind": "function", "line": 84, "name": "mix", "signature": "def mix(a, b, t)"}, {"doc": "RGB color plus an alpha in [0, 1] as an RGBA tuple.", "kind": "function", "line": 89, "name": "alpha", "signature": "def alpha(c, a)"}, {"doc": "Neon color derived from a digest: the file fingerprint.", "kind": "function", "line": 94, "name": "hash_color", "signature": "def hash_color(digest)"}, {"doc": "Truncate a label to a character budget without newlines.", "kind": "function", "line": 103, "name": "short_label", "signature": "def short_label(text, limit)"}, {"doc": "Main content panel fitted to the configured canvas.", "kind": "function", "line": 111, "name": "_panel", "signature": "def _panel(cfg)"}, {"doc": "Y coordinate of the lower-third narration line.", "kind": "function", "line": 116, "name": "_caption_y", "signature": "def _caption_y(cfg)"}, {"doc": "Graph panel plus telemetry side panel fitted to the canvas.", "kind": "function", "line": 121, "name": "_graph_boxes", "signature": "def _graph_boxes(cfg)"}, {"doc": "DNA grid panel plus security side panel fitted to the canvas.", "kind": "function", "line": 130, "name": "_dna_boxes", "signature": "def _dna_boxes(cfg)"}, {"doc": "Left content panel plus right detail panel fitted to the canvas.", "kind": "function", "line": 139, "name": "_split_boxes", "signature": "def _split_boxes(cfg)"}, {"doc": "Pulsing verdict badge pinned to the bottom of a panel.", "kind": "function", "line": 148, "name": "_verdict_badge", "signature": "def _verdict_badge(d, box, text, fonts, lt, dur, col)"}, {"doc": "Vertical sweep line travelling across a panel.", "kind": "function", "line": 163, "name": "_scan_cursor", "signature": "def _scan_cursor(d, box, progress, col)"}, {"doc": "Single-color tint for a source line: comments dim, code bright.", "kind": "function", "line": 172, "name": "_code_tint", "signature": "def _code_tint(line)"}, {"doc": "Deterministic phase offset for a packet travelling edge a->b.", "kind": "function", "line": 182, "name": "_packet_offset", "signature": "def _packet_offset(a, b, k)"}, {"doc": "Check that PIL and ffmpeg exist for video rendering.", "kind": "function", "line": 188, "name": "dependencies_available", "signature": "def dependencies_available()"}, {"doc": "Resolve monospace fonts through fontconfig with PIL fallback.", "kind": "function", "line": 197, "name": "resolve_fonts", "signature": "def resolve_fonts()"}, {"doc": "Precomputed synthwave background with sun and CRT mask.", "kind": "class", "line": 236, "name": "Backdrop", "signature": "class Backdrop"}, {"doc": "Import PIL Image lazily for optional-dependency support.", "kind": "method", "line": 292, "name": "_img", "signature": "def _img()"}, {"doc": "Draw the scrolling perspective grid below the horizon.", "kind": "method", "line": 299, "name": "draw_grid", "signature": "def draw_grid(img, t, strength, bd)"}, {"doc": "Paste the striped synthwave sun behind the horizon.", "kind": "method", "line": 319, "name": "draw_sun", "signature": "def draw_sun(img, a, bd, cy)"}, {"doc": "Apply bloom, scanlines, vignette and optional glitch.", "kind": "method", "line": 336, "name": "post", "signature": "def post(img, glitch, seed)"}, {"doc": "RGB split plus horizontal slice displacement.", "kind": "method", "line": 354, "name": "glitch_fx", "signature": "def glitch_fx(img, amount, seed)"}, {"doc": "Draw text with red/cyan CRT chromatic aberration.", "kind": "method", "line": 377, "name": "chroma_text", "signature": "def chroma_text(img, xy, text, font, col, spread, anchor)"}, {"doc": "Draw a translucent HUD panel with neon edge and corner brackets.", "kind": "method", "line": 388, "name": "hud_panel", "signature": "def hud_panel(d, box, title, fonts, col)"}, {"doc": "Draw the top strip with project title, act label and progress.", "kind": "method", "line": 401, "name": "draw_header", "signature": "def draw_header(img, d, gt, total, project, act_label, fonts, width)"}, {"doc": "Draw the lower-third narration line with typing effect.", "kind": "method", "line": 415, "name": "draw_caption", "signature": "def draw_caption(d, text, lt, dur, fonts, width, y)"}, {"doc": "Builds and renders the general-purpose codebase overview video.", "kind": "class", "line": 431, "name": "CinematicVideoRenderer", "signature": "class CinematicVideoRenderer"}, {"doc": "Pool worker: draw one frame and return raw RGB bytes.", "kind": "method", "line": 752, "name": "_render_frame_bytes", "signature": "def _render_frame_bytes(fi)"}, {"doc": "Draw one frame for the global render state.", "kind": "method", "line": 757, "name": "_draw_frame", "signature": "def _draw_frame(fi)"}, {"doc": "Cold open with counting project stats and language chips.", "kind": "method", "line": 785, "name": "_scene_title", "signature": "def _scene_title(img, d, lt, gt, sc)"}, {"doc": "Act interstitial card.", "kind": "method", "line": 820, "name": "_scene_card", "signature": "def _scene_card(img, d, lt, gt, sc)"}, {"doc": "Animated horizontal bars for the 5-layer model with sweep cursor.", "kind": "method", "line": 834, "name": "_scene_layers", "signature": "def _scene_layers(img, d, lt, gt, sc)"}, {"doc": "Ranked god nodes with the formula exposed plus real source preview.", "kind": "method", "line": 859, "name": "_scene_gods", "signature": "def _scene_gods(img, d, lt, gt, sc)"}, {"doc": "The true dependency tree: BFS spanning tree grown from the hub file.", "kind": "method", "line": 902, "name": "_scene_tree", "signature": "def _scene_tree(img, d, lt, gt, sc)"}, {"doc": "Community cards explaining why each group sticks together.", "kind": "method", "line": 963, "name": "_scene_communities", "signature": "def _scene_communities(img, d, lt, gt, sc)"}, {"doc": "The resolved import graph growing node by node, with live packets.", "kind": "method", "line": 1006, "name": "_scene_graph", "signature": "def _scene_graph(img, d, lt, gt, sc)"}, {"doc": "Every file as a color, scanned live, with a zoom on the hub file.", "kind": "method", "line": 1064, "name": "_scene_dna", "signature": "def _scene_dna(img, d, lt, gt, sc)"}, {"doc": "Closing summary with the measured numbers.", "kind": "method", "line": 1119, "name": "_scene_outro", "signature": "def _scene_outro(img, d, lt, gt, sc)"}, {"doc": "Find one font file for a style, else None.", "kind": "method", "line": 201, "name": "_find", "signature": "def _find(style)"}, {"doc": "Build the gradient sky, star field, sun and CRT mask.", "kind": "method", "line": 239, "name": "__init__", "signature": "def __init__(self, width, height)"}, {"doc": "Build the striped synthwave sun sprite.", "kind": "method", "line": 277, "name": "_sun", "signature": "def _sun(self, r)"}, {"doc": "Collect every number each scene draws, from real scan data.", "kind": "method", "line": 436, "name": "collect", "signature": "def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map)"}, {"doc": "Grow a true dependency spanning tree with BFS from the hub file.", "kind": "method", "line": 572, "name": "_build_dep_tree", "signature": "def _build_dep_tree(self, node_by_id, link_set, god_names)"}, {"doc": "Lay every scene on the global clock.", "kind": "method", "line": 612, "name": "build_scenes", "signature": "def build_scenes(self, data)"}, {"doc": "Compute deterministic positions for graph nodes inside a box.", "kind": "method", "line": 638, "name": "graph_positions", "signature": "def graph_positions(self, data, box)"}, {"doc": "Compute tidy tree positions for the BFS dependency tree.", "kind": "method", "line": 673, "name": "tree_positions", "signature": "def tree_positions(self, data, box)"}, {"doc": "Render one frame to raw RGB bytes without touching ffmpeg.", "kind": "method", "line": 694, "name": "render_single_frame", "signature": "def render_single_frame(self, data, frame_index)"}, {"doc": "Render all frames and encode to mp4, muxing music if configured.", "kind": "method", "line": 712, "name": "render", "signature": "def render(self, data, output_path)"}]}, {"doc": "Filesystem watcher for auto-rebuilding the knowledge base.  Monitors the project directory for file changes and triggers automatic regeneration of KNOWLEDGE_BASE.md. Uses polling with configurable interval to avoid external dependencies.", "id": "readmenator/_watcher.py", "kind": "module", "label": "_watcher.py", "language": "py", "sha256": "239589d6f7746a2a", "symbol_count": 5, "symbols": [{"doc": "Polling-based directory watcher for auto-rebuild on changes.\n\nComputes a combined hash of all tracked files (filenames + sizes)\nand triggers a callback when the hash changes. Uses polling to\navoid external dependencies like watchdog or inotify.", "kind": "class", "line": 21, "name": "DirectoryWatcher", "signature": "class DirectoryWatcher"}, {"doc": "Initialise the watcher for a project root.\n\nArgs:\n    root: Project directory to watch.\n    config: Application configuration.\n    callback: Function called when changes are detected.\n    interval_seconds: Polling interval in seconds.", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, root, config, callback, interval_seconds)"}, {"doc": "Compute a quick hash of all tracked files in the project.\n\nUses file paths and sizes (not full content) for speed.\nReturns a hex digest that changes when files are added,\nremoved, or modified.", "kind": "method", "line": 51, "name": "_compute_snapshot", "signature": "def _compute_snapshot(self)"}, {"doc": "Start watching the directory (blocking).", "kind": "method", "line": 80, "name": "start", "signature": "def start(self)"}, {"doc": "Stop watching.", "kind": "method", "line": 97, "name": "stop", "signature": "def stop(self)"}]}, {"doc": "Deterministic agent wiki generator for readmenator.  Builds a navigable, progressively disclosed wiki on top of the scanned knowledge graph. The layout mirrors the Karpathy LLM Wiki Pattern used by graphify and second-brain (index plus one page per community plus machine-readable connections), but every page is synthesised deterministically from static analysis with zero LLM calls, zero tokens, and an honest confidence trail.  Output layout::  readmenator-wiki/ ├── index.md              # entry point: overview plus all links ├── community_<id>_<slug>.md  # one synthesis page per community ├── connections.json      # typed bridges with strength and confidence ├── queries.md            # suggested questions plus answer log └── REPORT.md             # honest audit: coverage, confidence, limits", "id": "readmenator/_wiki.py", "kind": "module", "label": "_wiki.py", "language": "py", "sha256": "413693197c57ef5a", "symbol_count": 31, "symbols": [{"doc": "Return True for file-doc first lines that state no purpose.", "kind": "function", "line": 47, "name": "_is_garbage_purpose", "signature": "def _is_garbage_purpose(text)"}, {"doc": "Return a filesystem-safe slug for community labels.", "kind": "function", "line": 55, "name": "_slug", "signature": "def _slug(text)"}, {"doc": "Return community id pairs already linked, to avoid duplicate edges.", "kind": "function", "line": 62, "name": "existing_ids", "signature": "def existing_ids(connections)"}, {"doc": "Return unique display names, disambiguating duplicate labels.", "kind": "function", "line": 72, "name": "_display_names", "signature": "def _display_names(communities)"}, {"doc": "Generates the navigable agent wiki from scanned topology.", "kind": "class", "line": 86, "name": "WikiGenerator", "signature": "class WikiGenerator"}, {"doc": "Store configuration for wiki output limits and paths.", "kind": "method", "line": 89, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Write all wiki files and return the output directory path.", "kind": "method", "line": 94, "name": "generate", "signature": "def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)"}, {"doc": "Delete community pages from previous runs that are no longer generated.", "kind": "method", "line": 142, "name": "_prune_stale_pages", "signature": "def _prune_stale_pages(self, out_dir, current)"}, {"doc": "Check wiki health and return a list of issue descriptions.", "kind": "method", "line": 151, "name": "lint", "signature": "def lint(self, project_root)"}, {"doc": "Return detected communities plus an orphan fallback for leftovers.", "kind": "method", "line": 174, "name": "_resolve_communities", "signature": "def _resolve_communities(self, nodes, analysis, resolved)"}, {"doc": "Return the community containing the given node id.", "kind": "method", "line": 200, "name": "_community_of", "signature": "def _community_of(self, node_id, communities)"}, {"doc": "Derive typed bridges between communities with strength scores.", "kind": "method", "line": 209, "name": "_build_connections", "signature": "def _build_connections(self, communities, resolved, analysis, node_map, layers)"}, {"doc": "Flag community pairs sharing an unusual fraction of symbol names.", "kind": "method", "line": 274, "name": "_duplicate_links", "signature": "def _duplicate_links(communities, node_map, skip_pairs)"}, {"doc": "Infer weak links between otherwise disconnected communities.", "kind": "method", "line": 317, "name": "_shared_context_links", "signature": "def _shared_context_links(self, communities, existing, node_map, layers)"}, {"doc": "Describe shared language or layer between two communities.", "kind": "method", "line": 353, "name": "_shared_context", "signature": "def _shared_context(first, second, node_map, layers)"}, {"doc": "Serialize connections as pretty-printed JSON.", "kind": "method", "line": 386, "name": "_build_connections_json", "signature": "def _build_connections_json(self, connections)"}, {"doc": "Synthesize a one-paragraph definition for a community.", "kind": "method", "line": 390, "name": "_definition_for", "signature": "def _definition_for(self, community, node_map)"}, {"doc": "Return a markdown table row for a single file, or empty string.", "kind": "method", "line": 419, "name": "_file_row", "signature": "def _file_row(self, fid, node_map, layers)"}, {"doc": "List oversized communities grouped by directory within budget.", "kind": "method", "line": 433, "name": "_build_grouped_files", "signature": "def _build_grouped_files(self, members, node_map, layers, max_files)"}, {"doc": "Build the synthesis page for a single community.", "kind": "method", "line": 482, "name": "_build_community_page", "signature": "def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)"}, {"doc": "Generate deterministic open questions for a community.", "kind": "method", "line": 635, "name": "_questions_for", "signature": "def _questions_for(self, community, node_map, member_set, analysis_v2)"}, {"doc": "Return node ids whose on-disk size exceeds the large-file threshold.", "kind": "method", "line": 673, "name": "_large_files", "signature": "def _large_files(self, nodes, project_root)"}, {"doc": "Build the wiki entry point with overview and navigation.", "kind": "method", "line": 686, "name": "_build_index", "signature": "def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections, project_name, project_root)"}, {"doc": "Synthesize the central preoccupations paragraph.", "kind": "method", "line": 798, "name": "_overview_paragraph", "signature": "def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)"}, {"doc": "Synthesize the connective tissue paragraph.", "kind": "method", "line": 831, "name": "_connective_paragraph", "signature": "def _connective_paragraph(self, communities, connections)"}, {"doc": "Synthesize the open questions paragraph.", "kind": "method", "line": 852, "name": "_questions_paragraph", "signature": "def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)"}, {"doc": "Build the starter question log with feedback loop instructions.", "kind": "method", "line": 868, "name": "_build_queries", "signature": "def _build_queries(self, analysis)"}, {"doc": "Build the honest audit report with confidence and limits.", "kind": "method", "line": 893, "name": "_build_report", "signature": "def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name, project_root)"}, {"doc": "Estimate wiki read cost as characters divided by four.", "kind": "method", "line": 965, "name": "_estimate_tokens", "signature": "def _estimate_tokens(self, nodes, connections)"}, {"doc": "Write wiki file content with UTF-8 encoding.", "kind": "method", "line": 976, "name": "_write", "signature": "def _write(path, content)"}, {"kind": "method", "line": 360, "name": "dominant", "signature": "def dominant(ids, key)"}]}, {"doc": "Parser factory: maps file extensions to per-language LanguageParser classes.", "id": "readmenator/parsers/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "8bbef7b526b8e00a", "symbol_count": 2, "symbols": [{"kind": "function", "line": 34, "name": "_init_parser_map", "signature": "def _init_parser_map()"}, {"doc": "Factory: return a parser instance for the given file extension.", "kind": "function", "line": 70, "name": "create_parser", "signature": "def create_parser(extension, filename, config)"}]}, {"doc": "Assembly parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_assembly.py", "kind": "module", "label": "_assembly.py", "language": "py", "sha256": "8302729865f9addb", "symbol_count": 2, "symbols": [{"doc": "Parser for assembly (.asm, .s, .S).\n\nExtracts labels at the start of a line (``label:``) as function\nsymbols. This is a best-effort heuristic; local labels and\ndirectives are not always distinguishable.", "kind": "class", "line": 11, "name": "AssemblyParser", "signature": "class AssemblyParser(LanguageParser)"}, {"kind": "method", "line": 19, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "LanguageParser base class with shared docstring and signature extraction.", "id": "readmenator/parsers/_base.py", "kind": "module", "label": "_base.py", "language": "py", "sha256": "864d8a7c8f75e81b", "symbol_count": 6, "symbols": [{"doc": "Base class for all language-specific parsers.\n\nSubclasses must implement ``_extract_specifics`` to populate\n``self.symbols`` and ``self.imports``. Common utility methods\n``_extract_docstring`` and ``_extract_signature`` are provided\nfor reuse across all parsers.", "kind": "class", "line": 12, "name": "LanguageParser", "signature": "class LanguageParser"}, {"doc": "Initialise the parser with a file path and application config.\n\nArgs:\n    filename: Relative or absolute path of the source file.\n    config: Application-wide configuration settings.", "kind": "method", "line": 21, "name": "__init__", "signature": "def __init__(self, filename, config)"}, {"doc": "Parse *content* and populate symbol/import lists.\n\nSplits the source into lines, then delegates to the subclass-\nspecific ``_extract_specifics`` logic.", "kind": "method", "line": 36, "name": "parse", "signature": "def parse(self, content)"}, {"doc": "Subclass hook for language-specific symbol extraction.", "kind": "method", "line": 45, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}, {"doc": "Walk backwards from *line_num* to collect preceding comments/docstrings.\n\nSupports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``\ncomment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``\nfrom Config.", "kind": "method", "line": 49, "name": "_extract_docstring", "signature": "def _extract_docstring(self, line_num)"}, {"doc": "Extract a compact signature snippet starting at *match_start*.\n\nScans forward to the opening brace or a fallback length,\nthen truncates to 100 characters for display.", "kind": "method", "line": 91, "name": "_extract_signature", "signature": "def _extract_signature(self, content, match_start, pattern)"}]}, {"doc": "C and C++ parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_c.py", "kind": "module", "label": "_c.py", "language": "py", "sha256": "95bfbf6354399505", "symbol_count": 3, "symbols": [{"doc": "Return True when a prototype prefix carries a return type.", "kind": "function", "line": 18, "name": "_has_type_prefix", "signature": "def _has_type_prefix(prefix)"}, {"doc": "Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).\n\nExtracts includes, structs, classes, functions, and preprocessor\nmacros using regex heuristics tuned to C-family syntax.", "kind": "class", "line": 30, "name": "CParser", "signature": "class CParser(LanguageParser)"}, {"doc": "Extract C-family symbols and imports from source content.\n\nCollects includes (quoted vs system), structs, classes, enums,\nunions, typedefs, functions (definitions and prototypes), extern\ndeclarations, globals, and macros.", "kind": "method", "line": 37, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "C# parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_csharp.py", "kind": "module", "label": "_csharp.py", "language": "py", "sha256": "72953e4fdd0d211b", "symbol_count": 2, "symbols": [{"doc": "Parser for C# (.cs).\n\nExtracts ``using`` directives, class/struct/interface/record\ndeclarations, and methods with access modifiers.", "kind": "class", "line": 11, "name": "CSharpParser", "signature": "class CSharpParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Dart parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_dart.py", "kind": "module", "label": "_dart.py", "language": "py", "sha256": "344399a064b052b5", "symbol_count": 2, "symbols": [{"doc": "Parser for Dart (.dart).\n\nExtracts import statements, class declarations (with extends),\nand top-level or method function declarations by return type.", "kind": "class", "line": 11, "name": "DartParser", "signature": "class DartParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Elixir parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_elixir.py", "kind": "module", "label": "_elixir.py", "language": "py", "sha256": "d799080e08bda638", "symbol_count": 2, "symbols": [{"doc": "Parser for Elixir (.ex, .exs).\n\nExtracts ``import``/``alias``/``require``/``use`` directives,\nmodule definitions, and named function definitions.", "kind": "class", "line": 11, "name": "ElixirParser", "signature": "class ElixirParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "GDScript parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_gdscript.py", "kind": "module", "label": "_gdscript.py", "language": "py", "sha256": "00f5443c25e7d991", "symbol_count": 2, "symbols": [{"doc": "Parser for Godot GDScript (.gd).\n\nExtracts ``extends`` / ``class_name`` directives and ``func``\nmethod declarations.", "kind": "class", "line": 11, "name": "GDScriptParser", "signature": "class GDScriptParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Go parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_go.py", "kind": "module", "label": "_go.py", "language": "py", "sha256": "526dff226f3d22fe", "symbol_count": 2, "symbols": [{"doc": "Parser for Go (.go).\n\nExtracts import blocks or single import statements, exported\nfunctions (including methods), and type definitions (struct/interface).", "kind": "class", "line": 11, "name": "GoParser", "signature": "class GoParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Java parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_java.py", "kind": "module", "label": "_java.py", "language": "py", "sha256": "62ed3036088612a4", "symbol_count": 2, "symbols": [{"doc": "Parser for Java (.java).\n\nExtracts import statements, class and interface declarations,\nand methods complete with access modifiers and type signatures.", "kind": "class", "line": 11, "name": "JavaParser", "signature": "class JavaParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "JavaScript and TypeScript parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_javascript.py", "kind": "module", "label": "_javascript.py", "language": "py", "sha256": "c27e7fa4a88f8585", "symbol_count": 2, "symbols": [{"doc": "Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).\n\nExtracts ES module imports, CommonJS ``require`` calls, function\ndeclarations, arrow-function variables, and class definitions\n(including inheritance).", "kind": "class", "line": 11, "name": "JavaScriptParser", "signature": "class JavaScriptParser(LanguageParser)"}, {"kind": "method", "line": 19, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Kotlin parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_kotlin.py", "kind": "module", "label": "_kotlin.py", "language": "py", "sha256": "87189fdd0f2978a1", "symbol_count": 2, "symbols": [{"doc": "Parser for Kotlin (.kt, .kts).\n\nExtracts ``import`` statements, class/object/interface/data class\ndeclarations, and function definitions.", "kind": "class", "line": 11, "name": "KotlinParser", "signature": "class KotlinParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Lua parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_lua.py", "kind": "module", "label": "_lua.py", "language": "py", "sha256": "16320b2be180ea64", "symbol_count": 2, "symbols": [{"doc": "Parser for Lua (.lua).\n\nExtracts ``require`` imports, function declarations (named and\ntable-based), and module returns.", "kind": "class", "line": 11, "name": "LuaParser", "signature": "class LuaParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Nim parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_nim.py", "kind": "module", "label": "_nim.py", "language": "py", "sha256": "1723010d3f717307", "symbol_count": 2, "symbols": [{"doc": "Parser for Nim (.nim).\n\nExtracts ``import`` statements, ``proc`` / ``func`` / ``method``\ndeclarations, and ``type`` definitions.", "kind": "class", "line": 11, "name": "NimParser", "signature": "class NimParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "PHP parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_php.py", "kind": "module", "label": "_php.py", "language": "py", "sha256": "7249bfb61e8ac879", "symbol_count": 2, "symbols": [{"doc": "Parser for PHP (.php).\n\nExtracts ``use/require/include`` (including ``_once`` variants),\nfunction declarations, and class declarations.", "kind": "class", "line": 11, "name": "PHPParser", "signature": "class PHPParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Python parser: native ast extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_python.py", "kind": "module", "label": "_python.py", "language": "py", "sha256": "bc64944e53564e7b", "symbol_count": 2, "symbols": [{"doc": "Parser for Python (.py) using the native ``ast`` module.\n\nExtracts imports, functions (including async), and class\ndefinitions with docstrings via ``ast.get_docstring``.", "kind": "class", "line": 12, "name": "PythonParser", "signature": "class PythonParser(LanguageParser)"}, {"kind": "method", "line": 19, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Ruby parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_ruby.py", "kind": "module", "label": "_ruby.py", "language": "py", "sha256": "132a544faf508487", "symbol_count": 2, "symbols": [{"doc": "Parser for Ruby (.rb).\n\nExtracts ``require`` / ``require_relative`` imports, class and\nmodule definitions with inheritance, and method definitions.", "kind": "class", "line": 11, "name": "RubyParser", "signature": "class RubyParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Rust parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_rust.py", "kind": "module", "label": "_rust.py", "language": "py", "sha256": "7b5d8a443719c780", "symbol_count": 2, "symbols": [{"doc": "Parser for Rust (.rs).\n\nExtracts ``use`` imports, public and private functions,\nstructs, traits, and enums.", "kind": "class", "line": 11, "name": "RustParser", "signature": "class RustParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Scala parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_scala.py", "kind": "module", "label": "_scala.py", "language": "py", "sha256": "a0adb5d08d1cf0ec", "symbol_count": 2, "symbols": [{"doc": "Parser for Scala (.scala).\n\nExtracts ``import`` statements, class/object/trait declarations,\nand method definitions.", "kind": "class", "line": 11, "name": "ScalaParser", "signature": "class ScalaParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Shell parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_shell.py", "kind": "module", "label": "_shell.py", "language": "py", "sha256": "49b92556abae2fd0", "symbol_count": 2, "symbols": [{"doc": "Parser for shell scripts (.sh, .bash, .zsh).\n\nExtracts function declarations in both POSIX (``name() {``)\nand ``function`` keyword syntax.", "kind": "class", "line": 11, "name": "ShellParser", "signature": "class ShellParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Swift parser: regex extraction of symbols, signatures, docstrings, and imports.", "id": "readmenator/parsers/_swift.py", "kind": "module", "label": "_swift.py", "language": "py", "sha256": "b089c1aff3df1e54", "symbol_count": 2, "symbols": [{"doc": "Parser for Swift (.swift).\n\nExtracts ``import`` statements, class/struct/enum/protocol\ndeclarations with inheritance, and function definitions.", "kind": "class", "line": 11, "name": "SwiftParser", "signature": "class SwiftParser(LanguageParser)"}, {"kind": "method", "line": 18, "name": "_extract_specifics", "signature": "def _extract_specifics(self, content)"}]}, {"doc": "Launcher shim that runs the readmenator CLI from a source checkout.", "id": "readmenator.py", "kind": "module", "label": "readmenator.py", "language": "py", "sha256": "beabccf3e6d231db", "symbol_count": 0, "symbols": []}, {"id": "readmenator_orchestrator.py", "kind": "module", "label": "readmenator_orchestrator.py", "language": "py", "sha256": "b231c08688e2e407", "symbol_count": 34, "symbols": [{"kind": "class", "line": 21, "name": "Config", "signature": "class Config"}, {"kind": "method", "line": 50, "name": "_validate_repo_name", "signature": "def _validate_repo_name(name)"}, {"kind": "method", "line": 56, "name": "_validate_branch_name", "signature": "def _validate_branch_name(name)"}, {"kind": "method", "line": 62, "name": "_safe_env", "signature": "def _safe_env()"}, {"kind": "class", "line": 77, "name": "GitHubClient", "signature": "class GitHubClient"}, {"kind": "class", "line": 191, "name": "RepositoryProcessor", "signature": "class RepositoryProcessor"}, {"kind": "class", "line": 341, "name": "Orchestrator", "signature": "class Orchestrator"}, {"kind": "class", "line": 396, "name": "TestOrchestrator", "signature": "class TestOrchestrator(TestCase)"}, {"kind": "method", "line": 438, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 455, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 78, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 83, "name": "_resolve_user", "signature": "def _resolve_user(self)"}, {"kind": "method", "line": 104, "name": "_setup_git_auth", "signature": "def _setup_git_auth(self)"}, {"kind": "method", "line": 118, "name": "list_repos", "signature": "def list_repos(self)"}, {"kind": "method", "line": 130, "name": "close_existing_prs", "signature": "def close_existing_prs(self, repo)"}, {"kind": "method", "line": 158, "name": "delete_remote_branch", "signature": "def delete_remote_branch(self, repo)"}, {"kind": "method", "line": 170, "name": "create_pr", "signature": "def create_pr(self, repo, default_branch, timestamp)"}, {"kind": "method", "line": 192, "name": "__init__", "signature": "def __init__(self, config, github_client)"}, {"kind": "method", "line": 196, "name": "process", "signature": "def process(self, repo)"}, {"kind": "method", "line": 225, "name": "_get_default_branch", "signature": "def _get_default_branch(self, repo)"}, {"kind": "method", "line": 241, "name": "_clone_repository", "signature": "def _clone_repository(self, repo)"}, {"kind": "method", "line": 257, "name": "_run_readmenator", "signature": "def _run_readmenator(self, repo_dir)"}, {"kind": "method", "line": 277, "name": "_copy_to_docs_dir", "signature": "def _copy_to_docs_dir(self, repo_dir, generated_file)"}, {"kind": "method", "line": 290, "name": "_commit_and_push", "signature": "def _commit_and_push(self, repo_dir, repo)"}, {"kind": "method", "line": 336, "name": "_cleanup_temp_dir", "signature": "def _cleanup_temp_dir(temp_dir)"}, {"kind": "method", "line": 342, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 347, "name": "run", "signature": "def run(self, dry_run, only_repo)"}, {"kind": "method", "line": 397, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 401, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 404, "name": "test_config_immutability", "signature": "def test_config_immutability(self)"}, {"kind": "method", "line": 408, "name": "test_config_defaults", "signature": "def test_config_defaults(self)"}, {"kind": "method", "line": 415, "name": "test_skip_repos_logic", "signature": "def test_skip_repos_logic(self)"}, {"kind": "method", "line": 419, "name": "test_repo_name_validation", "signature": "def test_repo_name_validation(self)"}, {"kind": "method", "line": 429, "name": "test_branch_name_validation", "signature": "def test_branch_name_validation(self)"}]}, {"id": "tests/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "f813c53b4d1cc74f", "symbol_count": 0, "symbols": []}, {"doc": "Contract tests for agent-facing output quality: budgets, purposes, freshness, noise.", "id": "tests/test_agent_friendliness.py", "kind": "module", "label": "test_agent_friendliness.py", "language": "py", "sha256": "b1fd187e1f2c3393", "symbol_count": 43, "symbols": [{"doc": "Build a Python file node for tests.", "kind": "function", "line": 21, "name": "_node", "signature": "def _node(node_id, doc, symbols)"}, {"doc": "Build an extracted edge for tests.", "kind": "function", "line": 29, "name": "_edge", "signature": "def _edge(source, target, relation)"}, {"doc": "Build a project large enough to force pagination of every document.", "kind": "function", "line": 34, "name": "_big_project", "signature": "def _big_project(files, symbols_per_file)"}, {"doc": "Every generated document respects the line cap, with nothing lost.", "kind": "class", "line": 55, "name": "TestAgentOutputBudget", "signature": "class TestAgentOutputBudget(TestCase)"}, {"doc": "Documents carry signal, not repetition.", "kind": "class", "line": 110, "name": "TestAgentOutputSignal", "signature": "class TestAgentOutputSignal(TestCase)"}, {"doc": "File purposes are one clean sentence with a symbol fallback.", "kind": "class", "line": 176, "name": "TestPurposeExtraction", "signature": "class TestPurposeExtraction(TestCase)"}, {"doc": "MANIFEST lets an agent decide staleness without reading anything else.", "kind": "class", "line": 199, "name": "TestManifestFreshness", "signature": "class TestManifestFreshness(TestCase)"}, {"doc": "Generated artifacts and naive heuristics never pollute the graph.", "kind": "class", "line": 244, "name": "TestNoiseReduction", "signature": "class TestNoiseReduction(TestCase)"}, {"doc": "The published site exposes an llms.txt entry point for agents.", "kind": "class", "line": 281, "name": "TestLlmsTxt", "signature": "class TestLlmsTxt(TestCase)"}, {"doc": "A shared hub imported by every file must not merge unrelated clusters.", "kind": "class", "line": 308, "name": "TestCommunityHubDamping", "signature": "class TestCommunityHubDamping(TestCase)"}, {"doc": "Docs freshness is verifiable from content, independent of commit timing.", "kind": "class", "line": 329, "name": "TestSourceFreshness", "signature": "class TestSourceFreshness(TestCase)"}, {"doc": "Tiny groups fold into neighbors and shared-directory labels stay distinct.", "kind": "class", "line": 363, "name": "TestCommunityShaping", "signature": "class TestCommunityShaping(TestCase)"}, {"doc": "The static site never keeps copies of docs that were renamed or removed.", "kind": "class", "line": 394, "name": "TestSiteDocsPruning", "signature": "class TestSiteDocsPruning(TestCase)"}, {"kind": "method", "line": 58, "name": "test_agent_output_pages_respect_line_cap_on_large_projects", "signature": "def test_agent_output_pages_respect_line_cap_on_large_projects(self)"}, {"kind": "method", "line": 71, "name": "test_agent_output_pagination_keeps_every_symbol_greppable", "signature": "def test_agent_output_pagination_keeps_every_symbol_greppable(self)"}, {"kind": "method", "line": 84, "name": "test_agent_output_pages_repeat_table_header_and_link_next", "signature": "def test_agent_output_pages_repeat_table_header_and_link_next(self)"}, {"kind": "method", "line": 96, "name": "test_agent_output_prunes_stale_pages", "signature": "def test_agent_output_prunes_stale_pages(self)"}, {"kind": "method", "line": 113, "name": "test_api_states_dependencies_once_per_file", "signature": "def test_api_states_dependencies_once_per_file(self)"}, {"kind": "method", "line": 122, "name": "test_api_skips_private_helpers_and_test_layer", "signature": "def test_api_skips_private_helpers_and_test_layer(self)"}, {"kind": "method", "line": 136, "name": "test_api_qualifies_methods_with_owner_class", "signature": "def test_api_qualifies_methods_with_owner_class(self)"}, {"kind": "method", "line": 144, "name": "test_architecture_external_excludes_internally_resolved_imports", "signature": "def test_architecture_external_excludes_internally_resolved_imports(self)"}, {"kind": "method", "line": 153, "name": "test_index_reports_used_by_count_and_escapes_pipes", "signature": "def test_index_reports_used_by_count_and_escapes_pipes(self)"}, {"kind": "method", "line": 161, "name": "test_gotchas_exclude_test_layer_and_report_blast_radius", "signature": "def test_gotchas_exclude_test_layer_and_report_blast_radius(self)"}, {"kind": "method", "line": 179, "name": "test_purpose_takes_first_sentence", "signature": "def test_purpose_takes_first_sentence(self)"}, {"kind": "method", "line": 182, "name": "test_purpose_skips_banners_and_spdx", "signature": "def test_purpose_skips_banners_and_spdx(self)"}, {"kind": "method", "line": 185, "name": "test_purpose_falls_back_to_primary_public_symbol", "signature": "def test_purpose_falls_back_to_primary_public_symbol(self)"}, {"kind": "method", "line": 192, "name": "test_purpose_truncates_on_word_boundary", "signature": "def test_purpose_truncates_on_word_boundary(self)"}, {"doc": "Create a minimal git directory layout pointing at a fixed commit.", "kind": "method", "line": 202, "name": "_git_repo", "signature": "def _git_repo(self, root, packed)"}, {"kind": "method", "line": 214, "name": "test_gitmeta_reads_loose_and_packed_refs", "signature": "def test_gitmeta_reads_loose_and_packed_refs(self)"}, {"kind": "method", "line": 220, "name": "test_gitmeta_outside_repository_is_empty", "signature": "def test_gitmeta_outside_repository_is_empty(self)"}, {"kind": "method", "line": 224, "name": "test_manifest_has_commit_relative_root_and_inventory", "signature": "def test_manifest_has_commit_relative_root_and_inventory(self)"}, {"kind": "method", "line": 247, "name": "test_scanner_skips_own_generated_outputs", "signature": "def test_scanner_skips_own_generated_outputs(self)"}, {"kind": "method", "line": 260, "name": "test_resolver_prefers_root_package_over_launcher_shim", "signature": "def test_resolver_prefers_root_package_over_launcher_shim(self)"}, {"kind": "method", "line": 264, "name": "test_layers_match_whole_words_not_substrings", "signature": "def test_layers_match_whole_words_not_substrings(self)"}, {"kind": "method", "line": 272, "name": "test_layers_test_framework_import_needs_test_path", "signature": "def test_layers_test_framework_import_needs_test_path(self)"}, {"kind": "method", "line": 284, "name": "test_llms_txt_lists_wiki_before_agent_docs", "signature": "def test_llms_txt_lists_wiki_before_agent_docs(self)"}, {"kind": "method", "line": 296, "name": "test_publish_writes_llms_txt", "signature": "def test_publish_writes_llms_txt(self)"}, {"kind": "method", "line": 311, "name": "test_communities_survive_a_shared_hub", "signature": "def test_communities_survive_a_shared_hub(self)"}, {"kind": "method", "line": 332, "name": "test_fingerprint_changes_with_content_not_with_order", "signature": "def test_fingerprint_changes_with_content_not_with_order(self)"}, {"kind": "method", "line": 343, "name": "test_check_freshness_detects_source_edits", "signature": "def test_check_freshness_detects_source_edits(self)"}, {"kind": "method", "line": 366, "name": "test_small_community_merges_into_best_connected_neighbor", "signature": "def test_small_community_merges_into_best_connected_neighbor(self)"}, {"kind": "method", "line": 380, "name": "test_shared_directory_labels_use_core_file", "signature": "def test_shared_directory_labels_use_core_file(self)"}, {"kind": "method", "line": 397, "name": "test_publish_assets_prunes_stale_markdown", "signature": "def test_publish_assets_prunes_stale_markdown(self)"}]}, {"doc": "Contract tests for AI agent file injection.  SDD + TDD + BDD: Each test validates a specific behavioral contract of the AgentInjector for injecting/deleting knowledge base references into AI agent instruction files.", "id": "tests/test_agent_injector.py", "kind": "module", "label": "test_agent_injector.py", "language": "py", "sha256": "aa95990d0f7c19ca", "symbol_count": 38, "symbols": [{"doc": "BDD: AgentInjector injection contract.", "kind": "class", "line": 19, "name": "TestAgentInjectorInjectBehavior", "signature": "class TestAgentInjectorInjectBehavior(TestCase)"}, {"doc": "BDD: AgentInjector removal contract.", "kind": "class", "line": 168, "name": "TestAgentInjectorRemoveBehavior", "signature": "class TestAgentInjectorRemoveBehavior(TestCase)"}, {"doc": "BDD: AgentInjector file detection contract.", "kind": "class", "line": 211, "name": "TestAgentInjectorFindFiles", "signature": "class TestAgentInjectorFindFiles(TestCase)"}, {"doc": "BDD: AgentInjector edge case contract.", "kind": "class", "line": 248, "name": "TestAgentInjectorEdgeCases", "signature": "class TestAgentInjectorEdgeCases(TestCase)"}, {"kind": "method", "line": 22, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 27, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 30, "name": "test_inject_into_agents_md_adds_kb_link", "signature": "def test_inject_into_agents_md_adds_kb_link(self)"}, {"kind": "method", "line": 39, "name": "test_inject_into_claude_md_adds_kb_link", "signature": "def test_inject_into_claude_md_adds_kb_link(self)"}, {"kind": "method", "line": 49, "name": "test_inject_into_cursorrules_adds_kb_link", "signature": "def test_inject_into_cursorrules_adds_kb_link(self)"}, {"kind": "method", "line": 57, "name": "test_inject_into_github_copilot_instructions", "signature": "def test_inject_into_github_copilot_instructions(self)"}, {"kind": "method", "line": 67, "name": "test_inject_replaces_old_injection_without_regen_command", "signature": "def test_inject_replaces_old_injection_without_regen_command(self)"}, {"kind": "method", "line": 82, "name": "test_inject_skips_when_already_up_to_date", "signature": "def test_inject_skips_when_already_up_to_date(self)"}, {"kind": "method", "line": 96, "name": "test_inject_into_cursor_rules_mdc_glob", "signature": "def test_inject_into_cursor_rules_mdc_glob(self)"}, {"kind": "method", "line": 106, "name": "test_inject_is_idempotent_does_not_duplicate", "signature": "def test_inject_is_idempotent_does_not_duplicate(self)"}, {"kind": "method", "line": 117, "name": "test_inject_no_agent_files_returns_zero", "signature": "def test_inject_no_agent_files_returns_zero(self)"}, {"kind": "method", "line": 121, "name": "test_inject_preserves_existing_content", "signature": "def test_inject_preserves_existing_content(self)"}, {"kind": "method", "line": 129, "name": "test_inject_multiple_agent_files", "signature": "def test_inject_multiple_agent_files(self)"}, {"kind": "method", "line": 136, "name": "test_inject_plain_text_format_for_yaml", "signature": "def test_inject_plain_text_format_for_yaml(self)"}, {"kind": "method", "line": 145, "name": "test_custom_kb_filename_works", "signature": "def test_custom_kb_filename_works(self)"}, {"kind": "method", "line": 153, "name": "test_injection_includes_regeneration_command", "signature": "def test_injection_includes_regeneration_command(self)"}, {"kind": "method", "line": 160, "name": "test_inject_does_not_execute_commands", "signature": "def test_inject_does_not_execute_commands(self)"}, {"kind": "method", "line": 171, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 176, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 179, "name": "test_remove_strips_injected_section", "signature": "def test_remove_strips_injected_section(self)"}, {"kind": "method", "line": 190, "name": "test_remove_without_injection_returns_zero", "signature": "def test_remove_without_injection_returns_zero(self)"}, {"kind": "method", "line": 196, "name": "test_remove_no_files_returns_zero", "signature": "def test_remove_no_files_returns_zero(self)"}, {"kind": "method", "line": 200, "name": "test_remove_preserves_original_content", "signature": "def test_remove_preserves_original_content(self)"}, {"kind": "method", "line": 214, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 218, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 221, "name": "test_finds_agents_md", "signature": "def test_finds_agents_md(self)"}, {"kind": "method", "line": 227, "name": "test_finds_all_listed_files", "signature": "def test_finds_all_listed_files(self)"}, {"kind": "method", "line": 234, "name": "test_finds_cursor_rules_glob", "signature": "def test_finds_cursor_rules_glob(self)"}, {"kind": "method", "line": 243, "name": "test_returns_empty_when_no_files", "signature": "def test_returns_empty_when_no_files(self)"}, {"kind": "method", "line": 251, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 256, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 259, "name": "test_inject_into_empty_file", "signature": "def test_inject_into_empty_file(self)"}, {"kind": "method", "line": 267, "name": "test_inject_respects_custom_agent_files_list", "signature": "def test_inject_respects_custom_agent_files_list(self)"}, {"kind": "method", "line": 275, "name": "test_inject_does_not_touch_unlisted_files", "signature": "def test_inject_does_not_touch_unlisted_files(self)"}]}, {"id": "tests/test_agent_output.py", "kind": "module", "label": "test_agent_output.py", "language": "py", "sha256": "02505a50e24794e4", "symbol_count": 45, "symbols": [{"kind": "function", "line": 19, "name": "_make_node", "signature": "def _make_node(node_id, symbols, doc, language)"}, {"kind": "function", "line": 30, "name": "_make_edge", "signature": "def _make_edge(source, target, relation)"}, {"kind": "function", "line": 34, "name": "_make_finding", "signature": "def _make_finding(file_path, line, severity, rule_id, description, snippet, cwe)"}, {"kind": "class", "line": 49, "name": "TestAgentOutputContract", "signature": "class TestAgentOutputContract(TestCase)"}, {"kind": "class", "line": 63, "name": "TestSubsystemInference", "signature": "class TestSubsystemInference(TestCase)"}, {"kind": "class", "line": 117, "name": "TestIndexGeneration", "signature": "class TestIndexGeneration(TestCase)"}, {"kind": "class", "line": 143, "name": "TestSecurityGeneration", "signature": "class TestSecurityGeneration(TestCase)"}, {"kind": "class", "line": 190, "name": "TestGotchasGeneration", "signature": "class TestGotchasGeneration(TestCase)"}, {"kind": "class", "line": 246, "name": "TestArchitectureGeneration", "signature": "class TestArchitectureGeneration(TestCase)"}, {"kind": "class", "line": 268, "name": "TestApiGeneration", "signature": "class TestApiGeneration(TestCase)"}, {"kind": "class", "line": 294, "name": "TestSubsystemFileGeneration", "signature": "class TestSubsystemFileGeneration(TestCase)"}, {"kind": "class", "line": 316, "name": "TestRecipesGeneration", "signature": "class TestRecipesGeneration(TestCase)"}, {"kind": "class", "line": 362, "name": "TestFullGenerate", "signature": "class TestFullGenerate(TestCase)"}, {"kind": "class", "line": 434, "name": "TestInjectionOutdatedDetection", "signature": "class TestInjectionOutdatedDetection(TestCase)"}, {"kind": "method", "line": 50, "name": "test_config_defaults", "signature": "def test_config_defaults(self)"}, {"kind": "method", "line": 56, "name": "test_config_immutable", "signature": "def test_config_immutable(self)"}, {"kind": "method", "line": 64, "name": "test_inferred_from_directories", "signature": "def test_inferred_from_directories(self)"}, {"kind": "method", "line": 80, "name": "test_flat_project_single_file", "signature": "def test_flat_project_single_file(self)"}, {"kind": "method", "line": 91, "name": "test_min_threshold_respected", "signature": "def test_min_threshold_respected(self)"}, {"kind": "method", "line": 103, "name": "test_misc_catches_unassigned", "signature": "def test_misc_catches_unassigned(self)"}, {"kind": "method", "line": 118, "name": "test_index_lists_all_files", "signature": "def test_index_lists_all_files(self)"}, {"kind": "method", "line": 133, "name": "test_index_table_format", "signature": "def test_index_table_format(self)"}, {"kind": "method", "line": 144, "name": "test_empty_findings", "signature": "def test_empty_findings(self)"}, {"kind": "method", "line": 150, "name": "test_findings_grouped_by_severity", "signature": "def test_findings_grouped_by_severity(self)"}, {"kind": "method", "line": 166, "name": "test_findings_include_fix_hint_and_scope", "signature": "def test_findings_include_fix_hint_and_scope(self)"}, {"kind": "method", "line": 181, "name": "test_no_json_wrapping", "signature": "def test_no_json_wrapping(self)"}, {"kind": "method", "line": 191, "name": "test_god_nodes_section", "signature": "def test_god_nodes_section(self)"}, {"kind": "method", "line": 207, "name": "test_cycles_section", "signature": "def test_cycles_section(self)"}, {"kind": "method", "line": 224, "name": "test_empty_gotchas", "signature": "def test_empty_gotchas(self)"}, {"kind": "method", "line": 230, "name": "test_cycle_loop_closed", "signature": "def test_cycle_loop_closed(self)"}, {"kind": "method", "line": 247, "name": "test_internal_dependencies", "signature": "def test_internal_dependencies(self)"}, {"kind": "method", "line": 258, "name": "test_external_imports", "signature": "def test_external_imports(self)"}, {"kind": "method", "line": 269, "name": "test_functions_listed", "signature": "def test_functions_listed(self)"}, {"kind": "method", "line": 283, "name": "test_no_json_in_api", "signature": "def test_no_json_in_api(self)"}, {"kind": "method", "line": 295, "name": "test_subsystem_files_written", "signature": "def test_subsystem_files_written(self)"}, {"kind": "method", "line": 317, "name": "test_recipes_directory", "signature": "def test_recipes_directory(self)"}, {"kind": "method", "line": 330, "name": "test_recipes_grounded_in_actual_findings", "signature": "def test_recipes_grounded_in_actual_findings(self)"}, {"kind": "method", "line": 363, "name": "test_generate_creates_all_files", "signature": "def test_generate_creates_all_files(self)"}, {"kind": "method", "line": 394, "name": "test_all_files_under_500_lines", "signature": "def test_all_files_under_500_lines(self)"}, {"kind": "method", "line": 409, "name": "test_no_json_in_any_output", "signature": "def test_no_json_in_any_output(self)"}, {"kind": "method", "line": 421, "name": "test_manifest_workflow_orients_with_ls", "signature": "def test_manifest_workflow_orients_with_ls(self)"}, {"kind": "method", "line": 435, "name": "test_agent_injector_detects_outdated", "signature": "def test_agent_injector_detects_outdated(self)"}, {"kind": "method", "line": 457, "name": "test_agent_injector_skips_identical", "signature": "def test_agent_injector_skips_identical(self)"}, {"kind": "method", "line": 473, "name": "test_readme_injector_detects_outdated", "signature": "def test_readme_injector_detects_outdated(self)"}, {"kind": "method", "line": 495, "name": "test_readme_injector_skips_identical", "signature": "def test_readme_injector_skips_identical(self)"}]}, {"doc": "Contract tests for the GraphAnalyzer.  Validates community detection, god node computation, surprising connection discovery, and suggested question generation.", "id": "tests/test_analyzer.py", "kind": "module", "label": "test_analyzer.py", "language": "py", "sha256": "0176c63295817db0", "symbol_count": 14, "symbols": [{"doc": "Contract: GraphAnalyzer provides graph intelligence.", "kind": "class", "line": 16, "name": "TestGraphAnalyzerContract", "signature": "class TestGraphAnalyzerContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 26, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt, rel)"}, {"kind": "method", "line": 29, "name": "test_analyze_empty_graph_returns_empty_result", "signature": "def test_analyze_empty_graph_returns_empty_result(self)"}, {"kind": "method", "line": 34, "name": "test_analyze_detects_communities_for_connected_graph", "signature": "def test_analyze_detects_communities_for_connected_graph(self)"}, {"kind": "method", "line": 48, "name": "test_analyze_computes_god_nodes", "signature": "def test_analyze_computes_god_nodes(self)"}, {"kind": "method", "line": 64, "name": "test_analyze_finds_surprising_connections", "signature": "def test_analyze_finds_surprising_connections(self)"}, {"kind": "method", "line": 81, "name": "test_analyze_generates_questions", "signature": "def test_analyze_generates_questions(self)"}, {"kind": "method", "line": 92, "name": "test_community_cohesion_is_between_zero_and_one", "signature": "def test_community_cohesion_is_between_zero_and_one(self)"}, {"kind": "method", "line": 107, "name": "test_isolated_nodes_do_not_form_communities", "signature": "def test_isolated_nodes_do_not_form_communities(self)"}, {"kind": "method", "line": 116, "name": "test_analyze_with_resolved_edges_counts_them", "signature": "def test_analyze_with_resolved_edges_counts_them(self)"}, {"kind": "method", "line": 130, "name": "test_analyze_is_repeatable", "signature": "def test_analyze_is_repeatable(self)"}, {"kind": "method", "line": 141, "name": "test_dominant_directory_prefers_specific_on_tie", "signature": "def test_dominant_directory_prefers_specific_on_tie(self)"}]}, {"doc": "Contract tests for the FileCache.  Validates SHA256 hashing, cache persistence, change detection, and stale entry pruning.", "id": "tests/test_cache.py", "kind": "module", "label": "test_cache.py", "language": "py", "sha256": "122bbfc37460eb38", "symbol_count": 22, "symbols": [{"doc": "Contract: FileCache provides SHA256-based incremental scan support.", "kind": "class", "line": 18, "name": "TestFileCacheContract", "signature": "class TestFileCacheContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 26, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 30, "name": "_write", "signature": "def _write(self, rel_path, content)"}, {"kind": "method", "line": 36, "name": "test_compute_hash_returns_hex_string", "signature": "def test_compute_hash_returns_hex_string(self)"}, {"kind": "method", "line": 42, "name": "test_different_content_produces_different_hash", "signature": "def test_different_content_produces_different_hash(self)"}, {"kind": "method", "line": 49, "name": "test_same_content_produces_same_hash", "signature": "def test_same_content_produces_same_hash(self)"}, {"kind": "method", "line": 56, "name": "test_load_returns_empty_dict_when_no_cache", "signature": "def test_load_returns_empty_dict_when_no_cache(self)"}, {"kind": "method", "line": 60, "name": "test_save_and_load_roundtrip", "signature": "def test_save_and_load_roundtrip(self)"}, {"kind": "method", "line": 66, "name": "test_find_changed_detects_new_files", "signature": "def test_find_changed_detects_new_files(self)"}, {"kind": "method", "line": 71, "name": "test_find_changed_detects_modified_files", "signature": "def test_find_changed_detects_modified_files(self)"}, {"kind": "method", "line": 78, "name": "test_find_changed_skips_unchanged_files", "signature": "def test_find_changed_skips_unchanged_files(self)"}, {"kind": "method", "line": 85, "name": "test_prune_deleted_removes_ghost_entries", "signature": "def test_prune_deleted_removes_ghost_entries(self)"}, {"kind": "method", "line": 92, "name": "test_compute_hashes_batch", "signature": "def test_compute_hashes_batch(self)"}, {"kind": "method", "line": 100, "name": "test_nonexistent_file_returns_empty_hash", "signature": "def test_nonexistent_file_returns_empty_hash(self)"}, {"kind": "method", "line": 109, "name": "test_save_and_load_analysis_roundtrip", "signature": "def test_save_and_load_analysis_roundtrip(self)"}, {"kind": "method", "line": 116, "name": "test_load_missing_analysis_key_returns_none", "signature": "def test_load_missing_analysis_key_returns_none(self)"}, {"kind": "method", "line": 120, "name": "test_clear_analysis_specific_key", "signature": "def test_clear_analysis_specific_key(self)"}, {"kind": "method", "line": 127, "name": "test_clear_analysis_all_keys", "signature": "def test_clear_analysis_all_keys(self)"}, {"kind": "method", "line": 134, "name": "test_has_changed_since_last_analysis_returns_true_on_first_run", "signature": "def test_has_changed_since_last_analysis_returns_true_on_first_run(self)"}, {"kind": "method", "line": 139, "name": "test_has_changed_since_last_analysis_returns_false_when_no_changes", "signature": "def test_has_changed_since_last_analysis_returns_false_when_no_changes(self)"}, {"kind": "method", "line": 147, "name": "test_has_changed_since_last_analysis_returns_true_when_file_changed", "signature": "def test_has_changed_since_last_analysis_returns_true_when_file_changed(self)"}]}, {"id": "tests/test_config.py", "kind": "module", "label": "test_config.py", "language": "py", "sha256": "0123e0442447e271", "symbol_count": 6, "symbols": [{"kind": "class", "line": 7, "name": "TestConfigContract", "signature": "class TestConfigContract(TestCase)"}, {"kind": "method", "line": 8, "name": "test_config_is_immutable", "signature": "def test_config_is_immutable(self)"}, {"kind": "method", "line": 13, "name": "test_config_defaults_are_sane", "signature": "def test_config_defaults_are_sane(self)"}, {"kind": "method", "line": 24, "name": "test_ignore_dirs_are_comprehensive", "signature": "def test_ignore_dirs_are_comprehensive(self)"}, {"kind": "method", "line": 30, "name": "test_plural_map_covers_all_symbol_types", "signature": "def test_plural_map_covers_all_symbol_types(self)"}, {"kind": "method", "line": 41, "name": "test_supported_extensions_no_duplicates", "signature": "def test_supported_extensions_no_duplicates(self)"}]}, {"id": "tests/test_cpg.py", "kind": "module", "label": "test_cpg.py", "language": "py", "sha256": "f71374c5b5964fc8", "symbol_count": 11, "symbols": [{"doc": "Contract: CodePropertyGraph generates valid JSON-LD CPG output.", "kind": "class", "line": 11, "name": "TestCodePropertyGraphContract", "signature": "class TestCodePropertyGraphContract(TestCase)"}, {"kind": "method", "line": 14, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 18, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 21, "name": "_make_sym", "signature": "def _make_sym(self, name, kind, line)"}, {"kind": "method", "line": 24, "name": "test_generate_returns_valid_json", "signature": "def test_generate_returns_valid_json(self)"}, {"kind": "method", "line": 33, "name": "test_generate_includes_node_data", "signature": "def test_generate_includes_node_data(self)"}, {"kind": "method", "line": 49, "name": "test_generate_includes_edges", "signature": "def test_generate_includes_edges(self)"}, {"kind": "method", "line": 61, "name": "test_generate_includes_metadata", "signature": "def test_generate_includes_metadata(self)"}, {"kind": "method", "line": 71, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 89, "name": "test_sha256_hash_included", "signature": "def test_sha256_hash_included(self)"}, {"kind": "method", "line": 96, "name": "test_empty_graph_returns_valid_json", "signature": "def test_empty_graph_returns_valid_json(self)"}]}, {"doc": "Contract tests for the CursorRulesGenerator.  Validates base rule generation, layer constraint extraction, analysis constraint extraction, and violation rule formatting.", "id": "tests/test_cursorrules.py", "kind": "module", "label": "test_cursorrules.py", "language": "py", "sha256": "cc1c4a1ca3487d28", "symbol_count": 12, "symbols": [{"doc": "Contract: CursorRulesGenerator produces deterministic rulesets.", "kind": "class", "line": 18, "name": "TestCursorRulesGeneratorContract", "signature": "class TestCursorRulesGeneratorContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 25, "name": "test_generate_returns_string", "signature": "def test_generate_returns_string(self)"}, {"kind": "method", "line": 29, "name": "test_generate_contains_header", "signature": "def test_generate_contains_header(self)"}, {"kind": "method", "line": 33, "name": "test_generate_contains_base_rules", "signature": "def test_generate_contains_base_rules(self)"}, {"kind": "method", "line": 38, "name": "test_generate_includes_layer_constraints", "signature": "def test_generate_includes_layer_constraints(self)"}, {"kind": "method", "line": 49, "name": "test_generate_includes_god_nodes", "signature": "def test_generate_includes_god_nodes(self)"}, {"kind": "method", "line": 62, "name": "test_generate_includes_communities", "signature": "def test_generate_includes_communities(self)"}, {"kind": "method", "line": 82, "name": "test_generate_includes_violations", "signature": "def test_generate_includes_violations(self)"}, {"kind": "method", "line": 95, "name": "test_generate_limits_violations_to_ten", "signature": "def test_generate_limits_violations_to_ten(self)"}, {"kind": "method", "line": 103, "name": "test_generate_writes_file_when_project_root", "signature": "def test_generate_writes_file_when_project_root(self)"}, {"kind": "method", "line": 111, "name": "test_generate_idempotent", "signature": "def test_generate_idempotent(self)"}]}, {"id": "tests/test_dataflow.py", "kind": "module", "label": "test_dataflow.py", "language": "py", "sha256": "d62ea2d04f4a9db7", "symbol_count": 47, "symbols": [{"kind": "function", "line": 8, "name": "_node", "signature": "def _node(node_id, funcs)"}, {"kind": "function", "line": 17, "name": "_analyze", "signature": "def _analyze(body)"}, {"kind": "class", "line": 25, "name": "TestDataflowContract", "signature": "class TestDataflowContract(TestCase)"}, {"kind": "method", "line": 26, "name": "test_config_defaults", "signature": "def test_config_defaults(self)"}, {"kind": "method", "line": 31, "name": "test_config_immutable", "signature": "def test_config_immutable(self)"}, {"kind": "method", "line": 37, "name": "test_uninit_use_detected", "signature": "def test_uninit_use_detected(self)"}, {"kind": "method", "line": 46, "name": "test_initialized_use_clean", "signature": "def test_initialized_use_clean(self)"}, {"kind": "method", "line": 50, "name": "test_params_count_as_initialized", "signature": "def test_params_count_as_initialized(self)"}, {"kind": "method", "line": 58, "name": "test_scanf_addr_counts_as_init", "signature": "def test_scanf_addr_counts_as_init(self)"}, {"kind": "method", "line": 62, "name": "test_dead_store_detected", "signature": "def test_dead_store_detected(self)"}, {"kind": "method", "line": 67, "name": "test_read_store_clean", "signature": "def test_read_store_clean(self)"}, {"kind": "method", "line": 71, "name": "test_unchecked_alloc_detected", "signature": "def test_unchecked_alloc_detected(self)"}, {"kind": "method", "line": 78, "name": "test_checked_alloc_clean", "signature": "def test_checked_alloc_clean(self)"}, {"kind": "method", "line": 84, "name": "test_disabled_returns_empty", "signature": "def test_disabled_returns_empty(self)"}, {"kind": "method", "line": 91, "name": "test_missing_content_skipped", "signature": "def test_missing_content_skipped(self)"}, {"kind": "method", "line": 96, "name": "test_issue_cap_respected", "signature": "def test_issue_cap_respected(self)"}, {"kind": "method", "line": 105, "name": "test_plain_assignment_is_not_a_declaration", "signature": "def test_plain_assignment_is_not_a_declaration(self)"}, {"kind": "method", "line": 110, "name": "test_subscript_store_counts_as_init", "signature": "def test_subscript_store_counts_as_init(self)"}, {"kind": "method", "line": 116, "name": "test_asm_output_counts_as_init", "signature": "def test_asm_output_counts_as_init(self)"}, {"kind": "method", "line": 123, "name": "test_fd_lt_zero_counts_as_checked", "signature": "def test_fd_lt_zero_counts_as_checked(self)"}, {"kind": "method", "line": 129, "name": "test_map_failed_counts_as_checked", "signature": "def test_map_failed_counts_as_checked(self)"}, {"kind": "method", "line": 136, "name": "test_member_null_check_counts", "signature": "def test_member_null_check_counts(self)"}, {"kind": "method", "line": 144, "name": "test_loop_carried_var_not_dead", "signature": "def test_loop_carried_var_not_dead(self)"}, {"kind": "method", "line": 156, "name": "test_line_numbers_survive_subscript_stores", "signature": "def test_line_numbers_survive_subscript_stores(self)"}, {"kind": "method", "line": 167, "name": "test_member_store_not_local_assign", "signature": "def test_member_store_not_local_assign(self)"}, {"kind": "method", "line": 173, "name": "test_array_arg_to_filler_counts_as_init", "signature": "def test_array_arg_to_filler_counts_as_init(self)"}, {"kind": "method", "line": 181, "name": "test_array_arg_to_readonly_still_uninit", "signature": "def test_array_arg_to_readonly_still_uninit(self)"}, {"kind": "method", "line": 188, "name": "test_array_filled_in_decl_init_call", "signature": "def test_array_filled_in_decl_init_call(self)"}, {"kind": "method", "line": 196, "name": "test_static_never_uninit", "signature": "def test_static_never_uninit(self)"}, {"kind": "method", "line": 203, "name": "test_derived_pointer_not_dead", "signature": "def test_derived_pointer_not_dead(self)"}, {"kind": "method", "line": 216, "name": "test_sizeof_is_not_a_read", "signature": "def test_sizeof_is_not_a_read(self)"}, {"kind": "method", "line": 225, "name": "test_block_comment_malloc_ignored", "signature": "def test_block_comment_malloc_ignored(self)"}, {"kind": "method", "line": 234, "name": "test_address_alias_pointer_not_dead", "signature": "def test_address_alias_pointer_not_dead(self)"}, {"kind": "method", "line": 248, "name": "test_array_store_before_read_suppresses_uninit", "signature": "def test_array_store_before_read_suppresses_uninit(self)"}, {"kind": "method", "line": 256, "name": "test_same_line_use_not_dead", "signature": "def test_same_line_use_not_dead(self)"}, {"kind": "method", "line": 264, "name": "test_same_line_only_assign_is_dead", "signature": "def test_same_line_only_assign_is_dead(self)"}, {"kind": "method", "line": 272, "name": "test_alias_pointer_store_initializes_array", "signature": "def test_alias_pointer_store_initializes_array(self)"}, {"kind": "method", "line": 281, "name": "test_inline_alias_fill_suppresses_uninit", "signature": "def test_inline_alias_fill_suppresses_uninit(self)"}, {"kind": "method", "line": 290, "name": "test_function_pointer_call_counts_as_use", "signature": "def test_function_pointer_call_counts_as_use(self)"}, {"kind": "method", "line": 298, "name": "test_plain_call_is_not_a_local_use", "signature": "def test_plain_call_is_not_a_local_use(self)"}, {"kind": "method", "line": 305, "name": "test_local_struct_does_not_truncate_span", "signature": "def test_local_struct_does_not_truncate_span(self)"}, {"kind": "method", "line": 329, "name": "test_file_scope_symbol_still_bounds_span", "signature": "def test_file_scope_symbol_still_bounds_span(self)"}, {"kind": "method", "line": 344, "name": "test_url_string_does_not_truncate_line", "signature": "def test_url_string_does_not_truncate_line(self)"}, {"kind": "method", "line": 352, "name": "test_assert_macro_counts_as_null_check", "signature": "def test_assert_macro_counts_as_null_check(self)"}, {"kind": "method", "line": 360, "name": "test_multiline_call_assigns_array_arg", "signature": "def test_multiline_call_assigns_array_arg(self)"}, {"kind": "method", "line": 369, "name": "test_address_taken_suppresses_dead_store", "signature": "def test_address_taken_suppresses_dead_store(self)"}, {"kind": "method", "line": 377, "name": "test_member_store_initializes_base", "signature": "def test_member_store_initializes_base(self)"}]}, {"doc": "Contract tests for the DeadCodeStripper.  Validates dead code detection, in-degree computation, entry point exclusion, and recommendation classification.", "id": "tests/test_dead_code.py", "kind": "module", "label": "test_dead_code.py", "language": "py", "sha256": "4878048842697a87", "symbol_count": 15, "symbols": [{"doc": "Contract: DeadCodeStripper identifies orphaned symbols.", "kind": "class", "line": 16, "name": "TestDeadCodeStripperContract", "signature": "class TestDeadCodeStripperContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_symbol", "signature": "def _make_symbol(self, name, kind)"}, {"kind": "method", "line": 26, "name": "_make_node", "signature": "def _make_node(self, nid, symbols)"}, {"kind": "method", "line": 35, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt)"}, {"kind": "method", "line": 38, "name": "test_identify_empty_graph_returns_empty", "signature": "def test_identify_empty_graph_returns_empty(self)"}, {"kind": "method", "line": 42, "name": "test_identify_finds_dead_symbol", "signature": "def test_identify_finds_dead_symbol(self)"}, {"kind": "method", "line": 53, "name": "test_identify_excludes_entry_points", "signature": "def test_identify_excludes_entry_points(self)"}, {"kind": "method", "line": 61, "name": "test_identify_excludes_app_entry_point", "signature": "def test_identify_excludes_app_entry_point(self)"}, {"kind": "method", "line": 69, "name": "test_identify_excludes_init_entry_point", "signature": "def test_identify_excludes_init_entry_point(self)"}, {"kind": "method", "line": 77, "name": "test_identify_recommends_review_for_classes", "signature": "def test_identify_recommends_review_for_classes(self)"}, {"kind": "method", "line": 85, "name": "test_identify_recommends_trash_for_functions", "signature": "def test_identify_recommends_trash_for_functions(self)"}, {"kind": "method", "line": 93, "name": "test_identify_recommends_trash_for_variables", "signature": "def test_identify_recommends_trash_for_variables(self)"}, {"kind": "method", "line": 101, "name": "test_all_symbols_imported_returns_empty", "signature": "def test_all_symbols_imported_returns_empty(self)"}, {"kind": "method", "line": 113, "name": "test_reports_sorted_by_file_path", "signature": "def test_reports_sorted_by_file_path(self)"}]}, {"doc": "Contract tests for interactive system maps.  Validates typed intermediate representations, deterministic validation receipts, before and after comparison, and self-contained HTML rendering for the five diagram kinds.", "id": "tests/test_diagrams.py", "kind": "module", "label": "test_diagrams.py", "language": "py", "sha256": "b7cdc257d034f07a", "symbol_count": 69, "symbols": [{"doc": "Contract: builder produces deterministic maps for all five kinds.", "kind": "class", "line": 30, "name": "TestSystemMapBuilderContract", "signature": "class TestSystemMapBuilderContract(TestCase)"}, {"doc": "Contract: validator returns deterministic receipts with rule codes.", "kind": "class", "line": 176, "name": "TestSystemMapValidatorContract", "signature": "class TestSystemMapValidatorContract(TestCase)"}, {"doc": "Contract: renderer emits standalone interactive HTML documents.", "kind": "class", "line": 237, "name": "TestInteractiveMapRendererContract", "signature": "class TestInteractiveMapRendererContract(TestCase)"}, {"doc": "Contract: publisher writes maps plus a gallery index as a static site.", "kind": "class", "line": 360, "name": "TestDocsSitePublisherContract", "signature": "class TestDocsSitePublisherContract(TestCase)"}, {"doc": "Contract: vis.js renderer emits CDN-powered physics documents.", "kind": "class", "line": 503, "name": "TestVisNetworkRendererContract", "signature": "class TestVisNetworkRendererContract(TestCase)"}, {"doc": "Contract: default exports are vis.js maps with gallery links.", "kind": "class", "line": 619, "name": "TestDiagramVariantsContract", "signature": "class TestDiagramVariantsContract(TestCase)"}, {"doc": "Initialise builder with default configuration.", "kind": "method", "line": 33, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Create a small deterministic project graph.", "kind": "method", "line": 38, "name": "_make_graph", "signature": "def _make_graph(self)"}, {"doc": "Builder exposes architecture, workflow, sequence, dataflow, lifecycle.", "kind": "method", "line": 52, "name": "test_builder_supports_five_kinds", "signature": "def test_builder_supports_five_kinds(self)"}, {"doc": "Build all returns one map per supported kind.", "kind": "method", "line": 59, "name": "test_builder_produces_all_kinds", "signature": "def test_builder_produces_all_kinds(self)"}, {"doc": "Two builds over identical input share coordinates and bytes.", "kind": "method", "line": 68, "name": "test_builder_is_deterministic", "signature": "def test_builder_is_deterministic(self)"}, {"doc": "Shuffled input edges yield identical ordered map relationships.", "kind": "method", "line": 80, "name": "test_builder_orders_links_deterministically", "signature": "def test_builder_orders_links_deterministically(self)"}, {"doc": "Large layered graphs validate for every diagram kind.", "kind": "method", "line": 101, "name": "test_builder_validates_large_graph_for_all_kinds", "signature": "def test_builder_validates_large_graph_for_all_kinds(self)"}, {"doc": "Built maps record shown scope and total input file count.", "kind": "method", "line": 119, "name": "test_builder_reports_total_scope", "signature": "def test_builder_reports_total_scope(self)"}, {"doc": "Map nodes carry symbol records, file docs, and language.", "kind": "method", "line": 126, "name": "test_builder_attaches_symbols_and_docs", "signature": "def test_builder_attaches_symbols_and_docs(self)"}, {"doc": "Symbol records respect the per-node configured cap.", "kind": "method", "line": 143, "name": "test_builder_truncates_symbols_per_node", "signature": "def test_builder_truncates_symbols_per_node(self)"}, {"doc": "Oversized graphs are truncated to the configured node limit.", "kind": "method", "line": 152, "name": "test_builder_truncates_to_configured_limit", "signature": "def test_builder_truncates_to_configured_limit(self)"}, {"doc": "Delta comparison reports added, removed, and rerouted facts.", "kind": "method", "line": 162, "name": "test_compare_reports_added_removed_rerouted", "signature": "def test_compare_reports_added_removed_rerouted(self)"}, {"doc": "Initialise validator with default configuration.", "kind": "method", "line": 179, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Create a minimal valid architecture map.", "kind": "method", "line": 184, "name": "_valid_map", "signature": "def _valid_map(self)"}, {"doc": "Valid maps pass with the full check list and zero errors.", "kind": "method", "line": 197, "name": "test_validator_passes_valid_map", "signature": "def test_validator_passes_valid_map(self)"}, {"doc": "Duplicate identifiers fail with rule D001.", "kind": "method", "line": 204, "name": "test_validator_rejects_duplicate_node_ids", "signature": "def test_validator_rejects_duplicate_node_ids(self)"}, {"doc": "Edges pointing at unknown nodes fail with rule D002.", "kind": "method", "line": 214, "name": "test_validator_rejects_dangling_edge", "signature": "def test_validator_rejects_dangling_edge(self)"}, {"doc": "Maps without nodes fail with rule D003.", "kind": "method", "line": 222, "name": "test_validator_rejects_empty_map", "signature": "def test_validator_rejects_empty_map(self)"}, {"doc": "Unknown diagram kinds fail with rule D000.", "kind": "method", "line": 228, "name": "test_validator_rejects_unknown_kind", "signature": "def test_validator_rejects_unknown_kind(self)"}, {"doc": "Initialise builder and renderer with default configuration.", "kind": "method", "line": 240, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Build a small map of the requested kind.", "kind": "method", "line": 246, "name": "_map", "signature": "def _map(self, kind)"}, {"doc": "Output is a complete HTML document with inline SVG.", "kind": "method", "line": 256, "name": "test_renderer_produces_standalone_document", "signature": "def test_renderer_produces_standalone_document(self)"}, {"doc": "Output performs no external fetches or CDN references.", "kind": "method", "line": 263, "name": "test_renderer_has_no_external_requests", "signature": "def test_renderer_has_no_external_requests(self)"}, {"doc": "Output includes search, passport, reach, route, lens, views, export.", "kind": "method", "line": 270, "name": "test_renderer_includes_interaction_controls", "signature": "def test_renderer_includes_interaction_controls(self)"}, {"doc": "Output documents shortcuts and hash deep link contracts.", "kind": "method", "line": 276, "name": "test_renderer_includes_keyboard_and_deep_links", "signature": "def test_renderer_includes_keyboard_and_deep_links(self)"}, {"doc": "Malicious labels are escaped and never break the document.", "kind": "method", "line": 285, "name": "test_renderer_escapes_malicious_labels", "signature": "def test_renderer_escapes_malicious_labels(self)"}, {"doc": "Embedded payload scripts parse as valid JSON arrays.", "kind": "method", "line": 298, "name": "test_renderer_embeds_valid_json_payloads", "signature": "def test_renderer_embeds_valid_json_payloads(self)"}, {"doc": "Every diagram kind renders a standalone document.", "kind": "method", "line": 307, "name": "test_renderer_covers_all_five_kinds", "signature": "def test_renderer_covers_all_five_kinds(self)"}, {"doc": "Maps with a home target expose a gallery back link.", "kind": "method", "line": 314, "name": "test_renderer_links_gallery_home_when_configured", "signature": "def test_renderer_links_gallery_home_when_configured(self)"}, {"doc": "Maps without a home target expose no gallery link.", "kind": "method", "line": 321, "name": "test_renderer_omits_gallery_home_by_default", "signature": "def test_renderer_omits_gallery_home_by_default(self)"}, {"doc": "Canvas background differs from node fill for readability.", "kind": "method", "line": 326, "name": "test_renderer_keeps_canvas_distinct_from_nodes", "signature": "def test_renderer_keeps_canvas_distinct_from_nodes(self)"}, {"doc": "Nodes are draggable with pointer capture plus a force pass.", "kind": "method", "line": 334, "name": "test_renderer_supports_drag_and_settle", "signature": "def test_renderer_supports_drag_and_settle(self)"}, {"doc": "Exports drop temporary focus, dim, and drag classes.", "kind": "method", "line": 342, "name": "test_renderer_sanitizes_viewer_state_on_export", "signature": "def test_renderer_sanitizes_viewer_state_on_export(self)"}, {"doc": "Every toolbar action carries a human-readable title.", "kind": "method", "line": 348, "name": "test_renderer_buttons_explain_their_purpose", "signature": "def test_renderer_buttons_explain_their_purpose(self)"}, {"doc": "Initialise builder and publisher with default configuration.", "kind": "method", "line": 363, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Build all five maps from a small deterministic graph.", "kind": "method", "line": 369, "name": "_maps", "signature": "def _maps(self)"}, {"doc": "Publish creates an index, five map files, and a nojekyll marker.", "kind": "method", "line": 379, "name": "test_publish_writes_index_plus_five_maps", "signature": "def test_publish_writes_index_plus_five_maps(self)"}, {"doc": "Gallery index links every published map with relative paths.", "kind": "method", "line": 390, "name": "test_publish_index_links_every_map", "signature": "def test_publish_index_links_every_map(self)"}, {"doc": "Index and maps perform no external fetches or CDN references.", "kind": "method", "line": 399, "name": "test_publish_output_has_no_external_requests", "signature": "def test_publish_output_has_no_external_requests(self)"}, {"doc": "Two publishes over identical input share index bytes.", "kind": "method", "line": 412, "name": "test_publish_is_deterministic", "signature": "def test_publish_is_deterministic(self)"}, {"doc": "Malicious project names are escaped in the gallery index.", "kind": "method", "line": 423, "name": "test_publish_escapes_malicious_project_name", "signature": "def test_publish_escapes_malicious_project_name(self)"}, {"doc": "Malicious statistics keys are escaped in the gallery index.", "kind": "method", "line": 432, "name": "test_publish_escapes_malicious_stat_keys", "signature": "def test_publish_escapes_malicious_stat_keys(self)"}, {"doc": "Maps failing validation are skipped while the index is written.", "kind": "method", "line": 443, "name": "test_publish_skips_invalid_maps", "signature": "def test_publish_skips_invalid_maps(self)"}, {"doc": "Empty input writes an index with an empty gallery notice.", "kind": "method", "line": 455, "name": "test_publish_empty_maps_writes_empty_gallery", "signature": "def test_publish_empty_maps_writes_empty_gallery(self)"}, {"doc": "Publish never mutates the caller supplied map metadata.", "kind": "method", "line": 464, "name": "test_publish_leaves_input_maps_unmodified", "signature": "def test_publish_leaves_input_maps_unmodified(self)"}, {"doc": "Flat layouts link maps beside the index with a local home.", "kind": "method", "line": 473, "name": "test_publish_flat_subdir_keeps_links_relative", "signature": "def test_publish_flat_subdir_keeps_links_relative(self)"}, {"doc": "Gallery index documents the reader interactions.", "kind": "method", "line": 486, "name": "test_publish_index_explains_how_to_read", "signature": "def test_publish_index_explains_how_to_read(self)"}, {"doc": "Gallery cards state shown files against the project total.", "kind": "method", "line": 494, "name": "test_publish_card_reports_primary_scope", "signature": "def test_publish_card_reports_primary_scope(self)"}, {"doc": "Initialise builder and renderer with default configuration.", "kind": "method", "line": 506, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Build a small map of the requested kind.", "kind": "method", "line": 512, "name": "_map", "signature": "def _map(self, kind)"}, {"doc": "Script and style tags come from Config, never hardcoded.", "kind": "method", "line": 522, "name": "test_renderer_uses_configured_cdn_urls", "signature": "def test_renderer_uses_configured_cdn_urls(self)"}, {"doc": "Output instantiates a vis network with physics enabled.", "kind": "method", "line": 535, "name": "test_renderer_builds_vis_network_with_physics", "signature": "def test_renderer_builds_vis_network_with_physics(self)"}, {"doc": "Vis maps with a home target expose a gallery back link.", "kind": "method", "line": 543, "name": "test_renderer_links_gallery_home_when_configured", "signature": "def test_renderer_links_gallery_home_when_configured(self)"}, {"doc": "Physics honors the configured enabled flag.", "kind": "method", "line": 551, "name": "test_renderer_disables_physics_from_config", "signature": "def test_renderer_disables_physics_from_config(self)"}, {"doc": "Malicious labels never break tooltips or markup.", "kind": "method", "line": 558, "name": "test_renderer_escapes_malicious_titles", "signature": "def test_renderer_escapes_malicious_titles(self)"}, {"doc": "Output carries search, reach, route, lens, chapters, export.", "kind": "method", "line": 571, "name": "test_renderer_exposes_reader_controls", "signature": "def test_renderer_exposes_reader_controls(self)"}, {"doc": "Two renders over identical input share bytes.", "kind": "method", "line": 577, "name": "test_renderer_is_deterministic", "signature": "def test_renderer_is_deterministic(self)"}, {"doc": "Embedded node and edge payloads parse as valid JSON.", "kind": "method", "line": 582, "name": "test_renderer_embeds_valid_payloads", "signature": "def test_renderer_embeds_valid_payloads(self)"}, {"doc": "Node payloads and tooltips expose symbols with signatures.", "kind": "method", "line": 590, "name": "test_renderer_documents_symbols_per_file", "signature": "def test_renderer_documents_symbols_per_file(self)"}, {"doc": "Malicious symbol documentation never breaks tooltips.", "kind": "method", "line": 606, "name": "test_renderer_escapes_malicious_symbol_docs", "signature": "def test_renderer_escapes_malicious_symbol_docs(self)"}, {"doc": "Create a two-file project in a temporary directory.", "kind": "method", "line": 622, "name": "_project", "signature": "def _project(self, tmp)"}, {"doc": "Default diagram export writes CDN-powered vis.js maps.", "kind": "method", "line": 627, "name": "test_export_diagrams_writes_vis_maps_by_default", "signature": "def test_export_diagrams_writes_vis_maps_by_default(self)"}, {"doc": "Disabled vis flag produces offline maps without CDN.", "kind": "method", "line": 641, "name": "test_export_diagrams_falls_back_offline_when_disabled", "signature": "def test_export_diagrams_falls_back_offline_when_disabled(self)"}]}, {"id": "tests/test_documentation.py", "kind": "module", "label": "test_documentation.py", "language": "py", "sha256": "11ed437912c144e4", "symbol_count": 29, "symbols": [{"kind": "class", "line": 17, "name": "TestDocumentationGeneratorContract", "signature": "class TestDocumentationGeneratorContract(TestCase)"}, {"kind": "method", "line": 18, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 22, "name": "test_contains_header", "signature": "def test_contains_header(self)"}, {"kind": "method", "line": 26, "name": "test_contains_metadata_line", "signature": "def test_contains_metadata_line(self)"}, {"kind": "method", "line": 32, "name": "test_contains_mermaid_block", "signature": "def test_contains_mermaid_block(self)"}, {"kind": "method", "line": 37, "name": "test_contains_architecture_reference", "signature": "def test_contains_architecture_reference(self)"}, {"kind": "method", "line": 41, "name": "test_contains_cpg_block", "signature": "def test_contains_cpg_block(self)"}, {"kind": "method", "line": 46, "name": "test_contains_statistics_dashboard", "signature": "def test_contains_statistics_dashboard(self)"}, {"kind": "method", "line": 51, "name": "test_groups_files_by_language", "signature": "def test_groups_files_by_language(self)"}, {"kind": "method", "line": 70, "name": "test_lists_symbols_under_file", "signature": "def test_lists_symbols_under_file(self)"}, {"kind": "method", "line": 83, "name": "test_class_symbol_is_pluralized_correctly", "signature": "def test_class_symbol_is_pluralized_correctly(self)"}, {"kind": "method", "line": 97, "name": "test_function_pluralization", "signature": "def test_function_pluralization(self)"}, {"kind": "method", "line": 109, "name": "test_method_pluralization", "signature": "def test_method_pluralization(self)"}, {"kind": "method", "line": 121, "name": "test_shows_no_symbols_for_empty_files", "signature": "def test_shows_no_symbols_for_empty_files(self)"}, {"kind": "method", "line": 132, "name": "test_includes_file_path", "signature": "def test_includes_file_path(self)"}, {"kind": "method", "line": 143, "name": "test_docstring_in_output", "signature": "def test_docstring_in_output(self)"}, {"kind": "method", "line": 155, "name": "test_truncation_note_when_limited", "signature": "def test_truncation_note_when_limited(self)"}, {"kind": "method", "line": 165, "name": "test_taint_propagation_section_present", "signature": "def test_taint_propagation_section_present(self)"}, {"kind": "method", "line": 185, "name": "test_hotspot_section_present", "signature": "def test_hotspot_section_present(self)"}, {"kind": "method", "line": 203, "name": "test_no_taint_section_when_empty", "signature": "def test_no_taint_section_when_empty(self)"}, {"kind": "method", "line": 207, "name": "test_no_hotspot_section_when_empty", "signature": "def test_no_hotspot_section_when_empty(self)"}, {"kind": "method", "line": 211, "name": "test_cpg_block_disabled_via_config", "signature": "def test_cpg_block_disabled_via_config(self)"}, {"kind": "method", "line": 217, "name": "test_architectural_layers_section", "signature": "def test_architectural_layers_section(self)"}, {"kind": "method", "line": 229, "name": "test_security_findings_section", "signature": "def test_security_findings_section(self)"}, {"kind": "method", "line": 252, "name": "test_context_budget_zero_returns_full_content", "signature": "def test_context_budget_zero_returns_full_content(self)"}, {"kind": "method", "line": 260, "name": "test_context_budget_returns_compact_summary", "signature": "def test_context_budget_returns_compact_summary(self)"}, {"kind": "method", "line": 268, "name": "test_context_budget_prioritizes_god_nodes", "signature": "def test_context_budget_prioritizes_god_nodes(self)"}, {"kind": "method", "line": 285, "name": "test_context_budget_truncates_at_limit", "signature": "def test_context_budget_truncates_at_limit(self)"}, {"kind": "method", "line": 293, "name": "test_context_budget_includes_security_findings", "signature": "def test_context_budget_includes_security_findings(self)"}]}, {"doc": "Contract tests for the GraphExporter.  Validates JSON, HTML, and SVG export formats with various node/edge configurations and analysis metadata.", "id": "tests/test_exporter.py", "kind": "module", "label": "test_exporter.py", "language": "py", "sha256": "b70cde45a0105c5f", "symbol_count": 15, "symbols": [{"doc": "Contract: GraphExporter produces valid JSON, HTML, and SVG outputs.", "kind": "class", "line": 23, "name": "TestGraphExporterContract", "signature": "class TestGraphExporterContract(TestCase)"}, {"kind": "method", "line": 26, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 30, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang, symbols)"}, {"kind": "method", "line": 42, "name": "_make_sym", "signature": "def _make_sym(self, name, kind, line)"}, {"kind": "method", "line": 47, "name": "test_to_json_produces_valid_json", "signature": "def test_to_json_produces_valid_json(self)"}, {"kind": "method", "line": 56, "name": "test_to_json_includes_symbol_data", "signature": "def test_to_json_includes_symbol_data(self)"}, {"kind": "method", "line": 65, "name": "test_to_json_includes_metadata", "signature": "def test_to_json_includes_metadata(self)"}, {"kind": "method", "line": 76, "name": "test_to_json_includes_analysis_metadata", "signature": "def test_to_json_includes_analysis_metadata(self)"}, {"kind": "method", "line": 101, "name": "test_to_html_produces_standalone_page", "signature": "def test_to_html_produces_standalone_page(self)"}, {"kind": "method", "line": 109, "name": "test_to_html_includes_node_data", "signature": "def test_to_html_includes_node_data(self)"}, {"kind": "method", "line": 116, "name": "test_to_html_includes_community_legend_when_analysis", "signature": "def test_to_html_includes_community_legend_when_analysis(self)"}, {"kind": "method", "line": 138, "name": "test_to_svg_produces_svg_string", "signature": "def test_to_svg_produces_svg_string(self)"}, {"kind": "method", "line": 145, "name": "test_to_svg_render_truncation_for_large_graph", "signature": "def test_to_svg_render_truncation_for_large_graph(self)"}, {"kind": "method", "line": 154, "name": "test_to_svg_includes_readmenator_title", "signature": "def test_to_svg_includes_readmenator_title(self)"}, {"kind": "method", "line": 160, "name": "test_to_json_handles_resolved_edges", "signature": "def test_to_json_handles_resolved_edges(self)"}]}, {"doc": "Contract tests for the GitHub wiki publisher (no network: git/gh calls are faked).", "id": "tests/test_gh_wiki.py", "kind": "module", "label": "test_gh_wiki.py", "language": "py", "sha256": "d839e4cbda80fe15", "symbol_count": 15, "symbols": [{"doc": "Records commands and simulates gh/git with a local wiki clone.", "kind": "class", "line": 14, "name": "_FakeRunner", "signature": "class _FakeRunner"}, {"doc": "Create generated outputs the publisher mirrors.", "kind": "method", "line": 41, "name": "_project", "signature": "def _project(root, config)"}, {"doc": "Pages are flat, linked, navigable, and pinned to the source commit.", "kind": "class", "line": 61, "name": "TestGitHubWikiPages", "signature": "class TestGitHubWikiPages(TestCase)"}, {"doc": "Publishing clones the wiki remote, commits, and pushes only when changed.", "kind": "class", "line": 115, "name": "TestGitHubWikiPublish", "signature": "class TestGitHubWikiPublish(TestCase)"}, {"kind": "method", "line": 17, "name": "__init__", "signature": "def __init__(self, origin, clone_ok, dirty)"}, {"kind": "method", "line": 24, "name": "__call__", "signature": "def __call__(self, command, cwd)"}, {"kind": "method", "line": 64, "name": "test_gh_wiki_page_names_are_flat_and_prefixed", "signature": "def test_gh_wiki_page_names_are_flat_and_prefixed(self)"}, {"kind": "method", "line": 71, "name": "test_gh_wiki_render_rewrites_links_and_permalinks", "signature": "def test_gh_wiki_render_rewrites_links_and_permalinks(self)"}, {"kind": "method", "line": 88, "name": "test_gh_wiki_permalinks_never_escape_project_root", "signature": "def test_gh_wiki_permalinks_never_escape_project_root(self)"}, {"kind": "method", "line": 96, "name": "test_gh_wiki_dry_run_writes_locally_and_prunes_only_owned_pages", "signature": "def test_gh_wiki_dry_run_writes_locally_and_prunes_only_owned_pages(self)"}, {"kind": "method", "line": 118, "name": "test_gh_wiki_publish_clones_commits_and_pushes", "signature": "def test_gh_wiki_publish_clones_commits_and_pushes(self)"}, {"kind": "method", "line": 130, "name": "test_gh_wiki_publish_skips_push_when_unchanged", "signature": "def test_gh_wiki_publish_skips_push_when_unchanged(self)"}, {"kind": "method", "line": 139, "name": "test_gh_wiki_publish_explains_uninitialized_wiki", "signature": "def test_gh_wiki_publish_explains_uninitialized_wiki(self)"}, {"kind": "method", "line": 147, "name": "test_gh_wiki_rejects_malformed_configured_remote", "signature": "def test_gh_wiki_rejects_malformed_configured_remote(self)"}, {"kind": "method", "line": 154, "name": "test_gh_wiki_disabled_by_default", "signature": "def test_gh_wiki_disabled_by_default(self)"}]}, {"id": "tests/test_hotspots.py", "kind": "module", "label": "test_hotspots.py", "language": "py", "sha256": "2f31e5fb128e17d4", "symbol_count": 11, "symbols": [{"doc": "Contract: HotspotAnalyzer detects hotspots, cycles, and change impact.", "kind": "class", "line": 10, "name": "TestHotspotAnalyzerContract", "signature": "class TestHotspotAnalyzerContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label, sym_count)"}, {"kind": "method", "line": 29, "name": "test_empty_graph_returns_empty_hotspots", "signature": "def test_empty_graph_returns_empty_hotspots(self)"}, {"kind": "method", "line": 33, "name": "test_hotspots_rank_by_combined_score", "signature": "def test_hotspots_rank_by_combined_score(self)"}, {"kind": "method", "line": 43, "name": "test_hotspot_includes_scores", "signature": "def test_hotspot_includes_scores(self)"}, {"kind": "method", "line": 53, "name": "test_no_cycles_in_acyclic_graph", "signature": "def test_no_cycles_in_acyclic_graph(self)"}, {"kind": "method", "line": 66, "name": "test_detects_simple_cycle", "signature": "def test_detects_simple_cycle(self)"}, {"kind": "method", "line": 79, "name": "test_change_impact_ranks_by_total_impact", "signature": "def test_change_impact_ranks_by_total_impact(self)"}, {"kind": "method", "line": 94, "name": "test_change_impact_no_edges", "signature": "def test_change_impact_no_edges(self)"}, {"kind": "method", "line": 100, "name": "test_hotspot_weights_from_config", "signature": "def test_hotspot_weights_from_config(self)"}]}, {"id": "tests/test_integration.py", "kind": "module", "label": "test_integration.py", "language": "py", "sha256": "fa1c42eb78225f90", "symbol_count": 16, "symbols": [{"kind": "class", "line": 9, "name": "TestEndToEndContract", "signature": "class TestEndToEndContract(TestCase)"}, {"kind": "method", "line": 10, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 15, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 19, "name": "_write", "signature": "def _write(self, path, content)"}, {"kind": "method", "line": 24, "name": "test_full_pipeline_generates_knowledge_base", "signature": "def test_full_pipeline_generates_knowledge_base(self)"}, {"kind": "method", "line": 40, "name": "test_knowledge_base_contains_mermaid", "signature": "def test_knowledge_base_contains_mermaid(self)"}, {"kind": "method", "line": 48, "name": "test_query_subcommand_works", "signature": "def test_query_subcommand_works(self)"}, {"kind": "method", "line": 53, "name": "test_explain_subcommand_works", "signature": "def test_explain_subcommand_works(self)"}, {"kind": "method", "line": 59, "name": "test_path_subcommand_works", "signature": "def test_path_subcommand_works(self)"}, {"kind": "method", "line": 65, "name": "test_summary_works", "signature": "def test_summary_works(self)"}, {"kind": "method", "line": 71, "name": "test_rebuild", "signature": "def test_rebuild(self)"}, {"kind": "method", "line": 81, "name": "test_knowledge_base_contains_cpg", "signature": "def test_knowledge_base_contains_cpg(self)"}, {"kind": "method", "line": 89, "name": "test_knowledge_base_contains_statistics_dashboard", "signature": "def test_knowledge_base_contains_statistics_dashboard(self)"}, {"kind": "method", "line": 98, "name": "test_audit_deep_returns_analysis", "signature": "def test_audit_deep_returns_analysis(self)"}, {"kind": "method", "line": 105, "name": "test_privacy_mode_works", "signature": "def test_privacy_mode_works(self)"}, {"kind": "method", "line": 114, "name": "test_export_sarif_produces_file", "signature": "def test_export_sarif_produces_file(self)"}]}, {"id": "tests/test_layer_rules.py", "kind": "module", "label": "test_layer_rules.py", "language": "py", "sha256": "d530692da5fb3cd6", "symbol_count": 13, "symbols": [{"doc": "Contract: LayerRuleEngine detects architectural layer violations.", "kind": "class", "line": 10, "name": "TestLayerRuleEngineContract", "signature": "class TestLayerRuleEngineContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label)"}, {"kind": "method", "line": 20, "name": "test_empty_graph_returns_empty_violations", "signature": "def test_empty_graph_returns_empty_violations(self)"}, {"kind": "method", "line": 24, "name": "test_no_layers_returns_empty_violations", "signature": "def test_no_layers_returns_empty_violations(self)"}, {"kind": "method", "line": 29, "name": "test_same_layer_no_violation", "signature": "def test_same_layer_no_violation(self)"}, {"kind": "method", "line": 36, "name": "test_forbidden_edge_detected", "signature": "def test_forbidden_edge_detected(self)"}, {"kind": "method", "line": 46, "name": "test_allowed_testing_edges_no_violation", "signature": "def test_allowed_testing_edges_no_violation(self)"}, {"kind": "method", "line": 57, "name": "test_multiple_violations", "signature": "def test_multiple_violations(self)"}, {"kind": "method", "line": 75, "name": "test_utility_layer_ignored", "signature": "def test_utility_layer_ignored(self)"}, {"kind": "method", "line": 82, "name": "test_violation_summary", "signature": "def test_violation_summary(self)"}, {"kind": "method", "line": 104, "name": "test_resolved_edges_also_checked", "signature": "def test_resolved_edges_also_checked(self)"}, {"kind": "method", "line": 115, "name": "test_presentation_to_data_access_forbidden", "signature": "def test_presentation_to_data_access_forbidden(self)"}]}, {"doc": "Contract tests for the ArchitectureLinter.  Validates file length checks, cross-layer violation detection, and circular dependency identification.", "id": "tests/test_linter.py", "kind": "module", "label": "test_linter.py", "language": "py", "sha256": "f65b401457b24d7c", "symbol_count": 14, "symbols": [{"doc": "Contract: ArchitectureLinter enforces architectural rules.", "kind": "class", "line": 16, "name": "TestArchitectureLinterContract", "signature": "class TestArchitectureLinterContract(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 26, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt, rel)"}, {"kind": "method", "line": 29, "name": "test_lint_empty_graph_returns_no_violations", "signature": "def test_lint_empty_graph_returns_no_violations(self)"}, {"kind": "method", "line": 33, "name": "test_lint_returns_empty_for_files_under_threshold", "signature": "def test_lint_returns_empty_for_files_under_threshold(self)"}, {"kind": "method", "line": 40, "name": "test_lint_detects_file_exceeding_max_lines", "signature": "def test_lint_detects_file_exceeding_max_lines(self)"}, {"kind": "method", "line": 49, "name": "test_lint_detects_cross_layer_violation", "signature": "def test_lint_detects_cross_layer_violation(self)"}, {"kind": "method", "line": 61, "name": "test_lint_allows_same_layer_imports", "signature": "def test_lint_allows_same_layer_imports(self)"}, {"kind": "method", "line": 72, "name": "test_lint_allows_testing_to_business_logic", "signature": "def test_lint_allows_testing_to_business_logic(self)"}, {"kind": "method", "line": 83, "name": "test_lint_ignores_utility_layer", "signature": "def test_lint_ignores_utility_layer(self)"}, {"kind": "method", "line": 94, "name": "test_lint_detects_circular_dependencies", "signature": "def test_lint_detects_circular_dependencies(self)"}, {"kind": "method", "line": 108, "name": "test_violations_sorted_by_severity", "signature": "def test_violations_sorted_by_severity(self)"}, {"kind": "method", "line": 121, "name": "test_lint_returns_empty_when_disabled", "signature": "def test_lint_returns_empty_when_disabled(self)"}]}, {"doc": "Contract tests for the MCP server protocol and tool dispatch.  Validates JSON-RPC 2.0 message handling, tool definitions, resource definitions, proper error responses, and the full tool/resource lifecycle using a lightweight mock server.", "id": "tests/test_mcp_server.py", "kind": "module", "label": "test_mcp_server.py", "language": "py", "sha256": "b5ae9c9e9ce2e49f", "symbol_count": 25, "symbols": [{"doc": "Contract: MCP server implements JSON-RPC 2.0 over stdio.", "kind": "class", "line": 21, "name": "TestMCPProtocol", "signature": "class TestMCPProtocol(TestCase)"}, {"kind": "method", "line": 24, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 33, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 36, "name": "_make_request", "signature": "def _make_request(self, method, params, msg_id)"}, {"kind": "method", "line": 42, "name": "_call", "signature": "def _call(self, req)"}, {"kind": "method", "line": 49, "name": "test_initialize_exchanges_protocol_version", "signature": "def test_initialize_exchanges_protocol_version(self)"}, {"kind": "method", "line": 62, "name": "test_notifications_initialized_returns_no_response", "signature": "def test_notifications_initialized_returns_no_response(self)"}, {"kind": "method", "line": 67, "name": "test_unknown_method_returns_error", "signature": "def test_unknown_method_returns_error(self)"}, {"kind": "method", "line": 75, "name": "test_uninitialized_request_returns_error", "signature": "def test_uninitialized_request_returns_error(self)"}, {"kind": "method", "line": 85, "name": "test_list_tools_returns_all_tool_definitions", "signature": "def test_list_tools_returns_all_tool_definitions(self)"}, {"kind": "method", "line": 115, "name": "test_call_tool_without_initialize_returns_error", "signature": "def test_call_tool_without_initialize_returns_error(self)"}, {"kind": "method", "line": 123, "name": "test_call_tool_unknown_tool_returns_method_not_found", "signature": "def test_call_tool_unknown_tool_returns_method_not_found(self)"}, {"kind": "method", "line": 132, "name": "test_call_summary_tool_returns_content", "signature": "def test_call_summary_tool_returns_content(self)"}, {"kind": "method", "line": 145, "name": "test_call_query_tool_with_text_returns_results", "signature": "def test_call_query_tool_with_text_returns_results(self)"}, {"kind": "method", "line": 154, "name": "test_call_query_tool_missing_required_param_raises", "signature": "def test_call_query_tool_missing_required_param_raises(self)"}, {"kind": "method", "line": 168, "name": "test_list_resources_returns_resource_definitions", "signature": "def test_list_resources_returns_resource_definitions(self)"}, {"kind": "method", "line": 186, "name": "test_read_resource_summary_returns_json", "signature": "def test_read_resource_summary_returns_json(self)"}, {"kind": "method", "line": 197, "name": "test_read_resource_unknown_uri_returns_error", "signature": "def test_read_resource_unknown_uri_returns_error(self)"}, {"kind": "method", "line": 205, "name": "test_read_resource_kb_returns_markdown", "signature": "def test_read_resource_kb_returns_markdown(self)"}, {"kind": "method", "line": 219, "name": "_get_tool_def", "signature": "def _get_tool_def(self, name)"}, {"kind": "method", "line": 226, "name": "test_query_tool_requires_text_param", "signature": "def test_query_tool_requires_text_param(self)"}, {"kind": "method", "line": 230, "name": "test_explain_tool_requires_name_param", "signature": "def test_explain_tool_requires_name_param(self)"}, {"kind": "method", "line": 234, "name": "test_path_tool_requires_two_params", "signature": "def test_path_tool_requires_two_params(self)"}, {"kind": "method", "line": 243, "name": "test_parse_error_for_invalid_json", "signature": "def test_parse_error_for_invalid_json(self)"}, {"kind": "method", "line": 251, "name": "test_call_tool_returns_text_content_list", "signature": "def test_call_tool_returns_text_content_list(self)"}]}, {"id": "tests/test_mermaid.py", "kind": "module", "label": "test_mermaid.py", "language": "py", "sha256": "447a55c490312fe7", "symbol_count": 11, "symbols": [{"kind": "class", "line": 7, "name": "TestMermaidRendererContract", "signature": "class TestMermaidRendererContract(TestCase)"}, {"kind": "method", "line": 8, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 11, "name": "test_renders_graph_header", "signature": "def test_renders_graph_header(self)"}, {"kind": "method", "line": 19, "name": "test_renders_module_node", "signature": "def test_renders_module_node(self)"}, {"kind": "method", "line": 27, "name": "test_renders_symbol_subnodes", "signature": "def test_renders_symbol_subnodes(self)"}, {"kind": "method", "line": 36, "name": "test_class_symbol_gets_cls_style", "signature": "def test_class_symbol_gets_cls_style(self)"}, {"kind": "method", "line": 45, "name": "test_function_symbol_gets_fn_style", "signature": "def test_function_symbol_gets_fn_style(self)"}, {"kind": "method", "line": 54, "name": "test_external_import_edge_is_dashed", "signature": "def test_external_import_edge_is_dashed(self)"}, {"kind": "method", "line": 62, "name": "test_truncation_when_over_limit", "signature": "def test_truncation_when_over_limit(self)"}, {"kind": "method", "line": 72, "name": "test_limits_symbols_to_five_per_node", "signature": "def test_limits_symbols_to_five_per_node(self)"}, {"kind": "method", "line": 82, "name": "test_handles_special_characters_in_ids", "signature": "def test_handles_special_characters_in_ids(self)"}]}, {"id": "tests/test_models.py", "kind": "module", "label": "test_models.py", "language": "py", "sha256": "af0df48f490c3633", "symbol_count": 11, "symbols": [{"kind": "class", "line": 6, "name": "TestSymbolContract", "signature": "class TestSymbolContract(TestCase)"}, {"kind": "class", "line": 20, "name": "TestNodeContract", "signature": "class TestNodeContract(TestCase)"}, {"kind": "class", "line": 48, "name": "TestEdgeContract", "signature": "class TestEdgeContract(TestCase)"}, {"kind": "class", "line": 56, "name": "TestPluralizeContract", "signature": "class TestPluralizeContract(TestCase)"}, {"kind": "method", "line": 7, "name": "test_symbol_creation", "signature": "def test_symbol_creation(self)"}, {"kind": "method", "line": 15, "name": "test_symbol_with_signature", "signature": "def test_symbol_with_signature(self)"}, {"kind": "method", "line": 21, "name": "test_node_creation", "signature": "def test_node_creation(self)"}, {"kind": "method", "line": 35, "name": "test_node_with_symbols", "signature": "def test_node_with_symbols(self)"}, {"kind": "method", "line": 49, "name": "test_edge_creation", "signature": "def test_edge_creation(self)"}, {"kind": "method", "line": 57, "name": "test_pluralize_class", "signature": "def test_pluralize_class(self)"}, {"kind": "method", "line": 62, "name": "test_pluralize_unknown_appends_s", "signature": "def test_pluralize_unknown_appends_s(self)"}]}, {"id": "tests/test_parsers.py", "kind": "module", "label": "test_parsers.py", "language": "py", "sha256": "586493423afcd80a", "symbol_count": 87, "symbols": [{"kind": "class", "line": 22, "name": "TestCParserContract", "signature": "class TestCParserContract(TestCase)"}, {"kind": "class", "line": 88, "name": "TestPythonParserContract", "signature": "class TestPythonParserContract(TestCase)"}, {"kind": "class", "line": 157, "name": "TestGoParserContract", "signature": "class TestGoParserContract(TestCase)"}, {"kind": "class", "line": 200, "name": "TestRustParserContract", "signature": "class TestRustParserContract(TestCase)"}, {"kind": "class", "line": 238, "name": "TestJavaScriptParserContract", "signature": "class TestJavaScriptParserContract(TestCase)"}, {"kind": "class", "line": 277, "name": "TestJavaParserContract", "signature": "class TestJavaParserContract(TestCase)"}, {"kind": "class", "line": 309, "name": "TestCSharpParserContract", "signature": "class TestCSharpParserContract(TestCase)"}, {"kind": "class", "line": 342, "name": "TestShellParserContract", "signature": "class TestShellParserContract(TestCase)"}, {"kind": "class", "line": 361, "name": "TestPHPParserContract", "signature": "class TestPHPParserContract(TestCase)"}, {"kind": "class", "line": 387, "name": "TestDartParserContract", "signature": "class TestDartParserContract(TestCase)"}, {"kind": "class", "line": 412, "name": "TestGDScriptParserContract", "signature": "class TestGDScriptParserContract(TestCase)"}, {"kind": "class", "line": 430, "name": "TestNimParserContract", "signature": "class TestNimParserContract(TestCase)"}, {"kind": "class", "line": 456, "name": "TestAssemblyParserContract", "signature": "class TestAssemblyParserContract(TestCase)"}, {"kind": "class", "line": 483, "name": "TestParserFactoryContract", "signature": "class TestParserFactoryContract(TestCase)"}, {"kind": "method", "line": 23, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 26, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 33, "name": "test_extracts_struct", "signature": "def test_extracts_struct(self)"}, {"kind": "method", "line": 40, "name": "test_extracts_include", "signature": "def test_extracts_include(self)"}, {"kind": "method", "line": 47, "name": "test_extracts_define", "signature": "def test_extracts_define(self)"}, {"kind": "method", "line": 54, "name": "test_skips_reserved_words", "signature": "def test_skips_reserved_words(self)"}, {"kind": "method", "line": 64, "name": "test_function_line_points_at_definition", "signature": "def test_function_line_points_at_definition(self)"}, {"kind": "method", "line": 71, "name": "test_calls_are_not_prototypes", "signature": "def test_calls_are_not_prototypes(self)"}, {"kind": "method", "line": 80, "name": "test_class_with_inheritance", "signature": "def test_class_with_inheritance(self)"}, {"kind": "method", "line": 89, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 92, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 99, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 106, "name": "test_extracts_imports", "signature": "def test_extracts_imports(self)"}, {"kind": "method", "line": 114, "name": "test_extracts_async_function", "signature": "def test_extracts_async_function(self)"}, {"kind": "method", "line": 121, "name": "test_handles_syntax_error_gracefully", "signature": "def test_handles_syntax_error_gracefully(self)"}, {"kind": "method", "line": 127, "name": "test_suppresses_syntax_warnings", "signature": "def test_suppresses_syntax_warnings(self)"}, {"kind": "method", "line": 139, "name": "test_extracts_signature_with_params", "signature": "def test_extracts_signature_with_params(self)"}, {"kind": "method", "line": 147, "name": "test_extracts_class_with_bases", "signature": "def test_extracts_class_with_bases(self)"}, {"kind": "method", "line": 158, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 161, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 168, "name": "test_extracts_method_receiver", "signature": "def test_extracts_method_receiver(self)"}, {"kind": "method", "line": 175, "name": "test_extracts_import_block", "signature": "def test_extracts_import_block(self)"}, {"kind": "method", "line": 182, "name": "test_extracts_single_import", "signature": "def test_extracts_single_import(self)"}, {"kind": "method", "line": 188, "name": "test_extracts_struct_and_interface", "signature": "def test_extracts_struct_and_interface(self)"}, {"kind": "method", "line": 201, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 204, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 211, "name": "test_extracts_pub_function", "signature": "def test_extracts_pub_function(self)"}, {"kind": "method", "line": 218, "name": "test_extracts_struct_and_trait_and_enum", "signature": "def test_extracts_struct_and_trait_and_enum(self)"}, {"kind": "method", "line": 231, "name": "test_extracts_use", "signature": "def test_extracts_use(self)"}, {"kind": "method", "line": 239, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 242, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 249, "name": "test_extracts_arrow_function", "signature": "def test_extracts_arrow_function(self)"}, {"kind": "method", "line": 256, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 263, "name": "test_extracts_import_and_require", "signature": "def test_extracts_import_and_require(self)"}, {"kind": "method", "line": 270, "name": "test_skips_reserved_words", "signature": "def test_skips_reserved_words(self)"}, {"kind": "method", "line": 278, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 281, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 288, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 295, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 301, "name": "test_abstract_class", "signature": "def test_abstract_class(self)"}, {"kind": "method", "line": 310, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 313, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 320, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 327, "name": "test_extracts_using", "signature": "def test_extracts_using(self)"}, {"kind": "method", "line": 333, "name": "test_record_and_interface", "signature": "def test_record_and_interface(self)"}, {"kind": "method", "line": 343, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 346, "name": "test_extracts_function_with_parentheses", "signature": "def test_extracts_function_with_parentheses(self)"}, {"kind": "method", "line": 353, "name": "test_extracts_function_keyword", "signature": "def test_extracts_function_keyword(self)"}, {"kind": "method", "line": 362, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 365, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 372, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 379, "name": "test_extracts_use_and_require", "signature": "def test_extracts_use_and_require(self)"}, {"kind": "method", "line": 388, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 391, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 398, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 405, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 413, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 416, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 423, "name": "test_extracts_extends", "signature": "def test_extracts_extends(self)"}, {"kind": "method", "line": 431, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 434, "name": "test_extracts_proc", "signature": "def test_extracts_proc(self)"}, {"kind": "method", "line": 441, "name": "test_extracts_type", "signature": "def test_extracts_type(self)"}, {"kind": "method", "line": 448, "name": "test_extracts_import", "signature": "def test_extracts_import(self)"}, {"kind": "method", "line": 457, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 460, "name": "test_extracts_label", "signature": "def test_extracts_label(self)"}, {"kind": "method", "line": 467, "name": "test_extracts_multiple_labels", "signature": "def test_extracts_multiple_labels(self)"}, {"kind": "method", "line": 475, "name": "test_extracts_includes", "signature": "def test_extracts_includes(self)"}, {"kind": "method", "line": 484, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 487, "name": "test_returns_c_parser_for_c_extensions", "signature": "def test_returns_c_parser_for_c_extensions(self)"}, {"kind": "method", "line": 493, "name": "test_returns_python_parser_for_py", "signature": "def test_returns_python_parser_for_py(self)"}, {"kind": "method", "line": 498, "name": "test_returns_none_for_unknown_extension", "signature": "def test_returns_none_for_unknown_extension(self)"}, {"kind": "method", "line": 502, "name": "test_returns_rust_parser_for_rs", "signature": "def test_returns_rust_parser_for_rs(self)"}, {"kind": "method", "line": 507, "name": "test_case_insensitive_extension", "signature": "def test_case_insensitive_extension(self)"}]}, {"doc": "Contract tests for the 6 new language parsers.  Validates that Ruby, Swift, Kotlin, Scala, Lua, and Elixir parsers correctly extract symbols, imports, calls, and inheritance edges.", "id": "tests/test_parsers_new.py", "kind": "module", "label": "test_parsers_new.py", "language": "py", "sha256": "a737c2342ea5e554", "symbol_count": 36, "symbols": [{"kind": "class", "line": 15, "name": "TestRubyParserContract", "signature": "class TestRubyParserContract(TestCase)"}, {"kind": "class", "line": 45, "name": "TestSwiftParserContract", "signature": "class TestSwiftParserContract(TestCase)"}, {"kind": "class", "line": 68, "name": "TestKotlinParserContract", "signature": "class TestKotlinParserContract(TestCase)"}, {"kind": "class", "line": 85, "name": "TestScalaParserContract", "signature": "class TestScalaParserContract(TestCase)"}, {"kind": "class", "line": 102, "name": "TestLuaParserContract", "signature": "class TestLuaParserContract(TestCase)"}, {"kind": "class", "line": 117, "name": "TestElixirParserContract", "signature": "class TestElixirParserContract(TestCase)"}, {"kind": "class", "line": 134, "name": "TestNewParserFactoryContract", "signature": "class TestNewParserFactoryContract(TestCase)"}, {"kind": "class", "line": 151, "name": "TestPythonCallExtractionContract", "signature": "class TestPythonCallExtractionContract(TestCase)"}, {"kind": "method", "line": 16, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 19, "name": "test_extracts_class_with_inheritance", "signature": "def test_extracts_class_with_inheritance(self)"}, {"kind": "method", "line": 27, "name": "test_extracts_module", "signature": "def test_extracts_module(self)"}, {"kind": "method", "line": 33, "name": "test_extracts_method", "signature": "def test_extracts_method(self)"}, {"kind": "method", "line": 39, "name": "test_extracts_require", "signature": "def test_extracts_require(self)"}, {"kind": "method", "line": 46, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 49, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 55, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 61, "name": "test_extracts_protocol", "signature": "def test_extracts_protocol(self)"}, {"kind": "method", "line": 69, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 72, "name": "test_extracts_class", "signature": "def test_extracts_class(self)"}, {"kind": "method", "line": 78, "name": "test_extracts_fun", "signature": "def test_extracts_fun(self)"}, {"kind": "method", "line": 86, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 89, "name": "test_extracts_object", "signature": "def test_extracts_object(self)"}, {"kind": "method", "line": 95, "name": "test_extracts_def", "signature": "def test_extracts_def(self)"}, {"kind": "method", "line": 103, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 106, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 111, "name": "test_extracts_require", "signature": "def test_extracts_require(self)"}, {"kind": "method", "line": 118, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 121, "name": "test_extracts_defmodule", "signature": "def test_extracts_defmodule(self)"}, {"kind": "method", "line": 127, "name": "test_extracts_function", "signature": "def test_extracts_function(self)"}, {"kind": "method", "line": 135, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 138, "name": "test_ruby_extension_maps_correctly", "signature": "def test_ruby_extension_maps_correctly(self)"}, {"kind": "method", "line": 142, "name": "test_swift_extension_maps_correctly", "signature": "def test_swift_extension_maps_correctly(self)"}, {"kind": "method", "line": 146, "name": "test_kotlin_extension_maps_correctly", "signature": "def test_kotlin_extension_maps_correctly(self)"}, {"kind": "method", "line": 152, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 155, "name": "test_extracts_class_inheritance", "signature": "def test_extracts_class_inheritance(self)"}, {"kind": "method", "line": 160, "name": "test_extracts_function_calls", "signature": "def test_extracts_function_calls(self)"}]}, {"doc": "Property-based contract tests for all 19 language parsers.  Uses Hypothesis to generate random, malformed, edge-case, and massive inputs to guarantee parsers fail gracefully without crashing.  Run with: hypothesis profile (e.g. ``pytest --hypothesis-show-statistics``).  These tests are skipped if Hypothesis is not installed.", "id": "tests/test_parsers_property.py", "kind": "module", "label": "test_parsers_property.py", "language": "py", "sha256": "ff42464cddb86ba2", "symbol_count": 27, "symbols": [{"doc": "Generate source code with a configurable number of lines.", "kind": "function", "line": 105, "name": "_generate_multiline_code", "signature": "def _generate_multiline_code(lines, line_strategy)"}, {"doc": "Create a parser for the given extension.", "kind": "function", "line": 142, "name": "_create_parser", "signature": "def _create_parser(ext)"}, {"doc": "Property-based contract: parsers never crash on arbitrary input.", "kind": "class", "line": 155, "name": "TestParserHypothesisContract", "signature": "class TestParserHypothesisContract(TestCase)"}, {"doc": "Property-based tests specific to the Python parser (native ast).", "kind": "class", "line": 288, "name": "TestPythonParserProperty", "signature": "class TestPythonParserProperty(TestCase)"}, {"kind": "method", "line": 162, "name": "test_never_crashes_on_malformed_code", "signature": "def test_never_crashes_on_malformed_code(self, ext, code)"}, {"kind": "method", "line": 180, "name": "test_never_crashes_on_unicode_code", "signature": "def test_never_crashes_on_unicode_code(self, ext, code)"}, {"kind": "method", "line": 198, "name": "test_empty_code_returns_empty_or_valid", "signature": "def test_empty_code_returns_empty_or_valid(self, ext)"}, {"kind": "method", "line": 208, "name": "test_whitespace_code_returns_empty_or_valid", "signature": "def test_whitespace_code_returns_empty_or_valid(self, ext)"}, {"kind": "method", "line": 220, "name": "test_never_crashes_on_many_lines", "signature": "def test_never_crashes_on_many_lines(self, ext, lines)"}, {"kind": "method", "line": 238, "name": "test_repeated_keywords_no_crash", "signature": "def test_repeated_keywords_no_crash(self, ext)"}, {"kind": "method", "line": 257, "name": "test_parser_imports_is_list_of_strings", "signature": "def test_parser_imports_is_list_of_strings(self, ext)"}, {"kind": "method", "line": 269, "name": "test_unknown_extension_returns_none", "signature": "def test_unknown_extension_returns_none(self)"}, {"kind": "method", "line": 275, "name": "_assert_valid_symbols", "signature": "def _assert_valid_symbols(self, symbols)"}, {"kind": "method", "line": 291, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 296, "name": "test_python_never_crashes_on_weird_ascii", "signature": "def test_python_never_crashes_on_weird_ascii(self, code)"}, {"kind": "method", "line": 310, "name": "test_python_never_crashes_on_any_text", "signature": "def test_python_never_crashes_on_any_text(self, code)"}, {"doc": "Chainable placeholder that never generates data.", "kind": "class", "line": 45, "name": "_StrategyPlaceholder", "signature": "class _StrategyPlaceholder"}, {"doc": "Permissive strategy factory used only when hypothesis is missing.", "kind": "class", "line": 60, "name": "_UnavailableStrategies", "signature": "class _UnavailableStrategies"}, {"doc": "Identity decorator used when hypothesis is unavailable.", "kind": "method", "line": 69, "name": "given", "signature": "def given()"}, {"doc": "Identity decorator used when hypothesis is unavailable.", "kind": "method", "line": 75, "name": "settings", "signature": "def settings()"}, {"doc": "Combine placeholders without evaluating strategies.", "kind": "method", "line": 48, "name": "__or__", "signature": "def __or__(self, other)"}, {"doc": "Combine placeholders without evaluating strategies.", "kind": "method", "line": 52, "name": "__ror__", "signature": "def __ror__(self, other)"}, {"doc": "Return the placeholder unchanged.", "kind": "method", "line": 56, "name": "map", "signature": "def map(self)"}, {"doc": "Return a builder producing inert placeholders.", "kind": "method", "line": 63, "name": "__getattr__", "signature": "def __getattr__(self, name)"}, {"kind": "method", "line": 71, "name": "wrapper", "signature": "def wrapper(fn)"}, {"kind": "method", "line": 77, "name": "wrapper", "signature": "def wrapper(fn)"}, {"kind": "method", "line": 65, "name": "builder", "signature": "def builder()"}]}, {"id": "tests/test_query.py", "kind": "module", "label": "test_query.py", "language": "py", "sha256": "9065822de432127b", "symbol_count": 18, "symbols": [{"kind": "function", "line": 7, "name": "_make_node", "signature": "def _make_node(node_id, symbols)"}, {"kind": "function", "line": 18, "name": "_make_sym", "signature": "def _make_sym(name, kind, line)"}, {"kind": "class", "line": 22, "name": "TestQueryEngineContract", "signature": "class TestQueryEngineContract(TestCase)"}, {"kind": "method", "line": 23, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 36, "name": "test_find_exact_symbol", "signature": "def test_find_exact_symbol(self)"}, {"kind": "method", "line": 42, "name": "test_find_symbol_fuzzy", "signature": "def test_find_symbol_fuzzy(self)"}, {"kind": "method", "line": 47, "name": "test_find_symbol_not_found", "signature": "def test_find_symbol_not_found(self)"}, {"kind": "method", "line": 51, "name": "test_explain_returns_details", "signature": "def test_explain_returns_details(self)"}, {"kind": "method", "line": 58, "name": "test_explain_shows_imports", "signature": "def test_explain_shows_imports(self)"}, {"kind": "method", "line": 63, "name": "test_explain_shows_siblings", "signature": "def test_explain_shows_siblings(self)"}, {"kind": "method", "line": 69, "name": "test_explain_unknown_returns_none", "signature": "def test_explain_unknown_returns_none(self)"}, {"kind": "method", "line": 73, "name": "test_find_path_direct_import", "signature": "def test_find_path_direct_import(self)"}, {"kind": "method", "line": 79, "name": "test_find_path_same_file", "signature": "def test_find_path_same_file(self)"}, {"kind": "method", "line": 84, "name": "test_find_path_unknown_returns_none", "signature": "def test_find_path_unknown_returns_none(self)"}, {"kind": "method", "line": 88, "name": "test_summary_shows_counts", "signature": "def test_summary_shows_counts(self)"}, {"kind": "method", "line": 94, "name": "test_summary_shows_top_modules", "signature": "def test_summary_shows_top_modules(self)"}, {"kind": "method", "line": 98, "name": "test_query_returns_matching_symbols", "signature": "def test_query_returns_matching_symbols(self)"}, {"kind": "method", "line": 102, "name": "test_query_returns_file_matches", "signature": "def test_query_returns_file_matches(self)"}]}, {"doc": "Contract tests for the category theory and ranking system.  Tests cover: - EdgeKind enum contract - Morphism weight computation - Category composition and path finding - TypedGraph stochastic matrix construction - Global PageRank invariants (sum=1, convergence, stability) - Personalized PageRank seed sensitivity - HITS authority/hub separation - Composite scoring formula - Seed generation from queries - Noise penalty for hub names - Projection functors and views - Score explanation formatting", "id": "tests/test_ranking.py", "kind": "module", "label": "test_ranking.py", "language": "py", "sha256": "3b50ba6e273cbac1", "symbol_count": 72, "symbols": [{"kind": "class", "line": 60, "name": "TestEdgeKind", "signature": "class TestEdgeKind"}, {"kind": "class", "line": 84, "name": "TestMorphism", "signature": "class TestMorphism"}, {"kind": "class", "line": 104, "name": "TestCategory", "signature": "class TestCategory"}, {"kind": "class", "line": 183, "name": "TestTypedGraph", "signature": "class TestTypedGraph"}, {"kind": "method", "line": 238, "name": "_make_test_graph", "signature": "def _make_test_graph()"}, {"kind": "class", "line": 247, "name": "TestGlobalPageRank", "signature": "class TestGlobalPageRank"}, {"kind": "class", "line": 288, "name": "TestPersonalizedPageRank", "signature": "class TestPersonalizedPageRank"}, {"kind": "class", "line": 325, "name": "TestHITS", "signature": "class TestHITS"}, {"kind": "class", "line": 350, "name": "TestSeedGeneration", "signature": "class TestSeedGeneration"}, {"kind": "class", "line": 403, "name": "TestCompositeRanker", "signature": "class TestCompositeRanker"}, {"kind": "class", "line": 490, "name": "TestProjections", "signature": "class TestProjections"}, {"kind": "class", "line": 539, "name": "TestExplain", "signature": "class TestExplain"}, {"kind": "class", "line": 587, "name": "TestIntegration", "signature": "class TestIntegration"}, {"kind": "method", "line": 61, "name": "test_all_edge_kinds_have_weights", "signature": "def test_all_edge_kinds_have_weights(self)"}, {"kind": "method", "line": 66, "name": "test_infer_edge_kind_maps_correctly", "signature": "def test_infer_edge_kind_maps_correctly(self)"}, {"kind": "method", "line": 71, "name": "test_infer_edge_kind_falls_back", "signature": "def test_infer_edge_kind_falls_back(self)"}, {"kind": "method", "line": 75, "name": "test_edge_kind_is_str_enum", "signature": "def test_edge_kind_is_str_enum(self)"}, {"kind": "method", "line": 85, "name": "test_weight_is_edge_weight_times_confidence", "signature": "def test_weight_is_edge_weight_times_confidence(self)"}, {"kind": "method", "line": 90, "name": "test_weight_default_confidence", "signature": "def test_weight_default_confidence(self)"}, {"kind": "method", "line": 94, "name": "test_morphism_is_frozen", "signature": "def test_morphism_is_frozen(self)"}, {"kind": "method", "line": 105, "name": "test_empty_category", "signature": "def test_empty_category(self)"}, {"kind": "method", "line": 110, "name": "test_add_object_and_morphism", "signature": "def test_add_object_and_morphism(self)"}, {"kind": "method", "line": 118, "name": "test_outgoing_and_incoming", "signature": "def test_outgoing_and_incoming(self)"}, {"kind": "method", "line": 130, "name": "test_compose_same_kind", "signature": "def test_compose_same_kind(self)"}, {"kind": "method", "line": 140, "name": "test_compose_imports_then_defines", "signature": "def test_compose_imports_then_defines(self)"}, {"kind": "method", "line": 148, "name": "test_compose_incompatible_returns_none", "signature": "def test_compose_incompatible_returns_none(self)"}, {"kind": "method", "line": 155, "name": "test_compose_mismatched_target_source", "signature": "def test_compose_mismatched_target_source(self)"}, {"kind": "method", "line": 162, "name": "test_paths_finds_composition_chains", "signature": "def test_paths_finds_composition_chains(self)"}, {"kind": "method", "line": 171, "name": "test_paths_empty_when_no_route", "signature": "def test_paths_empty_when_no_route(self)"}, {"kind": "method", "line": 184, "name": "test_empty_graph", "signature": "def test_empty_graph(self)"}, {"kind": "method", "line": 190, "name": "test_stochastic_row_normalizes_to_one", "signature": "def test_stochastic_row_normalizes_to_one(self)"}, {"kind": "method", "line": 199, "name": "test_stochastic_row_empty_for_dangling", "signature": "def test_stochastic_row_empty_for_dangling(self)"}, {"kind": "method", "line": 205, "name": "test_transition_weight_aggregates_parallel_edges", "signature": "def test_transition_weight_aggregates_parallel_edges(self)"}, {"kind": "method", "line": 214, "name": "test_build_category_from_edges", "signature": "def test_build_category_from_edges(self)"}, {"kind": "method", "line": 225, "name": "test_build_category_from_edges_filters_by_node_ids", "signature": "def test_build_category_from_edges_filters_by_node_ids(self)"}, {"kind": "method", "line": 248, "name": "test_scores_sum_to_one", "signature": "def test_scores_sum_to_one(self)"}, {"kind": "method", "line": 254, "name": "test_all_nodes_have_positive_score", "signature": "def test_all_nodes_have_positive_score(self)"}, {"kind": "method", "line": 260, "name": "test_converges_within_max_iter", "signature": "def test_converges_within_max_iter(self)"}, {"kind": "method", "line": 266, "name": "test_stable_across_calls", "signature": "def test_stable_across_calls(self)"}, {"kind": "method", "line": 273, "name": "test_dangling_node_handled", "signature": "def test_dangling_node_handled(self)"}, {"kind": "method", "line": 284, "name": "test_empty_graph", "signature": "def test_empty_graph(self)"}, {"kind": "method", "line": 289, "name": "test_seed_node_gets_highest_score", "signature": "def test_seed_node_gets_highest_score(self)"}, {"kind": "method", "line": 296, "name": "test_scores_sum_to_one", "signature": "def test_scores_sum_to_one(self)"}, {"kind": "method", "line": 303, "name": "test_different_seeds_produce_different_rankings", "signature": "def test_different_seeds_produce_different_rankings(self)"}, {"kind": "method", "line": 310, "name": "test_empty_seeds_uses_uniform", "signature": "def test_empty_seeds_uses_uniform(self)"}, {"kind": "method", "line": 317, "name": "test_multi_seed", "signature": "def test_multi_seed(self)"}, {"kind": "method", "line": 326, "name": "test_authorities_and_hubs_have_positive_scores", "signature": "def test_authorities_and_hubs_have_positive_scores(self)"}, {"kind": "method", "line": 333, "name": "test_authorities_l2_normalized", "signature": "def test_authorities_l2_normalized(self)"}, {"kind": "method", "line": 339, "name": "test_hubs_l2_normalized", "signature": "def test_hubs_l2_normalized(self)"}, {"kind": "method", "line": 351, "name": "test_build_seeds_from_query_matches_node_id", "signature": "def test_build_seeds_from_query_matches_node_id(self)"}, {"kind": "method", "line": 363, "name": "test_build_seeds_from_query_matches_symbol", "signature": "def test_build_seeds_from_query_matches_symbol(self)"}, {"kind": "method", "line": 374, "name": "test_build_seeds_from_query_no_match_returns_empty", "signature": "def test_build_seeds_from_query_no_match_returns_empty(self)"}, {"kind": "method", "line": 383, "name": "test_build_seeds_for_context", "signature": "def test_build_seeds_for_context(self)"}, {"kind": "method", "line": 392, "name": "test_build_seeds_for_context_no_match", "signature": "def test_build_seeds_for_context_no_match(self)"}, {"kind": "method", "line": 404, "name": "test_rank_returns_sorted_results", "signature": "def test_rank_returns_sorted_results(self)"}, {"kind": "method", "line": 421, "name": "test_rank_items_have_all_score_fields", "signature": "def test_rank_items_have_all_score_fields(self)"}, {"kind": "method", "line": 447, "name": "test_noise_penalty_applied", "signature": "def test_noise_penalty_applied(self)"}, {"kind": "method", "line": 466, "name": "test_top_n", "signature": "def test_top_n(self)"}, {"kind": "method", "line": 479, "name": "test_explain_returns_none_for_missing", "signature": "def test_explain_returns_none_for_missing(self)"}, {"kind": "method", "line": 491, "name": "test_identity_projection_passes_all", "signature": "def test_identity_projection_passes_all(self)"}, {"kind": "method", "line": 498, "name": "test_doc_projection_filters_undocumented", "signature": "def test_doc_projection_filters_undocumented(self)"}, {"kind": "method", "line": 506, "name": "test_doc_projection_filters_morphism_kind", "signature": "def test_doc_projection_filters_morphism_kind(self)"}, {"kind": "method", "line": 512, "name": "test_apply_view_architecture", "signature": "def test_apply_view_architecture(self)"}, {"kind": "method", "line": 521, "name": "test_apply_view_reverse", "signature": "def test_apply_view_reverse(self)"}, {"kind": "method", "line": 528, "name": "test_apply_view_empty", "signature": "def test_apply_view_empty(self)"}, {"kind": "method", "line": 540, "name": "test_explain_rank_found", "signature": "def test_explain_rank_found(self)"}, {"kind": "method", "line": 559, "name": "test_explain_rank_not_found", "signature": "def test_explain_rank_not_found(self)"}, {"kind": "method", "line": 565, "name": "test_rank_summary_format", "signature": "def test_rank_summary_format(self)"}, {"kind": "method", "line": 588, "name": "test_category_from_real_edges", "signature": "def test_category_from_real_edges(self)"}, {"kind": "method", "line": 613, "name": "test_pagerank_on_real_category", "signature": "def test_pagerank_on_real_category(self)"}, {"kind": "method", "line": 625, "name": "test_ppr_favors_seed", "signature": "def test_ppr_favors_seed(self)"}, {"kind": "method", "line": 637, "name": "test_ranker_from_real_data", "signature": "def test_ranker_from_real_data(self)"}]}, {"doc": "Contract tests for README injection into documented projects.  SDD + TDD + BDD: Each test validates a specific behavioral contract of the ReadmeInjector for injecting/deleting knowledge base links.", "id": "tests/test_readme_injector.py", "kind": "module", "label": "test_readme_injector.py", "language": "py", "sha256": "2eea2e1fb178b422", "symbol_count": 26, "symbols": [{"doc": "BDD: ReadmeInjector injection contract.", "kind": "class", "line": 16, "name": "TestReadmeInjectorInjectBehavior", "signature": "class TestReadmeInjectorInjectBehavior(TestCase)"}, {"doc": "BDD: ReadmeInjector removal contract.", "kind": "class", "line": 72, "name": "TestReadmeInjectorRemoveBehavior", "signature": "class TestReadmeInjectorRemoveBehavior(TestCase)"}, {"doc": "BDD: ReadmeInjector README file detection contract.", "kind": "class", "line": 105, "name": "TestReadmeInjectorFindReadme", "signature": "class TestReadmeInjectorFindReadme(TestCase)"}, {"doc": "BDD: ReadmeInjector edge case contract.", "kind": "class", "line": 140, "name": "TestReadmeInjectorEdgeCases", "signature": "class TestReadmeInjectorEdgeCases(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 24, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 28, "name": "test_inject_into_markdown_readme_adds_kb_link", "signature": "def test_inject_into_markdown_readme_adds_kb_link(self)"}, {"kind": "method", "line": 39, "name": "test_inject_into_rst_readme_adds_kb_link", "signature": "def test_inject_into_rst_readme_adds_kb_link(self)"}, {"kind": "method", "line": 48, "name": "test_inject_is_idempotent_does_not_duplicate", "signature": "def test_inject_is_idempotent_does_not_duplicate(self)"}, {"kind": "method", "line": 59, "name": "test_inject_no_readme_file_returns_false", "signature": "def test_inject_no_readme_file_returns_false(self)"}, {"kind": "method", "line": 63, "name": "test_inject_preserves_existing_content", "signature": "def test_inject_preserves_existing_content(self)"}, {"kind": "method", "line": 75, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 80, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 84, "name": "test_remove_strips_injected_section", "signature": "def test_remove_strips_injected_section(self)"}, {"kind": "method", "line": 94, "name": "test_remove_without_injection_returns_false", "signature": "def test_remove_without_injection_returns_false(self)"}, {"kind": "method", "line": 100, "name": "test_remove_no_readme_returns_false", "signature": "def test_remove_no_readme_returns_false(self)"}, {"kind": "method", "line": 108, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 112, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 116, "name": "test_finds_readme_md", "signature": "def test_finds_readme_md(self)"}, {"kind": "method", "line": 122, "name": "test_finds_readme_rst", "signature": "def test_finds_readme_rst(self)"}, {"kind": "method", "line": 128, "name": "test_prefers_readme_md_over_rst", "signature": "def test_prefers_readme_md_over_rst(self)"}, {"kind": "method", "line": 135, "name": "test_returns_none_when_no_readme", "signature": "def test_returns_none_when_no_readme(self)"}, {"kind": "method", "line": 143, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 148, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 152, "name": "test_inject_into_empty_readme", "signature": "def test_inject_into_empty_readme(self)"}, {"kind": "method", "line": 160, "name": "test_custom_kb_filename_works", "signature": "def test_custom_kb_filename_works(self)"}]}, {"doc": "Contract tests for the MonolithRefactorizer.  Validates monolithic file detection, refactoring plan generation, symbol grouping, target file suggestion, and script generation.", "id": "tests/test_refactorizer.py", "kind": "module", "label": "test_refactorizer.py", "language": "py", "sha256": "e6cf2a22e1c89a39", "symbol_count": 17, "symbols": [{"doc": "Contract: MonolithRefactorizer generates refactoring plans.", "kind": "class", "line": 18, "name": "TestMonolithRefactorizerContract", "signature": "class TestMonolithRefactorizerContract(TestCase)"}, {"kind": "method", "line": 21, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 25, "name": "_make_symbol", "signature": "def _make_symbol(self, name, kind, line)"}, {"kind": "method", "line": 28, "name": "_make_node", "signature": "def _make_node(self, nid, symbols)"}, {"kind": "method", "line": 37, "name": "_make_edge", "signature": "def _make_edge(self, src, tgt)"}, {"kind": "method", "line": 40, "name": "test_analyze_empty_graph_returns_empty", "signature": "def test_analyze_empty_graph_returns_empty(self)"}, {"kind": "method", "line": 44, "name": "test_analyze_ignores_small_files", "signature": "def test_analyze_ignores_small_files(self)"}, {"kind": "method", "line": 50, "name": "test_analyze_detects_large_file", "signature": "def test_analyze_detects_large_file(self)"}, {"kind": "method", "line": 59, "name": "test_analyze_generates_extract_class_for_multiple_classes", "signature": "def test_analyze_generates_extract_class_for_multiple_classes(self)"}, {"kind": "method", "line": 74, "name": "test_analyze_generates_extract_function_for_multiple_functions", "signature": "def test_analyze_generates_extract_function_for_multiple_functions(self)"}, {"kind": "method", "line": 89, "name": "test_analyze_splits_file_with_many_symbols", "signature": "def test_analyze_splits_file_with_many_symbols(self)"}, {"kind": "method", "line": 97, "name": "test_analyze_estimates_impact_from_resolved_edges", "signature": "def test_analyze_estimates_impact_from_resolved_edges(self)"}, {"kind": "method", "line": 109, "name": "test_generate_script_contains_shebang", "signature": "def test_generate_script_contains_shebang(self)"}, {"kind": "method", "line": 129, "name": "test_generate_script_contains_set_e", "signature": "def test_generate_script_contains_set_e(self)"}, {"kind": "method", "line": 140, "name": "test_generate_script_contains_sed_commands", "signature": "def test_generate_script_contains_sed_commands(self)"}, {"kind": "method", "line": 160, "name": "test_analyze_sorted_by_line_count", "signature": "def test_analyze_sorted_by_line_count(self)"}, {"kind": "method", "line": 173, "name": "test_analyze_respects_max_files_limit", "signature": "def test_analyze_respects_max_files_limit(self)"}]}, {"doc": "Contract tests for the ImportResolver.  Validates that import strings from various languages are correctly resolved to project file paths, handles edge cases like relative imports, dotted modules, and extensionless imports.", "id": "tests/test_resolver.py", "kind": "module", "label": "test_resolver.py", "language": "py", "sha256": "b2581f4f753e37ca", "symbol_count": 22, "symbols": [{"doc": "Contract: ImportResolver maps import strings to file paths.", "kind": "class", "line": 15, "name": "TestImportResolverContract", "signature": "class TestImportResolverContract(TestCase)"}, {"kind": "method", "line": 18, "name": "test_resolves_python_module_dotpath", "signature": "def test_resolves_python_module_dotpath(self)"}, {"kind": "method", "line": 25, "name": "test_resolves_relative_import", "signature": "def test_resolves_relative_import(self)"}, {"kind": "method", "line": 32, "name": "test_resolves_extensionless_python_import", "signature": "def test_resolves_extensionless_python_import(self)"}, {"kind": "method", "line": 39, "name": "test_resolves_package_init", "signature": "def test_resolves_package_init(self)"}, {"kind": "method", "line": 46, "name": "test_returns_none_for_external_stdlib", "signature": "def test_returns_none_for_external_stdlib(self)"}, {"kind": "method", "line": 53, "name": "test_returns_none_for_unknown_import", "signature": "def test_returns_none_for_unknown_import(self)"}, {"kind": "method", "line": 60, "name": "test_resolves_stem_match_when_unique", "signature": "def test_resolves_stem_match_when_unique(self)"}, {"kind": "method", "line": 67, "name": "test_returns_none_for_empty_import", "signature": "def test_returns_none_for_empty_import(self)"}, {"kind": "method", "line": 72, "name": "test_resolves_go_import", "signature": "def test_resolves_go_import(self)"}, {"kind": "method", "line": 79, "name": "test_resolves_same_directory_import", "signature": "def test_resolves_same_directory_import(self)"}, {"kind": "method", "line": 86, "name": "test_resolves_c_quoted_header_same_dir", "signature": "def test_resolves_c_quoted_header_same_dir(self)"}, {"kind": "method", "line": 93, "name": "test_resolves_c_quoted_header_subdir", "signature": "def test_resolves_c_quoted_header_subdir(self)"}, {"kind": "method", "line": 100, "name": "test_resolves_c_extensionless_header", "signature": "def test_resolves_c_extensionless_header(self)"}, {"kind": "method", "line": 107, "name": "test_resolves_c_source_from_header_dir", "signature": "def test_resolves_c_source_from_header_dir(self)"}, {"kind": "method", "line": 114, "name": "test_resolves_cpp_header_same_dir", "signature": "def test_resolves_cpp_header_same_dir(self)"}, {"kind": "method", "line": 121, "name": "test_resolves_c_header_stem_across_dirs", "signature": "def test_resolves_c_header_stem_across_dirs(self)"}, {"kind": "method", "line": 128, "name": "test_returns_none_for_c_system_header", "signature": "def test_returns_none_for_c_system_header(self)"}, {"kind": "method", "line": 135, "name": "test_resolves_parent_dir_include", "signature": "def test_resolves_parent_dir_include(self)"}, {"kind": "method", "line": 142, "name": "test_resolves_parent_dir_include_despite_ambiguous_stem", "signature": "def test_resolves_parent_dir_include_despite_ambiguous_stem(self)"}, {"kind": "method", "line": 149, "name": "test_resolves_include_dir_suffix_match", "signature": "def test_resolves_include_dir_suffix_match(self)"}, {"kind": "method", "line": 156, "name": "test_returns_none_for_ambiguous_suffix_match", "signature": "def test_returns_none_for_ambiguous_suffix_match(self)"}]}, {"id": "tests/test_rule_gen.py", "kind": "module", "label": "test_rule_gen.py", "language": "py", "sha256": "fe6c1fc2b2c56a51", "symbol_count": 10, "symbols": [{"doc": "Contract: RuleGenerator detects patterns and suggests rules.", "kind": "class", "line": 12, "name": "TestRuleGeneratorContract", "signature": "class TestRuleGeneratorContract(TestCase)"}, {"kind": "method", "line": 15, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 19, "name": "_make_node", "signature": "def _make_node(self, nid, label, lang)"}, {"kind": "method", "line": 29, "name": "_make_node_with_symbols", "signature": "def _make_node_with_symbols(self, nid, sym_count)"}, {"kind": "method", "line": 44, "name": "test_empty_nodes_returns_empty_rules", "signature": "def test_empty_nodes_returns_empty_rules(self)"}, {"kind": "method", "line": 48, "name": "test_generates_rules_for_function_heavy_language", "signature": "def test_generates_rules_for_function_heavy_language(self)"}, {"kind": "method", "line": 56, "name": "test_detects_antipatterns_with_content", "signature": "def test_detects_antipatterns_with_content(self)"}, {"kind": "method", "line": 67, "name": "test_antipattern_threshold_from_config", "signature": "def test_antipattern_threshold_from_config(self)"}, {"kind": "method", "line": 77, "name": "test_write_rules_creates_files", "signature": "def test_write_rules_creates_files(self)"}, {"kind": "method", "line": 90, "name": "test_rule_id_increments", "signature": "def test_rule_id_increments(self)"}]}, {"id": "tests/test_sarif.py", "kind": "module", "label": "test_sarif.py", "language": "py", "sha256": "6522296ceb83662c", "symbol_count": 10, "symbols": [{"doc": "Contract: SarifExporter produces valid SARIF v2.1.0 JSON.", "kind": "class", "line": 11, "name": "TestSarifExporterContract", "signature": "class TestSarifExporterContract(TestCase)"}, {"kind": "method", "line": 14, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 18, "name": "_make_finding", "signature": "def _make_finding(self, file_path, line, severity, rule_id, description, snippet, cwe)"}, {"kind": "method", "line": 38, "name": "test_export_returns_valid_json", "signature": "def test_export_returns_valid_json(self)"}, {"kind": "method", "line": 46, "name": "test_export_includes_tool_info", "signature": "def test_export_includes_tool_info(self)"}, {"kind": "method", "line": 54, "name": "test_export_includes_rule", "signature": "def test_export_includes_rule(self)"}, {"kind": "method", "line": 62, "name": "test_export_includes_result", "signature": "def test_export_includes_result(self)"}, {"kind": "method", "line": 73, "name": "test_severity_maps_correctly", "signature": "def test_severity_maps_correctly(self)"}, {"kind": "method", "line": 88, "name": "test_privacy_mode_strips_snippets", "signature": "def test_privacy_mode_strips_snippets(self)"}, {"kind": "method", "line": 97, "name": "test_empty_findings_produces_valid_sarif", "signature": "def test_empty_findings_produces_valid_sarif(self)"}]}, {"id": "tests/test_scanner.py", "kind": "module", "label": "test_scanner.py", "language": "py", "sha256": "f28efb00e2f48f41", "symbol_count": 21, "symbols": [{"kind": "class", "line": 11, "name": "TestScannerContract", "signature": "class TestScannerContract(TestCase)"}, {"kind": "method", "line": 12, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 16, "name": "tearDown", "signature": "def tearDown(self)"}, {"kind": "method", "line": 20, "name": "_write", "signature": "def _write(self, path, content)"}, {"kind": "method", "line": 25, "name": "test_scans_python_files", "signature": "def test_scans_python_files(self)"}, {"kind": "method", "line": 32, "name": "test_ignores_env_and_vendor_dirs", "signature": "def test_ignores_env_and_vendor_dirs(self)"}, {"kind": "method", "line": 45, "name": "test_rejects_symlinks", "signature": "def test_rejects_symlinks(self)"}, {"kind": "method", "line": 59, "name": "test_skips_non_code_files", "signature": "def test_skips_non_code_files(self)"}, {"kind": "method", "line": 70, "name": "test_scans_multiple_languages", "signature": "def test_scans_multiple_languages(self)"}, {"kind": "method", "line": 79, "name": "test_respects_max_directory_depth", "signature": "def test_respects_max_directory_depth(self)"}, {"kind": "method", "line": 89, "name": "test_raises_on_invalid_directory", "signature": "def test_raises_on_invalid_directory(self)"}, {"kind": "method", "line": 94, "name": "test_import_edges_are_created", "signature": "def test_import_edges_are_created(self)"}, {"kind": "method", "line": 104, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 114, "name": "test_module_docstring_extracted_as_file_doc", "signature": "def test_module_docstring_extracted_as_file_doc(self)"}, {"kind": "method", "line": 121, "name": "test_multiline_module_docstring_extracted", "signature": "def test_multiline_module_docstring_extracted(self)"}, {"kind": "method", "line": 129, "name": "test_coding_cookie_ignored_as_file_doc", "signature": "def test_coding_cookie_ignored_as_file_doc(self)"}, {"kind": "method", "line": 136, "name": "test_preprocessor_guards_ignored_as_file_doc", "signature": "def test_preprocessor_guards_ignored_as_file_doc(self)"}, {"kind": "method", "line": 143, "name": "test_scan_with_content_returns_content_map", "signature": "def test_scan_with_content_returns_content_map(self)"}, {"kind": "method", "line": 151, "name": "test_gitignore_respected_when_enabled", "signature": "def test_gitignore_respected_when_enabled(self)"}, {"kind": "method", "line": 162, "name": "test_gitignore_disabled_by_default", "signature": "def test_gitignore_disabled_by_default(self)"}, {"kind": "method", "line": 171, "name": "test_gitignore_glob_conversion", "signature": "def test_gitignore_glob_conversion(self)"}]}, {"doc": "Contract tests for the static security analysis module.  Tests cover the SecurityFinding data model, per-language rule detection, severity threshold filtering, path validation, and end-to-end scanning of dangerous patterns across all supported languages.", "id": "tests/test_security.py", "kind": "module", "label": "test_security.py", "language": "py", "sha256": "26fcb14104b92d9d", "symbol_count": 68, "symbols": [{"doc": "SecurityFinding dataclass contract tests.", "kind": "class", "line": 21, "name": "TestSecurityFinding", "signature": "class TestSecurityFinding(TestCase)"}, {"doc": "SecurityAnalyzer configuration contract tests.", "kind": "class", "line": 43, "name": "TestSecurityAnalyzerConfig", "signature": "class TestSecurityAnalyzerConfig(TestCase)"}, {"doc": "Per-language rule detection tests using inline code.", "kind": "class", "line": 64, "name": "TestSecurityAnalyzerRules", "signature": "class TestSecurityAnalyzerRules(TestCase)"}, {"doc": "Severity threshold filtering tests.", "kind": "class", "line": 295, "name": "TestSecurityAnalyzerThreshold", "signature": "class TestSecurityAnalyzerThreshold(TestCase)"}, {"doc": "Security path validation tests.", "kind": "class", "line": 327, "name": "TestSecurityAnalyzerPathValidation", "signature": "class TestSecurityAnalyzerPathValidation(TestCase)"}, {"doc": "Security summary output tests.", "kind": "class", "line": 374, "name": "TestSecurityAnalyzerSummary", "signature": "class TestSecurityAnalyzerSummary(TestCase)"}, {"doc": "fix_hint_for remediation hint contract tests.", "kind": "class", "line": 396, "name": "TestFixGuidance", "signature": "class TestFixGuidance(TestCase)"}, {"kind": "method", "line": 24, "name": "test_security_finding_fields", "signature": "def test_security_finding_fields(self)"}, {"kind": "method", "line": 46, "name": "test_default_config_disables_security", "signature": "def test_default_config_disables_security(self)"}, {"kind": "method", "line": 50, "name": "test_default_severity_threshold", "signature": "def test_default_severity_threshold(self)"}, {"kind": "method", "line": 54, "name": "test_default_security_output", "signature": "def test_default_security_output(self)"}, {"kind": "method", "line": 58, "name": "test_init_with_config", "signature": "def test_init_with_config(self)"}, {"kind": "method", "line": 67, "name": "setUp", "signature": "def setUp(self)"}, {"doc": "Write content to a temp file and scan it.", "kind": "method", "line": 71, "name": "_scan_content", "signature": "def _scan_content(self, content, extension)"}, {"kind": "method", "line": 78, "name": "test_python_os_system", "signature": "def test_python_os_system(self)"}, {"kind": "method", "line": 83, "name": "test_python_eval", "signature": "def test_python_eval(self)"}, {"kind": "method", "line": 88, "name": "test_python_pickle", "signature": "def test_python_pickle(self)"}, {"kind": "method", "line": 93, "name": "test_python_sql_injection", "signature": "def test_python_sql_injection(self)"}, {"kind": "method", "line": 98, "name": "test_python_hardcoded_secret", "signature": "def test_python_hardcoded_secret(self)"}, {"kind": "method", "line": 103, "name": "test_python_weak_crypto", "signature": "def test_python_weak_crypto(self)"}, {"kind": "method", "line": 108, "name": "test_python_request_verify_false", "signature": "def test_python_request_verify_false(self)"}, {"kind": "method", "line": 113, "name": "test_python_flask_debug", "signature": "def test_python_flask_debug(self)"}, {"kind": "method", "line": 118, "name": "test_python_yaml_load", "signature": "def test_python_yaml_load(self)"}, {"kind": "method", "line": 123, "name": "test_javascript_inner_html", "signature": "def test_javascript_inner_html(self)"}, {"kind": "method", "line": 128, "name": "test_javascript_eval", "signature": "def test_javascript_eval(self)"}, {"kind": "method", "line": 133, "name": "test_javascript_child_process", "signature": "def test_javascript_child_process(self)"}, {"kind": "method", "line": 138, "name": "test_javascript_dangerously_set_inner_html", "signature": "def test_javascript_dangerously_set_inner_html(self)"}, {"kind": "method", "line": 143, "name": "test_c_strcpy", "signature": "def test_c_strcpy(self)"}, {"kind": "method", "line": 148, "name": "test_c_gets", "signature": "def test_c_gets(self)"}, {"kind": "method", "line": 153, "name": "test_c_system", "signature": "def test_c_system(self)"}, {"kind": "method", "line": 158, "name": "test_java_runtime_exec", "signature": "def test_java_runtime_exec(self)"}, {"kind": "method", "line": 163, "name": "test_java_sql_injection", "signature": "def test_java_sql_injection(self)"}, {"kind": "method", "line": 168, "name": "test_go_exec_command", "signature": "def test_go_exec_command(self)"}, {"kind": "method", "line": 173, "name": "test_ruby_eval", "signature": "def test_ruby_eval(self)"}, {"kind": "method", "line": 178, "name": "test_ruby_marshal_load", "signature": "def test_ruby_marshal_load(self)"}, {"kind": "method", "line": 183, "name": "test_php_eval", "signature": "def test_php_eval(self)"}, {"kind": "method", "line": 188, "name": "test_php_sql_injection", "signature": "def test_php_sql_injection(self)"}, {"kind": "method", "line": 193, "name": "test_php_unseralize", "signature": "def test_php_unseralize(self)"}, {"kind": "method", "line": 198, "name": "test_shell_eval", "signature": "def test_shell_eval(self)"}, {"kind": "method", "line": 203, "name": "test_csharp_process_start", "signature": "def test_csharp_process_start(self)"}, {"kind": "method", "line": 208, "name": "test_kotlin_runtime_exec", "signature": "def test_kotlin_runtime_exec(self)"}, {"kind": "method", "line": 213, "name": "test_swift_process", "signature": "def test_swift_process(self)"}, {"kind": "method", "line": 218, "name": "test_lua_load", "signature": "def test_lua_load(self)"}, {"kind": "method", "line": 223, "name": "test_lua_os_execute", "signature": "def test_lua_os_execute(self)"}, {"kind": "method", "line": 228, "name": "test_dart_process_run", "signature": "def test_dart_process_run(self)"}, {"kind": "method", "line": 233, "name": "test_rust_unsafe", "signature": "def test_rust_unsafe(self)"}, {"kind": "method", "line": 238, "name": "test_elixir_code_eval", "signature": "def test_elixir_code_eval(self)"}, {"kind": "method", "line": 243, "name": "test_elixir_system_cmd", "signature": "def test_elixir_system_cmd(self)"}, {"kind": "method", "line": 248, "name": "test_gdscript_os_execute", "signature": "def test_gdscript_os_execute(self)"}, {"kind": "method", "line": 253, "name": "test_scala_runtime_exec", "signature": "def test_scala_runtime_exec(self)"}, {"kind": "method", "line": 258, "name": "test_nim_exec_process", "signature": "def test_nim_exec_process(self)"}, {"kind": "method", "line": 263, "name": "test_safe_code_produces_no_findings", "signature": "def test_safe_code_produces_no_findings(self)"}, {"kind": "method", "line": 274, "name": "test_csharp_binary_formatter", "signature": "def test_csharp_binary_formatter(self)"}, {"kind": "method", "line": 279, "name": "test_ruby_backtick", "signature": "def test_ruby_backtick(self)"}, {"kind": "method", "line": 284, "name": "test_php_xss", "signature": "def test_php_xss(self)"}, {"kind": "method", "line": 289, "name": "test_go_unsafe_package", "signature": "def test_go_unsafe_package(self)"}, {"kind": "method", "line": 298, "name": "test_threshold_filters_low", "signature": "def test_threshold_filters_low(self)"}, {"kind": "method", "line": 312, "name": "test_threshold_info_shows_all", "signature": "def test_threshold_info_shows_all(self)"}, {"kind": "method", "line": 330, "name": "test_ignores_symlinks", "signature": "def test_ignores_symlinks(self)"}, {"kind": "method", "line": 345, "name": "test_ignores_ignored_dirs", "signature": "def test_ignores_ignored_dirs(self)"}, {"kind": "method", "line": 357, "name": "test_empty_directory", "signature": "def test_empty_directory(self)"}, {"kind": "method", "line": 364, "name": "test_unsupported_extension", "signature": "def test_unsupported_extension(self)"}, {"kind": "method", "line": 377, "name": "test_summary_empty", "signature": "def test_summary_empty(self)"}, {"kind": "method", "line": 383, "name": "test_summary_with_findings", "signature": "def test_summary_with_findings(self)"}, {"kind": "method", "line": 399, "name": "_finding", "signature": "def _finding(self, cwe)"}, {"kind": "method", "line": 402, "name": "test_known_cwe_returns_actionable_hint", "signature": "def test_known_cwe_returns_actionable_hint(self)"}, {"kind": "method", "line": 408, "name": "test_unknown_cwe_falls_back", "signature": "def test_unknown_cwe_falls_back(self)"}, {"kind": "method", "line": 413, "name": "test_empty_cwe_falls_back", "signature": "def test_empty_cwe_falls_back(self)"}]}, {"id": "tests/test_taint.py", "kind": "module", "label": "test_taint.py", "language": "py", "sha256": "d196fca30ed7d086", "symbol_count": 10, "symbols": [{"doc": "Contract: TaintAnalyzer discovers taint propagation paths.", "kind": "class", "line": 10, "name": "TestTaintAnalyzerContract", "signature": "class TestTaintAnalyzerContract(TestCase)"}, {"kind": "method", "line": 13, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 17, "name": "_make_node", "signature": "def _make_node(self, nid, label)"}, {"kind": "method", "line": 20, "name": "test_empty_graph_returns_empty_result", "signature": "def test_empty_graph_returns_empty_result(self)"}, {"kind": "method", "line": 25, "name": "test_no_dangerous_imports_returns_empty", "signature": "def test_no_dangerous_imports_returns_empty(self)"}, {"kind": "method", "line": 31, "name": "test_direct_dangerous_import_found", "signature": "def test_direct_dangerous_import_found(self)"}, {"kind": "method", "line": 38, "name": "test_taint_propagates_through_resolved_edges", "signature": "def test_taint_propagates_through_resolved_edges(self)"}, {"kind": "method", "line": 62, "name": "test_dangerous_import_by_language", "signature": "def test_dangerous_import_by_language(self)"}, {"kind": "method", "line": 70, "name": "test_taint_path_has_severity", "signature": "def test_taint_path_has_severity(self)"}, {"kind": "method", "line": 77, "name": "test_max_depth_limits_propagation", "signature": "def test_max_depth_limits_propagation(self)"}]}, {"doc": "BDD-style contract tests for taint propagation analysis.  Uses pytest-bdd scenarios to verify multi-step taint propagation workflows: discovering dangerous imports, propagating through the import graph, and generating complete TaintPath results.  These tests are skipped if pytest-bdd is not installed.", "id": "tests/test_taint_bdd.py", "kind": "module", "label": "test_taint_bdd.py", "language": "py", "sha256": "7d68f72a29549f07", "symbol_count": 26, "symbols": [{"kind": "function", "line": 29, "name": "_build_project_files", "signature": "def _build_project_files(project, root)"}, {"kind": "function", "line": 36, "name": "_scan_project", "signature": "def _scan_project(root, cfg)"}, {"kind": "function", "line": 54, "name": "_run_taint", "signature": "def _run_taint(files, cfg)"}, {"kind": "function", "line": 71, "name": "test_direct_dangerous_import", "signature": "def test_direct_dangerous_import()"}, {"kind": "function", "line": 75, "name": "test_taint_propagates_chain", "signature": "def test_taint_propagates_chain()"}, {"kind": "function", "line": 79, "name": "test_taint_max_depth", "signature": "def test_taint_max_depth()"}, {"kind": "function", "line": 83, "name": "test_cross_language_taint", "signature": "def test_cross_language_taint()"}, {"kind": "function", "line": 87, "name": "test_bdd_skipped", "signature": "def test_bdd_skipped()"}, {"kind": "function", "line": 112, "name": "_bkg", "signature": "def _bkg()"}, {"kind": "function", "line": 117, "name": "_direct_given", "signature": "def _direct_given()"}, {"kind": "function", "line": 121, "name": "_direct_when", "signature": "def _direct_when(_taint_result)"}, {"kind": "function", "line": 125, "name": "_check_has_path", "signature": "def _check_has_path(_taint_result)"}, {"kind": "function", "line": 130, "name": "_check_direct_path", "signature": "def _check_direct_path(_taint_result)"}, {"kind": "function", "line": 135, "name": "_check_src", "signature": "def _check_src(_taint_result)"}, {"kind": "function", "line": 139, "name": "_check_sink", "signature": "def _check_sink(_taint_result)"}, {"kind": "function", "line": 144, "name": "_chain_given", "signature": "def _chain_given()"}, {"kind": "function", "line": 148, "name": "_chain_when", "signature": "def _chain_when(_taint_result)"}, {"kind": "function", "line": 152, "name": "_check_long_path", "signature": "def _check_long_path(_taint_result)"}, {"kind": "function", "line": 159, "name": "_shallow_cfg", "signature": "def _shallow_cfg()"}, {"kind": "function", "line": 163, "name": "_chain_given2", "signature": "def _chain_given2()"}, {"kind": "function", "line": 167, "name": "_run_shallow", "signature": "def _run_shallow(_shallow_cfg)"}, {"kind": "function", "line": 171, "name": "_check_shallow", "signature": "def _check_shallow(_taint_result)"}, {"kind": "function", "line": 178, "name": "_js_given", "signature": "def _js_given()"}, {"kind": "function", "line": 182, "name": "_js_when", "signature": "def _js_when(_taint_result)"}, {"kind": "function", "line": 186, "name": "_check_js_dangerous", "signature": "def _check_js_dangerous(_taint_result)"}, {"kind": "function", "line": 192, "name": "_check_js_source", "signature": "def _check_js_source(_taint_result)"}]}, {"doc": "Contract tests for UML class diagram generation and language code generation.  SDD + TDD + BDD: Each test method validates a specific behavioral contract of the UmlGenerator and its per-language code generators.", "id": "tests/test_uml.py", "kind": "module", "label": "test_uml.py", "language": "py", "sha256": "7988cf8ccdf212bc", "symbol_count": 49, "symbols": [{"doc": "BDD: UmlGenerator mermaid class diagram rendering contract.", "kind": "class", "line": 16, "name": "TestUmlMermaidDiagram", "signature": "class TestUmlMermaidDiagram(TestCase)"}, {"doc": "BDD: UmlGenerator ID sanitization contract.", "kind": "class", "line": 157, "name": "TestUmlSanitizeId", "signature": "class TestUmlSanitizeId(TestCase)"}, {"doc": "BDD: C++ code generation contract.", "kind": "class", "line": 181, "name": "TestUmlCodeGenerationCpp", "signature": "class TestUmlCodeGenerationCpp(TestCase)"}, {"doc": "BDD: Java code generation contract.", "kind": "class", "line": 239, "name": "TestUmlCodeGenerationJava", "signature": "class TestUmlCodeGenerationJava(TestCase)"}, {"doc": "BDD: C# code generation contract.", "kind": "class", "line": 281, "name": "TestUmlCodeGenerationCSharp", "signature": "class TestUmlCodeGenerationCSharp(TestCase)"}, {"doc": "BDD: Go code generation contract.", "kind": "class", "line": 306, "name": "TestUmlCodeGenerationGo", "signature": "class TestUmlCodeGenerationGo(TestCase)"}, {"doc": "BDD: Rust code generation contract.", "kind": "class", "line": 347, "name": "TestUmlCodeGenerationRust", "signature": "class TestUmlCodeGenerationRust(TestCase)"}, {"doc": "BDD: PHP code generation contract.", "kind": "class", "line": 387, "name": "TestUmlCodeGenerationPhp", "signature": "class TestUmlCodeGenerationPhp(TestCase)"}, {"doc": "BDD: Kotlin, Scala, Swift, Dart, Ruby code generation contracts.", "kind": "class", "line": 427, "name": "TestUmlCodeGenerationKotlinScalaSwiftDartRuby", "signature": "class TestUmlCodeGenerationKotlinScalaSwiftDartRuby(TestCase)"}, {"kind": "method", "line": 19, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 23, "name": "test_render_empty_nodes_returns_empty_string", "signature": "def test_render_empty_nodes_returns_empty_string(self)"}, {"kind": "method", "line": 27, "name": "test_render_no_class_symbols_returns_empty_string", "signature": "def test_render_no_class_symbols_returns_empty_string(self)"}, {"kind": "method", "line": 42, "name": "test_render_single_class_produces_mermaid_class_diagram", "signature": "def test_render_single_class_produces_mermaid_class_diagram(self)"}, {"kind": "method", "line": 62, "name": "test_render_multiple_classes_from_different_files", "signature": "def test_render_multiple_classes_from_different_files(self)"}, {"kind": "method", "line": 90, "name": "test_render_with_import_edges_produces_relationships", "signature": "def test_render_with_import_edges_produces_relationships(self)"}, {"kind": "method", "line": 119, "name": "test_render_respects_max_classes_limit", "signature": "def test_render_respects_max_classes_limit(self)"}, {"kind": "method", "line": 137, "name": "test_render_with_structs_interfaces_traits", "signature": "def test_render_with_structs_interfaces_traits(self)"}, {"kind": "method", "line": 160, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 164, "name": "test_sanitize_preserves_alphanumeric", "signature": "def test_sanitize_preserves_alphanumeric(self)"}, {"kind": "method", "line": 168, "name": "test_sanitize_replaces_special_chars", "signature": "def test_sanitize_replaces_special_chars(self)"}, {"kind": "method", "line": 172, "name": "test_sanitize_prefixes_digit_start", "signature": "def test_sanitize_prefixes_digit_start(self)"}, {"kind": "method", "line": 176, "name": "test_sanitize_handles_empty_string", "signature": "def test_sanitize_handles_empty_string(self)"}, {"kind": "method", "line": 184, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 188, "name": "test_generate_cpp_produces_valid_code", "signature": "def test_generate_cpp_produces_valid_code(self)"}, {"kind": "method", "line": 208, "name": "test_generate_cpp_with_empty_classes", "signature": "def test_generate_cpp_with_empty_classes(self)"}, {"kind": "method", "line": 223, "name": "test_generate_cpp_unknown_language_returns_error_message", "signature": "def test_generate_cpp_unknown_language_returns_error_message(self)"}, {"kind": "method", "line": 242, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 246, "name": "test_generate_java_class_produces_valid_code", "signature": "def test_generate_java_class_produces_valid_code(self)"}, {"kind": "method", "line": 265, "name": "test_generate_java_interface_produces_interface", "signature": "def test_generate_java_interface_produces_interface(self)"}, {"kind": "method", "line": 284, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 288, "name": "test_generate_csharp_produces_valid_code", "signature": "def test_generate_csharp_produces_valid_code(self)"}, {"kind": "method", "line": 309, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 313, "name": "test_generate_go_struct_produces_valid_code", "signature": "def test_generate_go_struct_produces_valid_code(self)"}, {"kind": "method", "line": 330, "name": "test_generate_go_interface_produces_valid_code", "signature": "def test_generate_go_interface_produces_valid_code(self)"}, {"kind": "method", "line": 350, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 354, "name": "test_generate_rust_struct_produces_valid_code", "signature": "def test_generate_rust_struct_produces_valid_code(self)"}, {"kind": "method", "line": 370, "name": "test_generate_rust_trait_produces_valid_code", "signature": "def test_generate_rust_trait_produces_valid_code(self)"}, {"kind": "method", "line": 390, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 394, "name": "test_generate_php_class_produces_valid_code", "signature": "def test_generate_php_class_produces_valid_code(self)"}, {"kind": "method", "line": 411, "name": "test_generate_php_interface_produces_valid_code", "signature": "def test_generate_php_interface_produces_valid_code(self)"}, {"kind": "method", "line": 430, "name": "setUp", "signature": "def setUp(self)"}, {"kind": "method", "line": 434, "name": "_make_class_node", "signature": "def _make_class_node(self, name, lang, kind)"}, {"kind": "method", "line": 446, "name": "test_generate_kotlin_produces_valid_code", "signature": "def test_generate_kotlin_produces_valid_code(self)"}, {"kind": "method", "line": 452, "name": "test_generate_scala_produces_valid_code", "signature": "def test_generate_scala_produces_valid_code(self)"}, {"kind": "method", "line": 458, "name": "test_generate_scala_trait_produces_valid_code", "signature": "def test_generate_scala_trait_produces_valid_code(self)"}, {"kind": "method", "line": 463, "name": "test_generate_swift_produces_valid_code", "signature": "def test_generate_swift_produces_valid_code(self)"}, {"kind": "method", "line": 469, "name": "test_generate_swift_protocol_produces_valid_code", "signature": "def test_generate_swift_protocol_produces_valid_code(self)"}, {"kind": "method", "line": 474, "name": "test_generate_dart_produces_valid_code", "signature": "def test_generate_dart_produces_valid_code(self)"}, {"kind": "method", "line": 480, "name": "test_generate_ruby_produces_valid_code", "signature": "def test_generate_ruby_produces_valid_code(self)"}]}, {"doc": "Contract tests for the cinematic overview video renderer.", "id": "tests/test_video.py", "kind": "module", "label": "test_video.py", "language": "py", "sha256": "25d486a86b2abbe4", "symbol_count": 14, "symbols": [{"doc": "Build a tiny two-file project for video tests.", "kind": "function", "line": 15, "name": "_nodes", "signature": "def _nodes()"}, {"doc": "Build minimal analysis output with one community.", "kind": "function", "line": 23, "name": "_analysis", "signature": "def _analysis()"}, {"kind": "class", "line": 35, "name": "TestVideoContract", "signature": "class TestVideoContract(TestCase)"}, {"kind": "method", "line": 36, "name": "test_video_collect_counts", "signature": "def test_video_collect_counts(self)"}, {"kind": "method", "line": 48, "name": "test_video_collect_empty_project", "signature": "def test_video_collect_empty_project(self)"}, {"kind": "method", "line": 58, "name": "test_video_collect_enriched_fields", "signature": "def test_video_collect_enriched_fields(self)"}, {"kind": "method", "line": 78, "name": "test_video_build_scenes_durations", "signature": "def test_video_build_scenes_durations(self)"}, {"kind": "method", "line": 88, "name": "test_video_all_scenes_render_small_canvas", "signature": "def test_video_all_scenes_render_small_canvas(self)"}, {"kind": "method", "line": 106, "name": "test_video_graph_positions_deterministic", "signature": "def test_video_graph_positions_deterministic(self)"}, {"kind": "method", "line": 117, "name": "test_video_single_frame_bytes", "signature": "def test_video_single_frame_bytes(self)"}, {"kind": "method", "line": 132, "name": "test_video_hash_color_deterministic", "signature": "def test_video_hash_color_deterministic(self)"}, {"kind": "method", "line": 138, "name": "test_video_short_label_truncates", "signature": "def test_video_short_label_truncates(self)"}, {"kind": "method", "line": 143, "name": "test_video_dependencies_returns_bool", "signature": "def test_video_dependencies_returns_bool(self)"}, {"kind": "method", "line": 146, "name": "test_video_disabled_skips_without_render", "signature": "def test_video_disabled_skips_without_render(self)"}]}, {"id": "tests/test_wiki.py", "kind": "module", "label": "test_wiki.py", "language": "py", "sha256": "204193393de64d94", "symbol_count": 30, "symbols": [{"kind": "function", "line": 12, "name": "_make_node", "signature": "def _make_node(node_id, doc, symbols, language)"}, {"kind": "function", "line": 23, "name": "_make_symbol", "signature": "def _make_symbol(name, kind, line, doc)"}, {"kind": "function", "line": 27, "name": "_make_analysis", "signature": "def _make_analysis()"}, {"kind": "function", "line": 41, "name": "_make_nodes", "signature": "def _make_nodes()"}, {"kind": "class", "line": 49, "name": "TestWikiConfigContract", "signature": "class TestWikiConfigContract(TestCase)"}, {"kind": "class", "line": 65, "name": "TestWikiGenerationContract", "signature": "class TestWikiGenerationContract(TestCase)"}, {"kind": "method", "line": 50, "name": "test_config_defaults", "signature": "def test_config_defaults(self)"}, {"kind": "method", "line": 58, "name": "test_config_immutable", "signature": "def test_config_immutable(self)"}, {"kind": "method", "line": 66, "name": "test_generate_writes_all_files", "signature": "def test_generate_writes_all_files(self)"}, {"kind": "method", "line": 81, "name": "test_community_page_sections", "signature": "def test_community_page_sections(self)"}, {"kind": "method", "line": 95, "name": "test_connections_typed_with_confidence", "signature": "def test_connections_typed_with_confidence(self)"}, {"kind": "method", "line": 115, "name": "test_fallback_single_community_without_analysis", "signature": "def test_fallback_single_community_without_analysis(self)"}, {"kind": "method", "line": 125, "name": "test_report_honest_audit_sections", "signature": "def test_report_honest_audit_sections(self)"}, {"kind": "method", "line": 139, "name": "test_index_entry_point", "signature": "def test_index_entry_point(self)"}, {"kind": "method", "line": 152, "name": "test_lint_healthy_after_generate", "signature": "def test_lint_healthy_after_generate(self)"}, {"kind": "method", "line": 161, "name": "test_deterministic_connections", "signature": "def test_deterministic_connections(self)"}, {"kind": "method", "line": 174, "name": "test_privacy_mode_strips_docs", "signature": "def test_privacy_mode_strips_docs(self)"}, {"kind": "method", "line": 184, "name": "test_leftover_files_covered_by_orphans_community", "signature": "def test_leftover_files_covered_by_orphans_community(self)"}, {"kind": "method", "line": 194, "name": "test_shared_context_link_for_disconnected_communities", "signature": "def test_shared_context_link_for_disconnected_communities(self)"}, {"kind": "method", "line": 210, "name": "test_garbage_doc_filtered_from_definition", "signature": "def test_garbage_doc_filtered_from_definition(self)"}, {"kind": "method", "line": 217, "name": "test_definition_names_core_file", "signature": "def test_definition_names_core_file(self)"}, {"kind": "method", "line": 240, "name": "test_duplicate_community_labels_disambiguated", "signature": "def test_duplicate_community_labels_disambiguated(self)"}, {"kind": "method", "line": 259, "name": "test_duplicate_god_basenames_disambiguated", "signature": "def test_duplicate_god_basenames_disambiguated(self)"}, {"kind": "method", "line": 278, "name": "test_oversized_community_grouped_by_directory", "signature": "def test_oversized_community_grouped_by_directory(self)"}, {"kind": "method", "line": 302, "name": "test_large_files_flagged_in_index_and_report", "signature": "def test_large_files_flagged_in_index_and_report(self)"}, {"kind": "method", "line": 323, "name": "test_stale_pages_pruned_on_regenerate", "signature": "def test_stale_pages_pruned_on_regenerate(self)"}, {"kind": "method", "line": 335, "name": "test_risks_carry_fix_hint_scope_and_closed_cycle", "signature": "def test_risks_carry_fix_hint_scope_and_closed_cycle(self)"}, {"kind": "method", "line": 365, "name": "test_duplicate_symbol_scope_detected", "signature": "def test_duplicate_symbol_scope_detected(self)"}, {"kind": "method", "line": 388, "name": "test_no_duplicate_link_for_disjoint_scopes", "signature": "def test_no_duplicate_link_for_disjoint_scopes(self)"}, {"kind": "method", "line": 408, "name": "test_garbage_purpose_filtered", "signature": "def test_garbage_purpose_filtered(self)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (105 files)

#### `__init__.py`
**Path:** `readmenator/__init__.py`
**File Doc:** *ReadMenator -- Zero-token polyglot codebase knowledge graph generator.  Public API: Config, Symbol, Node, Edge, EdgeKind, Morphism, Category, and readmenatorApplication provide the complete toolkit for generating, querying, ranking, and UML diagramming codebase knowledge graphs without any LLM calls or cloud dependencies.*

*No symbols extracted*

#### `__main__.py`
**Path:** `readmenator/__main__.py`
**File Doc:** *Command line entry point: argument parsing and subcommand dispatch.*

**Functions:**
- `build_parser` (line 18) `def build_parser()`
- `_run_tests` (line 121) `def _run_tests()`
- `main` (line 136) `def main()`

#### `_agent_injector.py`
**Path:** `readmenator/_agent_injector.py`
**File Doc:** *Injects KNOWLEDGE_BASE.md references into AI agent instruction files.  Detects common AI agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules, etc.) and appends a pointer to KNOWLEDGE_BASE.md so that agents can discover project context quickly without manual setup.  The injected text includes instructions for the agent to regenerate KNOWLEDGE_BASE.md by running readmenator when needed.*

**Classes:**
- `AgentInjector` (line 123) `class AgentInjector` - *Injects a link to KNOWLEDGE_BASE.md into AI agent instruction files.

Detects common AI agent configuration files (AGENTS.md, CLAUDE.md,
.cursorrules, etc.) and appends a descriptive section pointing to
the knowledge base so agents discover it automatically.

The injected text instructs the agent how to regenerate the KB
by running readmenator when needed.*

**Functions:**
- `ensure_readmenator_installed` (line 101) `def ensure_readmenator_installed()` - *Check if readmenator is installed via pip; install it if missing.

Returns True if readmenator is available after the check.*

**Methods:**
- `__init__` (line 134) `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)`
- `inject` (line 148) `def inject(self, project_root)` - *Inject KB reference into all discovered agent files.

Returns the number of agent files actually modified.*
- `remove` (line 166) `def remove(self, project_root)` - *Remove KB injection from all discovered agent files.

Returns the number of files actually modified.*
- `find_agent_files` (line 179) `def find_agent_files(self, project_root)` - *Public accessor: return all detected agent files.*
- `_find_agent_files` (line 183) `def _find_agent_files(self, root)`
- `_inject_single` (line 197) `def _inject_single(self, path)`
- `_extract_current_injection` (line 235) `def _extract_current_injection(content)`
- `_remove_old_injection` (line 244) `def _remove_old_injection(content)`
- `_remove_single` (line 254) `def _remove_single(self, path)`
- `_build_injection` (line 270) `def _build_injection(self, fmt)`
- `_build_mdc_injection` (line 282) `def _build_mdc_injection(self)` - *Build Cursor .mdc injection body (frontmatter added separately).*
- `_prepend_mdc_frontmatter` (line 287) `def _prepend_mdc_frontmatter(content, injection)` - *Prepend Cursor frontmatter so the rule is auto-attached.*

#### `_agent_output.py`
**Path:** `readmenator/_agent_output.py`
**File Doc:** *Agent-friendly output generator for ReadMenator.  Generates grep-optimized, flat-markdown files in a dedicated output directory.  File names for per-subsystem files are **inferred** from the project's directory structure, never hardcoded.  The generated files are designed to be consumed by AI agents that perform ``grep`` / ``read`` operations and need queryable, small-context documents.  Every document is capped at ``AGENT_OUTPUT_MAX_LINES``: oversized documents are split on section boundaries into ``NAME.md``, ``NAME_p2.md``, ... with the table header repeated on each page, so a ``grep`` over ``NAME*.md`` still sees every line and a single read never blows an agent's context window.  Output layout::  readmenator-agent/ ├── MANIFEST.json         # freshness (git commit), read order, token costs ├── INDEX.md              # file -> purpose -> blast radius map ├── SYMBOLS.md            # one line per symbol ├── ARCHITECTURE.md       # dependency pairs (flat list) ├── SECURITY.md           # findings by severity ├── API.md                # public functions, one line each ├── GOTCHAS.md            # "don't change X because Y" ├── recipes/ │   └── *.md              # actionable task blocks └── KB_<subsystem>.md     # 1 file per inferred subsystem*

**Classes:**
- `AgentOutputGenerator` (line 70) `class AgentOutputGenerator` - *Generates agent-friendly, grep-optimised output files.

All output is plain Markdown -- no JSON wrapping, no fenced code
blocks around data structures.  Every line is greppable.*

**Methods:**
- `__init__` (line 77) `def __init__(self, config)` - *Store configuration for output paths and size budgets.*
- `generate` (line 81) `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` - *Write all agent output files and return the output directory path.*
- `_infer_subsystems` (line 137) `def _infer_subsystems(self, nodes)` - *Group nodes by directory, inferring subsystem names.*
- `_build_index` (line 172) `def _build_index(self, nodes, subsystems, imported_by)` - *Build the file -> purpose -> subsystem -> blast radius table.*
- `_build_architecture` (line 204) `def _build_architecture(self, edges, resolved_edges, nodes)` - *Build internal dependency pairs plus per-file external imports.

External imports exclude raw import strings that resolved to a
project file, so internal modules are never listed twice.*
- `_build_security` (line 256) `def _build_security(self, findings, nodes)` - *Build findings grouped by severity with scope and fix hints.*
- `_enclosing_symbol` (line 292) `def _enclosing_symbol(symbols, line)` - *Return the nearest symbol defined at or before line.*
- `_is_public` (line 302) `def _is_public(self, sym)` - *Return whether a symbol belongs in the public API listing.*
- `_qualified_names` (line 309) `def _qualified_names(symbols)` - *Map each method's index to ``Owner.method`` using the nearest preceding type.*
- `_build_api` (line 327) `def _build_api(self, nodes, resolved_map, imported_by, layers)` - *Build one greppable line per public function or method.

Dependencies and importers are stated once per file instead of
once per function, and test-layer files are skipped, which keeps
the listing an API reference rather than a symbol dump.*
- `_build_manifest` (line 385) `def _build_manifest(self, nodes, edges, resolved_edges, findings, project_root, subsystems, layers, out_dir)` - *Build MANIFEST.json: freshness, entry points, read order, costs.

The project root is recorded relatively (never an absolute path),
and the git commit lets agents detect a stale knowledge base with
one ``git rev-parse HEAD`` instead of re-reading everything.*
- `_entrypoints` (line 457) `def _entrypoints(self, nodes, layers)` - *Return likely program entry points, shallowest paths first.*
- `_inventory` (line 468) `def _inventory(self, out_dir)` - *List generated documents with line counts and token estimates.*
- `_build_symbols` (line 481) `def _build_symbols(self, nodes)` - *Build grep-friendly symbol index (one line per symbol).*
- `_closed_loop` (line 496) `def _closed_loop(cycle)` - *Render a cycle as a closed loop without duplicating a closed tail.*
- `_build_gotchas` (line 503) `def _build_gotchas(self, analysis, analysis_v2, nodes, layers, imported_by)` - *Build actionable warnings: blast radius, hotspots, cycles, violations.

Files in excluded layers (tests by default) are left out of the
centrality lists because their connectivity says nothing about
the risk of editing production code.*
- `_safe_name` (line 626) `def _safe_name(name)` - *Return a filesystem-safe subsystem name.*
- `_write_subsystem_files` (line 633) `def _write_subsystem_files(self, out_dir, subsystems, resolved_map, imported_by, layers)` - *Write one paged KB_<subsystem>.md per inferred subsystem.*
- `_build_subsystem_content` (line 648) `def _build_subsystem_content(self, name, file_nodes, resolved_map, imported_by, layers)` - *Build per-file context (purpose, layer, symbols, edges) for one subsystem.*
- `_write_recipes` (line 698) `def _write_recipes(self, recipes_dir, analysis, analysis_v2, findings, layers)` - *Write task recipes grounded in this project's actual analysis data.*
- `_deps_by_source` (line 826) `def _deps_by_source(resolved_map)` - *Index resolved dependencies by source file, sorted and deduplicated.*
- `_build_resolved_map` (line 836) `def _build_resolved_map(resolved_edges)` - *Map (source, target) pairs to their relation.*
- `_build_imported_by_map` (line 846) `def _build_imported_by_map(resolved_edges)` - *Map each file to the files that import it.*
- `_page_name` (line 856) `def _page_name(filename, page)` - *Return the file name of a page (page 1 keeps the original name).*
- `_split_units` (line 864) `def _split_units(body, is_table)` - *Split a document body into atomic units that should not straddle pages.*
- `_chunk_unit` (line 877) `def _chunk_unit(unit, budget)` - *Split an oversized unit into budget-sized chunks with continued headings.*
- `_paginate` (line 894) `def _paginate(self, filename, content)` - *Split a document into pages that each respect the line cap.*
- `_write_paged` (line 933) `def _write_paged(self, out_dir, filename, content)` - *Write a document as one or more capped pages and return their paths.*
- `_prune_owned` (line 943) `def _prune_owned(out_dir)` - *Remove previously generated pages so renamed or shrunk docs leave no stale files.*
- `_write` (line 950) `def _write(path, content)` - *Write UTF-8 text content to a path.*
- `keep` (line 522) `def keep(file_id)` - *Return whether a file belongs in the gotcha lists.*

#### `_analyzer.py`
**Path:** `readmenator/_analyzer.py`
**File Doc:** *Graph analysis engine for the readmenator knowledge graph.  Provides community detection (Louvain-like greedy modularity), god node identification (degree/PageRank centrality), surprising connection discovery (cross-community bridges), and suggested exploration questions derived from graph structure. All operations are deterministic and token-free.*

**Classes:**
- `GraphAnalyzer` (line 40) `class GraphAnalyzer` - *Deterministic graph analysis over scanned nodes and edges.

Builds an internal adjacency graph from import edges, then applies
community detection, centrality scoring, cross-community bridge
discovery, and question generation without any external API calls.*

**Functions:**
- `dominant_directory` (line 22) `def dominant_directory(file_ids)` - *Return the most informative directory label for a set of files.

Highest file count wins; ties prefer the longest (most specific)
directory so that ``sandbox`` beats ``.``; remaining ties go
alphabetical. ``"."`` is reported as ``"root"``.*

**Methods:**
- `__init__` (line 48) `def __init__(self, config)` - *Initialise with application configuration.

Args:
    config: Settings for thresholds and limits.*
- `analyze` (line 56) `def analyze(self, nodes, edges, resolved_edges)` - *Run the full analysis pipeline and return structured results.

Args:
    nodes: Scanned file nodes.
    edges: Import edges from the scanner.
    resolved_edges: Optional list of resolved-import edges (source and
        target are both project file IDs).

Returns:
    An AnalysisResult with god nodes, communities, surprising
    connections, and suggested questions.*
- `_build_adjacency` (line 109) `def _build_adjacency(self, nodes, edges)` - *Build an undirected adjacency map from import edges.*
- `_build_reverse_adjacency` (line 123) `def _build_reverse_adjacency(self, adjacency)` - *Build a directed reverse adjacency (incoming edges) map.*
- `_compute_god_nodes` (line 133) `def _compute_god_nodes(self, nodes, adjacency, reverse_adjacency)` - *Compute the most central nodes using combined degree centrality.

Score is a combination of out-degree (imports), in-degree (imported-by),
and symbol count. Higher score means more architecturally significant.*
- `_detect_communities` (line 155) `def _detect_communities(self, nodes, adjacency)` - *Detect communities using label propagation.

Each node adopts the label with the highest weighted vote among
its neighbors. Iterates until convergence or max iterations reached.
Deterministic: content-seeded order, sorted neighbors, min-label
tie-break within COMMUNITY_VOTE_EPSILON.*
- `_merge_small_communities` (line 217) `def _merge_small_communities(self, groups, adjacency, weights)` - *Fold communities smaller than COMMUNITY_MERGE_BELOW into their best neighbor.

Label propagation leaves many module-plus-test pairs; each would
become its own wiki page. The smallest group first joins the
neighboring community it shares the most vote weight with (ties
to the lowest label). Isolated groups are kept unchanged.*
- `_vote_weights` (line 264) `def _vote_weights(self, file_ids, adjacency)` - *Return each node's label-propagation vote weight.

With COMMUNITY_HUB_DAMPING a neighbor votes with weight
``1 / log2(2 + degree)``: hubs such as shared models or config,
which nearly every file imports, stop pulling the whole project
into one giant community, while ordinary neighbors keep full say.*
- `_label_communities` (line 281) `def _label_communities(self, nodes, communities)` - *Generate human-readable labels for communities.

Labels are based on the most common directory within the community.*
- `_core_file` (line 308) `def _core_file(members, node_map)` - *Return the stem of a community's most symbol-rich non-test file.

Used to tell apart communities that share a dominant directory,
so labels read ``pkg: _video`` instead of an opaque number.*
- `_build_community_map` (line 328) `def _build_community_map(self, communities)` - *Build a reverse map from file ID to community ID.*
- `_compute_cohesion` (line 338) `def _compute_cohesion(self, communities, adjacency)` - *Compute cohesion score for each community.

Cohesion = internal edges / (internal edges + external edges).*
- `_find_surprising_connections` (line 363) `def _find_surprising_connections(self, nodes, adjacency, community_map)` - *Find non-obvious cross-community bridges.

A connection is surprising when two nodes in different communities
are connected indirectly through 3 or more hops, and the path
crosses community boundaries.*
- `_shortest_path_communities` (line 403) `def _shortest_path_communities(self, source, target, adjacency, community_map)` - *Find the shortest path and communities traversed.*
- `_suggest_questions` (line 430) `def _suggest_questions(self, nodes, god_nodes, communities, community_labels, surprising, adjacency)` - *Generate plain-language exploration questions from graph structure.*
- `is_test` (line 314) `def is_test(fid)` - *Return whether a path looks like a test file.*

#### `_app.py`
**Path:** `readmenator/_app.py`
**File Doc:** *Application orchestrator: scan, resolve, analyze, and write every output.  Thin facade over AnalyzerFactory that wires the scanner, analyzers, and generators into the run, rebuild, update, query, and export commands.*

**Classes:**
- `readmenatorApplication` (line 43) `class readmenatorApplication`

**Methods:**
- `__init__` (line 44) `def __init__(self, config)`
- `_scan` (line 53) `def _scan(self, target_dir)`
- `_scan_with_content` (line 61) `def _scan_with_content(self, target_dir)`
- `_resolve_imports` (line 71) `def _resolve_imports(self, nodes, edges, target_dir)`
- `run` (line 90) `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- `check_freshness` (line 214) `def check_freshness(self, target_dir)` - *Compare the MANIFEST source fingerprint against the current sources.

Args:
    target_dir: Project root directory.

Returns:
    Tuple of (fresh, human-readable reason).*
- `_maybe_refresh_pages` (line 241) `def _maybe_refresh_pages(self, root)` - *Refresh the static docs site when a previous ``pages`` run created it.

The site directory is only rewritten when it already holds a
readmenator gallery (index plus maps subdirectory), so a user's own
docs folder is never taken over by a plain rebuild.*
- `_maybe_publish_github_wiki` (line 259) `def _maybe_publish_github_wiki(self, root)` - *Publish generated docs to the GitHub wiki when GH_WIKI_ENABLED is set.*
- `publish_github_wiki` (line 265) `def publish_github_wiki(self, target_dir, dry_run)` - *Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.

Args:
    target_dir: Project root directory with generated outputs.
    dry_run: Render pages into GH_WIKI_DRY_RUN_DIR without git calls.

Returns:
    WikiPublishResult with pages written and push status.*
- `_write_sidecar_outputs` (line 279) `def _write_sidecar_outputs(self, root, findings, analysis_v2)`
- `_inject_readme_link` (line 305) `def _inject_readme_link(self, root)`
- `_inject_agent_files` (line 313) `def _inject_agent_files(self, root)`
- `generate_uml_code` (line 321) `def generate_uml_code(self, target_dir, language, output_path)`
- `_log_summary` (line 333) `def _log_summary(self, nodes, edges, root, resolved_edges, analysis, layer_summary, analysis_v2, findings)`
- `update` (line 388) `def update(self, target_dir, run_security)`
- `_scan_for_cache` (line 493) `def _scan_for_cache(self, root, cache)`
- `query` (line 511) `def query(self, target_dir, question)`
- `explain` (line 516) `def explain(self, target_dir, symbol_name)`
- `find_path` (line 528) `def find_path(self, target_dir, symbol_a, symbol_b)`
- `summary` (line 541) `def summary(self, target_dir)`
- `rank_query` (line 546) `def rank_query(self, target_dir, query, top_n)` - *Run a ranked query against the knowledge graph.

Uses Personalized PageRank seeded from query terms to produce
a relevance-ranked list of files with score decomposition.

Args:
    target_dir: Project root directory.
    query: Free-text query.
    top_n: Number of results.

Returns:
    A RankedResult with scored items.*
- `rebuild` (line 576) `def rebuild(self, target_dir, run_security)`
- `analyze` (line 579) `def analyze(self, target_dir)`
- `export_json` (line 583) `def export_json(self, target_dir, output_path)`
- `export_html` (line 594) `def export_html(self, target_dir, output_path)`
- `export_svg` (line 605) `def export_svg(self, target_dir, output_path)`
- `export` (line 616) `def export(self, target_dir)`
- `export_graphml` (line 621) `def export_graphml(self, target_dir, output_path)`
- `export_cypher` (line 632) `def export_cypher(self, target_dir, output_path)`
- `export_obsidian` (line 645) `def export_obsidian(self, target_dir, output_dir)`
- `export_wiki` (line 655) `def export_wiki(self, target_dir, output_dir)` - *Generate the navigable agent wiki for the target project.

Args:
    target_dir: Project root directory.
    output_dir: Optional override for the wiki output directory.

Returns:
    Path of the wiki directory that was written.*
- `lint_wiki` (line 678) `def lint_wiki(self, target_dir)` - *Check wiki health and log reported issues.

Args:
    target_dir: Project root directory.

Returns:
    List of issue descriptions, empty when healthy.*
- `export_diagrams` (line 696) `def export_diagrams(self, target_dir, output_dir, full)` - *Export all five interactive system maps plus a gallery index.

Args:
    target_dir: Project root directory.
    output_dir: Destination directory for map files.
    full: True includes every file with a grown canvas, False truncates.

Returns:
    Mapping of diagram kind to written file path.*
- `_live_renderer` (line 738) `def _live_renderer(self)` - *Return the configured map renderer for published output.

Returns:
    The vis.js renderer when enabled, else the offline renderer.*
- `export_diagram` (line 748) `def export_diagram(self, target_dir, kind, output_path, full)` - *Export a single interactive system map as standalone HTML.

Args:
    target_dir: Project root directory.
    kind: Diagram kind identifier.
    output_path: Destination file path.
    full: True includes every file with a grown canvas, False truncates.

Returns:
    Rendered HTML document that was written.*
- `export_pages` (line 787) `def export_pages(self, target_dir, output_dir, full)` - *Publish all system maps plus a gallery index as a static site.

Args:
    target_dir: Project root directory.
    output_dir: Destination directory for the static site.
    full: True includes every file with a grown canvas, False truncates.

Returns:
    Mapping of published page identifier to written file path.*
- `export_video` (line 826) `def export_video(self, target_dir, output_path)` - *Render the cinematic overview video for the target project.

Args:
    target_dir: Project root directory.
    output_path: Destination mp4 path.

Returns:
    Written file path, or None when video is disabled or skipped.*
- `_maybe_export_video` (line 850) `def _maybe_export_video(self, root, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, content_map, output_path)` - *Render video when enabled, skipping gracefully without deps.*
- `watch` (line 890) `def watch(self, target_dir)`
- `audit` (line 900) `def audit(self, target_dir)`
- `audit_deep` (line 907) `def audit_deep(self, target_dir)`
- `export_sarif` (line 927) `def export_sarif(self, target_dir, output_path)`
- `export_rules` (line 937) `def export_rules(self, target_dir, output_dir)`
- `detect_layers` (line 947) `def detect_layers(self, target_dir)`
- `lint` (line 957) `def lint(self, target_dir)`
- `strip_dead_code` (line 970) `def strip_dead_code(self, target_dir)`
- `generate_cursorrules` (line 980) `def generate_cursorrules(self, target_dir)`
- `refactor_monolith` (line 995) `def refactor_monolith(self, target_dir)`
- `on_change` (line 894) `def on_change()`

#### `_cache.py`
**Path:** `readmenator/_cache.py`
**File Doc:** *File-content hash cache for incremental scanning and analysis caching.  Computes SHA256 digests of file contents and persists them to disk so that subsequent scans can skip unchanged files. Also supports caching of analysis results (security findings, v2 analysis, etc.) for faster incremental rebuilds.*

**Classes:**
- `FileCache` (line 20) `class FileCache` - *SHA256-based cache for incremental file scanning and analysis.

Stores a JSON mapping of relative file paths to their content
hashes inside the project's cache directory. On subsequent runs,
files whose hash matches the cached value are skipped.

Also caches analysis results so that unchanged files reuse
previously-computed security findings, taint paths, etc.*

**Methods:**
- `source_fingerprint` (line 179) `def source_fingerprint(project_root, file_ids)` - *Return one SHA256 over the sorted paths and contents of scanned sources.

Generated documents embed this value; recomputing it later answers
"do the docs still describe these sources?" exactly, independent of
git commits (docs generated before a commit stay fresh after it).

Args:
    project_root: Project root directory.
    file_ids: Project-relative source paths that were scanned.

Returns:
    Hex digest; missing, unreadable, or symlinked files hash as empty.*
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
**File Doc:** *Category theory model for the readmenator code graph.  Defines typed morphisms (edges with semantic kind), objects (file nodes), and a Category class for algebraic path composition. Every edge in the knowledge graph carries an EdgeKind that survives through to ranking computations.  The gain from category theory is that ReadMenator can answer queries by transformation, not just proximity:  - "What code implements this concept?"  -> documents -> defines - "What breaks if I change this node?"  -> composition of reverse edges - "What tests validate this abstraction?" -> defines <- tests - "How do I get from public API to impl?" -> composite paths*

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
- `_infer_edge_kind` (line 278) `def _infer_edge_kind(relation)` - *Map a relation string to an EdgeKind.

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
**File Doc:** *Immutable configuration dataclass for readmenator.  All tuneable parameters live here as frozen dataclass fields. No magic numbers or hardcoded paths exist elsewhere in the codebase. Derived consumers import Config and read values from an instance.*

**Classes:**
- `Config` (line 15) `class Config` - *Single source of truth for all readmenator settings.

Every tuneable constant -- file-size limits, directory depth,
supported extensions, symbol pluralisation map, Mermaid style
tokens, graph analysis thresholds, and export settings -- is
defined here and consumed by reference elsewhere.*

#### `_cpg.py`
**Path:** `readmenator/_cpg.py`
**File Doc:** *Code Property Graph (CPG) generator emitting JSON-LD for AI agents.  Merges symbols, call, import, and inheritance edges, content hashes, and optional analysis metadata into one embeddable, zero-token graph.*

**Classes:**
- `CodePropertyGraph` (line 16) `class CodePropertyGraph` - *Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.

Produces a structured representation merging AST-level symbol data,
control-flow edges (calls), data-flow edges (imports), inheritance
relationships, and security findings (with MITRE ATT&CK mappings)
into a single machine-readable document. Designed to be embedded in
KNOWLEDGE_BASE.md for zero-token agent context.*

**Methods:**
- `__init__` (line 26) `def __init__(self, privacy_mode, cpg_context)`
- `generate` (line 30) `def generate(self, nodes, edges, resolved_edges, analysis, findings)` - *Generate the CPG JSON-LD string embeddable in markdown.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for metadata.
    findings: Optional security findings with MITRE ATT&CK IDs.

Returns:
    Compact JSON-LD string with @context, nodes, edges, analysis,
    and mitre_attack metadata.*
- `_severity_counts` (line 147) `def _severity_counts(self, findings)`
- `_build_symbol_list` (line 153) `def _build_symbol_list(self, node)`
- `_compute_node_hash` (line 169) `def _compute_node_hash(node)`

#### `_cursorrules_generator.py`
**Path:** `readmenator/_cursorrules_generator.py`
**File Doc:** *Dynamic .cursorrules generator for the readmenator knowledge graph.  Reads architectural analysis results and linter violations to produce a deterministic .cursorrules file that feeds structural constraints back into AI coding assistants.*

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

#### `_dataflow.py`
**Path:** `readmenator/_dataflow.py`
**File Doc:** *Procedural intra-function dataflow analysis for readmenator.  Detects classic logic bug classes without tokens, types, or control-flow graphs: use of uninitialized locals, dead stores (assigned but never read), and unchecked allocator results. Pure regex over function body spans derived from parsed symbol line ranges. Every finding is marked INFERRED: heuristics trade recall for reviewable, line-grounded leads.*

**Classes:**
- `DataflowAnalyzer` (line 122) `class DataflowAnalyzer` - *Regex-based intra-function dataflow checker over scanned content.*

**Functions:**
- `_strip_noise` (line 96) `def _strip_noise(line)` - *Remove comments and string contents that confuse identifier scans.

Strings are blanked before comment stripping so that ``//`` inside
URL literals is not mistaken for a comment opener.*
- `_strip_block_comments` (line 107) `def _strip_block_comments(content)` - *Blank block comments while preserving newlines and line numbers.*
- `_strip_sizeof` (line 116) `def _strip_sizeof(line)` - *Blank sizeof operands, which never evaluate their argument at runtime.*

**Methods:**
- `_blank` (line 110) `def _blank(match)`
- `__init__` (line 125) `def __init__(self, config)` - *Store configuration for enable flag and issue caps.*
- `analyze` (line 129) `def analyze(self, nodes, content_map)` - *Check every function body span and return capped issues.*
- `_brace_depths` (line 153) `def _brace_depths(lines)` - *Return the brace depth before each line of noise-stripped code.*
- `_function_spans` (line 164) `def _function_spans(self, node, total_lines, depths)` - *Return (name, start_idx, end_idx) spans for function symbols.

Only function lines and file-scope (depth 0) symbols terminate a
span; local struct, enum, or variable declarations inside a body
do not truncate the enclosing function.*
- `_analyze_function` (line 191) `def _analyze_function(self, file_id, func, lines, start, end)` - *Run def-use checks over one function body span.*
- `_scan_reads` (line 403) `def _scan_reads(text, lineno, reads, assigned, declared_names)` - *Record identifier reads and address-takes inside an expression.*
- `_scan_inline_aliases` (line 427) `def _scan_inline_aliases(line, lineno, arrays, derived_alias, deriv_reads)` - *Discover pointer-from-array aliases in mid-line statements.*
- `_scan_out_params` (line 450) `def _scan_out_params(line, lineno, assigned)` - *Treat known filler/scan call arguments as assignments.*
- `_scan_array_args` (line 461) `def _scan_array_args(line, lineno, arrays, assigned)` - *Treat arrays passed to non-readonly calls as assignments.*
- `_params_of` (line 474) `def _params_of(signature_line)` - *Extract parameter names from a function signature line.*
- `_track_call_continuation` (line 494) `def _track_call_continuation(line, call_open, paren_balance)` - *Track whether the next line continues an unclosed call.*
- `_mentions_param` (line 513) `def _mentions_param(text, params)` - *Return True when an expression mentions a function parameter.*
- `_is_member` (line 521) `def _is_member(line, pos)` - *Return True when the identifier at pos is a struct member access.*
- `_member_base` (line 527) `def _member_base(line, pos)` - *Return the base identifier of a member access chain.*
- `_is_prototype` (line 535) `def _is_prototype(line)` - *Return True for declaration lines that are actually prototypes.*
- `_null_checked` (line 540) `def _null_checked(body_text, name)` - *Return True when body contains a NULL/boolean check for name.*

#### `_dead_code.py`
**Path:** `readmenator/_dead_code.py`
**File Doc:** *Dead code detection for the readmenator knowledge graph.  Identifies orphaned symbols with zero in-degree in the resolved import graph, excluding known entry points. Generates structured reports without auto-deleting any code.*

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

#### `_diagrams.py`
**Path:** `readmenator/_diagrams.py`
**File Doc:** *Self-contained interactive system maps for the knowledge graph.  Builds typed intermediate representations for five diagram kinds (architecture, workflow, sequence, dataflow, lifecycle) from scanned nodes and edges, validates each map deterministically, and renders a single self-contained HTML document with inline SVG, search, focus, reach tracing, route probing, role comparison, guided views, presentation stage, themes, presets, keyboard access, deep links, finite motion, and client-side export.*

**Classes:**
- `MapNode` (line 62) `class MapNode` - *Single authored node in a system map.

Attributes:
    node_id: Stable identifier derived from the file path.
    label: Short display label.
    role: Semantic role used for color and lens comparison.
    group: Lane or layer grouping used for layout.
    detail: Supporting detail shown in the passport panel.
    x: Deterministic horizontal canvas coordinate.
    y: Deterministic vertical canvas coordinate.
    language: Programming language of the source file.
    doc: File-level documentation string.
    symbols: Symbol records with name, kind, line, signature, doc.
    symbol_total: Total symbol count before per-node truncation.*
- `MapEdge` (line 93) `class MapEdge` - *Single authored directed relationship in a system map.

Attributes:
    source: Source node identifier.
    target: Target node identifier.
    label: Semantic relationship label.
    kind: Relationship kind used for styling.*
- `MapView` (line 110) `class MapView` - *Single guided chapter over authored topology.

Attributes:
    view_id: Stable chapter identifier usable in deep links.
    title: Chapter title.
    focus: Ordered node identifiers highlighted by the chapter.
    description: Supporting explanation for the chapter.*
- `SystemMap` (line 127) `class SystemMap` - *Typed intermediate representation of one diagram.

Attributes:
    kind: Diagram kind identifier.
    title: Human-readable diagram title.
    nodes: Authored nodes with deterministic coordinates.
    edges: Authored directed relationships.
    views: Guided chapters over the topology.
    meta: Generation metadata for receipts and exports.*
- `MapDiagnostic` (line 148) `class MapDiagnostic` - *Single machine-readable validation diagnostic.

Attributes:
    rule: Stable rule code.
    subject: Identifier of the offending subject.
    evidence: Measured evidence describing the failure.
    repair: Supported repair control for the failure.*
- `MapReceipt` (line 165) `class MapReceipt` - *Deterministic validation receipt for a system map.

Attributes:
    passed: True when zero errors were found.
    checks: Names of checks that were executed.
    errors: Error diagnostics blocking delivery.
    warnings: Non-blocking advisory diagnostics.*
- `MapDelta` (line 182) `class MapDelta` - *Before and after comparison between two maps of the same kind.

Attributes:
    kind: Diagram kind that was compared.
    added: Node identifiers present only in the head map.
    removed: Node identifiers present only in the base map.
    changed: Node identifiers with altered role, group, or label.
    moved: Node identifiers with altered coordinates.
    rerouted: Edge pairs present only in one of the two maps.*
- `SystemMapValidator` (line 202) `class SystemMapValidator` - *Deterministic validator for system map intermediate representations.*
- `SystemMapBuilder` (line 426) `class SystemMapBuilder` - *Builds deterministic system maps from the scanned knowledge graph.*
- `InteractiveMapRenderer` (line 1471) `class InteractiveMapRenderer` - *Renders a system map as one self-contained interactive HTML document.*
- `VisNetworkRenderer` (line 2186) `class VisNetworkRenderer` - *Renders a system map as a physics-driven vis.js network document.

Fetches the configured vis-network bundle from a CDN at view time,
so pages need network access. Nodes stay draggable with live
physics; use the inline renderer when fully offline output matters.*
- `DocsSitePublisher` (line 2707) `class DocsSitePublisher` - *Publishes validated system maps as a static documentation site.

Writes one standalone map document per diagram kind plus a gallery
index page, ready to serve as project documentation or a static
hosting root. All output is self-contained with zero external
requests and relative links only.*

**Functions:**
- `_escape_markup` (line 24) `def _escape_markup(value)` - *Escape text for HTML and tooltip embedding.

Args:
    value: Raw text.

Returns:
    Escaped text safe for markup contexts.*
- `_json_payload` (line 36) `def _json_payload(payload)` - *Serialize a payload for safe inline script embedding.

Args:
    payload: JSON-serializable payload.

Returns:
    JSON text with angle brackets unicode-escaped.*
- `_role_color` (line 48) `def _role_color(role, config)` - *Return the stroke color for a semantic role.

Args:
    role: Semantic role identifier.
    config: Central settings holding the role palette.

Returns:
    Hex color string for the role.*

**Methods:**
- `__init__` (line 205) `def __init__(self, config)` - *Initialise the validator with application configuration.

Args:
    config: Central settings for map size limits.*
- `_effective_canvas` (line 213) `def _effective_canvas(self, system_map)` - *Return the canvas bounds applying per-map full-mode growth.

Args:
    system_map: Map carrying optional canvas_width/canvas_height metadata.

Returns:
    Effective canvas width and height pair.*
- `validate` (line 234) `def validate(self, system_map)` - *Validate a system map and return a deterministic receipt.

Args:
    system_map: Map intermediate representation to validate.

Returns:
    Validation receipt with executed checks and diagnostics.*
- `__init__` (line 455) `def __init__(self, config)` - *Initialise the builder with application configuration.

Args:
    config: Central settings for layout geometry and limits.*
- `supported_kinds` (line 464) `def supported_kinds(self)` - *Return the supported diagram kind identifiers.

Returns:
    Ordered list of the configured diagram kinds.*
- `_is_full` (line 472) `def _is_full(self, full)` - *Return whether full-map scope applies for this build.

Args:
    full: Explicit caller override, None honors configuration.

Returns:
    True when every scanned file must be included without truncation.*
- `build` (line 485) `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)` - *Build one deterministic system map of the requested kind.

Args:
    nodes: Scanned file nodes.
    edges: Raw import edges.
    resolved_edges: Project-internal resolved import edges.
    layers: Mapping of file identifier to architectural layer.
    findings: Security findings used for sensitivity marking.
    analysis: Graph analysis used for centrality ranking.
    kind: Diagram kind identifier.
    full: True includes every file with a grown canvas, None honors config.

Returns:
    Validated system map intermediate representation.*
- `build_all` (line 523) `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)` - *Build all five diagram kinds deterministically.

Args:
    nodes: Scanned file nodes.
    edges: Raw import edges.
    resolved_edges: Project-internal resolved import edges.
    layers: Mapping of file identifier to architectural layer.
    findings: Security findings used for sensitivity marking.
    analysis: Graph analysis used for centrality ranking.
    full: True includes every file with a grown canvas, None honors config.

Returns:
    Mapping of diagram kind to system map.*
- `compare` (line 554) `def compare(self, base, head)` - *Compare two maps of the same kind as before, delta, and after.

Args:
    base: Baseline system map.
    head: Revised system map.

Returns:
    Deterministic delta with added, removed, changed, moved, rerouted facts.*
- `_title_for` (line 593) `def _title_for(self, kind)` - *Return the display title for a diagram kind.

Args:
    kind: Diagram kind identifier.

Returns:
    Human-readable diagram title.*
- `_role_for` (line 607) `def _role_for(self, group, sensitive)` - *Return the semantic role for a group with sensitivity override.

Args:
    group: Architectural layer group name.
    sensitive: True when the file carries elevated findings.

Returns:
    Semantic role identifier.*
- `_sensitive_files` (line 624) `def _sensitive_files(self, findings)` - *Return files carrying elevated severity findings.

Args:
    findings: Security findings to inspect.

Returns:
    Set of file paths with critical or high severity.*
- `_ranked_file_ids` (line 641) `def _ranked_file_ids(self, nodes, links, analysis)` - *Rank file identifiers by centrality then symbol count.

Args:
    nodes: Scanned file nodes.
    links: Internal edges used for degree scoring.
    analysis: Optional analysis with god node scores.

Returns:
    File identifiers ordered by importance.*
- `_select_primary` (line 676) `def _select_primary(self, nodes, links, analysis, full)` - *Select the primary node scope honoring the configured limit.

Args:
    nodes: Scanned file nodes.
    links: Internal edges used for ranking.
    analysis: Optional analysis with centrality scores.
    full: True returns every ranked node without truncation.

Returns:
    Primary nodes in deterministic ranked order.*
- `_internal_links` (line 702) `def _internal_links(self, edges, selected, full)` - *Filter edges to project-internal links between selected files.

Args:
    edges: Candidate edges.
    selected: Selected file identifiers.
    full: True keeps every internal edge without truncation.

Returns:
    Deterministically ordered internal edges.*
- `_symbol_records` (line 725) `def _symbol_records(self, node)` - *Build truncated symbol records for map documentation payloads.

Args:
    node: Scanned file node with extracted symbols.

Returns:
    Symbol records ordered by line, capped by configuration.*
- `_short_label` (line 747) `def _short_label(self, value)` - *Shorten a label to the configured readable length.

Args:
    value: Raw label text.

Returns:
    Truncated label with length guard applied.*
- `_layout_columns` (line 762) `def _layout_columns(self, items, kind, full)` - *Compute deterministic column lane coordinates for grouped items.

Args:
    items: Pairs of identifier and group name.
    kind: Diagram kind used only for metadata completeness.
    full: True keeps every lane and grows the canvas instead of dropping.

Returns:
    Mapping of identifier to canvas coordinates.*
- `_lanes_that_fit` (line 810) `def _lanes_that_fit(self, lanes)` - *Drop lowest-priority lanes until columns fit the canvas width.

Args:
    lanes: Lane names in priority order.

Returns:
    Leading lanes whose node boxes fit the canvas width.*
- `_fitted_gap` (line 827) `def _fitted_gap(self, count, item, gap, total, margin)` - *Compress spacing deterministically so items fit the canvas.

Args:
    count: Number of items placed along the axis.
    item: Fixed item extent along the axis.
    gap: Preferred spacing between items.
    total: Total canvas extent along the axis.
    margin: Margin reserved on each side.

Returns:
    Spacing that keeps every item inside the canvas.*
- `_lane_capacity` (line 851) `def _lane_capacity(self)` - *Return the maximum members per lane fitting the canvas height.

Returns:
    Number of node rows fitting between lane top and margin.*
- `_cap_lane_scope` (line 865) `def _cap_lane_scope(self, ranked, layer_of)` - *Cap ranked nodes per lane so every lane fits the canvas height.

Args:
    ranked: Nodes in global rank order.
    layer_of: Mapping of file identifier to lane name.

Returns:
    Scoped nodes preserving rank order within each lane.*
- `_layout_sequence` (line 889) `def _layout_sequence(self, ordered, full)` - *Compute deterministic lifeline row coordinates for sequences.

Args:
    ordered: Participant identifiers in display order.
    full: True wraps participants across rows instead of truncating width.

Returns:
    Mapping of identifier to canvas coordinates.*
- `_sequence_capacity` (line 926) `def _sequence_capacity(self)` - *Return the maximum participants fitting the canvas width.

Returns:
    Number of lifelines fitting with minimum spacing applied.*
- `_place` (line 940) `def _place(self, ranked, layer_of, kind, full)` - *Cap lane scope and compute coordinates for placed nodes only.

Args:
    ranked: Nodes in global rank order.
    layer_of: Mapping of file identifier to lane name.
    kind: Diagram kind used only for metadata completeness.
    full: True keeps every node without lane caps or drops.

Returns:
    Canvas positions and the placed node subset.*
- `_canvas_for` (line 960) `def _canvas_for(self, positions, full)` - *Grow the canvas to enclose every placed node in full mode.

Args:
    positions: Placed node coordinates.
    full: True grows beyond configured bounds, False returns configured size.

Returns:
    Effective canvas width and height pair.*
- `_meta_for` (line 978) `def _meta_for(self, kind, placed, links, total, positions, full)` - *Build generation metadata with honest scope and canvas size.

Args:
    kind: Diagram kind identifier, unused beyond completeness.
    placed: Authored map nodes.
    links: Authored edge count.
    total: Total scanned file count.
    positions: Placed coordinates used for canvas growth.
    full: True tags the map as untruncated with a grown canvas.

Returns:
    Metadata mapping for receipts and exports.*
- `_make_views` (line 1001) `def _make_views(self, kind, primary, links)` - *Create guided chapters from authored topology.

Args:
    kind: Diagram kind identifier.
    primary: Ordered primary path node identifiers.
    links: Authored internal relationships.

Returns:
    Guided chapters limited to the configured maximum.*
- `_build_architecture` (line 1073) `def _build_architecture(self, nodes, links, layers, findings, analysis, full)` - *Build the runtime architecture map from file topology.

Args:
    nodes: Scanned file nodes.
    links: Internal edges.
    layers: Layer mapping.
    findings: Security findings.
    analysis: Graph analysis.
    full: True keeps every file without truncation.

Returns:
    Architecture system map.*
- `_build_workflow` (line 1133) `def _build_workflow(self, nodes, links, layers, findings, full)` - *Build the delivery workflow map across architectural lanes.

Args:
    nodes: Scanned file nodes.
    links: Internal edges.
    layers: Layer mapping.
    findings: Security findings.
    full: True keeps every file without lane sampling.

Returns:
    Workflow system map.*
- `_build_sequence` (line 1213) `def _build_sequence(self, nodes, links, layers, analysis, full)` - *Build the request sequence map over top participants.

Args:
    nodes: Scanned file nodes.
    links: Internal edges.
    layers: Layer mapping.
    analysis: Graph analysis.
    full: True keeps every participant with wrapped rows.

Returns:
    Sequence system map.*
- `_build_dataflow` (line 1295) `def _build_dataflow(self, nodes, links, layers, findings, full)` - *Build the data flow map from sources through stores.

Args:
    nodes: Scanned file nodes.
    links: Internal edges.
    layers: Layer mapping.
    findings: Security findings for sensitivity.
    full: True keeps every file without truncation.

Returns:
    Dataflow system map.*
- `_build_lifecycle` (line 1378) `def _build_lifecycle(self, nodes, links, layers, findings, full)` - *Build the change lifecycle map with waits, retries, and terminals.

Args:
    nodes: Scanned file nodes.
    links: Internal edges.
    layers: Layer mapping.
    findings: Security findings.
    full: True keeps every file without truncation.

Returns:
    Lifecycle system map.*
- `__init__` (line 1474) `def __init__(self, config)` - *Initialise the renderer with application configuration.

Args:
    config: Central settings for preset, theme, and share size.*
- `_canvas_size` (line 1482) `def _canvas_size(self, system_map)` - *Return the effective canvas size for rendering a map.

Args:
    system_map: Map carrying optional grown canvas metadata.

Returns:
    Effective canvas width and height pair.*
- `render` (line 1503) `def render(self, system_map)` - *Render a system map as a self-contained HTML document.

Args:
    system_map: Validated system map intermediate representation.

Returns:
    Complete standalone HTML document with inline SVG and scripting.*
- `write` (line 1605) `def write(self, system_map, output_path)` - *Render a system map and write it to a relative output path.

Args:
    system_map: System map intermediate representation.
    output_path: Destination file path.

Returns:
    Rendered HTML document that was written.*
- `_safe_json` (line 1624) `def _safe_json(self, payload)` - *Serialize a payload for safe inline script embedding.

Args:
    payload: JSON-serializable payload.

Returns:
    JSON text with angle brackets unicode-escaped.*
- `_escape` (line 1635) `def _escape(self, value)` - *Escape text for SVG and HTML embedding.

Args:
    value: Raw text.

Returns:
    Escaped text safe for markup contexts.*
- `_role_color` (line 1646) `def _role_color(self, role)` - *Return the stroke color for a semantic role.

Args:
    role: Semantic role identifier.

Returns:
    Hex color string for the role.*
- `_edge_path` (line 1657) `def _edge_path(self, x1, y1, x2, y2)` - *Compute a deterministic curved route between two nodes.

Args:
    x1: Source horizontal center.
    y1: Source vertical center.
    x2: Target horizontal center.
    y2: Target vertical center.

Returns:
    SVG path data string.*
- `_nodes_svg` (line 1693) `def _nodes_svg(self, system_map)` - *Render authored nodes as inline SVG groups.

Args:
    system_map: System map intermediate representation.

Returns:
    SVG fragment with one group per node.*
- `_edges_svg` (line 1741) `def _edges_svg(self, system_map)` - *Render authored relationships as inline SVG paths.

Args:
    system_map: System map intermediate representation.

Returns:
    SVG fragment with one path per relationship.*
- `_template` (line 1788) `def _template(self)` - *Return the self-contained viewer document template.

Returns:
    HTML template with replacement tokens for map content.*
- `__init__` (line 2194) `def __init__(self, config)` - *Initialise the renderer with application configuration.

Args:
    config: Central settings for CDN bundle and physics.*
- `render` (line 2202) `def render(self, system_map)` - *Render a system map as a vis.js network HTML document.

Args:
    system_map: Validated system map intermediate representation.

Returns:
    HTML document driving a draggable physics network.*
- `write` (line 2303) `def write(self, system_map, output_path)` - *Render a vis.js map and write it to a relative output path.

Args:
    system_map: System map intermediate representation.
    output_path: Destination file path.

Returns:
    Rendered HTML document that was written.*
- `_tooltip` (line 2320) `def _tooltip(self, node)` - *Build a documentation tooltip for a network node.

Args:
    node: Authored map node.

Returns:
    Escaped tooltip markup with docs and top symbols.*
- `_template` (line 2351) `def _template(self)` - *Return the vis.js viewer document template.

Returns:
    HTML template with replacement tokens for map content.*
- `__init__` (line 2724) `def __init__(self, config)` - *Initialise the publisher with application configuration.

Args:
    config: Central settings for pages layout and map limits.*
- `description_for` (line 2734) `def description_for(self, kind)` - *Return the gallery description for a diagram kind.

Args:
    kind: Diagram kind identifier.

Returns:
    Human-readable gallery description.*
- `publish` (line 2748) `def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries)` - *Publish maps and a gallery index into a documentation directory.

Args:
    maps: Mapping of diagram kind to system map.
    project_name: Display name used for index titles.
    output_dir: Destination directory for the static site.
    stats: Optional project counters shown in the gallery header.
    renderer: Map renderer with a write method, defaults to offline.
    project_root: Optional project root used to collect video and docs.
    video_rel: Optional precomputed video href relative to the index.
    doc_entries: Optional precomputed doc entries with name and href.

Returns:
    Mapping of published page identifier to written file path.*
- `collect_doc_sources` (line 2836) `def collect_doc_sources(self, project_root)` - *Collect generated markdown sources for the static site.

Args:
    project_root: Project root directory to scan for docs.

Returns:
    Sorted list of markdown file paths capped by configuration.*
- `publish_assets` (line 2862) `def publish_assets(self, project_root, output_dir)` - *Copy overview video and markdown docs into the static site.

Args:
    project_root: Project root holding generated artifacts.
    output_dir: Static site root receiving copied assets.

Returns:
    Mapping with video_rel, doc_entries, and written paths.*
- `_prune_stale_docs` (line 2918) `def _prune_stale_docs(docs_root, keep)` - *Delete copied markdown docs that no longer exist in the project.

The docs subdirectory is owned by the publisher; without pruning,
renamed wiki or paged agent files would linger in the site forever.

Args:
    docs_root: Site directory holding copied markdown.
    keep: Relative paths published in this run.*
- `render_llms_txt` (line 2935) `def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)` - *Render an llms.txt entry point so agents can navigate the site as text.

Follows the llms.txt convention: an H1 title, a blockquote summary,
then H2 sections of markdown links. Agent-oriented markdown comes
first because it is cheaper to read than the HTML maps.

Args:
    project_name: Display name used for the title.
    maps: Mapping of published diagram kind to system map.
    stats: Project counters summarized in the blockquote.
    href_prefix: Relative prefix pointing at the map directory.
    doc_entries: Published markdown docs with name and href.

Returns:
    Plain markdown text for llms.txt.*
- `render_index` (line 3011) `def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries)` - *Render the gallery index page for published maps.

Args:
    project_name: Display name used for index titles.
    maps: Mapping of published diagram kind to system map.
    stats: Project counters shown in the gallery header.
    href_prefix: Relative prefix pointing at the map directory.
    video_rel: Optional video href relative to the index.
    doc_entries: Optional doc entries with name, href, preview.

Returns:
    Complete standalone HTML gallery document.*
- `_video_section` (line 3170) `def _video_section(self, video_rel)` - *Render the overview video section with an HTML5 video tag.

Args:
    video_rel: Video href relative to the index, None hides the section.

Returns:
    HTML section fragment, empty string when no video is available.*
- `_docs_section` (line 3194) `def _docs_section(self, doc_entries)` - *Render the documentation grid with an offline markdown viewer.

Args:
    doc_entries: Doc entries with name, href, and preview keys.

Returns:
    HTML section fragment, empty string when no docs are available.*
- `_href_prefix` (line 3239) `def _href_prefix(self)` - *Return the relative href prefix for map links.

Returns:
    Map subdirectory with trailing slash, or empty string.*
- `_card` (line 3250) `def _card(self, kind, system_map, href_prefix)` - *Render one gallery card linking to a published map.

Args:
    kind: Diagram kind identifier.
    system_map: Published system map.
    href_prefix: Relative prefix pointing at the map directory.

Returns:
    HTML card fragment with a relative map link.*
- `_stats_line` (line 3289) `def _stats_line(self, stats)` - *Render the gallery header statistics line.

Args:
    stats: Project counters.

Returns:
    Escaped statistics summary string.*
- `_escape` (line 3303) `def _escape(self, value)` - *Escape text for HTML embedding.

Args:
    value: Raw text.

Returns:
    Escaped text safe for markup contexts.*
- `order` (line 2983) `def order(entry)` - *Sort entry points first, then alphabetically.*

#### `_documentation.py`
**Path:** `readmenator/_documentation.py`
**File Doc:** *KNOWLEDGE_BASE.md generator: the human-facing architecture reference.  Renders the dashboard, layers, communities, CPG, taint, hotspots, cycles, security audit, Mermaid graph, and per-file reference sections.*

**Classes:**
- `DocumentationGenerator` (line 33) `class DocumentationGenerator` - *Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

Delegates graph rendering to MermaidRenderer and handles the
Markdown layout: header metadata, Mermaid block, statistics dashboard,
god nodes, community analysis, surprising connections, architecture
layers, security audit, taint analysis, hotspots, dependency cycles,
change impact, architecture violations, suggested rules, CPG block,
ranking metadata, orphans, query recipes, and per-language architecture
sections with pluralised symbol kind headings.*

**Methods:**
- `__init__` (line 45) `def __init__(self, config)`
- `_ranking_version` (line 63) `def _ranking_version(self)`
- `_get_git_commit` (line 81) `def _get_git_commit()`
- `generate` (line 91) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)`
- `_apply_context_budget` (line 178) `def _apply_context_budget(self, content, nodes, edges, resolved_edges, analysis, analysis_v2, findings)`
- `_build_toc` (line 316) `def _build_toc(self, nodes, analysis, layers, findings, analysis_v2, is_truncated, ranked)`
- `_build_layers` (line 404) `def _build_layers(self, layers, nodes)`
- `_build_dashboard` (line 438) `def _build_dashboard(self, nodes, edges, resolved_edges)`
- `_build_god_nodes` (line 518) `def _build_god_nodes(self, analysis, ranked)`
- `_build_community_analysis` (line 546) `def _build_community_analysis(self, analysis, nodes)`
- `_build_surprising_connections` (line 579) `def _build_surprising_connections(self, analysis, nodes)`
- `_build_suggested_questions` (line 604) `def _build_suggested_questions(self, analysis)`
- `_build_ranked_context` (line 620) `def _build_ranked_context(self, ranked)`
- `_build_orphans` (line 666) `def _build_orphans(self, nodes, analysis_v2, ranked)` - *Build a section listing nodes with low coverage signals.*
- `_build_query_recipes` (line 716) `def _build_query_recipes(self)`
- `_build_taint_analysis` (line 758) `def _build_taint_analysis(self, analysis_v2)`
- `_build_hotspots` (line 793) `def _build_hotspots(self, analysis_v2, ranked)`
- `_build_dataflow_analysis` (line 831) `def _build_dataflow_analysis(self, analysis_v2)` - *Build the procedural dataflow findings section.*
- `_build_dependency_cycles` (line 862) `def _build_dependency_cycles(self, analysis_v2)`
- `_build_change_impact` (line 883) `def _build_change_impact(self, analysis_v2)`
- `_build_layer_violations` (line 908) `def _build_layer_violations(self, analysis_v2)`
- `_build_suggested_rules` (line 936) `def _build_suggested_rules(self, analysis_v2)`
- `_build_security_findings` (line 961) `def _build_security_findings(self, findings)`
- `_build_mermaid_section` (line 1008) `def _build_mermaid_section(self, graph_output, is_truncated)`
- `_build_uml_diagram` (line 1031) `def _build_uml_diagram(self, nodes, edges)`
- `_build_cpg_block` (line 1057) `def _build_cpg_block(self, nodes, edges, resolved_edges, analysis)`
- `_build_architecture_reference` (line 1083) `def _build_architecture_reference(self, nodes, edges)`

#### `_explain.py`
**Path:** `readmenator/_explain.py`
**File Doc:** *Score explanation and path decomposition for the ranking system.  Provides human-readable explanations of why a particular node ranks where it does, including score breakdown, strongest paths from seeds, and quality signal summary.*

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
**File Doc:** *Multi-format exporter for the readmenator knowledge graph.  Produces JSON (GraphRAG-ready node-link format), interactive HTML (vis.js standalone), and static SVG (matplotlib-based) outputs from the scanned nodes, edges, and optional analysis results.*

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
- `_community_color_map` (line 239) `def _community_color_map(self, analysis)` - *Build a node-to-color map based on community membership.*
- `_lighten` (line 257) `def _lighten(hex_color)` - *Lighten a hex color by 30% for border use.*
- `_render_html` (line 265) `def _render_html(self, vis_nodes, vis_edges, analysis, findings)` - *Render the full HTML document with vis.js.*
- `to_svg` (line 436) `def to_svg(self, nodes, edges, resolved_edges, analysis)` - *Generate a static SVG representation of the graph.

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
- `_render_truncated_svg` (line 554) `def _render_truncated_svg(self, total_nodes)` - *Render a minimal SVG with a truncation notice.*
- `_layout_spring` (line 569) `def _layout_spring(self, nodes, edges, node_map)` - *Compute a simple spring-layout for node positioning.

Implements a basic force-directed layout with repulsion
between all nodes and attraction along edges. Runs a fixed
number of iterations for determinism.*
- `to_graphml` (line 650) `def to_graphml(self, nodes, edges, resolved_edges, analysis)` - *Export the graph as GraphML (Gephi/yEd compatible).

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved-import edges.
    analysis: Optional analysis results for community data.

Returns:
    GraphML XML string.*
- `to_cypher` (line 727) `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings)` - *Export the graph as native Cypher CREATE statements.

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
- `to_obsidian` (line 832) `def to_obsidian(self, nodes, edges, output_dir, analysis)` - *Export the graph as an Obsidian vault with wikilinks.

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
- `_project` (line 498) `def _project(pos)`
- `_sev_span` (line 337) `def _sev_span(sev, count)`

#### `_gh_wiki.py`
**Path:** `readmenator/_gh_wiki.py`
**File Doc:** *GitHub wiki publisher: mirrors generated knowledge into the repository wiki.  Turns the readmenator wiki, agent docs, recipes, and KNOWLEDGE_BASE.md into flat GitHub wiki pages (Home, _Sidebar, _Footer), rewrites relative markdown links to wiki page names, and turns backticked project paths into commit-pinned source permalinks. Publishing clones ``<repo>.wiki.git``, replaces only pages it generated before (tracked in a state file), commits, and pushes. It is opt-in, never runs during analysis, and shells out with argument lists only (no shell).*

**Classes:**
- `WikiPublishResult` (line 39) `class WikiPublishResult` - *Outcome of a GitHub wiki publish.

Attributes:
    pages: Wiki page file names written.
    removed: Previously generated page files deleted as stale.
    pushed: Whether a commit was pushed to the wiki remote.
    remote: Wiki remote URL used, empty in dry runs without a remote.
    output_dir: Directory holding the rendered pages.
    message: Human-readable status line.*
- `GitHubWikiPublisher` (line 59) `class GitHubWikiPublisher` - *Renders and publishes generated documentation to a GitHub wiki.*

**Methods:**
- `__init__` (line 62) `def __init__(self, config, runner)` - *Store configuration and the subprocess runner (injectable for tests).

Args:
    config: Central settings for paths, page names, and git options.
    runner: Callable compatible with ``subprocess.run``.*
- `page_name` (line 72) `def page_name(self, rel_path)` - *Map a generated markdown path to its flat GitHub wiki page name.

Args:
    rel_path: Project-relative markdown path.

Returns:
    Wiki page name without extension.*
- `collect_sources` (line 96) `def collect_sources(self, project_root)` - *List project-relative markdown sources to publish, sorted.

Args:
    project_root: Project root holding generated outputs.

Returns:
    Relative POSIX paths of regular, non-symlink markdown files.*
- `_blob_base` (line 121) `def _blob_base(self, remote, commit)` - *Return the web URL prefix for commit-pinned source links, or empty.*
- `rewrite` (line 129) `def rewrite(self, text, rel_path, names, project_root, blob_base)` - *Rewrite relative doc links to wiki pages and paths to source permalinks.

Args:
    text: Markdown content of one source document.
    rel_path: Project-relative path of that document.
    names: Mapping of published relative paths to page names.
    project_root: Project root used to check that paths exist.
    blob_base: Commit-pinned blob URL prefix, empty to skip.

Returns:
    Markdown ready for the GitHub wiki.*
- `render` (line 179) `def render(self, project_root, remote)` - *Render every wiki page, including sidebar and footer.

Args:
    project_root: Project root holding generated outputs.
    remote: Main repository remote used for source permalinks.

Returns:
    Mapping of wiki file name to markdown content.*
- `_fallback_home` (line 205) `def _fallback_home(self, project_name)` - *Return a Home page used when the readmenator wiki was not generated.*
- `_sidebar` (line 213) `def _sidebar(self, names)` - *Return the navigation sidebar grouping pages by origin.*
- `_footer` (line 241) `def _footer(git)` - *Return the footer stamping the source commit and regeneration command.*
- `wiki_remote` (line 249) `def wiki_remote(self, project_root)` - *Resolve the wiki remote from config, ``gh``, or the git origin.

Args:
    project_root: Project root of the main repository.

Returns:
    The ``.wiki.git`` remote URL, or empty string when unknown.*
- `_origin` (line 267) `def _origin(self, project_root)` - *Return the main repository URL via ``gh`` or ``git remote``.*
- `_call` (line 279) `def _call(self, command, cwd)` - *Run a command without a shell and return stdout, or None on failure.*
- `_write_pages` (line 293) `def _write_pages(self, target, pages)` - *Write pages, delete stale previously generated ones, and record state.*
- `publish` (line 313) `def publish(self, project_root, dry_run)` - *Render pages and push them to the GitHub wiki (or a local folder).

Args:
    project_root: Project root holding generated outputs.
    dry_run: Render into GH_WIKI_DRY_RUN_DIR without any git calls.

Returns:
    WikiPublishResult describing what was written and pushed.*
- `link` (line 151) `def link(match)` - *Replace one relative markdown link when its target is published.*
- `permalink` (line 164) `def permalink(match)` - *Link a backticked project file (optionally with a line) to source.*

#### `_gitmeta.py`
**Path:** `readmenator/_gitmeta.py`
**File Doc:** *Read-only git metadata for freshness stamps on generated documents.  Reads ``.git`` plumbing files directly (no subprocess, no network) so agents can compare a generated MANIFEST against ``git rev-parse HEAD`` and know whether the knowledge base is stale before trusting it.*

**Functions:**
- `_read_small` (line 19) `def _read_small(path)` - *Return the stripped text of a small regular file, or empty string.

Args:
    path: File to read.

Returns:
    File contents, or empty string when missing, a symlink, or oversized.*
- `_git_dir` (line 38) `def _git_dir(root)` - *Locate the git directory for a work tree, following gitdir files.

Args:
    root: Work tree root.

Returns:
    The git directory path, or None when the root is not a repository.*
- `_packed_ref` (line 59) `def _packed_ref(git_dir, ref)` - *Look up a ref in packed-refs, honoring worktree commondir.

Args:
    git_dir: Git directory of the work tree.
    ref: Fully qualified ref name.

Returns:
    The commit hash, or empty string.*
- `read_git_head` (line 84) `def read_git_head(project_root)` - *Return the current commit and branch of a project, when available.

Args:
    project_root: Work tree root directory.

Returns:
    Mapping with ``commit`` and ``branch`` keys (empty strings when
    unknown or not a git repository).*

#### `_hotspots.py`
**Path:** `readmenator/_hotspots.py`
**File Doc:** *Hotspot, dependency cycle, and change impact analysis.  Scores files by complexity plus centrality, finds import cycles with DFS, and measures transitive dependents with bounded BFS.*

**Classes:**
- `HotspotAnalyzer` (line 22) `class HotspotAnalyzer` - *Hotspot detection, cycle analysis, and change impact analysis.

Hotspots are files with high complexity (many symbols) and high
centrality (many connections). Cycle detection finds circular
dependencies in the resolved import graph. Change impact analysis
computes transitive-dependent lists for every file.*

**Methods:**
- `__init__` (line 31) `def __init__(self, config)`
- `analyze_hotspots` (line 34) `def analyze_hotspots(self, nodes, edges, resolved_edges)` - *Rank files by combined complexity and centrality scores.

Complexity is normalised symbol count. Centrality is normalised
connection count (in-degree + out-degree). The combined score
uses configured weights.*
- `detect_cycles` (line 90) `def detect_cycles(self, nodes, resolved_edges)` - *Detect cycles in the resolved import graph using DFS.

Uses Tarjan's algorithm variant with three-colour DFS to find
all elementary cycles. Returns each cycle as a DependencyCycle.*
- `analyze_change_impact` (line 155) `def analyze_change_impact(self, nodes, resolved_edges)` - *Compute change impact for every file in the project.

For each file, finds all files that would be affected if it
changed (direct and transitive dependents via reverse import
graph traversal).*
- `_dfs_visit` (line 114) `def _dfs_visit(current)`
- `_record_cycle` (line 125) `def _record_cycle(start, end)`

#### `_layer_rules.py`
**Path:** `readmenator/_layer_rules.py`
**File Doc:** *Architecture layer rule engine: forbidden and warning edges between layers.*

**Classes:**
- `LayerRuleEngine` (line 11) `class LayerRuleEngine` - *Architectural layer violation detection engine.

Defines a set of permitted and forbidden layer-to-layer import
rules. Scans all resolved import edges and flags violations
where one layer imports from another in a way that violates
the architecture.*

**Methods:**
- `__init__` (line 36) `def __init__(self, config)`
- `detect_violations` (line 39) `def detect_violations(self, nodes, edges, resolved_edges, layers)` - *Detect architectural layer violations.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.
    resolved_edges: Optional resolved import edges.
    layers: Dict mapping node_id to layer name. If None, imports
        _layers.LayerDetector for automatic detection.

Returns:
    List of LayerViolation instances.*
- `violation_summary` (line 111) `def violation_summary(violations)` - *Summarise violations by severity.*

#### `_layers.py`
**Path:** `readmenator/_layers.py`
**File Doc:** *Architectural layer detection for the readmenator knowledge graph.  Infers architectural layers (presentation, business logic, data access, infrastructure, testing, configuration) from file paths, naming conventions, and import patterns. No external API calls.*

**Classes:**
- `LayerDetector` (line 17) `class LayerDetector` - *Detects architectural layers in a codebase.

Assigns each file to a layer based on path patterns, naming
conventions, and imported frameworks. Returns a mapping that
can enrich documentation and analysis. No config dependency.*

**Methods:**
- `detect` (line 83) `def detect(self, nodes, edges)` - *Assign each file node to an architectural layer.

Args:
    nodes: Scanned file nodes.
    edges: Import edges.

Returns:
    Dict mapping node_id to layer name.*
- `_path_tokens` (line 108) `def _path_tokens(cls, node_id)` - *Split a path into lowercase word tokens, honoring camelCase.*
- `_pattern_hits` (line 114) `def _pattern_hits(cls, pattern, tokens, joined)` - *Return whether a layer pattern matches path tokens as a whole word.

Short patterns (``ui``, ``di``, ``api``) must equal a token;
longer ones also match token prefixes (``tests``, ``views``).
Multi-word patterns match underscore-joined token runs.*
- `_import_roots` (line 128) `def _import_roots(cls, imports)` - *Return the top-level module names of raw import strings.*
- `_classify_file` (line 138) `def _classify_file(self, node, edges, imports)` - *Classify a single file into an architectural layer.

Path words score one point each, framework imports three, and
test-file naming five. Layers in _EVIDENCE_REQUIRED_LAYERS only
accept framework points when the path already points there, so a
CLI that imports ``unittest`` to run the suite stays production code.*
- `layer_summary` (line 189) `def layer_summary(layers)` - *Count files per layer.

Args:
    layers: Mapping from detect().

Returns:
    Dict of layer_name -> file_count.*

#### `_linter.py`
**Path:** `readmenator/_linter.py`
**File Doc:** *Architecture linter for the readmenator knowledge graph.  Evaluates files against predefined architectural rules: file length limits, cross-layer import violations, and circular dependency detection. All rules are deterministic and token-free.*

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
**File Doc:** *MCP (Model Context Protocol) stdio server for ReadMenator.  Exposes the full codebase knowledge graph as MCP tools and resources, allowing AI agents to query structural information without parsing KNOWLEDGE_BASE.md as text. Each query costs ~50-200 tokens vs 2000-8000+ tokens of reading the full KB file.  Tools: readmenator.summary       — codebase overview (files, symbols, langs) readmenator.query         — free-text symbol/file search readmenator.explain       — detailed symbol explanation readmenator.path          — dependency chain between two symbols readmenator.findings      — security findings readmenator.taint         — taint propagation analysis readmenator.hotspots      — hotspot analysis readmenator.cycles        — dependency cycles readmenator.communities   — community detection readmenator.layers        — architectural layers readmenator.layer_violations — layer rule violations readmenator.rebuild       — regenerate KNOWLEDGE_BASE.md readmenator.update        — incremental update (SHA256 cache) readmenator.export_json   — export graph.json readmenator.security_summary — security audit summary  Resources: readmenator://summary     — structured JSON summary readmenator://graph       — graph data (nodes + edges) readmenator://file/{path} — file details readmenator://symbol/{name} — symbol details readmenator://findings    — security findings*

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
**File Doc:** *Mermaid graph renderer with intelligent pruning.  Converts the internal Node/Edge graph into a Mermaid flowchart (string) suitable for embedding in Markdown. Handles node limits, deduplication, CSS-like class styling, internal import edges, and community subgraphs.*

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
**File Doc:** *Data model types for the readmenator knowledge graph.  Defines the core entity types -- Symbol, Node, Edge -- plus a utility function for pluralising symbol kind labels and a helper for constructing community analysis results. Every parser, scanner, renderer, and query engine depends on these definitions.*

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
    layer_violations: List of layer violations.
    dataflow_issues: List of procedural dataflow findings.*
- `DataflowIssue` (line 307) `class DataflowIssue` - *A procedural intra-function dataflow finding.

Attributes:
    file_path: Relative path of the file containing the issue.
    function: Name of the enclosing function.
    line: One-based line number of the suspicious operation.
    kind: Issue kind (UNINIT_USE, DEAD_STORE, UNCHECKED_ALLOC).
    variable: Name of the involved local variable.
    description: Human-readable explanation of the suspicion.
    confidence: Confidence tier (always INFERRED for heuristics).*
- `LinterViolation` (line 330) `class LinterViolation` - *A violation detected by the architecture linter.

Attributes:
    file_path: Relative path of the file containing the violation.
    rule_id: Unique identifier for the linter rule (e.g. "ARC001").
    severity: Severity level (error, warning, info).
    message: Human-readable description of the violation.*
- `DeadCodeReport` (line 347) `class DeadCodeReport` - *A dead code symbol identified by the stripper.

Attributes:
    file_path: Relative path of the file containing the symbol.
    symbol_name: Name of the dead symbol.
    symbol_type: Type of symbol (function, class, method, etc.).
    recommendation: Recommended action (MOVE_TO_TRASH, REVIEW, KEEP).*
- `RefactoringAction` (line 364) `class RefactoringAction` - *A single refactoring action within a plan.

Attributes:
    action_type: Type of action (EXTRACT_CLASS, EXTRACT_FUNCTION, MOVE_SYMBOL).
    source_file: The file to refactor.
    start_line: Start line of the code range to extract.
    end_line: End line of the code range to extract.
    target_file: The new file to create (for EXTRACT actions).
    description: Human-readable description of the action.*
- `RefactoringPlan` (line 385) `class RefactoringPlan` - *A complete refactoring plan for a monolithic file.

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
**File Doc:** *AnalyzerFactory (lazy component construction) and DeepAnalysisRunner.  Decouples the application orchestrator from concrete analyzers and runs the v2 analyses (taint, cycles, impact, hotspots, rules, layers, dataflow).*

**Classes:**
- `AnalyzerFactory` (line 49) `class AnalyzerFactory` - *Lazy factory for all readmenator analyzer and generator instances.

Decouples the application orchestrator from the concrete
instantiation of analysis modules. Each component is created
on first access and cached for the lifetime of the factory.*
- `DeepAnalysisRunner` (line 292) `class DeepAnalysisRunner` - *Orchestrates the extended V2 analysis pipeline.

Runs taint propagation, hotspot detection, cycle detection,
change impact, layer violations, and rule generation as a
coordinated batch. Isolated from the main app to reduce
coupling in the primary orchestration layer.*

**Methods:**
- `__init__` (line 57) `def __init__(self, config)`
- `scanner` (line 88) `def scanner(self)`
- `generator` (line 94) `def generator(self)`
- `analyzer` (line 100) `def analyzer(self)`
- `security` (line 106) `def security(self)`
- `exporter` (line 112) `def exporter(self)`
- `taint` (line 118) `def taint(self)`
- `dataflow` (line 124) `def dataflow(self)` - *Return the lazily initialised dataflow analyzer.*
- `hotspots` (line 131) `def hotspots(self)`
- `layer_rules` (line 137) `def layer_rules(self)`
- `rule_gen` (line 143) `def rule_gen(self)`
- `sarif` (line 149) `def sarif(self)`
- `cpg` (line 155) `def cpg(self)`
- `layer_detector` (line 164) `def layer_detector(self)`
- `uml` (line 170) `def uml(self)`
- `wiki` (line 176) `def wiki(self)` - *Return the lazily initialised agent wiki generator.*
- `readme_injector` (line 183) `def readme_injector(self)`
- `agent_injector` (line 193) `def agent_injector(self)`
- `gh_wiki` (line 203) `def gh_wiki(self)` - *Return the lazily initialised GitHub wiki publisher.*
- `agent_output` (line 210) `def agent_output(self)`
- `diagram_builder` (line 216) `def diagram_builder(self)` - *Return the lazily initialised system map builder.*
- `diagram_renderer` (line 223) `def diagram_renderer(self)` - *Return the lazily initialised interactive map renderer.*
- `diagram_validator` (line 230) `def diagram_validator(self)` - *Return the lazily initialised system map validator.*
- `diagram_publisher` (line 237) `def diagram_publisher(self)` - *Return the lazily initialised documentation site publisher.*
- `vis_renderer` (line 244) `def vis_renderer(self)` - *Return the lazily initialised vis.js network renderer.*
- `video` (line 251) `def video(self)` - *Return the lazily initialised cinematic video renderer.*
- `build_typed_graph` (line 257) `def build_typed_graph(self, nodes, edges, resolved_edges)`
- `make_ranker` (line 267) `def make_ranker(self, typed_graph)` - *Create a CompositeRanker for the given typed graph.*
- `last_category` (line 284) `def last_category(self)`
- `last_typed_graph` (line 288) `def last_typed_graph(self)`
- `__init__` (line 301) `def __init__(self, factory)`
- `run` (line 304) `def run(self, nodes, edges, resolved_edges, layers, content_map)`

#### `_projections.py`
**Path:** `readmenator/_projections.py`
**File Doc:** *Functors and projections for the readmenator code category.  Defines projection functors that preserve structure but change the point of view: F_docs (code -> documentation), F_risk (code -> risk), and view-based projections for architecture, execution, quality, and change impact analysis.*

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

#### `_purpose.py`
**Path:** `readmenator/_purpose.py`
**File Doc:** *Purpose extraction shared by every agent-facing document generator.  Turns raw file and symbol docstrings into one clean, bounded sentence that tells a reader what a file is for. Banner rules, SPDX headers, encoding cookies, and bare file names are rejected; files without a module docstring fall back to the docstring of their primary symbol so agent indexes never show an empty purpose when the code explains itself.*

**Functions:**
- `is_garbage_doc` (line 26) `def is_garbage_doc(text)` - *Return True for doc lines that carry no purpose signal.

Args:
    text: One doc line.

Returns:
    Whether the line is too short, an encoding cookie, or symbol noise.*
- `clean_purpose` (line 43) `def clean_purpose(text)` - *Return the purpose signal of a doc first line, or an empty string.

Args:
    text: First line of a file or symbol docstring.

Returns:
    The line without banners, SPDX tags, and leading file names.*
- `escape_cell` (line 66) `def escape_cell(text)` - *Escape markdown table breaking characters in one line of text.

Args:
    text: Arbitrary text destined for a table cell.

Returns:
    Single-line text with pipes escaped.*
- `truncate_words` (line 78) `def truncate_words(text, max_chars)` - *Truncate text at a word boundary and mark the cut with an ellipsis.

Args:
    text: Text to shorten.
    max_chars: Maximum length of the returned string.

Returns:
    The original text when short enough, otherwise a word-aligned prefix.*
- `first_sentence` (line 98) `def first_sentence(doc)` - *Return the first clean sentence of the first meaningful paragraph.

Args:
    doc: Full docstring text.

Returns:
    One sentence with whitespace collapsed, or an empty string.*
- `_primary_symbol` (line 116) `def _primary_symbol(symbols)` - *Pick the documented symbol that best represents a file.

Public symbols outrank private ones and type-like kinds outrank
functions; ties fall back to source order.

Args:
    symbols: Symbols extracted from one file.

Returns:
    The representative documented symbol, or None.*
- `file_purpose` (line 140) `def file_purpose(node, max_chars)` - *Return a bounded one-sentence purpose for a file node.

Args:
    node: Scanned file node.
    max_chars: Maximum characters of the returned purpose.

Returns:
    Module doc sentence, else ``Symbol: sentence`` from the primary
    documented symbol, else an empty string.*

#### `_query.py`
**Path:** `readmenator/_query.py`
**File Doc:** *Query engine for the readmenator knowledge base.  Supports natural-language-like search (``query``), symbol explanation (``explain``), dependency-path tracing (``find_path``), ranked queries via PageRank/PPR integration (``ranked_query``), and a concise codebase overview (``summary``). All queries operate on an in-memory index built from the scanned Node/Edge list.*

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
**File Doc:** *PageRank, Personalized PageRank, HITS, and composite scoring.  Provides typed-graph-aware ranking for the readmenator knowledge graph. Global PageRank measures structural authority; Personalized PageRank measures query-specific relevance; HITS separates authorities from hubs; composite scoring combines multiple quality signals into a single explainable rank.*

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
**File Doc:** *Injects a knowledge base section into the project README (Markdown or RST).*

**Classes:**
- `ReadmeInjector` (line 70) `class ReadmeInjector` - *Injects a link to KNOWLEDGE_BASE.md into the project README.

Detects the project's README file, checks if injection is already
present, and appends a descriptive section about the knowledge base
so that both human developers and AI agents know it exists.*

**Methods:**
- `__init__` (line 78) `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)`
- `inject` (line 88) `def inject(self, project_root)`
- `_extract_current_injection` (line 117) `def _extract_current_injection(content)`
- `_remove_old_injection` (line 126) `def _remove_old_injection(content)`
- `remove` (line 136) `def remove(self, project_root)`
- `_find_readme` (line 165) `def _find_readme(root)`
- `_build_injection` (line 172) `def _build_injection(self, suffix)`

#### `_refactorizer.py`
**Path:** `readmenator/_refactorizer.py`
**File Doc:** *Monolithic file refactoring planner for the readmenator knowledge graph.  Identifies large files exceeding configurable thresholds and generates deterministic refactoring plans based on symbol extraction and cohesive cluster detection. Never auto-executes; only produces plans.*

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
**File Doc:** *Import path resolver for the readmenator knowledge graph.  Maps raw import strings (e.g. ``"os"``, ``"../utils"``, ``"java.util.List"``) to actual file node IDs within the scanned project so that dependency- tracing operations work on concrete files rather than opaque strings.*

**Classes:**
- `ImportResolver` (line 18) `class ImportResolver` - *Resolves raw import strings to project file paths.

Uses heuristics tuned to each language's import conventions:
Python dots to slashes, Java dots to directory separators,
relative-path resolution, and extensionless module detection.*

**Methods:**
- `__init__` (line 61) `def __init__(self, file_ids, root, extensions, include_dirs)` - *Initialise the resolver with all known file paths.

Args:
    file_ids: List of relative file paths from the scan.
    root: Root directory for relative-path resolution.
    extensions: Known source extensions, defaults to Config.
    include_dirs: Extra include search dirs (``-I`` style).*
- `_build_stem_index` (line 83) `def _build_stem_index(self, file_ids)` - *Map file stems (without extension) to their full paths.*
- `_build_dir_index` (line 93) `def _build_dir_index(self, file_ids)` - *Map directory paths to the files they contain.*
- `resolve` (line 110) `def resolve(self, import_str, source_file)` - *Resolve an import string to a concrete project file path.

Args:
    import_str: The raw import string from the parser.
    source_file: The file that contains the import (for relative resolution).

Returns:
    Matching file node ID or ``None`` if no match found.*
- `resolve_all` (line 163) `def resolve_all(self, import_str, source_file)` - *Resolve *import_str* to all possible matching project file paths.

Args:
    import_str: The raw import string.
    source_file: The file that contains the import.

Returns:
    List of matching file node IDs (may be empty).*
- `_resolve_include_dirs` (line 179) `def _resolve_include_dirs(self, import_str)` - *Resolve *import_str* against configured ``-I`` include dirs.

Args:
    import_str: Raw header path without ``sys:`` prefix.

Returns:
    Matching file node ID or ``None``.*
- `_resolve_relative` (line 199) `def _resolve_relative(self, import_str, source_file)` - *Resolve a relative import (starts with ``.`` or ``..``).*
- `_resolve_verbatim` (line 217) `def _resolve_verbatim(self, import_str, source_file)` - *Resolve a path-like import verbatim against the source directory.

Covers quoted C-family includes such as ``"utils.h"`` or
``"lib/net.h"`` which name a project file relative to the
including file.*
- `_resolve_extensionless` (line 235) `def _resolve_extensionless(self, import_str, source_file)` - *Resolve a bare module name by appending known extensions.*
- `_resolve_directory_init` (line 244) `def _resolve_directory_init(self, import_str, source_file)` - *Resolve as a package directory with __init__ or index file.*
- `_resolve_root_package` (line 254) `def _resolve_root_package(self, import_str)` - *Resolve a bare top-level name to a root package ``__init__.py``.

Python prefers a package directory over a same-named module, so
``import pkg`` must map to ``pkg/__init__.py`` even when a
``pkg.py`` launcher shim exists; stem matching would otherwise
pick the shim and fabricate dependency cycles.*
- `_resolve_module_dotpath` (line 269) `def _resolve_module_dotpath(self, import_str)` - *Resolve a dotted module path (Python/Java convention).*
- `_resolve_suffix_match` (line 291) `def _resolve_suffix_match(self, import_str)` - *Match a slash-qualified include against project path suffixes.

Covers include-directory style references such as
``"kernel/mm.h"`` mapping to ``"include/kernel/mm.h"``. Only
unambiguous matches resolve.*
- `_resolve_basename_match` (line 306) `def _resolve_basename_match(self, import_str)` - *Match by exact file basename including extension.

Covers the classic C pair pattern where ``kernel.h`` is
included but ``kernel.c`` shares its stem: stem matching
stays ambiguous while the basename is unique. Only
unambiguous matches resolve.*
- `_resolve_stem_match` (line 324) `def _resolve_stem_match(self, import_str)` - *Match by file stem only (last resort).*
- `_strip_extension` (line 333) `def _strip_extension(self, name)` - *Remove a trailing known source extension from a file name.

Args:
    name: Base file name which may carry an extension.

Returns:
    The file stem used for stem index lookups.*

#### `_rule_gen.py`
**Path:** `readmenator/_rule_gen.py`
**File Doc:** *Suggested linting rule generator producing Semgrep YAML from detected antipatterns.*

**Classes:**
- `RuleGenerator` (line 14) `class RuleGenerator` - *Generates suggested linting and security rules from code patterns.

Analyses the scanned codebase for repeated patterns that suggest
project-specific linting rules: bare except clauses, repeated
type annotations, common security antipatterns, and naming
convention violations. Outputs Semgrep YAML rules to a directory.*

**Methods:**
- `__init__` (line 90) `def __init__(self, config)`
- `generate` (line 94) `def generate(self, nodes, content_map)` - *Generate suggested rules by scanning code patterns.

Args:
    nodes: Scanned file nodes with symbols.
    content_map: Optional mapping of file paths to their source content
        for deeper pattern matching.

Returns:
    List of SuggestedRule instances.*
- `write_rules` (line 122) `def write_rules(self, rules, output_dir)` - *Write suggested rules to Semgrep YAML files in output_dir.

Returns the number of rule files written.*
- `_group_by_language` (line 161) `def _group_by_language(self, nodes)` - *Group nodes by their language extension.*
- `_analyze_language` (line 171) `def _analyze_language(self, lang, nodes, content_map)` - *Analyze a single language group for rule suggestions.*
- `_detect_antipatterns` (line 204) `def _detect_antipatterns(self, nodes, content_map)` - *Detect known antipatterns across all files.*
- `_infer_language_for_rule` (line 250) `def _infer_language_for_rule(rule_id)` - *Infer target language for a built-in antipattern rule.*
- `_next_rule_id` (line 260) `def _next_rule_id(self)` - *Generate the next rule identifier.*

#### `_sarif.py`
**Path:** `readmenator/_sarif.py`
**File Doc:** *SARIF v2.1.0 exporter for security findings (GitHub Code Scanning compatible).*

**Classes:**
- `SarifExporter` (line 11) `class SarifExporter` - *Exports security findings to the SARIF standard format.

SARIF is an OASIS standard format for static analysis tool output.
This exporter produces SARIF v2.1.0 JSON compatible with GitHub
Code Scanning, VS Code SARIF viewer, and other SARIF consumers.*

**Methods:**
- `__init__` (line 30) `def __init__(self, privacy_mode)`
- `export` (line 33) `def export(self, findings, project_name)` - *Generate a SARIF v2.1.0 JSON string from security findings.

Args:
    findings: List of SecurityFinding instances.
    project_name: Name of the scanned project for metadata.

Returns:
    SARIF JSON string.*
- `_build_rule` (line 82) `def _build_rule(self, finding)` - *Build a SARIF reportingDescriptor (rule) object.*
- `_build_result` (line 106) `def _build_result(self, finding, rule_index)` - *Build a SARIF result object for a single finding.*

#### `_scanner.py`
**Path:** `readmenator/_scanner.py`
**File Doc:** *Secure polyglot directory traversal and file analysis.  The scanner walks a directory tree, applies security and size checks, resolves each supported file through ParserFactory, and returns a flat list of Node and Edge objects that form the knowledge graph.*

**Classes:**
- `PolyglotScanner` (line 28) `class PolyglotScanner` - *Recursive directory scanner with security and size guards.

Rejects symlinks, enforces file-size and directory-depth limits,
skips ignored directories, and silently catches parse errors
so a single misbehaving file never breaks the full scan.

Supports privacy mode (strips snippets and docstrings) and
gitignore-aware scanning for more accurate project coverage.*

**Methods:**
- `__init__` (line 39) `def __init__(self, config)` - *Initialise the scanner with application configuration.

Args:
    config: Settings including ignore dirs, size limits, etc.*
- `_is_ignored` (line 50) `def _is_ignored(self, path)` - *Return ``True`` if any path component matches IGNORE_DIRS.*
- `_is_generated` (line 57) `def _is_generated(self, rel_path)` - *Return ``True`` for artifacts readmenator itself wrote into the project.

Rescanning its own output (agent docs, wiki, rules, maps, refactor
scripts) would feed generated noise back into the graph and skew
indexes, centrality, and purposes on every rebuild.

Args:
    rel_path: Path relative to the scan root.

Returns:
    Whether the path belongs to a readmenator-generated artifact.*
- `_load_gitignore` (line 83) `def _load_gitignore(self, root)` - *Parse .gitignore patterns using regex (no external deps).*
- `_gitignore_glob_to_regex` (line 105) `def _gitignore_glob_to_regex(pattern)` - *Convert a .gitignore glob pattern to a regex pattern.*
- `_is_gitignored` (line 145) `def _is_gitignored(self, rel_path)` - *Check if a relative path matches any .gitignore pattern.*
- `_validate_path_security` (line 154) `def _validate_path_security(self, path)` - *Reject symlinks and files exceeding MAX_FILE_SIZE_MB.*
- `_check_directory_depth` (line 167) `def _check_directory_depth(self, path, root)` - *Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.*
- `_extract_file_doc` (line 175) `def _extract_file_doc(self, content)` - *Extract a file-level docstring from the first lines of a source file.

Walks the first FILE_HEADER_MAX_LINES lines looking for a contiguous
block of comments, a Python module docstring, or a shebang followed
by comments. Returns the concatenated comment text.

Args:
    content: Raw file content as a string.

Returns:
    Extracted file-level docstring or empty string.*
- `_emit_progress` (line 251) `def _emit_progress(self, count)` - *Emit a progress message every PROGRESS_REPORT_BATCH files.

Args:
    count: Number of files scanned so far.*
- `scan` (line 261) `def scan(self, root)` - *Walk *root* recursively and produce (nodes, edges) for the graph.

Security checks (symlinks, size, depth, ignore dirs) are applied
per file. Parse failures are silently caught so a single broken
file never blocks the rest of the scan.

Returns:
    A tuple of (list of Node, list of Edge). Edges represent
    ``imports`` relationships between scanned files.*
- `scan_with_content` (line 275) `def scan_with_content(self, root)` - *Scan and also return raw file contents for deeper analysis.

Returns:
    Tuple of (nodes, edges, content_map) where content_map maps
    node_id to raw file content.*
- `_scan_impl` (line 286) `def _scan_impl(self, root)` - *Internal scan implementation returning nodes, edges, and content.*

#### `_security.py`
**Path:** `readmenator/_security.py`
**File Doc:** *Pattern-based static security analysis for the readmenator knowledge graph.  Scans source files across all supported languages for dangerous patterns: command injection, SQL injection, XSS, weak crypto, unsafe deserialization, hardcoded secrets, and more. Pure regex-based, zero external dependencies.  Rules are loaded from readmenator-rules/_security_rules.yml at runtime, eliminating hardcoded patterns from source code (per the externalization principle). Falls back to built-in rules if the YAML file is not present.*

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
- `fix_hint_for` (line 620) `def fix_hint_for(finding)` - *Return a one-line remediation hint for a security finding.

Looks up the finding CWE in the guidance map and falls back to a
generic least-privilege hint for unmapped identifiers.

Args:
    finding: Security finding with a CWE identifier string.

Returns:
    One-line remediation hint without markdown formatting.*
- `__init__` (line 496) `def __init__(self, config)`
- `_resolve_rules` (line 500) `def _resolve_rules(self)` - *Resolve rules: prefer YAML, fall back to built-in.*
- `_meets_threshold` (line 509) `def _meets_threshold(self, severity)`
- `scan` (line 513) `def scan(self, root)`
- `_validate_path` (line 555) `def _validate_path(self, path, root)`
- `summary` (line 572) `def summary(self, findings)`

#### `_taint.py`
**Path:** `readmenator/_taint.py`
**File Doc:** *Taint propagation analysis of dangerous imports through the resolved import graph.*

**Classes:**
- `TaintAnalyzer` (line 12) `class TaintAnalyzer` - *Propagation-based taint analysis over the resolved import graph.

Identifies files that import known-dangerous modules or functions
(sources) and traces how that danger propagates through the import
graph to files that never directly import the dangerous module
but receive taint through transitive dependencies.*

**Methods:**
- `__init__` (line 73) `def __init__(self, config)`
- `analyze` (line 77) `def analyze(self, nodes, edges, resolved_edges)` - *Run taint propagation analysis on the codebase.

Scans all nodes for direct dangerous imports, then propagates
taint through the resolved import graph. Returns all discovered
taint paths from sources to sinks.*
- `_find_direct_sources` (line 136) `def _find_direct_sources(self, nodes, edges)` - *Find files that directly import known-dangerous modules.*
- `_propagate` (line 162) `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` - *BFS propagation from source through the import graph.*
- `_build_forward_graph` (line 213) `def _build_forward_graph(nodes, resolved_edges)` - *Build a forward-directed import graph from resolved edges.*

#### `_uml.py`
**Path:** `readmenator/_uml.py`
**File Doc:** *UML class diagram renderer (Mermaid classDiagram) and 12-language stub generator.*

**Classes:**
- `UmlGenerator` (line 34) `class UmlGenerator`

**Methods:**
- `_get_code_generator` (line 172) `def _get_code_generator(language)`
- `_type_map_py_to_target` (line 190) `def _type_map_py_to_target(target, py_type_hint)`
- `_generate_cpp` (line 233) `def _generate_cpp(class_symbols, nodes, edges)`
- `_cpp_params` (line 259) `def _cpp_params(params)`
- `_generate_java` (line 274) `def _generate_java(class_symbols, nodes, edges)`
- `_java_params` (line 301) `def _java_params(params)`
- `_generate_csharp` (line 316) `def _generate_csharp(class_symbols, nodes, edges)`
- `_cs_params` (line 345) `def _cs_params(params)`
- `_generate_python` (line 360) `def _generate_python(class_symbols, nodes, edges)`
- `_generate_go` (line 395) `def _generate_go(class_symbols, nodes, edges)`
- `_generate_rust` (line 422) `def _generate_rust(class_symbols, nodes, edges)`
- `_generate_php` (line 448) `def _generate_php(class_symbols, nodes, edges)`
- `_generate_kotlin` (line 476) `def _generate_kotlin(class_symbols, nodes, edges)`
- `_generate_scala` (line 496) `def _generate_scala(class_symbols, nodes, edges)`
- `_generate_swift` (line 518) `def _generate_swift(class_symbols, nodes, edges)`
- `_generate_dart` (line 547) `def _generate_dart(class_symbols, nodes, edges)`
- `_generate_ruby` (line 567) `def _generate_ruby(class_symbols, nodes, edges)`
- `_safe_name` (line 588) `def _safe_name(name)`
- `_extract_params` (line 592) `def _extract_params(signature)`
- `__init__` (line 36) `def __init__(self, config)`
- `render_mermaid_class_diagram` (line 39) `def render_mermaid_class_diagram(self, nodes, edges)`
- `generate_code` (line 129) `def generate_code(self, nodes, edges, target_language)`
- `_sanitize_id` (line 153) `def _sanitize_id(raw)`
- `_find_node` (line 165) `def _find_node(nodes, node_id)`

#### `_video.py`
**Path:** `readmenator/_video.py`
**File Doc:** *Cinematic codebase overview video, general purpose.  Renders a short synthwave explainer for any project analysed by readmenator, in the visual language of the miniGCC self-host video (neon HUD panels, striped sun, scrolling grid, bloom, scanlines, chromatic text, glitch transitions). Every number on screen comes from a real scan: file/symbol/import counts, detected layers, god nodes, communities, the resolved import graph, per-file hash colors and top security findings.  Zero tokens: pure PIL frame drawing piped to ffmpeg. Optional dependency: when PIL or ffmpeg is missing the caller skips with a warning instead of failing the rebuild.*

**Classes:**
- `Backdrop` (line 236) `class Backdrop` - *Precomputed synthwave background with sun and CRT mask.*
- `CinematicVideoRenderer` (line 431) `class CinematicVideoRenderer` - *Builds and renders the general-purpose codebase overview video.*

**Functions:**
- `ease` (line 73) `def ease(x)` - *Smoothstep clamped to [0, 1].*
- `fmt_int` (line 79) `def fmt_int(n)` - *Group thousands with commas.*
- `mix` (line 84) `def mix(a, b, t)` - *Linear blend of two RGB colors.*
- `alpha` (line 89) `def alpha(c, a)` - *RGB color plus an alpha in [0, 1] as an RGBA tuple.*
- `hash_color` (line 94) `def hash_color(digest)` - *Neon color derived from a digest: the file fingerprint.*
- `short_label` (line 103) `def short_label(text, limit)` - *Truncate a label to a character budget without newlines.*
- `_panel` (line 111) `def _panel(cfg)` - *Main content panel fitted to the configured canvas.*
- `_caption_y` (line 116) `def _caption_y(cfg)` - *Y coordinate of the lower-third narration line.*
- `_graph_boxes` (line 121) `def _graph_boxes(cfg)` - *Graph panel plus telemetry side panel fitted to the canvas.*
- `_dna_boxes` (line 130) `def _dna_boxes(cfg)` - *DNA grid panel plus security side panel fitted to the canvas.*
- `_split_boxes` (line 139) `def _split_boxes(cfg)` - *Left content panel plus right detail panel fitted to the canvas.*
- `_verdict_badge` (line 148) `def _verdict_badge(d, box, text, fonts, lt, dur, col)` - *Pulsing verdict badge pinned to the bottom of a panel.*
- `_scan_cursor` (line 163) `def _scan_cursor(d, box, progress, col)` - *Vertical sweep line travelling across a panel.*
- `_code_tint` (line 172) `def _code_tint(line)` - *Single-color tint for a source line: comments dim, code bright.*
- `_packet_offset` (line 182) `def _packet_offset(a, b, k)` - *Deterministic phase offset for a packet travelling edge a->b.*
- `dependencies_available` (line 188) `def dependencies_available()` - *Check that PIL and ffmpeg exist for video rendering.*
- `resolve_fonts` (line 197) `def resolve_fonts()` - *Resolve monospace fonts through fontconfig with PIL fallback.*

**Methods:**
- `_img` (line 292) `def _img()` - *Import PIL Image lazily for optional-dependency support.*
- `draw_grid` (line 299) `def draw_grid(img, t, strength, bd)` - *Draw the scrolling perspective grid below the horizon.*
- `draw_sun` (line 319) `def draw_sun(img, a, bd, cy)` - *Paste the striped synthwave sun behind the horizon.*
- `post` (line 336) `def post(img, glitch, seed)` - *Apply bloom, scanlines, vignette and optional glitch.*
- `glitch_fx` (line 354) `def glitch_fx(img, amount, seed)` - *RGB split plus horizontal slice displacement.*
- `chroma_text` (line 377) `def chroma_text(img, xy, text, font, col, spread, anchor)` - *Draw text with red/cyan CRT chromatic aberration.*
- `hud_panel` (line 388) `def hud_panel(d, box, title, fonts, col)` - *Draw a translucent HUD panel with neon edge and corner brackets.*
- `draw_header` (line 401) `def draw_header(img, d, gt, total, project, act_label, fonts, width)` - *Draw the top strip with project title, act label and progress.*
- `draw_caption` (line 415) `def draw_caption(d, text, lt, dur, fonts, width, y)` - *Draw the lower-third narration line with typing effect.*
- `_render_frame_bytes` (line 752) `def _render_frame_bytes(fi)` - *Pool worker: draw one frame and return raw RGB bytes.*
- `_draw_frame` (line 757) `def _draw_frame(fi)` - *Draw one frame for the global render state.*
- `_scene_title` (line 785) `def _scene_title(img, d, lt, gt, sc)` - *Cold open with counting project stats and language chips.*
- `_scene_card` (line 820) `def _scene_card(img, d, lt, gt, sc)` - *Act interstitial card.*
- `_scene_layers` (line 834) `def _scene_layers(img, d, lt, gt, sc)` - *Animated horizontal bars for the 5-layer model with sweep cursor.*
- `_scene_gods` (line 859) `def _scene_gods(img, d, lt, gt, sc)` - *Ranked god nodes with the formula exposed plus real source preview.*
- `_scene_tree` (line 902) `def _scene_tree(img, d, lt, gt, sc)` - *The true dependency tree: BFS spanning tree grown from the hub file.*
- `_scene_communities` (line 963) `def _scene_communities(img, d, lt, gt, sc)` - *Community cards explaining why each group sticks together.*
- `_scene_graph` (line 1006) `def _scene_graph(img, d, lt, gt, sc)` - *The resolved import graph growing node by node, with live packets.*
- `_scene_dna` (line 1064) `def _scene_dna(img, d, lt, gt, sc)` - *Every file as a color, scanned live, with a zoom on the hub file.*
- `_scene_outro` (line 1119) `def _scene_outro(img, d, lt, gt, sc)` - *Closing summary with the measured numbers.*
- `_find` (line 201) `def _find(style)` - *Find one font file for a style, else None.*
- `__init__` (line 239) `def __init__(self, width, height)` - *Build the gradient sky, star field, sun and CRT mask.*
- `_sun` (line 277) `def _sun(self, r)` - *Build the striped synthwave sun sprite.*
- `collect` (line 436) `def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map)` - *Collect every number each scene draws, from real scan data.*
- `_build_dep_tree` (line 572) `def _build_dep_tree(self, node_by_id, link_set, god_names)` - *Grow a true dependency spanning tree with BFS from the hub file.*
- `build_scenes` (line 612) `def build_scenes(self, data)` - *Lay every scene on the global clock.*
- `graph_positions` (line 638) `def graph_positions(self, data, box)` - *Compute deterministic positions for graph nodes inside a box.*
- `tree_positions` (line 673) `def tree_positions(self, data, box)` - *Compute tidy tree positions for the BFS dependency tree.*
- `render_single_frame` (line 694) `def render_single_frame(self, data, frame_index)` - *Render one frame to raw RGB bytes without touching ffmpeg.*
- `render` (line 712) `def render(self, data, output_path)` - *Render all frames and encode to mp4, muxing music if configured.*

#### `_watcher.py`
**Path:** `readmenator/_watcher.py`
**File Doc:** *Filesystem watcher for auto-rebuilding the knowledge base.  Monitors the project directory for file changes and triggers automatic regeneration of KNOWLEDGE_BASE.md. Uses polling with configurable interval to avoid external dependencies.*

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

#### `_wiki.py`
**Path:** `readmenator/_wiki.py`
**File Doc:** *Deterministic agent wiki generator for readmenator.  Builds a navigable, progressively disclosed wiki on top of the scanned knowledge graph. The layout mirrors the Karpathy LLM Wiki Pattern used by graphify and second-brain (index plus one page per community plus machine-readable connections), but every page is synthesised deterministically from static analysis with zero LLM calls, zero tokens, and an honest confidence trail.  Output layout::  readmenator-wiki/ ├── index.md              # entry point: overview plus all links ├── community_<id>_<slug>.md  # one synthesis page per community ├── connections.json      # typed bridges with strength and confidence ├── queries.md            # suggested questions plus answer log └── REPORT.md             # honest audit: coverage, confidence, limits*

**Classes:**
- `WikiGenerator` (line 86) `class WikiGenerator` - *Generates the navigable agent wiki from scanned topology.*

**Functions:**
- `_is_garbage_purpose` (line 47) `def _is_garbage_purpose(text)` - *Return True for file-doc first lines that state no purpose.*
- `_slug` (line 55) `def _slug(text)` - *Return a filesystem-safe slug for community labels.*
- `existing_ids` (line 62) `def existing_ids(connections)` - *Return community id pairs already linked, to avoid duplicate edges.*
- `_display_names` (line 72) `def _display_names(communities)` - *Return unique display names, disambiguating duplicate labels.*

**Methods:**
- `__init__` (line 89) `def __init__(self, config)` - *Store configuration for wiki output limits and paths.*
- `generate` (line 94) `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)` - *Write all wiki files and return the output directory path.*
- `_prune_stale_pages` (line 142) `def _prune_stale_pages(self, out_dir, current)` - *Delete community pages from previous runs that are no longer generated.*
- `lint` (line 151) `def lint(self, project_root)` - *Check wiki health and return a list of issue descriptions.*
- `_resolve_communities` (line 174) `def _resolve_communities(self, nodes, analysis, resolved)` - *Return detected communities plus an orphan fallback for leftovers.*
- `_community_of` (line 200) `def _community_of(self, node_id, communities)` - *Return the community containing the given node id.*
- `_build_connections` (line 209) `def _build_connections(self, communities, resolved, analysis, node_map, layers)` - *Derive typed bridges between communities with strength scores.*
- `_duplicate_links` (line 274) `def _duplicate_links(communities, node_map, skip_pairs)` - *Flag community pairs sharing an unusual fraction of symbol names.*
- `_shared_context_links` (line 317) `def _shared_context_links(self, communities, existing, node_map, layers)` - *Infer weak links between otherwise disconnected communities.*
- `_shared_context` (line 353) `def _shared_context(first, second, node_map, layers)` - *Describe shared language or layer between two communities.*
- `_build_connections_json` (line 386) `def _build_connections_json(self, connections)` - *Serialize connections as pretty-printed JSON.*
- `_definition_for` (line 390) `def _definition_for(self, community, node_map)` - *Synthesize a one-paragraph definition for a community.*
- `_file_row` (line 419) `def _file_row(self, fid, node_map, layers)` - *Return a markdown table row for a single file, or empty string.*
- `_build_grouped_files` (line 433) `def _build_grouped_files(self, members, node_map, layers, max_files)` - *List oversized communities grouped by directory within budget.*
- `_build_community_page` (line 482) `def _build_community_page(self, community, node_map, resolved, analysis, layers, findings, analysis_v2, connections)` - *Build the synthesis page for a single community.*
- `_questions_for` (line 635) `def _questions_for(self, community, node_map, member_set, analysis_v2)` - *Generate deterministic open questions for a community.*
- `_large_files` (line 673) `def _large_files(self, nodes, project_root)` - *Return node ids whose on-disk size exceeds the large-file threshold.*
- `_build_index` (line 686) `def _build_index(self, nodes, resolved, analysis, layers, findings, analysis_v2, communities, pages, connections, project_name, project_root)` - *Build the wiki entry point with overview and navigation.*
- `_overview_paragraph` (line 798) `def _overview_paragraph(self, nodes, analysis, layers, findings, analysis_v2, communities)` - *Synthesize the central preoccupations paragraph.*
- `_connective_paragraph` (line 831) `def _connective_paragraph(self, communities, connections)` - *Synthesize the connective tissue paragraph.*
- `_questions_paragraph` (line 852) `def _questions_paragraph(self, analysis, findings, analysis_v2, coverage)` - *Synthesize the open questions paragraph.*
- `_build_queries` (line 868) `def _build_queries(self, analysis)` - *Build the starter question log with feedback loop instructions.*
- `_build_report` (line 893) `def _build_report(self, nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, project_name, project_root)` - *Build the honest audit report with confidence and limits.*
- `_estimate_tokens` (line 965) `def _estimate_tokens(self, nodes, connections)` - *Estimate wiki read cost as characters divided by four.*
- `_write` (line 976) `def _write(path, content)` - *Write wiki file content with UTF-8 encoding.*
- `dominant` (line 360) `def dominant(ids, key)`

#### `__init__.py`
**Path:** `readmenator/parsers/__init__.py`
**File Doc:** *Parser factory: maps file extensions to per-language LanguageParser classes.*

**Functions:**
- `_init_parser_map` (line 34) `def _init_parser_map()`
- `create_parser` (line 70) `def create_parser(extension, filename, config)` - *Factory: return a parser instance for the given file extension.*

#### `_assembly.py`
**Path:** `readmenator/parsers/_assembly.py`
**File Doc:** *Assembly parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `AssemblyParser` (line 11) `class AssemblyParser(LanguageParser)` - *Parser for assembly (.asm, .s, .S).

Extracts labels at the start of a line (``label:``) as function
symbols. This is a best-effort heuristic; local labels and
directives are not always distinguishable.*

**Methods:**
- `_extract_specifics` (line 19) `def _extract_specifics(self, content)`

#### `_base.py`
**Path:** `readmenator/parsers/_base.py`
**File Doc:** *LanguageParser base class with shared docstring and signature extraction.*

**Classes:**
- `LanguageParser` (line 12) `class LanguageParser` - *Base class for all language-specific parsers.

Subclasses must implement ``_extract_specifics`` to populate
``self.symbols`` and ``self.imports``. Common utility methods
``_extract_docstring`` and ``_extract_signature`` are provided
for reuse across all parsers.*

**Methods:**
- `__init__` (line 21) `def __init__(self, filename, config)` - *Initialise the parser with a file path and application config.

Args:
    filename: Relative or absolute path of the source file.
    config: Application-wide configuration settings.*
- `parse` (line 36) `def parse(self, content)` - *Parse *content* and populate symbol/import lists.

Splits the source into lines, then delegates to the subclass-
specific ``_extract_specifics`` logic.*
- `_extract_specifics` (line 45) `def _extract_specifics(self, content)` - *Subclass hook for language-specific symbol extraction.*
- `_extract_docstring` (line 49) `def _extract_docstring(self, line_num)` - *Walk backwards from *line_num* to collect preceding comments/docstrings.

Supports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``
comment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``
from Config.*
- `_extract_signature` (line 91) `def _extract_signature(self, content, match_start, pattern)` - *Extract a compact signature snippet starting at *match_start*.

Scans forward to the opening brace or a fallback length,
then truncates to 100 characters for display.*

#### `_c.py`
**Path:** `readmenator/parsers/_c.py`
**File Doc:** *C and C++ parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `CParser` (line 30) `class CParser(LanguageParser)` - *Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).

Extracts includes, structs, classes, functions, and preprocessor
macros using regex heuristics tuned to C-family syntax.*

**Functions:**
- `_has_type_prefix` (line 18) `def _has_type_prefix(prefix)` - *Return True when a prototype prefix carries a return type.*

**Methods:**
- `_extract_specifics` (line 37) `def _extract_specifics(self, content)` - *Extract C-family symbols and imports from source content.

Collects includes (quoted vs system), structs, classes, enums,
unions, typedefs, functions (definitions and prototypes), extern
declarations, globals, and macros.*

#### `_csharp.py`
**Path:** `readmenator/parsers/_csharp.py`
**File Doc:** *C# parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `CSharpParser` (line 11) `class CSharpParser(LanguageParser)` - *Parser for C# (.cs).

Extracts ``using`` directives, class/struct/interface/record
declarations, and methods with access modifiers.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_dart.py`
**Path:** `readmenator/parsers/_dart.py`
**File Doc:** *Dart parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `DartParser` (line 11) `class DartParser(LanguageParser)` - *Parser for Dart (.dart).

Extracts import statements, class declarations (with extends),
and top-level or method function declarations by return type.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_elixir.py`
**Path:** `readmenator/parsers/_elixir.py`
**File Doc:** *Elixir parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `ElixirParser` (line 11) `class ElixirParser(LanguageParser)` - *Parser for Elixir (.ex, .exs).

Extracts ``import``/``alias``/``require``/``use`` directives,
module definitions, and named function definitions.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_gdscript.py`
**Path:** `readmenator/parsers/_gdscript.py`
**File Doc:** *GDScript parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `GDScriptParser` (line 11) `class GDScriptParser(LanguageParser)` - *Parser for Godot GDScript (.gd).

Extracts ``extends`` / ``class_name`` directives and ``func``
method declarations.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_go.py`
**Path:** `readmenator/parsers/_go.py`
**File Doc:** *Go parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `GoParser` (line 11) `class GoParser(LanguageParser)` - *Parser for Go (.go).

Extracts import blocks or single import statements, exported
functions (including methods), and type definitions (struct/interface).*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_java.py`
**Path:** `readmenator/parsers/_java.py`
**File Doc:** *Java parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `JavaParser` (line 11) `class JavaParser(LanguageParser)` - *Parser for Java (.java).

Extracts import statements, class and interface declarations,
and methods complete with access modifiers and type signatures.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_javascript.py`
**Path:** `readmenator/parsers/_javascript.py`
**File Doc:** *JavaScript and TypeScript parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `JavaScriptParser` (line 11) `class JavaScriptParser(LanguageParser)` - *Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).

Extracts ES module imports, CommonJS ``require`` calls, function
declarations, arrow-function variables, and class definitions
(including inheritance).*

**Methods:**
- `_extract_specifics` (line 19) `def _extract_specifics(self, content)`

#### `_kotlin.py`
**Path:** `readmenator/parsers/_kotlin.py`
**File Doc:** *Kotlin parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `KotlinParser` (line 11) `class KotlinParser(LanguageParser)` - *Parser for Kotlin (.kt, .kts).

Extracts ``import`` statements, class/object/interface/data class
declarations, and function definitions.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_lua.py`
**Path:** `readmenator/parsers/_lua.py`
**File Doc:** *Lua parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `LuaParser` (line 11) `class LuaParser(LanguageParser)` - *Parser for Lua (.lua).

Extracts ``require`` imports, function declarations (named and
table-based), and module returns.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_nim.py`
**Path:** `readmenator/parsers/_nim.py`
**File Doc:** *Nim parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `NimParser` (line 11) `class NimParser(LanguageParser)` - *Parser for Nim (.nim).

Extracts ``import`` statements, ``proc`` / ``func`` / ``method``
declarations, and ``type`` definitions.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_php.py`
**Path:** `readmenator/parsers/_php.py`
**File Doc:** *PHP parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `PHPParser` (line 11) `class PHPParser(LanguageParser)` - *Parser for PHP (.php).

Extracts ``use/require/include`` (including ``_once`` variants),
function declarations, and class declarations.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_python.py`
**Path:** `readmenator/parsers/_python.py`
**File Doc:** *Python parser: native ast extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `PythonParser` (line 12) `class PythonParser(LanguageParser)` - *Parser for Python (.py) using the native ``ast`` module.

Extracts imports, functions (including async), and class
definitions with docstrings via ``ast.get_docstring``.*

**Methods:**
- `_extract_specifics` (line 19) `def _extract_specifics(self, content)`

#### `_ruby.py`
**Path:** `readmenator/parsers/_ruby.py`
**File Doc:** *Ruby parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `RubyParser` (line 11) `class RubyParser(LanguageParser)` - *Parser for Ruby (.rb).

Extracts ``require`` / ``require_relative`` imports, class and
module definitions with inheritance, and method definitions.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_rust.py`
**Path:** `readmenator/parsers/_rust.py`
**File Doc:** *Rust parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `RustParser` (line 11) `class RustParser(LanguageParser)` - *Parser for Rust (.rs).

Extracts ``use`` imports, public and private functions,
structs, traits, and enums.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_scala.py`
**Path:** `readmenator/parsers/_scala.py`
**File Doc:** *Scala parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `ScalaParser` (line 11) `class ScalaParser(LanguageParser)` - *Parser for Scala (.scala).

Extracts ``import`` statements, class/object/trait declarations,
and method definitions.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_shell.py`
**Path:** `readmenator/parsers/_shell.py`
**File Doc:** *Shell parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `ShellParser` (line 11) `class ShellParser(LanguageParser)` - *Parser for shell scripts (.sh, .bash, .zsh).

Extracts function declarations in both POSIX (``name() {``)
and ``function`` keyword syntax.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `_swift.py`
**Path:** `readmenator/parsers/_swift.py`
**File Doc:** *Swift parser: regex extraction of symbols, signatures, docstrings, and imports.*

**Classes:**
- `SwiftParser` (line 11) `class SwiftParser(LanguageParser)` - *Parser for Swift (.swift).

Extracts ``import`` statements, class/struct/enum/protocol
declarations with inheritance, and function definitions.*

**Methods:**
- `_extract_specifics` (line 18) `def _extract_specifics(self, content)`

#### `readmenator.py`
**Path:** `readmenator.py`
**File Doc:** *Launcher shim that runs the readmenator CLI from a source checkout.*

*No symbols extracted*

#### `readmenator_orchestrator.py`
**Path:** `readmenator_orchestrator.py`

**Classes:**
- `Config` (line 21) `class Config`
- `GitHubClient` (line 77) `class GitHubClient`
- `RepositoryProcessor` (line 191) `class RepositoryProcessor`
- `Orchestrator` (line 341) `class Orchestrator`
- `TestOrchestrator` (line 396) `class TestOrchestrator(TestCase)`

**Methods:**
- `_validate_repo_name` (line 50) `def _validate_repo_name(name)`
- `_validate_branch_name` (line 56) `def _validate_branch_name(name)`
- `_safe_env` (line 62) `def _safe_env()`
- `parse_arguments` (line 438) `def parse_arguments()`
- `main` (line 455) `def main()`
- `__init__` (line 78) `def __init__(self, config)`
- `_resolve_user` (line 83) `def _resolve_user(self)`
- `_setup_git_auth` (line 104) `def _setup_git_auth(self)`
- `list_repos` (line 118) `def list_repos(self)`
- `close_existing_prs` (line 130) `def close_existing_prs(self, repo)`
- `delete_remote_branch` (line 158) `def delete_remote_branch(self, repo)`
- `create_pr` (line 170) `def create_pr(self, repo, default_branch, timestamp)`
- `__init__` (line 192) `def __init__(self, config, github_client)`
- `process` (line 196) `def process(self, repo)`
- `_get_default_branch` (line 225) `def _get_default_branch(self, repo)`
- `_clone_repository` (line 241) `def _clone_repository(self, repo)`
- `_run_readmenator` (line 257) `def _run_readmenator(self, repo_dir)`
- `_copy_to_docs_dir` (line 277) `def _copy_to_docs_dir(self, repo_dir, generated_file)`
- `_commit_and_push` (line 290) `def _commit_and_push(self, repo_dir, repo)`
- `_cleanup_temp_dir` (line 336) `def _cleanup_temp_dir(temp_dir)`
- `__init__` (line 342) `def __init__(self, config)`
- `run` (line 347) `def run(self, dry_run, only_repo)`
- `setUp` (line 397) `def setUp(self)`
- `tearDown` (line 401) `def tearDown(self)`
- `test_config_immutability` (line 404) `def test_config_immutability(self)`
- `test_config_defaults` (line 408) `def test_config_defaults(self)`
- `test_skip_repos_logic` (line 415) `def test_skip_repos_logic(self)`
- `test_repo_name_validation` (line 419) `def test_repo_name_validation(self)`
- `test_branch_name_validation` (line 429) `def test_branch_name_validation(self)`

#### `__init__.py`
**Path:** `tests/__init__.py`

*No symbols extracted*

#### `test_agent_friendliness.py`
**Path:** `tests/test_agent_friendliness.py`
**File Doc:** *Contract tests for agent-facing output quality: budgets, purposes, freshness, noise.*

**Classes:**
- `TestAgentOutputBudget` (line 55) `class TestAgentOutputBudget(TestCase)` - *Every generated document respects the line cap, with nothing lost.*
- `TestAgentOutputSignal` (line 110) `class TestAgentOutputSignal(TestCase)` - *Documents carry signal, not repetition.*
- `TestPurposeExtraction` (line 176) `class TestPurposeExtraction(TestCase)` - *File purposes are one clean sentence with a symbol fallback.*
- `TestManifestFreshness` (line 199) `class TestManifestFreshness(TestCase)` - *MANIFEST lets an agent decide staleness without reading anything else.*
- `TestNoiseReduction` (line 244) `class TestNoiseReduction(TestCase)` - *Generated artifacts and naive heuristics never pollute the graph.*
- `TestLlmsTxt` (line 281) `class TestLlmsTxt(TestCase)` - *The published site exposes an llms.txt entry point for agents.*
- `TestCommunityHubDamping` (line 308) `class TestCommunityHubDamping(TestCase)` - *A shared hub imported by every file must not merge unrelated clusters.*
- `TestSourceFreshness` (line 329) `class TestSourceFreshness(TestCase)` - *Docs freshness is verifiable from content, independent of commit timing.*
- `TestCommunityShaping` (line 363) `class TestCommunityShaping(TestCase)` - *Tiny groups fold into neighbors and shared-directory labels stay distinct.*
- `TestSiteDocsPruning` (line 394) `class TestSiteDocsPruning(TestCase)` - *The static site never keeps copies of docs that were renamed or removed.*

**Functions:**
- `_node` (line 21) `def _node(node_id, doc, symbols)` - *Build a Python file node for tests.*
- `_edge` (line 29) `def _edge(source, target, relation)` - *Build an extracted edge for tests.*
- `_big_project` (line 34) `def _big_project(files, symbols_per_file)` - *Build a project large enough to force pagination of every document.*

**Methods:**
- `test_agent_output_pages_respect_line_cap_on_large_projects` (line 58) `def test_agent_output_pages_respect_line_cap_on_large_projects(self)`
- `test_agent_output_pagination_keeps_every_symbol_greppable` (line 71) `def test_agent_output_pagination_keeps_every_symbol_greppable(self)`
- `test_agent_output_pages_repeat_table_header_and_link_next` (line 84) `def test_agent_output_pages_repeat_table_header_and_link_next(self)`
- `test_agent_output_prunes_stale_pages` (line 96) `def test_agent_output_prunes_stale_pages(self)`
- `test_api_states_dependencies_once_per_file` (line 113) `def test_api_states_dependencies_once_per_file(self)`
- `test_api_skips_private_helpers_and_test_layer` (line 122) `def test_api_skips_private_helpers_and_test_layer(self)`
- `test_api_qualifies_methods_with_owner_class` (line 136) `def test_api_qualifies_methods_with_owner_class(self)`
- `test_architecture_external_excludes_internally_resolved_imports` (line 144) `def test_architecture_external_excludes_internally_resolved_imports(self)`
- `test_index_reports_used_by_count_and_escapes_pipes` (line 153) `def test_index_reports_used_by_count_and_escapes_pipes(self)`
- `test_gotchas_exclude_test_layer_and_report_blast_radius` (line 161) `def test_gotchas_exclude_test_layer_and_report_blast_radius(self)`
- `test_purpose_takes_first_sentence` (line 179) `def test_purpose_takes_first_sentence(self)`
- `test_purpose_skips_banners_and_spdx` (line 182) `def test_purpose_skips_banners_and_spdx(self)`
- `test_purpose_falls_back_to_primary_public_symbol` (line 185) `def test_purpose_falls_back_to_primary_public_symbol(self)`
- `test_purpose_truncates_on_word_boundary` (line 192) `def test_purpose_truncates_on_word_boundary(self)`
- `_git_repo` (line 202) `def _git_repo(self, root, packed)` - *Create a minimal git directory layout pointing at a fixed commit.*
- `test_gitmeta_reads_loose_and_packed_refs` (line 214) `def test_gitmeta_reads_loose_and_packed_refs(self)`
- `test_gitmeta_outside_repository_is_empty` (line 220) `def test_gitmeta_outside_repository_is_empty(self)`
- `test_manifest_has_commit_relative_root_and_inventory` (line 224) `def test_manifest_has_commit_relative_root_and_inventory(self)`
- `test_scanner_skips_own_generated_outputs` (line 247) `def test_scanner_skips_own_generated_outputs(self)`
- `test_resolver_prefers_root_package_over_launcher_shim` (line 260) `def test_resolver_prefers_root_package_over_launcher_shim(self)`
- `test_layers_match_whole_words_not_substrings` (line 264) `def test_layers_match_whole_words_not_substrings(self)`
- `test_layers_test_framework_import_needs_test_path` (line 272) `def test_layers_test_framework_import_needs_test_path(self)`
- `test_llms_txt_lists_wiki_before_agent_docs` (line 284) `def test_llms_txt_lists_wiki_before_agent_docs(self)`
- `test_publish_writes_llms_txt` (line 296) `def test_publish_writes_llms_txt(self)`
- `test_communities_survive_a_shared_hub` (line 311) `def test_communities_survive_a_shared_hub(self)`
- `test_fingerprint_changes_with_content_not_with_order` (line 332) `def test_fingerprint_changes_with_content_not_with_order(self)`
- `test_check_freshness_detects_source_edits` (line 343) `def test_check_freshness_detects_source_edits(self)`
- `test_small_community_merges_into_best_connected_neighbor` (line 366) `def test_small_community_merges_into_best_connected_neighbor(self)`
- `test_shared_directory_labels_use_core_file` (line 380) `def test_shared_directory_labels_use_core_file(self)`
- `test_publish_assets_prunes_stale_markdown` (line 397) `def test_publish_assets_prunes_stale_markdown(self)`

#### `test_agent_injector.py`
**Path:** `tests/test_agent_injector.py`
**File Doc:** *Contract tests for AI agent file injection.  SDD + TDD + BDD: Each test validates a specific behavioral contract of the AgentInjector for injecting/deleting knowledge base references into AI agent instruction files.*

**Classes:**
- `TestAgentInjectorInjectBehavior` (line 19) `class TestAgentInjectorInjectBehavior(TestCase)` - *BDD: AgentInjector injection contract.*
- `TestAgentInjectorRemoveBehavior` (line 168) `class TestAgentInjectorRemoveBehavior(TestCase)` - *BDD: AgentInjector removal contract.*
- `TestAgentInjectorFindFiles` (line 211) `class TestAgentInjectorFindFiles(TestCase)` - *BDD: AgentInjector file detection contract.*
- `TestAgentInjectorEdgeCases` (line 248) `class TestAgentInjectorEdgeCases(TestCase)` - *BDD: AgentInjector edge case contract.*

**Methods:**
- `setUp` (line 22) `def setUp(self)`
- `tearDown` (line 27) `def tearDown(self)`
- `test_inject_into_agents_md_adds_kb_link` (line 30) `def test_inject_into_agents_md_adds_kb_link(self)`
- `test_inject_into_claude_md_adds_kb_link` (line 39) `def test_inject_into_claude_md_adds_kb_link(self)`
- `test_inject_into_cursorrules_adds_kb_link` (line 49) `def test_inject_into_cursorrules_adds_kb_link(self)`
- `test_inject_into_github_copilot_instructions` (line 57) `def test_inject_into_github_copilot_instructions(self)`
- `test_inject_replaces_old_injection_without_regen_command` (line 67) `def test_inject_replaces_old_injection_without_regen_command(self)`
- `test_inject_skips_when_already_up_to_date` (line 82) `def test_inject_skips_when_already_up_to_date(self)`
- `test_inject_into_cursor_rules_mdc_glob` (line 96) `def test_inject_into_cursor_rules_mdc_glob(self)`
- `test_inject_is_idempotent_does_not_duplicate` (line 106) `def test_inject_is_idempotent_does_not_duplicate(self)`
- `test_inject_no_agent_files_returns_zero` (line 117) `def test_inject_no_agent_files_returns_zero(self)`
- `test_inject_preserves_existing_content` (line 121) `def test_inject_preserves_existing_content(self)`
- `test_inject_multiple_agent_files` (line 129) `def test_inject_multiple_agent_files(self)`
- `test_inject_plain_text_format_for_yaml` (line 136) `def test_inject_plain_text_format_for_yaml(self)`
- `test_custom_kb_filename_works` (line 145) `def test_custom_kb_filename_works(self)`
- `test_injection_includes_regeneration_command` (line 153) `def test_injection_includes_regeneration_command(self)`
- `test_inject_does_not_execute_commands` (line 160) `def test_inject_does_not_execute_commands(self)`
- `setUp` (line 171) `def setUp(self)`
- `tearDown` (line 176) `def tearDown(self)`
- `test_remove_strips_injected_section` (line 179) `def test_remove_strips_injected_section(self)`
- `test_remove_without_injection_returns_zero` (line 190) `def test_remove_without_injection_returns_zero(self)`
- `test_remove_no_files_returns_zero` (line 196) `def test_remove_no_files_returns_zero(self)`
- `test_remove_preserves_original_content` (line 200) `def test_remove_preserves_original_content(self)`
- `setUp` (line 214) `def setUp(self)`
- `tearDown` (line 218) `def tearDown(self)`
- `test_finds_agents_md` (line 221) `def test_finds_agents_md(self)`
- `test_finds_all_listed_files` (line 227) `def test_finds_all_listed_files(self)`
- `test_finds_cursor_rules_glob` (line 234) `def test_finds_cursor_rules_glob(self)`
- `test_returns_empty_when_no_files` (line 243) `def test_returns_empty_when_no_files(self)`
- `setUp` (line 251) `def setUp(self)`
- `tearDown` (line 256) `def tearDown(self)`
- `test_inject_into_empty_file` (line 259) `def test_inject_into_empty_file(self)`
- `test_inject_respects_custom_agent_files_list` (line 267) `def test_inject_respects_custom_agent_files_list(self)`
- `test_inject_does_not_touch_unlisted_files` (line 275) `def test_inject_does_not_touch_unlisted_files(self)`

#### `test_agent_output.py`
**Path:** `tests/test_agent_output.py`

**Classes:**
- `TestAgentOutputContract` (line 49) `class TestAgentOutputContract(TestCase)`
- `TestSubsystemInference` (line 63) `class TestSubsystemInference(TestCase)`
- `TestIndexGeneration` (line 117) `class TestIndexGeneration(TestCase)`
- `TestSecurityGeneration` (line 143) `class TestSecurityGeneration(TestCase)`
- `TestGotchasGeneration` (line 190) `class TestGotchasGeneration(TestCase)`
- `TestArchitectureGeneration` (line 246) `class TestArchitectureGeneration(TestCase)`
- `TestApiGeneration` (line 268) `class TestApiGeneration(TestCase)`
- `TestSubsystemFileGeneration` (line 294) `class TestSubsystemFileGeneration(TestCase)`
- `TestRecipesGeneration` (line 316) `class TestRecipesGeneration(TestCase)`
- `TestFullGenerate` (line 362) `class TestFullGenerate(TestCase)`
- `TestInjectionOutdatedDetection` (line 434) `class TestInjectionOutdatedDetection(TestCase)`

**Functions:**
- `_make_node` (line 19) `def _make_node(node_id, symbols, doc, language)`
- `_make_edge` (line 30) `def _make_edge(source, target, relation)`
- `_make_finding` (line 34) `def _make_finding(file_path, line, severity, rule_id, description, snippet, cwe)`

**Methods:**
- `test_config_defaults` (line 50) `def test_config_defaults(self)`
- `test_config_immutable` (line 56) `def test_config_immutable(self)`
- `test_inferred_from_directories` (line 64) `def test_inferred_from_directories(self)`
- `test_flat_project_single_file` (line 80) `def test_flat_project_single_file(self)`
- `test_min_threshold_respected` (line 91) `def test_min_threshold_respected(self)`
- `test_misc_catches_unassigned` (line 103) `def test_misc_catches_unassigned(self)`
- `test_index_lists_all_files` (line 118) `def test_index_lists_all_files(self)`
- `test_index_table_format` (line 133) `def test_index_table_format(self)`
- `test_empty_findings` (line 144) `def test_empty_findings(self)`
- `test_findings_grouped_by_severity` (line 150) `def test_findings_grouped_by_severity(self)`
- `test_findings_include_fix_hint_and_scope` (line 166) `def test_findings_include_fix_hint_and_scope(self)`
- `test_no_json_wrapping` (line 181) `def test_no_json_wrapping(self)`
- `test_god_nodes_section` (line 191) `def test_god_nodes_section(self)`
- `test_cycles_section` (line 207) `def test_cycles_section(self)`
- `test_empty_gotchas` (line 224) `def test_empty_gotchas(self)`
- `test_cycle_loop_closed` (line 230) `def test_cycle_loop_closed(self)`
- `test_internal_dependencies` (line 247) `def test_internal_dependencies(self)`
- `test_external_imports` (line 258) `def test_external_imports(self)`
- `test_functions_listed` (line 269) `def test_functions_listed(self)`
- `test_no_json_in_api` (line 283) `def test_no_json_in_api(self)`
- `test_subsystem_files_written` (line 295) `def test_subsystem_files_written(self)`
- `test_recipes_directory` (line 317) `def test_recipes_directory(self)`
- `test_recipes_grounded_in_actual_findings` (line 330) `def test_recipes_grounded_in_actual_findings(self)`
- `test_generate_creates_all_files` (line 363) `def test_generate_creates_all_files(self)`
- `test_all_files_under_500_lines` (line 394) `def test_all_files_under_500_lines(self)`
- `test_no_json_in_any_output` (line 409) `def test_no_json_in_any_output(self)`
- `test_manifest_workflow_orients_with_ls` (line 421) `def test_manifest_workflow_orients_with_ls(self)`
- `test_agent_injector_detects_outdated` (line 435) `def test_agent_injector_detects_outdated(self)`
- `test_agent_injector_skips_identical` (line 457) `def test_agent_injector_skips_identical(self)`
- `test_readme_injector_detects_outdated` (line 473) `def test_readme_injector_detects_outdated(self)`
- `test_readme_injector_skips_identical` (line 495) `def test_readme_injector_skips_identical(self)`

#### `test_analyzer.py`
**Path:** `tests/test_analyzer.py`
**File Doc:** *Contract tests for the GraphAnalyzer.  Validates community detection, god node computation, surprising connection discovery, and suggested question generation.*

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
- `test_analyze_is_repeatable` (line 130) `def test_analyze_is_repeatable(self)`
- `test_dominant_directory_prefers_specific_on_tie` (line 141) `def test_dominant_directory_prefers_specific_on_tie(self)`

#### `test_cache.py`
**Path:** `tests/test_cache.py`
**File Doc:** *Contract tests for the FileCache.  Validates SHA256 hashing, cache persistence, change detection, and stale entry pruning.*

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
**File Doc:** *Contract tests for the CursorRulesGenerator.  Validates base rule generation, layer constraint extraction, analysis constraint extraction, and violation rule formatting.*

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

#### `test_dataflow.py`
**Path:** `tests/test_dataflow.py`

**Classes:**
- `TestDataflowContract` (line 25) `class TestDataflowContract(TestCase)`

**Functions:**
- `_node` (line 8) `def _node(node_id, funcs)`
- `_analyze` (line 17) `def _analyze(body)`

**Methods:**
- `test_config_defaults` (line 26) `def test_config_defaults(self)`
- `test_config_immutable` (line 31) `def test_config_immutable(self)`
- `test_uninit_use_detected` (line 37) `def test_uninit_use_detected(self)`
- `test_initialized_use_clean` (line 46) `def test_initialized_use_clean(self)`
- `test_params_count_as_initialized` (line 50) `def test_params_count_as_initialized(self)`
- `test_scanf_addr_counts_as_init` (line 58) `def test_scanf_addr_counts_as_init(self)`
- `test_dead_store_detected` (line 62) `def test_dead_store_detected(self)`
- `test_read_store_clean` (line 67) `def test_read_store_clean(self)`
- `test_unchecked_alloc_detected` (line 71) `def test_unchecked_alloc_detected(self)`
- `test_checked_alloc_clean` (line 78) `def test_checked_alloc_clean(self)`
- `test_disabled_returns_empty` (line 84) `def test_disabled_returns_empty(self)`
- `test_missing_content_skipped` (line 91) `def test_missing_content_skipped(self)`
- `test_issue_cap_respected` (line 96) `def test_issue_cap_respected(self)`
- `test_plain_assignment_is_not_a_declaration` (line 105) `def test_plain_assignment_is_not_a_declaration(self)`
- `test_subscript_store_counts_as_init` (line 110) `def test_subscript_store_counts_as_init(self)`
- `test_asm_output_counts_as_init` (line 116) `def test_asm_output_counts_as_init(self)`
- `test_fd_lt_zero_counts_as_checked` (line 123) `def test_fd_lt_zero_counts_as_checked(self)`
- `test_map_failed_counts_as_checked` (line 129) `def test_map_failed_counts_as_checked(self)`
- `test_member_null_check_counts` (line 136) `def test_member_null_check_counts(self)`
- `test_loop_carried_var_not_dead` (line 144) `def test_loop_carried_var_not_dead(self)`
- `test_line_numbers_survive_subscript_stores` (line 156) `def test_line_numbers_survive_subscript_stores(self)`
- `test_member_store_not_local_assign` (line 167) `def test_member_store_not_local_assign(self)`
- `test_array_arg_to_filler_counts_as_init` (line 173) `def test_array_arg_to_filler_counts_as_init(self)`
- `test_array_arg_to_readonly_still_uninit` (line 181) `def test_array_arg_to_readonly_still_uninit(self)`
- `test_array_filled_in_decl_init_call` (line 188) `def test_array_filled_in_decl_init_call(self)`
- `test_static_never_uninit` (line 196) `def test_static_never_uninit(self)`
- `test_derived_pointer_not_dead` (line 203) `def test_derived_pointer_not_dead(self)`
- `test_sizeof_is_not_a_read` (line 216) `def test_sizeof_is_not_a_read(self)`
- `test_block_comment_malloc_ignored` (line 225) `def test_block_comment_malloc_ignored(self)`
- `test_address_alias_pointer_not_dead` (line 234) `def test_address_alias_pointer_not_dead(self)`
- `test_array_store_before_read_suppresses_uninit` (line 248) `def test_array_store_before_read_suppresses_uninit(self)`
- `test_same_line_use_not_dead` (line 256) `def test_same_line_use_not_dead(self)`
- `test_same_line_only_assign_is_dead` (line 264) `def test_same_line_only_assign_is_dead(self)`
- `test_alias_pointer_store_initializes_array` (line 272) `def test_alias_pointer_store_initializes_array(self)`
- `test_inline_alias_fill_suppresses_uninit` (line 281) `def test_inline_alias_fill_suppresses_uninit(self)`
- `test_function_pointer_call_counts_as_use` (line 290) `def test_function_pointer_call_counts_as_use(self)`
- `test_plain_call_is_not_a_local_use` (line 298) `def test_plain_call_is_not_a_local_use(self)`
- `test_local_struct_does_not_truncate_span` (line 305) `def test_local_struct_does_not_truncate_span(self)`
- `test_file_scope_symbol_still_bounds_span` (line 329) `def test_file_scope_symbol_still_bounds_span(self)`
- `test_url_string_does_not_truncate_line` (line 344) `def test_url_string_does_not_truncate_line(self)`
- `test_assert_macro_counts_as_null_check` (line 352) `def test_assert_macro_counts_as_null_check(self)`
- `test_multiline_call_assigns_array_arg` (line 360) `def test_multiline_call_assigns_array_arg(self)`
- `test_address_taken_suppresses_dead_store` (line 369) `def test_address_taken_suppresses_dead_store(self)`
- `test_member_store_initializes_base` (line 377) `def test_member_store_initializes_base(self)`

#### `test_dead_code.py`
**Path:** `tests/test_dead_code.py`
**File Doc:** *Contract tests for the DeadCodeStripper.  Validates dead code detection, in-degree computation, entry point exclusion, and recommendation classification.*

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

#### `test_diagrams.py`
**Path:** `tests/test_diagrams.py`
**File Doc:** *Contract tests for interactive system maps.  Validates typed intermediate representations, deterministic validation receipts, before and after comparison, and self-contained HTML rendering for the five diagram kinds.*

**Classes:**
- `TestSystemMapBuilderContract` (line 30) `class TestSystemMapBuilderContract(TestCase)` - *Contract: builder produces deterministic maps for all five kinds.*
- `TestSystemMapValidatorContract` (line 176) `class TestSystemMapValidatorContract(TestCase)` - *Contract: validator returns deterministic receipts with rule codes.*
- `TestInteractiveMapRendererContract` (line 237) `class TestInteractiveMapRendererContract(TestCase)` - *Contract: renderer emits standalone interactive HTML documents.*
- `TestDocsSitePublisherContract` (line 360) `class TestDocsSitePublisherContract(TestCase)` - *Contract: publisher writes maps plus a gallery index as a static site.*
- `TestVisNetworkRendererContract` (line 503) `class TestVisNetworkRendererContract(TestCase)` - *Contract: vis.js renderer emits CDN-powered physics documents.*
- `TestDiagramVariantsContract` (line 619) `class TestDiagramVariantsContract(TestCase)` - *Contract: default exports are vis.js maps with gallery links.*

**Methods:**
- `setUp` (line 33) `def setUp(self)` - *Initialise builder with default configuration.*
- `_make_graph` (line 38) `def _make_graph(self)` - *Create a small deterministic project graph.*
- `test_builder_supports_five_kinds` (line 52) `def test_builder_supports_five_kinds(self)` - *Builder exposes architecture, workflow, sequence, dataflow, lifecycle.*
- `test_builder_produces_all_kinds` (line 59) `def test_builder_produces_all_kinds(self)` - *Build all returns one map per supported kind.*
- `test_builder_is_deterministic` (line 68) `def test_builder_is_deterministic(self)` - *Two builds over identical input share coordinates and bytes.*
- `test_builder_orders_links_deterministically` (line 80) `def test_builder_orders_links_deterministically(self)` - *Shuffled input edges yield identical ordered map relationships.*
- `test_builder_validates_large_graph_for_all_kinds` (line 101) `def test_builder_validates_large_graph_for_all_kinds(self)` - *Large layered graphs validate for every diagram kind.*
- `test_builder_reports_total_scope` (line 119) `def test_builder_reports_total_scope(self)` - *Built maps record shown scope and total input file count.*
- `test_builder_attaches_symbols_and_docs` (line 126) `def test_builder_attaches_symbols_and_docs(self)` - *Map nodes carry symbol records, file docs, and language.*
- `test_builder_truncates_symbols_per_node` (line 143) `def test_builder_truncates_symbols_per_node(self)` - *Symbol records respect the per-node configured cap.*
- `test_builder_truncates_to_configured_limit` (line 152) `def test_builder_truncates_to_configured_limit(self)` - *Oversized graphs are truncated to the configured node limit.*
- `test_compare_reports_added_removed_rerouted` (line 162) `def test_compare_reports_added_removed_rerouted(self)` - *Delta comparison reports added, removed, and rerouted facts.*
- `setUp` (line 179) `def setUp(self)` - *Initialise validator with default configuration.*
- `_valid_map` (line 184) `def _valid_map(self)` - *Create a minimal valid architecture map.*
- `test_validator_passes_valid_map` (line 197) `def test_validator_passes_valid_map(self)` - *Valid maps pass with the full check list and zero errors.*
- `test_validator_rejects_duplicate_node_ids` (line 204) `def test_validator_rejects_duplicate_node_ids(self)` - *Duplicate identifiers fail with rule D001.*
- `test_validator_rejects_dangling_edge` (line 214) `def test_validator_rejects_dangling_edge(self)` - *Edges pointing at unknown nodes fail with rule D002.*
- `test_validator_rejects_empty_map` (line 222) `def test_validator_rejects_empty_map(self)` - *Maps without nodes fail with rule D003.*
- `test_validator_rejects_unknown_kind` (line 228) `def test_validator_rejects_unknown_kind(self)` - *Unknown diagram kinds fail with rule D000.*
- `setUp` (line 240) `def setUp(self)` - *Initialise builder and renderer with default configuration.*
- `_map` (line 246) `def _map(self, kind)` - *Build a small map of the requested kind.*
- `test_renderer_produces_standalone_document` (line 256) `def test_renderer_produces_standalone_document(self)` - *Output is a complete HTML document with inline SVG.*
- `test_renderer_has_no_external_requests` (line 263) `def test_renderer_has_no_external_requests(self)` - *Output performs no external fetches or CDN references.*
- `test_renderer_includes_interaction_controls` (line 270) `def test_renderer_includes_interaction_controls(self)` - *Output includes search, passport, reach, route, lens, views, export.*
- `test_renderer_includes_keyboard_and_deep_links` (line 276) `def test_renderer_includes_keyboard_and_deep_links(self)` - *Output documents shortcuts and hash deep link contracts.*
- `test_renderer_escapes_malicious_labels` (line 285) `def test_renderer_escapes_malicious_labels(self)` - *Malicious labels are escaped and never break the document.*
- `test_renderer_embeds_valid_json_payloads` (line 298) `def test_renderer_embeds_valid_json_payloads(self)` - *Embedded payload scripts parse as valid JSON arrays.*
- `test_renderer_covers_all_five_kinds` (line 307) `def test_renderer_covers_all_five_kinds(self)` - *Every diagram kind renders a standalone document.*
- `test_renderer_links_gallery_home_when_configured` (line 314) `def test_renderer_links_gallery_home_when_configured(self)` - *Maps with a home target expose a gallery back link.*
- `test_renderer_omits_gallery_home_by_default` (line 321) `def test_renderer_omits_gallery_home_by_default(self)` - *Maps without a home target expose no gallery link.*
- `test_renderer_keeps_canvas_distinct_from_nodes` (line 326) `def test_renderer_keeps_canvas_distinct_from_nodes(self)` - *Canvas background differs from node fill for readability.*
- `test_renderer_supports_drag_and_settle` (line 334) `def test_renderer_supports_drag_and_settle(self)` - *Nodes are draggable with pointer capture plus a force pass.*
- `test_renderer_sanitizes_viewer_state_on_export` (line 342) `def test_renderer_sanitizes_viewer_state_on_export(self)` - *Exports drop temporary focus, dim, and drag classes.*
- `test_renderer_buttons_explain_their_purpose` (line 348) `def test_renderer_buttons_explain_their_purpose(self)` - *Every toolbar action carries a human-readable title.*
- `setUp` (line 363) `def setUp(self)` - *Initialise builder and publisher with default configuration.*
- `_maps` (line 369) `def _maps(self)` - *Build all five maps from a small deterministic graph.*
- `test_publish_writes_index_plus_five_maps` (line 379) `def test_publish_writes_index_plus_five_maps(self)` - *Publish creates an index, five map files, and a nojekyll marker.*
- `test_publish_index_links_every_map` (line 390) `def test_publish_index_links_every_map(self)` - *Gallery index links every published map with relative paths.*
- `test_publish_output_has_no_external_requests` (line 399) `def test_publish_output_has_no_external_requests(self)` - *Index and maps perform no external fetches or CDN references.*
- `test_publish_is_deterministic` (line 412) `def test_publish_is_deterministic(self)` - *Two publishes over identical input share index bytes.*
- `test_publish_escapes_malicious_project_name` (line 423) `def test_publish_escapes_malicious_project_name(self)` - *Malicious project names are escaped in the gallery index.*
- `test_publish_escapes_malicious_stat_keys` (line 432) `def test_publish_escapes_malicious_stat_keys(self)` - *Malicious statistics keys are escaped in the gallery index.*
- `test_publish_skips_invalid_maps` (line 443) `def test_publish_skips_invalid_maps(self)` - *Maps failing validation are skipped while the index is written.*
- `test_publish_empty_maps_writes_empty_gallery` (line 455) `def test_publish_empty_maps_writes_empty_gallery(self)` - *Empty input writes an index with an empty gallery notice.*
- `test_publish_leaves_input_maps_unmodified` (line 464) `def test_publish_leaves_input_maps_unmodified(self)` - *Publish never mutates the caller supplied map metadata.*
- `test_publish_flat_subdir_keeps_links_relative` (line 473) `def test_publish_flat_subdir_keeps_links_relative(self)` - *Flat layouts link maps beside the index with a local home.*
- `test_publish_index_explains_how_to_read` (line 486) `def test_publish_index_explains_how_to_read(self)` - *Gallery index documents the reader interactions.*
- `test_publish_card_reports_primary_scope` (line 494) `def test_publish_card_reports_primary_scope(self)` - *Gallery cards state shown files against the project total.*
- `setUp` (line 506) `def setUp(self)` - *Initialise builder and renderer with default configuration.*
- `_map` (line 512) `def _map(self, kind)` - *Build a small map of the requested kind.*
- `test_renderer_uses_configured_cdn_urls` (line 522) `def test_renderer_uses_configured_cdn_urls(self)` - *Script and style tags come from Config, never hardcoded.*
- `test_renderer_builds_vis_network_with_physics` (line 535) `def test_renderer_builds_vis_network_with_physics(self)` - *Output instantiates a vis network with physics enabled.*
- `test_renderer_links_gallery_home_when_configured` (line 543) `def test_renderer_links_gallery_home_when_configured(self)` - *Vis maps with a home target expose a gallery back link.*
- `test_renderer_disables_physics_from_config` (line 551) `def test_renderer_disables_physics_from_config(self)` - *Physics honors the configured enabled flag.*
- `test_renderer_escapes_malicious_titles` (line 558) `def test_renderer_escapes_malicious_titles(self)` - *Malicious labels never break tooltips or markup.*
- `test_renderer_exposes_reader_controls` (line 571) `def test_renderer_exposes_reader_controls(self)` - *Output carries search, reach, route, lens, chapters, export.*
- `test_renderer_is_deterministic` (line 577) `def test_renderer_is_deterministic(self)` - *Two renders over identical input share bytes.*
- `test_renderer_embeds_valid_payloads` (line 582) `def test_renderer_embeds_valid_payloads(self)` - *Embedded node and edge payloads parse as valid JSON.*
- `test_renderer_documents_symbols_per_file` (line 590) `def test_renderer_documents_symbols_per_file(self)` - *Node payloads and tooltips expose symbols with signatures.*
- `test_renderer_escapes_malicious_symbol_docs` (line 606) `def test_renderer_escapes_malicious_symbol_docs(self)` - *Malicious symbol documentation never breaks tooltips.*
- `_project` (line 622) `def _project(self, tmp)` - *Create a two-file project in a temporary directory.*
- `test_export_diagrams_writes_vis_maps_by_default` (line 627) `def test_export_diagrams_writes_vis_maps_by_default(self)` - *Default diagram export writes CDN-powered vis.js maps.*
- `test_export_diagrams_falls_back_offline_when_disabled` (line 641) `def test_export_diagrams_falls_back_offline_when_disabled(self)` - *Disabled vis flag produces offline maps without CDN.*

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
**File Doc:** *Contract tests for the GraphExporter.  Validates JSON, HTML, and SVG export formats with various node/edge configurations and analysis metadata.*

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

#### `test_gh_wiki.py`
**Path:** `tests/test_gh_wiki.py`
**File Doc:** *Contract tests for the GitHub wiki publisher (no network: git/gh calls are faked).*

**Classes:**
- `_FakeRunner` (line 14) `class _FakeRunner` - *Records commands and simulates gh/git with a local wiki clone.*
- `TestGitHubWikiPages` (line 61) `class TestGitHubWikiPages(TestCase)` - *Pages are flat, linked, navigable, and pinned to the source commit.*
- `TestGitHubWikiPublish` (line 115) `class TestGitHubWikiPublish(TestCase)` - *Publishing clones the wiki remote, commits, and pushes only when changed.*

**Methods:**
- `_project` (line 41) `def _project(root, config)` - *Create generated outputs the publisher mirrors.*
- `__init__` (line 17) `def __init__(self, origin, clone_ok, dirty)`
- `__call__` (line 24) `def __call__(self, command, cwd)`
- `test_gh_wiki_page_names_are_flat_and_prefixed` (line 64) `def test_gh_wiki_page_names_are_flat_and_prefixed(self)`
- `test_gh_wiki_render_rewrites_links_and_permalinks` (line 71) `def test_gh_wiki_render_rewrites_links_and_permalinks(self)`
- `test_gh_wiki_permalinks_never_escape_project_root` (line 88) `def test_gh_wiki_permalinks_never_escape_project_root(self)`
- `test_gh_wiki_dry_run_writes_locally_and_prunes_only_owned_pages` (line 96) `def test_gh_wiki_dry_run_writes_locally_and_prunes_only_owned_pages(self)`
- `test_gh_wiki_publish_clones_commits_and_pushes` (line 118) `def test_gh_wiki_publish_clones_commits_and_pushes(self)`
- `test_gh_wiki_publish_skips_push_when_unchanged` (line 130) `def test_gh_wiki_publish_skips_push_when_unchanged(self)`
- `test_gh_wiki_publish_explains_uninitialized_wiki` (line 139) `def test_gh_wiki_publish_explains_uninitialized_wiki(self)`
- `test_gh_wiki_rejects_malformed_configured_remote` (line 147) `def test_gh_wiki_rejects_malformed_configured_remote(self)`
- `test_gh_wiki_disabled_by_default` (line 154) `def test_gh_wiki_disabled_by_default(self)`

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
**File Doc:** *Contract tests for the ArchitectureLinter.  Validates file length checks, cross-layer violation detection, and circular dependency identification.*

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
**File Doc:** *Contract tests for the MCP server protocol and tool dispatch.  Validates JSON-RPC 2.0 message handling, tool definitions, resource definitions, proper error responses, and the full tool/resource lifecycle using a lightweight mock server.*

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
- `TestPythonParserContract` (line 88) `class TestPythonParserContract(TestCase)`
- `TestGoParserContract` (line 157) `class TestGoParserContract(TestCase)`
- `TestRustParserContract` (line 200) `class TestRustParserContract(TestCase)`
- `TestJavaScriptParserContract` (line 238) `class TestJavaScriptParserContract(TestCase)`
- `TestJavaParserContract` (line 277) `class TestJavaParserContract(TestCase)`
- `TestCSharpParserContract` (line 309) `class TestCSharpParserContract(TestCase)`
- `TestShellParserContract` (line 342) `class TestShellParserContract(TestCase)`
- `TestPHPParserContract` (line 361) `class TestPHPParserContract(TestCase)`
- `TestDartParserContract` (line 387) `class TestDartParserContract(TestCase)`
- `TestGDScriptParserContract` (line 412) `class TestGDScriptParserContract(TestCase)`
- `TestNimParserContract` (line 430) `class TestNimParserContract(TestCase)`
- `TestAssemblyParserContract` (line 456) `class TestAssemblyParserContract(TestCase)`
- `TestParserFactoryContract` (line 483) `class TestParserFactoryContract(TestCase)`

**Methods:**
- `setUp` (line 23) `def setUp(self)`
- `test_extracts_function` (line 26) `def test_extracts_function(self)`
- `test_extracts_struct` (line 33) `def test_extracts_struct(self)`
- `test_extracts_include` (line 40) `def test_extracts_include(self)`
- `test_extracts_define` (line 47) `def test_extracts_define(self)`
- `test_skips_reserved_words` (line 54) `def test_skips_reserved_words(self)`
- `test_function_line_points_at_definition` (line 64) `def test_function_line_points_at_definition(self)`
- `test_calls_are_not_prototypes` (line 71) `def test_calls_are_not_prototypes(self)`
- `test_class_with_inheritance` (line 80) `def test_class_with_inheritance(self)`
- `setUp` (line 89) `def setUp(self)`
- `test_extracts_function` (line 92) `def test_extracts_function(self)`
- `test_extracts_class` (line 99) `def test_extracts_class(self)`
- `test_extracts_imports` (line 106) `def test_extracts_imports(self)`
- `test_extracts_async_function` (line 114) `def test_extracts_async_function(self)`
- `test_handles_syntax_error_gracefully` (line 121) `def test_handles_syntax_error_gracefully(self)`
- `test_suppresses_syntax_warnings` (line 127) `def test_suppresses_syntax_warnings(self)`
- `test_extracts_signature_with_params` (line 139) `def test_extracts_signature_with_params(self)`
- `test_extracts_class_with_bases` (line 147) `def test_extracts_class_with_bases(self)`
- `setUp` (line 158) `def setUp(self)`
- `test_extracts_function` (line 161) `def test_extracts_function(self)`
- `test_extracts_method_receiver` (line 168) `def test_extracts_method_receiver(self)`
- `test_extracts_import_block` (line 175) `def test_extracts_import_block(self)`
- `test_extracts_single_import` (line 182) `def test_extracts_single_import(self)`
- `test_extracts_struct_and_interface` (line 188) `def test_extracts_struct_and_interface(self)`
- `setUp` (line 201) `def setUp(self)`
- `test_extracts_function` (line 204) `def test_extracts_function(self)`
- `test_extracts_pub_function` (line 211) `def test_extracts_pub_function(self)`
- `test_extracts_struct_and_trait_and_enum` (line 218) `def test_extracts_struct_and_trait_and_enum(self)`
- `test_extracts_use` (line 231) `def test_extracts_use(self)`
- `setUp` (line 239) `def setUp(self)`
- `test_extracts_function` (line 242) `def test_extracts_function(self)`
- `test_extracts_arrow_function` (line 249) `def test_extracts_arrow_function(self)`
- `test_extracts_class` (line 256) `def test_extracts_class(self)`
- `test_extracts_import_and_require` (line 263) `def test_extracts_import_and_require(self)`
- `test_skips_reserved_words` (line 270) `def test_skips_reserved_words(self)`
- `setUp` (line 278) `def setUp(self)`
- `test_extracts_class` (line 281) `def test_extracts_class(self)`
- `test_extracts_method` (line 288) `def test_extracts_method(self)`
- `test_extracts_import` (line 295) `def test_extracts_import(self)`
- `test_abstract_class` (line 301) `def test_abstract_class(self)`
- `setUp` (line 310) `def setUp(self)`
- `test_extracts_class` (line 313) `def test_extracts_class(self)`
- `test_extracts_method` (line 320) `def test_extracts_method(self)`
- `test_extracts_using` (line 327) `def test_extracts_using(self)`
- `test_record_and_interface` (line 333) `def test_record_and_interface(self)`
- `setUp` (line 343) `def setUp(self)`
- `test_extracts_function_with_parentheses` (line 346) `def test_extracts_function_with_parentheses(self)`
- `test_extracts_function_keyword` (line 353) `def test_extracts_function_keyword(self)`
- `setUp` (line 362) `def setUp(self)`
- `test_extracts_function` (line 365) `def test_extracts_function(self)`
- `test_extracts_class` (line 372) `def test_extracts_class(self)`
- `test_extracts_use_and_require` (line 379) `def test_extracts_use_and_require(self)`
- `setUp` (line 388) `def setUp(self)`
- `test_extracts_class` (line 391) `def test_extracts_class(self)`
- `test_extracts_function` (line 398) `def test_extracts_function(self)`
- `test_extracts_import` (line 405) `def test_extracts_import(self)`
- `setUp` (line 413) `def setUp(self)`
- `test_extracts_function` (line 416) `def test_extracts_function(self)`
- `test_extracts_extends` (line 423) `def test_extracts_extends(self)`
- `setUp` (line 431) `def setUp(self)`
- `test_extracts_proc` (line 434) `def test_extracts_proc(self)`
- `test_extracts_type` (line 441) `def test_extracts_type(self)`
- `test_extracts_import` (line 448) `def test_extracts_import(self)`
- `setUp` (line 457) `def setUp(self)`
- `test_extracts_label` (line 460) `def test_extracts_label(self)`
- `test_extracts_multiple_labels` (line 467) `def test_extracts_multiple_labels(self)`
- `test_extracts_includes` (line 475) `def test_extracts_includes(self)`
- `setUp` (line 484) `def setUp(self)`
- `test_returns_c_parser_for_c_extensions` (line 487) `def test_returns_c_parser_for_c_extensions(self)`
- `test_returns_python_parser_for_py` (line 493) `def test_returns_python_parser_for_py(self)`
- `test_returns_none_for_unknown_extension` (line 498) `def test_returns_none_for_unknown_extension(self)`
- `test_returns_rust_parser_for_rs` (line 502) `def test_returns_rust_parser_for_rs(self)`
- `test_case_insensitive_extension` (line 507) `def test_case_insensitive_extension(self)`

#### `test_parsers_new.py`
**Path:** `tests/test_parsers_new.py`
**File Doc:** *Contract tests for the 6 new language parsers.  Validates that Ruby, Swift, Kotlin, Scala, Lua, and Elixir parsers correctly extract symbols, imports, calls, and inheritance edges.*

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
**File Doc:** *Property-based contract tests for all 19 language parsers.  Uses Hypothesis to generate random, malformed, edge-case, and massive inputs to guarantee parsers fail gracefully without crashing.  Run with: hypothesis profile (e.g. ``pytest --hypothesis-show-statistics``).  These tests are skipped if Hypothesis is not installed.*

**Classes:**
- `TestParserHypothesisContract` (line 155) `class TestParserHypothesisContract(TestCase)` - *Property-based contract: parsers never crash on arbitrary input.*
- `TestPythonParserProperty` (line 288) `class TestPythonParserProperty(TestCase)` - *Property-based tests specific to the Python parser (native ast).*
- `_StrategyPlaceholder` (line 45) `class _StrategyPlaceholder` - *Chainable placeholder that never generates data.*
- `_UnavailableStrategies` (line 60) `class _UnavailableStrategies` - *Permissive strategy factory used only when hypothesis is missing.*

**Functions:**
- `_generate_multiline_code` (line 105) `def _generate_multiline_code(lines, line_strategy)` - *Generate source code with a configurable number of lines.*
- `_create_parser` (line 142) `def _create_parser(ext)` - *Create a parser for the given extension.*

**Methods:**
- `test_never_crashes_on_malformed_code` (line 162) `def test_never_crashes_on_malformed_code(self, ext, code)`
- `test_never_crashes_on_unicode_code` (line 180) `def test_never_crashes_on_unicode_code(self, ext, code)`
- `test_empty_code_returns_empty_or_valid` (line 198) `def test_empty_code_returns_empty_or_valid(self, ext)`
- `test_whitespace_code_returns_empty_or_valid` (line 208) `def test_whitespace_code_returns_empty_or_valid(self, ext)`
- `test_never_crashes_on_many_lines` (line 220) `def test_never_crashes_on_many_lines(self, ext, lines)`
- `test_repeated_keywords_no_crash` (line 238) `def test_repeated_keywords_no_crash(self, ext)`
- `test_parser_imports_is_list_of_strings` (line 257) `def test_parser_imports_is_list_of_strings(self, ext)`
- `test_unknown_extension_returns_none` (line 269) `def test_unknown_extension_returns_none(self)`
- `_assert_valid_symbols` (line 275) `def _assert_valid_symbols(self, symbols)`
- `setUp` (line 291) `def setUp(self)`
- `test_python_never_crashes_on_weird_ascii` (line 296) `def test_python_never_crashes_on_weird_ascii(self, code)`
- `test_python_never_crashes_on_any_text` (line 310) `def test_python_never_crashes_on_any_text(self, code)`
- `given` (line 69) `def given()` - *Identity decorator used when hypothesis is unavailable.*
- `settings` (line 75) `def settings()` - *Identity decorator used when hypothesis is unavailable.*
- `__or__` (line 48) `def __or__(self, other)` - *Combine placeholders without evaluating strategies.*
- `__ror__` (line 52) `def __ror__(self, other)` - *Combine placeholders without evaluating strategies.*
- `map` (line 56) `def map(self)` - *Return the placeholder unchanged.*
- `__getattr__` (line 63) `def __getattr__(self, name)` - *Return a builder producing inert placeholders.*
- `wrapper` (line 71) `def wrapper(fn)`
- `wrapper` (line 77) `def wrapper(fn)`
- `builder` (line 65) `def builder()`

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
**File Doc:** *Contract tests for the category theory and ranking system.  Tests cover: - EdgeKind enum contract - Morphism weight computation - Category composition and path finding - TypedGraph stochastic matrix construction - Global PageRank invariants (sum=1, convergence, stability) - Personalized PageRank seed sensitivity - HITS authority/hub separation - Composite scoring formula - Seed generation from queries - Noise penalty for hub names - Projection functors and views - Score explanation formatting*

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
**File Doc:** *Contract tests for README injection into documented projects.  SDD + TDD + BDD: Each test validates a specific behavioral contract of the ReadmeInjector for injecting/deleting knowledge base links.*

**Classes:**
- `TestReadmeInjectorInjectBehavior` (line 16) `class TestReadmeInjectorInjectBehavior(TestCase)` - *BDD: ReadmeInjector injection contract.*
- `TestReadmeInjectorRemoveBehavior` (line 72) `class TestReadmeInjectorRemoveBehavior(TestCase)` - *BDD: ReadmeInjector removal contract.*
- `TestReadmeInjectorFindReadme` (line 105) `class TestReadmeInjectorFindReadme(TestCase)` - *BDD: ReadmeInjector README file detection contract.*
- `TestReadmeInjectorEdgeCases` (line 140) `class TestReadmeInjectorEdgeCases(TestCase)` - *BDD: ReadmeInjector edge case contract.*

**Methods:**
- `setUp` (line 19) `def setUp(self)`
- `tearDown` (line 24) `def tearDown(self)`
- `test_inject_into_markdown_readme_adds_kb_link` (line 28) `def test_inject_into_markdown_readme_adds_kb_link(self)`
- `test_inject_into_rst_readme_adds_kb_link` (line 39) `def test_inject_into_rst_readme_adds_kb_link(self)`
- `test_inject_is_idempotent_does_not_duplicate` (line 48) `def test_inject_is_idempotent_does_not_duplicate(self)`
- `test_inject_no_readme_file_returns_false` (line 59) `def test_inject_no_readme_file_returns_false(self)`
- `test_inject_preserves_existing_content` (line 63) `def test_inject_preserves_existing_content(self)`
- `setUp` (line 75) `def setUp(self)`
- `tearDown` (line 80) `def tearDown(self)`
- `test_remove_strips_injected_section` (line 84) `def test_remove_strips_injected_section(self)`
- `test_remove_without_injection_returns_false` (line 94) `def test_remove_without_injection_returns_false(self)`
- `test_remove_no_readme_returns_false` (line 100) `def test_remove_no_readme_returns_false(self)`
- `setUp` (line 108) `def setUp(self)`
- `tearDown` (line 112) `def tearDown(self)`
- `test_finds_readme_md` (line 116) `def test_finds_readme_md(self)`
- `test_finds_readme_rst` (line 122) `def test_finds_readme_rst(self)`
- `test_prefers_readme_md_over_rst` (line 128) `def test_prefers_readme_md_over_rst(self)`
- `test_returns_none_when_no_readme` (line 135) `def test_returns_none_when_no_readme(self)`
- `setUp` (line 143) `def setUp(self)`
- `tearDown` (line 148) `def tearDown(self)`
- `test_inject_into_empty_readme` (line 152) `def test_inject_into_empty_readme(self)`
- `test_custom_kb_filename_works` (line 160) `def test_custom_kb_filename_works(self)`

#### `test_refactorizer.py`
**Path:** `tests/test_refactorizer.py`
**File Doc:** *Contract tests for the MonolithRefactorizer.  Validates monolithic file detection, refactoring plan generation, symbol grouping, target file suggestion, and script generation.*

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
**File Doc:** *Contract tests for the ImportResolver.  Validates that import strings from various languages are correctly resolved to project file paths, handles edge cases like relative imports, dotted modules, and extensionless imports.*

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
- `test_resolves_c_quoted_header_same_dir` (line 86) `def test_resolves_c_quoted_header_same_dir(self)`
- `test_resolves_c_quoted_header_subdir` (line 93) `def test_resolves_c_quoted_header_subdir(self)`
- `test_resolves_c_extensionless_header` (line 100) `def test_resolves_c_extensionless_header(self)`
- `test_resolves_c_source_from_header_dir` (line 107) `def test_resolves_c_source_from_header_dir(self)`
- `test_resolves_cpp_header_same_dir` (line 114) `def test_resolves_cpp_header_same_dir(self)`
- `test_resolves_c_header_stem_across_dirs` (line 121) `def test_resolves_c_header_stem_across_dirs(self)`
- `test_returns_none_for_c_system_header` (line 128) `def test_returns_none_for_c_system_header(self)`
- `test_resolves_parent_dir_include` (line 135) `def test_resolves_parent_dir_include(self)`
- `test_resolves_parent_dir_include_despite_ambiguous_stem` (line 142) `def test_resolves_parent_dir_include_despite_ambiguous_stem(self)`
- `test_resolves_include_dir_suffix_match` (line 149) `def test_resolves_include_dir_suffix_match(self)`
- `test_returns_none_for_ambiguous_suffix_match` (line 156) `def test_returns_none_for_ambiguous_suffix_match(self)`

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
- `test_module_docstring_extracted_as_file_doc` (line 114) `def test_module_docstring_extracted_as_file_doc(self)`
- `test_multiline_module_docstring_extracted` (line 121) `def test_multiline_module_docstring_extracted(self)`
- `test_coding_cookie_ignored_as_file_doc` (line 129) `def test_coding_cookie_ignored_as_file_doc(self)`
- `test_preprocessor_guards_ignored_as_file_doc` (line 136) `def test_preprocessor_guards_ignored_as_file_doc(self)`
- `test_scan_with_content_returns_content_map` (line 143) `def test_scan_with_content_returns_content_map(self)`
- `test_gitignore_respected_when_enabled` (line 151) `def test_gitignore_respected_when_enabled(self)`
- `test_gitignore_disabled_by_default` (line 162) `def test_gitignore_disabled_by_default(self)`
- `test_gitignore_glob_conversion` (line 171) `def test_gitignore_glob_conversion(self)`

#### `test_security.py`
**Path:** `tests/test_security.py`
**File Doc:** *Contract tests for the static security analysis module.  Tests cover the SecurityFinding data model, per-language rule detection, severity threshold filtering, path validation, and end-to-end scanning of dangerous patterns across all supported languages.*

**Classes:**
- `TestSecurityFinding` (line 21) `class TestSecurityFinding(TestCase)` - *SecurityFinding dataclass contract tests.*
- `TestSecurityAnalyzerConfig` (line 43) `class TestSecurityAnalyzerConfig(TestCase)` - *SecurityAnalyzer configuration contract tests.*
- `TestSecurityAnalyzerRules` (line 64) `class TestSecurityAnalyzerRules(TestCase)` - *Per-language rule detection tests using inline code.*
- `TestSecurityAnalyzerThreshold` (line 295) `class TestSecurityAnalyzerThreshold(TestCase)` - *Severity threshold filtering tests.*
- `TestSecurityAnalyzerPathValidation` (line 327) `class TestSecurityAnalyzerPathValidation(TestCase)` - *Security path validation tests.*
- `TestSecurityAnalyzerSummary` (line 374) `class TestSecurityAnalyzerSummary(TestCase)` - *Security summary output tests.*
- `TestFixGuidance` (line 396) `class TestFixGuidance(TestCase)` - *fix_hint_for remediation hint contract tests.*

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
- `_finding` (line 399) `def _finding(self, cwe)`
- `test_known_cwe_returns_actionable_hint` (line 402) `def test_known_cwe_returns_actionable_hint(self)`
- `test_unknown_cwe_falls_back` (line 408) `def test_unknown_cwe_falls_back(self)`
- `test_empty_cwe_falls_back` (line 413) `def test_empty_cwe_falls_back(self)`

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
**File Doc:** *BDD-style contract tests for taint propagation analysis.  Uses pytest-bdd scenarios to verify multi-step taint propagation workflows: discovering dangerous imports, propagating through the import graph, and generating complete TaintPath results.  These tests are skipped if pytest-bdd is not installed.*

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
**File Doc:** *Contract tests for UML class diagram generation and language code generation.  SDD + TDD + BDD: Each test method validates a specific behavioral contract of the UmlGenerator and its per-language code generators.*

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

#### `test_video.py`
**Path:** `tests/test_video.py`
**File Doc:** *Contract tests for the cinematic overview video renderer.*

**Classes:**
- `TestVideoContract` (line 35) `class TestVideoContract(TestCase)`

**Functions:**
- `_nodes` (line 15) `def _nodes()` - *Build a tiny two-file project for video tests.*
- `_analysis` (line 23) `def _analysis()` - *Build minimal analysis output with one community.*

**Methods:**
- `test_video_collect_counts` (line 36) `def test_video_collect_counts(self)`
- `test_video_collect_empty_project` (line 48) `def test_video_collect_empty_project(self)`
- `test_video_collect_enriched_fields` (line 58) `def test_video_collect_enriched_fields(self)`
- `test_video_build_scenes_durations` (line 78) `def test_video_build_scenes_durations(self)`
- `test_video_all_scenes_render_small_canvas` (line 88) `def test_video_all_scenes_render_small_canvas(self)`
- `test_video_graph_positions_deterministic` (line 106) `def test_video_graph_positions_deterministic(self)`
- `test_video_single_frame_bytes` (line 117) `def test_video_single_frame_bytes(self)`
- `test_video_hash_color_deterministic` (line 132) `def test_video_hash_color_deterministic(self)`
- `test_video_short_label_truncates` (line 138) `def test_video_short_label_truncates(self)`
- `test_video_dependencies_returns_bool` (line 143) `def test_video_dependencies_returns_bool(self)`
- `test_video_disabled_skips_without_render` (line 146) `def test_video_disabled_skips_without_render(self)`

#### `test_wiki.py`
**Path:** `tests/test_wiki.py`

**Classes:**
- `TestWikiConfigContract` (line 49) `class TestWikiConfigContract(TestCase)`
- `TestWikiGenerationContract` (line 65) `class TestWikiGenerationContract(TestCase)`

**Functions:**
- `_make_node` (line 12) `def _make_node(node_id, doc, symbols, language)`
- `_make_symbol` (line 23) `def _make_symbol(name, kind, line, doc)`
- `_make_analysis` (line 27) `def _make_analysis()`
- `_make_nodes` (line 41) `def _make_nodes()`

**Methods:**
- `test_config_defaults` (line 50) `def test_config_defaults(self)`
- `test_config_immutable` (line 58) `def test_config_immutable(self)`
- `test_generate_writes_all_files` (line 66) `def test_generate_writes_all_files(self)`
- `test_community_page_sections` (line 81) `def test_community_page_sections(self)`
- `test_connections_typed_with_confidence` (line 95) `def test_connections_typed_with_confidence(self)`
- `test_fallback_single_community_without_analysis` (line 115) `def test_fallback_single_community_without_analysis(self)`
- `test_report_honest_audit_sections` (line 125) `def test_report_honest_audit_sections(self)`
- `test_index_entry_point` (line 139) `def test_index_entry_point(self)`
- `test_lint_healthy_after_generate` (line 152) `def test_lint_healthy_after_generate(self)`
- `test_deterministic_connections` (line 161) `def test_deterministic_connections(self)`
- `test_privacy_mode_strips_docs` (line 174) `def test_privacy_mode_strips_docs(self)`
- `test_leftover_files_covered_by_orphans_community` (line 184) `def test_leftover_files_covered_by_orphans_community(self)`
- `test_shared_context_link_for_disconnected_communities` (line 194) `def test_shared_context_link_for_disconnected_communities(self)`
- `test_garbage_doc_filtered_from_definition` (line 210) `def test_garbage_doc_filtered_from_definition(self)`
- `test_definition_names_core_file` (line 217) `def test_definition_names_core_file(self)`
- `test_duplicate_community_labels_disambiguated` (line 240) `def test_duplicate_community_labels_disambiguated(self)`
- `test_duplicate_god_basenames_disambiguated` (line 259) `def test_duplicate_god_basenames_disambiguated(self)`
- `test_oversized_community_grouped_by_directory` (line 278) `def test_oversized_community_grouped_by_directory(self)`
- `test_large_files_flagged_in_index_and_report` (line 302) `def test_large_files_flagged_in_index_and_report(self)`
- `test_stale_pages_pruned_on_regenerate` (line 323) `def test_stale_pages_pruned_on_regenerate(self)`
- `test_risks_carry_fix_hint_scope_and_closed_cycle` (line 335) `def test_risks_carry_fix_hint_scope_and_closed_cycle(self)`
- `test_duplicate_symbol_scope_detected` (line 365) `def test_duplicate_symbol_scope_detected(self)`
- `test_no_duplicate_link_for_disjoint_scopes` (line 388) `def test_no_duplicate_link_for_disjoint_scopes(self)`
- `test_garbage_purpose_filtered` (line 408) `def test_garbage_purpose_filtered(self)`
