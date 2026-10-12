"""Architecture and execution-flow Mermaid diagrams from static structure.

Two deterministic, zero-token generators:

* ArchitectureDiagramBuilder aggregates files into components (analyzer
  communities, falling back to directories), builds the weighted
  component dependency graph, condenses strongly connected components
  (Tarjan) so cycles are explicit, removes transitively implied edges
  (transitive reduction on the condensation DAG), places components in
  architectural-layer lanes ordered by longest-path rank, and renders a
  ``flowchart TB`` whose edge thickness and labels carry import weight
  and whose cycle edges are highlighted.
* ExecutionFlowBuilder scores entry points (``__main__`` guards,
  ``main`` functions, CLI and server files, call-graph sources), walks
  the resolved call graph in call-site order to produce an execution
  call tree, renders a control-flow flowchart (decisions, loops, try
  blocks, returns) for Python entry functions from ``ast``, and a
  cross-file ``sequenceDiagram`` of the same walk.
"""

from __future__ import annotations

import ast
import re
import warnings
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Dict, List, Optional, Set, Tuple

from readmenator._apidocs import is_vendored_path
from readmenator._config import Config
from readmenator._models import AnalysisResult, Edge, Node
from readmenator._pytypes import PythonReceiverTypes
from readmenator._symindex import ResolvedCall, SymbolDef, SymbolIndex

LAYER_ORDER: Tuple[str, ...] = (
    "presentation", "business_logic", "data_access", "infrastructure", "utility", "testing",
)
LAYER_TITLES: Dict[str, str] = {
    "presentation": "Presentation / entry",
    "business_logic": "Business logic",
    "data_access": "Data access",
    "infrastructure": "Infrastructure",
    "utility": "Core / utility",
    "testing": "Tests",
}
_ENTRY_STEMS: Set[str] = {
    "__main__", "main", "cli", "app", "server", "index", "manage", "wsgi", "asgi",
    "program", "entry", "entrypoint", "run", "bootstrap", "start",
}
_ENTRY_NAMES: Set[str] = {
    "main", "Main", "run", "cli", "app", "start", "serve", "handler",
    "lambda_handler", "execute", "entrypoint", "entry_point", "_main", "init_app",
}
_MAIN_GUARD_RE = re.compile(r"^if\s+__name__\s*==\s*['\"]__main__['\"]\s*:", re.MULTILINE)
_HARD_MAIN_LANGUAGES: Set[str] = {
    "c", "cc", "cpp", "cxx", "C", "go", "rs", "java", "cs", "kt", "kts", "scala", "swift", "dart", "nim",
}


_MERMAID_ESCAPES: Dict[str, str] = {
    "#": "#35;", '"': "#quot;", "<": "#lt;", ">": "#gt;", ";": "#59;", "`": "#96;",
}


def mermaid_id(text: str, prefix: str = "n") -> str:
    """Return a Mermaid-safe identifier for *text*."""
    return f"{prefix}_" + re.sub(r"[^A-Za-z0-9_]", "_", text)


def mermaid_text(text: str, limit: int = 0) -> str:
    """Escape *text* for a quoted Mermaid label, optionally truncating it."""
    clean = " ".join(str(text).split())
    if limit and len(clean) > limit:
        clean = clean[: max(1, limit - 3)].rstrip() + "..."
    return "".join(_MERMAID_ESCAPES.get(char, char) for char in clean)


def tarjan_scc(vertices: List[str], adjacency: Dict[str, Set[str]]) -> List[List[str]]:
    """Return strongly connected components (iterative Tarjan, deterministic order).

    Args:
        vertices: Vertex ids (visited in sorted order).
        adjacency: Directed successor sets.

    Returns:
        Components as sorted vertex lists, ordered by their smallest vertex.
    """
    index_of: Dict[str, int] = {}
    low: Dict[str, int] = {}
    on_stack: Set[str] = set()
    stack: List[str] = []
    result: List[List[str]] = []
    counter = 0
    for root in sorted(vertices):
        if root in index_of:
            continue
        work: List[Tuple[str, List[str]]] = [(root, sorted(adjacency.get(root, ())))]
        index_of[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        while work:
            vertex, pending = work[-1]
            if pending:
                nxt = pending.pop(0)
                if nxt not in index_of:
                    index_of[nxt] = low[nxt] = counter
                    counter += 1
                    stack.append(nxt)
                    on_stack.add(nxt)
                    work.append((nxt, sorted(adjacency.get(nxt, ()))))
                elif nxt in on_stack:
                    low[vertex] = min(low[vertex], index_of[nxt])
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[vertex])
            if low[vertex] == index_of[vertex]:
                component: List[str] = []
                while True:
                    item = stack.pop()
                    on_stack.discard(item)
                    component.append(item)
                    if item == vertex:
                        break
                result.append(sorted(component))
    result.sort(key=lambda comp: comp[0])
    return result


def transitive_reduction(adjacency: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """Return the transitive reduction of a DAG.

    An edge ``u -> v`` is dropped when ``v`` stays reachable from ``u``
    through another successor, so the diagram keeps only direct
    architectural dependencies.

    Args:
        adjacency: Successor sets of an acyclic graph.

    Returns:
        Reduced successor sets (same vertices).
    """
    reach: Dict[str, Set[str]] = {}

    def reachable(vertex: str) -> Set[str]:
        """Return every vertex reachable from *vertex* (memoised, iterative)."""
        if vertex in reach:
            return reach[vertex]
        order: List[str] = []
        seen: Set[str] = set()
        todo = [vertex]
        while todo:
            current = todo.pop()
            if current in seen:
                continue
            seen.add(current)
            order.append(current)
            todo.extend(adjacency.get(current, ()))
        for item in reversed(order):
            if item in reach:
                continue
            acc: Set[str] = set()
            for succ in adjacency.get(item, ()):
                acc.add(succ)
                acc |= reach.get(succ, set())
            reach[item] = acc
        return reach[vertex]

    reduced: Dict[str, Set[str]] = {}
    for vertex in sorted(adjacency):
        successors = adjacency.get(vertex, set())
        keep: Set[str] = set()
        for target in successors:
            implied = any(target in reachable(other) for other in successors if other != target)
            if not implied:
                keep.add(target)
        reduced[vertex] = keep
    return reduced


def eades_lin_smyth(vertices: List[str], weight: Dict[Tuple[str, str], int]) -> List[str]:
    """Order vertices so that heavy dependencies point forward (weighted ELS heuristic).

    Eades, Lin and Smyth (1993): repeatedly peel sinks to the back and
    sources to the front; otherwise move the vertex with the largest
    (outgoing - incoming) weight to the front. Edges that point
    backwards in the result form a small feedback arc set. Ties break
    on the vertex key, so the order is deterministic.

    Args:
        vertices: Vertex keys.
        weight: Directed edge weights keyed by (source, target).

    Returns:
        Vertices from highest level (dependents) to lowest (dependencies).
    """
    remaining: Set[str] = set(vertices)
    out_w: Dict[str, Dict[str, int]] = {v: {} for v in vertices}
    in_w: Dict[str, Dict[str, int]] = {v: {} for v in vertices}
    for (src, dst), count in weight.items():
        if src in remaining and dst in remaining and src != dst:
            out_w[src][dst] = out_w[src].get(dst, 0) + count
            in_w[dst][src] = in_w[dst].get(src, 0) + count
    head: List[str] = []
    tail: List[str] = []

    def live(table: Dict[str, int]) -> int:
        """Sum the weights of edges to vertices still remaining."""
        return sum(w for other, w in table.items() if other in remaining)

    while remaining:
        progressed = True
        while progressed:
            progressed = False
            for vertex in sorted(remaining):
                if live(out_w[vertex]) == 0:
                    tail.insert(0, vertex)
                    remaining.discard(vertex)
                    progressed = True
            for vertex in sorted(remaining):
                if live(in_w[vertex]) == 0:
                    head.append(vertex)
                    remaining.discard(vertex)
                    progressed = True
        if remaining:
            best = max(sorted(remaining), key=lambda v: live(out_w[v]) - live(in_w[v]))
            head.append(best)
            remaining.discard(best)
    return head + tail


@dataclass
class Component:
    """One architectural component (a group of files).

    Attributes:
        key: Stable component key.
        label: Display label.
        files: Member file ids (sorted).
        symbols: Total symbol count of member files.
        core: Member file with the most symbols.
        layer: Dominant architectural layer.
        has_entry: Whether an entry-point file belongs to the component.
    """

    key: str
    label: str
    files: List[str] = field(default_factory=list)
    symbols: int = 0
    core: str = ""
    layer: str = "utility"
    has_entry: bool = False


class ArchitectureDiagramBuilder:
    """Builds a layered, cycle-aware, transitively reduced component diagram."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for component budgets and test exclusion.
        """
        self._config = config

    def components(
        self,
        nodes: List[Node],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
    ) -> List[Component]:
        """Group files into components with dominant layers.

        Args:
            nodes: Scanned file nodes.
            analysis: Optional analyzer communities.
            layers: Optional file-to-layer mapping.

        Returns:
            Components sorted by size descending, then key.
        """
        layers = layers or {}
        include_tests = self._config.ARCH_DIAGRAM_INCLUDE_TESTS
        by_id = {n.node_id: n for n in nodes}
        owner: Dict[str, str] = {}
        labels: Dict[str, str] = {}
        if analysis and analysis.communities:
            for community in analysis.communities:
                key = f"c{community.community_id}"
                labels[key] = community.label or key
                for file_id in sorted(community.file_ids):
                    if file_id in by_id:
                        owner.setdefault(file_id, key)
        for node in sorted(nodes, key=lambda n: n.node_id):
            if node.node_id in owner:
                continue
            parts = PurePosixPath(node.node_id).parts
            directory = parts[0] if len(parts) > 1 else "(root)"
            key = f"d:{directory}"
            labels.setdefault(key, directory)
            owner[node.node_id] = key
        groups: Dict[str, Component] = {}
        for file_id, key in sorted(owner.items()):
            if is_vendored_path(file_id, self._config):
                continue
            layer = layers.get(file_id, "utility")
            if layer == "testing" and not include_tests:
                continue
            component = groups.setdefault(key, Component(key=key, label=labels[key]))
            component.files.append(file_id)
        entry_stems = _ENTRY_STEMS
        for component in groups.values():
            counts: Dict[str, int] = {}
            best = ("", -1)
            for file_id in component.files:
                node = by_id[file_id]
                component.symbols += len(node.symbols)
                counts[layers.get(file_id, "utility")] = counts.get(layers.get(file_id, "utility"), 0) + 1
                if len(node.symbols) > best[1] or (len(node.symbols) == best[1] and file_id < best[0]):
                    best = (file_id, len(node.symbols))
                if PurePosixPath(file_id).stem in entry_stems:
                    component.has_entry = True
            component.core = best[0]
            component.layer = min(
                counts, key=lambda lay: (-counts[lay], LAYER_ORDER.index(lay) if lay in LAYER_ORDER else len(LAYER_ORDER))
            ) if counts else "utility"
        ordered = sorted(groups.values(), key=lambda c: (-len(c.files), c.key))
        cap = max(1, int(self._config.ARCH_DIAGRAM_MAX_COMPONENTS))
        return ordered[:cap]

    def render(
        self,
        nodes: List[Node],
        resolved_edges: Optional[List[Edge]],
        analysis: Optional[AnalysisResult] = None,
        layers: Optional[Dict[str, str]] = None,
    ) -> Tuple[str, Dict[str, object]]:
        """Render the tiered architecture overview.

        Components are ordered with the weighted Eades-Lin-Smyth
        feedback-arc-set heuristic, so the dependency direction that
        most imports agree on points downwards. Edges against that
        order are the minimal set that creates cycles ("upward"
        dependencies, drawn dashed red). Tiers are longest-path levels
        over the remaining acyclic edges, and implied forward edges are
        removed by transitive reduction.

        Args:
            nodes: Scanned file nodes.
            resolved_edges: Resolved import edges.
            analysis: Optional analyzer communities.
            layers: Optional file-to-layer mapping.

        Returns:
            Tuple of (Mermaid source, stats with components, edges,
            reduced edge count, upward edges, cycles, tiers).
        """
        components = self.components(nodes, analysis, layers)
        empty: Dict[str, object] = {"components": 0, "edges": 0, "reduced": 0, "upward": [], "cycles": [], "tiers": 0}
        if not components:
            return "", empty
        owner = {f: c.key for c in components for f in c.files}
        weight: Dict[Tuple[str, str], int] = {}
        for edge in resolved_edges or []:
            if edge.relation != "resolved_imports":
                continue
            src, dst = owner.get(edge.source), owner.get(edge.target)
            if src and dst and src != dst:
                weight[(src, dst)] = weight.get((src, dst), 0) + 1
        keys = [c.key for c in components]
        order = eades_lin_smyth(keys, weight)
        position = {key: pos for pos, key in enumerate(order)}
        forward: Dict[str, Set[str]] = {key: set() for key in keys}
        upward: List[Tuple[str, str, int]] = []
        for (src, dst), count in sorted(weight.items()):
            if position[src] < position[dst]:
                forward[src].add(dst)
            else:
                upward.append((src, dst, count))
        tier: Dict[str, int] = {}
        for key in order:
            preds = [p for p in keys if key in forward[p]]
            tier[key] = max([tier[p] + 1 for p in preds if p in tier] or [0])
        reduced = transitive_reduction(forward)
        adjacency: Dict[str, Set[str]] = {key: set() for key in keys}
        for (src, dst) in weight:
            adjacency[src].add(dst)
        cyclic = [comp for comp in tarjan_scc(keys, adjacency) if len(comp) > 1]
        kept: List[Tuple[str, str, int, bool]] = []
        dropped = 0
        for (src, dst), count in sorted(weight.items(), key=lambda kv: (position[kv[0][0]], position[kv[0][1]])):
            if position[src] < position[dst]:
                if dst in reduced[src]:
                    kept.append((src, dst, count, False))
                else:
                    dropped += 1
        for src, dst, count in upward:
            kept.append((src, dst, count, True))
        by_key = {c.key: c for c in components}
        lines = [
            "flowchart TB",
            "    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;",
            "    classDef comp fill:#111827,stroke:#38bdf8,color:#e5e7eb;",
            "    classDef cyc fill:#1f1530,stroke:#f472b6,color:#fce7f3,stroke-width:2px;",
        ]
        in_cycle = {key for comp in cyclic for key in comp}
        label_cap = int(self._config.ARCH_DIAGRAM_LABEL_CHARS)
        tiers = sorted(set(tier.values()))
        for level in tiers:
            members = sorted((by_key[k] for k in keys if tier[k] == level), key=lambda c: (position[c.key], c.key))
            title = f"Tier {level + 1}" + (" (entry / high level)" if level == tiers[0] and len(tiers) > 1 else "")
            if level == tiers[-1] and len(tiers) > 1:
                title = f"Tier {level + 1} (foundation)"
            lines.append(f'    subgraph {mermaid_id(str(level), "tier")}["{mermaid_text(title)}"]')
            lines.append("        direction LR")
            for component in members:
                core = PurePosixPath(component.core).name if component.core else ""
                layer = LAYER_TITLES.get(component.layer, component.layer)
                label = (
                    f"{mermaid_text(component.label, label_cap)}<br/>"
                    f"{len(component.files)} files, {component.symbols} symbols<br/>"
                    f"{mermaid_text(layer)}"
                    + (f", core {mermaid_text(core, label_cap)}" if core else "")
                )
                css = "entry" if component.has_entry else ("cyc" if component.key in in_cycle else "comp")
                lines.append(f'        {mermaid_id(component.key, "c")}["{label}"]:::{css}')
            lines.append("    end")
        heavy = self._heavy_threshold([count for _, _, count, up in kept if not up])
        upward_links: List[int] = []
        for pos, (src, dst, count, up) in enumerate(kept):
            if up:
                lines.append(f'    {mermaid_id(dst, "c")} <-.-|"{count} upward"| {mermaid_id(src, "c")}')
                upward_links.append(pos)
            else:
                arrow = "==>" if count >= heavy else "-->"
                lines.append(f'    {mermaid_id(src, "c")} {arrow}|"{count}"| {mermaid_id(dst, "c")}')
        if upward_links:
            lines.append(f"    linkStyle {','.join(str(i) for i in upward_links)} stroke:#f87171,stroke-width:2px;")
        anchors = [
            min((k for k in keys if tier[k] == level), key=lambda k: (position[k], k)) for level in tiers
        ]
        for upper, lower in zip(anchors, anchors[1:]):
            lines.append(f'    {mermaid_id(upper, "c")} ~~~ {mermaid_id(lower, "c")}')
        stats: Dict[str, object] = {
            "components": len(components),
            "edges": len(kept),
            "reduced": dropped,
            "upward": [(by_key[s].label, by_key[d].label, c) for s, d, c in upward],
            "cycles": [[by_key[k].label for k in comp] for comp in cyclic],
            "tiers": len(tiers),
            "entry_components": [c.label for c in components if c.has_entry],
        }
        return "\n".join(lines), stats

    @staticmethod
    def _heavy_threshold(counts: List[int]) -> int:
        """Return the import count at the top quartile (at least 2)."""
        if not counts:
            return 2
        ordered = sorted(counts)
        return max(2, ordered[int(0.75 * (len(ordered) - 1))])


@dataclass
class EntryPoint:
    """A scored execution entry point.

    Attributes:
        file: Relative file id.
        name: Callable name ("" for a module-level ``__main__`` block).
        line: One-based definition (or guard) line.
        score: Heuristic entry score.
        reasons: Human-readable evidence.
    """

    file: str
    name: str
    line: int
    score: int
    reasons: List[str] = field(default_factory=list)

    @property
    def key(self) -> str:
        """Return the call-graph key of this entry point."""
        return f"{self.file}::{self.name}" if self.name else f"{self.file}::<main>"


@dataclass
class FlowStep:
    """One step of an execution walk.

    Attributes:
        caller: Caller key (``file::name``).
        callee: Callee key.
        line: Call-site line in the caller file.
        depth: Depth from the entry point (1 = direct call).
        repeat: True when the callee was already expanded earlier.
        recursive: True when the callee is on the current call stack.
    """

    caller: str
    callee: str
    line: int
    depth: int
    repeat: bool = False
    recursive: bool = False


class ExecutionFlowBuilder:
    """Detects entry points and renders their execution flows as Mermaid."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for entry-point, depth, and step budgets.
        """
        self._config = config
        self._owners: Dict[str, str] = {}

    def _is_test(self, file_id: str) -> bool:
        """Return True for files under test trees or named as tests."""
        tokens: Set[str] = set()
        for part in PurePosixPath(file_id).parts:
            stem = part.rsplit(".", 1)[0].lower()
            tokens.add(stem)
            tokens.update(t for t in re.split(r"[_\-.]", stem) if t)
        return bool(tokens & set(self._config.APIDOCS_TEST_PATH_TOKENS))

    def call_graph(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]],
        content_map: Optional[Dict[str, str]],
    ) -> Tuple[Dict[str, List[Tuple[int, str]]], Dict[str, SymbolDef], List[ResolvedCall]]:
        """Build the ordered call graph keyed by ``file::name``.

        Returns:
            Tuple of (caller -> ordered (line, callee) list, definitions by
            key, all resolved calls).
        """
        index = SymbolIndex(self._config)
        defs: Dict[str, SymbolDef] = {}
        at_line: Dict[Tuple[str, int], str] = {}
        by_file: Dict[str, List[Tuple[str, SymbolDef]]] = {}
        for items in index.build(nodes, content_map).values():
            for definition in items:
                key = definition.qualified
                if key in defs:
                    key = f"{definition.qualified}@{definition.line}"
                defs[key] = definition
                at_line[(definition.file, definition.line)] = key
                by_file.setdefault(definition.file, []).append((key, definition))
        calls = index.resolve(nodes, edges, resolved_edges, content_map)
        language = {n.node_id: n.language for n in nodes}
        types = PythonReceiverTypes(content_map or {}, language)
        self._owners = {
            key: types.owner_of(d.file, d.line) for key, d in defs.items() if types.owner_of(d.file, d.line)
        }

        def caller_key(site_file: str, site_line: int, caller: str) -> str:
            """Return the definition key of the scope making a call."""
            scope = types.scope_at(site_file, site_line)
            if scope is not None and (site_file, scope.start) in at_line:
                return at_line[(site_file, scope.start)]
            if not caller:
                return f"{site_file}::<main>"
            best = ""
            best_line = -1
            for key, definition in by_file.get(site_file, []):
                limit = site_line or definition.line
                if definition.name == caller and best_line < definition.line <= limit:
                    best, best_line = key, definition.line
            return best or f"{site_file}::{caller}"

        graph: Dict[str, List[Tuple[int, str]]] = {}
        for call in calls:
            site = call.site
            if call.confidence == "BUILTIN":
                continue
            target = ""
            typed = types.resolve_method(site.file, site.line, site.receiver, site.callee) if site.receiver else None
            if typed is not None:
                target = at_line.get(typed, "")
            elif call.confidence in ("SAME_FILE", "IMPORTED", "UNIQUE") and call.target_qualified:
                verdict = types.accepts(
                    site.file, site.line, site.receiver, call.target_file, call.target_line, site.callee,
                )
                if verdict is None:
                    verdict = not site.receiver or site.receiver.split(".")[0] in ("self", "this", "cls", "super()") \
                        or site.receiver.split(".")[-1].strip("_").lower() == PurePosixPath(call.target_file).stem.strip("_").lower()
                if verdict:
                    target = at_line.get((call.target_file, call.target_line), call.target_qualified)
            if not target:
                continue
            source = caller_key(site.file, site.line, site.caller)
            if source == target and not site.receiver and site.caller != site.callee:
                continue
            graph.setdefault(source, []).append((site.line, target))
        for key in graph:
            seen: Set[str] = set()
            ordered: List[Tuple[int, str]] = []
            for line, callee in sorted(graph[key]):
                if callee not in seen:
                    seen.add(callee)
                    ordered.append((line, callee))
            graph[key] = ordered
        return graph, defs, calls

    def entry_points(
        self,
        nodes: List[Node],
        graph: Dict[str, List[Tuple[int, str]]],
        defs: Dict[str, SymbolDef],
        content_map: Optional[Dict[str, str]],
    ) -> List[EntryPoint]:
        """Score candidate entry points and return the strongest ones.

        Args:
            nodes: Scanned file nodes.
            graph: Ordered call graph from call_graph().
            defs: Definitions keyed by ``file::name``.
            content_map: File contents (enables ``__main__`` guard detection).

        Returns:
            Entry points sorted by score descending, capped by FLOW_MAX_ENTRYPOINTS.
        """
        contents = content_map or {}
        language = {n.node_id: n.language for n in nodes}
        called: Set[str] = {callee for items in graph.values() for _, callee in items}
        candidates: Dict[str, EntryPoint] = {}

        def bump(file_id: str, name: str, line: int, points: int, reason: str) -> None:
            """Add *points* and evidence to a candidate."""
            key = f"{file_id}::{name}" if name else f"{file_id}::<main>"
            entry = candidates.setdefault(key, EntryPoint(file_id, name, line, 0))
            entry.score += points
            if reason not in entry.reasons:
                entry.reasons.append(reason)

        for file_id, content in sorted(contents.items()):
            if self._is_test(file_id) or language.get(file_id) != "py":
                continue
            guard = _MAIN_GUARD_RE.search(content)
            if guard:
                line = content[: guard.start()].count("\n") + 1
                bump(file_id, "", line, 8, "`if __name__ == \"__main__\"` guard")
        for key, definition in sorted(defs.items()):
            file_id = definition.file
            if self._is_test(file_id) or definition.kind not in ("function", "method", "macro", "constructor"):
                continue
            stem = PurePosixPath(file_id).stem
            if definition.name in ("main", "Main") and language.get(file_id) in _HARD_MAIN_LANGUAGES:
                bump(file_id, definition.name, definition.line, 8, f"`{definition.name}` in a compiled-language file")
            if definition.name in _ENTRY_NAMES:
                bump(file_id, definition.name, definition.line, 3, f"entry-style name `{definition.name}`")
            if stem in _ENTRY_STEMS and definition.kind == "function":
                bump(file_id, definition.name, definition.line, 2, f"defined in entry file `{PurePosixPath(file_id).name}`")
            out = len(graph.get(key, []))
            if key not in called and out >= int(self._config.FLOW_SOURCE_MIN_CALLS):
                bump(file_id, definition.name, definition.line, 1, f"call-graph source with {out} calls")
        for entry in list(candidates.values()):
            if not entry.name:
                for _, callee in graph.get(entry.key, []):
                    target = candidates.get(callee)
                    if target is not None:
                        target.score += 4
                        target.reasons.append("called from the `__main__` guard")
        minimum = int(self._config.FLOW_MIN_ENTRY_SCORE)
        ranked = sorted(
            (e for e in candidates.values() if e.score >= minimum and (graph.get(e.key) or not e.name)),
            key=lambda e: (-e.score, e.file, e.line, e.name),
        )
        picked: List[EntryPoint] = []
        covered: Set[str] = set()
        for entry in ranked:
            if entry.key in covered:
                continue
            callees = {callee for _, callee in graph.get(entry.key, [])}
            if not entry.name and callees and callees <= {p.key for p in picked}:
                continue
            picked.append(entry)
            covered.update(callee for _, callee in graph.get(entry.key, []))
            if len(picked) >= int(self._config.FLOW_MAX_ENTRYPOINTS):
                break
        return picked

    def walk(self, graph: Dict[str, List[Tuple[int, str]]], start: str) -> List[FlowStep]:
        """Depth-first walk in call-site order, bounded by depth and steps.

        Args:
            graph: Ordered call graph.
            start: Entry key.

        Returns:
            Steps in execution order; repeated callees are not re-expanded.
        """
        max_depth = max(1, int(self._config.FLOW_MAX_DEPTH))
        budget = max(1, int(self._config.FLOW_MAX_STEPS))
        steps: List[FlowStep] = []
        expanded: Set[str] = {start}

        def visit(caller: str, depth: int, path: List[str]) -> None:
            """Emit the calls of *caller* recursively."""
            for line, callee in graph.get(caller, []):
                if len(steps) >= budget:
                    return
                recursive = callee in path
                repeat = callee in expanded and not recursive
                steps.append(FlowStep(caller, callee, line, depth, repeat, recursive))
                if recursive or repeat or depth >= max_depth:
                    continue
                expanded.add(callee)
                visit(callee, depth + 1, path + [callee])

        visit(start, 1, [start])
        return steps

    def _short(self, key: str) -> str:
        """Return ``file_stem.Owner.name`` for a call-graph key."""
        file_id, _, name = key.partition("::")
        name = name.split("@", 1)[0]
        stem = PurePosixPath(file_id).stem
        if not name or name == "<main>":
            return f"{stem} (__main__)"
        owner = self._owners.get(key, "")
        return f"{stem}.{owner}.{name}" if owner else f"{stem}.{name}"

    def call_tree_mermaid(self, entry: EntryPoint, steps: List[FlowStep]) -> str:
        """Render an execution call tree as ``flowchart LR``."""
        label_cap = int(self._config.FLOW_LABEL_CHARS)
        lines = [
            "flowchart LR",
            "    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;",
            "    classDef ext fill:#111827,stroke:#a78bfa,color:#ede9fe;",
            "    classDef fn fill:#111827,stroke:#38bdf8,color:#e5e7eb;",
        ]
        declared: Set[str] = set()

        def node(key: str, css: str) -> str:
            """Declare *key* once and return its Mermaid id."""
            nid = mermaid_id(key, "f")
            if nid not in declared:
                declared.add(nid)
                lines.append(f'    {nid}["{mermaid_text(self._short(key), label_cap)}"]:::{css}')
            return nid

        root = node(entry.key, "entry")
        root_file = entry.file
        links: List[str] = []
        back: List[int] = []
        for step in steps:
            src = root if step.caller == entry.key else node(step.caller, "fn")
            css = "fn" if step.callee.partition("::")[0] == root_file else "ext"
            dst = node(step.callee, css)
            if step.recursive:
                links.append(f'    {src} -.->|"recursion"| {dst}')
                back.append(len(links) - 1)
            elif step.repeat:
                links.append(f"    {src} -.-> {dst}")
            else:
                order = sum(1 for s in steps[: steps.index(step) + 1] if s.caller == step.caller and not s.repeat)
                links.append(f'    {src} -->|"{order}"| {dst}')
        lines.extend(links)
        if back:
            lines.append(f"    linkStyle {','.join(str(i) for i in back)} stroke:#f87171;")
        return "\n".join(lines)

    def sequence_mermaid(self, entry: EntryPoint, steps: List[FlowStep]) -> str:
        """Render the cross-file part of a walk as ``sequenceDiagram``."""
        cap = max(1, int(self._config.FLOW_SEQUENCE_MAX_MESSAGES))
        participants: List[str] = []
        messages: List[str] = []
        files = {entry.file}
        for step in steps:
            src_file = step.caller.partition("::")[0]
            dst_file = step.callee.partition("::")[0]
            if src_file == dst_file or step.repeat:
                continue
            for file_id in (src_file, dst_file):
                if file_id not in participants:
                    participants.append(file_id)
            files.update((src_file, dst_file))
            name = step.callee.partition("::")[2].split("@", 1)[0]
            messages.append(
                f"    {mermaid_id(src_file, 'p')}->>{mermaid_id(dst_file, 'p')}: {mermaid_text(name, int(self._config.FLOW_LABEL_CHARS))}()"
            )
            if len(messages) >= cap:
                break
        if not messages:
            return ""
        if entry.file in participants:
            participants.remove(entry.file)
        participants.insert(0, entry.file)
        lines = ["sequenceDiagram", "    autonumber"]
        for file_id in participants:
            lines.append(f"    participant {mermaid_id(file_id, 'p')} as {mermaid_text(PurePosixPath(file_id).name)}")
        lines.extend(messages)
        return "\n".join(lines)

    def control_flow_mermaid(self, content: str, entry: EntryPoint, project_names: Set[str]) -> str:
        """Render a Python entry function (or ``__main__`` block) as a flowchart.

        Decisions become diamonds with Yes/No branches, loops become
        hexagons with a back edge, ``try`` blocks expose their handlers,
        and ``return`` / ``raise`` end their branch. Straight-line runs
        collapse into one step naming the project calls they make.

        Args:
            content: Python source of the entry file.
            entry: The entry point.
            project_names: Callable names defined in the project.

        Returns:
            Mermaid ``flowchart TD`` source, or "" when not applicable.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                tree = ast.parse(content)
            except (SyntaxError, ValueError, RecursionError):
                return ""
        body: Optional[List[ast.stmt]] = None
        if entry.name:
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == entry.name and node.lineno == entry.line:
                    body = node.body
                    break
            if body is None:
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == entry.name:
                        body = node.body
                        break
        else:
            for stmt in tree.body:
                if isinstance(stmt, ast.If) and _MAIN_GUARD_RE.match(ast.unparse(stmt).split("\n")[0]):
                    body = stmt.body
                    break
        if not body:
            return ""
        return _ControlFlowRenderer(self._config, project_names).render(body, self._short(entry.key))


class _ControlFlowRenderer:
    """Turns a Python statement list into a Mermaid control-flow flowchart."""

    def __init__(self, config: Config, project_names: Set[str]) -> None:
        """Initialise with budgets and the set of project callable names."""
        self._cap = max(4, int(config.FLOW_CFG_MAX_NODES))
        self._switch_min = max(2, int(config.FLOW_SWITCH_MIN_CASES))
        self._label = int(config.FLOW_LABEL_CHARS)
        self._names = project_names
        self._lines: List[str] = []
        self._count = 0
        self._truncated = False

    def _new(self, shape: str, text: str, css: str = "") -> str:
        """Declare a node and return its id."""
        self._count += 1
        nid = f"s{self._count}"
        label = mermaid_text(text, self._label)
        open_, close = {
            "box": ("[", "]"), "dec": ("{", "}"), "loop": ("{{", "}}"),
            "end": ("([", "])"), "io": ("[/", "/]"),
        }[shape]
        self._lines.append(f'    {nid}{open_}"{label}"{close}' + (f":::{css}" if css else ""))
        return nid

    def _link(self, src: str, dst: str, label: str = "", dotted: bool = False) -> None:
        """Append one edge."""
        arrow = "-.->" if dotted else "-->"
        if label:
            self._lines.append(f'    {src} {arrow}|"{mermaid_text(label, self._label)}"| {dst}')
        else:
            self._lines.append(f"    {src} {arrow} {dst}")

    def _calls(self, node: ast.AST) -> List[str]:
        """Return project callable names called inside *node*, in order."""
        found: List[str] = []
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                name = ""
                if isinstance(child.func, ast.Name):
                    name = child.func.id
                elif isinstance(child.func, ast.Attribute):
                    name = child.func.attr
                if name and name in self._names and name not in found:
                    found.append(name)
        return found

    def render(self, body: List[ast.stmt], title: str) -> str:
        """Render *body* and return the Mermaid source."""
        self._lines = [
            "flowchart TD",
            "    classDef term fill:#0e7490,stroke:#22d3ee,color:#ecfeff;",
            "    classDef dec fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;",
            "    classDef stop fill:#3f1d1d,stroke:#f87171,color:#fee2e2;",
        ]
        start = self._new("end", f"start {title}", "term")
        tails = self._block(body, [(start, "")])
        if tails:
            finish = self._new("end", "end", "term")
            for tail, label in tails:
                self._link(tail, finish, label)
        if self._truncated:
            self._lines.append(f'    trunc["... truncated at FLOW_CFG_MAX_NODES={self._cap}"]')
            self._lines.append(f"    {start} -.- trunc")
        return "\n".join(self._lines)

    def _connect(self, tails: List[Tuple[str, str]], target: str) -> None:
        """Link every pending tail to *target*."""
        for tail, label in tails:
            self._link(tail, target, label)

    def _block(self, body: List[ast.stmt], tails: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Render a statement list; return the open tails after it."""
        pending: List[str] = []

        def flush() -> None:
            """Emit collapsed straight-line statements as one step."""
            nonlocal tails
            if not pending:
                return
            text = "; ".join(pending)
            nid = self._new("box", text)
            self._connect(tails, nid)
            tails = [(nid, "")]
            pending.clear()

        for stmt in body:
            if self._count >= self._cap:
                self._truncated = True
                break
            if isinstance(stmt, (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.With, ast.AsyncWith)) or (
                hasattr(ast, "Match") and isinstance(stmt, getattr(ast, "Match"))
            ):
                flush()
                tails = self._compound(stmt, tails)
                continue
            if isinstance(stmt, (ast.Return, ast.Raise)):
                flush()
                kind = "return" if isinstance(stmt, ast.Return) else "raise"
                calls = self._calls(stmt)
                text = kind + (f" {', '.join(calls)}()" if calls else (f" {ast.unparse(stmt.exc).split('(')[0]}" if isinstance(stmt, ast.Raise) and stmt.exc is not None else ""))
                nid = self._new("end", text, "stop" if kind == "raise" else "term")
                self._connect(tails, nid)
                return []
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom, ast.Pass)):
                continue
            calls = self._calls(stmt)
            if calls:
                pending.append(", ".join(f"{c}()" for c in calls))
            elif isinstance(stmt, (ast.Break, ast.Continue)):
                flush()
                nid = self._new("box", "break" if isinstance(stmt, ast.Break) else "continue")
                self._connect(tails, nid)
                return []
        flush()
        return tails

    @staticmethod
    def _case_of(test: ast.expr) -> Optional[Tuple[str, str, str]]:
        """Split ``subject == literal [and guard]`` into (subject, case label, guard)."""
        guard = ""
        compare = test
        if isinstance(test, ast.BoolOp) and isinstance(test.op, ast.And) and test.values:
            compare = test.values[0]
            guard = " and ".join(ast.unparse(v) for v in test.values[1:])
        if not isinstance(compare, ast.Compare) or len(compare.ops) != 1:
            return None
        if not isinstance(compare.ops[0], (ast.Eq, ast.In, ast.Is)):
            return None
        right = compare.comparators[0]
        if isinstance(right, ast.Constant):
            label = repr(right.value)
        elif isinstance(right, (ast.Tuple, ast.List, ast.Set)) and all(isinstance(e, ast.Constant) for e in right.elts):
            label = " / ".join(repr(e.value) for e in right.elts)
        else:
            return None
        return ast.unparse(compare.left), label, guard

    def _switch_chain(self, stmt: ast.If) -> Optional[Tuple[str, List[Tuple[str, List[ast.stmt]]], List[ast.stmt]]]:
        """Detect an if/elif chain that dispatches on one subject (a switch)."""
        cases: List[Tuple[str, List[ast.stmt]]] = []
        subject = ""
        current: Optional[ast.stmt] = stmt
        default: List[ast.stmt] = []
        while isinstance(current, ast.If):
            parsed = self._case_of(current.test)
            if parsed is None or (subject and parsed[0] != subject):
                if len(cases) < self._switch_min:
                    return None
                default = [current]
                break
            subject = parsed[0]
            label = parsed[1] + (f" if {parsed[2]}" if parsed[2] else "")
            cases.append((label, current.body))
            if len(current.orelse) == 1 and isinstance(current.orelse[0], ast.If):
                current = current.orelse[0]
            else:
                default = list(current.orelse)
                current = None
        if len(cases) < self._switch_min:
            return None
        return subject, cases, default

    def _switch(
        self, subject: str, cases: List[Tuple[str, List[ast.stmt]]],
        default: List[ast.stmt], tails: List[Tuple[str, str]],
    ) -> List[Tuple[str, str]]:
        """Render a dispatch chain as one decision with a labelled branch per case."""
        decision = self._new("dec", f"switch {subject}", "dec")
        self._connect(tails, decision)
        out: List[Tuple[str, str]] = []
        for label, body in cases:
            if self._count >= self._cap:
                self._truncated = True
                break
            out += self._block(body, [(decision, label)])
        if default:
            out += self._block(default, [(decision, "otherwise")])
        else:
            out.append((decision, "otherwise"))
        return out

    def _condition(self, test: ast.expr) -> str:
        """Return a short condition label."""
        return ast.unparse(test)

    def _compound(self, stmt: ast.stmt, tails: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Render one compound statement; return its exit tails."""
        if isinstance(stmt, ast.If):
            switch = self._switch_chain(stmt)
            if switch is not None:
                return self._switch(switch[0], switch[1], switch[2], tails)
            decision = self._new("dec", self._condition(stmt.test) + "?", "dec")
            self._connect(tails, decision)
            yes = self._block(stmt.body, [(decision, "yes")])
            if stmt.orelse:
                no = self._block(stmt.orelse, [(decision, "no")])
            else:
                no = [(decision, "no")]
            return yes + no
        if isinstance(stmt, (ast.For, ast.AsyncFor, ast.While)):
            if isinstance(stmt, ast.While):
                text = f"while {self._condition(stmt.test)}"
            else:
                text = f"for {ast.unparse(stmt.target)} in {ast.unparse(stmt.iter)}"
            loop = self._new("loop", text, "dec")
            self._connect(tails, loop)
            inner = self._block(stmt.body, [(loop, "each")])
            for tail, label in inner:
                self._link(tail, loop, label or "next", dotted=True)
            after: List[Tuple[str, str]] = [(loop, "done")]
            if stmt.orelse:
                after = self._block(stmt.orelse, after)
            return after
        if isinstance(stmt, ast.Try):
            guard = self._new("box", "try")
            self._connect(tails, guard)
            out = self._block(stmt.body, [(guard, "")])
            for handler in stmt.handlers:
                name = ast.unparse(handler.type) if handler.type is not None else "any error"
                out += self._block(handler.body, [(guard, f"except {name}")])
            if stmt.orelse:
                out = self._block(stmt.orelse, out)
            if stmt.finalbody:
                out = self._block(stmt.finalbody, out)
            return out
        if isinstance(stmt, (ast.With, ast.AsyncWith)):
            text = "with " + ", ".join(ast.unparse(item.context_expr) for item in stmt.items)
            ctx = self._new("io", text)
            self._connect(tails, ctx)
            return self._block(stmt.body, [(ctx, "")])
        match_type = getattr(ast, "Match", None)
        if match_type is not None and isinstance(stmt, match_type):
            decision = self._new("dec", f"match {ast.unparse(stmt.subject)}", "dec")
            self._connect(tails, decision)
            out: List[Tuple[str, str]] = []
            for case in stmt.cases:
                out += self._block(case.body, [(decision, ast.unparse(case.pattern))])
            return out
        return tails


def render_architecture_section(
    config: Config,
    nodes: List[Node],
    resolved_edges: Optional[List[Edge]],
    analysis: Optional[AnalysisResult],
    layers: Optional[Dict[str, str]],
) -> List[str]:
    """Return Markdown lines for the Architecture Overview section."""
    source, stats = ArchitectureDiagramBuilder(config).render(nodes, resolved_edges, analysis, layers)
    if not source:
        return []
    upward = stats["upward"]
    lines = [
        "## Architecture Overview",
        "",
        f"{stats['components']} components stacked in {stats['tiers']} dependency tiers "
        "(weighted Eades-Lin-Smyth ordering: arrows point from dependent to dependency, top to bottom). "
        f"Labels are import counts, thick arrows the top quartile; {stats['reduced']} transitively implied "
        "edges are omitted. Dashed red arrows are upward dependencies: the smallest set of imports that "
        "closes every cycle and breaks the layering. Cyan components hold entry points.",
        "",
    ]
    if upward:
        lines.append("Upward dependencies to fix first: " + "; ".join(
            f"`{src}` -> `{dst}` ({count} imports)" for src, dst, count in sorted(upward, key=lambda item: -item[2])
        ))
        lines.append("")
    lines.extend(["```mermaid", source, "```", "", "---", ""])
    return lines


def render_flows_section(
    config: Config,
    nodes: List[Node],
    edges: List[Edge],
    resolved_edges: Optional[List[Edge]],
    content_map: Optional[Dict[str, str]],
) -> List[str]:
    """Return Markdown lines for the Execution Flows section."""
    builder = ExecutionFlowBuilder(config)
    graph, defs, _ = builder.call_graph(nodes, edges, resolved_edges, content_map)
    entries = builder.entry_points(nodes, graph, defs, content_map)
    if not entries:
        return []
    names = {d.name for d in defs.values()}
    lines = [
        "## Execution Flows",
        "",
        "Entry points are scored from `__main__` guards, `main` functions, entry-style names and files, "
        "and call-graph sources. Each flow walks resolved calls in call-site order "
        f"(depth <= {config.FLOW_MAX_DEPTH}, <= {config.FLOW_MAX_STEPS} steps); numbers give the call order, "
        "dotted arrows revisit an already expanded callee, red arrows are recursion.",
        "",
    ]
    language = {n.node_id: n.language for n in nodes}
    for entry in entries:
        steps = builder.walk(graph, entry.key)
        title = builder._short(entry.key)
        lines.extend([
            f"### `{title}`",
            "",
            f"`{entry.file}:{entry.line}`, score {entry.score}: " + "; ".join(entry.reasons) + ".",
            "",
        ])
        content = (content_map or {}).get(entry.file)
        if content and language.get(entry.file) == "py":
            cfg_source = builder.control_flow_mermaid(content, entry, names)
            if cfg_source and cfg_source.count("\n") > 5:
                lines.extend(["Control flow:", "", "```mermaid", cfg_source, "```", ""])
        if steps:
            lines.extend(["Call tree:", "", "```mermaid", builder.call_tree_mermaid(entry, steps), "```", ""])
        sequence = builder.sequence_mermaid(entry, steps)
        if sequence:
            lines.extend(["Cross-file sequence:", "", "```mermaid", sequence, "```", ""])
    lines.extend(["---", ""])
    return lines
