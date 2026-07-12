"""Application orchestrator for the readmenator pipeline.

Wires together scanner, documentation generator, query engine,
import resolver, graph analyzer, file cache, and graph exporter
into a single facade consumed by the CLI entry point (__main__) and
the public API (__init__).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from readmenator._analyzer import GraphAnalyzer
from readmenator._cache import FileCache
from readmenator._config import Config
from readmenator._documentation import DocumentationGenerator
from readmenator._exporter import GraphExporter
from readmenator._models import AnalysisResult, Edge, Node
from readmenator._query import QueryEngine
from readmenator._resolver import ImportResolver
from readmenator._scanner import PolyglotScanner


class readmenatorApplication:
    """High-level facade for readmenator operations.

    Provides convenience methods for the full pipeline:
      - ``run`` / ``rebuild``: scan + generate KNOWLEDGE_BASE.md
      - ``update``: incremental scan using content hash cache
      - ``query``, ``explain``, ``find_path``, ``summary``:
        scan + query in a single call
      - ``analyze``: run community detection and graph analysis
      - ``export_json``, ``export_html``, ``export_svg``:
        export the graph to various formats
    """

    def __init__(self, config: Optional[Config] = None):
        """Initialise the application with an optional custom config.

        Args:
            config: Application settings; defaults to Config() if omitted.
        """
        self._config = config or Config()
        self._scanner = PolyglotScanner(self._config)
        self._generator = DocumentationGenerator(self._config)
        self._analyzer = GraphAnalyzer(self._config)
        self._exporter = GraphExporter(self._config)
        self._last_nodes: List[Node] = []
        self._last_edges: List[Edge] = []
        self._last_resolved_edges: List[Edge] = []

    def _scan(self, target_dir: str) -> Tuple[List[Node], List[Edge]]:
        """Resolve *target_dir* and run the scanner, caching results."""
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        self._last_nodes = nodes
        self._last_edges = edges
        self._last_resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        return nodes, edges

    def _resolve_imports(
        self, nodes: List[Node], edges: List[Edge], target_dir: str
    ) -> List[Edge]:
        """Resolve raw import strings to project file paths.

        Args:
            nodes: Scanned file nodes.
            edges: Raw import edges.
            target_dir: Project root directory.

        Returns:
            List of resolved import edges with project file targets.
        """
        file_ids = [n.node_id for n in nodes]
        resolver = ImportResolver(file_ids, target_dir)
        resolved: List[Edge] = []
        for edge in edges:
            target = resolver.resolve(edge.target, edge.source)
            if target is not None and target != edge.source:
                resolved.append(
                    Edge(
                        source=edge.source,
                        target=target,
                        relation="resolved_imports",
                        confidence="EXTRACTED",
                    )
                )
        return resolved

    def run(
        self,
        target_dir: str,
        resolve_imports: bool = True,
        run_analysis: bool = True,
    ) -> None:
        """Scan *target_dir* and write KNOWLEDGE_BASE.md to disk.

        Args:
            target_dir: Project directory to scan.
            resolve_imports: Whether to resolve raw imports to project files.
            run_analysis: Whether to run community detection and graph analysis.
        """
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        self._last_nodes = nodes
        self._last_edges = edges

        resolved_edges: Optional[List[Edge]] = None
        if resolve_imports:
            resolved_edges = self._resolve_imports(nodes, edges, target_dir)
            self._last_resolved_edges = resolved_edges

        analysis: Optional[AnalysisResult] = None
        if run_analysis:
            analysis = self._analyzer.analyze(nodes, edges, resolved_edges)

        content = self._generator.generate(nodes, edges, resolved_edges, analysis)
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")
        total_symbols = sum(len(n.symbols) for n in nodes)
        print(f"[+] Knowledge base generated: {output_path}")
        print(
            f"[+] Files: {len(nodes)} | "
            f"Symbols: {total_symbols} | "
            f"Imports: {len(edges)}"
        )
        if resolved_edges:
            print(f"[+] Resolved imports: {len(resolved_edges)}")
        if analysis and analysis.communities:
            print(f"[+] Communities detected: {len(analysis.communities)}")

    def update(self, target_dir: str) -> None:
        """Incrementally update KNOWLEDGE_BASE.md for changed files only.

        Uses SHA256 content hashing to detect which files have changed
        since the last run. Falls back to full rebuild if no cache exists.

        Args:
            target_dir: Project directory to scan.
        """
        root = Path(target_dir).resolve()
        cache = FileCache(self._config, str(root))
        nodes, edges = self._scan_for_cache(root, cache)
        self._last_nodes = nodes
        self._last_edges = edges
        resolved_edges = self._resolve_imports(nodes, edges, target_dir)
        self._last_resolved_edges = resolved_edges
        analysis = self._analyzer.analyze(nodes, edges, resolved_edges)
        content = self._generator.generate(nodes, edges, resolved_edges, analysis)
        output_path = root / self._config.OUTPUT_FILENAME
        output_path.write_text(content, encoding="utf-8")
        total_symbols = sum(len(n.symbols) for n in nodes)
        print(f"[+] Knowledge base updated: {output_path}")
        print(
            f"[+] Files: {len(nodes)} | "
            f"Symbols: {total_symbols} | "
            f"Imports: {len(edges)}"
        )

    def _scan_for_cache(
        self, root: Path, cache: FileCache
    ) -> Tuple[List[Node], List[Edge]]:
        """Scan only files that have changed since the last cache write.

        If no cache exists, performs a full scan and populates the cache.
        """
        cached_hashes = cache.load()
        if not cached_hashes:
            return self._scanner.scan(root)

        nodes, edges = self._scanner.scan(root)
        current_ids = {n.node_id for n in nodes}
        cache.prune_deleted(current_ids)

        file_paths: Dict[str, Path] = {
            n.node_id: root / n.node_id for n in nodes
        }
        new_hashes = cache.compute_hashes(file_paths)
        if new_hashes:
            cache.save(new_hashes)

        return nodes, edges

    def query(self, target_dir: str, question: str) -> str:
        """Scan *target_dir* and answer *question* using the query engine."""
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        return engine.query(question)

    def explain(self, target_dir: str, symbol_name: str) -> str:
        """Scan *target_dir* and return a detailed explanation of *symbol_name*."""
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        result = engine.explain(symbol_name)
        if result is None:
            return (
                f"Symbol '{symbol_name}' not found in the knowledge base. "
                f"Scanned {len(nodes)} files with "
                f"{sum(len(n.symbols) for n in nodes)} total symbols."
            )
        return result

    def find_path(self, target_dir: str, symbol_a: str, symbol_b: str) -> str:
        """Scan *target_dir* and find the shortest import path between two symbols.

        Uses resolved imports when available for project-internal paths.
        """
        nodes, edges = self._scan(target_dir)
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
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
        engine = QueryEngine(nodes, edges, self._last_resolved_edges)
        return engine.summary()

    def rebuild(self, target_dir: str) -> None:
        """Alias for ``run`` -- forces regeneration of KNOWLEDGE_BASE.md."""
        self.run(target_dir)

    def analyze(self, target_dir: str) -> AnalysisResult:
        """Run community detection and graph analysis on *target_dir*.

        Returns:
            Structured AnalysisResult with god nodes, communities, etc.
        """
        nodes, edges = self._scan(target_dir)
        return self._analyzer.analyze(nodes, edges, self._last_resolved_edges)

    def export_json(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        """Export the knowledge graph as JSON.

        Args:
            target_dir: Project directory to scan.
            output_path: Optional file path for the JSON output.
                Defaults to ``<target_dir>/graph.json``.

        Returns:
            JSON string content.
        """
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_json(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.json")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] Graph JSON exported: {output_path}")
        return data

    def export_html(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        """Export the knowledge graph as an interactive HTML page.

        Args:
            target_dir: Project directory to scan.
            output_path: Optional file path for the HTML output.
                Defaults to ``<target_dir>/graph.html``.

        Returns:
            HTML document string.
        """
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_html(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.html")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] Graph HTML exported: {output_path}")
        return data

    def export_svg(
        self,
        target_dir: str,
        output_path: Optional[str] = None,
    ) -> str:
        """Export the knowledge graph as a static SVG image.

        Args:
            target_dir: Project directory to scan.
            output_path: Optional file path for the SVG output.
                Defaults to ``<target_dir>/graph.svg``.

        Returns:
            SVG document string.
        """
        nodes, edges = self._scan(target_dir)
        analysis = self._analyzer.analyze(nodes, edges, self._last_resolved_edges)
        data = self._exporter.to_svg(nodes, edges, self._last_resolved_edges, analysis)
        if output_path is None:
            root = Path(target_dir).resolve()
            output_path = str(root / "graph.svg")
        Path(output_path).write_text(data, encoding="utf-8")
        print(f"[+] Graph SVG exported: {output_path}")
        return data

    def export(self, target_dir: str) -> None:
        """Export all formats (JSON, HTML, SVG) at once."""
        self.export_json(target_dir)
        self.export_html(target_dir)
        self.export_svg(target_dir)
