"""Force-graph explorer for the readmenator knowledge graph.

Builds a heterogeneous node-link payload (files, communities, layers,
externals) and renders a standalone HTML document on top of the
vasturiano force-graph library. The 2D engine ships vendored beside
the page so it works offline and via file://; the CDN copy is only a
fallback and the 3D engine loads on demand. Visual language (theme
tokens, cards, chips, toolbar) matches the system-maps gallery.
"""

from __future__ import annotations

import html
import json
import math
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._graphlayout import ForceAtlas2Settings, fit_frames, forceatlas2_frames
from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding
from readmenator._purpose import file_purpose, first_sentence, truncate_words
from readmenator._rank import file_pagerank
from readmenator._resolver import ImportResolver


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
                        "color": edge_palette.get("resolved_imports", "rgba(255,255,255,.15)"),
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
                    "color": edge_palette.get("resolved_imports", "rgba(255,255,255,.15)"),
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
        return (
            _HTML_TEMPLATE.replace("__TITLE__", safe_title)
            .replace("__HOME__", home_link)
            .replace("__VENDOR_SRC__", safe_vendor)
            .replace("__CDN_2D__", safe_cdn_2d)
            .replace("__CDN_3D__", safe_cdn_3d)
            .replace("__DATA__", data_json)
            .replace("__ANALYTICS__", analytics_json)
            .replace(
                "__SETTINGS__",
                json.dumps(
                    {
                        "charge": self._config.FORCEGRAPH_CHARGE,
                        "linkDistance": self._config.FORCEGRAPH_LINK_DISTANCE,
                        "linkStrength": self._config.FORCEGRAPH_LINK_STRENGTH,
                        "nodeRelSize": self._config.FORCEGRAPH_NODE_REL_SIZE,
                        "hulls": self._config.FORCEGRAPH_HULLS_ENABLED,
                        "hullFill": self._config.FORCEGRAPH_HULL_FILL_ALPHA,
                        "hullStroke": self._config.FORCEGRAPH_HULL_STROKE_ALPHA,
                        "hullPad": self._config.FORCEGRAPH_HULL_PAD,
                        "particles": self._config.FORCEGRAPH_PARTICLES_ON_HIGHLIGHT,
                        "dimNode": self._config.FORCEGRAPH_DIM_NODE,
                        "dimLink": self._config.FORCEGRAPH_DIM_LINK,
                        "mode": self._config.FORCEGRAPH_MODE,
                        "labelTopN": self._config.FORCEGRAPH_LABEL_TOP_N,
                        "labelZoom": self._config.FORCEGRAPH_LABEL_ZOOM,
                        "labelMax": self._config.FORCEGRAPH_LABEL_MAX_CHARS,
                        "clusterStrength": self._config.FORCEGRAPH_CLUSTER_STRENGTH,
                        "collidePad": self._config.FORCEGRAPH_COLLIDE_PADDING,
                        "dagLevel": self._config.FORCEGRAPH_DAG_LEVEL_DISTANCE,
                        "flyMs": self._config.FORCEGRAPH_FLY_MS,
                        "flyZoom": self._config.FORCEGRAPH_FLY_ZOOM,
                        "searchResults": self._config.FORCEGRAPH_SEARCH_RESULTS,
                        "symbolTotal": self._config.FORCEGRAPH_SYMBOLS_PER_NODE,
                    }
                ),
            )
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
            return family_color_from_name(
                family,
                self._config.FORCEGRAPH_FAMILY_SAT_BASE,
                self._config.FORCEGRAPH_FAMILY_SAT_SPAN,
                self._config.FORCEGRAPH_FAMILY_LIGHT_BASE,
                self._config.FORCEGRAPH_FAMILY_LIGHT_SPAN,
            )
        return palette.get("file", "#4f8ef7")


_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ | Graph Explorer</title>
<style>
:root{--canvas:#020617;--stage:#030a1c;--mask:#0b1224;--mask2:#111c33;--ink:#f8fafc;--muted:#94a3b8;--faint:#475569;--border:#1e293b;--accent:#22d3ee;--accent2:#f472b6;--warn:#fb7185;--ok:#34d399;--glow:rgba(34,211,238,.16);--label-bg:rgba(2,6,23,.78);--label-ink:#e2e8f0}
html[data-theme="light"]{--canvas:#f8fafc;--stage:#eef2f7;--mask:#ffffff;--mask2:#f1f5f9;--ink:#0f172a;--muted:#475569;--faint:#94a3b8;--border:#e2e8f0;--accent:#0891b2;--accent2:#db2777;--warn:#e11d48;--ok:#059669;--glow:rgba(8,145,178,.10);--label-bg:rgba(255,255,255,.88);--label-ink:#0f172a}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;line-height:1.5;display:flex;flex-direction:column}
a{color:var(--accent)}
button{font:inherit;font-size:12px;background:var(--mask);border:1px solid var(--border);border-radius:9px;padding:6px 10px;color:var(--ink);cursor:pointer;transition:border-color .15s,background .15s}
button:hover,button:focus-visible{border-color:var(--accent);outline:none}
button[aria-pressed="true"]{background:color-mix(in srgb,var(--accent) 18%,var(--mask));border-color:var(--accent)}
kbd{border:1px solid var(--border);border-bottom-width:2px;border-radius:5px;padding:0 5px;font-size:10.5px;color:var(--muted)}
.topbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:10px 16px;border-bottom:1px solid var(--border);background:color-mix(in srgb,var(--mask) 92%,transparent);backdrop-filter:blur(8px);position:relative;z-index:10}
.brand{display:flex;flex-direction:column;min-width:0;margin-right:6px}
.brand b{font-size:14px;background:linear-gradient(90deg,var(--ink),var(--accent) 70%,var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:36ch}
.brand span{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.home{font-size:12px;text-decoration:none;border:1px solid var(--border);border-radius:9px;padding:6px 10px;color:var(--ink)}
.home:hover{border-color:var(--accent)}
.searchbox{position:relative;flex:1;min-width:220px;max-width:520px}
.searchbox input{width:100%;background:var(--canvas);border:1px solid var(--border);border-radius:10px;color:var(--ink);padding:8px 10px 8px 30px;font:inherit;font-size:12px}
.searchbox input:focus{border-color:var(--accent);outline:none;box-shadow:0 0 0 3px var(--glow)}
.searchbox::before{content:"";position:absolute;left:11px;top:50%;width:9px;height:9px;border:2px solid var(--muted);border-radius:50%;transform:translateY(-60%)}
.results{position:absolute;left:0;right:0;top:calc(100% + 4px);background:var(--mask);border:1px solid var(--border);border-radius:10px;box-shadow:0 18px 40px rgba(0,0,0,.35);overflow:hidden;display:none}
.results.open{display:block}
.result{display:flex;gap:8px;align-items:center;padding:7px 10px;cursor:pointer;border-bottom:1px solid var(--border)}
.result:last-child{border-bottom:none}
.result[aria-selected="true"],.result:hover{background:var(--mask2)}
.result .dot{flex:none;width:9px;height:9px;border-radius:50%}
.result .name{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.result .sub{color:var(--muted);font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-left:auto;max-width:55%}
.seg{display:inline-flex;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.seg button{border:none;border-radius:0;border-right:1px solid var(--border)}
.seg button:last-child{border-right:none}
.group{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.app{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 380px;min-height:0}
#stage{position:relative;background:radial-gradient(1000px 520px at 20% 0%,var(--glow),transparent 70%),var(--stage);overflow:hidden;min-height:420px}
#graph{position:absolute;inset:0}
.overlay{position:absolute;z-index:3;background:color-mix(in srgb,var(--mask) 88%,transparent);border:1px solid var(--border);border-radius:12px;backdrop-filter:blur(6px)}
#hud{left:12px;top:12px;padding:6px 10px;font-size:11px;color:var(--muted);display:flex;gap:12px}
#hud b{color:var(--ink)}
#legend{left:12px;bottom:12px;max-width:280px;max-height:42%;overflow:auto;padding:8px 10px;font-size:11.5px}
#legend h3{margin:0 0 6px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);display:flex;justify-content:space-between;align-items:center}
.pills{display:flex;gap:5px;flex-wrap:wrap;margin:0 0 8px}
.pill{font-size:10.5px;color:var(--muted);border:1px solid var(--border);border-radius:999px;padding:1px 8px;cursor:pointer;user-select:none;background:transparent}
.pill.active{color:var(--ink);border-color:var(--accent)}
.fam{display:flex;align-items:center;gap:7px;width:100%;text-align:left;border:1px solid transparent;background:transparent;padding:3px 5px;border-radius:7px}
.fam:hover,.fam[aria-pressed="true"]{border-color:var(--border);background:var(--mask2)}
.fam i{flex:none;width:10px;height:10px;border-radius:50%;box-shadow:0 0 8px currentColor}
.fam span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fam em{margin-left:auto;font-style:normal;color:var(--muted)}
#toast{right:12px;top:12px;max-width:min(420px,80%);padding:8px 12px;font-size:12px;border-color:var(--accent);display:none}
#engine-error{display:none;margin:12px;background:var(--mask);border:1px solid var(--accent2);border-radius:10px;padding:10px 12px;font-size:12px}
#inspector{border-left:1px solid var(--border);background:var(--mask);overflow:auto;min-height:0;display:flex;flex-direction:column}
.insp-empty{padding:22px 18px;color:var(--muted);font-size:12px;line-height:1.8}
.insp-empty h2{color:var(--ink);font-size:14px;margin:0 0 8px}
.insp-head{padding:16px 18px 12px;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--mask);z-index:2}
.insp-nav{display:flex;gap:6px;margin-bottom:10px}
.insp-nav button{padding:3px 8px;font-size:11px}
.type{display:inline-flex;align-items:center;gap:6px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.type i{width:10px;height:10px;border-radius:50%}
.insp-head h2{margin:4px 0 4px;font-size:17px;word-break:break-word}
.path{display:flex;gap:6px;align-items:center;color:var(--muted);font-size:11px;word-break:break-all}
.path button{padding:1px 7px;font-size:10.5px;flex:none}
.badges{display:flex;gap:5px;flex-wrap:wrap;margin-top:10px}
.badge{font-size:10.5px;border:1px solid var(--border);border-radius:999px;padding:1px 8px;color:var(--ink);background:transparent}
button.badge{cursor:pointer}
.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:12px 18px;border-bottom:1px solid var(--border)}
.metric{background:var(--mask2);border:1px solid var(--border);border-radius:10px;padding:8px}
.metric b{display:block;font-size:17px}
.metric span{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.1em}
.metric.warn b{color:var(--warn)}
.rankbar{grid-column:1/-1;font-size:11px;color:var(--muted)}
.rankbar div{height:6px;border-radius:999px;background:var(--border);margin-top:5px;overflow:hidden}
.rankbar div i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2))}
.doc{padding:12px 18px;border-bottom:1px solid var(--border);color:var(--ink);font-size:12.5px;line-height:1.7}
.actions{display:flex;gap:6px;flex-wrap:wrap;padding:10px 18px;border-bottom:1px solid var(--border);align-items:center}
.actions label{font-size:11px;color:var(--muted)}
details{border-bottom:1px solid var(--border)}
summary{cursor:pointer;padding:10px 18px;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);list-style:none;display:flex;justify-content:space-between}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--faint)}
details[open] summary::after{content:"-"}
.list{padding:0 12px 10px}
.nb{display:flex;align-items:center;gap:8px;width:100%;text-align:left;border:1px solid transparent;background:transparent;padding:4px 6px;border-radius:7px}
.nb:hover,.nb:focus-visible{border-color:var(--border);background:var(--mask2)}
.nb i{flex:none;width:8px;height:8px;border-radius:50%}
.nb span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.nb em{margin-left:auto;font-style:normal;color:var(--muted);font-size:10.5px;flex:none}
.symfilter{width:calc(100% - 12px);margin:0 6px 8px;background:var(--canvas);border:1px solid var(--border);border-radius:8px;color:var(--ink);padding:5px 8px;font:inherit;font-size:11.5px}
.sym{padding:6px 6px;border-radius:7px;border:1px solid transparent}
.sym:hover{border-color:var(--border);background:var(--mask2)}
.sym .k{display:inline-block;font-size:9.5px;text-transform:uppercase;letter-spacing:.08em;border-radius:5px;padding:0 5px;margin-right:6px;background:var(--mask2);color:var(--accent);border:1px solid var(--border)}
.sym .ln{float:right;color:var(--muted);font-size:10.5px}
.sym code{display:block;color:var(--muted);font-size:10.5px;margin-top:2px;white-space:pre-wrap;word-break:break-word}
.sym p{margin:2px 0 0;font-size:11px;color:var(--ink);opacity:.85}
.more{color:var(--muted);font-size:11px;padding:4px 6px}
.chips{display:flex;flex-wrap:wrap;gap:6px;padding:12px 18px}
.chip{font-size:10.5px;color:var(--muted);border:1px solid var(--border);border-radius:999px;padding:2px 8px}
.help{padding:0 18px 18px;color:var(--muted);font-size:11px;line-height:1.9}
.fg-tip{font-family:inherit;max-width:340px;background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:10px;padding:8px 10px;font-size:11.5px;line-height:1.55;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.fg-tip b{font-size:12.5px}
.fg-tip .m{color:var(--muted)}
@media (max-width:980px){.app{grid-template-columns:minmax(0,1fr)}#stage{min-height:62vh}#inspector{border-left:none;border-top:1px solid var(--border);max-height:none}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<script src="__VENDOR_SRC__"></script>
</head>
<body>
<header class="topbar">
<div class="brand"><span>Graph explorer</span><b>__TITLE__</b></div>
__HOME__
<div class="searchbox"><input id="search" type="search" autocomplete="off" placeholder="Find file, symbol, community ( / )" aria-label="Find nodes" aria-controls="results"><div class="results" id="results" role="listbox"></div></div>
<div class="seg" role="group" aria-label="Layout">
<button type="button" data-layout="force" aria-pressed="true" title="Force-directed layout ( 1 )">Force</button>
<button type="button" data-layout="cluster" aria-pressed="false" title="Pull files toward their community centroid ( 2 )">Clusters</button>
<button type="button" data-layout="radial" aria-pressed="false" title="Concentric rings by architectural layer ( 3 )">Layers</button>
<button type="button" data-layout="dag" aria-pressed="false" title="Top-down dependency levels ( 4 )">Tree</button>
</div>
<div class="group">
<button type="button" id="btn-labels" aria-pressed="true" title="Toggle node names ( L )">Names</button>
<button type="button" id="btn-hulls" aria-pressed="true" title="Toggle community hulls ( H )">Hulls</button>
<button type="button" id="btn-flow" aria-pressed="true" title="Toggle particles on highlighted edges">Flow</button>
<button type="button" id="btn-freeze" aria-pressed="false" title="Freeze or resume physics ( Space )">Freeze</button>
<button type="button" id="btn-fit" title="Fit graph to view ( F )">Fit</button>
<button type="button" id="btn-3d" title="Toggle 2D/3D (3D loads from CDN)">3D</button>
<button type="button" id="btn-png" title="Export PNG snapshot">PNG</button>
<button type="button" id="btn-json" title="Export graph JSON">JSON</button>
<button type="button" id="btn-theme" title="Toggle dark and light theme ( T )">Theme</button>
</div>
</header>
<div id="engine-error" role="alert"></div>
<div class="app">
<div id="stage">
<div id="graph" role="application" aria-label="Interactive dependency graph"></div>
<div class="overlay" id="hud"></div>
<div class="overlay" id="legend"><h3><span>Show</span></h3><div class="pills" id="pills"></div><h3><span>Communities</span><span id="legend-hint">click to focus</span></h3><div id="families"></div></div>
<div class="overlay" id="toast" role="status"></div>
</div>
<aside id="inspector" aria-live="polite" aria-label="Node inspector"></aside>
</div>
<script>
(function(){
"use strict";
const RAW=__DATA__;
const ANALYTICS=__ANALYTICS__;
const SETTINGS=__SETTINGS__;
const CDN_2D="__CDN_2D__";
const CDN_3D="__CDN_3D__";
const reduced=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const fly=reduced?0:SETTINGS.flyMs;
const $=id=>document.getElementById(id);
const esc=t=>String(t==null?"":t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
const short=(t,n)=>{t=String(t||"");return t.length>n?t.slice(0,n-1)+"…":t;};
const TYPE_COLORS={file:"#4f8ef7",community:"#a78bfa",layer:"#34d399",external:"#f59e0b"};
const REL_NAMES={resolved_imports:"imports",imports:"imports",calls:"calls",inherits:"inherits",member_of:"member of",layered_as:"layer"};
const byId={};RAW.nodes.forEach(n=>{byId[n.id]=n;n.val=nodeVal(n);});
const out={},inn={};RAW.nodes.forEach(n=>{out[n.id]=[];inn[n.id]=[];});
RAW.edges.forEach(e=>{if(!byId[e.source]||!byId[e.target])return;out[e.source].push(e);inn[e.target].push(e);});
const files=RAW.nodes.filter(n=>n.type==="file");
const famColor={},famMembers={};
files.forEach(n=>{const f=n.family||"unknown";if(!famColor[f])famColor[f]=n.color;(famMembers[f]=famMembers[f]||[]).push(n.id);});
const labelSet=new Set(files.slice().sort((a,b)=>(b.rank||0)-(a.rank||0)||(b.degree||0)-(a.degree||0)).slice(0,SETTINGS.labelTopN).map(n=>n.id));
RAW.nodes.forEach(n=>{if(n.type==="community"||n.type==="layer")labelSet.add(n.id);});
const layerOrder=["presentation","business_logic","data_access","infrastructure","utility","testing","unknown"];
let g2=null,g3=null,is3d=(SETTINGS.mode==="3d");
const S={selected:null,hover:null,hl:new Set(),hlLinks:new Set(),depth:1,labels:true,hulls:!!SETTINGS.hulls,flow:true,frozen:false,layout:"force",isolate:false,hidden:new Set(),history:[],famFocus:null,hits:new Set(),zoom:1};
let inkCache=null;
function ink(){if(!inkCache){const cs=getComputedStyle(document.documentElement);inkCache={bg:cs.getPropertyValue("--label-bg").trim(),fg:cs.getPropertyValue("--label-ink").trim(),accent:cs.getPropertyValue("--accent").trim(),warn:cs.getPropertyValue("--warn").trim(),stage:cs.getPropertyValue("--stage").trim()};}return inkCache;}
function nodeVal(n){if(n.type==="file")return Math.max(1,Math.log2((n.symbols||0)+(n.degree||0)+(n.findings||0)+1));if(n.type==="community")return 3+Math.log2((n.size||1)+1);return 2;}
function radius(n){return Math.sqrt(Math.max(0,n.val||1))*SETTINGS.nodeRelSize;}
function fail(msg){const b=$("engine-error");b.style.display="block";b.textContent=msg;}
let toastTimer=0;
function toast(msg){const b=$("toast");b.style.display="block";b.textContent=msg;clearTimeout(toastTimer);toastTimer=setTimeout(()=>{b.style.display="none";},3200);}
function lkey(l){const s=l.source.id||l.source,t=l.target.id||l.target;return s+"|"+t+"|"+l.type;}
function colorOf(n){return n.color||TYPE_COLORS[n.type]||"#94a3b8";}
function dimmed(n){return S.hl.size>0&&!S.hl.has(n.id);}
function visible(){
  const keep=new Set();
  RAW.nodes.forEach(n=>{if(S.hidden.has(n.type))return;if(S.isolate&&S.hl.size&&!S.hl.has(n.id))return;keep.add(n.id);});
  const nodes=RAW.nodes.filter(n=>keep.has(n.id));
  const links=RAW.edges.filter(e=>keep.has(e.source)&&keep.has(e.target)).map(e=>Object.assign({},e));
  return {nodes,links};
}
function computeHighlight(id,depth){
  S.hl=new Set([id]);S.hlLinks=new Set();
  let frontier=[id];
  for(let d=0;d<depth;d++){const next=[];
    frontier.forEach(cur=>{(out[cur]||[]).forEach(e=>{S.hlLinks.add(e.source+"|"+e.target+"|"+e.type);if(!S.hl.has(e.target)){S.hl.add(e.target);next.push(e.target);}});
      (inn[cur]||[]).forEach(e=>{S.hlLinks.add(e.source+"|"+e.target+"|"+e.type);if(!S.hl.has(e.source)){S.hl.add(e.source);next.push(e.source);}});});
    frontier=next;}
}
function setHighlightSet(ids){S.hl=new Set(ids);S.hlLinks=new Set();RAW.edges.forEach(e=>{if(S.hl.has(e.source)&&S.hl.has(e.target))S.hlLinks.add(e.source+"|"+e.target+"|"+e.type);});}
function shapePath(ctx,n,x,y,r){
  ctx.beginPath();
  if(n.type==="community"){for(let i=0;i<6;i++){const a=Math.PI/3*i+Math.PI/6;const px=x+r*1.15*Math.cos(a),py=y+r*1.15*Math.sin(a);i?ctx.lineTo(px,py):ctx.moveTo(px,py);}ctx.closePath();}
  else if(n.type==="layer"){const s=r*1.05;ctx.moveTo(x,y-s*1.25);ctx.lineTo(x+s*1.25,y);ctx.lineTo(x,y+s*1.25);ctx.lineTo(x-s*1.25,y);ctx.closePath();}
  else if(n.type==="external"){ctx.moveTo(x,y-r*1.2);ctx.lineTo(x+r*1.1,y+r*0.8);ctx.lineTo(x-r*1.1,y+r*0.8);ctx.closePath();}
  else{ctx.arc(x,y,r,0,2*Math.PI);}
}
let labelBoxes=[];
function overlaps(b){for(const o of labelBoxes){if(b.x<o.x+o.w&&b.x+b.w>o.x&&b.y<o.y+o.h&&b.y+b.h>o.y)return true;}return false;}
function wantLabel(n,scale){
  if(!S.labels||dimmed(n))return false;
  if(n.id===S.selected||n.id===S.hover||S.hits.has(n.id))return true;
  if(S.hl.size&&S.hl.size<=60&&S.hl.has(n.id))return true;
  if(n.type==="external")return scale>=SETTINGS.labelZoom*1.6;
  if(n.type==="community"&&S.hulls&&S.layout!=="dag")return scale>=SETTINGS.labelZoom;
  return labelSet.has(n.id)||scale>=SETTINGS.labelZoom;
}
function drawNode(n,ctx,scale){
  const r=radius(n),c=ink(),dim=dimmed(n);
  ctx.save();
  if(n.id===S.selected||n.id===S.hover){ctx.shadowColor=colorOf(n);ctx.shadowBlur=18;}
  shapePath(ctx,n,n.x,n.y,r);
  ctx.fillStyle=dim?SETTINGS.dimNode:colorOf(n);ctx.fill();
  ctx.shadowBlur=0;
  if(n.id===S.selected){ctx.lineWidth=2.5/scale;ctx.strokeStyle=c.fg;ctx.stroke();shapePath(ctx,n,n.x,n.y,r+4/scale);ctx.lineWidth=1.2/scale;ctx.strokeStyle=c.accent;ctx.stroke();}
  else if(S.hits.has(n.id)){ctx.lineWidth=2/scale;ctx.strokeStyle=c.accent;ctx.stroke();}
  if(!dim&&n.findings>0){ctx.beginPath();ctx.arc(n.x+r*0.75,n.y-r*0.75,Math.max(1.6,r*0.32),0,2*Math.PI);ctx.fillStyle=c.warn;ctx.fill();}
  if(wantLabel(n,scale)){
    const fs=(n.type==="community"||n.type==="layer"?12.5:11)/scale;
    const text=short(n.type==="layer"?n.label.replace(/_/g," "):n.label,SETTINGS.labelMax);
    ctx.font=`${n.type==="file"?500:700} ${fs}px ui-monospace,Menlo,monospace`;
    const w=ctx.measureText(text).width,pad=3/scale,y=n.y+r+fs*0.95;
    const bx=n.x-w/2-pad,by=y-fs*0.85,bw=w+pad*2,bh=fs*1.25,rr=3/scale;
    const box={x:bx,y:by,w:bw,h:bh};
    const forced=n.id===S.selected||n.id===S.hover||S.hits.has(n.id);
    if(!forced&&overlaps(box)){ctx.restore();return;}
    labelBoxes.push(box);
    ctx.fillStyle=c.bg;
    ctx.beginPath();ctx.moveTo(bx+rr,by);ctx.arcTo(bx+bw,by,bx+bw,by+bh,rr);ctx.arcTo(bx+bw,by+bh,bx,by+bh,rr);ctx.arcTo(bx,by+bh,bx,by,rr);ctx.arcTo(bx,by,bx+bw,by,rr);ctx.fill();
    ctx.fillStyle=n.type==="file"?c.fg:colorOf(n);ctx.textAlign="center";ctx.textBaseline="alphabetic";
    ctx.fillText(text,n.x,y+fs*0.12);
  }
  ctx.restore();
}
function paintArea(n,color,ctx){ctx.fillStyle=color;ctx.beginPath();ctx.arc(n.x,n.y,radius(n)+3,0,2*Math.PI);ctx.fill();}
function linkColor(l){if(S.hl.size){return S.hlLinks.has(lkey(l))?(l.color&&l.type!=="member_of"&&l.type!=="layered_as"?l.color.replace(/[\d.]+\)$/,"0.95)"):ink().accent):SETTINGS.dimLink;}return l.color||"rgba(148,163,184,.18)";}
function linkWidth(l){return S.hlLinks.has(lkey(l))?2.2:(l.type==="member_of"||l.type==="layered_as"?0.3:0.6);}
function tip(n){
  let h=`<div class="fg-tip"><b>${esc(n.label)}</b> <span class="m">${esc(n.type)}</span>`;
  if(n.type==="file"){h+=`<div class="m">${esc(n.file)}</div><div>${n.symbols||0} symbols · ${n.degree||0} links${n.findings?` · <span style="color:var(--warn)">${n.findings} findings</span>`:""}${n.rank_pos?` · PageRank #${n.rank_pos}`:""}</div>`;
    if(n.community_label)h+=`<div class="m">${esc(n.community_label)} · ${esc(n.layer)}</div>`;
    if(n.doc)h+=`<div style="margin-top:4px">${esc(short(n.doc,200))}</div>`;}
  else if(n.type==="community")h+=`<div>${n.size||0} files</div>`;
  else{h+=`<div>${(inn[n.id]||[]).length} incoming</div>`;}
  return h+`<div class="m" style="margin-top:4px">click to inspect</div></div>`;
}
const famList=Object.keys(famMembers).sort((a,b)=>famMembers[b].length-famMembers[a].length||a.localeCompare(b));
function famAnchor(f){
  const i=famList.indexOf(f);if(i<0)return {x:0,y:0};
  const R=SETTINGS.linkDistance*Math.max(1.5,Math.sqrt(famList.length)*1.6);
  if(i===0&&famList.length>2)return {x:0,y:0};
  const k=famList.length>2?i-1:i,n=famList.length>2?famList.length-1:famList.length;
  const a=2*Math.PI*k/Math.max(1,n)-Math.PI/2;return {x:R*Math.cos(a),y:R*Math.sin(a)};
}
function famOf(n){if(n.type==="file")return n.family;if(n.type==="community")return n.label;return null;}
function clusterForce(){
  let nodes=[];
  function force(alpha){
    if(S.layout!=="cluster")return;
    const k=SETTINGS.clusterStrength*alpha;
    nodes.forEach(n=>{const f=famOf(n);if(f==null)return;const t=famAnchor(f);n.vx+=(t.x-n.x)*k;n.vy+=(t.y-n.y)*k;});
  }
  force.initialize=ns=>{nodes=ns;};return force;
}
function ringOf(n){
  let idx;
  if(n.type==="file")idx=layerOrder.indexOf(n.layer);
  else if(n.type==="layer")idx=layerOrder.indexOf(n.label);
  else if(n.type==="community")return 0;
  else return layerOrder.length+1;
  return (idx<0?layerOrder.length-1:idx)+1;
}
function radialForce(){
  let nodes=[];
  function force(alpha){
    if(S.layout!=="radial")return;
    const ring=SETTINGS.linkDistance*1.3,k=SETTINGS.clusterStrength*alpha;
    nodes.forEach(n=>{const target=ringOf(n)*ring;const d=Math.hypot(n.x,n.y)||1;const tx=n.x/d*target,ty=n.y/d*target;n.vx+=(tx-n.x)*k;n.vy+=(ty-n.y)*k;});
  }
  force.initialize=ns=>{nodes=ns;};return force;
}
function drawRings(ctx,scale){
  if(S.layout!=="radial"||is3d)return;
  const ring=SETTINGS.linkDistance*1.3,c=ink();
  ctx.save();
  for(let i=1;i<=layerOrder.length;i++){
    ctx.beginPath();ctx.arc(0,0,i*ring,0,2*Math.PI);ctx.strokeStyle=c.accent;ctx.globalAlpha=0.16;ctx.lineWidth=1/scale;ctx.setLineDash([4/scale,6/scale]);ctx.stroke();
    ctx.setLineDash([]);ctx.globalAlpha=0.7;ctx.fillStyle=c.accent;ctx.font=`600 ${11/scale}px ui-monospace,Menlo,monospace`;ctx.textAlign="left";
    const ang=-Math.PI/2+i*0.42;ctx.fillText(layerOrder[i-1].replace(/_/g," "),Math.cos(ang)*i*ring+6/scale,Math.sin(ang)*i*ring);
  }
  ctx.restore();
}
function linkStrength(l){
  const base=SETTINGS.linkStrength;
  if(l.type==="layered_as")return S.layout==="radial"?0:base*0.15;
  if(l.type==="member_of")return S.layout==="radial"?base*0.05:base*0.6;
  if(S.layout==="cluster"){const a=byId[l.source.id||l.source],b=byId[l.target.id||l.target];return a&&b&&famOf(a)===famOf(b)?base:base*0.08;}
  if(S.layout==="radial")return base*0.35;
  return base;
}
function collideForce(){
  let nodes=[];
  function force(){
    if(nodes.length>1500)return;
    const pad=SETTINGS.collidePad;
    for(let i=0;i<nodes.length;i++){const a=nodes[i];const ra=radius(a)+pad;
      for(let j=i+1;j<nodes.length;j++){const b=nodes[j];const dx=b.x-a.x,dy=b.y-a.y;const min=ra+radius(b);
        if(Math.abs(dx)>min||Math.abs(dy)>min)continue;const d=Math.hypot(dx,dy)||0.01;if(d<min){const m=(min-d)/d*0.5;a.x-=dx*m;a.y-=dy*m;b.x+=dx*m;b.y+=dy*m;}}}
  }
  force.initialize=ns=>{nodes=ns;};return force;
}
function convexHull(pts){
  if(pts.length<3)return pts.slice();
  const p=pts.slice().sort((a,b)=>a.x-b.x||a.y-b.y);
  const cross=(o,a,b)=>(a.x-o.x)*(b.y-o.y)-(a.y-o.y)*(b.x-o.x);
  const lo=[],up=[];
  for(const q of p){while(lo.length>=2&&cross(lo[lo.length-2],lo[lo.length-1],q)<=0)lo.pop();lo.push(q);}
  for(let i=p.length-1;i>=0;i--){const q=p[i];while(up.length>=2&&cross(up[up.length-2],up[up.length-1],q)<=0)up.pop();up.push(q);}
  up.pop();lo.pop();return lo.concat(up);
}
function inflate(h,pad){
  if(!h.length)return h;
  const cx=h.reduce((a,q)=>a+q.x,0)/h.length,cy=h.reduce((a,q)=>a+q.y,0)/h.length;
  return h.map(q=>{const dx=q.x-cx,dy=q.y-cy,l=Math.hypot(dx,dy)||1;return{x:q.x+dx/l*pad,y:q.y+dy/l*pad};});
}
function drawHulls(ctx,scale){
  labelBoxes=[];
  if(!S.hulls||is3d||!g2||S.layout==="dag")return;
  const nodes=g2.graphData().nodes||[];
  const groups={};nodes.forEach(n=>{if(n.type==="file"&&n.family&&n.x!=null)(groups[n.family]=groups[n.family]||[]).push(n);});
  ctx.save();
  Object.keys(groups).sort().forEach(fam=>{
    const ms=groups[fam];const col=famColor[fam]||"#22d3ee";
    const faded=S.famFocus&&S.famFocus!==fam;
    let hull=convexHull(ms.map(n=>({x:n.x,y:n.y})));
    hull=hull.length<3?hull:inflate(hull,SETTINGS.hullPad/Math.sqrt(scale)+12);
    if(hull.length<3)return;
    ctx.beginPath();
    for(let i=0;i<hull.length;i++){const a=hull[i],b=hull[(i+1)%hull.length];const mx=(a.x+b.x)/2,my=(a.y+b.y)/2;i?ctx.quadraticCurveTo(a.x,a.y,mx,my):ctx.moveTo(mx,my);}
    const a0=hull[0],b0=hull[1%hull.length];ctx.quadraticCurveTo(a0.x,a0.y,(a0.x+b0.x)/2,(a0.y+b0.y)/2);
    ctx.closePath();
    ctx.globalAlpha=(faded?0.3:1)*SETTINGS.hullFill;ctx.fillStyle=col;ctx.fill();
    ctx.globalAlpha=(faded?0.3:1)*SETTINGS.hullStroke;ctx.strokeStyle=col;ctx.lineWidth=1.4/scale;ctx.setLineDash([6/scale,4/scale]);ctx.stroke();ctx.setLineDash([]);
    if(S.labels){const top=hull.reduce((p,q)=>q.y<p.y?q:p);ctx.globalAlpha=faded?0.35:0.95;ctx.font=`700 ${12/scale}px ui-monospace,Menlo,monospace`;ctx.textAlign="center";ctx.fillStyle=col;
      ctx.fillText(short(fam,32)+"  ·  "+ms.length,top.x,top.y-8/scale);}
  });
  ctx.restore();
}
function cur(){return is3d?g3:g2;}
function refresh(){const g=cur();if(!g)return;if(is3d)g.nodeColor(g.nodeColor());g.linkColor(g.linkColor()).linkWidth(g.linkWidth()).linkDirectionalParticles(g.linkDirectionalParticles());if(!is3d)g.linkDirectionalArrowLength(g.linkDirectionalArrowLength());}
function applyLayout(){
  const g=g2;if(!g)return;
  g.dagMode(S.layout==="dag"?"td":null);
  if(S.layout==="dag")g.dagLevelDistance(SETTINGS.dagLevel);
  g.d3Force("charge").strength(S.layout==="force"||S.layout==="dag"?SETTINGS.charge:SETTINGS.charge*0.4);
  g.d3Force("link").strength(linkStrength);
  g.d3ReheatSimulation();
  document.querySelectorAll("[data-layout]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.layout===S.layout)));
  hud();
}
function build2D(el,data){
  g2=ForceGraph()(el).graphData(data).nodeId("id").nodeVal("val").nodeRelSize(SETTINGS.nodeRelSize)
    .nodeLabel(tip).nodeCanvasObject(drawNode).nodePointerAreaPaint(paintArea)
    .linkColor(linkColor).linkWidth(linkWidth)
    .linkDirectionalArrowLength(l=>S.hlLinks.has(lkey(l))&&l.type!=="member_of"&&l.type!=="layered_as"?4:0).linkDirectionalArrowRelPos(0.92)
    .linkDirectionalParticles(l=>S.flow&&S.hlLinks.has(lkey(l))?SETTINGS.particles:0).linkDirectionalParticleWidth(2.2)
    .linkDirectionalParticleColor(()=>ink().accent)
    .onNodeClick(n=>select(n.id,{fly:true})).onNodeHover(onHover).onBackgroundClick(()=>clearSelection())
    .onNodeDragEnd(n=>{n.fx=n.x;n.fy=n.y;}).onNodeRightClick(n=>{n.fx=undefined;n.fy=undefined;g2.d3ReheatSimulation();toast("Pin released: "+n.label);})
    .onZoom(z=>{S.zoom=z.k;}).onDagError(()=>{}).backgroundColor("rgba(0,0,0,0)")
    .onRenderFramePre((ctx,scale)=>{drawRings(ctx,scale);drawHulls(ctx,scale);}).cooldownTicks(reduced?60:400).onEngineStop(onFirstStop);
  g2.d3Force("charge").strength(SETTINGS.charge);
  g2.d3Force("link").distance(l=>l.type==="member_of"||l.type==="layered_as"?SETTINGS.linkDistance*1.4:SETTINGS.linkDistance);
  try{const hp=new URLSearchParams((location.hash||"").slice(1)).get("layout");if(["force","cluster","radial","dag"].includes(hp))S.layout=hp;}catch(e){}
  g2.d3Force("cluster",clusterForce());g2.d3Force("radial",radialForce());g2.d3Force("collide",collideForce());
  applyLayout();
}
function build3D(el,data){
  g3=ForceGraph3D()(el).graphData(data).nodeId("id").nodeVal("val").nodeRelSize(SETTINGS.nodeRelSize)
    .nodeLabel(tip).nodeColor(n=>dimmed(n)?SETTINGS.dimNode:colorOf(n))
    .linkColor(l=>S.hl.size?(S.hlLinks.has(lkey(l))?ink().accent:SETTINGS.dimLink):(l.color||"rgba(148,163,184,.2)"))
    .linkWidth(l=>S.hlLinks.has(lkey(l))?2:0.4).linkDirectionalParticles(l=>S.flow&&S.hlLinks.has(lkey(l))?SETTINGS.particles:0)
    .onNodeClick(n=>select(n.id,{fly:false})).onBackgroundClick(()=>clearSelection()).backgroundColor("rgba(0,0,0,0)");
}
function mount(){
  const el=$("graph");clearEl(el);g2=null;g3=null;
  const data=visible();
  try{if(is3d)build3D(el,data);else build2D(el,data);}catch(err){fail("Graph engine failed to start: "+(err&&err.message||err));return;}
  resize();hud();
  if(!is3d){setTimeout(warmFit,900);setTimeout(()=>{if(!started){started=true;readHash();if(!S.selected)warmFit();}},2600);}
}
function reload(){const g=cur();if(!g){mount();return;}g.graphData(visible());hud();}
function resize(){const g=cur();if(!g)return;const st=$("stage");g.width(st.clientWidth).height(st.clientHeight);}
let started=false;
function onFirstStop(){if(started)return;started=true;readHash();if(!S.selected){try{g2.zoomToFit(fly,48);}catch(e){}}}
function warmFit(){if(started||!g2)return;try{g2.zoomToFit(0,48);}catch(e){}}
function hud(){
  const g=cur();const d=g?g.graphData():{nodes:[],links:[]};
  const sel=S.selected&&byId[S.selected];
  const box=$("hud");clearEl(box);
function stat(num,label){const s=mkEl("span");s.appendChild(mkEl("b",null,String(num)));s.appendChild(document.createTextNode(" "+label));return s;}
  box.appendChild(stat(d.nodes.length,"nodes"));box.appendChild(stat(d.links.length,"edges"));
  box.appendChild(mkEl("span",null,S.layout));
  if(S.hl.size)box.appendChild(stat(S.hl.size,"highlighted"));
  if(sel){const s=mkEl("span");s.appendChild(document.createTextNode("focus "));s.appendChild(mkEl("b",null,short(sel.label,24)));box.appendChild(s);}
}
function onHover(n){
  S.hover=n?n.id:null;
  $("graph").style.cursor=n?"pointer":"";
  if(!S.selected&&!S.famFocus){if(n)computeHighlight(n.id,1);else{S.hl=new Set();S.hlLinks=new Set();}refresh();}
}
function select(id,opts){
  const n=byId[id];if(!n)return;
  opts=opts||{};
  if(S.selected&&S.selected!==id&&!opts.fromHistory)S.history.push(S.selected);
  S.selected=id;S.famFocus=null;markFamilies();
  computeHighlight(id,S.depth);
  if(S.isolate)reload();
  refresh();renderInspector(n);hud();
  writeHash();
  if(opts.fly!==false&&!is3d&&g2){const live=g2.graphData().nodes.find(x=>x.id===id);if(live&&live.x!=null){g2.centerAt(live.x,live.y,fly);g2.zoom(Math.max(S.zoom,SETTINGS.flyZoom),fly);}}
}
function clearSelection(){
  S.selected=null;S.hl=new Set();S.hlLinks=new Set();S.famFocus=null;S.history=[];markFamilies();
  if(S.isolate){S.isolate=false;reload();}
  refresh();renderEmpty();hud();writeHash();
}
function focusFamily(fam){
  if(S.famFocus===fam){clearSelection();return;}
  S.selected=null;S.famFocus=fam;
  const ids=new Set(famMembers[fam]||[]);
  RAW.nodes.forEach(n=>{if(n.type==="community"&&n.label===fam)ids.add(n.id);});
  setHighlightSet(ids);markFamilies();refresh();hud();
  renderFamily(fam);
  if(!is3d&&g2){try{g2.zoomToFit(fly,60,n=>ids.has(n.id));}catch(e){}}
}
function markFamilies(){document.querySelectorAll(".fam").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.fam===S.famFocus)));}
function grouped(id){
  const res={importedBy:[],imports:[],calls:[],calledBy:[],inherits:[],externals:[],members:[],other:[]};
  (inn[id]||[]).forEach(e=>{const s=byId[e.source];if(!s)return;
    if(e.type==="member_of"||e.type==="layered_as")res.members.push(e.source);
    else if(e.type==="calls")res.calledBy.push(e.source);
    else if(e.type==="inherits")res.inherits.push(e.source);
    else res.importedBy.push(e.source);});
  (out[id]||[]).forEach(e=>{const t=byId[e.target];if(!t)return;
    if(e.type==="member_of"||e.type==="layered_as")res.other.push(e.target);
    else if(t.type==="external")res.externals.push(e.target);
    else if(e.type==="calls")res.calls.push(e.target);
    else if(e.type==="inherits")res.inherits.push(e.target);
    else res.imports.push(e.target);});
  Object.keys(res).forEach(k=>{res[k]=[...new Set(res[k])].sort((a,b)=>((byId[b].rank||0)-(byId[a].rank||0))||String(byId[a].label).localeCompare(byId[b].label));});
  return res;
}
function clearEl(el){if(el.replaceChildren){el.replaceChildren();}else{while(el.firstChild){el.removeChild(el.firstChild);}}}
function mkEl(tag,cls,text){const e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined&&text!==null)e.textContent=text;return e;}
function navBarEl(){const d=mkEl("div","insp-nav");const b=mkEl("button",null,"← Back");b.type="button";b.dataset.act="back";b.title="Previous node ( Backspace )";if(!S.history.length)b.disabled=true;d.appendChild(b);const c=mkEl("button",null,"Clear");c.type="button";c.dataset.act="clear";c.title="Clear selection ( Esc )";d.appendChild(c);return d;}
function nbButtonEl(id,meta){const n=byId[id];if(!n)return null;const b=mkEl("button","nb");b.type="button";b.dataset.node=id;b.title=n.file||n.label;const dot=mkEl("i");dot.style.background=colorOf(n);b.appendChild(dot);b.appendChild(mkEl("span",null,n.label));if(meta)b.appendChild(mkEl("em",null,meta));return b;}
function sectionEl(title,entries,open){if(!entries.length)return null;const det=document.createElement("details");if(open)det.open=true;const sum=document.createElement("summary");sum.appendChild(mkEl("span",null,title+" ("+entries.length+")"));det.appendChild(sum);const list=mkEl("div","list");entries.forEach(en=>{const b=nbButtonEl(en.id,en.meta);if(b)list.appendChild(b);});det.appendChild(list);return det;}
function metricEl(num,label,warn){const d=mkEl("div","metric"+(warn?" warn":""));d.appendChild(mkEl("b",null,String(num)));d.appendChild(mkEl("span",null,label));return d;}
function renderInspector(n){
  const g=grouped(n.id);
  const totalFiles=files.length||1;
  const root=$("inspector");clearEl(root);
  const head=mkEl("div","insp-head");head.appendChild(navBarEl());
  const type=mkEl("div","type");const dot=mkEl("i");dot.style.background=colorOf(n);type.appendChild(dot);type.appendChild(mkEl("span",null,n.type));head.appendChild(type);
  head.appendChild(mkEl("h2",null,n.label));
  if(n.file){const p=mkEl("div","path");p.appendChild(mkEl("span",null,n.file));const cp=mkEl("button",null,"copy");cp.type="button";cp.dataset.act="copy";cp.dataset.copy=n.file;cp.title="Copy path";p.appendChild(cp);head.appendChild(p);}
  if(n.type==="file"){const badges=mkEl("div","badges");badges.appendChild(mkEl("span","badge",n.language||"?"));badges.appendChild(mkEl("span","badge",String(n.layer||"").replace(/_/g," ")));if(n.community_label){const cf=mkEl("button","badge",n.community_label);cf.type="button";cf.dataset.fam=n.family;cf.style.borderColor=colorOf(n);cf.title="Focus this community";badges.appendChild(cf);}head.appendChild(badges);}
  root.appendChild(head);
  const metrics=mkEl("div","metrics");
  if(n.type==="file"){
    const pct=n.rank_pos?Math.round((1-(n.rank_pos-1)/totalFiles)*100):0;
    metrics.appendChild(metricEl(n.symbols||0,"symbols"));
    metrics.appendChild(metricEl(g.importedBy.length,"used by"));
    metrics.appendChild(metricEl(g.imports.length,"imports"));
    metrics.appendChild(metricEl(g.calls.length+g.calledBy.length,"call links"));
    metrics.appendChild(metricEl(g.externals.length,"externals"));
    metrics.appendChild(metricEl(n.findings||0,"findings",!!n.findings));
    const rb=mkEl("div","rankbar","PageRank #"+(n.rank_pos||"-")+" of "+totalFiles+" · more central than "+pct+"% of files");const bar=mkEl("div");const fill=mkEl("i");fill.style.width=pct+"%";bar.appendChild(fill);rb.appendChild(bar);metrics.appendChild(rb);
    root.appendChild(metrics);
    if(n.doc)root.appendChild(mkEl("div","doc",n.doc));
  }else if(n.type==="community"){
    metrics.appendChild(metricEl(n.size||g.members.length,"files"));
    metrics.appendChild(metricEl(g.members.reduce((a,id)=>a+(byId[id].symbols||0),0),"symbols"));
    metrics.appendChild(metricEl(g.members.reduce((a,id)=>a+(byId[id].findings||0),0),"findings"));
    root.appendChild(metrics);
  }else{
    metrics.appendChild(metricEl((inn[n.id]||[]).length,"incoming"));
    metrics.appendChild(metricEl((out[n.id]||[]).length,"outgoing"));
    metrics.appendChild(metricEl(S.hl.size,"in reach"));
    root.appendChild(metrics);
  }
  const actions=mkEl("div","actions");actions.appendChild(mkEl("label",null,"Reach"));
  [1,2,3].forEach(d=>{const b=mkEl("button",null,d+" hop");b.type="button";b.dataset.depth=String(d);b.setAttribute("aria-pressed",String(S.depth===d));b.title="Highlight "+d+"-hop neighbourhood";actions.appendChild(b);});
  const iso=mkEl("button",null,"Isolate");iso.type="button";iso.dataset.act="isolate";iso.setAttribute("aria-pressed",String(S.isolate));iso.title="Show only the highlighted neighbourhood ( I )";actions.appendChild(iso);
  const fit=mkEl("button",null,"Fit");fit.type="button";fit.dataset.act="fit";fit.title="Fit the neighbourhood";actions.appendChild(fit);
  root.appendChild(actions);
  const rk=id=>byId[id].rank_pos?"#"+byId[id].rank_pos:"";
  const ent=ids=>ids.map(id=>({id,meta:rk(id)}));
  const entMeta=(ids,meta)=>ids.map(id=>({id,meta}));
  [["Used by",ent(g.importedBy),true],["Imports",ent(g.imports),true],["Called by",entMeta(g.calledBy,"calls"),false],["Calls",entMeta(g.calls,"calls"),false],["Inheritance",entMeta(g.inherits,""),false],["Members",g.members.map(id=>({id,meta:(byId[id].symbols||0)+" sym"})),n.type!=="file"],["External modules",entMeta(g.externals,""),false],["Groups",g.other.map(id=>({id,meta:byId[id].type})),false]].forEach(t=>{const s=sectionEl(t[0],t[1],t[2]);if(s)root.appendChild(s);});
  const syms=n.symbol_list||[];
  if(syms.length){
    const hidden=Math.max(0,(n.symbols||0)-syms.length);
    const det=document.createElement("details");det.open=true;const sum=document.createElement("summary");sum.appendChild(mkEl("span",null,"Symbols ("+(n.symbols||syms.length)+")"));det.appendChild(sum);
    const list=mkEl("div","list");const filt=mkEl("input");filt.className="symfilter";filt.id="symfilter";filt.type="search";filt.placeholder="filter symbols";filt.setAttribute("aria-label","Filter symbols");list.appendChild(filt);
    const sl=mkEl("div");sl.id="symlist";
    syms.forEach(s=>{const row=mkEl("div","sym");row.dataset.name=String(s.n).toLowerCase();row.appendChild(mkEl("span","k",s.k));row.appendChild(mkEl("b",null,s.n));row.appendChild(mkEl("span","ln","L"+s.l));if(s.s)row.appendChild(mkEl("code",null,s.s));if(s.d)row.appendChild(mkEl("p",null,s.d));sl.appendChild(row);});
    list.appendChild(sl);
    if(hidden)list.appendChild(mkEl("div","more","+"+hidden+" more symbols in source"));
    det.appendChild(list);root.appendChild(det);
  }
  const f=$("symfilter");if(f)f.addEventListener("input",()=>{const q=f.value.trim().toLowerCase();document.querySelectorAll("#symlist .sym").forEach(el=>{el.style.display=!q||el.dataset.name.includes(q)?"":"none";});});
}
function renderFamily(fam){
  const ids=(famMembers[fam]||[]).slice().sort((a,b)=>(byId[b].rank||0)-(byId[a].rank||0));
  const sym=ids.reduce((a,id)=>a+(byId[id].symbols||0),0),fnd=ids.reduce((a,id)=>a+(byId[id].findings||0),0);
  let internal=0,crossing=0;const set=new Set(ids);
  RAW.edges.forEach(e=>{if(e.type!=="resolved_imports")return;const a=set.has(e.source),b=set.has(e.target);if(a&&b)internal++;else if(a!==b)crossing++;});
  const root=$("inspector");clearEl(root);
  const head=mkEl("div","insp-head");head.appendChild(navBarEl());
  const type=mkEl("div","type");const dot=mkEl("i");dot.style.background=famColor[fam]||"#888";type.appendChild(dot);type.appendChild(mkEl("span",null,"community"));head.appendChild(type);
  head.appendChild(mkEl("h2",null,fam));root.appendChild(head);
  const metrics=mkEl("div","metrics");
  metrics.appendChild(metricEl(ids.length,"files"));metrics.appendChild(metricEl(sym,"symbols"));metrics.appendChild(metricEl(fnd,"findings",!!fnd));
  const pct=internal+crossing?Math.round(internal/(internal+crossing)*100):0;
  const rb=mkEl("div","rankbar","Cohesion "+pct+"% · "+internal+" internal imports, "+crossing+" crossing");const bar=mkEl("div");const fill=mkEl("i");fill.style.width=pct+"%";bar.appendChild(fill);rb.appendChild(bar);metrics.appendChild(rb);
  root.appendChild(metrics);
  const s=sectionEl("Files by PageRank",ids.map(id=>({id,meta:byId[id].rank_pos?"#"+byId[id].rank_pos:""})),true);if(s)root.appendChild(s);
}
function renderEmpty(){
  const f=ANALYTICS&&ANALYTICS.attribution_funnel?ANALYTICS.attribution_funnel:null;
  const top=files.slice().sort((a,b)=>(a.rank_pos||1e9)-(b.rank_pos||1e9)).slice(0,10);
  const root=$("inspector");clearEl(root);
  const box=mkEl("div","insp-empty");box.appendChild(mkEl("h2",null,"Inspect any node"));
  box.appendChild(mkEl("div",null,"Hover a node to preview its neighbourhood; click to open its passport: purpose, metrics, PageRank, symbols with signatures, and every neighbour grouped by relation. Neighbours are clickable, so you can walk the graph from here."));
  root.appendChild(box);
  if(f){const chips=mkEl("div","chips");[["files",f.total],["symbols",f.total_symbols],["god nodes",f.god_nodes],["attributed",f.attributed]].forEach(p=>chips.appendChild(mkEl("span","chip",p[0]+" "+p[1])));root.appendChild(chips);}
  const s=sectionEl("Most central files (PageRank)",top.map(n=>({id:n.id,meta:"#"+(n.rank_pos||"-")})),true);if(s)root.appendChild(s);
  const help=mkEl("div","help");
  function kbdEl(t){const k=document.createElement("kbd");k.textContent=t;return k;}
  [["k","/"],["t"," find · "],["k","Esc"],["t"," clear · "],["k","Backspace"],["t"," back · "],["k","1"],["t","-"],["k","4"],["t"," layouts · "],["k","L"],["t"," names · "],["k","H"],["t"," hulls · "],["k","I"],["t"," isolate · "],["k","F"],["t"," fit · "],["k","Space"],["t"," freeze · "],["k","T"],["t"," theme. Drag pins a node; right-click releases it. Deep links: "]].forEach(p=>{help.appendChild(p[0]==="k"?kbdEl(p[1]):document.createTextNode(p[1]));});
  help.appendChild(mkEl("code",null,"#node=<id>&layout=cluster|radial|dag"));help.appendChild(document.createTextNode("."));
  root.appendChild(help);
}
$("inspector").addEventListener("click",ev=>{
  const t=ev.target.closest("button");if(!t)return;
  if(t.dataset.node){select(t.dataset.node,{fly:true});return;}
  if(t.dataset.fam){focusFamily(t.dataset.fam);return;}
  if(t.dataset.depth){S.depth=+t.dataset.depth;if(S.selected)select(S.selected,{fly:false,fromHistory:true});return;}
  const act=t.dataset.act;
  if(act==="back")goBack();
  else if(act==="clear")clearSelection();
  else if(act==="isolate"){S.isolate=!S.isolate;reload();if(S.selected)renderInspector(byId[S.selected]);}
  else if(act==="fit"){if(g2&&S.hl.size){try{g2.zoomToFit(fly,60,n=>S.hl.has(n.id));}catch(e){}}}
  else if(act==="copy"){try{navigator.clipboard.writeText(t.dataset.copy);toast("Path copied");}catch(e){toast(t.dataset.copy);}}
});
function goBack(){const prev=S.history.pop();if(prev)select(prev,{fly:true,fromHistory:true});}
let hits=[],hitIdx=0;
function runSearch(){
  const q=$("search").value.trim().toLowerCase();const box=$("results");
  if(!q){hits=[];S.hits=new Set();box.classList.remove("open");clearEl(box);refresh();return;}
  const scored=[];
  RAW.nodes.forEach(n=>{const label=String(n.label).toLowerCase(),path=String(n.file||n.id).toLowerCase();let s=0,via="";
    if(label===q)s=100;else if(label.startsWith(q))s=60;else if(label.includes(q))s=40;else if(path.includes(q))s=25;
    if(!s&&n.symbol_list){const m=n.symbol_list.find(x=>String(x.n).toLowerCase().includes(q));if(m){s=20;via=m.n+" L"+m.l;}}
    if(s)scored.push({n,s:s+(n.type==="file"?5:0)+Math.min(5,(n.degree||0)/10),via});});
  scored.sort((a,b)=>b.s-a.s||String(a.n.label).localeCompare(b.n.label));
  hits=scored.slice(0,SETTINGS.searchResults);hitIdx=0;
  S.hits=new Set(scored.map(x=>x.n.id));refresh();
  clearEl(box);
  if(hits.length){hits.forEach((x,i)=>{const r=mkEl("div","result");r.setAttribute("role","option");r.dataset.i=String(i);r.setAttribute("aria-selected",String(i===0));const dot=mkEl("i","dot");dot.style.background=colorOf(x.n);r.appendChild(dot);r.appendChild(mkEl("span","name",x.n.label));r.appendChild(mkEl("span","sub",x.via?("symbol "+x.via):(x.n.file||x.n.type)));box.appendChild(r);});}
  else{const r=mkEl("div","result");const sub=mkEl("span","sub","no match");sub.style.margin="0";r.appendChild(sub);box.appendChild(r);}
  box.classList.add("open");
}
function pickHit(i){const x=hits[i];if(!x)return;$("results").classList.remove("open");select(x.n.id,{fly:true});}
$("search").addEventListener("input",runSearch);
$("search").addEventListener("keydown",ev=>{
  if(ev.key==="ArrowDown"||ev.key==="ArrowUp"){ev.preventDefault();if(!hits.length)return;hitIdx=(hitIdx+(ev.key==="ArrowDown"?1:hits.length-1))%hits.length;document.querySelectorAll(".result").forEach((el,i)=>el.setAttribute("aria-selected",String(i===hitIdx)));}
  else if(ev.key==="Enter"){ev.preventDefault();pickHit(hitIdx);}
  else if(ev.key==="Escape"){$("search").value="";runSearch();$("search").blur();}
});
$("results").addEventListener("mousedown",ev=>{const r=ev.target.closest(".result");if(r&&r.dataset.i)pickHit(+r.dataset.i);});
$("search").addEventListener("blur",()=>setTimeout(()=>$("results").classList.remove("open"),150));
function toggle(btn,key,after){S[key]=!S[key];btn.setAttribute("aria-pressed",String(S[key]));if(after)after();}
$("btn-labels").addEventListener("click",e=>toggle(e.currentTarget,"labels"));
$("btn-hulls").addEventListener("click",e=>toggle(e.currentTarget,"hulls"));
$("btn-hulls").setAttribute("aria-pressed",String(S.hulls));
$("btn-flow").addEventListener("click",e=>toggle(e.currentTarget,"flow",refresh));
$("btn-freeze").addEventListener("click",e=>toggle(e.currentTarget,"frozen",()=>{const g=cur();if(!g)return;if(S.frozen){g.d3Force&&g.cooldownTicks(0);}else{g.cooldownTicks(Infinity);g.d3ReheatSimulation&&g.d3ReheatSimulation();}toast(S.frozen?"Physics frozen":"Physics resumed");}));
$("btn-fit").addEventListener("click",()=>{const g=cur();if(g&&g.zoomToFit)g.zoomToFit(fly,48);});
document.querySelectorAll("[data-layout]").forEach(b=>b.addEventListener("click",()=>{if(is3d){toast("Layouts apply to the 2D view");return;}S.layout=b.dataset.layout;applyLayout();hud();writeHash();toast("Layout: "+b.textContent);}));
$("btn-3d").addEventListener("click",()=>{
  if(!is3d&&(typeof ForceGraph3D==="undefined")){
    toast("Loading 3D engine…");
    const s=document.createElement("script");s.src=CDN_3D;
    s.onload=()=>{is3d=true;mount();};s.onerror=()=>toast("3D engine needs network access.");
    document.head.appendChild(s);return;}
  is3d=!is3d;ensure2D(mount);
});
$("btn-png").addEventListener("click",()=>{
  const canvas=document.querySelector("#graph canvas");
  if(!canvas){toast("Nothing to snapshot yet.");return;}
  const a=document.createElement("a");a.href=canvas.toDataURL("image/png");a.download="forcegraph.png";a.click();});
$("btn-json").addEventListener("click",()=>{
  const blob=new Blob([JSON.stringify(RAW,null,1)],{type:"application/json"});
  const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="forcegraph.json";a.click();});
function toggleTheme(){
  const root=document.documentElement;const next=root.getAttribute("data-theme")==="light"?"dark":"light";
  root.setAttribute("data-theme",next);inkCache=null;
  try{localStorage.setItem("readmenator-theme",next);}catch(err){}
}
$("btn-theme").addEventListener("click",toggleTheme);
try{const saved=localStorage.getItem("readmenator-theme");if(saved==="light"||saved==="dark")document.documentElement.setAttribute("data-theme",saved);}catch(err){}
document.addEventListener("keydown",e=>{
  const tag=(e.target&&e.target.tagName)||"";
  if(tag==="INPUT"||tag==="TEXTAREA")return;
  if(e.key==="/"){e.preventDefault();$("search").focus();}
  else if(e.key==="Escape")clearSelection();
  else if(e.key==="Backspace"){e.preventDefault();goBack();}
  else if(e.key==="l"||e.key==="L")$("btn-labels").click();
  else if(e.key==="h"||e.key==="H")$("btn-hulls").click();
  else if(e.key==="f"||e.key==="F")$("btn-fit").click();
  else if(e.key==="t"||e.key==="T")toggleTheme();
  else if(e.key===" "){e.preventDefault();$("btn-freeze").click();}
  else if(e.key==="i"||e.key==="I"){if(S.selected){S.isolate=!S.isolate;reload();renderInspector(byId[S.selected]);}}
  else if(["1","2","3","4"].includes(e.key)){const b=document.querySelectorAll("[data-layout]")[+e.key-1];if(b)b.click();}
});
(function pills(){
  const types=[...new Set(RAW.nodes.map(n=>n.type))];
  const box=$("pills");
  types.forEach(t=>{const s=document.createElement("button");s.type="button";s.className="pill active";s.textContent=t;s.title="Show or hide "+t+" nodes";
    s.addEventListener("click",()=>{s.classList.toggle("active");if(s.classList.contains("active"))S.hidden.delete(t);else S.hidden.add(t);reload();});
    box.appendChild(s);});
})();
(function families(){
  const box=$("families");
  const fams=Object.keys(famMembers).sort((a,b)=>famMembers[b].length-famMembers[a].length||a.localeCompare(b));
  if(!fams.length){$("legend-hint").textContent="none";return;}
  fams.forEach(f=>{const b=document.createElement("button");b.type="button";b.className="fam";b.dataset.fam=f;b.setAttribute("aria-pressed","false");b.title="Focus "+f;
    const dot=mkEl("i");dot.style.background=famColor[f];dot.style.color=famColor[f];b.appendChild(dot);b.appendChild(mkEl("span",null,f));b.appendChild(mkEl("em",null,String(famMembers[f].length)));
    b.addEventListener("click",()=>focusFamily(f));box.appendChild(b);});
})();
function readHash(){
  let params;try{params=new URLSearchParams((location.hash||"").slice(1));}catch(e){return;}
  const id=params.get("node");if(id&&byId[id])select(id,{fly:true});
}
function writeHash(){const p=new URLSearchParams();if(S.selected)p.set("node",S.selected);if(S.layout!=="force")p.set("layout",S.layout);try{history.replaceState(null,"","#"+p.toString());}catch(e){}}
function ensure2D(cb){
  if(typeof ForceGraph!=="undefined")return cb();
  const s=document.createElement("script");s.src=CDN_2D;
  s.onload=cb;s.onerror=()=>fail("Graph engine missing: keep vendor/force-graph.min.js next to this file or connect to the network.");
  document.head.appendChild(s);
}
window.addEventListener("resize",resize);
renderEmpty();
ensure2D(mount);
})();
</script>
</body>
</html>
"""
