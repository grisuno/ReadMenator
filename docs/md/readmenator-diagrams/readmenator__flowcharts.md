# readmenator: _flowcharts

readmenator: _flowcharts groups 12 files (py) around _receiver_text, SymbolDef, CallSite, ResolvedCall, _kind_to_node_type. Deterministic API reference model: extraction, cross-references, coverage.

```mermaid
graph LR
    readmenator["readmenator"]
    tests["tests"]
    tests -- "calls into" --> readmenator
```

## readmenator (6.1)

readmenator groups 9 files (py) around _receiver_text, SymbolDef, CallSite, ResolvedCall, _kind_to_node_type. Deterministic API reference model: extraction, cross-references, coverage.

## tests (6.2)

tests groups 3 files (py) around _project, TestDocstringParser, test_docstrings_google_sections, test_docstrings_numpy_sections, test_docstrings_rest_fields_and_directives. Contract tests for the docstring parser and the deterministic API reference.

**Files**:

- readmenator/_apidocs.py
- readmenator/_apidocs_page.py
- readmenator/_apidocs_render.py
- readmenator/_docstrings.py
- readmenator/_flowcharts.py
- readmenator/_flowlayout.py
- readmenator/_flowpage.py
- readmenator/_pytypes.py
- readmenator/_symindex.py
- tests/test_apidocs.py
- tests/test_flowcharts.py
- tests/test_symindex.py
