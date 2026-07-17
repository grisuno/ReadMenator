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


