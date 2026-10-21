"""Uncertainty engine: classify candidate edges, never invent facts.

Input: candidate edges (kind=candidate) declared by release receipts
(feasible sets from config / CLI / interface contract) plus the
observed edges recorded so far. Output: predicted edges -- always
labeled ``predicted`` with the model name, the probability and the
feature vector that produced them, for downstream audit.

Two scorers:
  - HeuristicScorer: pure-Python, zero-dependency logistic-style
    readout over the feature vector.
  - RandomForestScorer: optional sklearn ensemble trained on the
    receipt history (observed edges are label 1, unobserved
    candidates label 0), calibrating per-class confidence. Falls back
    to the heuristic scorer when sklearn is unavailable.

Golden rule: a prediction is a hypothesis with provenance; presenting
it as fact is the cardinal error.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from readmenator._config import Config
from readmenator._receipts import EdgeInfo, KIND_CANDIDATE, KIND_PREDICTED

MODEL_NAME = "readmenator-uncertainty"
MODEL_VERSION = "v1"

FEATURE_NAMES: Tuple[str, ...] = (
    "confidence",
    "evidence_config",
    "evidence_cli",
    "evidence_toml",
    "evidence_interface",
    "evidence_platform",
    "target_github",
    "target_gitlab",
    "target_bitbucket",
    "target_git",
    "target_pypi_or_docs",
    "historically_observed",
    "target_observed",
)


def _bucket_evidence(evidence: str) -> Dict[str, int]:
    flags = {name: 0 for name in FEATURE_NAMES[1:6]}
    lowered = (evidence or "").lower()
    if lowered.startswith("config:") or lowered.startswith("toml:"):
        if lowered.startswith("toml:"):
            flags["evidence_toml"] = 1
        else:
            flags["evidence_config"] = 1
    elif lowered.startswith("cli:"):
        flags["evidence_cli"] = 1
    elif lowered.startswith("interface:"):
        flags["evidence_interface"] = 1
    elif lowered.startswith("platform:"):
        flags["evidence_platform"] = 1
    return flags


def _bucket_target(callee: str) -> Dict[str, int]:
    flags = {name: 0 for name in FEATURE_NAMES[6:11]}
    lowered = (callee or "").lower()
    if "github" in lowered:
        flags["target_github"] = 1
    elif "gitlab" in lowered:
        flags["target_gitlab"] = 1
    elif "bitbucket" in lowered:
        flags["target_bitbucket"] = 1
    elif lowered.startswith("gitoperations"):
        flags["target_git"] = 1
    else:
        flags["target_pypi_or_docs"] = 1
    return flags


def featurize(edge: EdgeInfo, known_observed: set) -> Dict[str, int]:
    features = {"confidence": int(round(edge.confidence * 100.0))}
    features.update(_bucket_evidence(edge.evidence))
    features.update(_bucket_target(edge.callee))
    features["historically_observed"] = 1 if (edge.caller, edge.callee) in known_observed else 0
    features["target_observed"] = 1 if any(callee == edge.callee for _, callee in known_observed) else 0
    return features


@dataclass
class UncertaintyPrediction:
    edge: EdgeInfo
    score: float
    model: str = f"{MODEL_NAME}:{MODEL_VERSION}"
    model_kind: str = "heuristic"
    features: Dict[str, int] = field(default_factory=dict)


class HeuristicScorer:
    """Deterministic zero-dependency scorer.

    Readout: logistic(theta . features) with hand-set weights derived
    from the evidence hierarchy. Calibrated on the receipt corpus
    structure, not fitted per project.
    """

    WEIGHTS: Dict[str, float] = {
        "confidence": 0.0015,
        "evidence_config": 0.5,
        "evidence_cli": 0.9,
        "evidence_toml": 0.55,
        "evidence_interface": -1.2,
        "evidence_platform": 0.3,
        "target_github": 0.0,
        "target_gitlab": 0.0,
        "target_bitbucket": 0.0,
        "target_git": 0.2,
        "target_pypi_or_docs": -0.35,
        "historically_observed": -2.4,
        "target_observed": 1.4,
    }
    BIAS = 0.4
    # Interaction: config-only evidence with zero platform history is a weak
    # hypothesis (deployment was never observed for that target anywhere).
    WEAK_NO_HISTORY_PENALTY = 1.4

    def score(self, features: Dict[str, int]) -> float:
        linear = self.BIAS + sum(self.WEIGHTS.get(name, 0.0) * float(value)
                                 for name, value in features.items())
        if (features.get("evidence_config") and not features.get("target_observed")
                and not features.get("historically_observed")):
            linear -= self.WEAK_NO_HISTORY_PENALTY
        return _sigmoid(linear)


class RandomForestScorer:
    """Optional sklearn-based classifier over past receipt outcomes."""

    model_kind = "random_forest"

    def __init__(self, n_estimators: int = 120, random_state: int = 42) -> None:
        self._n_estimators = n_estimators
        self._random_state = random_state
        self._pipeline: Optional[Any] = None

    @staticmethod
    def available() -> bool:
        try:
            import sklearn  # noqa: F401
            return True
        except ImportError:
            return False

    def fit(self, x: List[Dict[str, int]], y: List[int]) -> None:
        if not y or all(label == y[0] for label in y):
            raise ValueError("random forest needs both classes present "
                             "(observed edges and unobserved candidates)")
        try:
            from sklearn.ensemble import RandomForestClassifier
        except ImportError as exc:
            raise ValueError(f"sklearn unavailable: {exc}") from exc
        order = list(FEATURE_NAMES)
        matrix = [[row[name] for name in order] for row in x]
        self._pipeline = RandomForestClassifier(
            n_estimators=self._n_estimators, random_state=self._random_state,
            class_weight="balanced")
        self._pipeline.fit(matrix, y)

    def score(self, features: Dict[str, int]) -> float:
        if self._pipeline is None:
            raise ValueError("model not fitted; call fit() first")
        order = list(FEATURE_NAMES)
        row = [features.get(name, 0) for name in order]
        probabilities = self._pipeline.predict_proba([row])[0]
        return float(probabilities[-1])


def _sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    exp_x = math.exp(x)
    return exp_x / (1.0 + exp_x)


def predict_uncertain_edges(
    candidate_edges: Sequence[EdgeInfo],
    known_observed: set,
    config: Optional[Config] = None,
    min_confidence: float = 0.5,
    scorer: Optional[Any] = None,
) -> List[UncertaintyPrediction]:
    """Predict outcome probabilities for candidate edges.

    Never returns information presented as fact: every result is a
    ``predicted`` edge with model provenance and the feature vector.
    """
    chosen_scorer = scorer or HeuristicScorer()
    predictions: List[UncertaintyPrediction] = []
    for edge in candidate_edges:
        features = featurize(edge, known_observed)
        score = float(chosen_scorer.score(features))
        if score < min_confidence:
            continue
        predictions.append(UncertaintyPrediction(
            edge=edge, score=score, features=features,
            model_kind=getattr(chosen_scorer, "model_kind", "heuristic"),
        ))
    predictions.sort(key=lambda p: p.score, reverse=True)
    return predictions


def prediction_edges(predictions: Sequence[UncertaintyPrediction],
                     provenance_version: str = MODEL_VERSION) -> List[EdgeInfo]:
    """Convert predictions into EdgeInfo records (kind=predicted)."""
    edges: List[EdgeInfo] = []
    for prediction in predictions:
        edges.append(EdgeInfo(
            caller=prediction.edge.caller,
            callee=prediction.edge.callee,
            kind=KIND_PREDICTED,
            evidence=f"model:{prediction.model}",
            confidence=round(prediction.score, 4),
            provenance=prediction.model,
        ))
    return edges
