from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional, Set

from readmenator._models import Edge, Node, Symbol


class QueryEngine:
    def __init__(self, nodes: List[Node], edges: List[Edge]) -> None:
        self._nodes = nodes
        self._edges = edges
        self._symbol_index: Dict[str, List[tuple]] = self._build_symbol_index()
        self._import_graph: Dict[str, Set[str]] = self._build_import_graph()

    def _build_symbol_index(self) -> Dict[str, List[tuple]]:
        index: Dict[str, List[tuple]] = {}
        for node in self._nodes:
            for symbol in node.symbols:
                if symbol.name not in index:
                    index[symbol.name] = []
                index[symbol.name].append((node, symbol))
        return index

    def _build_import_graph(self) -> Dict[str, Set[str]]:
        graph: Dict[str, Set[str]] = {}
        for edge in self._edges:
            if edge.relation == "imports":
                if edge.source not in graph:
                    graph[edge.source] = set()
                graph[edge.source].add(edge.target)
                if edge.target not in graph:
                    graph[edge.target] = set()
        return graph

    def find_symbol(self, name: str) -> Optional[List[tuple]]:
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
        results = self.find_symbol(name)
        if results is None:
            return None
        lines: List[str] = []
        for node, symbol in results:
            lines.append(f"Symbol: {symbol.name}")
            lines.append(f"  Type: {symbol.kind}")
            lines.append(f"  File: {node.node_id}")
            lines.append(f"  Line: {symbol.line}")
            if symbol.doc:
                lines.append(f"  Doc: {symbol.doc}")
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
        result: List[str] = []
        for edge in self._edges:
            if edge.relation == "imports" and edge.target == target:
                result.append(edge.source)
        return result

    def find_path(self, symbol_a: str, symbol_b: str) -> Optional[List[str]]:
        results_a = self.find_symbol(symbol_a)
        results_b = self.find_symbol(symbol_b)
        if not results_a or not results_b:
            return None
        file_a = results_a[0][0].node_id
        file_b = results_b[0][0].node_id
        if file_a == file_b:
            return [file_a]
        graph: Dict[str, List[str]] = {}
        for edge in self._edges:
            if edge.relation == "imports":
                if edge.source not in graph:
                    graph[edge.source] = []
                graph[edge.source].append(edge.target)
        visited: Set[str] = set()
        queue: deque = deque()
        queue.append((file_a, [file_a]))
        visited.add(file_a)
        while queue:
            current, path = queue.popleft()
            for neighbor in graph.get(current, []):
                if neighbor == file_b:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def query(self, question: str) -> str:
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
