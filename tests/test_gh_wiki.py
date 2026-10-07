"""Contract tests for the GitHub wiki publisher (no network: git/gh calls are faked)."""

import subprocess
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import List

from readmenator._config import Config
from readmenator._gh_wiki import GitHubWikiPublisher


class _FakeRunner:
    """Records commands and simulates gh/git with a local wiki clone."""

    def __init__(self, origin: str = "https://github.com/owner/repo.git",
                 clone_ok: bool = True, dirty: bool = True) -> None:
        self.calls: List[List[str]] = []
        self.origin = origin
        self.clone_ok = clone_ok
        self.dirty = dirty

    def __call__(self, command, cwd=None, **kwargs) -> subprocess.CompletedProcess:
        self.calls.append(list(command))
        out, code = "", 0
        if command[:2] == ["gh", "repo"]:
            out, code = (self.origin + "\n", 0) if self.origin else ("", 1)
        elif command[:3] == ["git", "remote", "get-url"]:
            out, code = (self.origin + "\n", 0) if self.origin else ("", 1)
        elif command[:2] == ["git", "clone"]:
            if self.clone_ok:
                Path(command[-1]).mkdir(parents=True)
            else:
                code = 128
        elif command[:2] == ["git", "status"]:
            out = " M Home.md\n" if self.dirty else ""
        return subprocess.CompletedProcess(command, code, out, "")


def _project(root: Path, config: Config) -> None:
    """Create generated outputs the publisher mirrors."""
    wiki = root / config.WIKI_OUTPUT_DIR
    agent = root / config.AGENT_OUTPUT_DIR
    (agent / "recipes").mkdir(parents=True)
    wiki.mkdir()
    (root / "src").mkdir()
    (root / "src" / "core.py").write_text("x = 1\n")
    (wiki / "index.md").write_text("# Brain\n\n- [Core](./community_0_core.md)\n- `src/core.py:1`\n")
    (wiki / "community_0_core.md").write_text("# Core\n\nBack to [index](index.md)\n")
    (agent / "INDEX.md").write_text("# Index\n\nNext: [INDEX_p2.md](INDEX_p2.md)\n")
    (agent / "INDEX_p2.md").write_text("# Index (page 2 of 2)\n")
    (agent / "recipes" / "fix-cycle.md").write_text("# Recipe\n")
    (root / config.OUTPUT_FILENAME).write_text("# KB\n")
    git = root / ".git"
    (git / "refs" / "heads").mkdir(parents=True)
    (git / "HEAD").write_text("ref: refs/heads/main\n")
    (git / "refs" / "heads" / "main").write_text("a" * 40 + "\n")


class TestGitHubWikiPages(unittest.TestCase):
    """Pages are flat, linked, navigable, and pinned to the source commit."""

    def test_gh_wiki_page_names_are_flat_and_prefixed(self) -> None:
        pub = GitHubWikiPublisher(Config())
        self.assertEqual(pub.page_name("readmenator-wiki/index.md"), "Home")
        self.assertEqual(pub.page_name("KNOWLEDGE_BASE.md"), "Knowledge-Base")
        self.assertEqual(pub.page_name("readmenator-agent/API_p2.md"), "Agent-API_p2")
        self.assertEqual(pub.page_name("readmenator-agent/recipes/fix-cycle.md"), "Recipe-fix-cycle")

    def test_gh_wiki_render_rewrites_links_and_permalinks(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            _project(Path(tmpdir), config)
            pages = GitHubWikiPublisher(config, _FakeRunner()).render(
                tmpdir, "https://github.com/owner/repo.git",
            )
            self.assertIn("](community_0_core)", pages["Home.md"])
            self.assertIn(
                "(https://github.com/owner/repo/blob/" + "a" * 40 + "/src/core.py#L1)",
                pages["Home.md"],
            )
            self.assertIn("](Home)", pages["community_0_core.md"])
            self.assertIn("](Agent-INDEX_p2)", pages["Agent-INDEX.md"])
            self.assertIn("Recipe-fix-cycle", pages["_Sidebar.md"])
            self.assertIn("aaaaaaaaaaaa", pages["_Footer.md"])

    def test_gh_wiki_permalinks_never_escape_project_root(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            _project(Path(tmpdir), config)
            pub = GitHubWikiPublisher(config, _FakeRunner())
            text = pub.rewrite("`../../etc/passwd.txt`", "x.md", {}, tmpdir, "https://h/o/r/blob/c/")
            self.assertEqual(text, "`../../etc/passwd.txt`")

    def test_gh_wiki_dry_run_writes_locally_and_prunes_only_owned_pages(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _project(root, config)
            out = root / config.GH_WIKI_DRY_RUN_DIR
            out.mkdir()
            (out / config.GH_WIKI_STATE_FILE).write_text("Old-Page.md\n")
            (out / "Old-Page.md").write_text("stale")
            (out / "Hand-Written.md").write_text("keep")
            runner = _FakeRunner()
            result = GitHubWikiPublisher(config, runner).publish(tmpdir, dry_run=True)
            self.assertFalse(result.pushed)
            self.assertIn("Home.md", result.pages)
            self.assertEqual(result.removed, ["Old-Page.md"])
            self.assertTrue((out / "Hand-Written.md").exists())
            self.assertFalse(any(c[:2] in (["git", "clone"], ["git", "push"]) for c in runner.calls))


class TestGitHubWikiPublish(unittest.TestCase):
    """Publishing clones the wiki remote, commits, and pushes only when changed."""

    def test_gh_wiki_publish_clones_commits_and_pushes(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            _project(Path(tmpdir), config)
            runner = _FakeRunner()
            result = GitHubWikiPublisher(config, runner).publish(tmpdir)
            self.assertTrue(result.pushed, result.message)
            self.assertEqual(result.remote, "https://github.com/owner/repo.wiki.git")
            clone = next(c for c in runner.calls if c[:2] == ["git", "clone"])
            self.assertIn("https://github.com/owner/repo.wiki.git", clone)
            self.assertTrue(any(c[:2] == ["git", "push"] for c in runner.calls))

    def test_gh_wiki_publish_skips_push_when_unchanged(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            _project(Path(tmpdir), config)
            runner = _FakeRunner(dirty=False)
            result = GitHubWikiPublisher(config, runner).publish(tmpdir)
            self.assertFalse(result.pushed)
            self.assertFalse(any(c[:2] == ["git", "push"] for c in runner.calls))

    def test_gh_wiki_publish_explains_uninitialized_wiki(self) -> None:
        config = Config()
        with tempfile.TemporaryDirectory() as tmpdir:
            _project(Path(tmpdir), config)
            result = GitHubWikiPublisher(config, _FakeRunner(clone_ok=False)).publish(tmpdir)
            self.assertFalse(result.pushed)
            self.assertIn("first page", result.message)

    def test_gh_wiki_rejects_malformed_configured_remote(self) -> None:
        config = replace(Config(), GH_WIKI_REMOTE="https://x/o/r.git; rm -rf /")
        with tempfile.TemporaryDirectory() as tmpdir:
            result = GitHubWikiPublisher(config, _FakeRunner()).publish(tmpdir)
            self.assertFalse(result.pushed)
            self.assertEqual(result.remote, "")

    def test_gh_wiki_disabled_by_default(self) -> None:
        self.assertFalse(Config().GH_WIKI_ENABLED)


if __name__ == "__main__":
    unittest.main()
