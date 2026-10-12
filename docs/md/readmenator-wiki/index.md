# Second Brain

*Last synthesized: 2026-10-12 | 149 files | 7 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 6 layers, dominant utility (82 files) across 7 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _graphrag, readmenator/parsers, readmenator: _diagrams: 15 extracted cross-community imports and 5 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (87% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 149 |
| Symbols | 2934 |
| Resolved imports | 559 |
| Languages | js, py |
| Communities | 7 |
| Doc coverage | 87% (129/149 files) |
| Security findings | 0 |
| Estimated read cost | ~80632 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _graphrag (38 files, cohesion 0.38)](./community_0_readmenator_graphrag.md)
- [readmenator/parsers (34 files, cohesion 0.52)](./community_1_readmenator_parsers.md)
- [readmenator: _diagrams (29 files, cohesion 0.38)](./community_2_readmenator_diagrams.md)
- [readmenator: _pipeline (20 files, cohesion 0.28)](./community_3_readmenator_pipeline.md)
- [readmenator: _graphlayout (13 files, cohesion 0.38)](./community_4_readmenator_graphlayout.md)
- [readmenator: _flowcharts (12 files, cohesion 0.47)](./community_5_readmenator_flowcharts.md)
- [orphans (3 files, cohesion 0.00)](./community_6_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 206.3 |
| `readmenator/_config.py` | 192.1 |
| `readmenator/_pipeline.py` | 91.2 |
| `readmenator/_app.py` | 88.4 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 5: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 5 -> 0: depends_on (strength 0.9, EXTRACTED)
- 5 -> 1: depends_on (strength 0.9, EXTRACTED)
- 5 -> 4: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
