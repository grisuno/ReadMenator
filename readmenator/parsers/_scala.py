from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


