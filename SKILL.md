---
name: readmenator
description: "Zero-token static analysis codebase context. MCP-native AI agent integration. Use MCP tools for queries -- no LLM extraction, no KB file parsing, no token cost. Pure AST + regex."
trigger: /readmenator
---

# /readmenator

Turn any codebase into a queryable knowledge base using pure static analysis. No LLMs. No tokens. No cloud.

## Architecture: MCP-first, KB-fallback

```
Agent (Claude) ──MCP tools──> readmenator MCP server ──> live queries (50-200 tokens)
              \
               ──read file──> KNOWLEDGE_BASE.md ──> fallback (2000-8000 tokens)
```

The MCP server is the **primary** interface. The KNOWLEDGE_BASE.md file is the **fallback** for agents that don't support MCP tool calls.

**Token savings with MCP:**
| Query type | Without MCP (read KB.md) | With MCP (tool call) | Savings |
|-----------|------------------------|---------------------|---------|
| Summary  | 2000-8000 tokens | ~300 tokens | 85-96% |
| Symbol search | Full KB parse | ~150 tokens | 93-98% |
| Explain symbol | Parse KB for context | ~100 tokens | 95-99% |
| Path tracing | Parse KB for context | ~100 tokens | 95-99% |
| Daily (10 queries) | 20K-80K tokens | ~3K tokens | 85-96% |

## Usage

```
/readmenator                              # ensure KB + MCP server exist, then use tools
/readmenator <path>                       # target a specific directory
/readmenator --rebuild                    # force regeneration
/readmenator serve <path>                 # start MCP stdio server
/readmenator --context-budget 500         # generate KB truncated to ~500 tokens
```

## What ReadMenator is for

ReadMenator pre-computes a structural map of your codebase (statically, for free), then serves it via MCP tools so the AI agent never needs to read source files or parse large KB documents.

**19 languages:** C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, PHP, Dart, GDScript, Nim, Assembly, Ruby, Swift, Kotlin, Scala, Lua, Elixir.

## What You Must Do When Invoked

If no path was given, use `.` (current directory). Do not ask the user for a path.

### Step 1 -- Ensure the MCP server is ready

First, check if KNOWLEDGE_BASE.md exists. Generate it if not:

```bash
python3 -m readmenator TARGET_PATH --rebuild
```

If `readmenator` is not installed:
```bash
if [ -f "readmenator.py" ]; then
    python3 readmenator.py TARGET_PATH
else
    pip install readmenator && python3 -m readmenator TARGET_PATH --rebuild
fi
```

Replace `TARGET_PATH` with the actual path.

### Step 2 -- Use MCP tools (primary path)

**Do NOT read KNOWLEDGE_BASE.md as text.** Use the MCP tools below instead. They return structured data at a fraction of the token cost.

Available MCP tools (when `readmenator serve <path>` is running):

| Tool | Purpose | Token cost |
|------|---------|-----------|
| `readmenator.summary` | Codebase overview | ~300 |
| `readmenator.query(text)` | Free-text symbol search | ~150 |
| `readmenator.explain(name)` | Full symbol detail | ~100 |
| `readmenator.path(symbol_a, symbol_b)` | Dependency chain | ~100 |
| `readmenator.findings(min_severity)` | Security issues | ~200 |
| `readmenator.security_summary` | Security audit summary | ~100 |
| `readmenator.taint` | Taint propagation paths | ~300 |
| `readmenator.hotspots(top_n)` | Hotspot files | ~200 |
| `readmenator.cycles` | Circular dependencies | ~200 |
| `readmenator.communities` | Import communities | ~300 |
| `readmenator.layers` | Architecture layers | ~200 |
| `readmenator.layer_violations` | Layer rule violations | ~200 |
| `readmenator.rebuild` | Full KB regeneration | N/A |
| `readmenator.update` | Incremental update | N/A |

**How to call MCP tools (Claude Desktop):**

The MCP server communicates via stdin/stdout using JSON-RPC 2.0. Claude Desktop connects automatically when configured with:

```json
{
  "mcpServers": {
    "readmenator": {
      "command": "readmenator-mcp",
      "args": ["/path/to/project"]
    }
  }
}
```

Or via Python directly:
```json
{
  "mcpServers": {
    "readmenator": {
      "command": "python3",
      "args": ["-m", "readmenator._mcp_server", "/path/to/project"]
    }
  }
}
```

### Step 2b -- Fallback: Read KNOWLEDGE_BASE.md (only if MCP unavailable)

If the MCP server is not running AND you cannot start it, read `TARGET_PATH/KNOWLEDGE_BASE.md` directly.

The file structure is deterministic:

1. **Header** -- metadata (total files, symbols, imports)
2. **Statistics Dashboard** -- file counts, fan-in/fan-out, language breakdown
3. **God Nodes** -- most central files ranked by connectivity
4. **Community Analysis** -- import-based groups with cohesion scores
5. **Structural Knowledge Map** -- Mermaid graph (```mermaid ... ```)
6. **Architecture Reference** -- grouped by language, each file lists its symbols

If `--context-budget` was used during generation, the KB starts with a compact summary section (first ~400 chars) followed by high-priority analysis sections, truncated to the specified token budget.

### Step 3 -- Answer based on MCP tool results

For `/readmenator` (no subcommand): Call `readmenator.summary` and present the result.

For `/readmenator query "<question>"`: Call `readmenator.query(text="<question>")`.

For `/readmenator explain "<symbol>"`: Call `readmenator.explain(name="<symbol>")`.

For `/readmenator path "<A>" "<B>"`: Call `readmenator.path(symbol_a="<A>", symbol_b="<B>")`.

### Step 4 -- Offer regeneration

When done, suggest:
> "The knowledge base may be stale. Run `/readmenator --rebuild` to regenerate, or use `readmenator.rebuild` via MCP."

## MCP Resources (structured data access)

For agents that support MCP resources:

| Resource | Content | Type |
|----------|---------|------|
| `readmenator://summary` | Structured JSON: files, symbols, imports, langs, god nodes | JSON |
| `readmenator://graph` | Full graph: nodes + edges | JSON |
| `readmenator://findings` | All security findings grouped by severity | JSON |
| `readmenator://analysis` | Complete analysis: communities, taint, hotspots, cycles | JSON |
| `readmenator://kb` | Full KNOWLEDGE_BASE.md text | Markdown |

## Comparison with graphify

| Aspect | graphify | readmenator |
|--------|----------|-------------|
| Extraction | LLM agents (tokens) | AST + regex (free) |
| Agent integration | MCP queries | MCP tools + resources |
| Community detection | Yes (Leiden) | Yes (label propagation) |
| Semantic edges | Yes (costs tokens) | No (structural only, free) |
| Security analysis | No | Yes (18 languages) |
| Taint propagation | No | Yes |
| Export formats | HTML, JSON, Obsidian | JSON, HTML, SVG, GraphML, Obsidian, SARIF |
| Token cost per query | ~200 (MCP query) | ~100-300 (MCP tool) |
| Regeneration cost | Token-based (LLM) | Zero (AST) |

Use readmenator when you want **zero-token generation + minimal-token queries** via MCP. Use graphify when you need semantic cross-document inference with LLM extraction.

## Script location

- Repo: https://github.com/grisuno/ReadMenator
- Install: `pip install readmenator`
- MCP entry: `python3 -m readmenator._mcp_server <path>`

<!-- readmenator-agent-kb-link -->
## Project Knowledge Base

This project contains analysis outputs generated by [ReadMenator](https://github.com/grisuno/ReadMenator), a zero-token polyglot static analysis tool.

**For humans:** Read `KNOWLEDGE_BASE.md` -- full architecture reference.

**For agents:** Read `readmenator-agent/INDEX.md` -- grep-friendly index.
  - `readmenator-agent/INDEX.md` -- file -> purpose map (start here)
  - `readmenator-agent/API.md` -- public functions + contracts
  - `readmenator-agent/GOTCHAS.md` -- "don't change X because Y breaks"
  - `readmenator-agent/KB_<subsystem>.md` -- per-subsystem context (grep-friendly)
  - `readmenator-agent/SECURITY.md` -- findings by severity
  - `readmenator-agent/recipes/*.md` -- actionable task blocks

If outputs are outdated, regenerate by running:

    pip install readmenator && readmenator .
<!-- /readmenator-agent-kb-link -->
