#!/bin/bash
# Refactoring plan for tests/test_parsers.py
# Current lines: 487
# Estimated impact: 0 files

set -e

# Extract 14 class symbols into tests/test_parsers_classes.py
echo 'Executing: Extract 14 class symbols into tests/test_parsers_classes.py'
mkdir -p $(dirname 'tests/test_parsers_classes.py')
sed -n '22,510p' 'tests/test_parsers.py' > 'tests/test_parsers_classes.py'
sed -i '22,510d' 'tests/test_parsers.py'

# Extract 70 method symbols into tests/test_parsers_helpers.py
echo 'Executing: Extract 70 method symbols into tests/test_parsers_helpers.py'
mkdir -p $(dirname 'tests/test_parsers_helpers.py')
sed -n '23,534p' 'tests/test_parsers.py' > 'tests/test_parsers_helpers.py'
sed -i '23,534d' 'tests/test_parsers.py'

echo 'Refactoring complete. Review changes and update imports manually.'