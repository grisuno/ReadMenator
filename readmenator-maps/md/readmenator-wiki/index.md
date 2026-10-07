# Second Brain

*Last synthesized: 2026-10-07 | 105 files | 8 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (57 files) across 8 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _diagrams, tests: _agent_injector, readmenator: _agent_output: 14 extracted cross-community imports and 6 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (82% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 105 |
| Symbols | 1852 |
| Resolved imports | 348 |
| Languages | py |
| Communities | 8 |
| Doc coverage | 82% (86/105 files) |
| Security findings | 0 |
| Estimated read cost | ~39544 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _diagrams (50 files, cohesion 0.55)](./community_0_readmenator_diagrams.md)
- [tests: _agent_injector (3 files, cohesion 0.29)](./community_1_tests_agent_injector.md)
- [readmenator: _agent_output (10 files, cohesion 0.35)](./community_2_readmenator_agent_output.md)
- [readmenator: _category (5 files, cohesion 0.42)](./community_3_readmenator_category.md)
- [readmenator: _documentation (4 files, cohesion 0.23)](./community_4_readmenator_documentation.md)
- [readmenator/parsers (26 files, cohesion 0.56)](./community_5_readmenator_parsers.md)
- [tests: _scanner (5 files, cohesion 0.21)](./community_6_tests_scanner.md)
- [orphans (2 files, cohesion 0.00)](./community_7_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 160.0 |
| `readmenator/_config.py` | 122.1 |
| `readmenator/_pipeline.py` | 55.4 |
| `readmenator/_app.py` | 53.0 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 0 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 5: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 5: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 5: depends_on (strength 0.9, EXTRACTED)
- 4 -> 3: depends_on (strength 0.9, EXTRACTED)
- 5 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 6: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
