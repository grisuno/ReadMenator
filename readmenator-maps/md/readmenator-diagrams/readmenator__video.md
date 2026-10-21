# readmenator: _video

readmenator: _video groups 36 files (py) around Config, readmenatorApplication, __init__, ingest_receipts, _scan. Launcher shim that runs the readmenator CLI from a source checkout.

```mermaid
graph LR
    readmenator["readmenator"]
    root["root"]
    tests["tests"]
    root -- "calls into" --> readmenator
    tests -- "calls into" --> readmenator
```

## readmenator (2.1)

readmenator groups 17 files (py) around Config, readmenatorApplication, __init__, ingest_receipts, _scan. Command line entry point: argument parsing and subcommand dispatch.

## root (2.2)

root groups 1 files (py). Launcher shim that runs the readmenator CLI from a source checkout.

## tests (2.3)

tests groups 18 files (py) around TestConfigContract, test_config_is_immutable, test_config_defaults_are_sane, test_ignore_dirs_are_comprehensive, test_plural_map_covers_all_symbol_types. TestCodePropertyGraphContract: Contract: CodePropertyGraph generates valid JSON-LD CPG...

**Files**:

- readmenator.py
- readmenator/__main__.py
- readmenator/_app.py
- readmenator/_config.py
- readmenator/_cursorrules_generator.py
- readmenator/_dataflow.py
- readmenator/_dead_code.py
- readmenator/_hotspots.py
- readmenator/_hypotheses.py
- readmenator/_layers.py
- readmenator/_linter.py
- readmenator/_mcp_server.py
- readmenator/_receipts.py
- readmenator/_refactorizer.py
- readmenator/_uncertainty.py
- readmenator/_video.py
- readmenator/_watcher.py
- readmenator/_yaralite.py
- tests/test_config.py
- tests/test_cpg.py
- tests/test_cursorrules.py
- tests/test_dataflow.py
- tests/test_dead_code.py
- tests/test_diagrams.py
- tests/test_documentation.py
- tests/test_exporter.py
- tests/test_hotspots.py
- tests/test_htmlpack.py
- tests/test_integration.py
- tests/test_linter.py
- tests/test_mcp_server.py
- tests/test_parsers.py
- tests/test_parsers_new.py
- tests/test_receipts.py
- tests/test_refactorizer.py
- tests/test_video.py
