# API (page 2 of 2)
Previous: [API.md](API.md)

## readmenator/_mermaid.py
Depends on: `readmenator/_models.py`
Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`
- `MermaidRenderer.__init__` (method) `readmenator/_mermaid.py:26` `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style...` -- Initialise rendering budgets and styles.
- `MermaidRenderer.render` (method) `readmenator/_mermaid.py:74` `def render(self, nodes, edges, resolved_edges, analysis)` -- Produce a Mermaid flowchart string and a truncation flag.

## readmenator/_models.py
Depends on: `readmenator/_category.py`
Imported by: `readmenator/__init__.py`, `readmenator/_agent_output.py`, `readmenator/_analytics.py`, `readmenator/_analyzer.py`, `readmenator/_apidocs.py`, `readmenator/_app.py`, `readmenator/_components.py`, `readmenator/_concepts.py`, `readmenator/_cpg.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dataflow.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_explorer.py`, `readmenator/_exporter.py`, `readmenator/_flowcharts.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_memory.py`, `readmenator/_mermaid.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_provenance.py`, `readmenator/_purpose.py`, `readmenator/_query.py`, `readmenator/_refactorizer.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_scantext.py`, `readmenator/_security.py`, `readmenator/_sourceview.py`, `readmenator/_symindex.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_video.py`, `readmenator/_wiki.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`, `tests/test_agent_friendliness.py`, `tests/test_agent_output.py`, `tests/test_analyzer.py`, `tests/test_apidocs.py`, `tests/test_bundlegraph.py`, `tests/test_components.py`, `tests/test_concepts.py`, `tests/test_cpg.py`, `tests/test_cursorrules.py`, `tests/test_dataflow.py`, `tests/test_dead_code.py`, `tests/test_diagrams.py`, `tests/test_documentation.py`, `tests/test_exporter.py`, `tests/test_flowcharts.py`, `tests/test_graphrag.py`, `tests/test_hotspots.py`, `tests/test_interactive_graph.py`, `tests/test_layer_rules.py`, `tests/test_layout_quality.py`, `tests/test_linter.py`, `tests/test_memory.py`, `tests/test_mermaid.py`, `tests/test_models.py`, `tests/test_parsers_property.py`, `tests/test_query.py`, `tests/test_ranking.py`, `tests/test_refactorizer.py`, `tests/test_rule_gen.py`, `tests/test_sarif.py`, `tests/test_scanner.py`, `tests/test_security.py`, `tests/test_sourceview.py`, `tests/test_symindex.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`, `tests/test_uml.py`, `tests/test_video.py`, `tests/test_wiki.py`
- `pluralize_symbol_kind` (function) `readmenator/_models.py:101` `def pluralize_symbol_kind(kind, plural_map)` -- Return the plural form of *kind* according to *plural_map*.

## readmenator/_ollama.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/__init__.py`, `readmenator/_components.py`, `readmenator/_pipeline.py`, `tests/test_ollama.py`
- `strip_thinking` (function) `readmenator/_ollama.py:21` `def strip_thinking(text)` -- Remove reasoning-model thinking blocks from a completion.
- `OllamaClient.__init__` (method) `readmenator/_ollama.py:36` `def __init__(self, config)` -- Initialise with application configuration.
- `OllamaClient.enabled` (method) `readmenator/_ollama.py:44` `def enabled(self)` -- Return True when Ollama enrichment is switched on.
- `OllamaClient.available` (method) `readmenator/_ollama.py:48` `def available(self, timeout)` -- Probe the daemon without generating text.
- `OllamaClient.generate` (method) `readmenator/_ollama.py:69` `def generate(self, prompt, system)` -- Generate one completion, bounded and infallible.
- `OllamaClient.describe_component` (method) `readmenator/_ollama.py:104` `def describe_component(self, name, files, symbols, imports)` -- Draft a one-paragraph component description via Ollama.

## readmenator/_pipeline.py
Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analytics.py`, `readmenator/_analyzer.py`, `readmenator/_apidocs.py`, `readmenator/_apidocs_render.py`, `readmenator/_bundlegraph.py`, `readmenator/_category.py`, `readmenator/_components.py`, `readmenator/_concepts.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_embed.py`, `readmenator/_exclusions.py`, `readmenator/_exporter.py`, `readmenator/_forcegraph.py`, `readmenator/_gh_wiki.py`, `readmenator/_graphrag.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_memory.py`, `readmenator/_models.py`, `readmenator/_ollama.py`, `readmenator/_provenance.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_scantext.py`, `readmenator/_security.py`, `readmenator/_skill_installer.py`, `readmenator/_sourceview.py`, `readmenator/_symindex.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_video.py`, `readmenator/_wiki.py`
Imported by: `readmenator/_app.py`
- `AnalyzerFactory.__init__` (method) `readmenator/_pipeline.py:74` `def __init__(self, config)`
- `AnalyzerFactory.scanner` (method) `readmenator/_pipeline.py:123` `def scanner(self)`
- `AnalyzerFactory.generator` (method) `readmenator/_pipeline.py:129` `def generator(self)`
- `AnalyzerFactory.analyzer` (method) `readmenator/_pipeline.py:135` `def analyzer(self)`
- `AnalyzerFactory.security` (method) `readmenator/_pipeline.py:141` `def security(self)`
- `AnalyzerFactory.exporter` (method) `readmenator/_pipeline.py:147` `def exporter(self)`
- `AnalyzerFactory.taint` (method) `readmenator/_pipeline.py:153` `def taint(self)`
- `AnalyzerFactory.dataflow` (method) `readmenator/_pipeline.py:159` `def dataflow(self)` -- Return the lazily initialised dataflow analyzer.
- `AnalyzerFactory.hotspots` (method) `readmenator/_pipeline.py:166` `def hotspots(self)`
- `AnalyzerFactory.layer_rules` (method) `readmenator/_pipeline.py:172` `def layer_rules(self)`
- `AnalyzerFactory.rule_gen` (method) `readmenator/_pipeline.py:178` `def rule_gen(self)`
- `AnalyzerFactory.sarif` (method) `readmenator/_pipeline.py:184` `def sarif(self)`
- `AnalyzerFactory.cpg` (method) `readmenator/_pipeline.py:190` `def cpg(self)`
- `AnalyzerFactory.layer_detector` (method) `readmenator/_pipeline.py:199` `def layer_detector(self)`
- `AnalyzerFactory.uml` (method) `readmenator/_pipeline.py:205` `def uml(self)`
- `AnalyzerFactory.wiki` (method) `readmenator/_pipeline.py:211` `def wiki(self)` -- Return the lazily initialised agent wiki generator.
- `AnalyzerFactory.readme_injector` (method) `readmenator/_pipeline.py:218` `def readme_injector(self)`
- `AnalyzerFactory.agent_injector` (method) `readmenator/_pipeline.py:242` `def agent_injector(self)`
- `AnalyzerFactory.gh_wiki` (method) `readmenator/_pipeline.py:252` `def gh_wiki(self)` -- Return the lazily initialised GitHub wiki publisher.
- `AnalyzerFactory.agent_output` (method) `readmenator/_pipeline.py:259` `def agent_output(self)`
- `AnalyzerFactory.diagram_builder` (method) `readmenator/_pipeline.py:265` `def diagram_builder(self)` -- Return the lazily initialised system map builder.
- `AnalyzerFactory.diagram_renderer` (method) `readmenator/_pipeline.py:272` `def diagram_renderer(self)` -- Return the lazily initialised interactive map renderer.
- `AnalyzerFactory.diagram_validator` (method) `readmenator/_pipeline.py:279` `def diagram_validator(self)` -- Return the lazily initialised system map validator.
- `AnalyzerFactory.diagram_publisher` (method) `readmenator/_pipeline.py:286` `def diagram_publisher(self)` -- Return the lazily initialised documentation site publisher.
- `AnalyzerFactory.vis_renderer` (method) `readmenator/_pipeline.py:293` `def vis_renderer(self)` -- Return the lazily initialised vis.js network renderer.
- `AnalyzerFactory.video` (method) `readmenator/_pipeline.py:300` `def video(self)` -- Return the lazily initialised cinematic video renderer.
- `AnalyzerFactory.concepts` (method) `readmenator/_pipeline.py:307` `def concepts(self)` -- Return the lazily initialised semantic concept extractor.
- `AnalyzerFactory.forcegraph` (method) `readmenator/_pipeline.py:314` `def forcegraph(self)` -- Return the lazily initialised force-graph renderer.
- `AnalyzerFactory.bundlegraph` (method) `readmenator/_pipeline.py:321` `def bundlegraph(self)` -- Return the lazily initialised edge bundle explorer renderer.
- `AnalyzerFactory.analytics` (method) `readmenator/_pipeline.py:328` `def analytics(self)` -- Return the lazily initialised corpus analytics builder.
- `AnalyzerFactory.scantext` (method) `readmenator/_pipeline.py:335` `def scantext(self)` -- Return the lazily initialised scan-text builder.
- `AnalyzerFactory.provenance` (method) `readmenator/_pipeline.py:342` `def provenance(self)` -- Return the lazily initialised provenance auditor.
- `AnalyzerFactory.exclusions` (method) `readmenator/_pipeline.py:349` `def exclusions(self)` -- Return the lazily initialised FP exclusion list.
- `AnalyzerFactory.embedder` (method) `readmenator/_pipeline.py:356` `def embedder(self)` -- Return the lazily initialised semantic embedder.
- `AnalyzerFactory.graphrag` (method) `readmenator/_pipeline.py:363` `def graphrag(self)` -- Return the lazily initialised GraphRAG index builder.
- `AnalyzerFactory.graphrag_store` (method) `readmenator/_pipeline.py:370` `def graphrag_store(self)` -- Return the lazily initialised GraphRAG index store.
- `AnalyzerFactory.memory` (method) `readmenator/_pipeline.py:377` `def memory(self)` -- Return the lazily initialised project memory.
- `AnalyzerFactory.skills` (method) `readmenator/_pipeline.py:384` `def skills(self)` -- Return the lazily initialised agent skill installer.
- `AnalyzerFactory.sourceview` (method) `readmenator/_pipeline.py:391` `def sourceview(self)` -- Return the lazily initialised source viewer builder.
- `AnalyzerFactory.symindex` (method) `readmenator/_pipeline.py:398` `def symindex(self)` -- Return the lazily initialised symbol index.
- `AnalyzerFactory.components` (method) `readmenator/_pipeline.py:405` `def components(self)` -- Return the lazily initialised component diagram builder.
- `AnalyzerFactory.apidocs` (method) `readmenator/_pipeline.py:412` `def apidocs(self)` -- Return the lazily initialised API reference builder.
- `AnalyzerFactory.apidocs_writer` (method) `readmenator/_pipeline.py:419` `def apidocs_writer(self)` -- Return the lazily initialised API reference writer.
- `AnalyzerFactory.ollama` (method) `readmenator/_pipeline.py:426` `def ollama(self)` -- Return the lazily initialised local Ollama client.
- `AnalyzerFactory.build_typed_graph` (method) `readmenator/_pipeline.py:432` `def build_typed_graph(self, nodes, edges, resolved_edges)`
- `AnalyzerFactory.make_ranker` (method) `readmenator/_pipeline.py:442` `def make_ranker(self, typed_graph)` -- Create a CompositeRanker for the given typed graph.
- `AnalyzerFactory.last_category` (method) `readmenator/_pipeline.py:459` `def last_category(self)`
- `AnalyzerFactory.last_typed_graph` (method) `readmenator/_pipeline.py:463` `def last_typed_graph(self)`
- `DeepAnalysisRunner.__init__` (method) `readmenator/_pipeline.py:476` `def __init__(self, factory)`
- `DeepAnalysisRunner.run` (method) `readmenator/_pipeline.py:479` `def run(self, nodes, edges, resolved_edges, layers, content_map)`

## readmenator/_projections.py
Depends on: `readmenator/_category.py`, `readmenator/_models.py`
Imported by: `tests/test_ranking.py`
- `Projection.map_node` (method) `readmenator/_projections.py:23` `def map_node(self, node)` -- Map a code node.
- `Projection.map_morphism` (method) `readmenator/_projections.py:27` `def map_morphism(self, m)` -- Map a morphism.
- `IdentityProjection.map_node` (method) `readmenator/_projections.py:35` `def map_node(self, node)`
- `IdentityProjection.map_morphism` (method) `readmenator/_projections.py:38` `def map_morphism(self, m)`
- `DocProjection.__init__` (method) `readmenator/_projections.py:49` `def __init__(self, documented_ids)`
- `DocProjection.map_node` (method) `readmenator/_projections.py:52` `def map_node(self, node)`
- `DocProjection.map_morphism` (method) `readmenator/_projections.py:57` `def map_morphism(self, m)`
- `RiskProjection.__init__` (method) `readmenator/_projections.py:70` `def __init__(self, fan_in, fan_out, test_files)`
- `RiskProjection.map_node` (method) `readmenator/_projections.py:80` `def map_node(self, node)`
- `RiskProjection.map_morphism` (method) `readmenator/_projections.py:91` `def map_morphism(self, m)`
- `apply_view` (function) `readmenator/_projections.py:95` `def apply_view(category, view_config)` -- Apply a named view to produce a projected category.

## readmenator/_provenance.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `ProvenanceFinding.is_inferred_only` (method) `readmenator/_provenance.py:32` `def is_inferred_only(self)` -- Return True when no static evidence supports the finding.
- `ProvenanceFinding.reading` (method) `readmenator/_provenance.py:37` `def reading(self)` -- Explain which way an inferred-only hit points.
- `ProvenanceAuditor.__init__` (method) `readmenator/_provenance.py:49` `def __init__(self, config)` -- Initialise with application configuration.
- `ProvenanceAuditor.audit` (method) `readmenator/_provenance.py:57` `def audit(self, findings, content_map)` -- Audit findings for evidence provenance.
- `ProvenanceAuditor.summary` (method) `readmenator/_provenance.py:98` `def summary(self, findings)` -- Summarize provenance findings by provenance class.

## readmenator/_purpose.py
Depends on: `readmenator/_models.py`
Imported by: `readmenator/_agent_output.py`, `readmenator/_components.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `readmenator/_memory.py`, `readmenator/_wiki.py`, `tests/test_agent_friendliness.py`
- `is_garbage_doc` (function) `readmenator/_purpose.py:26` `def is_garbage_doc(text)` -- Return True for doc lines that carry no purpose signal.
- `clean_purpose` (function) `readmenator/_purpose.py:43` `def clean_purpose(text)` -- Return the purpose signal of a doc first line, or an empty string.
- `escape_cell` (function) `readmenator/_purpose.py:66` `def escape_cell(text)` -- Escape markdown table breaking characters in one line of text.
- `truncate_words` (function) `readmenator/_purpose.py:78` `def truncate_words(text, max_chars)` -- Truncate text at a word boundary and mark the cut with an ellipsis.
- `first_sentence` (function) `readmenator/_purpose.py:98` `def first_sentence(doc)` -- Return the first clean sentence of the first meaningful paragraph.
- `file_purpose` (function) `readmenator/_purpose.py:140` `def file_purpose(node, max_chars)` -- Return a bounded one-sentence purpose for a file node.

## readmenator/_pytypes.py
Imported by: `readmenator/_apidocs.py`, `readmenator/_flowcharts.py`, `tests/test_flowcharts.py`
- `PythonReceiverTypes.__init__` (method) `readmenator/_pytypes.py:81` `def __init__(self, contents, language)` -- Index every Python file in *contents*.
- `PythonReceiverTypes.classes` (method) `readmenator/_pytypes.py:118` `def classes(self)` -- Return every project class name seen.
- `visit` (function) `readmenator/_pytypes.py:126` `def visit(body, owner)` -- Walk class and function bodies recording scopes.
- `PythonReceiverTypes.scope_at` (method) `readmenator/_pytypes.py:179` `def scope_at(self, file_id, line)` -- Return the innermost function scope spanning *line*.
- `PythonReceiverTypes.owner_of` (method) `readmenator/_pytypes.py:187` `def owner_of(self, file_id, line)` -- Return the class that defines the function starting at *line* ("" if none).
- `PythonReceiverTypes.receiver_class` (method) `readmenator/_pytypes.py:191` `def receiver_class(self, file_id, line, receiver)` -- Return the project class a receiver expression holds at a call site.
- `PythonReceiverTypes.lineage` (method) `readmenator/_pytypes.py:233` `def lineage(self, class_name)` -- Return *class_name* plus every project base class it derives from.
- `PythonReceiverTypes.resolve_method` (method) `readmenator/_pytypes.py:245` `def resolve_method(self, file_id, line, receiver, name)` -- Return the (file, line) of the method a typed receiver dispatches to.
- `PythonReceiverTypes.accepts` (method) `readmenator/_pytypes.py:269` `def accepts(self, file_id, line, receiver, target_file, target_line, target_name)` -- Decide whether a Python attribute call can target a definition.
- `PythonReceiverTypes.is_self_receiver` (method) `readmenator/_pytypes.py:304` `def is_self_receiver(self, receiver)` -- Return True for ``self``, ``cls``, and ``super()`` receivers.

## readmenator/_query.py
Depends on: `readmenator/_category.py`, `readmenator/_models.py`, `readmenator/_rank.py`
Imported by: `readmenator/_app.py`, `readmenator/_mcp_server.py`, `tests/test_query.py`
- `QueryEngine.__init__` (method) `readmenator/_query.py:34` `def __init__(self, nodes, edges, resolved_edges, ranker, config)` -- Initialise internal indexes from scanned data.
- `QueryEngine.ranked_query` (method) `readmenator/_query.py:73` `def ranked_query(self, query, top_n)` -- Answer *query* with a ranked list of relevant nodes.
- `QueryEngine.find_symbol` (method) `readmenator/_query.py:220` `def find_symbol(self, name)` -- Look up *name* by exact match, then by substring fuzzy match.
- `QueryEngine.explain` (method) `readmenator/_query.py:238` `def explain(self, name)` -- Return a detailed multi-line explanation of *name*.
- `QueryEngine.find_path` (method) `readmenator/_query.py:285` `def find_path(self, symbol_a, symbol_b)` -- Find the shortest import path from *symbol_a* to *symbol_b*.
- `QueryEngine.query` (method) `readmenator/_query.py:355` `def query(self, question)` -- Free-text search over symbols and file paths.
- `QueryEngine.summary` (method) `readmenator/_query.py:411` `def summary(self)` -- Return a concise overview of the loaded knowledge base.

## readmenator/_rank.py
Depends on: `readmenator/_category.py`
Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_components.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_video.py`, `tests/test_ranking.py`
- `global_pagerank` (function) `readmenator/_rank.py:61` `def global_pagerank(graph, alpha, max_iter, tolerance)` -- Compute global PageRank on the typed weighted graph.
- `file_pagerank` (function) `readmenator/_rank.py:119` `def file_pagerank(file_ids, edges, alpha, max_iter, tolerance)` -- Directed PageRank over file-to-file dependency pairs.
- `personalized_pagerank` (function) `readmenator/_rank.py:153` `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` -- Compute Personalized PageRank with a seed-node preference vector.
- `hits` (function) `readmenator/_rank.py:223` `def hits(graph, max_iter, tolerance)` -- Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.
- `build_seeds_from_query` (function) `readmenator/_rank.py:274` `def build_seeds_from_query(query, node_ids, node_labels, symbols)` -- Build a PPR seed vector from a natural-language query string.
- `build_seeds_for_context` (function) `readmenator/_rank.py:320` `def build_seeds_for_context(node_ids, anchor_patterns)` -- Build a PPR seed vector from anchor pattern strings.
- `RankedItem.label` (method) `readmenator/_rank.py:378` `def label(self)`
- `RankedResult.top` (method) `readmenator/_rank.py:400` `def top(self, n)`
- `RankedResult.explain` (method) `readmenator/_rank.py:403` `def explain(self, node_id)` -- Return a human-readable explanation of why *node_id* ranks as it does.
- `CompositeRanker.__init__` (method) `readmenator/_rank.py:419` `def __init__(self, graph, config)`
- `CompositeRanker.rank` (method) `readmenator/_rank.py:438` `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` -- Compute composite ranking for a query.

## readmenator/_readme_injector.py
Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`
- `ReadmeInjector.__init__` (method) `readmenator/_readme_injector.py:133` `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir, graphrag_output_dir, maps_output_dir, pages_dir...` -- Initialise the injector with output locations.
- `ReadmeInjector.inject` (method) `readmenator/_readme_injector.py:192` `def inject(self, project_root)` -- Inject or refresh the knowledge base section in the README.
- `ReadmeInjector.remove` (method) `readmenator/_readme_injector.py:284` `def remove(self, project_root)` -- Remove the injected section from the README.

## readmenator/_refactorizer.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`
- `MonolithRefactorizer.__init__` (method) `readmenator/_refactorizer.py:32` `def __init__(self, config)`
- `MonolithRefactorizer.analyze` (method) `readmenator/_refactorizer.py:35` `def analyze(self, nodes, edges, resolved_edges, content_map)` -- Identify monolithic files and generate refactoring plans.
- `MonolithRefactorizer.generate_script` (method) `readmenator/_refactorizer.py:156` `def generate_script(self, plan, project_root)`

## readmenator/_resolver.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `tests/test_agent_friendliness.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`
- `ImportResolver.__init__` (method) `readmenator/_resolver.py:61` `def __init__(self, file_ids, root, extensions, include_dirs)` -- Initialise the resolver with all known file paths.
- `ImportResolver.resolve` (method) `readmenator/_resolver.py:110` `def resolve(self, import_str, source_file)` -- Resolve an import string to a concrete project file path.
- `ImportResolver.resolve_all` (method) `readmenator/_resolver.py:163` `def resolve_all(self, import_str, source_file)` -- Resolve *import_str* to all possible matching project file paths.

## readmenator/_rule_gen.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_rule_gen.py`
- `RuleGenerator.__init__` (method) `readmenator/_rule_gen.py:90` `def __init__(self, config)`
- `RuleGenerator.generate` (method) `readmenator/_rule_gen.py:94` `def generate(self, nodes, content_map)` -- Generate suggested rules by scanning code patterns.
- `RuleGenerator.write_rules` (method) `readmenator/_rule_gen.py:122` `def write_rules(self, rules, output_dir)` -- Write suggested rules to Semgrep YAML files in output_dir.

## readmenator/_sarif.py
Depends on: `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_sarif.py`
- `SarifExporter.__init__` (method) `readmenator/_sarif.py:30` `def __init__(self, privacy_mode)`
- `SarifExporter.export` (method) `readmenator/_sarif.py:33` `def export(self, findings, project_name)` -- Generate a SARIF v2.1.0 JSON string from security findings.

## readmenator/_scanner.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/parsers/__init__.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`, `tests/test_scanner.py`, `tests/test_taint_bdd.py`
- `PolyglotScanner.__init__` (method) `readmenator/_scanner.py:39` `def __init__(self, config)` -- Initialise the scanner with application configuration.
- `PolyglotScanner.scan` (method) `readmenator/_scanner.py:262` `def scan(self, root)` -- Walk *root* recursively and produce (nodes, edges) for the graph.
- `PolyglotScanner.scan_with_content` (method) `readmenator/_scanner.py:276` `def scan_with_content(self, root)` -- Scan and also return raw file contents for deeper analysis.

## readmenator/_scantext.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `ScanTextBuilder.__init__` (method) `readmenator/_scantext.py:19` `def __init__(self, config)` -- Initialise with application configuration.
- `ScanTextBuilder.build_for_node` (method) `readmenator/_scantext.py:27` `def build_for_node(self, node, content, imports)` -- Build the scan-text blob for a single file node.
- `ScanTextBuilder.build_corpus` (method) `readmenator/_scantext.py:67` `def build_corpus(self, nodes, content_map, edges)` -- Build scan-text blobs for every node in the corpus.

## readmenator/_security.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_agent_output.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_security.py`
- `SecurityAnalyzer.__init__` (method) `readmenator/_security.py:496` `def __init__(self, config)`
- `SecurityAnalyzer.scan` (method) `readmenator/_security.py:513` `def scan(self, root)`
- `SecurityAnalyzer.summary` (method) `readmenator/_security.py:572` `def summary(self, findings)`
- `fix_hint_for` (function) `readmenator/_security.py:620` `def fix_hint_for(finding)` -- Return a one-line remediation hint for a security finding.

## readmenator/_skill_installer.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_memory.py`
- `SkillInstaller.__init__` (method) `readmenator/_skill_installer.py:25` `def __init__(self, config)` -- Initialise with application configuration.
- `SkillInstaller.source_dir` (method) `readmenator/_skill_installer.py:34` `def source_dir()` -- Return the packaged skills directory.
- `SkillInstaller.available` (method) `readmenator/_skill_installer.py:38` `def available(self)` -- Return the names of the packaged skills, sorted.
- `SkillInstaller.target_dir` (method) `readmenator/_skill_installer.py:48` `def target_dir(self, project_root, target)` -- Resolve the destination skills directory.
- `SkillInstaller.install` (method) `readmenator/_skill_installer.py:61` `def install(self, project_root, target)` -- Write every packaged skill whose content changed.
- `SkillInstaller.maybe_install_on_run` (method) `readmenator/_skill_installer.py:87` `def maybe_install_on_run(self, project_root)` -- Install during run() only when the project already uses agent skills.

## readmenator/_sourceview.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_explorer.py`, `readmenator/_forcegraph.py`, `readmenator/_pipeline.py`, `tests/test_sourceview.py`
- `SourceViewBuilder.__init__` (method) `readmenator/_sourceview.py:39` `def __init__(self, config)` -- Initialise with application configuration.
- `SourceViewBuilder.enabled` (method) `readmenator/_sourceview.py:47` `def enabled(self)` -- Return True when sources may be embedded in the payload.
- `SourceViewBuilder.build_sources` (method) `readmenator/_sourceview.py:55` `def build_sources(self, nodes, content_map)` -- Build bounded source entries for every node in sorted order.
- `SourceViewBuilder.build_reasons` (method) `readmenator/_sourceview.py:70` `def build_reasons(self, nodes, content_map)` -- Explain every file left without embedded source.
- `SourceViewBuilder.to_payload` (method) `readmenator/_sourceview.py:149` `def to_payload(self, sources)` -- Serialise source entries to JSON-safe payload records.

## readmenator/_symindex.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/__init__.py`, `readmenator/_apidocs.py`, `readmenator/_components.py`, `readmenator/_flowcharts.py`, `readmenator/_linter.py`, `readmenator/_pipeline.py`, `tests/test_symindex.py`
- `SymbolIndex.__init__` (method) `readmenator/_symindex.py:135` `def __init__(self, config)` -- Initialise with application configuration.
- `SymbolIndex.build` (method) `readmenator/_symindex.py:144` `def build(self, nodes, content_map)` -- Index every symbol with its file span.
- `SymbolIndex.methods_index` (method) `readmenator/_symindex.py:184` `def methods_index(self, index)` -- Serialise definitions to component-diagram methods_index entries.
- `SymbolIndex.extract_call_sites` (method) `readmenator/_symindex.py:212` `def extract_call_sites(self, file_id, content, language, symbols)` -- Find call sites with line numbers in one file.
- `SymbolIndex.resolve` (method) `readmenator/_symindex.py:237` `def resolve(self, nodes, edges, resolved_edges, content_map)` -- Resolve every call to its best definition candidate.
- `_Visitor.visit_ClassDef` (method) `readmenator/_symindex.py:379` `def visit_ClassDef(self, node)` -- Visit a class body within its scope.
- `_Visitor.visit_FunctionDef` (method) `readmenator/_symindex.py:385` `def visit_FunctionDef(self, node)` -- Visit a function body within its scope.
- `_Visitor.visit_AsyncFunctionDef` (method) `readmenator/_symindex.py:391` `def visit_AsyncFunctionDef(self, node)` -- Visit an async function body within its scope.
- `_Visitor.visit_Call` (method) `readmenator/_symindex.py:397` `def visit_Call(self, node)` -- Record a call with its source location.

## readmenator/_taint.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`
- `TaintAnalyzer.__init__` (method) `readmenator/_taint.py:73` `def __init__(self, config)`
- `TaintAnalyzer.analyze` (method) `readmenator/_taint.py:77` `def analyze(self, nodes, edges, resolved_edges)` -- Run taint propagation analysis on the codebase.

## readmenator/_uml.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/__init__.py`, `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_uml.py`
- `UmlGenerator.__init__` (method) `readmenator/_uml.py:36` `def __init__(self, config)`
- `UmlGenerator.render_mermaid_class_diagram` (method) `readmenator/_uml.py:39` `def render_mermaid_class_diagram(self, nodes, edges)`
- `UmlGenerator.generate_code` (method) `readmenator/_uml.py:129` `def generate_code(self, nodes, edges, target_language)`

## readmenator/_vendor/force-graph.min.js
- `t` (function) `readmenator/_vendor/force-graph.min.js:2` -- Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `n` (function) `readmenator/_vendor/force-graph.min.js:2` -- Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `cr` (function) `readmenator/_vendor/force-graph.min.js:2` -- Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `y` (function) `readmenator/_vendor/force-graph.min.js:2` -- Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `Sr` (function) `readmenator/_vendor/force-graph.min.js:2` -- Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `e` (function) `readmenator/_vendor/force-graph.min.js:2` -- Version 1.52.0 force-graph - https://github.com/vasturiano/force-graph
- `e` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `h` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `s` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `l` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `Lo` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `b` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `h` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `u` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `f` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `i` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `Ha` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `o` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `e` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `n` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `n` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `xo` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `r` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `n` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `Ia` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `La` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `i` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...
- `s` (function) `readmenator/_vendor/force-graph.min.js:5` -- <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef (WCAG Version 2) Analyze the 2 colors and returns...

## readmenator/_video.py
Depends on: `readmenator/_config.py`, `readmenator/_graphlayout.py`, `readmenator/_models.py`, `readmenator/_rank.py`
Imported by: `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_video.py`
- `ease` (function) `readmenator/_video.py:96` `def ease(x)` -- Quintic smootherstep clamped to [0, 1].
- `fmt_int` (function) `readmenator/_video.py:107` `def fmt_int(n)` -- Group thousands with commas.
- `mix` (function) `readmenator/_video.py:112` `def mix(a, b, t)` -- Linear blend of two RGB colors.
- `alpha` (function) `readmenator/_video.py:117` `def alpha(c, a)` -- RGB color plus an alpha in [0, 1] as an RGBA tuple.
- `hash_color` (function) `readmenator/_video.py:122` `def hash_color(digest)` -- Neon color derived from a digest: the file fingerprint.
- `short_label` (function) `readmenator/_video.py:131` `def short_label(text, limit)` -- Truncate a label to a character budget without newlines.
- `community_color` (function) `readmenator/_video.py:176` `def community_color(index)` -- Neon color for a community index (grey for unassigned).
- `project3d` (function) `readmenator/_video.py:194` `def project3d(p, yaw, pitch, target, scale, center, perspective)` -- Project a 3D point through an orbiting perspective camera.
- `mode_color` (function) `readmenator/_video.py:233` `def mode_color(data, nid, mode)` -- Node color under an explorer color mode (community, layer, language).
- `draw_cloud3d` (function) `readmenator/_video.py:282` `def draw_cloud3d(img, data, box, cfg, yaw, pitch, target, zoom, mode, lit_nodes, edge_lit, gt, fonts, appear, labels)` -- Draw the 3D force graph (graph-force 3D view) through an orbiting camera.
- `draw_sphere3d` (function) `readmenator/_video.py:402` `def draw_sphere3d(img, data, box, cfg, yaw, pitch, morph, reveal, spot, gt, fonts, group_labels)` -- Draw the bundled sphere, optionally morphing out of the 3D force layout.
- `pr` (function) `readmenator/_video.py:469` `def pr(p)` -- Project a layout point through the scene camera.
- `dependencies_available` (function) `readmenator/_video.py:566` `def dependencies_available()` -- Check that PIL and ffmpeg exist for video rendering.
- `resolve_fonts` (function) `readmenator/_video.py:575` `def resolve_fonts()` -- Resolve monospace fonts through fontconfig with PIL fallback.
- `Backdrop.__init__` (method) `readmenator/_video.py:617` `def __init__(self, width, height)` -- Build the gradient sky, star field, sun and CRT mask.
- `draw_grid` (function) `readmenator/_video.py:677` `def draw_grid(img, t, strength, bd)` -- Draw the scrolling perspective grid below the horizon.
- `draw_sun` (function) `readmenator/_video.py:697` `def draw_sun(img, a, bd, cy)` -- Paste the striped synthwave sun behind the horizon.
- `post` (function) `readmenator/_video.py:714` `def post(img, glitch, seed)` -- Apply bloom, scanlines, vignette and optional glitch.
- `glitch_fx` (function) `readmenator/_video.py:732` `def glitch_fx(img, amount, seed)` -- RGB split plus horizontal slice displacement.
- `chroma_text` (function) `readmenator/_video.py:755` `def chroma_text(img, xy, text, font, col, spread, anchor)` -- Draw text with red/cyan CRT chromatic aberration.
- `hud_panel` (function) `readmenator/_video.py:766` `def hud_panel(d, box, title, fonts, col)` -- Draw a translucent HUD panel with neon edge and corner brackets.
- `draw_header` (function) `readmenator/_video.py:779` `def draw_header(img, d, gt, total, project, act_label, fonts, width)` -- Draw the top strip with project title, act label and progress.
- `draw_caption` (function) `readmenator/_video.py:793` `def draw_caption(d, text, lt, dur, fonts, width, y)` -- Draw the lower-third narration line with typing effect.
- `CinematicVideoRenderer.collect` (method) `readmenator/_video.py:814` `def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map...` -- Collect every number each scene draws, from real scan data.
- `CinematicVideoRenderer.build_scenes` (method) `readmenator/_video.py:1029` `def build_scenes(self, data)` -- Lay every scene on the global clock.
- `CinematicVideoRenderer.graph_positions` (method) `readmenator/_video.py:1058` `def graph_positions(self, data, box)` -- Compute deterministic positions for graph nodes inside a box.
- `CinematicVideoRenderer.tree_positions` (method) `readmenator/_video.py:1105` `def tree_positions(self, data, box)` -- Place the full BFS tree radially: root in the center, one ring per depth.
- `CinematicVideoRenderer.emergence_frames` (method) `readmenator/_video.py:1148` `def emergence_frames(self, data, box)` -- ForceAtlas2 snapshots of the resolved import graph fitted to a pixel box.
- `CinematicVideoRenderer.bundle_groups` (method) `readmenator/_video.py:1158` `def bundle_groups(self, data)` -- Group graph files by community (hubs first), unassigned files last.
- `CinematicVideoRenderer.ordered_groups` (method) `readmenator/_video.py:1173` `def ordered_groups(self, data)` -- Bundle groups reordered to shorten bundled edges (same optimizer as the explorer).
- `CinematicVideoRenderer.bundle_layout` (method) `readmenator/_video.py:1183` `def bundle_layout(self, data, box)` -- Hierarchical edge bundling of resolved imports grouped by community.
- `CinematicVideoRenderer.orbit_positions` (method) `readmenator/_video.py:1192` `def orbit_positions(self, data)` -- 3D ForceAtlas2 layout of the graph, centered and scaled to the unit sphere.
- `CinematicVideoRenderer.sphere_layout` (method) `readmenator/_video.py:1202` `def sphere_layout(self, data)` -- Spherical edge bundling of resolved imports on community caps.
- `CinematicVideoRenderer.orbit_stops` (method) `readmenator/_video.py:1211` `def orbit_stops(self, data, positions)` -- Camera tour stops: the largest communities with their 3D centroid.
- `CinematicVideoRenderer.render_single_frame` (method) `readmenator/_video.py:1240` `def render_single_frame(self, data, frame_index)` -- Render one frame to raw RGB bytes without touching ffmpeg.
- `CinematicVideoRenderer.render` (method) `readmenator/_video.py:1254` `def render(self, data, output_path)` -- Render all frames and encode to mp4, muxing music if configured.

## readmenator/_watcher.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_app.py`
- `DirectoryWatcher.__init__` (method) `readmenator/_watcher.py:29` `def __init__(self, root, config, callback, interval_seconds)` -- Initialise the watcher for a project root.
- `DirectoryWatcher.start` (method) `readmenator/_watcher.py:80` `def start(self)` -- Start watching the directory (blocking).
- `DirectoryWatcher.stop` (method) `readmenator/_watcher.py:97` `def stop(self)` -- Stop watching.

## readmenator/_wiki.py
Depends on: `readmenator/_analyzer.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_purpose.py`, `readmenator/_security.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_wiki.py`
- `existing_ids` (function) `readmenator/_wiki.py:62` `def existing_ids(connections)` -- Return community id pairs already linked, to avoid duplicate edges.
- `WikiGenerator.__init__` (method) `readmenator/_wiki.py:89` `def __init__(self, config)` -- Store configuration for wiki output limits and paths.
- `WikiGenerator.generate` (method) `readmenator/_wiki.py:94` `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_root)` -- Write all wiki files and return the output directory path.
- `WikiGenerator.lint` (method) `readmenator/_wiki.py:219` `def lint(self, project_root)` -- Check wiki health and return a list of issue descriptions.
- `dominant` (function) `readmenator/_wiki.py:428` `def dominant(ids, key)`

## readmenator/_yaralite.py
Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`
- `YaraLiteRule.tier` (method) `readmenator/_yaralite.py:42` `def tier(self)` -- Return the rule tier from meta or name prefix.
- `parse_yaralite_rules` (function) `readmenator/_yaralite.py:76` `def parse_yaralite_rules(rules_text)` -- Parse YARA-lite rules text into rules and error messages.
- `run_yaralite_rules` (function) `readmenator/_yaralite.py:112` `def run_yaralite_rules(text, rules)` -- Run parsed rules against a scan-text blob.
- `validate_yaralite_rules` (function) `readmenator/_yaralite.py:139` `def validate_yaralite_rules(rules_text)` -- Validate rules text and summarize tier counts.
- `replace_group` (function) `readmenator/_yaralite.py:270` `def replace_group(match)` -- Replace an N-of group with its boolean outcome.
- `replace_identifier` (function) `readmenator/_yaralite.py:292` `def replace_identifier(match)` -- Replace a string identifier with its hit boolean.

## readmenator/parsers/__init__.py
Depends on: `readmenator/_config.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
Imported by: `readmenator/_scanner.py`, `tests/test_parsers.py`, `tests/test_parsers_new.py`
- `create_parser` (function) `readmenator/parsers/__init__.py:70` `def create_parser(extension, filename, config)` -- Factory: return a parser instance for the given file extension.

## readmenator/parsers/_base.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/parsers/__init__.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`
- `LanguageParser.__init__` (method) `readmenator/parsers/_base.py:21` `def __init__(self, filename, config)` -- Initialise the parser with a file path and application config.
- `LanguageParser.parse` (method) `readmenator/parsers/_base.py:36` `def parse(self, content)` -- Parse *content* and populate symbol/import lists.

## readmenator_orchestrator.py
- `GitHubClient.__init__` (method) `readmenator_orchestrator.py:84` `def __init__(self, config)`
- `GitHubClient.list_repos` (method) `readmenator_orchestrator.py:124` `def list_repos(self)`
- `GitHubClient.close_existing_prs` (method) `readmenator_orchestrator.py:136` `def close_existing_prs(self, repo)`
- `GitHubClient.delete_remote_branch` (method) `readmenator_orchestrator.py:164` `def delete_remote_branch(self, repo)`
- `GitHubClient.create_pr` (method) `readmenator_orchestrator.py:176` `def create_pr(self, repo, default_branch, timestamp)`
- `RepositoryProcessor.__init__` (method) `readmenator_orchestrator.py:198` `def __init__(self, config, github_client)`
- `RepositoryProcessor.process` (method) `readmenator_orchestrator.py:202` `def process(self, repo)`
- `Orchestrator.__init__` (method) `readmenator_orchestrator.py:367` `def __init__(self, config)`
- `Orchestrator.run` (method) `readmenator_orchestrator.py:372` `def run(self, dry_run, only_repo)`
- `TestOrchestrator.setUp` (method) `readmenator_orchestrator.py:422` `def setUp(self)`
- `TestOrchestrator.tearDown` (method) `readmenator_orchestrator.py:426` `def tearDown(self)`
- `TestOrchestrator.test_config_immutability` (method) `readmenator_orchestrator.py:429` `def test_config_immutability(self)`
- `TestOrchestrator.test_config_defaults` (method) `readmenator_orchestrator.py:433` `def test_config_defaults(self)`
- `TestOrchestrator.test_rebuild_command_includes_full_concept_layer` (method) `readmenator_orchestrator.py:441` `def test_rebuild_command_includes_full_concept_layer(self)` -- The orchestrator must force a full rebuild with all improvements.
- `TestOrchestrator.test_pr_body_mentions_concept_layer` (method) `readmenator_orchestrator.py:452` `def test_pr_body_mentions_concept_layer(self)`
- `TestOrchestrator.test_skip_repos_logic` (method) `readmenator_orchestrator.py:458` `def test_skip_repos_logic(self)`
- `TestOrchestrator.test_repo_name_validation` (method) `readmenator_orchestrator.py:462` `def test_repo_name_validation(self)`
- `TestOrchestrator.test_branch_name_validation` (method) `readmenator_orchestrator.py:472` `def test_branch_name_validation(self)`
- `parse_arguments` (function) `readmenator_orchestrator.py:481` `def parse_arguments()`
- `main` (function) `readmenator_orchestrator.py:498` `def main()`

