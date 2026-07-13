"""KNOWLEDGE_BASE.md generator for the readmenator project.

Produces the human-readable Markdown artifact that contains the
structural knowledge map (Mermaid graph), architecture reference
grouped by language, per-file symbol listings with docstrings
and signatures, table of contents, community analysis, god node
summary, statistics dashboard, and cross-references.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._mermaid import MermaidRenderer
from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding, Symbol, pluralize_symbol_kind


class DocumentationGenerator:
    """Builds the KNOWLEDGE_BASE.md document from scanned nodes and edges.

    Delegates graph rendering to MermaidRenderer and handles the
    Markdown layout: header metadata, Mermaid block, and per-language
    architecture sections with pluralised symbol kind headings.
    """

    def __init__(self, config: Config) -> None:
        """Initialise with config and pre-compute the plural map.

        Args:
            config: Application settings including SYMBOL_TYPE_PLURALS.
        """
        self._config = config
        self._mermaid = MermaidRenderer(config)
        self._plural_map: Dict[str, str] = dict(config.SYMBOL_TYPE_PLURALS)

    def generate(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        layers: Optional[Dict[str, str]] = None,
        findings: Optional[List[SecurityFinding]] = None,
    ) -> str:
        """Assemble the full KNOWLEDGE_BASE.md Markdown document.

        Groups files by language, lists symbols per file under
        pluralised kind headings (e.g. "Classes", "Functions"),
        and includes a note when the Mermaid graph was pruned.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional analysis results for communities, god nodes, etc.
            layers: Optional dict mapping node_id to architectural layer.
            findings: Optional security audit findings.

        Returns:
            Complete Markdown string ready to write to disk.
        """
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

        sections.extend(self._build_toc(nodes, analysis, layers, findings, is_truncated))
        sections.extend(self._build_dashboard(nodes, edges, resolved_edges))
        sections.extend(self._build_layers(layers, nodes))
        sections.extend(self._build_god_nodes(analysis))
        sections.extend(self._build_community_analysis(analysis, nodes))
        sections.extend(self._build_surprising_connections(analysis, nodes))
        sections.extend(self._build_suggested_questions(analysis))
        sections.extend(self._build_security_findings(findings))
        sections.extend(self._build_mermaid_section(graph_output, is_truncated))
        sections.extend(self._build_architecture_reference(nodes, edges))

        return "\n".join(sections)

    def _build_toc(
        self,
        nodes: List[Node],
        analysis: Optional[AnalysisResult],
        layers: Optional[Dict[str, str]],
        findings: Optional[List[SecurityFinding]],
        is_truncated: bool,
    ) -> List[str]:
        """Build a table of contents for the document."""
        toc: List[str] = ["## Table of Contents", ""]
        toc.append("1. [Statistics Dashboard](#statistics-dashboard)")

        entry = 2
        if layers:
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

        if findings:
            toc.append(f"{entry}. [Security Audit](#security-audit)")
            entry += 1

        toc.append(f"{entry}. [Structural Knowledge Map](#structural-knowledge-map)")
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
        """Build the architectural layers section."""
        if not layers:
            return []
        from collections import Counter
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
        """Build a statistics dashboard with import metrics and top files."""
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
        """Build the god nodes section."""
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
        """Build the community analysis section."""
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
        """Build the surprising connections section."""
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
        """Build the suggested questions section."""
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

    def _build_security_findings(
        self, findings: Optional[List[SecurityFinding]]
    ) -> List[str]:
        """Build the security audit section."""
        if not findings:
            return []
        by_severity: Dict[str, List[SecurityFinding]] = {}
        for f in findings:
            by_severity.setdefault(f.severity, []).append(f)

        lines: List[str] = [
            "## Security Audit",
            "",
            "Automated pattern-based security analysis. "
            "Findings are grouped by severity (critical → info).",
            "",
        ]
        severity_emoji = {
            "critical": "🔴",
            "high": "🟠",
            "medium": "🟡",
            "low": "🔵",
            "info": "⚪",
        }
        sev_order = ["critical", "high", "medium", "low", "info"]
        for sev in sev_order:
            items = by_severity.get(sev)
            if not items:
                continue
            emoji = severity_emoji.get(sev, "")
            lines.append(f"### {emoji} {sev.title()} ({len(items)})")
            lines.append("")
            lines.append("| File | Line | Rule | Description | Snippet | CWE |")
            lines.append("|------|------|------|-------------|---------|-----|")
            for f in items:
                snippet = f.snippet.replace("|", "\\|")[:100]
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
        """Build the Mermaid graph section."""
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

    def _build_architecture_reference(
        self,
        nodes: List[Node],
        edges: List[Edge],
    ) -> List[str]:
        """Build the architecture reference grouped by language."""
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
