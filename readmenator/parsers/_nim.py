from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


