# Recipe: Fix a Dependency Cycle

Target cycle: `readmenator/_app.py` -> `readmenator/_pipeline.py` -> `readmenator/_agent_injector.py` -> `readmenator.py` -> `readmenator/__main__.py` -> `readmenator/_mcp_server.py` -> `readmenator/_app.py`

1. Read the imports between these files: `grep -n '^import\|^from\|#include' readmenator/_app.py`, `grep -n '^import\|^from\|#include' readmenator/_pipeline.py`, `grep -n '^import\|^from\|#include' readmenator/_agent_injector.py`, `grep -n '^import\|^from\|#include' readmenator.py`, `grep -n '^import\|^from\|#include' readmenator/__main__.py`, `grep -n '^import\|^from\|#include' readmenator/_mcp_server.py`
2. Move the shared symbols into a new leaf module both sides import
3. Verify: `readmenator . && grep -c 'Dependency Cycles' readmenator-agent/GOTCHAS.md`
