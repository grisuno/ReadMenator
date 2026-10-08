"""Optional semantic embeddings for the readmenator knowledge graph.

Provides sentence-transformer encoding with HDBSCAN clustering and
UMAP/t-SNE projection when the optional dependencies are installed,
and a deterministic zero-dependency Jaccard fallback otherwise. The
fallback keeps `near` queries and similarity grouping available
offline without extra packages.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Any, Dict, List, Tuple

from readmenator._config import Config

_TOKEN_RE = re.compile(r"[A-Za-z0-9_]{2,}")


def _tokens(text: str) -> Counter:
    """Tokenize scan text into a lowercase term counter."""
    return Counter(match.group(0).lower() for match in _TOKEN_RE.finditer(text or ""))


def _jaccard(left: Counter, right: Counter) -> float:
    """Compute Jaccard similarity between two token counters."""
    if not left or not right:
        return 0.0
    left_keys = set(left)
    right_keys = set(right)
    union = left_keys | right_keys
    if not union:
        return 0.0
    return len(left_keys & right_keys) / len(union)


class Embedder:
    """Encodes scan-text blobs and answers similarity queries."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for model name and neighbor budgets.
        """
        self._config = config

    def dependencies_available(self) -> bool:
        """Return True when sentence-transformers is importable."""
        try:
            __import__("sentence_transformers")
            return True
        except ImportError:
            return False

    def encode(self, texts: List[str]) -> List[List[float]]:
        """Encode texts into L2-normalized vectors when available.

        Args:
            texts: Scan-text blobs to encode.

        Returns:
            List of float vectors; empty when dependencies are missing.
        """
        if not self.dependencies_available():
            return []
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(self._config.EMBED_MODEL)
        vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return [[float(value) for value in row] for row in vectors]

    def near_jaccard(
        self, query: str, corpus: Dict[str, str], top_k: int = 0
    ) -> List[Dict[str, Any]]:
        """Find nearest neighbors with offline Jaccard similarity.

        Args:
            query: Query scan text or file identifier present in corpus.
            corpus: Mapping of file identifier to scan text.
            top_k: Maximum neighbors to return (0 uses config default).

        Returns:
            Neighbor list sorted by descending similarity score.
        """
        limit = top_k or self._config.EMBED_MAX_NEIGHBORS
        query_text = corpus.get(query, query)
        query_tokens = _tokens(query_text)
        scored: List[Tuple[str, float]] = []
        for file_id, text in corpus.items():
            if file_id == query:
                continue
            scored.append((file_id, _jaccard(query_tokens, _tokens(text))))
        scored.sort(key=lambda item: (-item[1], item[0]))
        return [{"file": file_id, "score": round(score, 4)} for file_id, score in scored[:limit]]

    def cluster_jaccard(
        self, corpus: Dict[str, str], threshold: float = 0.08
    ) -> List[List[str]]:
        """Group files into similarity clusters with union-find.

        Args:
            corpus: Mapping of file identifier to scan text.
            threshold: Minimum Jaccard similarity to link two files.

        Returns:
            Clusters with at least EMBED_MIN_CLUSTER_SIZE members.
        """
        files = sorted(corpus)
        tokenized = {file_id: _tokens(corpus[file_id]) for file_id in files}
        parent = {file_id: file_id for file_id in files}

        def find(item: str) -> str:
            """Find the union-find root for an item."""
            while parent[item] != item:
                parent[item] = parent[parent[item]]
                item = parent[item]
            return item

        def union(left: str, right: str) -> None:
            """Merge two union-find sets."""
            parent[find(left)] = find(right)

        for index, left in enumerate(files):
            for right in files[index + 1 :]:
                if _jaccard(tokenized[left], tokenized[right]) >= threshold:
                    union(left, right)
        groups: Dict[str, List[str]] = {}
        for file_id in files:
            groups.setdefault(find(file_id), []).append(file_id)
        return sorted(
            [sorted(members) for members in groups.values() if len(members) >= self._config.EMBED_MIN_CLUSTER_SIZE],
            key=lambda members: (-len(members), members[0] if members else ""),
        )

    def project_jaccard(self, corpus: Dict[str, str]) -> List[Dict[str, Any]]:
        """Project files to 2D with a deterministic radial layout.

        Args:
            corpus: Mapping of file identifier to scan text.

        Returns:
            Points normalized to the [-1, 1] square.
        """
        files = sorted(corpus)
        if not files:
            return []
        tokenized = {file_id: _tokens(corpus[file_id]) for file_id in files}
        totals = {file_id: max(1, sum(tokenized[file_id].values())) for file_id in files}
        points = []
        for index, file_id in enumerate(files):
            angle = 2.0 * math.pi * index / max(1, len(files))
            radius = min(1.0, math.log2(totals[file_id] + 1) / 8.0)
            points.append(
                {
                    "file": file_id,
                    "x": round(radius * math.cos(angle), 4),
                    "y": round(radius * math.sin(angle), 4),
                }
            )
        return points
