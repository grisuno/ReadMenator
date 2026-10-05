# Second Brain

*Last synthesized: 2026-10-04 | 110 files | 4 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (57 files) across 4 import-based communities. Recorded risk surface: 0 security findings and 3 dependency cycles.

Surprising tissue lives between readmenator (community 0), readmenator (community 1), readmenator/parsers: 2 extracted cross-community imports and 7 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (52% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 110 |
| Symbols | 1736 |
| Resolved imports | 322 |
| Languages | py, sh |
| Communities | 4 |
| Doc coverage | 52% (57/110 files) |
| Security findings | 0 |
| Estimated read cost | ~34320 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator (community 0) (69 files, cohesion 0.83)](./community_0_readmenator.md)
- [readmenator (community 1) (7 files, cohesion 0.46)](./community_1_readmenator.md)
- [readmenator/parsers (22 files, cohesion 0.68)](./community_2_readmenator_parsers.md)
- [orphans (12 files, cohesion 0.00)](./community_3_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 156.0 |
| `readmenator/_config.py` | 116.1 |
| `readmenator/_pipeline.py` | 53.3 |
| `readmenator/_app.py` | 48.6 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 2: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 3: shares_context (strength 0.5, INFERRED)
- 2 -> 3: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
