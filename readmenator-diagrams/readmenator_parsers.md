# readmenator/parsers

readmenator/parsers groups 34 files (py) around Symbol, Node, Edge, SecurityFinding, pluralize_symbol_kind. Hotspot, dependency cycle, and change impact analysis.

```mermaid
graph LR
    readmenator["readmenator"]
    tests["tests"]
    tests -- "calls into" --> readmenator
```

## readmenator (2.1)

readmenator groups 27 files (py) around Symbol, Node, Edge, SecurityFinding, pluralize_symbol_kind. Hotspot, dependency cycle, and change impact analysis.

## tests (2.2)

tests groups 7 files (py) around TestHotspotAnalyzerContract, setUp, _make_node, test_empty_graph_returns_empty_hotspots, test_hotspots_rank_by_combined_score. TestHotspotAnalyzerContract: Contract: HotspotAnalyzer detects hotspots, cycles, and...

**Files**:

- readmenator/_hotspots.py
- readmenator/_layer_rules.py
- readmenator/_mermaid.py
- readmenator/_models.py
- readmenator/_rule_gen.py
- readmenator/_sarif.py
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
- tests/test_hotspots.py
- tests/test_layer_rules.py
- tests/test_mermaid.py
- tests/test_models.py
- tests/test_parsers_property.py
- tests/test_rule_gen.py
- tests/test_sarif.py
