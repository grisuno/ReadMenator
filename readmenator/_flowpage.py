"""Interactive SVG viewer for laid-out architecture and execution-flow diagrams.

The diagrams arrive already placed by readmenator._flowlayout, so the
page only draws: no Mermaid, no CDN, no network. Every diagram gets a
card with its reading guide, a toolbar (fit width, 100 %, zoom in/out,
fullscreen, SVG download), drag to pan, Ctrl/Cmd + wheel to zoom,
hover highlighting of a node's arrows, and a detail panel on click
(signature, docstring summary, called functions with their docs,
component files with purposes and importer counts, a link into the API
reference). Themes follow CSS variables, so the same code serves the
standalone page and the API reference browser.
"""

from __future__ import annotations

import html
import json
import re
from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._flowlayout import FlowGraph
from readmenator._htmlpack import PAYLOAD_LOADER_JS, payload_script

_PLACEHOLDER_RE = re.compile(r"@@(TITLE|DATA|API|HOME|CSS|JS|LOADER|VIEWER_MODAL|VIEWER_JS)@@")

FLOW_VIEWER_CSS = r"""
.fv-card{background:var(--panel);border:1px solid var(--line);border-radius:12px;margin:18px 0;overflow:hidden}
.fv-head{padding:14px 16px 6px}
.fv-head h3{margin:0 0 4px;font-size:17px}
.fv-meta{color:var(--muted);font-size:13px;margin:2px 0}
.fv-cap{color:var(--muted);font-size:13.5px;margin:6px 0 0;max-width:980px}
.fv-bar{display:flex;flex-wrap:wrap;gap:6px;padding:8px 16px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--panel2);align-items:center}
.fv-bar button{background:var(--chip);color:var(--text);border:1px solid var(--line);border-radius:7px;padding:4px 10px;cursor:pointer;font-size:13px}
.fv-bar button:hover{border-color:var(--accent)}
.fv-bar .fv-hint{color:var(--muted);font-size:12px;margin-left:auto}
.fv-stage{position:relative;overflow:hidden;cursor:grab;background:var(--bg);touch-action:none}
.fv-stage.drag{cursor:grabbing}
.fv-stage svg{position:absolute;left:0;top:0;transform-origin:0 0;user-select:none}
.fv-card.full{position:fixed;inset:0;z-index:50;margin:0;border-radius:0;display:flex;flex-direction:column}
.fv-card.full .fv-stage{flex:1;height:auto!important}
.fv-panel{position:absolute;right:10px;top:10px;width:min(380px,calc(100% - 20px));max-height:calc(100% - 20px);overflow:auto;background:var(--panel);border:1px solid var(--accent);border-radius:10px;padding:12px 14px;box-shadow:0 14px 40px rgba(0,0,0,.45);display:none;font-size:13.5px;cursor:auto}
.fv-panel.open{display:block}
.fv-panel h4{margin:0 0 6px;font-size:15px;word-break:break-word}
.fv-panel pre{white-space:pre-wrap;margin:6px 0}
.fv-panel table{width:100%;border-collapse:collapse;font-size:12.5px}
.fv-panel td{border-top:1px solid var(--line);padding:4px 4px;vertical-align:top}
.fv-panel .x{float:right;cursor:pointer;color:var(--muted);border:0;background:none;font-size:16px}
.fv-svg-text{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.fv-node{cursor:pointer}
.fv-node:hover .fv-shape{stroke-width:2.6}
.fv-dim .fv-edge,.fv-dim .fv-node{opacity:.18}
.fv-dim .fv-on{opacity:1}
.fv-toc{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.fv-toc a{background:var(--chip);border-radius:999px;padding:3px 11px;font-size:13px}
"""

FLOW_VIEWER_JS = r"""
(function(){
"use strict";
var NS="http://www.w3.org/2000/svg";
var TONE={default:["--fv-box","--accent2"],entry:["--fv-entry","--accent"],external:["--fv-ext","--fv-purple"],cycle:["--fv-cycle","--fv-pink"],decision:["--fv-dec","--fv-purple"],stop:["--fv-stop","--bad"],muted:["--panel2","--line"],hub:["--fv-hub","--good"]};
function el(tag,attrs,parent){var e=document.createElementNS(NS,tag);for(var k in attrs)e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
function h(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e;}
function cssv(name){return getComputedStyle(document.documentElement).getPropertyValue(name).trim()||"#888";}
function shapePath(n){var x=n.x-n.w/2,y=n.y-n.h/2,w=n.w,hh=n.h,r;
  if(n.s==="decision")return "M"+n.x+" "+y+" L"+(x+w)+" "+n.y+" L"+n.x+" "+(y+hh)+" L"+x+" "+n.y+" Z";
  if(n.s==="loop"){var c=16;return "M"+(x+c)+" "+y+" L"+(x+w-c)+" "+y+" L"+(x+w)+" "+n.y+" L"+(x+w-c)+" "+(y+hh)+" L"+(x+c)+" "+(y+hh)+" L"+x+" "+n.y+" Z";}
  if(n.s==="io"){var k=12;return "M"+(x+k)+" "+y+" L"+(x+w)+" "+y+" L"+(x+w-k)+" "+(y+hh)+" L"+x+" "+(y+hh)+" Z";}
  r=(n.s==="terminal"||n.s==="stop")?hh/2:(n.s==="component"?10:7);
  return "M"+(x+r)+" "+y+" H"+(x+w-r)+" A"+r+" "+r+" 0 0 1 "+(x+w)+" "+(y+r)+" V"+(y+hh-r)+" A"+r+" "+r+" 0 0 1 "+(x+w-r)+" "+(y+hh)+" H"+(x+r)+" A"+r+" "+r+" 0 0 1 "+x+" "+(y+hh-r)+" V"+(y+r)+" A"+r+" "+r+" 0 0 1 "+(x+r)+" "+y+" Z";}
function bez(p,t){var u=1-t;return [u*u*u*p[0][0]+3*u*u*t*p[1][0]+3*u*t*t*p[2][0]+t*t*t*p[3][0],u*u*u*p[0][1]+3*u*u*t*p[1][1]+3*u*t*t*p[2][1]+t*t*t*p[3][1]];}
function drawGraph(G,svg,onPick){
  var defs=el("defs",{},svg);
  ["n","r","m"].forEach(function(k){var mk=el("marker",{id:"fv-arrow-"+k+"-"+G.uid,viewBox:"0 0 10 10",refX:"9",refY:"5",markerWidth:"7",markerHeight:"7",orient:"auto-start-reverse"},defs);
    el("path",{d:"M0 0 L10 5 L0 10 z",fill:k==="r"?cssv("--bad"):(k==="m"?cssv("--muted"):cssv("--accent2"))},mk);});
  el("rect",{x:0,y:0,width:G.w,height:G.h,fill:cssv("--bg")},svg);
  (G.lanes||[]).forEach(function(l,i){el("rect",{x:6,y:l.y,width:G.w-12,height:l.h,rx:12,fill:cssv(i%2?"--panel2":"--panel"),stroke:cssv("--line")},svg);
    var t=el("text",{x:18,y:l.y+18,"class":"fv-svg-text","font-size":"12","font-weight":"700",fill:cssv("--muted")},svg);t.textContent=l.t.toUpperCase();});
  var byId={},edgesOf={},gEdges=el("g",{},svg),gNodes=el("g",{},svg);
  G.nodes.forEach(function(n){byId[n.id]=n;edgesOf[n.id]=[];});
  G.edges.forEach(function(e,i){if(!e.p||e.p.length<4)return;var p=e.p;
    var red=e.y==="back"||e.y==="upward",kind=red?"r":(e.y==="dashed"?"m":"n");
    var g=el("g",{"class":"fv-edge"},gEdges);
    var d="M"+p[0][0]+" "+p[0][1]+" C"+p[1][0]+" "+p[1][1]+" "+p[2][0]+" "+p[2][1]+" "+p[3][0]+" "+p[3][1];
    var path=el("path",{d:d,fill:"none",stroke:red?cssv("--bad"):(e.y==="dashed"?cssv("--muted"):cssv("--accent2")),"stroke-width":e.y==="heavy"?3.4:1.6,"stroke-opacity":e.y==="dashed"?0.7:0.9},g);
    if(e.y==="dashed"||red)path.setAttribute("stroke-dasharray","6 5");
    if(e.y==="upward")path.setAttribute("marker-start","url(#fv-arrow-"+kind+"-"+G.uid+")");else path.setAttribute("marker-end","url(#fv-arrow-"+kind+"-"+G.uid+")");
    if(e.l){var m=bez(p,0.5),tw=e.l.length*6.6+10;el("rect",{x:m[0]-tw/2,y:m[1]-9,width:tw,height:18,rx:5,fill:cssv("--panel"),stroke:red?cssv("--bad"):cssv("--line")},g);
      var tx=el("text",{x:m[0],y:m[1]+4,"text-anchor":"middle","class":"fv-svg-text","font-size":"11",fill:red?cssv("--bad"):cssv("--text")},g);tx.textContent=e.l;}
    edgesOf[e.s]&&edgesOf[e.s].push(g);edgesOf[e.t]&&edgesOf[e.t].push(g);g.__ends=[e.s,e.t];});
  G.nodes.forEach(function(n){var tone=TONE[n.o]||TONE.default;
    var g=el("g",{"class":"fv-node",tabindex:"0"},gNodes);
    el("path",{d:shapePath(n),fill:cssv(tone[0]),stroke:cssv(tone[1]),"stroke-width":n.s==="component"?2:1.5,"class":"fv-shape"},g);
    if(n.s==="note")g.lastChild.setAttribute("stroke-dasharray","5 4");
    if(n.s==="component")el("rect",{x:n.x-n.w/2+1,y:n.y-n.h/2+1,width:n.w-2,height:5,rx:3,fill:cssv(tone[1])},g);
    var lines=[n.t].concat(n.l||[]),total=18+(lines.length-1)*15,y0=n.y-total/2+13;
    lines.forEach(function(line,i){var t=el("text",{x:n.x,y:y0+(i===0?0:3+i*15),"text-anchor":"middle","class":"fv-svg-text","font-size":i===0?"13":"11.5","font-weight":i===0?"700":"400",fill:i===0?cssv("--text"):cssv("--muted")},g);t.textContent=line;});
    var tip=el("title",{},g);tip.textContent=n.t+(n.d&&n.d.doc?"\n"+n.d.doc:"");
    g.addEventListener("mouseenter",function(){svg.classList.add("fv-dim");g.classList.add("fv-on");(edgesOf[n.id]||[]).forEach(function(x){x.classList.add("fv-on");});});
    g.addEventListener("mouseleave",function(){svg.classList.remove("fv-dim");g.classList.remove("fv-on");(edgesOf[n.id]||[]).forEach(function(x){x.classList.remove("fv-on");});});
    g.addEventListener("click",function(ev){ev.stopPropagation();onPick(n);});});
}
function drawSequence(G,svg,onPick){
  var defs=el("defs",{},svg),mk=el("marker",{id:"fv-arrow-s-"+G.uid,viewBox:"0 0 10 10",refX:"9",refY:"5",markerWidth:"7",markerHeight:"7",orient:"auto"},defs);
  el("path",{d:"M0 0 L10 5 L0 10 z",fill:cssv("--accent2")},mk);
  el("rect",{x:0,y:0,width:G.w,height:G.h,fill:cssv("--bg")},svg);
  (G.participants||[]).forEach(function(p,i){el("line",{x1:p.x,y1:58,x2:p.x,y2:G.h-12,stroke:cssv("--line"),"stroke-dasharray":"4 5"},svg);
    el("rect",{x:p.x-p.w/2,y:14,width:p.w,height:40,rx:9,fill:cssv(i?"--fv-ext":"--fv-entry"),stroke:cssv(i?"--fv-purple":"--accent")},svg);
    var t=el("text",{x:p.x,y:39,"text-anchor":"middle","class":"fv-svg-text","font-size":"13","font-weight":"700",fill:cssv("--text")},svg);t.textContent=p.t;});
  (G.messages||[]).forEach(function(m){var g=el("g",{"class":"fv-node"},svg),dir=m.x2>m.x1?1:-1;
    el("line",{x1:m.x1,y1:m.y,x2:m.x2-dir*4,y2:m.y,stroke:cssv("--accent2"),"stroke-width":1.6,"marker-end":"url(#fv-arrow-s-"+G.uid+")"},g);
    var t=el("text",{x:(m.x1+m.x2)/2,y:m.y-6,"text-anchor":"middle","class":"fv-svg-text","font-size":"11.5",fill:cssv("--text")},g);t.textContent=m.n+". "+m.l;
    var tip=el("title",{},g);tip.textContent=m.l+(m.d&&m.d.doc?"\n"+m.d.doc:"");
    g.addEventListener("click",function(ev){ev.stopPropagation();onPick({t:m.l,d:m.d||{}});});});
}
function panelHtml(n,apiHref){var d=n.d||{},out=[];
  function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});}
  out.push("<button class='x' title='Close'>&times;</button><h4>"+esc(n.t)+"</h4>");
  if(d.kind)out.push("<div class='fv-meta'>"+esc(d.kind)+(d.file?" &middot; <code>"+esc(d.file)+(d.line?":"+esc(d.line):"")+"</code>":"")+"</div>");
  if(d.summary)out.push("<p>"+esc(d.summary)+"</p>");
  if(d.sig)out.push("<pre><code>"+esc(d.sig)+"</code></pre>");
  if(d.doc)out.push("<p>"+esc(d.doc)+"</p>");
  if(d.stmt&&d.stmt!==n.t)out.push("<pre><code>"+esc(d.stmt)+"</code></pre>");
  if(d.calls&&d.calls.length)out.push("<p><b>Calls</b></p><table>"+d.calls.map(function(c){return "<tr><td><code>"+esc(c.n)+"()</code></td><td>"+esc(c.d||"")+"</td></tr>";}).join("")+"</table>");
  if(d.layers&&d.layers.length)out.push("<p class='fv-meta'>Layers: "+d.layers.map(function(l){return esc(l[0])+" "+l[1];}).join(", ")+"</p>");
  if(d.files&&d.files.length)out.push("<p><b>Files</b> (most imported first)</p><table>"+d.files.map(function(f){return "<tr><td><code>"+esc(f.f)+"</code><br><span class='fv-meta'>"+f.i+" importers, "+f.n+" symbols</span></td><td>"+esc(f.p||"")+"</td></tr>";}).join("")+"</table>");
  if(apiHref&&d.file&&d.qual)out.push("<p><a href='"+esc(apiHref+"#/m/"+encodeURIComponent(d.file)+"/"+encodeURIComponent(d.qual))+"'>Open in the API reference</a></p>");
  else if(apiHref&&d.file)out.push("<p><a href='"+esc(apiHref+"#/m/"+encodeURIComponent(d.file))+"'>Open the module in the API reference</a></p>");
  return out.join("");}
function mount(host,graphs,opts){
  opts=opts||{};host.innerHTML="";
  if(!graphs||!graphs.length){host.appendChild(h("p","fv-meta","No architecture or execution-flow diagrams for this project."));return;}
  var toc=h("div","fv-toc");host.appendChild(toc);
  graphs.forEach(function(G,gi){G.uid="g"+gi;
    var card=h("section","fv-card");card.id="fv-"+gi;host.appendChild(card);
    var a=h("a",null,G.title);a.href="javascript:void(0)";a.addEventListener("click",function(){card.scrollIntoView({behavior:"smooth"});});toc.appendChild(a);
    var head=h("div","fv-head");card.appendChild(head);head.appendChild(h("h3",null,G.title));
    var m=G.meta||{};
    if(m.entry)head.appendChild(h("div","fv-meta","Entry point "+m.entry+" at "+m.file+":"+m.line+" (score "+m.score+": "+(m.reasons||[]).join("; ")+")"));
    if(m.stats)head.appendChild(h("div","fv-meta",m.stats.components+" components, "+m.stats.tiers+" tiers, "+m.stats.edges+" dependencies shown, "+m.stats.reduced+" implied edges removed"));
    if(m.upward&&m.upward.length)head.appendChild(h("div","fv-meta","Fix first (upward): "+m.upward.map(function(u){return u[0]+" -> "+u[1]+" ("+u[2]+")";}).join("; ")));
    head.appendChild(h("p","fv-cap",G.caption||""));
    var bar=h("div","fv-bar");card.appendChild(bar);
    var stage=h("div","fv-stage");card.appendChild(stage);
    var panel=h("div","fv-panel");stage.appendChild(panel);
    var svg=el("svg",{width:G.w,height:G.h,viewBox:"0 0 "+G.w+" "+G.h,role:"img","aria-label":G.title});stage.insertBefore(svg,panel);
    function pick(n){panel.innerHTML=panelHtml(n,opts.apiHref||"");panel.classList.add("open");var x=panel.querySelector(".x");if(x)x.addEventListener("click",function(){panel.classList.remove("open");});}
    if(G.kind==="sequence")drawSequence(G,svg,pick);else drawGraph(G,svg,pick);
    var S={k:1,x:0,y:0};
    function apply(){svg.style.transform="translate("+S.x+"px,"+S.y+"px) scale("+S.k+")";}
    function clampPan(){var W=stage.clientWidth,H=stage.clientHeight,cw=G.w*S.k,ch=G.h*S.k;
      S.x=cw<=W?(W-cw)/2:Math.min(0,Math.max(W-cw,S.x));S.y=ch<=H?Math.max(0,Math.min((H-ch)/2,12)):Math.min(0,Math.max(H-ch,S.y));}
    function fit(){var W=Math.max(320,stage.clientWidth||host.clientWidth||900);S.k=Math.max(opts.minScale||0.8,Math.min(1.15,(W-16)/G.w));
      var want=G.h*S.k+24,max=card.classList.contains("full")?99999:Math.round(window.innerHeight*0.8);
      if(!card.classList.contains("full"))stage.style.height=Math.max(260,Math.min(want,max))+"px";S.x=0;S.y=0;clampPan();apply();}
    function zoom(f,cx,cy){var nk=Math.max(0.25,Math.min(3,S.k*f));cx=cx==null?stage.clientWidth/2:cx;cy=cy==null?stage.clientHeight/2:cy;
      S.x=cx-(cx-S.x)*nk/S.k;S.y=cy-(cy-S.y)*nk/S.k;S.k=nk;clampPan();apply();}
    function btn(label,title,fn){var b=h("button",null,label);b.title=title;b.addEventListener("click",fn);bar.appendChild(b);}
    btn("Fit width","Scale the diagram to the card width",fit);
    btn("100%","Actual size",function(){S.k=1;clampPan();apply();});
    btn("+","Zoom in",function(){zoom(1.25);});btn("-","Zoom out",function(){zoom(0.8);});
    btn("Fullscreen","Toggle fullscreen (Esc leaves)",function(){card.classList.toggle("full");setTimeout(fit,30);});
    btn("SVG","Download this diagram as SVG",function(){var c=svg.cloneNode(true);c.removeAttribute("style");c.setAttribute("xmlns",NS);
      var blob=new Blob([new XMLSerializer().serializeToString(c)],{type:"image/svg+xml"}),u=URL.createObjectURL(blob),a2=document.createElement("a");a2.href=u;a2.download=(G.id||"diagram").replace(/[^a-z0-9]+/gi,"_")+".svg";a2.click();setTimeout(function(){URL.revokeObjectURL(u);},500);});
    bar.appendChild(h("span","fv-hint",G.nodes.length?G.nodes.length+" nodes, "+G.edges.length+" arrows | drag to pan, Ctrl+wheel to zoom, click a node":((G.messages||[]).length+" calls | drag to pan, click a call")));
    var drag=null;
    stage.addEventListener("pointerdown",function(ev){if(ev.target.closest&&ev.target.closest(".fv-panel"))return;drag={x:ev.clientX,y:ev.clientY,sx:S.x,sy:S.y,moved:false};stage.classList.add("drag");});
    window.addEventListener("pointermove",function(ev){if(!drag)return;var dx=ev.clientX-drag.x,dy=ev.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>3)drag.moved=true;S.x=drag.sx+dx;S.y=drag.sy+dy;clampPan();apply();});
    window.addEventListener("pointerup",function(){drag=null;stage.classList.remove("drag");});
    stage.addEventListener("click",function(ev){if(!ev.target.closest(".fv-panel")&&!ev.target.closest(".fv-node"))panel.classList.remove("open");});
    stage.addEventListener("wheel",function(ev){var r=stage.getBoundingClientRect();
      if(ev.ctrlKey||ev.metaKey){ev.preventDefault();zoom(ev.deltaY<0?1.12:0.89,ev.clientX-r.left,ev.clientY-r.top);return;}
      var ch=G.h*S.k,H=stage.clientHeight;if(ch<=H)return;var before=S.y;S.y-=ev.deltaY;clampPan();if(S.y!==before){ev.preventDefault();apply();}},{passive:false});
    document.addEventListener("keydown",function(ev){if(ev.key==="Escape"&&card.classList.contains("full")){card.classList.remove("full");setTimeout(fit,30);}});
    window.addEventListener("resize",fit);
    requestAnimationFrame(fit);
  });
}
window.ReadmenatorFlows={mount:mount};
})();
"""

_THEME_CSS = r"""
:root{--bg:#0b0f17;--panel:#111827;--panel2:#0f172a;--line:#1f2937;--text:#e5e7eb;--muted:#94a3b8;--accent:#22d3ee;--accent2:#38bdf8;--bad:#f87171;--good:#34d399;--chip:#1e293b;--fv-box:#111c2e;--fv-entry:#0b3a4a;--fv-ext:#1d1838;--fv-cycle:#2a1630;--fv-dec:#1e1b4b;--fv-stop:#3f1d1d;--fv-hub:#0b3b2e;--fv-purple:#a78bfa;--fv-pink:#f472b6}
:root[data-theme="light"]{--bg:#f8fafc;--panel:#ffffff;--panel2:#f1f5f9;--line:#e2e8f0;--text:#0f172a;--muted:#475569;--accent:#0891b2;--accent2:#0284c7;--bad:#b91c1c;--good:#047857;--chip:#e2e8f0;--fv-box:#eef6ff;--fv-entry:#cffafe;--fv-ext:#f3e8ff;--fv-cycle:#fce7f3;--fv-dec:#ede9fe;--fv-stop:#fee2e2;--fv-hub:#d1fae5;--fv-purple:#7c3aed;--fv-pink:#db2777}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f8fafc;--panel:#ffffff;--panel2:#f1f5f9;--line:#e2e8f0;--text:#0f172a;--muted:#475569;--accent:#0891b2;--accent2:#0284c7;--bad:#b91c1c;--good:#047857;--chip:#e2e8f0;--fv-box:#eef6ff;--fv-entry:#cffafe;--fv-ext:#f3e8ff;--fv-cycle:#fce7f3;--fv-dec:#ede9fe;--fv-stop:#fee2e2;--fv-hub:#d1fae5;--fv-purple:#7c3aed;--fv-pink:#db2777}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px}
header{display:flex;gap:14px;align-items:center;padding:12px 20px;border-bottom:1px solid var(--line);background:var(--panel);position:sticky;top:0;z-index:5}
header h1{font-size:17px;margin:0}header .sp{margin-left:auto}header button{background:var(--chip);color:var(--text);border:1px solid var(--line);border-radius:8px;padding:5px 10px;cursor:pointer}
main{padding:12px 24px 60px;max-width:1500px;margin:0 auto}
"""

_PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TITLE@@</title>
<style>@@CSS@@</style>
</head>
<body>
<header><h1>@@TITLE@@</h1>@@API@@@@HOME@@<span class="sp"></span><button id="fv-theme" title="Toggle dark and light theme">Theme</button><button type="button" data-rm-config title="Viewer config (no reload)">Config</button></header>
<main><p class="fv-cap">Every diagram is computed from the source with zero tokens and laid out offline: tiers come from a feedback-arc-set ordering of the component graph, flows from the resolved call graph and the Python syntax tree. Click any box for its signature, docs, and files.</p><div id="fv-host"></div></main>
@@DATA@@
@@VIEWER_MODAL@@
<script>@@JS@@</script>
<script>@@LOADER@@</script>
<script>
(function(){var root=document.documentElement;try{var t=localStorage.getItem("readmenator-theme");if(t)root.setAttribute("data-theme",t);}catch(e){}
window.ReadmenatorViewerApply=function(patch){patch=patch||{};var handled=[];["theme","html_style","accent","accent2"].forEach(function(k){if(k in patch&&handled.indexOf(k)<0)handled.push(k);});if(!handled.length)return handled;try{if(typeof window.__rmFlowsDraw__==="function")window.__rmFlowsDraw__();}catch(e){}return handled;};
readmenatorPayload("fv-data",{graphs:[],api:""}).then(function(data){
function draw(){window.ReadmenatorFlows.mount(document.getElementById("fv-host"),data.graphs,{apiHref:data.api});}
window.__rmFlowsDraw__=draw;
document.getElementById("fv-theme").addEventListener("click",function(){var cur=root.getAttribute("data-theme")||(matchMedia("(prefers-color-scheme: light)").matches?"light":"dark");var n=cur==="light"?"dark":"light";root.setAttribute("data-theme",n);try{localStorage.setItem("readmenator-theme",n);}catch(e){}draw();});
draw();},readmenatorPayloadError);})();
</script>
<script>@@VIEWER_JS@@</script>
</body>
</html>
"""


def flows_payload_json(graphs: List[FlowGraph], api_href: str = "") -> str:
    """Serialise laid-out graphs for embedding in a page (angle brackets and ampersands escaped)."""
    data = json.dumps({"graphs": [g.to_dict() for g in graphs], "api": api_href}, separators=(",", ":"))
    return data.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def render_flows_page(
    graphs: List[FlowGraph], project_name: str, api_href: str = "", config: Optional[Config] = None,
) -> str:
    """Render the standalone architecture and execution-flow page.

    Args:
        graphs: Laid-out graphs from build_flow_graphs().
        project_name: Display name.
        api_href: Relative link to the API reference index.html ("" hides links).
        config: Application configuration (payload compression); defaults to Config().

    Returns:
        Complete self-contained HTML document (zero external requests).
    """
    cfg = config or Config()
    from readmenator._project_config import branding_css, display_name
    from readmenator._viewer_ui import VIEWER_MODAL_CSS, home_anchor, modal_html, modal_script

    title = html.escape(f"{display_name(cfg, project_name)}: architecture and execution flows")
    api = f'<a href="{html.escape(api_href, quote=True)}">API reference</a>' if api_href else ""
    values: Dict[str, str] = {
        "TITLE": title, "API": api, "HOME": home_anchor(cfg), "LOADER": PAYLOAD_LOADER_JS,
        "DATA": payload_script("fv-data", {"graphs": [g.to_dict() for g in graphs], "api": api_href}, cfg),
        "CSS": _THEME_CSS + FLOW_VIEWER_CSS + VIEWER_MODAL_CSS + branding_css(cfg)
        + "header a.home{border:1px solid var(--line);border-radius:8px;padding:5px 10px;font-size:13px}"
        + "header a.home svg{width:12px;height:12px;vertical-align:-1px}",
        "JS": FLOW_VIEWER_JS,
        "VIEWER_MODAL": modal_html(),
        "VIEWER_JS": modal_script(cfg),
    }
    return _PLACEHOLDER_RE.sub(lambda m: values[m.group(1)], _PAGE)


def flow_thumbnail_svg(graph: FlowGraph, width: int, height: int) -> str:
    """Render a small preview of a laid-out diagram for gallery cards.

    Only numbers and fixed colors reach the markup (no text), so nothing
    needs escaping.

    Args:
        graph: Laid-out graph (architecture tiers look best).
        width: Thumbnail width in pixels.
        height: Thumbnail height in pixels.

    Returns:
        ``<svg class="thumb" ...>`` markup, or "" for an empty graph.
    """
    if not graph.nodes or graph.width <= 0 or graph.height <= 0:
        return ""
    pad = 8.0
    scale = min((width - 2 * pad) / graph.width, (height - 2 * pad) / graph.height)
    ox = (width - graph.width * scale) / 2
    oy = (height - graph.height * scale) / 2
    colors = {"entry": "#22d3ee", "cycle": "#f472b6", "external": "#a78bfa", "decision": "#a78bfa", "stop": "#f87171"}
    parts = [f'<svg class="thumb" viewBox="0 0 {width} {height}" aria-hidden="true" focusable="false">']
    for lane in graph.lanes:
        parts.append(
            f'<rect x="{ox + 4 * scale:.1f}" y="{oy + float(lane["y"]) * scale:.1f}" width="{(graph.width - 8) * scale:.1f}" '
            f'height="{float(lane["h"]) * scale:.1f}" rx="4" fill="#0f172a" stroke="#1f2937"/>'
        )
    for edge in graph.edges:
        if len(edge.points) < 4:
            continue
        pts = [(ox + x * scale, oy + y * scale) for x, y in edge.points]
        red = edge.style in ("back", "upward")
        parts.append(
            f'<path d="M{pts[0][0]:.1f} {pts[0][1]:.1f} C{pts[1][0]:.1f} {pts[1][1]:.1f} {pts[2][0]:.1f} {pts[2][1]:.1f} '
            f'{pts[3][0]:.1f} {pts[3][1]:.1f}" fill="none" stroke="{"#f87171" if red else "#38bdf8"}" '
            f'stroke-width="{1.6 if edge.style == "heavy" else 0.9}" stroke-opacity="0.8"'
            + (' stroke-dasharray="3 3"' if red else "") + "/>"
        )
    for node in graph.nodes:
        parts.append(
            f'<rect x="{ox + (node.x - node.w / 2) * scale:.1f}" y="{oy + (node.y - node.h / 2) * scale:.1f}" '
            f'width="{node.w * scale:.1f}" height="{node.h * scale:.1f}" rx="3" fill="#111827" '
            f'stroke="{colors.get(node.tone, "#38bdf8")}" stroke-width="1.2"/>'
        )
    parts.append("</svg>")
    return "".join(parts)
