# ReadMenator

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/8d146d5d-8e35-45c9-a119-fa154d03446b" />


A token-free, offline, production-grade polyglot codebase knowledge graph & architectural analyzer.

**No LLMs. No tokens. No cloud costs.** Pure static analysis via AST + regex.

ReadMenator builds production-grade codebase knowledge graphs and architectural health reports 100% offline. Identify structural risks, security flaws, and change impact patterns instantly across 19 languages.

- [https://pypi.org/project/readmenator/](https://pypi.org/project/readmenator/)

## Supported Languages (19)

C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly, Ruby, Swift, Kotlin, Scala, Lua, Elixir.

## What ReadMenator Does Better Than Graphify

| Feature | graphify | readmenator |
|---------|----------|-------------|
| Extraction | LLM agents (tokens) | AST + regex (free) |
| Languages | Any (LLM reads anything) | 19 static parsers |
| Call graph edges | No | Yes (intra-file calls) |
| Inheritance edges | No | Yes (class, interface) |
| Architectural layers | No | Yes (5-layer detection) |
| Community detection | Leiden/Louvain | Label propagation |
| God nodes | Yes | Yes |
| Surprising connections | Yes | Yes |
| Suggested questions | Yes | Yes |
| Edge types | 1 (imports) | 4 (imports, calls, inherits, resolved_imports) |
| Export formats | JSON, HTML, SVG, GraphML, Obsidian, Cypher/Neo4j | JSON, HTML, SVG, GraphML, Obsidian |
| Watch mode | Yes | Yes (polling) |
| Incremental updates | Cache-based | SHA256 cache |
| Confidence-tagged edges | EXTRACTED/INFERRED/AMBIGUOUS | EXTRACTED |
| Cost | Token-based | Zero |
| Speed | Minutes | Seconds |

## Installation

```bash
pip install readmenator 
```

or install from path

```bash
pip install .
```

## Usage

### Generate knowledge base

```bash
python -m readmenator /path/to/project --rebuild
```

Creates `KNOWLEDGE_BASE.md` with Table of Contents, Statistics Dashboard, Architectural Layers, God Nodes, Community Analysis, Surprising Connections, Suggested Questions, **UML Class Diagram**, Mermaid graph (internal edges + community subgraphs), and Architecture Reference. A link to the knowledge base is automatically injected into the project's README.md.

### Export formats

```bash
python -m readmenator /path/to/project --export-all     # JSON + HTML + SVG
python -m readmenator /path/to/project --json           # graph.json (GraphRAG-ready)
python -m readmenator /path/to/project --html           # graph.html (interactive vis.js)
python -m readmenator /path/to/project --svg            # graph.svg (static)
python -m readmenator /path/to/project --graphml        # graph.graphml (Gephi/yEd)
python -m readmenator /path/to/project obsidian         # Obsidian vault (wikilinks)
python3 readmenator.py <path> lint                      # Architecture violations (exit 1 on errors)
python3 readmenator.py <path> strip-dead-code           # Orphaned symbol report
python3 readmenator.py <path> generate-rules            # Generate .cursorrules file
python3 readmenator.py <path> refactor-monolith         # Refactoring plans + executable scripts
```

### Query, explain, and path trace

```bash
python -m readmenator /path/to/project query "What classes handle HTTP?"
python -m readmenator /path/to/project explain Database
python -m readmenator /path/to/project path SymbolA SymbolB
```

### Analysis

```bash
python -m readmenator /path/to/project analyze          # community + god nodes + questions
python -m readmenator /path/to/project layers           # architectural layer detection
```

## Advanced Architectural Insights (Out of the Box)

ReadMenator goes beyond simple visualization. It runs complex graph algorithms locally to give you deep insights into your code's health:

*   **Change Impact Analysis:** Know exactly which files are highly coupled. ReadMenator calculates direct and transitive dependents so you can predict what will break before you refactor.
*   **Hotspot Detection:** Automatically ranks files by combining cognitive complexity (symbol richness) and graph centrality to pinpoint technical debt.
*   **Taint Propagation Mapping:** Traces how risky imports (like `subprocess` or OS-level sinks) propagate transitively through your codebase dependency graph.
*   **Community & Layer Detection:** Automatically groups files into structural layers (utility, business logic, infrastructure) and highly cohesive communities using label propagation.

### Automation

```bash
python -m readmenator /path/to/project update           # incremental (SHA256 cache)
python -m readmenator /path/to/project watch            # auto-rebuild on file changes
python -m readmenator /path/to/project analyze          # Analyze the proyect
```

### Run tests

```bash
python -m readmenator --test
```

### UML Class Diagram

ReadMenator auto-generates Mermaid `classDiagram` from parsed class-level symbols across all
supported languages. UML diagrams are embedded in `KNOWLEDGE_BASE.md` by default.

```bash
python -m readmenator /path/to/project uml              # Print UML class diagram
```

### Generate Class Stubs in Other Languages

Translate extracted class structures into target language declarations:

```bash
python -m readmenator /path/to/project --c++            # C++ class declarations
python -m readmenator /path/to/project --java           # Java class declarations
python -m readmenator /path/to/project --csharp         # C# class declarations
python -m readmenator /path/to/project --kotlin         # Kotlin class declarations
python -m readmenator /path/to/project --scala          # Scala class declarations
python -m readmenator /path/to/project --swift-classes  # Swift type declarations
python -m readmenator /path/to/project --dart-classes   # Dart class declarations
python -m readmenator /path/to/project --ruby-classes   # Ruby class declarations
python -m readmenator /path/to/project --go-classes     # Go type declarations
python -m readmenator /path/to/project --rust-classes   # Rust type declarations
python -m readmenator /path/to/project --php-classes    # PHP class declarations
python -m readmenator /path/to/project --python-classes # Python class declarations
```

Supported target languages (12): C++, Java, C#, Python, Go, Rust, PHP, Kotlin, Scala, Swift, Dart, Ruby.

## Architecture

| Contract | File | Responsibility |
|----------|------|----------------|
| Config | `_config.py` | Immutable centralized configuration |
| Models | `_models.py` | Symbol, Node, Edge, AnalysisResult |
| Parsers | `parsers/` package | 19 language parsers + factory (Strategy pattern) |
| Scanner | `_scanner.py` | Secure directory walking, file-level docs, progress |
| Resolver | `_resolver.py` | Import path resolution |
| Mermaid | `_mermaid.py` | Mermaid graph with internal edges and community subgraphs |
| UML Generator | `_uml.py` | Mermaid class diagrams + 12-language code generation |
| Documentation | `_documentation.py` | KNOWLEDGE_BASE.md with TOC, dashboard, layers, analysis, UML |
| Query | `_query.py` | Query/explain/path engine with bidirectional path finding |
| Analyzer | `_analyzer.py` | Communities, god nodes, surprising connections, questions |
| Cache | `_cache.py` | SHA256 content cache for incremental updates |
| Exporter | `_exporter.py` | JSON, HTML (vis.js), SVG, GraphML, Obsidian |
| Layers | `_layers.py` | Architectural layer detection (5-layer model) |
| Watcher | `_watcher.py` | Filesystem polling watcher for auto-rebuild |
| README Injector | `_readme_injector.py` | Auto-injects KB link into project README |
| Application | `_app.py` | Application orchestrator |
| CLI | `__main__.py` | CLI entry point and argument dispatch |

## Security

- Symlinks rejected
- File size capped at 10 MB
- Directory depth limited to 20
- No absolute paths in source code
- No external network calls in any module
- All exceptions silently caught during parsing

## License

<img width="300" height="124" alt="image" src="https://github.com/user-attachments/assets/e25f889b-aae5-4e53-a397-284ca1988825" />

AGPL-3.0

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. A comprehensive knowledge base is available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.

AI agents and developers: Read `KNOWLEDGE_BASE.md` for full project context
without LLM token cost.
<!-- /readmenator-kb-link -->

