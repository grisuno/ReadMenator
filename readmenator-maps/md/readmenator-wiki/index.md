# Second Brain

*Last synthesized: 2026-10-12 | 151 files | 8 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 6 layers, dominant utility (83 files) across 8 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _pipeline, readmenator/parsers, readmenator: _diagrams: 18 extracted cross-community imports and 2 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (87% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 151 |
| Symbols | 2963 |
| Resolved imports | 571 |
| Languages | js, py |
| Communities | 8 |
| Doc coverage | 87% (131/151 files) |
| Security findings | 0 |
| Estimated read cost | ~81509 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _pipeline (44 files, cohesion 0.43)](./community_0_readmenator_pipeline.md)
- [readmenator/parsers (37 files, cohesion 0.53)](./community_1_readmenator_parsers.md)
- [readmenator: _diagrams (30 files, cohesion 0.40)](./community_2_readmenator_diagrams.md)
- [readmenator: _video (14 files, cohesion 0.30)](./community_3_readmenator_video.md)
- [readmenator: _flowcharts (12 files, cohesion 0.47)](./community_4_readmenator_flowcharts.md)
- [readmenator: _security (6 files, cohesion 0.21)](./community_5_readmenator_security.md)
- [readmenator: _agent_injector (5 files, cohesion 0.40)](./community_6_readmenator_agent_injector.md)
- [orphans (3 files, cohesion 0.00)](./community_7_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 206.3 |
| `readmenator/_config.py` | 196.1 |
| `readmenator/_pipeline.py` | 93.3 |
| `readmenator/_app.py` | 90.5 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 4: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 6: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 5: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 5 -> 0: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
