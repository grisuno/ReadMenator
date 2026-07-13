"""Language parsers for code symbol extraction.

Implements the Strategy pattern with a common LanguageParser base,
13 concrete subclasses (one per supported language), and a factory
function ``create_parser`` that maps file extensions to parser classes.

Python uses the native ``ast`` module; all other languages rely on
regex-based heuristics tuned to each language's grammar.
"""

from __future__ import annotations

import ast
import re
import warnings
from typing import Dict, List, Optional, Tuple, Type

from readmenator._config import Config
from readmenator._models import Symbol


class LanguageParser:
    """Base class for all language-specific parsers.

    Subclasses must implement ``_extract_specifics`` to populate
    ``self.symbols`` and ``self.imports``. Common utility methods
    ``_extract_docstring`` and ``_extract_signature`` are provided
    for reuse across all parsers.
    """

    def __init__(self, filename: str, config: Config) -> None:
        """Initialise the parser with a file path and application config.

        Args:
            filename: Relative or absolute path of the source file.
            config: Application-wide configuration settings.
        """
        self.filename = filename
        self.config = config
        self.symbols: List[Symbol] = []
        self.imports: List[str] = []
        self.calls: List[Tuple[str, str]] = []
        self.inherits: List[Tuple[str, str]] = []
        self.lines: List[str] = []

    def parse(self, content: str) -> None:
        """Parse *content* and populate symbol/import lists.

        Splits the source into lines, then delegates to the subclass-
        specific ``_extract_specifics`` logic.
        """
        self.lines = content.split("\n")
        self._extract_specifics(content)

    def _extract_specifics(self, content: str) -> None:
        """Subclass hook for language-specific symbol extraction."""
        raise NotImplementedError

    def _extract_docstring(self, line_num: int) -> str:
        """Walk backwards from *line_num* to collect preceding comments/docstrings.

        Supports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``
        comment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``
        from Config.
        """
        if line_num >= len(self.lines):
            return ""
        doc_lines: List[str] = []
        in_block_comment = False
        max_lookback = self.config.DOCSTRING_LOOKBACK_LINES
        for i in range(line_num - 1, max(-1, line_num - max_lookback), -1):
            line = self.lines[i].strip()
            if not line:
                if not in_block_comment:
                    break
                continue
            if line.endswith("*/"):
                in_block_comment = True
                doc_lines.insert(0, line.rstrip("*/").strip())
                continue
            if in_block_comment:
                cleaned = line.lstrip("/*").lstrip("*").strip()
                doc_lines.insert(0, cleaned)
                if line.startswith("/*") or line.startswith("/**"):
                    break
                continue
            if line.startswith("///") or line.startswith("//!"):
                doc_lines.insert(0, line[3:].strip())
            elif line.startswith("//"):
                doc_lines.insert(0, line[2:].strip())
            elif line.startswith("#") and not line.startswith("#!"):
                doc_lines.insert(0, line[1:].strip())
            elif line == "":
                continue
            else:
                break
        doc = " ".join(doc_lines).strip()
        doc = re.sub(r"^[\-\*\+]\s*", "", doc)
        return doc

    def _extract_signature(self, content: str, match_start: int, pattern: str) -> str:
        """Extract a compact signature snippet starting at *match_start*.

        Scans forward to the opening brace or a fallback length,
        then truncates to 100 characters for display.
        """
        start = match_start
        end = content.find("{", start)
        if end == -1:
            end = start + 120
        raw = content[start:end].strip()
        if len(raw) > 100:
            raw = raw[:97] + "..."
        return raw


class CParser(LanguageParser):
    """Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).

    Extracts includes, structs, classes, functions, and preprocessor
    macros using regex heuristics tuned to C-family syntax.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r'^\s*#\s*include\s*[<"]([^>"]+)[>"]', content, re.MULTILINE
        ):
            self.imports.append(m.group(1))

        for m in re.finditer(r"\b(?:typedef\s+)?struct\s+(\w+)\s*(?:\{|;)", content):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )

        for m in re.finditer(
            r"\bclass\s+(\w+)(?:\s*:\s*(?:public|private|protected)\s+(\w+))?\s*\{",
            content,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )

        func_pattern = (
            r"^[\w\s\*&:<>]+?\b([a-zA-Z_]\w*)\s*\([^;{]*\)\s*(?:const)?\s*(?:override)?\s*\{"
        )
        for m in re.finditer(func_pattern, content, re.MULTILINE):
            name = m.group(1)
            if name in (
                "if",
                "for",
                "while",
                "switch",
                "catch",
                "return",
                "sizeof",
                "typedef",
            ):
                continue
            preceding = content[max(0, m.start() - 200) : m.start()]
            if "/*" in preceding and "*/" not in preceding.split("/*")[-1]:
                continue
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                    signature=self._extract_signature(content, m.start(), func_pattern),
                )
            )

        for m in re.finditer(r'^\s*#\s*define\s+(\w+)', content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(name=m.group(1), kind="macro", line=line_num + 1)
            )


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


class GoParser(LanguageParser):
    """Parser for Go (.go).

    Extracts import blocks or single import statements, exported
    functions (including methods), and type definitions (struct/interface).
    """

    def _extract_specifics(self, content: str) -> None:
        block = re.search(r"import\s*\((.*?)\)", content, re.DOTALL)
        if block:
            for m in re.finditer(r'"([^"]+)"', block.group(1)):
                self.imports.append(m.group(1))
        else:
            for m in re.finditer(r'import\s+"([^"]+)"', content):
                self.imports.append(m.group(1))
        for m in re.finditer(
            r"^func\s+(?:\([^)]+\)\s+)?(\w+)\s*\(", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                    signature=m.group(0).strip(),
                )
            )
        for m in re.finditer(
            r"^type\s+(\w+)\s+(struct|interface)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind=m.group(2),
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class RustParser(LanguageParser):
    """Parser for Rust (.rs).

    Extracts ``use`` imports, public and private functions,
    structs, traits, and enums.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^use\s+([\w:]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^(?:pub\s+)?(?:async\s+)?fn\s+(\w+)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^(?:pub\s+)?struct\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^(?:pub\s+)?trait\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="trait",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^(?:pub\s+)?enum\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="enum",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class JavaScriptParser(LanguageParser):
    """Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).

    Extracts ES module imports, CommonJS ``require`` calls, function
    declarations, arrow-function variables, and class definitions
    (including inheritance).
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"""import\s+(?:\{[^}]*\}\s+from\s+)?['"]([^'"]+)['"]""", content
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"""require\s*\(['"]([^'"]+)['"]\)""", content
        ):
            self.imports.append(m.group(1))
        patterns = [
            r"(?:^|\s)function\s+(\w+)",
            r"(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(",
            r"(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?function",
        ]
        reserved = {"if", "for", "while", "switch", "catch"}
        for pattern in patterns:
            for m in re.finditer(pattern, content):
                name = m.group(1)
                if name not in reserved:
                    line_num = content[: m.start()].count("\n")
                    self.symbols.append(
                        Symbol(
                            name=name,
                            kind="function",
                            line=line_num + 1,
                            doc=self._extract_docstring(line_num),
                        )
                    )
        for m in re.finditer(
            r"class\s+(\w+)(?:\s+extends\s+(\w+))?", content
        ):
            name = m.group(1)
            parent = m.group(2)
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
            if parent:
                self.inherits.append((name, parent))
        for m in re.finditer(r"(\w+)\s*\([^)]*\)\s*(?:;|{)?", content):
            callee = m.group(1)
            if callee and callee[0].isupper() is False and callee not in reserved:
                if len(callee) >= 3 and callee not in {"var", "let", "const", "new", "true", "false", "null"}:
                    self.calls.append(("", callee))


class JavaParser(LanguageParser):
    """Parser for Java (.java).

    Extracts import statements, class and interface declarations,
    and methods complete with access modifiers and type signatures.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+([\w.]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"(?:public|private|protected)?\s*(?:abstract\s+)?(?:class|interface)\s+(\w+)",
            content,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        method_pattern = r"(?:public|private|protected)?\s*(?:static\s+)?(?:[\w<>\[\]]+\s+)+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{"
        reserved = {"if", "for", "while", "switch", "catch"}
        for m in re.finditer(method_pattern, content):
            name = m.group(1)
            if name not in reserved:
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="method",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class CSharpParser(LanguageParser):
    """Parser for C# (.cs).

    Extracts ``using`` directives, class/struct/interface/record
    declarations, and methods with access modifiers.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^using\s+([\w.]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"(?:public|private|protected|internal)?\s*(?:static\s+)?(?:class|struct|interface|record)\s+(\w+)",
            content,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        method_pattern = r"(?:public|private|protected|internal)?\s*(?:static\s+)?(?:virtual\s+)?(?:override\s+)?(?:async\s+)?(?:[\w<>\[\]]+\s+)+(\w+)\s*\([^)]*\)\s*\{"
        reserved = {"if", "for", "while", "switch", "catch"}
        for m in re.finditer(method_pattern, content):
            name = m.group(1)
            if name not in reserved:
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="method",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class ShellParser(LanguageParser):
    """Parser for shell scripts (.sh, .bash, .zsh).

    Extracts function declarations in both POSIX (``name() {``)
    and ``function`` keyword syntax.
    """

    def _extract_specifics(self, content: str) -> None:
        patterns = [
            r"^(\w+)\s*\(\)\s*\{",
            r"^function\s+(\w+)\s*(?:\(\))?\s*\{",
        ]
        for pattern in patterns:
            for m in re.finditer(pattern, content, re.MULTILINE):
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=m.group(1),
                        kind="function",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class PHPParser(LanguageParser):
    """Parser for PHP (.php).

    Extracts ``use/require/include`` (including ``_once`` variants),
    function declarations, and class declarations.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"(?:use|require|include)(?:_once)?\s+['\"]?([^'\";\s]+)", content
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(r"function\s+(\w+)\s*\(", content):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"class\s+(\w+)", content):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class DartParser(LanguageParser):
    """Parser for Dart (.dart).

    Extracts import statements, class declarations (with extends),
    and top-level or method function declarations by return type.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"""import\s+['"]([^'"]+)['"]""", content):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"class\s+(\w+)(?:\s+extends\s+(\w+))?", content
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"(?:void|int|String|bool|dynamic|Future|[\w<>]+)\s+(\w+)\s*\(", content
        ):
            name = m.group(1)
            if name not in ("if", "for", "while", "switch"):
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="function",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class GDScriptParser(LanguageParser):
    """Parser for Godot GDScript (.gd).

    Extracts ``extends`` / ``class_name`` directives and ``func``
    method declarations.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"^(?:extends|class_name)\s+(\w+)", content, re.MULTILINE
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(r"^func\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class NimParser(LanguageParser):
    """Parser for Nim (.nim).

    Extracts ``import`` statements, ``proc`` / ``func`` / ``method``
    declarations, and ``type`` definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+([\w,/ ]+)", content, re.MULTILINE):
            self.imports.extend(x.strip() for x in m.group(1).split(","))
        for m in re.finditer(
            r"^(?:proc|func|method)\s+(\w+)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^type\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class AssemblyParser(LanguageParser):
    """Parser for assembly (.asm, .s, .S).

    Extracts labels at the start of a line (``label:``) as function
    symbols. This is a best-effort heuristic; local labels and
    directives are not always distinguishable.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^([a-zA-Z_]\w*):", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class RubyParser(LanguageParser):
    """Parser for Ruby (.rb).

    Extracts ``require`` / ``require_relative`` imports, class and
    module definitions with inheritance, and method definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"""(?:require|require_relative)\s+['"]([^'"]+)['"]""", content
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*class\s+(\w+)(?:\s*<\s*(\w+))?", content, re.MULTILINE
        ):
            name = m.group(1)
            parent = m.group(2)
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
            if parent:
                self.inherits.append((name, parent))
        for m in re.finditer(
            r"^\s*module\s+(\w+)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="module",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^\s*def\s+(self\.)?(\w+)", content, re.MULTILINE
        ):
            name = m.group(2)
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="method",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class SwiftParser(LanguageParser):
    """Parser for Swift (.swift).

    Extracts ``import`` statements, class/struct/enum/protocol
    declarations with inheritance, and function definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+(\w+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*(?:public|private|internal|fileprivate\s+)?"
            r"(?:final\s+)?class\s+(\w+)(?:\s*:\s*(\w+))?",
            content,
            re.MULTILINE,
        ):
            name = m.group(1)
            parent = m.group(2)
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
            if parent:
                self.inherits.append((name, parent))
        for m in re.finditer(
            r"^\s*(?:public|private|internal\s+)?(?:struct|enum)\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind=m.group(2) if "group" in str(m) else "struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^\s*(?:public|private|internal\s+)?protocol\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="protocol",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^\s*(?:public|private|internal\s+)?"
            r"(?:override\s+)?(?:class\s+)?func\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


class KotlinParser(LanguageParser):
    """Parser for Kotlin (.kt, .kts).

    Extracts ``import`` statements, class/object/interface/data class
    declarations, and function definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+([\w.]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*(?:open\s+)?(?:abstract\s+)?(?:data\s+)?(?:sealed\s+)?"
            r"(?:inner\s+)?class\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^\s*(?:abstract\s+)?(?:sealed\s+)?interface\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="interface",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^\s*(?:object|companion object)\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        reserved = {"if", "for", "while", "when", "catch", "try"}
        for m in re.finditer(
            r"^\s*(?:suspend\s+)?(?:inline\s+)?(?:tailrec\s+)?"
            r"fun\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            name = m.group(1)
            if name not in reserved:
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="function",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class ScalaParser(LanguageParser):
    """Parser for Scala (.scala).

    Extracts ``import`` statements, class/object/trait declarations,
    and method definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+([\w.]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*(?:abstract\s+)?(?:sealed\s+)?(?:case\s+)?"
            r"class\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^\s*(?:sealed\s+)?trait\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="trait",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^\s*object\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        reserved = {"if", "for", "while", "match", "case", "try", "catch"}
        for m in re.finditer(
            r"^\s*(?:private|protected\s+)?(?:override\s+)?"
            r"def\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            name = m.group(1)
            if name not in reserved:
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="method",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class LuaParser(LanguageParser):
    """Parser for Lua (.lua).

    Extracts ``require`` imports, function declarations (named and
    table-based), and module returns.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"""require\s*\(?\s*['"]([^'"]+)['"]""", content):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^local\s+function\s+(\w+)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^function\s+(\w+)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^(?:local\s+)?(\w+)\s*=\s*\{", content, re.MULTILINE
        ):
            name = m.group(1)
            if name not in ("if", "for", "while", "do", "repeat"):
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="struct",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


class ElixirParser(LanguageParser):
    """Parser for Elixir (.ex, .exs).

    Extracts ``import``/``alias``/``require``/``use`` directives,
    module definitions, and named function definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"^\s*(?:import|alias|require|use)\s+([\w.{}]+)",
            content,
            re.MULTILINE,
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*defmodule\s+([\w.]+)", content, re.MULTILINE
        ):
            name = m.group(1).split(".")[-1]
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="module",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^\s*def(?:macro)?(?:p)?\s+(when\s+.*?\bdo\b\s*)?(\w+)",
            content,
            re.MULTILINE,
        ):
            name = m.group(2) if m.group(2) else m.group(1)
            if name and name not in ("if", "unless", "case", "cond", "with", "for", "try", "receive"):
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="function",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


_PARSER_MAP: Dict[str, Type[LanguageParser]] = {
    ".c": CParser,
    ".cpp": CParser,
    ".cc": CParser,
    ".cxx": CParser,
    ".h": CParser,
    ".hpp": CParser,
    ".hxx": CParser,
    ".py": PythonParser,
    ".go": GoParser,
    ".rs": RustParser,
    ".js": JavaScriptParser,
    ".ts": JavaScriptParser,
    ".jsx": JavaScriptParser,
    ".tsx": JavaScriptParser,
    ".java": JavaParser,
    ".cs": CSharpParser,
    ".sh": ShellParser,
    ".bash": ShellParser,
    ".zsh": ShellParser,
    ".php": PHPParser,
    ".dart": DartParser,
    ".gd": GDScriptParser,
    ".nim": NimParser,
    ".asm": AssemblyParser,
    ".s": AssemblyParser,
    ".S": AssemblyParser,
    ".rb": RubyParser,
    ".swift": SwiftParser,
    ".kt": KotlinParser,
    ".kts": KotlinParser,
    ".scala": ScalaParser,
    ".sc": ScalaParser,
    ".lua": LuaParser,
    ".ex": ElixirParser,
    ".exs": ElixirParser,
}


def create_parser(
    extension: str, filename: str, config: Config
) -> Optional[LanguageParser]:
    """Factory: return a parser instance for *extension* or ``None``.

    Looks up the extension in ``_PARSER_MAP`` (case-insensitive).
    Returns ``None`` for unsupported extensions so the caller can
    silently skip unknown file types.
    """
    parser_class = _PARSER_MAP.get(extension.lower())
    if parser_class is not None:
        return parser_class(filename, config)
    return None
