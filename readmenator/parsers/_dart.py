from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


