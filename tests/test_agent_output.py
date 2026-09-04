import os
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from readmenator._agent_output import AgentOutputGenerator
from readmenator._config import Config
from readmenator._models import (
    AnalysisResult,
    AnalysisResultV2,
    Edge,
    HotspotResult,
    Node,
    SecurityFinding,
    Symbol,
)


def _make_node(node_id: str, symbols=None, doc: str = "", language: str = "py") -> Node:
    return Node(
        node_id=node_id,
        label=os.path.basename(node_id),
        kind="module",
        language=language,
        doc=doc,
        symbols=symbols or [],
    )


def _make_edge(source: str, target: str, relation: str = "resolved_imports") -> Edge:
    return Edge(source=source, target=target, relation=relation, confidence="EXTRACTED")


def _make_finding(
    file_path: str = "src/main.py",
    line: int = 10,
    severity: str = "high",
    rule_id: str = "PY001",
    description: str = "test finding",
    snippet: str = "eval(x)",
    cwe: str = "CWE-95",
) -> SecurityFinding:
    return SecurityFinding(
        file_path=file_path, line=line, severity=severity,
        rule_id=rule_id, description=description, snippet=snippet, cwe=cwe,
    )


class TestAgentOutputContract(unittest.TestCase):
    def test_config_defaults(self) -> None:
        config = Config()
        self.assertTrue(config.AGENT_OUTPUT_ENABLED)
        self.assertEqual(config.AGENT_OUTPUT_DIR, "readmenator-agent")
        self.assertEqual(config.AGENT_OUTPUT_MIN_SUBSYSTEM_FILES, 2)

    def test_config_immutable(self) -> None:
        from dataclasses import FrozenInstanceError
        config = Config()
        with self.assertRaises(FrozenInstanceError):
            config.AGENT_OUTPUT_ENABLED = False


class TestSubsystemInference(unittest.TestCase):
    def test_inferred_from_directories(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("src/net/sock.c"),
            _make_node("src/net/tcp.c"),
            _make_node("src/net/udp.c"),
            _make_node("src/fs/ext4.c"),
            _make_node("src/fs/vfs.c"),
        ]
        subs = gen._infer_subsystems(nodes)
        self.assertIn("net", subs)
        self.assertIn("fs", subs)
        self.assertEqual(len(subs["net"]), 3)
        self.assertEqual(len(subs["fs"]), 2)

    def test_flat_project_single_file(self) -> None:
        config = Config(AGENT_OUTPUT_MIN_SUBSYSTEM_FILES=2)
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("main.py"),
            _make_node("utils.py"),
        ]
        subs = gen._infer_subsystems(nodes)
        self.assertEqual(len(subs), 1)
        self.assertIn("root", subs)

    def test_min_threshold_respected(self) -> None:
        config = Config(AGENT_OUTPUT_MIN_SUBSYSTEM_FILES=3)
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("src/net/sock.c"),
            _make_node("src/net/tcp.c"),
            _make_node("src/fs/ext4.c"),
        ]
        subs = gen._infer_subsystems(nodes)
        self.assertIn("misc", subs)
        self.assertNotIn("net", subs)

    def test_misc_catches_unassigned(self) -> None:
        config = Config(AGENT_OUTPUT_MIN_SUBSYSTEM_FILES=2)
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("src/net/sock.c"),
            _make_node("src/net/tcp.c"),
            _make_node("standalone.py"),
        ]
        subs = gen._infer_subsystems(nodes)
        self.assertIn("net", subs)
        self.assertIn("misc", subs)
        self.assertEqual(len(subs["misc"]), 1)


class TestIndexGeneration(unittest.TestCase):
    def test_index_lists_all_files(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("a.py", doc="File A"),
            _make_node("b.py", doc="File B"),
            _make_node("c.py"),
        ]
        subs = {"root": nodes}
        content = gen._build_index(nodes, subs)
        self.assertIn("a.py", content)
        self.assertIn("b.py", content)
        self.assertIn("c.py", content)
        self.assertIn("File A", content)

    def test_index_table_format(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [_make_node("test.py")]
        subs = {"root": nodes}
        content = gen._build_index(nodes, subs)
        self.assertIn("| File |", content)
        self.assertIn("| `test.py`", content)


class TestSecurityGeneration(unittest.TestCase):
    def test_empty_findings(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        content = gen._build_security([])
        self.assertIn("No security findings", content)

    def test_findings_grouped_by_severity(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        findings = [
            _make_finding(severity="critical", file_path="a.py", line=1),
            _make_finding(severity="high", file_path="b.py", line=2),
            _make_finding(severity="critical", file_path="c.py", line=3),
            _make_finding(severity="low", file_path="d.py", line=4),
        ]
        content = gen._build_security(findings)
        self.assertIn("CRITICAL (2)", content)
        self.assertIn("HIGH (1)", content)
        self.assertIn("LOW (1)", content)
        self.assertIn("a.py:1", content)
        self.assertIn("b.py:2", content)

    def test_no_json_wrapping(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        findings = [_make_finding()]
        content = gen._build_security(findings)
        self.assertNotIn("{", content)
        self.assertNotIn("}", content)


class TestGotchasGeneration(unittest.TestCase):
    def test_god_nodes_section(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        analysis = AnalysisResult(
            god_nodes=[("src/main.py", 15.0), ("src/utils.py", 10.0)],
            communities=[],
            surprising_connections=[],
            suggested_questions=[],
            node_count=5,
            edge_count=10,
        )
        content = gen._build_gotchas(analysis, None, [])
        self.assertIn("God Nodes", content)
        self.assertIn("src/main.py", content)
        self.assertIn("15.00", content)

    def test_cycles_section(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        from readmenator._models import DependencyCycle
        analysis_v2 = AnalysisResultV2(
            taint=None,
            cycles=[DependencyCycle(cycle=["a.py", "b.py", "a.py"], length=3)],
            change_impacts=[],
            hotspots=[],
            suggested_rules=[],
            layer_violations=[],
        )
        content = gen._build_gotchas(None, analysis_v2, [])
        self.assertIn("Dependency Cycles", content)
        self.assertIn("a.py", content)
        self.assertIn("b.py", content)

    def test_empty_gotchas(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        content = gen._build_gotchas(None, None, [])
        self.assertIn("No gotchas detected", content)


class TestArchitectureGeneration(unittest.TestCase):
    def test_internal_dependencies(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [_make_node("a.py"), _make_node("b.py")]
        edges = []
        resolved = [_make_edge("a.py", "b.py")]
        content = gen._build_architecture(edges, resolved, nodes)
        self.assertIn("a.py", content)
        self.assertIn("b.py", content)
        self.assertIn("->", content)

    def test_external_imports(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [_make_node("main.py")]
        edges = [_make_edge("main.py", "os")]
        content = gen._build_architecture(edges, [], nodes)
        self.assertIn("External Imports", content)
        self.assertIn("os", content)


class TestApiGeneration(unittest.TestCase):
    def test_functions_listed(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("lib.py", symbols=[
                Symbol(name="helper", kind="function", line=10, signature="def helper(x)"),
                Symbol(name="MyClass", kind="class", line=20),
            ]),
        ]
        content = gen._build_api(nodes, {}, {})
        self.assertIn("helper", content)
        self.assertIn("def helper(x)", content)
        self.assertNotIn("MyClass", content)

    def test_no_json_in_api(self) -> None:
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [_make_node("mod.py", symbols=[
            Symbol(name="foo", kind="function", line=1),
        ])]
        content = gen._build_api(nodes, {}, {})
        self.assertNotIn("{", content)
        self.assertNotIn("}", content)


class TestSubsystemFileGeneration(unittest.TestCase):
    def test_subsystem_files_written(self) -> None:
        import tempfile
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("src/net/sock.c", symbols=[
                Symbol(name="socket_create", kind="function", line=5),
            ]),
            _make_node("src/net/tcp.c"),
        ]
        subs = {"net": nodes}
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir)
            gen._write_subsystem_files(out_dir, subs, {}, {}, {})
            kb_net = out_dir / "KB_net.md"
            self.assertTrue(kb_net.exists())
            content = kb_net.read_text()
            self.assertIn("Subsystem: net", content)
            self.assertIn("socket_create", content)


class TestRecipesGeneration(unittest.TestCase):
    def test_recipes_directory(self) -> None:
        import tempfile
        config = Config()
        gen = AgentOutputGenerator(config)
        with tempfile.TemporaryDirectory() as tmpdir:
            recipes_dir = Path(tmpdir) / "recipes"
            recipes_dir.mkdir()
            gen._write_recipes(recipes_dir, None, None)
            self.assertTrue((recipes_dir / "add-function.md").exists())
            self.assertTrue((recipes_dir / "fix-cycle.md").exists())
            self.assertTrue((recipes_dir / "fix-security.md").exists())
            self.assertTrue((recipes_dir / "reduce-complexity.md").exists())


class TestFullGenerate(unittest.TestCase):
    def test_generate_creates_all_files(self) -> None:
        import tempfile
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [
            _make_node("src/net/sock.c", symbols=[
                Symbol(name="create", kind="function", line=5),
            ]),
            _make_node("src/net/tcp.c"),
            _make_node("src/fs/ext4.c"),
            _make_node("src/fs/vfs.c"),
        ]
        resolved = [_make_edge("src/net/tcp.c", "src/net/sock.c")]
        findings = [_make_finding(file_path="src/net/sock.c", severity="critical")]
        layers = {"src/net/sock.c": "infrastructure", "src/net/tcp.c": "infrastructure"}
        with tempfile.TemporaryDirectory() as tmpdir:
            result_dir = gen.generate(
                nodes, [], resolved, None, None, findings, layers, tmpdir,
            )
            self.assertTrue(Path(result_dir).exists())
            out = Path(result_dir)
            self.assertTrue((out / "INDEX.md").exists())
            self.assertTrue((out / "ARCHITECTURE.md").exists())
            self.assertTrue((out / "SECURITY.md").exists())
            self.assertTrue((out / "API.md").exists())
            self.assertTrue((out / "GOTCHAS.md").exists())
            kb_files = list(out.glob("KB_*.md"))
            self.assertGreaterEqual(len(kb_files), 1)
            recipes = list((out / "recipes").glob("*.md"))
            self.assertGreaterEqual(len(recipes), 1)

    def test_all_files_under_500_lines(self) -> None:
        import tempfile
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [_make_node(f"file_{i}.py") for i in range(50)]
        with tempfile.TemporaryDirectory() as tmpdir:
            gen.generate(nodes, [], [], None, None, [], {}, tmpdir)
            out = Path(tmpdir) / config.AGENT_OUTPUT_DIR
            for md_file in out.rglob("*.md"):
                line_count = len(md_file.read_text().splitlines())
                self.assertLessEqual(
                    line_count, 500,
                    f"{md_file.name} has {line_count} lines (max 500)",
                )

    def test_no_json_in_any_output(self) -> None:
        import tempfile
        config = Config()
        gen = AgentOutputGenerator(config)
        nodes = [_make_node("a.py"), _make_node("b.py")]
        with tempfile.TemporaryDirectory() as tmpdir:
            gen.generate(nodes, [], [], None, None, [], {}, tmpdir)
            out = Path(tmpdir) / config.AGENT_OUTPUT_DIR
            for md_file in out.rglob("*.md"):
                content = md_file.read_text()
                self.assertNotIn('"', f"{md_file.name} contains double quotes (possible JSON)")


class TestInjectionOutdatedDetection(unittest.TestCase):
    def test_agent_injector_detects_outdated(self) -> None:
        from readmenator._agent_injector import AgentInjector, _ANCHOR, _ANCHOR_END
        import tempfile
        injector = AgentInjector(
            kb_filename="KNOWLEDGE_BASE.md",
            agent_output_dir="readmenator-agent",
        )
        old_text = (
            f"{_ANCHOR}\n"
            "## Project Knowledge Base\n"
            "OLD OUTDATED TEXT THAT SHOULD BE REPLACED\n"
            f"{_ANCHOR_END}\n"
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            claude_md = Path(tmpdir) / "CLAUDE.md"
            claude_md.write_text("# My Project\n\nSome content.\n\n" + old_text)
            modified = injector.inject(tmpdir)
            self.assertTrue(modified)
            content = claude_md.read_text()
            self.assertIn("readmenator-agent", content)
            self.assertNotIn("OLD OUTDATED TEXT", content)

    def test_agent_injector_skips_identical(self) -> None:
        from readmenator._agent_injector import AgentInjector
        import tempfile
        injector = AgentInjector(
            kb_filename="KNOWLEDGE_BASE.md",
            agent_output_dir="readmenator-agent",
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            claude_md = Path(tmpdir) / "CLAUDE.md"
            claude_md.write_text("# My Project\n")
            injector.inject(tmpdir)
            first_content = claude_md.read_text()
            modified = injector.inject(tmpdir)
            self.assertFalse(modified)
            self.assertEqual(claude_md.read_text(), first_content)

    def test_readme_injector_detects_outdated(self) -> None:
        from readmenator._readme_injector import ReadmeInjector, _ANCHOR_START, _ANCHOR_END
        import tempfile
        injector = ReadmeInjector(
            kb_filename="KNOWLEDGE_BASE.md",
            agent_output_dir="readmenator-agent",
        )
        old_text = (
            f"{_ANCHOR_START}\n"
            "## Knowledge Base\n"
            "OLD OUTDATED TEXT\n"
            f"{_ANCHOR_END}\n"
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            readme = Path(tmpdir) / "README.md"
            readme.write_text("# Project\n\n" + old_text)
            modified = injector.inject(tmpdir)
            self.assertTrue(modified)
            content = readme.read_text()
            self.assertIn("readmenator-agent", content)
            self.assertNotIn("OLD OUTDATED TEXT", content)

    def test_readme_injector_skips_identical(self) -> None:
        from readmenator._readme_injector import ReadmeInjector
        import tempfile
        injector = ReadmeInjector(
            kb_filename="KNOWLEDGE_BASE.md",
            agent_output_dir="readmenator-agent",
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            readme = Path(tmpdir) / "README.md"
            readme.write_text("# Project\n")
            injector.inject(tmpdir)
            first_content = readme.read_text()
            modified = injector.inject(tmpdir)
            self.assertFalse(modified)
            self.assertEqual(readme.read_text(), first_content)


if __name__ == "__main__":
    unittest.main()
