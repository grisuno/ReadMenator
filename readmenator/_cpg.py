from __future__ import annotations

import hashlib
import json
from typing import Dict, List, Optional

from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding, Symbol


class CodePropertyGraph:
    """Generates a Code Property Graph (CPG) as JSON-LD for AI agent consumption.

    Produces a structured representation merging AST-level symbol data,
    control-flow edges (calls), data-flow edges (imports), inheritance
    relationships, and security findings (with MITRE ATT&CK mappings)
    into a single machine-readable document. Designed to be embedded in
    KNOWLEDGE_BASE.md for zero-token agent context.
    """

    def __init__(self, privacy_mode: bool = False, cpg_context: str = "") -> None:
        self._privacy_mode = privacy_mode
        self._cpg_context = cpg_context

    def generate(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        findings: Optional[List[SecurityFinding]] = None,
    ) -> str:
        """Generate the CPG JSON-LD string embeddable in markdown.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional analysis results for metadata.
            findings: Optional security findings with MITRE ATT&CK IDs.

        Returns:
            Compact JSON-LD string with @context, nodes, edges, analysis,
            and mitre_attack metadata.
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
            if node.doc and not self._privacy_mode:
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
            "@context": self._cpg_context or "https://schema.org",
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

        if findings:
            result["security"] = {
                "total_findings": len(findings),
                "by_severity": self._severity_counts(findings),
                "findings": [
                    {
                        "file_path": f.file_path,
                        "line": f.line,
                        "severity": f.severity,
                        "rule_id": f.rule_id,
                        "description": f.description,
                        "cwe": f.cwe,
                        "mitre_attack": f.mitre_attack,
                    }
                    for f in findings
                ],
            }
            mitre_ids = sorted({f.mitre_attack for f in findings if f.mitre_attack})
            if mitre_ids:
                result["mitre_attack"] = {
                    "techniques": mitre_ids,
                    "count": len(mitre_ids),
                    "mapping": "https://attack.mitre.org/techniques/{id}/",
                }

        return json.dumps(result, indent=None, ensure_ascii=False, sort_keys=True)

    def _severity_counts(self, findings: List[SecurityFinding]) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for f in findings:
            counts[f.severity] = counts.get(f.severity, 0) + 1
        return dict(sorted(counts.items()))

    def _build_symbol_list(self, node: Node) -> List[Dict]:
        symbols: List[Dict] = []
        for sym in node.symbols:
            entry: Dict = {
                "name": sym.name,
                "kind": sym.kind,
                "line": sym.line,
            }
            if sym.signature:
                entry["signature"] = sym.signature
            if sym.doc and not self._privacy_mode:
                entry["doc"] = sym.doc
            symbols.append(entry)
        return symbols

    @staticmethod
    def _compute_node_hash(node: Node) -> str:
        parts = [node.node_id, node.label, node.kind, node.language]
        for s in node.symbols:
            parts.extend([s.name, s.kind, str(s.line)])
        raw = "|".join(parts)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
