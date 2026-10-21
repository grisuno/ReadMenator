"""Release receipts ingest contract: deploys as first-class evidence.

deploynator writes `release-receipts/*.json` receipts. This contract
loads them, extracts observed edges (caller -> callee with exit codes
and provenance), reconciles candidate edges (feasible sets from
config/CLI/interface) against observed ones, and renders a release
history page plus an edge-reconciliation JSON artifact.

Golden rule: only `observed` edges are facts. `candidate` edges were
never executed (feasible-set hypotheses from config); `predicted`
edges come from the uncertainty engine and are always labeled with
model version and confidence.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Sequence, Tuple

from readmenator._config import Config

RECEIPT_SCHEMA_PREFIX = "deploynator/receipt@"

KIND_OBSERVED = "observed"
KIND_CANDIDATE = "candidate"
KIND_PREDICTED = "predicted"

_MODE_RUN = "run"
_MODE_PLAN = "plan"

EDGES_JSON_NAME = "release-edges.json"
RELEASES_PAGE_NAME = "RELEASES.md"

_PLATFORM_CLI_PREFIX = {"gh": "GitHubCLI", "glab": "GitLabCLI", "bb": "BitbucketCLI"}
_GIT_VERB_EDGE = {"commit": "GitOperations.commit", "tag": "GitOperations.tag",
                  "push": "GitOperations.push"}


@dataclass
class ReleaseReceiptRecord:
    """A parsed deploynator release receipt."""

    project: str
    source_path: str
    mode: str
    status: str
    version_from: str = ""
    version_to: str = ""
    tag: str = ""
    commit: str = ""
    branch: str = ""
    error: str = ""
    created_at: str = ""
    duration_ms: int = 0
    platforms: List[Dict[str, Any]] = field(default_factory=list)
    steps: List[Dict[str, Any]] = field(default_factory=list)
    commands: List[Dict[str, Any]] = field(default_factory=list)
    edges: List[Dict[str, Any]] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any], source_path: str) -> "ReleaseReceiptRecord":
        schema = str(data.get("schema", ""))
        if not schema.startswith(RECEIPT_SCHEMA_PREFIX):
            raise ValueError(f"Unknown receipt schema: {schema!r} ({source_path})")
        if not data.get("project"):
            raise ValueError(f"Receipt without project: {source_path}")
        return cls(
            project=str(data["project"]),
            source_path=source_path,
            mode=str(data.get("mode", _MODE_RUN)),
            status=str(data.get("status", "")),
            version_from=str(data.get("version_from", "")),
            version_to=str(data.get("version_to", "")),
            tag=str(data.get("tag", "")),
            commit=str(data.get("commit", "")),
            branch=str(data.get("branch", "")),
            error=str(data.get("error", "")),
            created_at=str(data.get("created_at", "")),
            duration_ms=int(data.get("duration_ms", 0) or 0),
            platforms=list(data.get("platforms", [])) or [],
            steps=list(data.get("steps", [])) or [],
            commands=list(data.get("commands", [])) or [],
            edges=list(data.get("edges", [])) or [],
        )


@dataclass(frozen=True)
class EdgeInfo:
    """One evidence edge: caller -> callee with provenance."""

    caller: str
    callee: str
    kind: str
    evidence: str
    confidence: float
    provenance: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "caller": self.caller, "callee": self.callee, "kind": self.kind,
            "evidence": self.evidence, "confidence": self.confidence,
            "provenance": self.provenance,
        }


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class ReceiptIngestor:
    """Loads release receipts and reconciles their evidence edges."""

    def __init__(self, config: Optional[Config] = None) -> None:
        self._config = config or Config()

    # Loading ---------------------------------------------------------

    def load_file(self, path: str) -> ReleaseReceiptRecord:
        if os.path.islink(path):
            raise ValueError(f"Symlink rejected: {path}")
        size_limit = int(self._config.MAX_FILE_SIZE_MB * 1024 * 1024)
        if os.path.getsize(path) > size_limit:
            raise ValueError(f"Receipt too large: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not data:
            raise ValueError(f"Empty receipt: {path}")
        record = ReleaseReceiptRecord.from_dict(data, path)
        return record

    def load_dir(self, receipts_dir: str) -> List[ReleaseReceiptRecord]:
        base = receipts_dir or self._config.RECEIPTS_SCAN_DIR
        if os.path.islink(base):
            raise ValueError(f"Symlink rejected: {base}")
        if not os.path.isdir(base):
            return []
        records: List[ReleaseReceiptRecord] = []
        for entry in sorted(os.listdir(base)):
            if not entry.endswith(".json") or entry.startswith("."):
                continue
            path = os.path.join(base, entry)
            try:
                records.append(self.load_file(path))
            except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
                continue
        limit = self._config.RECEIPTS_MAX_HISTORICAL
        if len(records) > limit:
            records = records[-limit:]
        return records

    # Edges -----------------------------------------------------------

    def observed_edges(self, records: Sequence[ReleaseReceiptRecord]) -> List[EdgeInfo]:
        """Observed facts: explicit receipt edges plus command-derived ones."""
        edges: List[EdgeInfo] = []
        for record in records:
            version = record.version_to or record.tag or record.version_from
            provenance = f"receipt:{record.project}/{version or record.source_path}"
            for raw in record.commands:
                derived = _edge_from_command(raw, provenance)
                if derived is not None:
                    edges.append(derived)
        edges.extend(self._explicit_edges(records))
        return _dedupe(edges)

    def candidate_edges(self, records: Sequence[ReleaseReceiptRecord]) -> List[EdgeInfo]:
        """Feasible-set edges (kind=candidate) declared by receipts."""
        edges: List[EdgeInfo] = []
        for record in records:
            for raw in record.edges:
                if raw.get("kind") == KIND_CANDIDATE:
                    edges.append(EdgeInfo(
                        caller=str(raw.get("caller", "")),
                        callee=str(raw.get("callee", "")),
                        kind=KIND_CANDIDATE,
                        evidence=str(raw.get("evidence", "")),
                        confidence=float(raw.get("confidence", 0.0) or 0.0),
                        provenance=f"receipt:{record.project}",
                    ))
        return _dedupe(edges)

    def _explicit_edges(self, records: Sequence[ReleaseReceiptRecord]) -> List[EdgeInfo]:
        edges: List[EdgeInfo] = []
        for record in records:
            for raw in record.edges:
                if raw.get("kind") == KIND_OBSERVED:
                    edges.append(EdgeInfo(
                        caller=str(raw.get("caller", "")),
                        callee=str(raw.get("callee", "")),
                        kind=KIND_OBSERVED,
                        evidence=str(raw.get("evidence", "")),
                        confidence=float(raw.get("confidence", 1.0) or 1.0),
                        provenance=str(raw.get("provenance", "")) or f"receipt:{record.project}",
                    ))
        return _dedupe(edges)


def _edge_from_command(raw: Dict[str, Any], provenance: str) -> Optional[EdgeInfo]:
    argv = raw.get("command") or []
    if not argv:
        return None
    head = str(argv[0])
    stage = str(raw.get("stage", ""))
    kind = raw.get("kind")
    if kind and kind != KIND_OBSERVED:
        return None
    if raw.get("exit_code") is None and not raw.get("exception"):
        return None
    cli_name = _PLATFORM_CLI_PREFIX.get(head)
    parts = [str(p) for p in argv[1:]]
    if cli_name:
        if "release" in parts and "create" in parts:
            callee = f"{cli_name}.create_release"
        elif "release" in parts and "upload" in parts:
            callee = f"{cli_name}.upload_release_assets"
        else:
            callee = f"{cli_name}._run"
        caller = _caller_from_stage(stage, "DeployOrchestrator.deploy")
        evidence = f"command:{stage or head}"
        return EdgeInfo(caller=caller, callee=callee, kind=KIND_OBSERVED,
                        evidence=evidence, confidence=1.0, provenance=provenance)
    if head == "git":
        verb = next((v for v in _GIT_VERB_EDGE if v in parts[:4]), None)
        if verb is None:
            return None
        caller = _caller_from_stage(stage, "DeployOrchestrator.deploy")
        return EdgeInfo(caller=caller, callee=_GIT_VERB_EDGE[verb], kind=KIND_OBSERVED,
                        evidence=f"command:{stage or 'git:' + verb}", confidence=1.0,
                        provenance=provenance)
    return None


_STAGE_CALLERS = {
    "gh_release": "DeployOrchestrator._gh_release_in_repo",
    "pypi": "DeployOrchestrator.deploy",
    "deb": "DeployOrchestrator.deploy",
    "commit": "DeployOrchestrator.deploy",
    "tag": "DeployOrchestrator.deploy",
    "tests": "DeployOrchestrator.deploy",
    "docs": "DeployOrchestrator.deploy",
}


def _caller_from_stage(stage: str, default: str) -> str:
    if not stage:
        return default
    if stage.startswith("release:"):
        return "Platform.create_release"
    if stage.startswith("assets:"):
        return "Platform.upload_release_assets"
    return _STAGE_CALLERS.get(stage, default)


def _dedupe(edges: List[EdgeInfo]) -> List[EdgeInfo]:
    seen = set()
    out: List[EdgeInfo] = []
    for edge in edges:
        key = (edge.caller, edge.callee, edge.kind, edge.evidence)
        if key in seen:
            continue
        seen.add(key)
        out.append(edge)
    return out


class ReceiptsReconciler:
    """Reconciles candidate vs observed edges and renders artifacts."""

    def __init__(self, config: Optional[Config] = None) -> None:
        self._ingestor = ReceiptIngestor(config)
        self._config = config or Config()

    def reconcile(
        self,
        records: Sequence[ReleaseReceiptRecord],
        candidate_edges: Sequence[EdgeInfo] = (),
        predicted_edges: Sequence[EdgeInfo] = (),
    ) -> Dict[str, Any]:
        observed = self._ingestor.observed_edges(records)
        covered = {(e.caller, e.callee) for e in observed}
        candidates = list(candidate_edges) or self._ingestor.candidate_edges(records)
        unobserved = [e for e in candidates if (e.caller, e.callee) not in covered]
        confirmed = [e for e in candidates if (e.caller, e.callee) in covered]
        now = _now_iso()
        report = {
            "generated_at": now,
            "receipts": [
                {
                    "project": r.project, "status": r.status, "mode": r.mode,
                    "version_from": r.version_from, "version_to": r.version_to,
                    "tag": r.tag, "commit": r.commit, "error": r.error,
                    "platforms": r.platforms,
                    "source": r.source_path,
                }
                for r in records
            ],
            "observed_edges": [e.to_dict() for e in observed],
            "confirmed_candidates": [e.to_dict() for e in confirmed],
            "unobserved_candidates": [e.to_dict() for e in unobserved],
            "predicted_edges": [e.to_dict() for e in predicted_edges],
        }
        return report

    def releases_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = ["# Release history (receipts)", ""]
        lines.append(f"_Generated {report['generated_at']} (zero LLM tokens, offline)._")
        lines.append("")
        for receipt in report["receipts"]:
            title = _receipt_title(receipt)
            lines.append(f"## {title}")
            lines.append("")
            if receipt["commit"]:
                lines.append(f"- commit: `{receipt['commit']}`")
            platforms = _format_receipt(receipt)
            for entry in platforms:
                lines.append(f"- {entry}")
            if receipt["error"]:
                lines.append(f"- error: `{receipt['error']}`")
            lines.append("")
        lines.extend(_edges_section(report["observed_edges"], "Observed edges (facts)"))
        lines.extend(_edges_section(report["unobserved_candidates"],
                                    "Unobserved candidates (feasible set, not executed)"))
        lines.extend(_edges_section(report["predicted_edges"],
                                    "Predicted edges (model hypotheses)"))
        return "\n".join(lines) + "\n"

    def write_pages(self, report: Dict[str, Any], target_dir: str,
                    out_dirname: str = "") -> str:
        root = os.path.abspath(target_dir)
        out_dir = os.path.join(root, out_dirname or self._config.RELEASES_DIR)
        if os.path.islink(out_dir):
            raise ValueError(f"Symlink rejected: {out_dir}")
        os.makedirs(out_dir, exist_ok=True)
        edges_path = os.path.join(out_dir, EDGES_JSON_NAME)
        with open(edges_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        page_path = os.path.join(out_dir, RELEASES_PAGE_NAME)
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(self.releases_markdown(report))
        return out_dir


def _receipt_title(receipt: Dict[str, Any]) -> str:
    project = receipt["project"]
    version_to = receipt.get("version_to") or receipt.get("tag") or "?"
    version_from = receipt.get("version_from") or "?"
    status = receipt.get("status") or "?"
    return f"{project} {version_from} → {version_to} [{status}]"


def _format_receipt(receipt: Dict[str, Any]) -> List[str]:
    entries: List[str] = []
    platforms = receipt.get("platforms") or []
    for platform in platforms:
        enabled = platform.get("enabled")
        pushed = platform.get("pushed")
        released = platform.get("released")
        label = platform.get("platform", "?")
        state = ("disabled" if not enabled else
                 f"pushed={_opt(pushed)}, released={_opt(released)}")
        error = platform.get("error") or ""
        suffix = f" — `{error}`" if error else ""
        entries.append(f"platform {label}: {state}{suffix}")
    return entries


def _opt(value: Any) -> str:
    if value is None:
        return "n/a"
    return "yes" if value else "no"


def _edges_section(edges: List[Dict[str, Any]], title: str) -> List[str]:
    if not edges:
        return []
    lines: List[str] = [f"## {title}", ""]
    for edge in edges[:50]:
        lines.append(
            f"- {edge['caller']} → {edge['callee']} "
            f"[evidence: {edge['evidence']}, conf: {edge['confidence']:.2f}, "
            f"provenance: {edge['provenance']}]"
        )
    if len(edges) > 50:
        lines.append(f"- ... and {len(edges) - 50} more")
    lines.append("")
    return lines
