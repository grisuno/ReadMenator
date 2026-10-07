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
  test_readme_injector.py - README injection contract tests
  test_agent_output.py - Agent output generator contract tests (subsystems, grep-friendly, injection)
  test_wiki.py - Agent wiki contract tests (index, community pages, connections, orphans, lint, privacy)
  test_dataflow.py - Dataflow analyzer contract tests (def-use, alloc checks, C idioms, span bounds)
  test_agent_friendliness.py - Agent output budgets, purposes, MANIFEST freshness, noise reduction, llms.txt
  test_gh_wiki.py - GitHub wiki publisher contract tests (faked git/gh runner, no network)
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
- Video scope settings (VIDEO_MAX_GRAPH_NODES 0 = all, VIDEO_TREE_MAX_NODES 0 = all, VIDEO_TREE_RING_MARGIN, VIDEO_TREE_LABEL_GAP, VIDEO_TREE_CHAR_PX, VIDEO_GRAPH_TRIM_FRACTION, VIDEO_GRAPH_SPREAD, VIDEO_GRAPH_LOOSE_STRIP, VIDEO_DNA_MAX_CELL, VIDEO_MAX_LABEL_CHARS, VIDEO_MUSIC_PATH, VIDEO_PREVIEW_LINES)
- Agent budget settings (AGENT_OUTPUT_MAX_LINES, AGENT_PURPOSE_MAX_CHARS, AGENT_DOC_MAX_CHARS, AGENT_SIGNATURE_MAX_CHARS, AGENT_GOTCHAS_TOP_N, AGENT_GOTCHAS_EXCLUDE_LAYERS, AGENT_API_PUBLIC_ONLY, AGENT_API_EXCLUDE_LAYERS, AGENT_CHARS_PER_TOKEN, AGENT_ENTRYPOINT_FILENAMES)
- Generated artifact settings (GENERATED_FILE_PREFIXES, SKIP_GENERATED_OUTPUTS, REFACTORIZER_SCRIPT_PREFIX)
- Site agent settings (SITE_LLMS_TXT_ENABLED, SITE_LLMS_TXT_FILENAME, SITE_REFRESH_ON_REBUILD)
- GitHub wiki settings (GH_WIKI_ENABLED default True, GH_WIKI_REMOTE, GH_WIKI_GIT_REMOTE_NAME, GH_WIKI_HOME_PAGE, GH_WIKI_KB_PAGE, GH_WIKI_AGENT_PREFIX, GH_WIKI_RECIPE_PREFIX, GH_WIKI_INCLUDE_KB, GH_WIKI_PERMALINKS, GH_WIKI_STATE_FILE, GH_WIKI_DRY_RUN_DIR, GH_WIKI_TIMEOUT_S, GH_WIKI_COMMIT_MESSAGE)

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
- Skips its own generated outputs (agent, wiki, rules, maps, site, cache, gh-wiki dry run dirs and `.refactor_*` scripts) via SKIP_GENERATED_OUTPUTS; counted as `generated` in last_skip_counts
- scan_with_content() returns content map for rule gen, taint analysis

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
- Mermaid graph in fenced code block with community subgraphs
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
- Provides: scanner, generator, analyzer, security, exporter, taint, hotspots, layer_rules, rule_gen, sarif, cpg, layer_detector, uml, wiki, readme_injector, video, gh_wiki
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
- Tools: summary, query, explain, path, findings, security_summary, taint, hotspots, cycles, communities, layers, layer_violations, rebuild, update, export_json
- Resources: readmenator://summary, readmenator://graph, readmenator://findings, readmenator://analysis, readmenator://kb
- Integrated with readmenatorApplication for all query/analysis operations
- Entry point: `python3 -m readmenator._mcp_server <path>` or `readmenator-mcp <path>`

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
- Injects a section linking to KNOWLEDGE_BASE.md and agent output directory with HTML anchor comments
- Injected section also links readmenator-wiki/ (index.md entry point, community pages, REPORT.md)
- Idempotent: second injection returns False when injection text is identical
- **Outdated detection**: when anchor exists but text differs from current template, removes old and injects new
- Preserves existing README content
- Markdown injection: link, description, AI/human context
- reStructuredText injection: adapted RST syntax
- Uses configurable kb_filename and agent_output_dir parameters
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
- Respects LAYER_VIOLATION_STRICT_MODE for warning edges
- Returns List[LinterViolation] sorted by severity (error > warning > info)
- Configurable via LINTER_ENABLED and LINTER_CROSS_LAYER_VIOLATIONS flags

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
- Live maps color nodes by code community (legend with counts, click isolates, #community=id deep link, C toggles to role colors), size dots by link count, always label the DIAGRAM_VIS_LABEL_TOP_N most connected files and reveal the rest on zoom, dim edges that light up on hover/selection, forceAtlas2Based physics from DIAGRAM_VIS_* settings
- Layer roles are honest: utility -> core, testing -> test (never "external" for project files)
- Default export format for `diagrams`, `diagram`, and `pages` (CDN bundle URLs from Config, pages need network access)
- Map nodes carry documentation payloads: file doc, language, symbol records with signatures, total counts
- Tooltips show docs plus top symbols; focus passport renders the symbol table with docs, neighbor lists, and counts
- Draggable nodes with barnesHut physics, stabilization, freeze toggle, PNG snapshot and typed JSON export
- Reuses reader contracts: search, focus, reach, route, lens, chapters, deep links, titled controls
- Every toolbar and dialog action carries a human-readable title plus a visible reading guide and a gallery how-to section
- Deep links restore #focus=id, #focus=id&reach=upstream|downstream, #route=a~b, #lens=role, #view=id
- Motion is finite, honors prefers-reduced-motion, and never enters canonical exports
- All labels HTML-escaped in Python and script payloads unicode-escaped for angle brackets
- DocsSitePublisher class with publish(maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries) entry point
- Publishes maps/<kind>.html plus a gallery index.html and a .nojekyll marker into DIAGRAM_PAGES_DIR
- Gallery index: project header with stats, one card per validated map with counts and descriptions, filter input, theme toggle, how-to-read section, relative links only, zero external requests
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
- Six acts: title (counting stats + language chips), I layers, II god nodes (formula exposed + real source preview), III true dependency tree (BFS from hub, focus-file symbols), IV communities (hub, cohesion bar, inside/crossing imports, key symbols), V resolved import graph with packets + hottest ranking, VI code DNA (sha256 color per file, scan sweep, hub zoom) + security side panel, outro telemetry
- Deterministic: content-hashed DNA colors, seed-7 graph layout, networkx spring layout with circular fallback when networkx is missing
- No truncation of reality: act III is the full blast-radius tree (every file that transitively imports the hub, BFS over dependents, VIDEO_TREE_MAX_NODES 0 = all) in a radial layout (one ring per depth, sectors by leaf count); act V graph shows every file and every resolved import (VIDEO_MAX_GRAPH_NODES 0 = all), spring layout on connected files with isolated files in a bottom strip; act VI DNA grid sizes cells so every file fits (VIDEO_DNA_MAX_CELL)
- Labels never overlap: tree labels placed greedily by depth and skipped only when they would collide (nodes are always drawn); labels truncated to VIDEO_MAX_LABEL_CHARS
- Fit by construction: all panels/boxes derived from VIDEO_WIDTH/HEIGHT
- Optional dependency: dependencies_available() checks PIL + ffmpeg; run()/rebuild() skip with a warning when missing, never fail the KB pipeline
- AnalyzerFactory exposes video (lazy init); app.export_video(target) renders standalone, run()/rebuild() auto-render to VIDEO_OUTPUT unless VIDEO_ENABLED=False
- CLI: `video` renders the mp4, `--video` forces it, `--no-video` skips it (including on the `--rebuild` path)
- Configurable via VIDEO_ENABLED, VIDEO_OUTPUT, VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS, VIDEO_CRF, VIDEO_JOBS, per-act VIDEO_*_S durations, VIDEO_MAX_GRAPH_NODES, VIDEO_MAX_LABEL_CHARS, VIDEO_MUSIC_PATH

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

1. Freshness: `readmenator . fresh` (exit 1 means stale: run `readmenator . --rebuild`). Without the CLI, compare `git_commit` in `readmenator-agent/MANIFEST.json` with `git log -1`.
2. Orient: `ls *.md readmenator-agent/ readmenator-wiki/`, then read `readmenator-wiki/index.md` (big picture, communities, god nodes).
3. Locate: `grep -n '<keyword>' readmenator-agent/INDEX*.md readmenator-agent/SYMBOLS*.md` before any `glob` over sources.
4. Context: `cat readmenator-agent/KB_<subsystem>.md` for the subsystem you touch.
5. Before editing: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md` (blast radius, cycles, findings).

Also: `API*.md` (public functions, one line each), `ARCHITECTURE*.md` (dependency pairs), `recipes/*.md` (grounded task steps). Large docs are paged as `NAME_p2.md`, so always grep with `NAME*.md`.

    pip install readmenator && readmenator . --rebuild
<!-- /readmenator-agent-kb-link -->
