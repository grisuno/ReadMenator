from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)

_ANCHOR_START = "<!-- readmenator-kb-link -->"
_ANCHOR_END = "<!-- /readmenator-kb-link -->"

_INJECTION_TEXT_MD = """{anchor_start}
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. A comprehensive knowledge base is available:

- **[{kb_filename}](./{kb_filename})** -- Architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.

AI agents and developers: Read `{kb_filename}` for full project context
without LLM token cost.
{anchor_end}
"""

_INJECTION_TEXT_RST = """{anchor_start}
Knowledge Base
--------------

This project has been analyzed by `ReadMenator <https://github.com/grisuno/ReadMenator>`_,
a zero-token polyglot static analysis tool. A comprehensive knowledge base is available:

- **{kb_filename}** -- Architecture reference with all classes, functions,
  imports, dependency graphs, UML class diagrams, security audit findings,
  community analysis, and more.

AI agents and developers: Read `{kb_filename}` for full project context
without LLM token cost.
{anchor_end}
"""

_README_CANDIDATES = (
    "README.md", "README.rst", "Readme.md", "readme.md", "README.txt",
    "README", "README.markdown", "README.mdown",
)


class ReadmeInjector:
    """Injects a link to KNOWLEDGE_BASE.md into the project README.

    Detects the project's README file, checks if injection is already
    present, and appends a descriptive section about the knowledge base
    so that both human developers and AI agents know it exists.
    """

    def __init__(self, kb_filename: str = "KNOWLEDGE_BASE.md") -> None:
        self._kb_filename = kb_filename

    def inject(self, project_root: str) -> bool:
        root = Path(project_root).resolve()
        readme_path = self._find_readme(root)
        if readme_path is None:
            logger.debug("No README file found in %s, skipping injection", root)
            return False

        content = readme_path.read_text(encoding="utf-8", errors="replace")

        if _ANCHOR_START in content and _ANCHOR_END in content:
            logger.debug("Injection already present in %s", readme_path.name)
            return False

        injection = self._build_injection(readme_path.suffix.lower())
        new_content = content.rstrip("\n") + "\n\n" + injection + "\n"

        readme_path.write_text(new_content, encoding="utf-8")
        logger.info(
            "Injected knowledge base link into %s", readme_path.name
        )
        return True

    def remove(self, project_root: str) -> bool:
        root = Path(project_root).resolve()
        readme_path = self._find_readme(root)
        if readme_path is None:
            return False

        content = readme_path.read_text(encoding="utf-8", errors="replace")

        if _ANCHOR_START not in content:
            return False

        start_idx = content.find(_ANCHOR_START)
        end_idx = content.find(_ANCHOR_END)
        if end_idx < 0:
            return False

        end_idx += len(_ANCHOR_END)
        before = content[:start_idx].rstrip("\n")
        after = content[end_idx:].lstrip("\n")

        new_content = before + "\n" + after if after else before
        readme_path.write_text(new_content, encoding="utf-8")

        logger.info(
            "Removed knowledge base injection from %s", readme_path.name
        )
        return True

    @staticmethod
    def _find_readme(root: Path) -> Optional[Path]:
        for name in _README_CANDIDATES:
            path = root / name
            if path.is_file():
                return path
        return None

    def _build_injection(self, suffix: str) -> str:
        if suffix == ".rst":
            return _INJECTION_TEXT_RST.format(
                anchor_start=_ANCHOR_START,
                anchor_end=_ANCHOR_END,
                kb_filename=self._kb_filename,
            )
        return _INJECTION_TEXT_MD.format(
            anchor_start=_ANCHOR_START,
            anchor_end=_ANCHOR_END,
            kb_filename=self._kb_filename,
        )
