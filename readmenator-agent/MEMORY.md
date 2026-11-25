# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 167 files at commit `e90663a9ff78`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: A token-free, offline, production-grade polyglot codebase knowledge graph & architectural analyzer. (`README.md:7`)
- Domain vocabulary (term, files): `readmenator` (113), `file` (99), `graph` (77), `files` (70), `node` (67), `project` (65), `edges` (64), `config` (63), `symbols` (62), `one` (61), `set` (59), `imports` (57), `build` (56), `path` (56), `text` (55)
- Subsystem `readmenator: _app`: 46 files, core `readmenator/_app.py`: Application orchestrator: scan, resolve, analyze, and write every output.
- Subsystem `readmenator/parsers`: 30 files, core `readmenator/_models.py`: Data model types for the readmenator knowledge graph.
- Subsystem `readmenator: _pipeline`: 25 files, core `readmenator/_pipeline.py`: AnalyzerFactory (lazy component construction) and DeepAnalysisRunner.
- Subsystem `readmenator: _diagrams`: 20 files, core `readmenator/_diagrams.py`: Self-contained interactive system maps for the knowledge graph.
- Subsystem `readmenator: _mcp_server`: 15 files, core `readmenator/_mcp_server.py`: MCP (Model Context Protocol) stdio server for ReadMenator.
- Subsystem `readmenator: _flowcharts`: 14 files, core `readmenator/_flowcharts.py`: Architecture and execution-flow Mermaid diagrams from static structure.
- Subsystem `readmenator: _video`: 13 files, core `readmenator/_video.py`: Cinematic codebase overview video, general purpose.
- Business rules that the code cannot show live in section 7: record them there.

## 2. Workflow

Detected commands:
- `python -m pytest -q` (pyproject.toml)
- `readmenator --help` (pyproject.toml [project.scripts])
- `readmenator-mcp --help` (pyproject.toml [project.scripts])
- `CI workflow main.yml` (.github/workflows/main.yml)
- `CI workflow publish.yml` (.github/workflows/publish.yml)
- `CI workflow static.yml` (.github/workflows/static.yml)
- `CI workflow validate-rules.yml` (.github/workflows/validate-rules.yml)

Session protocol:
1. Start: read this file, then `readmenator . fresh` (exit 1 means run `readmenator . --rebuild`).
2. Orient: `readmenator-wiki/index.md`; for a question use `readmenator . ask "<question>"` (local = entities + sources, `--global` = community reports).
3. Before editing a file: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md`.
4. After the change: run the tests above, then `readmenator . --rebuild` so the maps, wiki, and this file stay true.
5. End: record decisions, business rules, and gotchas with `readmenator . remember "<note>" --kind decision`.

## 3. Rules and constraints

Declared:
- Config is the single source of truth for all constants (`CLAUDE.md:908`)
- Symbol creation logic is not duplicated across parsers (`CLAUDE.md:909`)
- Docstring extraction lives once in LanguageParser base class (`CLAUDE.md:910`)
- File-level doc extraction lives once in PolyglotScanner (`CLAUDE.md:911`)
- All analysis thresholds in Config, never hardcoded (`CLAUDE.md:912`)
- Single Responsibility: each module has one job (`CLAUDE.md:915`)
- Open/Closed: add parsers/analyzers without modifying existing code (`CLAUDE.md:916`)
- Liskov Substitution: all parsers inherit from LanguageParser (`CLAUDE.md:917`)
- Interface Segregation: each contract exposes minimal surface (`CLAUDE.md:918`)
- Dependency Inversion: app depends on abstractions (Config, Scanner) (`CLAUDE.md:919`)
- No absolute paths in source code (`CLAUDE.md:922`)
- No network calls from the core scanner (`CLAUDE.md:923`)
- Symlinks rejected (`CLAUDE.md:924`)
- File size limits enforced (`CLAUDE.md:925`)
- Directory depth limits enforced (`CLAUDE.md:926`)
- All parsing exceptions caught (`CLAUDE.md:927`)
- No external API calls in any analysis or export module (`CLAUDE.md:928`)
- Pattern-based security analyzer with 18 language rule sets (`CLAUDE.md:929`)
- Privacy mode strips source snippets from output (`CLAUDE.md:930`)
- Fix any security issues found (symlinks, path traversal, size limits) (`CLAUDE.md:959`)
- Remove hardcoded values and move to Config if they are tuneable (`CLAUDE.md:960`)
- Update tests to cover new behaviors (`CLAUDE.md:961`)
- Keep the "Classs" pluralization fix intact (`CLAUDE.md:962`)
- Do not add absolute paths (`CLAUDE.md:963`)
- Do not add external dependencies to the core scanner (`CLAUDE.md:964`)
- Maintain backward compatibility of the CLI interface (`CLAUDE.md:965`)
- Update this CLAUDE.md and README.md for any contract changes (`CLAUDE.md:966`)
- Fix inline imports (move to top of file) (`CLAUDE.md:967`)
- Add type annotations to all function signatures (`CLAUDE.md:968`)
- Maintain strict separation of concerns. (`.cursorrules:5`)
- UI/presentation components must not contain business logic or database queries. (`.cursorrules:6`)
- Business logic must not depend on presentation or infrastructure details. (`.cursorrules:7`)
- Data access must be isolated behind repository interfaces. (`.cursorrules:8`)
- Keep files under 300 lines. Split larger files into cohesive modules. (`.cursorrules:9`)
- Never add absolute paths to source code. (`.cursorrules:10`)
- Never hardcode configuration values. Use the Config class. (`.cursorrules:11`)
- All new modules must have corresponding test files. (`.cursorrules:12`)
- Use type annotations on all function signatures. (`.cursorrules:13`)
- Follow the existing code style and naming conventions. (`.cursorrules:14`)

Measured baseline:
- Security findings at medium or above: 0 (see `readmenator-agent/SECURITY.md`); do not add new ones.
- Dependency cycles: 0; layer violations: 11 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- All progress/report messages use `logging.getLogger(__name__)` (never `print()`) (`CLAUDE.md:933`)
- User-facing output (query results, summaries) uses `print()` to stdout (`CLAUDE.md:934`)
- Logging format configured in `__main__.py` via `logging.basicConfig` (`CLAUDE.md:935`)
- Each module gets its own logger via `logger = logging.getLogger(__name__)` (`CLAUDE.md:936`)

Measured baseline:
- py: 165 files, 3338 symbols; docstrings on 56% of symbols; functions snake_case (96%); types PascalCase (100%); median file 224 lines, max 4182.
- js: 1 files, 35 symbols; docstrings on 100% of symbols; functions snake_case (80%); types PascalCase (40%); median file 5 lines, max 5.
- sh: 1 files, 1 symbols; docstrings on 100% of symbols; functions snake_case (100%); median file 42 lines, max 42.
- Tests: 60 files under tests; follow the existing naming (e.g. `test_agent_friendliness.py`).

## 5. Minimum deliverables

Declared:
- Tests named as `test_<contract>_<behavior>` (BDD style) (`CLAUDE.md:939`)
- Each module has its own test class (`CLAUDE.md:940`)
- Security behaviors tested explicitly (`CLAUDE.md:941`)
- Edge cases tested (empty files, syntax errors, symlinks) (`CLAUDE.md:942`)
- Integration tests validate end-to-end pipeline (`CLAUDE.md:943`)
- "Classs" regression test prevents re-introduction (`CLAUDE.md:944`)
- All new modules have complete contract test suites (`CLAUDE.md:945`)
- Mutation check after SDD+TDD+BDD: introduce one-line mutants (validation bypass, escaping bypass, ordering change); a killed mutant fails at least one test, a surviving mutant requires a stronger test before refactor (`CLAUDE.md:946`)
- Property-based parser tests skip cleanly when hypothesis is not installed (inert strategy placeholders, identity decorators) (`CLAUDE.md:947`)
- English only, no emojis, no prose comments, docstrings on every public and private function (`CLAUDE.md:950`)
- DRY and SOLID, one self-contained file per contract, production code with no placeholders or simplifications (`CLAUDE.md:951`)
- No hardcoded tuneables or magic numbers: every setting lives in Config (`CLAUDE.md:952`)
- No absolute paths, no network calls from analysis or export modules, all untrusted text escaped at the boundary (`CLAUDE.md:953`)
- Boy scout: any technical debt or security flaw found during the change is fixed without losing functionality (`CLAUDE.md:954`)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 56%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `readmenator/parsers/__init__.py`
- Hotspots (complex and central): `readmenator/_vendor/force-graph.min.js`, `readmenator/_video.py`, `readmenator/_diagrams.py`, `readmenator/_app.py`, `tests/test_parsers.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind> --sem "synonym, synonym"` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover. `--sem` seeds 3-5 synonyms at write time so `readmenator . recall` finds the note without embeddings.

<!-- readmenator:memory:notes:begin -->
- 2026-10-21 [decision] Added _receipts/_uncertainty/_hypotheses contracts: deploynator release receipts ingest (observed/candidate/predicted evidence hierarchy), uncertainty scorer (heuristic + optional sklearn RF, predictions carry model version and provenance), hypothesis validator (LLM proposals never enter graph unverified). CLI: readmenator . receipts [dir].
- 2026-10-21 [workflow] Deployment flow: deploynator release --receipt (or --trace with dry-run) writes receipt JSON at release-receipts/; readmenator . receipts consumes them writing RELEASES.md + release-edges.json (confirmed/unobserved/predicted edges). _receipts.py maps receipt commands to callership via stage labels (release:<platform> -> Platform.create_release).
- 2026-10-21 [decision] Packaged skills updated: new readmenator-receipts skill (receipt ingest + evidence reconciliation workflow); orient cheat sheet links release evidence layer; deploynator SKILL.md now documents --receipt/--trace and the receipt consumption chain.
- 2026-10-28 [decision] Video act XII (The Organism) tells the git history: readmenator/_githistory.py reads every release tag (plus first commit and HEAD) with read-only git plumbing, materialises each tracked tree with the same scanner, and the union graph grows release by release (ghosts for unborn files, heartbeat pulse per landing release, final fold onto the community globe).
<!-- readmenator:memory:notes:end -->
