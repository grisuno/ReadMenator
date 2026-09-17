"""Procedural intra-function dataflow analysis for readmenator.

Detects classic logic bug classes without tokens, types, or control-flow
graphs: use of uninitialized locals, dead stores (assigned but never
read), and unchecked allocator results. Pure regex over function body
spans derived from parsed symbol line ranges. Every finding is marked
INFERRED: heuristics trade recall for reviewable, line-grounded leads.
"""

from __future__ import annotations

import logging
import re
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import DataflowIssue, Node

logger = logging.getLogger(__name__)

_FUNCTION_KINDS = frozenset({"function", "method"})

_KEYWORDS = frozenset({
    "if", "else", "for", "while", "do", "switch", "case", "default",
    "break", "continue", "return", "goto", "sizeof", "typedef",
    "struct", "union", "enum", "static", "const", "volatile",
    "register", "extern", "auto", "signed", "unsigned", "void",
    "int", "char", "short", "long", "float", "double", "bool",
    "true", "false", "NULL", "null", "nil", "None",
})

_TYPE_WORDS = (
    r"void|char|short|int|long|float|double|_Bool|bool|size_t|ssize_t|"
    r"ptrdiff_t|int8_t|int16_t|int32_t|int64_t|uint8_t|uint16_t|uint32_t|"
    r"uint64_t|FILE|DIR|struct\s+\w+|union\s+\w+|enum\s+\w+|\w+_t"
)

_DECL_RE = re.compile(
    r"^\s*(?:(?:static|const|volatile|register|extern|auto|signed|unsigned)\s+)*"
    r"(?:(?P<type>" + _TYPE_WORDS + r")\b\s*)"
    r"(?P<ptr>\*+)?\s*(?P<name>[A-Za-z_]\w*)"
    r"(?P<array>\s*\[[^\]]*\])?"
    r"(?:\s*=\s*(?P<init>[^;]+))?;\s*$"
)

_ASSIGN_RE = re.compile(
    r"\b([A-Za-z_]\w*)\s*(?:=(?![=<>!])|\+=|-=|\*=|/=|%=|<<=|>>=|&=|\|=|\^=)"
)

_INCR_RE = re.compile(r"(?:\+\+|--)\s*([A-Za-z_]\w*)|([A-Za-z_]\w*)\s*(?:\+\+|--)")

_ADDR_RE = re.compile(r"&\s*([A-Za-z_]\w*)")

_IDENT_RE = re.compile(r"[A-Za-z_]\w*")

_CALL_RE = re.compile(r"([A-Za-z_]\w*)\s*\(")

_MEMBER_RE = re.compile(r"(?:\.|->)\s*([A-Za-z_]\w*)")

_ALLOC_RE = re.compile(
    r"\b(malloc|calloc|realloc|strdup|fopen|fopen64|popen|socket|opendir|mmap|open)\s*\("
)

_PARAM_RE = re.compile(r"([A-Za-z_]\w*)(?:\s*\[[^\]]*\])?\s*(?:,|\))")

_COMMENT_RE = re.compile(r"//.*$")
_STRING_RE = re.compile(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'')

_BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)

_SIZEOF_PAREN_RE = re.compile(r"\bsizeof\s*\([^)]*\)")
_SIZEOF_IDENT_RE = re.compile(r"\bsizeof\s+[A-Za-z_]\w*")

_OUT_PARAM_FUNCS = frozenset({
    "strcpy", "strncpy", "strcat", "strncat", "sprintf", "snprintf",
    "memset", "memcpy", "memmove", "bzero", "bcopy",
    "fgets", "fread", "read", "recv", "recvfrom", "recvmsg",
    "scanf", "fscanf", "sscanf", "gets", "getcwd", "realpath",
    "strtol", "strtoul", "strtod", "strtok", "strtok_r",
})

_LOOP_RE = re.compile(r"^\s*(while|for)\s*\(")

_READ_ONLY_CALLS = frozenset({
    "printf", "fprintf", "puts", "strlen", "strcmp", "strncmp",
    "strstr", "strchr", "strrchr", "memcmp", "memchr",
})

_SUBSCRIPT_STORE_RE = re.compile(r"\b([A-Za-z_]\w*)\s*\[[^\]]*\]\s*=(?![=])")

_ALIAS_STORE_RE = re.compile(r"\*\s*([A-Za-z_]\w*)\s*(?:\+\+|--)?\s*=(?![=<>!])")

_ASM_OUT_RE = re.compile(r'"=[^"]*"\s*\(\s*([A-Za-z_]\w*)\s*\)')


def _strip_noise(line: str) -> str:
    """Remove comments and string contents that confuse identifier scans.

    Strings are blanked before comment stripping so that ``//`` inside
    URL literals is not mistaken for a comment opener.
    """
    line = _STRING_RE.sub('""', line)
    line = _COMMENT_RE.sub("", line)
    return line


def _strip_block_comments(content: str) -> str:
    """Blank block comments while preserving newlines and line numbers."""

    def _blank(match: re.Match) -> str:
        return "".join("\n" if ch == "\n" else " " for ch in match.group(0))

    return _BLOCK_COMMENT_RE.sub(_blank, content)


def _strip_sizeof(line: str) -> str:
    """Blank sizeof operands, which never evaluate their argument at runtime."""
    line = _SIZEOF_PAREN_RE.sub("sizeof()", line)
    return _SIZEOF_IDENT_RE.sub("sizeof", line)


class DataflowAnalyzer:
    """Regex-based intra-function dataflow checker over scanned content."""

    def __init__(self, config: Config) -> None:
        """Store configuration for enable flag and issue caps."""
        self._config = config

    def analyze(
        self, nodes: List[Node], content_map: Optional[Dict[str, str]]
    ) -> List[DataflowIssue]:
        """Check every function body span and return capped issues."""
        if not self._config.DATAFLOW_ENABLED:
            return []
        content_map = content_map or {}
        issues: List[DataflowIssue] = []
        for node in nodes:
            content = content_map.get(node.node_id, "")
            if not content:
                continue
            lines = _strip_block_comments(content).split("\n")
            depths = self._brace_depths(lines)
            spans = self._function_spans(node, len(lines), depths)
            for func_name, start, end in spans:
                issues.extend(
                    self._analyze_function(node.node_id, func_name, lines, start, end)
                )
                if len(issues) >= self._config.DATAFLOW_MAX_ISSUES:
                    return issues[: self._config.DATAFLOW_MAX_ISSUES]
        return issues

    @staticmethod
    def _brace_depths(lines: List[str]) -> List[int]:
        """Return the brace depth before each line of noise-stripped code."""
        depths: List[int] = []
        depth = 0
        for raw in lines:
            depths.append(depth)
            clean = _strip_noise(raw)
            depth += clean.count("{") - clean.count("}")
            depth = max(0, depth)
        return depths

    def _function_spans(
        self, node: Node, total_lines: int, depths: Optional[List[int]] = None
    ) -> List[Tuple[str, int, int]]:
        """Return (name, start_idx, end_idx) spans for function symbols.

        Only function lines and file-scope (depth 0) symbols terminate a
        span; local struct, enum, or variable declarations inside a body
        do not truncate the enclosing function.
        """
        ordered = sorted(
            [s for s in node.symbols if s.kind in _FUNCTION_KINDS],
            key=lambda s: s.line,
        )
        bounds: Set[int] = {total_lines + 1}
        for sym in node.symbols:
            if sym.kind in _FUNCTION_KINDS:
                bounds.add(sym.line)
                continue
            depth = depths[sym.line - 1] if depths and 0 < sym.line <= len(depths) else 0
            if depth == 0:
                bounds.add(sym.line)
        spans: List[Tuple[str, int, int]] = []
        for sym in ordered:
            end = min(b for b in bounds if b > sym.line)
            spans.append((sym.name, sym.line - 1, end - 1))
        return spans

    def _analyze_function(
        self, file_id: str, func: str, lines: List[str], start: int, end: int
    ) -> List[DataflowIssue]:
        """Run def-use checks over one function body span."""
        body = lines[start:end]
        params = self._params_of(lines[start] if start < len(lines) else "")
        declared: Dict[str, int] = {}
        initialized: Set[str] = set(params)
        assigned: Dict[str, int] = {}
        first_assigned: Dict[str, int] = {}
        assign_depth: Dict[str, int] = {}
        assign_end: Dict[str, Tuple[int, int]] = {}
        arrays: Set[str] = set()
        array_stores: Dict[str, int] = {}
        addr_taken: Set[str] = set()
        static_vars: Set[str] = set()
        file_scope_vars: Set[str] = set()
        derived_ptrs: Set[str] = set()
        alias_ptrs: Set[str] = set()
        derived_alias: Dict[str, str] = {}
        deriv_reads: Set[Tuple[str, int]] = set()
        reads: Dict[str, List[Tuple[int, int]]] = {}
        alloc_at: Dict[str, int] = {}
        depth = 0
        if body:
            depth = _strip_noise(body[0]).count("{") - _strip_noise(body[0]).count("}")
        call_open: Optional[str] = None
        paren_balance = 0

        for offset, raw in enumerate(body[1:], start=1):
            lineno = start + offset + 1
            line = _strip_noise(raw)
            depth_before = depth
            depth += line.count("{") - line.count("}")
            if not line.strip():
                continue
            decl = _DECL_RE.match(line)
            if decl and not self._is_prototype(line):
                name = decl.group("name")
                if decl.group("type") and name not in _KEYWORDS:
                    declared[name] = lineno
                    if depth_before == 0:
                        file_scope_vars.add(name)
                    if re.match(r"^\s*static\b", line):
                        static_vars.add(name)
                    if decl.group("array") is not None:
                        arrays.add(name)
                    init = decl.group("init")
                    if init is not None:
                        initialized.add(name)
                        assigned[name] = lineno
                        first_assigned[name] = lineno
                        assign_depth[name] = depth_before
                        assign_end[name] = (lineno, decl.end())
                        if decl.group("ptr") and self._mentions_param(init, params):
                            derived_ptrs.add(name)
                        if decl.group("ptr") and "&" in init:
                            alias_ptrs.add(name)
                        if decl.group("ptr"):
                            for ident in _IDENT_RE.findall(init):
                                if ident in arrays and ident != name:
                                    derived_alias[name] = ident
                                    deriv_reads.add((ident, lineno))
                                    break
                        if _ALLOC_RE.search(init):
                            alloc_at[name] = lineno
                        self._scan_reads(init, lineno, reads, first_assigned, set(declared))
                        self._scan_out_params(init, lineno, first_assigned)
                        self._scan_array_args(init, lineno, arrays, first_assigned)
                    continue
            self._scan_inline_aliases(
                line, lineno, arrays, derived_alias, deriv_reads
            )
            assign_matches = list(_ASSIGN_RE.finditer(line))
            for match in assign_matches:
                name = match.group(1)
                if name in _KEYWORDS:
                    continue
                if self._is_member(line, match.start()):
                    base = self._member_base(line, match.start())
                    if base is not None and base not in _KEYWORDS:
                        first_assigned.setdefault(base, lineno)
                    continue
                assigned[name] = lineno
                first_assigned.setdefault(name, lineno)
                assign_depth[name] = depth_before
                assign_end[name] = (lineno, match.end())
                rhs = line[match.end():]
                if _ALLOC_RE.search(rhs):
                    alloc_at[name] = lineno
            for match in _INCR_RE.finditer(line):
                name = match.group(1) or match.group(2)
                hit = match.start(1) if match.group(1) else match.start(2)
                if name not in _KEYWORDS and not self._is_member(line, hit):
                    assigned[name] = lineno
                    first_assigned.setdefault(name, lineno)
                    assign_depth[name] = depth_before
                    assign_end[name] = (lineno, match.end())
            for match in _ADDR_RE.finditer(line):
                name = match.group(1)
                if name not in _KEYWORDS:
                    first_assigned.setdefault(name, lineno)
                    addr_taken.add(name)
                    reads.setdefault(name, []).append((lineno, match.start(1)))
            for match in _SUBSCRIPT_STORE_RE.finditer(line):
                name = match.group(1)
                if name not in _KEYWORDS:
                    first_assigned.setdefault(name, lineno)
                    if name in arrays:
                        array_stores.setdefault(name, lineno)
            for match in _ALIAS_STORE_RE.finditer(line):
                alias = match.group(1)
                base = derived_alias.get(alias)
                if base is not None:
                    first_assigned.setdefault(base, lineno)
                    array_stores.setdefault(base, lineno)
            for match in _ASM_OUT_RE.finditer(_COMMENT_RE.sub("", raw)):
                name = match.group(1)
                if name not in _KEYWORDS:
                    first_assigned.setdefault(name, lineno)
            self._scan_out_params(line, lineno, first_assigned)
            self._scan_array_args(line, lineno, arrays, first_assigned)
            if call_open is not None and call_open not in _READ_ONLY_CALLS:
                for ident in _IDENT_RE.findall(line):
                    if ident in arrays:
                        first_assigned.setdefault(ident, lineno)
            call_open, paren_balance = self._track_call_continuation(
                line, call_open, paren_balance
            )
            calls = {m.group(1) for m in _CALL_RE.finditer(line)}
            members = {m.group(1) for m in _MEMBER_RE.finditer(line)}
            read_line = _strip_sizeof(line)
            for match in _SUBSCRIPT_STORE_RE.finditer(line):
                name_start = match.start(1)
                read_line = (
                    read_line[:name_start] + " " * len(match.group(1)) + read_line[match.end(1):]
                )
            for match in _IDENT_RE.finditer(read_line):
                name = match.group(0)
                if name in _KEYWORDS or name in members:
                    continue
                if name in calls and name not in declared:
                    continue
                reads.setdefault(name, []).append((lineno, match.start()))

        issues: List[DataflowIssue] = []
        body_text = "\n".join(_strip_noise(raw) for raw in body)
        loop_reads: Set[str] = set()
        for offset, raw in enumerate(body[1:], start=1):
            clean = _strip_noise(raw)
            if _LOOP_RE.match(raw):
                for match in _IDENT_RE.finditer(clean):
                    if match.group(0) not in _KEYWORDS:
                        loop_reads.add(match.group(0))
        for name, decl_line in declared.items():
            if name in initialized and name not in assigned:
                continue
            if name in static_vars or name in file_scope_vars:
                continue
            first_assign = first_assigned.get(name)
            name_reads = [
                pos for pos in reads.get(name, []) if pos[0] > decl_line
            ]
            name_reads = [
                pos for pos in name_reads if (name, pos[0]) not in deriv_reads
            ]
            store_before_read = (
                name in array_stores and array_stores[name] <= min(name_reads)[0]
            ) if name_reads else False
            if name_reads and not store_before_read and (
                first_assign is None or min(name_reads)[0] < first_assign
            ):
                issues.append(DataflowIssue(
                    file_path=file_id, function=func, line=min(name_reads)[0],
                    kind="UNINIT_USE", variable=name,
                    description=(
                        f"`{name}` may be read before initialization "
                        f"(declared line {decl_line})."
                    ),
                ))
            last_assign = assigned.get(name)
            if last_assign is not None and name not in loop_reads:
                end_pos = assign_end.get(name, (last_assign, -1))
                later_reads = [pos for pos in reads.get(name, []) if pos > end_pos]
                nested_flow = assign_depth.get(name, 1) > 1 and bool(reads.get(name))
                escaped = name in addr_taken
                static_used = (
                    name in static_vars or name in file_scope_vars
                ) and len(re.findall(rf"\b{re.escape(name)}\b", "\n".join(lines))) > 2
                derived = name in derived_ptrs or name in alias_ptrs
                if not later_reads and name in declared and not nested_flow and not escaped and not static_used and not derived:
                    issues.append(DataflowIssue(
                        file_path=file_id, function=func, line=last_assign,
                        kind="DEAD_STORE", variable=name,
                        description=(
                            f"`{name}` assigned at line {last_assign} "
                            f"but never read afterwards."
                        ),
                    ))
        for name, alloc_line in alloc_at.items():
            if not self._null_checked(body_text, name):
                issues.append(DataflowIssue(
                    file_path=file_id, function=func, line=alloc_line,
                    kind="UNCHECKED_ALLOC", variable=name,
                    description=(
                        f"Result of allocator stored in `{name}` "
                        f"is never checked against NULL."
                    ),
                ))
        return issues

    @staticmethod
    def _scan_reads(
        text: str, lineno: int,
        reads: Dict[str, List[Tuple[int, int]]], assigned: Dict[str, int],
        declared_names: Optional[Set[str]] = None,
    ) -> None:
        """Record identifier reads and address-takes inside an expression."""
        text = _strip_sizeof(text)
        declared_names = declared_names or set()
        for match in _ADDR_RE.finditer(text):
            name = match.group(1)
            if name not in _KEYWORDS:
                assigned.setdefault(name, lineno)
                reads.setdefault(name, []).append((lineno, match.start(1)))
        calls = {m.group(1) for m in _CALL_RE.finditer(text)}
        members = {m.group(1) for m in _MEMBER_RE.finditer(text)}
        for match in _IDENT_RE.finditer(text):
            name = match.group(0)
            if name in _KEYWORDS or name in members:
                continue
            if name in calls and name not in declared_names:
                continue
            reads.setdefault(name, []).append((lineno, match.start()))

    @staticmethod
    def _scan_inline_aliases(
        line: str, lineno: int, arrays: Set[str],
        derived_alias: Dict[str, str], deriv_reads: Set[Tuple[str, int]],
    ) -> None:
        """Discover pointer-from-array aliases in mid-line statements."""
        for segment in re.split(r"[{};]", line):
            segment = segment.strip()
            if not segment:
                continue
            match = _DECL_RE.match(segment + ";")
            if not match or not match.group("type") or not match.group("ptr"):
                continue
            name = match.group("name")
            if name in _KEYWORDS:
                continue
            init = match.group("init") or ""
            for ident in _IDENT_RE.findall(init):
                if ident in arrays and ident != name:
                    derived_alias[name] = ident
                    deriv_reads.add((ident, lineno))
                    break

    @staticmethod
    def _scan_out_params(line: str, lineno: int, assigned: Dict[str, int]) -> None:
        """Treat known filler/scan call arguments as assignments."""
        for match in _CALL_RE.finditer(line):
            if match.group(1) not in _OUT_PARAM_FUNCS:
                continue
            tail = line[match.end():].split(";")[0]
            for ident in _IDENT_RE.findall(tail):
                if ident not in _KEYWORDS:
                    assigned.setdefault(ident, lineno)

    @staticmethod
    def _scan_array_args(
        line: str, lineno: int, arrays: Set[str], assigned: Dict[str, int]
    ) -> None:
        """Treat arrays passed to non-readonly calls as assignments."""
        for match in _CALL_RE.finditer(line):
            if match.group(1) in _READ_ONLY_CALLS:
                continue
            tail = line[match.end():].split(";")[0]
            for ident in _IDENT_RE.findall(tail):
                if ident in arrays:
                    assigned.setdefault(ident, lineno)

    @staticmethod
    def _params_of(signature_line: str) -> Set[str]:
        """Extract parameter names from a function signature line."""
        start = signature_line.find("(")
        end = signature_line.rfind(")")
        if start < 0 or end <= start:
            return set()
        inner = signature_line[start + 1:end]
        params: Set[str] = set()
        for chunk in inner.split(","):
            chunk = chunk.strip().rstrip("*").strip()
            if not chunk or chunk in ("void", "..."):
                continue
            tokens = chunk.split()
            if tokens:
                name = tokens[-1].lstrip("*")
                if re.fullmatch(r"[A-Za-z_]\w*", name or ""):
                    params.add(name)
        return params

    @staticmethod
    def _track_call_continuation(
        line: str, call_open: Optional[str], paren_balance: int
    ) -> Tuple[Optional[str], int]:
        """Track whether the next line continues an unclosed call."""
        depth = paren_balance
        opener = call_open
        for match in re.finditer(r"([A-Za-z_]\w*)?\s*(\(|\))", line):
            name, paren = match.group(1), match.group(2)
            if paren == "(":
                if depth == 0:
                    opener = None if name in _KEYWORDS else name
                depth += 1
            else:
                depth = max(0, depth - 1)
                if depth == 0:
                    opener = None
        return opener, depth

    @staticmethod
    def _mentions_param(text: str, params: Set[str]) -> bool:
        """Return True when an expression mentions a function parameter."""
        if not params:
            return False
        found = set(_IDENT_RE.findall(text))
        return bool(found & params)

    @staticmethod
    def _is_member(line: str, pos: int) -> bool:
        """Return True when the identifier at pos is a struct member access."""
        before = line[:pos].rstrip()
        return before.endswith(".") or before.endswith("->")

    @staticmethod
    def _member_base(line: str, pos: int) -> Optional[str]:
        """Return the base identifier of a member access chain."""
        match = re.search(
            r"([A-Za-z_]\w*)(\s*\[[^\]]*\])?\s*(?:\.|->)", line[:pos]
        )
        return match.group(1) if match else None

    @staticmethod
    def _is_prototype(line: str) -> bool:
        """Return True for declaration lines that are actually prototypes."""
        return "(" in line and ")" in line and "{" not in line and "=" not in line.split(")")[0]

    @staticmethod
    def _null_checked(body_text: str, name: str) -> bool:
        """Return True when body contains a NULL/boolean check for name."""
        member = rf"(?:->|\.){re.escape(name)}\b"
        patterns = [
            rf"!\s*{re.escape(name)}\b",
            rf"!\s*[A-Za-z_][\w.\->]*?(?:->|\.){re.escape(name)}\b",
            rf"\b{re.escape(name)}\s*(==|!=)\s*NULL",
            rf"NULL\s*(==|!=)\s*{re.escape(name)}\b",
            rf"{member}\s*(==|!=)\s*NULL",
            rf"assert\w*\([^)]*\b{re.escape(name)}\b[^)]*\)",
            rf"\b{re.escape(name)}\s*(==|!=)\s*MAP_FAILED",
            rf"\b{re.escape(name)}\s*(==|!=|<|<=|>|>=)\s*-1",
            rf"-1\s*(==|!=)\s*{re.escape(name)}\b",
            rf"\b{re.escape(name)}\s*<\s*0",
            rf"\b{re.escape(name)}\s*>=\s*0",
            rf"\b{re.escape(name)}\s*>\s*-1",
            rf"if\s*\(\s*{re.escape(name)}\s*\)",
        ]
        return any(re.search(p, body_text) for p in patterns)
