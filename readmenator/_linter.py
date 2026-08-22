"""Architecture linter for the readmenator knowledge graph.

Evaluates files against predefined architectural rules: file length
limits, cross-layer import violations, and circular dependency
detection. All rules are deterministic and token-free.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._layers import LayerDetector
from readmenator._models import Edge, LinterViolation, Node


class ArchitectureLinter:
    """Enforces architectural rules over scanned nodes and edges.

    Checks file length, cross-layer import violations, and circular
    dependencies. Returns structured LinterViolation instances for
    each detected issue.
    """

    FORBIDDEN_IMPORTS: Dict[str, Set[str]] = {
        "presentation": {"data_access", "repository", "database", "dao", "orm", "migration"},
        "testing": {"presentation"},
    }

    def __init__(self, config: Config) -> None:
        self._config = config

    def lint(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> List[LinterViolation]:
        """Run all linter rules and return violations.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            layers: Optional mapping from node_id to layer name.
            content_map: Optional mapping from node_id to file content.

        Returns:
            List of LinterViolation instances sorted by severity.
        """
        violations: List[LinterViolation] = []
        violations.extend(self._check_file_length(nodes, content_map))
        if self._config.LINTER_CROSS_LAYER_VIOLATIONS:
            if layers is None:
                detector = LayerDetector()
                layers = detector.detect(nodes, edges)
            violations.extend(self._check_cross_layer_violations(nodes, edges, resolved_edges, layers))
            violations.extend(self._check_circular_dependencies(nodes, resolved_edges))
        violations.sort(key=lambda v: ("error", "warning", "info").index(v.severity) if v.severity in ("error", "warning", "info") else 3)
        return violations

    def _check_file_length(
        self,
        nodes: List[Node],
        content_map: Optional[Dict[str, str]] = None,
    ) -> List[LinterViolation]:
        """Check files against maximum line count threshold."""
        violations: List[LinterViolation] = []
        max_lines = self._config.LINTER_MAX_LINES
        for node in nodes:
            line_count = 0
            if content_map and node.node_id in content_map:
                line_count = len(content_map[node.node_id].splitlines())
            else:
                try:
                    file_path = Path(node.node_id)
                    if file_path.is_file():
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            line_count = sum(1 for _ in f)
                except (OSError, UnicodeDecodeError):
                    continue
            if line_count > max_lines:
                violations.append(
                    LinterViolation(
                        file_path=node.node_id,
                        rule_id="ARC001",
                        severity="warning",
                        message=f"File exceeds {max_lines} lines ({line_count} lines). Consider modularization.",
                    )
                )
        return violations

    def _check_cross_layer_violations(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]],
        layers: Dict[str, str],
    ) -> List[LinterViolation]:
        """Check for forbidden cross-layer imports."""
        violations: List[LinterViolation] = []
        all_edges = edges + (resolved_edges or [])
        for edge in all_edges:
            source_layer = layers.get(edge.source)
            target_layer = layers.get(edge.target)
            if source_layer is None or target_layer is None:
                continue
            if source_layer == target_layer:
                continue
            if source_layer == "utility" or target_layer == "utility":
                continue
            forbidden = self.FORBIDDEN_IMPORTS.get(source_layer, set())
            if target_layer in forbidden:
                violations.append(
                    LinterViolation(
                        file_path=edge.source,
                        rule_id="ARC002",
                        severity="error",
                        message=f"{source_layer} layer must not import {target_layer} layer. Found edge: {edge.source} -> {edge.target}",
                    )
                )
        return violations

    def _check_circular_dependencies(
        self,
        nodes: List[Node],
        resolved_edges: Optional[List[Edge]],
    ) -> List[LinterViolation]:
        """Check for circular dependencies in the resolved import graph."""
        if not resolved_edges:
            return []
        violations: List[LinterViolation] = []
        file_ids: Set[str] = {n.node_id for n in nodes}
        adj: Dict[str, List[str]] = {}
        for edge in resolved_edges:
            if edge.source in file_ids and edge.target in file_ids:
                adj.setdefault(edge.source, []).append(edge.target)
        WHITE, GRAY, BLACK = 0, 1, 2
        color: Dict[str, int] = {}
        parent: Dict[str, Optional[str]] = {}
        cycles_found: List[List[str]] = []

        def _dfs(current: str) -> None:
            color[current] = GRAY
            for neighbor in adj.get(current, []):
                if neighbor not in color:
                    color[neighbor] = WHITE
                    parent[neighbor] = current
                    _dfs(neighbor)
                elif color[neighbor] == GRAY:
                    cycle: List[str] = [neighbor]
                    node: Optional[str] = current
                    while node is not None and node != neighbor:
                        cycle.append(node)
                        node = parent.get(node)
                    if node == neighbor:
                        cycle.append(neighbor)
                    cycle.reverse()
                    if len(cycle) >= 2:
                        cycles_found.append(cycle)
            color[current] = BLACK

        for n in nodes:
            if n.node_id not in color:
                color[n.node_id] = WHITE
                parent[n.node_id] = None
                _dfs(n.node_id)

        seen_cycles: Set[Tuple[str, ...]] = set()
        for cycle in cycles_found:
            canonical = tuple(sorted(set(cycle)))
            if canonical not in seen_cycles and len(canonical) >= 2:
                seen_cycles.add(canonical)
                cycle_str = " -> ".join(cycle)
                violations.append(
                    LinterViolation(
                        file_path=cycle[0],
                        rule_id="ARC003",
                        severity="warning",
                        message=f"Circular dependency detected: {cycle_str}",
                    )
                )
        return violations
