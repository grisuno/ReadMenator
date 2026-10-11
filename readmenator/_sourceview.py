"""Source viewer payload builder for the graph explorers.

Builds the per-file source texts embedded in the force-graph and edge
bundle explorer pages. The frontend renders them lazily inside a drawer
with offline syntax highlighting, theme-aware colors, hover cards, and
Ctrl+Click go-to-definition driven by the symbol index already present
in the payload. No network requests are involved.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from readmenator._config import Config
from readmenator._models import Node


@dataclass
class SourceEntry:
    """Bounded source text for one file.

    Attributes:
        text: Truncated source text ("" when unavailable or private).
        lines: Total line count of the original content.
        truncated: True when the text was cut to fit the budgets.
        language: Language label copied from the scanned node.
    """

    text: str
    lines: int
    truncated: bool
    language: str


class SourceViewBuilder:
    """Builds bounded source payloads for the explorer drawer."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for source viewer budgets and privacy mode.
        """
        self._config = config

    def enabled(self) -> bool:
        """Return True when sources may be embedded in the payload.

        Returns:
            False when disabled by config or privacy mode.
        """
        return bool(self._config.SOURCEVIEW_ENABLED) and not bool(self._config.PRIVACY_MODE)

    def build_sources(
        self, nodes: List[Node], content_map: Dict[str, str] | None
    ) -> Dict[str, SourceEntry]:
        """Build bounded source entries for every node in sorted order.

        Args:
            nodes: Scanned file nodes.
            content_map: Mapping of file identifier to full file content.

        Returns:
            Mapping of file identifier to bounded SourceEntry.
        """
        if not self.enabled() or not content_map:
            return {}
        max_files = max(0, int(self._config.SOURCEVIEW_MAX_FILES))
        max_chars = max(0, int(self._config.SOURCEVIEW_MAX_CHARS_PER_FILE))
        max_lines = max(0, int(self._config.SOURCEVIEW_MAX_LINES_PER_FILE))
        max_total = max(0, int(self._config.SOURCEVIEW_MAX_TOTAL_CHARS))
        sources: Dict[str, SourceEntry] = {}
        total = 0
        for node in sorted(nodes, key=lambda item: item.node_id):
            if len(sources) >= max_files:
                break
            content = content_map.get(node.node_id, "")
            if not content:
                continue
            lines = content.splitlines()
            original_lines = len(lines)
            truncated = False
            if max_lines and len(lines) > max_lines:
                lines = lines[:max_lines]
                truncated = True
            text = "\n".join(lines)
            if max_chars and len(text) > max_chars:
                text = text[:max_chars]
                truncated = True
            if max_total and total + len(text) > max_total:
                remaining = max_total - total
                if remaining <= 0:
                    break
                text = text[:remaining]
                truncated = True
            total += len(text)
            sources[node.node_id] = SourceEntry(
                text=text, lines=original_lines, truncated=truncated, language=node.language
            )
            if max_total and total >= max_total:
                break
        return sources

    def to_payload(self, sources: Dict[str, SourceEntry]) -> Dict[str, Dict[str, object]]:
        """Serialise source entries to JSON-safe payload records.

        Args:
            sources: Mapping from build_sources.

        Returns:
            Mapping of file identifier to payload record.
        """
        return {
            file_id: {
                "t": entry.text,
                "n": entry.lines,
                "c": 1 if entry.truncated else 0,
                "lg": entry.language,
            }
            for file_id, entry in sources.items()
        }
