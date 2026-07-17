from __future__ import annotations

from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import Edge, LayerViolation, Node


class LayerRuleEngine:
    """Architectural layer violation detection engine.

    Defines a set of permitted and forbidden layer-to-layer import
    rules. Scans all resolved import edges and flags violations
    where one layer imports from another in a way that violates
    the architecture.
    """

    FORBIDDEN_EDGES: Set[Tuple[str, str]] = {
        ("testing", "presentation"),
        ("presentation", "data_access"),
    }

    ALLOWED_EDGES: Set[Tuple[str, str]] = {
        ("testing", "business_logic"),
        ("testing", "infrastructure"),
        ("testing", "data_access"),
    }

    WARN_EDGES: Set[Tuple[str, str]] = {
        ("data_access", "presentation"),
        ("infrastructure", "presentation"),
    }

    def __init__(self, config: Config) -> None:
        self._config = config

    def detect_violations(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
    ) -> List[LayerViolation]:
        """Detect architectural layer violations.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved import edges.
            layers: Dict mapping node_id to layer name. If None, imports
                _layers.LayerDetector for automatic detection.

        Returns:
            List of LayerViolation instances.
        """
        if not nodes or layers is None:
            return []

        all_edges = edges + (resolved_edges or [])
        file_ids: Set[str] = {n.node_id for n in nodes}
        violations: List[LayerViolation] = []

        for edge in all_edges:
            source_layer = layers.get(edge.source)
            target_layer = layers.get(edge.target)

            if source_layer is None or target_layer is None:
                continue
            if source_layer == target_layer:
                continue
            if source_layer == "utility" or target_layer == "utility":
                continue

            pair = (source_layer, target_layer)

            if pair in self.ALLOWED_EDGES:
                continue

            if pair in self.FORBIDDEN_EDGES:
                violations.append(
                    LayerViolation(
                        source_file=edge.source,
                        source_layer=source_layer,
                        target_file=edge.target,
                        target_layer=target_layer,
                        description=f"{source_layer} must not import {target_layer}",
                        severity="strict",
                    )
                )
            elif pair in self.WARN_EDGES:
                if not self._config.LAYER_VIOLATION_STRICT_MODE:
                    continue
                violations.append(
                    LayerViolation(
                        source_file=edge.source,
                        source_layer=source_layer,
                        target_file=edge.target,
                        target_layer=target_layer,
                        description=f"{source_layer} should not import {target_layer} (warn)",
                        severity="warn",
                    )
                )

        violations.sort(key=lambda v: ("strict", "warn", "info").index(v.severity) if v.severity in ("strict", "warn", "info") else 3)

        return violations

    @staticmethod
    def violation_summary(violations: List[LayerViolation]) -> Dict[str, int]:
        """Summarise violations by severity."""
        summary: Dict[str, int] = {}
        for v in violations:
            summary[v.severity] = summary.get(v.severity, 0) + 1
        return summary
