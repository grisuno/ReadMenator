"""Force-graph explorer for the readmenator knowledge graph.

Builds a heterogeneous node-link payload (files, communities, layers,
externals) and renders a standalone HTML document on top of the
vasturiano force-graph library. The 2D engine ships vendored beside
the page so it works offline and via file://; the CDN copy is only a
fallback and the 3D engine loads on demand. The page itself lives in
_forcegraph_page.py; this module builds its payload and settings.
Visual language (theme tokens, cards, chips, toolbar) matches the
system-maps gallery.
"""

from __future__ import annotations

import html
import json
import math
import re
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._forcegraph_page import FORCEGRAPH_PAGE_TEMPLATE
from readmenator._graphlayout import ForceAtlas2Settings, fit_frames, forceatlas2_frames
from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding
from readmenator._purpose import file_purpose, first_sentence, truncate_words
from readmenator._rank import file_pagerank
from readmenator._resolver import ImportResolver

_PLACEHOLDER = re.compile(r"__(TITLE|HOME|VENDOR_SRC|CDN_2D|CDN_3D|DATA|ANALYTICS|SETTINGS)__")


def family_color_from_name(
    name: str,
    sat_base: int = 55,
    sat_span: int = 12,
    light_base: int = 58,
    light_span: int = 10,
) -> str:
    """Derive a stable, visually-distinct HSL color from a label.

    Args:
        name: Community or layer label to hash.
        sat_base: Minimum saturation percent.
        sat_span: Saturation variation range.
        light_base: Minimum lightness percent.
        light_span: Lightness variation range.

    Returns:
        CSS hsl() color string stable across runs.
    """
    hashed = 5381
    for char in name:
        hashed = ((hashed << 5) + hashed + ord(char)) & 0xFFFFFFFF
    hue = hashed % 360
    sat = sat_base + ((hashed >> 8) % max(1, sat_span))
    light = light_base + ((hashed >> 16) % max(1, light_span))
    return f"hsl({hue}, {sat}%, {light}%)"


def node_value(symbols: int, degree: int) -> float:
    """Scale a node value with log2 dampening.

    Args:
        symbols: Symbol count for the file.
        degree: Connection degree for the file.

    Returns:
        Dampened node size value with a minimum of 1.
    """
    return max(1.0, math.log2(float(symbols + degree) + 1.0))


class ForceGraphRenderer:
    """Builds force-graph payloads and renders the explorer HTML."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for palette, physics, hulls, and CDN URLs.
        """
        self._config = config

    def node_palette(self) -> Dict[str, str]:
        """Return the node-type color palette from configuration."""
        return dict(self._config.FORCEGRAPH_NODE_COLORS)

    def edge_palette(self) -> Dict[str, str]:
        """Return the edge-relation color palette from configuration."""
        return dict(self._config.FORCEGRAPH_EDGE_COLORS)

    def vendor_source(self) -> Path:
        """Return the path of the vendored 2D engine shipped in the package."""
        return (
            Path(__file__).resolve().parent
            / "_vendor"
            / self._config.FORCEGRAPH_VENDOR_JS_2D
        )

    def vendor_href(self) -> str:
        """Return the relative vendor script href used beside the page."""
        subdir = self._config.FORCEGRAPH_VENDOR_SUBDIR.strip().strip("/")
        return f"./{subdir}/{self._config.FORCEGRAPH_VENDOR_JS_2D}"

    def build_payload(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[List[SecurityFinding]] = None,
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Build a heterogeneous graph payload for the explorer.

        Args:
            nodes: Scanned file nodes.
            edges: Raw import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional community and god-node analysis.
            layers: Optional file-to-layer mapping.
            findings: Optional security findings for node weights.

        Returns:
            Dictionary with nodes and edges lists for the frontend.
        """
        palette = self.node_palette()
        edge_palette = self.edge_palette()
        community_of: Dict[str, Tuple[int, str]] = {}
        if analysis:
            for community in analysis.communities:
                for file_id in community.file_ids:
                    community_of[file_id] = (community.community_id, community.label)
        finding_counts: Dict[str, int] = {}
        for finding in findings or []:
            finding_counts[finding.file_path] = finding_counts.get(finding.file_path, 0) + 1
        node_ids = {node.node_id for node in nodes}

        def file_of(edge_id: str) -> Optional[str]:
            """Map a symbol-scoped edge endpoint to its file identifier."""
            if edge_id in node_ids:
                return edge_id
            base = edge_id.split("::", 1)[0]
            if base in node_ids:
                return base
            return None

        resolver = ImportResolver(sorted(node_ids))
        degree: Dict[str, int] = {}
        normalized: List[Edge] = []
        for edge in list(edges) + list(resolved_edges or []):
            source_file = file_of(edge.source)
            if source_file is None:
                continue
            target_file = file_of(edge.target)
            if target_file is None:
                if edge.relation != "imports" or resolver.resolve(edge.target, source_file) is not None:
                    continue
                normalized.append(
                    Edge(
                        source=source_file,
                        target=edge.target,
                        relation=edge.relation,
                        confidence=edge.confidence,
                    )
                )
                degree[source_file] = degree.get(source_file, 0) + 1
                continue
            if source_file == target_file and edge.relation == "calls":
                continue
            normalized.append(
                Edge(
                    source=source_file,
                    target=target_file,
                    relation=edge.relation,
                    confidence=edge.confidence,
                )
            )
            degree[source_file] = degree.get(source_file, 0) + 1
            degree[target_file] = degree.get(target_file, 0) + 1
        out_nodes: Dict[str, Dict[str, Any]] = {}
        out_edges: List[Dict[str, Any]] = []
        rank = file_pagerank(
            sorted(node_ids),
            [(e.source, e.target) for e in normalized if e.target in node_ids],
            self._config.RANKING_ALPHA, self._config.RANKING_MAX_ITER, self._config.RANKING_TOLERANCE,
        )
        ordered_rank = sorted(rank.values(), reverse=True)
        community_sizes: Dict[int, int] = {}
        for cid, _label in community_of.values():
            community_sizes[cid] = community_sizes.get(cid, 0) + 1

        def add_node(node_id: str, label: str, node_type: str, **attrs: Any) -> None:
            """Insert a node unless already present."""
            out_nodes.setdefault(node_id, {"id": node_id, "label": label, "type": node_type, **attrs})

        for node in nodes:
            community = community_of.get(node.node_id)
            layer = (layers or {}).get(node.node_id, "unknown")
            family = community[1] if community else layer
            color = self._file_color(node.node_id, family, layer, palette)
            add_node(
                f"file:{node.node_id}",
                node.label,
                "file",
                file=node.node_id,
                language=node.language,
                symbols=len(node.symbols),
                degree=degree.get(node.node_id, 0),
                findings=sum(
                    1 for key in finding_counts
                    if node.node_id.endswith(key) or key.endswith(node.node_id)
                ),
                community=community[0] if community else None,
                community_label=community[1] if community else "",
                family=family,
                layer=layer,
                color=color,
                rank=round(rank.get(node.node_id, 0.0), 6),
                rank_pos=(ordered_rank.index(rank[node.node_id]) + 1) if node.node_id in rank else 0,
                doc=self._node_doc(node),
                symbol_list=self._symbol_list(node),
            )
            if community:
                cid, label = community
                add_node(
                    f"community:{cid}",
                    label,
                    "community",
                    community_id=cid,
                    size=community_sizes.get(cid, 0),
                    color=palette.get("community", "#7c5aef"),
                )
                out_edges.append(
                    {
                        "source": f"file:{node.node_id}",
                        "target": f"community:{cid}",
                        "type": "member_of",
                        "weight": 1,
                        "color": edge_palette.get("member_of", edge_palette.get("external", "rgba(255,255,255,.15)")),
                    }
                )
            add_node(
                f"layer:{layer}",
                layer,
                "layer",
                color=palette.get("layer", "#4fef8e"),
            )
            out_edges.append(
                {
                    "source": f"file:{node.node_id}",
                    "target": f"layer:{layer}",
                    "type": "layered_as",
                    "weight": 1,
                    "color": edge_palette.get("layered_as", edge_palette.get("external", "rgba(255,255,255,.15)")),
                }
            )
        for edge in normalized:
            source = f"file:{edge.source}"
            if edge.target in node_ids:
                target = f"file:{edge.target}"
            else:
                target = f"ext:{edge.target}"
                add_node(
                    target,
                    edge.target.split("/")[-1],
                    "external",
                    color=palette.get("external", "#efb84f"),
                )
            out_edges.append(
                {
                    "source": source,
                    "target": target,
                    "type": edge.relation,
                    "weight": 1,
                    "color": edge_palette.get(edge.relation, edge_palette.get("external", "rgba(255,255,255,.15)")),
                }
            )
        return {"nodes": list(out_nodes.values()), "edges": out_edges}

    def render(
        self,
        payload: Dict[str, List[Dict[str, Any]]],
        analytics: Optional[Dict[str, Any]] = None,
        title: str = "Force Graph",
        home_href: Optional[str] = "index.html",
    ) -> str:
        """Render the standalone force-graph explorer HTML document.

        Args:
            payload: Heterogeneous graph payload from build_payload.
            analytics: Optional analytics payload for the side panel.
            title: Document title shown in the header.
            home_href: Optional gallery home link; omitted when None.

        Returns:
            Complete HTML document as a string.
        """
        data_json = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
        analytics_json = json.dumps(analytics or {}, ensure_ascii=False).replace("<", "\\u003c")
        safe_title = html.escape(title, quote=True)
        safe_vendor = html.escape(self.vendor_href(), quote=True)
        safe_cdn_2d = html.escape(self._config.FORCEGRAPH_CDN_JS_2D, quote=True)
        safe_cdn_3d = html.escape(self._config.FORCEGRAPH_CDN_JS_3D, quote=True)
        home_link = ""
        if home_href:
            home_link = (
                '<a class="home" href="'
                + html.escape(home_href, quote=True)
                + '">\u2190 Maps gallery</a>'
            )
        values = {
            "TITLE": safe_title,
            "HOME": home_link,
            "VENDOR_SRC": safe_vendor,
            "CDN_2D": safe_cdn_2d,
            "CDN_3D": safe_cdn_3d,
            "DATA": data_json,
            "ANALYTICS": analytics_json,
            "SETTINGS": json.dumps(self.page_settings(payload)).replace("<", "\\u003c"),
        }
        return _PLACEHOLDER.sub(lambda match: values[match.group(1)], FORCEGRAPH_PAGE_TEMPLATE)

    def group_colors(self, payload: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Dict[str, str]]:
        """Return stable colors for the layer and language groupings in a payload.

        Args:
            payload: Heterogeneous graph payload from build_payload.

        Returns:
            Mapping of grouping mode to {group key: CSS color}.
        """
        layer_palette = dict(self._config.FORCEGRAPH_LAYER_COLORS)
        layers: Dict[str, str] = {}
        languages: Dict[str, str] = {}
        for node in payload.get("nodes", []):
            if node.get("type") != "file":
                continue
            layer = str(node.get("layer") or "unknown")
            language = str(node.get("language") or "unknown")
            if layer not in layers:
                layers[layer] = layer_palette.get(layer) or self._family_color(layer)
            if language not in languages:
                languages[language] = self._family_color(language)
        return {"layer": layers, "language": languages}

    def page_settings(self, payload: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Collect the explorer page settings serialized into the HTML.

        Args:
            payload: Heterogeneous graph payload from build_payload.

        Returns:
            JSON-serializable settings for physics, hit-testing, 3D view, and palettes.
        """
        cfg = self._config
        return {
            "charge": cfg.FORCEGRAPH_CHARGE,
            "linkDistance": cfg.FORCEGRAPH_LINK_DISTANCE,
            "linkStrength": cfg.FORCEGRAPH_LINK_STRENGTH,
            "nodeRelSize": cfg.FORCEGRAPH_NODE_REL_SIZE,
            "hulls": cfg.FORCEGRAPH_HULLS_ENABLED,
            "hullFill": cfg.FORCEGRAPH_HULL_FILL_ALPHA,
            "hullStroke": cfg.FORCEGRAPH_HULL_STROKE_ALPHA,
            "hullPad": cfg.FORCEGRAPH_HULL_PAD,
            "particles": cfg.FORCEGRAPH_PARTICLES_ON_HIGHLIGHT,
            "dimNode": cfg.FORCEGRAPH_DIM_NODE,
            "dimLink": cfg.FORCEGRAPH_DIM_LINK,
            "mode": cfg.FORCEGRAPH_MODE,
            "labelTopN": cfg.FORCEGRAPH_LABEL_TOP_N,
            "labelZoom": cfg.FORCEGRAPH_LABEL_ZOOM,
            "labelMax": cfg.FORCEGRAPH_LABEL_MAX_CHARS,
            "labelHighlightMax": cfg.FORCEGRAPH_LABEL_HIGHLIGHT_MAX,
            "clusterStrength": cfg.FORCEGRAPH_CLUSTER_STRENGTH,
            "collidePad": cfg.FORCEGRAPH_COLLIDE_PADDING,
            "collideMaxNodes": cfg.FORCEGRAPH_COLLIDE_MAX_NODES,
            "dagLevel": cfg.FORCEGRAPH_DAG_LEVEL_DISTANCE,
            "flyMs": cfg.FORCEGRAPH_FLY_MS,
            "flyZoom": cfg.FORCEGRAPH_FLY_ZOOM,
            "searchResults": cfg.FORCEGRAPH_SEARCH_RESULTS,
            "symbolTotal": cfg.FORCEGRAPH_SYMBOLS_PER_NODE,
            "hitPad": cfg.FORCEGRAPH_HIT_PADDING_PX,
            "minHitPx": cfg.FORCEGRAPH_MIN_HIT_PX,
            "edgeHitPx": cfg.FORCEGRAPH_EDGE_HIT_PX,
            "dragPx": cfg.FORCEGRAPH_DRAG_THRESHOLD_PX,
            "curveStep": cfg.FORCEGRAPH_CURVE_STEP,
            "curveSamples": cfg.FORCEGRAPH_CURVE_SAMPLES,
            "arrowLen": cfg.FORCEGRAPH_ARROW_LENGTH,
            "arrowZoom": cfg.FORCEGRAPH_ARROW_ZOOM,
            "cooldownTicks": cfg.FORCEGRAPH_COOLDOWN_TICKS,
            "cooldownTicksReduced": cfg.FORCEGRAPH_COOLDOWN_TICKS_REDUCED,
            "docLinesPx": cfg.FORCEGRAPH_DOC_LINES_PX,
            "tipDocChars": cfg.FORCEGRAPH_TIP_DOC_CHARS,
            "hubTopN": cfg.FORCEGRAPH_HUB_TOP_N,
            "fitPad": cfg.FORCEGRAPH_FIT_PADDING_PX,
            "fitMaxZoom": cfg.FORCEGRAPH_FIT_MAX_ZOOM,
            "fitLegendMinWidth": cfg.FORCEGRAPH_FIT_LEGEND_MIN_WIDTH,
            "linkOpacity3d": cfg.FORCEGRAPH_3D_LINK_OPACITY,
            "linkWidth3dHighlight": cfg.FORCEGRAPH_3D_LINK_WIDTH_HIGHLIGHT,
            "linkWidth3dActive": cfg.FORCEGRAPH_3D_LINK_WIDTH_ACTIVE,
            "particleWidth3d": cfg.FORCEGRAPH_3D_PARTICLE_WIDTH,
            "depthFade": cfg.FORCEGRAPH_3D_DEPTH_FADE,
            "minGlyphPx": cfg.FORCEGRAPH_3D_MIN_GLYPH_PX,
            "label3dPx": cfg.FORCEGRAPH_3D_LABEL_PX,
            "orbitSpeed": cfg.FORCEGRAPH_3D_ORBIT_SPEED,
            "flyDistance3d": cfg.FORCEGRAPH_3D_FLY_DISTANCE,
            "typeColors": {
                "file": self.node_palette().get("file", "#4f8ef7"),
                "community": self.node_palette().get("community", "#7c5aef"),
                "layer": self.node_palette().get("layer", "#4fef8e"),
                "external": self.node_palette().get("external", "#efb84f"),
            },
            "groupColors": self.group_colors(payload),
        }

    def _family_color(self, name: str) -> str:
        """Return the configured stable hash color for a group name.

        Args:
            name: Group label to hash.

        Returns:
            CSS hsl() color string.
        """
        return family_color_from_name(
            name,
            self._config.FORCEGRAPH_FAMILY_SAT_BASE,
            self._config.FORCEGRAPH_FAMILY_SAT_SPAN,
            self._config.FORCEGRAPH_FAMILY_LIGHT_BASE,
            self._config.FORCEGRAPH_FAMILY_LIGHT_SPAN,
        )

    def thumbnail_svg(self, payload: Dict[str, List[Dict[str, Any]]]) -> str:
        """Render a small ForceAtlas2 preview of the file graph as inline SVG.

        Only numeric coordinates and escaped colors reach the markup, so the
        fragment is safe to embed in the gallery card.

        Args:
            payload: Heterogeneous graph payload from build_payload.

        Returns:
            SVG markup, or an empty string when the payload has no files.
        """
        cfg = self._config
        files = [n for n in payload.get("nodes", []) if n.get("type") == "file"]
        if not files:
            return ""
        ids = sorted(n["id"] for n in files)
        known = set(ids)
        links = sorted({
            (e["source"], e["target"]) for e in payload.get("edges", [])
            if e["source"] in known and e["target"] in known and e["source"] != e["target"]
        })
        w, h = cfg.FORCEGRAPH_THUMB_WIDTH, cfg.FORCEGRAPH_THUMB_HEIGHT
        frames = forceatlas2_frames(ids, links, ForceAtlas2Settings(iterations=cfg.FORCEGRAPH_THUMB_ITERATIONS, snapshots=2))
        pos = fit_frames(frames, (0, 0, w, h), 8.0, 0.02)[-1]
        by_id = {n["id"]: n for n in files}
        top_rank = max([1e-9] + [float(n.get("rank", 0.0)) for n in files])
        parts = [f'<svg class="thumb" viewBox="0 0 {w} {h}" aria-hidden="true" focusable="false">']
        for a, b in links:
            (x1, y1), (x2, y2) = pos[a], pos[b]
            color = html.escape(str(by_id[a].get("color", "#4f8ef7")), quote=True)
            parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-opacity="0.22" stroke-width="0.7"/>')
        for nid in sorted(ids, key=lambda i: float(by_id[i].get("rank", 0.0))):
            x, y = pos[nid]
            r = 1.6 + 4.5 * math.sqrt(float(by_id[nid].get("rank", 0.0)) / top_rank)
            color = html.escape(str(by_id[nid].get("color", "#4f8ef7")), quote=True)
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}"/>')
        parts.append("</svg>")
        return "".join(parts)

    def write(
        self,
        output_path: str | Path,
        payload: Dict[str, List[Dict[str, Any]]],
        analytics: Optional[Dict[str, Any]] = None,
        title: str = "Force Graph",
        home_href: Optional[str] = "index.html",
    ) -> str:
        """Write the explorer HTML plus the vendored engine beside it.

        Args:
            output_path: Destination HTML file path.
            payload: Heterogeneous graph payload from build_payload.
            analytics: Optional analytics payload for the side panel.
            title: Document title shown in the header.
            home_href: Gallery home link relative to the page; None omits it.

        Returns:
            Rendered HTML content that was written.
        """
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        content = self.render(payload, analytics, title=title, home_href=home_href)
        target.write_text(content, encoding="utf-8")
        self.copy_vendor(target.parent)
        return content

    def copy_vendor(self, dest_dir: str | Path) -> Optional[Path]:
        """Copy the vendored 2D engine next to an exported page.

        Args:
            dest_dir: Directory holding the explorer HTML file.

        Returns:
            Vendored script path, or None when the source is missing.
        """
        source = self.vendor_source()
        if not source.is_file():
            return None
        subdir = self._config.FORCEGRAPH_VENDOR_SUBDIR.strip().strip("/")
        target = Path(dest_dir) / subdir / self._config.FORCEGRAPH_VENDOR_JS_2D
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.is_file() or target.stat().st_size != source.stat().st_size:
            shutil.copy2(source, target)
        return target

    def _node_doc(self, node: Node) -> str:
        """Return the bounded file purpose shown in the inspector ("" in privacy mode)."""
        if self._config.PRIVACY_MODE:
            return ""
        return file_purpose(node, self._config.FORCEGRAPH_DOC_MAX_CHARS)

    def _symbol_list(self, node: Node) -> List[Dict[str, Any]]:
        """Return compact symbol records (name, kind, line, signature, doc) for the inspector."""
        cfg = self._config
        out: List[Dict[str, Any]] = []
        for symbol in sorted(node.symbols, key=lambda s: (s.line, s.name))[: cfg.FORCEGRAPH_SYMBOLS_PER_NODE]:
            record: Dict[str, Any] = {"n": symbol.name, "k": symbol.kind, "l": symbol.line}
            if symbol.signature:
                record["s"] = truncate_words(symbol.signature, cfg.FORCEGRAPH_SIGNATURE_MAX_CHARS)
            if symbol.doc and not cfg.PRIVACY_MODE:
                record["d"] = truncate_words(first_sentence(symbol.doc), cfg.FORCEGRAPH_DOC_MAX_CHARS)
            out.append(record)
        return out

    def _file_color(
        self, node_id: str, family: str, layer: str, palette: Dict[str, str]
    ) -> str:
        """Resolve a file node color preferring stable family colors."""
        if family and family != "unknown":
            return self._family_color(family)
        return palette.get("file", "#4f8ef7")
