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


@dataclass
class SecurityFinding:
    """A security-relevant pattern detected in a source file.

    Attributes:
        file_path: Relative path of the file containing the finding.
        line: One-based line number where the pattern was found.
        severity: Severity level (critical, high, medium, low, info).
        rule_id: Unique identifier for the detection rule (e.g. "PY001").
        description: Human-readable explanation of the issue.
        snippet: The offending source code line.
        cwe: CWE identifier string (e.g. "CWE-78").
    """

    file_path: str
    line: int
    severity: str
    rule_id: str
    description: str
    snippet: str
    cwe: str


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


@dataclass
class TaintPath:
    """A taint propagation path from source to sink through the import graph.

    Attributes:
        source_file: The file that introduces the dangerous import.
        sink_file: The file that transitively receives the taint.
        path: List of file node IDs forming the propagation chain.
        hops: Number of hops in the propagation path.
        dangerous_import: The specific dangerous module or function imported.
        severity: Inferred severity of the taint path.
    """

    source_file: str
    sink_file: str
    path: List[str]
    hops: int
    dangerous_import: str
    severity: str


@dataclass
class TaintAnalysisResult:
    """Complete taint propagation analysis output.

    Attributes:
        paths: List of TaintPath instances discovered.
        source_count: Number of unique taint source files.
        sink_count: Number of unique taint sink files.
    """

    paths: List[TaintPath]
    source_count: int
    sink_count: int


@dataclass
class DependencyCycle:
    """A cycle detected in the resolved import graph.

    Attributes:
        cycle: List of file node IDs forming the cycle.
        length: Number of files in the cycle.
    """

    cycle: List[str]
    length: int


@dataclass
class ChangeImpact:
    """Change impact analysis for a single file.

    Attributes:
        file_id: The file that would be changed.
        direct_dependents: Files that directly import this file.
        transitive_dependents: Files that transitively depend on this file.
        total_impact: Total number of affected files (direct + transitive).
    """

    file_id: str
    direct_dependents: List[str]
    transitive_dependents: List[str]
    total_impact: int


@dataclass
class HotspotResult:
    """A hotspot file combining complexity and centrality metrics.

    Attributes:
        file_id: The file node ID.
        complexity_score: Normalised symbol count score (0-1).
        centrality_score: Normalised god node score (0-1).
        combined_score: Weighted combination of complexity and centrality.
        symbol_count: Raw symbol count.
        connection_count: Raw connection count.
    """

    file_id: str
    complexity_score: float
    centrality_score: float
    combined_score: float
    symbol_count: int
    connection_count: int


@dataclass
class SuggestedRule:
    """A suggested linting/security rule derived from code patterns.

    Attributes:
        rule_id: Suggested rule identifier (e.g. "RM001").
        severity: Suggested severity (info, warning, error).
        description: Human-readable description of the pattern.
        pattern: The detected pattern or code snippet.
        file_examples: Example file paths where the pattern was found.
        match_count: Number of times the pattern was matched.
        language: Target language for the rule.
        semgrep_yaml: Optional Semgrep rule YAML string.
    """

    rule_id: str
    severity: str
    description: str
    pattern: str
    file_examples: List[str]
    match_count: int
    language: str
    semgrep_yaml: str


@dataclass
class LayerViolation:
    """A detected architectural layer violation.

    Attributes:
        source_file: The file causing the violation.
        source_layer: The layer of the source file.
        target_file: The file being imported.
        target_layer: The layer of the target file.
        description: Description of the violation.
        severity: Severity (strict, warn, info).
    """

    source_file: str
    source_layer: str
    target_file: str
    target_layer: str
    description: str
    severity: str


@dataclass
class AnalysisResultV2:
    """Extended analysis result combining all new analysis modules.

    Attributes:
        taint: Optional taint analysis result.
        cycles: List of dependency cycles.
        change_impacts: List of change impact results for key files.
        hotspots: List of hotspot results.
        suggested_rules: List of suggested linting rules.
        layer_violations: List of layer violations.
    """

    taint: TaintAnalysisResult | None = None
    cycles: List[DependencyCycle] = field(default_factory=list)
    change_impacts: List[ChangeImpact] = field(default_factory=list)
    hotspots: List[HotspotResult] = field(default_factory=list)
    suggested_rules: List[SuggestedRule] = field(default_factory=list)
    layer_violations: List[LayerViolation] = field(default_factory=list)
