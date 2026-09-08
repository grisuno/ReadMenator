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
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple

from readmenator._config import Config
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
        if len(system_map.nodes) > self._config.DIAGRAM_MAX_NODES:
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
        if len(system_map.edges) > self._config.DIAGRAM_MAX_EDGES:
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
            if node.x > self._config.DIAGRAM_CANVAS_WIDTH or node.y > self._config.DIAGRAM_CANVAS_HEIGHT:
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
        ("testing", "external"),
        ("utility", "external"),
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

    def build(
        self,
        nodes: Sequence[Node],
        edges: Sequence[Edge],
        resolved_edges: Optional[Sequence[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[Sequence[SecurityFinding]] = None,
        analysis: Optional[AnalysisResult] = None,
        kind: str = "architecture",
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

        Returns:
            Validated system map intermediate representation.
        """
        normalized = kind if kind in self.supported_kinds() else "architecture"
        if normalized == "architecture":
            return self._build_architecture(nodes, resolved_edges or edges, layers, findings, analysis)
        if normalized == "workflow":
            return self._build_workflow(nodes, resolved_edges or edges, layers, findings)
        if normalized == "sequence":
            return self._build_sequence(nodes, resolved_edges or edges, layers, analysis)
        if normalized == "dataflow":
            return self._build_dataflow(nodes, resolved_edges or edges, layers, findings)
        return self._build_lifecycle(nodes, resolved_edges or edges, layers, findings)

    def build_all(
        self,
        nodes: Sequence[Node],
        edges: Sequence[Edge],
        resolved_edges: Optional[Sequence[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[Sequence[SecurityFinding]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> Dict[str, SystemMap]:
        """Build all five diagram kinds deterministically.

        Args:
            nodes: Scanned file nodes.
            edges: Raw import edges.
            resolved_edges: Project-internal resolved import edges.
            layers: Mapping of file identifier to architectural layer.
            findings: Security findings used for sensitivity marking.
            analysis: Graph analysis used for centrality ranking.

        Returns:
            Mapping of diagram kind to system map.
        """
        result: Dict[str, SystemMap] = {}
        for kind in self.supported_kinds():
            result[kind] = self.build(
                nodes, edges, resolved_edges, layers, findings, analysis, kind
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
    ) -> List[Node]:
        """Select the primary node scope honoring the configured limit.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges used for ranking.
            analysis: Optional analysis with centrality scores.

        Returns:
            Primary nodes in deterministic ranked order.
        """
        ordered_ids = self._ranked_file_ids(nodes, links, analysis)
        by_id = {node.node_id: node for node in nodes}
        limit = max(1, self._config.DIAGRAM_MAX_NODES)
        selected = [by_id[nid] for nid in ordered_ids[:limit] if nid in by_id]
        return selected

    def _internal_links(
        self, edges: Sequence[Edge], selected: Set[str]
    ) -> List[Edge]:
        """Filter edges to project-internal links between selected files.

        Args:
            edges: Candidate edges.
            selected: Selected file identifiers.

        Returns:
            Deterministically ordered internal edges.
        """
        kept = [
            edge
            for edge in edges
            if edge.source in selected and edge.target in selected
        ]
        kept.sort(key=lambda e: (e.source, e.target, e.relation))
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
        self, items: List[Tuple[str, str]], kind: str
    ) -> Dict[str, Tuple[int, int]]:
        """Compute deterministic column lane coordinates for grouped items.

        Args:
            items: Pairs of identifier and group name.
            kind: Diagram kind used only for metadata completeness.

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

    def _layout_sequence(self, ordered: List[str]) -> Dict[str, Tuple[int, int]]:
        """Compute deterministic lifeline row coordinates for sequences.

        Args:
            ordered: Participant identifiers in display order.

        Returns:
            Mapping of identifier to canvas coordinates.
        """
        width = self._config.DIAGRAM_NODE_WIDTH
        col_gap = self._config.DIAGRAM_COLUMN_GAP
        canvas_w = self._config.DIAGRAM_CANVAS_WIDTH
        margin_x = self._config.DIAGRAM_MARGIN_X
        gap = self._fitted_gap(len(ordered), width, col_gap, canvas_w, margin_x)
        total_w = len(ordered) * width + max(0, len(ordered) - 1) * gap
        start_x = margin_x + max(0, (canvas_w - 2 * margin_x - total_w) // 2)
        positions: Dict[str, Tuple[int, int]] = {}
        for index, nid in enumerate(ordered):
            positions[nid] = (start_x + index * (width + gap), self._config.DIAGRAM_SEQUENCE_TOP)
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
        self, ranked: List[Node], layer_of: Dict[str, str], kind: str
    ) -> Tuple[Dict[str, Tuple[int, int]], List[Node]]:
        """Cap lane scope and compute coordinates for placed nodes only.

        Args:
            ranked: Nodes in global rank order.
            layer_of: Mapping of file identifier to lane name.
            kind: Diagram kind used only for metadata completeness.

        Returns:
            Canvas positions and the placed node subset.
        """
        scoped = self._cap_lane_scope(ranked, layer_of)
        items = [(node.node_id, layer_of.get(node.node_id, "utility")) for node in scoped]
        positions = self._layout_columns(items, kind)
        placed = [node for node in scoped if node.node_id in positions]
        return positions, placed

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
    ) -> SystemMap:
        """Build the runtime architecture map from file topology.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings.
            analysis: Graph analysis.

        Returns:
            Architecture system map.
        """
        selected = self._select_primary(nodes, links, analysis)
        layer_of_all = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        positions, selected = self._place(selected, layer_of_all, "architecture")
        chosen = {node.node_id for node in selected}
        kept = self._internal_links(links, chosen)
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
            meta={"scope": str(len(map_nodes)), "total": str(len(nodes)), "links": str(len(map_edges))},
        )

    def _build_workflow(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
    ) -> SystemMap:
        """Build the delivery workflow map across architectural lanes.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings.

        Returns:
            Workflow system map.
        """
        selected = self._select_primary(nodes, links, None)
        layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
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
        kept = self._internal_links(links, chosen)
        workflow_edges: List[MapEdge] = [
            MapEdge(source=e.source, target=e.target, label=e.relation, kind=e.relation)
            for e in kept
        ]
        items = [(node.node_id, layer_of[node.node_id]) for node in lane_nodes]
        positions = self._layout_columns(items, "workflow")
        lane_nodes = [node for node in lane_nodes if node.node_id in positions]
        chain = [node.node_id for node in lane_nodes]
        for first, second in zip(chain, chain[1:]):
            if not any(e.source == first and e.target == second for e in workflow_edges):
                workflow_edges.append(MapEdge(source=first, target=second, label="next", kind="next"))
        placed_ids = set(chain)
        ordered_edges = sorted(
            [e for e in workflow_edges if e.source in placed_ids and e.target in placed_ids],
            key=lambda e: (e.source, e.target),
        )[: max(0, self._config.DIAGRAM_MAX_EDGES)]
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
            meta={"scope": str(len(map_nodes)), "total": str(len(nodes)), "links": str(len(ordered_edges))},
        )

    def _build_sequence(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        analysis: Optional[AnalysisResult],
    ) -> SystemMap:
        """Build the request sequence map over top participants.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            analysis: Graph analysis.

        Returns:
            Sequence system map.
        """
        selected = self._select_primary(nodes, links, analysis)
        width_cap = min(
            max(1, self._config.DIAGRAM_SEQUENCE_MAX_PARTICIPANTS),
            self._sequence_capacity(),
        )
        participants = list(selected[: min(len(selected), width_cap)])
        if len(participants) < 2 and len(selected) >= 2:
            participants = list(selected[: min(len(selected), 2)])
        chosen = {node.node_id for node in participants}
        ordered_ids = [node.node_id for node in participants]
        positions = self._layout_sequence(ordered_ids)
        kept = self._internal_links(links, chosen)
        sequence_edges: List[MapEdge] = [
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
            meta={"scope": str(len(map_nodes)), "total": str(len(nodes)), "links": str(len(sequence_edges))},
        )

    def _build_dataflow(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
    ) -> SystemMap:
        """Build the data flow map from sources through stores.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings for sensitivity.

        Returns:
            Dataflow system map.
        """
        selected = self._select_primary(nodes, links, None)
        proto_layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        _proto_positions, selected = self._place(selected, proto_layer_of, "dataflow")
        chosen = {node.node_id for node in selected}
        kept = self._internal_links(links, chosen)
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
        positions, ordered = self._place(ordered, stage_of, "dataflow")
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
            meta={"scope": str(len(map_nodes)), "total": str(len(nodes)), "links": str(len(map_edges))},
        )

    def _build_lifecycle(
        self,
        nodes: Sequence[Node],
        links: Sequence[Edge],
        layers: Optional[Dict[str, str]],
        findings: Optional[Sequence[SecurityFinding]],
    ) -> SystemMap:
        """Build the change lifecycle map with waits, retries, and terminals.

        Args:
            nodes: Scanned file nodes.
            links: Internal edges.
            layers: Layer mapping.
            findings: Security findings.

        Returns:
            Lifecycle system map.
        """
        selected = self._select_primary(nodes, links, None)
        proto_layer_of = {node.node_id: (layers or {}).get(node.node_id, "utility") for node in selected}
        _proto_positions, selected = self._place(selected, proto_layer_of, "lifecycle")
        chosen = {node.node_id for node in selected}
        kept = self._internal_links(links, chosen)
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
        positions, selected = self._place(selected, state_of, "lifecycle")
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
        return SystemMap(
            kind="lifecycle",
            title=self._title_for("lifecycle"),
            nodes=map_nodes,
            edges=deduped[: max(0, self._config.DIAGRAM_MAX_EDGES)],
            views=views,
            meta={"scope": str(len(map_nodes)), "total": str(len(nodes)), "links": str(len(deduped))},
        )


class InteractiveMapRenderer:
    """Renders a system map as one self-contained interactive HTML document."""

    def __init__(self, config: Config) -> None:
        """Initialise the renderer with application configuration.

        Args:
            config: Central settings for preset, theme, and share size.
        """
        self._config = config

    def render(self, system_map: SystemMap) -> str:
        """Render a system map as a self-contained HTML document.

        Args:
            system_map: Validated system map intermediate representation.

        Returns:
            Complete standalone HTML document with inline SVG and scripting.
        """
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
                    "canvasWidth": self._config.DIAGRAM_CANVAS_WIDTH,
                    "canvasHeight": self._config.DIAGRAM_CANVAS_HEIGHT,
                }
            ),
        )
        document = document.replace(
            "__PRESETS_JSON__", self._safe_json(list(self._config.DIAGRAM_PRESETS))
        )
        document = document.replace("__CANVAS_W__", str(self._config.DIAGRAM_CANVAS_WIDTH))
        document = document.replace("__CANVAS_H__", str(self._config.DIAGRAM_CANVAS_HEIGHT))
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
<div class="routebox"><input id="route-from" placeholder="route from id" aria-label="Route source" title="Source node id for the route probe"><input id="route-to" placeholder="route to id" aria-label="Route target" title="Target node id for the route probe"><button type="button" data-action="route" aria-label="Probe directed route" title="Highlight the shortest authored directed path">Path</button></div>
<div class="journey" id="journey"></div>
<div class="receipt" id="receipt"></div>
</aside>
</div>
<dialog id="guide" aria-label="Diagram guide dialog">
<h2>Diagram guide</h2>
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
                "barnesHut": {
                    "gravitationalConstant": -60000,
                    "centralGravity": 0.15,
                    "springLength": 320,
                    "damping": 0.12,
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
                }
            ),
        )
        document = document.replace("__PHYSICS_JSON__", _json_payload(physics))
        document = document.replace(
            "__ROLES_JSON__",
            _json_payload(dict(self._config.DIAGRAM_ROLE_COLORS)),
        )
        return document

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
.views{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
.views button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:6px 9px;font:inherit;font-size:11px;cursor:pointer}
.journey{font-size:12px;line-height:1.7}
.receipt{font-size:11px;color:var(--muted);border:1px solid var(--border);border-radius:8px;padding:8px;margin-top:10px}
.routebox{display:flex;gap:6px;margin-top:8px}
.routebox input{flex:1;background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:7px;font:inherit;font-size:12px;min-width:0}
.routebox button{background:var(--canvas);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:7px 10px;font:inherit;font-size:12px;cursor:pointer}
.present .layout{grid-template-columns:minmax(0,1fr)}
.present .passport{display:none}
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
<button type="button" data-action="views-prev" aria-label="Previous chapter" title="Show the previous guided chapter">[</button>
<button type="button" data-action="views-next" aria-label="Next chapter" title="Show the next guided chapter">]</button>
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
<div class="views" id="chapters"></div>
<div class="counts" id="role-counts"></div>
<div class="row">1. Drag any node; physics settles the rest. 2. Click a node to focus it. 3. Upstream and Downstream trace authored reach. 4. Path probes the exact route between two ids. 5. Play walks the guided chapters. Press ? for every shortcut. This page loads its network engine from a CDN and needs network access.</div>
<div class="routebox"><input id="route-from" placeholder="route from id" aria-label="Route source" title="Source node id for the route probe"><input id="route-to" placeholder="route to id" aria-label="Route target" title="Target node id for the route probe"><button type="button" data-action="route" aria-label="Probe directed route" title="Highlight the shortest authored directed path">Path</button></div>
<div class="journey" id="journey"></div>
<div class="symbols" id="node-symbols"></div>
<div class="receipt" id="receipt"></div>
</aside>
</div>
<dialog id="guide" aria-label="Diagram guide dialog">
<h2>Diagram guide</h2>
<p><kbd>/</kbd> search &middot; <kbd>R</kbd> route probe &middot; <kbd>L</kbd> role lens &middot; <kbd>P</kbd> play &middot; <kbd>[</kbd> <kbd>]</kbd> chapters &middot; <kbd>F</kbd> present &middot; <kbd>S</kbd> style &middot; <kbd>T</kbd> theme &middot; <kbd>E</kbd> export &middot; <kbd>+</kbd> <kbd>-</kbd> <kbd>0</kbd> zoom &middot; <kbd>B</kbd> physics</p>
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
function paintNodes(){
var palette=themeBox();
var update=rawNodes.map(function(n){
return {id:n.id,color:{background:palette.box,border:roleColors[n.group]||"#94a3b8",highlight:{background:palette.box,border:roleColors[n.group]||"#94a3b8"}},font:{color:palette.ink,size:13,face:"monospace"}};});
visNodes.update(update);}
var visNodes=new vis.DataSet(rawNodes.map(function(n){return {id:n.id,label:n.label,title:n.title,group:n.group,shape:"box"};}));
var visEdges=new vis.DataSet(rawEdges.map(function(e,index){return {id:"e"+index,from:e.from,to:e.to,title:e.label,arrows:"to",dashes:!!e.dashes,smooth:{type:"dynamic"},color:{opacity:0.7}};}));
paintNodes();
var network=new vis.Network(container,{nodes:visNodes,edges:visEdges},{
physics:physics,
interaction:{hover:true,navigationButtons:false,keyboard:false},
nodes:{shape:"box",borderWidth:2,margin:10},
edges:{arrows:{to:{enabled:true}},smooth:{type:"dynamic"}}});
if(reduced&&physics.enabled){try{network.stabilize(50);}catch(e){}}
function outgoing(id){return rawEdges.filter(function(e){return e.from===id;});}
function incoming(id){return rawEdges.filter(function(e){return e.to===id;});}
function nodeById(id){for(var i=0;i<rawNodes.length;i++){if(rawNodes[i].id===id){return rawNodes[i];}}return null;}
function escapeHtml(text){
return String(text==null?"":text).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function neighborNames(ids){
var cap=(meta.neighbors||8);
return ids.slice().sort().slice(0,cap).map(function(id){var n=nodeById(id);return escapeHtml(n?n.label:id);});}
function renderNodeDetail(node){
if(!nodeSymbols){return;}
var ins=incoming(node.id).map(function(e){return e.from;});
var outs=outgoing(node.id).map(function(e){return e.to;});
var html="";
if(node.doc){html+='<p class="filedoc">'+escapeHtml(node.doc)+"</p>";}
var symbols=node.symbols||[];
if(symbols.length){
html+="<table><thead><tr><th>Symbol</th><th>Kind</th><th>Line</th></tr></thead><tbody>";
symbols.forEach(function(s){
var docTitle=s.doc?(' title="'+escapeHtml(s.doc)+'"'):"";
var name="<span"+docTitle+">"+escapeHtml(s.name)+"</span>"+(s.signature?" <code>"+escapeHtml(s.signature)+"</code>":"");
html+="<tr><td>"+name+"</td><td>"+escapeHtml(s.kind)+"</td><td>"+escapeHtml(s.line)+"</td></tr>";});
html+="</tbody></table>";
var hidden=(node.symbolTotal||symbols.length)-symbols.length;
if(hidden>0){html+='<p class="filedoc">+'+hidden+' more symbols in source.</p>';}}
else{html+='<p class="filedoc">No symbols extracted.</p>';}
html+='<p class="neighbors">Imports '+outs.length+(outs.length?": "+neighborNames(outs).join(", "):"")+"</p>";
html+='<p class="neighbors">Imported by '+ins.length+(ins.length?": "+neighborNames(ins).join(", "):"")+"</p>";
nodeSymbols.innerHTML=html;}
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
var nodeUpdate=rawNodes.map(function(n){return {id:n.id,hidden:false};});
visNodes.update(nodeUpdate);
var edgeUpdate=rawEdges.map(function(e,index){return {id:"e"+index,hidden:false};});
visEdges.update(edgeUpdate);}
function setHash(value){try{history.replaceState(null,"",value);}catch(e){location.hash=value;}}
function focusNode(id,reach){
var node=nodeById(id);if(!node){return;}
state.focus=id;state.reach=reach||null;
var allowed={};allowed[id]=true;
if(state.reach){var found=bfsReach(id,state.reach);found.members.forEach(function(m){allowed[m]=true;});
var hops=0;for(var k in found.hops){if(found.hops[k]>hops){hops=found.hops[k];}}
receipt.textContent=(state.reach==="downstream"?"Downstream":"Upstream")+" reach: "+found.members.length+" nodes, "+hops+" max hops. Authored relationships only.";}
else{receipt.textContent="In: "+incoming(id).length+" | Out: "+outgoing(id).length+" | Views: "+views.length;}
showOnly(allowed);
network.selectNodes([id]);
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
function renderRoleCounts(){
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
if(hash.indexOf("#view=")===0){var id=decodeURIComponent(hash.slice(6));for(var i=0;i<views.length;i++){if(views[i].id===id){showView(i);return;}}return;}
if(hash.indexOf("#focus=")===0){var rest=hash.slice(7).split("&reach=");focusNode(decodeURIComponent(rest[0]),rest[1]?decodeURIComponent(rest[1]):null);return;}}
network.on("click",function(params){
if(params.nodes.length>0){focusNode(params.nodes[0]);}});
network.on("stabilized",function(){receipt.textContent="Physics stabilized: "+rawNodes.length+" nodes placed.";});
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
else if(ev.key==="0"){try{network.fit();}catch(e){}}});
passportMeta.textContent=(meta.nodeCount||rawNodes.length)+" of "+(meta.totalFiles||rawNodes.length)+" files | "+(meta.edgeCount||rawEdges.length)+" links | "+views.length+" chapters. Primary scope only; full listing lives in the knowledge base.";
receipt.textContent="Live physics network. Drag nodes, search, focus, trace reach, probe routes, compare roles, or play chapters.";
renderChapters();renderRoleCounts();readHash();
})();
</script>
</body>
</html>"""
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
    ) -> Dict[str, str]:
        """Publish maps and a gallery index into a documentation directory.

        Args:
            maps: Mapping of diagram kind to system map.
            project_name: Display name used for index titles.
            output_dir: Destination directory for the static site.
            stats: Optional project counters shown in the gallery header.
            renderer: Map renderer with a write method, defaults to offline.

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
        index_target = root / "index.html"
        index_target.write_text(
            self.render_index(project_name, published, stats or {}, href_prefix),
            encoding="utf-8",
        )
        written["index"] = str(index_target)
        nojekyll_target = root / ".nojekyll"
        nojekyll_target.write_text("", encoding="utf-8")
        written["nojekyll"] = str(nojekyll_target)
        return written

    def render_index(
        self,
        project_name: str,
        maps: Dict[str, SystemMap],
        stats: Dict[str, int],
        href_prefix: Optional[str] = None,
    ) -> str:
        """Render the gallery index page for published maps.

        Args:
            project_name: Display name used for index titles.
            maps: Mapping of published diagram kind to system map.
            stats: Project counters shown in the gallery header.
            href_prefix: Relative prefix pointing at the map directory.

        Returns:
            Complete standalone HTML gallery document.
        """
        if href_prefix is None:
            href_prefix = self._href_prefix()
        title = self._escape(project_name.strip() or "Project")
        cards = []
        for kind in sorted(maps):
            system_map = maps[kind]
            cards.append(self._card(kind, system_map, href_prefix))
        gallery = "\n".join(cards) if cards else (
            '<p class="empty">No validated maps were published yet.</p>'
        )
        stats_line = self._stats_line(stats)
        return """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>""" + title + """ | System Maps</title>
<style>
:root{--canvas:#020617;--mask:#0f172a;--ink:#ffffff;--muted:#94a3b8;--border:#1e293b}
html[data-theme="light"]{--canvas:#f8fafc;--mask:#ffffff;--ink:#0f172a;--muted:#475569;--border:#e2e8f0}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
header{padding:28px 20px 18px;max-width:1024px;margin:0 auto}
header h1{font-size:22px;margin:0 0 8px}
header p{color:var(--muted);font-size:13px;margin:4px 0}
.controls{max-width:1024px;margin:0 auto;padding:0 20px 10px;display:flex;gap:8px;flex-wrap:wrap}
.controls input{background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font:inherit;font-size:12px;min-width:220px}
.controls button{background:var(--mask);color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font:inherit;font-size:12px;cursor:pointer}
.grid{max-width:1024px;margin:0 auto;padding:10px 20px 40px;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.card{background:var(--mask);border:1px solid var(--border);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:8px}
.card h2{font-size:15px;margin:0}
.card p{font-size:12px;color:var(--muted);margin:0;line-height:1.6}
.card .meta{font-size:11px;color:var(--muted)}
.card a{margin-top:auto;color:var(--ink);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font-size:12px;text-decoration:none;text-align:center}
.card a:hover,.card a:focus-visible{border-color:#22d3ee;outline:2px solid #22d3ee;outline-offset:2px}
.howto{max-width:1024px;margin:0 auto;padding:0 20px 20px}
.howto h2{font-size:15px;margin:0 0 8px}
.howto p{font-size:12px;color:var(--muted);line-height:1.7;margin:0}
.empty{color:var(--muted);font-size:13px}
footer{max-width:1024px;margin:0 auto;padding:0 20px 30px;color:var(--muted);font-size:11px}
</style>
</head>
<body>
<header>
<h1>""" + title + """ | System Maps</h1>
<p>""" + stats_line + """</p>
<p>This gallery page works offline. Each map loads its physics engine from a CDN and needs network access.</p>
</header>
<div class="controls">
<input id="filter" type="search" placeholder="Filter diagrams..." aria-label="Filter diagrams">
<button type="button" id="theme">Theme</button>
</div>
<main class="grid" id="gallery">
""" + gallery + """
</main>
<section class="howto">
<h2>How to read these maps</h2>
<p>Open any map, then: drag nodes freely while physics settles the rest, search (/) to filter, click a node to focus it with full file documentation, Upstream and Downstream to trace authored reach, Path to probe the exact route between two ids, Lens to compare semantic roles, Play to walk the guided chapters, Stabilize to re-run physics, Theme for dark and light, Export for PNG or typed JSON. Deep links such as #route=a~b restore any reading.</p>
</section>
<footer>Generated offline from scanned source topology. Counts reflect authored relationships only.</footer>
<script>
(function(){
"use strict";
var filter=document.getElementById("filter");
var theme=document.getElementById("theme");
var cards=Array.prototype.slice.call(document.querySelectorAll(".card"));
filter.addEventListener("input",function(){
var term=filter.value.trim().toLowerCase();
cards.forEach(function(card){
var text=(card.textContent||"").toLowerCase();
card.style.display=(!term||text.indexOf(term)>=0)?"":"none";});});
theme.addEventListener("click",function(){
var root=document.documentElement;
root.setAttribute("data-theme",root.getAttribute("data-theme")==="light"?"dark":"light");});
})();
</script>
</body>
</html>"""

    def _href_prefix(self) -> str:
        """Return the relative href prefix for map links.

        Returns:
            Map subdirectory with trailing slash, or empty string.
        """
        subdir = self._config.DIAGRAM_MAPS_SUBDIR.strip().strip("/")
        if subdir in ("", "."):
            return ""
        return subdir + "/"

    def _card(self, kind: str, system_map: SystemMap, href_prefix: str) -> str:
        """Render one gallery card linking to a published map.

        Args:
            kind: Diagram kind identifier.
            system_map: Published system map.
            href_prefix: Relative prefix pointing at the map directory.

        Returns:
            HTML card fragment with a relative map link.
        """
        href = self._escape(href_prefix + kind + ".html")
        total = system_map.meta.get("total", str(len(system_map.nodes)))
        return (
            '<article class="card" data-kind="'
            + self._escape(kind)
            + '"><h2>'
            + self._escape(system_map.title)
            + "</h2><p>"
            + self._escape(self.description_for(kind))
            + '</p><div class="meta">'
            + str(len(system_map.nodes))
            + " of "
            + self._escape(str(total))
            + " files in primary scope | "
            + str(len(system_map.edges))
            + " links | "
            + str(len(system_map.views))
            + ' chapters</div><a href="'
            + href
            + '">Open '
            + self._escape(kind)
            + " map</a>"
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
