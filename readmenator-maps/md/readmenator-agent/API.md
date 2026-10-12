# API (page 1 of 2)
Pages: [API.md](API.md), [API_p2.md](API_p2.md)

## readmenator/__main__.py
Depends on: `readmenator/_app.py`, `readmenator/_config.py`, `readmenator/_mcp_server.py`
Imported by: `readmenator.py`
- `build_parser` (function) `readmenator/__main__.py:18` `def build_parser()`
- `main` (function) `readmenator/__main__.py:151` `def main()`

## readmenator/_agent_injector.py
Imported by: `readmenator/_pipeline.py`, `tests/test_agent_injector.py`, `tests/test_agent_output.py`
- `ensure_readmenator_installed` (function) `readmenator/_agent_injector.py:107` `def ensure_readmenator_installed()` -- Check if readmenator is installed via pip; install it if missing.
- `AgentInjector.__init__` (method) `readmenator/_agent_injector.py:140` `def __init__(self, kb_filename, agent_output_dir, agent_files, agent_globs, wiki_output_dir)`
- `AgentInjector.inject` (method) `readmenator/_agent_injector.py:154` `def inject(self, project_root)` -- Inject KB reference into all discovered agent files.
- `AgentInjector.remove` (method) `readmenator/_agent_injector.py:172` `def remove(self, project_root)` -- Remove KB injection from all discovered agent files.
- `AgentInjector.find_agent_files` (method) `readmenator/_agent_injector.py:185` `def find_agent_files(self, project_root)` -- Public accessor: return all detected agent files.

## readmenator/_agent_output.py
Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_gitmeta.py`, `readmenator/_models.py`, `readmenator/_purpose.py`, `readmenator/_resolver.py`, `readmenator/_security.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`, `tests/test_agent_output.py`
- `AgentOutputGenerator.__init__` (method) `readmenator/_agent_output.py:77` `def __init__(self, config)` -- Store configuration for output paths and size budgets.
- `AgentOutputGenerator.generate` (method) `readmenator/_agent_output.py:81` `def generate(self, nodes, edges, resolved_edges, analysis, analysis_v2, findings, layers, project_root)` -- Write all agent output files and return the output directory path.
- `keep` (function) `readmenator/_agent_output.py:525` `def keep(file_id)` -- Return whether a file belongs in the gotcha lists.

## readmenator/_analytics.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_documentation.py`, `readmenator/_explorer.py`, `readmenator/_exporter.py`, `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `AnalyticsBuilder.__init__` (method) `readmenator/_analytics.py:28` `def __init__(self, config)` -- Initialise with application configuration.
- `AnalyticsBuilder.build` (method) `readmenator/_analytics.py:36` `def build(self, nodes, edges, resolved_edges, analysis, findings, layers, v2, hotspots)` -- Build the full analytics payload.

## readmenator/_analyzer.py
Depends on: `readmenator/_config.py`, `readmenator/_models.py`
Imported by: `readmenator/_graphrag.py`, `readmenator/_pipeline.py`, `readmenator/_wiki.py`, `tests/test_agent_friendliness.py`, `tests/test_analyzer.py`
- `dominant_directory` (function) `readmenator/_analyzer.py:22` `def dominant_directory(file_ids)` -- Return the most informative directory label for a set of files.
- `GraphAnalyzer.__init__` (method) `readmenator/_analyzer.py:54` `def __init__(self, config)` -- Initialise with application configuration.
- `GraphAnalyzer.analyze` (method) `readmenator/_analyzer.py:62` `def analyze(self, nodes, edges, resolved_edges)` -- Run the full analysis pipeline and return structured results.
- `GraphAnalyzer.partition` (method) `readmenator/_analyzer.py:268` `def partition(self, ids, adjacency)` -- Partition an arbitrary undirected id graph with deterministic Louvain.

## readmenator/_apidocs.py
Depends on: `readmenator/_config.py`, `readmenator/_docstrings.py`, `readmenator/_models.py`, `readmenator/_pytypes.py`, `readmenator/_symindex.py`
Imported by: `readmenator/_apidocs_page.py`, `readmenator/_apidocs_render.py`, `readmenator/_app.py`, `readmenator/_flowcharts.py`, `readmenator/_pipeline.py`, `tests/test_apidocs.py`, `tests/test_flowcharts.py`
- `ApiParam.to_dict` (method) `readmenator/_apidocs.py:91` `def to_dict(self)` -- Serialise to a plain dict for JSON output.
- `ApiEntity.is_documented` (method) `readmenator/_apidocs.py:156` `def is_documented(self)` -- Return True when any documentation text was found.
- `ApiEntity.to_dict` (method) `readmenator/_apidocs.py:160` `def to_dict(self)` -- Serialise to a plain dict for JSON output.
- `DocWarning.to_dict` (method) `readmenator/_apidocs.py:197` `def to_dict(self)` -- Serialise to a plain dict for JSON output.
- `ApiReference.children` (method) `readmenator/_apidocs.py:221` `def children(self, uid, kinds)` -- Return direct members of *uid*, optionally filtered by kind, in source order.
- `ApiReference.to_dict` (method) `readmenator/_apidocs.py:232` `def to_dict(self, schema_version)` -- Serialise the whole reference for ``api.json``.
- `_PythonExtractor.__init__` (method) `readmenator/_apidocs.py:257` `def __init__(self, file_id, language, include_private)` -- Initialise for one file.
- `_PythonExtractor.extract` (method) `readmenator/_apidocs.py:272` `def extract(self, content)` -- Parse *content*; return False when it is not valid Python.
- `parse_signature_params` (function) `readmenator/_apidocs.py:685` `def parse_signature_params(signature, name, language)` -- Split a non-Python signature into parameters and a return type.
- `is_vendored_path` (function) `readmenator/_apidocs.py:759` `def is_vendored_path(file_id, config)` -- Return True for minified bundles and files under vendored third-party trees.
- `ApiReferenceBuilder.__init__` (method) `readmenator/_apidocs.py:775` `def __init__(self, config)` -- Initialise with application configuration.
- `ApiReferenceBuilder.build` (method) `readmenator/_apidocs.py:796` `def build(self, nodes, edges, resolved_edges, content_map)` -- Build the full API reference.
- `innermost` (function) `readmenator/_apidocs.py:1154` `def innermost(file_id, line, name)` -- Return the narrowest callable in *file_id* spanning *line*.
- `target_entity` (function) `readmenator/_apidocs.py:1166` `def target_entity(file_id, line, name)` -- Return the entity defined at *line* in *file_id* (or by name).
- `counts` (function) `readmenator/_apidocs.py:1320` `def counts(items)` -- Return documented/total/percent for *items*.

## readmenator/_apidocs_page.py
Depends on: `readmenator/_apidocs.py`, `readmenator/_config.py`, `readmenator/_flowlayout.py`, `readmenator/_flowpage.py`
Imported by: `readmenator/_apidocs_render.py`, `tests/test_apidocs.py`, `tests/test_flowcharts.py`
- `render_api_site` (function) `readmenator/_apidocs_page.py:57` `def render_api_site(reference, project_name, config, flow_graphs)` -- Render the standalone HTML API browser.

## readmenator/_apidocs_render.py
Depends on: `readmenator/_apidocs.py`, `readmenator/_apidocs_page.py`, `readmenator/_config.py`, `readmenator/_docstrings.py`, `readmenator/_flowlayout.py`, `readmenator/_flowpage.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_apidocs.py`
- `module_display_name` (function) `readmenator/_apidocs_render.py:64` `def module_display_name(entity)` -- Return the Sphinx-style display name of a module entity.
- `page_slug` (function) `readmenator/_apidocs_render.py:75` `def page_slug(module_uid)` -- Return the deterministic page file stem for a module uid.
- `anchor_slug` (function) `readmenator/_apidocs_render.py:81` `def anchor_slug(qualname)` -- Return the HTML anchor id for an entity qualname.
- `ApiLinker.__init__` (method) `readmenator/_apidocs_render.py:103` `def __init__(self, reference)` -- Index every entity by uid, qualname, and simple name.
- `ApiLinker.module_of` (method) `readmenator/_apidocs_render.py:120` `def module_of(self, entity)` -- Return the module entity that contains *entity*.
- `ApiLinker.resolve` (method) `readmenator/_apidocs_render.py:124` `def resolve(self, name, context_file)` -- Resolve a written reference to an entity, preferring *context_file*.
- `ApiLinker.href` (method) `readmenator/_apidocs_render.py:161` `def href(self, entity, from_module)` -- Return the relative link to *entity* from a module page (or index when "").
- `ApiLinker.link` (method) `readmenator/_apidocs_render.py:170` `def link(self, entity, from_module, label)` -- Return a Markdown link to *entity*.
- `ApiLinker.link_uid` (method) `readmenator/_apidocs_render.py:175` `def link_uid(self, uid, from_module)` -- Return a Markdown link to the entity with *uid* (plain code when unknown).
- `ApiLinker.autolink` (method) `readmenator/_apidocs_render.py:182` `def autolink(self, text, from_module)` -- Turn backtick names, Sphinx roles, and ``{@link}`` tags into links.
- `ApiMarkdownRenderer.__init__` (method) `readmenator/_apidocs_render.py:221` `def __init__(self, config)` -- Initialise with application configuration.
- `ApiMarkdownRenderer.render` (method) `readmenator/_apidocs_render.py:229` `def render(self, reference, project_name)` -- Render every page.
- `walk` (function) `readmenator/_apidocs_render.py:348` `def walk(entity, depth)` -- Emit *entity* and its subclasses as a nested list.
- `ApiDocsWriter.__init__` (method) `readmenator/_apidocs_render.py:736` `def __init__(self, config)` -- Initialise with application configuration.
- `ApiDocsWriter.write` (method) `readmenator/_apidocs_render.py:745` `def write(self, reference, project_root, project_name, architecture_markdown, flow_graphs)` -- Write every page and prune stale module pages.

## readmenator/_app.py
Depends on: `readmenator/_apidocs.py`, `readmenator/_bundlegraph.py`, `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_dead_code.py`, `readmenator/_diagrams.py`, `readmenator/_explorer.py`, `readmenator/_flowcharts.py`, `readmenator/_flowlayout.py`, `readmenator/_flowpage.py`, `readmenator/_gh_wiki.py`, `readmenator/_gitmeta.py`, `readmenator/_graphrag.py`, `readmenator/_layers.py`, `readmenator/_linter.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `readmenator/_refactorizer.py`, `readmenator/_resolver.py`, `readmenator/_video.py`, `readmenator/_watcher.py`, `readmenator/_yaralite.py`
Imported by: `readmenator/__init__.py`, `readmenator/__main__.py`, `readmenator/_mcp_server.py`, `tests/test_agent_friendliness.py`, `tests/test_apidocs.py`, `tests/test_bundlegraph.py`, `tests/test_components.py`, `tests/test_diagrams.py`, `tests/test_gh_wiki.py`, `tests/test_integration.py`, `tests/test_interactive_graph.py`, `tests/test_mcp_server.py`, `tests/test_sourceview.py`, `tests/test_video.py`
- `readmenatorApplication.__init__` (method) `readmenator/_app.py:55` `def __init__(self, config)`
- `readmenatorApplication.run` (method) `readmenator/_app.py:101` `def run(self, target_dir, resolve_imports, run_analysis, run_security, run_v2_analysis)`
- `readmenatorApplication.check_freshness` (method) `readmenator/_app.py:252` `def check_freshness(self, target_dir)` -- Compare the MANIFEST source fingerprint against the current sources.
- `readmenatorApplication.publish_github_wiki` (method) `readmenator/_app.py:315` `def publish_github_wiki(self, target_dir, dry_run)` -- Mirror the generated wiki, agent docs, and knowledge base to the GitHub wiki.
- `readmenatorApplication.generate_uml_code` (method) `readmenator/_app.py:371` `def generate_uml_code(self, target_dir, language, output_path)`
- `readmenatorApplication.update` (method) `readmenator/_app.py:438` `def update(self, target_dir, run_security)`
- `readmenatorApplication.query` (method) `readmenator/_app.py:569` `def query(self, target_dir, question)`
- `readmenatorApplication.explain` (method) `readmenator/_app.py:574` `def explain(self, target_dir, symbol_name)`
- `readmenatorApplication.find_path` (method) `readmenator/_app.py:586` `def find_path(self, target_dir, symbol_a, symbol_b)`
- `readmenatorApplication.summary` (method) `readmenator/_app.py:599` `def summary(self, target_dir)`
- `readmenatorApplication.rank_query` (method) `readmenator/_app.py:604` `def rank_query(self, target_dir, query, top_n)` -- Run a ranked query against the knowledge graph.
- `readmenatorApplication.rebuild` (method) `readmenator/_app.py:634` `def rebuild(self, target_dir, run_security)`
- `readmenatorApplication.analyze` (method) `readmenator/_app.py:637` `def analyze(self, target_dir)`
- `readmenatorApplication.export_json` (method) `readmenator/_app.py:641` `def export_json(self, target_dir, output_path)`
- `readmenatorApplication.export_html` (method) `readmenator/_app.py:658` `def export_html(self, target_dir, output_path)`
- `readmenatorApplication.export_svg` (method) `readmenator/_app.py:669` `def export_svg(self, target_dir, output_path)`
- `readmenatorApplication.export` (method) `readmenator/_app.py:680` `def export(self, target_dir)`
- `readmenatorApplication.export_forcegraph` (method) `readmenator/_app.py:933` `def export_forcegraph(self, target_dir, output_path)` -- Export the force-graph explorer HTML document.
- `readmenatorApplication.export_bundlegraph` (method) `readmenator/_app.py:952` `def export_bundlegraph(self, target_dir, output_path)` -- Export the edge bundle explorer HTML document (circle and sphere views).
- `readmenatorApplication.export_components` (method) `readmenator/_app.py:978` `def export_components(self, target_dir, output_dir)` -- Export component diagrams (analysis.json + graph LR markdown + index.html).
- `readmenatorApplication.build_api_reference` (method) `readmenator/_app.py:1113` `def build_api_reference(self, target_dir)` -- Scan *target_dir* and build its API reference without writing it.
- `readmenatorApplication.export_apidocs` (method) `readmenator/_app.py:1125` `def export_apidocs(self, target_dir)` -- Generate the API reference tree (Markdown, api.json, index.html).
- `readmenatorApplication.export_flows` (method) `readmenator/_app.py:1145` `def export_flows(self, target_dir)` -- Write the standalone interactive architecture and flow page into the maps directory.
- `readmenatorApplication.explorer_state` (method) `readmenator/_app.py:1162` `def explorer_state(self, target_dir)` -- Build explorer state for the local HTTP server.
- `readmenatorApplication.serve_explorer` (method) `readmenator/_app.py:1178` `def serve_explorer(self, target_dir, open_browser)` -- Serve the local explorer UI until interrupted.
- `readmenatorApplication.analytics` (method) `readmenator/_app.py:1191` `def analytics(self, target_dir)` -- Compute the corpus analytics payload.
- `readmenatorApplication.scan_texts` (method) `readmenator/_app.py:1208` `def scan_texts(self, target_dir)` -- Build scan-text blobs for every file in the project.
- `readmenatorApplication.near` (method) `readmenator/_app.py:1220` `def near(self, target_dir, query, top_k)` -- Find semantically similar files for a query file or text.
- `readmenatorApplication.audit_provenance` (method) `readmenator/_app.py:1234` `def audit_provenance(self, target_dir)` -- Audit security findings by evidence provenance.
- `readmenatorApplication.validate_yaralite` (method) `readmenator/_app.py:1257` `def validate_yaralite(self, target_dir)` -- Validate the project YARA-lite rules file.
- `readmenatorApplication.export_graphml` (method) `readmenator/_app.py:1271` `def export_graphml(self, target_dir, output_path)`
- `readmenatorApplication.export_cypher` (method) `readmenator/_app.py:1282` `def export_cypher(self, target_dir, output_path)`
- `readmenatorApplication.export_obsidian` (method) `readmenator/_app.py:1298` `def export_obsidian(self, target_dir, output_dir)`
- `readmenatorApplication.export_wiki` (method) `readmenator/_app.py:1313` `def export_wiki(self, target_dir, output_dir)` -- Generate the navigable agent wiki for the target project.
- `readmenatorApplication.lint_wiki` (method) `readmenator/_app.py:1336` `def lint_wiki(self, target_dir)` -- Check wiki health and log reported issues.
- `readmenatorApplication.export_diagrams` (method) `readmenator/_app.py:1354` `def export_diagrams(self, target_dir, output_dir, full)` -- Export all five interactive system maps plus a gallery index.
- `readmenatorApplication.export_diagram` (method) `readmenator/_app.py:1421` `def export_diagram(self, target_dir, kind, output_path, full)` -- Export a single interactive system map as standalone HTML.
- `readmenatorApplication.export_pages` (method) `readmenator/_app.py:1460` `def export_pages(self, target_dir, output_dir, full)` -- Publish all system maps plus a gallery index as a static site.
- `readmenatorApplication.export_video` (method) `readmenator/_app.py:1505` `def export_video(self, target_dir, output_path)` -- Render the cinematic overview video for the target project.
- `readmenatorApplication.memory` (method) `readmenator/_app.py:1732` `def memory(self, target_dir)` -- Return MEMORY.md, generating it first when missing.
- `readmenatorApplication.remember` (method) `readmenator/_app.py:1755` `def remember(self, target_dir, note, kind)` -- Append a note to the preserved MEMORY.md session log.
- `readmenatorApplication.install_skills` (method) `readmenator/_app.py:1769` `def install_skills(self, target_dir, target)` -- Install the packaged agent skills into the project.
- `readmenatorApplication.build_graphrag` (method) `readmenator/_app.py:1781` `def build_graphrag(self, target_dir)` -- Scan, analyse, and write the GraphRAG index for a project.
- `readmenatorApplication.graphrag_search` (method) `readmenator/_app.py:1804` `def graphrag_search(self, target_dir, query, mode, budget_tokens)` -- Answer a question with GraphRAG retrieval over the persisted index.
- `readmenatorApplication.watch` (method) `readmenator/_app.py:1825` `def watch(self, target_dir)`
- `on_change` (function) `readmenator/_app.py:1829` `def on_change()`
- `readmenatorApplication.audit` (method) `readmenator/_app.py:1835` `def audit(self, target_dir)`
- `readmenatorApplication.audit_deep` (method) `readmenator/_app.py:1842` `def audit_deep(self, target_dir)`
- `readmenatorApplication.export_sarif` (method) `readmenator/_app.py:1862` `def export_sarif(self, target_dir, output_path)`
- `readmenatorApplication.export_rules` (method) `readmenator/_app.py:1872` `def export_rules(self, target_dir, output_dir)`
- `readmenatorApplication.detect_layers` (method) `readmenator/_app.py:1882` `def detect_layers(self, target_dir)`
- `readmenatorApplication.lint` (method) `readmenator/_app.py:1892` `def lint(self, target_dir)`
- `readmenatorApplication.strip_dead_code` (method) `readmenator/_app.py:1905` `def strip_dead_code(self, target_dir)`
- `readmenatorApplication.generate_cursorrules` (method) `readmenator/_app.py:1915` `def generate_cursorrules(self, target_dir)`
- `readmenatorApplication.refactor_monolith` (method) `readmenator/_app.py:1930` `def refactor_monolith(self, target_dir)`

## readmenator/_bundlegraph.py
Depends on: `readmenator/_bundlegraph_page.py`, `readmenator/_config.py`, `readmenator/_forcegraph.py`, `readmenator/_graphlayout.py`
Imported by: `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_bundlegraph.py`, `tests/test_layout_quality.py`, `tests/test_sourceview.py`
- `BundleGraphRenderer.__init__` (method) `readmenator/_bundlegraph.py:51` `def __init__(self, config)` -- Initialise with application configuration.
- `BundleGraphRenderer.build_payload` (method) `readmenator/_bundlegraph.py:60` `def build_payload(self, force_payload)` -- Derive the bundle payload from a force-graph payload.
- `BundleGraphRenderer.page_settings` (method) `readmenator/_bundlegraph.py:181` `def page_settings(self, force_payload, explorer_href, live_api)` -- Collect the page settings serialized into the HTML.
- `BundleGraphRenderer.render` (method) `readmenator/_bundlegraph.py:225` `def render(self, force_payload, title, home_href, explorer_href, live_api)` -- Render the standalone edge bundle explorer HTML document.
- `BundleGraphRenderer.write` (method) `readmenator/_bundlegraph.py:263` `def write(self, output_path, force_payload, title, home_href, explorer_href)` -- Write the edge bundle explorer HTML document.
- `BundleGraphRenderer.thumbnail_svg` (method) `readmenator/_bundlegraph.py:289` `def thumbnail_svg(self, force_payload)` -- Render a small circular bundle preview as inline SVG.

## readmenator/_cache.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `readmenator/_components.py`, `tests/test_agent_friendliness.py`, `tests/test_cache.py`
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
- `source_fingerprint` (function) `readmenator/_cache.py:179` `def source_fingerprint(project_root, file_ids)` -- Return one SHA256 over the sorted paths and contents of scanned sources.

## readmenator/_category.py
Imported by: `readmenator/__init__.py`, `readmenator/_explain.py`, `readmenator/_graphrag.py`, `readmenator/_models.py`, `readmenator/_pipeline.py`, `readmenator/_projections.py`, `readmenator/_query.py`, `readmenator/_rank.py`, `tests/test_ranking.py`
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
- `dfs` (function) `readmenator/_category.py:139` `def dfs(current, goal, path, depth)`
- `TypedGraph.__init__` (method) `readmenator/_category.py:188` `def __init__(self, category)`
- `TypedGraph.nodes` (method) `readmenator/_category.py:203` `def nodes(self)`
- `TypedGraph.size` (method) `readmenator/_category.py:207` `def size(self)`
- `TypedGraph.node_index` (method) `readmenator/_category.py:210` `def node_index(self, node_id)`
- `TypedGraph.transition_weight` (method) `readmenator/_category.py:213` `def transition_weight(self, source, target)` -- Sum of weights of all morphisms from source to target.
- `TypedGraph.stochastic_row` (method) `readmenator/_category.py:221` `def stochastic_row(self, source)` -- Return dict of target -> probability for the row of *source*.
- `build_category_from_edges` (function) `readmenator/_category.py:236` `def build_category_from_edges(edges, resolved_edges, node_ids)` -- Build a Category from lists of Edge objects.

## readmenator/_components.py
Depends on: `readmenator/_cache.py`, `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_ollama.py`, `readmenator/_purpose.py`, `readmenator/_rank.py`, `readmenator/_symindex.py`
Imported by: `readmenator/__init__.py`, `readmenator/_pipeline.py`, `tests/test_components.py`
- `sanitize` (function) `readmenator/_components.py:45` `def sanitize(name)` -- Replace non-alphanumerics with underscores for Mermaid node ids.
- `ComponentDiagramBuilder.__init__` (method) `readmenator/_components.py:60` `def __init__(self, config)` -- Initialise with application configuration.
- `ComponentDiagramBuilder.build` (method) `readmenator/_components.py:70` `def build(self, nodes, edges, resolved_edges, analysis, project_root, content_map)` -- Build the full analysis document.
- `ComponentDiagramBuilder.mermaid_lr` (method) `readmenator/_components.py:165` `def mermaid_lr(self, components, relations, docs_ref)` -- Render the ``graph LR`` overview diagram.
- `ComponentDiagramBuilder.overview_markdown` (method) `readmenator/_components.py:199` `def overview_markdown(self, analysis, docs_ref, rel_prefix)` -- Render the overview page (diagram plus component details).
- `ComponentDiagramBuilder.component_markdown` (method) `readmenator/_components.py:247` `def component_markdown(self, component)` -- Render one expandable component's detail page.
- `ComponentDiagramBuilder.write` (method) `readmenator/_components.py:275` `def write(self, analysis, output_dir, project_root)` -- Write analysis.json, the overview, component pages, and index.html.
- `ComponentDiagramBuilder.render_page` (method) `readmenator/_components.py:611` `def render_page(self, analysis, title, home_href, rel_prefix, link_files)` -- Render the standalone interactive diagram page.
- `ComponentDiagramBuilder.thumbnail_svg` (method) `readmenator/_components.py:738` `def thumbnail_svg(self, components, relations)` -- Render a small dagre-style preview as inline SVG.

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
Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`, `tests/test_components.py`, `tests/test_diagrams.py`, `tests/test_interactive_graph.py`
- `SystemMapValidator.__init__` (method) `readmenator/_diagrams.py:233` `def __init__(self, config)` -- Initialise the validator with application configuration.
- `SystemMapValidator.validate` (method) `readmenator/_diagrams.py:262` `def validate(self, system_map)` -- Validate a system map and return a deterministic receipt.
- `SystemMapBuilder.__init__` (method) `readmenator/_diagrams.py:483` `def __init__(self, config)` -- Initialise the builder with application configuration.
- `SystemMapBuilder.supported_kinds` (method) `readmenator/_diagrams.py:492` `def supported_kinds(self)` -- Return the supported diagram kind identifiers.
- `SystemMapBuilder.build` (method) `readmenator/_diagrams.py:513` `def build(self, nodes, edges, resolved_edges, layers, findings, analysis, kind, full)` -- Build one deterministic system map of the requested kind.
- `SystemMapBuilder.build_all` (method) `readmenator/_diagrams.py:572` `def build_all(self, nodes, edges, resolved_edges, layers, findings, analysis, full)` -- Build all five diagram kinds deterministically.
- `SystemMapBuilder.compare` (method) `readmenator/_diagrams.py:603` `def compare(self, base, head)` -- Compare two maps of the same kind as before, delta, and after.
- `InteractiveMapRenderer.__init__` (method) `readmenator/_diagrams.py:1523` `def __init__(self, config)` -- Initialise the renderer with application configuration.
- `InteractiveMapRenderer.render` (method) `readmenator/_diagrams.py:1552` `def render(self, system_map)` -- Render a system map as a self-contained HTML document.
- `InteractiveMapRenderer.write` (method) `readmenator/_diagrams.py:1643` `def write(self, system_map, output_path)` -- Render a system map and write it to a relative output path.
- `VisNetworkRenderer.__init__` (method) `readmenator/_diagrams.py:2234` `def __init__(self, config)` -- Initialise the renderer with application configuration.
- `VisNetworkRenderer.render` (method) `readmenator/_diagrams.py:2242` `def render(self, system_map)` -- Render a system map as a vis.js network HTML document.
- `VisNetworkRenderer.write` (method) `readmenator/_diagrams.py:2364` `def write(self, system_map, output_path)` -- Render a vis.js map and write it to a relative output path.
- `DocsSitePublisher.__init__` (method) `readmenator/_diagrams.py:3224` `def __init__(self, config)` -- Initialise the publisher with application configuration.
- `DocsSitePublisher.description_for` (method) `readmenator/_diagrams.py:3234` `def description_for(self, kind)` -- Return the gallery description for a diagram kind.
- `DocsSitePublisher.publish` (method) `readmenator/_diagrams.py:3248` `def publish(self, maps, project_name, output_dir, stats, renderer, project_root, video_rel, doc_entries, extra_cards)` -- Publish maps and a gallery index into a documentation directory.
- `DocsSitePublisher.collect_doc_sources` (method) `readmenator/_diagrams.py:3342` `def collect_doc_sources(self, project_root)` -- Collect generated markdown sources for the static site.
- `DocsSitePublisher.publish_assets` (method) `readmenator/_diagrams.py:3368` `def publish_assets(self, project_root, output_dir)` -- Copy overview video and markdown docs into the static site.
- `DocsSitePublisher.render_llms_txt` (method) `readmenator/_diagrams.py:3537` `def render_llms_txt(self, project_name, maps, stats, href_prefix, doc_entries)` -- Render an llms.txt entry point so agents can navigate the site as text.
- `order` (function) `readmenator/_diagrams.py:3588` `def order(entry)` -- Sort entry points first, then alphabetically.
- `DocsSitePublisher.render_index` (method) `readmenator/_diagrams.py:3616` `def render_index(self, project_name, maps, stats, href_prefix, video_rel, doc_entries, poster_rel, extra_cards)` -- Render the gallery index page for published maps.
- `doc_order` (function) `readmenator/_diagrams.py:3851` `def doc_order(base)` -- Entry points first, then alphabetical.

## readmenator/_docstrings.py
Imported by: `readmenator/_apidocs.py`, `readmenator/_apidocs_render.py`, `tests/test_apidocs.py`
- `DocField.to_dict` (method) `readmenator/_docstrings.py:150` `def to_dict(self)` -- Serialise to a plain dict for JSON output.
- `DocComment.is_empty` (method) `readmenator/_docstrings.py:195` `def is_empty(self)` -- Return True when no documentation text was recovered.
- `DocComment.param` (method) `readmenator/_docstrings.py:203` `def param(self, name)` -- Return the documented parameter called *name* (stars ignored).
- `DocComment.to_dict` (method) `readmenator/_docstrings.py:211` `def to_dict(self)` -- Serialise to a plain dict for JSON output.
- `clean_text` (function) `readmenator/_docstrings.py:230` `def clean_text(text)` -- Dedent *text* like ``inspect.cleandoc`` and strip blank edges.
- `detect_style` (function) `readmenator/_docstrings.py:254` `def detect_style(text)` -- Classify the docstring convention used by *text*.
- `split_summary` (function) `readmenator/_docstrings.py:293` `def split_summary(text)` -- Split free text into a one-sentence summary and the remainder.
- `flush` (function) `readmenator/_docstrings.py:413` `def flush()` -- Finalise the item under construction.
- `grab` (function) `readmenator/_docstrings.py:782` `def grab(tag)` -- Return the inner text of the first *tag* element.
- `parse_docstring` (function) `readmenator/_docstrings.py:809` `def parse_docstring(text)` -- Parse *text* in any supported convention into a DocComment.
- `recover_comment` (function) `readmenator/_docstrings.py:910` `def recover_comment(content_lines, line, language, lookback)` -- Recover the raw documentation comment directly above a declaration.

## readmenator/_documentation.py
Depends on: `readmenator/_analytics.py`, `readmenator/_config.py`, `readmenator/_cpg.py`, `readmenator/_flowcharts.py`, `readmenator/_forcegraph.py`, `readmenator/_mermaid.py`, `readmenator/_models.py`, `readmenator/_rank.py`, `readmenator/_uml.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_documentation.py`, `tests/test_flowcharts.py`
- `DocumentationGenerator.__init__` (method) `readmenator/_documentation.py:48` `def __init__(self, config)`
- `DocumentationGenerator.generate` (method) `readmenator/_documentation.py:99` `def generate(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, ranked, content_map)` -- Render KNOWLEDGE_BASE.md.

## readmenator/_embed.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_interactive_graph.py`
- `Embedder.__init__` (method) `readmenator/_embed.py:42` `def __init__(self, config)` -- Initialise with application configuration.
- `Embedder.dependencies_available` (method) `readmenator/_embed.py:50` `def dependencies_available(self)` -- Return True when sentence-transformers is importable.
- `Embedder.encode` (method) `readmenator/_embed.py:58` `def encode(self, texts)` -- Encode texts into L2-normalized vectors when available.
- `Embedder.near_jaccard` (method) `readmenator/_embed.py:75` `def near_jaccard(self, query, corpus, top_k)` -- Find nearest neighbors with offline Jaccard similarity.
- `Embedder.cluster_jaccard` (method) `readmenator/_embed.py:99` `def cluster_jaccard(self, corpus, threshold)` -- Group files into similarity clusters with union-find.
- `find` (function) `readmenator/_embed.py:115` `def find(item)` -- Find the union-find root for an item.
- `union` (function) `readmenator/_embed.py:122` `def union(left, right)` -- Merge two union-find sets.
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
- `parse_exclusions` (function) `readmenator/_exclusions.py:114` `def parse_exclusions(text)` -- Parse the minimal exclusions YAML into entries.

## readmenator/_explain.py
Depends on: `readmenator/_category.py`, `readmenator/_rank.py`
Imported by: `tests/test_ranking.py`
- `explain_rank` (function) `readmenator/_explain.py:16` `def explain_rank(node_id, ranked, category)` -- Return a detailed breakdown of why *node_id* has its rank.
- `rank_summary` (function) `readmenator/_explain.py:140` `def rank_summary(ranked, top_n)` -- Return a short summary of the top-N ranked results.

## readmenator/_explorer.py
Depends on: `readmenator/_analytics.py`, `readmenator/_config.py`, `readmenator/_forcegraph.py`, `readmenator/_models.py`, `readmenator/_sourceview.py`
Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`
- `ExplorerState.__init__` (method) `readmenator/_explorer.py:26` `def __init__(self, config, nodes, edges, resolved_edges, analysis, findings, layers, content_map)` -- Initialise explorer state and precompute payloads.
- `ExplorerState.samples` (method) `readmenator/_explorer.py:64` `def samples(self)` -- Return a compact per-file sample listing.
- `ExplorerState.source` (method) `readmenator/_explorer.py:80` `def source(self, file_id)` -- Return the bounded source text for one file.
- `_Handler.log_message` (method) `readmenator/_explorer.py:108` `def log_message(self, fmt)` -- Silence the default access log.
- `_Handler.do_GET` (method) `readmenator/_explorer.py:112` `def do_GET(self)` -- Dispatch GET routes for HTML and JSON APIs.
- `find_free_port` (function) `readmenator/_explorer.py:169` `def find_free_port(preferred)` -- Find a free TCP port, preferring the configured value.
- `serve` (function) `readmenator/_explorer.py:188` `def serve(state, host, port, open_browser)` -- Serve the explorer state until interrupted.
- `build_state` (function) `readmenator/_explorer.py:221` `def build_state(config, nodes, edges, resolved_edges, analysis, findings, layers, content_map)` -- Build explorer state without starting the server.
- `write_static` (function) `readmenator/_explorer.py:249` `def write_static(state, output_dir, filename)` -- Write the explorer HTML to a static file.

## readmenator/_exporter.py
Depends on: `readmenator/_analytics.py`, `readmenator/_config.py`, `readmenator/_forcegraph.py`, `readmenator/_models.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_exporter.py`, `tests/test_interactive_graph.py`
- `GraphExporter.__init__` (method) `readmenator/_exporter.py:36` `def __init__(self, config)` -- Initialise with application configuration.
- `GraphExporter.to_json` (method) `readmenator/_exporter.py:44` `def to_json(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` -- Export the graph as a node-link JSON string.
- `GraphExporter.to_html` (method) `readmenator/_exporter.py:183` `def to_html(self, nodes, edges, resolved_edges, analysis, findings)` -- Generate a standalone interactive HTML graph page.
- `GraphExporter.to_svg` (method) `readmenator/_exporter.py:482` `def to_svg(self, nodes, edges, resolved_edges, analysis)` -- Generate a static SVG representation of the graph.
- `GraphExporter.to_graphml` (method) `readmenator/_exporter.py:696` `def to_graphml(self, nodes, edges, resolved_edges, analysis)` -- Export the graph as GraphML (Gephi/yEd compatible).
- `GraphExporter.to_cypher` (method) `readmenator/_exporter.py:773` `def to_cypher(self, nodes, edges, resolved_edges, analysis, findings, concept_graph)` -- Export the graph as native Cypher CREATE statements.
- `GraphExporter.to_obsidian` (method) `readmenator/_exporter.py:895` `def to_obsidian(self, nodes, edges, output_dir, analysis, concept_graph)` -- Export the graph as an Obsidian vault with wikilinks.
- `GraphExporter.to_forcegraph` (method) `readmenator/_exporter.py:1020` `def to_forcegraph(self, nodes, edges, resolved_edges, analysis, layers, findings, analytics)` -- Generate the force-graph explorer HTML document.

## readmenator/_flowcharts.py
Depends on: `readmenator/_apidocs.py`, `readmenator/_config.py`, `readmenator/_flowlayout.py`, `readmenator/_models.py`, `readmenator/_pytypes.py`, `readmenator/_symindex.py`
Imported by: `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_video.py`, `tests/test_flowcharts.py`
- `mermaid_id` (function) `readmenator/_flowcharts.py:67` `def mermaid_id(text, prefix)` -- Return a Mermaid-safe identifier for *text*.
- `mermaid_text` (function) `readmenator/_flowcharts.py:72` `def mermaid_text(text, limit)` -- Escape *text* for a quoted Mermaid label, optionally truncating it.
- `tarjan_scc` (function) `readmenator/_flowcharts.py:80` `def tarjan_scc(vertices, adjacency)` -- Return strongly connected components (iterative Tarjan, deterministic order).
- `transitive_reduction` (function) `readmenator/_flowcharts.py:134` `def transitive_reduction(adjacency)` -- Return the transitive reduction of a DAG.
- `reachable` (function) `readmenator/_flowcharts.py:149` `def reachable(vertex)` -- Return every vertex reachable from *vertex* (memoised, iterative).
- `eades_lin_smyth` (function) `readmenator/_flowcharts.py:185` `def eades_lin_smyth(vertices, weight)` -- Order vertices so that heavy dependencies point forward (weighted ELS heuristic).
- `live` (function) `readmenator/_flowcharts.py:211` `def live(table)` -- Sum the weights of edges to vertices still remaining.
- `ArchitectureDiagramBuilder.__init__` (method) `readmenator/_flowcharts.py:262` `def __init__(self, config)` -- Initialise with application configuration.
- `ArchitectureDiagramBuilder.components` (method) `readmenator/_flowcharts.py:270` `def components(self, nodes, analysis, layers)` -- Group files into components with dominant layers.
- `ArchitectureDiagramBuilder.model` (method) `readmenator/_flowcharts.py:335` `def model(self, nodes, resolved_edges, analysis, layers)` -- Build the tiered architecture diagram as a FlowGraph.
- `ArchitectureDiagramBuilder.render` (method) `readmenator/_flowcharts.py:476` `def render(self, nodes, resolved_edges, analysis, layers)` -- Render the tiered architecture as Mermaid (see model()).
- `EntryPoint.key` (method) `readmenator/_flowcharts.py:517` `def key(self)` -- Return the call-graph key of this entry point.
- `ExecutionFlowBuilder.__init__` (method) `readmenator/_flowcharts.py:546` `def __init__(self, config)` -- Initialise with application configuration.
- `ExecutionFlowBuilder.call_graph` (method) `readmenator/_flowcharts.py:564` `def call_graph(self, nodes, edges, resolved_edges, content_map)` -- Build the ordered call graph keyed by ``file::name``.
- `caller_key` (function) `readmenator/_flowcharts.py:596` `def caller_key(site_file, site_line, caller)` -- Return the definition key of the scope making a call.
- `ExecutionFlowBuilder.entry_points` (method) `readmenator/_flowcharts.py:645` `def entry_points(self, nodes, graph, defs, content_map)` -- Score candidate entry points and return the strongest ones.
- `bump` (function) `readmenator/_flowcharts.py:668` `def bump(file_id, name, line, points, reason)` -- Add *points* and evidence to a candidate.
- `ExecutionFlowBuilder.walk` (method) `readmenator/_flowcharts.py:723` `def walk(self, graph, start)` -- Depth-first walk in call-site order, bounded by depth and steps.
- `visit` (function) `readmenator/_flowcharts.py:738` `def visit(caller, depth, path)` -- Emit the calls of *caller* recursively.
- `ExecutionFlowBuilder.call_tree_model` (method) `readmenator/_flowcharts.py:779` `def call_tree_model(self, entry, steps, defs)` -- Build the execution call tree of one entry point.
- `add` (function) `readmenator/_flowcharts.py:800` `def add(key, tone)` -- Declare *key* once.
- `ExecutionFlowBuilder.call_tree_mermaid` (method) `readmenator/_flowcharts.py:827` `def call_tree_mermaid(self, entry, steps, defs)` -- Render an execution call tree as ``flowchart LR``.
- `ExecutionFlowBuilder.sequence_model` (method) `readmenator/_flowcharts.py:831` `def sequence_model(self, entry, steps, defs)` -- Build the cross-file sequence of one walk (None when it never leaves the entry file).
- `ExecutionFlowBuilder.sequence_mermaid` (method) `readmenator/_flowcharts.py:862` `def sequence_mermaid(self, entry, steps, defs)` -- Render the cross-file part of a walk as ``sequenceDiagram``.
- `ExecutionFlowBuilder.control_flow_model` (method) `readmenator/_flowcharts.py:877` `def control_flow_model(self, content, entry, project_names, defs, call_graph)` -- Build the control-flow flowchart of a Python entry function (or ``__main__`` block).
- `ExecutionFlowBuilder.control_flow_mermaid` (method) `readmenator/_flowcharts.py:921` `def control_flow_mermaid(self, content, entry, project_names)` -- Render a Python entry function (or ``__main__`` block) as a Mermaid flowchart.
- `_ControlFlowBuilder.__init__` (method) `readmenator/_flowcharts.py:948` `def __init__(self, config, project_names, summaries, file_id)` -- Initialise with budgets, project callable names, and doc summaries.
- `_ControlFlowBuilder.build` (method) `readmenator/_flowcharts.py:994` `def build(self, body, title)` -- Build the graph for *body*.
- `flush` (function) `readmenator/_flowcharts.py:1022` `def flush()` -- Emit collapsed straight-line calls as one step.
- `to_mermaid` (function) `readmenator/_flowcharts.py:1170` `def to_mermaid(graph, direction)` -- Convert a FlowGraph into Mermaid ``flowchart`` source.
- `label` (function) `readmenator/_flowcharts.py:1182` `def label(node)` -- Node label: title plus detail lines.
- `declare` (function) `readmenator/_flowcharts.py:1187` `def declare(node, indent)` -- Emit one node declaration.
- `build_flow_graphs` (function) `readmenator/_flowcharts.py:1231` `def build_flow_graphs(config, nodes, edges, resolved_edges, content_map, analysis, layers)` -- Build and lay out every architecture and execution-flow diagram.
- `render_architecture_section` (function) `readmenator/_flowcharts.py:1287` `def render_architecture_section(config, nodes, resolved_edges, analysis, layers)` -- Return Markdown lines for the Architecture Overview section.
- `render_flows_section` (function) `readmenator/_flowcharts.py:1319` `def render_flows_section(config, nodes, edges, resolved_edges, content_map)` -- Return Markdown lines for the Execution Flows section.

## readmenator/_flowlayout.py
Imported by: `readmenator/_apidocs_page.py`, `readmenator/_apidocs_render.py`, `readmenator/_app.py`, `readmenator/_flowcharts.py`, `readmenator/_flowpage.py`, `tests/test_flowcharts.py`
- `FlowGraph.node` (method) `readmenator/_flowlayout.py:117` `def node(self, node_id)` -- Return the node with *node_id*.
- `FlowGraph.to_dict` (method) `readmenator/_flowlayout.py:124` `def to_dict(self)` -- Serialise the laid-out diagram for the HTML viewer.
- `measure` (function) `readmenator/_flowlayout.py:195` `def measure(node, metrics)` -- Set the node's wrapped lines and its width and height from text metrics.
- `layout_flow` (function) `readmenator/_flowlayout.py:260` `def layout_flow(graph, metrics, direction)` -- Lay out *graph* in place and return it.
- `layout_sequence` (function) `readmenator/_flowlayout.py:414` `def layout_sequence(graph, metrics)` -- Place sequence participants as columns and messages as rows.

## readmenator/_flowpage.py
Depends on: `readmenator/_flowlayout.py`
Imported by: `readmenator/_apidocs_page.py`, `readmenator/_apidocs_render.py`, `readmenator/_app.py`, `tests/test_flowcharts.py`
- `flows_payload_json` (function) `readmenator/_flowpage.py:218` `def flows_payload_json(graphs, api_href)` -- Serialise laid-out graphs for embedding in a page (angle brackets and ampersands escaped).
- `render_flows_page` (function) `readmenator/_flowpage.py:224` `def render_flows_page(graphs, project_name, api_href)` -- Render the standalone architecture and execution-flow page.
- `flow_thumbnail_svg` (function) `readmenator/_flowpage.py:244` `def flow_thumbnail_svg(graph, width, height)` -- Render a small preview of a laid-out diagram for gallery cards.

## readmenator/_forcegraph.py
Depends on: `readmenator/_config.py`, `readmenator/_forcegraph_page.py`, `readmenator/_graphlayout.py`, `readmenator/_models.py`, `readmenator/_purpose.py`, `readmenator/_rank.py`, `readmenator/_resolver.py`, `readmenator/_sourceview.py`
Imported by: `readmenator/_bundlegraph.py`, `readmenator/_documentation.py`, `readmenator/_explorer.py`, `readmenator/_exporter.py`, `readmenator/_pipeline.py`, `tests/test_bundlegraph.py`, `tests/test_interactive_graph.py`, `tests/test_layout_quality.py`, `tests/test_sourceview.py`
- `family_color_from_name` (function) `readmenator/_forcegraph.py:38` `def family_color_from_name(name, sat_base, sat_span, light_base, light_span)` -- Derive a stable, visually-distinct HSL color from a label.
- `node_value` (function) `readmenator/_forcegraph.py:66` `def node_value(symbols, degree)` -- Scale a node value with log2 dampening.
- `ForceGraphRenderer.__init__` (method) `readmenator/_forcegraph.py:82` `def __init__(self, config)` -- Initialise with application configuration.
- `ForceGraphRenderer.node_palette` (method) `readmenator/_forcegraph.py:90` `def node_palette(self)` -- Return the node-type color palette from configuration.
- `ForceGraphRenderer.edge_palette` (method) `readmenator/_forcegraph.py:94` `def edge_palette(self)` -- Return the edge-relation color palette from configuration.
- `ForceGraphRenderer.vendor_source` (method) `readmenator/_forcegraph.py:98` `def vendor_source(self)` -- Return the path of the vendored 2D engine shipped in the package.
- `ForceGraphRenderer.vendor_href` (method) `readmenator/_forcegraph.py:106` `def vendor_href(self)` -- Return the relative vendor script href used beside the page.
- `ForceGraphRenderer.build_payload` (method) `readmenator/_forcegraph.py:111` `def build_payload(self, nodes, edges, resolved_edges, analysis, layers, findings, content_map)` -- Build a heterogeneous graph payload for the explorer.
- `file_of` (function) `readmenator/_forcegraph.py:147` `def file_of(edge_id)` -- Map a symbol-scoped edge endpoint to its file identifier.
- `add_node` (function) `readmenator/_forcegraph.py:201` `def add_node(node_id, label, node_type)` -- Insert a node unless already present.
- `ForceGraphRenderer.render` (method) `readmenator/_forcegraph.py:355` `def render(self, payload, analytics, title, home_href, live_api)` -- Render the standalone force-graph explorer HTML document.
- `ForceGraphRenderer.group_colors` (method) `readmenator/_forcegraph.py:403` `def group_colors(self, payload)` -- Return stable colors for the layer and language groupings in a payload.
- `ForceGraphRenderer.page_settings` (method) `readmenator/_forcegraph.py:426` `def page_settings(self, payload, live_api)` -- Collect the explorer page settings serialized into the HTML.
- `ForceGraphRenderer.family_color` (method) `readmenator/_forcegraph.py:502` `def family_color(self, name)` -- Return the configured stable hash color for a group name.
- `ForceGraphRenderer.thumbnail_svg` (method) `readmenator/_forcegraph.py:530` `def thumbnail_svg(self, payload)` -- Render a small ForceAtlas2 preview of the file graph as inline SVG.
- `ForceGraphRenderer.write` (method) `readmenator/_forcegraph.py:570` `def write(self, output_path, payload, analytics, title, home_href)` -- Write the explorer HTML plus the vendored engine beside it.
- `ForceGraphRenderer.copy_vendor` (method) `readmenator/_forcegraph.py:597` `def copy_vendor(self, dest_dir)` -- Copy the vendored 2D engine next to an exported page.

## readmenator/_gh_wiki.py
Depends on: `readmenator/_config.py`, `readmenator/_gitmeta.py`
Imported by: `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_gh_wiki.py`
- `GitHubWikiPublisher.__init__` (method) `readmenator/_gh_wiki.py:62` `def __init__(self, config, runner)` -- Store configuration and the subprocess runner (injectable for tests).
- `GitHubWikiPublisher.page_name` (method) `readmenator/_gh_wiki.py:72` `def page_name(self, rel_path)` -- Map a generated markdown path to its flat GitHub wiki page name.
- `GitHubWikiPublisher.collect_sources` (method) `readmenator/_gh_wiki.py:96` `def collect_sources(self, project_root)` -- List project-relative markdown sources to publish, sorted.
- `GitHubWikiPublisher.rewrite` (method) `readmenator/_gh_wiki.py:129` `def rewrite(self, text, rel_path, names, project_root, blob_base)` -- Rewrite relative doc links to wiki pages and paths to source permalinks.
- `link` (function) `readmenator/_gh_wiki.py:151` `def link(match)` -- Replace one relative markdown link when its target is published.
- `permalink` (function) `readmenator/_gh_wiki.py:164` `def permalink(match)` -- Link a backticked project file (optionally with a line) to source.
- `GitHubWikiPublisher.render` (method) `readmenator/_gh_wiki.py:179` `def render(self, project_root, remote)` -- Render every wiki page, including sidebar and footer.
- `GitHubWikiPublisher.wiki_remote` (method) `readmenator/_gh_wiki.py:249` `def wiki_remote(self, project_root)` -- Resolve the wiki remote from config, ``gh``, or the git origin.
- `GitHubWikiPublisher.publish` (method) `readmenator/_gh_wiki.py:313` `def publish(self, project_root, dry_run)` -- Render pages and push them to the GitHub wiki (or a local folder).

## readmenator/_gitmeta.py
Imported by: `readmenator/_agent_output.py`, `readmenator/_app.py`, `readmenator/_gh_wiki.py`, `readmenator/_memory.py`, `tests/test_agent_friendliness.py`
- `read_git_head` (function) `readmenator/_gitmeta.py:84` `def read_git_head(project_root)` -- Return the current commit and branch of a project, when available.

## readmenator/_graphlayout.py
Imported by: `readmenator/_bundlegraph.py`, `readmenator/_forcegraph.py`, `readmenator/_video.py`, `tests/test_graphlayout.py`, `tests/test_layout_quality.py`
- `forceatlas2_frames` (function) `readmenator/_graphlayout.py:73` `def forceatlas2_frames(ids, edges, settings)` -- Run ForceAtlas2 and return evenly spaced layout snapshots.
- `fit_frames` (function) `readmenator/_graphlayout.py:221` `def fit_frames(frames, box, margin, trim)` -- Map raw snapshots into a pixel box using the final layout's bounds.
- `interpolate_frames` (function) `readmenator/_graphlayout.py:266` `def interpolate_frames(frames, t)` -- Linear interpolation between snapshots for a progress t in [0, 1].
- `hierarchical_edge_bundling` (function) `readmenator/_graphlayout.py:374` `def hierarchical_edge_bundling(groups, edges, center, radius, beta, samples, group_gap, inner_ratio)` -- Lay leaves on a circle by group and bundle edges through the hierarchy.
- `fibonacci_sphere` (function) `readmenator/_graphlayout.py:429` `def fibonacci_sphere(count)` -- Return count nearly uniform unit vectors on a golden-angle spiral.
- `spherical_edge_bundling` (function) `readmenator/_graphlayout.py:516` `def spherical_edge_bundling(groups, edges, radius, beta, samples, inner_ratio, refine_sweeps, affinity_edges)` -- Lay leaves on a sphere in community caps and bundle edges through the hierarchy.
- `normalize_cloud` (function) `readmenator/_graphlayout.py:586` `def normalize_cloud(points, quantile, max_radius)` -- Center a 3D point cloud, scale a radius quantile to 1, and pull outliers in.
- `bundle_angular_cost` (function) `readmenator/_graphlayout.py:654` `def bundle_angular_cost(groups, edges, group_gap)` -- Total angular length of all edges for a circular group layout.
- `optimize_bundle_order` (function) `readmenator/_graphlayout.py:702` `def optimize_bundle_order(groups, edges, sweeps, passes, group_gap)` -- Reorder groups and members to shorten bundled edges (fewer crossings).
- `refine_sphere_leaves` (function) `readmenator/_graphlayout.py:804` `def refine_sphere_leaves(layout, groups, edges, sweeps)` -- Reassign leaves inside each cap so members face their neighbours.
- `chord_total` (function) `readmenator/_graphlayout.py:829` `def chord_total(leaves)` -- Sum of straight-line edge lengths.

## readmenator/_graphrag.py
Depends on: `readmenator/_analyzer.py`, `readmenator/_category.py`, `readmenator/_config.py`, `readmenator/_models.py`, `readmenator/_purpose.py`, `readmenator/_rank.py`, `readmenator/_resolver.py`
Imported by: `readmenator/_app.py`, `readmenator/_pipeline.py`, `tests/test_graphrag.py`, `tests/test_memory.py`
- `GraphRagIndex.to_dict` (method) `readmenator/_graphrag.py:186` `def to_dict(self)` -- Serialise the index into JSON-compatible primitives.
- `GraphRagIndex.from_dict` (method) `readmenator/_graphrag.py:197` `def from_dict(cls, data)` -- Rebuild an index from :meth:`to_dict` output.
- `tokenize` (function) `readmenator/_graphrag.py:240` `def tokenize(text, min_len, stopwords)` -- Split text into lowercase retrieval tokens.
- `Bm25Index.__init__` (method) `readmenator/_graphrag.py:270` `def __init__(self, documents, k1, b)` -- Index token documents.
- `Bm25Index.scores` (method) `readmenator/_graphrag.py:298` `def scores(self, query)` -- Return the BM25 score of every document for the query tokens.
- `GraphRagBuilder.__init__` (method) `readmenator/_graphrag.py:348` `def __init__(self, config)` -- Initialise with application configuration.
- `GraphRagBuilder.build` (method) `readmenator/_graphrag.py:358` `def build(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, concept_graph, content_map...` -- Build entities, relationships, text units, and community reports.
- `add_relation` (function) `readmenator/_graphrag.py:406` `def add_relation(source, target, relation, description, confidence)` -- Insert a relationship once, keyed by endpoints and relation.
- `resolve_symbol` (function) `readmenator/_graphrag.py:452` `def resolve_symbol(file_id, name)` -- Resolve a symbol name inside a file, else a globally unique name.
- `GraphRagSearcher.__init__` (method) `readmenator/_graphrag.py:945` `def __init__(self, config, index)` -- Prepare lexical indexes and the entity random-walk graph.
- `GraphRagSearcher.choose_mode` (method) `readmenator/_graphrag.py:987` `def choose_mode(self, query)` -- Pick local or global retrieval for a query.
- `GraphRagSearcher.search` (method) `readmenator/_graphrag.py:1004` `def search(self, query, mode, budget_tokens)` -- Run local, global, or automatically chosen retrieval.
- `GraphRagSearcher.local_search` (method) `readmenator/_graphrag.py:1025` `def local_search(self, query, budget_tokens)` -- Entity-centric retrieval: BM25 seeds expanded by Personalized PageRank.
- `GraphRagSearcher.global_search` (method) `readmenator/_graphrag.py:1106` `def global_search(self, query, budget_tokens)` -- Map-reduce over community reports for broad, corpus-level questions.
- `GraphRagStore.__init__` (method) `readmenator/_graphrag.py:1215` `def __init__(self, config)` -- Initialise with application configuration.
- `GraphRagStore.directory` (method) `readmenator/_graphrag.py:1223` `def directory(self, project_root)` -- Return the output directory for a project root.
- `GraphRagStore.write` (method) `readmenator/_graphrag.py:1227` `def write(self, index, project_root)` -- Write index.json, JSONL tables, and REPORTS.md.
- `GraphRagStore.load` (method) `readmenator/_graphrag.py:1257` `def load(self, project_root)` -- Load a previously written index, or None when missing or invalid.
- `GraphRagStore.render_reports` (method) `readmenator/_graphrag.py:1279` `def render_reports(index)` -- Render the community report hierarchy as greppable Markdown.

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
Imported by: `readmenator/_app.py`, `readmenator/_components.py`, `readmenator/_cursorrules_generator.py`, `readmenator/_linter.py`, `readmenator/_mcp_server.py`, `readmenator/_pipeline.py`, `tests/test_agent_friendliness.py`
- `LayerDetector.detect` (method) `readmenator/_layers.py:83` `def detect(self, nodes, edges)` -- Assign each file node to an architectural layer.
- `LayerDetector.layer_summary` (method) `readmenator/_layers.py:189` `def layer_summary(layers)` -- Count files per layer.

## readmenator/_linter.py
Depends on: `readmenator/_config.py`, `readmenator/_layers.py`, `readmenator/_models.py`, `readmenator/_symindex.py`
Imported by: `readmenator/_app.py`, `tests/test_linter.py`
- `ArchitectureLinter.__init__` (method) `readmenator/_linter.py:34` `def __init__(self, config)`
- `ArchitectureLinter.lint` (method) `readmenator/_linter.py:37` `def lint(self, nodes, edges, resolved_edges, layers, content_map)` -- Run all linter rules and return violations.


Next: [API_p2.md](API_p2.md)
