"""Contract tests for ForceAtlas2 and hierarchical edge bundling layouts."""

from __future__ import annotations

import math
import unittest

from readmenator._graphlayout import (
    ForceAtlas2Settings,
    _fa2_python,
    fit_frames,
    forceatlas2_frames,
    hierarchical_edge_bundling,
    interpolate_frames,
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


if __name__ == "__main__":
    unittest.main()
