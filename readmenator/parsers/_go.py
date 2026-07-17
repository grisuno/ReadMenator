from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



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


