---
name: readmenator
description: "Zero-token static analysis codebase context. Use KNOWLEDGE_BASE.md as source of truth -- no LLM extraction, no token cost. Pure AST + regex."
trigger: /readmenator
---

# /readmenator

Turn any codebase into a queryable knowledge base using pure static analysis. No LLMs. No tokens. No cloud. A single `KNOWLEDGE_BASE.md` file serves as the source of truth for all codebase questions.

Contrast with graphify: graphify costs tokens to extract entities and relationships via LLM agents. ReadMenator generates the same structural knowledge through deterministic AST/regex parsing -- zero tokens, instant, repeatable.

## Usage

```
/readmenator                              # ensure KNOWLEDGE_BASE.md exists, then use as context
/readmenator <path>                       # target a specific directory
/readmenator --rebuild                    # force regeneration even if KNOWLEDGE_BASE.md exists
/readmenator query "<question>"           # answer a question using the knowledge base
/readmenator explain "<ClassName>"        # explain a specific symbol with its relationships
/readmenator path "<SymbolA>" "<SymbolB>" # trace the dependency chain between two symbols
/readmenator update                       # regenerate KNOWLEDGE_BASE.md for changed files only (TODO)
```

## What ReadMenator is for

ReadMenator solves a specific problem: every time you ask an AI about a codebase, it needs to read files to understand the structure. This burns tokens. With ReadMenator, you pre-compute the structural map once (statically, for free), then use that map as context for all subsequent questions.

What it gives you:
1. **A structural map** -- classes, functions, methods, imports, all with line numbers and docstrings, organized by file and language
2. **Mermaid graph** -- visual dependency diagram showing which files import what, which symbols belong to which modules
3. **Zero ongoing cost** -- regenerate after code changes, always free

Supported languages (13+): C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly.

## What You Must Do When Invoked

If no path was given, use `.` (current directory). Do not ask the user for a path.

### Step 1 -- Ensure KNOWLEDGE_BASE.md exists

Check if `KNOWLEDGE_BASE.md` already exists in the target directory. If it does (and `--rebuild` was not given), skip to Step 2.

Otherwise, generate it:

```bash
python3 readmenator.py TARGET_PATH
```

If `readmenator.py` is not in the current directory, find it. The script ships with the ReadMenator repo. Common locations:

```bash
# Try these in order:
# 1. Current directory
# 2. Cloned repo
# 3. pip-installed (if packaged)
if [ -f "readmenator.py" ]; then
    READMENATOR_SCRIPT="readmenator.py"
elif [ -f "$HOME/src_note/py/readmenator.py/repo/ReadMenator/readmenator.py" ]; then
    READMENATOR_SCRIPT="$HOME/src_note/py/readmenator.py/repo/ReadMenator/readmenator.py"
else
    echo "readmenator.py not found. Clone it: git clone https://github.com/grisuno/ReadMenator"
    exit 1
fi
python3 "$READMENATOR_SCRIPT" TARGET_PATH
```

Replace `TARGET_PATH` with the actual path. If generation succeeds, print the summary (files, symbols, imports) shown in the script output.

If generation fails, tell the user and stop.

### Step 2 -- Read KNOWLEDGE_BASE.md as context

Read `TARGET_PATH/KNOWLEDGE_BASE.md`. This file has a predictable structure:

1. **Header** -- metadata (total files, symbols, imports)
2. **Structural Knowledge Map** -- a Mermaid graph (```mermaid ... ```) showing the file/import dependency diagram. Nodes are modules (rectangles), classes (green), and functions (yellow). External imports are dashed nodes.
3. **Architecture Reference** -- grouped by language (e.g. `### PY (1 files)`), then each file gets a section with:
   - File path
   - Lists of **Classes** with name, line number, and docstring
   - Lists of **Functions** with name, line number, and docstring

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

Then offer to explore: "Ask me anything about this codebase. I'll answer from the knowledge base."

#### For `/readmenator query "<question>"`

1. Parse the question for key terms (class names, function names, file names, concepts).
2. Search the KNOWLEDGE_BASE.md content you already read for those terms.
3. Answer using ONLY what the knowledge base contains. Cite file paths and line numbers from the Architecture Reference.
4. If the knowledge base lacks enough detail, say so -- do not hallucinate. Offer to read the specific source file if needed.

#### For `/readmenator explain "<SymbolName>"`

1. Find the symbol in the Architecture Reference section of KNOWLEDGE_BASE.md.
2. Report: its type (class/function), file path, line number, docstring.
3. Use the Mermaid graph to identify what imports it (incoming edges) and what it imports (outgoing edges).
4. List other symbols in the same file for context.

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

**Total Files Parsed:** N | **Total Symbols Extracted:** M | **Total Imports:** K

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,...
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,...
    classDef fn fill:#333,stroke:#dcdcaa,...
    classDef ext fill:#111,stroke:#666,...

    module_py["module.py (py)"]     <- module node
    class module_py mod;
    module_py_ClassName["ClassName"] <- class node
    class module_py_ClassName cls;
    module_py --> module_py_ClassName <- containment edge
    ext_os["os"]                      <- external import node
    class ext_os ext;
    module_py -.->|imports| ext_os   <- import edge (dashed)
```

## Architecture Reference

### PY (N files)

#### `filename.py`
**Path:** `path/to/filename.py`

**Classs:**
- `ClassName` (line 42) - *Docstring describing the class.*
- ...

**Functions:**
- `function_name` (line 100) - *Docstring describing the function.*
- ...
```

Node IDs in Mermaid follow the pattern: `{sanitized_path}_{sanitized_symbol_name}`. All non-alphanumeric chars become `_`. External imports are prefixed with `ext_`.

## How this compares to graphify

| Aspect | graphify | readmenator |
|--------|----------|-------------|
| Extraction | LLM agents (tokens) | AST + regex (free) |
| Output | graph.json + HTML + report | KNOWLEDGE_BASE.md |
| Languages | Any (LLM reads anything) | 13+ static parsers |
| Semantic edges | Yes (INFERRED, AMBIGUOUS) | No (structural only) |
| Community detection | Yes (Leiden/Louvain) | No |
| Cross-document inference | Yes | No (import chains only) |
| Speed | Minutes (LLM calls) | Seconds |
| Cost | Token-based | Zero |
| Regeneration | Full or incremental | Full (always fast) |

Use readmenator when you need fast, free, structural understanding of a codebase. Use graphify when you need semantic cross-document relationships and community detection.

## Script location

The canonical `readmenator.py` lives at:
- Repo: https://github.com/grisuno/ReadMenator
- Local path hint: `$HOME/src_note/py/readmenator.py/repo/ReadMenator/readmenator.py`

Update the find-command in Step 1 if you clone it elsewhere.
