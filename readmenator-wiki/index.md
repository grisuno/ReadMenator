# Second Brain

*Last synthesized: 2026-10-07 | 115 files | 3 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (60 files) across 3 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator, readmenator/parsers, orphans: 1 extracted cross-community imports and 6 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (83% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 115 |
| Symbols | 1852 |
| Resolved imports | 348 |
| Languages | py, sh |
| Communities | 3 |
| Doc coverage | 83% (96/115 files) |
| Security findings | 0 |
| Estimated read cost | ~39428 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator (81 files, cohesion 0.90)](./community_0_readmenator.md)
- [readmenator/parsers (22 files, cohesion 0.68)](./community_1_readmenator_parsers.md)
- [orphans (12 files, cohesion 0.00)](./community_2_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 160.0 |
| `readmenator/_config.py` | 122.1 |
| `readmenator/_pipeline.py` | 55.4 |
| `readmenator/_app.py` | 53.0 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 1 -> 2: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
