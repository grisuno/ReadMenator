"""Edge bundle explorer: circle and sphere hierarchical edge bundling pages.

Turns the force-graph payload (file nodes with community, layer,
language, PageRank, purpose; file-to-file dependency edges) into a
compact bundle payload. Leaf positions come from _graphlayout: a circle
grouped by community for the 2D view (hierarchical_edge_bundling) and a
sphere of community caps for the 3D view (spherical_edge_bundling). The
page in _bundlegraph_page.py routes every edge through the community
hubs itself, so the bundling strength stays adjustable in the browser.
The page is self-contained: no CDN, no fonts, no network.
"""

from __future__ import annotations

import html
import json
import math
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from readmenator._bundlegraph_page import BUNDLEGRAPH_PAGE_TEMPLATE
from readmenator._config import Config
from readmenator._forcegraph import ForceGraphRenderer
from readmenator._graphlayout import hierarchical_edge_bundling, spherical_edge_bundling

_PLACEHOLDER = re.compile(r"__(TITLE|HOME|EXPLORER|DATA|SETTINGS)__")

BUNDLE_RELATIONS = ("resolved_imports", "imports", "calls", "inherits")

UNASSIGNED_KEY = "unassigned"

COORD_DIGITS = 5


def _json_script(value: object) -> str:
    """Serialize a value for an inline script, escaping angle brackets.

    Args:
        value: JSON-serializable value.

    Returns:
        JSON text safe inside a script element.
    """
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")


class BundleGraphRenderer:
    """Builds the bundle payload and renders the edge bundle explorer page."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for bundling, camera, labels, and palettes.
        """
        self._config = config
        self._force = ForceGraphRenderer(config)

    def build_payload(self, force_payload: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Derive the bundle payload from a force-graph payload.

        Communities keep the analyzer order (largest first) and files
        without a community form a trailing unassigned group. Inside a
        group files are ordered by PageRank, so hubs sit at the center
        of their arc and cap. Edges are distinct directed file pairs.

        Args:
            force_payload: Payload from ForceGraphRenderer.build_payload.

        Returns:
            Dictionary with nodes, groups, and edges for the page.
        """
        cfg = self._config
        files = sorted(
            (n for n in force_payload.get("nodes", []) if n.get("type") == "file"),
            key=lambda n: str(n.get("id", "")),
        )
        if not files:
            return {"nodes": [], "groups": [], "edges": []}
        group_label: Dict[str, str] = {}
        group_order: List[Tuple[int, str]] = []
        member_key: Dict[str, str] = {}
        for node in files:
            cid = node.get("community")
            key = f"community:{cid}" if cid is not None else UNASSIGNED_KEY
            member_key[node["id"]] = key
            if key not in group_label:
                group_label[key] = str(node.get("community_label") or "") if cid is not None else UNASSIGNED_KEY
                group_order.append((int(cid) if cid is not None else math.inf, key))
        keys = [key for _order, key in sorted(group_order)]
        members: Dict[str, List[str]] = {key: [] for key in keys}
        for node in sorted(files, key=lambda n: (-float(n.get("rank", 0.0)), str(n["id"]))):
            members[member_key[node["id"]]].append(node["id"])
        circle = hierarchical_edge_bundling(
            members, [], (0.0, 0.0), 1.0, group_gap=cfg.BUNDLEGRAPH_GROUP_GAP,
            inner_ratio=cfg.BUNDLEGRAPH_INNER_RATIO,
        )
        sphere = spherical_edge_bundling(members, [], 1.0, inner_ratio=cfg.BUNDLEGRAPH_INNER_RATIO)
        group_index = {key: i for i, key in enumerate(keys)}
        caps = {label: center for label, center, _count in sphere.groups}
        fallback = self._force.node_palette().get("file", "#4f8ef7")
        groups: List[Dict[str, Any]] = []
        for label, start, end, count in circle.groups:
            mid = (start + end) / 2
            ratio = cfg.BUNDLEGRAPH_INNER_RATIO
            name = group_label[label]
            groups.append({
                "k": label,
                "l": name,
                "c": fallback if label == UNASSIGNED_KEY else self._force.family_color(name),
                "n": count,
                "a0": round(start, COORD_DIGITS),
                "a1": round(end, COORD_DIGITS),
                "h2": [round(ratio * math.cos(mid), COORD_DIGITS), round(ratio * math.sin(mid), COORD_DIGITS)],
                "h3": [round(v, COORD_DIGITS) for v in sphere.hubs[label]],
                "u": [round(v, COORD_DIGITS) for v in caps[label]],
            })
        index = {node["id"]: i for i, node in enumerate(files)}
        nodes: List[Dict[str, Any]] = []
        for node in files:
            nid = node["id"]
            nodes.append({
                "id": nid,
                "f": str(node.get("file") or node.get("label") or nid),
                "l": str(node.get("label") or nid),
                "g": group_index[member_key[nid]],
                "c": str(node.get("color") or fallback),
                "ly": str(node.get("layer") or "unknown"),
                "lg": str(node.get("language") or "unknown"),
                "r": float(node.get("rank", 0.0)),
                "rp": int(node.get("rank_pos", 0)),
                "fd": int(node.get("findings", 0)),
                "d": str(node.get("doc") or ""),
                "a": round(circle.angles[nid], COORD_DIGITS),
                "p": [round(v, COORD_DIGITS) for v in sphere.leaves[nid]],
            })
        pairs = sorted({
            (index[e["source"]], index[e["target"]])
            for e in force_payload.get("edges", [])
            if e.get("type") in BUNDLE_RELATIONS
            and e.get("source") in index and e.get("target") in index
            and e["source"] != e["target"]
        })
        return {"nodes": nodes, "groups": groups, "edges": [list(p) for p in pairs]}

    def page_settings(self, force_payload: Dict[str, List[Dict[str, Any]]], explorer_href: Optional[str]) -> Dict[str, Any]:
        """Collect the page settings serialized into the HTML.

        Args:
            force_payload: Force-graph payload (for layer and language colors).
            explorer_href: Relative link to the force-graph explorer, or None.

        Returns:
            JSON-serializable settings for bundling, camera, labels, and palettes.
        """
        cfg = self._config
        return {
            "mode": cfg.BUNDLEGRAPH_MODE,
            "beta": cfg.BUNDLEGRAPH_BETA,
            "samples": cfg.BUNDLEGRAPH_SAMPLES,
            "edgeAlpha": cfg.BUNDLEGRAPH_EDGE_ALPHA,
            "dimAlpha": cfg.BUNDLEGRAPH_DIM_ALPHA,
            "labelAllMax": cfg.BUNDLEGRAPH_LABEL_ALL_MAX,
            "labelTopN": cfg.BUNDLEGRAPH_LABEL_TOP_N,
            "labelMax": cfg.BUNDLEGRAPH_LABEL_MAX_CHARS,
            "nodeMin": cfg.BUNDLEGRAPH_NODE_MIN_PX,
            "nodeMax": cfg.BUNDLEGRAPH_NODE_MAX_PX,
            "hitPx": cfg.BUNDLEGRAPH_HIT_PX,
            "rotateSpeed": cfg.BUNDLEGRAPH_ROTATE_SPEED,
            "perspective": cfg.BUNDLEGRAPH_PERSPECTIVE,
            "depthFade": cfg.BUNDLEGRAPH_DEPTH_FADE,
            "particles": cfg.BUNDLEGRAPH_PARTICLES,
            "revealMs": cfg.BUNDLEGRAPH_REVEAL_MS,
            "flowTopN": cfg.BUNDLEGRAPH_FLOW_TOP_N,
            "listMax": cfg.BUNDLEGRAPH_LIST_MAX,
            "searchResults": cfg.FORCEGRAPH_SEARCH_RESULTS,
            "tipDocChars": cfg.FORCEGRAPH_TIP_DOC_CHARS,
            "dragPx": cfg.FORCEGRAPH_DRAG_THRESHOLD_PX,
            "flyMs": cfg.FORCEGRAPH_FLY_MS,
            "explorerHref": explorer_href or "",
            "unassignedKey": UNASSIGNED_KEY,
            "groupColors": self._force.group_colors(force_payload),
        }

    def render(
        self,
        force_payload: Dict[str, List[Dict[str, Any]]],
        title: str = "Edge Bundles",
        home_href: Optional[str] = "index.html",
        explorer_href: Optional[str] = None,
    ) -> str:
        """Render the standalone edge bundle explorer HTML document.

        Args:
            force_payload: Payload from ForceGraphRenderer.build_payload.
            title: Document title shown in the header.
            home_href: Optional gallery home link; omitted when None.
            explorer_href: Optional link to the force-graph explorer page.

        Returns:
            Complete HTML document as a string.
        """
        home = ""
        if home_href:
            home = '<a class="home" href="' + html.escape(home_href, quote=True) + '">← Maps gallery</a>'
        explorer = ""
        if explorer_href:
            explorer = (
                '<a class="home" href="' + html.escape(explorer_href, quote=True)
                + '" title="Open the force-graph explorer (2D and 3D)">Force graph →</a>'
            )
        values = {
            "TITLE": html.escape(title, quote=True),
            "HOME": home,
            "EXPLORER": explorer,
            "DATA": _json_script(self.build_payload(force_payload)),
            "SETTINGS": _json_script(self.page_settings(force_payload, explorer_href)),
        }
        return _PLACEHOLDER.sub(lambda match: values[match.group(1)], BUNDLEGRAPH_PAGE_TEMPLATE)

    def write(
        self,
        output_path: str | Path,
        force_payload: Dict[str, List[Dict[str, Any]]],
        title: str = "Edge Bundles",
        home_href: Optional[str] = "index.html",
        explorer_href: Optional[str] = None,
    ) -> str:
        """Write the edge bundle explorer HTML document.

        Args:
            output_path: Destination HTML file path.
            force_payload: Payload from ForceGraphRenderer.build_payload.
            title: Document title shown in the header.
            home_href: Gallery home link relative to the page; None omits it.
            explorer_href: Force-graph explorer link relative to the page.

        Returns:
            Rendered HTML content that was written.
        """
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        content = self.render(force_payload, title=title, home_href=home_href, explorer_href=explorer_href)
        target.write_text(content, encoding="utf-8")
        return content

    def thumbnail_svg(self, force_payload: Dict[str, List[Dict[str, Any]]]) -> str:
        """Render a small circular bundle preview as inline SVG.

        The busiest edges (by endpoint PageRank) are drawn as bundled
        B-splines in their source color; only numbers and escaped colors
        reach the markup.

        Args:
            force_payload: Payload from ForceGraphRenderer.build_payload.

        Returns:
            SVG markup, or an empty string when there are no files.
        """
        cfg = self._config
        payload = self.build_payload(force_payload)
        nodes = payload["nodes"]
        if not nodes:
            return ""
        w, h = cfg.FORCEGRAPH_THUMB_WIDTH, cfg.FORCEGRAPH_THUMB_HEIGHT
        members: Dict[str, List[str]] = {str(g): [] for g in range(len(payload["groups"]))}
        for node in sorted(nodes, key=lambda n: (-n["r"], n["id"])):
            members[str(node["g"])].append(node["id"])
        ranked = sorted(
            payload["edges"],
            key=lambda e: (-(nodes[e[0]]["r"] + nodes[e[1]]["r"]), e[0], e[1]),
        )[: cfg.BUNDLEGRAPH_THUMB_EDGES]
        radius = min(w, h) / 2 - 8
        layout = hierarchical_edge_bundling(
            members, [(nodes[a]["id"], nodes[b]["id"]) for a, b in ranked],
            (w / 2, h / 2), radius, beta=cfg.BUNDLEGRAPH_BETA, samples=cfg.BUNDLEGRAPH_THUMB_SAMPLES,
            group_gap=cfg.BUNDLEGRAPH_GROUP_GAP, inner_ratio=cfg.BUNDLEGRAPH_INNER_RATIO,
        )
        by_id = {node["id"]: node for node in nodes}
        parts = [f'<svg class="thumb" viewBox="0 0 {w} {h}" aria-hidden="true" focusable="false">']
        for source, _target, points in layout.curves:
            color = html.escape(str(by_id[source]["c"]), quote=True)
            path = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
            parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-opacity="0.35" stroke-width="0.7"/>')
        for group in payload["groups"]:
            a0, a1 = float(group["a0"]), float(group["a1"])
            r = radius + 3
            large = 1 if a1 - a0 > math.pi else 0
            x0, y0 = w / 2 + r * math.cos(a0), h / 2 + r * math.sin(a0)
            x1, y1 = w / 2 + r * math.cos(a1), h / 2 + r * math.sin(a1)
            color = html.escape(str(group["c"]), quote=True)
            parts.append(
                f'<path d="M{x0:.1f} {y0:.1f} A{r:.1f} {r:.1f} 0 {large} 1 {x1:.1f} {y1:.1f}" '
                f'fill="none" stroke="{color}" stroke-width="2.5"/>'
            )
        for nid, (x, y) in layout.leaves.items():
            color = html.escape(str(by_id[nid]["c"]), quote=True)
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.3" fill="{color}"/>')
        parts.append("</svg>")
        return "".join(parts)
