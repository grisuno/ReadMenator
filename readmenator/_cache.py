"""File-content hash cache for incremental scanning.

Computes SHA256 digests of file contents and persists them to disk
so that subsequent scans can skip unchanged files. This avoids
re-parsing files that have not been modified since the last run.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Dict, Set

from readmenator._config import Config


class FileCache:
    """SHA256-based cache for incremental file scanning.

    Stores a JSON mapping of relative file paths to their content
    hashes inside the project's cache directory. On subsequent runs,
    files whose hash matches the cached value are skipped.
    """

    def __init__(self, config: Config, project_root: str):
        """Initialise cache for the given project root.

        Args:
            config: Application settings including CACHE_DIR.
            project_root: Absolute path of the scanned project.
        """
        self._config = config
        self._project_root = Path(project_root).resolve()
        self._cache_path = self._project_root / config.CACHE_DIR / "file_hashes.json"

    def load(self) -> Dict[str, str]:
        """Load the cached hash map from disk.

        Returns:
            Dict mapping relative file paths to their SHA256 hex digests.
        """
        if not self._cache_path.is_file():
            return {}
        try:
            data = json.loads(self._cache_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except (json.JSONDecodeError, OSError):
            pass
        return {}

    def save(self, hashes: Dict[str, str]) -> None:
        """Persist the hash map to disk.

        Args:
            hashes: Dict mapping relative file paths to SHA256 hex digests.
        """
        self._cache_path.parent.mkdir(parents=True, exist_ok=True)
        self._cache_path.write_text(
            json.dumps(hashes, indent=2, sort_keys=True), encoding="utf-8"
        )

    def compute_hash(self, file_path: Path) -> str:
        """Compute the SHA256 hex digest of a file's contents.

        Args:
            file_path: Absolute path to the file.

        Returns:
            SHA256 hex digest string.
        """
        hasher = hashlib.sha256()
        try:
            data = file_path.read_bytes()
            hasher.update(data)
        except OSError:
            return ""
        return hasher.hexdigest()

    def compute_hashes(self, file_paths: Dict[str, Path]) -> Dict[str, str]:
        """Compute hashes for a batch of relative-path-to-absolute-path mappings.

        Args:
            file_paths: Dict mapping relative paths to absolute Path objects.

        Returns:
            Dict mapping relative paths to their SHA256 hex digests.
        """
        result: Dict[str, str] = {}
        for rel_path, abs_path in file_paths.items():
            h = self.compute_hash(abs_path)
            if h:
                result[rel_path] = h
        return result

    def find_changed(
        self, file_paths: Dict[str, Path]
    ) -> Set[str]:
        """Determine which files have changed since the last cache.

        Args:
            file_paths: Dict mapping relative paths to absolute Path objects.

        Returns:
            Set of relative paths for files that are new or changed.
        """
        cached = self.load()
        changed: Set[str] = set()
        for rel_path, abs_path in file_paths.items():
            if rel_path not in cached:
                changed.add(rel_path)
                continue
            current_hash = self.compute_hash(abs_path)
            if current_hash and current_hash != cached[rel_path]:
                changed.add(rel_path)
        return changed

    def prune_deleted(
        self, current_file_ids: Set[str]
    ) -> None:
        """Remove entries for files that no longer exist on disk.

        Args:
            current_file_ids: Set of relative paths currently in the project.
        """
        cached = self.load()
        pruned = {k: v for k, v in cached.items() if k in current_file_ids}
        if len(pruned) != len(cached):
            self.save(pruned)
