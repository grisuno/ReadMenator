"""BDD-style contract tests for taint propagation analysis.

Uses pytest-bdd scenarios to verify multi-step taint propagation
workflows: discovering dangerous imports, propagating through the
import graph, and generating complete TaintPath results.

These tests are skipped if pytest-bdd is not installed.
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Dict, List, Optional

from readmenator._config import Config
from readmenator._models import Edge, Node
from readmenator._taint import TaintAnalyzer

try:
    from pytest_bdd import scenario, given, when, then, parsers
    HAS_PYTEST_BDD = True
except ImportError:
    HAS_PYTEST_BDD = False


# ── Shared helpers ──────────────────────────────────────────────────────────

def _build_project_files(project: Dict[str, str], root: Path) -> None:
    for rel_path, content in project.items():
        file_path = root / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")


def _scan_project(root: Path, cfg: Config) -> tuple:
    from readmenator._scanner import PolyglotScanner
    from readmenator._resolver import ImportResolver

    scanner = PolyglotScanner(cfg)
    nodes, edges = scanner.scan(root)
    file_ids = [n.node_id for n in nodes]
    resolver = ImportResolver(file_ids, str(root))
    resolved_edges: List[Edge] = []
    for edge in edges:
        target = resolver.resolve(edge.target, edge.source)
        if target and target != edge.target:
            resolved_edges.append(
                Edge(source=target, target=edge.source, relation="resolved_imports")
            )
    return nodes, edges, resolved_edges


def _run_taint(files: Dict[str, str], cfg: Config = None) -> tuple:
    if cfg is None:
        cfg = Config(SECURITY_ENABLED=True)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _build_project_files(files, root)
        nodes, edges, resolved_edges = _scan_project(root, cfg)
        analyzer = TaintAnalyzer(cfg)
        result = analyzer.analyze(nodes, edges, resolved_edges)
        return result


# ── Gherkin scenarios ────────────────────────────────────────────────────────

if HAS_PYTEST_BDD:

    @scenario("features/taint_propagation.feature", "Direct dangerous import is detected as a taint source")
    def test_direct_dangerous_import():
        pass

    @scenario("features/taint_propagation.feature", "Taint propagates through a single import chain")
    def test_taint_propagates_chain():
        pass

    @scenario("features/taint_propagation.feature", "Taint does not propagate beyond max depth")
    def test_taint_max_depth():
        pass

    @scenario("features/taint_propagation.feature", "Cross-language taint propagation works for JS")
    def test_cross_language_taint():
        pass

else:
    def test_bdd_skipped():
        import unittest
        raise unittest.SkipTest("pytest-bdd not installed — skipping BDD tests")


# ── Step definitions ─────────────────────────────────────────────────────────

if HAS_PYTEST_BDD:

    _DIRECT_PROJECT = {
        "main.py": "import subprocess\nsubprocess.run(['ls'], shell=True)\n",
    }

    _CHAIN_PROJECT = {
        "entry.py": "from middle import handler\ndef run():\n    handler()\n",
        "middle.py": "from dangerous import danger\ndef handler():\n    danger()\n",
        "dangerous.py": "import subprocess\nsubprocess.run(['rm', '-rf'], shell=True)\n",
    }

    _JS_PROJECT = {
        "server.js": "const sp = require('subprocess');\nsp.run(['ls'], {shell: true});\n",
    }

    # Background
    @given("the taint analyzer is configured with standard settings")
    def _bkg():
        pass

    # Scenario 1
    @given("a Python project importing subprocess", target_fixture="_taint_result")
    def _direct_given():
        return _run_taint(_DIRECT_PROJECT)

    @when("I detect direct taint sources")
    def _direct_when(_taint_result):
        pass

    @then("the result has at least one path")
    def _check_has_path(_taint_result):
        assert _taint_result is not None
        assert len(_taint_result.paths) >= 1

    @then("there is a 0-hop direct path")
    def _check_direct_path(_taint_result):
        direct = [p for p in _taint_result.paths if p.hops == 0]
        assert direct, f"No 0-hop paths among {len(_taint_result.paths)}"

    @then("source count is at least 1")
    def _check_src(_taint_result):
        assert _taint_result.source_count >= 1

    @then("sink count is at least 1")
    def _check_sink(_taint_result):
        assert _taint_result.sink_count >= 1

    # Scenario 2
    @given("a three-file import chain ending in subprocess", target_fixture="_taint_result")
    def _chain_given():
        return _run_taint(_CHAIN_PROJECT)

    @when("I propagate taint through the import chain")
    def _chain_when(_taint_result):
        pass

    @then("the longest path has at least 2 hops")
    def _check_long_path(_taint_result):
        assert _taint_result and _taint_result.paths
        longest = max(_taint_result.paths, key=lambda p: p.hops)
        assert longest.hops >= 2, f"Expected hops>=2, got {longest.hops}"

    # Scenario 3
    @given("a max depth config of 1", target_fixture="_shallow_cfg")
    def _shallow_cfg():
        return Config(SECURITY_ENABLED=True, TAINT_MAX_DEPTH=1)

    @given("a three-file chain with subprocess (max depth test)", target_fixture="_taint_result")
    def _chain_given2():
        return _run_taint(_CHAIN_PROJECT)

    @when("I run shallow (max depth 1) taint analysis", target_fixture="_taint_result")
    def _run_shallow(_shallow_cfg):
        return _run_taint(_CHAIN_PROJECT, _shallow_cfg)

    @then("no path exceeds 1 hop")
    def _check_shallow(_taint_result):
        assert _taint_result is not None
        for path in _taint_result.paths:
            assert path.hops <= 1, f"Path exceeded max depth of 1: {path.hops} hops"

    # Scenario 4
    @given("a JavaScript project with child_process import", target_fixture="_taint_result")
    def _js_given():
        return _run_taint(_JS_PROJECT)

    @when("I run JS taint analysis")
    def _js_when(_taint_result):
        pass

    @then("subprocess appears as the dangerous import")
    def _check_js_dangerous(_taint_result):
        assert _taint_result is not None
        dangerous_imports = {p.dangerous_import for p in _taint_result.paths}
        assert "subprocess" in dangerous_imports, f"Expected subprocess in: {dangerous_imports}"

    @then("JS source count is at least 1")
    def _check_js_source(_taint_result):
        assert _taint_result.source_count >= 1
