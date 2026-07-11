# ReadMenator

A token-free, offline, production-grade polyglot codebase knowledge graph generator.

**No LLMs. No tokens. No cloud costs.** Pure static analysis via AST + regex.

## Supported Languages (13)

C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly.

## Installation

```bash
pip install .
```

Or run directly:

```bash
python -m readmenator /path/to/project
```

## Usage

### Generate knowledge base

```bash
python -m readmenator /path/to/project
```

Creates `KNOWLEDGE_BASE.md` in the project root with a Mermaid dependency graph and full architecture reference.

### Force regeneration

```bash
python -m readmenator /path/to/project --rebuild
```

### Query the knowledge base

```bash
python -m readmenator /path/to/project query "What classes handle HTTP?"
```

### Explain a symbol

```bash
python -m readmenator /path/to/project explain Database
```

### Trace dependency path

```bash
python -m readmenator /path/to/project path SymbolA SymbolB
```

### Show summary

```bash
python -m readmenator /path/to/project summary
```

### Run tests

```bash
python -m readmenator --test
```

## Backward Compatibility

The existing `readmenator.py` wrapper preserves the original CLI interface:

```bash
python readmenator.py /path/to/project
python readmenator.py --test
```

## Architecture

ReadMenator follows a contract-based design with strict separation of concerns:

| Contract | File | Responsibility |
|----------|------|----------------|
| Config | `_config.py` | Immutable centralized configuration |
| Models | `_models.py` | Symbol, Node, Edge data types |
| Parsers | `_parsers.py` | 13 language parsers + factory (Strategy pattern) |
| Scanner | `_scanner.py` | Secure directory walking and file processing |
| Mermaid | `_mermaid.py` | Mermaid graph rendering |
| Documentation | `_documentation.py` | KNOWLEDGE_BASE.md generation |
| Query | `_query.py` | Interactive query/explain/path engine |
| Application | `_app.py` | Application orchestrator |
| CLI | `__main__.py` | CLI entry point and argument dispatch |

## Security

- Symlinks are rejected
- File size capped at 10 MB
- Directory depth limited to 20
- Binary/unreadable files are silently skipped
- No absolute paths in code; no external network calls
- All exceptions during parsing are caught

## Self-Documentation

This repository is documented using ReadMenator itself. See [KNOWLEDGE_BASE.md](KNOWLEDGE_BASE.md) -- the tool analyzing its own codebase.

## License

AGPL-3.0
