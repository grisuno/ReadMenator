# readmenator/parsers

readmenator/parsers groups 37 files (py) around Symbol, Node, Edge, SecurityFinding, pluralize_symbol_kind. Dead code detection for the readmenator knowledge graph.

```mermaid
graph LR
    readmenator["readmenator"]
    tests["tests"]
    tests -- "calls into" --> readmenator
```

## readmenator (2.1)

readmenator groups 28 files (py) around Symbol, Node, Edge, SecurityFinding, pluralize_symbol_kind. Dead code detection for the readmenator knowledge graph.

## tests (2.2)

tests groups 9 files (py) around TestDeadCodeStripperContract, setUp, _make_symbol, _make_node, _make_edge. Contract tests for the DeadCodeStripper.

**Files**:

- readmenator/_dead_code.py
- readmenator/_mermaid.py
- readmenator/_models.py
- readmenator/_refactorizer.py
- readmenator/_sarif.py
- readmenator/_scanner.py
- readmenator/_taint.py
- readmenator/parsers/__init__.py
- readmenator/parsers/_assembly.py
- readmenator/parsers/_base.py
- readmenator/parsers/_c.py
- readmenator/parsers/_csharp.py
- readmenator/parsers/_dart.py
- readmenator/parsers/_elixir.py
- readmenator/parsers/_gdscript.py
- readmenator/parsers/_go.py
- readmenator/parsers/_java.py
- readmenator/parsers/_javascript.py
- readmenator/parsers/_kotlin.py
- readmenator/parsers/_lua.py
- readmenator/parsers/_nim.py
- readmenator/parsers/_php.py
- readmenator/parsers/_python.py
- readmenator/parsers/_ruby.py
- readmenator/parsers/_rust.py
- readmenator/parsers/_scala.py
- readmenator/parsers/_shell.py
- readmenator/parsers/_swift.py
- tests/test_dead_code.py
- tests/test_mermaid.py
- tests/test_models.py
- tests/test_parsers_property.py
- tests/test_refactorizer.py
- tests/test_sarif.py
- tests/test_scanner.py
- tests/test_taint.py
- tests/test_taint_bdd.py
