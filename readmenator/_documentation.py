from __future__ import annotations

from collections import Counter
from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._cpg import CodePropertyGraph
from readmenator._mermaid import MermaidRenderer
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    HotspotResult,
    LayerViolation,
    Node,
    SecurityFinding,
    SuggestedRule,
    Symbol,
    TaintAnalysisResult,
    pluralize_symbol_kind,
)


class DocumentationGenerator:
    """Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

    Delegates graph rendering to MermaidRenderer and handles the
    Markdown layout: header metadata, Mermaid block, statistics dashboard,
    god nodes, community analysis, surprising connections, architecture
    layers, security audit, taint analysis, hotspots, dependency cycles,
    change impact, architecture violations, suggested rules, CPG block,
    and per-language architecture sections with pluralised symbol kind headings.
    """

    def __init__(self, config: Config) -> None:
        self._config = config
        self._mermaid = MermaidRenderer(config)
        self._cpg = CodePropertyGraph(config)
        self._plural_map: Dict[str, str] = dict(config.SYMBOL_TYPE_PLURALS)

    def generate(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[List[SecurityFinding]] = None,
        analysis_v2: Optional[AnalysisResultV2] = None,
    ) -> str:
        total_symbols = sum(len(n.symbols) for n in nodes)
        import_edges = sum(1 for e in edges if e.relation == "imports")
        graph_output, is_truncated = self._mermaid.render(
            nodes, edges, resolved_edges, analysis
        )

        sections: List[str] = [
            "# Polyglot Codebase Knowledge Graph",
            "",
            "> Generated offline by **readmenator**. "
            "Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, "
            "Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.",
            "> No LLMs. No tokens. Pure static analysis. "
            "See more [here](https://github.com/grisuno/ReadMenator)",
            "",
            f"**Total Files Parsed:** {len(nodes)} | "
            f"**Total Symbols Extracted:** {total_symbols} | "
            f"**Total Imports:** {import_edges}",
        ]

        if resolved_edges:
            sections.append(
                f" | **Resolved Imports:** {len(resolved_edges)}"
            )
        sections.extend(["", ""])

        sections.extend(self._build_toc(nodes, analysis, layers, findings, analysis_v2, is_truncated))
        sections.extend(self._build_dashboard(nodes, edges, resolved_edges))
        sections.extend(self._build_layers(layers, nodes))
        sections.extend(self._build_god_nodes(analysis))
        sections.extend(self._build_community_analysis(analysis, nodes))
        sections.extend(self._build_surprising_connections(analysis, nodes))
        sections.extend(self._build_suggested_questions(analysis))
        sections.extend(self._build_taint_analysis(analysis_v2))
        sections.extend(self._build_hotspots(analysis_v2))
        sections.extend(self._build_dependency_cycles(analysis_v2))
        sections.extend(self._build_change_impact(analysis_v2))
        sections.extend(self._build_layer_violations(analysis_v2))
        sections.extend(self._build_suggested_rules(analysis_v2))
        sections.extend(self._build_security_findings(findings))
        sections.extend(self._build_mermaid_section(graph_output, is_truncated))
        sections.extend(self._build_cpg_block(nodes, edges, resolved_edges, analysis))
        sections.extend(self._build_architecture_reference(nodes, edges))

        return "\n".join(sections)

    def _build_toc(
        self,
        nodes: List[Node],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: Optional[List[SecurityFinding]],
        analysis_v2: Optional[AnalysisResultV2],
        is_truncated: bool,
    ) -> List[str]:
        toc: List[str] = ["## Table of Contents", ""]
        toc.append("1. [Statistics Dashboard](#statistics-dashboard)")
        entry = 2

        toc.append(f"{entry}. [Architectural Layers](#architectural-layers)")
        entry += 1

        if analysis and analysis.god_nodes:
            toc.append(f"{entry}. [God Nodes](#god-nodes)")
            entry += 1
        if analysis and analysis.communities:
            toc.append(f"{entry}. [Community Analysis](#community-analysis)")
            entry += 1
        if analysis and analysis.surprising_connections:
            toc.append(f"{entry}. [Surprising Connections](#surprising-connections)")
            entry += 1
        if analysis and analysis.suggested_questions:
            toc.append(f"{entry}. [Suggested Questions](#suggested-questions)")
            entry += 1

        if analysis_v2 and analysis_v2.taint and analysis_v2.taint.paths:
            toc.append(f"{entry}. [Taint Propagation Map](#taint-propagation-map)")
            entry += 1
        if analysis_v2 and analysis_v2.hotspots:
            toc.append(f"{entry}. [Hotspot Analysis](#hotspot-analysis)")
            entry += 1
        if analysis_v2 and analysis_v2.cycles:
            toc.append(f"{entry}. [Dependency Cycles](#dependency-cycles)")
            entry += 1
        if analysis_v2 and analysis_v2.change_impacts:
            toc.append(f"{entry}. [Change Impact Analysis](#change-impact-analysis)")
            entry += 1
        if analysis_v2 and analysis_v2.layer_violations:
            toc.append(f"{entry}. [Architecture Violations](#architecture-violations)")
            entry += 1
        if analysis_v2 and analysis_v2.suggested_rules:
            toc.append(f"{entry}. [Suggested Linting Rules](#suggested-linting-rules)")
            entry += 1

        if findings:
            toc.append(f"{entry}. [Security Audit](#security-audit)")
            entry += 1

        toc.append(f"{entry}. [Structural Knowledge Map](#structural-knowledge-map)")
        entry += 1
        toc.append(f"{entry}. [Code Property Graph](#code-property-graph)")
        entry += 1
        toc.append(f"{entry}. [Architecture Reference](#architecture-reference)")
        entry += 1

        langs = sorted(set(n.language.upper() for n in nodes))
        for lang in langs:
            lang_nodes = [n for n in nodes if n.language.upper() == lang]
            toc.append(f"    - [{lang} ({len(lang_nodes)} files)](#{lang.lower()}-{len(lang_nodes)}-files)")

        toc.extend(["", "---", ""])
        return toc

    def _build_layers(
        self,
        layers: Optional[Dict[str, str]],
        nodes: List[Node],
    ) -> List[str]:
        if not layers:
            return []
        counts = Counter(layers.values())
        node_map = {n.node_id: n for n in nodes}
        lines: List[str] = [
            "## Architectural Layers",
            "",
            "Auto-detected from path patterns, naming conventions, and imported frameworks.",
            "",
            "| Layer | Files |",
            "|-------|-------|",
        ]
        for layer, count in counts.most_common():
            lines.append(f"| {layer} | {count} |")
        lines.append("")
        for layer in counts:
            file_ids = [nid for nid, l in layers.items() if l == layer]
            lines.append(f"### {layer}")
            lines.append("")
            for nid in sorted(file_ids)[:15]:
                node = node_map.get(nid)
                if node:
                    lines.append(f"- `{node.label}` ({node.language}, {len(node.symbols)} symbols)")
            if len(file_ids) > 15:
                lines.append(f"- *... and {len(file_ids) - 15} more*")
            lines.append("")
        lines.extend(["---", ""])
        return lines

    def _build_dashboard(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> List[str]:
        import_only = [e for e in edges if e.relation == "imports"]
        call_only = [e for e in edges if e.relation == "calls"]
        inherit_only = [e for e in edges if e.relation == "inherits"]
        total_symbols = sum(len(n.symbols) for n in nodes)
        langs = set(n.language for n in nodes)

        lines: List[str] = [
            "## Statistics Dashboard",
            "",
        ]
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        lines.append(f"| Total Files | {len(nodes)} |")
        lines.append(f"| Total Symbols | {total_symbols} |")
        lines.append(f"| Total Imports | {len(import_only)} |")
        lines.append(f"| Call Edges | {len(call_only)} |")
        lines.append(f"| Inheritance Edges | {len(inherit_only)} |")
        lines.append(f"| Languages | {len(langs)} |")
        lines.append(f"| Avg Symbols/File | {total_symbols / max(len(nodes), 1):.1f} |")
        lines.append(f"| Avg Imports/File | {len(import_only) / max(len(nodes), 1):.1f} |")

        if resolved_edges:
            lines.append(f"| Resolved Imports | {len(resolved_edges)} |")
        lines.append("")

        import_counts: Dict[str, int] = {}
        for edge in import_only:
            import_counts[edge.source] = import_counts.get(edge.source, 0) + 1

        node_map = {n.node_id: n for n in nodes}
        fan_out = sorted(
            [(nid, c) for nid, c in import_counts.items() if nid in node_map],
            key=lambda x: x[1],
            reverse=True,
        )[:10]

        if fan_out:
            lines.append("### Top Files by Import Count (Fan-Out)")
            lines.append("")
            lines.append("| File | Imports | Symbols | Language |")
            lines.append("|------|---------|---------|----------|")
            for nid, count in fan_out:
                node = node_map[nid]
                lines.append(
                    f"| `{node.label}` | {count} | "
                    f"{len(node.symbols)} | {node.language} |"
                )
            lines.append("")

        fan_in: Dict[str, int] = {}
        file_ids = {n.node_id for n in nodes}
        for edge in import_only:
            if edge.target in file_ids:
                fan_in[edge.target] = fan_in.get(edge.target, 0) + 1

        fan_in_sorted = sorted(fan_in.items(), key=lambda x: x[1], reverse=True)[:10]
        if fan_in_sorted:
            lines.append("### Top Files by Imported-By Count (Fan-In)")
            lines.append("")
            lines.append("| File | Imported By | Symbols | Language |")
            lines.append("|------|-------------|---------|----------|")
            for nid, count in fan_in_sorted:
                node = node_map.get(nid)
                if node:
                    lines.append(
                        f"| `{node.label}` | {count} | "
                        f"{len(node.symbols)} | {node.language} |"
                    )
            lines.append("")

        lines.append("---")
        lines.append("")
        return lines

    def _build_god_nodes(
        self, analysis: Optional[AnalysisResult]
    ) -> List[str]:
        if not analysis or not analysis.god_nodes:
            return []
        lines: List[str] = [
            "## God Nodes",
            "",
            "Most architecturally central files ranked by combined "
            "import/export degree and symbol richness.",
            "",
            "| File | Score | Connections |",
            "|------|-------|-------------|",
        ]
        for nid, score in analysis.god_nodes[:10]:
            label = nid.split("/")[-1] if "/" in nid else nid
            lines.append(f"| `{label}` | {score:.1f} | |")
        lines.extend(["", "---", ""])
        return lines

    def _build_community_analysis(
        self,
        analysis: Optional[AnalysisResult],
        nodes: List[Node],
    ) -> List[str]:
        if not analysis or not analysis.communities:
            return []
        node_map = {n.node_id: n for n in nodes}
        lines: List[str] = [
            "## Community Analysis",
            "",
            "Files grouped by import-based community detection. "
            "Cohesion measures how tightly connected each community is internally.",
            "",
        ]
        for c in analysis.communities:
            lines.append(f"### {c.label} (Cohesion: {c.cohesion:.2f})")
            lines.append("")
            lines.append(f"**{c.size} files** in this community:")
            lines.append("")
            for fid in sorted(c.file_ids)[:20]:
                node = node_map.get(fid)
                if node:
                    lines.append(
                        f"- `{node.label}` ({node.language}, "
                        f"{len(node.symbols)} symbols)"
                    )
            if len(c.file_ids) > 20:
                lines.append(f"- ... and {len(c.file_ids) - 20} more files")
            lines.append("")
        lines.extend(["---", ""])
        return lines

    def _build_surprising_connections(
        self,
        analysis: Optional[AnalysisResult],
        nodes: List[Node],
    ) -> List[str]:
        if not analysis or not analysis.surprising_connections:
            return []
        lines: List[str] = [
            "## Surprising Connections",
            "",
            "Files in different communities connected through "
            f"{self._config.SURPRISING_CONNECTION_HOP_THRESHOLD}+ indirect hops.",
            "",
        ]
        node_map = {n.node_id: n for n in nodes}
        for src, tgt, hops, comms in analysis.surprising_connections:
            src_label = node_map[src].label if src in node_map else src
            tgt_label = node_map[tgt].label if tgt in node_map else tgt
            lines.append(
                f"- `{src_label}` <-> `{tgt_label}` "
                f"({hops} hops, across {len(comms)} communities)"
            )
        lines.extend(["", "---", ""])
        return lines

    def _build_suggested_questions(
        self, analysis: Optional[AnalysisResult]
    ) -> List[str]:
        if not analysis or not analysis.suggested_questions:
            return []
        lines: List[str] = [
            "## Suggested Questions",
            "",
            "Auto-generated exploration prompts based on graph structure:",
            "",
        ]
        for q in analysis.suggested_questions:
            lines.append(f"- {q}")
        lines.extend(["", "---", ""])
        return lines

    def _build_taint_analysis(
        self, analysis_v2: Optional[AnalysisResultV2]
    ) -> List[str]:
        if not analysis_v2 or not analysis_v2.taint or not analysis_v2.taint.paths:
            return []
        taint: TaintAnalysisResult = analysis_v2.taint
        lines: List[str] = [
            "## Taint Propagation Map",
            "",
            "Taint analysis traces how dangerous imports propagate through the "
            "codebase via transitive dependencies. Source files import dangerous "
            "modules directly; sink files receive the danger indirectly.",
            "",
            f"**Taint Sources:** {taint.source_count} | "
            f"**Taint Sinks:** {taint.sink_count} | "
            f"**Propagation Paths:** {len(taint.paths)}",
            "",
        ]
        for tp in taint.paths[:20]:
            path_str = " -> ".join(
                p.split("/")[-1] for p in tp.path[:5]
            )
            if len(tp.path) > 5:
                path_str += " -> ..."
            lines.append(
                f"- `{tp.source_file.split('/')[-1]}` imports "
                f"`{tp.dangerous_import}` "
                f"({tp.hops} hop{'s' if tp.hops > 1 else ''} to "
                f"`{tp.sink_file.split('/')[-1]}`) "
                f"[{tp.severity}]"
            )
            lines.append(f"  Path: {path_str}")
        lines.extend(["", "---", ""])
        return lines

    def _build_hotspots(
        self, analysis_v2: Optional[AnalysisResultV2]
    ) -> List[str]:
        if not analysis_v2 or not analysis_v2.hotspots:
            return []
        lines: List[str] = [
            "## Hotspot Analysis",
            "",
            "Files ranked by combined complexity (symbol count) and "
            "centrality (connection count). High-scoring files are "
            "architecturally critical and may need refactoring attention.",
            "",
            "| File | Complexity | Centrality | Combined | Symbols | Connections |",
            "|------|-----------|------------|----------|---------|-------------|",
        ]
        for h in analysis_v2.hotspots[:15]:
            lines.append(
                f"| `{h.file_id.split('/')[-1]}` | "
                f"{h.complexity_score:.3f} | "
                f"{h.centrality_score:.3f} | "
                f"{h.combined_score:.3f} | "
                f"{h.symbol_count} | {h.connection_count} |"
            )
        lines.extend(["", "---", ""])
        return lines

    def _build_dependency_cycles(
        self, analysis_v2: Optional[AnalysisResultV2]
    ) -> List[str]:
        if not analysis_v2 or not analysis_v2.cycles:
            return []
        lines: List[str] = [
            "## Dependency Cycles",
            "",
            "Circular dependencies detected in the resolved import graph. "
            "Cycles increase coupling and make refactoring harder.",
            "",
            "| Cycle | Length | Files |",
            "|-------|--------|-------|",
        ]
        for dc in analysis_v2.cycles[:10]:
            files_str = " -> ".join(f.split("/")[-1] for f in dc.cycle)
            lines.append(f"| `{files_str}` | {dc.length} | {len(dc.cycle)} |")
        lines.extend(["", "---", ""])
        return lines

    def _build_change_impact(
        self, analysis_v2: Optional[AnalysisResultV2]
    ) -> List[str]:
        if not analysis_v2 or not analysis_v2.change_impacts:
            return []
        lines: List[str] = [
            "## Change Impact Analysis",
            "",
            "Files sorted by how many other files would be affected if "
            "they changed. High-impact files should be changed with caution.",
            "",
            "| File | Direct Dependents | Transitive Dependents | Total Impact |",
            "|------|------------------|----------------------|--------------|",
        ]
        for ci in analysis_v2.change_impacts[:15]:
            direct_count = len(ci.direct_dependents)
            trans_count = len(ci.transitive_dependents)
            lines.append(
                f"| `{ci.file_id.split('/')[-1]}` | "
                f"{direct_count} | {trans_count} | "
                f"{ci.total_impact} |"
            )
        lines.extend(["", "---", ""])
        return lines

    def _build_layer_violations(
        self, analysis_v2: Optional[AnalysisResultV2]
    ) -> List[str]:
        if not analysis_v2 or not analysis_v2.layer_violations:
            return []
        violations: List[LayerViolation] = analysis_v2.layer_violations
        strict_count = sum(1 for v in violations if v.severity == "strict")
        warn_count = sum(1 for v in violations if v.severity == "warn")
        lines: List[str] = [
            "## Architecture Violations",
            "",
            "Violations of architectural layer rules detected in the import graph. "
            f"**{strict_count} strict violations, {warn_count} warnings.**",
            "",
            "| Source | Source Layer | Target | Target Layer | Description | Severity |",
            "|--------|-------------|--------|-------------|-------------|----------|",
        ]
        for v in violations[:20]:
            src_label = v.source_file.split("/")[-1]
            tgt_label = v.target_file.split("/")[-1]
            lines.append(
                f"| `{src_label}` | {v.source_layer} | "
                f"`{tgt_label}` | {v.target_layer} | "
                f"{v.description} | {v.severity} |"
            )
        lines.extend(["", "---", ""])
        return lines

    def _build_suggested_rules(
        self, analysis_v2: Optional[AnalysisResultV2]
    ) -> List[str]:
        if not analysis_v2 or not analysis_v2.suggested_rules:
            return []
        rules: List[SuggestedRule] = analysis_v2.suggested_rules
        lines: List[str] = [
            "## Suggested Linting Rules",
            "",
            "Automatically suggested linting and security rules based on "
            "patterns detected in the codebase. These can be exported as "
            "Semgrep rules using the `--export-rules` flag.",
            "",
            "| Rule ID | Severity | Description | Language | Matches |",
            "|---------|----------|-------------|----------|---------|",
        ]
        for rule in rules[:15]:
            lines.append(
                f"| `{rule.rule_id}` | {rule.severity} | "
                f"{rule.description} | {rule.language} | "
                f"{rule.match_count} |"
            )
        lines.extend(["", "---", ""])
        return lines

    def _build_security_findings(
        self, findings: Optional[List[SecurityFinding]]
    ) -> List[str]:
        if not findings:
            return []
        by_severity: Dict[str, List[SecurityFinding]] = {}
        for f in findings:
            by_severity.setdefault(f.severity, []).append(f)

        lines: List[str] = [
            "## Security Audit",
            "",
            "Automated pattern-based security analysis. "
            "Findings are grouped by severity (critical -> info).",
            "",
        ]
        sev_order = ["critical", "high", "medium", "low", "info"]
        for sev in sev_order:
            items = by_severity.get(sev)
            if not items:
                continue
            lines.append(f"### {sev.title()} ({len(items)})")
            lines.append("")
            lines.append("| File | Line | Rule | Description | Snippet | CWE |")
            lines.append("|------|------|------|-------------|---------|-----|")
            for f in items:
                snippet = f.snippet.replace("|", "\\|")[:100] if f.snippet else ""
                lines.append(
                    f"| `{f.file_path}` | {f.line} | `{f.rule_id}` | "
                    f"{f.description} | `{snippet}` | {f.cwe} |"
                )
            lines.append("")

        by_lang: Dict[str, List[SecurityFinding]] = {}
        for f in findings:
            ext = f.file_path.rsplit(".", 1)[-1] if "." in f.file_path else "?"
            by_lang.setdefault(ext, []).append(f)

        lines.append("### By Language")
        lines.append("")
        lines.append("| Language | Findings |")
        lines.append("|----------|----------|")
        for lang in sorted(by_lang):
            lines.append(f"| {lang} | {len(by_lang[lang])} |")
        lines.extend(["", "---", ""])
        return lines

    def _build_mermaid_section(
        self, graph_output: str, is_truncated: bool
    ) -> List[str]:
        lines: List[str] = ["## Structural Knowledge Map"]
        if is_truncated:
            lines.extend([
                "",
                "> **Note:** The visual graph below has been intelligently pruned "
                f"to the top {self._config.MERMAID_MAX_NODES} most relevant nodes "
                "to prevent rendering crashes. Full details of all files are "
                "documented in the Architecture Reference.",
            ])
        lines.extend([
            "",
            "```mermaid",
            graph_output,
            "```",
            "",
            "---",
            "",
        ])
        return lines

    def _build_cpg_block(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
    ) -> List[str]:
        if not self._config.CPG_ENABLED:
            return []
        cpg_json = self._cpg.generate(nodes, edges, resolved_edges, analysis)
        lines: List[str] = [
            "## Code Property Graph",
            "",
            "Machine-readable Code Property Graph (CPG) in JSON-LD format. "
            "This block allows AI agents to parse the full structural graph "
            "without additional file reads. Compatible with GraphRAG pipelines.",
            "",
            "```json",
            cpg_json,
            "```",
            "",
            "---",
            "",
        ]
        return lines

    def _build_architecture_reference(
        self,
        nodes: List[Node],
        edges: List[Edge],
    ) -> List[str]:
        lines: List[str] = [
            "## Architecture Reference",
            "",
        ]

        files_by_lang: Dict[str, List[Node]] = {}
        for node in nodes:
            lang = node.language.upper() if node.language else "UNKNOWN"
            if lang not in files_by_lang:
                files_by_lang[lang] = []
            files_by_lang[lang].append(node)

        for lang, lang_nodes in sorted(files_by_lang.items()):
            lines.append(f"### {lang} ({len(lang_nodes)} files)")
            lines.append("")

            for node in lang_nodes:
                anchor = node.node_id.replace("/", "-").replace(" ", "-")
                lines.append(f"#### `{node.label}`")
                lines.append(f"**Path:** `{node.node_id}`")
                if node.doc:
                    lines.append(f"**File Doc:** *{node.doc}*")
                lines.append("")

                incoming = [
                    e for e in edges
                    if e.target == node.node_id and e.source in {n.node_id for n in nodes}
                ]
                if incoming:
                    in_files = sorted(set(e.source.split("/")[-1] for e in incoming[:5]))
                    lines.append(f"**Imported by:** {', '.join(f'`{f}`' for f in in_files)}")
                    lines.append("")

                if node.symbols:
                    symbols_by_type: Dict[str, List[Symbol]] = {}
                    for symbol in node.symbols:
                        if symbol.kind not in symbols_by_type:
                            symbols_by_type[symbol.kind] = []
                        symbols_by_type[symbol.kind].append(symbol)

                    for sym_kind, symbols in sorted(symbols_by_type.items()):
                        plural = pluralize_symbol_kind(sym_kind, self._plural_map)
                        lines.append(f"**{plural.title()}:**")
                        for symbol in symbols:
                            doc_str = f" - *{symbol.doc}*" if symbol.doc else ""
                            sig_str = f" `{symbol.signature}`" if symbol.signature else ""
                            lines.append(
                                f"- `{symbol.name}` (line {symbol.line}){sig_str}{doc_str}"
                            )
                        lines.append("")
                else:
                    lines.append("*No symbols extracted*")
                    lines.append("")

        return lines
