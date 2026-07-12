"""Mermaid graph renderer with intelligent pruning.

Converts the internal Node/Edge graph into a Mermaid flowchart
(string) suitable for embedding in Markdown. Handles node limits,
deduplication, CSS-like class styling, internal import edges, and
community subgraphs.
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import AnalysisResult, Edge, Node


class MermaidRenderer:
    """Renders a knowledge graph to Mermaid JS flowchart syntax.

    Nodes are ordered by import count and symbol richness; the top
    ``MERMAID_MAX_NODES`` entries are included. External dependencies
    (import targets not matching any scanned file) appear as dashed
    boxes. Internal import edges between project files are rendered
    as solid arrows. Community subgraphs group related files when
    analysis results are available.
    """

    def __init__(self, config: Config) -> None:
        """Initialise with configuration for style tokens and node limits.

        Args:
            config: Provides MERMAID_* style strings and MERMAID_MAX_NODES.
        """
        self._config = config

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
        lines.append(f"    classDef mod {self._config.MERMAID_MODULE_STYLE};")
        lines.append(f"    classDef cls {self._config.MERMAID_CLASS_STYLE};")
        lines.append(f"    classDef fn {self._config.MERMAID_FUNCTION_STYLE};")
        lines.append(f"    classDef ext {self._config.MERMAID_EXTERNAL_STYLE};")

        seen_ids: Set[str] = set()
        node_count = 0
        is_truncated = False
        max_nodes = self._config.MERMAID_MAX_NODES

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

            max_symbols = self._config.MERMAID_MAX_SYMBOLS_PER_FILE
            for symbol in node.symbols[:max_symbols]:
                if node_count >= max_nodes:
                    is_truncated = True
                    break
                symbol_id = f"{safe_id}_{self._sanitize_id(symbol.name)}"
                symbol_label = symbol.name.replace('"', '\\"')
                lines.append(f'    {symbol_id}["{symbol_label}"]')
                cls_types = {"class", "struct", "interface", "trait", "enum", "record"}
                if symbol.kind in cls_types:
                    lines.append(f"    class {symbol_id} cls;")
                else:
                    lines.append(f"    class {symbol_id} fn;")
                lines.append(f"    {safe_id} --> {symbol_id}")
                node_count += 1

            if node_count >= max_nodes:
                is_truncated = True
                break

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

        for edge in edges:
            if is_truncated:
                break
            src = self._sanitize_id(edge.source)
            if src not in seen_ids:
                continue
            target_id = self._sanitize_id(f"ext_{edge.target}")
            target_label = edge.target.split("/")[-1].replace('"', '\\"')
            if target_id not in seen_ids:
                if node_count >= max_nodes:
                    is_truncated = True
                    break
                lines.append(f'    {target_id}["{target_label}"]')
                lines.append(f"    class {target_id} ext;")
                seen_ids.add(target_id)
                node_count += 1
            lines.append(f"    {src} -.->|imports| {target_id}")

        return "\n".join(lines), is_truncated
