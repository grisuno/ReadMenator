from __future__ import annotations

import json
from typing import Dict, List

from readmenator._config import Config
from readmenator._models import SecurityFinding


class SarifExporter:
    """Exports security findings to the SARIF (Static Analysis Results
    Interchange Format) standard.

    SARIF is an OASIS standard format for static analysis tool output.
    This exporter produces SARIF v2.1.0 JSON that is compatible with
    GitHub Code Scanning, VS Code SARIF viewer, and other SARIF consumers.
    """

    SARIF_VERSION = "2.1.0"
    SARIF_SCHEMA = "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json"

    SEVERITY_LEVEL_MAP: Dict[str, str] = {
        "critical": "error",
        "high": "error",
        "medium": "warning",
        "low": "note",
        "info": "note",
    }

    def __init__(self, config: Config) -> None:
        self._config = config

    def export(
        self,
        findings: List[SecurityFinding],
        project_name: str = "readmenator",
    ) -> str:
        """Generate a SARIF v2.1.0 JSON string from security findings.

        Args:
            findings: List of SecurityFinding instances.
            project_name: Name of the scanned project for metadata.

        Returns:
            SARIF JSON string.
        """
        tool_rules: List[Dict] = []
        results: List[Dict] = []
        rule_ids: Dict[str, int] = {}

        for finding in findings:
            if finding.rule_id not in rule_ids:
                rule_ids[finding.rule_id] = len(rule_ids)
                tool_rules.append(self._build_rule(finding))

            result = self._build_result(finding, rule_ids[finding.rule_id])
            results.append(result)

        log = {
            "$schema": self.SARIF_SCHEMA,
            "version": self.SARIF_VERSION,
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "ReadMenator",
                            "version": "1.0",
                            "informationUri": "https://github.com/grisuno/ReadMenator",
                            "rules": tool_rules,
                        }
                    },
                    "results": results,
                    "properties": {
                        "projectName": project_name,
                    },
                }
            ],
        }

        return json.dumps(log, indent=2, ensure_ascii=False)

    def _build_rule(self, finding: SecurityFinding) -> Dict:
        """Build a SARIF reportingDescriptor (rule) object."""
        return {
            "id": finding.rule_id,
            "name": finding.rule_id,
            "shortDescription": {
                "text": finding.description,
            },
            "fullDescription": {
                "text": finding.description,
            },
            "defaultConfiguration": {
                "level": self.SEVERITY_LEVEL_MAP.get(
                    finding.severity, "warning"
                ),
            },
            "properties": {
                "securitySeverity": finding.severity,
                "cwe": finding.cwe,
                "precision": "high",
                "tags": ["security", finding.severity],
            },
        }

    def _build_result(self, finding: SecurityFinding, rule_index: int) -> Dict:
        """Build a SARIF result object for a single finding."""
        result: Dict = {
            "ruleId": finding.rule_id,
            "ruleIndex": rule_index,
            "level": self.SEVERITY_LEVEL_MAP.get(finding.severity, "warning"),
            "message": {
                "text": finding.description,
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": finding.file_path,
                            "uriBaseId": "%SRCROOT%",
                        },
                        "region": {
                            "startLine": finding.line,
                        },
                    }
                }
            ],
        }

        if finding.snippet and not self._config.PRIVACY_MODE:
            result["locations"][0]["physicalLocation"]["region"]["snippet"] = {
                "text": finding.snippet,
            }

        if finding.cwe:
            result["properties"] = {
                "cwe": finding.cwe,
            }

        return result
