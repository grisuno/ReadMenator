from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


