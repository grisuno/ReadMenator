"""Mermaid graph renderer with intelligent pruning.

Converts the internal Node/Edge graph into a Mermaid flowchart
(string) suitable for embedding in Markdown. Handles node limits,
deduplication, CSS-like class styling, internal import edges, and
community subgraphs.
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Set, Tuple

from readmenator._models import AnalysisResult, Edge, Node


class MermaidRenderer:
    """Renders a knowledge graph to Mermaid JS flowchart syntax.

    Nodes are ordered by import count and symbol richness; the top
    ``max_nodes`` entries are included. External dependencies appear
    as dashed boxes. Internal import edges are solid arrows.
    Community subgraphs group related files when analysis is available.
    """

    def __init__(
        self,
        max_nodes: int = 300,
        max_symbols_per_file: int = 5,
        module_style: str = "fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff",
        class_style: str = "fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff",
        function_style: str = "fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa",
        external_style: str = "fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa",
        internal_edge_style: str = "stroke:#88aaff,stroke-width:1px",
    ) -> None:
        self._max_nodes = max_nodes
        self._max_symbols = max_symbols_per_file
        self._module_style = module_style
        self._class_style = class_style
        self._function_style = function_style
        self._external_style = external_style
        self._internal_edge_style = internal_edge_style

    @staticmethod
    def _sanitize_id(node_id: str) -> str:
        """Convert *node_id* to a Mermaid-safe identifier.

        Replaces non-alphanumeric characters with underscores and
        prepends ``n_`` if the result starts with a digit.
        """
        sanitized = re.sub(r"[^a-zA-Z0-9]", "_", node_id)
        if sanitized and sanitized[0].isdigit():
            sanitized = "n_" + sanitized
        return sanitized

    def render(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> Tuple[str, bool]:
        """Produce a Mermaid flowchart string and a truncation flag.

        Nodes are sorted by import popularity, then by symbol count.
        Internal import edges (between project files) are rendered as
        solid arrows when *resolved_edges* is provided. Community
        subgraphs wrap related files when *analysis* is given.

        Returns:
            Tuple of (Mermaid source string, is_truncated bool).
        """
        lines: List[str] = ["graph TD"]
        lines.append(f"    classDef mod {self._module_style};")
        lines.append(f"    classDef cls {self._class_style};")
        lines.append(f"    classDef fn {self._function_style};")
        lines.append(f"    classDef ext {self._external_style};")

        seen_ids: Set[str] = set()
        node_count = 0
        symbol_count = 0
        is_truncated = False
        max_nodes = self._max_nodes
        max_symbols = self._max_symbols

        import_counts: Dict[str, int] = {node.node_id: 0 for node in nodes}
        for edge in edges:
            if edge.source in import_counts:
                import_counts[edge.source] += 1
        if resolved_edges:
            for edge in resolved_edges:
                if edge.source in import_counts:
                    import_counts[edge.source] += 1

        sorted_nodes = sorted(
            nodes,
            key=lambda n: (import_counts.get(n.node_id, 0), len(n.symbols)),
            reverse=True,
        )

        community_map: Dict[str, int] = {}
        if analysis and analysis.communities:
            for c in analysis.communities:
                for fid in c.file_ids:
                    community_map[fid] = c.community_id

        rendered_communities: Set[int] = set()
        pending_subgraph_close = False

        for node in sorted_nodes:
            safe_id = self._sanitize_id(node.node_id)
            if safe_id in seen_ids:
                continue
            if node_count >= max_nodes:
                is_truncated = True
                break

            comm_id = community_map.get(node.node_id)
            if comm_id is not None and comm_id not in rendered_communities:
                if pending_subgraph_close:
                    lines.append("    end")
                    pending_subgraph_close = False
                comm_nodes = [
                    n for n in sorted_nodes
                    if community_map.get(n.node_id) == comm_id
                    and self._sanitize_id(n.node_id) not in seen_ids
                ]
                if len(comm_nodes) >= 2:
                    label = ""
                    if analysis:
                        for c in analysis.communities:
                            if c.community_id == comm_id:
                                label = c.label
                                break
                    safe_label = label.replace('"', '\\"') if label else f"Community {comm_id}"
                    lines.append(f"    subgraph community_{comm_id} [\"{safe_label}\"]")
                    rendered_communities.add(comm_id)
                    pending_subgraph_close = True

            label = node.label.replace('"', '\\"')
            lines.append(f'    {safe_id}["{label} ({node.language})"]')
            lines.append(f"    class {safe_id} mod;")
            seen_ids.add(safe_id)
            node_count += 1

            if symbol_count < max_symbols:
                sym_limit = max_symbols
            else:
                sym_limit = 0
            for symbol in node.symbols[:sym_limit]:
                symbol_id = f"{safe_id}_{self._sanitize_id(symbol.name)}"
                symbol_label = symbol.name.replace('"', '\\"')
                lines.append(f'    {symbol_id}["{symbol_label}"]')
                cls_types = {"class", "struct", "interface", "trait", "enum", "record"}
                if symbol.kind in cls_types:
                    lines.append(f"    class {symbol_id} cls;")
                else:
                    lines.append(f"    class {symbol_id} fn;")
                lines.append(f"    {safe_id} --> {symbol_id}")
                symbol_count += 1

        if pending_subgraph_close:
            lines.append("    end")

        internal_edge_count = 0
        if resolved_edges and not is_truncated:
            file_ids = {n.node_id for n in nodes}
            for edge in resolved_edges:
                if internal_edge_count >= 100:
                    break
                src_safe = self._sanitize_id(edge.source)
                tgt_safe = self._sanitize_id(edge.target)
                if src_safe not in seen_ids or tgt_safe not in seen_ids:
                    continue
                if edge.source in file_ids and edge.target in file_ids:
                    lines.append(
                        f"    {src_safe} -- {edge.relation} --> {tgt_safe}"
                    )
                    internal_edge_count += 1

        ext_node_count = 0
        for edge in edges:
            if is_truncated:
                break
            src = self._sanitize_id(edge.source)
            if src not in seen_ids:
                continue
            target_id = self._sanitize_id(f"ext_{edge.target}")
            target_label = edge.target.split("/")[-1].replace('"', '\\"')
            if target_id not in seen_ids:
                if ext_node_count >= max_nodes:
                    is_truncated = True
                    break
                lines.append(f'    {target_id}["{target_label}"]')
                lines.append(f"    class {target_id} ext;")
                seen_ids.add(target_id)
                ext_node_count += 1
            lines.append(f"    {src} -.->|imports| {target_id}")

        return "\n".join(lines), is_truncated
