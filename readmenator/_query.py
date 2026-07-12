"""Query engine for the readmenator knowledge base.

Supports natural-language-like search (``query``), symbol explanation
(``explain``), dependency-path tracing (``find_path``), and a concise
codebase overview (``summary``). All queries operate on an in-memory
index built from the scanned Node/Edge list.
"""

from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional, Set

from readmenator._models import Edge, Node, Symbol


class QueryEngine:
    """In-memory query engine over the scanned knowledge graph.

    Builds a symbol-name index and an import-adjacency graph on
    construction. Provides exact and fuzzy symbol lookup, detailed
    explanation output, BFS shortest-path resolution, free-text
    search, and a summary report.
    """

    def __init__(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ):
        """Initialise internal indexes from scanned data.

        Args:
            nodes: List of scanned file nodes.
            edges: List of import-relationship edges.
            resolved_edges: Optional resolved-import edges (both
                source and target are project file IDs).
        """
        self._nodes = nodes
        self._edges = edges
        self._resolved_edges = resolved_edges or []
        self._symbol_index: Dict[str, List[tuple]] = self._build_symbol_index()
        self._import_graph: Dict[str, Set[str]] = self._build_import_graph()
        self._resolved_graph: Dict[str, Set[str]] = self._build_resolved_graph()

    def _build_symbol_index(self) -> Dict[str, List[tuple]]:
        """Build a name-to-list-of-(node, symbol) lookup.

        Returns:
            Dict mapping symbol names to list of (Node, Symbol) tuples.
        """
        index: Dict[str, List[tuple]] = {}
        for node in self._nodes:
            for symbol in node.symbols:
                if symbol.name not in index:
                    index[symbol.name] = []
                index[symbol.name].append((node, symbol))
        return index

    def _build_import_graph(self) -> Dict[str, Set[str]]:
        """Build an adjacency map from import edges.

        Returns:
            Dict mapping each file node_id to its set of import targets.
        """
        graph: Dict[str, Set[str]] = {}
        for edge in self._edges:
            if edge.relation == "imports":
                if edge.source not in graph:
                    graph[edge.source] = set()
                graph[edge.source].add(edge.target)
                if edge.target not in graph:
                    graph[edge.target] = set()
        return graph

    def _build_resolved_graph(self) -> Dict[str, Set[str]]:
        """Build an adjacency map from resolved import edges.

        Only contains edges where both source and target are
        project files (not external modules).

        Returns:
            Dict mapping each file node_id to files it imports within the project.
        """
        graph: Dict[str, Set[str]] = {}
        file_ids = {n.node_id for n in self._nodes}
        for edge in self._resolved_edges:
            if edge.source in file_ids and edge.target in file_ids:
                if edge.source not in graph:
                    graph[edge.source] = set()
                graph[edge.source].add(edge.target)
                if edge.target not in graph:
                    graph[edge.target] = set()
        return graph

    def find_symbol(self, name: str) -> Optional[List[tuple]]:
        """Look up *name* by exact match, then by substring fuzzy match.

        Returns:
            A list of (Node, Symbol) tuples, or ``None`` if not found.
        """
        results = self._symbol_index.get(name)
        if results:
            return results
        lower_name = name.lower()
        fuzzy: List[tuple] = []
        for sym_name, entries in self._symbol_index.items():
            if lower_name in sym_name.lower():
                fuzzy.extend(entries)
        if fuzzy:
            return fuzzy
        return None

    def explain(self, name: str) -> Optional[str]:
        """Return a detailed multi-line explanation of *name*.

        Includes kind, file path, line number, docstring, signature,
        imports, reverse dependencies ("imported by"), and sibling
        symbols in the same file.

        Returns:
            Formatted string or ``None`` if the symbol is not found.
        """
        results = self.find_symbol(name)
        if results is None:
            return None
        lines: List[str] = []
        for node, symbol in results:
            lines.append(f"Symbol: {symbol.name}")
            lines.append(f"  Type: {symbol.kind}")
            lines.append(f"  File: {node.node_id}")
            lines.append(f"  Line: {symbol.line}")
            if node.doc:
                lines.append(f"  File Doc: {node.doc}")
            if symbol.doc:
                lines.append(f"  Symbol Doc: {symbol.doc}")
            if symbol.signature:
                lines.append(f"  Signature: {symbol.signature}")
            file_imports = self._import_graph.get(node.node_id, set())
            if file_imports:
                lines.append(f"  Imports ({len(file_imports)}): {', '.join(sorted(file_imports))}")
            incoming = self._find_incoming_imports(node.node_id)
            if incoming:
                lines.append(f"  Imported by ({len(incoming)}): {', '.join(sorted(incoming))}")
            siblings = [s for s in node.symbols if s.name != symbol.name]
            if siblings:
                lines.append(f"  Siblings in file ({len(siblings)}): {', '.join(s.name for s in siblings[:10])}")
                if len(siblings) > 10:
                    lines[-1] += "..."
            lines.append("")
        return "\n".join(lines)

    def _find_incoming_imports(self, target: str) -> List[str]:
        """List all node IDs that import *target*."""
        result: List[str] = []
        for edge in self._edges:
            if edge.relation == "imports" and edge.target == target:
                result.append(edge.source)
        return result

    def find_path(self, symbol_a: str, symbol_b: str) -> Optional[List[str]]:
        """Find the shortest import path from *symbol_a* to *symbol_b*.

        Uses BFS on the resolved import graph (project-internal edges)
        first, traversing in both directions (forward = A imports B,
        reverse = B is imported by A). Falls back to the raw import
        graph if no resolved path exists.

        Returns:
            List of file node IDs forming the dependency chain, or ``None``.
        """
        results_a = self.find_symbol(symbol_a)
        results_b = self.find_symbol(symbol_b)
        if not results_a or not results_b:
            return None
        file_a = results_a[0][0].node_id
        file_b = results_b[0][0].node_id
        if file_a == file_b:
            return [file_a]

        bidir = self._make_bidirectional(self._resolved_graph)
        path = self._bfs_shortest_path(bidir, file_a, file_b)
        if path is not None:
            return path

        bidir_raw = self._make_bidirectional(self._import_graph)
        path = self._bfs_shortest_path(bidir_raw, file_a, file_b)
        return path

    @staticmethod
    def _make_bidirectional(graph: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
        """Convert a directed graph to a bidirectional one.

        For each edge A→B, adds both A→B and B→A edges.
        """
        bidir: Dict[str, Set[str]] = {}
        for src, targets in graph.items():
            if src not in bidir:
                bidir[src] = set()
            for tgt in targets:
                bidir[src].add(tgt)
                if tgt not in bidir:
                    bidir[tgt] = set()
                bidir[tgt].add(src)
        return bidir

    def _bfs_shortest_path(
        self,
        graph: Dict[str, Set[str]],
        start: str,
        goal: str,
    ) -> Optional[List[str]]:
        """Run BFS to find the shortest path from *start* to *goal*.

        Returns:
            List of node IDs or ``None`` if no path exists.
        """
        visited: Set[str] = {start}
        queue: deque = deque()
        queue.append((start, [start]))
        while queue:
            current, path = queue.popleft()
            for neighbor in graph.get(current, set()):
                if neighbor == goal:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def query(self, question: str) -> str:
        """Free-text search over symbols and file paths.

        Tokenises the input, matches against symbol names (substring)
        and then against file paths as a fallback. Returns a
        human-readable result string summarising matches or a
        no-results message with KB statistics.
        """
        terms = question.lower().split()
        relevant_symbols: List[tuple] = []
        for term in terms:
            if len(term) < 3:
                continue
            for sym_name, entries in self._symbol_index.items():
                if term in sym_name.lower():
                    relevant_symbols.extend(entries)
        if not relevant_symbols:
            file_matches: List[str] = []
            for term in terms:
                if len(term) < 3:
                    continue
                for node in self._nodes:
                    if term in node.node_id.lower():
                        file_matches.append(node.node_id)
            if file_matches:
                unique_files = sorted(set(file_matches))
                total_syms = sum(len(n.symbols) for n in self._nodes if n.node_id in unique_files)
                return (
                    f"Found {len(unique_files)} files matching your query.\n"
                    f"Files: {', '.join(unique_files)}\n"
                    f"Symbols in matching files: {total_syms}"
                )
            return (
                "No matches found in the knowledge base. "
                "The KB contains "
                f"{sum(len(n.symbols) for n in self._nodes)} symbols across "
                f"{len(self._nodes)} files. Try different terms or "
                "run --rebuild if the codebase has changed."
            )
        seen = set()
        unique: List[tuple] = []
        for entry in relevant_symbols:
            key = (entry[0].node_id, entry[1].name)
            if key not in seen:
                seen.add(key)
                unique.append(entry)
        lines: List[str] = [
            f"Found {len(unique)} symbol(s) matching your query:"
        ]
        for node, symbol in unique:
            doc_short = f" - {symbol.doc[:60]}" if symbol.doc else ""
            lines.append(
                f"  - {symbol.name} ({symbol.kind}, {node.node_id}:{symbol.line}){doc_short}"
            )
        return "\n".join(lines)

    def summary(self) -> str:
        """Return a concise overview of the loaded knowledge base.

        Reports file count, symbol count, import count, language
        diversity, top-level modules (by import popularity), and
        lists of key class-like and function-like symbols.
        """
        nodes = self._nodes
        edges = self._edges
        total_symbols = sum(len(n.symbols) for n in nodes)
        langs = set(n.language for n in nodes)
        top_modules = sorted(
            nodes,
            key=lambda n: (
                sum(1 for e in edges if e.source == n.node_id),
                len(n.symbols),
            ),
            reverse=True,
        )[:10]
        module_lines: List[str] = []
        for node in top_modules:
            imp_count = sum(1 for e in edges if e.source == node.node_id)
            module_lines.append(
                f"  - {node.label} ({len(node.symbols)} symbols, "
                f"{imp_count} imports)"
            )

        all_classes: List[str] = []
        all_functions: List[str] = []
        for node in nodes:
            for sym in node.symbols:
                if sym.kind in ("class", "struct", "interface", "trait", "enum"):
                    all_classes.append(sym.name)
                elif sym.kind in ("function", "method"):
                    all_functions.append(sym.name)

        lines: List[str] = [
            f"Knowledge base loaded: {len(nodes)} files, "
            f"{total_symbols} symbols, "
            f"{len(edges)} imports across "
            f"{len(langs)} languages.",
            "",
            "Top-level modules:",
        ]
        lines.extend(module_lines)
        if all_classes:
            lines.append("")
            lines.append(
                f"Key classes: {', '.join(all_classes[:10])}"
                f"{'...' if len(all_classes) > 10 else ''}"
            )
        if all_functions:
            lines.append("")
            lines.append(
                f"Key functions: {', '.join(all_functions[:10])}"
                f"{'...' if len(all_functions) > 10 else ''}"
            )
        lines.append("")
        lines.append(
            "Ask me anything about this codebase. I will answer from the "
            "knowledge base."
        )
        return "\n".join(lines)
