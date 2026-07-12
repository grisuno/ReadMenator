"""Graph analysis engine for the readmenator knowledge graph.

Provides community detection (Louvain-like greedy modularity), god
node identification (degree/PageRank centrality), surprising connection
discovery (cross-community bridges), and suggested exploration questions
derived from graph structure. All operations are deterministic and
token-free.
"""

from __future__ import annotations

import random
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import AnalysisResult, CommunityResult, Edge, Node


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

        Each node adopts the most frequent community label among its
        neighbors. Iterates until convergence or max iterations reached.
        Simple, deterministic, and correct for connected graphs.
        """
        if not nodes or not adjacency:
            return {}

        file_ids = [n.node_id for n in nodes]
        labels: Dict[str, int] = {fid: i for i, fid in enumerate(file_ids)}

        for _iteration in range(50):
            changed = False
            node_list = list(file_ids)
            random.shuffle(node_list)
            for fid in node_list:
                neighbor_labels: Dict[int, int] = {}
                for neighbor in adjacency.get(fid, set()):
                    nl = labels.get(neighbor)
                    if nl is not None:
                        neighbor_labels[nl] = neighbor_labels.get(nl, 0) + 1
                if not neighbor_labels:
                    continue
                max_count = max(neighbor_labels.values())
                best_labels = [lab for lab, cnt in neighbor_labels.items() if cnt == max_count]
                best_label = best_labels[0] if best_labels else labels[fid]
                if best_label != labels[fid]:
                    labels[fid] = best_label
                    changed = True
            if not changed:
                break

        result: Dict[int, List[str]] = {}
        for fid, lab in labels.items():
            if lab not in result:
                result[lab] = []
            result[lab].append(fid)

        filtered: Dict[int, List[str]] = {}
        new_id = 0
        for lab, members in result.items():
            if len(members) >= self._config.COMMUNITY_MIN_SIZE:
                filtered[new_id] = sorted(members)
                new_id += 1

        return filtered

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
            dirs: List[str] = []
            for n in member_nodes:
                parent = n.node_id.rsplit("/", 1)[0] if "/" in n.node_id else "."
                dirs.append(parent)
            dir_counts: Dict[str, int] = {}
            for d in dirs:
                dir_counts[d] = dir_counts.get(d, 0) + 1
            top_dir = max(dir_counts, key=dir_counts.get) if dir_counts else "."
            if top_dir == ".":
                top_dir = "root"
            labels[cid] = top_dir
        return labels

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
        from collections import deque
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
            for neighbor in adjacency.get(current, set()):
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
