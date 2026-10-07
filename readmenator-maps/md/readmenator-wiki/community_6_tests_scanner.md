# tests: _scanner

*Community 6 | 5 files | cohesion 0.21*

## Definition

This community groups 5 file(s) rooted at `tests` with dominant language py (cohesion 0.21). Central symbols: `PolyglotScanner`, `TaintAnalyzer`, `TestScannerContract`, `TestTaintAnalyzerContract`, `__init__`, `_bkg`, `_build_forward_graph`, `_build_project_files`. Core file: `tests/test_taint_bdd.py` (26 symbols). Documented purpose: Secure polyglot directory traversal and file analysis.  The scanner walks a directory tree, applies security and size checks, resolves each supported file throu.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_scanner.py` | py | utility | 14 | yes |
| `readmenator/_taint.py` | py | utility | 6 | yes |
| `tests/test_scanner.py` | py | testing | 21 | no |
| `tests/test_taint.py` | py | testing | 10 | no |
| `tests/test_taint_bdd.py` | py | testing | 26 | yes |

## Key Symbols

- `PolyglotScanner` (class, `readmenator/_scanner.py:28`) `class PolyglotScanner` - Recursive directory scanner with security and size guards.
- `__init__` (method, `readmenator/_scanner.py:39`) `def __init__(self, config)` - Initialise the scanner with application configuration.
- `_is_ignored` (method, `readmenator/_scanner.py:50`) `def _is_ignored(self, path)` - Return ``True`` if any path component matches IGNORE_DIRS.
- `_is_generated` (method, `readmenator/_scanner.py:57`) `def _is_generated(self, rel_path)` - Return ``True`` for artifacts readmenator itself wrote into the project.
- `_load_gitignore` (method, `readmenator/_scanner.py:83`) `def _load_gitignore(self, root)` - Parse .gitignore patterns using regex (no external deps).
- `_gitignore_glob_to_regex` (method, `readmenator/_scanner.py:105`) `def _gitignore_glob_to_regex(pattern)` - Convert a .gitignore glob pattern to a regex pattern.
- `_is_gitignored` (method, `readmenator/_scanner.py:145`) `def _is_gitignored(self, rel_path)` - Check if a relative path matches any .gitignore pattern.
- `_validate_path_security` (method, `readmenator/_scanner.py:154`) `def _validate_path_security(self, path)` - Reject symlinks and files exceeding MAX_FILE_SIZE_MB.
- `_check_directory_depth` (method, `readmenator/_scanner.py:167`) `def _check_directory_depth(self, path, root)` - Return ``True`` if *path* is within MAX_DIRECTORY_DEPTH of *root*.
- `_extract_file_doc` (method, `readmenator/_scanner.py:175`) `def _extract_file_doc(self, content)` - Extract a file-level docstring from the first lines of a source file.
- `_emit_progress` (method, `readmenator/_scanner.py:251`) `def _emit_progress(self, count)` - Emit a progress message every PROGRESS_REPORT_BATCH files.
- `scan` (method, `readmenator/_scanner.py:261`) `def scan(self, root)` - Walk *root* recursively and produce (nodes, edges) for the graph.
- `scan_with_content` (method, `readmenator/_scanner.py:275`) `def scan_with_content(self, root)` - Scan and also return raw file contents for deeper analysis.
- `_scan_impl` (method, `readmenator/_scanner.py:286`) `def _scan_impl(self, root)` - Internal scan implementation returning nodes, edges, and content.
- `TaintAnalyzer` (class, `readmenator/_taint.py:12`) `class TaintAnalyzer` - Propagation-based taint analysis over the resolved import graph.
- `__init__` (method, `readmenator/_taint.py:73`) `def __init__(self, config)`
- `analyze` (method, `readmenator/_taint.py:77`) `def analyze(self, nodes, edges, resolved_edges)` - Run taint propagation analysis on the codebase.
- `_find_direct_sources` (method, `readmenator/_taint.py:136`) `def _find_direct_sources(self, nodes, edges)` - Find files that directly import known-dangerous modules.
- `_propagate` (method, `readmenator/_taint.py:162`) `def _propagate(self, source_node_id, danger_import, adj, nodes, max_depth)` - BFS propagation from source through the import graph.
- `_build_forward_graph` (method, `readmenator/_taint.py:213`) `def _build_forward_graph(nodes, resolved_edges)` - Build a forward-directed import graph from resolved edges.
- `TestScannerContract` (class, `tests/test_scanner.py:11`) `class TestScannerContract(TestCase)`
- `setUp` (method, `tests/test_scanner.py:12`) `def setUp(self)`
- `tearDown` (method, `tests/test_scanner.py:16`) `def tearDown(self)`
- `_write` (method, `tests/test_scanner.py:20`) `def _write(self, path, content)`
- `test_scans_python_files` (method, `tests/test_scanner.py:25`) `def test_scans_python_files(self)`
- `test_ignores_env_and_vendor_dirs` (method, `tests/test_scanner.py:32`) `def test_ignores_env_and_vendor_dirs(self)`
- `test_rejects_symlinks` (method, `tests/test_scanner.py:45`) `def test_rejects_symlinks(self)`
- `test_skips_non_code_files` (method, `tests/test_scanner.py:59`) `def test_skips_non_code_files(self)`
- `test_scans_multiple_languages` (method, `tests/test_scanner.py:70`) `def test_scans_multiple_languages(self)`
- `test_respects_max_directory_depth` (method, `tests/test_scanner.py:79`) `def test_respects_max_directory_depth(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 4
- Cross-boundary resolved imports (EXTRACTED): 15

## Connections

- [EXTRACTED] depends_on community 0 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_pipeline.py imports readmenator/_scanner.py.
- [EXTRACTED] depends_on community 6 <-> 5 (strength 0.9): Extracted import edge crosses communities: readmenator/_scanner.py imports readmenator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 6 (strength 0.9): Extracted import edge crosses communities: tests/test_agent_friendliness.py imports readmenator/_scanner.py.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_scanner.py`)? What purpose do they serve?
- What would break if the most connected file in tests: _scanner changed?
- Should tests: _scanner be split, given cohesion 0.21?

## Sources

- `readmenator/_scanner.py`
- `readmenator/_taint.py`
- `tests/test_scanner.py`
- `tests/test_taint.py`
- `tests/test_taint_bdd.py`
