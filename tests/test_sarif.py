from __future__ import annotations

import json
import unittest

from readmenator._config import Config
from readmenator._models import SecurityFinding
from readmenator._sarif import SarifExporter


class TestSarifExporterContract(unittest.TestCase):
    """Contract: SarifExporter produces valid SARIF v2.1.0 JSON."""

    def setUp(self) -> None:
        self.config = Config()
        self.sarif = SarifExporter(self.config)

    def _make_finding(
        self,
        file_path: str = "main.py",
        line: int = 10,
        severity: str = "high",
        rule_id: str = "TEST001",
        description: str = "Test finding",
        snippet: str = "eval(x)",
        cwe: str = "CWE-95",
    ) -> SecurityFinding:
        return SecurityFinding(
            file_path=file_path,
            line=line,
            severity=severity,
            rule_id=rule_id,
            description=description,
            snippet=snippet,
            cwe=cwe,
        )

    def test_export_returns_valid_json(self) -> None:
        findings = [self._make_finding()]
        result = self.sarif.export(findings)
        data = json.loads(result)
        self.assertIn("$schema", data)
        self.assertEqual(data["version"], "2.1.0")
        self.assertIn("runs", data)

    def test_export_includes_tool_info(self) -> None:
        findings = [self._make_finding()]
        result = self.sarif.export(findings)
        data = json.loads(result)
        driver = data["runs"][0]["tool"]["driver"]
        self.assertEqual(driver["name"], "ReadMenator")
        self.assertIn("rules", driver)

    def test_export_includes_rule(self) -> None:
        findings = [self._make_finding(rule_id="PY001")]
        result = self.sarif.export(findings)
        data = json.loads(result)
        rules = data["runs"][0]["tool"]["driver"]["rules"]
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0]["id"], "PY001")

    def test_export_includes_result(self) -> None:
        findings = [self._make_finding(file_path="src/main.py", line=42)]
        result = self.sarif.export(findings)
        data = json.loads(result)
        results = data["runs"][0]["results"]
        self.assertEqual(len(results), 1)
        uri = results[0]["locations"][0]["physicalLocation"]["artifactLocation"]["uri"]
        self.assertEqual(uri, "src/main.py")
        start_line = results[0]["locations"][0]["physicalLocation"]["region"]["startLine"]
        self.assertEqual(start_line, 42)

    def test_severity_maps_correctly(self) -> None:
        tests = [
            ("critical", "error"),
            ("high", "error"),
            ("medium", "warning"),
            ("low", "note"),
            ("info", "note"),
        ]
        for sev, expected_level in tests:
            finding = self._make_finding(severity=sev)
            result = self.sarif.export([finding])
            data = json.loads(result)
            level = data["runs"][0]["results"][0]["level"]
            self.assertEqual(level, expected_level, f"Failed for severity {sev}")

    def test_privacy_mode_strips_snippets(self) -> None:
        cfg = Config(PRIVACY_MODE=True)
        sarif = SarifExporter(cfg)
        finding = self._make_finding(snippet="secret = 'hunter2'")
        result = sarif.export([finding])
        data = json.loads(result)
        region = data["runs"][0]["results"][0]["locations"][0]["physicalLocation"]["region"]
        self.assertNotIn("snippet", region)

    def test_empty_findings_produces_valid_sarif(self) -> None:
        result = self.sarif.export([])
        data = json.loads(result)
        self.assertEqual(len(data["runs"][0]["results"]), 0)
        self.assertEqual(len(data["runs"][0]["tool"]["driver"]["rules"]), 0)
