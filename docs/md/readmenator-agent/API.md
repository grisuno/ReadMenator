# API (page 1 of 2)
Pages: [API.md](API.md), [API_p2.md](API_p2.md)

## readmenator/__main__.py
Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
Imported by: `readmenator.py`
- `build_parser` (function) `readmenator/__main__.py:18` `def build_parser()`
- `main` (function) `readmenator/__main__.py:141` `def main()`

## readmenator/_agent_injector.py
Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`
- `ensure_readmenator_installed` (function) `readmenator/_agent_injector.py:101` `def ensure_readmenator_installed()` -- Check if readmenator is installed via pip; install it if missing.
- `AgentInjector.__init__` (method) `readmenator/_agent_injector.py:134` `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)`
- `AgentInjector.inject` (method) `readmenator/_agent_injector.py:148` `def inject(self, project_root)` -- Inject KB reference into all discovered agent files.
- `AgentInjector.remove` (method) `readmenator/_agent_injector.py:166` `def remove(self, project_root)` -- Remove KB injection from all discovered agent files.
- `AgentInjector.find_agent_files` (method) `readmenator/_agent_injector.py:179` `def find_agent_files(self, project_root)` -- Public accessor: return all detected agent files.

## readmenator/_agent_output.py
Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_gitmeta.py`, `readmenator/_models.py`, `readmenator/_purpose.py`, `readmenator/_resolver.py`, `readmenator/_security.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`, `tests/test_agent_output.py`
- `AgentOutputGenerator.__init__` (method) `readmenator/_agent_output.py:77` `def __init__(self, config)` -- Store configuration for output paths and size budgets.
- `AgentOutputGenerator.generate` (method) `readmenator/_agent_output.py:81` `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` -- Write all agent output files and return the output directory path.
- `AgentOutputGenerator.keep` (method) `readmenator/_agent_output.py:523` `def keep(file_id)` -- Return whether a file belongs in the gotcha lists.

## readmenator/_analytics.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_documentation.py`, `readmenator/_explorer.py`, `readmenator/_exporter.py`, `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `AnalyticsBuilder.__init__` (method) `readmenator/_analytics.py:28` `def __init__(self, config)` -- Initialise with application configuration.
- `AnalyticsBuilder.build` (method) `readmenator/_analytics.py:36` `def build(self, nodes, edges, resolved_edges, analysis, findings, layers, v2, hotspots)` -- Build the full analytics payload.

## readmenator/_analyzer.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_agent_friendliness.py`, `tests/test_analyzer.py`
- `dominant_directory` (function) `readmenator/_analyzer.py:22` `def dominant_directory(file_ids)` -- Return the most informative directory label for a set of files.
- `GraphAnalyzer.__init__` (method) `readmenator/_analyzer.py:54` `def __init__(self, config)` -- Initialise with application configuration.
- `GraphAnalyzer.analyze` (method) `readmenator/_analyzer.py:62` `def analyze(self, nodes, edges, resolved_edges)` -- Run the full analysis pipeline and return structured results.

## readmenator/_app.py
Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_explorer.py`, `readmenator/_gh_wiki.py`, `readmenator/_gitmeta.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_video.py`, `readmenator/_watcher.py`, `readmenator/_yaralite.py`
Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_agent_friendliness.py`, `tests/test_diagrams.py`, `tests/test_gh_wiki.py`, `tests/test_integration.py`, `tests/test_interactive_graph.py`, `tests/test_mcp_server.py`, `tests/test_video.py`
- `readmenatorApplication.__init__` (method) `readmenator/_app.py:48` `def __init__(self, config)`
- `readmenatorApplication.run` (method) `readmenator/_app.py:94` `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- `readmenatorApplication.check_freshness` (method) `readmenator/_app.py:222` `def check_freshness(self, target_dir)` -- Compare the MANIFEST source fingerprint against the current sources.
- `readmenatorApplication.publish_github_wiki` (method) `readmenator/_app.py:285` `def publish_github_wiki(self, target_dir, dry_run)` -- Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `readmenatorApplication.generate_uml_code` (method) `readmenator/_app.py:341` `def generate_uml_code(self, target_dir, language, output_path)`
- `readmenatorApplication.update` (method) `readmenator/_app.py:408` `def update(self, target_dir, run_security)`
- `readmenatorApplication.query` (method) `readmenator/_app.py:531` `def query(self, target_dir, question)`
- `readmenatorApplication.explain` (method) `readmenator/_app.py:536` `def explain(self, target_dir, symbol_name)`
- `readmenatorApplication.find_path` (method) `readmenator/_app.py:548` `def find_path(self, target_dir, symbol_a, symbol_b)`
- `readmenatorApplication.summary` (method) `readmenator/_app.py:561` `def summary(self, target_dir)`
- `readmenatorApplication.rank_query` (method) `readmenator/_app.py:566` `def rank_query(self, target_dir, query, top_n)` -- Run a ranked query against the knowledge graph.
- `readmenatorApplication.rebuild` (method) `readmenator/_app.py:596` `def rebuild(self, target_dir, run_security)`
- `readmenatorApplication.analyze` (method) `readmenator/_app.py:599` `def analyze(self, target_dir)`
- `readmenatorApplication.export_json` (method) `readmenator/_app.py:603` `def export_json(self, target_dir, output_path)`
- `readmenatorApplication.export_html` (method) `readmenator/_app.py:620` `def export_html(self, target_dir, output_path)`
- `readmenatorApplication.export_svg` (method) `readmenator/_app.py:631` `def export_svg(self, target_dir, output_path)`
- `readmenatorApplication.export` (method) `readmenator/_app.py:642` `def export(self, target_dir)`
- `readmenatorApplication.export_forcegraph` (method) `readmenator/_app.py:698` `def export_forcegraph(self, target_dir, output_path)` -- Export the force-graph explorer HTML document.
- `readmenatorApplication.explorer_state` (method) `readmenator/_app.py:717` `def explorer_state(self, target_dir)` -- Build explorer state for the local HTTP server.
- `readmenatorApplication.serve_explorer` (method) `readmenator/_app.py:733` `def serve_explorer(self, target_dir, open_browser)` -- Serve the local explorer UI until interrupted.
- `readmenatorApplication.analytics` (method) `readmenator/_app.py:746` `def analytics(self, target_dir)` -- Compute the corpus analytics payload.
- `readmenatorApplication.scan_texts` (method) `readmenator/_app.py:763` `def scan_texts(self, target_dir)` -- Build scan-text blobs for every file in the project.
- `readmenatorApplication.near` (method) `readmenator/_app.py:775` `def near(self, target_dir, query, top_k)` -- Find semantically similar files for a query file or text.
- `readmenatorApplication.audit_provenance` (method) `readmenator/_app.py:789` `def audit_provenance(self, target_dir)` -- Audit security findings by evidence provenance.
- `readmenatorApplication.validate_yaralite` (method) `readmenator/_app.py:813` `def validate_yaralite(self, target_dir)` -- Validate the project YARA-lite rules file.
- `readmenatorApplication.export_graphml` (method) `readmenator/_app.py:827` `def export_graphml(self, target_dir, output_path)`
- `readmenatorApplication.export_cypher` (method) `readmenator/_app.py:838` `def export_cypher(self, target_dir, output_path)`
- `readmenatorApplication.export_obsidian` (method) `readmenator/_app.py:854` `def export_obsidian(self, target_dir, output_dir)`
- `readmenatorApplication.export_wiki` (method) `readmenator/_app.py:869` `def export_wiki(self, target_dir, output_dir)` -- Generate the navigable agent wiki for the target project.
- `readmenatorApplication.lint_wiki` (method) `readmenator/_app.py:892` `def lint_wiki(self, target_dir)` -- Check wiki health and log reported issues.
- `readmenatorApplication.export_diagrams` (method) `readmenator/_app.py:910` `def export_diagrams(self, target_dir, output_dir, full)` -- Export all five interactive system maps plus a gallery index.
- `readmenatorApplication.export_diagram` (method) `readmenator/_app.py:985` `def export_diagram(self, target_dir, kind, output_path, full)` -- Export a single interactive system map as standalone HTML.
- `readmenatorApplication.export_pages` (method) `readmenator/_app.py:1024` `def export_pages(self, target_dir, output_dir, full)` -- Publish all system maps plus a gallery index as a static site.
- `readmenatorApplication.export_video` (method) `readmenator/_app.py:1059` `def export_video(self, target_dir, output_path)` -- Render the cinematic overview video for the target project.
- `readmenatorApplication.watch` (method) `readmenator/_app.py:1153` `def watch(self, target_dir)`
- `readmenatorApplication.on_change` (method) `readmenator/_app.py:1157` `def on_change()`
- `readmenatorApplication.audit` (method) `readmenator/_app.py:1163` `def audit(self, target_dir)`
- `readmenatorApplication.audit_deep` (method) `readmenator/_app.py:1170` `def audit_deep(self, target_dir)`
- `readmenatorApplication.export_sarif` (method) `readmenator/_app.py:1190` `def export_sarif(self, target_dir, output_path)`
- `readmenatorApplication.export_rules` (method) `readmenator/_app.py:1200` `def export_rules(self, target_dir, output_dir)`
- `readmenatorApplication.detect_layers` (method) `readmenator/_app.py:1210` `def detect_layers(self, target_dir)`
- `readmenatorApplication.lint` (method) `readmenator/_app.py:1220` `def lint(self, target_dir)`
- `readmenatorApplication.strip_dead_code` (method) `readmenator/_app.py:1233` `def strip_dead_code(self, target_dir)`
- `readmenatorApplication.generate_cursorrules` (method) `readmenator/_app.py:1243` `def generate_cursorrules(self, target_dir)`
- `readmenatorApplication.refactor_monolith` (method) `readmenator/_app.py:1258` `def refactor_monolith(self, target_dir)`

## readmenator/_cache.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `tests/test_agent_friendliness.py`, `tests/test_cache.py`
- `FileCache.__init__` (method) `readmenator/_cache.py:31` `def __init__(self, config, project_root)`
- `FileCache.load` (method) `readmenator/_cache.py:38` `def load(self)`
- `FileCache.save` (method) `readmenator/_cache.py:49` `def save(self, hashes)`
- `FileCache.compute_hash` (method) `readmenator/_cache.py:55` `def compute_hash(self, file_path)`
- `FileCache.compute_hashes` (method) `readmenator/_cache.py:64` `def compute_hashes(self, file_paths)`
- `FileCache.find_changed` (method) `readmenator/_cache.py:72` `def find_changed(self, file_paths)`
- `FileCache.prune_deleted` (method) `readmenator/_cache.py:84` `def prune_deleted(self, current_file_ids)`
- `FileCache.save_analysis` (method) `readmenator/_cache.py:95` `def save_analysis(self, key, data)` -- Save an analysis result to the semantic cache.
- `FileCache.load_analysis` (method) `readmenator/_cache.py:118` `def load_analysis(self, key)` -- Load a previously cached analysis result.
- `FileCache.clear_analysis` (method) `readmenator/_cache.py:135` `def clear_analysis(self, key)` -- Clear analysis cache, optionally for a specific key only.
- `FileCache.has_changed_since_last_analysis` (method) `readmenator/_cache.py:166` `def has_changed_since_last_analysis(self, file_paths)` -- Check if any file has changed since the last analysis cache.
- `FileCache.source_fingerprint` (method) `readmenator/_cache.py:179` `def source_fingerprint(project_root, file_ids)` -- Return one SHA256 over the sorted paths and contents of scanned sources.

## readmenator/_category.py
Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`
- `Morphism.weight` (method) `readmenator/_category.py:73` `def weight(self)` -- Effective weight for ranking = semantic weight * confidence.
- `Category.__init__` (method) `readmenator/_category.py:86` `def __init__(self)`
- `Category.add_object` (method) `readmenator/_category.py:92` `def add_object(self, obj_id)`
- `Category.add_morphism` (method) `readmenator/_category.py:95` `def add_morphism(self, m)`
- `Category.objects` (method) `readmenator/_category.py:103` `def objects(self)`
- `Category.morphisms` (method) `readmenator/_category.py:107` `def morphisms(self)`
- `Category.outgoing` (method) `readmenator/_category.py:110` `def outgoing(self, obj_id)`
- `Category.incoming` (method) `readmenator/_category.py:113` `def incoming(self, obj_id)`
- `Category.compose` (method) `readmenator/_category.py:116` `def compose(self, a, b)` -- Compose two morphisms if target of a matches source of b.
- `Category.paths` (method) `readmenator/_category.py:133` `def paths(self, source, target, max_depth)` -- Find all composition paths from source to target up to max_depth.
- `Category.dfs` (method) `readmenator/_category.py:139` `def dfs(current, goal, path, depth)`
- `TypedGraph.__init__` (method) `readmenator/_category.py:188` `def __init__(self, category)`
- `TypedGraph.nodes` (method) `readmenator/_category.py:203` `def nodes(self)`
- `TypedGraph.size` (method) `readmenator/_category.py:207` `def size(self)`
- `TypedGraph.node_index` (method) `readmenator/_category.py:210` `def node_index(self, node_id)`
- `TypedGraph.transition_weight` (method) `readmenator/_category.py:213` `def transition_weight(self, source, target)` -- Sum of weights of all morphisms from source to target.
- `TypedGraph.stochastic_row` (method) `readmenator/_category.py:221` `def stochastic_row(self, source)` -- Return dict of target -> probability for the row of *source*.
- `TypedGraph.build_category_from_edges` (method) `readmenator/_category.py:236` `def build_category_from_edges(edges, resolved_edges, node_ids)` -- Build a Category from lists of Edge objects.

## readmenator/_concepts.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_concepts.py`
- `verb_for_relation` (function) `readmenator/_concepts.py:33` `def verb_for_relation(relation)` -- Return the verb label for a structural edge relation.
- `ConceptExtractor.__init__` (method) `readmenator/_concepts.py:41` `def __init__(self, config)` -- Store configuration for concept extraction budgets.
- `ConceptExtractor.extract` (method) `readmenator/_concepts.py:47` `def extract(self, nodes, edges, resolved_edges)` -- Build concepts and verb relations from structural topology.

## readmenator/_cpg.py
Depends on: `readmenator/_models.py`
Imported by: `readmenator/_documentation.py`, `readmenator/_pipeline.py`, `tests/test_cpg.py`
- `CodePropertyGraph.__init__` (method) `readmenator/_cpg.py:26` `def __init__(self, privacy_mode, cpg_context)`
- `CodePropertyGraph.generate` (method) `readmenator/_cpg.py:30` `def generate(self, nodes, edges, resolved_edges, analysis, findings)` -- Generate the CPG JSON-LD string embeddable in markdown.

## readmenator/_cursorrules_generator.py
Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `tests/test_cursorrules.py`
- `CursorRulesGenerator.__init__` (method) `readmenator/_cursorrules_generator.py:25` `def __init__(self, config)`
- `CursorRulesGenerator.generate` (method) `readmenator/_cursorrules_generator.py:28` `def generate(self, nodes, edges, analysis, layers, violations, project_root)` -- Generate the .cursorrules content string.

## readmenator/_dataflow.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_dataflow.py`
- `DataflowAnalyzer.__init__` (method) `readmenator/_dataflow.py:125` `def __init__(self, config)` -- Store configuration for enable flag and issue caps.
- `DataflowAnalyzer.analyze` (method) `readmenator/_dataflow.py:129` `def analyze(self, nodes, content_map)` -- Check every function body span and return capped issues.

## readmenator/_dead_code.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `tests/test_dead_code.py`
- `DeadCodeStripper.__init__` (method) `readmenator/_dead_code.py:25` `def __init__(self, config)`
- `DeadCodeStripper.identify` (method) `readmenator/_dead_code.py:28` `def identify(self, nodes, edges, resolved_edges)` -- Identify dead code symbols with zero in-degree.

## readmenator/_diagrams.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`, `tests/test_diagrams.py`, `tests/test_interactive_graph.py`
- `SystemMapValidator.__init__` (method) `readmenator/_diagrams.py:214` `def __init__(self, config)` -- Initialise the validator with application configuration.
- `SystemMapValidator.validate` (method) `readmenator/_diagrams.py:243` `def validate(self, system_map)` -- Validate a system map and return a deterministic receipt.
- `SystemMapBuilder.__init__` (method) `readmenator/_diagrams.py:464` `def __init__(self, config)` -- Initialise the builder with application configuration.
- `SystemMapBuilder.supported_kinds` (method) `readmenator/_diagrams.py:473` `def supported_kinds(self)` -- Return the supported diagram kind identifiers.
- `SystemMapBuilder.build` (method) `readmenator/_diagrams.py:494` `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)` -- Build one deterministic system map of the requested kind.
- `SystemMapBuilder.build_all` (method) `readmenator/_diagrams.py:553` `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)` -- Build all five diagram kinds deterministically.
- `SystemMapBuilder.compare` (method) `readmenator/_diagrams.py:584` `def compare(self, base, head)` -- Compare two maps of the same kind as before, delta, and after.
- `InteractiveMapRenderer.__init__` (method) `readmenator/_diagrams.py:1504` `def __init__(self, config)` -- Initialise the renderer with application configuration.
- `InteractiveMapRenderer.render` (method) `readmenator/_diagrams.py:1533` `def render(self, system_map)` -- Render a system map as a self-contained HTML document.
- `InteractiveMapRenderer.write` (method) `readmenator/_diagrams.py:1635` `def write(self, system_map, output_path)` -- Render a system map and write it to a relative output path.
- `VisNetworkRenderer.__init__` (method) `readmenator/_diagrams.py:2224` `def __init__(self, config)` -- Initialise the renderer with application configuration.
- `VisNetworkRenderer.render` (method) `readmenator/_diagrams.py:2232` `def render(self, system_map)` -- Render a system map as a vis.js network HTML document.
- `VisNetworkRenderer.write` (method) `readmenator/_diagrams.py:2360` `def write(self, system_map, output_path)` -- Render a vis.js map and write it to a relative output path.
- `DocsSitePublisher.__init__` (method) `readmenator/_diagrams.py:3009` `def __init__(self, config)` -- Initialise the publisher with application configuration.
- `DocsSitePublisher.description_for` (method) `readmenator/_diagrams.py:3019` `def description_for(self, kind)` -- Return the gallery description for a diagram kind.
- `DocsSitePublisher.publish` (method) `readmenator/_diagrams.py:3033` `def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries, extra_cards)` -- Publish maps and a gallery index into a documentation directory.
- `DocsSitePublisher.collect_doc_sources` (method) `readmenator/_diagrams.py:3127` `def collect_doc_sources(self, project_root)` -- Collect generated markdown sources for the static site.
- `DocsSitePublisher.publish_assets` (method) `readmenator/_diagrams.py:3153` `def publish_assets(self, project_root, output_dir)` -- Copy overview video and markdown docs into the static site.
- `DocsSitePublisher.render_llms_txt` (method) `readmenator/_diagrams.py:3322` `def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)` -- Render an llms.txt entry point so agents can navigate the site as text.
- `DocsSitePublisher.order` (method) `readmenator/_diagrams.py:3370` `def order(entry)` -- Sort entry points first, then alphabetically.
- `DocsSitePublisher.render_index` (method) `readmenator/_diagrams.py:3398` `def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries, poster_rel, extra_cards)` -- Render the gallery index page for published maps.
- `DocsSitePublisher.doc_order` (method) `readmenator/_diagrams.py:3593` `def doc_order(base)` -- Entry points first, then alphabetical.

## readmenator/_documentation.py
Depends on: `readmenator/_analytics.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_forcegraph.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`
- `DocumentationGenerator.__init__` (method) `readmenator/_documentation.py:47` `def __init__(self, config)`
- `DocumentationGenerator.generate` (method) `readmenator/_documentation.py:93` `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked)`

## readmenator/_embed.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `Embedder.__init__` (method) `readmenator/_embed.py:42` `def __init__(self, config)` -- Initialise with application configuration.
- `Embedder.dependencies_available` (method) `readmenator/_embed.py:50` `def dependencies_available(self)` -- Return True when sentence-transformers is importable.
- `Embedder.encode` (method) `readmenator/_embed.py:58` `def encode(self, texts)` -- Encode texts into L2-normalized vectors when available.
- `Embedder.near_jaccard` (method) `readmenator/_embed.py:75` `def near_jaccard(self, query, corpus, top_k)` -- Find nearest neighbors with offline Jaccard similarity.
- `Embedder.cluster_jaccard` (method) `readmenator/_embed.py:99` `def cluster_jaccard(self, corpus, threshold)` -- Group files into similarity clusters with union-find.
- `Embedder.find` (method) `readmenator/_embed.py:115` `def find(item)` -- Find the union-find root for an item.
- `Embedder.union` (method) `readmenator/_embed.py:122` `def union(left, right)` -- Merge two union-find sets.
- `Embedder.project_jaccard` (method) `readmenator/_embed.py:138` `def project_jaccard(self, corpus)` -- Project files to 2D with a deterministic radial layout.

## readmenator/_exclusions.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `ExclusionEntry.matches` (method) `readmenator/_exclusions.py:27` `def matches(self, file_path, rule_id)` -- Return True when this entry suppresses the finding.
- `ExclusionList.__init__` (method) `readmenator/_exclusions.py:47` `def __init__(self, config)` -- Initialise with application configuration.
- `ExclusionList.entries` (method) `readmenator/_exclusions.py:58` `def entries(self)` -- Return the loaded exclusion entries.
- `ExclusionList.load` (method) `readmenator/_exclusions.py:62` `def load(self, project_root)` -- Load exclusions from the project blocklist file.
- `ExclusionList.is_excluded` (method) `readmenator/_exclusions.py:86` `def is_excluded(self, file_path, rule_id)` -- Return True when a finding is suppressed by the blocklist.
- `ExclusionList.filter_findings` (method) `readmenator/_exclusions.py:98` `def filter_findings(self, findings)` -- Remove excluded findings from a finding list.
- `ExclusionList.parse_exclusions` (method) `readmenator/_exclusions.py:114` `def parse_exclusions(text)` -- Parse the minimal exclusions YAML into entries.

## readmenator/_explain.py
Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
Imported by: `tests/test_ranking.py`
- `explain_rank` (function) `readmenator/_explain.py:16` `def explain_rank(node_id, ranked, category)` -- Return a detailed breakdown of why *node_id* has its rank.
- `rank_summary` (function) `readmenator/_explain.py:140` `def rank_summary(ranked, top_n)` -- Return a short summary of the top-N ranked results.

## readmenator/_explorer.py
Depends on: `readmenator/_analytics.py`, `readmenator/_config.py`, `readmenator/_forcegraph.py`, `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`
- `ExplorerState.__init__` (method) `readmenator/_explorer.py:26` `def __init__(self, config, nodes, edges, resolved_edges, analysis, findings, layers)` -- Initialise explorer state and precompute payloads.
- `ExplorerState.samples` (method) `readmenator/_explorer.py:61` `def samples(self)` -- Return a compact per-file sample listing.
- `_Handler.log_message` (method) `readmenator/_explorer.py:84` `def log_message(self, fmt)` -- Silence the default access log.
- `_Handler.do_GET` (method) `readmenator/_explorer.py:88` `def do_GET(self)` -- Dispatch GET routes for HTML and JSON APIs.
- `_Handler.find_free_port` (method) `readmenator/_explorer.py:139` `def find_free_port(preferred)` -- Find a free TCP port, preferring the configured value.
- `_Handler.serve` (method) `readmenator/_explorer.py:158` `def serve(state, host, port, open_browser)` -- Serve the explorer state until interrupted.
- `_Handler.build_state` (method) `readmenator/_explorer.py:191` `def build_state(config, nodes, edges, resolved_edges, analysis, findings, layers)` -- Build explorer state without starting the server.
- `_Handler.write_static` (method) `readmenator/_explorer.py:217` `def write_static(state, output_dir, filename)` -- Write the explorer HTML to a static file.

## readmenator/_exporter.py
Depends on: `readmenator/_analytics.py`, `readmenator/_config.py`, `readmenator/_forcegraph.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`, `tests/test_interactive_graph.py`
- `GraphExporter.__init__` (method) `readmenator/_exporter.py:36` `def __init__(self, config)` -- Initialise with application configuration.
- `GraphExporter.to_json` (method) `readmenator/_exporter.py:44` `def to_json(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` -- Export the graph as a node-link JSON string.
- `GraphExporter.to_html` (method) `readmenator/_exporter.py:183` `def to_html(self, nodes, edges, resolved_edges, analysis, findings)` -- Generate a standalone interactive HTML graph page.
- `GraphExporter.to_svg` (method) `readmenator/_exporter.py:469` `def to_svg(self, nodes, edges, resolved_edges, analysis)` -- Generate a static SVG representation of the graph.
- `GraphExporter.to_graphml` (method) `readmenator/_exporter.py:683` `def to_graphml(self, nodes, edges, resolved_edges, analysis)` -- Export the graph as GraphML (Gephi/yEd compatible).
- `GraphExporter.to_cypher` (method) `readmenator/_exporter.py:760` `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` -- Export the graph as native Cypher CREATE statements.
- `GraphExporter.to_obsidian` (method) `readmenator/_exporter.py:882` `def to_obsidian(self, nodes, edges, output_dir, analysis, concept_graph)` -- Export the graph as an Obsidian vault with wikilinks.
- `GraphExporter.to_forcegraph` (method) `readmenator/_exporter.py:1007` `def to_forcegraph(self, nodes, edges, resolved_edges, analysis, layers, findings, analytics)` -- Generate the force-graph explorer HTML document.

## readmenator/_forcegraph.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_documentation.py`, `readmenator/_explorer.py`, `readmenator/_exporter.py`, `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `family_color_from_name` (function) `readmenator/_forcegraph.py:24` `def family_color_from_name(name, sat_base, sat_span, light_base, light_span)` -- Derive a stable, visually-distinct HSL color from a label.
- `node_value` (function) `readmenator/_forcegraph.py:52` `def node_value(symbols, degree)` -- Scale a node value with log2 dampening.
- `ForceGraphRenderer.__init__` (method) `readmenator/_forcegraph.py:68` `def __init__(self, config)` -- Initialise with application configuration.
- `ForceGraphRenderer.node_palette` (method) `readmenator/_forcegraph.py:76` `def node_palette(self)` -- Return the node-type color palette from configuration.
- `ForceGraphRenderer.edge_palette` (method) `readmenator/_forcegraph.py:80` `def edge_palette(self)` -- Return the edge-relation color palette from configuration.
- `ForceGraphRenderer.vendor_source` (method) `readmenator/_forcegraph.py:84` `def vendor_source(self)` -- Return the path of the vendored 2D engine shipped in the package.
- `ForceGraphRenderer.vendor_href` (method) `readmenator/_forcegraph.py:92` `def vendor_href(self)` -- Return the relative vendor script href used beside the page.
- `ForceGraphRenderer.build_payload` (method) `readmenator/_forcegraph.py:97` `def build_payload(self, nodes, edges, resolved_edges, analysis, layers, findings)` -- Build a heterogeneous graph payload for the explorer.
- `ForceGraphRenderer.file_of` (method) `readmenator/_forcegraph.py:131` `def file_of(edge_id)` -- Map a symbol-scoped edge endpoint to its file identifier.
- `ForceGraphRenderer.add_node` (method) `readmenator/_forcegraph.py:173` `def add_node(node_id, label, node_type)` -- Insert a node unless already present.
- `ForceGraphRenderer.render` (method) `readmenator/_forcegraph.py:255` `def render(self, payload, analytics, title, home_href)` -- Render the standalone force-graph explorer HTML document.
- `ForceGraphRenderer.write` (method) `readmenator/_forcegraph.py:315` `def write(self, output_path, payload, analytics, title)` -- Write the explorer HTML plus the vendored engine beside it.
- `ForceGraphRenderer.copy_vendor` (method) `readmenator/_forcegraph.py:340` `def copy_vendor(self, dest_dir)` -- Copy the vendored 2D engine next to an exported page.

## readmenator/_gh_wiki.py
Depends on: `readmenator/_config.py`, `readmenator/_gitmeta.py`
Imported by: `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_gh_wiki.py`
- `GitHubWikiPublisher.__init__` (method) `readmenator/_gh_wiki.py:62` `def __init__(self, config, runner)` -- Store configuration and the subprocess runner (injectable for tests).
- `GitHubWikiPublisher.page_name` (method) `readmenator/_gh_wiki.py:72` `def page_name(self, rel_path)` -- Map a generated markdown path to its flat GitHub wiki page name.
- `GitHubWikiPublisher.collect_sources` (method) `readmenator/_gh_wiki.py:96` `def collect_sources(self, project_root)` -- List project-relative markdown sources to publish, sorted.
- `GitHubWikiPublisher.rewrite` (method) `readmenator/_gh_wiki.py:129` `def rewrite(self, text, rel_path, names, project_root, blob_base)` -- Rewrite relative doc links to wiki pages and paths to source permalinks.
- `GitHubWikiPublisher.link` (method) `readmenator/_gh_wiki.py:151` `def link(match)` -- Replace one relative markdown link when its target is published.
- `GitHubWikiPublisher.permalink` (method) `readmenator/_gh_wiki.py:164` `def permalink(match)` -- Link a backticked project file (optionally with a line) to source.
- `GitHubWikiPublisher.render` (method) `readmenator/_gh_wiki.py:179` `def render(self, project_root, remote)` -- Render every wiki page, including sidebar and footer.
- `GitHubWikiPublisher.wiki_remote` (method) `readmenator/_gh_wiki.py:249` `def wiki_remote(self, project_root)` -- Resolve the wiki remote from config, ``gh``, or the git origin.
- `GitHubWikiPublisher.publish` (method) `readmenator/_gh_wiki.py:313` `def publish(self, project_root, dry_run)` -- Render pages and push them to the GitHub wiki (or a local folder).

## readmenator/_gitmeta.py
Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `readmenator/_gh_wiki.py`, `tests/test_agent_friendliness.py`
- `read_git_head` (function) `readmenator/_gitmeta.py:84` `def read_git_head(project_root)` -- Return the current commit and branch of a project, when available.

## readmenator/_hotspots.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_hotspots.py`
- `HotspotAnalyzer.__init__` (method) `readmenator/_hotspots.py:31` `def __init__(self, config)`
- `HotspotAnalyzer.analyze_hotspots` (method) `readmenator/_hotspots.py:34` `def analyze_hotspots(self, nodes, edges, resolved_edges)` -- Rank files by combined complexity and centrality scores.
- `HotspotAnalyzer.detect_cycles` (method) `readmenator/_hotspots.py:90` `def detect_cycles(self, nodes, resolved_edges)` -- Detect cycles in the resolved import graph using DFS.
- `HotspotAnalyzer.analyze_change_impact` (method) `readmenator/_hotspots.py:155` `def analyze_change_impact(self, nodes, resolved_edges)` -- Compute change impact for every file in the project.

## readmenator/_layer_rules.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_layer_rules.py`
- `LayerRuleEngine.__init__` (method) `readmenator/_layer_rules.py:36` `def __init__(self, config)`
- `LayerRuleEngine.detect_violations` (method) `readmenator/_layer_rules.py:39` `def detect_violations(self, nodes, edges, resolved_edges, layers)` -- Detect architectural layer violations.
- `LayerRuleEngine.violation_summary` (method) `readmenator/_layer_rules.py:111` `def violation_summary(violations)` -- Summarise violations by severity.

## readmenator/_layers.py
Depends on: `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`
- `LayerDetector.detect` (method) `readmenator/_layers.py:83` `def detect(self, nodes, edges)` -- Assign each file node to an architectural layer.
- `LayerDetector.layer_summary` (method) `readmenator/_layers.py:189` `def layer_summary(layers)` -- Count files per layer.

## readmenator/_linter.py
Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `tests/test_linter.py`
- `ArchitectureLinter.__init__` (method) `readmenator/_linter.py:31` `def __init__(self, config)`
- `ArchitectureLinter.lint` (method) `readmenator/_linter.py:34` `def lint(self, nodes, edges, resolved_edges, layers, content_map)` -- Run all linter rules and return violations.

## readmenator/_mcp_server.py
Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_query.py`
Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `tests/test_mcp_server.py`
- `MCPError.__init__` (method) `readmenator/_mcp_server.py:59` `def __init__(self, code, message, data)`
- `MCPRequest.__init__` (method) `readmenator/_mcp_server.py:72` `def __init__(self, msg)`
- `MCPRequest.is_notification` (method) `readmenator/_mcp_server.py:79` `def is_notification(self)`
- `MCPRequest.response` (method) `readmenator/_mcp_server.py:82` `def response(self, result)`
- `MCPRequest.error` (method) `readmenator/_mcp_server.py:85` `def error(self, code, message, data)`
- `MCPTool.__init__` (method) `readmenator/_mcp_server.py:93` `def __init__(self, name, description, handler, input_schema)`
- `MCPTool.definition` (method) `readmenator/_mcp_server.py:108` `def definition(self)`
- `MCPTool.call` (method) `readmenator/_mcp_server.py:115` `def call(self, arguments)`
- `MCPResource.__init__` (method) `readmenator/_mcp_server.py:120` `def __init__(self, uri, name, description, mime_type, handler)`
- `MCPResource.definition` (method) `readmenator/_mcp_server.py:134` `def definition(self)`
- `MCPResource.read` (method) `readmenator/_mcp_server.py:142` `def read(self)`
- `MCPServer.__init__` (method) `readmenator/_mcp_server.py:147` `def __init__(self, app, target_dir)`
- `MCPServer.register_tool` (method) `readmenator/_mcp_server.py:155` `def register_tool(self, tool)`
- `MCPServer.register_resource` (method) `readmenator/_mcp_server.py:158` `def register_resource(self, resource)`
- `MCPServer.dispatch` (method) `readmenator/_mcp_server.py:241` `def dispatch(self, req)`
- `MCPServer.run` (method) `readmenator/_mcp_server.py:261` `def run(self)`
- `MCPServer.main` (method) `readmenator/_mcp_server.py:990` `def main()` -- CLI entry point for `readmenator serve <path>`.

## readmenator/_mermaid.py
Depends on: `readmenator/_models.py`
Imported by: `readmenator/_documentation.py`, `tests/test_mermaid.py`
- `MermaidRenderer.__init__` (method) `readmenator/_mermaid.py:26` `def __init__(self, max_nodes, max_symbols_per_file, module_style, class_style, function_style, external_style...`
- `MermaidRenderer.render` (method) `readmenator/_mermaid.py:56` `def render(self, nodes, edges, resolved_edges, analysis)` -- Produce a Mermaid flowchart string and a truncation flag.

## readmenator/_models.py
Depends on: `readmenator/_category.py`
Imported by: `readmenator/__init__.py`, `readmenator/_agent_output.py`, `readmenator/_analytics.py`, `readmenator/_analyzer.py`, `readmenator/_app.py`, `readmenator/_concepts.py`, `readmenator/_cpg.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dataflow.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_explorer.py`, `readmenator/_exporter.py`, `readmenator/_forcegraph.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_mermaid.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_provenance.py`, `readmenator/_purpose.py`, `readmenator/_query.py`, `readmenator/_refactorizer.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_scantext.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_video.py`, `readmenator/_wiki.py`, `readmenator/parsers/_assembly.py`, `readmenator/parsers/_base.py`, `readmenator/parsers/_c.py`, `readmenator/parsers/_csharp.py`, `readmenator/parsers/_dart.py`, `readmenator/parsers/_elixir.py`, `readmenator/parsers/_gdscript.py`, `readmenator/parsers/_go.py`, `readmenator/parsers/_java.py`, `readmenator/parsers/_javascript.py`, `readmenator/parsers/_kotlin.py`, `readmenator/parsers/_lua.py`, `readmenator/parsers/_nim.py`, `readmenator/parsers/_php.py`, `readmenator/parsers/_python.py`, `readmenator/parsers/_ruby.py`, `readmenator/parsers/_rust.py`, `readmenator/parsers/_scala.py`, `readmenator/parsers/_shell.py`, `readmenator/parsers/_swift.py`, `tests/test_agent_friendliness.py`, `tests/test_agent_output.py`, `tests/test_analyzer.py`, `tests/test_concepts.py`, `tests/test_cpg.py`, `tests/test_cursorrules.py`, `tests/test_dataflow.py`, `tests/test_dead_code.py`, `tests/test_diagrams.py`, `tests/test_documentation.py`, `tests/test_exporter.py`, `tests/test_hotspots.py`, `tests/test_interactive_graph.py`, `tests/test_layer_rules.py`, `tests/test_linter.py`, `tests/test_mermaid.py`, `tests/test_models.py`, `tests/test_parsers_property.py`, `tests/test_query.py`, `tests/test_ranking.py`, `tests/test_refactorizer.py`, `tests/test_rule_gen.py`, `tests/test_sarif.py`, `tests/test_scanner.py`, `tests/test_security.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`, `tests/test_uml.py`, `tests/test_video.py`, `tests/test_wiki.py`
- `SecurityFinding.pluralize_symbol_kind` (method) `readmenator/_models.py:101` `def pluralize_symbol_kind(kind, plural_map)` -- Return the plural form of *kind* according to *plural_map*.

## readmenator/_pipeline.py
Depends on: `readmenator/_agent_injector.py`, `readmenator/_agent_output.py`, `readmenator/_analytics.py`, `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_concepts.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_dataflow.py`, `readmenator/_diagrams.py`, `readmenator/_documentation.py`, `readmenator/_embed.py`, `readmenator/_exclusions.py`, `readmenator/_exporter.py`, `readmenator/_forcegraph.py`, `readmenator/_gh_wiki.py`, `readmenator/_hotspots.py`, `readmenator/_layer_rules.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_provenance.py`, `readmenator/_rank.py`, `readmenator/_readme_injector.py`, `readmenator/_rule_gen.py`, `readmenator/_sarif.py`, `readmenator/_scanner.py`, `readmenator/_scantext.py`, `readmenator/_security.py`, `readmenator/_taint.py`, `readmenator/_uml.py`, `readmenator/_video.py`, `readmenator/_wiki.py`
Imported by: `readmenator/_app.py`
- `AnalyzerFactory.__init__` (method) `readmenator/_pipeline.py:64` `def __init__(self, config)`
- `AnalyzerFactory.scanner` (method) `readmenator/_pipeline.py:102` `def scanner(self)`
- `AnalyzerFactory.generator` (method) `readmenator/_pipeline.py:108` `def generator(self)`
- `AnalyzerFactory.analyzer` (method) `readmenator/_pipeline.py:114` `def analyzer(self)`
- `AnalyzerFactory.security` (method) `readmenator/_pipeline.py:120` `def security(self)`
- `AnalyzerFactory.exporter` (method) `readmenator/_pipeline.py:126` `def exporter(self)`
- `AnalyzerFactory.taint` (method) `readmenator/_pipeline.py:132` `def taint(self)`
- `AnalyzerFactory.dataflow` (method) `readmenator/_pipeline.py:138` `def dataflow(self)` -- Return the lazily initialised dataflow analyzer.
- `AnalyzerFactory.hotspots` (method) `readmenator/_pipeline.py:145` `def hotspots(self)`
- `AnalyzerFactory.layer_rules` (method) `readmenator/_pipeline.py:151` `def layer_rules(self)`
- `AnalyzerFactory.rule_gen` (method) `readmenator/_pipeline.py:157` `def rule_gen(self)`
- `AnalyzerFactory.sarif` (method) `readmenator/_pipeline.py:163` `def sarif(self)`
- `AnalyzerFactory.cpg` (method) `readmenator/_pipeline.py:169` `def cpg(self)`
- `AnalyzerFactory.layer_detector` (method) `readmenator/_pipeline.py:178` `def layer_detector(self)`
- `AnalyzerFactory.uml` (method) `readmenator/_pipeline.py:184` `def uml(self)`
- `AnalyzerFactory.wiki` (method) `readmenator/_pipeline.py:190` `def wiki(self)` -- Return the lazily initialised agent wiki generator.
- `AnalyzerFactory.readme_injector` (method) `readmenator/_pipeline.py:197` `def readme_injector(self)`
- `AnalyzerFactory.agent_injector` (method) `readmenator/_pipeline.py:207` `def agent_injector(self)`
- `AnalyzerFactory.gh_wiki` (method) `readmenator/_pipeline.py:217` `def gh_wiki(self)` -- Return the lazily initialised GitHub wiki publisher.
- `AnalyzerFactory.agent_output` (method) `readmenator/_pipeline.py:224` `def agent_output(self)`
- `AnalyzerFactory.diagram_builder` (method) `readmenator/_pipeline.py:230` `def diagram_builder(self)` -- Return the lazily initialised system map builder.
- `AnalyzerFactory.diagram_renderer` (method) `readmenator/_pipeline.py:237` `def diagram_renderer(self)` -- Return the lazily initialised interactive map renderer.
- `AnalyzerFactory.diagram_validator` (method) `readmenator/_pipeline.py:244` `def diagram_validator(self)` -- Return the lazily initialised system map validator.
- `AnalyzerFactory.diagram_publisher` (method) `readmenator/_pipeline.py:251` `def diagram_publisher(self)` -- Return the lazily initialised documentation site publisher.
- `AnalyzerFactory.vis_renderer` (method) `readmenator/_pipeline.py:258` `def vis_renderer(self)` -- Return the lazily initialised vis.js network renderer.
- `AnalyzerFactory.video` (method) `readmenator/_pipeline.py:265` `def video(self)` -- Return the lazily initialised cinematic video renderer.
- `AnalyzerFactory.concepts` (method) `readmenator/_pipeline.py:272` `def concepts(self)` -- Return the lazily initialised semantic concept extractor.
- `AnalyzerFactory.forcegraph` (method) `readmenator/_pipeline.py:279` `def forcegraph(self)` -- Return the lazily initialised force-graph renderer.
- `AnalyzerFactory.analytics` (method) `readmenator/_pipeline.py:286` `def analytics(self)` -- Return the lazily initialised corpus analytics builder.
- `AnalyzerFactory.scantext` (method) `readmenator/_pipeline.py:293` `def scantext(self)` -- Return the lazily initialised scan-text builder.
- `AnalyzerFactory.provenance` (method) `readmenator/_pipeline.py:300` `def provenance(self)` -- Return the lazily initialised provenance auditor.
- `AnalyzerFactory.exclusions` (method) `readmenator/_pipeline.py:307` `def exclusions(self)` -- Return the lazily initialised FP exclusion list.
- `AnalyzerFactory.embedder` (method) `readmenator/_pipeline.py:314` `def embedder(self)` -- Return the lazily initialised semantic embedder.
- `AnalyzerFactory.build_typed_graph` (method) `readmenator/_pipeline.py:320` `def build_typed_graph(self, nodes, edges, resolved_edges)`
- `AnalyzerFactory.make_ranker` (method) `readmenator/_pipeline.py:330` `def make_ranker(self, typed_graph)` -- Create a CompositeRanker for the given typed graph.
- `AnalyzerFactory.last_category` (method) `readmenator/_pipeline.py:347` `def last_category(self)`
- `AnalyzerFactory.last_typed_graph` (method) `readmenator/_pipeline.py:351` `def last_typed_graph(self)`
- `DeepAnalysisRunner.__init__` (method) `readmenator/_pipeline.py:364` `def __init__(self, factory)`
- `DeepAnalysisRunner.run` (method) `readmenator/_pipeline.py:367` `def run(self, nodes, edges, resolved_edges, layers, content_map)`

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
- `RiskProjection.apply_view` (method) `readmenator/_projections.py:95` `def apply_view(category, view_config)` -- Apply a named view to produce a projected category.

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
Imported by: `readmenator/_agent_output.py`, `readmenator/_wiki.py`, `tests/test_agent_friendliness.py`
- `is_garbage_doc` (function) `readmenator/_purpose.py:26` `def is_garbage_doc(text)` -- Return True for doc lines that carry no purpose signal.
- `clean_purpose` (function) `readmenator/_purpose.py:43` `def clean_purpose(text)` -- Return the purpose signal of a doc first line, or an empty string.
- `escape_cell` (function) `readmenator/_purpose.py:66` `def escape_cell(text)` -- Escape markdown table breaking characters in one line of text.
- `truncate_words` (function) `readmenator/_purpose.py:78` `def truncate_words(text, max_chars)` -- Truncate text at a word boundary and mark the cut with an ellipsis.
- `first_sentence` (function) `readmenator/_purpose.py:98` `def first_sentence(doc)` -- Return the first clean sentence of the first meaningful paragraph.
- `file_purpose` (function) `readmenator/_purpose.py:140` `def file_purpose(node, max_chars)` -- Return a bounded one-sentence purpose for a file node.

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
Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `tests/test_ranking.py`
- `RankConfig.global_pagerank` (method) `readmenator/_rank.py:61` `def global_pagerank(graph, alpha, max_iter, tolerance)` -- Compute global PageRank on the typed weighted graph.
- `RankConfig.personalized_pagerank` (method) `readmenator/_rank.py:119` `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` -- Compute Personalized PageRank with a seed-node preference vector.
- `RankConfig.hits` (method) `readmenator/_rank.py:189` `def hits(graph, max_iter, tolerance)` -- Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.
- `RankConfig.build_seeds_from_query` (method) `readmenator/_rank.py:240` `def build_seeds_from_query(query, node_ids, node_labels, symbols)` -- Build a PPR seed vector from a natural-language query string.
- `RankConfig.build_seeds_for_context` (method) `readmenator/_rank.py:286` `def build_seeds_for_context(node_ids, anchor_patterns)` -- Build a PPR seed vector from anchor pattern strings.
- `RankedItem.label` (method) `readmenator/_rank.py:344` `def label(self)`
- `RankedResult.top` (method) `readmenator/_rank.py:366` `def top(self, n)`
- `RankedResult.explain` (method) `readmenator/_rank.py:369` `def explain(self, node_id)` -- Return a human-readable explanation of why *node_id* ranks as it does.
- `CompositeRanker.__init__` (method) `readmenator/_rank.py:385` `def __init__(self, graph, config)`
- `CompositeRanker.rank` (method) `readmenator/_rank.py:404` `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` -- Compute composite ranking for a query.

## readmenator/_readme_injector.py
Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_agent_output.py`, `tests/test_readme_injector.py`
- `ReadmeInjector.__init__` (method) `readmenator/_readme_injector.py:78` `def __init__(self, kb_filename, agent_output_dir, wiki_output_dir)`
- `ReadmeInjector.inject` (method) `readmenator/_readme_injector.py:88` `def inject(self, project_root)`
- `ReadmeInjector.remove` (method) `readmenator/_readme_injector.py:136` `def remove(self, project_root)`

## readmenator/_refactorizer.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_app.py`, `tests/test_refactorizer.py`
- `MonolithRefactorizer.__init__` (method) `readmenator/_refactorizer.py:32` `def __init__(self, config)`
- `MonolithRefactorizer.analyze` (method) `readmenator/_refactorizer.py:35` `def analyze(self, nodes, edges, resolved_edges, content_map)` -- Identify monolithic files and generate refactoring plans.
- `MonolithRefactorizer.generate_script` (method) `readmenator/_refactorizer.py:156` `def generate_script(self, plan, project_root)`

## readmenator/_resolver.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `tests/test_agent_friendliness.py`, `tests/test_resolver.py`, `tests/test_taint_bdd.py`
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
- `PolyglotScanner.scan` (method) `readmenator/_scanner.py:261` `def scan(self, root)` -- Walk *root* recursively and produce (nodes, edges) for the graph.
- `PolyglotScanner.scan_with_content` (method) `readmenator/_scanner.py:275` `def scan_with_content(self, root)` -- Scan and also return raw file contents for deeper analysis.

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
- `SecurityAnalyzer.fix_hint_for` (method) `readmenator/_security.py:620` `def fix_hint_for(finding)` -- Return a one-line remediation hint for a security finding.

## readmenator/_taint.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_taint.py`, `tests/test_taint_bdd.py`
- `TaintAnalyzer.__init__` (method) `readmenator/_taint.py:73` `def __init__(self, config)`
- `TaintAnalyzer.analyze` (method) `readmenator/_taint.py:77` `def analyze(self, nodes, edges, resolved_edges)` -- Run taint propagation analysis on the codebase.


Next: [API_p2.md](API_p2.md)
