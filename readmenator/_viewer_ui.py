"""Shared Config button + modal for maps/explorer pages.

Every maps-family page (gallery index, force-graph, edge bundles,
flows) embeds the same ``Config`` control: a button that opens a modal
with the viewer subset of ``readmenator.toml``. ``Apply`` updates the
live view without a full page reload (only the affected segment is
re-rendered), persists the choice to ``localStorage``, and offers a
``Copy TOML`` action so the choice can be persisted back into
``readmenator.toml`` for the next rebuild.

Pages expose a hook instead of sharing internals:
``window.ReadmenatorViewerApply(patch)`` applies a ``{key: value}``
patch live and returns the list of modal keys it handled live
(``[]`` when none). Apply diffs the form against its opening values,
applies only what changed, and reports "Live: ..." vs "Needs rebuild:
..." per key. Reset asks for confirmation before clearing overrides.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List

VIEWER_SCHEMA: List[Dict[str, Any]] = [
    {"key": "theme", "label": "Theme", "type": "select", "section": "viewer",
     "options": ["dark", "light"],
     "help": "Page color scheme. Applies instantly."},
    {"key": "preset", "label": "Map preset", "type": "select", "section": "viewer",
     "options": ["classic", "flow", "blueprint", "editorial"],
     "help": "Gallery map style. Needs rebuild for system maps."},
    {"key": "motion_enabled", "label": "Motion", "type": "bool", "section": "viewer",
     "help": "Finite animations. Honors prefers-reduced-motion."},
    {"key": "mode", "label": "Default view", "type": "select", "section": "viewer",
     "options": ["2d", "3d"],
     "help": "Explorer view used on first load."},
    {"key": "label_top_n", "label": "Labels (top N)", "type": "int", "section": "viewer",
     "min": 0, "max": 200,
     "help": "How many top-ranked files always show names."},
    {"key": "label_zoom", "label": "Label zoom", "type": "number", "section": "viewer",
     "min": 0.5, "max": 4.0, "step": 0.1,
     "help": "Zoom level from which all labels appear."},
    {"key": "charge", "label": "Repulsion", "type": "int", "section": "viewer",
     "min": -1000, "max": 0,
     "help": "Force-graph node repulsion. Reheats physics live."},
    {"key": "link_distance", "label": "Link distance", "type": "int", "section": "viewer",
     "min": 20, "max": 400,
     "help": "Target edge length. Reheats physics live."},
    {"key": "link_strength", "label": "Link strength", "type": "number", "section": "viewer",
     "min": 0.0, "max": 1.0, "step": 0.05,
     "help": "Edge stiffness. Reheats physics live."},
    {"key": "hulls_enabled", "label": "Group halos", "type": "bool", "section": "viewer",
     "help": "Community halo overlays around file groups."},
    {"key": "particles", "label": "Flow particles", "type": "int", "section": "viewer",
     "min": 0, "max": 12,
     "help": "Particles on highlighted edges."},
    {"key": "bundle_beta", "label": "Bundle strength", "type": "number", "section": "viewer",
     "min": 0.0, "max": 1.0, "step": 0.05,
     "help": "Edge bundling pull toward the hierarchy (bundles page)."},
    {"key": "html_style", "label": "HTML style", "type": "select", "section": "viewer",
     "options": ["dark", "light"],
     "help": "Default style for freshly generated pages."},
    {"key": "name", "label": "Project name", "type": "text", "section": "branding",
     "help": "Page titles and hero. Needs rebuild."},
    {"key": "author", "label": "Author", "type": "text", "section": "branding",
     "help": "Credited in the hero and footer. Needs rebuild."},
    {"key": "description", "label": "Description", "type": "text", "section": "branding",
     "help": "One-line project summary in the hero. Needs rebuild."},
    {"key": "github_url", "label": "GitHub URL", "type": "text", "section": "branding",
     "help": "Absolute http(s) link. Footer icon. Needs rebuild."},
    {"key": "pages_url", "label": "Pages URL", "type": "text", "section": "branding",
     "help": "Absolute http(s) link to the published site. Footer icon. Needs rebuild."},
    {"key": "home_url", "label": "Home URL", "type": "text", "section": "branding",
     "help": "Where the maps home icon points. Footer icon. Needs rebuild."},
    {"key": "logo_url", "label": "Logo URL", "type": "text", "section": "branding",
     "help": "Absolute http(s) brand image shown in the hero. Needs rebuild."},
    {"key": "accent", "label": "Accent color", "type": "color", "section": "branding",
     "help": "Primary highlight color (#rrggbb). Applies instantly."},
    {"key": "accent2", "label": "Accent 2", "type": "color", "section": "branding",
     "help": "Secondary highlight color (#rrggbb). Applies instantly."},
    {"key": "sourceview_max_files", "label": "View sources (files)", "type": "int", "section": "maps",
     "min": 0, "max": 100000,
     "help": "Files embedding source for the View button. Needs rebuild."},
    {"key": "sourceview_max_total_chars", "label": "View sources (chars)", "type": "int", "section": "maps",
     "min": 0, "max": 1000000000,
     "help": "Total char budget across embedded sources. Needs rebuild."},
    {"key": "readme_heading", "label": "README heading", "type": "text", "section": "messages",
     "help": "README injection heading. Empty = built-in. Needs rebuild."},
    {"key": "readme_intro", "label": "README intro", "type": "textarea", "section": "messages",
     "help": "Opening paragraph of the README section. Needs rebuild."},
    {"key": "readme_agents_line", "label": "README agents line", "type": "text", "section": "messages",
     "help": "Closing 'AI agents' guidance line. Needs rebuild."},
    {"key": "readme_developers_line", "label": "README developers line", "type": "text", "section": "messages",
     "help": "Closing 'Developers' guidance line. Needs rebuild."},
    {"key": "readme_regen_command", "label": "Regen command", "type": "text", "section": "messages",
     "help": "Rebuild command shown in injections. Needs rebuild."},
    {"key": "agent_heading", "label": "Agent heading", "type": "text", "section": "messages",
     "help": "Agent files injection heading. Needs rebuild."},
    {"key": "agent_intro", "label": "Agent intro", "type": "textarea", "section": "messages",
     "help": "Opening paragraph of agent injections. Needs rebuild."},
    {"key": "agent_extra", "label": "Agent extra", "type": "textarea", "section": "messages",
     "help": "Extra project instructions appended to agent files. Needs rebuild."},
    {"key": "folder_notice", "label": "Folder notice", "type": "textarea", "section": "messages",
     "help": "Notice paragraph in generated folder READMEs. Needs rebuild."},
]

VIEWER_MODAL_CSS = r"""
#rm-cfg-scrim{position:fixed;inset:0;z-index:90;background:rgba(2,6,23,.6);opacity:0;pointer-events:none;transition:opacity .2s}
#rm-cfg-scrim.open{opacity:1;pointer-events:auto}
#rm-cfg-modal{position:fixed;z-index:91;top:50%;left:50%;transform:translate(-50%,-50%) scale(.98);width:min(560px,calc(100vw - 32px));max-height:min(82vh,760px);overflow:auto;background:var(--mask,var(--panel,#0b1224));color:var(--ink,var(--text,#f8fafc));border:1px solid var(--accent,#22d3ee);border-radius:14px;padding:18px 20px;box-shadow:0 24px 70px rgba(0,0,0,.5);display:none}
#rm-cfg-modal.open{display:block;transform:translate(-50%,-50%) scale(1)}
#rm-cfg-modal h2{margin:0 0 4px;font-size:16px}
#rm-cfg-modal .rm-cfg-sub{color:var(--muted,#94a3b8);font-size:12px;margin:0 0 12px;line-height:1.6}
#rm-cfg-modal .rm-cfg-row{display:grid;grid-template-columns:150px minmax(0,1fr);gap:10px;align-items:center;padding:7px 0;border-top:1px solid var(--border,var(--line,#1e293b))}
#rm-cfg-modal label{font-size:12px;font-weight:600}
#rm-cfg-modal .rm-cfg-help{font-size:11px;color:var(--muted,#94a3b8);grid-column:1/-1;margin:-4px 0 0}
#rm-cfg-modal input[type="number"],#rm-cfg-modal input[type="text"],#rm-cfg-modal select,#rm-cfg-modal textarea{width:100%;background:var(--canvas,var(--bg,#020617));border:1px solid var(--border,var(--line,#1e293b));border-radius:8px;color:var(--ink,var(--text,#f8fafc));padding:6px 8px;font:inherit;font-size:12px}
#rm-cfg-modal textarea{resize:vertical;min-height:56px;line-height:1.5}
#rm-cfg-modal .rm-cfg-sec{margin:14px 0 2px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted,#94a3b8)}
.rm-home-icon{width:12px;height:12px;flex:none;vertical-align:-1px}
a.home .rm-home-icon{margin-right:5px}
#rm-cfg-modal input[type="checkbox"]{width:18px;height:18px;accent-color:var(--accent,#22d3ee)}
#rm-cfg-modal .rm-cfg-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
#rm-cfg-modal .rm-cfg-actions button{font-size:12px;border-radius:9px;padding:7px 12px;cursor:pointer}
#rm-cfg-status{font-size:11.5px;color:var(--muted,#94a3b8);margin-top:10px;min-height:18px}
@media (prefers-reduced-motion:reduce){#rm-cfg-scrim,#rm-cfg-modal{transition:none}}
"""

VIEWER_MODAL_JS = r"""
(function(){
"use strict";
var LS_KEY="readmenator.viewer.v1";
var SCHEMA=__SCHEMA__;
function defaults(){var d={};try{d=window.__RM_VIEWER__||{};}catch(e){}return d;}
function stored(){try{var raw=localStorage.getItem(LS_KEY);if(raw)return JSON.parse(raw);}catch(e){}return {};}
function save(patch){try{var cur=stored();for(var k in patch)cur[k]=patch[k];localStorage.setItem(LS_KEY,JSON.stringify(cur));}catch(e){}}
function clear(){try{localStorage.removeItem(LS_KEY);}catch(e){}}
function current(){var d=defaults(),s=stored(),out={};for(var i=0;i<SCHEMA.length;i++){var k=SCHEMA[i].key;out[k]=(k in s)?s[k]:d[k];}return out;}
function setTheme(t){try{document.documentElement.setAttribute("data-theme",t);localStorage.setItem("readmenator-theme",t);}catch(e){try{document.documentElement.setAttribute("data-theme",t);}catch(_){}}}
function setAccent(which,val){
  if(!/^#[0-9a-fA-F]{3}([0-9a-fA-F]{3}([0-9a-fA-F]{2})?)?$/.test(String(val||"")))return false;
  try{document.documentElement.style.setProperty(which,val);}catch(e){return false;}
  return true;
}
function num(v,f){var n=parseFloat(v);return isFinite(n)?n:f;}
function applyLive(patch){
  patch=patch||{};var live=[];
  if("theme" in patch||"html_style" in patch){setTheme(patch.theme||patch.html_style||"dark");live.push("theme");}
  if("accent" in patch&&setAccent("--accent",patch.accent))live.push("accent");
  if("accent2" in patch&&setAccent("--accent2",patch.accent2))live.push("accent2");
  try{
    if(typeof window.ReadmenatorViewerApply==="function"){
      var r=window.ReadmenatorViewerApply(patch);
      if(r===true){if(live.indexOf("view")<0)live.push("view");}
      else if(r&&r.length)for(var i=0;i<r.length;i++)if(live.indexOf(r[i])<0)live.push(r[i]);
    }
  }catch(e){if(window.console)console.warn("viewer apply failed",e);}
  return live;
}
function fieldRow(spec,val){
  var row=document.createElement("div");row.className="rm-cfg-row";
  var lab=document.createElement("label");lab.textContent=spec.label;lab.setAttribute("for","rm-cfg-"+spec.key);row.appendChild(lab);
  var input;
  if(spec.type==="bool"){input=document.createElement("input");input.type="checkbox";input.checked=!!val;}
  else if(spec.type==="select"){input=document.createElement("select");(spec.options||[]).forEach(function(o){var op=document.createElement("option");op.value=o;op.textContent=o;if(String(o)===String(val))op.selected=true;input.appendChild(op);});}
  else if(spec.type==="color"){input=document.createElement("input");input.type="color";try{input.value=/^#[0-9a-fA-F]{6}$/.test(String(val||""))?val:"#22d3ee";}catch(e){input.value="#22d3ee";}}
  else if(spec.type==="text"){input=document.createElement("input");input.type="text";input.value=(val==null?"":String(val));if(spec.key.indexOf("_url")>=0)input.placeholder="https:"+"//your-site.example/…";}
  else if(spec.type==="textarea"){input=document.createElement("textarea");input.rows=3;input.value=(val==null?"":String(val));}
  else{input=document.createElement("input");input.type="number";input.value=val;if(spec.min!=null)input.min=spec.min;if(spec.max!=null)input.max=spec.max;if(spec.step)input.step=spec.step;}
  input.id="rm-cfg-"+spec.key;input.dataset.key=spec.key;row.appendChild(input);
  if(spec.help){var h=document.createElement("p");h.className="rm-cfg-help";h.textContent=spec.help;row.appendChild(h);}
  return row;
}
function renderForm(){
  var form=document.getElementById("rm-cfg-form");
  if(!form)return {};
  while(form.firstChild)form.removeChild(form.firstChild);
  var cur=current(),lastSec="";
  SCHEMA.forEach(function(spec){
    var sec=spec.section||"viewer";
    if(sec!==lastSec){lastSec=sec;var hd=document.createElement("h3");hd.className="rm-cfg-sec";hd.textContent=sec.charAt(0).toUpperCase()+sec.slice(1);form.appendChild(hd);}
    form.appendChild(fieldRow(spec,cur[spec.key]));
  });
  window.__rmCfgBase__=cur;
  return cur;
}
function openModal(){
  var scrim=document.getElementById("rm-cfg-scrim"),modal=document.getElementById("rm-cfg-modal");
  if(!scrim||!modal)return;
  renderForm();
  scrim.classList.add("open");modal.classList.add("open");modal.setAttribute("aria-hidden","false");
  var first=document.getElementById("rm-cfg-form").querySelector("select,input,textarea");if(first)first.focus();
}
function closeModal(){var scrim=document.getElementById("rm-cfg-scrim"),modal=document.getElementById("rm-cfg-modal");if(scrim)scrim.classList.remove("open");if(modal){modal.classList.remove("open");modal.setAttribute("aria-hidden","true");}}
function readForm(){
  var patch={},form=document.getElementById("rm-cfg-form");
  var els=form.querySelectorAll("[data-key]");
  for(var i=0;i<els.length;i++){var el=els[i],k=el.dataset.key,spec=null;
    for(var j=0;j<SCHEMA.length;j++)if(SCHEMA[j].key===k)spec=SCHEMA[j];
    if(!spec)continue;
    if(spec.type==="bool")patch[k]=!!el.checked;
    else if(spec.type==="int")patch[k]=Math.round(num(el.value,0));
    else if(spec.type==="number")patch[k]=num(el.value,0);
    else patch[k]=el.value;
  }
  return patch;
}
function toToml(patch){
  var sections={},order=[];
  SCHEMA.forEach(function(spec){
    if(!(spec.key in patch))return;
    var sec=spec.section||"viewer";
    if(!(sec in sections)){sections[sec]=[];order.push(sec);}
    var v=patch[spec.key],lit;
    if(typeof v==="boolean")lit=v?"true":"false";
    else if(typeof v==="number")lit=String(v);
    else lit='"'+String(v).replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n").replace(/\r/g,"\\r").replace(/\t/g,"\\t")+'"';
    sections[sec].push(spec.key+" = "+lit);
  });
  var lines=[];
  order.forEach(function(sec){lines.push("["+sec+"]");lines.push(sections[sec].join("\n"));lines.push("");});
  return lines.join("\n").replace(/\n$/,"");
}
function status(msg){var s=document.getElementById("rm-cfg-status");if(s)s.textContent=msg;}
function boot(){
  document.querySelectorAll("[data-rm-config]").forEach(function(btn){
    if(btn.__rmBound)return;btn.__rmBound=true;
    btn.addEventListener("click",openModal);
  });
  var scrim=document.getElementById("rm-cfg-scrim");
  if(scrim)scrim.addEventListener("click",closeModal);
  var close=document.getElementById("rm-cfg-close");
  if(close)close.addEventListener("click",closeModal);
  document.addEventListener("keydown",function(e){if(e.key==="Escape")closeModal();});
  var apply=document.getElementById("rm-cfg-apply");
  if(apply)apply.addEventListener("click",function(){
    var patch=readForm(),base=window.__rmCfgBase__||{},dirty={};
    for(var k in patch)if(patch[k]!==base[k])dirty[k]=patch[k];
    save(patch);
    var live=applyLive(dirty);
    var pending=Object.keys(dirty).filter(function(k){return live.indexOf(k)<0;});
    var msg="";
    if(live.length)msg+="Live: "+live.join(", ")+". ";
    if(pending.length)msg+="Needs rebuild: "+pending.join(", ")+".";
    status(msg||"No changes.");
    window.__rmCfgBase__=patch;
  });
  var reset=document.getElementById("rm-cfg-reset");
  if(reset)reset.addEventListener("click",function(){
    if(!window.confirm("Clear local Config overrides and restore last-rebuild defaults?"))return;
    clear();
    renderForm();
    applyLive(current());
    status("Local overrides cleared. Last-rebuild defaults restored.");
  });
  var copy=document.getElementById("rm-cfg-copy");
  if(copy)copy.addEventListener("click",function(){
    var toml=toToml(readForm());
    function done(){status("Copied TOML sections. Paste them into readmenator.toml and rebuild to persist.");}
    try{
      if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(toml).then(done,function(){status(toml);});
      else status(toml);
    }catch(e){status(toml);}
  });
  var init=stored();
  if(init&&Object.keys(init).length)applyLive(init);
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
})();
"""


def viewer_json(config: Any) -> str:
    """Serialize the viewer + branding subset of Config for embedding in pages.

    Args:
        config: Effective configuration.

    Returns:
        JSON object string with viewer and branding keys (flat namespace).
    """
    from readmenator._project_config import (
        BRANDING_TOML_KEYS,
        MAPS_TOML_KEYS,
        MESSAGES_TOML_KEYS,
        TOML_MAP,
        VIEWER_TOML_KEYS,
    )

    out: Dict[str, Any] = {}
    for section, toml_keys in (
        ("viewer", VIEWER_TOML_KEYS),
        ("branding", BRANDING_TOML_KEYS),
        ("messages", MESSAGES_TOML_KEYS),
        ("maps", MAPS_TOML_KEYS),
    ):
        for toml_key in toml_keys:
            field_name = TOML_MAP[(section, toml_key)]
            value = getattr(config, field_name, None)
            if isinstance(value, tuple):
                value = list(value)
            out[toml_key] = value
    return json.dumps(out, sort_keys=True).replace("<", "\\u003c")


HOUSE_SVG = (
    '<svg class="rm-home-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M12 3l9 8h-3v9h-4v-6h-4v6H6v-9H3z"/></svg>'
)

GLOBE_SVG = (
    '<svg class="rm-home-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<g fill="none" stroke="currentColor" stroke-width="1.8">'
    '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c3.2 3.6 3.2 13.4 0 17M12 3.5c-3.2 3.6-3.2 13.4 0 17"/>'
    "</g></svg>"
)


def branding_style(config: Any) -> str:
    """Return a style element overriding accent colors from branding.

    Args:
        config: Effective configuration.

    Returns:
        Style element, or "" when no valid accent color is configured.
    """
    from readmenator._project_config import branding_css

    css = branding_css(config)
    return "<style>" + css + "</style>" if css else ""


def home_anchor(config: Any) -> str:
    """Return a home icon link to the configured maps home URL.

    Args:
        config: Effective configuration.

    Returns:
        Anchor fragment, or "" when branding.home_url is not an http(s) link.
    """
    import html as _html

    from readmenator._project_config import safe_url

    home = safe_url(getattr(config, "PROJECT_HOME_URL", ""))
    if not home:
        return ""
    return (
        '<a class="home" href="' + _html.escape(home, quote=True) + '" target="_blank" '
        'rel="noopener" title="Project home (readmenator.toml branding.home_url)">'
        + HOUSE_SVG + "<span>Home</span></a>"
    )


def project_links(config: Any) -> List[Dict[str, str]]:
    """Return validated project link pills for footers and heroes.

    Args:
        config: Effective configuration.

    Returns:
        List of {"label": ..., "url": ..., "icon": "github"|"globe"|"house"}.
    """
    from readmenator._project_config import safe_url

    links: List[Dict[str, str]] = []
    github = safe_url(getattr(config, "PROJECT_GITHUB_URL", ""))
    if github:
        links.append({"label": "Repo", "url": github, "icon": "github"})
    pages = safe_url(getattr(config, "PROJECT_PAGES_URL", ""))
    if pages:
        links.append({"label": "Site", "url": pages, "icon": "globe"})
    home = safe_url(getattr(config, "PROJECT_HOME_URL", ""))
    if home and home != pages:
        links.append({"label": "Home", "url": home, "icon": "house"})
    return links


def modal_html() -> str:
    """Return the Config modal + scrim markup shared by every page."""
    return (
        '<div id="rm-cfg-scrim"></div>'
        '<div id="rm-cfg-modal" role="dialog" aria-modal="true" '
        'aria-labelledby="rm-cfg-title" aria-hidden="true">'
        "<h2 id=\"rm-cfg-title\">Viewer config</h2>"
        '<p class="rm-cfg-sub">Project view options from readmenator.toml '
        "([viewer], [branding], [maps], [messages]). Apply re-renders only the "
        "affected segment, no full reload. Copy TOML persists the choice "
        "for the next rebuild.</p>"
        '<div id="rm-cfg-form"></div>'
        '<div class="rm-cfg-actions">'
        '<button type="button" id="rm-cfg-apply" title="Apply without reloading">Apply</button>'
        '<button type="button" id="rm-cfg-copy" title="Copy TOML sections to clipboard">Copy TOML</button>'
        '<button type="button" id="rm-cfg-reset" title="Clear local overrides">Reset</button>'
        '<button type="button" id="rm-cfg-close" title="Close ( Esc )">Close</button>'
        "</div>"
        '<div id="rm-cfg-status" role="status" aria-live="polite"></div>'
        "</div>"
    )


def modal_script(config: Any) -> str:
    """Return the modal boot script with schema + viewer defaults injected.

    Args:
        config: Effective configuration.

    Returns:
        Inline script body (without script tags).
    """
    schema = json.dumps(VIEWER_SCHEMA).replace("<", "\\u003c")
    return (
        "window.__RM_VIEWER__=" + viewer_json(config) + ";\n"
        + VIEWER_MODAL_JS.replace("__SCHEMA__", schema)
    )


def config_button_markup() -> str:
    """Return the native Config toolbar button opening the shared modal.

    Deliberately classless so every template styles it exactly like its
    sibling buttons (the gallery pairs it with #theme via CSS).

    Returns:
        Button HTML fragment.
    """
    return (
        '<button type="button" data-rm-config '
        'title="Viewer config (no reload)">Config</button>'
    )
