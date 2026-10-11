"""Component architecture diagrams, token-free by default.

Builds an ``analysis.json`` (metadata, description, files,
methods_index, components with key entities and file methods,
component relations with method-level key edges and call sites)
from the readmenator scan, plus ``graph LR`` Mermaid overviews,
per-component markdown pages, and an offline interactive index.html
with the layered diagram. Structure is always deterministic static
analysis; prose descriptions may optionally be enriched through a
local Ollama daemon, with deterministic fallback.
"""

from __future__ import annotations

import html
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from readmenator._cache import source_fingerprint
from readmenator._config import Config
from readmenator._layers import LayerDetector
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node
from readmenator._ollama import OllamaClient
from readmenator._purpose import file_purpose
from readmenator._rank import file_pagerank
from readmenator._symindex import SymbolIndex

_SANITIZE_RE = re.compile(r"\W+")

_CB_NODE_W = 270
_CB_NODE_H = 134
_CB_RANK_SEP = 210
_CB_NODE_SEP = 64
_CB_PAD = 40
_CB_LABEL_CHARS = 28
_CB_SYM_CHARS = 24
_CB_EDGE_LABEL_CHARS = 24


def sanitize(name: str) -> str:
    """Replace non-alphanumerics with underscores for Mermaid node ids.

    Args:
        name: Component or relation label.

    Returns:
        Valid Mermaid identifier (non-alphanumerics as underscores).
    """
    return _SANITIZE_RE.sub("_", name)


class ComponentDiagramBuilder:
    """Builds component-diagram analysis from readmenator topology."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for component budgets and Ollama enrichment.
        """
        self._config = config
        self._symbols = SymbolIndex(config)
        self._ollama = OllamaClient(config)

    def build(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        project_root: str = ".",
        content_map: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Build the full analysis document.

        Args:
            nodes: Scanned file nodes.
            edges: Raw import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional community analysis (components source).
            project_root: Project root for the source-tree hash.
            content_map: Optional file contents for call-site lines.

        Returns:
            JSON-serializable component/relation analysis document.
        """
        ordered = sorted(nodes, key=lambda item: item.node_id)
        communities = self._components_of(ordered, analysis)
        rank = file_pagerank(
            [n.node_id for n in ordered],
            [(e.source, e.target) for e in (resolved_edges or [])],
            self._config.RANKING_ALPHA,
            self._config.RANKING_MAX_ITER,
            self._config.RANKING_TOLERANCE,
        )
        index = self._symbols.build(ordered, content_map)
        methods = self._symbols.methods_index(index)
        resolved_calls = self._symbols.resolve(nodes, edges, resolved_edges, content_map)
        by_id = {node.node_id: node for node in ordered}
        layers = LayerDetector().detect(ordered, edges)
        file_of_component: Dict[str, str] = {}
        components: List[Dict[str, Any]] = []
        for pos, community in enumerate(communities, start=1):
            cid = str(pos)
            members = sorted(community.file_ids)
            for member in members:
                file_of_component[member] = cid
            components.append(
                self._component(
                    cid, community.label, members, by_id, rank,
                    index, resolved_calls, depth=1,
                    resolved=resolved_edges or [], raw=edges, layers=layers,
                )
            )
        hub = ""
        if components:
            hub = max(
                components,
                key=lambda c: (sum(rank.get(m, 0.0) for m in
                                  [fm["file_path"] for fm in c["file_methods"]]),
                               c["component_id"]),
            )["component_id"]
        for component in components:
            component["hub"] = component["component_id"] == hub
        relations = self._relations(
            components, file_of_component, resolved_edges or [],
            edges, resolved_calls, index,
        )
        root = Path(project_root).resolve()
        try:
            tree_hash = source_fingerprint(str(root), [n.node_id for n in ordered])
        except (OSError, ValueError):
            tree_hash = ""
        total = len(ordered)
        return {
            "metadata": {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "source_tree_hash": tree_hash,
                "repo_name": root.name,
                "depth_level": 1 + (1 if any(c["components"] for c in components) else 0),
                "depth_cap": int(self._config.COMPONENTS_DEPTH_CAP),
                "file_coverage_summary": {
                    "total_files": total,
                    "analyzed": total,
                    "not_analyzed": 0,
                    "not_analyzed_by_reason": {},
                },
                "tree_spec": {},
            },
            "description": self._root_description(ordered, components),
            "files": {
                node.node_id: {"language": node.language, "symbols": len(node.symbols)}
                for node in ordered
            },
            "methods_index": methods,
            "components": components,
            "components_relations": relations,
        }

    def mermaid_lr(
        self,
        components: List[Dict[str, Any]],
        relations: List[Dict[str, Any]],
        docs_ref: str = ".",
    ) -> str:
        """Render the ``graph LR`` overview diagram.

        Args:
            components: Component records from build().
            relations: Relation records from build().
            docs_ref: Base href for per-component detail pages.

        Returns:
            Fenced Mermaid block with nodes, labeled edges, and clicks.
        """
        lines = ["```mermaid", "graph LR"]
        for component in components:
            lines.append(f'    {sanitize(component["name"])}["{component["name"]}"]')
        for relation in relations:
            lines.append(
                f'    {sanitize(relation["src_name"])} -- "{relation["relation"]}"'
                f' --> {sanitize(relation["dst_name"])}'
            )
        base = docs_ref.rstrip("/") if docs_ref else "."
        for component in components:
            if component.get("can_expand"):
                lines.append(
                    f'    click {sanitize(component["name"])}'
                    f' href "{base}/{sanitize(component["name"])}.md" "Details"'
                )
        lines.append("```")
        return "\n".join(lines)

    def overview_markdown(self, analysis: Dict[str, Any], docs_ref: str = ".") -> str:
        """Render the overview page (diagram plus component details).

        Args:
            analysis: Document from build().
            docs_ref: Base href for per-component detail pages.

        Returns:
            Markdown text with the diagram, details, and related entities.
        """
        components = analysis["components"]
        relations = analysis["components_relations"]
        lines = [
            self.mermaid_lr(components, relations, docs_ref),
            "",
            "## Details",
            "",
            str(analysis.get("description", "")),
            "",
        ]
        for component in components:
            lines.append(f"### {component['name']} ({component['component_id']})")
            lines.append("")
            lines.append(str(component.get("description", "")))
            entities = component.get("key_entities", [])
            if entities:
                lines.append("")
                lines.append("**Related Classes/Methods**:")
                lines.append("")
                for entity in entities:
                    ref = str(entity.get("reference_file", ""))
                    start = entity.get("reference_start_line")
                    end = entity.get("reference_end_line")
                    name = str(entity.get("qualified_name", ref))
                    if ref and start and end and start != end:
                        lines.append(f"- <a href=\"{ref}#L{start}-L{end}\">{name}</a>")
                    elif ref:
                        lines.append(f"- <a href=\"{ref}\">{name}</a>")
                    else:
                        lines.append(f"- {name}")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    def component_markdown(self, component: Dict[str, Any]) -> str:
        """Render one expandable component's detail page.

        Args:
            component: Component record with nested components.

        Returns:
            Markdown with a nested diagram and sub-component details.
        """
        nested = component.get("components", [])
        nested_relations = component.get("components_relations", [])
        lines = [f"# {component['name']}", "", str(component.get("description", "")), ""]
        if nested:
            lines.append(self.mermaid_lr(nested, nested_relations))
            lines.append("")
            for child in nested:
                lines.append(f"## {child['name']} ({child['component_id']})")
                lines.append("")
                lines.append(str(child.get("description", "")))
                lines.append("")
        files = sorted({m["file_path"] for m in component.get("file_methods", [])})
        if files:
            lines.append("**Files**:")
            lines.append("")
            lines.extend(f"- {path}" for path in files)
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    def write(
        self, analysis: Dict[str, Any], output_dir: str | Path
    ) -> Dict[str, str]:
        """Write analysis.json, the overview, component pages, and index.html.

        Args:
            analysis: Document from build().
            output_dir: Destination directory.

        Returns:
            Mapping of page identifier to written file path.
        """
        root = Path(output_dir)
        root.mkdir(parents=True, exist_ok=True)
        written: Dict[str, str] = {}
        target = root / "analysis.json"
        target.write_text(
            json.dumps(analysis, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        written["analysis"] = str(target)
        page = root / "index.html"
        page.write_text(
            self.render_page(analysis, home_href=None), encoding="utf-8"
        )
        written["index"] = str(page)
        overview = root / "overview.md"
        overview.write_text(self.overview_markdown(analysis), encoding="utf-8")
        written["overview"] = str(overview)
        for component in analysis.get("components", []):
            if not component.get("can_expand"):
                continue
            page = root / f"{sanitize(component['name'])}.md"
            page.write_text(self.component_markdown(component), encoding="utf-8")
            written[component["component_id"]] = str(page)
        stale = {p.name for p in root.glob("*.md")} - {
            Path(p).name for key, p in written.items() if key != "analysis"
        }
        for name in sorted(stale):
            try:
                (root / name).unlink()
            except OSError:
                continue
        return written

    def _components_of(
        self, nodes: List[Node], analysis: Optional[AnalysisResult]
    ) -> List[CommunityResult]:
        """Return communities, or one fallback component for all files."""
        if analysis and analysis.communities:
            return sorted(analysis.communities, key=lambda c: (-c.size, c.community_id))
        if not nodes:
            return []
        return [
            CommunityResult(
                0, "project", {n.node_id for n in nodes}, 1.0, len(nodes)
            )
        ]

    def _component(
        self,
        cid: str,
        label: str,
        members: List[str],
        by_id: Dict[str, Node],
        rank: Dict[str, float],
        index: Dict[str, List[Any]],
        calls: List[Any],
        depth: int,
        resolved: Optional[List[Edge]] = None,
        raw: Optional[List[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Build one component record with entities and file methods."""
        member_nodes = [by_id[m] for m in members if m in by_id]
        scored: List[Tuple[float, str, Any]] = []
        for node in member_nodes:
            for symbol in index.get(node.node_id, []):
                scored.append((rank.get(node.node_id, 0.0), node.node_id, symbol))
        scored.sort(key=lambda item: (-item[0], item[1], item[2].line))
        limit = max(1, int(self._config.COMPONENTS_MAX_KEY_ENTITIES))
        entities = [
            {
                "qualified_name": f"{symbol.file}::{symbol.name}",
                "reference_file": symbol.file,
                "reference_start_line": symbol.line,
                "reference_end_line": symbol.end_line,
            }
            for _, _, symbol in scored[:limit]
        ]
        file_methods = [
            {
                "file_path": node.node_id,
                "methods": [f"{node.node_id}::{s.name}" for s in index.get(node.node_id, [])],
            }
            for node in sorted(member_nodes, key=lambda n: n.node_id)
        ]
        outgoing = sorted({
            call.target_file
            for call in calls
            if call.site.file in set(members) and call.target_file
            and call.target_file not in set(members)
        })
        top_symbols = [s.name for _, _, s in scored[:limit]]
        description = self._describe(label, members, member_nodes, top_symbols, outgoing)
        layer = self._dominant_layer(members, layers or {})
        shown = max(1, int(self._config.COMPONENTS_NODE_SYMBOLS))
        expandable = (
            len(members) >= max(2, int(self._config.COMPONENTS_EXPAND_MIN_FILES))
            and depth < max(1, int(self._config.COMPONENTS_DEPTH_CAP))
        )
        nested: List[Dict[str, Any]] = []
        nested_relations: List[Dict[str, Any]] = []
        if expandable:
            groups = self._split(members)
            if len(groups) > 1:
                for pos, (name, group) in enumerate(sorted(groups.items()), start=1):
                    nested.append(
                        self._component(
                            f"{cid}.{pos}", name, sorted(group), by_id,
                            rank, index, calls, depth + 1,
                            resolved, raw, layers,
                        )
                    )
                # Roll up parent-level edges onto the nested level: files
                # outside this component map to nothing and their edges
                # drop, and pairs collapsing onto one child drop as
                # self-loops.
                nested_relations = self._relations(
                    nested,
                    {m: n["component_id"] for n in nested for m in
                     [fm["file_path"] for fm in n["file_methods"]]},
                    resolved or [], raw or [], calls, index,
                )
                expandable = True
            else:
                expandable = False
        return {
            "name": label,
            "description": description,
            "key_entities": entities,
            "source_cluster_ids": [],
            "file_methods": file_methods,
            "component_id": cid,
            "can_expand": expandable,
            "components": nested,
            "components_relations": nested_relations,
            "layer": layer,
            "symbol_count": len(scored),
            "top_symbols": [
                {"n": s.name, "k": s.kind}
                for _, _, s in scored[:shown]
            ],
            "top_symbols_more": max(0, len({s.name for _, _, s in scored}) - shown),
        }

    @staticmethod
    def _dominant_layer(members: List[str], layers: Dict[str, str]) -> str:
        """Return the most common layer among member files.

        Args:
            members: Member file identifiers.
            layers: File-to-layer mapping.

        Returns:
            Dominant layer name, or "unknown" on ties and empties.
        """
        counts: Dict[str, int] = {}
        for member in members:
            layer = layers.get(member, "unknown")
            counts[layer] = counts.get(layer, 0) + 1
        if not counts:
            return "unknown"
        top = max(counts.values())
        winners = sorted(layer for layer, total in counts.items() if total == top)
        return winners[0]

    def _split(self, members: List[str]) -> Dict[str, List[str]]:
        """Split component files by top directory for nested expansion."""
        groups: Dict[str, List[str]] = {}
        for member in members:
            parts = member.split("/")
            key = parts[0] if len(parts) > 1 else "root"
            groups.setdefault(key, []).append(member)
        if len(groups) < 2:
            return {members[0] if members else "root": members} if members else {}
        return groups

    def _relations(
        self,
        components: List[Dict[str, Any]],
        file_of_component: Dict[str, str],
        resolved: List[Edge],
        raw: List[Edge],
        calls: List[Any],
        index: Dict[str, List[Any]],
    ) -> List[Dict[str, Any]]:
        """Aggregate cross-component file edges into labeled relations."""
        by_cid = {c["component_id"]: c for c in components}
        pair_imports: Dict[Tuple[str, str], int] = {}
        for edge in list(resolved) + [e for e in raw if e.relation == "imports"]:
            src = file_of_component.get(edge.source)
            dst = file_of_component.get(edge.target)
            if src and dst and src != dst:
                pair_imports[(src, dst)] = pair_imports.get((src, dst), 0) + 1
        pair_calls: Dict[Tuple[str, str], List[Any]] = {}
        for call in calls:
            if not call.target_file:
                continue
            src = file_of_component.get(call.site.file)
            dst = file_of_component.get(call.target_file)
            if src and dst and src != dst:
                pair_calls.setdefault((src, dst), []).append(call)
        relations: List[Dict[str, Any]] = []
        for src, dst in sorted(set(pair_imports) | set(pair_calls)):
            imports = pair_imports.get((src, dst), 0)
            call_list = pair_calls.get((src, dst), [])
            if len(call_list) >= imports and call_list:
                phrase = "calls into"
            else:
                phrase = "depends on"
            key_limit = max(1, int(self._config.COMPONENTS_MAX_KEY_EDGES))
            all_limit = max(1, int(self._config.COMPONENTS_MAX_ALL_EDGES))
            key_edges = [
                {
                    "source": f"{call.site.file}|{call.site.file}::{call.site.caller}"
                    if call.site.caller else f"{call.site.file}|{call.site.file}",
                    "target": f"{call.target_file}|{call.target_qualified}",
                    "call_sites": [{"line": call.site.line, "column": call.site.column}],
                    "description": "",
                }
                for call in call_list[:key_limit]
            ]
            all_edges = [
                {
                    "source": f"{call.site.file}|{call.site.file}::{call.site.caller}"
                    if call.site.caller else f"{call.site.file}|{call.site.file}",
                    "target": f"{call.target_file}|{call.target_qualified}",
                    "call_sites": [{"line": call.site.line, "column": call.site.column}],
                    "description": "",
                }
                for call in call_list[:all_limit]
            ]
            relations.append({
                "relation": phrase,
                "src_name": by_cid[src]["name"],
                "dst_name": by_cid[dst]["name"],
                "evidence": (
                    f"{imports} imports, {len(call_list)} calls across the boundary"
                ),
                "import_count": imports,
                "call_count": len(call_list),
                "key_edges": key_edges,
                "src_id": src,
                "dst_id": dst,
                "is_static": True,
                "all_edges": all_edges,
            })
        return relations

    def _describe(
        self,
        label: str,
        members: List[str],
        member_nodes: List[Node],
        top_symbols: List[str],
        outgoing: List[str],
    ) -> str:
        """Describe a component deterministically, Ollama optionally."""
        purposes = [file_purpose(n, 90) for n in member_nodes[:3]]
        purposes = [p for p in purposes if p]
        languages = sorted({n.language for n in member_nodes})
        fallback = (
            f"{label} groups {len(members)} files"
            f" ({', '.join(languages) or 'unknown language'})"
            + (f" around {', '.join(top_symbols[:5])}" if top_symbols else "")
            + (f". {purposes[0]}" if purposes else ".")
        )
        if not self._ollama.enabled():
            return fallback
        enriched = self._ollama.describe_component(
            label, members[:12], top_symbols[:12], outgoing[:8]
        )
        return enriched or fallback

    def _root_description(
        self, nodes: List[Node], components: List[Dict[str, Any]]
    ) -> str:
        """Summarise the whole project deterministically."""
        languages = sorted({n.language for n in nodes})
        names = ", ".join(c["name"] for c in components[:8])
        text = (
            f"Static architecture map of {len(nodes)} files"
            f" ({', '.join(languages) or 'unknown languages'})"
            f" in {len(components)} components: {names}."
            " Structure is extracted statically without LLM calls;"
            " component prose may be enriched locally."
        )
        if not self._ollama.enabled():
            return text
        enriched = self._ollama.generate(
            f"Summarise this codebase in two sentences. Components: {names}. "
            f"Languages: {', '.join(languages)}. Files: {len(nodes)}.",
            system="You summarise software architectures briefly and factually.",
        )
        return enriched or text

    def render_page(
        self,
        analysis: Dict[str, Any],
        title: str = "Component Diagrams",
        home_href: Optional[str] = None,
    ) -> str:
        """Render the standalone interactive diagram page.

        Offline Cytoscape/dagre look-alike: layered left-to-right SVG
        with rounded boxes, labeled bezier arrows, hover descriptions,
        click-to-component, pan/zoom, PNG export, and a light/dark
        theme toggle. Zero external requests.

        Args:
            analysis: Document from build().
            title: Document title shown in the header.
            home_href: Optional gallery home link; omitted when None.

        Returns:
            Complete HTML document as a string.
        """
        components = analysis.get("components", [])
        relations = analysis.get("components_relations", [])
        meta = analysis.get("metadata", {})
        safe_title = html.escape(title, quote=True)
        home = (
            '<a class="home" href="' + html.escape(home_href, quote=True)
            + '">\u2190 Maps gallery</a>'
            if home_href else ""
        )
        diagram = self._svg_level(components, relations, "cb-diagram", "comp-")
        cards: List[str] = []
        for component in components:
            cards.append(self._component_card(component))
        body = "\n".join([
            _CB_PAGE_HEAD.replace("__TITLE__", safe_title),
            '<div class="topbar"><span class="brand">Component diagrams</span>',
            home,
            '<span class="spacer"></span>',
            '<button type="button" id="cb-theme" title="Toggle light and dark theme">Theme</button></div>',
            "<main>",
            f"<h1>{safe_title}</h1>",
            self._meta_chips(analysis),
            self._legend(components),
            '<div class="diagram-controls">'
            '<button type="button" id="cb-reset" title="Reset pan and zoom">Reset Layout</button>'
            '<button type="button" id="cb-fit" title="Fit the diagram to the view">Fit to View</button>'
            '<button type="button" id="cb-png" title="Export the diagram as PNG">Export PNG</button>'
            "</div>",
            diagram,
            "<h2>Details</h2>",
            f"<p>{html.escape(str(analysis.get('description', '')))}</p>",
            self._relations_section(relations),
            "\n".join(cards),
            f"<footer>Generated offline from static analysis"
            f" &middot; {html.escape(str(meta.get('source_tree_hash', ''))[:12])}</footer>",
            "</main>",
            '<div id="cb-tip" role="tooltip"></div>',
            _CB_PAGE_JS,
            "</body>\n</html>",
        ])
        return body

    def _legend(self, components: List[Dict[str, Any]]) -> str:
        """Render the dominant-layer color legend for the diagram.

        Args:
            components: Component records from build().

        Returns:
            HTML legend fragment, empty when no layer is known.
        """
        layers = sorted({str(c.get("layer", "unknown")) for c in components})
        layers = [layer for layer in layers if layer != "unknown"]
        if not layers:
            return ""
        items = "".join(
            f'<span><i style="background:'
            f"{html.escape(self._layer_color(layer), quote=True)}\"></i>"
            f"{html.escape(layer.replace('_', ' '))}</span>"
            for layer in layers
        )
        return f'<div class="legend"><span class="legend-title">Layer</span>{items}</div>'

    def _relations_section(self, relations: List[Dict[str, Any]]) -> str:
        """Render every arrow with its evidence and sample call sites.

        Args:
            relations: Relation records from build().

        Returns:
            HTML fragment listing each relation and its top key edges.
        """
        if not relations:
            return ""
        parts = ["<h2>Relations</h2>", '<ul class="rellist">']
        for relation in relations:
            src = html.escape(str(relation.get("src_name", "")))
            dst = html.escape(str(relation.get("dst_name", "")))
            phrase = html.escape(str(relation.get("relation", "")))
            evidence = html.escape(str(relation.get("evidence", "")))
            parts.append(f"<li><b>{src}</b> {phrase} <b>{dst}</b> — {evidence}")
            samples = []
            for edge in relation.get("key_edges", [])[:3]:
                source = str(edge.get("source", "")).split("|")[-1]
                target = str(edge.get("target", "")).split("|")[-1]
                sites = edge.get("call_sites", [])
                line = sites[0].get("line", 0) if sites else 0
                samples.append(
                    f"<code>{html.escape(source)}@{int(line)} "
                    f"\u2192 {html.escape(target)}</code>"
                )
            if samples:
                parts.append("<br>" + " · ".join(samples))
            parts.append("</li>")
        parts.append("</ul>")
        return "\n".join(parts)

    def thumbnail_svg(
        self, components: List[Dict[str, Any]], relations: List[Dict[str, Any]]
    ) -> str:
        """Render a small dagre-style preview as inline SVG.

        Only numbers and escaped colors reach the markup, so the
        fragment is safe to embed in the gallery card.

        Args:
            components: Component records from build().
            relations: Relation records from build().

        Returns:
            SVG markup, or an empty string when there are no components.
        """
        if not components:
            return ""
        w, h = 320, 150
        names = sorted(c["component_id"] for c in components)
        slots = {cid: pos for pos, cid in enumerate(names)}
        parts = [f'<svg class="thumb" viewBox="0 0 {w} {h}" aria-hidden="true" focusable="false">']
        drawn = 0
        for relation in relations:
            a = slots.get(str(relation.get("src_id", "")))
            b = slots.get(str(relation.get("dst_id", "")))
            if a is None or b is None or a == b:
                continue
            x1 = 20 + 280 * a / max(1, len(names) - 1)
            x2 = 20 + 280 * b / max(1, len(names) - 1)
            y1 = 40 + (drawn * 37) % 70
            y2 = 40 + ((drawn + 2) * 41) % 70
            parts.append(
                f'<path d="M{x1:.1f} {y1:.1f} C{x1 + 40:.1f} {y1:.1f} '
                f'{x2 - 40:.1f} {y2:.1f} {x2:.1f} {y2:.1f}" fill="none" '
                f'stroke="#38bdf8" stroke-opacity="0.75" stroke-width="1.4"/>'
            )
            drawn += 1
        for pos, cid in enumerate(names):
            x = 20 + 280 * pos / max(1, len(names) - 1)
            y = 75
            parts.append(
                f'<circle cx="{x:.1f}" cy="{y}" r="7" fill="#0b1224" '
                f'stroke="#22d3ee" stroke-width="2"/>'
            )
        parts.append("</svg>")
        return "".join(parts)

    def _meta_chips(self, analysis: Dict[str, Any]) -> str:
        """Render headline counters for the diagram page."""
        meta = analysis.get("metadata", {})
        coverage = meta.get("file_coverage_summary", {})
        chips = [
            f"{len(analysis.get('components', []))} components",
            f"{len(analysis.get('components_relations', []))} relations",
            f"{coverage.get('analyzed', len(analysis.get('files', {})))} files",
        ]
        return '<div class="chips">' + "".join(
            f"<span>{html.escape(chip)}</span>" for chip in chips
        ) + "</div>"

    def _component_card(self, component: Dict[str, Any]) -> str:
        """Render one component detail card with entities and files."""
        cid = str(component.get("component_id", ""))
        anchor = "comp-" + cid.replace(".", "-")
        name = html.escape(str(component.get("name", cid)))
        parts = [
            f'<section class="component" id="{anchor}">',
            f"<h3>{name} ({html.escape(cid)})",
        ]
        if component.get("can_expand"):
            parts.append(f' <a href="#{anchor}-children">[Expand]</a>')
        parts.append("</h3>")
        parts.append(f"<p>{html.escape(str(component.get('description', '')))}</p>")
        entities = component.get("key_entities", [])
        if entities:
            parts.append("<h4>Related Classes/Methods:</h4>")
            parts.append('<ul class="references">')
            for entity in entities:
                ref = str(entity.get("reference_file", ""))
                start = entity.get("reference_start_line")
                end = entity.get("reference_end_line")
                label = html.escape(str(entity.get("qualified_name", ref)), quote=True)
                if ref and start and end and start != end:
                    parts.append(
                        f'<li><a href="{html.escape(ref, quote=True)}'
                        f'#L{int(start)}-L{int(end)}"><code>{label}</code></a></li>'
                    )
                elif ref:
                    parts.append(
                        f'<li><a href="{html.escape(ref, quote=True)}">'
                        f"<code>{label}</code></a></li>"
                    )
                else:
                    parts.append(f"<li><code>{label}</code></li>")
            parts.append("</ul>")
        else:
            parts.append("<h4>Related Classes/Methods:</h4><p><em>None</em></p>")
        nested = component.get("components", [])
        if nested:
            parts.append(f'<h4 id="{anchor}-children">Sub-components</h4>')
            parts.append(self._svg_level(
                nested, component.get("components_relations", []),
                f"cb-sub-{anchor}", "comp-",
            ))
            for child in nested:
                child_cid = str(child.get("component_id", ""))
                child_anchor = "comp-" + child_cid.replace(".", "-")
                parts.append(f'<h5 id="{child_anchor}">'
                             f"{html.escape(str(child.get('name', child_cid)))}"
                             f" ({html.escape(child_cid)})</h5>")
                parts.append(f"<p>{html.escape(str(child.get('description', '')))}</p>")
        files = sorted({m["file_path"] for m in component.get("file_methods", [])})
        if files:
            parts.append("<h4>Files</h4>")
            parts.append('<ul class="references">')
            parts.extend(
                f"<li><code>{html.escape(path)}</code></li>" for path in files
            )
            parts.append("</ul>")
        parts.append("</section>")
        return "\n".join(parts)

    def _layer_color(self, layer: str) -> str:
        """Return the configured palette color for an architectural layer.

        Args:
            layer: Layer name.

        Returns:
            CSS color string, gray when the layer is unknown.
        """
        palette = dict(self._config.FORCEGRAPH_LAYER_COLORS)
        return palette.get(layer or "unknown", "#64748b")

    def _svg_level(
        self,
        components: List[Dict[str, Any]],
        relations: List[Dict[str, Any]],
        svg_id: str,
        anchor_prefix: str,
    ) -> str:
        """Render one component level as a layered LR SVG diagram.

        Boxes carry the component name, file/symbol counts, dominant
        layer, and top symbols; hubs glow; arrow width follows call and
        import evidence.
        """
        if not components:
            return '<p class="muted">No components at this level.</p>'
        by_cid = {str(c["component_id"]): c for c in components}
        rel_of: Dict[Tuple[str, str], Dict[str, Any]] = {}
        for entry in relations:
            src, dst = str(entry.get("src_id", "")), str(entry.get("dst_id", ""))
            if src in by_cid and dst in by_cid and src != dst:
                rel_of.setdefault((src, dst), entry)
        pairs = sorted(rel_of)
        pos, width, height = _rank_layout(sorted(by_cid), pairs)
        edges: List[str] = []
        for src, dst in pairs:
            entry = rel_of[(src, dst)]
            phrase = str(entry.get("relation", ""))
            calls = int(entry.get("call_count", 0))
            imports = int(entry.get("import_count", 0))
            weight = 1.5 + min(3.5, math.log2(1 + calls + imports))
            x1, y1 = pos[src]
            x2, y2 = pos[dst]
            sx, sy = x1 + _CB_NODE_W, y1 + _CB_NODE_H / 2
            tx, ty = x2, y2 + _CB_NODE_H / 2
            dx = max(50.0, (tx - sx) / 2)
            mx, my = (sx + tx) / 2, (sy + ty) / 2
            label = phrase if len(phrase) <= _CB_EDGE_LABEL_CHARS else phrase[:_CB_EDGE_LABEL_CHARS - 1] + "…"
            counts = f"{calls} calls · {imports} imports"
            edges.append(
                f'<path d="M{sx:.1f} {sy:.1f} C{sx + dx:.1f} {sy:.1f} '
                f'{tx - dx:.1f} {ty:.1f} {tx:.1f} {ty:.1f}" class="cb-edge" '
                f'style="stroke-width:{weight:.1f}"/>'
                f'<text x="{mx:.1f}" y="{my - 8:.1f}" class="cb-edge-label">'
                f"{html.escape(label)}</text>"
                f'<text x="{mx:.1f}" y="{my + 6:.1f}" class="cb-edge-sub">'
                f"{html.escape(counts)}</text>"
            )
        shown = max(1, int(self._config.COMPONENTS_NODE_SYMBOLS))
        nodes: List[str] = []
        for cid in sorted(by_cid):
            component = by_cid[cid]
            x, y = pos[cid]
            name = str(component.get("name", cid))
            short = name if len(name) <= _CB_LABEL_CHARS else name[:_CB_LABEL_CHARS - 1] + "…"
            files = len(component.get("file_methods", []))
            symbols = int(component.get("symbol_count", 0))
            layer = str(component.get("layer", "unknown"))
            anchor = anchor_prefix + cid.replace(".", "-")
            desc = html.escape(str(component.get("description", "")), quote=True)
            classes = "cb-node"
            if component.get("can_expand"):
                classes += " linked"
            if component.get("hub"):
                classes += " hub"
            lines = [f'<g class="{classes}" data-desc="{desc}"><a href="#{anchor}">']
            border = html.escape(self._layer_color(layer), quote=True)
            stroke_w = "3" if component.get("can_expand") else "2.5"
            lines.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{_CB_NODE_W}" height="{_CB_NODE_H}" rx="10" '
                f'stroke="{border}" stroke-width="{stroke_w}"/>'
                f'<text x="{x + 14:.1f}" y="{y + 24:.1f}" class="cb-node-label">'
                f"{html.escape(short)}</text>"
                f'<text x="{x + 14:.1f}" y="{y + 40:.1f}" class="cb-node-sub">'
                f"{files} files · {symbols} symbols</text>"
                f'<circle cx="{x + 20:.1f}" cy="{y + 52:.1f}" r="4" fill="'
                f"{html.escape(self._layer_color(layer), quote=True)}\"/>"
                f'<text x="{x + 30:.1f}" y="{y + 56:.1f}" class="cb-node-layer">'
                f"{html.escape(layer.replace('_', ' '))}</text>"
            )
            top = component.get("top_symbols", [])[:shown]
            row = y + 72
            for symbol in top:
                label = str(symbol.get("n", ""))
                if len(label) > _CB_SYM_CHARS:
                    label = label[:_CB_SYM_CHARS - 1] + "…"
                lines.append(
                    f'<text x="{x + 14:.1f}" y="{row:.1f}" class="cb-node-sym">'
                    f"{html.escape(label)}</text>"
                )
                row += 14
            more = int(component.get("top_symbols_more", 0))
            if more:
                lines.append(
                    f'<text x="{x + 14:.1f}" y="{row:.1f}" class="cb-node-sub">'
                    f"+{more} more</text>"
                )
            if component.get("hub"):
                lines.append(
                    f'<text x="{x + _CB_NODE_W - 14:.1f}" y="{y + 20:.1f}" '
                    f'class="cb-node-hub">HUB</text>'
                )
            lines.append("</a></g>")
            nodes.append("".join(lines))
        return (
            f'<div class="cb-wrap"><svg id="{html.escape(svg_id, quote=True)}" class="cb-diagram" '
            f'viewBox="0 0 {width:.0f} {height:.0f}" role="img" '
            f'aria-label="Component diagram">'
            f"<defs><marker id=\"{html.escape(svg_id, quote=True)}-arrow\" "
            'viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0 0 L10 5 L0 10 z" class="cb-arrow"/></marker></defs>'
            + "".join(
                edge.replace('class="cb-edge"', 'class="cb-edge" marker-end="url(#'
                             + html.escape(svg_id, quote=True) + '-arrow)"')
                for edge in edges
            )
            + "".join(nodes)
            + "</svg></div>"
        )


def _rank_layout(
    cids: List[str], pairs: List[Tuple[str, str]]
) -> Tuple[Dict[str, Tuple[float, float]], float, float]:
    """Layer component ids left-to-right by longest-path rank.

    Args:
        cids: Component ids in deterministic order.
        pairs: Directed (source, target) component pairs.

    Returns:
        Tuple of positions by id plus the SVG width and height.
    """
    rank: Dict[str, int] = {cid: 0 for cid in cids}
    edges = sorted({(a, b) for a, b in pairs if a in rank and b in rank and a != b})
    for _ in range(len(cids) + 1):
        moved = False
        for src, dst in edges:
            if rank[dst] < rank[src] + 1:
                rank[dst] = rank[src] + 1
                moved = True
        if not moved:
            break
    columns: Dict[int, List[str]] = {}
    for cid in cids:
        columns.setdefault(rank[cid], []).append(cid)
    tallest = 0.0
    for members in columns.values():
        tallest = max(tallest, len(members) * (_CB_NODE_H + _CB_NODE_SEP) - _CB_NODE_SEP)
    pos: Dict[str, Tuple[float, float]] = {}
    for depth in sorted(columns):
        members = sorted(columns[depth])
        height = len(members) * (_CB_NODE_H + _CB_NODE_SEP) - _CB_NODE_SEP
        top = _CB_PAD + (tallest - height) / 2
        for row, cid in enumerate(members):
            pos[cid] = (
                _CB_PAD + depth * (_CB_NODE_W + _CB_RANK_SEP),
                top + row * (_CB_NODE_H + _CB_NODE_SEP),
            )
    width = _CB_PAD * 2 + (max(rank.values()) + 1) * _CB_NODE_W + max(rank.values()) * _CB_RANK_SEP
    return pos, width, tallest + _CB_PAD * 2


_CB_PAGE_HEAD = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ | Component diagrams</title>
<style>
:root{--cb-bg:#020617;--cb-stage:#030a1c;--cb-panel:#0b1224;--cb-panel2:#111c33;--cb-ink:#f8fafc;--cb-muted:#94a3b8;--cb-faint:#475569;--cb-border:#1e293b;--cb-accent:#22d3ee;--cb-accent2:#f472b6;--cb-chip:#111c33;--cb-glow:rgba(34,211,238,.16)}
html[data-theme="light"]{--cb-bg:#f8fafc;--cb-stage:#eef2f7;--cb-panel:#ffffff;--cb-panel2:#f1f5f9;--cb-ink:#0f172a;--cb-muted:#475569;--cb-faint:#94a3b8;--cb-border:#e2e8f0;--cb-accent:#0891b2;--cb-accent2:#db2777;--cb-chip:#f1f5f9;--cb-glow:rgba(8,145,178,.10)}
*{box-sizing:border-box}
body{margin:0 auto;max-width:1240px;padding:20px;background:var(--cb-bg);color:var(--cb-ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;line-height:1.6}
a{color:var(--cb-accent)}
.topbar{display:flex;align-items:center;gap:12px;margin-bottom:8px}
.brand{font-weight:700;background:linear-gradient(90deg,var(--cb-ink),var(--cb-accent) 70%,var(--cb-accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.spacer{flex:1}
.home,.topbar button{font:inherit;font-size:12px;text-decoration:none;border:1px solid var(--cb-border);border-radius:9px;padding:6px 10px;color:var(--cb-ink);background:var(--cb-panel);cursor:pointer}
.home:hover,.topbar button:hover{border-color:var(--cb-accent)}
h1{margin:.4em 0 .2em;font-size:22px}
h2{font-size:15px;letter-spacing:.1em;text-transform:uppercase;color:var(--cb-muted);margin:26px 0 8px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 4px}
.chips span{background:var(--cb-chip);border:1px solid var(--cb-border);border-radius:999px;padding:2px 10px;font-size:12px;color:var(--cb-muted)}
.chips span b{color:var(--cb-accent)}
.legend{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:10px 0 2px;font-size:12px;color:var(--cb-muted)}
.legend-title{letter-spacing:.12em;text-transform:uppercase;font-size:10px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:3px;box-shadow:0 0 8px currentColor}
.diagram-controls{margin:10px 0;text-align:center}
.diagram-controls button{font:inherit;margin:0 5px;padding:8px 16px;background:var(--cb-panel);color:var(--cb-ink);border:1px solid var(--cb-border);border-radius:9px;cursor:pointer}
.diagram-controls button:hover{border-color:var(--cb-accent)}
.cb-wrap{border:1px solid var(--cb-border);border-radius:12px;background:radial-gradient(900px 400px at 20% 0%,var(--cb-glow),transparent 70%),var(--cb-stage);overflow:hidden}
svg.cb-diagram{display:block;width:100%;height:auto;touch-action:none;cursor:grab}
.cb-node rect{fill:var(--cb-panel2)}
.cb-node:hover rect{stroke:var(--cb-accent)!important;stroke-width:3}
.cb-node.hub rect{filter:drop-shadow(0 0 10px var(--cb-glow))}
.cb-node a{text-decoration:none}
.cb-node-label{fill:var(--cb-ink);font-size:13px;font-weight:700}
.cb-node-sub{fill:var(--cb-muted);font-size:10px}
.cb-node-layer{fill:var(--cb-muted);font-size:10px}
.cb-node-sym{fill:var(--cb-accent);font-size:10.5px;font-family:ui-monospace,Menlo,Consolas,monospace}
.cb-node-hub{fill:var(--cb-accent2);font-size:9px;font-weight:700;text-anchor:end;letter-spacing:.1em}
.cb-edge{fill:none;stroke:#38bdf8;stroke-opacity:.75}
.cb-arrow{fill:#38bdf8;fill-opacity:.9}
.cb-edge-label{fill:var(--cb-ink);font-size:10.5px;text-anchor:middle;paint-order:stroke;stroke:var(--cb-stage);stroke-width:4px}
.cb-edge-sub{fill:var(--cb-muted);font-size:9px;text-anchor:middle;paint-order:stroke;stroke:var(--cb-stage);stroke-width:4px}
.component{border:1px solid var(--cb-border);border-left:3px solid var(--cb-accent);background:var(--cb-panel);padding:15px;border-radius:10px;margin-bottom:20px}
.component h3{color:var(--cb-ink);margin-top:0}
.component h4{color:var(--cb-muted);font-size:11px;letter-spacing:.1em;text-transform:uppercase}
.rellist{list-style:none;padding-left:0}
.rellist li{background:var(--cb-panel);border:1px solid var(--cb-border);border-radius:8px;padding:8px 12px;margin:6px 0;font-size:12px}
.rellist b{color:var(--cb-accent)}
.references{list-style:none;padding-left:0;margin:10px 0}
.references li{margin:4px 0}
code{background:var(--cb-chip);border:1px solid var(--cb-border);padding:1px 6px;border-radius:6px;font-size:12px}
.muted{color:var(--cb-muted)}
footer{color:var(--cb-muted);font-size:12px;margin:24px 0}
#cb-tip{position:fixed;z-index:50;pointer-events:none;display:none;max-width:340px;background:var(--cb-panel);color:var(--cb-ink);border:1px solid var(--cb-border);border-radius:10px;padding:8px 10px;font-size:12px;box-shadow:0 12px 30px rgba(0,0,0,.4)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
</head>
<body>
"""

_CB_PAGE_JS = """<script>
(function(){
"use strict";
try{var s=localStorage.getItem("readmenator-theme");if(s==="light"||s==="dark")document.documentElement.setAttribute("data-theme",s);}catch(e){}
document.getElementById("cb-theme").addEventListener("click",function(){
  var r=document.documentElement,n=r.getAttribute("data-theme")==="light"?"dark":"light";
  r.setAttribute("data-theme",n);try{localStorage.setItem("readmenator-theme",n);}catch(e){}
});
var tip=document.getElementById("cb-tip");
document.querySelectorAll(".cb-node").forEach(function(g){
  g.addEventListener("mousemove",function(ev){
    var d=g.getAttribute("data-desc");
    if(!d){tip.style.display="none";return;}
    tip.textContent=d;tip.style.display="block";
    tip.style.left=Math.min(window.innerWidth-330,ev.clientX+12)+"px";
    tip.style.top=(ev.clientY+14)+"px";
  });
  g.addEventListener("mouseleave",function(){tip.style.display="none";});
});
document.querySelectorAll("svg.cb-diagram").forEach(function(svg){
  var vb=svg.viewBox.baseVal,home={x:vb.x,y:vb.y,w:vb.width,h:vb.height},drag=null;
  function set(x,y,w,h){svg.setAttribute("viewBox",x+" "+y+" "+w+" "+h);}
  function cur(){var v=svg.viewBox.baseVal;return {x:v.x,y:v.y,w:v.width,h:v.height};}
  svg.addEventListener("pointerdown",function(ev){drag={x:ev.clientX,y:ev.clientY,v:cur()};svg.setPointerCapture(ev.pointerId);});
  svg.addEventListener("pointermove",function(ev){
    if(!drag)return;
    var r=svg.getBoundingClientRect(),k=drag.v.w/r.width;
    set(drag.v.x-(ev.clientX-drag.x)*k,drag.v.y-(ev.clientY-drag.y)*k,drag.v.w,drag.v.h);
  });
  svg.addEventListener("pointerup",function(){drag=null;});
  svg.addEventListener("wheel",function(ev){
    ev.preventDefault();
    var v=cur(),r=svg.getBoundingClientRect(),f=Math.exp(ev.deltaY*0.0012);
    var mx=v.x+(ev.clientX-r.left)/r.width*v.w,my=v.y+(ev.clientY-r.top)/r.height*v.h;
    var w=Math.min(home.w*4,Math.max(home.w/8,v.w*f)),h=w*v.h/v.w;
    set(mx-(mx-v.x)*w/v.w,my-(my-v.y)*h/v.h,w,h);
  },{passive:false});
  svg._home=home;svg._set=set;
});
document.getElementById("cb-reset").addEventListener("click",function(){
  var svg=document.getElementById("cb-diagram");if(!svg)return;var h=svg._home;svg._set(h.x,h.y,h.w,h.h);
});
document.getElementById("cb-fit").addEventListener("click",function(){
  var svg=document.getElementById("cb-diagram");if(!svg)return;var h=svg._home;svg._set(h.x,h.y,h.w,h.h);
});
document.getElementById("cb-png").addEventListener("click",function(){
  var svg=document.getElementById("cb-diagram");if(!svg)return;
  try{
    var data=new XMLSerializer().serializeToString(svg);
    var img=new Image();
    img.onload=function(){
      var c=document.createElement("canvas"),k=2;
      c.width=svg.viewBox.baseVal.width*k;c.height=svg.viewBox.baseVal.height*k;
      var x=c.getContext("2d");x.fillStyle="#020617";x.fillRect(0,0,c.width,c.height);
      x.drawImage(img,0,0,c.width,c.height);
      var a=document.createElement("a");a.download="component-diagram.png";a.href=c.toDataURL("image/png");a.click();
    };
    img.src="data:image/svg+xml;charset=utf-8,"+encodeURIComponent(data);
  }catch(e){}
});
})();
</script>
"""
