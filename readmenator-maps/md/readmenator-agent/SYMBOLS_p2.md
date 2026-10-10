# Symbols (page 2 of 5)
Previous: [SYMBOLS.md](SYMBOLS.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_kind_counts` | method | `readmenator/_graphrag.py:578` | `def _kind_counts(entities)` |
| `_location` | method | `readmenator/_graphrag.py:1151` | `def _location(entity)` |
| `_pack` | method | `readmenator/_graphrag.py:1175` | `def _pack(self, header, sections, budget_tokens, shares)` |
| `_rating` | method | `readmenator/_graphrag.py:851` | `def _rating(self, mass, top_mass, risk)` |
| `_relation_weight` | method | `readmenator/_graphrag.py:335` | `def _relation_weight(relation)` |
| `_report_block` | method | `readmenator/_graphrag.py:1163` | `def _report_block(report)` |
| `_reports` | method | `readmenator/_graphrag.py:659` | `def _reports(self, nodes, resolved_edges, analysis, layers, findings, analysis_v2, file_rank, entities)` |
| `_risk_score` | method | `readmenator/_graphrag.py:649` | `def _risk_score(self, files, findings)` |
| `_root_report` | method | `readmenator/_graphrag.py:908` | `def _root_report(self, reports, themes, nodes, analysis)` |
| `_section` | method | `readmenator/_graphrag.py:1158` | `def _section(title, items)` |
| `_short` | method | `readmenator/_graphrag.py:340` | `def _short(file_id)` |
| `_text_units` | method | `readmenator/_graphrag.py:615` | `def _text_units(self, nodes, content_map)` |
| `_themes` | method | `readmenator/_graphrag.py:864` | `def _themes(self, reports, links)` |
| `_tok` | method | `readmenator/_graphrag.py:970` | `def _tok(self, text)` |
| `_undirected_graph` | method | `readmenator/_graphrag.py:585` | `def _undirected_graph(self, ids, relations)` |
| `_unit_block` | method | `readmenator/_graphrag.py:1170` | `def _unit_block(unit)` |
| `_walk_graph` | method | `readmenator/_graphrag.py:979` | `def _walk_graph(self)` |
| `add_relation` | method | `readmenator/_graphrag.py:406` | `def add_relation(source, target, relation, description, confidence)` |
| `build` | method | `readmenator/_graphrag.py:358` | `def build(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, concept_graph, content_map...` |
| `choose_mode` | method | `readmenator/_graphrag.py:987` | `def choose_mode(self, query)` |
| `directory` | method | `readmenator/_graphrag.py:1223` | `def directory(self, project_root)` |
| `from_dict` | method | `readmenator/_graphrag.py:197` | `def from_dict(cls, data)` |
| `global_search` | method | `readmenator/_graphrag.py:1106` | `def global_search(self, query, budget_tokens)` |
| `load` | method | `readmenator/_graphrag.py:1257` | `def load(self, project_root)` |
| `local_search` | method | `readmenator/_graphrag.py:1025` | `def local_search(self, query, budget_tokens)` |
| `render_reports` | method | `readmenator/_graphrag.py:1279` | `def render_reports(index)` |
| `resolve_symbol` | method | `readmenator/_graphrag.py:452` | `def resolve_symbol(file_id, name)` |
| `scores` | method | `readmenator/_graphrag.py:298` | `def scores(self, query)` |
| `search` | method | `readmenator/_graphrag.py:1004` | `def search(self, query, mode, budget_tokens)` |
| `to_dict` | method | `readmenator/_graphrag.py:186` | `def to_dict(self)` |
| `tokenize` | method | `readmenator/_graphrag.py:240` | `def tokenize(text, min_len, stopwords)` |
| `write` | method | `readmenator/_graphrag.py:1227` | `def write(self, index, project_root)` |
| `HotspotAnalyzer` | class | `readmenator/_hotspots.py:22` | `class HotspotAnalyzer` |
| `__init__` | method | `readmenator/_hotspots.py:31` | `def __init__(self, config)` |
| `_dfs_visit` | method | `readmenator/_hotspots.py:114` | `def _dfs_visit(current)` |
| `_record_cycle` | method | `readmenator/_hotspots.py:125` | `def _record_cycle(start, end)` |
| `analyze_change_impact` | method | `readmenator/_hotspots.py:155` | `def analyze_change_impact(self, nodes, resolved_edges)` |
| `analyze_hotspots` | method | `readmenator/_hotspots.py:34` | `def analyze_hotspots(self, nodes, edges, resolved_edges)` |
| `detect_cycles` | method | `readmenator/_hotspots.py:90` | `def detect_cycles(self, nodes, resolved_edges)` |
| `LayerRuleEngine` | class | `readmenator/_layer_rules.py:11` | `class LayerRuleEngine` |
| `__init__` | method | `readmenator/_layer_rules.py:36` | `def __init__(self, config)` |
| `detect_violations` | method | `readmenator/_layer_rules.py:39` | `def detect_violations(self, nodes, edges, resolved_edges, layers)` |
| `violation_summary` | method | `readmenator/_layer_rules.py:111` | `def violation_summary(violations)` |
| `LayerDetector` | class | `readmenator/_layers.py:17` | `class LayerDetector` |
| `_classify_file` | method | `readmenator/_layers.py:138` | `def _classify_file(self, node, edges, imports)` |
| `_import_roots` | method | `readmenator/_layers.py:128` | `def _import_roots(cls, imports)` |
| `_path_tokens` | method | `readmenator/_layers.py:108` | `def _path_tokens(cls, node_id)` |
| `_pattern_hits` | method | `readmenator/_layers.py:114` | `def _pattern_hits(cls, pattern, tokens, joined)` |
| `detect` | method | `readmenator/_layers.py:83` | `def detect(self, nodes, edges)` |
| `layer_summary` | method | `readmenator/_layers.py:189` | `def layer_summary(layers)` |
| `ArchitectureLinter` | class | `readmenator/_linter.py:18` | `class ArchitectureLinter` |
| `__init__` | method | `readmenator/_linter.py:31` | `def __init__(self, config)` |
| `_check_circular_dependencies` | method | `readmenator/_linter.py:127` | `def _check_circular_dependencies(self, nodes, resolved_edges)` |
| `_check_cross_layer_violations` | method | `readmenator/_linter.py:96` | `def _check_cross_layer_violations(self, nodes, edges, resolved_edges, layers)` |
| `_check_file_length` | method | `readmenator/_linter.py:65` | `def _check_file_length(self, nodes, content_map)` |
| `_dfs` | method | `readmenator/_linter.py:146` | `def _dfs(current)` |
| `lint` | method | `readmenator/_linter.py:34` | `def lint(self, nodes, edges, resolved_edges, layers, content_map)` |
| `MCPError` | class | `readmenator/_mcp_server.py:58` | `class MCPError(Exception)` |
| `MCPRequest` | class | `readmenator/_mcp_server.py:71` | `class MCPRequest` |
| `MCPResource` | class | `readmenator/_mcp_server.py:119` | `class MCPResource` |
| `MCPServer` | class | `readmenator/_mcp_server.py:146` | `class MCPServer` |
| `MCPTool` | class | `readmenator/_mcp_server.py:92` | `class MCPTool` |
| `__init__` | method | `readmenator/_mcp_server.py:59` | `def __init__(self, code, message, data)` |
| `__init__` | method | `readmenator/_mcp_server.py:72` | `def __init__(self, msg)` |
| `__init__` | method | `readmenator/_mcp_server.py:93` | `def __init__(self, name, description, handler, input_schema)` |
| `__init__` | method | `readmenator/_mcp_server.py:120` | `def __init__(self, uri, name, description, mime_type, handler)` |
| `__init__` | method | `readmenator/_mcp_server.py:147` | `def __init__(self, app, target_dir)` |
| `_ensure_kb` | method | `readmenator/_mcp_server.py:161` | `def _ensure_kb(self)` |
| `_get_query_engine` | method | `readmenator/_mcp_server.py:1069` | `def _get_query_engine(self, nodes, edges, resolved)` |
| `_handle_call_tool` | method | `readmenator/_mcp_server.py:192` | `def _handle_call_tool(self, req)` |
| `_handle_initialize` | method | `readmenator/_mcp_server.py:173` | `def _handle_initialize(self, req)` |
| `_handle_list_resources` | method | `readmenator/_mcp_server.py:214` | `def _handle_list_resources(self, req)` |
| `_handle_list_tools` | method | `readmenator/_mcp_server.py:187` | `def _handle_list_tools(self, req)` |
| `_handle_read_resource` | method | `readmenator/_mcp_server.py:219` | `def _handle_read_resource(self, req)` |
| `_register_all` | method | `readmenator/_mcp_server.py:285` | `def _register_all(self)` |
| `_resource_analysis` | method | `readmenator/_mcp_server.py:988` | `def _resource_analysis(self)` |
| `_resource_analytics` | method | `readmenator/_mcp_server.py:1063` | `def _resource_analytics(self)` |
| `_resource_concepts` | method | `readmenator/_mcp_server.py:1022` | `def _resource_concepts(self)` |
| `_resource_findings` | method | `readmenator/_mcp_server.py:972` | `def _resource_findings(self)` |
| `_resource_forcegraph` | method | `readmenator/_mcp_server.py:1049` | `def _resource_forcegraph(self)` |
| `_resource_graph` | method | `readmenator/_mcp_server.py:953` | `def _resource_graph(self)` |
| `_resource_graphrag` | method | `readmenator/_mcp_server.py:1055` | `def _resource_graphrag(self)` |
| `_resource_kb` | method | `readmenator/_mcp_server.py:1018` | `def _resource_kb(self)` |
| `_resource_summary` | method | `readmenator/_mcp_server.py:936` | `def _resource_summary(self)` |
| `_scan` | method | `readmenator/_mcp_server.py:590` | `def _scan(self)` |
| `_scan_deep` | method | `readmenator/_mcp_server.py:596` | `def _scan_deep(self)` |
| `_tool_analytics` | method | `readmenator/_mcp_server.py:850` | `def _tool_analytics(self)` |
| `_tool_communities` | method | `readmenator/_mcp_server.py:753` | `def _tool_communities(self)` |
| `_tool_concepts` | method | `readmenator/_mcp_server.py:824` | `def _tool_concepts(self)` |
| `_tool_cycles` | method | `readmenator/_mcp_server.py:742` | `def _tool_cycles(self)` |
| `_tool_explain` | method | `readmenator/_mcp_server.py:647` | `def _tool_explain(self, name)` |
| `_tool_export_json` | method | `readmenator/_mcp_server.py:820` | `def _tool_export_json(self)` |
| `_tool_findings` | method | `readmenator/_mcp_server.py:670` | `def _tool_findings(self, min_severity)` |
| `_tool_forcegraph` | method | `readmenator/_mcp_server.py:900` | `def _tool_forcegraph(self)` |
| `_tool_graphrag` | method | `readmenator/_mcp_server.py:925` | `def _tool_graphrag(self, query, mode, budget_tokens)` |
| `_tool_hotspots` | method | `readmenator/_mcp_server.py:726` | `def _tool_hotspots(self, top_n)` |
| `_tool_layer_violations` | method | `readmenator/_mcp_server.py:786` | `def _tool_layer_violations(self)` |
| `_tool_layers` | method | `readmenator/_mcp_server.py:768` | `def _tool_layers(self)` |
| `_tool_memory` | method | `readmenator/_mcp_server.py:914` | `def _tool_memory(self)` |
| `_tool_near` | method | `readmenator/_mcp_server.py:870` | `def _tool_near(self, query, top_k)` |
| `_tool_path` | method | `readmenator/_mcp_server.py:659` | `def _tool_path(self, symbol_a, symbol_b)` |
| `_tool_provenance` | method | `readmenator/_mcp_server.py:887` | `def _tool_provenance(self)` |
| `_tool_query` | method | `readmenator/_mcp_server.py:642` | `def _tool_query(self, text)` |
| `_tool_rebuild` | method | `readmenator/_mcp_server.py:802` | `def _tool_rebuild(self)` |
| `_tool_remember` | method | `readmenator/_mcp_server.py:918` | `def _tool_remember(self, note, kind)` |
| `_tool_security_summary` | method | `readmenator/_mcp_server.py:700` | `def _tool_security_summary(self)` |
| `_tool_summary` | method | `readmenator/_mcp_server.py:604` | `def _tool_summary(self)` |
| `_tool_taint` | method | `readmenator/_mcp_server.py:705` | `def _tool_taint(self)` |
| `_tool_update` | method | `readmenator/_mcp_server.py:812` | `def _tool_update(self)` |
| `call` | method | `readmenator/_mcp_server.py:115` | `def call(self, arguments)` |
| `definition` | method | `readmenator/_mcp_server.py:108` | `def definition(self)` |
| `definition` | method | `readmenator/_mcp_server.py:134` | `def definition(self)` |
| `dispatch` | method | `readmenator/_mcp_server.py:241` | `def dispatch(self, req)` |
| `error` | method | `readmenator/_mcp_server.py:85` | `def error(self, code, message, data)` |
| `is_notification` | method | `readmenator/_mcp_server.py:79` | `def is_notification(self)` |
| `main` | method | `readmenator/_mcp_server.py:1074` | `def main()` |
| `read` | method | `readmenator/_mcp_server.py:142` | `def read(self)` |
| `register_resource` | method | `readmenator/_mcp_server.py:158` | `def register_resource(self, resource)` |
| `register_tool` | method | `readmenator/_mcp_server.py:155` | `def register_tool(self, tool)` |
| `response` | method | `readmenator/_mcp_server.py:82` | `def response(self, result)` |
| `run` | method | `readmenator/_mcp_server.py:261` | `def run(self)` |
| `DeclaredRule` | class | `readmenator/_memory.py:53` | `class DeclaredRule` |
| `MemoryNote` | class | `readmenator/_memory.py:70` | `class MemoryNote` |
| `ProjectMemory` | class | `readmenator/_memory.py:102` | `class ProjectMemory` |
| `__init__` | method | `readmenator/_memory.py:105` | `def __init__(self, config)` |
| `_categorise` | method | `readmenator/_memory.py:360` | `def _categorise(heading, keywords)` |
| `_count_severe` | method | `readmenator/_memory.py:606` | `def _count_severe(findings)` |
| `_declared_section` | method | `readmenator/_memory.py:512` | `def _declared_section(title, rules, category, measured)` |
| `_deliverable_baselines` | method | `readmenator/_memory.py:559` | `def _deliverable_baselines(self, root, nodes, findings, analysis_v2)` |
| `_is_test` | method | `readmenator/_memory.py:483` | `def _is_test(file_id)` |
| `_log_section` | method | `readmenator/_memory.py:190` | `def _log_section(self, block)` |
| `_notes_block` | method | `readmenator/_memory.py:141` | `def _notes_block(text)` |
| `_pct` | method | `readmenator/_memory.py:601` | `def _pct(part, whole)` |
| `_purpose_section` | method | `readmenator/_memory.py:368` | `def _purpose_section(self, root, nodes, analysis, concept_graph)` |
| `_readme_lead` | method | `readmenator/_memory.py:400` | `def _readme_lead(self, root)` |
| `_risk_section` | method | `readmenator/_memory.py:579` | `def _risk_section(self, analysis, analysis_v2)` |
| `_safe_read` | method | `readmenator/_memory.py:473` | `def _safe_read(self, path)` |
| `_skeleton` | method | `readmenator/_memory.py:182` | `def _skeleton(self)` |
| `_splice` | method | `readmenator/_memory.py:201` | `def _splice(self, document, block)` |
| `_style_baselines` | method | `readmenator/_memory.py:524` | `def _style_baselines(self, nodes, content_map)` |
| `_workflow_section` | method | `readmenator/_memory.py:492` | `def _workflow_section(self, root, nodes)` |
| `_write` | method | `readmenator/_memory.py:209` | `def _write(self, project_root, text)` |
| `build` | method | `readmenator/_memory.py:231` | `def build(self, project_root, nodes, analysis, analysis_v2, findings, concept_graph, content_map)` |
| `detect_commands` | method | `readmenator/_memory.py:419` | `def detect_commands(self, root, nodes)` |
| `extract_rules` | method | `readmenator/_memory.py:291` | `def extract_rules(self, project_root)` |
| `notes` | method | `readmenator/_memory.py:124` | `def notes(self, project_root)` |
| `path` | method | `readmenator/_memory.py:113` | `def path(self, project_root)` |
| `read` | method | `readmenator/_memory.py:117` | `def read(self, project_root)` |
| `remember` | method | `readmenator/_memory.py:149` | `def remember(self, project_root, note, kind, today)` |
| `sanitize_note` | method | `readmenator/_memory.py:84` | `def sanitize_note(text, max_chars)` |
| `write` | method | `readmenator/_memory.py:218` | `def write(self, project_root, generated)` |
| `MermaidRenderer` | class | `readmenator/_mermaid.py:17` | `class MermaidRenderer` |
| `__init__` | method | `readmenator/_mermaid.py:26` | `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style...` |
| `_sanitize_id` | method | `readmenator/_mermaid.py:45` | `def _sanitize_id(node_id)` |
| `render` | method | `readmenator/_mermaid.py:56` | `def render(self, nodes, edges, resolved_edges, analysis)` |
| `AnalysisResult` | class | `readmenator/_models.py:130` | `class AnalysisResult` |
| `AnalysisResultV2` | class | `readmenator/_models.py:284` | `class AnalysisResultV2` |
| `ChangeImpact` | class | `readmenator/_models.py:200` | `class ChangeImpact` |
| `CommunityResult` | class | `readmenator/_models.py:111` | `class CommunityResult` |
| `ConceptGraph` | class | `readmenator/_models.py:442` | `class ConceptGraph` |
| `ConceptNode` | class | `readmenator/_models.py:404` | `class ConceptNode` |
| `ConceptRelation` | class | `readmenator/_models.py:421` | `class ConceptRelation` |
| `DataflowIssue` | class | `readmenator/_models.py:309` | `class DataflowIssue` |
| `DeadCodeReport` | class | `readmenator/_models.py:349` | `class DeadCodeReport` |
| `DependencyCycle` | class | `readmenator/_models.py:187` | `class DependencyCycle` |
| `Edge` | class | `readmenator/_models.py:58` | `class Edge` |
| `HotspotResult` | class | `readmenator/_models.py:217` | `class HotspotResult` |
| `LayerViolation` | class | `readmenator/_models.py:263` | `class LayerViolation` |
| `LinterViolation` | class | `readmenator/_models.py:332` | `class LinterViolation` |
| `Node` | class | `readmenator/_models.py:37` | `class Node` |
| `RefactoringAction` | class | `readmenator/_models.py:366` | `class RefactoringAction` |
| `RefactoringPlan` | class | `readmenator/_models.py:387` | `class RefactoringPlan` |
| `SecurityFinding` | class | `readmenator/_models.py:77` | `class SecurityFinding` |
| `SuggestedRule` | class | `readmenator/_models.py:238` | `class SuggestedRule` |
| `Symbol` | class | `readmenator/_models.py:18` | `class Symbol` |
| `TaintAnalysisResult` | class | `readmenator/_models.py:172` | `class TaintAnalysisResult` |
| `TaintPath` | class | `readmenator/_models.py:151` | `class TaintPath` |
| `pluralize_symbol_kind` | method | `readmenator/_models.py:101` | `def pluralize_symbol_kind(kind, plural_map)` |
| `AnalyzerFactory` | class | `readmenator/_pipeline.py:59` | `class AnalyzerFactory` |
| `DeepAnalysisRunner` | class | `readmenator/_pipeline.py:390` | `class DeepAnalysisRunner` |
| `__init__` | method | `readmenator/_pipeline.py:67` | `def __init__(self, config)` |
| `__init__` | method | `readmenator/_pipeline.py:399` | `def __init__(self, factory)` |
| `agent_injector` | method | `readmenator/_pipeline.py:214` | `def agent_injector(self)` |
| `agent_output` | method | `readmenator/_pipeline.py:231` | `def agent_output(self)` |
| `analytics` | method | `readmenator/_pipeline.py:293` | `def analytics(self)` |
| `analyzer` | method | `readmenator/_pipeline.py:121` | `def analyzer(self)` |
| `build_typed_graph` | method | `readmenator/_pipeline.py:355` | `def build_typed_graph(self, nodes, edges, resolved_edges)` |
| `concepts` | method | `readmenator/_pipeline.py:279` | `def concepts(self)` |
| `cpg` | method | `readmenator/_pipeline.py:176` | `def cpg(self)` |
| `dataflow` | method | `readmenator/_pipeline.py:145` | `def dataflow(self)` |
| `diagram_builder` | method | `readmenator/_pipeline.py:237` | `def diagram_builder(self)` |
| `diagram_publisher` | method | `readmenator/_pipeline.py:258` | `def diagram_publisher(self)` |
| `diagram_renderer` | method | `readmenator/_pipeline.py:244` | `def diagram_renderer(self)` |
| `diagram_validator` | method | `readmenator/_pipeline.py:251` | `def diagram_validator(self)` |
| `embedder` | method | `readmenator/_pipeline.py:321` | `def embedder(self)` |
| `exclusions` | method | `readmenator/_pipeline.py:314` | `def exclusions(self)` |
| `exporter` | method | `readmenator/_pipeline.py:133` | `def exporter(self)` |
| `forcegraph` | method | `readmenator/_pipeline.py:286` | `def forcegraph(self)` |
| `generator` | method | `readmenator/_pipeline.py:115` | `def generator(self)` |
| `gh_wiki` | method | `readmenator/_pipeline.py:224` | `def gh_wiki(self)` |
| `graphrag` | method | `readmenator/_pipeline.py:328` | `def graphrag(self)` |
| `graphrag_store` | method | `readmenator/_pipeline.py:335` | `def graphrag_store(self)` |
| `hotspots` | method | `readmenator/_pipeline.py:152` | `def hotspots(self)` |
| `last_category` | method | `readmenator/_pipeline.py:382` | `def last_category(self)` |
| `last_typed_graph` | method | `readmenator/_pipeline.py:386` | `def last_typed_graph(self)` |
| `layer_detector` | method | `readmenator/_pipeline.py:185` | `def layer_detector(self)` |
| `layer_rules` | method | `readmenator/_pipeline.py:158` | `def layer_rules(self)` |
| `make_ranker` | method | `readmenator/_pipeline.py:365` | `def make_ranker(self, typed_graph)` |
| `memory` | method | `readmenator/_pipeline.py:342` | `def memory(self)` |
| `provenance` | method | `readmenator/_pipeline.py:307` | `def provenance(self)` |
| `readme_injector` | method | `readmenator/_pipeline.py:204` | `def readme_injector(self)` |
| `rule_gen` | method | `readmenator/_pipeline.py:164` | `def rule_gen(self)` |
| `run` | method | `readmenator/_pipeline.py:402` | `def run(self, nodes, edges, resolved_edges, layers, content_map)` |
| `sarif` | method | `readmenator/_pipeline.py:170` | `def sarif(self)` |
| `scanner` | method | `readmenator/_pipeline.py:109` | `def scanner(self)` |
| `scantext` | method | `readmenator/_pipeline.py:300` | `def scantext(self)` |
| `security` | method | `readmenator/_pipeline.py:127` | `def security(self)` |
| `skills` | method | `readmenator/_pipeline.py:349` | `def skills(self)` |
| `taint` | method | `readmenator/_pipeline.py:139` | `def taint(self)` |
| `uml` | method | `readmenator/_pipeline.py:191` | `def uml(self)` |
| `video` | method | `readmenator/_pipeline.py:272` | `def video(self)` |
| `vis_renderer` | method | `readmenator/_pipeline.py:265` | `def vis_renderer(self)` |
| `wiki` | method | `readmenator/_pipeline.py:197` | `def wiki(self)` |
| `DocProjection` | class | `readmenator/_projections.py:42` | `class DocProjection` |
| `IdentityProjection` | class | `readmenator/_projections.py:32` | `class IdentityProjection` |
| `Projection` | class | `readmenator/_projections.py:17` | `class Projection(Protocol)` |
| `RiskProjection` | class | `readmenator/_projections.py:63` | `class RiskProjection` |
| `__init__` | method | `readmenator/_projections.py:49` | `def __init__(self, documented_ids)` |
| `__init__` | method | `readmenator/_projections.py:70` | `def __init__(self, fan_in, fan_out, test_files)` |
| `apply_view` | method | `readmenator/_projections.py:95` | `def apply_view(category, view_config)` |
| `map_morphism` | method | `readmenator/_projections.py:27` | `def map_morphism(self, m)` |
| `map_morphism` | method | `readmenator/_projections.py:38` | `def map_morphism(self, m)` |
| `map_morphism` | method | `readmenator/_projections.py:57` | `def map_morphism(self, m)` |
| `map_morphism` | method | `readmenator/_projections.py:91` | `def map_morphism(self, m)` |
| `map_node` | method | `readmenator/_projections.py:23` | `def map_node(self, node)` |
| `map_node` | method | `readmenator/_projections.py:35` | `def map_node(self, node)` |
| `map_node` | method | `readmenator/_projections.py:52` | `def map_node(self, node)` |
| `map_node` | method | `readmenator/_projections.py:80` | `def map_node(self, node)` |
| `ProvenanceAuditor` | class | `readmenator/_provenance.py:46` | `class ProvenanceAuditor` |
| `ProvenanceFinding` | class | `readmenator/_provenance.py:20` | `class ProvenanceFinding` |
| `__init__` | method | `readmenator/_provenance.py:49` | `def __init__(self, config)` |
| `_attach_frequency` | method | `readmenator/_provenance.py:124` | `def _attach_frequency(self, findings, content_map)` |
| `_corpus_frequency` | method | `readmenator/_provenance.py:153` | `def _corpus_frequency(patterns, rows)` |
| `_snippet_in_content` | method | `readmenator/_provenance.py:115` | `def _snippet_in_content(self, file_path, snippet, content_map)` |
| `audit` | method | `readmenator/_provenance.py:57` | `def audit(self, findings, content_map)` |
| `is_inferred_only` | method | `readmenator/_provenance.py:32` | `def is_inferred_only(self)` |
| `reading` | method | `readmenator/_provenance.py:37` | `def reading(self)` |
| `summary` | method | `readmenator/_provenance.py:98` | `def summary(self, findings)` |
| `_primary_symbol` | function | `readmenator/_purpose.py:116` | `def _primary_symbol(symbols)` |
| `clean_purpose` | function | `readmenator/_purpose.py:43` | `def clean_purpose(text)` |
| `escape_cell` | function | `readmenator/_purpose.py:66` | `def escape_cell(text)` |
| `file_purpose` | function | `readmenator/_purpose.py:140` | `def file_purpose(node, max_chars)` |
| `first_sentence` | function | `readmenator/_purpose.py:98` | `def first_sentence(doc)` |
| `is_garbage_doc` | function | `readmenator/_purpose.py:26` | `def is_garbage_doc(text)` |
| `truncate_words` | function | `readmenator/_purpose.py:78` | `def truncate_words(text, max_chars)` |
| `QueryEngine` | class | `readmenator/_query.py:25` | `class QueryEngine` |
| `__init__` | method | `readmenator/_query.py:34` | `def __init__(self, nodes, edges, resolved_edges, ranker, config)` |
| `_bfs_shortest_path` | method | `readmenator/_query.py:331` | `def _bfs_shortest_path(self, graph, start, goal)` |
| `_build_import_graph` | method | `readmenator/_query.py:184` | `def _build_import_graph(self)` |
| `_build_resolved_graph` | method | `readmenator/_query.py:200` | `def _build_resolved_graph(self)` |
| `_build_symbol_index` | method | `readmenator/_query.py:170` | `def _build_symbol_index(self)` |
| `_estimate_doc_coverage` | method | `readmenator/_query.py:150` | `def _estimate_doc_coverage(self)` |
| `_estimate_test_coverage` | method | `readmenator/_query.py:124` | `def _estimate_test_coverage(self)` |
| `_find_incoming_imports` | method | `readmenator/_query.py:277` | `def _find_incoming_imports(self, target)` |
| `_init_default_ranker` | method | `readmenator/_query.py:64` | `def _init_default_ranker(self)` |
| `_make_bidirectional` | method | `readmenator/_query.py:315` | `def _make_bidirectional(graph)` |
| `explain` | method | `readmenator/_query.py:238` | `def explain(self, name)` |
| `find_path` | method | `readmenator/_query.py:285` | `def find_path(self, symbol_a, symbol_b)` |
| `find_symbol` | method | `readmenator/_query.py:220` | `def find_symbol(self, name)` |
| `query` | method | `readmenator/_query.py:355` | `def query(self, question)` |
| `ranked_query` | method | `readmenator/_query.py:73` | `def ranked_query(self, query, top_n)` |
| `summary` | method | `readmenator/_query.py:411` | `def summary(self)` |
| `CompositeRanker` | class | `readmenator/_rank.py:411` | `class CompositeRanker` |
| `RankConfig` | class | `readmenator/_rank.py:32` | `class RankConfig` |
| `RankedItem` | class | `readmenator/_rank.py:354` | `class RankedItem` |
| `RankedResult` | class | `readmenator/_rank.py:383` | `class RankedResult` |
| `__init__` | method | `readmenator/_rank.py:419` | `def __init__(self, graph, config)` |
| `_find_justification_paths` | method | `readmenator/_rank.py:520` | `def _find_justification_paths(self, target, seed_ids, category, max_paths)` |
| `_format_explanation` | method | `readmenator/_rank.py:546` | `def _format_explanation(item, result)` |
| `_get_global_pr` | method | `readmenator/_rank.py:428` | `def _get_global_pr(self)` |
| `build_seeds_for_context` | method | `readmenator/_rank.py:320` | `def build_seeds_for_context(node_ids, anchor_patterns)` |
| `build_seeds_from_query` | method | `readmenator/_rank.py:274` | `def build_seeds_from_query(query, node_ids, node_labels, symbols)` |
| `explain` | method | `readmenator/_rank.py:403` | `def explain(self, node_id)` |
| `file_pagerank` | method | `readmenator/_rank.py:119` | `def file_pagerank(file_ids, edges, alpha, max_iter, tolerance)` |
| `global_pagerank` | method | `readmenator/_rank.py:61` | `def global_pagerank(graph, alpha, max_iter, tolerance)` |
| `hits` | method | `readmenator/_rank.py:223` | `def hits(graph, max_iter, tolerance)` |
| `label` | method | `readmenator/_rank.py:378` | `def label(self)` |
| `personalized_pagerank` | method | `readmenator/_rank.py:153` | `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` |
| `rank` | method | `readmenator/_rank.py:438` | `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` |
| `top` | method | `readmenator/_rank.py:400` | `def top(self, n)` |
| `ReadmeInjector` | class | `readmenator/_readme_injector.py:70` | `class ReadmeInjector` |
| `__init__` | method | `readmenator/_readme_injector.py:78` | `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)` |
| `_build_injection` | method | `readmenator/_readme_injector.py:172` | `def _build_injection(self, suffix)` |
| `_extract_current_injection` | method | `readmenator/_readme_injector.py:117` | `def _extract_current_injection(content)` |
| `_find_readme` | method | `readmenator/_readme_injector.py:165` | `def _find_readme(root)` |
| `_remove_old_injection` | method | `readmenator/_readme_injector.py:126` | `def _remove_old_injection(content)` |
| `inject` | method | `readmenator/_readme_injector.py:88` | `def inject(self, project_root)` |
| `remove` | method | `readmenator/_readme_injector.py:136` | `def remove(self, project_root)` |
| `MonolithRefactorizer` | class | `readmenator/_refactorizer.py:24` | `class MonolithRefactorizer` |
| `__init__` | method | `readmenator/_refactorizer.py:32` | `def __init__(self, config)` |
| `_estimate_impact` | method | `readmenator/_refactorizer.py:147` | `def _estimate_impact(self, file_id, resolved_edges)` |
| `_get_line_count` | method | `readmenator/_refactorizer.py:70` | `def _get_line_count(self, file_id, content_map)` |
| `_group_symbols_by_kind` | method | `readmenator/_refactorizer.py:126` | `def _group_symbols_by_kind(self, symbols)` |
| `_plan_refactoring` | method | `readmenator/_refactorizer.py:82` | `def _plan_refactoring(self, node, edges, resolved_edges, content_map)` |
| `_suggest_target_file` | method | `readmenator/_refactorizer.py:132` | `def _suggest_target_file(self, source_file, kind)` |
| `analyze` | method | `readmenator/_refactorizer.py:35` | `def analyze(self, nodes, edges, resolved_edges, content_map)` |
| `generate_script` | method | `readmenator/_refactorizer.py:156` | `def generate_script(self, plan, project_root)` |
| `ImportResolver` | class | `readmenator/_resolver.py:18` | `class ImportResolver` |
| `__init__` | method | `readmenator/_resolver.py:61` | `def __init__(self, file_ids, root, extensions, include_dirs)` |
| `_build_dir_index` | method | `readmenator/_resolver.py:93` | `def _build_dir_index(self, file_ids)` |
| `_build_stem_index` | method | `readmenator/_resolver.py:83` | `def _build_stem_index(self, file_ids)` |
| `_resolve_basename_match` | method | `readmenator/_resolver.py:306` | `def _resolve_basename_match(self, import_str)` |
| `_resolve_directory_init` | method | `readmenator/_resolver.py:244` | `def _resolve_directory_init(self, import_str, source_file)` |
| `_resolve_extensionless` | method | `readmenator/_resolver.py:235` | `def _resolve_extensionless(self, import_str, source_file)` |
| `_resolve_include_dirs` | method | `readmenator/_resolver.py:179` | `def _resolve_include_dirs(self, import_str)` |
| `_resolve_module_dotpath` | method | `readmenator/_resolver.py:269` | `def _resolve_module_dotpath(self, import_str)` |
| `_resolve_relative` | method | `readmenator/_resolver.py:199` | `def _resolve_relative(self, import_str, source_file)` |
| `_resolve_root_package` | method | `readmenator/_resolver.py:254` | `def _resolve_root_package(self, import_str)` |
| `_resolve_stem_match` | method | `readmenator/_resolver.py:324` | `def _resolve_stem_match(self, import_str)` |
| `_resolve_suffix_match` | method | `readmenator/_resolver.py:291` | `def _resolve_suffix_match(self, import_str)` |
| `_resolve_verbatim` | method | `readmenator/_resolver.py:217` | `def _resolve_verbatim(self, import_str, source_file)` |
| `_strip_extension` | method | `readmenator/_resolver.py:333` | `def _strip_extension(self, name)` |
| `resolve` | method | `readmenator/_resolver.py:110` | `def resolve(self, import_str, source_file)` |
| `resolve_all` | method | `readmenator/_resolver.py:163` | `def resolve_all(self, import_str, source_file)` |
| `RuleGenerator` | class | `readmenator/_rule_gen.py:14` | `class RuleGenerator` |
| `__init__` | method | `readmenator/_rule_gen.py:90` | `def __init__(self, config)` |
| `_analyze_language` | method | `readmenator/_rule_gen.py:171` | `def _analyze_language(self, lang, nodes, content_map)` |
| `_detect_antipatterns` | method | `readmenator/_rule_gen.py:204` | `def _detect_antipatterns(self, nodes, content_map)` |
| `_group_by_language` | method | `readmenator/_rule_gen.py:161` | `def _group_by_language(self, nodes)` |
| `_infer_language_for_rule` | method | `readmenator/_rule_gen.py:250` | `def _infer_language_for_rule(rule_id)` |
| `_next_rule_id` | method | `readmenator/_rule_gen.py:260` | `def _next_rule_id(self)` |
| `generate` | method | `readmenator/_rule_gen.py:94` | `def generate(self, nodes, content_map)` |
| `write_rules` | method | `readmenator/_rule_gen.py:122` | `def write_rules(self, rules, output_dir)` |
| `SarifExporter` | class | `readmenator/_sarif.py:11` | `class SarifExporter` |
| `__init__` | method | `readmenator/_sarif.py:30` | `def __init__(self, privacy_mode)` |
| `_build_result` | method | `readmenator/_sarif.py:106` | `def _build_result(self, finding, rule_index)` |
| `_build_rule` | method | `readmenator/_sarif.py:82` | `def _build_rule(self, finding)` |
| `export` | method | `readmenator/_sarif.py:33` | `def export(self, findings, project_name)` |
| `PolyglotScanner` | class | `readmenator/_scanner.py:28` | `class PolyglotScanner` |
| `__init__` | method | `readmenator/_scanner.py:39` | `def __init__(self, config)` |
| `_check_directory_depth` | method | `readmenator/_scanner.py:167` | `def _check_directory_depth(self, path, root)` |
| `_emit_progress` | method | `readmenator/_scanner.py:251` | `def _emit_progress(self, count)` |
| `_extract_file_doc` | method | `readmenator/_scanner.py:175` | `def _extract_file_doc(self, content)` |
| `_gitignore_glob_to_regex` | method | `readmenator/_scanner.py:105` | `def _gitignore_glob_to_regex(pattern)` |
| `_is_generated` | method | `readmenator/_scanner.py:57` | `def _is_generated(self, rel_path)` |
| `_is_gitignored` | method | `readmenator/_scanner.py:145` | `def _is_gitignored(self, rel_path)` |
| `_is_ignored` | method | `readmenator/_scanner.py:50` | `def _is_ignored(self, path)` |
| `_load_gitignore` | method | `readmenator/_scanner.py:83` | `def _load_gitignore(self, root)` |
| `_scan_impl` | method | `readmenator/_scanner.py:286` | `def _scan_impl(self, root)` |
| `_validate_path_security` | method | `readmenator/_scanner.py:154` | `def _validate_path_security(self, path)` |
| `scan` | method | `readmenator/_scanner.py:261` | `def scan(self, root)` |
| `scan_with_content` | method | `readmenator/_scanner.py:275` | `def scan_with_content(self, root)` |
| `ScanTextBuilder` | class | `readmenator/_scantext.py:16` | `class ScanTextBuilder` |
| `__init__` | method | `readmenator/_scantext.py:19` | `def __init__(self, config)` |
| `build_corpus` | method | `readmenator/_scantext.py:67` | `def build_corpus(self, nodes, content_map, edges)` |
| `build_for_node` | method | `readmenator/_scantext.py:27` | `def build_for_node(self, node, content, imports)` |
| `SecurityAnalyzer` | class | `readmenator/_security.py:486` | `class SecurityAnalyzer` |
| `SecurityRule` | class | `readmenator/_security.py:24` | `class SecurityRule` |
| `__init__` | method | `readmenator/_security.py:496` | `def __init__(self, config)` |
| `_build_rules_from_yaml` | method | `readmenator/_security.py:447` | `def _build_rules_from_yaml(yaml_path)` |
| `_c_rules` | method | `readmenator/_security.py:201` | `def _c_rules()` |
| `_compile` | method | `readmenator/_security.py:148` | `def _compile()` |
| `_csharp_rules` | method | `readmenator/_security.py:297` | `def _csharp_rules()` |
| `_dart_rules` | method | `readmenator/_security.py:354` | `def _dart_rules()` |
| `_elixir_rules` | method | `readmenator/_security.py:398` | `def _elixir_rules()` |
| `_gdscript_rules` | method | `readmenator/_security.py:387` | `def _gdscript_rules()` |
| `_go_rules` | method | `readmenator/_security.py:237` | `def _go_rules()` |
| `_java_rules` | method | `readmenator/_security.py:222` | `def _java_rules()` |
| `_javascript_rules` | method | `readmenator/_security.py:182` | `def _javascript_rules()` |
| `_kotlin_rules` | method | `readmenator/_security.py:310` | `def _kotlin_rules()` |
| `_load_rules_from_yaml` | method | `readmenator/_security.py:128` | `def _load_rules_from_yaml(yaml_path)` |
| `_lua_rules` | method | `readmenator/_security.py:343` | `def _lua_rules()` |
| `_meets_threshold` | method | `readmenator/_security.py:509` | `def _meets_threshold(self, severity)` |
| `_nim_rules` | method | `readmenator/_security.py:376` | `def _nim_rules()` |
| `_parse_minimal_yaml` | method | `readmenator/_security.py:46` | `def _parse_minimal_yaml(text)` |
| `_php_rules` | method | `readmenator/_security.py:267` | `def _php_rules()` |
| `_python_rules` | method | `readmenator/_security.py:153` | `def _python_rules()` |
| `_resolve_rules` | method | `readmenator/_security.py:500` | `def _resolve_rules(self)` |
| `_ruby_rules` | method | `readmenator/_security.py:250` | `def _ruby_rules()` |
| `_rust_rules` | method | `readmenator/_security.py:365` | `def _rust_rules()` |
| `_scala_rules` | method | `readmenator/_security.py:332` | `def _scala_rules()` |
| `_shell_rules` | method | `readmenator/_security.py:284` | `def _shell_rules()` |
| `_swift_rules` | method | `readmenator/_security.py:321` | `def _swift_rules()` |
| `_unquote` | method | `readmenator/_security.py:121` | `def _unquote(s)` |
| `_validate_path` | method | `readmenator/_security.py:555` | `def _validate_path(self, path, root)` |
| `fix_hint_for` | method | `readmenator/_security.py:620` | `def fix_hint_for(finding)` |
| `scan` | method | `readmenator/_security.py:513` | `def scan(self, root)` |
| `summary` | method | `readmenator/_security.py:572` | `def summary(self, findings)` |
| `SkillInstaller` | class | `readmenator/_skill_installer.py:22` | `class SkillInstaller` |
| `__init__` | method | `readmenator/_skill_installer.py:25` | `def __init__(self, config)` |
| `available` | method | `readmenator/_skill_installer.py:38` | `def available(self)` |
| `install` | method | `readmenator/_skill_installer.py:61` | `def install(self, project_root, target)` |
| `maybe_install_on_run` | method | `readmenator/_skill_installer.py:87` | `def maybe_install_on_run(self, project_root)` |
| `source_dir` | method | `readmenator/_skill_installer.py:34` | `def source_dir()` |
| `target_dir` | method | `readmenator/_skill_installer.py:48` | `def target_dir(self, project_root, target)` |
| `TaintAnalyzer` | class | `readmenator/_taint.py:12` | `class TaintAnalyzer` |
| `__init__` | method | `readmenator/_taint.py:73` | `def __init__(self, config)` |
| `_build_forward_graph` | method | `readmenator/_taint.py:213` | `def _build_forward_graph(nodes, resolved_edges)` |
| `_find_direct_sources` | method | `readmenator/_taint.py:136` | `def _find_direct_sources(self, nodes, edges)` |
| `_propagate` | method | `readmenator/_taint.py:162` | `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` |
| `analyze` | method | `readmenator/_taint.py:77` | `def analyze(self, nodes, edges, resolved_edges)` |
| `UmlGenerator` | class | `readmenator/_uml.py:34` | `class UmlGenerator` |
| `__init__` | method | `readmenator/_uml.py:36` | `def __init__(self, config)` |
| `_cpp_params` | method | `readmenator/_uml.py:259` | `def _cpp_params(params)` |
| `_cs_params` | method | `readmenator/_uml.py:345` | `def _cs_params(params)` |
| `_extract_params` | method | `readmenator/_uml.py:592` | `def _extract_params(signature)` |
| `_find_node` | method | `readmenator/_uml.py:165` | `def _find_node(nodes, node_id)` |
| `_generate_cpp` | method | `readmenator/_uml.py:233` | `def _generate_cpp(class_symbols, nodes, edges)` |
| `_generate_csharp` | method | `readmenator/_uml.py:316` | `def _generate_csharp(class_symbols, nodes, edges)` |
| `_generate_dart` | method | `readmenator/_uml.py:547` | `def _generate_dart(class_symbols, nodes, edges)` |
| `_generate_go` | method | `readmenator/_uml.py:395` | `def _generate_go(class_symbols, nodes, edges)` |
| `_generate_java` | method | `readmenator/_uml.py:274` | `def _generate_java(class_symbols, nodes, edges)` |
| `_generate_kotlin` | method | `readmenator/_uml.py:476` | `def _generate_kotlin(class_symbols, nodes, edges)` |
| `_generate_php` | method | `readmenator/_uml.py:448` | `def _generate_php(class_symbols, nodes, edges)` |
| `_generate_python` | method | `readmenator/_uml.py:360` | `def _generate_python(class_symbols, nodes, edges)` |
| `_generate_ruby` | method | `readmenator/_uml.py:567` | `def _generate_ruby(class_symbols, nodes, edges)` |
| `_generate_rust` | method | `readmenator/_uml.py:422` | `def _generate_rust(class_symbols, nodes, edges)` |
| `_generate_scala` | method | `readmenator/_uml.py:496` | `def _generate_scala(class_symbols, nodes, edges)` |
| `_generate_swift` | method | `readmenator/_uml.py:518` | `def _generate_swift(class_symbols, nodes, edges)` |
| `_get_code_generator` | method | `readmenator/_uml.py:172` | `def _get_code_generator(language)` |
| `_java_params` | method | `readmenator/_uml.py:301` | `def _java_params(params)` |
| `_safe_name` | method | `readmenator/_uml.py:588` | `def _safe_name(name)` |
| `_sanitize_id` | method | `readmenator/_uml.py:153` | `def _sanitize_id(raw)` |
| `_type_map_py_to_target` | method | `readmenator/_uml.py:190` | `def _type_map_py_to_target(target, py_type_hint)` |
| `generate_code` | method | `readmenator/_uml.py:129` | `def generate_code(self, nodes, edges, target_language)` |
| `render_mermaid_class_diagram` | method | `readmenator/_uml.py:39` | `def render_mermaid_class_diagram(self, nodes, edges)` |
| `Fe` | class | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `Ha` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Ia` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `La` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Lo` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Na` | class | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `Sr` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `_` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `_n` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `as` | class | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `as` | class | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `b` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `cr` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `e` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `e` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `e` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `f` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `h` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `h` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `i` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `i` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `l` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `n` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `o` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `r` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `s` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `s` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `t` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `u` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `wa` | class | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `xo` | function | `readmenator/_vendor/force-graph.min.js:5` | `` |
| `y` | function | `readmenator/_vendor/force-graph.min.js:2` | `` |
| `Backdrop` | class | `readmenator/_video.py:269` | `class Backdrop` |
| `CinematicVideoRenderer` | class | `readmenator/_video.py:464` | `class CinematicVideoRenderer` |
| `__init__` | method | `readmenator/_video.py:272` | `def __init__(self, width, height)` |
| `_build_dep_tree` | method | `readmenator/_video.py:631` | `def _build_dep_tree(self, node_by_id, link_set, god_names)` |
| `_caption_y` | function | `readmenator/_video.py:131` | `def _caption_y(cfg)` |
| `_code_tint` | function | `readmenator/_video.py:205` | `def _code_tint(line)` |
| `_dna_boxes` | function | `readmenator/_video.py:145` | `def _dna_boxes(cfg)` |
| `_draw_frame` | method | `readmenator/_video.py:895` | `def _draw_frame(fi)` |
| `_find` | method | `readmenator/_video.py:234` | `def _find(style)` |
| `_graph_boxes` | function | `readmenator/_video.py:136` | `def _graph_boxes(cfg)` |
| `_img` | method | `readmenator/_video.py:325` | `def _img()` |
| `_packet_offset` | function | `readmenator/_video.py:215` | `def _packet_offset(a, b, k)` |
| `_panel` | function | `readmenator/_video.py:126` | `def _panel(cfg)` |
| `_polyline_point` | function | `readmenator/_video.py:170` | `def _polyline_point(points, f)` |
| `_prepare_layouts` | method | `readmenator/_video.py:829` | `def _prepare_layouts(self, data)` |
| `_render_frame_bytes` | method | `readmenator/_video.py:890` | `def _render_frame_bytes(fi)` |
| `_scan_cursor` | function | `readmenator/_video.py:196` | `def _scan_cursor(d, box, progress, col)` |
| `_scene_bundle` | method | `readmenator/_video.py:1243` | `def _scene_bundle(img, d, lt, gt, sc)` |
| `_scene_card` | method | `readmenator/_video.py:957` | `def _scene_card(img, d, lt, gt, sc)` |
| `_scene_communities` | method | `readmenator/_video.py:1113` | `def _scene_communities(img, d, lt, gt, sc)` |
| `_scene_dna` | method | `readmenator/_video.py:1329` | `def _scene_dna(img, d, lt, gt, sc)` |
| `_scene_gods` | method | `readmenator/_video.py:996` | `def _scene_gods(img, d, lt, gt, sc)` |
| `_scene_graph` | method | `readmenator/_video.py:1157` | `def _scene_graph(img, d, lt, gt, sc)` |
| `_scene_layers` | method | `readmenator/_video.py:971` | `def _scene_layers(img, d, lt, gt, sc)` |
| `_scene_outro` | method | `readmenator/_video.py:1388` | `def _scene_outro(img, d, lt, gt, sc)` |
| `_scene_title` | method | `readmenator/_video.py:922` | `def _scene_title(img, d, lt, gt, sc)` |
| `_scene_tree` | method | `readmenator/_video.py:1039` | `def _scene_tree(img, d, lt, gt, sc)` |
| `_split_boxes` | function | `readmenator/_video.py:154` | `def _split_boxes(cfg)` |
| `_sun` | method | `readmenator/_video.py:310` | `def _sun(self, r)` |
| `_verdict_badge` | function | `readmenator/_video.py:181` | `def _verdict_badge(d, box, text, fonts, lt, dur, col)` |
| `alpha` | function | `readmenator/_video.py:104` | `def alpha(c, a)` |
| `build_scenes` | method | `readmenator/_video.py:682` | `def build_scenes(self, data)` |

Next: [SYMBOLS_p3.md](SYMBOLS_p3.md)
