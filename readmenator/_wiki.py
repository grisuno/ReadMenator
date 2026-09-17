"""Deterministic agent wiki generator for readmenator.

Builds a navigable, progressively disclosed wiki on top of the scanned
knowledge graph. The layout mirrors the Karpathy LLM Wiki Pattern used
by graphify and second-brain (index plus one page per community plus
machine-readable connections), but every page is synthesised
deterministically from static analysis with zero LLM calls, zero
tokens, and an honest confidence trail.

Output layout::

    readmenator-wiki/
    ├── index.md              # entry point: overview plus all links
    ├── community_<id>_<slug>.md  # one synthesis page per community
    ├── connections.json      # typed bridges with strength and confidence
    ├── queries.md            # suggested questions plus answer log
    └── REPORT.md             # honest audit: coverage, confidence, limits
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._analyzer import dominant_directory
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    CommunityResult,
    Edge,
    Node,
    SecurityFinding,
)
from readmenator._security import fix_hint_for


def _is_garbage_purpose(text: str) -> bool:
    """Return True for file-doc first lines that state no purpose."""
    return _clean_purpose(text) == ""


_BANNER_RUN_RE = re.compile(r"(?:[=#*]{4,}|[-_]{8,})")
_LEADING_FILE_RE = re.compile(
    r"^[\w\-.]+\.(c|h|py|js|go|rs|sh|s|java|cs|php)\b[\s:.\-]*", re.IGNORECASE
)


def _clean_purpose(text: str) -> str:
    """Return the purpose signal of a doc first line, or empty string."""
    stripped = text.strip()
    if _is_garbage_doc(stripped):
        return ""
    lowered = stripped.lower()
    if lowered.startswith("spdx-license-identifier"):
        return ""
    cut = _BANNER_RUN_RE.split(stripped, maxsplit=1)[0].strip()
    cut = _LEADING_FILE_RE.sub("", cut).strip()
    if not cut or _is_garbage_doc(cut):
        return ""
    if re.fullmatch(r"[\(\[].*[\)\]]", cut):
        return ""
    return cut

logger = logging.getLogger(__name__)


def _slug(text: str) -> str:
    """Return a filesystem-safe slug for community labels."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower())
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "community"


def _escape(text: str) -> str:
    """Escape markdown table breaking characters in one line of text."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def _is_garbage_doc(text: str) -> bool:
    """Return True for doc lines that carry no purpose signal."""
    stripped = text.strip()
    if len(stripped) < 3:
        return True
    if re.search(r"coding[:=]", stripped):
        return True
    return not re.search(r"[A-Za-z]{3,}", stripped)


def existing_ids(connections: List[Dict[str, object]]) -> Set[frozenset]:
    """Return community id pairs already linked, to avoid duplicate edges."""
    pairs: Set[frozenset] = set()
    for conn in connections:
        pair = {conn.get("community_a"), conn.get("community_b")}
        if all(isinstance(v, int) for v in pair):
            pairs.add(frozenset(pair))
    return pairs


def _display_names(communities: List[CommunityResult]) -> Dict[int, str]:
    """Return unique display names, disambiguating duplicate labels."""
    counts = Counter(c.label for c in communities)
    names: Dict[int, str] = {}
    for community in communities:
        if counts[community.label] > 1:
            names[community.community_id] = (
                f"{community.label} (community {community.community_id})"
            )
        else:
            names[community.community_id] = community.label
    return names


class WikiGenerator:
    """Generates the navigable agent wiki from scanned topology."""

    def __init__(self, config: Config) -> None:
        """Store configuration for wiki output limits and paths."""
        self._config = config
        self._privacy = bool(config.PRIVACY_MODE)

    def generate(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        project_root: str,
    ) -> str:
        """Write all wiki files and return the output directory path."""
        root = Path(project_root).resolve()
        out_dir = root / self._config.WIKI_OUTPUT_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        communities = self._resolve_communities(nodes, analysis, list(resolved_edges or []))
        node_map: Dict[str, Node] = {n.node_id: n for n in nodes}
        resolved = list(resolved_edges or [])
        connections = self._build_connections(communities, resolved, analysis, node_map, layers)

        pages: List[Tuple[CommunityResult, str]] = []
        for community in communities:
            filename = f"community_{community.community_id}_{_slug(community.label)}.md"
            content = self._build_community_page(
                community, node_map, resolved, analysis,
                layers, findings, analysis_v2, connections,
            )
            self._write(out_dir / filename, content)
            pages.append((community, filename))

        self._prune_stale_pages(out_dir, {filename for _, filename in pages})

        index = self._build_index(
            nodes, resolved, analysis, layers, findings,
            analysis_v2, communities, pages, connections, root.name, str(root),
        )
        self._write(out_dir / "index.md", index)
        self._write(out_dir / "connections.json", self._build_connections_json(connections))
        self._write(out_dir / "queries.md", self._build_queries(analysis))
        self._write(
            out_dir / "REPORT.md",
            self._build_report(nodes, edges, resolved, analysis, layers, findings, analysis_v2, communities, root.name, str(root)),
        )

        logger.info("Agent wiki written to %s (%d pages)", out_dir, len(pages))
        return str(out_dir)

    def _prune_stale_pages(self, out_dir: Path, current: Set[str]) -> None:
        """Delete community pages from previous runs that are no longer generated."""
        for stale in sorted(out_dir.glob("community_*.md")):
            if stale.name not in current:
                try:
                    stale.unlink()
                except OSError:
                    logger.debug("Could not prune stale wiki page: %s", stale)

    def lint(self, project_root: str) -> List[str]:
        """Check wiki health and return a list of issue descriptions."""
        root = Path(project_root).resolve()
        out_dir = root / self._config.WIKI_OUTPUT_DIR
        issues: List[str] = []
        if not out_dir.is_dir():
            return [f"missing wiki directory: {self._config.WIKI_OUTPUT_DIR}"]
        if not (out_dir / "index.md").exists():
            issues.append("missing entry point: index.md")
        pages = sorted(out_dir.glob("community_*.md"))
        if not pages:
            issues.append("no community pages found")
        try:
            raw = (out_dir / "connections.json").read_text(encoding="utf-8")
            data = json.loads(raw)
            if not isinstance(data, list):
                issues.append("connections.json is not a list")
        except FileNotFoundError:
            issues.append("missing connections.json")
        except json.JSONDecodeError as exc:
            issues.append(f"connections.json is not valid JSON: {exc}")
        return issues

    def _resolve_communities(
        self,
        nodes: List[Node],
        analysis: Optional[AnalysisResult],
        resolved: List[Edge],
    ) -> List[CommunityResult]:
        """Return detected communities plus an orphan fallback for leftovers."""
        detected = list(analysis.communities) if analysis and analysis.communities else []
        if not detected:
            file_ids = {n.node_id for n in nodes}
            if not file_ids:
                return []
            detected = [CommunityResult(0, "root", file_ids, 1.0, len(file_ids))]
            return sorted(detected, key=lambda c: c.community_id)
        covered: Set[str] = set()
        for community in detected:
            covered.update(community.file_ids)
        leftovers = {n.node_id for n in nodes} - covered
        if leftovers:
            internal = sum(1 for e in resolved if e.source in leftovers and e.target in leftovers)
            touching = sum(1 for e in resolved if e.source in leftovers or e.target in leftovers)
            cohesion = (internal / touching) if touching else 0.0
            next_id = max(c.community_id for c in detected) + 1
            detected.append(CommunityResult(next_id, "orphans", leftovers, cohesion, len(leftovers)))
        return sorted(detected, key=lambda c: c.community_id)

    def _community_of(
        self, node_id: str, communities: List[CommunityResult]
    ) -> Optional[CommunityResult]:
        """Return the community containing the given node id."""
        for community in communities:
            if node_id in community.file_ids:
                return community
        return None

    def _build_connections(
        self,
        communities: List[CommunityResult],
        resolved: List[Edge],
        analysis: Optional[AnalysisResult],
        node_map: Optional[Dict[str, Node]] = None,
        layers: Optional[Dict[str, str]] = None,
    ) -> List[Dict[str, object]]:
        """Derive typed bridges between communities with strength scores."""
        connections: List[Dict[str, object]] = []
        seen: Set[Tuple[str, str, str]] = set()
        node_to_community: Dict[str, int] = {}
        for community in communities:
            for fid in community.file_ids:
                node_to_community[fid] = community.community_id

        for edge in resolved:
            src_c = node_to_community.get(edge.source)
            tgt_c = node_to_community.get(edge.target)
            if src_c is None or tgt_c is None or src_c == tgt_c:
                continue
            key = (str(min(src_c, tgt_c)), str(max(src_c, tgt_c)), "depends_on")
            if key in seen:
                continue
            seen.add(key)
            connections.append({
                "community_a": src_c,
                "community_b": tgt_c,
                "connection_type": "depends_on",
                "explanation": (
                    f"Extracted import edge crosses communities: "
                    f"{edge.source} imports {edge.target}."
                ),
                "strength": 0.9,
                "confidence": "EXTRACTED",
            })

        if analysis and analysis.surprising_connections:
            for src, tgt, hops, _comms in analysis.surprising_connections:
                src_c = node_to_community.get(src)
                tgt_c = node_to_community.get(tgt)
                strength = max(0.4, round(1.0 - 0.1 * hops, 2))
                connections.append({
                    "community_a": src_c if src_c is not None else src,
                    "community_b": tgt_c if tgt_c is not None else tgt,
                    "connection_type": "bridges",
                    "explanation": (
                        f"Inferred cross-community bridge: {src} reaches "
                        f"{tgt} in {hops} hops."
                    ),
                    "strength": strength,
                    "confidence": "INFERRED",
                })

        connections.sort(key=lambda c: float(c["strength"]), reverse=True)
        connections.extend(
            self._duplicate_links(communities, node_map, existing_ids(connections))
        )
        connections.extend(
            self._shared_context_links(communities, connections, node_map or {}, layers or {})
        )
        connections.sort(key=lambda c: float(c["strength"]), reverse=True)
        return connections[: self._config.WIKI_MAX_CONNECTIONS]

    @staticmethod
    def _duplicate_links(
        communities: List[CommunityResult],
        node_map: Dict[str, Node],
        skip_pairs: Set[frozenset],
    ) -> List[Dict[str, object]]:
        """Flag community pairs sharing an unusual fraction of symbol names."""
        symbols: Dict[int, Set[str]] = {}
        for community in communities:
            names: Set[str] = set()
            for fid in community.file_ids:
                node = node_map.get(fid)
                if node is not None:
                    names.update(s.name for s in node.symbols)
            symbols[community.community_id] = names
        links: List[Dict[str, object]] = []
        ids = sorted(symbols)
        for pos, first in enumerate(ids):
            for second in ids[pos + 1:]:
                if frozenset({first, second}) in skip_pairs:
                    continue
                left, right = symbols[first], symbols[second]
                if not left or not right:
                    continue
                shared = left & right
                union = left | right
                jaccard = len(shared) / len(union) if union else 0.0
                if len(shared) >= 3 and jaccard >= 0.3:
                    shown = ", ".join(f"`{s}`" for s in sorted(shared)[:6])
                    links.append({
                        "community_a": first,
                        "community_b": second,
                        "connection_type": "duplicates",
                        "explanation": (
                            f"Inferred duplicated scope: communities {first} and "
                            f"{second} share {len(shared)} symbols "
                            f"(Jaccard {jaccard:.2f}), e.g. {shown}. "
                            f"Candidate for consolidation."
                        ),
                        "strength": round(0.4 + 0.4 * jaccard, 2),
                        "confidence": "INFERRED",
                    })
        return links

    def _shared_context_links(
        self,
        communities: List[CommunityResult],
        existing: List[Dict[str, object]],
        node_map: Dict[str, Node],
        layers: Dict[str, str],
    ) -> List[Dict[str, object]]:
        """Infer weak links between otherwise disconnected communities."""
        linked: Set[frozenset] = set()
        for conn in existing:
            pair = {conn.get("community_a"), conn.get("community_b")}
            if all(isinstance(v, int) for v in pair):
                linked.add(frozenset(pair))
        links: List[Dict[str, object]] = []
        for i, first in enumerate(communities):
            for second in communities[i + 1:]:
                if frozenset({first.community_id, second.community_id}) in linked:
                    continue
                shared = self._shared_context(first, second, node_map, layers)
                if shared:
                    links.append({
                        "community_a": first.community_id,
                        "community_b": second.community_id,
                        "connection_type": "shares_context",
                        "explanation": (
                            f"Inferred shared context ({shared}) with no import "
                            f"path between community {first.community_id} "
                            f"({first.label}) and community {second.community_id} "
                            f"({second.label})."
                        ),
                        "strength": 0.5,
                        "confidence": "INFERRED",
                    })
        return links

    @staticmethod
    def _shared_context(
        first: CommunityResult,
        second: CommunityResult,
        node_map: Dict[str, Node],
        layers: Dict[str, str],
    ) -> str:
        """Describe shared language or layer between two communities."""
        def dominant(ids: Set[str], key: str) -> str:
            values = []
            for fid in ids:
                if key == "language":
                    node = node_map.get(fid)
                    if node:
                        values.append(node.language)
                else:
                    layer = layers.get(fid)
                    if layer:
                        values.append(layer)
            if not values:
                return ""
            return Counter(values).most_common(1)[0][0]

        shared: List[str] = []
        first_lang = dominant(first.file_ids, "language")
        second_lang = dominant(second.file_ids, "language")
        if first_lang and first_lang == second_lang:
            shared.append(f"language {first_lang}")
        first_layer = dominant(first.file_ids, "layer")
        second_layer = dominant(second.file_ids, "layer")
        if first_layer and first_layer == second_layer:
            shared.append(f"layer {first_layer}")
        return " and ".join(shared)

    def _build_connections_json(self, connections: List[Dict[str, object]]) -> str:
        """Serialize connections as pretty-printed JSON."""
        return json.dumps(connections, indent=2, ensure_ascii=False) + "\n"

    def _definition_for(
        self, community: CommunityResult, node_map: Dict[str, Node]
    ) -> str:
        """Synthesize a one-paragraph definition for a community."""
        members = [node_map[f] for f in sorted(community.file_ids) if f in node_map]
        if not members:
            return "Empty community with no scanned files."
        top_dir = dominant_directory(set(community.file_ids))
        langs = Counter(n.language for n in members)
        top_lang, _ = langs.most_common(1)[0]
        symbols: List[str] = []
        for node in members:
            symbols.extend(s.name for s in node.symbols)
        top_symbols = ", ".join(f"`{s}`" for s in sorted(set(symbols))[:8]) or "no extracted symbols"
        docs = [] if self._privacy else [
            cleaned for n in members
            if n.doc and (cleaned := _clean_purpose(n.doc.split("\n")[0]))
        ]
        doc_hint = f" Documented purpose: {docs[0][:160]}." if docs else ""
        core = max(members, key=lambda n: len(n.symbols), default=None)
        core_hint = ""
        if core is not None and core.symbols:
            core_hint = f" Core file: `{core.node_id}` ({len(core.symbols)} symbols)."
        return (
            f"This community groups {len(members)} file(s) rooted at `{top_dir}` "
            f"with dominant language {top_lang} (cohesion {community.cohesion:.2f}). "
            f"Central symbols: {top_symbols}.{core_hint}{doc_hint}"
        )

    def _file_row(
        self, fid: str, node_map: Dict[str, Node], layers: Optional[Dict[str, str]]
    ) -> str:
        """Return a markdown table row for a single file, or empty string."""
        node = node_map.get(fid)
        if node is None:
            return ""
        layer = (layers or {}).get(fid, "-")
        doc = "yes" if node.doc else "no"
        return (
            f"| `{_escape(fid)}` | {node.language} | {layer} | "
            f"{len(node.symbols)} | {doc} |"
        )

    def _build_grouped_files(
        self,
        members: List[str],
        node_map: Dict[str, Node],
        layers: Optional[Dict[str, str]],
        max_files: int,
    ) -> List[str]:
        """List oversized communities grouped by directory within budget."""
        groups: Dict[str, List[str]] = {}
        for fid in members:
            groups.setdefault(os.path.dirname(fid) or ".", []).append(fid)
        ordered = sorted(groups, key=lambda d: (-len(groups[d]), d))
        for dir_files in groups.values():
            dir_files.sort()
        shown_per_dir: Dict[str, List[str]] = {d: [] for d in ordered}
        shown = 0
        progress = True
        while shown < max_files and progress:
            progress = False
            for dirname in ordered:
                if shown >= max_files:
                    break
                remaining = [f for f in groups[dirname] if f not in shown_per_dir[dirname]]
                if remaining:
                    shown_per_dir[dirname].append(remaining[0])
                    shown += 1
                    progress = True
        lines: List[str] = []
        for dirname in ordered:
            dir_files = groups[dirname]
            visible = shown_per_dir[dirname]
            if not visible:
                continue
            lines.append(f"### `{_escape(dirname)}` ({len(dir_files)} files)")
            lines.append("")
            lines.append("| File | Language | Layer | Symbols | Doc |")
            lines.append("|------|----------|-------|---------|-----|")
            for fid in visible:
                row = self._file_row(fid, node_map, layers)
                if row:
                    lines.append(row)
            lines.append("")
        if shown < len(members):
            lines.append(
                f"*... and {len(members) - shown} more files in this community.*"
            )
            lines.append("")
        return lines

    def _build_community_page(
        self,
        community: CommunityResult,
        node_map: Dict[str, Node],
        resolved: List[Edge],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        connections: List[Dict[str, object]],
    ) -> str:
        """Build the synthesis page for a single community."""
        max_files = self._config.WIKI_MAX_FILES_PER_PAGE
        max_symbols = self._config.WIKI_MAX_SYMBOLS_PER_PAGE
        members = sorted(community.file_ids)
        lines: List[str] = [
            f"# {community.label}",
            "",
            f"*Community {community.community_id} | {len(members)} files | "
            f"cohesion {community.cohesion:.2f}*",
            "",
            "## Definition",
            "",
            self._definition_for(community, node_map),
            "",
            "## Files",
            "",
        ]
        if len(members) > max_files:
            lines.extend(self._build_grouped_files(members, node_map, layers, max_files))
        else:
            lines.extend([
                "| File | Language | Layer | Symbols | Doc |",
                "|------|----------|-------|---------|-----|",
            ])
            for fid in members:
                row = self._file_row(fid, node_map, layers)
                if row:
                    lines.append(row)
        lines.append("")

        lines.extend(["## Key Symbols", ""])
        shown = 0
        for fid in members:
            node = node_map.get(fid)
            if node is None:
                continue
            for sym in sorted(node.symbols, key=lambda s: s.line):
                if shown >= max_symbols:
                    break
                doc = ""
                if sym.doc and not self._privacy:
                    doc = f" - {_escape(sym.doc.splitlines()[0][:100])}"
                sig = f" `{_escape(sym.signature[:80])}`" if sym.signature else ""
                lines.append(f"- `{_escape(sym.name)}` ({sym.kind}, `{_escape(fid)}:{sym.line}`){sig}{doc}")
                shown += 1
            if shown >= max_symbols:
                break
        if shown == 0:
            lines.append("- No symbols extracted in this community.")
        lines.append("")

        internal = sum(1 for e in resolved if e.source in community.file_ids and e.target in community.file_ids)
        external = sum(1 for e in resolved if (e.source in community.file_ids) != (e.target in community.file_ids))
        lines.extend([
            "## Internal vs External Edges",
            "",
            f"- Internal resolved imports (EXTRACTED): {internal}",
            f"- Cross-boundary resolved imports (EXTRACTED): {external}",
            "",
        ])

        lines.extend(["## Connections", ""])
        scoped = [
            c for c in connections
            if c.get("community_a") == community.community_id
            or c.get("community_b") == community.community_id
        ]
        if scoped:
            for conn in scoped[:10]:
                lines.append(
                    f"- [{conn['confidence']}] {conn['connection_type']} "
                    f"community {conn['community_a']} <-> {conn['community_b']} "
                    f"(strength {conn['strength']}): {_escape(str(conn['explanation']))}"
                )
        else:
            lines.append("- No cross-community bridges recorded. This community is self-contained.")
        lines.append("")

        lines.extend(["## Risks", ""])
        risks: List[str] = []
        member_set = set(members)
        for finding in findings or []:
            if finding.file_path in member_set:
                scope = ""
                node = node_map.get(finding.file_path)
                if node is not None:
                    best = ""
                    best_line = -1
                    for sym in node.symbols:
                        if sym.line <= finding.line and sym.line > best_line:
                            best = sym.name
                            best_line = sym.line
                    if best:
                        scope = f" (in `{_escape(best)}`)"
                risks.append(
                    f"- [{finding.severity}] `{finding.file_path}:{finding.line}`{scope} "
                    f"{finding.rule_id}: {_escape(finding.description)} "
                    f"Fix: {fix_hint_for(finding)}"
                )
        if analysis_v2:
            if analysis_v2.taint and analysis_v2.taint.paths:
                for path in analysis_v2.taint.paths:
                    if path.source_file in member_set or path.sink_file in member_set:
                        risks.append(
                            f"- [taint {path.severity}] `{path.source_file}` -> `{path.sink_file}` "
                            f"via `{path.dangerous_import}` ({path.hops} hops)"
                        )
            for cycle in analysis_v2.cycles or []:
                if member_set.intersection(cycle.cycle):
                    loop = list(cycle.cycle) + ([cycle.cycle[0]] if cycle.cycle else [])
                    risks.append(f"- [cycle] {' -> '.join(f'`{f}`' for f in loop)}")
            for violation in analysis_v2.layer_violations or []:
                if violation.source_file in member_set or violation.target_file in member_set:
                    risks.append(
                        f"- [layer {violation.severity}] `{violation.source_file}` "
                        f"({violation.source_layer}) -> `{violation.target_file}` "
                        f"({violation.target_layer})"
                    )
            for issue in analysis_v2.dataflow_issues or []:
                if issue.file_path in member_set:
                    risks.append(
                        f"- [dataflow {issue.kind}] `{issue.file_path}:{issue.line}` "
                        f"`{issue.function}` `{issue.variable}`: "
                        f"{_escape(issue.description)}"
                    )
        lines.extend(risks[:15] if risks else ["- No scoped security, taint, cycle, or layer risks."])
        lines.append("")

        lines.extend(["## Open Questions", ""])
        questions = self._questions_for(community, node_map, member_set, analysis_v2)
        for question in questions:
            lines.append(f"- {question}")
        lines.append("")

        lines.extend(["## Sources", ""])
        for fid in members[:max_files]:
            lines.append(f"- `{_escape(fid)}`")
        if len(members) > max_files:
            lines.append(f"- *... and {len(members) - max_files} more*")
        lines.append("")
        return "\n".join(lines)

    def _questions_for(
        self,
        community: CommunityResult,
        node_map: Dict[str, Node],
        member_set: Set[str],
        analysis_v2: Optional[AnalysisResultV2],
    ) -> List[str]:
        """Generate deterministic open questions for a community."""
        questions: List[str] = []
        undocumented = [f for f in member_set if f in node_map and not node_map[f].doc]
        if undocumented:
            questions.append(
                f"Why do {len(undocumented)} file(s) lack file-level docs "
                f"(e.g. `{sorted(undocumented)[0]}`)? What purpose do they serve?"
            )
        if analysis_v2 and analysis_v2.cycles:
            for cycle in analysis_v2.cycles:
                if member_set.intersection(cycle.cycle):
                    questions.append(
                        "Can the cycle " + " -> ".join(f"`{f}`" for f in cycle.cycle) + " be broken with an interface?"
                    )
                    break
        if analysis_v2 and analysis_v2.taint and analysis_v2.taint.paths:
            for path in analysis_v2.taint.paths:
                if path.source_file in member_set:
                    questions.append(
                        f"Is the dangerous import `{path.dangerous_import}` in "
                        f"`{path.source_file}` still required, or can it be isolated?"
                    )
                    break
        questions.append(
            f"What would break if the most connected file in {community.label} changed?"
        )
        questions.append(
            f"Should {community.label} be split, given cohesion {community.cohesion:.2f}?"
        )
        return questions[:5]

    def _large_files(self, nodes: List[Node], project_root: str) -> List[str]:
        """Return node ids whose on-disk size exceeds the large-file threshold."""
        threshold = self._config.WIKI_LARGE_FILE_KB * 1024
        root = Path(project_root)
        large: List[str] = []
        for node in nodes:
            try:
                if (root / node.node_id).stat().st_size > threshold:
                    large.append(node.node_id)
            except OSError:
                continue
        return sorted(large)

    def _build_index(
        self,
        nodes: List[Node],
        resolved: List[Edge],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        communities: List[CommunityResult],
        pages: List[Tuple[CommunityResult, str]],
        connections: List[Dict[str, object]],
        project_name: str,
        project_root: str,
    ) -> str:
        """Build the wiki entry point with overview and navigation."""
        total_symbols = sum(len(n.symbols) for n in nodes)
        langs = sorted({n.language for n in nodes})
        documented = sum(1 for n in nodes if n.doc)
        coverage = (documented / max(len(nodes), 1)) * 100.0
        token_estimate = self._estimate_tokens(nodes, connections)
        display = _display_names(communities)
        large = self._large_files(nodes, project_root)
        lines: List[str] = [
            "# Second Brain",
            "",
            f"*Last synthesized: {time.strftime('%Y-%m-%d')} | {len(nodes)} files | "
            f"{len(pages)} concept pages | offline, zero tokens*",
            "",
            "> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).",
            "> Start here, then open one community page. Prefer grep over full reads.",
            "",
            "## Vault Overview",
            "",
            self._overview_paragraph(nodes, analysis, layers, findings, analysis_v2, communities),
            "",
            self._connective_paragraph(communities, connections),
            "",
            self._questions_paragraph(analysis, findings, analysis_v2, coverage),
            "",
            "## Stats",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Files | {len(nodes)} |",
            f"| Symbols | {total_symbols} |",
            f"| Resolved imports | {len(resolved)} |",
            f"| Languages | {', '.join(langs) if langs else '-'} |",
            f"| Communities | {len(communities)} |",
            f"| Doc coverage | {coverage:.0f}% ({documented}/{len(nodes)} files) |",
            f"| Security findings | {len(findings or [])} |",
            f"| Estimated read cost | ~{token_estimate} tokens (chars/4, offline so $0) |",
        ]
        if large:
            shown = ", ".join(f"`{f.split('/')[-1]}`" for f in large[:5])
            extra = f" (+{len(large) - 5} more)" if len(large) > 5 else ""
            lines.append(
                f"| Large files (>{self._config.WIKI_LARGE_FILE_KB}KB, maybe generated) "
                f"| {len(large)}: {shown}{extra} |"
            )
        lines.append("")
        lines.extend([
            "## Reading Order",
            "",
            "1. Skim Stats and God Nodes below for blast radius.",
            "2. Open the largest community page first, then follow Connections.",
            "3. Use `queries.md` for the next question; log the answer there.",
            "",
            "```",
            "grep -rn '<keyword>' index.md community_*.md",
            f"readmenator query \"<question>\" --target {project_name}",
            "```",
            "",
            "## Concept Wiki",
            "",
        ])
        for community, filename in pages:
            name = display.get(community.community_id, community.label)
            lines.append(
                f"- [{name} ({community.size} files, cohesion {community.cohesion:.2f})](./{filename})"
            )
        lines.append("")
        lines.extend(["## God Nodes", "", "| File | Score |", "|------|-------|"])
        gods = (analysis.god_nodes if analysis and analysis.god_nodes else [])[:5]
        large_set = set(large)
        if gods:
            for nid, score in gods:
                tag = " (large, maybe generated)" if nid in large_set else ""
                lines.append(f"| `{_escape(nid)}` | {score:.1f}{tag} |")
        else:
            lines.append("| - | - |")
        lines.append("")
        lines.extend(["## Strongest Connections", ""])
        if connections:
            for conn in connections[:10]:
                lines.append(
                    f"- {conn['community_a']} -> {conn['community_b']}: "
                    f"{conn['connection_type']} (strength {conn['strength']}, {conn['confidence']})"
                )
        else:
            lines.append("- No cross-community connections recorded.")
        lines.append("")
        lines.extend([
            "## Navigation Tips",
            "",
            "- Obsidian Graph View works: every community page links back here.",
            "- `connections.json` is machine-readable for GraphRAG pipelines.",
            "- `REPORT.md` states what was extracted vs inferred and current limits.",
            "- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).",
            "",
        ])
        return "\n".join(lines)

    def _overview_paragraph(
        self,
        nodes: List[Node],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        communities: List[CommunityResult],
    ) -> str:
        """Synthesize the central preoccupations paragraph."""
        top_gods = analysis.god_nodes[:3] if analysis and analysis.god_nodes else []
        seen: Set[str] = set()
        names: List[str] = []
        for nid, _ in top_gods:
            base = nid.split("/")[-1]
            if base in seen:
                base = nid
            seen.add(nid.split("/")[-1])
            names.append(f"`{base}`")
        gods = ", ".join(names) or "no dominant files"
        layer_text = "unlayered"
        if layers:
            counts = Counter(layers.values())
            top = counts.most_common(1)[0]
            layer_text = f"{len(counts)} layers, dominant {top[0]} ({top[1]} files)"
        risks = len(findings or [])
        cycles = len(analysis_v2.cycles) if analysis_v2 and analysis_v2.cycles else 0
        return (
            f"The codebase centres on {gods}. Architecturally it is {layer_text} "
            f"across {len(communities)} import-based communities. "
            f"Recorded risk surface: {risks} security findings and {cycles} dependency cycles."
        )

    def _connective_paragraph(
        self, communities: List[CommunityResult], connections: List[Dict[str, object]]
    ) -> str:
        """Synthesize the connective tissue paragraph."""
        extracted = sum(1 for c in connections if c.get("confidence") == "EXTRACTED")
        inferred = sum(1 for c in connections if c.get("confidence") == "INFERRED")
        if not connections:
            return (
                "Communities are self-contained in the resolved import graph; "
                "no cross-boundary bridges were recorded."
            )
        labels = ", ".join(
            _display_names(communities).get(c.community_id, c.label)
            for c in communities[:3]
        )
        return (
            f"Surprising tissue lives between {labels}: {extracted} extracted "
            f"cross-community imports and {inferred} inferred bridges. "
            f"Follow `connections.json` sorted by strength before refactoring."
        )

    def _questions_paragraph(
        self,
        analysis: Optional[AnalysisResult],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        coverage: float,
    ) -> str:
        """Synthesize the open questions paragraph."""
        suggested = len(analysis.suggested_questions) if analysis and analysis.suggested_questions else 0
        taint = len(analysis_v2.taint.paths) if analysis_v2 and analysis_v2.taint and analysis_v2.taint.paths else 0
        return (
            f"Open work clusters around documentation ({coverage:.0f}% file coverage), "
            f"{len(findings or [])} security findings, {taint} taint paths, "
            f"and {suggested} suggested exploration questions in `queries.md`."
        )

    def _build_queries(self, analysis: Optional[AnalysisResult]) -> str:
        """Build the starter question log with feedback loop instructions."""
        lines: List[str] = [
            "# Queries",
            "",
            "Log each answered question here so the wiki compounds. "
            "Format: question, answer, cited files.",
            "",
            "## Suggested",
            "",
        ]
        suggested = analysis.suggested_questions if analysis and analysis.suggested_questions else []
        if suggested:
            for question in suggested:
                lines.extend([f"### Q: {_escape(question)}", "", "- Status: unanswered", ""])
        else:
            lines.extend([
                "### Q: Which file has the largest blast radius, and why?",
                "",
                "- Status: unanswered",
                "",
            ])
        lines.extend(["## Answered", "", "- None yet. Append entries; never overwrite.", ""])
        return "\n".join(lines)

    def _build_report(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved: List[Edge],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        communities: List[CommunityResult],
        project_name: str,
        project_root: str,
    ) -> str:
        """Build the honest audit report with confidence and limits."""
        import_edges = sum(1 for e in edges if e.relation == "imports")
        inferred = len(analysis.surprising_connections) if analysis and analysis.surprising_connections else 0
        orphans = sum(1 for n in nodes if not n.doc and not any(s.doc for s in n.symbols))
        documented = sum(1 for n in nodes if n.doc)
        token_estimate = self._estimate_tokens(nodes, [])
        large = self._large_files(nodes, project_root)
        lines: List[str] = [
            "# Audit Report",
            "",
            f"*Project: {_escape(project_name)} | {time.strftime('%Y-%m-%d')} | offline, deterministic*",
            "",
            "## Confidence Trail",
            "",
            "Every edge is tagged. Extracted means parsed from source; "
            "inferred means derived heuristically; ambiguous is reported, never hidden.",
            "",
            "| Confidence | Count | Meaning |",
            "|------------|-------|---------|",
            f"| EXTRACTED | {len(resolved)} | Resolved import edges parsed from source |",
            f"| EXTRACTED | {import_edges} | Raw import statements (may include externals) |",
            f"| INFERRED | {inferred} | Surprising cross-community bridges |",
            "| AMBIGUOUS | 0 | No uncertain edges are emitted by the static scanner |",
            "",
            "## Coverage",
            "",
            f"- Files: {len(nodes)}, communities: {len(communities)}",
            f"- File doc coverage: {documented}/{len(nodes)}",
            f"- Orphans (no docs at any level): {orphans}",
            f"- Layers detected: {len(set((layers or {}).values()))}",
            f"- Security findings: {len(findings or [])}",
            f"- Large files (>{self._config.WIKI_LARGE_FILE_KB}KB, maybe generated): "
            f"{len(large)}" + (f" ({', '.join(f.split('/')[-1] for f in large[:5])})" if large else ""),
            "",
            "## Limits",
            "",
            "- Python uses the ast module; all other languages use regex parsers.",
            "- No dataflow or runtime tracing; taint follows the import graph only.",
            "- Symbol docs come from adjacent comments; missing docs are listed, not invented.",
            "- Centrality scores count every scanned file equally, including "
            "checked-in build artifacts; verify large files before refactoring.",
            "",
            "## Token Benchmark",
            "",
            f"- Wiki index plus community pages estimate: ~{token_estimate} tokens (chars/4).",
            "- Full re-read of every source file would cost strictly more on any "
            "non-trivial project; this wiki is the cheaper entry point.",
            "- Generation cost: $0, offline, no network calls.",
            "",
            "## Reproduce",
            "",
            "```",
            "readmenator . --rebuild",
            "readmenator . wiki",
            "```",
            "",
        ]
        return "\n".join(lines)

    def _estimate_tokens(
        self, nodes: List[Node], connections: List[Dict[str, object]]
    ) -> int:
        """Estimate wiki read cost as characters divided by four."""
        chars = sum(len(n.node_id) + len(n.doc or "") for n in nodes)
        chars += sum(len(s.name) + len(s.doc or "") for n in nodes for s in n.symbols)
        chars += len(connections) * 120
        chars += 2000
        return max(chars // 4, 1)

    @staticmethod
    def _write(path: Path, content: str) -> None:
        """Write wiki file content with UTF-8 encoding."""
        path.write_text(content, encoding="utf-8")
