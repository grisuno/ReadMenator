"""CLI entry point for readmenator.

Parses command-line arguments, dispatches to the appropriate subcommand
(query, explain, path, summary, update, export, analyze, --rebuild,
--test, --json, --html, --svg, --export-all), and manages the
target directory analysis lifecycle.
"""

from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path

from readmenator._app import readmenatorApplication


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser with subcommand help and examples."""
    parser = argparse.ArgumentParser(
        description="ReadMenator: Zero-token polyglot codebase knowledge graph generator.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Subcommands:\n"
            "  query \"<question>\"     Answer a question using the knowledge base\n"
            "  explain \"<symbol>\"     Explain a symbol with relationships\n"
            "  path \"<A>\" \"<B>\"       Trace dependency chain between two symbols\n"
            "  summary | sum | info   Print a concise codebase overview\n"
            "  analyze                 Run community detection and analysis\n"
            "  update                  Incremental rebuild (cache-based)\n"
            "  export                  Export graph (JSON + HTML + SVG)\n"
            "\n"
            "Flags:\n"
            "  --rebuild               Force full regeneration\n"
            "  --json                  Export graph.json\n"
            "  --html                  Export graph.html (interactive)\n"
            "  --svg                   Export graph.svg (static)\n"
            "  --export-all            Export all formats (JSON + HTML + SVG)\n"
            "  --test                  Run the test suite\n"
            "\n"
            "Examples:\n"
            "  python -m readmenator /path/to/project\n"
            "  python -m readmenator /path/to/project explain ClassName\n"
            "  python -m readmenator . query \"What classes handle HTTP?\"\n"
            "  python -m readmenator . --export-all\n"
            "  python -m readmenator /path/to/project --json\n"
        ),
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory to analyze (default: current directory)",
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Force regeneration of KNOWLEDGE_BASE.md",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the built-in test suite",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Export graph.json",
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Export graph.html (interactive visualization)",
    )
    parser.add_argument(
        "--svg",
        action="store_true",
        help="Export graph.svg (static visualization)",
    )
    parser.add_argument(
        "--export-all",
        action="store_true",
        help="Export all formats (JSON + HTML + SVG)",
    )
    parser.add_argument(
        "--graphml",
        action="store_true",
        help="Export graph.graphml (Gephi/yEd)",
    )
    parser.add_argument(
        "--no-analysis",
        action="store_true",
        help="Skip community detection and graph analysis",
    )
    return parser


def _run_tests() -> None:
    """Discover and run the full test suite from the tests/ directory."""
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
        print("No tests directory found.", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Primary CLI entry point invoked by ``python -m readmenator``.

    Supports direct subcommand dispatch (query, explain, path, summary,
    update, export, analyze, --rebuild) or falls back to the argument
    parser for the default workflow: generate or summarise
    KNOWLEDGE_BASE.md.
    """
    if "--test" in sys.argv:
        _run_tests()
        return

    has_export_flags = any(
        f in sys.argv for f in {"--json", "--html", "--svg", "--export-all", "--graphml"}
    )

    positional_args = [
        a for a in sys.argv[1:] if not a.startswith("-") and a not in {
            "query", "explain", "path", "summary", "sum", "info",
            "update", "export", "analyze",
        }
    ]

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
            print(f"Communities: {len(result.communities)}")
            print(f"God nodes: {len(result.god_nodes)}")
            print(f"Surprising connections: {len(result.surprising_connections)}")
            print("Suggested questions:")
            for q in result.suggested_questions:
                print(f"  - {q}")
            return
        elif command == "--rebuild":
            app.rebuild(target)
            return
        elif command.startswith("--"):
            pass
        else:
            print(f"Unknown command: {command}", file=sys.stderr)
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
        return

    parser = build_parser()
    args = parser.parse_args()
    target = args.target

    app = readmenatorApplication()
    output_path = Path(target) / "KNOWLEDGE_BASE.md"

    if args.rebuild or not output_path.exists():
        app.run(target, run_analysis=not args.no_analysis)
    else:
        result = app.summary(target)
        print(result)

    print("\nRun with --rebuild to regenerate or use query/explain/path subcommands.")
    print("Use --json, --html, --svg, or --export-all for graph exports.")


if __name__ == "__main__":
    main()
