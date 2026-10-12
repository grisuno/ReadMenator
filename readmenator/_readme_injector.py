"""Injects a knowledge base section into the project README (Markdown or RST)."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

_ANCHOR_START = "<!-- readmenator-kb-link -->"
_ANCHOR_END = "<!-- /readmenator-kb-link -->"

_INJECTION_TEXT_MD = """{anchor_start}
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Regenerate with
`pip install readmenator && readmenator . --rebuild`. Analysis outputs:

- **[{kb_filename}](./{kb_filename})** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, taint paths, hotspots, cycles, and more.
- **[{agent_output_dir}/](./{agent_output_dir}/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `SYMBOLS.md` -- Every symbol with file:line
  - `ARCHITECTURE.md` -- Internal dependency pairs + external imports
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings (blast radius, cycles, hotspots)
  - `SECURITY.md` -- Findings by severity with fix hints
  - `MEMORY.md` -- Rules, workflow, style, deliverables, session log
  - `MANIFEST.json` -- Freshness (git_commit + source_fingerprint) + read order
  - `KB_<subsystem>.md` -- Per-subsystem context
  - `recipes/*.md` -- Grounded task guides (add-function, fix-cycle, ...)
- **[{wiki_output_dir}/](./{wiki_output_dir}/)** -- Navigable wiki (start here for the big picture).
  - `index.md` -- Entry point: overview, reading order, god nodes, connections
  - `community_*.md` -- One synthesis page per code community
  - `connections.json` -- Typed bridges between communities
  - `queries.md` -- Suggested questions + answer log
  - `REPORT.md` -- Honest audit: coverage, confidence, limits
- **[{graphrag_output_dir}/](./{graphrag_output_dir}/)** -- Zero-token GraphRAG index.
  - `index.json` + `REPORTS.md` -- Query with `readmenator . ask "<question>"`
- **[{apidocs_output_dir}/](./{apidocs_output_dir}/)** -- API reference (Sphinx/Doxygen style).
  - `index.md` + `modules/*.md` -- Signatures, parameters, returns, raises, examples, call graphs
  - `architecture.md` -- Tiered architecture + execution flows (control flow, call tree, sequence)
  - `classes.md`, `genindex.md`, `COVERAGE.md` -- Hierarchy, A-Z index, doc coverage + warnings
  - `index.html` + `api.json` -- Offline searchable browser and machine-readable model
- **[{maps_output_dir}/](./{maps_output_dir}/)** -- Interactive gallery (`index.html`).
  - 5 system maps: architecture, workflow, sequence, dataflow, lifecycle
  - `{forcegraph_output}` -- Force-graph explorer (2D/3D, reach, paths, lenses)
  - `{bundlegraph_output}` -- Edge bundle explorer (circle + sphere)
  - `components.html` -- Component diagrams
- **[{pages_dir}/](./{pages_dir}/)** -- Static site (GitHub Pages ready).
  - Gallery copy + `{llms_txt}` (agent entry point) + `md/` docs + video
- **[{components_output_dir}/](./{components_output_dir}/)** -- Component diagrams.
  - `analysis.json` + `graph LR` markdown + per-component pages + `index.html`
- **[{rules_output_dir}/](./{rules_output_dir}/)** -- Suggested Semgrep rules (`*.yml`),
  `yara_rules.yar` (YARA-lite) + `exclusions.yaml` (false-positive blocklist)
- **[{video_output}](./{video_output})** -- Cinematic synthwave overview video
- **[{cursorrules_output}](./{cursorrules_output})** -- Generated AI assistant rules
- **[{sarif_output}](./{sarif_output})** -- SARIF v2.1.0 audit (when security scan is on)

Cache (`{cache_dir}/`), packaged agent skills (`{skills_dir}/`), and the
GitHub wiki mirror are also produced on `run`/`--rebuild`.

AI agents: Read `{wiki_output_dir}/index.md` first for the big picture, then `{agent_output_dir}/INDEX.md` for grep-friendly lookup.
Developers: Read `{kb_filename}` for full architecture reference, open `{maps_output_dir}/index.html` for the visual gallery.
{anchor_end}
"""

_INJECTION_TEXT_RST = """{anchor_start}
Knowledge Base
--------------

This project has been analyzed by `ReadMenator <https://github.com/grisuno/ReadMenator>`_,
a zero-token polyglot static analysis tool. Regenerate with
``pip install readmenator && readmenator . --rebuild``. Analysis outputs:

- **{kb_filename}** -- Full architecture reference with all classes, functions,
  imports, dependency graphs, UML class diagrams, security audit findings,
  community analysis, taint paths, hotspots, cycles, and more.
- **{agent_output_dir}/** -- Agent-friendly, grep-optimized index.

  - ``INDEX.md`` -- Quick reference: what each file does
  - ``SYMBOLS.md`` -- Every symbol with file:line
  - ``ARCHITECTURE.md`` -- Internal dependency pairs + external imports
  - ``API.md`` -- Public function contracts
  - ``GOTCHAS.md`` -- Change warnings
  - ``SECURITY.md`` -- Findings by severity
  - ``MEMORY.md`` -- Rules, workflow, style, session log
  - ``MANIFEST.json`` -- Freshness + read order
  - ``KB_<subsystem>.md`` -- Per-subsystem context
  - ``recipes/*.md`` -- Grounded task guides
- **{wiki_output_dir}/** -- Navigable wiki (start here for the big picture).

  - ``index.md`` -- Entry point: overview, reading order, god nodes
  - ``community_*.md`` -- One synthesis page per code community
  - ``REPORT.md`` -- Honest audit: coverage, confidence, limits
- **{graphrag_output_dir}/** -- Zero-token GraphRAG index (``readmenator . ask``).
- **{apidocs_output_dir}/** -- API reference (``index.md``, ``modules/``, ``architecture.md``,
  ``COVERAGE.md``, offline ``index.html``, ``api.json``).
- **{maps_output_dir}/** -- Interactive gallery (``index.html``): 5 system maps,
  ``{forcegraph_output}``, ``{bundlegraph_output}``, ``components.html``.
- **{pages_dir}/** -- Static site (gallery copy + ``{llms_txt}`` + video).
- **{components_output_dir}/** -- Component diagrams (``analysis.json`` + markdown).
- **{rules_output_dir}/** -- Semgrep rules + ``yara_rules.yar`` + ``exclusions.yaml``.
- **{video_output}** -- Cinematic overview video.
- **{cursorrules_output}** -- Generated AI assistant rules.
- **{sarif_output}** -- SARIF audit (when security scan is on).

AI agents: Read ``{wiki_output_dir}/index.md`` first, then ``{agent_output_dir}/INDEX.md``.
Developers: Read ``{kb_filename}`` for full architecture reference.
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

    When the anchor tag is missing the section is created; when the tag
    exists but the text is outdated it is replaced in place.
    """

    def __init__(
        self,
        kb_filename: str = "KNOWLEDGE_BASE.md",
        agent_output_dir: str = "readmenator-agent",
        wiki_output_dir: str = "readmenator-wiki",
        graphrag_output_dir: str = "readmenator-graphrag",
        maps_output_dir: str = "readmenator-maps",
        pages_dir: str = "docs",
        components_output_dir: str = "readmenator-diagrams",
        rules_output_dir: str = "readmenator-rules",
        video_output: str = "readmenator.mp4",
        cursorrules_output: str = ".cursorrules",
        sarif_output: str = "readmenator_audit.sarif",
        cache_dir: str = ".readmenator_cache",
        skills_dir: str = ".claude/skills",
        llms_txt: str = "llms.txt",
        forcegraph_output: str = "graph-force.html",
        bundlegraph_output: str = "graph-bundle.html",
        apidocs_output_dir: str = "readmenator-apidocs",
    ) -> None:
        """Initialise the injector with output locations.

        Args:
            kb_filename: Knowledge base filename.
            agent_output_dir: Agent output directory.
            wiki_output_dir: Wiki output directory.
            graphrag_output_dir: GraphRAG output directory.
            maps_output_dir: Interactive maps output directory.
            pages_dir: Static site output directory.
            components_output_dir: Component diagram output directory.
            rules_output_dir: Suggested rules output directory.
            video_output: Overview video filename.
            cursorrules_output: Generated cursor rules filename.
            sarif_output: SARIF audit filename.
            cache_dir: Incremental cache directory.
            skills_dir: Packaged agent skills target directory.
            llms_txt: Site llms.txt filename.
            forcegraph_output: Force-graph explorer filename.
            bundlegraph_output: Edge bundle explorer filename.
            apidocs_output_dir: API reference output directory.
        """
        self._kb_filename = kb_filename
        self._agent_output_dir = agent_output_dir
        self._wiki_output_dir = wiki_output_dir
        self._graphrag_output_dir = graphrag_output_dir
        self._maps_output_dir = maps_output_dir
        self._pages_dir = pages_dir
        self._components_output_dir = components_output_dir
        self._rules_output_dir = rules_output_dir
        self._video_output = video_output
        self._cursorrules_output = cursorrules_output
        self._sarif_output = sarif_output
        self._cache_dir = cache_dir
        self._skills_dir = skills_dir
        self._llms_txt = llms_txt
        self._forcegraph_output = forcegraph_output
        self._bundlegraph_output = bundlegraph_output
        self._apidocs_output_dir = apidocs_output_dir

    def inject(self, project_root: str) -> bool:
        """Inject or refresh the knowledge base section in the README.

        Args:
            project_root: Project root directory holding the README.

        Returns:
            True when the README was created or modified, False otherwise.
        """
        root = Path(project_root).resolve()
        readme_path = self._find_readme(root)
        if readme_path is None:
            logger.debug("No README file found in %s, skipping injection", root)
            return False

        content = readme_path.read_text(encoding="utf-8", errors="replace")
        injection = self._build_injection(readme_path.suffix.lower())
        has_start = _ANCHOR_START in content
        has_end = _ANCHOR_END in content

        if has_start and has_end:
            current = self._extract_current_injection(content)
            if current.strip() == injection.strip():
                logger.debug("Injection already up to date in %s", readme_path.name)
                return False
            content = self._remove_old_injection(content)
            new_content = content.rstrip("\n") + "\n\n" + injection + "\n"
            readme_path.write_text(new_content, encoding="utf-8")
            logger.info("Updated knowledge base link in %s", readme_path.name)
            return True

        if has_start or has_end:
            content = self._strip_partial_anchor(content)
        new_content = content.rstrip("\n") + "\n\n" + injection + "\n"
        readme_path.write_text(new_content, encoding="utf-8")
        logger.info(
            "Injected knowledge base link into %s", readme_path.name
        )
        return True

    @staticmethod
    def _extract_current_injection(content: str) -> str:
        """Return the current anchored injection block.

        Args:
            content: README text.

        Returns:
            Anchored block including both markers, or empty string.
        """
        start_idx = content.find(_ANCHOR_START)
        end_idx = content.find(_ANCHOR_END)
        if start_idx < 0 or end_idx < 0:
            return ""
        end_idx += len(_ANCHOR_END)
        return content[start_idx:end_idx]

    @staticmethod
    def _remove_old_injection(content: str) -> str:
        """Remove a complete anchored injection block.

        Args:
            content: README text.

        Returns:
            Text without the anchored block.
        """
        start_idx = content.find(_ANCHOR_START)
        end_idx = content.find(_ANCHOR_END)
        if start_idx < 0 or end_idx < 0:
            return content
        end_idx += len(_ANCHOR_END)
        before = content[:start_idx].rstrip("\n")
        after = content[end_idx:].lstrip("\n")
        return before + ("\n" + after if after else "")

    @staticmethod
    def _strip_partial_anchor(content: str) -> str:
        """Remove a broken half-anchor so a fresh tag can be created.

        Args:
            content: README text with only one of the two markers.

        Returns:
            Text with the stray marker line removed.
        """
        for marker in (_ANCHOR_START, _ANCHOR_END):
            if marker in content:
                content = content.replace(marker, "")
        lines = [line for line in content.splitlines() if line.strip()]
        return "\n".join(lines) + ("\n" if content.endswith("\n") else "")

    def remove(self, project_root: str) -> bool:
        """Remove the injected section from the README.

        Args:
            project_root: Project root directory holding the README.

        Returns:
            True when a section was removed, False otherwise.
        """
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
        """Return the first README candidate present in the directory.

        Args:
            root: Project root directory.

        Returns:
            README path or None when no candidate exists.
        """
        for name in _README_CANDIDATES:
            path = root / name
            if path.is_file():
                return path
        return None

    def _build_injection(self, suffix: str) -> str:
        """Build the injection text for a README suffix.

        Args:
            suffix: Lowercase file suffix (``.rst`` selects RST).

        Returns:
            Injection block with all output locations filled in.
        """
        kwargs = dict(
            anchor_start=_ANCHOR_START,
            anchor_end=_ANCHOR_END,
            kb_filename=self._kb_filename,
            agent_output_dir=self._agent_output_dir,
            wiki_output_dir=self._wiki_output_dir,
            graphrag_output_dir=self._graphrag_output_dir,
            maps_output_dir=self._maps_output_dir,
            pages_dir=self._pages_dir,
            components_output_dir=self._components_output_dir,
            rules_output_dir=self._rules_output_dir,
            video_output=self._video_output,
            cursorrules_output=self._cursorrules_output,
            sarif_output=self._sarif_output,
            cache_dir=self._cache_dir,
            skills_dir=self._skills_dir,
            llms_txt=self._llms_txt,
            forcegraph_output=self._forcegraph_output,
            bundlegraph_output=self._bundlegraph_output,
            apidocs_output_dir=self._apidocs_output_dir,
        )
        if suffix == ".rst":
            return _INJECTION_TEXT_RST.format(**kwargs)
        return _INJECTION_TEXT_MD.format(**kwargs)
