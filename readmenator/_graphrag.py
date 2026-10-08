"""Zero-token GraphRAG index and retrieval for AI agents.

Builds a Microsoft-GraphRAG style index from the static scan without
calling any language model: typed entities (files, symbols, concepts,
external modules), typed relationships, source text units, and a
hierarchy of community reports (Louvain communities, Louvain themes
over the community quotient graph, and a project root). Reports are
extractive: every sentence is computed from measured structure
(PageRank, fan-in, findings, cycles, hotspots, layer violations).

Retrieval follows two complementary strategies:

- local search (HippoRAG style): BM25 over entities and text units
  seeds a Personalized PageRank walk on the entity graph; the top
  entities, the relationships between them, their community reports,
  and their source text units are packed into a token-budgeted
  Markdown context.
- global search (GraphRAG map-reduce): community reports are scored
  against the query, the matching findings of each report are mapped
  out, and the results are reduced into one ranked answer context.
"""

from __future__ import annotations

import json
import logging
import math
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from readmenator._analyzer import GraphAnalyzer, dominant_directory
from readmenator._category import Category, EdgeKind, Morphism, TypedGraph
from readmenator._config import Config
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    ConceptGraph,
    Edge,
    Node,
    SecurityFinding,
)
from readmenator._purpose import file_purpose, first_sentence, truncate_words
from readmenator._rank import file_pagerank, global_pagerank, personalized_pagerank
from readmenator._resolver import ImportResolver

logger = logging.getLogger(__name__)

SCHEMA_VERSION = 1

_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*")
_CAMEL_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")

_FILE_PREFIX = "file:"
_SYMBOL_PREFIX = "sym:"
_CONCEPT_PREFIX = "concept:"
_EXTERNAL_PREFIX = "ext:"
_MEMORY_ENTITY = "memory:log"

_CLASS_KINDS = frozenset(
    {"class", "struct", "interface", "trait", "enum", "record", "protocol", "type"}
)


@dataclass(frozen=True)
class RagEntity:
    """A typed node of the GraphRAG entity graph.

    Attributes:
        entity_id: Stable identifier (``file:``, ``sym:``, ``concept:``, ``ext:``).
        name: Human-readable name.
        kind: file, symbol kind (class, function, ...), concept, or external.
        file: Owning file path ("" for concepts and externals).
        line: Definition line (0 when not applicable).
        description: Extractive description (purpose, signature, doc).
        community: Level-0 community index, -1 when unassigned.
        degree: Number of relationships touching the entity.
        rank: Global PageRank of the entity on the entity graph.
    """

    entity_id: str
    name: str
    kind: str
    file: str
    line: int
    description: str
    community: int
    degree: int
    rank: float


@dataclass(frozen=True)
class RagRelation:
    """A typed, weighted edge between two entities.

    Attributes:
        source: Source entity id.
        target: Target entity id.
        relation: defines, resolved_imports, calls, inherits, documents, imports.
        weight: Semantic edge weight from the category model.
        confidence: EXTRACTED or INFERRED.
        description: One-line extractive description.
    """

    source: str
    target: str
    relation: str
    weight: float
    confidence: str
    description: str


@dataclass(frozen=True)
class RagTextUnit:
    """A source chunk anchored to one entity.

    Attributes:
        unit_id: Stable identifier.
        file: Source file path.
        entity_id: Entity the chunk belongs to.
        start_line: First line of the chunk (1-based).
        end_line: Last line of the chunk (1-based, inclusive).
        text: Chunk text (source excerpt or signature plus doc in privacy mode).
    """

    unit_id: str
    file: str
    entity_id: str
    start_line: int
    end_line: int
    text: str


@dataclass
class RagCommunity:
    """One node of the community report hierarchy.

    Attributes:
        community_id: ``c<n>`` for communities, ``t<n>`` for themes, ``root``.
        level: 0 community, 1 theme, 2 project root.
        parent: Parent report id ("" for root).
        children: Child report ids.
        title: Report title.
        file_ids: Files covered by the report.
        summary: Extractive summary paragraph.
        findings: Ranked extractive findings.
        key_entities: Most central entity ids inside the report.
        key_relations: Most informative relationship lines.
        rating: Impact rating in [0, 10].
        rating_explanation: How the rating was computed.
    """

    community_id: str
    level: int
    parent: str
    children: List[str]
    title: str
    file_ids: List[str]
    summary: str
    findings: List[str]
    key_entities: List[str]
    key_relations: List[str]
    rating: float
    rating_explanation: str


@dataclass
class GraphRagIndex:
    """Complete GraphRAG index persisted beside the knowledge base.

    Attributes:
        entities: Entity table.
        relationships: Relationship table.
        communities: Community report hierarchy (communities, themes, root).
        text_units: Source chunk table.
        meta: Counts and schema metadata.
    """

    entities: List[RagEntity] = field(default_factory=list)
    relationships: List[RagRelation] = field(default_factory=list)
    communities: List[RagCommunity] = field(default_factory=list)
    text_units: List[RagTextUnit] = field(default_factory=list)
    meta: Dict[str, object] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, object]:
        """Serialise the index into JSON-compatible primitives."""
        return {
            "meta": dict(self.meta),
            "entities": [asdict(e) for e in self.entities],
            "relationships": [asdict(r) for r in self.relationships],
            "communities": [asdict(c) for c in self.communities],
            "text_units": [asdict(t) for t in self.text_units],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, object]) -> "GraphRagIndex":
        """Rebuild an index from :meth:`to_dict` output.

        Args:
            data: Dictionary produced by to_dict (or loaded from index.json).

        Returns:
            Reconstructed GraphRagIndex.
        """
        return cls(
            entities=[RagEntity(**e) for e in data.get("entities", [])],  # type: ignore[arg-type]
            relationships=[RagRelation(**r) for r in data.get("relationships", [])],  # type: ignore[arg-type]
            communities=[RagCommunity(**c) for c in data.get("communities", [])],  # type: ignore[arg-type]
            text_units=[RagTextUnit(**t) for t in data.get("text_units", [])],  # type: ignore[arg-type]
            meta=dict(data.get("meta", {})),  # type: ignore[arg-type]
        )


@dataclass
class RagContext:
    """Result of a GraphRAG search ready for an agent prompt.

    Attributes:
        query: Original query text.
        mode: local or global.
        entities: Ranked (entity id, score) pairs.
        relations: Selected relationship lines.
        reports: Selected report ids.
        text_units: Selected text unit ids.
        markdown: Token-budgeted Markdown context.
        approx_tokens: Approximate token count of the Markdown.
    """

    query: str
    mode: str
    entities: List[Tuple[str, float]]
    relations: List[str]
    reports: List[str]
    text_units: List[str]
    markdown: str
    approx_tokens: int


def tokenize(text: str, min_len: int, stopwords: Set[str]) -> List[str]:
    """Split text into lowercase retrieval tokens.

    Identifiers are split on camelCase, digits-to-letters boundaries and
    separators; the joined lowercase identifier is kept too so exact
    symbol names still match.

    Args:
        text: Raw text (names, paths, docs, code).
        min_len: Minimum token length.
        stopwords: Lowercase tokens to drop.

    Returns:
        Ordered token list (duplicates preserved for term frequency).
    """
    out: List[str] = []
    for raw in _TOKEN_RE.findall(text or ""):
        parts = [p.lower() for p in _CAMEL_RE.split(raw) if p]
        whole = raw.lower()
        if len(parts) > 1 and len(whole) >= min_len and whole not in stopwords:
            out.append(whole)
        for part in parts:
            if len(part) >= min_len and part not in stopwords and not part.isdigit():
                out.append(part)
    return out


class Bm25Index:
    """Okapi BM25 ranking over a fixed corpus of token lists."""

    def __init__(self, documents: Sequence[Sequence[str]], k1: float, b: float) -> None:
        """Index token documents.

        Args:
            documents: Token list per document.
            k1: Term-frequency saturation.
            b: Length normalisation strength.
        """
        self._k1 = k1
        self._b = b
        self._tf: List[Dict[str, int]] = []
        self._len: List[int] = []
        df: Dict[str, int] = {}
        for doc in documents:
            counts: Dict[str, int] = {}
            for token in doc:
                counts[token] = counts.get(token, 0) + 1
            self._tf.append(counts)
            self._len.append(len(doc))
            for token in counts:
                df[token] = df.get(token, 0) + 1
        total = len(self._tf)
        self._avg = (sum(self._len) / total) if total else 0.0
        self._idf = {
            token: math.log(1.0 + (total - freq + 0.5) / (freq + 0.5))
            for token, freq in df.items()
        }

    def scores(self, query: Sequence[str]) -> List[float]:
        """Return the BM25 score of every document for the query tokens.

        Args:
            query: Query tokens.

        Returns:
            One score per indexed document, in corpus order.
        """
        unique = sorted(set(query))
        out: List[float] = []
        avg = self._avg or 1.0
        for counts, length in zip(self._tf, self._len):
            score = 0.0
            norm = self._k1 * (1.0 - self._b + self._b * length / avg)
            for token in unique:
                tf = counts.get(token)
                if not tf:
                    continue
                score += self._idf.get(token, 0.0) * tf * (self._k1 + 1.0) / (tf + norm)
            out.append(score)
        return out


def _file_entity(file_id: str) -> str:
    """Return the entity id of a file."""
    return _FILE_PREFIX + file_id


def _edge_kind(relation: str) -> EdgeKind:
    """Map a relation name to its EdgeKind, defaulting to DEPENDS_ON."""
    try:
        return EdgeKind(relation)
    except ValueError:
        return EdgeKind.DEPENDS_ON


def _relation_weight(relation: str) -> float:
    """Return the category weight of a relation name."""
    return Morphism("", "", _edge_kind(relation)).weight


def _short(file_id: str) -> str:
    """Return the basename of a file path."""
    return file_id.rpartition("/")[2] or file_id


class GraphRagBuilder:
    """Builds the zero-token GraphRAG index from scan and analysis results."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: GRAPHRAG_* budgets, weights, and privacy settings.
        """
        self._config = config
        self._stopwords = set(config.GRAPHRAG_STOPWORDS)
        self._severity = dict(config.GRAPHRAG_SEVERITY_WEIGHTS)

    def build(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[List[SecurityFinding]] = None,
        analysis_v2: Optional[AnalysisResultV2] = None,
        concept_graph: Optional[ConceptGraph] = None,
        content_map: Optional[Dict[str, str]] = None,
        memory_notes: Optional[List[Tuple[str, str, str]]] = None,
    ) -> GraphRagIndex:
        """Build entities, relationships, text units, and community reports.

        Args:
            nodes: Scanned file nodes.
            edges: Raw edges (imports, calls, inherits).
            resolved_edges: Project-internal resolved import edges.
            analysis: Community and god-node analysis.
            layers: File to architectural layer mapping.
            findings: Security findings.
            analysis_v2: Hotspots, cycles, taint, violations, dataflow.
            concept_graph: Semantic noun graph (falls back to analysis_v2).
            content_map: File contents for source text units.
            memory_notes: Session-log notes as (date, kind, text) from MEMORY.md.

        Returns:
            Deterministic GraphRagIndex.
        """
        cfg = self._config
        if not cfg.GRAPHRAG_ENABLED:
            return GraphRagIndex(meta={"schema_version": SCHEMA_VERSION, "enabled": False})
        nodes = sorted(nodes, key=lambda n: n.node_id)
        node_by_id = {n.node_id: n for n in nodes}
        layers = layers or {}
        content_map = {} if cfg.PRIVACY_MODE else (content_map or {})
        if concept_graph is None and analysis_v2 is not None:
            concept_graph = analysis_v2.concept_graph
        community_of: Dict[str, int] = {}
        for community in (analysis.communities if analysis else []):
            for fid in community.file_ids:
                community_of[fid] = community.community_id
        entities: Dict[str, Dict[str, object]] = {}
        relations: Dict[Tuple[str, str, str], RagRelation] = {}
        symbol_index: Dict[Tuple[str, str], str] = {}
        symbol_by_name: Dict[str, List[str]] = {}

        def add_relation(source: str, target: str, relation: str, description: str,
                         confidence: str = "EXTRACTED") -> None:
            """Insert a relationship once, keyed by endpoints and relation."""
            if source == target or source not in entities or target not in entities:
                return
            key = (source, target, relation)
            if key not in relations:
                relations[key] = RagRelation(
                    source, target, relation, round(_relation_weight(relation), 3),
                    confidence, description,
                )

        for node in nodes:
            eid = _file_entity(node.node_id)
            purpose = "" if cfg.PRIVACY_MODE else file_purpose(node, cfg.GRAPHRAG_DESCRIPTION_MAX_CHARS)
            layer = layers.get(node.node_id, "unknown")
            description = (
                f"{node.language} file in layer {layer} with {len(node.symbols)} symbols."
                + (f" {purpose}" if purpose else "")
            )
            entities[eid] = {
                "name": node.label, "kind": "file", "file": node.node_id, "line": 0,
                "description": description,
                "community": community_of.get(node.node_id, -1),
            }
            if not cfg.GRAPHRAG_INCLUDE_SYMBOLS:
                continue
            for symbol in node.symbols:
                sid = f"{_SYMBOL_PREFIX}{node.node_id}::{symbol.name}@{symbol.line}"
                doc = "" if cfg.PRIVACY_MODE else first_sentence(symbol.doc or "")
                signature = (symbol.signature or "").strip()
                text = " ".join(part for part in (signature, doc) if part)
                entities[sid] = {
                    "name": symbol.name, "kind": symbol.kind, "file": node.node_id,
                    "line": symbol.line,
                    "description": truncate_words(
                        f"{symbol.kind} {symbol.name} in {node.node_id}:{symbol.line}."
                        + (f" {text}" if text else ""),
                        cfg.GRAPHRAG_DESCRIPTION_MAX_CHARS,
                    ),
                    "community": community_of.get(node.node_id, -1),
                }
                symbol_index.setdefault((node.node_id, symbol.name), sid)
                symbol_by_name.setdefault(symbol.name, []).append(sid)
                add_relation(eid, sid, "defines", f"{node.label} defines {symbol.kind} {symbol.name}")

        def resolve_symbol(file_id: str, name: str) -> Optional[str]:
            """Resolve a symbol name inside a file, else a globally unique name."""
            local = symbol_index.get((file_id, name))
            if local:
                return local
            short = name.rpartition(".")[2]
            local = symbol_index.get((file_id, short))
            if local:
                return local
            candidates = symbol_by_name.get(short, [])
            return candidates[0] if len(candidates) == 1 else None

        resolver = ImportResolver(sorted(node_by_id))
        for edge in resolved_edges or []:
            if edge.source in node_by_id and edge.target in node_by_id:
                add_relation(
                    _file_entity(edge.source), _file_entity(edge.target), "resolved_imports",
                    f"{_short(edge.source)} imports {_short(edge.target)}",
                    edge.confidence or "EXTRACTED",
                )
        for edge in edges:
            source_file, _, source_name = edge.source.partition("::")
            if source_file not in node_by_id:
                continue
            if edge.relation == "calls":
                caller = resolve_symbol(source_file, source_name) if source_name else None
                target_file, _, target_name = edge.target.partition("::")
                if target_name and target_file in node_by_id:
                    callee = resolve_symbol(target_file, target_name)
                else:
                    callee = resolve_symbol(source_file, edge.target)
                origin = caller or _file_entity(source_file)
                if callee:
                    add_relation(origin, callee, "calls",
                                 f"{source_name or _short(source_file)} calls "
                                 f"{entities[callee]['name']}", "INFERRED")
            elif edge.relation == "inherits":
                child = resolve_symbol(source_file, source_name) if source_name else None
                parent = resolve_symbol(source_file, edge.target)
                if child and parent:
                    add_relation(child, parent, "inherits",
                                 f"{source_name} extends {edge.target}")
            elif edge.relation == "imports" and cfg.GRAPHRAG_INCLUDE_EXTERNALS:
                if edge.target in node_by_id or resolver.resolve(edge.target, source_file) is not None:
                    continue
                xid = _EXTERNAL_PREFIX + edge.target
                if xid not in entities:
                    entities[xid] = {
                        "name": edge.target, "kind": "external", "file": "", "line": 0,
                        "description": f"External module {edge.target}.", "community": -1,
                    }
                add_relation(_file_entity(source_file), xid, "imports",
                             f"{_short(source_file)} imports external {edge.target}")
        if concept_graph is not None and cfg.GRAPHRAG_INCLUDE_CONCEPTS:
            for concept in concept_graph.concepts:
                cid = _CONCEPT_PREFIX + concept.name
                files = sorted(f for f in concept.file_ids if f in node_by_id)
                entities[cid] = {
                    "name": concept.name, "kind": "concept", "file": "", "line": 0,
                    "description": (
                        f"Concept '{concept.name}' mentioned {concept.mention_count} times "
                        f"across {len(files)} files."
                    ),
                    "community": -1,
                }
                for fid in files:
                    add_relation(cid, _file_entity(fid), "documents",
                                 f"concept {concept.name} appears in {_short(fid)}", "INFERRED")
            for rel in concept_graph.relations:
                add_relation(_CONCEPT_PREFIX + rel.source, _CONCEPT_PREFIX + rel.target,
                             "depends_on", f"{rel.source} {rel.verb} {rel.target}", "INFERRED")

        notes = list(memory_notes or [])
        if notes:
            entities[_MEMORY_ENTITY] = {
                "name": "project memory", "kind": "memory",
                "file": f"{cfg.AGENT_OUTPUT_DIR}/{cfg.MEMORY_FILENAME}", "line": 0,
                "description": f"Session log with {len(notes)} recorded business rules, decisions, and notes.",
                "community": -1,
            }
        relationship_list = sorted(relations.values(), key=lambda r: (r.source, r.target, r.relation))
        entity_rank = self._entity_rank(sorted(entities), relationship_list)
        degree: Dict[str, int] = {}
        for rel in relationship_list:
            degree[rel.source] = degree.get(rel.source, 0) + 1
            degree[rel.target] = degree.get(rel.target, 0) + 1
        entity_list = [
            RagEntity(
                entity_id=eid,
                name=str(attrs["name"]),
                kind=str(attrs["kind"]),
                file=str(attrs["file"]),
                line=int(attrs["line"]),  # type: ignore[arg-type]
                description=str(attrs["description"]),
                community=int(attrs["community"]),  # type: ignore[arg-type]
                degree=degree.get(eid, 0),
                rank=round(entity_rank.get(eid, 0.0), 6),
            )
            for eid, attrs in sorted(entities.items())
        ]
        text_units = self._text_units(nodes, content_map)
        memory_file = f"{cfg.AGENT_OUTPUT_DIR}/{cfg.MEMORY_FILENAME}"
        for index, (date, kind, text) in enumerate(notes, start=1):
            text_units.append(RagTextUnit(
                f"memory#{index}", memory_file, _MEMORY_ENTITY, 0, 0, f"[{kind}] {date}: {text}",
            ))
        file_rank = self._file_rank(nodes, resolved_edges or [])
        communities = self._reports(
            nodes, resolved_edges or [], analysis, layers, findings or [],
            analysis_v2, file_rank, entity_list,
        )
        meta: Dict[str, object] = {
            "schema_version": SCHEMA_VERSION,
            "enabled": True,
            "files": len(nodes),
            "entities": len(entity_list),
            "relationships": len(relationship_list),
            "communities": sum(1 for c in communities if c.level == 0),
            "themes": sum(1 for c in communities if c.level == 1),
            "text_units": len(text_units),
            "privacy_mode": cfg.PRIVACY_MODE,
            "entity_kinds": self._kind_counts(entity_list),
        }
        return GraphRagIndex(entity_list, relationship_list, communities, text_units, meta)

    @staticmethod
    def _kind_counts(entities: Iterable[RagEntity]) -> Dict[str, int]:
        """Count entities per kind, sorted by kind name."""
        counts: Dict[str, int] = {}
        for entity in entities:
            counts[entity.kind] = counts.get(entity.kind, 0) + 1
        return dict(sorted(counts.items()))

    def _undirected_graph(self, ids: Iterable[str], relations: Iterable[RagRelation]) -> TypedGraph:
        """Build a symmetric typed graph over entity ids for random walks."""
        category = Category()
        for eid in ids:
            category.add_object(eid)
        for rel in relations:
            kind = _edge_kind(rel.relation)
            confidence = 1.0 if rel.confidence == "EXTRACTED" else 0.8
            category.add_morphism(Morphism(rel.source, rel.target, kind, confidence))
            category.add_morphism(Morphism(rel.target, rel.source, kind, confidence))
        return TypedGraph(category)

    def _entity_rank(self, ids: List[str], relations: List[RagRelation]) -> Dict[str, float]:
        """Global PageRank of every entity on the symmetric entity graph."""
        if not ids:
            return {}
        graph = self._undirected_graph(ids, relations)
        return global_pagerank(
            graph, alpha=self._config.RANKING_ALPHA,
            max_iter=self._config.GRAPHRAG_PPR_MAX_ITER,
            tolerance=self._config.GRAPHRAG_PPR_TOLERANCE,
        )

    def _file_rank(self, nodes: List[Node], resolved_edges: List[Edge]) -> Dict[str, float]:
        """Directed PageRank of files on resolved imports (authority = imported)."""
        return file_pagerank(
            [n.node_id for n in nodes], [(e.source, e.target) for e in resolved_edges],
            self._config.RANKING_ALPHA, self._config.RANKING_MAX_ITER, self._config.RANKING_TOLERANCE,
        )

    def _text_units(self, nodes: List[Node], content_map: Dict[str, str]) -> List[RagTextUnit]:
        """Chunk each symbol's source span (or signature plus doc) into text units."""
        cfg = self._config
        units: List[RagTextUnit] = []
        for node in nodes:
            lines = content_map.get(node.node_id, "").splitlines()
            purpose = "" if cfg.PRIVACY_MODE else (node.doc or "").strip()
            if purpose:
                units.append(RagTextUnit(
                    f"{node.node_id}#doc", node.node_id, _file_entity(node.node_id), 1, 1,
                    purpose[: cfg.GRAPHRAG_TEXT_UNIT_MAX_CHARS],
                ))
            if not cfg.GRAPHRAG_INCLUDE_SYMBOLS:
                continue
            ordered = sorted(node.symbols, key=lambda s: (s.line, s.name))
            for index, symbol in enumerate(ordered):
                sid = f"{_SYMBOL_PREFIX}{node.node_id}::{symbol.name}@{symbol.line}"
                start = max(1, symbol.line)
                next_line = ordered[index + 1].line if index + 1 < len(ordered) else len(lines) + 1
                end = max(start, min(next_line - 1, start + cfg.GRAPHRAG_TEXT_UNIT_MAX_LINES - 1))
                if lines:
                    text = "\n".join(lines[start - 1:end]).rstrip()
                else:
                    doc = "" if cfg.PRIVACY_MODE else (symbol.doc or "")
                    text = "\n".join(p for p in ((symbol.signature or symbol.name), doc) if p)
                    end = start
                if not text.strip():
                    continue
                units.append(RagTextUnit(
                    f"{node.node_id}:{start}", node.node_id, sid, start, end,
                    text[: cfg.GRAPHRAG_TEXT_UNIT_MAX_CHARS],
                ))
        return units

    def _risk_score(self, files: Set[str], findings: List[SecurityFinding]) -> Tuple[float, Dict[str, int]]:
        """Severity-weighted finding score plus per-severity counts for a file set."""
        counts: Dict[str, int] = {}
        score = 0.0
        for finding in findings:
            if finding.file_path in files:
                counts[finding.severity] = counts.get(finding.severity, 0) + 1
                score += self._severity.get(finding.severity, 0.0)
        return score, counts

    def _reports(
        self,
        nodes: List[Node],
        resolved_edges: List[Edge],
        analysis: Optional[AnalysisResult],
        layers: Dict[str, str],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        file_rank: Dict[str, float],
        entities: List[RagEntity],
    ) -> List[RagCommunity]:
        """Build level-0 community reports, level-1 themes, and the root report."""
        node_by_id = {n.node_id: n for n in nodes}
        groups: List[Tuple[str, Set[str]]] = []
        assigned: Set[str] = set()
        for community in sorted(analysis.communities if analysis else [], key=lambda c: c.community_id):
            members = {f for f in community.file_ids if f in node_by_id}
            if members:
                groups.append((community.label, members))
                assigned |= members
        leftover = {n.node_id for n in nodes} - assigned
        if leftover:
            groups.append(("unassigned files", leftover))
        group_of: Dict[str, int] = {}
        for index, (_label, members) in enumerate(groups):
            for fid in members:
                group_of[fid] = index
        links: Dict[Tuple[int, int], int] = {}
        for edge in resolved_edges:
            a, b = group_of.get(edge.source), group_of.get(edge.target)
            if a is not None and b is not None and a != b:
                links[(a, b)] = links.get((a, b), 0) + 1
        mass = [sum(file_rank.get(f, 0.0) for f in members) for _label, members in groups]
        top_mass = max(mass) if mass else 0.0
        reports: List[RagCommunity] = []
        for index, (label, members) in enumerate(groups):
            reports.append(self._community_report(
                index, label, members, node_by_id, resolved_edges, layers, findings,
                analysis_v2, file_rank, links, groups, mass[index], top_mass, entities,
                analysis,
            ))
        themes = self._themes(reports, links)
        root = self._root_report(reports, themes, nodes, analysis)
        return reports + themes + [root]

    def _community_report(
        self,
        index: int,
        label: str,
        members: Set[str],
        node_by_id: Dict[str, Node],
        resolved_edges: List[Edge],
        layers: Dict[str, str],
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2],
        file_rank: Dict[str, float],
        links: Dict[Tuple[int, int], int],
        groups: List[Tuple[str, Set[str]]],
        mass: float,
        top_mass: float,
        entities: List[RagEntity],
        analysis: Optional[AnalysisResult],
    ) -> RagCommunity:
        """Compose one extractive level-0 community report."""
        cfg = self._config
        ranked_files = sorted(members, key=lambda f: (-file_rank.get(f, 0.0), f))
        core = ranked_files[0]
        core_node = node_by_id[core]
        languages: Dict[str, int] = {}
        for fid in members:
            lang = node_by_id[fid].language or "unknown"
            languages[lang] = languages.get(lang, 0) + 1
        lang_text = ", ".join(f"{k} {v}" for k, v in sorted(languages.items(), key=lambda kv: (-kv[1], kv[0])))
        layer_counts: Dict[str, int] = {}
        for fid in members:
            layer = layers.get(fid, "unknown")
            layer_counts[layer] = layer_counts.get(layer, 0) + 1
        main_layer = sorted(layer_counts.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
        fan_in: Dict[str, int] = {}
        internal = 0
        for edge in resolved_edges:
            if edge.target in members:
                fan_in[edge.target] = fan_in.get(edge.target, 0) + 1
            if edge.source in members and edge.target in members:
                internal += 1
        depends = sorted(((b, n) for (a, b), n in links.items() if a == index), key=lambda kv: (-kv[1], kv[0]))
        used_by = sorted(((a, n) for (a, b), n in links.items() if b == index), key=lambda kv: (-kv[1], kv[0]))
        key_symbols: List[str] = []
        for fid in ranked_files:
            for symbol in sorted(node_by_id[fid].symbols, key=lambda s: (s.kind not in _CLASS_KINDS, s.line)):
                if symbol.name.startswith("_"):
                    continue
                key_symbols.append(symbol.name)
                if len(key_symbols) >= cfg.GRAPHRAG_REPORT_KEY_ENTITIES:
                    break
            if len(key_symbols) >= cfg.GRAPHRAG_REPORT_KEY_ENTITIES:
                break
        purpose = "" if cfg.PRIVACY_MODE else file_purpose(core_node, cfg.GRAPHRAG_DESCRIPTION_MAX_CHARS)
        directory = dominant_directory(members)
        summary_parts = [
            f"{len(members)} files under {directory} ({lang_text}), mostly {main_layer}.",
            f"Core file {core} (PageRank {file_rank.get(core, 0.0):.4f}, imported by {fan_in.get(core, 0)} files)"
            + (f": {purpose}" if purpose else "."),
        ]
        if key_symbols:
            summary_parts.append("Key abstractions: " + ", ".join(key_symbols[:6]) + ".")
        if depends:
            summary_parts.append("Depends on " + ", ".join(
                f"{groups[b][0]} ({n})" for b, n in depends[:3]) + ".")
        if used_by:
            summary_parts.append("Used by " + ", ".join(
                f"{groups[a][0]} ({n})" for a, n in used_by[:3]) + ".")
        findings_out: List[str] = []
        for fid in ranked_files[:3]:
            node = node_by_id[fid]
            text = "" if cfg.PRIVACY_MODE else file_purpose(node, cfg.GRAPHRAG_DESCRIPTION_MAX_CHARS)
            findings_out.append(
                f"`{fid}` ranks {ranked_files.index(fid) + 1} by PageRank, "
                f"{fan_in.get(fid, 0)} importers, {len(node.symbols)} symbols"
                + (f": {text}" if text else ".")
            )
        risk, severity_counts = self._risk_score(members, findings)
        if severity_counts:
            ordered = [s for s, _w in cfg.GRAPHRAG_SEVERITY_WEIGHTS if s in severity_counts]
            rules: Dict[str, int] = {}
            for finding in findings:
                if finding.file_path in members:
                    rules[finding.rule_id] = rules.get(finding.rule_id, 0) + 1
            top_rules = ", ".join(r for r, _n in sorted(rules.items(), key=lambda kv: (-kv[1], kv[0]))[:3])
            findings_out.append(
                "Security: " + ", ".join(f"{severity_counts[s]} {s}" for s in ordered)
                + f" findings (top rules: {top_rules})."
            )
        if analysis_v2 is not None:
            hot = [h for h in analysis_v2.hotspots if h.file_id in members][:2]
            for h in hot:
                findings_out.append(
                    f"Hotspot `{h.file_id}`: {h.symbol_count} symbols, "
                    f"{h.connection_count} connections (score {h.combined_score:.2f})."
                )
            for cycle in analysis_v2.cycles:
                if any(f in members for f in cycle.cycle):
                    loop = list(cycle.cycle)
                    if loop and loop[0] != loop[-1]:
                        loop.append(loop[0])
                    findings_out.append("Dependency cycle: " + " -> ".join(_short(f) for f in loop) + ".")
                    break
            violations = [v for v in analysis_v2.layer_violations if v.source_file in members]
            if violations:
                v = violations[0]
                findings_out.append(
                    f"{len(violations)} layer violations, e.g. {_short(v.source_file)} "
                    f"({v.source_layer}) -> {_short(v.target_file)} ({v.target_layer})."
                )
            if analysis_v2.taint is not None:
                sinks = [p for p in analysis_v2.taint.paths if p.sink_file in members]
                if sinks:
                    imports = sorted({p.dangerous_import for p in sinks})
                    findings_out.append(
                        f"Taint: {len(sinks)} paths reach this group via " + ", ".join(imports[:4]) + "."
                    )
            flows = [d for d in analysis_v2.dataflow_issues if d.file_path in members]
            if flows:
                findings_out.append(f"Dataflow: {len(flows)} INFERRED issues (first: {flows[0].kind} in {flows[0].function}).")
        if analysis is not None:
            for source, target, distance, _path in analysis.surprising_connections:
                if source in members or target in members:
                    findings_out.append(
                        f"Surprising bridge: {_short(source)} <-> {_short(target)} ({distance} hops across communities)."
                    )
                    break
        member_entities = sorted(
            (e for e in entities if e.file in members and e.kind != "external"),
            key=lambda e: (-e.rank, e.entity_id),
        )
        key_entities = [e.entity_id for e in member_entities[: cfg.GRAPHRAG_REPORT_KEY_ENTITIES]]
        key_relations: List[str] = []
        for edge in sorted(resolved_edges, key=lambda e: (-file_rank.get(e.target, 0.0), e.source, e.target)):
            if edge.source in members and edge.target in members and edge.source != edge.target:
                key_relations.append(f"{edge.source} -> {edge.target}")
                if len(key_relations) >= cfg.GRAPHRAG_REPORT_KEY_RELATIONS:
                    break
        rating, explanation = self._rating(mass, top_mass, risk)
        return RagCommunity(
            community_id=f"c{index}", level=0, parent="", children=[],
            title=label, file_ids=sorted(members), summary=" ".join(summary_parts),
            findings=findings_out[: cfg.GRAPHRAG_REPORT_MAX_FINDINGS],
            key_entities=key_entities, key_relations=key_relations,
            rating=rating,
            rating_explanation=explanation + f" Internal imports: {internal}.",
        )

    def _rating(self, mass: float, top_mass: float, risk: float) -> Tuple[float, str]:
        """Impact rating from centrality share and severity-weighted risk."""
        cfg = self._config
        centrality = (mass / top_mass) if top_mass > 0 else 0.0
        risk_part = min(cfg.GRAPHRAG_RATING_RISK_CAP, risk) / (cfg.GRAPHRAG_RATING_RISK_CAP or 1.0)
        rating = round(
            cfg.GRAPHRAG_RATING_CENTRALITY_WEIGHT * centrality + cfg.GRAPHRAG_RATING_RISK_WEIGHT * risk_part, 1
        )
        return rating, (
            f"Rating {rating}/10 = {cfg.GRAPHRAG_RATING_CENTRALITY_WEIGHT:g} x PageRank share "
            f"{centrality:.2f} + {cfg.GRAPHRAG_RATING_RISK_WEIGHT:g} x risk {risk_part:.2f}."
        )

    def _themes(self, reports: List[RagCommunity], links: Dict[Tuple[int, int], int]) -> List[RagCommunity]:
        """Group community reports into level-1 themes with Louvain on the quotient graph."""
        if len(reports) < 3:
            return []
        ids = [r.community_id for r in reports]
        adjacency: Dict[str, Set[str]] = {cid: set() for cid in ids}
        for (a, b), _n in links.items():
            adjacency[ids[a]].add(ids[b])
            adjacency[ids[b]].add(ids[a])
        partition = GraphAnalyzer(self._config).partition(ids, adjacency)
        buckets: Dict[int, List[RagCommunity]] = {}
        for report in reports:
            buckets.setdefault(partition[report.community_id], []).append(report)
        if len(buckets) <= 1 or len(buckets) == len(reports):
            return []
        themes: List[RagCommunity] = []
        ordered = sorted(buckets.values(), key=lambda rs: (-sum(len(r.file_ids) for r in rs), rs[0].community_id))
        for index, children in enumerate(ordered):
            children = sorted(children, key=lambda r: (-r.rating, r.community_id))
            theme_id = f"t{index}"
            files = sorted({f for r in children for f in r.file_ids})
            for child in children:
                child.parent = theme_id
            title = " + ".join(r.title for r in children[:2]) + (f" +{len(children) - 2}" if len(children) > 2 else "")
            findings: List[str] = []
            for child in children:
                findings.extend(f"[{child.title}] {item}" for item in child.findings[:2])
            rating = max(r.rating for r in children)
            themes.append(RagCommunity(
                community_id=theme_id, level=1, parent="root",
                children=[r.community_id for r in children], title=title, file_ids=files,
                summary=(
                    f"Theme of {len(children)} communities and {len(files)} files: "
                    + "; ".join(f"{r.title} ({len(r.file_ids)} files, rating {r.rating})" for r in children)
                    + "."
                ),
                findings=findings[: self._config.GRAPHRAG_REPORT_MAX_FINDINGS],
                key_entities=[e for r in children for e in r.key_entities[:2]][: self._config.GRAPHRAG_REPORT_KEY_ENTITIES],
                key_relations=[k for r in children for k in r.key_relations[:2]][: self._config.GRAPHRAG_REPORT_KEY_RELATIONS],
                rating=rating,
                rating_explanation="Theme rating = highest child community rating.",
            ))
        return themes

    def _root_report(
        self,
        reports: List[RagCommunity],
        themes: List[RagCommunity],
        nodes: List[Node],
        analysis: Optional[AnalysisResult],
    ) -> RagCommunity:
        """Project-level report summarising the top of the hierarchy."""
        cfg = self._config
        top = themes or reports
        for report in top:
            report.parent = "root"
        ranked = sorted(reports, key=lambda r: (-r.rating, r.community_id))
        gods = [nid for nid, _score in (analysis.god_nodes if analysis else [])[:5]]
        findings = [f"[{r.title}] rating {r.rating}: {r.findings[0]}" for r in ranked if r.findings]
        summary = (
            f"{len(nodes)} files in {len(reports)} communities"
            + (f" and {len(themes)} themes" if themes else "")
            + ". Highest-impact communities: "
            + ", ".join(f"{r.title} ({r.rating})" for r in ranked[:3])
            + "."
            + (" God nodes: " + ", ".join(gods) + "." if gods else "")
        )
        return RagCommunity(
            community_id="root", level=2, parent="", children=[r.community_id for r in top],
            title="Project overview", file_ids=sorted(n.node_id for n in nodes),
            summary=summary, findings=findings[: cfg.GRAPHRAG_REPORT_MAX_FINDINGS],
            key_entities=[e for r in ranked[:3] for e in r.key_entities[:2]],
            key_relations=[k for r in ranked[:3] for k in r.key_relations[:2]],
            rating=ranked[0].rating if ranked else 0.0,
            rating_explanation="Root rating = highest community rating.",
        )


class GraphRagSearcher:
    """Local (BM25 + Personalized PageRank) and global (map-reduce) retrieval."""

    def __init__(self, config: Config, index: GraphRagIndex) -> None:
        """Prepare lexical indexes and the entity random-walk graph.

        Args:
            config: GRAPHRAG_* retrieval budgets.
            index: Built or loaded GraphRagIndex.
        """
        self._config = config
        self._index = index
        self._stop = set(config.GRAPHRAG_STOPWORDS)
        self._entities = {e.entity_id: e for e in index.entities}
        self._entity_ids = [e.entity_id for e in index.entities]
        self._units_by_entity: Dict[str, List[int]] = {}
        for i, unit in enumerate(index.text_units):
            self._units_by_entity.setdefault(unit.entity_id, []).append(i)
        self._reports = {c.community_id: c for c in index.communities}
        self._level0 = [c for c in index.communities if c.level == 0]
        k1, b = config.GRAPHRAG_BM25_K1, config.GRAPHRAG_BM25_B
        self._entity_bm25 = Bm25Index([self._entity_doc(e) for e in index.entities], k1, b)
        self._unit_bm25 = Bm25Index([self._tok(u.file + " " + u.text) for u in index.text_units], k1, b)
        self._report_bm25 = Bm25Index(
            [self._tok(" ".join([c.title, c.summary] + c.findings + c.file_ids)) for c in self._level0], k1, b
        )
        self._graph: Optional[TypedGraph] = None

    def _tok(self, text: str) -> List[str]:
        """Tokenize with the configured minimum length and stopwords."""
        return tokenize(text, self._config.GRAPHRAG_MIN_TOKEN_LEN, self._stop)

    def _entity_doc(self, entity: RagEntity) -> List[str]:
        """Token document for one entity, with the name boosted."""
        name = self._tok(entity.name)
        return name + name + self._tok(entity.file) + self._tok(entity.description) + [entity.kind]

    def _walk_graph(self) -> TypedGraph:
        """Lazily build the symmetric entity graph used by Personalized PageRank."""
        if self._graph is None:
            self._graph = GraphRagBuilder(self._config)._undirected_graph(
                self._entity_ids, self._index.relationships,
            )
        return self._graph

    def choose_mode(self, query: str) -> str:
        """Pick local or global retrieval for a query.

        Args:
            query: Natural-language query.

        Returns:
            ``global`` for broad questions or when no entity matches, else ``local``.
        """
        raw = set(tokenize(query, 1, set()))
        if raw & set(self._config.GRAPHRAG_GLOBAL_HINTS):
            return "global"
        tokens = self._tok(query)
        if not tokens or not any(s > 0 for s in self._entity_bm25.scores(tokens)):
            return "global"
        return "local"

    def search(self, query: str, mode: str = "auto", budget_tokens: int = 0) -> RagContext:
        """Run local, global, or automatically chosen retrieval.

        Args:
            query: Natural-language query.
            mode: ``local``, ``global``, or ``auto``.
            budget_tokens: Context budget; 0 uses GRAPHRAG_CONTEXT_BUDGET_TOKENS.

        Returns:
            RagContext with the packed Markdown context.
        """
        chosen = self.choose_mode(query) if mode == "auto" else mode
        if chosen == "global":
            return self.global_search(query, budget_tokens)
        return self.local_search(query, budget_tokens)

    def _budget_chars(self, budget_tokens: int) -> int:
        """Convert a token budget into a character budget."""
        tokens = budget_tokens or self._config.GRAPHRAG_CONTEXT_BUDGET_TOKENS
        return max(1, tokens) * max(1, self._config.AGENT_CHARS_PER_TOKEN)

    def local_search(self, query: str, budget_tokens: int = 0) -> RagContext:
        """Entity-centric retrieval: BM25 seeds expanded by Personalized PageRank.

        Args:
            query: Natural-language query.
            budget_tokens: Context budget; 0 uses the configured default.

        Returns:
            RagContext with entities, relationships, reports, and sources.
        """
        cfg = self._config
        tokens = self._tok(query)
        entity_scores = self._entity_bm25.scores(tokens) if tokens else []
        unit_scores = self._unit_bm25.scores(tokens) if tokens else []
        seeds: Dict[str, float] = {}
        ranked_entities = sorted(
            (i for i, s in enumerate(entity_scores) if s > 0),
            key=lambda i: (-entity_scores[i], self._entity_ids[i]),
        )[: cfg.GRAPHRAG_SEED_TOP_K]
        for i in ranked_entities:
            seeds[self._entity_ids[i]] = entity_scores[i]
        ranked_units = sorted(
            (i for i, s in enumerate(unit_scores) if s > 0),
            key=lambda i: (-unit_scores[i], self._index.text_units[i].unit_id),
        )[: cfg.GRAPHRAG_SEED_TOP_K]
        top_unit = unit_scores[ranked_units[0]] if ranked_units else 1.0
        top_entity = entity_scores[ranked_entities[0]] if ranked_entities else 1.0
        for i in ranked_units:
            eid = self._index.text_units[i].entity_id
            seeds[eid] = seeds.get(eid, 0.0) + 0.5 * top_entity * unit_scores[i] / (top_unit or 1.0)
        if not seeds:
            return RagContext(query, "local", [], [], [], [],
                              f"# GraphRAG local context\n\nNo entity matches `{query}`. Try global mode.", 0)
        ppr = personalized_pagerank(
            self._walk_graph(), seeds, alpha=cfg.GRAPHRAG_PPR_ALPHA,
            max_iter=cfg.GRAPHRAG_PPR_MAX_ITER, tolerance=cfg.GRAPHRAG_PPR_TOLERANCE,
        )
        top = sorted(
            ((eid, score) for eid, score in ppr.items() if score > 0 and self._entities[eid].kind != "external"),
            key=lambda kv: (-kv[1], kv[0]),
        )[: cfg.GRAPHRAG_LOCAL_TOP_ENTITIES]
        chosen = {eid for eid, _ in top}
        relations = sorted(
            (r for r in self._index.relationships if r.source in chosen and r.target in chosen),
            key=lambda r: (-(ppr.get(r.source, 0.0) + ppr.get(r.target, 0.0)) * r.weight, r.source, r.target),
        )[: cfg.GRAPHRAG_LOCAL_TOP_RELATIONS]
        report_mass: Dict[str, float] = {}
        for eid, score in top:
            entity = self._entities[eid]
            if entity.community >= 0:
                for report in self._level0:
                    if entity.file in report.file_ids:
                        report_mass[report.community_id] = report_mass.get(report.community_id, 0.0) + score
                        break
        reports = [cid for cid, _m in sorted(report_mass.items(), key=lambda kv: (-kv[1], kv[0]))][: cfg.GRAPHRAG_LOCAL_TOP_REPORTS]
        unit_rank: Dict[int, float] = {}
        for eid, score in top:
            for ui in self._units_by_entity.get(eid, []):
                unit_rank[ui] = score * (1.0 + (unit_scores[ui] / top_unit if unit_scores else 0.0))
        units = [i for i, _s in sorted(unit_rank.items(), key=lambda kv: (-kv[1], kv[0]))][: cfg.GRAPHRAG_LOCAL_TOP_TEXT_UNITS]
        sections = [
            self._section("Entities", [
                f"- `{self._entities[eid].name}` [{self._entities[eid].kind}] "
                f"{self._location(self._entities[eid])} score={score:.4f}: {self._entities[eid].description}"
                for eid, score in top
            ]),
            self._section("Relationships", [
                f"- {self._entities[r.source].name} --{r.relation}--> {self._entities[r.target].name} "
                f"({r.confidence}, w={r.weight})"
                for r in relations
            ]),
            self._section("Community reports", [self._report_block(self._reports[cid]) for cid in reports]),
            self._section("Sources", [self._unit_block(self._index.text_units[i]) for i in units]),
        ]
        markdown, used = self._pack(f"# GraphRAG local context: {query}", sections, budget_tokens,
                                    cfg.GRAPHRAG_LOCAL_SECTION_SHARES)
        return RagContext(
            query, "local", top, [f"{r.source} --{r.relation}--> {r.target}" for r in relations],
            reports, [self._index.text_units[i].unit_id for i in units], markdown, used,
        )

    def global_search(self, query: str, budget_tokens: int = 0) -> RagContext:
        """Map-reduce over community reports for broad, corpus-level questions.

        Args:
            query: Natural-language query.
            budget_tokens: Context budget; 0 uses the configured default.

        Returns:
            RagContext with the overview plus the most relevant reports.
        """
        cfg = self._config
        tokens = self._tok(query)
        scores = self._report_bm25.scores(tokens) if tokens else [0.0] * len(self._level0)
        order = sorted(
            range(len(self._level0)),
            key=lambda i: (-scores[i], -self._level0[i].rating, self._level0[i].community_id),
        )[: cfg.GRAPHRAG_GLOBAL_TOP_REPORTS]
        query_set = set(tokens)
        mapped: List[str] = []
        chosen: List[str] = []
        for i in order:
            report = self._level0[i]
            chosen.append(report.community_id)
            matching = [f for f in report.findings if query_set & set(self._tok(f))]
            points = matching or report.findings[:2]
            mapped.append(
                f"### {report.title} (`{report.community_id}`, rating {report.rating}, relevance {scores[i]:.2f})\n"
                + report.summary + "\n" + "\n".join(f"- {p}" for p in points)
            )
        root = self._reports.get("root")
        themes = [c for c in self._index.communities if c.level == 1]
        overview: List[str] = []
        if root is not None:
            overview.append(root.summary)
        for theme in themes:
            overview.append(f"- Theme `{theme.community_id}` {theme.title}: {len(theme.file_ids)} files, rating {theme.rating}")
        sections = [
            self._section("Overview", overview),
            self._section("Relevant communities (map-reduce)", mapped),
        ]
        markdown, used = self._pack(f"# GraphRAG global context: {query}", sections, budget_tokens,
                                    cfg.GRAPHRAG_GLOBAL_SECTION_SHARES)
        return RagContext(query, "global", [], [], chosen, [], markdown, used)

    @staticmethod
    def _location(entity: RagEntity) -> str:
        """Return ``file:line`` for an entity when it has one."""
        if entity.file and entity.line:
            return f"{entity.file}:{entity.line}"
        return entity.file

    @staticmethod
    def _section(title: str, items: List[str]) -> Tuple[str, List[str]]:
        """Bundle a section title with its items."""
        return title, items

    @staticmethod
    def _report_block(report: RagCommunity) -> str:
        """Render a compact community report block."""
        lines = [f"### {report.title} (`{report.community_id}`, rating {report.rating})", report.summary]
        lines.extend(f"- {item}" for item in report.findings)
        return "\n".join(lines)

    @staticmethod
    def _unit_block(unit: RagTextUnit) -> str:
        """Render a source excerpt with its location."""
        location = f"{unit.file}:{unit.start_line}-{unit.end_line}" if unit.start_line > 0 else f"{unit.file} (session log)"
        return f"`{location}`\n```\n{unit.text}\n```"

    def _pack(
        self, header: str, sections: List[Tuple[str, List[str]]], budget_tokens: int, shares: Sequence[float],
    ) -> Tuple[str, int]:
        """Pack sections under the character budget with per-section shares.

        Each section may use its share of the budget plus whatever earlier
        sections left unused; a heading is emitted only when at least one of
        its items fits.
        """
        budget = self._budget_chars(budget_tokens)
        out = [header, ""]
        used = len(header) + 2
        carry = 0
        total_share = sum(shares[: len(sections)]) or 1.0
        for position, (title, items) in enumerate(sections):
            share = shares[position] if position < len(shares) else 0.0
            allowance = int((budget - len(header) - 2) * share / total_share) + carry
            heading = f"## {title}"
            spent = len(heading) + 2
            kept: List[str] = []
            for item in items:
                if spent + len(item) + 1 > allowance or used + spent + len(item) + 1 > budget:
                    break
                kept.append(item)
                spent += len(item) + 1
            if kept:
                out.append(heading)
                out.extend(kept)
                out.append("")
                used += spent
                carry = max(0, allowance - spent)
            else:
                carry = allowance
        text = "\n".join(out).rstrip() + "\n"
        return text, len(text) // max(1, self._config.AGENT_CHARS_PER_TOKEN)


class GraphRagStore:
    """Persists and loads the GraphRAG index as JSON, JSONL tables, and Markdown."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: GRAPHRAG_OUTPUT_DIR location.
        """
        self._config = config

    def directory(self, project_root: str) -> Path:
        """Return the output directory for a project root."""
        return Path(project_root) / self._config.GRAPHRAG_OUTPUT_DIR

    def write(self, index: GraphRagIndex, project_root: str) -> List[Path]:
        """Write index.json, JSONL tables, and REPORTS.md.

        Args:
            index: Built GraphRagIndex.
            project_root: Project root directory.

        Returns:
            Paths of written files.
        """
        out_dir = self.directory(project_root)
        out_dir.mkdir(parents=True, exist_ok=True)
        written: List[Path] = []
        data = index.to_dict()
        index_path = out_dir / "index.json"
        index_path.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        written.append(index_path)
        for name in ("entities", "relationships", "communities", "text_units"):
            path = out_dir / f"{name}.jsonl"
            rows = data[name]  # type: ignore[index]
            path.write_text(
                "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),  # type: ignore[union-attr]
                encoding="utf-8",
            )
            written.append(path)
        reports_path = out_dir / "REPORTS.md"
        reports_path.write_text(self.render_reports(index), encoding="utf-8")
        written.append(reports_path)
        return written

    def load(self, project_root: str) -> Optional[GraphRagIndex]:
        """Load a previously written index, or None when missing or invalid.

        Args:
            project_root: Project root directory.

        Returns:
            GraphRagIndex or None.
        """
        path = self.directory(project_root) / "index.json"
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None
        if not isinstance(data, dict) or data.get("meta", {}).get("schema_version") != SCHEMA_VERSION:
            return None
        try:
            return GraphRagIndex.from_dict(data)
        except TypeError:
            return None

    @staticmethod
    def render_reports(index: GraphRagIndex) -> str:
        """Render the community report hierarchy as greppable Markdown.

        Args:
            index: Built GraphRagIndex.

        Returns:
            Markdown text with one section per report, root first.
        """
        meta = index.meta
        lines = [
            "# GraphRAG Community Reports",
            "",
            f"Entities: {meta.get('entities', 0)} | Relationships: {meta.get('relationships', 0)} | "
            f"Communities: {meta.get('communities', 0)} | Themes: {meta.get('themes', 0)} | "
            f"Text units: {meta.get('text_units', 0)}",
            "",
            "Query with `readmenator . ask \"<question>\"` (local: BM25 + Personalized PageRank; "
            "global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.",
            "",
        ]
        ordered = sorted(index.communities, key=lambda c: (-c.level, -c.rating, c.community_id))
        for report in ordered:
            level = {0: "community", 1: "theme", 2: "root"}.get(report.level, str(report.level))
            lines.append(f"## {report.title} (`{report.community_id}`, {level}, rating {report.rating})")
            lines.append("")
            lines.append(report.summary)
            lines.append("")
            for item in report.findings:
                lines.append(f"- {item}")
            if report.key_entities:
                lines.append(f"- Key entities: {', '.join(report.key_entities)}")
            if report.children:
                lines.append(f"- Children: {', '.join(report.children)}")
            lines.append(f"- {report.rating_explanation}")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"
