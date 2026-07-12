"""Secure polyglot directory traversal and file analysis.

The scanner walks a directory tree, applies security and size checks,
resolves each supported file through ParserFactory, and returns a
flat list of Node and Edge objects that form the knowledge graph.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple

from readmenator._config import Config
from readmenator._models import Edge, Node
from readmenator._parsers import create_parser


class PolyglotScanner:
    """Recursive directory scanner with security and size guards.

    Rejects symlinks, enforces file-size and directory-depth limits,
    skips ignored directories, and silently catches parse errors
    so a single misbehaving file never breaks the full scan.
    """

    def __init__(self, config: Config) -> None:
        """Initialise the scanner with application configuration.

        Args:
            config: Settings including ignore dirs, size limits, etc.
        """
        self._config = config

    def _is_ignored(self, path: Path) -> bool:
        """Return ``True`` if any path component matches IGNORE_DIRS."""
        return any(part in self._config.IGNORE_DIRS for part in path.parts)

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
        max_len = self._config.DOCSTRING_MAX_LENGTH
        if len(doc) > max_len:
            doc = doc[: max_len - 3] + "..."
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
        nodes: List[Node] = []
        edges: List[Edge] = []

        if not root.is_dir():
            raise ValueError(f"Path is not a valid directory: {root}")

        root = root.resolve()
        scanned_count = 0

        for file_path in sorted(root.rglob("*")):
            if not file_path.is_file():
                continue

            if not self._validate_path_security(file_path):
                continue

            rel_path = file_path.relative_to(root)
            if self._is_ignored(rel_path):
                continue

            if not self._check_directory_depth(file_path, root):
                continue

            rel_path_str = rel_path.as_posix()
            extension = file_path.suffix

            parser = create_parser(extension, rel_path_str, self._config)
            if parser is None:
                continue

            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                file_doc = self._extract_file_doc(content)
                parser.parse(content)

                node = Node(
                    node_id=rel_path_str,
                    label=file_path.name,
                    kind="module",
                    language=extension.lstrip("."),
                    doc=file_doc,
                    symbols=parser.symbols,
                )
                nodes.append(node)

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

        return nodes, edges
