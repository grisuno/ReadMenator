"""Read-only git metadata for freshness stamps on generated documents.

Reads ``.git`` plumbing files directly (no subprocess, no network) so
agents can compare a generated MANIFEST against ``git rev-parse HEAD``
and know whether the knowledge base is stale before trusting it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

_REF_PREFIX = "ref: "
_GITDIR_PREFIX = "gitdir: "
_HEADS_PREFIX = "refs/heads/"
_MAX_META_BYTES = 65536


def _read_small(path: Path) -> str:
    """Return the stripped text of a small regular file, or empty string.

    Args:
        path: File to read.

    Returns:
        File contents, or empty string when missing, a symlink, or oversized.
    """
    try:
        if path.is_symlink() or not path.is_file():
            return ""
        if path.stat().st_size > _MAX_META_BYTES:
            return ""
        return path.read_text(encoding="utf-8", errors="ignore").strip()
    except OSError:
        return ""


def _git_dir(root: Path) -> Optional[Path]:
    """Locate the git directory for a work tree, following gitdir files.

    Args:
        root: Work tree root.

    Returns:
        The git directory path, or None when the root is not a repository.
    """
    dot_git = root / ".git"
    if dot_git.is_dir() and not dot_git.is_symlink():
        return dot_git
    pointer = _read_small(dot_git)
    if pointer.startswith(_GITDIR_PREFIX):
        target = Path(pointer[len(_GITDIR_PREFIX):].strip())
        resolved = target if target.is_absolute() else (root / target)
        if resolved.is_dir():
            return resolved
    return None


def _packed_ref(git_dir: Path, ref: str) -> str:
    """Look up a ref in packed-refs, honoring worktree commondir.

    Args:
        git_dir: Git directory of the work tree.
        ref: Fully qualified ref name.

    Returns:
        The commit hash, or empty string.
    """
    candidates = [git_dir]
    common = _read_small(git_dir / "commondir")
    if common:
        candidates.append((git_dir / common).resolve())
    for base in candidates:
        loose = _read_small(base / ref)
        if loose:
            return loose
        for line in _read_small(base / "packed-refs").splitlines():
            parts = line.split(" ", 1)
            if len(parts) == 2 and parts[1].strip() == ref:
                return parts[0].strip()
    return ""


def read_git_head(project_root: str) -> Dict[str, str]:
    """Return the current commit and branch of a project, when available.

    Args:
        project_root: Work tree root directory.

    Returns:
        Mapping with ``commit`` and ``branch`` keys (empty strings when
        unknown or not a git repository).
    """
    git_dir = _git_dir(Path(project_root).resolve())
    if git_dir is None:
        return {"commit": "", "branch": ""}
    head = _read_small(git_dir / "HEAD")
    if head.startswith(_REF_PREFIX):
        ref = head[len(_REF_PREFIX):].strip()
        branch = ref[len(_HEADS_PREFIX):] if ref.startswith(_HEADS_PREFIX) else ref
        return {"commit": _packed_ref(git_dir, ref), "branch": branch}
    return {"commit": head, "branch": ""}
