#!/bin/bash
# Refactoring plan for readmenator/_rank.py
# Current lines: 537
# Estimated impact: 7 files

set -e

# Extract 4 class symbols into readmenator/_rank_classes.py
echo 'Executing: Extract 4 class symbols into readmenator/_rank_classes.py'
mkdir -p $(dirname 'readmenator/_rank_classes.py')
sed -n '32,427p' 'readmenator/_rank.py' > 'readmenator/_rank_classes.py'
sed -i '32,427d' 'readmenator/_rank.py'

# Extract 13 method symbols into readmenator/_rank_helpers.py
echo 'Executing: Extract 13 method symbols into readmenator/_rank_helpers.py'
mkdir -p $(dirname 'readmenator/_rank_helpers.py')
sed -n '61,562p' 'readmenator/_rank.py' > 'readmenator/_rank_helpers.py'
sed -i '61,562d' 'readmenator/_rank.py'

echo 'Refactoring complete. Review changes and update imports manually.'