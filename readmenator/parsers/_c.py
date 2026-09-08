from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class CParser(LanguageParser):
    """Parser for C, C++ (.c, .cpp, .cc, .cxx, .h, .hpp, .hxx).

    Extracts includes, structs, classes, functions, and preprocessor
    macros using regex heuristics tuned to C-family syntax.
    """

    def _extract_specifics(self, content: str) -> None:
        """Extract C-family symbols and imports from source content.

        Collects includes (quoted vs system), structs, classes, enums,
        unions, typedefs, functions (definitions and prototypes), extern
        declarations, globals, and macros.
        """
        lines = content.split("\n")
        in_block_comment = False
        active_code_lines: list[str] = []
        for raw in lines:
            code = raw
            if in_block_comment:
                end = code.find("*/")
                if end < 0:
                    active_code_lines.append("")
                    continue
                code = code[end + 2 :]
                in_block_comment = False
            while "/*" in code:
                start = code.find("/*")
                end = code.find("*/", start + 2)
                if end < 0:
                    code = code[:start]
                    in_block_comment = True
                    break
                code = code[:start] + code[end + 2 :]
            stripped = code.split("//")[0]
            active_code_lines.append(stripped)
        active = "\n".join(active_code_lines)
        in_if0 = False
        for raw_line in active.split("\n"):
            s = raw_line.strip()
            if s.startswith("#"):
                if s.startswith("#if 0") or s.startswith("#if\t0"):
                    in_if0 = True
                    continue
                if s.startswith("#endif"):
                    in_if0 = False
                    continue
                if in_if0:
                    continue
                m = re.match(r'#\s*(?:include|include_next|import)\s*[<"]([^>"]+)[>"]', s)
                if m:
                    header = m.group(1).strip()
                    if header not in self.imports:
                        self.imports.append(header)
                    continue

        for m in re.finditer(
            r'^\s*#\s*include\s*[<"]([^>"]+)[>"]', content, re.MULTILINE
        ):
            if m.group(1) not in self.imports and ("sys:" + m.group(1)) not in self.imports:
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

        for m in re.finditer(r"\btypedef\s+struct\s*\{[^}]*\}\s*(\w+)\s*;", content):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )

        for m in re.finditer(r"\b(?:typedef\s+)?(?:enum(?:\s+class)?)\s+(\w+)\s*(?:\{|:|;)", content):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="enum",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )

        for m in re.finditer(r"\b(?:typedef\s+)?union\s+(\w+)\s*(?:\{|;)", content):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="union",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )

        for m in re.finditer(r"^\s*typedef\s+(?!struct\s*\{|enum\s|union\s)([^;]+?)\s+(\w+)(?:\s*\[[^\]]*\])?\s*;", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(2),
                    kind="type_alias",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                    signature=" ".join(m.group(0).split()),
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
        seen_funcs: set[tuple[str, int]] = set()
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
                "do",
                "else",
                "case",
                "enum",
                "struct",
                "union",
            ):
                continue
            preceding = content[max(0, m.start() - 200) : m.start()]
            if "/*" in preceding and "*/" not in preceding.split("/*")[-1]:
                continue
            line_num = content[: m.start()].count("\n")
            seen_funcs.add((name, line_num + 1))
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                    signature=self._extract_signature(content, m.start(), func_pattern),
                )
            )

        proto_pattern = r"^[\w\s\*&:<>]+?\b([a-zA-Z_]\w*)\s*\([^;{}]*\)\s*(?:const\s*)?(?:noexcept\s*)?;"
        for m in re.finditer(proto_pattern, content, re.MULTILINE):
            name = m.group(1)
            if name in ("if", "for", "while", "switch", "catch", "return",
                        "sizeof", "typedef", "do", "else", "case"):
                continue
            line_num = content[: m.start()].count("\n")
            if (name, line_num + 1) in seen_funcs:
                continue
            if any(s.name == name and s.kind == "function" for s in self.symbols):
                continue
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                    signature=" ".join(m.group(0).split())[:200],
                )
            )

        for m in re.finditer(r"^\s*extern\s+(?:\"C\"\s*\{?)?\s*([^;]+?)\s*(\w+)\s*(?:\[[^\]]*\])?\s*;", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(2),
                    kind="variable",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                    signature=" ".join(m.group(0).split())[:200],
                )
            )

        for m in re.finditer(r'^\s*#\s*define\s+(\w+)(\([^)]*\))?', content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            sig = m.group(0).strip()[:200]
            self.symbols.append(
                Symbol(name=m.group(1), kind="macro", line=line_num + 1, signature=sig)
            )


