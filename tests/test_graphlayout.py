"""Contract tests for ForceAtlas2 and hierarchical edge bundling layouts."""

from __future__ import annotations

import math
import unittest

from readmenator._graphlayout import (
    ForceAtlas2Settings,
    _fa2_python,
    _initial_positions,
    fibonacci_sphere,
    fit_frames,
    forceatlas2_frames,
    hierarchical_edge_bundling,
    interpolate_frames,
    normalize_cloud,
    spherical_edge_bundling,
)


def _two_cliques():
    """Two dense 4-cliques joined by one bridge edge."""
    a = [f"a{i}" for i in range(4)]
    b = [f"b{i}" for i in range(4)]
    edges = [(x, y) for grp in (a, b) for i, x in enumerate(grp) for y in grp[i + 1:]]
    edges.append(("a0", "b0"))
    return a + b, edges


class TestForceAtlas2Contract(unittest.TestCase):
    """Contract: deterministic snapshots that separate dense groups."""

    def test_graphlayout_fa2_snapshot_count(self) -> None:
        """Snapshots include start and end and match the requested count."""
        ids, edges = _two_cliques()
        frames = forceatlas2_frames(ids, edges, ForceAtlas2Settings(iterations=50, snapshots=6))
        self.assertEqual(len(frames), 6)
        self.assertEqual(set(frames[-1]), set(ids))

    def test_graphlayout_fa2_is_deterministic(self) -> None:
        """Identical input and seed yield identical layouts."""
        ids, edges = _two_cliques()
        cfg = ForceAtlas2Settings(iterations=40, snapshots=3)
        self.assertEqual(forceatlas2_frames(ids, edges, cfg), forceatlas2_frames(ids, edges, cfg))

    def test_graphlayout_fa2_separates_communities(self) -> None:
        """Intra-clique distances end smaller than inter-clique distances."""
        ids, edges = _two_cliques()
        final = forceatlas2_frames(ids, edges, ForceAtlas2Settings(iterations=200, snapshots=2))[-1]

        def mean(pairs):
            return sum(math.dist(final[x], final[y]) for x, y in pairs) / len(pairs)

        inside = [("a1", "a2"), ("a2", "a3"), ("b1", "b2"), ("b2", "b3")]
        across = [("a1", "b1"), ("a2", "b2"), ("a3", "b3"), ("a1", "b3")]
        self.assertLess(mean(inside), mean(across))

    def test_graphlayout_fa2_python_fallback_runs(self) -> None:
        """The pure Python path produces finite coordinates."""
        frames = _fa2_python(3, [(0, 1), (1, 2)], [(0.0, 0.0), (5.0, 1.0), (2.0, 7.0)],
                             ForceAtlas2Settings(iterations=20, snapshots=2))
        for x, y in frames[-1]:
            self.assertTrue(math.isfinite(x) and math.isfinite(y))

    def test_graphlayout_empty_and_single(self) -> None:
        """Empty input yields no frames; one node sits at the origin."""
        self.assertEqual(forceatlas2_frames([], []), [])
        self.assertEqual(forceatlas2_frames(["x"], [])[-1], {"x": (0.0, 0.0)})

    def test_graphlayout_fit_frames_stays_in_box(self) -> None:
        """Fitted coordinates stay inside the box margins."""
        ids, edges = _two_cliques()
        frames = fit_frames(forceatlas2_frames(ids, edges, ForceAtlas2Settings(iterations=30, snapshots=4)),
                            (0, 0, 200, 100), 10)
        for frame in frames:
            for x, y in frame.values():
                self.assertTrue(10 <= x <= 190 and 10 <= y <= 90)

    def test_graphlayout_interpolate_endpoints(self) -> None:
        """t=0 returns the first snapshot and t=1 the last."""
        frames = [{"n": (0.0, 0.0)}, {"n": (10.0, 20.0)}]
        self.assertEqual(interpolate_frames(frames, 0.0), {"n": (0.0, 0.0)})
        self.assertEqual(interpolate_frames(frames, 1.0), {"n": (10.0, 20.0)})
        self.assertEqual(interpolate_frames(frames, 0.5), {"n": (5.0, 10.0)})


class TestEdgeBundlingContract(unittest.TestCase):
    """Contract: radial leaves by group and bundled B-spline curves."""

    def setUp(self) -> None:
        """Build a two-group bundle."""
        self.layout = hierarchical_edge_bundling(
            {"g1": ["a", "b"], "g2": ["c", "d"]},
            [("a", "c"), ("a", "b"), ("x", "a")],
            (100.0, 100.0), 50.0, beta=0.9, samples=12,
        )

    def test_graphlayout_leaves_on_circle(self) -> None:
        """Every leaf lies on the outer radius."""
        for x, y in self.layout.leaves.values():
            self.assertAlmostEqual(math.hypot(x - 100, y - 100), 50.0, places=6)

    def test_graphlayout_curves_skip_unknown_and_keep_endpoints(self) -> None:
        """Unknown endpoints are dropped and curves start and end at the leaves."""
        self.assertEqual(len(self.layout.curves), 2)
        for a, b, pts in self.layout.curves:
            self.assertAlmostEqual(pts[0][0], self.layout.leaves[a][0], places=6)
            self.assertAlmostEqual(pts[-1][1], self.layout.leaves[b][1], places=6)

    def test_graphlayout_cross_group_curve_bends_inward(self) -> None:
        """A cross-group edge passes closer to the center than its chord midpoint."""
        a, c, pts = [cv for cv in self.layout.curves if cv[1] == "c"][0]
        chord = ((self.layout.leaves[a][0] + self.layout.leaves[c][0]) / 2,
                 (self.layout.leaves[a][1] + self.layout.leaves[c][1]) / 2)
        closest = min(math.hypot(x - 100, y - 100) for x, y in pts)
        self.assertLessEqual(closest, math.hypot(chord[0] - 100, chord[1] - 100) + 1e-6)

    def test_graphlayout_groups_cover_full_circle(self) -> None:
        """Group arcs are ordered and carry member counts."""
        self.assertEqual([g[0] for g in self.layout.groups], ["g1", "g2"])
        self.assertEqual([g[3] for g in self.layout.groups], [2, 2])



class TestForceAtlas2ThreeDContract(unittest.TestCase):
    """Contract: ForceAtlas2 in three dimensions, deterministic, with a pure Python path."""

    def test_graphlayout_fa2_3d_returns_triples(self) -> None:
        """dims=3 yields (x, y, z) for every node in every snapshot."""
        ids, edges = _two_cliques()
        frames = forceatlas2_frames(ids, edges, ForceAtlas2Settings(iterations=30, snapshots=3, dims=3))
        self.assertEqual(len(frames), 3)
        for frame in frames:
            self.assertTrue(all(len(p) == 3 for p in frame.values()))

    def test_graphlayout_fa2_3d_is_deterministic(self) -> None:
        """Two runs with the same seed are identical."""
        ids, edges = _two_cliques()
        cfg = ForceAtlas2Settings(iterations=30, snapshots=2, dims=3)
        self.assertEqual(forceatlas2_frames(ids, edges, cfg), forceatlas2_frames(ids, edges, cfg))

    def test_graphlayout_fa2_3d_python_fallback_runs(self) -> None:
        """The pure Python path handles three dimensions."""
        start = _initial_positions(4, 7, 3)
        frames = _fa2_python(4, [(0, 1), (2, 3)], start, ForceAtlas2Settings(iterations=12, snapshots=2))
        self.assertTrue(all(len(p) == 3 for p in frames[-1]))

    def test_graphlayout_fa2_2d_seed_unchanged_by_dims(self) -> None:
        """2D starting positions keep the historical random sequence."""
        self.assertEqual(_initial_positions(3, 7, 2), _initial_positions(3, 7))

    def test_graphlayout_single_node_3d_at_origin(self) -> None:
        """A single node sits at the 3D origin."""
        frames = forceatlas2_frames(["n"], [], ForceAtlas2Settings(dims=3))
        self.assertEqual(frames[-1]["n"], (0.0, 0.0, 0.0))

    def test_graphlayout_normalize_cloud_bounds_outliers(self) -> None:
        """Normalized clouds are centered and no point exceeds max_radius."""
        pts = {f"n{i}": (float(i % 3), float(i % 5), float(i % 7)) for i in range(40)}
        pts["far"] = (1000.0, 0.0, 0.0)
        out = normalize_cloud(pts, 0.85, 1.3)
        self.assertTrue(all(math.sqrt(sum(c * c for c in p)) <= 1.3 + 1e-9 for p in out.values()))
        self.assertEqual(normalize_cloud({}), {})


class TestSphericalBundlingContract(unittest.TestCase):
    """Contract: community caps on a unit sphere with exact sizes and bundled 3D curves."""

    def setUp(self) -> None:
        """Build three groups of unequal size with cross and inner edges."""
        self.groups = {
            "big": [f"b{i}" for i in range(30)],
            "mid": [f"m{i}" for i in range(12)],
            "small": [f"s{i}" for i in range(4)],
        }
        self.edges = [("b0", "m0"), ("b1", "b2"), ("s0", "b3"), ("ghost", "b0"), ("m1", "m1")]
        self.layout = spherical_edge_bundling(self.groups, self.edges, 1.0, beta=0.9, samples=12)

    def test_graphlayout_fibonacci_sphere_unit_vectors(self) -> None:
        """Fibonacci points are unit vectors and distinct."""
        pts = fibonacci_sphere(50)
        self.assertEqual(len(set(pts)), 50)
        for p in pts:
            self.assertAlmostEqual(math.sqrt(sum(c * c for c in p)), 1.0, places=9)
        self.assertEqual(fibonacci_sphere(0), [])

    def test_graphlayout_sphere_leaves_on_surface(self) -> None:
        """Every member gets a distinct point on the sphere."""
        self.assertEqual(len(self.layout.leaves), 46)
        self.assertEqual(len(set(self.layout.leaves.values())), 46)
        for p in self.layout.leaves.values():
            self.assertAlmostEqual(math.sqrt(sum(c * c for c in p)), 1.0, places=9)

    def test_graphlayout_sphere_caps_have_exact_sizes(self) -> None:
        """Caps keep caller order and member counts."""
        self.assertEqual([(g[0], g[2]) for g in self.layout.groups], [("big", 30), ("mid", 12), ("small", 4)])

    def test_graphlayout_sphere_caps_are_compact(self) -> None:
        """Members sit closer to their own cap center than to any other cap center on average."""
        centers = {label: center for label, center, _n in self.layout.groups}
        for label, members in self.groups.items():
            own = sum(sum(self.layout.leaves[m][k] * centers[label][k] for k in range(3)) for m in members)
            for other in centers:
                if other != label:
                    alien = sum(sum(self.layout.leaves[m][k] * centers[other][k] for k in range(3)) for m in members)
                    self.assertGreater(own, alien)

    def test_graphlayout_sphere_hub_is_closest_to_cap_center(self) -> None:
        """The first listed member (the hub) takes the point nearest its cap center."""
        center = dict((label, c) for label, c, _n in self.layout.groups)["big"]
        dots = {m: sum(self.layout.leaves[m][k] * center[k] for k in range(3)) for m in self.groups["big"]}
        self.assertEqual(max(dots, key=dots.get), "b0")

    def test_graphlayout_sphere_curves_skip_unknown_and_self(self) -> None:
        """Unknown endpoints and self loops are dropped; curves keep their endpoints."""
        self.assertEqual(len(self.layout.curves), 3)
        for a, b, pts in self.layout.curves:
            for k in range(3):
                self.assertAlmostEqual(pts[0][k], self.layout.leaves[a][k], places=6)
                self.assertAlmostEqual(pts[-1][k], self.layout.leaves[b][k], places=6)

    def test_graphlayout_sphere_cross_curve_dives_inside(self) -> None:
        """A cross-cap edge passes well inside the sphere."""
        _a, _b, pts = [c for c in self.layout.curves if c[1] == "m0"][0]
        self.assertLess(min(math.sqrt(sum(v * v for v in p)) for p in pts), 0.8)

    def test_graphlayout_sphere_is_deterministic_and_empty_safe(self) -> None:
        """Same input, same layout; no members yields an empty layout."""
        again = spherical_edge_bundling(self.groups, self.edges, 1.0, beta=0.9, samples=12)
        self.assertEqual(again.leaves, self.layout.leaves)
        self.assertEqual(spherical_edge_bundling({}, [], 1.0).leaves, {})


if __name__ == "__main__":
    unittest.main()
