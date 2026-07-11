"""Public API for the readmenator knowledge graph generator.

Export the core types and application class used by external consumers:
  - Config: immutable settings dataclass
  - Symbol, Node, Edge: data model for codebase entities and relations
  - readmenatorApplication: high-level orchestrator for scanning, querying,
    and generating the KNOWLEDGE_BASE.md artifact
"""

from readmenator._app import readmenatorApplication
from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol

__all__ = [
    "Config",
    "Symbol",
    "Node",
    "Edge",
    "readmenatorApplication",
]
