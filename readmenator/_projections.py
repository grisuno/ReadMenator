"""Functors and projections for the readmenator code category.

Defines projection functors that preserve structure but change the
point of view: F_docs (code -> documentation), F_risk (code -> risk),
and view-based projections for architecture, execution, quality, and
change impact analysis.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Protocol, Set

from readmenator._category import Category, EdgeKind, Morphism
from readmenator._models import Node


class Projection(Protocol):
    """A functor from C_code to another category.

    Maps nodes and morphisms while preserving composition structure.
    """

    def map_node(self, node: Node) -> Optional[Node]:
        """Map a code node. Return None to exclude."""
        ...

    def map_morphism(self, m: Morphism) -> Optional[Morphism]:
        """Map a morphism. Return None to exclude."""
        ...


class IdentityProjection:
    """Identity functor: maps everything to itself."""

    def map_node(self, node: Node) -> Optional[Node]:
        return node

    def map_morphism(self, m: Morphism) -> Optional[Morphism]:
        return m


class DocProjection:
    """F_docs: project code to documentation.

    Keeps only nodes that have docstrings or are referenced in README.
    Useful for quantifying documentation gaps.
    """

    def __init__(self, documented_ids: Set[str]) -> None:
        self._documented_ids = documented_ids

    def map_node(self, node: Node) -> Optional[Node]:
        if node.node_id in self._documented_ids or node.doc:
            return node
        return None

    def map_morphism(self, m: Morphism) -> Optional[Morphism]:
        if m.kind in (EdgeKind.DOCUMENTS, EdgeKind.IMPORTS, EdgeKind.DEFINES):
            return m
        return None


class RiskProjection:
    """F_risk: project code to risk/fragility nodes.

    Nodes are transformed with risk attributes: fan-in, fan-out,
    symbol count, test absence, and public API exposure.
    """

    def __init__(
        self,
        fan_in: Dict[str, int],
        fan_out: Dict[str, int],
        test_files: Set[str],
    ) -> None:
        self._fan_in = fan_in
        self._fan_out = fan_out
        self._test_files = test_files

    def map_node(self, node: Node) -> Optional[Node]:
        fi = self._fan_in.get(node.node_id, 0)
        fo = self._fan_out.get(node.node_id, 0)
        has_tests = node.node_id in self._test_files
        risk_score = fi * 2 + fo + len(node.symbols) * 0.5
        if has_tests:
            risk_score *= 0.5
        if risk_score > 0 or node.doc:
            return node
        return None

    def map_morphism(self, m: Morphism) -> Optional[Morphism]:
        return m


def apply_view(
    category: Category,
    view_config: Dict,
) -> Category:
    """Apply a named view to produce a projected category.

    View config format::
        {
            "edge_types": [EdgeKind.IMPORTS, EdgeKind.DEFINES, ...],
            "direction": "forward" | "reverse",  # default "forward"
        }

    Args:
        category: Source category.
        view_config: View definition dict.

    Returns:
        A new Category with only matching morphisms.
    """
    allowed_kinds: List[EdgeKind] = view_config.get("edge_types", [])
    direction: str = view_config.get("direction", "forward")
    allowed_set = set(allowed_kinds)

    projected = Category()
    obj_set: Set[str] = set()

    for m in category.morphisms:
        if m.kind not in allowed_set:
            continue
        if direction == "reverse":
            m = Morphism(
                source=m.target,
                target=m.source,
                kind=m.kind,
                confidence=m.confidence,
            )
        obj_set.add(m.source)
        obj_set.add(m.target)
        projected.add_morphism(m)

    for obj in obj_set:
        projected.add_object(obj)

    return projected


# Predefined view configurations
VIEWS: Dict[str, Dict] = {
    "architecture": {
        "edge_types": [
            EdgeKind.IMPORTS,
            EdgeKind.DEFINES,
            EdgeKind.INHERITS,
            EdgeKind.IMPLEMENTS,
        ],
        "direction": "forward",
    },
    "execution": {
        "edge_types": [EdgeKind.CALLS],
        "direction": "forward",
    },
    "quality": {
        "edge_types": [
            EdgeKind.TESTS,
            EdgeKind.DOCUMENTS,
        ],
        "direction": "forward",
    },
    "change_impact": {
        "edge_types": [
            EdgeKind.IMPORTS,
            EdgeKind.CALLS,
        ],
        "direction": "reverse",
    },
    "security": {
        "edge_types": [
            EdgeKind.IMPORTS,
            EdgeKind.CALLS,
            EdgeKind.DEPENDS_ON,
        ],
        "direction": "forward",
    },
}
