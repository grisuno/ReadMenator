"""Flow graph model and deterministic layered layout (Sugiyama style).

Every architecture and execution-flow diagram is first built as a
FlowGraph (nodes with a title, wrapped detail lines, shape, tone and a
detail payload; typed edges). layout_flow() then places it:

1. Ranks: explicit ranks when the builder provides them (architecture
   tiers), otherwise longest-path ranks over the DAG left after removing
   DFS back edges.
2. Order: barycentric up/down sweeps reduce crossings.
3. Wrapping: a rank wider than ``max_per_row`` is folded into several
   rows, so no diagram degenerates into a thin strip.
4. Coordinates: every row is placed under the barycenter of its parents,
   overlaps are pushed apart, rows are stacked by their real heights.
5. Routing: forward edges are vertical cubic curves; back edges (loops,
   recursion, upward dependencies) leave on the right and bend around.

Sizes come from monospace text metrics, so the same coordinates drive
the SVG viewer and the PIL video frames. Pure Python, deterministic.
"""

from __future__ import annotations

import textwrap
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

SHAPES: Tuple[str, ...] = ("box", "decision", "loop", "terminal", "stop", "component", "io", "note")
TONES: Tuple[str, ...] = ("default", "entry", "external", "cycle", "decision", "stop", "muted", "hub")
EDGE_STYLES: Tuple[str, ...] = ("solid", "heavy", "dashed", "back", "upward")
BRANCH_LABELS: Set[str] = {"yes", "each"}
TRUNK_LABELS: Set[str] = {"no", "done", "otherwise", ""}


@dataclass
class FlowNode:
    """One diagram node.

    Attributes:
        id: Stable node id.
        title: Bold first line.
        lines: Detail lines (wrapped by layout).
        shape: One of SHAPES.
        tone: One of TONES (color family).
        detail: Free payload for the viewer side panel (file, line, doc, href, ...).
        rank: Explicit rank, or -1 to compute.
        x: Center x after layout.
        y: Center y after layout.
        w: Width after layout.
        h: Height after layout.
    """

    id: str
    title: str
    lines: List[str] = field(default_factory=list)
    shape: str = "box"
    tone: str = "default"
    detail: Dict[str, Any] = field(default_factory=dict)
    rank: int = -1
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0


@dataclass
class FlowEdge:
    """One directed diagram edge.

    Attributes:
        source: Source node id.
        target: Target node id.
        label: Short label ("" for none).
        style: One of EDGE_STYLES.
        points: Cubic Bezier control points after layout (start, c1, c2, end).
    """

    source: str
    target: str
    label: str = ""
    style: str = "solid"
    points: List[Tuple[float, float]] = field(default_factory=list)


@dataclass
class FlowGraph:
    """A complete diagram.

    Attributes:
        id: Stable diagram id.
        title: Heading.
        kind: architecture, control, calltree, or sequence.
        caption: One-paragraph reading guide.
        nodes: Nodes in insertion order.
        edges: Edges in insertion order.
        lanes: Horizontal bands as dicts (title, y, h) after layout.
        width: Layout width.
        height: Layout height.
        meta: Free metadata (entry point, reasons, stats).
        participants: Sequence diagram participants (kind == sequence).
        messages: Sequence diagram messages (kind == sequence).
    """

    id: str
    title: str
    kind: str
    caption: str = ""
    nodes: List[FlowNode] = field(default_factory=list)
    edges: List[FlowEdge] = field(default_factory=list)
    lanes: List[Dict[str, Any]] = field(default_factory=list)
    width: float = 0.0
    height: float = 0.0
    meta: Dict[str, Any] = field(default_factory=dict)
    participants: List[Dict[str, Any]] = field(default_factory=list)
    messages: List[Dict[str, Any]] = field(default_factory=list)

    def node(self, node_id: str) -> Optional[FlowNode]:
        """Return the node with *node_id*."""
        for item in self.nodes:
            if item.id == node_id:
                return item
        return None

    def to_dict(self) -> Dict[str, Any]:
        """Serialise the laid-out diagram for the HTML viewer."""
        return {
            "id": self.id, "title": self.title, "kind": self.kind, "caption": self.caption,
            "w": round(self.width, 1), "h": round(self.height, 1), "meta": self.meta,
            "lanes": self.lanes,
            "nodes": [
                {"id": n.id, "t": n.title, "l": n.lines, "s": n.shape, "o": n.tone, "d": n.detail,
                 "x": round(n.x, 1), "y": round(n.y, 1), "w": round(n.w, 1), "h": round(n.h, 1)}
                for n in self.nodes
            ],
            "edges": [
                {"s": e.source, "t": e.target, "l": e.label, "y": e.style,
                 "p": [[round(px, 1), round(py, 1)] for px, py in e.points]}
                for e in self.edges
            ],
            "participants": self.participants,
            "messages": self.messages,
        }


@dataclass(frozen=True)
class LayoutMetrics:
    """Text and spacing metrics shared by the layout, the SVG viewer, and the video.

    Attributes:
        char_w: Width of one monospace character of detail text.
        title_char_w: Width of one title character.
        line_h: Height of one detail line.
        title_h: Height of the title line.
        pad_x: Horizontal padding inside a node.
        pad_y: Vertical padding inside a node.
        max_chars: Wrap width of detail lines in characters.
        max_lines: Maximum detail lines per node.
        min_w: Minimum node width.
        gap_x: Gap between nodes in a row.
        gap_y: Gap between rows.
        max_per_row: Rank width before wrapping into another row.
        margin: Outer margin.
    """

    char_w: float = 6.6
    title_char_w: float = 7.6
    line_h: float = 15.0
    title_h: float = 18.0
    pad_x: float = 12.0
    pad_y: float = 9.0
    max_chars: int = 38
    max_lines: int = 3
    min_w: float = 96.0
    gap_x: float = 34.0
    gap_y: float = 54.0
    max_per_row: int = 5
    margin: float = 24.0


def _wrap(lines: List[str], metrics: LayoutMetrics) -> List[str]:
    """Wrap and cap detail lines."""
    out: List[str] = []
    for line in lines:
        text = " ".join(str(line).split())
        if not text:
            continue
        out.extend(textwrap.wrap(text, metrics.max_chars, break_long_words=True) or [""])
    if len(out) > metrics.max_lines:
        out = out[: metrics.max_lines]
        last = out[-1]
        out[-1] = (last[: max(0, metrics.max_chars - 3)].rstrip() + "...") if len(last) > metrics.max_chars - 3 else last + "..."
    return out


def measure(node: FlowNode, metrics: LayoutMetrics) -> None:
    """Set the node's wrapped lines and its width and height from text metrics."""
    title = node.title if len(node.title) <= metrics.max_chars + 10 else node.title[: metrics.max_chars + 7] + "..."
    node.title = title
    node.lines = _wrap(node.lines, metrics)
    widest = max([len(title) * metrics.title_char_w] + [len(l) * metrics.char_w for l in node.lines])
    node.w = max(metrics.min_w, widest + 2 * metrics.pad_x)
    node.h = metrics.title_h + len(node.lines) * metrics.line_h + 2 * metrics.pad_y
    if node.shape == "decision":
        node.w += 56
        node.h += 26
    elif node.shape == "loop":
        node.w += 30


def _ranks(graph: FlowGraph) -> Dict[str, int]:
    """Explicit ranks, or longest-path ranks over the DAG without DFS back edges."""
    ids = [n.id for n in graph.nodes]
    if graph.nodes and all(n.rank >= 0 for n in graph.nodes):
        return {n.id: n.rank for n in graph.nodes}
    succ: Dict[str, List[str]] = {i: [] for i in ids}
    for edge in graph.edges:
        if edge.source in succ and edge.target in succ and edge.source != edge.target:
            succ[edge.source].append(edge.target)
    state: Dict[str, int] = {}
    back: Set[Tuple[str, str]] = set()
    order: List[str] = []
    indeg = {i: 0 for i in ids}
    for edge in graph.edges:
        if edge.target in indeg and edge.source != edge.target:
            indeg[edge.target] += 1
    roots = [i for i in ids if indeg[i] == 0] or ids[:1]
    for root in roots + ids:
        if root in state:
            continue
        stack: List[Tuple[str, int]] = [(root, 0)]
        state[root] = 1
        while stack:
            vertex, pos = stack[-1]
            if pos < len(succ[vertex]):
                stack[-1] = (vertex, pos + 1)
                nxt = succ[vertex][pos]
                if state.get(nxt) == 1:
                    back.add((vertex, nxt))
                elif nxt not in state:
                    state[nxt] = 1
                    stack.append((nxt, 0))
            else:
                state[vertex] = 2
                order.append(vertex)
                stack.pop()
    rank: Dict[str, int] = {}
    for vertex in reversed(order):
        if vertex not in rank:
            rank[vertex] = 0
        for nxt in succ[vertex]:
            if (vertex, nxt) in back:
                continue
            rank[nxt] = max(rank.get(nxt, 0), rank[vertex] + 1)
    for node in graph.nodes:
        if node.rank >= 0:
            rank[node.id] = node.rank
    return rank


def layout_flow(graph: FlowGraph, metrics: Optional[LayoutMetrics] = None, direction: str = "TB") -> FlowGraph:
    """Lay out *graph* in place and return it.

    Args:
        graph: Diagram to place.
        metrics: Text and spacing metrics.
        direction: TB (ranks top to bottom) or LR (ranks left to right).

    Returns:
        The same graph with node coordinates, edge control points, lanes, and size.
    """
    m = metrics or LayoutMetrics()
    if not graph.nodes:
        graph.width = graph.height = 0.0
        return graph
    for node in graph.nodes:
        measure(node, m)
    horizontal = direction == "LR"
    if horizontal:
        for node in graph.nodes:
            node.w, node.h = node.h, node.w
    rank = _ranks(graph)
    by_id = {n.id: n for n in graph.nodes}
    parents: Dict[str, List[str]] = {n.id: [] for n in graph.nodes}
    children: Dict[str, List[str]] = {n.id: [] for n in graph.nodes}
    for edge in graph.edges:
        if edge.source in by_id and edge.target in by_id and rank[edge.target] > rank[edge.source]:
            parents[edge.target].append(edge.source)
            children[edge.source].append(edge.target)
    levels: Dict[int, List[str]] = {}
    for node in graph.nodes:
        levels.setdefault(rank[node.id], []).append(node.id)
    keys = sorted(levels)
    position: Dict[str, float] = {}
    for key in keys:
        for pos, nid in enumerate(levels[key]):
            position[nid] = float(pos)
    for _sweep in range(6):
        for key in keys[1:]:
            levels[key].sort(key=lambda nid: (
                sum(position[p] for p in parents[nid]) / len(parents[nid]) if parents[nid] else position[nid],
                position[nid],
            ))
            for pos, nid in enumerate(levels[key]):
                position[nid] = float(pos)
        for key in reversed(keys[:-1]):
            levels[key].sort(key=lambda nid: (
                sum(position[c] for c in children[nid]) / len(children[nid]) if children[nid] else position[nid],
                position[nid],
            ))
            for pos, nid in enumerate(levels[key]):
                position[nid] = float(pos)
    rows: List[Tuple[int, List[str]]] = []
    per_row = max(1, m.max_per_row if not horizontal else max(m.max_per_row * 2, 6))
    for key in keys:
        members = levels[key]
        for start in range(0, len(members), per_row):
            rows.append((key, members[start:start + per_row]))
    titled = bool(graph.meta.get("lane_titles")) and not horizontal
    lane_pad = m.title_h + 14 if titled else 0.0
    cursor = m.margin + lane_pad
    lanes_raw: Dict[int, List[float]] = {}
    for key, members in rows:
        height = max(by_id[nid].h for nid in members)
        desired: Dict[str, float] = {}
        for nid in members:
            node = by_id[nid]
            incoming = [e for e in graph.edges if e.target == nid and e.source in parents[nid]]
            if incoming:
                first = by_id[incoming[0].source]
                label = incoming[0].label.lower()
                if label in BRANCH_LABELS or label.startswith("except"):
                    desired[nid] = first.x + first.w / 2 + m.gap_x + node.w / 2
                else:
                    others = [by_id[p].x for p in parents[nid]]
                    desired[nid] = first.x if label in TRUNK_LABELS else sum(others) / len(others)
            else:
                desired[nid] = 0.0
        placed = sorted(members, key=lambda nid: (desired[nid], members.index(nid)))
        if not any(parents[nid] for nid in members):
            total = sum(by_id[nid].w for nid in placed) + m.gap_x * (len(placed) - 1)
            left = -total / 2
            for nid in placed:
                desired[nid] = left + by_id[nid].w / 2
                left += by_id[nid].w + m.gap_x
        previous: Optional[str] = None
        for nid in placed:
            x = desired[nid]
            if previous is not None:
                x = max(x, by_id[previous].x + by_id[previous].w / 2 + m.gap_x + by_id[nid].w / 2)
            by_id[nid].x = x
            by_id[nid].y = cursor + height / 2
            previous = nid
        lanes_raw.setdefault(key, [cursor, cursor + height])
        lanes_raw[key][1] = cursor + height
        cursor += height + m.gap_y + (lane_pad if titled and rows.index((key, members)) + 1 < len(rows) and rows[rows.index((key, members)) + 1][0] != key else 0.0)
    min_x = min(n.x - n.w / 2 for n in graph.nodes)
    for node in graph.nodes:
        node.x += m.margin - min_x
    width = max(n.x + n.w / 2 for n in graph.nodes) + m.margin
    height = cursor - m.gap_y + m.margin
    back_slots: Dict[str, int] = {}
    for edge in graph.edges:
        a, b = by_id.get(edge.source), by_id.get(edge.target)
        if a is None or b is None:
            continue
        forward = rank[edge.target] > rank[edge.source] and b.y > a.y
        if forward:
            start = (a.x, a.y + a.h / 2)
            end = (b.x, b.y - b.h / 2)
            bend = max(18.0, (end[1] - start[1]) * 0.5)
            edge.points = [start, (start[0], start[1] + bend), (end[0], end[1] - bend), end]
        else:
            slot = back_slots.get("all", 0)
            back_slots["all"] = slot + 1
            start = (a.x + a.w / 2, a.y)
            end = (b.x + b.w / 2, b.y)
            reach = max(start[0], end[0]) + 40 + 26 * (slot % 8)
            edge.points = [start, (reach, start[1]), (reach, end[1]), end]
            width = max(width, reach + m.margin)
    graph.lanes = []
    if horizontal:
        for node in graph.nodes:
            node.x, node.y = node.y, node.x
            node.w, node.h = node.h, node.w
        for edge in graph.edges:
            a, b = by_id.get(edge.source), by_id.get(edge.target)
            if a is None or b is None:
                continue
            if rank[edge.target] > rank[edge.source] and b.x > a.x:
                start = (a.x + a.w / 2, a.y)
                end = (b.x - b.w / 2, b.y)
                bend = max(18.0, (end[0] - start[0]) * 0.5)
                edge.points = [start, (start[0] + bend, start[1]), (end[0] - bend, end[1]), end]
            else:
                start = (a.x, a.y + a.h / 2)
                end = (b.x, b.y + b.h / 2)
                reach = max(start[1], end[1]) + 40
                edge.points = [start, (start[0], reach), (end[0], reach), end]
        width, height = height, width
        width = max(width, max(p[0] for e in graph.edges for p in e.points) + m.margin if graph.edges else width)
        height = max(height, max(p[1] for e in graph.edges for p in e.points) + m.margin if graph.edges else height)
    else:
        titles = graph.meta.get("lane_titles", {})
        for key in keys:
            top, bottom = lanes_raw[key]
            if str(key) in titles:
                graph.lanes.append({"t": titles[str(key)], "y": round(top - lane_pad - 6, 1),
                                    "h": round(bottom - top + lane_pad + 18, 1)})
    graph.width = width
    graph.height = height
    return graph


def layout_sequence(graph: FlowGraph, metrics: Optional[LayoutMetrics] = None) -> FlowGraph:
    """Place sequence participants as columns and messages as rows.

    Args:
        graph: Diagram with ``participants`` ({id, t}) and ``messages`` ({s, t, l, d}).
        metrics: Text metrics.

    Returns:
        The graph with participant x / box width and message y filled in.
    """
    m = metrics or LayoutMetrics()
    x = m.margin
    col: Dict[str, float] = {}
    for part in graph.participants:
        w = max(m.min_w + 20, len(str(part["t"])) * m.title_char_w + 2 * m.pad_x)
        part["w"] = round(w, 1)
        part["x"] = round(x + w / 2, 1)
        col[part["id"]] = part["x"]
        x += w + m.gap_x * 2
    y = m.margin + 52
    for msg in graph.messages:
        msg["y"] = round(y, 1)
        msg["x1"] = col.get(msg["s"], 0.0)
        msg["x2"] = col.get(msg["t"], 0.0)
        y += 36
    graph.width = x - m.gap_x * 2 + m.margin
    graph.height = y + m.margin
    return graph
