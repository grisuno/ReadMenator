from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


