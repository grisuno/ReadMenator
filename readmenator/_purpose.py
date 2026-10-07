"""Purpose extraction shared by every agent-facing document generator.

Turns raw file and symbol docstrings into one clean, bounded sentence
that tells a reader what a file is for. Banner rules, SPDX headers,
encoding cookies, and bare file names are rejected; files without a
module docstring fall back to the docstring of their primary symbol so
agent indexes never show an empty purpose when the code explains itself.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional

from readmenator._models import Node, Symbol

_BANNER_RUN_RE = re.compile(r"(?:[=#*]{4,}|[-_]{8,})")
_LEADING_FILE_RE = re.compile(
    r"^[\w\-.]+\.(c|h|py|js|go|rs|sh|s|java|cs|php)\b[\s:.\-]*", re.IGNORECASE
)
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9`(])")
_PRIMARY_KINDS = ("class", "struct", "interface", "trait", "enum", "function")
_ELLIPSIS = "..."


def is_garbage_doc(text: str) -> bool:
    """Return True for doc lines that carry no purpose signal.

    Args:
        text: One doc line.

    Returns:
        Whether the line is too short, an encoding cookie, or symbol noise.
    """
    stripped = text.strip()
    if len(stripped) < 3:
        return True
    if re.search(r"coding[:=]", stripped):
        return True
    return not re.search(r"[A-Za-z]{3,}", stripped)


def clean_purpose(text: str) -> str:
    """Return the purpose signal of a doc first line, or an empty string.

    Args:
        text: First line of a file or symbol docstring.

    Returns:
        The line without banners, SPDX tags, and leading file names.
    """
    stripped = text.strip()
    if is_garbage_doc(stripped):
        return ""
    if stripped.lower().startswith("spdx-license-identifier"):
        return ""
    cut = _BANNER_RUN_RE.split(stripped, maxsplit=1)[0].strip()
    cut = _LEADING_FILE_RE.sub("", cut).strip()
    if not cut or is_garbage_doc(cut):
        return ""
    if re.fullmatch(r"[\(\[].*[\)\]]", cut):
        return ""
    return cut


def escape_cell(text: str) -> str:
    """Escape markdown table breaking characters in one line of text.

    Args:
        text: Arbitrary text destined for a table cell.

    Returns:
        Single-line text with pipes escaped.
    """
    return text.replace("|", "\\|").replace("\n", " ").strip()


def truncate_words(text: str, max_chars: int) -> str:
    """Truncate text at a word boundary and mark the cut with an ellipsis.

    Args:
        text: Text to shorten.
        max_chars: Maximum length of the returned string.

    Returns:
        The original text when short enough, otherwise a word-aligned prefix.
    """
    if max_chars <= 0 or len(text) <= max_chars:
        return text
    budget = max(max_chars - len(_ELLIPSIS), 1)
    head = text[:budget]
    space = head.rfind(" ")
    if space > budget // 2:
        head = head[:space]
    return head.rstrip(" ,;:-") + _ELLIPSIS


def first_sentence(doc: str) -> str:
    """Return the first clean sentence of the first meaningful paragraph.

    Args:
        doc: Full docstring text.

    Returns:
        One sentence with whitespace collapsed, or an empty string.
    """
    for paragraph in re.split(r"\n\s*\n", doc or ""):
        lines = [clean_purpose(line) for line in paragraph.splitlines()]
        joined = " ".join(line for line in lines if line)
        if not joined:
            continue
        return _SENTENCE_END_RE.split(joined, maxsplit=1)[0].strip()
    return ""


def _primary_symbol(symbols: Iterable[Symbol]) -> Optional[Symbol]:
    """Pick the documented symbol that best represents a file.

    Public symbols outrank private ones and type-like kinds outrank
    functions; ties fall back to source order.

    Args:
        symbols: Symbols extracted from one file.

    Returns:
        The representative documented symbol, or None.
    """
    ranked = []
    for index, sym in enumerate(symbols):
        if not sym.doc or not first_sentence(sym.doc):
            continue
        kind_rank = _PRIMARY_KINDS.index(sym.kind) if sym.kind in _PRIMARY_KINDS else len(_PRIMARY_KINDS)
        private = 1 if sym.name.startswith("_") else 0
        ranked.append((private, kind_rank, index, sym))
    if not ranked:
        return None
    return min(ranked, key=lambda item: item[:3])[3]


def file_purpose(node: Node, max_chars: int) -> str:
    """Return a bounded one-sentence purpose for a file node.

    Args:
        node: Scanned file node.
        max_chars: Maximum characters of the returned purpose.

    Returns:
        Module doc sentence, else ``Symbol: sentence`` from the primary
        documented symbol, else an empty string.
    """
    sentence = first_sentence(node.doc or "")
    if not sentence:
        primary = _primary_symbol(node.symbols)
        if primary is not None:
            sentence = f"{primary.name}: {first_sentence(primary.doc)}"
    return truncate_words(sentence, max_chars)
