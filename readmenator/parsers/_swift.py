from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class SwiftParser(LanguageParser):
    """Parser for Swift (.swift).

    Extracts ``import`` statements, class/struct/enum/protocol
    declarations with inheritance, and function definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+(\w+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*(?:public|private|internal|fileprivate\s+)?"
            r"(?:final\s+)?class\s+(\w+)(?:\s*:\s*(\w+))?",
            content,
            re.MULTILINE,
        ):
            name = m.group(1)
            parent = m.group(2)
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="class",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
            if parent:
                self.inherits.append((name, parent))
        for m in re.finditer(
            r"^\s*(?:public|private|internal\s+)?(?:struct|enum)\s+(\w+)",
            content,
            re.MULTILINE,
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind=m.group(2) if "group" in str(m) else "struct",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(r"^\s*(?:public|private|internal\s+)?protocol\s+(\w+)", content, re.MULTILINE):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="protocol",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^\s*(?:public|private|internal\s+)?"
            r"(?:override\s+)?(?:class\s+)?func\s+(\w+)",
            content,
            re.MULTILINE,
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


