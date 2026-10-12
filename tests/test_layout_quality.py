"""Contract tests for bundle crossing reduction and seeded explorer layouts."""

from __future__ import annotations

import math
import random
import unittest
from dataclasses import replace

from readmenator._bundlegraph import BundleGraphRenderer
from readmenator._config import Config
from readmenator._forcegraph import ForceGraphRenderer
from readmenator._forcegraph_page import FORCEGRAPH_PAGE_TEMPLATE as FORCE_TEMPLATE
from readmenator._graphlayout import (
    bundle_angular_cost,
    optimize_bundle_order,
    refine_sphere_leaves,
    spherical_edge_bundling,
)
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node, Symbol


def _clustered() -> tuple:
    """Six groups whose edges chain g0-g3-g5-g1-g4-g2 plus noise."""
    rng = random.Random(3)
    groups = {f"g{i}": [f"g{i}m{j}" for j in range(8)] for i in range(6)}
    members = [m for ms in groups.values() for m in ms]
    edges = []
    for a, b in [(0, 3), (3, 5), (5, 1), (1, 4), (4, 2)]:
        for _ in range(10):
            edges.append((f"g{a}m{rng.randrange(8)}", f"g{b}m{rng.randrange(8)}"))
    for _ in range(15):
        edges.append((rng.choice(members), rng.choice(members)))
    return groups, edges


def _chords(layout, edges) -> float:
    """Total straight-line edge length on the sphere."""
    return sum(math.dist(layout.leaves[a], layout.leaves[b]) for a, b in edges if a != b)


class TestBundleOrdering(unittest.TestCase):
    """Contract: ordering shortens bundles, keeps membership, and is deterministic."""

    def test_layout_order_reduces_angular_cost(self) -> None:
        groups, edges = _clustered()
        optimized = optimize_bundle_order(groups, edges)
        self.assertLess(bundle_angular_cost(optimized, edges), 0.7 * bundle_angular_cost(groups, edges))

    def test_layout_order_keeps_members_and_first_group(self) -> None:
        groups, edges = _clustered()
        optimized = optimize_bundle_order(groups, edges)
        self.assertEqual(list(optimized)[0], "g0")
        self.assertEqual({g: sorted(ms) for g, ms in optimized.items()}, {g: sorted(ms) for g, ms in groups.items()})

    def test_layout_order_deterministic_and_never_worse(self) -> None:
        groups, edges = _clustered()
        self.assertEqual(optimize_bundle_order(groups, edges), optimize_bundle_order(groups, edges))
        lone = {"a": ["a1", "a2"], "b": ["b1"]}
        self.assertLessEqual(bundle_angular_cost(optimize_bundle_order(lone, []), []), 0.0)
        self.assertEqual(optimize_bundle_order({}, []), {})

    def test_layout_more_sweeps_never_increase_cost(self) -> None:
        for seed in range(12):
            rng = random.Random(seed)
            groups = {f"g{i}": [f"g{i}m{j}" for j in range(rng.randint(2, 9))] for i in range(rng.randint(2, 6))}
            members = [m for ms in groups.values() for m in ms]
            edges = [(rng.choice(members), rng.choice(members)) for _ in range(rng.randint(5, 60))]
            baseline = bundle_angular_cost(groups, edges)
            previous = bundle_angular_cost(optimize_bundle_order(groups, edges, sweeps=0), edges)
            self.assertLessEqual(previous, baseline + 1e-9)
            for sweeps in range(1, 6):
                current = bundle_angular_cost(optimize_bundle_order(groups, edges, sweeps=sweeps), edges)
                self.assertLessEqual(current, previous + 1e-9, f"seed {seed} sweeps {sweeps}")
                previous = current

    def test_layout_center_out_puts_hub_mid_arc(self) -> None:
        groups = {"g": ["hub", "b", "c", "d", "e"]}
        optimized = optimize_bundle_order(groups, [], sweeps=0)
        self.assertEqual(optimized["g"].index("hub"), 2)

    def test_layout_sphere_refinement_shortens_chords(self) -> None:
        groups, edges = _clustered()
        base = spherical_edge_bundling(groups, [], 1.0)
        refined = refine_sphere_leaves(base, groups, edges)
        self.assertLess(_chords(refined, edges), _chords(base, edges))
        for label, members in groups.items():
            self.assertEqual(
                sorted(refined.leaves[m] for m in members), sorted(base.leaves[m] for m in members),
            )

    def test_layout_sphere_refine_in_bundling_call(self) -> None:
        groups, edges = _clustered()
        plain = spherical_edge_bundling(groups, edges, 1.0)
        refined = spherical_edge_bundling(groups, edges, 1.0, refine_sweeps=4)
        self.assertLess(_chords(refined, edges), _chords(plain, edges))
        self.assertEqual(len(refined.curves), len(plain.curves))


def _force_payload_inputs() -> tuple:
    """Small two-community project for payload tests."""
    nodes = [Node(f"pkg/{c}{i}.py", f"{c}{i}.py", "module", "py", "", [Symbol("f", "function", 1)])
             for c in "ab" for i in range(4)]
    resolved = [Edge(f"pkg/{c}{i}.py", f"pkg/{c}{(i + 1) % 4}.py", "resolved_imports") for c in "ab" for i in range(4)]
    resolved.append(Edge("pkg/a0.py", "pkg/b0.py", "resolved_imports"))
    analysis = AnalysisResult(
        god_nodes=[], communities=[
            CommunityResult(0, "a", {f"pkg/a{i}.py" for i in range(4)}, 1.0, 4),
            CommunityResult(1, "b", {f"pkg/b{i}.py" for i in range(4)}, 1.0, 4),
        ],
        surprising_connections=[], suggested_questions=[], node_count=8, edge_count=9,
    )
    return nodes, resolved, analysis


class TestSeededExplorer(unittest.TestCase):
    """Contract: the explorer payload carries deterministic FA2 start positions."""

    def test_layout_seed_positions_present_and_scaled(self) -> None:
        nodes, resolved, analysis = _force_payload_inputs()
        cfg = Config()
        payload = ForceGraphRenderer(cfg).build_payload(nodes, [], resolved, analysis, {}, [])
        files = [n for n in payload["nodes"] if n["type"] == "file"]
        self.assertTrue(all(len(n["s2"]) == 2 and len(n["s3"]) == 3 for n in files))
        by_id = {n["id"]: n for n in payload["nodes"]}
        lengths = sorted(
            math.dist(by_id[e["source"]]["s2"], by_id[e["target"]]["s2"])
            for e in payload["edges"] if e["source"] in by_id and e["target"] in by_id
        )
        self.assertAlmostEqual(lengths[len(lengths) // 2], cfg.FORCEGRAPH_LINK_DISTANCE, delta=1.0)

    def test_layout_seed_deterministic_and_disableable(self) -> None:
        nodes, resolved, analysis = _force_payload_inputs()
        first = ForceGraphRenderer(Config()).build_payload(nodes, [], resolved, analysis, {}, [])
        second = ForceGraphRenderer(Config()).build_payload(nodes, [], resolved, analysis, {}, [])
        self.assertEqual([n.get("s2") for n in first["nodes"]], [n.get("s2") for n in second["nodes"]])
        off = ForceGraphRenderer(replace(Config(), FORCEGRAPH_SEED_LAYOUT=False)).build_payload(
            nodes, [], resolved, analysis, {}, [],
        )
        self.assertFalse(any("s2" in n for n in off["nodes"]))

    def test_layout_seed_page_wiring(self) -> None:
        self.assertIn("function seedPositions()", FORCE_TEMPLATE)
        self.assertIn("d3VelocityDecay(SETTINGS.seedVelocityDecay)", FORCE_TEMPLATE)
        nodes, resolved, analysis = _force_payload_inputs()
        renderer = ForceGraphRenderer(Config())
        payload = renderer.build_payload(nodes, [], resolved, analysis, {}, [])
        self.assertTrue(renderer.page_settings(payload)["seedLayout"])

    def test_layout_bundle_payload_uses_optimized_order(self) -> None:
        nodes, resolved, analysis = _force_payload_inputs()
        force = ForceGraphRenderer(Config()).build_payload(nodes, [], resolved, analysis, {}, [])
        on = BundleGraphRenderer(Config()).build_payload(force)
        off = BundleGraphRenderer(replace(Config(), BUNDLEGRAPH_ORDER_OPTIMIZE=False)).build_payload(force)
        self.assertEqual(sorted(n["id"] for n in on["nodes"]), sorted(n["id"] for n in off["nodes"]))
        self.assertEqual(len(on["edges"]), len(off["edges"]))
        self.assertTrue(BundleGraphRenderer(Config()).thumbnail_svg(force).startswith("<svg"))


if __name__ == "__main__":
    unittest.main()
