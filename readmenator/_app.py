from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple

from readmenator._analyzer import GraphAnalyzer
from readmenator._cache import FileCache
from readmenator._config import Config
from readmenator._cpg import CodePropertyGraph
from readmenator._documentation import DocumentationGenerator
from readmenator._exporter import GraphExporter
from readmenator._hotspots import HotspotAnalyzer
from readmenator._layer_rules import LayerRuleEngine
from readmenator._layers import LayerDetector
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    Node,
    SecurityFinding,
    TaintAnalysisResult,
)
from readmenator._query import QueryEngine
from readmenator._resolver import ImportResolver
from readmenator._rule_gen import RuleGenerator
from readmenator._sarif import SarifExporter
from readmenator._scanner import PolyglotScanner
from readmenator._security import SecurityAnalyzer
from readmenator._taint import TaintAnalyzer


class readmenatorApplication:
    """High-level facade for readmenator operations.

    Provides convenience methods for the full pipeline:
      - run / rebuild: scan + generate KNOWLEDGE_BASE.md
      - update: incremental scan using content hash cache
      - query, explain, find_path, summary: scan + query in a single call
      - analyze: run community detection and graph analysis
      - export_json, export_html, export_svg: export the graph
      - audit, audit_deep: security and deep analysis
      - export_sarif, export_rules: SARIF and rule output
    """

    def __init__(self, config: Optional[Config] = None):
        self._config = config or Config()
        self._scanner = PolyglotScanner(self._config)
        self._generator = DocumentationGenerator(self._config)
        self._analyzer = GraphAnalyzer(self._config)
        self._security = SecurityAnalyzer(self._config)
        self._exporter = GraphExporter(self._config)
        self._taint = TaintAnalyzer(self._config)
        self._hotspots = HotspotAnalyzer(self._config)
        self._layer_rules = LayerRuleEngine(self._config)
        self._rule_gen = RuleGenerator(self._config)
        self._sarif = SarifExporter(self._config)
        self._cpg = CodePropertyGraph(self._config)
        self._last_nodes: List[Node] = []
        self._last_edges: List[Edge] = []
        self._last_resolved_edges: List[Edge] = []
        self._last_findings: List[SecurityFinding] = []

    def _scan(self, target_dir: str) -> Tuple[List[Node], List[Edge]]:
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        self._last_nodes = nodes
        self._last_edges = edges
        self._last_resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        return nodes, edges

    def _scan_with_content(
        self, target_dir: str
    ) -> Tuple[List[Node], List[Edge], Dict[str, str]]:
        root = Path(target_dir).resolve()
        nodes, edges, content_map = self._scanner.scan_with_content(root)
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

    def _run_v2_analysis(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> AnalysisResultV2:
        taint_result: Optional[TaintAnalysisResult] = None
        if self._config.TAINT_ENABLED:
            taint_result = self._taint.analyze(nodes, edges, resolved_edges)

        hotspots = self._hotspots.analyze_hotspots(nodes, edges, resolved_edges) if self._config.HOTSPOTS_ENABLED else []

        cycles = self._hotspots.detect_cycles(nodes, resolved_edges) if self._config.CYCLE_DETECTION_ENABLED else []

        change_impacts = self._hotspots.analyze_change_impact(nodes, resolved_edges) if self._config.HOTSPOTS_ENABLED else []

        layer_violations = self._layer_rules.detect_violations(
            nodes, edges, resolved_edges, layers
        ) if self._config.LAYER_VIOLATION_ENABLED else []

        suggested_rules = self._rule_gen.generate(nodes, content_map) if self._config.RULE_GEN_ENABLED else []

        return AnalysisResultV2(
            taint=taint_result,
            cycles=cycles,
            change_impacts=change_impacts,
            hotspots=hotspots,
            suggested_rules=suggested_rules,
            layer_violations=layer_violations,
        )

    def run(
        self,
        target_dir: str,
        resolve_imports: bool = True,
        run_analysis: bool = True,
        run_security: Optional[bool] = None,
        run_v2_analysis: Optional[bool] = None,
    ) -> None:
        root = Path(target_dir).resolve()
        nodes, edges, content_map = self._scanner.scan_with_content(root)
        self._last_nodes = nodes
        self._last_edges = edges

        resolved_edges: Optional[List[Edge]] = None
        if resolve_imports:
            resolved_edges = self._resolve_imports(nodes, edges, target_dir)
            self._last_resolved_edges = resolved_edges

        analysis: Optional[AnalysisResult] = None
        if run_analysis:
            analysis = self._analyzer.analyze(nodes, edges, resolved_edges)

        if run_security is None:
            run_security = self._config.SECURITY_ENABLED
        findings: List[SecurityFinding] = []
        if run_security:
            findings = self._security.scan(root)
            self._last_findings = findings

        layers = LayerDetector(self._config).detect(nodes, edges)
        layer_summary = LayerDetector(self._config).layer_summary(layers)

        if run_v2_analysis is None:
            run_v2_analysis = True
        analysis_v2: Optional[AnalysisResultV2] = None
        if run_v2_analysis:
            analysis_v2 = self._run_v2_analysis(
                nodes, edges, resolved_edges, layers, content_map
            )

        content = self._generator.generate(
            nodes,
            edges,
            resolved_edges,
            analysis,
            layers,
            findings,
            analysis_v2,
        )
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")

        if self._config.SARIF_ENABLED and findings:
            sarif_path = root / self._config.SARIF_OUTPUT
            sarif_content = self._sarif.export(findings, root.name)
            sarif_path.write_text(sarif_content, encoding="utf-8")
            print(f"[+] SARIF audit: {sarif_path}")

        if self._config.RULE_GEN_ENABLED and analysis_v2 and analysis_v2.suggested_rules:
            rules_dir = str(root / self._config.RULE_GEN_OUTPUT_DIR)
            written = self._rule_gen.write_rules(analysis_v2.suggested_rules, rules_dir)
            if written:
                print(f"[+] Suggested rules: {written} files in {rules_dir}")

        total_symbols = sum(len(n.symbols) for n in nodes)
        import_edges = [e for e in edges if e.relation == "imports"]
        call_edges = [e for e in edges if e.relation == "calls"]
        inherit_edges = [e for e in edges if e.relation == "inherits"]
        print(f"[+] Knowledge base generated: {output_path}")
        print(
            f"[+] Files: {len(nodes)} | "
            f"Symbols: {total_symbols} | "
            f"Imports: {len(import_edges)}"
        )
        if call_edges:
            print(f"[+] Call edges: {len(call_edges)}")
        if inherit_edges:
            print(f"[+] Inheritance edges: {len(inherit_edges)}")
        if resolved_edges:
            print(f"[+] Resolved imports: {len(resolved_edges)}")
        if analysis and analysis.communities:
            print(f"[+] Communities detected: {len(analysis.communities)}")
        if layer_summary:
            top_layer = max(layer_summary, key=layer_summary.get)
            print(f"[+] Layers detected: {len(layer_summary)} (dominant: {top_layer})")
        if analysis_v2:
            if analysis_v2.taint and analysis_v2.taint.paths:
                print(f"[+] Taint paths: {len(analysis_v2.taint.paths)}")
            if analysis_v2.hotspots:
                print(f"[+] Hotspot files: {len(analysis_v2.hotspots)}")
            if analysis_v2.cycles:
                print(f"[+] Dependency cycles: {len(analysis_v2.cycles)}")
            if analysis_v2.layer_violations:
                print(f"[+] Layer violations: {len(analysis_v2.layer_violations)}")
            if analysis_v2.suggested_rules:
                print(f"[+] Suggested rules: {len(analysis_v2.suggested_rules)}")
        if findings:
            print(self._security.summary(findings))

    def update(self, target_dir: str, run_security: Optional[bool] = None) -> None:
        root = Path(target_dir).resolve()
        cache = FileCache(self._config, str(root))
        nodes, edges = self._scan_for_cache(root, cache)
        self._last_nodes = nodes
        self._last_edges = edges
        resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        self._last_resolved_edges = resolved_edges
        analysis = self._analyzer.analyze(nodes, edges, resolved_edges)

        if run_security is None:
            run_security = self._config.SECURITY_ENABLED
        findings: List[SecurityFinding] = []
        if run_security:
            findings = self._security.scan(root)
            self._last_findings = findings

        content = self._generator.generate(
            nodes, edges, resolved_edges, analysis, findings=findings
        )
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")
        total_symbols = sum(len(n.symbols) for n in nodes)
        print(f"[+] Knowledge base updated: {output_path}")
        print(
            f"[+] Files: {len(nodes)} | "
            f"Symbols: {total_symbols} | "
            f"Imports: {len(edges)}"
        )

    def _scan_for_cache(
        self, root: Path, cache: FileCache
    ) -> Tuple[List[Node], List[Edge]]:
        cached_hashes = cache.load()
        if not cached_hashes:
            return self._scanner.scan(root)

        nodes, edges = self._scanner.scan(root)
        current_ids = {n.node_id for n in nodes}
        cache.prune_deleted(current_ids)

        file_paths: Dict[str, Path] = {
            n.node_id: root / n.node_id for n in nodes
        }
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

    def rebuild(self, target_dir: str, run_security: Optional[bool] = None) -> None:
        self.run(target_dir, run_security=run_security)

    def analyze(self, target_dir: str) -> AnalysisResult:
        nodes, edges = self._scan(target_dir)
        return self._analyzer.analyze(nodes, edges, self._last_resolved_edges)

    def export_json(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_json(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.json")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] Graph JSON exported: {output_path}")
        return data

    def export_html(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_html(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.html")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] Graph HTML exported: {output_path}")
        return data

    def export_svg(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_svg(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.svg")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] Graph SVG exported: {output_path}")
        return data

    def export(self, target_dir: str) -> None:
        self.export_json(target_dir)
        self.export_html(target_dir)
        self.export_svg(target_dir)

    def export_graphml(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_graphml(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.graphml")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] GraphML exported: {output_path}")
        return data

    def export_obsidian(
        self,
        target_dir: str,
        output_dir: Optional[str] = None,
    ) -> int:
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        if output_dir is None:
            root = Path(target_dir).resolve()
            output_dir = str(root / "obsidian")
        written = self._exporter.to_obsidian(nodes, edges, output_dir, analysis)
        print(f"[+] Obsidian vault: {written} notes in {output_dir}")
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
        findings = self._security.scan(root)
        self._last_findings = findings
        print(self._security.summary(findings))
        return findings

    def audit_deep(self, target_dir: str) -> AnalysisResultV2:
        """Run deep analysis including taint, hotspots, cycles, and rules."""
        nodes, edges, content_map = self._scan_with_content(target_dir)
        resolved_edges = self._last_resolved_edges
        layers = LayerDetector(self._config).detect(nodes, edges)
        result = self._run_v2_analysis(
            nodes, edges, resolved_edges, layers, content_map
        )
        if result.taint:
            print(f"[+] Taint paths: {len(result.taint.paths)}")
        if result.cycles:
            print(f"[+] Dependency cycles: {len(result.cycles)}")
        if result.hotspots:
            print(f"[+] Top hotspots: {result.hotspots[0].file_id if result.hotspots else 'none'}")
        if result.layer_violations:
            print(f"[+] Layer violations: {len(result.layer_violations)}")
        if result.suggested_rules:
            print(f"[+] Suggested rules: {len(result.suggested_rules)}")
        return result

    def export_sarif(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        root = Path(target_dir).resolve()
        findings = self._security.scan(root)
        if output_path is None:
            output_path = str(root / self._config.SARIF_OUTPUT)
        data = self._sarif.export(findings, root.name)
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] SARIF exported: {output_path}")
        return data

    def export_rules(
        self,
        target_dir: str,
        output_dir: Optional[str] = None,
    ) -> int:
        root = Path(target_dir).resolve()
        content_map: Dict[str, str] = {}
        nodes, edges, content_map = self._scan_with_content(target_dir)
        if output_dir is None:
            output_dir = str(root / self._config.RULE_GEN_OUTPUT_DIR)
        rules = self._rule_gen.generate(nodes, content_map)
        written = self._rule_gen.write_rules(rules, output_dir)
        print(f"[+] Rules exported: {written} files to {output_dir}")
        return written

    def detect_layers(self, target_dir: str) -> dict:
        nodes, edges = self._scan(target_dir)
        detector = LayerDetector(self._config)
        layers = detector.detect(nodes, edges)
        summary = detector.layer_summary(layers)
        print("[+] Layer detection complete:")
        for layer, count in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"    {layer}: {count} files")
        return layers
