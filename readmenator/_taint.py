from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional, Set

from readmenator._config import Config
from readmenator._models import Edge, Node, TaintAnalysisResult, TaintPath


class TaintAnalyzer:
    """Propagation-based taint analysis over the resolved import graph.

    Identifies files that import known-dangerous modules or functions
    (sources) and traces how that danger propagates through the import
    graph to files that never directly import the dangerous module
    but receive taint through transitive dependencies.
    """

    DANGEROUS_IMPORTS: Dict[str, str] = {
        "subprocess": "Command injection via subprocess",
        "os.system": "Command injection via os.system",
        "os.popen": "Command injection via os.popen",
        "eval": "Arbitrary code execution via eval",
        "exec": "Arbitrary code execution via exec",
        "compile": "Arbitrary code execution via compile",
        "pickle.loads": "Unsafe deserialization via pickle",
        "pickle.load": "Unsafe deserialization via pickle",
        "yaml.load": "Unsafe deserialization via yaml.load (without Loader)",
        "cPickle.loads": "Unsafe deserialization via cPickle",
        "cPickle.load": "Unsafe deserialization via cPickle",
        "marshal.load": "Unsafe deserialization via marshal",
        "marshal.loads": "Unsafe deserialization via marshal",
        "shelve.open": "Unsafe deserialization via shelve",
        "sqlite3.execute": "SQL injection risk",
        "sqlite3.executemany": "SQL injection risk",
        "os.environ": "Environment variable access (sensitive)",
        "getpass.getpass": "Password prompt (sensitive)",
        "input": "Unsafe input in Python 2 / risk of eval",
        "__import__": "Dynamic import (code injection risk)",
        "requests": "External HTTP request (SSRF risk)",
        "urllib.request": "External HTTP request (SSRF risk)",
        "urlopen": "External HTTP request (SSRF risk)",
    }

    DANGEROUS_IMPORTS_BY_LANGUAGE: Dict[str, Dict[str, str]] = {
        ".py": DANGEROUS_IMPORTS,
        ".js": {
            "eval(": "Arbitrary code execution via eval",
            "Function(": "Arbitrary code construction",
            "child_process.exec": "Command injection",
            "child_process.spawn": "Command injection",
            "execSync": "Command injection",
            "require('child_process')": "Command injection via child_process",
        },
        ".ts": {
            "eval(": "Arbitrary code execution via eval",
            "child_process.exec": "Command injection",
            "child_process.spawn": "Command injection",
        },
    }

    SEVERITIES: Dict[str, str] = {
        "subprocess": "high",
        "os.system": "critical",
        "eval": "critical",
        "exec": "critical",
        "pickle.loads": "high",
        "sqlite3.execute": "medium",
    }

    def __init__(self, config: Config) -> None:
        self._config = config
        self._severity_map: Dict[str, str] = dict(self.SEVERITIES)

    def analyze(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> TaintAnalysisResult:
        """Run taint propagation analysis on the codebase.

        Scans all nodes for direct dangerous imports, then propagates
        taint through the resolved import graph. Returns all discovered
        taint paths from sources to sinks.
        """
        direct_danger: Dict[str, List[str]] = self._find_direct_sources(nodes, edges)
        paths: List[TaintPath] = []
        if not direct_danger:
            return TaintAnalysisResult(paths=[], source_count=0, sink_count=0)

        adj: Dict[str, Set[str]] = self._build_forward_graph(nodes, resolved_edges or [])
        max_depth = self._config.TAINT_MAX_DEPTH
        max_paths = self._config.TAINT_MAX_PATHS

        for source_node_id, danger_imports in direct_danger.items():
            for danger_import in danger_imports:
                severity = self._severity_map.get(
                    danger_import,
                    self._severity_map.get(
                        danger_import.split(".")[0], "medium"
                    ),
                )
                self_path = TaintPath(
                    source_file=source_node_id,
                    sink_file=source_node_id,
                    path=[source_node_id],
                    hops=0,
                    dangerous_import=danger_import,
                    severity=severity,
                )
                paths.append(self_path)
                discovered = self._propagate(
                    source_node_id, danger_import, adj, nodes, max_depth
                )
                paths.extend(discovered)
                if len(paths) >= max_paths:
                    break
            if len(paths) >= max_paths:
                break

        source_set: Set[str] = set()
        sink_set: Set[str] = set()
        for p in paths:
            source_set.add(p.source_file)
            sink_set.add(p.sink_file)

        return TaintAnalysisResult(
            paths=paths[:max_paths],
            source_count=len(source_set),
            sink_count=len(sink_set),
        )

    def _find_direct_sources(
        self, nodes: List[Node], edges: List[Edge]
    ) -> Dict[str, List[str]]:
        """Find files that directly import known-dangerous modules."""
        source_map: Dict[str, List[str]] = {}
        node_ids: Set[str] = {n.node_id for n in nodes}

        all_rules: Dict[str, str] = {}
        for lang_rules in self.DANGEROUS_IMPORTS_BY_LANGUAGE.values():
            all_rules.update(lang_rules)

        for edge in edges:
            if edge.relation != "imports":
                continue
            if edge.source not in node_ids:
                continue
            target_lower = edge.target.lower()
            for dangerous_key, _description in all_rules.items():
                if dangerous_key in target_lower:
                    if edge.source not in source_map:
                        source_map[edge.source] = []
                    source_map[edge.source].append(dangerous_key)
                    break

        return source_map

    def _propagate(
        self,
        source_node_id: str,
        danger_import: str,
        adj: Dict[str, Set[str]],
        nodes: List[Node],
        max_depth: int,
    ) -> List[TaintPath]:
        """BFS propagation from source through the import graph."""
        node_ids: Set[str] = {n.node_id for n in nodes}
        if source_node_id not in adj:
            return []

        paths: List[TaintPath] = []
        visited: Set[str] = {source_node_id}
        queue: deque = deque()
        queue.append((source_node_id, [source_node_id], 0))

        while queue and len(paths) < self._config.TAINT_MAX_PATHS:
            current, path, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for neighbor in adj.get(current, set()):
                if neighbor not in node_ids:
                    continue
                if neighbor in visited and neighbor != source_node_id:
                    continue
                visited.add(neighbor)
                new_path = path + [neighbor]
                severity = self._severity_map.get(
                    danger_import,
                    self._severity_map.get(
                        danger_import.split(".")[0], "medium"
                    ),
                )
                paths.append(
                    TaintPath(
                        source_file=source_node_id,
                        sink_file=neighbor,
                        path=list(new_path),
                        hops=depth + 1,
                        dangerous_import=danger_import,
                        severity=severity,
                    )
                )
                if depth + 1 < max_depth:
                    queue.append((neighbor, new_path, depth + 1))

        return paths

    @staticmethod
    def _build_forward_graph(
        nodes: List[Node], resolved_edges: List[Edge]
    ) -> Dict[str, Set[str]]:
        """Build a forward-directed import graph from resolved edges."""
        adj: Dict[str, Set[str]] = {}
        file_ids: Set[str] = {n.node_id for n in nodes}
        for edge in resolved_edges:
            if edge.source in file_ids and edge.target in file_ids:
                if edge.source not in adj:
                    adj[edge.source] = set()
                adj[edge.source].add(edge.target)
        return adj
