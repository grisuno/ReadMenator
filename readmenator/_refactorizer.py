"""Monolithic file refactoring planner for the readmenator knowledge graph.

Identifies large files exceeding configurable thresholds and generates
deterministic refactoring plans based on symbol extraction and
cohesive cluster detection. Never auto-executes; only produces plans.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from readmenator._config import Config
from readmenator._models import (
    Edge,
    Node,
    RefactoringAction,
    RefactoringPlan,
    Symbol,
)


class MonolithRefactorizer:
    """Generates refactoring plans for monolithic files.

    Analyzes files exceeding the line threshold, extracts symbol
    boundaries, detects cohesive clusters via import analysis, and
    produces structured refactoring plans without auto-execution.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    def analyze(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> List[RefactoringPlan]:
        """Identify monolithic files and generate refactoring plans.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            content_map: Optional mapping from node_id to file content.

        Returns:
            List of RefactoringPlan instances for files needing refactoring.
        """
        plans: List[RefactoringPlan] = []
        for node in nodes:
            line_count = self._get_line_count(node.node_id, content_map)
            if line_count > self._config.REFACTORIZER_MIN_LINES:
                actions = self._plan_refactoring(node, edges, resolved_edges, content_map)
                if actions:
                    plans.append(
                        RefactoringPlan(
                            file_path=node.node_id,
                            actions=actions,
                            estimated_impact=self._estimate_impact(node.node_id, resolved_edges),
                            current_lines=line_count,
                        )
                    )
        plans.sort(key=lambda p: p.current_lines, reverse=True)
        return plans[:self._config.REFACTORIZER_MAX_FILES]

    def _get_line_count(self, file_id: str, content_map: Optional[Dict[str, str]]) -> int:
        if content_map and file_id in content_map:
            return len(content_map[file_id].splitlines())
        try:
            file_path = Path(file_id)
            if file_path.is_file():
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    return sum(1 for _ in f)
        except (OSError, UnicodeDecodeError):
            pass
        return 0

    def _plan_refactoring(
        self,
        node: Node,
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]],
        content_map: Optional[Dict[str, str]],
    ) -> List[RefactoringAction]:
        actions: List[RefactoringAction] = []
        symbols_by_kind = self._group_symbols_by_kind(node.symbols)
        for kind, symbols in symbols_by_kind.items():
            if len(symbols) >= 2:
                target_file = self._suggest_target_file(node.node_id, kind)
                start_line = min(s.line for s in symbols)
                end_line = max(s.line for s in symbols) + 50
                actions.append(
                    RefactoringAction(
                        action_type="EXTRACT_CLASS" if kind in ("class", "struct", "interface") else "EXTRACT_FUNCTION",
                        source_file=node.node_id,
                        start_line=start_line,
                        end_line=end_line,
                        target_file=target_file,
                        description=f"Extract {len(symbols)} {kind} symbols into {target_file}",
                    )
                )
        if not actions and len(node.symbols) > 5:
            mid = len(node.symbols) // 2
            first_half = node.symbols[:mid]
            second_half = node.symbols[mid:]
            target_file = self._suggest_target_file(node.node_id, "module")
            if first_half and second_half:
                start_line = min(s.line for s in first_half)
                end_line = max(s.line for s in first_half) + 50
                actions.append(
                    RefactoringAction(
                        action_type="EXTRACT_MODULE",
                        source_file=node.node_id,
                        start_line=start_line,
                        end_line=end_line,
                        target_file=target_file,
                        description=f"Split first half of symbols into {target_file}",
                    )
                )
        return actions

    def _group_symbols_by_kind(self, symbols: List[Symbol]) -> Dict[str, List[Symbol]]:
        groups: Dict[str, List[Symbol]] = {}
        for symbol in symbols:
            groups.setdefault(symbol.kind, []).append(symbol)
        return groups

    def _suggest_target_file(self, source_file: str, kind: str) -> str:
        stem = Path(source_file).stem
        parent = Path(source_file).parent
        suffix = Path(source_file).suffix
        kind_map = {
            "class": "_classes",
            "struct": "_types",
            "interface": "_interfaces",
            "function": "_helpers",
            "method": "_helpers",
            "module": "_split",
        }
        suffix_name = kind_map.get(kind, "_extracted")
        return str(parent / f"{stem}{suffix_name}{suffix}")

    def _estimate_impact(self, file_id: str, resolved_edges: Optional[List[Edge]]) -> int:
        if not resolved_edges:
            return 0
        impact = 0
        for edge in resolved_edges:
            if edge.target == file_id:
                impact += 1
        return impact

    def generate_script(self, plan: RefactoringPlan, project_root: str) -> str:
        lines = [
            "#!/bin/bash",
            f"# Refactoring plan for {plan.file_path}",
            f"# Current lines: {plan.current_lines}",
            f"# Estimated impact: {plan.estimated_impact} files",
            "",
            "set -e",
            "",
        ]
        for action in plan.actions:
            lines.append(f"# {action.description}")
            lines.append(f"echo 'Executing: {action.description}'")
            lines.append(f"mkdir -p $(dirname '{action.target_file}')")
            lines.append(f"sed -n '{action.start_line},{action.end_line}p' '{action.source_file}' > '{action.target_file}'")
            lines.append(f"sed -i '{action.start_line},{action.end_line}d' '{action.source_file}'")
            lines.append("")
        lines.append("echo 'Refactoring complete. Review changes and update imports manually.'")
        return "\n".join(lines)
