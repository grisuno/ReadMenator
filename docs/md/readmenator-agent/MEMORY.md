# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 151 files at commit `ba552ee3474a`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: A token-free, offline, production-grade polyglot codebase knowledge graph & architectural analyzer. (`README.md:7`)
- Domain vocabulary (term, files): `readmenator` (101), `file` (90), `graph` (72), `node` (67), `files` (66), `symbols` (61), `edges` (59), `project` (56), `imports` (56), `nodes` (55), `build` (54), `symbol` (53), `all` (53), `set` (52), `import` (51)
- Subsystem `readmenator: _pipeline`: 44 files, core `readmenator/_pipeline.py`: AnalyzerFactory (lazy component construction) and DeepAnalysisRunner.
- Subsystem `readmenator/parsers`: 37 files, core `readmenator/_models.py`: Data model types for the readmenator knowledge graph.
- Subsystem `readmenator: _diagrams`: 30 files, core `readmenator/_diagrams.py`: Self-contained interactive system maps for the knowledge graph.
- Subsystem `readmenator: _video`: 14 files, core `readmenator/_video.py`: Cinematic codebase overview video, general purpose.
- Subsystem `readmenator: _flowcharts`: 12 files, core `readmenator/_flowcharts.py`: Architecture and execution-flow Mermaid diagrams from static structure.
- Subsystem `readmenator: _security`: 6 files, core `readmenator/_security.py`: Pattern-based static security analysis for the readmenator knowledge graph.
- Subsystem `readmenator: _agent_injector`: 5 files, core `readmenator/_agent_injector.py`: Injects KNOWLEDGE_BASE.md references into AI agent instruction files.
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
- Config is the single source of truth for all constants (`CLAUDE.md:827`)
- Symbol creation logic is not duplicated across parsers (`CLAUDE.md:828`)
- Docstring extraction lives once in LanguageParser base class (`CLAUDE.md:829`)
- File-level doc extraction lives once in PolyglotScanner (`CLAUDE.md:830`)
- All analysis thresholds in Config, never hardcoded (`CLAUDE.md:831`)
- Single Responsibility: each module has one job (`CLAUDE.md:834`)
- Open/Closed: add parsers/analyzers without modifying existing code (`CLAUDE.md:835`)
- Liskov Substitution: all parsers inherit from LanguageParser (`CLAUDE.md:836`)
- Interface Segregation: each contract exposes minimal surface (`CLAUDE.md:837`)
- Dependency Inversion: app depends on abstractions (Config, Scanner) (`CLAUDE.md:838`)
- No absolute paths in source code (`CLAUDE.md:841`)
- No network calls from the core scanner (`CLAUDE.md:842`)
- Symlinks rejected (`CLAUDE.md:843`)
- File size limits enforced (`CLAUDE.md:844`)
- Directory depth limits enforced (`CLAUDE.md:845`)
- All parsing exceptions caught (`CLAUDE.md:846`)
- No external API calls in any analysis or export module (`CLAUDE.md:847`)
- Pattern-based security analyzer with 18 language rule sets (`CLAUDE.md:848`)
- Privacy mode strips source snippets from output (`CLAUDE.md:849`)
- Fix any security issues found (symlinks, path traversal, size limits) (`CLAUDE.md:878`)
- Remove hardcoded values and move to Config if they are tuneable (`CLAUDE.md:879`)
- Update tests to cover new behaviors (`CLAUDE.md:880`)
- Keep the "Classs" pluralization fix intact (`CLAUDE.md:881`)
- Do not add absolute paths (`CLAUDE.md:882`)
- Do not add external dependencies to the core scanner (`CLAUDE.md:883`)
- Maintain backward compatibility of the CLI interface (`CLAUDE.md:884`)
- Update this CLAUDE.md and README.md for any contract changes (`CLAUDE.md:885`)
- Fix inline imports (move to top of file) (`CLAUDE.md:886`)
- Add type annotations to all function signatures (`CLAUDE.md:887`)
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
- Dependency cycles: 0; layer violations: 6 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- All progress/report messages use `logging.getLogger(__name__)` (never `print()`) (`CLAUDE.md:852`)
- User-facing output (query results, summaries) uses `print()` to stdout (`CLAUDE.md:853`)
- Logging format configured in `__main__.py` via `logging.basicConfig` (`CLAUDE.md:854`)
- Each module gets its own logger via `logger = logging.getLogger(__name__)` (`CLAUDE.md:855`)

Measured baseline:
- py: 150 files, 2928 symbols; docstrings on 55% of symbols; functions snake_case (96%); types PascalCase (100%); median file 202 lines, max 4062.
- js: 1 files, 35 symbols; docstrings on 100% of symbols; functions snake_case (80%); types PascalCase (40%); median file 5 lines, max 5.
- Tests: 54 files under tests; follow the existing naming (e.g. `test_agent_friendliness.py`).

## 5. Minimum deliverables

Declared:
- Tests named as `test_<contract>_<behavior>` (BDD style) (`CLAUDE.md:858`)
- Each module has its own test class (`CLAUDE.md:859`)
- Security behaviors tested explicitly (`CLAUDE.md:860`)
- Edge cases tested (empty files, syntax errors, symlinks) (`CLAUDE.md:861`)
- Integration tests validate end-to-end pipeline (`CLAUDE.md:862`)
- "Classs" regression test prevents re-introduction (`CLAUDE.md:863`)
- All new modules have complete contract test suites (`CLAUDE.md:864`)
- Mutation check after SDD+TDD+BDD: introduce one-line mutants (validation bypass, escaping bypass, ordering change); a killed mutant fails at least one test, a surviving mutant requires a stronger test before refactor (`CLAUDE.md:865`)
- Property-based parser tests skip cleanly when hypothesis is not installed (inert strategy placeholders, identity decorators) (`CLAUDE.md:866`)
- English only, no emojis, no prose comments, docstrings on every public and private function (`CLAUDE.md:869`)
- DRY and SOLID, one self-contained file per contract, production code with no placeholders or simplifications (`CLAUDE.md:870`)
- No hardcoded tuneables or magic numbers: every setting lives in Config (`CLAUDE.md:871`)
- No absolute paths, no network calls from analysis or export modules, all untrusted text escaped at the boundary (`CLAUDE.md:872`)
- Boy scout: any technical debt or security flaw found during the change is fixed without losing functionality (`CLAUDE.md:873`)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 55%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `readmenator/_models.py`, `readmenator/_config.py`, `readmenator/_pipeline.py`, `readmenator/_app.py`, `readmenator/parsers/__init__.py`
- Hotspots (complex and central): `readmenator/_vendor/force-graph.min.js`, `readmenator/_diagrams.py`, `readmenator/_video.py`, `readmenator/_app.py`, `tests/test_parsers.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
<!-- readmenator:memory:notes:end -->
