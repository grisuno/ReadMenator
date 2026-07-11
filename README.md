# ReadMenator

A token-free, offline, production-grade polyglot codebase knowledge graph generator.

**No LLMs. No tokens. No cloud costs.** Pure static analysis via AST + regex.

Stop uploading proprietary code to the cloud just to understand it. ReadMenator builds production-grade codebase knowledge graphs 100% offline—with zero LLMs, zero token costs, and absolute data privacy.

## Supported Languages (13)

C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly.

Accelerate developer onboarding without compromising your security. ReadMenator uses pure static analysis to map architectures and trace dependencies locally, giving you a complete codebase knowledge base for free.

Tired of burning LLM tokens to navigate legacy code? ReadMenator generates full Mermaid dependency graphs and answers architectural queries right from your terminal, completely offline and with zero cloud costs.

## [Installation](https://pypi.org/project/readmenator/)

```bash
pip install readmenator 
```

or install from path

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

- [https://pypi.org/project/readmenator/](https://pypi.org/project/readmenator/)

## License

AGPL-3.0
