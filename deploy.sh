#!/bin/bash
# deploy.sh -- one-liner deploy via deploynator (generic per-repo script).
# Deployed by deploynator: detects its own directory, ensures tooling,
# then releases this repo. Usage:
#   ./deploy.sh                    # patch release (smallest bump)
#   ./deploy.sh feat --dry-run     # preview a minor release
#   ./deploy.sh fix --no-test      # patch release skipping tests
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TYPE="patch"
if [ $# -gt 0 ]; then
    TYPE="$1"
    shift
fi

PIP_BIN="pip"
command -v pip >/dev/null 2>&1 || PIP_BIN="pip3"

# Install or update one package (best effort: works offline with current versions,
# on PEP 668 systems, and before the PyPI upload via git fallback).
ensure_pkg() {
    if python3 -c "import $1" 2>/dev/null; then
        "$PIP_BIN" install -U "$2" 2>/dev/null || true
    else
        "$PIP_BIN" install "$2" 2>/dev/null \
            || "$PIP_BIN" install "$3" 2>/dev/null \
            || "$PIP_BIN" install --break-system-packages "$2" 2>/dev/null \
            || "$PIP_BIN" install --break-system-packages "$3" 2>/dev/null \
            || true
    fi
}

ensure_pkg deploynator deploynator "git+https://github.com/grisuno/deploynator.git"
ensure_pkg readmenator readmenator readmenator

if ! python3 -c "import deploynator" 2>/dev/null; then
    echo "[!] deploynator not available and install failed (offline?)." >&2
    exit 1
fi

exec python3 -m deploynator release --type "$TYPE" --project "$DIR" "$@"
