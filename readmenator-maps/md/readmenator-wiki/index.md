# Second Brain

*Last synthesized: 2026-10-07 | 107 files | 6 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_models.py`, `_config.py`, `_pipeline.py`. Architecturally it is 5 layers, dominant utility (58 files) across 6 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between readmenator: _security, readmenator/parsers, readmenator: _pipeline: 10 extracted cross-community imports and 10 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (81% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 107 |
| Symbols | 1909 |
| Resolved imports | 364 |
| Languages | py |
| Communities | 6 |
| Doc coverage | 81% (87/107 files) |
| Security findings | 0 |
| Estimated read cost | ~41484 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target ReadMenator
```

## Concept Wiki

- [readmenator: _security (29 files, cohesion 0.34)](./community_0_readmenator_security.md)
- [readmenator/parsers (26 files, cohesion 0.56)](./community_1_readmenator_parsers.md)
- [readmenator: _pipeline (19 files, cohesion 0.39)](./community_2_readmenator_pipeline.md)
- [readmenator: _diagrams (18 files, cohesion 0.35)](./community_3_readmenator_diagrams.md)
- [readmenator: _agent_output (13 files, cohesion 0.34)](./community_4_readmenator_agent_output.md)
- [orphans (2 files, cohesion 0.00)](./community_5_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `readmenator/_models.py` | 164.3 |
| `readmenator/_config.py` | 126.1 |
| `readmenator/_pipeline.py` | 57.5 |
| `readmenator/_app.py` | 57.1 |
| `readmenator/parsers/__init__.py` | 48.2 |

## Strongest Connections

- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 3 -> 4: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 4: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
