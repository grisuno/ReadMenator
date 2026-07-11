"""Application orchestrator for the readmenator pipeline.

Wires together scanner, documentation generator, and query engine
into a single facade consumed by the CLI entry point (__main__) and
the public API (__init__).
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple

from readmenator._config import Config
from readmenator._documentation import DocumentationGenerator
from readmenator._models import Edge, Node
from readmenator._query import QueryEngine
from readmenator._scanner import PolyglotScanner


class readmenatorApplication:
    """High-level facade for readmenator operations.

    Provides convenience methods for the full pipeline:
      - ``run`` / ``rebuild``: scan + generate KNOWLEDGE_BASE.md
      - ``query``, ``explain``, ``find_path``, ``summary``:
        scan + query in a single call.
    """

    def __init__(self, config: Optional[Config] = None) -> None:
        """Initialise the application with an optional custom config.

        Args:
            config: Application settings; defaults to Config() if omitted.
        """
        self._config = config or Config()
        self._scanner = PolyglotScanner(self._config)
        self._generator = DocumentationGenerator(self._config)
        self._last_nodes: List[Node] = []
        self._last_edges: List[Edge] = []

    def _scan(self, target_dir: str) -> Tuple[List[Node], List[Edge]]:
        """Resolve *target_dir* and run the scanner, caching results."""
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        self._last_nodes = nodes
        self._last_edges = edges
        return nodes, edges

    def run(self, target_dir: str) -> None:
        """Scan *target_dir* and write KNOWLEDGE_BASE.md to disk.

        Prints a summary of files, symbols, and imports on completion.
        """
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        content = self._generator.generate(nodes, edges)
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")
        total_symbols = sum(len(n.symbols) for n in nodes)
        print(f"[+] Knowledge base generated: {output_path}")
        print(
            f"[+] Files: {len(nodes)} | "
            f"Symbols: {total_symbols} | "
            f"Imports: {len(edges)}"
        )

    def query(self, target_dir: str, question: str) -> str:
        """Scan *target_dir* and answer *question* using the query engine."""
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges)
        return engine.query(question)

    def explain(self, target_dir: str, symbol_name: str) -> str:
        """Scan *target_dir* and return a detailed explanation of *symbol_name*."""
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges)
        result = engine.explain(symbol_name)
        if result is None:
            return (
                f"Symbol '{symbol_name}' not found in the knowledge base. "
                f"Scanned {len(nodes)} files with "
                f"{sum(len(n.symbols) for n in nodes)} total symbols."
            )
        return result

    def find_path(self, target_dir: str, symbol_a: str, symbol_b: str) -> str:
        """Scan *target_dir* and find the shortest import path between two symbols."""
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges)
        result = engine.find_path(symbol_a, symbol_b)
        if result is None:
            return (
                f"Could not find a dependency path between '{symbol_a}' "
                f"and '{symbol_b}'. They may be in disconnected components "
                f"or one of the symbols does not exist."
            )
        path_str = " --imports--> ".join(result)
        return f"Dependency path: {path_str}"

    def summary(self, target_dir: str) -> str:
        """Scan *target_dir* and return a concise knowledge base overview."""
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges)
        return engine.summary()

    def rebuild(self, target_dir: str) -> None:
        """Alias for ``run`` -- forces regeneration of KNOWLEDGE_BASE.md."""
        self.run(target_dir)
