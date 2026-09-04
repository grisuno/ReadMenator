"""Agent-friendly output generator for ReadMenator.

Generates grep-optimized, flat-markdown files in a dedicated output
directory.  File names for per-subsystem files are **inferred** from the
project's directory structure, never hardcoded.  The generated files are
designed to be consumed by AI agents that perform ``grep`` / ``read``
operations and need queryable, small-context documents.

Output layout::

    readmenator-agent/
    ├── INDEX.md              # file -> purpose map (1 page)
    ├── ARCHITECTURE.md       # dependency pairs (flat list)
    ├── SECURITY.md           # findings by severity
    ├── API.md                # public functions + contracts
    ├── GOTCHAS.md            # "don't change X because Y"
    ├── recipes/
    │   └── *.md              # actionable task blocks
    └── KB_<subsystem>.md     # 1 file per inferred subsystem
"""

from __future__ import annotations

import logging
import os
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from readmenator._config import Config
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    HotspotResult,
    Node,
    SecurityFinding,
    Symbol,
)

logger = logging.getLogger(__name__)

_SEVERITY_ORDER = ("critical", "high", "medium", "low", "info")


class AgentOutputGenerator:
    """Generates agent-friendly, grep-optimised output files.

    All output is plain Markdown -- no JSON wrapping, no fenced code
    blocks around data structures.  Every line is greppable.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------

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

        files_by_subsystem = self._infer_subsystems(nodes)
        resolved_map = self._build_resolved_map(resolved_edges)
        imported_by = self._build_imported_by_map(resolved_edges)

        self._write(out_dir / "INDEX.md", self._build_index(
            nodes, files_by_subsystem,
        ))
        self._write(out_dir / "ARCHITECTURE.md", self._build_architecture(
            edges, resolved_edges, nodes,
        ))
        self._write(out_dir / "SECURITY.md", self._build_security(findings))
        self._write(out_dir / "API.md", self._build_api(
            nodes, resolved_map, imported_by,
        ))
        self._write(out_dir / "GOTCHAS.md", self._build_gotchas(
            analysis, analysis_v2, nodes,
        ))
        self._write_subsystem_files(
            out_dir, files_by_subsystem, resolved_map, imported_by, layers,
        )
        self._write_recipes(recipes_dir, analysis, analysis_v2)

        logger.info(
            "Agent output written to %s (%d files)",
            out_dir,
            len(list(out_dir.rglob("*.md"))),
        )
        return str(out_dir)

    # ------------------------------------------------------------------
    # Subsystem inference
    # ------------------------------------------------------------------

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
        assigned: set[str] = set()

        for dir_path, file_nodes in sorted(
            dir_groups.items(), key=lambda kv: -len(kv[1])
        ):
            if len(file_nodes) >= min_files:
                name = os.path.basename(dir_path)
                if not name or name == ".":
                    name = Path(
                        self._config.OUTPUT_FILENAME
                    ).stem.replace("KNOWLEDGE_BASE", "root")
                subsystems[name] = file_nodes
                assigned.update(n.node_id for n in file_nodes)

        misc = [n for n in nodes if n.node_id not in assigned]
        if misc:
            subsystems["misc"] = misc

        return subsystems

    # ------------------------------------------------------------------
    # INDEX.md
    # ------------------------------------------------------------------

    def _build_index(
        self,
        nodes: List[Node],
        subsystems: Dict[str, List[Node]],
    ) -> str:
        node_to_sub: Dict[str, str] = {}
        for name, members in subsystems.items():
            for n in members:
                node_to_sub[n.node_id] = name

        lines = [
            "# Index",
            "",
            "| File | Purpose | Subsystem | Symbols |",
            "|------|---------|-----------|---------|",
        ]
        for node in sorted(nodes, key=lambda n: n.node_id):
            purpose = (node.doc.split("\n")[0][:80] if node.doc else "-")
            sub = node_to_sub.get(node.node_id, "-")
            sym_count = len(node.symbols)
            lines.append(
                f"| `{node.node_id}` | {purpose} | {sub} | {sym_count} |"
            )
        lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # ARCHITECTURE.md
    # ------------------------------------------------------------------

    def _build_architecture(
        self,
        edges: List[Edge],
        resolved_edges: List[Edge],
        nodes: List[Node],
    ) -> str:
        node_ids = {n.node_id for n in nodes}
        lines = [
            "# Architecture",
            "",
            "## Internal Dependencies",
            "",
        ]
        internal = [
            e for e in resolved_edges
            if e.source in node_ids and e.target in node_ids
        ]
        if internal:
            for e in sorted(internal, key=lambda x: (x.source, x.target)):
                lines.append(f"- `{e.source}` -> `{e.target}`")
        else:
            lines.append("- (no internal resolved imports)")

        lines.extend([
            "",
            "## External Imports",
            "",
        ])
        external = [
            e for e in edges
            if e.source in node_ids and e.target not in node_ids
        ]
        if external:
            for e in sorted(external, key=lambda x: (x.source, x.target)):
                lines.append(f"- `{e.source}` -> `{e.target}`")
        else:
            lines.append("- (no external imports detected)")
        lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # SECURITY.md
    # ------------------------------------------------------------------

    def _build_security(self, findings: List[SecurityFinding]) -> str:
        lines = ["# Security Findings", ""]
        if not findings:
            lines.append("No security findings.")
            return "\n".join(lines)

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
                lines.append(
                    f"- `{f.file_path}:{f.line}` -- {f.description}{cwe}"
                )
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # API.md
    # ------------------------------------------------------------------

    def _build_api(
        self,
        nodes: List[Node],
        resolved_map: Dict[Tuple[str, str], str],
        imported_by: Dict[str, List[str]],
    ) -> str:
        lines = ["# API", ""]
        functions = [
            sym
            for node in nodes
            for sym in node.symbols
            if sym.kind in ("function", "method")
        ]
        if not functions:
            lines.append("No public functions detected.")
            return "\n".join(lines)

        for node in sorted(nodes, key=lambda n: n.node_id):
            node_fns = [
                s for s in node.symbols
                if s.kind in ("function", "method")
            ]
            if not node_fns:
                continue
            lines.append(f"## {node.node_id}")
            lines.append("")
            for fn in node_fns:
                sig = f" `{fn.signature}`" if fn.signature else ""
                lines.append(f"### {fn.name}{sig}")
                lines.append(f"- Defined: `{node.node_id}:{fn.line}`")
                if fn.doc:
                    doc_line = fn.doc.split("\n")[0][:120]
                    lines.append(f"- Doc: {doc_line}")

                deps = []
                for target in list(resolved_map.keys()):
                    if target[0] == node.node_id:
                        deps.append(target[1])
                if deps:
                    lines.append(
                        "- Depends on: "
                        + ", ".join(f"`{d}`" for d in sorted(deps))
                    )

                callers = imported_by.get(node.node_id, [])
                if callers:
                    lines.append(
                        "- Imported by: "
                        + ", ".join(f"`{c}`" for c in sorted(callers))
                    )
                lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # GOTCHAS.md
    # ------------------------------------------------------------------

    def _build_gotchas(
        self,
        analysis: Optional[AnalysisResult],
        analysis_v2: Optional[AnalysisResultV2],
        nodes: List[Node],
    ) -> str:
        lines = ["# Gotchas", ""]

        if analysis and analysis.god_nodes:
            lines.append("## God Nodes (high connectivity)")
            lines.append("")
            lines.append(
                "These files have the most connections. "
                "Changes here have high blast radius."
            )
            lines.append("")
            for nid, score in analysis.god_nodes[:10]:
                lines.append(f"- `{nid}` (score: {score:.2f})")
            lines.append("")

        if analysis_v2 and analysis_v2.hotspots:
            lines.append("## Hotspots (complexity + centrality)")
            lines.append("")
            for h in analysis_v2.hotspots[:10]:
                lines.append(
                    f"- `{h.file_id}` -- complexity: {h.complexity_score:.1f}, "
                    f"centrality: {h.centrality_score:.1f}, "
                    f"combined: {h.combined_score:.1f}"
                )
            lines.append("")

        if analysis_v2 and analysis_v2.cycles:
            lines.append("## Dependency Cycles")
            lines.append("")
            lines.append(
                "Circular dependencies. "
                "Refactor to break the cycle."
            )
            lines.append("")
            for c in analysis_v2.cycles[:10]:
                cycle_str = " -> ".join(f"`{f}`" for f in c.cycle)
                lines.append(f"- {cycle_str}")
            lines.append("")

        if analysis_v2 and analysis_v2.layer_violations:
            lines.append("## Layer Violations")
            lines.append("")
            for v in analysis_v2.layer_violations[:10]:
                lines.append(
                    f"- `{v.source_file}` ({v.source_layer}) -> "
                    f"`{v.target_file}` ({v.target_layer}): {v.description}"
                )
            lines.append("")

        if not any([
            analysis and analysis.god_nodes,
            analysis_v2 and analysis_v2.hotspots,
            analysis_v2 and analysis_v2.cycles,
            analysis_v2 and analysis_v2.layer_violations,
        ]):
            lines.append("No gotchas detected.")
            lines.append("")

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Per-subsystem KB files
    # ------------------------------------------------------------------

    def _write_subsystem_files(
        self,
        out_dir: Path,
        subsystems: Dict[str, List[Node]],
        resolved_map: Dict[Tuple[str, str], str],
        imported_by: Dict[str, List[str]],
        layers: Dict[str, str],
    ) -> None:
        for name, file_nodes in subsystems.items():
            safe_name = "".join(
                c if c.isalnum() or c in ("-", "_") else "_"
                for c in name
            )
            path = out_dir / f"KB_{safe_name}.md"
            content = self._build_subsystem_content(
                name, file_nodes, resolved_map, imported_by, layers,
            )
            self._write(path, content)

    def _build_subsystem_content(
        self,
        name: str,
        file_nodes: List[Node],
        resolved_map: Dict[Tuple[str, str], str],
        imported_by: Dict[str, List[str]],
        layers: Dict[str, str],
    ) -> str:
        lines = [f"# Subsystem: {name}", ""]

        for node in sorted(file_nodes, key=lambda n: n.node_id):
            lines.append(f"## {node.node_id}")
            layer = layers.get(node.node_id, "")
            if layer:
                lines.append(f"- Layer: {layer}")
            if node.doc:
                doc_line = node.doc.split("\n")[0][:120]
                lines.append(f"- Doc: {doc_line}")
            if node.language:
                lines.append(f"- Language: {node.language}")

            if node.symbols:
                lines.append("- Symbols:")
                for sym in node.symbols:
                    sig = f" `{sym.signature}`" if sym.signature else ""
                    lines.append(f"  - `{sym.name}` ({sym.kind}, line {sym.line}){sig}")

            deps = []
            for (src, tgt) in resolved_map:
                if src == node.node_id:
                    deps.append(tgt)
            if deps:
                lines.append(
                    "- Depends on: "
                    + ", ".join(f"`{d}`" for d in sorted(deps))
                )

            callers = imported_by.get(node.node_id, [])
            if callers:
                lines.append(
                    "- Imported by: "
                    + ", ".join(f"`{c}`" for c in sorted(callers))
                )
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Recipes
    # ------------------------------------------------------------------

    def _write_recipes(
        self,
        recipes_dir: Path,
        analysis: Optional[AnalysisResult],
        analysis_v2: Optional[AnalysisResultV2],
    ) -> None:
        self._write(
            recipes_dir / "add-function.md",
            "# Recipe: Add a Function\n"
            "\n"
            "1. Find the target file: `grep -rn 'TODO\\|FIXME' readmenator-agent/INDEX.md`\n"
            "2. Read the subsystem context: `cat readmenator-agent/KB_<subsystem>.md`\n"
            "3. Check dependencies: `grep -n '<filename>' readmenator-agent/ARCHITECTURE.md`\n"
            "4. Edit the file\n"
            "5. Regenerate: `readmenator .`\n"
            "\n",
        )
        self._write(
            recipes_dir / "fix-cycle.md",
            "# Recipe: Fix a Dependency Cycle\n"
            "\n"
            "1. Read cycles: `grep -A5 'Dependency Cycles' readmenator-agent/GOTCHAS.md`\n"
            "2. Pick the cycle to break\n"
            "3. Introduce an interface/abstraction to decouple\n"
            "4. Verify: `readmenator . && grep -c 'cycle' readmenator-agent/GOTCHAS.md`\n"
            "\n",
        )
        self._write(
            recipes_dir / "fix-security.md",
            "# Recipe: Fix a Security Finding\n"
            "\n"
            "1. Read findings: `grep -n '<file>' readmenator-agent/SECURITY.md`\n"
            "2. Check API contract: `grep -A10 '<function>' readmenator-agent/API.md`\n"
            "3. Apply fix\n"
            "4. Verify: `readmenator . --audit && grep -c 'CRITICAL\\|HIGH' readmenator-agent/SECURITY.md`\n"
            "\n",
        )
        self._write(
            recipes_dir / "reduce-complexity.md",
            "# Recipe: Reduce File Complexity\n"
            "\n"
            "1. Read hotspots: `grep -A5 'Hotspots' readmenator-agent/GOTCHAS.md`\n"
            "2. Pick the worst offender\n"
            "3. Extract functions/classes into new files in the same subsystem\n"
            "4. Update imports\n"
            "5. Regenerate: `readmenator .`\n"
            "\n",
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_resolved_map(
        resolved_edges: List[Edge],
    ) -> Dict[Tuple[str, str], str]:
        mapping: Dict[Tuple[str, str], str] = {}
        for e in resolved_edges:
            mapping[(e.source, e.target)] = e.relation
        return mapping

    @staticmethod
    def _build_imported_by_map(
        resolved_edges: List[Edge],
    ) -> Dict[str, List[str]]:
        result: Dict[str, List[str]] = defaultdict(list)
        for e in resolved_edges:
            result[e.target].append(e.source)
        return result

    @staticmethod
    def _write(path: Path, content: str) -> None:
        path.write_text(content, encoding="utf-8")
