"""Contract tests for the docs branch publisher and linguist gitattributes."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import List

from readmenator._app import readmenatorApplication
from readmenator._config import Config
from readmenator._docbranch import DocsBranchPublisher


class _FakeRunner:
    """Records git commands and accepts every push-stage call."""

    def __init__(self, origin: str = "https://github.com/owner/repo.git") -> None:
        self.calls: List[List[str]] = []
        self.origin = origin

    def __call__(self, command, cwd=None, **kwargs) -> subprocess.CompletedProcess:
        self.calls.append(list(command))
        out, code = "", 0
        if command[:3] == ["git", "remote", "get-url"]:
            out, code = (self.origin + "\n", 0) if self.origin else ("", 1)
        return subprocess.CompletedProcess(command, code, out, "")


def _git_tree(root: Path, commit: str = "a" * 40) -> None:
    """Minimal .git layout so read_git_head succeeds."""
    git = root / ".git"
    (git / "refs" / "heads").mkdir(parents=True)
    (git / "HEAD").write_text("ref: refs/heads/main\n")
    (git / "refs" / "heads" / "main").write_text(commit + "\n")


def _site(root: Path, config: Config) -> None:
    """Minimal published site (index.html plus one map)."""
    site = root / config.DIAGRAM_PAGES_DIR
    (site / "maps").mkdir(parents=True)
    (site / "index.html").write_text("<html><body>gallery</body></html>\n")
    (site / "maps" / "architecture.html").write_text("<html></html>\n")
    (site / ".nojekyll").touch()


class TestDocsBranchGitattributes(unittest.TestCase):
    """Contract: .gitattributes marks generated outputs as linguist-generated."""

    def setUp(self) -> None:
        """Create a temporary project."""
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.publisher = DocsBranchPublisher(Config())

    def tearDown(self) -> None:
        """Remove the temporary project."""
        self.tmp.cleanup()

    def test_creates_block_with_generated_paths(self) -> None:
        """A missing .gitattributes is created with the generated block."""
        self.assertTrue(self.publisher.ensure_gitattributes(str(self.root)))
        text = (self.root / Config().GITATTRIBUTES_FILENAME).read_text(encoding="utf-8")
        self.assertIn("# readmenator:gitattributes:begin", text)
        self.assertIn("/readmenator-agent/** linguist-generated=true", text)
        self.assertIn("/docs/** linguist-generated=true", text)
        self.assertIn("/readmenator.mp4 linguist-generated=true", text)

    def test_is_idempotent(self) -> None:
        """A second run does not change the file."""
        self.publisher.ensure_gitattributes(str(self.root))
        before = (self.root / Config().GITATTRIBUTES_FILENAME).read_bytes()
        self.assertFalse(self.publisher.ensure_gitattributes(str(self.root)))
        self.assertEqual(before, (self.root / Config().GITATTRIBUTES_FILENAME).read_bytes())

    def test_preserves_existing_content_and_refreshes_block(self) -> None:
        """User entries survive and a stale block is replaced in place."""
        path = self.root / Config().GITATTRIBUTES_FILENAME
        path.write_text(
            "*.png binary text\n"
            "# readmenator:gitattributes:begin\n"
            "/old/** linguist-generated=true\n"
            "# readmenator:gitattributes:end\n"
            "*.zip -text\n",
            encoding="utf-8",
        )
        self.assertTrue(self.publisher.ensure_gitattributes(str(self.root)))
        text = path.read_text(encoding="utf-8")
        self.assertIn("*.png binary text", text)
        self.assertIn("*.zip -text", text)
        self.assertNotIn("/old/**", text)
        self.assertIn("/readmenator-wiki/** linguist-generated=true", text)

    def test_disabled_config_writes_nothing(self) -> None:
        """GITATTRIBUTES_ENABLED=False leaves the file alone."""
        publisher = DocsBranchPublisher(replace(Config(), GITATTRIBUTES_ENABLED=False))
        self.assertFalse(publisher.ensure_gitattributes(str(self.root)))
        self.assertFalse((self.root / Config().GITATTRIBUTES_FILENAME).exists())

    def test_symlink_target_refused(self) -> None:
        """A symlinked .gitattributes is never written through."""
        outside = self.root / "outside.txt"
        outside.write_text("keep\n")
        link = self.root / Config().GITATTRIBUTES_FILENAME
        link.symlink_to(outside)
        self.assertFalse(self.publisher.ensure_gitattributes(str(self.root)))
        self.assertEqual(outside.read_text(), "keep\n")


class TestDocsBranchPagesUrl(unittest.TestCase):
    """Contract: Pages URL inferred from the origin remote, overridable."""

    def test_github_https(self) -> None:
        """https remote maps to owner.github.io."""
        self.assertEqual(
            DocsBranchPublisher.infer_pages_url("https://github.com/owner/repo.git"),
            "https://owner.github.io/repo/",
        )

    def test_github_ssh_and_scp_forms(self) -> None:
        """ssh:// and git@ remotes map to the same Pages URL."""
        self.assertEqual(
            DocsBranchPublisher.infer_pages_url("git@github.com:owner/repo.git"),
            "https://owner.github.io/repo/",
        )
        self.assertEqual(
            DocsBranchPublisher.infer_pages_url("ssh://git@github.com/owner/repo"),
            "https://owner.github.io/repo/",
        )

    def test_gitlab_com(self) -> None:
        """gitlab.com maps to owner.gitlab.io."""
        self.assertEqual(
            DocsBranchPublisher.infer_pages_url("git@gitlab.com:owner/repo.git"),
            "https://owner.gitlab.io/repo/",
        )

    def test_unknown_host_is_empty(self) -> None:
        """Self-hosted remotes yield no inference."""
        self.assertEqual(DocsBranchPublisher.infer_pages_url("git@git.example.com:team/repo.git"), "")

    def test_local_path_is_empty(self) -> None:
        """Local remotes yield no inference."""
        self.assertEqual(DocsBranchPublisher.infer_pages_url("/srv/git/repo.git"), "")

    def test_config_override_wins(self) -> None:
        """DOC_PAGES_URL set in Config beats the inferred URL."""
        with tempfile.TemporaryDirectory() as tmp:
            publisher = DocsBranchPublisher(replace(Config(), DOC_PAGES_URL="https://docs.example.dev/"))
            self.assertEqual(publisher.pages_url(tmp), "https://docs.example.dev/")


class TestDocsBranchPublish(unittest.TestCase):
    """Contract: staging, dry run, push, and failure messages."""

    def setUp(self) -> None:
        """Create a project with a site and a faked git runner."""
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cfg = Config()
        _git_tree(self.root)
        _site(self.root, self.cfg)
        self.runner = _FakeRunner()
        self.publisher = DocsBranchPublisher(self.cfg, runner=self.runner)

    def tearDown(self) -> None:
        """Remove the temporary project."""
        self.tmp.cleanup()

    def test_publish_without_site_asks_for_pages(self) -> None:
        """A missing index.html points the user at `readmenator . pages`."""
        (self.root / self.cfg.DIAGRAM_PAGES_DIR / "index.html").unlink()
        result = self.publisher.publish(str(self.root))
        self.assertIn("pages", result.message)
        self.assertFalse(result.pushed)

    def test_dry_run_stages_without_git(self) -> None:
        """Dry run copies the site into DOC_DRY_RUN_DIR and calls no git."""
        result = self.publisher.publish(str(self.root), dry_run=True)
        out = Path(result.output_dir)
        self.assertTrue((out / "index.html").is_file())
        self.assertTrue((out / ".nojekyll").is_file())
        self.assertIn("maps/architecture.html", result.files)
        self.assertFalse(result.pushed)
        git_calls = [c for c in self.runner.calls if c[:1] == ["git"]]
        self.assertEqual(git_calls, [])

    def test_publish_pushes_orphan_branch_with_force(self) -> None:
        """Push sends HEAD to refs/heads/<DOC_BRANCH_NAME> without touching main."""
        result = self.publisher.publish(str(self.root), push=True)
        self.assertTrue(result.pushed)
        self.assertEqual(result.branch, self.cfg.DOC_BRANCH_NAME)
        push_calls = [c for c in self.runner.calls if c[:2] == ["git", "push"]]
        self.assertEqual(len(push_calls), 1)
        self.assertIn(f"+HEAD:refs/heads/{self.cfg.DOC_BRANCH_NAME}", push_calls[0])
        self.assertIn("--force", push_calls[0])
        self.assertTrue((self.root / self.cfg.GITATTRIBUTES_FILENAME).exists())
        self.assertIn("https://owner.github.io/repo/", result.pages_url)

    def test_publish_without_remote_reports_skip(self) -> None:
        """No origin remote means no push and an explicit message."""
        self.publisher = DocsBranchPublisher(self.cfg, runner=_FakeRunner(origin=""))
        result = self.publisher.publish(str(self.root), push=True)
        self.assertFalse(result.pushed)
        self.assertIn("no origin remote", result.message)

    def test_failed_push_reports_commit_ready(self) -> None:
        """A failed push still leaves the staged commit described."""
        class _FailingRunner(_FakeRunner):
            def __call__(self, command, cwd=None, **kwargs):
                if command[:2] == ["git", "push"]:
                    return subprocess.CompletedProcess(command, 128, "", "rejected")
                return super().__call__(command, cwd=cwd, **kwargs)

        self.publisher = DocsBranchPublisher(self.cfg, runner=_FailingRunner())
        result = self.publisher.publish(str(self.root), push=True)
        self.assertFalse(result.pushed)
        self.assertIn("push", result.message.lower())

    def test_disabled_flag_skips_gitattributes_only(self) -> None:
        """DOC_BRANCH_ENABLED=False does not block an explicit publish call."""
        publisher = DocsBranchPublisher(replace(self.cfg, DOC_BRANCH_ENABLED=False), runner=self.runner)
        result = publisher.publish(str(self.root))
        self.assertTrue(result.pushed)

    def test_generated_paths_cover_outputs_and_video(self) -> None:
        """The gitattributes list names every generated output plus the video."""
        paths = self.publisher.generated_paths()
        self.assertIn(self.cfg.AGENT_OUTPUT_DIR, paths)
        self.assertIn(self.cfg.DIAGRAM_PAGES_DIR, paths)
        self.assertIn(self.cfg.GRAPHRAG_OUTPUT_DIR, paths)
        self.assertIn(self.cfg.SITE_VIDEO_FILENAME, paths)
        self.assertTrue(all("/" not in p or p == p for p in paths))


class TestDocsBranchAppWiring(unittest.TestCase):
    """Contract: publish_doc_branch refreshes the README docs-site link."""

    def setUp(self) -> None:
        """Create a project with a site, a README, and git metadata."""
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        _git_tree(self.root)
        _site(self.root, Config())
        (self.root / "README.md").write_text("# Proj\n\nA tiny project.\n", encoding="utf-8")

    def tearDown(self) -> None:
        """Remove the temporary project."""
        self.tmp.cleanup()

    def test_publish_refreshes_readme_site_link(self) -> None:
        """A configured DOC_PAGES_URL lands in the README after publishing."""
        app = readmenatorApplication(replace(Config(), DOC_PAGES_URL="https://proj.example.dev/"))
        result = app.publish_doc_branch(str(self.root), push=False)
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://proj.example.dev/", readme)
        self.assertIn("Docs site", readme)
        second = app.publish_doc_branch(str(self.root), push=False)
        readme2 = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertEqual(readme2.count("readmenator-kb-link"), 2)
        self.assertTrue(second.files)

    def test_publish_without_url_leaves_readme_unchanged(self) -> None:
        """No remote and no override means no site bullet is injected."""
        app = readmenatorApplication(Config())
        app.publish_doc_branch(str(self.root), push=False)
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("Docs site", readme)


if __name__ == "__main__":
    unittest.main()
