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

    CPG_CONTEXT: str = ""

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

    CONTEXT_BUDGET: int = 0

    RANKING_ENABLED: bool = True

    RANKING_ALPHA: float = 0.85

    RANKING_MAX_ITER: int = 100

    RANKING_TOLERANCE: float = 1e-6

    RANKING_TOP_N: int = 10

    RANKING_NOISE_PENALTY: float = 0.7

    RANKING_PPR_WEIGHT: float = 0.45

    RANKING_AUTHORITY_WEIGHT: float = 0.20

    RANKING_TEST_WEIGHT: float = 0.15

    RANKING_DOC_WEIGHT: float = 0.10

    RANKING_FRESHNESS_WEIGHT: float = 0.10

    UML_ENABLED: bool = True

    UML_MAX_CLASSES: int = 50

    UML_GENERATED_LANGUAGES: Tuple[str, ...] = (
        "cpp", "java", "csharp", "python", "go", "rust",
        "php", "kotlin", "scala", "swift", "dart", "ruby",
    )

    README_INJECTION_ENABLED: bool = True

    LINTER_ENABLED: bool = True

    LINTER_MAX_LINES: int = 300

    LINTER_CROSS_LAYER_VIOLATIONS: bool = True

    DEAD_CODE_ENABLED: bool = True

    DEAD_CODE_ENTRY_POINTS: Tuple[str, ...] = ("main", "app", "index", "__init__")

    DEAD_CODE_QUARANTINE_DIR: str = ".readmenator_trash"

    CURSORRULES_ENABLED: bool = True

    CURSORRULES_OUTPUT: str = ".cursorrules"

    REFACTORIZER_ENABLED: bool = True

    REFACTORIZER_MIN_LINES: int = 300

    REFACTORIZER_MAX_FILES: int = 10

    AGENT_INJECTION_ENABLED: bool = True

    AGENT_INJECTION_KB_FILENAME: str = "KNOWLEDGE_BASE.md"

    AGENT_OUTPUT_ENABLED: bool = True

    AGENT_OUTPUT_DIR: str = "readmenator-agent"

    AGENT_OUTPUT_MIN_SUBSYSTEM_FILES: int = 2

    DIAGRAM_ENABLED: bool = True

    DIAGRAM_MAX_NODES: int = 60

    DIAGRAM_MAX_EDGES: int = 120

    DIAGRAM_NODE_WIDTH: int = 190

    DIAGRAM_NODE_HEIGHT: int = 64

    DIAGRAM_COLUMN_GAP: int = 90

    DIAGRAM_ROW_GAP: int = 48

    DIAGRAM_CANVAS_WIDTH: int = 1280

    DIAGRAM_CANVAS_HEIGHT: int = 760

    DIAGRAM_PRESET: str = "classic"

    DIAGRAM_THEME: str = "dark"

    DIAGRAM_OUTPUT_DIR: str = "readmenator-maps"

    DIAGRAM_PAGES_DIR: str = "docs"

    DIAGRAM_MAPS_SUBDIR: str = "maps"

    DIAGRAM_VIS_ENABLED: bool = True

    DIAGRAM_VIS_CDN_JS: str = "https://unpkg.com/vis-network@9/standalone/umd/vis-network.min.js"

    DIAGRAM_VIS_CDN_CSS: str = "https://unpkg.com/vis-network@9/styles/vis-network.min.css"

    DIAGRAM_VIS_PHYSICS_ENABLED: bool = True

    DIAGRAM_VIS_STABILIZE_ITERATIONS: int = 250

    DIAGRAM_MOTION_ENABLED: bool = True

    DIAGRAM_SHARE_WIDTH: int = 1200

    DIAGRAM_SHARE_HEIGHT: int = 630

    DIAGRAM_MAX_VIEWS: int = 5

    DIAGRAM_MAX_LABEL_CHARS: int = 28

    DIAGRAM_MARGIN_X: int = 40

    DIAGRAM_MARGIN_Y: int = 40

    DIAGRAM_MIN_GAP: int = 12

    DIAGRAM_LANE_TOP: int = 90

    DIAGRAM_SEQUENCE_TOP: int = 110

    DIAGRAM_SEQUENCE_MAX_PARTICIPANTS: int = 8

    DIAGRAM_WORKFLOW_FALLBACK_NODES: int = 4

    DIAGRAM_CHAPTER_FOCUS: int = 6

    DIAGRAM_MAP_SYMBOLS_PER_NODE: int = 25

    DIAGRAM_TOOLTIP_DOC_CHARS: int = 160

    DIAGRAM_NEIGHBOR_NAMES: int = 8

    DIAGRAM_PRESETS: Tuple[str, ...] = (
        "classic", "flow", "blueprint", "editorial",
    )

    DIAGRAM_KINDS: Tuple[str, ...] = (
        "architecture", "workflow", "sequence", "dataflow", "lifecycle",
    )

    DIAGRAM_ROLES: Tuple[str, ...] = (
        "frontend", "backend", "database", "cloud",
        "security", "messagebus", "external",
    )

    DIAGRAM_ROLE_COLORS: Tuple[Tuple[str, str], ...] = (
        ("frontend", "#22d3ee"),
        ("backend", "#34d399"),
        ("database", "#a78bfa"),
        ("cloud", "#fbbf24"),
        ("security", "#fb7185"),
        ("messagebus", "#fb923c"),
        ("external", "#94a3b8"),
    )
