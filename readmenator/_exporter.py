"""Multi-format exporter for the readmenator knowledge graph.

Produces JSON (GraphRAG-ready node-link format), interactive HTML
(vis.js standalone), and static SVG (matplotlib-based) outputs from
the scanned nodes, edges, and optional analysis results.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._models import AnalysisResult, Edge, Node


class GraphExporter:
    """Exports the knowledge graph to JSON, HTML, and SVG formats.

    Each method is self-contained and produces a single file. No
    external network calls are made; the HTML file embeds vis.js
    from a CDN reference for offline-compatible rendering.
    """

    def __init__(self, config: Config):
        """Initialise with application configuration.

        Args:
            config: Settings for export styling and limits.
        """
        self._config = config

    def to_json(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> str:
        """Export the graph as a node-link JSON string.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional analysis results for metadata.

        Returns:
            JSON string with nodes, edges, and optional analysis metadata.
        """
        all_edges = edges + (resolved_edges or [])
        node_data = []
        for node in nodes:
            nd = {
                "id": node.node_id,
                "label": node.label,
                "kind": node.kind,
                "language": node.language,
                "doc": node.doc,
                "symbols": [
                    {
                        "name": s.name,
                        "kind": s.kind,
                        "line": s.line,
                        "doc": s.doc,
                        "signature": s.signature,
                    }
                    for s in node.symbols
                ],
            }
            if analysis:
                for c in analysis.communities:
                    if node.node_id in c.file_ids:
                        nd["community"] = c.community_id
                        nd["community_label"] = c.label
                        break
            node_data.append(nd)

        edge_data = [
            {
                "source": e.source,
                "target": e.target,
                "relation": e.relation,
                "confidence": e.confidence,
            }
            for e in all_edges
        ]

        result = {
            "nodes": node_data,
            "edges": edge_data,
            "metadata": {
                "file_count": len(nodes),
                "symbol_count": sum(len(n.symbols) for n in nodes),
                "import_count": len(edges),
                "resolved_import_count": len(resolved_edges or []),
            },
        }

        if analysis:
            result["analysis"] = {
                "god_nodes": [
                    {"node_id": nid, "score": score}
                    for nid, score in analysis.god_nodes
                ],
                "communities": [
                    {
                        "id": c.community_id,
                        "label": c.label,
                        "size": c.size,
                        "cohesion": c.cohesion,
                        "files": sorted(c.file_ids),
                    }
                    for c in analysis.communities
                ],
                "surprising_connections": [
                    {
                        "source": src,
                        "target": tgt,
                        "hops": hops,
                        "communities_crossed": sorted(comms),
                    }
                    for src, tgt, hops, comms in analysis.surprising_connections
                ],
                "suggested_questions": analysis.suggested_questions,
            }

        return json.dumps(result, indent=2, ensure_ascii=False)

    def to_html(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> str:
        """Generate a standalone interactive HTML graph page.

        Uses vis.js loaded from CDN. Supports click-to-inspect nodes,
        search filtering, and community-based coloring.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional analysis results for community coloring.

        Returns:
            Complete HTML document as a string.
        """
        all_edges = edges + (resolved_edges or [])

        vis_nodes: List[Dict] = []
        vis_edges: List[Dict] = []
        node_map = {n.node_id: n for n in nodes}
        seen_ext: set = set()
        community_colors = self._community_color_map(analysis)

        for node in nodes:
            color = community_colors.get(node.node_id)
            bg = color or "#2d2d2d"
            border = self._lighten(bg) if color else "#4ec9b0"
            title_parts = [f"<b>{node.label}</b>", f"Language: {node.language}"]
            if node.symbols:
                sym_list = "<br>".join(
                    f"  {s.name} ({s.kind})" for s in node.symbols[:10]
                )
                title_parts.append(f"<br>Symbols:<br>{sym_list}")
                if len(node.symbols) > 10:
                    title_parts.append(f"  ... +{len(node.symbols) - 10} more")
            if node.doc:
                title_parts.append(f"<br><i>{node.doc[:200]}</i>")

            vis_nodes.append({
                "id": node.node_id,
                "label": node.label,
                "title": "<br>".join(title_parts),
                "color": {"background": bg, "border": border},
                "shape": "box",
                "font": {"color": "#ffffff", "size": 12},
            })

        for edge in all_edges:
            if edge.source in node_map and edge.target in node_map:
                vis_edges.append({
                    "from": edge.source,
                    "to": edge.target,
                    "arrows": "to",
                    "color": {"color": "#88aaff", "opacity": 0.6},
                    "title": f"{edge.relation} ({edge.confidence})",
                })
            else:
                target_id = f"ext_{edge.target}"
                if target_id not in seen_ext:
                    seen_ext.add(target_id)
                    vis_nodes.append({
                        "id": target_id,
                        "label": edge.target.split("/")[-1],
                        "title": f"External: {edge.target}",
                        "color": {"background": "#111111", "border": "#666666"},
                        "shape": "box",
                        "font": {"color": "#aaaaaa", "size": 10},
                    })
                vis_edges.append({
                    "from": edge.source,
                    "to": target_id,
                    "arrows": "to",
                    "color": {"color": "#666666", "opacity": 0.3},
                    "dashes": True,
                    "title": edge.relation,
                })

        return self._render_html(vis_nodes, vis_edges, analysis)

    def _community_color_map(
        self, analysis: Optional[AnalysisResult]
    ) -> Dict[str, str]:
        """Build a node-to-color map based on community membership."""
        colors = [
            "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
            "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        ]
        cmap: Dict[str, str] = {}
        if analysis is None:
            return cmap
        for c in analysis.communities:
            color = colors[c.community_id % len(colors)]
            for fid in c.file_ids:
                cmap[fid] = color
        return cmap

    @staticmethod
    def _lighten(hex_color: str) -> str:
        """Lighten a hex color by 30% for border use."""
        hex_color = hex_color.lstrip("#")
        r = min(255, int(int(hex_color[0:2], 16) * 1.3))
        g = min(255, int(int(hex_color[2:4], 16) * 1.3))
        b = min(255, int(int(hex_color[4:6], 16) * 1.3))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _render_html(
        self,
        vis_nodes: List[Dict],
        vis_edges: List[Dict],
        analysis: Optional[AnalysisResult],
    ) -> str:
        """Render the full HTML document with vis.js."""
        nodes_json = json.dumps(vis_nodes, ensure_ascii=False)
        edges_json = json.dumps(vis_edges, ensure_ascii=False)

        community_legend = ""
        if analysis and analysis.communities:
            legend_items = []
            colors = self._community_color_map(analysis).values()
            color_list = sorted(set(colors))
            for c in analysis.communities:
                color = self._community_color_map(analysis).get(
                    next(iter(c.file_ids), ""), "#666"
                )
                legend_items.append(
                    f'<span style="display:inline-block;width:12px;height:12px;'
                    f'background:{color};margin-right:4px;border-radius:2px;"></span>'
                    f'{c.label} ({c.size} files)'
                )
            if legend_items:
                community_legend = (
                    '<div style="padding:8px;background:#1e1e1e;'
                    'border-bottom:1px solid #333;font-size:12px;color:#aaa;">'
                    + " &nbsp;|&nbsp; ".join(legend_items)
                    + "</div>"
                )

        god_section = ""
        if analysis and analysis.god_nodes:
            god_items = [
                f"<li>{nid} (score: {score:.1f})</li>"
                for nid, score in analysis.god_nodes[:5]
            ]
            god_section = (
                "<details><summary style='cursor:pointer;color:#4ec9b0;'>"
                "God Nodes (most central)</summary>"
                f"<ul>{''.join(god_items)}</ul></details>"
            )

        question_section = ""
        if analysis and analysis.suggested_questions:
            q_items = [f"<li>{q}</li>" for q in analysis.suggested_questions]
            question_section = (
                "<details><summary style='cursor:pointer;color:#dcdcaa;'>"
                "Suggested Questions</summary>"
                f"<ul>{''.join(q_items)}</ul></details>"
            )

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ReadMenator - Knowledge Graph</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet">
<style>
    body {{ margin:0; font-family:'Segoe UI',sans-serif; background:#0d0d0d; color:#ccc; }}
    #header {{ padding:12px 16px; background:#1a1a1a; border-bottom:2px solid #ff6666; display:flex; align-items:center; gap:12px; flex-wrap:wrap; }}
    #header h1 {{ margin:0; font-size:18px; color:#ff6666; }}
    #search {{ padding:6px 12px; background:#2d2d2d; border:1px solid #444; color:#fff; border-radius:4px; min-width:200px; }}
    #stats {{ font-size:12px; color:#888; margin-left:auto; }}
    #mynetwork {{ width:100vw; height:calc(100vh - 56px); }}
    .vis-network:focus {{ outline:none; }}
</style>
</head>
<body>
<div id="header">
    <h1>ReadMenator</h1>
    <input id="search" type="text" placeholder="Search nodes..." oninput="filterNodes()">
    <span id="stats">Nodes: {len(vis_nodes)} | Edges: {len(vis_edges)}</span>
</div>
{community_legend}
{god_section}
{question_section}
<div id="mynetwork"></div>
<script>
var nodes = new vis.DataSet({json.dumps(vis_nodes, ensure_ascii=False)});
var edges = new vis.DataSet({json.dumps(vis_edges, ensure_ascii=False)});
var container = document.getElementById('mynetwork');
var data = {{ nodes: nodes, edges: edges }};
var options = {{
    physics: {{ solver:'forceAtlas2Based', forceAtlas2Based:{{ gravitationalConstant:-50, centralGravity:0.01 }} }},
    interaction: {{ hover:true, tooltipDelay:100 }},
    nodes: {{ borderWidth:2 }},
    edges: {{ smooth:{{ type:'cubicBezier', forceDirection:'vertical' }} }}
}};
var network = new vis.Network(container, data, options);

function filterNodes() {{
    var term = document.getElementById('search').value.toLowerCase();
    nodes.forEach(function(n) {{
        var match = !term || n.label.toLowerCase().includes(term) || (n.title && n.title.toLowerCase().includes(term));
        nodes.update({{ id:n.id, hidden:!match }});
    }});
    if (!term) {{
        edges.forEach(function(e) {{ edges.update({{ id:e.id, hidden:false }}); }});
    }} else {{
        var visibleIds = new Set();
        nodes.forEach(function(n) {{ if (!n.hidden) visibleIds.add(n.id); }});
        edges.forEach(function(e) {{
            edges.update({{ id:e.id, hidden:!(visibleIds.has(e.from) && visibleIds.has(e.to)) }});
        }});
    }}
}}

network.on("click", function(params) {{
    if (params.nodes.length > 0) {{
        var node = nodes.get(params.nodes[0]);
        alert(node.title || node.label);
    }}
}});
</script>
</body>
</html>"""

    def to_svg(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> str:
        """Generate a static SVG representation of the graph.

        Uses a simple force-directed layout without external dependencies.
        For graphs with more than SVG_MAX_NODES, returns a plain SVG
        with a truncation message.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional analysis results for community coloring.

        Returns:
            SVG document as a string.
        """
        max_nodes = self._config.SVG_MAX_NODES
        all_edges = edges + (resolved_edges or [])

        if len(nodes) > max_nodes:
            return self._render_truncated_svg(len(nodes))

        node_map = {n.node_id: n for n in nodes}
        positions = self._layout_spring(nodes, all_edges, node_map)
        community_colors = self._community_color_map(analysis)

        width = 1600
        height = 1200
        margin = 60
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="background:#0d0d0d;">',
            '<defs><style>',
            '.node-rect { fill:#2d2d2d; stroke:#4ec9b0; stroke-width:2; rx:4; }',
            '.node-text { fill:#ffffff; font-size:11px; font-family:monospace; }',
            '.edge-line { stroke:#88aaff; stroke-width:1; opacity:0.5; }',
            '.edge-ext { stroke:#666; stroke-width:0.5; stroke-dasharray:4,4; opacity:0.3; }',
            '.label-bg { fill:#1a1a1a; opacity:0.85; }',
            '.title-text { fill:#ff6666; font-size:18px; font-family:sans-serif; }',
            '.stat-text { fill:#888; font-size:12px; font-family:monospace; }',
            '</style></defs>',
            f'<text x="{margin}" y="30" class="title-text">ReadMenator Knowledge Graph</text>',
            f'<text x="{margin}" y="50" class="stat-text">{len(nodes)} files | {len(all_edges)} imports | {len(positions)} nodes</text>',
        ]

        all_x = [p[0] for p in positions.values()]
        all_y = [p[1] for p in positions.values()]
        if not all_x:
            return "\n".join(svg_parts) + "\n</svg>"
        x_min, x_max = min(all_x), max(all_x)
        y_min, y_max = min(all_y), max(all_y)
        x_range = x_max - x_min or 1
        y_range = y_max - y_min or 1
        scale_x = (width - 2 * margin) / x_range
        scale_y = (height - 2 * margin) / y_range
        scale = min(scale_x, scale_y)

        def _project(pos):
            x = margin + (pos[0] - x_min) * scale
            y = margin + (pos[1] - y_min) * scale
            return (x, y)

        seen_ext: set = set()
        for edge in all_edges:
            if edge.source in positions and edge.target in positions:
                src_pos = _project(positions[edge.source])
                tgt_pos = _project(positions[edge.target])
                svg_parts.append(
                    f'<line x1="{src_pos[0]:.1f}" y1="{src_pos[1]:.1f}" '
                    f'x2="{tgt_pos[0]:.1f}" y2="{tgt_pos[1]:.1f}" class="edge-line"/>'
                )
            elif edge.source in positions:
                src_pos = _project(positions[edge.source])
                ext_id = f"ext_{edge.target}"
                if ext_id not in seen_ext:
                    seen_ext.add(ext_id)
                    ext_x = src_pos[0] + 80
                    ext_y = src_pos[1] + 40
                    svg_parts.append(
                        f'<rect x="{ext_x - 40:.1f}" y="{ext_y - 12:.1f}" '
                        f'width="80" height="20" fill="#111" stroke="#666" rx="3"/>'
                    )
                    svg_parts.append(
                        f'<text x="{ext_x:.1f}" y="{ext_y + 4:.1f}" '
                        f'text-anchor="middle" fill="#aaa" font-size="9px" font-family="monospace">'
                        f'{edge.target[:20]}</text>'
                    )
                svg_parts.append(
                    f'<line x1="{src_pos[0]:.1f}" y1="{src_pos[1]:.1f}" '
                    f'x2="{src_pos[0] + 80:.1f}" y2="{src_pos[1] + 40:.1f}" class="edge-ext"/>'
                )

        for nid, pos in positions.items():
            node = node_map.get(nid)
            if node is None:
                continue
            proj = _project(pos)
            color = community_colors.get(nid, None)
            fill = color if color else "#2d2d2d"
            stroke = self._lighten(fill) if color else "#4ec9b0"
            label_text = node.label[:25]
            svg_parts.append(
                f'<rect x="{proj[0] - 50:.1f}" y="{proj[1] - 14:.1f}" '
                f'width="100" height="28" fill="{fill}" stroke="{stroke}" stroke-width="2" rx="4"/>'
            )
            svg_parts.append(
                f'<text x="{proj[0]:.1f}" y="{proj[1] + 4:.1f}" '
                f'text-anchor="middle" class="node-text">{label_text}</text>'
            )

        svg_parts.append("</svg>")
        return "\n".join(svg_parts)

    def _render_truncated_svg(self, total_nodes: int) -> str:
        """Render a minimal SVG with a truncation notice."""
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" style="background:#0d0d0d;">
    <text x="400" y="80" text-anchor="middle" fill="#ff6666" font-size="20" font-family="sans-serif">
        Graph Too Large for SVG Rendering
    </text>
    <text x="400" y="120" text-anchor="middle" fill="#aaa" font-size="14" font-family="monospace">
        {total_nodes} nodes exceed the SVG limit of {self._config.SVG_MAX_NODES}.
    </text>
    <text x="400" y="150" text-anchor="middle" fill="#888" font-size="12" font-family="monospace">
        Use HTML export (--html) for interactive visualization of large graphs.
    </text>
</svg>"""

    def _layout_spring(
        self,
        nodes: List[Node],
        edges: List[Edge],
        node_map: Dict[str, Node],
    ) -> Dict[str, Tuple[float, float]]:
        """Compute a simple spring-layout for node positioning.

        Implements a basic force-directed layout with repulsion
        between all nodes and attraction along edges. Runs a fixed
        number of iterations for determinism.
        """
        import math

        positions: Dict[str, List[float]] = {}
        file_ids = [n.node_id for n in nodes]
        for i, fid in enumerate(file_ids):
            angle = (i / len(file_ids)) * 2 * math.pi
            r = 200 + (i % 5) * 20
            positions[fid] = [math.cos(angle) * r, math.sin(angle) * r]

        adj: Dict[str, Set[str]] = {}
        for edge in edges:
            if edge.source in node_map and edge.target in node_map:
                adj.setdefault(edge.source, set()).add(edge.target)
                adj.setdefault(edge.target, set()).add(edge.source)

        iterations = 60
        k = 150.0
        damping = 0.85
        min_delta = 0.01

        for _iter in range(iterations):
            displacements: Dict[str, List[float]] = {fid: [0.0, 0.0] for fid in file_ids}

            for i, fid_a in enumerate(file_ids):
                for fid_b in file_ids[i + 1 :]:
                    dx = positions[fid_a][0] - positions[fid_b][0]
                    dy = positions[fid_a][1] - positions[fid_b][1]
                    dist_sq = dx * dx + dy * dy
                    if dist_sq < 1.0:
                        dist_sq = 1.0
                    dist = math.sqrt(dist_sq)
                    force = k * k / dist
                    fx = (dx / dist) * force
                    fy = (dy / dist) * force
                    displacements[fid_a][0] += fx
                    displacements[fid_a][1] += fy
                    displacements[fid_b][0] -= fx
                    displacements[fid_b][1] -= fy

            for src, targets in adj.items():
                if src not in positions:
                    continue
                for tgt in targets:
                    if tgt not in positions:
                        continue
                    dx = positions[tgt][0] - positions[src][0]
                    dy = positions[tgt][1] - positions[src][1]
                    dist = math.sqrt(dx * dx + dy * dy)
                    if dist < 1.0:
                        dist = 1.0
                    force = (dist * dist) / k
                    fx = (dx / dist) * force
                    fy = (dy / dist) * force
                    displacements[src][0] += fx
                    displacements[src][1] += fy
                    displacements[tgt][0] -= fx
                    displacements[tgt][1] -= fy

            max_disp = 0.0
            for fid in file_ids:
                dx = displacements[fid][0] * damping
                dy = displacements[fid][1] * damping
                positions[fid][0] += dx
                positions[fid][1] += dy
                max_disp = max(max_disp, abs(dx), abs(dy))

            if max_disp < min_delta:
                break

        return {fid: (p[0], p[1]) for fid, p in positions.items()}
