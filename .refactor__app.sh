#!/bin/bash
# Refactoring plan for readmenator/_app.py
# Current lines: 643
# Estimated impact: 5 files

set -e

# Extract 36 method symbols into readmenator/_app_helpers.py
echo 'Executing: Extract 36 method symbols into readmenator/_app_helpers.py'
mkdir -p $(dirname 'readmenator/_app_helpers.py')
sed -n '34,679p' 'readmenator/_app.py' > 'readmenator/_app_helpers.py'
sed -i '34,679d' 'readmenator/_app.py'

echo 'Refactoring complete. Review changes and update imports manually.'