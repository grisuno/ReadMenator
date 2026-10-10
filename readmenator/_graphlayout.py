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
- Spherical edge bundling: the same hierarchy on a unit sphere, each
  community owning a cap of Fibonacci lattice points sized by its
  member count, hubs inside the sphere and the root at its center.

ForceAtlas2 runs in two or three dimensions (settings.dims).

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
Point3 = Tuple[float, float, float]


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
        dims: Layout dimensions (2 or 3).
    """

    iterations: int = 300
    snapshots: int = 60
    scaling: float = 2.0
    gravity: float = 1.0
    linlog: bool = True
    tolerance: float = 1.0
    seed: int = 7
    fallback_budget: int = 20_000_000
    dims: int = 2


def _initial_positions(n: int, seed: int, dims: int = 2) -> List[Tuple[float, ...]]:
    """Seeded uniform positions inside a cube scaled to sqrt(n)."""
    rng = random.Random(seed)
    span = max(1.0, math.sqrt(n)) * 10.0
    return [tuple(rng.uniform(-span, span) for _ in range(dims)) for _ in range(n)]


def forceatlas2_frames(
    ids: Sequence[str],
    edges: Sequence[Tuple[str, str]],
    settings: Optional[ForceAtlas2Settings] = None,
) -> List[Dict[str, Tuple[float, ...]]]:
    """Run ForceAtlas2 and return evenly spaced layout snapshots.

    Args:
        ids: Node identifiers (order defines determinism).
        edges: Undirected (a, b) pairs; unknown ids and self loops are ignored.
        settings: Algorithm settings; defaults when None.

    Returns:
        Snapshots from the seeded start to the converged layout; each
        maps node id to raw coordinates ((x, y), or (x, y, z) when
        settings.dims is 3). Empty for no nodes.
    """
    cfg = settings or ForceAtlas2Settings()
    dims = 3 if cfg.dims == 3 else 2
    ids = list(ids)
    n = len(ids)
    if n == 0:
        return []
    index = {nid: i for i, nid in enumerate(ids)}
    pairs = sorted({
        (min(index[a], index[b]), max(index[a], index[b]))
        for a, b in edges if a in index and b in index and a != b
    })
    start = _initial_positions(n, cfg.seed, dims)
    if n == 1:
        origin = tuple(0.0 for _ in range(dims))
        return [{ids[0]: origin}, {ids[0]: origin}]
    try:
        import numpy as np  # noqa: F401
        raw = _fa2_numpy(n, pairs, start, cfg)
    except ImportError:
        raw = _fa2_python(n, pairs, start, cfg)
    return [{ids[i]: tuple(float(v) for v in p[i]) for i in range(n)} for p in raw]


def _snapshot_steps(iterations: int, snapshots: int) -> List[int]:
    """Iteration indices at which to record snapshots (always includes 0 and the last)."""
    count = max(2, snapshots)
    return sorted({round(i * iterations / (count - 1)) for i in range(count)})


def _fa2_numpy(n: int, pairs: List[Tuple[int, int]], start: List[Tuple[float, ...]], cfg: ForceAtlas2Settings) -> List[List[Tuple[float, ...]]]:
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
    frames: List[List[Tuple[float, ...]]] = []
    for step in range(cfg.iterations + 1):
        if step in record:
            frames.append([tuple(float(v) for v in row) for row in pos])
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


def _fa2_python(n: int, pairs: List[Tuple[int, int]], start: List[Tuple[float, ...]], cfg: ForceAtlas2Settings) -> List[List[Tuple[float, ...]]]:
    """Pure Python ForceAtlas2 with a bounded iteration budget (any dimension)."""
    iterations = max(10, min(cfg.iterations, cfg.fallback_budget // max(1, n * n)))
    dims = len(start[0]) if start else 2
    axes = range(dims)
    pos = [list(p) for p in start]
    mass = [1.0] * n
    for a, b in pairs:
        mass[a] += 1.0
        mass[b] += 1.0
    old = [[0.0] * dims for _ in range(n)]
    speed = 1.0
    record = set(_snapshot_steps(iterations, cfg.snapshots))
    frames: List[List[Tuple[float, ...]]] = []
    for step in range(iterations + 1):
        if step in record:
            frames.append([tuple(p) for p in pos])
        if step == iterations:
            break
        force = [[0.0] * dims for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                delta = [pos[i][k] - pos[j][k] for k in axes]
                d2 = sum(v * v for v in delta) + 1e-9
                f = cfg.scaling * mass[i] * mass[j] / d2
                for k in axes:
                    force[i][k] += delta[k] * f
                    force[j][k] -= delta[k] * f
        for a, b in pairs:
            delta = [pos[b][k] - pos[a][k] for k in axes]
            d = math.hypot(*delta) + 1e-9
            mag = math.log1p(d) / d if cfg.linlog else 1.0
            for k in axes:
                force[a][k] += delta[k] * mag
                force[b][k] -= delta[k] * mag
        total_swing = total_traction = 0.0
        swings = []
        for i in range(n):
            norm = math.hypot(*pos[i]) + 1e-9
            for k in axes:
                force[i][k] -= pos[i][k] / norm * cfg.gravity * mass[i]
            sw = mass[i] * math.hypot(*[force[i][k] - old[i][k] for k in axes])
            swings.append(sw)
            total_swing += sw
            total_traction += mass[i] * math.hypot(*[force[i][k] + old[i][k] for k in axes]) / 2.0
        target = cfg.tolerance * total_traction / (total_swing + 1e-9)
        speed = speed + min(target - speed, 0.5 * speed)
        for i in range(n):
            local = speed / (1.0 + math.sqrt(speed * swings[i]))
            for k in axes:
                pos[i][k] += force[i][k] * local
        old = force
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


def _bspline(control: Sequence[Tuple[float, ...]], samples: int) -> List[Tuple[float, ...]]:
    """Sample a clamped uniform cubic B-spline through a control polygon (any dimension)."""
    dims = range(len(control[0]))
    if len(control) < 3:
        a, b = control[0], control[-1]
        return [tuple(a[i] + (b[i] - a[i]) * k / samples for i in dims) for k in range(samples + 1)]
    pts = [control[0], control[0]] + list(control) + [control[-1], control[-1]]
    segments = len(pts) - 3
    out: List[Tuple[float, ...]] = []
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
            out.append(tuple(b0 * p0[i] + b1 * p1[i] + b2 * p2[i] + b3 * p3[i] for i in dims))
    return out


def _bundle_curves(
    leaves: Dict[str, Tuple[float, ...]],
    member_group: Dict[str, str],
    hub: Dict[str, Tuple[float, ...]],
    root: Tuple[float, ...],
    edges: Sequence[Tuple[str, str]],
    beta: float,
    samples: int,
) -> List[Tuple[str, str, List[Tuple[float, ...]]]]:
    """Route every edge through the group hierarchy and sample it as a B-spline.

    Cross-group edges follow leaf -> source hub -> root -> target hub -> leaf;
    same-group edges bend through the centroid of their hub and both leaves.
    The control polygon is blended toward the straight chord by 1 - beta.

    Args:
        leaves: Leaf positions (2D or 3D).
        member_group: Leaf id to group label.
        hub: Group label to hub position.
        root: Hierarchy root position.
        edges: (source, target) pairs; unknown ids and self loops are skipped.
        beta: Bundling strength in [0, 1].
        samples: Points per sampled curve.

    Returns:
        One (source, target, points) entry per kept edge.
    """
    beta = max(0.0, min(1.0, beta))
    curves: List[Tuple[str, str, List[Tuple[float, ...]]]] = []
    for a, b in edges:
        if a not in leaves or b not in leaves or a == b:
            continue
        la, lb = leaves[a], leaves[b]
        dims = range(len(la))
        ga, gb = member_group[a], member_group[b]
        if ga == gb:
            mid = hub[ga]
            inner = tuple((mid[i] + la[i] + lb[i]) / 3 for i in dims)
            control = [la, inner, lb]
        else:
            control = [la, hub[ga], root, hub[gb], lb]
        m = len(control) - 1
        straightened = [
            tuple(beta * p[i] + (1 - beta) * (la[i] + j / m * (lb[i] - la[i])) for i in dims)
            for j, p in enumerate(control)
        ]
        curves.append((a, b, _bspline(straightened, samples)))
    return curves


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
    curves = _bundle_curves(leaves, member_group, hub, (cx, cy), edges, beta, samples)
    return BundleLayout(leaves, angles, arcs, curves, center, radius)


def fibonacci_sphere(count: int) -> List[Point3]:
    """Return count nearly uniform unit vectors on a golden-angle spiral.

    Args:
        count: Number of points.

    Returns:
        Unit vectors ordered from the north pole to the south pole.
    """
    if count <= 0:
        return []
    if count == 1:
        return [(0.0, -1.0, 0.0)]
    golden = math.pi * (3.0 - math.sqrt(5.0))
    out: List[Point3] = []
    for i in range(count):
        y = 1.0 - 2.0 * (i + 0.5) / count
        ring = math.sqrt(max(0.0, 1.0 - y * y))
        theta = golden * i
        out.append((ring * math.cos(theta), y, ring * math.sin(theta)))
    return out


def _unit(v: Sequence[float]) -> Point3:
    """Normalize a 3D vector (zero vectors map to the north pole)."""
    norm = math.sqrt(sum(c * c for c in v))
    if norm < 1e-12:
        return (0.0, -1.0, 0.0)
    return (v[0] / norm, v[1] / norm, v[2] / norm)


@dataclass(frozen=True)
class SphereBundleLayout:
    """Spherical hierarchical edge bundling result.

    Attributes:
        leaves: Leaf positions on the sphere surface.
        groups: Group caps as (label, unit center, member count).
        hubs: Group hub positions inside the sphere.
        curves: One sampled 3D polyline per edge as (source, target, points).
        radius: Sphere radius.
    """

    leaves: Dict[str, Point3]
    groups: List[Tuple[str, Point3, int]]
    hubs: Dict[str, Point3]
    curves: List[Tuple[str, str, List[Tuple[float, ...]]]]
    radius: float


def _split_caps(
    labels: List[str],
    sizes: Dict[str, int],
    points: List[int],
    lattice: List[Point3],
    out: Dict[str, List[int]],
) -> None:
    """Recursively bisect lattice points between runs of groups of matching size.

    Args:
        labels: Group labels in caller order.
        sizes: Group label to member count (sums to len(points)).
        points: Lattice indices to distribute.
        lattice: Unit vectors of the full lattice.
        out: Receives group label to its lattice indices.
    """
    if len(labels) == 1:
        out[labels[0]] = points
        return
    total = sum(sizes[label] for label in labels)
    best, cut, running = total, 1, 0
    for i in range(1, len(labels)):
        running += sizes[labels[i - 1]]
        gap = abs(2 * running - total)
        if gap < best:
            best, cut = gap, i
    left_count = sum(sizes[label] for label in labels[:cut])
    spread = []
    for k in range(3):
        values = [lattice[pi][k] for pi in points]
        spread.append(max(values) - min(values))
    axis = max(range(3), key=lambda k: (spread[k], -k))
    ordered = sorted(points, key=lambda pi: (lattice[pi][axis], pi))
    _split_caps(labels[:cut], sizes, ordered[:left_count], lattice, out)
    _split_caps(labels[cut:], sizes, ordered[left_count:], lattice, out)


def spherical_edge_bundling(
    groups: Dict[str, List[str]],
    edges: Sequence[Tuple[str, str]],
    radius: float = 1.0,
    beta: float = 0.85,
    samples: int = 24,
    inner_ratio: float = 0.55,
) -> SphereBundleLayout:
    """Lay leaves on a sphere in community caps and bundle edges through the hierarchy.

    Leaves occupy a Fibonacci lattice with one point per member. The
    lattice is split recursively: the groups are cut into two runs of
    nearly equal total size, the points are sorted along their axis of
    largest spread and cut at the same count, and each half recurses.
    Every community therefore owns one contiguous cap whose area matches
    its size exactly. Inside a cap the points nearest its mean direction
    go to the members listed first (callers list hubs first). Each hub
    sits at the cap's mean direction scaled by inner_ratio; the root is
    the sphere center.

    Args:
        groups: Ordered mapping of group label to member ids.
        edges: (source, target) pairs between members.
        radius: Sphere radius.
        beta: Bundling strength in [0, 1].
        samples: Points per sampled curve.
        inner_ratio: Radius ratio of the group hubs.

    Returns:
        SphereBundleLayout with leaf positions, caps, hubs, and curves.
    """
    labels = [g for g in groups if groups[g]]
    total = sum(len(groups[g]) for g in labels)
    if total == 0:
        return SphereBundleLayout({}, [], {}, [], radius)
    lattice = fibonacci_sphere(total)
    regions: Dict[str, List[int]] = {}
    _split_caps(labels, {label: len(groups[label]) for label in labels},
                list(range(total)), lattice, regions)
    leaves: Dict[str, Point3] = {}
    hubs: Dict[str, Point3] = {}
    caps: List[Tuple[str, Point3, int]] = []
    member_group: Dict[str, str] = {}
    for label in labels:
        region = regions[label]
        center = _unit([sum(lattice[pi][k] for pi in region) for k in range(3)])
        points = sorted(region, key=lambda pi: (-sum(lattice[pi][k] * center[k] for k in range(3)), pi))
        for nid, pi in zip(groups[label], points):
            p = lattice[pi]
            leaves[nid] = (p[0] * radius, p[1] * radius, p[2] * radius)
            member_group[nid] = label
        hubs[label] = (center[0] * radius * inner_ratio, center[1] * radius * inner_ratio,
                       center[2] * radius * inner_ratio)
        caps.append((label, center, len(groups[label])))
    curves = _bundle_curves(leaves, member_group, hubs, (0.0, 0.0, 0.0), edges, beta, samples)
    return SphereBundleLayout(leaves, caps, hubs, curves, radius)


def normalize_cloud(
    points: Dict[str, Tuple[float, ...]],
    quantile: float = 0.85,
    max_radius: float = 1.3,
) -> Dict[str, Point3]:
    """Center a 3D point cloud, scale a radius quantile to 1, and pull outliers in.

    Force layouts push isolated files far from the core; scaling by the
    full extent would shrink the core to a dot. Points beyond radius 1
    are compressed smoothly (tanh) so none lies past max_radius.

    Args:
        points: Raw 3D positions.
        quantile: Fraction of points that end up inside the unit sphere.
        max_radius: Hard bound on the radius after compression (> 1).

    Returns:
        Normalized positions (empty for no points).
    """
    if not points:
        return {}
    n = len(points)
    mean = [sum(p[k] for p in points.values()) / n for k in range(3)]
    radii = sorted(math.sqrt(sum((p[k] - mean[k]) ** 2 for k in range(3))) for p in points.values())
    cut = radii[min(n - 1, int(n * max(0.0, min(1.0, quantile))))] or 1.0
    room = max(1e-9, max_radius - 1.0)
    out: Dict[str, Point3] = {}
    for nid, p in points.items():
        v = [(p[k] - mean[k]) / cut for k in range(3)]
        r = math.sqrt(sum(c * c for c in v))
        if r > 1.0:
            factor = (1.0 + room * math.tanh((r - 1.0) / room)) / r
            v = [c * factor for c in v]
        out[nid] = (v[0], v[1], v[2])
    return out
