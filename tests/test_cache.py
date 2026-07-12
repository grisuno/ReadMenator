"""Contract tests for the FileCache.

Validates SHA256 hashing, cache persistence, change detection,
and stale entry pruning.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from readmenator._cache import FileCache
from readmenator._config import Config


class TestFileCacheContract(unittest.TestCase):
    """Contract: FileCache provides SHA256-based incremental scan support."""

    def setUp(self) -> None:
        self.config = Config()
        self.temp_dir = tempfile.mkdtemp()
        self.cache = FileCache(self.config, self.temp_dir)

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write(self, rel_path: str, content: str) -> Path:
        abs_path = Path(self.temp_dir) / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(content, encoding="utf-8")
        return abs_path

    def test_compute_hash_returns_hex_string(self) -> None:
        path = self._write("test.py", "print('hello')")
        result = self.cache.compute_hash(path)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 64)

    def test_different_content_produces_different_hash(self) -> None:
        path_a = self._write("a.py", "x = 1")
        path_b = self._write("b.py", "x = 2")
        hash_a = self.cache.compute_hash(path_a)
        hash_b = self.cache.compute_hash(path_b)
        self.assertNotEqual(hash_a, hash_b)

    def test_same_content_produces_same_hash(self) -> None:
        path_a = self._write("a.py", "x = 1")
        path_b = self._write("b.py", "x = 1")
        hash_a = self.cache.compute_hash(path_a)
        hash_b = self.cache.compute_hash(path_b)
        self.assertEqual(hash_a, hash_b)

    def test_load_returns_empty_dict_when_no_cache(self) -> None:
        result = self.cache.load()
        self.assertEqual(result, {})

    def test_save_and_load_roundtrip(self) -> None:
        hashes = {"a.py": "abc123", "b.py": "def456"}
        self.cache.save(hashes)
        loaded = self.cache.load()
        self.assertEqual(loaded, hashes)

    def test_find_changed_detects_new_files(self) -> None:
        path = self._write("new.py", "content")
        changed = self.cache.find_changed({"new.py": path})
        self.assertIn("new.py", changed)

    def test_find_changed_detects_modified_files(self) -> None:
        path = self._write("file.py", "original content")
        self.cache.save({"file.py": self.cache.compute_hash(path)})
        path.write_text("modified content")
        changed = self.cache.find_changed({"file.py": path})
        self.assertIn("file.py", changed)

    def test_find_changed_skips_unchanged_files(self) -> None:
        path = self._write("file.py", "stable content")
        file_hash = self.cache.compute_hash(path)
        self.cache.save({"file.py": file_hash})
        changed = self.cache.find_changed({"file.py": path})
        self.assertNotIn("file.py", changed)

    def test_prune_deleted_removes_ghost_entries(self) -> None:
        self.cache.save({"a.py": "hash1", "b.py": "hash2"})
        self.cache.prune_deleted({"a.py"})
        loaded = self.cache.load()
        self.assertIn("a.py", loaded)
        self.assertNotIn("b.py", loaded)

    def test_compute_hashes_batch(self) -> None:
        path_a = self._write("a.py", "content a")
        path_b = self._write("b.py", "content b")
        batch = self.cache.compute_hashes({"a.py": path_a, "b.py": path_b})
        self.assertEqual(len(batch), 2)
        self.assertIn("a.py", batch)
        self.assertIn("b.py", batch)

    def test_nonexistent_file_returns_empty_hash(self) -> None:
        path = Path(self.temp_dir) / "does_not_exist.py"
        result = self.cache.compute_hash(path)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
