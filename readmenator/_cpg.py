from __future__ import annotations

import hashlib
import json
from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._models import AnalysisResult, Edge, Node, Symbol


class CodePropertyGraph:
    """Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.

    Produces a structured representation merging AST-level symbol data,
    control-flow edges (calls), data-flow edges (imports), and inheritance
    relationships into a single machine-readable document. Designed to be
    embedded in KNOWLEDGE_BASE.md for zero-token agent context.
    """

    CPG_CONTEXT = "https://readmenator.dev/cpg/v1"

    def __init__(self, config: Config) -> None:
        self._config = config

    def generate(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> str:
        """Generate the CPG JSON-LD string embeddable in markdown.

        Returns a compact JSON object with @context, nodes array (each
        containing id, label, kind, language, sha256, symbols, layer),
        edges array (source, target, relation, confidence), and analysis
        metadata (god_nodes, communities).
        """
        cpg_nodes: List[Dict] = []
        node_map: Dict[str, Node] = {n.node_id: n for n in nodes}

        for node in nodes:
            cpg_node: Dict = {
                "id": node.node_id,
                "label": node.label,
                "kind": node.kind,
                "language": node.language,
            }
            if node.doc and not self._config.PRIVACY_MODE:
                cpg_node["doc"] = node.doc
            content_hash = self._compute_node_hash(node)
            cpg_node["sha256"] = content_hash
            cpg_node["symbols"] = self._build_symbol_list(node)
            cpg_node["symbol_count"] = len(node.symbols)
            cpg_nodes.append(cpg_node)

        all_edges = edges + (resolved_edges or [])
        cpg_edges: List[Dict] = []
        for edge in all_edges:
            if edge.source in node_map or edge.source.startswith("ext_"):
                cpg_edges.append({
                    "source": edge.source,
                    "target": edge.target,
                    "relation": edge.relation,
                    "confidence": edge.confidence,
                })

        result: Dict = {
            "@context": self.CPG_CONTEXT,
            "type": "CodePropertyGraph",
            "version": "1.0",
            "generator": "readmenator",
            "metadata": {
                "file_count": len(nodes),
                "symbol_count": sum(len(n.symbols) for n in nodes),
                "edge_count": len(all_edges),
                "language_count": len({n.language for n in nodes}),
            },
            "nodes": cpg_nodes,
            "edges": cpg_edges,
        }

        if analysis:
            result["analysis"] = {
                "god_nodes": [
                    {"node_id": nid, "score": round(score, 2)}
                    for nid, score in analysis.god_nodes
                ],
                "communities": [
                    {
                        "id": c.community_id,
                        "label": c.label,
                        "size": c.size,
                        "cohesion": round(c.cohesion, 3),
                    }
                    for c in analysis.communities
                ],
                "surprising_connections": [
                    {
                        "source": src,
                        "target": tgt,
                        "hops": hops,
                    }
                    for src, tgt, hops, _comms in analysis.surprising_connections
                ],
            }

        return json.dumps(result, indent=None, ensure_ascii=False, sort_keys=True)

    def _build_symbol_list(self, node: Node) -> List[Dict]:
        """Build symbol list for a node, respecting privacy mode."""
        symbols: List[Dict] = []
        for sym in node.symbols:
            entry: Dict = {
                "name": sym.name,
                "kind": sym.kind,
                "line": sym.line,
            }
            if sym.signature:
                entry["signature"] = sym.signature
            if sym.doc and not self._config.PRIVACY_MODE:
                entry["doc"] = sym.doc
            symbols.append(entry)
        return symbols

    @staticmethod
    def _compute_node_hash(node: Node) -> str:
        """Compute a deterministic content hash for a node."""
        parts = [node.node_id, node.label, node.kind, node.language]
        for s in node.symbols:
            parts.extend([s.name, s.kind, str(s.line)])
        raw = "|".join(parts)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
