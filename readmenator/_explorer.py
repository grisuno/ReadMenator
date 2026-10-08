"""Stdlib explorer HTTP server for the readmenator knowledge graph.

A zero-dependency http.server process serving the force-graph UI plus
JSON APIs for graph, analytics, samples, and rules. Used by
`readmenator <dir> explorer` for local interactive exploration.
"""

from __future__ import annotations

import json
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from readmenator._analytics import AnalyticsBuilder
from readmenator._config import Config
from readmenator._forcegraph import ForceGraphRenderer
from readmenator._models import AnalysisResult, Edge, Node, SecurityFinding


class ExplorerState:
    """Holds the precomputed payloads served by the explorer."""

    def __init__(
        self,
        config: Config,
        nodes: List[Node],
        edges: List[Edge],
        resolved_edges: Optional[List[Edge]] = None,
        analysis: Optional[AnalysisResult] = None,
        findings: Optional[List[SecurityFinding]] = None,
        layers: Optional[Dict[str, str]] = None,
    ) -> None:
        """Initialise explorer state and precompute payloads.

        Args:
            config: Application configuration.
            nodes: Scanned file nodes.
            edges: Import edges.
            resolved_edges: Optional resolved-import edges.
            analysis: Optional community analysis.
            findings: Optional security findings.
            layers: Optional file-to-layer mapping.
        """
        self._config = config
        self._nodes = nodes
        self._edges = edges
        self._resolved = resolved_edges or []
        self._analysis = analysis
        self._findings = findings or []
        self._layers = layers or {}
        renderer = ForceGraphRenderer(config)
        self.graph = renderer.build_payload(nodes, edges, resolved_edges, analysis, layers, findings)
        self.analytics = AnalyticsBuilder(config).build(
            nodes, edges, resolved_edges, analysis, findings, layers
        )
        self.html = renderer.render(self.graph, self.analytics, home_href=None)

    def samples(self) -> List[Dict[str, Any]]:
        """Return a compact per-file sample listing."""
        rows = []
        for node in self._nodes:
            rows.append(
                {
                    "file": node.node_id,
                    "label": node.label,
                    "language": node.language,
                    "symbols": len(node.symbols),
                    "layer": self._layers.get(node.node_id),
                }
            )
        rows.sort(key=lambda item: (-item["symbols"], item["file"]))
        return rows


_STATE: ExplorerState | None = None


class _Handler(BaseHTTPRequestHandler):
    """HTTP handler serving explorer HTML and JSON APIs."""

    def log_message(self, fmt: str, *args: Any) -> None:
        """Silence the default access log."""
        return

    def do_GET(self) -> None:
        """Dispatch GET routes for HTML and JSON APIs."""
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"
        if path == "/":
            self._serve_html()
        elif path == "/vendor/force-graph.min.js":
            self._serve_vendor()
        elif path == "/api/graph":
            self._serve_json(_STATE.graph if _STATE else {})
        elif path == "/api/analytics":
            self._serve_json(_STATE.analytics if _STATE else {})
        elif path == "/api/samples":
            self._serve_json(_STATE.samples() if _STATE else [])
        else:
            self.send_error(404)

    def _serve_html(self) -> None:
        """Serve the precomputed explorer HTML document."""
        body = (_STATE.html if _STATE else "<p>empty</p>").encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_vendor(self) -> None:
        """Serve the vendored 2D graph engine beside the page."""
        source = ForceGraphRenderer(_STATE._config).vendor_source() if _STATE else None
        if source is None or not source.is_file():
            self.send_error(404)
            return
        body = source.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "application/javascript")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=86400")
        self.end_headers()
        self.wfile.write(body)

    def _serve_json(self, payload: Any) -> None:
        """Serve a JSON payload with permissive CORS headers."""
        body = json.dumps(payload, default=str).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


def find_free_port(preferred: int) -> int:
    """Find a free TCP port, preferring the configured value.

    Args:
        preferred: Preferred port number to bind.

    Returns:
        Preferred port when free, otherwise an OS-assigned port.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", preferred))
            return preferred
    except OSError:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 0))
            return int(sock.getsockname()[1])


def serve(
    state: ExplorerState,
    host: str = "127.0.0.1",
    port: int = 8421,
    open_browser: bool = False,
) -> str:
    """Serve the explorer state until interrupted.

    Args:
        state: Precomputed explorer payloads.
        host: Bind address for the HTTP server.
        port: Preferred port number.
        open_browser: Open the URL in a browser when True.

    Returns:
        Base URL of the running server.
    """
    global _STATE
    _STATE = state
    resolved_port = find_free_port(port)
    server = HTTPServer((host, resolved_port), _Handler)
    url = f"http://{host}:{resolved_port}"
    if open_browser:
        import webbrowser

        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return url


def build_state(
    config: Config,
    nodes: List[Node],
    edges: List[Edge],
    resolved_edges: Optional[List[Edge]] = None,
    analysis: Optional[AnalysisResult] = None,
    findings: Optional[List[SecurityFinding]] = None,
    layers: Optional[Dict[str, str]] = None,
) -> ExplorerState:
    """Build explorer state without starting the server.

    Args:
        config: Application configuration.
        nodes: Scanned file nodes.
        edges: Import edges.
        resolved_edges: Optional resolved-import edges.
        analysis: Optional community analysis.
        findings: Optional security findings.
        layers: Optional file-to-layer mapping.

    Returns:
        Precomputed explorer state.
    """
    return ExplorerState(config, nodes, edges, resolved_edges, analysis, findings, layers)


def write_static(
    state: ExplorerState, output_dir: str | Path, filename: str = "explorer.html"
) -> Path:
    """Write the explorer HTML to a static file.

    Args:
        state: Precomputed explorer payloads.
        output_dir: Directory receiving the HTML file.
        filename: Output HTML filename.

    Returns:
        Path of the written HTML file.
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / filename
    target.write_text(state.html, encoding="utf-8")
    ForceGraphRenderer(state._config).copy_vendor(out_dir)
    (out_dir / "explorer-graph.json").write_text(
        json.dumps(state.graph, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (out_dir / "explorer-analytics.json").write_text(
        json.dumps(state.analytics, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    return target
