from __future__ import annotations

from typing import Dict, List

from readmenator._config import Config
from readmenator._mermaid import MermaidRenderer
from readmenator._models import Edge, Node, Symbol, pluralize_symbol_kind


class DocumentationGenerator:
    def __init__(self, config: Config) -> None:
        self._config = config
        self._mermaid = MermaidRenderer(config)
        self._plural_map: Dict[str, str] = dict(config.SYMBOL_TYPE_PLURALS)

    def generate(self, nodes: List[Node], edges: List[Edge]) -> str:
        total_symbols = sum(len(n.symbols) for n in nodes)
        graph_output, is_truncated = self._mermaid.render(nodes, edges)

        sections: List[str] = [
            "# Polyglot Codebase Knowledge Graph",
            "",
            "> Generated offline by **readmenator**. "
            "Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, "
            "Dart, GDScript, Nim, ASM.",
            "> No LLMs. No tokens. Pure static analysis. "
            "See more [here](https://github.com/grisuno/ReadMenator)",
            "",
            f"**Total Files Parsed:** {len(nodes)} | "
            f"**Total Symbols Extracted:** {total_symbols} | "
            f"**Total Imports:** {len(edges)}",
            "",
            "## Structural Knowledge Map",
        ]

        if is_truncated:
            sections.append(
                "> **Note:** The visual graph below has been intelligently pruned "
                f"to the top {self._config.MERMAID_MAX_NODES} most relevant nodes "
                "to prevent rendering crashes. Full details of all "
                f"{len(nodes)} files are documented below."
            )
            sections.append("")

        sections.extend(
            [
                "```mermaid",
                graph_output,
                "```",
                "",
                "---",
                "",
                "## Architecture Reference",
                "",
            ]
        )

        files_by_lang: Dict[str, List[Node]] = {}
        for node in nodes:
            lang = node.language.upper() if node.language else "UNKNOWN"
            if lang not in files_by_lang:
                files_by_lang[lang] = []
            files_by_lang[lang].append(node)

        for lang, lang_nodes in sorted(files_by_lang.items()):
            sections.append(f"### {lang} ({len(lang_nodes)} files)")
            sections.append("")

            for node in lang_nodes:
                sections.append(f"#### `{node.label}`")
                sections.append(f"**Path:** `{node.node_id}`")
                sections.append("")

                if node.symbols:
                    symbols_by_type: Dict[str, List[Symbol]] = {}
                    for symbol in node.symbols:
                        if symbol.kind not in symbols_by_type:
                            symbols_by_type[symbol.kind] = []
                        symbols_by_type[symbol.kind].append(symbol)

                    for sym_kind, symbols in sorted(symbols_by_type.items()):
                        plural = pluralize_symbol_kind(sym_kind, self._plural_map)
                        sections.append(f"**{plural.title()}:**")
                        for symbol in symbols:
                            doc_str = f" - *{symbol.doc}*" if symbol.doc else ""
                            sig_str = f" `{symbol.signature}`" if symbol.signature else ""
                            sections.append(
                                f"- `{symbol.name}` (line {symbol.line}){sig_str}{doc_str}"
                            )
                        sections.append("")
                else:
                    sections.append("*No symbols extracted*")
                    sections.append("")

        return "\n".join(sections)
