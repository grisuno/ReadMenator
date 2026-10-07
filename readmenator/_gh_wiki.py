"""GitHub wiki publisher: mirrors generated knowledge into the repository wiki.

Turns the readmenator wiki, agent docs, recipes, and KNOWLEDGE_BASE.md
into flat GitHub wiki pages (Home, _Sidebar, _Footer), rewrites relative
markdown links to wiki page names, and turns backticked project paths
into commit-pinned source permalinks. Publishing clones
``<repo>.wiki.git``, replaces only pages it generated before (tracked in
a state file), commits, and pushes. It runs after every rebuild of a git
checkout (GH_WIKI_ENABLED), never during analysis, and shells out with argument lists only (no shell).
"""

from __future__ import annotations

import logging
import posixpath
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

from readmenator._config import Config
from readmenator._gitmeta import read_git_head

logger = logging.getLogger(__name__)

Runner = Callable[..., subprocess.CompletedProcess]

_LINK_RE = re.compile(r"\]\((?!https?://|mailto:|#)([^)\s]+?\.md)(#[^)\s]*)?\)")
_PATH_RE = re.compile(r"`([A-Za-z0-9_.\-/]+\.[A-Za-z0-9]+)(?::(\d+))?`")
_REMOTE_RE = re.compile(r"^(https://[^\s/]+/|ssh://git@[^\s/]+/|git@[^\s:]+:)[\w.\-]+/[\w.\-]+?(\.git)?/?$")
_PAGE_SAFE_RE = re.compile(r"[^A-Za-z0-9_\-]+")
_WEB_RE = re.compile(r"^(?:https://|ssh://git@|git@)([^/:]+)[/:]([\w.\-]+)/([\w.\-]+?)(?:\.git)?/?$")


@dataclass
class WikiPublishResult:
    """Outcome of a GitHub wiki publish.

    Attributes:
        pages: Wiki page file names written.
        removed: Previously generated page files deleted as stale.
        pushed: Whether a commit was pushed to the wiki remote.
        remote: Wiki remote URL used, empty in dry runs without a remote.
        output_dir: Directory holding the rendered pages.
        message: Human-readable status line.
    """

    pages: List[str] = field(default_factory=list)
    removed: List[str] = field(default_factory=list)
    pushed: bool = False
    remote: str = ""
    output_dir: str = ""
    message: str = ""


class GitHubWikiPublisher:
    """Renders and publishes generated documentation to a GitHub wiki."""

    def __init__(self, config: Config, runner: Optional[Runner] = None) -> None:
        """Store configuration and the subprocess runner (injectable for tests).

        Args:
            config: Central settings for paths, page names, and git options.
            runner: Callable compatible with ``subprocess.run``.
        """
        self._config = config
        self._run = runner or subprocess.run

    def page_name(self, rel_path: str) -> str:
        """Map a generated markdown path to its flat GitHub wiki page name.

        Args:
            rel_path: Project-relative markdown path.

        Returns:
            Wiki page name without extension.
        """
        cfg = self._config
        path = posixpath.normpath(rel_path)
        stem = posixpath.splitext(posixpath.basename(path))[0]
        if path == f"{cfg.WIKI_OUTPUT_DIR}/index.md":
            return cfg.GH_WIKI_HOME_PAGE
        if path == cfg.OUTPUT_FILENAME:
            return cfg.GH_WIKI_KB_PAGE
        if path.startswith(f"{cfg.AGENT_OUTPUT_DIR}/recipes/"):
            prefix = cfg.GH_WIKI_RECIPE_PREFIX
        elif path.startswith(f"{cfg.AGENT_OUTPUT_DIR}/"):
            prefix = cfg.GH_WIKI_AGENT_PREFIX
        else:
            prefix = ""
        return _PAGE_SAFE_RE.sub("-", prefix + stem).strip("-") or cfg.GH_WIKI_HOME_PAGE

    def collect_sources(self, project_root: str) -> List[str]:
        """List project-relative markdown sources to publish, sorted.

        Args:
            project_root: Project root holding generated outputs.

        Returns:
            Relative POSIX paths of regular, non-symlink markdown files.
        """
        cfg = self._config
        base = Path(project_root).resolve()
        sources: List[str] = []
        if cfg.GH_WIKI_INCLUDE_KB:
            kb = base / cfg.OUTPUT_FILENAME
            if kb.is_file() and not kb.is_symlink():
                sources.append(cfg.OUTPUT_FILENAME)
        for dirname in (cfg.WIKI_OUTPUT_DIR, cfg.AGENT_OUTPUT_DIR):
            folder = base / dirname
            if not folder.is_dir() or folder.is_symlink():
                continue
            for path in sorted(folder.rglob("*.md")):
                if path.is_file() and not path.is_symlink():
                    sources.append(path.relative_to(base).as_posix())
        return sorted(set(sources))

    def _blob_base(self, remote: str, commit: str) -> str:
        """Return the web URL prefix for commit-pinned source links, or empty."""
        match = _WEB_RE.match(remote.strip())
        if not match or not commit:
            return ""
        host, owner, repo = match.groups()
        return f"https://{host}/{owner}/{repo}/blob/{commit}/"

    def rewrite(
        self,
        text: str,
        rel_path: str,
        names: Dict[str, str],
        project_root: str,
        blob_base: str,
    ) -> str:
        """Rewrite relative doc links to wiki pages and paths to source permalinks.

        Args:
            text: Markdown content of one source document.
            rel_path: Project-relative path of that document.
            names: Mapping of published relative paths to page names.
            project_root: Project root used to check that paths exist.
            blob_base: Commit-pinned blob URL prefix, empty to skip.

        Returns:
            Markdown ready for the GitHub wiki.
        """
        source_dir = posixpath.dirname(rel_path)

        def link(match: "re.Match[str]") -> str:
            """Replace one relative markdown link when its target is published."""
            target = posixpath.normpath(posixpath.join(source_dir, match.group(1)))
            page = names.get(target)
            if page is None:
                return match.group(0)
            return f"]({page}{match.group(2) or ''})"

        text = _LINK_RE.sub(link, text)
        if not blob_base:
            return text
        base = Path(project_root).resolve()

        def permalink(match: "re.Match[str]") -> str:
            """Link a backticked project file (optionally with a line) to source."""
            path, line = match.group(1), match.group(2)
            candidate = (base / path)
            try:
                inside = candidate.resolve().is_relative_to(base)
            except (OSError, ValueError):
                inside = False
            if not inside or not candidate.is_file() or candidate.is_symlink():
                return match.group(0)
            anchor = f"#L{line}" if line else ""
            return f"[{match.group(0)}]({blob_base}{path}{anchor})"

        return _PATH_RE.sub(permalink, text)

    def render(self, project_root: str, remote: str = "") -> Dict[str, str]:
        """Render every wiki page, including sidebar and footer.

        Args:
            project_root: Project root holding generated outputs.
            remote: Main repository remote used for source permalinks.

        Returns:
            Mapping of wiki file name to markdown content.
        """
        cfg = self._config
        base = Path(project_root).resolve()
        sources = self.collect_sources(project_root)
        names = {rel: self.page_name(rel) for rel in sources}
        git = read_git_head(project_root)
        blob_base = self._blob_base(remote, git["commit"]) if cfg.GH_WIKI_PERMALINKS else ""
        pages: Dict[str, str] = {}
        for rel in sources:
            text = (base / rel).read_text(encoding="utf-8", errors="replace")
            pages[names[rel] + ".md"] = self.rewrite(text, rel, names, project_root, blob_base)
        if cfg.GH_WIKI_HOME_PAGE + ".md" not in pages:
            pages[cfg.GH_WIKI_HOME_PAGE + ".md"] = self._fallback_home(base.name)
        pages["_Sidebar.md"] = self._sidebar(names)
        pages["_Footer.md"] = self._footer(git)
        return pages

    def _fallback_home(self, project_name: str) -> str:
        """Return a Home page used when the readmenator wiki was not generated."""
        return (
            f"# {project_name}\n\n"
            "Generated by readmenator. Run `readmenator . --rebuild` to populate "
            "the full wiki.\n"
        )

    def _sidebar(self, names: Dict[str, str]) -> str:
        """Return the navigation sidebar grouping pages by origin."""
        cfg = self._config
        groups: List[Tuple[str, List[Tuple[str, str]]]] = [
            ("Start", []), ("Wiki", []), ("Agent Docs", []), ("Recipes", []),
        ]
        index = {title: items for title, items in groups}
        for rel, page in sorted(names.items(), key=lambda item: item[1].lower()):
            label = posixpath.splitext(posixpath.basename(rel))[0]
            if page in (cfg.GH_WIKI_HOME_PAGE, cfg.GH_WIKI_KB_PAGE):
                index["Start"].append((page.replace("-", " "), page))
            elif rel.startswith(f"{cfg.AGENT_OUTPUT_DIR}/recipes/"):
                index["Recipes"].append((label, page))
            elif rel.startswith(f"{cfg.AGENT_OUTPUT_DIR}/"):
                index["Agent Docs"].append((label, page))
            else:
                index["Wiki"].append((label, page))
        lines: List[str] = []
        for title, items in groups:
            if not items:
                continue
            lines.append(f"**{title}**")
            lines.append("")
            lines.extend(f"- [{label}]({page})" for label, page in items)
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _footer(git: Dict[str, str]) -> str:
        """Return the footer stamping the source commit and regeneration command."""
        commit = git.get("commit", "")[:12] or "unknown"
        return (
            f"Generated offline by readmenator from commit `{commit}`. "
            "Edits here are overwritten by `readmenator . --rebuild`.\n"
        )

    def wiki_remote(self, project_root: str) -> str:
        """Resolve the wiki remote from config, ``gh``, or the git origin.

        Args:
            project_root: Project root of the main repository.

        Returns:
            The ``.wiki.git`` remote URL, or empty string when unknown.
        """
        configured = self._config.GH_WIKI_REMOTE.strip()
        if configured:
            return configured if _REMOTE_RE.match(configured) else ""
        origin = self._origin(project_root)
        if not origin:
            return ""
        trimmed = origin[:-4] if origin.endswith(".git") else origin.rstrip("/")
        return trimmed + ".wiki.git"

    def _origin(self, project_root: str) -> str:
        """Return the main repository URL via ``gh`` or ``git remote``."""
        attempts: Sequence[List[str]] = (
            ["gh", "repo", "view", "--json", "url", "--jq", ".url"],
            ["git", "remote", "get-url", self._config.GH_WIKI_GIT_REMOTE_NAME],
        )
        for command in attempts:
            out = self._call(command, cwd=project_root)
            if out is not None and _REMOTE_RE.match(out.strip()):
                return out.strip()
        return ""

    def _call(self, command: List[str], cwd: str) -> Optional[str]:
        """Run a command without a shell and return stdout, or None on failure."""
        try:
            result = self._run(
                command, cwd=cwd, capture_output=True, text=True,
                timeout=self._config.GH_WIKI_TIMEOUT_S, check=False,
            )
        except (OSError, subprocess.SubprocessError):
            return None
        if result.returncode != 0:
            logger.debug("Command failed (%s): %s", result.returncode, " ".join(command))
            return None
        return result.stdout or ""

    def _write_pages(self, target: Path, pages: Dict[str, str]) -> List[str]:
        """Write pages, delete stale previously generated ones, and record state."""
        state = target / self._config.GH_WIKI_STATE_FILE
        previous: List[str] = []
        if state.is_file() and not state.is_symlink():
            previous = [
                line.strip() for line in state.read_text(encoding="utf-8").splitlines()
                if line.strip().endswith(".md") and "/" not in line
            ]
        removed: List[str] = []
        for name in previous:
            stale = target / name
            if name not in pages and stale.is_file() and not stale.is_symlink():
                stale.unlink()
                removed.append(name)
        for name, content in pages.items():
            (target / name).write_text(content, encoding="utf-8")
        state.write_text("\n".join(sorted(pages)) + "\n", encoding="utf-8")
        return removed

    def publish(self, project_root: str, dry_run: bool = False) -> WikiPublishResult:
        """Render pages and push them to the GitHub wiki (or a local folder).

        Args:
            project_root: Project root holding generated outputs.
            dry_run: Render into GH_WIKI_DRY_RUN_DIR without any git calls.

        Returns:
            WikiPublishResult describing what was written and pushed.
        """
        cfg = self._config
        result = WikiPublishResult()
        if dry_run:
            out = Path(project_root).resolve() / cfg.GH_WIKI_DRY_RUN_DIR
            out.mkdir(parents=True, exist_ok=True)
            remote = cfg.GH_WIKI_REMOTE.strip() or self._origin(project_root)
            pages = self.render(project_root, remote)
            result.removed = self._write_pages(out, pages)
            result.pages = sorted(pages)
            result.output_dir = str(out)
            result.message = f"Dry run: {len(pages)} wiki pages rendered into {out}"
            return result

        wiki_remote = self.wiki_remote(project_root)
        if not wiki_remote:
            result.message = (
                "GitHub wiki skipped: no remote found (set GH_WIKI_REMOTE or add an origin)"
            )
            return result
        result.remote = wiki_remote
        origin = wiki_remote[: -len(".wiki.git")] + ".git" if wiki_remote.endswith(".wiki.git") else wiki_remote
        workdir = Path(tempfile.mkdtemp(prefix="readmenator-ghwiki-"))
        try:
            clone = workdir / "wiki"
            if self._call(["git", "clone", "--depth", "1", wiki_remote, str(clone)], cwd=str(workdir)) is None:
                result.message = (
                    "GitHub wiki clone failed. Enable the wiki and create its first page "
                    "once in the web UI, then rerun readmenator . --rebuild"
                )
                return result
            pages = self.render(project_root, origin)
            result.removed = self._write_pages(clone, pages)
            result.pages = sorted(pages)
            if self._call(["git", "add", "-A"], cwd=str(clone)) is None:
                result.message = "GitHub wiki staging failed"
                return result
            status = self._call(["git", "status", "--porcelain"], cwd=str(clone))
            if not (status or "").strip():
                result.message = "GitHub wiki already up to date"
                return result
            commit = read_git_head(project_root)["commit"][:12]
            message = cfg.GH_WIKI_COMMIT_MESSAGE + (f" ({commit})" if commit else "")
            if self._call(["git", "commit", "-m", message], cwd=str(clone)) is None:
                result.message = "GitHub wiki commit failed (check git user.name/user.email)"
                return result
            if self._call(["git", "push", "origin", "HEAD"], cwd=str(clone)) is None:
                result.message = "GitHub wiki push failed (check `gh auth status` / credentials)"
                return result
            result.pushed = True
            result.message = f"GitHub wiki published: {len(pages)} pages to {wiki_remote}"
            return result
        finally:
            shutil.rmtree(workdir, ignore_errors=True)
