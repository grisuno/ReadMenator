# Second Brain

*Last synthesized: 2026-10-08 | 124 files | 7 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (71 files) across 7 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _agent_output, readmenator/parsers, readmenator: _diagrams: 14 extracted cross-community imports and 6 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (84% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 124 |
| Symbols | 2305 |
| Resolved imports | 436 |
| Languages | js, py |
| Communities | 7 |
| Doc coverage | 84% (104/124 files) |
| Security findings | 0 |
| Estimated read cost | ~56023 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _agent_output (38 files, cohesion 0.41)](./community_0_readmenator_agent_output.md)
- [readmenator/parsers (28 files, cohesion 0.54)](./community_1_readmenator_parsers.md)
- [readmenator: _diagrams (20 files, cohesion 0.33)](./community_2_readmenator_diagrams.md)
- [readmenator: _pipeline (17 files, cohesion 0.31)](./community_3_readmenator_pipeline.md)
- [readmenator: _video (13 files, cohesion 0.36)](./community_4_readmenator_video.md)
- [readmenator: _agent_injector (5 files, cohesion 0.40)](./community_5_readmenator_agent_injector.md)
- [orphans (3 files, cohesion 0.00)](./community_6_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 182.3 |
| `readmenator/_config.py` | 152.1 |
| `readmenator/_pipeline.py` | 76.5 |
| `readmenator/_app.py` | 67.1 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 2 -> 4: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 5: depends_on (strength 0.9, EXTRACTED)
- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 4: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
