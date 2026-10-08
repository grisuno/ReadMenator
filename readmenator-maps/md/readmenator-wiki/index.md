# Second Brain

*Last synthesized: 2026-10-08 | 117 files | 6 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (67 files) across 6 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _pipeline, readmenator/parsers, readmenator: _diagrams: 10 extracted cross-community imports and 10 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (83% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 117 |
| Symbols | 2107 |
| Resolved imports | 406 |
| Languages | js, py |
| Communities | 6 |
| Doc coverage | 83% (97/117 files) |
| Security findings | 0 |
| Estimated read cost | ~48374 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _pipeline (37 files, cohesion 0.45)](./community_0_readmenator_pipeline.md)
- [readmenator/parsers (28 files, cohesion 0.55)](./community_1_readmenator_parsers.md)
- [readmenator: _diagrams (27 files, cohesion 0.44)](./community_2_readmenator_diagrams.md)
- [readmenator: _agent_output (17 files, cohesion 0.36)](./community_3_readmenator_agent_output.md)
- [readmenator: _agent_injector (5 files, cohesion 0.40)](./community_4_readmenator_agent_injector.md)
- [orphans (3 files, cohesion 0.00)](./community_5_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 176.3 |
| `readmenator/_config.py` | 142.1 |
| `readmenator/_pipeline.py` | 70.1 |
| `readmenator/_app.py` | 64.2 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 4: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 4: depends_on (strength 0.9, EXTRACTED)
- 4 -> 3: depends_on (strength 0.9, EXTRACTED)
- 4 -> 1: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
