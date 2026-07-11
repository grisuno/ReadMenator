from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple

from readmenator._config import Config
from readmenator._documentation import DocumentationGenerator
from readmenator._models import Edge, Node
from readmenator._query import QueryEngine
from readmenator._scanner import PolyglotScanner


class readmenatorApplication:
    def __init__(self, config: Optional[Config] = None) -> None:
        self._config = config or Config()
        self._scanner = PolyglotScanner(self._config)
        self._generator = DocumentationGenerator(self._config)
        self._last_nodes: List[Node] = []
        self._last_edges: List[Edge] = []

    def _scan(self, target_dir: str) -> Tuple[List[Node], List[Edge]]:
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        self._last_nodes = nodes
        self._last_edges = edges
        return nodes, edges

    def run(self, target_dir: str) -> None:
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
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges)
        return engine.query(question)

    def explain(self, target_dir: str, symbol_name: str) -> str:
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
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges)
        return engine.summary()

    def rebuild(self, target_dir: str) -> None:
        self.run(target_dir)
