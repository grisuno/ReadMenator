# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 161 files at commit `9f15c8bd2c4c`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: A token-free, offline, production-grade polyglot codebase knowledge graph & architectural analyzer. (`README.md:7`)
- Domain vocabulary (term, files): `readmenator` (109), `file` (94), `graph` (75), `files` (69), `node` (67), `edges` (64), `symbols` (62), `project` (61), `config` (57), `imports` (57), `build` (55), `nodes` (55), `one` (55), `symbol` (55), `set` (55)
- Subsystem `readmenator: _video`: 41 files, core `readmenator/_video.py`: Cinematic codebase overview video, general purpose.
- Subsystem `readmenator/parsers`: 34 files, core `readmenator/_models.py`: Data model types for the readmenator knowledge graph.
- Subsystem `readmenator: _agent_output`: 19 files, core `readmenator/_agent_output.py`: Agent-friendly output generator for ReadMenator.
- Subsystem `readmenator: _graphrag`: 18 files, core `readmenator/_graphrag.py`: Zero-token GraphRAG index and retrieval for AI agents.
- Subsystem `readmenator: _pipeline`: 18 files, core `readmenator/_pipeline.py`: AnalyzerFactory (lazy component construction) and DeepAnalysisRunner.
- Subsystem `readmenator: _diagrams`: 15 files, core `readmenator/_diagrams.py`: Self-contained interactive system maps for the knowledge graph.
- Subsystem `readmenator: _flowcharts`: 12 files, core `readmenator/_flowcharts.py`: Architecture and execution-flow Mermaid diagrams from static structure.
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
- Config is the single source of truth for all constants (`CLAUDE.md:863`)
- Symbol creation logic is not duplicated across parsers (`CLAUDE.md:864`)
- Docstring extraction lives once in LanguageParser base class (`CLAUDE.md:865`)
- File-level doc extraction lives once in PolyglotScanner (`CLAUDE.md:866`)
- All analysis thresholds in Config, never hardcoded (`CLAUDE.md:867`)
- Single Responsibility: each module has one job (`CLAUDE.md:870`)
- Open/Closed: add parsers/analyzers without modifying existing code (`CLAUDE.md:871`)
- Liskov Substitution: all parsers inherit from LanguageParser (`CLAUDE.md:872`)
- Interface Segregation: each contract exposes minimal surface (`CLAUDE.md:873`)
- Dependency Inversion: app depends on abstractions (Config, Scanner) (`CLAUDE.md:874`)
- No absolute paths in source code (`CLAUDE.md:877`)
- No network calls from the core scanner (`CLAUDE.md:878`)
- Symlinks rejected (`CLAUDE.md:879`)
- File size limits enforced (`CLAUDE.md:880`)
- Directory depth limits enforced (`CLAUDE.md:881`)
- All parsing exceptions caught (`CLAUDE.md:882`)
- No external API calls in any analysis or export module (`CLAUDE.md:883`)
- Pattern-based security analyzer with 18 language rule sets (`CLAUDE.md:884`)
- Privacy mode strips source snippets from output (`CLAUDE.md:885`)
- Fix any security issues found (symlinks, path traversal, size limits) (`CLAUDE.md:914`)
- Remove hardcoded values and move to Config if they are tuneable (`CLAUDE.md:915`)
- Update tests to cover new behaviors (`CLAUDE.md:916`)
- Keep the "Classs" pluralization fix intact (`CLAUDE.md:917`)
- Do not add absolute paths (`CLAUDE.md:918`)
- Do not add external dependencies to the core scanner (`CLAUDE.md:919`)
- Maintain backward compatibility of the CLI interface (`CLAUDE.md:920`)
- Update this CLAUDE.md and README.md for any contract changes (`CLAUDE.md:921`)
- Fix inline imports (move to top of file) (`CLAUDE.md:922`)
- Add type annotations to all function signatures (`CLAUDE.md:923`)
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
- All progress/report messages use `logging.getLogger(__name__)` (never `print()`) (`CLAUDE.md:888`)
- User-facing output (query results, summaries) uses `print()` to stdout (`CLAUDE.md:889`)
- Logging format configured in `__main__.py` via `logging.basicConfig` (`CLAUDE.md:890`)
- Each module gets its own logger via `logger = logging.getLogger(__name__)` (`CLAUDE.md:891`)

Measured baseline:
- py: 159 files, 3138 symbols; docstrings on 55% of symbols; functions snake_case (96%); types PascalCase (100%); median file 205 lines, max 4182.
- js: 1 files, 35 symbols; docstrings on 100% of symbols; functions snake_case (80%); types PascalCase (40%); median file 5 lines, max 5.
- sh: 1 files, 1 symbols; docstrings on 100% of symbols; functions snake_case (100%); median file 42 lines, max 42.
- Tests: 57 files under tests; follow the existing naming (e.g. `test_agent_friendliness.py`).

## 5. Minimum deliverables

Declared:
- Tests named as `test_<contract>_<behavior>` (BDD style) (`CLAUDE.md:894`)
- Each module has its own test class (`CLAUDE.md:895`)
- Security behaviors tested explicitly (`CLAUDE.md:896`)
- Edge cases tested (empty files, syntax errors, symlinks) (`CLAUDE.md:897`)
- Integration tests validate end-to-end pipeline (`CLAUDE.md:898`)
- "Classs" regression test prevents re-introduction (`CLAUDE.md:899`)
- All new modules have complete contract test suites (`CLAUDE.md:900`)
- Mutation check after SDD+TDD+BDD: introduce one-line mutants (validation bypass, escaping bypass, ordering change); a killed mutant fails at least one test, a surviving mutant requires a stronger test before refactor (`CLAUDE.md:901`)
- Property-based parser tests skip cleanly when hypothesis is not installed (inert strategy placeholders, identity decorators) (`CLAUDE.md:902`)
- English only, no emojis, no prose comments, docstrings on every public and private function (`CLAUDE.md:905`)
- DRY and SOLID, one self-contained file per contract, production code with no placeholders or simplifications (`CLAUDE.md:906`)
- No hardcoded tuneables or magic numbers: every setting lives in Config (`CLAUDE.md:907`)
- No absolute paths, no network calls from analysis or export modules, all untrusted text escaped at the boundary (`CLAUDE.md:908`)
- Boy scout: any technical debt or security flaw found during the change is fixed without losing functionality (`CLAUDE.md:909`)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 55%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `readmenator/parsers/__init__.py`
- Hotspots (complex and central): `readmenator/_vendor/force-graph.min.js`, `readmenator/_video.py`, `readmenator/_diagrams.py`, `readmenator/_app.py`, `tests/test_parsers.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
- 2026-10-21 [decision] Added _receipts/_uncertainty/_hypotheses contracts: deploynator release receipts ingest (observed/candidate/predicted evidence hierarchy), uncertainty scorer (heuristic + optional sklearn RF, predictions carry model version and provenance), hypothesis validator (LLM proposals never enter graph unverified). CLI: readmenator . receipts [dir].
- 2026-10-21 [workflow] Deployment flow: deploynator release --receipt (or --trace with dry-run) writes receipt JSON at release-receipts/; readmenator . receipts consumes them writing RELEASES.md + release-edges.json (confirmed/unobserved/predicted edges). _receipts.py maps receipt commands to callership via stage labels (release:<platform> -> Platform.create_release).
- 2026-10-21 [decision] Packaged skills updated: new readmenator-receipts skill (receipt ingest + evidence reconciliation workflow); orient cheat sheet links release evidence layer; deploynator SKILL.md now documents --receipt/--trace and the receipt consumption chain.
- 2026-10-28 [decision] Video act XII (The Organism) tells the git history: readmenator/_githistory.py reads every release tag (plus first commit and HEAD) with read-only git plumbing, materialises each tracked tree with the same scanner, and the union graph grows release by release (ghosts for unborn files, heartbeat pulse per landing release, final fold onto the community globe).
<!-- readmenator:memory:notes:end -->
