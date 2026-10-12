"""Self-contained HTML browser for the deterministic API reference.

One file, zero external requests: the reference is embedded as JSON
(angle brackets escaped) and rendered client-side with a module tree,
instant search over names, qualnames and summaries, module pages with
signatures, parameter tables, returns, raises, examples, admonitions,
inheritance and call links, a class hierarchy, a general index, a
coverage report, hash deep links, and a dark / light theme that shares
the readmenator theme key.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import PurePosixPath
from typing import Dict, List, Optional

from readmenator._apidocs import ApiReference
from readmenator._config import Config
from readmenator._flowlayout import FlowGraph
from readmenator._flowpage import FLOW_VIEWER_CSS, FLOW_VIEWER_JS


_PLACEHOLDER_RE = re.compile(r"@@(TITLE|DATA|FVCSS|FVJS)@@")


def _payload(reference: ApiReference, project_name: str, config: Config) -> Dict[str, object]:
    """Build the compact JSON payload consumed by the page script."""
    entities: List[Dict[str, object]] = []
    for entity in reference.entities.values():
        record = entity.to_dict()
        record["display"] = ""
        if entity.kind == "module":
            path = PurePosixPath(entity.file)
            if entity.language == "py":
                parts = list(path.with_suffix("").parts)
                if parts and parts[-1] == "__init__":
                    parts = parts[:-1]
                record["display"] = ".".join(parts) or path.stem
            else:
                record["display"] = entity.file
        entities.append(record)
    return {
        "project": project_name,
        "meta": reference.meta,
        "coverage": reference.coverage,
        "modules": reference.modules,
        "entities": entities,
        "warnings": [w.to_dict() for w in reference.warnings[: max(1, int(config.APIDOCS_MAX_WARNINGS_LISTED))]],
        "warning_total": len(reference.warnings),
        "summary_max": int(config.APIDOCS_SUMMARY_MAX_CHARS),
    }


def render_api_site(
    reference: ApiReference, project_name: str, config: Config, flow_graphs: Optional[List[FlowGraph]] = None,
) -> str:
    """Render the standalone HTML API browser.

    Args:
        reference: The API reference.
        project_name: Display name of the project.
        config: Application configuration.
        flow_graphs: Laid-out architecture and execution-flow diagrams,
            drawn as interactive SVG in the Flows tab (no network).

    Returns:
        Complete HTML document text.
    """
    payload = _payload(reference, project_name, config)
    payload["flows"] = [g.to_dict() for g in (flow_graphs or [])]
    data = json.dumps(payload, separators=(",", ":"))
    data = data.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    values = {"TITLE": html.escape(f"{project_name} API Reference"), "DATA": data,
              "FVCSS": FLOW_VIEWER_CSS, "FVJS": FLOW_VIEWER_JS}
    return _PLACEHOLDER_RE.sub(lambda m: values[m.group(1)], _TEMPLATE)


_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TITLE@@</title>
<style>
:root{--bg:#0b0f17;--panel:#111827;--panel2:#0f172a;--line:#1f2937;--text:#e5e7eb;--muted:#94a3b8;--accent:#22d3ee;--accent2:#38bdf8;--warn:#fbbf24;--bad:#f87171;--good:#34d399;--code:#0a0e15;--kw:#c084fc;--str:#a3e635;--chip:#1e293b;--fv-box:#111c2e;--fv-entry:#0b3a4a;--fv-ext:#1d1838;--fv-cycle:#2a1630;--fv-dec:#1e1b4b;--fv-stop:#3f1d1d;--fv-hub:#0b3b2e;--fv-purple:#a78bfa;--fv-pink:#f472b6}
:root[data-theme="light"]{--bg:#f8fafc;--panel:#ffffff;--panel2:#f1f5f9;--line:#e2e8f0;--text:#0f172a;--muted:#475569;--accent:#0891b2;--accent2:#0284c7;--warn:#b45309;--bad:#b91c1c;--good:#047857;--code:#f1f5f9;--kw:#7c3aed;--str:#4d7c0f;--chip:#e2e8f0;--fv-box:#eef6ff;--fv-entry:#cffafe;--fv-ext:#f3e8ff;--fv-cycle:#fce7f3;--fv-dec:#ede9fe;--fv-stop:#fee2e2;--fv-hub:#d1fae5;--fv-purple:#7c3aed;--fv-pink:#db2777}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f8fafc;--panel:#ffffff;--panel2:#f1f5f9;--line:#e2e8f0;--text:#0f172a;--muted:#475569;--accent:#0891b2;--accent2:#0284c7;--warn:#b45309;--bad:#b91c1c;--good:#047857;--code:#f1f5f9;--kw:#7c3aed;--str:#4d7c0f;--chip:#e2e8f0;--fv-box:#eef6ff;--fv-entry:#cffafe;--fv-ext:#f3e8ff;--fv-cycle:#fce7f3;--fv-dec:#ede9fe;--fv-stop:#fee2e2;--fv-hub:#d1fae5;--fv-purple:#7c3aed;--fv-pink:#db2777}}
*{box-sizing:border-box}html,body{margin:0;height:100%}
body{background:var(--bg);color:var(--text);font:15px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px}
code{background:var(--chip);padding:1px 5px;border-radius:4px}
pre{background:var(--code);border:1px solid var(--line);border-radius:8px;padding:12px 14px;overflow:auto;margin:10px 0}
pre code{background:none;padding:0}
header{position:sticky;top:0;z-index:5;display:flex;gap:12px;align-items:center;padding:10px 16px;background:var(--panel);border-bottom:1px solid var(--line)}
header h1{font-size:16px;margin:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
header nav{display:flex;gap:10px;font-size:14px}
.search{position:relative;flex:1;max-width:520px;margin-left:auto}
.search input,.side input{width:100%;padding:7px 10px;border-radius:8px;border:1px solid var(--line);background:var(--panel2);color:var(--text)}
.results{position:absolute;top:38px;left:0;right:0;background:var(--panel);border:1px solid var(--line);border-radius:8px;max-height:60vh;overflow:auto;display:none;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.results a{display:block;padding:7px 10px;border-bottom:1px solid var(--line);color:var(--text)}
.results a.sel,.results a:hover{background:var(--chip);text-decoration:none}
.results small{color:var(--muted)}
button{background:var(--chip);color:var(--text);border:1px solid var(--line);border-radius:8px;padding:6px 10px;cursor:pointer}
.layout{display:grid;grid-template-columns:300px 1fr;min-height:calc(100% - 52px)}
.side{border-right:1px solid var(--line);padding:12px;position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto;background:var(--panel2)}
.side h4{margin:14px 0 4px;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.06em}
.side a{display:block;padding:2px 6px;border-radius:5px;color:var(--text);font-size:13.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.side a.active{background:var(--chip);color:var(--accent)}
.side .sub a{padding-left:18px;color:var(--muted);font-size:12.5px}
main{padding:22px 32px 80px;max-width:1100px;min-width:0}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:16px 0}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px}
.tile b{display:block;font-size:22px;color:var(--accent)}
.tile span{color:var(--muted);font-size:13px}
table{border-collapse:collapse;width:100%;margin:10px 0;font-size:14px}
th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{background:var(--panel2)}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:14px 0}
.card .card{background:var(--panel2)}
.card h3,.card h4,.card h5{margin:0 0 6px;font-size:16px;word-break:break-word}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 8px;font-size:12px}
.badge{background:var(--chip);border-radius:999px;padding:1px 9px;color:var(--muted)}
.badge.kind{color:var(--accent)}.badge.dep{color:var(--bad)}.badge.priv{color:var(--warn)}
.src{color:var(--muted);font-size:12.5px}
.note{border-left:3px solid var(--accent2);background:var(--panel2);padding:6px 10px;border-radius:0 8px 8px 0;margin:8px 0}
.note.warning,.note.deprecated{border-color:var(--bad)}
.refs{font-size:13.5px;color:var(--muted);margin:6px 0}
.bar{height:8px;background:var(--chip);border-radius:6px;overflow:hidden;min-width:80px}
.bar i{display:block;height:100%;background:var(--good)}
.kw{color:var(--kw)}.st{color:var(--str)}
ul.tree{list-style:none;padding-left:18px}ul.tree>li{margin:2px 0}
.muted{color:var(--muted)}
.letters a{margin-right:8px}
@media (max-width:860px){.layout{grid-template-columns:1fr}.side{position:static;height:auto;max-height:40vh}main{padding:16px}header nav{display:none}}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
@@FVCSS@@
</style>
</head>
<body>
<header>
  <h1 id="title"></h1>
  <nav><a href="#/">Overview</a><a href="#/flows">Flows</a><a href="#/hierarchy">Hierarchy</a><a href="#/index">Index</a><a href="#/coverage">Coverage</a></nav>
  <div class="search"><input id="q" type="search" placeholder="Search API ( / )" autocomplete="off" aria-label="Search the API"><div class="results" id="results" role="listbox"></div></div>
  <button id="theme" title="Toggle dark and light theme">Theme</button>
</header>
<div class="layout">
  <aside class="side"><input id="filter" type="search" placeholder="Filter modules" aria-label="Filter modules"><div id="tree"></div></aside>
  <main id="main"></main>
</div>
<script type="application/json" id="api-data">@@DATA@@</script>
<script>@@FVJS@@</script>
<script>
(function(){
"use strict";
var D=JSON.parse(document.getElementById("api-data").textContent);
var E={},byName={},byQual={};
D.entities.forEach(function(e){E[e.uid]=e;if(e.kind!=="module"){(byName[e.name]=byName[e.name]||[]).push(e);(byQual[e.qualname]=byQual[e.qualname]||[]).push(e);}});
var CLASS=["class","struct","interface","trait","enum","record","protocol","union","exception","extension","object","impl","type_alias"];
var CALL=["function","method","constructor","property","classmethod","staticmethod","macro","async_function"];
var DATA=["attribute","variable","constant","field"];
var TITLES={class:"Classes",struct:"Structs",interface:"Interfaces",trait:"Traits",enum:"Enums",record:"Records",protocol:"Protocols",union:"Unions",exception:"Exceptions",extension:"Extensions",object:"Objects",impl:"Implementations",type_alias:"Type Aliases",function:"Functions",macro:"Macros",constant:"Constants",variable:"Variables"};
var KW=/\b(def|class|async|await|return|function|fn|func|pub|public|private|protected|static|const|let|var|val|struct|enum|trait|impl|interface|extends|implements|void|int|bool|str|self|None|True|False|null|new|abstract|override|virtual|export|import|from|type|where|mut|final)\b/g;
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});}
function hl(code){return esc(code).replace(/(&quot;.*?&quot;|&#39;.*?&#39;)/g,'<span class="st">$1</span>').replace(KW,'<span class="kw">$1</span>');}
function href(e){if(!e)return "#/";if(e.kind==="module")return "#/m/"+encodeURIComponent(e.uid);return "#/m/"+encodeURIComponent(e.file)+"/"+encodeURIComponent(e.qualname);}
function modName(e){var m=E[e.file]||e;return m.display||m.file;}
function resolve(name,ctx){var t=String(name).replace(/^~/,"").replace(/\(\)$/,"").replace(/#|::/g,".");if(!t)return null;
  var c=byQual[t]||[];if(!c.length&&t.indexOf(".")<0)c=byName[t]||[];
  if(!c.length){var p=t.split(".");if(p.length>1)c=byQual[p.slice(-2).join(".")]||byName[p[p.length-1]]||[];}
  if(!c.length)return null;var same=c.filter(function(x){return x.file===ctx;});if(same.length)return same[0];
  if(c.length===1)return c[0];var ty=c.filter(function(x){return CLASS.indexOf(x.kind)>=0;});return ty.length===1?ty[0]:null;}
function link(e,label){return '<a href="'+href(e)+'"><code>'+esc(label||(e.kind==="module"?modName(e):e.qualname))+'</code></a>';}
function linkUid(u){var e=E[u];return e?link(e):'<code>'+esc(u)+'</code>';}
function inline(s,ctx){
  var parts=String(s).split(/(`[^`]+`)/g);
  return parts.map(function(p){
    if(p.length>1&&p[0]==="`"&&p[p.length-1]==="`"){var inner=p.slice(1,-1);var t=resolve(inner,ctx);return t?link(t,inner):"<code>"+esc(inner)+"</code>";}
    var h=esc(p);
    h=h.replace(/:(?:py:)?(?:class|func|meth|attr|mod|obj|exc|data|const):(?:`|&#39;)?~?([\w.]+)`?/g,function(m,n){var t=resolve(n,ctx);return t?link(t,n):"<code>"+n+"</code>";});
    h=h.replace(/\{@link\s+([\w.#]+)[^}]*\}/g,function(m,n){var t=resolve(n,ctx);return t?link(t,n):"<code>"+n+"</code>";});
    h=h.replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>").replace(/(^|[^*])\*([^*\s][^*]*)\*/g,"$1<i>$2</i>");
    h=h.replace(/\[([^\]]+)\]\(((?:https?:\/\/|#|\.{0,2}\/)[^)\s]*)\)/g,'<a href="$2" rel="noopener">$1</a>');
    return h;}).join("");}
function md(text,ctx){if(!text)return "";var out=[],lines=String(text).split("\n"),i=0,para=[],list=[];
  function flush(){if(para.length){out.push("<p>"+inline(para.join(" "),ctx)+"</p>");para=[];}if(list.length){out.push("<ul>"+list.map(function(x){return "<li>"+inline(x,ctx)+"</li>";}).join("")+"</ul>");list=[];}}
  while(i<lines.length){var l=lines[i];
    if(/^\s*```/.test(l)){flush();var lang=l.trim().slice(3).trim(),buf=[];i++;while(i<lines.length&&!/^\s*```/.test(lines[i])){buf.push(lines[i]);i++;}i++;out.push(lang==="mermaid"?'<pre class="mermaid-src"><code>'+esc(buf.join("\n"))+"</code></pre>":"<pre><code>"+hl(buf.join("\n"))+"</code></pre>");continue;}
    if(/^\s*#{2,3}\s+/.test(l)){flush();var lvl=l.trim().indexOf(" ");out.push("<h"+(lvl+1)+">"+inline(l.replace(/^\s*#+\s+/,""),ctx)+"</h"+(lvl+1)+">");i++;continue;}
    if(/^\s*>>>/.test(l)){flush();var b2=[];while(i<lines.length&&lines[i].trim()){b2.push(lines[i]);i++;}out.push("<pre><code>"+hl(b2.join("\n"))+"</code></pre>");continue;}
    if(/^\s*[-*+]\s+/.test(l)){if(para.length){out.push("<p>"+inline(para.join(" "),ctx)+"</p>");para=[];}list.push(l.replace(/^\s*[-*+]\s+/,""));i++;continue;}
    if(/^\s*#{1,4}\s+/.test(l)){flush();out.push("<h5>"+inline(l.replace(/^\s*#+\s+/,""),ctx)+"</h5>");i++;continue;}
    if(!l.trim()){flush();i++;continue;}
    if(list.length&&/^\s+/.test(l)){list[list.length-1]+=" "+l.trim();i++;continue;}
    para.push(l.trim());i++;}
  flush();return out.join("");}
function summary(e){var s=(e.doc&&e.doc.summary)||"";return s.length>D.summary_max?s.slice(0,D.summary_max).replace(/\s+\S*$/,"")+"...":s;}
function children(e,kinds){return (e.members||[]).map(function(u){return E[u];}).filter(function(x){return x&&(!kinds||kinds.indexOf(x.kind)>=0);});}
function descendants(uid){var r=[],st=(E[uid].members||[]).slice().reverse();while(st.length){var u=st.pop();var x=E[u];if(!x)continue;r.push(x);st=st.concat((x.members||[]).slice().reverse());}return r;}
function cov(uid){var c=(D.coverage.by_module||{})[uid];return c?c.percent:100;}
function bar(p){return '<div class="bar" title="'+p+'%"><i style="width:'+p+'%"></i></div>';}

function renderTree(filter,active){var groups={};D.modules.forEach(function(u){var e=E[u];var dir=e.file.indexOf("/")>=0?e.file.slice(0,e.file.lastIndexOf("/")):".";(groups[dir]=groups[dir]||[]).push(e);});
  var f=(filter||"").toLowerCase(),h=[];
  Object.keys(groups).sort().forEach(function(dir){var items=groups[dir].filter(function(e){return !f||(e.display+" "+e.file).toLowerCase().indexOf(f)>=0;});if(!items.length)return;
    h.push("<h4>"+esc(dir)+"</h4>");
    items.forEach(function(e){h.push('<a href="'+href(e)+'" class="'+(e.uid===active?"active":"")+'" title="'+esc(e.file)+'">'+esc(e.display.split(/[./]/).pop()||e.display)+'</a>');
      if(e.uid===active){h.push('<div class="sub">');children(e).forEach(function(c){if(DATA.indexOf(c.kind)<0)h.push('<a href="'+href(c)+'">'+esc(c.name)+'</a>');});h.push("</div>");}});});
  document.getElementById("tree").innerHTML=h.join("")||'<p class="muted">No modules match.</p>';}

function paramsTable(e){var doc=e.doc||{},rows=[];if(CLASS.indexOf(e.kind)>=0&&(e.modifiers||[]).indexOf("dataclass")>=0&&!(doc.params||[]).length)return "";var dp={};(doc.params||[]).forEach(function(p){dp[p.name.replace(/^[*$&]+/,"")]=p;});
  (e.params||[]).forEach(function(p){if(!p.name)return;var d=dp[p.name.replace(/^[*$&]+/,"")]||{};rows.push([p.name,p.annotation||d.type||"",p.default||d.default||"",d.description||""]);});
  if(!(e.params||[]).length)(doc.params||[]).forEach(function(d){rows.push([d.name,d.type,d.default,d.description]);});
  if(!rows.length)return "";
  return "<table><tr><th>Parameter</th><th>Type</th><th>Default</th><th>Description</th></tr>"+rows.map(function(r){return "<tr><td><code>"+esc(r[0])+"</code></td><td>"+(r[1]?"<code>"+esc(r[1])+"</code>":"")+"</td><td>"+(r[2]?"<code>"+esc(r[2])+"</code>":"")+"</td><td>"+inline(r[3]||"",e.file)+"</td></tr>";}).join("")+"</table>";}

function docBlock(e){var d=e.doc||{},h=[];
  if(d.deprecated)h.push('<div class="note deprecated"><b>Deprecated:</b> '+inline(d.deprecated,e.file)+"</div>");
  if(d.summary)h.push(md(d.summary,e.file));if(d.description)h.push(md(d.description,e.file));
  if(CALL.indexOf(e.kind)>=0||CLASS.indexOf(e.kind)>=0)h.push(paramsTable(e));
  var rt=(d.returns&&d.returns.type)||e.returns;if(d.returns||(CALL.indexOf(e.kind)>=0&&rt&&rt!=="None"&&rt!=="void"&&e.kind!=="constructor"))h.push("<p><b>Returns:</b> "+(rt?"<code>"+esc(rt)+"</code> ":"")+inline((d.returns&&d.returns.description)||"",e.file)+"</p>");
  if(d.yields)h.push("<p><b>Yields:</b> "+(d.yields.type?"<code>"+esc(d.yields.type)+"</code> ":"")+inline(d.yields.description||"",e.file)+"</p>");
  var rs=(d.raises||[]).slice(),seen={};rs.forEach(function(r){seen[(r.name||"").split(".").pop()]=1;});(e.inferred_raises||[]).forEach(function(n){if(!seen[n])rs.push({name:n,description:"(raised in the body, not documented)"});});
  if(rs.length)h.push("<p><b>Raises</b></p><ul>"+rs.map(function(r){var t=r.name?resolve(r.name,e.file):null;return "<li>"+(r.name?(t?link(t,r.name):"<code>"+esc(r.name)+"</code>")+": ":"")+inline(r.description||"",e.file)+"</li>";}).join("")+"</ul>");
  (d.examples||[]).forEach(function(x){h.push("<p><b>Example</b></p><pre><code>"+hl(x)+"</code></pre>");});
  (d.notes||[]).forEach(function(n){h.push('<div class="note '+esc(String(n[0]).toLowerCase())+'"><b>'+esc(n[0])+":</b> "+md(n[1],e.file)+"</div>");});
  if(d.since)h.push('<p class="muted">Since '+esc(d.since)+"</p>");
  if((d.see_also||[]).length)h.push('<p class="refs"><b>See also:</b> '+d.see_also.map(function(s){var t=resolve(s,e.file);return t?link(t,s):"<code>"+esc(s)+"</code>";}).join(", ")+"</p>");
  if((e.calls||[]).length)h.push('<p class="refs"><b>Calls:</b> '+e.calls.map(linkUid).join(", ")+"</p>");
  if((e.called_by||[]).length)h.push('<p class="refs"><b>Called by:</b> '+e.called_by.map(linkUid).join(", ")+"</p>");
  return h.join("");}

function entityCard(e,level){var b=['<span class="badge kind">'+esc(e.kind)+"</span>"];(e.modifiers||[]).forEach(function(m){b.push('<span class="badge">'+esc(m)+"</span>");});
  if(e.visibility!=="public")b.push('<span class="badge priv">'+esc(e.visibility)+"</span>");if(e.doc&&e.doc.deprecated)b.push('<span class="badge dep">deprecated</span>');
  var tag="h"+Math.min(level,5),h=['<section class="card" id="'+esc("e:"+e.qualname)+'">'];
  h.push("<"+tag+'><a href="'+href(e)+'">'+esc(e.qualname)+"</a></"+tag+'><div class="badges">'+b.join("")+'<span class="src">'+esc(e.file)+":"+e.line+"</span></div>");
  if((e.decorators||[]).length)h.push('<div class="refs">'+e.decorators.map(function(d){return "<code>@"+esc(d)+"</code>";}).join(" ")+"</div>");
  if(e.signature)h.push("<pre><code>"+hl(e.signature)+"</code></pre>");
  if(CLASS.indexOf(e.kind)>=0){if((e.bases||[]).length)h.push('<p class="refs"><b>Bases:</b> '+e.bases.map(function(bn){var t=(e.base_uids||[]).map(function(u){return E[u];}).filter(function(x){return x&&x.name===bn.replace(/\[.*\]$/,"").split(".").pop();})[0];return t?link(t,bn):"<code>"+esc(bn)+"</code>";}).join(", ")+"</p>");
    if((e.subclasses||[]).length)h.push('<p class="refs"><b>Subclasses:</b> '+e.subclasses.map(linkUid).join(", ")+"</p>");}
  h.push(docBlock(e));
  if(CLASS.indexOf(e.kind)>=0){var ms=children(e),data=ms.filter(function(m){return DATA.indexOf(m.kind)>=0;});
    if(data.length){var da={};((e.doc||{}).attributes||[]).forEach(function(a){da[a.name]=a;});
      h.push("<table><tr><th>Attribute</th><th>Type</th><th>Default</th><th>Description</th></tr>"+data.map(function(a){var x=da[a.name]||{};return "<tr><td><code>"+esc(a.name)+"</code></td><td>"+((a.returns||x.type)?"<code>"+esc(a.returns||x.type)+"</code>":"")+"</td><td>"+(a.value?"<code>"+esc(a.value.length>60?a.value.slice(0,57)+"...":a.value)+"</code>":"")+"</td><td>"+inline((a.doc&&a.doc.summary)||x.description||"",e.file)+"</td></tr>";}).join("")+"</table>");}
    ms.filter(function(m){return DATA.indexOf(m.kind)<0;}).forEach(function(m){h.push(entityCard(m,level+1));});}
  h.push("</section>");return h.join("");}

function home(){var c=D.coverage.overall||{},m=D.meta||{},h=[];
  h.push("<h2>"+esc(D.project)+" API Reference</h2><p class=\"muted\">Generated offline by readmenator from source: signatures are extracted, documentation is parsed from Google, NumPy, reST, Javadoc / JSDoc / Doxygen, C# XML, and Rustdoc comments.</p>");
  h.push('<div class="tiles"><div class="tile"><b>'+(m.modules||0)+'</b><span>modules</span></div><div class="tile"><b>'+(m.entities||0)+'</b><span>entities</span></div><div class="tile"><b>'+(c.percent==null?100:c.percent)+'%</b><span>documented ('+(c.documented||0)+"/"+(c.total||0)+')</span></div><div class="tile"><b>'+D.warning_total+'</b><span>doc warnings</span></div></div>');
  var groups={};D.modules.forEach(function(u){var e=E[u];var dir=e.file.indexOf("/")>=0?e.file.slice(0,e.file.lastIndexOf("/")):".";(groups[dir]=groups[dir]||[]).push(e);});
  Object.keys(groups).sort().forEach(function(dir){h.push("<h3><code>"+esc(dir)+"</code></h3><table><tr><th>Module</th><th>Summary</th><th>Coverage</th></tr>");
    groups[dir].forEach(function(e){h.push("<tr><td>"+link(e)+"</td><td>"+inline(summary(e),e.file)+"</td><td>"+bar(cov(e.uid))+'<span class="muted">'+cov(e.uid)+"%</span></td></tr>");});h.push("</table>");});
  return h.join("");}

function modulePage(uid){var e=E[uid];if(!e)return "<p>Unknown module.</p>";var h=[];
  h.push("<h2><code>"+esc(e.display)+"</code></h2><div class=\"badges\"><span class=\"badge kind\">module</span><span class=\"badge\">"+esc(e.language)+'</span><span class="src">'+esc(e.file)+"</span><span class=\"badge\">coverage "+cov(uid)+"%</span></div>");
  h.push(docBlock(e));var top=children(e),order=CLASS.concat(["function","macro","constant","variable"]);
  var secs=order.map(function(k){return [TITLES[k]||k,top.filter(function(x){return x.kind===k;})];}).filter(function(s){return s[1].length;});
  var other=top.filter(function(x){return order.indexOf(x.kind)<0;});if(other.length)secs.push(["Other Members",other]);
  if(secs.length)h.push('<div class="card"><b>Contents</b>'+secs.map(function(s){return '<p class="refs"><b>'+s[0]+":</b> "+s[1].map(function(x){return '<a href="'+href(x)+'">'+esc(x.name)+"</a>";}).join(", ")+"</p>";}).join("")+"</div>");
  secs.forEach(function(s){h.push("<h3>"+s[0]+"</h3>");s[1].forEach(function(x){h.push(DATA.indexOf(x.kind)>=0?'<section class="card" id="'+esc("e:"+x.qualname)+'"><h4>'+esc(x.qualname)+'</h4><div class="badges"><span class="badge kind">'+esc(x.kind)+'</span><span class="src">'+esc(x.file)+":"+x.line+"</span></div><pre><code>"+hl(x.signature)+"</code></pre>"+docBlock(x)+"</section>":entityCard(x,4));});});
  return h.join("");}

function hierarchy(){var types=D.entities.filter(function(e){return CLASS.indexOf(e.kind)>=0;});if(!types.length)return "<h2>Class Hierarchy</h2><p>No class-like types.</p>";
  var seen={};function walk(e){if(seen[e.uid])return "";seen[e.uid]=1;var ext=(e.bases||[]).filter(function(b){return !(e.base_uids||[]).some(function(u){return E[u]&&E[u].name===b.replace(/\[.*\]$/,"").split(".").pop();});});
    return "<li>"+link(e)+' <span class="muted">'+esc(e.kind)+" in "+esc(modName(e))+(ext.length?" ("+esc(ext.join(", "))+")":"")+"</span>"+((e.subclasses||[]).length?'<ul class="tree">'+e.subclasses.map(function(u){return E[u]?walk(E[u]):"";}).join("")+"</ul>":"")+"</li>";}
  var roots=types.filter(function(e){return !(e.base_uids||[]).length;}).sort(function(a,b){return a.name.toLowerCase()<b.name.toLowerCase()?-1:1;});
  var h='<h2>Class Hierarchy</h2><ul class="tree">'+roots.map(walk).join("")+types.map(function(e){return seen[e.uid]?"":walk(e);}).join("")+"</ul>";return h;}

function genIndex(){var items=D.entities.filter(function(e){return e.kind!=="module";}).sort(function(a,b){var x=a.name.replace(/^[_#$]+/,"").toLowerCase(),y=b.name.replace(/^[_#$]+/,"").toLowerCase();return x<y?-1:x>y?1:(a.uid<b.uid?-1:1);});
  var L={};items.forEach(function(e){var c=(e.name.replace(/^[_#$]+/,"")[0]||"#").toUpperCase();if(!/[A-Z]/.test(c))c="#";(L[c]=L[c]||[]).push(e);});
  var keys=Object.keys(L).sort();return "<h2>General Index</h2><p class=\"letters\">"+keys.map(function(k){return '<a href="#/index/'+encodeURIComponent(k)+'">'+esc(k)+"</a>";}).join("")+"</p>"+keys.map(function(k){return '<h3 id="'+esc("L:"+k)+'">'+esc(k)+"</h3><ul>"+L[k].map(function(e){return "<li>"+link(e,e.name)+' <span class="muted">'+esc(e.kind)+(e.qualname.indexOf(".")>=0?" of "+esc(e.qualname.slice(0,e.qualname.lastIndexOf("."))):"")+" in "+esc(modName(e))+"</span></li>";}).join("")+"</ul>";}).join("");}

function flowsPage(){return '<h2>Architecture and Execution Flows</h2><p class="muted">Computed from the source and laid out offline. Click any box for its signature, docs and files; Ctrl+wheel zooms, drag pans.</p><div id="fv-host"></div>';}
function coveragePage(){var c=D.coverage,h=["<h2>Documentation Coverage</h2>"];var o=c.overall||{};
  h.push("<p>Overall <b>"+(o.percent==null?100:o.percent)+"%</b> ("+(o.documented||0)+" of "+(o.total||0)+" public modules, types, and callables).</p>"+bar(o.percent==null?100:o.percent));
  h.push("<h3>By kind</h3><table><tr><th>Kind</th><th>Documented</th><th>Total</th><th>Coverage</th></tr>"+Object.keys(c.by_kind||{}).map(function(k){var s=c.by_kind[k];return "<tr><td>"+esc(k)+"</td><td>"+s.documented+"</td><td>"+s.total+"</td><td>"+s.percent+"%</td></tr>";}).join("")+"</table>");
  var mods=Object.keys(c.by_module||{}).sort(function(a,b){return c.by_module[a].percent-c.by_module[b].percent||(a<b?-1:1);});
  h.push("<h3>By module</h3><table><tr><th>Module</th><th>Documented</th><th>Total</th><th>Coverage</th></tr>"+mods.map(function(u){var s=c.by_module[u];return "<tr><td>"+(E[u]?link(E[u]):esc(u))+"</td><td>"+s.documented+"</td><td>"+s.total+"</td><td>"+bar(s.percent)+s.percent+"%</td></tr>";}).join("")+"</table>");
  h.push("<h3>Warnings ("+D.warning_total+")</h3><p class=\"muted\">DOC001 undocumented, DOC002 parameter not documented, DOC003 documented parameter missing from the signature, DOC004 return not documented, DOC005 raised exception not documented.</p><ul>"+D.warnings.map(function(w){var e=E[w.uid];return "<li><code>"+esc(w.code)+"</code> "+(e?link(e):"")+' <span class="muted">'+esc(w.file)+":"+w.line+"</span> "+esc(w.message)+"</li>";}).join("")+"</ul>");
  return h.join("");}

var main=document.getElementById("main");
function route(){var h=decodeURIComponent(location.hash.replace(/^#\/?/,"")),active="",html,focus="";
  if(h.indexOf("m/")===0){var rest=h.slice(2),uid=null;D.modules.forEach(function(u){if((rest===u||rest.indexOf(u+"/")===0)&&(!uid||u.length>uid.length))uid=u;});
    if(uid){active=uid;html=modulePage(uid);focus=rest.length>uid.length?"e:"+rest.slice(uid.length+1):"";}else html="<p>Unknown module.</p>";}
  else if(h==="flows"||h==="architecture")html=flowsPage();else if(h==="hierarchy")html=hierarchy();else if(h.indexOf("index")===0){html=genIndex();focus=h.length>6?"L:"+h.slice(6):"";}else if(h==="coverage")html=coveragePage();else html=home();
  main.innerHTML=html;renderTree(document.getElementById("filter").value,active);
  var fh=document.getElementById("fv-host");if(fh&&window.ReadmenatorFlows)window.ReadmenatorFlows.mount(fh,D.flows||[],{apiHref:"index.html"});
  if(focus){var el=document.getElementById(focus);if(el){el.scrollIntoView({block:"start"});window.scrollBy(0,-64);el.style.outline="2px solid var(--accent)";}}else window.scrollTo(0,0);}
window.addEventListener("hashchange",route);
document.getElementById("filter").addEventListener("input",function(){var h=decodeURIComponent(location.hash);var a=D.modules.filter(function(u){return h.indexOf("#/m/"+u)===0;})[0]||"";renderTree(this.value,a);});
var q=document.getElementById("q"),res=document.getElementById("results"),sel=0,hits=[];
function search(){var t=q.value.trim().toLowerCase();if(!t){res.style.display="none";return;}
  var scored=[];D.entities.forEach(function(e){var n=(e.kind==="module"?e.display:e.name).toLowerCase(),qn=e.qualname.toLowerCase(),s=0;
    if(n===t)s=100;else if(n.indexOf(t)===0)s=80;else if(qn.indexOf(t)>=0)s=60;else if(n.indexOf(t)>=0)s=50;else if(((e.doc&&e.doc.summary)||"").toLowerCase().indexOf(t)>=0)s=20;
    if(s){if(CLASS.indexOf(e.kind)>=0||e.kind==="module")s+=5;scored.push([s,e]);}});
  scored.sort(function(a,b){return b[0]-a[0]||(a[1].qualname<b[1].qualname?-1:1);});hits=scored.slice(0,40).map(function(x){return x[1];});sel=0;
  res.innerHTML=hits.map(function(e,i){return '<a href="'+href(e)+'" class="'+(i===0?"sel":"")+'"><code>'+esc(e.kind==="module"?e.display:e.qualname)+"</code> <small>"+esc(e.kind)+" &middot; "+esc(modName(e))+"</small><br><small>"+esc(summary(e))+"</small></a>";}).join("")||'<a class="muted">No results</a>';
  res.style.display="block";}
q.addEventListener("input",search);
q.addEventListener("keydown",function(ev){var links=res.querySelectorAll("a");if(ev.key==="ArrowDown"||ev.key==="ArrowUp"){ev.preventDefault();if(!links.length)return;links[sel].classList.remove("sel");sel=(sel+(ev.key==="ArrowDown"?1:links.length-1))%links.length;links[sel].classList.add("sel");links[sel].scrollIntoView({block:"nearest"});}
  else if(ev.key==="Enter"&&hits[sel]){location.hash=href(hits[sel]).slice(1);res.style.display="none";q.blur();}else if(ev.key==="Escape"){res.style.display="none";q.blur();}});
res.addEventListener("click",function(){res.style.display="none";});
document.addEventListener("click",function(ev){if(!ev.target.closest(".search"))res.style.display="none";});
document.addEventListener("keydown",function(ev){if(ev.key==="/"&&document.activeElement!==q&&document.activeElement.tagName!=="INPUT"){ev.preventDefault();q.focus();}});
var root=document.documentElement;
try{var saved=localStorage.getItem("readmenator-theme");if(saved)root.setAttribute("data-theme",saved);}catch(err){}
document.getElementById("theme").addEventListener("click",function(){var cur=root.getAttribute("data-theme")||(matchMedia("(prefers-color-scheme: light)").matches?"light":"dark");var nxt=cur==="light"?"dark":"light";root.setAttribute("data-theme",nxt);try{localStorage.setItem("readmenator-theme",nxt);}catch(err){}route();});
document.getElementById("title").textContent=D.project+" API";
route();
})();
</script>
</body>
</html>
"""
