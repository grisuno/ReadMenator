# ReadMenator

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/8d146d5d-8e35-45c9-a119-fa154d03446b" />


A token-free, offline, production-grade polyglot codebase knowledge graph & architectural analyzer.

**No LLMs. No tokens. No cloud costs.** Pure static analysis via AST + regex.

ReadMenator builds production-grade codebase knowledge graphs and architectural health reports 100% offline. Identify structural risks, security flaws, and change impact patterns instantly across 19 languages.

https://github.com/user-attachments/assets/af02cae9-5cb5-427e-84cc-af4d82374116

- [https://pypi.org/project/readmenator/](https://pypi.org/project/readmenator/)
- [https://grisuno.github.io/ReadMenator/](https://grisuno.github.io/ReadMenator/)

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
python -m readmenator /path/to/project --export-all                # JSON + HTML + SVG
python -m readmenator /path/to/project --json                      # graph.json (GraphRAG-ready)
python -m readmenator /path/to/project --html                      # graph.html (interactive vis.js)
python -m readmenator /path/to/project --svg                       # graph.svg (static)
python -m readmenator /path/to/project --graphml                   # graph.graphml (Gephi/yEd)
python -m readmenator /path/to/project obsidian                    # Obsidian vault (wikilinks)
python -m readmenator /path/to/project wiki                       # Agent wiki (index + community pages)
python -m readmenator /path/to/project lint-wiki                  # Wiki health check
python -m readmenator /path/to/project lint                        # Architecture violations (exit 1 on errors)
python -m readmenator /path/to/project strip-dead-code             # Orphaned symbol report
python -m readmenator /path/to/project generate-rules              # Generate .cursorrules file
python -m readmenator /path/to/project refactor-monolith           # Refactoring plans + executable scripts
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

### Interactive System Maps

ReadMenator builds five interactive physics-driven diagrams from scanned topology and writes
them to `readmenator-maps/` on every run: architecture, workflow, sequence, dataflow,
and lifecycle. Each file is a vis.js network with draggable nodes, live physics,
search, focus passport with full file documentation, upstream/downstream reach,
directed route probing, role comparison, guided chapters, dark/light themes,
keyboard shortcuts, hash deep links, and client-side PNG and JSON export.
Cards state the primary scope honestly ("N of M files");
the full per-file listing lives in KNOWLEDGE_BASE.md.

```bash
python -m readmenator /path/to/project diagrams        # Export all 5 vis.js maps + gallery index (needs network)
python -m readmenator /path/to/project diagram sequence # Export one vis.js map (draggable nodes, live physics)
python -m readmenator /path/to/project pages           # Publish docs/ static site: gallery index + maps (GitHub Pages ready)
```

Maps are physics-driven vis.js documents (engine loaded from a CDN pinned in
Config). Hover a node for a preview card; click it to dim everything outside its
neighbourhood and open a passport with metric tiles, an ego mini-map (used-by on
the left, imports on the right, every dot clickable), the docstring, a filterable
symbol table with signatures, and Back history. Links are first-class too: hover
one for a card, click it for a link passport (what depends on what, mutual
dependencies, community bridges, role crossings, parallel links, both
neighbourhoods) and share it with `#edge=<from>~<to>`.

The **Force Graph Explorer** (`readmenator-maps/graph-force.html`, featured in the
gallery with a real ForceAtlas2 thumbnail) draws every file, community, layer and
external in a 2D map or a 3D space:

- **Exact selection.** Hover, click, drag and right-click are hit-tested in the page
  against the positions drawn in the same frame, so the pointer always picks what is
  under it, including labels and curved edges, in both 2D and 3D.
- **3D without planets.** The 3D view keeps the WebGL engine for links, arrows and
  flow particles, but draws files as flat document tiles (communities as hexagons,
  layers as diamonds, externals as triangles) on an overlay synced to the camera, with
  depth fade, group halos, readable labels, camera fly-to and an optional orbit.
- **Node actions.** Passport with PageRank, symbols, docs and grouped neighbours;
  reach Upstream (used by, the blast radius), Downstream (uses) or Both at 1, 2, 3 or
  all hops; isolate, hide, pin by dragging (2D), copy path; right-click menu for all of
  it; double-click isolates.
- **Edge actions.** Hover and click any dependency edge for a passport that reads the
  relation as a sentence and flags mutual dependencies, edges that close an import
  cycle, upward layer crossings and community bridges.
- **Exploration.** Path finder (Shift+click, `P`, or the menu) that prefers a directed
  route and explains it hop by hop; color by community, layer or language (clusters
  follow the grouping); node and edge type filters; layouts force, clusters, layer
  rings (shells in 3D) and dependency tree.
- **Lenses for logic bugs.** Import cycles (Tarjan SCC), files nothing imports
  (entry points or dead code), disconnected files, and PageRank hubs.
- Deep links restore the view: `#node=<id>&view=3d&layout=cluster&color=layer&dir=up&depth=2`,
  `#path=<a>~<b>`, `#lens=cycles`, `#edge=<key>`. The page also exposes
  `window.ReadmenatorExplorer` for console scripting.

The **Edge Bundle Explorer** (`readmenator-maps/graph-bundle.html`, its own gallery
card next to the force graph, `readmenator . bundles` to export it alone) is the
hierarchical edge bundling view from the video, live. It needs no network: one
canvas, no CDN.

- **Circle (2D).** Files sit on a ring grouped into community arcs (hubs first);
  every resolved import is a B-spline routed through the community tree, so thick
  bundles are the real seams between subsystems.
- **Sphere (3D).** The same hierarchy on a globe: each community owns a contiguous
  cap sized by its file count, wires dive through the core between caps. Drag to
  rotate, wheel to zoom, optional auto-rotate; selecting a file or community flies
  the camera to face it.
- **Reading it.** Hover a file: cyan wires are what it imports, pink what imports it.
  Click to pin it (imports and importers listed, one click to open it in the force
  graph in 2D or 3D). Click an arc, cap label or legend row to focus a community
  (inside/out/in counts, cohesion, top flows to other communities).
- **Controls.** Beta slider (0 straight chords, 1 fully bundled, recomputed live),
  crossing-only filter, direction (both, imports, imported by), color by community,
  layer or language, search, PNG export, light/dark theme. Deep links:
  `#view=3d&node=<id>&group=<key>&beta=0.7&color=layer&dir=out&cross=1`; console API
  `window.ReadmenatorBundles`.

Serve the `docs/` directory directly with GitHub Pages (Settings -> Pages ->
Deploy from branch -> folder `docs/`). The gallery `index.html` links every map
with relative paths, works fully offline, and needs no build step.
The site also ships `llms.txt` (the [llms.txt](https://llmstxt.org) convention),
so agents browsing the published site get a plain-markdown map of the wiki,
agent docs, and knowledge base instead of parsing HTML. Once `docs/` holds a
gallery, every `--rebuild` refreshes it (video and docs included).

### Overview Video

`readmenator . video` renders a synthwave mp4 from real scan data in nine acts:
layers, god nodes, blast-radius tree, communities, **Emergence** (ForceAtlas2
LinLog with adaptive speed, animated from seeded chaos to convergence, nodes
sized by PageRank with random-surfer particles on the hottest edges), **Orbit**
(the force graph laid out by ForceAtlas2 in 3D and flown by a camera: color by
community, layer and language in turn, a tour that zooms into the largest
communities with their cohesion and seams, then the 1-hop reach of the top hub),
**The Wiring** (Holten hierarchical edge bundling: files on a circle by community,
imports routed as B-splines through the community tree, a spotlight sweeping each
community and a live flow ranking), **The Sphere** (the 3D layout folds onto a globe
of community caps and every import bundles through its core), and code DNA. A
closing invitation shows both explorers spinning with their paths, so viewers know
where to go next. Set an act's duration (`VIDEO_ORBIT_S`, `VIDEO_SPHERE_S`,
`VIDEO_INVITE_S`, ...) to 0 to drop it with its card.

### GraphRAG for agents (zero tokens to build, cheap to query)

`readmenator-graphrag/` is a GraphRAG index built without any language model:
entities (files, symbols, concepts, external modules, project memory), typed
relationships (defines, imports, calls, inherits, documents), source text units
(each symbol's real code span), and a report hierarchy (Louvain communities,
Louvain themes over the community graph, a project root) whose sentences are all
measured facts: PageRank, fan-in, findings, cycles, hotspots, layer violations.

```bash
readmenator . ask "how are communities detected"      # auto mode
readmenator . ask "PageRank seeds" --local            # BM25 + Personalized PageRank (HippoRAG style)
readmenator . ask "main subsystems and risks" --global --budget 1500   # map-reduce over reports
readmenator . graphrag                                # rebuild only the index
```

MCP: tool `readmenator.graphrag` and resource `readmenator://graphrag`.

### Project memory and agent skills

`readmenator-agent/MEMORY.md` is the cross-session context file: purpose and
domain vocabulary, detected workflow commands, declared rules, style norms and
definition of done quoted from AGENTS.md / CLAUDE.md / CONTRIBUTING.md /
.cursorrules with `file:line`, measured baselines (docstring coverage, naming,
findings, cycles), risks, and a **session log preserved across rebuilds**:

```bash
readmenator . remember "Retries capped at 3: the bank bans clients after 4 failures" --kind business
readmenator . memory            # print it (MCP: readmenator.memory / readmenator.remember)
readmenator . skills            # install agent skills into .claude/skills/
```

Notes are indexed by GraphRAG, so `ask` surfaces recorded business rules next to
the code they govern. Four packaged skills (`readmenator-orient`, `readmenator-ask`,
`readmenator-change`, `readmenator-memory`) teach any agent the protocol; `run`
installs them automatically when the project already has a `.claude/` directory.

### Agent-Ready Output (zero tokens)

`readmenator-agent/` is built for agents that `grep` and `read`:

- `MANIFEST.json` records `git_commit`: compare it with `git rev-parse HEAD`
  to know whether the docs are stale before trusting them. It also lists every
  document with its line count and approximate token cost.
- Every document stays under 500 lines. Larger ones are paged as `NAME_p2.md`,
  so grep with `NAME*.md`.
- `INDEX.md` gives each file a one-sentence purpose and a "Used by" count
  (blast radius at a glance).
- `API.md` lists one line per public function, and `GOTCHAS.md` ranks blast
  radius without counting tests.
- readmenator never rescans its own generated output.

### GitHub Wiki

Mirror the wiki, agent docs, recipes, and KNOWLEDGE_BASE.md into the
repository's GitHub wiki. Pages get a sidebar, cross-links, and source
permalinks pinned to the current commit:

```bash
readmenator . --rebuild                  # regenerates everything AND publishes the GitHub wiki
readmenator . gh-wiki                    # publish the wiki only
readmenator . gh-wiki --dry-run          # render pages into readmenator-ghwiki/ (no git calls)
```

Requirements: the wiki is enabled, its first page was created once in the web
UI, and git can push (for example after `gh auth setup-git`). Pages written by
hand are never deleted. Only pages that readmenator generated earlier are
replaced.

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
| GraphRAG | `_graphrag.py` | Entities, relationships, text units, community report hierarchy, local/global search |
| Graph layouts | `_graphlayout.py` | ForceAtlas2 (2D/3D) snapshots, circular and spherical hierarchical edge bundling |
| Edge bundles | `_bundlegraph.py` | Circle + sphere bundle payload, settings, thumbnail |
| Bundle page | `_bundlegraph_page.py` | Self-contained canvas page: 2D circle, 3D sphere, live beta, focus panels |
| Force graph | `_forcegraph.py` | Heterogeneous explorer payload, settings, thumbnail |
| Explorer page | `_forcegraph_page.py` | 2D/3D explorer HTML: hit-testing, overlay glyphs, node and edge actions |
| Memory | `_memory.py` | MEMORY.md: declared rules, measured baselines, preserved session log |
| Skills | `_skill_installer.py` | Installs packaged agent skills from `_skills/` |
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
a zero-token polyglot static analysis tool. Analysis outputs are available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings
  - `SECURITY.md` -- Findings by severity
- **[readmenator-wiki/](./readmenator-wiki/)** -- Navigable wiki (start here for the big picture).
  - `index.md` -- Entry point: overview, reading order, god nodes, connections
  - `community_*.md` -- One synthesis page per code community
  - `REPORT.md` -- Honest audit: coverage, confidence, limits

AI agents: Read `readmenator-wiki/index.md` first for the big picture, then `readmenator-agent/INDEX.md` for grep-friendly lookup.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference.
<!-- /readmenator-kb-link -->

