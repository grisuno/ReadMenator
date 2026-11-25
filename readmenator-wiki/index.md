# Second Brain

*Last synthesized: 2026-11-25 | 167 files | 8 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_config.py`, `_models.py`, `_app.py`. Architecturally it is 6 layers, dominant utility (91 files) across 8 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _app, readmenator/parsers, readmenator: _pipeline: 20 extracted cross-community imports and 0 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (87% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 167 |
| Symbols | 3374 |
| Resolved imports | 650 |
| Languages | js, py, sh |
| Communities | 8 |
| Doc coverage | 87% (146/167 files) |
| Security findings | 0 |
| Estimated read cost | ~94168 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _app (46 files, cohesion 0.36)](./community_0_readmenator_app.md)
- [readmenator/parsers (30 files, cohesion 0.51)](./community_1_readmenator_parsers.md)
- [readmenator: _pipeline (25 files, cohesion 0.33)](./community_2_readmenator_pipeline.md)
- [readmenator: _diagrams (20 files, cohesion 0.41)](./community_3_readmenator_diagrams.md)
- [readmenator: _mcp_server (15 files, cohesion 0.32)](./community_4_readmenator_mcp_server.md)
- [readmenator: _flowcharts (14 files, cohesion 0.41)](./community_5_readmenator_flowcharts.md)
- [readmenator: _video (13 files, cohesion 0.29)](./community_6_readmenator_video.md)
- [orphans (4 files, cohesion 0.00)](./community_7_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_config.py` | 220.1 |
| `readmenator/_models.py` | 206.3 |
| `readmenator/_app.py` | 103.0 |
| `readmenator/_pipeline.py` | 97.5 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 3: depends_on (strength 0.9, EXTRACTED)
- 4 -> 2: depends_on (strength 0.9, EXTRACTED)
- 4 -> 5: depends_on (strength 0.9, EXTRACTED)
- 4 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 6: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 5 -> 0: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
