"""Installs the packaged ReadMenator agent skills into a project.

Skills follow the Agent Skills layout (``<name>/SKILL.md`` with YAML
frontmatter) used by Claude Code and compatible agents. Only the
``readmenator-*`` skill directories shipped in ``readmenator/_skills`` are
written; any other skill in the target directory is left untouched.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional

from readmenator._config import Config

logger = logging.getLogger(__name__)

SKILL_PREFIX = "readmenator-"


class SkillInstaller:
    """Copies packaged skills into ``SKILLS_TARGET_DIR`` (idempotent)."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: SKILLS_* settings.
        """
        self._config = config

    @staticmethod
    def source_dir() -> Path:
        """Return the packaged skills directory."""
        return Path(__file__).resolve().parent / "_skills"

    def available(self) -> List[str]:
        """Return the names of the packaged skills, sorted."""
        base = self.source_dir()
        if not base.is_dir():
            return []
        return sorted(
            p.name for p in base.iterdir()
            if p.is_dir() and p.name.startswith(SKILL_PREFIX) and (p / "SKILL.md").is_file()
        )

    def target_dir(self, project_root: str, target: Optional[str] = None) -> Path:
        """Resolve the destination skills directory.

        Args:
            project_root: Project root directory.
            target: Optional explicit directory (relative to the project root when not absolute).

        Returns:
            Destination directory path.
        """
        raw = Path(target) if target else Path(self._config.SKILLS_TARGET_DIR)
        return raw if raw.is_absolute() else Path(project_root).resolve() / raw

    def install(self, project_root: str, target: Optional[str] = None) -> List[Path]:
        """Write every packaged skill whose content changed.

        Args:
            project_root: Project root directory.
            target: Optional explicit destination directory.

        Returns:
            Paths of SKILL.md files written in this call.
        """
        dest_root = self.target_dir(project_root, target)
        written: List[Path] = []
        for name in self.available():
            source = self.source_dir() / name / "SKILL.md"
            dest = dest_root / name / "SKILL.md"
            if dest.is_symlink() or dest.parent.is_symlink():
                logger.warning("Skipping skill %s: destination is a symlink", name)
                continue
            content = source.read_text(encoding="utf-8")
            if dest.is_file() and dest.read_text(encoding="utf-8") == content:
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
            written.append(dest)
        return written

    def maybe_install_on_run(self, project_root: str) -> List[Path]:
        """Install during run() only when the project already uses agent skills.

        The default target is written only when its parent directory (for
        example ``.claude/``) already exists, so plain projects never gain a
        new hidden directory.

        Args:
            project_root: Project root directory.

        Returns:
            Paths written, empty when skipped.
        """
        cfg = self._config
        if not (cfg.SKILLS_ENABLED and cfg.SKILLS_INSTALL_ON_RUN):
            return []
        if not self.target_dir(project_root).parent.is_dir():
            return []
        return self.install(project_root)
