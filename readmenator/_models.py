from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Symbol:
    name: str
    kind: str
    line: int
    doc: str = ""
    signature: str = ""


@dataclass
class Node:
    node_id: str
    label: str
    kind: str
    language: str
    doc: str = ""
    symbols: List[Symbol] = field(default_factory=list)


@dataclass
class Edge:
    source: str
    target: str
    relation: str


def pluralize_symbol_kind(kind: str, plural_map: Dict[str, str]) -> str:
    return plural_map.get(kind, kind + "s")
