"""Markdown, JSON, and writer layer for the deterministic API reference.

Renders an ApiReference into a Sphinx / Doxygen style documentation
tree: an index with per-module coverage, one page per module (classes,
members, parameters merged from signatures and docstrings, returns,
raises, examples, admonitions, inheritance, call graphs as Mermaid,
callers and callees), a class hierarchy, an alphabetical general index,
a coverage report with stale-doc warnings, ``api.json``, and the
self-contained HTML browser from ``readmenator._apidocs_page``.
Cross-references in prose (backticks, Sphinx roles, ``{@link}``) are
resolved to anchors. Everything is deterministic and offline.
"""

from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Tuple

from readmenator._apidocs import (
    CALLABLE_KINDS,
    CLASS_KINDS,
    DATA_KINDS,
    KIND_MODULE,
    ApiEntity,
    ApiReference,
)
from readmenator._apidocs_page import render_api_site
from readmenator._config import Config
from readmenator._flowlayout import FlowGraph
from readmenator._flowpage import render_flows_page
from readmenator._docstrings import DocComment, DocField

logger = logging.getLogger(__name__)

FENCE_LANGUAGES: Dict[str, str] = {
    "py": "python", "rs": "rust", "ts": "typescript", "tsx": "tsx", "js": "javascript",
    "jsx": "jsx", "cs": "csharp", "kt": "kotlin", "kts": "kotlin", "c": "c", "h": "c",
    "cpp": "cpp", "cc": "cpp", "cxx": "cpp", "hpp": "cpp", "hxx": "cpp", "hh": "cpp",
    "go": "go", "java": "java", "rb": "ruby", "sh": "bash", "bash": "bash", "zsh": "bash",
    "php": "php", "dart": "dart", "swift": "swift", "scala": "scala", "sc": "scala",
    "lua": "lua", "ex": "elixir", "exs": "elixir", "nim": "nim", "gd": "gdscript",
    "asm": "nasm", "s": "asm", "S": "asm",
}

KIND_TITLES: Dict[str, str] = {
    "class": "Classes", "struct": "Structs", "interface": "Interfaces", "trait": "Traits",
    "enum": "Enums", "record": "Records", "protocol": "Protocols", "union": "Unions",
    "exception": "Exceptions", "extension": "Extensions", "object": "Objects",
    "impl": "Implementations", "type_alias": "Type Aliases", "function": "Functions",
    "macro": "Macros", "constant": "Constants", "variable": "Variables",
}

_ROLE_RE = re.compile(
    r":(?:py:)?(?:class|func|meth|attr|mod|obj|exc|data|const|ref):`~?([^`<>]+?)(?:\s*<([^>]+)>)?`"
    r"|\{@link(?:plain)?\s+([^}\s]+)[^}]*\}"
    r"|`([A-Za-z_$][\w$.:#]*?)(?:\(\))?`"
)


def module_display_name(entity: ApiEntity) -> str:
    """Return the Sphinx-style display name of a module entity."""
    path = PurePosixPath(entity.file)
    if entity.language == "py":
        parts = list(path.with_suffix("").parts)
        if parts and parts[-1] == "__init__":
            parts = parts[:-1]
        return ".".join(parts) or path.stem
    return entity.file


def page_slug(module_uid: str) -> str:
    """Return the deterministic page file stem for a module uid."""
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", module_uid.replace("/", "."))
    return slug.strip("._") or "module"


def jsonl_index_path(config: Config) -> str:
    """Return the API JSONL index path relative to APIDOCS_OUTPUT_DIR."""
    return str(PurePosixPath(config.APIDOCS_JSONL_DIR) / config.APIDOCS_JSONL_INDEX)


def jsonl_warnings_path(config: Config) -> str:
    """Return the API warnings JSONL path relative to APIDOCS_OUTPUT_DIR."""
    return str(PurePosixPath(config.APIDOCS_JSONL_DIR) / config.APIDOCS_JSONL_WARNINGS)


def _jsonl_line(record: Dict[str, object]) -> str:
    """Serialise one record as a single compact JSON line."""
    return json.dumps(record, ensure_ascii=False, separators=(",", ":"), sort_keys=False)


def jsonl_pages(reference: ApiReference, config: Config) -> Dict[str, str]:
    """Split the API model into one JSON Lines file per module plus an index.

    Every entity is one line in ``api/modules/<slug>.jsonl`` so a grep returns
    exactly the matching entity; no file grows with the whole project.

    Args:
        reference: The API reference.
        config: Application configuration.

    Returns:
        Mapping of path relative to APIDOCS_OUTPUT_DIR to file text.
    """
    base = PurePosixPath(config.APIDOCS_JSONL_DIR)
    modules_rel = PurePosixPath(config.APIDOCS_JSONL_MODULES_SUBDIR)
    grouped: Dict[str, List[str]] = {uid: [] for uid in reference.modules}
    for entity in reference.entities.values():
        grouped.setdefault(entity.file, []).append(_jsonl_line(entity.to_dict()))
    pages: Dict[str, str] = {}
    listing: List[Dict[str, object]] = []
    for uid, lines in grouped.items():
        if not lines:
            continue
        rel = modules_rel / f"{page_slug(uid)}.jsonl"
        pages[str(base / rel)] = "\n".join(lines) + "\n"
        listing.append({"uid": uid, "path": str(rel), "entities": len(lines)})
    warnings = [_jsonl_line(w.to_dict()) for w in reference.warnings]
    pages[str(base / config.APIDOCS_JSONL_WARNINGS)] = "\n".join(warnings) + ("\n" if warnings else "")
    root = f"{config.APIDOCS_OUTPUT_DIR}/{base}"
    index = {
        "schema_version": config.APIDOCS_SCHEMA_VERSION,
        "format": "jsonl",
        "meta": dict(reference.meta),
        "coverage": reference.coverage,
        "modules": listing,
        "warnings": {"path": config.APIDOCS_JSONL_WARNINGS, "total": len(warnings)},
        "usage": [
            f"grep -h '\"name\":\"<Name>\"' {root}/{modules_rel}/*.jsonl",
            f"grep -h '\"qualname\":\"<Owner.method>\"' {root}/{modules_rel}/*.jsonl",
            f"cat {root}/{modules_rel}/<module-slug>.jsonl",
            f"grep -h '\"code\":\"DOC001\"' {root}/{config.APIDOCS_JSONL_WARNINGS}",
        ],
    }
    pages[str(base / config.APIDOCS_JSONL_INDEX)] = json.dumps(index, indent=1, ensure_ascii=False) + "\n"
    return pages


def read_api_jsonl(api_dir: str, config: Config) -> Dict[str, object]:
    """Reassemble the split JSONL API model into the monolithic api.json shape.

    Args:
        api_dir: The ``api/`` directory written by jsonl_pages.
        config: Application configuration.

    Returns:
        Dictionary with schema_version, meta, coverage, modules, entities, warnings.
    """
    root = Path(api_dir)
    index = json.loads((root / config.APIDOCS_JSONL_INDEX).read_text(encoding="utf-8"))
    entities: List[Dict[str, object]] = []
    for module in index.get("modules", []):
        text = (root / module["path"]).read_text(encoding="utf-8")
        entities.extend(json.loads(line) for line in text.splitlines() if line.strip())
    warn_path = root / index.get("warnings", {}).get("path", config.APIDOCS_JSONL_WARNINGS)
    warnings = [json.loads(line) for line in warn_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {
        "schema_version": index.get("schema_version"),
        "meta": index.get("meta", {}),
        "coverage": index.get("coverage", {}),
        "modules": [m["uid"] for m in index.get("modules", [])],
        "entities": entities,
        "warnings": warnings,
    }


def anchor_slug(qualname: str) -> str:
    """Return the HTML anchor id for an entity qualname."""
    return re.sub(r"[^a-z0-9_-]+", "-", qualname.lower()).strip("-") or "entity"


def _cell(text: str) -> str:
    """Escape *text* for a Markdown table cell."""
    return " ".join((text or "").split()).replace("|", "\\|")


def _inline_code(text: str) -> str:
    """Wrap *text* in a backtick span safe for embedded backticks."""
    if not text:
        return ""
    if "`" in text:
        return f"`` {text} ``"
    return f"`{text}`"


class ApiLinker:
    """Resolves names and entity uids to relative Markdown links."""

    def __init__(self, reference: ApiReference) -> None:
        """Index every entity by uid, qualname, and simple name.

        Args:
            reference: The API reference to link within.
        """
        self._ref = reference
        self._by_qual: Dict[str, List[ApiEntity]] = {}
        self._by_name: Dict[str, List[ApiEntity]] = {}
        self._by_module_name: Dict[str, ApiEntity] = {}
        for entity in reference.entities.values():
            if entity.kind == KIND_MODULE:
                self._by_module_name[module_display_name(entity)] = entity
                continue
            self._by_qual.setdefault(entity.qualname, []).append(entity)
            self._by_name.setdefault(entity.name, []).append(entity)

    def module_of(self, entity: ApiEntity) -> ApiEntity:
        """Return the module entity that contains *entity*."""
        return self._ref.entities.get(entity.file, entity)

    def resolve(self, name: str, context_file: str = "") -> Optional[ApiEntity]:
        """Resolve a written reference to an entity, preferring *context_file*.

        Accepts dotted Python paths (``pkg.mod.Class.method``), qualnames,
        ``Class#method`` / ``Class::method`` forms, and unique simple names.
        """
        target = name.strip().strip("~").rstrip("()").replace("#", ".").replace("::", ".")
        if not target:
            return None
        if target in self._by_module_name:
            return self._by_module_name[target]
        pieces = target.split(".")
        for cut in range(len(pieces) - 1, 0, -1):
            module = self._by_module_name.get(".".join(pieces[:cut]))
            if module is not None:
                qual = ".".join(pieces[cut:])
                for entity in self._by_qual.get(qual, []):
                    if entity.file == module.file:
                        return entity
        candidates = self._by_qual.get(target) or []
        if not candidates and "." not in target:
            candidates = self._by_name.get(target) or []
        if not candidates and len(pieces) > 1:
            tail = ".".join(pieces[-2:])
            candidates = self._by_qual.get(tail) or []
        if not candidates:
            return None
        same = [c for c in candidates if c.file == context_file]
        if same:
            return sorted(same, key=lambda e: e.line)[0]
        if len(candidates) == 1:
            return candidates[0]
        types = [c for c in candidates if c.kind in CLASS_KINDS]
        if len({c.uid for c in types}) == 1:
            return types[0]
        return None

    def href(self, entity: ApiEntity, from_module: str) -> str:
        """Return the relative link to *entity* from a module page (or index when "")."""
        module = self.module_of(entity)
        page = f"{page_slug(module.uid)}.md"
        anchor = "" if entity.kind == KIND_MODULE else f"#{anchor_slug(entity.qualname)}"
        if from_module == module.uid:
            return anchor or page
        return page + anchor

    def link(self, entity: ApiEntity, from_module: str, label: str = "") -> str:
        """Return a Markdown link to *entity*."""
        text = label or (module_display_name(entity) if entity.kind == KIND_MODULE else entity.qualname)
        return f"[{_inline_code(text)}]({self.href(entity, from_module)})"

    def link_uid(self, uid: str, from_module: str) -> str:
        """Return a Markdown link to the entity with *uid* (plain code when unknown)."""
        entity = self._ref.entities.get(uid)
        if entity is None:
            return _inline_code(uid)
        return self.link(entity, from_module)

    def autolink(self, text: str, from_module: str) -> str:
        """Turn backtick names, Sphinx roles, and ``{@link}`` tags into links.

        Fenced code blocks are left untouched.
        """
        if not text:
            return ""
        out: List[str] = []
        fenced = False
        for line in text.split("\n"):
            if line.strip().startswith("```"):
                fenced = not fenced
                out.append(line)
                continue
            if fenced:
                out.append(line)
                continue
            out.append(_ROLE_RE.sub(lambda m: self._replace(m, from_module), line))
        return "\n".join(out)

    def _replace(self, match: "re.Match[str]", from_module: str) -> str:
        """Replace one reference match with a link when it resolves."""
        written = match.group(1) or match.group(3) or match.group(4) or ""
        explicit = match.group(2)
        target = explicit or written
        entity = self.resolve(target, from_module)
        if entity is None:
            if match.group(4) is not None:
                return match.group(0)
            return _inline_code(written.strip().lstrip("~"))
        label = written.strip().lstrip("~")
        if match.group(1) and written.startswith("~"):
            label = label.split(".")[-1]
        return f"[{_inline_code(label)}]({self.href(entity, from_module)})"


class ApiMarkdownRenderer:
    """Renders an ApiReference into Markdown pages."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for budgets and output layout.
        """
        self._config = config

    def render(self, reference: ApiReference, project_name: str) -> Dict[str, str]:
        """Render every page.

        Args:
            reference: The API reference.
            project_name: Display name of the project.

        Returns:
            Mapping of relative output path to Markdown text.
        """
        linker = ApiLinker(reference)
        subdir = self._config.APIDOCS_MODULES_SUBDIR
        pages: Dict[str, str] = {
            "index.md": self._index(reference, linker, project_name),
            "classes.md": self._hierarchy(reference, linker),
            "genindex.md": self._genindex(reference, linker),
            "COVERAGE.md": self._coverage(reference, linker),
        }
        for uid in reference.modules:
            pages[f"{subdir}/{page_slug(uid)}.md"] = self._module(reference, linker, uid)
        return pages

    def _module_link(self, linker: ApiLinker, entity: ApiEntity) -> str:
        """Link from a top-level page into a module page."""
        subdir = self._config.APIDOCS_MODULES_SUBDIR
        return f"{subdir}/{linker.href(entity, '')}"

    def _top_link(self, linker: ApiLinker, entity: ApiEntity, label: str = "") -> str:
        """Markdown link from a top-level page to *entity*."""
        text = label or (module_display_name(entity) if entity.kind == KIND_MODULE else entity.qualname)
        return f"[{_inline_code(text)}]({self._module_link(linker, entity)})"

    def _summary(self, entity: ApiEntity) -> str:
        """Return the one-line summary capped by APIDOCS_SUMMARY_MAX_CHARS."""
        text = " ".join(entity.doc.summary.split())
        limit = max(16, int(self._config.APIDOCS_SUMMARY_MAX_CHARS))
        if len(text) > limit:
            cut = text[:limit].rsplit(" ", 1)[0]
            text = cut.rstrip(",;:") + "..."
        return text

    def _index(self, reference: ApiReference, linker: ApiLinker, project_name: str) -> str:
        """Render index.md: overview, coverage, and the module table by package."""
        cov = reference.coverage.get("overall", {})
        meta = reference.meta
        lines = [
            f"# {project_name} API Reference",
            "",
            f"> Generated offline by readmenator: {meta.get('modules', 0)} modules, "
            f"{meta.get('entities', 0)} documented entities, "
            f"documentation coverage {cov.get('percent', 100.0)}% "
            f"({cov.get('documented', 0)}/{cov.get('total', 0)} public items). "
            "Deterministic, zero tokens: signatures from source, docs parsed from "
            "Google, NumPy, reST, Javadoc/JSDoc/Doxygen, C# XML, and Rustdoc comments.",
            "",
            "Navigate: [Interactive architecture and flows](" + self._config.FLOWS_OUTPUT + ") | "
            "[Architecture and flows (Mermaid)](" + self._config.APIDOCS_ARCHITECTURE_FILENAME + ") | "
            "[Class hierarchy](classes.md) | [General index](genindex.md) | "
            f"[Coverage and warnings](COVERAGE.md) | [`{jsonl_index_path(self._config)}`]"
            f"({jsonl_index_path(self._config)})"
            + (f" | [HTML browser]({self._config.APIDOCS_HTML_FILENAME})" if self._config.APIDOCS_HTML_ENABLED else ""),
            "",
        ]
        if meta.get("truncated"):
            lines.extend([
                f"> Truncated at APIDOCS_MAX_ENTITIES={self._config.APIDOCS_MAX_ENTITIES}; "
                "raise it to document every module.",
                "",
            ])
        languages = meta.get("languages", {})
        if languages:
            lines.append("Languages: " + ", ".join(f"{k} ({v})" for k, v in languages.items()))
            lines.append("")
        groups: Dict[str, List[ApiEntity]] = {}
        for uid in reference.modules:
            entity = reference.entities[uid]
            package = str(PurePosixPath(entity.file).parent)
            groups.setdefault("." if package == "." else package, []).append(entity)
        by_module = reference.coverage.get("by_module", {})
        lines.append("## Modules")
        lines.append("")
        for package in sorted(groups):
            lines.extend([f"### `{package}`", "", "| Module | Summary | Types | Callables | Coverage |", "|---|---|---|---|---|"])
            for entity in groups[package]:
                members = [reference.entities[m] for m in self._descendants(reference, entity.uid)]
                types = sum(1 for m in members if m.kind in CLASS_KINDS)
                callables = sum(1 for m in members if m.kind in CALLABLE_KINDS)
                percent = by_module.get(entity.uid, {}).get("percent", 100.0)
                lines.append(
                    f"| {self._top_link(linker, entity)} | {_cell(self._summary(entity))} | "
                    f"{types} | {callables} | {percent}% |"
                )
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    @staticmethod
    def _descendants(reference: ApiReference, uid: str) -> List[str]:
        """Return all nested member uids of *uid* depth-first in source order."""
        result: List[str] = []
        stack = list(reversed(reference.entities[uid].members)) if uid in reference.entities else []
        while stack:
            current = stack.pop()
            if current not in reference.entities:
                continue
            result.append(current)
            stack.extend(reversed(reference.entities[current].members))
        return result

    def _hierarchy(self, reference: ApiReference, linker: ApiLinker) -> str:
        """Render classes.md: the inheritance forest of project types."""
        types = [e for e in reference.entities.values() if e.kind in CLASS_KINDS]
        lines = ["# Class Hierarchy", "", "Project types nested under the project types they derive from. "
                 "External bases are listed in parentheses.", "", "[Back to index](index.md)", ""]
        if not types:
            lines.append("No class-like types found.")
            return "\n".join(lines) + "\n"
        roots = sorted((e for e in types if not e.base_uids), key=lambda e: (e.name.lower(), e.uid))
        visited: set = set()

        def walk(entity: ApiEntity, depth: int) -> None:
            """Emit *entity* and its subclasses as a nested list."""
            if entity.uid in visited:
                return
            visited.add(entity.uid)
            external = [b for b in entity.bases if not any(
                reference.entities[u].name == re.sub(r"\[.*\]$", "", b).split(".")[-1] for u in entity.base_uids
                if u in reference.entities
            )]
            extra = f" ({', '.join(external)})" if external and depth == 0 else ""
            module = linker.module_of(entity)
            lines.append(
                f"{'  ' * depth}- {self._top_link(linker, entity)} {entity.kind} in "
                f"`{module_display_name(module)}`{_cell(extra)}"
            )
            for child_uid in entity.subclasses:
                if child_uid in reference.entities:
                    walk(reference.entities[child_uid], depth + 1)

        for root in roots:
            walk(root, 0)
        for entity in sorted(types, key=lambda e: e.uid):
            if entity.uid not in visited:
                walk(entity, 0)
        return "\n".join(lines) + "\n"

    def _genindex(self, reference: ApiReference, linker: ApiLinker) -> str:
        """Render genindex.md: every entity alphabetically, grouped by initial."""
        entries = sorted(
            (e for e in reference.entities.values() if e.kind != KIND_MODULE),
            key=lambda e: (e.name.lstrip("_#$").lower(), e.qualname, e.uid),
        )
        letters: Dict[str, List[ApiEntity]] = {}
        for entity in entries:
            initial = (entity.name.lstrip("_#$")[:1] or "_").upper()
            letters.setdefault(initial if initial.isalpha() else "#", []).append(entity)
        lines = ["# General Index", "", "[Back to index](index.md)", ""]
        if letters:
            lines.append(" | ".join(f"[{letter}](#{('sym' if letter == '#' else letter.lower())})" for letter in sorted(letters)))
            lines.append("")
        for letter in sorted(letters):
            anchor = "sym" if letter == "#" else letter.lower()
            lines.extend([f'<a id="{anchor}"></a>', "", f"## {letter}", ""])
            for entity in letters[letter]:
                module = linker.module_of(entity)
                lines.append(
                    f"- {self._top_link(linker, entity, entity.name)} {entity.kind}"
                    f"{' of `' + entity.qualname.rsplit('.', 1)[0] + '`' if '.' in entity.qualname else ''}"
                    f" in `{module_display_name(module)}`"
                )
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    def _coverage(self, reference: ApiReference, linker: ApiLinker) -> str:
        """Render COVERAGE.md: coverage tables plus Doxygen-style warnings."""
        cov = reference.coverage
        overall = cov.get("overall", {})
        lines = [
            "# Documentation Coverage",
            "",
            f"Overall: **{overall.get('percent', 100.0)}%** "
            f"({overall.get('documented', 0)} of {overall.get('total', 0)} public modules, types, and callables). "
            "Data members are excluded from the ratio.",
            "",
            "[Back to index](index.md)",
            "",
            "## By kind",
            "",
            "| Kind | Documented | Total | Coverage |",
            "|---|---|---|---|",
        ]
        for kind, stats in cov.get("by_kind", {}).items():
            lines.append(f"| {kind} | {stats['documented']} | {stats['total']} | {stats['percent']}% |")
        lines.extend(["", "## By module (lowest first)", "", "| Module | Documented | Total | Coverage |", "|---|---|---|---|"])
        by_module = sorted(cov.get("by_module", {}).items(), key=lambda kv: (kv[1]["percent"], kv[0]))
        for uid, stats in by_module:
            entity = reference.entities.get(uid)
            label = self._top_link(linker, entity) if entity else _inline_code(uid)
            lines.append(f"| {label} | {stats['documented']} | {stats['total']} | {stats['percent']}% |")
        counts: Dict[str, int] = {}
        for warning in reference.warnings:
            counts[warning.code] = counts.get(warning.code, 0) + 1
        lines.extend([
            "",
            "## Warnings",
            "",
            "DOC001 undocumented public item, DOC002 parameter not documented, "
            "DOC003 documented parameter missing from the signature (stale doc), "
            "DOC004 return value not documented, DOC005 raised exception not documented.",
            "",
        ])
        if counts:
            lines.append(", ".join(f"{code}: {num}" for code, num in sorted(counts.items())))
            lines.append("")
        cap = max(1, int(self._config.APIDOCS_MAX_WARNINGS_LISTED))
        for warning in reference.warnings[:cap]:
            lines.append(f"- {warning.code} `{warning.file}:{warning.line}` {warning.message}")
        if len(reference.warnings) > cap:
            lines.append(f"- ... {len(reference.warnings) - cap} more in `{jsonl_warnings_path(self._config)}`")
        if not reference.warnings:
            lines.append("No warnings.")
        return "\n".join(lines).rstrip() + "\n"

    def _source_link(self, entity: ApiEntity) -> str:
        """Relative link from a module page to the source line."""
        depth = len(PurePosixPath(self._config.APIDOCS_OUTPUT_DIR).parts) + len(
            PurePosixPath(self._config.APIDOCS_MODULES_SUBDIR).parts
        )
        prefix = "../" * depth
        return f"[{entity.file}:{entity.line}]({prefix}{entity.file}#L{entity.line})"

    def _module(self, reference: ApiReference, linker: ApiLinker, uid: str) -> str:
        """Render one module page."""
        module = reference.entities[uid]
        fence = FENCE_LANGUAGES.get(module.language, "")
        stats = reference.coverage.get("by_module", {}).get(uid, {})
        top = reference.children(uid)
        lines = [
            f"# {_inline_code(module_display_name(module))}",
            "",
            f"> Source: {self._source_link(module)} | language `{module.language}` | "
            f"coverage {stats.get('percent', 100.0)}% | [API index](../index.md)",
            "",
        ]
        lines.extend(self._doc_block(module.doc, linker, uid, module))
        sections: List[Tuple[str, List[ApiEntity]]] = []
        for kind in CLASS_KINDS + ("function", "macro", "constant", "variable"):
            items = [e for e in top if e.kind == kind]
            if items:
                sections.append((KIND_TITLES.get(kind, kind.capitalize() + "s"), items))
        others = [e for e in top if e.kind not in CLASS_KINDS + ("function", "macro", "constant", "variable")]
        if others:
            sections.append(("Other Members", others))
        if sections:
            lines.extend(["## Contents", ""])
            for title, items in sections:
                lines.append(f"- **{title}:** " + ", ".join(linker.link(e, uid, e.name) for e in items))
            lines.append("")
        diagram = self._class_diagram(reference, uid)
        if diagram:
            lines.extend(["## Type Diagram", "", "```mermaid", diagram, "```", ""])
        callgraph = self._call_graph(reference, uid)
        if callgraph:
            lines.extend(["## Call Graph", "", "Solid arrows stay in this module, dashed arrows leave it.", "",
                          "```mermaid", callgraph, "```", ""])
        for title, items in sections:
            lines.extend([f"## {title}", ""])
            for entity in items:
                lines.extend(self._entity(reference, linker, entity, uid, fence, 3))
        return "\n".join(lines).rstrip() + "\n"

    def _entity(
        self, reference: ApiReference, linker: ApiLinker, entity: ApiEntity,
        module_uid: str, fence: str, level: int,
    ) -> List[str]:
        """Render one entity block (recursing into members of types)."""
        heading = "#" * min(level, 6)
        badges = [entity.kind] + [m for m in entity.modifiers if m != entity.kind]
        if entity.visibility != "public":
            badges.append(entity.visibility)
        if entity.doc.deprecated:
            badges.append("deprecated")
        lines = [
            f'<a id="{anchor_slug(entity.qualname)}"></a>',
            "",
            f"{heading} {_inline_code(entity.qualname)}",
            "",
            " ".join(f"`{b}`" for b in badges) + f" | {self._source_link(entity)}",
            "",
        ]
        if entity.decorators:
            lines.extend(["Decorators: " + ", ".join(_inline_code("@" + d) for d in entity.decorators), ""])
        if entity.signature:
            lines.extend([f"```{fence}", entity.signature, "```", ""])
        if entity.kind in CLASS_KINDS:
            if entity.bases:
                rendered = []
                for base in entity.bases:
                    target = next(
                        (reference.entities[u] for u in entity.base_uids
                         if u in reference.entities and reference.entities[u].name == re.sub(r"\[.*\]$", "", base).split(".")[-1]),
                        None,
                    )
                    rendered.append(linker.link(target, module_uid, base) if target else _inline_code(base))
                lines.extend(["Bases: " + ", ".join(rendered), ""])
            if entity.subclasses:
                lines.extend(["Subclasses: " + ", ".join(linker.link_uid(u, module_uid) for u in entity.subclasses), ""])
        lines.extend(self._doc_block(entity.doc, linker, module_uid, entity))
        if entity.kind in CALLABLE_KINDS:
            lines.extend(self._call_refs(linker, entity, module_uid))
        if entity.kind in CLASS_KINDS:
            members = reference.children(entity.uid)
            data = [m for m in members if m.kind in DATA_KINDS]
            doc_attrs = {a.name: a for a in entity.doc.attributes}
            if data:
                lines.extend(["**Attributes**", "", "| Name | Type | Default | Description |", "|---|---|---|---|"])
                for item in data:
                    described = item.doc.summary or (doc_attrs[item.name].description if item.name in doc_attrs else "")
                    kind = item.returns or (doc_attrs[item.name].type if item.name in doc_attrs else "")
                    lines.append(
                        f"| {linker.link(item, module_uid, item.name)} | {_cell(_inline_code(kind))} | "
                        f"{_cell(_inline_code(item.value))} | {_cell(linker.autolink(described, module_uid))} |"
                    )
                lines.append("")
            callables = [m for m in members if m.kind not in DATA_KINDS]
            if callables:
                lines.extend(["**Members**", "", "| Member | Kind | Summary |", "|---|---|---|"])
                for item in callables:
                    lines.append(
                        f"| {linker.link(item, module_uid, item.name)} | {item.kind} | "
                        f"{_cell(linker.autolink(self._summary(item), module_uid))} |"
                    )
                lines.append("")
            for item in members:
                if item.kind in DATA_KINDS and item.doc.is_empty:
                    continue
                lines.extend(self._entity(reference, linker, item, module_uid, fence, level + 1))
        if level <= 3:
            lines.extend(["---", ""])
        return lines

    def _doc_block(self, doc: DocComment, linker: ApiLinker, module_uid: str, entity: ApiEntity) -> List[str]:
        """Render summary, description, parameters, returns, raises, examples, and notes."""
        lines: List[str] = []
        if doc.deprecated:
            lines.extend([f"> **Deprecated:** {linker.autolink(doc.deprecated, module_uid)}", ""])
        if doc.summary:
            lines.extend([linker.autolink(doc.summary, module_uid), ""])
        if doc.description:
            lines.extend([linker.autolink(doc.description, module_uid), ""])
        params = self._merged_params(entity, doc)
        if params:
            lines.extend(["**Parameters**", "", "| Name | Type | Default | Description |", "|---|---|---|---|"])
            for item in params:
                lines.append(
                    f"| {_inline_code(item.name)} | {_cell(_inline_code(item.type))} | "
                    f"{_cell(_inline_code(item.default))} | {_cell(linker.autolink(item.description, module_uid))} |"
                )
            lines.append("")
        for label, value in (("Returns", doc.returns), ("Yields", doc.yields)):
            kind = (value.type if value else "") or (entity.returns if label == "Returns" and entity.kind in CALLABLE_KINDS else "")
            if value is None and not (label == "Returns" and kind and kind not in ("None", "void")):
                continue
            desc = linker.autolink(value.description, module_uid) if value else ""
            lines.extend([f"**{label}:** {_inline_code(kind)}{' - ' if kind and desc else ''}{desc}".rstrip(), ""])
        raises = list(doc.raises)
        documented = {r.name.split(".")[-1] for r in raises}
        for name in entity.inferred_raises:
            if name not in documented:
                raises.append(DocField(name=name, description="(raised in the body, not documented)"))
        if raises:
            lines.extend(["**Raises**", ""])
            for item in raises:
                head = linker.autolink(f"`{item.name}`", module_uid) if item.name else ""
                lines.append(f"- {head}{': ' if head and item.description else ''}{linker.autolink(item.description, module_uid)}")
            lines.append("")
        fence = FENCE_LANGUAGES.get(entity.language, "")
        for example in doc.examples:
            lang = "pycon" if example.lstrip().startswith(">>>") else fence
            lines.extend(["**Example**", "", f"```{lang}", example, "```", ""])
        for label, text in doc.notes:
            body = linker.autolink(text, module_uid).replace("\n", "\n> ")
            lines.extend([f"> **{label}:** {body}", ""])
        if doc.since:
            lines.extend([f"*Since:* {doc.since}", ""])
        if doc.see_also:
            refs = []
            for ref in doc.see_also:
                target = linker.resolve(ref, entity.file)
                refs.append(linker.link(target, module_uid, ref) if target else _inline_code(ref))
            lines.extend(["**See also:** " + ", ".join(refs), ""])
        return lines

    @staticmethod
    def _merged_params(entity: ApiEntity, doc: DocComment) -> List[DocField]:
        """Merge signature parameters with documented ones (signature order wins)."""
        if entity.kind not in CALLABLE_KINDS and entity.kind not in CLASS_KINDS:
            return list(doc.params)
        if entity.kind in CLASS_KINDS and "dataclass" in entity.modifiers and not doc.params:
            return []
        merged: List[DocField] = []
        seen = set()
        for param in entity.params:
            if not param.name:
                continue
            documented = doc.param(param.name)
            merged.append(DocField(
                name=param.name,
                type=param.annotation or (documented.type if documented else ""),
                default=param.default or (documented.default if documented else ""),
                description=documented.description if documented else "",
            ))
            seen.add(param.name.lstrip("*$&"))
        for item in doc.params:
            if item.name.lstrip("*$&") not in seen and not entity.params:
                merged.append(item)
        return merged

    def _call_refs(self, linker: ApiLinker, entity: ApiEntity, module_uid: str) -> List[str]:
        """Render Calls / Called by lines capped by APIDOCS_MAX_CALL_REFS."""
        cap = max(1, int(self._config.APIDOCS_MAX_CALL_REFS))
        lines: List[str] = []
        for label, uids in (("Calls", entity.calls), ("Called by", entity.called_by)):
            if not uids:
                continue
            shown = ", ".join(linker.link_uid(u, module_uid) for u in uids[:cap])
            more = f" and {len(uids) - cap} more" if len(uids) > cap else ""
            lines.extend([f"*{label}:* {shown}{more}", ""])
        return lines

    @staticmethod
    def _mermaid_id(uid: str) -> str:
        """Return a Mermaid-safe node id for *uid*."""
        return "n_" + re.sub(r"[^A-Za-z0-9_]", "_", uid)

    @staticmethod
    def _mermaid_label(text: str) -> str:
        """Escape a label for a quoted Mermaid node."""
        return text.replace('"', "#quot;").replace("<", "#lt;").replace(">", "#gt;")

    def _class_diagram(self, reference: ApiReference, uid: str) -> str:
        """Mermaid classDiagram of the module's types with members and bases."""
        types = [e for e in (reference.entities[u] for u in self._descendants(reference, uid)) if e.kind in CLASS_KINDS]
        if not types or (len(types) < 2 and not any(t.base_uids or t.bases for t in types)):
            return ""
        cap = max(1, int(self._config.APIDOCS_CALLGRAPH_MAX_EDGES))
        lines = ["classDiagram", "    direction LR"]
        known: Dict[str, str] = {}
        for entity in types[:cap]:
            cid = re.sub(r"[^A-Za-z0-9_]", "_", entity.qualname)
            known[entity.uid] = cid
            lines.append(f"    class {cid}")
            if entity.kind != "class":
                lines.append(f"    <<{entity.kind}>> {cid}")
            for member in reference.children(entity.uid)[:cap]:
                name = re.sub(r"[^A-Za-z0-9_]", "_", member.name)
                if member.kind in DATA_KINDS:
                    kind = re.sub(r"[^A-Za-z0-9_\[\], ]", "", member.returns)[:40]
                    lines.append(f"    {cid} : {kind + ' ' if kind else ''}{name}")
                elif member.kind in CALLABLE_KINDS:
                    lines.append(f"    {cid} : {name}()")
        for entity in types[:cap]:
            for base_uid in entity.base_uids:
                base = reference.entities.get(base_uid)
                if base is None:
                    continue
                base_id = known.get(base_uid) or re.sub(r"[^A-Za-z0-9_]", "_", base.qualname)
                if base_uid not in known:
                    lines.append(f"    class {base_id}")
                    known[base_uid] = base_id
                lines.append(f"    {base_id} <|-- {known[entity.uid]}")
        return "\n".join(lines)

    def _call_graph(self, reference: ApiReference, uid: str) -> str:
        """Mermaid flowchart of calls made by this module's callables."""
        members = [reference.entities[u] for u in self._descendants(reference, uid)]
        pairs: List[Tuple[ApiEntity, ApiEntity]] = []
        for entity in members:
            if entity.kind not in CALLABLE_KINDS:
                continue
            for target_uid in entity.calls:
                target = reference.entities.get(target_uid)
                if target is not None:
                    pairs.append((entity, target))
        if not pairs:
            return ""
        cap = max(1, int(self._config.APIDOCS_CALLGRAPH_MAX_EDGES))
        pairs.sort(key=lambda p: (p[1].file != p[0].file, p[0].line, p[1].uid))
        pairs = pairs[:cap]
        lines = ["flowchart LR"]
        declared: Dict[str, str] = {}
        for source, target in pairs:
            for entity in (source, target):
                if entity.uid not in declared:
                    nid = self._mermaid_id(entity.uid)
                    declared[entity.uid] = nid
                    label = entity.qualname if entity.file == uid else f"{PurePosixPath(entity.file).stem}.{entity.qualname}"
                    shape = f'(["{self._mermaid_label(label)}"])' if entity.file == uid else f'["{self._mermaid_label(label)}"]'
                    lines.append(f"    {nid}{shape}")
        for source, target in pairs:
            arrow = "-->" if target.file == uid else "-.->"
            lines.append(f"    {declared[source.uid]} {arrow} {declared[target.uid]}")
        return "\n".join(lines)


class ApiDocsWriter:
    """Writes the API reference tree (Markdown, JSON, HTML) to disk."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for the output directory and file names.
        """
        self._config = config
        self._markdown = ApiMarkdownRenderer(config)

    def write(
        self,
        reference: ApiReference,
        project_root: str,
        project_name: str = "",
        architecture_markdown: str = "",
        flow_graphs: Optional[List[FlowGraph]] = None,
    ) -> Dict[str, str]:
        """Write every page and prune stale module pages.

        Refuses to write through a symlinked output directory.

        Args:
            reference: The API reference.
            project_root: Project root directory.
            project_name: Display name (defaults to the root directory name).
            architecture_markdown: Optional architecture and execution-flow
                Markdown (written as ``architecture.md``).
            flow_graphs: Laid-out diagrams drawn in the HTML Flows tab and in
                the standalone FLOWS_OUTPUT page.

        Returns:
            Mapping of relative output path to absolute written path.
        """
        cfg = self._config
        root = Path(project_root).resolve()
        out_dir = root / cfg.APIDOCS_OUTPUT_DIR
        jsonl_dir = out_dir / cfg.APIDOCS_JSONL_DIR
        jsonl_modules = jsonl_dir / cfg.APIDOCS_JSONL_MODULES_SUBDIR
        if any(p.is_symlink() for p in (out_dir, out_dir / cfg.APIDOCS_MODULES_SUBDIR, jsonl_dir, jsonl_modules)):
            raise OSError(f"Refusing to write API docs through a symlink: {out_dir}")
        name = project_name or root.name
        pages = self._markdown.render(reference, name)
        if architecture_markdown:
            pages[cfg.APIDOCS_ARCHITECTURE_FILENAME] = (
                f"# {name} Architecture and Execution Flows\n\n[Back to index](index.md)\n\n"
                + architecture_markdown.rstrip() + "\n"
            )
        pages.update(jsonl_pages(reference, cfg))
        if cfg.APIDOCS_JSON_MONOLITH:
            pages[cfg.APIDOCS_JSON_FILENAME] = json.dumps(
                reference.to_dict(cfg.APIDOCS_SCHEMA_VERSION), indent=1, sort_keys=False
            ) + "\n"
        if cfg.APIDOCS_HTML_ENABLED:
            pages[cfg.APIDOCS_HTML_FILENAME] = render_api_site(reference, name, cfg, flow_graphs or [])
            if flow_graphs:
                pages[cfg.FLOWS_OUTPUT] = render_flows_page(flow_graphs, name, cfg.APIDOCS_HTML_FILENAME, cfg)
        modules_dir = out_dir / cfg.APIDOCS_MODULES_SUBDIR
        modules_dir.mkdir(parents=True, exist_ok=True)
        expected = {
            str(PurePosixPath(rel).name)
            for rel in pages
            if PurePosixPath(rel).parent == PurePosixPath(cfg.APIDOCS_MODULES_SUBDIR)
        }
        for stale in sorted(modules_dir.glob("*.md")):
            if stale.name not in expected and stale.is_file() and not stale.is_symlink():
                stale.unlink()
        self._prune_jsonl(out_dir, pages)
        written: Dict[str, str] = {}
        for rel, text in sorted(pages.items()):
            target = out_dir / rel
            if target.is_symlink():
                logger.warning("Skipping symlinked API docs target %s", target)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.is_file() and target.read_text(encoding="utf-8", errors="ignore") == text:
                written[rel] = str(target)
                continue
            target.write_text(text, encoding="utf-8")
            written[rel] = str(target)
        logger.info(
            "API reference: %d modules, %d entities, coverage %s%% -> %s",
            len(reference.modules), len(reference.entities),
            reference.coverage.get("overall", {}).get("percent", 100.0),
            os.path.relpath(out_dir, root),
        )
        return written

    def _prune_jsonl(self, out_dir: Path, pages: Dict[str, str]) -> None:
        """Remove stale per-module JSONL files and a disabled monolithic api.json.

        Args:
            out_dir: API reference output directory.
            pages: Pages about to be written (relative path to text).
        """
        cfg = self._config
        jsonl_modules = out_dir / cfg.APIDOCS_JSONL_DIR / cfg.APIDOCS_JSONL_MODULES_SUBDIR
        if jsonl_modules.is_dir():
            for stale in sorted(jsonl_modules.glob("*.jsonl")):
                rel = str(PurePosixPath(stale.relative_to(out_dir).as_posix()))
                if rel not in pages and stale.is_file() and not stale.is_symlink():
                    stale.unlink()
        monolith = out_dir / cfg.APIDOCS_JSON_FILENAME
        if not cfg.APIDOCS_JSON_MONOLITH and monolith.is_file() and not monolith.is_symlink():
            monolith.unlink()
