"""Contract tests for the procedural video soundtrack and chapter marks."""

import array
import dataclasses
import io
import math
import os
import tempfile
import unittest
import wave
from unittest import mock

from readmenator._config import Config
from readmenator._soundtrack import AudioCue, SoundtrackComposer
from readmenator._video import (
    CinematicVideoRenderer,
    apply_glow,
    chapter_metadata,
    draw_orb,
    emit_beam,
    emit_orb,
    dependencies_available,
    draw_stars,
    growth_release_times,
    hook_lines,
    impact_punch,
    score_ping_times,
    score_sync,
)


def _config(**overrides: object) -> Config:
    """Build a small, fast audio configuration."""
    base = dict(VIDEO_AUDIO_SAMPLE_RATE=8000, VIDEO_AUDIO_FADE_IN_S=0.0, VIDEO_AUDIO_FADE_OUT_S=0.0)
    base.update(overrides)
    return dataclasses.replace(Config(), **base)


def _scenes() -> list:
    """Title, card, act, card, act, outro on a short clock."""
    plan = [("title", 2.0), ("card", 1.5), ("graph", 3.0), ("card", 1.5), ("growth", 4.0), ("outro", 2.0)]
    out, clock = [], 0.0
    for kind, dur in plan:
        out.append({"kind": kind, "start": clock, "dur": dur})
        clock += dur
    return out


def _frames(blob: bytes) -> array.array:
    """Decode WAV bytes into interleaved signed 16-bit samples."""
    with wave.open(io.BytesIO(blob), "rb") as handle:
        samples = array.array("h")
        samples.frombytes(handle.readframes(handle.getnframes()))
    return samples


def _rms(samples: array.array, rate: int, start: float, end: float) -> float:
    """Root mean square of the left channel between two times."""
    window = samples[int(start * rate) * 2:int(end * rate) * 2:2]
    return math.sqrt(sum(v * v for v in window) / max(1, len(window)))


class TestSoundtrackContract(unittest.TestCase):
    def test_soundtrack_wav_shape_matches_video_duration(self) -> None:
        blob = SoundtrackComposer(_config()).compose(_scenes(), 14.0)
        with wave.open(io.BytesIO(blob), "rb") as handle:
            self.assertEqual(handle.getnchannels(), 2)
            self.assertEqual(handle.getsampwidth(), 2)
            self.assertEqual(handle.getframerate(), 8000)
            self.assertEqual(handle.getnframes(), 14 * 8000)

    def test_soundtrack_is_deterministic(self) -> None:
        first = SoundtrackComposer(_config()).compose(_scenes(), 14.0, [9.0, 10.0])
        second = SoundtrackComposer(_config()).compose(_scenes(), 14.0, [9.0, 10.0])
        self.assertEqual(first, second)

    def test_soundtrack_seed_changes_noise(self) -> None:
        first = SoundtrackComposer(_config()).compose(_scenes(), 14.0)
        second = SoundtrackComposer(_config(VIDEO_AUDIO_SEED=99)).compose(_scenes(), 14.0)
        self.assertNotEqual(first, second)

    def test_soundtrack_acts_are_louder_than_cards(self) -> None:
        cfg = _config(VIDEO_AUDIO_IMPACT_GAIN=0.0, VIDEO_AUDIO_RISER_GAIN=0.0)
        samples = _frames(SoundtrackComposer(cfg).compose(_scenes(), 14.0))
        card = _rms(samples, 8000, 2.6, 3.4)
        act = _rms(samples, 8000, 4.0, 6.0)
        self.assertGreater(card, 0.0)
        self.assertGreater(act, card * 1.5)

    def test_soundtrack_never_clips_past_pcm_range(self) -> None:
        cfg = _config(VIDEO_AUDIO_MASTER_GAIN=5.0)
        samples = _frames(SoundtrackComposer(cfg).compose(_scenes(), 14.0, [9.0]))
        self.assertLessEqual(max(samples), 32767)
        self.assertGreaterEqual(min(samples), -32767)

    def test_soundtrack_master_fades_reach_silence(self) -> None:
        cfg = _config(VIDEO_AUDIO_FADE_IN_S=0.5, VIDEO_AUDIO_FADE_OUT_S=0.5)
        samples = _frames(SoundtrackComposer(cfg).compose(_scenes(), 14.0))
        self.assertEqual(samples[0], 0)
        self.assertEqual(samples[-1], 0)
        self.assertEqual(samples[-2], 0)

    def test_soundtrack_cues_follow_scene_cuts(self) -> None:
        composer = SoundtrackComposer(_config())
        cues = composer.cues(_scenes(), [9.0, 10.0])
        impacts = [cue.time for cue in cues if cue.kind == "impact"]
        risers = [cue.time for cue in cues if cue.kind == "riser"]
        self.assertEqual(impacts, [3.5, 8.0, 12.0])
        riser = Config().VIDEO_AUDIO_RISER_S
        self.assertEqual(risers, [3.5 - riser, 8.0 - riser, 12.0 - riser])
        self.assertEqual(cues, sorted(cues, key=lambda cue: (cue.time, cue.kind)))

    def test_soundtrack_pings_rise_along_the_scale(self) -> None:
        composer = SoundtrackComposer(_config())
        pings = [cue for cue in composer.cues([], [1.0, 2.0, 3.0]) if cue.kind == "ping"]
        self.assertEqual(len(pings), 3)
        self.assertLess(pings[0].pitch, pings[1].pitch)
        self.assertLess(pings[1].pitch, pings[2].pitch)

    def test_soundtrack_impact_adds_energy_on_the_cut(self) -> None:
        quiet = _config(VIDEO_AUDIO_IMPACT_GAIN=0.0, VIDEO_AUDIO_RISER_GAIN=0.0)
        loud = _config(VIDEO_AUDIO_RISER_GAIN=0.0)
        base = _frames(SoundtrackComposer(quiet).compose(_scenes(), 14.0))
        hit = _frames(SoundtrackComposer(loud).compose(_scenes(), 14.0))
        self.assertGreater(_rms(hit, 8000, 3.5, 3.8), _rms(base, 8000, 3.5, 3.8))
        self.assertEqual(_rms(hit, 8000, 0.5, 1.5), _rms(base, 8000, 0.5, 1.5))

    def test_soundtrack_beat_restarts_on_every_act(self) -> None:
        cfg = _config(VIDEO_AUDIO_IMPACT_GAIN=0.0, VIDEO_AUDIO_RISER_GAIN=0.0, VIDEO_AUDIO_CROSSFADE_S=0.0)
        scenes = [{"kind": "graph", "start": 0.0, "dur": 1.3}, {"kind": "graph", "start": 1.3, "dur": 1.0}]
        samples = _frames(SoundtrackComposer(cfg).compose(scenes, 2.3))
        offset = int(round(1.3 * 8000)) * 2
        self.assertEqual(samples[:4000], samples[offset:offset + 4000])

    def test_soundtrack_empty_timeline_is_valid_silence(self) -> None:
        blob = SoundtrackComposer(_config()).compose([], 0.0)
        with wave.open(io.BytesIO(blob), "rb") as handle:
            self.assertEqual(handle.getnframes(), 0)

    def test_soundtrack_unknown_cue_is_ignored(self) -> None:
        composer = SoundtrackComposer(_config())
        self.assertEqual(composer._event(AudioCue("laser", 0.0)), [])

    def test_soundtrack_level_is_clamped(self) -> None:
        cfg = _config(VIDEO_AUDIO_SCENE_LEVELS=(("card", -3.0), ("graph", 9.0)))
        composer = SoundtrackComposer(cfg)
        self.assertEqual(composer.level("card"), 0.0)
        self.assertEqual(composer.level("graph"), 1.0)
        self.assertEqual(composer.level("unknown"), Config().VIDEO_AUDIO_DEFAULT_LEVEL)


class TestVideoAudioWiringContract(unittest.TestCase):
    def test_video_audio_track_composes_score_in_workdir(self) -> None:
        renderer = CinematicVideoRenderer(_config())
        with tempfile.TemporaryDirectory() as workdir, mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("READMENATOR_MUSIC", None)
            path = renderer.audio_track({}, _scenes(), 14.0, workdir)
            self.assertTrue(path.startswith(workdir))
            self.assertTrue(os.path.isfile(path))

    def test_video_audio_disabled_yields_silent_video(self) -> None:
        renderer = CinematicVideoRenderer(_config(VIDEO_AUDIO_ENABLED=False))
        with tempfile.TemporaryDirectory() as workdir, mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("READMENATOR_MUSIC", None)
            self.assertEqual(renderer.audio_track({}, _scenes(), 14.0, workdir), "")
            cmd = renderer._encode_command({}, _scenes(), 14.0, "out.mp4", workdir)
        self.assertNotIn("aac", cmd)

    def test_video_user_music_wins_over_generated_score(self) -> None:
        with tempfile.TemporaryDirectory() as workdir:
            music = os.path.join(workdir, "mine.mp3")
            with open(music, "wb") as handle:
                handle.write(b"x")
            renderer = CinematicVideoRenderer(_config(VIDEO_MUSIC_PATH=music))
            self.assertEqual(renderer.audio_track({}, _scenes(), 14.0, workdir), music)

    def test_video_encode_command_maps_audio_and_chapters(self) -> None:
        renderer = CinematicVideoRenderer(_config())
        with tempfile.TemporaryDirectory() as workdir, mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("READMENATOR_MUSIC", None)
            cmd = renderer._encode_command({"project": "demo"}, _scenes(), 14.0, "out.mp4", workdir)
        self.assertEqual(cmd[0], "ffmpeg")
        self.assertEqual(cmd[-1], "out.mp4")
        self.assertIn("1:a", cmd)
        self.assertEqual(cmd[cmd.index("-map_chapters") + 1], "2")
        self.assertEqual(cmd[cmd.index("-b:a") + 1], Config().VIDEO_AUDIO_BITRATE)

    def test_video_chapters_cover_the_timeline_from_each_card(self) -> None:
        scenes = _scenes()
        scenes[2]["act"] = "V"
        text = chapter_metadata(scenes, 14.0, Config(), "demo")
        self.assertTrue(text.startswith(";FFMETADATA1\n"))
        self.assertEqual(text.count("[CHAPTER]"), 4)
        self.assertIn("START=2000\nEND=6500\ntitle=V. Emergence", text)
        self.assertIn("START=6500\nEND=12000\ntitle=The Organism", text)
        self.assertIn("END=14000\ntitle=Telemetry", text)

    def test_video_chapter_titles_escape_metadata_syntax(self) -> None:
        text = chapter_metadata(_scenes(), 14.0, Config(), "a=b;c#d\nTIMEBASE=1/1")
        self.assertIn("title=a\\=b\\;c\\#d\\\nTIMEBASE\\=1/1 // codebase overview", text)

    def test_video_growth_release_times_span_the_growing_phase(self) -> None:
        cfg = Config()
        data = {"growth": {"releases": [{}, {}, {}]}}
        times = growth_release_times(_scenes(), data, cfg)
        grow = cfg.VIDEO_GROWTH_GROW_FRACTION * 4.0
        self.assertEqual(times, [8.0, 8.0 + grow / 2, 8.0 + grow])
        self.assertEqual(growth_release_times(_scenes(), {}, cfg), [])


def _hook_data() -> dict:
    """Scene payload with a hub, dependents and a release history."""
    return {
        "files": 1200, "symbols": 3400,
        "dep_tree": {"root": "pkg/core.py", "order": ["pkg/core.py", "a.py", "b.py"]},
        "growth": {"releases": [{}, {}, {}]},
    }


class TestVideoColdOpenContract(unittest.TestCase):
    def test_video_hook_lines_state_measured_facts(self) -> None:
        lines = hook_lines(_hook_data())
        self.assertEqual(lines[0], "1,200 FILES. 3,400 SYMBOLS.")
        self.assertEqual(lines[1], "2 OF THEM BREAK IF CORE.PY BREAKS.")
        self.assertEqual(lines[2], "3 RELEASES OF HISTORY.")
        self.assertEqual(lines[-1], "THIS IS ITS ANATOMY.")

    def test_video_hook_lines_skip_missing_facts(self) -> None:
        self.assertEqual(hook_lines({"files": 0}), [])
        lines = hook_lines({"files": 2, "symbols": 5, "dep_tree": {"root": "a.py", "order": ["a.py"]}})
        self.assertEqual(lines, ["2 FILES. 5 SYMBOLS.", "THIS IS ITS ANATOMY."])

    def test_video_hook_scene_opens_the_timeline_with_accents(self) -> None:
        renderer = CinematicVideoRenderer(Config())
        scenes, _total = renderer.build_scenes(_hook_data())
        self.assertEqual([scene["kind"] for scene in scenes[:2]], ["hook", "title"])
        accents = scenes[0]["accents"]
        self.assertEqual(len(accents), len(scenes[0]["lines"]))
        self.assertEqual(accents, sorted(accents))
        self.assertLess(accents[-1], scenes[0]["dur"])
        self.assertEqual(scenes[1]["start"], Config().VIDEO_HOOK_S)

    def test_video_hook_disabled_or_empty_starts_on_title(self) -> None:
        off = CinematicVideoRenderer(dataclasses.replace(Config(), VIDEO_HOOK_S=0.0))
        self.assertEqual(off.build_scenes(_hook_data())[0][0]["kind"], "title")
        empty = CinematicVideoRenderer(Config())
        self.assertEqual(empty.build_scenes({"files": 0})[0][0]["kind"], "title")

    def test_video_ping_times_cover_hook_lines_then_releases(self) -> None:
        cfg = Config()
        scenes = [{"kind": "hook", "start": 0.0, "dur": 4.0, "accents": [0.5, 1.5]},
                  {"kind": "growth", "start": 10.0, "dur": 10.0}]
        times = score_ping_times(scenes, {"growth": {"releases": [{}, {}]}}, cfg)
        self.assertEqual(times, [0.5, 1.5, 10.0, 10.0 + cfg.VIDEO_GROWTH_GROW_FRACTION * 10.0])

    def test_video_chapters_fold_the_hook_into_the_overview(self) -> None:
        scenes = [{"kind": "hook", "start": 0.0, "dur": 4.0}, {"kind": "title", "start": 4.0, "dur": 5.0}]
        text = chapter_metadata(scenes, 9.0, Config())
        self.assertEqual(text.count("[CHAPTER]"), 1)
        self.assertIn("START=0\nEND=9000\ntitle=Overview", text)


class TestVideoScoreSyncContract(unittest.TestCase):
    def setUp(self) -> None:
        self.cfg = Config()
        self.composer = SoundtrackComposer(self.cfg)
        self.scenes = _scenes()

    def test_video_beat_peaks_on_the_downbeat_of_an_act(self) -> None:
        beat = self.composer.beat_seconds
        on, _ = score_sync(self.scenes, 2, 0.0, self.cfg, self.composer)
        again, _ = score_sync(self.scenes, 2, beat + 1e-6, self.cfg, self.composer)
        off, _ = score_sync(self.scenes, 2, beat * 0.5, self.cfg, self.composer)
        self.assertAlmostEqual(on, 1.0)
        self.assertAlmostEqual(again, 1.0, places=3)
        self.assertLess(off, 0.2)

    def test_video_beat_is_silent_where_the_drums_are(self) -> None:
        beat, punch = score_sync(self.scenes, 1, 0.0, self.cfg, self.composer)
        self.assertEqual((beat, punch), (0.0, 0.0))

    def test_video_punch_decays_from_every_scored_cut(self) -> None:
        window = self.cfg.VIDEO_IMPACT_VISUAL_S
        _, start = score_sync(self.scenes, 2, 0.0, self.cfg, self.composer)
        _, mid = score_sync(self.scenes, 2, window / 2, self.cfg, self.composer)
        _, after = score_sync(self.scenes, 2, window, self.cfg, self.composer)
        _, first = score_sync(self.scenes, 0, 0.0, self.cfg, self.composer)
        self.assertEqual(start, 1.0)
        self.assertAlmostEqual(mid, 0.25)
        self.assertEqual(after, 0.0)
        self.assertEqual(first, 0.0)

    def test_video_sync_is_off_without_a_generated_score(self) -> None:
        cfg = dataclasses.replace(self.cfg, VIDEO_AUDIO_ENABLED=False)
        self.assertEqual(score_sync(self.scenes, 2, 0.0, cfg, self.composer), (0.0, 0.0))
        self.assertEqual(score_sync(self.scenes, 2, 0.0, self.cfg, None), (0.0, 0.0))

    def test_soundtrack_stem_weight_follows_thresholds(self) -> None:
        self.assertEqual(self.composer.stem_weight("pad", 0.0), 1.0)
        self.assertEqual(self.composer.stem_weight("drums", 0.1), 0.0)
        self.assertEqual(self.composer.stem_weight("drums", 1.0), 1.0)


@unittest.skipUnless(dependencies_available(), "PIL or ffmpeg is not installed")
class TestVideoImpactFramesContract(unittest.TestCase):
    def test_video_impact_punch_keeps_size_and_brightens(self) -> None:
        from PIL import Image

        frame = Image.new("RGB", (64, 36), (10, 20, 30))
        out = impact_punch(frame, 1.0, Config())
        self.assertEqual(out.size, frame.size)
        self.assertGreater(out.getpixel((32, 18))[0], 10)
        still = impact_punch(frame, 0.0, dataclasses.replace(Config(), VIDEO_IMPACT_FLASH=0.0))
        self.assertEqual(still.getpixel((32, 18)), (10, 20, 30))

    def test_video_stars_turn_with_the_camera_and_stay_in_the_box(self) -> None:
        from PIL import Image, ImageDraw

        def field(yaw: float) -> Image.Image:
            """Render the star field alone for one camera yaw."""
            img = Image.new("RGB", (120, 80), (0, 0, 0))
            draw_stars(ImageDraw.Draw(img, "RGBA"), (20, 10, 100, 70), yaw, 0.0, 0.0, 200)
            return img

        first, again, turned = field(0.0), field(0.0), field(1.0)
        self.assertEqual(first.tobytes(), again.tobytes())
        self.assertNotEqual(first.tobytes(), turned.tobytes())
        self.assertIsNotNone(first.getbbox())
        left, top, right, bottom = first.getbbox()
        self.assertTrue(left >= 20 and top >= 10 and right <= 100 and bottom <= 70)

    def test_video_stars_behind_the_camera_are_culled(self) -> None:
        from PIL import Image, ImageDraw

        img = Image.new("RGB", (400, 400), (0, 0, 0))
        draw_stars(ImageDraw.Draw(img, "RGBA"), (0, 0, 400, 400), 0.0, 0.0, 0.0, 300)
        data = img.tobytes()
        lit = sum(1 for i in range(0, len(data), 3) if data[i:i + 3] != b"\x00\x00\x00")
        self.assertGreater(lit, 0)
        self.assertLessEqual(lit, 30)


@unittest.skipUnless(dependencies_available(), "PIL or ffmpeg is not installed")
class TestVideoGlowContract(unittest.TestCase):
    def test_video_glow_adds_light_around_an_emitter_only(self) -> None:
        from PIL import Image

        frame = Image.new("RGB", (120, 80), (10, 10, 10))
        out = apply_glow(frame, [("orb", 60.0, 40.0, 4.0, (0, 255, 255), 1.0)], Config())
        self.assertEqual(out.size, frame.size)
        self.assertGreater(out.getpixel((60, 40))[1], 60)
        self.assertGreater(out.getpixel((70, 40))[1], out.getpixel((110, 40))[1])
        self.assertEqual(out.getpixel((60, 40))[0], 10)

    def test_video_glow_draws_beams_and_fog(self) -> None:
        from PIL import Image

        frame = Image.new("RGB", (120, 80), (0, 0, 0))
        beam = apply_glow(frame, [("beam", [(10.0, 40.0), (110.0, 40.0)], (255, 0, 0), 1.0, 2.0)], Config())
        self.assertGreater(beam.getpixel((60, 40))[0], 10)
        self.assertLess(beam.getpixel((60, 2))[0], beam.getpixel((60, 40))[0] // 2)
        fog = apply_glow(frame, [("fog", 60.0, 40.0, 30.0, (0, 0, 255), 0.2)], Config())
        self.assertGreater(fog.getpixel((60, 40))[2], 0)

    def test_video_glow_disabled_or_empty_returns_the_frame(self) -> None:
        from PIL import Image

        frame = Image.new("RGB", (40, 40), (5, 5, 5))
        off = dataclasses.replace(Config(), VIDEO_GLOW_ENABLED=False)
        self.assertIs(apply_glow(frame, [("orb", 20.0, 20.0, 4.0, (255, 255, 255), 1.0)], off), frame)
        self.assertIs(apply_glow(frame, [], Config()), frame)

    def test_video_emitters_record_only_inside_a_glow_pass(self) -> None:
        import readmenator._video as video
        from PIL import Image, ImageDraw

        emit_orb(1.0, 1.0, 2.0, (255, 255, 255), 1.0)
        self.assertIsNone(video._EMIT)
        video._EMIT = []
        try:
            frame = Image.new("RGB", (40, 40), (0, 0, 0))
            draw_orb(ImageDraw.Draw(frame, "RGBA"), 20.0, 20.0, 6.0, (0, 200, 0), 1.0)
            emit_beam([(0.0, 0.0), (5.0, 5.0)], (255, 0, 0), 0.5)
            emit_orb(1.0, 1.0, 2.0, (255, 255, 255), 0.0)
            kinds = [item[0] for item in video._EMIT]
        finally:
            video._EMIT = None
        self.assertEqual(kinds, ["orb", "beam"])
        self.assertGreater(min(frame.getpixel((20, 20))), 200)
        self.assertEqual(frame.getpixel((25, 20)), (0, 200, 0))


if __name__ == "__main__":
    unittest.main()
