"""Graph analysis engine for the readmenator knowledge graph.

Provides community detection (Louvain-like greedy modularity), god
node identification (degree/PageRank centrality), surprising connection
discovery (cross-community bridges), and suggested exploration questions
derived from graph structure. All operations are deterministic and
token-free.
"""

from __future__ import annotations

import hashlib
import math
import random
from collections import defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node


def dominant_directory(file_ids: Set[str]) -> str:
    """Return the most informative directory label for a set of files.

    Highest file count wins; ties prefer the longest (most specific)
    directory so that ``sandbox`` beats ``.``; remaining ties go
    alphabetical. ``"."`` is reported as ``"root"``.
    """
    counts: Dict[str, int] = {}
    for fid in sorted(file_ids):
        parent = fid.rsplit("/", 1)[0] if "/" in fid else "."
        counts[parent] = counts.get(parent, 0) + 1
    if not counts:
        return "root"
    ranked = sorted(counts, key=lambda d: (-counts[d], -len(d), d))
    best = ranked[0]
    return "root" if best == "." else best


def _is_test_path(file_id: str) -> bool:
    """Return whether a project path looks like a test file or lives under tests/."""
    base = file_id.rsplit("/", 1)[-1].lower()
    return base.startswith("test") or "_test." in base or "/tests/" in f"/{file_id.lower()}"


class GraphAnalyzer:
    """Deterministic graph analysis over scanned nodes and edges.

    Builds an internal adjacency graph from import edges, then applies
    community detection, centrality scoring, cross-community bridge
    discovery, and question generation without any external API calls.
    """

    def __init__(self, config: Config):
        """Initialise with application configuration.

        Args:
            config: Settings for thresholds and limits.
        """
        self._config = config

    def analyze(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> AnalysisResult:
        """Run the full analysis pipeline and return structured results.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges from the scanner.
            resolved_edges: Optional list of resolved-import edges (source and
                target are both project file IDs).

        Returns:
            An AnalysisResult with god nodes, communities, surprising
            connections, and suggested questions.
        """
        all_edges = edges + (resolved_edges or [])
        adjacency = self._build_adjacency(nodes, all_edges)
        reverse_adjacency = self._build_reverse_adjacency(adjacency)
        god_nodes = self._compute_god_nodes(nodes, adjacency, reverse_adjacency)
        communities = self._detect_communities(nodes, adjacency)
        community_labels = self._label_communities(nodes, communities)
        community_map = self._build_community_map(communities)
        cohesion = self._compute_cohesion(communities, adjacency)
        surprising = self._find_surprising_connections(
            nodes, adjacency, community_map
        )
        questions = self._suggest_questions(
            nodes, god_nodes, communities, community_labels, surprising, adjacency
        )

        community_results = [
            CommunityResult(
                community_id=cid,
                label=community_labels.get(cid, f"Community {cid}"),
                file_ids=set(members),
                cohesion=cohesion.get(cid, 0.0),
                size=len(members),
            )
            for cid, members in communities.items()
        ]

        return AnalysisResult(
            god_nodes=god_nodes,
            communities=community_results,
            surprising_connections=surprising,
            suggested_questions=questions,
            node_count=len(nodes),
            edge_count=len(all_edges),
        )

    def _build_adjacency(
        self, nodes: List[Node], edges: List[Edge]
    ) -> Dict[str, Set[str]]:
        """Build an undirected adjacency map from import edges."""
        file_ids = {n.node_id for n in nodes}
        adj: Dict[str, Set[str]] = defaultdict(set)
        for edge in edges:
            src = edge.source
            tgt = edge.target
            if src in file_ids and tgt in file_ids:
                adj[src].add(tgt)
                adj[tgt].add(src)
        return adj

    def _build_reverse_adjacency(
        self, adjacency: Dict[str, Set[str]]
    ) -> Dict[str, Set[str]]:
        """Build a directed reverse adjacency (incoming edges) map."""
        rev: Dict[str, Set[str]] = defaultdict(set)
        for src, targets in adjacency.items():
            for tgt in targets:
                rev[tgt].add(src)
        return rev

    def _compute_god_nodes(
        self,
        nodes: List[Node],
        adjacency: Dict[str, Set[str]],
        reverse_adjacency: Dict[str, Set[str]],
    ) -> List[Tuple[str, float]]:
        """Compute the most central nodes using combined degree centrality.

        Score is a combination of out-degree (imports), in-degree (imported-by),
        and symbol count. Higher score means more architecturally significant.
        """
        scores: List[Tuple[str, float]] = []
        for node in nodes:
            nid = node.node_id
            out_deg = len(adjacency.get(nid, set()))
            in_deg = len(reverse_adjacency.get(nid, set()))
            symbol_weight = len(node.symbols) * 0.1
            score = float(out_deg + in_deg + symbol_weight)
            scores.append((nid, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[: self._config.GOD_NODE_TOP_N]

    def _detect_communities(
        self, nodes: List[Node], adjacency: Dict[str, Set[str]]
    ) -> Dict[int, List[str]]:
        """Detect communities using label propagation.

        Each node adopts the label with the highest weighted vote among
        its neighbors. Iterates until convergence or max iterations reached.
        Deterministic: content-seeded order, sorted neighbors, min-label
        tie-break within COMMUNITY_VOTE_EPSILON.
        """
        if not nodes or not adjacency:
            return {}
        if self._config.COMMUNITY_ALGORITHM == "louvain":
            return self._finalize_communities(
                self._louvain([n.node_id for n in nodes], adjacency), adjacency,
            )

        file_ids = [n.node_id for n in nodes]
        labels: Dict[str, int] = {fid: i for i, fid in enumerate(file_ids)}
        seed = int(
            hashlib.sha256("|".join(sorted(file_ids)).encode()).hexdigest(), 16
        ) % (2 ** 32)
        rng = random.Random(seed)
        weights = self._vote_weights(file_ids, adjacency)
        epsilon = self._config.COMMUNITY_VOTE_EPSILON

        for _iteration in range(50):
            changed = False
            node_list = list(file_ids)
            rng.shuffle(node_list)
            for fid in node_list:
                neighbor_labels: Dict[int, float] = {}
                for neighbor in sorted(adjacency.get(fid, set())):
                    nl = labels.get(neighbor)
                    if nl is not None:
                        neighbor_labels[nl] = neighbor_labels.get(nl, 0.0) + weights[neighbor]
                if not neighbor_labels:
                    continue
                max_count = max(neighbor_labels.values())
                best_labels = [
                    lab for lab, cnt in neighbor_labels.items()
                    if cnt >= max_count - epsilon
                ]
                best_label = min(best_labels) if best_labels else labels[fid]
                if best_label != labels[fid]:
                    labels[fid] = best_label
                    changed = True
            if not changed:
                break

        return self._finalize_communities(labels, adjacency)

    def _finalize_communities(
        self, labels: Dict[str, int], adjacency: Dict[str, Set[str]]
    ) -> Dict[int, List[str]]:
        """Group labels, fold tiny groups, drop undersized ones, renumber by size.

        Communities are numbered largest first (ties by first member) so
        ids and wiki page names stay stable and meaningful across runs.
        """
        weights = self._vote_weights(list(labels), adjacency)
        result: Dict[int, List[str]] = {}
        for fid, lab in labels.items():
            result.setdefault(lab, []).append(fid)
        result = self._merge_small_communities(result, adjacency, weights)
        kept = [
            sorted(members) for members in result.values()
            if len(members) >= self._config.COMMUNITY_MIN_SIZE
        ]
        kept.sort(key=lambda members: (-len(members), members[0]))
        return {index: members for index, members in enumerate(kept)}

    def _louvain(
        self, file_ids: List[str], adjacency: Dict[str, Set[str]]
    ) -> Dict[str, int]:
        """Partition files by greedy modularity optimisation (Louvain method).

        Pure Python and deterministic: nodes are visited in sorted order,
        moves require a strictly positive gain, and ties pick the smallest
        community key. Modularity already discounts hub degree, so shared
        modules do not swallow the project.

        Args:
            file_ids: All file ids.
            adjacency: Undirected adjacency between files.

        Returns:
            Mapping of file id to community label.
        """
        resolution = self._config.COMMUNITY_RESOLUTION
        epsilon = self._config.COMMUNITY_VOTE_EPSILON
        ids = sorted(set(file_ids))
        index = {fid: i for i, fid in enumerate(ids)}
        graph: Dict[int, Dict[int, float]] = {i: {} for i in range(len(ids))}
        for fid in ids:
            for neighbor in adjacency.get(fid, set()):
                if neighbor in index and neighbor != fid:
                    graph[index[fid]][index[neighbor]] = 1.0
        membership = list(range(len(ids)))
        for _level in range(self._config.COMMUNITY_MAX_LEVELS):
            partition, improved = self._louvain_pass(graph, resolution, epsilon)
            if not improved:
                break
            membership = [partition[m] for m in membership]
            graph = self._aggregate(graph, partition)
        return {fid: membership[i] for i, fid in enumerate(ids)}

    def _louvain_pass(
        self, graph: Dict[int, Dict[int, float]], resolution: float, epsilon: float,
    ) -> Tuple[Dict[int, int], bool]:
        """Run Louvain local moves on one level and return a compact partition."""
        degree = {n: sum(nbrs.values()) for n, nbrs in graph.items()}
        total = sum(degree.values())
        community = {n: n for n in graph}
        if total <= 0:
            return community, False
        tot = dict(degree)
        improved = False
        for _sweep in range(self._config.COMMUNITY_MAX_SWEEPS):
            moved = False
            for node in sorted(graph):
                current = community[node]
                k_i = degree[node]
                links: Dict[int, float] = {}
                for neighbor, weight in graph[node].items():
                    if neighbor != node:
                        links[community[neighbor]] = links.get(community[neighbor], 0.0) + weight
                tot[current] -= k_i
                best = current
                best_gain = links.get(current, 0.0) - resolution * tot[current] * k_i / total
                for target in sorted(links):
                    gain = links[target] - resolution * tot[target] * k_i / total
                    if gain > best_gain + epsilon:
                        best, best_gain = target, gain
                tot[best] += k_i
                if best != current:
                    community[node] = best
                    moved = True
                    improved = True
            if not moved:
                break
        renumber: Dict[int, int] = {}
        for node in sorted(graph):
            renumber.setdefault(community[node], len(renumber))
        return {node: renumber[community[node]] for node in graph}, improved

    @staticmethod
    def _aggregate(
        graph: Dict[int, Dict[int, float]], partition: Dict[int, int],
    ) -> Dict[int, Dict[int, float]]:
        """Collapse each community into one weighted super node."""
        merged: Dict[int, Dict[int, float]] = {c: {} for c in set(partition.values())}
        for node, nbrs in graph.items():
            source = partition[node]
            for neighbor, weight in nbrs.items():
                target = partition[neighbor]
                merged[source][target] = merged[source].get(target, 0.0) + weight
        return merged

    def _merge_small_communities(
        self,
        groups: Dict[int, List[str]],
        adjacency: Dict[str, Set[str]],
        weights: Dict[str, float],
    ) -> Dict[int, List[str]]:
        """Fold communities smaller than COMMUNITY_MERGE_BELOW into their best neighbor.

        Label propagation leaves many module-plus-test pairs; each would
        become its own wiki page. The smallest group first joins the
        neighboring community it shares the most vote weight with (ties
        to the lowest label). Isolated groups are kept unchanged.
        """
        threshold = self._config.COMMUNITY_MERGE_BELOW
        merged = {lab: list(members) for lab, members in groups.items()}
        if threshold <= 1:
            return merged
        owner = {fid: lab for lab, members in merged.items() for fid in members}
        while True:
            small = sorted(
                (len(members), lab) for lab, members in merged.items()
                if len(members) < threshold
            )
            moved = False
            for _size, lab in small:
                links: Dict[int, float] = {}
                for fid in sorted(merged[lab]):
                    for neighbor in sorted(adjacency.get(fid, set())):
                        other = owner.get(neighbor)
                        if other is None or other == lab:
                            continue
                        links[other] = links.get(other, 0.0) + weights.get(neighbor, 1.0)
                if not links:
                    continue
                top = max(links.values())
                target = min(
                    other for other, weight in links.items()
                    if weight >= top - self._config.COMMUNITY_VOTE_EPSILON
                )
                for fid in merged[lab]:
                    owner[fid] = target
                merged[target].extend(merged.pop(lab))
                moved = True
                break
            if not moved:
                return merged

    def _vote_weights(
        self, file_ids: List[str], adjacency: Dict[str, Set[str]]
    ) -> Dict[str, float]:
        """Return each node's label-propagation vote weight.

        With COMMUNITY_HUB_DAMPING a neighbor votes with weight
        ``1 / log2(2 + degree)``: hubs such as shared models or config,
        which nearly every file imports, stop pulling the whole project
        into one giant community, while ordinary neighbors keep full say.
        """
        if not self._config.COMMUNITY_HUB_DAMPING:
            return {fid: 1.0 for fid in file_ids}
        return {
            fid: 1.0 / math.log2(2 + len(adjacency.get(fid, ())))
            for fid in file_ids
        }

    def _label_communities(
        self, nodes: List[Node], communities: Dict[int, List[str]]
    ) -> Dict[int, str]:
        """Generate human-readable labels for communities.

        Labels are based on the most common directory within the community.
        """
        labels: Dict[int, str] = {}
        node_map = {n.node_id: n for n in nodes}
        for cid, members in communities.items():
            member_nodes = [node_map[mid] for mid in members if mid in node_map]
            if not member_nodes:
                labels[cid] = f"Community {cid}"
                continue
            production = {n.node_id for n in member_nodes if not _is_test_path(n.node_id)}
            labels[cid] = dominant_directory(production or {n.node_id for n in member_nodes})
        counts: Dict[str, int] = {}
        for label in labels.values():
            counts[label] = counts.get(label, 0) + 1
        for cid, members in communities.items():
            if counts.get(labels[cid], 0) < 2:
                continue
            core = self._core_file(members, node_map)
            if core:
                labels[cid] = f"{labels[cid]}: {core}"
        return labels

    @staticmethod
    def _core_file(members: List[str], node_map: Dict[str, Node]) -> str:
        """Return the stem of a community's most symbol-rich non-test file.

        Used to tell apart communities that share a dominant directory,
        so labels read ``pkg: _video`` instead of an opaque number.
        """
        candidates = [m for m in members if m in node_map and not _is_test_path(m)]
        if not candidates:
            candidates = [m for m in members if m in node_map]
        if not candidates:
            return ""
        best = min(candidates, key=lambda m: (-len(node_map[m].symbols), m))
        stem = best.rsplit("/", 1)[-1]
        return stem.rsplit(".", 1)[0] if "." in stem else stem

    def _build_community_map(
        self, communities: Dict[int, List[str]]
    ) -> Dict[str, int]:
        """Build a reverse map from file ID to community ID."""
        cmap: Dict[str, int] = {}
        for cid, members in communities.items():
            for mid in members:
                cmap[mid] = cid
        return cmap

    def _compute_cohesion(
        self,
        communities: Dict[int, List[str]],
        adjacency: Dict[str, Set[str]],
    ) -> Dict[int, float]:
        """Compute cohesion score for each community.

        Cohesion = internal edges / (internal edges + external edges).
        """
        scores: Dict[int, float] = {}
        for cid, members in communities.items():
            member_set = set(members)
            internal = 0
            external = 0
            for mid in members:
                for neighbor in adjacency.get(mid, set()):
                    if neighbor in member_set:
                        internal += 1
                    else:
                        external += 1
            internal //= 2
            total = internal + external
            scores[cid] = internal / total if total > 0 else 0.0
        return scores

    def _find_surprising_connections(
        self,
        nodes: List[Node],
        adjacency: Dict[str, Set[str]],
        community_map: Dict[str, int],
    ) -> List[Tuple[str, str, int, Set[int]]]:
        """Find non-obvious cross-community bridges.

        A connection is surprising when two nodes in different communities
        are connected indirectly through 3 or more hops, and the path
        crosses community boundaries.
        """
        surprising: List[Tuple[str, str, int, Set[int]]] = []
        threshold = self._config.SURPRISING_CONNECTION_HOP_THRESHOLD
        file_ids = [n.node_id for n in nodes]
        processed: Set[Tuple[str, str]] = set()

        for source in file_ids:
            src_community = community_map.get(source)
            if src_community is None:
                continue
            for target in file_ids:
                if source >= target:
                    continue
                tgt_community = community_map.get(target)
                if tgt_community is None or tgt_community == src_community:
                    continue
                pair = (source, target) if source < target else (target, source)
                if pair in processed:
                    continue
                processed.add(pair)
                path_communities, distance = self._shortest_path_communities(
                    source, target, adjacency, community_map
                )
                if distance is not None and distance >= threshold:
                    surprising.append((source, target, distance, path_communities))

        surprising.sort(key=lambda x: x[2], reverse=True)
        return surprising[: self._config.SURPRISING_CONNECTION_TOP_N]

    def _shortest_path_communities(
        self,
        source: str,
        target: str,
        adjacency: Dict[str, Set[str]],
        community_map: Dict[str, int],
    ) -> Tuple[Set[int], Optional[int]]:
        """Find the shortest path and communities traversed."""
        visited: Set[str] = {source}
        queue: deque = deque([(source, 0, set())])
        src_comm = community_map.get(source, -1)
        communities_seen: Set[int] = {src_comm} if src_comm >= 0 else set()

        while queue:
            current, distance, comms = queue.popleft()
            cur_comm = community_map.get(current, -1)
            if cur_comm >= 0:
                comms = comms | {cur_comm}
            if current == target:
                return comms, distance
            for neighbor in sorted(adjacency.get(current, set())):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1, comms))

        return communities_seen, None

    def _suggest_questions(
        self,
        nodes: List[Node],
        god_nodes: List[Tuple[str, float]],
        communities: Dict[int, List[str]],
        community_labels: Dict[int, str],
        surprising: List[Tuple[str, str, int, Set[int]]],
        adjacency: Dict[str, Set[str]],
    ) -> List[str]:
        """Generate plain-language exploration questions from graph structure."""
        questions: List[str] = []
        count = self._config.SUGGESTED_QUESTIONS_COUNT
        node_map = {n.node_id: n for n in nodes}

        for nid, score in god_nodes[:3]:
            node = node_map.get(nid)
            if node:
                imp_count = len(adjacency.get(nid, set()))
                questions.append(
                    f"What does {node.label} depend on, and what depends on it? "
                    f"({imp_count} connections)"
                )

        for cid, members in communities.items():
            if len(questions) >= count:
                break
            if len(members) >= 3:
                label = community_labels.get(cid, f"Community {cid}")
                questions.append(
                    f"How are the {len(members)} files in '{label}' related to each other?"
                )
                break

        for src, tgt, hops, comms in surprising[:1]:
            src_node = node_map.get(src)
            tgt_node = node_map.get(tgt)
            if src_node and tgt_node:
                questions.append(
                    f"Why are {src_node.label} and {tgt_node.label} "
                    f"connected through {hops} hops across {len(comms)} communities?"
                )

        for node in nodes[:5]:
            if len(questions) >= count:
                break
            symbols = [s for s in node.symbols if s.kind in ("class", "struct", "interface")]
            if symbols:
                questions.append(
                    f"What is {symbols[0].name} in {node.label} and how is it used?"
                )

        while len(questions) < count:
            questions.append(f"What is the overall architecture of this codebase?")
            break

        return questions[:count]
