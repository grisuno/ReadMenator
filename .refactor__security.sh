#!/bin/bash
# Refactoring plan for readmenator/_security.py
# Current lines: 583
# Estimated impact: 2 files

set -e

# Extract 2 class symbols into readmenator/_security_classes.py
echo 'Executing: Extract 2 class symbols into readmenator/_security_classes.py'
mkdir -p $(dirname 'readmenator/_security_classes.py')
sed -n '24,536p' 'readmenator/_security.py' > 'readmenator/_security_classes.py'
sed -i '24,536d' 'readmenator/_security.py'

# Extract 29 method symbols into readmenator/_security_helpers.py
echo 'Executing: Extract 29 method symbols into readmenator/_security_helpers.py'
mkdir -p $(dirname 'readmenator/_security_helpers.py')
sed -n '46,622p' 'readmenator/_security.py' > 'readmenator/_security_helpers.py'
sed -i '46,622d' 'readmenator/_security.py'

echo 'Refactoring complete. Review changes and update imports manually.'