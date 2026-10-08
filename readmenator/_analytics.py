"""Corpus analytics aggregations for the readmenator knowledge graph.

Computes the explorer dashboard payloads (attribution funnel,
distributions, scatter, rule yield) from file-level code graphs so the
force-graph explorer and gallery can render an analytics dashboard
from a single payload.
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List, Optional

from readmenator._config import Config
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    HotspotResult,
    Node,
    SecurityFinding,
)


class AnalyticsBuilder:
    """Builds analytics payloads from scanned topology and findings."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings guarding the analytics flag.
        """
        self._config = config

    def build(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        findings: Optional[List[SecurityFinding]] = None,
        layers: Optional[Dict[str, str]] = None,
        v2: Optional[AnalysisResultV2] = None,
        hotspots: Optional[List[HotspotResult]] = None,
    ) -> Dict[str, Any]:
        """Build the full analytics payload.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional community and god-node analysis.
            findings: Optional security findings.
            layers: Optional file-to-layer mapping.
            v2: Optional deep analysis results.
            hotspots: Optional hotspot ranking override.

        Returns:
            Analytics dictionary with funnel, distributions, and scatter.
        """
        resolved = resolved_edges or []
        fan_out: Counter = Counter()
        fan_in: Counter = Counter()
        for edge in resolved:
            fan_out[edge.source] += 1
            fan_in[edge.target] += 1
        total_symbols = sum(len(node.symbols) for node in nodes)
        communities = list(analysis.communities) if analysis else []
        god_nodes = list(analysis.god_nodes) if analysis else []
        attributed = len({fid for community in communities for fid in community.file_ids})
        payload: Dict[str, Any] = {
            "attribution_funnel": {
                "total": len(nodes),
                "with_symbols": sum(1 for node in nodes if node.symbols),
                "attributed": attributed,
                "god_nodes": len(god_nodes),
                "total_symbols": total_symbols,
            },
            "layer_distribution": self._layer_distribution(nodes, layers),
            "language_distribution": self._language_distribution(nodes),
            "community_cohesion": [
                {
                    "id": community.community_id,
                    "label": community.label,
                    "size": community.size,
                    "cohesion": round(community.cohesion, 3),
                }
                for community in sorted(communities, key=lambda item: item.community_id)
            ],
            "hotspot_ranking": self._hotspot_ranking(nodes, fan_in, fan_out, hotspots),
            "rule_yield": self._rule_yield(findings or []),
            "detection_bands": self._size_bands(nodes),
            "sample_scatter": self._scatter(nodes, fan_in, fan_out, layers),
            "cycles": len(v2.cycles) if v2 else 0,
            "layer_violations": len(v2.layer_violations) if v2 else 0,
        }
        return payload

    def _layer_distribution(
        self, nodes: List[Node], layers: Optional[Dict[str, str]]
    ) -> List[Dict[str, Any]]:
        """Count files per architectural layer."""
        counts: Counter = Counter()
        for node in nodes:
            counts[(layers or {}).get(node.node_id, "unknown")] += 1
        return [
            {"layer": layer, "count": count}
            for layer, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ]

    def _language_distribution(self, nodes: List[Node]) -> List[Dict[str, Any]]:
        """Count files per programming language."""
        counts: Counter = Counter(node.language or "unknown" for node in nodes)
        return [
            {"language": language, "count": count}
            for language, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ]

    def _hotspot_ranking(
        self,
        nodes: List[Node],
        fan_in: Counter,
        fan_out: Counter,
        hotspots: Optional[List[HotspotResult]],
    ) -> List[Dict[str, Any]]:
        """Rank files by combined symbol and connectivity weight."""
        if hotspots:
            return [
                {
                    "file": item.file_id,
                    "score": round(item.combined_score, 3),
                    "symbols": item.symbol_count,
                    "connections": item.connection_count,
                }
                for item in hotspots[: self._config.GOD_NODE_TOP_N]
            ]
        scored = []
        for node in nodes:
            connections = fan_in.get(node.node_id, 0) + fan_out.get(node.node_id, 0)
            score = (
                self._config.HOTSPOT_COMPLEXITY_WEIGHT * len(node.symbols)
                + self._config.HOTSPOT_CENTRALITY_WEIGHT * connections
            )
            scored.append((node.node_id, score, len(node.symbols), connections))
        scored.sort(key=lambda item: (-item[1], item[0]))
        return [
            {"file": file_id, "score": round(score, 3), "symbols": symbols, "connections": connections}
            for file_id, score, symbols, connections in scored[: self._config.GOD_NODE_TOP_N]
        ]

    def _rule_yield(self, findings: List[SecurityFinding]) -> List[Dict[str, Any]]:
        """Count security findings per rule with severity breakdown."""
        by_rule: Dict[str, Dict[str, Any]] = {}
        for finding in findings:
            entry = by_rule.setdefault(
                finding.rule_id,
                {"rule": finding.rule_id, "total": 0, "by_severity": {}},
            )
            entry["total"] += 1
            entry["by_severity"][finding.severity] = entry["by_severity"].get(finding.severity, 0) + 1
        return sorted(by_rule.values(), key=lambda item: (-item["total"], item["rule"]))

    def _size_bands(self, nodes: List[Node]) -> List[Dict[str, Any]]:
        """Bucket files by symbol-count bands."""
        bands = {"0": 0, "1-4": 0, "5-9": 0, "10-19": 0, "20+": 0}
        for node in nodes:
            count = len(node.symbols)
            if count == 0:
                bands["0"] += 1
            elif count <= 4:
                bands["1-4"] += 1
            elif count <= 9:
                bands["5-9"] += 1
            elif count <= 19:
                bands["10-19"] += 1
            else:
                bands["20+"] += 1
        return [{"band": band, "count": count} for band, count in bands.items()]

    def _scatter(
        self,
        nodes: List[Node],
        fan_in: Counter,
        fan_out: Counter,
        layers: Optional[Dict[str, str]],
    ) -> List[Dict[str, Any]]:
        """Build a file scatter of symbols versus connectivity."""
        rows = []
        for node in nodes:
            rows.append(
                {
                    "file": node.node_id,
                    "symbols": len(node.symbols),
                    "connections": fan_in.get(node.node_id, 0) + fan_out.get(node.node_id, 0),
                    "layer": (layers or {}).get(node.node_id),
                    "language": node.language,
                }
            )
        rows.sort(key=lambda item: (-item["connections"], -item["symbols"], item["file"]))
        return rows
