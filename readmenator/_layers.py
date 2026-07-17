"""Architectural layer detection for the readmenator knowledge graph.

Infers architectural layers (presentation, business logic, data access,
infrastructure, testing, configuration) from file paths, naming
conventions, and import patterns. No external API calls.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from readmenator._models import Edge, Node


class LayerDetector:
    """Detects architectural layers in a codebase.

    Assigns each file to a layer based on path patterns, naming
    conventions, and imported frameworks. Returns a mapping that
    can enrich documentation and analysis. No config dependency.
    """

    _LAYER_PATTERNS: Dict[str, List[str]] = {
        "presentation": [
            "view", "template", "component", "page", "screen", "ui",
            "widget", "render", "layout", "frontend", "presentation",
            "controller", "handler", "route", "router", "endpoint", "api",
            "http", "rest", "graphql", "action",
        ],
        "business_logic": [
            "service", "usecase", "use_case", "interactor", "business",
            "logic", "domain", "model", "entity", "aggregate", "value_object",
            "policy", "rule", "strategy", "workflow", "process",
        ],
        "data_access": [
            "repository", "dao", "dal", "data", "database", "persistence",
            "storage", "store", "query", "mapper", "orm", "migration",
            "seed", "fixture",
        ],
        "infrastructure": [
            "config", "settings", "env", "environment", "setup", "bootstrap",
            "middleware", "plugin", "extension", "adapter", "connector",
            "client", "driver", "provider", "factory", "builder",
            "container", "di", "inject", "logger", "logging", "cache",
            "queue", "message", "event", "bus", "scheduler", "cron",
        ],
        "testing": [
            "test", "spec", "mock", "stub", "fixture", "helper_test",
            "test_util", "conftest",
        ],
    }

    _FRAMEWORK_LAYERS: Dict[str, str] = {
        "flask": "presentation",
        "django": "presentation",
        "fastapi": "presentation",
        "express": "presentation",
        "react": "presentation",
        "vue": "presentation",
        "angular": "presentation",
        "spring": "business_logic",
        "hibernate": "data_access",
        "sqlalchemy": "data_access",
        "typeorm": "data_access",
        "prisma": "data_access",
        "pytest": "testing",
        "jest": "testing",
        "unittest": "testing",
    }

    def detect(
        self, nodes: List[Node], edges: List[Edge]
    ) -> Dict[str, str]:
        """Assign each file node to an architectural layer.

        Args:
            nodes: Scanned file nodes.
            edges: Import edges.

        Returns:
            Dict mapping node_id to layer name.
        """
        layers: Dict[str, str] = {}
        for node in nodes:
            layer = self._classify_file(node, edges)
            layers[node.node_id] = layer
        return layers

    def _classify_file(self, node: Node, edges: List[Edge]) -> str:
        """Classify a single file into an architectural layer."""
        path_lower = node.node_id.lower()
        scores: Dict[str, int] = {
            "presentation": 0,
            "business_logic": 0,
            "data_access": 0,
            "infrastructure": 0,
            "testing": 0,
        }

        for layer, patterns in self._LAYER_PATTERNS.items():
            for pattern in patterns:
                if pattern in path_lower:
                    scores[layer] += 1

        imports = {
            e.target.lower() for e in edges if e.source == node.node_id
        }
        for fw, layer in self._FRAMEWORK_LAYERS.items():
            if any(fw in imp for imp in imports):
                scores[layer] += 3

        if node.label.lower().startswith("test") or "_test" in node.label.lower():
            scores["testing"] += 5

        max_layer = max(scores, key=scores.get)
        if scores[max_layer] == 0:
            return "utility"

        return max_layer

    @staticmethod
    def layer_summary(layers: Dict[str, str]) -> Dict[str, int]:
        """Count files per layer.

        Args:
            layers: Mapping from detect().

        Returns:
            Dict of layer_name -> file_count.
        """
        summary: Dict[str, int] = {}
        for layer in layers.values():
            summary[layer] = summary.get(layer, 0) + 1
        return summary
