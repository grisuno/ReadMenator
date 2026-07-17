from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import (
    ChangeImpact,
    DependencyCycle,
    Edge,
    HotspotResult,
    Node,
)


class HotspotAnalyzer:
    """Hotspot detection, cycle analysis, and change impact analysis.

    Hotspots are files with high complexity (many symbols) and high
    centrality (many connections). Cycle detection finds circular
    dependencies in the resolved import graph. Change impact analysis
    computes transitive-dependent lists for every file.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    def analyze_hotspots(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> List[HotspotResult]:
        """Rank files by combined complexity and centrality scores.

        Complexity is normalised symbol count. Centrality is normalised
        connection count (in-degree + out-degree). The combined score
        uses configured weights.
        """
        if not nodes:
            return []

        all_edges = edges + (resolved_edges or [])
        symbol_counts: Dict[str, int] = {n.node_id: len(n.symbols) for n in nodes}
        connection_counts: Dict[str, int] = defaultdict(int)
        file_ids: Set[str] = {n.node_id for n in nodes}

        for edge in all_edges:
            if edge.source in file_ids:
                connection_counts[edge.source] += 1
            if edge.target in file_ids:
                connection_counts[edge.target] += 1

        max_symbols = max(symbol_counts.values()) if symbol_counts else 1
        max_connections = max(connection_counts.values()) if connection_counts else 1

        complexity_weight = self._config.HOTSPOT_COMPLEXITY_WEIGHT
        centrality_weight = self._config.HOTSPOT_CENTRALITY_WEIGHT

        results: List[HotspotResult] = []
        for node in nodes:
            nid = node.node_id
            sym_count = symbol_counts.get(nid, 0)
            conn_count = connection_counts.get(nid, 0)
            complexity_score = sym_count / max(max_symbols, 1)
            centrality_score = conn_count / max(max_connections, 1)
            combined = (complexity_score * complexity_weight) + (
                centrality_score * centrality_weight
            )
            results.append(
                HotspotResult(
                    file_id=nid,
                    complexity_score=round(complexity_score, 4),
                    centrality_score=round(centrality_score, 4),
                    combined_score=round(combined, 4),
                    symbol_count=sym_count,
                    connection_count=conn_count,
                )
            )

        results.sort(key=lambda r: r.combined_score, reverse=True)
        return results

    def detect_cycles(
        self,
        nodes: List[Node],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> List[DependencyCycle]:
        """Detect cycles in the resolved import graph using DFS.

        Uses Tarjan's algorithm variant with three-colour DFS to find
        all elementary cycles. Returns each cycle as a DependencyCycle.
        """
        if not nodes or not resolved_edges:
            return []

        adj: Dict[str, List[str]] = defaultdict(list)
        file_ids: Set[str] = {n.node_id for n in nodes}
        for edge in resolved_edges:
            if edge.source in file_ids and edge.target in file_ids:
                adj[edge.source].append(edge.target)

        cycles: List[DependencyCycle] = []
        WHITE, GRAY, BLACK = 0, 1, 2
        color: Dict[str, int] = {}
        parent: Dict[str, Optional[str]] = {}

        def _dfs_visit(current: str) -> None:
            color[current] = GRAY
            for neighbor in adj.get(current, []):
                if neighbor not in color:
                    color[neighbor] = WHITE
                    parent[neighbor] = current
                    _dfs_visit(neighbor)
                elif color[neighbor] == GRAY:
                    _record_cycle(neighbor, current)
            color[current] = BLACK

        def _record_cycle(start: str, end: str) -> None:
            cycle_path: List[str] = [start]
            node: Optional[str] = end
            while node is not None and node != start:
                cycle_path.append(node)
                node = parent.get(node)
            if node == start or not node:
                cycle_path.append(start)
            cycle_path.reverse()
            if len(cycle_path) >= 3:
                deduped: List[str] = []
                seen_in_cycle: Set[str] = set()
                for n in cycle_path:
                    if n not in seen_in_cycle:
                        seen_in_cycle.add(n)
                        deduped.append(n)
                if len(deduped) >= 2:
                    cycles.append(
                        DependencyCycle(cycle=list(deduped), length=len(deduped))
                    )

        for n in nodes:
            if n.node_id not in color:
                color[n.node_id] = WHITE
                parent[n.node_id] = None
                _dfs_visit(n.node_id)

        cycles.sort(key=lambda c: c.length, reverse=True)
        return cycles

    def analyze_change_impact(
        self,
        nodes: List[Node],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> List[ChangeImpact]:
        """Compute change impact for every file in the project.

        For each file, finds all files that would be affected if it
        changed (direct and transitive dependents via reverse import
        graph traversal).
        """
        if not nodes:
            return []

        rev_adj: Dict[str, Set[str]] = defaultdict(set)
        file_ids: Set[str] = {n.node_id for n in nodes}
        for edge in resolved_edges or []:
            if edge.source in file_ids and edge.target in file_ids:
                rev_adj[edge.target].add(edge.source)

        max_depth = self._config.CHANGE_IMPACT_MAX_DEPTH
        max_files = self._config.CHANGE_IMPACT_MAX_FILES
        results: List[ChangeImpact] = []

        for node in nodes:
            dependents: Set[str] = set()
            visited: Set[str] = {node.node_id}
            queue: deque = deque()
            queue.append((node.node_id, 0))

            while queue and len(dependents) < max_files:
                current, depth = queue.popleft()
                if depth >= max_depth:
                    continue
                for dependent in rev_adj.get(current, set()):
                    if dependent not in visited:
                        visited.add(dependent)
                        dependents.add(dependent)
                        queue.append((dependent, depth + 1))

            direct: List[str] = sorted(
                d for d in rev_adj.get(node.node_id, set()) if d in file_ids
            )
            transitive: List[str] = sorted(
                d for d in dependents if d not in direct
            )

            results.append(
                ChangeImpact(
                    file_id=node.node_id,
                    direct_dependents=direct[:max_files],
                    transitive_dependents=transitive[:max_files],
                    total_impact=len(dependents),
                )
            )

        results.sort(key=lambda r: r.total_impact, reverse=True)
        return results
