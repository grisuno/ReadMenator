from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._models import Symbol


class LanguageParser:
    """Base class for all language-specific parsers.

    Subclasses must implement ``_extract_specifics`` to populate
    ``self.symbols`` and ``self.imports``. Common utility methods
    ``_extract_docstring`` and ``_extract_signature`` are provided
    for reuse across all parsers.
    """

    def __init__(self, filename: str, config: Config) -> None:
        """Initialise the parser with a file path and application config.

        Args:
            filename: Relative or absolute path of the source file.
            config: Application-wide configuration settings.
        """
        self.filename = filename
        self.config = config
        self.symbols: List[Symbol] = []
        self.imports: List[str] = []
        self.calls: List[Tuple[str, str]] = []
        self.inherits: List[Tuple[str, str]] = []
        self.lines: List[str] = []

    def parse(self, content: str) -> None:
        """Parse *content* and populate symbol/import lists.

        Splits the source into lines, then delegates to the subclass-
        specific ``_extract_specifics`` logic.
        """
        self.lines = content.split("\n")
        self._extract_specifics(content)

    def _extract_specifics(self, content: str) -> None:
        """Subclass hook for language-specific symbol extraction."""
        raise NotImplementedError

    def _extract_docstring(self, line_num: int) -> str:
        """Walk backwards from *line_num* to collect preceding comments/docstrings.

        Supports ``//``, ``///``, ``//!``, ``#``, ``/* */``, and ``/** */``
        comment styles. Limits lookback to ``DOCSTRING_LOOKBACK_LINES``
        from Config.
        """
        if line_num >= len(self.lines):
            return ""
        doc_lines: List[str] = []
        in_block_comment = False
        max_lookback = self.config.DOCSTRING_LOOKBACK_LINES
        for i in range(line_num - 1, max(-1, line_num - max_lookback), -1):
            line = self.lines[i].strip()
            if not line:
                if not in_block_comment:
                    break
                continue
            if line.endswith("*/"):
                in_block_comment = True
                doc_lines.insert(0, line.rstrip("*/").strip())
                continue
            if in_block_comment:
                cleaned = line.lstrip("/*").lstrip("*").strip()
                doc_lines.insert(0, cleaned)
                if line.startswith("/*") or line.startswith("/**"):
                    break
                continue
            if line.startswith("///") or line.startswith("//!"):
                doc_lines.insert(0, line[3:].strip())
            elif line.startswith("//"):
                doc_lines.insert(0, line[2:].strip())
            elif line.startswith("#") and not line.startswith("#!"):
                doc_lines.insert(0, line[1:].strip())
            elif line == "":
                continue
            else:
                break
        doc = " ".join(doc_lines).strip()
        doc = re.sub(r"^[\-\*\+]\s*", "", doc)
        return doc

    def _extract_signature(self, content: str, match_start: int, pattern: str) -> str:
        """Extract a compact signature snippet starting at *match_start*.

        Scans forward to the opening brace or a fallback length,
        then truncates to 100 characters for display.
        """
        start = match_start
        end = content.find("{", start)
        if end == -1:
            end = start + 120
        raw = content[start:end].strip()
        if len(raw) > 100:
            raw = raw[:97] + "..."
        return raw


