---
name: readmenator
description: "Zero-token static analysis codebase context. Use KNOWLEDGE_BASE.md as source of truth -- no LLM extraction, no token cost. Pure AST + regex. Now with community detection, god nodes, surprising connections, and interactive HTML/SVG exports."
trigger: /readmenator
---

# /readmenator

Turn any codebase into a queryable knowledge base using pure static analysis. No LLMs. No tokens. No cloud. A single `KNOWLEDGE_BASE.md` file serves as the source of truth for all codebase questions.

Contrast with graphify: graphify costs tokens to extract entities and relationships via LLM agents. ReadMenator generates the same structural knowledge through deterministic AST/regex parsing -- zero tokens, instant, repeatable. Now with community detection, god node identification, surprising connection discovery, and suggested questions -- all the structural intelligence of graphify without the token cost.

## Usage

```
/readmenator                              # ensure KNOWLEDGE_BASE.md exists, then use as context
/readmenator <path>                       # target a specific directory
/readmenator --rebuild                    # force regeneration even if KNOWLEDGE_BASE.md exists
/readmenator query "<question>"           # answer a question using the knowledge base
/readmenator explain "<ClassName>"        # explain a specific symbol with its relationships
/readmenator path "<SymbolA>" "<SymbolB>" # trace the dependency chain between two symbols (bidirectional)
/readmenator update                       # incremental rebuild using SHA256 cache
/readmenator analyze                      # run community detection and graph analysis
/readmenator --export-all                 # export graph.json + graph.html + graph.svg
/readmenator --json                       # export graph.json (GraphRAG-ready)
/readmenator --html                       # export graph.html (interactive vis.js)
/readmenator --svg                        # export graph.svg (static)
/readmenator --no-analysis                # skip community detection (faster)
```

## What ReadMenator is for

ReadMenator solves a specific problem: every time you ask an AI about a codebase, it needs to read files to understand the structure. This burns tokens. With ReadMenator, you pre-compute the structural map once (statically, for free), then use that map as context for all subsequent questions.

What it gives you:
1. **A structural map** -- classes, functions, methods, imports, all with line numbers and docstrings, organized by file and language
2. **Mermaid graph** -- visual dependency diagram showing which files import what, which symbols belong to which modules, with internal import edges between project files and community subgraphs
3. **Community analysis** -- files grouped by import-based communities with cohesion scores
4. **God nodes** -- most architecturally central files ranked by connectivity
5. **Surprising connections** -- cross-community indirect bridges
6. **Suggested questions** -- auto-generated exploration prompts from graph structure
7. **Statistics dashboard** -- fan-in/fan-out, symbol density, language breakdown
8. **Multi-format exports** -- JSON (GraphRAG-ready), HTML (interactive vis.js), SVG (static)
9. **Zero ongoing cost** -- regenerate after code changes, always free

Supported languages (13+): C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly.

## What You Must Do When Invoked

If no path was given, use `.` (current directory). Do not ask the user for a path.

### Step 1 -- Ensure KNOWLEDGE_BASE.md exists

Check if `KNOWLEDGE_BASE.md` already exists in the target directory. If it does (and `--rebuild` was not given), skip to Step 2.

Otherwise, generate it:

```bash
python3 -m readmenator TARGET_PATH --rebuild
```

If installed via pip. Or if the script is available locally:

```bash
python3 readmenator.py TARGET_PATH
```

If `readmenator.py` is not in the current directory, find it. Common locations:

```bash
if [ -f "readmenator.py" ]; then
    READMENATOR_SCRIPT="readmenator.py"
else
    echo "readmenator.py not found. Install with: pip install readmenator"
    exit 1
fi
python3 "$READMENATOR_SCRIPT" TARGET_PATH
```

Replace `TARGET_PATH` with the actual path. If generation succeeds, print the summary (files, symbols, imports) shown in the script output.

If generation fails, tell the user and stop.

### Step 2 -- Read KNOWLEDGE_BASE.md as context

Read `TARGET_PATH/KNOWLEDGE_BASE.md`. This file now has a richer structure:

1. **Header** -- metadata (total files, symbols, imports, resolved imports)
2. **Table of Contents** -- links to all sections
3. **Statistics Dashboard** -- file counts, fan-in/fan-out, language breakdown
4. **God Nodes** -- most central files ranked by connectivity
5. **Community Analysis** -- import-based groups with cohesion scores
6. **Surprising Connections** -- cross-community indirect bridges
7. **Suggested Questions** -- auto-generated exploration prompts
8. **Structural Knowledge Map** -- a Mermaid graph (```mermaid ... ```) showing the file/import dependency diagram. Nodes are modules (rectangles), classes (green), and functions (yellow). External imports are dashed nodes. Internal imports between project files are solid arrows. Community subgraphs group related files.
9. **Architecture Reference** -- grouped by language, each file lists its symbols with cross-references ("Imported by" links) and file-level docstrings.

**Parse the Mermaid graph first** to understand the high-level structure (what depends on what). Then use the Architecture Reference to look up specific symbols when answering queries.

**IMPORTANT:** Do NOT read individual source files unless KNOWLEDGE_BASE.md lacks the information needed. The whole point is to avoid reading source files -- KNOWLEDGE_BASE.md IS the context.

### Step 3 -- Answer based on the knowledge base

#### For `/readmenator` (no subcommand)

After Step 1 and Step 2, present a summary:

```
Knowledge base loaded: N files, M symbols, K imports across L languages.

Top-level modules:
  - module_a.py (X symbols, imports: a, b, c)
  - module_b.py (Y symbols, imports: d, e)
  ...

Key classes: ClassA, ClassB, ClassC
Key functions: funcX, funcY, funcZ
```

Also highlight notable findings: god nodes, communities, surprising connections. Then offer to explore.

#### For `/readmenator query "<question>"`

1. Parse the question for key terms (class names, function names, file names, concepts).
2. Search the KNOWLEDGE_BASE.md content you already read for those terms.
3. Answer using ONLY what the knowledge base contains. Cite file paths and line numbers from the Architecture Reference.
4. If the knowledge base lacks enough detail, say so -- do not hallucinate. Offer to read the specific source file if needed.

#### For `/readmenator explain "<SymbolName>"`

1. Find the symbol in the Architecture Reference section of KNOWLEDGE_BASE.md.
2. Report: its type (class/function), file path, line number, docstring.
3. Use the Mermaid graph to identify what imports it (incoming edges) and what it imports (outgoing edges).
4. Use the "Imported by" cross-reference to list files that depend on it.
5. List other symbols in the same file for context.

#### For `/readmenator path "<SymbolA>" "<SymbolB>"`

1. Find both symbols in KNOWLEDGE_BASE.md.
2. Trace the import chain between their containing files using the Mermaid graph.
3. Report the path as: `file_a.py --imports--> module_x --imports--> file_b.py`
4. If no path exists, report the disconnected components.

### Step 4 -- Offer regeneration

When you finish answering, if the KNOWLEDGE_BASE.md is older than the source files (check git status or modify times), suggest:

> "The knowledge base may be stale. Run `/readmenator --rebuild` to regenerate it."

## Structure of KNOWLEDGE_BASE.md (for reference)

The agent should understand this format to parse it efficiently:

```
# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. ...

**Total Files Parsed:** N | **Total Symbols Extracted:** M | **Total Imports:** K | **Resolved Imports:** R

## Table of Contents
1. [Statistics Dashboard](#statistics-dashboard)
2. [God Nodes](#god-nodes)
3. [Community Analysis](#community-analysis)
4. [Surprising Connections](#surprising-connections)
5. [Suggested Questions](#suggested-questions)
6. [Structural Knowledge Map](#structural-knowledge-map)
7. [Architecture Reference](#architecture-reference)

---

## Statistics Dashboard
| Metric | Value |
|--------|-------|
| Total Files | N |
| ...

### Top Files by Import Count (Fan-Out)
| File | Imports | Symbols | Language |
| ...

## God Nodes
| File | Score | Connections |
| ...

## Community Analysis
### community_name (Cohesion: X.XX)
**N files** in this community:
- `file.py` (py, M symbols)
...

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod ...
    classDef cls ...
    classDef fn ...
    classDef ext ...

    subgraph community_0 ["Community Label"]
        module_py["module.py (py)"]
        class module_py mod;
        ...
    end

    module_py -- resolved_imports --> other_py  <- internal edge
    ext_os["os"]
    class ext_os ext;
    module_py -.->|imports| ext_os   <- external import edge (dashed)
```

## Architecture Reference

### PY (N files)

#### `filename.py`
**Path:** `path/to/filename.py`
**File Doc:** *Module-level documentation*

**Imported by:** `file_a.py`, `file_b.py`

**Classes:**
- `ClassName` (line 42) `class ClassName(Base)` - *Docstring describing the class.*

**Functions:**
- `function_name` (line 100) `def func(x, y)` - *Docstring describing the function.*
```

## How this compares to graphify

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
| Speed | Minutes (LLM calls) | Seconds |
| Cost | Token-based | Zero |
| Regeneration | Full or incremental | Full or incremental (SHA256 cache) |

Use readmenator when you need fast, free, structural understanding of a codebase with community intelligence. Use graphify when you need semantic cross-document relationships and multi-modal (pdf/image/video) extraction.

## Script location

The canonical source lives at:
- Repo: https://github.com/grisuno/ReadMenator
- Install: `pip install readmenator`
