# `readmenator._gitmeta`

> Source: [readmenator/_gitmeta.py:1](../../readmenator/_gitmeta.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Read-only git metadata for freshness stamps on generated documents.

Reads ``.git`` plumbing files directly (no subprocess, no network) so
agents can compare a generated MANIFEST against ``git rev-parse HEAD``
and know whether the knowledge base is stale before trusting it.

## Contents

- **Functions:** [`read_git_head`](#read_git_head)

## Functions

<a id="read_git_head"></a>

### `read_git_head`

`function` | [readmenator/_gitmeta.py:84](../../readmenator/_gitmeta.py#L84)

```python
def read_git_head(project_root: str) -> Dict[str, str]
```

Return the current commit and branch of a project, when available.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_root` | `str` |  | Work tree root directory. |

**Returns:** `Dict[str, str]` - Mapping with `[`commit`](readmenator._receipts.py.md#releasereceiptrecord-commit)` and `[`branch`](readmenator._receipts.py.md#releasereceiptrecord-branch)` keys (empty strings when
unknown or not a git repository).

*Called by:* [`GitHubWikiPublisher.publish`](readmenator._gh_wiki.py.md#githubwikipublisher-publish), [`GitHubWikiPublisher.render`](readmenator._gh_wiki.py.md#githubwikipublisher-render), [`ProjectMemory.build`](readmenator._memory.py.md#projectmemory-build)

---
