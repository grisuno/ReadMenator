#!/bin/bash
# Refactoring plan for tests/test_uml.py
# Current lines: 488
# Estimated impact: 0 files

set -e

# Extract 9 class symbols into tests/test_uml_classes.py
echo 'Executing: Extract 9 class symbols into tests/test_uml_classes.py'
mkdir -p $(dirname 'tests/test_uml_classes.py')
sed -n '16,477p' 'tests/test_uml.py' > 'tests/test_uml_classes.py'
sed -i '16,477d' 'tests/test_uml.py'

# Extract 40 method symbols into tests/test_uml_helpers.py
echo 'Executing: Extract 40 method symbols into tests/test_uml_helpers.py'
mkdir -p $(dirname 'tests/test_uml_helpers.py')
sed -n '19,530p' 'tests/test_uml.py' > 'tests/test_uml_helpers.py'
sed -i '19,530d' 'tests/test_uml.py'

echo 'Refactoring complete. Review changes and update imports manually.'