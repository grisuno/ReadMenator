#!/bin/bash
# Refactoring plan for readmenator/_documentation.py
# Current lines: 1087
# Estimated impact: 2 files

set -e

# Extract 26 method symbols into readmenator/_documentation_helpers.py
echo 'Executing: Extract 26 method symbols into readmenator/_documentation_helpers.py'
mkdir -p $(dirname 'readmenator/_documentation_helpers.py')
sed -n '39,1078p' 'readmenator/_documentation.py' > 'readmenator/_documentation_helpers.py'
sed -i '39,1078d' 'readmenator/_documentation.py'

echo 'Refactoring complete. Review changes and update imports manually.'