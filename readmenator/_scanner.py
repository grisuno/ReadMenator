from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple

from readmenator._config import Config
from readmenator._models import Edge, Node
from readmenator._parsers import create_parser


class PolyglotScanner:
    def __init__(self, config: Config) -> None:
        self._config = config

    def _is_ignored(self, path: Path) -> bool:
        return any(part in self._config.IGNORE_DIRS for part in path.parts)

    def _validate_path_security(self, path: Path) -> bool:
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
        try:
            rel_path = path.relative_to(root)
            return len(rel_path.parts) <= self._config.MAX_DIRECTORY_DEPTH
        except ValueError:
            return False

    def scan(self, root: Path) -> Tuple[List[Node], List[Edge]]:
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
