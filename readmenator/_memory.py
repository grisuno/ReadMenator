"""Persistent project memory for agents, generated with zero tokens.

MEMORY.md is the cross-session context file an agent reads first. Its
generated sections are rebuilt from the source tree on every run:

1. Purpose and domain: README lead sentence, domain vocabulary from the
   concept graph, and the main subsystems.
2. Workflow: build/test/run commands detected from project manifests,
   plus the knowledge refresh and session protocol.
3. Rules and constraints, 4. Style norms, 5. Minimum deliverables: each
   splits into *declared* lines extracted verbatim from instruction files
   (cited ``file:line``) and *measured* baselines computed from the code.
6. Risks to respect: god nodes, cycles, findings, hotspots.

Section 7 is the session log. Agents append decisions, business rules,
and workflow notes with ``readmenator . remember "<note>"`` (or the MCP
``readmenator.remember`` tool); the block is preserved byte for byte
across rebuilds, so knowledge survives between sessions without any
model writing the rest of the file.
"""

from __future__ import annotations

import datetime as _dt
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from readmenator._config import Config
from readmenator._gitmeta import read_git_head
from readmenator._models import AnalysisResult, AnalysisResultV2, ConceptGraph, Node, SecurityFinding
from readmenator._purpose import file_purpose, first_sentence

NOTES_BEGIN = "<!-- readmenator:memory:notes:begin -->"
NOTES_END = "<!-- readmenator:memory:notes:end -->"

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.+?)\s*$")
_NOTE_RE = re.compile(r"^- (\d{4}-\d{2}-\d{2}) \[([a-z_-]+)\] (.+)$")
_SNAKE_RE = re.compile(r"^_*[a-z][a-z0-9]*(?:_[a-z0-9]+)*_*$")
_CAMEL_RE = re.compile(r"^_*[a-z][a-zA-Z0-9]*$")
_PASCAL_RE = re.compile(r"^_*[A-Z][a-zA-Z0-9]*$")
_ANCHOR_RE = re.compile(r"<!--\s*readmenator", re.IGNORECASE)
_ANCHOR_END_RE = re.compile(r"<!--\s*/readmenator", re.IGNORECASE)

_CLASS_KINDS = frozenset({"class", "struct", "interface", "trait", "enum", "record", "protocol"})
_FUNCTION_KINDS = frozenset({"function", "method", "func", "fn", "def", "procedure"})


@dataclass(frozen=True)
class DeclaredRule:
    """One rule line extracted verbatim from an instruction file.

    Attributes:
        category: constraints, style, or deliverables.
        text: The rule text (single line).
        source: ``file:line`` citation.
        heading: Heading the line was found under.
    """

    category: str
    text: str
    source: str
    heading: str


@dataclass(frozen=True)
class MemoryNote:
    """One entry of the preserved session log.

    Attributes:
        date: ISO date the note was recorded.
        kind: Note kind from MEMORY_NOTE_KINDS.
        text: Single-line note text.
    """

    date: str
    kind: str
    text: str


def sanitize_note(text: str, max_chars: int) -> str:
    """Collapse a note to one safe line that cannot break the preserved block.

    Args:
        text: Raw note text.
        max_chars: Maximum characters kept.

    Returns:
        Single-line note without control characters or HTML comment markers.
    """
    clean = "".join(ch if ch.isprintable() else " " for ch in str(text))
    clean = clean.replace("<!--", "< !--").replace("-->", "-- >")
    clean = " ".join(clean.split())
    if len(clean) > max_chars:
        clean = clean[: max(0, max_chars - 3)].rstrip() + "..."
    return clean


class ProjectMemory:
    """Builds, preserves, and appends to the agent memory file."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: MEMORY_* settings and output directories.
        """
        self._config = config

    def path(self, project_root: str) -> Path:
        """Return the MEMORY.md location for a project root."""
        return Path(project_root) / self._config.AGENT_OUTPUT_DIR / self._config.MEMORY_FILENAME

    def read(self, project_root: str) -> str:
        """Return the current memory file text ("" when missing)."""
        try:
            return self.path(project_root).read_text(encoding="utf-8")
        except OSError:
            return ""

    def notes(self, project_root: str) -> List[MemoryNote]:
        """Parse the preserved session log into notes.

        Args:
            project_root: Project root directory.

        Returns:
            Notes in file order.
        """
        out: List[MemoryNote] = []
        for line in self._notes_block(self.read(project_root)).splitlines():
            match = _NOTE_RE.match(line.strip())
            if match:
                out.append(MemoryNote(match.group(1), match.group(2), match.group(3)))
        return out

    @staticmethod
    def _notes_block(text: str) -> str:
        """Return the raw text between the preserved notes markers."""
        start = text.find(NOTES_BEGIN)
        end = text.find(NOTES_END)
        if start < 0 or end < 0 or end < start:
            return ""
        return text[start + len(NOTES_BEGIN):end].strip("\n")

    def remember(self, project_root: str, note: str, kind: str = "note", today: Optional[str] = None) -> MemoryNote:
        """Append one note to the preserved session log.

        Creates a minimal MEMORY.md when none exists yet; the next rebuild
        fills the generated sections around the preserved log.

        Args:
            project_root: Project root directory.
            note: Note text (collapsed to one line).
            kind: One of MEMORY_NOTE_KINDS.
            today: ISO date override (defaults to the local date).

        Returns:
            The stored note.

        Raises:
            ValueError: Unknown kind or empty note.
        """
        cfg = self._config
        if kind not in cfg.MEMORY_NOTE_KINDS:
            raise ValueError(f"unknown kind '{kind}', expected one of: {', '.join(cfg.MEMORY_NOTE_KINDS)}")
        text = sanitize_note(note, cfg.MEMORY_NOTE_MAX_CHARS)
        if not text:
            raise ValueError("empty note")
        stored = MemoryNote(today or _dt.date.today().isoformat(), kind, text)
        current = self.read(project_root)
        block = self._notes_block(current)
        lines = [line for line in block.splitlines() if line.strip()]
        lines.append(f"- {stored.date} [{stored.kind}] {stored.text}")
        body = current if NOTES_BEGIN in current and NOTES_END in current else self._skeleton()
        self._write(project_root, self._splice(body, "\n".join(lines)))
        return stored

    def _skeleton(self) -> str:
        """Minimal memory document used before the first full build."""
        return (
            "# Project Memory\n\n"
            "Run `readmenator . --rebuild` to generate sections 1-6.\n\n"
            + self._log_section("")
        )

    def _log_section(self, block: str) -> str:
        """Render section 7 around a preserved notes block."""
        kinds = ", ".join(self._config.MEMORY_NOTE_KINDS)
        return (
            "## 7. Session log (preserved across rebuilds)\n\n"
            "Append with `readmenator . remember \"<note>\" --kind <kind>` (kinds: "
            + kinds + ") or the MCP tool `readmenator.remember`. Record business rules, decisions and "
            "their reasons, workflow changes, and anything the next session must not rediscover.\n\n"
            + NOTES_BEGIN + "\n" + (block + "\n" if block else "") + NOTES_END + "\n"
        )

    def _splice(self, document: str, block: str) -> str:
        """Replace the notes block inside a document."""
        start = document.find(NOTES_BEGIN)
        end = document.find(NOTES_END)
        if start < 0 or end < 0:
            return document.rstrip() + "\n\n" + self._log_section(block)
        return document[:start] + NOTES_BEGIN + "\n" + (block + "\n" if block else "") + document[end:]

    def _write(self, project_root: str, text: str) -> Path:
        """Write the memory file, creating the agent directory when needed."""
        target = self.path(project_root)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.is_symlink():
            raise OSError(f"refusing to write through symlink: {target}")
        target.write_text(text, encoding="utf-8")
        return target

    def write(self, project_root: str, generated: str) -> Path:
        """Write generated sections while preserving the existing session log.

        Args:
            project_root: Project root directory.
            generated: Output of :meth:`build` (contains an empty notes block).

        Returns:
            Path of the written MEMORY.md.
        """
        block = self._notes_block(self.read(project_root))
        return self._write(project_root, self._splice(generated, block))

    def build(
        self,
        project_root: str,
        nodes: List[Node],
        analysis: Optional[AnalysisResult] = None,
        analysis_v2: Optional[AnalysisResultV2] = None,
        findings: Optional[List[SecurityFinding]] = None,
        concept_graph: Optional[ConceptGraph] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> str:
        """Render the generated memory document (with an empty notes block).

        Args:
            project_root: Project root directory.
            nodes: Scanned file nodes.
            analysis: Community and god-node analysis.
            analysis_v2: Cycles, hotspots, and other deep results.
            findings: Security findings.
            concept_graph: Semantic noun graph for the domain vocabulary.
            content_map: File contents for line-length baselines.

        Returns:
            Markdown text of MEMORY.md.
        """
        cfg = self._config
        root = Path(project_root).resolve()
        if concept_graph is None and analysis_v2 is not None:
            concept_graph = analysis_v2.concept_graph
        rules = self.extract_rules(str(root))
        head = read_git_head(str(root))
        agent = cfg.AGENT_OUTPUT_DIR
        lines: List[str] = [
            "# Project Memory",
            "",
            "> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM "
            "tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. "
            "Section 7 is written by agents and humans and is preserved across rebuilds.",
            "",
            f"Generated from {len(nodes)} files"
            + (f" at commit `{head['commit'][:12]}`" if head.get("commit") else "")
            + ". Read this first, then `readmenator-wiki/index.md`, then "
            "`readmenator . ask \"<question>\"` for anything specific.",
            "",
        ]
        lines += self._purpose_section(root, nodes, analysis, concept_graph)
        lines += self._workflow_section(root, nodes)
        lines += self._declared_section("3. Rules and constraints", rules, "constraints", [
            f"Security findings at medium or above: {self._count_severe(findings or [])} "
            f"(see `{agent}/SECURITY.md`); do not add new ones.",
            f"Dependency cycles: {len(analysis_v2.cycles) if analysis_v2 else 0}; "
            f"layer violations: {len(analysis_v2.layer_violations) if analysis_v2 else 0} "
            f"(see `{agent}/GOTCHAS.md`).",
        ])
        lines += self._declared_section("4. Style norms", rules, "style", self._style_baselines(nodes, content_map or {}))
        lines += self._declared_section("5. Minimum deliverables", rules, "deliverables",
                                        self._deliverable_baselines(root, nodes, findings or [], analysis_v2))
        lines += self._risk_section(analysis, analysis_v2)
        lines.append(self._log_section(""))
        return "\n".join(lines)

    def extract_rules(self, project_root: str) -> List[DeclaredRule]:
        """Extract categorised rule lines from the project's instruction files.

        Only bullet or numbered lines under headings that match the
        configured keywords are kept; readmenator's own injected blocks are
        skipped. Files are read when they are regular, non-symlink files
        under MAX_FILE_SIZE_MB.

        Args:
            project_root: Project root directory.

        Returns:
            Rules in file order, capped per file and category and per category overall.
        """
        cfg = self._config
        root = Path(project_root)
        keywords = {
            "constraints": tuple(cfg.MEMORY_CONSTRAINT_KEYWORDS),
            "style": tuple(cfg.MEMORY_STYLE_KEYWORDS),
            "deliverables": tuple(cfg.MEMORY_DELIVERABLE_KEYWORDS),
        }
        out: List[DeclaredRule] = []
        per_category: Dict[str, int] = {}
        limit = cfg.MAX_FILE_SIZE_MB * 1024 * 1024
        for name in cfg.MEMORY_RULE_SOURCES:
            path = root / name
            if not path.is_file() or path.is_symlink():
                continue
            try:
                if path.stat().st_size > limit:
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            taken: Dict[str, int] = {}
            category = ""
            heading = ""
            skipping = False
            for number, raw in enumerate(text.splitlines(), start=1):
                if _ANCHOR_END_RE.search(raw):
                    skipping = False
                    continue
                if _ANCHOR_RE.search(raw):
                    skipping = True
                    continue
                if skipping:
                    continue
                match = _HEADING_RE.match(raw)
                if match:
                    heading = match.group(2).strip()
                    excluded = any(word in heading.lower() for word in cfg.MEMORY_HEADING_EXCLUDE)
                    category = "" if excluded else self._categorise(heading, keywords)
                    continue
                if not category or taken.get(category, 0) >= cfg.MEMORY_MAX_RULES_PER_FILE:
                    continue
                item = _ITEM_RE.match(raw)
                if not item:
                    continue
                if per_category.get(category, 0) >= cfg.MEMORY_MAX_RULES_PER_CATEGORY:
                    continue
                rule = " ".join(item.group(1).split())
                if len(rule) < cfg.MEMORY_MIN_RULE_CHARS:
                    continue
                out.append(DeclaredRule(category, rule, f"{name}:{number}", heading))
                taken[category] = taken.get(category, 0) + 1
                per_category[category] = per_category.get(category, 0) + 1
        return out

    @staticmethod
    def _categorise(heading: str, keywords: Dict[str, Tuple[str, ...]]) -> str:
        """Map a heading to a rule category by keyword (first match wins)."""
        low = heading.lower()
        for category in ("deliverables", "style", "constraints"):
            if any(word in low for word in keywords[category]):
                return category
        return ""

    def _purpose_section(
        self, root: Path, nodes: List[Node], analysis: Optional[AnalysisResult], concept_graph: Optional[ConceptGraph],
    ) -> List[str]:
        """Section 1: README lead, domain vocabulary, and subsystems."""
        cfg = self._config
        lines = ["## 1. Purpose and domain", ""]
        lead = self._readme_lead(root)
        if lead:
            lines.append(f"- What it is: {lead[0]} (`{lead[1]}`)")
        if concept_graph is not None and concept_graph.concepts:
            stop = set(cfg.MEMORY_VOCABULARY_STOPWORDS)
            terms = [c for c in concept_graph.concepts if c.name not in stop][: cfg.MEMORY_VOCABULARY_TOP_N]
            vocab = ", ".join(f"`{c.name}` ({len(c.file_ids)})" for c in terms)
            lines.append(f"- Domain vocabulary (term, files): {vocab}")
        node_by_id = {n.node_id: n for n in nodes}
        for community in (analysis.communities if analysis else [])[: cfg.MEMORY_SUBSYSTEMS_TOP_N]:
            members = sorted(
                community.file_ids,
                key=lambda f: (self._is_test(f), -len(node_by_id[f].symbols) if f in node_by_id else 0, f),
            )
            core = members[0] if members else ""
            purpose = file_purpose(node_by_id[core], cfg.AGENT_PURPOSE_MAX_CHARS) if core in node_by_id else ""
            lines.append(
                f"- Subsystem `{community.label}`: {community.size} files, core `{core}`"
                + (f": {purpose}" if purpose else "")
            )
        if len(lines) == 2:
            lines.append("- No README lead or communities detected yet.")
        lines.append("- Business rules that the code cannot show live in section 7: record them there.")
        lines.append("")
        return lines

    def _readme_lead(self, root: Path) -> Optional[Tuple[str, str]]:
        """First prose sentence of the README with its citation."""
        for name in ("README.md", "README.rst", "README.txt", "readme.md", "Readme.md"):
            path = root / name
            if not path.is_file() or path.is_symlink():
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for number, raw in enumerate(text.splitlines(), start=1):
                line = raw.strip()
                if not line or line.startswith(("#", "!", "[", "<", "|", "`", "=", "-", ">", "*")):
                    continue
                sentence = first_sentence(line)
                if len(sentence) >= self._config.MEMORY_MIN_RULE_CHARS:
                    return sentence, f"{name}:{number}"
        return None

    def detect_commands(self, root: Path, nodes: Sequence[Node]) -> List[Tuple[str, str]]:
        """Detect workflow commands from project manifests.

        Args:
            root: Project root.
            nodes: Scanned nodes (languages and test layout).

        Returns:
            (command, source) pairs in a stable order.
        """
        cmds: List[Tuple[str, str]] = []
        languages = {n.language for n in nodes}
        has_tests = any(self._is_test(n.node_id) for n in nodes)
        pyproject = root / "pyproject.toml"
        if pyproject.is_file():
            text = self._safe_read(pyproject)
            if "pytest" in text or (has_tests and "py" in languages):
                cmds.append(("python -m pytest -q", "pyproject.toml"))
            section = re.search(r"^\[project\.scripts\]\s*$(.*?)(?=^\[|\Z)", text, re.M | re.S)
            if section:
                for match in re.finditer(r"^([A-Za-z0-9_.-]+)\s*=", section.group(1), re.M):
                    cmds.append((f"{match.group(1)} --help", "pyproject.toml [project.scripts]"))
        elif has_tests and "py" in languages:
            cmds.append(("python -m pytest -q", "tests/ layout"))
        package = root / "package.json"
        if package.is_file():
            try:
                scripts = json.loads(self._safe_read(package) or "{}").get("scripts", {})
            except ValueError:
                scripts = {}
            for name in sorted(scripts)[: self._config.MEMORY_MAX_COMMANDS]:
                cmds.append((f"npm run {name}", "package.json scripts"))
        makefile = root / "Makefile"
        if makefile.is_file():
            for match in re.finditer(r"^([A-Za-z][A-Za-z0-9_-]*):", self._safe_read(makefile), re.M):
                cmds.append((f"make {match.group(1)}", "Makefile"))
        for manifest, cmd in (("go.mod", "go test ./..."), ("Cargo.toml", "cargo test"),
                              ("pom.xml", "mvn test"), ("build.gradle", "gradle test"),
                              ("mix.exs", "mix test"), ("Gemfile", "bundle exec rake")):
            if (root / manifest).is_file():
                cmds.append((cmd, manifest))
        for folder in (".github/workflows", "workflows"):
            directory = root / folder
            if directory.is_dir() and not directory.is_symlink():
                for wf in sorted(directory.glob("*.y*ml")):
                    cmds.append((f"CI workflow {wf.name}", f"{folder}/{wf.name}"))
        seen: set = set()
        unique = []
        for cmd, src in cmds:
            if cmd not in seen:
                seen.add(cmd)
                unique.append((cmd, src))
        return unique[: self._config.MEMORY_MAX_COMMANDS]

    def _safe_read(self, path: Path) -> str:
        """Read a small regular file, returning "" on any problem."""
        try:
            if path.is_symlink() or path.stat().st_size > self._config.MAX_FILE_SIZE_MB * 1024 * 1024:
                return ""
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""

    @staticmethod
    def _is_test(file_id: str) -> bool:
        """Return whether a path looks like a test file."""
        name = file_id.rpartition("/")[2].lower()
        parts = file_id.lower().split("/")
        return (
            name.startswith("test_") or name.endswith(("_test.py", "_test.go", ".test.js", ".test.ts", ".spec.ts", ".spec.js"))
            or "tests" in parts[:-1] or "test" in parts[:-1] or "__tests__" in parts[:-1]
        )

    def _workflow_section(self, root: Path, nodes: List[Node]) -> List[str]:
        """Section 2: detected commands plus the knowledge and session protocol."""
        agent = self._config.AGENT_OUTPUT_DIR
        lines = ["## 2. Workflow", "", "Detected commands:"]
        commands = self.detect_commands(root, nodes)
        lines += [f"- `{cmd}` ({src})" for cmd, src in commands] or ["- none detected"]
        lines += [
            "",
            "Session protocol:",
            "1. Start: read this file, then `readmenator . fresh` (exit 1 means run `readmenator . --rebuild`).",
            "2. Orient: `readmenator-wiki/index.md`; for a question use `readmenator . ask \"<question>\"` "
            "(local = entities + sources, `--global` = community reports).",
            f"3. Before editing a file: `grep -n '<file>' {agent}/GOTCHAS.md {agent}/SECURITY.md`.",
            "4. After the change: run the tests above, then `readmenator . --rebuild` so the maps, wiki, and this file stay true.",
            "5. End: record decisions, business rules, and gotchas with `readmenator . remember \"<note>\" --kind decision`.",
            "",
        ]
        return lines

    @staticmethod
    def _declared_section(title: str, rules: List[DeclaredRule], category: str, measured: List[str]) -> List[str]:
        """Render a declared + measured section."""
        lines = [f"## {title}", "", "Declared:"]
        picked = [r for r in rules if r.category == category]
        lines += [f"- {r.text} (`{r.source}`)" for r in picked] or [
            "- none declared in instruction files (add them to AGENTS.md or record them in section 7)"
        ]
        lines += ["", "Measured baseline:"]
        lines += [f"- {m}" for m in measured] or ["- not enough data"]
        lines.append("")
        return lines

    def _style_baselines(self, nodes: List[Node], content_map: Dict[str, str]) -> List[str]:
        """Naming conventions, docstring coverage, and file length per language."""
        cfg = self._config
        by_lang: Dict[str, List[Node]] = {}
        for node in nodes:
            by_lang.setdefault(node.language or "unknown", []).append(node)
        out: List[str] = []
        for lang in sorted(by_lang, key=lambda k: (-len(by_lang[k]), k))[: cfg.MEMORY_STYLE_LANGUAGES]:
            group = by_lang[lang]
            symbols = [s for n in group for s in n.symbols]
            funcs = [s.name.rpartition(".")[2] for s in symbols if s.kind in _FUNCTION_KINDS]
            classes = [s.name.rpartition(".")[2] for s in symbols if s.kind in _CLASS_KINDS]
            documented = sum(1 for s in symbols if (s.doc or "").strip())
            parts = [f"{lang}: {len(group)} files, {len(symbols)} symbols"]
            if symbols:
                parts.append(f"docstrings on {self._pct(documented, len(symbols))} of symbols")
            if funcs:
                snake = sum(1 for f in funcs if _SNAKE_RE.match(f))
                camel = sum(1 for f in funcs if _CAMEL_RE.match(f) and not _SNAKE_RE.match(f))
                style = "snake_case" if snake >= camel else "camelCase"
                parts.append(f"functions {style} ({self._pct(max(snake, camel), len(funcs))})")
            if classes:
                pascal = sum(1 for c in classes if _PASCAL_RE.match(c))
                parts.append(f"types PascalCase ({self._pct(pascal, len(classes))})")
            sizes = sorted(len(content_map[n.node_id].splitlines()) for n in group if n.node_id in content_map)
            if sizes:
                parts.append(f"median file {sizes[len(sizes) // 2]} lines, max {sizes[-1]}")
            out.append("; ".join(parts) + ".")
        tests = [n.node_id for n in nodes if self._is_test(n.node_id)]
        if tests:
            dirs = sorted({t.rpartition("/")[0] or "." for t in tests})
            named = [t for t in tests if "test" in t.rpartition("/")[2].lower()] or tests
            out.append(f"Tests: {len(tests)} files under {', '.join(dirs[:3])}; follow the existing naming (e.g. `{named[0].rpartition('/')[2]}`).")
        return out

    def _deliverable_baselines(
        self, root: Path, nodes: List[Node], findings: List[SecurityFinding], analysis_v2: Optional[AnalysisResultV2],
    ) -> List[str]:
        """Measured minimums every change should keep."""
        cfg = self._config
        commands = [c for c, _s in self.detect_commands(root, nodes) if "test" in c]
        symbols = [s for n in nodes for s in n.symbols]
        documented = sum(1 for s in symbols if (s.doc or "").strip())
        out = []
        if commands:
            out.append(f"Tests pass: `{commands[0]}`.")
        if symbols:
            out.append(f"Docstring coverage stays at or above {self._pct(documented, len(symbols))}.")
        out.append(f"No new security findings at medium or above (current: {self._count_severe(findings)}).")
        if analysis_v2 is not None:
            out.append(f"No new dependency cycles (current: {len(analysis_v2.cycles)}).")
        out.append(f"Files stay under {cfg.LINTER_MAX_LINES} lines where possible (`readmenator . lint`).")
        out.append("Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.")
        return out

    def _risk_section(self, analysis: Optional[AnalysisResult], analysis_v2: Optional[AnalysisResultV2]) -> List[str]:
        """Section 6: the structural risks an agent must respect."""
        cfg = self._config
        agent = cfg.AGENT_OUTPUT_DIR
        lines = ["## 6. Risks to respect", ""]
        gods = [nid for nid, _s in (analysis.god_nodes if analysis else [])[: cfg.MEMORY_RISKS_TOP_N]]
        if gods:
            lines.append("- God nodes (changes ripple widely): " + ", ".join(f"`{g}`" for g in gods))
        if analysis_v2 is not None:
            hot = [h.file_id for h in analysis_v2.hotspots[: cfg.MEMORY_RISKS_TOP_N]]
            if hot:
                lines.append("- Hotspots (complex and central): " + ", ".join(f"`{h}`" for h in hot))
            for cycle in analysis_v2.cycles[: cfg.MEMORY_RISKS_TOP_N]:
                loop = list(cycle.cycle)
                if loop and loop[0] != loop[-1]:
                    loop.append(loop[0])
                lines.append("- Cycle: " + " -> ".join(f"`{f}`" for f in loop))
        lines.append(f"- Full blast radius: `{agent}/GOTCHAS.md`; findings: `{agent}/SECURITY.md`.")
        lines.append("")
        return lines

    @staticmethod
    def _pct(part: int, whole: int) -> str:
        """Format a percentage with no decimals."""
        return f"{round(100 * part / whole) if whole else 0}%"

    @staticmethod
    def _count_severe(findings: Iterable[SecurityFinding]) -> int:
        """Count findings at medium severity or above."""
        return sum(1 for f in findings if f.severity in ("critical", "high", "medium"))
