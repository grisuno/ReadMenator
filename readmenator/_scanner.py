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
                parser.parse(content)

                node = Node(
                    node_id=rel_path_str,
                    label=file_path.name,
                    kind="module",
                    language=extension.lstrip("."),
                    doc="",
                    symbols=parser.symbols,
                )
                nodes.append(node)

                for imp in parser.imports:
                    edges.append(
                        Edge(source=rel_path_str, target=imp, relation="imports")
                    )

            except Exception:
                continue

        return nodes, edges
