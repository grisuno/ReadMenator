# ReadMenator Architecture and Execution Flows

[Back to index](index.md)

## Architecture Overview

7 components stacked in 5 dependency tiers (weighted Eades-Lin-Smyth ordering: arrows point from dependent to dependency, top to bottom). Labels are import counts, thick arrows the top quartile; 7 transitively implied edges are omitted. Dashed red arrows are upward dependencies: the smallest set of imports that closes every cycle and breaks the layering. Cyan components hold entry points.

Upward dependencies to fix first: `readmenator: _diagrams` -> `readmenator: _pipeline` (5 imports); `readmenator/parsers` -> `readmenator: _graphrag` (4 imports); `readmenator: _apidocs` -> `readmenator: _diagrams` (3 imports); `readmenator: _graphrag` -> `readmenator: _diagrams` (2 imports); `readmenator: _apidocs` -> `readmenator: _pipeline` (2 imports); `readmenator/parsers` -> `readmenator: _diagrams` (1 imports)

```mermaid
flowchart TB
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef comp fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef cyc fill:#1f1530,stroke:#f472b6,color:#fce7f3,stroke-width:2px;
    subgraph tier_0["Tier 1 (entry / high level)"]
        direction LR
        c_c3["readmenator: _pipeline<br/>14 files, 192 symbols<br/>Core / utility, core _pipeline.py"]:::cyc
        c_d__root_["(root)<br/>1 files, 37 symbols<br/>Core / utility, core readmenator_orchestrator.py"]:::comp
    end
    subgraph tier_1["Tier 2"]
        direction LR
        c_c2["readmenator: _diagrams<br/>20 files, 502 symbols<br/>Core / utility, core _diagrams.py"]:::entry
    end
    subgraph tier_2["Tier 3"]
        direction LR
        c_c4["readmenator: _apidocs<br/>9 files, 247 symbols<br/>Core / utility, core _apidocs.py"]:::cyc
        c_c5["readmenator: _agent_injector<br/>2 files, 23 symbols<br/>Infrastructure, core _agent_injector.py"]:::comp
    end
    subgraph tier_3["Tier 4"]
        direction LR
        c_c0["readmenator: _graphrag<br/>20 files, 338 symbols<br/>Core / utility, core _graphrag.py"]:::cyc
    end
    subgraph tier_4["Tier 5 (foundation)"]
        direction LR
        c_c1["readmenator/parsers<br/>26 files, 95 symbols<br/>Core / utility, core _models.py"]:::cyc
    end
    c_c3 ==>|"9"| c_c2
    c_c2 -->|"3"| c_c4
    c_c2 -->|"1"| c_c5
    c_c4 -->|"6"| c_c0
    c_c0 ==>|"15"| c_c1
    c_c2 <-.-|"2 upward"| c_c0
    c_c0 <-.-|"4 upward"| c_c1
    c_c2 <-.-|"1 upward"| c_c1
    c_c3 <-.-|"5 upward"| c_c2
    c_c2 <-.-|"3 upward"| c_c4
    c_c3 <-.-|"2 upward"| c_c4
    linkStyle 5,6,7,8,9,10 stroke:#f87171,stroke-width:2px;
    c_c3 ~~~ c_c2
    c_c2 ~~~ c_c4
    c_c4 ~~~ c_c0
    c_c0 ~~~ c_c1
```

---

## Execution Flows

Entry points are scored from `__main__` guards, `main` functions, entry-style names and files, and call-graph sources. Each flow walks resolved calls in call-site order (depth <= 4, <= 40 steps); numbers give the call order, dotted arrows revisit an already expanded callee, red arrows are recursion.

### `__main__.main`

`readmenator/__main__.py:150`, score 9: entry-style name `main`; defined in entry file `__main__.py`; called from the `__main__` guard.

Control flow:

```mermaid
flowchart TD
    classDef term fill:#0e7490,stroke:#22d3ee,color:#ecfeff;
    classDef dec fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef stop fill:#3f1d1d,stroke:#f87171,color:#fee2e2;
    s1(["start __main__.main"]):::term
    s2{"'--test' in sys.argv?"}:::dec
    s1 --> s2
    s3["_run_tests()"]
    s2 -->|"yes"| s3
    s4(["return"]):::term
    s3 --> s4
    s5{{"for (flag, lang) in uml_lang_flags.items()"}}:::dec
    s2 -->|"no"| s5
    s6{"flag in sys.argv?"}:::dec
    s5 -->|"each"| s6
    s7["break"]
    s6 -->|"yes"| s7
    s6 -.->|"no"| s5
    s8{"uml_codegen_flag?"}:::dec
    s5 -->|"done"| s8
    s9["build_parser()#59; readmenatorApplication()#59; gen..."]
    s8 -->|"yes"| s9
    s10(["return"]):::term
    s9 --> s10
    s11{"len(sys.argv) #gt; 2 and sys.argv[1] != '--rebui..."}:::dec
    s8 -->|"no"| s11
    s12["readmenatorApplication()"]
    s11 -->|"yes"| s12
    s13{"switch command"}:::dec
    s12 --> s13
    s14["query()"]
    s13 -->|"'query' if len(sys.argv) #gt;= 4"| s14
    s15(["return"]):::term
    s14 --> s15
    s16["explain()"]
    s13 -->|"'explain' if len(sys.argv) #gt;= 4"| s16
    s17(["return"]):::term
    s16 --> s17
    s18["find_path()"]
    s13 -->|"'path' if len(sys.argv) #gt;= 5"| s18
    s19(["return"]):::term
    s18 --> s19
    s20["summary()"]
    s13 -->|"'summary' / 'sum' / 'info'"| s20
    s21(["return"]):::term
    s20 --> s21
    s22["update()"]
    s13 -->|"'update'"| s22
    s23(["return"]):::term
    s22 --> s23
    s24["export()"]
    s13 -->|"'export'"| s24
    s25(["return"]):::term
    s24 --> s25
    s26["export_graphml()"]
    s13 -->|"'graphml'"| s26
    s27(["return"]):::term
    s26 --> s27
    s28["export_cypher()"]
    s13 -->|"'cypher'"| s28
    s29(["return"]):::term
    s28 --> s29
    s30["export_obsidian()"]
    s13 -->|"'obsidian'"| s30
    s31(["return"]):::term
    s30 --> s31
    s32["export_wiki()"]
    s13 -->|"'wiki'"| s32
    s33(["return"]):::term
    s32 --> s33
    s34["lint_wiki()"]
    s13 -->|"'lint-wiki'"| s34
    s35(["return"]):::term
    s34 --> s35
    s36["watch()"]
    s13 -->|"'watch'"| s36
    s37(["return"]):::term
    s36 --> s37
    s38["detect_layers()"]
    s13 -->|"'layers'"| s38
    s39(["return"]):::term
    s38 --> s39
    s40["analyze()"]
    s13 -->|"'analyze'"| s40
    s41{{"for q in result.suggested_questions"}}:::dec
    s40 --> s41
    s41 -.->|"each"| s41
    s42(["return"]):::term
    s41 -->|"done"| s42
    s43["audit()"]
    s13 -->|"'audit'"| s43
    s44(["return"]):::term
    s43 --> s44
    s45["audit_deep()"]
    s13 -->|"'audit-deep'"| s45
    s46(["return"]):::term
    s45 --> s46
    s47["export_sarif()"]
    s13 -->|"'export-sarif'"| s47
    s48(["return"]):::term
    s47 --> s48
    s49["export_rules()"]
    s13 -->|"'export-rules'"| s49
    s50(["return"]):::term
    s49 --> s50
    s51["_scan()#59; render_mermaid_class_diagram()"]
    s13 -->|"'uml'"| s51
    s52{"uml_diagram?"}:::dec
    s51 --> s52
    s53(["return"]):::term
    s52 -->|"yes"| s53
    s52 -->|"no"| s53
    s54(["return"]):::term
    s13 -->|"'serve'"| s54
    s55["lint()"]
    s13 -->|"'lint'"| s55
    s56(["return"]):::term
    s55 --> s56
    s57["strip_dead_code()"]
    s13 -->|"'strip-dead-code'"| s57
    s58{{"for r in reports"}}:::dec
    s57 --> s58
    s58 -.->|"each"| s58
    s59(["return"]):::term
    s58 -->|"done"| s59
    s60["generate_cursorrules()"]
    s13 -->|"'generate-rules'"| s60
    s61(["return"]):::term
    s60 --> s61
    s62(["end"]):::term
    s13 -->|"otherwise"| s62
    s11 -->|"no"| s62
    trunc["... truncated at FLOW_CFG_MAX_NODES=60"]
    s1 -.- trunc
```

Call tree:

```mermaid
flowchart LR
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef ext fill:#111827,stroke:#a78bfa,color:#ede9fe;
    classDef fn fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    f_readmenator___main___py__main["__main__.main"]:::entry
    f_readmenator___main___py___run_tests["__main__._run_tests"]:::fn
    f_readmenator___main___py__build_parser["__main__.build_parser"]:::fn
    f_readmenator__app_py__readmenatorApplication["_app.readmenatorApplication"]:::ext
    f_readmenator__app_py__generate_uml_code["_app.readmenatorApplication.generate_uml_code"]:::ext
    f_readmenator__app_py___scan["_app.readmenatorApplication._scan"]:::ext
    f_readmenator__app_py___resolve_imports["_app.readmenatorApplication._resolve_imports"]:::ext
    f_readmenator__resolver_py__ImportResolver["_resolver.ImportResolver"]:::ext
    f_readmenator__resolver_py__resolve["_resolver.ImportResolver.resolve"]:::ext
    f_readmenator__models_py__Edge["_models.Edge"]:::ext
    f_readmenator__app_py__query["_app.readmenatorApplication.query"]:::ext
    f_readmenator__query_py__QueryEngine["_query.QueryEngine"]:::ext
    f_readmenator__query_py__query["_query.QueryEngine.query"]:::ext
    f_readmenator__app_py__explain["_app.readmenatorApplication.explain"]:::ext
    f_readmenator__query_py__explain["_query.QueryEngine.explain"]:::ext
    f_readmenator__query_py__find_symbol["_query.QueryEngine.find_symbol"]:::ext
    f_readmenator__query_py___find_incoming_imports["_query.QueryEngine._find_incoming_imports"]:::ext
    f_readmenator__app_py__find_path["_app.readmenatorApplication.find_path"]:::ext
    f_readmenator__query_py__find_path["_query.QueryEngine.find_path"]:::ext
    f_readmenator__query_py___make_bidirectional["_query.QueryEngine._make_bidirectional"]:::ext
    f_readmenator__query_py___bfs_shortest_path["_query.QueryEngine._bfs_shortest_path"]:::ext
    f_readmenator__app_py__summary["_app.readmenatorApplication.summary"]:::ext
    f_readmenator__query_py__summary["_query.QueryEngine.summary"]:::ext
    f_readmenator__app_py__update["_app.readmenatorApplication.update"]:::ext
    f_readmenator__cache_py__FileCache["_cache.FileCache"]:::ext
    f_readmenator__app_py___scan_for_cache["_app.readmenatorApplication._scan_for_cache"]:::ext
    f_readmenator__cache_py__load["_cache.FileCache.load"]:::ext
    f_readmenator__cache_py__prune_deleted["_cache.FileCache.prune_deleted"]:::ext
    f_readmenator__cache_py__save["_cache.FileCache.save"]:::ext
    f_readmenator__cache_py___prune_analysis_cache["_cache.FileCache._prune_analysis_cache"]:::ext
    f_readmenator__cache_py__compute_hashes["_cache.FileCache.compute_hashes"]:::ext
    f_readmenator__cache_py__compute_hash["_cache.FileCache.compute_hash"]:::ext
    f_readmenator___main___py__main -->|"1"| f_readmenator___main___py___run_tests
    f_readmenator___main___py__main -->|"2"| f_readmenator___main___py__build_parser
    f_readmenator___main___py__main -->|"3"| f_readmenator__app_py__readmenatorApplication
    f_readmenator___main___py__main -->|"4"| f_readmenator__app_py__generate_uml_code
    f_readmenator__app_py__generate_uml_code -->|"1"| f_readmenator__app_py___scan
    f_readmenator__app_py___scan -->|"1"| f_readmenator__app_py___resolve_imports
    f_readmenator__app_py___resolve_imports -->|"1"| f_readmenator__resolver_py__ImportResolver
    f_readmenator__app_py___resolve_imports -->|"2"| f_readmenator__resolver_py__resolve
    f_readmenator__app_py___resolve_imports -->|"3"| f_readmenator__models_py__Edge
    f_readmenator___main___py__main -->|"5"| f_readmenator__app_py__query
    f_readmenator__app_py__query -.-> f_readmenator__app_py___scan
    f_readmenator__app_py__query -->|"1"| f_readmenator__query_py__QueryEngine
    f_readmenator__app_py__query -->|"2"| f_readmenator__query_py__query
    f_readmenator___main___py__main -->|"6"| f_readmenator__app_py__explain
    f_readmenator__app_py__explain -.-> f_readmenator__app_py___scan
    f_readmenator__app_py__explain -.-> f_readmenator__query_py__QueryEngine
    f_readmenator__app_py__explain -->|"1"| f_readmenator__query_py__explain
    f_readmenator__query_py__explain -->|"1"| f_readmenator__query_py__find_symbol
    f_readmenator__query_py__explain -->|"2"| f_readmenator__query_py___find_incoming_imports
    f_readmenator___main___py__main -->|"7"| f_readmenator__app_py__find_path
    f_readmenator__app_py__find_path -.-> f_readmenator__app_py___scan
    f_readmenator__app_py__find_path -.-> f_readmenator__query_py__QueryEngine
    f_readmenator__app_py__find_path -->|"1"| f_readmenator__query_py__find_path
    f_readmenator__query_py__find_path -.-> f_readmenator__query_py__find_symbol
    f_readmenator__query_py__find_path -->|"1"| f_readmenator__query_py___make_bidirectional
    f_readmenator__query_py__find_path -->|"2"| f_readmenator__query_py___bfs_shortest_path
    f_readmenator___main___py__main -->|"8"| f_readmenator__app_py__summary
    f_readmenator__app_py__summary -.-> f_readmenator__app_py___scan
    f_readmenator__app_py__summary -.-> f_readmenator__query_py__QueryEngine
    f_readmenator__app_py__summary -->|"1"| f_readmenator__query_py__summary
    f_readmenator___main___py__main -->|"9"| f_readmenator__app_py__update
    f_readmenator__app_py__update -->|"1"| f_readmenator__cache_py__FileCache
    f_readmenator__app_py__update -->|"2"| f_readmenator__app_py___scan_for_cache
    f_readmenator__app_py___scan_for_cache -->|"1"| f_readmenator__cache_py__load
    f_readmenator__app_py___scan_for_cache -->|"2"| f_readmenator__cache_py__prune_deleted
    f_readmenator__cache_py__prune_deleted -.-> f_readmenator__cache_py__load
    f_readmenator__cache_py__prune_deleted -->|"1"| f_readmenator__cache_py__save
    f_readmenator__cache_py__prune_deleted -->|"2"| f_readmenator__cache_py___prune_analysis_cache
    f_readmenator__app_py___scan_for_cache -->|"3"| f_readmenator__cache_py__compute_hashes
    f_readmenator__cache_py__compute_hashes -->|"1"| f_readmenator__cache_py__compute_hash
```

Cross-file sequence:

```mermaid
sequenceDiagram
    autonumber
    participant p_readmenator___main___py as __main__.py
    participant p_readmenator__app_py as _app.py
    participant p_readmenator__resolver_py as _resolver.py
    participant p_readmenator__models_py as _models.py
    participant p_readmenator__query_py as _query.py
    participant p_readmenator__cache_py as _cache.py
    p_readmenator___main___py->>p_readmenator__app_py: readmenatorApplication()
    p_readmenator___main___py->>p_readmenator__app_py: generate_uml_code()
    p_readmenator__app_py->>p_readmenator__resolver_py: ImportResolver()
    p_readmenator__app_py->>p_readmenator__resolver_py: resolve()
    p_readmenator__app_py->>p_readmenator__models_py: Edge()
    p_readmenator___main___py->>p_readmenator__app_py: query()
    p_readmenator__app_py->>p_readmenator__query_py: QueryEngine()
    p_readmenator__app_py->>p_readmenator__query_py: query()
    p_readmenator___main___py->>p_readmenator__app_py: explain()
    p_readmenator__app_py->>p_readmenator__query_py: explain()
    p_readmenator___main___py->>p_readmenator__app_py: find_path()
    p_readmenator__app_py->>p_readmenator__query_py: find_path()
    p_readmenator___main___py->>p_readmenator__app_py: summary()
    p_readmenator__app_py->>p_readmenator__query_py: summary()
    p_readmenator___main___py->>p_readmenator__app_py: update()
    p_readmenator__app_py->>p_readmenator__cache_py: FileCache()
    p_readmenator__app_py->>p_readmenator__cache_py: load()
    p_readmenator__app_py->>p_readmenator__cache_py: prune_deleted()
    p_readmenator__app_py->>p_readmenator__cache_py: compute_hashes()
```

### `_mcp_server (__main__)`

`readmenator/_mcp_server.py:1090`, score 8: `if __name__ == "__main__"` guard.

Control flow:

```mermaid
flowchart TD
    classDef term fill:#0e7490,stroke:#22d3ee,color:#ecfeff;
    classDef dec fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef stop fill:#3f1d1d,stroke:#f87171,color:#fee2e2;
    s1(["start _mcp_server (__main__)"]):::term
    s2["main()"]
    s1 --> s2
    s3(["end"]):::term
    s2 --> s3
```

Call tree:

```mermaid
flowchart LR
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef ext fill:#111827,stroke:#a78bfa,color:#ede9fe;
    classDef fn fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    f_readmenator__mcp_server_py___main_["_mcp_server (__main__)"]:::entry
    f_readmenator__mcp_server_py__main["_mcp_server.main"]:::fn
    f_readmenator__config_py__Config["_config.Config"]:::ext
    f_readmenator__app_py__readmenatorApplication["_app.readmenatorApplication"]:::ext
    f_readmenator__app_py__run["_app.readmenatorApplication.run"]:::ext
    f_readmenator__app_py___resolve_imports["_app.readmenatorApplication._resolve_imports"]:::ext
    f_readmenator__resolver_py__ImportResolver["_resolver.ImportResolver"]:::ext
    f_readmenator__resolver_py__resolve["_resolver.ImportResolver.resolve"]:::ext
    f_readmenator__models_py__Edge["_models.Edge"]:::ext
    f_readmenator__layers_py__LayerDetector["_layers.LayerDetector"]:::ext
    f_readmenator__layers_py__detect["_layers.LayerDetector.detect"]:::ext
    f_readmenator__layers_py___classify_file["_layers.LayerDetector._classify_file"]:::ext
    f_readmenator__layers_py__layer_summary["_layers.LayerDetector.layer_summary"]:::ext
    f_readmenator__pipeline_py__run["_pipeline.DeepAnalysisRunner.run"]:::ext
    f_readmenator__models_py__AnalysisResultV2["_models.AnalysisResultV2"]:::ext
    f_readmenator__pipeline_py__build_typed_graph["_pipeline.AnalyzerFactory.build_typed_graph"]:::ext
    f_readmenator__category_py__build_category_from_edges["_category.build_category_from_edges"]:::ext
    f_readmenator__category_py__TypedGraph["_category.TypedGraph"]:::ext
    f_readmenator__pipeline_py__make_ranker["_pipeline.AnalyzerFactory.make_ranker"]:::ext
    f_readmenator__rank_py__RankConfig["_rank.RankConfig"]:::ext
    f_readmenator__rank_py__CompositeRanker["_rank.CompositeRanker"]:::ext
    f_readmenator__query_py__QueryEngine["_query.QueryEngine"]:::ext
    f_readmenator__query_py__ranked_query["_query.QueryEngine.ranked_query"]:::ext
    f_readmenator__query_py___init_default_ranker["_query.QueryEngine._init_default_ranker"]:::ext
    f_readmenator__rank_py__build_seeds_from_query["_rank.build_seeds_from_query"]:::ext
    f_readmenator__query_py___estimate_test_coverage["_query.QueryEngine._estimate_test_coverage"]:::ext
    f_readmenator__query_py___estimate_doc_coverage["_query.QueryEngine._estimate_doc_coverage"]:::ext
    f_readmenator__rank_py__rank["_rank.CompositeRanker.rank"]:::ext
    f_readmenator__cache_py__FileCache["_cache.FileCache"]:::ext
    f_readmenator__cache_py__compute_hashes["_cache.FileCache.compute_hashes"]:::ext
    f_readmenator__cache_py__compute_hash["_cache.FileCache.compute_hash"]:::ext
    f_readmenator__cache_py__save["_cache.FileCache.save"]:::ext
    f_readmenator__cache_py__save_analysis["_cache.FileCache.save_analysis"]:::ext
    f_readmenator__app_py___write_sidecar_outputs["_app.readmenatorApplication._write_sidecar_ou..."]:::ext
    f_readmenator__app_py___maybe_write_memory["_app.readmenatorApplication._maybe_write_memory"]:::ext
    f_readmenator__app_py___maybe_write_graphrag["_app.readmenatorApplication._maybe_write_grap..."]:::ext
    f_readmenator__app_py___memory_notes["_app.readmenatorApplication._memory_notes"]:::ext
    f_readmenator__app_py___maybe_write_apidocs["_app.readmenatorApplication._maybe_write_apidocs"]:::ext
    f_readmenator__app_py___architecture_markdown["_app.readmenatorApplication._architecture_mar..."]:::ext
    f_readmenator__app_py___maybe_export_video["_app.readmenatorApplication._maybe_export_video"]:::ext
    f_readmenator__mcp_server_py___main_ -->|"1"| f_readmenator__mcp_server_py__main
    f_readmenator__mcp_server_py__main -->|"1"| f_readmenator__config_py__Config
    f_readmenator__mcp_server_py__main -->|"2"| f_readmenator__app_py__readmenatorApplication
    f_readmenator__mcp_server_py__main -->|"3"| f_readmenator__app_py__run
    f_readmenator__app_py__run -->|"1"| f_readmenator__app_py___resolve_imports
    f_readmenator__app_py___resolve_imports -->|"1"| f_readmenator__resolver_py__ImportResolver
    f_readmenator__app_py___resolve_imports -->|"2"| f_readmenator__resolver_py__resolve
    f_readmenator__app_py___resolve_imports -->|"3"| f_readmenator__models_py__Edge
    f_readmenator__app_py__run -->|"2"| f_readmenator__layers_py__LayerDetector
    f_readmenator__app_py__run -->|"3"| f_readmenator__layers_py__detect
    f_readmenator__layers_py__detect -->|"1"| f_readmenator__layers_py___classify_file
    f_readmenator__app_py__run -->|"4"| f_readmenator__layers_py__layer_summary
    f_readmenator__app_py__run -->|"5"| f_readmenator__pipeline_py__run
    f_readmenator__pipeline_py__run -->|"1"| f_readmenator__models_py__AnalysisResultV2
    f_readmenator__app_py__run -->|"6"| f_readmenator__pipeline_py__build_typed_graph
    f_readmenator__pipeline_py__build_typed_graph -->|"1"| f_readmenator__category_py__build_category_from_edges
    f_readmenator__pipeline_py__build_typed_graph -->|"2"| f_readmenator__category_py__TypedGraph
    f_readmenator__app_py__run -->|"7"| f_readmenator__pipeline_py__make_ranker
    f_readmenator__pipeline_py__make_ranker -->|"1"| f_readmenator__rank_py__RankConfig
    f_readmenator__pipeline_py__make_ranker -->|"2"| f_readmenator__rank_py__CompositeRanker
    f_readmenator__app_py__run -->|"8"| f_readmenator__query_py__QueryEngine
    f_readmenator__app_py__run -->|"9"| f_readmenator__query_py__ranked_query
    f_readmenator__query_py__ranked_query -->|"1"| f_readmenator__query_py___init_default_ranker
    f_readmenator__query_py__ranked_query -->|"2"| f_readmenator__rank_py__build_seeds_from_query
    f_readmenator__query_py__ranked_query -->|"3"| f_readmenator__category_py__build_category_from_edges
    f_readmenator__query_py__ranked_query -->|"4"| f_readmenator__query_py___estimate_test_coverage
    f_readmenator__query_py__ranked_query -->|"5"| f_readmenator__query_py___estimate_doc_coverage
    f_readmenator__query_py__ranked_query -->|"6"| f_readmenator__rank_py__rank
    f_readmenator__app_py__run -->|"10"| f_readmenator__cache_py__FileCache
    f_readmenator__app_py__run -->|"11"| f_readmenator__cache_py__compute_hashes
    f_readmenator__cache_py__compute_hashes -->|"1"| f_readmenator__cache_py__compute_hash
    f_readmenator__app_py__run -->|"12"| f_readmenator__cache_py__save
    f_readmenator__app_py__run -->|"13"| f_readmenator__cache_py__save_analysis
    f_readmenator__app_py__run -->|"14"| f_readmenator__app_py___write_sidecar_outputs
    f_readmenator__app_py__run -->|"15"| f_readmenator__app_py___maybe_write_memory
    f_readmenator__app_py__run -->|"16"| f_readmenator__app_py___maybe_write_graphrag
    f_readmenator__app_py___maybe_write_graphrag -->|"1"| f_readmenator__app_py___memory_notes
    f_readmenator__app_py__run -->|"17"| f_readmenator__app_py___maybe_write_apidocs
    f_readmenator__app_py___maybe_write_apidocs -->|"1"| f_readmenator__app_py___architecture_markdown
    f_readmenator__app_py__run -->|"18"| f_readmenator__app_py___maybe_export_video
```

Cross-file sequence:

```mermaid
sequenceDiagram
    autonumber
    participant p_readmenator__mcp_server_py as _mcp_server.py
    participant p_readmenator__config_py as _config.py
    participant p_readmenator__app_py as _app.py
    participant p_readmenator__resolver_py as _resolver.py
    participant p_readmenator__models_py as _models.py
    participant p_readmenator__layers_py as _layers.py
    participant p_readmenator__pipeline_py as _pipeline.py
    participant p_readmenator__category_py as _category.py
    participant p_readmenator__rank_py as _rank.py
    participant p_readmenator__query_py as _query.py
    participant p_readmenator__cache_py as _cache.py
    p_readmenator__mcp_server_py->>p_readmenator__config_py: Config()
    p_readmenator__mcp_server_py->>p_readmenator__app_py: readmenatorApplication()
    p_readmenator__mcp_server_py->>p_readmenator__app_py: run()
    p_readmenator__app_py->>p_readmenator__resolver_py: ImportResolver()
    p_readmenator__app_py->>p_readmenator__resolver_py: resolve()
    p_readmenator__app_py->>p_readmenator__models_py: Edge()
    p_readmenator__app_py->>p_readmenator__layers_py: LayerDetector()
    p_readmenator__app_py->>p_readmenator__layers_py: detect()
    p_readmenator__app_py->>p_readmenator__layers_py: layer_summary()
    p_readmenator__app_py->>p_readmenator__pipeline_py: run()
    p_readmenator__pipeline_py->>p_readmenator__models_py: AnalysisResultV2()
    p_readmenator__app_py->>p_readmenator__pipeline_py: build_typed_graph()
    p_readmenator__pipeline_py->>p_readmenator__category_py: build_category_from_edges()
    p_readmenator__pipeline_py->>p_readmenator__category_py: TypedGraph()
    p_readmenator__app_py->>p_readmenator__pipeline_py: make_ranker()
    p_readmenator__pipeline_py->>p_readmenator__rank_py: RankConfig()
    p_readmenator__pipeline_py->>p_readmenator__rank_py: CompositeRanker()
    p_readmenator__app_py->>p_readmenator__query_py: QueryEngine()
    p_readmenator__app_py->>p_readmenator__query_py: ranked_query()
    p_readmenator__query_py->>p_readmenator__rank_py: build_seeds_from_query()
    p_readmenator__query_py->>p_readmenator__category_py: build_category_from_edges()
    p_readmenator__query_py->>p_readmenator__rank_py: rank()
    p_readmenator__app_py->>p_readmenator__cache_py: FileCache()
    p_readmenator__app_py->>p_readmenator__cache_py: compute_hashes()
    p_readmenator__app_py->>p_readmenator__cache_py: save()
    p_readmenator__app_py->>p_readmenator__cache_py: save_analysis()
```

### `readmenator_orchestrator (__main__)`

`readmenator_orchestrator.py:516`, score 8: `if __name__ == "__main__"` guard.

Control flow:

```mermaid
flowchart TD
    classDef term fill:#0e7490,stroke:#22d3ee,color:#ecfeff;
    classDef dec fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef stop fill:#3f1d1d,stroke:#f87171,color:#fee2e2;
    s1(["start readmenator_orchestrator (__main__)"]):::term
    s2["main()"]
    s1 --> s2
    s3(["end"]):::term
    s2 --> s3
```

Call tree:

```mermaid
flowchart LR
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef ext fill:#111827,stroke:#a78bfa,color:#ede9fe;
    classDef fn fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    f_readmenator_orchestrator_py___main_["readmenator_orchestrator (__main__)"]:::entry
    f_readmenator_orchestrator_py__main["readmenator_orchestrator.main"]:::fn
    f_readmenator_orchestrator_py__parse_arguments["readmenator_orchestrator.parse_arguments"]:::fn
    f_readmenator_orchestrator_py__Config["readmenator_orchestrator.Config"]:::fn
    f_readmenator_orchestrator_py__Orchestrator["readmenator_orchestrator.Orchestrator"]:::fn
    f_readmenator_orchestrator_py__run["readmenator_orchestrator.Orchestrator.run"]:::fn
    f_readmenator_orchestrator_py__list_repos["readmenator_orchestrator.GitHubClient.list_repos"]:::fn
    f_readmenator_orchestrator_py___safe_env["readmenator_orchestrator._safe_env"]:::fn
    f_readmenator_orchestrator_py__close_existing_prs["readmenator_orchestrator.GitHubClient.close_e..."]:::fn
    f_readmenator_orchestrator_py___validate_repo_name["readmenator_orchestrator._validate_repo_name"]:::fn
    f_readmenator_orchestrator_py___validate_branch_name["readmenator_orchestrator._validate_branch_name"]:::fn
    f_readmenator_orchestrator_py__delete_remote_branch["readmenator_orchestrator.GitHubClient.delete_..."]:::fn
    f_readmenator_orchestrator_py__process["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___get_default_branch["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___clone_repository["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___run_readmenator["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___copy_to_docs_dir["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___commit_and_push["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___cleanup_temp_dir["readmenator_orchestrator.RepositoryProcessor...."]:::fn
    f_readmenator_orchestrator_py___main_ -->|"1"| f_readmenator_orchestrator_py__main
    f_readmenator_orchestrator_py__main -->|"1"| f_readmenator_orchestrator_py__parse_arguments
    f_readmenator_orchestrator_py__main -->|"2"| f_readmenator_orchestrator_py__Config
    f_readmenator_orchestrator_py__main -->|"3"| f_readmenator_orchestrator_py__Orchestrator
    f_readmenator_orchestrator_py__main -->|"4"| f_readmenator_orchestrator_py__run
    f_readmenator_orchestrator_py__run -->|"1"| f_readmenator_orchestrator_py__list_repos
    f_readmenator_orchestrator_py__list_repos -->|"1"| f_readmenator_orchestrator_py___safe_env
    f_readmenator_orchestrator_py__run -->|"2"| f_readmenator_orchestrator_py__close_existing_prs
    f_readmenator_orchestrator_py__close_existing_prs -->|"1"| f_readmenator_orchestrator_py___validate_repo_name
    f_readmenator_orchestrator_py__close_existing_prs -->|"2"| f_readmenator_orchestrator_py___validate_branch_name
    f_readmenator_orchestrator_py__close_existing_prs -->|"3"| f_readmenator_orchestrator_py___safe_env
    f_readmenator_orchestrator_py__run -->|"3"| f_readmenator_orchestrator_py__delete_remote_branch
    f_readmenator_orchestrator_py__delete_remote_branch -->|"1"| f_readmenator_orchestrator_py___validate_repo_name
    f_readmenator_orchestrator_py__delete_remote_branch -->|"2"| f_readmenator_orchestrator_py___validate_branch_name
    f_readmenator_orchestrator_py__delete_remote_branch -->|"3"| f_readmenator_orchestrator_py___safe_env
    f_readmenator_orchestrator_py__run -->|"4"| f_readmenator_orchestrator_py__process
    f_readmenator_orchestrator_py__process -->|"1"| f_readmenator_orchestrator_py___validate_repo_name
    f_readmenator_orchestrator_py__process -->|"2"| f_readmenator_orchestrator_py___get_default_branch
    f_readmenator_orchestrator_py__process -->|"3"| f_readmenator_orchestrator_py___clone_repository
    f_readmenator_orchestrator_py__process -->|"4"| f_readmenator_orchestrator_py___run_readmenator
    f_readmenator_orchestrator_py__process -->|"5"| f_readmenator_orchestrator_py___copy_to_docs_dir
    f_readmenator_orchestrator_py__process -->|"6"| f_readmenator_orchestrator_py___commit_and_push
    f_readmenator_orchestrator_py__process -->|"7"| f_readmenator_orchestrator_py___cleanup_temp_dir
```

---
