"""Multi-style docstring parser for the deterministic API reference.

Parses Google, NumPy, reStructuredText (Sphinx), Javadoc / JSDoc /
PHPDoc / KDoc / Doxygen tag blocks, C# XML documentation comments, and
Rustdoc markdown sections into one structured DocComment. Also recovers
raw comment blocks above a declaration in any supported language while
preserving line structure. Pure regex and string handling, zero tokens.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

STYLE_PLAIN = "plain"
STYLE_GOOGLE = "google"
STYLE_NUMPY = "numpy"
STYLE_REST = "rest"
STYLE_TAGS = "tags"
STYLE_XML = "xml"
STYLE_RUSTDOC = "rustdoc"

_SECTION_ALIASES: Dict[str, str] = {
    "args": "params",
    "arguments": "params",
    "parameters": "params",
    "params": "params",
    "param": "params",
    "keyword args": "params",
    "keyword arguments": "params",
    "other parameters": "params",
    "kwargs": "params",
    "returns": "returns",
    "return": "returns",
    "yields": "yields",
    "yield": "yields",
    "raises": "raises",
    "raise": "raises",
    "exceptions": "raises",
    "except": "raises",
    "throws": "raises",
    "errors": "raises",
    "examples": "examples",
    "example": "examples",
    "attributes": "attributes",
    "members": "attributes",
    "fields": "attributes",
    "see also": "see_also",
    "references": "see_also",
    "note": "note",
    "notes": "note",
    "warning": "warning",
    "warnings": "warning",
    "todo": "todo",
    "panics": "panics",
    "safety": "safety",
    "deprecated": "deprecated",
}

_NOTE_LABELS: Dict[str, str] = {
    "note": "Note",
    "warning": "Warning",
    "todo": "Todo",
    "panics": "Panics",
    "safety": "Safety",
}

_GOOGLE_HEADER_RE = re.compile(
    r"^\s*(" + "|".join(re.escape(k) for k in sorted(_SECTION_ALIASES, key=len, reverse=True))
    + r")\s*:\s*$",
    re.IGNORECASE,
)
_NUMPY_UNDERLINE_RE = re.compile(r"^\s*-{3,}\s*$")
_RUST_HEADER_RE = re.compile(r"^\s*#{1,3}\s+([A-Za-z ]+?)\s*$")
_REST_FIELD_RE = re.compile(r"^\s*:([a-zA-Z]+)((?:\s+[^:]+?)?)\s*:\s?(.*)$")
_REST_DIRECTIVE_RE = re.compile(r"^\s*\.\.\s+([a-zA-Z-]+)::\s*(.*)$")
_TAG_RE = re.compile(r"^\s*[@\\]([a-zA-Z]+)(\[[a-z, ]+\])?\s?(.*)$")
_XML_HINT_RE = re.compile(r"<(summary|param\s+name|returns|remarks|exception\s+cref)\b", re.IGNORECASE)
_GOOGLE_ITEM_RE = re.compile(r"^(\*{0,2}[A-Za-z_$][\w$.]*)\s*(?:\(([^)]*)\))?\s*:\s*(.*)$")
_NUMPY_ITEM_RE = re.compile(r"^(\*{0,2}[A-Za-z_$][\w$.,\s*]*?)\s*(?::\s*(.*))?$")
_RUST_ITEM_RE = re.compile(r"^[*\-+]\s+`?([A-Za-z_$][\w$]*)`?\s*(?:[:\-]+)\s*(.*)$")
_JSDOC_TYPE_RE = re.compile(r"^\{([^}]*)\}\s*(.*)$", re.DOTALL)
_DEFAULTS_TO_RE = re.compile(r"\bDefaults?\s+to\s+`?([^`\s]+?)`?\.?(?:\s|$)")
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9`\"'(\[])")

_TAG_ALIASES: Dict[str, str] = {
    "param": "param",
    "arg": "param",
    "argument": "param",
    "tparam": "tparam",
    "property": "attribute",
    "prop": "attribute",
    "field": "attribute",
    "member": "attribute",
    "return": "returns",
    "returns": "returns",
    "retval": "returns",
    "result": "returns",
    "yield": "yields",
    "yields": "yields",
    "throws": "raises",
    "throw": "raises",
    "exception": "raises",
    "raises": "raises",
    "example": "example",
    "examples": "example",
    "sample": "example",
    "code": "example",
    "see": "see",
    "sa": "see",
    "seealso": "see",
    "link": "see",
    "deprecated": "deprecated",
    "since": "since",
    "version": "since",
    "brief": "brief",
    "short": "brief",
    "summary": "brief",
    "details": "details",
    "description": "details",
    "desc": "details",
    "note": "note",
    "remark": "note",
    "remarks": "note",
    "warning": "warning",
    "attention": "warning",
    "todo": "todo",
    "pre": "note",
    "post": "note",
}


@dataclass
class DocField:
    """One documented item: a parameter, return value, exception, or attribute.

    Attributes:
        name: Parameter, attribute, or exception name ("" for returns).
        type: Declared type text from the docstring ("" when absent).
        description: Free-text description.
        default: Default value text when the style declares one.
    """

    name: str = ""
    type: str = ""
    description: str = ""
    default: str = ""

    def to_dict(self) -> Dict[str, str]:
        """Serialise to a plain dict for JSON output."""
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "default": self.default,
        }


@dataclass
class DocComment:
    """Structured documentation recovered from one docstring or comment block.

    Attributes:
        summary: First sentence or brief line.
        description: Remaining free text (Markdown-compatible).
        params: Documented parameters in source order.
        returns: Documented return value, if any.
        yields: Documented generator yield, if any.
        raises: Documented exceptions or error conditions.
        attributes: Documented attributes, properties, or fields.
        examples: Example code blocks (verbatim).
        notes: Labelled admonitions as (label, text) pairs.
        see_also: Cross-reference targets.
        deprecated: Deprecation message ("" when not deprecated).
        since: Version the entity appeared in.
        style: Detected docstring style.
    """

    summary: str = ""
    description: str = ""
    params: List[DocField] = field(default_factory=list)
    returns: Optional[DocField] = None
    yields: Optional[DocField] = None
    raises: List[DocField] = field(default_factory=list)
    attributes: List[DocField] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    notes: List[Tuple[str, str]] = field(default_factory=list)
    see_also: List[str] = field(default_factory=list)
    deprecated: str = ""
    since: str = ""
    style: str = STYLE_PLAIN

    @property
    def is_empty(self) -> bool:
        """Return True when no documentation text was recovered."""
        return not (
            self.summary or self.description or self.params or self.returns
            or self.yields or self.raises or self.attributes or self.examples
            or self.notes or self.see_also or self.deprecated
        )

    def param(self, name: str) -> Optional[DocField]:
        """Return the documented parameter called *name* (stars ignored)."""
        wanted = name.lstrip("*$&")
        for item in self.params:
            if item.name.lstrip("*$&") == wanted:
                return item
        return None

    def to_dict(self) -> Dict[str, object]:
        """Serialise to a plain dict for JSON output."""
        return {
            "summary": self.summary,
            "description": self.description,
            "params": [p.to_dict() for p in self.params],
            "returns": self.returns.to_dict() if self.returns else None,
            "yields": self.yields.to_dict() if self.yields else None,
            "raises": [r.to_dict() for r in self.raises],
            "attributes": [a.to_dict() for a in self.attributes],
            "examples": list(self.examples),
            "notes": [[label, text] for label, text in self.notes],
            "see_also": list(self.see_also),
            "deprecated": self.deprecated,
            "since": self.since,
            "style": self.style,
        }


def clean_text(text: str) -> str:
    """Dedent *text* like ``inspect.cleandoc`` and strip blank edges.

    Args:
        text: Raw docstring or comment body.

    Returns:
        Normalised text with tabs expanded and common indentation removed.
    """
    lines = text.expandtabs().split("\n")
    if not lines:
        return ""
    first = lines[0].strip()
    rest = lines[1:]
    indents = [len(line) - len(line.lstrip()) for line in rest if line.strip()]
    margin = min(indents) if indents else 0
    body = [first] + [line[margin:].rstrip() for line in rest]
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return "\n".join(body)


def detect_style(text: str) -> str:
    """Classify the docstring convention used by *text*.

    Args:
        text: Cleaned docstring.

    Returns:
        One of the STYLE_* constants.
    """
    if _XML_HINT_RE.search(text):
        return STYLE_XML
    lines = text.split("\n")
    for pos, line in enumerate(lines):
        if _REST_FIELD_RE.match(line) and re.match(
            r"^\s*:(param|parameter|arg|argument|key|keyword|type|returns?|rtype|raises?|"
            r"except|exception|var|ivar|cvar|vartype|yields?|ytype)\b",
            line,
        ):
            return STYLE_REST
        if (
            pos + 1 < len(lines)
            and _NUMPY_UNDERLINE_RE.match(lines[pos + 1])
            and line.strip().lower() in _SECTION_ALIASES
        ):
            return STYLE_NUMPY
    for line in lines:
        tag = _TAG_RE.match(line)
        if tag and tag.group(1).lower() in _TAG_ALIASES:
            return STYLE_TAGS
    for line in lines:
        if _GOOGLE_HEADER_RE.match(line):
            return STYLE_GOOGLE
    for line in lines:
        header = _RUST_HEADER_RE.match(line)
        if header and header.group(1).strip().lower() in _SECTION_ALIASES:
            return STYLE_RUSTDOC
    return STYLE_PLAIN


def split_summary(text: str) -> Tuple[str, str]:
    """Split free text into a one-sentence summary and the remainder.

    The summary is the first paragraph when it holds one sentence,
    otherwise the first sentence of it; the rest becomes the description.

    Args:
        text: Free-text documentation.

    Returns:
        Tuple of (summary, description).
    """
    stripped = text.strip()
    if not stripped:
        return "", ""
    paragraphs = re.split(r"\n\s*\n", stripped, maxsplit=1)
    first = paragraphs[0]
    rest = paragraphs[1].strip() if len(paragraphs) > 1 else ""
    if first.lstrip().startswith(("```", ">>>", "|", "-", "*", "#")) and "\n" in first:
        return "", stripped
    joined = " ".join(line.strip() for line in first.split("\n"))
    sentences = _SENTENCE_END_RE.split(joined, maxsplit=1)
    if len(sentences) > 1:
        remainder = sentences[1].strip()
        rest = f"{remainder}\n\n{rest}".strip() if rest else remainder
    return sentences[0].strip(), rest


def _indent(line: str) -> int:
    """Return the number of leading spaces in *line*."""
    return len(line) - len(line.lstrip(" "))


def _join_block(lines: List[str]) -> str:
    """Join continuation lines, keeping blank-line paragraph breaks."""
    return clean_text("\n".join(lines)).strip()


def _section_key(header: str) -> str:
    """Normalise a section header to its canonical key."""
    return _SECTION_ALIASES.get(header.strip().lower().rstrip(":"), "")


def _apply_section(doc: DocComment, key: str, body: List[str], item_mode: str) -> None:
    """Store one parsed section body into *doc*.

    Args:
        doc: Target comment being filled.
        key: Canonical section key.
        body: Raw section lines (dedented relative to the header).
        item_mode: ``google``, ``numpy``, or ``rustdoc`` item grammar.
    """
    text = _join_block(body)
    if not text and key not in ("examples",):
        return
    if key == "params":
        doc.params.extend(_parse_items(body, item_mode))
    elif key == "attributes":
        doc.attributes.extend(_parse_items(body, item_mode))
    elif key == "raises":
        items = _parse_items(body, item_mode, allow_bare=True)
        doc.raises.extend(items or [DocField(description=text)])
    elif key in ("returns", "yields"):
        result = _parse_return(body, item_mode)
        if key == "returns":
            doc.returns = result
        else:
            doc.yields = result
    elif key == "examples":
        if text:
            doc.examples.append(_strip_fence(text))
    elif key == "see_also":
        doc.see_also.extend(_split_refs(text))
    elif key == "deprecated":
        doc.deprecated = " ".join(text.split()) or "Deprecated."
    elif key in _NOTE_LABELS:
        doc.notes.append((_NOTE_LABELS[key], text))


def _strip_fence(text: str) -> str:
    """Remove one enclosing Markdown code fence from *text*."""
    lines = text.split("\n")
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
    return "\n".join(lines).strip("\n")


def _split_refs(text: str) -> List[str]:
    """Split a see-also body into reference targets."""
    refs: List[str] = []
    for chunk in re.split(r"[,\n]", text):
        target = chunk.strip().strip("`").split(" : ")[0].split(" -- ")[0].strip()
        target = re.sub(r"^:[a-z]+:`?|`$", "", target).strip("`~ ")
        if target and target not in refs:
            refs.append(target)
    return refs


def _parse_items(body: List[str], mode: str, allow_bare: bool = False) -> List[DocField]:
    """Parse a list of ``name (type): description`` style items.

    Args:
        body: Section lines.
        mode: ``google``, ``numpy``, or ``rustdoc`` item grammar.
        allow_bare: Accept items that are only a type name (raises sections).

    Returns:
        Parsed fields in source order.
    """
    items: List[DocField] = []
    content = [line for line in body]
    nonblank = [_indent(line) for line in content if line.strip()]
    if not nonblank:
        return items
    base = min(nonblank)
    current: Optional[DocField] = None
    desc: List[str] = []

    def flush() -> None:
        """Finalise the item under construction."""
        if current is not None:
            extra = _join_block(desc)
            if extra:
                current.description = (
                    f"{current.description} {extra}".strip()
                    if current.description and "\n" not in extra
                    else (f"{current.description}\n{extra}".strip() if current.description else extra)
                )
            items.append(current)

    for line in content:
        if not line.strip():
            desc.append("")
            continue
        if _indent(line) > base and current is not None:
            desc.append(line.strip() if mode != "numpy" else line[base:])
            continue
        stripped = line.strip()
        parsed: Optional[DocField] = None
        if mode == "rustdoc":
            match = _RUST_ITEM_RE.match(stripped)
            if match:
                parsed = DocField(name=match.group(1), description=match.group(2).strip())
            elif allow_bare and stripped[:1] in "*-+":
                parsed = DocField(description=stripped[1:].strip())
        elif mode == "numpy":
            match = _NUMPY_ITEM_RE.match(stripped)
            if match:
                name = match.group(1).strip()
                kind = (match.group(2) or "").strip()
                if allow_bare and not kind:
                    parsed = DocField(name=name)
                else:
                    parsed = DocField(name=name, type=kind)
        else:
            match = _GOOGLE_ITEM_RE.match(stripped)
            if match:
                parsed = DocField(
                    name=match.group(1),
                    type=(match.group(2) or "").strip(),
                    description=match.group(3).strip(),
                )
            elif allow_bare:
                parsed = DocField(name=stripped.rstrip(":"))
        if parsed is None:
            if current is not None:
                desc.append(stripped)
            continue
        flush()
        if not parsed.default:
            hint = _DEFAULTS_TO_RE.search(parsed.description)
            if hint:
                parsed.default = hint.group(1).strip()
        if parsed.type:
            default = re.search(r"default[s]?\s*[:=]?\s*(.+)$", parsed.type, re.IGNORECASE)
            if default:
                parsed.default = default.group(1).strip()
                parsed.type = re.sub(r",?\s*default.*$", "", parsed.type, flags=re.IGNORECASE).strip()
            parsed.type = re.sub(r",?\s*optional\s*$", "", parsed.type).strip()
        current = parsed
        desc = []
    flush()
    return items


def _parse_return(body: List[str], mode: str) -> DocField:
    """Parse a returns/yields section body into one DocField."""
    text = _join_block(body)
    if mode == "numpy":
        lines = [line for line in body if line.strip()]
        if lines:
            head = lines[0].strip()
            rest = _join_block(lines[1:]) if len(lines) > 1 else ""
            if ":" in head:
                name, kind = head.split(":", 1)
                return DocField(name=name.strip(), type=kind.strip(), description=rest)
            return DocField(type=head, description=rest)
    match = re.match(r"^([A-Za-z_][\w.\[\], |]*?)\s*:\s+(.*)$", text, re.DOTALL)
    if match and len(match.group(1)) <= 60 and " " not in match.group(1).replace(", ", ",").replace(" | ", "|"):
        return DocField(type=match.group(1).strip(), description=match.group(2).strip())
    return DocField(description=text)


def _parse_sections(text: str, mode: str) -> DocComment:
    """Parse Google, NumPy, or Rustdoc section-structured text."""
    doc = DocComment(style=mode)
    lines = text.split("\n")
    free: List[str] = []
    key = ""
    body: List[str] = []
    header_indent = 0
    pos = 0
    while pos < len(lines):
        line = lines[pos]
        new_key = ""
        skip = 1
        if mode == STYLE_NUMPY:
            if pos + 1 < len(lines) and _NUMPY_UNDERLINE_RE.match(lines[pos + 1]):
                new_key = _section_key(line) or "note"
                skip = 2
        elif mode == STYLE_RUSTDOC:
            header = _RUST_HEADER_RE.match(line)
            if header:
                new_key = _section_key(header.group(1))
        else:
            header = _GOOGLE_HEADER_RE.match(line)
            if header:
                new_key = _section_key(header.group(1))
        if new_key and (mode != STYLE_GOOGLE or not key or _indent(line) <= header_indent):
            if key:
                _apply_section(doc, key, body, mode)
            key = new_key
            header_indent = _indent(line)
            body = []
            pos += skip
            continue
        if key:
            if (
                mode == STYLE_GOOGLE and line.strip() and _indent(line) <= header_indent
                and key not in ("examples",)
            ):
                _apply_section(doc, key, body, mode)
                key = ""
                body = []
                free.append(line)
            else:
                body.append(line)
        else:
            free.append(line)
        pos += 1
    if key:
        _apply_section(doc, key, body, mode)
    doc.summary, doc.description = split_summary("\n".join(free))
    return doc


def _parse_rest(text: str) -> DocComment:
    """Parse reStructuredText / Sphinx field lists and directives."""
    doc = DocComment(style=STYLE_REST)
    types: Dict[str, str] = {}
    vartypes: Dict[str, str] = {}
    free: List[str] = []
    lines = text.split("\n")
    pos = 0
    while pos < len(lines):
        line = lines[pos]
        field_match = _REST_FIELD_RE.match(line)
        directive = _REST_DIRECTIVE_RE.match(line)
        if not field_match and not directive:
            free.append(line)
            pos += 1
            continue
        base = _indent(line)
        cont: List[str] = []
        pos += 1
        while pos < len(lines) and (not lines[pos].strip() or _indent(lines[pos]) > base):
            if not lines[pos].strip() and (pos + 1 >= len(lines) or _indent(lines[pos + 1]) <= base):
                break
            cont.append(lines[pos])
            pos += 1
        if directive:
            name = directive.group(1).lower()
            body = "\n".join([directive.group(2)] + [clean_text("\n".join(cont))]).strip()
            if name in ("note", "warning", "todo", "attention", "important", "tip", "hint", "danger", "caution"):
                label = "Warning" if name in ("warning", "attention", "danger", "caution") else name.capitalize()
                if name == "important":
                    label = "Note"
                doc.notes.append((label, body))
            elif name == "deprecated":
                doc.deprecated = " ".join(body.split()) or "Deprecated."
            elif name in ("versionadded", "versionchanged"):
                if name == "versionadded" and not doc.since:
                    doc.since = directive.group(2).strip()
            elif name == "seealso":
                doc.see_also.extend(_split_refs(body))
            elif name in ("code-block", "code", "sourcecode", "doctest"):
                doc.examples.append(clean_text("\n".join(cont)))
            else:
                free.append(line)
                free.extend(cont)
            continue
        tag = field_match.group(1).lower()
        arg = field_match.group(2).strip()
        value = " ".join(
            [field_match.group(3).strip()] + [c.strip() for c in cont if c.strip()]
        ).strip()
        if tag in ("param", "parameter", "arg", "argument", "key", "keyword"):
            parts = arg.split()
            name = parts[-1] if parts else ""
            kind = " ".join(parts[:-1])
            doc.params.append(DocField(name=name, type=kind, description=value))
        elif tag == "type":
            types[arg] = value
        elif tag in ("returns", "return"):
            doc.returns = DocField(type=(doc.returns.type if doc.returns else ""), description=value)
        elif tag == "rtype":
            if doc.returns is None:
                doc.returns = DocField()
            doc.returns.type = value
        elif tag in ("yields", "yield"):
            doc.yields = DocField(type=(doc.yields.type if doc.yields else ""), description=value)
        elif tag == "ytype":
            if doc.yields is None:
                doc.yields = DocField()
            doc.yields.type = value
        elif tag in ("raises", "raise", "except", "exception", "throws"):
            doc.raises.append(DocField(name=arg, description=value))
        elif tag in ("var", "ivar", "cvar"):
            doc.attributes.append(DocField(name=arg, description=value))
        elif tag == "vartype":
            vartypes[arg] = value
        else:
            free.append(line)
            free.extend(cont)
    for item in doc.params:
        if not item.type and item.name in types:
            item.type = types[item.name]
    for item in doc.attributes:
        if not item.type and item.name in vartypes:
            item.type = vartypes[item.name]
    free_text = "\n".join(free)
    examples, free_text = _extract_doctests(free_text)
    doc.examples.extend(examples)
    doc.summary, doc.description = split_summary(free_text)
    return doc


def _extract_doctests(text: str) -> Tuple[List[str], str]:
    """Pull ``>>>`` doctest blocks out of free text.

    Returns:
        Tuple of (example blocks, remaining text).
    """
    examples: List[str] = []
    kept: List[str] = []
    block: List[str] = []
    for line in text.split("\n"):
        if line.strip().startswith(">>>") or (block and line.strip()):
            block.append(line.strip())
            continue
        if block:
            examples.append("\n".join(block))
            block = []
        kept.append(line)
    if block:
        examples.append("\n".join(block))
    return examples, "\n".join(kept)


def _parse_jsdoc_param(rest: str) -> DocField:
    """Parse the body of a ``@param`` tag in JSDoc, PHPDoc, Javadoc, or Doxygen form."""
    kind = ""
    typed = _JSDOC_TYPE_RE.match(rest)
    if typed:
        kind = typed.group(1).strip()
        rest = typed.group(2)
    parts = rest.split(None, 1)
    if not parts:
        return DocField(type=kind)
    first = parts[0]
    remainder = parts[1] if len(parts) > 1 else ""
    if not kind and not first.startswith(("$", "[")) and remainder.split(None, 1)[:1] and remainder.split(None, 1)[0].startswith("$"):
        kind = first
        bits = remainder.split(None, 1)
        first = bits[0]
        remainder = bits[1] if len(bits) > 1 else ""
    default = ""
    if first.startswith("[") and first.endswith("]"):
        first = first[1:-1]
        if "=" in first:
            first, default = first.split("=", 1)
    remainder = re.sub(r"^[-:]\s*", "", remainder.strip())
    return DocField(name=first, type=kind, description=remainder, default=default)


def _parse_tags(text: str) -> DocComment:
    """Parse Javadoc / JSDoc / PHPDoc / KDoc / Doxygen tag blocks."""
    doc = DocComment(style=STYLE_TAGS)
    free: List[str] = []
    tags: List[Tuple[str, str, List[str]]] = []
    for line in text.split("\n"):
        match = _TAG_RE.match(line)
        if match and match.group(1).lower() in _TAG_ALIASES:
            tags.append((_TAG_ALIASES[match.group(1).lower()], match.group(3), []))
            continue
        if match and not tags and match.group(1).lower() not in _TAG_ALIASES:
            if line.strip().startswith("@"):
                continue
        if tags:
            tags[-1][2].append(line)
        else:
            free.append(line)
    brief = ""
    details: List[str] = []
    for tag, head, cont in tags:
        body_lines = [head] + cont
        joined = " ".join(part.strip() for part in body_lines if part.strip())
        if tag == "param":
            doc.params.append(_parse_jsdoc_param(joined))
        elif tag == "attribute":
            doc.attributes.append(_parse_jsdoc_param(joined))
        elif tag in ("returns", "yields"):
            kind = ""
            typed = _JSDOC_TYPE_RE.match(joined)
            if typed:
                kind, joined = typed.group(1).strip(), typed.group(2).strip()
            result = DocField(type=kind, description=joined)
            if tag == "returns":
                if doc.returns and doc.returns.description:
                    doc.returns.description += f"; {joined}"
                else:
                    doc.returns = result
            else:
                doc.yields = result
        elif tag == "raises":
            typed = _JSDOC_TYPE_RE.match(joined)
            if typed:
                doc.raises.append(DocField(name=typed.group(1).strip(), description=typed.group(2).strip()))
            else:
                parts = joined.split(None, 1)
                doc.raises.append(DocField(
                    name=parts[0] if parts else "",
                    description=re.sub(r"^[-:]\s*", "", parts[1]) if len(parts) > 1 else "",
                ))
        elif tag == "example":
            block = clean_text("\n".join(body_lines))
            if block:
                doc.examples.append(_strip_fence(block))
        elif tag == "see":
            doc.see_also.extend(_split_refs(re.sub(r"[{}]|@link\s*", "", joined)))
        elif tag == "deprecated":
            doc.deprecated = joined or "Deprecated."
        elif tag == "since":
            doc.since = doc.since or joined
        elif tag == "brief":
            brief = joined
        elif tag == "details":
            details.append(clean_text("\n".join(body_lines)))
        elif tag in _NOTE_LABELS:
            doc.notes.append((_NOTE_LABELS[tag], joined))
        elif tag == "tparam":
            parsed = _parse_jsdoc_param(joined)
            doc.notes.append(("Type parameter", f"{parsed.name}: {parsed.description}".strip(": ")))
    free_text = "\n".join(free + details)
    summary, description = split_summary(free_text)
    if brief:
        description = "\n\n".join(part for part in (summary, description) if part) if summary else description
        summary = brief
    doc.summary, doc.description = summary, description
    return doc


def _xml_inline(text: str) -> str:
    """Convert inline C# XML doc markup to Markdown."""
    text = re.sub(r'<see\s+(?:cref|langword|href)="([^"]+)"\s*/>', lambda m: f"`{m.group(1).split(':')[-1]}`", text)
    text = re.sub(r'<paramref\s+name="([^"]+)"\s*/>', r"`\1`", text)
    text = re.sub(r'<typeparamref\s+name="([^"]+)"\s*/>', r"`\1`", text)
    text = re.sub(r"<c>(.*?)</c>", r"`\1`", text, flags=re.DOTALL)
    text = re.sub(r"<para>|</para>", "\n\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    return clean_text(text)


def _parse_xml(text: str) -> DocComment:
    """Parse C# / VB XML documentation comments."""
    doc = DocComment(style=STYLE_XML)

    def grab(tag: str) -> str:
        """Return the inner text of the first *tag* element."""
        match = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", text, re.DOTALL | re.IGNORECASE)
        return _xml_inline(match.group(1)) if match else ""

    summary_text = grab("summary")
    doc.summary, doc.description = split_summary(summary_text)
    remarks = grab("remarks")
    if remarks:
        doc.description = "\n\n".join(part for part in (doc.description, remarks) if part)
    for match in re.finditer(r'<param\s+name="([^"]+)"\s*>(.*?)</param>', text, re.DOTALL):
        doc.params.append(DocField(name=match.group(1), description=" ".join(_xml_inline(match.group(2)).split())))
    returns = grab("returns") or grab("value")
    if returns:
        doc.returns = DocField(description=" ".join(returns.split()))
    for match in re.finditer(r'<exception\s+cref="([^"]+)"\s*>(.*?)</exception>', text, re.DOTALL):
        doc.raises.append(DocField(name=match.group(1).split(":")[-1], description=" ".join(_xml_inline(match.group(2)).split())))
    for match in re.finditer(r"<example>(.*?)</example>", text, re.DOTALL):
        code = re.search(r"<code>(.*?)</code>", match.group(1), re.DOTALL)
        doc.examples.append(clean_text(code.group(1) if code else _xml_inline(match.group(1))))
    for match in re.finditer(r'<seealso\s+cref="([^"]+)"\s*/>', text):
        doc.see_also.append(match.group(1).split(":")[-1])
    for match in re.finditer(r'<typeparam\s+name="([^"]+)"\s*>(.*?)</typeparam>', text, re.DOTALL):
        doc.notes.append(("Type parameter", f"{match.group(1)}: {' '.join(_xml_inline(match.group(2)).split())}"))
    return doc


def parse_docstring(text: str) -> DocComment:
    """Parse *text* in any supported convention into a DocComment.

    Args:
        text: Raw docstring or recovered comment body (markers stripped).

    Returns:
        Structured documentation; empty when *text* is blank.
    """
    cleaned = clean_text(text or "")
    if not cleaned.strip():
        return DocComment()
    style = detect_style(cleaned)
    if style == STYLE_XML:
        doc = _parse_xml(cleaned)
    elif style == STYLE_REST:
        doc = _parse_rest(cleaned)
    elif style == STYLE_TAGS:
        doc = _parse_tags(cleaned)
    elif style in (STYLE_NUMPY, STYLE_GOOGLE, STYLE_RUSTDOC):
        doc = _parse_sections(cleaned, style)
    else:
        doc = DocComment(style=STYLE_PLAIN)
        examples, remaining = _extract_doctests(cleaned)
        doc.examples.extend(examples)
        doc.summary, doc.description = split_summary(remaining)
    if style != STYLE_REST and doc.description:
        examples, remaining = _extract_doctests(doc.description)
        if examples:
            doc.examples.extend(examples)
            doc.description = remaining.strip()
    return doc


_LINE_PREFIXES: Dict[str, Tuple[str, ...]] = {
    "hash": ("##", "#"),
    "slash": ("///", "//!", "//"),
    "dash": ("---", "--"),
    "semi": (";;", ";"),
}

_LANGUAGE_COMMENT_FAMILY: Dict[str, Tuple[str, ...]] = {
    "py": ("hash",),
    "sh": ("hash",),
    "bash": ("hash",),
    "zsh": ("hash",),
    "rb": ("hash",),
    "nim": ("hash",),
    "gd": ("hash",),
    "ex": ("hash",),
    "exs": ("hash",),
    "lua": ("dash",),
    "asm": ("semi", "slash"),
    "s": ("semi", "slash", "hash"),
    "S": ("semi", "slash", "hash"),
    "php": ("slash", "hash"),
}

_SKIPPABLE_DECL_RE = re.compile(
    r"^\s*(@[A-Za-z_][\w.]*(\(.*\))?|#\[.*\]|#!\[.*\]|\[\[.*\]\]|\[[A-Z][\w.]*(\(.*\))?\]|template\s*<.*>|"
    r"export\s+default\s*$|@(?:spec|impl|tag)\b.*)\s*$"
)
_RULER_RE = re.compile(r"^[\s/*#=\-;~+]*$")


def _strip_line_prefix(line: str, prefixes: Tuple[str, ...]) -> Optional[str]:
    """Return *line* without its comment prefix, or None when it is not a comment."""
    stripped = line.strip()
    for prefix in prefixes:
        if stripped.startswith(prefix):
            body = stripped[len(prefix):]
            if body.startswith("<") and prefix in ("///", "//!", "//"):
                return None
            if prefix == "#" and body.startswith("!"):
                return None
            return body[1:] if body.startswith(" ") else body
    return None


def _elixir_doc(lines: List[str], index: int, lookback: int) -> Optional[str]:
    """Recover an Elixir ``@doc`` heredoc or string above line *index*."""
    pos = index - 1
    floor = max(-1, index - 1 - lookback)
    while pos > floor and (not lines[pos].strip() or lines[pos].strip().startswith("@spec")):
        pos -= 1
    if pos <= floor:
        return None
    if lines[pos].strip() in ('"""', "'''"):
        end = pos
        pos -= 1
        while pos > floor and not re.match(r'^\s*@(module)?doc\s+(~[sS])?("""|\'\'\')', lines[pos]):
            pos -= 1
        if pos <= floor:
            return None
        return "\n".join(lines[pos + 1:end])
    single = re.match(r'^\s*@doc\s+"(.*)"\s*$', lines[pos])
    if single:
        return single.group(1)
    return None


def recover_comment(content_lines: List[str], line: int, language: str, lookback: int) -> str:
    """Recover the raw documentation comment directly above a declaration.

    Walks upwards from the one-based *line*, skipping attribute and
    decorator lines, and collects one contiguous comment block in any
    of ``///``, ``//!``, ``//``, ``/** */``, ``/* */``, ``#``, ``##``,
    ``--``, ``;``, or Elixir ``@doc`` forms. Line structure is preserved
    so tag and section grammars can be parsed afterwards.

    Args:
        content_lines: File content split into lines.
        line: One-based declaration line.
        language: Scanner language label (file extension without dot).
        lookback: Maximum number of lines to scan upwards.

    Returns:
        Comment body without markers, or "" when none is adjacent.
    """
    index = line - 1
    if index <= 0 or index > len(content_lines):
        return ""
    if language in ("ex", "exs"):
        elixir = _elixir_doc(content_lines, index, lookback)
        if elixir is not None:
            return clean_text(elixir)
    families = _LANGUAGE_COMMENT_FAMILY.get(language, ("slash",))
    prefixes: Tuple[str, ...] = tuple(p for fam in families for p in _LINE_PREFIXES[fam])
    floor = max(-1, index - 1 - lookback)
    pos = index - 1
    while pos > floor and _SKIPPABLE_DECL_RE.match(content_lines[pos]):
        pos -= 1
    if pos <= floor:
        return ""
    current = content_lines[pos].rstrip()
    collected: List[str] = []
    if "slash" in families and current.strip().endswith("*/"):
        block: List[str] = []
        while pos > floor:
            text = content_lines[pos]
            block.insert(0, text)
            if "/*" in text:
                break
            pos -= 1
        else:
            return ""
        raw = "\n".join(block)
        start = raw.find("/*")
        end = raw.rfind("*/")
        if start < 0 or end < start:
            return ""
        inner = raw[start + 2:end]
        if inner.startswith(("*", "!")):
            inner = inner[1:]
        for text in inner.split("\n"):
            stripped = text.strip()
            if stripped.startswith("*") and not stripped.startswith("*/"):
                stripped = stripped[1:]
                if stripped.startswith(" "):
                    stripped = stripped[1:]
                collected.append(stripped)
            else:
                collected.append(text)
        body = clean_text("\n".join(collected))
        return "" if _RULER_RE.match(body) else body
    while pos > floor:
        body = _strip_line_prefix(content_lines[pos], prefixes)
        if body is None:
            break
        collected.insert(0, body.rstrip())
        pos -= 1
    while collected and _RULER_RE.match(collected[0]) and collected[0].strip():
        collected.pop(0)
    while collected and _RULER_RE.match(collected[-1]) and collected[-1].strip():
        collected.pop()
    text = clean_text("\n".join(collected))
    if text and _RULER_RE.match(text):
        return ""
    return text
