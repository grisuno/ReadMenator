"""Immutable configuration dataclass for readmenator.

All tuneable parameters live here as frozen dataclass fields. No magic
numbers or hardcoded paths exist elsewhere in the codebase. Derived
consumers import Config and read values from an instance.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Config:
    """Single source of truth for all readmenator settings.

    Every tuneable constant -- file-size limits, directory depth,
    supported extensions, symbol pluralisation map, Mermaid style
    tokens, graph analysis thresholds, and export settings -- is
    defined here and consumed by reference elsewhere.
    """

    IGNORE_DIRS: Tuple[str, ...] = (
        ".git", "__pycache__", "venv", ".venv", "env", ".env", "node_modules",
        ".tox", ".eggs", ".pytest_cache", "build", "dist", ".idea", ".vscode",
        "target", "bin", "obj", "out", "vendor", "third_party", "deps",
        "third-party", "thirdparty", ".m2", ".gradle", ".nuget", "packages",
        "Pods", ".dart_tool", ".pub-cache", "bower_components", ".yarn",
        "Carthage", "node_packages", ".meteor", ".gitlab", ".github",
        "htmlcov", ".coverage", "__pycache__",
    )

    OUTPUT_FILENAME: str = "KNOWLEDGE_BASE.md"

    MAX_FILE_SIZE_MB: float = 10.0

    MAX_DIRECTORY_DEPTH: int = 20

    DOCSTRING_LOOKBACK_LINES: int = 15

    FILE_HEADER_MAX_LINES: int = 30

    MERMAID_MAX_NODES: int = 300

    MERMAID_MAX_SYMBOLS_PER_FILE: int = 5

    MERMAID_MODULE_STYLE: str = "fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff"

    MERMAID_CLASS_STYLE: str = "fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff"

    MERMAID_FUNCTION_STYLE: str = "fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa"

    MERMAID_EXTERNAL_STYLE: str = "fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa"

    MERMAID_INTERNAL_EDGE_STYLE: str = "stroke:#88aaff,stroke-width:1px"

    SUPPORTED_EXTENSIONS: Tuple[str, ...] = (
        ".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hxx",
        ".py", ".go", ".rs",
        ".js", ".ts", ".jsx", ".tsx",
        ".java", ".cs",
        ".sh", ".bash", ".zsh",
        ".php", ".dart", ".gd", ".nim",
        ".asm", ".s", ".S",
        ".rb", ".swift", ".kt", ".kts", ".scala", ".sc",
        ".lua", ".ex", ".exs",
    )

    SYMBOL_TYPE_PLURALS: Tuple[Tuple[str, str], ...] = (
        ("class", "classes"),
        ("struct", "structs"),
        ("function", "functions"),
        ("method", "methods"),
        ("macro", "macros"),
        ("trait", "traits"),
        ("enum", "enums"),
        ("interface", "interfaces"),
        ("record", "records"),
        ("variable", "variables"),
        ("constant", "constants"),
        ("type_alias", "type_aliases"),
        ("module", "modules"),
        ("protocol", "protocols"),
        ("extension", "extensions"),
    )

    COMMUNITY_MIN_SIZE: int = 2

    COMMUNITY_MAX_SIZE_RATIO: float = 0.25

    GOD_NODE_TOP_N: int = 10

    SURPRISING_CONNECTION_HOP_THRESHOLD: int = 3

    SURPRISING_CONNECTION_TOP_N: int = 5

    SUGGESTED_QUESTIONS_COUNT: int = 5

    CACHE_DIR: str = ".readmenator_cache"

    HTML_TEMPLATE_STYLE: str = "dark"

    SVG_DPI: int = 150

    SVG_MAX_NODES: int = 200

    PROGRESS_REPORT_BATCH: int = 50

    SECURITY_ENABLED: bool = False

    SECURITY_SEVERITY_THRESHOLD: str = "medium"

    SECURITY_OUTPUT: str = "KNOWLEDGE_BASE.md"

    CPG_ENABLED: bool = True

    CPG_EMBED_IN_KNOWLEDGE_BASE: bool = True

    TAINT_ENABLED: bool = True

    TAINT_MAX_DEPTH: int = 10

    TAINT_MAX_PATHS: int = 20

    SARIF_ENABLED: bool = False

    SARIF_OUTPUT: str = "readmenator_audit.sarif"

    HOTSPOTS_ENABLED: bool = True

    HOTSPOT_COMPLEXITY_WEIGHT: float = 0.4

    HOTSPOT_CENTRALITY_WEIGHT: float = 0.6

    CYCLE_DETECTION_ENABLED: bool = True

    CHANGE_IMPACT_MAX_DEPTH: int = 10

    CHANGE_IMPACT_MAX_FILES: int = 50

    RULE_GEN_ENABLED: bool = True

    RULE_GEN_MIN_PATTERN_COUNT: int = 3

    RULE_GEN_OUTPUT_DIR: str = "readmenator-rules"

    LAYER_VIOLATION_ENABLED: bool = True

    LAYER_VIOLATION_STRICT_MODE: bool = False

    PRIVACY_MODE: bool = False

    GITIGNORE_AWARE: bool = True
