"""Evidence-provenance audit for readmenator security findings.

Every match must answer which evidence tier supports it. Findings
resting only on weak or inferred signals (no snippet, inferred
confidence) are flagged as `inferred_only`; findings with static
extracts are `static`. Corpus frequency tells shared boilerplate
apart from file-unique signals.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

from readmenator._config import Config
from readmenator._models import SecurityFinding


@dataclass(frozen=True)
class ProvenanceFinding:
    """A single finding classified by evidence provenance."""

    file_path: str
    rule: str
    severity: str
    provenance: str
    memory_only_patterns: List[str] = field(default_factory=list)
    static_patterns: List[str] = field(default_factory=list)
    corpus_frequency: Dict[str, int] = field(default_factory=dict)

    @property
    def is_inferred_only(self) -> bool:
        """Return True when no static evidence supports the finding."""
        return self.provenance == "inferred_only"

    @property
    def reading(self) -> str:
        """Explain which way an inferred-only hit points."""
        if self.provenance != "inferred_only" or not self.corpus_frequency:
            return "n/a"
        if max(self.corpus_frequency.values()) <= 1:
            return "file_unique — likely real signal; inspect the file"
        return "shared — needs an independent check (imports/layer/cluster) to tell project idiom from boilerplate"


class ProvenanceAuditor:
    """Classifies security findings by static versus inferred evidence."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings guarding the provenance audit flag.
        """
        self._config = config

    def audit(
        self,
        findings: List[SecurityFinding],
        content_map: Dict[str, str] | None = None,
    ) -> List[ProvenanceFinding]:
        """Audit findings for evidence provenance.

        Args:
            findings: Security findings to classify.
            content_map: Optional mapping of file path to raw content.

        Returns:
            Provenance findings sorted by severity then file path.
        """
        results: List[ProvenanceFinding] = []
        for finding in findings:
            snippet = (finding.snippet or "").strip()
            has_static = bool(snippet) and self._snippet_in_content(
                finding.file_path, snippet, content_map or {}
            )
            if snippet and not (content_map or {}):
                has_static = True
            provenance = "static" if has_static else "inferred_only"
            static_patterns = [finding.rule_id] if has_static else []
            memory_patterns: List[str] = [] if has_static else [finding.rule_id]
            results.append(
                ProvenanceFinding(
                    file_path=finding.file_path,
                    rule=finding.rule_id,
                    severity=finding.severity,
                    provenance=provenance,
                    memory_only_patterns=memory_patterns,
                    static_patterns=static_patterns,
                )
            )
        order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
        results.sort(key=lambda item: (order.get(item.severity, 5), item.file_path))
        if content_map:
            return self._attach_frequency(results, content_map)
        return results

    def summary(self, findings: List[ProvenanceFinding]) -> Dict[str, Any]:
        """Summarize provenance findings by provenance class.

        Args:
            findings: Classified provenance findings.

        Returns:
            Counts of static, inferred-only, and affected files.
        """
        inferred = [item for item in findings if item.is_inferred_only]
        return {
            "total": len(findings),
            "static": len(findings) - len(inferred),
            "inferred_only": len(inferred),
            "inferred_only_files": len({item.file_path for item in inferred}),
        }

    def _snippet_in_content(
        self, file_path: str, snippet: str, content_map: Dict[str, str]
    ) -> bool:
        """Check whether a snippet is present in the stored file content."""
        for path, content in content_map.items():
            if path == file_path or path.endswith(file_path) or file_path.endswith(path):
                return snippet[:40] in content or snippet in content
        return any(snippet[:40] in content for content in content_map.values())

    def _attach_frequency(
        self, findings: List[ProvenanceFinding], content_map: Dict[str, str]
    ) -> List[ProvenanceFinding]:
        """Attach corpus frequency counts to inferred-only findings."""
        patterns = sorted({item.rule for item in findings if item.is_inferred_only})
        rows: List[Tuple[str, str]] = list(content_map.items())
        frequency = _corpus_frequency(patterns, rows)
        enriched: List[ProvenanceFinding] = []
        for item in findings:
            if item.is_inferred_only:
                enriched.append(
                    ProvenanceFinding(
                        file_path=item.file_path,
                        rule=item.rule,
                        severity=item.severity,
                        provenance=item.provenance,
                        memory_only_patterns=item.memory_only_patterns,
                        static_patterns=item.static_patterns,
                        corpus_frequency={
                            pattern: frequency.get(pattern, 0)
                            for pattern in item.memory_only_patterns
                        },
                    )
                )
            else:
                enriched.append(item)
        return enriched


def _corpus_frequency(patterns: List[str], rows: List[Tuple[str, str]]) -> Dict[str, int]:
    """Count how many corpus files contain each pattern string."""
    counts = {pattern: 0 for pattern in patterns}
    lowered = {pattern: pattern.lower() for pattern in patterns}
    for _path, content in rows:
        blob = (content or "").lower()
        for pattern, needle in lowered.items():
            if needle and needle in blob:
                counts[pattern] += 1
    return counts
