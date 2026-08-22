#!/bin/bash
# Refactoring plan for readmenator/_uml.py
# Current lines: 599
# Estimated impact: 4 files

set -e

# Extract 24 method symbols into readmenator/_uml_helpers.py
echo 'Executing: Extract 24 method symbols into readmenator/_uml_helpers.py'
mkdir -p $(dirname 'readmenator/_uml_helpers.py')
sed -n '34,640p' 'readmenator/_uml.py' > 'readmenator/_uml_helpers.py'
sed -i '34,640d' 'readmenator/_uml.py'

echo 'Refactoring complete. Review changes and update imports manually.'