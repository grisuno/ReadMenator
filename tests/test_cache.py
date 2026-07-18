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

    # ------------------------------------------------------------------
    # Semantic analysis cache tests
    # ------------------------------------------------------------------

    def test_save_and_load_analysis_roundtrip(self) -> None:
        data = {"god_nodes": [["a.py", 10.5]], "communities": []}
        self.cache.save_analysis("analysis_v2", data)
        loaded = self.cache.load_analysis("analysis_v2")
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded["god_nodes"], data["god_nodes"])

    def test_load_missing_analysis_key_returns_none(self) -> None:
        result = self.cache.load_analysis("nonexistent_key")
        self.assertIsNone(result)

    def test_clear_analysis_specific_key(self) -> None:
        self.cache.save_analysis("key_a", {"data": 1})
        self.cache.save_analysis("key_b", {"data": 2})
        self.cache.clear_analysis("key_a")
        self.assertIsNone(self.cache.load_analysis("key_a"))
        self.assertIsNotNone(self.cache.load_analysis("key_b"))

    def test_clear_analysis_all_keys(self) -> None:
        self.cache.save_analysis("key_a", {"data": 1})
        self.cache.save_analysis("key_b", {"data": 2})
        self.cache.clear_analysis()
        self.assertIsNone(self.cache.load_analysis("key_a"))
        self.assertIsNone(self.cache.load_analysis("key_b"))

    def test_has_changed_since_last_analysis_returns_true_on_first_run(self) -> None:
        path = self._write("test.py", "content")
        result = self.cache.has_changed_since_last_analysis({"test.py": path})
        self.assertTrue(result)

    def test_has_changed_since_last_analysis_returns_false_when_no_changes(self) -> None:
        path = self._write("stable.py", "content")
        h = self.cache.compute_hash(path)
        self.cache.save({"stable.py": h})
        self.cache.save_analysis("analysis_v2", {"done": True})
        result = self.cache.has_changed_since_last_analysis({"stable.py": path})
        self.assertFalse(result)

    def test_has_changed_since_last_analysis_returns_true_when_file_changed(self) -> None:
        path = self._write("changed.py", "original")
        h = self.cache.compute_hash(path)
        self.cache.save({"changed.py": h})
        self.cache.save_analysis("analysis_v2", {"done": True})
        path.write_text("modified")
        result = self.cache.has_changed_since_last_analysis({"changed.py": path})
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
