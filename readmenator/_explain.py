"""Score explanation and path decomposition for the ranking system.

Provides human-readable explanations of why a particular node ranks
where it does, including score breakdown, strongest paths from seeds,
and quality signal summary.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from readmenator._category import Category, Morphism
from readmenator._rank import RankedItem, RankedResult


def explain_rank(
    node_id: str,
    ranked: RankedResult,
    category: Optional[Category] = None,
) -> Optional[str]:
    """Return a detailed breakdown of why *node_id* has its rank.

    Includes score decomposition, seed paths, and quality signals.

    Args:
        node_id: The node to explain.
        ranked: The RankedResult containing scores.
        category: Optional Category for enriched path details.

    Returns:
        Formatted explanation string, or None if node_id not found.
    """
    item = _find_item(node_id, ranked.items)
    if item is None:
        return None

    lines: List[str] = []
    rank = next(
        (i + 1 for i, it in enumerate(ranked.items) if it.node_id == node_id),
        None,
    )
    label = node_id.split("/")[-1]
    lines.append(f"### Why `{label}` ranks #{rank}" if rank else f"### `{label}`")
    lines.append("")

    has_ppr = item.ppr_score > 0
    has_auth = item.authority_score > 0
    has_test = item.test_coverage > 0
    has_doc = item.doc_coverage > 0
    has_fresh = item.freshness > 0

    if any([has_ppr, has_auth, has_test, has_doc, has_fresh]):
        lines.append("**Score decomposition:**")
        lines.append("")
        lines.append("| Signal | Value | Weight | Contribution |")
        lines.append("|--------|-------|--------|-------------|")
        cfg = ranked.config
        if has_ppr:
            contrib = cfg.composite_ppr_weight * item.ppr_score
            lines.append(
                f"| Personalized PageRank | {item.ppr_score:.4f} | "
                f"{cfg.composite_ppr_weight:.2f} | {contrib:.4f} |"
            )
        if has_auth:
            contrib = cfg.composite_authority_weight * item.authority_score
            lines.append(
                f"| Authority (global PR) | {item.authority_score:.4f} | "
                f"{cfg.composite_authority_weight:.2f} | {contrib:.4f} |"
            )
        if has_test:
            contrib = cfg.composite_test_weight * item.test_coverage
            lines.append(
                f"| Test Coverage | {item.test_coverage:.2f} | "
                f"{cfg.composite_test_weight:.2f} | {contrib:.4f} |"
            )
        if has_doc:
            contrib = cfg.composite_doc_weight * item.doc_coverage
            lines.append(
                f"| Doc Coverage | {item.doc_coverage:.2f} | "
                f"{cfg.composite_doc_weight:.2f} | {contrib:.4f} |"
            )
        if has_fresh:
            contrib = cfg.composite_freshness_weight * item.freshness
            lines.append(
                f"| Freshness | {item.freshness:.2f} | "
                f"{cfg.composite_freshness_weight:.2f} | {contrib:.4f} |"
            )
        lines.append(
            f"| **Composite** | **{item.composite_score:.4f}** | **1.00** | **{item.composite_score:.4f}** |"
        )
        lines.append("")

    if ranked.seed_nodes:
        lines.append(f"**Query anchors:** {', '.join(ranked.seed_nodes[:5])}")
        if len(ranked.seed_nodes) > 5:
            extra = len(ranked.seed_nodes) - 5
            lines[-1] += f" (+ {extra} more)"
            lines.append("")

    if item.justification_paths:
        lines.append("**Strongest paths from anchors:**")
        lines.append("")
        for path in item.justification_paths[:3]:
            path_str = " -> ".join(p.split("/")[-1] for p in path)
            lines.append(f"  `{path_str}`")
        lines.append("")

        if category and item.justification_paths:
            lines.append("**Path details (with edge types):**")
            lines.append("")
            for path_nodes in item.justification_paths[:2]:
                for i in range(len(path_nodes) - 1):
                    src, tgt = path_nodes[i], path_nodes[i + 1]
                    for m in category.outgoing(src):
                        if m.target == tgt:
                            lines.append(
                                f"  `{src.split('/')[-1]}` --{m.kind}--> "
                                f"`{tgt.split('/')[-1]}` (w={m.weight:.2f})"
                            )
                            break
                lines.append("")

    signals: List[str] = []
    if item.test_coverage > 0:
        pct = item.test_coverage * 100
        signals.append(f"test coverage ({pct:.0f}%)")
    if item.doc_coverage > 0:
        pct = item.doc_coverage * 100
        signals.append(f"documented ({pct:.0f}%)")
    if signals:
        lines.append(f"**Quality signals:** {', '.join(signals)}")
        lines.append("")

    lines.append(f"**Ranking model:** {ranked.model_version}")
    lines.append("")

    return "\n".join(lines)


def rank_summary(ranked: RankedResult, top_n: int = 5) -> str:
    """Return a short summary of the top-N ranked results."""
    lines: List[str] = [
        f"**Ranked results for:** _{ranked.query}_",
        f"**Model:** {ranked.model_version} | **Seeds:** {len(ranked.seed_nodes)}",
        "",
        "| Rank | File | Composite | PPR | Authority | Test | Doc |",
        "|------|------|-----------|-----|-----------|------|-----|",
    ]
    for i, item in enumerate(ranked.top(top_n)):
        label = item.node_id.split("/")[-1]
        lines.append(
            f"| {i + 1} | `{label}` | "
            f"{item.composite_score:.4f} | "
            f"{item.ppr_score:.4f} | "
            f"{item.authority_score:.4f} | "
            f"{item.test_coverage:.2f} | "
            f"{item.doc_coverage:.2f} |"
        )
    lines.append("")
    return "\n".join(lines)


def _find_item(
    node_id: str, items: List[RankedItem]
) -> Optional[RankedItem]:
    for item in items:
        if item.node_id == node_id:
            return item
    return None
