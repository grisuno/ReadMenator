from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class ShellParser(LanguageParser):
    """Parser for shell scripts (.sh, .bash, .zsh).

    Extracts function declarations in both POSIX (``name() {``)
    and ``function`` keyword syntax.
    """

    def _extract_specifics(self, content: str) -> None:
        patterns = [
            r"^(\w+)\s*\(\)\s*\{",
            r"^function\s+(\w+)\s*(?:\(\))?\s*\{",
        ]
        for pattern in patterns:
            for m in re.finditer(pattern, content, re.MULTILINE):
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=m.group(1),
                        kind="function",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


