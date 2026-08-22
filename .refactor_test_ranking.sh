#!/bin/bash
# Refactoring plan for tests/test_ranking.py
# Current lines: 666
# Estimated impact: 0 files

set -e

# Extract 12 class symbols into tests/test_ranking_classes.py
echo 'Executing: Extract 12 class symbols into tests/test_ranking_classes.py'
mkdir -p $(dirname 'tests/test_ranking_classes.py')
sed -n '60,637p' 'tests/test_ranking.py' > 'tests/test_ranking_classes.py'
sed -i '60,637d' 'tests/test_ranking.py'

# Extract 60 method symbols into tests/test_ranking_helpers.py
echo 'Executing: Extract 60 method symbols into tests/test_ranking_helpers.py'
mkdir -p $(dirname 'tests/test_ranking_helpers.py')
sed -n '61,687p' 'tests/test_ranking.py' > 'tests/test_ranking_helpers.py'
sed -i '61,687d' 'tests/test_ranking.py'

echo 'Refactoring complete. Review changes and update imports manually.'