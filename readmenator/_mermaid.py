from __future__ import annotations

import re
from typing import Dict, List, Set, Tuple

from readmenator._config import Config
from readmenator._models import Edge, Node


class MermaidRenderer:
    def __init__(self, config: Config) -> None:
        self._config = config

    def _sanitize_id(self, node_id: str) -> str:
        sanitized = re.sub(r"[^a-zA-Z0-9]", "_", node_id)
        if sanitized and sanitized[0].isdigit():
            sanitized = "n_" + sanitized
        return sanitized

    def render(self, nodes: List[Node], edges: List[Edge]) -> Tuple[str, bool]:
        lines: List[str] = ["graph TD"]
        lines.append(f"    classDef mod {self._config.MERMAID_MODULE_STYLE};")
        lines.append(f"    classDef cls {self._config.MERMAID_CLASS_STYLE};")
        lines.append(f"    classDef fn {self._config.MERMAID_FUNCTION_STYLE};")
        lines.append(f"    classDef ext {self._config.MERMAID_EXTERNAL_STYLE};")

        seen_ids: Set[str] = set()
        node_count = 0
        is_truncated = False
        max_nodes = self._config.MERMAID_MAX_NODES

        import_counts: Dict[str, int] = {node.node_id: 0 for node in nodes}
        for edge in edges:
            if edge.source in import_counts:
                import_counts[edge.source] += 1

        sorted_nodes = sorted(
            nodes,
            key=lambda n: (import_counts.get(n.node_id, 0), len(n.symbols)),
            reverse=True,
        )

        for node in sorted_nodes:
            safe_id = self._sanitize_id(node.node_id)
            if safe_id in seen_ids:
                continue
            label = node.label.replace('"', '\\"')
            lines.append(f'    {safe_id}["{label} ({node.language})"]')
            lines.append(f"    class {safe_id} mod;")
            seen_ids.add(safe_id)
            node_count += 1

            for symbol in node.symbols[:5]:
                if node_count >= max_nodes:
                    is_truncated = True
                    break
                symbol_id = f"{safe_id}_{self._sanitize_id(symbol.name)}"
                symbol_label = symbol.name.replace('"', '\\"')
                lines.append(f'    {symbol_id}["{symbol_label}"]')
                cls_types = {"class", "struct", "interface", "trait", "enum", "record"}
                if symbol.kind in cls_types:
                    lines.append(f"    class {symbol_id} cls;")
                else:
                    lines.append(f"    class {symbol_id} fn;")
                lines.append(f"    {safe_id} --> {symbol_id}")
                node_count += 1

            if node_count >= max_nodes:
                is_truncated = True
                break

        for edge in edges:
            if is_truncated:
                break
            src = self._sanitize_id(edge.source)
            if src not in seen_ids:
                continue
            target_id = self._sanitize_id(f"ext_{edge.target}")
            target_label = edge.target.split("/")[-1].replace('"', '\\"')
            if target_id not in seen_ids:
                if node_count >= max_nodes:
                    is_truncated = True
                    break
                lines.append(f'    {target_id}["{target_label}"]')
                lines.append(f"    class {target_id} ext;")
                seen_ids.add(target_id)
                node_count += 1
            lines.append(f"    {src} -.->|imports| {target_id}")

        return "\n".join(lines), is_truncated
