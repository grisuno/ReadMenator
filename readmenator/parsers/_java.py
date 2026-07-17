from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class JavaParser(LanguageParser):
    """Parser for Java (.java).

    Extracts import statements, class and interface declarations,
    and methods complete with access modifiers and type signatures.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(r"^import\s+([\w.]+)", content, re.MULTILINE):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"(?:public|private|protected)?\s*(?:abstract\s+)?(?:class|interface)\s+(\w+)",
            content,
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
        method_pattern = r"(?:public|private|protected)?\s*(?:static\s+)?(?:[\w<>\[\]]+\s+)+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{"
        reserved = {"if", "for", "while", "switch", "catch"}
        for m in re.finditer(method_pattern, content):
            name = m.group(1)
            if name not in reserved:
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="method",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


