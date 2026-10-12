"""Lightweight, deterministic receiver typing for Python attribute calls.

Resolving ``obj.method()`` by method name alone invents edges whenever
two classes share a method name. This module recovers just enough type
information from the ``ast`` to decide which class a receiver holds:

* method ownership (which class defines the function at a given line),
* local variables assigned from a project class constructor or
  annotated with a project class (``app = App()``, ``app: App``,
  parameters ``def f(app: App)``),
* instance attributes assigned or annotated in any method
  (``self.engine = Engine()``, ``self.engine: Engine``),
* class-level annotated fields (dataclass style), and
* ``self`` / ``cls`` / ``super()`` and bare class names.

No inference across returns or containers is attempted: unknown stays
unknown, so callers can stay conservative.
"""

from __future__ import annotations

import ast
import warnings
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

_SELF_NAMES: Set[str] = {"self", "cls", "super()", "super"}


@dataclass
class _Scope:
    """One function scope with its span, owner class, and local types."""

    name: str
    start: int
    end: int
    owner: str = ""
    locals: Dict[str, str] = field(default_factory=dict)


def _annotation_name(node: Optional[ast.expr]) -> str:
    """Return the class name an annotation refers to (unwrapping Optional/quotes)."""
    if node is None:
        return ""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value.split("[")[0].split(".")[-1].strip()
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Subscript):
        outer = _annotation_name(node.value)
        if outer in ("Optional", "Final", "ClassVar", "Annotated"):
            inner = node.slice
            if isinstance(inner, ast.Tuple) and inner.elts:
                inner = inner.elts[0]
            return _annotation_name(inner)
        return ""
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        left, right = _annotation_name(node.left), _annotation_name(node.right)
        if right in ("None", "") :
            return left
        if left in ("None", ""):
            return right
    return ""


def _constructed(node: Optional[ast.expr]) -> str:
    """Return the class name when *node* is ``Name(...)`` or ``mod.Name(...)``."""
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            return node.func.id
        if isinstance(node.func, ast.Attribute):
            return node.func.attr
    return ""


class PythonReceiverTypes:
    """Per-project receiver type index for Python sources."""

    def __init__(self, contents: Dict[str, str], language: Dict[str, str]) -> None:
        """Index every Python file in *contents*.

        Args:
            contents: File id to source text.
            language: File id to scanner language label.
        """
        self._scopes: Dict[str, List[_Scope]] = {}
        self._attrs: Dict[str, Dict[str, str]] = {}
        self._owner: Dict[Tuple[str, int], str] = {}
        self._classes: Set[str] = set()
        self._bases: Dict[str, List[str]] = {}
        self._files: Set[str] = set()
        self._methods: Dict[Tuple[str, str], Tuple[str, int]] = {}
        trees: Dict[str, ast.Module] = {}
        for file_id in sorted(contents):
            if language.get(file_id) != "py":
                continue
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                try:
                    trees[file_id] = ast.parse(contents[file_id])
                except (SyntaxError, ValueError, RecursionError):
                    continue
            self._files.add(file_id)
            for node in ast.walk(trees[file_id]):
                if isinstance(node, ast.ClassDef):
                    self._classes.add(node.name)
                    bases = self._bases.setdefault(node.name, [])
                    for base in node.bases:
                        name = _annotation_name(base)
                        if name and name not in bases:
                            bases.append(name)
        for file_id, tree in trees.items():
            self._index_file(file_id, tree)

    @property
    def classes(self) -> Set[str]:
        """Return every project class name seen."""
        return set(self._classes)

    def _index_file(self, file_id: str, tree: ast.Module) -> None:
        """Collect scopes, ownership, locals, and attribute types for one file."""
        scopes: List[_Scope] = []

        def visit(body: List[ast.stmt], owner: str) -> None:
            """Walk class and function bodies recording scopes."""
            for stmt in body:
                if isinstance(stmt, ast.ClassDef):
                    attrs = self._attrs.setdefault(stmt.name, {})
                    for item in stmt.body:
                        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                            kind = _annotation_name(item.annotation)
                            if kind in self._classes:
                                attrs.setdefault(item.target.id, kind)
                    visit(stmt.body, stmt.name)
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    end = getattr(stmt, "end_lineno", stmt.lineno) or stmt.lineno
                    scope = _Scope(stmt.name, stmt.lineno, end, owner)
                    if owner:
                        self._owner[(file_id, stmt.lineno)] = owner
                        self._methods.setdefault((owner, stmt.name), (file_id, stmt.lineno))
                    args = list(stmt.args.posonlyargs) + list(stmt.args.args) + list(stmt.args.kwonlyargs)
                    for arg in args:
                        kind = _annotation_name(arg.annotation)
                        if kind in self._classes:
                            scope.locals[arg.arg] = kind
                    for node in ast.walk(stmt):
                        self._record_assignment(node, scope)
                    scopes.append(scope)
                    visit(stmt.body, owner)

        visit(tree.body, "")
        self._scopes[file_id] = scopes

    def _record_assignment(self, node: ast.AST, scope: _Scope) -> None:
        """Record local and ``self.attr`` types from one assignment node."""
        targets: List[ast.expr] = []
        kind = ""
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
            kind = _constructed(node.value)
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
            kind = _annotation_name(node.annotation) or _constructed(node.value)
        if kind not in self._classes:
            return
        for target in targets:
            if isinstance(target, ast.Name):
                scope.locals.setdefault(target.id, kind)
            elif (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and scope.owner
            ):
                self._attrs.setdefault(scope.owner, {}).setdefault(target.attr, kind)

    def scope_at(self, file_id: str, line: int) -> Optional[_Scope]:
        """Return the innermost function scope spanning *line*."""
        best: Optional[_Scope] = None
        for scope in self._scopes.get(file_id, []):
            if scope.start <= line <= scope.end and (best is None or scope.start >= best.start):
                best = scope
        return best

    def owner_of(self, file_id: str, line: int) -> str:
        """Return the class that defines the function starting at *line* ("" if none)."""
        return self._owner.get((file_id, line), "")

    def receiver_class(self, file_id: str, line: int, receiver: str) -> str:
        """Return the project class a receiver expression holds at a call site.

        Args:
            file_id: Caller file.
            line: Call line.
            receiver: Receiver text from the call site (``self``, ``app``,
                ``self.engine``, ``Engine()``, ``Engine``).

        Returns:
            Class name, or "" when it cannot be proven.
        """
        if not receiver:
            return ""
        scope = self.scope_at(file_id, line)
        owner = scope.owner if scope else ""
        parts = receiver.split(".")
        head = parts[0]
        if head in _SELF_NAMES:
            current = owner
            for attr in parts[1:]:
                current = self._attrs.get(current, {}).get(attr.rstrip("()"), "")
                if not current:
                    return ""
            return current
        if len(parts) == 1:
            bare = head.rstrip("()")
            if bare in self._classes:
                return bare
            if scope is not None:
                return scope.locals.get(head, "")
            return ""
        if scope is not None and head in scope.locals:
            current = scope.locals[head]
            for attr in parts[1:]:
                current = self._attrs.get(current, {}).get(attr.rstrip("()"), "")
                if not current:
                    return ""
            return current
        tail = parts[-1].rstrip("()")
        return tail if tail in self._classes and not receiver.endswith("()") else ""

    def lineage(self, class_name: str) -> Set[str]:
        """Return *class_name* plus every project base class it derives from."""
        seen: Set[str] = set()
        todo = [class_name]
        while todo:
            current = todo.pop()
            if not current or current in seen:
                continue
            seen.add(current)
            todo.extend(self._bases.get(current, []))
        return seen

    def resolve_method(self, file_id: str, line: int, receiver: str, name: str) -> Optional[Tuple[str, int]]:
        """Return the (file, line) of the method a typed receiver dispatches to.

        Walks the receiver class lineage in base order; returns None when
        the receiver type is unknown or no project class in the lineage
        defines *name*.
        """
        holder = self.receiver_class(file_id, line, receiver)
        if not holder:
            return None
        order: List[str] = []
        todo = [holder]
        while todo:
            current = todo.pop(0)
            if current in order:
                continue
            order.append(current)
            todo.extend(self._bases.get(current, []))
        for cls in order:
            found = self._methods.get((cls, name))
            if found is not None:
                return found
        return None

    def accepts(
        self, file_id: str, line: int, receiver: str,
        target_file: str, target_line: int, target_name: str,
    ) -> Optional[bool]:
        """Decide whether a Python attribute call can target a definition.

        Args:
            file_id: Caller file.
            line: Call line.
            receiver: Receiver text ("" for plain calls).
            target_file: Candidate definition file.
            target_line: Candidate definition line.
            target_name: Candidate definition name.

        Returns:
            True or False for Python callers, None when the caller is not
            an indexed Python file (callers then fall back to their own rules).
        """
        if file_id not in self._files:
            return None
        if not receiver:
            return True
        owner = self.owner_of(target_file, target_line)
        holder = self.receiver_class(file_id, line, receiver)
        if owner:
            return bool(holder) and owner in self.lineage(holder)
        if holder:
            return holder == target_name
        stem = target_file.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        if stem == "__init__":
            parts = target_file.rsplit("/", 2)
            stem = parts[-2] if len(parts) >= 2 else stem
        tail = receiver.split(".")[-1].rstrip("()")
        return tail.strip("_") == stem.strip("_")

    def is_self_receiver(self, receiver: str) -> bool:
        """Return True for ``self``, ``cls``, and ``super()`` receivers."""
        return receiver in _SELF_NAMES
