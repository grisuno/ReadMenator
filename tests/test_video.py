"""Contract tests for the cinematic overview video renderer."""

import math
import unittest

from readmenator._config import Config
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node, SecurityFinding, Symbol
from readmenator._video import (
    CinematicVideoRenderer,
    dependencies_available,
    hash_color,
    project3d,
    short_label,
)


def _nodes() -> list:
    """Build a tiny two-file project for video tests."""
    return [
        Node("a.py", "a.py", "module", "python", "", [Symbol("main", "function", 1)]),
        Node("b.py", "b.py", "module", "python", "", [Symbol("help", "function", 2)]),
    ]


def _analysis() -> AnalysisResult:
    """Build minimal analysis output with one community."""
    return AnalysisResult(
        god_nodes=[("a.py", 2.0)],
        communities=[CommunityResult(0, "root", {"a.py", "b.py"}, 1.0, 2)],
        surprising_connections=[],
        suggested_questions=[],
        node_count=2,
        edge_count=1,
    )


class TestVideoContract(unittest.TestCase):
    def test_video_collect_counts(self) -> None:
        renderer = CinematicVideoRenderer(Config())
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")], None,
            _analysis(), {"a.py": "business_logic"}, [], None, "demo", {},
        )
        self.assertEqual(data["files"], 2)
        self.assertEqual(data["symbols"], 2)
        self.assertEqual(data["imports"], 1)
        self.assertEqual(data["project"], "demo")
        self.assertTrue(data["dna"])

    def test_video_collect_empty_project(self) -> None:
        renderer = CinematicVideoRenderer(Config())
        data = renderer.collect([], [], None, None, {}, [], None, "empty", {})
        self.assertEqual(data["files"], 0)
        self.assertEqual(data["graph_nodes"], [])
        self.assertEqual(data["dep_tree"]["order"], [])
        scenes, total = renderer.build_scenes(data)
        self.assertTrue(total > 0)
        self.assertEqual(len(scenes), 21)

    def test_video_collect_enriched_fields(self) -> None:
        renderer = CinematicVideoRenderer(Config())
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")],
            [Edge("a.py", "b.py", "resolved_imports")],
            _analysis(), {"a.py": "business_logic", "b.py": "testing"},
            [], None, "demo", {"a.py": "def main():\n    pass\n"},
        )
        self.assertTrue(data["god_details"])
        self.assertEqual(data["god_details"][0]["file"], "a.py")
        self.assertIn("in", data["god_details"][0])
        self.assertEqual(data["dep_tree"]["root"], "a.py")
        self.assertIn("a.py", data["dep_tree"]["order"])
        self.assertIn("b.py", data["dep_tree"]["order"])
        self.assertTrue(data["preview_lines"])
        self.assertEqual(data["preview_file"], "a.py")
        self.assertTrue(data["node_symbols"]["a.py"])
        self.assertEqual(data["communities"][0]["hub"], "a.py")
        self.assertIn("internal", data["communities"][0])

    def test_video_build_scenes_durations(self) -> None:
        config = Config(VIDEO_TITLE_S=1.0, VIDEO_OUTRO_S=2.0)
        renderer = CinematicVideoRenderer(config)
        data = renderer.collect([], [], None, None, {}, [], None, "x", {})
        scenes, total = renderer.build_scenes(data)
        self.assertAlmostEqual(total, sum(s["dur"] for s in scenes))
        kinds = [s["kind"] for s in scenes]
        for expected in ("title", "layers", "gods", "tree", "communities", "graph", "orbit",
                         "bundle", "sphere", "dna", "invite", "outro"):
            self.assertIn(expected, kinds)
        self.assertEqual(kinds[-2:], ["invite", "outro"])

    def test_video_all_scenes_render_small_canvas(self) -> None:
        config = Config(VIDEO_WIDTH=320, VIDEO_HEIGHT=180, VIDEO_FPS=5,
                        VIDEO_TITLE_S=0.5, VIDEO_CARD_S=0.3, VIDEO_LAYER_S=0.5,
                        VIDEO_GOD_S=0.5, VIDEO_TREE_S=0.5, VIDEO_COMM_S=0.5,
                        VIDEO_GRAPH_S=0.8, VIDEO_DNA_S=0.8, VIDEO_OUTRO_S=0.5,
                        VIDEO_ORBIT_S=0.8, VIDEO_SPHERE_S=0.8, VIDEO_INVITE_S=0.5)
        renderer = CinematicVideoRenderer(config)
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")],
            [Edge("a.py", "b.py", "resolved_imports")],
            _analysis(), {"a.py": "business_logic", "b.py": "testing"},
            [], None, "demo", {"a.py": "def main():\n    pass\n", "b.py": "x = 1\n"},
        )
        scenes, _ = renderer.build_scenes(data)
        for s in scenes:
            fi = int((s["start"] + s["dur"] / 2) * config.VIDEO_FPS)
            buf = renderer.render_single_frame(data, fi)
            self.assertEqual(len(buf), 320 * 180 * 3, s["kind"])

    def test_video_new_scenes_render_every_phase(self) -> None:
        """Orbit, sphere and invite render at every phase on a small canvas."""
        config = Config(VIDEO_WIDTH=320, VIDEO_HEIGHT=180, VIDEO_FPS=10,
                        VIDEO_ORBIT_S=2.0, VIDEO_SPHERE_S=2.0, VIDEO_INVITE_S=1.0)
        renderer = CinematicVideoRenderer(config)
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")],
            [Edge("a.py", "b.py", "resolved_imports")],
            _analysis(), {"a.py": "business_logic", "b.py": "testing"},
            [], None, "demo", {},
        )
        scenes, _ = renderer.build_scenes(data)
        for s in scenes:
            if s["kind"] not in ("orbit", "sphere", "invite"):
                continue
            for frac in (0.05, 0.2, 0.5, 0.85, 0.99):
                fi = int((s["start"] + s["dur"] * frac) * config.VIDEO_FPS)
                self.assertEqual(len(renderer.render_single_frame(data, fi)), 320 * 180 * 3, (s["kind"], frac))

    def test_video_zero_duration_act_skips_its_card(self) -> None:
        """An act with no duration disappears together with its interstitial card."""
        renderer = CinematicVideoRenderer(Config(VIDEO_ORBIT_S=0.0, VIDEO_SPHERE_S=0.0, VIDEO_INVITE_S=0.0))
        data = renderer.collect([], [], None, None, {}, [], None, "x", {})
        scenes, _ = renderer.build_scenes(data)
        kinds = [s["kind"] for s in scenes]
        for gone in ("orbit", "sphere", "invite"):
            self.assertNotIn(gone, kinds)
        self.assertNotIn("VI", [s.get("card") for s in scenes])
        self.assertEqual(len(scenes), 16)

    def test_video_orbit_layout_is_normalized_and_stable(self) -> None:
        """The 3D orbit layout is deterministic and bounded; tour stops target real communities."""
        renderer = CinematicVideoRenderer(Config())
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")],
            [Edge("a.py", "b.py", "resolved_imports")],
            _analysis(), {}, [], None, "demo", {},
        )
        first = renderer.orbit_positions(data)
        self.assertEqual(first, renderer.orbit_positions(data))
        self.assertEqual(set(first), {"a.py", "b.py"})
        for p in first.values():
            self.assertLessEqual(math.sqrt(sum(c * c for c in p)), 1.3 + 1e-9)
        stops = renderer.orbit_stops(data, first)
        self.assertEqual(stops[0]["label"], "root")
        sphere = renderer.sphere_layout(data)
        self.assertEqual(set(sphere.leaves), {"a.py", "b.py"})

    def test_video_project3d_centers_target(self) -> None:
        """The look-at point projects to the screen center; nearer points scale up."""
        x, y, _z, _k = project3d((1.0, 2.0, 3.0), 0.7, -0.3, (1.0, 2.0, 3.0), 100.0, (50.0, 40.0), 3.0)
        self.assertAlmostEqual(x, 50.0)
        self.assertAlmostEqual(y, 40.0)
        near = project3d((0.0, 0.0, -1.0), 0.0, 0.0, (0.0, 0.0, 0.0), 100.0, (0.0, 0.0), 3.0)
        far = project3d((0.0, 0.0, 1.0), 0.0, 0.0, (0.0, 0.0, 0.0), 100.0, (0.0, 0.0), 3.0)
        self.assertGreater(near[3], far[3])

    def test_video_graph_positions_deterministic(self) -> None:
        renderer = CinematicVideoRenderer(Config())
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")],
            [Edge("a.py", "b.py", "resolved_imports")],
            _analysis(), {}, [], None, "demo", {},
        )
        first = renderer.graph_positions(data, (0, 0, 400, 300))
        second = renderer.graph_positions(data, (0, 0, 400, 300))
        self.assertEqual(first, second)

    def test_video_single_frame_bytes(self) -> None:
        config = Config(VIDEO_WIDTH=320, VIDEO_HEIGHT=180, VIDEO_FPS=5,
                        VIDEO_TITLE_S=0.5, VIDEO_CARD_S=0.3, VIDEO_LAYER_S=0.5,
                        VIDEO_GOD_S=0.5, VIDEO_COMM_S=0.5, VIDEO_GRAPH_S=0.8,
                        VIDEO_DNA_S=0.8, VIDEO_OUTRO_S=0.5)
        renderer = CinematicVideoRenderer(config)
        data = renderer.collect(
            _nodes(), [Edge("a.py", "b.py", "imports")], None,
            _analysis(), {"a.py": "business_logic", "b.py": "testing"},
            [SecurityFinding("a.py", 1, "high", "PY001", "d", "s", "CWE-78")],
            None, "demo", {"a.py": "print(1)", "b.py": "print(2)"},
        )
        buf = renderer.render_single_frame(data, 0)
        self.assertEqual(len(buf), 320 * 180 * 3)

    def test_video_hash_color_deterministic(self) -> None:
        import hashlib

        digest = hashlib.sha256(b"a.py").digest()
        self.assertEqual(hash_color(digest), hash_color(digest))

    def test_video_short_label_truncates(self) -> None:
        self.assertEqual(short_label("abc", 5), "abc")
        self.assertTrue(short_label("a" * 50, 10).endswith("…"))
        self.assertNotIn("\n", short_label("a\nb", 10))

    def test_video_dependencies_returns_bool(self) -> None:
        self.assertIsInstance(dependencies_available(), bool)

    def test_video_disabled_skips_without_render(self) -> None:
        from pathlib import Path

        from readmenator._app import readmenatorApplication

        app = readmenatorApplication(Config(VIDEO_ENABLED=False))
        out = app._maybe_export_video(
            Path("."), _nodes(), [], None, _analysis(), {}, [], None, {},
        )
        self.assertIsNone(out)


if __name__ == "__main__":
    unittest.main()
