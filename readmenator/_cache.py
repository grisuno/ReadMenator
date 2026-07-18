"""File-content hash cache for incremental scanning and analysis caching.

Computes SHA256 digests of file contents and persists them to disk
so that subsequent scans can skip unchanged files. Also supports
caching of analysis results (security findings, v2 analysis, etc.)
for faster incremental rebuilds.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Set

from readmenator._config import Config


class FileCache:
    """SHA256-based cache for incremental file scanning and analysis.

    Stores a JSON mapping of relative file paths to their content
    hashes inside the project's cache directory. On subsequent runs,
    files whose hash matches the cached value are skipped.

    Also caches analysis results so that unchanged files reuse
    previously-computed security findings, taint paths, etc.
    """

    def __init__(self, config: Config, project_root: str):
        self._config = config
        self._project_root = Path(project_root).resolve()
        self._cache_dir = self._project_root / config.CACHE_DIR
        self._cache_path = self._cache_dir / "file_hashes.json"
        self._analysis_cache_path = self._cache_dir / "analysis_cache.json"

    def load(self) -> Dict[str, str]:
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
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        self._cache_path.write_text(
            json.dumps(hashes, indent=2, sort_keys=True), encoding="utf-8"
        )

    def compute_hash(self, file_path: Path) -> str:
        hasher = hashlib.sha256()
        try:
            data = file_path.read_bytes()
            hasher.update(data)
        except OSError:
            return ""
        return hasher.hexdigest()

    def compute_hashes(self, file_paths: Dict[str, Path]) -> Dict[str, str]:
        result: Dict[str, str] = {}
        for rel_path, abs_path in file_paths.items():
            h = self.compute_hash(abs_path)
            if h:
                result[rel_path] = h
        return result

    def find_changed(self, file_paths: Dict[str, Path]) -> Set[str]:
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

    def prune_deleted(self, current_file_ids: Set[str]) -> None:
        cached = self.load()
        pruned = {k: v for k, v in cached.items() if k in current_file_ids}
        if len(pruned) != len(cached):
            self.save(pruned)
            self._prune_analysis_cache(current_file_ids)

    # ------------------------------------------------------------------
    # Analysis result caching (semantic cache)
    # ------------------------------------------------------------------

    def save_analysis(
        self,
        key: str,
        data: Dict[str, Any],
    ) -> None:
        """Save an analysis result to the semantic cache.

        Args:
            key: Cache key (e.g. "security", "analysis_v2", "taint").
            data: Serializable analysis data.
        """
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        cache: Dict[str, Any] = {}
        if self._analysis_cache_path.is_file():
            try:
                cache = json.loads(self._analysis_cache_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        cache[key] = data
        self._analysis_cache_path.write_text(
            json.dumps(cache, indent=2, default=str), encoding="utf-8"
        )

    def load_analysis(self, key: str) -> Optional[Dict[str, Any]]:
        """Load a previously cached analysis result.

        Args:
            key: Cache key.

        Returns:
            Cached data dict, or None if not found or expired.
        """
        if not self._analysis_cache_path.is_file():
            return None
        try:
            cache = json.loads(self._analysis_cache_path.read_text(encoding="utf-8"))
            return cache.get(key)
        except (json.JSONDecodeError, OSError):
            return None

    def clear_analysis(self, key: Optional[str] = None) -> None:
        """Clear analysis cache, optionally for a specific key only.

        Args:
            key: If given, only clears this key. Otherwise clears all.
        """
        if not self._analysis_cache_path.is_file():
            return
        try:
            if key is None:
                self._analysis_cache_path.unlink(missing_ok=True)
            else:
                cache = json.loads(self._analysis_cache_path.read_text(encoding="utf-8"))
                cache.pop(key, None)
                self._analysis_cache_path.write_text(
                    json.dumps(cache, indent=2, default=str), encoding="utf-8"
                )
        except (json.JSONDecodeError, OSError):
            pass

    def _prune_analysis_cache(self, current_file_ids: Set[str]) -> None:
        """Remove analysis entries for files that no longer exist."""
        cache = self.load_analysis("file_level")
        if not cache:
            return
        pruned = {
            fid: data for fid, data in cache.get("findings", {}).items()
            if fid in current_file_ids
        }
        self.save_analysis("file_level", {"findings": pruned})

    def has_changed_since_last_analysis(self, file_paths: Dict[str, Path]) -> bool:
        """Check if any file has changed since the last analysis cache.

        Returns True if there are no cached hashes (first run) or if
        any file hash differs from the cached value.
        """
        changed = self.find_changed(file_paths)
        if changed:
            return True
        cached = self.load_analysis("analysis_v2")
        return cached is None
