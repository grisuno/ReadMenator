"""Category theory model for the readmenator code graph.

Defines typed morphisms (edges with semantic kind), objects (file nodes),
and a Category class for algebraic path composition. Every edge in
the knowledge graph carries an EdgeKind that survives through to
ranking computations.

The gain from category theory is that ReadMenator can answer queries
by transformation, not just proximity:

- "What code implements this concept?"  -> documents -> defines
- "What breaks if I change this node?"  -> composition of reverse edges
- "What tests validate this abstraction?" -> defines <- tests
- "How do I get from public API to impl?" -> composite paths
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Set


class EdgeKind(str, Enum):
    """Semantic type of a morphism between two code artifacts."""

    IMPORTS = "imports"
    CALLS = "calls"
    DEFINES = "defines"
    INHERITS = "inherits"
    IMPLEMENTS = "implements"
    TESTS = "tests"
    DOCUMENTS = "documents"
    GENERATES = "generates"
    DEPENDS_ON = "depends_on"
    RESOLVED_IMPORTS = "resolved_imports"

    def __str__(self) -> str:
        return self.value


EDGE_WEIGHTS: Dict[EdgeKind, float] = {
    EdgeKind.CALLS: 1.00,
    EdgeKind.IMPORTS: 0.85,
    EdgeKind.INHERITS: 0.80,
    EdgeKind.IMPLEMENTS: 0.80,
    EdgeKind.DEFINES: 0.70,
    EdgeKind.TESTS: 0.65,
    EdgeKind.DOCUMENTS: 0.45,
    EdgeKind.GENERATES: 0.55,
    EdgeKind.DEPENDS_ON: 0.60,
    EdgeKind.RESOLVED_IMPORTS: 0.85,
}


@dataclass(frozen=True)
class Morphism:
    """A typed directed edge between two code artifacts.

    Attributes:
        source: Node ID of the source artifact.
        target: Node ID of the target artifact.
        kind: Semantic type of the relationship.
        confidence: Confidence score from static analysis (0.0 to 1.0).
    """

    source: str
    target: str
    kind: EdgeKind
    confidence: float = 1.0

    @property
    def weight(self) -> float:
        """Effective weight for ranking = semantic weight * confidence."""
        return EDGE_WEIGHTS.get(self.kind, 0.5) * self.confidence


class Category:
    """A category of code artifacts with typed morphisms.

    Objects are node IDs (file paths or symbol identifiers).
    Morphisms are typed directed edges. Composition follows
    compatible source/target chains respecting edge-kind semantics.
    """

    def __init__(self) -> None:
        self._objects: Set[str] = set()
        self._morphisms: List[Morphism] = []
        self._outgoing: Dict[str, List[Morphism]] = {}
        self._incoming: Dict[str, List[Morphism]] = {}

    def add_object(self, obj_id: str) -> None:
        self._objects.add(obj_id)

    def add_morphism(self, m: Morphism) -> None:
        self._morphisms.append(m)
        self._objects.add(m.source)
        self._objects.add(m.target)
        self._outgoing.setdefault(m.source, []).append(m)
        self._incoming.setdefault(m.target, []).append(m)

    @property
    def objects(self) -> Set[str]:
        return self._objects

    @property
    def morphisms(self) -> List[Morphism]:
        return list(self._morphisms)

    def outgoing(self, obj_id: str) -> List[Morphism]:
        return self._outgoing.get(obj_id, [])

    def incoming(self, obj_id: str) -> List[Morphism]:
        return self._incoming.get(obj_id, [])

    def compose(self, a: Morphism, b: Morphism) -> Optional[Morphism]:
        """Compose two morphisms if target of a matches source of b.

        Returns a new Morphism with composite kind, or None if
        the kinds are incompatible.
        """
        if a.target == b.source:
            composite_kind = self._compose_kind(a.kind, b.kind)
            if composite_kind is not None:
                return Morphism(
                    source=a.source,
                    target=b.target,
                    kind=composite_kind,
                    confidence=a.confidence * b.confidence,
                )
        return None

    def paths(
        self, source: str, target: str, max_depth: int = 10
    ) -> List[List[Morphism]]:
        """Find all composition paths from source to target up to max_depth."""
        results: List[List[Morphism]] = []

        def dfs(
            current: str, goal: str, path: List[Morphism], depth: int
        ) -> None:
            if depth > max_depth:
                return
            if current == goal and path:
                results.append(list(path))
                return
            for m in self._outgoing.get(current, []):
                if m not in path:
                    path.append(m)
                    dfs(m.target, goal, path, depth + 1)
                    path.pop()

        dfs(source, target, [], 0)
        return results

    @staticmethod
    def _compose_kind(a: EdgeKind, b: EdgeKind) -> Optional[EdgeKind]:
        """Determine the composite edge kind.

        Composition rules:
        - imports + defines -> defines (reachable definition)
        - imports + calls -> calls (reachable call)
        - defines + tests -> tests (tested through definition)
        - documents + defines -> documents (documented definition)
        - Same kind -> same kind.
        - Other combinations -> None (incompatible).
        """
        if a == b:
            return a
        composition_map: Dict[tuple, EdgeKind] = {
            (EdgeKind.IMPORTS, EdgeKind.DEFINES): EdgeKind.DEFINES,
            (EdgeKind.IMPORTS, EdgeKind.CALLS): EdgeKind.CALLS,
            (EdgeKind.DEFINES, EdgeKind.TESTS): EdgeKind.TESTS,
            (EdgeKind.DOCUMENTS, EdgeKind.DEFINES): EdgeKind.DOCUMENTS,
            (EdgeKind.IMPORTS, EdgeKind.TESTS): EdgeKind.TESTS,
            (EdgeKind.IMPLEMENTS, EdgeKind.DEFINES): EdgeKind.DEFINES,
        }
        return composition_map.get((a, b))


class TypedGraph:
    """Weighted directed graph for PageRank computations.

    Converts a Category into a stochastic transition matrix suitable
    for eigenvalue computation, preserving edge kind weights.
    """

    def __init__(self, category: Category) -> None:
        self._category = category
        self._node_list: List[str] = sorted(category.objects)
        self._node_index: Dict[str, int] = {
            n: i for i, n in enumerate(self._node_list)
        }
        self._out_weights: Dict[str, float] = {}
        self._compute_out_weights()

    def _compute_out_weights(self) -> None:
        for obj in self._category.objects:
            total = sum(m.weight for m in self._category.outgoing(obj))
            self._out_weights[obj] = total if total > 0 else 0.0

    @property
    def nodes(self) -> List[str]:
        return list(self._node_list)

    @property
    def size(self) -> int:
        return len(self._node_list)

    def node_index(self, node_id: str) -> int:
        return self._node_index.get(node_id, -1)

    def transition_weight(self, source: str, target: str) -> float:
        """Sum of weights of all morphisms from source to target."""
        total = 0.0
        for m in self._category.outgoing(source):
            if m.target == target:
                total += m.weight
        return total

    def stochastic_row(self, source: str) -> Dict[str, float]:
        """Return dict of target -> probability for the row of *source*.

        Probabilities sum to 1.0 if source has outgoing edges.
        Returns empty dict for dangling nodes.
        """
        total = self._out_weights.get(source, 0.0)
        if total == 0.0:
            return {}
        result: Dict[str, float] = {}
        for m in self._category.outgoing(source):
            result[m.target] = result.get(m.target, 0.0) + (m.weight / total)
        return result


def build_category_from_edges(
    edges: List["Edge"],
    resolved_edges: Optional[List["Edge"]] = None,
    node_ids: Optional[Set[str]] = None,
) -> Category:
    """Build a Category from lists of Edge objects.

    Maps Edge.relation strings to EdgeKind where possible.
    Unrecognised relation strings are mapped to DEPENDS_ON.

    Args:
        edges: Raw import edges from the scanner.
        resolved_edges: Optional resolved-import edges.
        node_ids: Optional set of valid node IDs to include.

    Returns:
        A populated Category instance.
    """
    from readmenator._models import Edge as EdgeModel

    cat = Category()
    all_edges: List[EdgeModel] = list(edges)
    if resolved_edges:
        all_edges.extend(resolved_edges)

    for edge in all_edges:
        source = edge.source
        target = edge.target
        if node_ids is not None:
            if source not in node_ids or target not in node_ids:
                continue
        cat.add_object(source)
        cat.add_object(target)
        kind = _infer_edge_kind(edge.relation)
        m = Morphism(
            source=source,
            target=target,
            kind=kind,
            confidence=1.0,
        )
        cat.add_morphism(m)
    return cat


def _infer_edge_kind(relation: str) -> EdgeKind:
    """Map a relation string to an EdgeKind.

    Falls back to DEPENDS_ON for unrecognised strings.
    """
    try:
        return EdgeKind(relation)
    except ValueError:
        return EdgeKind.DEPENDS_ON
