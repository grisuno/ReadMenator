from __future__ import annotations

import argparse
import os
import sys
import unittest
from pathlib import Path

from readmenator._app import readmenatorApplication


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="ReadMenator: Zero-token polyglot codebase knowledge graph generator.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Subcommands:\n"
            "  query \"<question>\"   Answer a question using the knowledge base\n"
            "  explain \"<symbol>\"   Explain a symbol with relationships\n"
            "  path \"<A>\" \"<B>\"     Trace dependency chain between two symbols\n"
            "\n"
            "Examples:\n"
            "  python -m readmenator /path/to/project\n"
            "  python -m readmenator /path/to/project explain ClassName\n"
            "  python -m readmenator . query \"What classes handle HTTP?\"\n"
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
        print("No tests directory found.", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        _run_tests()
        return

    if len(sys.argv) > 2 and sys.argv[1] != "--rebuild" and not sys.argv[1].startswith("-"):
        target = sys.argv[1]
        command = sys.argv[2]
        app = readmenatorApplication()

        if command == "query" and len(sys.argv) >= 4:
            result = app.query(target, sys.argv[3])
            print(result)
        elif command == "explain" and len(sys.argv) >= 4:
            result = app.explain(target, sys.argv[3])
            print(result)
        elif command == "path" and len(sys.argv) >= 5:
            result = app.find_path(target, sys.argv[3], sys.argv[4])
            print(result)
        elif command in ("summary", "sum", "info"):
            result = app.summary(target)
            print(result)
        elif command == "--rebuild":
            app.rebuild(target)
        elif command == "update":
            app.rebuild(target)
        else:
            print(f"Unknown command: {command}", file=sys.stderr)
            sys.exit(1)
        return

    parser = build_parser()
    args = parser.parse_args()
    target = args.target

    app = readmenatorApplication()
    output_path = Path(target) / "KNOWLEDGE_BASE.md"

    if args.rebuild or not output_path.exists():
        app.run(target)
    else:
        result = app.summary(target)
        print(result)

    print("\nRun with --rebuild to regenerate or use query/explain/path subcommands.")


if __name__ == "__main__":
    main()
