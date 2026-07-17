"""Filesystem watcher for auto-rebuilding the knowledge base.

Monitors the project directory for file changes and triggers
automatic regeneration of KNOWLEDGE_BASE.md. Uses polling with
configurable interval to avoid external dependencies.
"""

from __future__ import annotations

import hashlib
import logging
import time
from pathlib import Path
from typing import Callable, Optional, Set

from readmenator._config import Config

logger = logging.getLogger(__name__)


class DirectoryWatcher:
    """Polling-based directory watcher for auto-rebuild on changes.

    Computes a combined hash of all tracked files (filenames + sizes)
    and triggers a callback when the hash changes. Uses polling to
    avoid external dependencies like watchdog or inotify.
    """

    def __init__(
        self,
        root: str,
        config: Config,
        callback: Callable[[], None],
        interval_seconds: float = 3.0,
    ):
        """Initialise the watcher for a project root.

        Args:
            root: Project directory to watch.
            config: Application configuration.
            callback: Function called when changes are detected.
            interval_seconds: Polling interval in seconds.
        """
        self._root = Path(root).resolve()
        self._config = config
        self._callback = callback
        self._interval = interval_seconds
        self._last_hash: Optional[str] = None
        self._running = False

    def _compute_snapshot(self) -> str:
        """Compute a quick hash of all tracked files in the project.

        Uses file paths and sizes (not full content) for speed.
        Returns a hex digest that changes when files are added,
        removed, or modified.
        """
        hasher = hashlib.sha256()
        files: Set[str] = set()
        try:
            for file_path in sorted(self._root.rglob("*")):
                if file_path.is_file():
                    rel = str(file_path.relative_to(self._root))
                    if any(part in self._config.IGNORE_DIRS for part in file_path.parts):
                        continue
                    try:
                        if file_path.is_symlink():
                            continue
                        size = file_path.stat().st_size
                        mtime = file_path.stat().st_mtime
                    except OSError:
                        continue
                    files.add(f"{rel}:{size}:{mtime}")
        except (OSError, ValueError):
            return ""
        for entry in sorted(files):
            hasher.update(entry.encode("utf-8"))
        return hasher.hexdigest()

    def start(self) -> None:
        """Start watching the directory (blocking)."""
        self._running = True
        self._last_hash = self._compute_snapshot()
        logger.info("Watching %s for changes...", self._root)
        try:
            while self._running:
                time.sleep(self._interval)
                current_hash = self._compute_snapshot()
                if current_hash and current_hash != self._last_hash:
                    logger.info("Changes detected, rebuilding...")
                    self._last_hash = current_hash
                    self._callback()
                    logger.info("Rebuild complete. Watching...")
        except KeyboardInterrupt:
            logger.info("Watch stopped.")

    def stop(self) -> None:
        """Stop watching."""
        self._running = False
