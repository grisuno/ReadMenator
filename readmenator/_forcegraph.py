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
from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding


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

        degree: Dict[str, int] = {}
        normalized: List[Edge] = []
        for edge in list(edges) + list(resolved_edges or []):
            source_file = file_of(edge.source)
            if source_file is None:
                continue
            target_file = file_of(edge.target)
            if target_file is None:
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
                family=family,
                layer=layer,
                color=color,
            )
            if community:
                cid, label = community
                add_node(
                    f"community:{cid}",
                    label,
                    "community",
                    community_id=cid,
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
                    }
                ),
            )
        )

    def write(
        self,
        output_path: str | Path,
        payload: Dict[str, List[Dict[str, Any]]],
        analytics: Optional[Dict[str, Any]] = None,
        title: str = "Force Graph",
    ) -> str:
        """Write the explorer HTML plus the vendored engine beside it.

        Args:
            output_path: Destination HTML file path.
            payload: Heterogeneous graph payload from build_payload.
            analytics: Optional analytics payload for the side panel.
            title: Document title shown in the header.

        Returns:
            Rendered HTML content that was written.
        """
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        content = self.render(payload, analytics, title=title)
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
<title>__TITLE__ | System Maps</title>
<style>
:root{--canvas:#020617;--mask:#0f172a;--mask2:#111c33;--ink:#ffffff;--muted:#94a3b8;--border:#1e293b;--accent:#22d3ee;--accent2:#f472b6;--glow:rgba(34,211,238,.18)}
html[data-theme="light"]{--canvas:#f8fafc;--mask:#ffffff;--mask2:#f1f5f9;--ink:#0f172a;--muted:#475569;--border:#e2e8f0;--accent:#0891b2;--accent2:#db2777;--glow:rgba(8,145,178,.12)}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;line-height:1.5}
a{color:var(--accent)}
.backdrop{position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(900px 420px at 15% -10%,var(--glow),transparent 70%)}
.wrap{max-width:1400px;margin:0 auto;padding:20px}
.eyebrow{color:var(--accent);font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin:0 0 8px}
h1{font-size:24px;margin:0 0 6px;background:linear-gradient(90deg,var(--ink),var(--accent) 70%,var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{color:var(--muted);font-size:12px;max-width:900px;margin:0 0 12px}
.home{display:inline-block;margin:0 0 12px;font-size:12px;text-decoration:none;border:1px solid var(--border);border-radius:10px;padding:6px 10px;color:var(--ink)}
.home:hover{border-color:var(--accent)}
.toolbar{position:sticky;top:0;z-index:5;display:flex;gap:10px;align-items:center;flex-wrap:wrap;background:color-mix(in srgb,var(--canvas) 88%,transparent);padding:10px 0}
.toolbar input[type="search"]{flex:1;min-width:200px;background:var(--mask);border:1px solid var(--border);border-radius:10px;color:var(--ink);padding:8px 10px;font:inherit;font-size:12px}
button{font:inherit;font-size:12px;background:var(--mask);border:1px solid var(--border);border-radius:10px;padding:8px 10px;color:var(--ink);cursor:pointer}
button:hover{border-color:var(--accent)}
.pills{display:flex;gap:6px;flex-wrap:wrap}
.pill{font-size:11px;color:var(--muted);border:1px solid var(--border);border-radius:999px;padding:2px 8px;cursor:pointer;user-select:none}
.pill.active{color:var(--ink);border-color:var(--accent)}
#stats{color:var(--muted);font-size:11px}
#stage{position:relative;border:1px solid var(--border);border-radius:14px;overflow:hidden;background:#020617}
html[data-theme="light"] #stage{background:#f1f5f9}
#graph{width:100%;height:70vh}
#detail{position:absolute;left:12px;bottom:12px;max-width:min(480px,90%);max-height:40%;overflow:auto;background:var(--mask);border:1px solid var(--border);border-radius:10px;padding:10px 12px;font-size:11px;white-space:pre-wrap;word-break:break-word}
#toast{position:absolute;right:12px;top:12px;max-width:min(420px,90%);background:var(--mask);border:1px solid var(--accent);border-radius:10px;padding:8px 12px;font-size:12px;display:none}
#engine-error{display:none;margin:0 0 12px;background:var(--mask);border:1px solid var(--accent2);border-radius:10px;padding:10px 12px;font-size:12px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 0}
.chip{font-size:10.5px;color:var(--muted);border:1px solid var(--border);border-radius:999px;padding:2px 8px}
footer{color:var(--muted);font-size:11px;padding:16px 0 32px}
</style>
<script src="__VENDOR_SRC__"></script>
</head>
<body>
<div class="backdrop" aria-hidden="true"></div>
<div class="wrap">
<p class="eyebrow">Zero-token knowledge base</p>
<h1>__TITLE__ <span>| Explorer</span></h1>
<p class="lede">Physics-driven explorer: files, communities, layers and externals. Drag nodes, click one to inspect, toggle community hulls. The 2D engine ships with this page; 3D loads on demand.</p>
__HOME__
<div id="engine-error" role="alert"></div>
<div class="toolbar">
<input id="search" type="search" placeholder="Filter nodes ( / )" aria-label="Filter nodes">
<div class="pills" id="pills"></div>
<button type="button" id="btn-hulls" title="Toggle community hulls">Hulls</button>
<button type="button" id="btn-png" title="Export PNG snapshot">PNG</button>
<button type="button" id="btn-json" title="Export graph JSON">JSON</button>
<button type="button" id="btn-3d" title="Toggle 2D/3D">2D/3D</button>
<button type="button" id="btn-theme" title="Toggle dark and light theme">Theme</button>
</div>
<div id="stats"></div>
<div id="stage"><div id="graph"></div><div id="detail">Click a node to inspect.</div><div id="toast"></div></div>
<div class="chips" id="analytics"></div>
<footer>Generated offline from scanned source topology. Counts reflect authored relationships only.</footer>
</div>
<script>
(function(){
"use strict";
const RAW=__DATA__;
const ANALYTICS=__ANALYTICS__;
const SETTINGS=__SETTINGS__;
const CDN_2D="__CDN_2D__";
const CDN_3D="__CDN_3D__";
let g2=null,g3=null,is3d=(SETTINGS.mode==='3d');
let highlight=new Set(),hullsOn=!!SETTINGS.hulls;
function fail(msg){
  const box=document.getElementById('engine-error');
  box.style.display='block';
  box.textContent=msg;
}
function toast(msg){
  const box=document.getElementById('toast');
  box.style.display='block';box.textContent=msg;
  setTimeout(()=>{box.style.display='none';},4000);
}
function log2val(n){return Math.max(1,Math.log2((n.symbols||0)+(n.degree||0)+(n.findings||0)+1));}
function process(raw){
  const byId={};raw.nodes.forEach(n=>{byId[n.id]=n;});
  return {nodes:raw.nodes,links:raw.edges.map(e=>({...e})),byId};
}
let DATA=process(RAW);
function nodeColor(n){
  if(highlight.size&&!highlight.has(n.id))return SETTINGS.dimNode;
  return n.color||'#4f8ef7';
}
function linkColor(l){
  if(highlight.size&&!highlight.has(l))return SETTINGS.dimLink;
  return l.color||'rgba(255,255,255,.15)';
}
function convexHull(pts){
  if(pts.length<3)return pts.slice();
  let s=0;for(let i=1;i<pts.length;i++)if(pts[i].x<pts[s].x)s=i;
  const h=[];let c=s;
  do{h.push(pts[c]);let nx=(c+1)%pts.length;
    for(let i=0;i<pts.length;i++){const cr=(pts[nx].x-pts[c].x)*(pts[i].y-pts[c].y)-(pts[nx].y-pts[c].y)*(pts[i].x-pts[c].x);if(cr<0)nx=i;}
    c=nx;}while(c!==s&&h.length<=pts.length);
  return h;
}
function inflate(h,pad){
  if(!h.length)return h;
  const cx=h.reduce((a,p)=>a+p.x,0)/h.length,cy=h.reduce((a,p)=>a+p.y,0)/h.length;
  return h.map(p=>{const dx=p.x-cx,dy=p.y-cy,l=Math.sqrt(dx*dx+dy*dy)||1;return{x:p.x+dx/l*pad,y:p.y+dy/l*pad};});
}
function drawHulls(ctx,scale){
  if(!hullsOn||is3d||!g2)return;
  const gd=g2.graphData();const nodes=gd.nodes||[];
  const byId={};nodes.forEach(n=>{byId[n.id]=n;});
  const fams=new Set(nodes.filter(n=>n.family&&n.type==='file').map(n=>n.family));
  ctx.save();
  for(const fam of fams){
    const ids=new Set(nodes.filter(n=>n.family===fam).map(n=>n.id));
    const pts=[...ids].map(id=>byId[id]).filter(n=>n&&n.x!=null).map(n=>({x:n.x,y:n.y}));
    if(!pts.length)continue;
    const hull=pts.length<3?pts:inflate(convexHull(pts),SETTINGS.hullPad/scale);
    ctx.beginPath();
    hull.forEach((p,i)=>{if(i===0)ctx.moveTo(p.x,p.y);else ctx.lineTo(p.x,p.y);});
    ctx.closePath();
    ctx.globalAlpha=SETTINGS.hullFill;ctx.fillStyle='#22d3ee';ctx.fill();
    ctx.globalAlpha=SETTINGS.hullStroke;ctx.strokeStyle='#22d3ee';ctx.lineWidth=1.5/scale;ctx.stroke();
    const top=hull.reduce((a,b)=>b.y<a.y?b:a);
    ctx.globalAlpha=0.9;ctx.font=`600 ${11/scale}px monospace`;ctx.textAlign='center';ctx.fillStyle='#e2e8f0';
    ctx.fillText(String(fam).slice(0,28),top.x,top.y-14/scale);
  }
  ctx.restore();
}
function cur(){return is3d?g3:g2;}
function mount(){
  const el=document.getElementById('graph');el.innerHTML='';
  const q=document.getElementById('search').value.toLowerCase();
  const nodes=DATA.nodes.filter(n=>!q||(n.label||'').toLowerCase().includes(q));
  const keep=new Set(nodes.map(n=>n.id));
  const links=DATA.links.filter(l=>keep.has(l.source.id||l.source)&&keep.has(l.target.id||l.target));
  try{
    if(!is3d){
      g3=null;
      g2=ForceGraph()(el).graphData({nodes,links}).nodeId('id')
        .nodeLabel(n=>`${n.label||n.id} (${n.symbols||0} sym)`)
        .nodeColor(nodeColor).nodeRelSize(SETTINGS.nodeRelSize)
        .nodeVal(n=>n.type==='file'?log2val(n):(n.type==='community'?3:2))
        .linkColor(linkColor).linkWidth(l=>highlight.has(l)?2:0.5)
        .linkDirectionalParticles(l=>highlight.has(l)?SETTINGS.particles:0)
        .onNodeClick(onClick).onBackgroundClick(clear).backgroundColor('rgba(0,0,0,0)')
        .onRenderFramePost(drawHulls);
      if(g2.d3Force('charge'))g2.d3Force('charge').strength(SETTINGS.charge);
      if(g2.d3Force('link'))g2.d3Force('link').distance(SETTINGS.linkDistance).strength(SETTINGS.linkStrength);
    }else{
      g2=null;
      g3=ForceGraph3D()(el).graphData({nodes,links}).nodeId('id')
        .nodeLabel(n=>`${n.label||n.id}`).nodeColor(nodeColor).nodeRelSize(SETTINGS.nodeRelSize)
        .nodeVal(n=>n.type==='file'?log2val(n):3)
        .linkColor(linkColor).linkWidth(l=>highlight.has(l)?3:1.2)
        .linkDirectionalParticles(l=>highlight.has(l)?SETTINGS.particles:0)
        .onNodeClick(onClick).onBackgroundClick(clear).backgroundColor('rgba(0,0,0,0)');
    }
  }catch(err){fail('Graph engine failed to start: '+(err&&err.message||err));return;}
  document.getElementById('stats').textContent=`${nodes.length} nodes / ${links.length} edges`;
}
function onClick(n){
  highlight=new Set([n.id]);
  DATA.links.forEach(l=>{const s=l.source.id||l.source,t=l.target.id||l.target;
    if(s===n.id){highlight.add(t);highlight.add(l);}if(t===n.id){highlight.add(s);highlight.add(l);}});
  const g=cur();if(g){g.nodeColor(nodeColor).linkColor(linkColor).linkWidth(l=>highlight.has(l)?2:0.5).linkDirectionalParticles(l=>highlight.has(l)?SETTINGS.particles:0);}
  document.getElementById('detail').textContent=JSON.stringify(n,null,1).slice(0,2000);
}
function clear(){highlight=new Set();const g=cur();if(g){g.nodeColor(nodeColor).linkColor(linkColor);}document.getElementById('detail').textContent='Click a node to inspect.';}
function ensure2D(cb){
  if(typeof ForceGraph!=='undefined')return cb();
  const s=document.createElement('script');s.src=CDN_2D;
  s.onload=cb;s.onerror=()=>fail('Graph engine missing: keep vendor/force-graph.min.js next to this file or connect to the network.');
  document.head.appendChild(s);
}
document.getElementById('search').addEventListener('input',mount);
document.addEventListener('keydown',e=>{
  if(e.key==='/'&&document.activeElement!==document.getElementById('search')){e.preventDefault();document.getElementById('search').focus();}
});
document.getElementById('btn-hulls').addEventListener('click',()=>{hullsOn=!hullsOn;});
document.getElementById('btn-3d').addEventListener('click',()=>{
  if(!is3d&&(typeof ForceGraph3D==='undefined')){
    toast('Loading 3D engine…');
    const s=document.createElement('script');s.src=CDN_3D;
    s.onload=()=>{is3d=true;mount();};
    s.onerror=()=>toast('3D engine needs network access.');
    document.head.appendChild(s);return;
  }
  is3d=!is3d;ensure2D(mount);
});
document.getElementById('btn-png').addEventListener('click',()=>{
  const canvas=document.querySelector('#graph canvas');
  if(!canvas){toast('Nothing to snapshot yet.');return;}
  const a=document.createElement('a');a.href=canvas.toDataURL('image/png');a.download='forcegraph.png';a.click();});
document.getElementById('btn-json').addEventListener('click',()=>{
  const blob=new Blob([JSON.stringify(RAW,null,1)],{type:'application/json'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='forcegraph.json';a.click();});
document.getElementById('btn-theme').addEventListener('click',()=>{
  const root=document.documentElement;
  const next=root.getAttribute('data-theme')==='light'?'dark':'light';
  root.setAttribute('data-theme',next);
  try{localStorage.setItem('readmenator-theme',next);}catch(err){}
});
try{
  const saved=localStorage.getItem('readmenator-theme');
  if(saved==='light'||saved==='dark')document.documentElement.setAttribute('data-theme',saved);
}catch(err){}
(function pills(){
  const types=[...new Set(RAW.nodes.map(n=>n.type))];
  const box=document.getElementById('pills');
  types.forEach(t=>{const s=document.createElement('span');s.className='pill active';s.textContent=t;
    s.addEventListener('click',()=>{s.classList.toggle('active');
      const on=new Set([...box.children].filter(c=>c.classList.contains('active')).map(c=>c.textContent));
      DATA=process({nodes:RAW.nodes.filter(n=>on.has(n.type)),edges:RAW.edges});mount();});
    box.appendChild(s);});
})();
(function analytics(){
  if(!ANALYTICS||!ANALYTICS.attribution_funnel)return;
  const f=ANALYTICS.attribution_funnel;
  const box=document.getElementById('analytics');
  box.innerHTML='';
  [[`files`,f.total],[`symbols`,f.total_symbols],[`god nodes`,f.god_nodes]].forEach(([label,value])=>{
    const s=document.createElement('span');s.className='chip';s.textContent=`${label}: ${value}`;box.appendChild(s);});
})();
ensure2D(mount);
})();
</script>
</body>
</html>
"""
