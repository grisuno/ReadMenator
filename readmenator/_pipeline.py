from __future__ import annotations

from typing import Dict, List, Optional

from readmenator._analyzer import GraphAnalyzer
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
from readmenator._rule_gen import RuleGenerator
from readmenator._sarif import SarifExporter
from readmenator._scanner import PolyglotScanner
from readmenator._security import SecurityAnalyzer
from readmenator._taint import TaintAnalyzer


class AnalyzerFactory:
    """Lazy factory for all readmenator analyzer and generator instances.

    Decouples the application orchestrator from the concrete
    instantiation of analysis modules. Each component is created
    on first access and cached for the lifetime of the factory.
    """

    def __init__(self, config: Config) -> None:
        self._config = config
        self._scanner: PolyglotScanner | None = None
        self._generator: DocumentationGenerator | None = None
        self._analyzer: GraphAnalyzer | None = None
        self._security: SecurityAnalyzer | None = None
        self._exporter: GraphExporter | None = None
        self._taint: TaintAnalyzer | None = None
        self._hotspots: HotspotAnalyzer | None = None
        self._layer_rules: LayerRuleEngine | None = None
        self._rule_gen: RuleGenerator | None = None
        self._sarif: SarifExporter | None = None
        self._cpg: CodePropertyGraph | None = None
        self._layer_detector: LayerDetector | None = None

    @property
    def scanner(self) -> PolyglotScanner:
        if self._scanner is None:
            self._scanner = PolyglotScanner(self._config)
        return self._scanner

    @property
    def generator(self) -> DocumentationGenerator:
        if self._generator is None:
            self._generator = DocumentationGenerator(self._config)
        return self._generator

    @property
    def analyzer(self) -> GraphAnalyzer:
        if self._analyzer is None:
            self._analyzer = GraphAnalyzer(self._config)
        return self._analyzer

    @property
    def security(self) -> SecurityAnalyzer:
        if self._security is None:
            self._security = SecurityAnalyzer(self._config)
        return self._security

    @property
    def exporter(self) -> GraphExporter:
        if self._exporter is None:
            self._exporter = GraphExporter(self._config)
        return self._exporter

    @property
    def taint(self) -> TaintAnalyzer:
        if self._taint is None:
            self._taint = TaintAnalyzer(self._config)
        return self._taint

    @property
    def hotspots(self) -> HotspotAnalyzer:
        if self._hotspots is None:
            self._hotspots = HotspotAnalyzer(self._config)
        return self._hotspots

    @property
    def layer_rules(self) -> LayerRuleEngine:
        if self._layer_rules is None:
            self._layer_rules = LayerRuleEngine(self._config)
        return self._layer_rules

    @property
    def rule_gen(self) -> RuleGenerator:
        if self._rule_gen is None:
            self._rule_gen = RuleGenerator(self._config)
        return self._rule_gen

    @property
    def sarif(self) -> SarifExporter:
        if self._sarif is None:
            self._sarif = SarifExporter(self._config)
        return self._sarif

    @property
    def cpg(self) -> CodePropertyGraph:
        if self._cpg is None:
            self._cpg = CodePropertyGraph(self._config)
        return self._cpg

    @property
    def layer_detector(self) -> LayerDetector:
        if self._layer_detector is None:
            self._layer_detector = LayerDetector(self._config)
        return self._layer_detector


class DeepAnalysisRunner:
    """Orchestrates the extended V2 analysis pipeline.

    Runs taint propagation, hotspot detection, cycle detection,
    change impact, layer violations, and rule generation as a
    coordinated batch. Isolated from the main app to reduce
    coupling in the primary orchestration layer.
    """

    def __init__(self, factory: AnalyzerFactory) -> None:
        self._factory = factory

    def run(
        self,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        layers: Optional[Dict[str, str]] = None,
        content_map: Optional[Dict[str, str]] = None,
    ) -> AnalysisResultV2:
        config = self._factory._config

        taint_result: Optional[TaintAnalysisResult] = None
        if config.TAINT_ENABLED:
            taint_result = self._factory.taint.analyze(nodes, edges, resolved_edges)

        hotspots = (
            self._factory.hotspots.analyze_hotspots(nodes, edges, resolved_edges)
            if config.HOTSPOTS_ENABLED
            else []
        )

        cycles = (
            self._factory.hotspots.detect_cycles(nodes, resolved_edges)
            if config.CYCLE_DETECTION_ENABLED
            else []
        )

        change_impacts = (
            self._factory.hotspots.analyze_change_impact(nodes, resolved_edges)
            if config.HOTSPOTS_ENABLED
            else []
        )

        layer_violations = (
            self._factory.layer_rules.detect_violations(
                nodes, edges, resolved_edges, layers
            )
            if config.LAYER_VIOLATION_ENABLED
            else []
        )

        suggested_rules = (
            self._factory.rule_gen.generate(nodes, content_map)
            if config.RULE_GEN_ENABLED
            else []
        )

        return AnalysisResultV2(
            taint=taint_result,
            cycles=cycles,
            change_impacts=change_impacts,
            hotspots=hotspots,
            suggested_rules=suggested_rules,
            layer_violations=layer_violations,
        )
