# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `readmenator/_models.py` (score: 184.30, imported by 90 files)
- `readmenator/_config.py` (score: 156.10, imported by 78 files)
- `readmenator/_pipeline.py` (score: 78.60, imported by 1 files)
- `readmenator/_app.py` (score: 71.30, imported by 11 files)
- `readmenator/parsers/__init__.py` (score: 48.20, imported by 3 files)
- `readmenator/parsers/_base.py` (score: 44.60, imported by 20 files)
- `readmenator/_forcegraph.py` (score: 30.20, imported by 7 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `readmenator/_category.py` -- 9 direct, 94 total dependents
- `readmenator/_models.py` -- 50 direct, 90 total dependents
- `readmenator/_config.py` -- 50 direct, 78 total dependents
- `readmenator/parsers/_base.py` -- 20 direct, 40 total dependents
- `readmenator/_purpose.py` -- 6 direct, 29 total dependents
- `readmenator/_rank.py` -- 10 direct, 29 total dependents
- `readmenator/_resolver.py` -- 7 direct, 28 total dependents
- `readmenator/_graphlayout.py` -- 4 direct, 23 total dependents
- `readmenator/_forcegraph_page.py` -- 1 direct, 21 total dependents
- `readmenator/parsers/_c.py` -- 2 direct, 21 total dependents

## Hotspots (complexity + centrality)

- `readmenator/_vendor/force-graph.min.js` -- complexity: 0.4, centrality: 1.0, combined: 0.8
- `readmenator/_diagrams.py` -- complexity: 1.0, centrality: 0.0, combined: 0.4
- `readmenator/_video.py` -- complexity: 0.8, centrality: 0.0, combined: 0.3
- `readmenator/_app.py` -- complexity: 0.8, centrality: 0.0, combined: 0.3
- `readmenator/_mcp_server.py` -- complexity: 0.7, centrality: 0.0, combined: 0.3
- `readmenator/_graphrag.py` -- complexity: 0.6, centrality: 0.0, combined: 0.2
- `readmenator/_pipeline.py` -- complexity: 0.5, centrality: 0.0, combined: 0.2
- `readmenator_orchestrator.py` -- complexity: 0.4, centrality: 0.0, combined: 0.2
- `readmenator/_agent_output.py` -- complexity: 0.4, centrality: 0.0, combined: 0.2
- `readmenator/_wiki.py` -- complexity: 0.4, centrality: 0.0, combined: 0.1
