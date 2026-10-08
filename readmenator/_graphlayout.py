"""Deterministic graph layout algorithms for animated renders.

Implements two layout families used by the cinematic video:

- ForceAtlas2 (Jacomy et al., 2014): degree-weighted repulsion,
  LinLog attraction, degree-weighted gravity, and the adaptive global
  speed driven by swing and traction. Snapshots are recorded during
  the run so the convergence itself can be animated.
- Hierarchical edge bundling (Holten, 2006): leaves placed on a circle
  grouped by community, every edge routed through the community
  hierarchy as a control polygon, straightened by the bundling
  strength beta, and sampled as a uniform cubic B-spline.

numpy is used when available for the O(n^2) force pass; a pure Python
path keeps the module dependency-free (the iteration budget shrinks
to keep the fallback fast). Results are deterministic for a given
seed and input ordering.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

Point = Tuple[float, float]


@dataclass(frozen=True)
class ForceAtlas2Settings:
    """Tuneables for ForceAtlas2.

    Attributes:
        iterations: Total simulation steps.
        snapshots: Number of recorded intermediate layouts (>= 2).
        scaling: Repulsion constant kr.
        gravity: Gravity constant kg (pulls every node to the origin).
        linlog: Use log(1 + d) attraction for tighter clusters.
        tolerance: Swing tolerance of the adaptive speed.
        seed: Random seed for the initial positions.
        fallback_budget: Max n^2 * iterations for the pure Python path.
    """

    iterations: int = 300
    snapshots: int = 60
    scaling: float = 2.0
    gravity: float = 1.0
    linlog: bool = True
    tolerance: float = 1.0
    seed: int = 7
    fallback_budget: int = 20_000_000


def _initial_positions(n: int, seed: int) -> List[Point]:
    """Seeded uniform positions inside a square scaled to sqrt(n)."""
    rng = random.Random(seed)
    span = max(1.0, math.sqrt(n)) * 10.0
    return [(rng.uniform(-span, span), rng.uniform(-span, span)) for _ in range(n)]


def forceatlas2_frames(
    ids: Sequence[str],
    edges: Sequence[Tuple[str, str]],
    settings: Optional[ForceAtlas2Settings] = None,
) -> List[Dict[str, Point]]:
    """Run ForceAtlas2 and return evenly spaced layout snapshots.

    Args:
        ids: Node identifiers (order defines determinism).
        edges: Undirected (a, b) pairs; unknown ids and self loops are ignored.
        settings: Algorithm settings; defaults when None.

    Returns:
        Snapshots from the seeded start to the converged layout; each
        maps node id to raw (x, y) coordinates. Empty for no nodes.
    """
    cfg = settings or ForceAtlas2Settings()
    ids = list(ids)
    n = len(ids)
    if n == 0:
        return []
    index = {nid: i for i, nid in enumerate(ids)}
    pairs = sorted({
        (min(index[a], index[b]), max(index[a], index[b]))
        for a, b in edges if a in index and b in index and a != b
    })
    start = _initial_positions(n, cfg.seed)
    if n == 1:
        return [{ids[0]: (0.0, 0.0)}, {ids[0]: (0.0, 0.0)}]
    try:
        import numpy as np  # noqa: F401
        raw = _fa2_numpy(n, pairs, start, cfg)
    except ImportError:
        raw = _fa2_python(n, pairs, start, cfg)
    return [{ids[i]: (float(p[i][0]), float(p[i][1])) for i in range(n)} for p in raw]


def _snapshot_steps(iterations: int, snapshots: int) -> List[int]:
    """Iteration indices at which to record snapshots (always includes 0 and the last)."""
    count = max(2, snapshots)
    return sorted({round(i * iterations / (count - 1)) for i in range(count)})


def _fa2_numpy(n: int, pairs: List[Tuple[int, int]], start: List[Point], cfg: ForceAtlas2Settings) -> List[List[Point]]:
    """Vectorised ForceAtlas2 with adaptive global speed."""
    import numpy as np

    pos = np.array(start, dtype=float)
    mass = np.ones(n)
    if pairs:
        src = np.array([a for a, _ in pairs])
        dst = np.array([b for _, b in pairs])
        np.add.at(mass, src, 1.0)
        np.add.at(mass, dst, 1.0)
    else:
        src = dst = np.array([], dtype=int)
    old = np.zeros_like(pos)
    speed = 1.0
    record = set(_snapshot_steps(cfg.iterations, cfg.snapshots))
    frames: List[List[Point]] = []
    for step in range(cfg.iterations + 1):
        if step in record:
            frames.append([(float(x), float(y)) for x, y in pos])
        if step == cfg.iterations:
            break
        delta = pos[:, None, :] - pos[None, :, :]
        dist2 = (delta ** 2).sum(-1) + 1e-9
        rep = cfg.scaling * (mass[:, None] * mass[None, :]) / dist2
        np.fill_diagonal(rep, 0.0)
        force = (delta * rep[:, :, None]).sum(1)
        if len(src):
            vec = pos[dst] - pos[src]
            dist = np.sqrt((vec ** 2).sum(-1)) + 1e-9
            mag = np.log1p(dist) / dist if cfg.linlog else np.ones_like(dist)
            pull = vec * mag[:, None]
            np.add.at(force, src, pull)
            np.add.at(force, dst, -pull)
        norm = np.sqrt((pos ** 2).sum(-1)) + 1e-9
        force -= pos / norm[:, None] * (cfg.gravity * mass)[:, None]
        swing = mass * np.sqrt(((force - old) ** 2).sum(-1))
        traction = mass * np.sqrt(((force + old) ** 2).sum(-1)) / 2.0
        total_swing, total_traction = float(swing.sum()), float(traction.sum())
        target = cfg.tolerance * total_traction / (total_swing + 1e-9)
        speed = speed + min(target - speed, 0.5 * speed)
        local = speed / (1.0 + np.sqrt(speed * swing))
        pos = pos + force * local[:, None]
        old = force
    return frames


def _fa2_python(n: int, pairs: List[Tuple[int, int]], start: List[Point], cfg: ForceAtlas2Settings) -> List[List[Point]]:
    """Pure Python ForceAtlas2 with a bounded iteration budget."""
    iterations = max(10, min(cfg.iterations, cfg.fallback_budget // max(1, n * n)))
    xs = [p[0] for p in start]
    ys = [p[1] for p in start]
    mass = [1.0] * n
    for a, b in pairs:
        mass[a] += 1.0
        mass[b] += 1.0
    old = [(0.0, 0.0)] * n
    speed = 1.0
    record = set(_snapshot_steps(iterations, cfg.snapshots))
    frames: List[List[Point]] = []
    for step in range(iterations + 1):
        if step in record:
            frames.append(list(zip(xs, ys)))
        if step == iterations:
            break
        fx = [0.0] * n
        fy = [0.0] * n
        for i in range(n):
            for j in range(i + 1, n):
                dx, dy = xs[i] - xs[j], ys[i] - ys[j]
                d2 = dx * dx + dy * dy + 1e-9
                f = cfg.scaling * mass[i] * mass[j] / d2
                fx[i] += dx * f
                fy[i] += dy * f
                fx[j] -= dx * f
                fy[j] -= dy * f
        for a, b in pairs:
            dx, dy = xs[b] - xs[a], ys[b] - ys[a]
            d = math.hypot(dx, dy) + 1e-9
            mag = math.log1p(d) / d if cfg.linlog else 1.0
            fx[a] += dx * mag
            fy[a] += dy * mag
            fx[b] -= dx * mag
            fy[b] -= dy * mag
        total_swing = total_traction = 0.0
        swings = []
        for i in range(n):
            norm = math.hypot(xs[i], ys[i]) + 1e-9
            fx[i] -= xs[i] / norm * cfg.gravity * mass[i]
            fy[i] -= ys[i] / norm * cfg.gravity * mass[i]
            sw = mass[i] * math.hypot(fx[i] - old[i][0], fy[i] - old[i][1])
            swings.append(sw)
            total_swing += sw
            total_traction += mass[i] * math.hypot(fx[i] + old[i][0], fy[i] + old[i][1]) / 2.0
        target = cfg.tolerance * total_traction / (total_swing + 1e-9)
        speed = speed + min(target - speed, 0.5 * speed)
        for i in range(n):
            local = speed / (1.0 + math.sqrt(speed * swings[i]))
            xs[i] += fx[i] * local
            ys[i] += fy[i] * local
        old = list(zip(fx, fy))
    return frames


def fit_frames(
    frames: List[Dict[str, Point]],
    box: Tuple[float, float, float, float],
    margin: float,
    trim: float = 0.0,
) -> List[Dict[str, Point]]:
    """Map raw snapshots into a pixel box using the final layout's bounds.

    Earlier snapshots share the final camera, so the animation shows the
    graph contracting into place. Coordinates are clamped to the box.

    Args:
        frames: Raw snapshots from forceatlas2_frames.
        box: Target (x0, y0, x1, y1) pixel box.
        margin: Inner margin in pixels.
        trim: Fraction of outliers ignored on each side when fitting.

    Returns:
        Snapshots in pixel coordinates.
    """
    if not frames:
        return []
    final = frames[-1]
    xs = sorted(p[0] for p in final.values())
    ys = sorted(p[1] for p in final.values())
    cut = int(len(xs) * max(0.0, min(0.45, trim)))
    lo_x, hi_x = xs[cut], xs[len(xs) - 1 - cut]
    lo_y, hi_y = ys[cut], ys[len(ys) - 1 - cut]
    x0, y0, x1, y1 = box
    w = max(1.0, x1 - x0 - 2 * margin)
    h = max(1.0, y1 - y0 - 2 * margin)
    span = max(hi_x - lo_x, (hi_y - lo_y) * w / h, 1e-9)
    scale = w / span
    cx, cy = (lo_x + hi_x) / 2, (lo_y + hi_y) / 2
    out: List[Dict[str, Point]] = []
    for frame in frames:
        mapped: Dict[str, Point] = {}
        for nid, (x, y) in frame.items():
            px = (x0 + x1) / 2 + (x - cx) * scale
            py = (y0 + y1) / 2 + (y - cy) * scale
            mapped[nid] = (min(x1 - margin, max(x0 + margin, px)), min(y1 - margin, max(y0 + margin, py)))
        out.append(mapped)
    return out


def interpolate_frames(frames: List[Dict[str, Point]], t: float) -> Dict[str, Point]:
    """Linear interpolation between snapshots for a progress t in [0, 1]."""
    if not frames:
        return {}
    if len(frames) == 1 or t >= 1.0:
        return dict(frames[-1])
    t = max(0.0, t)
    pos = t * (len(frames) - 1)
    i = int(pos)
    f = pos - i
    a, b = frames[i], frames[min(i + 1, len(frames) - 1)]
    return {nid: (a[nid][0] + (b[nid][0] - a[nid][0]) * f, a[nid][1] + (b[nid][1] - a[nid][1]) * f) for nid in a}


@dataclass(frozen=True)
class BundleLayout:
    """Radial hierarchical edge bundling result.

    Attributes:
        leaves: Leaf positions on the outer circle.
        angles: Leaf angles in radians.
        groups: Group arcs as (label, start angle, end angle, member count).
        curves: One sampled polyline per edge as (source, target, points).
        center: Circle center.
        radius: Outer radius.
    """

    leaves: Dict[str, Point]
    angles: Dict[str, float]
    groups: List[Tuple[str, float, float, int]]
    curves: List[Tuple[str, str, List[Point]]]
    center: Point
    radius: float


def _bspline(control: List[Point], samples: int) -> List[Point]:
    """Sample a clamped uniform cubic B-spline through a control polygon."""
    if len(control) < 3:
        a, b = control[0], control[-1]
        return [(a[0] + (b[0] - a[0]) * k / samples, a[1] + (b[1] - a[1]) * k / samples) for k in range(samples + 1)]
    pts = [control[0], control[0]] + control + [control[-1], control[-1]]
    segments = len(pts) - 3
    out: List[Point] = []
    per = max(2, samples // max(1, segments))
    for s in range(segments):
        p0, p1, p2, p3 = pts[s], pts[s + 1], pts[s + 2], pts[s + 3]
        for k in range(per + (1 if s == segments - 1 else 0)):
            t = k / per
            t2, t3 = t * t, t * t * t
            b0 = (1 - t) ** 3 / 6
            b1 = (3 * t3 - 6 * t2 + 4) / 6
            b2 = (-3 * t3 + 3 * t2 + 3 * t + 1) / 6
            b3 = t3 / 6
            out.append((
                b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0],
                b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1],
            ))
    return out


def hierarchical_edge_bundling(
    groups: Dict[str, List[str]],
    edges: Sequence[Tuple[str, str]],
    center: Point,
    radius: float,
    beta: float = 0.85,
    samples: int = 24,
    group_gap: float = 0.04,
    inner_ratio: float = 0.55,
) -> BundleLayout:
    """Lay leaves on a circle by group and bundle edges through the hierarchy.

    Args:
        groups: Ordered mapping of group label to member ids.
        edges: (source, target) pairs between members.
        center: Circle center in pixels.
        radius: Outer radius in pixels.
        beta: Bundling strength in [0, 1] (1 = fully bundled).
        samples: Points per sampled curve.
        group_gap: Angular gap between groups in radians.
        inner_ratio: Radius ratio of the group control points.

    Returns:
        BundleLayout with leaf positions, group arcs, and sampled curves.
    """
    cx, cy = center
    labels = [g for g in groups if groups[g]]
    total = sum(len(groups[g]) for g in labels)
    if total == 0:
        return BundleLayout({}, {}, [], [], center, radius)
    usable = 2 * math.pi - group_gap * len(labels)
    step = usable / total
    angle = -math.pi / 2
    leaves: Dict[str, Point] = {}
    angles: Dict[str, float] = {}
    arcs: List[Tuple[str, float, float, int]] = []
    hub: Dict[str, Point] = {}
    member_group: Dict[str, str] = {}
    for label in labels:
        start = angle
        for nid in groups[label]:
            a = angle + step / 2
            leaves[nid] = (cx + radius * math.cos(a), cy + radius * math.sin(a))
            angles[nid] = a
            member_group[nid] = label
            angle += step
        end = angle
        mid = (start + end) / 2
        hub[label] = (cx + radius * inner_ratio * math.cos(mid), cy + radius * inner_ratio * math.sin(mid))
        arcs.append((label, start, end, len(groups[label])))
        angle += group_gap
    curves: List[Tuple[str, str, List[Point]]] = []
    beta = max(0.0, min(1.0, beta))
    for a, b in edges:
        if a not in leaves or b not in leaves or a == b:
            continue
        ga, gb = member_group[a], member_group[b]
        if ga == gb:
            mid = hub[ga]
            inner = ((mid[0] + leaves[a][0] + leaves[b][0]) / 3, (mid[1] + leaves[a][1] + leaves[b][1]) / 3)
            control = [leaves[a], inner, leaves[b]]
        else:
            control = [leaves[a], hub[ga], (cx, cy), hub[gb], leaves[b]]
        p0, pn = control[0], control[-1]
        m = len(control) - 1
        straightened = [
            (beta * p[0] + (1 - beta) * (p0[0] + i / m * (pn[0] - p0[0])),
             beta * p[1] + (1 - beta) * (p0[1] + i / m * (pn[1] - p0[1])))
            for i, p in enumerate(control)
        ]
        curves.append((a, b, _bspline(straightened, samples)))
    return BundleLayout(leaves, angles, arcs, curves, center, radius)
