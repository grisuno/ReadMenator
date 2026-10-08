"""Self-contained interactive system maps for the knowledge graph.

Builds typed intermediate representations for five diagram kinds
(architecture, workflow, sequence, dataflow, lifecycle) from scanned
nodes and edges, validates each map deterministically, and renders a
single self-contained HTML document with inline SVG, search, focus,
reach tracing, route probing, role comparison, guided views,
presentation stage, themes, presets, keyboard access, deep links,
finite motion, and client-side export.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple

from readmenator._config import Config

_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_MD_MARK_RE = re.compile(r"[`*_]")
_PAGE_PART_RE = re.compile(r"^(?P<base>.+?)_p(?P<page>\d+)\.md$")
from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding


def _escape_markup(value: str) -> str:
    """Escape text for HTML and tooltip embedding.

    Args:
        value: Raw text.

    Returns:
        Escaped text safe for markup contexts.
    """
    return html.escape(value, quote=True)


def _json_payload(payload: object) -> str:
    """Serialize a payload for safe inline script embedding.

    Args:
        payload: JSON-serializable payload.

    Returns:
        JSON text with angle brackets unicode-escaped.
    """
    return json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")


def _role_color(role: str, config: Config) -> str:
    """Return the stroke color for a semantic role.

    Args:
        role: Semantic role identifier.
        config: Central settings holding the role palette.

    Returns:
        Hex color string for the role.
    """
    return dict(config.DIAGRAM_ROLE_COLORS).get(role, "#94a3b8")


@dataclass
class MapNode:
    """Single authored node in a system map.

    Attributes:
        node_id: Stable identifier derived from the file path.
        label: Short display label.
        role: Semantic role used for color and lens comparison.
        group: Lane or layer grouping used for layout.
        detail: Supporting detail shown in the passport panel.
        x: Deterministic horizontal canvas coordinate.
        y: Deterministic vertical canvas coordinate.
        language: Programming language of the source file.
        doc: File-level documentation string.
        symbols: Symbol records with name, kind, line, signature, doc.
        symbol_total: Total symbol count before per-node truncation.
    """

    node_id: str
    label: str
    role: str
    group: str
    detail: str = ""
    x: int = 0
    y: int = 0
    language: str = ""
    doc: str = ""
    symbols: List[Dict[str, str]] = field(default_factory=list)
    symbol_total: int = 0
    community: int = -1
    community_label: str = ""


@dataclass
class MapEdge:
    """Single authored directed relationship in a system map.

    Attributes:
        source: Source node identifier.
        target: Target node identifier.
        label: Semantic relationship label.
        kind: Relationship kind used for styling.
    """

    source: str
    target: str
    label: str = ""
    kind: str = "imports"


@dataclass
class MapView:
    """Single guided chapter over authored topology.

    Attributes:
        view_id: Stable chapter identifier usable in deep links.
        title: Chapter title.
        focus: Ordered node identifiers highlighted by the chapter.
        description: Supporting explanation for the chapter.
    """

    view_id: str
    title: str
    focus: List[str] = field(default_factory=list)
    description: str = ""


@dataclass
class SystemMap:
    """Typed intermediate representation of one diagram.

    Attributes:
        kind: Diagram kind identifier.
        title: Human-readable diagram title.
        nodes: Authored nodes with deterministic coordinates.
        edges: Authored directed relationships.
        views: Guided chapters over the topology.
        meta: Generation metadata for receipts and exports.
    """

    kind: str
    title: str
    nodes: List[MapNode] = field(default_factory=list)
    edges: List[MapEdge] = field(default_factory=list)
    views: List[MapView] = field(default_factory=list)
    meta: Dict[str, str] = field(default_factory=dict)


@dataclass
class MapDiagnostic:
    """Single machine-readable validation diagnostic.

    Attributes:
        rule: Stable rule code.
        subject: Identifier of the offending subject.
        evidence: Measured evidence describing the failure.
        repair: Supported repair control for the failure.
    """

    rule: str
    subject: str
    evidence: str
    repair: str


@dataclass
class MapReceipt:
    """Deterministic validation receipt for a system map.

    Attributes:
        passed: True when zero errors were found.
        checks: Names of checks that were executed.
        errors: Error diagnostics blocking delivery.
        warnings: Non-blocking advisory diagnostics.
    """

    passed: bool
    checks: List[str] = field(default_factory=list)
    errors: List[MapDiagnostic] = field(default_factory=list)
    warnings: List[MapDiagnostic] = field(default_factory=list)


@dataclass
class MapDelta:
    """Before and after comparison between two maps of the same kind.

    Attributes:
        kind: Diagram kind that was compared.
        added: Node identifiers present only in the head map.
        removed: Node identifiers present only in the base map.
        changed: Node identifiers with altered role, group, or label.
        moved: Node identifiers with altered coordinates.
        rerouted: Edge pairs present only in one of the two maps.
    """

    kind: str
    added: List[str] = field(default_factory=list)
    removed: List[str] = field(default_factory=list)
    changed: List[str] = field(default_factory=list)
    moved: List[str] = field(default_factory=list)
    rerouted: List[str] = field(default_factory=list)


class SystemMapValidator:
    """Deterministic validator for system map intermediate representations."""

    def __init__(self, config: Config) -> None:
        """Initialise the validator with application configuration.

        Args:
            config: Central settings for map size limits.
        """
        self._config = config

    def _effective_canvas(self, system_map: SystemMap) -> Tuple[int, int]:
        """Return the canvas bounds applying per-map full-mode growth.

        Args:
            system_map: Map carrying optional canvas_width/canvas_height metadata.

        Returns:
            Effective canvas width and height pair.
        """
        width = self._config.DIAGRAM_CANVAS_WIDTH
        height = self._config.DIAGRAM_CANVAS_HEIGHT
        try:
            width = max(width, int(str(system_map.meta.get("canvas_width", width))))
        except ValueError:
            pass
        try:
            height = max(height, int(str(system_map.meta.get("canvas_height", height))))
        except ValueError:
            pass
        return width, height

    def validate(self, system_map: SystemMap) -> MapReceipt:
        """Validate a system map and return a deterministic receipt.

        Args:
            system_map: Map intermediate representation to validate.

        Returns:
            Validation receipt with executed checks and diagnostics.
        """
        checks = [
            "schema",
            "unique_ids",
            "endpoints",
            "connectivity",
            "size_bounds",
            "canvas_bounds",
            "overlap",
            "label_clearance",
            "export_ready",
        ]
        errors: List[MapDiagnostic] = []
        warnings: List[MapDiagnostic] = []
        if system_map.kind not in tuple(self._config.DIAGRAM_KINDS):
            errors.append(
                MapDiagnostic(
                    rule="D000",
                    subject=system_map.kind,
                    evidence="unknown diagram kind",
                    repair="set kind to one of the five supported kinds",
                )
            )
            return MapReceipt(passed=False, checks=checks, errors=errors, warnings=warnings)
        if not system_map.nodes:
            errors.append(
                MapDiagnostic(
                    rule="D003",
                    subject=system_map.kind,
                    evidence="map contains zero nodes",
                    repair="include at least one authored node",
                )
            )
            return MapReceipt(passed=False, checks=checks, errors=errors, warnings=warnings)
        seen: Set[str] = set()
        for node in system_map.nodes:
            if node.node_id in seen:
                errors.append(
                    MapDiagnostic(
                        rule="D001",
                        subject=node.node_id,
                        evidence="duplicate node identifier",
                        repair="assign a unique stable identifier",
                    )
                )
            seen.add(node.node_id)
            if not node.label.strip():
                errors.append(
                    MapDiagnostic(
                        rule="D006",
                        subject=node.node_id,
                        evidence="empty node label",
                        repair="provide a short domain label",
                    )
                )
        for edge in system_map.edges:
            if edge.source not in seen or edge.target not in seen:
                errors.append(
                    MapDiagnostic(
                        rule="D002",
                        subject=edge.source + "->" + edge.target,
                        evidence="edge references an unknown endpoint",
                        repair="point the edge at authored node identifiers",
                    )
                )
            if edge.source == edge.target:
                warnings.append(
                    MapDiagnostic(
                        rule="D007",
                        subject=edge.source,
                        evidence="self-loop relationship",
                        repair="remove the loop or model it as a retry transition",
                    )
                )
        full = str(system_map.meta.get("full", "")).lower() == "true"
        if not full and len(system_map.nodes) > self._config.DIAGRAM_MAX_NODES:
            errors.append(
                MapDiagnostic(
                    rule="D004",
                    subject=system_map.kind,
                    evidence="node count "
                    + str(len(system_map.nodes))
                    + " exceeds limit "
                    + str(self._config.DIAGRAM_MAX_NODES),
                    repair="reduce scope to the primary path plus side branches",
                )
            )
        if not full and len(system_map.edges) > self._config.DIAGRAM_MAX_EDGES:
            errors.append(
                MapDiagnostic(
                    rule="D008",
                    subject=system_map.kind,
                    evidence="edge count "
                    + str(len(system_map.edges))
                    + " exceeds limit "
                    + str(self._config.DIAGRAM_MAX_EDGES),
                    repair="remove low-value edges before adding routing detail",
                )
            )
        if len(system_map.nodes) > 1 and not system_map.edges:
            warnings.append(
                MapDiagnostic(
                    rule="D005",
                    subject=system_map.kind,
                    evidence="multiple nodes without relationships",
                    repair="author the primary path between core nodes",
                )
            )
        positions: Set[Tuple[int, int]] = set()
        canvas_w, canvas_h = self._effective_canvas(system_map)
        for node in system_map.nodes:
            if node.x < 0 or node.y < 0:
                errors.append(
                    MapDiagnostic(
                        rule="D009",
                        subject=node.node_id,
                        evidence="negative canvas coordinate",
                        repair="re-run the deterministic layout",
                    )
                )
            if node.x > canvas_w or node.y > canvas_h:
                errors.append(
                    MapDiagnostic(
                        rule="D010",
                        subject=node.node_id,
                        evidence="coordinate outside canvas bounds",
                        repair="re-run the deterministic layout",
                    )
                )
            key = (node.x, node.y)
            if key in positions:
                errors.append(
                    MapDiagnostic(
                        rule="D011",
                        subject=node.node_id,
                        evidence="overlapping node position",
                        repair="spread nodes across lanes before delivery",
                    )
                )
            positions.add(key)
            if len(node.label) > self._config.DIAGRAM_MAX_LABEL_CHARS * 2:
                warnings.append(
                    MapDiagnostic(
                        rule="D012",
                        subject=node.node_id,
                        evidence="label exceeds readable length",
                        repair="shorten wording while preserving meaning",
                    )
                )
        view_ids = [view.view_id for view in system_map.views]
        if len(set(view_ids)) != len(view_ids):
            errors.append(
                MapDiagnostic(
                    rule="D013",
                    subject=system_map.kind,
                    evidence="duplicate guided view identifier",
                    repair="assign unique chapter identifiers",
                )
            )
        if len(system_map.views) > self._config.DIAGRAM_MAX_VIEWS:
            errors.append(
                MapDiagnostic(
                    rule="D014",
                    subject=system_map.kind,
                    evidence="too many guided views",
                    repair="keep at most the configured chapter count",
                )
            )
        for view in system_map.views:
            for focused in view.focus:
                if focused not in seen:
                    errors.append(
                        MapDiagnostic(
                            rule="D015",
                            subject=view.view_id,
                            evidence="chapter references unknown node " + focused,
                            repair="focus only authored node identifiers",
                        )
                    )
        return MapReceipt(
            passed=not errors, checks=checks, errors=errors, warnings=warnings
        )


class SystemMapBuilder:
    """Builds deterministic system maps from the scanned knowledge graph."""

    _GROUP_ORDER: Tuple[str, ...] = (
        "presentation",
        "business_logic",
        "data_access",
        "infrastructure",
        "testing",
        "utility",
    )

    _ROLE_BY_GROUP: Tuple[Tuple[str, str], ...] = (
        ("presentation", "frontend"),
        ("business_logic", "backend"),
        ("data_access", "database"),
        ("infrastructure", "cloud"),
        ("testing", "test"),
        ("utility", "core"),
    )

    _KIND_TITLES: Tuple[Tuple[str, str], ...] = (
        ("architecture", "Runtime Architecture"),
        ("workflow", "Delivery Workflow"),
        ("sequence", "Request Sequence"),
        ("dataflow", "Data Flow"),
        ("lifecycle", "Change Lifecycle"),
    )

    def __init__(self, config: Config) -> None:
        """Initialise the builder with application configuration.

        Args:
            config: Central settings for layout geometry and limits.
        """
        self._config = config
        self._validator = SystemMapValidator(config)

    def supported_kinds(self) -> List[str]:
        """Return the supported diagram kind identifiers.

        Returns:
            Ordered list of the configured diagram kinds.
        """
        return list(self._config.DIAGRAM_KINDS)

    def _is_full(self, full: Optional[bool]) -> bool:
        """Return whether full-map scope applies for this build.

        Args:
            full: Explicit caller override, None honors configuration.

        Returns:
            True when every scanned file must be included without truncation.
        """
        if full is not None:
            return bool(full)
        return bool(self._config.DIAGRAM_FULL_MODE)

    def build(
        self,
        nodes: Sequence[Node],
        edges: Sequence[Edge],
        resolved_edges: Optional[Sequence[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[Sequence[SecurityFinding]] = None,
        analysis: Optional[AnalysisResult] = None,
        kind: str = "architecture",
        full: Optional[bool] = None,
    ) -> SystemMap:
        """Build one deterministic system map of the requested kind.

        Args:
            nodes: Scanned file nodes.
            edges: Raw import edges.
            resolved_edges: Project-internal resolved import edges.
            layers: Mapping of file identifier to architectural layer.
            findings: Security findings used for sensitivity marking.
            analysis: Graph analysis used for centrality ranking.
            kind: Diagram kind identifier.
            full: True includes every file with a grown canvas, None honors config.

        Returns:
            Validated system map intermediate representation.
        """
        normalized = kind if kind in self.supported_kinds() else "architecture"
        use_full = self._is_full(full)
        if normalized == "architecture":
            built = self._build_architecture(nodes, resolved_edges or edges, layers, findings, analysis, use_full)
        elif normalized == "workflow":
            built = self._build_workflow(nodes, resolved_edges or edges, layers, findings, use_full)
        elif normalized == "sequence":
            built = self._build_sequence(nodes, resolved_edges or edges, layers, analysis, use_full)
        elif normalized == "dataflow":
            built = self._build_dataflow(nodes, resolved_edges or edges, layers, findings, use_full)
        else:
            built = self._build_lifecycle(nodes, resolved_edges or edges, layers, findings, use_full)
        self._annotate_communities(built, analysis)
        return built

    @staticmethod
    def _annotate_communities(system_map: "SystemMap", analysis: Optional[AnalysisResult]) -> None:
        """Tag map nodes with their code community so renderers can color clusters.

        Args:
            system_map: Freshly built map whose nodes are annotated in place.
            analysis: Graph analysis holding detected communities.
        """
        if analysis is None:
            return
        owner: Dict[str, Tuple[int, str]] = {}
        for community in analysis.communities:
            for file_id in community.file_ids:
                owner[file_id] = (community.community_id, community.label)
        for node in system_map.nodes:
            if node.node_id in owner:
                node.community, node.community_label = owner[node.node_id]

    def build_all(
        self,
        nodes: Sequence[Node],
        edges: Sequence[Edge],
        resolved_edges: Optional[Sequence[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[Sequence[SecurityFinding]] = None,
        analysis: Optional[AnalysisResult] = None,
        full: Optional[bool] = None,
    ) -> Dict[str, SystemMap]:
        """Build all five diagram kinds deterministically.

        Args:
            nodes: Scanned file nodes.
            edges: Raw import edges.
            resolved_edges: Project-internal resolved import edges.
            layers: Mapping of file identifier to architectural layer.
            findings: Security findings used for sensitivity marking.
            analysis: Graph analysis used for centrality ranking.
            full: True includes every file with a grown canvas, None honors config.

        Returns:
            Mapping of diagram kind to system map.
        """
        result: Dict[str, SystemMap] = {}
        for kind in self.supported_kinds():
            result[kind] = self.build(
                nodes, edges, resolved_edges, layers, findings, analysis, kind, full
            )
        return result

    def compare(self, base: SystemMap, head: SystemMap) -> MapDelta:
        """Compare two maps of the same kind as before, delta, and after.

        Args:
            base: Baseline system map.
            head: Revised system map.

        Returns:
            Deterministic delta with added, removed, changed, moved, rerouted facts.
        """
        base_nodes = {node.node_id: node for node in base.nodes}
        head_nodes = {node.node_id: node for node in head.nodes}
        added = sorted([nid for nid in head_nodes if nid not in base_nodes])
        removed = sorted([nid for nid in base_nodes if nid not in head_nodes])
        changed: List[str] = []
        moved: List[str] = []
        for nid in sorted(set(base_nodes).intersection(head_nodes)):
            before = base_nodes[nid]
            after = head_nodes[nid]
            if (
                before.label != after.label
                or before.role != after.role
                or before.group != after.group
            ):
                changed.append(nid)
            if before.x != after.x or before.y != after.y:
                moved.append(nid)
        base_routes = {edge.source + "->" + edge.target for edge in base.edges}
        head_routes = {edge.source + "->" + edge.target for edge in head.edges}
        rerouted = sorted(list((base_routes ^ head_routes)))
        return MapDelta(
            kind=head.kind,
            added=added,
            removed=removed,
            changed=changed,
            moved=moved,
            rerouted=rerouted,
        )

    def _title_for(self, kind: str) -> str:
        """Return the display title for a diagram kind.

        Args:
            kind: Diagram kind identifier.

        Returns:
            Human-readable diagram title.
        """
        for candidate, title in self._KIND_TITLES:
            if candidate == kind:
                return title
        return "System Map"

    def _role_for(self, group: str, sensitive: bool) -> str:
        """Return the semantic role for a group with sensitivity override.

        Args:
            group: Architectural layer group name.
            sensitive: True when the file carries elevated findings.

        Returns:
            Semantic role identifier.
        """
        if sensitive:
            return "security"
        for candidate, role in self._ROLE_BY_GROUP:
            if candidate == group:
                return role
        return "external"

    def _sensitive_files(
        self, findings: Optional[Sequence[SecurityFinding]]
    ) -> Set[str]:
        """Return files carrying elevated severity findings.

        Args:
            findings: Security findings to inspect.

        Returns:
            Set of file paths with critical or high severity.
        """
        sensitive: Set[str] = set()
        for finding in findings or []:
            if finding.severity in ("critical", "high"):
                sensitive.add(finding.file_path)
        return sensitive

    def _ranked_file_ids(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        analysis: Optional[AnalysisResult],
    ) -> List[str]:
        """Rank file identifiers by centrality then symbol count.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges used for degree scoring.
            analysis: Optional analysis with god node scores.

        Returns:
            File identifiers ordered by importance.
        """
        scores: Dict[str, float] = {}
        if analysis is not None:
            for nid, score in analysis.god_nodes:
                scores[nid] = float(score)
        degree: Dict[str, int] = {}
        for edge in links:
            degree[edge.source] = degree.get(edge.source, 0) + 1
            degree[edge.target] = degree.get(edge.target, 0) + 1
        ranked = sorted(
            list(nodes),
            key=lambda n: (
                -scores.get(n.node_id, 0.0),
                -degree.get(n.node_id, 0),
                -len(n.symbols),
                n.node_id,
            ),
        )
        return [node.node_id for node in ranked]

    def _select_primary(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        analysis: Optional[AnalysisResult],
        full: bool = False,
    ) -> List[Node]:
        """Select the primary node scope honoring the configured limit.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges used for ranking.
            analysis: Optional analysis with centrality scores.
            full: True returns every ranked node without truncation.

        Returns:
            Primary nodes in deterministic ranked order.
        """
        ordered_ids = self._ranked_file_ids(nodes, links, analysis)
        by_id = {node.node_id: node for node in nodes}
        if full:
            return [by_id[nid] for nid in ordered_ids if nid in by_id]
        limit = max(1, self._config.DIAGRAM_MAX_NODES)
        selected = [by_id[nid] for nid in ordered_ids[:limit] if nid in by_id]
        return selected

    def _internal_links(
        self, edges: Sequence[Edge], selected: Set[str], full: bool = False
    ) -> List[Edge]:
        """Filter edges to project-internal links between selected files.

        Args:
            edges: Candidate edges.
            selected: Selected file identifiers.
            full: True keeps every internal edge without truncation.

        Returns:
            Deterministically ordered internal edges.
        """
        kept = [
            edge
            for edge in edges
            if edge.source in selected and edge.target in selected
        ]
        kept.sort(key=lambda e: (e.source, e.target, e.relation))
        if full:
            return kept
        return kept[: max(0, self._config.DIAGRAM_MAX_EDGES)]

    def _symbol_records(self, node: Node) -> List[Dict[str, str]]:
        """Build truncated symbol records for map documentation payloads.

        Args:
            node: Scanned file node with extracted symbols.

        Returns:
            Symbol records ordered by line, capped by configuration.
        """
        cap = max(1, self._config.DIAGRAM_MAP_SYMBOLS_PER_NODE)
        ordered = sorted(node.symbols, key=lambda s: (s.line, s.name))
        return [
            {
                "name": symbol.name,
                "kind": symbol.kind,
                "line": str(symbol.line),
                "signature": symbol.signature,
                "doc": symbol.doc,
            }
            for symbol in ordered[:cap]
        ]

    def _short_label(self, value: str) -> str:
        """Shorten a label to the configured readable length.

        Args:
            value: Raw label text.

        Returns:
            Truncated label with length guard applied.
        """
        text = value.strip().split("/")[-1]
        limit = max(8, self._config.DIAGRAM_MAX_LABEL_CHARS)
        if len(text) <= limit:
            return text
        return text[: max(1, limit - 1)] + "+"

    def _layout_columns(
        self, items: List[Tuple[str, str]], kind: str, full: bool = False
    ) -> Dict[str, Tuple[int, int]]:
        """Compute deterministic column lane coordinates for grouped items.

        Args:
            items: Pairs of identifier and group name.
            kind: Diagram kind used only for metadata completeness.
            full: True keeps every lane and grows the canvas instead of dropping.

        Returns:
            Mapping of identifier to canvas coordinates.
        """
        del kind
        width = self._config.DIAGRAM_NODE_WIDTH
        height = self._config.DIAGRAM_NODE_HEIGHT
        col_gap = self._config.DIAGRAM_COLUMN_GAP
        row_gap = self._config.DIAGRAM_ROW_GAP
        order = list(self._GROUP_ORDER)
        lanes: Dict[str, List[str]] = {}
        for nid, group in items:
            lanes.setdefault(group, []).append(nid)
        for group in lanes:
            lanes[group] = sorted(lanes[group])
        used_lanes = [group for group in order if group in lanes]
        for group in sorted(lanes):
            if group not in used_lanes:
                used_lanes.append(group)
        if not full:
            used_lanes = self._lanes_that_fit(used_lanes)
        positions: Dict[str, Tuple[int, int]] = {}
        lane_count = max(1, len(used_lanes))
        canvas_w = self._config.DIAGRAM_CANVAS_WIDTH
        canvas_h = self._config.DIAGRAM_CANVAS_HEIGHT
        margin_x = self._config.DIAGRAM_MARGIN_X
        gap = self._fitted_gap(lane_count, width, col_gap, canvas_w, margin_x)
        lane_w = width + gap
        total_w = lane_count * width + (lane_count - 1) * gap
        start_x = margin_x + max(0, (canvas_w - 2 * margin_x - total_w) // 2)
        for index, group in enumerate(used_lanes):
            members = lanes[group]
            total_h = len(members) * height + max(0, len(members) - 1) * row_gap
            start_y = max(self._config.DIAGRAM_LANE_TOP, (canvas_h - total_h) // 2)
            base_x = start_x + index * lane_w
            for row, nid in enumerate(members):
                positions[nid] = (base_x, start_y + row * (height + row_gap))
        return positions

    def _lanes_that_fit(self, lanes: List[str]) -> List[str]:
        """Drop lowest-priority lanes until columns fit the canvas width.

        Args:
            lanes: Lane names in priority order.

        Returns:
            Leading lanes whose node boxes fit the canvas width.
        """
        width = self._config.DIAGRAM_NODE_WIDTH
        margin_x = self._config.DIAGRAM_MARGIN_X
        available = self._config.DIAGRAM_CANVAS_WIDTH - 2 * margin_x
        kept = list(lanes)
        while len(kept) > 1 and len(kept) * width > available:
            kept = kept[:-1]
        return kept

    def _fitted_gap(
        self, count: int, item: int, gap: int, total: int, margin: int
    ) -> int:
        """Compress spacing deterministically so items fit the canvas.

        Args:
            count: Number of items placed along the axis.
            item: Fixed item extent along the axis.
            gap: Preferred spacing between items.
            total: Total canvas extent along the axis.
            margin: Margin reserved on each side.

        Returns:
            Spacing that keeps every item inside the canvas.
        """
        if count < 2:
            return gap
        available = total - 2 * margin - count * item
        if available < 0:
            return max(0, self._config.DIAGRAM_MIN_GAP)
        return max(
            self._config.DIAGRAM_MIN_GAP, min(gap, available // (count - 1))
        )

    def _lane_capacity(self) -> int:
        """Return the maximum members per lane fitting the canvas height.

        Returns:
            Number of node rows fitting between lane top and margin.
        """
        usable = (
            self._config.DIAGRAM_CANVAS_HEIGHT
            - self._config.DIAGRAM_LANE_TOP
            - self._config.DIAGRAM_MARGIN_Y
        )
        step = self._config.DIAGRAM_NODE_HEIGHT + self._config.DIAGRAM_ROW_GAP
        return max(1, usable // max(1, step))

    def _cap_lane_scope(
        self, ranked: List[Node], layer_of: Dict[str, str]
    ) -> List[Node]:
        """Cap ranked nodes per lane so every lane fits the canvas height.

        Args:
            ranked: Nodes in global rank order.
            layer_of: Mapping of file identifier to lane name.

        Returns:
            Scoped nodes preserving rank order within each lane.
        """
        capacity = self._lane_capacity()
        taken: Dict[str, int] = {}
        scoped: List[Node] = []
        for node in ranked:
            lane = layer_of.get(node.node_id, "utility")
            used = taken.get(lane, 0)
            if used >= capacity:
                continue
            taken[lane] = used + 1
            scoped.append(node)
        return scoped

    def _layout_sequence(self, ordered: List[str], full: bool = False) -> Dict[str, Tuple[int, int]]:
        """Compute deterministic lifeline row coordinates for sequences.

        Args:
            ordered: Participant identifiers in display order.
            full: True wraps participants across rows instead of truncating width.

        Returns:
            Mapping of identifier to canvas coordinates.
        """
        width = self._config.DIAGRAM_NODE_WIDTH
        col_gap = self._config.DIAGRAM_COLUMN_GAP
        canvas_w = self._config.DIAGRAM_CANVAS_WIDTH
        margin_x = self._config.DIAGRAM_MARGIN_X
        if not full:
            gap = self._fitted_gap(len(ordered), width, col_gap, canvas_w, margin_x)
            total_w = len(ordered) * width + max(0, len(ordered) - 1) * gap
            start_x = margin_x + max(0, (canvas_w - 2 * margin_x - total_w) // 2)
            positions: Dict[str, Tuple[int, int]] = {}
            for index, nid in enumerate(ordered):
                positions[nid] = (start_x + index * (width + gap), self._config.DIAGRAM_SEQUENCE_TOP)
            return positions
        per_row = max(1, self._sequence_capacity())
        row_step = self._config.DIAGRAM_NODE_HEIGHT + self._config.DIAGRAM_ROW_GAP
        gap = self._fitted_gap(min(len(ordered), per_row), width, col_gap, canvas_w, margin_x)
        total_w = per_row * width + max(0, per_row - 1) * gap
        start_x = margin_x + max(0, (canvas_w - 2 * margin_x - total_w) // 2)
        positions = {}
        for index, nid in enumerate(ordered):
            col = index % per_row
            row = index // per_row
            positions[nid] = (
                start_x + col * (width + gap),
                self._config.DIAGRAM_SEQUENCE_TOP + row * row_step,
            )
        return positions

    def _sequence_capacity(self) -> int:
        """Return the maximum participants fitting the canvas width.

        Returns:
            Number of lifelines fitting with minimum spacing applied.
        """
        available = (
            self._config.DIAGRAM_CANVAS_WIDTH
            - 2 * self._config.DIAGRAM_MARGIN_X
            + self._config.DIAGRAM_MIN_GAP
        )
        step = self._config.DIAGRAM_NODE_WIDTH + self._config.DIAGRAM_MIN_GAP
        return max(1, available // max(1, step))

    def _place(
        self, ranked: List[Node], layer_of: Dict[str, str], kind: str, full: bool = False
    ) -> Tuple[Dict[str, Tuple[int, int]], List[Node]]:
        """Cap lane scope and compute coordinates for placed nodes only.

        Args:
            ranked: Nodes in global rank order.
            layer_of: Mapping of file identifier to lane name.
            kind: Diagram kind used only for metadata completeness.
            full: True keeps every node without lane caps or drops.

        Returns:
            Canvas positions and the placed node subset.
        """
        scoped = list(ranked) if full else self._cap_lane_scope(ranked, layer_of)
        items = [(node.node_id, layer_of.get(node.node_id, "utility")) for node in scoped]
        positions = self._layout_columns(items, kind, full)
        placed = [node for node in scoped if node.node_id in positions]
        return positions, placed

    def _canvas_for(self, positions: Dict[str, Tuple[int, int]], full: bool = False) -> Tuple[int, int]:
        """Grow the canvas to enclose every placed node in full mode.

        Args:
            positions: Placed node coordinates.
            full: True grows beyond configured bounds, False returns configured size.

        Returns:
            Effective canvas width and height pair.
        """
        base_w = self._config.DIAGRAM_CANVAS_WIDTH
        base_h = self._config.DIAGRAM_CANVAS_HEIGHT
        if not full or not positions:
            return base_w, base_h
        need_w = max(x for x, _ in positions.values()) + self._config.DIAGRAM_NODE_WIDTH + self._config.DIAGRAM_MARGIN_X
        need_h = max(y for _, y in positions.values()) + self._config.DIAGRAM_NODE_HEIGHT + self._config.DIAGRAM_MARGIN_Y
        return max(base_w, need_w), max(base_h, need_h)

    def _meta_for(self, kind: str, placed: List[MapNode], links: int, total: int, positions: Dict[str, Tuple[int, int]], full: bool = False) -> Dict[str, str]:
        """Build generation metadata with honest scope and canvas size.

        Args:
            kind: Diagram kind identifier, unused beyond completeness.
            placed: Authored map nodes.
            links: Authored edge count.
            total: Total scanned file count.
            positions: Placed coordinates used for canvas growth.
            full: True tags the map as untruncated with a grown canvas.

        Returns:
            Metadata mapping for receipts and exports.
        """
        del kind
        canvas_w, canvas_h = self._canvas_for(positions, full)
        meta = {"scope": str(len(placed)), "total": str(total), "links": str(links)}
        if full:
            meta["full"] = "true"
            meta["canvas_width"] = str(canvas_w)
            meta["canvas_height"] = str(canvas_h)
        return meta

    def _make_views(
        self, kind: str, primary: List[str], links: Sequence[Edge]
    ) -> List[MapView]:
        """Create guided chapters from authored topology.

        Args:
            kind: Diagram kind identifier.
            primary: Ordered primary path node identifiers.
            links: Authored internal relationships.

        Returns:
            Guided chapters limited to the configured maximum.
        """
        if not primary:
            return []
        chapters: List[MapView] = []
        focus_cap = max(1, self._config.DIAGRAM_CHAPTER_FOCUS)
        chapters.append(
            MapView(
                view_id="primary-path",
                title="Primary path",
                focus=list(primary[: min(len(primary), focus_cap)]),
                description="Follow the dominant authored path first.",
            )
        )
        if len(primary) > 1:
            chapters.append(
                MapView(
                    view_id="happy-path",
                    title="Happy path",
                    focus=[primary[0], primary[len(primary) // 2], primary[-1]],
                    description="Trace the shortest authored route end to end.",
                )
            )
        outgoing: Dict[str, int] = {}
        for edge in links:
            outgoing[edge.source] = outgoing.get(edge.source, 0) + 1
        if outgoing:
            hub = sorted(outgoing.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
            chapters.append(
                MapView(
                    view_id="hub-focus",
                    title="Hub focus",
                    focus=[hub],
                    description="Inspect the most connected authored hub.",
                )
            )
        if len(primary) > 2:
            chapters.append(
                MapView(
                    view_id="side-branches",
                    title="Side branches",
                    focus=list(primary[-3:]),
                    description="Review supporting detail without losing orientation.",
                )
            )
        chapters.append(
            MapView(
                view_id="full-map",
                title="Full map",
                focus=list(primary),
                description="Restore the complete authored context.",
            )
        )
        deduped: List[MapView] = []
        seen_views: Set[str] = set()
        for chapter in chapters:
            if chapter.view_id not in seen_views:
                deduped.append(chapter)
                seen_views.add(chapter.view_id)
        return deduped[: max(1, self._config.DIAGRAM_MAX_VIEWS)]

    def _build_architecture(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
        analysis: Optional[AnalysisResult],
        full: bool = False,
    ) -> SystemMap:
        """Build the runtime architecture map from file topology.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings.
            analysis: Graph analysis.
            full: True keeps every file without truncation.

        Returns:
            Architecture system map.
        """
        selected = self._select_primary(nodes, links, analysis, full)
        layer_of_all = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        positions, selected = self._place(selected, layer_of_all, "architecture", full)
        chosen = {node.node_id for node in selected}
        kept = self._internal_links(links, chosen, full)
        sensitive = self._sensitive_files(findings)
        groups = {node.node_id: layer_of_all[node.node_id] for node in selected}
        map_nodes = [
            MapNode(
                node_id=node.node_id,
                label=self._short_label(node.label),
                role=self._role_for(groups[node.node_id], node.node_id in sensitive),
                group=groups[node.node_id],
                detail=str(len(node.symbols)) + " symbols | " + node.language,
                x=positions[node.node_id][0],
                y=positions[node.node_id][1],
                language=node.language,
                doc=node.doc,
                symbols=self._symbol_records(node),
                symbol_total=len(node.symbols),
            )
            for node in selected
        ]
        map_edges = [
            MapEdge(source=e.source, target=e.target, label=e.relation, kind=e.relation)
            for e in kept
        ]
        primary = [node.node_id for node in selected]
        views = self._make_views("architecture", primary, kept)
        return SystemMap(
            kind="architecture",
            title=self._title_for("architecture"),
            nodes=map_nodes,
            edges=map_edges,
            views=views,
            meta=self._meta_for("architecture", map_nodes, len(map_edges), len(nodes), positions, full),
        )

    def _build_workflow(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
        full: bool = False,
    ) -> SystemMap:
        """Build the delivery workflow map across architectural lanes.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings.
            full: True keeps every file without lane sampling.

        Returns:
            Workflow system map.
        """
        selected = self._select_primary(nodes, links, None, full)
        layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        if full:
            lane_nodes = list(selected)
        else:
            lane_representative: Dict[str, Node] = {}
            for node in selected:
                group = layer_of[node.node_id]
                if group not in lane_representative:
                    lane_representative[group] = node
            lane_nodes = [lane_representative[group] for group in self._GROUP_ORDER if group in lane_representative]
            if not lane_nodes:
                lane_nodes = list(selected[: min(len(selected), self._config.DIAGRAM_WORKFLOW_FALLBACK_NODES)])
        chosen = {node.node_id for node in lane_nodes}
        sensitive = self._sensitive_files(findings)
        kept = self._internal_links(links, chosen, full)
        workflow_edges: List[MapEdge] = [
            MapEdge(source=e.source, target=e.target, label=e.relation, kind=e.relation)
            for e in kept
        ]
        items = [(node.node_id, layer_of[node.node_id]) for node in lane_nodes]
        positions = self._layout_columns(items, "workflow", full)
        lane_nodes = [node for node in lane_nodes if node.node_id in positions]
        chain = [node.node_id for node in lane_nodes]
        for first, second in zip(chain, chain[1:]):
            if not any(e.source == first and e.target == second for e in workflow_edges):
                workflow_edges.append(MapEdge(source=first, target=second, label="next", kind="next"))
        placed_ids = set(chain)
        ordered_edges = sorted(
            [e for e in workflow_edges if e.source in placed_ids and e.target in placed_ids],
            key=lambda e: (e.source, e.target),
        )
        if not full:
            ordered_edges = ordered_edges[: max(0, self._config.DIAGRAM_MAX_EDGES)]
        map_nodes = [
            MapNode(
                node_id=node.node_id,
                label=self._short_label(node.label),
                role=self._role_for(layer_of[node.node_id], node.node_id in sensitive),
                group=layer_of[node.node_id],
                detail="lane " + layer_of[node.node_id],
                x=positions[node.node_id][0],
                y=positions[node.node_id][1],
                language=node.language,
                doc=node.doc,
                symbols=self._symbol_records(node),
                symbol_total=len(node.symbols),
            )
            for node in lane_nodes
        ]
        views = self._make_views("workflow", chain, ordered_edges)
        return SystemMap(
            kind="workflow",
            title=self._title_for("workflow"),
            nodes=map_nodes,
            edges=ordered_edges,
            views=views,
            meta=self._meta_for("workflow", map_nodes, len(ordered_edges), len(nodes), positions, full),
        )

    def _build_sequence(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        analysis: Optional[AnalysisResult],
        full: bool = False,
    ) -> SystemMap:
        """Build the request sequence map over top participants.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            analysis: Graph analysis.
            full: True keeps every participant with wrapped rows.

        Returns:
            Sequence system map.
        """
        selected = self._select_primary(nodes, links, analysis, full)
        if full:
            participants = list(selected)
        else:
            width_cap = min(
                max(1, self._config.DIAGRAM_SEQUENCE_MAX_PARTICIPANTS),
                self._sequence_capacity(),
            )
            participants = list(selected[: min(len(selected), width_cap)])
            if len(participants) < 2 and len(selected) >= 2:
                participants = list(selected[: min(len(selected), 2)])
        chosen = {node.node_id for node in participants}
        ordered_ids = [node.node_id for node in participants]
        positions = self._layout_sequence(ordered_ids, full)
        kept = self._internal_links(links, chosen, full)
        if full:
            sequence_edges: List[MapEdge] = [
                MapEdge(source=e.source, target=e.target, label=e.relation, kind=e.relation)
                for e in kept
            ]
        else:
            sequence_edges = [
                MapEdge(source=e.source, target=e.target, label=e.relation, kind=e.relation)
                for e in kept[: min(len(kept), max(1, self._config.DIAGRAM_MAX_EDGES // 2))]
            ]
        if not sequence_edges and len(ordered_ids) >= 2:
            sequence_edges = [
                MapEdge(
                    source=ordered_ids[index],
                    target=ordered_ids[index + 1],
                    label="calls",
                    kind="calls",
                )
                for index in range(len(ordered_ids) - 1)
            ]
        layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in participants}
        map_nodes = [
            MapNode(
                node_id=node.node_id,
                label=self._short_label(node.label),
                role=self._role_for(layer_of[node.node_id], False),
                group="lifeline",
                detail="participant | " + node.language,
                x=positions[node.node_id][0],
                y=positions[node.node_id][1],
                language=node.language,
                doc=node.doc,
                symbols=self._symbol_records(node),
                symbol_total=len(node.symbols),
            )
            for node in participants
        ]
        views = self._make_views("sequence", ordered_ids, sequence_edges)
        return SystemMap(
            kind="sequence",
            title=self._title_for("sequence"),
            nodes=map_nodes,
            edges=sequence_edges,
            views=views,
            meta=self._meta_for("sequence", map_nodes, len(sequence_edges), len(nodes), positions, full),
        )

    def _build_dataflow(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
        full: bool = False,
    ) -> SystemMap:
        """Build the data flow map from sources through stores.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings for sensitivity.
            full: True keeps every file without truncation.

        Returns:
            Dataflow system map.
        """
        selected = self._select_primary(nodes, links, None, full)
        proto_layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        _proto_positions, selected = self._place(selected, proto_layer_of, "dataflow", full)
        chosen = {node.node_id for node in selected}
        kept = self._internal_links(links, chosen, full)
        targets = {edge.target for edge in kept}
        sources = [node for node in selected if node.node_id not in targets]
        stores = [
            node
            for node in selected
            if (layers or {}).get(node.node_id, "") == "data_access"
        ]
        ordered = sources + [n for n in stores if n not in sources] + [
            n for n in selected if n not in sources and n not in stores
        ]
        sensitive = self._sensitive_files(findings)
        layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in ordered}
        stage_of: Dict[str, str] = {}
        for node in ordered:
            if node in sources:
                stage_of[node.node_id] = "presentation"
            elif node in stores:
                stage_of[node.node_id] = "data_access"
            else:
                stage_of[node.node_id] = layer_of[node.node_id]
        positions, ordered = self._place(ordered, stage_of, "dataflow", full)
        placed_ids = {node.node_id for node in ordered}
        scoped_kept = [e for e in kept if e.source in placed_ids and e.target in placed_ids]
        map_nodes = [
            MapNode(
                node_id=node.node_id,
                label=self._short_label(node.label),
                role=self._role_for(stage_of[node.node_id], node.node_id in sensitive),
                group=stage_of[node.node_id],
                detail="stage " + stage_of[node.node_id],
                x=positions[node.node_id][0],
                y=positions[node.node_id][1],
                language=node.language,
                doc=node.doc,
                symbols=self._symbol_records(node),
                symbol_total=len(node.symbols),
            )
            for node in ordered
        ]
        map_edges = [
            MapEdge(
                source=e.source,
                target=e.target,
                label="flows" if e.target in {n.node_id for n in stores} else e.relation,
                kind="sensitive" if e.source in sensitive else e.relation,
            )
            for e in scoped_kept
        ]
        views = self._make_views("dataflow", [node.node_id for node in ordered], map_edges)
        return SystemMap(
            kind="dataflow",
            title=self._title_for("dataflow"),
            nodes=map_nodes,
            edges=map_edges,
            views=views,
            meta=self._meta_for("dataflow", map_nodes, len(map_edges), len(nodes), positions, full),
        )

    def _build_lifecycle(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
        full: bool = False,
    ) -> SystemMap:
        """Build the change lifecycle map with waits, retries, and terminals.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings.
            full: True keeps every file without truncation.

        Returns:
            Lifecycle system map.
        """
        selected = self._select_primary(nodes, links, None, full)
        proto_layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        _proto_positions, selected = self._place(selected, proto_layer_of, "lifecycle", full)
        chosen = {node.node_id for node in selected}
        kept = self._internal_links(links, chosen, full)
        sensitive = self._sensitive_files(findings)
        layer_of = {node.node_id: proto_layer_of[node.node_id] for node in selected}
        dependents: Dict[str, int] = {}
        for edge in kept:
            dependents[edge.target] = dependents.get(edge.target, 0) + 1
        orphans = [node for node in selected if dependents.get(node.node_id, 0) == 0]
        terminal_group = "testing"
        state_of: Dict[str, str] = {}
        for node in selected:
            if node in orphans and len(selected) > 3:
                state_of[node.node_id] = terminal_group
            else:
                state_of[node.node_id] = layer_of[node.node_id]
        positions, selected = self._place(selected, state_of, "lifecycle", full)
        placed_ids = {node.node_id for node in selected}
        scoped_kept = [e for e in kept if e.source in placed_ids and e.target in placed_ids]
        group_of = {node.node_id: state_of[node.node_id] for node in selected}
        map_nodes = [
            MapNode(
                node_id=node.node_id,
                label=self._short_label(node.label),
                role=self._role_for(group_of[node.node_id], node.node_id in sensitive),
                group=group_of[node.node_id],
                detail="state " + group_of[node.node_id],
                x=positions[node.node_id][0],
                y=positions[node.node_id][1],
                language=node.language,
                doc=node.doc,
                symbols=self._symbol_records(node),
                symbol_total=len(node.symbols),
            )
            for node in selected
        ]
        lifecycle_edges = [
            MapEdge(source=e.source, target=e.target, label="transitions", kind="transitions")
            for e in scoped_kept
        ]
        mutual = {(e.target, e.source) for e in scoped_kept}
        for edge in scoped_kept:
            if (edge.source, edge.target) in mutual:
                lifecycle_edges.append(
                    MapEdge(
                        source=edge.target,
                        target=edge.source,
                        label="retry",
                        kind="retry",
                    )
                )
                break
        deduped: List[MapEdge] = []
        seen_routes: Set[str] = set()
        for edge in lifecycle_edges:
            key = edge.source + "->" + edge.target + ":" + edge.kind
            if key not in seen_routes:
                deduped.append(edge)
                seen_routes.add(key)
        views = self._make_views("lifecycle", [node.node_id for node in selected], deduped)
        final_edges = deduped if full else deduped[: max(0, self._config.DIAGRAM_MAX_EDGES)]
        return SystemMap(
            kind="lifecycle",
            title=self._title_for("lifecycle"),
            nodes=map_nodes,
            edges=final_edges,
            views=views,
            meta=self._meta_for("lifecycle", map_nodes, len(final_edges), len(nodes), positions, full),
        )


class InteractiveMapRenderer:
    """Renders a system map as one self-contained interactive HTML document."""

    def __init__(self, config: Config) -> None:
        """Initialise the renderer with application configuration.

        Args:
            config: Central settings for preset, theme, and share size.
        """
        self._config = config

    def _canvas_size(self, system_map: SystemMap) -> Tuple[int, int]:
        """Return the effective canvas size for rendering a map.

        Args:
            system_map: Map carrying optional grown canvas metadata.

        Returns:
            Effective canvas width and height pair.
        """
        width = self._config.DIAGRAM_CANVAS_WIDTH
        height = self._config.DIAGRAM_CANVAS_HEIGHT
        try:
            width = max(width, int(str(system_map.meta.get("canvas_width", width))))
        except ValueError:
            pass
        try:
            height = max(height, int(str(system_map.meta.get("canvas_height", height))))
        except ValueError:
            pass
        return width, height

    def render(self, system_map: SystemMap) -> str:
        """Render a system map as a self-contained HTML document.

        Args:
            system_map: Validated system map intermediate representation.

        Returns:
            Complete standalone HTML document with inline SVG and scripting.
        """
        canvas_w, canvas_h = self._canvas_size(system_map)
        nodes_payload = [
            {
                "id": node.node_id,
                "label": node.label,
                "role": node.role,
                "group": node.group,
                "detail": node.detail,
                "x": node.x,
                "y": node.y,
                "language": node.language,
                "doc": node.doc[: self._config.DIAGRAM_TOOLTIP_DOC_CHARS],
                "symbols": node.symbols,
                "symbol_total": node.symbol_total,
            }
            for node in system_map.nodes
        ]
        edges_payload = [
            {
                "source": edge.source,
                "target": edge.target,
                "label": edge.label,
                "kind": edge.kind,
            }
            for edge in system_map.edges
        ]
        views_payload = [
            {
                "id": view.view_id,
                "title": view.title,
                "focus": list(view.focus),
                "description": view.description,
            }
            for view in system_map.views
        ]
        preset = system_map.meta.get("preset", self._config.DIAGRAM_PRESET)
        if preset not in tuple(self._config.DIAGRAM_PRESETS):
            preset = "classic"
        theme = system_map.meta.get("theme", self._config.DIAGRAM_THEME)
        if theme not in ("dark", "light"):
            theme = "dark"
        home_target = str(system_map.meta.get("home", "")).strip()
        if home_target:
            home_link = (
                '<a class="home-link" href="'
                + html.escape(home_target, quote=True)
                + '">Gallery</a>'
            )
        else:
            home_link = ""
        document = self._template()
        document = document.replace("__HOME_LINK__", home_link)
        document = document.replace("__MAP_KIND__", html.escape(system_map.kind))
        document = document.replace("__MAP_TITLE__", html.escape(system_map.title))
        document = document.replace("__MAP_PRESET__", html.escape(preset))
        document = document.replace("__MAP_THEME__", html.escape(theme))
        document = document.replace("__NODES_SVG__", self._nodes_svg(system_map))
        document = document.replace("__EDGES_SVG__", self._edges_svg(system_map))
        document = document.replace(
            "__NODES_JSON__", self._safe_json(nodes_payload)
        )
        document = document.replace(
            "__EDGES_JSON__", self._safe_json(edges_payload)
        )
        document = document.replace(
            "__VIEWS_JSON__", self._safe_json(views_payload)
        )
        document = document.replace(
            "__META_JSON__",
            self._safe_json(
                {
                    "kind": system_map.kind,
                    "title": system_map.title,
                    "nodeCount": len(system_map.nodes),
                    "edgeCount": len(system_map.edges),
                    "shareWidth": self._config.DIAGRAM_SHARE_WIDTH,
                    "shareHeight": self._config.DIAGRAM_SHARE_HEIGHT,
                    "motion": bool(self._config.DIAGRAM_MOTION_ENABLED),
                    "totalFiles": system_map.meta.get("total", str(len(system_map.nodes))),
                    "nodeWidth": self._config.DIAGRAM_NODE_WIDTH,
                    "nodeHeight": self._config.DIAGRAM_NODE_HEIGHT,
                    "canvasWidth": canvas_w,
                    "canvasHeight": canvas_h,
                }
            ),
        )
        document = document.replace(
            "__PRESETS_JSON__", self._safe_json(list(self._config.DIAGRAM_PRESETS))
        )
        document = document.replace("__CANVAS_W__", str(canvas_w))
        document = document.replace("__CANVAS_H__", str(canvas_h))
        return document

    def write(
        self, system_map: SystemMap, output_path: str
    ) -> str:
        """Render a system map and write it to a relative output path.

        Args:
            system_map: System map intermediate representation.
            output_path: Destination file path.

        Returns:
            Rendered HTML document that was written.
        """
        target = Path(output_path)
        if target.parent != Path(".") and str(target.parent) not in ("", "."):
            target.parent.mkdir(parents=True, exist_ok=True)
        content = self.render(system_map)
        target.write_text(content, encoding="utf-8")
        return content

    def _safe_json(self, payload: object) -> str:
        """Serialize a payload for safe inline script embedding.

        Args:
            payload: JSON-serializable payload.

        Returns:
            JSON text with angle brackets unicode-escaped.
        """
        return _json_payload(payload)

    def _escape(self, value: str) -> str:
        """Escape text for SVG and HTML embedding.

        Args:
            value: Raw text.

        Returns:
            Escaped text safe for markup contexts.
        """
        return _escape_markup(value)

    def _role_color(self, role: str) -> str:
        """Return the stroke color for a semantic role.

        Args:
            role: Semantic role identifier.

        Returns:
            Hex color string for the role.
        """
        return _role_color(role, self._config)

    def _edge_path(self, x1: int, y1: int, x2: int, y2: int) -> str:
        """Compute a deterministic curved route between two nodes.

        Args:
            x1: Source horizontal center.
            y1: Source vertical center.
            x2: Target horizontal center.
            y2: Target vertical center.

        Returns:
            SVG path data string.
        """
        width = self._config.DIAGRAM_NODE_WIDTH
        half = width // 2
        start_x = x1 + half
        end_x = x2 - half
        mid_x = (start_x + end_x) // 2
        return (
            "M "
            + str(start_x)
            + " "
            + str(y1)
            + " C "
            + str(mid_x)
            + " "
            + str(y1)
            + ", "
            + str(mid_x)
            + " "
            + str(y2)
            + ", "
            + str(end_x)
            + " "
            + str(y2)
        )

    def _nodes_svg(self, system_map: SystemMap) -> str:
        """Render authored nodes as inline SVG groups.

        Args:
            system_map: System map intermediate representation.

        Returns:
            SVG fragment with one group per node.
        """
        width = self._config.DIAGRAM_NODE_WIDTH
        height = self._config.DIAGRAM_NODE_HEIGHT
        parts: List[str] = []
        for node in system_map.nodes:
            color = self._role_color(node.role)
            label = self._escape(node.label[: max(1, self._config.DIAGRAM_MAX_LABEL_CHARS)])
            group = self._escape(node.group)
            parts.append(
                '<g class="map-node" data-id="'
                + self._escape(node.node_id)
                + '" data-role="'
                + self._escape(node.role)
                + '" transform="translate('
                + str(node.x)
                + ","
                + str(node.y)
                + ')" tabindex="0" role="button" aria-label="'
                + label
                + '">'
                + '<rect class="node-box" width="'
                + str(width)
                + '" height="'
                + str(height)
                + '" rx="10" style="stroke:'
                + color
                + '"></rect>'
                + '<circle class="node-dot" cx="16" cy="16" r="5" style="fill:'
                + color
                + '"></circle>'
                + '<text class="node-label" x="30" y="26">'
                + label
                + "</text>"
                + '<text class="node-group" x="30" y="46">'
                + group
                + "</text>"
                + "</g>"
            )
        return "\n".join(parts)

    def _edges_svg(self, system_map: SystemMap) -> str:
        """Render authored relationships as inline SVG paths.

        Args:
            system_map: System map intermediate representation.

        Returns:
            SVG fragment with one path per relationship.
        """
        by_id = {node.node_id: node for node in system_map.nodes}
        height = self._config.DIAGRAM_NODE_HEIGHT
        parts: List[str] = []
        for edge in system_map.edges:
            source = by_id.get(edge.source)
            target = by_id.get(edge.target)
            if source is None or target is None:
                continue
            y1 = source.y + height // 2
            y2 = target.y + height // 2
            dashed = " edge-dashed" if edge.kind in ("retry", "sensitive", "next") else ""
            label = self._escape(edge.label[: max(1, self._config.DIAGRAM_MAX_LABEL_CHARS)])
            mid = (source.x + target.x) // 2
            mid_y = (y1 + y2) // 2
            parts.append(
                '<g class="map-edge'
                + dashed
                + '" data-source="'
                + self._escape(edge.source)
                + '" data-target="'
                + self._escape(edge.target)
                + '">'
                + '<path class="edge-path" d="'
                + self._edge_path(source.x, source.y + height // 2, target.x, target.y + height // 2)
                + '" style="stroke:'
                + self._role_color(target.role)
                + '"></path>'
                + '<text class="edge-label" x="'
                + str(mid)
                + '" y="'
                + str(mid_y - 6)
                + '">'
                + label
                + "</text>"
                + "</g>"
            )
        return "\n".join(parts)

    def _template(self) -> str:
        """Return the self-contained viewer document template.

        Returns:
            HTML template with replacement tokens for map content.
        """
        return """<!DOCTYPE html>
<html lang="en" data-theme="__MAP_THEME__" data-preset="__MAP_PRESET__">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__MAP_TITLE__ | System Map</title>
<style>
:root{--canvas:#020617;--mask:#0f172a;--ink:#ffffff;--muted:#94a3b8;--dim:#475569;--border:#1e293b}
html[data-theme="light"]{--canvas:#f8fafc;--mask:#ffffff;--ink:#0f172a;--muted:#475569;--dim:#94a3b8;--border:#e2e8f0}
html[data-preset="blueprint"]{--canvas:#0b1e3a;--mask:#10294f;--border:#274a7a}
html[data-preset="flow"]{--canvas:#05070f;--mask:#0b1226;--border:#26314d}
html[data-preset="editorial"]{--canvas:#14110c;--mask:#221c12;--border:#4a3d28}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.toolbar{display:flex;gap:8px;align-items:center;padding:10px 14px;background:var(--mask);border-bottom:1px solid var(--border);flex-wrap:wrap}
.brand{font-weight:700;font-size:14px;letter-spacing:.04em}
.kind{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.12em}
.toolbar input{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;min-width:220px;font:inherit;font-size:12px}
.toolbar button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font:inherit;font-size:12px;cursor:pointer;min-height:32px}
.toolbar button:hover,.toolbar button:focus-visible{border-color:#22d3ee;outline:2px solid #22d3ee;outline-offset:2px}
.home-link{color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font-size:12px;text-decoration:none;background:var(--canvas)}
.home-link:hover,.home-link:focus-visible{border-color:#22d3ee;outline:2px solid #22d3ee;outline-offset:2px}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 320px;min-height:calc(100vh - 53px)}
.stage{position:relative;padding:16px;overflow:auto}
svg#canvas{width:100%;height:auto;min-height:520px;background:var(--canvas);background-image:radial-gradient(circle,var(--border) 1px,transparent 1px);background-size:28px 28px;border:1px solid var(--border);border-radius:16px}
html[data-preset="blueprint"] svg#canvas{background-image:linear-gradient(var(--border) 1px,transparent 1px),linear-gradient(90deg,var(--border) 1px,transparent 1px);background-size:32px 32px}
html[data-preset="blueprint"] .node-box{rx:2}
html[data-preset="flow"] .edge-path{filter:drop-shadow(0 0 5px rgba(148,163,184,.65))}
html[data-preset="flow"] .map-node.strong .node-box{filter:drop-shadow(0 0 8px rgba(34,211,238,.55))}
html[data-preset="editorial"] .node-label{font-size:13px}
.node-box{fill:var(--mask);stroke-width:2}
.map-node:hover .node-box{stroke-width:3}
.node-label{fill:var(--ink);font-size:12px;font-weight:600}
.node-group{fill:var(--muted);font-size:10px;text-transform:uppercase;letter-spacing:.08em}
.edge-path{fill:none;stroke-width:2;opacity:.85}
.map-edge.edge-dashed .edge-path{stroke-dasharray:6 5}
.edge-label{fill:var(--muted);font-size:10px;text-anchor:middle;paint-order:stroke;stroke:var(--canvas);stroke-width:3px}
.map-node{cursor:grab;touch-action:none}
.map-node.dragging{cursor:grabbing}
.map-node.dim,.map-edge.dim{opacity:.12}
.map-node.strong .node-box{stroke-width:3}
.map-edge.strong .edge-path{stroke-width:3;opacity:1}
.map-node:focus-visible{outline:2px solid #22d3ee;outline-offset:3px}
.passport{background:var(--mask);border-left:1px solid var(--border);padding:16px;overflow:auto}
.passport h2{font-size:13px;margin:0 0 8px}
.passport .row{font-size:12px;color:var(--muted);margin:6px 0}
.passport .counts{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.chip{border:1px solid var(--border);border-radius:999px;padding:3px 10px;font-size:11px;color:var(--ink)}
.views{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
.journey{font-size:12px;line-height:1.7}
.receipt{font-size:11px;color:var(--muted);border:1px solid var(--border);border-radius:8px;padding:8px;margin-top:10px}
.routebox{display:flex;gap:6px;margin-top:8px}
.routebox input{flex:1;background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:7px;font:inherit;font-size:12px;min-width:0}
.present .layout{grid-template-columns:minmax(0,1fr)}
.present .passport{display:none}
.present svg#canvas{min-height:78vh}
.motion .edge-path{stroke-dasharray:8 6;animation:trace 1.1s linear 1}
@keyframes trace{from{stroke-dashoffset:28}to{stroke-dashoffset:0}}
@media (prefers-reduced-motion:reduce){.motion .edge-path{animation:none}}
#map-overview{position:absolute;right:26px;bottom:26px;background:var(--mask);border:1px solid var(--border);border-radius:10px;padding:8px 10px;font-size:11px;color:var(--muted)}
dialog{background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:12px;max-width:520px}
dialog kbd{border:1px solid var(--border);border-radius:6px;padding:1px 6px;font-size:11px}
@media (max-width:960px){.layout{grid-template-columns:minmax(0,1fr)}.passport{border-left:none;border-top:1px solid var(--border)}}
</style>
</head>
<body>
<header class="toolbar" aria-label="Map controls">
<span class="brand">System Maps</span>
__HOME_LINK__
<span class="kind">__MAP_KIND__ | __MAP_TITLE__</span>
<input id="search" type="search" placeholder="Search nodes ( / )" aria-label="Search nodes" title="Filter nodes by label, id, or detail. Shortcut: /">
<button type="button" data-action="reach-up" aria-label="Trace upstream reach" title="Show everything that reaches the focused node (authored relationships only)">Upstream</button>
<button type="button" data-action="reach-down" aria-label="Trace downstream reach" title="Show everything the focused node reaches (authored relationships only)">Downstream</button>
<button type="button" data-action="lens" aria-label="Compare roles" title="Highlight one semantic role and compare counts; activate again to clear">Lens</button>
<button type="button" data-action="views-prev" aria-label="Previous chapter" title="Show the previous guided chapter">[</button>
<button type="button" data-action="views-next" aria-label="Next chapter" title="Show the next guided chapter">]</button>
<button type="button" data-action="play" aria-label="Play guided story" title="Play all guided chapters in order">Play</button>
<button type="button" data-action="map" aria-label="Toggle overview" title="Toggle the live overview radar">Overview</button>
<button type="button" data-action="present" aria-label="Enter presentation stage" title="Hide the side panel for presenting">Present</button>
<button type="button" data-action="settle" aria-label="Relax layout" title="Relax node positions with a force pass (nodes stay draggable)">Settle</button>
<button type="button" data-action="style" aria-label="Cycle visual preset" title="Cycle visual preset: classic, flow, blueprint, editorial">Style</button>
<button type="button" data-action="theme" aria-label="Toggle theme" title="Toggle dark and light themes">Theme</button>
<button type="button" data-action="export" aria-label="Open export menu" title="Download full-diagram SVG, share-card PNG, or typed JSON">Export</button>
<button type="button" data-action="help" aria-label="Open diagram guide" title="Open the diagram guide with every shortcut">?</button>
</header>
<div class="layout">
<main class="stage">
<svg id="canvas" viewBox="0 0 __CANVAS_W__ __CANVAS_H__" role="img" aria-label="__MAP_TITLE__ diagram">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8"></path></marker></defs>
<g id="edges">__EDGES_SVG__</g>
<g id="nodes">__NODES_SVG__</g>
</svg>
<div id="map-overview" hidden></div>
</main>
<aside class="passport" aria-live="polite" aria-label="Semantic passport">
<h2 id="passport-title">Diagram guide</h2>
<div class="row" id="passport-meta"></div>
<div class="views" id="chapters"></div>
<div class="counts" id="role-counts"></div>
<div class="row">1. Search (/) or click a node to focus it. 2. Upstream and Downstream trace authored reach. 3. Path probes the exact route between two ids. 4. Play walks the guided chapters. Drag nodes to rearrange, Settle to relax, ? for every shortcut.</div>
<div class="routebox guide"><input id="route-from" placeholder="route from id" aria-label="Route source" title="Source node id for the route probe"><input id="route-to" placeholder="route to id" aria-label="Route target" title="Target node id for the route probe"><button type="button" data-action="route" aria-label="Probe directed route" title="Highlight the shortest authored directed path">Path</button></div>
<div class="journey" id="journey"></div>
<div class="receipt" id="receipt"></div>
</aside>
</div>
<div class="peek" id="peek" role="tooltip"></div>
<dialog id="guide" aria-label="Diagram guide dialog">
<h2>Diagram guide</h2>
<p>Hover a node for a preview card; click it to open its passport with a neighbourhood mini-map, metrics, symbols, and clickable neighbours. <kbd>Backspace</kbd> goes back.</p>
<p><kbd>/</kbd> search &middot; <kbd>R</kbd> route probe &middot; <kbd>L</kbd> role lens &middot; <kbd>M</kbd> overview &middot; <kbd>P</kbd> play &middot; <kbd>[</kbd> <kbd>]</kbd> chapters &middot; <kbd>F</kbd> present &middot; <kbd>G</kbd> settle &middot; <kbd>S</kbd> style &middot; <kbd>T</kbd> theme &middot; <kbd>E</kbd> export &middot; <kbd>+</kbd> <kbd>-</kbd> <kbd>0</kbd> zoom</p>
<p>Drag any node to rearrange it; edges follow. Settle relaxes the whole layout with one deterministic force pass. Reload restores the authored layout.</p>
<p>Deep links restore <code>#focus=id</code>, <code>#focus=id&amp;reach=upstream|downstream</code>, <code>#route=a~b</code>, <code>#lens=role</code>, and <code>#view=id</code>. Motion is finite, honors reduced-motion settings, and never enters exports.</p>
<button type="button" data-action="close-guide" title="Close the diagram guide">Close</button>
</dialog>
<dialog id="exports" aria-label="Export dialog">
<h2>Export</h2>
<p>Exports are full-diagram and free of temporary viewer state.</p>
<button type="button" data-action="export-svg" title="Download the full diagram as SVG">Download SVG</button>
<button type="button" data-action="export-png" title="Download a share-card PNG with title and counts">Download share card PNG</button>
<button type="button" data-action="export-json" title="Download the typed JSON behind this diagram">Download typed JSON</button>
<button type="button" data-action="close-exports" title="Close the export menu">Close</button>
</dialog>
<script type="application/json" id="map-nodes">__NODES_JSON__</script>
<script type="application/json" id="map-edges">__EDGES_JSON__</script>
<script type="application/json" id="map-views">__VIEWS_JSON__</script>
<script type="application/json" id="map-meta">__META_JSON__</script>
<script>
(function(){
"use strict";
var nodes=JSON.parse(document.getElementById("map-nodes").textContent||"[]");
var edges=JSON.parse(document.getElementById("map-edges").textContent||"[]");
var views=JSON.parse(document.getElementById("map-views").textContent||"[]");
var meta=JSON.parse(document.getElementById("map-meta").textContent||"{}");
var root=document.documentElement;
var svg=document.getElementById("canvas");
var search=document.getElementById("search");
var passportTitle=document.getElementById("passport-title");
var passportMeta=document.getElementById("passport-meta");
var journey=document.getElementById("journey");
var receipt=document.getElementById("receipt");
var chapters=document.getElementById("chapters");
var roleCounts=document.getElementById("role-counts");
var overview=document.getElementById("map-overview");
var guide=document.getElementById("guide");
var exportsDialog=document.getElementById("exports");
var state={focus:null,reach:null,route:[],lens:null,view:-1,zoom:1};
var reduced=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
function byId(id){for(var i=0;i<nodes.length;i++){if(nodes[i].id===id){return nodes[i];}}return null;}
function outgoing(id){return edges.filter(function(e){return e.source===id;});}
function incoming(id){return edges.filter(function(e){return e.target===id;});}
function bfsReach(start,direction){
var seen={};seen[start]=0;var queue=[start];var order=[start];
while(queue.length){var current=queue.shift();var nexts=direction==="downstream"?outgoing(current):incoming(current);
for(var i=0;i<nexts.length;i++){var nid=direction==="downstream"?nexts[i].target:nexts[i].source;
if(!(nid in seen)){seen[nid]=seen[current]+1;queue.push(nid);order.push(nid);}}}
return {members:order,hops:seen};}
function bfsRoute(from,to){
if(from===to){return [from];}
var prev={};var seen={};seen[from]=true;var queue=[from];
while(queue.length){var current=queue.shift();var nexts=outgoing(current);
for(var i=0;i<nexts.length;i++){var nid=nexts[i].target;
if(!(nid in seen)){seen[nid]=true;prev[nid]=current;
if(nid===to){var path=[to];var c=to;while(c!==from){c=prev[c];path.unshift(c);}return path;}
queue.push(nid);}}}
return [];}
function applyClasses(predicate){
var nodeEls=document.querySelectorAll(".map-node");
for(var i=0;i<nodeEls.length;i++){var id=nodeEls[i].getAttribute("data-id");var on=predicate(id);nodeEls[i].classList.toggle("dim",!on);nodeEls[i].classList.toggle("strong",!!on&&state.focus===id);}
var edgeEls=document.querySelectorAll(".map-edge");
for(var j=0;j<edgeEls.length;j++){var s=edgeEls[j].getAttribute("data-source");var t=edgeEls[j].getAttribute("data-target");edgeEls[j].classList.toggle("dim",!(predicate(s)&&predicate(t)));edgeEls[j].classList.toggle("strong",state.route.length>1&&state.route.indexOf(s)>=0&&state.route.indexOf(t)===state.route.indexOf(s)+1);}}
function showAll(){applyClasses(function(){return true;});}
function setHash(value){try{history.replaceState(null,"",value);}catch(e){location.hash=value;}}
function focusNode(id,reach){
var node=byId(id);if(!node){return;}
state.focus=id;state.reach=reach||null;state.route=[];
var ins=incoming(id);var outs=outgoing(id);
passportTitle.textContent=node.label;
passportMeta.textContent=node.id+" | role "+node.role+" | group "+node.group+" | "+node.detail;
var allowed={};allowed[id]=true;
if(state.reach){var found=bfsReach(id,state.reach);found.members.forEach(function(m){allowed[m]=true;});
var hops=0;for(var k in found.hops){if(found.hops[k]>hops){hops=found.hops[k];}}
receipt.textContent=(state.reach==="downstream"?"Downstream":"Upstream")+" reach: "+found.members.length+" nodes, "+hops+" max hops. Authored relationships only.";}
else{receipt.textContent="In: "+ins.length+" | Out: "+outs.length+" | Views: "+views.length;}
applyClasses(function(nid){return !!allowed[nid];});
var hash="#focus="+encodeURIComponent(id);
if(state.reach){hash+="&reach="+state.reach;}
setHash(hash);}
function probeRoute(){
var from=document.getElementById("route-from").value.trim();
var to=document.getElementById("route-to").value.trim();
if(!from||!to){return;}
var path=bfsRoute(from,to);state.route=path;state.focus=null;
if(!path.length){journey.textContent="No authored directed route from "+from+" to "+to+".";receipt.textContent="Route probe: 0 links.";return;}
var allowed={};path.forEach(function(n){allowed[n]=true;});
applyClasses(function(nid){return !!allowed[nid];});
svg.classList.remove("motion");
if(meta.motion&&!reduced){void svg.getBoundingClientRect();svg.classList.add("motion");setTimeout(function(){svg.classList.remove("motion");},1300);}
var names=path.map(function(n){var node=byId(n);return node?node.label:n;});
journey.textContent="Journey: "+names.join(" -> ")+" ("+(path.length-1)+" hops).";
receipt.textContent="Route probe: "+path.length+" nodes, "+(path.length-1)+" links.";
setHash("#route="+encodeURIComponent(from)+"~"+encodeURIComponent(to));}
function applyLens(role){
state.lens=role;
if(!role){showAll();receipt.textContent="Lens cleared.";setHash("#");return;}
var counts={};nodes.forEach(function(n){counts[n.role]=(counts[n.role]||0)+1;});
applyClasses(function(nid){var n=byId(nid);return n&&n.role===role;});
var parts=[];for(var k in counts){parts.push(k+": "+counts[k]);}
receipt.textContent="Lens "+role+": "+(counts[role]||0)+" of "+nodes.length+" nodes. "+parts.join(" | ");
setHash("#lens="+encodeURIComponent(role));}
function showView(index){
if(!views.length){return;}
state.view=(index+views.length)%views.length;
var view=views[state.view];
chapters.querySelectorAll("button").forEach(function(b,i){b.disabled=(i===state.view);});
passportTitle.textContent=view.title;
passportMeta.textContent=view.description||"";
var allowed={};view.focus.forEach(function(n){allowed[n]=true;});
if(!view.focus.length){showAll();}else{applyClasses(function(nid){return !!allowed[nid];});}
journey.textContent=view.focus.length?("Chapter focus: "+view.focus.join(", ")):"";
receipt.textContent="Chapter "+(state.view+1)+" of "+views.length+".";
setHash("#view="+encodeURIComponent(view.id));}
function renderChapters(){
chapters.innerHTML="";
views.forEach(function(view,index){var b=document.createElement("button");b.type="button";b.textContent=view.title;b.setAttribute("aria-label","Show chapter "+view.title);b.addEventListener("click",function(){showView(index);});chapters.appendChild(b);});}
function renderRoleCounts(){
var counts={};nodes.forEach(function(n){counts[n.role]=(counts[n.role]||0)+1;});
roleCounts.innerHTML="";
Object.keys(counts).sort().forEach(function(role){var s=document.createElement("button");s.type="button";s.className="chip";s.textContent=role+": "+counts[role];s.setAttribute("aria-label","Filter role "+role);s.addEventListener("click",function(){applyLens(role);});roleCounts.appendChild(s);});}
function cyclePreset(){
var presets=__PRESETS_JSON__;
var current=root.getAttribute("data-preset")||"classic";
var next=presets[(presets.indexOf(current)+1)%presets.length];
root.setAttribute("data-preset",next);}
function toggleTheme(){
var current=root.getAttribute("data-theme")||"dark";
root.setAttribute("data-theme",current==="dark"?"light":"dark");}
function setZoom(factor){
state.zoom=Math.min(2.5,Math.max(0.5,state.zoom*factor));
svg.setAttribute("viewBox","0 0 "+Math.round(__CANVAS_W__/state.zoom)+" "+Math.round(__CANVAS_H__/state.zoom));}
function resetZoom(){state.zoom=1;svg.setAttribute("viewBox","0 0 __CANVAS_W__ __CANVAS_H__");}
var nodeW=(meta.nodeWidth||190);
var nodeH=(meta.nodeHeight||64);
var live={};
nodes.forEach(function(n){live[n.id]={x:n.x,y:n.y};});
function edgePath(x1,y1,x2,y2){
var sx=x1+nodeW/2,ex=x2-nodeW/2,mx=(sx+ex)/2;
var yy1=y1+nodeH/2,yy2=y2+nodeH/2;
return "M "+sx+" "+yy1+" C "+mx+" "+yy1+", "+mx+" "+yy2+", "+ex+" "+yy2;}
function refreshEdges(){
document.querySelectorAll(".map-edge").forEach(function(g){
var s=live[g.getAttribute("data-source")],t=live[g.getAttribute("data-target")];
if(!s||!t){return;}
var path=g.querySelector(".edge-path");
if(path){path.setAttribute("d",edgePath(s.x,s.y,t.x,t.y));}
var label=g.querySelector(".edge-label");
if(label){label.setAttribute("x",String(Math.round((s.x+t.x)/2)));label.setAttribute("y",String(Math.round((s.y+t.y)/2+nodeH/2-6)));}});}
function svgPoint(ev){
var pt=svg.createSVGPoint();pt.x=ev.clientX;pt.y=ev.clientY;
var m=svg.getScreenCTM();if(!m){return {x:pt.x,y:pt.y};}
var p=pt.matrixTransform(m.inverse());return {x:p.x,y:p.y};}
function settle(){
var ids=Object.keys(live);
var adj={};ids.forEach(function(id){adj[id]=[];});
edges.forEach(function(e){if(live[e.source]&&live[e.target]){adj[e.source].push(e.target);adj[e.target].push(e.source);}});
for(var iter=0;iter<150;iter++){
var dx={},dy={};ids.forEach(function(id){dx[id]=0;dy[id]=0;});
for(var a=0;a<ids.length;a++){for(var b=a+1;b<ids.length;b++){
var pa=live[ids[a]],pb=live[ids[b]];
var ddx=pa.x-pb.x,ddy=pa.y-pb.y;
var dist=Math.sqrt(ddx*ddx+ddy*ddy)||1;
var force=Math.min(9000/(dist*dist),40);
dx[ids[a]]+=ddx/dist*force;dy[ids[a]]+=ddy/dist*force;
dx[ids[b]]-=ddx/dist*force;dy[ids[b]]-=ddy/dist*force;}}
ids.forEach(function(id){
var seen={};
adj[id].forEach(function(other){
if(seen[other]){return;}seen[other]=true;
var pa=live[id],pb=live[other];
var ddx=pb.x-pa.x,ddy=pb.y-pa.y;
var dist=Math.sqrt(ddx*ddx+ddy*ddy)||1;
var step=(dist-320)*0.02;
dx[id]+=ddx/dist*step;dy[id]+=ddy/dist*step;});});
ids.forEach(function(id){live[id].x+=dx[id];live[id].y+=dy[id];});}
document.querySelectorAll(".map-node").forEach(function(el){
var p=live[el.getAttribute("data-id")];
if(p){el.setAttribute("transform","translate("+Math.round(p.x)+","+Math.round(p.y)+")");}});
refreshEdges();
receipt.textContent="Layout relaxed with one deterministic force pass.";}
function cleanClone(){
var clone=svg.cloneNode(true);clone.classList.remove("motion");
clone.querySelectorAll(".dim,.strong,.dragging").forEach(function(el){el.classList.remove("dim","strong","dragging");});
clone.setAttribute("xmlns","http://www.w3.org/2000/svg");return clone;}
function updateOverview(){
var total=nodes.length;var visible=nodes.length;
try{visible=document.querySelectorAll(".map-node:not(.dim)").length;}catch(e){}
overview.textContent=total+" nodes | "+edges.length+" links | "+visible+" visible";}
function exportSVG(){
var clone=cleanClone();
var text=new XMLSerializer().serializeToString(clone);
var blob=new Blob([text],{type:"image/svg+xml"});download(blob,"system-map-"+(meta.kind||"map")+".svg");}
function exportJSON(){
var payload={kind:meta.kind,title:meta.title,nodes:nodes,edges:edges,views:views};
var blob=new Blob([JSON.stringify(payload,null,2)],{type:"application/json"});download(blob,"system-map-"+(meta.kind||"map")+".json");}
function exportPNG(){
var clone=cleanClone();
var text=new XMLSerializer().serializeToString(clone);
var width=(meta.shareWidth||1200);var height=(meta.shareHeight||630);
var image=new Image();
image.onload=function(){
var canvas=document.createElement("canvas");canvas.width=width;canvas.height=height;
var ctx=canvas.getContext("2d");var dark=root.getAttribute("data-theme")!=="light";
ctx.fillStyle=dark?"#020617":"#f8fafc";ctx.fillRect(0,0,width,height);
ctx.fillStyle=dark?"#ffffff":"#0f172a";ctx.font="700 30px monospace";ctx.fillText(meta.title||"System Map",40,60);
ctx.font="20px monospace";ctx.fillStyle="#94a3b8";ctx.fillText((meta.kind||"map")+" | "+nodes.length+" nodes | "+edges.length+" links",40,95);
var url=URL.createObjectURL(new Blob([text],{type:"image/svg+xml"}));
var diagram=new Image();
diagram.onload=function(){ctx.drawImage(diagram,20,120,width-40,height-160);URL.revokeObjectURL(url);canvas.toBlob(function(blob){if(blob){download(blob,"system-map-"+(meta.kind||"map")+"-share.png");}});};
diagram.src=url;};
var url=URL.createObjectURL(new Blob([text],{type:"image/svg+xml"}));image.src=url;}
function download(blob,name){
var link=document.createElement("a");link.href=URL.createObjectURL(blob);link.download=name;document.body.appendChild(link);link.click();
setTimeout(function(){URL.revokeObjectURL(link.href);link.remove();},400);}
function readHash(){
var hash=location.hash||"";
if(hash.indexOf("#route=")===0){var parts=hash.slice(7).split("~");if(parts.length===2){document.getElementById("route-from").value=decodeURIComponent(parts[0]);document.getElementById("route-to").value=decodeURIComponent(parts[1]);probeRoute();}return;}
if(hash.indexOf("#lens=")===0){applyLens(decodeURIComponent(hash.slice(6)));return;}
if(hash.indexOf("#view=")===0){var id=decodeURIComponent(hash.slice(6));for(var i=0;i<views.length;i++){if(views[i].id===id){showView(i);return;}}return;}
if(hash.indexOf("#focus=")===0){var rest=hash.slice(7).split("&reach=");focusNode(decodeURIComponent(rest[0]),rest[1]?decodeURIComponent(rest[1]):null);return;}}
document.querySelectorAll(".map-node").forEach(function(el){
el.addEventListener("click",function(){if(state.dragged){state.dragged=false;return;}focusNode(el.getAttribute("data-id"));});
el.addEventListener("keydown",function(ev){if(ev.key==="Enter"||ev.key===" "){ev.preventDefault();focusNode(el.getAttribute("data-id"));}});
el.addEventListener("pointerdown",function(ev){
var id=el.getAttribute("data-id");var p=live[id];if(!p){return;}
el.classList.add("dragging");
try{el.setPointerCapture(ev.pointerId);}catch(e){}
var start=svgPoint(ev);var ox=p.x,oy=p.y;
var move=function(me){var q=svgPoint(me);p.x=Math.round(ox+q.x-start.x);p.y=Math.round(oy+q.y-start.y);state.dragged=true;
el.setAttribute("transform","translate("+p.x+","+p.y+")");refreshEdges();};
var up=function(){el.classList.remove("dragging");el.removeEventListener("pointermove",move);el.removeEventListener("pointerup",up);el.removeEventListener("pointercancel",up);};
el.addEventListener("pointermove",move);el.addEventListener("pointerup",up);el.addEventListener("pointercancel",up);});});
document.querySelectorAll("[data-action]").forEach(function(btn){
btn.addEventListener("click",function(){
var action=btn.getAttribute("data-action");
if(action==="reach-up"&&state.focus){focusNode(state.focus,"upstream");}
else if(action==="reach-down"&&state.focus){focusNode(state.focus,"downstream");}
else if(action==="route"){probeRoute();}
else if(action==="lens"){applyLens(state.lens?null:"backend");}
else if(action==="views-prev"){showView(state.view-1);}
else if(action==="views-next"){showView(state.view+1);}
else if(action==="play"){var i=0;var step=function(){if(i>=views.length){return;}showView(i);i++;if(!reduced){setTimeout(step,1400);}};step();}
else if(action==="map"){overview.hidden=!overview.hidden;updateOverview();}
else if(action==="present"){document.body.classList.toggle("present");}
else if(action==="settle"){settle();}
else if(action==="style"){cyclePreset();}
else if(action==="theme"){toggleTheme();}
else if(action==="export"){if(typeof exportsDialog.showModal==="function"){exportsDialog.showModal();}}
else if(action==="help"){if(typeof guide.showModal==="function"){guide.showModal();}}
else if(action==="close-guide"){guide.close();}
else if(action==="close-exports"){exportsDialog.close();}
else if(action==="export-svg"){exportSVG();}
else if(action==="export-png"){exportPNG();}
else if(action==="export-json"){exportJSON();}});});
search.addEventListener("input",function(){
var term=search.value.trim().toLowerCase();
if(!term){showAll();updateOverview();return;}
applyClasses(function(nid){var n=byId(nid);if(!n){return false;}return n.label.toLowerCase().indexOf(term)>=0||n.id.toLowerCase().indexOf(term)>=0||n.detail.toLowerCase().indexOf(term)>=0;});
updateOverview();});
document.addEventListener("keydown",function(ev){
if(ev.target&&(ev.target.tagName==="INPUT"||ev.target.tagName==="TEXTAREA")){return;}
if(ev.key==="/"){ev.preventDefault();search.focus();}
else if(ev.key==="R"||ev.key==="r"){var f=document.getElementById("route-from");if(f){f.focus();}}
else if(ev.key==="L"||ev.key==="l"){applyLens(state.lens?null:"backend");}
else if(ev.key==="M"||ev.key==="m"){overview.hidden=!overview.hidden;updateOverview();}
else if(ev.key==="P"||ev.key==="p"){showView(state.view+1);}
else if(ev.key==="["){showView(state.view-1);}
else if(ev.key==="]"){showView(state.view+1);}
else if(ev.key==="F"||ev.key==="f"){document.body.classList.toggle("present");}
else if(ev.key==="G"||ev.key==="g"){settle();}
else if(ev.key==="S"||ev.key==="s"){cyclePreset();}
else if(ev.key==="T"||ev.key==="t"){toggleTheme();}
else if(ev.key==="E"||ev.key==="e"){if(typeof exportsDialog.showModal==="function"){exportsDialog.showModal();}}
else if(ev.key==="?"){if(typeof guide.showModal==="function"){guide.showModal();}}
else if(ev.key==="+"){setZoom(1.15);}
else if(ev.key==="-"){setZoom(1/1.15);}
else if(ev.key==="0"){resetZoom();}});
passportMeta.textContent=nodes.length+" of "+(meta.totalFiles||nodes.length)+" files | "+edges.length+" links | "+views.length+" chapters. Primary scope only; full listing lives in the knowledge base.";
receipt.textContent="Ready. Drag nodes, search, focus, trace reach, probe routes, compare roles, or play chapters.";
renderChapters();renderRoleCounts();updateOverview();readHash();
})();
</script>
</body>
</html>"""


class VisNetworkRenderer:
    """Renders a system map as a physics-driven vis.js network document.

    Fetches the configured vis-network bundle from a CDN at view time,
    so pages need network access. Nodes stay draggable with live
    physics; use the inline renderer when fully offline output matters.
    """

    def __init__(self, config: Config) -> None:
        """Initialise the renderer with application configuration.

        Args:
            config: Central settings for CDN bundle and physics.
        """
        self._config = config

    def render(self, system_map: SystemMap) -> str:
        """Render a system map as a vis.js network HTML document.

        Args:
            system_map: Validated system map intermediate representation.

        Returns:
            HTML document driving a draggable physics network.
        """
        nodes_payload = [
            {
                "id": node.node_id,
                "label": node.label,
                "title": self._tooltip(node),
                "group": node.role,
                "language": node.language,
                "doc": node.doc,
                "symbols": node.symbols,
                "symbolTotal": node.symbol_total,
                "community": node.community,
                "communityLabel": node.community_label,
            }
            for node in system_map.nodes
        ]
        edges_payload = [
            {
                "from": edge.source,
                "to": edge.target,
                "title": edge.label,
                "dashes": edge.kind in ("retry", "sensitive", "next"),
            }
            for edge in system_map.edges
        ]
        views_payload = [
            {
                "id": view.view_id,
                "title": view.title,
                "focus": list(view.focus),
                "description": view.description,
            }
            for view in system_map.views
        ]
        preset = system_map.meta.get("preset", self._config.DIAGRAM_PRESET)
        if preset not in tuple(self._config.DIAGRAM_PRESETS):
            preset = "classic"
        theme = system_map.meta.get("theme", self._config.DIAGRAM_THEME)
        if theme not in ("dark", "light"):
            theme = "dark"
        if self._config.DIAGRAM_VIS_PHYSICS_ENABLED:
            physics = {
                "enabled": True,
                "solver": "forceAtlas2Based",
                "forceAtlas2Based": {
                    "gravitationalConstant": self._config.DIAGRAM_VIS_GRAVITY,
                    "centralGravity": self._config.DIAGRAM_VIS_CENTRAL_GRAVITY,
                    "springLength": self._config.DIAGRAM_VIS_SPRING_LENGTH,
                    "springConstant": self._config.DIAGRAM_VIS_SPRING_CONSTANT,
                    "damping": self._config.DIAGRAM_VIS_DAMPING,
                    "avoidOverlap": self._config.DIAGRAM_VIS_AVOID_OVERLAP,
                },
                "stabilization": {
                    "iterations": self._config.DIAGRAM_VIS_STABILIZE_ITERATIONS
                },
            }
        else:
            physics = {"enabled": False}
        home_target = str(system_map.meta.get("home", "")).strip()
        if home_target:
            home_link = (
                '<a class="home-link" href="'
                + _escape_markup(home_target)
                + '">Gallery</a>'
            )
        else:
            home_link = ""
        document = self._template()
        document = document.replace("__HOME_LINK__", home_link)
        document = document.replace("__VIS_JS__", _escape_markup(self._config.DIAGRAM_VIS_CDN_JS))
        document = document.replace("__VIS_CSS__", _escape_markup(self._config.DIAGRAM_VIS_CDN_CSS))
        document = document.replace("__MAP_KIND__", _escape_markup(system_map.kind))
        document = document.replace("__MAP_TITLE__", _escape_markup(system_map.title))
        document = document.replace("__MAP_PRESET__", _escape_markup(preset))
        document = document.replace("__MAP_THEME__", _escape_markup(theme))
        document = document.replace("__NODES_JSON__", _json_payload(nodes_payload))
        document = document.replace("__EDGES_JSON__", _json_payload(edges_payload))
        document = document.replace("__VIEWS_JSON__", _json_payload(views_payload))
        document = document.replace(
            "__META_JSON__",
            _json_payload(
                {
                    "kind": system_map.kind,
                    "title": system_map.title,
                    "nodeCount": len(system_map.nodes),
                    "edgeCount": len(system_map.edges),
                    "totalFiles": system_map.meta.get("total", str(len(system_map.nodes))),
                    "neighbors": self._config.DIAGRAM_NEIGHBOR_NAMES,
                    "communities": self._community_legend(system_map),
                    "labelTopN": self._config.DIAGRAM_VIS_LABEL_TOP_N,
                }
            ),
        )
        document = document.replace("__PHYSICS_JSON__", _json_payload(physics))
        document = document.replace(
            "__ROLES_JSON__",
            _json_payload(dict(self._config.DIAGRAM_ROLE_COLORS)),
        )
        return document

    def _community_legend(self, system_map: SystemMap) -> List[Dict[str, object]]:
        """Return community legend entries (id, label, color, size) for the map nodes."""
        palette = list(self._config.DIAGRAM_COMMUNITY_COLORS)
        sizes: Dict[int, int] = {}
        labels: Dict[int, str] = {}
        for node in system_map.nodes:
            if node.community < 0:
                continue
            sizes[node.community] = sizes.get(node.community, 0) + 1
            labels[node.community] = node.community_label
        return [
            {
                "id": cid,
                "label": labels[cid] or "community " + str(cid),
                "color": palette[cid % len(palette)] if palette else "#94a3b8",
                "size": sizes[cid],
            }
            for cid in sorted(sizes)
        ]

    def write(self, system_map: SystemMap, output_path: str) -> str:
        """Render a vis.js map and write it to a relative output path.

        Args:
            system_map: System map intermediate representation.
            output_path: Destination file path.

        Returns:
            Rendered HTML document that was written.
        """
        target = Path(output_path)
        if target.parent != Path(".") and str(target.parent) not in ("", "."):
            target.parent.mkdir(parents=True, exist_ok=True)
        content = self.render(system_map)
        target.write_text(content, encoding="utf-8")
        return content

    def _tooltip(self, node: MapNode) -> str:
        """Build a documentation tooltip for a network node.

        Args:
            node: Authored map node.

        Returns:
            Escaped tooltip markup with docs and top symbols.
        """
        doc_chars = max(16, self._config.DIAGRAM_TOOLTIP_DOC_CHARS)
        doc = node.doc.strip()
        if len(doc) > doc_chars:
            doc = doc[:doc_chars] + "..."
        names = [symbol["name"] for symbol in node.symbols[:5]]
        more = node.symbol_total - len(node.symbols)
        symbols_line = ", ".join(names)
        if more > 0:
            symbols_line += " +" + str(more) + " more"
        parts = [
            "<b>" + _escape_markup(node.label) + "</b>",
            _escape_markup(node.role + " | " + node.group + " | " + node.language),
        ]
        if doc:
            parts.append(_escape_markup(doc))
        parts.append(
            _escape_markup(
                "symbols: " + str(node.symbol_total) + (" (" + symbols_line + ")" if symbols_line else "")
            )
        )
        return "<br>".join(parts)

    def _template(self) -> str:
        """Return the vis.js viewer document template.

        Returns:
            HTML template with replacement tokens for map content.
        """
        return """<!DOCTYPE html>
<html lang="en" data-theme="__MAP_THEME__" data-preset="__MAP_PRESET__">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__MAP_TITLE__ | Live System Map</title>
<link href="__VIS_CSS__" rel="stylesheet">
<script src="__VIS_JS__"></script>
<style>
:root{--canvas:#020617;--mask:#0f172a;--ink:#ffffff;--muted:#94a3b8;--border:#1e293b;--box:#0f172a;--boxink:#ffffff}
html[data-theme="light"]{--canvas:#f8fafc;--mask:#ffffff;--ink:#0f172a;--muted:#475569;--border:#e2e8f0;--box:#ffffff;--boxink:#0f172a}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.toolbar{display:flex;gap:8px;align-items:center;padding:10px 14px;background:var(--mask);border-bottom:1px solid var(--border);flex-wrap:wrap}
.brand{font-weight:700;font-size:14px;letter-spacing:.04em}
.kind{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.12em}
.live{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;border:1px solid var(--border);border-radius:999px;padding:3px 10px}
.toolbar input{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;min-width:220px;font:inherit;font-size:12px}
.toolbar button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font:inherit;font-size:12px;cursor:pointer;min-height:32px}
.toolbar button:hover,.toolbar button:focus-visible{border-color:#22d3ee;outline:2px solid #22d3ee;outline-offset:2px}
.home-link{color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font-size:12px;text-decoration:none;background:var(--canvas)}
.home-link:hover,.home-link:focus-visible{border-color:#22d3ee;outline:2px solid #22d3ee;outline-offset:2px}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 320px;min-height:calc(100vh - 53px)}
.stage{position:relative;padding:16px;overflow:auto}
#network{width:100%;height:78vh;min-height:520px;background:var(--canvas);border:1px solid var(--border);border-radius:16px}
#network:focus-visible{outline:2px solid #22d3ee;outline-offset:3px}
.symbols{font-size:11px;margin-top:10px;overflow:auto}
.symbols table{width:100%;border-collapse:collapse}
.symbols th{text-align:left;color:var(--muted);font-weight:400;border-bottom:1px solid var(--border);padding:3px 4px}
.symbols td{border-bottom:1px solid var(--border);padding:3px 4px;vertical-align:top}
.symbols code{font-size:11px}
.symbols .filedoc{color:var(--muted);margin:0 0 8px;line-height:1.6}
.symbols .neighbors{color:var(--muted);margin:8px 0 0;line-height:1.6}
.passport{background:var(--mask);border-left:1px solid var(--border);padding:16px;overflow:auto}
.passport h2{font-size:13px;margin:0 0 8px}
.passport .row{font-size:12px;color:var(--muted);margin:6px 0;line-height:1.7}
.counts{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.chip{border:1px solid var(--border);border-radius:999px;padding:3px 10px;font-size:11px;color:var(--ink);background:transparent;cursor:pointer;font:inherit}
.legend-title{width:100%;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 2px}
.legend-item{display:flex;align-items:center;gap:8px;width:100%;text-align:left;background:transparent;color:var(--ink);border:1px solid transparent;border-radius:8px;padding:5px 6px;font:inherit;font-size:12px;cursor:pointer}
.legend-item:hover,.legend-item:focus-visible{border-color:var(--border);background:var(--canvas);outline:none}
.swatch{flex:none;width:12px;height:12px;border-radius:50%;box-shadow:0 0 10px currentColor}
.views{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
.views button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:6px 9px;font:inherit;font-size:11px;cursor:pointer}
.journey{font-size:12px;line-height:1.7}
.receipt{font-size:11px;color:var(--muted);border:1px solid var(--border);border-radius:8px;padding:8px;margin-top:10px}
.routebox{display:flex;gap:6px;margin-top:8px}
.routebox input{flex:1;background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:7px;font:inherit;font-size:12px;min-width:0}
.routebox button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:7px 10px;font:inherit;font-size:12px;cursor:pointer}
.present .layout{grid-template-columns:minmax(0,1fr)}
.present .passport{display:none}
.passport.focused .guide{display:none!important}
.filedoc.clamp{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden;cursor:pointer}
.peek{position:fixed;z-index:20;pointer-events:none;max-width:340px;background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:12px;padding:10px 12px;font-size:11.5px;line-height:1.55;box-shadow:0 18px 40px rgba(0,0,0,.35);display:none}
.peek b{font-size:13px}
.peek .m{color:var(--muted)}
.peek .sw{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px}
.peek ul{margin:6px 0 0;padding-left:16px}
.detail-nav{display:flex;gap:6px;margin:0 0 10px}
.detail-nav button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:4px 9px;font:inherit;font-size:11px;cursor:pointer}
.detail-nav button:disabled{opacity:.4;cursor:default}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:8px 0}
.tile{border:1px solid var(--border);border-radius:9px;padding:6px;background:var(--canvas);text-align:center}
.tile b{display:block;font-size:15px}
.tile span{font-size:9.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.ego{display:block;width:100%;height:auto;margin:6px 0 4px;border:1px solid var(--border);border-radius:10px;background:var(--canvas)}
.ego g[data-node]{cursor:pointer}
.ego g[data-node]:hover circle{stroke-width:3}
.ego text{font-family:inherit;font-size:10.5px;fill:var(--ink)}
.ego .cap{fill:var(--muted);font-size:9.5px;letter-spacing:.08em}
.nbs{display:flex;flex-wrap:wrap;gap:5px;margin:4px 0 8px}
.nbs button{display:inline-flex;align-items:center;gap:5px;background:transparent;color:var(--ink);border:1px solid var(--border);border-radius:999px;padding:2px 9px;font:inherit;font-size:11px;cursor:pointer}
.nbs button:hover,.nbs button:focus-visible{border-color:#22d3ee;outline:none}
.nbs i{width:8px;height:8px;border-radius:50%}
.sublabel{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-top:8px}
.symfilter{width:100%;background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:6px 8px;font:inherit;font-size:11.5px;margin:4px 0 6px}
dialog{background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:12px;max-width:520px}
dialog kbd{border:1px solid var(--border);border-radius:6px;padding:1px 6px;font-size:11px}
@media (max-width:960px){.layout{grid-template-columns:minmax(0,1fr)}.passport{border-left:none;border-top:1px solid var(--border)}}
</style>
</head>
<body>
<header class="toolbar" aria-label="Map controls">
<span class="brand">System Maps</span>
<span class="live">Live physics</span>
__HOME_LINK__
<span class="kind">__MAP_KIND__ | __MAP_TITLE__</span>
<input id="search" type="search" placeholder="Search nodes ( / )" aria-label="Search nodes" title="Filter nodes by label or id. Shortcut: /">
<button type="button" data-action="reach-up" aria-label="Trace upstream reach" title="Show everything that reaches the focused node (authored relationships only)">Upstream</button>
<button type="button" data-action="reach-down" aria-label="Trace downstream reach" title="Show everything the focused node reaches (authored relationships only)">Downstream</button>
<button type="button" data-action="lens" aria-label="Compare roles" title="Highlight one semantic role and compare counts; activate again to clear">Lens</button>
<button type="button" data-action="views-prev" aria-label="Previous chapter" title="Show the previous guided chapter ( [ )">Prev</button>
<button type="button" data-action="views-next" aria-label="Next chapter" title="Show the next guided chapter ( ] )">Next</button>
<button type="button" data-action="color" aria-label="Toggle color mode" title="Color nodes by code community or by architectural role ( C )">Color</button>
<button type="button" data-action="show-all" aria-label="Show all nodes" title="Clear focus, lens, and filters ( Esc )">Show all</button>
<button type="button" data-action="play" aria-label="Play guided story" title="Play all guided chapters in order">Play</button>
<button type="button" data-action="stabilize" aria-label="Stabilize layout" title="Re-run the physics stabilization">Stabilize</button>
<button type="button" data-action="physics" aria-label="Toggle physics" title="Freeze or resume the live physics engine">Physics</button>
<button type="button" data-action="present" aria-label="Enter presentation stage" title="Hide the side panel for presenting">Present</button>
<button type="button" data-action="style" aria-label="Cycle visual preset" title="Cycle visual preset: classic, flow, blueprint, editorial">Style</button>
<button type="button" data-action="theme" aria-label="Toggle theme" title="Toggle dark and light themes">Theme</button>
<button type="button" data-action="export" aria-label="Open export menu" title="Download a PNG snapshot or the typed JSON">Export</button>
<button type="button" data-action="help" aria-label="Open diagram guide" title="Open the diagram guide with every shortcut">?</button>
</header>
<div class="layout">
<main class="stage">
<div id="network" tabindex="0" role="application" aria-label="__MAP_TITLE__ live network. Drag nodes to rearrange them."></div>
</main>
<aside class="passport" aria-live="polite" aria-label="Semantic passport">
<h2 id="passport-title">Diagram guide</h2>
<div class="row" id="passport-meta"></div>
<div class="views guide" id="chapters"></div>
<div class="counts guide" id="role-counts"></div>
<div class="row guide">Node size = number of links. Color = code community (press C for roles). Labels show the most connected files; zoom in for the rest.</div>
<div class="row guide">1. Drag any node; physics settles the rest. 2. Click a node to focus it. 3. Upstream and Downstream trace authored reach. 4. Path probes the exact route between two ids. 5. Play walks the guided chapters. Press ? for every shortcut. This page loads its network engine from a CDN and needs network access.</div>
<div class="routebox"><input id="route-from" placeholder="route from id" aria-label="Route source" title="Source node id for the route probe"><input id="route-to" placeholder="route to id" aria-label="Route target" title="Target node id for the route probe"><button type="button" data-action="route" aria-label="Probe directed route" title="Highlight the shortest authored directed path">Path</button></div>
<div class="journey" id="journey"></div>
<div class="symbols" id="node-symbols"></div>
<div class="receipt" id="receipt"></div>
</aside>
</div>
<dialog id="guide" aria-label="Diagram guide dialog">
<h2>Diagram guide</h2>
<p><kbd>/</kbd> search &middot; <kbd>R</kbd> route probe &middot; <kbd>L</kbd> role lens &middot; <kbd>P</kbd> play &middot; <kbd>[</kbd> <kbd>]</kbd> chapters &middot; <kbd>C</kbd> color by community or role &middot; <kbd>Esc</kbd> show all &middot; <kbd>F</kbd> present &middot; <kbd>S</kbd> style &middot; <kbd>T</kbd> theme &middot; <kbd>E</kbd> export &middot; <kbd>+</kbd> <kbd>-</kbd> <kbd>0</kbd> zoom &middot; <kbd>B</kbd> physics</p>
<p>Drag nodes freely; Stabilize re-runs the physics engine and Physics freezes it. Reach, routes, lens, and chapters reuse authored relationships only. Deep links restore <code>#focus=id</code>, <code>#focus=id&amp;reach=upstream|downstream</code>, <code>#route=a~b</code>, <code>#lens=role</code>, and <code>#view=id</code>.</p>
<button type="button" data-action="close-guide" title="Close the diagram guide">Close</button>
</dialog>
<dialog id="exports" aria-label="Export dialog">
<h2>Export</h2>
<p>PNG captures the live canvas; JSON carries the typed source.</p>
<button type="button" data-action="export-png" title="Download a PNG snapshot of the live canvas">Download PNG</button>
<button type="button" data-action="export-json" title="Download the typed JSON behind this diagram">Download typed JSON</button>
<button type="button" data-action="close-exports" title="Close the export menu">Close</button>
</dialog>
<script type="application/json" id="vis-nodes">__NODES_JSON__</script>
<script type="application/json" id="vis-edges">__EDGES_JSON__</script>
<script type="application/json" id="vis-views">__VIEWS_JSON__</script>
<script type="application/json" id="vis-meta">__META_JSON__</script>
<script type="application/json" id="vis-physics">__PHYSICS_JSON__</script>
<script type="application/json" id="vis-roles">__ROLES_JSON__</script>
<script>
(function(){
"use strict";
var rawNodes=JSON.parse(document.getElementById("vis-nodes").textContent||"[]");
var rawEdges=JSON.parse(document.getElementById("vis-edges").textContent||"[]");
var views=JSON.parse(document.getElementById("vis-views").textContent||"[]");
var meta=JSON.parse(document.getElementById("vis-meta").textContent||"{}");
var physics=JSON.parse(document.getElementById("vis-physics").textContent||"{}");
var roleColors=JSON.parse(document.getElementById("vis-roles").textContent||"{}");
var root=document.documentElement;
var container=document.getElementById("network");
var search=document.getElementById("search");
var passportTitle=document.getElementById("passport-title");
var passportMeta=document.getElementById("passport-meta");
var journey=document.getElementById("journey");
var receipt=document.getElementById("receipt");
var chapters=document.getElementById("chapters");
var roleCounts=document.getElementById("role-counts");
var nodeSymbols=document.getElementById("node-symbols");
var guide=document.getElementById("guide");
var exportsDialog=document.getElementById("exports");
var state={focus:null,reach:null,lens:null,view:-1,physicsOn:true};
var reduced=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
function themeBox(){return root.getAttribute("data-theme")==="light"?{box:"#ffffff",ink:"#0f172a"}:{box:"#0f172a",ink:"#ffffff"};}
var communities=meta.communities||[];
var communityColor={};communities.forEach(function(c){communityColor[c.id]=c.color;});
state.colorMode=communities.length?"community":"role";
var degree={};rawNodes.forEach(function(n){degree[n.id]=0;});
rawEdges.forEach(function(e){if(e.from in degree){degree[e.from]++;}if(e.to in degree){degree[e.to]++;}});
var ranked=rawNodes.slice().sort(function(a,b){return (degree[b.id]-degree[a.id])||(a.id<b.id?-1:1);});
var labelled={};ranked.slice(0,meta.labelTopN||25).forEach(function(n){labelled[n.id]=true;});
function colorFor(n){if(state.colorMode==="community"&&n.community>=0&&communityColor[n.community]){return communityColor[n.community];}return roleColors[n.group]||"#94a3b8";}
var dimSet=null;
function paintNodes(){
var palette=themeBox();
var update=rawNodes.map(function(n){var dim=dimSet&&!dimSet[n.id];var c=dim?"rgba(100,116,139,0.18)":colorFor(n);
return {id:n.id,color:{background:c,border:dim?"rgba(100,116,139,0.25)":palette.box,highlight:{background:colorFor(n),border:palette.ink},hover:{background:colorFor(n),border:palette.ink}},
font:{color:dim?"rgba(148,163,184,0.35)":palette.ink,size:labelled[n.id]||(dimSet&&!dim)?22:14,face:"monospace",strokeWidth:5,strokeColor:palette.box},
label:(labelled[n.id]||allLabels||(dimSet&&!dim))?n.label:" "};});
visNodes.update(update);
if(typeof visEdges!=="undefined"){visEdges.update(rawEdges.map(function(e,index){var on=dimSet&&dimSet[e.from]&&dimSet[e.to];
return {id:"e"+index,width:on?2.2:1,color:{color:on?"#22d3ee":"#64748b",opacity:dimSet?(on?0.95:0.08):0.28,highlight:"#22d3ee",hover:"#22d3ee",inherit:false}};}));}
renderLegend();}
function setDim(allowed){dimSet=allowed;paintNodes();}
var allLabels=false;
var visNodes=new vis.DataSet(rawNodes.map(function(n){return {id:n.id,label:labelled[n.id]?n.label:" ",group:n.group,shape:"dot",value:1+degree[n.id]};}));
function syncLabels(scale){var want=scale>=1.1;if(want===allLabels){return;}allLabels=want;
visNodes.update(rawNodes.filter(function(n){return !labelled[n.id]&&!(dimSet&&dimSet[n.id]);}).map(function(n){return {id:n.id,label:want?n.label:" "};}));}
var visEdges=new vis.DataSet(rawEdges.map(function(e,index){return {id:"e"+index,from:e.from,to:e.to,title:e.label,arrows:{to:{enabled:true,scaleFactor:0.45}},dashes:!!e.dashes,smooth:{type:"continuous"},color:{color:"#64748b",opacity:0.28,highlight:"#22d3ee",hover:"#22d3ee",inherit:false},width:1,selectionWidth:2,hoverWidth:1.5};}));
var network=new vis.Network(container,{nodes:visNodes,edges:visEdges},{
physics:physics,
interaction:{hover:true,hoverConnectedEdges:true,selectConnectedEdges:true,navigationButtons:false,keyboard:false,tooltipDelay:120},
nodes:{shape:"dot",borderWidth:2,scaling:{min:7,max:38,label:{enabled:false}}},
edges:{smooth:{type:"continuous"}}});
paintNodes();
if(reduced&&physics.enabled){try{network.stabilize(50);}catch(e){}}
function outgoing(id){return rawEdges.filter(function(e){return e.from===id;});}
function incoming(id){return rawEdges.filter(function(e){return e.to===id;});}
function nodeById(id){for(var i=0;i<rawNodes.length;i++){if(rawNodes[i].id===id){return rawNodes[i];}}return null;}
function escapeHtml(text){
return String(text==null?"":text).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function neighborNames(ids){
var cap=(meta.neighbors||8);
return ids.slice().sort().slice(0,cap).map(function(id){var n=nodeById(id);return escapeHtml(n?n.label:id);});}
var detailHistory=[];
function uniq(list){var seen={};return list.filter(function(x){if(seen[x]){return false;}seen[x]=true;return true;});}
function short(text,n){text=String(text||"");return text.length>n?text.slice(0,n-1)+"…":text;}
function egoSvg(node,ins,outs){
var cap=7,rowH=26,leftL=ins.slice(0,cap),rightL=outs.slice(0,cap);
var rows=Math.max(1,leftL.length,rightL.length);var h=Math.max(120,rows*rowH+46);var w=288,cx=w/2,cy=h/2+6;
var svg='<svg class="ego" viewBox="0 0 '+w+' '+h+'" role="img" aria-label="Neighbourhood of '+escapeHtml(node.label)+'">';
svg+='<text class="cap" x="8" y="14">USED BY '+ins.length+'</text><text class="cap" x="'+(w-8)+'" y="14" text-anchor="end">IMPORTS '+outs.length+'</text>';
function col(list,x,anchor,dir){var out="";var top=cy-((list.length-1)*rowH)/2;
list.forEach(function(id,i){var n=nodeById(id);var y=top+i*rowH;var c=n?colorFor(n):"#94a3b8";
out+='<path d="M'+(dir<0?x+6:cx+16)+' '+(dir<0?y:cy)+' C'+(cx+(dir<0?-60:60)*0.5)+' '+(dir<0?y:cy)+' '+(cx+(dir<0?-60:60)*0.5)+' '+(dir<0?cy:y)+' '+(dir<0?cx-16:x-6)+' '+(dir<0?cy:y)+'" fill="none" stroke="'+c+'" stroke-opacity="0.55" stroke-width="1.4"/>';
out+='<g data-node="'+escapeHtml(id)+'"><title>'+escapeHtml(id)+'</title><circle cx="'+x+'" cy="'+y+'" r="6" fill="'+c+'" stroke="var(--canvas)" stroke-width="2"/>';
out+='<text x="'+(anchor==="end"?x-10:x+10)+'" y="'+(y+3.5)+'" text-anchor="'+anchor+'">'+escapeHtml(short(n?n.label:id,12))+'</text></g>';});
return out;}
svg+=col(leftL,94,"end",-1);svg+=col(rightL,w-94,"start",1);
if(ins.length>cap){svg+='<text class="cap" x="8" y="'+(h-6)+'">+'+(ins.length-cap)+' more</text>';}
if(outs.length>cap){svg+='<text class="cap" x="'+(w-8)+'" y="'+(h-6)+'" text-anchor="end">+'+(outs.length-cap)+' more</text>';}
svg+='<circle cx="'+cx+'" cy="'+cy+'" r="14" fill="'+colorFor(node)+'" stroke="#22d3ee" stroke-width="2.5"/>';
svg+='<text x="'+cx+'" y="'+(cy-22)+'" text-anchor="middle" style="font-weight:700">'+escapeHtml(short(node.label,18))+'</text>';
return svg+"</svg>";}
function chipList(ids){
var cap=(meta.neighbors||8)*3;
return '<div class="nbs">'+ids.slice(0,cap).map(function(id){var n=nodeById(id);return '<button type="button" data-goto="'+escapeHtml(id)+'" title="'+escapeHtml(id)+'"><i style="background:'+(n?colorFor(n):"#94a3b8")+'"></i>'+escapeHtml(n?n.label:id)+'</button>';}).join("")+(ids.length>cap?'<span class="sublabel">+'+(ids.length-cap)+' more</span>':"")+"</div>";}
function renderNodeDetail(node){
if(!nodeSymbols){return;}
var ins=uniq(incoming(node.id).map(function(e){return e.from;})).sort(function(a,b){return degree[b]-degree[a]||(a<b?-1:1);});
var outs=uniq(outgoing(node.id).map(function(e){return e.to;})).sort(function(a,b){return degree[b]-degree[a]||(a<b?-1:1);});
var rank=ranked.indexOf(node)+1;
var html='<div class="detail-nav"><button type="button" data-detail="back" '+(detailHistory.length?"":"disabled")+' title="Previous node (Backspace)">&larr; Back</button><button type="button" data-detail="fit" title="Zoom to this neighbourhood">Fit</button><button type="button" data-detail="clear" title="Clear focus (Esc)">Clear</button></div>';
if(node.communityLabel){html+='<div class="nbs"><button type="button" data-community="'+node.community+'" title="Isolate this community"><i style="background:'+(communityColor[node.community]||"#94a3b8")+'"></i>'+escapeHtml(node.communityLabel)+'</button></div>';}
html+='<div class="tiles"><div class="tile"><b>'+(node.symbolTotal||0)+'</b><span>symbols</span></div><div class="tile"><b>'+ins.length+'</b><span>used by</span></div><div class="tile"><b>'+outs.length+'</b><span>imports</span></div><div class="tile"><b>#'+rank+'</b><span>by links</span></div></div>';
if(node.doc){html+='<p class="filedoc clamp" title="Click to expand" data-clamp="1">'+escapeHtml(node.doc)+"</p>";}
html+=egoSvg(node,ins,outs);
if(ins.length){html+='<div class="sublabel">Used by</div>'+chipList(ins);}
if(outs.length){html+='<div class="sublabel">Imports</div>'+chipList(outs);}
var symbols=node.symbols||[];
if(symbols.length){
html+='<div class="sublabel">Symbols</div><input class="symfilter" id="symfilter" type="search" placeholder="filter symbols" aria-label="Filter symbols">';
html+='<table><thead><tr><th>Symbol</th><th>Kind</th><th>Line</th></tr></thead><tbody id="symrows">';
symbols.forEach(function(s){
var docTitle=s.doc?(' title="'+escapeHtml(s.doc)+'"'):"";
var name="<span"+docTitle+"><b>"+escapeHtml(s.name)+"</b></span>"+(s.signature?" <code>"+escapeHtml(s.signature)+"</code>":"")+(s.doc?'<div class="filedoc" style="margin:2px 0 0">'+escapeHtml(s.doc)+"</div>":"");
html+='<tr data-name="'+escapeHtml(String(s.name).toLowerCase())+'"><td>'+name+"</td><td>"+escapeHtml(s.kind)+"</td><td>"+escapeHtml(s.line)+"</td></tr>";});
html+="</tbody></table>";
var hidden=(node.symbolTotal||symbols.length)-symbols.length;
if(hidden>0){html+='<p class="filedoc">+'+hidden+' more symbols in source.</p>';}}
else{html+='<p class="filedoc">No symbols extracted.</p>';}
nodeSymbols.innerHTML=html;
var filter=document.getElementById("symfilter");
if(filter){filter.addEventListener("input",function(){var q=filter.value.trim().toLowerCase();nodeSymbols.querySelectorAll("#symrows tr").forEach(function(tr){tr.style.display=!q||tr.getAttribute("data-name").indexOf(q)>=0?"":"none";});});}}
function clearNodeDetail(){
if(nodeSymbols){nodeSymbols.innerHTML="";}
passportTitle.textContent="Diagram guide";}
function clearNodeDetailSilent(){
if(nodeSymbols){nodeSymbols.innerHTML="";}}
function bfsReach(start,direction){
var seen={};seen[start]=0;var queue=[start];var order=[start];
while(queue.length){var current=queue.shift();var nexts=direction==="downstream"?outgoing(current):incoming(current);
for(var i=0;i<nexts.length;i++){var nid=direction==="downstream"?nexts[i].to:nexts[i].from;
if(!(nid in seen)){seen[nid]=seen[current]+1;queue.push(nid);order.push(nid);}}}
return {members:order,hops:seen};}
function bfsRoute(from,to){
if(from===to){return [from];}
var prev={};var seen={};seen[from]=true;var queue=[from];
while(queue.length){var current=queue.shift();var nexts=outgoing(current);
for(var i=0;i<nexts.length;i++){var nid=nexts[i].to;
if(!(nid in seen)){seen[nid]=true;prev[nid]=current;
if(nid===to){var path=[to];var c=to;while(c!==from){c=prev[c];path.unshift(c);}return path;}
queue.push(nid);}}}
return [];}
function showOnly(allowed){
var nodeUpdate=rawNodes.map(function(n){return {id:n.id,hidden:!allowed[n.id]};});
visNodes.update(nodeUpdate);
var edgeUpdate=rawEdges.map(function(e,index){return {id:"e"+index,hidden:!(allowed[e.from]&&allowed[e.to])};});
visEdges.update(edgeUpdate);}
function showAll(){
var pp=document.querySelector(".passport");if(pp){pp.classList.remove("focused");}
if(dimSet){dimSet=null;paintNodes();}
var nodeUpdate=rawNodes.map(function(n){return {id:n.id,hidden:false};});
visNodes.update(nodeUpdate);
var edgeUpdate=rawEdges.map(function(e,index){return {id:"e"+index,hidden:false};});
visEdges.update(edgeUpdate);}
function setHash(value){try{history.replaceState(null,"",value);}catch(e){location.hash=value;}}
function focusNode(id,reach,fromHistory){
var node=nodeById(id);if(!node){return;}
if(state.focus&&state.focus!==id&&!fromHistory){detailHistory.push(state.focus);}
state.focus=id;state.reach=reach||null;
var allowed={};allowed[id]=true;
if(state.reach){var found=bfsReach(id,state.reach);found.members.forEach(function(m){allowed[m]=true;});
var hops=0;for(var k in found.hops){if(found.hops[k]>hops){hops=found.hops[k];}}
receipt.textContent=(state.reach==="downstream"?"Downstream":"Upstream")+" reach: "+found.members.length+" nodes, "+hops+" max hops. Authored relationships only.";}
else{receipt.textContent="In: "+incoming(id).length+" | Out: "+outgoing(id).length+" | Views: "+views.length;
incoming(id).forEach(function(e){allowed[e.from]=true;});outgoing(id).forEach(function(e){allowed[e.to]=true;});}
if(state.reach){setDim(null);showOnly(allowed);}else{showAll();setDim(allowed);}
document.querySelector(".passport").classList.add("focused");
network.selectNodes([id]);
try{network.fit({nodes:Object.keys(allowed),animation:reduced?false:{duration:600,easingFunction:"easeInOutQuad"}});}catch(e){}
setTimeout(function(){if(state.focus===id&&dimSet){try{network.fit({nodes:Object.keys(dimSet),animation:reduced?false:{duration:500}});}catch(e){}}},1600);
passportTitle.textContent=node.label;
passportMeta.textContent=node.id+" | role "+node.group+" | "+(node.language||"")+" | "+(node.symbolTotal||0)+" symbols";
renderNodeDetail(node);
var hash="#focus="+encodeURIComponent(id);
if(state.reach){hash+="&reach="+state.reach;}
setHash(hash);}
function probeRoute(){
var from=document.getElementById("route-from").value.trim();
var to=document.getElementById("route-to").value.trim();
if(!from||!to){return;}
var path=bfsRoute(from,to);
if(!path.length){journey.textContent="No authored directed route from "+from+" to "+to+".";receipt.textContent="Route probe: 0 links.";return;}
var allowed={};path.forEach(function(n){allowed[n]=true;});
showOnly(allowed);
network.selectNodes(path);
try{network.fit({nodes:path,animation:reduced?false:{duration:600}});}catch(e){}
var names=path.map(function(n){var node=nodeById(n);return node?node.label:n;});
journey.textContent="Journey: "+names.join(" -> ")+" ("+(path.length-1)+" hops).";
receipt.textContent="Route probe: "+path.length+" nodes, "+(path.length-1)+" links.";
setHash("#route="+encodeURIComponent(from)+"~"+encodeURIComponent(to));}
function applyLens(role){
state.lens=role;
if(!role){showAll();clearNodeDetail();receipt.textContent="Lens cleared.";setHash("#");return;}
var counts={};rawNodes.forEach(function(n){counts[n.group]=(counts[n.group]||0)+1;});
var allowed={};rawNodes.forEach(function(n){if(n.group===role){allowed[n.id]=true;}});
showOnly(allowed);
var parts=[];for(var k in counts){parts.push(k+": "+counts[k]);}
receipt.textContent="Lens "+role+": "+(counts[role]||0)+" of "+rawNodes.length+" nodes. "+parts.join(" | ");
setHash("#lens="+encodeURIComponent(role));}
function showView(index){
if(!views.length){return;}
state.view=(index+views.length)%views.length;
var view=views[state.view];
chapters.querySelectorAll("button").forEach(function(b,i){b.disabled=(i===state.view);});
passportTitle.textContent=view.title;
passportMeta.textContent=view.description||"";
clearNodeDetailSilent();
if(!view.focus.length){showAll();}
else{var allowed={};view.focus.forEach(function(n){allowed[n]=true;});showOnly(allowed);network.selectNodes(view.focus);}
journey.textContent=view.focus.length?("Chapter focus: "+view.focus.join(", ")):"";
receipt.textContent="Chapter "+(state.view+1)+" of "+views.length+".";
setHash("#view="+encodeURIComponent(view.id));}
function renderChapters(){
chapters.innerHTML="";
views.forEach(function(view,index){var b=document.createElement("button");b.type="button";b.textContent=view.title;b.setAttribute("aria-label","Show chapter "+view.title);b.setAttribute("title","Focus the "+view.title+" chapter");b.addEventListener("click",function(){showView(index);});chapters.appendChild(b);});}
function renderLegend(){
if(!roleCounts){return;}
roleCounts.innerHTML="";
var title=document.createElement("div");title.className="legend-title";
title.textContent=state.colorMode==="community"?"Communities (click to isolate)":"Roles (click to isolate)";roleCounts.appendChild(title);
var items=[];
if(state.colorMode==="community"){communities.forEach(function(c){items.push({key:"c"+c.id,label:c.label,color:c.color,count:c.size,pick:function(){isolateCommunity(c.id,c.label);}});});}
else{var counts={};rawNodes.forEach(function(n){counts[n.group]=(counts[n.group]||0)+1;});
Object.keys(counts).sort().forEach(function(role){items.push({key:role,label:role,color:roleColors[role]||"#94a3b8",count:counts[role],pick:function(){applyLens(role);}});});}
items.forEach(function(item){var b=document.createElement("button");b.type="button";b.className="legend-item";
var sw=document.createElement("span");sw.className="swatch";sw.style.background=item.color;b.appendChild(sw);
var tx=document.createElement("span");tx.textContent=item.label+" ("+item.count+")";b.appendChild(tx);
b.setAttribute("title","Show only "+item.label);b.addEventListener("click",item.pick);roleCounts.appendChild(b);});}
function isolateCommunity(cid,label){
var allowed={};var count=0;rawNodes.forEach(function(n){if(n.community===cid){allowed[n.id]=true;count++;}});
showOnly(allowed);try{network.fit({nodes:Object.keys(allowed),animation:reduced?false:{duration:600}});}catch(e){}
receipt.textContent="Community "+label+": "+count+" of "+rawNodes.length+" nodes. Press Esc or Show all to reset.";
setHash("#community="+cid);}
function toggleColorMode(){state.colorMode=state.colorMode==="community"?"role":"community";if(!communities.length){state.colorMode="role";}paintNodes();}
function renderRoleCounts(){renderLegend();return;
var counts={};rawNodes.forEach(function(n){counts[n.group]=(counts[n.group]||0)+1;});
roleCounts.innerHTML="";
Object.keys(counts).sort().forEach(function(role){var s=document.createElement("button");s.type="button";s.className="chip";s.textContent=role+": "+counts[role];s.setAttribute("aria-label","Filter role "+role);s.setAttribute("title","Highlight the "+role+" role");s.addEventListener("click",function(){applyLens(role);});roleCounts.appendChild(s);});}
function cyclePreset(){
var presets=["classic","flow","blueprint","editorial"];
var current=root.getAttribute("data-preset")||"classic";
root.setAttribute("data-preset",presets[(presets.indexOf(current)+1)%presets.length]);}
function toggleTheme(){
var current=root.getAttribute("data-theme")||"dark";
root.setAttribute("data-theme",current==="dark"?"light":"dark");
paintNodes();}
function togglePhysics(){
state.physicsOn=!state.physicsOn;
try{network.setOptions({physics:{enabled:state.physicsOn}});}catch(e){}
receipt.textContent=state.physicsOn?"Physics resumed.":"Physics frozen; nodes stay draggable.";}
function exportPNG(){
try{
var link=document.createElement("a");
link.href=network.canvas.frame.canvas.toDataURL("image/png");
link.download="system-map-"+(meta.kind||"map")+".png";
document.body.appendChild(link);link.click();
setTimeout(function(){link.remove();},400);
receipt.textContent="PNG snapshot downloaded.";
}catch(e){receipt.textContent="PNG export unavailable in this browser.";}}
function exportJSON(){
var payload={kind:meta.kind,title:meta.title,nodes:rawNodes,edges:rawEdges,views:views};
var blob=new Blob([JSON.stringify(payload,null,2)],{type:"application/json"});
var link=document.createElement("a");link.href=URL.createObjectURL(blob);link.download="system-map-"+(meta.kind||"map")+".json";document.body.appendChild(link);link.click();
setTimeout(function(){URL.revokeObjectURL(link.href);link.remove();},400);}
function readHash(){
var hash=location.hash||"";
if(hash.indexOf("#route=")===0){var parts=hash.slice(7).split("~");if(parts.length===2){document.getElementById("route-from").value=decodeURIComponent(parts[0]);document.getElementById("route-to").value=decodeURIComponent(parts[1]);probeRoute();}return;}
if(hash.indexOf("#lens=")===0){applyLens(decodeURIComponent(hash.slice(6)));return;}
if(hash.indexOf("#community=")===0){var cid=parseInt(hash.slice(11),10);communities.forEach(function(c){if(c.id===cid){isolateCommunity(c.id,c.label);}});return;}
if(hash.indexOf("#view=")===0){var id=decodeURIComponent(hash.slice(6));for(var i=0;i<views.length;i++){if(views[i].id===id){showView(i);return;}}return;}
if(hash.indexOf("#focus=")===0){var rest=hash.slice(7).split("&reach=");focusNode(decodeURIComponent(rest[0]),rest[1]?decodeURIComponent(rest[1]):null);return;}}
network.on("click",function(params){
if(params.nodes.length>0){focusNode(params.nodes[0]);}
else if(params.edges.length===0&&state.focus&&!state.reach){showAll();state.focus=null;clearNodeDetail();setHash("#");}});
var peek=document.getElementById("peek");
network.on("hoverNode",function(params){
var n=nodeById(params.node);if(!n||!peek){return;}
var ins=incoming(n.id).length,outs=outgoing(n.id).length;
var syms=(n.symbols||[]).slice(0,4).map(function(s){return "<li>"+escapeHtml(s.kind)+" <b>"+escapeHtml(s.name)+"</b> L"+escapeHtml(s.line)+"</li>";}).join("");
peek.innerHTML='<b><span class="sw" style="background:'+colorFor(n)+'"></span>'+escapeHtml(n.label)+'</b><div class="m">'+escapeHtml(n.id)+'</div>'+
'<div>'+(n.symbolTotal||0)+' symbols &middot; used by '+ins+' &middot; imports '+outs+'</div>'+
(n.communityLabel?'<div class="m">'+escapeHtml(n.communityLabel)+' &middot; '+escapeHtml(n.group)+'</div>':'<div class="m">'+escapeHtml(n.group)+'</div>')+
(n.doc?'<div style="margin-top:4px">'+escapeHtml(short(n.doc,220))+'</div>':"")+(syms?"<ul>"+syms+"</ul>":"")+'<div class="m" style="margin-top:4px">click to open passport</div>';
var p=params.event&&params.event.center?params.event.center:{x:params.pointer.DOM.x+container.getBoundingClientRect().left,y:params.pointer.DOM.y+container.getBoundingClientRect().top};
peek.style.display="block";
var left=Math.min(window.innerWidth-peek.offsetWidth-12,p.x+16),top=Math.min(window.innerHeight-peek.offsetHeight-12,p.y+16);
peek.style.left=Math.max(8,left)+"px";peek.style.top=Math.max(8,top)+"px";});
network.on("blurNode",function(){if(peek){peek.style.display="none";}});
network.on("dragStart",function(){if(peek){peek.style.display="none";}});
nodeSymbols.addEventListener("click",function(ev){
var clamp=ev.target.closest?ev.target.closest("[data-clamp]"):null;if(clamp){clamp.classList.toggle("clamp");return;}
var t=ev.target.closest?ev.target.closest("[data-goto],[data-node],[data-detail],[data-community]"):null;if(!t){return;}
var go=t.getAttribute("data-goto")||t.getAttribute("data-node");
if(go){focusNode(go);return;}
var cid=t.getAttribute("data-community");
if(cid!==null){communities.forEach(function(c){if(String(c.id)===cid){isolateCommunity(c.id,c.label);}});return;}
var act=t.getAttribute("data-detail");
if(act==="back"){var prev=detailHistory.pop();if(prev){focusNode(prev,null,true);}}
else if(act==="fit"){var ids=[state.focus];incoming(state.focus).forEach(function(e){ids.push(e.from);});outgoing(state.focus).forEach(function(e){ids.push(e.to);});try{network.fit({nodes:ids,animation:reduced?false:{duration:500}});}catch(e){}}
else if(act==="clear"){showAll();state.focus=null;detailHistory=[];clearNodeDetail();setHash("#");}});
network.on("zoom",function(p){syncLabels(p.scale);});
network.on("stabilized",function(){receipt.textContent="Physics stabilized: "+rawNodes.length+" nodes placed.";
if(state.focus&&dimSet){try{network.fit({nodes:Object.keys(dimSet),animation:reduced?false:{duration:500}});}catch(e){}}});
document.querySelectorAll("[data-action]").forEach(function(btn){
btn.addEventListener("click",function(){
var action=btn.getAttribute("data-action");
if(action==="reach-up"&&state.focus){focusNode(state.focus,"upstream");}
else if(action==="reach-down"&&state.focus){focusNode(state.focus,"downstream");}
else if(action==="route"){probeRoute();}
else if(action==="lens"){applyLens(state.lens?null:"backend");}
else if(action==="color"){toggleColorMode();}
else if(action==="show-all"){showAll();state.focus=null;try{network.fit({animation:reduced?false:{duration:500}});}catch(e){}receipt.textContent="Showing all "+rawNodes.length+" nodes.";setHash("#");}
else if(action==="views-prev"){showView(state.view-1);}
else if(action==="views-next"){showView(state.view+1);}
else if(action==="play"){var i=0;var step=function(){if(i>=views.length){return;}showView(i);i++;if(!reduced){setTimeout(step,1400);}};step();}
else if(action==="stabilize"){try{network.stabilize();}catch(e){}receipt.textContent="Stabilizing physics...";}
else if(action==="physics"){togglePhysics();}
else if(action==="present"){document.body.classList.toggle("present");}
else if(action==="style"){cyclePreset();}
else if(action==="theme"){toggleTheme();}
else if(action==="export"){if(typeof exportsDialog.showModal==="function"){exportsDialog.showModal();}}
else if(action==="help"){if(typeof guide.showModal==="function"){guide.showModal();}}
else if(action==="close-guide"){guide.close();}
else if(action==="close-exports"){exportsDialog.close();}
else if(action==="export-png"){exportPNG();}
else if(action==="export-json"){exportJSON();}});});
search.addEventListener("input",function(){
var term=search.value.trim().toLowerCase();
if(!term){showAll();return;}
var allowed={};rawNodes.forEach(function(n){
if(n.label.toLowerCase().indexOf(term)>=0||n.id.toLowerCase().indexOf(term)>=0){allowed[n.id]=true;}});
showOnly(allowed);});
document.addEventListener("keydown",function(ev){
if(ev.target&&(ev.target.tagName==="INPUT"||ev.target.tagName==="TEXTAREA")){return;}
if(ev.key==="/"){ev.preventDefault();search.focus();}
else if(ev.key==="R"||ev.key==="r"){var f=document.getElementById("route-from");if(f){f.focus();}}
else if(ev.key==="L"||ev.key==="l"){applyLens(state.lens?null:"backend");}
else if(ev.key==="P"||ev.key==="p"){showView(state.view+1);}
else if(ev.key==="["){showView(state.view-1);}
else if(ev.key==="]"){showView(state.view+1);}
else if(ev.key==="B"||ev.key==="b"){togglePhysics();}
else if(ev.key==="F"||ev.key==="f"){document.body.classList.toggle("present");}
else if(ev.key==="S"||ev.key==="s"){cyclePreset();}
else if(ev.key==="T"||ev.key==="t"){toggleTheme();}
else if(ev.key==="E"||ev.key==="e"){if(typeof exportsDialog.showModal==="function"){exportsDialog.showModal();}}
else if(ev.key==="?"){if(typeof guide.showModal==="function"){guide.showModal();}}
else if(ev.key==="+"){try{network.zoomIn();}catch(e){}}
else if(ev.key==="-"){try{network.zoomOut();}catch(e){}}
else if(ev.key==="0"){try{network.fit();}catch(e){}}
else if(ev.key==="C"||ev.key==="c"){toggleColorMode();}
else if(ev.key==="Backspace"){var prev=detailHistory.pop();if(prev){ev.preventDefault();focusNode(prev,null,true);}}
else if(ev.key==="Escape"){showAll();state.focus=null;detailHistory=[];}});
passportMeta.textContent=(meta.nodeCount||rawNodes.length)+" of "+(meta.totalFiles||rawNodes.length)+" files | "+(meta.edgeCount||rawEdges.length)+" links | "+views.length+" chapters. Primary scope only; full listing lives in the knowledge base.";
receipt.textContent="Live physics network. Drag nodes, search, focus, trace reach, probe routes, compare roles, or play chapters.";
renderChapters();renderRoleCounts();readHash();
})();
</script>
</body>
</html>"""
_GALLERY_HEAD = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ | System Maps</title>
<style>
:root{--canvas:#020617;--mask:#0f172a;--mask2:#111c33;--ink:#ffffff;--muted:#94a3b8;--border:#1e293b;--accent:#22d3ee;--accent2:#f472b6;--code:#0b1226;--kw:#c084fc;--str:#86efac;--fn:#fcd34d;--cm:#64748b;--glow:rgba(34,211,238,.18)}
html[data-theme="light"]{--canvas:#f8fafc;--mask:#ffffff;--mask2:#f1f5f9;--ink:#0f172a;--muted:#475569;--border:#e2e8f0;--code:#f1f5f9;--cm:#94a3b8;--accent:#0891b2;--accent2:#db2777;--glow:rgba(8,145,178,.12)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;line-height:1.5}
a{color:var(--accent)}
.muted{color:var(--muted);font-size:12px}
.backdrop{position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(900px 420px at 15% -10%,var(--glow),transparent 70%),radial-gradient(700px 380px at 95% 0%,rgba(244,114,182,.10),transparent 70%)}
.backdrop::after{content:"";position:absolute;left:-50%;right:-50%;bottom:-40%;height:70%;background-image:linear-gradient(var(--border) 1px,transparent 1px),linear-gradient(90deg,var(--border) 1px,transparent 1px);background-size:44px 44px;transform:perspective(500px) rotateX(62deg);opacity:.35;animation:grid 14s linear infinite;mask-image:linear-gradient(to top,#000,transparent)}
@keyframes grid{to{background-position:0 44px,0 0}}
.hero,.section,.toolbar,footer{max-width:1120px;margin:0 auto;padding-left:20px;padding-right:20px}
.hero{padding-top:40px;padding-bottom:12px}
.eyebrow{color:var(--accent);font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin:0 0 8px}
.hero h1{font-size:30px;margin:0 0 10px;background:linear-gradient(90deg,var(--ink),var(--accent) 70%,var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.hero h1 span{font-weight:400}
.lede{color:var(--muted);font-size:13px;max-width:760px;margin:0 0 18px}
.stats-line{color:var(--muted);font-size:11px;margin:10px 0 0}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px}
.tile{background:linear-gradient(160deg,var(--mask2),var(--mask));border:1px solid var(--border);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column}
.tile .num{font-size:26px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums}
.tile .label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.section{padding-top:22px;padding-bottom:10px}
.section h2{font-size:17px;margin:0 0 6px}
.starts{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;margin-top:10px}
.start{display:flex;gap:12px;align-items:flex-start;text-align:left;background:var(--mask);border:1px solid var(--border);border-radius:14px;padding:14px;color:var(--ink);text-decoration:none;font:inherit;font-size:13px;cursor:pointer;transition:transform .2s,border-color .2s,box-shadow .2s}
.start:hover,.start:focus-visible{transform:translateY(-2px);border-color:var(--accent);box-shadow:0 8px 28px var(--glow);outline:none}
.step{flex:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:var(--canvas);font-weight:700;font-size:13px}
.toolbar{position:sticky;top:0;z-index:5;display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding-top:12px;padding-bottom:12px;background:color-mix(in srgb,var(--canvas) 85%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--border)}
.toolbar input{flex:1;min-width:220px;background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:10px;padding:10px 12px;font:inherit;font-size:13px}
.toolbar input:focus{outline:2px solid var(--accent);outline-offset:1px}
button{font:inherit}
#theme{background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:10px;padding:9px 12px;font-size:12px;cursor:pointer}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-top:12px}
.card{position:relative;background:var(--mask);border:1px solid var(--border);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:8px;transition:transform .2s,border-color .2s,box-shadow .2s}
.card:hover,.card:focus-within{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 10px 30px var(--glow)}
.card h3{font-size:14px;margin:0;overflow-wrap:anywhere}
.card p{font-size:12px;color:var(--muted);margin:0;line-height:1.6}
.card .path{font-size:11px;opacity:.8;overflow-wrap:anywhere}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto}
.chip{font-size:10.5px;color:var(--muted);border:1px solid var(--border);border-radius:999px;padding:2px 8px}
.glyph{width:80px;height:64px;fill:none;stroke:var(--accent);stroke-width:2;stroke-linecap:round}
.thumb{display:block;width:100%;height:auto;aspect-ratio:32/15;border:1px solid var(--border);border-radius:10px;background:radial-gradient(circle at 50% 40%,var(--glow),transparent 70%),var(--canvas);margin:0 0 10px}
.card.featured{grid-column:span 2;border-color:color-mix(in srgb,var(--accent) 45%,var(--border))}
.card.featured:hover .thumb circle{animation:pulse 1.6s ease-in-out infinite}
@keyframes pulse{50%{opacity:.55}}
@media (max-width:720px){.card.featured{grid-column:auto}}
@media (prefers-reduced-motion:reduce){.card.featured:hover .thumb circle{animation:none}}
.glyph .flow{stroke:var(--accent2);stroke-dasharray:4 4}
.map-card:hover .glyph .flow{animation:flow .8s linear infinite}
@keyframes flow{to{stroke-dashoffset:-16}}
.stretch{color:var(--ink);border:1px solid var(--border);border-radius:10px;padding:8px 10px;font-size:12px;text-decoration:none;text-align:center}
.stretch::after{content:"";position:absolute;inset:0;border-radius:14px}
.stretch:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.actions{display:flex;gap:8px;align-items:center}
.doc-open.primary{flex:1;background:var(--accent);color:var(--canvas);border:0;border-radius:10px;padding:8px 10px;font-size:12px;font-weight:700;cursor:pointer}
.doc-open.primary:hover,.doc-open.primary:focus-visible{filter:brightness(1.1);outline:2px solid var(--accent);outline-offset:2px}
.raw{font-size:11px;color:var(--muted)}
.pages{display:flex;gap:4px;flex-wrap:wrap}
.page{min-width:28px;background:transparent;color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:3px 6px;font-size:11px;cursor:pointer}
.page:hover,.page:focus-visible{border-color:var(--accent);outline:none}
.doc-group{margin-top:18px}
.group-title{font-size:14px;margin:0 0 2px}
.video-frame{margin:10px 0 0}
video.overview{width:100%;max-height:560px;background:#000;border:1px solid var(--border);border-radius:16px;box-shadow:0 20px 60px var(--glow)}
figcaption{margin-top:8px}
.howto p{font-size:12px;color:var(--muted);line-height:1.7;margin:0}
.empty{color:var(--muted);font-size:13px}
footer{padding-top:24px;padding-bottom:40px;color:var(--muted);font-size:11px}
#doc-viewer{position:fixed;top:0;right:0;bottom:0;width:min(860px,100%);z-index:20;background:var(--mask);border-left:1px solid var(--border);box-shadow:-20px 0 60px rgba(0,0,0,.45);transform:translateX(100%);transition:transform .28s ease;display:flex;flex-direction:column}
#doc-viewer.open{transform:none}
#doc-viewer .bar{display:flex;gap:8px;align-items:center;padding:14px 18px;border-bottom:1px solid var(--border)}
#doc-viewer .bar h2{font-size:14px;margin:0;flex:1;word-break:break-all}
#doc-viewer .bar a,#doc-viewer .bar button{background:transparent;color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:6px 10px;font-size:12px;cursor:pointer;text-decoration:none}
#doc-meta{font-size:11px;color:var(--muted);padding:8px 18px 0}
#doc-body{padding:4px 18px 30px;overflow:auto;flex:1}
.scrim{position:fixed;inset:0;z-index:19;background:rgba(2,6,23,.55);opacity:0;pointer-events:none;transition:opacity .25s}
.scrim.open{opacity:1;pointer-events:auto}
.md-body{font-size:13px;line-height:1.7}
.md-body h1,.md-body h2,.md-body h3{margin:16px 0 8px;line-height:1.3}
.md-body h1{font-size:19px}.md-body h2{font-size:16px;color:var(--accent)}.md-body h3{font-size:14px}
.md-body p{margin:8px 0;color:var(--ink)}
.md-body a{color:var(--accent)}
.md-body code{background:var(--code);border:1px solid var(--border);border-radius:6px;padding:1px 6px;font-size:12px}
.md-body pre{background:var(--code);border:1px solid var(--border);border-radius:10px;padding:12px;overflow:auto}
.md-body pre code{background:none;border:none;padding:0}
.md-body blockquote{border-left:3px solid var(--accent);margin:8px 0;padding:4px 12px;color:var(--muted)}
.md-body ul,.md-body ol{margin:8px 0;padding-left:22px}
.md-body table{border-collapse:collapse;width:100%;font-size:12px;margin:10px 0;display:block;overflow:auto}
.md-body th,.md-body td{border:1px solid var(--border);padding:6px 8px;text-align:left}
.md-body th{color:var(--muted);font-weight:400;position:sticky;top:0;background:var(--mask)}
.md-body tr:hover td{background:var(--mask2)}
.md-body hr{border:none;border-top:1px solid var(--border);margin:14px 0}
.tok-kw{color:var(--kw)}.tok-str{color:var(--str)}.tok-fn{color:var(--fn)}.tok-cm{color:var(--cm);font-style:italic}
.hidden{display:none!important}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}
@media (max-width:640px){.hero h1{font-size:22px}.tile .num{font-size:20px}}
</style>
</head>
<body>
"""

_GALLERY_DRAWER = (
    '<div class="scrim" id="doc-scrim"></div>'
    '<aside id="doc-viewer" role="dialog" aria-modal="true" aria-labelledby="doc-title" aria-hidden="true">'
    '<div class="bar"><h2 id="doc-title">Rendered documentation</h2>'
    '<a id="doc-raw" href="#">Raw</a><button type="button" id="doc-close" title="Close (Esc)">Close</button></div>'
    '<div class="meta" id="doc-meta">Pick any document to render it here with offline markdown2html and colored code.</div>'
    '<div id="doc-body" class="md-body"></div></aside>'
)

_GALLERY_APP_JS = """var filter=document.getElementById("filter");
var countEl=document.getElementById("filter-count");
var cards=Array.prototype.slice.call(document.querySelectorAll(".card"));
function applyFilter(){
var term=filter.value.trim().toLowerCase();var shown=0;
cards.forEach(function(card){var hit=!term||(card.textContent||"").toLowerCase().indexOf(term)>=0;card.classList.toggle("hidden",!hit);if(hit){shown++;}});
document.querySelectorAll(".doc-group").forEach(function(g){g.classList.toggle("hidden",!g.querySelector(".card:not(.hidden)"));});
if(countEl){countEl.textContent=term?shown+" of "+cards.length+" shown":"";}}
filter.addEventListener("input",applyFilter);
document.addEventListener("keydown",function(e){
if(e.key==="/"&&document.activeElement!==filter){e.preventDefault();filter.focus();}
if(e.key==="Escape"){closeDoc();}});
document.getElementById("theme").addEventListener("click",function(){
var root=document.documentElement;root.setAttribute("data-theme",root.getAttribute("data-theme")==="light"?"dark":"light");});
var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if(!reduce){document.querySelectorAll("[data-count]").forEach(function(el){
var target=parseInt(el.getAttribute("data-count"),10)||0;var t0=Date.now();var done=false;
function finish(){done=true;el.textContent=target.toLocaleString();}
function tick(){if(done){return;}var p=Math.min((Date.now()-t0)/900,1);if(p>=1){finish();return;}el.textContent=Math.round(target*(1-Math.pow(1-p,3))).toLocaleString();requestAnimationFrame(tick);}
el.textContent="0";requestAnimationFrame(tick);setTimeout(finish,1000);});}
var drawer=document.getElementById("doc-viewer");var scrim=document.getElementById("doc-scrim");
var viewer=document.getElementById("doc-body");var title=document.getElementById("doc-title");
var meta=document.getElementById("doc-meta");var raw=document.getElementById("doc-raw");
var known={};document.querySelectorAll(".doc-open").forEach(function(b){known[b.getAttribute("data-name")]=b.getAttribute("data-href");});
var lastFocus=null;
function closeDoc(){if(!drawer.classList.contains("open")){return;}drawer.classList.remove("open");scrim.classList.remove("open");drawer.setAttribute("aria-hidden","true");
if(location.hash.indexOf("#doc=")===0){history.replaceState(null,"",location.pathname+location.search);}if(lastFocus){lastFocus.focus();}}
function resolveDoc(base,rel){var parts=base.split("/");parts.pop();rel.split("/").forEach(function(seg){if(seg==="..") {parts.pop();}else if(seg!=="."&&seg!==""){parts.push(seg);}});return parts.join("/");}
function openDoc(name){var href=known[name];if(!href){return;}
lastFocus=document.activeElement;title.textContent=name;raw.setAttribute("href",href);meta.textContent="Loading "+name+"...";
drawer.classList.add("open");scrim.classList.add("open");drawer.setAttribute("aria-hidden","false");document.getElementById("doc-close").focus();
fetch(href).then(function(r){if(!r.ok){throw new Error("HTTP "+r.status);}return r.text();}).then(function(md){
meta.textContent=name+" | "+md.split("\\n").length+" lines | rendered offline";
viewer.innerHTML=md2html(md);viewer.scrollTop=0;history.replaceState(null,"","#doc="+encodeURIComponent(name));
viewer.querySelectorAll("a[href]").forEach(function(a){var h=a.getAttribute("href");if(!h||/^[a-z]+:/i.test(h)||h.charAt(0)==="#"){return;}
var target=resolveDoc(name,h.split("#")[0]);if(known[target]){a.addEventListener("click",function(ev){ev.preventDefault();openDoc(target);});}});
}).catch(function(e){meta.textContent="Could not load "+name+": "+e+" (serve the folder over http to read docs inline)";});}
document.querySelectorAll(".doc-open").forEach(function(btn){btn.addEventListener("click",function(){openDoc(btn.getAttribute("data-name"));});});
document.getElementById("doc-close").addEventListener("click",closeDoc);scrim.addEventListener("click",closeDoc);
if(location.hash.indexOf("#doc=")===0){openDoc(decodeURIComponent(location.hash.slice(5)));}
"""

_GALLERY_MD_JS = """function escapeHtml(text){return String(text).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function highlightCode(code,lang){
var esc=escapeHtml(code);
esc=esc.replace(/(&quot;.*?&quot;|&#x27;.*?&#x27;|"[^"\\n]*"|'[^'\\n]*')/g,'<span class="tok-str">$1</span>');
esc=esc.replace(/(^|\\s)(def|class|return|import|from|if|else|elif|for|while|try|except|with|as|pass|raise|None|True|False|function|const|let|var|new|typeof|struct|impl|fn|pub|mut|match|enum|interface|type)\\b/g,'$1<span class="tok-kw">$2</span>');
return esc;}
function md2html(src){
var lines=String(src).split("\\n");var out=[];var inCode=false;var codeLang="";var buf=[];var listTag="";
function closeList(){if(listTag){out.push("</"+listTag+">");listTag="";}}
function flushCode(){out.push('<pre><code class="lang-'+escapeHtml(codeLang)+'">'+highlightCode(buf.join("\\n"),codeLang)+'</code></pre>');buf=[];}
for(var i=0;i<lines.length;i++){var line=lines[i];
if(line.indexOf("```")===0){if(!inCode){inCode=true;codeLang=line.slice(3).trim();buf=[];}else{inCode=false;flushCode();}continue;}
if(inCode){buf.push(line);continue;}
if(line.indexOf("# ")===0){closeList();out.push("<h1>"+inline(line.slice(2))+"</h1>");continue;}
if(line.indexOf("## ")===0){closeList();out.push("<h2>"+inline(line.slice(3))+"</h2>");continue;}
if(line.indexOf("### ")===0){closeList();out.push("<h3>"+inline(line.slice(4))+"</h3>");continue;}
if(line.trim()==="---"||line.trim()==="***"){closeList();out.push("<hr>");continue;}
if(line.indexOf("> ")===0){closeList();out.push("<blockquote>"+inline(line.slice(2))+"</blockquote>");continue;}
if(line.indexOf("|")>=0&&lines[i+1]&&/^\\s*\\|?[\\s:\\-|]+\\|?\\s*$/.test(lines[i+1])){closeList();var head=line.split("|").map(function(c){return c.trim();}).filter(function(c){return c;});i++;var rows=[];while(i+1<lines.length&&lines[i+1].indexOf("|")>=0){i++;rows.push(lines[i].split("|").map(function(c){return c.trim();}).filter(function(c){return c;}));}var h="<table><thead><tr>"+head.map(function(c){return "<th>"+inline(c)+"</th>";}).join("")+"</tr></thead>";if(rows.length){h+="<tbody>"+rows.map(function(r){return "<tr>"+r.map(function(c){return "<td>"+inline(c)+"</td>";}).join("")+"</tr>";}).join("")+"</tbody>";}out.push(h+"</table>");continue;}
if(/^(\\s*[-*]\\s+)/.test(line)){if(listTag!=="ul"){closeList();listTag="ul";out.push("<ul>");}out.push("<li>"+inline(line.replace(/^\\s*[-*]\\s+/,""))+"</li>");continue;}
if(/^(\\s*\\d+\\.\\s+)/.test(line)){if(listTag!=="ol"){closeList();listTag="ol";out.push("<ol>");}out.push("<li>"+inline(line.replace(/^\\s*\\d+\\.\\s+/,""))+"</li>");continue;}
if(!line.trim()){closeList();continue;}
closeList();out.push("<p>"+inline(line)+"</p>");}
closeList();if(inCode){flushCode();}
return out.join("\\n");}
function inline(s){var esc=escapeHtml(s);esc=esc.replace(/`([^`]+)`/g,"<code>$1</code>");esc=esc.replace(/\\*\\*([^*]+)\\*\\*/g,"<strong>$1</strong>");esc=esc.replace(/\\*([^*]+)\\*/g,"<em>$1</em>");esc=esc.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g,'<a href="$2">$1</a>');return esc;}
"""


class DocsSitePublisher:
    """Publishes validated system maps as a static documentation site.

    Writes one standalone map document per diagram kind plus a gallery
    index page, ready to serve as project documentation or a static
    hosting root. All output is self-contained with zero external
    requests and relative links only.
    """

    _KIND_DESCRIPTIONS: Tuple[Tuple[str, str], ...] = (
        ("architecture", "Components, services, storage, and boundaries across layers."),
        ("workflow", "Delivery path across lanes from entry to terminal outcomes."),
        ("sequence", "Ordered interaction between top participants over time."),
        ("dataflow", "Movement of data from sources through transforms to stores."),
        ("lifecycle", "States, transitions, waits, and retry paths of change."),
    )

    def __init__(self, config: Config) -> None:
        """Initialise the publisher with application configuration.

        Args:
            config: Central settings for pages layout and map limits.
        """
        self._config = config
        self._validator = SystemMapValidator(config)
        self._renderer = InteractiveMapRenderer(config)

    def description_for(self, kind: str) -> str:
        """Return the gallery description for a diagram kind.

        Args:
            kind: Diagram kind identifier.

        Returns:
            Human-readable gallery description.
        """
        for candidate, description in self._KIND_DESCRIPTIONS:
            if candidate == kind:
                return description
        return "Authored system topology."

    def publish(
        self,
        maps: Dict[str, SystemMap],
        project_name: str,
        output_dir: str,
        stats: Optional[Dict[str, int]] = None,
        renderer: Optional[object] = None,
        project_root: Optional[str] = None,
        video_rel: Optional[str] = None,
        doc_entries: Optional[List[Dict[str, str]]] = None,
        extra_cards: Optional[List[Dict[str, str]]] = None,
    ) -> Dict[str, str]:
        """Publish maps and a gallery index into a documentation directory.

        Args:
            maps: Mapping of diagram kind to system map.
            project_name: Display name used for index titles.
            output_dir: Destination directory for the static site.
            stats: Optional project counters shown in the gallery header.
            renderer: Map renderer with a write method, defaults to offline.
            project_root: Optional project root used to collect video and docs.
            video_rel: Optional precomputed video href relative to the index.
            doc_entries: Optional precomputed doc entries with name and href.
            extra_cards: Optional extra gallery cards (kind, title, href,
                description, meta) appended after the map cards.

        Returns:
            Mapping of published page identifier to written file path.
        """
        active = renderer if renderer is not None else self._renderer
        root = Path(output_dir)
        subdir = self._config.DIAGRAM_MAPS_SUBDIR.strip().strip("/")
        depth = 0 if subdir in ("", ".") else len(Path(subdir).parts)
        maps_dir = root if depth == 0 else root / subdir
        maps_dir.mkdir(parents=True, exist_ok=True)
        home_target = "index.html" if depth == 0 else "../" * depth + "index.html"
        href_prefix = self._href_prefix()
        written: Dict[str, str] = {}
        published: Dict[str, SystemMap] = {}
        for kind in sorted(maps):
            system_map = maps[kind]
            receipt = self._validator.validate(system_map)
            if not receipt.passed:
                continue
            localized = SystemMap(
                kind=system_map.kind,
                title=system_map.title,
                nodes=system_map.nodes,
                edges=system_map.edges,
                views=system_map.views,
                meta={**system_map.meta, "home": home_target},
            )
            target = maps_dir / (kind + ".html")
            active.write(localized, str(target))
            published[kind] = system_map
            written[kind] = str(target)
        resolved_video = video_rel
        resolved_poster: Optional[str] = None
        resolved_docs = list(doc_entries) if doc_entries is not None else None
        if resolved_video is None and resolved_docs is None and project_root is not None:
            try:
                collected = self.publish_assets(project_root, str(root))
                resolved_video = collected.get("video_rel")
                resolved_poster = collected.get("poster_rel")
                resolved_docs = collected.get("doc_entries", [])
                for key, path in collected.get("written", {}).items():
                    written[key] = path
            except OSError:
                resolved_video = None
                resolved_docs = []
        index_target = root / "index.html"
        index_target.write_text(
            self.render_index(
                project_name, published, stats or {}, href_prefix,
                resolved_video, resolved_docs, resolved_poster,
                extra_cards=extra_cards,
            ),
            encoding="utf-8",
        )
        written["index"] = str(index_target)
        if self._config.SITE_LLMS_TXT_ENABLED:
            llms_target = root / self._config.SITE_LLMS_TXT_FILENAME
            llms_target.write_text(
                self.render_llms_txt(
                    project_name, published, stats or {}, href_prefix, resolved_docs,
                ),
                encoding="utf-8",
            )
            written["llms"] = str(llms_target)
        nojekyll_target = root / ".nojekyll"
        nojekyll_target.write_text("", encoding="utf-8")
        written["nojekyll"] = str(nojekyll_target)
        return written

    def collect_doc_sources(self, project_root: str) -> List[Path]:
        """Collect generated markdown sources for the static site.

        Args:
            project_root: Project root directory to scan for docs.

        Returns:
            Sorted list of markdown file paths capped by configuration.
        """
        base = Path(project_root).resolve()
        candidates: List[Path] = []
        for name in ("KNOWLEDGE_BASE.md", "README.md", "SECURITY.md", "SKILL.md"):
            candidate = base / name
            if candidate.is_file():
                candidates.append(candidate)
        for dirname in (self._config.AGENT_OUTPUT_DIR, self._config.WIKI_OUTPUT_DIR, self._config.GRAPHRAG_OUTPUT_DIR):
            docs_dir = base / dirname
            if not docs_dir.is_dir():
                continue
            for path in sorted(docs_dir.rglob("*.md")):
                if path.is_file() and path not in candidates:
                    candidates.append(path)
        limit = max(1, self._config.SITE_MAX_DOCS)
        ordered = sorted(candidates, key=lambda p: p.relative_to(base).as_posix())
        return ordered[:limit]

    def publish_assets(
        self, project_root: str, output_dir: str
    ) -> Dict[str, object]:
        """Copy overview video and markdown docs into the static site.

        Args:
            project_root: Project root holding generated artifacts.
            output_dir: Static site root receiving copied assets.

        Returns:
            Mapping with video_rel, doc_entries, and written paths.
        """
        base = Path(project_root).resolve()
        root = Path(output_dir)
        root.mkdir(parents=True, exist_ok=True)
        written: Dict[str, str] = {}
        video_rel: Optional[str] = None
        poster_rel: Optional[str] = None
        if self._config.SITE_VIDEO_ENABLED:
            source = base / self._config.VIDEO_OUTPUT
            if source.is_file():
                target = root / self._config.SITE_VIDEO_FILENAME
                if source.resolve() != target.resolve():
                    shutil.copy2(source, target)
                    written["video"] = str(target)
                else:
                    written["video"] = str(target)
                video_rel = target.name
                poster = self._render_poster(target, root)
                if poster is not None:
                    written["poster"] = str(poster)
                    poster_rel = poster.name
        doc_entries: List[Dict[str, str]] = []
        if self._config.SITE_DOCS_ENABLED:
            docs_root = root / self._config.SITE_DOCS_SUBDIR.strip().strip("/")
            docs_root.mkdir(parents=True, exist_ok=True)
            sources = self.collect_doc_sources(str(base))
            self._prune_stale_docs(
                docs_root, {s.relative_to(base).as_posix() for s in sources},
            )
            for source in sources:
                rel = source.relative_to(base).as_posix()
                target = docs_root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
                href = (
                    self._config.SITE_DOCS_SUBDIR.strip().strip("/") + "/" + rel
                )
                preview = ""
                lines = 0
                chars = 0
                try:
                    text = source.read_text(encoding="utf-8", errors="replace")
                    preview = self._doc_preview(text)
                    lines = len(text.splitlines())
                    chars = len(text)
                except OSError:
                    preview = ""
                doc_entries.append({
                    "name": rel, "href": href, "preview": preview,
                    "title": self._doc_title(text) if chars else "",
                    "lines": str(lines), "chars": str(chars),
                })
                written["doc:" + rel] = str(target)
        return {
            "video_rel": video_rel, "poster_rel": poster_rel,
            "doc_entries": doc_entries, "written": written,
        }

    def _render_poster(self, video: Path, site_root: Path) -> Optional[Path]:
        """Extract one video frame as the player poster so it never shows black.

        Re-renders only when the video is newer than the poster. Skips
        silently when ffmpeg is missing or fails.

        Args:
            video: Published video file.
            site_root: Site root receiving the poster image.

        Returns:
            Poster path, or None when no poster is available.
        """
        poster = site_root / self._config.SITE_VIDEO_POSTER_FILENAME
        try:
            if poster.is_file() and poster.stat().st_mtime >= video.stat().st_mtime:
                return poster
        except OSError:
            return None
        ffmpeg = shutil.which("ffmpeg")
        if ffmpeg is None:
            return poster if poster.is_file() else None
        command = [
            ffmpeg, "-y", "-loglevel", "error",
            "-ss", str(self._config.SITE_VIDEO_POSTER_AT_S),
            "-i", str(video), "-frames:v", "1",
            "-q:v", str(self._config.SITE_VIDEO_POSTER_QUALITY), str(poster),
        ]
        try:
            subprocess.run(
                command, check=True, capture_output=True,
                timeout=self._config.SITE_VIDEO_POSTER_TIMEOUT_S,
            )
        except (OSError, subprocess.SubprocessError):
            return poster if poster.is_file() else None
        return poster if poster.is_file() else None

    @staticmethod
    def _doc_title(text: str) -> str:
        """Return the first H1 heading of a markdown document without page suffixes."""
        for raw in text.splitlines()[:40]:
            line = raw.strip()
            if line.startswith("# "):
                title = line[2:].replace("**", "").replace("`", "").strip()
                return title.split(" (page ")[0].strip()
        return ""

    def _doc_preview(self, text: str) -> str:
        """Return the first prose sentence of a markdown document for its card.

        Headings, tables, navigation lines, front matter, and code fences
        are skipped and inline markdown is stripped, so cards show what a
        document says instead of its raw syntax.

        Args:
            text: Markdown source.

        Returns:
            Plain-text preview capped at SITE_MD_PREVIEW_CHARS.
        """
        skip_prefixes = ("#", "|", ">", "```", "---", "Pages:", "Previous:", "Next:", "<", "*Last")
        in_fence = False
        for raw in text.splitlines():
            line = raw.strip()
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or not line or line.startswith(skip_prefixes):
                continue
            if ":" in line.split(" ", 1)[0] and line.endswith(("\"", "'")):
                continue
            plain = _MD_LINK_RE.sub(r"\1", line)
            plain = _MD_MARK_RE.sub("", plain).lstrip("-*0123456789. ").strip()
            if len(plain) < self._config.SITE_MD_PREVIEW_MIN_CHARS:
                continue
            limit = self._config.SITE_MD_PREVIEW_CHARS
            if len(plain) <= limit:
                return plain
            cut = plain[:limit].rsplit(" ", 1)[0]
            return cut.rstrip(",;:-") + "..."
        return ""

    @staticmethod
    def _prune_stale_docs(docs_root: Path, keep: Set[str]) -> None:
        """Delete copied markdown docs that no longer exist in the project.

        The docs subdirectory is owned by the publisher; without pruning,
        renamed wiki or paged agent files would linger in the site forever.

        Args:
            docs_root: Site directory holding copied markdown.
            keep: Relative paths published in this run.
        """
        if docs_root.is_symlink() or not docs_root.is_dir():
            return
        for path in sorted(docs_root.rglob("*.md")):
            rel = path.relative_to(docs_root).as_posix()
            if rel not in keep and path.is_file() and not path.is_symlink():
                path.unlink()

    def render_llms_txt(
        self,
        project_name: str,
        maps: Dict[str, SystemMap],
        stats: Dict[str, int],
        href_prefix: str,
        doc_entries: Optional[List[Dict[str, str]]] = None,
    ) -> str:
        """Render an llms.txt entry point so agents can navigate the site as text.

        Follows the llms.txt convention: an H1 title, a blockquote summary,
        then H2 sections of markdown links. Agent-oriented markdown comes
        first because it is cheaper to read than the HTML maps.

        Args:
            project_name: Display name used for the title.
            maps: Mapping of published diagram kind to system map.
            stats: Project counters summarized in the blockquote.
            href_prefix: Relative prefix pointing at the map directory.
            doc_entries: Published markdown docs with name and href.

        Returns:
            Plain markdown text for llms.txt.
        """
        name = " ".join(project_name.split()) or "project"
        counters = ", ".join(
            f"{value} {key}" for key, value in sorted(stats.items())
        )
        summary = f"Static analysis knowledge base for {name}"
        lines = [f"# {name}", "", f"> {summary}{': ' + counters if counters else ''}.", ""]
        lines.append(
            "Generated offline by readmenator (zero LLM tokens). Start with the "
            "wiki index for the big picture, then the agent INDEX for file lookup."
        )
        lines.append("")
        agent_dir = self._config.AGENT_OUTPUT_DIR + "/"
        wiki_dir = self._config.WIKI_OUTPUT_DIR + "/"
        graphrag_dir = self._config.GRAPHRAG_OUTPUT_DIR + "/"
        groups: Dict[str, List[Dict[str, str]]] = {"wiki": [], "graphrag": [], "agent": [], "other": []}
        for entry in doc_entries or []:
            rel = entry.get("name", "")
            if rel.startswith(wiki_dir):
                groups["wiki"].append(entry)
            elif rel.startswith(graphrag_dir):
                groups["graphrag"].append(entry)
            elif rel.startswith(agent_dir):
                groups["agent"].append(entry)
            else:
                groups["other"].append(entry)
        priority = ("index.md", "INDEX.md", "MANIFEST.json", "GOTCHAS.md")

        def order(entry: Dict[str, str]) -> Tuple[int, str]:
            """Sort entry points first, then alphabetically."""
            base = entry.get("name", "").rsplit("/", 1)[-1]
            rank = priority.index(base) if base in priority else len(priority)
            return rank, entry.get("name", "")

        titles = (("wiki", "Wiki"), ("graphrag", "GraphRAG"), ("agent", "Agent Docs"), ("other", "Project Docs"))
        for key, title in titles:
            if not groups[key]:
                continue
            lines.append(f"## {title}")
            lines.append("")
            for entry in sorted(groups[key], key=order):
                preview = " ".join(entry.get("preview", "").split())
                note = f": {preview}" if preview else ""
                lines.append(f"- [{entry.get('name', '')}]({entry.get('href', '')}){note}")
            lines.append("")
        if maps:
            lines.append("## Optional")
            lines.append("")
            for kind in sorted(maps):
                lines.append(
                    f"- [{maps[kind].title}]({href_prefix}{kind}.html): "
                    f"{self.description_for(kind)} (interactive HTML)"
                )
            lines.append("")
        return "\n".join(lines)

    def render_index(
        self,
        project_name: str,
        maps: Dict[str, SystemMap],
        stats: Dict[str, int],
        href_prefix: Optional[str] = None,
        video_rel: Optional[str] = None,
        doc_entries: Optional[List[Dict[str, str]]] = None,
        poster_rel: Optional[str] = None,
        extra_cards: Optional[List[Dict[str, str]]] = None,
    ) -> str:
        """Render the gallery index page for published maps.

        Args:
            project_name: Display name used for index titles.
            maps: Mapping of published diagram kind to system map.
            stats: Project counters shown in the gallery header.
            href_prefix: Relative prefix pointing at the map directory.
            video_rel: Optional video href relative to the index.
            doc_entries: Optional doc entries with name, href, preview, lines, chars.
            poster_rel: Optional poster image href for the video player.
            extra_cards: Optional extra gallery cards appended after maps.

        Returns:
            Complete standalone HTML gallery document.
        """
        if href_prefix is None:
            href_prefix = self._href_prefix()
        title = self._escape(project_name.strip() or "Project")
        entries = list(doc_entries or [])
        cards = [self._extra_card(extra) for extra in extra_cards or []]
        cards.extend(self._card(kind, maps[kind], href_prefix) for kind in sorted(maps))
        gallery = "\n".join(cards) if cards else (
            '<p class="empty">No validated maps were published yet.</p>'
        )
        return (
            _GALLERY_HEAD.replace("__TITLE__", title)
            + '<div class="backdrop" aria-hidden="true"></div>'
            + '<header class="hero"><p class="eyebrow">Zero-token knowledge base</p>'
            + "<h1>" + title + " <span>| System Maps</span></h1>"
            + "<p class=\"lede\">Architecture maps, an overview video, and the full documentation "
            + "set, generated offline from the source code. Nothing here was written by an LLM.</p>"
            + self._stat_tiles(stats)
            + "</header>"
            + self._start_here(entries, video_rel)
            + '<div class="toolbar"><input id="filter" type="search" '
            + 'placeholder="Filter maps and docs ( / )" aria-label="Filter diagrams and docs">'
            + '<span id="filter-count" class="muted" aria-live="polite"></span>'
            + '<button type="button" id="theme" title="Toggle dark and light theme">Theme</button></div>'
            + '<section class="section" id="maps"><h2>Interactive maps</h2>'
            + '<p class="muted">Physics-driven diagrams: drag nodes, click one for its documentation, '
            + "trace upstream or downstream reach. Maps load their engine from a CDN.</p>"
            + '<div class="grid" id="gallery">' + gallery + "</div></section>"
            + self._video_section(video_rel, poster_rel)
            + self._docs_section(entries)
            + '<section class="howto section"><h2>How to read these maps</h2>'
            + "<p>Open any map, then: drag nodes freely while physics settles the rest, search (/) to filter, "
            + "click a node to focus it with full file documentation, Upstream and Downstream to trace authored "
            + "reach, Path to probe the exact route between two ids, Lens to compare semantic roles, Play to walk "
            + "the guided chapters, Stabilize to re-run physics, Theme for dark and light, Export for PNG or typed "
            + "JSON. Deep links such as #route=a~b restore any reading.</p></section>"
            + "<footer>Generated offline from scanned source topology. Counts reflect authored relationships only. "
            + "Agents: read <a href=\"" + self._escape(self._config.SITE_LLMS_TXT_FILENAME) + "\">"
            + self._escape(self._config.SITE_LLMS_TXT_FILENAME) + "</a>.</footer>"
            + _GALLERY_DRAWER
            + "<script>\n(function(){\n\"use strict\";\n"
            + _GALLERY_MD_JS
            + _GALLERY_APP_JS
            + "})();\n</script>\n</body>\n</html>"
        )

    def _stat_tiles(self, stats: Dict[str, int]) -> str:
        """Render animated counter tiles for the headline project metrics.

        Args:
            stats: Project counters.

        Returns:
            HTML fragment, empty when no stats are known.
        """
        if not stats:
            return ""
        tiles = []
        for key in sorted(stats):
            value = int(stats[key])
            tiles.append(
                '<div class="tile"><span class="num" data-count="' + str(value) + '">'
                + "{:,}".format(value) + '</span><span class="label">' + self._escape(str(key)) + "</span></div>"
            )
        return '<div class="tiles">' + "".join(tiles) + "</div>"

    def _start_here(self, entries: List[Dict[str, str]], video_rel: Optional[str]) -> str:
        """Render the three-step reading path shown above the maps.

        Args:
            entries: Published doc entries.
            video_rel: Video href, when a video was published.

        Returns:
            HTML fragment linking the wiki overview, knowledge base, and video.
        """
        by_name = {e.get("name", ""): e for e in entries}
        steps: List[Tuple[str, str, str, str]] = []
        wiki = by_name.get(self._config.WIKI_OUTPUT_DIR + "/index.md")
        if wiki:
            steps.append(("doc", wiki.get("name", ""), "Big picture", "Wiki overview: communities, god nodes, reading order"))
        if video_rel:
            steps.append(("link", "#video", "Watch", "Overview video of the whole codebase"))
        kb = by_name.get(self._config.OUTPUT_FILENAME)
        if kb:
            steps.append(("doc", kb.get("name", ""), "Deep dive", "Knowledge base: every file, symbol, and finding"))
        agent = by_name.get(self._config.AGENT_OUTPUT_DIR + "/INDEX.md")
        if agent:
            steps.append(("doc", agent.get("name", ""), "Look up", "Agent index: file, purpose, who depends on it"))
        if not steps:
            return ""
        items = []
        for index, (mode, target, label, text) in enumerate(steps, start=1):
            inner = (
                '<span class="step">' + str(index) + '</span><span><strong>' + self._escape(label)
                + "</strong><br><span class=\"muted\">" + self._escape(text) + "</span></span>"
            )
            if mode == "doc":
                items.append(
                    '<button type="button" class="start doc-open" data-name="' + self._escape(target)
                    + '" data-href="' + self._escape(by_name[target].get("href", "")) + '">' + inner + "</button>"
                )
            else:
                items.append('<a class="start" href="' + self._escape(target) + '">' + inner + "</a>")
        return '<nav class="start-here section" aria-label="Start here"><h2>Start here</h2><div class="starts">' + "".join(items) + "</div></nav>"

    def _video_section(self, video_rel: Optional[str], poster_rel: Optional[str] = None) -> str:
        """Render the overview video section with an HTML5 video tag.

        Args:
            video_rel: Video href relative to the index, None hides the section.
            poster_rel: Optional poster image shown before playback.

        Returns:
            HTML section fragment, empty string when no video is available.
        """
        if not video_rel:
            return ""
        src = self._escape(video_rel)
        poster = ' poster="' + self._escape(poster_rel) + '"' if poster_rel else ""
        return (
            '<section class="section" id="video">'
            "<h2>Overview video</h2>"
            '<figure class="video-frame"><video class="overview" controls preload="metadata"'
            + poster + ' src="' + src
            + '">Your browser does not support the video tag. '
            + '<a href="' + src + '">Download the overview video</a>.</video>'
            + '<figcaption class="muted">Cinematic synthwave overview rendered from real scan data: layers, '
            + "god nodes, dependency tree, communities, import graph, and code DNA. "
            + '<a href="' + src + '">Open/download ' + src + "</a>.</figcaption></figure>"
            + "</section>"
        )

    def _doc_group(self, name: str) -> str:
        """Return the gallery group a published document belongs to."""
        if name.startswith(self._config.WIKI_OUTPUT_DIR + "/"):
            return "wiki"
        if name.startswith(self._config.GRAPHRAG_OUTPUT_DIR + "/"):
            return "graphrag"
        if name.startswith(self._config.AGENT_OUTPUT_DIR + "/recipes/"):
            return "recipes"
        if name.startswith(self._config.AGENT_OUTPUT_DIR + "/"):
            return "agent"
        return "project"

    def _docs_section(self, doc_entries: List[Dict[str, str]]) -> str:
        """Render grouped documentation cards with an offline markdown drawer.

        Paged documents (``NAME_p2.md``) collapse into their first page's
        card as page chips, and every card shows a prose preview plus its
        size, so readers pick the right document before opening it.

        Args:
            doc_entries: Doc entries with name, href, preview, lines, chars.

        Returns:
            HTML section fragment, empty string when no docs are available.
        """
        if not doc_entries:
            return ""
        chars_per_token = max(1, self._config.AGENT_CHARS_PER_TOKEN)
        pages: Dict[str, List[Tuple[int, Dict[str, str]]]] = {}
        for entry in sorted(doc_entries, key=lambda d: str(d.get("name", ""))):
            name = str(entry.get("name", ""))
            match = _PAGE_PART_RE.match(name)
            base = match.group("base") + ".md" if match else name
            page = int(match.group("page")) if match else 1
            pages.setdefault(base, []).append((page, entry))
        groups: Dict[str, List[str]] = {"wiki": [], "graphrag": [], "project": [], "agent": [], "recipes": []}
        lead = ("index.md", "INDEX.md", self._config.OUTPUT_FILENAME, "README.md")

        def doc_order(base: str) -> Tuple[int, str]:
            """Entry points first, then alphabetical."""
            leaf = base.rsplit("/", 1)[-1]
            return (lead.index(leaf) if leaf in lead else len(lead), base.lower())

        for base in sorted(pages, key=doc_order):
            parts = sorted(pages[base], key=lambda item: item[0])
            first = parts[0][1]
            name = str(first.get("name", ""))
            total_lines = sum(int(str(p.get("lines", "0")) or 0) for _, p in parts)
            total_chars = sum(int(str(p.get("chars", "0")) or 0) for _, p in parts)
            badges = '<span class="chip">' + str(total_lines) + " lines</span>"
            if total_chars:
                badges += '<span class="chip">~' + str(max(1, total_chars // chars_per_token)) + " tokens</span>"
            chips = ""
            if len(parts) > 1:
                chips = '<div class="pages">' + "".join(
                    '<button type="button" class="page doc-open" data-href="' + self._escape(str(p.get("href", "")))
                    + '" data-name="' + self._escape(str(p.get("name", ""))) + '" title="Page ' + str(num) + '">'
                    + str(num) + "</button>"
                    for num, p in parts
                ) + "</div>"
            preview = str(first.get("preview", ""))
            groups[self._doc_group(name)].append(
                '<article class="card doc-card" data-doc="' + self._escape(name) + '">'
                + "<h3>" + self._escape(str(first.get("title", "")) or base.split("/")[-1]) + "</h3>"
                + '<p class="path">' + self._escape(base) + "</p>"
                + ("<p>" + self._escape(preview) + "</p>" if preview else "")
                + '<div class="chips">' + badges + "</div>" + chips
                + '<div class="actions"><button type="button" class="doc-open primary" data-href="'
                + self._escape(str(first.get("href", ""))) + '" data-name="' + self._escape(name)
                + '">Read rendered</button><a class="raw" href="' + self._escape(str(first.get("href", "")))
                + '">Open raw markdown</a></div></article>'
            )
        titles = (
            ("wiki", "Wiki", "Concept pages per code community: start with index.md."),
            ("graphrag", "GraphRAG", "Community report hierarchy for agents. Query it with: readmenator . ask \"question\" (or MCP readmenator.graphrag)."),
            ("project", "Project docs", "Knowledge base, README, and policies."),
            ("agent", "Agent docs", "Grep-friendly indexes for AI agents (also useful for humans)."),
            ("recipes", "Recipes", "Step-by-step tasks grounded in this codebase."),
        )
        total = sum(len(v) for v in groups.values())
        blocks = []
        for key, heading, blurb in titles:
            if not groups[key]:
                continue
            blocks.append(
                '<div class="doc-group" data-group="' + key + '"><h3 class="group-title">' + heading
                + ' <span class="muted">' + str(len(groups[key])) + '</span></h3><p class="muted">' + blurb
                + '</p><div class="grid">' + "\n".join(groups[key]) + "</div></div>"
            )
        return (
            '<section class="section" id="docs"><h2>Documentation ' + str(total) + " files</h2>"
            + "".join(blocks) + "</section>"
        )

    def _href_prefix(self) -> str:
        """Return the relative href prefix for map links.

        Returns:
            Map subdirectory with trailing slash, or empty string.
        """
        subdir = self._config.DIAGRAM_MAPS_SUBDIR.strip().strip("/")
        if subdir in ("", "."):
            return ""
        return subdir + "/"

    _KIND_GLYPHS: Tuple[Tuple[str, str], ...] = (
        ("architecture",
         '<rect x="8" y="6" width="64" height="12" rx="3"/><rect x="8" y="26" width="28" height="12" rx="3"/>'
         '<rect x="44" y="26" width="28" height="12" rx="3"/><rect x="8" y="46" width="64" height="12" rx="3"/>'
         '<path class="flow" d="M22 18v8M58 18v8M22 38v8M58 38v8"/>'),
        ("workflow",
         '<circle cx="10" cy="32" r="6"/><circle cx="31" cy="32" r="6"/><circle cx="52" cy="32" r="6"/>'
         '<rect x="64" y="26" width="12" height="12" rx="2"/><path class="flow" d="M16 32h9M37 32h9M58 32h6"/>'),
        ("sequence",
         '<path d="M14 6v52M40 6v52M66 6v52"/><path class="flow" d="M14 16h26M40 28h26M66 40H40M40 52H14"/>'),
        ("dataflow",
         '<circle cx="10" cy="20" r="6"/><circle cx="10" cy="44" r="6"/><rect x="30" y="24" width="18" height="16" rx="3"/>'
         '<ellipse cx="68" cy="22" rx="8" ry="3"/><path d="M60 22v20c0 2 16 2 16 0V22"/>'
         '<path class="flow" d="M16 20l14 8M16 44l14-8M48 32h12"/>'),
        ("lifecycle",
         '<circle cx="40" cy="10" r="6"/><circle cx="68" cy="32" r="6"/><circle cx="40" cy="54" r="6"/><circle cx="12" cy="32" r="6"/>'
         '<path class="flow" d="M46 12l17 15M64 38L46 52M34 52L17 38M16 27l18-15"/>'),
    )

    def _glyph(self, kind: str) -> str:
        """Return a small inline SVG pictogram for a diagram kind.

        Args:
            kind: Diagram kind identifier.

        Returns:
            SVG markup (decorative, hidden from assistive technology).
        """
        body = '<rect x="8" y="8" width="64" height="48" rx="6"/>'
        for candidate, markup in self._KIND_GLYPHS:
            if candidate == kind:
                body = markup
        return (
            '<svg class="glyph" viewBox="0 0 80 64" aria-hidden="true" focusable="false">'
            + body + "</svg>"
        )

    def _card(self, kind: str, system_map: SystemMap, href_prefix: str) -> str:
        """Render one gallery card linking to a published map.

        Args:
            kind: Diagram kind identifier.
            system_map: Published system map.
            href_prefix: Relative prefix pointing at the map directory.

        Returns:
            HTML card fragment with a relative map link covering the card.
        """
        href = self._escape(href_prefix + kind + ".html")
        total = system_map.meta.get("total", str(len(system_map.nodes)))
        scope = "full scope" if str(system_map.meta.get("full", "")).lower() == "true" else "primary scope"
        return (
            '<article class="card map-card" data-kind="'
            + self._escape(kind)
            + '">'
            + self._glyph(kind)
            + "<h3>"
            + self._escape(system_map.title)
            + "</h3><p>"
            + self._escape(self.description_for(kind))
            + '</p><div class="chips"><span class="chip">'
            + str(len(system_map.nodes))
            + " of "
            + self._escape(str(total))
            + " files in "
            + scope
            + '</span><span class="chip">'
            + str(len(system_map.edges))
            + ' links</span><span class="chip">'
            + str(len(system_map.views))
            + ' chapters</span></div><a class="stretch" href="'
            + href
            + '">Open '
            + self._escape(kind)
            + " map</a>"
            + "</article>"
        )

    def _extra_card(self, entry: Dict[str, str]) -> str:
        """Render one gallery card for a non-map page such as the explorer.

        Args:
            entry: Card fields (kind, title, href, description, meta).

        Returns:
            HTML card fragment with the same gallery styling as map cards.
        """
        kind = str(entry.get("kind", "extra"))
        thumb = str(entry.get("thumb", ""))
        visual = thumb if thumb.startswith('<svg class="thumb"') else self._glyph(kind)
        return (
            '<article class="card map-card featured" data-kind="'
            + self._escape(kind)
            + '">'
            + visual
            + "<h3>"
            + self._escape(str(entry.get("title", kind)))
            + "</h3><p>"
            + self._escape(str(entry.get("description", "")))
            + '</p><div class="chips"><span class="chip">'
            + self._escape(str(entry.get("meta", "")))
            + '</span></div><a class="stretch" href="'
            + self._escape(str(entry.get("href", "#")))
            + '">Open '
            + self._escape(str(entry.get("title", kind)))
            + "</a>"
            + "</article>"
        )

    def _stats_line(self, stats: Dict[str, int]) -> str:
        """Render the gallery header statistics line.

        Args:
            stats: Project counters.

        Returns:
            Escaped statistics summary string.
        """
        if not stats:
            return "Interactive maps generated offline from source."
        parts = [str(key) + ": " + str(int(stats[key])) for key in sorted(stats)]
        return self._escape(" | ".join(parts))

    def _escape(self, value: str) -> str:
        """Escape text for HTML embedding.

        Args:
            value: Raw text.

        Returns:
            Escaped text safe for markup contexts.
        """
        return html.escape(value, quote=True)
