"""Pattern-based static security analysis for the readmenator knowledge graph.

Scans source files across all supported languages for dangerous patterns:
command injection, SQL injection, XSS, weak crypto, unsafe deserialization,
hardcoded secrets, and more. Pure regex-based, zero external dependencies.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from readmenator._config import Config
from readmenator._models import SecurityFinding


@dataclass
class SecurityRule:
    """A single security detection rule.

    Attributes:
        rule_id: Unique identifier (e.g. "PY001").
        severity: Severity level (critical, high, medium, low, info).
        description: Human-readable description of the issue.
        pattern: Compiled regex to search for.
        cwe: CWE identifier string.
    """

    rule_id: str
    severity: str
    description: str
    pattern: re.Pattern
    cwe: str


class SecurityAnalyzer:
    """Pattern-based static security scanner.

    Maintains per-language rule sets and walks the target directory
    applying rules to every supported source file. Designed to slot
    into the readmenator pipeline alongside GraphAnalyzer.
    """

    SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings including SECURITY_ENABLED and
                SECURITY_SEVERITY_THRESHOLD.
        """
        self._config = config
        self._rules = self._build_rules()

    @staticmethod
    def _build_rules() -> Dict[str, List[SecurityRule]]:
        """Build the complete per-language rule set."""
        return {
            ".py": _python_rules(),
            ".js": _javascript_rules(),
            ".ts": _javascript_rules(),
            ".jsx": _javascript_rules(),
            ".tsx": _javascript_rules(),
            ".c": _c_rules(),
            ".cpp": _c_rules(),
            ".cc": _c_rules(),
            ".cxx": _c_rules(),
            ".h": _c_rules(),
            ".hpp": _c_rules(),
            ".hxx": _c_rules(),
            ".java": _java_rules(),
            ".go": _go_rules(),
            ".rb": _ruby_rules(),
            ".php": _php_rules(),
            ".sh": _shell_rules(),
            ".bash": _shell_rules(),
            ".zsh": _shell_rules(),
            ".cs": _csharp_rules(),
            ".kt": _kotlin_rules(),
            ".kts": _kotlin_rules(),
            ".swift": _swift_rules(),
            ".scala": _scala_rules(),
            ".sc": _scala_rules(),
            ".lua": _lua_rules(),
            ".dart": _dart_rules(),
            ".rs": _rust_rules(),
            ".nim": _nim_rules(),
            ".gd": _gdscript_rules(),
            ".ex": _elixir_rules(),
            ".exs": _elixir_rules(),
        }

    def _meets_threshold(self, severity: str) -> bool:
        """Check if *severity* meets the configured threshold."""
        threshold = self._config.SECURITY_SEVERITY_THRESHOLD
        return self.SEVERITY_ORDER.get(severity, 99) <= self.SEVERITY_ORDER.get(
            threshold, 2
        )

    def scan(self, root: Path) -> List[SecurityFinding]:
        """Walk *root* and return all security findings.

        Applies the same security checks as PolyglotScanner (symlinks,
        ignore dirs, size limits, depth limits) for consistency.

        Args:
            root: Project root directory to scan.

        Returns:
            List of SecurityFinding instances, sorted by severity.
        """
        findings: List[SecurityFinding] = []

        if not root.is_dir():
            raise ValueError(f"Path is not a valid directory: {root}")

        root = root.resolve()

        for file_path in sorted(root.rglob("*")):
            if not file_path.is_file():
                continue

            if not self._validate_path(file_path, root):
                continue

            rel_path_str = file_path.relative_to(root).as_posix()
            extension = file_path.suffix
            rules = self._rules.get(extension)
            if not rules:
                continue

            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
            except (OSError, UnicodeDecodeError):
                continue

            lines = content.split("\n")

            for rule in rules:
                if not self._meets_threshold(rule.severity):
                    continue
                for match in rule.pattern.finditer(content):
                    line_num = content[: match.start()].count("\n") + 1
                    snippet = lines[line_num - 1].strip()
                    snippet = snippet[:200]
                    findings.append(
                        SecurityFinding(
                            file_path=rel_path_str,
                            line=line_num,
                            severity=rule.severity,
                            rule_id=rule.rule_id,
                            description=rule.description,
                            snippet=snippet,
                            cwe=rule.cwe,
                        )
                    )

        findings.sort(
            key=lambda f: (
                self.SEVERITY_ORDER.get(f.severity, 99),
                f.file_path,
                f.line,
            )
        )
        return findings

    def _validate_path(self, path: Path, root: Path) -> bool:
        """Validate path security: reject symlinks and enforce limits."""
        try:
            if path.is_symlink():
                return False
            if path.is_file():
                size_mb = path.stat().st_size / (1024.0 * 1024.0)
                if size_mb > self._config.MAX_FILE_SIZE_MB:
                    return False
            rel = path.relative_to(root)
            if any(part in self._config.IGNORE_DIRS for part in rel.parts):
                return False
            if len(rel.parts) > self._config.MAX_DIRECTORY_DEPTH:
                return False
            return True
        except OSError:
            return False

    def summary(self, findings: List[SecurityFinding]) -> str:
        """Return a concise summary string of security findings."""
        if not findings:
            return "[+] Security audit complete — no findings."
        by_severity: Dict[str, int] = {}
        for f in findings:
            by_severity[f.severity] = by_severity.get(f.severity, 0) + 1
        parts = [f"[+] Security audit: {len(findings)} finding(s)"]
        for sev in ("critical", "high", "medium", "low", "info"):
            count = by_severity.get(sev, 0)
            if count:
                parts.append(f"    {sev}: {count}")
        return "\n".join(parts)


def _compile(*patterns: str) -> re.Pattern:
    """Compile multiple patterns into a single case-insensitive regex."""
    joined = "|".join(f"(?:{p})" for p in patterns)
    return re.compile(joined, re.IGNORECASE)


def _python_rules() -> List[SecurityRule]:
    """Return security rules for Python (.py)."""
    return [
        SecurityRule(
            "PY001", "critical",
            "Command injection via os.system/os.popen or subprocess with shell=True",
            _compile(
                r"os\.system\s*\(",
                r"os\.popen\s*\(",
                r"subprocess\s*\.\s*(?:call|Popen|run|check_call|check_output)\s*\([^)]*shell\s*=\s*True",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "PY002", "critical",
            "Use of eval/exec — can lead to arbitrary code execution",
            _compile(r"\beval\s*\(", r"\bexec\s*\(", r"\bcompile\s*\("),
            "CWE-95",
        ),
        SecurityRule(
            "PY003", "high",
            "Unsafe deserialization via pickle — can execute arbitrary code",
            _compile(
                r"pickle\.loads?\s*\(",
                r"cloudpickle\.loads?\s*\(",
                r"dill\.loads?\s*\(",
            ),
            "CWE-502",
        ),
        SecurityRule(
            "PY004", "high",
            "Possible SQL injection — string concatenation or f-string in SQL query",
            _compile(
                r"""(?:execute|executemany|rawSQL|raw_query)\s*\([^)]*\+""",
                r"""(?:execute|executemany|rawSQL|raw_query)\s*\(\s*f["']""",
                r"""cursor\s*\.\s*(?:execute|executemany)\s*\([^)]*\+""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "PY005", "medium",
            "Hardcoded secret/credential detected",
            _compile(
                r"""(?:password|passwd|pwd|secret|api_key|apikey|token|auth_token)\s*[:=]\s*['\"][^'\"]+""",
            ),
            "CWE-798",
        ),
        SecurityRule(
            "PY006", "medium",
            "Weak cryptographic hash function (MD5/SHA1) used for security",
            _compile(
                r"""hashlib\.md5\s*\(""",
                r"""hashlib\.sha1\s*\(""",
            ),
            "CWE-327",
        ),
        SecurityRule(
            "PY007", "medium",
            "Path traversal risk — file operation with variable path",
            _compile(
                r"(?:open|Path)\s*\(\s*(?:os\.path\.join|f[\"']|[\"']\s*\+\s*|%[sd])",
                r"shutil\.(?:copy|move|copytree|rmtree)\s*\([^)]*[\"']\s*\+\s*",
            ),
            "CWE-22",
        ),
        SecurityRule(
            "PY008", "medium",
            "HTTP request with certificate verification disabled",
            _compile(r"""requests\.(?:get|post|put|delete|patch)\s*\([^)]*verify\s*=\s*False"""),
            "CWE-295",
        ),
        SecurityRule(
            "PY009", "medium",
            "Flask debug mode enabled — can expose debugger in production",
            _compile(r"""app\.run\s*\([^)]*debug\s*=\s*True"""),
            "CWE-489",
        ),
        SecurityRule(
            "PY010", "low",
            "Assert statement used — can be disabled with -O flag",
            _compile(r"\bassert\s+"),
            "CWE-670",
        ),
        SecurityRule(
            "PY011", "low",
            "Unsafe temporary file creation (mktemp) — race condition",
            _compile(r"tempfile\.mktemp\s*\("),
            "CWE-377",
        ),
        SecurityRule(
            "PY012", "high",
            "Unsafe yaml.load — use yaml.safe_load instead",
            _compile(r"yaml\.load\s*\((?!.*Loader)"),
            "CWE-502",
        ),
    ]


def _javascript_rules() -> List[SecurityRule]:
    """Return security rules for JavaScript/TypeScript (.js/.ts/.jsx/.tsx)."""
    return [
        SecurityRule(
            "JS001", "high",
            "XSS via innerHTML — can lead to cross-site scripting",
            _compile(r"\.innerHTML\s*=", r"\.outerHTML\s*="),
            "CWE-79",
        ),
        SecurityRule(
            "JS002", "critical",
            "Use of eval — can lead to arbitrary code execution",
            _compile(r"\beval\s*\(", r"\bsetTimeout\s*\(\s*['\"]", r"\bsetInterval\s*\(\s*['\"]"),
            "CWE-95",
        ),
        SecurityRule(
            "JS003", "high",
            "Command injection via child_process exec/spawn with shell",
            _compile(
                r"""child_process\.(?:exec|execSync|spawn|spawnSync|fork)\s*\(""",
                r"""require\(['"]child_process['"]\)""",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "JS004", "medium",
            "XSS via document.write — can lead to cross-site scripting",
            _compile(r"document\.write\s*\("),
            "CWE-79",
        ),
        SecurityRule(
            "JS005", "high",
            "Use of new Function() — similar to eval",
            _compile(r"new\s+Function\s*\("),
            "CWE-95",
        ),
        SecurityRule(
            "JS006", "high",
            "Possible SQL injection — string formatting in SQL query",
            _compile(
                r"""execute\s*\(\s*(?:f[\"']|[\"']\s*\+\s*)""",
                r"""query\s*\(\s*(?:f[\"']|[\"']\s*\+\s*)""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "JS007", "high",
            "XSS via dangerouslySetInnerHTML in React",
            _compile(r"dangerouslySetInnerHTML"),
            "CWE-79",
        ),
    ]


def _c_rules() -> List[SecurityRule]:
    """Return security rules for C/C++ (.c/.cpp/.cc/.cxx/.h/.hpp/.hxx)."""
    return [
        SecurityRule(
            "C001", "high",
            "Buffer overflow risk: strcpy — use strncpy or snprintf instead",
            _compile(r"\bstrcpy\s*\("),
            "CWE-121",
        ),
        SecurityRule(
            "C002", "high",
            "Buffer overflow risk: strcat — use strncat instead",
            _compile(r"\bstrcat\s*\("),
            "CWE-121",
        ),
        SecurityRule(
            "C003", "critical",
            "Buffer overflow risk: gets — use fgets instead",
            _compile(r"\bgets\s*\("),
            "CWE-120",
        ),
        SecurityRule(
            "C004", "high",
            "Buffer overflow risk: sprintf — use snprintf instead",
            _compile(r"\bsprintf\s*\("),
            "CWE-121",
        ),
        SecurityRule(
            "C005", "medium",
            "Unbounded input: scanf with %s — limit buffer size",
            _compile(r"\bscanf\s*\(\s*[\"'][^\"']*%s"),
            "CWE-120",
        ),
        SecurityRule(
            "C006", "high",
            "Command injection via system() — use execve instead",
            _compile(r"\bsystem\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "C007", "medium",
            "Command injection via popen() — use execve instead",
            _compile(r"\bpopen\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "C008", "medium",
            "Stack overflow risk: alloca — use heap allocation instead",
            _compile(r"\balloca\s*\("),
            "CWE-770",
        ),
    ]


def _java_rules() -> List[SecurityRule]:
    """Return security rules for Java (.java)."""
    return [
        SecurityRule(
            "J001", "high",
            "Command injection via Runtime.exec()",
            _compile(r"Runtime\s*\.\s*getRuntime\s*\(\s*\)\s*\.\s*exec\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "J002", "high",
            "Command injection via ProcessBuilder",
            _compile(r"new\s+ProcessBuilder\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "J003", "high",
            "Possible SQL injection — string concatenation in SQL",
            _compile(
                r"""executeQuery\s*\([^)]*\+""",
                r"""executeUpdate\s*\([^)]*\+""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "J004", "high",
            "Unsafe deserialization via ObjectInputStream.readObject",
            _compile(r"ObjectInputStream\s*\(.*\).*readObject"),
            "CWE-502",
        ),
        SecurityRule(
            "J005", "medium",
            "XXE risk — DocumentBuilder without external entity protection",
            _compile(r"DocumentBuilderFactory\s*\.\s*newInstance"),
            "CWE-611",
        ),
    ]


def _go_rules() -> List[SecurityRule]:
    """Return security rules for Go (.go)."""
    return [
        SecurityRule(
            "G001", "high",
            "Command injection via exec.Command",
            _compile(r"exec\.Command\s*\(", r"exec\.CommandContext\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "G002", "high",
            "Possible SQL injection — string concatenation in query",
            _compile(
                r"""\.Query\s*\(\s*(?:fmt\.Sprintf|[\"']\s*\+\s*)""",
                r"""\.Exec\s*\(\s*(?:fmt\.Sprintf|[\"']\s*\+\s*)""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "G003", "medium",
            "Unsafe use of unsafe package",
            _compile(r'"unsafe"'),
            "CWE-676",
        ),
        SecurityRule(
            "G004", "medium",
            "Potential command injection via os/exec with shell",
            _compile(r"""os/exec""", r"""os\.StartProcess"""),
            "CWE-78",
        ),
    ]


def _ruby_rules() -> List[SecurityRule]:
    """Return security rules for Ruby (.rb)."""
    return [
        SecurityRule(
            "R001", "critical",
            "Use of eval — can lead to arbitrary code execution",
            _compile(r"\beval\s*\(", r"\bclass_eval\s*\(", r"\binstance_eval\s*\("),
            "CWE-95",
        ),
        SecurityRule(
            "R002", "high",
            "Command injection via system()",
            _compile(r"\bsystem\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "R003", "high",
            "Command injection via exec()",
            _compile(r"\bexec\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "R004", "high",
            "Unsafe deserialization via Marshal.load",
            _compile(r"Marshal\.(?:load|restore)\s*\("),
            "CWE-502",
        ),
        SecurityRule(
            "R005", "high",
            "Unsafe YAML.load — use YAML.safe_load instead",
            _compile(r"YAML\.load\s*\("),
            "CWE-502",
        ),
        SecurityRule(
            "R006", "high",
            "Command injection via backtick execution",
            _compile(r"`[^`]*#\{[^}]+}"),
            "CWE-78",
        ),
    ]


def _php_rules() -> List[SecurityRule]:
    """Return security rules for PHP (.php)."""
    return [
        SecurityRule(
            "P001", "critical",
            "Use of eval — can lead to arbitrary code execution",
            _compile(r"\beval\s*\(", r"\bassert\s*\(.*['\"]"),
            "CWE-95",
        ),
        SecurityRule(
            "P002", "high",
            "Command injection via exec/system/shell_exec/passthru",
            _compile(
                r"\bexec\s*\(",
                r"\bsystem\s*\(",
                r"\bshell_exec\s*\(",
                r"\bpassthru\s*\(",
                r"\bpopen\s*\(",
                r"\bproc_open\s*\(",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "P003", "high",
            "Possible SQL injection — direct query execution",
            _compile(
                r"""mysql_query\s*\(""",
                r"""mysqli_query\s*\(""",
                r"""mysqli::query\s*\(""",
                r"""->query\s*\(\s*[\"']\s*\+\s*""",
                r"""->prepare\s*\(\s*[\"']\s*\+\s*""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "P004", "high",
            "Unsafe unserialize — can lead to arbitrary code execution",
            _compile(r"\bunserialize\s*\("),
            "CWE-502",
        ),
        SecurityRule(
            "P005", "medium",
            "XSS via direct output of user input (echo/print with $_GET/$_POST)",
            _compile(
                r"""echo\s+\$_(?:GET|POST|REQUEST|SERVER\[['\"]QUERY_STRING)""",
                r"""print\s+\$_(?:GET|POST|REQUEST)""",
            ),
            "CWE-79",
        ),
        SecurityRule(
            "P006", "medium",
            "Remote file inclusion risk — include/require with variable",
            _compile(
                r"""(?:include|require)(?:_once)?\s*\$""",
                r"""(?:include|require)(?:_once)?\s*['\"].*\{""",
            ),
            "CWE-98",
        ),
    ]


def _shell_rules() -> List[SecurityRule]:
    """Return security rules for Shell (.sh/.bash/.zsh)."""
    return [
        SecurityRule(
            "S001", "critical",
            "Command injection via eval — can execute arbitrary commands",
            _compile(r"\beval\s+\$", r"\beval\s+\""),
            "CWE-78",
        ),
        SecurityRule(
            "S002", "high",
            "Source with variable — potential arbitrary file inclusion",
            _compile(r"\bsource\s+\$", r"\.\s+\$"),
            "CWE-98",
        ),
        SecurityRule(
            "S003", "medium",
            "Command substitution with user input — potential injection",
            _compile(r"\$\([^)]*\$\{", r"`[^`]*\$\{"),
            "CWE-78",
        ),
        SecurityRule(
            "S004", "medium",
            "export/declare with variable — potential environment injection",
            _compile(r"export\s+\$"),
            "CWE-78",
        ),
    ]


def _csharp_rules() -> List[SecurityRule]:
    """Return security rules for C# (.cs)."""
    return [
        SecurityRule(
            "CS001", "high",
            "Command injection via Process.Start",
            _compile(r"Process\.Start\s*\(", r"new\s+ProcessStartInfo\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "CS002", "high",
            "Possible SQL injection — string concatenation in query",
            _compile(
                r"""ExecuteQuery\s*\(\s*[\"']\s*\+\s*""",
                r"""ExecuteCommand\s*\(\s*[\"']\s*\+\s*""",
                r"""SqlCommand\s*\(\s*[\"']\s*\+\s*""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "CS003", "high",
            "Unsafe deserialization via BinaryFormatter",
            _compile(
                r"BinaryFormatter\.Deserialize",
                r"JavaScriptSerializer\.Deserialize",
                r"SoapFormatter\.Deserialize",
                r"NetDataContractSerializer\.Deserialize",
            ),
            "CWE-502",
        ),
        SecurityRule(
            "CS004", "medium",
            "Possible XSS via Literal control or WriteLiteral",
            _compile(r"Literal\s+.*Text\s*=", r"WriteLiteral\s*\("),
            "CWE-79",
        ),
    ]


def _kotlin_rules() -> List[SecurityRule]:
    """Return security rules for Kotlin (.kt/.kts)."""
    return [
        SecurityRule(
            "K001", "high",
            "Command injection via Runtime.exec()",
            _compile(r"Runtime\.getRuntime\(\)\.exec\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "K002", "high",
            "Command injection via ProcessBuilder",
            _compile(r"ProcessBuilder\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "K003", "high",
            "Possible SQL injection — string concatenation in SQL",
            _compile(
                r"""rawQuery\s*\(\s*[\"']\s*\+\s*""",
                r"""execSQL\s*\(\s*[\"']\s*\+\s*""",
            ),
            "CWE-89",
        ),
    ]


def _swift_rules() -> List[SecurityRule]:
    """Return security rules for Swift (.swift)."""
    return [
        SecurityRule(
            "SW001", "high",
            "Command injection via Process launch path",
            _compile(r"Process\s*\(\s*\)\s*\.launchPath", r"Process\.launchPath"),
            "CWE-78",
        ),
        SecurityRule(
            "SW002", "high",
            "Possible SQL injection — string interpolation in query",
            _compile(
                r"""execute\s*\(\s*.*\\\(""",
                r"""executeUpdate\s*\(\s*.*\\\(""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "SW003", "medium",
            "Use of JSContext eval — code execution risk",
            _compile(r"JSContext\s*\(\)\s*\.evaluateScript", r"JSValue\.value"),
            "CWE-95",
        ),
    ]


def _scala_rules() -> List[SecurityRule]:
    """Return security rules for Scala (.scala/.sc)."""
    return [
        SecurityRule(
            "SC001", "high",
            "Command injection via Runtime.exec",
            _compile(r"Runtime\.getRuntime\.exec\s*\(", r"java\.lang\.Runtime\.getRuntime"),
            "CWE-78",
        ),
        SecurityRule(
            "SC002", "high",
            "Possible SQL injection — string concatenation in SQL",
            _compile(
                r"""executeQuery\s*\(\s*[\"']\s*\+\s*""",
                r"""executeUpdate\s*\(\s*[\"']\s*\+\s*""",
                r"""sql\s*=\s*[\"']\s*\+\s*""",
            ),
            "CWE-89",
        ),
        SecurityRule(
            "SC003", "high",
            "Unsafe Java deserialization via ObjectInputStream",
            _compile(r"new\s+ObjectInputStream", r"readObject\s*\("),
            "CWE-502",
        ),
    ]


def _lua_rules() -> List[SecurityRule]:
    """Return security rules for Lua (.lua)."""
    return [
        SecurityRule(
            "L001", "critical",
            "Code injection via load/loadstring — similar to eval",
            _compile(r"\bload\s*\(", r"\bloadstring\s*\("),
            "CWE-95",
        ),
        SecurityRule(
            "L002", "medium",
            "Arbitrary file read via dofile/loadfile",
            _compile(r"\bdofile\s*\(", r"\bloadfile\s*\("),
            "CWE-73",
        ),
        SecurityRule(
            "L003", "high",
            "Command injection via os.execute/io.popen",
            _compile(r"os\.execute\s*\(", r"io\.popen\s*\("),
            "CWE-78",
        ),
    ]


def _dart_rules() -> List[SecurityRule]:
    """Return security rules for Dart (.dart)."""
    return [
        SecurityRule(
            "D001", "high",
            "Command injection via Process.run/start",
            _compile(
                r"Process\.run\s*\(",
                r"Process\.start\s*\(",
                r"Process\.runSync\s*\(",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "D002", "medium",
            "Dynamic code execution via JsObject eval",
            _compile(r"JsObject\.eval", r"context\.eval"),
            "CWE-95",
        ),
        SecurityRule(
            "D003", "high",
            "Possible SQL injection — string interpolation in query",
            _compile(
                r"""\.rawQuery\s*\(\s*[\"']\s*\+\s*""",
                r"""\.query\s*\(\s*[\"']\s*\+\s*""",
                r"""\.rawInsert\s*\(\s*[\"']\s*\+\s*""",
            ),
            "CWE-89",
        ),
    ]


def _rust_rules() -> List[SecurityRule]:
    """Return security rules for Rust (.rs)."""
    return [
        SecurityRule(
            "RS001", "high",
            "Command injection via std::process::Command",
            _compile(
                r"std::process::Command::new",
                r"Command::new\s*\(",
                r"Command::from_utf8",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "RS002", "medium",
            "Unsafe block bypasses memory safety guarantees",
            _compile(r"unsafe\s*\{"),
            "CWE-676",
        ),
        SecurityRule(
            "RS003", "high",
            "Possible SQL injection — raw string in query",
            _compile(
                r"""execute\s*\(\s*[\"']\s*\+\s*""",
                r"""query\s*\(\s*[\"']\s*\+\s*""",
                r"""sql_query\s*\(\s*[\"']\s*\+\s*""",
                r"""sqlx::query\s*\(\s*[\"']\s*\+\s*""",
            ),
            "CWE-89",
        ),
    ]


def _nim_rules() -> List[SecurityRule]:
    """Return security rules for Nim (.nim)."""
    return [
        SecurityRule(
            "N001", "high",
            "Command injection via execProcess/execCmd",
            _compile(
                r"execProcess\s*\(",
                r"execCmd\s*\(",
                r"osproc\.execProcess\s*\(",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "N002", "critical",
            "Use of eval — can lead to arbitrary code execution",
            _compile(r"\beval\s*\("),
            "CWE-95",
        ),
        SecurityRule(
            "N003", "medium",
            "GcSafe violation — passing closures across FFI",
            _compile(r"\{.gcsafe.\}", r"gcsafe"),
            "CWE-676",
        ),
    ]


def _gdscript_rules() -> List[SecurityRule]:
    """Return security rules for GDScript (.gd)."""
    return [
        SecurityRule(
            "GD001", "critical",
            "Dynamic code execution via GDScript eval",
            _compile(r"\beval\s*\("),
            "CWE-95",
        ),
        SecurityRule(
            "GD002", "high",
            "Command injection via OS.execute",
            _compile(r"OS\.execute\s*\(", r"OS\.shell_open\s*\("),
            "CWE-78",
        ),
        SecurityRule(
            "GD003", "medium",
            "File path traversal via load/preload with variable",
            _compile(r"\bload\s*\(\s*\$", r"\bpreload\s*\(\s*\$"),
            "CWE-22",
        ),
    ]


def _elixir_rules() -> List[SecurityRule]:
    """Return security rules for Elixir (.ex/.exs)."""
    return [
        SecurityRule(
            "E001", "critical",
            "Dynamic code execution via Code.eval_string",
            _compile(
                r"Code\.eval_string\s*\(",
                r"Code\.eval_quoted\s*\(",
                r"Code\.string_to_quoted\s*\(",
            ),
            "CWE-95",
        ),
        SecurityRule(
            "E002", "high",
            "Command injection via System.cmd/System.shell",
            _compile(
                r"System\.cmd\s*\(",
                r"System\.shell\s*\(",
                r"Porcelain\.exec\s*\(",
            ),
            "CWE-78",
        ),
        SecurityRule(
            "E003", "high",
            "Possible SQL injection — string interpolation in Ecto query",
            _compile(
                r"""Ecto\.Adapters\.SQL\.query\s*\(\s*.*\#\{""",
                r"""Repo\.query\s*\(\s*[\"']\s*<>\s*""",
            ),
            "CWE-89",
        ),
    ]
