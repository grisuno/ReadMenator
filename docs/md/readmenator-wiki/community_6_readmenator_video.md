# readmenator: _video

*Community 6 | 13 files | cohesion 0.29*

## Definition

This community groups 13 file(s) rooted at `tests` with dominant language py (cohesion 0.29). Central symbols: `AudioCue`, `Backdrop`, `CinematicVideoRenderer`, `GitHistoryReader`, `HistoryRelease`, `ImportResolver`, `PolyglotScanner`, `SoundtrackComposer`. Core file: `readmenator/_video.py` (114 symbols). Documented purpose: Git history replay: read release snapshots from a repository.  The video needs the growth story of a project, not only its final shape. This module walks the gi.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `readmenator/_githistory.py` | py | utility | 23 | yes |
| `readmenator/_resolver.py` | py | utility | 17 | yes |
| `readmenator/_scanner.py` | py | utility | 16 | yes |
| `readmenator/_soundtrack.py` | py | utility | 27 | yes |
| `readmenator/_taint.py` | py | utility | 6 | yes |
| `readmenator/_video.py` | py | utility | 114 | yes |
| `tests/test_githistory.py` | py | testing | 22 | yes |
| `tests/test_resolver.py` | py | testing | 22 | yes |
| `tests/test_scanner.py` | py | testing | 21 | no |
| `tests/test_soundtrack.py` | py | testing | 51 | yes |
| `tests/test_taint.py` | py | testing | 10 | no |
| `tests/test_taint_bdd.py` | py | testing | 26 | yes |
| `tests/test_video.py` | py | testing | 30 | yes |

## Key Symbols

- `HistoryRelease` (class, `readmenator/_githistory.py:43`) `class HistoryRelease` - One point of the repository timeline.
- `GitHistoryReader` (class, `readmenator/_githistory.py:67`) `class GitHistoryReader` - Read release snapshots from a git repository (read-only).
- `__init__` (method, `readmenator/_githistory.py:76`) `def __init__(self, config, runner)` - Initialise the reader with configuration and optional runner.
- `available` (method, `readmenator/_githistory.py:81`) `def available(self, project_root)` - Return ``True`` when the target looks like a readable git checkout.
- `timeline` (method, `readmenator/_githistory.py:100`) `def timeline(self, project_root)` - Build the ordered release timeline of a repository.
- `_entries` (method, `readmenator/_githistory.py:139`) `def _entries(self, root)` - Collect ``(label, ref, commit, date)`` points of the timeline.
- `_genesis` (method, `readmenator/_githistory.py:162`) `def _genesis(self, root)` - Return the root commits of the current history with their dates.
- `_tags` (method, `readmenator/_githistory.py:171`) `def _tags(self, root)` - Return ``(ref, commit, date)`` for every tag, oldest first.
- `_head` (method, `readmenator/_githistory.py:191`) `def _head(self, root)` - Return the HEAD commit sha and its date.
- `_commit_date` (method, `readmenator/_githistory.py:198`) `def _commit_date(self, root, commit)` - Return the ISO date of a commit.
- `_snapshot` (method, `readmenator/_githistory.py:202`) `def _snapshot(self, root, label, ref, commit, date)` - Materialise and parse the source tree of one commit.
- `_resolve_links` (method, `readmenator/_githistory.py:233`) `def _resolve_links(self, file_ids, edges, root)` - Resolve raw import strings into project-internal file pairs.
- `_source_files` (method, `readmenator/_githistory.py:247`) `def _source_files(self, tree)` - Filter a tree listing down to parseable, non-generated sources.
- `_is_source` (method, `readmenator/_githistory.py:261`) `def _is_source(self, path, scanner)` - Return ``True`` when a tracked path is a source file worth parsing.
- `_tree` (method, `readmenator/_githistory.py:274`) `def _tree(self, root, commit)` - Return ``(blob_sha, path)`` for every file tracked at a commit.
- `_blobs` (method, `readmenator/_githistory.py:279`) `def _blobs(self, root, shas)` - Read blob contents for the given object ids.
- `_git` (method, `readmenator/_githistory.py:296`) `def _git(self, root, args)` - Run a git command and return its stdout as text.
- `_git_bytes` (method, `readmenator/_githistory.py:301`) `def _git_bytes(self, root, args)` - Run a git command and return its raw stdout.
- `_run` (method, `readmenator/_githistory.py:308`) `def _run(self, root, args, stdin_file, stdout_file)` - Run a git command with a timeout, returning ``None`` on failure.
- `_git_env` (method, `readmenator/_githistory.py:333`) `def _git_env()` - Return the environment for git calls, without repository overrides.
- `_version_label` (method, `readmenator/_githistory.py:341`) `def _version_label(ref)` - Normalise a tag name into a version label.
- `_parse_tree` (method, `readmenator/_githistory.py:353`) `def _parse_tree(raw)` - Parse ``git ls-tree -r -z`` output into ``(sha, path)`` pairs.
- `_parse_blobs` (method, `readmenator/_githistory.py:367`) `def _parse_blobs(payload)` - Parse ``git cat-file --batch`` output into ``{sha: content}``.
- `ImportResolver` (class, `readmenator/_resolver.py:18`) `class ImportResolver` - Resolves raw import strings to project file paths.
- `__init__` (method, `readmenator/_resolver.py:61`) `def __init__(self, file_ids, root, extensions, include_dirs)` - Initialise the resolver with all known file paths.
- `_build_stem_index` (method, `readmenator/_resolver.py:83`) `def _build_stem_index(self, file_ids)` - Map file stems (without extension) to their full paths.
- `_build_dir_index` (method, `readmenator/_resolver.py:93`) `def _build_dir_index(self, file_ids)` - Map directory paths to the files they contain.
- `resolve` (method, `readmenator/_resolver.py:110`) `def resolve(self, import_str, source_file)` - Resolve an import string to a concrete project file path.
- `resolve_all` (method, `readmenator/_resolver.py:163`) `def resolve_all(self, import_str, source_file)` - Resolve *import_str* to all possible matching project file paths.
- `_resolve_include_dirs` (method, `readmenator/_resolver.py:179`) `def _resolve_include_dirs(self, import_str)` - Resolve *import_str* against configured ``-I`` include dirs.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 17
- Cross-boundary resolved imports (EXTRACTED): 34

## Connections

- [EXTRACTED] depends_on community 2 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_agent_output.py imports readmenator/_resolver.py.
- [EXTRACTED] depends_on community 0 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_app.py imports readmenator/_resolver.py.
- [EXTRACTED] depends_on community 3 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_forcegraph.py imports readmenator/_resolver.py.
- [EXTRACTED] depends_on community 4 <-> 6 (strength 0.9): Extracted import edge crosses communities: readmenator/_graphrag.py imports readmenator/_resolver.py.
- [EXTRACTED] depends_on community 6 <-> 1 (strength 0.9): Extracted import edge crosses communities: readmenator/_scanner.py imports readmenator/_models.py.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `tests/test_scanner.py`)? What purpose do they serve?
- What would break if the most connected file in readmenator: _video changed?
- Should readmenator: _video be split, given cohesion 0.29?

## Sources

- `readmenator/_githistory.py`
- `readmenator/_resolver.py`
- `readmenator/_scanner.py`
- `readmenator/_soundtrack.py`
- `readmenator/_taint.py`
- `readmenator/_video.py`
- `tests/test_githistory.py`
- `tests/test_resolver.py`
- `tests/test_scanner.py`
- `tests/test_soundtrack.py`
- `tests/test_taint.py`
- `tests/test_taint_bdd.py`
- `tests/test_video.py`
