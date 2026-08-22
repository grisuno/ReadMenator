#!/bin/bash
# Refactoring plan for readmenator/_mcp_server.py
# Current lines: 813
# Estimated impact: 3 files

set -e

# Extract 5 class symbols into readmenator/_mcp_server_classes.py
echo 'Executing: Extract 5 class symbols into readmenator/_mcp_server_classes.py'
mkdir -p $(dirname 'readmenator/_mcp_server_classes.py')
sed -n '58,196p' 'readmenator/_mcp_server.py' > 'readmenator/_mcp_server_classes.py'
sed -i '58,196d' 'readmenator/_mcp_server.py'

# Extract 47 method symbols into readmenator/_mcp_server_helpers.py
echo 'Executing: Extract 47 method symbols into readmenator/_mcp_server_helpers.py'
mkdir -p $(dirname 'readmenator/_mcp_server_helpers.py')
sed -n '59,846p' 'readmenator/_mcp_server.py' > 'readmenator/_mcp_server_helpers.py'
sed -i '59,846d' 'readmenator/_mcp_server.py'

echo 'Refactoring complete. Review changes and update imports manually.'