"""Contract tests for the local Ollama client."""

from __future__ import annotations

import unittest

from readmenator._config import Config
from readmenator._ollama import OllamaClient, strip_thinking


class TestOllamaContract(unittest.TestCase):
    """Contract: bounded, infallible, deterministic fallback."""

    def test_disabled_client_returns_empty(self) -> None:
        """A disabled client never touches the network."""
        client = OllamaClient(Config(OLLAMA_ENABLED=False))
        self.assertFalse(client.enabled())
        self.assertEqual(client.generate("hello"), "")

    def test_unreachable_daemon_returns_empty(self) -> None:
        """A dead daemon yields '' instead of raising."""
        client = OllamaClient(Config(
            OLLAMA_ENABLED=True, OLLAMA_HOST="http://127.0.0.1:1",
            OLLAMA_TIMEOUT_S=1,
        ))
        self.assertFalse(client.available(timeout=1))
        self.assertEqual(client.generate("hello"), "")
        self.assertEqual(client.describe_component("x", ["a.py"], ["f"], []), "")

    def test_strip_thinking_removes_reasoning_blocks(self) -> None:
        """Thinking models keep only the final answer."""
        self.assertEqual(
            strip_thinking("<think>hmm</think>  Final answer. "),
            "Final answer.",
        )


if __name__ == "__main__":
    unittest.main()
