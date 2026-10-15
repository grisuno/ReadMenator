# `deploy.sh`

> Source: [deploy.sh:1](../../deploy.sh#L1) | language `sh` | coverage 100.0% | [API index](../index.md)

deploy.sh -- one-liner deploy via deploynator (generic per-repo script).

Deployed by deploynator: detects its own directory, ensures tooling, then releases this repo. Usage: ./deploy.sh                    # patch release (smallest bump) ./deploy.sh feat --dry-run     # preview a minor release ./deploy.sh fix --no-test      # patch release skipping tests

## Contents

- **Functions:** [`ensure_pkg`](#ensure_pkg)

## Functions

<a id="ensure_pkg"></a>

### `ensure_pkg`

`function` | [deploy.sh:22](../../deploy.sh#L22)

```bash
ensure_pkg()
```

Install or update one package (best effort: works offline with current versions, on PEP 668 systems, and before the PyPI upload via git fallback).

---
