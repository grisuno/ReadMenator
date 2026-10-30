"""Git history replay: read release snapshots from a repository.

The video needs the growth story of a project, not only its final
shape. This module walks the git history of a checkout, materialises the
tracked source tree at every release tag, parses it with the very same
scanner used for the working copy, and resolves the internal import
graph of that release. The result is an ordered timeline the video can
play back as a timelapse: every release becomes a frame where the files
and the dependency edges that already existed are visible.

Read-only by construction: every git invocation is a plumbing command
with an explicit argument list (never a shell), a timeout, and no
network access. Repositories without git, without tags, or without a
reachable history simply produce an empty timeline.
"""

from __future__ import annotations

import logging
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from readmenator._config import Config
from readmenator._resolver import ImportResolver
from readmenator._scanner import PolyglotScanner

logger = logging.getLogger(__name__)

_REF_FORMAT = "%(refname:short)\t%(objectname)\t%(*objectname)\t%(creatordate:short)\t%(subject)"

_GIT_ENV_KEYS = (
    "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
    "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES",
)


@dataclass(frozen=True)
class HistoryRelease:
    """One point of the repository timeline.

    Attributes:
        label: Human version label (``v1.2.0``, ``genesis``).
        ref: Raw git ref the snapshot came from.
        commit: Commit sha of the snapshot.
        date: ISO date of the snapshot.
        file_ids: Source files tracked at that point, sorted.
        symbol_count: Symbols parsed from that tree.
        import_count: Project-internal import edges resolved at that point.
        links: Directed internal import pairs ``(importer, imported)``.
    """

    label: str
    ref: str
    commit: str
    date: str
    file_ids: Tuple[str, ...]
    symbol_count: int
    import_count: int
    links: Tuple[Tuple[str, str], ...]


class GitHistoryReader:
    """Read release snapshots from a git repository (read-only).

    Args:
        config: Settings; the history budgets live in it.
        runner: Optional callable replacing ``subprocess.run``, used by
            tests to inject a fake git.
    """

    def __init__(self, config: Config, runner: Optional[Any] = None) -> None:
        """Initialise the reader with configuration and optional runner."""
        self._config = config
        self._runner = runner

    def available(self, project_root: str) -> bool:
        """Return ``True`` when the target looks like a readable git checkout.

        Args:
            project_root: Directory that may hold the repository.

        Returns:
            Whether history can be read from that directory.
        """
        if shutil.which("git") is None:
            return False
        root = Path(project_root)
        if not root.is_dir():
            return False
        git_dir = root / ".git"
        if git_dir.is_symlink():
            return False
        return git_dir.exists()

    def timeline(self, project_root: str) -> List[HistoryRelease]:
        """Build the ordered release timeline of a repository.

        The first commit comes first (named after its tag when it carries
        one), then every tag ordered by its creation date, then HEAD when
        it is ahead of the last tag.

        When the timeline exceeds the snapshot budget the surviving
        releases are spread evenly between the first and the last entry,
        so the growth story keeps running from the beginning without
        jumping from the first release to a distant one.

        Args:
            project_root: Repository root to read.

        Returns:
            Snapshots in chronological order; empty when history is unavailable.
        """
        if not self._config.VIDEO_HISTORY_ENABLED:
            return []
        if not self.available(project_root):
            return []
        root = Path(project_root).resolve()
        entries = self._entries(root)
        limit = max(1, int(self._config.VIDEO_HISTORY_MAX_SNAPSHOTS))
        if len(entries) > limit:
            if limit <= 1:
                entries = entries[:1]
            else:
                step = (len(entries) - 1) / (limit - 1)
                picked = [int(round(index * step)) for index in range(limit)]
                entries = [entries[min(len(entries) - 1, picked_index)] for picked_index in picked]
        releases: List[HistoryRelease] = []
        for label, ref, commit, date in entries:
            release = self._snapshot(root, label, ref, commit, date)
            if release is not None:
                releases.append(release)
        return releases

    def _entries(self, root: Path) -> List[Tuple[str, str, str, str]]:
        """Collect ``(label, ref, commit, date)`` points of the timeline."""
        entries: List[Tuple[str, str, str, str]] = []
        seen: set = set()
        tags = self._tags(root)
        tagged = {commit: ref for ref, commit, _date in tags}
        for commit, date in self._genesis(root):
            if commit in seen:
                continue
            seen.add(commit)
            ref = tagged.get(commit, "")
            label = self._version_label(ref) if ref else "genesis"
            entries.append((label, ref, commit, date))
        for ref, commit, date in tags:
            if commit in seen:
                continue
            seen.add(commit)
            entries.append((self._version_label(ref), ref, commit, date))
        head, head_date = self._head(root)
        if head and head not in seen:
            entries.append(("HEAD", "HEAD", head, head_date))
        return entries

    def _genesis(self, root: Path) -> List[Tuple[str, str]]:
        """Return the root commits of the current history with their dates."""
        out = self._git(root, ["rev-list", "--max-parents=0", "HEAD"])
        commits = [line.strip() for line in out.splitlines() if line.strip()]
        result: List[Tuple[str, str]] = []
        for commit in commits[:1]:
            result.append((commit, self._commit_date(root, commit)))
        return result

    def _tags(self, root: Path) -> List[Tuple[str, str, str]]:
        """Return ``(ref, commit, date)`` for every tag, oldest first."""
        out = self._git(root, [
            "for-each-ref", "--sort=creatordate", f"--format={_REF_FORMAT}", "refs/tags",
        ])
        tags: List[Tuple[str, str, str]] = []
        for line in out.splitlines():
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            ref = parts[0].strip()
            commit = (parts[2].strip() or parts[1].strip())
            date = parts[3].strip()
            if not ref or not commit:
                continue
            tags.append((ref, commit, date))
        return tags

    def _head(self, root: Path) -> Tuple[str, str]:
        """Return the HEAD commit sha and its date."""
        commit = self._git(root, ["rev-parse", "HEAD"]).strip()
        if not commit:
            return ("", "")
        return (commit, self._commit_date(root, commit))

    def _commit_date(self, root: Path, commit: str) -> str:
        """Return the ISO date of a commit."""
        return self._git(root, ["log", "-1", "--format=%cs", commit]).strip()

    def _snapshot(
        self, root: Path, label: str, ref: str, commit: str, date: str,
    ) -> Optional[HistoryRelease]:
        """Materialise and parse the source tree of one commit."""
        tree = self._tree(root, commit)
        if not tree:
            return None
        sources = self._source_files(tree)
        if not sources:
            return None
        blobs = self._blobs(root, [sha for sha, _path in sources])
        contents: Dict[str, str] = {}
        max_bytes = int(self._config.MAX_FILE_SIZE_MB * 1024 * 1024)
        for sha, path in sources:
            blob = blobs.get(sha)
            if blob is None or len(blob) > max_bytes:
                continue
            contents[path] = blob.decode("utf-8", "ignore")
        if not contents:
            return None
        scanner = PolyglotScanner(self._config)
        nodes, edges, _content = scanner.scan_contents(contents)
        file_ids = sorted(contents)
        links = self._resolve_links(file_ids, edges, root)
        symbols = sum(len(node.symbols) for node in nodes)
        return HistoryRelease(
            label=label, ref=ref, commit=commit, date=date,
            file_ids=tuple(file_ids), symbol_count=symbols,
            import_count=len(links), links=tuple(links),
        )

    def _resolve_links(
        self, file_ids: Sequence[str], edges: Sequence[Any], root: Path,
    ) -> List[Tuple[str, str]]:
        """Resolve raw import strings into project-internal file pairs."""
        resolver = ImportResolver(list(file_ids), str(root))
        links: set = set()
        for edge in edges:
            if getattr(edge, "relation", "") != "imports":
                continue
            target = resolver.resolve(edge.target, edge.source)
            if target and target != edge.source and target in file_ids:
                links.add((edge.source, target))
        return sorted(links)

    def _source_files(self, tree: Sequence[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Filter a tree listing down to parseable, non-generated sources."""
        cfg = self._config
        scanner = PolyglotScanner(cfg)
        limit = max(1, int(cfg.VIDEO_HISTORY_MAX_FILES))
        out: List[Tuple[str, str]] = []
        for sha, path in tree:
            if len(out) >= limit:
                break
            if not self._is_source(path, scanner):
                continue
            out.append((sha, path))
        return out

    def _is_source(self, path: str, scanner: PolyglotScanner) -> bool:
        """Return ``True`` when a tracked path is a source file worth parsing."""
        cfg = self._config
        pure = Path(path)
        suffix = pure.suffix
        if suffix.lower() not in {ext.lower() for ext in cfg.SUPPORTED_EXTENSIONS}:
            return False
        if scanner.is_generated(pure):
            return False
        if len(pure.parts) > cfg.MAX_DIRECTORY_DEPTH:
            return False
        return True

    def _tree(self, root: Path, commit: str) -> List[Tuple[str, str]]:
        """Return ``(blob_sha, path)`` for every file tracked at a commit."""
        raw = self._git_bytes(root, ["ls-tree", "-r", "-z", commit])
        return self._parse_tree(raw)

    def _blobs(self, root: Path, shas: Sequence[str]) -> Dict[str, bytes]:
        """Read blob contents for the given object ids."""
        if not shas:
            return {}
        with tempfile.TemporaryFile() as stdin_file, tempfile.TemporaryFile() as stdout_file:
            stdin_file.write(("\n".join(shas) + "\n").encode("ascii"))
            stdin_file.seek(0)
            result = self._run(
                root, ["cat-file", "--batch"],
                stdin_file=stdin_file, stdout_file=stdout_file,
            )
            if result is None or result.returncode != 0:
                return {}
            stdout_file.seek(0)
            payload = stdout_file.read()
        return self._parse_blobs(payload)

    def _git(self, root: Path, args: Sequence[str]) -> str:
        """Run a git command and return its stdout as text."""
        raw = self._git_bytes(root, args)
        return raw.decode("utf-8", "replace")

    def _git_bytes(self, root: Path, args: Sequence[str]) -> bytes:
        """Run a git command and return its raw stdout."""
        result = self._run(root, list(args))
        if result is None or result.returncode != 0:
            return b""
        return result.stdout or b""

    def _run(
        self, root: Path, args: List[str], stdin_file: Any = None, stdout_file: Any = None,
    ) -> Optional[Any]:
        """Run a git command with a timeout, returning ``None`` on failure.

        Stdout is captured into a pipe by default so nothing leaks to the
        terminal; a temporary file is used for the binary blob protocol.
        The environment is sanitised so an inherited ``GIT_DIR`` can never
        point the reader at another repository.
        """
        timeout = max(1, int(self._config.VIDEO_HISTORY_TIMEOUT_S))
        try:
            if self._runner is not None:
                return self._runner(args, root, stdin_file, stdout_file)
            return subprocess.run(
                ["git", *args], cwd=str(root),
                stdin=stdin_file if stdin_file is not None else subprocess.DEVNULL,
                stdout=stdout_file if stdout_file is not None else subprocess.PIPE,
                stderr=subprocess.PIPE, timeout=timeout, check=False,
                env=self._git_env(),
            )
        except (OSError, subprocess.SubprocessError):
            return None

    @staticmethod
    def _git_env() -> Dict[str, str]:
        """Return the environment for git calls, without repository overrides."""
        env = dict(os.environ)
        for key in _GIT_ENV_KEYS:
            env.pop(key, None)
        return env

    @staticmethod
    def _version_label(ref: str) -> str:
        """Normalise a tag name into a version label."""
        name = ref.rsplit("/", 1)[-1].strip()
        if not name:
            return ref
        if name[0] == "v" and name[1:2].isdigit():
            return name
        if name[0:1].isdigit():
            return f"v{name}"
        return name

    @staticmethod
    def _parse_tree(raw: bytes) -> List[Tuple[str, str]]:
        """Parse ``git ls-tree -r -z`` output into ``(sha, path)`` pairs."""
        entries: List[Tuple[str, str]] = []
        for record in raw.split(b"\x00"):
            if not record:
                continue
            head, _, path = record.partition(b"\t")
            fields = head.split()
            if len(fields) < 3 or fields[1] != b"blob":
                continue
            entries.append((fields[2].decode("ascii", "replace"), path.decode("utf-8", "replace")))
        return entries

    @staticmethod
    def _parse_blobs(payload: bytes) -> Dict[str, bytes]:
        """Parse ``git cat-file --batch`` output into ``{sha: content}``."""
        blobs: Dict[str, bytes] = {}
        position = 0
        total = len(payload)
        while position < total:
            newline = payload.find(b"\n", position)
            if newline == -1:
                break
            header = payload[position:newline].decode("utf-8", "replace").split()
            position = newline + 1
            if len(header) < 3:
                continue
            sha, kind, size_text = header[0], header[1], header[2]
            try:
                size = int(size_text)
            except ValueError:
                break
            if kind != "blob":
                position += size + 1
                continue
            blobs[sha] = payload[position:position + size]
            position += size + 1
        return blobs
