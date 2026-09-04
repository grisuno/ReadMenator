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
  _readme_injector.py - Auto-injects KNOWLEDGE_BASE.md link into project README
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
  test_readme_injector.py - README injection contract tests
```

## Contracts

### Config Contract
- Immutable FrozenInstanceError on mutation
- No magic numbers or hardcoded paths
- All tuneable parameters in one place
- Pluralization map for symbol types
- Graph analysis thresholds (COMMUNITY_MIN_SIZE, GOD_NODE_TOP_N, etc.)
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
- Reserved keywords filtered out (if, for, while, switch, catch)

### Scanner Contract
- Rejects symlinks for security
- Skips files > MAX_FILE_SIZE_MB
- Enforces MAX_DIRECTORY_DEPTH
- Ignores paths containing IGNORE_DIRS entries
- Only processes files with supported extensions
- Catches all exceptions silently during parsing
- Returns (List[Node], List[Edge])
- Extracts file-level docstrings from header comments
- Emits progress messages every PROGRESS_REPORT_BATCH files
- Supports `.gitignore`-aware scanning (GITIGNORE_AWARE)
- Supports privacy mode (PRIVACY_MODE) that strips snippets and docstrings
- scan_with_content() returns content map for rule gen, taint analysis

### Import Resolver Contract
- Maps raw import strings (Python dots, relative paths, bare module names) to project file paths
- Handles Python stdlib exclusion
- Handles relative imports (./ and ../)
- Handles dotted module paths (foo.bar.baz -> foo/bar/baz.py)
- Handles package __init__.py resolution
- Handles extensionless imports by trying known extensions
- Handles stem matching as fallback
- Works across all supported languages

### Mermaid Renderer Contract
- Renders internal import edges between project files (solid arrows)
- Renders community subgraphs when analysis results provided
- Maintains existing external import dashed edges
- Limits symbols per file to MERMAID_MAX_SYMBOLS_PER_FILE
- Returns (mermaid_source, is_truncated) tuple

### Documentation Generator Contract
- Header: title + metadata line
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
- Community detection via label propagation
- God node scoring via combined in/out degree + symbol weight
- Surprising connection discovery via cross-community path analysis
- Suggested question generation from graph structure
- Community cohesion scoring (internal / total edges)
- Community labeling from dominant directory

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
- Provides: scanner, generator, analyzer, security, exporter, taint, hotspots, layer_rules, rule_gen, sarif, cpg, layer_detector, uml, readme_injector
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
- Reuses scanner security checks (symlinks, ignore dirs, size/depth limits)
- No external API calls -- fully offline

### Layer Detection Contract
- detect(nodes, edges): maps each file to an architectural layer
- No Config dependency (static patterns only)
- 5-layer model: presentation, business_logic, data_access, infrastructure, testing
- Detection via path patterns, naming conventions, and imported frameworks
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
- Injects a section linking to KNOWLEDGE_BASE.md with HTML anchor comments
- Idempotent: second injection returns False when anchor already present
- Preserves existing README content
- Markdown injection: link, description, AI/human context
- reStructuredText injection: adapted RST syntax
- Uses configurable kb_filename parameter for custom KB paths
- Remove method strips injected section cleanly
- Returns False when no README found or no injection present
- Guided by README_INJECTION_ENABLED config flag

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
## Project Knowledge Base

This project contains a KNOWLEDGE_BASE.md generated by [ReadMenator](https://github.com/grisuno/ReadMenator), a zero-token polyglot static analysis tool.

If KNOWLEDGE_BASE.md does not exist or is outdated, regenerate it by running:

    pip install readmenator && readmenator .

Read KNOWLEDGE_BASE.md for full project context: architecture overview, all classes, functions, imports, dependency graphs, security audit findings, community analysis, and more. This file provides comprehensive codebase understanding without LLM token cost.
<!-- /readmenator-agent-kb-link -->
