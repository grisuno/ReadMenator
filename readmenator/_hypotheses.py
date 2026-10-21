"""Hypothesis validator: LLM/agent proposals are never facts.

The LLM proposes, the model scores, but only this validator (backed by
the AST symbol index, the static graph and receipts) decides whether a
proposed edge enters the graph as verified or is rejected with the
reason recorded. Works fully offline: proposals arrive as JSON from
any agent; no LLM is invoked here.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from readmenator._receipts import KIND_OBSERVED

STATUS_VERIFIED = "verified"
STATUS_REJECTED = "rejected"

REQUIRED_FIELDS: Tuple[str, ...] = ("caller", "callee")


@dataclass
class Hypothesis:
    caller: str
    callee: str
    rationale: str = ""
    proposed_by: str = "agent"
    extra: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Hypothesis":
        if not isinstance(data, dict):
            raise ValueError("hypothesis must be a JSON object")
        missing = [name for name in REQUIRED_FIELDS if not str(data.get(name, "")).strip()]
        if missing:
            raise ValueError(f"hypothesis missing fields: {missing}")
        allowed = set(REQUIRED_FIELDS + ("rationale", "proposed_by"))
        extra = {k: v for k, v in data.items() if k not in allowed}
        return cls(
            caller=str(data["caller"]).strip(),
            callee=str(data["callee"]).strip(),
            rationale=str(data.get("rationale", "")).strip(),
            proposed_by=str(data.get("proposed_by", "agent")).strip() or "agent",
            extra=extra,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "caller": self.caller, "callee": self.callee,
            "rationale": self.rationale, "proposed_by": self.proposed_by,
            **self.extra,
        }


@dataclass(frozen=True)
class HypothesisVerdict:
    hypothesis: Hypothesis
    status: str
    reasons: List[str] = field(default_factory=list)
    assumed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            **self.hypothesis.to_dict(),
            "status": self.status,
            "reasons": list(self.reasons),
            "assumed": self.assumed,
        }


class HypothesisValidator:
    """Constraint checker for proposed caller->callee edges.

    A proposal is verified only when every constraint passes:
      1. well-formed (required fields present);
      2. the callee exists in the symbol universe (static graph /
         symbol index / receipts);
      3. the caller is known, or the proposal marks it ``assumed``
         with an explicit user approval note.
    """

    def __init__(
        self,
        known_edges: Optional[Set[Tuple[str, str]]] = None,
        known_symbols: Optional[Set[str]] = None,
    ) -> None:
        self._known_edges = known_edges or set()
        self._known_symbols = known_symbols or set()

    def validate(self, hypothesis: Hypothesis,
                 allow_assumed: bool = False) -> HypothesisVerdict:
        reasons: List[str] = []
        assumed = False

        if not hypothesis.caller or not hypothesis.callee:
            reasons.append("malformed: caller/callee required")
            return HypothesisVerdict(hypothesis, STATUS_REJECTED, reasons)

        pair = (hypothesis.caller, hypothesis.callee)
        if pair in self._known_edges:
            reasons.append("already observed in receipts or static graph")
            return HypothesisVerdict(hypothesis, STATUS_VERIFIED, reasons)

        if self._known_symbols and not _callee_symbol_match(hypothesis.callee, self._known_symbols):
            reasons.append(
                f"callee {hypothesis.callee!r} not found in symbol index; "
                "run readmenator . --rebuild or check the class name")
            return HypothesisVerdict(hypothesis, STATUS_REJECTED, reasons)

        caller_names = {caller for caller, _ in self._known_edges}
        caller_ok = (hypothesis.caller in caller_names
                     or _callee_symbol_match(hypothesis.caller, self._known_symbols))
        if not caller_ok:
            if allow_assumed:
                assumed = True
                reasons.append("caller unknown; accepted as assumed "
                               "(explicit user approval required)")
            else:
                reasons.append(f"caller {hypothesis.caller!r} unknown; "
                               "rejected (pass allow_assumed to accept with trace)")
                return HypothesisVerdict(hypothesis, STATUS_REJECTED, reasons)
        return HypothesisVerdict(hypothesis, STATUS_VERIFIED, reasons, assumed)

    def validate_json(self, raw_json: str,
                      allow_assumed: bool = False) -> List[HypothesisVerdict]:
        """Validate a JSON list (or single object) of LLM proposals."""
        data = json.loads(raw_json)
        if isinstance(data, dict):
            data = [data]
        if not isinstance(data, list):
            raise ValueError("proposals must be a JSON object or list")
        verdicts = []
        for item in data:
            hypothesis = Hypothesis.from_dict(item)
            verdicts.append(self.validate(hypothesis, allow_assumed))
        return verdicts


def _callee_symbol_match(callee: str, symbols: Set[str]) -> bool:
    if callee in symbols:
        return True
    class_part, _, method_part = callee.partition(".")
    if class_part in symbols:
        return True
    if method_part and method_part in symbols:
        return True
    return False
