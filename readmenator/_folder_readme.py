"""Per-folder README.md files for every generated readmenator-* directory.

Each output folder gets a README explaining what the folder is for, what
every file in it is (only entries that actually exist are listed), how
humans and agents use it, and how to regenerate it. Files carry
FOLDER_README_MARKER on their first line; a README without the marker is
the user's own and is never overwritten. Consumers that glob Markdown
(site docs, GitHub wiki, agent inventory, component pruning) skip
generated folder READMEs through is_generated_folder_readme.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from readmenator._config import Config

logger = logging.getLogger(__name__)

MARKER_SCAN_BYTES = 512


@dataclass(frozen=True)
class FolderSpec:
    """Description of one generated output folder.

    Attributes:
        dirname: Folder name relative to the project root.
        purpose: One paragraph stating what the folder is for.
        entries: (glob pattern, description) pairs; only matching entries are listed.
        usage: Bullet lines telling humans and agents how to use the folder.
        regenerate: Shell commands that rebuild the folder.
    """

    dirname: str
    purpose: str
    entries: Tuple[Tuple[str, str], ...]
    usage: Tuple[str, ...]
    regenerate: Tuple[str, ...]


def is_generated_folder_readme(path: Path, config: Config) -> bool:
    """Return True when path is a README written by FolderReadmeWriter.

    Args:
        path: Candidate file path.
        config: Application configuration.

    Returns:
        True for a regular file named FOLDER_README_FILENAME whose head holds the marker.
    """
    if path.name != config.FOLDER_README_FILENAME or path.is_symlink() or not path.is_file():
        return False
    try:
        with path.open("rb") as handle:
            head = handle.read(MARKER_SCAN_BYTES)
    except OSError:
        return False
    return config.FOLDER_README_MARKER.encode("utf-8") in head


class FolderReadmeWriter:
    """Writes README.md into each generated readmenator-* folder that exists."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings naming every output folder and file.
        """
        self._config = config

    def specs(self) -> List[FolderSpec]:
        """Return the folder descriptions built from Config names.

        Returns:
            One FolderSpec per generated output folder, in reading order.
        """
        cfg = self._config
        agent = cfg.AGENT_OUTPUT_DIR
        api = cfg.APIDOCS_JSONL_DIR
        return [
            FolderSpec(
                dirname=agent,
                purpose=(
                    "Agent docs: flat, grep-optimized Markdown written for AI coding agents "
                    "(and humans in a hurry). Every line is self-contained so a single grep "
                    "answers where a symbol lives, who imports a file, and what is risky to touch."
                ),
                entries=(
                    ("MEMORY.md", "Project memory: purpose, workflow commands, declared rules with file:line, style, done criteria, risks, preserved session log"),
                    ("MANIFEST.json", "Freshness stamp (git commit, source fingerprint), subsystems, entry points, read order, document inventory"),
                    ("INDEX*.md", "One row per file: purpose, subsystem, symbol count, importers"),
                    ("SYMBOLS*.md", "One line per symbol with kind and file:line"),
                    ("API*.md", "One line per public function or method with signature and first doc sentence"),
                    ("ARCHITECTURE*.md", "Internal dependency pairs and external imports per file"),
                    ("GOTCHAS*.md", "God nodes, blast radius, hotspots, cycles, layer violations, dataflow leads"),
                    ("SECURITY*.md", "Security findings by severity with CWE and fix hints"),
                    ("CONCEPTS*.md", "Semantic concept vocabulary (nouns and verbs of the codebase)"),
                    ("KB_*.md", "One knowledge page per subsystem (directory)"),
                    ("recipes", "Grounded task recipes: add a function, change impact, fix a cycle, fix security, reduce complexity"),
                ),
                usage=(
                    f"Start with `cat {agent}/MEMORY.md`, then check freshness with `readmenator . fresh`.",
                    f"Locate before reading sources: `grep -n '<keyword>' {agent}/INDEX*.md {agent}/SYMBOLS*.md`.",
                    f"Before editing a file: `grep -n '<file>' {agent}/GOTCHAS*.md {agent}/SECURITY*.md`.",
                    "Large documents are paged as `NAME_p2.md`; always grep with `NAME*.md`.",
                ),
                regenerate=("readmenator . --rebuild",),
            ),
            FolderSpec(
                dirname=cfg.WIKI_OUTPUT_DIR,
                purpose=(
                    "Agent wiki: the big picture as a navigable, progressively disclosed wiki. "
                    "One page per code community (group of files that import each other), plus "
                    "typed connections between them and an honest audit of what was extracted vs inferred."
                ),
                entries=(
                    ("index.md", "Entry point: overview, stats, reading order, god nodes, strongest connections"),
                    ("community_*.md", "One page per community: definition, files, key symbols, edges, risks, open questions"),
                    ("connections.json", "Typed bridges between communities with confidence and strength"),
                    ("concepts.md", "Concept graph summary"),
                    ("concept_graph.json", "Concept graph data (nouns as nodes, verbs as edges)"),
                    ("queries.md", "Suggested questions plus an append-only answer log"),
                    ("REPORT.md", "Audit: EXTRACTED vs INFERRED vs AMBIGUOUS counts, coverage, orphans, limits"),
                ),
                usage=(
                    f"Read `{cfg.WIKI_OUTPUT_DIR}/index.md` first, then open the community page of the area you touch.",
                    "Check health with `readmenator . lint-wiki` (exit 1 on issues).",
                ),
                regenerate=("readmenator . wiki", "readmenator . --rebuild"),
            ),
            FolderSpec(
                dirname=cfg.GRAPHRAG_OUTPUT_DIR,
                purpose=(
                    "Zero-token GraphRAG index: entities, relationships, community reports and source "
                    "text units built deterministically from the code graph, so questions can be "
                    "answered with ranked, budgeted context instead of reading the whole repository."
                ),
                entries=(
                    ("index.json", "Index header with schema version and counts"),
                    ("entities.jsonl", "One entity per line: files, symbols, concepts, externals"),
                    ("relationships.jsonl", "One relationship per line: imports, calls, inherits, defines, documents"),
                    ("communities.jsonl", "Community report hierarchy (communities, themes, root)"),
                    ("text_units.jsonl", "Source text units per symbol (empty in privacy mode)"),
                    ("REPORTS.md", "Human-readable community reports"),
                ),
                usage=(
                    "Ask questions: `readmenator . ask \"<question>\"` (`--global` for overviews, `--local` for specifics).",
                    "The JSONL files are one record per line, so `grep` works directly on them.",
                ),
                regenerate=("readmenator . graphrag", "readmenator . --rebuild"),
            ),
            FolderSpec(
                dirname=cfg.APIDOCS_OUTPUT_DIR,
                purpose=(
                    "API reference in the style of Sphinx and Doxygen: every module, class, function "
                    "and constant with exact signatures, parsed docstrings, inheritance, callers and "
                    "callees, documentation coverage and doc warnings."
                ),
                entries=(
                    ("index.md", "Modules by package with coverage"),
                    (cfg.APIDOCS_MODULES_SUBDIR, "One Markdown page per module (signatures, parameters, returns, raises, call graph)"),
                    ("classes.md", "Class hierarchy"),
                    ("genindex.md", "A-Z general index"),
                    ("COVERAGE.md", "Documentation coverage and DOC00x warnings"),
                    (cfg.APIDOCS_ARCHITECTURE_FILENAME, "Tiered architecture and execution flows (Mermaid)"),
                    (cfg.FLOWS_OUTPUT, "Interactive architecture and execution-flow diagrams"),
                    (cfg.APIDOCS_HTML_FILENAME, "Offline searchable HTML API browser (open in a browser)"),
                    (f"{api}/{cfg.APIDOCS_JSONL_INDEX}", "Machine-readable model index: meta, coverage, module list, grep examples"),
                    (f"{api}/{cfg.APIDOCS_JSONL_MODULES_SUBDIR}", "One JSON Lines file per module, one entity per line"),
                    (f"{api}/{cfg.APIDOCS_JSONL_WARNINGS}", "One documentation warning per line"),
                    (cfg.APIDOCS_JSON_FILENAME, "Monolithic model (only with APIDOCS_JSON_MONOLITH=True)"),
                ),
                usage=(
                    f"Humans: open `{cfg.APIDOCS_OUTPUT_DIR}/{cfg.APIDOCS_HTML_FILENAME}` or start at `index.md`.",
                    f"Agents: `grep -h '\"name\":\"<Name>\"' {cfg.APIDOCS_OUTPUT_DIR}/{api}/{cfg.APIDOCS_JSONL_MODULES_SUBDIR}/*.jsonl`.",
                    "Gate documentation in CI: `readmenator . doc-coverage --fail-under 80`.",
                ),
                regenerate=("readmenator . apidocs", "readmenator . --rebuild"),
            ),
            FolderSpec(
                dirname=cfg.DIAGRAM_OUTPUT_DIR,
                purpose=(
                    "Interactive maps gallery: a self-contained static site with system maps, "
                    "the 2D/3D force-graph explorer, the edge bundle explorer, flow diagrams, "
                    "component diagrams, the overview video and the documentation set. "
                    "It can be served as-is (for example as the GitHub Pages root)."
                ),
                entries=(
                    ("index.html", "Gallery home: start here"),
                    ("architecture.html", "Architecture map (files by layer, resolved imports)"),
                    ("workflow.html", "Workflow map (delivery path across layers)"),
                    ("sequence.html", "Sequence map (participants and call messages)"),
                    ("dataflow.html", "Dataflow map (sources, transforms, stores)"),
                    ("lifecycle.html", "Lifecycle map (layer states and transitions)"),
                    (cfg.FORCEGRAPH_OUTPUT, "Force-graph explorer: 2D/3D, inspector, reach, paths, lenses, source viewer"),
                    (cfg.BUNDLEGRAPH_OUTPUT, "Edge bundle explorer: circle and sphere views of every import"),
                    (cfg.FLOWS_OUTPUT, "Interactive architecture tiers and execution flows"),
                    ("components.html", "Component diagrams"),
                    (cfg.FORCEGRAPH_VENDOR_SUBDIR, "Vendored graph engine used offline by the explorer"),
                    (cfg.SITE_DOCS_SUBDIR, "Markdown copies shown in the gallery document drawer"),
                    (cfg.SITE_LLMS_TXT_FILENAME, "Agent entry point listing every document"),
                    (Path(cfg.VIDEO_OUTPUT).name, "Overview video"),
                    (cfg.SITE_VIDEO_POSTER_FILENAME, "Video poster frame"),
                ),
                usage=(
                    f"Open `{cfg.DIAGRAM_OUTPUT_DIR}/index.html` in a browser; maps load vis.js from a CDN, explorers work offline.",
                    "Large pages embed their data gzip-compressed; any current Chrome, Edge, Firefox or Safari decodes it natively.",
                ),
                regenerate=("readmenator . diagrams --full", "readmenator . --rebuild"),
            ),
            FolderSpec(
                dirname=cfg.COMPONENTS_OUTPUT_DIR,
                purpose=(
                    "Component diagrams: the codebase as a handful of components (code communities) "
                    "with the relations between them, method-level key edges and call-site evidence."
                ),
                entries=(
                    ("analysis.json", "Component model: files, methods index, components, relations"),
                    ("overview.md", "Top-level `graph LR` diagram with related classes and methods"),
                    ("*.md", "One page per expandable component (nested diagram)"),
                    ("index.html", "Offline interactive layered diagram"),
                ),
                usage=(
                    f"Start at `{cfg.COMPONENTS_OUTPUT_DIR}/overview.md` or open `index.html`.",
                ),
                regenerate=("readmenator . components", "readmenator . --rebuild"),
            ),
            FolderSpec(
                dirname=cfg.RULE_GEN_OUTPUT_DIR,
                purpose=(
                    "Rules: Semgrep rules suggested from patterns actually found in the code, plus "
                    "the YARA-lite rules and the false-positive exclusion list used by the security audit."
                ),
                entries=(
                    ("readmenator_*.yml", "Suggested Semgrep rules (all languages and per language)"),
                    ("rule_schema.json", "Schema of the suggested rules"),
                    ("yara_rules.yar", "YARA-lite rules (T1/T2/T3); yours to edit"),
                    ("exclusions.yaml", "False-positive blocklist (globs, optional rule_id scope); yours to edit"),
                ),
                usage=(
                    f"Run the suggestions: `semgrep --config {cfg.RULE_GEN_OUTPUT_DIR}/`.",
                    "Validate the YARA-lite rules: `readmenator . validate-rules`.",
                ),
                regenerate=("readmenator . export-rules", "readmenator . --rebuild"),
            ),
            FolderSpec(
                dirname=cfg.GH_WIKI_DRY_RUN_DIR,
                purpose=(
                    "GitHub wiki dry run: the exact pages that would be pushed to the repository wiki, "
                    "rendered locally without any git call, so they can be reviewed first."
                ),
                entries=(
                    (f"{cfg.GH_WIKI_HOME_PAGE}.md", "Wiki home (from the agent wiki index)"),
                    (f"{cfg.GH_WIKI_KB_PAGE}.md", "Knowledge base page"),
                    (f"{cfg.GH_WIKI_AGENT_PREFIX}*.md", "Agent docs as flat wiki pages"),
                    (f"{cfg.GH_WIKI_RECIPE_PREFIX}*.md", "Recipes as flat wiki pages"),
                    ("_Sidebar.md", "Generated sidebar"),
                    ("_Footer.md", "Footer with the source commit"),
                ),
                usage=(
                    "Review the pages, then publish for real with `readmenator . gh-wiki`.",
                ),
                regenerate=("readmenator . gh-wiki --dry-run",),
            ),
        ]

    def render(self, spec: FolderSpec, folder: Path) -> str:
        """Render the README text for one folder.

        Args:
            spec: Folder description.
            folder: Existing folder on disk (entries are listed only when present).

        Returns:
            Markdown README text starting with the marker line.
        """
        cfg = self._config
        rows: List[str] = []
        for pattern, description in spec.entries:
            matches = sorted(p for p in folder.glob(pattern) if p.name != cfg.FOLDER_README_FILENAME)
            if not matches:
                continue
            suffix = "/" if all(p.is_dir() for p in matches) else ""
            rows.append(f"| `{pattern}{suffix}` | {description} |")
        notice = cfg.MSG_FOLDER_NOTICE.strip() or (
            "Generated offline by ReadMenator (static analysis, zero LLM tokens). Files here are "
            "rewritten on every run, so do not edit them by hand. To keep a hand-written README "
            "in this folder instead, delete the first line of this file."
        )
        lines = [
            cfg.FOLDER_README_MARKER,
            f"# {spec.dirname}",
            "",
            spec.purpose,
            "",
            notice,
            "",
        ]
        if rows:
            lines += ["## Contents", "", "| Path | What it is |", "|---|---|", *rows, ""]
        lines += ["## How to use", ""] + [f"- {line}" for line in spec.usage] + [""]
        lines += ["## Regenerate", ""] + [f"    {command}" for command in spec.regenerate] + [""]
        return "\n".join(lines)

    def write_all(self, project_root: str) -> List[str]:
        """Write the README of every generated folder that exists.

        Symlinked folders or targets and READMEs without the marker are left untouched.

        Args:
            project_root: Project root directory.

        Returns:
            Sorted paths of README files written or already current.
        """
        cfg = self._config
        if not cfg.FOLDER_README_ENABLED:
            return []
        root = Path(project_root).resolve()
        written: List[str] = []
        for spec in self.specs():
            folder = root / spec.dirname
            if folder.is_symlink() or not folder.is_dir():
                continue
            target = folder / cfg.FOLDER_README_FILENAME
            if target.is_symlink():
                logger.warning("Skipping symlinked folder README %s", target)
                continue
            if target.exists() and not is_generated_folder_readme(target, cfg):
                logger.info("Keeping hand-written %s", target)
                continue
            text = self.render(spec, folder)
            if not (target.is_file() and target.read_text(encoding="utf-8", errors="ignore") == text):
                target.write_text(text, encoding="utf-8")
            written.append(str(target))
        return sorted(written)
