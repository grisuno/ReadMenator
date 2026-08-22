#!/bin/bash
# Refactoring plan for readmenator/_exporter.py
# Current lines: 898
# Estimated impact: 2 files

set -e

# Extract 14 method symbols into readmenator/_exporter_helpers.py
echo 'Executing: Extract 14 method symbols into readmenator/_exporter_helpers.py'
mkdir -p $(dirname 'readmenator/_exporter_helpers.py')
sed -n '29,867p' 'readmenator/_exporter.py' > 'readmenator/_exporter_helpers.py'
sed -i '29,867d' 'readmenator/_exporter.py'

echo 'Refactoring complete. Review changes and update imports manually.'