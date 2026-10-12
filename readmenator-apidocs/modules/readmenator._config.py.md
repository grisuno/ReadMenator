# `readmenator._config`

> Source: [readmenator/_config.py:1](../../readmenator/_config.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Immutable configuration dataclass for readmenator.

All tuneable parameters live here as frozen dataclass fields. No magic
numbers or hardcoded paths exist elsewhere in the codebase. Derived
consumers import Config and read values from an instance.

## Contents

- **Classes:** [`Config`](#config)

## Classes

<a id="config"></a>

### `Config`

`class` `dataclass` | [readmenator/_config.py:15](../../readmenator/_config.py#L15)

Decorators: `@dataclass(frozen=True)`

```python
class Config
```

Single source of truth for all readmenator settings.

Every tuneable constant -- file-size limits, directory depth,
supported extensions, symbol pluralisation map, Mermaid style
tokens, graph analysis thresholds, and export settings -- is
defined here and consumed by reference elsewhere.

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`IGNORE_DIRS`](#config-ignore_dirs) | `Tuple[str, ...]` | `('.git', '__pycache__', 'venv', '.venv', 'env', '.env', 'node_modules', '.tox', '.eggs', '.pytest_cache', 'build', 'dist', '.idea', '.vscode', 'target', 'bin', 'obj', 'out', 'vendor', 'third_party', 'deps', 'third-party', 'thirdparty', '.m2', '.gradle', '.nuget', 'packages', 'Pods', '.dart_tool', '.pub-cache', 'bower_components', '.yarn', 'Carthage', 'node_packages', '.meteor', '.gitlab', '.github', 'htmlcov', '.coverage', '__pycache__')` |  |
| [`OUTPUT_FILENAME`](#config-output_filename) | `str` | `'KNOWLEDGE_BASE.md'` |  |
| [`MAX_FILE_SIZE_MB`](#config-max_file_size_mb) | `float` | `10.0` |  |
| [`MAX_DIRECTORY_DEPTH`](#config-max_directory_depth) | `int` | `20` |  |
| [`DOCSTRING_LOOKBACK_LINES`](#config-docstring_lookback_lines) | `int` | `15` |  |
| [`FILE_HEADER_MAX_LINES`](#config-file_header_max_lines) | `int` | `30` |  |
| [`MERMAID_MAX_NODES`](#config-mermaid_max_nodes) | `int` | `300` |  |
| [`MERMAID_MAX_SYMBOLS_PER_FILE`](#config-mermaid_max_symbols_per_file) | `int` | `5` |  |
| [`MERMAID_MAX_EDGES`](#config-mermaid_max_edges) | `int` | `480` |  |
| [`MERMAID_MAX_INTERNAL_EDGES`](#config-mermaid_max_internal_edges) | `int` | `100` |  |
| [`MERMAID_GRID_COLUMNS`](#config-mermaid_grid_columns) | `int` | `6` |  |
| [`MERMAID_MAX_EXTERNALS`](#config-mermaid_max_externals) | `int` | `24` |  |
| [`MERMAID_DIRECTION`](#config-mermaid_direction) | `str` | `'LR'` |  |
| [`UML_CLASSES_PER_DIAGRAM`](#config-uml_classes_per_diagram) | `int` | `6` |  |
| [`MERMAID_MODULE_STYLE`](#config-mermaid_module_style) | `str` | `'fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff'` |  |
| [`MERMAID_CLASS_STYLE`](#config-mermaid_class_style) | `str` | `'fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff'` |  |
| [`MERMAID_FUNCTION_STYLE`](#config-mermaid_function_style) | `str` | `'fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa'` |  |
| [`MERMAID_EXTERNAL_STYLE`](#config-mermaid_external_style) | `str` | `'fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa'` |  |
| [`MERMAID_INTERNAL_EDGE_STYLE`](#config-mermaid_internal_edge_style) | `str` | `'stroke:#88aaff,stroke-width:1px'` |  |
| [`SUPPORTED_EXTENSIONS`](#config-supported_extensions) | `Tuple[str, ...]` | `('.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hxx', '.hh', '.h++', '.tcc', '.inl', '.inc', '.i', '.C', '.py', '.go', '.rs', '.js', '.ts', '.jsx', '.tsx', '.java', '.cs', '.sh', '.bash', '.zsh', '.php', '.dart', '.gd', '.nim', '.asm', '.s', '.S', '.rb', '.swift', '.kt', '.kts', '.scala', '.sc', '.lua', '.ex', '.exs')` |  |
| [`SCAN_MODE`](#config-scan_mode) | `str` | `'default'` |  |
| [`SCAN_INCLUDE_DIRS`](#config-scan_include_dirs) | `Tuple[str, ...]` | `()` |  |
| [`SCAN_EXCLUDE_PATTERNS`](#config-scan_exclude_patterns) | `Tuple[str, ...]` | `()` |  |
| [`KB_TITLE`](#config-kb_title) | `str` | `'Polyglot Codebase Knowledge Graph'` |  |
| [`KB_HERO_ENABLED`](#config-kb_hero_enabled) | `bool` | `True` |  |
| [`KB_MERMAID_THEME`](#config-kb_mermaid_theme) | `str` | `'dark'` |  |
| [`SITE_ENABLED`](#config-site_enabled) | `bool` | `True` |  |
| [`SITE_DIR`](#config-site_dir) | `str` | `'readmenator-site'` |  |
| [`SITE_VIDEO_ENABLED`](#config-site_video_enabled) | `bool` | `True` |  |
| [`SITE_VIDEO_FILENAME`](#config-site_video_filename) | `str` | `'readmenator.mp4'` |  |
| [`SITE_DOCS_ENABLED`](#config-site_docs_enabled) | `bool` | `True` |  |
| [`SITE_DOCS_SUBDIR`](#config-site_docs_subdir) | `str` | `'md'` |  |
| [`SITE_MAX_DOCS`](#config-site_max_docs) | `int` | `60` |  |
| [`SITE_MD_PREVIEW_CHARS`](#config-site_md_preview_chars) | `int` | `160` |  |
| [`SITE_MD_PREVIEW_MIN_CHARS`](#config-site_md_preview_min_chars) | `int` | `24` |  |
| [`SITE_VIDEO_POSTER_FILENAME`](#config-site_video_poster_filename) | `str` | `'readmenator-poster.jpg'` |  |
| [`SITE_VIDEO_POSTER_AT_S`](#config-site_video_poster_at_s) | `float` | `6.0` |  |
| [`SITE_VIDEO_POSTER_QUALITY`](#config-site_video_poster_quality) | `int` | `3` |  |
| [`SITE_VIDEO_POSTER_TIMEOUT_S`](#config-site_video_poster_timeout_s) | `int` | `60` |  |
| [`SITE_LLMS_TXT_ENABLED`](#config-site_llms_txt_enabled) | `bool` | `True` |  |
| [`SITE_REFRESH_ON_REBUILD`](#config-site_refresh_on_rebuild) | `bool` | `True` |  |
| [`SITE_LLMS_TXT_FILENAME`](#config-site_llms_txt_filename) | `str` | `'llms.txt'` |  |
| [`SITE_GITHUB_URL`](#config-site_github_url) | `str` | `'https://github.com/grisuno/ReadMenator'` |  |
| [`SITE_PYPI_URL`](#config-site_pypi_url) | `str` | `'https://pypi.org/project/readmenator/'` |  |
| [`GENERATED_FILE_PREFIXES`](#config-generated_file_prefixes) | `Tuple[str, ...]` | `('.refactor_',)` |  |
| [`SKIP_GENERATED_OUTPUTS`](#config-skip_generated_outputs) | `bool` | `True` |  |
| [`SYMBOL_TYPE_PLURALS`](#config-symbol_type_plurals) | `Tuple[Tuple[str, str], ...]` | `(('class', 'classes'), ('struct', 'structs'), ('function', 'functions'), ('method', 'methods'), ('macro', 'macros'), ('trait', 'traits'), ('enum', 'enums'), ('interface', 'interfaces'), ('record', 'records'), ('variable', 'variables'), ('constant', 'constants'), ('type_alias', 'type_aliases'), ('module', 'modules'), ('protocol', 'protocols'), ('extension', 'extensions'))` |  |
| [`COMMUNITY_MIN_SIZE`](#config-community_min_size) | `int` | `2` |  |
| [`COMMUNITY_MAX_SIZE_RATIO`](#config-community_max_size_ratio) | `float` | `0.25` |  |
| [`GOD_NODE_TOP_N`](#config-god_node_top_n) | `int` | `10` |  |
| [`COMMUNITY_HUB_DAMPING`](#config-community_hub_damping) | `bool` | `True` |  |
| [`COMMUNITY_VOTE_EPSILON`](#config-community_vote_epsilon) | `float` | `1e-09` |  |
| [`COMMUNITY_MERGE_BELOW`](#config-community_merge_below) | `int` | `3` |  |
| [`COMMUNITY_ALGORITHM`](#config-community_algorithm) | `str` | `'louvain'` |  |
| [`COMMUNITY_RESOLUTION`](#config-community_resolution) | `float` | `1.0` |  |
| [`COMMUNITY_MAX_LEVELS`](#config-community_max_levels) | `int` | `10` |  |
| [`COMMUNITY_MAX_SWEEPS`](#config-community_max_sweeps) | `int` | `50` |  |
| [`SURPRISING_CONNECTION_HOP_THRESHOLD`](#config-surprising_connection_hop_threshold) | `int` | `3` |  |
| [`SURPRISING_CONNECTION_TOP_N`](#config-surprising_connection_top_n) | `int` | `5` |  |
| [`SUGGESTED_QUESTIONS_COUNT`](#config-suggested_questions_count) | `int` | `5` |  |
| [`CACHE_DIR`](#config-cache_dir) | `str` | `'.readmenator_cache'` |  |
| [`HTML_TEMPLATE_STYLE`](#config-html_template_style) | `str` | `'dark'` |  |
| [`SVG_DPI`](#config-svg_dpi) | `int` | `150` |  |
| [`SVG_MAX_NODES`](#config-svg_max_nodes) | `int` | `200` |  |
| [`PROGRESS_REPORT_BATCH`](#config-progress_report_batch) | `int` | `50` |  |
| [`SECURITY_ENABLED`](#config-security_enabled) | `bool` | `False` |  |
| [`SECURITY_SEVERITY_THRESHOLD`](#config-security_severity_threshold) | `str` | `'medium'` |  |
| [`SECURITY_OUTPUT`](#config-security_output) | `str` | `'KNOWLEDGE_BASE.md'` |  |
| [`CPG_ENABLED`](#config-cpg_enabled) | `bool` | `True` |  |
| [`CPG_CONTEXT`](#config-cpg_context) | `str` | `''` |  |
| [`CPG_EMBED_IN_KNOWLEDGE_BASE`](#config-cpg_embed_in_knowledge_base) | `bool` | `True` |  |
| [`TAINT_ENABLED`](#config-taint_enabled) | `bool` | `True` |  |
| [`TAINT_MAX_DEPTH`](#config-taint_max_depth) | `int` | `10` |  |
| [`TAINT_MAX_PATHS`](#config-taint_max_paths) | `int` | `20` |  |
| [`SARIF_ENABLED`](#config-sarif_enabled) | `bool` | `False` |  |
| [`SARIF_OUTPUT`](#config-sarif_output) | `str` | `'readmenator_audit.sarif'` |  |
| [`HOTSPOTS_ENABLED`](#config-hotspots_enabled) | `bool` | `True` |  |
| [`HOTSPOT_COMPLEXITY_WEIGHT`](#config-hotspot_complexity_weight) | `float` | `0.4` |  |
| [`HOTSPOT_CENTRALITY_WEIGHT`](#config-hotspot_centrality_weight) | `float` | `0.6` |  |
| [`CYCLE_DETECTION_ENABLED`](#config-cycle_detection_enabled) | `bool` | `True` |  |
| [`CHANGE_IMPACT_MAX_DEPTH`](#config-change_impact_max_depth) | `int` | `10` |  |
| [`CHANGE_IMPACT_MAX_FILES`](#config-change_impact_max_files) | `int` | `50` |  |
| [`RULE_GEN_ENABLED`](#config-rule_gen_enabled) | `bool` | `True` |  |
| [`RULE_GEN_MIN_PATTERN_COUNT`](#config-rule_gen_min_pattern_count) | `int` | `3` |  |
| [`RULE_GEN_OUTPUT_DIR`](#config-rule_gen_output_dir) | `str` | `'readmenator-rules'` |  |
| [`LAYER_VIOLATION_ENABLED`](#config-layer_violation_enabled) | `bool` | `True` |  |
| [`LAYER_VIOLATION_STRICT_MODE`](#config-layer_violation_strict_mode) | `bool` | `False` |  |
| [`PRIVACY_MODE`](#config-privacy_mode) | `bool` | `False` |  |
| [`GITIGNORE_AWARE`](#config-gitignore_aware) | `bool` | `True` |  |
| [`CONTEXT_BUDGET`](#config-context_budget) | `int` | `0` |  |
| [`RANKING_ENABLED`](#config-ranking_enabled) | `bool` | `True` |  |
| [`RANKING_ALPHA`](#config-ranking_alpha) | `float` | `0.85` |  |
| [`RANKING_MAX_ITER`](#config-ranking_max_iter) | `int` | `100` |  |
| [`RANKING_TOLERANCE`](#config-ranking_tolerance) | `float` | `1e-06` |  |
| [`RANKING_TOP_N`](#config-ranking_top_n) | `int` | `10` |  |
| [`RANKING_NOISE_PENALTY`](#config-ranking_noise_penalty) | `float` | `0.7` |  |
| [`RANKING_PPR_WEIGHT`](#config-ranking_ppr_weight) | `float` | `0.45` |  |
| [`RANKING_AUTHORITY_WEIGHT`](#config-ranking_authority_weight) | `float` | `0.2` |  |
| [`RANKING_TEST_WEIGHT`](#config-ranking_test_weight) | `float` | `0.15` |  |
| [`RANKING_DOC_WEIGHT`](#config-ranking_doc_weight) | `float` | `0.1` |  |
| [`RANKING_FRESHNESS_WEIGHT`](#config-ranking_freshness_weight) | `float` | `0.1` |  |
| [`UML_ENABLED`](#config-uml_enabled) | `bool` | `True` |  |
| [`UML_MAX_CLASSES`](#config-uml_max_classes) | `int` | `50` |  |
| [`UML_GENERATED_LANGUAGES`](#config-uml_generated_languages) | `Tuple[str, ...]` | `('cpp', 'java', 'csharp', 'python', 'go', 'rust', 'php', 'kotlin', 'scala', 'swift', 'dart', 'ruby')` |  |
| [`README_INJECTION_ENABLED`](#config-readme_injection_enabled) | `bool` | `True` |  |
| [`LINTER_ENABLED`](#config-linter_enabled) | `bool` | `True` |  |
| [`LINTER_MAX_LINES`](#config-linter_max_lines) | `int` | `300` |  |
| [`LINTER_CROSS_LAYER_VIOLATIONS`](#config-linter_cross_layer_violations) | `bool` | `True` |  |
| [`DEAD_CODE_ENABLED`](#config-dead_code_enabled) | `bool` | `True` |  |
| [`DEAD_CODE_ENTRY_POINTS`](#config-dead_code_entry_points) | `Tuple[str, ...]` | `('main', 'app', 'index', '__init__')` |  |
| [`DEAD_CODE_QUARANTINE_DIR`](#config-dead_code_quarantine_dir) | `str` | `'.readmenator_trash'` |  |
| [`CURSORRULES_ENABLED`](#config-cursorrules_enabled) | `bool` | `True` |  |
| [`CURSORRULES_OUTPUT`](#config-cursorrules_output) | `str` | `'.cursorrules'` |  |
| [`REFACTORIZER_ENABLED`](#config-refactorizer_enabled) | `bool` | `True` |  |
| [`REFACTORIZER_MIN_LINES`](#config-refactorizer_min_lines) | `int` | `300` |  |
| [`REFACTORIZER_MAX_FILES`](#config-refactorizer_max_files) | `int` | `10` |  |
| [`REFACTORIZER_SCRIPT_PREFIX`](#config-refactorizer_script_prefix) | `str` | `'.refactor_'` |  |
| [`AGENT_INJECTION_ENABLED`](#config-agent_injection_enabled) | `bool` | `True` |  |
| [`AGENT_INJECTION_KB_FILENAME`](#config-agent_injection_kb_filename) | `str` | `'KNOWLEDGE_BASE.md'` |  |
| [`AGENT_OUTPUT_ENABLED`](#config-agent_output_enabled) | `bool` | `True` |  |
| [`AGENT_OUTPUT_DIR`](#config-agent_output_dir) | `str` | `'readmenator-agent'` |  |
| [`AGENT_OUTPUT_MIN_SUBSYSTEM_FILES`](#config-agent_output_min_subsystem_files) | `int` | `2` |  |
| [`AGENT_OUTPUT_MAX_LINES`](#config-agent_output_max_lines) | `int` | `500` |  |
| [`AGENT_PURPOSE_MAX_CHARS`](#config-agent_purpose_max_chars) | `int` | `100` |  |
| [`AGENT_DOC_MAX_CHARS`](#config-agent_doc_max_chars) | `int` | `120` |  |
| [`AGENT_SIGNATURE_MAX_CHARS`](#config-agent_signature_max_chars) | `int` | `120` |  |
| [`AGENT_GOTCHAS_TOP_N`](#config-agent_gotchas_top_n) | `int` | `10` |  |
| [`AGENT_GOTCHAS_EXCLUDE_LAYERS`](#config-agent_gotchas_exclude_layers) | `Tuple[str, ...]` | `('testing',)` |  |
| [`AGENT_API_PUBLIC_ONLY`](#config-agent_api_public_only) | `bool` | `True` |  |
| [`AGENT_API_EXCLUDE_LAYERS`](#config-agent_api_exclude_layers) | `Tuple[str, ...]` | `('testing',)` |  |
| [`AGENT_CHARS_PER_TOKEN`](#config-agent_chars_per_token) | `int` | `4` |  |
| [`AGENT_ENTRYPOINT_FILENAMES`](#config-agent_entrypoint_filenames) | `Tuple[str, ...]` | `('__main__.py', 'main.py', 'cli.py', 'app.py', 'manage.py', 'main.c', 'main.cpp', 'main.cc', 'kernel.c', 'main.go', 'main.rs', 'lib.rs', 'index.js', 'index.ts', 'server.js', 'server.ts', 'Main.java', 'Program.cs', 'main.dart', 'main.swift', 'Main.kt')` |  |
| [`WIKI_ENABLED`](#config-wiki_enabled) | `bool` | `True` |  |
| [`WIKI_OUTPUT_DIR`](#config-wiki_output_dir) | `str` | `'readmenator-wiki'` |  |
| [`WIKI_MAX_FILES_PER_PAGE`](#config-wiki_max_files_per_page) | `int` | `20` |  |
| [`WIKI_MAX_SYMBOLS_PER_PAGE`](#config-wiki_max_symbols_per_page) | `int` | `30` |  |
| [`WIKI_MAX_CONNECTIONS`](#config-wiki_max_connections) | `int` | `20` |  |
| [`GH_WIKI_ENABLED`](#config-gh_wiki_enabled) | `bool` | `True` |  |
| [`GH_WIKI_REMOTE`](#config-gh_wiki_remote) | `str` | `''` |  |
| [`GH_WIKI_GIT_REMOTE_NAME`](#config-gh_wiki_git_remote_name) | `str` | `'origin'` |  |
| [`GH_WIKI_HOME_PAGE`](#config-gh_wiki_home_page) | `str` | `'Home'` |  |
| [`GH_WIKI_KB_PAGE`](#config-gh_wiki_kb_page) | `str` | `'Knowledge-Base'` |  |
| [`GH_WIKI_AGENT_PREFIX`](#config-gh_wiki_agent_prefix) | `str` | `'Agent-'` |  |
| [`GH_WIKI_RECIPE_PREFIX`](#config-gh_wiki_recipe_prefix) | `str` | `'Recipe-'` |  |
| [`GH_WIKI_INCLUDE_KB`](#config-gh_wiki_include_kb) | `bool` | `True` |  |
| [`GH_WIKI_PERMALINKS`](#config-gh_wiki_permalinks) | `bool` | `True` |  |
| [`GH_WIKI_STATE_FILE`](#config-gh_wiki_state_file) | `str` | `'.readmenator-pages'` |  |
| [`GH_WIKI_DRY_RUN_DIR`](#config-gh_wiki_dry_run_dir) | `str` | `'readmenator-ghwiki'` |  |
| [`GH_WIKI_TIMEOUT_S`](#config-gh_wiki_timeout_s) | `int` | `120` |  |
| [`GH_WIKI_COMMIT_MESSAGE`](#config-gh_wiki_commit_message) | `str` | `'docs(wiki): regenerate from readmenator'` |  |
| [`WIKI_LARGE_FILE_KB`](#config-wiki_large_file_kb) | `int` | `256` |  |
| [`DATAFLOW_ENABLED`](#config-dataflow_enabled) | `bool` | `True` |  |
| [`DATAFLOW_MAX_ISSUES`](#config-dataflow_max_issues) | `int` | `50` |  |
| [`DIAGRAM_ENABLED`](#config-diagram_enabled) | `bool` | `True` |  |
| [`DIAGRAM_FULL_MODE`](#config-diagram_full_mode) | `bool` | `False` |  |
| [`DIAGRAM_MAX_NODES`](#config-diagram_max_nodes) | `int` | `60` |  |
| [`DIAGRAM_MAX_EDGES`](#config-diagram_max_edges) | `int` | `120` |  |
| [`DIAGRAM_NODE_WIDTH`](#config-diagram_node_width) | `int` | `190` |  |
| [`DIAGRAM_NODE_HEIGHT`](#config-diagram_node_height) | `int` | `64` |  |
| [`DIAGRAM_COLUMN_GAP`](#config-diagram_column_gap) | `int` | `90` |  |
| [`DIAGRAM_ROW_GAP`](#config-diagram_row_gap) | `int` | `48` |  |
| [`DIAGRAM_CANVAS_WIDTH`](#config-diagram_canvas_width) | `int` | `1280` |  |
| [`DIAGRAM_CANVAS_HEIGHT`](#config-diagram_canvas_height) | `int` | `760` |  |
| [`DIAGRAM_PRESET`](#config-diagram_preset) | `str` | `'classic'` |  |
| [`DIAGRAM_THEME`](#config-diagram_theme) | `str` | `'dark'` |  |
| [`DIAGRAM_OUTPUT_DIR`](#config-diagram_output_dir) | `str` | `'readmenator-maps'` |  |
| [`DIAGRAM_PAGES_DIR`](#config-diagram_pages_dir) | `str` | `'docs'` |  |
| [`DIAGRAM_MAPS_SUBDIR`](#config-diagram_maps_subdir) | `str` | `'maps'` |  |
| [`DIAGRAM_VIS_ENABLED`](#config-diagram_vis_enabled) | `bool` | `True` |  |
| [`DIAGRAM_VIS_CDN_JS`](#config-diagram_vis_cdn_js) | `str` | `'https://unpkg.com/vis-network@9/standalone/umd/vis-network.min.js'` |  |
| [`DIAGRAM_VIS_CDN_CSS`](#config-diagram_vis_cdn_css) | `str` | `'https://unpkg.com/vis-network@9/styles/vis-network.min.css'` |  |
| [`DIAGRAM_VIS_PHYSICS_ENABLED`](#config-diagram_vis_physics_enabled) | `bool` | `True` |  |
| [`DIAGRAM_VIS_STABILIZE_ITERATIONS`](#config-diagram_vis_stabilize_iterations) | `int` | `250` |  |
| [`DIAGRAM_VIS_GRAVITY`](#config-diagram_vis_gravity) | `float` | `-90.0` |  |
| [`DIAGRAM_VIS_CENTRAL_GRAVITY`](#config-diagram_vis_central_gravity) | `float` | `0.012` |  |
| [`DIAGRAM_VIS_SPRING_LENGTH`](#config-diagram_vis_spring_length) | `float` | `120.0` |  |
| [`DIAGRAM_VIS_SPRING_CONSTANT`](#config-diagram_vis_spring_constant) | `float` | `0.06` |  |
| [`DIAGRAM_VIS_DAMPING`](#config-diagram_vis_damping) | `float` | `0.55` |  |
| [`DIAGRAM_VIS_AVOID_OVERLAP`](#config-diagram_vis_avoid_overlap) | `float` | `0.6` |  |
| [`DIAGRAM_VIS_LABEL_TOP_N`](#config-diagram_vis_label_top_n) | `int` | `25` |  |
| [`DIAGRAM_MOTION_ENABLED`](#config-diagram_motion_enabled) | `bool` | `True` |  |
| [`DIAGRAM_SHARE_WIDTH`](#config-diagram_share_width) | `int` | `1200` |  |
| [`DIAGRAM_SHARE_HEIGHT`](#config-diagram_share_height) | `int` | `630` |  |
| [`DIAGRAM_MAX_VIEWS`](#config-diagram_max_views) | `int` | `5` |  |
| [`DIAGRAM_MAX_LABEL_CHARS`](#config-diagram_max_label_chars) | `int` | `28` |  |
| [`DIAGRAM_MARGIN_X`](#config-diagram_margin_x) | `int` | `40` |  |
| [`DIAGRAM_MARGIN_Y`](#config-diagram_margin_y) | `int` | `40` |  |
| [`DIAGRAM_MIN_GAP`](#config-diagram_min_gap) | `int` | `12` |  |
| [`DIAGRAM_LANE_TOP`](#config-diagram_lane_top) | `int` | `90` |  |
| [`DIAGRAM_SEQUENCE_TOP`](#config-diagram_sequence_top) | `int` | `110` |  |
| [`DIAGRAM_SEQUENCE_MAX_PARTICIPANTS`](#config-diagram_sequence_max_participants) | `int` | `8` |  |
| [`DIAGRAM_WORKFLOW_FALLBACK_NODES`](#config-diagram_workflow_fallback_nodes) | `int` | `4` |  |
| [`DIAGRAM_CHAPTER_FOCUS`](#config-diagram_chapter_focus) | `int` | `6` |  |
| [`DIAGRAM_MAP_SYMBOLS_PER_NODE`](#config-diagram_map_symbols_per_node) | `int` | `25` |  |
| [`DIAGRAM_TOOLTIP_DOC_CHARS`](#config-diagram_tooltip_doc_chars) | `int` | `160` |  |
| [`DIAGRAM_NEIGHBOR_NAMES`](#config-diagram_neighbor_names) | `int` | `8` |  |
| [`DIAGRAM_PRESETS`](#config-diagram_presets) | `Tuple[str, ...]` | `('classic', 'flow', 'blueprint', 'editorial')` |  |
| [`DIAGRAM_KINDS`](#config-diagram_kinds) | `Tuple[str, ...]` | `('architecture', 'workflow', 'sequence', 'dataflow', 'lifecycle')` |  |
| [`DIAGRAM_ROLES`](#config-diagram_roles) | `Tuple[str, ...]` | `('frontend', 'backend', 'database', 'cloud', 'security', 'messagebus', 'external', 'core', 'test')` |  |
| [`DIAGRAM_ROLE_COLORS`](#config-diagram_role_colors) | `Tuple[Tuple[str, str], ...]` | `(('frontend', '#22d3ee'), ('backend', '#34d399'), ('database', '#a78bfa'), ('cloud', '#fbbf24'), ('security', '#fb7185'), ('messagebus', '#fb923c'), ('external', '#94a3b8'), ('core', '#38bdf8'), ('test', '#64748b'))` |  |
| [`DIAGRAM_COMMUNITY_COLORS`](#config-diagram_community_colors) | `Tuple[str, ...]` | `('#22d3ee', '#f472b6', '#a3e635', '#fbbf24', '#a78bfa', '#fb923c', '#34d399', '#f87171', '#60a5fa', '#e879f9')` |  |
| [`VIDEO_ENABLED`](#config-video_enabled) | `bool` | `True` |  |
| [`VIDEO_OUTPUT`](#config-video_output) | `str` | `'readmenator.mp4'` |  |
| [`VIDEO_WIDTH`](#config-video_width) | `int` | `1280` |  |
| [`VIDEO_HEIGHT`](#config-video_height) | `int` | `720` |  |
| [`VIDEO_FPS`](#config-video_fps) | `int` | `24` |  |
| [`VIDEO_CRF`](#config-video_crf) | `str` | `'20'` |  |
| [`VIDEO_JOBS`](#config-video_jobs) | `int` | `0` |  |
| [`VIDEO_TITLE_S`](#config-video_title_s) | `float` | `5.0` |  |
| [`VIDEO_CARD_S`](#config-video_card_s) | `float` | `2.2` |  |
| [`VIDEO_LAYER_S`](#config-video_layer_s) | `float` | `8.0` |  |
| [`VIDEO_GOD_S`](#config-video_god_s) | `float` | `8.0` |  |
| [`VIDEO_TREE_S`](#config-video_tree_s) | `float` | `10.0` |  |
| [`VIDEO_PREVIEW_LINES`](#config-video_preview_lines) | `int` | `24` |  |
| [`VIDEO_TREE_MAX_NODES`](#config-video_tree_max_nodes) | `int` | `0` |  |
| [`VIDEO_TREE_RING_MARGIN`](#config-video_tree_ring_margin) | `int` | `40` |  |
| [`VIDEO_TREE_LABEL_GAP`](#config-video_tree_label_gap) | `int` | `6` |  |
| [`VIDEO_TREE_CHAR_PX`](#config-video_tree_char_px) | `int` | `9` |  |
| [`VIDEO_DNA_MAX_CELL`](#config-video_dna_max_cell) | `int` | `64` |  |
| [`VIDEO_GRAPH_TRIM_FRACTION`](#config-video_graph_trim_fraction) | `float` | `0.05` |  |
| [`VIDEO_GRAPH_SPREAD`](#config-video_graph_spread) | `float` | `2.2` |  |
| [`VIDEO_GRAPH_LOOSE_STRIP`](#config-video_graph_loose_strip) | `int` | `60` |  |
| [`VIDEO_COMM_S`](#config-video_comm_s) | `float` | `9.0` |  |
| [`VIDEO_GRAPH_S`](#config-video_graph_s) | `float` | `12.0` |  |
| [`VIDEO_DNA_S`](#config-video_dna_s) | `float` | `10.0` |  |
| [`VIDEO_OUTRO_S`](#config-video_outro_s) | `float` | `7.0` |  |
| [`VIDEO_MAX_GRAPH_NODES`](#config-video_max_graph_nodes) | `int` | `0` |  |
| [`VIDEO_MAX_LABEL_CHARS`](#config-video_max_label_chars) | `int` | `28` |  |
| [`VIDEO_MUSIC_PATH`](#config-video_music_path) | `str` | `''` |  |
| [`CONCEPT_ENABLED`](#config-concept_enabled) | `bool` | `True` |  |
| [`CONCEPT_MIN_FILES`](#config-concept_min_files) | `int` | `2` |  |
| [`CONCEPT_MAX_CONCEPTS`](#config-concept_max_concepts) | `int` | `50` |  |
| [`CONCEPT_MAX_RELATIONS`](#config-concept_max_relations) | `int` | `100` |  |
| [`CONCEPT_MIN_TOKEN_LEN`](#config-concept_min_token_len) | `int` | `3` |  |
| [`CONCEPT_MAX_FILES_PER_CONCEPT`](#config-concept_max_files_per_concept) | `int` | `50` |  |
| [`CONCEPT_DIALECTIC_MAX`](#config-concept_dialectic_max) | `int` | `10` |  |
| [`CONCEPT_STOPWORDS`](#config-concept_stopwords) | `Tuple[str, ...]` | `('the', 'and', 'for', 'with', 'from', 'that', 'this', 'with', 'into', 'your', 'you', 'are', 'was', 'were', 'has', 'have', 'had', 'will', 'would', 'could', 'should', 'py', 'c', 'h', 'js', 'ts', 'src', 'lib', 'test', 'tests', 'init', 'main', 'utils', 'util', 'core', 'base', 'impl')` |  |
| [`FORCEGRAPH_ENABLED`](#config-forcegraph_enabled) | `bool` | `True` |  |
| [`FORCEGRAPH_MODE`](#config-forcegraph_mode) | `str` | `'2d'` |  |
| [`FORCEGRAPH_OUTPUT`](#config-forcegraph_output) | `str` | `'graph-force.html'` |  |
| [`FORCEGRAPH_CDN_JS_2D`](#config-forcegraph_cdn_js_2d) | `str` | `'https://cdn.jsdelivr.net/npm/force-graph@1/dist/force-graph.min.js'` |  |
| [`FORCEGRAPH_CDN_JS_3D`](#config-forcegraph_cdn_js_3d) | `str` | `'https://cdn.jsdelivr.net/npm/3d-force-graph@1.77.0/dist/3d-force-graph.min.js'` |  |
| [`FORCEGRAPH_VENDOR_SUBDIR`](#config-forcegraph_vendor_subdir) | `str` | `'vendor'` |  |
| [`FORCEGRAPH_VENDOR_JS_2D`](#config-forcegraph_vendor_js_2d) | `str` | `'force-graph.min.js'` |  |
| [`FORCEGRAPH_BG`](#config-forcegraph_bg) | `str` | `'#0d0f14'` |  |
| [`FORCEGRAPH_CHARGE`](#config-forcegraph_charge) | `int` | `-300` |  |
| [`FORCEGRAPH_LINK_DISTANCE`](#config-forcegraph_link_distance) | `int` | `120` |  |
| [`FORCEGRAPH_LINK_STRENGTH`](#config-forcegraph_link_strength) | `float` | `0.3` |  |
| [`FORCEGRAPH_NODE_REL_SIZE`](#config-forcegraph_node_rel_size) | `int` | `4` |  |
| [`FORCEGRAPH_HULLS_ENABLED`](#config-forcegraph_hulls_enabled) | `bool` | `True` |  |
| [`FORCEGRAPH_HULL_FILL_ALPHA`](#config-forcegraph_hull_fill_alpha) | `float` | `0.07` |  |
| [`FORCEGRAPH_HULL_STROKE_ALPHA`](#config-forcegraph_hull_stroke_alpha) | `float` | `0.5` |  |
| [`FORCEGRAPH_HULL_PAD`](#config-forcegraph_hull_pad) | `int` | `18` |  |
| [`FORCEGRAPH_PARTICLES_ON_HIGHLIGHT`](#config-forcegraph_particles_on_highlight) | `int` | `4` |  |
| [`FORCEGRAPH_DIM_NODE`](#config-forcegraph_dim_node) | `str` | `'rgba(80,85,110,.4)'` |  |
| [`FORCEGRAPH_DIM_LINK`](#config-forcegraph_dim_link) | `str` | `'rgba(255,255,255,.04)'` |  |
| [`FORCEGRAPH_NODE_COLORS`](#config-forcegraph_node_colors) | `Tuple[Tuple[str, str], ...]` | `(('file', '#4f8ef7'), ('community', '#7c5aef'), ('layer', '#4fef8e'), ('external', '#efb84f'), ('security', '#ef5a5a'), ('hotspot', '#ef8e4f'))` |  |
| [`FORCEGRAPH_EDGE_COLORS`](#config-forcegraph_edge_colors) | `Tuple[Tuple[str, str], ...]` | `(('imports', 'rgba(79,142,247,.45)'), ('resolved_imports', 'rgba(79,239,142,.35)'), ('calls', 'rgba(239,184,79,.4)'), ('inherits', 'rgba(124,90,239,.45)'), ('external', 'rgba(255,255,255,.15)'), ('member_of', 'rgba(167,139,250,.22)'), ('layered_as', 'rgba(52,211,153,.16)'))` |  |
| [`FORCEGRAPH_FAMILY_SAT_BASE`](#config-forcegraph_family_sat_base) | `int` | `55` |  |
| [`FORCEGRAPH_FAMILY_SAT_SPAN`](#config-forcegraph_family_sat_span) | `int` | `12` |  |
| [`FORCEGRAPH_FAMILY_LIGHT_BASE`](#config-forcegraph_family_light_base) | `int` | `58` |  |
| [`FORCEGRAPH_FAMILY_LIGHT_SPAN`](#config-forcegraph_family_light_span) | `int` | `10` |  |
| [`ANALYTICS_ENABLED`](#config-analytics_enabled) | `bool` | `True` |  |
| [`SCANTEXT_ENABLED`](#config-scantext_enabled) | `bool` | `True` |  |
| [`SCANTEXT_MAX_SYMBOLS`](#config-scantext_max_symbols) | `int` | `80` |  |
| [`SCANTEXT_MAX_IMPORTS`](#config-scantext_max_imports) | `int` | `80` |  |
| [`SCANTEXT_SNIPPET_CHARS`](#config-scantext_snippet_chars) | `int` | `4000` |  |
| [`YARALITE_ENABLED`](#config-yaralite_enabled) | `bool` | `True` |  |
| [`YARALITE_RULES_FILE`](#config-yaralite_rules_file) | `str` | `'readmenator-rules/yara_rules.yar'` |  |
| [`YARALITE_MAX_HITS_PER_ID`](#config-yaralite_max_hits_per_id) | `int` | `50` |  |
| [`PROVENANCE_ENABLED`](#config-provenance_enabled) | `bool` | `True` |  |
| [`EXCLUSIONS_ENABLED`](#config-exclusions_enabled) | `bool` | `True` |  |
| [`EXCLUSIONS_FILE`](#config-exclusions_file) | `str` | `'readmenator-rules/exclusions.yaml'` |  |
| [`EXPLORER_ENABLED`](#config-explorer_enabled) | `bool` | `True` |  |
| [`EXPLORER_HOST`](#config-explorer_host) | `str` | `'127.0.0.1'` |  |
| [`EXPLORER_PORT`](#config-explorer_port) | `int` | `8421` |  |
| [`EMBED_ENABLED`](#config-embed_enabled) | `bool` | `True` |  |
| [`EMBED_MODEL`](#config-embed_model) | `str` | `'all-MiniLM-L6-v2'` |  |
| [`EMBED_MIN_CLUSTER_SIZE`](#config-embed_min_cluster_size) | `int` | `3` |  |
| [`EMBED_MAX_NEIGHBORS`](#config-embed_max_neighbors) | `int` | `10` |  |
| [`GRAPHRAG_ENABLED`](#config-graphrag_enabled) | `bool` | `True` |  |
| [`GRAPHRAG_OUTPUT_DIR`](#config-graphrag_output_dir) | `str` | `'readmenator-graphrag'` |  |
| [`GRAPHRAG_INCLUDE_SYMBOLS`](#config-graphrag_include_symbols) | `bool` | `True` |  |
| [`GRAPHRAG_INCLUDE_CONCEPTS`](#config-graphrag_include_concepts) | `bool` | `True` |  |
| [`GRAPHRAG_INCLUDE_EXTERNALS`](#config-graphrag_include_externals) | `bool` | `True` |  |
| [`GRAPHRAG_TEXT_UNIT_MAX_LINES`](#config-graphrag_text_unit_max_lines) | `int` | `40` |  |
| [`GRAPHRAG_TEXT_UNIT_MAX_CHARS`](#config-graphrag_text_unit_max_chars) | `int` | `1600` |  |
| [`GRAPHRAG_DESCRIPTION_MAX_CHARS`](#config-graphrag_description_max_chars) | `int` | `240` |  |
| [`GRAPHRAG_MIN_TOKEN_LEN`](#config-graphrag_min_token_len) | `int` | `2` |  |
| [`GRAPHRAG_BM25_K1`](#config-graphrag_bm25_k1) | `float` | `1.2` |  |
| [`GRAPHRAG_BM25_B`](#config-graphrag_bm25_b) | `float` | `0.75` |  |
| [`GRAPHRAG_PPR_ALPHA`](#config-graphrag_ppr_alpha) | `float` | `0.5` |  |
| [`GRAPHRAG_PPR_MAX_ITER`](#config-graphrag_ppr_max_iter) | `int` | `50` |  |
| [`GRAPHRAG_PPR_TOLERANCE`](#config-graphrag_ppr_tolerance) | `float` | `1e-06` |  |
| [`GRAPHRAG_SEED_TOP_K`](#config-graphrag_seed_top_k) | `int` | `8` |  |
| [`GRAPHRAG_LOCAL_TOP_ENTITIES`](#config-graphrag_local_top_entities) | `int` | `15` |  |
| [`GRAPHRAG_LOCAL_TOP_RELATIONS`](#config-graphrag_local_top_relations) | `int` | `20` |  |
| [`GRAPHRAG_LOCAL_TOP_TEXT_UNITS`](#config-graphrag_local_top_text_units) | `int` | `6` |  |
| [`GRAPHRAG_LOCAL_TOP_REPORTS`](#config-graphrag_local_top_reports) | `int` | `3` |  |
| [`GRAPHRAG_GLOBAL_TOP_REPORTS`](#config-graphrag_global_top_reports) | `int` | `6` |  |
| [`GRAPHRAG_REPORT_MAX_FINDINGS`](#config-graphrag_report_max_findings) | `int` | `8` |  |
| [`GRAPHRAG_REPORT_KEY_ENTITIES`](#config-graphrag_report_key_entities) | `int` | `8` |  |
| [`GRAPHRAG_REPORT_KEY_RELATIONS`](#config-graphrag_report_key_relations) | `int` | `8` |  |
| [`GRAPHRAG_CONTEXT_BUDGET_TOKENS`](#config-graphrag_context_budget_tokens) | `int` | `4000` |  |
| [`GRAPHRAG_RATING_CENTRALITY_WEIGHT`](#config-graphrag_rating_centrality_weight) | `float` | `7.0` |  |
| [`GRAPHRAG_RATING_RISK_WEIGHT`](#config-graphrag_rating_risk_weight) | `float` | `3.0` |  |
| [`GRAPHRAG_RATING_RISK_CAP`](#config-graphrag_rating_risk_cap) | `float` | `10.0` |  |
| [`GRAPHRAG_SEVERITY_WEIGHTS`](#config-graphrag_severity_weights) | `Tuple[Tuple[str, float], ...]` | `(('critical', 4.0), ('high', 2.0), ('medium', 1.0), ('low', 0.25), ('info', 0.1))` |  |
| [`GRAPHRAG_GLOBAL_HINTS`](#config-graphrag_global_hints) | `Tuple[str, ...]` | `('architecture', 'overview', 'overall', 'themes', 'theme', 'structure', 'design', 'summary', 'summarize', 'landscape', 'communities', 'subsystems', 'modules', 'big', 'picture', 'main', 'risks', 'everything', 'whole', 'project')` |  |
| [`GRAPHRAG_STOPWORDS`](#config-graphrag_stopwords) | `Tuple[str, ...]` | `('the', 'and', 'for', 'with', 'from', 'that', 'this', 'what', 'how', 'does', 'where', 'which', 'who', 'why', 'when', 'are', 'is', 'of', 'to', 'in', 'on', 'a', 'an', 'it', 'be', 'do', 'can', 'should', 'i', 'me', 'my', 'we', 'our', 'you', 'your', 'use', 'used', 'uses', 'using', 'about', 'into', 'there')` |  |
| [`FORCEGRAPH_LABEL_TOP_N`](#config-forcegraph_label_top_n) | `int` | `30` |  |
| [`FORCEGRAPH_LABEL_ZOOM`](#config-forcegraph_label_zoom) | `float` | `1.6` |  |
| [`FORCEGRAPH_LABEL_MAX_CHARS`](#config-forcegraph_label_max_chars) | `int` | `28` |  |
| [`FORCEGRAPH_SYMBOLS_PER_NODE`](#config-forcegraph_symbols_per_node) | `int` | `40` |  |
| [`FORCEGRAPH_DOC_MAX_CHARS`](#config-forcegraph_doc_max_chars) | `int` | `280` |  |
| [`FORCEGRAPH_SIGNATURE_MAX_CHARS`](#config-forcegraph_signature_max_chars) | `int` | `90` |  |
| [`FORCEGRAPH_CLUSTER_STRENGTH`](#config-forcegraph_cluster_strength) | `float` | `0.6` |  |
| [`FORCEGRAPH_COLLIDE_PADDING`](#config-forcegraph_collide_padding) | `int` | `4` |  |
| [`FORCEGRAPH_DAG_LEVEL_DISTANCE`](#config-forcegraph_dag_level_distance) | `int` | `60` |  |
| [`FORCEGRAPH_FLY_MS`](#config-forcegraph_fly_ms) | `int` | `700` |  |
| [`FORCEGRAPH_FLY_ZOOM`](#config-forcegraph_fly_zoom) | `float` | `3.0` |  |
| [`FORCEGRAPH_SEARCH_RESULTS`](#config-forcegraph_search_results) | `int` | `8` |  |
| [`VIDEO_BUNDLE_S`](#config-video_bundle_s) | `float` | `11.0` |  |
| [`VIDEO_FA2_ITERATIONS`](#config-video_fa2_iterations) | `int` | `300` |  |
| [`VIDEO_FA2_SNAPSHOTS`](#config-video_fa2_snapshots) | `int` | `60` |  |
| [`VIDEO_FA2_SCALING`](#config-video_fa2_scaling) | `float` | `2.0` |  |
| [`VIDEO_FA2_GRAVITY`](#config-video_fa2_gravity) | `float` | `1.0` |  |
| [`VIDEO_FA2_LINLOG`](#config-video_fa2_linlog) | `bool` | `True` |  |
| [`VIDEO_BUNDLE_BETA`](#config-video_bundle_beta) | `float` | `0.85` |  |
| [`VIDEO_BUNDLE_SAMPLES`](#config-video_bundle_samples) | `int` | `24` |  |
| [`VIDEO_SURFERS`](#config-video_surfers) | `int` | `48` |  |
| [`VIDEO_RANK_LABELS`](#config-video_rank_labels) | `int` | `8` |  |
| [`VIDEO_ORBIT_S`](#config-video_orbit_s) | `float` | `16.0` |  |
| [`VIDEO_SPHERE_S`](#config-video_sphere_s) | `float` | `13.0` |  |
| [`VIDEO_INVITE_S`](#config-video_invite_s) | `float` | `7.0` |  |
| [`VIDEO_ORBIT_FA2_ITERATIONS`](#config-video_orbit_fa2_iterations) | `int` | `220` |  |
| [`VIDEO_ORBIT_TOUR_STOPS`](#config-video_orbit_tour_stops) | `int` | `4` |  |
| [`VIDEO_ORBIT_TURNS`](#config-video_orbit_turns) | `float` | `0.85` |  |
| [`VIDEO_ORBIT_PITCH_DEG`](#config-video_orbit_pitch_deg) | `float` | `18.0` |  |
| [`VIDEO_ORBIT_PERSPECTIVE`](#config-video_orbit_perspective) | `float` | `3.2` |  |
| [`VIDEO_ORBIT_ZOOM`](#config-video_orbit_zoom) | `float` | `1.5` |  |
| [`VIDEO_ORBIT_DEPTH_FADE`](#config-video_orbit_depth_fade) | `float` | `0.6` |  |
| [`VIDEO_ORBIT_LABELS`](#config-video_orbit_labels) | `int` | `6` |  |
| [`VIDEO_SPHERE_TURNS`](#config-video_sphere_turns) | `float` | `0.6` |  |
| [`VIDEO_SPHERE_SAMPLES`](#config-video_sphere_samples) | `int` | `18` |  |
| [`VIDEO_TIERS_S`](#config-video_tiers_s) | `float` | `12.0` |  |
| [`VIDEO_FLOW_S`](#config-video_flow_s) | `float` | `16.0` |  |
| [`VIDEO_FLOW_VIEW_WIDTH`](#config-video_flow_view_width) | `int` | `1100` |  |
| [`VIDEO_TRANSITION_S`](#config-video_transition_s) | `float` | `0.45` |  |
| [`VIDEO_TRANSITION_GLITCH`](#config-video_transition_glitch) | `float` | `0.35` |  |
| [`VIDEO_MOTION_BLUR_SAMPLES`](#config-video_motion_blur_samples) | `int` | `3` |  |
| [`VIDEO_MOTION_BLUR_SHUTTER`](#config-video_motion_blur_shutter) | `float` | `0.5` |  |
| [`VIDEO_MOTION_BLUR_ACTS`](#config-video_motion_blur_acts) | `Tuple[str, ...]` | `('orbit', 'sphere', 'invite')` |  |
| [`BUNDLEGRAPH_ENABLED`](#config-bundlegraph_enabled) | `bool` | `True` |  |
| [`BUNDLEGRAPH_OUTPUT`](#config-bundlegraph_output) | `str` | `'graph-bundle.html'` |  |
| [`BUNDLEGRAPH_MODE`](#config-bundlegraph_mode) | `str` | `'2d'` |  |
| [`BUNDLEGRAPH_BETA`](#config-bundlegraph_beta) | `float` | `0.85` |  |
| [`BUNDLEGRAPH_SAMPLES`](#config-bundlegraph_samples) | `int` | `20` |  |
| [`BUNDLEGRAPH_INNER_RATIO`](#config-bundlegraph_inner_ratio) | `float` | `0.55` |  |
| [`BUNDLEGRAPH_GROUP_GAP`](#config-bundlegraph_group_gap) | `float` | `0.04` |  |
| [`BUNDLEGRAPH_EDGE_ALPHA`](#config-bundlegraph_edge_alpha) | `float` | `0.3` |  |
| [`BUNDLEGRAPH_DIM_ALPHA`](#config-bundlegraph_dim_alpha) | `float` | `0.035` |  |
| [`BUNDLEGRAPH_LABEL_ALL_MAX`](#config-bundlegraph_label_all_max) | `int` | `140` |  |
| [`BUNDLEGRAPH_LABEL_TOP_N`](#config-bundlegraph_label_top_n) | `int` | `24` |  |
| [`BUNDLEGRAPH_LABEL_MAX_CHARS`](#config-bundlegraph_label_max_chars) | `int` | `26` |  |
| [`BUNDLEGRAPH_NODE_MIN_PX`](#config-bundlegraph_node_min_px) | `float` | `2.0` |  |
| [`BUNDLEGRAPH_NODE_MAX_PX`](#config-bundlegraph_node_max_px) | `float` | `7.0` |  |
| [`BUNDLEGRAPH_HIT_PX`](#config-bundlegraph_hit_px) | `float` | `9.0` |  |
| [`BUNDLEGRAPH_ROTATE_SPEED`](#config-bundlegraph_rotate_speed) | `float` | `0.12` |  |
| [`BUNDLEGRAPH_PERSPECTIVE`](#config-bundlegraph_perspective) | `float` | `3.0` |  |
| [`BUNDLEGRAPH_DEPTH_FADE`](#config-bundlegraph_depth_fade) | `float` | `0.7` |  |
| [`BUNDLEGRAPH_PARTICLES`](#config-bundlegraph_particles) | `int` | `3` |  |
| [`BUNDLEGRAPH_REVEAL_MS`](#config-bundlegraph_reveal_ms) | `int` | `1400` |  |
| [`BUNDLEGRAPH_FLOW_TOP_N`](#config-bundlegraph_flow_top_n) | `int` | `8` |  |
| [`BUNDLEGRAPH_LIST_MAX`](#config-bundlegraph_list_max) | `int` | `40` |  |
| [`BUNDLEGRAPH_THUMB_EDGES`](#config-bundlegraph_thumb_edges) | `int` | `500` |  |
| [`BUNDLEGRAPH_THUMB_SAMPLES`](#config-bundlegraph_thumb_samples) | `int` | `12` |  |
| [`BUNDLEGRAPH_ORDER_OPTIMIZE`](#config-bundlegraph_order_optimize) | `bool` | `True` |  |
| [`BUNDLEGRAPH_ORDER_SWEEPS`](#config-bundlegraph_order_sweeps) | `int` | `6` |  |
| [`BUNDLEGRAPH_ORDER_PASSES`](#config-bundlegraph_order_passes) | `int` | `8` |  |
| [`BUNDLEGRAPH_SPHERE_REFINE_SWEEPS`](#config-bundlegraph_sphere_refine_sweeps) | `int` | `4` |  |
| [`FORCEGRAPH_THUMB_WIDTH`](#config-forcegraph_thumb_width) | `int` | `320` |  |
| [`FORCEGRAPH_THUMB_HEIGHT`](#config-forcegraph_thumb_height) | `int` | `150` |  |
| [`FORCEGRAPH_THUMB_ITERATIONS`](#config-forcegraph_thumb_iterations) | `int` | `150` |  |
| [`FORCEGRAPH_SEED_LAYOUT`](#config-forcegraph_seed_layout) | `bool` | `True` |  |
| [`FORCEGRAPH_SEED_ITERATIONS`](#config-forcegraph_seed_iterations) | `int` | `220` |  |
| [`FORCEGRAPH_SEED_GRAVITY`](#config-forcegraph_seed_gravity) | `float` | `1.0` |  |
| [`FORCEGRAPH_SEED_MAX_NODES`](#config-forcegraph_seed_max_nodes) | `int` | `3000` |  |
| [`FORCEGRAPH_SEED_VELOCITY_DECAY`](#config-forcegraph_seed_velocity_decay) | `float` | `0.55` |  |
| [`FORCEGRAPH_LAYER_COLORS`](#config-forcegraph_layer_colors) | `Tuple[Tuple[str, str], ...]` | `(('presentation', '#22d3ee'), ('business_logic', '#34d399'), ('data_access', '#a78bfa'), ('infrastructure', '#fbbf24'), ('utility', '#94a3b8'), ('testing', '#fb923c'), ('unknown', '#64748b'))` |  |
| [`FORCEGRAPH_HIT_PADDING_PX`](#config-forcegraph_hit_padding_px) | `float` | `3.0` |  |
| [`FORCEGRAPH_MIN_HIT_PX`](#config-forcegraph_min_hit_px) | `float` | `7.0` |  |
| [`FORCEGRAPH_EDGE_HIT_PX`](#config-forcegraph_edge_hit_px) | `float` | `5.0` |  |
| [`FORCEGRAPH_DRAG_THRESHOLD_PX`](#config-forcegraph_drag_threshold_px) | `float` | `4.0` |  |
| [`FORCEGRAPH_CURVE_STEP`](#config-forcegraph_curve_step) | `float` | `0.18` |  |
| [`FORCEGRAPH_CURVE_SAMPLES`](#config-forcegraph_curve_samples) | `int` | `16` |  |
| [`FORCEGRAPH_ARROW_LENGTH`](#config-forcegraph_arrow_length) | `float` | `4.0` |  |
| [`FORCEGRAPH_ARROW_ZOOM`](#config-forcegraph_arrow_zoom) | `float` | `2.2` |  |
| [`FORCEGRAPH_COOLDOWN_TICKS`](#config-forcegraph_cooldown_ticks) | `int` | `400` |  |
| [`FORCEGRAPH_COOLDOWN_TICKS_REDUCED`](#config-forcegraph_cooldown_ticks_reduced) | `int` | `60` |  |
| [`FORCEGRAPH_COLLIDE_MAX_NODES`](#config-forcegraph_collide_max_nodes) | `int` | `1500` |  |
| [`FORCEGRAPH_LABEL_HIGHLIGHT_MAX`](#config-forcegraph_label_highlight_max) | `int` | `60` |  |
| [`FORCEGRAPH_DOC_LINES_PX`](#config-forcegraph_doc_lines_px) | `float` | `9.0` |  |
| [`FORCEGRAPH_TIP_DOC_CHARS`](#config-forcegraph_tip_doc_chars) | `int` | `200` |  |
| [`FORCEGRAPH_HUB_TOP_N`](#config-forcegraph_hub_top_n) | `int` | `10` |  |
| [`FORCEGRAPH_FIT_PADDING_PX`](#config-forcegraph_fit_padding_px) | `int` | `48` |  |
| [`FORCEGRAPH_FIT_MAX_ZOOM`](#config-forcegraph_fit_max_zoom) | `float` | `2.5` |  |
| [`FORCEGRAPH_FIT_LEGEND_MIN_WIDTH`](#config-forcegraph_fit_legend_min_width) | `int` | `700` |  |
| [`FORCEGRAPH_3D_LINK_OPACITY`](#config-forcegraph_3d_link_opacity) | `float` | `0.5` |  |
| [`FORCEGRAPH_3D_LINK_WIDTH_HIGHLIGHT`](#config-forcegraph_3d_link_width_highlight) | `float` | `0.7` |  |
| [`FORCEGRAPH_3D_LINK_WIDTH_ACTIVE`](#config-forcegraph_3d_link_width_active) | `float` | `1.4` |  |
| [`FORCEGRAPH_3D_PARTICLE_WIDTH`](#config-forcegraph_3d_particle_width) | `float` | `1.3` |  |
| [`FORCEGRAPH_3D_DEPTH_FADE`](#config-forcegraph_3d_depth_fade) | `float` | `0.3` |  |
| [`FORCEGRAPH_3D_MIN_GLYPH_PX`](#config-forcegraph_3d_min_glyph_px) | `float` | `2.5` |  |
| [`FORCEGRAPH_3D_LABEL_PX`](#config-forcegraph_3d_label_px) | `float` | `9.0` |  |
| [`FORCEGRAPH_3D_ORBIT_SPEED`](#config-forcegraph_3d_orbit_speed) | `float` | `0.6` |  |
| [`FORCEGRAPH_3D_FLY_DISTANCE`](#config-forcegraph_3d_fly_distance) | `int` | `320` |  |
| [`MEMORY_ENABLED`](#config-memory_enabled) | `bool` | `True` |  |
| [`MEMORY_FILENAME`](#config-memory_filename) | `str` | `'MEMORY.md'` |  |
| [`MEMORY_NOTE_MAX_CHARS`](#config-memory_note_max_chars) | `int` | `500` |  |
| [`MEMORY_NOTE_KINDS`](#config-memory_note_kinds) | `Tuple[str, ...]` | `('business', 'decision', 'rule', 'workflow', 'style', 'deliverable', 'gotcha', 'todo', 'note')` |  |
| [`MEMORY_RULE_SOURCES`](#config-memory_rule_sources) | `Tuple[str, ...]` | `('AGENTS.md', 'CLAUDE.md', 'GEMINI.md', 'CONVENTIONS.md', 'CONTRIBUTING.md', 'RULES.md', 'PROJECT_RULES.md', '.cursorrules', '.windsurfrules', '.github/copilot-instructions.md', 'SECURITY.md', 'STYLEGUIDE.md', 'docs/CONTRIBUTING.md')` |  |
| [`MEMORY_CONSTRAINT_KEYWORDS`](#config-memory_constraint_keywords) | `Tuple[str, ...]` | `('rule', 'constraint', 'principle', 'security', 'must', 'never', 'forbidden', 'restriction', 'policy', 'boy scout', 'invariant', 'dry', 'solid')` |  |
| [`MEMORY_STYLE_KEYWORDS`](#config-memory_style_keywords) | `Tuple[str, ...]` | `('style', 'convention', 'naming', 'format', 'lint', 'code quality', 'structured output')` |  |
| [`MEMORY_DELIVERABLE_KEYWORDS`](#config-memory_deliverable_keywords) | `Tuple[str, ...]` | `('definition of done', 'done', 'checklist', 'deliverable', 'testing', 'test', 'review', 'pull request', 'release', 'acceptance')` |  |
| [`MEMORY_HEADING_EXCLUDE`](#config-memory_heading_exclude) | `Tuple[str, ...]` | `('contract', 'project structure', 'knowledge base')` |  |
| [`MEMORY_MAX_RULES_PER_FILE`](#config-memory_max_rules_per_file) | `int` | `40` |  |
| [`MEMORY_MAX_RULES_PER_CATEGORY`](#config-memory_max_rules_per_category) | `int` | `60` |  |
| [`MEMORY_MIN_RULE_CHARS`](#config-memory_min_rule_chars) | `int` | `12` |  |
| [`MEMORY_MAX_COMMANDS`](#config-memory_max_commands) | `int` | `12` |  |
| [`MEMORY_VOCABULARY_TOP_N`](#config-memory_vocabulary_top_n) | `int` | `15` |  |
| [`MEMORY_SUBSYSTEMS_TOP_N`](#config-memory_subsystems_top_n) | `int` | `8` |  |
| [`MEMORY_STYLE_LANGUAGES`](#config-memory_style_languages) | `int` | `4` |  |
| [`MEMORY_RISKS_TOP_N`](#config-memory_risks_top_n) | `int` | `5` |  |
| [`SKILLS_ENABLED`](#config-skills_enabled) | `bool` | `True` |  |
| [`SKILLS_TARGET_DIR`](#config-skills_target_dir) | `str` | `'.claude/skills'` |  |
| [`SKILLS_INSTALL_ON_RUN`](#config-skills_install_on_run) | `bool` | `True` |  |
| [`MEMORY_VOCABULARY_STOPWORDS`](#config-memory_vocabulary_stopwords) | `Tuple[str, ...]` | `('returns', 'return', 'when', 'empty', 'none', 'true', 'false', 'given', 'value', 'values', 'args', 'raises', 'list', 'dict', 'string', 'str', 'int', 'each', 'every', 'into', 'used', 'uses', 'only', 'also', 'must', 'never', 'then', 'than', 'contract')` |  |
| [`GRAPHRAG_LOCAL_SECTION_SHARES`](#config-graphrag_local_section_shares) | `Tuple[float, ...]` | `(0.35, 0.15, 0.2, 0.3)` |  |
| [`GRAPHRAG_GLOBAL_SECTION_SHARES`](#config-graphrag_global_section_shares) | `Tuple[float, ...]` | `(0.3, 0.7)` |  |
| [`SYMINDEX_MAX_CALL_SITES`](#config-symindex_max_call_sites) | `int` | `2000` |  |
| [`SYMINDEX_BUILTINS`](#config-symindex_builtins) | `Tuple[str, ...]` | `('print', 'len', 'range', 'str', 'int', 'float', 'bool', 'list', 'dict', 'set', 'tuple', 'open', 'super', 'self', 'cls', 'isinstance', 'issubclass', 'hasattr', 'getattr', 'setattr', 'enumerate', 'zip', 'map', 'filter', 'sorted', 'reversed', 'min', 'max', 'sum', 'abs', 'round', 'repr', 'type', 'id', 'hash', 'iter', 'next', 'all', 'any', 'exit', 'quit', 'input', 'format', 'vars', 'dir', 'globals', 'locals', 'callable', 'ord', 'chr', 'hex', 'oct', 'bin', 'pow', 'divmod', 'console', 'require', 'module', 'exports', 'window', 'document', 'parseInt', 'parseFloat', 'isNaN', 'setTimeout', 'setInterval', 'fetch', 'assert', 'expect', 'describe', 'it', 'test')` |  |
| [`LINTER_UNRESOLVED_CALLS`](#config-linter_unresolved_calls) | `bool` | `True` |  |
| [`SYMINDEX_RECEIVER_WINDOW`](#config-symindex_receiver_window) | `int` | `160` |  |
| [`COMPONENTS_ENABLED`](#config-components_enabled) | `bool` | `True` |  |
| [`COMPONENTS_OUTPUT_DIR`](#config-components_output_dir) | `str` | `'readmenator-diagrams'` |  |
| [`COMPONENTS_MAX_KEY_ENTITIES`](#config-components_max_key_entities) | `int` | `8` |  |
| [`COMPONENTS_MAX_KEY_EDGES`](#config-components_max_key_edges) | `int` | `8` |  |
| [`COMPONENTS_MAX_ALL_EDGES`](#config-components_max_all_edges) | `int` | `50` |  |
| [`COMPONENTS_EXPAND_MIN_FILES`](#config-components_expand_min_files) | `int` | `6` |  |
| [`COMPONENTS_DEPTH_CAP`](#config-components_depth_cap) | `int` | `3` |  |
| [`COMPONENTS_NODE_SYMBOLS`](#config-components_node_symbols) | `int` | `3` |  |
| [`OLLAMA_ENABLED`](#config-ollama_enabled) | `bool` | `False` |  |
| [`OLLAMA_HOST`](#config-ollama_host) | `str` | `'http://localhost:11434'` |  |
| [`OLLAMA_MODEL`](#config-ollama_model) | `str` | `'deepseek-r1:1.5b'` |  |
| [`OLLAMA_TIMEOUT_S`](#config-ollama_timeout_s) | `int` | `120` |  |
| [`OLLAMA_MAX_PROMPT_CHARS`](#config-ollama_max_prompt_chars) | `int` | `2000` |  |
| [`OLLAMA_MAX_CHARS`](#config-ollama_max_chars) | `int` | `600` |  |
| [`SOURCEVIEW_ENABLED`](#config-sourceview_enabled) | `bool` | `True` |  |
| [`SOURCEVIEW_MAX_FILES`](#config-sourceview_max_files) | `int` | `2500` |  |
| [`SOURCEVIEW_MAX_CHARS_PER_FILE`](#config-sourceview_max_chars_per_file) | `int` | `60000` |  |
| [`SOURCEVIEW_MAX_LINES_PER_FILE`](#config-sourceview_max_lines_per_file) | `int` | `2000` |  |
| [`SOURCEVIEW_MAX_TOTAL_CHARS`](#config-sourceview_max_total_chars) | `int` | `20000000` |  |
| [`SOURCEVIEW_CHUNK_LINES`](#config-sourceview_chunk_lines) | `int` | `300` |  |
| [`SOURCEVIEW_CONTEXT_LINES`](#config-sourceview_context_lines) | `int` | `3` |  |
| [`APIDOCS_ENABLED`](#config-apidocs_enabled) | `bool` | `True` |  |
| [`APIDOCS_OUTPUT_DIR`](#config-apidocs_output_dir) | `str` | `'readmenator-apidocs'` |  |
| [`APIDOCS_MODULES_SUBDIR`](#config-apidocs_modules_subdir) | `str` | `'modules'` |  |
| [`APIDOCS_INCLUDE_PRIVATE`](#config-apidocs_include_private) | `bool` | `False` |  |
| [`APIDOCS_INCLUDE_TESTS`](#config-apidocs_include_tests) | `bool` | `False` |  |
| [`APIDOCS_TEST_PATH_TOKENS`](#config-apidocs_test_path_tokens) | `Tuple[str, ...]` | `('test', 'tests', 'spec', 'specs', '__tests__', 'testing', 'conftest')` |  |
| [`APIDOCS_SKIP_SUFFIXES`](#config-apidocs_skip_suffixes) | `Tuple[str, ...]` | `('.min.js', '.min.mjs', '.bundle.js', '.min.css')` |  |
| [`APIDOCS_EXCLUDE_DIRS`](#config-apidocs_exclude_dirs) | `Tuple[str, ...]` | `('vendor', '_vendor', 'third_party', 'thirdparty', 'external', 'node_modules')` |  |
| [`APIDOCS_MAX_ENTITIES`](#config-apidocs_max_entities) | `int` | `20000` |  |
| [`APIDOCS_DOC_LOOKBACK_LINES`](#config-apidocs_doc_lookback_lines) | `int` | `80` |  |
| [`APIDOCS_BRACE_SCAN_LINES`](#config-apidocs_brace_scan_lines) | `int` | `12` |  |
| [`APIDOCS_MAX_CALL_REFS`](#config-apidocs_max_call_refs) | `int` | `12` |  |
| [`APIDOCS_CALLGRAPH_MAX_EDGES`](#config-apidocs_callgraph_max_edges) | `int` | `24` |  |
| [`APIDOCS_SUMMARY_MAX_CHARS`](#config-apidocs_summary_max_chars) | `int` | `160` |  |
| [`APIDOCS_HTML_ENABLED`](#config-apidocs_html_enabled) | `bool` | `True` |  |
| [`APIDOCS_HTML_FILENAME`](#config-apidocs_html_filename) | `str` | `'index.html'` |  |
| [`APIDOCS_JSON_FILENAME`](#config-apidocs_json_filename) | `str` | `'api.json'` |  |
| [`APIDOCS_ARCHITECTURE_FILENAME`](#config-apidocs_architecture_filename) | `str` | `'architecture.md'` |  |
| [`APIDOCS_SCHEMA_VERSION`](#config-apidocs_schema_version) | `int` | `1` |  |
| [`APIDOCS_MERMAID_CDN_JS`](#config-apidocs_mermaid_cdn_js) | `str` | `'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js'` |  |
| [`APIDOCS_COVERAGE_FAIL_UNDER`](#config-apidocs_coverage_fail_under) | `float` | `0.0` |  |
| [`APIDOCS_MAX_WARNINGS_LISTED`](#config-apidocs_max_warnings_listed) | `int` | `500` |  |
| [`ARCH_DIAGRAM_ENABLED`](#config-arch_diagram_enabled) | `bool` | `True` |  |
| [`ARCH_DIAGRAM_INCLUDE_TESTS`](#config-arch_diagram_include_tests) | `bool` | `False` |  |
| [`ARCH_DIAGRAM_MAX_COMPONENTS`](#config-arch_diagram_max_components) | `int` | `40` |  |
| [`ARCH_DIAGRAM_LABEL_CHARS`](#config-arch_diagram_label_chars) | `int` | `36` |  |
| [`FLOW_ENABLED`](#config-flow_enabled) | `bool` | `True` |  |
| [`FLOW_MAX_ENTRYPOINTS`](#config-flow_max_entrypoints) | `int` | `3` |  |
| [`FLOW_MIN_ENTRY_SCORE`](#config-flow_min_entry_score) | `int` | `3` |  |
| [`FLOW_SOURCE_MIN_CALLS`](#config-flow_source_min_calls) | `int` | `3` |  |
| [`FLOW_MAX_DEPTH`](#config-flow_max_depth) | `int` | `4` |  |
| [`FLOW_MAX_STEPS`](#config-flow_max_steps) | `int` | `40` |  |
| [`FLOW_LABEL_CHARS`](#config-flow_label_chars) | `int` | `48` |  |
| [`FLOW_SEQUENCE_MAX_MESSAGES`](#config-flow_sequence_max_messages) | `int` | `30` |  |
| [`FLOW_CFG_MAX_NODES`](#config-flow_cfg_max_nodes) | `int` | `160` |  |
| [`FLOW_SWITCH_MIN_CASES`](#config-flow_switch_min_cases) | `int` | `3` |  |
| [`FLOW_NODE_MAX_CHARS`](#config-flow_node_max_chars) | `int` | `38` |  |
| [`FLOW_NODE_MAX_LINES`](#config-flow_node_max_lines) | `int` | `3` |  |
| [`FLOW_MAX_PER_ROW`](#config-flow_max_per_row) | `int` | `5` |  |
| [`ARCH_DIAGRAM_MAX_PER_ROW`](#config-arch_diagram_max_per_row) | `int` | `4` |  |
| [`ARCH_DIAGRAM_PANEL_FILES`](#config-arch_diagram_panel_files) | `int` | `40` |  |
| [`FLOWS_OUTPUT`](#config-flows_output) | `str` | `'flows.html'` |  |

---
