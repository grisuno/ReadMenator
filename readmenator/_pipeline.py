from __future__ import annotations

from typing import Dict, List, Optional

from readmenator._agent_injector import AgentInjector
from readmenator._agent_output import AgentOutputGenerator
from readmenator._analyzer import GraphAnalyzer
from readmenator._category import Category, TypedGraph, build_category_from_edges
from readmenator._config import Config
from readmenator._cpg import CodePropertyGraph
from readmenator._diagrams import DocsSitePublisher, InteractiveMapRenderer, SystemMapBuilder, SystemMapValidator, VisNetworkRenderer
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
from readmenator._rank import (
    CompositeRanker,
    RankConfig,
    RankedResult,
)
from readmenator._readme_injector import ReadmeInjector
from readmenator._rule_gen import RuleGenerator
from readmenator._sarif import SarifExporter
from readmenator._scanner import PolyglotScanner
from readmenator._security import SecurityAnalyzer
from readmenator._taint import TaintAnalyzer
from readmenator._uml import UmlGenerator


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
        self._uml: UmlGenerator | None = None
        self._readme_injector: ReadmeInjector | None = None
        self._agent_injector: AgentInjector | None = None
        self._agent_output: AgentOutputGenerator | None = None
        self._diagram_builder: SystemMapBuilder | None = None
        self._diagram_renderer: InteractiveMapRenderer | None = None
        self._diagram_validator: SystemMapValidator | None = None
        self._diagram_publisher: DocsSitePublisher | None = None
        self._vis_renderer: VisNetworkRenderer | None = None
        self._last_category: Category | None = None
        self._last_typed_graph: TypedGraph | None = None

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
            self._sarif = SarifExporter(privacy_mode=self._config.PRIVACY_MODE)
        return self._sarif

    @property
    def cpg(self) -> CodePropertyGraph:
        if self._cpg is None:
            self._cpg = CodePropertyGraph(
                privacy_mode=self._config.PRIVACY_MODE,
                cpg_context=self._config.CPG_CONTEXT,
            )
        return self._cpg

    @property
    def layer_detector(self) -> LayerDetector:
        if self._layer_detector is None:
            self._layer_detector = LayerDetector()
        return self._layer_detector

    @property
    def uml(self) -> UmlGenerator:
        if self._uml is None:
            self._uml = UmlGenerator(self._config)
        return self._uml

    @property
    def readme_injector(self) -> ReadmeInjector:
        if self._readme_injector is None:
            self._readme_injector = ReadmeInjector(
                kb_filename=self._config.OUTPUT_FILENAME,
                agent_output_dir=self._config.AGENT_OUTPUT_DIR,
            )
        return self._readme_injector

    @property
    def agent_injector(self) -> AgentInjector:
        if self._agent_injector is None:
            self._agent_injector = AgentInjector(
                kb_filename=self._config.AGENT_INJECTION_KB_FILENAME,
                agent_output_dir=self._config.AGENT_OUTPUT_DIR,
            )
        return self._agent_injector

    @property
    def agent_output(self) -> AgentOutputGenerator:
        if self._agent_output is None:
            self._agent_output = AgentOutputGenerator(self._config)
        return self._agent_output

    @property
    def diagram_builder(self) -> SystemMapBuilder:
        """Return the lazily initialised system map builder."""
        if self._diagram_builder is None:
            self._diagram_builder = SystemMapBuilder(self._config)
        return self._diagram_builder

    @property
    def diagram_renderer(self) -> InteractiveMapRenderer:
        """Return the lazily initialised interactive map renderer."""
        if self._diagram_renderer is None:
            self._diagram_renderer = InteractiveMapRenderer(self._config)
        return self._diagram_renderer

    @property
    def diagram_validator(self) -> SystemMapValidator:
        """Return the lazily initialised system map validator."""
        if self._diagram_validator is None:
            self._diagram_validator = SystemMapValidator(self._config)
        return self._diagram_validator

    @property
    def diagram_publisher(self) -> DocsSitePublisher:
        """Return the lazily initialised documentation site publisher."""
        if self._diagram_publisher is None:
            self._diagram_publisher = DocsSitePublisher(self._config)
        return self._diagram_publisher

    @property
    def vis_renderer(self) -> VisNetworkRenderer:
        """Return the lazily initialised vis.js network renderer."""
        if self._vis_renderer is None:
            self._vis_renderer = VisNetworkRenderer(self._config)
        return self._vis_renderer

    def build_typed_graph(
        self, nodes: List[Node], edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
    ) -> Category:
        node_ids = {n.node_id for n in nodes}
        cat = build_category_from_edges(edges, resolved_edges, node_ids)
        self._last_category = cat
        self._last_typed_graph = TypedGraph(cat)
        return cat

    def make_ranker(self, typed_graph: TypedGraph) -> CompositeRanker:
        """Create a CompositeRanker for the given typed graph."""
        cfg = RankConfig(
            alpha=self._config.RANKING_ALPHA,
            max_iter=self._config.RANKING_MAX_ITER,
            tolerance=self._config.RANKING_TOLERANCE,
            top_n=self._config.RANKING_TOP_N,
            noise_penalty=self._config.RANKING_NOISE_PENALTY,
            composite_ppr_weight=self._config.RANKING_PPR_WEIGHT,
            composite_authority_weight=self._config.RANKING_AUTHORITY_WEIGHT,
            composite_test_weight=self._config.RANKING_TEST_WEIGHT,
            composite_doc_weight=self._config.RANKING_DOC_WEIGHT,
            composite_freshness_weight=self._config.RANKING_FRESHNESS_WEIGHT,
        )
        return CompositeRanker(typed_graph, config=cfg)

    @property
    def last_category(self) -> Optional[Category]:
        return self._last_category

    @property
    def last_typed_graph(self) -> Optional[TypedGraph]:
        return self._last_typed_graph


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
