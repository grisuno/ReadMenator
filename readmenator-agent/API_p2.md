# API (page 2 of 2)
Previous: [API.md](API.md)

## readmenator/_rank.py
Depends on: `readmenator/_category.py`
Imported by: `readmenator/__init__.py`, `readmenator/_app.py`, `readmenator/_documentation.py`, `readmenator/_explain.py`, `readmenator/_forcegraph.py`, `readmenator/_graphrag.py`, `readmenator/_pipeline.py`, `readmenator/_query.py`, `readmenator/_video.py`, `tests/test_ranking.py`
- `RankConfig.global_pagerank` (method) `readmenator/_rank.py:61` `def global_pagerank(graph, alpha, max_iter, tolerance)` -- Compute global PageRank on the typed weighted graph.
- `RankConfig.file_pagerank` (method) `readmenator/_rank.py:119` `def file_pagerank(file_ids, edges, alpha, max_iter, tolerance)` -- Directed PageRank over file-to-file dependency pairs.
- `RankConfig.personalized_pagerank` (method) `readmenator/_rank.py:153` `def personalized_pagerank(graph, seeds, alpha, max_iter, tolerance)` -- Compute Personalized PageRank with a seed-node preference vector.
- `RankConfig.hits` (method) `readmenator/_rank.py:223` `def hits(graph, max_iter, tolerance)` -- Compute HITS (Hyperlink-Induced Topic Search) authorities and hubs.
- `RankConfig.build_seeds_from_query` (method) `readmenator/_rank.py:274` `def build_seeds_from_query(query, node_ids, node_labels, symbols)` -- Build a PPR seed vector from a natural-language query string.
- `RankConfig.build_seeds_for_context` (method) `readmenator/_rank.py:320` `def build_seeds_for_context(node_ids, anchor_patterns)` -- Build a PPR seed vector from anchor pattern strings.
- `RankedItem.label` (method) `readmenator/_rank.py:378` `def label(self)`
- `RankedResult.top` (method) `readmenator/_rank.py:400` `def top(self, n)`
- `RankedResult.explain` (method) `readmenator/_rank.py:403` `def explain(self, node_id)` -- Return a human-readable explanation of why *node_id* ranks as it does.
- `CompositeRanker.__init__` (method) `readmenator/_rank.py:419` `def __init__(self, graph, config)`
- `CompositeRanker.rank` (method) `readmenator/_rank.py:438` `def rank(self, query, seeds, category, node_ids, test_coverage, doc_coverage, freshness)` -- Compute composite ranking for a query.

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

## readmenator/_skill_installer.py
Depends on: `readmenator/_config.py`
Imported by: `readmenator/_pipeline.py`, `tests/test_memory.py`
- `SkillInstaller.__init__` (method) `readmenator/_skill_installer.py:25` `def __init__(self, config)` -- Initialise with application configuration.
- `SkillInstaller.source_dir` (method) `readmenator/_skill_installer.py:34` `def source_dir()` -- Return the packaged skills directory.
- `SkillInstaller.available` (method) `readmenator/_skill_installer.py:38` `def available(self)` -- Return the names of the packaged skills, sorted.
- `SkillInstaller.target_dir` (method) `readmenator/_skill_installer.py:48` `def target_dir(self, project_root, target)` -- Resolve the destination skills directory.
- `SkillInstaller.install` (method) `readmenator/_skill_installer.py:61` `def install(self, project_root, target)` -- Write every packaged skill whose content changed.
- `SkillInstaller.maybe_install_on_run` (method) `readmenator/_skill_installer.py:87` `def maybe_install_on_run(self, project_root)` -- Install during run() only when the project already uses agent skills.

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
- `ease` (function) `readmenator/_video.py:95` `def ease(x)` -- Smoothstep clamped to [0, 1].
- `fmt_int` (function) `readmenator/_video.py:101` `def fmt_int(n)` -- Group thousands with commas.
- `mix` (function) `readmenator/_video.py:106` `def mix(a, b, t)` -- Linear blend of two RGB colors.
- `alpha` (function) `readmenator/_video.py:111` `def alpha(c, a)` -- RGB color plus an alpha in [0, 1] as an RGBA tuple.
- `hash_color` (function) `readmenator/_video.py:116` `def hash_color(digest)` -- Neon color derived from a digest: the file fingerprint.
- `short_label` (function) `readmenator/_video.py:125` `def short_label(text, limit)` -- Truncate a label to a character budget without newlines.
- `community_color` (function) `readmenator/_video.py:170` `def community_color(index)` -- Neon color for a community index (grey for unassigned).
- `project3d` (function) `readmenator/_video.py:188` `def project3d(p, yaw, pitch, target, scale, center, perspective)` -- Project a 3D point through an orbiting perspective camera.
- `mode_color` (function) `readmenator/_video.py:227` `def mode_color(data, nid, mode)` -- Node color under an explorer color mode (community, layer, language).
- `draw_cloud3d` (function) `readmenator/_video.py:276` `def draw_cloud3d(img, data, box, cfg, yaw, pitch, target, zoom, mode, lit_nodes, edge_lit, gt, fonts, appear, labels)` -- Draw the 3D force graph (graph-force 3D view) through an orbiting camera.
- `draw_sphere3d` (function) `readmenator/_video.py:396` `def draw_sphere3d(img, data, box, cfg, yaw, pitch, morph, reveal, spot, gt, fonts, group_labels)` -- Draw the bundled sphere, optionally morphing out of the 3D force layout.
- `pr` (method) `readmenator/_video.py:463` `def pr(p)` -- Project a layout point through the scene camera.
- `dependencies_available` (function) `readmenator/_video.py:560` `def dependencies_available()` -- Check that PIL and ffmpeg exist for video rendering.
- `resolve_fonts` (function) `readmenator/_video.py:569` `def resolve_fonts()` -- Resolve monospace fonts through fontconfig with PIL fallback.
- `Backdrop.__init__` (method) `readmenator/_video.py:611` `def __init__(self, width, height)` -- Build the gradient sky, star field, sun and CRT mask.
- `Backdrop.draw_grid` (method) `readmenator/_video.py:671` `def draw_grid(img, t, strength, bd)` -- Draw the scrolling perspective grid below the horizon.
- `Backdrop.draw_sun` (method) `readmenator/_video.py:691` `def draw_sun(img, a, bd, cy)` -- Paste the striped synthwave sun behind the horizon.
- `Backdrop.post` (method) `readmenator/_video.py:708` `def post(img, glitch, seed)` -- Apply bloom, scanlines, vignette and optional glitch.
- `Backdrop.glitch_fx` (method) `readmenator/_video.py:726` `def glitch_fx(img, amount, seed)` -- RGB split plus horizontal slice displacement.
- `Backdrop.chroma_text` (method) `readmenator/_video.py:749` `def chroma_text(img, xy, text, font, col, spread, anchor)` -- Draw text with red/cyan CRT chromatic aberration.
- `Backdrop.hud_panel` (method) `readmenator/_video.py:760` `def hud_panel(d, box, title, fonts, col)` -- Draw a translucent HUD panel with neon edge and corner brackets.
- `Backdrop.draw_header` (method) `readmenator/_video.py:773` `def draw_header(img, d, gt, total, project, act_label, fonts, width)` -- Draw the top strip with project title, act label and progress.
- `Backdrop.draw_caption` (method) `readmenator/_video.py:787` `def draw_caption(d, text, lt, dur, fonts, width, y)` -- Draw the lower-third narration line with typing effect.
- `CinematicVideoRenderer.collect` (method) `readmenator/_video.py:808` `def collect(self, nodes, edges, resolved_edges, analysis, layers, findings, analysis_v2, project_name, content_map...` -- Collect every number each scene draws, from real scan data.
- `CinematicVideoRenderer.build_scenes` (method) `readmenator/_video.py:1023` `def build_scenes(self, data)` -- Lay every scene on the global clock.
- `CinematicVideoRenderer.graph_positions` (method) `readmenator/_video.py:1052` `def graph_positions(self, data, box)` -- Compute deterministic positions for graph nodes inside a box.
- `CinematicVideoRenderer.tree_positions` (method) `readmenator/_video.py:1099` `def tree_positions(self, data, box)` -- Place the full BFS tree radially: root in the center, one ring per depth.
- `CinematicVideoRenderer.emergence_frames` (method) `readmenator/_video.py:1142` `def emergence_frames(self, data, box)` -- ForceAtlas2 snapshots of the resolved import graph fitted to a pixel box.
- `CinematicVideoRenderer.bundle_groups` (method) `readmenator/_video.py:1152` `def bundle_groups(self, data)` -- Group graph files by community (hubs first), unassigned files last.
- `CinematicVideoRenderer.bundle_layout` (method) `readmenator/_video.py:1167` `def bundle_layout(self, data, box)` -- Hierarchical edge bundling of resolved imports grouped by community.
- `CinematicVideoRenderer.orbit_positions` (method) `readmenator/_video.py:1176` `def orbit_positions(self, data)` -- 3D ForceAtlas2 layout of the graph, centered and scaled to the unit sphere.
- `CinematicVideoRenderer.sphere_layout` (method) `readmenator/_video.py:1186` `def sphere_layout(self, data)` -- Spherical edge bundling of resolved imports on community caps.
- `CinematicVideoRenderer.orbit_stops` (method) `readmenator/_video.py:1194` `def orbit_stops(self, data, positions)` -- Camera tour stops: the largest communities with their 3D centroid.
- `CinematicVideoRenderer.render_single_frame` (method) `readmenator/_video.py:1223` `def render_single_frame(self, data, frame_index)` -- Render one frame to raw RGB bytes without touching ffmpeg.
- `CinematicVideoRenderer.render` (method) `readmenator/_video.py:1237` `def render(self, data, output_path)` -- Render all frames and encode to mp4, muxing music if configured.

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
- `WikiGenerator.dominant` (method) `readmenator/_wiki.py:428` `def dominant(ids, key)`

## readmenator/_yaralite.py
Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`
- `YaraLiteRule.tier` (method) `readmenator/_yaralite.py:42` `def tier(self)` -- Return the rule tier from meta or name prefix.
- `YaraLiteMatch.parse_yaralite_rules` (method) `readmenator/_yaralite.py:76` `def parse_yaralite_rules(rules_text)` -- Parse YARA-lite rules text into rules and error messages.
- `YaraLiteMatch.run_yaralite_rules` (method) `readmenator/_yaralite.py:112` `def run_yaralite_rules(text, rules)` -- Run parsed rules against a scan-text blob.
- `YaraLiteMatch.validate_yaralite_rules` (method) `readmenator/_yaralite.py:139` `def validate_yaralite_rules(rules_text)` -- Validate rules text and summarize tier counts.
- `YaraLiteMatch.replace_group` (method) `readmenator/_yaralite.py:270` `def replace_group(match)` -- Replace an N-of group with its boolean outcome.
- `YaraLiteMatch.replace_identifier` (method) `readmenator/_yaralite.py:292` `def replace_identifier(match)` -- Replace a string identifier with its hit boolean.

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
- `TestOrchestrator.parse_arguments` (method) `readmenator_orchestrator.py:481` `def parse_arguments()`
- `TestOrchestrator.main` (method) `readmenator_orchestrator.py:498` `def main()`

