"""Dead code detection for the readmenator knowledge graph.

Identifies orphaned symbols with zero in-degree in the resolved import
graph, excluding known entry points. Generates structured reports
without auto-deleting any code.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Optional, Set

from readmenator._config import Config
from readmenator._models import DeadCodeReport, Edge, Node, Symbol


class DeadCodeStripper:
    """Identifies dead code symbols in the knowledge graph.

    Builds an in-degree map from resolved import edges, then flags
    symbols that are never imported by any other file. Known entry
    points are excluded from the dead code report.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    def identify(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> List[DeadCodeReport]:
        """Identify dead code symbols with zero in-degree.

        Args:
            nodes: Scanned file nodes with symbols.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.

        Returns:
            List of DeadCodeReport instances for orphaned symbols.
        """
        in_degree = self._build_in_degree_map(nodes, resolved_edges)
        entry_points = set(self._config.DEAD_CODE_ENTRY_POINTS)
        reports: List[DeadCodeReport] = []
        for node in nodes:
            for symbol in node.symbols:
                if symbol.name in entry_points:
                    continue
                if in_degree.get(symbol.name, 0) == 0:
                    recommendation = self._classify_recommendation(symbol)
                    reports.append(
                        DeadCodeReport(
                            file_path=node.node_id,
                            symbol_name=symbol.name,
                            symbol_type=symbol.kind,
                            recommendation=recommendation,
                        )
                    )
        reports.sort(key=lambda r: r.file_path)
        return reports

    def _build_in_degree_map(
        self,
        nodes: List[Node],
        resolved_edges: Optional[List[Edge]],
    ) -> Dict[str, int]:
        """Build in-degree count for each symbol name."""
        symbol_names: Set[str] = set()
        for node in nodes:
            for symbol in node.symbols:
                symbol_names.add(symbol.name)
        in_degree: Dict[str, int] = {name: 0 for name in symbol_names}
        if not resolved_edges:
            return in_degree
        node_symbol_map: Dict[str, Set[str]] = defaultdict(set)
        for node in nodes:
            for symbol in node.symbols:
                node_symbol_map[node.node_id].add(symbol.name)
        for edge in resolved_edges:
            target_symbols = node_symbol_map.get(edge.target, set())
            for sym in target_symbols:
                if sym in in_degree:
                    in_degree[sym] += 1
        return in_degree

    def _classify_recommendation(self, symbol: Symbol) -> str:
        """Classify the recommended action for a dead symbol."""
        if symbol.kind in ("class", "struct", "interface", "trait"):
            return "REVIEW"
        if symbol.kind in ("function", "method"):
            return "MOVE_TO_TRASH"
        if symbol.kind in ("variable", "constant"):
            return "MOVE_TO_TRASH"
        return "REVIEW"
