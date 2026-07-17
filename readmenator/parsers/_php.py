from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


