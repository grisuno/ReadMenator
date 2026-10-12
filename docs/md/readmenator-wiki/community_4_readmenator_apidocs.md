# readmenator: _apidocs

*Community 4 | 14 files | cohesion 0.37*

## Definition

This community groups 14 file(s) rooted at `readmenator` with dominant language py (cohesion 0.37). Central symbols: `ApiDocsWriter`, `ApiEntity`, `ApiLinker`, `ApiMarkdownRenderer`, `ApiParam`, `ApiReference`, `ApiReferenceBuilder`, `ArchitectureDiagramBuilder`. Core file: `readmenator/_apidocs.py` (52 symbols). Documented purpose: Deterministic API reference model: extraction, cross-references, coverage.  Builds a Sphinx / Doxygen style API reference from the scanned graph with zero token.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_apidocs.py` | py | utility | 52 | yes |
| `readmenator/_apidocs_page.py` | py | presentation | 2 | yes |
| `readmenator/_apidocs_render.py` | py | presentation | 39 | yes |
| `readmenator/_cpg.py` | py | utility | 6 | yes |
| `readmenator/_docstrings.py` | py | utility | 30 | yes |
| `readmenator/_documentation.py` | py | utility | 31 | yes |
| `readmenator/_flowcharts.py` | py | utility | 46 | yes |
| `readmenator/_pytypes.py` | py | utility | 16 | yes |
| `readmenator/_uml.py` | py | utility | 25 | yes |
| `tests/test_apidocs.py` | py | testing | 44 | yes |
| `tests/test_cpg.py` | py | testing | 11 | no |
| `tests/test_documentation.py` | py | testing | 29 | no |
| `tests/test_flowcharts.py` | py | testing | 26 | yes |
| `tests/test_uml.py` | py | testing | 49 | yes |

## Key Symbols

- `ApiParam` (class, `readmenator/_apidocs.py:76`) `class ApiParam` - One parameter of a callable signature.
- `to_dict` (method, `readmenator/_apidocs.py:91`) `def to_dict(self)` - Serialise to a plain dict for JSON output.
- `ApiEntity` (class, `readmenator/_apidocs.py:98`) `class ApiEntity` - One documented API element (module, type, callable, or data member).
- `is_documented` (method, `readmenator/_apidocs.py:156`) `def is_documented(self)` - Return True when any documentation text was found.
- `to_dict` (method, `readmenator/_apidocs.py:160`) `def to_dict(self)` - Serialise to a plain dict for JSON output.
- `DocWarning` (class, `readmenator/_apidocs.py:180`) `class DocWarning` - One documentation quality warning.
- `to_dict` (method, `readmenator/_apidocs.py:197`) `def to_dict(self)` - Serialise to a plain dict for JSON output.
- `ApiReference` (class, `readmenator/_apidocs.py:204`) `class ApiReference` - Complete API reference for one project.
- `children` (method, `readmenator/_apidocs.py:221`) `def children(self, uid, kinds)` - Return direct members of *uid*, optionally filtered by kind, in source order.
- `to_dict` (method, `readmenator/_apidocs.py:232`) `def to_dict(self, schema_version)` - Serialise the whole reference for ``api.json``.
- `_unparse` (function, `readmenator/_apidocs.py:244`) `def _unparse(node)` - Return the source text of an AST node ("" for None).
- `_PythonExtractor` (class, `readmenator/_apidocs.py:254`) `class _PythonExtractor` - Extracts Python API entities with the native ``ast`` module.
- `__init__` (method, `readmenator/_apidocs.py:257`) `def __init__(self, file_id, language, include_private)` - Initialise for one file.
- `extract` (method, `readmenator/_apidocs.py:272`) `def extract(self, content)` - Parse *content*; return False when it is not valid Python.
- `_read_all` (method, `readmenator/_apidocs.py:286`) `def _read_all(tree)` - Return the names listed in a literal module ``__all__``.
- `_visibility` (method, `readmenator/_apidocs.py:305`) `def _visibility(self, name, parent_uid)` - Classify *name* as public, protected, or private.
- `_keep` (method, `readmenator/_apidocs.py:317`) `def _keep(self, name, visibility, documented)` - Return True when the entity belongs in the reference.
- `_walk_body` (method, `readmenator/_apidocs.py:325`) `def _walk_body(self, body, parent_uid, prefix)` - Extract entities from one statement list; return member uids.
- `_class` (method, `readmenator/_apidocs.py:344`) `def _class(self, node, parent_uid, prefix)` - Extract one class and its members.
- `_params` (method, `readmenator/_apidocs.py:391`) `def _params(self, args, drop_receiver)` - Convert ``ast.arguments`` into ordered ApiParam records.
- `_render_params` (method, `readmenator/_apidocs.py:410`) `def _render_params(params, args, receiver)` - Render a parameter list including ``/`` and ``*`` separators.
- `_body_facts` (method, `readmenator/_apidocs.py:432`) `def _body_facts(node)` - Return (raised exception names, returns a value, is generator).
- `_function` (method, `readmenator/_apidocs.py:455`) `def _function(self, node, parent_uid, prefix, in_class)` - Extract one function, method, property, or constructor.
- `_data` (method, `readmenator/_apidocs.py:513`) `def _data(self, stmt, body, pos, parent_uid, prefix, in_class)` - Extract a module constant or class attribute.
- `_matching_close` (function, `readmenator/_apidocs.py:564`) `def _matching_close(lines, start, scan_limit)` - Return the zero-based line closing the first ``{`` at or after *start*.
- `_indent_end` (function, `readmenator/_apidocs.py:620`) `def _indent_end(lines, start)` - Return the zero-based last line of an indentation block opened at *start*.
- `_split_top_level` (function, `readmenator/_apidocs.py:639`) `def _split_top_level(text, sep)` - Split *text* on *sep* outside brackets and strings.
- `_param_span` (function, `readmenator/_apidocs.py:668`) `def _param_span(signature, name)` - Return the (open, close) indexes of the parameter list after *name*.
- `parse_signature_params` (function, `readmenator/_apidocs.py:685`) `def parse_signature_params(signature, name, language)` - Split a non-Python signature into parameters and a return type.
- `is_vendored_path` (function, `readmenator/_apidocs.py:759`) `def is_vendored_path(file_id, config)` - Return True for minified bundles and files under vendored third-party trees.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 21
- Cross-boundary resolved imports (EXTRACTED): 40

## Connections

- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: readmenator/__init__.py imports readmenator/_uml.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_apidocs.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 3 (strength 0.9): Extracted import edge crosses communities: readmenator/_documentation.py imports readmenator/_analytics.py.
- [INFERRED] bridges community 4 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator/_docstrings.py reaches tests/test_graphlayout.py in 5 hops.
- [INFERRED] bridges community 4 <-> 3 (strength 0.5): Inferred cross-community bridge: readmenator/_pytypes.py reaches tests/test_graphlayout.py in 5 hops.

## Risks

- [taint high] `readmenator/_documentation.py` -> `readmenator/_documentation.py` via `subprocess` (0 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_mermaid.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_config.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_analytics.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_cpg.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_rank.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_flowcharts.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_uml.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_models.py` via `subprocess` (1 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_graphlayout.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_purpose.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_forcegraph_page.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_resolver.py` via `subprocess` (2 hops)
- [taint high] `readmenator/_documentation.py` -> `readmenator/_sourceview.py` via `subprocess` (2 hops)

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_cpg.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `readmenator/_documentation.py` still required, or can it be isolated?
- What would break if the most connected file in readmenator: _apidocs changed?
- Should readmenator: _apidocs be split, given cohesion 0.37?

## Sources

- `readmenator/_apidocs.py`
- `readmenator/_apidocs_page.py`
- `readmenator/_apidocs_render.py`
- `readmenator/_cpg.py`
- `readmenator/_docstrings.py`
- `readmenator/_documentation.py`
- `readmenator/_flowcharts.py`
- `readmenator/_pytypes.py`
- `readmenator/_uml.py`
- `tests/test_apidocs.py`
- `tests/test_cpg.py`
- `tests/test_documentation.py`
- `tests/test_flowcharts.py`
- `tests/test_uml.py`
