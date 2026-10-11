"""Local Ollama client for optional LLM enrichment.

Stdlib-only HTTP against a local Ollama daemon. Every call is
bounded by a timeout and never raises: failures return "" so the
deterministic zero-token output always survives. Used only for
prose (component descriptions), never for structure.
"""

from __future__ import annotations

import json
import re
import urllib.request
from typing import Optional

from readmenator._config import Config

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


def strip_thinking(text: str) -> str:
    """Remove reasoning-model thinking blocks from a completion.

    Args:
        text: Raw model output.

    Returns:
        Output without <think> sections, stripped.
    """
    return _THINK_RE.sub("", text).strip()


class OllamaClient:
    """Minimal generate-only client for a local Ollama daemon."""

    def __init__(self, config: Config) -> None:
        """Initialise with application configuration.

        Args:
            config: Settings for host, model, timeout, and max chars.
        """
        self._config = config

    def enabled(self) -> bool:
        """Return True when Ollama enrichment is switched on."""
        return bool(self._config.OLLAMA_ENABLED)

    def available(self, timeout: Optional[float] = None) -> bool:
        """Probe the daemon without generating text.

        Args:
            timeout: Optional probe timeout override.

        Returns:
            True when /api/tags answers, False otherwise.
        """
        try:
            request = urllib.request.Request(
                self._config.OLLAMA_HOST.rstrip("/") + "/api/tags",
                method="GET",
            )
            with urllib.request.urlopen(
                request, timeout=self._config.OLLAMA_TIMEOUT_S if timeout is None else timeout
            ):
                return True
        except Exception:
            return False

    def generate(self, prompt: str, system: Optional[str] = None) -> str:
        """Generate one completion, bounded and infallible.

        Args:
            prompt: User prompt text.
            system: Optional system instruction.

        Returns:
            Completion text (thinking stripped, capped), or "" on any
            failure, including a disabled client.
        """
        if not self.enabled() or not prompt.strip():
            return ""
        payload: dict = {
            "model": self._config.OLLAMA_MODEL,
            "prompt": prompt[: self._config.OLLAMA_MAX_PROMPT_CHARS],
            "stream": False,
        }
        if system:
            payload["system"] = system
        try:
            body = json.dumps(payload).encode("utf-8")
            request = urllib.request.Request(
                self._config.OLLAMA_HOST.rstrip("/") + "/api/generate",
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=self._config.OLLAMA_TIMEOUT_S) as response:
                data = json.loads(response.read().decode("utf-8", errors="replace"))
            text = strip_thinking(str(data.get("response", "")))
            return text[: self._config.OLLAMA_MAX_CHARS]
        except Exception:
            return ""

    def describe_component(
        self, name: str, files: list, symbols: list, imports: list
    ) -> str:
        """Draft a one-paragraph component description via Ollama.

        Args:
            name: Component label.
            files: Member file paths (capped by the caller).
            symbols: Top symbol names (capped by the caller).
            imports: Outgoing dependency labels (capped by the caller).

        Returns:
            One-paragraph description, or "" when unavailable.
        """
        prompt = (
            f"Describe in one short paragraph what the '{name}' component of a "
            f"codebase does, given these files: {', '.join(files)}. "
            f"Key symbols: {', '.join(symbols)}. "
            f"It depends on: {', '.join(imports) or 'nothing else'}. "
            "Plain text, no markdown, under 60 words."
        )
        return self.generate(
            prompt,
            system="You describe software architecture components briefly and factually.",
        )
