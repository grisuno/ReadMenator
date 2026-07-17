from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class RustParser(LanguageParser):
    """Parser for Rust (.rs).

    Extracts ``use`` imports, public and private functions,
    structs, traits, and enums.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^use\s+([\w:]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^(?:pub\s+)?(?:async\s+)?fn\s+(\w+)", content, re.MULTILINE
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
        for m in re.finditer(r"^(?:pub\s+)?struct\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^(?:pub\s+)?trait\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="trait",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^(?:pub\s+)?enum\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="enum",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


