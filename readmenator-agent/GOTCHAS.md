# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `readmenator/_models.py` (score: 143.90)
- `readmenator/_config.py` (score: 104.10)
- `readmenator/parsers/__init__.py` (score: 48.20)
- `readmenator/_pipeline.py` (score: 47.00)
- `readmenator/parsers/_base.py` (score: 44.60)
- `readmenator/_app.py` (score: 44.20)
- `tests/test_parsers_property.py` (score: 42.70)
- `readmenator/_mcp_server.py` (score: 21.20)
- `readmenator/_diagrams.py` (score: 18.70)
- `readmenator/_documentation.py` (score: 18.70)

## Hotspots (complexity + centrality)

- `readmenator/_models.py` -- complexity: 0.2, centrality: 1.0, combined: 0.7
- `tests/test_diagrams.py` -- complexity: 0.8, centrality: 0.4, combined: 0.6
- `readmenator/_app.py` -- complexity: 0.5, centrality: 0.5, combined: 0.5
- `readmenator/_pipeline.py` -- complexity: 0.4, centrality: 0.5, combined: 0.5
- `tests/test_parsers_property.py` -- complexity: 0.3, centrality: 0.5, combined: 0.5
- `tests/test_parsers.py` -- complexity: 1.0, centrality: 0.1, combined: 0.4
- `tests/test_ranking.py` -- complexity: 0.8, centrality: 0.2, combined: 0.4
- `readmenator/_diagrams.py` -- complexity: 0.8, centrality: 0.2, combined: 0.4
- `tests/test_agent_output.py` -- complexity: 0.5, centrality: 0.4, combined: 0.4
- `readmenator/_config.py` -- complexity: 0.0, centrality: 0.7, combined: 0.4

## Dependency Cycles

Circular dependencies. Refactor to break the cycle.

- `readmenator/_app.py` -> `readmenator/_pipeline.py` -> `readmenator/_agent_injector.py` -> `readmenator.py` -> `readmenator/__main__.py` -> `readmenator/_mcp_server.py`
- `readmenator/_app.py` -> `readmenator/_pipeline.py` -> `readmenator/_agent_injector.py` -> `readmenator.py` -> `readmenator/__main__.py`
- `readmenator/_models.py` -> `readmenator/_category.py`
