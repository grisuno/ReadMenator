from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from readmenator._cache import FileCache
from readmenator._config import Config
from readmenator._layers import LayerDetector
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    Node,
    SecurityFinding,
)
from readmenator._pipeline import AnalyzerFactory, DeepAnalysisRunner
from readmenator._query import QueryEngine
from readmenator._rank import RankedResult
from readmenator._resolver import ImportResolver

logger = logging.getLogger(__name__)


class readmenatorApplication:
    def __init__(self, config: Optional[Config] = None):
        self._config = config or Config()
        self._factory = AnalyzerFactory(self._config)
        self._deep_runner = DeepAnalysisRunner(self._factory)
        self._last_nodes: List[Node] = []
        self._last_edges: List[Edge] = []
        self._last_resolved_edges: List[Edge] = []
        self._last_findings: List[SecurityFinding] = []

    def _scan(self, target_dir: str) -> Tuple[List[Node], List[Edge]]:
        root = Path(target_dir).resolve()
        nodes, edges = self._factory.scanner.scan(root)
        self._last_nodes = nodes
        self._last_edges = edges
        self._last_resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        return nodes, edges

    def _scan_with_content(
        self, target_dir: str
    ) -> Tuple[List[Node], List[Edge], Dict[str, str]]:
        root = Path(target_dir).resolve()
        nodes, edges, content_map = self._factory.scanner.scan_with_content(root)
        self._last_nodes = nodes
        self._last_edges = edges
        self._last_resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        return nodes, edges, content_map

    def _resolve_imports(
        self, nodes: List[Node], edges: List[Edge], target_dir: str
    ) -> List[Edge]:
        file_ids = [n.node_id for n in nodes]
        resolver = ImportResolver(file_ids, target_dir)
        resolved: List[Edge] = []
        for edge in edges:
            target = resolver.resolve(edge.target, edge.source)
            if target is not None and target != edge.source:
                resolved.append(
                    Edge(
                        source=edge.source,
                        target=target,
                        relation="resolved_imports",
                        confidence="EXTRACTED",
                    )
                )
        return resolved

    def run(
        self,
        target_dir: str,
        resolve_imports: bool = True,
        run_analysis: bool = True,
        run_security: Optional[bool] = None,
        run_v2_analysis: Optional[bool] = None,
    ) -> None:
        root = Path(target_dir).resolve()
        nodes, edges, content_map = self._factory.scanner.scan_with_content(root)
        self._last_nodes = nodes
        self._last_edges = edges

        resolved_edges: Optional[List[Edge]] = None
        if resolve_imports:
            resolved_edges = self._resolve_imports(nodes, edges, target_dir)
            self._last_resolved_edges = resolved_edges

        analysis: Optional[AnalysisResult] = None
        if run_analysis:
            analysis = self._factory.analyzer.analyze(nodes, edges, resolved_edges)

        if run_security is None:
            run_security = self._config.SECURITY_ENABLED
        findings: List[SecurityFinding] = []
        if run_security:
            findings = self._factory.security.scan(root)
            self._last_findings = findings

        layers = LayerDetector().detect(nodes, edges)
        layer_summary = LayerDetector.layer_summary(layers)

        if run_v2_analysis is None:
            run_v2_analysis = True
        analysis_v2: Optional[AnalysisResultV2] = None
        if run_v2_analysis:
            analysis_v2 = self._deep_runner.run(
                nodes, edges, resolved_edges, layers, content_map
            )

        ranked: Optional[RankedResult] = None
        if self._config.RANKING_ENABLED:
            try:
                cat = self._factory.build_typed_graph(nodes, edges, resolved_edges)
                tg = self._factory.last_typed_graph
                if tg is not None:
                    ranker = self._factory.make_ranker(tg)
                    engine = QueryEngine(
                        nodes, edges, resolved_edges, ranker=ranker,
                    )
                    ranked = engine.ranked_query(
                        "architecture patterns design implementation",
                        top_n=self._config.RANKING_TOP_N,
                    )
            except Exception:
                logger.exception("Ranking failed, continuing without it")

        content = self._factory.generator.generate(
            nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked,
        )
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")

        cache = FileCache(self._config, str(root))
        file_paths: Dict[str, Path] = {n.node_id: root / n.node_id for n in nodes}
        hashes = cache.compute_hashes(file_paths)
        if hashes:
            cache.save(hashes)
        cache.save_analysis("analysis_v2", {
            "god_nodes": [(nid, s) for nid, s in (analysis.god_nodes or [])],
            "communities": [
                {"id": c.community_id, "label": c.label,
                 "file_ids": list(c.file_ids), "cohesion": c.cohesion, "size": c.size}
                for c in (analysis.communities or [])
            ],
            "surprising_connections": list(analysis.surprising_connections or []),
            "suggested_questions": list(analysis.suggested_questions or []),
        })
        cache.save_analysis("layers", dict(layers))
        cache.save_analysis("security", {
            "findings": [
                {"file_path": f.file_path, "line": f.line,
                 "severity": f.severity, "rule_id": f.rule_id,
                 "description": f.description, "snippet": f.snippet, "cwe": f.cwe}
                for f in findings
            ]
        })

        self._write_sidecar_outputs(root, findings, analysis_v2)
        self._log_summary(
            nodes, edges, resolved_edges, analysis, layer_summary, analysis_v2, findings,
        )

    def _write_sidecar_outputs(
        self,
        root: Path,
        findings: List[SecurityFinding],
        analysis_v2: Optional[AnalysisResultV2] = None,
    ) -> None:
        if self._config.SARIF_ENABLED and findings:
            sarif_path = root / self._config.SARIF_OUTPUT
            sarif_content = self._factory.sarif.export(findings, root.name)
            sarif_path.write_text(sarif_content, encoding="utf-8")
            logger.info("SARIF audit written: %s", sarif_path)

        if (
            self._config.RULE_GEN_ENABLED
            and analysis_v2
            and analysis_v2.suggested_rules
        ):
            rules_dir = str(root / self._config.RULE_GEN_OUTPUT_DIR)
            written = self._factory.rule_gen.write_rules(
                analysis_v2.suggested_rules, rules_dir
            )
            if written:
                logger.info(
                    "Suggested rules: %d files in %s", written, rules_dir
                )

    def _log_summary(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        layer_summary: Optional[Dict[str, int]] = None,
        analysis_v2: Optional[AnalysisResultV2] = None,
        findings: Optional[List[SecurityFinding]] = None,
    ) -> None:
        total_symbols = sum(len(n.symbols) for n in nodes)
        import_edges = [e for e in edges if e.relation == "imports"]
        call_edges = [e for e in edges if e.relation == "calls"]
        inherit_edges = [e for e in edges if e.relation == "inherits"]
        logger.info(
            "Files: %d | Symbols: %d | Imports: %d",
            len(nodes), total_symbols, len(import_edges),
        )
        if call_edges:
            logger.info("Call edges: %d", len(call_edges))
        if inherit_edges:
            logger.info("Inheritance edges: %d", len(inherit_edges))
        if resolved_edges:
            logger.info("Resolved imports: %d", len(resolved_edges))
        if analysis and analysis.communities:
            logger.info("Communities detected: %d", len(analysis.communities))
        if layer_summary:
            top_layer = max(layer_summary, key=layer_summary.get)
            logger.info(
                "Layers detected: %d (dominant: %s)",
                len(layer_summary), top_layer,
            )
        if analysis_v2:
            if analysis_v2.taint and analysis_v2.taint.paths:
                logger.info("Taint paths: %d", len(analysis_v2.taint.paths))
            if analysis_v2.hotspots:
                logger.info("Hotspot files: %d", len(analysis_v2.hotspots))
            if analysis_v2.cycles:
                logger.info("Dependency cycles: %d", len(analysis_v2.cycles))
            if analysis_v2.layer_violations:
                logger.info(
                    "Layer violations: %d", len(analysis_v2.layer_violations)
                )
            if analysis_v2.suggested_rules:
                logger.info(
                    "Suggested rules: %d", len(analysis_v2.suggested_rules)
                )
        if findings:
            logger.info(self._factory.security.summary(findings))
        logger.info(
            "Knowledge base generated: %s",
            Path.cwd() / self._config.OUTPUT_FILENAME,
        )

    def update(self, target_dir: str, run_security: Optional[bool] = None) -> None:
        root = Path(target_dir).resolve()
        cache = FileCache(self._config, str(root))
        nodes, edges = self._scan_for_cache(root, cache)
        self._last_nodes = nodes
        self._last_edges = edges
        resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        self._last_resolved_edges = resolved_edges

        cached_analysis = cache.load_analysis("analysis_v2")
        cached_findings = cache.load_analysis("security")

        file_paths: Dict[str, Path] = {n.node_id: root / n.node_id for n in nodes}
        needs_reanalysis = cache.has_changed_since_last_analysis(file_paths)

        if needs_reanalysis or cached_analysis is None:
            analysis = self._factory.analyzer.analyze(nodes, edges, resolved_edges)
            analysis_v2 = self._deep_runner.run(
                nodes, edges, resolved_edges,
                LayerDetector().detect(nodes, edges),
                {n.node_id: "" for n in nodes},
            )
            layers = LayerDetector().detect(nodes, edges)
            cache.save_analysis("analysis_v2", {
                "god_nodes": [(nid, s) for nid, s in (analysis.god_nodes or [])],
                "communities": [
                    {"id": c.community_id, "label": c.label,
                     "file_ids": list(c.file_ids), "cohesion": c.cohesion, "size": c.size}
                    for c in (analysis.communities or [])
                ],
                "surprising_connections": list(analysis.surprising_connections or []),
                "suggested_questions": list(analysis.suggested_questions or []),
            })
            cache.save_analysis("layers", dict(layers))
        else:
            analysis_data = cached_analysis
            from readmenator._models import AnalysisResult, CommunityResult
            communities = [
                CommunityResult(c["id"], c["label"], set(c["file_ids"]), c["cohesion"], c["size"])
                for c in analysis_data.get("communities", [])
            ] if analysis_data.get("communities") else []
            analysis = AnalysisResult(
                god_nodes=[tuple(g) for g in analysis_data.get("god_nodes", [])],
                communities=communities,
                surprising_connections=[tuple(s) for s in analysis_data.get("surprising_connections", [])],
                suggested_questions=list(analysis_data.get("suggested_questions", [])),
                node_count=len(nodes),
                edge_count=len(edges),
            )
            analysis_v2 = None
            layers = cache.load_analysis("layers") or {}

        if run_security is None:
            run_security = self._config.SECURITY_ENABLED
        findings: List[SecurityFinding] = []
        if run_security:
            if cached_findings and not needs_reanalysis:
                from readmenator._models import SecurityFinding
                findings = [
                    SecurityFinding(**f) for f in cached_findings.get("findings", [])
                ]
            else:
                findings = self._factory.security.scan(root)
                cache.save_analysis("security", {
                    "findings": [
                        {"file_path": f.file_path, "line": f.line,
                         "severity": f.severity, "rule_id": f.rule_id,
                         "description": f.description, "snippet": f.snippet,
                         "cwe": f.cwe}
                        for f in findings
                    ]
                })
            self._last_findings = findings

        content = self._factory.generator.generate(
            nodes, edges, resolved_edges, analysis,
            layers=layers, findings=findings, analysis_v2=analysis_v2,
        )
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")
        total_symbols = sum(len(n.symbols) for n in nodes)
        logger.info(
            "Knowledge base updated: %s", output_path,
        )
        logger.info(
            "Files: %d | Symbols: %d | Imports: %d",
            len(nodes), total_symbols, len(edges),
        )

    def _scan_for_cache(
        self, root: Path, cache: FileCache
    ) -> Tuple[List[Node], List[Edge]]:
        cached_hashes = cache.load()
        if not cached_hashes:
            return self._factory.scanner.scan(root)

        nodes, edges = self._factory.scanner.scan(root)
        current_ids = {n.node_id for n in nodes}
        cache.prune_deleted(current_ids)

        file_paths: Dict[str, Path] = {n.node_id: root / n.node_id for n in nodes}
        new_hashes = cache.compute_hashes(file_paths)
        if new_hashes:
            cache.save(new_hashes)

        return nodes, edges

    def query(self, target_dir: str, question: str) -> str:
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        return engine.query(question)

    def explain(self, target_dir: str, symbol_name: str) -> str:
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        result = engine.explain(symbol_name)
        if result is None:
            return (
                f"Symbol '{symbol_name}' not found in the knowledge base. "
                f"Scanned {len(nodes)} files with "
                f"{sum(len(n.symbols) for n in nodes)} total symbols."
            )
        return result

    def find_path(self, target_dir: str, symbol_a: str, symbol_b: str) -> str:
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        result = engine.find_path(symbol_a, symbol_b)
        if result is None:
            return (
                f"Could not find a dependency path between '{symbol_a}' "
                f"and '{symbol_b}'. They may be in disconnected components "
                f"or one of the symbols does not exist."
            )
        path_str = " --imports--> ".join(result)
        return f"Dependency path: {path_str}"

    def summary(self, target_dir: str) -> str:
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        return engine.summary()

    def rank_query(
        self, target_dir: str, query: str, top_n: Optional[int] = None
    ) -> RankedResult:
        """Run a ranked query against the knowledge graph.

        Uses Personalized PageRank seeded from query terms to produce
        a relevance-ranked list of files with score decomposition.

        Args:
            target_dir: Project root directory.
            query: Free-text query.
            top_n: Number of results.

        Returns:
            A RankedResult with scored items.
        """
        nodes, edges, content_map = self._scan_with_content(target_dir)
        resolved_edges = self._last_resolved_edges

        cat = self._factory.build_typed_graph(nodes, edges, resolved_edges)
        typed_graph = self._factory.last_typed_graph
        if typed_graph is None:
            typed_graph = self._factory.build_typed_graph(nodes, edges, resolved_edges)

        ranker = self._factory.make_ranker(typed_graph)
        engine = QueryEngine(
            nodes, edges, resolved_edges, ranker=ranker,
        )
        return engine.ranked_query(query, top_n=top_n)

    def rebuild(self, target_dir: str, run_security: Optional[bool] = None) -> None:
        self.run(target_dir, run_security=run_security)

    def analyze(self, target_dir: str) -> AnalysisResult:
        nodes, edges = self._scan(target_dir)
        return self._factory.analyzer.analyze(nodes, edges, self._last_resolved_edges)

    def export_json(self, target_dir: str, output_path: Optional[str] = None) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._factory.analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._factory.exporter.to_json(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.json")
        Path(output_path).write_text(data, encoding="utf-8")
        logger.info("Graph JSON exported: %s", output_path)
        return data

    def export_html(self, target_dir: str, output_path: Optional[str] = None) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._factory.analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._factory.exporter.to_html(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.html")
        Path(output_path).write_text(data, encoding="utf-8")
        logger.info("Graph HTML exported: %s", output_path)
        return data

    def export_svg(self, target_dir: str, output_path: Optional[str] = None) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._factory.analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._factory.exporter.to_svg(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.svg")
        Path(output_path).write_text(data, encoding="utf-8")
        logger.info("Graph SVG exported: %s", output_path)
        return data

    def export(self, target_dir: str) -> None:
        self.export_json(target_dir)
        self.export_html(target_dir)
        self.export_svg(target_dir)

    def export_graphml(self, target_dir: str, output_path: Optional[str] = None) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._factory.analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._factory.exporter.to_graphml(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.graphml")
        Path(output_path).write_text(data, encoding="utf-8")
        logger.info("GraphML exported: %s", output_path)
        return data

    def export_cypher(self, target_dir: str, output_path: Optional[str] = None) -> str:
        nodes, edges = self._scan(target_dir)
        resolved = self._last_resolved_edges
        analysis = self._factory.analyzer.analyze(nodes, edges, resolved)
        findings = self._last_findings or []
        data = self._factory.exporter.to_cypher(nodes, edges, resolved, analysis, findings)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.cypher")
        Path(output_path).write_text(data, encoding="utf-8")
        logger.info("Cypher exported: %s", output_path)
        return data

    def export_obsidian(self, target_dir: str, output_dir: Optional[str] = None) -> int:
        nodes, edges = self._scan(target_dir)
        analysis = self._factory.analyzer.analyze(nodes, edges, self._last_resolved_edges)
        if output_dir is None:
            root = Path(target_dir).resolve()
            output_dir = str(root / "obsidian")
        written = self._factory.exporter.to_obsidian(nodes, edges, output_dir, analysis)
        logger.info("Obsidian vault: %d notes in %s", written, output_dir)
        return written

    def watch(self, target_dir: str) -> None:
        from readmenator._watcher import DirectoryWatcher
        root = str(Path(target_dir).resolve())

        def on_change() -> None:
            self.run(target_dir, resolve_imports=True, run_analysis=True)

        watcher = DirectoryWatcher(root, self._config, on_change)
        watcher.start()

    def audit(self, target_dir: str) -> List[SecurityFinding]:
        root = Path(target_dir).resolve()
        findings = self._factory.security.scan(root)
        self._last_findings = findings
        logger.info(self._factory.security.summary(findings))
        return findings

    def audit_deep(self, target_dir: str) -> AnalysisResultV2:
        nodes, edges, content_map = self._scan_with_content(target_dir)
        resolved_edges = self._last_resolved_edges
        layers = LayerDetector().detect(nodes, edges)
        result = self._deep_runner.run(nodes, edges, resolved_edges, layers, content_map)
        if result.taint:
            logger.info("Taint paths: %d", len(result.taint.paths))
        if result.cycles:
            logger.info("Dependency cycles: %d", len(result.cycles))
        if result.hotspots:
            logger.info(
                "Top hotspot: %s",
                result.hotspots[0].file_id if result.hotspots else "none",
            )
        if result.layer_violations:
            logger.info("Layer violations: %d", len(result.layer_violations))
        if result.suggested_rules:
            logger.info("Suggested rules: %d", len(result.suggested_rules))
        return result

    def export_sarif(self, target_dir: str, output_path: Optional[str] = None) -> str:
        root = Path(target_dir).resolve()
        findings = self._factory.security.scan(root)
        if output_path is None:
            output_path = str(root / self._config.SARIF_OUTPUT)
        data = self._factory.sarif.export(findings, root.name)
        Path(output_path).write_text(data, encoding="utf-8")
        logger.info("SARIF exported: %s", output_path)
        return data

    def export_rules(self, target_dir: str, output_dir: Optional[str] = None) -> int:
        root = Path(target_dir).resolve()
        nodes, edges, content_map = self._scan_with_content(target_dir)
        if output_dir is None:
            output_dir = str(root / self._config.RULE_GEN_OUTPUT_DIR)
        rules = self._factory.rule_gen.generate(nodes, content_map)
        written = self._factory.rule_gen.write_rules(rules, output_dir)
        logger.info("Rules exported: %d files to %s", written, output_dir)
        return written

    def detect_layers(self, target_dir: str) -> dict:
        nodes, edges = self._scan(target_dir)
        detector = LayerDetector()
        layers = detector.detect(nodes, edges)
        summary = detector.layer_summary(layers)
        logger.info("Layer detection complete:")
        for layer, count in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            logger.info("  %s: %d files", layer, count)
        return layers
