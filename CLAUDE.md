# ReadMenator Development Contract

## Project Structure

```
readmenator/
  __init__.py       - Public API exports
  __main__.py       - CLI entry point with argument dispatch
  _config.py        - Immutable Config dataclass (all settings, no magic numbers)
  _models.py        - Symbol, Node, Edge data types + pluralize helper
  _parsers.py       - 13 language parsers (Strategy pattern) + ParserFactory
  _scanner.py       - Secure directory traversal and file analysis
  _mermaid.py       - Mermaid graph renderer with intelligent pruning
  _documentation.py - KNOWLEDGE_BASE.md generator
  _query.py         - QueryEngine: query, explain, path dependency tracing
  _app.py           - Application orchestrator
tests/
  test_config.py    - Config contract tests
  test_models.py    - Data model contract tests
  test_parsers.py   - 13 parser contract tests (SDD+TDD+BDD)
  test_scanner.py   - Scanner security and behavior tests
  test_mermaid.py   - Mermaid rendering contract tests
  test_documentation.py - Documentation output contract tests
  test_query.py     - Query engine contract tests
  test_integration.py - End-to-end pipeline tests
```

## Contracts

### Config Contract
- Immutable FrozenInstanceError on mutation
- No magic numbers or hardcoded paths
- All tuneable parameters in one place
- Pluralization map for symbol types

### Models Contract
- Symbol: name, kind (not `type`), line, doc, signature
- Node: node_id, label, kind, language, doc, symbols
- Edge: source, target, relation
- pluralize_symbol_kind: returns correct plural form

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

### Documentation Generator Contract
- Header: title + metadata line
- Mermaid graph in fenced code block
- Architecture Reference grouped by language
- Each file lists its symbols by kind with correct pluralization
- "Classes" not "Classs" (regression guard)
- Truncation note when MERMAID_MAX_NODES exceeded

### Query Engine Contract
- find_symbol(name): exact + fuzzy match
- explain(name): type, file, line, doc, signature, imports, siblings
- find_path(A, B): BFS shortest path through import graph
- query(text): search symbols and files for matching terms
- summary(): files, symbols, imports, top modules, key classes/functions

## Design Principles

### DRY
- Config is the single source of truth for all constants
- Symbol creation logic is not duplicated across parsers
- Docstring extraction lives once in LanguageParser base class

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

### Testing (SDD + TDD + BDD)
- Tests named as `test_<contract>_<behavior>` (BDD style)
- Each parser has its own test class
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
