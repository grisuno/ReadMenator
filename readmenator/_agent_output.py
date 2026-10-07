"""Agent-friendly output generator for ReadMenator.

Generates grep-optimized, flat-markdown files in a dedicated output
directory.  File names for per-subsystem files are **inferred** from the
project's directory structure, never hardcoded.  The generated files are
designed to be consumed by AI agents that perform ``grep`` / ``read``
operations and need queryable, small-context documents.

Every document is capped at ``AGENT_OUTPUT_MAX_LINES``: oversized
documents are split on section boundaries into ``NAME.md``,
``NAME_p2.md``, ... with the table header repeated on each page, so a
``grep`` over ``NAME*.md`` still sees every line and a single read never
blows an agent's context window.

Output layout::

    readmenator-agent/
    ├── MANIFEST.json         # freshness (git commit), read order, token costs
    ├── INDEX.md              # file -> purpose -> blast radius map
    ├── SYMBOLS.md            # one line per symbol
    ├── ARCHITECTURE.md       # dependency pairs (flat list)
    ├── SECURITY.md           # findings by severity
    ├── API.md                # public functions, one line each
    ├── GOTCHAS.md            # "don't change X because Y"
    ├── recipes/
    │   └── *.md              # actionable task blocks
    └── KB_<subsystem>.md     # 1 file per inferred subsystem
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from readmenator._cache import source_fingerprint
from readmenator._config import Config
from readmenator._gitmeta import read_git_head
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    Node,
    SecurityFinding,
    Symbol,
)
from readmenator._purpose import escape_cell, file_purpose, first_sentence, truncate_words
from readmenator._resolver import ImportResolver
from readmenator._security import fix_hint_for

logger = logging.getLogger(__name__)

_SEVERITY_ORDER = ("critical", "high", "medium", "low", "info")
_PAGE_SUFFIX = "_p"
_MANIFEST_SCHEMA_VERSION = 2
_TABLE_RULE_RE = re.compile(r"^\|[-| :]+\|$")
_OWNED_MD_RE = re.compile(
    r"^(INDEX|SYMBOLS|ARCHITECTURE|SECURITY|API|GOTCHAS|KB_[\w-]+?)(_p\d+)?\.md$"
)
_CLASS_KINDS = ("class", "struct", "interface", "trait", "enum", "record", "protocol")
_PUBLIC_DUNDERS = ("__init__", "__call__")
_PAGE_OVERHEAD_LINES = 4


class AgentOutputGenerator:
    """Generates agent-friendly, grep-optimised output files.

    All output is plain Markdown -- no JSON wrapping, no fenced code
    blocks around data structures.  Every line is greppable.
    """

    def __init__(self, config: Config) -> None:
        """Store configuration for output paths and size budgets."""
        self._config = config

    def generate(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: List[Edge],
        analysis: Optional[AnalysisResult],
        analysis_v2: Optional[AnalysisResultV2],
        findings: List[SecurityFinding],
        layers: Dict[str, str],
        project_root: str,
    ) -> str:
        """Write all agent output files and return the output directory path."""
        root = Path(project_root).resolve()
        out_dir = root / self._config.AGENT_OUTPUT_DIR
        out_dir.mkdir(parents=True, exist_ok=True)
        recipes_dir = out_dir / "recipes"
        recipes_dir.mkdir(exist_ok=True)
        self._prune_owned(out_dir)

        files_by_subsystem = self._infer_subsystems(nodes)
        resolved_map = self._build_resolved_map(resolved_edges)
        imported_by = self._build_imported_by_map(resolved_edges)

        documents: Dict[str, str] = {
            "INDEX.md": self._build_index(nodes, files_by_subsystem, imported_by),
            "SYMBOLS.md": self._build_symbols(nodes),
            "ARCHITECTURE.md": self._build_architecture(edges, resolved_edges, nodes),
            "SECURITY.md": self._build_security(findings, nodes),
            "API.md": self._build_api(nodes, resolved_map, imported_by, layers),
            "GOTCHAS.md": self._build_gotchas(
                analysis, analysis_v2, nodes, layers, imported_by,
            ),
        }
        for name, file_nodes in files_by_subsystem.items():
            documents[f"KB_{self._safe_name(name)}.md"] = self._build_subsystem_content(
                name, file_nodes, resolved_map, imported_by, layers,
            )

        written: Dict[str, List[Path]] = {}
        for filename, content in documents.items():
            written[filename] = self._write_paged(out_dir, filename, content)
        self._write_recipes(
            recipes_dir, analysis, analysis_v2, findings, layers,
        )
        self._write(out_dir / "MANIFEST.json", self._build_manifest(
            nodes, edges, resolved_edges, findings, project_root,
            files_by_subsystem, layers, out_dir,
        ))

        logger.info(
            "Agent output written to %s (%d files)",
            out_dir,
            len(list(out_dir.rglob("*.md"))),
        )
        return str(out_dir)

    def _infer_subsystems(
        self, nodes: List[Node],
    ) -> Dict[str, List[Node]]:
        """Group nodes by directory, inferring subsystem names."""
        min_files = self._config.AGENT_OUTPUT_MIN_SUBSYSTEM_FILES
        dir_groups: Dict[str, List[Node]] = defaultdict(list)
        for node in nodes:
            parent = os.path.dirname(node.node_id)
            if not parent:
                parent = "."
            dir_groups[parent].append(node)

        subsystems: Dict[str, List[Node]] = {}
        assigned: Set[str] = set()

        for dir_path, file_nodes in sorted(
            dir_groups.items(), key=lambda kv: (-len(kv[1]), kv[0])
        ):
            if len(file_nodes) >= min_files:
                name = os.path.basename(dir_path)
                if not name or name == ".":
                    name = Path(
                        self._config.OUTPUT_FILENAME
                    ).stem.replace("KNOWLEDGE_BASE", "root")
                if name in subsystems:
                    name = dir_path.replace("/", "_")
                subsystems[name] = file_nodes
                assigned.update(n.node_id for n in file_nodes)

        misc = [n for n in nodes if n.node_id not in assigned]
        if misc:
            subsystems["misc"] = misc

        return subsystems

    def _build_index(
        self,
        nodes: List[Node],
        subsystems: Dict[str, List[Node]],
        imported_by: Optional[Dict[str, List[str]]] = None,
    ) -> str:
        """Build the file -> purpose -> subsystem -> blast radius table."""
        node_to_sub: Dict[str, str] = {}
        for name, members in subsystems.items():
            for n in members:
                node_to_sub[n.node_id] = name
        users = imported_by or {}

        lines = [
            "# Index",
            "",
            "| File | Purpose | Subsystem | Symbols | Used by |",
            "|------|---------|-----------|---------|---------|",
        ]
        for node in sorted(nodes, key=lambda n: n.node_id):
            purpose = escape_cell(
                file_purpose(node, self._config.AGENT_PURPOSE_MAX_CHARS)
            ) or "-"
            sub = node_to_sub.get(node.node_id, "-")
            used_by = len(set(users.get(node.node_id, [])))
            lines.append(
                f"| `{node.node_id}` | {purpose} | {sub} | "
                f"{len(node.symbols)} | {used_by} |"
            )
        lines.append("")
        return "\n".join(lines)

    def _build_architecture(
        self,
        edges: List[Edge],
        resolved_edges: List[Edge],
        nodes: List[Node],
    ) -> str:
        """Build internal dependency pairs plus per-file external imports.

        External imports exclude raw import strings that resolved to a
        project file, so internal modules are never listed twice.
        """
        node_ids = {n.node_id for n in nodes}
        lines = [
            "# Architecture",
            "",
            "## Internal Dependencies",
            "",
        ]
        internal = sorted({
            (e.source, e.target) for e in resolved_edges
            if e.source in node_ids and e.target in node_ids
        })
        if internal:
            for source, target in internal:
                lines.append(f"- `{source}` -> `{target}`")
        else:
            lines.append("- (no internal resolved imports)")

        lines.extend([
            "",
            "## External Imports",
            "",
        ])
        resolver = ImportResolver(sorted(node_ids))
        external: Dict[str, Set[str]] = defaultdict(set)
        for e in edges:
            if e.relation not in ("imports", "resolved_imports"):
                continue
            if e.source not in node_ids or e.target in node_ids:
                continue
            if resolver.resolve(e.target, e.source) is not None:
                continue
            external[e.source].add(e.target)
        if external:
            for source in sorted(external):
                targets = ", ".join(sorted(external[source]))
                lines.append(f"- `{source}` -> {targets}")
        else:
            lines.append("- (no external imports detected)")
        lines.append("")
        return "\n".join(lines)

    def _build_security(
        self, findings: List[SecurityFinding], nodes: Optional[List[Node]] = None
    ) -> str:
        """Build findings grouped by severity with scope and fix hints."""
        lines = ["# Security Findings", ""]
        if not findings:
            lines.append("No security findings.")
            return "\n".join(lines)

        symbols_by_file: Dict[str, List[Symbol]] = {
            n.node_id: n.symbols for n in (nodes or [])
        }
        by_severity: Dict[str, List[SecurityFinding]] = defaultdict(list)
        for f in findings:
            by_severity[f.severity].append(f)

        for sev in _SEVERITY_ORDER:
            group = by_severity.get(sev, [])
            if not group:
                continue
            lines.append(f"## {sev.upper()} ({len(group)})")
            lines.append("")
            for f in sorted(group, key=lambda x: (x.file_path, x.line)):
                cwe = f" [{f.cwe}]" if f.cwe else ""
                scope = self._enclosing_symbol(
                    symbols_by_file.get(f.file_path, []), f.line,
                )
                scope_str = f" (in `{scope}`)" if scope else ""
                lines.append(
                    f"- `{f.file_path}:{f.line}`{scope_str} -- {f.description}{cwe}"
                )
                lines.append(f"  Fix: {fix_hint_for(f)}")
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _enclosing_symbol(symbols: List[Symbol], line: int) -> str:
        """Return the nearest symbol defined at or before line."""
        best = ""
        best_line = -1
        for sym in symbols:
            if best_line < sym.line <= line:
                best = sym.name
                best_line = sym.line
        return best

    def _is_public(self, sym: Symbol) -> bool:
        """Return whether a symbol belongs in the public API listing."""
        if not self._config.AGENT_API_PUBLIC_ONLY:
            return True
        return not sym.name.startswith("_") or sym.name in _PUBLIC_DUNDERS

    @staticmethod
    def _qualified_names(symbols: List[Symbol]) -> Dict[int, str]:
        """Map each method's index to ``Owner.method`` using the nearest preceding type."""
        owners = sorted(
            (s.line, s.name) for s in symbols if s.kind in _CLASS_KINDS
        )
        qualified: Dict[int, str] = {}
        for index, sym in enumerate(symbols):
            if sym.kind != "method":
                continue
            owner = ""
            for line, name in owners:
                if line > sym.line:
                    break
                owner = name
            if owner:
                qualified[index] = f"{owner}.{sym.name}"
        return qualified

    def _build_api(
        self,
        nodes: List[Node],
        resolved_map: Dict[Tuple[str, str], str],
        imported_by: Dict[str, List[str]],
        layers: Optional[Dict[str, str]] = None,
    ) -> str:
        """Build one greppable line per public function or method.

        Dependencies and importers are stated once per file instead of
        once per function, and test-layer files are skipped, which keeps
        the listing an API reference rather than a symbol dump.
        """
        lines = ["# API", ""]
        api_kinds = ("function", "method")
        excluded_layers = set(self._config.AGENT_API_EXCLUDE_LAYERS)
        layer_of = layers or {}
        deps_by_src = self._deps_by_source(resolved_map)
        doc_max = self._config.AGENT_DOC_MAX_CHARS
        sig_max = self._config.AGENT_SIGNATURE_MAX_CHARS

        for node in sorted(nodes, key=lambda n: n.node_id):
            if layer_of.get(node.node_id, "") in excluded_layers:
                continue
            qualified = self._qualified_names(node.symbols)
            entries = [
                (index, s) for index, s in enumerate(node.symbols)
                if s.kind in api_kinds and self._is_public(s)
            ]
            if not entries:
                continue
            lines.append(f"## {node.node_id}")
            deps = deps_by_src.get(node.node_id, [])
            if deps:
                lines.append(
                    "Depends on: " + ", ".join(f"`{d}`" for d in deps)
                )
            callers = sorted(set(imported_by.get(node.node_id, [])))
            if callers:
                lines.append(
                    "Imported by: " + ", ".join(f"`{c}`" for c in callers)
                )
            for index, fn in sorted(entries, key=lambda item: item[1].line):
                name = qualified.get(index, fn.name)
                sig = (
                    f" `{truncate_words(fn.signature, sig_max)}`"
                    if fn.signature else ""
                )
                doc = first_sentence(fn.doc) if fn.doc else ""
                doc_str = f" -- {truncate_words(doc, doc_max)}" if doc else ""
                lines.append(
                    f"- `{name}` ({fn.kind}) `{node.node_id}:{fn.line}`{sig}{doc_str}"
                )
            lines.append("")
        if len(lines) == 2:
            lines.append("No public functions detected.")
        return "\n".join(lines)

    def _build_manifest(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: List[Edge],
        findings: List[SecurityFinding],
        project_root: str,
        subsystems: Optional[Dict[str, List[Node]]] = None,
        layers: Optional[Dict[str, str]] = None,
        out_dir: Optional[Path] = None,
    ) -> str:
        """Build MANIFEST.json: freshness, entry points, read order, costs.

        The project root is recorded relatively (never an absolute path),
        and the git commit lets agents detect a stale knowledge base with
        one ``git rev-parse HEAD`` instead of re-reading everything.
        """
        langs: Dict[str, int] = {}
        for n in nodes:
            langs[n.language] = langs.get(n.language, 0) + 1
        relations: Dict[str, int] = defaultdict(int)
        for e in edges:
            relations[e.relation] += 1
        git = read_git_head(project_root)
        agent_dir = self._config.AGENT_OUTPUT_DIR
        wiki_dir = self._config.WIKI_OUTPUT_DIR
        manifest = {
            "tool": "readmenator",
            "schema_version": _MANIFEST_SCHEMA_VERSION,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "project_root": ".",
            "project_name": Path(project_root).resolve().name,
            "git_commit": git["commit"],
            "git_branch": git["branch"],
            "source_fingerprint": source_fingerprint(
                project_root, (n.node_id for n in nodes),
            ),
            "freshness_check": (
                "readmenator . fresh  # exit 0 = docs match sources, "
                "exit 1 = run: readmenator . --rebuild"
            ),
            "files": len(nodes),
            "symbols": sum(len(n.symbols) for n in nodes),
            "imports": relations.get("imports", 0),
            "calls": relations.get("calls", 0),
            "inherits": relations.get("inherits", 0),
            "resolved_imports": len(resolved_edges),
            "security_findings": len(findings),
            "languages": dict(sorted(langs.items())),
            "subsystems": {
                name: len(members)
                for name, members in sorted((subsystems or {}).items())
            },
            "entrypoints": self._entrypoints(nodes, layers or {}),
            "start_here": "INDEX.md",
            "read_order": [
                f"{wiki_dir}/index.md  # big picture, communities, god nodes",
                f"{agent_dir}/INDEX.md  # file -> purpose -> used-by count",
                f"{agent_dir}/GOTCHAS.md  # blast radius before editing",
                f"{agent_dir}/KB_<subsystem>.md  # only the subsystem you touch",
            ],
            "workflow": [
                "ls *.md readmenator-*/  # orient: docs first, ignore build noise",
                "grep -n '<keyword>' INDEX*.md SYMBOLS*.md",
                "cat KB_<subsystem>.md",
                "grep -n '<file>' ARCHITECTURE*.md API*.md",
            ],
            "documents": self._inventory(out_dir) if out_dir is not None else [],
            "regenerate": "readmenator . --rebuild",
        }
        return json.dumps(manifest, indent=2, ensure_ascii=False)

    def _entrypoints(self, nodes: List[Node], layers: Dict[str, str]) -> List[str]:
        """Return likely program entry points, shallowest paths first."""
        names = set(self._config.AGENT_ENTRYPOINT_FILENAMES)
        excluded = set(self._config.AGENT_GOTCHAS_EXCLUDE_LAYERS)
        found = [
            n.node_id for n in nodes
            if n.label in names and layers.get(n.node_id, "") not in excluded
        ]
        found.sort(key=lambda nid: (nid.count("/"), nid))
        return found[: self._config.AGENT_GOTCHAS_TOP_N]

    def _inventory(self, out_dir: Path) -> List[Dict[str, object]]:
        """List generated documents with line counts and token estimates."""
        chars_per_token = max(1, self._config.AGENT_CHARS_PER_TOKEN)
        inventory: List[Dict[str, object]] = []
        for path in sorted(out_dir.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            inventory.append({
                "path": path.relative_to(out_dir).as_posix(),
                "lines": len(text.splitlines()),
                "approx_tokens": max(1, len(text) // chars_per_token),
            })
        return inventory

    def _build_symbols(self, nodes: List[Node]) -> str:
        """Build grep-friendly symbol index (one line per symbol)."""
        lines = ["# Symbols", "",
                 "| Symbol | Kind | File:Line | Signature |",
                 "|--------|------|-----------|-----------|"]
        sig_max = self._config.AGENT_SIGNATURE_MAX_CHARS
        for node in sorted(nodes, key=lambda n: n.node_id):
            for s in sorted(node.symbols, key=lambda x: (x.name, x.line)):
                sig = escape_cell(truncate_words(s.signature or "", sig_max))
                lines.append(f"| `{s.name}` | {s.kind} | "
                             f"`{node.node_id}:{s.line}` | `{sig}` |")
        lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _closed_loop(cycle: List[str]) -> str:
        """Render a cycle as a closed loop without duplicating a closed tail."""
        loop = list(cycle)
        if loop and loop[-1] != loop[0]:
            loop.append(loop[0])
        return " -> ".join(f"`{f}`" for f in loop)

    def _build_gotchas(
        self,
        analysis: Optional[AnalysisResult],
        analysis_v2: Optional[AnalysisResultV2],
        nodes: List[Node],
        layers: Optional[Dict[str, str]] = None,
        imported_by: Optional[Dict[str, List[str]]] = None,
    ) -> str:
        """Build actionable warnings: blast radius, hotspots, cycles, violations.

        Files in excluded layers (tests by default) are left out of the
        centrality lists because their connectivity says nothing about
        the risk of editing production code.
        """
        top_n = self._config.AGENT_GOTCHAS_TOP_N
        excluded = set(self._config.AGENT_GOTCHAS_EXCLUDE_LAYERS)
        layer_of = layers or {}
        users = imported_by or {}

        def keep(file_id: str) -> bool:
            """Return whether a file belongs in the gotcha lists."""
            return layer_of.get(file_id, "") not in excluded

        lines = ["# Gotchas", ""]
        found = False

        god_nodes = [
            (nid, score) for nid, score in (analysis.god_nodes if analysis else [])
            if keep(nid)
        ][:top_n]
        if god_nodes:
            found = True
            lines.append("## God Nodes (high connectivity)")
            lines.append("")
            lines.append(
                "These files have the most connections. "
                "Changes here have high blast radius."
            )
            lines.append("")
            for nid, score in god_nodes:
                used = len(set(users.get(nid, [])))
                used_str = f", imported by {used} files" if used else ""
                lines.append(f"- `{nid}` (score: {score:.2f}{used_str})")
            lines.append("")

        impacts = sorted(
            (c for c in (analysis_v2.change_impacts if analysis_v2 else [])
             if keep(c.file_id) and c.total_impact > 0),
            key=lambda c: (-c.total_impact, c.file_id),
        )[:top_n]
        if impacts:
            found = True
            lines.append("## Blast Radius (change impact)")
            lines.append("")
            lines.append(
                "Editing these files can break the listed number of dependents. "
                "Run their tests after any change."
            )
            lines.append("")
            for c in impacts:
                lines.append(
                    f"- `{c.file_id}` -- {len(c.direct_dependents)} direct, "
                    f"{c.total_impact} total dependents"
                )
            lines.append("")

        hotspots = [
            h for h in (analysis_v2.hotspots if analysis_v2 else [])
            if keep(h.file_id)
        ][:top_n]
        if hotspots:
            found = True
            lines.append("## Hotspots (complexity + centrality)")
            lines.append("")
            for h in hotspots:
                lines.append(
                    f"- `{h.file_id}` -- complexity: {h.complexity_score:.1f}, "
                    f"centrality: {h.centrality_score:.1f}, "
                    f"combined: {h.combined_score:.1f}"
                )
            lines.append("")

        if analysis_v2 and analysis_v2.cycles:
            found = True
            lines.append("## Dependency Cycles")
            lines.append("")
            lines.append(
                "Circular dependencies. "
                "Refactor to break the cycle."
            )
            lines.append("")
            for c in analysis_v2.cycles[:top_n]:
                lines.append(f"- {self._closed_loop(c.cycle)}")
            lines.append("")

        if analysis_v2 and analysis_v2.layer_violations:
            found = True
            lines.append("## Layer Violations")
            lines.append("")
            for v in analysis_v2.layer_violations[:top_n]:
                lines.append(
                    f"- `{v.source_file}` ({v.source_layer}) -> "
                    f"`{v.target_file}` ({v.target_layer}): {v.description}"
                )
            lines.append("")

        if analysis_v2 and analysis_v2.dataflow_issues:
            found = True
            lines.append("## Dataflow Issues (INFERRED, review each lead)")
            lines.append("")
            for issue in analysis_v2.dataflow_issues[:top_n]:
                lines.append(
                    f"- `{issue.file_path}:{issue.line}` `{issue.function}` "
                    f"[{issue.kind}] `{issue.variable}`: {issue.description}"
                )
            lines.append("")

        if not found:
            lines.append("No gotchas detected.")
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _safe_name(name: str) -> str:
        """Return a filesystem-safe subsystem name."""
        return "".join(
            c if c.isalnum() or c in ("-", "_") else "_"
            for c in name
        )

    def _write_subsystem_files(
        self,
        out_dir: Path,
        subsystems: Dict[str, List[Node]],
        resolved_map: Dict[Tuple[str, str], str],
        imported_by: Dict[str, List[str]],
        layers: Dict[str, str],
    ) -> None:
        """Write one paged KB_<subsystem>.md per inferred subsystem."""
        for name, file_nodes in subsystems.items():
            content = self._build_subsystem_content(
                name, file_nodes, resolved_map, imported_by, layers,
            )
            self._write_paged(out_dir, f"KB_{self._safe_name(name)}.md", content)

    def _build_subsystem_content(
        self,
        name: str,
        file_nodes: List[Node],
        resolved_map: Dict[Tuple[str, str], str],
        imported_by: Dict[str, List[str]],
        layers: Dict[str, str],
    ) -> str:
        """Build per-file context (purpose, layer, symbols, edges) for one subsystem."""
        lines = [f"# Subsystem: {name}", ""]
        deps_by_src = self._deps_by_source(resolved_map)
        purpose_max = self._config.AGENT_PURPOSE_MAX_CHARS
        sig_max = self._config.AGENT_SIGNATURE_MAX_CHARS

        for node in sorted(file_nodes, key=lambda n: n.node_id):
            lines.append(f"## {node.node_id}")
            purpose = file_purpose(node, purpose_max)
            if purpose:
                lines.append(f"- Doc: {purpose}")
            layer = layers.get(node.node_id, "")
            if layer:
                lines.append(f"- Layer: {layer}")
            if node.language:
                lines.append(f"- Language: {node.language}")

            if node.symbols:
                lines.append("- Symbols:")
                for sym in node.symbols:
                    sig = (
                        f" `{truncate_words(sym.signature, sig_max)}`"
                        if sym.signature else ""
                    )
                    lines.append(f"  - `{sym.name}` ({sym.kind}, line {sym.line}){sig}")

            deps = deps_by_src.get(node.node_id, [])
            if deps:
                lines.append(
                    "- Depends on: "
                    + ", ".join(f"`{d}`" for d in deps)
                )

            callers = sorted(set(imported_by.get(node.node_id, [])))
            if callers:
                lines.append(
                    "- Imported by: "
                    + ", ".join(f"`{c}`" for c in callers)
                )
            lines.append("")
        return "\n".join(lines)

    def _write_recipes(
        self,
        recipes_dir: Path,
        analysis: Optional[AnalysisResult],
        analysis_v2: Optional[AnalysisResultV2],
        findings: Optional[List[SecurityFinding]] = None,
        layers: Optional[Dict[str, str]] = None,
    ) -> None:
        """Write task recipes grounded in this project's actual analysis data."""
        agent_dir = self._config.AGENT_OUTPUT_DIR
        excluded = set(self._config.AGENT_GOTCHAS_EXCLUDE_LAYERS)
        layer_of = layers or {}
        cycles = list(analysis_v2.cycles[:3]) if analysis_v2 and analysis_v2.cycles else []
        hotspots = [
            h for h in (analysis_v2.hotspots if analysis_v2 else [])
            if layer_of.get(h.file_id, "") not in excluded
        ][:1]
        impacts = sorted(
            (c for c in (analysis_v2.change_impacts if analysis_v2 else [])
             if layer_of.get(c.file_id, "") not in excluded and c.total_impact > 0),
            key=lambda c: (-c.total_impact, c.file_id),
        )[:1]
        top_findings = sorted(
            findings or [],
            key=lambda f: (
                _SEVERITY_ORDER.index(f.severity) if f.severity in _SEVERITY_ORDER
                else len(_SEVERITY_ORDER),
                f.file_path, f.line,
            ),
        )[:3]

        cycle_lines = ["# Recipe: Fix a Dependency Cycle", ""]
        if cycles:
            cycle_lines.append("Target cycle: " + self._closed_loop(cycles[0].cycle))
            cycle_lines.append("")
            cycle_lines.append(
                "1. Read the imports between these files: "
                + ", ".join(f"`grep -n '^import\\|^from\\|#include' {f}`" for f in dict.fromkeys(cycles[0].cycle))
            )
            cycle_lines.append("2. Move the shared symbols into a new leaf module both sides import")
            cycle_lines.append(f"3. Verify: `readmenator . && grep -c 'Dependency Cycles' {agent_dir}/GOTCHAS.md`")
        else:
            cycle_lines.extend([
                f"1. Read cycles: `grep -A5 'Dependency Cycles' {agent_dir}/GOTCHAS.md`",
                "2. Pick the cycle to break",
                "3. Introduce an interface/abstraction to decouple",
                f"4. Verify: `readmenator . && grep -c 'cycle' {agent_dir}/GOTCHAS.md`",
            ])
        cycle_lines.append("")
        self._write(recipes_dir / "fix-cycle.md", "\n".join(cycle_lines))

        security_lines = ["# Recipe: Fix a Security Finding", ""]
        if top_findings:
            for f in top_findings:
                security_lines.append(
                    f"- `{f.file_path}:{f.line}` [{f.severity}] {f.rule_id}: {f.description}"
                )
                security_lines.append(f"  Fix: {fix_hint_for(f)}")
            security_lines.append("")
            security_lines.append(
                f"Verify: `readmenator . --audit && grep -c 'CRITICAL\\|HIGH' {agent_dir}/SECURITY.md`"
            )
        else:
            security_lines.extend([
                f"1. Read findings: `grep -n '<file>' {agent_dir}/SECURITY.md`",
                f"2. Check API contract: `grep -n '<function>' {agent_dir}/API*.md`",
                "3. Apply fix",
                f"4. Verify: `readmenator . --audit && grep -c 'CRITICAL\\|HIGH' {agent_dir}/SECURITY.md`",
            ])
        security_lines.append("")
        self._write(recipes_dir / "fix-security.md", "\n".join(security_lines))

        hotspot_lines = ["# Recipe: Reduce File Complexity", ""]
        if hotspots:
            hotspot_lines.append(f"Target hotspot: `{hotspots[0].file_id}`")
            hotspot_lines.append(
                f"(complexity {hotspots[0].complexity_score:.1f}, "
                f"centrality {hotspots[0].centrality_score:.1f})"
            )
            hotspot_lines.append("")
            hotspot_lines.append(
                f"1. Read dependents: `grep -n '{hotspots[0].file_id}' {agent_dir}/ARCHITECTURE*.md`"
            )
            hotspot_lines.append("2. Extract functions/classes into new files in the same subsystem")
            hotspot_lines.append("3. Update imports")
            hotspot_lines.append("4. Regenerate: `readmenator .`")
        else:
            hotspot_lines.extend([
                f"1. Read hotspots: `grep -A5 'Hotspots' {agent_dir}/GOTCHAS.md`",
                "2. Pick the worst offender",
                "3. Extract functions/classes into new files in the same subsystem",
                "4. Update imports",
                "5. Regenerate: `readmenator .`",
            ])
        hotspot_lines.append("")
        self._write(recipes_dir / "reduce-complexity.md", "\n".join(hotspot_lines))

        impact_lines = ["# Recipe: Change a File Safely", ""]
        if impacts:
            target = impacts[0]
            impact_lines.append(
                f"Riskiest file: `{target.file_id}` ({target.total_impact} dependents)"
            )
            impact_lines.append("")
        impact_lines.extend([
            f"1. Who depends on it: `grep -n -- '-> `<file>`' {agent_dir}/ARCHITECTURE*.md`",
            f"2. Its public surface: `grep -n '`<file>:' {agent_dir}/API*.md`",
            f"3. Known risks: `grep -n '<file>' {agent_dir}/GOTCHAS.md {agent_dir}/SECURITY.md`",
            "4. Keep signatures stable or update every importer found in step 1",
            "5. Regenerate: `readmenator .`",
            "",
        ])
        self._write(recipes_dir / "change-impact.md", "\n".join(impact_lines))

        self._write(
            recipes_dir / "add-function.md",
            "# Recipe: Add a Function\n"
            "\n"
            f"1. Find the target file by purpose: `grep -in '<topic>' {agent_dir}/INDEX*.md`\n"
            f"2. Reuse before writing: `grep -in '<verb or noun>' {agent_dir}/SYMBOLS*.md`\n"
            f"3. Read the subsystem context: `cat {agent_dir}/KB_<subsystem>.md`\n"
            f"4. Check dependencies: `grep -n '<filename>' {agent_dir}/ARCHITECTURE*.md`\n"
            "5. Edit the file\n"
            "6. Regenerate: `readmenator .`\n"
            "\n",
        )

    @staticmethod
    def _deps_by_source(
        resolved_map: Dict[Tuple[str, str], str],
    ) -> Dict[str, List[str]]:
        """Index resolved dependencies by source file, sorted and deduplicated."""
        deps: Dict[str, Set[str]] = defaultdict(set)
        for (src, tgt) in resolved_map:
            deps[src].add(tgt)
        return {src: sorted(targets) for src, targets in deps.items()}

    @staticmethod
    def _build_resolved_map(
        resolved_edges: List[Edge],
    ) -> Dict[Tuple[str, str], str]:
        """Map (source, target) pairs to their relation."""
        mapping: Dict[Tuple[str, str], str] = {}
        for e in resolved_edges:
            mapping[(e.source, e.target)] = e.relation
        return mapping

    @staticmethod
    def _build_imported_by_map(
        resolved_edges: List[Edge],
    ) -> Dict[str, List[str]]:
        """Map each file to the files that import it."""
        result: Dict[str, List[str]] = defaultdict(list)
        for e in resolved_edges:
            result[e.target].append(e.source)
        return result

    @staticmethod
    def _page_name(filename: str, page: int) -> str:
        """Return the file name of a page (page 1 keeps the original name)."""
        if page <= 1:
            return filename
        stem, ext = os.path.splitext(filename)
        return f"{stem}{_PAGE_SUFFIX}{page}{ext}"

    @staticmethod
    def _split_units(body: List[str], is_table: bool) -> List[List[str]]:
        """Split a document body into atomic units that should not straddle pages."""
        if is_table:
            return [[line] for line in body]
        units: List[List[str]] = []
        for line in body:
            if line.startswith("## ") or not units:
                units.append([line])
            else:
                units[-1].append(line)
        return units

    @staticmethod
    def _chunk_unit(unit: List[str], budget: int) -> List[List[str]]:
        """Split an oversized unit into budget-sized chunks with continued headings."""
        if len(unit) <= budget:
            return [unit]
        heading = unit[0] if unit[0].startswith("#") else ""
        chunks: List[List[str]] = []
        rest = list(unit)
        first = True
        while rest:
            size = budget if first or not heading else budget - 1
            piece, rest = rest[:size], rest[size:]
            if not first and heading:
                piece = [f"{heading} (continued)"] + piece
            chunks.append(piece)
            first = False
        return chunks

    def _paginate(self, filename: str, content: str) -> List[str]:
        """Split a document into pages that each respect the line cap."""
        cap = self._config.AGENT_OUTPUT_MAX_LINES
        lines = content.rstrip("\n").split("\n")
        if cap <= 0 or len(lines) <= cap:
            return [content]
        title, body = lines[0], lines[1:]
        preamble: List[str] = []
        for index, line in enumerate(body[:cap]):
            if _TABLE_RULE_RE.match(line):
                preamble, body = body[: index + 1], body[index + 1:]
                break
        is_table = bool(preamble)
        if not is_table:
            preamble = [""]
            while body and not body[0].strip():
                body = body[1:]
        budget = max(1, cap - len(preamble) - _PAGE_OVERHEAD_LINES)
        pages: List[List[str]] = [[]]
        for unit in self._split_units(body, is_table):
            for chunk in self._chunk_unit(unit, budget):
                if pages[-1] and len(pages[-1]) + len(chunk) > budget:
                    pages.append([])
                pages[-1].extend(chunk)
        total = len(pages)
        names = [self._page_name(filename, i + 1) for i in range(total)]
        rendered: List[str] = []
        for i, chunk in enumerate(pages):
            head = [f"{title} (page {i + 1} of {total})"]
            if i == 0:
                head.append("Pages: " + ", ".join(f"[{n}]({n})" for n in names))
            else:
                head.append(f"Previous: [{names[i - 1]}]({names[i - 1]})")
            tail = [""]
            if i + 1 < total:
                tail.append(f"Next: [{names[i + 1]}]({names[i + 1]})")
            rendered.append("\n".join(head + preamble + chunk + tail) + "\n")
        return rendered

    def _write_paged(self, out_dir: Path, filename: str, content: str) -> List[Path]:
        """Write a document as one or more capped pages and return their paths."""
        written: List[Path] = []
        for index, page in enumerate(self._paginate(filename, content)):
            path = out_dir / self._page_name(filename, index + 1)
            self._write(path, page)
            written.append(path)
        return written

    @staticmethod
    def _prune_owned(out_dir: Path) -> None:
        """Remove previously generated pages so renamed or shrunk docs leave no stale files."""
        for path in out_dir.glob("*.md"):
            if _OWNED_MD_RE.match(path.name) and path.is_file() and not path.is_symlink():
                path.unlink()

    @staticmethod
    def _write(path: Path, content: str) -> None:
        """Write UTF-8 text content to a path."""
        path.write_text(content, encoding="utf-8")
