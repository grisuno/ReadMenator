from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class RubyParser(LanguageParser):
    """Parser for Ruby (.rb).

    Extracts ``require`` / ``require_relative`` imports, class and
    module definitions with inheritance, and method definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"""(?:require|require_relative)\s+['"]([^'"]+)['"]""", content
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*class\s+(\w+)(?:\s*<\s*(\w+))?", content, re.MULTILINE
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
            r"^\s*module\s+(\w+)", content, re.MULTILINE
        ):
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=m.group(1),
                    kind="module",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^\s*def\s+(self\.)?(\w+)", content, re.MULTILINE
        ):
            name = m.group(2)
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="method",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )


