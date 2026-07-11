from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class Config:
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

    DOCSTRING_MAX_LENGTH: int = 150

    MERMAID_MAX_NODES: int = 300

    MERMAID_MODULE_STYLE: str = "fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff"

    MERMAID_CLASS_STYLE: str = "fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff"

    MERMAID_FUNCTION_STYLE: str = "fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa"

    MERMAID_EXTERNAL_STYLE: str = "fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa"

    SUPPORTED_EXTENSIONS: Tuple[str, ...] = (
        ".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hxx",
        ".py", ".go", ".rs",
        ".js", ".ts", ".jsx", ".tsx",
        ".java", ".cs",
        ".sh", ".bash", ".zsh",
        ".php", ".dart", ".gd", ".nim",
        ".asm", ".s", ".S",
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
