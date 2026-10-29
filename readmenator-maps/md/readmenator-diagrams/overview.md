```mermaid
graph LR
    readmenator__video["readmenator: _video"]
    readmenator_parsers["readmenator/parsers"]
    readmenator__agent_output["readmenator: _agent_output"]
    readmenator__graphrag["readmenator: _graphrag"]
    readmenator__pipeline["readmenator: _pipeline"]
    readmenator__diagrams["readmenator: _diagrams"]
    readmenator__flowcharts["readmenator: _flowcharts"]
    readmenator__video -- "calls into" --> readmenator_parsers
    readmenator__video -- "calls into" --> readmenator__agent_output
    readmenator__video -- "calls into" --> readmenator__graphrag
    readmenator__video -- "calls into" --> readmenator__pipeline
    readmenator__video -- "calls into" --> readmenator__diagrams
    readmenator__video -- "calls into" --> readmenator__flowcharts
    readmenator_parsers -- "calls into" --> readmenator__video
    readmenator_parsers -- "calls into" --> readmenator__graphrag
    readmenator_parsers -- "calls into" --> readmenator__pipeline
    readmenator_parsers -- "calls into" --> readmenator__flowcharts
    readmenator__agent_output -- "calls into" --> readmenator__video
    readmenator__agent_output -- "calls into" --> readmenator_parsers
    readmenator__agent_output -- "calls into" --> readmenator__graphrag
    readmenator__agent_output -- "calls into" --> readmenator__pipeline
    readmenator__agent_output -- "calls into" --> readmenator__diagrams
    readmenator__agent_output -- "calls into" --> readmenator__flowcharts
    readmenator__graphrag -- "calls into" --> readmenator__video
    readmenator__graphrag -- "calls into" --> readmenator_parsers
    readmenator__graphrag -- "calls into" --> readmenator__agent_output
    readmenator__graphrag -- "depends on" --> readmenator__pipeline
    readmenator__graphrag -- "depends on" --> readmenator__diagrams
    readmenator__graphrag -- "calls into" --> readmenator__flowcharts
    readmenator__pipeline -- "calls into" --> readmenator__video
    readmenator__pipeline -- "calls into" --> readmenator_parsers
    readmenator__pipeline -- "calls into" --> readmenator__agent_output
    readmenator__pipeline -- "calls into" --> readmenator__graphrag
    readmenator__pipeline -- "calls into" --> readmenator__diagrams
    readmenator__pipeline -- "calls into" --> readmenator__flowcharts
    readmenator__diagrams -- "calls into" --> readmenator__video
    readmenator__diagrams -- "calls into" --> readmenator_parsers
    readmenator__diagrams -- "calls into" --> readmenator__agent_output
    readmenator__diagrams -- "calls into" --> readmenator__graphrag
    readmenator__diagrams -- "calls into" --> readmenator__pipeline
    readmenator__diagrams -- "calls into" --> readmenator__flowcharts
    readmenator__flowcharts -- "calls into" --> readmenator__video
    readmenator__flowcharts -- "calls into" --> readmenator_parsers
    readmenator__flowcharts -- "calls into" --> readmenator__agent_output
    readmenator__flowcharts -- "calls into" --> readmenator__graphrag
    readmenator__flowcharts -- "calls into" --> readmenator__pipeline
    readmenator__flowcharts -- "calls into" --> readmenator__diagrams
    click readmenator__video href "./readmenator__video.md" "Details"
    click readmenator_parsers href "./readmenator_parsers.md" "Details"
    click readmenator__agent_output href "./readmenator__agent_output.md" "Details"
    click readmenator__graphrag href "./readmenator__graphrag.md" "Details"
    click readmenator__pipeline href "./readmenator__pipeline.md" "Details"
    click readmenator__diagrams href "./readmenator__diagrams.md" "Details"
    click readmenator__flowcharts href "./readmenator__flowcharts.md" "Details"
```

## Details

Static architecture map of 161 files (js, py, sh) in 7 components: readmenator: _video, readmenator/parsers, readmenator: _agent_output, readmenator: _graphrag, readmenator: _pipeline, readmenator: _diagrams, readmenator: _flowcharts. Structure is extracted statically without LLM calls; component prose may be enriched locally.

### readmenator: _video (1)

readmenator: _video groups 41 files (py) around Config, readmenatorApplication, __init__, ingest_receipts, _scan. Launcher shim that runs the readmenator CLI from a source checkout.

**Related Classes/Methods**:

- <a href="../readmenator/_config.py#L15-L1266">readmenator/_config.py::Config</a>
- <a href="../readmenator/_app.py">readmenator/_app.py::readmenatorApplication</a>
- <a href="../readmenator/_app.py#L55-L63">readmenator/_app.py::__init__</a>
- <a href="../readmenator/_app.py#L64-L92">readmenator/_app.py::ingest_receipts</a>
- <a href="../readmenator/_app.py#L93-L100">readmenator/_app.py::_scan</a>
- <a href="../readmenator/_app.py#L101-L110">readmenator/_app.py::_scan_with_content</a>
- <a href="../readmenator/_app.py#L111-L129">readmenator/_app.py::_resolve_imports</a>
- <a href="../readmenator/_app.py#L130-L160">readmenator/_app.py::_apply_project_config</a>

### readmenator/parsers (2)

readmenator/parsers groups 34 files (py) around Symbol, Node, Edge, SecurityFinding, pluralize_symbol_kind. Hotspot, dependency cycle, and change impact analysis.

**Related Classes/Methods**:

- <a href="../readmenator/_models.py#L18-L36">readmenator/_models.py::Symbol</a>
- <a href="../readmenator/_models.py#L37-L57">readmenator/_models.py::Node</a>
- <a href="../readmenator/_models.py#L58-L76">readmenator/_models.py::Edge</a>
- <a href="../readmenator/_models.py#L77-L100">readmenator/_models.py::SecurityFinding</a>
- <a href="../readmenator/_models.py#L101-L110">readmenator/_models.py::pluralize_symbol_kind</a>
- <a href="../readmenator/_models.py#L111-L129">readmenator/_models.py::CommunityResult</a>
- <a href="../readmenator/_models.py#L130-L150">readmenator/_models.py::AnalysisResult</a>
- <a href="../readmenator/_models.py#L151-L171">readmenator/_models.py::TaintPath</a>

### readmenator: _agent_output (3)

readmenator: _agent_output groups 19 files (py) around ImportResolver, __init__, _build_stem_index, _build_dir_index, resolve. Agent-friendly output generator for ReadMenator.

**Related Classes/Methods**:

- <a href="../readmenator/_resolver.py#L18-L60">readmenator/_resolver.py::ImportResolver</a>
- <a href="../readmenator/_resolver.py#L61-L82">readmenator/_resolver.py::__init__</a>
- <a href="../readmenator/_resolver.py#L83-L92">readmenator/_resolver.py::_build_stem_index</a>
- <a href="../readmenator/_resolver.py#L93-L109">readmenator/_resolver.py::_build_dir_index</a>
- <a href="../readmenator/_resolver.py#L110-L162">readmenator/_resolver.py::resolve</a>
- <a href="../readmenator/_resolver.py#L163-L178">readmenator/_resolver.py::resolve_all</a>
- <a href="../readmenator/_resolver.py#L179-L198">readmenator/_resolver.py::_resolve_include_dirs</a>
- <a href="../readmenator/_resolver.py#L199-L216">readmenator/_resolver.py::_resolve_relative</a>

### readmenator: _graphrag (4)

readmenator: _graphrag groups 18 files (py) around EdgeKind, __str__, Morphism, weight, Category. ReadMenator -- Zero-token polyglot codebase knowledge graph generator.

**Related Classes/Methods**:

- <a href="../readmenator/_category.py#L24-L37">readmenator/_category.py::EdgeKind</a>
- <a href="../readmenator/_category.py#L38-L56">readmenator/_category.py::__str__</a>
- <a href="../readmenator/_category.py#L57-L72">readmenator/_category.py::Morphism</a>
- <a href="../readmenator/_category.py#L73-L77">readmenator/_category.py::weight</a>
- <a href="../readmenator/_category.py#L78-L85">readmenator/_category.py::Category</a>
- <a href="../readmenator/_category.py#L86-L91">readmenator/_category.py::__init__</a>
- <a href="../readmenator/_category.py#L92-L94">readmenator/_category.py::add_object</a>
- <a href="../readmenator/_category.py#L95-L102">readmenator/_category.py::add_morphism</a>

### readmenator: _pipeline (5)

readmenator: _pipeline groups 18 files (py) around ReadmeInjector, __init__, inject, _extract_current_injection, _remove_old_injection. Injects KNOWLEDGE_BASE.md references into AI agent instruction files.

**Related Classes/Methods**:

- <a href="../readmenator/_readme_injector.py#L134-L144">readmenator/_readme_injector.py::ReadmeInjector</a>
- <a href="../readmenator/_readme_injector.py#L145-L218">readmenator/_readme_injector.py::__init__</a>
- <a href="../readmenator/_readme_injector.py#L219-L259">readmenator/_readme_injector.py::inject</a>
- <a href="../readmenator/_readme_injector.py#L260-L276">readmenator/_readme_injector.py::_extract_current_injection</a>
- <a href="../readmenator/_readme_injector.py#L277-L295">readmenator/_readme_injector.py::_remove_old_injection</a>
- <a href="../readmenator/_readme_injector.py#L296-L310">readmenator/_readme_injector.py::_strip_partial_anchor</a>
- <a href="../readmenator/_readme_injector.py#L311-L347">readmenator/_readme_injector.py::remove</a>
- <a href="../readmenator/_readme_injector.py#L348-L362">readmenator/_readme_injector.py::_find_readme</a>

### readmenator: _diagrams (6)

readmenator: _diagrams groups 15 files (py) around _toml_str, _toml_value, template_text, config_path, ensure_project_config. Edge bundle explorer: circle and sphere hierarchical edge bundling pages.

**Related Classes/Methods**:

- <a href="../readmenator/_project_config.py#L136-L147">readmenator/_project_config.py::_toml_str</a>
- <a href="../readmenator/_project_config.py#L148-L158">readmenator/_project_config.py::_toml_value</a>
- <a href="../readmenator/_project_config.py#L159-L285">readmenator/_project_config.py::template_text</a>
- <a href="../readmenator/_project_config.py#L286-L299">readmenator/_project_config.py::config_path</a>
- <a href="../readmenator/_project_config.py#L300-L332">readmenator/_project_config.py::ensure_project_config</a>
- <a href="../readmenator/_project_config.py#L333-L366">readmenator/_project_config.py::_mini_toml_parse</a>
- <a href="../readmenator/_project_config.py#L367-L394">readmenator/_project_config.py::_strip_toml_comment</a>
- <a href="../readmenator/_project_config.py#L395-L449">readmenator/_project_config.py::_mini_toml_value</a>

### readmenator: _flowcharts (7)

readmenator: _flowcharts groups 12 files (py) around _receiver_text, SymbolDef, CallSite, ResolvedCall, _kind_to_node_type. Deterministic API reference model: extraction, cross-references, coverage.

**Related Classes/Methods**:

- <a href="../readmenator/_symindex.py#L42-L55">readmenator/_symindex.py::_receiver_text</a>
- <a href="../readmenator/_symindex.py#L56-L80">readmenator/_symindex.py::SymbolDef</a>
- <a href="../readmenator/_symindex.py#L81-L101">readmenator/_symindex.py::CallSite</a>
- <a href="../readmenator/_symindex.py#L102-L121">readmenator/_symindex.py::ResolvedCall</a>
- <a href="../readmenator/_symindex.py#L122-L131">readmenator/_symindex.py::_kind_to_node_type</a>
- <a href="../readmenator/_symindex.py#L132-L134">readmenator/_symindex.py::SymbolIndex</a>
- <a href="../readmenator/_symindex.py#L135-L143">readmenator/_symindex.py::__init__</a>
- <a href="../readmenator/_symindex.py#L144-L183">readmenator/_symindex.py::build</a>
