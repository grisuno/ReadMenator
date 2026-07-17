from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


