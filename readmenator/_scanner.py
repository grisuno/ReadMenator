"""Secure polyglot directory traversal and file analysis.

The scanner walks a directory tree, applies security and size checks,
resolves each supported file through ParserFactory, and returns a
flat list of Node and Edge objects that form the knowledge graph.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol
from readmenator._parsers import create_parser


class PolyglotScanner:
    """Recursive directory scanner with security and size guards.

    Rejects symlinks, enforces file-size and directory-depth limits,
    skips ignored directories, and silently catches parse errors
    so a single misbehaving file never breaks the full scan.

    Supports privacy mode (strips snippets and docstrings) and
    gitignore-aware scanning for more accurate project coverage.
    """

    def __init__(self, config: Config) -> None:
        """Initialise the scanner with application configuration.

        Args:
            config: Settings including ignore dirs, size limits, etc.
        """
        self._config = config
        self._gitignore_patterns: List[re.Pattern] = []

    def _is_ignored(self, path: Path) -> bool:
        """Return ``True`` if any path component matches IGNORE_DIRS."""
        return any(part in self._config.IGNORE_DIRS for part in path.parts)

    def _load_gitignore(self, root: Path) -> None:
        """Parse .gitignore patterns using regex (no external deps)."""
        gitignore_path = root / ".gitignore"
        if not gitignore_path.is_file():
            self._gitignore_patterns = []
            return
        try:
            patterns: List[str] = []
            for line in gitignore_path.read_text(encoding="utf-8", errors="ignore").split("\n"):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if stripped.startswith("!"):
                    continue
                regex_pattern = self._gitignore_glob_to_regex(stripped)
                if regex_pattern:
                    patterns.append(regex_pattern)
            self._gitignore_patterns = [re.compile(p) for p in patterns]
        except (OSError, re.error):
            self._gitignore_patterns = []

    @staticmethod
    def _gitignore_glob_to_regex(pattern: str) -> str:
        """Convert a .gitignore glob pattern to a regex pattern."""
        if pattern.startswith("/"):
            pattern = pattern[1:]
        if pattern.endswith("/"):
            pattern = pattern.rstrip("/")
        regex_parts: List[str] = []
        i = 0
        while i < len(pattern):
            c = pattern[i]
            if c == "*":
                if i + 1 < len(pattern) and pattern[i + 1] == "*":
                    regex_parts.append(".*")
                    i += 2
                    if i < len(pattern) and pattern[i] == "/":
                        i += 1
                    continue
                else:
                    regex_parts.append("[^/]*")
                    i += 1
            elif c == "?":
                regex_parts.append("[^/]")
                i += 1
            elif c == ".":
                regex_parts.append("\\.")
                i += 1
            elif c == "[":
                end = pattern.find("]", i)
                if end == -1:
                    regex_parts.append(re.escape(c))
                    i += 1
                else:
                    regex_parts.append(pattern[i:end + 1])
                    i = end + 1
            else:
                regex_parts.append(re.escape(c))
                i += 1
        result = "".join(regex_parts)
        return f"(^|/){result}"

    def _is_gitignored(self, rel_path: str) -> bool:
        """Check if a relative path matches any .gitignore pattern."""
        if not self._gitignore_patterns:
            return False
        for pattern in self._gitignore_patterns:
            if pattern.search(rel_path):
                return True
        return False

    def _validate_path_security(self, path: Path) -> bool:
        """Reject symlinks and files exceeding MAX_FILE_SIZE_MB."""
        try:
            if path.is_symlink():
                return False
            if path.is_file():
                size_mb = path.stat().st_size / (1024.0 * 1024.0)
                if size_mb > self._config.MAX_FILE_SIZE_MB:
                    return False
            return True
        except OSError:
            return False

    def _check_directory_depth(self, path: Path, root: Path) -> bool:
        """Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*."""
        try:
            rel_path = path.relative_to(root)
            return len(rel_path.parts) <= self._config.MAX_DIRECTORY_DEPTH
        except ValueError:
            return False

    def _extract_file_doc(self, content: str) -> str:
        """Extract a file-level docstring from the first lines of a source file.

        Walks the first FILE_HEADER_MAX_LINES lines looking for a contiguous
        block of comments or a shebang followed by comments. Returns the
        concatenated comment text.

        Args:
            content: Raw file content as a string.

        Returns:
            Extracted file-level docstring or empty string.
        """
        if not content:
            return ""
        lines = content.split("\n")
        max_lines = min(self._config.FILE_HEADER_MAX_LINES, len(lines))
        doc_lines: List[str] = []
        collecting = False
        for i in range(max_lines):
            line = lines[i].strip()
            if not line:
                if collecting:
                    doc_lines.append("")
                continue
            if line.startswith("#!") and i == 0:
                continue
            if line.startswith("#"):
                cleaned = line.lstrip("#").strip()
                doc_lines.append(cleaned)
                collecting = True
            elif line.startswith("//"):
                cleaned = line.lstrip("/").strip()
                doc_lines.append(cleaned)
                collecting = True
            elif line.startswith("/*") or line.startswith("/**"):
                collecting = True
                cleaned = line.lstrip("/*").rstrip("*/").lstrip("*").strip()
                doc_lines.append(cleaned)
                if "*/" in line:
                    break
            elif collecting and ("*/" in line):
                cleaned = line.rstrip("*/").lstrip("*").strip()
                if cleaned:
                    doc_lines.append(cleaned)
                break
            elif collecting:
                break
            else:
                break
        doc = " ".join(doc_lines).strip()
        return doc

    def _emit_progress(self, count: int) -> None:
        """Emit a progress message every PROGRESS_REPORT_BATCH files.

        Args:
            count: Number of files scanned so far.
        """
        batch = self._config.PROGRESS_REPORT_BATCH
        if count > 0 and count % batch == 0:
            print(f"[readmenator] Scanned {count} files...", flush=True)

    def scan(self, root: Path) -> Tuple[List[Node], List[Edge]]:
        """Walk *root* recursively and produce (nodes, edges) for the graph.

        Security checks (symlinks, size, depth, ignore dirs) are applied
        per file. Parse failures are silently caught so a single broken
        file never blocks the rest of the scan.

        Returns:
            A tuple of (list of Node, list of Edge). Edges represent
            ``imports`` relationships between scanned files.
        """
        nodes, edges, _ = self._scan_impl(root)
        return nodes, edges

    def scan_with_content(
        self, root: Path
    ) -> Tuple[List[Node], List[Edge], Dict[str, str]]:
        """Scan and also return raw file contents for deeper analysis.

        Returns:
            Tuple of (nodes, edges, content_map) where content_map maps
            node_id to raw file content.
        """
        return self._scan_impl(root)

    def _scan_impl(
        self, root: Path
    ) -> Tuple[List[Node], List[Edge], Dict[str, str]]:
        """Internal scan implementation returning nodes, edges, and content."""
        nodes: List[Node] = []
        edges: List[Edge] = []
        content_map: Dict[str, str] = {}

        if not root.is_dir():
            raise ValueError(f"Path is not a valid directory: {root}")

        root = root.resolve()
        privacy = self._config.PRIVACY_MODE

        if self._config.GITIGNORE_AWARE:
            self._load_gitignore(root)

        scanned_count = 0

        for file_path in sorted(root.rglob("*")):
            if not file_path.is_file():
                continue

            if not self._validate_path_security(file_path):
                continue

            rel_path = file_path.relative_to(root)
            if self._is_ignored(rel_path):
                continue

            rel_path_str = rel_path.as_posix()
            if self._is_gitignored(rel_path_str):
                continue

            if not self._check_directory_depth(file_path, root):
                continue

            extension = file_path.suffix

            parser = create_parser(extension, rel_path_str, self._config)
            if parser is None:
                continue

            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                file_doc = self._extract_file_doc(content) if not privacy else ""
                parser.parse(content)

                if privacy:
                    parser.symbols = [
                        Symbol(s.name, s.kind, s.line, "", "")
                        for s in parser.symbols
                    ] if hasattr(parser, "symbols") else parser.symbols

                node = Node(
                    node_id=rel_path_str,
                    label=file_path.name,
                    kind="module",
                    language=extension.lstrip("."),
                    doc=file_doc,
                    symbols=parser.symbols,
                )
                nodes.append(node)
                content_map[rel_path_str] = content

                for imp in parser.imports:
                    edges.append(
                        Edge(source=rel_path_str, target=imp, relation="imports")
                    )

                for caller, callee in parser.calls:
                    if caller and callee:
                        edges.append(
                            Edge(
                                source=f"{rel_path_str}::{caller}",
                                target=f"{rel_path_str}::{callee}",
                                relation="calls",
                            )
                        )
                    elif callee:
                        edges.append(
                            Edge(
                                source=rel_path_str,
                                target=callee,
                                relation="calls",
                            )
                        )

                for child, parent in parser.inherits:
                    edges.append(
                        Edge(
                            source=f"{rel_path_str}::{child}",
                            target=parent,
                            relation="inherits",
                        )
                    )

                scanned_count += 1
                self._emit_progress(scanned_count)

            except Exception:
                continue

        return nodes, edges, content_map
