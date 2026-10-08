"""Synthesized scan-text builder for the readmenator knowledge graph.

Flattens per-file metadata (names, symbols, imports, docs, content
snippets) into a single searchable text blob. The blob is the shared
input for YARA-lite matching, provenance auditing, and embedding.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._models import Edge, Node


class ScanTextBuilder:
    """Builds searchable scan-text blobs from scanned nodes."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for symbol/import/snippet budgets.
        """
        self._config = config

    def build_for_node(
        self,
        node: Node,
        content: str = "",
        imports: Optional[List[str]] = None,
    ) -> str:
        """Build the scan-text blob for a single file node.

        Args:
            node: Scanned file node with symbols and docs.
            content: Optional raw file content for snippet inclusion.
            imports: Optional raw import strings for the file.

        Returns:
            Newline-joined scan text with labelled sections.
        """
        parts: List[str] = []
        parts.append(f"file: {node.node_id}")
        parts.append(f"label: {node.label}")
        parts.append(f"language: {node.language}")
        if node.doc and not self._config.PRIVACY_MODE:
            parts.append(f"doc: {node.doc}")
        symbol_names = [s.name for s in node.symbols[: self._config.SCANTEXT_MAX_SYMBOLS]]
        if symbol_names:
            parts.append("symbols: " + " ".join(symbol_names))
        signatures: List[str] = []
        if not self._config.PRIVACY_MODE:
            for symbol in node.symbols[: self._config.SCANTEXT_MAX_SYMBOLS]:
                if symbol.signature:
                    signatures.append(symbol.signature)
        if signatures:
            parts.append("signatures: " + " | ".join(signatures))
        import_list = imports if imports is not None else []
        if import_list:
            parts.append("imports: " + " ".join(import_list[: self._config.SCANTEXT_MAX_IMPORTS]))
        if content and not self._config.PRIVACY_MODE:
            snippet = content[: self._config.SCANTEXT_SNIPPET_CHARS].replace("\n", " ")
            parts.append(f"content: {snippet}")
        return "\n".join(parts)

    def build_corpus(
        self,
        nodes: List[Node],
        content_map: Optional[Dict[str, str]] = None,
        edges: Optional[List[Edge]] = None,
    ) -> Dict[str, str]:
        """Build scan-text blobs for every node in the corpus.

        Args:
            nodes: Scanned file nodes.
            content_map: Optional mapping of node_id to raw content.
            edges: Optional import edges used as per-file import lists.

        Returns:
            Mapping of node_id to scan-text blob.
        """
        imports_by_source: Dict[str, List[str]] = {}
        for edge in edges or []:
            imports_by_source.setdefault(edge.source, []).append(edge.target)
        result: Dict[str, str] = {}
        for node in nodes:
            content = (content_map or {}).get(node.node_id, "")
            result[node.node_id] = self.build_for_node(
                node, content=content, imports=imports_by_source.get(node.node_id, [])
            )
        return result
