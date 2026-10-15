# Second Brain

*Last synthesized: 2026-10-14 | 154 files | 8 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 6 layers, dominant utility (83 files) across 8 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _video, readmenator/parsers, readmenator: _agent_output: 20 extracted cross-community imports and 0 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (87% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 154 |
| Symbols | 3028 |
| Resolved imports | 611 |
| Languages | js, py |
| Communities | 8 |
| Doc coverage | 87% (134/154 files) |
| Security findings | 0 |
| Estimated read cost | ~83897 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _video (35 files, cohesion 0.30)](./community_0_readmenator_video.md)
- [readmenator/parsers (35 files, cohesion 0.52)](./community_1_readmenator_parsers.md)
- [readmenator: _agent_output (19 files, cohesion 0.33)](./community_2_readmenator_agent_output.md)
- [readmenator: _graphrag (18 files, cohesion 0.32)](./community_3_readmenator_graphrag.md)
- [readmenator: _pipeline (17 files, cohesion 0.26)](./community_4_readmenator_pipeline.md)
- [readmenator: _diagrams (15 files, cohesion 0.39)](./community_5_readmenator_diagrams.md)
- [readmenator: _flowcharts (12 files, cohesion 0.44)](./community_6_readmenator_flowcharts.md)
- [orphans (3 files, cohesion 0.00)](./community_7_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 206.3 |
| `readmenator/_config.py` | 200.1 |
| `readmenator/_pipeline.py` | 93.3 |
| `readmenator/_app.py` | 92.7 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 5: depends_on (strength 0.9, EXTRACTED)
- 3 -> 6: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 4: depends_on (strength 0.9, EXTRACTED)
- 0 -> 5: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 1: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
