"""Contract tests for the git history reader used by the growth video act."""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._githistory import GitHistoryReader


def _git_available() -> bool:
    """Return whether a git binary is reachable."""
    return shutil.which("git") is not None


def _run_git(root: Path, *args: str) -> None:
    """Run a git command inside *root* with an isolated identity.

    Args:
        root: Repository directory.
        args: Git arguments.
    """
    env = dict(os.environ)
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        env.pop(key, None)
    subprocess.run(
        ["git", "-c", "user.email=test@example.com", "-c", "user.name=Test", *args],
        cwd=str(root), env=env, check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def _write(path: Path, text: str) -> None:
    """Write *text* to *path*, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@unittest.skipUnless(_git_available(), "git is not installed")
class TestGitHistoryReader(unittest.TestCase):
    """Contract: releases are read from git without touching the working copy."""

    def setUp(self) -> None:
        """Create a temporary repository with two tagged releases."""
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        _run_git(self.root, "init", "-q")
        _write(self.root / "app.py", "import helper\n\n\ndef main():\n    return helper.run()\n")
        _write(self.root / "helper.py", "def run():\n    return 1\n")
        _run_git(self.root, "add", "-A")
        _run_git(self.root, "commit", "-q", "-m", "first")
        _run_git(self.root, "tag", "v1.0.0")
        _write(self.root / "extra.py", "def extra():\n    return 2\n")
        _run_git(self.root, "add", "-A")
        _run_git(self.root, "commit", "-q", "-m", "second")
        _run_git(self.root, "tag", "release/v1.1.0")
        _write(self.root / "later.py", "def later():\n    return 3\n")
        _run_git(self.root, "add", "-A")
        _run_git(self.root, "commit", "-q", "-m", "third")

    def tearDown(self) -> None:
        """Remove the temporary repository."""
        self._tmp.cleanup()

    def test_githistory_timeline_orders_releases(self) -> None:
        """Every tag and HEAD come back in chronological order."""
        reader = GitHistoryReader(Config())
        releases = reader.timeline(str(self.root))
        self.assertEqual([r.label for r in releases], ["v1.0.0", "v1.1.0", "HEAD"])
        self.assertEqual(releases[0].ref, "v1.0.0")
        self.assertEqual(releases[1].ref, "release/v1.1.0")

    def test_githistory_untagged_first_commit_is_genesis(self) -> None:
        """A first commit without a tag opens the timeline as genesis."""
        _run_git(self.root, "tag", "-d", "v1.0.0")
        releases = GitHistoryReader(Config()).timeline(str(self.root))
        self.assertEqual([r.label for r in releases], ["genesis", "v1.1.0", "HEAD"])
        self.assertEqual(releases[0].ref, "")

    def test_githistory_snapshots_count_files_and_links(self) -> None:
        """Each release carries the files and the internal imports of its tree."""
        reader = GitHistoryReader(Config())
        releases = reader.timeline(str(self.root))
        genesis = releases[0]
        self.assertEqual(genesis.file_ids, ("app.py", "helper.py"))
        self.assertEqual(genesis.symbol_count, 2)
        self.assertIn(("app.py", "helper.py"), genesis.links)
        self.assertEqual(releases[1].file_ids, ("app.py", "extra.py", "helper.py"))
        self.assertEqual(releases[-1].file_ids, ("app.py", "extra.py", "helper.py", "later.py"))

    def test_githistory_skips_generated_outputs(self) -> None:
        """Readmenator artifacts are never part of a release snapshot."""
        _write(self.root / "readmenator-agent" / "INDEX.md", "# generated\n")
        _run_git(self.root, "add", "-A")
        _run_git(self.root, "commit", "-q", "-m", "agent output")
        reader = GitHistoryReader(Config())
        releases = reader.timeline(str(self.root))
        self.assertNotIn("readmenator-agent/INDEX.md", releases[-1].file_ids)

    def test_githistory_respects_snapshot_budget(self) -> None:
        """The timeline keeps the first snapshot plus the most recent ones."""
        reader = GitHistoryReader(Config(VIDEO_HISTORY_MAX_SNAPSHOTS=2))
        releases = reader.timeline(str(self.root))
        self.assertEqual(len(releases), 2)
        self.assertEqual(releases[0].label, "v1.0.0")
        self.assertEqual(releases[-1].label, "HEAD")

    def test_githistory_disabled_returns_empty(self) -> None:
        """A disabled history reader never touches the repository."""
        reader = GitHistoryReader(Config(VIDEO_HISTORY_ENABLED=False))
        self.assertEqual(reader.timeline(str(self.root)), [])

    def test_githistory_ignores_inherited_git_environment(self) -> None:
        """An inherited GIT_DIR never redirects the reader to another repository."""
        os.environ["GIT_DIR"] = str(self.root / ".git" / "does-not-exist")
        try:
            releases = GitHistoryReader(Config()).timeline(str(self.root))
        finally:
            os.environ.pop("GIT_DIR", None)
        self.assertEqual([r.label for r in releases], ["v1.0.0", "v1.1.0", "HEAD"])

    def test_githistory_unavailable_paths_are_empty(self) -> None:
        """A directory without git produces no timeline and no crash."""
        reader = GitHistoryReader(Config())
        with tempfile.TemporaryDirectory() as plain:
            self.assertFalse(reader.available(plain))
            self.assertEqual(reader.timeline(plain), [])
        self.assertFalse(reader.available(str(self.root / "missing")))


class TestGitHistoryParsing(unittest.TestCase):
    """Contract: git plumbing output is parsed without a repository."""

    def test_githistory_version_label_normalises_tags(self) -> None:
        """Tag names become comparable version labels."""
        self.assertEqual(GitHistoryReader._version_label("release/v1.2.3"), "v1.2.3")
        self.assertEqual(GitHistoryReader._version_label("1.4.0"), "v1.4.0")
        self.assertEqual(GitHistoryReader._version_label("v2.0.0"), "v2.0.0")
        self.assertEqual(GitHistoryReader._version_label("nightly"), "nightly")

    def test_githistory_parses_tree_listing(self) -> None:
        """``ls-tree`` records become blob/path pairs."""
        raw = b"100644 blob abc123\tapp.py\x00100644 blob def456\tdir/x.py\x00"
        self.assertEqual(
            GitHistoryReader._parse_tree(raw),
            [("abc123", "app.py"), ("def456", "dir/x.py")],
        )

    def test_githistory_parses_blob_batch(self) -> None:
        """``cat-file --batch`` payloads become sha/content pairs."""
        payload = b"abc123 blob 5\nhello\ndef456 blob 3\nbye\n"
        self.assertEqual(
            GitHistoryReader._parse_blobs(payload),
            {"abc123": b"hello", "def456": b"bye"},
        )

    def test_githistory_failed_git_returns_empty_timeline(self) -> None:
        """A broken git runner yields an empty timeline instead of raising."""

        def broken(args, root, stdin_file, stdout_file):
            raise OSError("git missing")

        reader = GitHistoryReader(Config(), runner=broken)
        with tempfile.TemporaryDirectory() as plain:
            self.assertEqual(reader.timeline(plain), [])

    def test_githistory_git_environment_is_sanitised(self) -> None:
        """Repository overrides never reach the git plumbing calls."""
        env = GitHistoryReader._git_env()
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
            self.assertNotIn(key, env)


if __name__ == "__main__":
    unittest.main()
