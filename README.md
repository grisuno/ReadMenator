# ReadMenator

A token-free, offline, production-grade polyglot codebase knowledge graph generator.

**No LLMs. No tokens. No cloud costs.** Pure static analysis via AST + regex.

Stop uploading proprietary code to the cloud just to understand it. ReadMenator builds production-grade codebase knowledge graphs 100% offline -- with zero LLMs, zero token costs, and absolute data privacy.

## Supported Languages (13)

C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly.

## New in v2.0: Graphify-style Intelligence Without Tokens

ReadMenator now provides the same structural analysis that graphify offers -- community detection, god node identification, surprising connection discovery, and suggested questions -- all without a single LLM call.

**What's new:**
- **Community detection** -- files grouped by import patterns (label propagation)
- **God nodes** -- most architecturally central files ranked by connectivity
- **Surprising connections** -- cross-community indirect bridges you didn't know about
- **Suggested questions** -- auto-generated exploration prompts from graph structure
- **Internal import edges** -- the Mermaid graph now shows how project files depend on each other, not just external deps
- **Statistics dashboard** -- fan-in/fan-out, symbol density, language breakdown
- **Table of contents** -- auto-generated navigable TOC
- **Cross-references** -- "imported by" links between files
- **File-level docs** -- header comments extracted as module docstrings
- **Import resolver** -- raw import strings mapped to actual project files
- **Bidirectional path finding** -- trace dependency chains in both directions
- **Graph exports** -- `graph.json` (GraphRAG-ready), `graph.html` (interactive vis.js), `graph.svg` (static)
- **Incremental updates** -- SHA256 cache skips unchanged files on re-scan

## Installation

```bash
pip install readmenator
```

Or run directly:

```bash
python -m readmenator /path/to/project
```

## Usage

### Generate knowledge base (with analysis)

```bash
python -m readmenator /path/to/project --rebuild
```

Creates `KNOWLEDGE_BASE.md` with:
- Table of Contents
- Statistics Dashboard
- God Nodes
- Community Analysis
- Surprising Connections
- Suggested Questions
- Mermaid dependency graph (with internal edges and community subgraphs)
- Architecture Reference (with cross-references and file-level docs)

### Export graphs

```bash
python -m readmenator /path/to/project --export-all     # JSON + HTML + SVG
python -m readmenator /path/to/project --json           # graph.json only
python -m readmenator /path/to/project --html           # graph.html only (interactive)
python -m readmenator /path/to/project --svg            # graph.svg only (static)
```

### Query the knowledge base

```bash
python -m readmenator /path/to/project query "What classes handle HTTP?"
```

### Explain a symbol

```bash
python -m readmenator /path/to/project explain Database
```

### Trace dependency path (bidirectional)

```bash
python -m readmenator /path/to/project path SymbolA SymbolB
```

### Run community analysis

```bash
python -m readmenator /path/to/project analyze
```

### Incremental update (cache-based)

```bash
python -m readmenator /path/to/project update
```

### Show summary

```bash
python -m readmenator /path/to/project summary
```

### Run tests

```bash
python -m readmenator --test
```

## Architecture

ReadMenator follows a contract-based design with strict separation of concerns:

| Contract | File | Responsibility |
|----------|------|----------------|
| Config | `_config.py` | Immutable centralized configuration |
| Models | `_models.py` | Symbol, Node, Edge, AnalysisResult data types |
| Parsers | `_parsers.py` | 13 language parsers + factory (Strategy pattern) |
| Scanner | `_scanner.py` | Secure directory walking and file processing |
| Resolver | `_resolver.py` | Import path resolution |
| Mermaid | `_mermaid.py` | Mermaid graph with internal edges and community subgraphs |
| Documentation | `_documentation.py` | KNOWLEDGE_BASE.md with TOC, dashboard, analysis |
| Query | `_query.py` | Query/explain/path engine with bidirectional path finding |
| Analyzer | `_analyzer.py` | Communities, god nodes, surprising connections, questions |
| Cache | `_cache.py` | SHA256 content cache for incremental updates |
| Exporter | `_exporter.py` | JSON, HTML (vis.js), SVG export |
| Application | `_app.py` | Application orchestrator |
| CLI | `__main__.py` | CLI entry point and argument dispatch |

## Security

- Symlinks are rejected
- File size capped at 10 MB
- Directory depth limited to 20
- Binary/unreadable files are silently skipped
- No absolute paths in code; no external network calls
- All exceptions during parsing are caught
- No LLM calls in any module

## Comparison: graphify vs readmenator

| Aspect | graphify | readmenator |
|--------|----------|-------------|
| Extraction | LLM agents (tokens) | AST + regex (free) |
| Output | graph.json + HTML + report | KNOWLEDGE_BASE.md + JSON + HTML + SVG |
| Languages | Any (LLM reads anything) | 13+ static parsers |
| Semantic edges | Yes (INFERRED, AMBIGUOUS) | No (structural only) |
| Community detection | Yes (Leiden/Louvain) | Yes (label propagation) |
| God node analysis | Yes | Yes |
| Surprising connections | Yes | Yes |
| Suggested questions | Yes | Yes |
| Interactive HTML | Yes (vis.js) | Yes (vis.js) |
| Cross-document inference | Yes | No (import chains only) |
| Import resolution | Yes | Yes |
| Incremental updates | Yes (cache-based) | Yes (SHA256 cache) |
| Speed | Minutes (LLM calls) | Seconds |
| Cost | Token-based | Zero |
| Regeneration | Full or incremental | Full (always fast) |

## Self-Documentation

This repository is documented using ReadMenator itself. See [KNOWLEDGE_BASE.md](KNOWLEDGE_BASE.md) -- the tool analyzing its own codebase.

## License

AGPL-3.0
