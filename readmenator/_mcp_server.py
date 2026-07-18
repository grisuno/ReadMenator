"""MCP (Model Context Protocol) stdio server for ReadMenator.

Exposes the full codebase knowledge graph as MCP tools and resources,
allowing AI agents to query structural information without parsing
KNOWLEDGE_BASE.md as text. Each query costs ~50-200 tokens vs
2000-8000+ tokens of reading the full KB file.

Tools:
  readmenator.summary       — codebase overview (files, symbols, langs)
  readmenator.query         — free-text symbol/file search
  readmenator.explain       — detailed symbol explanation
  readmenator.path          — dependency chain between two symbols
  readmenator.findings      — security findings
  readmenator.taint         — taint propagation analysis
  readmenator.hotspots      — hotspot analysis
  readmenator.cycles        — dependency cycles
  readmenator.communities   — community detection
  readmenator.layers        — architectural layers
  readmenator.layer_violations — layer rule violations
  readmenator.rebuild       — regenerate KNOWLEDGE_BASE.md
  readmenator.update        — incremental update (SHA256 cache)
  readmenator.export_json   — export graph.json
  readmenator.security_summary — security audit summary

Resources:
  readmenator://summary     — structured JSON summary
  readmenator://graph       — graph data (nodes + edges)
  readmenator://file/{path} — file details
  readmenator://symbol/{name} — symbol details
  readmenator://findings    — security findings
  readmenator://analysis    — full analysis result
  readmenator://kb          — full KNOWLEDGE_BASE.md text
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from readmenator._app import readmenatorApplication
from readmenator._config import Config
from readmenator._layers import LayerDetector
from readmenator._models import (
    AnalysisResultV2,
    SecurityFinding,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Minimal MCP stdio server (JSON-RPC 2.0)
# ---------------------------------------------------------------------------

class MCPError(Exception):
    def __init__(self, code: int, message: str, data: Any = None):
        self.code = code
        self.message = message
        self.data = data


TOOL_CALL_ERROR = -32000
INVALID_PARAMS = -32602
METHOD_NOT_FOUND = -32601
INTERNAL_ERROR = -32603


class MCPRequest:
    def __init__(self, msg: Dict[str, Any]):
        self.jsonrpc = msg.get("jsonrpc", "2.0")
        self.id: Any = msg.get("id")
        self.method: str = msg.get("method", "")
        self.params: Any = msg.get("params", {})

    @property
    def is_notification(self) -> bool:
        return self.id is None

    def response(self, result: Any = None) -> Dict[str, Any]:
        return {"jsonrpc": "2.0", "id": self.id, "result": result}

    def error(self, code: int, message: str, data: Any = None) -> Dict[str, Any]:
        err: Dict[str, Any] = {"jsonrpc": "2.0", "id": self.id, "error": {"code": code, "message": message}}
        if data is not None:
            err["error"]["data"] = data
        return err


class MCPTool:
    def __init__(
        self,
        name: str,
        description: str,
        handler: Callable,
        input_schema: Optional[Dict[str, Any]] = None,
    ):
        self.name = name
        self.description = description
        self.handler = handler
        self.input_schema = input_schema or {
            "type": "object",
            "properties": {},
        }

    def definition(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.input_schema,
        }

    def call(self, arguments: Dict[str, Any]) -> Any:
        return self.handler(**arguments)


class MCPResource:
    def __init__(
        self,
        uri: str,
        name: str,
        description: str,
        mime_type: str,
        handler: Callable,
    ):
        self.uri = uri
        self.name = name
        self.description = description
        self.mime_type = mime_type
        self.handler = handler

    def definition(self) -> Dict[str, Any]:
        return {
            "uri": self.uri,
            "name": self.name,
            "description": self.description,
            "mimeType": self.mime_type,
        }

    def read(self) -> Any:
        return self.handler()


class MCPServer:
    def __init__(self, app: readmenatorApplication, target_dir: str):
        self._app = app
        self._target_dir = target_dir
        self._tools: Dict[str, MCPTool] = {}
        self._resources: Dict[str, MCPResource] = {}
        self._initialized = False
        self._kb_cache: Optional[str] = None

    def register_tool(self, tool: MCPTool) -> None:
        self._tools[tool.name] = tool

    def register_resource(self, resource: MCPResource) -> None:
        self._resources[resource.uri] = resource

    def _ensure_kb(self) -> str:
        root = Path(self._target_dir).resolve()
        kb_path = root / "KNOWLEDGE_BASE.md"
        if not kb_path.exists():
            self._app.run(self._target_dir)
        if self._kb_cache is None:
            try:
                self._kb_cache = kb_path.read_text(encoding="utf-8")
            except OSError:
                self._kb_cache = ""
        return self._kb_cache

    def _handle_initialize(self, req: MCPRequest) -> Dict[str, Any]:
        self._initialized = True
        return req.response({
            "protocolVersion": "2024-11-05",
            "serverInfo": {
                "name": "readmenator",
                "version": "1.0.1",
            },
            "capabilities": {
                "tools": {},
                "resources": {},
            },
        })

    def _handle_list_tools(self, req: MCPRequest) -> Dict[str, Any]:
        return req.response({
            "tools": [t.definition() for t in self._tools.values()],
        })

    def _handle_call_tool(self, req: MCPRequest) -> Dict[str, Any]:
        name = req.params.get("name", "")
        arguments = req.params.get("arguments", {})
        tool = self._tools.get(name)
        if not tool:
            return req.error(METHOD_NOT_FOUND, f"Tool not found: {name}")
        try:
            result = tool.call(arguments)
            if not isinstance(result, str):
                result = json.dumps(result, indent=2, default=str)
            return req.response({
                "content": [{"type": "text", "text": result}],
                "isError": False,
            })
        except TypeError as e:
            return req.error(INVALID_PARAMS, f"Invalid arguments: {e}")
        except MCPError as e:
            return req.error(e.code, e.message, e.data)
        except Exception as e:
            logger.exception("Tool call failed: %s", name)
            return req.error(INTERNAL_ERROR, str(e))

    def _handle_list_resources(self, req: MCPRequest) -> Dict[str, Any]:
        return req.response({
            "resources": [r.definition() for r in self._resources.values()],
        })

    def _handle_read_resource(self, req: MCPRequest) -> Dict[str, Any]:
        uri = req.params.get("uri", "")
        resource = self._resources.get(uri)
        if not resource:
            return req.error(METHOD_NOT_FOUND, f"Resource not found: {uri}")
        try:
            content = resource.read()
            if isinstance(content, str):
                text = content
            else:
                text = json.dumps(content, indent=2, default=str)
            return req.response({
                "contents": [{
                    "uri": uri,
                    "mimeType": resource.mime_type,
                    "text": text,
                }],
            })
        except Exception as e:
            logger.exception("Resource read failed: %s", uri)
            return req.error(INTERNAL_ERROR, str(e))

    def dispatch(self, req: MCPRequest) -> Optional[Dict[str, Any]]:
        method = req.method
        if method == "initialize":
            return self._handle_initialize(req)
        if method == "notifications/initialized":
            return None
        if not self._initialized and method not in ("initialize",):
            return req.error(-32000, "Server not initialized")

        handlers = {
            "tools/list": self._handle_list_tools,
            "tools/call": self._handle_call_tool,
            "resources/list": self._handle_list_resources,
            "resources/read": self._handle_read_resource,
        }
        handler = handlers.get(method)
        if handler:
            return handler(req)
        return req.error(METHOD_NOT_FOUND, f"Method not found: {method}")

    def run(self) -> None:
        self._register_all()
        logger.info("ReadMenator MCP server started for: %s", self._target_dir)
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
                req = MCPRequest(msg)
                response = self.dispatch(req)
                if response is not None:
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
            except json.JSONDecodeError:
                err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
                sys.stdout.write(json.dumps(err) + "\n")
                sys.stdout.flush()
            except Exception:
                logger.exception("Unhandled error in MCP dispatch")
                err = {"jsonrpc": "2.0", "id": None, "error": {"code": INTERNAL_ERROR, "message": "Internal error"}}
                sys.stdout.write(json.dumps(err) + "\n")
                sys.stdout.flush()

    def _register_all(self) -> None:
        self.register_tool(MCPTool(
            "readmenator.summary",
            "Get a concise codebase overview: file count, symbol count, "
            "import count, languages, top modules, key classes/functions, "
            "god nodes, communities, and hotspot count.",
            self._tool_summary,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.query",
            "Free-text search over symbol names and file paths. "
            "Returns matching symbols with their file, line, kind, and docstring.",
            self._tool_query,
            {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Search terms"},
                },
                "required": ["text"],
            },
        ))
        self.register_tool(MCPTool(
            "readmenator.explain",
            "Detailed explanation of a symbol: its type, file, line, "
            "docstring, signature, what it imports, what imports it, "
            "and sibling symbols in the same file.",
            self._tool_explain,
            {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Symbol name"},
                },
                "required": ["name"],
            },
        ))
        self.register_tool(MCPTool(
            "readmenator.path",
            "Find the shortest dependency path between two symbols "
            "through the resolved import graph.",
            self._tool_path,
            {
                "type": "object",
                "properties": {
                    "symbol_a": {"type": "string", "description": "Start symbol"},
                    "symbol_b": {"type": "string", "description": "End symbol"},
                },
                "required": ["symbol_a", "symbol_b"],
            },
        ))
        self.register_tool(MCPTool(
            "readmenator.findings",
            "List security findings grouped by severity (critical -> info). "
            "Includes file, line, rule_id, description, and CWE.",
            self._tool_findings,
            {
                "type": "object",
                "properties": {
                    "min_severity": {
                        "type": "string",
                        "description": "Minimum severity: info, low, medium, high, critical",
                        "default": "medium",
                    },
                },
            },
        ))
        self.register_tool(MCPTool(
            "readmenator.security_summary",
            "Get a summary of the security audit: total findings and "
            "breakdown by severity level.",
            self._tool_security_summary,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.taint",
            "Get taint propagation analysis showing how dangerous "
            "imports propagate through the codebase.",
            self._tool_taint,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.hotspots",
            "List hotspot files ranked by combined complexity and "
            "centrality score.",
            self._tool_hotspots,
            {
                "type": "object",
                "properties": {
                    "top_n": {
                        "type": "integer",
                        "description": "Number of top hotspots to return",
                        "default": 15,
                    },
                },
            },
        ))
        self.register_tool(MCPTool(
            "readmenator.cycles",
            "List circular dependencies detected in the import graph.",
            self._tool_cycles,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.communities",
            "Get community detection results: files grouped by "
            "import-based communities with cohesion scores.",
            self._tool_communities,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.layers",
            "Get architectural layer mapping for each file "
            "(presentation, business_logic, data_access, infrastructure, testing).",
            self._tool_layers,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.layer_violations",
            "Get architectural layer rule violations.",
            self._tool_layer_violations,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.rebuild",
            "Force full regeneration of KNOWLEDGE_BASE.md and all analysis.",
            self._tool_rebuild,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.update",
            "Incremental update using SHA256 content cache. "
            "Only re-scans changed files.",
            self._tool_update,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "readmenator.export_json",
            "Export the full knowledge graph as graph.json in GraphRAG-compatible format.",
            self._tool_export_json,
            {"type": "object", "properties": {}},
        ))

        self.register_resource(MCPResource(
            "readmenator://summary",
            "Codebase Summary",
            "Structured JSON summary of the entire codebase",
            "application/json",
            self._resource_summary,
        ))
        self.register_resource(MCPResource(
            "readmenator://graph",
            "Knowledge Graph",
            "Full graph data as nodes and edges",
            "application/json",
            self._resource_graph,
        ))
        self.register_resource(MCPResource(
            "readmenator://findings",
            "Security Findings",
            "All security findings with full detail",
            "application/json",
            self._resource_findings,
        ))
        self.register_resource(MCPResource(
            "readmenator://analysis",
            "Full Analysis",
            "Complete analysis: communities, god nodes, hotspots, taint, cycles",
            "application/json",
            self._resource_analysis,
        ))
        self.register_resource(MCPResource(
            "readmenator://kb",
            "Knowledge Base Full Text",
            "The complete KNOWLEDGE_BASE.md document",
            "text/markdown",
            self._resource_kb,
        ))

    # ------------------------------------------------------------------
    # Tool handlers
    # ------------------------------------------------------------------

    def _scan(self):
        root = Path(self._target_dir).resolve()
        nodes, edges = self._app._factory.scanner.scan(root)
        resolved = self._app._resolve_imports(nodes, edges, self._target_dir)
        return nodes, edges, resolved

    def _scan_deep(self):
        root = Path(self._target_dir).resolve()
        nodes, edges = self._app._factory.scanner.scan(root)
        resolved = self._app._resolve_imports(nodes, edges, self._target_dir)
        content = {n.node_id: "" for n in nodes}
        layers = LayerDetector().detect(nodes, edges)
        return nodes, edges, resolved, content, layers

    def _tool_summary(self) -> str:
        nodes, edges, resolved = self._scan()
        engine = self._app._factory
        analysis = engine.analyzer.analyze(nodes, edges, resolved)
        total_symbols = sum(len(n.symbols) for n in nodes)
        import_edges = sum(1 for e in edges if e.relation == "imports")
        langs = sorted(set(n.language for n in nodes))
        top_modules = sorted(
            nodes,
            key=lambda n: (sum(1 for e in edges if e.source == n.node_id), len(n.symbols)),
            reverse=True,
        )[:5]

        lines = [
            f"Files: {len(nodes)} | Symbols: {total_symbols} | Imports: {import_edges} | Languages: {len(langs)}",
            f"Languages: {', '.join(langs)}",
            "",
            "Top modules:",
        ]
        for n in top_modules:
            imp = sum(1 for e in edges if e.source == n.node_id)
            lines.append(f"  {n.label} ({n.language}, {len(n.symbols)} symbols, {imp} imports)")

        if analysis.god_nodes:
            lines.append("")
            lines.append("God nodes:")
            for nid, score in analysis.god_nodes[:5]:
                label = nid.split("/")[-1]
                lines.append(f"  {label} (score: {score:.1f})")

        if analysis.communities:
            lines.append("")
            lines.append(f"Communities: {len(analysis.communities)}")
            for c in analysis.communities[:5]:
                lines.append(f"  {c.label}: {c.size} files, cohesion {c.cohesion:.2f}")

        return "\n".join(lines)

    def _tool_query(self, text: str) -> str:
        nodes, edges, resolved = self._scan()
        q = self._get_query_engine(nodes, edges, resolved)
        return q.query(text)

    def _tool_explain(self, name: str) -> str:
        nodes, edges, resolved = self._scan()
        q = self._get_query_engine(nodes, edges, resolved)
        result = q.explain(name)
        if result is None:
            total = sum(len(n.symbols) for n in nodes)
            return (
                f"Symbol '{name}' not found. "
                f"KB has {total} symbols across {len(nodes)} files."
            )
        return result

    def _tool_path(self, symbol_a: str, symbol_b: str) -> str:
        nodes, edges, resolved = self._scan()
        q = self._get_query_engine(nodes, edges, resolved)
        result = q.find_path(symbol_a, symbol_b)
        if result is None:
            return (
                f"No dependency path between '{symbol_a}' and '{symbol_b}'. "
                "They may be in disconnected components or not found."
            )
        return "Dependency path: " + " --imports--> ".join(result)

    def _tool_findings(self, min_severity: str = "medium") -> str:
        root = Path(self._target_dir).resolve()
        findings = self._app._factory.security.scan(root)
        self._app._last_findings = findings
        severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
        min_level = severity_order.get(min_severity, 2)

        filtered = [
            f for f in findings
            if severity_order.get(f.severity, 99) >= min_level
        ]

        if not filtered:
            return f"No security findings at severity >= {min_severity}."

        by_severity: Dict[str, list] = {}
        for f in filtered:
            by_severity.setdefault(f.severity, []).append(f)

        lines = [f"Security findings (min: {min_severity}):"]
        for sev in ["critical", "high", "medium", "low", "info"]:
            items = by_severity.get(sev)
            if not items:
                continue
            lines.append(f"\n{sev.title()} ({len(items)}):")
            for f in items:
                label = f.file_path.split("/")[-1]
                lines.append(f"  {label}:{f.line} [{f.rule_id}] {f.description} (CWE: {f.cwe})")
        return "\n".join(lines)

    def _tool_security_summary(self) -> str:
        root = Path(self._target_dir).resolve()
        findings = self._app._factory.security.scan(root)
        return self._app._factory.security.summary(findings)

    def _tool_taint(self) -> str:
        nodes, edges, resolved, content, layers = self._scan_deep()
        taint = self._app._factory.taint.analyze(nodes, edges, resolved)
        if not taint or not taint.paths:
            return "No taint propagation paths detected."
        lines = [
            f"Taint analysis: {taint.source_count} sources, "
            f"{taint.sink_count} sinks, {len(taint.paths)} paths"
        ]
        for tp in taint.paths[:20]:
            path_str = " -> ".join(p.split("/")[-1] for p in tp.path[:5])
            if len(tp.path) > 5:
                path_str += " -> ..."
            lines.append(
                f"  {tp.source_file.split('/')[-1]} imports {tp.dangerous_import} "
                f"({tp.hops} hop{'s' if tp.hops > 1 else ''} to "
                f"{tp.sink_file.split('/')[-1]}) [{tp.severity}]"
            )
            lines.append(f"    Path: {path_str}")
        return "\n".join(lines)

    def _tool_hotspots(self, top_n: int = 15) -> str:
        nodes, edges, resolved, content, layers = self._scan_deep()
        hotspots = self._app._factory.hotspots.analyze_hotspots(nodes, edges, resolved)
        if not hotspots:
            return "No hotspot analysis available."
        lines = ["Hotspot files (combined complexity + centrality):"]
        lines.append(f"{'File':<30} {'Complexity':<12} {'Centrality':<12} {'Combined':<10} {'Symbols':<8} {'Conns':<6}")
        lines.append("-" * 80)
        for h in hotspots[:top_n]:
            label = h.file_id.split("/")[-1][:28]
            lines.append(
                f"{label:<30} {h.complexity_score:<12.3f} {h.centrality_score:<12.3f} "
                f"{h.combined_score:<10.3f} {h.symbol_count:<8} {h.connection_count:<6}"
            )
        return "\n".join(lines)

    def _tool_cycles(self) -> str:
        nodes, edges, resolved, content, layers = self._scan_deep()
        cycles = self._app._factory.hotspots.detect_cycles(nodes, resolved)
        if not cycles:
            return "No circular dependencies detected."
        lines = [f"Dependency cycles: {len(cycles)}"]
        for dc in cycles[:10]:
            files_str = " -> ".join(f.split("/")[-1] for f in dc.cycle)
            lines.append(f"  Cycle ({dc.length} files): {files_str}")
        return "\n".join(lines)

    def _tool_communities(self) -> str:
        nodes, edges, resolved = self._scan()
        analysis = self._app._factory.analyzer.analyze(nodes, edges, resolved)
        if not analysis.communities:
            return "No communities detected."
        lines = [f"Communities detected: {len(analysis.communities)}"]
        for c in analysis.communities:
            lines.append(f"\n{c.label} (Cohesion: {c.cohesion:.2f}, {c.size} files):")
            top5 = sorted(c.file_ids)[:5]
            for fid in top5:
                lines.append(f"  {fid.split('/')[-1]}")
            if len(c.file_ids) > 5:
                lines.append(f"  ... and {len(c.file_ids) - 5} more")
        return "\n".join(lines)

    def _tool_layers(self) -> str:
        nodes, edges, resolved = self._scan()
        layers = LayerDetector().detect(nodes, edges)
        summary = LayerDetector.layer_summary(layers)
        if not summary:
            return "No layers detected."
        lines = ["Architectural layers:"]
        for layer, count in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"  {layer}: {count} files")
        lines.append("")
        for layer in summary:
            files = [nid for nid, l in layers.items() if l == layer][:5]
            if files:
                lines.append(f"{layer}:")
                for f in files:
                    lines.append(f"  {f.split('/')[-1]}")
        return "\n".join(lines)

    def _tool_layer_violations(self) -> str:
        nodes, edges, resolved, content, layers = self._scan_deep()
        violations = self._app._factory.layer_rules.detect_violations(
            nodes, edges, resolved, layers
        )
        if not violations:
            return "No layer violations detected."
        strict = sum(1 for v in violations if v.severity == "strict")
        warn = sum(1 for v in violations if v.severity == "warn")
        lines = [f"Layer violations: {len(violations)} ({strict} strict, {warn} warnings)"]
        for v in violations[:20]:
            src = v.source_file.split("/")[-1]
            tgt = v.target_file.split("/")[-1]
            lines.append(f"  {src} ({v.source_layer}) -> {tgt} ({v.target_layer}): {v.description} [{v.severity}]")
        return "\n".join(lines)

    def _tool_rebuild(self) -> str:
        root = Path(self._target_dir).resolve()
        self._app.run(self._target_dir)
        self._kb_cache = None
        kb_path = root / "KNOWLEDGE_BASE.md"
        if kb_path.exists():
            size = kb_path.stat().st_size
            return f"Rebuilt successfully. KNOWLEDGE_BASE.md ({size} bytes)."
        return "Rebuild completed."

    def _tool_update(self) -> str:
        try:
            self._app.update(self._target_dir)
            self._kb_cache = None
            return "Incremental update completed."
        except Exception as e:
            return f"Update failed: {e}"

    def _tool_export_json(self) -> str:
        result = self._app.export_json(self._target_dir)
        return f"graph.json exported. {result[:200]}..."

    # ------------------------------------------------------------------
    # Resource handlers
    # ------------------------------------------------------------------

    def _resource_summary(self) -> dict:
        nodes, edges, resolved = self._scan()
        engine = self._app._factory
        analysis = engine.analyzer.analyze(nodes, edges, resolved)
        total_symbols = sum(len(n.symbols) for n in nodes)
        import_edges = sum(1 for e in edges if e.relation == "imports")
        return {
            "files": len(nodes),
            "symbols": total_symbols,
            "imports": import_edges,
            "resolved_imports": len(resolved) if resolved else 0,
            "languages": sorted(set(n.language for n in nodes)),
            "god_nodes": [(nid, round(score, 2)) for nid, score in (analysis.god_nodes or [])[:10]],
            "communities": len(analysis.communities or []),
            "hotspots": 0,
        }

    def _resource_graph(self) -> dict:
        nodes, edges, resolved = self._scan()
        return {
            "nodes": [
                {
                    "id": n.node_id,
                    "label": n.label,
                    "kind": n.kind,
                    "language": n.language,
                    "symbols": [{"name": s.name, "kind": s.kind, "line": s.line} for s in n.symbols],
                }
                for n in nodes
            ],
            "edges": [
                {"source": e.source, "target": e.target, "relation": e.relation, "confidence": e.confidence}
                for e in (resolved or edges)
            ],
        }

    def _resource_findings(self) -> dict:
        root = Path(self._target_dir).resolve()
        findings = self._app._factory.security.scan(root)
        self._app._last_findings = findings
        by_severity: Dict[str, list] = {}
        for f in findings:
            by_severity.setdefault(f.severity, []).append({
                "file": f.file_path,
                "line": f.line,
                "rule_id": f.rule_id,
                "description": f.description,
                "cwe": f.cwe,
                "severity": f.severity,
            })
        return {"total": len(findings), "by_severity": by_severity}

    def _resource_analysis(self) -> dict:
        nodes, edges, resolved, content, layers = self._scan_deep()
        factory = self._app._factory
        analysis = factory.analyzer.analyze(nodes, edges, resolved)
        taint = factory.taint.analyze(nodes, edges, resolved)
        hotspots = factory.hotspots.analyze_hotspots(nodes, edges, resolved)
        cycles = factory.hotspots.detect_cycles(nodes, resolved)
        violations = factory.layer_rules.detect_violations(nodes, edges, resolved, layers)
        return {
            "god_nodes": [(nid, round(score, 2)) for nid, score in (analysis.god_nodes or [])[:10]],
            "communities": [
                {"id": c.community_id, "label": c.label, "cohesion": round(c.cohesion, 2), "size": c.size}
                for c in (analysis.communities or [])
            ],
            "taint": {
                "paths": len(taint.paths) if taint else 0,
                "sources": taint.source_count if taint else 0,
                "sinks": taint.sink_count if taint else 0,
            } if taint else None,
            "hotspots": [
                {"file": h.file_id, "combined_score": round(h.combined_score, 3), "symbols": h.symbol_count}
                for h in hotspots[:10]
            ],
            "cycles": [{"files": c.cycle, "length": c.length} for c in cycles[:10]],
            "layer_violations": [
                {"source": v.source_file, "target": v.target_file, "severity": v.severity, "description": v.description}
                for v in violations[:20]
            ],
        }

    def _resource_kb(self) -> str:
        self._ensure_kb()
        return self._kb_cache or ""

    def _get_query_engine(self, nodes, edges, resolved):
        from readmenator._query import QueryEngine
        return QueryEngine(nodes, edges, resolved)


def main() -> None:
    """CLI entry point for `readmenator serve <path>`."""
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    config = Config()
    app = readmenatorApplication(config)

    root = Path(target).resolve()
    kb_path = root / "KNOWLEDGE_BASE.md"
    if not kb_path.exists():
        logger.info("No KNOWLEDGE_BASE.md found. Generating first...")
        app.run(target)

    server = MCPServer(app, target)
    server.run()


if __name__ == "__main__":
    main()
