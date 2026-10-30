# ReadMenator Development Contract

## Project Structure

```
readmenator/
  __init__.py       - Public API exports
  __main__.py       - CLI entry point with argument dispatch
  _config.py        - Immutable Config dataclass (all settings, no magic numbers)
  _models.py        - Symbol, Node, Edge, AnalysisResult, CommunityResult, AnalysisResultV2, TaintPath, LinterViolation, DeadCodeReport, RefactoringPlan, RefactoringAction, etc.
  parsers/          - Language parsers package (Strategy pattern, 1 file per language)
    __init__.py     - ParserFactory (create_parser) + extension registry
    _base.py        - LanguageParser base class with docstring/signature extraction
    _c.py, _python.py, _go.py, _rust.py, _javascript.py, _java.py,
    _csharp.py, _shell.py, _php.py, _dart.py, _gdscript.py, _nim.py,
    _assembly.py, _ruby.py, _swift.py, _kotlin.py, _scala.py, _lua.py,
    _elixir.py      - 19 per-language parsers
  _scanner.py       - Secure directory traversal, file-level docs, call/inherit edges, gitignore, privacy mode
  _resolver.py      - Import path resolver (raw import strings -> project file paths)
  _mermaid.py       - Mermaid graph renderer with community subgraphs and internal edges
  _documentation.py - KNOWLEDGE_BASE.md with TOC, dashboard, layers, communities, CPG, taint, hotspots, etc.
  _query.py         - QueryEngine: query, explain, bidirectional path dependency tracing
  _analyzer.py      - Graph analysis: communities, god nodes, surprising connections
  _cache.py         - SHA256 content hash cache for incremental updates
  _exporter.py      - Export: JSON, HTML (vis.js), SVG, GraphML, Obsidian vault
  _layers.py        - Architectural layer detection (5-layer model)
  _layer_rules.py   - Architecture violation detection engine
  _linter.py        - Architecture linter: file length, cross-layer, circular dependencies
  _dead_code.py     - Dead code detection: orphaned symbols with zero in-degree
  _cursorrules_generator.py - Dynamic .cursorrules generator for AI assistants
  _refactorizer.py  - Monolithic file refactoring planner
  _watcher.py       - Filesystem polling watcher for auto-rebuild
  _security.py      - Pattern-based static security analysis (18 language rule sets)
  _cpg.py           - Code Property Graph (CPG) JSON-LD embed generator
  _uml.py           - UML class diagram generator (Mermaid classDiagram + 12-language code generation)
  _diagrams.py      - Interactive system maps: typed IR, validator, builder, standalone HTML renderer
  _video.py         - Cinematic synthwave overview video (general-purpose codebase explainer, PIL + ffmpeg)
  _githistory.py    - Read-only git release timeline (per-release source snapshots for the growth act)
  _readme_injector.py - Auto-injects KNOWLEDGE_BASE.md link into project README
  _agent_injector.py - Injects KB + agent output references into AI agent config files
  _agent_output.py   - Agent-friendly grep-optimized output generator (INDEX.md, API.md, etc.)
  _purpose.py        - Shared one-sentence file purpose extraction (banner/SPDX cleaning, symbol fallback)
  _gitmeta.py        - Read-only git HEAD/branch reader for freshness stamps (no subprocess)
  _gh_wiki.py        - Opt-in GitHub wiki publisher (flat pages, sidebar, permalinks, git push)
  _taint.py         - Taint propagation analysis through import graph
  _hotspots.py      - Hotspot detection, cycle analysis, change impact analysis
  _rule_gen.py      - Suggested linting/security rule generation (Semgrep YAML)
  _sarif.py         - SARIF v2.1.0 output generator for security findings
  _pipeline.py      - AnalyzerFactory (lazy init) + DeepAnalysisRunner (decoupled v2 analysis)
  _app.py           - Application orchestrator (thin facade over AnalyzerFactory)
  _mcp_server.py    - MCP stdio server exposing tools + resources for AI agent queries
  _concepts.py      - Semantic ConceptGraph: nouns as nodes, verbs as edges, atomic zero-token extraction
  _forcegraph.py    - CAIRN-style heterogeneous force-graph payload, page settings, thumbnail (hulls, log2 sizing)
  _forcegraph_page.py - 2D/3D explorer HTML template: page-side hit-testing, 3D overlay glyphs, node/edge/path/lens actions
  _bundlegraph.py   - Edge bundle explorer: circle + sphere bundle payload from the force-graph payload, settings, thumbnail
  _bundlegraph_page.py - Self-contained edge bundle page (canvas, 2D circle, 3D sphere camera, live beta, focus panels)
  _analytics.py     - Corpus analytics aggregations (funnel, distributions, hotspots, scatter)
  _scantext.py      - Synthesized scan-text blobs (names, symbols, imports, snippets) for rules/embeddings
  _yaralite.py      - Zero-dep tiered T1/T2/T3 YARA-lite parser + runner (no native dependency)
  _provenance.py    - Evidence-provenance audit (static vs inferred-only findings)
  _exclusions.py    - FP exclusion blocklist loader (glob + rule_id scoping)
  _explorer.py      - Stdlib HTTP explorer server (/api/graph, /api/analytics, /api/samples, /api/source)
  _embed.py         - Optional semantic embeddings with offline Jaccard fallback
  _graphrag.py      - Zero-token GraphRAG: entities, relationships, text units, report hierarchy, local/global search
  _graphlayout.py   - ForceAtlas2 snapshots in 2D/3D (numpy optional), circular and spherical hierarchical edge bundling
  _memory.py        - MEMORY.md: declared rules (file:line), measured baselines, preserved session log
  _skill_installer.py - Installs packaged agent skills (readmenator/_skills/*/SKILL.md)
  _sourceview.py      - Bounded per-file source texts for the explorer View drawer (caps, privacy)
  _symindex.py        - Deterministic symbol index: spans, call sites with lines, definition resolver
  _ollama.py          - Optional local Ollama client (stdlib, bounded, never fatal)
  _components.py      - Component diagrams: analysis.json, graph LR, per-component markdown, offline index.html
  _docstrings.py      - Multi-style docstring parser (Google, NumPy, reST, Javadoc/JSDoc/PHPDoc/Doxygen, C# XML, Rustdoc) + raw comment recovery
  _apidocs.py         - API reference model: Python ast extraction, generic symbol nesting, signatures, cross-refs, coverage, DOC00x warnings
  _apidocs_render.py  - API reference Markdown (index, modules, hierarchy, genindex, coverage), split api/ JSON Lines model, writer, linker
  _apidocs_page.py    - Self-contained offline HTML API browser (search, tree, hierarchy, coverage, architecture page)
  _folder_readme.py   - Per-folder README.md for every generated readmenator-* directory (purpose, present contents, usage, regenerate)
  _htmlpack.py        - Embedded page payloads: plain JSON when small (legacy per-page format), deterministic gzip+base64 decoded by native DecompressionStream when large; shared async loader
  _flowcharts.py      - Tiered architecture (Tarjan SCC, Eades-Lin-Smyth FAS, transitive reduction) + execution flows (entry points, call tree, control flow, sequence)
  _flowlayout.py      - FlowGraph model + deterministic layered layout (ranks, barycenter ordering, row wrapping, curve routing, lanes)
  _flowpage.py        - Offline interactive SVG viewer for flow graphs (flows.html, API Flows tab, gallery thumbnail)
  _pytypes.py         - Deterministic Python receiver typing (constructors, annotations, self attributes) for precise call graphs
  _project_config.py  - Per-project readmenator.toml: ensure-from-template, allow-listed load (CLI wins), viewer config.json
  _viewer_ui.py       - Shared Config button + modal for maps pages: live segment re-render, localStorage, Copy TOML
  _skills/          - Packaged Agent Skills: readmenator-orient, -ask, -change, -memory
  _vendor/          - Vendored frontend assets (force-graph 2D engine, MIT) copied beside exported pages
example.readmenator.toml - Human template copy of the embedded project config template
tests/
  test_config.py        - Config contract tests
  test_models.py        - Data model contract tests
  test_parsers.py       - 13 original parser contract tests
  test_parsers_new.py   - 6 new parser contract tests (Ruby, Swift, Kotlin, Scala, Lua, Elixir)
  test_scanner.py       - Scanner security, behavior, gitignore, privacy mode tests
  test_resolver.py      - Import resolver contract tests
  test_mermaid.py       - Mermaid rendering contract tests
  test_documentation.py - Documentation output contract tests (all sections)
  test_query.py         - Query engine contract tests
  test_analyzer.py      - Graph analysis contract tests
  test_linter.py        - Architecture linter contract tests
  test_dead_code.py     - Dead code stripper contract tests
  test_cursorrules.py   - Cursor rules generator contract tests
  test_refactorizer.py  - Monolith refactorizer contract tests
  test_cache.py         - File cache contract tests
  test_exporter.py      - Graph exporter contract tests
  test_security.py      - Security analyzer contract tests (41 languages, thresholds, paths)
  test_integration.py   - End-to-end pipeline tests
  test_cpg.py           - Code Property Graph contract tests
  test_taint.py         - Taint analysis contract tests
  test_hotspots.py      - Hotspot, cycle, change impact contract tests
  test_rule_gen.py      - Rule generation contract tests
  test_sarif.py         - SARIF export contract tests
  test_layer_rules.py   - Layer violation detection contract tests
  test_mcp_server.py    - MCP server protocol, tools, and resources contract tests
  test_uml.py           - UML class diagram and code generation contract tests
  test_diagrams.py      - Interactive system maps contract tests (IR, validation, rendering)
  test_video.py         - Cinematic video contract tests (collect, scenes, frames, skip)
  test_githistory.py    - Git release timeline contract tests (order, snapshots, budgets, isolation)
  test_readme_injector.py - README injection contract tests
  test_agent_output.py - Agent output generator contract tests (subsystems, grep-friendly, injection)
  test_wiki.py - Agent wiki contract tests (index, community pages, connections, orphans, lint, privacy)
  test_dataflow.py - Dataflow analyzer contract tests (def-use, alloc checks, C idioms, span bounds)
  test_agent_friendliness.py - Agent output budgets, purposes, MANIFEST freshness, noise reduction, llms.txt
  test_gh_wiki.py - GitHub wiki publisher contract tests (faked git/gh runner, no network)
  test_concepts.py - Semantic ConceptGraph contract tests (nouns, verbs, atomic, deterministic, dialectic)
  test_interactive_graph.py - Interactive explorer contract tests (forcegraph, explorer hit-testing/3D overlay/actions, scantext, yaralite, provenance, exclusions, analytics, explorer, embed, rebuild wiring)
  test_graphrag.py - GraphRAG contract tests (entities, relations, reports, text units, privacy, BM25, PPR local, global, store)
  test_graphlayout.py - ForceAtlas2 (2D/3D) and circular/spherical edge bundling contract tests (determinism, separation, bounds, caps, curves)
  test_bundlegraph.py - Edge bundle explorer contract tests (payload, escaping, no network, gallery card, disable flag)
  test_memory.py - Project memory and skill installer contract tests (rules, citations, preserved log, marker safety)
  test_sourceview.py - Source viewer contract tests (caps, privacy, View drawer, highlight, ctrl+click, themes)
  test_symindex.py - Symbol index contract tests (spans, call-site lines, confidence tiers, methods_index)
  test_components.py - Component diagram contract tests (schema, graph LR, markdown, page, gallery card)
  test_ollama.py - Local Ollama client contract tests (disabled, unreachable, thinking strip)
  test_apidocs.py - Docstring parser (all styles, comment recovery) + API reference contract tests (signatures, nesting, inheritance, calls, warnings, coverage, privacy, rendering, HTML escaping, writer)
  test_flowcharts.py - Architecture tiers, SCC/transitive reduction/ELS, entry points, call walks, control flow, sequence, KB integration, receiver typing
  test_folder_readme.py - Folder README contract (existing folders only, present entries only, idempotent, hand-written kept, symlinks refused, consumers skip, app wiring)
  test_htmlpack.py - Payload compression contract (threshold, determinism, legacy plain format, browser loader in node, every page decodes identical payloads plain vs compressed, inline scripts valid JS)
  test_layout_quality.py - Bundle crossing reduction (cost, determinism, monotone sweeps, sphere refinement) and seeded explorer layouts
```

## Contracts

### Config Contract
- Immutable FrozenInstanceError on mutation
- No magic numbers or hardcoded paths
- All tuneable parameters in one place
- Pluralization map for symbol types
- Graph analysis thresholds (COMMUNITY_MIN_SIZE, GOD_NODE_TOP_N, COMMUNITY_HUB_DAMPING, COMMUNITY_VOTE_EPSILON, COMMUNITY_MERGE_BELOW, etc.)
- Export settings (SVG_DPI, SVG_MAX_NODES, HTML_TEMPLATE_STYLE)
- Cache directory config (CACHE_DIR)
- Docstrings stored in full, no truncation
- Security audit settings (SECURITY_ENABLED, SECURITY_SEVERITY_THRESHOLD, SECURITY_OUTPUT)
- Progress reporting batch size (PROGRESS_REPORT_BATCH)
- CPG settings (CPG_ENABLED, CPG_EMBED_IN_KNOWLEDGE_BASE)
- Taint analysis settings (TAINT_ENABLED, TAINT_MAX_DEPTH, TAINT_MAX_PATHS)
- SARIF export settings (SARIF_ENABLED, SARIF_OUTPUT)
- Hotspot settings (HOTSPOTS_ENABLED, HOTSPOT_COMPLEXITY_WEIGHT, HOTSPOT_CENTRALITY_WEIGHT)
- Cycle detection settings (CYCLE_DETECTION_ENABLED)
- Change impact settings (CHANGE_IMPACT_MAX_DEPTH, CHANGE_IMPACT_MAX_FILES)
- Rule generation settings (RULE_GEN_ENABLED, RULE_GEN_MIN_PATTERN_COUNT, RULE_GEN_OUTPUT_DIR)
- Layer violation settings (LAYER_VIOLATION_ENABLED, LAYER_VIOLATION_STRICT_MODE)
- Privacy and gitignore settings (PRIVACY_MODE, GITIGNORE_AWARE)
- Per-project config file (PROJECT_CONFIG_FILENAME, PROJECT_CONFIG_ENABLED, PROJECT_NAME) and viewer config (VIEWER_CONFIG_FILENAME)
- Project branding (PROJECT_AUTHOR/DESCRIPTION/GITHUB_URL/PAGES_URL/HOME_URL/LOGO_URL/ACCENT/ACCENT2), injection message overrides (MSG_*), and maps budgets (SOURCEVIEW_* via [maps])
- Context budget for token-optimized KB (CONTEXT_BUDGET)
- Linter settings (LINTER_ENABLED, LINTER_MAX_LINES, LINTER_CROSS_LAYER_VIOLATIONS)
- Dead code settings (DEAD_CODE_ENABLED, DEAD_CODE_ENTRY_POINTS, DEAD_CODE_QUARANTINE_DIR)
- Cursor rules settings (CURSORRULES_ENABLED, CURSORRULES_OUTPUT)
- Refactorizer settings (REFACTORIZER_ENABLED, REFACTORIZER_MIN_LINES, REFACTORIZER_MAX_FILES)
- Agent output settings (AGENT_OUTPUT_ENABLED, AGENT_OUTPUT_DIR, AGENT_OUTPUT_MIN_SUBSYSTEM_FILES)
- Wiki settings (WIKI_ENABLED, WIKI_OUTPUT_DIR, WIKI_MAX_FILES_PER_PAGE, WIKI_MAX_SYMBOLS_PER_PAGE, WIKI_MAX_CONNECTIONS)
- Large-file threshold via WIKI_LARGE_FILE_KB (default 256)
- Dataflow settings (DATAFLOW_ENABLED, DATAFLOW_MAX_ISSUES, default 50)
- Interactive map settings (DIAGRAM_ENABLED, DIAGRAM_MAX_NODES, DIAGRAM_MAX_EDGES, DIAGRAM_OUTPUT_DIR)
- Map geometry settings (DIAGRAM_NODE_WIDTH, DIAGRAM_NODE_HEIGHT, DIAGRAM_COLUMN_GAP, DIAGRAM_ROW_GAP, DIAGRAM_CANVAS_WIDTH, DIAGRAM_CANVAS_HEIGHT, DIAGRAM_MARGIN_X, DIAGRAM_MARGIN_Y, DIAGRAM_MIN_GAP, DIAGRAM_LANE_TOP, DIAGRAM_SEQUENCE_TOP)
- Map scope settings (DIAGRAM_SEQUENCE_MAX_PARTICIPANTS, DIAGRAM_WORKFLOW_FALLBACK_NODES, DIAGRAM_CHAPTER_FOCUS, DIAGRAM_MAX_VIEWS, DIAGRAM_MAX_LABEL_CHARS)
- Map style vocabulary (DIAGRAM_PRESETS, DIAGRAM_KINDS, DIAGRAM_ROLES, DIAGRAM_ROLE_COLORS, DIAGRAM_PRESET, DIAGRAM_THEME, DIAGRAM_MOTION_ENABLED, DIAGRAM_SHARE_WIDTH, DIAGRAM_SHARE_HEIGHT)
- Map documentation payload (DIAGRAM_MAP_SYMBOLS_PER_NODE, DIAGRAM_TOOLTIP_DOC_CHARS, DIAGRAM_NEIGHBOR_NAMES)
- Live CDN renderer settings (DIAGRAM_VIS_ENABLED, DIAGRAM_VIS_CDN_JS, DIAGRAM_VIS_CDN_CSS, DIAGRAM_VIS_PHYSICS_ENABLED, DIAGRAM_VIS_STABILIZE_ITERATIONS)
- Pages publishing settings (DIAGRAM_PAGES_DIR, DIAGRAM_MAPS_SUBDIR)
- Site media settings (SITE_VIDEO_ENABLED, SITE_VIDEO_FILENAME, SITE_DOCS_ENABLED, SITE_DOCS_SUBDIR, SITE_MAX_DOCS, SITE_MD_PREVIEW_CHARS)
- Cinematic video settings (VIDEO_ENABLED, VIDEO_OUTPUT, VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS, VIDEO_CRF, VIDEO_JOBS)
- Video act durations (VIDEO_TITLE_S, VIDEO_CARD_S, VIDEO_LAYER_S, VIDEO_GOD_S, VIDEO_TREE_S, VIDEO_COMM_S, VIDEO_GRAPH_S, VIDEO_DNA_S, VIDEO_OUTRO_S)
- Growth act settings (VIDEO_GROWTH_S, VIDEO_GROWTH_BIRTH_S, VIDEO_GROWTH_PULSES, VIDEO_GROWTH_GHOST)
- Git history settings (VIDEO_HISTORY_ENABLED, VIDEO_HISTORY_MAX_SNAPSHOTS, VIDEO_HISTORY_MAX_FILES, VIDEO_HISTORY_TIMEOUT_S)
- Video scope settings (VIDEO_MAX_GRAPH_NODES 0 = all, VIDEO_TREE_MAX_NODES 0 = all, VIDEO_TREE_RING_MARGIN, VIDEO_TREE_LABEL_GAP, VIDEO_TREE_CHAR_PX, VIDEO_GRAPH_TRIM_FRACTION, VIDEO_GRAPH_SPREAD, VIDEO_GRAPH_LOOSE_STRIP, VIDEO_DNA_MAX_CELL, VIDEO_MAX_LABEL_CHARS, VIDEO_MUSIC_PATH, VIDEO_PREVIEW_LINES)
- Agent budget settings (AGENT_OUTPUT_MAX_LINES, AGENT_PURPOSE_MAX_CHARS, AGENT_DOC_MAX_CHARS, AGENT_SIGNATURE_MAX_CHARS, AGENT_GOTCHAS_TOP_N, AGENT_GOTCHAS_EXCLUDE_LAYERS, AGENT_API_PUBLIC_ONLY, AGENT_API_EXCLUDE_LAYERS, AGENT_CHARS_PER_TOKEN, AGENT_ENTRYPOINT_FILENAMES)
- Generated artifact settings (GENERATED_FILE_PREFIXES, SKIP_GENERATED_OUTPUTS, REFACTORIZER_SCRIPT_PREFIX)
- Site agent settings (SITE_LLMS_TXT_ENABLED, SITE_LLMS_TXT_FILENAME, SITE_REFRESH_ON_REBUILD)
- Site project links (SITE_GITHUB_URL, SITE_PYPI_URL)
- GitHub wiki settings (GH_WIKI_ENABLED default True, GH_WIKI_REMOTE, GH_WIKI_GIT_REMOTE_NAME, GH_WIKI_HOME_PAGE, GH_WIKI_KB_PAGE, GH_WIKI_AGENT_PREFIX, GH_WIKI_RECIPE_PREFIX, GH_WIKI_INCLUDE_KB, GH_WIKI_PERMALINKS, GH_WIKI_STATE_FILE, GH_WIKI_DRY_RUN_DIR, GH_WIKI_TIMEOUT_S, GH_WIKI_COMMIT_MESSAGE)
- Force-graph settings (FORCEGRAPH_ENABLED, FORCEGRAPH_MODE, FORCEGRAPH_OUTPUT, FORCEGRAPH_CDN_JS_2D/3D, FORCEGRAPH_BG, FORCEGRAPH_CHARGE, FORCEGRAPH_LINK_DISTANCE/STRENGTH, FORCEGRAPH_NODE_REL_SIZE, FORCEGRAPH_HULLS_ENABLED/FILL/STROKE/PAD, FORCEGRAPH_PARTICLES_ON_HIGHLIGHT, FORCEGRAPH_DIM_NODE/LINK, FORCEGRAPH_NODE_COLORS, FORCEGRAPH_EDGE_COLORS, FORCEGRAPH_FAMILY_SAT/LIGHT_BASE/SPAN)
- Analytics settings (ANALYTICS_ENABLED)
- Scan-text settings (SCANTEXT_ENABLED, SCANTEXT_MAX_SYMBOLS/IMPORTS, SCANTEXT_SNIPPET_CHARS)
- YARA-lite settings (YARALITE_ENABLED, YARALITE_RULES_FILE, YARALITE_MAX_HITS_PER_ID)
- Provenance settings (PROVENANCE_ENABLED)
- Exclusion settings (EXCLUSIONS_ENABLED, EXCLUSIONS_FILE)
- Explorer settings (EXPLORER_ENABLED, EXPLORER_HOST, EXPLORER_PORT)
- Embedding settings (EMBED_ENABLED, EMBED_MODEL, EMBED_MIN_CLUSTER_SIZE, EMBED_MAX_NEIGHBORS)
- GraphRAG settings (GRAPHRAG_ENABLED, GRAPHRAG_OUTPUT_DIR, GRAPHRAG_INCLUDE_SYMBOLS/CONCEPTS/EXTERNALS, GRAPHRAG_TEXT_UNIT_MAX_LINES/CHARS, GRAPHRAG_BM25_K1/B, GRAPHRAG_PPR_ALPHA/MAX_ITER/TOLERANCE, GRAPHRAG_SEED_TOP_K, GRAPHRAG_LOCAL_TOP_*, GRAPHRAG_GLOBAL_TOP_REPORTS, GRAPHRAG_REPORT_*, GRAPHRAG_CONTEXT_BUDGET_TOKENS, GRAPHRAG_LOCAL_SECTION_SHARES, GRAPHRAG_GLOBAL_SECTION_SHARES, GRAPHRAG_RATING_*, GRAPHRAG_SEVERITY_WEIGHTS, GRAPHRAG_GLOBAL_HINTS, GRAPHRAG_STOPWORDS)
- Explorer interaction (FORCEGRAPH_LAYER_COLORS, FORCEGRAPH_HIT_PADDING_PX, FORCEGRAPH_MIN_HIT_PX, FORCEGRAPH_EDGE_HIT_PX, FORCEGRAPH_DRAG_THRESHOLD_PX, FORCEGRAPH_CURVE_STEP/SAMPLES, FORCEGRAPH_ARROW_LENGTH/ZOOM, FORCEGRAPH_COOLDOWN_TICKS(_REDUCED), FORCEGRAPH_COLLIDE_MAX_NODES, FORCEGRAPH_LABEL_HIGHLIGHT_MAX, FORCEGRAPH_DOC_LINES_PX, FORCEGRAPH_TIP_DOC_CHARS, FORCEGRAPH_HUB_TOP_N, FORCEGRAPH_FIT_PADDING_PX/MAX_ZOOM/LEGEND_MIN_WIDTH)
- Explorer 3D view (FORCEGRAPH_CDN_JS_3D pinned to an exact release, FORCEGRAPH_3D_LINK_OPACITY, FORCEGRAPH_3D_LINK_WIDTH_HIGHLIGHT/ACTIVE, FORCEGRAPH_3D_PARTICLE_WIDTH, FORCEGRAPH_3D_DEPTH_FADE, FORCEGRAPH_3D_MIN_GLYPH_PX, FORCEGRAPH_3D_LABEL_PX, FORCEGRAPH_3D_ORBIT_SPEED, FORCEGRAPH_3D_FLY_DISTANCE)
- Force-graph explorer UX (FORCEGRAPH_LABEL_TOP_N, FORCEGRAPH_LABEL_ZOOM, FORCEGRAPH_LABEL_MAX_CHARS, FORCEGRAPH_SYMBOLS_PER_NODE, FORCEGRAPH_DOC_MAX_CHARS, FORCEGRAPH_SIGNATURE_MAX_CHARS, FORCEGRAPH_CLUSTER_STRENGTH, FORCEGRAPH_COLLIDE_PADDING, FORCEGRAPH_DAG_LEVEL_DISTANCE, FORCEGRAPH_FLY_MS, FORCEGRAPH_FLY_ZOOM, FORCEGRAPH_SEARCH_RESULTS, FORCEGRAPH_THUMB_WIDTH/HEIGHT/ITERATIONS)
- Video layout acts (VIDEO_BUNDLE_S, VIDEO_FA2_ITERATIONS, VIDEO_FA2_SNAPSHOTS, VIDEO_FA2_SCALING, VIDEO_FA2_GRAVITY, VIDEO_FA2_LINLOG, VIDEO_BUNDLE_BETA, VIDEO_BUNDLE_SAMPLES, VIDEO_SURFERS, VIDEO_RANK_LABELS)
- Video 3D acts (VIDEO_ORBIT_S, VIDEO_SPHERE_S, VIDEO_INVITE_S, VIDEO_ORBIT_FA2_ITERATIONS, VIDEO_ORBIT_TOUR_STOPS, VIDEO_ORBIT_TURNS, VIDEO_ORBIT_PITCH_DEG, VIDEO_ORBIT_PERSPECTIVE, VIDEO_ORBIT_ZOOM, VIDEO_ORBIT_DEPTH_FADE, VIDEO_ORBIT_LABELS, VIDEO_SPHERE_TURNS, VIDEO_SPHERE_SAMPLES)
- Edge bundle explorer (BUNDLEGRAPH_ENABLED, BUNDLEGRAPH_OUTPUT, BUNDLEGRAPH_MODE, BUNDLEGRAPH_BETA, BUNDLEGRAPH_SAMPLES, BUNDLEGRAPH_INNER_RATIO, BUNDLEGRAPH_GROUP_GAP, BUNDLEGRAPH_EDGE_ALPHA, BUNDLEGRAPH_DIM_ALPHA, BUNDLEGRAPH_LABEL_ALL_MAX, BUNDLEGRAPH_LABEL_TOP_N, BUNDLEGRAPH_LABEL_MAX_CHARS, BUNDLEGRAPH_NODE_MIN_PX/MAX_PX, BUNDLEGRAPH_HIT_PX, BUNDLEGRAPH_ROTATE_SPEED, BUNDLEGRAPH_PERSPECTIVE, BUNDLEGRAPH_DEPTH_FADE, BUNDLEGRAPH_PARTICLES, BUNDLEGRAPH_REVEAL_MS, BUNDLEGRAPH_FLOW_TOP_N, BUNDLEGRAPH_LIST_MAX, BUNDLEGRAPH_THUMB_EDGES, BUNDLEGRAPH_THUMB_SAMPLES)
- Memory settings (MEMORY_ENABLED, MEMORY_FILENAME, MEMORY_VOCABULARY_STOPWORDS, MEMORY_NOTE_MAX_CHARS, MEMORY_NOTE_KINDS, MEMORY_RULE_SOURCES, MEMORY_CONSTRAINT/STYLE/DELIVERABLE_KEYWORDS, MEMORY_HEADING_EXCLUDE, MEMORY_MAX_RULES_PER_FILE/CATEGORY, MEMORY_MIN_RULE_CHARS, MEMORY_MAX_COMMANDS, MEMORY_VOCABULARY_TOP_N, MEMORY_SUBSYSTEMS_TOP_N, MEMORY_STYLE_LANGUAGES, MEMORY_RISKS_TOP_N)
- Skills settings (SKILLS_ENABLED, SKILLS_TARGET_DIR, SKILLS_INSTALL_ON_RUN)
- Symbol index settings (SYMINDEX_MAX_CALL_SITES, SYMINDEX_BUILTINS)
- Component diagram settings (COMPONENTS_ENABLED, COMPONENTS_OUTPUT_DIR, COMPONENTS_MAX_KEY_ENTITIES/KEY_EDGES/ALL_EDGES, COMPONENTS_EXPAND_MIN_FILES, COMPONENTS_DEPTH_CAP)
- Ollama settings (OLLAMA_ENABLED default False, OLLAMA_HOST, OLLAMA_MODEL, OLLAMA_TIMEOUT_S, OLLAMA_MAX_PROMPT_CHARS, OLLAMA_MAX_CHARS)
- Source viewer settings (SOURCEVIEW_ENABLED, SOURCEVIEW_MAX_FILES/CHARS_PER_FILE/LINES_PER_FILE/TOTAL_CHARS, SOURCEVIEW_CHUNK_LINES, SOURCEVIEW_CONTEXT_LINES)
- API reference settings (APIDOCS_ENABLED, APIDOCS_OUTPUT_DIR, APIDOCS_MODULES_SUBDIR, APIDOCS_INCLUDE_PRIVATE, APIDOCS_INCLUDE_TESTS, APIDOCS_TEST_PATH_TOKENS, APIDOCS_SKIP_SUFFIXES, APIDOCS_EXCLUDE_DIRS, APIDOCS_MAX_ENTITIES, APIDOCS_DOC_LOOKBACK_LINES, APIDOCS_BRACE_SCAN_LINES, APIDOCS_MAX_CALL_REFS, APIDOCS_CALLGRAPH_MAX_EDGES, APIDOCS_SUMMARY_MAX_CHARS, APIDOCS_HTML_ENABLED, APIDOCS_HTML_FILENAME, APIDOCS_JSON_FILENAME, APIDOCS_JSON_MONOLITH (default False), APIDOCS_JSONL_DIR, APIDOCS_JSONL_MODULES_SUBDIR, APIDOCS_JSONL_INDEX, APIDOCS_JSONL_WARNINGS, APIDOCS_ARCHITECTURE_FILENAME, APIDOCS_SCHEMA_VERSION, APIDOCS_MERMAID_CDN_JS, APIDOCS_COVERAGE_FAIL_UNDER, APIDOCS_MAX_WARNINGS_LISTED)
- Architecture and flow diagram settings (ARCH_DIAGRAM_ENABLED, ARCH_DIAGRAM_INCLUDE_TESTS, ARCH_DIAGRAM_MAX_COMPONENTS, ARCH_DIAGRAM_LABEL_CHARS, FLOW_ENABLED, FLOW_MAX_ENTRYPOINTS, FLOW_MIN_ENTRY_SCORE, FLOW_SOURCE_MIN_CALLS, FLOW_MAX_DEPTH, FLOW_MAX_STEPS, FLOW_LABEL_CHARS, FLOW_SEQUENCE_MAX_MESSAGES, FLOW_CFG_MAX_NODES, FLOW_SWITCH_MIN_CASES)
- Symbol index receiver window (SYMINDEX_RECEIVER_WINDOW: bounded look-behind for attribute-call receivers, keeps minified lines linear)
- Bundle ordering (BUNDLEGRAPH_ORDER_OPTIMIZE, BUNDLEGRAPH_ORDER_SWEEPS, BUNDLEGRAPH_ORDER_PASSES, BUNDLEGRAPH_SPHERE_REFINE_SWEEPS)
- Explorer seeded layout (FORCEGRAPH_SEED_LAYOUT, FORCEGRAPH_SEED_ITERATIONS, FORCEGRAPH_SEED_GRAVITY, FORCEGRAPH_SEED_MAX_NODES, FORCEGRAPH_SEED_VELOCITY_DECAY)
- Flow layout settings (FLOW_NODE_MAX_CHARS, FLOW_NODE_MAX_LINES, FLOW_MAX_PER_ROW, ARCH_DIAGRAM_MAX_PER_ROW, ARCH_DIAGRAM_PANEL_FILES, FLOWS_OUTPUT)
- Legacy Mermaid shape (MERMAID_GRID_COLUMNS, MERMAID_MAX_EXTERNALS, MERMAID_DIRECTION, UML_CLASSES_PER_DIAGRAM)
- Video flow acts (VIDEO_TIERS_S, VIDEO_FLOW_S, VIDEO_FLOW_VIEW_WIDTH)
- Video transitions (VIDEO_TRANSITION_S crossfade, VIDEO_TRANSITION_GLITCH, VIDEO_MOTION_BLUR_SAMPLES, VIDEO_MOTION_BLUR_SHUTTER, VIDEO_MOTION_BLUR_ACTS)
- Folder READMEs (FOLDER_README_ENABLED, FOLDER_README_FILENAME, FOLDER_README_MARKER)
- Embedded payload compression (PAYLOAD_COMPRESSION_ENABLED, PAYLOAD_COMPRESSION_MIN_BYTES default 256 KiB, PAYLOAD_COMPRESSION_LEVEL)

### Models Contract
- Symbol: name, kind (not `type`), line, doc, signature
- Node: node_id, label, kind, language, doc, symbols
- Edge: source, target, relation, confidence
- pluralize_symbol_kind: returns correct plural form
- CommunityResult: community_id, label, file_ids, cohesion, size
- AnalysisResult: god_nodes, communities, surprising_connections, suggested_questions
- SecurityFinding: file_path, line, severity, rule_id, description, snippet, cwe
- TaintPath: source_file, sink_file, path, hops, dangerous_import, severity
- TaintAnalysisResult: paths, source_count, sink_count
- DependencyCycle: cycle, length
- ChangeImpact: file_id, direct_dependents, transitive_dependents, total_impact
- HotspotResult: file_id, complexity_score, centrality_score, combined_score, symbol_count, connection_count
- SuggestedRule: rule_id, severity, description, pattern, file_examples, match_count, language, semgrep_yaml
- LayerViolation: source_file, source_layer, target_file, target_layer, description, severity
- AnalysisResultV2: taint, cycles, change_impacts, hotspots, suggested_rules, layer_violations
- LinterViolation: file_path, rule_id, severity, message
- DeadCodeReport: file_path, symbol_name, symbol_type, recommendation
- RefactoringAction: action_type, source_file, start_line, end_line, target_file, description
- RefactoringPlan: file_path, actions, estimated_impact, current_lines

### Parsers Contract
- LanguageParser base with _extract_docstring and _extract_signature
- 19 parser subclasses, one per language, in `parsers/` package
- Python uses native ast module; all others use regex
- ParserFactory (create_parser) maps extension to parser class (case-insensitive)
- All parsers populate: self.symbols (List[Symbol]), self.imports (List[str])
- C-family and assembly parsers extract #include directives (quoted and angled) as imports
- Reserved keywords filtered out (if, for, while, switch, catch)
- C parser: function/prototype line numbers anchored at the symbol name (multiline signatures safe); call statements rejected as prototypes via return-type prefix check; extern/define patterns never span newlines
- Java, C#, and JS/TS symbol lines are anchored at the name group (leading whitespace never shifts them); Java abstract methods ending in ; are extracted; JS/TS class methods are extracted as methods; Python methods are functions defined directly in a class body

### Scanner Contract
- Rejects symlinks for security
- Skips files > MAX_FILE_SIZE_MB
- Enforces MAX_DIRECTORY_DEPTH
- Ignores paths containing IGNORE_DIRS entries
- Only processes files with supported extensions
- Catches all exceptions silently during parsing
- Returns (List[Node], List[Edge])
- Extracts file-level docstrings from header comments (including Python `"""`/`'''` module docstrings)
- Skips encoding-cookie lines (`coding: utf-8`) when extracting file docs
- Skips preprocessor directives (`#ifndef`, `#define`, `#include`, ...) when extracting file docs
- Emits progress messages every PROGRESS_REPORT_BATCH files
- Supports `.gitignore`-aware scanning (GITIGNORE_AWARE)
- Supports privacy mode (PRIVACY_MODE) that strips snippets and docstrings
- Skips its own generated outputs (agent, wiki, rules, maps, site, cache, graphrag, component diagrams, gh-wiki dry run dirs and `.refactor_*` scripts) via SKIP_GENERATED_OUTPUTS; counted as `generated` in last_skip_counts
- scan_with_content() returns content map for rule gen, taint analysis
- is_generated(rel_path) is public (the git history replay filters historical trees with it)
- scan_contents(contents) parses an in-memory file map with the same parsers and the same _parse_source path, used to replay historical trees

### Import Resolver Contract
- Maps raw import strings (Python dots, relative paths, bare module names) to project file paths
- Handles Python stdlib exclusion
- Handles relative imports (./ and ../)
- Handles quoted C-family includes verbatim against the source directory ("utils.h", "lib/net.h")
- Normalizes parent directory segments ("src/../include/types.h" -> "include/types.h")
- Handles include-directory suffix matching ("kernel/mm.h" -> "include/kernel/mm.h", unique matches only)
- Handles extensionless imports with the full Config extension list (C headers, C++ sources, and all 19 languages)
- Handles dotted module paths (foo.bar.baz -> foo/bar/baz.py)
- Handles package __init__.py resolution
- Bare top-level names prefer a root package (`pkg/__init__.py`) over a same-stem launcher shim (`pkg.py`), mirroring Python import precedence
- Handles stem matching as fallback with known-extension stripping ("utils.h" -> "utils")
- Works across all supported languages

### Mermaid Renderer Contract
- Renders internal import edges between project files (solid arrows)
- Renders community subgraphs when analysis results provided
- Maintains existing external import dashed edges
- Limits symbols per file to MERMAID_MAX_SYMBOLS_PER_FILE
- Returns (mermaid_source, is_truncated) tuple

### Documentation Generator Contract
- Header: title + metadata line
- Header links the agent wiki (`readmenator-wiki/index.md`) and states the EXTRACTED/INFERRED/AMBIGUOUS confidence legend
- Table of Contents with section links for all new sections
- Statistics Dashboard (file counts, import fan-in/fan-out, language breakdown)
- Architectural Layers section (auto-detected 5-layer model)
- God Nodes section (most central files ranked by connectivity)
- Community Analysis section (import-based groups with cohesion scores)
- Surprising Connections section (cross-community indirect bridges)
- Suggested Questions section (auto-generated exploration prompts)
- Taint Propagation Map section (dangerous import propagation paths)
- Hotspot Analysis section (files ranked by complexity + centrality)
- Dependency Cycles section (circular dependencies)
- Change Impact Analysis section (files sorted by transitive impact)
- Architecture Violations section (layer rule violations)
- Suggested Linting Rules section (auto-generated Semgrep rules)
- Security Audit section (findings by severity, no emojis)
- Mermaid graph in fenced code block with community subgraphs (graph LR, grid-wrapped communities, capped externals)
- Code Property Graph (CPG) block in JSON-LD format
- Architecture Reference grouped by language
- Each file lists its symbols by kind with correct pluralization
- File-level docstring displayed per file
- Cross-reference: "Imported by" links for each file
- "Classes" not "Classs" (regression guard)
- Truncation note when MERMAID_MAX_NODES exceeded
- Context budget mode: when CONTEXT_BUDGET > 0, generates compact summary first, prioritizes sections by architectural importance, truncates at specified token budget

### Query Engine Contract
- find_symbol(name): exact + fuzzy match
- explain(name): type, file, line, doc, signature, file_doc, imports, imported_by, siblings
- find_path(A, B): BFS bidirectional shortest path through resolved import graph
- query(text): search symbols and files for matching terms
- summary(): files, symbols, imports, top modules, key classes/functions
- Supports resolved_edges for project-internal path tracing

### Graph Analyzer Contract
- analyze(nodes, edges, resolved_edges): returns AnalysisResult
- Community detection via deterministic Louvain modularity optimisation by default (COMMUNITY_ALGORITHM="louvain", COMMUNITY_RESOLUTION, COMMUNITY_MAX_LEVELS, COMMUNITY_MAX_SWEEPS; sorted visit order, strict-gain moves, smallest-key ties); "label_propagation" kept as alternative
- Communities numbered largest first; labels come from production (non-test) files
- Deterministic: content-seeded shuffle order, sorted neighbor traversal, min-label tie-break (stable across runs and hash seeds)
- Small-group folding: communities under COMMUNITY_MERGE_BELOW join the neighbor sharing the most vote weight (smallest first, lowest label on ties); isolated groups untouched
- Labels shared by several communities get the core file stem (most symbols, non-test preferred): `pkg: _video`
- Hub damping (COMMUNITY_HUB_DAMPING): neighbors vote with weight 1/log2(2 + degree), so shared hubs (models, config) do not collapse the project into one community; ties within COMMUNITY_VOTE_EPSILON
- God node scoring via combined in/out degree + symbol weight
- Surprising connection discovery via cross-community path analysis
- Suggested question generation from graph structure
- Community cohesion scoring (internal / total edges)
- Community labeling from dominant directory (dominant_directory(): count wins, ties prefer longest/most-specific dir, then alphabetical; deterministic)
- AnalysisResultV2 carries dataflow_issues alongside taint/cycles/hotspots/rules/violations

### Code Property Graph Contract
- generate(nodes, edges, resolved_edges, analysis): returns JSON-LD string
- JSON-LD schema with @context, nodes (id, label, kind, language, sha256, symbols), edges (source, target, relation)
- Embeddable in KNOWLEDGE_BASE.md for zero-token AI agent consumption
- Respects PRIVACY_MODE (strips doc contents)
- Includes SHA256 content hashes per node
- Optional analysis metadata (god nodes, communities, surprising connections)

### Taint Analyzer Contract
- analyze(nodes, edges, resolved_edges): returns TaintAnalysisResult
- Scans for known-dangerous imports per language (subprocess, eval, exec, etc.)
- Propagates taint through resolved import graph (BFS)
- Generates self-paths for direct dangerous imports (hops=0)
- Configurable max propagation depth (TAINT_MAX_DEPTH)
- Configurable max path count (TAINT_MAX_PATHS)
- Per-language dangerous import maps

### Hotspot Analyzer Contract
- analyze_hotspots(nodes, edges, resolved_edges): returns List[HotspotResult]
- Combined complexity (symbol count) + centrality (connection count) scoring
- Configurable weights (HOTSPOT_COMPLEXITY_WEIGHT, HOTSPOT_CENTRALITY_WEIGHT)
- detect_cycles(nodes, resolved_edges): DFS cycle detection, returns List[DependencyCycle]
- analyze_change_impact(nodes, resolved_edges): BFS transitive dependent analysis
- Configurable max depth and file count for change impact

### Rule Generation Contract
- generate(nodes, content_map): returns List[SuggestedRule]
- Detects antipatterns: bare except, print statements, TODO/FIXME, hardcoded credentials
- Language-aware analysis (per-language naming patterns)
- Generates Semgrep YAML rules
- write_rules(rules, output_dir): writes Semgrep YAML to filesystem
- Configurable minimum pattern count (RULE_GEN_MIN_PATTERN_COUNT)
- Output directory configurable (RULE_GEN_OUTPUT_DIR)

### SARIF Exporter Contract
- export(findings, project_name): returns SARIF v2.1.0 JSON string
- OASIS SARIF standard format
- Compatible with GitHub Code Scanning and VS Code SARIF viewer
- Severity mapping: critical/high -> error, medium -> warning, low/info -> note
- Respects PRIVACY_MODE (strips code snippets from regions)
- Includes CWE identifiers in rule metadata

### Layer Rule Engine Contract
- detect_violations(nodes, edges, resolved_edges, layers): returns List[LayerViolation]
- Forbidden layer edges: testing -> presentation, presentation -> data_access
- Allowed edges: testing -> business_logic, testing -> infrastructure, testing -> data_access
- Warning edges: data_access -> presentation, infrastructure -> presentation
- Utility layer is ignored (no violations from/to utility)
- violation_summary(violations): counts by severity
- Strict mode enforces warning edges as violations (LAYER_VIOLATION_STRICT_MODE)

### AnalyzerFactory Contract (pipeline)
- Lazy property-based initialization of all analyzer components
- Each component is created on first access and cached
- Provides: scanner, generator, analyzer, security, exporter, taint, hotspots, layer_rules, rule_gen, sarif, cpg, layer_detector, uml, wiki, readme_injector, video, gh_wiki, folder_readme
- Decouples the application orchestrator from concrete instantiation

### DeepAnalysisRunner Contract (pipeline)
- run(nodes, edges, resolved_edges, layers, content_map): returns AnalysisResultV2
- Runs all v2 analyses as a coordinated batch
- Respects individual config enable flags (TAINT_ENABLED, HOTSPOTS_ENABLED, etc.)
- Isolated from the main app to reduce coupling in _app.py

### Security Analyzer Contract
- Pattern-based static analysis (regex, zero deps)
- Per-language rule sets: Python, JS/TS, C/C++, Java, Go, Ruby, PHP, Shell, C#, Kotlin, Swift, Scala, Lua, Dart, Rust, Nim, GDScript, Elixir
- Detects: command injection, SQL injection, XSS, eval/exec, unsafe deserialization, hardcoded secrets, weak crypto, path traversal, buffer overflow functions
- Severity levels: critical, high, medium, low, info
- Configurable severity threshold (SECURITY_SEVERITY_THRESHOLD)
- Findings sorted by severity then file path
- fix_hint_for(finding): one-line CWE-keyed remediation hint with least-privilege fallback
- Reuses scanner security checks (symlinks, ignore dirs, size/depth limits)
- No external API calls -- fully offline

### Layer Detection Contract
- detect(nodes, edges): maps each file to an architectural layer
- No Config dependency (static patterns only)
- 5-layer model: presentation, business_logic, data_access, infrastructure, testing
- Detection via path patterns, naming conventions, and imported frameworks
- Path patterns match whole words (camelCase and separators split; short patterns like `ui`/`di`/`api` must equal a token), never raw substrings
- Framework imports match the import root module from `imports` edges only; testing frameworks count only when the path already indicates tests (a CLI importing unittest stays production code)
- layer_summary: static method, counts files per layer

### Cache Contract
- SHA256 content hash cache for incremental scanning
- FileCache class with load/save/compute_hash/find_changed/prune_deleted methods
- Cache stored in CACHE_DIR/file_hashes.json within project
- Empty cache on first run returns empty dict
- Supports batch hash computation
- Handles missing/deleted files gracefully
- **Semantic cache**: save_analysis/load_analysis/clear_analysis for caching analysis results
- **Change-aware analysis**: has_changed_since_last_analysis() for detecting staleness
- source_fingerprint(project_root, file_ids): order-independent content fingerprint; app.check_freshness(target) compares it with MANIFEST; CLI `fresh` exits 0 (fresh) or 1 (stale), so docs generated before a commit stay fresh after it

### MCP Server Contract
- JSON-RPC 2.0 stdio-based MCP protocol server (zero external deps)
- `initialize` handshake exchanges protocol version + server capabilities
- `tools/list` returns all tool definitions with input schemas
- `tools/call` dispatches to registered tool handlers, returns text content
- `resources/list` returns all resource definitions with mime types
- `resources/read` returns resource content (JSON or Markdown)
- `notifications/initialized` acknowledged silently (no response)
- Unknown methods return standard JSON-RPC error codes
- Uninitialized requests return error code -32000
- Tools: summary, query, explain, path, findings, security_summary, taint, hotspots, cycles, communities, layers, layer_violations, rebuild, update, export_json, concepts, analytics, near, provenance, forcegraph, graphrag, memory, remember
- Resources: readmenator://summary, readmenator://graph, readmenator://findings, readmenator://analysis, readmenator://kb, readmenator://concepts, readmenator://forcegraph, readmenator://analytics, readmenator://graphrag, readmenator://memory
- Integrated with readmenatorApplication for all query/analysis operations
- Entry point: `python3 -m readmenator._mcp_server <path>` or `readmenator-mcp <path>`

### Folder README Contract
- FolderReadmeWriter.write_all(project_root) (readmenator/_folder_readme.py) writes FOLDER_README_FILENAME into each existing generated folder: AGENT_OUTPUT_DIR, WIKI_OUTPUT_DIR, GRAPHRAG_OUTPUT_DIR, APIDOCS_OUTPUT_DIR, DIAGRAM_OUTPUT_DIR, COMPONENTS_OUTPUT_DIR, RULE_GEN_OUTPUT_DIR, GH_WIKI_DRY_RUN_DIR (folder names from Config)
- Content: FOLDER_README_MARKER first line, title, purpose, regenerated-on-every-run notice, Contents table listing only entries whose glob matches on disk (directories with a trailing slash), How to use (human and agent commands), Regenerate commands; deterministic and idempotent
- A README without the marker is hand-written and never overwritten; symlinked folders and targets are refused
- is_generated_folder_readme(path, config) lets consumers skip generated READMEs: site docs (collect_doc_sources, so llms.txt), GitHub wiki collect_sources, agent MANIFEST inventory; component stale-page pruning never deletes any README
- Wired (never fatal) into run()/rebuild()/update() before README/agent injection, and into export_apidocs, export_diagrams, export_components, export_wiki, export_rules, build_graphrag, publish_github_wiki(dry_run=True)

### Payload Compression Contract
- payload_script(element_id, payload, config, compact, escape) (readmenator/_htmlpack.py): payloads under PAYLOAD_COMPRESSION_MIN_BYTES (or with PAYLOAD_COMPRESSION_ENABLED=False) stay plain application/json in the page's legacy serialization (compact/escape per page, "<" always escaped); larger ones become application/octet-stream data-encoding="gzip+base64" with mtime 0 (byte-deterministic)
- PAYLOAD_LOADER_JS: readmenatorPayload(id, fallback) / readmenatorPayloads(specs) resolve plain JSON or decode via native DecompressionStream (works from file://, zero requests); readmenatorPayloadError shows a role=alert box on load failure only (boot errors stay console errors via then(boot, onError))
- Pages boot as readmenatorPayloads([...]).then(function(__rmPayload){ unchanged body }): API browser (api-data), flows pages (fv-data), force-graph explorer (fg-data, fg-analytics; SETTINGS stays inline), edge bundle explorer (bundle-data; CFG stays inline), live vis maps (vis-*), offline SVG maps (map-*); the flows page restores the theme synchronously before data loads
- read_payload_script(document, element_id) decodes either encoding for tests and tools
- Rendered DOM is identical to the pre-compression pages in plain and compressed modes (verified in headless Chromium)

### Project Config Contract
- Per-project readmenator.toml (readmenator/_project_config.py): ensure-from-template on run/rebuild/update (never overwrites, symlinks refused), allow-listed TOML_MAP load ([project]/[branding]/[outputs]/[features]/[viewer]/[scan]/[maps]/[messages] -> Config fields), CLI flags win (non-default base values preserved), stdlib tomllib with zero-dep mini-parser fallback (3.10 safe, quote-aware `#` comments, `\n` escapes)
- Viewer config: viewer_config_dict/write_viewer_config emit maps config.json (viewer + branding/messages/maps subsets + _meta) on every run/update/diagrams export; example.readmenator.toml mirrors template_text() output
- CLI `config` ensures the file and prints its path plus the effective viewer JSON

### Viewer Config UI Contract
- Shared Config button + modal (readmenator/_viewer_ui.py): VIEWER_SCHEMA (viewer/branding/maps/messages sections with types/bounds/help, textarea for long texts), modal CSS/HTML/JS injected into force-graph, edge bundles, flows, and the maps gallery; placeholders filled in the existing single regex pass
- Config buttons are native per-template buttons (gallery pairs `[data-rm-config]` with `#theme` in CSS); no custom button class
- Apply diffs the form against its opening values, applies only what changed, and reports per key via window.ReadmenatorViewerApply(patch) returning handled keys (force-graph: snake_case modal keys mapped to camelCase SETTINGS, physics reheat, label-set rebuild, S.hulls sync, inkCache bust for theme/accents; bundles: live beta, label rebuild, INK bust; flows/gallery: redraw/theme, accents via live CSS vars); status shows "Live: ..." vs "Needs rebuild: ..."
- Stored localStorage overrides auto-apply on page load; Reset asks for confirmation before clearing them back to last-rebuild defaults
- Copy TOML emits paste-ready section blocks for readmenator.toml (strings escaped, incl. newlines)

### Injection Messages Contract
- Automated injection texts are overridable per project via [messages] (MSG_* Config fields, empty = built-in): ReadmeInjector heading/intro/agents/developers/regen (RST underline adapts to heading length), AgentInjector heading/intro/extra (extra appends raw project rules to every agent file), FolderReadmeWriter notice paragraph; override values are inserted verbatim (braces safe)
- Wired through AnalyzerFactory from the effective Config, so `readmenator . --rebuild` applies them; idempotency compares the fully built text

### Interactive Explorer Modules Contract
- ScanTextBuilder (readmenator/_scantext.py): build_for_node/build_corpus flatten names, symbols, signatures, imports, content snippets into labelled blobs; respects PRIVACY_MODE and SCANTEXT_* budgets; CLI `scan-text`
- YaraLiteEngine (readmenator/_yaralite.py): zero-dep T1/T2/T3 parser + runner (rule headers, meta, strings with nocase, conditions with N-of groups, any-of-them, $identifiers via restricted eval); validate_yaralite_rules reports tier counts; default rules in readmenator-rules/yara_rules.yar; CLI `validate-rules`
- ProvenanceAuditor (readmenator/_provenance.py): classifies findings as static (snippet present in content) vs inferred_only with corpus frequency and reading guidance; CLI `provenance`
- ExclusionList (readmenator/_exclusions.py): glob blocklist from readmenator-rules/exclusions.yaml with rule_id scoping; applied in audit_provenance before auditing
- ForceGraphRenderer (readmenator/_forcegraph.py): heterogeneous payload (file/community/layer/external nodes; member_of/layered_as/imports/resolved_imports/calls/inherits edges) with djb2 stable family colors, log2 node sizing, per-relation edge colors, symbol-scope normalization (calls edges collapsed to files, intra-file calls dropped); file nodes carry bounded `src`/`src_lines`/`src_cut`/`src_why` for the source viewer when content_map is passed ("" in privacy mode or when disabled; src_why is "budget" or "empty" via SourceViewBuilder.build_reasons); build_payload logs a console WARNING naming SOURCEVIEW_MAX_FILES/SOURCEVIEW_MAX_TOTAL_CHARS whenever budgets cut files; render()/write() emit the gallery-styled 2D/3D explorer HTML with vendored engine (readmenator/_vendor, copied to maps/vendor/), hull overlays, dimming, particles, pills, search, theme toggle, PNG/JSON export; render(live_api=True) is only used by the explorer server (ExplorerState), static write() keeps srcLive false; CLI `forcegraph`; GraphExporter.to_forcegraph delegates to it; output lives in DIAGRAM_OUTPUT_DIR and is card-linked from the maps gallery index
- AnalyticsBuilder (readmenator/_analytics.py): attribution funnel, layer/language distributions, community cohesion, hotspot ranking, rule yield, size bands, file scatter; KB Corpus Analytics section; CLI `analytics`
- ExplorerServer (readmenator/_explorer.py): stdlib HTTPServer with /api/graph, /api/analytics, /api/samples, /api/source?file= (bounded source text), /vendor/force-graph.min.js plus static write_static(); CLI `explorer` (add --no-browser to skip auto-open)
- Embedder (readmenator/_embed.py): optional sentence-transformers encode with offline Jaccard near_jaccard/cluster_jaccard/project_jaccard fallback; CLI `near <file|text>`
- Explorer UX: canvas names with collision-aware labels (top FORCEGRAPH_LABEL_TOP_N by PageRank, all past FORCEGRAPH_LABEL_ZOOM), shapes per type, findings badge, hover neighbourhood preview, inspector panel (PageRank position and percentile, metrics, purpose, filterable symbols with signatures and docs, neighbours grouped by relation, clickable, Back history, 1-3 hop reach, isolate), View button opening the source drawer (S key, right-click menu), search over labels, paths and symbol names, layouts force / cluster (community anchors) / radial (layer rings) / dag, deep links #node=&layout=; unresolved calls and imports that resolve to project files never become externals; payload file nodes carry rank, rank_pos, doc (empty in privacy mode), symbol_list
- ForceGraphRenderer.thumbnail_svg(payload): escaped ForceAtlas2 preview used as the featured gallery card in both `diagrams` and `pages`
- Explorer page (readmenator/_forcegraph_page.py): template placeholders are filled in one regex pass (payload text naming a token is never rescanned); page_settings(payload) serializes every tuneable from Config plus group_colors (layer palette, language hash colors) plus srcEnabled/srcLive/srcChunk/srcContext; member_of/layered_as edges use their own palette entries; source drawer (src-viewer + src-scrim + src-tip) renders embedded sources lazily in chunks with offline keyword/string/comment/number/call highlighting themed via CSS vars, hover definition cards from the symbol index, and Ctrl/Cmd+Click follow-to-definition (same file scrolls, other files open and refocus the graph); S key, View button, context menu, Esc/scrim close; window.ReadmenatorExplorer exposes openSource/closeSource; empty embedded source reports its src_why (budget = raise SOURCEVIEW_MAX_FILES/TOTAL_CHARS, empty = file is empty) and otherwise falls back to a live `api/source?file=` fetch only when served by the explorer server (srcLive, http); static exports keep srcLive false so Pages-style hosting (e.g. readmenator-maps/ as deploy root per .github/workflows/static.yml, where no API exists) never fires a doomed fetch (no 404), showing the stale message with the exact rebuild command instead (never blames SOURCEVIEW_ENABLED, which defaults on)
- Source viewer is always on by default (SOURCEVIEW_ENABLED=True): run()/rebuild()/update() all embed bounded sources (update() re-reads contents via _refresh_explorers, skipping symlinks and files over MAX_FILE_SIZE_MB); only PRIVACY_MODE or SOURCEVIEW_ENABLED=False disables it, with an explicit disabled message instead of the rebuild hint
- Explorer selection: engine pointer picking is disabled (force-graph repaints its shadow canvas at most every 800 ms, so picks drifted while nodes moved); hover, click, drag-to-pin, double-click isolate and right-click menus are hit-tested in the page against the positions drawn in the same frame; priority node glyph, then label, then enlarged grab area (FORCEGRAPH_MIN_HIT_PX + padding), then dependency edges (curved edges via __controlPoints); while a focus is active only highlighted edges are pickable
- Explorer 3D: 3d-force-graph (pinned CDN, orbit controls) keeps links, arrows and particles; node spheres hidden (nodeVisibility false) and flat glyphs (document tiles, hexagon communities, diamond layers, triangle externals), group halos and collision-aware labels painted on an overlay canvas from the same camera inside renderer.render, with depth fade; camera fly-to, orbit toggle, cluster anchors on a Fibonacci sphere, layer shells; falls back to 2D when the CDN is unreachable
- Explorer actions: reach direction (both, upstream used by, downstream uses) x depth (1, 2, 3, all); path finder (directed first, then reverse, undirected, then via shared group) with hop-by-hop passport; edge passport (sentence, endpoints, mutual dependency, cycle closure, upward layer crossing, community bridge, parallel relations); group passport (cohesion, depends-on and used-by groups); color by community/layer/language; node and edge type filters; hide/unhide; lenses: import cycles (Tarjan SCC), no importers, disconnected, hubs; deep links node, edge, path, lens, group, view, layout, color, dir, depth; window.ReadmenatorExplorer API
- AnalyzerFactory exposes forcegraph, analytics, scantext, provenance, exclusions, embedder, symindex, components, ollama (lazy init); app.export_forcegraph/explorer_state/serve_explorer/analytics/scan_texts/near/audit_provenance/validate_yaralite/export_components; run()/rebuild()/update() write readmenator-maps/graph-force.html via _maybe_export_forcegraph/_refresh_explorers (skipped when FORCEGRAPH_ENABLED=False) plus readmenator-diagrams/ via export_components (skipped when COMPONENTS_ENABLED=False); export_diagrams() writes it first and links it from the gallery index; export() also writes it

### GraphRAG Contract
- GraphRagBuilder.build(nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, concept_graph, content_map, memory_notes) returns a deterministic GraphRagIndex (readmenator/_graphrag.py); zero LLM tokens
- Entities: file:, sym:<file>::<name>@<line>, concept:, ext: (only imports that do not resolve to project files), memory:log; each with description, level-0 community, degree, global PageRank on the symmetric entity graph
- Relationships: defines, resolved_imports, calls (symbol-resolved, INFERRED), inherits, documents (concept -> file), imports (file -> external), depends_on (concept verbs); weights from the category EdgeKind model
- Text units: one per symbol spanning to the next symbol (capped by GRAPHRAG_TEXT_UNIT_MAX_LINES/CHARS) plus file docs; PRIVACY_MODE drops source text and docs; MEMORY.md session-log notes become memory text units
- Report hierarchy: level 0 = analyzer communities (plus "unassigned files"), level 1 = Louvain themes on the community quotient graph (GraphAnalyzer.partition), level 2 = root; extractive summary and findings (PageRank rank, importers, security counts, hotspots, cycles, layer violations, taint, dataflow, surprising bridges); rating = GRAPHRAG_RATING_CENTRALITY_WEIGHT x PageRank share + GRAPHRAG_RATING_RISK_WEIGHT x capped severity risk
- GraphRagSearcher: local_search = BM25 over entities and text units -> seeds -> Personalized PageRank (GRAPHRAG_PPR_ALPHA) -> top entities, relations among them, community reports, source units; global_search = BM25 over level-0 reports, findings mapped by query overlap, reduced under the root overview; choose_mode routes broad hints or no entity hit to global
- Context packing gives each section its GRAPHRAG_*_SECTION_SHARES slice of GRAPHRAG_CONTEXT_BUDGET_TOKENS x AGENT_CHARS_PER_TOKEN plus unused carry; empty sections emit no heading
- GraphRagStore writes readmenator-graphrag/index.json (schema_version), entities/relationships/communities/text_units.jsonl, REPORTS.md; load() rejects other schema versions
- Wired into run() (_maybe_write_graphrag), CLI `graphrag` / `ask "<q>" [--local|--global] [--budget N]`, MCP tool readmenator.graphrag + resource readmenator://graphrag, gallery docs group, llms.txt section; scanner skips GRAPHRAG_OUTPUT_DIR

### Project Memory Contract
- ProjectMemory (readmenator/_memory.py) writes readmenator-agent/MEMORY.md: 1 purpose and domain (README lead with citation, concept vocabulary, subsystems), 2 workflow (commands detected from pyproject, package.json, Makefile, go.mod, Cargo.toml, CI workflows; session protocol), 3 rules and constraints, 4 style norms, 5 minimum deliverables (each Declared + Measured baseline), 6 risks, 7 session log
- Declared rules: bullet or numbered lines under headings matching MEMORY_*_KEYWORDS in MEMORY_RULE_SOURCES files, quoted verbatim with file:line; MEMORY_HEADING_EXCLUDE headings and readmenator-injected anchor blocks skipped; symlinks and oversized files skipped
- Session log between NOTES_BEGIN/NOTES_END markers is preserved byte for byte by write(); remember(note, kind) validates MEMORY_NOTE_KINDS, sanitizes to one line (no control chars, comment markers neutralised, MEMORY_NOTE_MAX_CHARS)
- CLI `memory`, `remember "<note>" --kind <kind>`; MCP tools readmenator.memory, readmenator.remember, resource readmenator://memory; MANIFEST read_order starts with MEMORY.md; agent injection step 0 points at it

### Agent Skills Contract
- readmenator/_skills/<readmenator-*>/SKILL.md with name + description frontmatter (orient, ask, change, memory)
- SkillInstaller.install(project_root, target) copies only readmenator-* skills into SKILLS_TARGET_DIR, idempotent, refuses symlinked destinations; maybe_install_on_run installs during run() only when the target's parent (e.g. .claude/) already exists and SKILLS_INSTALL_ON_RUN is set
- CLI `skills [--target DIR]`

### Graph Layout Contract
- forceatlas2_frames(ids, edges, settings) (readmenator/_graphlayout.py): Jacomy 2014 ForceAtlas2 with degree-weighted repulsion, LinLog attraction, degree-weighted gravity, swing/traction adaptive speed; seeded start; evenly spaced snapshots incl. start and end; numpy path with pure Python fallback under a budget; settings.dims 2 (default, unchanged random sequence) or 3
- normalize_cloud(points, quantile, max_radius): centers a 3D cloud, scales the radius quantile to 1, tanh-compresses outliers so none exceeds max_radius
- spherical_edge_bundling(groups, edges, radius, beta, samples, inner_ratio): one Fibonacci lattice point per member; recursive balanced bisection (group runs of near-equal size vs points sorted on their widest axis) gives every group one contiguous cap of exact size; first-listed members (hubs) take the points nearest the cap center; hubs at cap mean direction x inner_ratio, root at the center; same control polygon and B-spline as the circle (shared, dimension-agnostic)
- fit_frames maps snapshots into a pixel box using the final layout's bounds (fixed camera); interpolate_frames blends snapshots
- hierarchical_edge_bundling(groups, edges, center, radius, beta, samples): leaves on a circle by group, control polygon leaf -> group hub -> center -> group hub -> leaf, straightened by beta, sampled as clamped uniform cubic B-spline

### Edge Bundle Explorer Contract
- BundleGraphRenderer (readmenator/_bundlegraph.py) derives its payload from ForceGraphRenderer.build_payload: file nodes (id = force-graph id for deep links, path, label, group, color, layer, language, PageRank, findings, purpose; "" in privacy mode), groups in analyzer community order plus a trailing "unassigned" group, members by PageRank, distinct directed file pairs from resolved_imports/imports/calls/inherits
- Each node carries a circle angle (hierarchical_edge_bundling) and a unit-sphere position (spherical_edge_bundling); each group carries its arc, 2D and 3D hub, and cap center; the page builds the B-splines itself so beta is live
- Page (readmenator/_bundlegraph_page.py): one canvas, zero external requests; 2D circle (radial labels for all files up to BUNDLEGRAPH_LABEL_ALL_MAX, community arcs) and 3D sphere (perspective camera, drag rotate, wheel zoom, auto-rotate, depth fade, fly-to on focus); hover/click hit-testing on drawn positions; cyan = imports, pink = imported by; node panel (metrics, purpose, imports and importers, links into graph-force.html #node= in 2D/3D), community panel (inside/out/in, cohesion, flows, members); crossing-only, direction, color by community/layer/language, search, PNG, theme; deep links view, node, group, beta, color, dir, cross; prefers-reduced-motion disables reveal, rotation and particles; window.ReadmenatorBundles
- Placeholders filled in one regex pass; payload JSON escapes angle brackets; titles and hrefs HTML-escaped
- Written beside graph-force.html from the same payload by app._write_forcegraph whenever BUNDLEGRAPH_ENABLED (run/rebuild, export, diagrams, pages); gallery gets a featured "Edge Bundle Explorer" card with a circular bundle thumbnail; CLI `bundles`; AnalyzerFactory exposes bundlegraph (lazy init)

### Semantic ConceptGraph Contract
- ConceptExtractor class with extract(nodes, edges, resolved_edges) entry point (readmenator/_concepts.py)
- Second-brain parameters as extra layer: nouns are ConceptNode (EXTRACTED), verbs are ConceptRelation (INFERRED)
- Atomic zero-token tokenization: path, label, symbol names, docs split on camelCase, dots, slashes, separators; stopwords and short tokens filtered
- Verb vocabulary from structure: imports->consumes, resolved_imports->depends_on, calls->invokes, inherits->extends, fallback bridges
- Concept-concept aggregation over file edges with strength normalization and top-N budgets
- Dialectic prompts: overlapping file sets (Jaccard>=0.3) emit Thesis/Antithesis/Synthesis questions
- Deterministic: sorted traversal, ranked by file coverage then mentions then name
- Respects PRIVACY_MODE (doc text skipped) and CONCEPT_ENABLED (empty graph when off)
- Wired into DeepAnalysisRunner (AnalysisResultV2.concept_graph), KB Concept Graph section, wiki concepts.md + concept_graph.json, agent CONCEPTS.md, exporter JSON/Cypher/Obsidian, video collect concepts/dialectic, MCP concepts tool + resource
- Configurable via CONCEPT_ENABLED, CONCEPT_MIN_FILES, CONCEPT_MAX_CONCEPTS, CONCEPT_MAX_RELATIONS, CONCEPT_MIN_TOKEN_LEN, CONCEPT_STOPWORDS, CONCEPT_MAX_FILES_PER_CONCEPT, CONCEPT_DIALECTIC_MAX

### Watcher Contract
- Polling-based filesystem monitor (no external deps)
- Combined hash of file paths + sizes + mtimes for change detection
- Triggers callback (auto-rebuild) when changes detected
- Respects IGNORE_DIRS and symlink exclusion
- Configurable polling interval

### UML Generator Contract
- render_mermaid_class_diagram(nodes, edges): returns Mermaid classDiagram string
- Collects class, struct, interface, trait, enum, record, protocol, extension symbols
- Groups symbols by file, renders methods up to 10 per class
- Shows inheritance edges (inherits relation from parsers)
- Shows dependency/usage edges (imports relation between files with class symbols)
- Respects UML_MAX_CLASSES limit (default 50)
- Returns empty string when no class-like symbols found
- ID sanitization: alphanumeric + underscore preserved, special chars replaced, digit prefix handled
- generate_code(nodes, edges, target_language): returns class stubs in target language
- 12 target languages: cpp, java, csharp, python, go, rust, php, kotlin, scala, swift, dart, ruby
- Each language generator produces idiomatic class/type declarations
- Unknown language returns error message string
- Type mapping from Python-style hints to target language types

### README Injection Contract
- ReadmeInjector class with inject(project_root) and remove(project_root) methods
- Detects README.md, README.rst, Readme.md, readme.md, and 4 other variants
- Injects a section linking to KNOWLEDGE_BASE.md and every run artifact with HTML anchor comments
- Injected section covers: KNOWLEDGE_BASE.md, readmenator-agent/ (INDEX, SYMBOLS, ARCHITECTURE, API, GOTCHAS, SECURITY, MEMORY, MANIFEST, KB_*, recipes), readmenator-wiki/ (index, community_*, connections.json, queries, REPORT), readmenator-graphrag/ (ask), readmenator-apidocs/ (index, modules, architecture, classes, genindex, COVERAGE, index.html, api/ JSONL), readmenator-maps/ (index gallery + 5 maps + graph-force.html + graph-bundle.html + components.html), docs/ site (llms.txt + video), readmenator-diagrams/ (analysis.json), readmenator-rules/ (Semgrep + yara + exclusions), readmenator.mp4, .cursorrules, SARIF audit, cache, skills
- Idempotent: second injection returns False when injection text is identical
- **Outdated detection**: when anchor exists but text differs from current template, removes old and injects new
- **Tag creation**: when the anchor tag is missing (or only half present), the section is created fresh; partial markers are stripped before appending
- Preserves existing README content
- Markdown injection: link, description, AI/human context
- reStructuredText injection: adapted RST syntax
- Uses configurable kb_filename, agent_output_dir, wiki_output_dir, graphrag/apidocs/maps/pages/components/rules dirs, video/cursorrules/sarif/cache/skills/llms/forcegraph/bundle names (AnalyzerFactory wires every Config value)
- Remove method strips injected section cleanly
- Returns False when no README found or no injection present
- Guided by README_INJECTION_ENABLED config flag

### Agent Injection Contract
- AgentInjector class with inject(project_root) and remove(project_root) methods
- Detects 15 AI agent config files: AGENTS.md, CLAUDE.md, SOUL.md, LLM.md, CONVENTIONS.md, .cursorrules, .instructions.md, .windsurfrules, .aider.conf.yml, SKILL.md, GEMINI.md, AGENTS.override.md, RULES.md, PROJECT_RULES.md, .github/copilot-instructions.md, plus .cursor/rules/*.mdc globs
- Injects section referencing both KNOWLEDGE_BASE.md and readmenator-agent/ directory
- Injected section points agents at readmenator-wiki/index.md first (big picture) before grep-friendly files
- Injected markdown is a 5-step numbered workflow (freshness via MANIFEST git_commit vs `git rev-parse HEAD`, orient, locate with NAME*.md greps, subsystem context, gotchas before editing), kept short because it is paid on every agent session
- Idempotent: second injection returns False when injection text is identical
- **Outdated detection**: when anchor exists but text differs from current template, removes old and injects new
- Markdown vs plain text injection based on file suffix (.yml/.yaml = plain, else markdown)
- Uses configurable kb_filename and agent_output_dir parameters
- Guided by AGENT_INJECTION_ENABLED config flag
- Auto-install feature: ensure_readmenator_installed() checks and installs via pip

### Agent Output Contract
- AgentOutputGenerator class with generate() entry point
- Generates grep-optimized, flat-markdown files in readmenator-agent/ directory
- Output layout: MANIFEST.json, INDEX.md, SYMBOLS.md, ARCHITECTURE.md, SECURITY.md, API.md, GOTCHAS.md, recipes/*.md, KB_<subsystem>.md
- Paging: any document over AGENT_OUTPUT_MAX_LINES splits on `## ` section boundaries into NAME.md, NAME_p2.md, ...; table headers repeat per page; pages link Pages/Previous/Next; stale owned pages pruned each run (user files untouched)
- MANIFEST.json: schema_version, git_commit + git_branch (read from .git, no subprocess), source_fingerprint (_cache.source_fingerprint: sha256 over sorted path + content hashes), freshness_check, relative project_root (never absolute), imports/calls/inherits counted by relation, subsystems, layer-aware entrypoints, read_order, documents inventory (path, lines, approx_tokens)
- Purposes come from _purpose.file_purpose: first clean sentence, word-boundary truncation (AGENT_PURPOSE_MAX_CHARS), fallback `Symbol: sentence` from the primary documented public symbol
- **Subsystem inference**: groups nodes by directory, names from last directory component (never hardcoded)
- Files with >= AGENT_OUTPUT_MIN_SUBSYSTEM_FILES get their own KB_<name>.md
- Unassigned files go to KB_root.md (flat project) or KB_misc.md (scattered)
- INDEX.md: table format `| File | Purpose | Subsystem | Symbols | Used by |` (grep-friendly, pipes escaped, Used by = distinct resolved importers)
- ARCHITECTURE.md: flat list of internal dependency pairs; External Imports one line per source file, excluding imports that resolve to project files
- SECURITY.md: findings grouped by severity, flat list (critical->info), each line with enclosing symbol, CWE, and Fix hint
- API.md: one line per public function/method (`Owner.method`, kind, file:line, signature, first doc sentence); Depends on / Imported by stated once per file; private `_helpers` (AGENT_API_PUBLIC_ONLY) and AGENT_API_EXCLUDE_LAYERS files skipped
- GOTCHAS.md: god nodes (with importer counts), Blast Radius from change impact, hotspots, closed-loop cycles (`a -> b -> a`, never double-closed), layer violations, dataflow leads; AGENT_GOTCHAS_EXCLUDE_LAYERS files (tests) left out of centrality lists
- recipes/: add-function.md, change-impact.md, fix-cycle.md, fix-security.md, reduce-complexity.md (grep paths use NAME*.md globs)
- recipes/ are grounded in project data: fix-cycle names the actual cycle + per-file import grep, fix-security lists top 3 findings with fixes, reduce-complexity names the top hotspot
- All output is plain Markdown, no JSON wrapping, no fenced code blocks around data
- Every line is greppable
- No file exceeds AGENT_OUTPUT_MAX_LINES (default 500), enforced by paging
- Configurable via AGENT_OUTPUT_ENABLED, AGENT_OUTPUT_DIR, AGENT_OUTPUT_MIN_SUBSYSTEM_FILES

### Agent Wiki Contract
- WikiGenerator class with generate() entry point (readmenator/_wiki.py)
- Generates navigable, progressively disclosed wiki in readmenator-wiki/ directory (offline, zero tokens, deterministic)
- Output layout: index.md, community_<id>_<slug>.md, connections.json, queries.md, REPORT.md
- index.md: Second Brain entry point (overview synthesis, stats, token estimate, reading order, god nodes, strongest connections, navigation tips)
- Community pages: Definition (core file by symbol count, garbage-doc filtered purpose), Files (directory-grouped when over budget), Key Symbols, Internal vs External Edges, Connections, Risks (scoped security with enclosing symbol + Fix hint, taint, closed-loop cycles, layer, dataflow), Open Questions, Sources
- connections.json: typed bridges (depends_on EXTRACTED 0.9, bridges INFERRED from surprising connections, duplicates INFERRED from symbol overlap Jaccard>=0.3, shares_context INFERRED 0.5) sorted by strength desc
- Purpose cleaning: banner runs, SPDX lines, bare filenames, and parenthesized metadata stripped (never shown as purpose)
- Unassigned files covered by computed orphans community (never dropped from the wiki)
- Stale community pages pruned on regenerate (no rot across runs with shifting ids)
- Duplicate community labels disambiguated in index (`label (community <id>)`)
- Duplicate god-node basenames disambiguated in overview (full path on repeat)
- Oversized files flagged (`WIKI_LARGE_FILE_KB`): tagged in God Nodes, listed in Stats and REPORT (checked-in build artifacts skew centrality)
- queries.md: suggested questions starter plus append-only answer log (feedback loop)
- REPORT.md: honest audit (EXTRACTED vs INFERRED vs AMBIGUOUS counts, coverage, orphans, limits, token benchmark, reproduce commands)
- lint(project_root): health check (missing dir, missing index, no community pages, invalid connections.json)
- Respects PRIVACY_MODE (strips doc text from synthesis)
- Every connection tagged with confidence; ambiguous edges reported, never hidden
- Configurable via WIKI_ENABLED, WIKI_OUTPUT_DIR, WIKI_MAX_FILES_PER_PAGE, WIKI_MAX_SYMBOLS_PER_PAGE, WIKI_MAX_CONNECTIONS
- Large-file threshold via WIKI_LARGE_FILE_KB (default 256)
- CLI: `wiki` generates the wiki, `lint-wiki` health-checks it (exit 1 on issues)

### Dataflow Analyzer Contract
- DataflowAnalyzer class with analyze(nodes, content_map) entry point (readmenator/_dataflow.py)
- Procedural intra-function def-use over symbol line spans: UNINIT_USE, DEAD_STORE, UNCHECKED_ALLOC (all INFERRED)
- Zero tokens: brace-depth spans (locals never truncate), block-comment stripping, strings-before-comments, sizeof-is-not-a-read
- Models C idioms: &out-params, array args to fillers (multiline calls tracked), subscript stores, asm outputs, assert-macro checks, fd/MAP_FAILED checks, function-pointer calls, alias-pointer stores, member-base attribution
- Statics/globals skipped (zero-init + cross-function visibility); same-line reads compared positionally
- Wired into DeepAnalysisRunner (DATAFLOW_ENABLED), KB Dataflow Analysis section, agent GOTCHAS, wiki Risks
- Configurable via DATAFLOW_ENABLED, DATAFLOW_MAX_ISSUES (default 50)

### Architecture Linter Contract
- ArchitectureLinter class with lint(nodes, edges, resolved_edges, layers, content_map) method
- ARC001: File exceeds configurable line threshold (LINTER_MAX_LINES, default 300)
- ARC002: Cross-layer import violations (presentation -> data_access forbidden)
- ARC003: Circular dependency detection in resolved import graph
- ARC004: Unresolved/ambiguous call targets via the symbol index (info, file:line + caller -> callee + definition evidence)
- Respects LAYER_VIOLATION_STRICT_MODE for warning edges
- Returns List[LinterViolation] sorted by severity (error > warning > info)
- Configurable via LINTER_ENABLED, LINTER_CROSS_LAYER_VIOLATIONS, LINTER_UNRESOLVED_CALLS flags

### Symbol Index Contract
- SymbolIndex class with build/resolve/extract_call_sites/methods_index entry points (readmenator/_symindex.py)
- Definitions carry file spans (end_line from the next symbol); deterministic sorted traversal
- Python call sites exact via ast (caller scope, line, column); other languages regex-approximated with caller attribution
- Resolution tiers: BUILTIN (stoplist) > SAME_FILE > IMPORTED (via resolved imports) > UNIQUE > AMBIGUOUS > UNRESOLVED
- methods_index keys use the `file|file::symbol` shape with CLASS/FUNCTION types and short content hashes
- CallSite.receiver records the attribute-call receiver (ast text for Python, bounded regex look-behind elsewhere)
- Configurable via SYMINDEX_MAX_CALL_SITES, SYMINDEX_BUILTINS, SYMINDEX_RECEIVER_WINDOW; never needs the network or an LSP

### Local Ollama Contract
- OllamaClient class with generate/describe_component/available entry points (readmenator/_ollama.py)
- Stdlib urllib against the local daemon only; bounded timeout; every failure returns "" (never fatal)
- Thinking-model `<think>` blocks stripped; prompt and output capped by config
- Used only for prose (component descriptions), never for structure; default off (zero-token)
- Configurable via OLLAMA_ENABLED (default False), OLLAMA_HOST, OLLAMA_MODEL, OLLAMA_TIMEOUT_S, OLLAMA_MAX_PROMPT_CHARS, OLLAMA_MAX_CHARS

### Component Diagram Contract
- ComponentDiagramBuilder class with build/mermaid_lr/overview_markdown/component_markdown/render_page/thumbnail_svg/write entry points (readmenator/_components.py)
- analysis.json carries the component model: metadata (source_tree_hash, depth, file coverage), description, files, methods_index, components, components_relations
- Components come from analyzer communities (component_id 1..N, nested i.j by top directory when expandable); relations aggregate cross-component imports/calls with method-level key_edges + call-site lines; nested levels roll parent edges up like project_relations_to_level (outside files drop, self-pairs drop)
- Overview renders their `graph LR` style (quoted labels, `"phrase"` edges, click links) plus Related Classes/Methods with file#L anchors
- index.html renders the layered diagram offline as inline SVG in the readmenator dark theme (cyan accents, shared readmenator-theme key): longest-path LR ranks; boxes with name, file/symbol counts, dominant-layer border + label, top symbols, file counts, hub glow for the top PageRank component; arrows weighted by call/import evidence with phrase + counts labels; hover description cards; click-to-component anchors; layer legend; a Relations section with evidence and file:line call samples; nested SVGs per expandable component; drag-pan/wheel-zoom, Reset/Fit/PNG; zero external requests
- Written to COMPONENTS_OUTPUT_DIR (scanner-skipped) on every run when COMPONENTS_ENABLED, plus CLI `components`; maps and docs galleries get a featured "Component Diagrams" card opening a self-contained components.html copy inside the maps dir (never a ../.. href, so subpath Pages deployments keep working; source refs render as text there, links home); collect_doc_sources ships the markdown into the site drawer and llms.txt
- Configurable via COMPONENTS_ENABLED/OUTPUT_DIR/MAX_KEY_ENTITIES/MAX_KEY_EDGES/MAX_ALL_EDGES/EXPAND_MIN_FILES/DEPTH_CAP

### Docstring Parser Contract
- parse_docstring(text) (readmenator/_docstrings.py) returns a DocComment (summary, description, params, returns, yields, raises, attributes, examples, notes, see_also, deprecated, since, style); empty text yields an empty comment
- detect_style order: C# XML > reST field lists > NumPy underlined sections > Javadoc/JSDoc/PHPDoc/KDoc/Doxygen tags (@ and backslash forms, [in]/[out], {type}, [name=default], PHP Type $name) > Google sections > Rustdoc headings > plain
- Google "Defaults to X." and NumPy "type, optional"/"default" populate DocField.default; doctest (>>>) blocks become examples
- recover_comment(lines, line, language, lookback) recovers the adjacent comment block above a declaration with line structure intact: ///, //!, //, /** */, /* */, #, ##, --, ;, Elixir @doc heredocs; decorators/attributes/annotations ([[x]], #[x], @X, [X]) skipped; shebangs, ///< trailing docs, rulers, and blank-line-separated blocks ignored

### API Reference Contract
- ApiReferenceBuilder.build(nodes, edges, resolved_edges, content_map) (readmenator/_apidocs.py) returns a deterministic ApiReference (entities keyed by uid `file` / `file::Qual.name`, modules, warnings, coverage, meta)
- Python: own ast pass with exact signatures (annotations, defaults, / and * markers, *args/**kwargs), decorators, nested classes, constructor/property/classmethod/staticmethod kinds, enum/protocol/exception class kinds, dataclass fields as attributes, module constants with following docstrings, `__all__` visibility, inferred raises, return/generator behaviour; class Args docs flow into an undocumented `__init__`
- Other languages: parser symbols plus recover_comment docs, members nested by brace span (string/comment aware, prototypes ending in ; never span) or indentation, signatures split into typed params and return types per language family, visibility from modifiers / Go case / Rust pub / C static / _ and # prefixes / Elixir defp; include guards dropped; module doc dropped when it is really the first declaration's doc
- Tests (APIDOCS_TEST_PATH_TOKENS), minified bundles (APIDOCS_SKIP_SUFFIXES), and vendored trees (APIDOCS_EXCLUDE_DIRS) are skipped; APIDOCS_MAX_ENTITIES truncates with meta.truncated
- Cross-references: bases resolved to project types (subclasses filled), C-family definitions inherit header prototype docs, undocumented overrides inherit base docs (marked with an Inherited note), callers/callees from the symbol index filtered by receiver typing (typed self/var/attr receivers re-resolved to the owning class; untyped attribute calls dropped unless the receiver names the module or class)
- Warnings: DOC001 undocumented public item, DOC002 parameter not documented, DOC003 documented parameter missing from the signature, DOC004 return not documented, DOC005 raised exception not documented; coverage overall/by kind/by module over public modules, types, and callables
- PRIVACY_MODE keeps signatures and parameter names only
- ApiMarkdownRenderer/ApiDocsWriter (readmenator/_apidocs_render.py) write APIDOCS_OUTPUT_DIR: index.md (modules by package with coverage), modules/<slug>.md (contents, Mermaid classDiagram, Mermaid call graph, per-entity anchors, badges, signature, merged parameter table, returns, raises incl. undocumented inferred ones, examples, admonitions, see also, calls/called by, source file#Lline links), classes.md, genindex.md, COVERAGE.md, architecture.md, api/ (index.json with schema_version, meta, coverage, module listing, warning total and grep usage; modules/<slug>.jsonl one compact entity per line; warnings.jsonl one warning per line; read_api_jsonl reassembles the monolithic shape), index.html; api.json only when APIDOCS_JSON_MONOLITH (stale api.json removed otherwise); stale module pages and module JSONL files pruned; symlinked output refused
- ApiLinker resolves backticks, Sphinx roles (:class:, :func:, ~), and {@link} to anchors, never inside fenced code
- render_api_site (readmenator/_apidocs_page.py): one self-contained page, JSON payload with < > & escaped (payloads of PAYLOAD_COMPRESSION_MIN_BYTES or more embedded as gzip+base64 with mtime 0, decoded offline by DecompressionStream, load errors shown in the page; api/ JSONL and modules/*.md stay plain and greppable), placeholders filled in one regex pass, zero requests by default; the Architecture page renders Mermaid only when the reader clicks the button (APIDOCS_MERMAID_CDN_JS)
- Wired into run() and update() (_maybe_write_apidocs, never fatal), CLI `apidocs`, `doc-coverage [--fail-under N]` (exit 1 below threshold); scanner skips APIDOCS_OUTPUT_DIR; README injection lists it

### Architecture and Execution Flow Contract
- ArchitectureDiagramBuilder (readmenator/_flowcharts.py): components from analyzer communities (directory fallback), tests and vendored files excluded; weighted component graph ordered by weighted Eades-Lin-Smyth so most imports point downward; edges against the order are upward dependencies (dashed red, declared reversed so Mermaid keeps tiers in order); tiers = longest path over forward edges; forward edges transitively reduced; Tarjan SCC reports cycles; thick arrows for the top quartile; invisible ~~~ anchors keep tier order
- ExecutionFlowBuilder: call graph from SymbolIndex plus PythonReceiverTypes (same-name methods disambiguated by line); entry points scored from __main__ guards, compiled-language main, entry-style names and files, and call-graph sources; a guard that only calls picked entries is skipped
- walk(): depth-first in call-site order, FLOW_MAX_DEPTH / FLOW_MAX_STEPS, repeats not re-expanded, recursion flagged
- Mermaid outputs: call tree (flowchart LR, numbered call order, Owner.method labels), Python control flow (decisions, loops with back edges, try/except, with, match, return/raise ends, collapsed straight-line runs, if/elif dispatch on one subject compacted into one switch node), cross-file sequenceDiagram; labels escaped with Mermaid entity codes
- KNOWLEDGE_BASE.md gains Architecture Overview and Execution Flows (TOC entries only when present); run() and update() pass content_map; architecture.md in the API reference uses the same renderers

### Flow Layout and Viewer Contract
- FlowGraph/FlowNode/FlowEdge (readmenator/_flowlayout.py); layout_flow(graph, metrics, TB|LR): node sizes from monospace metrics with wrapped detail lines (FLOW_NODE_MAX_CHARS, FLOW_NODE_MAX_LINES); explicit ranks (architecture tiers) or longest-path ranks without DFS back edges; barycentric sweeps; ranks wider than FLOW_MAX_PER_ROW / ARCH_DIAGRAM_MAX_PER_ROW wrap into extra rows (never a strip); trunk edges (no, done, otherwise) stay under their parent, branch edges (yes, each, except) go right; nodes never overlap; forward edges are vertical cubics, back/upward edges bend around the right side; architecture lanes carry tier titles; layout_sequence places participants and messages
- ArchitectureDiagramBuilder.model and ExecutionFlowBuilder.call_tree_model / control_flow_model / sequence_model build FlowGraphs with viewer payloads (component files with purpose and importers; definitions with kind, file, line, signature, doc, qual; CFG steps with the docs of the functions they call, resolved through the typed call graph); if/elif chains become a ladder; to_mermaid converts any FlowGraph for Markdown
- build_flow_graphs(config, nodes, edges, resolved, content_map, analysis, layers) returns laid-out graphs: architecture first, then per entry point control flow (when it has more than 3 nodes), call tree, sequence
- render_flows_page (readmenator/_flowpage.py): self-contained page (payload with < > & escaped, single-pass placeholders, zero requests) with per-diagram cards, toolbar (fit width, 100%, zoom, fullscreen, SVG download), drag pan, Ctrl+wheel zoom, hover highlighting, click detail panel with API reference links; theme from shared CSS variables and the readmenator-theme key
- Written as readmenator-maps/flows.html (featured gallery card with flow_thumbnail_svg, also in the docs site), readmenator-apidocs/flows.html, and the API browser Flows tab (#/flows); CLI `flows`
- Video acts X The Tiers and XI Execution (VIDEO_TIERS_S, VIDEO_FLOW_S, VIDEO_FLOW_VIEW_WIDTH) draw the same laid-out graphs with PIL

### Python Receiver Typing Contract
- PythonReceiverTypes(contents, language) (readmenator/_pytypes.py) indexes scopes, method owners, class bases, locals typed by constructor calls / annotations / annotated parameters, self attributes assigned or annotated, class-level annotated fields
- receiver_class, resolve_method (lineage in base order), accepts (True/False for Python callers, None otherwise); unknown stays unknown

### Layout Quality Contract
- optimize_bundle_order(groups, edges, sweeps, passes, gap) (readmenator/_graphlayout.py): first group fixed, greedy weighted chaining + 2-opt on arc-center distance, center-out hub seeding, barycentric sweeps; each stage accepted only when bundle_angular_cost drops, so more sweeps never cost more; deterministic, membership preserved
- refine_sphere_leaves / spherical_edge_bundling(refine_sweeps, affinity_edges): members take cap points facing their neighbours, caps keep exactly their lattice points, kept only when total chord length drops
- Edge bundle explorer and video bundle/sphere acts use the optimized order (BUNDLEGRAPH_ORDER_OPTIMIZE); thumbnails follow payload angles
- ForceGraphRenderer payload nodes carry deterministic ForceAtlas2 seeds s2 (2D) and s3 (3D) scaled so the median edge equals FORCEGRAPH_LINK_DISTANCE; the explorer starts the force layout from them with FORCEGRAPH_SEED_VELOCITY_DECAY (pins respected, seeded once per view mode)

### Dead Code Stripper Contract
- DeadCodeStripper class with identify(nodes, edges, resolved_edges) method
- Builds in-degree map from resolved import edges
- Excludes configurable entry points (DEAD_CODE_ENTRY_POINTS)
- Classifies recommendations: MOVE_TO_TRASH for functions/variables, REVIEW for classes
- Returns List[DeadCodeReport] sorted by file path
- Configurable via DEAD_CODE_ENABLED flag

### Cursor Rules Generator Contract
- CursorRulesGenerator class with generate(nodes, edges, analysis, layers, violations, project_root) method
- Produces deterministic .cursorrules file content
- Base rules: separation of concerns, file length limits, no absolute paths, no hardcoded config
- Layer constraints from detected architectural layers
- Analysis constraints from god nodes and community boundaries
- Violation rules from linter output (limited to 10 entries)
- Optional file output when project_root is provided
- Configurable via CURSORRULES_ENABLED and CURSORRULES_OUTPUT flags

### Monolith Refactorizer Contract
- MonolithRefactorizer class with analyze(nodes, edges, resolved_edges, content_map) method
- Identifies files exceeding REFACTORIZER_MIN_LINES threshold
- Groups symbols by kind (class, function, etc.) to detect extractable clusters
- Generates EXTRACT_CLASS, EXTRACT_FUNCTION, EXTRACT_MODULE actions
- Estimates impact from resolved import edges
- generate_script(plan, project_root): produces executable bash script with sed commands
- Returns List[RefactoringPlan] sorted by line count (largest first)
- Respects REFACTORIZER_MAX_FILES limit
- Configurable via REFACTORIZER_ENABLED flag

### Interactive System Maps Contract
- SystemMapBuilder class with build() and build_all() entry points
- Builds five typed maps from scanned topology: architecture, workflow, sequence, dataflow, lifecycle
- Architecture: centrality-ranked files grouped by layer with resolved import edges
- Workflow: one representative file per architectural lane chained as the delivery path
- Sequence: top participants as lifelines with directed call messages
- Dataflow: sources through transforms to data_access stores with sensitivity marking
- Lifecycle: layer states with transitions plus retry edges for mutual dependencies
- Deterministic: identical input yields identical coordinates and bytes (sorted selection, fixed layout)
- Fit by construction: per-lane member caps from canvas geometry, column gap compression with DIAGRAM_MIN_GAP floor, lane priority dropping, sequence participant capacity; every built map passes canvas-bound validation at any project size
- Oversized graphs truncated to DIAGRAM_MAX_NODES with internal edges capped at DIAGRAM_MAX_EDGES
- SystemMapValidator class with validate(map) returning a MapReceipt (passed, checks, errors, warnings)
- Nine deterministic checks: schema, unique_ids, endpoints, connectivity, size_bounds, canvas_bounds, overlap, label_clearance, export_ready
- Stable rule codes D000 (unknown kind), D001 (duplicate id), D002 (dangling edge), D003 (empty map), D004/D008 (size limits), D009/D010 (canvas bounds), D011 (overlap), D013/D014/D015 (guided view violations); advisories D005/D006/D007/D012
- compare(base, head) returns a MapDelta with added, removed, changed, moved, rerouted facts
- InteractiveMapRenderer class with render(map) returning one self-contained HTML document
- Zero external requests: inline SVG, inline CSS, inline scripts, no CDN, no fonts fetched
- Retained as offline fallback; default published output uses the live renderer below
- Canvas uses the darkest token with lifted node panels; edge labels carry halo strokes for readability
- Four visual presets with identity (classic, signal-flow glow, blueprint grid with square nodes, warm editorial) and dark/light themes from Config
- VisNetworkRenderer class with render(map) returning a physics-driven vis.js document
- Live map selection: hover preview card (the #peek element ships in the template); click dims everything outside the 1-hop neighbourhood (reach modes still filter), fits the camera, and opens a passport with metric tiles, an ego mini-map SVG (used by left, imports right, clickable), clamped doc, neighbour chips, filterable symbol table, Back history (Backspace); guide rows hide while focused
- Live maps color nodes by code community (legend with counts, click isolates, #community=id deep link, C toggles to role colors), size dots by link count, always label the DIAGRAM_VIS_LABEL_TOP_N most connected files and reveal the rest on zoom, dim edges that light up on hover/selection, forceAtlas2Based physics from DIAGRAM_VIS_* settings
- Layer roles are honest: utility -> core, testing -> test (never "external" for project files)
- Default export format for `diagrams`, `diagram`, and `pages` (CDN bundle URLs from Config, pages need network access)
- Map nodes carry documentation payloads: file doc, language, symbol records with signatures, total counts
- Tooltips show docs plus top symbols; focus passport renders the symbol table with docs, neighbor lists, and counts
- Draggable nodes with barnesHut physics, stabilization, freeze toggle, PNG snapshot and typed JSON export
- Reuses reader contracts: search, focus, reach, route, lens, chapters, deep links, titled controls
- Live map links: hover card, click opens a link passport (sentence, endpoints, mutual dependency, community bridge, role crossing, other links between the pair, Fit, Both neighbourhoods), #edge=from~to deep link, Esc clears
- Both map renderers fill placeholders with _fill_template in one pass, so payload text naming a placeholder stays literal
- Every toolbar and dialog action carries a human-readable title plus a visible reading guide and a gallery how-to section
- Deep links restore #focus=id, #focus=id&reach=upstream|downstream, #route=a~b, #lens=role, #view=id
- Motion is finite, honors prefers-reduced-motion, and never enters canonical exports
- All labels HTML-escaped in Python and script payloads unicode-escaped for angle brackets
- DocsSitePublisher class with publish(maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries) entry point
- Publishes maps/<kind>.html plus a gallery index.html and a .nojekyll marker into DIAGRAM_PAGES_DIR
- Gallery index: project header with stats, one card per validated map with counts and descriptions, filter input, theme toggle, how-to-read section, relative links only, zero external fetches (the only `https://` hrefs allowed are the footer SITE_GITHUB_URL + SITE_PYPI_URL project links)
- Gallery footer: offline notice + llms.txt agent pointer + footer-links nav with GitHub (inline SVG mark, blue-to-cyan gradient `#38bdf8`->`#22d3ee` matching `--accent`) and PyPI pills (target _blank, rel noopener, escaped Config URLs)
- Gallery redesign: hero with counter tiles (files, symbols, imports by relation only, languages, communities; count-up always lands on the real value), Start here path (wiki index, video, KB, agent INDEX), sticky filter toolbar (`/` focuses, live match count), map cards with per-kind inline SVG glyphs and hover flow animation, whole-card links
- Video player gets a poster frame (SITE_VIDEO_POSTER_FILENAME extracted by ffmpeg at SITE_VIDEO_POSTER_AT_S, refreshed only when the video is newer; skipped without ffmpeg)
- Docs grouped Wiki / Project / Agent / Recipes, entry points first; paged NAME_pN.md collapse into one card with page chips; cards show the document H1 title, a prose preview (markdown syntax stripped), line count, and approximate tokens
- Docs open in a slide-over drawer (Esc/scrim closes, focus restored, #doc= deep links); relative .md links inside a rendered doc open in the drawer
- No entrance animations that can leave content hidden; all motion disabled under prefers-reduced-motion
- Gallery index embeds the overview video with an HTML5 <video controls> tag (SITE_VIDEO_FILENAME) and a documentation grid with offline markdown2html viewer (colored code, tables, deep link #doc=name)
- publish_assets(project_root, output_dir) copies VIDEO_OUTPUT into the site root and KNOWLEDGE_BASE/README/agent/wiki markdown into SITE_DOCS_SUBDIR (capped by SITE_MAX_DOCS); collect_doc_sources() is deterministic and sorted
- export_pages/export_diagrams pass project_root so `pages` and `diagrams` outputs always ship video + docs without extra flags
- Gallery cards report primary scope honestly ("N of M files"); maps embed the project total in their passport header
- Published maps carry a Gallery home link via the optional meta home target (omitted for standalone exports)
- Invalid maps are skipped while the index is still written; empty input yields an empty gallery notice
- Publish never mutates caller supplied map metadata
- CLI: `pages` publishes the static site (GitHub Pages ready: serve the output directory directly)
- publish() writes llms.txt (SITE_LLMS_TXT_FILENAME) at the site root: H1, blockquote summary, Wiki then Agent Docs then Project Docs link sections (entry points first), maps under Optional
- run()/rebuild() refresh the site only when DIAGRAM_PAGES_DIR already holds a readmenator gallery (index.html + maps dir) and SITE_REFRESH_ON_REBUILD is set; a user's own docs folder is never taken over
- CLI: `diagrams` exports all five maps, `diagram <kind>` exports one map
- AnalyzerFactory exposes diagram_builder, diagram_renderer, diagram_validator, vis_renderer (lazy init)
- Configurable via DIAGRAM_ENABLED, DIAGRAM_OUTPUT_DIR, and all DIAGRAM_* geometry/scope/style settings
- Full mode (`DIAGRAM_FULL_MODE=True` or `diagrams --full` / `diagram <kind> --full` / `pages --full`): zero exclusions, every scanned file in every map, grown per-map canvas, size-limit checks D004/D008 skipped, gallery cards report "full scope"
- `run`/`rebuild` always export full maps (`export_diagrams(full=True)`), so default `KNOWLEDGE_BASE.md` regeneration never ships truncated doom-only diagrams
- `run`/`rebuild` render the video before exporting maps and refreshing the site, so every published gallery embeds the video of the same run

### GitHub Wiki Publisher Contract
- GitHubWikiPublisher class with render(project_root, remote) and publish(project_root, dry_run) entry points (readmenator/_gh_wiki.py)
- Sources: KNOWLEDGE_BASE.md (GH_WIKI_INCLUDE_KB), readmenator-wiki/*.md, readmenator-agent/**/*.md; regular non-symlink files only
- Flat page names: wiki index -> Home, KB -> Knowledge-Base, agent docs -> Agent-<stem>, recipes -> Recipe-<stem>; plus generated _Sidebar.md (Start, Wiki, Agent Docs, Recipes) and _Footer.md (source commit)
- Relative `.md` links rewritten to page names; backticked existing project paths (optional `:line`) become commit-pinned blob permalinks (GH_WIKI_PERMALINKS); paths outside the project root are never linked
- Remote: GH_WIKI_REMOTE (validated) else `gh repo view` URL else `git remote get-url origin`, mapped to `<repo>.wiki.git`
- Publish: shallow clone into a temp dir, write pages, delete only pages listed in GH_WIKI_STATE_FILE from the previous run (hand-written pages kept), commit and push only when `git status` shows changes; temp dir always removed
- Uninitialized wiki (clone fails) yields an actionable message: create the first page once in the web UI
- Commands run as argument lists with GH_WIKI_TIMEOUT_S, never through a shell; runner injectable for tests
- Default on: GH_WIKI_ENABLED defaults True; run()/`--rebuild` publish automatically when the root is a git checkout (skipped otherwise, failures logged, never fatal); CLI `readmenator . gh-wiki`, `readmenator . gh-wiki --dry-run` (renders into GH_WIKI_DRY_RUN_DIR, no git calls)
- AnalyzerFactory exposes gh_wiki (lazy init); app.publish_github_wiki(target, dry_run) returns WikiPublishResult

### Cinematic Video Contract
- CinematicVideoRenderer class with collect() + build_scenes() + render() entry points (readmenator/_video.py)
- General-purpose synthwave overview: same neon HUD / sun / grid / bloom / scanline / glitch language as the miniGCC self-host video, driven by real scan data (never staged numbers)
- Twelve acts: title (counting stats + language chips), I layers, II god nodes (formula exposed + real source preview), III true dependency tree (BFS from hub, focus-file symbols), IV communities (hub, cohesion bar, inside/crossing imports, key symbols), V Emergence (ForceAtlas2 LinLog convergence animated from snapshots, PageRank sizing, random-surfer particles on top-PageRank edges, PageRank telemetry), VI Orbit (3D ForceAtlas2 layout through an orbiting perspective camera: assemble, color-mode montage community/layer/language, eased camera tour over the VIDEO_ORBIT_TOUR_STOPS largest communities with cohesion and seams, 1-hop reach of the top hub with particles, explorer-style side panel and graph-force path), VII The Wiring (hierarchical edge bundling by community, community spotlight sweep, flow ranking), VIII The Sphere (3D layout morphs onto spherical community caps, bundled curves grow, rotation, spotlight sweep with crossing particles, graph-bundle path), IX code DNA (sha256 color per file, scan sweep, hub zoom) + security side panel, X The Tiers (tier-by-tier architecture assembly, upward imports flashing red with a fix-first list), XI Execution (camera follows the entry call tree in call order with a travelling packet and a callee doc panel), XII The Organism (git release timeline played as a growing organism: every release snapshot materialises its files and import edges, the unborn shape waits as a ghost, a landing release pulses from its hub, the finished organism folds onto a globe of communities), invite scene (both explorers spinning with their paths), outro telemetry; layouts precomputed before forking frame workers; 3D panels clipped to their box
- An act with duration <= 0 is skipped together with its card; VIDEO_INVITE_S <= 0 drops the invite
- Motion: ease() is quintic smootherstep (C2); scenes crossfade from the previous scene's last frame over VIDEO_TRANSITION_S (glitch scaled by VIDEO_TRANSITION_GLITCH); VIDEO_MOTION_BLUR_ACTS average VIDEO_MOTION_BLUR_SAMPLES shutter sub-frames
- Deterministic: content-hashed DNA colors, seed-7 graph layout, networkx spring layout with circular fallback when networkx is missing
- No truncation of reality: act III is the full blast-radius tree (every file that transitively imports the hub, BFS over dependents, VIDEO_TREE_MAX_NODES 0 = all) in a radial layout (one ring per depth, sectors by leaf count); act V graph shows every file and every resolved import (VIDEO_MAX_GRAPH_NODES 0 = all), spring layout on connected files with isolated files in a bottom strip; act VI DNA grid sizes cells so every file fits (VIDEO_DNA_MAX_CELL)
- Labels never overlap: tree labels placed greedily by depth and skipped only when they would collide (nodes are always drawn); labels truncated to VIDEO_MAX_LABEL_CHARS
- Fit by construction: all panels/boxes derived from VIDEO_WIDTH/HEIGHT
- Optional dependency: dependencies_available() checks PIL + ffmpeg; run()/rebuild() skip with a warning when missing, never fail the KB pipeline
- AnalyzerFactory exposes video (lazy init); app.export_video(target) renders standalone, run()/rebuild() auto-render to VIDEO_OUTPUT unless VIDEO_ENABLED=False
- CLI: `video` renders the mp4, `--video` forces it, `--no-video` skips it (including on the `--rebuild` path)
- Configurable via VIDEO_ENABLED, VIDEO_OUTPUT, VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS, VIDEO_CRF, VIDEO_JOBS, per-act VIDEO_*_S durations, VIDEO_MAX_GRAPH_NODES, VIDEO_MAX_LABEL_CHARS, VIDEO_MUSIC_PATH

### Git History Contract
- GitHistoryReader class with available() + timeline() entry points (readmenator/_githistory.py)
- Read-only: git plumbing only (rev-list, for-each-ref, rev-parse, log, ls-tree, cat-file --batch), explicit argument lists, never a shell, bounded by VIDEO_HISTORY_TIMEOUT_S, sanitised environment (no inherited GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE), no network
- Timeline order: first commit (named after its tag when it carries one, otherwise "genesis"), then every tag by creation date, then HEAD when it is ahead of the last tag; one snapshot per commit
- Each snapshot materialises the tracked tree at that commit, parses it with the same PolyglotScanner (shared _parse_source path), and resolves project-internal imports with ImportResolver
- Generated outputs, unsupported extensions, oversized files and too deep paths are skipped; budgets VIDEO_HISTORY_MAX_SNAPSHOTS (evenly spaced sample between the first and the last release) and VIDEO_HISTORY_MAX_FILES apply
- Repositories without git, without tags, or without a reachable history produce an empty timeline; the act is skipped instead of failing
- Wired into the growth act: collect(project_root=...) fills data["growth"], which lays out the union graph once (nodes and edges carry birth indices), materialises each release with a birth window, keeps unborn files as ghosts (VIDEO_GROWTH_GHOST) and pulses the hub of the landing release (VIDEO_GROWTH_PULSES)

## Design Principles

### DRY
- Config is the single source of truth for all constants
- Symbol creation logic is not duplicated across parsers
- Docstring extraction lives once in LanguageParser base class
- File-level doc extraction lives once in PolyglotScanner
- All analysis thresholds in Config, never hardcoded

### SOLID
- Single Responsibility: each module has one job
- Open/Closed: add parsers/analyzers without modifying existing code
- Liskov Substitution: all parsers inherit from LanguageParser
- Interface Segregation: each contract exposes minimal surface
- Dependency Inversion: app depends on abstractions (Config, Scanner)

### Security
- No absolute paths in source code
- No network calls from the core scanner
- Symlinks rejected
- File size limits enforced
- Directory depth limits enforced
- All parsing exceptions caught
- No external API calls in any analysis or export module
- Pattern-based security analyzer with 18 language rule sets
- Privacy mode strips source snippets from output

### Structured Output
- All progress/report messages use `logging.getLogger(__name__)` (never `print()`)
- User-facing output (query results, summaries) uses `print()` to stdout
- Logging format configured in `__main__.py` via `logging.basicConfig`
- Each module gets its own logger via `logger = logging.getLogger(__name__)`

### Testing (SDD + TDD + BDD)
- Tests named as `test_<contract>_<behavior>` (BDD style)
- Each module has its own test class
- Security behaviors tested explicitly
- Edge cases tested (empty files, syntax errors, symlinks)
- Integration tests validate end-to-end pipeline
- "Classs" regression test prevents re-introduction
- All new modules have complete contract test suites
- Mutation check after SDD+TDD+BDD: introduce one-line mutants (validation bypass, escaping bypass, ordering change); a killed mutant fails at least one test, a surviving mutant requires a stronger test before refactor
- Property-based parser tests skip cleanly when hypothesis is not installed (inert strategy placeholders, identity decorators)

### Definition of Done (code)
- English only, no emojis, no prose comments, docstrings on every public and private function
- DRY and SOLID, one self-contained file per contract, production code with no placeholders or simplifications
- No hardcoded tuneables or magic numbers: every setting lives in Config
- No absolute paths, no network calls from analysis or export modules, all untrusted text escaped at the boundary
- Boy scout: any technical debt or security flaw found during the change is fixed without losing functionality

## Boy Scout Rules

When modifying this codebase:
1. Fix any security issues found (symlinks, path traversal, size limits)
2. Remove hardcoded values and move to Config if they are tuneable
3. Update tests to cover new behaviors
4. Keep the "Classs" pluralization fix intact
5. Do not add absolute paths
6. Do not add external dependencies to the core scanner
7. Maintain backward compatibility of the CLI interface
8. Update this CLAUDE.md and README.md for any contract changes
9. Fix inline imports (move to top of file)
10. Add type annotations to all function signatures

<!-- readmenator-agent-kb-link -->
## Project Knowledge Base (MUST read before coding)

Generated offline by [ReadMenator](https://github.com/grisuno/ReadMenator) (zero-token static analysis). Humans: `KNOWLEDGE_BASE.md`.

0. Memory: `cat readmenator-agent/MEMORY.md` (business rules, workflow, constraints, style, done criteria, session log). Record new decisions with `readmenator . remember "<note>" --kind decision`.
1. Freshness: `readmenator . fresh` (exit 1 means stale: run `readmenator . --rebuild`). Without the CLI, compare `git_commit` in `readmenator-agent/MANIFEST.json` with `git log -1`.
2. Orient: `ls *.md readmenator-agent/ readmenator-wiki/`, then read `readmenator-wiki/index.md` (big picture, communities, god nodes).
3. Locate: `grep -n '<keyword>' readmenator-agent/INDEX*.md readmenator-agent/SYMBOLS*.md` before any `glob` over sources; for questions use `readmenator . ask "<question>"` (GraphRAG, `--global` for overviews).
4. Context: `cat readmenator-agent/KB_<subsystem>.md` for the subsystem you touch.
5. Before editing: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md` (blast radius, cycles, findings).

Also: `API*.md` (public functions, one line each), `ARCHITECTURE*.md` (dependency pairs), `recipes/*.md` (grounded task steps). Large docs are paged as `NAME_p2.md`, so always grep with `NAME*.md`.

    pip install readmenator && readmenator . --rebuild
<!-- /readmenator-agent-kb-link -->
