"""Cinematic codebase overview video, general purpose.

Renders a short synthwave explainer for any project analysed by
readmenator, in the visual language of the miniGCC self-host video
(neon HUD panels, striped sun, scrolling grid, bloom, scanlines,
chromatic text, glitch transitions). Every number on screen comes
from a real scan: file/symbol/import counts, detected layers, god
nodes, communities, the resolved import graph, per-file hash colors
and top security findings.

Zero tokens: pure PIL frame drawing piped to ffmpeg. Optional
dependency: when PIL or ffmpeg is missing the caller skips with a
warning instead of failing the rebuild.
"""

from __future__ import annotations

import colorsys
import hashlib
import math
import multiprocessing
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._graphlayout import (
    BundleLayout,
    ForceAtlas2Settings,
    SphereBundleLayout,
    fit_frames,
    forceatlas2_frames,
    hierarchical_edge_bundling,
    interpolate_frames,
    normalize_cloud,
    spherical_edge_bundling,
)
from readmenator._models import AnalysisResult, AnalysisResultV2, Edge, Node, SecurityFinding
from readmenator._rank import file_pagerank

BG_TOP = (6, 3, 16)
BG_HORIZON = (34, 6, 52)
PANEL_FILL = (10, 7, 26, 225)
PANEL_HEAD = (22, 12, 48, 240)
TXT = (222, 220, 255)
DIM = (130, 120, 180)
FAINT = (80, 70, 125)
MAGENTA = (255, 46, 151)
CYAN = (0, 234, 255)
YELLOW = (255, 225, 60)
GREEN = (57, 255, 136)
ORANGE = (255, 140, 50)
VIOLET = (170, 100, 255)
RED = (255, 60, 90)

COMMUNITY_PALETTE = (
    (0, 234, 255), (255, 46, 151), (57, 255, 136), (255, 225, 60),
    (170, 100, 255), (255, 140, 50), (90, 160, 255), (255, 110, 200),
)

LAYER_COLORS = {
    "presentation": (0, 234, 255),
    "business_logic": (57, 255, 136),
    "data_access": (170, 100, 255),
    "infrastructure": (255, 225, 60),
    "testing": (255, 140, 50),
    "utility": (130, 120, 180),
}

ACT_CARDS = {
    "I": ("ACT I", "ARCHITECTURAL LAYERS", "where each file lives"),
    "II": ("ACT II", "GOD NODES", "ranked by measured connections + symbols"),
    "III": ("ACT III", "THE BLAST RADIUS", "who breaks when the hub changes, grown by BFS"),
    "IV": ("ACT IV", "COMMUNITIES", "import neighbourhoods, and why they stick"),
    "V": ("ACT V", "EMERGENCE", "ForceAtlas2 LinLog: the structure finds its own shape"),
    "VI": ("ACT VI", "ORBIT", "the force graph in 3D, flown community by community"),
    "VII": ("ACT VII", "THE WIRING", "hierarchical edge bundling between communities"),
    "VIII": ("ACT VIII", "THE SPHERE", "every import bundled through a globe of communities"),
    "IX": ("ACT IX", "CODE DNA", "each file becomes a color"),
}

COLOR_MODES = ("community", "layer", "language")

_RENDER_D: Optional[Dict[str, Any]] = None
_RENDER_SCENES: List[Dict[str, Any]] = []
_RENDER_TOTAL: float = 0.0
_RENDER_BD: Any = None
_RENDER_FONTS: Optional[Dict[str, Any]] = None
_RENDER_CFG: Optional[Config] = None


def ease(x: float) -> float:
    """Smoothstep clamped to [0, 1]."""
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def fmt_int(n: int) -> str:
    """Group thousands with commas."""
    return f"{n:,}"


def mix(a: Tuple[int, int, int], b: Tuple[int, int, int], t: float) -> Tuple[int, int, int]:
    """Linear blend of two RGB colors."""
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def alpha(c: Tuple[int, int, int], a: float) -> Tuple[int, int, int, int]:
    """RGB color plus an alpha in [0, 1] as an RGBA tuple."""
    return (c[0], c[1], c[2], max(0, min(255, int(255 * a))))


def hash_color(digest: bytes) -> Tuple[int, int, int]:
    """Neon color derived from a digest: the file fingerprint."""
    h = int.from_bytes(digest[:2], "big") / 65535.0
    s = 0.65 + 0.35 * digest[2] / 255.0
    v = 0.80 + 0.20 * digest[3] / 255.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (int(r * 255), int(g * 255), int(b * 255))


def short_label(text: str, limit: int) -> str:
    """Truncate a label to a character budget without newlines."""
    clean = " ".join(str(text).split())
    if len(clean) <= limit:
        return clean
    return clean[: max(0, limit - 1)] + "…"


def _panel(cfg: Config) -> Tuple[int, int, int, int]:
    """Main content panel fitted to the configured canvas."""
    return (30, 90, cfg.VIDEO_WIDTH - 30, cfg.VIDEO_HEIGHT - 60)


def _caption_y(cfg: Config) -> int:
    """Y coordinate of the lower-third narration line."""
    return cfg.VIDEO_HEIGHT - 40


def _graph_boxes(cfg: Config) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
    """Graph panel plus telemetry side panel fitted to the canvas."""
    side_w = min(260, cfg.VIDEO_WIDTH // 4)
    return (
        (30, 90, cfg.VIDEO_WIDTH - side_w - 20, cfg.VIDEO_HEIGHT - 60),
        (cfg.VIDEO_WIDTH - side_w, 90, cfg.VIDEO_WIDTH - 30, cfg.VIDEO_HEIGHT - 60),
    )


def _dna_boxes(cfg: Config) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
    """DNA grid panel plus security side panel fitted to the canvas."""
    side_w = min(280, cfg.VIDEO_WIDTH // 4)
    return (
        (30, 90, cfg.VIDEO_WIDTH - side_w - 20, cfg.VIDEO_HEIGHT - 60),
        (cfg.VIDEO_WIDTH - side_w, 90, cfg.VIDEO_WIDTH - 30, cfg.VIDEO_HEIGHT - 60),
    )


def _split_boxes(cfg: Config) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
    """Left content panel plus right detail panel fitted to the canvas."""
    right_w = min(430, cfg.VIDEO_WIDTH // 3)
    return (
        (30, 90, cfg.VIDEO_WIDTH - right_w - 20, cfg.VIDEO_HEIGHT - 60),
        (cfg.VIDEO_WIDTH - right_w, 90, cfg.VIDEO_WIDTH - 30, cfg.VIDEO_HEIGHT - 60),
    )


def community_color(index: int) -> Tuple[int, int, int]:
    """Neon color for a community index (grey for unassigned)."""
    if index < 0:
        return DIM
    return COMMUNITY_PALETTE[index % len(COMMUNITY_PALETTE)]


def _polyline_point(points: List[Tuple[float, float]], f: float) -> Tuple[float, float]:
    """Point at fraction f along a sampled polyline (by index)."""
    if not points:
        return (0.0, 0.0)
    pos = max(0.0, min(1.0, f)) * (len(points) - 1)
    i = int(pos)
    j = min(i + 1, len(points) - 1)
    t = pos - i
    return (points[i][0] + (points[j][0] - points[i][0]) * t, points[i][1] + (points[j][1] - points[i][1]) * t)


def project3d(
    p: Tuple[float, ...],
    yaw: float,
    pitch: float,
    target: Tuple[float, ...],
    scale: float,
    center: Tuple[float, float],
    perspective: float,
) -> Tuple[float, float, float, float]:
    """Project a 3D point through an orbiting perspective camera.

    The camera looks at target from the -z side after rotating the
    world by yaw (around y) and pitch (around x).

    Returns:
        Screen x, screen y, view depth (smaller is nearer), and the
        perspective scale factor.
    """
    x, y, z = p[0] - target[0], p[1] - target[1], p[2] - target[2]
    cy, sy = math.cos(yaw), math.sin(yaw)
    cp, sp = math.cos(pitch), math.sin(pitch)
    x1 = x * cy + z * sy
    z1 = -x * sy + z * cy
    y2 = y * cp - z1 * sp
    z2 = y * sp + z1 * cp
    k = perspective / max(0.2, perspective + z2)
    return (center[0] + x1 * scale * k, center[1] + y2 * scale * k, z2, k)


def _depth_alpha(z: float, fade: float) -> float:
    """Opacity multiplier that fades points further from the camera."""
    return 1.0 - fade * max(0.0, min(1.0, (z + 1.0) / 2.0))


def _language_color(language: str) -> Tuple[int, int, int]:
    """Stable neon color for a language name."""
    return hash_color(hashlib.sha256(language.encode("utf-8", "replace")).digest())


def mode_color(data: Dict[str, Any], nid: str, mode: str) -> Tuple[int, int, int]:
    """Node color under an explorer color mode (community, layer, language)."""
    if mode == "layer":
        return LAYER_COLORS.get(data.get("node_layer", {}).get(nid, ""), DIM)
    if mode == "language":
        return _language_color(data.get("node_language", {}).get(nid, "unknown"))
    return community_color(data.get("membership", {}).get(nid, -1))


def _lerp3(a: Tuple[float, ...], b: Tuple[float, ...], t: float) -> Tuple[float, float, float]:
    """Linear blend of two 3D points."""
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t)


def _camera_track(keys: List[Tuple[float, Tuple[float, ...], float]], f: float) -> Tuple[Tuple[float, float, float], float]:
    """Eased camera target and zoom at progress f from (time, target, zoom) keys."""
    if f <= keys[0][0]:
        return (tuple(keys[0][1]), keys[0][2])
    for (t0, p0, z0), (t1, p1, z1) in zip(keys, keys[1:]):
        if t0 <= f <= t1:
            u = ease((f - t0) / max(1e-9, t1 - t0))
            return (_lerp3(p0, p1, u), z0 + (z1 - z0) * u)
    return (tuple(keys[-1][1]), keys[-1][2])


def _place_label(d: Any, placed: List[Tuple[float, float, float, float]], x: float, y: float, text: str,
                 font: Any, col: Tuple[int, int, int], a: float) -> None:
    """Draw a boxed label beside a point unless it collides with one already placed."""
    w = font.getlength(text)
    rect = (x + 8, y - 18, x + 16 + w, y)
    if any(not (rect[2] < q[0] or q[2] < rect[0] or rect[3] < q[1] or q[3] < rect[1]) for q in placed):
        return
    placed.append(rect)
    d.rectangle(rect, fill=(6, 3, 18, int(210 * a)), outline=alpha(col, 0.7 * a))
    d.text((x + 12, y - 16), text, font=font, fill=alpha(TXT, a))


def _clipped(img: Any, box: Tuple[int, int, int, int], paint: Any) -> None:
    """Run paint(draw, local_box) on a crop of img and paste it back (clips to box)."""
    from PIL import ImageDraw

    x0, y0, x1, y1 = (int(v) for v in box)
    if x1 <= x0 or y1 <= y0:
        return
    crop = img.crop((x0, y0, x1, y1))
    paint(ImageDraw.Draw(crop, "RGBA"), (0, 0, x1 - x0, y1 - y0))
    img.paste(crop, (x0, y0))


def draw_cloud3d(
    img: Any,
    data: Dict[str, Any],
    box: Tuple[int, int, int, int],
    cfg: Config,
    yaw: float,
    pitch: float,
    target: Tuple[float, ...],
    zoom: float,
    mode: str,
    lit_nodes: Optional[set],
    edge_lit: Optional[Any],
    gt: float,
    fonts: Dict[str, Any],
    appear: float = 1.0,
    labels: int = 0,
) -> None:
    """Draw the 3D force graph (graph-force 3D view) through an orbiting camera.

    Drawing is clipped to box.

    Args:
        img: Frame image.
        data: Collected scene data with orbit_pos.
        box: Pixel box the cloud is fitted into.
        cfg: Video settings.
        yaw: Camera yaw in radians.
        pitch: Camera pitch in radians.
        target: Look-at point in layout space.
        zoom: Scale multiplier.
        mode: Color mode (community, layer, language).
        lit_nodes: Highlighted node ids, or None for no focus.
        edge_lit: Predicate (a, b) -> bool for highlighted edges, or None.
        gt: Global time for particles and pulses.
        fonts: Font set.
        appear: Assembly progress in [0, 1] (nodes grow out of the center).
        labels: Number of PageRank-ranked labels to place.
    """
    if not data.get("orbit_pos"):
        return
    _clipped(img, box, lambda d, local: _cloud_core(d, data, local, cfg, yaw, pitch, target, zoom, mode,
                                                     lit_nodes, edge_lit, gt, fonts, appear, labels))


def _cloud_core(
    d: Any,
    data: Dict[str, Any],
    box: Tuple[int, int, int, int],
    cfg: Config,
    yaw: float,
    pitch: float,
    target: Tuple[float, ...],
    zoom: float,
    mode: str,
    lit_nodes: Optional[set],
    edge_lit: Optional[Any],
    gt: float,
    fonts: Dict[str, Any],
    appear: float,
    labels: int,
) -> None:
    """Paint the 3D force graph into a local box (see draw_cloud3d)."""
    pos: Dict[str, Tuple[float, float, float]] = data.get("orbit_pos", {})
    rank: Dict[str, float] = data.get("rank", {})
    top_rank = max([1e-9] + list(rank.values()))
    x0, y0, x1, y1 = box
    persp = cfg.VIDEO_ORBIT_PERSPECTIVE
    scale = min(x1 - x0, y1 - y0) / 2 * 0.8 * zoom
    center = ((x0 + x1) / 2, (y0 + y1) / 2)
    grow = ease(appear)
    proj = {nid: project3d((p[0] * grow, p[1] * grow, p[2] * grow), yaw, pitch, target, scale, center, persp)
            for nid, p in pos.items()}
    fade = cfg.VIDEO_ORBIT_DEPTH_FADE
    links = data["graph_links"]
    hot: List[Tuple[str, str]] = []
    for a, b in links:
        if a not in proj or b not in proj or a == b:
            continue
        pa, pb = proj[a], proj[b]
        on = edge_lit is None or edge_lit(a, b)
        if on and edge_lit is not None:
            hot.append((a, b))
            continue
        depth = _depth_alpha((pa[2] + pb[2]) / 2, fade)
        strength = (0.22 if edge_lit is None else 0.05) * depth * grow
        d.line((pa[0], pa[1], pb[0], pb[1]), fill=alpha(mode_color(data, a, mode), strength), width=1)
    for k, (a, b) in enumerate(hot):
        pa, pb = proj[a], proj[b]
        depth = _depth_alpha((pa[2] + pb[2]) / 2, fade)
        d.line((pa[0], pa[1], pb[0], pb[1]), fill=alpha(mode_color(data, a, mode), 0.75 * depth), width=2)
    for k, (a, b) in enumerate(hot[: cfg.VIDEO_SURFERS]):
        pa, pb = proj[a], proj[b]
        f = (gt * 0.6 + _packet_offset(a, b, k)) % 1.0
        x, y = pa[0] + (pb[0] - pa[0]) * f, pa[1] + (pb[1] - pa[1]) * f
        d.ellipse((x - 2.5, y - 2.5, x + 2.5, y + 2.5), fill=alpha((255, 255, 255), 0.9))
    order = sorted(proj, key=lambda nid: -proj[nid][2])
    for nid in order:
        x, y, z, k = proj[nid]
        if not (x0 - 20 < x < x1 + 20 and y0 - 20 < y < y1 + 20):
            continue
        weight = math.sqrt(rank.get(nid, 0.0) / top_rank)
        r = (2.0 + 7.0 * weight) * k * math.sqrt(zoom) * (0.3 + 0.7 * grow)
        on = lit_nodes is None or nid in lit_nodes
        a = (0.95 if on else 0.18) * _depth_alpha(z, fade)
        col = mode_color(data, nid, mode)
        if on and lit_nodes is not None and weight > 0.3:
            glow = r + 5 + 2 * math.sin(gt * 3 + weight * 5)
            d.ellipse((x - glow, y - glow, x + glow, y + glow), fill=alpha(col, 0.2 * a))
        d.ellipse((x - r, y - r, x + r, y + r), fill=alpha(col, a), outline=alpha((255, 255, 255), 0.45 * a), width=1)
    if labels > 0 and grow >= 1:
        placed: List[Tuple[float, float, float, float]] = []
        pool = [nid for nid in proj if lit_nodes is None or nid in lit_nodes]
        for nid in sorted(pool, key=lambda n: (-rank.get(n, 0.0), n))[:labels]:
            x, y, z, _k = proj[nid]
            if z > 0.4 or not (x0 < x < x1 - 120 and y0 + 20 < y < y1):
                continue
            _place_label(d, placed, x, y, short_label(nid.rpartition("/")[2] or nid, 22), fonts["tiny_b"],
                         mode_color(data, nid, mode), _depth_alpha(z, fade))


def draw_sphere3d(
    img: Any,
    data: Dict[str, Any],
    box: Tuple[int, int, int, int],
    cfg: Config,
    yaw: float,
    pitch: float,
    morph: float,
    reveal: float,
    spot: Optional[int],
    gt: float,
    fonts: Dict[str, Any],
    group_labels: bool = True,
) -> None:
    """Draw the bundled sphere, optionally morphing out of the 3D force layout.

    Drawing is clipped to box.

    Args:
        img: Frame image.
        data: Collected scene data with sphere and orbit_pos.
        box: Pixel box the sphere is fitted into.
        cfg: Video settings.
        yaw: Camera yaw in radians.
        pitch: Camera pitch in radians.
        morph: 0 = force layout positions, 1 = sphere positions.
        reveal: Fraction of each bundled curve drawn.
        spot: Community index in the spotlight, or None.
        gt: Global time for particles.
        fonts: Font set.
        group_labels: Draw cap labels when the morph is complete.
    """
    layout: Optional[SphereBundleLayout] = data.get("sphere")
    if layout is None or not layout.leaves:
        return
    _clipped(img, box, lambda d, local: _sphere_core(d, data, layout, local, cfg, yaw, pitch, morph,
                                                      reveal, spot, gt, fonts, group_labels))


def _sphere_core(
    d: Any,
    data: Dict[str, Any],
    layout: SphereBundleLayout,
    box: Tuple[int, int, int, int],
    cfg: Config,
    yaw: float,
    pitch: float,
    morph: float,
    reveal: float,
    spot: Optional[int],
    gt: float,
    fonts: Dict[str, Any],
    group_labels: bool,
) -> None:
    """Paint the bundled sphere into a local box (see draw_sphere3d)."""
    membership: Dict[str, int] = data.get("membership", {})
    rank: Dict[str, float] = data.get("rank", {})
    top_rank = max([1e-9] + list(rank.values()))
    orbit: Dict[str, Tuple[float, float, float]] = data.get("orbit_pos", {})
    x0, y0, x1, y1 = box
    persp = cfg.VIDEO_ORBIT_PERSPECTIVE
    scale = min(x1 - x0, y1 - y0) / 2 * 0.7
    center = ((x0 + x1) / 2, (y0 + y1) / 2)
    origin = (0.0, 0.0, 0.0)
    fade = cfg.VIDEO_ORBIT_DEPTH_FADE
    m = ease(morph)

    def pr(p: Tuple[float, ...]) -> Tuple[float, float, float, float]:
        """Project a layout point through the scene camera."""
        return project3d(p, yaw, pitch, origin, scale, center, persp)

    if m > 0:
        for lat in (-60, -30, 0, 30, 60):
            c, sn = math.cos(math.radians(lat)), math.sin(math.radians(lat))
            ring = [pr((c * math.cos(t * math.pi / 24), sn, c * math.sin(t * math.pi / 24))) for t in range(49)]
            d.line([(q[0], q[1]) for q in ring], fill=alpha(FAINT, 0.35 * m), width=1)
    pos = {nid: _lerp3(orbit.get(nid, leaf), leaf, m) for nid, leaf in layout.leaves.items()}
    proj = {nid: pr(p) for nid, p in pos.items()}
    if reveal < 1:
        for a, b in data["graph_links"]:
            if a in proj and b in proj and a != b:
                pa, pb = proj[a], proj[b]
                d.line((pa[0], pa[1], pb[0], pb[1]),
                       fill=alpha(community_color(membership.get(a, -1)), 0.2 * (1 - reveal)), width=1)
    if reveal > 0:
        hot: List[Tuple[int, List[Tuple[float, float]]]] = []
        for k, (a, b, pts) in enumerate(layout.curves):
            ca, cb = membership.get(a, -1), membership.get(b, -1)
            stop = max(2, int(math.ceil(len(pts) * reveal)))
            q = [pr(p) for p in pts[:stop]]
            depth = _depth_alpha(sum(v[2] for v in q) / len(q), fade)
            lit = spot is None or spot in (ca, cb)
            flat = [(v[0], v[1]) for v in q]
            if spot is not None and lit:
                hot.append((k, flat))
                continue
            d.line(flat, fill=alpha(community_color(ca), (0.3 if lit else 0.05) * depth), width=1)
        for k, flat in hot:
            a, b, _pts = layout.curves[k]
            d.line(flat, fill=alpha(community_color(membership.get(a, -1)), 0.8), width=2)
            if reveal >= 1 and membership.get(a, -1) != membership.get(b, -1):
                f = (gt * 0.45 + _packet_offset(a, b, k)) % 1.0
                x, y = _polyline_point(flat, f)
                d.ellipse((x - 2.5, y - 2.5, x + 2.5, y + 2.5), fill=alpha((255, 255, 255), 0.9))
    for nid in sorted(proj, key=lambda n: -proj[n][2]):
        x, y, z, k = proj[nid]
        comm = membership.get(nid, -1)
        on = spot is None or comm == spot
        r = (1.8 + 4.5 * math.sqrt(rank.get(nid, 0.0) / top_rank)) * k
        d.ellipse((x - r, y - r, x + r, y + r),
                  fill=alpha(community_color(comm), (0.95 if on else 0.25) * _depth_alpha(z, fade)))
    if group_labels and m >= 1:
        placed: List[Tuple[float, float, float, float]] = []
        for label, cap, count in layout.groups:
            index = int(label.split(":", 1)[0])
            x, y, z, _k = pr((cap[0] * 1.12, cap[1] * 1.12, cap[2] * 1.12))
            if z > 0.15 or (count < 2 and spot != index):
                continue
            name = short_label(label.split(":", 1)[1].rpartition(": ")[2] or label, 16)
            on = spot is None or spot == index
            _place_label(d, placed, x, y, f"{name} ({count})", fonts["tiny_b"], community_color(index),
                         (0.95 if on else 0.4) * _depth_alpha(z, fade))


def _verdict_badge(d: Any, box: Tuple[int, int, int, int], text: str, fonts: Dict[str, Any], lt: float, dur: float, col: Tuple[int, int, int] = GREEN) -> None:
    """Pulsing verdict badge pinned to the bottom of a panel."""
    if lt < dur - 2.6:
        return
    a = ease((lt - (dur - 2.6)) / 0.5)
    pulse = 0.5 + 0.5 * math.sin(lt * 4)
    x0, _, x1, y1 = box
    tw = fonts["small_b"].getlength(text)
    bx0 = (x0 + x1 - tw) / 2 - 24
    bx1 = (x0 + x1 + tw) / 2 + 24
    d.rectangle((bx0, y1 - 52, bx1, y1 - 14), fill=(8, 40, 26, int(230 * a)),
                outline=alpha(col, (0.6 + 0.4 * pulse) * a), width=3)
    d.text(((x0 + x1) / 2, y1 - 44), text, font=fonts["small_b"], fill=alpha(col, a), anchor="ma")


def _scan_cursor(d: Any, box: Tuple[int, int, int, int], progress: float, col: Tuple[int, int, int] = (255, 255, 255)) -> None:
    """Vertical sweep line travelling across a panel."""
    if not 0 < progress < 1:
        return
    x0, y0, x1, y1 = box
    x = x0 + 20 + (x1 - x0 - 40) * progress
    d.line((x, y0 + 36, x, y1 - 8), fill=alpha(col, 0.8), width=2)


def _code_tint(line: str) -> Tuple[int, int, int]:
    """Single-color tint for a source line: comments dim, code bright."""
    s = line.strip()
    if not s:
        return FAINT
    if s[:1] in ("#", '"', "'") or s.startswith(("//", "/*", "*", "<!--", "--")):
        return FAINT
    return TXT


def _packet_offset(a: str, b: str, k: int) -> float:
    """Deterministic phase offset for a packet travelling edge a->b."""
    digest = hashlib.md5(f"{a}>{b}#{k}".encode()).digest()
    return digest[0] / 255.0


def dependencies_available() -> bool:
    """Check that PIL and ffmpeg exist for video rendering."""
    try:
        import PIL  # noqa: F401
    except ImportError:
        return False
    return shutil.which("ffmpeg") is not None


def resolve_fonts() -> Dict[str, Any]:
    """Resolve monospace fonts through fontconfig with PIL fallback."""
    from PIL import ImageFont

    def _find(style: str) -> Optional[str]:
        """Find one font file for a style, else None."""
        for family in ("JetBrainsMono NL Nerd Font Mono", "DejaVu Sans Mono"):
            try:
                out = subprocess.run(
                    ["fc-match", "-f", "%{file}", f"{family}:style={style}"],
                    capture_output=True, text=True, check=True,
                ).stdout.strip()
            except (OSError, subprocess.CalledProcessError):
                continue
            if out and Path(out).is_file():
                return out
        return None

    reg = _find("Regular")
    bold = _find("Bold") or reg
    xbold = _find("ExtraBold") or bold or reg
    if reg is None:
        default = ImageFont.load_default()
        return {"head": default, "cap": default, "term": default,
                "small": default, "small_b": default, "mid": default,
                "big": default, "tiny": default, "tiny_b": default}
    return {
        "head": ImageFont.truetype(xbold or reg, 30),
        "cap": ImageFont.truetype(reg, 22),
        "term": ImageFont.truetype(reg, 18),
        "small": ImageFont.truetype(reg, 15),
        "small_b": ImageFont.truetype(bold or reg, 15),
        "mid": ImageFont.truetype(xbold or reg, 34),
        "big": ImageFont.truetype(xbold or reg, 52),
        "tiny": ImageFont.truetype(reg, 12),
        "tiny_b": ImageFont.truetype(bold or reg, 12),
    }


class Backdrop:
    """Precomputed synthwave background with sun and CRT mask."""

    def __init__(self, width: int, height: int) -> None:
        """Build the gradient sky, star field, sun and CRT mask."""
        from PIL import Image, ImageChops, ImageDraw

        self.width = width
        self.height = height
        self.base = Image.new("RGB", (width, height))
        px = self.base.load()
        horizon = int(height * 0.64)
        for y in range(height):
            if y <= horizon:
                t = min(1.0, y / max(1, horizon)) ** 1.6
                c = mix(BG_TOP, BG_HORIZON, t)
            else:
                t = min(1.0, (y - horizon) / max(1, height - horizon) * 1.5)
                c = mix(BG_HORIZON, BG_TOP, t)
            for x in range(width):
                px[x, y] = c
        d = ImageDraw.Draw(self.base)
        seed = 12345
        for _ in range(220):
            seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
            x = seed % width
            seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
            y = seed % max(1, horizon)
            seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
            b = 60 + seed % 140
            d.point((x, y), fill=(b, b, min(255, b + 40)))
        self.horizon = horizon
        mask = Image.new("L", (width, height), 255)
        md = ImageDraw.Draw(mask)
        for y in range(0, height, 3):
            md.line((0, y, width, y), fill=204)
        vig = Image.radial_gradient("L").resize((width, height))
        vig = vig.point(lambda v: int(255 - 0.55 * max(0, v - 90) * 255 / 165))
        self.mask = ImageChops.multiply(mask, vig).convert("RGB")
        self.sun = self._sun(min(240, height // 4))

    def _sun(self, r: int) -> Any:
        """Build the striped synthwave sun sprite."""
        from PIL import Image, ImageDraw

        sun = Image.new("RGBA", (2 * r, 2 * r), (0, 0, 0, 0))
        d = ImageDraw.Draw(sun)
        for y in range(2 * r):
            half = math.sqrt(max(0, r * r - (y - r) ** 2))
            c = mix((255, 220, 80), (255, 40, 140), y / max(1, 2 * r))
            band = y > r * 0.9 and int((y - r * 0.9) / 12) % 2 == 1
            if not band:
                d.line((r - half, y, r + half, y), fill=c + (255,))
        return sun


def _img() -> Any:
    """Import PIL Image lazily for optional-dependency support."""
    from PIL import Image

    return Image


def draw_grid(img: Any, t: float, strength: float, bd: Backdrop) -> None:
    """Draw the scrolling perspective grid below the horizon."""
    if strength <= 0:
        return
    from PIL import ImageDraw

    d = ImageDraw.Draw(img, "RGBA")
    w, h, hz = bd.width, bd.height, bd.horizon
    col = alpha(MAGENTA, 0.55 * strength)
    for i in range(-20, 21):
        d.line((w / 2 + i * 30, hz, w / 2 + i * 220, h), fill=col, width=1)
    phase = (t * 0.6) % 1.0
    for k in range(14):
        z = k + 1 - phase
        y = hz + (h - hz) * (1.0 / z) * 0.9 if z > 0 else h
        if hz < y < h:
            d.line((0, y, w, y), fill=alpha(MAGENTA, 0.6 * strength * min(1, (y - hz) / 60)), width=1)
    d.line((0, hz, w, hz), fill=alpha(CYAN, 0.5 * strength), width=2)


def draw_sun(img: Any, a: float, bd: Backdrop, cy: Optional[int] = None) -> None:
    """Paste the striped synthwave sun behind the horizon."""
    if a <= 0:
        return
    s = bd.sun
    if a < 1:
        s = s.copy()
        s.putalpha(s.getchannel("A").point(lambda v: int(v * a)))
    cy = cy if cy is not None else bd.horizon - 140
    top = cy - s.height // 2
    keep = max(0, min(s.height, bd.horizon - top))
    if keep <= 0:
        return
    s = s.crop((0, 0, s.width, keep))
    img.paste(s, (bd.width // 2 - s.width // 2, top), s)


def post(img: Any, glitch: float = 0.0, seed: int = 0) -> Any:
    """Apply bloom, scanlines, vignette and optional glitch."""
    from PIL import Image, ImageChops, ImageFilter

    w, h = img.size
    small = img.resize((max(1, w // 4), max(1, h // 4)), Image.BILINEAR)
    small = small.point(lambda v: max(0, v - 70) * 255 // 185)
    small = small.filter(ImageFilter.GaussianBlur(7))
    glow = small.resize((w, h), Image.BILINEAR).point(lambda v: int(v * 0.85))
    img = ImageChops.screen(img, glow)
    if glitch > 0:
        img = glitch_fx(img, glitch, seed)
    bd = _RENDER_BD
    if bd is not None and bd.mask.size == img.size:
        img = ImageChops.multiply(img, bd.mask)
    return img


def glitch_fx(img: Any, amount: float, seed: int) -> Any:
    """RGB split plus horizontal slice displacement."""
    from PIL import ImageChops

    w, h = img.size
    r, g, b = img.split()
    off = int(14 * amount)
    r = ImageChops.offset(r, off, 0)
    b = ImageChops.offset(b, -off, 0)
    img = _img().merge("RGB", (r, g, b))
    s = seed * 7919 + 17
    for _ in range(int(8 * amount)):
        s = (s * 1103515245 + 12345) & 0x7FFFFFFF
        y = s % h
        s = (s * 1103515245 + 12345) & 0x7FFFFFFF
        hgt = 6 + s % 50
        s = (s * 1103515245 + 12345) & 0x7FFFFFFF
        dx = (s % 120 - 60) * amount
        band = img.crop((0, y, w, min(h, y + hgt)))
        img.paste(band, (int(dx), y))
    return img


def chroma_text(img: Any, xy: Tuple[float, float], text: str, font: Any, col: Tuple[int, int, int], spread: int = 2, anchor: str = "la") -> None:
    """Draw text with red/cyan CRT chromatic aberration."""
    from PIL import ImageDraw

    d = ImageDraw.Draw(img, "RGBA")
    x, y = xy
    d.text((x - spread, y), text, font=font, fill=(255, 30, 90, 150), anchor=anchor)
    d.text((x + spread, y), text, font=font, fill=(0, 220, 255, 150), anchor=anchor)
    d.text((x, y), text, font=font, fill=col, anchor=anchor)


def hud_panel(d: Any, box: Tuple[int, int, int, int], title: str, fonts: Dict[str, Any], col: Tuple[int, int, int] = CYAN) -> None:
    """Draw a translucent HUD panel with neon edge and corner brackets."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=PANEL_FILL)
    d.rectangle((x0, y0, x1, y0 + 30), fill=PANEL_HEAD)
    d.rectangle(box, outline=alpha(col, 0.45), width=1)
    size = 18
    for (cx, cy, sx, sy) in ((x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)):
        d.line((cx, cy, cx + sx * size, cy), fill=col, width=3)
        d.line((cx, cy, cx, cy + sy * size), fill=col, width=3)
    d.text((x0 + 14, y0 + 6), title.upper(), font=fonts["small_b"], fill=col)


def draw_header(img: Any, d: Any, gt: float, total: float, project: str, act_label: str, fonts: Dict[str, Any], width: int) -> None:
    """Draw the top strip with project title, act label and progress."""
    chroma_text(img, (30, 20), project, fonts["head"], (255, 255, 255), spread=2)
    d.text((width - 30, 30), act_label, font=fonts["small_b"], fill=MAGENTA, anchor="rm")
    p = min(1.0, gt / max(0.001, total))
    d.rectangle((0, 72, width, 76), fill=(30, 15, 60))
    segs = 60
    for i in range(segs):
        x0 = width * i / segs
        if x0 > width * p:
            break
        d.rectangle((x0, 72, min(width * (i + 1) / segs, width * p), 76), fill=mix(MAGENTA, CYAN, i / segs))


def draw_caption(d: Any, text: str, lt: float, dur: float, fonts: Dict[str, Any], width: int, y: int) -> None:
    """Draw the lower-third narration line with typing effect."""
    if not text:
        return
    a = ease(lt / 0.3) * (1 - ease((lt - (dur - 0.3)) / 0.3))
    if a <= 0:
        return
    n = min(len(text), int(lt * 70))
    tw = fonts["cap"].getlength("> " + text)
    x = (width - tw) / 2
    d.rectangle((x - 20, y - 8, x + tw + 20, y + 34), fill=(10, 5, 25, int(200 * a)))
    d.line((x - 20, y - 8, x - 20, y + 34), fill=alpha(MAGENTA, a), width=3)
    d.text((x, y), "> " + text[:n], font=fonts["cap"], fill=alpha(TXT, a))


@dataclass
class CinematicVideoRenderer:
    """Builds and renders the general-purpose codebase overview video."""

    config: Config

    def collect(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: Optional[List[SecurityFinding]],
        analysis_v2: Optional[AnalysisResultV2],
        project_name: str,
        content_map: Optional[Dict[str, str]] = None,
        concept_graph: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """Collect every number each scene draws, from real scan data."""
        content_map = content_map or {}
        node_by_id: Dict[str, Node] = {n.node_id: n for n in nodes}
        file_count = len(nodes)
        symbol_count = sum(len(n.symbols) for n in nodes)
        import_count = len([e for e in edges if e.relation == "imports"])
        graph_edges = list(resolved_edges or [])
        if not graph_edges:
            graph_edges = [e for e in edges if e.relation in ("imports", "calls", "inherits")]
        languages: Dict[str, int] = {}
        for n in nodes:
            languages[n.language or "unknown"] = languages.get(n.language or "unknown", 0) + 1
        top_languages = sorted(languages.items(), key=lambda kv: -kv[1])[:4]
        layer_counts: Dict[str, int] = {}
        for fid, layer in (layers or {}).items():
            layer_counts[layer] = layer_counts.get(layer, 0) + 1
        if not layer_counts and nodes:
            layer_counts = {"business_logic": file_count}
        in_deg: Dict[str, int] = {}
        out_deg: Dict[str, int] = {}
        for e in graph_edges:
            out_deg[e.source] = out_deg.get(e.source, 0) + 1
            in_deg[e.target] = in_deg.get(e.target, 0) + 1
        god_names: List[Tuple[str, float]] = []
        if analysis and analysis.god_nodes:
            god_names = [(str(nid), float(score)) for nid, score in analysis.god_nodes[:8]]
        if not god_names:
            degree: Dict[str, int] = {}
            for nid in node_by_id:
                degree[nid] = in_deg.get(nid, 0) + out_deg.get(nid, 0) + len(node_by_id[nid].symbols)
            god_names = sorted(degree.items(), key=lambda kv: -kv[1])[:8]
        god_details: List[Dict[str, Any]] = []
        for nid, score in god_names:
            node = node_by_id.get(nid)
            god_details.append({"file": nid, "score": float(score),
                                "in": in_deg.get(nid, 0), "out": out_deg.get(nid, 0),
                                "symbols": len(node.symbols) if node else 0,
                                "language": node.language if node else ""})
        link_set = [(e.source, e.target) for e in graph_edges]
        communities: List[Dict[str, Any]] = []
        if analysis and analysis.communities:
            for c in analysis.communities[:6]:
                members = sorted(c.file_ids)
                shown = [f for f in members if f in node_by_id][:4]
                dirs: Dict[str, int] = {}
                for fid in members:
                    parent = fid.rpartition("/")[0] or "."
                    dirs[parent] = dirs.get(parent, 0) + 1
                dominant = max(sorted(dirs.items()), key=lambda kv: kv[1])[0] if dirs else "."
                member_set = set(members)
                internal = sum(1 for a, b in link_set if a in member_set and b in member_set)
                external = sum(1 for a, b in link_set
                               if (a in member_set) != (b in member_set))
                hub = max(members, key=lambda fid: in_deg.get(fid, 0) + out_deg.get(fid, 0)) if members else ""
                top_syms: List[str] = []
                for fid in ([hub] + [f for f in members if f != hub]):
                    node = node_by_id.get(fid)
                    if node:
                        for s in node.symbols:
                            if len(top_syms) >= 5:
                                break
                            top_syms.append(f"{s.name} ({s.kind} L{s.line})")
                    if len(top_syms) >= 5:
                        break
                communities.append({"label": c.label, "size": int(c.size),
                                    "cohesion": float(c.cohesion), "files": shown,
                                    "remaining": max(0, int(c.size) - len(shown)),
                                    "dominant": dominant, "internal": internal,
                                    "external": external, "hub": hub,
                                    "top_symbols": top_syms})
        hotspots: List[Dict[str, Any]] = []
        if analysis_v2 and analysis_v2.hotspots:
            for h in analysis_v2.hotspots[:6]:
                hotspots.append({"file": h.file_id, "score": float(h.combined_score)})
        cycles = len(analysis_v2.cycles) if analysis_v2 and analysis_v2.cycles else 0
        violations = len(analysis_v2.layer_violations) if analysis_v2 and analysis_v2.layer_violations else 0
        top_findings: List[Dict[str, Any]] = []
        for f in (findings or [])[:5]:
            top_findings.append({"file": f.file_path, "severity": f.severity,
                                 "rule": f.rule_id, "line": int(f.line)})
        dna: List[Dict[str, Any]] = []
        for n in nodes:
            raw = content_map.get(n.node_id)
            if raw is None:
                raw = f"{n.node_id}:{len(n.symbols)}:{n.language}"
            digest = hashlib.sha256(raw.encode("utf-8", "replace")).digest()
            dna.append({"file": n.node_id, "symbols": len(n.symbols),
                        "language": n.language, "digest": digest,
                        "color": hash_color(digest)})
        dna = sorted(dna, key=lambda r: r["file"])
        cap = self.config.VIDEO_MAX_GRAPH_NODES or file_count
        ranked_ids = [nid for nid, _ in god_names]
        keep = set(ranked_ids[:cap])
        for c in communities:
            for fid in c["files"][:3]:
                if len(keep) < cap:
                    keep.add(fid)
        if len(keep) < min(cap, file_count):
            for n in nodes:
                if len(keep) >= cap:
                    break
                keep.add(n.node_id)
        graph_nodes = [n.node_id for n in nodes if n.node_id in keep]
        graph_links = [(e.source, e.target) for e in graph_edges
                       if e.source in keep and e.target in keep]
        dep_tree = self._build_dep_tree(node_by_id, link_set, god_names)
        preview_lines: List[str] = []
        preview_file = dep_tree["root"]
        if preview_file and preview_file in content_map:
            for ln in content_map[preview_file].splitlines()[: self.config.VIDEO_PREVIEW_LINES]:
                preview_lines.append(ln[:100].expandtabs(4))
        resolved_graph = getattr(analysis_v2, "concept_graph", None) if analysis_v2 else None
        active_graph = concept_graph if concept_graph is not None else resolved_graph
        concepts: List[Dict[str, Any]] = []
        dialectic: List[str] = []
        if active_graph is not None and getattr(active_graph, "concepts", None):
            for concept in list(active_graph.concepts)[:12]:
                concepts.append({
                    "name": concept.name,
                    "files": len(concept.file_ids),
                    "mentions": concept.mention_count,
                })
            dialectic = list(getattr(active_graph, "dialectic_questions", []) or [])[:3]
        membership: Dict[str, int] = {}
        community_labels: List[str] = []
        if analysis and analysis.communities:
            for index, community in enumerate(analysis.communities):
                community_labels.append(community.label)
                for fid in community.file_ids:
                    membership[fid] = index
        rank = file_pagerank([n.node_id for n in nodes], link_set,
                             self.config.RANKING_ALPHA, self.config.RANKING_MAX_ITER,
                             self.config.RANKING_TOLERANCE)
        return {"project": short_label(project_name, 40), "files": file_count,
                "membership": membership, "community_labels": community_labels,
                "rank": rank,
                "symbols": symbol_count, "imports": import_count,
                "languages": top_languages, "layers": layer_counts,
                "gods": god_names, "god_details": god_details,
                "communities": communities,
                "hotspots": hotspots, "cycles": cycles,
                "violations": violations, "findings": top_findings,
                "dna": dna, "graph_nodes": graph_nodes,
                "graph_links": graph_links, "dep_tree": dep_tree,
                "preview_file": preview_file, "preview_lines": preview_lines,
                "concepts": concepts, "dialectic": dialectic,
                "node_layer": {nid: (layers or {}).get(nid, "unknown") for nid in node_by_id},
                "node_language": {nid: node.language or "unknown" for nid, node in node_by_id.items()},
                "node_symbols": {nid: [(s.name, s.kind, s.line) for s in node.symbols[:12]]
                                 for nid, node in node_by_id.items() if node.symbols}}

    def _build_dep_tree(
        self,
        node_by_id: Dict[str, Node],
        link_set: List[Tuple[str, str]],
        god_names: List[Tuple[str, float]],
    ) -> Dict[str, Any]:
        """Grow the blast-radius tree: BFS over files that import the hub.

        Edges point from a file to the files that depend on it, so the
        tree shows who breaks when the hub changes. Every dependent is
        kept (VIDEO_TREE_MAX_NODES 0 = no limit); children are ordered by
        their own fan-in so the most critical branches come first.
        """
        cfg = self.config
        dependents: Dict[str, List[str]] = {}
        imports: Dict[str, List[str]] = {}
        for a, b in link_set:
            if a in node_by_id and b in node_by_id and a != b:
                dependents.setdefault(b, []).append(a)
                imports.setdefault(a, []).append(b)
        root = ""
        for nid, _ in god_names:
            if nid in node_by_id:
                root = nid
                break
        if not root and node_by_id:
            root = sorted(node_by_id)[0]
        adjacency = dependents if dependents.get(root) else imports
        fan_in = {nid: len(set(kids)) for nid, kids in dependents.items()}
        for nid, children in list(adjacency.items()):
            adjacency[nid] = sorted(set(children), key=lambda c: (-fan_in.get(c, 0), c))
        order: List[str] = []
        parent: Dict[str, Optional[str]] = {}
        depth: Dict[str, int] = {}
        if root:
            parent[root] = None
            depth[root] = 0
            queue = [root]
            limit = cfg.VIDEO_TREE_MAX_NODES or len(node_by_id)
            while queue and len(order) < limit:
                cur = queue.pop(0)
                order.append(cur)
                for kid in adjacency.get(cur, []):
                    if kid not in parent and len(order) + len(queue) < limit:
                        parent[kid] = cur
                        depth[kid] = depth[cur] + 1
                        queue.append(kid)
        max_depth = max(depth.values()) if depth else 0
        return {"root": root, "order": order, "parent": parent,
                "depth": depth, "max_depth": max_depth}

    def build_scenes(self, data: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], float]:
        """Lay every scene on the global clock.

        Acts with a non-positive duration are skipped together with their card.
        """
        c = self.config
        acts = [("I", "layers", c.VIDEO_LAYER_S), ("II", "gods", c.VIDEO_GOD_S),
                ("III", "tree", c.VIDEO_TREE_S), ("IV", "communities", c.VIDEO_COMM_S),
                ("V", "graph", c.VIDEO_GRAPH_S), ("VI", "orbit", c.VIDEO_ORBIT_S),
                ("VII", "bundle", c.VIDEO_BUNDLE_S), ("VIII", "sphere", c.VIDEO_SPHERE_S),
                ("IX", "dna", c.VIDEO_DNA_S)]
        plan: List[Tuple[str, float, Dict[str, Any]]] = [("title", c.VIDEO_TITLE_S, {})]
        for card, kind, dur in acts:
            if dur <= 0:
                continue
            plan.append(("card", c.VIDEO_CARD_S, {"card": card}))
            plan.append((kind, dur, {"act": card}))
        if c.VIDEO_INVITE_S > 0:
            plan.append(("invite", c.VIDEO_INVITE_S, {}))
        plan.append(("outro", c.VIDEO_OUTRO_S, {}))
        out: List[Dict[str, Any]] = []
        t = 0.0
        for kind, dur, extra in plan:
            sc = dict(kind=kind, start=t, dur=float(dur))
            sc.update(extra)
            out.append(sc)
            t += float(dur)
        return out, t

    def graph_positions(self, data: Dict[str, Any], box: Tuple[int, int, int, int]) -> Dict[str, Tuple[float, float]]:
        """Compute deterministic positions for graph nodes inside a box."""
        ids = data["graph_nodes"]
        if not ids:
            return {}
        x0, y0, x1, y1 = box
        try:
            import networkx as nx

            g = nx.Graph()
            g.add_nodes_from(ids)
            for a, b in data["graph_links"]:
                if a != b and a in g and b in g:
                    g.add_edge(a, b)
            if len(g) == 1:
                return {ids[0]: ((x0 + x1) / 2, (y0 + y1) / 2)}
            linked = [nid for nid in ids if g.degree(nid) > 0]
            loose = sorted(nid for nid in ids if g.degree(nid) == 0)
            out: Dict[str, Tuple[float, float]] = {}
            strip = self.config.VIDEO_GRAPH_LOOSE_STRIP if loose else 0
            if linked:
                core = g.subgraph(linked)
                spread = self.config.VIDEO_GRAPH_SPREAD / math.sqrt(max(1, len(linked)))
                pos = nx.spring_layout(core, seed=7, iterations=200, k=spread)
                xs = sorted(p[0] for p in pos.values())
                ys = sorted(p[1] for p in pos.values())
                trim = int(len(xs) * self.config.VIDEO_GRAPH_TRIM_FRACTION)
                lo_x, hi_x = xs[trim], xs[len(xs) - 1 - trim]
                lo_y, hi_y = ys[trim], ys[len(ys) - 1 - trim]
                for nid, (px, py) in pos.items():
                    fx = min(1.0, max(0.0, (px - lo_x) / ((hi_x - lo_x) or 1)))
                    fy = min(1.0, max(0.0, (py - lo_y) / ((hi_y - lo_y) or 1)))
                    out[nid] = (x0 + 60 + fx * (x1 - x0 - 120), y0 + 50 + fy * (y1 - y0 - 100 - strip))
            for i, nid in enumerate(loose):
                fx = (i + 0.5) / len(loose)
                out[nid] = (x0 + 60 + fx * (x1 - x0 - 120), y1 - 30)
            return out
        except ImportError:
            out = {}
            n = len(ids)
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            rx, ry = (x1 - x0 - 120) / 2, (y1 - y0 - 120) / 2
            for i, nid in enumerate(sorted(ids)):
                ang = 2 * math.pi * i / max(1, n)
                out[nid] = (cx + rx * math.cos(ang), cy + ry * math.sin(ang))
            return out

    def tree_positions(self, data: Dict[str, Any], box: Tuple[int, int, int, int]) -> Dict[str, Tuple[float, float]]:
        """Place the full BFS tree radially: root in the center, one ring per depth.

        Each node gets an angular sector proportional to its number of
        leaves, so every dependent fits on screen without truncation.
        """
        tree = data.get("dep_tree", {})
        order: List[str] = tree.get("order", [])
        parent: Dict[str, Optional[str]] = tree.get("parent", {})
        depth: Dict[str, int] = tree.get("depth", {})
        if not order:
            return {}
        x0, y0, x1, y1 = box
        children: Dict[str, List[str]] = {}
        for nid in order:
            par = parent.get(nid)
            if par is not None:
                children.setdefault(par, []).append(nid)
        leaves: Dict[str, int] = {}
        for nid in reversed(order):
            kids = children.get(nid, [])
            leaves[nid] = sum(leaves[k] for k in kids) if kids else 1
        max_depth = max(depth.values()) if depth else 0
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        margin = self.config.VIDEO_TREE_RING_MARGIN
        rx = max(1.0, (x1 - x0) / 2 - margin * 3)
        ry = max(1.0, (y1 - y0) / 2 - margin)
        out: Dict[str, Tuple[float, float]] = {}
        span: Dict[str, Tuple[float, float]] = {order[0]: (-math.pi / 2, 3 * math.pi / 2)}
        for nid in order:
            lo, hi = span[nid]
            mid = (lo + hi) / 2
            frac = math.sqrt(depth.get(nid, 0) / max(1, max_depth))
            out[nid] = (cx + rx * frac * math.cos(mid), cy + ry * frac * math.sin(mid))
            kids = children.get(nid, [])
            total = sum(leaves[k] for k in kids) or 1
            cursor = lo
            for kid in kids:
                width = (hi - lo) * leaves[kid] / total
                span[kid] = (cursor, cursor + width)
                cursor += width
        return out

    def emergence_frames(self, data: Dict[str, Any], box: Tuple[int, int, int, int]) -> List[Dict[str, Tuple[float, float]]]:
        """ForceAtlas2 snapshots of the resolved import graph fitted to a pixel box."""
        c = self.config
        settings = ForceAtlas2Settings(
            iterations=c.VIDEO_FA2_ITERATIONS, snapshots=c.VIDEO_FA2_SNAPSHOTS,
            scaling=c.VIDEO_FA2_SCALING, gravity=c.VIDEO_FA2_GRAVITY, linlog=c.VIDEO_FA2_LINLOG,
        )
        raw = forceatlas2_frames(data["graph_nodes"], data["graph_links"], settings)
        return fit_frames(raw, box, 40.0, c.VIDEO_GRAPH_TRIM_FRACTION)

    def bundle_groups(self, data: Dict[str, Any]) -> Dict[str, List[str]]:
        """Group graph files by community (hubs first), unassigned files last."""
        membership: Dict[str, int] = data.get("membership", {})
        labels: List[str] = data.get("community_labels", [])
        rank: Dict[str, float] = data.get("rank", {})
        keep = set(data["graph_nodes"])
        groups: Dict[str, List[str]] = {}
        for index, label in enumerate(labels):
            members = [nid for nid, comm in membership.items() if comm == index and nid in keep]
            groups[f"{index}:{label}"] = sorted(members, key=lambda nid: (-rank.get(nid, 0.0), nid))
        loose = sorted(nid for nid in data["graph_nodes"] if nid not in membership)
        if loose:
            groups["-1:unassigned"] = loose
        return groups

    def bundle_layout(self, data: Dict[str, Any], box: Tuple[int, int, int, int]) -> BundleLayout:
        """Hierarchical edge bundling of resolved imports grouped by community."""
        x0, y0, x1, y1 = box
        radius = max(10.0, min(x1 - x0, y1 - y0) / 2 - 70)
        return hierarchical_edge_bundling(
            self.bundle_groups(data), data["graph_links"], ((x0 + x1) / 2, (y0 + y1) / 2 + 10), radius,
            beta=self.config.VIDEO_BUNDLE_BETA, samples=self.config.VIDEO_BUNDLE_SAMPLES,
        )

    def orbit_positions(self, data: Dict[str, Any]) -> Dict[str, Tuple[float, float, float]]:
        """3D ForceAtlas2 layout of the graph, centered and scaled to the unit sphere."""
        c = self.config
        settings = ForceAtlas2Settings(
            iterations=c.VIDEO_ORBIT_FA2_ITERATIONS, snapshots=2, scaling=c.VIDEO_FA2_SCALING,
            gravity=c.VIDEO_FA2_GRAVITY, linlog=c.VIDEO_FA2_LINLOG, dims=3,
        )
        frames = forceatlas2_frames(data["graph_nodes"], data["graph_links"], settings)
        return normalize_cloud(frames[-1]) if frames else {}

    def sphere_layout(self, data: Dict[str, Any]) -> SphereBundleLayout:
        """Spherical edge bundling of resolved imports on community caps."""
        c = self.config
        return spherical_edge_bundling(
            self.bundle_groups(data), data["graph_links"], 1.0, beta=c.VIDEO_BUNDLE_BETA,
            samples=c.VIDEO_SPHERE_SAMPLES, inner_ratio=c.BUNDLEGRAPH_INNER_RATIO,
        )

    def orbit_stops(self, data: Dict[str, Any], positions: Dict[str, Tuple[float, float, float]]) -> List[Dict[str, Any]]:
        """Camera tour stops: the largest communities with their 3D centroid."""
        membership: Dict[str, int] = data.get("membership", {})
        stops: List[Dict[str, Any]] = []
        for index, comm in enumerate(data.get("communities", [])[: self.config.VIDEO_ORBIT_TOUR_STOPS]):
            members = [nid for nid, ci in membership.items() if ci == index and nid in positions]
            if not members:
                continue
            centroid = tuple(sum(positions[m][k] for m in members) / len(members) for k in range(3))
            stops.append({"index": index, "label": comm["label"], "size": comm["size"],
                          "cohesion": comm["cohesion"], "hub": comm["hub"],
                          "internal": comm["internal"], "external": comm["external"],
                          "target": centroid})
        return stops

    def _prepare_layouts(self, data: Dict[str, Any]) -> None:
        """Precompute every layout the scenes draw (before forking workers)."""
        cfg = self.config
        box, _ = _graph_boxes(cfg)
        data["fa2_frames"] = self.emergence_frames(data, (box[0], box[1] + 30, box[2], box[3] - 10))
        tbox = _panel(cfg)
        data["tree_pos"] = self.tree_positions(data, (tbox[0], tbox[1] + 10, tbox[2] - 320, tbox[3] - 10))
        bbox, _ = _split_boxes(cfg)
        data["bundle"] = self.bundle_layout(data, (bbox[0], bbox[1] + 30, bbox[2], bbox[3] - 10))
        if cfg.VIDEO_ORBIT_S > 0 or cfg.VIDEO_SPHERE_S > 0 or cfg.VIDEO_INVITE_S > 0:
            data["orbit_pos"] = self.orbit_positions(data)
            data["orbit_stops"] = self.orbit_stops(data, data["orbit_pos"])
            data["sphere"] = self.sphere_layout(data)

    def render_single_frame(self, data: Dict[str, Any], frame_index: int) -> bytes:
        """Render one frame to raw RGB bytes without touching ffmpeg."""

        cfg = self.config
        scenes, total = self.build_scenes(data)
        bd = Backdrop(cfg.VIDEO_WIDTH, cfg.VIDEO_HEIGHT)
        fonts = resolve_fonts()
        global _RENDER_D, _RENDER_SCENES, _RENDER_TOTAL, _RENDER_BD, _RENDER_FONTS, _RENDER_CFG
        _RENDER_D, _RENDER_SCENES, _RENDER_TOTAL = data, scenes, total
        _RENDER_BD, _RENDER_FONTS, _RENDER_CFG = bd, fonts, cfg
        self._prepare_layouts(data)
        img = _draw_frame(frame_index)
        return img.tobytes()

    def render(self, data: Dict[str, Any], output_path: str) -> str:
        """Render all frames and encode to mp4, muxing music if configured."""
        cfg = self.config
        if shutil.which("ffmpeg") is None:
            raise RuntimeError("ffmpeg not found, skipping video")
        try:
            import PIL  # noqa: F401
        except ImportError as exc:
            raise RuntimeError("PIL not installed, skipping video") from exc
        scenes, total = self.build_scenes(data)
        global _RENDER_D, _RENDER_SCENES, _RENDER_TOTAL, _RENDER_BD, _RENDER_FONTS, _RENDER_CFG
        _RENDER_D, _RENDER_SCENES, _RENDER_TOTAL = data, scenes, total
        _RENDER_BD = Backdrop(cfg.VIDEO_WIDTH, cfg.VIDEO_HEIGHT)
        _RENDER_FONTS = resolve_fonts()
        _RENDER_CFG = cfg
        self._prepare_layouts(data)
        n_frames = max(1, int(total * cfg.VIDEO_FPS))
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{cfg.VIDEO_WIDTH}x{cfg.VIDEO_HEIGHT}", "-r", str(cfg.VIDEO_FPS), "-i", "-"]
        music = cfg.VIDEO_MUSIC_PATH or os.environ.get("READMENATOR_MUSIC", "")
        if music and Path(music).is_file():
            cmd += ["-i", str(music), "-map", "0:v", "-map", "1:a",
                    "-c:a", "aac", "-b:a", "128k", "-shortest"]
        cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(cfg.VIDEO_CRF),
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output_path)]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        jobs = cfg.VIDEO_JOBS or (os.cpu_count() or 4)
        ctx = multiprocessing.get_context("fork")
        with ctx.Pool(jobs) as pool:
            for buf in pool.imap(_render_frame_bytes, range(n_frames), chunksize=4):
                proc.stdin.write(buf)
        proc.stdin.close()
        if proc.wait() != 0:
            raise RuntimeError("ffmpeg failed while encoding video")
        return str(output_path)


def _render_frame_bytes(fi: int) -> bytes:
    """Pool worker: draw one frame and return raw RGB bytes."""
    return _draw_frame(fi).tobytes()


def _draw_frame(fi: int) -> Any:
    """Draw one frame for the global render state."""
    from PIL import ImageDraw

    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    cfg = _RENDER_CFG
    fps = cfg.VIDEO_FPS
    gt = fi / max(1, fps)
    sc = _RENDER_SCENES[-1]
    for s in _RENDER_SCENES:
        if s["start"] <= gt < s["start"] + s["dur"]:
            sc = s
            break
    lt = gt - sc["start"]
    img = _RENDER_BD.base.copy()
    if sc["kind"] not in ("title", "card", "outro", "invite"):
        draw_grid(img, gt, 0.35, _RENDER_BD)
    d = ImageDraw.Draw(img, "RGBA")
    _SCENE_FN[sc["kind"]](img, d, lt, gt, sc)
    edge = min(lt, sc["dur"] - lt) * fps
    glitch = max(0.0, 1 - edge / 12) if gt > 12 / max(1, fps) else 0.0
    img = post(img, glitch * 0.8, fi)
    if gt < 0.8:
        img = _img().blend(_img().new("RGB", img.size, (0, 0, 0)), img, gt / 0.8)
    return img


def _scene_title(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Cold open with counting project stats and language chips."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    w, h = cfg.VIDEO_WIDTH, cfg.VIDEO_HEIGHT
    a = ease(lt / 1.0)
    draw_sun(img, a, _RENDER_BD, _RENDER_BD.horizon + 10)
    draw_grid(img, gt, 1.0, _RENDER_BD)
    chroma_text(img, (w / 2, h * 0.26), data["project"], fonts["big"], (255, 255, 255), spread=3, anchor="mm")
    d.text((w / 2, h * 0.40), "CODEBASE OVERVIEW // READMENATOR", font=fonts["mid"], fill=CYAN, anchor="mm")
    k = ease((lt - 1.2) / 1.2)
    files_now = int(ease((lt - 1.2) / 1.6) * data["files"])
    syms_now = int(ease((lt - 1.4) / 1.6) * data["symbols"])
    imps_now = int(ease((lt - 1.6) / 1.6) * data["imports"])
    facts = f"{fmt_int(files_now)} files  //  {fmt_int(syms_now)} symbols  //  {fmt_int(imps_now)} imports"
    d.text((w / 2, h * 0.54), facts, font=fonts["small_b"], fill=alpha(TXT, k), anchor="mm")
    total_lang = max(1, sum(cnt for _, cnt in data["languages"]))
    x = w / 2 - sum(fonts["tiny_b"].getlength(f"{lang} {cnt}") + 60 for lang, cnt in data["languages"][:4]) / 2
    for lang, cnt in data["languages"][:4]:
        label = f"{lang} {cnt}"
        frac = cnt / total_lang
        bw = fonts["tiny_b"].getlength(label) + 36
        d.rectangle((x, h * 0.62, x + bw, h * 0.62 + 30), fill=(12, 8, 30, int(220 * k)),
                    outline=alpha(CYAN, 0.6 * k), width=1)
        d.rectangle((x + 8, h * 0.62 + 22, x + 8 + (bw - 16) * frac * k, h * 0.62 + 25),
                    fill=alpha(CYAN, 0.9 * k))
        d.text((x + 10, h * 0.62 + 4), label, font=fonts["tiny_b"], fill=alpha(TXT, k))
        x += bw + 14
    if not data["languages"]:
        d.text((w / 2, h * 0.62), "no files scanned", font=fonts["small"], fill=alpha(DIM, k), anchor="mm")
    k2 = ease((lt - 2.6) / 0.8)
    d.text((w / 2, h - 30), "every number on screen was measured for real",
           font=fonts["small"], fill=alpha(DIM, k2), anchor="mm")


def _scene_card(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Act interstitial card."""
    assert _RENDER_FONTS is not None and _RENDER_CFG is not None
    fonts, cfg = _RENDER_FONTS, _RENDER_CFG
    w, h = cfg.VIDEO_WIDTH, cfg.VIDEO_HEIGHT
    tag, title, sub = ACT_CARDS[sc["card"]]
    a = ease(lt / 0.5) * (1 - ease((lt - (sc["dur"] - 0.4)) / 0.4))
    draw_sun(img, 0.35 * a, _RENDER_BD, _RENDER_BD.horizon - 30)
    draw_grid(img, gt, 0.8, _RENDER_BD)
    d.text((w / 2, h * 0.38), tag, font=fonts["mid"], fill=alpha(MAGENTA, a), anchor="mm")
    chroma_text(img, (w / 2, h * 0.50), title, fonts["big"], alpha(TXT, a), spread=4, anchor="mm")
    d.text((w / 2, h * 0.62), sub, font=fonts["cap"], fill=alpha(CYAN, a), anchor="mm")


def _scene_layers(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Animated horizontal bars for the 5-layer model with sweep cursor."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT I // LAYERS", fonts, cfg.VIDEO_WIDTH)
    layers = sorted(data["layers"].items(), key=lambda kv: -kv[1]) or [("business_logic", 0)]
    top = max(1, max(c for _, c in layers))
    panel = _panel(cfg)
    hud_panel(d, panel, "architectural layers // path + import heuristics", fonts, CYAN)
    y = panel[1] + 45
    step = max(30, min(56, (panel[3] - panel[1] - 110) // max(1, len(layers))))
    for i, (layer, count) in enumerate(layers):
        reveal = ease((lt - 0.4 - i * 0.5) / 0.8)
        shown = int(reveal * count)
        bar_w = (panel[2] - panel[0] - 420) * (count / top) * reveal
        col = LAYER_COLORS.get(layer, DIM)
        d.text((panel[0] + 30, y), layer, font=fonts["small_b"], fill=alpha(TXT, reveal))
        d.rectangle((panel[0] + 270, y + 2, panel[0] + 270 + max(0, bar_w), y + 24), fill=alpha(col, 0.85 * reveal))
        d.text((panel[2] - 30, y), f"{fmt_int(shown)} files", font=fonts["term"], fill=alpha(TXT, reveal), anchor="ra")
        y += step
    _scan_cursor(d, panel, ease((lt - 0.5) / max(0.5, sc["dur"] - 2.5)))
    _verdict_badge(d, panel, f"{len(layers)} layers  //  {fmt_int(data['files'])} files mapped", fonts, lt, sc["dur"])
    draw_caption(d, "each file lands in one layer: follow the dominant one first", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_gods(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Ranked god nodes with the formula exposed plus real source preview."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT II // GOD NODES", fonts, cfg.VIDEO_WIDTH)
    details = data.get("god_details", [])[:6]
    left, right = _split_boxes(cfg)
    hud_panel(d, left, "centrality = connections + symbols // higher = read first", fonts, MAGENTA)
    hud_panel(d, right, f"inside #1 // {short_label(data.get('preview_file', ''), 24) or 'no file'}", fonts, YELLOW)
    top = max([1.0] + [g["score"] for g in details])
    y = left[1] + 42
    step = max(52, min(72, (left[3] - left[1] - 110) // max(1, len(details))))
    for i, g in enumerate(details):
        reveal = ease((lt - 0.3 - i * 0.4) / 0.7)
        bar_w = (left[2] - left[0] - 120) * (g["score"] / top) * reveal
        d.text((left[0] + 24, y), f"#{i + 1}  {short_label(g['file'], cfg.VIDEO_MAX_LABEL_CHARS)}",
               font=fonts["small_b"], fill=alpha(TXT, reveal))
        d.text((left[0] + 24, y + 22),
               f"in {g['in']} imported-by  ·  out {g['out']} imports  ·  {g['symbols']} symbols  ·  score {g['score']:.1f}",
               font=fonts["tiny"], fill=alpha(DIM, reveal))
        d.rectangle((left[0] + 24, y + 42, left[0] + 24 + max(0, bar_w), y + 50),
                    fill=alpha(YELLOW, 0.85 * reveal))
        y += step
    if not details:
        d.text(((left[0] + left[2]) / 2, (left[1] + left[3]) / 2), "no files scanned",
               font=fonts["cap"], fill=DIM, anchor="mm")
    lines = data.get("preview_lines", [])[:18]
    ry = right[1] + 44
    hl = int(ease(lt / max(0.5, sc["dur"] - 1.0)) * max(1, len(lines)))
    for i, ln in enumerate(lines):
        if ry + 20 > right[3] - 12:
            break
        if i == hl:
            d.rectangle((right[0] + 6, ry - 2, right[2] - 6, ry + 18), fill=alpha(YELLOW, 0.18))
        d.text((right[0] + 16, ry), f"{i + 1:>3}", font=fonts["tiny"], fill=FAINT)
        d.text((right[0] + 52, ry), short_label(ln, 52), font=fonts["tiny"], fill=alpha(_code_tint(ln), 0.95))
        ry += 21
    if not lines:
        d.text(((right[0] + right[2]) / 2, (right[1] + right[3]) / 2), "no preview",
               font=fonts["small"], fill=DIM, anchor="mm")
    draw_caption(d, "score = weighted connections + symbols: these files shape every change", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_tree(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """The true dependency tree: BFS spanning tree grown from the hub file."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT III // THE BLAST RADIUS", fonts, cfg.VIDEO_WIDTH)
    tree = data.get("dep_tree", {})
    order: List[str] = tree.get("order", [])
    parent: Dict[str, Optional[str]] = tree.get("parent", {})
    depth: Dict[str, int] = tree.get("depth", {})
    root = tree.get("root", "")
    left, right = _split_boxes(cfg)
    hud_panel(d, left, f"files that import {short_label(root, 22) or '...'} (BFS over real imports)", fonts, MAGENTA)
    hud_panel(d, right, "focus file // real symbols", fonts, CYAN)
    pos = data.get("tree_pos", {})
    p = ease((lt - 0.5) / max(0.5, sc["dur"] - 2.5))
    visible = max(0, int(p * len(order)))
    shown = order[:visible]
    shown_set = set(shown)
    for nid in shown:
        par = parent.get(nid)
        if par is None or par not in shown_set or nid not in pos or par not in pos:
            continue
        px, py = pos[par]
        x, y = pos[nid]
        col = CYAN if depth.get(nid, 0) > 1 else MAGENTA
        d.line((px, py, x, y), fill=alpha(col, 0.55), width=1 if depth.get(nid, 0) > 1 else 2)
    placed: List[Tuple[float, float, float, float]] = []
    gap = cfg.VIDEO_TREE_LABEL_GAP
    by_rank = sorted(range(len(shown)), key=lambda i: (depth.get(shown[i], 0), i))
    for i, nid in enumerate(shown):
        if nid not in pos:
            continue
        x, y = pos[nid]
        age = p * len(order) - i
        flash = max(0.0, 1 - age / 2)
        dep = depth.get(nid, 0)
        r = (9 if nid == root else 6 if dep == 1 else 4) + 4 * flash
        col = YELLOW if nid == root else (MAGENTA if dep == 1 else CYAN)
        d.ellipse((x - r, y - r, x + r, y + r), fill=col,
                  outline=(255, 255, 255) if flash > 0 else None, width=2)
    for i in by_rank:
        nid = shown[i]
        if nid not in pos:
            continue
        x, y = pos[nid]
        base = short_label(nid.rpartition("/")[2] or nid, 20)
        w = len(base) * cfg.VIDEO_TREE_CHAR_PX
        rect = (x + 8, y - 9, x + 8 + w, y + 9)
        if any(not (rect[2] + gap < q[0] or q[2] + gap < rect[0] or rect[3] < q[1] or q[3] < rect[1]) for q in placed):
            continue
        placed.append(rect)
        d.text((x + 8, y - 9), base, font=fonts["tiny_b"], fill=alpha(TXT, 0.95))
    if not order:
        d.text(((left[0] + left[2]) / 2, (left[1] + left[3]) / 2), "no resolved imports: flat project",
               font=fonts["cap"], fill=DIM, anchor="mm")
    symbol_map = data.get("node_symbols", {})
    with_symbols = [nid for nid in shown if symbol_map.get(nid)]
    focus = with_symbols[-1] if with_symbols else (shown[-1] if shown else "")
    syms = symbol_map.get(focus, [])
    d.text((right[0] + 20, right[1] + 44), short_label(focus, 30) or "…", font=fonts["small_b"], fill=TXT)
    ry = right[1] + 72
    for name, kind, line in syms[:12]:
        if ry + 20 > right[3] - 12:
            break
        d.text((right[0] + 20, ry), short_label(name, 22), font=fonts["tiny_b"], fill=CYAN)
        d.text((right[2] - 20, ry), f"{kind} L{line}", font=fonts["tiny"], fill=DIM, anchor="ra")
        ry += 22
    if focus and not syms:
        d.text((right[0] + 20, ry), "no symbols extracted", font=fonts["tiny"], fill=DIM)
    rings = max(depth.values()) if depth else 0
    _verdict_badge(d, left, f"all {max(0, len(order) - 1)} dependents of {short_label(root.rpartition('/')[2] or root, 18)} shown, {rings} rings deep", fonts, lt, sc["dur"], MAGENTA)
    draw_caption(d, "every edge is a real import: this is how the code actually hangs together", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_communities(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Community cards explaining why each group sticks together."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT IV // COMMUNITIES", fonts, cfg.VIDEO_WIDTH)
    comms = data["communities"][:6]
    panel = _panel(cfg)
    hud_panel(d, panel, "import neighbourhoods // louvain modularity on real edges", fonts, GREEN)
    if not comms:
        d.text((cfg.VIDEO_WIDTH / 2, (panel[1] + panel[3]) / 2), "one flat graph: no communities separated", font=fonts["cap"], fill=DIM, anchor="mm")
    cols = 3
    cw = (panel[2] - panel[0] - 30) / cols
    card_h = min(200, max(120, (panel[3] - panel[1] - 120) // 2))
    for i, c in enumerate(comms):
        reveal = ease((lt - 0.3 - i * 0.4) / 0.7)
        cx = panel[0] + 15 + (i % cols) * cw
        cy = panel[1] + 45 + (i // cols) * (card_h + 15)
        d.rectangle((cx, cy, cx + cw - 20, cy + card_h), fill=(12, 8, 30, int(220 * reveal)), outline=alpha(GREEN, reveal), width=2)
        name = c["label"].rpartition(": ")[2] or c["label"]
        d.text((cx + 14, cy + 10), f"C{i}: {short_label(name, 24)}", font=fonts["small_b"], fill=alpha(GREEN, reveal))
        d.text((cx + 14, cy + 32), f"{c['size']} files · cohesion {c['cohesion']:.2f}",
               font=fonts["tiny_b"], fill=alpha(TXT, reveal))
        coh_w = (cw - 48) * max(0.0, min(1.0, c["cohesion"])) * reveal
        d.rectangle((cx + 14, cy + 50, cx + 14 + max(0, coh_w), cy + 56), fill=alpha(GREEN, 0.9 * reveal))
        d.text((cx + 14, cy + 62), f"hub: {short_label(c['hub'].rpartition('/')[2] or c['hub'], 20)}",
               font=fonts["tiny"], fill=alpha(YELLOW, reveal))
        d.text((cx + 14, cy + 80), f"core dir: {short_label(c['dominant'], 22)}",
               font=fonts["tiny"], fill=alpha(DIM, reveal))
        d.text((cx + 14, cy + 98), f"{c['internal']} imports inside · {c['external']} crossing out",
               font=fonts["tiny"], fill=alpha(TXT, reveal))
        if c["top_symbols"]:
            d.text((cx + 14, cy + 116), f"key: {short_label(c['top_symbols'][0], 24)}",
                   font=fonts["tiny"], fill=alpha(CYAN, reveal))
        members = ", ".join(short_label(f.rpartition("/")[2] or f, 12) for f in c["files"][:3])
        if c["remaining"]:
            members += f" +{c['remaining']} more"
        d.text((cx + 14, cy + card_h - 22), short_label(members, 34), font=fonts["tiny"], fill=alpha(DIM, reveal))
    extra = ""
    if data["cycles"]:
        extra = f", {data['cycles']} cycles"
    _verdict_badge(d, panel, f"{len(comms)} communities{extra}: crossing imports are refactor seams", fonts, lt, sc["dur"])
    draw_caption(d, "cohesion = imports inside ÷ all imports: low cohesion leaks across groups", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_graph(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """ForceAtlas2 convergence of the real import graph, then PageRank surfers."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT V // EMERGENCE", fonts, cfg.VIDEO_WIDTH)
    box, side = _graph_boxes(cfg)
    hud_panel(d, box, "forceatlas2 linlog // repulsion ~ degree, gravity, adaptive speed", fonts, CYAN)
    hud_panel(d, side, "telemetry // pagerank", fonts, MAGENTA)
    frames = data.get("fa2_frames", [])
    ids = data["graph_nodes"]
    links = data["graph_links"]
    membership = data.get("membership", {})
    rank = data.get("rank", {})
    settle = max(0.5, sc["dur"] * 0.55)
    p = ease((lt - 0.4) / settle)
    pos = interpolate_frames(frames, p)
    top_rank = max([1e-9] + [rank.get(nid, 0.0) for nid in ids])
    edge_a = 0.12 + 0.28 * p
    for a, b in links:
        if a not in pos or b not in pos:
            continue
        ca, cb = membership.get(a, -1), membership.get(b, -1)
        col = community_color(ca) if ca == cb else (150, 140, 210)
        d.line((*pos[a], *pos[b]), fill=alpha(col, edge_a if ca == cb else edge_a * 0.6), width=1)
    after = ease((lt - 0.4 - settle) / 1.2)
    if after > 0 and links:
        hot = sorted(links, key=lambda e: (-(rank.get(e[0], 0.0) + rank.get(e[1], 0.0)), e))[: cfg.VIDEO_SURFERS]
        for k, (a, b) in enumerate(hot):
            if a not in pos or b not in pos:
                continue
            f = (gt * 0.7 + _packet_offset(a, b, k)) % 1.0
            x = pos[a][0] + (pos[b][0] - pos[a][0]) * f
            y = pos[a][1] + (pos[b][1] - pos[a][1]) * f
            r = 1.5 + 2.5 * (rank.get(b, 0.0) / top_rank)
            d.ellipse((x - r, y - r, x + r, y + r), fill=alpha((255, 255, 255), 0.9 * after))
    order = sorted((nid for nid in ids if nid in pos), key=lambda nid: rank.get(nid, 0.0))
    for nid in order:
        x, y = pos[nid]
        weight = math.sqrt(rank.get(nid, 0.0) / top_rank)
        r = 3 + 10 * weight * (0.4 + 0.6 * p)
        col = community_color(membership.get(nid, -1))
        if weight > 0.5 and after > 0:
            glow = r + 6 + 3 * math.sin(gt * 3 + weight * 5)
            d.ellipse((x - glow, y - glow, x + glow, y + glow), fill=alpha(col, 0.18 * after))
        d.ellipse((x - r, y - r, x + r, y + r), fill=alpha(col, 0.95), outline=alpha((255, 255, 255), 0.5), width=1)
    ranked = sorted(ids, key=lambda nid: (-rank.get(nid, 0.0), nid))
    label_a = ease((lt - 0.6 - settle) / 1.0)
    if label_a > 0:
        placed: List[Tuple[float, float, float, float]] = []
        for nid in ranked[: cfg.VIDEO_RANK_LABELS]:
            if nid not in pos:
                continue
            x, y = pos[nid]
            text = short_label(nid.rpartition("/")[2] or nid, 22)
            w = fonts["tiny_b"].getlength(text)
            rect = (x + 10, y - 20, x + 18 + w, y - 2)
            if any(not (rect[2] < q[0] or q[2] < rect[0] or rect[3] < q[1] or q[3] < rect[1]) for q in placed):
                continue
            placed.append(rect)
            d.rectangle(rect, fill=(6, 3, 18, int(210 * label_a)), outline=alpha(YELLOW, 0.7 * label_a))
            d.text((x + 14, y - 18), text, font=fonts["tiny_b"], fill=alpha(TXT, label_a))
    x0, _, x1, _ = side
    iters = int(p * cfg.VIDEO_FA2_ITERATIONS)
    chroma_text(img, (x0 + 20, box[1] + 40), fmt_int(iters), fonts["mid"], TXT, spread=2)
    d.text((x0 + 20, box[1] + 85), f"of {cfg.VIDEO_FA2_ITERATIONS} iterations", font=fonts["small"], fill=DIM)
    d.text((x0 + 20, box[1] + 110), f"{len(ids)} files · {len(links)} imports", font=fonts["small_b"], fill=CYAN)
    y = box[1] + 148
    d.text((x0 + 20, y), "PAGERANK (random surfer)", font=fonts["tiny_b"], fill=MAGENTA)
    y += 20
    for nid in ranked[:7]:
        if y + 34 > box[3] - 30:
            break
        score = rank.get(nid, 0.0)
        bw = (x1 - x0 - 60) * score / top_rank * ease((lt - 1.0) / 1.5)
        col = community_color(membership.get(nid, -1))
        d.text((x0 + 20, y), short_label(nid.rpartition("/")[2] or nid, 18), font=fonts["tiny"], fill=TXT)
        d.text((x1 - 20, y), f"{score:.3f}", font=fonts["tiny"], fill=DIM, anchor="ra")
        d.rectangle((x0 + 20, y + 16, x0 + 20 + max(0, bw), y + 22), fill=alpha(col, 0.9))
        y += 36
    d.text((x0 + 20, box[3] - 44), "size  = pagerank", font=fonts["tiny"], fill=DIM)
    d.text((x0 + 20, box[3] - 26), "color = community", font=fonts["tiny"], fill=DIM)
    caption = ("no forces tuned by hand: dense groups pull together, hubs push apart"
               if p < 1 else f"converged: {len(ids)} files settle into their communities, surfers follow PageRank")
    draw_caption(d, caption, lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_bundle(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Hierarchical edge bundling: every import routed through the community tree."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT VII // THE WIRING", fonts, cfg.VIDEO_WIDTH)
    left, right = _split_boxes(cfg)
    hud_panel(d, left, f"hierarchical edge bundling // beta {cfg.VIDEO_BUNDLE_BETA:.2f}, b-spline through communities", fonts, VIOLET)
    hud_panel(d, right, "flows // imports between communities", fonts, GREEN)
    layout: Optional[BundleLayout] = data.get("bundle")
    membership = data.get("membership", {})
    if layout is None or not layout.leaves:
        d.text(((left[0] + left[2]) / 2, (left[1] + left[3]) / 2), "no communities to bundle",
               font=fonts["cap"], fill=DIM, anchor="mm")
        draw_caption(d, "flat project: nothing to bundle", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))
        return
    cx, cy = layout.center
    rad = layout.radius
    reveal = ease((lt - 0.4) / max(0.5, sc["dur"] * 0.45))
    groups = layout.groups
    cycle_start = 0.5 + sc["dur"] * 0.45
    spot = -1
    if lt > cycle_start and groups:
        span = max(0.5, (sc["dur"] - cycle_start - 1.0) / len(groups))
        spot = min(len(groups) - 1, int((lt - cycle_start) / span))
    spot_index = int(groups[spot][0].split(":", 1)[0]) if spot >= 0 else None
    shown = int(reveal * len(layout.curves))
    for k, (a, b, pts) in enumerate(layout.curves[:shown]):
        ca = membership.get(a, -1)
        cb = membership.get(b, -1)
        lit = spot_index is None or ca == spot_index or cb == spot_index
        col = community_color(ca)
        d.line(pts, fill=alpha(col, (0.32 if lit else 0.05)), width=2 if lit and spot_index is not None else 1)
    if reveal >= 1:
        for k, (a, b, pts) in enumerate(layout.curves):
            ca, cb = membership.get(a, -1), membership.get(b, -1)
            if ca == cb or (spot_index is not None and spot_index not in (ca, cb)):
                continue
            f = (gt * 0.45 + _packet_offset(a, b, k)) % 1.0
            x, y = _polyline_point(pts, f)
            d.ellipse((x - 2.5, y - 2.5, x + 2.5, y + 2.5), fill=alpha((255, 255, 255), 0.85))
    for label, start, end, count in groups:
        index = int(label.split(":", 1)[0])
        col = community_color(index)
        lit = spot_index is None or spot_index == index
        steps = max(2, int((end - start) * 40))
        arc = [(cx + (rad + 14) * math.cos(start + (end - start) * i / steps),
                cy + (rad + 14) * math.sin(start + (end - start) * i / steps)) for i in range(steps + 1)]
        d.line(arc, fill=alpha(col, 0.95 if lit else 0.3), width=6 if lit else 4)
        mid = (start + end) / 2
        name = short_label(label.split(":", 1)[1].rpartition(": ")[2] or label, 18)
        tx, ty = cx + (rad + 30) * math.cos(mid), cy + (rad + 30) * math.sin(mid)
        anchor = "lm" if math.cos(mid) >= 0 else "rm"
        if count >= 2 or lit:
            d.text((tx, ty), f"{name} ({count})", font=fonts["tiny_b"], fill=alpha(col, 0.95 if lit else 0.45), anchor=anchor)
    for nid, (x, y) in layout.leaves.items():
        col = community_color(membership.get(nid, -1))
        d.ellipse((x - 2.5, y - 2.5, x + 2.5, y + 2.5), fill=alpha(col, 0.9))
    flows: Dict[Tuple[int, int], int] = {}
    for a, b, _pts in layout.curves:
        ca, cb = membership.get(a, -1), membership.get(b, -1)
        if ca != cb:
            flows[(ca, cb)] = flows.get((ca, cb), 0) + 1
    labels = data.get("community_labels", [])
    x0, _, x1, _ = right
    y = right[1] + 44
    top_flow = max([1] + list(flows.values()))
    ordered = sorted(flows.items(), key=lambda kv: (-kv[1], kv[0]))
    for (ca, cb), n in ordered[:8]:
        if y + 40 > right[3] - 60:
            break
        name_a = short_label((labels[ca] if 0 <= ca < len(labels) else "unassigned").rpartition(": ")[2], 14)
        name_b = short_label((labels[cb] if 0 <= cb < len(labels) else "unassigned").rpartition(": ")[2], 14)
        k = ease((lt - 0.8) / 1.2)
        d.text((x0 + 18, y), f"{name_a} -> {name_b}", font=fonts["tiny_b"], fill=alpha(TXT, k))
        d.text((x1 - 18, y), f"{n}", font=fonts["tiny"], fill=alpha(DIM, k), anchor="ra")
        bw = (x1 - x0 - 36) * n / top_flow * k
        d.rectangle((x0 + 18, y + 17, x0 + 18 + max(0, bw), y + 23), fill=alpha(community_color(ca), 0.9))
        y += 40
    internal = sum(1 for a, b, _p in layout.curves if membership.get(a, -1) == membership.get(b, -1))
    d.text((x0 + 18, right[3] - 44), f"{internal} inside · {sum(flows.values())} crossing", font=fonts["small_b"], fill=GREEN)
    caption = "thick bundles are the real seams between subsystems"
    if spot >= 0:
        caption = f"spotlight: {short_label(groups[spot][0].split(':', 1)[1], 30)} and everything it touches"
    draw_caption(d, caption, lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _orbit_plan(dur: float) -> Tuple[float, float, float]:
    """Phase boundaries of the orbit act: assemble, color modes, community tour, hub reach."""
    return (0.14 * dur, 0.30 * dur, 0.80 * dur)


def _scene_orbit(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Camera tour of the 3D force graph: color modes, communities, hub reach."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT VI // ORBIT", fonts, cfg.VIDEO_WIDTH)
    box, side = _graph_boxes(cfg)
    hud_panel(d, box, "graph-force // 3d view, camera tour", fonts, CYAN)
    hud_panel(d, side, "explorer // live state", fonts, MAGENTA)
    pos = data.get("orbit_pos", {})
    if not pos:
        d.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), "no graph to orbit", font=fonts["cap"], fill=DIM, anchor="mm")
        draw_caption(d, "nothing to fly through yet", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))
        return
    dur = sc["dur"]
    a_end, b_end, c_end = _orbit_plan(dur)
    f = lt / max(1e-9, dur)
    yaw = 0.6 + cfg.VIDEO_ORBIT_TURNS * 2 * math.pi * f
    pitch = -math.radians(cfg.VIDEO_ORBIT_PITCH_DEG) * (0.6 + 0.4 * math.sin(f * math.pi))
    stops: List[Dict[str, Any]] = data.get("orbit_stops", [])
    origin = (0.0, 0.0, 0.0)
    hub = next((g["file"] for g in data.get("god_details", []) if g["file"] in pos), "")
    zoom_in = cfg.VIDEO_ORBIT_ZOOM
    keys: List[Tuple[float, Tuple[float, ...], float]] = [(0.0, origin, 1.0), (b_end / dur, origin, 1.0)]
    span = (c_end - b_end) / max(1, len(stops))
    for k, stop in enumerate(stops):
        start = (b_end + k * span) / dur
        keys.append((start + 0.35 * span / dur, stop["target"], zoom_in))
        keys.append((start + 0.95 * span / dur, stop["target"], zoom_in))
    if hub:
        keys.append(((c_end + 0.3 * (dur - c_end)) / dur, pos[hub], zoom_in * 1.15))
        keys.append(((c_end + 0.75 * (dur - c_end)) / dur, pos[hub], zoom_in * 1.15))
    keys.append((1.0, origin, 1.0))
    target, zoom = _camera_track(keys, f)
    mode = "community"
    if a_end <= lt < b_end:
        mode = COLOR_MODES[min(len(COLOR_MODES) - 1, int((lt - a_end) / max(1e-9, b_end - a_end) * len(COLOR_MODES)))]
    membership = data.get("membership", {})
    links = data["graph_links"]
    lit: Optional[set] = None
    edge_lit: Optional[Any] = None
    stop: Optional[Dict[str, Any]] = None
    if b_end <= lt < c_end and stops:
        stop = stops[min(len(stops) - 1, int((lt - b_end) / max(1e-9, span)))]
        index = stop["index"]
        lit = {nid for nid, ci in membership.items() if ci == index}
        edge_lit = lambda a, b, i=index: membership.get(a, -1) == i or membership.get(b, -1) == i
    elif lt >= c_end and hub:
        uses = sorted({b for a, b in links if a == hub and b != hub})
        users = sorted({a for a, b in links if b == hub and a != hub})
        lit = {hub, *uses, *users}
        edge_lit = lambda a, b: a == hub or b == hub
    draw_cloud3d(img, data, (box[0] + 2, box[1] + 31, box[2] - 2, box[3] - 34), cfg, yaw, pitch, target, zoom, mode,
                 lit, edge_lit, gt, fonts, appear=lt / max(1e-9, a_end), labels=cfg.VIDEO_ORBIT_LABELS)
    hint = "drag to orbit  ·  click a node to inspect  ·  C recolors  ·  reach  ·  path finder"
    d.text(((box[0] + box[2]) / 2, box[3] - 18), hint, font=fonts["tiny"], fill=alpha(DIM, 0.9), anchor="mm")
    x0, _, x1, _ = side
    y = side[1] + 42
    d.text((x0 + 16, y), "COLOR BY", font=fonts["tiny_b"], fill=MAGENTA)
    y += 20
    px = x0 + 16
    for name in COLOR_MODES:
        w = fonts["tiny_b"].getlength(name) + 14
        on = name == mode
        d.rectangle((px, y, px + w, y + 20), fill=alpha(CYAN, 0.25) if on else (12, 8, 30, 200),
                    outline=alpha(CYAN if on else FAINT, 0.9))
        d.text((px + 7, y + 3), name, font=fonts["tiny_b"], fill=TXT if on else DIM)
        px += w + 6
    y += 36
    d.text((x0 + 16, y), f"{len(pos)} files · {len(links)} imports", font=fonts["tiny_b"], fill=CYAN)
    y += 28
    if stop is not None:
        d.text((x0 + 16, y), f"STOP {stops.index(stop) + 1}/{len(stops)}", font=fonts["tiny_b"], fill=YELLOW)
        y += 20
        d.text((x0 + 16, y), short_label(stop["label"].rpartition(": ")[2] or stop["label"], 20),
               font=fonts["small_b"], fill=community_color(stop["index"]))
        y += 28
        d.text((x0 + 16, y), f"{stop['size']} files · cohesion {stop['cohesion']:.0%}", font=fonts["tiny"], fill=TXT)
        y += 18
        bw = (x1 - x0 - 32) * max(0.0, min(1.0, stop["cohesion"]))
        d.rectangle((x0 + 16, y, x0 + 16 + bw, y + 6), fill=alpha(community_color(stop["index"]), 0.9))
        y += 18
        d.text((x0 + 16, y), f"hub {short_label(stop['hub'].rpartition('/')[2], 18)}", font=fonts["tiny"], fill=DIM)
        y += 18
        d.text((x0 + 16, y), f"{stop['internal']} inside · {stop['external']} crossing", font=fonts["tiny"], fill=DIM)
    elif lt >= c_end and hub:
        uses = sorted({b for a, b in links if a == hub and b != hub})
        users = sorted({a for a, b in links if b == hub and a != hub})
        d.text((x0 + 16, y), "REACH // 1 hop", font=fonts["tiny_b"], fill=YELLOW)
        y += 20
        d.text((x0 + 16, y), short_label(hub.rpartition("/")[2] or hub, 20), font=fonts["small_b"], fill=TXT)
        y += 28
        d.text((x0 + 16, y), f"upstream   {len(users)} use it", font=fonts["tiny"], fill=MAGENTA)
        y += 18
        d.text((x0 + 16, y), f"downstream {len(uses)} it uses", font=fonts["tiny"], fill=CYAN)
        y += 24
        for nid in users[:4]:
            if y + 18 > side[3] - 70:
                break
            d.text((x0 + 16, y), "<- " + short_label(nid.rpartition("/")[2] or nid, 18), font=fonts["tiny"], fill=DIM)
            y += 17
    d.text((x0 + 16, side[3] - 50), "LIVE", font=fonts["tiny_b"], fill=GREEN)
    d.text((x0 + 16, side[3] - 32), short_label(f"{cfg.DIAGRAM_OUTPUT_DIR}/{cfg.FORCEGRAPH_OUTPUT}", 26),
           font=fonts["tiny"], fill=TXT)
    if lt < a_end:
        caption = f"{len(pos)} files, {len(links)} imports: the explorer's 3D view, measured offline"
    elif lt < b_end:
        caption = f"color by {mode}: the same graph, three readings"
    elif stop is not None:
        caption = f"stop {stops.index(stop) + 1}/{len(stops)}: {short_label(stop['label'], 30)}, {stop['size']} files"
    elif hub:
        caption = f"reach of {short_label(hub.rpartition('/')[2], 24)}: everything one hop away lights up"
    else:
        caption = "every file, every import, in orbit"
    draw_caption(d, caption, lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_sphere(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """The 3D force layout folds onto a globe of community caps and bundles its imports."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT VIII // THE SPHERE", fonts, cfg.VIDEO_WIDTH)
    left, right = _split_boxes(cfg)
    hud_panel(d, left, f"spherical edge bundling // community caps, beta {cfg.VIDEO_BUNDLE_BETA:.2f}", fonts, VIOLET)
    hud_panel(d, right, "globe // caps and seams", fonts, GREEN)
    layout: Optional[SphereBundleLayout] = data.get("sphere")
    if layout is None or not layout.leaves:
        d.text(((left[0] + left[2]) / 2, (left[1] + left[3]) / 2), "no communities to wrap",
               font=fonts["cap"], fill=DIM, anchor="mm")
        draw_caption(d, "flat project: nothing to bundle", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))
        return
    dur = sc["dur"]
    morph = ease(lt / max(1e-9, 0.25 * dur))
    reveal = ease((lt - 0.2 * dur) / max(1e-9, 0.3 * dur))
    yaw = 0.4 + cfg.VIDEO_SPHERE_TURNS * 2 * math.pi * lt / max(1e-9, dur)
    pitch = -0.35
    groups = layout.groups
    cycle_start = 0.55 * dur
    spot_pos = -1
    if lt > cycle_start and groups:
        span = max(0.5, (dur - cycle_start - 0.6) / len(groups))
        spot_pos = min(len(groups) - 1, int((lt - cycle_start) / span))
    spot = int(groups[spot_pos][0].split(":", 1)[0]) if spot_pos >= 0 else None
    draw_sphere3d(img, data, (left[0] + 2, left[1] + 31, left[2] - 2, left[3] - 2), cfg, yaw, pitch,
                  morph, reveal, spot, gt, fonts)
    membership = data.get("membership", {})
    x0, _, x1, _ = right
    y = right[1] + 44
    top = max([1] + [count for _l, _c, count in groups])
    for label, _cap, count in groups:
        if y + 30 > right[3] - 80:
            break
        index = int(label.split(":", 1)[0])
        on = spot is None or spot == index
        k = ease((lt - 0.4) / 1.0)
        name = short_label(label.split(":", 1)[1].rpartition(": ")[2] or label, 22)
        d.text((x0 + 18, y), name, font=fonts["tiny_b"], fill=alpha(TXT if on else DIM, k))
        d.text((x1 - 18, y), str(count), font=fonts["tiny"], fill=alpha(DIM, k), anchor="ra")
        bw = (x1 - x0 - 36) * count / top * k
        d.rectangle((x0 + 18, y + 16, x0 + 18 + max(0, bw), y + 21),
                    fill=alpha(community_color(index), 0.9 if on else 0.35))
        y += 32
    if spot is not None:
        out_n = sum(1 for a, b in data["graph_links"] if membership.get(a, -1) == spot and membership.get(b, -1) != spot)
        in_n = sum(1 for a, b in data["graph_links"] if membership.get(b, -1) == spot and membership.get(a, -1) != spot)
        d.text((x0 + 18, right[3] - 72), f"spotlight: {out_n} out · {in_n} in", font=fonts["small_b"], fill=GREEN)
    d.text((x0 + 18, right[3] - 44), "LIVE " + short_label(f"{cfg.DIAGRAM_OUTPUT_DIR}/{cfg.BUNDLEGRAPH_OUTPUT}", 34),
           font=fonts["tiny_b"], fill=TXT)
    d.text((x0 + 18, right[3] - 26), "#view=3d · beta slider · crossing only", font=fonts["tiny"], fill=DIM)
    if morph < 1:
        caption = "the force layout folds onto a globe: one cap per community"
    elif spot is None:
        caption = "every import leaves its cap, dives through the core, and lands on its target"
    else:
        caption = f"spotlight: {short_label(groups[spot_pos][0].split(':', 1)[1], 30)} and every seam it crosses"
    draw_caption(d, caption, lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_invite(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Invitation to open the live explorers, with both 3D views spinning."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    w, h = cfg.VIDEO_WIDTH, cfg.VIDEO_HEIGHT
    a = ease(lt / 0.6) * (1 - ease((lt - (sc["dur"] - 0.4)) / 0.4))
    draw_grid(img, gt, 0.6, _RENDER_BD)
    chroma_text(img, (w / 2, h * 0.09), "NOW FLY IT YOURSELF", fonts["mid"], alpha(TXT, a), spread=3, anchor="mm")
    d.text((w / 2, h * 0.16), "every view in this video is a live page you can click, drag and search",
           font=fonts["small"], fill=alpha(CYAN, a), anchor="mm")
    gap = 24
    top, bottom = int(h * 0.22), h - 70
    left = (40, top, w // 2 - gap // 2, bottom)
    right = (w // 2 + gap // 2, top, w - 40, bottom)
    out = cfg.DIAGRAM_OUTPUT_DIR
    cards = [
        (left, "graph force // 2d + 3d", CYAN, f"{out}/{cfg.FORCEGRAPH_OUTPUT}",
         ["click any file: purpose, symbols, neighbours", "reach upstream / downstream, path finder",
          "lenses: cycles, orphans, hubs  ·  color by 3 modes"]),
        (right, "edge bundles // circle + sphere", VIOLET, f"{out}/{cfg.BUNDLEGRAPH_OUTPUT}",
         ["every import routed through its community", "beta slider: straight chords to full bundles",
          "crossing-only: just the seams between subsystems"]),
    ]
    for k, (box, title, col, path, lines) in enumerate(cards):
        ka = a * ease((lt - 0.3 - 0.25 * k) / 0.6)
        if ka <= 0:
            continue
        hud_panel(d, box, title, fonts, col)
        x0, y0, x1, y1 = box
        stage = (x0 + 10, y0 + 34, x1 - 10, y1 - 112)
        spin = 0.5 + lt * 0.5
        if k == 0:
            mode = COLOR_MODES[int(lt / 1.6) % len(COLOR_MODES)]
            draw_cloud3d(img, data, stage, cfg, spin, -0.3, (0.0, 0.0, 0.0), 1.0, mode, None, None, gt, fonts)
        else:
            draw_sphere3d(img, data, stage, cfg, spin, -0.35, 1.0, 1.0, None, gt, fonts, group_labels=False)
        y = y1 - 104
        d.text((x0 + 16, y), short_label(path, 44), font=fonts["small_b"], fill=alpha(col, ka))
        y += 30
        for line in lines:
            d.text((x0 + 16, y), "> " + line, font=fonts["tiny"], fill=alpha(TXT, ka))
            y += 20
    k2 = ease((lt - 1.2) / 0.6) * a
    d.text((w / 2, h - 38), f"start at {out}/index.html  ·  maps, video, wiki and agent docs in one gallery",
           font=fonts["small_b"], fill=alpha(GREEN, k2), anchor="mm")


def _scene_dna(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Every file as a color, scanned live, with a zoom on the hub file."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    draw_header(img, d, gt, _RENDER_TOTAL, data["project"], "ACT IX // CODE DNA", fonts, cfg.VIDEO_WIDTH)
    grid_box, sec_box = _dna_boxes(cfg)
    hud_panel(d, grid_box, "sha256 per file // color = fingerprint", fonts, YELLOW)
    hud_panel(d, sec_box, "security // pattern scan", fonts, RED)
    avail_w = max(1, grid_box[2] - grid_box[0] - 60)
    avail_h = max(1, grid_box[3] - grid_box[1] - 45 - 78)
    dna = data["dna"]
    count = max(1, len(dna))
    cell = max(2, min(cfg.VIDEO_DNA_MAX_CELL, int(math.sqrt(avail_w * avail_h / count)) - 3))
    while cell > 2 and math.ceil(count / max(1, avail_w // (cell + 3))) * (cell + 3) > avail_h:
        cell -= 1
    cols = max(1, avail_w // (cell + 3))
    top = grid_box[1] + 45
    fill_p = ease(lt / 3.0)
    scan_p = ease((lt - 3.0) / max(0.5, sc["dur"] - 4.0))
    scan = int(scan_p * max(1, len(dna)))
    for i, row in enumerate(dna):
        cx = grid_box[0] + 25 + (i % cols) * (cell + 3)
        cy = top + (i // cols) * (cell + 3)
        if cy + cell > grid_box[3] - 78:
            break
        if i / max(1, len(dna)) > fill_p:
            d.rectangle((cx, cy, cx + cell, cy + cell), outline=alpha(FAINT, 0.5))
            continue
        d.rectangle((cx, cy, cx + cell, cy + cell), fill=alpha(row["color"], 1.0))
        if i == scan:
            d.rectangle((cx - 2, cy - 2, cx + cell + 2, cy + cell + 2), outline=(255, 255, 255), width=2)
    if 0 < scan_p < 1 and dna:
        sx = grid_box[0] + 25 + (scan % cols) * (cell + 3)
        d.line((sx, grid_box[1] + 36, sx, grid_box[3] - 70), fill=alpha((255, 255, 255), 0.7), width=2)
    hub = (data.get("god_details", [{}])[0].get("file", "")) if data.get("god_details") else ""
    hub_row = next((r for r in dna if r["file"] == hub), dna[0] if dna else None)
    if hub_row is not None:
        zx0, zy1 = grid_box[0] + 20, grid_box[3] - 10
        zy0 = zy1 - 56
        d.rectangle((zx0, zy0, grid_box[2] - 20, zy1), fill=(6, 3, 18, 235), outline=alpha(YELLOW, 0.7), width=1)
        d.rectangle((zx0 + 12, zy0 + 16, zx0 + 34, zy0 + 38), fill=hub_row["color"])
        d.text((zx0 + 44, zy0 + 8), f"zoom // {short_label(hub_row['file'], 30)}", font=fonts["tiny_b"], fill=TXT)
        d.text((zx0 + 44, zy0 + 26), f"sha256 {hub_row['digest'].hex()[:24]}…  ·  {hub_row['symbols']} symbols",
               font=fonts["tiny"], fill=DIM)
    x0 = sec_box[0] + 15
    d.text((x0, sec_box[1] + 40), f"{len(data['findings'])} findings", font=fonts["small_b"], fill=RED)
    y = sec_box[1] + 70
    for f in data["findings"][:6]:
        if y + 36 > sec_box[3] - 10:
            break
        sev_col = {"critical": RED, "high": ORANGE, "medium": YELLOW}.get(f["severity"], DIM)
        d.text((x0, y), f"{f['severity']} · {short_label(f['rule'], 14)} L{f['line']}", font=fonts["tiny_b"], fill=sev_col)
        d.text((x0, y + 15), short_label(f["file"], 20), font=fonts["tiny"], fill=DIM)
        y += 38
    if not data["findings"]:
        d.text((x0, sec_box[1] + 70), "no findings", font=fonts["small"], fill=GREEN)
    draw_caption(d, "same color, same bytes: clones and vendored code pop out", lt, sc["dur"], fonts, cfg.VIDEO_WIDTH, _caption_y(cfg))


def _scene_outro(img: Any, d: Any, lt: float, gt: float, sc: Dict[str, Any]) -> None:
    """Closing summary with the measured numbers."""
    assert _RENDER_D is not None and _RENDER_FONTS is not None and _RENDER_CFG is not None
    data, fonts, cfg = _RENDER_D, _RENDER_FONTS, _RENDER_CFG
    w, h = cfg.VIDEO_WIDTH, cfg.VIDEO_HEIGHT
    a = ease(lt / 0.8)
    draw_grid(img, gt, 1.0, _RENDER_BD)
    chroma_text(img, (w / 2, h * 0.18), "MAP COMPLETE", fonts["big"], alpha(GREEN, a), spread=4, anchor="mm")
    rows = [
        ("project", data["project"]),
        ("files / symbols", f"{fmt_int(data['files'])} / {fmt_int(data['symbols'])}"),
        ("imports", fmt_int(data["imports"])),
        ("layers", str(len(data["layers"]))),
        ("communities", str(len(data["communities"]))),
        ("dependency cycles", str(data["cycles"])),
        ("layer violations", str(data["violations"])),
        ("security findings", str(len(data["findings"]))),
    ]
    text = [f"{k:<22}{v}" for k, v in rows]
    bw = max([fonts["term"].getlength(r) for r in text] + [100])
    line_h = max(20, min(36, int((h * 0.62) // len(text))))
    top_y = int(h * 0.26)
    bx = (w - bw) / 2
    d.rectangle((bx - 40, top_y, bx + bw + 40, top_y + len(text) * line_h + 50), fill=(8, 4, 22, int(215 * a)))
    hud_panel(d, (bx - 40, top_y, bx + bw + 40, top_y + len(text) * line_h + 50), "telemetry // final", fonts, MAGENTA)
    for i, r in enumerate(text):
        k = ease((lt - 0.5 - i * 0.25) / 0.5)
        d.text((bx, top_y + 45 + i * line_h), r, font=fonts["term"], fill=alpha(TXT, a * k))


_SCENE_FN = {"title": _scene_title, "card": _scene_card, "layers": _scene_layers,
             "gods": _scene_gods, "tree": _scene_tree, "communities": _scene_communities,
             "graph": _scene_graph, "orbit": _scene_orbit, "bundle": _scene_bundle,
             "sphere": _scene_sphere, "dna": _scene_dna, "invite": _scene_invite,
             "outro": _scene_outro}
