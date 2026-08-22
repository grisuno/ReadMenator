"""Dynamic .cursorrules generator for the readmenator knowledge graph.

Reads architectural analysis results and linter violations to produce
a deterministic .cursorrules file that feeds structural constraints
back into AI coding assistants.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from readmenator._config import Config
from readmenator._layers import LayerDetector
from readmenator._models import AnalysisResult, LinterViolation


class CursorRulesGenerator:
    """Generates a .cursorrules file from architectural analysis.

    Combines base rules, detected layer constraints, and active
    linter violations into a deterministic ruleset for AI assistants.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    def generate(
        self,
        nodes: Any,
        edges: Any,
        analysis: Optional[AnalysisResult] = None,
        layers: Optional[Dict[str, str]] = None,
        violations: Optional[List[LinterViolation]] = None,
        project_root: Optional[str] = None,
    ) -> str:
        """Generate the .cursorrules content string.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.
            analysis: Optional analysis results.
            layers: Optional layer mapping.
            violations: Optional linter violations.
            project_root: Optional project root for file output.

        Returns:
            The generated .cursorrules content as a string.
        """
        rules: List[str] = []
        rules.extend(self._build_base_rules())
        if layers:
            rules.extend(self._extract_layer_constraints(layers))
        if analysis:
            rules.extend(self._extract_analysis_constraints(analysis))
        if violations:
            rules.extend(self._extract_violation_rules(violations))
        content = "\n".join(rules)
        if project_root:
            self._write_file(project_root, content)
        return content

    def _build_base_rules(self) -> List[str]:
        return [
            "# ReadMenator Generated Architecture Rules",
            "# This file is auto-generated. Do not edit manually.",
            "",
            "## General Rules",
            "1. Maintain strict separation of concerns.",
            "2. UI/presentation components must not contain business logic or database queries.",
            "3. Business logic must not depend on presentation or infrastructure details.",
            "4. Data access must be isolated behind repository interfaces.",
            f"5. Keep files under {self._config.LINTER_MAX_LINES} lines. Split larger files into cohesive modules.",
            "6. Never add absolute paths to source code.",
            "7. Never hardcode configuration values. Use the Config class.",
            "8. All new modules must have corresponding test files.",
            "9. Use type annotations on all function signatures.",
            "10. Follow the existing code style and naming conventions.",
        ]

    def _extract_layer_constraints(self, layers: Dict[str, str]) -> List[str]:
        layer_files: Dict[str, List[str]] = {}
        for file_id, layer in layers.items():
            layer_files.setdefault(layer, []).append(file_id)
        lines = ["", "## Detected Architectural Layers"]
        for layer_name, files in sorted(layer_files.items()):
            sample = files[:5]
            suffix = f" (+{len(files) - 5} more)" if len(files) > 5 else ""
            lines.append(f"- **{layer_name}**: {', '.join(sample)}{suffix}")
        return lines

    def _extract_analysis_constraints(self, analysis: AnalysisResult) -> List[str]:
        lines = ["", "## Graph Analysis Constraints"]
        if analysis.god_nodes:
            lines.append("### Central Files (God Nodes)")
            lines.append("Changes to these files require extra review:")
            for nid, score in analysis.god_nodes[:5]:
                lines.append(f"- {nid} (centrality: {score:.1f})")
        if analysis.communities:
            lines.append("")
            lines.append("### Community Boundaries")
            lines.append("Avoid importing across community boundaries unless necessary:")
            for c in analysis.communities[:5]:
                lines.append(f"- Community '{c.label}': {c.size} files (cohesion: {c.cohesion:.2f})")
        return lines

    def _extract_violation_rules(self, violations: List[LinterViolation]) -> List[str]:
        lines = ["", "## Active Violations to Fix"]
        for v in violations[:10]:
            lines.append(f"- [{v.severity.upper()}] {v.rule_id}: {v.message}")
        if len(violations) > 10:
            lines.append(f"- ... and {len(violations) - 10} more violations")
        return lines

    def _write_file(self, project_root: str, content: str) -> None:
        output_path = Path(project_root) / self._config.CURSORRULES_OUTPUT
        output_path.write_text(content, encoding="utf-8")
