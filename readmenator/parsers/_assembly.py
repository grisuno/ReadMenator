from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class AssemblyParser(LanguageParser):
    """Parser for assembly (.asm, .s, .S).

    Extracts labels at the start of a line (``label:``) as function
    symbols. This is a best-effort heuristic; local labels and
    directives are not always distinguishable.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^([a-zA-Z_]\w*):", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="function",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


