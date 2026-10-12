# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `readmenator/_models.py` (score: 206.30, imported by 101 files)
- `readmenator/_config.py` (score: 186.10, imported by 93 files)
- `readmenator/_pipeline.py` (score: 91.20, imported by 1 files)
- `readmenator/_app.py` (score: 86.40, imported by 14 files)
- `readmenator/parsers/__init__.py` (score: 48.20, imported by 3 files)
- `readmenator/parsers/_base.py` (score: 44.60, imported by 20 files)
- `readmenator/_forcegraph.py` (score: 36.30, imported by 9 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `readmenator/_category.py` -- 9 direct, 105 total dependents
- `readmenator/_models.py` -- 50 direct, 101 total dependents
- `readmenator/_config.py` -- 50 direct, 93 total dependents
- `readmenator/parsers/_base.py` -- 20 direct, 43 total dependents
- `readmenator/_purpose.py` -- 7 direct, 35 total dependents
- `readmenator/_rank.py` -- 11 direct, 35 total dependents
- `readmenator/_resolver.py` -- 7 direct, 33 total dependents
- `readmenator/_symindex.py` -- 7 direct, 29 total dependents
- `readmenator/_graphlayout.py` -- 5 direct, 28 total dependents
- `readmenator/_forcegraph_page.py` -- 2 direct, 26 total dependents

## Hotspots (complexity + centrality)

- `readmenator/_vendor/force-graph.min.js` -- complexity: 0.4, centrality: 1.0, combined: 0.8
- `readmenator/_diagrams.py` -- complexity: 1.0, centrality: 0.0, combined: 0.4
- `readmenator/_video.py` -- complexity: 1.0, centrality: 0.0, combined: 0.4
- `readmenator/_app.py` -- complexity: 0.9, centrality: 0.0, combined: 0.4
- `readmenator/_mcp_server.py` -- complexity: 0.7, centrality: 0.0, combined: 0.3
- `readmenator/_pipeline.py` -- complexity: 0.6, centrality: 0.1, combined: 0.3
- `readmenator/_flowcharts.py` -- complexity: 0.6, centrality: 0.0, combined: 0.2
- `readmenator/_graphrag.py` -- complexity: 0.6, centrality: 0.0, combined: 0.2
- `readmenator/_apidocs.py` -- complexity: 0.6, centrality: 0.0, combined: 0.2
- `readmenator/_apidocs_render.py` -- complexity: 0.4, centrality: 0.0, combined: 0.2

## Layer Violations

- `tests/test_apidocs.py` (testing) -> `readmenator/_apidocs_page.py` (presentation): testing must not import presentation
- `tests/test_apidocs.py` (testing) -> `readmenator/_apidocs_render.py` (presentation): testing must not import presentation
- `tests/test_components.py` (testing) -> `readmenator/_components.py` (presentation): testing must not import presentation
- `tests/test_flowcharts.py` (testing) -> `readmenator/_apidocs_page.py` (presentation): testing must not import presentation
- `tests/test_layout_quality.py` (testing) -> `readmenator/_forcegraph_page.py` (presentation): testing must not import presentation
