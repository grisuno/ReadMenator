"""Contract tests for the MCP server protocol and tool dispatch.

Validates JSON-RPC 2.0 message handling, tool definitions, resource
definitions, proper error responses, and the full tool/resource
lifecycle using a lightweight mock server.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, Optional

from readmenator._mcp_server import MCPServer, MCPRequest, MCPTool, MCPResource
from readmenator._app import readmenatorApplication
from readmenator._config import Config


class TestMCPProtocol(unittest.TestCase):
    """Contract: MCP server implements JSON-RPC 2.0 over stdio."""

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "main.py").write_text(
            "import os\nclass App:\n    def run(self): pass\n"
        )
        app = readmenatorApplication(Config())
        self.server = MCPServer(app, str(self.root))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _make_request(self, method: str, params: Optional[Dict] = None, msg_id: Any = 1) -> MCPRequest:
        msg = {"jsonrpc": "2.0", "id": msg_id, "method": method}
        if params:
            msg["params"] = params
        return MCPRequest(msg)

    def _call(self, req: MCPRequest) -> Optional[Dict[str, Any]]:
        return self.server.dispatch(req)

    # ------------------------------------------------------------------
    # Protocol basics
    # ------------------------------------------------------------------

    def test_initialize_exchanges_protocol_version(self) -> None:
        req = self._make_request("initialize", {
            "protocolVersion": "2024-11-05",
            "clientInfo": {"name": "test", "version": "1.0"},
        })
        resp = self._call(req)
        self.assertIsNotNone(resp)
        self.assertIn("result", resp)
        self.assertEqual(resp["result"]["protocolVersion"], "2024-11-05")
        self.assertEqual(resp["result"]["serverInfo"]["name"], "readmenator")
        self.assertIn("tools", resp["result"]["capabilities"])
        self.assertIn("resources", resp["result"]["capabilities"])

    def test_notifications_initialized_returns_no_response(self) -> None:
        req = self._make_request("notifications/initialized")
        resp = self._call(req)
        self.assertIsNone(resp)

    def test_unknown_method_returns_error(self) -> None:
        self._call(self._make_request("initialize", {}))
        req = self._make_request("unknown_method")
        resp = self._call(req)
        self.assertIsNotNone(resp)
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32601)

    def test_uninitialized_request_returns_error(self) -> None:
        req = self._make_request("tools/list")
        resp = self._call(req)
        self.assertIsNotNone(resp)
        self.assertIn("error", resp)

    # ------------------------------------------------------------------
    # Tools lifecycle
    # ------------------------------------------------------------------

    def test_list_tools_returns_all_tool_definitions(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("tools/list"))
        tools = resp["result"]["tools"]
        names = [t["name"] for t in tools]
        self.assertIn("readmenator.summary", names)
        self.assertIn("readmenator.summary", names)
        self.assertIn("readmenator.query", names)
        self.assertIn("readmenator.explain", names)
        self.assertIn("readmenator.path", names)
        self.assertIn("readmenator.findings", names)
        self.assertIn("readmenator.taint", names)
        self.assertIn("readmenator.hotspots", names)
        self.assertIn("readmenator.cycles", names)
        self.assertIn("readmenator.communities", names)
        self.assertIn("readmenator.layers", names)
        self.assertIn("readmenator.layer_violations", names)
        self.assertIn("readmenator.rebuild", names)
        self.assertIn("readmenator.update", names)
        self.assertIn("readmenator.export_json", names)
        self.assertIn("readmenator.security_summary", names)

        for tool_def in tools:
            self.assertIn("name", tool_def)
            self.assertIn("description", tool_def)
            self.assertIn("inputSchema", tool_def)
            self.assertIn("type", tool_def["inputSchema"])
            self.assertIn("properties", tool_def["inputSchema"])

    def test_call_tool_without_initialize_returns_error(self) -> None:
        req = self._make_request("tools/call", {
            "name": "readmenator.summary", "arguments": {},
        })
        resp = self._call(req)
        self.assertIsNotNone(resp)
        self.assertIn("error", resp)

    def test_call_tool_unknown_tool_returns_method_not_found(self) -> None:
        self._call(self._make_request("initialize", {}))
        req = self._make_request("tools/call", {
            "name": "nonexistent.tool", "arguments": {},
        })
        resp = self._call(req)
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32601)

    def test_call_summary_tool_returns_content(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        req = self._make_request("tools/call", {
            "name": "readmenator.summary", "arguments": {},
        })
        resp = self._call(req)
        self.assertIn("result", resp)
        content = resp["result"]["content"]
        self.assertTrue(len(content) > 0)
        self.assertEqual(content[0]["type"], "text")
        self.assertIn("Files:", content[0]["text"])

    def test_call_query_tool_with_text_returns_results(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        req = self._make_request("tools/call", {
            "name": "readmenator.query", "arguments": {"text": "App"},
        })
        resp = self._call(req)
        self.assertIn("result", resp)

    def test_call_query_tool_missing_required_param_raises(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        req = self._make_request("tools/call", {
            "name": "readmenator.query", "arguments": {},
        })
        resp = self._call(req)
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32602)

    # ------------------------------------------------------------------
    # Resources lifecycle
    # ------------------------------------------------------------------

    def test_list_resources_returns_resource_definitions(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("resources/list"))
        self.assertIsNotNone(resp)
        resources = resp["result"]["resources"]
        uris = [r["uri"] for r in resources]
        self.assertIn("readmenator://summary", uris)
        self.assertIn("readmenator://graph", uris)
        self.assertIn("readmenator://findings", uris)
        self.assertIn("readmenator://analysis", uris)
        self.assertIn("readmenator://kb", uris)

        for r_def in resources:
            self.assertIn("uri", r_def)
            self.assertIn("name", r_def)
            self.assertIn("mimeType", r_def)

    def test_read_resource_summary_returns_json(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("resources/read", {
            "uri": "readmenator://summary",
        }))
        self.assertIn("result", resp)
        contents = resp["result"]["contents"]
        self.assertEqual(contents[0]["uri"], "readmenator://summary")
        self.assertEqual(contents[0]["mimeType"], "application/json")

    def test_read_resource_unknown_uri_returns_error(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("resources/read", {
            "uri": "readmenator://nonexistent",
        }))
        self.assertIn("error", resp)

    def test_read_resource_kb_returns_markdown(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("resources/read", {
            "uri": "readmenator://kb",
        }))
        self.assertIn("result", resp)
        contents = resp["result"]["contents"]
        self.assertEqual(contents[0]["mimeType"], "text/markdown")

    # ------------------------------------------------------------------
    # Tool input schema contract
    # ------------------------------------------------------------------

    def _get_tool_def(self, name: str) -> dict:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("tools/list"))
        tools = resp["result"]["tools"]
        return next(t for t in tools if t["name"] == name)

    def test_query_tool_requires_text_param(self) -> None:
        query_tool = self._get_tool_def("readmenator.query")
        self.assertIn("text", query_tool["inputSchema"]["required"])

    def test_explain_tool_requires_name_param(self) -> None:
        explain_tool = self._get_tool_def("readmenator.explain")
        self.assertIn("name", explain_tool["inputSchema"]["required"])

    def test_path_tool_requires_two_params(self) -> None:
        path_tool = self._get_tool_def("readmenator.path")
        self.assertIn("symbol_a", path_tool["inputSchema"]["required"])
        self.assertIn("symbol_b", path_tool["inputSchema"]["required"])

    # ------------------------------------------------------------------
    # Error handling
    # ------------------------------------------------------------------

    def test_parse_error_for_invalid_json(self) -> None:
        self._call(self._make_request("initialize", {}))
        req = MCPRequest({"jsonrpc": "2.0", "id": 1})
        req.method = ""
        resp = self._call(req)
        self.assertIsNotNone(resp)
        self.assertIn("error", resp)

    def test_call_tool_returns_text_content_list(self) -> None:
        self._call(self._make_request("initialize", {}))
        self.server._register_all()
        resp = self._call(self._make_request("tools/call", {
            "name": "readmenator.summary", "arguments": {},
        }))
        content = resp["result"]["content"]
        self.assertIsInstance(content, list)
        self.assertEqual(content[0]["type"], "text")


if __name__ == "__main__":
    unittest.main()
