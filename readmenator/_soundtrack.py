"""Procedural synthwave soundtrack for the overview video.

Composes a deterministic stereo score from the scene timeline with the
standard library only: a four-stem loop (pad, bass, drums, arpeggio)
whose density follows the energy of each scene, a downbeat that lands
on the first frame of every act, a riser into each act, an impact on
each cut and one rising ping per release of the growth timelapse.

Zero tokens, zero network, zero native dependencies: samples are
synthesised in pure Python and returned as 16-bit PCM WAV bytes.
"""

from __future__ import annotations

import array
import io
import math
import random
import sys
import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Sequence, Tuple

from readmenator._config import Config

PCM_PEAK = 32767
CHANNELS = 2
SAMPLE_WIDTH = 2
STEPS_PER_BEAT = 4
BEATS_PER_BAR = 4
SEMITONES = 12.0
TWO_PI = 2.0 * math.pi
THIRDS = {"minor": 3, "major": 4}
STEMS = ("pad", "bass", "drums", "arp")


@dataclass(frozen=True)
class AudioCue:
    """One timed sound event laid over the music bed.

    Attributes:
        kind: Event kind: impact, riser or ping.
        time: Start time in seconds on the video clock.
        pitch: Frequency in hertz for pitched events, 0.0 otherwise.
    """

    kind: str
    time: float
    pitch: float = 0.0


def _semitone(base: float, offset: float) -> float:
    """Return *base* shifted by *offset* equal-tempered semitones."""
    return base * (2.0 ** (offset / SEMITONES))


def _clamp_pcm(value: float) -> int:
    """Clamp a sample to the signed 16-bit range."""
    return max(-PCM_PEAK, min(PCM_PEAK, int(value)))


def _normalized(samples: List[float]) -> List[float]:
    """Scale samples so the absolute peak is 1.0 (silence stays silent)."""
    peak = max((abs(s) for s in samples), default=0.0)
    if peak <= 0.0:
        return samples
    return [s / peak for s in samples]


class SoundtrackComposer:
    """Compose the video score from the scene timeline.

    Args:
        config: Effective configuration carrying every VIDEO_AUDIO_* value.
    """

    def __init__(self, config: Config) -> None:
        self.config = config
        self._rate = max(8000, int(config.VIDEO_AUDIO_SAMPLE_RATE))
        beat_s = 60.0 / max(1.0, float(config.VIDEO_AUDIO_BPM))
        self._step = max(1, int(round(self._rate * beat_s / STEPS_PER_BEAT)))
        self._beat = self._step * STEPS_PER_BEAT
        self._bar = self._beat * BEATS_PER_BAR
        self._loops: Dict[float, array.array] = {}
        self._stems: Dict[str, List[float]] = {}

    @property
    def beat_seconds(self) -> float:
        """Exact duration of one beat of the rendered loop, in seconds."""
        return self._beat / self._rate

    def stem_weight(self, name: str, level: float) -> float:
        """Return how present a stem is (0..1) at one energy level."""
        thresholds = dict(self.config.VIDEO_AUDIO_STEM_THRESHOLDS)
        ramp = max(1e-6, float(self.config.VIDEO_AUDIO_STEM_RAMP))
        return max(0.0, min(1.0, (level - float(thresholds.get(name, 0.0))) / ramp))

    def level(self, kind: str) -> float:
        """Return the music energy (0..1) of a scene kind."""
        levels = dict(self.config.VIDEO_AUDIO_SCENE_LEVELS)
        value = float(levels.get(kind, self.config.VIDEO_AUDIO_DEFAULT_LEVEL))
        return max(0.0, min(1.0, value))

    def cues(
        self, scenes: Sequence[Dict[str, Any]], release_times: Sequence[float] = (),
    ) -> List[AudioCue]:
        """Derive the timed events from the scene timeline.

        Every scene that restarts the beat (acts, invite, outro) gets an
        impact on its first frame and a riser leading into it. Each
        release time of the growth act gets a ping on a rising scale.

        Args:
            scenes: Scene dictionaries with kind, start and dur.
            release_times: Video-clock seconds at which releases land.

        Returns:
            Cues sorted by time, then kind.
        """
        cfg = self.config
        out: List[AudioCue] = []
        riser = float(cfg.VIDEO_AUDIO_RISER_S)
        for index, scene in enumerate(scenes):
            if index == 0 or scene["kind"] in cfg.VIDEO_AUDIO_CONTINUE_KINDS:
                continue
            start = float(scene["start"])
            out.append(AudioCue("impact", start))
            if riser > 0:
                out.append(AudioCue("riser", max(0.0, start - riser)))
        scale = tuple(cfg.VIDEO_AUDIO_PING_SCALE) or (0,)
        base = float(cfg.VIDEO_AUDIO_ROOT_HZ) * 8.0
        for index, moment in enumerate(release_times):
            octave = (index // len(scale)) % 2
            pitch = _semitone(base, scale[index % len(scale)] + SEMITONES * octave)
            out.append(AudioCue("ping", float(moment), pitch))
        return sorted(out, key=lambda cue: (cue.time, cue.kind))

    def compose(
        self, scenes: Sequence[Dict[str, Any]], total: float,
        release_times: Sequence[float] = (),
    ) -> bytes:
        """Compose the full score and return it as WAV bytes.

        Args:
            scenes: Scene dictionaries with kind, start and dur.
            total: Video duration in seconds.
            release_times: Video-clock seconds at which releases land.

        Returns:
            A complete 16-bit stereo PCM WAV file.
        """
        frames = max(0, int(round(float(total) * self._rate)))
        track = self._bed(scenes, frames)
        for cue in self.cues(scenes, release_times):
            self._overlay(track, int(round(cue.time * self._rate)), self._event(cue))
        self._fade(track, frames)
        if sys.byteorder == "big":
            track.byteswap()
        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as handle:
            handle.setnchannels(CHANNELS)
            handle.setsampwidth(SAMPLE_WIDTH)
            handle.setframerate(self._rate)
            handle.writeframes(track.tobytes())
        return buffer.getvalue()

    def write(
        self, path: str, scenes: Sequence[Dict[str, Any]], total: float,
        release_times: Sequence[float] = (),
    ) -> str:
        """Compose the score and write it to *path*.

        Args:
            path: Destination WAV path.
            scenes: Scene dictionaries with kind, start and dur.
            total: Video duration in seconds.
            release_times: Video-clock seconds at which releases land.

        Returns:
            The written path.
        """
        Path(path).write_bytes(self.compose(scenes, total, release_times))
        return str(path)

    def _bed(self, scenes: Sequence[Dict[str, Any]], frames: int) -> array.array:
        """Lay the looped music bed under every scene.

        The loop restarts on the first frame of each scene outside
        VIDEO_AUDIO_CONTINUE_KINDS, so the downbeat lands on the cut;
        the previous texture crossfades out underneath.
        """
        cfg = self.config
        track = array.array("h")
        fade = max(0, int(round(float(cfg.VIDEO_AUDIO_CROSSFADE_S) * self._rate)))
        previous: Tuple[array.array, int] = (array.array("h"), 0)
        phase = 0
        for index, scene in enumerate(scenes):
            start = min(frames, int(round(float(scene["start"]) * self._rate)))
            end = min(frames, int(round((float(scene["start"]) + float(scene["dur"])) * self._rate)))
            count = end - start
            if count <= 0:
                continue
            loop = self._loop(self.level(scene["kind"]))
            if scene["kind"] not in cfg.VIDEO_AUDIO_CONTINUE_KINDS:
                phase = 0
            segment = self._tile(loop, phase, count)
            old_loop, old_phase = previous
            blend = min(fade, count) if index > 0 and len(old_loop) else 0
            if blend:
                tail = self._tile(old_loop, old_phase, blend)
                for i in range(blend * CHANNELS):
                    mix = (i // CHANNELS) / blend
                    segment[i] = int(tail[i] * (1.0 - mix) + segment[i] * mix)
            track.extend(segment)
            phase = (phase + count) % (len(loop) // CHANNELS)
            previous = (loop, phase)
        missing = frames * CHANNELS - len(track)
        if missing > 0:
            track.extend(array.array("h", bytes(missing * SAMPLE_WIDTH)))
        return track

    @staticmethod
    def _tile(loop: array.array, phase: int, frames: int) -> array.array:
        """Return *frames* stereo frames of *loop* starting at *phase*."""
        out = array.array("h")
        size = len(loop) // CHANNELS
        if size == 0:
            return array.array("h", bytes(frames * CHANNELS * SAMPLE_WIDTH))
        phase %= size
        while frames > 0:
            take = min(frames, size - phase)
            out.extend(loop[phase * CHANNELS:(phase + take) * CHANNELS])
            phase = (phase + take) % size
            frames -= take
        return out

    def _loop(self, level: float) -> array.array:
        """Return the interleaved stereo loop mixed for one energy level."""
        key = round(level, 3)
        if key in self._loops:
            return self._loops[key]
        cfg = self.config
        stems = self._all_stems()
        gains = dict(cfg.VIDEO_AUDIO_STEM_GAINS)
        weight = {name: float(gains.get(name, 0.0)) * self.stem_weight(name, key) for name in STEMS}
        size = len(stems["pad"])
        scale = float(cfg.VIDEO_AUDIO_MASTER_GAIN) * PCM_PEAK
        pad, bass, drums, arp = (stems[name] for name in STEMS)
        wp, wb, wd, wa = (weight[name] for name in STEMS)
        center = [pad[i] * wp + bass[i] * wb + drums[i] * wd for i in range(size)]
        delay = int(round(float(cfg.VIDEO_AUDIO_STEREO_DELAY_MS) * self._rate / 1000.0)) % max(1, size)
        loop = array.array("h", bytes(size * CHANNELS * SAMPLE_WIDTH))
        for i in range(size):
            loop[2 * i] = _clamp_pcm((center[i] + arp[i] * wa) * scale)
            loop[2 * i + 1] = _clamp_pcm((center[i] + arp[i - delay] * wa) * scale)
        self._loops[key] = loop
        return loop

    def _all_stems(self) -> Dict[str, List[float]]:
        """Synthesize every stem once (peak-normalised mono loops)."""
        if not self._stems:
            noise = random.Random(int(self.config.VIDEO_AUDIO_SEED))
            self._stems = {
                "pad": _normalized(self._pad()),
                "bass": _normalized(self._bass()),
                "drums": _normalized(self._drums(noise)),
                "arp": _normalized(self._arp()),
            }
        return self._stems

    def _chords(self) -> List[Tuple[int, int]]:
        """Return (root offset, third interval) for every bar of the loop."""
        progression = tuple(self.config.VIDEO_AUDIO_PROGRESSION) or ((0, "minor"),)
        return [(int(offset), THIRDS.get(quality, THIRDS["minor"])) for offset, quality in progression]

    def _pad(self) -> List[float]:
        """Slow detuned triad per bar with a raised-sine swell."""
        root = float(self.config.VIDEO_AUDIO_ROOT_HZ) * 4.0
        out: List[float] = []
        for offset, third in self._chords():
            steps = [
                TWO_PI * _semitone(root, offset + interval) * detune / self._rate
                for interval in (0, third, 7)
                for detune in (0.997, 1.003)
            ]
            for i in range(self._bar):
                swell = math.sin(math.pi * i / self._bar) ** 0.5
                out.append(swell * sum(math.sin(step * i) for step in steps))
        return out

    def _bass(self) -> List[float]:
        """Pulsing eighth-note bass on the chord root."""
        root = float(self.config.VIDEO_AUDIO_ROOT_HZ) * 2.0
        note = self._step * 2
        attack = max(1, int(0.004 * self._rate))
        out: List[float] = []
        for offset, _third in self._chords():
            step = TWO_PI * _semitone(root, offset) / self._rate
            for i in range(self._bar):
                k = i % note
                envelope = min(1.0, k / attack) * math.exp(-5.0 * k / self._rate)
                phase = step * k
                out.append(envelope * (
                    math.sin(phase) + 0.5 * math.sin(2 * phase)
                    + 0.33 * math.sin(3 * phase) + 0.2 * math.sin(4 * phase)
                ))
        return out

    def _drums(self, noise: random.Random) -> List[float]:
        """Four-on-the-floor kick, backbeat snare and offbeat hats for one bar, tiled."""
        rate = self._rate
        bar = [0.0] * self._bar
        hiss = [noise.uniform(-1.0, 1.0) for _ in range(self._beat)]
        for beat in range(BEATS_PER_BAR):
            base = beat * self._beat
            phase = 0.0
            for k in range(self._beat):
                t = k / rate
                phase += TWO_PI * (45.0 + 110.0 * math.exp(-30.0 * t)) / rate
                bar[base + k] += math.sin(phase) * math.exp(-9.0 * t)
                if beat % 2 == 1:
                    bar[base + k] += 0.5 * hiss[k] * math.exp(-18.0 * t)
                    bar[base + k] += 0.3 * math.sin(TWO_PI * 180.0 * t) * math.exp(-25.0 * t)
            hat = base + self._step * 2
            for k in range(1, self._step * 2):
                t = k / rate
                bar[hat + k] += 0.22 * (hiss[k] - hiss[k - 1]) * math.exp(-60.0 * t)
        return bar * len(self._chords())

    def _arp(self) -> List[float]:
        """Sixteenth-note arpeggio over the chord tones with a dotted echo."""
        root = float(self.config.VIDEO_AUDIO_ROOT_HZ) * 8.0
        dry: List[float] = []
        for offset, third in self._chords():
            pattern = (0, 7, 12, third + 12, 7, 12, third + 12, 19)
            for index in range(STEPS_PER_BEAT * BEATS_PER_BAR):
                step = TWO_PI * _semitone(root, offset + pattern[index % len(pattern)]) / self._rate
                for k in range(self._step):
                    envelope = math.exp(-11.0 * k / self._rate)
                    dry.append(envelope * (math.sin(step * k) + 0.3 * math.sin(2 * step * k)))
        echo = self._step * 3
        return [dry[i] + 0.35 * dry[i - echo] for i in range(len(dry))]

    def _event(self, cue: AudioCue) -> List[float]:
        """Synthesize the mono samples of one cue, already gain-scaled."""
        builders: Dict[str, Callable[[AudioCue], List[float]]] = {
            "impact": self._impact, "riser": self._riser, "ping": self._ping,
        }
        builder = builders.get(cue.kind)
        return builder(cue) if builder else []

    def _impact(self, cue: AudioCue) -> List[float]:
        """Sub drop with a filtered noise burst."""
        cfg = self.config
        rate = self._rate
        gain = float(cfg.VIDEO_AUDIO_IMPACT_GAIN)
        noise = random.Random(int(cfg.VIDEO_AUDIO_SEED) + 1)
        out: List[float] = []
        phase = 0.0
        low = 0.0
        for k in range(int(float(cfg.VIDEO_AUDIO_IMPACT_S) * rate)):
            t = k / rate
            phase += TWO_PI * (38.0 + 90.0 * math.exp(-14.0 * t)) / rate
            low += 0.12 * (noise.uniform(-1.0, 1.0) - low)
            out.append(gain * (math.sin(phase) * math.exp(-3.5 * t) + 1.6 * low * math.exp(-10.0 * t)))
        return out

    def _riser(self, cue: AudioCue) -> List[float]:
        """Rising sweep with swelling noise that ends on the cut."""
        cfg = self.config
        rate = self._rate
        gain = float(cfg.VIDEO_AUDIO_RISER_GAIN)
        noise = random.Random(int(cfg.VIDEO_AUDIO_SEED) + 2)
        count = int(float(cfg.VIDEO_AUDIO_RISER_S) * rate)
        out: List[float] = []
        phase = 0.0
        last = 0.0
        for k in range(count):
            progress = k / max(1, count)
            phase += TWO_PI * 220.0 * (2.0 ** (3.0 * progress)) / rate
            sample = noise.uniform(-1.0, 1.0)
            out.append(gain * progress * progress * (0.5 * math.sin(phase) + 0.6 * (sample - last)))
            last = sample
        return out

    def _ping(self, cue: AudioCue) -> List[float]:
        """Short bell at the cue pitch."""
        cfg = self.config
        rate = self._rate
        gain = float(cfg.VIDEO_AUDIO_PING_GAIN)
        step = TWO_PI * cue.pitch / rate
        out: List[float] = []
        for k in range(int(float(cfg.VIDEO_AUDIO_PING_S) * rate)):
            t = k / rate
            out.append(gain * (
                math.sin(step * k) * math.exp(-7.0 * t)
                + 0.3 * math.sin(2 * step * k) * math.exp(-10.0 * t)
            ))
        return out

    def _overlay(self, track: array.array, start: int, samples: List[float]) -> None:
        """Add mono *samples* to both channels of *track* from frame *start*."""
        frames = len(track) // CHANNELS
        scale = float(self.config.VIDEO_AUDIO_MASTER_GAIN) * PCM_PEAK
        for offset, sample in enumerate(samples):
            frame = start + offset
            if frame < 0:
                continue
            if frame >= frames:
                break
            value = sample * scale
            track[2 * frame] = _clamp_pcm(track[2 * frame] + value)
            track[2 * frame + 1] = _clamp_pcm(track[2 * frame + 1] + value)

    def _fade(self, track: array.array, frames: int) -> None:
        """Apply the master fade in and fade out in place."""
        cfg = self.config
        fade_in = min(frames, int(float(cfg.VIDEO_AUDIO_FADE_IN_S) * self._rate))
        fade_out = min(frames, int(float(cfg.VIDEO_AUDIO_FADE_OUT_S) * self._rate))
        for frame in range(fade_in):
            gain = frame / fade_in
            track[2 * frame] = int(track[2 * frame] * gain)
            track[2 * frame + 1] = int(track[2 * frame + 1] * gain)
        for k in range(fade_out):
            frame = frames - 1 - k
            gain = k / fade_out
            track[2 * frame] = int(track[2 * frame] * gain)
            track[2 * frame + 1] = int(track[2 * frame + 1] * gain)
