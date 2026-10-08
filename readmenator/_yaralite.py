"""Zero-dependency YARA-lite rule parser and runner.

Implements the YARA subset readmenator needs (rule header, meta,
strings, condition with `N of (...)`, `any of them`, `$identifiers`)
so tiered T1/T2/T3 text rules ship without a native YARA dependency.
Conditions evaluate through a restricted grammar, never through
arbitrary code execution.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple


RULE_HEADER_RE = re.compile(r"\brule\s+([^\s{]+)\s*\{", re.IGNORECASE)
COMMENT_RE = re.compile(r"/\*.*?\*/|//[^\n]*", re.DOTALL)
STRING_RE = re.compile(r"^\s*(\$\w+)\s*=\s*\"((?:\\.|[^\"])*)\"(.*)$")
META_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$")


@dataclass
class YaraLiteString:
    """A single named string pattern inside a rule."""

    identifier: str
    pattern: str
    nocase: bool = False


@dataclass
class YaraLiteRule:
    """A parsed YARA-lite rule with tier metadata."""

    name: str
    meta: Dict[str, Any] = field(default_factory=dict)
    strings: List[YaraLiteString] = field(default_factory=list)
    condition: str = ""

    @property
    def tier(self) -> str:
        """Return the rule tier from meta or name prefix."""
        tier = str(self.meta.get("tier", "")).upper()
        if tier in ("T1", "T2", "T3"):
            return tier
        upper = self.name.upper()
        if upper.startswith("T3-"):
            return "T3"
        if upper.startswith("T2-"):
            return "T2"
        return "T1"


@dataclass
class YaraLiteHit:
    """A single matched string occurrence."""

    identifier: str
    pattern: str
    excerpt: str
    offset: int


@dataclass
class YaraLiteMatch:
    """A rule match with all collected string hits."""

    rule: str
    tier: str
    description: str
    confidence: int
    matched_strings: List[YaraLiteHit] = field(default_factory=list)


def parse_yaralite_rules(rules_text: str) -> Tuple[List[YaraLiteRule], List[str]]:
    """Parse YARA-lite rules text into rules and error messages.

    Args:
        rules_text: Raw rules file content.

    Returns:
        Tuple of (rules, errors).
    """
    rules: List[YaraLiteRule] = []
    errors: List[str] = []
    for name, body in _rule_blocks(rules_text):
        try:
            meta_body = _section(body, "meta:", "strings:")
            strings_body = _section(body, "strings:", "condition:")
            condition = _strip_comments(_section(body, "condition:", None)).strip()
            strings = _parse_strings(strings_body)
            if not strings:
                errors.append(f"{name}: no strings parsed")
            if not condition:
                errors.append(f"{name}: missing condition")
            rules.append(
                YaraLiteRule(
                    name=name,
                    meta=_parse_meta(meta_body),
                    strings=strings,
                    condition=condition,
                )
            )
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
    if not rules:
        errors.append("no rules parsed")
    return rules, errors


def run_yaralite_rules(text: str, rules: List[YaraLiteRule]) -> List[YaraLiteMatch]:
    """Run parsed rules against a scan-text blob.

    Args:
        text: Haystack text to scan.
        rules: Parsed rules to evaluate.

    Returns:
        List of rule matches.
    """
    matches: List[YaraLiteMatch] = []
    for rule in rules:
        hits = _string_hits(text, rule)
        if _condition_matches(rule.condition, hits):
            flat = [hit for rule_hits in hits.values() for hit in rule_hits]
            matches.append(
                YaraLiteMatch(
                    rule=rule.name,
                    tier=rule.tier,
                    description=str(rule.meta.get("description") or rule.name),
                    confidence=_confidence(rule.meta.get("confidence")),
                    matched_strings=flat,
                )
            )
    return matches


def validate_yaralite_rules(rules_text: str) -> Dict[str, Any]:
    """Validate rules text and summarize tier counts.

    Args:
        rules_text: Raw rules file content.

    Returns:
        Validation payload with rule names, tier counts, and errors.
    """
    rules, errors = parse_yaralite_rules(rules_text)
    tiers: Dict[str, int] = {"T1": 0, "T2": 0, "T3": 0}
    for rule in rules:
        tiers[rule.tier] = tiers.get(rule.tier, 0) + 1
    return {
        "valid": bool(rules) and not errors,
        "rule_count": len(rules),
        "rules": [rule.name for rule in rules],
        "tiers": tiers,
        "errors": errors,
    }


def _rule_blocks(rules_text: str) -> List[Tuple[str, str]]:
    """Split rules text into (name, body) blocks by brace depth."""
    blocks: List[Tuple[str, str]] = []
    for match in RULE_HEADER_RE.finditer(rules_text):
        name = match.group(1)
        start = match.end()
        depth = 1
        index = start
        while index < len(rules_text):
            char = rules_text[index]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    blocks.append((name, rules_text[start:index]))
                    break
            index += 1
    return blocks


def _section(body: str, start_marker: str, end_marker: str | None) -> str:
    """Extract a named section body between markers."""
    start = body.lower().find(start_marker.lower())
    if start < 0:
        raise ValueError(f"missing {start_marker}")
    start += len(start_marker)
    if end_marker is None:
        return body[start:]
    end = body.lower().find(end_marker.lower(), start)
    if end < 0:
        raise ValueError(f"missing {end_marker}")
    return body[start:end]


def _parse_meta(meta_body: str) -> Dict[str, Any]:
    """Parse the meta section into a key-value map."""
    meta: Dict[str, Any] = {}
    for line in meta_body.splitlines():
        match = META_RE.match(line)
        if not match:
            continue
        key, raw_value = match.groups()
        value = raw_value.strip().rstrip(",")
        if value.startswith('"') and value.endswith('"'):
            meta[key] = _decode_yara_string(value[1:-1])
            continue
        try:
            meta[key] = int(value)
        except ValueError:
            meta[key] = value
    return meta


def _parse_strings(strings_body: str) -> List[YaraLiteString]:
    """Parse the strings section into pattern entries."""
    strings: List[YaraLiteString] = []
    for line in strings_body.splitlines():
        match = STRING_RE.match(line)
        if not match:
            continue
        identifier, raw_pattern, modifiers = match.groups()
        strings.append(
            YaraLiteString(
                identifier=identifier,
                pattern=_decode_yara_string(raw_pattern),
                nocase="nocase" in modifiers.lower(),
            )
        )
    return strings


def _strip_comments(text: str) -> str:
    """Remove YARA line and block comments from condition text."""
    return COMMENT_RE.sub(" ", text)


def _decode_yara_string(value: str) -> str:
    """Decode escaped quotes and backslashes in a YARA string."""
    return value.replace(r"\"", '"').replace(r"\\", "\\")


def _string_hits(text: str, rule: YaraLiteRule) -> Dict[str, List[YaraLiteHit]]:
    """Collect all string hits of a rule against the haystack."""
    hits: Dict[str, List[YaraLiteHit]] = {}
    for yara_string in rule.strings:
        haystack = text.lower() if yara_string.nocase else text
        needle = yara_string.pattern.lower() if yara_string.nocase else yara_string.pattern
        if not needle:
            continue
        offset = haystack.find(needle)
        while offset >= 0:
            hits.setdefault(yara_string.identifier, []).append(
                YaraLiteHit(
                    identifier=yara_string.identifier,
                    pattern=yara_string.pattern,
                    excerpt=_excerpt(text, offset, len(yara_string.pattern)),
                    offset=offset,
                )
            )
            offset = haystack.find(needle, offset + max(1, len(needle)))
    return hits


def _condition_matches(condition: str, hits: Dict[str, List[YaraLiteHit]]) -> bool:
    """Evaluate a YARA-lite condition over collected string hits."""
    hit_ids = {identifier for identifier, rule_hits in hits.items() if rule_hits}
    expression = " ".join(condition.split())

    def replace_group(match: re.Match[str]) -> str:
        """Replace an N-of group with its boolean outcome."""
        count = int(match.group(1))
        members = [member.strip() for member in match.group(2).split(",")]
        matched = 0
        for member in members:
            if member.endswith("*"):
                prefix = member[:-1]
                matched += sum(1 for identifier in hit_ids if identifier.startswith(prefix))
            elif member in hit_ids:
                matched += 1
        return str(matched >= count)

    expression = re.sub(r"(\d+)\s+of\s+\(([^)]+)\)", replace_group, expression, flags=re.IGNORECASE)
    expression = re.sub(r"\bany\s+of\s+them\b", str(bool(hit_ids)), expression, flags=re.IGNORECASE)
    expression = re.sub(
        r"\b(\d+)\s+of\s+them\b",
        lambda match: str(len(hit_ids) >= int(match.group(1))),
        expression,
        flags=re.IGNORECASE,
    )

    def replace_identifier(match: re.Match[str]) -> str:
        """Replace a string identifier with its hit boolean."""
        return str(match.group(0) in hit_ids)

    expression = re.sub(r"\$\w+", replace_identifier, expression)
    if not re.fullmatch(r"[TrueFalsandorNotefal\s().]+", expression):
        return False
    try:
        return bool(eval(expression, {"__builtins__": {}}, {}))  # noqa: S307
    except Exception:
        return False


def _confidence(value: Any) -> int:
    """Normalize a confidence meta value to a 0-100 integer."""
    if isinstance(value, int):
        return max(0, min(100, value))
    normalized = str(value or "").strip().lower()
    if normalized == "high":
        return 90
    if normalized == "medium":
        return 70
    if normalized == "low":
        return 45
    try:
        return max(0, min(100, int(normalized)))
    except ValueError:
        return 70


def _excerpt(text: str, offset: int, length: int) -> str:
    """Extract a context window around a match offset."""
    start = max(0, offset - 96)
    end = min(len(text), offset + length + 96)
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(text) else ""
    return prefix + text[start:end].replace("\n", " ").strip() + suffix
