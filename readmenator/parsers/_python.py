from __future__ import annotations

import ast
import warnings

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol


class PythonParser(LanguageParser):
    """Parser for Python (.py) using the native ``ast`` module.

    Extracts imports, functions (including async), and class
    definitions with docstrings via ``ast.get_docstring``.
    """

    def _extract_specifics(self, content: str) -> None:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            warnings.simplefilter("ignore", DeprecationWarning)
            try:
                tree = ast.parse(content, filename=self.filename)
            except SyntaxError:
                return
        current_class: Optional[str] = None
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.imports.append(alias.name)
                else:
                    if node.module:
                        self.imports.append(node.module)
            elif isinstance(node, ast.ClassDef):
                current_class = node.name
                bases = []
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        base_name = base.id
                        bases.append(base_name)
                        self.inherits.append((node.name, base_name))
                    elif isinstance(base, ast.Attribute):
                        base_name = base.attr if hasattr(base, 'attr') else str(base)
                        bases.append(base_name)
                        self.inherits.append((node.name, base_name))
                sig = f"class {node.name}({', '.join(bases)})" if bases else f"class {node.name}"
                self.symbols.append(
                    Symbol(
                        name=node.name,
                        kind="class",
                        line=node.lineno,
                        doc=ast.get_docstring(node) or "",
                        signature=sig,
                    )
                )
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                params = ", ".join(
                    arg.arg for arg in node.args.args
                )
                sig = f"def {node.name}({params})"
                kind = "method" if current_class else "function"
                self.symbols.append(
                    Symbol(
                        name=node.name,
                        kind=kind,
                        line=node.lineno,
                        doc=ast.get_docstring(node) or "",
                        signature=sig,
                    )
                )
                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        caller = node.name
                        if isinstance(child.func, ast.Name):
                            callee = child.func.id
                            self.calls.append((caller, callee))
                        elif isinstance(child.func, ast.Attribute):
                            callee = child.func.attr if hasattr(child.func, 'attr') else str(child.func)
                            self.calls.append((caller, callee))
            elif isinstance(node, ast.Call) and isinstance(node, ast.AST):
                pass


