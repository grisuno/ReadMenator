from __future__ import annotations

from readmenator.parsers._base import LanguageParser
from readmenator._models import Symbol
import re



class ElixirParser(LanguageParser):
    """Parser for Elixir (.ex, .exs).

    Extracts ``import``/``alias``/``require``/``use`` directives,
    module definitions, and named function definitions.
    """

    def _extract_specifics(self, content: str) -> None:
        for m in re.finditer(
            r"^\s*(?:import|alias|require|use)\s+([\w.{}]+)",
            content,
            re.MULTILINE,
        ):
            self.imports.append(m.group(1))
        for m in re.finditer(
            r"^\s*defmodule\s+([\w.]+)", content, re.MULTILINE
        ):
            name = m.group(1).split(".")[-1]
            line_num = content[: m.start()].count("\n")
            self.symbols.append(
                Symbol(
                    name=name,
                    kind="module",
                    line=line_num + 1,
                    doc=self._extract_docstring(line_num),
                )
            )
        for m in re.finditer(
            r"^\s*def(?:macro)?(?:p)?\s+(when\s+.*?\bdo\b\s*)?(\w+)",
            content,
            re.MULTILINE,
        ):
            name = m.group(2) if m.group(2) else m.group(1)
            if name and name not in ("if", "unless", "case", "cond", "with", "for", "try", "receive"):
                line_num = content[: m.start()].count("\n")
                self.symbols.append(
                    Symbol(
                        name=name,
                        kind="function",
                        line=line_num + 1,
                        doc=self._extract_docstring(line_num),
                    )
                )


