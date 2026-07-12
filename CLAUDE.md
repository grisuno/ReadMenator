# ReadMenator Development Contract

## Project Structure

```
readmenator/
  __init__.py       - Public API exports
  __main__.py       - CLI entry point with argument dispatch
  _config.py        - Immutable Config dataclass (all settings, no magic numbers)
  _models.py        - Symbol, Node, Edge, AnalysisResult, CommunityResult data types
  _parsers.py       - 13 language parsers (Strategy pattern) + ParserFactory
  _scanner.py       - Secure directory traversal and file analysis
  _resolver.py      - Import path resolver (raw import strings -> project file paths)
  _mermaid.py       - Mermaid graph renderer with community subgraphs and internal edges
  _documentation.py - KNOWLEDGE_BASE.md generator with TOC, dashboard, communities
  _query.py         - QueryEngine: query, explain, bidirectional path dependency tracing
  _analyzer.py      - Graph analysis: communities, god nodes, surprising connections
  _cache.py         - SHA256 content hash cache for incremental updates
  _exporter.py      - Multi-format export: JSON, interactive HTML (vis.js), static SVG
  _app.py           - Application orchestrator with import resolution and analysis
tests/
  test_config.py    - Config contract tests
  test_models.py    - Data model contract tests
  test_parsers.py   - 13 parser contract tests (SDD+TDD+BDD)
  test_scanner.py   - Scanner security and behavior tests
  test_resolver.py  - Import resolver contract tests
  test_mermaid.py   - Mermaid rendering contract tests
  test_documentation.py - Documentation output contract tests
  test_query.py     - Query engine contract tests
  test_analyzer.py  - Graph analysis contract tests
  test_cache.py     - File cache contract tests
  test_exporter.py  - Graph exporter contract tests
  test_integration.py - End-to-end pipeline tests
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
- Progress reporting batch size (PROGRESS_REPORT_BATCH)

### Models Contract
- Symbol: name, kind (not `type`), line, doc, signature
- Node: node_id, label, kind, language, doc, symbols
- Edge: source, target, relation, confidence
- pluralize_symbol_kind: returns correct plural form
- CommunityResult: community_id, label, file_ids, cohesion, size
- AnalysisResult: god_nodes, communities, surprising_connections, suggested_questions

### Parsers Contract
- LanguageParser base with _extract_docstring and _extract_signature
- 13 parser subclasses, one per language
- Python uses native ast module; all others use regex
- ParserFactory maps extension to parser class
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
- Table of Contents with section links
- Statistics Dashboard (file counts, import fan-in/fan-out, language breakdown)
- God Nodes section (most central files ranked by connectivity)
- Community Analysis section (import-based groups with cohesion scores)
- Surprising Connections section (cross-community indirect bridges)
- Suggested Questions section (auto-generated exploration prompts)
- Mermaid graph in fenced code block with community subgraphs
- Architecture Reference grouped by language
- Each file lists its symbols by kind with correct pluralization
- File-level docstring displayed per file
- Cross-reference: "Imported by" links for each file
- "Classes" not "Classs" (regression guard)
- Truncation note when MERMAID_MAX_NODES exceeded

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

### File Cache Contract
- SHA256-based content hashing
- Persistence to JSON file in CACHE_DIR
- Change detection (find_changed)
- Stale entry pruning (prune_deleted)
- Batch hash computation (compute_hashes)
- Save/load roundtrip

### Graph Exporter Contract
- to_json: GraphRAG-ready node-link JSON with optional analysis metadata
- to_html: Standalone interactive page using vis.js (CDN, no server needed)
- to_svg: Static SVG with spring-layout, truncation for large graphs
- Community-based node coloring in HTML and SVG
- Search/filter UI in HTML export
- All formats embed analysis metadata when available

## Design Principles

### DRY
- Config is the single source of truth for all constants
- Symbol creation logic is not duplicated across parsers
- Docstring extraction lives once in LanguageParser base class
- File-level doc extraction lives once in PolyglotScanner

### SOLID
- Single Responsibility: each module has one job
- Open/Closed: add parsers without modifying existing code
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

### Testing (SDD + TDD + BDD)
- Tests named as `test_<contract>_<behavior>` (BDD style)
- Each module has its own test class
- Security behaviors tested explicitly
- Edge cases tested (empty files, syntax errors, symlinks)
- Integration tests validate end-to-end pipeline
- "Classs" regression test prevents re-introduction

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
