# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `readmenator/_models.py` (score: 196.30, imported by 96 files)
- `readmenator/_config.py` (score: 172.10, imported by 86 files)
- `readmenator/_pipeline.py` (score: 87.00, imported by 1 files)
- `readmenator/_app.py` (score: 73.50, imported by 12 files)
- `readmenator/parsers/__init__.py` (score: 48.20, imported by 3 files)
- `readmenator/parsers/_base.py` (score: 44.60, imported by 20 files)
- `readmenator/_forcegraph.py` (score: 34.20, imported by 8 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `readmenator/_category.py` -- 9 direct, 99 total dependents
- `readmenator/_models.py` -- 50 direct, 96 total dependents
- `readmenator/_config.py` -- 50 direct, 86 total dependents
- `readmenator/parsers/_base.py` -- 20 direct, 41 total dependents
- `readmenator/_purpose.py` -- 7 direct, 32 total dependents
- `readmenator/_rank.py` -- 11 direct, 32 total dependents
- `readmenator/_resolver.py` -- 7 direct, 30 total dependents
- `readmenator/_graphlayout.py` -- 4 direct, 25 total dependents
- `readmenator/_forcegraph_page.py` -- 1 direct, 23 total dependents
- `readmenator/_sourceview.py` -- 4 direct, 23 total dependents

## Hotspots (complexity + centrality)

- `readmenator/_vendor/force-graph.min.js` -- complexity: 0.4, centrality: 1.0, combined: 0.8
- `readmenator/_diagrams.py` -- complexity: 1.0, centrality: 0.0, combined: 0.4
- `readmenator/_app.py` -- complexity: 0.8, centrality: 0.0, combined: 0.3
- `readmenator/_video.py` -- complexity: 0.8, centrality: 0.0, combined: 0.3
- `readmenator/_mcp_server.py` -- complexity: 0.7, centrality: 0.0, combined: 0.3
- `readmenator/_pipeline.py` -- complexity: 0.5, centrality: 0.0, combined: 0.2
- `readmenator/_graphrag.py` -- complexity: 0.6, centrality: 0.0, combined: 0.2
- `readmenator_orchestrator.py` -- complexity: 0.4, centrality: 0.0, combined: 0.2
- `readmenator/_agent_output.py` -- complexity: 0.4, centrality: 0.0, combined: 0.2
- `readmenator/_wiki.py` -- complexity: 0.4, centrality: 0.0, combined: 0.1

## Layer Violations

- `tests/test_components.py` (testing) -> `readmenator/_components.py` (presentation): testing must not import presentation
