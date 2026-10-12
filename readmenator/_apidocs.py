"""Deterministic API reference model: extraction, cross-references, coverage.

Builds a Sphinx / Doxygen style API reference from the scanned graph
with zero tokens. Python modules get a full ``ast`` pass (exact
signatures with annotations and defaults, decorators, nested classes,
properties, dataclass fields, ``__all__`` export lists, inferred raises
and return behaviour). Every other language reuses the parser symbols,
recovers the raw comment block above each declaration, nests members
into their enclosing type by brace or indentation span, and splits
signatures into typed parameters. Docstrings in any convention are
parsed by ``readmenator._docstrings``. Cross-references cover class
hierarchies, call graphs (callers and callees via the symbol index),
and see-also targets; documentation coverage and stale-doc warnings
mirror Doxygen's ``WARN_IF_UNDOCUMENTED`` and ``WARN_IF_DOC_ERROR``.
"""

from __future__ import annotations

import ast
import re
import warnings
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Dict, Iterable, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._docstrings import DocComment, parse_docstring, recover_comment
from readmenator._models import Edge, Node, Symbol
from readmenator._pytypes import PythonReceiverTypes
from readmenator._symindex import SymbolIndex

KIND_MODULE = "module"
CLASS_KINDS: Tuple[str, ...] = (
    "class", "struct", "interface", "trait", "enum", "record", "protocol",
    "union", "exception", "extension", "object", "impl", "type_alias",
)
CALLABLE_KINDS: Tuple[str, ...] = (
    "function", "method", "constructor", "property", "classmethod",
    "staticmethod", "macro", "async_function",
)
DATA_KINDS: Tuple[str, ...] = ("attribute", "variable", "constant", "field")
CONTAINER_KINDS: Tuple[str, ...] = ("class", "struct", "interface", "trait", "enum",
                                    "record", "protocol", "union", "exception",
                                    "extension", "object", "impl")

WARN_UNDOCUMENTED = "DOC001"
WARN_PARAM_MISSING = "DOC002"
WARN_PARAM_UNKNOWN = "DOC003"
WARN_RETURN_MISSING = "DOC004"
WARN_RAISE_MISSING = "DOC005"

_BRACE_LANGUAGES: Set[str] = {
    "c", "cpp", "cc", "cxx", "h", "hpp", "hxx", "hh", "h++", "tcc", "inl", "inc", "C",
    "go", "rs", "js", "ts", "jsx", "tsx", "java", "cs", "php", "dart", "swift",
    "kt", "kts", "scala", "sc",
}
_C_HEADER_LANGUAGES: Set[str] = {"h", "hpp", "hxx", "hh", "h++", "inl", "tcc"}
_COLON_TYPED_LANGUAGES: Set[str] = {"rs", "ts", "tsx", "kt", "kts", "swift", "scala", "sc", "nim", "py", "gd"}
_MODIFIER_WORDS: Set[str] = {
    "public", "private", "protected", "internal", "static", "final", "abstract",
    "virtual", "override", "async", "inline", "extern", "const", "constexpr",
    "export", "default", "pub", "fn", "func", "function", "def", "sealed",
    "open", "fileprivate", "readonly", "unsafe", "synchronized", "native",
    "suspend", "operator", "infix", "tailrec", "mutating", "class", "struct",
    "interface", "trait", "enum", "record", "proc", "method", "template",
    "volatile", "register", "noexcept", "explicit", "friend", "partial",
    "new", "let", "var", "val", "type", "sub", "defp", "defmacro", "local",
}
_PRIVATE_MODIFIERS: Set[str] = {"private", "fileprivate", "internal"}
_IDENT_RE = re.compile(r"[A-Za-z_$][\w$]*")
_VOID_RETURNS: Set[str] = {"", "void", "None", "Unit", "()", "unit", "Void", "nil"}
_MODULE_CONSTANT_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")


@dataclass
class ApiParam:
    """One parameter of a callable signature.

    Attributes:
        name: Parameter name as written (``*args`` keeps its star).
        annotation: Declared type text ("" when untyped).
        default: Default value source text ("" when required).
        kind: positional_only, positional, var_positional, keyword_only, var_keyword.
    """

    name: str
    annotation: str = ""
    default: str = ""
    kind: str = "positional"

    def to_dict(self) -> Dict[str, str]:
        """Serialise to a plain dict for JSON output."""
        return {"name": self.name, "annotation": self.annotation,
                "default": self.default, "kind": self.kind}


@dataclass
class ApiEntity:
    """One documented API element (module, type, callable, or data member).

    Attributes:
        uid: Stable identifier (``file`` for modules, ``file::Qual.name`` otherwise).
        name: Simple name.
        qualname: Dotted name inside its module.
        kind: Entity kind (module, class, method, function, attribute, ...).
        file: Relative source file.
        line: One-based definition line.
        end_line: One-based last line of the definition span.
        language: Scanner language label.
        signature: Display signature.
        params: Signature parameters (receiver excluded).
        returns: Declared return type text.
        decorators: Decorator / attribute / annotation texts.
        bases: Base type names as written.
        modifiers: Declaration modifiers (static, abstract, async, ...).
        visibility: public, protected, or private.
        doc: Parsed documentation.
        parent: uid of the enclosing entity ("" for modules).
        members: uids of directly contained entities.
        inferred_raises: Exception names raised in the body (Python).
        returns_value: Whether the body returns a value (None when unknown).
        value: Source text of a constant or attribute default.
        base_uids: Resolved project uids for bases.
        subclasses: uids of project types deriving from this one.
        calls: uids this callable calls (resolved, deduplicated).
        called_by: uids of callables that call this one.
    """

    uid: str
    name: str
    qualname: str
    kind: str
    file: str
    line: int
    end_line: int = 0
    language: str = ""
    signature: str = ""
    params: List[ApiParam] = field(default_factory=list)
    returns: str = ""
    decorators: List[str] = field(default_factory=list)
    bases: List[str] = field(default_factory=list)
    modifiers: List[str] = field(default_factory=list)
    visibility: str = "public"
    doc: DocComment = field(default_factory=DocComment)
    parent: str = ""
    members: List[str] = field(default_factory=list)
    inferred_raises: List[str] = field(default_factory=list)
    returns_value: Optional[bool] = None
    value: str = ""
    base_uids: List[str] = field(default_factory=list)
    subclasses: List[str] = field(default_factory=list)
    calls: List[str] = field(default_factory=list)
    called_by: List[str] = field(default_factory=list)

    @property
    def is_documented(self) -> bool:
        """Return True when any documentation text was found."""
        return not self.doc.is_empty

    def to_dict(self) -> Dict[str, object]:
        """Serialise to a plain dict for JSON output."""
        return {
            "uid": self.uid, "name": self.name, "qualname": self.qualname,
            "kind": self.kind, "file": self.file, "line": self.line,
            "end_line": self.end_line, "language": self.language,
            "signature": self.signature,
            "params": [p.to_dict() for p in self.params],
            "returns": self.returns, "decorators": list(self.decorators),
            "bases": list(self.bases), "modifiers": list(self.modifiers),
            "visibility": self.visibility, "doc": self.doc.to_dict(),
            "parent": self.parent, "members": list(self.members),
            "inferred_raises": list(self.inferred_raises),
            "returns_value": self.returns_value, "value": self.value,
            "base_uids": list(self.base_uids), "subclasses": list(self.subclasses),
            "calls": list(self.calls), "called_by": list(self.called_by),
        }


@dataclass
class DocWarning:
    """One documentation quality warning.

    Attributes:
        code: Stable rule code (DOC001 ... DOC005).
        uid: Entity the warning is about.
        file: Relative source file.
        line: One-based line.
        message: Human-readable explanation.
    """

    code: str
    uid: str
    file: str
    line: int
    message: str

    def to_dict(self) -> Dict[str, object]:
        """Serialise to a plain dict for JSON output."""
        return {"code": self.code, "uid": self.uid, "file": self.file,
                "line": self.line, "message": self.message}


@dataclass
class ApiReference:
    """Complete API reference for one project.

    Attributes:
        entities: Every entity keyed by uid, in deterministic order.
        modules: Module uids sorted by path.
        warnings: Documentation quality warnings.
        coverage: Coverage statistics (overall, per kind, per module).
        meta: Build metadata (counts, languages, truncation).
    """

    entities: Dict[str, ApiEntity] = field(default_factory=dict)
    modules: List[str] = field(default_factory=list)
    warnings: List[DocWarning] = field(default_factory=list)
    coverage: Dict[str, object] = field(default_factory=dict)
    meta: Dict[str, object] = field(default_factory=dict)

    def children(self, uid: str, kinds: Optional[Iterable[str]] = None) -> List[ApiEntity]:
        """Return direct members of *uid*, optionally filtered by kind, in source order."""
        entity = self.entities.get(uid)
        if entity is None:
            return []
        wanted = set(kinds) if kinds is not None else None
        result = [self.entities[m] for m in entity.members if m in self.entities]
        if wanted is not None:
            result = [e for e in result if e.kind in wanted]
        return result

    def to_dict(self, schema_version: int) -> Dict[str, object]:
        """Serialise the whole reference for ``api.json``."""
        return {
            "schema_version": schema_version,
            "meta": dict(self.meta),
            "coverage": self.coverage,
            "modules": list(self.modules),
            "entities": [e.to_dict() for e in self.entities.values()],
            "warnings": [w.to_dict() for w in self.warnings],
        }


def _unparse(node: Optional[ast.AST]) -> str:
    """Return the source text of an AST node ("" for None)."""
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except (ValueError, TypeError, AttributeError, RecursionError):
        return ""


class _PythonExtractor:
    """Extracts Python API entities with the native ``ast`` module."""

    def __init__(self, file_id: str, language: str, include_private: bool) -> None:
        """Initialise for one file.

        Args:
            file_id: Relative file path (module uid).
            language: Scanner language label.
            include_private: Keep underscore-prefixed names.
        """
        self._file = file_id
        self._language = language
        self._include_private = include_private
        self.entities: List[ApiEntity] = []
        self.module_doc = ""
        self.exports: Optional[Set[str]] = None

    def extract(self, content: str) -> bool:
        """Parse *content*; return False when it is not valid Python."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                tree = ast.parse(content, filename=self._file)
            except (SyntaxError, ValueError, RecursionError):
                return False
        self.module_doc = ast.get_docstring(tree) or ""
        self.exports = self._read_all(tree)
        self._walk_body(tree.body, self._file, "")
        return True

    @staticmethod
    def _read_all(tree: ast.Module) -> Optional[Set[str]]:
        """Return the names listed in a literal module ``__all__``."""
        for stmt in tree.body:
            targets: List[ast.expr] = []
            value: Optional[ast.expr] = None
            if isinstance(stmt, ast.Assign):
                targets, value = stmt.targets, stmt.value
            elif isinstance(stmt, ast.AnnAssign) and stmt.value is not None:
                targets, value = [stmt.target], stmt.value
            for target in targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(value, (ast.List, ast.Tuple)):
                        names = {
                            elt.value for elt in value.elts
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
                        }
                        return names
        return None

    def _visibility(self, name: str, parent_uid: str) -> str:
        """Classify *name* as public, protected, or private."""
        if name.startswith("__") and name.endswith("__"):
            return "public"
        if name.startswith("__"):
            return "private"
        if name.startswith("_"):
            return "protected" if parent_uid != self._file else "private"
        if parent_uid == self._file and self.exports is not None and name not in self.exports:
            return "private"
        return "public"

    def _keep(self, name: str, visibility: str, documented: bool) -> bool:
        """Return True when the entity belongs in the reference."""
        if name.startswith("__") and name.endswith("__"):
            return name in ("__init__", "__call__", "__new__") or documented
        if visibility == "public":
            return True
        return self._include_private

    def _walk_body(self, body: List[ast.stmt], parent_uid: str, prefix: str) -> List[str]:
        """Extract entities from one statement list; return member uids."""
        members: List[str] = []
        in_class = parent_uid != self._file
        for pos, stmt in enumerate(body):
            if isinstance(stmt, ast.ClassDef):
                uid = self._class(stmt, parent_uid, prefix)
                if uid:
                    members.append(uid)
            elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                uid = self._function(stmt, parent_uid, prefix, in_class)
                if uid:
                    members.append(uid)
            elif isinstance(stmt, (ast.Assign, ast.AnnAssign)):
                uid = self._data(stmt, body, pos, parent_uid, prefix, in_class)
                if uid:
                    members.append(uid)
        return members

    def _class(self, node: ast.ClassDef, parent_uid: str, prefix: str) -> str:
        """Extract one class and its members."""
        qualname = f"{prefix}{node.name}"
        uid = f"{self._file}::{qualname}"
        doc = parse_docstring(ast.get_docstring(node) or "")
        visibility = self._visibility(node.name, parent_uid)
        if not self._keep(node.name, visibility, not doc.is_empty):
            return ""
        bases = [_unparse(b) for b in node.bases]
        keywords = [f"{k.arg}={_unparse(k.value)}" for k in node.keywords if k.arg]
        decorators = [_unparse(d) for d in node.decorator_list]
        kind = "class"
        base_tails = {b.split(".")[-1].split("[")[0] for b in bases}
        if base_tails & {"Enum", "IntEnum", "StrEnum", "Flag", "IntFlag"}:
            kind = "enum"
        elif base_tails & {"Protocol"}:
            kind = "protocol"
        elif any(t.endswith(("Error", "Exception", "Warning")) for t in base_tails) or base_tails & {"BaseException"}:
            kind = "exception"
        modifiers: List[str] = []
        if any(d.split("(")[0].split(".")[-1] == "dataclass" for d in decorators):
            modifiers.append("dataclass")
        if base_tails & {"ABC"} or any(k.startswith("metaclass=") and "ABCMeta" in k for k in keywords):
            modifiers.append("abstract")
        signature = f"class {node.name}"
        if bases or keywords:
            signature += f"({', '.join(bases + keywords)})"
        entity = ApiEntity(
            uid=uid, name=node.name, qualname=qualname, kind=kind, file=self._file,
            line=node.lineno, end_line=getattr(node, "end_lineno", node.lineno) or node.lineno,
            language=self._language, signature=signature, decorators=decorators,
            bases=bases, modifiers=modifiers, visibility=visibility, doc=doc,
            parent=parent_uid,
        )
        self.entities.append(entity)
        entity.members = self._walk_body(node.body, uid, f"{qualname}.")
        init = next(
            (e for e in self.entities if e.uid == f"{uid}.__init__" or e.uid == f"{self._file}::{qualname}.__init__"),
            None,
        )
        if init is not None and entity.doc.is_empty is False and init.doc.is_empty:
            init.doc = DocComment(params=list(entity.doc.params), style=entity.doc.style)
        if "dataclass" in modifiers and init is None:
            fields = [e for e in self.entities if e.parent == uid and e.kind == "attribute"]
            entity.params = [ApiParam(name=f.name, annotation=f.returns, default=f.value) for f in fields]
        return uid

    def _params(self, args: ast.arguments, drop_receiver: bool) -> List[ApiParam]:
        """Convert ``ast.arguments`` into ordered ApiParam records."""
        params: List[ApiParam] = []
        positional = list(args.posonlyargs) + list(args.args)
        defaults: List[Optional[ast.expr]] = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
        for pos, arg in enumerate(positional):
            kind = "positional_only" if pos < len(args.posonlyargs) else "positional"
            params.append(ApiParam(arg.arg, _unparse(arg.annotation), _unparse(defaults[pos]), kind))
        if args.vararg is not None:
            params.append(ApiParam(f"*{args.vararg.arg}", _unparse(args.vararg.annotation), "", "var_positional"))
        for arg, default in zip(args.kwonlyargs, args.kw_defaults):
            params.append(ApiParam(arg.arg, _unparse(arg.annotation), _unparse(default), "keyword_only"))
        if args.kwarg is not None:
            params.append(ApiParam(f"**{args.kwarg.arg}", _unparse(args.kwarg.annotation), "", "var_keyword"))
        if drop_receiver and params and params[0].kind in ("positional_only", "positional"):
            params = params[1:]
        return params

    @staticmethod
    def _render_params(params: List[ApiParam], args: ast.arguments, receiver: str) -> str:
        """Render a parameter list including ``/`` and ``*`` separators."""
        parts: List[str] = [receiver] if receiver else []
        posonly = len(args.posonlyargs) - (1 if receiver and args.posonlyargs else 0)
        star_done = False
        for pos, param in enumerate(params):
            if param.kind == "keyword_only" and not star_done:
                parts.append("*")
                star_done = True
            if param.kind in ("var_positional",):
                star_done = True
            text = param.name
            if param.annotation:
                text += f": {param.annotation}"
            if param.default:
                text += f" = {param.default}" if param.annotation else f"={param.default}"
            parts.append(text)
            if posonly > 0 and pos == posonly - 1:
                parts.append("/")
        return ", ".join(parts)

    @staticmethod
    def _body_facts(node: ast.AST) -> Tuple[List[str], Optional[bool], bool]:
        """Return (raised exception names, returns a value, is generator)."""
        raises: List[str] = []
        returns_value = False
        generator = False
        stack: List[ast.AST] = list(ast.iter_child_nodes(node))
        while stack:
            child = stack.pop()
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
                continue
            if isinstance(child, ast.Raise) and child.exc is not None:
                target = child.exc.func if isinstance(child.exc, ast.Call) else child.exc
                name = _unparse(target).split(".")[-1]
                if name and name[0].isupper() and name not in raises:
                    raises.append(name)
            elif isinstance(child, ast.Return) and child.value is not None:
                if not (isinstance(child.value, ast.Constant) and child.value.value is None):
                    returns_value = True
            elif isinstance(child, (ast.Yield, ast.YieldFrom)):
                generator = True
            stack.extend(ast.iter_child_nodes(child))
        return sorted(raises), returns_value, generator

    def _function(
        self, node: ast.AST, parent_uid: str, prefix: str, in_class: bool
    ) -> str:
        """Extract one function, method, property, or constructor."""
        assert isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        qualname = f"{prefix}{node.name}"
        uid = f"{self._file}::{qualname}"
        doc = parse_docstring(ast.get_docstring(node) or "")
        visibility = self._visibility(node.name, parent_uid)
        if not self._keep(node.name, visibility, not doc.is_empty):
            return ""
        decorators = [_unparse(d) for d in node.decorator_list]
        tails = [d.split("(")[0].split(".")[-1] for d in decorators]
        kind = "method" if in_class else "function"
        modifiers: List[str] = []
        receiver = ""
        if in_class:
            if "staticmethod" in tails:
                kind, receiver = "staticmethod", ""
            elif "classmethod" in tails:
                kind, receiver = "classmethod", "cls"
            elif "property" in tails or "cached_property" in tails or any(d.endswith((".setter", ".getter", ".deleter")) for d in decorators):
                kind, receiver = "property", "self"
            else:
                receiver = "self"
            if node.name == "__init__":
                kind = "constructor"
        if isinstance(node, ast.AsyncFunctionDef):
            modifiers.append("async")
        if "abstractmethod" in tails:
            modifiers.append("abstract")
        if "overload" in tails:
            modifiers.append("overload")
        drop = bool(receiver)
        all_args = list(node.args.posonlyargs) + list(node.args.args)
        if drop and all_args:
            receiver = all_args[0].arg
        params = self._params(node.args, drop and bool(all_args))
        rendered = self._render_params(params, node.args, receiver if drop and all_args else "")
        returns = _unparse(node.returns)
        prefix_word = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
        signature = f"{prefix_word} {node.name}({rendered})"
        if returns:
            signature += f" -> {returns}"
        raises, returns_value, generator = self._body_facts(node)
        if generator:
            modifiers.append("generator")
        entity = ApiEntity(
            uid=uid, name=node.name, qualname=qualname, kind=kind, file=self._file,
            line=node.lineno, end_line=getattr(node, "end_lineno", node.lineno) or node.lineno,
            language=self._language, signature=signature, params=params, returns=returns,
            decorators=decorators, modifiers=modifiers, visibility=visibility, doc=doc,
            parent=parent_uid, inferred_raises=raises,
            returns_value=returns_value or generator,
        )
        self.entities.append(entity)
        return uid

    def _data(
        self, stmt: ast.stmt, body: List[ast.stmt], pos: int,
        parent_uid: str, prefix: str, in_class: bool,
    ) -> str:
        """Extract a module constant or class attribute."""
        if isinstance(stmt, ast.AnnAssign):
            target = stmt.target
            annotation = _unparse(stmt.annotation)
            value = stmt.value
        else:
            assert isinstance(stmt, ast.Assign)
            if len(stmt.targets) != 1:
                return ""
            target = stmt.targets[0]
            annotation = ""
            value = stmt.value
        if not isinstance(target, ast.Name):
            return ""
        name = target.id
        if name.startswith("__") and name.endswith("__"):
            return ""
        if not in_class and not isinstance(stmt, ast.AnnAssign) and not _MODULE_CONSTANT_RE.match(name):
            return ""
        doc_text = ""
        if pos + 1 < len(body):
            nxt = body[pos + 1]
            if isinstance(nxt, ast.Expr) and isinstance(nxt.value, ast.Constant) and isinstance(nxt.value.value, str):
                doc_text = nxt.value.value
        doc = parse_docstring(doc_text)
        visibility = self._visibility(name, parent_uid)
        if not self._keep(name, visibility, not doc.is_empty):
            return ""
        qualname = f"{prefix}{name}"
        value_text = _unparse(value)
        kind = "attribute" if in_class else ("constant" if _MODULE_CONSTANT_RE.match(name) else "variable")
        signature = name
        if annotation:
            signature += f": {annotation}"
        if value_text and len(value_text) <= 80:
            signature += f" = {value_text}"
        entity = ApiEntity(
            uid=f"{self._file}::{qualname}", name=name, qualname=qualname, kind=kind,
            file=self._file, line=stmt.lineno,
            end_line=getattr(stmt, "end_lineno", stmt.lineno) or stmt.lineno,
            language=self._language, signature=signature, returns=annotation,
            visibility=visibility, doc=doc, parent=parent_uid, value=value_text,
        )
        self.entities.append(entity)
        return entity.uid


def _matching_close(lines: List[str], start: int, scan_limit: int) -> int:
    """Return the zero-based line closing the first ``{`` at or after *start*.

    Skips string literals and comments roughly; returns -1 when no
    opening brace appears within *scan_limit* lines or it never closes.
    """
    depth = 0
    opened = False
    in_block = False
    for index in range(start, len(lines)):
        if not opened and index - start > scan_limit:
            return -1
        line = lines[index]
        pos = 0
        quote = ""
        while pos < len(line):
            char = line[pos]
            pair = line[pos:pos + 2]
            if in_block:
                if pair == "*/":
                    in_block = False
                    pos += 2
                    continue
                pos += 1
                continue
            if quote:
                if char == "\\":
                    pos += 2
                    continue
                if char == quote:
                    quote = ""
                pos += 1
                continue
            if pair == "//":
                break
            if pair == "/*":
                in_block = True
                pos += 2
                continue
            if char in ("'", '"', "`"):
                quote = char
            elif char == ";" and not opened and index == start:
                pass
            elif char == "{":
                depth += 1
                opened = True
            elif char == "}":
                depth -= 1
                if opened and depth == 0:
                    return index
            pos += 1
        if not opened and line.split("//")[0].rstrip().endswith(";"):
            return -1
    return -1


def _indent_end(lines: List[str], start: int) -> int:
    """Return the zero-based last line of an indentation block opened at *start*."""
    if start >= len(lines):
        return start
    base = len(lines[start]) - len(lines[start].lstrip())
    last = start
    for index in range(start + 1, len(lines)):
        text = lines[index]
        if not text.strip():
            continue
        indent = len(text) - len(text.lstrip())
        if indent <= base:
            if text.strip() in ("end", "end;", "end)", "end,"):
                return index
            break
        last = index
    return last


def _split_top_level(text: str, sep: str = ",") -> List[str]:
    """Split *text* on *sep* outside brackets and strings."""
    parts: List[str] = []
    depth = 0
    quote = ""
    current: List[str] = []
    for char in text:
        if quote:
            current.append(char)
            if char == quote:
                quote = ""
            continue
        if char in ("'", '"', "`"):
            quote = char
        elif char in "([{<":
            depth += 1
        elif char in ")]}>":
            depth = max(0, depth - 1)
        elif char == sep and depth == 0:
            parts.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    tail = "".join(current).strip()
    if tail:
        parts.append(tail)
    return parts


def _param_span(signature: str, name: str) -> Tuple[int, int]:
    """Return the (open, close) indexes of the parameter list after *name*."""
    anchor = signature.find(name)
    start = signature.find("(", anchor if anchor >= 0 else 0)
    if start < 0:
        return -1, -1
    depth = 0
    for index in range(start, len(signature)):
        if signature[index] == "(":
            depth += 1
        elif signature[index] == ")":
            depth -= 1
            if depth == 0:
                return start, index
    return start, -1


def parse_signature_params(signature: str, name: str, language: str) -> Tuple[List[ApiParam], str]:
    """Split a non-Python signature into parameters and a return type.

    Args:
        signature: Declaration snippet from the parser or the source line.
        name: Declared symbol name (anchors the parameter list).
        language: Scanner language label.

    Returns:
        Tuple of (parameters, return type text).
    """
    open_at, close_at = _param_span(signature, name)
    if open_at < 0:
        return [], ""
    inner = signature[open_at + 1:close_at] if close_at > 0 else signature[open_at + 1:]
    params: List[ApiParam] = []
    for raw in _split_top_level(inner):
        text = raw.strip()
        if not text or text in ("void", "self", "&self", "&mut self", "mut self", "this"):
            continue
        default = ""
        if "=" in text and "=>" not in text:
            text, default = (part.strip() for part in text.split("=", 1))
        text = re.sub(r"^(?:final|const|readonly|ref|out|in|inout|params|var|val|let|mut)\s+", "", text)
        text = re.sub(r"^@\w+(?:\([^)]*\))?\s+", "", text)
        annotation = ""
        pname = text
        if ":" in text and "::" not in text and language in _COLON_TYPED_LANGUAGES | {"js", "jsx", "dart"}:
            pname, annotation = (part.strip() for part in text.split(":", 1))
        elif language == "go":
            bits = text.split(None, 1)
            pname = bits[0]
            annotation = bits[1] if len(bits) > 1 else ""
        elif language == "php":
            match = re.search(r"(\$\w+)", text)
            pname = match.group(1) if match else text
            annotation = text[:match.start()].strip() if match else ""
        else:
            idents = list(_IDENT_RE.finditer(text))
            if len(idents) >= 2:
                last = idents[-1]
                pname = last.group(0)
                annotation = text[:last.start()].strip()
                suffix = text[last.end():].strip()
                if suffix:
                    annotation = f"{annotation} {suffix}".strip()
            elif idents:
                pname = idents[0].group(0)
                if language in ("c", "h", "cpp", "hpp", "cc", "cxx") and pname == text:
                    annotation, pname = text, ""
        pname = pname.strip().lstrip("&*") if language not in ("py",) else pname
        kind = "positional"
        if pname.startswith("...") or text.startswith("...") or pname == "...":
            kind = "var_positional"
            pname = pname.lstrip(".") or "..."
        params.append(ApiParam(name=pname, annotation=annotation, default=default, kind=kind))
    tail = signature[close_at + 1:].strip() if close_at > 0 else ""
    returns = ""
    arrow = re.match(r"^(?:->|:)\s*([^{=;]+)", tail)
    if arrow:
        returns = arrow.group(1).strip()
        returns = re.sub(r"\s+(where|throws|async)\b.*$", "", returns).strip()
    elif language == "go" and tail:
        returns = tail.split("{")[0].strip()
    else:
        head = signature[:signature.find(name)] if name in signature else ""
        words = [w for w in re.split(r"\s+", head.strip()) if w and w.strip("*&") not in _MODIFIER_WORDS]
        if words and not head.strip().endswith((".", "(")):
            candidate = " ".join(words).strip()
            if not candidate.startswith(("@", "#", "[")):
                returns = candidate
    return params, returns


def is_vendored_path(file_id: str, config: Config) -> bool:
    """Return True for minified bundles and files under vendored third-party trees.

    Args:
        file_id: Relative file path.
        config: Settings with APIDOCS_SKIP_SUFFIXES and APIDOCS_EXCLUDE_DIRS.
    """
    path = PurePosixPath(file_id)
    if path.name.endswith(tuple(config.APIDOCS_SKIP_SUFFIXES)):
        return True
    return any(part in config.APIDOCS_EXCLUDE_DIRS for part in path.parts[:-1])


class ApiReferenceBuilder:
    """Builds an ApiReference from scanned nodes, edges, and file contents."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for privacy, private members, tests, and budgets.
        """
        self._config = config

    def _is_test_path(self, file_id: str) -> bool:
        """Return True when *file_id* belongs to a test tree."""
        tokens = set()
        for part in PurePosixPath(file_id).parts:
            stem = part.rsplit(".", 1)[0].lower()
            tokens.add(stem)
            tokens.update(t for t in re.split(r"[_\-.]", stem) if t)
        return bool(tokens & set(self._config.APIDOCS_TEST_PATH_TOKENS))

    def _is_vendored(self, file_id: str) -> bool:
        """Return True for minified bundles and vendored third-party trees."""
        return is_vendored_path(file_id, self._config)

    def build(
        self,
        nodes: List[Node],
        edges: Optional[List[Edge]] = None,
        resolved_edges: Optional[List[Edge]] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> ApiReference:
        """Build the full API reference.

        Args:
            nodes: Scanned file nodes.
            edges: Raw edges (``inherits`` and ``calls`` used for cross-refs).
            resolved_edges: Resolved import edges (call resolution context).
            content_map: File contents; enables exact Python extraction and
                raw comment recovery. Without it, parser symbols are used.

        Returns:
            Deterministic ApiReference with coverage and warnings.
        """
        cfg = self._config
        contents = content_map or {}
        reference = ApiReference()
        budget = max(1, int(cfg.APIDOCS_MAX_ENTITIES))
        truncated = False
        selected = [
            n for n in sorted(nodes, key=lambda item: item.node_id)
            if (cfg.APIDOCS_INCLUDE_TESTS or not self._is_test_path(n.node_id))
            and not self._is_vendored(n.node_id)
        ]
        for node in selected:
            if len(reference.entities) >= budget:
                truncated = True
                break
            for entity in self._extract_file(node, contents.get(node.node_id)):
                if len(reference.entities) >= budget:
                    truncated = True
                    break
                reference.entities[entity.uid] = entity
            if node.node_id in reference.entities:
                reference.modules.append(node.node_id)
        for entity in reference.entities.values():
            if entity.parent and entity.parent in reference.entities:
                parent = reference.entities[entity.parent]
                if entity.uid not in parent.members:
                    parent.members.append(entity.uid)
        for entity in reference.entities.values():
            entity.members = [m for m in entity.members if m in reference.entities]
        if cfg.PRIVACY_MODE:
            for entity in reference.entities.values():
                entity.doc = DocComment(
                    params=[type(p)(name=p.name, type=p.type) for p in entity.doc.params],
                    style=entity.doc.style,
                ) if entity.doc.params else DocComment()
                entity.value = ""
        self._link_inheritance(reference, edges or [])
        self._inherit_docs(reference)
        self._link_calls(reference, nodes, edges or [], resolved_edges, contents)
        reference.warnings = self._lint(reference)
        reference.coverage = self._coverage(reference)
        languages: Dict[str, int] = {}
        for uid in reference.modules:
            lang = reference.entities[uid].language
            languages[lang] = languages.get(lang, 0) + 1
        kinds: Dict[str, int] = {}
        for entity in reference.entities.values():
            kinds[entity.kind] = kinds.get(entity.kind, 0) + 1
        reference.meta = {
            "modules": len(reference.modules),
            "entities": len(reference.entities),
            "languages": dict(sorted(languages.items())),
            "kinds": dict(sorted(kinds.items())),
            "truncated": truncated,
            "skipped_files": len(nodes) - len(selected),
            "privacy_mode": bool(cfg.PRIVACY_MODE),
        }
        return reference

    def _module_entity(self, node: Node, doc_text: str) -> ApiEntity:
        """Create the module entity for *node*."""
        return ApiEntity(
            uid=node.node_id, name=PurePosixPath(node.node_id).name,
            qualname=node.node_id, kind=KIND_MODULE, file=node.node_id, line=1,
            language=node.language, doc=parse_docstring(doc_text),
        )

    def _extract_file(self, node: Node, content: Optional[str]) -> List[ApiEntity]:
        """Extract the module entity plus every member entity of one file."""
        if node.language == "py" and content is not None:
            extractor = _PythonExtractor(node.node_id, node.language, self._config.APIDOCS_INCLUDE_PRIVATE)
            if extractor.extract(content):
                module = self._module_entity(node, extractor.module_doc or node.doc)
                module.end_line = len(content.splitlines())
                for entity in extractor.entities:
                    if entity.parent == node.node_id:
                        module.members.append(entity.uid)
                return [module] + extractor.entities
        return self._extract_generic(node, content)

    def _extract_generic(self, node: Node, content: Optional[str]) -> List[ApiEntity]:
        """Extract entities for non-Python files from parser symbols."""
        cfg = self._config
        lines = content.split("\n") if content is not None else []
        ordered = sorted(
            (s for s in node.symbols if not self._is_include_guard(s.name, s.kind, s.doc)),
            key=lambda s: (s.line, s.name),
        )
        module_doc = node.doc
        if ordered and lines and module_doc:
            first_doc = recover_comment(lines, ordered[0].line, node.language, cfg.APIDOCS_DOC_LOOKBACK_LINES)
            squash = " ".join(re.sub(r"[#*/!\-]+", " ", module_doc).split())
            first_squash = " ".join(re.sub(r"[#*/!\-]+", " ", first_doc).split())
            if first_squash and (squash == first_squash or squash.startswith(first_squash) or first_squash.startswith(squash)):
                module_doc = ""
        module = self._module_entity(node, module_doc)
        module.end_line = len(lines)
        spans: List[Tuple[int, int]] = []
        for pos, symbol in enumerate(ordered):
            start = max(0, symbol.line - 1)
            end = -1
            if lines:
                if node.language in _BRACE_LANGUAGES:
                    end = _matching_close(lines, start, cfg.APIDOCS_BRACE_SCAN_LINES)
                elif symbol.kind in CONTAINER_KINDS or symbol.kind in CALLABLE_KINDS:
                    end = _indent_end(lines, start)
            if end < 0:
                end = (ordered[pos + 1].line - 2) if pos + 1 < len(ordered) else max(start, len(lines) - 1)
                if symbol.kind not in CONTAINER_KINDS:
                    end = max(start, min(end, start))
            spans.append((symbol.line, max(symbol.line, end + 1)))
        entities: List[ApiEntity] = []
        stack: List[Tuple[ApiEntity, int]] = []
        seen: Set[str] = set()
        for symbol, (line, end_line) in zip(ordered, spans):
            while stack and line > stack[-1][1]:
                stack.pop()
            parent_entity = stack[-1][0] if stack else None
            parent_uid = parent_entity.uid if parent_entity else node.node_id
            qual_prefix = f"{parent_entity.qualname}." if parent_entity else ""
            qualname = f"{qual_prefix}{symbol.name}"
            uid = f"{node.node_id}::{qualname}"
            if uid in seen:
                uid = f"{uid}@{line}"
            seen.add(uid)
            raw_doc = ""
            if lines and not cfg.PRIVACY_MODE:
                raw_doc = recover_comment(lines, line, node.language, cfg.APIDOCS_DOC_LOOKBACK_LINES)
            doc = parse_docstring(raw_doc or symbol.doc)
            kind = symbol.kind
            if parent_entity is not None and kind == "function":
                kind = "method"
                if symbol.name in (parent_entity.name, "constructor", "__construct", "init", "initialize", "new"):
                    kind = "constructor"
            decl = lines[line - 1].strip() if 0 < line <= len(lines) else ""
            signature = symbol.signature or decl
            if lines and "(" in signature and ")" not in signature:
                joined = " ".join(l.strip() for l in lines[line - 1:min(len(lines), line - 1 + cfg.APIDOCS_BRACE_SCAN_LINES)])
                close = joined.find(")", joined.find(symbol.name))
                if close > 0:
                    signature = joined[:close + 1] + joined[close + 1:].split("{")[0].split(";")[0]
            signature = " ".join(signature.split()).rstrip("{ ").rstrip()
            params: List[ApiParam] = []
            returns = ""
            if kind in CALLABLE_KINDS or "(" in signature and kind not in CONTAINER_KINDS:
                params, returns = parse_signature_params(signature, symbol.name, node.language)
            visibility, modifiers = self._generic_visibility(symbol.name, decl or signature, node.language, parent_entity)
            bases: List[str] = []
            if kind in CONTAINER_KINDS:
                bases = self._generic_bases(signature, symbol.name)
            entity = ApiEntity(
                uid=uid, name=symbol.name, qualname=qualname, kind=kind, file=node.node_id,
                line=line, end_line=end_line, language=node.language, signature=signature,
                params=params, returns=returns, bases=bases, modifiers=modifiers,
                visibility=visibility, doc=doc, parent=parent_uid,
            )
            if visibility != "public" and not cfg.APIDOCS_INCLUDE_PRIVATE:
                if kind in CONTAINER_KINDS:
                    stack.append((entity, end_line))
                continue
            entities.append(entity)
            if parent_entity is None:
                module.members.append(uid)
            if kind in CONTAINER_KINDS:
                stack.append((entity, end_line))
        kept = {e.uid for e in entities}
        for entity in entities:
            if entity.parent not in kept and entity.parent != node.node_id:
                entity.parent = node.node_id
                module.members.append(entity.uid)
        return [module] + entities

    @staticmethod
    def _is_include_guard(name: str, kind: str, doc: str) -> bool:
        """Return True for undocumented C/C++ include-guard macros."""
        return kind == "macro" and not doc and bool(
            re.match(r"^_*[A-Z0-9_]+_(H|HH|HPP|HXX|H_|INCLUDED|DEFINED)_*$", name)
        )

    @staticmethod
    def _generic_visibility(
        name: str, decl: str, language: str, parent: Optional[ApiEntity]
    ) -> Tuple[str, List[str]]:
        """Infer visibility and modifiers from a declaration line."""
        words = set(re.findall(r"[A-Za-z_]+", decl.split("(")[0]))
        modifiers = sorted(w for w in words & {"static", "abstract", "virtual", "override", "async",
                                               "final", "const", "inline", "extern", "sealed",
                                               "suspend", "unsafe", "synchronized"})
        visibility = "public"
        if words & _PRIVATE_MODIFIERS:
            visibility = "private"
        elif "protected" in words:
            visibility = "protected"
        elif language == "go" and name[:1].islower():
            visibility = "private"
        elif language == "rs" and "pub" not in words and parent is None:
            visibility = "private"
        elif language in ("c", "cc", "cpp", "cxx", "C") and "static" in words and parent is None:
            visibility = "private"
        elif language in ("js", "jsx", "ts", "tsx", "dart", "rb", "lua", "ex", "exs") and name.startswith(("_", "#")):
            visibility = "private"
        elif language in ("ex", "exs") and re.match(r"^\s*defp\b", decl):
            visibility = "private"
        return visibility, modifiers

    @staticmethod
    def _generic_bases(signature: str, name: str) -> List[str]:
        """Extract base type names from a class-like declaration."""
        tail = signature.split(name, 1)[1] if name in signature else ""
        tail = re.sub(r"<[^<>]*>", "", tail)
        bases: List[str] = []
        for pattern in (r"\bextends\s+([\w.,\s]+?)(?:\bimplements\b|\{|$)",
                        r"\bimplements\s+([\w.,\s]+?)(?:\{|$)",
                        r"^\s*:\s*(?:public|private|protected)?\s*([\w.,:\s]+?)(?:\{|where|$)",
                        r"^\s*<\s*([\w.:]+)",
                        r"^\s*\(([\w.,\s]+)\)"):
            match = re.search(pattern, tail)
            if match:
                for part in match.group(1).split(","):
                    clean = re.sub(r"\b(public|private|protected|virtual)\b", "", part).strip()
                    clean = clean.split("(")[0].strip()
                    if clean and _IDENT_RE.match(clean) and clean not in bases:
                        bases.append(clean)
        return bases

    @staticmethod
    def _type_index(reference: ApiReference) -> Dict[str, List[ApiEntity]]:
        """Map simple and qualified type names to their entities."""
        index: Dict[str, List[ApiEntity]] = {}
        for entity in reference.entities.values():
            if entity.kind in CLASS_KINDS:
                for key in {entity.name, entity.qualname}:
                    index.setdefault(key, []).append(entity)
        return index

    def _link_inheritance(self, reference: ApiReference, edges: List[Edge]) -> None:
        """Resolve base names to project types and fill subclass lists."""
        index = self._type_index(reference)
        by_file_name: Dict[Tuple[str, str], ApiEntity] = {}
        for entity in reference.entities.values():
            if entity.kind in CLASS_KINDS:
                by_file_name.setdefault((entity.file, entity.name), entity)
        for edge in edges:
            if edge.relation != "inherits" or "::" not in edge.source:
                continue
            file_id, child = edge.source.split("::", 1)
            entity = by_file_name.get((file_id, child))
            base = edge.target.split(".")[-1]
            if entity is not None and base and base not in [b.split(".")[-1].split("[")[0] for b in entity.bases]:
                entity.bases.append(base)
        for entity in reference.entities.values():
            if entity.kind not in CLASS_KINDS:
                continue
            for base in entity.bases:
                key = re.sub(r"\[.*\]$", "", base).split(".")[-1].strip()
                candidates = [c for c in index.get(key, []) if c.uid != entity.uid]
                if not candidates:
                    continue
                same = [c for c in candidates if c.file == entity.file]
                target = (same or sorted(candidates, key=lambda c: c.uid))[0]
                if target.uid not in entity.base_uids:
                    entity.base_uids.append(target.uid)
                if entity.uid not in target.subclasses:
                    target.subclasses.append(entity.uid)
        for entity in reference.entities.values():
            entity.subclasses.sort()

    @staticmethod
    def _inherit_docs(reference: ApiReference) -> None:
        """Fill undocumented entities from their declaration or overridden base member.

        C-family definitions borrow the documentation of a same-named
        prototype in a header (Doxygen merges declaration and definition);
        undocumented overriding methods borrow the nearest documented
        base-class member of the same name (Sphinx ``autodoc_inherit_docstrings``).
        Borrowed docs keep their source in ``doc.notes``.
        """
        prototypes: Dict[str, ApiEntity] = {}
        for entity in reference.entities.values():
            if entity.language in _C_HEADER_LANGUAGES and entity.kind in CALLABLE_KINDS and entity.is_documented:
                prototypes.setdefault(entity.qualname, entity)
        for entity in reference.entities.values():
            if entity.is_documented or entity.kind not in CALLABLE_KINDS:
                continue
            source: Optional[ApiEntity] = None
            proto = prototypes.get(entity.qualname)
            if proto is not None and proto.uid != entity.uid:
                source = proto
            elif entity.parent in reference.entities:
                owner = reference.entities[entity.parent]
                queue = list(owner.base_uids)
                visited: Set[str] = set()
                while queue and source is None:
                    base_uid = queue.pop(0)
                    if base_uid in visited or base_uid not in reference.entities:
                        continue
                    visited.add(base_uid)
                    base = reference.entities[base_uid]
                    for member in reference.children(base_uid):
                        if member.name == entity.name and member.is_documented:
                            source = member
                            break
                    queue.extend(base.base_uids)
            if source is not None:
                borrowed = DocComment(**{k: v for k, v in vars(source.doc).items()})
                borrowed.notes = list(source.doc.notes) + [("Inherited", f"Documentation from `{source.qualname}` ({source.file}:{source.line}).")]
                entity.doc = borrowed

    def _link_calls(
        self,
        reference: ApiReference,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]],
        contents: Dict[str, str],
    ) -> None:
        """Attach resolved callers and callees to callable entities."""
        callables: Dict[str, List[ApiEntity]] = {}
        for entity in reference.entities.values():
            if entity.kind in CALLABLE_KINDS or entity.kind in CLASS_KINDS:
                callables.setdefault(entity.file, []).append(entity)
        if not callables:
            return
        for items in callables.values():
            items.sort(key=lambda e: (e.line, -(e.end_line or e.line)))
        language_of = {n.node_id: n.language for n in nodes}
        scoped_nodes = [
            Node(
                node_id=file_id, label=PurePosixPath(file_id).name, kind=KIND_MODULE,
                language=language_of.get(file_id, ""),
                symbols=[Symbol(e.name, e.kind, e.line) for e in items],
            )
            for file_id, items in sorted(callables.items())
        ]
        scoped_contents = {k: v for k, v in contents.items() if k in callables}
        try:
            resolved = SymbolIndex(self._config).resolve(scoped_nodes, edges, resolved_edges, scoped_contents)
        except (ValueError, RecursionError):
            return

        def innermost(file_id: str, line: int, name: str) -> Optional[ApiEntity]:
            """Return the narrowest callable in *file_id* spanning *line*."""
            best: Optional[ApiEntity] = None
            for entity in callables.get(file_id, []):
                end = entity.end_line or entity.line
                if line and entity.line <= line <= end and entity.kind in CALLABLE_KINDS:
                    if best is None or entity.line >= best.line:
                        best = entity
                elif not line and entity.name == name and best is None:
                    best = entity
            return best

        def target_entity(file_id: str, line: int, name: str) -> Optional[ApiEntity]:
            """Return the entity defined at *line* in *file_id* (or by name)."""
            for entity in callables.get(file_id, []):
                if entity.line == line and entity.name == name:
                    return entity
            for entity in callables.get(file_id, []):
                if entity.name == name:
                    return entity
            return None

        types = PythonReceiverTypes(scoped_contents, language_of)
        for call in resolved:
            site = call.site
            if call.confidence == "BUILTIN":
                continue
            caller = innermost(site.file, site.line, site.caller)
            if caller is None:
                continue
            typed = types.resolve_method(site.file, site.line, site.receiver, site.callee) if site.receiver else None
            if typed is not None:
                callee = target_entity(typed[0], typed[1], site.callee)
            else:
                if call.confidence in ("UNRESOLVED", "AMBIGUOUS", "EXTERNAL"):
                    continue
                callee = target_entity(call.target_file, call.target_line, site.callee)
                if callee is None:
                    continue
                verdict = types.accepts(site.file, site.line, site.receiver, callee.file, callee.line, callee.name)
                if verdict is False:
                    continue
                if verdict is None and not self._receiver_plausible(reference, site.receiver, caller, callee, call.confidence):
                    continue
            if callee is None or caller.uid == callee.uid:
                continue
            if callee.kind in CLASS_KINDS:
                ctor = next(
                    (reference.entities[m] for m in callee.members
                     if m in reference.entities and reference.entities[m].kind == "constructor"),
                    None,
                )
                callee = ctor or callee
            if callee.uid not in caller.calls:
                caller.calls.append(callee.uid)
            if caller.uid not in callee.called_by:
                callee.called_by.append(caller.uid)
        for entity in reference.entities.values():
            entity.calls.sort()
            entity.called_by.sort()

    @staticmethod
    def _owner_chain(reference: ApiReference, entity: ApiEntity) -> Set[str]:
        """Return the enclosing type of *entity* plus all its project base types."""
        owners: Set[str] = set()
        start = reference.entities.get(entity.parent)
        queue = [start.uid] if start is not None and start.kind in CLASS_KINDS else []
        while queue:
            uid = queue.pop()
            if uid in owners or uid not in reference.entities:
                continue
            owners.add(uid)
            queue.extend(reference.entities[uid].base_uids)
        return owners

    def _receiver_plausible(
        self, reference: ApiReference, receiver: str, caller: ApiEntity,
        callee: ApiEntity, confidence: str,
    ) -> bool:
        """Decide whether an attribute call can really target *callee*.

        Plain calls keep the symbol-index tier. Attribute calls are kept
        only when the receiver is ``self`` / ``this`` / ``cls`` / ``super()``
        and the callee belongs to the caller's type chain, when the
        receiver names the callee's type or module, or when the callee is
        a module-level function in an imported file. Everything else
        (``obj.search()`` resolved purely by a unique name) is dropped, so
        call graphs never claim edges the source cannot prove.
        """
        if not receiver:
            return True
        head = receiver.split(".")[0].split("(")[0]
        callee_owner = reference.entities.get(callee.parent)
        if head in ("self", "this", "cls", "super", "base", "Self", "static", "parent"):
            if callee_owner is None or callee_owner.kind not in CLASS_KINDS:
                return False
            return callee_owner.uid in self._owner_chain(reference, caller)
        last = receiver.split(".")[-1].rstrip("()")
        if callee_owner is not None and callee_owner.kind in CLASS_KINDS:
            return last == callee_owner.name
        module_stem = PurePosixPath(callee.file).stem
        if last in (module_stem, module_stem.lstrip("_")):
            return True
        return False

    def _lint(self, reference: ApiReference) -> List[DocWarning]:
        """Produce Doxygen-style documentation warnings."""
        found: List[DocWarning] = []
        for entity in reference.entities.values():
            if entity.visibility != "public":
                continue
            if not entity.is_documented:
                if entity.kind == "constructor" and entity.parent in reference.entities and reference.entities[entity.parent].is_documented:
                    continue
                if entity.kind in DATA_KINDS:
                    continue
                found.append(DocWarning(
                    WARN_UNDOCUMENTED, entity.uid, entity.file, entity.line,
                    f"{entity.kind} {entity.qualname} is not documented",
                ))
                continue
            if entity.kind not in CALLABLE_KINDS or entity.kind == "property":
                continue
            doc = entity.doc
            names = [p.name for p in entity.params if p.name]
            plain = {n.lstrip("*$&") for n in names}
            if doc.params:
                missing = [n for n in names if doc.param(n) is None and n.lstrip("*") not in ("args", "kwargs")]
                for name in missing:
                    found.append(DocWarning(
                        WARN_PARAM_MISSING, entity.uid, entity.file, entity.line,
                        f"parameter '{name}' of {entity.qualname} is not documented",
                    ))
                if names:
                    for item in doc.params:
                        if item.name and item.name.lstrip("*$&") not in plain:
                            found.append(DocWarning(
                                WARN_PARAM_UNKNOWN, entity.uid, entity.file, entity.line,
                                f"documented parameter '{item.name}' is not in the signature of {entity.qualname}",
                            ))
            structured = bool(doc.params or doc.returns or doc.raises)
            returns_something = entity.returns_value is True or (
                entity.returns_value is None and entity.returns.strip() not in _VOID_RETURNS
            )
            if entity.kind == "constructor" or entity.returns.strip() in ("None", "NoReturn"):
                returns_something = False
            if structured and returns_something and doc.returns is None and doc.yields is None:
                found.append(DocWarning(
                    WARN_RETURN_MISSING, entity.uid, entity.file, entity.line,
                    f"return value of {entity.qualname} is not documented",
                ))
            if structured and entity.inferred_raises:
                documented = {r.name.split(".")[-1] for r in doc.raises}
                for name in entity.inferred_raises:
                    if name not in documented:
                        found.append(DocWarning(
                            WARN_RAISE_MISSING, entity.uid, entity.file, entity.line,
                            f"{entity.qualname} raises {name} but does not document it",
                        ))
        found.sort(key=lambda w: (w.file, w.line, w.code, w.message))
        return found

    @staticmethod
    def _coverage(reference: ApiReference) -> Dict[str, object]:
        """Compute documentation coverage overall, per kind, and per module."""

        def counts(items: List[ApiEntity]) -> Dict[str, object]:
            """Return documented/total/percent for *items*."""
            total = len(items)
            done = sum(1 for e in items if e.is_documented)
            percent = round(100.0 * done / total, 1) if total else 100.0
            return {"documented": done, "total": total, "percent": percent}

        public = [
            e for e in reference.entities.values()
            if e.visibility == "public" and e.kind not in DATA_KINDS
        ]
        per_kind: Dict[str, List[ApiEntity]] = {}
        per_module: Dict[str, List[ApiEntity]] = {}
        for entity in public:
            per_kind.setdefault(entity.kind, []).append(entity)
            per_module.setdefault(entity.file, []).append(entity)
        return {
            "overall": counts(public),
            "by_kind": {k: counts(v) for k, v in sorted(per_kind.items())},
            "by_module": {k: counts(v) for k, v in sorted(per_module.items())},
        }
