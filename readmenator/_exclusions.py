"""False-positive exclusion list for readmenator findings.

The `exclusions.yaml` corpus blocklist records paths cleared through
investigation with a reason, so known-clean patterns are skipped on
future runs instead of being re-investigated.
"""

from __future__ import annotations

import fnmatch
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

from readmenator._config import Config


@dataclass
class ExclusionEntry:
    """A single exclusion record from the blocklist file."""

    pattern: str
    rule_id: str = "*"
    reason: str = ""
    reclassified_as: str = ""

    def matches(self, file_path: str, rule_id: str) -> bool:
        """Return True when this entry suppresses the finding.

        Args:
            file_path: Finding file path to test.
            rule_id: Finding rule identifier to test.

        Returns:
            True when both the path glob and rule match.
        """
        if self.rule_id not in ("*", rule_id):
            return False
        return fnmatch.fnmatch(file_path, self.pattern) or fnmatch.fnmatch(
            file_path.split("/")[-1], self.pattern
        )


class ExclusionList:
    """Loads and applies the YAML exclusion blocklist."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for the exclusions file path and flag.
        """
        self._config = config
        self._entries: List[ExclusionEntry] = []
        self._loaded_from: str = ""

    @property
    def entries(self) -> List[ExclusionEntry]:
        """Return the loaded exclusion entries."""
        return list(self._entries)

    def load(self, project_root: str | Path) -> List[ExclusionEntry]:
        """Load exclusions from the project blocklist file.

        Args:
            project_root: Project directory containing the rules dir.

        Returns:
            Loaded exclusion entries (empty when disabled or missing).
        """
        self._entries = []
        self._loaded_from = ""
        if not self._config.EXCLUSIONS_ENABLED:
            return []
        candidate = Path(project_root) / self._config.EXCLUSIONS_FILE
        if not candidate.is_file():
            return []
        try:
            text = candidate.read_text(encoding="utf-8")
        except OSError:
            return []
        self._entries = parse_exclusions(text)
        self._loaded_from = str(candidate)
        return list(self._entries)

    def is_excluded(self, file_path: str, rule_id: str) -> bool:
        """Return True when a finding is suppressed by the blocklist.

        Args:
            file_path: Finding file path.
            rule_id: Finding rule identifier.

        Returns:
            True when any entry matches.
        """
        return any(entry.matches(file_path, rule_id) for entry in self._entries)

    def filter_findings(self, findings: List) -> List:
        """Remove excluded findings from a finding list.

        Args:
            findings: Findings with file_path and rule_id attributes.

        Returns:
            Findings not matched by any exclusion entry.
        """
        return [
            item
            for item in findings
            if not self.is_excluded(str(getattr(item, "file_path", "")), str(getattr(item, "rule_id", "")))
        ]


def parse_exclusions(text: str) -> List[ExclusionEntry]:
    """Parse the minimal exclusions YAML into entries.

    Args:
        text: Raw YAML content with `exclusions:` list items.

    Returns:
        Parsed exclusion entries.
    """
    entries: List[ExclusionEntry] = []
    current: Dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "exclusions:":
            continue
        if stripped.startswith("- "):
            if current:
                entries.append(_to_entry(current))
            current = {}
            rest = stripped[2:].strip()
            if ": " in rest:
                key, value = rest.split(": ", 1)
                current[key.strip()] = _unquote(value.strip())
        elif ": " in stripped and current is not None:
            key, value = stripped.split(": ", 1)
            current[key.strip()] = _unquote(value.strip())
    if current:
        entries.append(_to_entry(current))
    return entries


def _to_entry(data: Dict[str, str]) -> ExclusionEntry:
    """Convert a raw mapping into an exclusion entry."""
    pattern = data.get("pattern") or data.get("path") or data.get("sha256") or "*"
    return ExclusionEntry(
        pattern=pattern,
        rule_id=data.get("rule_id", "*") or "*",
        reason=data.get("reason", ""),
        reclassified_as=data.get("reclassified_as", ""),
    )


def _unquote(value: str) -> str:
    """Strip matching single or double quotes from a scalar."""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value
