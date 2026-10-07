"""Architectural layer detection for the readmenator knowledge graph.

Infers architectural layers (presentation, business logic, data access,
infrastructure, testing, configuration) from file paths, naming
conventions, and import patterns. No external API calls.
"""

from __future__ import annotations

import re
from collections import defaultdict
from typing import Dict, List, Optional, Set

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

    _EVIDENCE_REQUIRED_LAYERS: Set[str] = {"testing"}

    _PREFIX_MIN_LEN: int = 4

    _CAMEL_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")

    _TOKEN_SPLIT_RE = re.compile(r"[^a-z0-9]+")

    _MODULE_SPLIT_RE = re.compile(r"[./:@\\-]+")

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
        imports_by_file: Dict[str, Set[str]] = defaultdict(set)
        for edge in edges:
            if edge.relation == "imports":
                imports_by_file[edge.source].add(edge.target)
        layers: Dict[str, str] = {}
        for node in nodes:
            layer = self._classify_file(
                node, edges, imports_by_file.get(node.node_id, set()),
            )
            layers[node.node_id] = layer
        return layers

    @classmethod
    def _path_tokens(cls, node_id: str) -> List[str]:
        """Split a path into lowercase word tokens, honoring camelCase."""
        spaced = cls._CAMEL_RE.sub("_", node_id).lower()
        return [t for t in cls._TOKEN_SPLIT_RE.split(spaced) if t]

    @classmethod
    def _pattern_hits(cls, pattern: str, tokens: List[str], joined: str) -> bool:
        """Return whether a layer pattern matches path tokens as a whole word.

        Short patterns (``ui``, ``di``, ``api``) must equal a token;
        longer ones also match token prefixes (``tests``, ``views``).
        Multi-word patterns match underscore-joined token runs.
        """
        if "_" in pattern:
            return f"_{pattern}_" in f"_{joined}_"
        if len(pattern) < cls._PREFIX_MIN_LEN:
            return pattern in tokens
        return any(t == pattern or t.startswith(pattern) for t in tokens)

    @classmethod
    def _import_roots(cls, imports: Set[str]) -> Set[str]:
        """Return the top-level module names of raw import strings."""
        roots: Set[str] = set()
        for imp in imports:
            parts = [p for p in cls._MODULE_SPLIT_RE.split(imp.lower()) if p]
            if parts:
                roots.add(parts[0])
                roots.add(parts[-1])
        return roots

    def _classify_file(
        self,
        node: Node,
        edges: List[Edge],
        imports: Optional[Set[str]] = None,
    ) -> str:
        """Classify a single file into an architectural layer.

        Path words score one point each, framework imports three, and
        test-file naming five. Layers in _EVIDENCE_REQUIRED_LAYERS only
        accept framework points when the path already points there, so a
        CLI that imports ``unittest`` to run the suite stays production code.
        """
        tokens = self._path_tokens(node.node_id)
        joined = "_".join(tokens)
        scores: Dict[str, int] = {
            "presentation": 0,
            "business_logic": 0,
            "data_access": 0,
            "infrastructure": 0,
            "testing": 0,
        }

        for layer, patterns in self._LAYER_PATTERNS.items():
            for pattern in patterns:
                if self._pattern_hits(pattern, tokens, joined):
                    scores[layer] += 1

        if node.label.lower().startswith("test") or "_test" in node.label.lower():
            scores["testing"] += 5

        if imports is None:
            imports = {
                e.target for e in edges
                if e.source == node.node_id and e.relation == "imports"
            }
        roots = self._import_roots(imports)
        for fw, layer in self._FRAMEWORK_LAYERS.items():
            if fw not in roots:
                continue
            if layer in self._EVIDENCE_REQUIRED_LAYERS and scores[layer] == 0:
                continue
            scores[layer] += 3

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
