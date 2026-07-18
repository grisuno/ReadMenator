"""PageRank, Personalized PageRank, HITS, and composite scoring.

Provides typed-graph-aware ranking for the readmenator knowledge graph.
Global PageRank measures structural authority; Personalized PageRank
measures query-specific relevance; HITS separates authorities from hubs;
composite scoring combines multiple quality signals into a single
explainable rank.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

from readmenator._category import (
    Category,
    EdgeKind,
    Morphism,
    TypedGraph,
    EDGE_WEIGHTS,
)

HUB_PENALTY_NAMES: Set[str] = {
    "utils", "utils.py", "constants", "constants.py",
    "__init__", "__init__.py", "helpers", "helpers.py",
    "common", "common.py", "base", "base.py",
}


@dataclass
class RankConfig:
    """Tuneable parameters for the ranking system.

    Attributes:
        alpha: Damping factor for PageRank (default 0.85).
        max_iter: Maximum power-iteration steps.
        tolerance: Convergence threshold (L1 norm).
        top_n: Default number of ranked results to return.
        noise_penalty: Multiplier applied to hub-penalty names
            when they are not part of the query seeds.
        composite_ppr_weight: Weight for PPR in composite score.
        composite_authority_weight: Weight for global PageRank.
        composite_test_weight: Weight for test coverage signal.
        composite_doc_weight: Weight for documentation coverage.
        composite_freshness_weight: Weight for code freshness.
    """

    alpha: float = 0.85
    max_iter: int = 100
    tolerance: float = 1e-6
    top_n: int = 10
    noise_penalty: float = 0.7
    composite_ppr_weight: float = 0.45
    composite_authority_weight: float = 0.20
    composite_test_weight: float = 0.15
    composite_doc_weight: float = 0.10
    composite_freshness_weight: float = 0.10


def global_pagerank(
    graph: TypedGraph,
    alpha: float = 0.85,
    max_iter: int = 100,
    tolerance: float = 1e-6,
) -> Dict[str, float]:
    """Compute global PageRank on the typed weighted graph.

    Uses power iteration on the stochastic matrix derived from
    the TypedGraph's edge weights. Dangling nodes (no outgoing
    edges) are handled by uniform random teleportation.

    Args:
        graph: A TypedGraph instance with weighted edges.
        alpha: Damping factor (probability of following an edge).
        max_iter: Maximum power-iteration steps.
        tolerance: Convergence threshold (L1 norm).

    Returns:
        Dict mapping node_id -> PageRank score. Scores sum to 1.0.
    """
    n = graph.size
    if n == 0:
        return {}
    nodes = graph.nodes
    node_to_idx = {nid: i for i, nid in enumerate(nodes)}

    dangling = [
        i for i, nid in enumerate(nodes)
        if not graph.stochastic_row(nid)
    ]
    teleport_prob = 1.0 / n

    r = [1.0 / n] * n

    for _iteration in range(max_iter):
        new_r = [0.0] * n
        dangling_sum = sum(r[i] for i in dangling)

        for i, nid in enumerate(nodes):
            row = graph.stochastic_row(nid)
            if row:
                for tgt, prob in row.items():
                    j = node_to_idx[tgt]
                    new_r[j] += alpha * r[i] * prob

        teleport_mass = (1.0 - alpha) * teleport_prob + alpha * dangling_sum * teleport_prob
        for i in range(n):
            new_r[i] += teleport_mass

        diff = sum(abs(new_r[i] - r[i]) for i in range(n))
        r = new_r
        if diff < tolerance:
            break

    return {nodes[i]: r[i] for i in range(n)}


def personalized_pagerank(
    graph: TypedGraph,
    seeds: Dict[str, float],
    alpha: float = 0.85,
    max_iter: int = 100,
    tolerance: float = 1e-6,
) -> Dict[str, float]:
    """Compute Personalized PageRank with a seed-node preference vector.

    Instead of uniform teleportation, probability mass is distributed
    according to the seed vector. This makes the ranking sensitive to
    a specific query or context.

    Args:
        graph: A TypedGraph instance.
        seeds: Dict mapping seed node_id -> preference mass (sums to 1.0).
        alpha: Damping factor.
        max_iter: Maximum power-iteration steps.
        tolerance: Convergence threshold (L1 norm).

    Returns:
        Dict mapping node_id -> PPR score. Scores sum to 1.0.
    """
    n = graph.size
    if n == 0:
        return {}
    nodes = graph.nodes
    node_to_idx = {nid: i for i, nid in enumerate(nodes)}

    dangling = [
        i for i, nid in enumerate(nodes)
        if not graph.stochastic_row(nid)
    ]

    v = [0.0] * n
    for nid, mass in seeds.items():
        idx = node_to_idx.get(nid)
        if idx is not None:
            v[idx] = mass
    seed_sum = sum(v)
    if seed_sum == 0.0:
        teleport_prob = [1.0 / n] * n
    else:
        teleport_prob = [mass / seed_sum for mass in v]

    r = [1.0 / n] * n

    for _iteration in range(max_iter):
        new_r = [0.0] * n
        dangling_sum = sum(r[i] for i in dangling)

        for i, nid in enumerate(nodes):
            row = graph.stochastic_row(nid)
            if row:
                for tgt, prob in row.items():
                    j = node_to_idx[tgt]
                    new_r[j] += alpha * r[i] * prob

        personalization_mass = (1.0 - alpha) + alpha * dangling_sum
        for i in range(n):
            new_r[i] += personalization_mass * teleport_prob[i]

        diff = sum(abs(new_r[i] - r[i]) for i in range(n))
        r = new_r
        if diff < tolerance:
            break

    return {nodes[i]: r[i] for i in range(n)}


def hits(
    graph: TypedGraph,
    max_iter: int = 100,
    tolerance: float = 1e-6,
) -> Tuple[Dict[str, float], Dict[str, float]]:
    """Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.

    Authorities are nodes with many incoming edges from good hubs.
    Hubs are nodes with many outgoing edges to good authorities.

    Returns:
        Tuple of (authorities, hubs) as dicts mapping node_id -> score.
        Scores are L2-normalised.
    """
    n = graph.size
    if n == 0:
        return {}, {}
    nodes = graph.nodes
    node_to_idx = {nid: i for i, nid in enumerate(nodes)}

    a = [1.0] * n
    h = [1.0] * n

    for _iteration in range(max_iter):
        new_a = [0.0] * n
        new_h = [0.0] * n

        for i, nid in enumerate(nodes):
            row = graph.stochastic_row(nid)
            for tgt, prob in row.items():
                j = node_to_idx[tgt]
                new_a[j] += h[i] * prob
                new_h[i] += a[j] * prob

        a_norm = math.sqrt(sum(x * x for x in new_a)) or 1.0
        h_norm = math.sqrt(sum(x * x for x in new_h)) or 1.0
        for i in range(n):
            new_a[i] /= a_norm
            new_h[i] /= h_norm

        diff_a = sum(abs(new_a[i] - a[i]) for i in range(n))
        diff_h = sum(abs(new_h[i] - h[i]) for i in range(n))
        a, h = new_a, new_h
        if diff_a < tolerance and diff_h < tolerance:
            break

    authorities = {nodes[i]: a[i] for i in range(n)}
    hubs = {nodes[i]: h[i] for i in range(n)}
    return authorities, hubs


def build_seeds_from_query(
    query: str,
    node_ids: List[str],
    node_labels: Dict[str, str],
    symbols: Dict[str, List[str]],
) -> Dict[str, float]:
    """Build a PPR seed vector from a natural-language query string.

    Matches query tokens against node IDs, labels, and symbol names.
    Seeds are assigned equal mass. If no match is found, returns
    empty dict (will use uniform teleportation).

    Args:
        query: Free-text query string.
        node_ids: All valid node IDs.
        node_labels: Mapping from node_id -> display label.
        symbols: Mapping from node_id -> list of symbol names.

    Returns:
        Dict of seed node_id -> equal mass fraction.
    """
    terms = set(query.lower().split())
    matched: Set[str] = set()

    for nid in node_ids:
        nid_lower = nid.lower()
        label_lower = node_labels.get(nid, "").lower()
        syms = [s.lower() for s in symbols.get(nid, [])]

        for term in terms:
            if len(term) < 2:
                continue
            if term in nid_lower or term in label_lower:
                matched.add(nid)
                break
            if any(term in s for s in syms):
                matched.add(nid)
                break

    if not matched:
        return {}

    mass = 1.0 / len(matched)
    return {nid: mass for nid in matched}


def build_seeds_for_context(
    node_ids: List[str],
    anchor_patterns: List[str],
) -> Dict[str, float]:
    """Build a PPR seed vector from anchor pattern strings.

    Nodes whose ID or label contains any anchor pattern receive
    equal seed mass. Useful for section-level seeding.

    Args:
        node_ids: All valid node IDs.
        anchor_patterns: List of substrings to match.

    Returns:
        Dict of seed node_id -> equal mass fraction.
    """
    matched: Set[str] = set()
    patterns_lower = [p.lower() for p in anchor_patterns]

    for nid in node_ids:
        nid_lower = nid.lower()
        for pat in patterns_lower:
            if pat in nid_lower:
                matched.add(nid)
                break

    if not matched:
        return {}

    mass = 1.0 / len(matched)
    return {nid: mass for nid in matched}


@dataclass
class RankedItem:
    """A single ranked result with score decomposition.

    Attributes:
        node_id: The ranked node ID.
        composite_score: Final multi-signal score.
        ppr_score: Personalized PageRank contribution.
        authority_score: Global PageRank contribution.
        test_coverage: Fraction of symbols referenced in test files.
        doc_coverage: Fraction of symbols with documentation.
        freshness: Decay-weighted recency signal.
        justification_paths: Shortest paths from seed nodes to this node.
    """

    node_id: str
    composite_score: float
    ppr_score: float
    authority_score: float
    test_coverage: float = 0.0
    doc_coverage: float = 0.0
    freshness: float = 0.0
    justification_paths: List[List[str]] = field(default_factory=list)

    @property
    def label(self) -> str:
        return self.node_id.split("/")[-1]


@dataclass
class RankedResult:
    """Complete ranking result for a query or context.

    Attributes:
        query: The query string or context label.
        items: Ranked items in descending score order.
        config: The RankConfig used.
        seed_nodes: The seed node IDs used for PPR.
        model_version: Version identifier for the ranking model.
    """

    query: str
    items: List[RankedItem]
    config: RankConfig
    seed_nodes: List[str]
    model_version: str = "v1.0"

    def top(self, n: int = 10) -> List[RankedItem]:
        return self.items[:n]

    def explain(self, node_id: str) -> Optional[str]:
        """Return a human-readable explanation of why *node_id* ranks as it does."""
        for item in self.items:
            if item.node_id == node_id:
                return _format_explanation(item, self)
        return None


class CompositeRanker:
    """Combines PPR, authority, test/doc coverage, and freshness.

    Produces a single composite score per node:
    S_q(n) = w_ppr * PPR_q(n) + w_auth * Auth(n) + w_test * Test(n)
           + w_doc * Doc(n) + w_fresh * Fresh(n)
    """

    def __init__(
        self,
        graph: TypedGraph,
        config: Optional[RankConfig] = None,
    ):
        self._graph = graph
        self._config = config or RankConfig()
        self._global_pr: Optional[Dict[str, float]] = None

    def _get_global_pr(self) -> Dict[str, float]:
        if self._global_pr is None:
            self._global_pr = global_pagerank(
                self._graph,
                alpha=self._config.alpha,
                max_iter=self._config.max_iter,
                tolerance=self._config.tolerance,
            )
        return self._global_pr

    def rank(
        self,
        query: str,
        seeds: Dict[str, float],
        category: Category,
        node_ids: List[str],
        test_coverage: Optional[Dict[str, float]] = None,
        doc_coverage: Optional[Dict[str, float]] = None,
        freshness: Optional[Dict[str, float]] = None,
    ) -> RankedResult:
        """Compute composite ranking for a query.

        Args:
            query: Query string.
            seeds: PPR seed vector.
            category: Category with morphisms for path finding.
            node_ids: All valid node IDs.
            test_coverage: Optional dict of node_id -> test coverage (0-1).
            doc_coverage: Optional dict of node_id -> doc coverage (0-1).
            freshness: Optional dict of node_id -> freshness (0-1).

        Returns:
            A RankedResult with scored and sorted items.
        """
        ppr = personalized_pagerank(
            self._graph,
            seeds,
            alpha=self._config.alpha,
            max_iter=self._config.max_iter,
            tolerance=self._config.tolerance,
        )
        global_pr = self._get_global_pr()

        cfg = self._config
        seed_ids = list(seeds.keys())
        scored: List[RankedItem] = []

        for nid in node_ids:
            ppr_val = ppr.get(nid, 0.0)
            auth_val = global_pr.get(nid, 0.0)
            test_val = test_coverage.get(nid, 0.0) if test_coverage else 0.0
            doc_val = doc_coverage.get(nid, 0.0) if doc_coverage else 0.0
            fresh_val = freshness.get(nid, 0.0) if freshness else 0.0

            composite = (
                cfg.composite_ppr_weight * ppr_val
                + cfg.composite_authority_weight * auth_val
                + cfg.composite_test_weight * test_val
                + cfg.composite_doc_weight * doc_val
                + cfg.composite_freshness_weight * fresh_val
            )

            label = nid.split("/")[-1]
            if label in HUB_PENALTY_NAMES:
                has_seed = any(
                    pat in nid.lower()
                    for pat in seeds
                )
                if not has_seed:
                    composite *= cfg.noise_penalty

            paths = self._find_justification_paths(nid, seed_ids, category)

            scored.append(RankedItem(
                node_id=nid,
                composite_score=composite,
                ppr_score=ppr_val,
                authority_score=auth_val,
                test_coverage=test_val,
                doc_coverage=doc_val,
                freshness=fresh_val,
                justification_paths=paths,
            ))

        scored.sort(key=lambda x: x.composite_score, reverse=True)
        return RankedResult(
            query=query,
            items=scored,
            config=cfg,
            seed_nodes=seed_ids,
        )

    def _find_justification_paths(
        self,
        target: str,
        seed_ids: List[str],
        category: Category,
        max_paths: int = 3,
    ) -> List[List[str]]:
        """Find shortest paths from any seed to target."""
        paths: List[List[str]] = []
        for seed in seed_ids:
            if seed == target:
                paths.append([seed])
                continue
            found = category.paths(seed, target, max_depth=8)
            for p in found:
                node_chain = [seed]
                for m in p:
                    node_chain.append(m.target)
                paths.append(node_chain)
                if len(paths) >= max_paths:
                    break
            if len(paths) >= max_paths:
                break
        return paths


def _format_explanation(item: RankedItem, result: RankedResult) -> str:
    """Format a human-readable explanation for a ranked item."""
    lines: List[str] = []
    lines.append(f"### Why `{item.label}` ranks #{result.items.index(item) + 1}")
    lines.append("")
    lines.append(f"- Personalized PageRank: {item.ppr_score:.4f}")
    lines.append(f"- Authority (global PR): {item.authority_score:.4f}")
    lines.append(f"- Composite score: {item.composite_score:.4f}")
    lines.append("")
    lines.append(f"**Reached from query anchors:** {', '.join(result.seed_nodes[:5])}")
    if item.justification_paths:
        lines.append("")
        lines.append("**Strongest paths:**")
        for path in item.justification_paths[:3]:
            path_str = " -> ".join(p.split("/")[-1] for p in path)
            lines.append(f"  - {path_str}")
    lines.append("")
    signals: List[str] = []
    if item.test_coverage > 0:
        signals.append(f"tested ({item.test_coverage:.0%})")
    if item.doc_coverage > 0:
        signals.append(f"documented ({item.doc_coverage:.0%})")
    if signals:
        lines.append(f"**Quality signals:** {', '.join(signals)}")
    lines.append("")
    return "\n".join(lines)
