# ReadMenator

A token-free, offline Polyglot Codebase Knowledge Graph generator.

**No LLMs. No tokens. No cloud costs.** Pure static analysis.

### Features

- Supports multiple languages: C, C++, Python, Go, Rust, JavaScript/TypeScript, Java, C#, Shell, PHP, and more.
- Generates structural knowledge graphs with Mermaid diagrams.
- Extracts classes, functions, imports, and relationships.
- Creates detailed architecture references with line numbers and descriptions.
- Works completely offline with zero token consumption.
- Designed as a lightweight alternative to Graphify.

### Usage

```bash
python3 readmenator.py
Usage:
  Generate docs:  python readmenator.py /path/to/project
  Run tests:      python readmenator.py --test

Supported languages:
  C/C++ (.c, .cpp, .h, .hpp)
  Python (.py)
  Go (.go)
  Rust (.rs)
  JavaScript/TypeScript (.js, .ts, .jsx, .tsx)
  Java (.java)
  C# (.cs)
  Shell (.sh, .bash, .zsh)
  PHP (.php)
  Dart (.dart)
  GDScript (.gd)
  Nim (.nim)
  Assembly (.asm, .s)

```

Or specify a directory:

```bash
python readmenator.py /path/to/your/project
```

The tool will generate a `KNOWLEDGE_BASE.md` file in the project root.

### Why ReadMenator?

While tools like Graphify depend on LLMs and consume large amounts of tokens, ReadMenator uses pure static analysis. It works reliably on small projects as well as large codebases without burning through your AI session limits.

### License

AGPL-3.0

---

¿Quieres que agregue alguna sección extra (instalación, configuración, comparación con Graphify, etc.)?

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)
