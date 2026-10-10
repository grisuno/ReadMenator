# Second Brain

*Last synthesized: 2026-10-10 | 128 files | 7 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 6 layers, dominant utility (72 files) across 7 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _agent_output, readmenator/parsers, readmenator: _pipeline: 14 extracted cross-community imports and 6 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (84% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 128 |
| Symbols | 2412 |
| Resolved imports | 451 |
| Languages | js, py |
| Communities | 7 |
| Doc coverage | 84% (108/128 files) |
| Security findings | 0 |
| Estimated read cost | ~60855 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _agent_output (38 files, cohesion 0.40)](./community_0_readmenator_agent_output.md)
- [readmenator/parsers (28 files, cohesion 0.53)](./community_1_readmenator_parsers.md)
- [readmenator: _pipeline (23 files, cohesion 0.35)](./community_2_readmenator_pipeline.md)
- [readmenator: _diagrams (22 files, cohesion 0.33)](./community_3_readmenator_diagrams.md)
- [readmenator: _graphrag (9 files, cohesion 0.36)](./community_4_readmenator_graphrag.md)
- [readmenator: _agent_injector (5 files, cohesion 0.40)](./community_5_readmenator_agent_injector.md)
- [orphans (3 files, cohesion 0.00)](./community_6_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 184.3 |
| `readmenator/_config.py` | 156.1 |
| `readmenator/_pipeline.py` | 78.6 |
| `readmenator/_app.py` | 71.3 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 3 -> 4: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 5: depends_on (strength 0.9, EXTRACTED)
- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 4: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
