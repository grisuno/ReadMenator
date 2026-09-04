from __future__ import annotations

import argparse
import logging
import sys
import unittest
from pathlib import Path

from readmenator._app import readmenatorApplication
from readmenator._mcp_server import main as mcp_main

logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="ReadMenator: Zero-token polyglot codebase knowledge graph generator.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Subcommands:\n"
            "  query \"<question>\"      Answer a question using the knowledge base\n"
            "  explain \"<symbol>\"      Explain a symbol with relationships\n"
            "  path \"<A>\" \"<B>\"        Trace dependency chain between two symbols\n"
            "  summary | sum | info    Print a concise codebase overview\n"
            "  analyze                 Run community detection and analysis\n"
            "  update                  Incremental rebuild (cache-based)\n"
            "  export                  Export graph (JSON + HTML + SVG)\n"
            "  audit                   Run static security analysis\n"
            "  audit-deep              Run deep analysis (taint, hotspots, cycles)\n"
            "  export-sarif            Export security findings as SARIF\n"
            "  export-rules            Export suggested linting rules as Semgrep YAML\n"
            "  graphml                 Export graph as GraphML (Gephi/yEd)\n"
            "  cypher                  Export graph as Cypher (Neo4j/Memgraph)\n"
            "  uml                     Generate UML class diagram and print\n"
            "  serve [path]            Start MCP stdio server for AI agent queries\n"
            "  lint                    Run architecture linter and report violations\n"
            "  strip-dead-code         Identify orphaned symbols (dead code)\n"
            "  generate-rules          Generate .cursorrules for AI assistants\n"
            "  refactor-monolith       Generate refactoring plans for large files\n"
            "\n"
            "Flags:\n"
            "  --rebuild               Force full regeneration\n"
            "  --audit                 Include security audit in output\n"
            "  --json                  Export graph.json\n"
            "  --html                  Export graph.html (interactive)\n"
            "  --svg                   Export graph.svg (static)\n"
            "  --export-all            Export all formats (JSON + HTML + SVG)\n"
            "  --graphml               Export graph.graphml\n"
            "  --cypher                Export graph.cypher (Neo4j/Memgraph)\n"
            "  --test                  Run the test suite\n"
            "  --privacy               Privacy mode (strip snippets and docstrings)\n"
            "  --no-agent-injection    Skip injecting KB reference into AI agent files\n"
            "  --no-agent-output       Skip generating agent-friendly output directory\n"
            "  --sarif                 Generate SARIF audit file\n"
            "  --context-budget N      Target token budget for KB (0 = full output)\n"
            "  --c++                   Generate C++ class declarations from UML\n"
            "  --java                  Generate Java class declarations from UML\n"
            "  --csharp                Generate C# class declarations from UML\n"
            "  --python-classes        Generate Python class declarations from UML\n"
            "  --go-classes            Generate Go type declarations from UML\n"
            "  --rust-classes          Generate Rust type declarations from UML\n"
            "  --php-classes           Generate PHP class declarations from UML\n"
            "  --kotlin                Generate Kotlin class declarations from UML\n"
            "  --scala                 Generate Scala class declarations from UML\n"
            "  --swift-classes         Generate Swift type declarations from UML\n"
            "  --dart-classes          Generate Dart class declarations from UML\n"
            "  --ruby-classes          Generate Ruby class declarations from UML\n"
        ),
    )
    parser.add_argument("target", nargs="?", default=".", help="Target directory to analyze (default: current directory)")
    parser.add_argument("--rebuild", action="store_true", help="Force regeneration of KNOWLEDGE_BASE.md")
    parser.add_argument("--test", action="store_true", help="Run the built-in test suite")
    parser.add_argument("--json", action="store_true", help="Export graph.json")
    parser.add_argument("--html", action="store_true", help="Export graph.html (interactive visualization)")
    parser.add_argument("--svg", action="store_true", help="Export graph.svg (static visualization)")
    parser.add_argument("--export-all", action="store_true", help="Export all formats (JSON + HTML + SVG)")
    parser.add_argument("--graphml", action="store_true", help="Export graph.graphml (Gephi/yEd)")
    parser.add_argument("--cypher", action="store_true", help="Export graph.cypher (Neo4j/Memgraph)")
    parser.add_argument("--no-analysis", action="store_true", help="Skip community detection and graph analysis")
    parser.add_argument("--audit", action="store_true", help="Run static security analysis and include findings in output")
    parser.add_argument("--privacy", action="store_true", help="Privacy mode: strip source snippets and docstrings from output")
    parser.add_argument("--no-agent-injection", dest="no_agent_injection", action="store_true", help="Skip injecting KB reference into AI agent files")
    parser.add_argument("--no-agent-output", dest="no_agent_output", action="store_true", help="Skip generating agent-friendly output directory")
    parser.add_argument("--sarif", action="store_true", help="Generate SARIF audit file alongside KNOWLEDGE_BASE.md")
    parser.add_argument("--context-budget", type=int, default=0, help="Target token budget for KNOWLEDGE_BASE.md summary (0 = full output)")
    parser.add_argument("--c++", dest="cpp", action="store_true", help="Generate C++ class declarations from UML")
    parser.add_argument("--java", action="store_true", help="Generate Java class declarations from UML")
    parser.add_argument("--csharp", action="store_true", help="Generate C# class declarations from UML")
    parser.add_argument("--python-classes", dest="python_classes", action="store_true", help="Generate Python class declarations from UML")
    parser.add_argument("--go-classes", dest="go_classes", action="store_true", help="Generate Go type declarations from UML")
    parser.add_argument("--rust-classes", dest="rust_classes", action="store_true", help="Generate Rust type declarations from UML")
    parser.add_argument("--php-classes", dest="php_classes", action="store_true", help="Generate PHP class declarations from UML")
    parser.add_argument("--kotlin", action="store_true", help="Generate Kotlin class declarations from UML")
    parser.add_argument("--scala", action="store_true", help="Generate Scala class declarations from UML")
    parser.add_argument("--swift-classes", dest="swift_classes", action="store_true", help="Generate Swift type declarations from UML")
    parser.add_argument("--dart-classes", dest="dart_classes", action="store_true", help="Generate Dart class declarations from UML")
    parser.add_argument("--ruby-classes", dest="ruby_classes", action="store_true", help="Generate Ruby class declarations from UML")
    return parser


def _run_tests() -> None:
    package_dir = Path(__file__).resolve().parent.parent
    tests_dir = package_dir / "tests"
    if tests_dir.is_dir():
        sys.path.insert(0, str(package_dir))
        loader = unittest.TestLoader()
        suite = loader.discover(str(tests_dir), pattern="test_*.py")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)
    else:
        logger.error("No tests directory found.")
        sys.exit(1)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
    )

    if "--test" in sys.argv:
        _run_tests()
        return

    has_export_flags = any(
        f in sys.argv for f in {"--json", "--html", "--svg", "--export-all", "--graphml", "--cypher"}
    )

    uml_lang_flags = {
        "--c++": "cpp", "--java": "java", "--csharp": "csharp",
        "--python-classes": "python", "--go-classes": "go",
        "--rust-classes": "rust", "--php-classes": "php",
        "--kotlin": "kotlin", "--scala": "scala",
        "--swift-classes": "swift", "--dart-classes": "dart",
        "--ruby-classes": "ruby",
    }
    uml_codegen_flag: Optional[str] = None
    for flag, lang in uml_lang_flags.items():
        if flag in sys.argv:
            uml_codegen_flag = lang
            break

    if uml_codegen_flag:
        parser = build_parser()
        args = parser.parse_args()
        target = args.target
        app = readmenatorApplication()
        code = app.generate_uml_code(target, uml_codegen_flag)
        print(code)
        return

    if len(sys.argv) > 2 and sys.argv[1] != "--rebuild" and not sys.argv[1].startswith("-"):
        target = sys.argv[1]
        command = sys.argv[2] if len(sys.argv) > 2 else ""
        app = readmenatorApplication()

        if command == "query" and len(sys.argv) >= 4:
            result = app.query(target, sys.argv[3])
            print(result)
            return
        elif command == "explain" and len(sys.argv) >= 4:
            result = app.explain(target, sys.argv[3])
            print(result)
            return
        elif command == "path" and len(sys.argv) >= 5:
            result = app.find_path(target, sys.argv[3], sys.argv[4])
            print(result)
            return
        elif command in ("summary", "sum", "info"):
            result = app.summary(target)
            print(result)
            return
        elif command == "update":
            app.update(target)
            return
        elif command == "export":
            app.export(target)
            return
        elif command == "graphml":
            app.export_graphml(target)
            return
        elif command == "cypher":
            app.export_cypher(target)
            return
        elif command == "obsidian":
            app.export_obsidian(target)
            return
        elif command == "watch":
            app.watch(target)
            return
        elif command == "layers":
            app.detect_layers(target)
            return
        elif command == "analyze":
            result = app.analyze(target)
            logger.info("Communities: %d", len(result.communities))
            logger.info("God nodes: %d", len(result.god_nodes))
            logger.info("Surprising connections: %d", len(result.surprising_connections))
            for q in result.suggested_questions:
                logger.info("  - %s", q)
            return
        elif command == "audit":
            app.audit(target)
            return
        elif command == "audit-deep":
            result = app.audit_deep(target)
            logger.info("Taint paths: %d", len(result.taint.paths) if result.taint else 0)
            logger.info("Hotspots: %d", len(result.hotspots))
            logger.info("Cycles: %d", len(result.cycles))
            logger.info("Layer violations: %d", len(result.layer_violations))
            logger.info("Suggested rules: %d", len(result.suggested_rules))
            return
        elif command == "export-sarif":
            app.export_sarif(target)
            return
        elif command == "export-rules":
            app.export_rules(target)
            return
        elif command == "uml":
            nodes, edges = app._scan(target)
            uml_diagram = app._factory.uml.render_mermaid_class_diagram(nodes, edges)
            if uml_diagram:
                print(uml_diagram)
            else:
                logger.info("No class-level symbols found for UML diagram.")
            return
        elif command == "serve":
            mcp_main()
            return
        elif command == "lint":
            violations = app.lint(target)
            sys.exit(1 if any(v.severity == "error" for v in violations) else 0)
            return
        elif command == "strip-dead-code":
            reports = app.strip_dead_code(target)
            for r in reports:
                print(f"{r.file_path}:{r.symbol_name} ({r.symbol_type}) -> {r.recommendation}")
            return
        elif command == "generate-rules":
            content = app.generate_cursorrules(target)
            print(content)
            return
        elif command == "refactor-monolith":
            plans = app.refactor_monolith(target)
            for plan in plans:
                print(f"\n{plan.file_path} ({plan.current_lines} lines, {plan.estimated_impact} dependents):")
                for action in plan.actions:
                    print(f"  [{action.action_type}] {action.description}")
            return
        elif command == "--rebuild":
            app.rebuild(target)
            return
        elif command.startswith("--"):
            pass
        else:
            logger.error("Unknown command: %s", command)
            sys.exit(1)

    if has_export_flags:
        parser = build_parser()
        args = parser.parse_args()
        target = args.target
        app = readmenatorApplication()

        if args.export_all or (args.json and args.html and args.svg):
            app.export(target)
        else:
            if args.json:
                app.export_json(target)
            if args.html:
                app.export_html(target)
            if args.svg:
                app.export_svg(target)
            if args.graphml:
                app.export_graphml(target)
            if args.cypher:
                app.export_cypher(target)
        return

    parser = build_parser()
    args = parser.parse_args()
    target = args.target

    app = readmenatorApplication()
    if args.privacy:
        from readmenator._config import Config
        app = readmenatorApplication(Config(
            PRIVACY_MODE=True, SARIF_ENABLED=args.sarif,
            SECURITY_ENABLED=args.audit,
            AGENT_INJECTION_ENABLED=not args.no_agent_injection,
            AGENT_OUTPUT_ENABLED=not args.no_agent_output,
        ))
    elif args.sarif:
        from readmenator._config import Config
        app = readmenatorApplication(Config(
            SARIF_ENABLED=True, SECURITY_ENABLED=args.audit,
            AGENT_INJECTION_ENABLED=not args.no_agent_injection,
            AGENT_OUTPUT_ENABLED=not args.no_agent_output,
        ))
    elif args.no_agent_injection or args.no_agent_output:
        from readmenator._config import Config
        app = readmenatorApplication(Config(
            AGENT_INJECTION_ENABLED=not args.no_agent_injection,
            AGENT_OUTPUT_ENABLED=not args.no_agent_output,
        ))

    output_path = Path(target) / "KNOWLEDGE_BASE.md"

    if args.rebuild or not output_path.exists():
        app.run(target, run_analysis=not args.no_analysis, run_security=args.audit)
    else:
        if args.context_budget > 0:
            from readmenator._config import Config as Cfg
            app = readmenatorApplication(Cfg(CONTEXT_BUDGET=args.context_budget))
            app.run(target, run_analysis=not args.no_analysis, run_security=args.audit)
        else:
            result = app.summary(target)
            print(result)


if __name__ == "__main__":
    main()
