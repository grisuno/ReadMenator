```mermaid
graph LR
    readmenator__graphrag["readmenator: _graphrag"]
    readmenator_parsers["readmenator/parsers"]
    readmenator__diagrams["readmenator: _diagrams"]
    readmenator__pipeline["readmenator: _pipeline"]
    readmenator__graphlayout["readmenator: _graphlayout"]
    readmenator__flowcharts["readmenator: _flowcharts"]
    readmenator__graphrag -- "calls into" --> readmenator_parsers
    readmenator__graphrag -- "calls into" --> readmenator__diagrams
    readmenator__graphrag -- "calls into" --> readmenator__pipeline
    readmenator__graphrag -- "calls into" --> readmenator__flowcharts
    readmenator_parsers -- "calls into" --> readmenator__graphrag
    readmenator_parsers -- "calls into" --> readmenator__diagrams
    readmenator_parsers -- "calls into" --> readmenator__pipeline
    readmenator_parsers -- "calls into" --> readmenator__flowcharts
    readmenator__diagrams -- "calls into" --> readmenator__graphrag
    readmenator__diagrams -- "calls into" --> readmenator_parsers
    readmenator__diagrams -- "calls into" --> readmenator__pipeline
    readmenator__diagrams -- "calls into" --> readmenator__graphlayout
    readmenator__diagrams -- "calls into" --> readmenator__flowcharts
    readmenator__pipeline -- "calls into" --> readmenator__graphrag
    readmenator__pipeline -- "calls into" --> readmenator_parsers
    readmenator__pipeline -- "calls into" --> readmenator__diagrams
    readmenator__pipeline -- "calls into" --> readmenator__graphlayout
    readmenator__pipeline -- "calls into" --> readmenator__flowcharts
    readmenator__graphlayout -- "calls into" --> readmenator__graphrag
    readmenator__graphlayout -- "calls into" --> readmenator_parsers
    readmenator__graphlayout -- "calls into" --> readmenator__diagrams
    readmenator__graphlayout -- "calls into" --> readmenator__pipeline
    readmenator__graphlayout -- "calls into" --> readmenator__flowcharts
    readmenator__flowcharts -- "calls into" --> readmenator__graphrag
    readmenator__flowcharts -- "calls into" --> readmenator_parsers
    readmenator__flowcharts -- "calls into" --> readmenator__diagrams
    readmenator__flowcharts -- "calls into" --> readmenator__pipeline
    readmenator__flowcharts -- "calls into" --> readmenator__graphlayout
    click readmenator__graphrag href "./readmenator__graphrag.md" "Details"
    click readmenator_parsers href "./readmenator_parsers.md" "Details"
    click readmenator__diagrams href "./readmenator__diagrams.md" "Details"
    click readmenator__pipeline href "./readmenator__pipeline.md" "Details"
    click readmenator__graphlayout href "./readmenator__graphlayout.md" "Details"
    click readmenator__flowcharts href "./readmenator__flowcharts.md" "Details"
```

## Details

Static architecture map of 149 files (js, py) in 6 components: readmenator: _graphrag, readmenator/parsers, readmenator: _diagrams, readmenator: _pipeline, readmenator: _graphlayout, readmenator: _flowcharts. Structure is extracted statically without LLM calls; component prose may be enriched locally.

### readmenator: _graphrag (1)

readmenator: _graphrag groups 38 files (py) around Config, ImportResolver, __init__, _build_stem_index, _build_dir_index. Agent-friendly output generator for ReadMenator.

**Related Classes/Methods**:

- <a href="../readmenator/_config.py#L15-L1194">readmenator/_config.py::Config</a>
- <a href="../readmenator/_resolver.py#L18-L60">readmenator/_resolver.py::ImportResolver</a>
- <a href="../readmenator/_resolver.py#L61-L82">readmenator/_resolver.py::__init__</a>
- <a href="../readmenator/_resolver.py#L83-L92">readmenator/_resolver.py::_build_stem_index</a>
- <a href="../readmenator/_resolver.py#L93-L109">readmenator/_resolver.py::_build_dir_index</a>
- <a href="../readmenator/_resolver.py#L110-L162">readmenator/_resolver.py::resolve</a>
- <a href="../readmenator/_resolver.py#L163-L178">readmenator/_resolver.py::resolve_all</a>
- <a href="../readmenator/_resolver.py#L179-L198">readmenator/_resolver.py::_resolve_include_dirs</a>

### readmenator/parsers (2)

readmenator/parsers groups 34 files (py) around Symbol, Node, Edge, SecurityFinding, pluralize_symbol_kind. Procedural intra-function dataflow analysis for readmenator.

**Related Classes/Methods**:

- <a href="../readmenator/_models.py#L18-L36">readmenator/_models.py::Symbol</a>
- <a href="../readmenator/_models.py#L37-L57">readmenator/_models.py::Node</a>
- <a href="../readmenator/_models.py#L58-L76">readmenator/_models.py::Edge</a>
- <a href="../readmenator/_models.py#L77-L100">readmenator/_models.py::SecurityFinding</a>
- <a href="../readmenator/_models.py#L101-L110">readmenator/_models.py::pluralize_symbol_kind</a>
- <a href="../readmenator/_models.py#L111-L129">readmenator/_models.py::CommunityResult</a>
- <a href="../readmenator/_models.py#L130-L150">readmenator/_models.py::AnalysisResult</a>
- <a href="../readmenator/_models.py#L151-L171">readmenator/_models.py::TaintPath</a>

### readmenator: _diagrams (3)

readmenator: _diagrams groups 29 files (py) around EdgeKind, __str__, Morphism, weight, Category. Launcher shim that runs the readmenator CLI from a source checkout.

**Related Classes/Methods**:

- <a href="../readmenator/_category.py#L24-L37">readmenator/_category.py::EdgeKind</a>
- <a href="../readmenator/_category.py#L38-L56">readmenator/_category.py::__str__</a>
- <a href="../readmenator/_category.py#L57-L72">readmenator/_category.py::Morphism</a>
- <a href="../readmenator/_category.py#L73-L77">readmenator/_category.py::weight</a>
- <a href="../readmenator/_category.py#L78-L85">readmenator/_category.py::Category</a>
- <a href="../readmenator/_category.py#L86-L91">readmenator/_category.py::__init__</a>
- <a href="../readmenator/_category.py#L92-L94">readmenator/_category.py::add_object</a>
- <a href="../readmenator/_category.py#L95-L102">readmenator/_category.py::add_morphism</a>

### readmenator: _pipeline (4)

readmenator: _pipeline groups 20 files (py) around ReadmeInjector, __init__, inject, _extract_current_injection, _remove_old_injection. Injects KNOWLEDGE_BASE.md references into AI agent instruction files.

**Related Classes/Methods**:

- <a href="../readmenator/_readme_injector.py#L122-L132">readmenator/_readme_injector.py::ReadmeInjector</a>
- <a href="../readmenator/_readme_injector.py#L133-L191">readmenator/_readme_injector.py::__init__</a>
- <a href="../readmenator/_readme_injector.py#L192-L232">readmenator/_readme_injector.py::inject</a>
- <a href="../readmenator/_readme_injector.py#L233-L249">readmenator/_readme_injector.py::_extract_current_injection</a>
- <a href="../readmenator/_readme_injector.py#L250-L268">readmenator/_readme_injector.py::_remove_old_injection</a>
- <a href="../readmenator/_readme_injector.py#L269-L283">readmenator/_readme_injector.py::_strip_partial_anchor</a>
- <a href="../readmenator/_readme_injector.py#L284-L320">readmenator/_readme_injector.py::remove</a>
- <a href="../readmenator/_readme_injector.py#L321-L335">readmenator/_readme_injector.py::_find_readme</a>

### readmenator: _graphlayout (5)

readmenator: _graphlayout groups 13 files (py) around escape_json_for_script, should_compress, compress_text, payload_script, read_payload_script. Edge bundle explorer: circle and sphere hierarchical edge bundling pages.

**Related Classes/Methods**:

- <a href="../readmenator/_htmlpack.py#L49-L63">readmenator/_htmlpack.py::escape_json_for_script</a>
- <a href="../readmenator/_htmlpack.py#L64-L76">readmenator/_htmlpack.py::should_compress</a>
- <a href="../readmenator/_htmlpack.py#L77-L91">readmenator/_htmlpack.py::compress_text</a>
- <a href="../readmenator/_htmlpack.py#L92-L118">readmenator/_htmlpack.py::payload_script</a>
- <a href="../readmenator/_htmlpack.py#L119-L139">readmenator/_htmlpack.py::read_payload_script</a>
- <a href="../readmenator/_graphlayout.py#L40-L65">readmenator/_graphlayout.py::ForceAtlas2Settings</a>
- <a href="../readmenator/_graphlayout.py#L66-L72">readmenator/_graphlayout.py::_initial_positions</a>
- <a href="../readmenator/_graphlayout.py#L73-L112">readmenator/_graphlayout.py::forceatlas2_frames</a>

### readmenator: _flowcharts (6)

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
