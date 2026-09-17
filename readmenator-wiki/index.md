# Second Brain

*Last synthesized: 2026-09-17 | 108 files | 3 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (56 files) across 3 import-based communities. Recorded risk surface: 0 security findings and 3 dependency cycles.

Surprising tissue lives between readmenator (community 0), readmenator (community 1), orphans: 1 extracted cross-community imports and 7 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (51% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 108 |
| Symbols | 1661 |
| Resolved imports | 314 |
| Languages | py, sh |
| Communities | 3 |
| Doc coverage | 51% (55/108 files) |
| Security findings | 0 |
| Estimated read cost | ~32221 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator (community 0) (93 files, cohesion 0.99)](./community_0_readmenator.md)
- [readmenator (community 1) (3 files, cohesion 0.40)](./community_1_readmenator.md)
- [orphans (12 files, cohesion 0.00)](./community_2_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 152.0 |
| `readmenator/_config.py` | 112.1 |
| `readmenator/_pipeline.py` | 51.2 |
| `readmenator/parsers/__init__.py` | 48.2 |
| `readmenator/parsers/_base.py` | 44.6 |

## Strongest Connections

- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.6, INFERRED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 1 -> 0: bridges (strength 0.5, INFERRED)
- 0 -> 2: shares_context (strength 0.5, INFERRED)
- 1 -> 2: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
