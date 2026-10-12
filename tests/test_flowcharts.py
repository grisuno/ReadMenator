"""Contract tests for architecture tiers, execution flows, and receiver typing."""

from __future__ import annotations

import unittest
from dataclasses import replace

from readmenator._config import Config
from readmenator._documentation import DocumentationGenerator
import json
import re

from readmenator._flowcharts import (
    build_flow_graphs,
    ArchitectureDiagramBuilder,
    EntryPoint,
    ExecutionFlowBuilder,
    eades_lin_smyth,
    mermaid_text,
    render_architecture_section,
    render_flows_section,
    tarjan_scc,
    transitive_reduction,
)
from readmenator._flowlayout import FlowEdge, FlowGraph, FlowNode, LayoutMetrics, layout_flow
from readmenator._flowpage import flow_thumbnail_svg, render_flows_page
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node, Symbol
from readmenator._pytypes import PythonReceiverTypes

APP_SOURCE = '''"""App entry."""
from pkg.engine import Engine


class App:
    """Application."""

    def __init__(self) -> None:
        self.engine = Engine()

    def run(self, mode: str) -> int:
        """Run the app."""
        if mode == "fast":
            self.engine.start()
        elif mode == "slow":
            self.engine.start()
            self.engine.stop()
        elif mode in ("idle", "noop"):
            return 0
        else:
            raise ValueError(mode)
        for item in range(3):
            self.engine.tick(item)
        try:
            self.engine.stop()
        except RuntimeError:
            return 1
        return 0


def main() -> int:
    """CLI entry."""
    app = App()
    return app.run("fast")


if __name__ == "__main__":
    main()
'''

ENGINE_SOURCE = '''class Engine:
    """Engine."""

    def start(self) -> None:
        """Start."""
        self.tick(0)

    def stop(self) -> None:
        """Stop."""

    def tick(self, n: int) -> None:
        """Tick."""
        if n > 3:
            self.tick(n - 1)


class Other:
    """Has a same-named method."""

    def start(self) -> None:
        """Different start."""
'''


def _project() -> tuple:
    """Two-file Python project with typed receivers and a __main__ guard."""
    contents = {"pkg/app.py": APP_SOURCE, "pkg/engine.py": ENGINE_SOURCE}
    nodes = [
        Node("pkg/app.py", "app.py", "module", "py", "App entry.", [
            Symbol("App", "class", 5), Symbol("__init__", "method", 8),
            Symbol("run", "method", 11), Symbol("main", "function", 31),
        ]),
        Node("pkg/engine.py", "engine.py", "module", "py", "", [
            Symbol("Engine", "class", 1), Symbol("start", "method", 4),
            Symbol("stop", "method", 8), Symbol("tick", "method", 11),
            Symbol("Other", "class", 17), Symbol("start", "method", 20),
        ]),
    ]
    edges = [Edge("pkg/app.py", "pkg.engine", "imports")]
    resolved = [Edge("pkg/app.py", "pkg/engine.py", "resolved_imports")]
    return nodes, edges, resolved, contents


class TestGraphAlgorithms(unittest.TestCase):
    """Contract: SCC, transitive reduction, and feedback-arc ordering."""

    def test_flowcharts_tarjan_finds_cycles(self) -> None:
        adjacency = {"a": {"b"}, "b": {"c"}, "c": {"a"}, "d": {"a"}}
        self.assertEqual(tarjan_scc(list(adjacency), adjacency), [["a", "b", "c"], ["d"]])

    def test_flowcharts_transitive_reduction_drops_implied(self) -> None:
        reduced = transitive_reduction({"a": {"b", "c"}, "b": {"c"}, "c": set()})
        self.assertEqual(reduced, {"a": {"b"}, "b": {"c"}, "c": set()})

    def test_flowcharts_eades_lin_smyth_orders_by_weight(self) -> None:
        weights = {("ui", "core"): 9, ("core", "db"): 7, ("db", "core"): 1, ("ui", "db"): 2}
        order = eades_lin_smyth(["core", "db", "ui"], weights)
        self.assertEqual(order, ["ui", "core", "db"])

    def test_flowcharts_eades_lin_smyth_deterministic(self) -> None:
        weights = {("a", "b"): 1, ("b", "a"): 1}
        self.assertEqual(eades_lin_smyth(["b", "a"], weights), eades_lin_smyth(["a", "b"], weights))

    def test_flowcharts_mermaid_text_escapes(self) -> None:
        self.assertEqual(mermaid_text('a#b;"c"<d>'), "a#35;b#59;#quot;c#quot;#lt;d#gt;")
        self.assertEqual(mermaid_text("abcdefghij", 6), "abc...")


class TestArchitectureDiagram(unittest.TestCase):
    """Contract: tiers, upward dependencies, reduction, and entry highlighting."""

    def _fixture(self) -> tuple:
        """Three communities with one upward dependency and one implied edge."""
        names = ["ui/cli.py", "ui/view.py", "core/svc.py", "core/rules.py", "db/store.py", "db/orm.py"]
        nodes = [Node(n, n.split("/")[-1], "module", "py", "", [Symbol("f", "function", 1)]) for n in names]
        analysis = AnalysisResult(
            god_nodes=[], communities=[
                CommunityResult(0, "ui", {"ui/cli.py", "ui/view.py"}, 1.0, 2),
                CommunityResult(1, "core", {"core/svc.py", "core/rules.py"}, 1.0, 2),
                CommunityResult(2, "db", {"db/store.py", "db/orm.py"}, 1.0, 2),
            ],
            surprising_connections=[], suggested_questions=[], node_count=6, edge_count=0,
        )
        pairs = [("ui/cli.py", "core/svc.py")] * 1 + [("ui/view.py", "core/rules.py"), ("core/svc.py", "db/store.py"),
                                                     ("core/rules.py", "db/orm.py"), ("ui/cli.py", "db/store.py"),
                                                     ("db/orm.py", "core/rules.py")]
        resolved = [Edge(s, t, "resolved_imports") for s, t in pairs]
        return nodes, resolved, analysis

    def test_flowcharts_architecture_tiers_and_upward(self) -> None:
        nodes, resolved, analysis = self._fixture()
        source, stats = ArchitectureDiagramBuilder(Config()).render(nodes, resolved, analysis, {})
        self.assertEqual(stats["tiers"], 3)
        self.assertEqual(stats["upward"], [("db", "core", 1)])
        self.assertEqual(stats["reduced"], 1)
        self.assertEqual(stats["cycles"], [["core", "db"]])
        self.assertIn('n_c1 <-.-|"1 upward"| n_c2', source)
        self.assertIn('subgraph lane_0["Tier 1 - entry / orchestration"]', source)
        self.assertIn(":::entry", source)
        self.assertIn("n_c0 ~~~ n_c1", source)

    def test_flowcharts_architecture_skips_tests_and_vendor(self) -> None:
        nodes = [
            Node("src/a.py", "a.py", "module", "py", "", []),
            Node("tests/test_a.py", "test_a.py", "module", "py", "", []),
            Node("src/vendor/lib.py", "lib.py", "module", "py", "", []),
        ]
        comps = ArchitectureDiagramBuilder(Config()).components(nodes, None, {"tests/test_a.py": "testing"})
        files = [f for c in comps for f in c.files]
        self.assertEqual(files, ["src/a.py"])

    def test_flowcharts_architecture_section_markdown(self) -> None:
        nodes, resolved, analysis = self._fixture()
        lines = render_architecture_section(Config(), nodes, resolved, analysis, {})
        text = "\n".join(lines)
        self.assertIn("## Architecture Overview", text)
        self.assertIn("Upward dependencies to fix first: `db` -> `core` (1 imports)", text)
        self.assertEqual(render_architecture_section(Config(), [], [], None, {}), [])


class TestExecutionFlows(unittest.TestCase):
    """Contract: entry points, ordered walks, control flow, and sequences."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.nodes, cls.edges, cls.resolved, cls.contents = _project()
        cls.builder = ExecutionFlowBuilder(Config())
        cls.graph, cls.defs, _ = cls.builder.call_graph(cls.nodes, cls.edges, cls.resolved, cls.contents)

    def test_flowcharts_typed_receivers_route_calls(self) -> None:
        run_calls = [callee for _, callee in self.graph["pkg/app.py::run"]]
        self.assertEqual(run_calls, ["pkg/engine.py::start", "pkg/engine.py::stop", "pkg/engine.py::tick"])
        self.assertEqual([c for _, c in self.graph["pkg/app.py::main"]], ["pkg/app.py::App", "pkg/app.py::run"])

    def test_flowcharts_entry_points_scored(self) -> None:
        entries = self.builder.entry_points(self.nodes, self.graph, self.defs, self.contents)
        self.assertEqual(entries[0].key, "pkg/app.py::main")
        self.assertIn("called from the `__main__` guard", entries[0].reasons)
        self.assertNotIn("pkg/app.py::<main>", [e.key for e in entries])

    def test_flowcharts_walk_order_and_recursion(self) -> None:
        steps = self.builder.walk(self.graph, "pkg/app.py::main")
        self.assertEqual([s.callee for s in steps[:2]], ["pkg/app.py::App", "pkg/app.py::run"])
        recursive = [s for s in steps if s.recursive]
        self.assertTrue(recursive and recursive[0].callee == "pkg/engine.py::tick")
        cfg = replace(Config(), FLOW_MAX_STEPS=2)
        self.assertEqual(len(ExecutionFlowBuilder(cfg).walk(self.graph, "pkg/app.py::main")), 2)

    def test_flowcharts_call_tree_mermaid(self) -> None:
        entries = self.builder.entry_points(self.nodes, self.graph, self.defs, self.contents)
        steps = self.builder.walk(self.graph, entries[0].key)
        source = self.builder.call_tree_mermaid(entries[0], steps)
        self.assertTrue(source.startswith("flowchart LR"))
        self.assertIn('"app.App.run<br/>', source)
        self.assertIn('"engine.Engine.tick<br/>', source)
        self.assertIn('|"recursion"|', source)

    def test_flowcharts_control_flow_switch_loop_try(self) -> None:
        entries = self.builder.entry_points(self.nodes, self.graph, self.defs, self.contents)
        names = {d.name for d in self.defs.values()}
        run_entry = type(entries[0])("pkg/app.py", "run", 11, 0)
        source = self.builder.control_flow_mermaid(APP_SOURCE, run_entry, names)
        self.assertIn('{"mode == \'fast\'?"}', source)
        self.assertIn('n_s2 -->|"no"| n_s4', source)
        self.assertIn("mode in 'idle' / 'noop'?", source)
        self.assertIn('{{"for item in range(3)"}}', source)
        self.assertIn("except RuntimeError", source)
        self.assertIn('(["raise ValueError"])', source)

    def test_flowcharts_sequence_crosses_files(self) -> None:
        entries = self.builder.entry_points(self.nodes, self.graph, self.defs, self.contents)
        steps = self.builder.walk(self.graph, entries[0].key)
        source = self.builder.sequence_mermaid(entries[0], steps)
        self.assertTrue(source.startswith("sequenceDiagram"))
        self.assertIn("participant p_pkg_app_py as app.py", source)
        self.assertIn("p_pkg_app_py->>p_pkg_engine_py: Engine.start()", source)

    def test_flowcharts_section_and_kb_integration(self) -> None:
        text = "\n".join(render_flows_section(Config(), self.nodes, self.edges, self.resolved, self.contents))
        self.assertIn("## Execution Flows", text)
        self.assertIn("### `app.main`", text)
        kb = DocumentationGenerator(Config()).generate(
            self.nodes, self.edges, self.resolved, None, {}, [], None, None, content_map=self.contents,
        )
        self.assertIn("[Execution Flows](#execution-flows)", kb)
        self.assertIn("## Execution Flows", kb)
        disabled = DocumentationGenerator(replace(Config(), FLOW_ENABLED=False)).generate(
            self.nodes, self.edges, self.resolved, None, {}, [], None, None, content_map=self.contents,
        )
        self.assertNotIn("## Execution Flows", disabled)


class TestPythonReceiverTypes(unittest.TestCase):
    """Contract: receiver typing from constructors, annotations, and self attributes."""

    def setUp(self) -> None:
        _, _, _, contents = _project()
        self.types = PythonReceiverTypes(contents, {k: "py" for k in contents})

    def test_pytypes_receiver_classes(self) -> None:
        self.assertEqual(self.types.receiver_class("pkg/app.py", 33, "app"), "App")
        self.assertEqual(self.types.receiver_class("pkg/app.py", 14, "self.engine"), "Engine")
        self.assertEqual(self.types.receiver_class("pkg/app.py", 14, "self"), "App")
        self.assertEqual(self.types.receiver_class("pkg/app.py", 14, "unknown"), "")

    def test_pytypes_resolve_method_picks_typed_owner(self) -> None:
        self.assertEqual(self.types.resolve_method("pkg/app.py", 14, "self.engine", "start"), ("pkg/engine.py", 4))
        self.assertIsNone(self.types.resolve_method("pkg/app.py", 14, "mystery", "start"))

    def test_pytypes_accepts_rejects_unproven(self) -> None:
        self.assertFalse(self.types.accepts("pkg/app.py", 14, "mystery", "pkg/engine.py", 20, "start"))
        self.assertTrue(self.types.accepts("pkg/app.py", 14, "", "pkg/engine.py", 20, "start"))
        self.assertIsNone(self.types.accepts("lib/x.js", 1, "obj", "pkg/engine.py", 20, "start"))


if __name__ == "__main__":
    unittest.main()


class TestFlowLayoutAndViewer(unittest.TestCase):
    """Contract: laid-out diagrams are well proportioned and the viewer is self-contained."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.nodes, cls.edges, cls.resolved, cls.contents = _project()
        cls.graphs = build_flow_graphs(Config(), cls.nodes, cls.edges, cls.resolved, cls.contents, None, {})

    def test_flowlayout_kinds_present(self) -> None:
        kinds = [g.kind for g in self.graphs]
        self.assertEqual(kinds[0], "architecture")
        for kind in ("calltree", "sequence"):
            self.assertIn(kind, kinds)

    def test_flowlayout_never_a_strip(self) -> None:
        wide = FlowGraph(id="w", title="w", kind="calltree")
        wide.nodes.append(FlowNode(id="root", title="root"))
        for i in range(40):
            wide.nodes.append(FlowNode(id=f"c{i}", title=f"child_function_{i}", lines=["does something useful"]))
            wide.edges.append(FlowEdge("root", f"c{i}"))
        layout_flow(wide, LayoutMetrics(max_per_row=5), "TB")
        self.assertLess(wide.width / wide.height, 3.0)
        boxes = [(n.x - n.w / 2, n.x + n.w / 2, n.y - n.h / 2, n.y + n.h / 2) for n in wide.nodes]
        for i, a in enumerate(boxes):
            for b in boxes[i + 1:]:
                overlap = a[0] < b[1] and b[0] < a[1] and a[2] < b[3] and b[2] < a[3]
                self.assertFalse(overlap)

    def test_flowlayout_ladder_is_narrow(self) -> None:
        source = "def run(c):\n" + "".join(
            f"    {'if' if i == 0 else 'elif'} c == 'k{i}':\n        return f{i}()\n" for i in range(20)
        )
        names = {f"f{i}" for i in range(20)}
        graph = ExecutionFlowBuilder(Config()).control_flow_model(source, EntryPoint("x.py", "run", 1, 0), names)
        layout_flow(graph, LayoutMetrics(), "TB")
        self.assertGreater(graph.height, 2 * graph.width)
        decisions = [n for n in graph.nodes if n.shape == "decision"]
        self.assertEqual(len({round(n.x) for n in decisions}), 1)

    def test_flowlayout_edges_have_geometry(self) -> None:
        for graph in self.graphs:
            if graph.kind == "sequence":
                self.assertTrue(all("y" in m for m in graph.messages))
                continue
            self.assertTrue(all(len(e.points) == 4 for e in graph.edges))
            self.assertGreater(graph.width, 0)

    def test_flowpage_self_contained_and_escaped(self) -> None:
        page = render_flows_page(self.graphs, "<Demo & co>", "index.html")
        self.assertIn("&lt;Demo &amp; co&gt;", page)
        payload = re.search(r'<script type="application/json" id="fv-data">(.*?)</script>', page, re.S).group(1)
        self.assertNotIn("<", payload)
        self.assertTrue(json.loads(payload)["graphs"])
        self.assertNotRegex(page, r'<script[^>]+src=|<link[^>]+href=|https://|fetch\(')
        self.assertIn("window.ReadmenatorFlows", page)

    def test_flowpage_thumbnail(self) -> None:
        thumb = flow_thumbnail_svg(self.graphs[0], 320, 180)
        self.assertTrue(thumb.startswith('<svg class="thumb"'))
        self.assertEqual(flow_thumbnail_svg(FlowGraph(id="e", title="", kind="x"), 320, 180), "")

    def test_flowpage_api_site_embeds_flows(self) -> None:
        from readmenator._apidocs import ApiReferenceBuilder
        from readmenator._apidocs_page import render_api_site
        ref = ApiReferenceBuilder(Config()).build(self.nodes, self.edges, self.resolved, self.contents)
        site = render_api_site(ref, "Demo", Config(), self.graphs)
        self.assertIn('href="#/flows"', site)
        self.assertIn("ReadmenatorFlows.mount", site)
        self.assertNotIn("render-mermaid", site)
        self.assertNotRegex(site, r'<script[^>]+src=')

