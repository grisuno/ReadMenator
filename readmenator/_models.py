"""Data model types for the readmenator knowledge graph.

Defines the core entity types -- Symbol, Node, Edge -- plus a
utility function for pluralising symbol kind labels and a helper
for constructing community analysis results. Every parser, scanner,
renderer, and query engine depends on these definitions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Symbol:
    """A single code symbol extracted from a source file.

    Attributes:
        name: Identifier of the symbol (class name, function name, etc.).
        kind: Semantic type (class, function, struct, enum, ...).
        line: One-based line number where the symbol is defined.
        doc: Optional docstring or comment extracted from the source.
        signature: Optional method or function signature snippet.
    """

    name: str
    kind: str
    line: int
    doc: str = ""
    signature: str = ""


@dataclass
class Node:
    """A file node in the knowledge graph, containing its symbols.

    Attributes:
        node_id: Relative path of the file used as a unique identifier.
        label: Base file name for display purposes.
        kind: Type of node (typically "module").
        language: Programming language derived from the file extension.
        doc: Optional file-level documentation string.
        symbols: List of Symbol instances defined in this file.
    """

    node_id: str
    label: str
    kind: str
    language: str
    doc: str = ""
    symbols: List[Symbol] = field(default_factory=list)


@dataclass
class Edge:
    """A directed relationship between two nodes in the knowledge graph.

    Attributes:
        source: Node ID of the source (dependent) file.
        target: Node ID of the target (dependency) file or module.
        relation: Semantic relation label (e.g. "imports", "resolved_imports").
        confidence: Confidence tier ("EXTRACTED" for structural, "INFERRED" for heuristic).
    """

    source: str
    target: str
    relation: str
    confidence: str = "EXTRACTED"


def pluralize_symbol_kind(kind: str, plural_map: Dict[str, str]) -> str:
    """Return the plural form of *kind* according to *plural_map*.

    Falls back to appending ``"s"`` when the kind is not found.
    This prevents obvious misspellings like ``"Classs"``.
    """
    return plural_map.get(kind, kind + "s")


@dataclass
class CommunityResult:
    """Result of community detection on the import graph.

    Attributes:
        community_id: Integer identifier of the community.
        label: Human-readable name for the community.
        file_ids: Set of node IDs belonging to this community.
        cohesion: Cohesion score (internal edges / total edges involving community).
        size: Number of files in the community.
    """

    community_id: int
    label: str
    file_ids: set
    cohesion: float
    size: int


@dataclass
class AnalysisResult:
    """Complete graph analysis output.

    Attributes:
        god_nodes: List of (node_id, score) for most central nodes.
        communities: List of CommunityResult instances.
        surprising_connections: List of (source_node, target_node, hops, bridging_communities).
        suggested_questions: List of plain-language exploration questions.
        node_count: Total nodes in the graph.
        edge_count: Total edges in the graph.
    """

    god_nodes: List[tuple]
    communities: List[CommunityResult]
    surprising_connections: List[tuple]
    suggested_questions: List[str]
    node_count: int
    edge_count: int
