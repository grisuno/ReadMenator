"""Contract tests for the static security analysis module.

Tests cover the SecurityFinding data model, per-language rule
detection, severity threshold filtering, path validation, and
end-to-end scanning of dangerous patterns across all supported
languages.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from readmenator._config import Config
from readmenator._models import SecurityFinding
from readmenator._security import SecurityAnalyzer


class TestSecurityFinding(unittest.TestCase):
    """SecurityFinding dataclass contract tests."""

    def test_security_finding_fields(self) -> None:
        finding = SecurityFinding(
            file_path="src/main.py",
            line=42,
            severity="high",
            rule_id="PY001",
            description="Command injection risk",
            snippet='os.system("rm -rf /")',
            cwe="CWE-78",
        )
        self.assertEqual(finding.file_path, "src/main.py")
        self.assertEqual(finding.line, 42)
        self.assertEqual(finding.severity, "high")
        self.assertEqual(finding.rule_id, "PY001")
        self.assertEqual(finding.description, "Command injection risk")
        self.assertEqual(finding.snippet, 'os.system("rm -rf /")')
        self.assertEqual(finding.cwe, "CWE-78")


class TestSecurityAnalyzerConfig(unittest.TestCase):
    """SecurityAnalyzer configuration contract tests."""

    def test_default_config_disables_security(self) -> None:
        config = Config()
        self.assertFalse(config.SECURITY_ENABLED)

    def test_default_severity_threshold(self) -> None:
        config = Config()
        self.assertEqual(config.SECURITY_SEVERITY_THRESHOLD, "medium")

    def test_default_security_output(self) -> None:
        config = Config()
        self.assertEqual(config.SECURITY_OUTPUT, "KNOWLEDGE_BASE.md")

    def test_init_with_config(self) -> None:
        config = Config()
        analyzer = SecurityAnalyzer(config)
        self.assertIsNotNone(analyzer)


class TestSecurityAnalyzerRules(unittest.TestCase):
    """Per-language rule detection tests using inline code."""

    def setUp(self) -> None:
        self.config = Config(SECURITY_ENABLED=True, SECURITY_SEVERITY_THRESHOLD="info")
        self.analyzer = SecurityAnalyzer(self.config)

    def _scan_content(self, content: str, extension: str = ".py") -> list:
        """Write content to a temp file and scan it."""
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / f"test{extension}"
            file_path.write_text(content, encoding="utf-8")
            return self.analyzer.scan(Path(tmp))

    def test_python_os_system(self) -> None:
        findings = self._scan_content('import os\nos.system("ls -la")\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY001", rule_ids)

    def test_python_eval(self) -> None:
        findings = self._scan_content('eval("__import__(\'os\').system(\'id\')")\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY002", rule_ids)

    def test_python_pickle(self) -> None:
        findings = self._scan_content('pickle.loads(data)\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY003", rule_ids)

    def test_python_sql_injection(self) -> None:
        findings = self._scan_content('cursor.execute("SELECT * FROM users WHERE id = " + uid)\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY004", rule_ids)

    def test_python_hardcoded_secret(self) -> None:
        findings = self._scan_content('password = "super_secret_123"\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY005", rule_ids)

    def test_python_weak_crypto(self) -> None:
        findings = self._scan_content('hashlib.md5(b"test")\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY006", rule_ids)

    def test_python_request_verify_false(self) -> None:
        findings = self._scan_content('requests.get(url, verify=False)\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY008", rule_ids)

    def test_python_flask_debug(self) -> None:
        findings = self._scan_content('app.run(debug=True)\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY009", rule_ids)

    def test_python_yaml_load(self) -> None:
        findings = self._scan_content('yaml.load(data)\n', ".py")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("PY012", rule_ids)

    def test_javascript_inner_html(self) -> None:
        findings = self._scan_content('element.innerHTML = userInput;\n', ".js")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("JS001", rule_ids)

    def test_javascript_eval(self) -> None:
        findings = self._scan_content('eval(userCode);\n', ".js")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("JS002", rule_ids)

    def test_javascript_child_process(self) -> None:
        findings = self._scan_content('child_process.exec("rm -rf /");\n', ".js")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("JS003", rule_ids)

    def test_javascript_dangerously_set_inner_html(self) -> None:
        findings = self._scan_content('dangerouslySetInnerHTML={{__html: xss}};\n', ".jsx")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("JS007", rule_ids)

    def test_c_strcpy(self) -> None:
        findings = self._scan_content('strcpy(buffer, source);\n', ".c")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("C001", rule_ids)

    def test_c_gets(self) -> None:
        findings = self._scan_content('gets(buffer);\n', ".c")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("C003", rule_ids)

    def test_c_system(self) -> None:
        findings = self._scan_content('system("ls");\n', ".c")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("C006", rule_ids)

    def test_java_runtime_exec(self) -> None:
        findings = self._scan_content('Runtime.getRuntime().exec("cmd");\n', ".java")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("J001", rule_ids)

    def test_java_sql_injection(self) -> None:
        findings = self._scan_content('stmt.executeQuery("SELECT * FROM " + table);\n', ".java")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("J003", rule_ids)

    def test_go_exec_command(self) -> None:
        findings = self._scan_content('exec.Command("bash", "-c", userInput)\n', ".go")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("G001", rule_ids)

    def test_ruby_eval(self) -> None:
        findings = self._scan_content('eval("system(\'id\')")\n', ".rb")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("R001", rule_ids)

    def test_ruby_marshal_load(self) -> None:
        findings = self._scan_content('Marshal.load(data)\n', ".rb")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("R004", rule_ids)

    def test_php_eval(self) -> None:
        findings = self._scan_content("<?php eval('echo 1;'); ?>", ".php")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("P001", rule_ids)

    def test_php_sql_injection(self) -> None:
        findings = self._scan_content('<?php mysql_query("SELECT * FROM " . $table); ?>', ".php")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("P003", rule_ids)

    def test_php_unseralize(self) -> None:
        findings = self._scan_content('<?php unserialize($data); ?>', ".php")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("P004", rule_ids)

    def test_shell_eval(self) -> None:
        findings = self._scan_content('eval "$command"\n', ".sh")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("S001", rule_ids)

    def test_csharp_process_start(self) -> None:
        findings = self._scan_content('Process.Start("malware.exe");\n', ".cs")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("CS001", rule_ids)

    def test_kotlin_runtime_exec(self) -> None:
        findings = self._scan_content('Runtime.getRuntime().exec("cmd")\n', ".kt")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("K001", rule_ids)

    def test_swift_process(self) -> None:
        findings = self._scan_content('Process().launchPath = "/bin/sh"\n', ".swift")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("SW001", rule_ids)

    def test_lua_load(self) -> None:
        findings = self._scan_content('load("os.execute(\'id\')")()\n', ".lua")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("L001", rule_ids)

    def test_lua_os_execute(self) -> None:
        findings = self._scan_content('os.execute("rm -rf /")\n', ".lua")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("L003", rule_ids)

    def test_dart_process_run(self) -> None:
        findings = self._scan_content('Process.run("bash", ["-c", cmd]);\n', ".dart")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("D001", rule_ids)

    def test_rust_unsafe(self) -> None:
        findings = self._scan_content('unsafe {\n    *ptr = 42;\n}\n', ".rs")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("RS002", rule_ids)

    def test_elixir_code_eval(self) -> None:
        findings = self._scan_content('Code.eval_string("IO.puts(1)")\n', ".ex")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("E001", rule_ids)

    def test_elixir_system_cmd(self) -> None:
        findings = self._scan_content('System.cmd("rm", ["-rf", "/"])\n', ".ex")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("E002", rule_ids)

    def test_gdscript_os_execute(self) -> None:
        findings = self._scan_content('OS.execute("ls", ["-la"])\n', ".gd")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("GD002", rule_ids)

    def test_scala_runtime_exec(self) -> None:
        findings = self._scan_content('Runtime.getRuntime.exec("cmd")\n', ".scala")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("SC001", rule_ids)

    def test_nim_exec_process(self) -> None:
        findings = self._scan_content('execProcess("bash")\n', ".nim")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("N001", rule_ids)

    def test_safe_code_produces_no_findings(self) -> None:
        content = """def hello(name: str) -> str:
    return f"Hello, {name}!"

class Greeter:
    def greet(self) -> None:
        print(hello("world"))
"""
        findings = self._scan_content(content, ".py")
        self.assertEqual(len(findings), 0)

    def test_csharp_binary_formatter(self) -> None:
        findings = self._scan_content('BinaryFormatter.Deserialize(stream);\n', ".cs")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("CS003", rule_ids)

    def test_ruby_backtick(self) -> None:
        findings = self._scan_content('`ls #{user_input}`\n', ".rb")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("R006", rule_ids)

    def test_php_xss(self) -> None:
        findings = self._scan_content('<?php echo $_GET["input"]; ?>', ".php")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("P005", rule_ids)

    def test_go_unsafe_package(self) -> None:
        findings = self._scan_content('import "unsafe"\n', ".go")
        rule_ids = [f.rule_id for f in findings]
        self.assertIn("G003", rule_ids)


class TestSecurityAnalyzerThreshold(unittest.TestCase):
    """Severity threshold filtering tests."""

    def test_threshold_filters_low(self) -> None:
        config = Config(SECURITY_ENABLED=True, SECURITY_SEVERITY_THRESHOLD="high")
        analyzer = SecurityAnalyzer(config)
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "test.py"
            file_path.write_text(
                'import os\nos.system("ls")\nassert True\n',
                encoding="utf-8",
            )
            findings = analyzer.scan(Path(tmp))
            rule_ids = [f.rule_id for f in findings]
            self.assertIn("PY001", rule_ids)
            self.assertNotIn("PY010", rule_ids)

    def test_threshold_info_shows_all(self) -> None:
        config = Config(SECURITY_ENABLED=True, SECURITY_SEVERITY_THRESHOLD="info")
        analyzer = SecurityAnalyzer(config)
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "test.py"
            file_path.write_text(
                'import os\nos.system("ls")\nassert True\n',
                encoding="utf-8",
            )
            findings = analyzer.scan(Path(tmp))
            rule_ids = [f.rule_id for f in findings]
            self.assertIn("PY001", rule_ids)
            self.assertIn("PY010", rule_ids)


class TestSecurityAnalyzerPathValidation(unittest.TestCase):
    """Security path validation tests."""

    def test_ignores_symlinks(self) -> None:
        config = Config(SECURITY_ENABLED=True)
        analyzer = SecurityAnalyzer(config)
        with tempfile.TemporaryDirectory() as tmp:
            real_file = Path(tmp) / "real.py"
            real_file.write_text('eval("test")\n', encoding="utf-8")
            link = Path(tmp) / "link.py"
            try:
                os.symlink(real_file, link)
                findings = analyzer.scan(Path(tmp))
                link_findings = [f for f in findings if "link.py" in f.file_path]
                self.assertEqual(len(link_findings), 0)
            except (OSError, NotImplementedError):
                pass

    def test_ignores_ignored_dirs(self) -> None:
        config = Config(SECURITY_ENABLED=True)
        analyzer = SecurityAnalyzer(config)
        with tempfile.TemporaryDirectory() as tmp:
            ignored = Path(tmp) / "node_modules"
            ignored.mkdir()
            bad_file = ignored / "bad.py"
            bad_file.write_text('eval("danger")\n', encoding="utf-8")
            findings = analyzer.scan(Path(tmp))
            bad_findings = [f for f in findings if "bad.py" in f.file_path]
            self.assertEqual(len(bad_findings), 0)

    def test_empty_directory(self) -> None:
        config = Config(SECURITY_ENABLED=True)
        analyzer = SecurityAnalyzer(config)
        with tempfile.TemporaryDirectory() as tmp:
            findings = analyzer.scan(Path(tmp))
            self.assertEqual(len(findings), 0)

    def test_unsupported_extension(self) -> None:
        config = Config(SECURITY_ENABLED=True)
        analyzer = SecurityAnalyzer(config)
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "test.xyz"
            file_path.write_text('eval("danger")\n', encoding="utf-8")
            findings = analyzer.scan(Path(tmp))
            self.assertEqual(len(findings), 0)


class TestSecurityAnalyzerSummary(unittest.TestCase):
    """Security summary output tests."""

    def test_summary_empty(self) -> None:
        config = Config(SECURITY_ENABLED=True)
        analyzer = SecurityAnalyzer(config)
        result = analyzer.summary([])
        self.assertIn("no findings", result.lower())

    def test_summary_with_findings(self) -> None:
        config = Config(SECURITY_ENABLED=True)
        analyzer = SecurityAnalyzer(config)
        findings = [
            SecurityFinding("a.py", 1, "high", "PY002", "eval", "eval(x)", "CWE-95"),
            SecurityFinding("b.py", 5, "critical", "PY001", "os.system", 'os.system("id")', "CWE-78"),
        ]
        result = analyzer.summary(findings)
        self.assertIn("2 finding", result)
        self.assertIn("high", result)
        self.assertIn("critical", result)


if __name__ == "__main__":
    unittest.main()
