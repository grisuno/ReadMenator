from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class JavaScriptParser(LanguageParser):
    """Parser for JavaScript / TypeScript (.js, .ts, .jsx, .tsx).

    Extracts ES module imports, CommonJS ``require`` calls, function
    declarations, arrow-function variables, and class definitions
    (including inheritance).
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"""import\s+(?:\{[^}]*\}\s+from\s+)?['"]([^'"]+)['"]""", content
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"""require\s*\(['"]([^'"]+)['"]\)""", content
        ):
            self.imports.append(m.group(1))
        patterns = [
            r"(?:^|\s)function\s+(\w+)",
            r"(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(",
            r"(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?function",
        ]
        reserved = {"if", "for", "while", "switch", "catch"}
        for pattern in patterns:
            for m in re.finditer(pattern, content):
                name = m.group(1)
                if name not in reserved:
                    line_num = content[: m.start()].count("\n")
                    self.symbols.append(
                        Symbol(
                            name=name,
                            kind="function",
                            line=line_num + 1,
                            doc=self._extract_docstring(line_num),
                        )
                    )
        for m in re.finditer(
            r"class\s+(\w+)(?:\s+extends\s+(\w+))?", content
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
        for m in re.finditer(r"(\w+)\s*\([^)]*\)\s*(?:;|{)?", content):
            callee = m.group(1)
            if callee and callee[0].isupper() is False and callee not in reserved:
                if len(callee) >= 3 and callee not in {"var", "let", "const", "new", "true", "false", "null"}:
                    self.calls.append(("", callee))


