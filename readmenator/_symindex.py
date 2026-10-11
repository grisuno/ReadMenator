"""Deterministic symbol index with call-site resolution.

Token-free and LSP-free alternative to language-server reference
resolution: builds file:line spans for every extracted symbol, finds
call sites with line numbers (exact via ``ast`` for Python,
regex approximation elsewhere), and resolves each callee to its
definition with an explicit confidence tier. Powers the ARC004
unresolved-call lint rule and the component-diagram key edges.
"""

from __future__ import annotations

import ast
import hashlib
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._models import Edge, Node

CALL_CONFIDENCE_ORDER: Tuple[str, ...] = (
    "BUILTIN",
    "SAME_FILE",
    "IMPORTED",
    "UNIQUE",
    "AMBIGUOUS",
    "EXTERNAL",
    "UNRESOLVED",
)

_CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
_DEF_RE = re.compile(
    r"^\s*(?:def|function|fn|func|public|private|protected|static|async|class|sub)\b"
    r"[\w\s<>\[\],]*?\b([A-Za-z_][A-Za-z0-9_]*)"
)


@dataclass
class SymbolDef:
    """One symbol definition with its file span.

    Attributes:
        file: Relative file identifier.
        name: Simple symbol name.
        qualified: Qualified key (``file::name``).
        kind: Symbol kind (class, function, method, ...).
        line: One-based definition line.
        end_line: One-based last line of the span.
        signature: Signature snippet.
        doc: First doc sentence.
    """

    file: str
    name: str
    qualified: str
    kind: str
    line: int
    end_line: int
    signature: str = ""
    doc: str = ""


@dataclass
class CallSite:
    """One call occurrence with its location.

    Attributes:
        file: Relative file identifier.
        caller: Enclosing symbol name ("" at module scope).
        callee: Called simple name.
        line: One-based call line (0 when unknown).
        column: Zero-based call column (0 when unknown).
    """

    file: str
    caller: str
    callee: str
    line: int = 0
    column: int = 0


@dataclass
class ResolvedCall:
    """A call site linked to its best definition candidate.

    Attributes:
        site: The originating call site.
        target_file: Definition file ("" when unresolved).
        target_line: Definition line (0 when unresolved).
        target_qualified: Qualified definition key ("" when unresolved).
        confidence: Resolution tier (see CALL_CONFIDENCE_ORDER).
        candidates: All same-name definition files (ambiguity evidence).
    """

    site: CallSite
    target_file: str = ""
    target_line: int = 0
    target_qualified: str = ""
    confidence: str = "UNRESOLVED"
    candidates: List[str] = field(default_factory=list)


def _kind_to_node_type(kind: str) -> str:
    """Map a readmenator symbol kind to a component-diagram node type."""
    normalized = (kind or "").lower()
    if normalized in ("class", "struct", "interface", "trait", "enum", "record", "protocol"):
        return "CLASS"
    if normalized in ("function", "method", "macro", "constructor"):
        return "FUNCTION"
    return "FUNCTION" if normalized else "UNKNOWN"


class SymbolIndex:
    """Builds definition spans and resolves call sites to definitions."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for builtin stoplist and call-site budgets.
        """
        self._config = config
        self._builtins = set(config.SYMINDEX_BUILTINS)

    def build(
        self, nodes: List[Node], content_map: Optional[Dict[str, str]] = None
    ) -> Dict[str, List[SymbolDef]]:
        """Index every symbol with its file span.

        Args:
            nodes: Scanned file nodes.
            content_map: Optional file contents for span end lines.

        Returns:
            Mapping of file identifier to ordered SymbolDef list.
        """
        index: Dict[str, List[SymbolDef]] = {}
        for node in sorted(nodes, key=lambda item: item.node_id):
            total = 0
            if content_map and node.node_id in content_map:
                total = len(content_map[node.node_id].splitlines())
            ordered = sorted(node.symbols, key=lambda s: (s.line, s.name))
            defs: List[SymbolDef] = []
            for pos, symbol in enumerate(ordered):
                end_line = symbol.line
                if pos + 1 < len(ordered):
                    end_line = max(symbol.line, ordered[pos + 1].line - 1)
                elif total:
                    end_line = max(symbol.line, total)
                defs.append(
                    SymbolDef(
                        file=node.node_id,
                        name=symbol.name,
                        qualified=f"{node.node_id}::{symbol.name}",
                        kind=symbol.kind,
                        line=symbol.line,
                        end_line=end_line,
                        signature=symbol.signature,
                        doc=symbol.doc,
                    )
                )
            index[node.node_id] = defs
        return index

    def methods_index(
        self, index: Dict[str, List[SymbolDef]]
    ) -> Dict[str, Dict[str, object]]:
        """Serialise definitions to component-diagram methods_index entries.

        Args:
            index: Mapping from build().

        Returns:
            Mapping of ``file|qualified`` to file, name, lines, and type.
        """
        methods: Dict[str, Dict[str, object]] = {}
        for defs in index.values():
            for symbol in defs:
                key = f"{symbol.file}|{symbol.file}::{symbol.name}"
                digest = hashlib.sha256(
                    f"{symbol.file}:{symbol.name}:{symbol.line}".encode("utf-8")
                ).hexdigest()[:16]
                methods[key] = {
                    "file_path": symbol.file,
                    "qualified_name": f"{symbol.file}::{symbol.name}",
                    "start_line": symbol.line,
                    "end_line": symbol.end_line,
                    "type": _kind_to_node_type(symbol.kind),
                    "content_hash": digest,
                }
        return methods

    def extract_call_sites(
        self,
        file_id: str,
        content: str,
        language: str,
        symbols: Optional[List[SymbolDef]] = None,
    ) -> List[CallSite]:
        """Find call sites with line numbers in one file.

        Args:
            file_id: Relative file identifier.
            content: Full file content.
            language: Language label from the scanner.
            symbols: Optional definitions for caller attribution.

        Returns:
            Call sites in file order (capped by configuration).
        """
        budget = max(1, int(self._config.SYMINDEX_MAX_CALL_SITES))
        if language == "py":
            sites = self._python_call_sites(file_id, content)
        else:
            sites = self._regex_call_sites(file_id, content, symbols or [])
        return sites[:budget]

    def resolve(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> List[ResolvedCall]:
        """Resolve every call to its best definition candidate.

        Prefers content-derived call sites (with lines) and falls back
        to parser ``calls`` edges (line 0) when content is missing.

        Args:
            nodes: Scanned file nodes.
            edges: Raw edges including ``calls`` relations.
            resolved_edges: Optional resolved-import edges.
            content_map: Optional file contents for call-site lines.

        Returns:
            Resolved calls sorted by file, line, and callee.
        """
        index = self.build(nodes, content_map)
        by_name: Dict[str, List[SymbolDef]] = {}
        for defs in index.values():
            for symbol in defs:
                by_name.setdefault(symbol.name, []).append(symbol)
        imports_of: Dict[str, List[str]] = {}
        for edge in resolved_edges or []:
            if edge.relation == "resolved_imports":
                imports_of.setdefault(edge.source, []).append(edge.target)
        sites: List[CallSite] = []
        if content_map:
            by_id = {node.node_id: node for node in nodes}
            for file_id in sorted(content_map):
                node = by_id.get(file_id)
                if node is None:
                    continue
                sites.extend(
                    self.extract_call_sites(
                        file_id, content_map[file_id], node.language,
                        index.get(file_id, []),
                    )
                )
        if not sites:
            sites.extend(self._edge_call_sites(edges))
        resolved = [self._resolve_one(site, by_name, imports_of) for site in sites]
        resolved.sort(key=lambda item: (item.site.file, item.site.line, item.site.callee))
        return resolved

    def _resolve_one(
        self,
        site: CallSite,
        by_name: Dict[str, List[SymbolDef]],
        imports_of: Dict[str, List[str]],
    ) -> ResolvedCall:
        """Resolve one call site against the definition index."""
        if site.callee in self._builtins:
            return ResolvedCall(site=site, confidence="BUILTIN")
        candidates = by_name.get(site.callee, [])
        if not candidates:
            return ResolvedCall(site=site, confidence="UNRESOLVED")
        files = sorted({symbol.file for symbol in candidates})
        same = [symbol for symbol in candidates if symbol.file == site.file]
        if same:
            best = min(same, key=lambda s: s.line)
            return ResolvedCall(
                site=site, target_file=best.file, target_line=best.line,
                target_qualified=best.qualified, confidence="SAME_FILE",
                candidates=files,
            )
        imported = {
            symbol.file
            for symbol in candidates
            if symbol.file in imports_of.get(site.file, [])
        }
        if imported:
            best = min(
                (s for s in candidates if s.file in imported),
                key=lambda s: (s.file, s.line),
            )
            return ResolvedCall(
                site=site, target_file=best.file, target_line=best.line,
                target_qualified=best.qualified, confidence="IMPORTED",
                candidates=files,
            )
        if len(files) == 1:
            best = min(candidates, key=lambda s: s.line)
            return ResolvedCall(
                site=site, target_file=best.file, target_line=best.line,
                target_qualified=best.qualified, confidence="UNIQUE",
                candidates=files,
            )
        return ResolvedCall(site=site, confidence="AMBIGUOUS", candidates=files)

    def _edge_call_sites(self, edges: List[Edge]) -> List[CallSite]:
        """Convert parser ``calls`` edges to line-less call sites."""
        sites: List[CallSite] = []
        for edge in edges:
            if edge.relation != "calls":
                continue
            caller = ""
            if "::" in edge.source:
                caller = edge.source.split("::", 1)[1]
                file_id = edge.source.split("::", 1)[0]
            else:
                file_id = edge.source
            callee = edge.target.split("::")[-1].split(".")[-1]
            if file_id and callee:
                sites.append(CallSite(file=file_id, caller=caller, callee=callee))
        return sites

    def _python_call_sites(self, file_id: str, content: str) -> List[CallSite]:
        """Extract exact call sites from Python via ``ast``.

        Args:
            file_id: Relative file identifier.
            content: Full file content.

        Returns:
            Call sites in source order.
        """
        try:
            tree = ast.parse(content)
        except (SyntaxError, ValueError):
            return []
        sites: List[CallSite] = []
        stack: List[str] = []

        class _Visitor(ast.NodeVisitor):
            """Track enclosing scopes while collecting calls."""

            def _push(self, node: ast.AST) -> None:
                """Record a scope entry by node name."""
                name = getattr(node, "name", "")
                if name:
                    stack.append(str(name))

            def _pop(self, node: ast.AST) -> None:
                """Leave the current scope when named."""
                if getattr(node, "name", "") and stack:
                    stack.pop()

            def visit_ClassDef(self, node: ast.ClassDef) -> None:
                """Visit a class body within its scope."""
                self._push(node)
                self.generic_visit(node)
                self._pop(node)

            def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
                """Visit a function body within its scope."""
                self._push(node)
                self.generic_visit(node)
                self._pop(node)

            def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
                """Visit an async function body within its scope."""
                self._push(node)
                self.generic_visit(node)
                self._pop(node)

            def visit_Call(self, node: ast.Call) -> None:
                """Record a call with its source location."""
                callee = ""
                if isinstance(node.func, ast.Name):
                    callee = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    callee = str(node.func.attr)
                if callee:
                    sites.append(
                        CallSite(
                            file=file_id,
                            caller=stack[-1] if stack else "",
                            callee=callee,
                            line=getattr(node, "lineno", 0),
                            column=getattr(node, "col_offset", 0),
                        )
                    )
                self.generic_visit(node)

        _Visitor().visit(tree)
        return sites

    def _regex_call_sites(
        self, file_id: str, content: str, symbols: List[SymbolDef]
    ) -> List[CallSite]:
        """Approximate call sites for non-Python languages.

        Caller attribution uses the nearest preceding definition line.

        Args:
            file_id: Relative file identifier.
            content: Full file content.
            symbols: Definitions for caller attribution.

        Returns:
            Call sites in source order.
        """
        sites: List[CallSite] = []
        ordered = sorted(symbols, key=lambda s: s.line)
        for lineno, line in enumerate(content.splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith(("#", "//", "*", "/*", "<!--")):
                continue
            caller = ""
            for symbol in ordered:
                if symbol.line <= lineno:
                    caller = symbol.name
                else:
                    break
            for match in _CALL_RE.finditer(line):
                name = match.group(1)
                if _DEF_RE.match(line) and name in {s.name for s in ordered}:
                    continue
                sites.append(
                    CallSite(
                        file=file_id, caller=caller, callee=name,
                        line=lineno, column=match.start(1),
                    )
                )
        return sites
